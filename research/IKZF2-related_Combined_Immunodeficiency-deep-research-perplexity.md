---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-15T14:54:54.678540'
end_time: '2026-10-15T14:59:51.109278'
duration_seconds: 296.43
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: IKZF2-related Combined Immunodeficiency
  mondo_id: MONDO:1010177
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
citation_count: 54
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IKZF2-related Combined Immunodeficiency
- **MONDO ID:** MONDO:1010177 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **IKZF2-related Combined Immunodeficiency** covering all of the
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

# IKZF2-related combined immunodeficiency: comprehensive disease-characteristics report

**Scope and evidence date:** 15 October 2026.  
**Evidence base:** exceptionally small—approximately **15 patients with pathogenic germline IKZF2 variants had been described by 2025**—so frequencies below are case-series counts, not population estimates. The core human evidence comes from three discovery cohorts: Hetemäki et al. 2021 (PMID **34826260**), Shahin et al. 2022 (PMID **34920454**), and Mohajeri et al. 2023 (PMID **37316189**). [19][46][64]

---

## Executive summary

**IKZF2-related combined immunodeficiency**, also called **HELIOS deficiency**, is a Mendelian inborn error of immunity caused by germline loss-of-function or dominant-negative variants in **IKZF2**, which encodes the zinc-finger transcription factor HELIOS. Its defining biology is impaired transcriptional and chromatin regulation in T-lineage cells, with chronic T-cell activation/senescence, deficient or dysregulated regulatory and follicular T-cell function, abnormal germinal-center responses, reduced MAIT cells, and variable B-, NK-, and antibody abnormalities. Clinical expression ranges from recurrent respiratory and mucosal fungal infection with hypogammaglobulinemia to autoimmune cytopenia, systemic lupus erythematosus, EBV-associated hemophagocytic lymphohistiocytosis, lymphoproliferation, and lymphoma. [19][46]

A particularly severe allelic form, **ICHAD syndrome**, results from heterozygous dominant-negative variants in HELIOS DNA-binding zinc fingers and combines neonatal T-cell lymphopenia and immune dysregulation with **craniofacial anomalies, hearing impairment, athelia, and developmental delay**. [33][64]

No disease-specific drug, gene therapy, or validated treatment algorithm exists. Management is phenotype-directed and may include immunoglobulin replacement, antimicrobial prophylaxis, prompt treatment of infection, standard therapy for autoimmune disease/HLH, hearing and developmental support, and consideration of hematopoietic stem-cell transplantation only on an individualized expert basis.

---

# 1. Disease information

## 1.1 Definition

IKZF2-related combined immunodeficiency is an **inborn error of immunity/primary immune regulatory disorder** in which impaired HELIOS function produces variable combined cellular and humoral immunodeficiency together with disproportionate immune activation or autoimmunity. The disease spectrum includes:

1. **HELIOS deficiency/IMDIA:** nonsyndromic or mildly syndromic immunodeficiency and immune dysregulation caused by monoallelic or, rarely, biallelic loss-of-function variants.
2. **ICHAD syndrome:** a severe developmental–immunologic phenotype caused by de novo dominant-negative DNA-binding-domain variants.

The 2024 IUIS classification lists HELIOS deficiency under combined immunodeficiencies, with autosomal-dominant and autosomal-recessive inheritance, increased activated T cells, reduced memory B cells/MAIT cells, and recurrent infections plus autoimmunity. [35]

## 1.2 Identifiers and nomenclature

| Resource | Identifier/name | Comment |
|---|---|---|
| MONDO | **MONDO:1010177**, IKZF2-related combined immunodeficiency | Target identifier supplied in the request; current mapping should be checked against each MONDO release because this ultra-rare entity is undergoing ontology refinement. |
| Orphanet | **ORPHA:697389**, combined immunodeficiency due to HELIOS deficiency | Orphanet lists autosomal-dominant inheritance and synonyms including combined immunodeficiency due to IKZF2 deficiency. [91] |
| OMIM gene | **606234**, IKZF2 | IKZF2/HELIOS gene entry. [3] |
| OMIM disease | **621233**, immunodysregulation with variable immunodeficiency and autoimmunity (IMDIA) | Broad HELIOS-deficiency phenotype. [96][99] |
| OMIM severe allelic disorder | **621234**, ICHAD syndrome | Immunodysregulation, craniofacial anomalies, hearing impairment, athelia, and developmental delay. [8] |
| NCBI Gene | **22807**, IKZF2 | Human IKAROS family zinc finger 2. [15] |
| HGNC | **HGNC:13177**, IKZF2 | Approved symbol; aliases include HELIOS, ZNFN1A2, and ANF1A2. |
| MeSH | No dedicated disease heading | Relevant broader headings include *Combined Immunodeficiency Diseases*, *Primary Immunodeficiency Diseases*, and *Ikaros Transcription Factor*. |
| ICD-10 | No specific code | Usually coded under **D81.9**, combined immunodeficiency, unspecified, or another phenotype-specific code. |
| ICD-11 | No dedicated IKZF2 code identified | Use the most specific available inborn-error/combined-immunodeficiency category plus phenotype codes. |
| SNOMED CT | No disease-specific concept confidently established | Encode combined immunodeficiency and manifestations separately pending a dedicated concept. |

**Synonyms:** HELIOS deficiency; combined immunodeficiency due to HELIOS deficiency; combined immunodeficiency due to IKZF2 deficiency; IKZF2 deficiency; immunodysregulation with variable immunodeficiency and autoimmunity; IMDIA; HELIOS-related inborn error of immunity. ICHAD is an allelic, usually dominant-negative, syndromic presentation—not a synonym for every IKZF2-related case.

