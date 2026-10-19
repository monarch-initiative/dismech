---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-18T04:55:30.387262'
end_time: '2026-10-18T04:59:59.639215'
duration_seconds: 269.25
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hyper-IgM Syndrome Type 5
  mondo_id: MONDO:0011971
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
citation_count: 54
reference_validation:
  total_references: 22
  verified: 21
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.045
  relevance_assessed: 21
  on_topic: 9
  off_topic: 1
  off_topic_references:
  - PMC:PMC2952935
  unresolved_references:
  - DOI:10.1371/journal.ppat.1003361&type=printable
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 43
  verified: 40
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 18
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: DOID:0060759
    reported_labels:
    - Disease Ontology
    ontology_label: immunodeficiency with hyper IgM type 5
  labels_variant: 1
  obsolete_terms:
  - term_id: HP:0002845
    ontology_label: obsolete Increased proportion of peripheral CD3+ T cells
    replaced_by: HP:0002851
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hyper-IgM Syndrome Type 5
- **MONDO ID:** MONDO:0011971 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hyper-IgM Syndrome Type 5** covering all of the
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

# Hyper-IgM syndrome type 5 — comprehensive disease-characteristics report

**Disease:** Hyper-IgM syndrome type 5  
**Preferred molecular name:** UNG-related immunodeficiency / hyper-IgM syndrome due to uracil-DNA glycosylase deficiency  
**MONDO:** MONDO:0011971  
**Category:** Mendelian, predominantly antibody deficiency  
**Report date:** October 18, 2026

## Executive summary

Hyper-IgM syndrome type 5 (HIGM5) is an **extremely rare autosomal-recessive, B-cell-intrinsic immunodeficiency caused by biallelic loss-of-function variants in `UNG`**. UNG normally removes activation-induced cytidine deaminase (AID)-generated uracil from immunoglobulin DNA. Its absence profoundly impairs immunoglobulin class-switch recombination (CSR), leaving affected people with normal or elevated IgM but markedly reduced IgG and IgA, deficient class-switched memory B cells, poor specific antibody responses, recurrent bacterial—especially sinopulmonary—infections, and lymphoid hyperplasia. T-cell immunity and total B-cell numbers are usually preserved, so opportunistic infection and neutropenia are not characteristic, unlike CD40/CD40L-pathway hyper-IgM disorders. [2][193][445]

The evidence base is unusually small. The landmark report described three patients (PMID: **12958596**), a large 140-patient hyper-IgM cohort found only one UNG-deficient individual (0.7%; PMID: **15358621**), and a 2022 report added a 40-year-old patient with a novel biallelic insertion (PMID: **35879489**). Thus, phenotype frequencies, penetrance, survival and treatment-response percentages cannot be estimated reliably. [31][449][148]

---

# 1. Disease information

## 1.1 Definition and classification

HIGM5 is a primary immunodeficiency in which impaired UNG-mediated processing of uracil in activated B-cell immunoglobulin loci causes a severe CSR defect. Immunologically, the defining pattern is:

- markedly decreased or absent IgG and IgA, often also IgE;
- normal or elevated—often substantially elevated—IgM;
- normal overall B-cell numbers;
- markedly reduced or absent class-switched memory B cells;
- poor antigen-specific IgG responses;
- recurrent bacterial infections and lymphoid hyperplasia.

The 2024 IUIS classification places **UNG deficiency** under “predominantly antibody deficiencies,” specifically “severe reduction in serum IgG and IgA with normal/elevated IgM and normal numbers of B cells.” [193][199]

## 1.2 Identifiers and synonyms

| Resource | Identifier/name |
|---|---|
| MONDO | **MONDO:0011971**, hyper-IgM syndrome type 5 |
| OMIM disease | **608106**, Immunodeficiency with hyper-IgM, type 5 |
| OMIM gene | **191525**, UNG |
| Orphanet | **ORPHA:101092** |
| Disease Ontology | **DOID:0060759** |
| MeSH | **D053306**, Hyper-IgM Immunodeficiency Syndrome |
| ICD-10 | **D80.5**, Immunodeficiency with increased immunoglobulin M |
| ICD-11 | **4A01.05**, Immunodeficiency with hyper-IgM; Orphanet also maps the non-opportunistic HIGM grouping to 4A01.1Y |
| SNOMED CT | **1351569004**, autosomal-recessive hyperimmunoglobulin M syndrome due to UNG deficiency |
| MedGen/UMLS | **C1720958** |
| GARD | **10581** |
| HGNC gene | **HGNC:12572**, `UNG` |
| NCBI Gene | **7374** |
| Ensembl | **ENSG00000076248** |
| UniProt | **P13051** |

The ICD and MeSH terms are umbrella HIGM codes rather than HIGM5-specific billing codes. [1][3][118][418][419][423]

**Common synonyms**

- HIGM5
- Hyper-IgM syndrome 5
- Hyper-IgM immunodeficiency syndrome type 5
- Immunodeficiency with hyper-IgM, type 5
- Hyper-IgM syndrome due to UNG deficiency
- UNG-related immunodeficiency
- Uracil-DNA glycosylase deficiency
- Hyper-IgM syndrome due to uracil N-glycosylase
- Autosomal-recessive hyper-IgM syndrome due to UNG deficiency [1][99]

## 1.3 Provenance of information

This report concerns an **aggregated disease entity**, not an EHR-derived phenotype. The strongest evidence comes from:

1. individual case reports and very small human cohorts;
2. biochemical studies of patient-derived EBV-transformed B-cell lines;
3. antibody-repertoire sequencing from one UNG-deficient patient;
4. `Ung`-knockout mice and engineered B-cell lines;
5. aggregated resources including OMIM, Orphanet, IUIS, ClinVar, MedGen and MONDO.

---

# 2. Etiology

## 2.1 Causal factor

The established cause is **biallelic germline pathogenic variants in `UNG`**, producing absent, unstable, mistargeted or catalytically nonfunctional uracil-DNA glycosylase. Homozygous and compound-heterozygous genotypes have been documented. No infectious, toxic, nutritional or lifestyle exposure causes HIGM5. [2][31]

