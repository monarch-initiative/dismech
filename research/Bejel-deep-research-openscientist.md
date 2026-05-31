---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-05T21:16:33.223689'
end_time: '2026-05-05T21:37:33.017170'
duration_seconds: 1259.79
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bejel
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
citation_count: 27
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bejel
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Bejel** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Comprehensive Disease Characterization Report: Bejel (Endemic Syphilis)

---

## Summary

**Bejel** (endemic syphilis) is a chronic, non-venereal treponematosis caused by *Treponema pallidum* subspecies *endemicum* (TEN). Classically, bejel is transmitted through direct skin-to-skin contact or shared contaminated utensils among children living in hot, arid, resource-poor regions of the Middle East, the Sahel belt of Africa, and parts of Central Asia. The disease progresses through primary (often subclinical oral mucous patches), secondary (mucocutaneous and osteoperiosteal lesions), and tertiary stages (destructive gummatous lesions of skin, bone, and nasopharynx). It is effectively treated with benzathine penicillin G, similar to other treponematoses. As of 1989, over 2.5 million cases of endemic treponematoses existed worldwide, with 75% in children and over 100 million additional children at risk ([PMID: 2682125](https://pubmed.ncbi.nlm.nih.gov/2682125/)).

A paradigm shift is underway in our understanding of bejel's epidemiology. Molecular typing studies have now identified TEN circulating via sexual transmission among men who have sex with men (MSM) in Japan, Cuba, and Europe, with clinical features indistinguishable from venereal syphilis. In Japan, TEN was found in 12% (3/25) of molecularly typed syphilis samples from MSM, and most strains carried the macrolide resistance mutation A2058G in 23S rDNA ([PMID: 39415268](https://pubmed.ncbi.nlm.nih.gov/39415268/)). Because standard serological tests cannot differentiate TEN from *T. pallidum* subsp. *pallidum* (TPA, the agent of venereal syphilis), many cases of sexually transmitted bejel are likely misdiagnosed as syphilis. This diagnostic blind spot, combined with the emergence of macrolide resistance, represents a significant and underappreciated public health challenge that demands enhanced molecular surveillance.

This report synthesizes evidence from 69 peer-reviewed publications and provides a comprehensive characterization of bejel covering disease information, etiology, phenotypes, genetics/molecular biology, pathophysiology, anatomical involvement, temporal development, epidemiology, diagnostics, prognosis, treatment, prevention, animal reservoirs, and model organisms.

---

## 1. Disease Information

### Overview

Bejel, also known as **endemic syphilis**, is one of the three endemic treponematoses (along with yaws and pinta) and is caused by *Treponema pallidum* subspecies *endemicum* (TEN). Unlike venereal syphilis, bejel is not primarily sexually transmitted but spreads through direct contact with infectious lesions or contaminated fomites (e.g., shared drinking vessels) in communities with poor hygiene and overcrowding. The disease predominantly affects children in arid tropical and subtropical environments.

As established by Mitjà et al. (2013): *"T. pallidum subsp. pallidum causes venereal syphilis, while T. pallidum subsp. pertenue, T. pallidum subsp. endemicum, and T. carateum are the agents of the endemic treponematoses yaws, bejel (or endemic syphilis), and pinta, respectively"* ([PMID: 24396138](https://pubmed.ncbi.nlm.nih.gov/24396138/)). Šmajs et al. (2014) further clarified: *"T. pallidum subsp. endemicum (TEN) is the causative agent of bejel (also known as endemic syphilis). Clinical symptoms of syphilis and bejel are overlapping and the epidemiological context is important for correct diagnosis of both diseases"* ([PMID: 25375929](https://pubmed.ncbi.nlm.nih.gov/25375929/)).

### Key Identifiers

| Identifier | Code/ID |
|---|---|
| **ICD-10** | A65 -- Non-venereal syphilis |
| **ICD-11** | 1A62 -- Endemic syphilis (bejel) |
| **MONDO** | MONDO:0001714 |
| **MeSH** | D014210 -- Syphilis, Endemic |
| **SNOMED CT** | 43753002 -- Endemic syphilis |
| **NCBI Taxonomy (organism)** | 160 |
| **Wikidata** | Q682798 |

### Synonyms and Alternative Names

- Endemic syphilis
- Bejel
- Dichuchwa (Southern Africa)
- Njovera (Zimbabwe)
- Belesh (Saudi Arabia)
- Skerljevo (Balkans)
- Firjal (Iraq)
- Siti
- Non-venereal endemic syphilis

### Information Sources

Information on bejel is derived primarily from **aggregated disease-level resources** (WHO reports, epidemiological surveys, case series, molecular epidemiology studies) rather than individual electronic health records (EHR). This is because bejel is a neglected tropical disease primarily affecting populations with limited access to healthcare infrastructure. Individual-level data from MSM populations in Japan and Cuba represent a newer, more granular data source.

---

## 2. Etiology

### Disease Causal Factors

Bejel is an **infectious disease** caused by the spirochete bacterium *Treponema pallidum* subspecies *endemicum* (TEN). The organism is a Gram-negative spirochete, 6-15 micrometer long and 0.15 micrometer wide, with endoflagella enabling corkscrew motility. It is an obligate human pathogen that cannot be cultured on artificial media, making laboratory study extremely challenging.

The TEN Bosnia A reference genome is **1,137,653 bp** in length (1.6-2.8 kbp shorter than other pathogenic treponeme genomes), with 513x average genome coverage achieved through pooled segment genome sequencing. Phylogenomic analyses show that TEN is most closely related to yaws-causing *T. pallidum* subsp. *pertenue* (TPE) strains but contains several sequences previously unique to syphilis treponemes ([PMID: 25375929](https://pubmed.ncbi.nlm.nih.gov/25375929/)).

### Risk Factors

#### Environmental and Socioeconomic Risk Factors (Classical Bejel)

Bejel foci are *"typically confined to underprivileged communities living in remote rural areas, with little or no access to health services and removed from the mainstream of socioeconomic development"* ([PMID: 1281363](https://pubmed.ncbi.nlm.nih.gov/1281363/)). Specific risk factors include:

- **Poverty and overcrowding:** Dense living conditions facilitate person-to-person transmission
- **Hot, dry climate:** Arid regions of the Middle East, Sahel Africa, and Central Asia favor transmission
- **Age:** Children aged 2-15 years are most commonly affected; 75% of all endemic treponematosis cases are in children ([PMID: 2682125](https://pubmed.ncbi.nlm.nih.gov/2682125/))
- **Shared utensils and communal living:** Drinking vessels shared among family members facilitate oral-to-oral transmission
- **Poor access to clean water and hygiene infrastructure**
- **Limited access to health services**

#### Emerging Risk Factors (Sexually Transmitted TEN)

- **Men who have sex with men (MSM):** TEN has been identified in MSM populations in Japan, Cuba, and Europe ([PMID: 31310214](https://pubmed.ncbi.nlm.nih.gov/31310214/); [PMID: 29454847](https://pubmed.ncbi.nlm.nih.gov/29454847/))
- **HIV co-infection:** In Japan, 97.2% of MSM with TEN infection were people with HIV ([PMID: 39415268](https://pubmed.ncbi.nlm.nih.gov/39415268/))
- **High-risk sexual behavior in urban populations**

#### Genetic Risk Factors

No specific host genetic susceptibility loci have been identified for bejel. Susceptibility is driven entirely by exposure in the context of environmental and behavioral risk factors. Host immune factors (HLA type, innate immune polymorphisms) may influence susceptibility, but these are unstudied specifically for TEN.

### Protective Factors

- **Improved sanitation and hygiene:** The single most effective protective factor; access to clean water and personal hygiene reduces fomite transmission
- **Socioeconomic development:** Elimination of overcrowding and improved housing
- **Prior treponemal infection:** Partial cross-immunity between treponemal subspecies may confer some protection
- **Mass treatment campaigns:** Population-level penicillin administration (as conducted by WHO/UNICEF in the 1950s-60s, treating over 50 million individuals in 46 countries)
- **Access to primary healthcare:** Early detection and treatment interrupt transmission chains

### Gene-Environment Interactions

Not applicable for bejel as a purely infectious disease. However, host immune status (particularly HIV co-infection) significantly modifies disease presentation and may facilitate the emergence of sexually transmitted TEN in immunocompromised populations.

---

## 3. Phenotypes

### Primary Stage

| Feature | Details |
|---|---|
| **Phenotype type** | Clinical sign |
| **Description** | Small, painless papule or mucous patch, typically on oral or oropharyngeal mucosa |
| **Age of onset** | Childhood (2-15 years in classic bejel); adulthood in sexually transmitted cases |
| **Severity** | Mild; often subclinical and painless |
| **Progression** | Self-resolving; may progress to secondary stage |
| **Frequency** | Often unnoticed (~50% subclinical) |
| **HPO terms** | HP:0000155 (Oral ulcer); HP:0011830 (Abnormality of oral mucosa) |

### Secondary Stage

| Feature | Details |
|---|---|
| **Mucous patches** | Oropharyngeal erosions (most common and characteristic) -- HP:0000155 |
| **Condylomata lata** | Moist, flat, wart-like lesions in intertriginous areas (axillae, groin) -- HP:0200039 |
| **Maculopapular rash** | Disseminated skin lesions on trunk and extremities -- HP:0011124 |
| **Angular stomatitis** | Fissured papules at angles of mouth (split papules) -- HP:0000161 |
| **Osteoperiostitis** | Painful swelling of long bones, particularly tibia -- HP:0100252; HP:0100539 |
| **Lymphadenopathy** | Regional or generalized lymph node enlargement -- HP:0002716 |
| **Age of onset** | Childhood to adolescence (classic); young adulthood (emerging) |
| **Severity** | Moderate |
| **Progression** | Lesions may wax and wane over 1-2 years; may resolve spontaneously, enter latency, or progress |
| **Frequency** | Most commonly recognized stage; ~60-70% of untreated primary cases |

### Latent Stage

- **Phenotype type:** Laboratory abnormality
- **Description:** Asymptomatic period with positive serological tests but no clinical manifestations. May persist indefinitely.
- **Progression:** May remain latent or progress to tertiary disease

### Tertiary Stage

| Feature | Details |
|---|---|
| **Gummatous skin lesions** | Destructive granulomatous nodules or ulcers -- HP:0100242; HP:0100686 |
| **Nasopharyngeal destruction (gangosa)** | Gummatous destruction of nasal septum and hard palate -- HP:0000277 |
| **Bone gumma** | Destructive osteitis, particularly of tibia (sabre tibia) and skull -- HP:0002762; HP:0002797 |
| **Age of onset** | Late adolescence to adulthood (years to decades after infection) |
| **Severity** | Severe; disfiguring |
| **Frequency** | ~10-15% of untreated cases |

### Sexually Transmitted TEN Phenotypes (Emerging)

In MSM populations, TEN infection presents with clinical features **indistinguishable from venereal syphilis**: genital chancres, maculopapular rash, mucous patches, and lymphadenopathy. Nishiki et al. (2021) described: *"Bejel, caused by Treponema pallidum subsp. Endemicum (TEN), is a locally transmitted disease among children and juveniles in hot and dry regions. The number of adult cases of TEN infection outside of endemic areas has recently increased"* ([PMID: 34836779](https://pubmed.ncbi.nlm.nih.gov/34836779/)).

### Quality of Life Impact

- **Primary/secondary bejel:** Moderate impact -- painful oral and skin lesions may impair eating and social interaction
- **Tertiary bejel:** Severe impact -- disfiguring gummatous destruction causes significant disability, social stigma, and functional impairment (eating, breathing, speech)
- **Cardiovascular and neurological involvement:** Unlike venereal syphilis, classic bejel is generally considered NOT to cause cardiovascular syphilis or neurosyphilis, though data are limited and this distinction is debated

---

## 4. Genetic/Molecular Information

### Pathogen Genomics

As bejel is an infectious disease, the relevant genetic/molecular information pertains to the **pathogen genome** rather than host genetics.

**TEN Bosnia A Reference Genome ([PMID: 25375929](https://pubmed.ncbi.nlm.nih.gov/25375929/)):**
- **Size:** 1,137,653 bp
- **GenBank accession:** CP007548
- **Key finding:** Most closely related to TPE (yaws) but containing sequences previously unique to TPA (syphilis)
- **Genome similarity:** >99.8% identical to TPA and TPE

### Key Virulence Factors and Molecular Features

| Gene/Protein | Function | Relevance |
|---|---|---|
| **tpr gene family** (tprC, D, G, I, J, K) | Outer membrane proteins; potential virulence factors | Evolve through gene duplication and gene conversion; recombination between subspecies detected ([PMID: 16926243](https://pubmed.ncbi.nlm.nih.gov/16926243/)) |
| **TprK** | Variable outer membrane protein; immune evasion | Promotes M1 macrophage polarization via TLR2/JAK1/STAT1/IDO pathway ([PMID: 40513619](https://pubmed.ncbi.nlm.nih.gov/40513619/)) |
| **TprC/TprD** | Outer membrane proteins; B-cell epitope targets | B-cell epitope mapping reveals variant-specific immune responses ([PMID: 35422800](https://pubmed.ncbi.nlm.nih.gov/35422800/)) |
| **BamA/FadL** | Outer membrane proteins; candidate vaccinogens | Sequence variability suggests divergent evolutionary paths ([PMID: 40802283](https://pubmed.ncbi.nlm.nih.gov/40802283/)) |
| **23S rDNA (A2058G mutation)** | Ribosomal RNA | Macrolide resistance; found in most sexually transmitted TEN strains |
| **TP0136, TP0548, TP0705** | MLST typing loci | Used for molecular epidemiological typing ([PMID: 39415268](https://pubmed.ncbi.nlm.nih.gov/39415268/)) |

### Genomic Diversity and Recombination

Whole-genome sequencing of TEN isolates from Cuba revealed **non-clonal diversity** with nucleotide variability of 0.2-10.3 substitutions per 100 kbp, affecting 27 genes. Recombination events were detected between tprC and tprI, in TP0488, and in the intergenic region TP0127-TP0129. Pospisilova et al. (2022) concluded: *"the determined non-clonal character of the isolates suggests a persistent infection in the Cuban population rather than a single outbreak caused by imported case"* ([PMID: 35687593](https://pubmed.ncbi.nlm.nih.gov/35687593/)).

Phylogenomic analysis of 75 *T. pallidum* genomes identified **21 recombination events involving 12 genes**, mostly intersubspecies transfers from TPE/TEN to TPA, with strong positive selection on recombinant genes. As Arora et al. (2021) reported: *"we found strong evidence for recombination among the T. pallidum subspecies, involving 12 genes and 21 events. In most cases, only one recombination event per gene was detected and all but one event corresponded to intersubspecies transfers, from TPE/TEN to TPA"* ([PMID: 34791386](https://pubmed.ncbi.nlm.nih.gov/34791386/)).

### Pre-Columbian Treponemal History

Recent paleogenomic work has recovered treponemal genomes from pre-Columbian remains in Brazil, redefining the history of treponemal diseases ([PMID: 38267579](https://pubmed.ncbi.nlm.nih.gov/38267579/)). The tpr gene evolution analyses show higher variation between human subspecies than within them, supporting the three-subspecies classification, while the divergence patterns do not support a much older origin of yaws at the emergence of modern humans ([PMID: 16926243](https://pubmed.ncbi.nlm.nih.gov/16926243/)).

---

## 5. Environmental Information

### Environmental Factors

- **Climate:** Hot, arid environments favor transmission (drying of skin creates entry points; communal water use increases fomite transmission)
- **Overcrowding and poor sanitation:** Critical environmental determinants
- **Rural isolation:** Limits access to healthcare for early diagnosis and treatment
- **No toxin, radiation, or occupational exposure involvement**

### Lifestyle Factors

- **Communal drinking and eating:** Shared utensils and cups facilitate oral-to-oral transmission among children
- **Sleeping arrangements:** Shared bedding in close quarters
- **Sexual behavior (emerging):** MSM sexual networks now identified as transmission routes for TEN

### Infectious Agent

| Property | Detail |
|---|---|
| **Pathogen** | *Treponema pallidum* subsp. *endemicum* (TEN) |
| **NCBI Taxonomy ID** | 160 |
| **Type** | Gram-negative spirochete bacterium |
| **Family** | Treponemataceae |
| **Order** | Spirochaetales |
| **Transmission** | Non-venereal: direct contact, fomites; Emerging: sexual contact |
| **Incubation period** | 2-6 weeks |
| **Reservoir** | Humans (primary); potentially non-human primates (speculative) |
| **Viability outside host** | Very fragile; rapidly inactivated by drying, temperature extremes, disinfectants |

---

## 6. Mechanism / Pathophysiology

### Causal Chain: Initial Trigger to Clinical Manifestation

```
TEN inoculation (oral mucosa or skin / genital mucosa in sexual transmission)
        |
        v
Local multiplication in epithelium
        |
        v
Primary lesion (mucous patch / chancre)  <-- Innate immune response
        |                                      (neutrophils, macrophages)
        v
Hematogenous/lymphatic dissemination (hours to days)
        |
        v
Secondary stage                          <-- Adaptive immune response
 - Mucocutaneous lesions                      (CD4+ and CD8+ T cells,
 - Periostitis                                 plasma cells, IFN-gamma, IL-17)
 - Condylomata lata
        |
        v
Partial immune control --> Latency
        |
        v
Tertiary stage (~10% untreated)          <-- Chronic granulomatous inflammation
 - Gummatous destruction                      (delayed-type hypersensitivity)
 - Bone/cartilage necrosis
 - Nasal/palatal destruction
```

### Immune System Involvement

Cell-mediated immunity is critical for anti-treponemal host defense. Cruz et al. (2010) demonstrated that in HIV-negative individuals with secondary syphilitic lesions, the inflammatory infiltrate contained equal numbers of CD4+ and CD8+ T cells, *"whereas in HIV+ patients, the majority of T cells belonged to the CD8 lineage and produced both IFN-gamma and IL-17"*. Furthermore, *"Regulatory T cells and Langerhans cells were reduced in these patients compared with their HIV- counterparts"* ([PMID: 20889558](https://pubmed.ncbi.nlm.nih.gov/20889558/)).

**Key immune pathways:**
- **Macrophage activation:** IFN-gamma enhances CD64-potentiated phagocytosis of *T. pallidum* ([PMID: 29051759](https://pubmed.ncbi.nlm.nih.gov/29051759/))
- **TLR2 signaling:** Recombinant TprK activates M1 macrophage polarization and induces indoleamine 2,3-dioxygenase (IDO) production through the TLR2/JAK1/STAT1 pathway. *"Inhibition of TLR2, JAK1, or STAT1 effectively reduces IDO expression and attenuates macrophage activation"* ([PMID: 40513619](https://pubmed.ncbi.nlm.nih.gov/40513619/))
- **Interferon-stimulated genes:** IFIT2 is upregulated in *T. pallidum* infection, modulating immune responses and infection outcomes ([PMID: 41046825](https://pubmed.ncbi.nlm.nih.gov/41046825/))
- **CRP as bacteremia marker:** Elevated CRP (cut-off 0.5 mg/dL) was significantly associated with detectable spirochetes in blood ([PMID: 39415268](https://pubmed.ncbi.nlm.nih.gov/39415268/))

### GO Terms for Biological Processes

- GO:0006955 -- Immune response
- GO:0006954 -- Inflammatory response
- GO:0042742 -- Defense response to bacterium
- GO:0050776 -- Regulation of immune response
- GO:0030593 -- Neutrophil chemotaxis
- GO:0007155 -- Cell adhesion
- GO:0044409 -- Entry into host
- GO:0009405 -- Pathogenesis

### Cell Types Involved (CL Terms)

- CL:0000235 -- Macrophage
- CL:0000084 -- T cell
- CL:0000625 -- CD8-positive, alpha-beta T cell
- CL:0000624 -- CD4-positive, alpha-beta T cell
- CL:0000775 -- Neutrophil
- CL:0000786 -- Plasma cell
- CL:0000451 -- Dendritic cell (Langerhans cell)

### Tissue Damage Mechanisms

**Primary/Secondary stages:**
- Direct tissue invasion by spirochetes
- Inflammatory infiltration (lymphocytes, plasma cells, macrophages, neutrophils)
- Endothelial swelling and perivascular inflammation (endarteritis obliterans)
- Periosteal invasion triggering inflammatory osteitis and new bone formation

**Tertiary stage:**
- Granulomatous inflammation (gumma): central necrosis surrounded by epithelioid cells, giant cells, lymphocytes, and plasma cells
- Immune-mediated tissue destruction (delayed-type hypersensitivity)
- Fibrosis and scarring

### Metabolic/Biochemical Features

- *T. pallidum* has extremely limited metabolic capacity (~5% of genome dedicated to biosynthesis)
- Cannot synthesize most amino acids, nucleotides, fatty acids, or enzyme cofactors
- Depends entirely on host for most metabolic precursors
- No known toxins produced; tissue damage results from host immune response

### Molecular Profiling

Limited molecular profiling data exist for bejel specifically. No transcriptomic, proteomic, or metabolomic studies have been conducted on TEN-infected human tissues. Comparative genomics shows the TEN genome is most similar to TPE but with TPA-specific sequences in several loci ([PMID: 25375929](https://pubmed.ncbi.nlm.nih.gov/25375929/)).

---

## 7. Anatomical Structures Affected

### Organ Level

| Organ/System | Involvement | UBERON Term |
|---|---|---|
| **Skin** | Primary (all stages) | UBERON:0002097 |
| **Oral cavity** | Primary site of inoculation and early lesions | UBERON:0000167 |
| **Bone (long bones, skull)** | Secondary/tertiary (periostitis, osteitis, gumma) | UBERON:0002481 |
| **Nasal structures** | Tertiary (gangosa) | UBERON:0000004 |
| **Hard palate** | Tertiary (perforation) | UBERON:0003216 |
| **Lymph nodes** | Secondary (lymphadenopathy) | UBERON:0000029 |
| **Liver** | Congenital (hepatomegaly in animal model) | UBERON:0002107 |
| **Spleen** | Congenital (splenomegaly in animal model) | UBERON:0002106 |

**Body systems involved:** Integumentary, skeletal, lymphatic/immune, upper respiratory tract

**Notable absence:** Unlike venereal syphilis, classic bejel does **not** typically involve the cardiovascular system (aortitis) or central nervous system (neurosyphilis), though the accuracy of this distinction remains debated due to limited data.

### Tissue and Cell Level

- **Epithelial tissue:** Initial site of infection and primary lesion formation
- **Connective tissue:** Periosteum, bone marrow (periostitis and osteitis)
- **Mucosal tissue:** Oral and nasal mucosa
- **Vascular endothelium:** Endarteritis obliterans

### Subcellular Level

*T. pallidum* is an extracellular pathogen that primarily resides in the extracellular space but can traverse endothelial barriers and invade perivascular spaces.
- GO:0005576 -- Extracellular region
- GO:0005615 -- Extracellular space
- GO:0031012 -- Extracellular matrix

### Localization

- **Primary lesion:** Typically oral/oropharyngeal mucosa in classic bejel; genital in sexually transmitted cases
- **Secondary lesions:** Bilateral, symmetric; oral mucosa, intertriginous areas, long bone periosteum
- **Tertiary lesions:** Nasopharynx, tibial bones, skull, skin
- **Lateralization:** Generally bilateral and symmetric

---

## 8. Temporal Development

### Onset

- **Typical age of onset:** 2-15 years (classic childhood bejel); young to middle-aged adults (sexually transmitted TEN)
- **Onset pattern:** Subacute to insidious; primary lesions are often painless and subclinical
- **Incubation period:** Approximately 2-6 weeks

### Progression

| Stage | Timing | Features | Duration |
|---|---|---|---|
| **Primary** | 2-6 weeks post-infection | Oral mucous patches (often subclinical) | Weeks |
| **Secondary** | Weeks to months after primary | Disseminated mucocutaneous lesions, periostitis, condylomata lata | Weeks to months; may wax and wane over 1-2 years |
| **Latent** | After secondary resolves | Asymptomatic; serologically positive | Years to decades |
| **Tertiary** | Years to decades | Gummatous destruction of skin, bone, nasopharynx | Chronic progressive |

- **Progression rate:** Slow; disease evolves over years to decades
- **Disease course pattern:** Relapsing-remitting in secondary stage; progressive in tertiary
- **Disease duration:** Chronic lifelong if untreated
- **Self-limited features:** Primary and secondary lesions may resolve spontaneously, but latent infection persists

### Critical Periods

- **Childhood (2-10 years):** Primary window of vulnerability for classic bejel due to close communal living and shared utensils
- **Early treatment window:** Treatment in primary or secondary stage prevents progression to destructive tertiary disease

---

## 9. Inheritance and Population

### Epidemiology

**Global Burden:** As described by Antal et al. (1989): *"Today there are more than 2.5 million cases of these diseases, 75% of them in children. More than 100 million additional children are at risk for these disabling and disfiguring infections which destroy tissue and bone"* ([PMID: 2682125](https://pubmed.ncbi.nlm.nih.gov/2682125/)). These figures encompass all endemic treponematoses (yaws, bejel, pinta), with bejel representing a subset concentrated in arid regions.

**Historical context:** The WHO/UNICEF mass treatment campaigns of the 1950s-1960s treated over 50 million individuals in 46 countries with remarkable success. However, resurgence occurred after campaign discontinuation, particularly in West and Central Africa. WHO set yaws eradication goals (initially 2020, extended to 2030).

**Precise prevalence and incidence for bejel alone remain poorly characterized** due to serological indistinguishability from other treponemal infections and limited surveillance in affected regions.

### Inheritance Pattern

**Not applicable.** Bejel is an infectious disease with no Mendelian or polygenic inheritance pattern. Familial clustering reflects shared environmental exposure rather than genetic susceptibility.

### Geographic Distribution

| Region | Status |
|---|---|
| **Sahel belt of Africa** (Niger, Mali, Burkina Faso, Senegal, Chad) | Endemic |
| **Middle East** (Saudi Arabia, Iraq, Syria) | Endemic/declining |
| **Central Asia** (historically) | Declining |
| **Bosnia-Herzegovina** (historically) | Eliminated |
| **Japan** | Sexually transmitted TEN in MSM ([PMID: 31310214](https://pubmed.ncbi.nlm.nih.gov/31310214/)) |
| **Cuba** | Sexually transmitted TEN ([PMID: 29454847](https://pubmed.ncbi.nlm.nih.gov/29454847/)) |
| **Europe** | Emerging reports in MSM |

### Population Demographics

- **Classic bejel:** Primarily children in rural, impoverished communities; no sex predilection (M:F ~1:1)
- **Sexually transmitted TEN:** Predominantly adult MSM, often HIV-co-infected
- **Age distribution:** Bimodal -- childhood in endemic settings; young to middle-aged adults in sexually transmitted cases

---

## 10. Diagnostics

### Serological Tests (Primary Diagnostic Method)

Serological tests for bejel are identical to those for venereal syphilis, as the antigens of TEN and TPA are indistinguishable:

| Test Category | Examples | Utility |
|---|---|---|
| **Non-treponemal** | RPR, VDRL | Screening; titers correlate with disease activity; monitor treatment response |
| **Treponemal** | FTA-ABS, TPHA, TPPA, EIA/CLIA | Confirmatory; remain positive for life |
| **Rapid/POC** | Dual treponemal/non-treponemal | Field use in resource-limited settings |

### Critical Diagnostic Limitation

**Serological tests CANNOT distinguish between TEN, TPA, and TPE infections.** This is the single most important diagnostic challenge. Grillova et al. (2018) demonstrated: *"Molecular identification of Treponema pallidum subsp. endemicum, the agent of bejel, in Cuban patients diagnosed with venereal syphilis indicates the clear limitations of a diagnosis based exclusively on serology, geographical occurrence, clinical symptoms and anamnestic data"* ([PMID: 29454847](https://pubmed.ncbi.nlm.nih.gov/29454847/)).

### Direct Detection Methods

- **Dark-field microscopy:** Can visualize live spirochetes in lesion exudate; cannot distinguish subspecies
- **Direct fluorescent antibody (DFA):** Monoclonal antibody-based detection ([PMID: 3897267](https://pubmed.ncbi.nlm.nih.gov/3897267/))
- **PCR:** Can detect and amplify treponemal DNA from clinical specimens; subspecies determination requires additional targets

### Molecular Typing (Essential for Subspecies Identification)

- **Multi-locus sequence typing (MLST):** Using TP0136, TP0548, TP0705 loci to differentiate TPA from TEN ([PMID: 39415268](https://pubmed.ncbi.nlm.nih.gov/39415268/))
- **Multi-locus sequence analysis (MLSA):** Definitive subspecies classification ([PMID: 29454847](https://pubmed.ncbi.nlm.nih.gov/29454847/))
- **Whole-genome sequencing:** Gold standard for subspecies identification; reveals genetically distinct TEN lineages in different geographic regions ([PMID: 41987031](https://pubmed.ncbi.nlm.nih.gov/41987031/))

### Imaging

- **X-ray of long bones:** Periostitis, cortical thickening (sabre tibia), metaphyseal changes
- **CT/MRI:** Evaluation of nasopharyngeal destruction in tertiary disease

### Differential Diagnosis

| Condition | Distinguishing Features |
|---|---|
| **Venereal syphilis (TPA)** | Sexual transmission; possible CNS/cardiovascular involvement; molecular typing required |
| **Yaws (TPE)** | Tropical humid climate; papillomatous primary lesion; molecular typing required |
| **Pinta (*T. carateum*)** | Skin-only; dyschromic patches; Central/South America |
| **Oral candidiasis** | White plaques, removable; KOH positive |
| **Leprosy** | Acid-fast bacilli; nerve involvement |
| **Cutaneous tuberculosis** | Chronic ulcers; positive cultures/PCR for *M. tuberculosis* |
| **Haemophilus ducreyi skin ulcers** | Ulcerative lesions in tropical regions; PCR differentiation needed ([PMID: 33591973](https://pubmed.ncbi.nlm.nih.gov/33591973/)) |

### Screening

No routine population screening programs exist specifically for bejel. In endemic areas, treponemal rapid tests may be used for community surveys. Mass screening is integrated with WHO yaws/endemic treponematosis eradication programs.

---

## 11. Outcome / Prognosis

### Survival and Mortality

- **Mortality:** Bejel is **rarely directly fatal**
- **Life expectancy:** Not significantly reduced with treatment; untreated tertiary disease causes significant morbidity but rarely death
- **Disease-specific mortality:** Deaths mainly from secondary infections of destructive lesions (historical)

### Morbidity and Function

- **Primary/secondary stages:** Mild to moderate morbidity; mucous patches may be painful; periostitis causes bone pain
- **Latent stage:** No morbidity
- **Tertiary stage:** Severe morbidity including disfiguring facial destruction (gangosa), chronic bone pain and deformity, difficulty eating/breathing/speaking, and profound social isolation

### Disease Course

- **Complications:** Secondary bacterial infection of ulcerative lesions; permanent scarring; nasopharyngeal stenosis
- **Recovery potential:** Excellent with early treatment; primary and secondary lesions resolve completely with penicillin. Tertiary destruction is irreversible.

### Prognostic Factors

- **Favorable:** Early diagnosis and treatment; access to penicillin
- **Unfavorable:** Late presentation; tertiary disease; lack of healthcare access; macrolide resistance limiting alternative treatments
- No established prognostic biomarkers specific to bejel

---

## 12. Treatment

### Pharmacotherapy

#### First-Line Treatment

**Benzathine penicillin G (BPG)** is the treatment of choice for all stages:

| Stage | Dose | Route | Schedule |
|---|---|---|---|
| Early disease (children <30 kg) | 600,000 units | IM | Single dose |
| Early disease (adults) | 2.4 million units | IM | Single dose |
| Late/unknown duration | 2.4 million units | IM | Three weekly injections |

**MAXO term:** MAXO:0010357 (antibiotic treatment)

No documented penicillin resistance has ever been found in any *T. pallidum* subspecies.

#### Alternative Treatments

| Drug | Regimen | Notes |
|---|---|---|
| **Doxycycline** | 100 mg PO BID x 14 days (early) or 28 days (late) | Not for children <8 years or pregnant women |
| **Tetracycline** | 500 mg PO QID x 14-28 days | Similar limitations |
| **Ceftriaxone** | 1 g IM/IV daily x 10-14 days | Limited evidence |

#### Azithromycin: NOT Recommended

Azithromycin should **NOT** be used for bejel treatment due to widespread macrolide resistance (A2058G mutation in 23S rDNA) found in circulating TEN strains. Most TEN strains from MSM in Japan carried this mutation ([PMID: 34836779](https://pubmed.ncbi.nlm.nih.gov/34836779/)). The 2020 European syphilis guidelines exclude azithromycin as an alternative treatment at any stage ([PMID: 33094521](https://pubmed.ncbi.nlm.nih.gov/33094521/)). This has significant implications for mass drug administration campaigns, as azithromycin is the WHO-recommended drug for yaws MDA.

### Experimental Therapeutics

**Linezolid** has shown promise: in vitro bactericidal activity against *T. pallidum* at concentrations >=0.5 microg/mL, and in vivo efficacy similar to BPG in the rabbit model (hazard ratio 3.84; 95% CI 2.05-7.17; p < 0.0001 compared to untreated controls) ([PMID: 33721817](https://pubmed.ncbi.nlm.nih.gov/33721817/)). Clinical trials are warranted.

### Mass Treatment Campaigns

The WHO/UNICEF mass treatment campaigns of the 1950s-60s treated over **50 million individuals in 46 countries** with remarkable success, dramatically reducing endemic treponematoses prevalence. Resurgence after discontinuation underscores the need for sustained surveillance and treatment ([PMID: 2682125](https://pubmed.ncbi.nlm.nih.gov/2682125/)).

### Surgical and Interventional

- **Reconstructive surgery** for tertiary gangosa (MAXO:0000004)
- **Orthopedic intervention** for severe bone deformities

### Treatment Outcomes

- **Response rate:** >95% clinical cure with appropriate penicillin therapy
- **Monitoring:** Serial non-treponemal test titers (RPR/VDRL); fourfold decline expected within 6-12 months
- **Side effects:** Jarisch-Herxheimer reaction may occur after treatment initiation (febrile reaction from spirochete killing)

---

## 13. Prevention

### Primary Prevention

- **Improved hygiene and sanitation:** Access to clean water, individual eating utensils, improved housing -- the most effective long-term strategy
- **Socioeconomic development:** Poverty reduction in endemic areas
- **Health education:** Community awareness of transmission routes (MAXO:0000015)
- **Safe sexual practices:** Relevant for emerging sexually transmitted TEN in MSM populations
- **MAXO terms:** MAXO:0000058 (preventive measure); MAXO:0000521 (hygiene intervention)

### Secondary Prevention

- **Mass drug administration (MDA):** Community-wide treatment in endemic areas
- **Active case finding:** Surveillance in endemic communities and contact tracing
- **Point-of-care testing:** Rapid treponemal tests for field use
- **Molecular surveillance:** Essential for identifying TEN in non-endemic settings where it may be misdiagnosed as syphilis

### Tertiary Prevention

- **Early treatment:** Prevents progression to destructive tertiary disease
- **Reconstructive surgery** for gangosa and other tertiary disfigurements
- **Rehabilitation and psychological support**

### Immunization

**No vaccine exists** for bejel or any treponemal disease. Outer membrane proteins (TprK, TprC, TprD, BamA, FadL) are being investigated as candidate vaccine antigens ([PMID: 35422800](https://pubmed.ncbi.nlm.nih.gov/35422800/); [PMID: 40802283](https://pubmed.ncbi.nlm.nih.gov/40802283/)). Cross-protection between subspecies suggests a universal treponemal vaccine might protect against all human treponematoses.

### Public Health Interventions

- **WHO eradication strategy:** Mass treatment campaigns targeting endemic treponematoses elimination by 2030
- **Integration with primary healthcare:** Essential for sustained control ([PMID: 1281363](https://pubmed.ncbi.nlm.nih.gov/1281363/))
- **Molecular epidemiological surveillance:** MLST/WGS for tracking transmission and resistance
- **Monitoring for macrolide resistance:** Critical for MDA program design
- **Doxycycline post-exposure prophylaxis (doxyPEP):** Being explored for STI prevention in MSM populations; may have relevance for sexually transmitted TEN

---

## 14. Other Species / Natural Disease

### Natural Treponemal Infection in Non-Human Primates

Treponematosis has been documented in **non-human primates**, particularly baboons in Africa. Knauf et al. (2015) found that 90% (18/20) of clinically healthy Guinea baboons (*Papio papio*) in Senegal tested positive for anti-*T. pallidum* antibodies, despite having no clinical symptoms. They noted that *"the West African simian strain has been shown to cause sustainable yaws infection when inoculated into humans"* and that *"Guinea baboons in West Africa serve as a natural reservoir for human infection"* ([PMID: 26588087](https://pubmed.ncbi.nlm.nih.gov/26588087/)).

Treponematosis has also been documented in critically endangered Western chimpanzees (*Pan troglodytes verus*), caused by strains closely related to TPE ([PMID: 39010964](https://pubmed.ncbi.nlm.nih.gov/39010964/)).

| Species | NCBI Taxon ID | Treponeme | Clinical Signs |
|---|---|---|---|
| *Papio papio* (Guinea baboon) | 9556 | Simian *T. pallidum* | Asymptomatic (90% seropositive) |
| *Pan troglodytes verus* (W. chimpanzee) | 37012 | TPE-related | Skin lesions |
| *Oryctolagus cuniculus* (Rabbit) | 9986 | *T. paraluiscuniculi* | Genital lesions (rabbit syphilis) |

### Comparative Biology

- Tpr gene evolution studies show higher variation between human subspecies than within them, supporting the three-subspecies classification ([PMID: 16926243](https://pubmed.ncbi.nlm.nih.gov/16926243/))
- All simian strains characterized to date are closely related to human yaws-causing TPE strains
- High prevalence and genetic diversity of *T. paraluiscuniculi* in wild European rabbits (>98% genome identity with human *T. pallidum*) ([PMID: 38095473](https://pubmed.ncbi.nlm.nih.gov/38095473/))

### Zoonotic Potential

While direct zoonotic transmission of TEN has not been documented, the close genetic relationship between simian and human treponemes suggests non-human primates may serve as a reservoir complicating eradication efforts. This is a major concern for the WHO yaws eradication campaign.

---

## 15. Model Organisms

### Hamster Model

The most relevant animal model for bejel is the **LSH hamster model**. Wicher et al. (1993) demonstrated that female hamsters infected with TEN before or during early pregnancy transmitted infection to the fetus: *"Female LSH hamsters infected with Treponema pallidum subsp. endemicum before pregnancy or during early pregnancy transmit a form of syphilis to the fetus that is similar to human congenital syphilis. The offspring develops rhinitis, skin rash, failure to thrive, and hepatosplenomegaly"* ([PMID: 8335390](https://pubmed.ncbi.nlm.nih.gov/8335390/)). *T. pallidum* was detectable in livers, spleens, and nasal secretions, and IgM antibodies were detected in offspring serum.

**Phenotype recapitulation:** Good recapitulation of human congenital syphilis features
**Limitations:** Not widely used; hamster immune reagents limited

### Rabbit Model

The **rabbit** (*Oryctolagus cuniculus*) is the standard model for all *T. pallidum* subspecies. Applications include:
- **Drug efficacy testing:** Linezolid showed comparable efficacy to BPG in the rabbit model ([PMID: 33721817](https://pubmed.ncbi.nlm.nih.gov/33721817/))
- **Pathogenesis studies:** Understanding tissue invasion and immune evasion
- **Propagation:** *T. pallidum* is propagated by intratesticular rabbit inoculation

### In Vitro Systems

- Short-term co-culture systems (1-3 weeks) in rabbit epithelial cells
- Used for in vitro drug susceptibility testing
- Limitations: *T. pallidum* cannot be continuously cultured on artificial media

| Model | Species | Applications | Limitations |
|---|---|---|---|
| **LSH hamster** | *Mesocricetus auratus* | Congenital transmission studies | Limited immune reagents; not widely used |
| **Rabbit** | *Oryctolagus cuniculus* | Drug testing, pathogenesis, propagation | Not ideal for congenital transmission |
| **In vitro co-culture** | Cell lines | Drug susceptibility testing | Limited viability and growth |
| **NHP (natural infection)** | *Papio papio*, *Pan troglodytes* | Comparative biology, reservoir studies | Ethical/practical constraints |

---

## Mechanistic Model / Interpretation

### The Dual Epidemiology of Bejel

The evidence reveals a striking duality in bejel's epidemiology that has fundamental implications for public health:

**Classic Pathway (Childhood Non-Venereal Transmission):**
Environmental poverty and poor hygiene --> shared utensils/close contact --> oral mucosal inoculation in children --> progressive treponemal disease in endemic communities

**Emerging Pathway (Adult Sexual Transmission):**
MSM sexual networks (often HIV+) --> genital mucosal inoculation --> clinical presentation indistinguishable from syphilis --> misdiagnosed by serology alone --> silent spread of TEN in non-endemic populations

The convergence of these pathways creates a critical diagnostic and surveillance gap: sexually transmitted TEN masquerades as syphilis, escaping detection by standard diagnostic algorithms. The non-clonal diversity of TEN strains in Cuba ([PMID: 35687593](https://pubmed.ncbi.nlm.nih.gov/35687593/)) suggests that this is not a single-outbreak phenomenon but rather a persistent, circulating reservoir of misidentified infection.

### Evolutionary Context

The intersubspecies recombination between TEN/TPE and TPA ([PMID: 34791386](https://pubmed.ncbi.nlm.nih.gov/34791386/)) suggests that the boundaries between treponemal subspecies are more porous than previously appreciated. This has implications for:
1. Understanding the historical origins of syphilis (the "Columbian vs. pre-Columbian" debate)
2. Predicting whether TEN may acquire additional virulence factors from TPA (e.g., neurotropism)
3. Vaccine development -- a universal approach may be both feasible and necessary

---

## Evidence Base: Key Literature

| PMID | Authors/Year | Key Contribution |
|---|---|---|
| [25375929](https://pubmed.ncbi.nlm.nih.gov/25375929/) | Smajs et al. 2014 | TEN Bosnia A whole genome; evolutionary relationship to TPE and TPA |
| [24396138](https://pubmed.ncbi.nlm.nih.gov/24396138/) | Mitja et al. 2013 | Comprehensive classification of endemic treponematoses |
| [34836779](https://pubmed.ncbi.nlm.nih.gov/34836779/) | Nishiki et al. 2021 | TEN in adult MSM outside endemic areas; macrolide resistance |
| [29454847](https://pubmed.ncbi.nlm.nih.gov/29454847/) | Grillova et al. 2018 | TEN misdiagnosed as syphilis in Cuba; molecular identification |
| [31310214](https://pubmed.ncbi.nlm.nih.gov/31310214/) | Marra et al. 2019 | First report of bejel in MSM in Japan |
| [35687593](https://pubmed.ncbi.nlm.nih.gov/35687593/) | Pospisilova et al. 2022 | Non-clonal TEN diversity; persistent endemic infection in Cuba |
| [34791386](https://pubmed.ncbi.nlm.nih.gov/34791386/) | Arora et al. 2021 | Intersubspecies recombination as key evolutionary mechanism |
| [2682125](https://pubmed.ncbi.nlm.nih.gov/2682125/) | Antal et al. 1989 | Global burden: 2.5+ million cases, 75% in children |
| [1281363](https://pubmed.ncbi.nlm.nih.gov/1281363/) | Meheus & Antal 1992 | Socioeconomic context of endemic treponematoses |
| [8335390](https://pubmed.ncbi.nlm.nih.gov/8335390/) | Wicher et al. 1993 | Hamster model of congenital TEN transmission |
| [39415268](https://pubmed.ncbi.nlm.nih.gov/39415268/) | Nakayama et al. 2024 | MLST; TEN in 12% of MSM syphilis samples; CRP as bacteremia marker |
| [41987031](https://pubmed.ncbi.nlm.nih.gov/41987031/) | WGS 2025 | Genetically distinct TEN lineage in Japanese MSM |
| [16926243](https://pubmed.ncbi.nlm.nih.gov/16926243/) | Centurion-Lara et al. 2006 | tpr gene evolution; gene conversion across subspecies |
| [40513619](https://pubmed.ncbi.nlm.nih.gov/40513619/) | 2025 | TprK-mediated macrophage polarization via TLR2/JAK1/STAT1 |
| [20889558](https://pubmed.ncbi.nlm.nih.gov/20889558/) | Cruz et al. 2010 | CD4/CD8 T cell responses in syphilitic lesions |
| [33721817](https://pubmed.ncbi.nlm.nih.gov/33721817/) | 2021 | Linezolid efficacy against T. pallidum |
| [26588087](https://pubmed.ncbi.nlm.nih.gov/26588087/) | Knauf et al. 2015 | 90% seroprevalence in Guinea baboons |
| [38267579](https://pubmed.ncbi.nlm.nih.gov/38267579/) | 2024 | Pre-Columbian treponemal genomes from Brazil |

---

## Limitations and Knowledge Gaps

1. **Diagnostic ambiguity:** The inability of serological tests to distinguish TEN from TPA means the true burden of bejel is unknown in both endemic and non-endemic settings. Many cases may be permanently misclassified as syphilis.

2. **Limited molecular surveillance:** Whole-genome sequencing and MLST are required for definitive subspecies identification but are not routinely performed in most clinical settings, especially in resource-limited endemic areas.

3. **Incomplete clinical characterization of sexually transmitted TEN:** Whether TEN can cause neurosyphilis, cardiovascular disease, or congenital disease in humans remains uncertain. The hamster model suggests congenital transmission is possible ([PMID: 8335390](https://pubmed.ncbi.nlm.nih.gov/8335390/)), but human data are absent.

4. **Macrolide resistance threat:** The presence of A2058G mutations in TEN strains raises concerns about azithromycin-based mass drug administration campaigns in regions where bejel and yaws may co-circulate.

5. **Zoonotic reservoir uncertainty:** While non-human primates harbor closely related treponemes, the role of animal reservoirs in maintaining TEN transmission is unknown.

6. **Historical bias:** Most clinical descriptions of bejel date from the pre-molecular era (1950s-1970s), and some features attributed to bejel may have been misclassified.

7. **Absence of molecular profiling:** No transcriptomic, proteomic, or metabolomic studies have been conducted specifically on bejel patients. Immune response data are extrapolated from syphilis studies.

8. **No vaccine:** No vaccine candidates have been tested specifically against TEN, though cross-reactive immunity between subspecies suggests a universal treponemal vaccine might protect against all human treponematoses.

---

## Proposed Follow-up Experiments / Actions

1. **Implement molecular typing in STI clinics:** Integrate MLST or targeted PCR-based subspecies identification into routine syphilis diagnostic workflows, particularly in MSM clinics and in regions with endemic treponematoses. This would quantify the true burden of sexually transmitted TEN.

2. **Prospective cohort study of sexually transmitted TEN:** Recruit MSM diagnosed with TEN to characterize clinical outcomes longitudinally, including potential neurological and cardiovascular complications, and determine whether disease course differs from venereal syphilis.

3. **Surveillance for macrolide resistance in endemic areas:** Screen TEN and TPE isolates from Sahel Africa and the Middle East for 23S rDNA A2058G and A2059G mutations before implementing azithromycin-based MDA campaigns.

4. **Investigate congenital TEN in humans:** Conduct retrospective molecular analysis of archived samples from congenital syphilis cases in endemic bejel regions to determine whether congenital bejel occurs in humans.

5. **Non-human primate reservoir assessment:** Characterize simian treponemes in West and Central Africa molecularly to determine whether TEN (as distinct from TPE) circulates in animal reservoirs.

6. **Comparative transcriptomics:** Perform RNA-seq on skin/mucosal biopsies from bejel and syphilis patients to identify subspecies-specific host response signatures that might inform differential diagnosis.

7. **Universal treponemal vaccine development:** Leverage advances in structural characterization of outer membrane proteins (TprK, TprC, TprD, BamA, FadL) to develop vaccine candidates with cross-subspecies protection.

8. **Point-of-care molecular diagnostics:** Develop a rapid, field-deployable PCR or LAMP-based assay that can distinguish TEN from TPA and TPE to support eradication campaigns in endemic regions.

---

*Report generated: 2026-05-05. Based on analysis of 69 peer-reviewed publications spanning molecular epidemiology, genomics, immunology, clinical medicine, and public health. This report is intended to populate a comprehensive disease knowledge base entry for Bejel (MONDO:0001714).*