## 1.3 Evidence granularity

The knowledge is derived principally from **individual deeply phenotyped patients and small pedigrees**, then aggregated by OMIM, Orphanet, IUIS, PanelApp, and reviews. It is not based on EHR-scale epidemiology, randomized trials, or a formal natural-history registry. Genomics England PanelApp currently treats IKZF2 as a clinically relevant primary-immunodeficiency gene, with monoallelic disease recognized. [2]

---

# 2. Etiology

## 2.1 Primary causal factor

The cause is a **germline pathogenic variant in IKZF2**:

- **Heterozygous truncating or function-disrupting variants:** generally autosomal dominant with incomplete penetrance.
- **Heterozygous DNA-binding-domain variants:** can act dominantly negatively and produce severe ICHAD.
- **Rare biallelic missense loss of function:** autosomal-recessive HELIOS deficiency, exemplified by p.Ile325Val.
- No environmental, infectious, nutritional, or toxic exposure is established as a primary cause.

HELIOS contains four N-terminal C2H2 zinc fingers for DNA binding and two C-terminal zinc fingers for homo-/heterodimerization with IKAROS-family proteins. Variants can impair DNA binding, dimerization, nuclear localization, IL2 repression, or interaction with the NuRD chromatin-remodeling complex. [19][64]

## 2.2 Genetic risk factors

| Risk factor | Evidence and interpretation |
|---|---|
| Pathogenic germline IKZF2 variant | Necessary causal factor in reported Mendelian cases. |
| DNA-binding zinc-finger variant | Associated with dominant-negative activity and severe neonatal/developmental disease in two unrelated ICHAD patients. [64] |
| Truncation removing dimerization region | p.Tyr200Ter and p.Arg291Ter impair HELIOS dimerization/interactomes and produce variable immunodeficiency or autoimmunity. [19][46] |
| Biallelic genotype | p.Ile325Val in a consanguineous family produced combined immunodeficiency with failure to thrive, infection, hypogammaglobulinemia, and inflammatory immune-cell profiles. |
| Family history | Relevant for inherited dominant variants, but absence of family history does not reduce risk substantially because de novo disease occurs and penetrance is incomplete. |
| Consanguinity | Relevant only to rare recessive HELIOS deficiency; not required for dominant disease. |

A p.Arg291Ter carrier father and two p.Arg106Trp family members were asymptomatic, demonstrating **incomplete penetrance**. [19]

## 2.3 Environmental and infectious modifiers

No exposure has been shown to cause HELIOS deficiency. Infection probably modifies clinical expression:

- Repeated respiratory antigen exposure may reveal cellular and antibody deficiency.
- **Candida albicans** infection may be facilitated by mucosal immune and MAIT-cell abnormalities.
- **EBV** can trigger HLH in susceptible patients.
- Viral stimulation may amplify germinal-center and autoimmune dysregulation; in mice, LCMV exposure precipitates autoimmune pathology despite eventual viral clearance. [46][77]

These are **disease triggers/complications**, not causes of the germline disorder.

## 2.4 Protective factors

No validated genetic protective variant, diet, lifestyle factor, or exposure is known. Apparent protection in asymptomatic carriers probably reflects unknown modifier genes, stochastic immune history, age-dependent penetrance, or residual variant function. Vaccination and antimicrobial prophylaxis may prevent complications but do not prevent the genetic disease.

## 2.5 Gene–environment interaction

A plausible but incompletely demonstrated model is:

**IKZF2 dysfunction → reduced tolerance and immune reserve → infection or antigenic stimulation → exaggerated effector/germinal-center activation → infection, autoimmunity, HLH, or lymphoproliferation.**

The interaction is supported by patient infections and mouse challenge studies but has not been quantified in prospective human cohorts.

---

# 3. Phenotypes

Reported frequencies cannot be generalized reliably because cohorts were ascertained differently. “Common” below means recurrent across published patients, not a population prevalence.