`UNG` is located at **12q24.11** and produces two principal isoforms through alternative promoter use and splicing:

- **UNG1:** principally mitochondrial;
- **UNG2:** principally nuclear and particularly important in proliferating and activated B cells.

NCBI Gene assigns `UNG` Gene ID **7374**, HGNC **12572** and Ensembl **ENSG00000076248**. [118][121]

## 2.2 Genetic risk factors

| Risk factor | Evidence and interpretation |
|---|---|
| Two pathogenic `UNG` alleles in trans | Necessary and sufficient cause under the established autosomal-recessive model |
| Consanguinity | Increases the probability that both parents carry the same rare allele; the 39-year-old cohort patient’s parents were first cousins [97] |
| Affected sibling/family history | Each sibling of an affected individual has a 25% recurrence risk when both parents are heterozygous carriers |
| Rare loss-of-function alleles | Frameshift, nonsense and damaging missense alleles have been reported |
| Population-specific alleles | Possible, but no replicated founder mutation has been established |
| Sex | Both sexes are genetically susceptible; unlike CD40LG deficiency, HIGM5 is not X-linked |

## 2.3 Environmental and infectious risk modifiers

Environment does not initiate the genetic disorder, but exposure to **encapsulated respiratory bacteria** determines when and how severely antibody failure becomes clinically evident. Crowding, daycare, smoke exposure, chronic airway disease and delayed access to immunoglobulin replacement are plausible severity modifiers, but none has been formally quantified in HIGM5.

The principal reported infections are upper and lower respiratory bacterial infections. Opportunistic infection is generally not increased because T-cell and myeloid CD40 signaling remain intact. [75][113][421]

## 2.4 Protective factors

No protective `UNG` allele has been established. Clinically protective measures include:

- early diagnosis;
- regular IgG replacement;
- prompt culture-directed antibiotics;
- prophylactic antibiotics if infections persist;
- vaccination of close contacts;
- reduction of respiratory pathogen and tobacco-smoke exposure;
- surveillance for bronchiectasis and lymphoproliferation.

Residual activity or compensation by SMUG1 might moderate severity, but this is chiefly model-organism evidence. Human patient B-cell lines showed that SMUG1 could not compensate effectively for UNG loss. [116][448]

## 2.5 Gene–environment interaction

The genotype creates deficient switched-antibody production; pathogen exposure then reveals the phenotype. Maternal IgG may temporarily protect infants, while recurrent respiratory exposure progressively produces airway injury. This is not a classic toxicogenomic interaction and no formal HIGM5 G×E study has been published.

---

# 3. Phenotypes

Because only a handful of molecularly confirmed patients have been described, **valid percentages are unavailable**. Frequencies below are therefore qualitative.

| Phenotype and type | Typical characteristics | Suggested HPO term |
|---|---|---|
| Hyper-IgM laboratory phenotype | Normal/elevated IgM; persistent; often marked | **HP:0003496**, Increased circulating IgM |
| Low IgG | Severe, persistent; central diagnostic abnormality | **HP:0004315**, Decreased circulating IgG |
| Low/absent IgA | Severe, persistent | **HP:0002720**, Decreased circulating IgA |
| Low IgE | Expected from CSR failure; incompletely reported in individual cases | **HP:0003212**, Decreased circulating IgE |
| Impaired class-switch recombination | Severe; patient B cells fail to generate normal IgG/IgA despite activation | **HP:0002959**, Impaired immunoglobulin class-switch recombination |
| Reduced class-switched memory B cells | Marked or absent; one repertoire-study patient had 0.7% versus a reference range of 6.5–29.1% | **HP:0032137**, Decreased class-switched memory B cells |
| Poor vaccine-specific antibody response | Persistent; abnormal pneumococcal antibody response documented | **HP:0032126**, Abnormality of specific antibody response |
| Recurrent bacterial infections | Usually childhood or adolescent onset; episodic; variable severity | **HP:0002718**, Recurrent bacterial infections |
| Recurrent upper/lower respiratory infection | Sinusitis, otitis, bronchitis or pneumonia; major morbidity | **HP:0200117**, Recurrent upper and lower respiratory tract infections |
| Lymphadenopathy | Chronic or recurrent lymphoid hyperplasia; common in the AID/UNG HIGM subgroup | **HP:0002716**, Lymphadenopathy |
| Splenomegaly | Reported as part of the autosomal-recessive HIGM lymphoid-hyperplasia phenotype; exact HIGM5 frequency unknown | **HP:0001744**, Splenomegaly |
| Tonsillar/adenoidal hypertrophy | May produce snoring or obstructive symptoms; subgroup-level evidence | **HP:0030817**, Tonsillar hypertrophy |
| Pulmonary lymphoid hyperplasia | Documented in one adult UNG-deficient patient and progressive despite IVIG | **HP:0006535**, Abnormal pulmonary interstitial morphology / use a more specific local term if available |
| Epididymitis | Documented in one adult patient; very rare | **HP:0000031**, Epididymitis |
| Sjögren syndrome/autoimmunity | Documented in one adult; autoimmune disease is considered a possible AID/UNG feature | **HP:0002814**, Abnormality of the immune system; annotate Sjögren syndrome separately |
| Normal total B-cell count | Distinguishes HIGM5 from agammaglobulinemias | **HP:0002845**, Normal B-cell count, if supported by local ontology |
| Absence of neutropenia | Negative distinguishing feature rather than phenotype | Do not encode as a positive HPO phenotype |
| No characteristic behavioral phenotype | No consistent neurobehavioral manifestation reported | Not applicable |

The landmark cases had bacterial susceptibility, lymphoid hyperplasia, elevated IgM and profoundly decreased IgG/IgA. [61] The best-described adult became symptomatic at 15 years and had IgM **785 mg/dL**, IgG **209 mg/dL**, IgA **<6.7–7 mg/dL**, abnormal pneumococcal responses, chronic epididymitis, Sjögren syndrome and pulmonary lymphoid hyperplasia. [442]