| Phenotype/type | Onset, severity, course and evidence | Suggested HPO term |
|---|---|---|
| Recurrent respiratory infection—symptom | Birth/childhood to adult; upper-respiratory infections, pneumonia, sinusitis and otitis; episodic, sometimes causing bronchiectasis/chronic lung disease | Recurrent respiratory infections **HP:0002205**; recurrent pneumonia **HP:0006532** |
| Mucocutaneous candidiasis—clinical sign | Recurrent oral/mucosal thrush in p.Tyr200Ter patients; variable | Oral candidiasis **HP:0000217**; recurrent fungal infections **HP:0002841** |
| Lymphadenopathy—sign | Chronic in the initial p.Tyr200Ter pedigree; reflects lymphoproliferation/germinal-center dysregulation | Lymphadenopathy **HP:0002716** |
| T-cell lymphopenia—laboratory | Neonatal in ICHAD, detected by low TRECs; variable in other genotypes; CD4 and/or CD8 affected | T-cell lymphopenia **HP:0005403** |
| Poor T-cell proliferation—laboratory | More evident in older or biallelic patients; may be progressive with immune senescence | Abnormal lymphocyte proliferation **HP:0031377** |
| Chronic T-cell activation/senescence—laboratory | Increased differentiated CD27−CD28−CD57+ T cells; inflammatory cytokines; potentially age-progressive | Abnormal T-cell activation **HP:0410035** |
| Hypogammaglobulinemia—laboratory | Variable; reported with p.Tyr200Ter, p.Ile325Val, p.Val347Met, p.Arg106Trp and ICHAD p.Gly153Arg | Hypogammaglobulinemia **HP:0004313** |
| Poor vaccine antibody response—laboratory | Demonstrated in severe ICHAD, including poor Hib, tetanus and pneumococcal responses | Impaired antibody response to vaccination **HP:0410308** |
| Reduced switched-memory B cells—laboratory | Recurrent immunophenotypic finding; variable total B-cell count | Reduced class-switched memory B cells **HP:0032139** |
| Reduced MAIT cells—laboratory | Profound in p.Tyr200Ter and p.Ile325Val; a characteristic research biomarker | Reduced mucosal-associated invariant T cells—new HPO term may be needed |
| Reduced NK cells/abnormal NK maturation—laboratory | Reduced CD56^dim^ populations in some patients; severe ICHAD can show immature NK cells and impaired function | Natural killer cell deficiency **HP:0005352** |
| Autoimmune thrombocytopenia—manifestation | Childhood/adult; variable severity, sometimes part of Evans syndrome | Thrombocytopenia **HP:0001873**; autoimmune thrombocytopenia **HP:0001973** |
| Autoimmune hemolytic anemia—manifestation | Congenital/early infancy in severe ICHAD; diagnosed at two months in one child | Autoimmune hemolytic anemia **HP:0001890** |
| Systemic lupus erythematosus—disease phenotype | Childhood onset documented at age 10 in p.Arg291Ter patient; skin lesions, photosensitivity, polyarthritis and autoantibodies | Systemic lupus erythematosus **HP:0002725** |
| EBV-associated HLH—acute complication | Potentially severe episodic hyperinflammation | Hemophagocytic lymphohistiocytosis **HP:0031250** |
| Failure to thrive—physical manifestation | Neonatal/childhood, especially ICHAD and recessive disease; feeding and infection contribute | Failure to thrive **HP:0001508** |
| Sensorineural hearing loss—sign | Congenital, bilateral, moderate to profound; may progress | Sensorineural hearing impairment **HP:0000407** |
| Craniofacial anomalies/cleft palate—physical | Congenital ICHAD; variable eyelid, nasal, ear, jaw, and palate abnormalities | Cleft palate **HP:0000175**; abnormality of facial skeleton **HP:0011821** |
| Athelia—physical | Congenital bilateral absent nipples in both original ICHAD patients | Athelia **HP:0001064** |
| Developmental delay/autism—behavioral/neurodevelopmental | Early childhood; global, language, motor and behavioral impairment; one child nonverbal with autism | Global developmental delay **HP:0001263**; autism **HP:0000717** |
| Atopic dermatitis—skin manifestation | Severe infancy-onset disease in one ICHAD child | Atopic dermatitis **HP:0001047** |
| Hodgkin lymphoma—complication | One p.Tyr200Ter carrier; causality/risk magnitude uncertain | Hodgkin lymphoma **HP:0012196** |
| Bronchiectasis/chronic lung disease—secondary tissue damage | Result of recurrent infection/secretions; documented in severe ICHAD | Bronchiectasis **HP:0002110** |

The p.Arg291Ter index patient developed SLE at age 10 and had reduced CD4 cells, circulating T-follicular-helper cells and CD16+CD56^dim^ NK cells, while the carrier father was asymptomatic. [19] Both original ICHAD children failed newborn hearing/TREC screening and later showed recurrent infections, T-cell lymphopenia, congenital anomalies and developmental impairment. [64]

### Quality-of-life effects

No EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life study exists. Expected burdens include recurrent healthcare use and school/work absence, infection precautions, infusion burden from IVIG, fatigue and pain from autoimmunity, feeding-tube dependence, hearing/communication impairment, developmental services, and psychosocial effects of a lifelong ultra-rare disorder.

---

# 4. Genetic and molecular information

## 4.1 Causal gene

- **Gene:** IKZF2
- **HGNC:** HGNC:13177
- **NCBI Gene:** 22807
- **OMIM gene:** 606234
- **Location:** chromosome **2q34**
- **Protein:** HELIOS, an IKAROS-family C2H2 zinc-finger transcription factor.
- **Subcellular localization:** nucleus, including pericentromeric heterochromatin and chromatin-remodeling complexes.

## 4.2 Published disease-associated variants

| Variant | Class/origin | Functional consequence | Population evidence/clinical interpretation |
|---|---|---|---|
| **p.Tyr200Ter** | Heterozygous nonsense, germline | Loss of C-terminal dimerization domain; reduced/undetectable variant protein in patient cells; impaired interactome | Rare; pathogenic on clinical/functional evidence |
| **NM_016260.3:c.871C>T, p.Arg291Ter** | Heterozygous nonsense; inherited | Cannot homodimerize or heterodimerize with IKAROS/AIOLOS; defective DNA-complex formation and nuclear foci | gnomAD MAF reported as **4×10⁻⁶**; incomplete penetrance [19] |
| **c.316C>T, p.Arg106Trp** | Heterozygous missense | Altered heterochromatin/chromatin-complex interaction; reduced NuRD interactions | Rare, <0.001 in discovery analysis; asymptomatic carriers reported |
| **c.659A>G, p.Asn220Ser** | Heterozygous missense | Reduced interaction with NuRD components | Rare, <0.001 |
| **c.1038G>A, p.Val347Met** | Heterozygous missense | Functional defect less clearly resolved; associated with hypogammaglobulinemia/HLH | Rare, <0.001 |
| **c.1076A>G, p.Tyr359Cys** | Heterozygous missense | No major dimerization defect in initial assays; associated with immune cytopenia and reduced switched B cells | Rare, <0.001 |
| **p.Ile325Val** | Homozygous missense, germline | DNA binding/dimerization retained but reduced Mi-2/NuRD partner interaction; inflammatory transcriptome | Recessive; reported in a consanguineous family |
| **NM_016260.3:c.406+540_574+13477dup; p.Gly136_Ser191dup** | De novo heterozygous ~20-kb tandem exon-5 duplication | Duplicates zinc fingers 2–3; dominant-negative failure of IL2 repression | Absent from gnomAD/DGV/ClinVar/LOVD/DECIPHER at publication; detectable by genome, not initial exome, sequencing [64] |
| **NM_016260.3:c.457G>C; p.Gly153Arg** | De novo heterozygous missense | Alters a critical DNA-contact residue; dominant-negative failure of IL2 repression | Absent from gnomAD, TOPMed, ClinVar, DECIPHER and LOVD at publication; CADD 32 [61][64] |

Formal ClinVar assertions may change over time. Primary papers often describe these variants as pathogenic based on rarity, segregation and functional evidence but do not uniformly publish an explicit ACMG/AMP evidence-code calculation.

## 4.3 Molecular consequence categories

- **Loss of function/haploinsufficiency-like:** truncating alleles with little stable variant protein.
- **Dimerization-defective loss of function:** p.Tyr200Ter and p.Arg291Ter.
- **Dominant negative:** p.Gly136_Ser191dup and p.Gly153Arg, which interfere with wild-type repression of the IL2 promoter.
- **Chromatin-cofactor defect:** p.Ile325Val and several missense variants reduce HELIOS interaction with NuRD components such as CHD3, MTA1/2 and RBBP4/7.
- **Possible neomorphism:** proposed for altered DNA-binding-domain variants, but not demonstrated.

## 4.4 Modifier genes, epigenetics and structural changes

No validated modifier gene or protective allele is known. HELIOS normally recruits or interacts with **NuRD**, SWI/SNF-related proteins, cohesin, and sumoylation machinery; thus the disease is partly an **epigenetic/transcriptional-regulation disorder**, but no reproducible patient DNA-methylation episignature has been established. The exon-5 tandem duplication is the principal reported disease-causing intragenic structural variant. No recurrent whole-chromosome abnormality is implicated.

---

# 5. Environmental information

No toxin, radiation, pollution, occupational exposure, smoking, alcohol, exercise pattern, or diet is known to cause or materially alter penetrance. Clinically important infectious exposures include:

- **Candida albicans:** recurrent mucosal candidiasis.
- **EBV:** trigger for HLH in some patients.
- Common respiratory bacteria and viruses: recurrent upper/lower respiratory infection and pneumonia.

Suggested organism identifiers include *Candida albicans* NCBI Taxon **5476** and Epstein–Barr virus/HHV-4 NCBI Taxon **10376**.

Live-vaccine exposure may present avoidable risk in patients with substantial T-cell deficiency; vaccine decisions must be based on measured immune competence rather than gene status alone.

---

# 6. Mechanism and pathophysiology

## 6.1 Ordered causal chain

1. **A germline IKZF2 loss-of-function, biallelic hypomorphic, or dominant-negative variant leads to reduced or qualitatively abnormal HELIOS protein.**
2. **Abnormal HELIOS leads to impaired DNA binding, dimerization with HELIOS/IKAROS/AIOLOS, and/or recruitment of NuRD and related chromatin-remodeling machinery.**
3. **Defective chromatin regulation leads to failure to repress HELIOS target programs, including excessive IL2-promoter activity in dominant-negative ICHAD variants.**
4. **Transcriptional dysregulation leads to chronic activation and abnormal maturation of conventional and regulatory T cells.**
5. **T-cell dysregulation branches into:**
   - **5A.** reduced immune reserve, lymphopenia and proliferative failure, which lead to recurrent respiratory and fungal infections;
   - **5B.** increased IL-2/IFN-γ and inflammatory programs, which lead to autoimmunity, immune cytopenia, SLE and, with infectious triggers, HLH;
   - **5C.** abnormal T-follicular-helper/T-follicular-regulatory control, which leads to dysregulated germinal centers.
6. **Germinal-center dysregulation leads either to impaired B-cell maturation/hypogammaglobulinemia or to autoantibody production and B-cell autoimmunity.**
7. **Impaired development or maintenance of MAIT and selected NK-cell populations leads—partly inferred—to reduced mucosal/innate-like immune defense and further infection susceptibility.**
8. **In dominant-negative DNA-binding-domain disease, altered HELIOS activity during embryogenesis leads—supported by mouse-expression and mutant data, but incompletely demonstrated in humans—to hearing, craniofacial, nipple and neurodevelopmental abnormalities.**
9. **Repeated infection, autoimmunity and immune-cell infiltration lead secondarily to tissue damage such as bronchiectasis, chronic lung disease, glomerulonephritis or organ injury during HLH.**

## 6.2 Protein and pathway dysfunction

HELIOS is not an enzyme or membrane receptor; it is a **nuclear transcription factor**. Accordingly, the central pathways are:

- T-cell receptor activation and differentiation.
- IL-2 transcription/signaling.
- IFN-γ and inflammatory cytokine programs.
- FOXP3+ regulatory-T-cell stability and in-vivo suppressive function.
- Tfh/Tfr control of germinal-center reactions.
- B-cell activation and maturation.
- Chromatin organization through NuRD, SWI/SNF-associated machinery and cohesin.

Functional assays showed that p.Arg291Ter abolished homodimerization, heterodimerization with IKAROS/AIOLOS and dimeric DNA-complex formation. Proteomic BioID identified abnormal interactions with NuRD components in three of five tested variants. Single-cell RNA sequencing showed inflammatory monocyte/T-cell states and upregulation of **JUNB, HSPA5 and DUSP2**. [19]