### Quality-of-life impact

No HIGM5-specific EQ-5D, SF-36 or PROMIS study exists. Expected burdens include recurrent illness and hospitalization, chronic airway symptoms, fatigue, missed education/work, regular IVIG/SCIG administration and anxiety concerning infection and hereditary risk. Home SCIG may reduce travel and scheduling burden, but comparative HIGM5 quality-of-life data are unavailable.

---

# 4. Genetic and molecular information

## 4.1 Causal gene

| Field | Value |
|---|---|
| Symbol | `UNG` |
| Full name | Uracil DNA glycosylase |
| HGNC | HGNC:12572 |
| NCBI Gene | 7374 |
| OMIM | 191525 |
| Ensembl | ENSG00000076248 |
| UniProt | P13051 |
| Chromosome | 12q24.11 |
| Inheritance | Autosomal recessive |
| Molecular consequence | Loss of nuclear UNG activity, usually loss of function |

## 4.2 Reported disease-associated variants

The transcript used by modern ClinVar records is frequently **NM_080911.3**; older publications used different numbering, so legacy and current descriptions should not be mixed without transcript normalization.

| Variant | Type/genotype | Classification/evidence | Functional consequence |
|---|---|---|---|
| **NM_080911.3:c.392del; p.Pro131HisfsTer13**; legacy “462delC” | Frameshift; reported in compound heterozygosity and later as homozygous in a repertoire-study patient | ClinVar pathogenic, Variation ID **12290**; PMID 12958596 | Premature termination; absent/disrupted protein |
| **NM_080911.3:c.572_573del; p.Glu191fs**; legacy “639delTA” | Frameshift, compound-heterozygous partner | ClinVar pathogenic, Variation ID **12291** | Truncation, catalytic-domain loss |
| **NM_080911.3:c.752T>C; p.Phe251Ser**, rs104894380 | Homozygous missense | ClinVar pathogenic, Variation ID **12292** | Catalytically active in bacteria but poorly expressed, mistargeted toward mitochondria and degraded in mammalian cells |
| **NM_080911.3:c.428_429del; p.Ile143fs**; legacy “497_498delAT” | Homozygous frameshift | ClinVar pathogenic, Variation ID **12293** | Premature termination around residue 159 |
| **c.924_925insGG**, transcript as reported | Homozygous insertion | Novel in a 40-year-old patient; PMID 35879489 | Predicted frameshift/loss of function; transcript normalization and independent replication needed |
| **c.685C>T; p.Arg229Ter**, rs772214871 | Nonsense | ClinVar pathogenic, Variation ID **578381** | Predicted nonsense-mediated decay or truncated protein |
| **c.730C>T; p.Gln244Ter**, rs751126274 | Nonsense | ClinVar pathogenic submission | Predicted loss of function |
| **c.371A>G; p.His124Arg** | Missense | ClinVar VUS | Insufficient evidence; not diagnostic by itself |
| **c.*537G>A** | 3′ UTR | ClinVar VUS | No published disease evidence |

The two original truncating variants and F251S all affected the catalytic domain; protein was absent from patient B-cell lines, indicating instability or degradation. [46][47][61][116]

The F251S allele is exceptionally rare: gnomAD v4 exomes reported **4/595,596 alleles**, global allele frequency about **7×10⁻⁶**, with no evidence of homozygotes in the cited summary. [253]

**Important curation caution:** ClinVar contains many `UNG` submissions attached to the disease record, including benign and uncertain variants. Only biallelic variants with appropriate segregation, rarity and functional/clinical evidence should be considered causal.

## 4.3 Origin and mechanism

- Origin: **germline**, not somatic.
- Disease mechanism: predominantly **biallelic loss of function**.
- No established dominant-negative or gain-of-function HIGM5 mechanism.
- No recurrent pathogenic aneuploidy, translocation or large chromosomal rearrangement has been established.
- Copy-number deletions encompassing `UNG` are theoretically detectable but are not a recognized common mechanism.

## 4.4 Modifier genes and epigenetics

No human modifier gene has been validated. Candidate compensatory or interacting factors include:

- `SMUG1`, a backup uracil glycosylase;
- `MSH2`/`MSH6`, mismatch-repair pathway;
- `APE1`/`APEX1` and `APEX2`, AP-site processing;
- `RPA1`/`RPA2`/`RPA3`, recruitment to single-stranded DNA;
- `PCNA`, replication-associated recruitment;
- `POLH`, error-prone synthesis;
- `FAM72A`, which regulates UNG2 abundance during antibody diversification.

These are mechanistic candidates, not clinically validated severity modifiers.

No reproducible HIGM5-specific DNA-methylation, histone-mark, chromatin or episignature has been reported.

---

# 5. Environmental information

| Domain | Current evidence |
|---|---|
| Toxins, radiation, pollution | No evidence that they cause HIGM5 |
| Smoking/air pollution | Plausibly aggravate respiratory morbidity but not studied specifically |
| Diet, alcohol, exercise | No demonstrated effect on disease occurrence |
| Occupational exposure | No established association |
| Infectious agents | Primarily bacterial respiratory pathogens act as complications, not causes |
| Opportunistic pathogens | Not characteristically increased in isolated UNG deficiency |
| Gene–environment studies | None specific to HIGM5 |

Encapsulated organisms such as *Streptococcus pneumoniae* and *Haemophilus influenzae* are biologically expected in severe antibody deficiency, although organism-level frequencies have not been published for HIGM5.

---

# 6. Mechanism and pathophysiology

## 6.1 Ordered causal chain