The 2023 ICHAD study demonstrated that both DNA-binding variants were expressed but could not effectively repress an IL2 reporter and interfered with wild-type HELIOS—a direct dominant-negative mechanism. [64]

## 6.3 Immune-cell mechanisms

| Cell/process | Finding | Suggested ontology |
|---|---|---|
| Regulatory T cell | Often numerically normal or mildly reduced but with inflammatory cytokine production and impaired in-vivo stability/control | CL:0000815; regulation of immune response GO:0050776 |
| Effector CD4/CD8 T cell | Chronic activation, terminal differentiation, senescence and reduced proliferation | CL:0000911/CL:0000909; T-cell activation GO:0042110 |
| T follicular helper cell | Reduced in blood but accumulated/proliferating in lymph nodes | CL:0002038; germinal-center formation GO:0002467 |
| T follicular regulatory cell | Inadequate restraint of germinal-center responses, strongly supported by mouse conditional knockout | Regulatory T-cell differentiation GO:0045066 |
| MAIT cell | Profoundly reduced in several genotypes | CL:0000940; alpha-beta T-cell differentiation GO:0046632 |
| B cell | Reduced class-switched memory/plasmablast compartments or low total B cells | CL:0000236; B-cell activation GO:0042113 |
| NK cell | Reduced mature CD56^dim^ cells or abnormal differentiation in some patients | CL:0000623; NK-cell differentiation GO:0001779 |
| Monocyte | Proinflammatory transcriptional state in scRNA-seq | CL:0000576; inflammatory response GO:0006954 |

## 6.4 Molecular profiling

- **Single-cell transcriptomics:** one p.Arg291Ter patient versus controls showed fewer NK/central-memory-like cells, more CD14+ monocytes, and inflammatory/exhaustion-associated gene expression. Dataset accessions include EGA **EGAS00001005874** and analysis code at `https://github.com/cancerbits/shahin2021_ikzf2_het`. [19]
- **Bulk transcriptomics:** p.Tyr200Ter and p.Ile325Val lymphocytes showed Th1/inflammatory and altered BCR-signaling signatures.
- **Proteomics:** proximity-labeling/mass spectrometry identified altered NuRD, SWI/SNF-related and cohesin interactions; MassIVE **MSV000088165**. [19]
- **Metabolomics/lipidomics/spatial transcriptomics:** no disease-specific studies identified.
- **CRISPR/RNAi:** experimental HELIOS silencing in healthy/CAR T cells increases inflammatory and antitumor function, supporting its role as a brake on effector activity, but these systems are not disease treatments.

### Key primary-literature quotes

Hetemäki et al. stated:

> “Patients carrying the IKZF2 variant presented with a combined immunodeficiency phenotype characterized by recurrent upper respiratory infections, thrush and mucosal ulcers, and chronic lymphadenopathy.”  
> “Affected individuals displayed a profound reduction in circulating MAIT cell numbers.”  
—*Science Immunology*, 26 November 2021, PMID **34826260**, DOI `https://doi.org/10.1126/sciimmunol.abe3454` [46]

Shahin et al. reported:

> “We identified germline IKZF2 mutations … in six patients with systemic lupus erythematosus, immune thrombocytopenia or EBV-associated hemophagocytic lymphohistiocytosis.”  
> “Single-cell RNA sequencing … revealed upregulation of proinflammatory genes associated with T-cell receptor activation and T-cell exhaustion.”  
—*Blood Advances*, 11 April 2022, PMID **34920454**, DOI `https://doi.org/10.1182/bloodadvances.2021006367` [19]

---

# 7. Anatomical structures affected

| Level | Principal structures | Ontology suggestions |
|---|---|---|
| Organ/system | Immune and hematopoietic system; lymph nodes, thymus, spleen, blood and bone marrow | UBERON:0002405 immune system; UBERON:0000029 lymph node; UBERON:0002370 thymus; UBERON:0002106 spleen |
| Respiratory | Upper airway, sinuses, middle ear and lungs; secondary bronchiectasis/atelectasis | UBERON:0002048 lung; UBERON:0001825 paranasal sinus |
| Auditory | Cochlea/outer hair cells in ICHAD; bilateral sensorineural loss | UBERON:0001844 cochlea; CL:0000202 auditory hair cell |
| Craniofacial/oral | Palate, eyelids, eye, ears, nose and dentition | UBERON:0001716 secondary palate; UBERON:0001769 eye |
| Nervous system | Neurodevelopmental involvement, especially language, behavior and motor learning | UBERON:0000955 brain |
| Skin/breast | Atopic dermatitis; congenital absence of nipples | UBERON:0002097 skin; UBERON:0002030 nipple |
| Kidney | Potential secondary autoimmune glomerular injury; strong mouse evidence, limited human-specific evidence | UBERON:0002113 kidney |
| Subcellular | Nucleus, chromatin, pericentromeric heterochromatin, NuRD complex | GO:0005634 nucleus; GO:0000792 heterochromatin; GO:0016581 NuRD complex |

No lateralization is intrinsic. Hearing loss and athelia are generally bilateral; individual eye abnormalities may be asymmetric.

---

# 8. Temporal development

- **Onset:** ranges from neonatal to childhood/adult.
  - ICHAD: congenital abnormalities, low TRECs and hearing-screen failure at birth; infection and autoimmunity may begin in infancy.
  - Recessive disease: childhood/adolescent failure to thrive, infection and hypogammaglobulinemia.
  - Dominant truncating/missense disease: childhood or adult immune dysregulation; SLE onset at age 10 in the p.Arg291Ter index case.
- **Course:** chronic lifelong genetic disease with episodic infections and autoimmune flares.
- **Progression:** variable. T-cell terminal differentiation/proliferative failure and autoimmune manifestations may worsen with age; this is supported by older patients and mouse models but not quantified longitudinally.
- **Remission:** manifestations can be treatment-controlled; the p.Arg291Ter patient’s SLE entered clinical remission on hydroxychloroquine and NSAIDs. The genetic immune defect does not spontaneously remit. [19]
- **Critical periods:** neonatal TREC/hearing screening provides an early diagnostic opportunity; infancy is critical for preventing infection and managing feeding, hearing and developmental needs.

No validated stage system exists.

---

# 9. Inheritance and population

## 9.1 Epidemiology

Prevalence, incidence, carrier frequency and mortality rates are **unknown**. The disease is ultra-rare, with only a few pedigrees and about 15 molecularly characterized patients by 2025. There is no demonstrated ethnic, geographic or sex enrichment. Both sexes and European and non-European families have been reported.

## 9.2 Inheritance

| Feature | Current conclusion |
|---|---|
| Autosomal dominant | Established for heterozygous loss-of-function and dominant-negative variants |
| Autosomal recessive | Established in at least one biallelic p.Ile325Val case |
| Penetrance | Incomplete for some dominant variants |
| Expressivity | Markedly variable, from asymptomatic carrier to congenital multisystem ICHAD |
| Anticipation | Not reported; no repeat-expansion mechanism |
| Germline mosaicism | Not reported, but low recurrence risk from parental germline mosaicism remains possible after an apparently de novo variant |
| Founder effect | None established |
| Consanguinity | Relevant to recessive disease, not dominant disease |
| Sex ratio | Unknown; no clear sex bias |
| Geographic distribution | Global potential; apparent clustering reflects referral and sequencing rather than biology |

---

# 10. Diagnostics

## 10.1 When to suspect

Consider IKZF2 testing in a patient with one or more of:

- combined infection susceptibility plus autoimmune cytopenia/SLE/HLH;
- low TRECs or T-cell lymphopenia with immune activation;
- hypogammaglobulinemia or poor vaccine responses plus differentiated/senescent T cells;
- profound reduction of MAIT cells;
- congenital sensorineural hearing loss, athelia, cleft palate or craniofacial anomalies together with immunodeficiency.

## 10.2 Recommended work-up

1. **CBC with differential and blood film:** lymphopenia, anemia, thrombocytopenia.
2. **Quantitative IgG, IgA, IgM and IgE.**
3. **Specific antibody titers:** tetanus, diphtheria, Hib and pneumococcal serotypes.
4. **Flow cytometry:** CD3/CD4/CD8, naive/memory and activation/senescence markers; CD19 B-cell subsets; switched-memory B cells; plasmablasts; CD16/CD56 NK subsets; Tregs and, at specialist centers, circulating Tfh and MAIT cells.
5. **T-cell proliferation:** mitogens and antigens.
6. **Autoimmune testing:** DAT, ANA, anti-dsDNA, complement, platelet antibodies where indicated.
7. **Infection/HLH assessment:** EBV PCR; ferritin, triglycerides, fibrinogen, soluble IL-2 receptor and organ evaluation if HLH is suspected.
8. **Pulmonary evaluation:** cultures, chest CT and pulmonary-function testing where recurrent pneumonia/chronic symptoms occur.
9. **ICHAD assessment:** audiology/ABR, ophthalmology, craniofacial examination, feeding/swallow evaluation and formal developmental assessment.

Lymph-node pathology in HELIOS deficiency may show follicular hyperplasia, proliferating follicular T cells and dysregulated germinal centers. [46]

## 10.3 Genetic testing strategy

- **First-line:** an inborn-error-of-immunity/CID/PIRD panel that includes IKZF2, or trio WES/WGS.
- **WGS advantage:** detects intragenic duplications and nonstandard structural variants; the p.Gly136_Ser191dup duplication was missed by initial exome sequencing and discovered by trio genome sequencing. [64]
- **WES:** effective for SNVs and small indels, including p.Gly153Arg.
- **Deletion/duplication analysis:** read-depth CNV calling, exon-level array/MLPA, or genome sequencing if sequencing is nondiagnostic.
- **Sanger testing:** confirm variants and perform parental/cascade segregation.
- **CMA/karyotype/FISH:** not first-line for isolated IKZF2 disease but appropriate if broader chromosomal disease is suspected.
- **RNA studies:** helpful for suspected splice or structural variants.
- **Functional confirmation:** HELIOS expression, IL2-reporter repression, localization/dimerization or chromatin-interaction studies remain research/specialist tests.

## 10.4 Differential diagnosis

| Disorder/gene | Distinguishing considerations |
|---|---|
| IKZF1/IKAROS deficiency | More prominent B-cell developmental/antibody defect; overlapping CID |
| IKZF3/AIOLOS deficiency | B-cell and antibody deficiency, susceptibility to infection; variant-specific immune dysregulation |
| CTLA4 or LRBA deficiency | Autoimmunity, lymphoproliferation and hypogammaglobulinemia; enteropathy often prominent |
| STAT3 gain of function | Early autoimmunity, lymphopenia, growth failure and enteropathy |
| DEF6/LRBA/FOXP3-related immune dysregulation | Autoimmunity/enteropathy; different syndromic and inheritance patterns |
| APDS—PIK3CD/PIK3R1 | Activated/senescent T cells, herpesvirus susceptibility, lymphadenopathy and abnormal B cells |
| GATA2 deficiency | Monocytopenia, B/NK deficiency, HPV/fungal infection and myeloid malignancy |
| 22q11.2 deletion/CHARGE | Cleft palate, low TRECs, hearing/developmental findings; chromosomal/developmental signatures |
| ICF syndrome | Immunodeficiency with characteristic centromeric instability and facial findings |
| ALPS | Chronic nonmalignant lymphadenopathy, autoimmune cytopenia and double-negative T cells |