1. **Biallelic pathogenic `UNG` variants lead to** absent, unstable, mistargeted or nonfunctional nuclear UNG protein in activated B cells.  
2. **Loss of nuclear UNG leads to** failure to efficiently excise AID-generated uracil from transcribed immunoglobulin switch-region single-stranded DNA.  
3. **Failure of uracil excision results in** markedly reduced formation of abasic/AP sites and the correctly positioned DNA nicks and staggered double-strand breaks needed for CSR.  
4. **Reduced switch-region DNA cleavage leads to** profound failure of recombination from `Cμ` to `Cγ`, `Cα` or `Cε`.  
5. **CSR failure results in** predominant IgM production, severe IgG/IgA/IgE deficiency and loss of class-switched memory B cells.  
6. **Deficient IgG/IgA and antigen-specific antibodies lead to** impaired opsonization and mucosal/systemic bacterial defense.  
7. **Impaired bacterial defense results in** recurrent sinopulmonary and other bacterial infections, with potential downstream bronchiectasis and chronic lung damage.  
8. **Persistent germinal-center activation in the face of ineffective switching leads to** lymphadenopathy, splenomegaly and tonsillar or pulmonary lymphoid hyperplasia; the exact link to autoimmunity is partly inferred.  
9. **In parallel, unrepaired uracil leads to** altered somatic-hypermutation spectra—especially excess G:C transitions and reduced G:C transversions—and elevated genomic uracil.  
10. **Elevated genomic uracil may lead to** genomic instability; a direct quantitative human HIGM5 cancer risk has not been demonstrated.

## 6.2 Upstream molecular lesion

AID converts cytosine to uracil at transcribed immunoglobulin switch and variable regions. UNG normally hydrolyzes the uracil–deoxyribose N-glycosidic bond, producing an AP site. AP endonucleases and mismatch-repair proteins then create and process DNA breaks. Nonhomologous end joining joins the donor Sμ region to a downstream switch region, replacing the constant region while retaining antigen specificity.

The original human study summarized the central finding:

> “Recessive mutations of the gene encoding uracil–DNA glycosylase (UNG) are associated with profound impairment in CSR at a DNA precleavage step and with a partial disturbance of the SHM pattern in three patients with hyper-IgM syndrome.”  
> — Imai et al., *Nature Immunology*, published September 7, 2003; PMID **12958596**, DOI [10.1038/ni974](https://doi.org/10.1038/ni974). [31][58]

## 6.3 Protein dysfunction and cellular processes

Patient B-cell studies showed:

- >99% of normal high-turnover ssDNA uracil-excision activity is attributable to UNG;
- patient P2 retained only approximately **0.4%** of normal activity;
- purified F251S UNG had nearly normal catalytic activity in vitro but was abnormally localized and degraded in mammalian cells;
- patient cell lines accumulated substantial genomic uracil;
- SMUG1 could remove uracil from some U:G or U:A substrates but was approximately **1,000-fold less efficient than UNG2 on ssDNA** and could not compensate in human B cells. [116][448]

The 2005 study’s abstract states:

> “In B cell lines from hyper-IgM patients carrying UNG mutations, the single-strand-specific uracil-DNA glycosylase, SMUG1, cannot complement this function. Moreover, the UNG mutations lead to increased accumulation of genomic uracil.”  
> — Kavli et al., *Journal of Experimental Medicine*, June 20, 2005; PMID **15967827**, DOI [10.1084/jem.20050042](https://doi.org/10.1084/jem.20050042). [448]

## 6.4 Somatic hypermutation

UNG deficiency does not simply abolish all SHM. It changes the mutation spectrum:

- persistence of U:G lesions favors replication-associated G:C transitions;
- reduced AP-site formation reduces transversions at G:C pairs;
- A:T mutation frequency is partly reduced;
- overall SHM frequency can be near normal or reduced depending on assay and repertoire.

Human BCR repertoire sequencing found approximately:

- **4.5-fold fewer G:C transversions**;
- **35% fewer A:T and WA/TW-motif mutations**;
- increased absolute G:C transitions.

That study included only one UNG-deficient patient, so the estimates should not be interpreted as population frequencies. [508]

## 6.5 2023–2024 mechanistic advance: RPA-guided UNG recruitment

A major recent development was demonstration that UNG1 and UNG2 contain an RPA-binding helix that permits access to RPA-coated ssDNA. CRISPR-engineered CH12F3 B cells carrying UNG RPA-binding mutations had approximately **80% lower IgA switching** after stimulation; in an appropriate UNG2-knockout context, RPA-binding-deficient UNG1 produced complete switching failure. Total genomic uracil was not comparably increased, indicating mechanistic separation between RPA-dependent antibody-locus processing and canonical dsDNA BER. [316][319]

> “We show that the UNG:RPA interaction plays a crucial role in both CSR and repair of AID-induced uracil at the Ig loci.”  
> — Hayran et al., *Nucleic Acids Research*, January 25, 2024; PMID **38000394**, DOI [10.1093/nar/gkad1115](https://doi.org/10.1093/nar/gkad1115). [463]

This refines the classical model: HIGM5 is not merely failure of generic DNA repair; it is failure of specialized recruitment and processing of AID-created uracil at activated B-cell immunoglobulin loci.

## 6.6 Suggested ontology annotations

**GO biological process/molecular function**

- GO:0045190 — immunoglobulin class-switch recombination
- GO:0016446 — somatic hypermutation of immunoglobulin genes
- GO:0016445 — somatic diversification of immunoglobulins
- GO:0006284 — base-excision repair
- GO:0006281 — DNA repair
- GO:0004844 — uracil DNA N-glycosylase activity
- GO:0016799 — hydrolase activity, hydrolyzing N-glycosyl compounds
- GO:0002250 — adaptive immune response

**Cell Ontology**

- CL:0000236 — B cell
- CL:0000788 — naive B cell
- CL:0000844 — germinal-center B cell
- CL:0000787 — memory B cell
- CL:0000786 — plasma cell
- CL:0000970 — unswitched memory B cell
- CL:4052108 — IgD-negative class-switched memory B cell

**GO cellular component**

- GO:0005634 — nucleus
- GO:0005739 — mitochondrion
- GO:0005654 — nucleoplasm
- GO:0000785 — chromatin

The key pathway is Reactome **R-HSA-73884, Base Excision Repair**, particularly AP-site formation. [121][368][373][377][478]

## 6.7 Molecular profiling and advanced technologies

| Modality | Disease-specific evidence |
|---|---|
| BCR repertoire sequencing | Available; one UNG-deficient patient, confirming altered SHM spectra [508] |
| Bulk transcriptomics | No replicated HIGM5-specific expression signature |
| Proteomics | No clinical HIGM5 proteomic biomarker |
| Metabolomics/lipidomics | None established |
| Single-cell RNA sequencing | No disease-specific patient study identified |
| Spatial transcriptomics | None |
| Multi-omics | None |
| CRISPR functional genomics | CH12F3 UNG isoform and RPA-binding studies available [314][316] |
| Patient iPSC/organoid models | None established |

---

# 7. Anatomical structures affected

| Level | Structure/cell/compartment | Role |
|---|---|---|
| System | Immune and lymphatic system — UBERON:0002405 | Primary disease system |
| Organ | Lymph node — UBERON:0000029 | Germinal-center B-cell activation; lymphadenopathy |
| Organ | Spleen — UBERON:0002106 | Secondary lymphoid activation; possible splenomegaly |
| Organ | Tonsil/adenoid | Lymphoid hypertrophy; airway obstruction possible |
| Tissue | Bone marrow — UBERON:0002371 | B-cell origin; not the principal site of the CSR lesion |
| Organ | Lung | Recurrent infection, possible bronchiectasis and pulmonary lymphoid hyperplasia |
| Organ | Paranasal sinuses/middle ear | Recurrent bacterial disease |
| Organ | Epididymis | Epididymitis in one patient |
| Cell | Germinal-center/activated B cell — CL:0000844 | Principal functionally affected cell |
| Cell | Class-switched memory B cell | Markedly reduced output |
| Subcellular | Nucleus/nucleoplasm | UNG2-mediated immunoglobulin-locus processing |
| Subcellular | Mitochondrion | UNG1; F251S mutant mistargeting reported |
| Molecular locus | Immunoglobulin heavy-chain switch and variable regions | CSR and SHM substrate |

No consistent lateralization exists. Respiratory and lymphoid involvement is systemic or bilateral rather than unilateral.

---

# 8. Temporal development

- **Biological onset:** congenital, because biallelic variants are present from conception.
- **Clinical onset:** variable; infancy or childhood is possible, but HIGM5 may present later than CD40LG deficiency.
- **Documented late presentation:** one molecularly confirmed man remained asymptomatic until **15 years**, and molecular analysis occurred at age **39**. [442]
- **Course:** chronic lifelong immunodeficiency with episodic infections superimposed on persistent immunoglobulin abnormalities.
- **Progression without adequate treatment:** recurrent infection → cumulative sinus/lung damage → bronchiectasis or chronic pulmonary disease.
- **Lymphoid/autoimmune disease:** may progress despite control of infections, as occurred with Sjögren syndrome and pulmonary lymphoid hyperplasia in one IVIG-treated patient.
- **Remission:** spontaneous molecular remission is not expected. Infection frequency can improve markedly with Ig replacement.
- **Critical intervention window:** before recurrent pneumonia and irreversible airway damage; after identification in an affected family, testing at birth permits presymptomatic management.

No validated disease-stage or staging system exists.

---

# 9. Inheritance and population

## 9.1 Inheritance

| Feature | Assessment |
|---|---|
| Mode | Autosomal recessive |
| Risk to siblings when both parents are carriers | 25% affected, 50% carrier, 25% neither per pregnancy |
| Sex ratio | Expected 1:1 |
| Penetrance | Not numerically established; likely high for severe biallelic loss-of-function genotypes |
| Expressivity | Variable, including childhood versus adolescent/adult onset |
| Anticipation | Not expected |
| Germline mosaicism | Theoretically possible but not reported |
| Consanguinity | Relevant; documented in at least one patient |
| Founder effects | None securely established |
| Carrier phenotype | Heterozygotes are generally expected to be asymptomatic |
| Carrier frequency | Unknown |

## 9.2 Epidemiology

No reliable HIGM5 incidence or prevalence estimate exists; Orphanet lists prevalence as unavailable. [245]

Useful context, not a HIGM5 prevalence estimate:

- A 140-patient HIGM cohort identified **one UNG-deficient patient (0.7%)**. [449]
- The original report included three unrelated patients from France, Japan and the United States. [110]
- A 2022 adult report added another molecular diagnosis. [148]
- In the broad USIDNET HIGM registry, 145 HIGM patients were recorded, but most molecular diagnoses were CD40LG deficiency, not HIGM5. [244]

No ethnicity, geography or demographic group has a demonstrated increased HIGM5 prevalence. Apparent regional clustering is likely to reflect consanguinity, founder alleles or ascertainment.

---

# 10. Diagnostics

## 10.1 Recommended diagnostic sequence

1. **Quantitative serum IgG, IgA, IgM and IgE**, repeated to verify persistence.
2. **Specific antibody responses**, ideally before Ig replacement—e.g., pneumococcal polysaccharide and protein vaccine responses.
3. **CBC with differential**, looking for neutropenia or lymphopenia.
4. **Flow cytometry:** CD3, CD4, CD8, CD19/CD20, NK cells; naive, unswitched and class-switched memory B-cell subsets.
5. **Activated T-cell CD40L expression and CD40-binding assay** to evaluate the more common X-linked form.
6. **Molecular testing** using an HIGM/primary-antibody-deficiency panel including at minimum `CD40LG`, `CD40`, `AICDA` and `UNG`.
7. Confirm candidate variants by orthogonal sequencing and parental segregation.
8. If genetics remain unresolved, consider WES/WGS, copy-number analysis and functional CSR/SHM testing.

Normal CD40L staining does not fully exclude CD40LG dysfunction; ligand-binding assays and sequencing remain important. Patients with normal CD40L expression/binding should be assessed for autosomal-recessive `CD40`, `AICDA` and `UNG` disease. [408]

## 10.2 Expected laboratory findings

| Test | Expected HIGM5 result |
|---|---|
| Serum IgM | Normal or elevated, sometimes markedly |
| Serum IgG | Very low or absent |
| Serum IgA | Very low or absent |
| Serum IgE | Low/absent |
| Total B cells | Usually normal |
| Class-switched memory B cells | Markedly reduced or absent |
| Pneumococcal-specific IgG | Poor |
| T-cell counts/function | Usually preserved |
| Neutrophils | Usually normal |
| In-vitro CSR | Profoundly impaired |
| SHM | Frequency variably reduced; G:C transition bias and reduced transversions |
| UNG protein/activity | Absent or severely reduced in patient B-cell lines |
| Genomic uracil | Elevated in experimental patient B-cell assays |

Routine imaging is not diagnostic, but high-resolution chest CT is indicated for recurrent pneumonia, chronic cough or abnormal pulmonary function to assess bronchiectasis or lymphoid disease.

## 10.3 Genetic-testing modalities

| Modality | Utility |
|---|---|
| Single-gene `UNG` sequencing | Appropriate when phenotype/functional evidence is strongly specific or familial variants are known |
| Multigene HIGM/PAD panel | Preferred first-line molecular test |
| WES | Useful when the panel is negative or phenotype is atypical |
| WGS | Can detect coding, noncoding and structural variants missed by WES; no proven superior HIGM5 diagnostic yield because cases are so rare |
| Deletion/duplication analysis | Add if sequencing finds one allele or suggests a copy-number event |
| CMA | Low yield for isolated HIGM5; not first-line |
| Karyotype/FISH | Not routinely indicated |
| mtDNA testing | Not indicated; `UNG` is nuclear encoded |
| Repeat-expansion testing | Not indicated |
| RNA sequencing | Research/adjunct for suspected splice variants |
| Functional UNG/CSR assay | Specialized research or reference-laboratory confirmation |

GTR lists clinical tests for HIGM5/UNG, but assay availability varies geographically. [500]

## 10.4 Differential diagnosis

| Disorder | Distinguishing features |
|---|---|
| CD40LG deficiency/HIGM1 | X-linked; males; opportunistic infection, neutropenia, cryptosporidial liver disease; abnormal CD40L expression/function |
| `AICDA` deficiency/HIGM2 | Very similar lymphoid hyperplasia and bacterial disease; SHM generally more severely reduced/absent; biallelic `AICDA` variants |
| `CD40` deficiency/HIGM3 | Combined immune defect with opportunistic infection |
| NEMO/`IKBKG` deficiency | Ectodermal dysplasia, infections and broader NF-κB dysfunction |
| PMS2/MSH6/MSH2 defects | CSR/SHM defects plus constitutional mismatch-repair deficiency and cancer predisposition |
| Common variable immunodeficiency | Low IgG/IgA, but IgM often low or normal; heterogeneous genetics; usually less specific CSR pattern |
| X-linked agammaglobulinemia | Very low/absent B cells rather than normal B-cell numbers |
| Secondary hypogammaglobulinemia | Medication, protein loss, malignancy or infection history; no biallelic `UNG` defect |
| Transient hypogammaglobulinemia of infancy | Spontaneous improvement and usually not persistent hyper-IgM |
| Ataxia-telangiectasia/Nijmegen breakage syndrome | Neurologic/syndromic features, radiosensitivity and characteristic laboratory findings |

## 10.5 Screening

There is **no population newborn screen for HIGM5**. TREC-based SCID screening is expected to be normal because T-cell development is preserved. Family-based molecular testing is therefore the principal presymptomatic strategy. [389]

---

# 11. Outcome and prognosis

## 11.1 Disease-specific evidence

No valid five-year survival, ten-year survival, mortality rate or median life expectancy has been calculated for HIGM5. Broad HIGM survival data are dominated by CD40LG deficiency and should not be transferred directly to UNG deficiency.

Prognosis in isolated AID/UNG antibody-switching defects is considered better than in CD40/CD40L disorders because T-cell immunity is preserved. With adequate Ig replacement and infection treatment, patients may live productive adult lives. [166][213]

## 11.2 Major morbidity

- recurrent sinus, ear and lower respiratory infections;
- bronchiectasis and chronic pulmonary impairment;
- chronic lymphadenopathy, splenomegaly or tonsillar hypertrophy;
- pulmonary lymphoid hyperplasia;
- autoimmune disease;
- burden of lifelong Ig replacement and monitoring;
- possible lymphoma or other malignancy risk, although HIGM5-specific incidence is unknown.

The best-described adult had fewer infections after IVIG, but Sjögren syndrome and pulmonary lymphoid hyperplasia continued to progress. [442]

## 11.3 Prognostic factors

Likely favorable:

- early diagnosis;
- initiation of adequate Ig replacement before chronic lung disease;
- adherence to therapy;
- rapid treatment of infection;
- absence of bronchiectasis, autoimmune disease or lymphoproliferation.

Likely adverse:

- delayed diagnosis;
- repeated pneumonia;
- structural lung disease;
- progressive lymphoid or autoimmune complications;
- inability to maintain protective IgG troughs.

No validated prognostic biomarker or calculator exists.

---

# 12. Treatment

## 12.1 Treatment strategy

1. **Begin lifelong IgG replacement** once the diagnosis and clinically significant antibody deficiency are established.
2. Treat acute bacterial infections promptly.
3. Add antimicrobial prophylaxis when infections continue despite optimized Ig replacement.
4. Monitor respiratory status, lymphoid organs and autoimmune complications.
5. Individualize immunosuppression for severe autoimmune/lymphoproliferative disease in an expert center.
6. Do not routinely use HSCT for isolated UNG deficiency outside exceptional circumstances or research protocols.

## 12.2 Current interventions

| Intervention | Use and evidence | Major adverse effects/limitations | Suggested NCIt annotation |
|---|---|---|---|
| IVIG | Mainstay; typically initial total dose around **0.4–0.6 g/kg/month**, individualized by infection burden and trough IgG | Infusion reaction, headache, thrombosis, hemolysis, renal injury, aseptic meningitis | Intravenous Immunoglobulin Therapy |
| SCIG | Equivalent replacement route; weekly or individualized schedules; supports home treatment | Local swelling/pain; frequent administration | Subcutaneous Immunoglobulin Therapy |
| Acute antibiotics | Culture-directed treatment of bacterial respiratory or other infections | Drug-specific toxicity/resistance | Antibiotic Therapy |
| Prophylactic antibiotics | Consider if infections persist despite adequate Ig; azithromycin, amoxicillin or TMP-SMX may be used depending on context | Resistance, allergy, gastrointestinal effects, QT risk for macrolides | Antibiotic Prophylaxis |
| Airway clearance/physiotherapy | For bronchiectasis or chronic secretion burden | Limited HIGM5-specific trial evidence | Respiratory Therapy |
| Autoimmune-disease therapy | Corticosteroids or other immunomodulators tailored to manifestation | Additional infection risk | Immunosuppressive Therapy |
| HSCT | Not routinely recommended for AID/UNG deficiency because the defect is confined largely to antibody production and manageable with Ig replacement | Conditioning toxicity, infection, GVHD, infertility, mortality | Hematopoietic Stem Cell Transplantation |
| Gene/RNA therapy | No approved or HIGM5-specific clinical program | Experimental | Gene Therapy / RNA Therapy |
| Genetic counseling | Recurrence-risk assessment and reproductive options | None intrinsic | Genetic Counseling |

Guidelines for primary antibody deficiency recommend individualized IgRT, commonly beginning around 0.4–0.6 g/kg/month; a trough above approximately 7 g/L is often used as an initial target but clinical infection control is more important than a universal numerical threshold. [230] HIGM guidance specifically identifies Ig replacement as necessary across HIGM forms. [166]

### HSCT nuance

Generic HIGM references sometimes recommend HSCT because they are focused on CD40LG/CD40 deficiency. For **isolated AID or UNG deficiency**, expert patient guidance states that HSCT is not currently recommended because T-cell function is intact and antibody failure can generally be treated with Ig replacement. [166][170]

## 12.3 Treatment outcome evidence

Disease-specific controlled trials do not exist. In the adult cohort patient:

- IVIG **reduced infection frequency**;
- it **did not stop progression** of Sjögren syndrome or pulmonary lymphoid hyperplasia. [442]

No HIGM5-specific response percentage, comparative IVIG-versus-SCIG trial or pharmacogenomic predictor has been reported.

## 12.4 Experimental and clinical-trial activity

No interventional gene, cell, RNA or targeted therapy trial specific to HIGM5 was identified. The relevant current registry study is:

| Study | Type/status | Relevance |
|---|---|---|
| **NCT06092346** — [Prospective Study of the Clinical, Genomic, Pharmacological, Laboratory, and Dietary Determinants of Pyrimidine and Purine Metabolism Disorders](https://clinicaltrials.gov/study/NCT06092346) | Observational natural-history study; started December 19, 2023 | Includes `UNG`/HIGM5 among eligible disorders; not a therapeutic trial [495] |

---

# 13. Prevention

## 13.1 Primary prevention

The disease cannot be prevented by lifestyle modification. Reproductive prevention options after familial-variant identification include:

- carrier testing of relatives;
- partner testing;
- preimplantation genetic testing for monogenic disease;
- prenatal diagnosis by chorionic-villus sampling or amniocentesis;
- use of donor gametes where desired.

## 13.2 Secondary prevention

- Cascade testing of siblings and at-risk relatives.
- Presymptomatic quantitative immunoglobulins and genetic testing in newborn relatives.
- Early Ig replacement before serious infection or bronchiectasis.
- Baseline and periodic pulmonary assessment.

## 13.3 Tertiary prevention

- Maintain adequate Ig replacement.
- Prompt antibiotic treatment.
- Consider antibiotic prophylaxis for breakthrough infection.
- Avoid smoke exposure.
- Airway-clearance therapy when structural lung disease is present.
- Monitor for lymphadenopathy, splenomegaly, autoimmune cytopenia, Sjögren-like disease and lymphoma warning signs.

## 13.4 Immunization

Because HIGM5 preserves T-cell function, vaccine safety should be individualized rather than inferred from combined immunodeficiencies. Nevertheless:

- give indicated **non-live vaccines** where useful, preferably before Ig replacement when diagnostic antibody responses need assessment;
- vaccine effectiveness may be poor owing to CSR failure;
- passive antibodies in IVIG can interfere with measles and varicella vaccine responses;
- live vaccines are commonly avoided in severe antibody deficiency or during Ig replacement, following specialist assessment;
- vaccinate household contacts against influenza, COVID-19, pertussis and other transmissible disease, while avoiding household use of oral poliovirus vaccine where still available.

CDC guidance lists OPV, smallpox, LAIV, BCG, live oral typhoid, yellow fever, MMR/MMRV and dengue live vaccine among contraindications for severe humoral deficiencies and notes uncertain vaccine effectiveness and interference from IVIG. [223]

---

# 14. Other species and natural disease

| Field | Finding |
|---|---|
| Human | *Homo sapiens*, NCBI Taxonomy **9606**; established natural disease |
| Mouse ortholog | `Ung`, NCBI Gene **22256**; experimentally induced knockout models |
| Natural disease in companion/livestock species | No convincing naturally occurring UNG-HIGM5 counterpart identified in OMIA or the veterinary literature searched |
| Breed association | None established; no applicable VBO term |
| Zoonotic potential | None; this is an inherited immunodeficiency |
| Transmission | Mendelian germline transmission, not infectious transmission |

The protein and antibody-diversification mechanism are evolutionarily conserved. Mouse loss of `Ung` reproduces severe CSR impairment and biased SHM, although residual CSR is greater than in the initial human cases, partly because murine SMUG1 can compensate over time. [298][342]

---

# 15. Model organisms and experimental systems

| Model | Type/resource | Phenotype recapitulated | Principal application and limitation |
|---|---|---|---|
| `Ung−/−` mouse | Mammalian knockout; MGI/IMSR-searchable | Substantially impaired CSR; G:C mutations shifted to **95% transitions**; residual switching remains | Landmark proof of the AID→uracil→UNG model; milder CSR defect than human HIGM5 [299] |
| `Ung−/−Smug1−/−` mouse | Double knockout | Further loss of residual IgG1 switching and serum IgG3, IgG2b and IgA | Defines SMUG1 compensation; may overstate pathways differently used in humans [298][470] |
| `Ung−/−Msh2−/−` mouse | Double knockout | Near-complete CSR block and mutation spectrum restricted mainly to transitions at C:G | Separates BER and mismatch-repair contributions |
| CH12F3 mouse B-cell line | In-vitro IgM→IgA-switching model | UNG knockout or inhibition markedly reduces switching | Highly tractable CRISPR system; transformed murine cells do not reproduce whole-patient immunity |
| UNG1/UNG2 isoform-specific CRISPR CH12F3 cells | Functional genomics | Either isoform can support switching in some contexts; dual knockout abolishes switching | Resolves isoform redundancy [314] |
| RPA-binding-helix mutant CH12F3 cells | 2024 CRISPR model | Approximately 80% reduction in IgA-positive cells after stimulation; context-dependent complete failure | Demonstrates RPA-guided recruitment; not yet tied to a human HIGM5 allele [316] |
| Patient EBV-transformed B-cell lines | Human cellular model | Absent UNG activity, excess genomic uracil and failed ssDNA uracil excision | Direct human evidence; EBV transformation may alter expression and metabolism [450] |
| HeLa cells expressing UNG2-F251S | Human in-vitro localization model | Cytoplasmic/mitochondrial mistargeting and poor nuclear accumulation | Explains F251S behavior but is not an activated B cell |
| Human PBMC/BCR repertoire sequencing | Human molecular-profiling model | Reduced G:C transversions and altered A:T mutation pattern | Direct human SHM evidence, but based on one UNG patient [508] |
| DT40 chicken B cells | Avian cellular model | UNG loss/inhibition shifts mutation patterns | Useful for antibody diversification, but species and locus biology differ |

---

# Recent developments and expert assessment

## 2023–2024 priorities

1. **RPA recruitment of UNG:** The 2024 Hayran et al. study established that direct UNG–RPA interaction targets UNG to RPA-coated ssDNA during CSR and AID-lesion repair, while bulk genomic BER remains comparatively RPA-independent. This is the most important recent mechanistic refinement. [463]
2. **Modern CSR synthesis:** A 2024 review emphasizes that UNG is essential to AID-generated uracil processing and that `Ung`-knockout mice produce only approximately 1–2% IgG1-positive splenic B cells under tested conditions. [16][310]
3. **Current IUIS recognition:** The 2024 IUIS update continues to classify UNG deficiency as an autosomal-recessive predominantly antibody deficiency with low IgG/IgA, increased IgM and enlarged lymph nodes/germinal centers. [193][199]
4. **Clinical natural history remains the major gap:** No contemporary multi-center HIGM5 cohort, validated patient-reported outcome measure, prospective treatment study or robust genotype–phenotype analysis exists.

## Expert interpretation

The most defensible interpretation is that HIGM5 is **a rare but highly specific failure of specialized DNA-repair machinery co-opted by activated B cells for antibody diversification**. The primary clinical problem is antibody failure rather than combined immunodeficiency. Accordingly:

- Ig replacement, infection control and lung preservation are the treatment priorities.
- Opportunistic-infection and HSCT recommendations designed for CD40LG/CD40 disease should not automatically be applied to isolated UNG deficiency.
- Autoimmune and lymphoid complications may not respond completely to Ig replacement.
- VUS in `UNG` should not be considered diagnostic without biallelic segregation plus functional or compelling phenotype evidence.
- Apparent disease frequencies and survival statistics from umbrella HIGM registries are not valid HIGM5 estimates.

## Critical knowledge gaps

- true prevalence and incidence;
- age-dependent penetrance;
- female-versus-male distribution in observed cases;
- comprehensive pathogenic-variant catalog with transcript-normalized HGVS;
- cancer and autoimmune risks;
- long-term IVIG/SCIG outcomes;
- HIGM5-specific quality-of-life measurements;
- single-cell or spatial immune profiling;
- whether residual UNG/SMUG1 activity predicts clinical severity;
- feasibility and necessity of gene correction given that standard Ig replacement is usually effective.

Overall, the causal gene–disease relationship is strong, but most clinical annotations remain based on fewer than ten well-characterized patients and should be curated with an explicit **limited-case-count evidence flag**.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 9 |
| Off topic | 1 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1371/journal.ppat.1003361&type=printable` (1 mention) - Identifier did not resolve to a record

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC2952935` (1 mention) - Controlling somatic hypermutation in immunoglobulin variable and switch regions.
  - shared terms: uracil, immunoglobulin

Weighed against this report's own most characteristic terms: `higm5`, `ung`, `disease`, `patient`, `infection`, `cell`, `deficiency`, `csr`, `antibody`, `replacement`, `uracil`, `igg`, `lymphoid`, `b-cell`, `immunoglobulin`, `gene`, `molecular`, `recurrent`, `reduced`, `iga`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 20 |
| Terms named correctly | 18 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0060759` (2 mentions) - the report calls it "Disease Ontology"; DOID calls it **immunodeficiency with hyper IgM type 5**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0002845` (obsolete Increased proportion of peripheral CD3+ T cells) (1 mention) - replaced by `HP:0002851`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0045190` (1 mention) - the report calls it "immunoglobulin class-switch recombination"; GO calls it **isotype switching**, and lists "class switch recombination" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.