No universally accepted disease-specific diagnostic criteria exist. Diagnosis requires a compatible phenotype plus a pathogenic/likely pathogenic germline IKZF2 variant, ideally supported by segregation and functional evidence.

## 10.5 Screening

- Population newborn screening does not target IKZF2 specifically, but **TREC screening can detect severe neonatal forms**.
- Cascade testing is appropriate for relatives of a proband.
- Prenatal diagnosis and PGT-M are technically possible once the familial variant is known.
- Asymptomatic carriers require baseline immunologic evaluation and longitudinal follow-up because penetrance can be age-dependent.

---

# 11. Outcome and prognosis

No 5- or 10-year survival estimates, standardized disability statistics, or validated prognostic model exists.

Potential morbidity includes:

- recurrent pneumonia, bronchiectasis and chronic lung damage;
- autoimmune cytopenias and SLE;
- EBV-associated HLH;
- hypogammaglobulinemia and chronic infection;
- feeding failure and growth impairment;
- permanent hearing and neurodevelopmental disability in ICHAD;
- possible lymphoma risk, although one Hodgkin-lymphoma case cannot establish incidence.

Features plausibly associated with poorer prognosis include neonatal low TRECs, profound T-cell lymphopenia, impaired proliferation, recurrent severe infection, HLH, severe autoimmune cytopenia, chronic lung injury, and dominant-negative DNA-binding variants. These have not been validated as formal prognostic biomarkers.

Recovery is manifestation-specific: infections may fall substantially with IVIG/prophylaxis, and autoimmunity may enter remission, but congenital hearing/developmental abnormalities and the germline defect persist.

---

# 12. Treatment

## 12.1 Current strategy

There is no IKZF2-specific guideline or approved precision therapy. Care should be coordinated through a clinical-immunology/IEI center.

| Intervention | Indication and evidence | Suggested NCIt concept |
|---|---|---|
| Immunoglobulin replacement—IVIG/SCIG | Hypogammaglobulinemia, impaired vaccine response or recurrent significant bacterial infection | Immunoglobulin Replacement Therapy **NCIT:C15749** |
| Antibacterial prophylaxis | Recurrent respiratory infection or significant cellular/antibody deficiency | Antibiotic Prophylaxis **NCIT:C51993** |
| Antifungal treatment/prophylaxis | Recurrent candidiasis, individualized to severity | Antifungal Therapy |
| Hydroxychloroquine | SLE manifestations; p.Arg291Ter patient entered remission with hydroxychloroquine plus NSAIDs | Hydroxychloroquine **NCIT:C557** |
| Corticosteroids/standard immunosuppression | Autoimmune cytopenia, SLE or inflammatory complications; balance against infection risk | Corticosteroid Therapy **NCIT:C15360** |
| HLH-directed therapy | Dexamethasone/etoposide-based or targeted regimens according to current HLH protocols, with EBV-directed measures as appropriate | Hemophagocytic Lymphohistiocytosis Treatment |
| Topical corticosteroids/emollients | Atopic dermatitis; effective in the original ICHAD child | Topical Corticosteroid Therapy |
| Cochlear implantation/hearing aids | Congenital severe sensorineural loss; cochlear implants improved hearing and language in one ICHAD child | Cochlear Implantation **NCIT:C91830** |
| Feeding and nutritional support | Failure to thrive, cleft palate or dysphagia; NG/G-tube where necessary | Enteral Nutrition **NCIT:C15293** |
| Developmental, speech, occupational and physical therapies | ICHAD neurodevelopmental manifestations | Rehabilitation Therapy |
| HSCT | Potentially curative for hematopoietic immune dysfunction but no robust IKZF2-specific outcome series; will not reverse established congenital anomalies | Hematopoietic Stem Cell Transplantation **NCIT:C15431** |

One ICHAD child received monthly IVIG and daily oral antibiotic prophylaxis with a documented reduction in respiratory infections and healthcare use. [64]

## 12.2 Practical treatment algorithm

1. Quantify infection burden, immunoglobulins, vaccine titers, T-cell count/function and organ damage.
2. Start IVIG/SCIG for clinically significant antibody failure; do not rely on IgG alone if vaccine responses are poor.
3. Use antimicrobial prophylaxis when infections persist or T-cell deficiency is substantial.
4. Treat autoimmunity by standard disease protocols while escalating infection surveillance.
5. Treat EBV/HLH urgently in a specialist center.
6. Avoid live vaccines when clinically important T-cell dysfunction is present.
7. Discuss HSCT for severe, progressive, life-threatening disease refractory to medical management; evidence remains insufficient for routine pre-emptive transplantation.
8. Provide hearing, developmental, pulmonary, nutritional and psychosocial support.

No evidence supports genotype-guided pharmacogenomics, HELIOS replacement, CRISPR editing, antisense/RNA therapy or a HELIOS-targeted drug in affected patients. Experimental HELIOS degraders being studied in cancer would mechanistically be inappropriate and potentially harmful in HELIOS deficiency.

---

# 13. Prevention

## Primary prevention

The spontaneous germline disorder cannot be prevented by lifestyle modification. Reproductive options include genetic counseling, PGT-M and prenatal diagnosis.

## Secondary prevention

- TREC newborn screening can identify severe T-cell lymphopenia.
- Hearing screening is particularly informative in ICHAD.
- Early genomic testing of syndromic low-TREC infants can shorten the diagnostic interval.
- Cascade testing can identify at-risk relatives before major complications.

## Tertiary prevention

- Immunoglobulin replacement and antimicrobial prophylaxis.
- Vaccination with non-live vaccines, followed by measurement of response where useful.
- Avoidance of live vaccines in patients with significant cellular immunodeficiency.
- Prompt infection treatment and EBV monitoring in selected patients.
- Pulmonary surveillance to prevent bronchiectasis progression.
- Early autoimmune/HLH recognition.
- Hearing, feeding and developmental intervention during infancy.

Because penetrance is incomplete, genetic counseling should explain that a positive variant does not precisely predict severity.

---

# 14. Other species and natural disease

| Item | Current evidence |
|---|---|
| Human | *Homo sapiens*, NCBI Taxon **9606**; IKZF2 NCBI Gene **22807** |
| Mouse | *Mus musculus*, NCBI Taxon **10090**; ortholog **Ikzf2**, NCBI Gene **22779**, MGI **1342541** [79][83] |
| Natural veterinary disease | No well-established spontaneous IKZF2-related CID in companion animals, livestock or wildlife was identified |
| Breed association/VBO | None established |
| Zoonotic potential | None; this is a germline genetic disease |
| Transmission | Mendelian inheritance, not infectious cross-species transmission |

The mechanism is evolutionarily conserved: mouse Helios regulates lymphocyte tolerance, germinal centers, cochlear hair-cell maturation and neurodevelopment, although the complete human disease spectrum is not reproduced by a single model.

---

# 15. Model organisms and experimental systems

| Model | Key phenotype and disease relevance | Limitations/resource |
|---|---|---|
| Global **Ikzf2−/− mouse** | Postnatal lethality in many homozygotes, reduced weight; survivors develop age-dependent immune activation, autoantibodies, lymphocytic infiltration and glomerulonephritis at 6–8 months | Human disease can present neonatally; mouse thymopoiesis is relatively preserved. MGI reports 11 phenotypes across four alleles. [79] |
| Treg-specific **Foxp3-Cre Ikzf2** knockout | Increased germinal centers, Tfh and GC B cells; impaired in-vivo control of autoimmunity; up to 75-fold increased splenic Tfh in one model | Models Treg-intrinsic loss, not every human cell lineage |
| **Ikzf2 cello/cello** mouse | Sensorineural hearing loss, elevated auditory-brainstem-response thresholds, defective outer-hair-cell maturation, microphthalmia/cloudy eye | Recapitulates developmental features better than immune spectrum |
| Helios reporter/Treg-transfer mice | Show that Helios-deficient Tregs may suppress in vitro yet fail under stringent in-vivo autoimmune challenge | Transfer systems do not reproduce human germline disease |
| LCMV-challenged Ikzf2−/− mice | Infection provokes kidney immune deposits and increased Tfh/GC cells, supporting infection–autoimmunity interaction | Artificial viral challenge; not equivalent to EBV |
| HEK293/Jurkat reporter systems | Define expression, dimerization, localization and IL2-promoter repression defects | Nonphysiologic overexpression and transformed-cell context |
| Patient PBMC/LCL systems | Direct immunophenotyping, cytokine assays, scRNA-seq and proteomic interactomes | Very small sample size and treatment confounding |
| CRISPR/RNAi HELIOS-silenced T cells | Increased effector/inflammatory and antitumor activity, supporting HELIOS as a restraint on T-cell activation | Models acute experimental depletion, not lifelong developmental deficiency |
| Patient-derived iPSC/organoid models | No mature disease-specific system reported | Important future need for cochlear, thymic and neurodevelopmental studies |

MGI allele **MGI:4355173** is a targeted null allele in which homozygous thymus lacks detectable protein. [76]

---

# Evidence assessment and knowledge gaps

**High-confidence conclusions**

- Germline IKZF2 variants cause a combined immunodeficiency/immune-dysregulation syndrome.
- HELIOS loss disrupts T-cell activation control, germinal-center regulation and MAIT-cell homeostasis.
- DNA-binding-domain p.Gly136_Ser191dup and p.Gly153Arg variants act dominantly negatively and cause ICHAD.
- Both dominant and recessive inheritance occur.

**Moderate-confidence conclusions**

- Genotype–phenotype correlation: DNA-binding dominant-negative variants are generally more severe and syndromic than dimerization-defective truncations.
- HELIOS deficiency increases lymphoma risk.
- Reduced MAIT cells materially cause fungal susceptibility rather than merely marking immune dysregulation.

**Major unavailable data**

- Population prevalence/incidence and carrier frequency.
- Prospective natural history, survival and validated prognostic markers.
- Standardized quality-of-life outcomes.
- Disease-specific treatment-response rates and HSCT outcomes.
- Validated methylation signature, metabolomic profile or diagnostic functional assay.
- Environmental or genetic modifiers explaining incomplete penetrance.

Overall, this is best represented in a knowledge base as a **rare allelic spectrum of HELIOS dysfunction**, with **combined immunodeficiency and immune dysregulation as the core phenotype** and **ICHAD as the severe dominant-negative developmental subtype**.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 2 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 71 |
| Resolved | 67 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:1010177` (2 mentions) - the report calls it "if available"; MONDO calls it **IKZF2-related combined immunodeficiency**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0001064` (1 mention) - HP does not contain this term

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.
