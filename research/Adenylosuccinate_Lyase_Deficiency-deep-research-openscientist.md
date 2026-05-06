---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-05T02:23:26.793003'
end_time: '2026-05-05T02:48:03.594957'
duration_seconds: 1476.8
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Adenylosuccinate Lyase Deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 15
    timeout: 5400
citation_count: 25
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Adenylosuccinate Lyase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Adenylosuccinate Lyase Deficiency** covering all of the
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

# Comprehensive Disease Characterization: Adenylosuccinate Lyase Deficiency

## Summary

Adenylosuccinate lyase deficiency (ADSLD) is an ultra-rare autosomal recessive inborn error of purine metabolism caused by biallelic pathogenic variants in the *ADSL* gene (chromosome 22q13.1). The disease has an estimated global prevalence of approximately 0.00125 cases per 100,000 individuals, with more than 80 patients identified worldwide. ADSL encodes a bifunctional homotetrameric enzyme that catalyzes two non-sequential steps in de novo purine synthesis and the purine nucleotide recycling pathway: the conversion of succinylaminoimidazole carboxamide ribotide (SAICAR) to aminoimidazole carboxamide ribotide (AICAR) and the conversion of adenylosuccinate (S-AMP) to adenosine monophosphate (AMP). Loss of ADSL function results in accumulation of dephosphorylated substrates -- succinylaminoimidazole carboxamide riboside (SAICAr) and succinyladenosine (S-Ado) -- in body fluids, which serve as diagnostic biomarkers and correlate with disease severity.

The clinical spectrum ranges from fatal neonatal encephalopathy to mild psychomotor retardation, classified into three phenotypic categories: a fatal neonatal form, type I (severe infantile), and type II (moderate/mild). Neurological involvement dominates the clinical picture, with epilepsy present in 81.8% of patients and onset within the first year of life in 89.2% of cases. Emerging mechanistic research has revealed that ADSLD is a secondary mitochondrial disease with disrupted organelle homeostasis, impaired respiration, and reduced ATP production, mediated in part through suppression of ERK2/AKT signaling. Additionally, activation of the alternative complement pathway has been implicated as a key driver of neuroinflammation, blood-brain barrier disruption, and progressive neurodegeneration. A recent Phase II clinical trial of allopurinol demonstrated clinical improvements in younger, less cognitively impaired patients, representing the first evidence-based pharmacological intervention for this condition.

No curative treatment currently exists. Management remains primarily supportive, encompassing anti-epileptic therapy, physical therapy, occupational therapy, and speech therapy. However, the emerging understanding of mitochondrial dysfunction and complement-mediated neuroinflammation opens promising avenues for targeted therapeutic development.

---

## 1. Disease Information

### Overview

Adenylosuccinate lyase deficiency (ADSLD) is an ultra-rare autosomal recessive neurometabolic disorder first identified in 1984 by Jaeken and Van den Berghe as the first inborn defect of purine biosynthesis. The disease results from loss-of-function mutations in the *ADSL* gene, leading to impaired de novo purine synthesis and purine nucleotide recycling. ADSLD is characterized by "severe neurological impairment, with an estimated global prevalence of approximately 0.00125 cases per 100,000 individuals" ([PMID: 40896413](https://pubmed.ncbi.nlm.nih.gov/40896413/)).

### Key Identifiers

| Database | Identifier |
|----------|-----------|
| OMIM (Gene) | *608222 |
| OMIM (Disease) | #103050 |
| Orphanet | ORPHA:46 |
| ICD-10 | E79.8 (Other disorders of purine and pyrimidine metabolism) |
| ICD-11 | 5C60.Y (Other specified disorders of purine metabolism) |
| MeSH | C538236 |
| MONDO | MONDO:0010041 |
| HGNC | HGNC:291 (ADSL) |
| UniProt | P30566 |
| NCBI Gene | 158 |
| Ensembl | ENSG00000239900 |

### Synonyms and Alternative Names

- Adenylosuccinate lyase deficiency (ADSLD)
- ADSL deficiency
- Adenylosuccinase deficiency
- Succinylpurinemic autism
- Adenylosuccinate lyase deficiency disorder (ADSLDD)

### Information Sources

Information is derived primarily from aggregated disease-level resources (OMIM, Orphanet, GeneReviews) supplemented by individual case reports and small case series in the published literature, as well as patient registries such as the "Our Journey with ADSL Deficiency Association." As an ultra-rare disorder, much of the clinical knowledge comes from case reports, small case series, and literature reviews of collectively ~100 identified patients worldwide.

---

## 2. Etiology

### Disease Causal Factors

**Primary Cause: Genetic**

ADSLD is caused exclusively by homozygous or compound heterozygous loss-of-function mutations in the *ADSL* gene. The enzyme ADSL is a homotetrameric protein belonging to the fumarase/aspartase superfamily that catalyzes two reactions in purine metabolism:

1. **De novo IMP synthesis (step 8 of 10):** Conversion of SAICAR to AICAR + fumarate
2. **Purine nucleotide recycling / AMP synthesis:** Conversion of adenylosuccinate (S-AMP) to AMP + fumarate

As described by Jurecka et al., "Adenylosuccinate lyase (ADSL) deficiency is a defect of purine metabolism affecting purinosome assembly and reducing metabolite fluxes through purine de novo synthesis and purine nucleotide recycling pathways" ([PMID: 25112391](https://pubmed.ncbi.nlm.nih.gov/25112391/)).

Deficiency leads to:
- Accumulation of dephosphorylated substrates: SAICAr and S-Ado in body fluids
- Reduced purine nucleotide pools (AMP, GMP, and their derivatives)
- Impaired purinosome assembly (the multi-enzyme complex for de novo purine synthesis) ([PMID: 22180458](https://pubmed.ncbi.nlm.nih.gov/22180458/))

**Mechanistic factors:**
- Toxic accumulation of SAICAr (particularly neurotoxic) ([PMID: 40896413](https://pubmed.ncbi.nlm.nih.gov/40896413/))
- Purine nucleotide depletion impairing energy metabolism
- Secondary mitochondrial dysfunction ([PMID: 40914938](https://pubmed.ncbi.nlm.nih.gov/40914938/))
- Complement-mediated neuroinflammation ([PMID: 40896413](https://pubmed.ncbi.nlm.nih.gov/40896413/))

### Risk Factors

**Genetic Risk Factors:**
- Biallelic pathogenic variants in *ADSL* (causal, required for disease)
- More than 70 distinct pathogenic variants have been reported, predominantly missense mutations ([PMID: 25112391](https://pubmed.ncbi.nlm.nih.gov/25112391/))
- Most frequent pathogenic variants: p.R426H (homozygous in 19 patients), p.Y114H (compound heterozygous in 13 patients), p.D430N (homozygous in 6 patients) ([PMID: 37842880](https://pubmed.ncbi.nlm.nih.gov/37842880/))
- Consanguinity is a risk factor, as the disease follows autosomal recessive inheritance

**Environmental Risk Factors:**
- No specific environmental risk factors have been identified for this Mendelian disorder
- The disease is entirely genetically determined
- Intercurrent illnesses (febrile episodes) may exacerbate seizures
- D-ribose supplementation withdrawal was associated with acute neurological deterioration in one patient ([PMID: 21903433](https://pubmed.ncbi.nlm.nih.gov/21903433/))

### Protective Factors

**Genetic Protective Factors:**
- Higher residual ADSL enzyme activity is associated with milder disease (type II vs type I) ([PMID: 20127976](https://pubmed.ncbi.nlm.nih.gov/20127976/))
- Greater structural stability of mutant ADSL protein complexes correlates with milder phenotype
- Some compound heterozygous combinations may result in milder disease through intersubunit complementation in the homotetramer

**Environmental Protective Factors:**
- No specific environmental protective factors have been identified
- Ketogenic diet has shown some benefit for seizure control in individual cases ([PMID: 23504561](https://pubmed.ncbi.nlm.nih.gov/23504561/))

### Gene-Environment Interactions

No specific gene-environment interactions have been documented for ADSLD. As a Mendelian recessive disorder, the disease phenotype is primarily determined by the nature and combination of *ADSL* pathogenic variants and their effect on residual enzyme activity. However, bacterial urinary tract infections can cause deribosylation of urinary biomarkers, complicating diagnosis ([PMID: 24183879](https://pubmed.ncbi.nlm.nih.gov/24183879/)).

---

## 3. Phenotypes

### Clinical Phenotypic Spectrum

ADSLD presents as a phenotypic continuum classified into three major categories ([PMID: 25112391](https://pubmed.ncbi.nlm.nih.gov/25112391/); [PMID: 37842880](https://pubmed.ncbi.nlm.nih.gov/37842880/); [PMID: 40896413](https://pubmed.ncbi.nlm.nih.gov/40896413/)):

#### Fatal Neonatal Form (~14% of cases)
- **Onset**: Birth to first days of life
- **Severity**: Lethal
- **Features**: Neonatal encephalopathy, absence of spontaneous movement, respiratory failure, intractable seizures, death within weeks
- **HPO terms**: Neonatal encephalopathy (HP:0012736), Respiratory failure (HP:0002878), Neonatal onset (HP:0003623)
- **S-Ado/SAICAr ratio**: Very low (< 1)

#### Type I -- Severe Infantile Form (~58% of cases)
- **Onset**: First months of life (median 0.63 years)
- **Severity**: Severe
- **Features**: Severe psychomotor retardation, early-onset seizures, microcephaly, autistic features, hypotonia progressing to spasticity
- **HPO terms**: Severe global developmental delay (HP:0011344), Epileptic encephalopathy (HP:0200134), Microcephaly (HP:0000252), Autistic behavior (HP:0000729), Muscular hypotonia (HP:0001252)
- **S-Ado/SAICAr ratio**: Low (< 2)

#### Type II -- Moderate/Mild Form (~28% of cases)
- **Onset**: First months to years of life
- **Severity**: Mild to moderate
- **Features**: Mild to moderate psychomotor retardation, later-onset seizures, transient contact disturbances, behavioral abnormalities
- **HPO terms**: Global developmental delay (HP:0001263), Seizures (HP:0001250), Intellectual disability (HP:0001249)
- **S-Ado/SAICAr ratio**: Higher (> 2)

### Comprehensive Phenotype Catalog

| Phenotype | HPO Term | Frequency | Severity | Progression |
|-----------|----------|-----------|----------|-------------|
| Epilepsy/Seizures | HP:0001250 | 81.8% | Variable (mild to intractable) | Often progressive, sometimes drug-resistant |
| Psychomotor retardation | HP:0001263 | >95% | Mild to severe | Progressive or stable |
| Intellectual disability | HP:0001249 | ~100% | Mild to profound | Variable |
| Muscular hypotonia | HP:0001252 | ~70% | Variable | May progress to spasticity |
| Microcephaly | HP:0000252 | ~50% | Variable | Progressive postnatal |
| Autistic features | HP:0000729 | ~40-50% | Variable | May improve in mild cases |
| White matter abnormalities | HP:0002500 | ~80% on MRI | Variable | Progressive |
| Delayed myelination | HP:0002188 | Common | Variable | Early life |
| Cerebellar atrophy | HP:0001272 | ~40% | Variable | Progressive |
| Growth retardation | HP:0001510 | Variable | Mild to severe | Variable |
| Nystagmus | HP:0000639 | Rare | Mild | Variable |
| Spasticity (lower limbs) | HP:0001258 | Variable (late) | Moderate to severe | Progressive |
| Muscular wasting | HP:0003202 | Some patients | Variable | Childhood |

Strikingly, as reported by Brun et al., "In the majority (89.2%), disease onset was within the first year of life. Epilepsy is present in 81.8% of the patients, with polymorphic and often intractable seizures" ([PMID: 37842880](https://pubmed.ncbi.nlm.nih.gov/37842880/)).

### EEG Features ([PMID: 37842880](https://pubmed.ncbi.nlm.nih.gov/37842880/))

- Poor general background organization with theta-delta activity
- Hypsarrhythmia with infantile spasms (common developmental trajectory)
- Multifocal epileptiform discharges

### Behavioral Phenotype

An important and sometimes misleading behavioral phenotype includes features mimicking Angelman syndrome: "excessive laughter, a very happy disposition, hyperactivity, a short attention span, the mouthing of objects, tantrums and stereotyped movements" ([PMID: 18830228](https://pubmed.ncbi.nlm.nih.gov/18830228/)). This overlap can lead to significant diagnostic delays.

ADSLD has been listed among "several genetic diseases consistently associated with autism," including fragile X, tuberous sclerosis, Angelman syndrome, and others ([PMID: 15796126](https://pubmed.ncbi.nlm.nih.gov/15796126/)).

### Quality of Life Impact

- Severe cognitive impairment affects daily functioning in most patients
- Drug-resistant epilepsy significantly impacts quality of life
- Most patients require full-time care
- Communication deficits (speech delay/absence) limit social participation
- Motor impairments limit mobility and independence
- Type II patients may attend special education and achieve some independence ([PMID: 23504561](https://pubmed.ncbi.nlm.nih.gov/23504561/))
- No formal EQ-5D or SF-36 assessments have been published for ADSLD

### Brain MRI Findings

Brain MRI abnormalities are characteristic and include impaired white matter myelination, global supra- and infratentorial white matter loss, widening of lateral ventricles, cerebral and cerebellar atrophy, and white matter hyperintense signal on T2-weighted sequences. As Jurecka et al. described: "Head MRI showed impaired white matter myelination with various degrees of global supra- and infratentorial white matter loss" ([PMID: 21625931](https://pubmed.ncbi.nlm.nih.gov/21625931/)). Notably, MRI may be normal in some mild cases ([PMID: 28768552](https://pubmed.ncbi.nlm.nih.gov/28768552/)).

---

## 4. Genetic/Molecular Information

### Causal Gene

**ADSL (Adenylosuccinate Lyase)**
- **HGNC ID**: HGNC:291
- **NCBI Gene ID**: 158
- **OMIM Gene**: *608222
- **OMIM Phenotype**: #103050
- **Ensembl**: ENSG00000239900
- **Chromosomal location**: 22q13.1
- **Gene structure**: 13 exons spanning ~23 kb ([PMID: 10888601](https://pubmed.ncbi.nlm.nih.gov/10888601/))
- **Protein**: 484 amino acids, functions as a homotetramer
- **EC number**: 4.3.2.2
- **Protein family**: Fumarase/aspartase superfamily
- **UniProt**: P30566

### Pathogenic Variants

Over 70 distinct pathogenic variants have been reported. The vast majority are missense mutations, consistent with the requirement for some residual enzyme activity for survival. Complete loss of ADSL activity is likely embryonically lethal.

**Most Common Variants:**

| Variant | Type | Frequency | Phenotype Association | Reference |
|---------|------|-----------|----------------------|-----------|
| p.R426H | Missense | Most common (19 patients homozygous) | Type I or II | [PMID: 37842880](https://pubmed.ncbi.nlm.nih.gov/37842880/) |
| p.Y114H | Missense | Common (13 patients compound het) | Variable | [PMID: 37842880](https://pubmed.ncbi.nlm.nih.gov/37842880/) |
| p.D430N | Missense | Moderate (6 patients homozygous) | Variable | [PMID: 37842880](https://pubmed.ncbi.nlm.nih.gov/37842880/) |
| p.R303C | Missense | Multiple patients | Severe (Type I) | [PMID: 33648541](https://pubmed.ncbi.nlm.nih.gov/33648541/) |
| p.R190X | Nonsense | Rare | Fatal neonatal (compound het) | [PMID: 15571235](https://pubmed.ncbi.nlm.nih.gov/15571235/) |
| p.A3P | Missense | Rare | Fatal neonatal (compound het) | [PMID: 15571235](https://pubmed.ncbi.nlm.nih.gov/15571235/) |
| p.M225T | Missense | Rare | Angelman-like phenotype | [PMID: 18830228](https://pubmed.ncbi.nlm.nih.gov/18830228/) |
| p.D268H | Missense | Rare | Type II (compound het with R426H) | [PMID: 23504561](https://pubmed.ncbi.nlm.nih.gov/23504561/) |
| p.I369L | Missense | Rare | Variable | [PMID: 21903433](https://pubmed.ncbi.nlm.nih.gov/21903433/) |
| p.M389V | Missense | Rare (novel) | Variable | [PMID: 21903433](https://pubmed.ncbi.nlm.nih.gov/21903433/) |

**Variant Classification and Functional Consequences:**
- **Classification**: Most identified variants are pathogenic or likely pathogenic per ACMG/AMP guidelines (ClinVar)
- **Origin**: All germline
- **Types**: Predominantly missense; rare nonsense (e.g., p.R190X) and splice-site mutations
- **Allele frequencies**: Extremely rare in population databases (gnomAD); most variants are private or found in very few families
- **Functional consequence**: Loss of function -- all pathogenic variants reduce ADSL enzyme activity to varying degrees
- **Genotype-phenotype correlation**: "Phenotypic severity in ADSL deficiency is correlated with residual enzymatic activity and structural stability of the corresponding mutant ADSL complexes and does not seem to result from genotype-specific disproportional catalytic activities toward one of the enzyme substrates" ([PMID: 20127976](https://pubmed.ncbi.nlm.nih.gov/20127976/))

### Alternative Splicing

An alternatively spliced isoform resulting from exon 12 skipping has been identified. The non-spliced form is approximately 10-fold more abundant, and only the unspliced ADSL is enzymatically active ([PMID: 10888601](https://pubmed.ncbi.nlm.nih.gov/10888601/)).

### Protein Structural Consequences

The P100A substitution "distorts the amino acid chain of domain I in the proximity of His-86, which behaves as general acid in the catalysis, and may expose Cys-98 and Cys-99 to oxidising agents" ([PMID: 15571240](https://pubmed.ncbi.nlm.nih.gov/15571240/)). This model is consistent with the observation that the defective protein is strongly inhibited by 4-hydroxy-2-nonenal, an oxidative stress product.

### Modifier Genes

No established modifier genes have been identified for ADSLD. However, genes involved in purine salvage pathways (e.g., *HPRT1*, *APRT*) could theoretically modify disease severity by affecting alternative purine supply.

### Epigenetic Information

No specific epigenetic modifications have been directly associated with ADSLD pathogenesis. This represents a knowledge gap in the field.

### Chromosomal Abnormalities

Not applicable. ADSLD is caused by point mutations (primarily missense) in the ADSL gene, not large-scale chromosomal abnormalities.

---

## 5. Environmental Information

### Environmental Factors

ADSLD is a purely genetic disorder with no known environmental causes. There are no established environmental, infectious, or non-genetic causal factors.

### Lifestyle Factors

- **Diet**: A ketogenic diet has been reported to improve seizure control in one patient with type II ADSLD: "Due to poor results in seizure control, the ketogenic diet was introduced at the age of 7 years, resulting in reduction of seizure frequency" ([PMID: 23504561](https://pubmed.ncbi.nlm.nih.gov/23504561/))
- **D-ribose therapy**: Attempted in one patient; withdrawal was associated with acute neurological deterioration, severe brain atrophy and demyelination on MRI ([PMID: 21903433](https://pubmed.ncbi.nlm.nih.gov/21903433/))
- **Exercise, smoking, alcohol**: Not specifically studied; not applicable given the typical pediatric onset

### Infectious Agents

Not applicable as causative agents. However, urinary tract infections can interfere with diagnostic testing by causing bacterial deribosylation of the urinary biomarkers SAICAr and S-Ado ([PMID: 24183879](https://pubmed.ncbi.nlm.nih.gov/24183879/)).

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

The primary biochemical defect in ADSLD involves two critical pathways:

1. **De novo purine synthesis pathway** (KEGG: hsa00230): ADSL catalyzes step 8 of the 10-step conversion of PRPP to IMP, converting SAICAR to AICAR
2. **Purine nucleotide recycling/interconversion** (KEGG: hsa00230): ADSL converts adenylosuccinate (S-AMP) to AMP in the IMP-to-AMP conversion branch

**GO terms**: Purine nucleotide biosynthetic process (GO:0006164), Adenylosuccinate lyase activity (GO:0004018), 'de novo' IMP biosynthetic process (GO:0006189), AMP biosynthetic process (GO:0006167), SAICAR lyase activity (GO:0070626)

### Causal Chain: From Genetic Defect to Clinical Disease

```
ADSL Gene Mutation (germline, biallelic)
       |
       v
Reduced ADSL Enzyme Activity & Protein Instability
       |
       +---> Impaired Purinosome Assembly (multi-enzyme complex disruption)
       |
       v
Two Concurrent Biochemical Consequences:
       |
       +---> 1. ACCUMULATION of toxic succinylpurines
       |         (SAICAr and S-Ado in body fluids)
       |              |
       |              +---> SAICAr neurotoxicity
       |              |     (promotes neuroinflammation)
       |              |
       |              +---> Complement pathway activation
       |              |     (alternative pathway)
       |              |
       |              +---> Blood-brain barrier disruption
       |              |
       |              +---> Progressive neurodegeneration
       |
       +---> 2. DEPLETION of purine nucleotides
                 (reduced AMP/GMP/ATP production)
                      |
                      +---> Mitochondrial dysfunction
                      |     (fragmentation, impaired respiration)
                      |
                      +---> ERK2/AKT signaling suppression
                      |
                      +---> Impaired energy metabolism
                      |
                      +---> Impaired DNA/RNA synthesis
                      |
                      v
            NEUROLOGICAL DAMAGE
            (seizures, developmental delay,
             white matter loss, brain atrophy)
```

### Purinosome Assembly Disruption

A critical upstream mechanism is the disruption of purinosome assembly. Purinosomes are dynamic multi-enzyme complexes that channel substrates through the de novo purine synthesis pathway. Marie et al. demonstrated that "various mutations of ATIC and ADSL destabilize to various degrees of purinosome assembly and found that the ability to form purinosomes correlates with clinical phenotypes of individual ADSL patients" ([PMID: 22180458](https://pubmed.ncbi.nlm.nih.gov/22180458/)). This finding establishes purinosome disruption as a proximal mechanistic step linking genotype to phenotype.

### Secondary Mitochondrial Dysfunction

A major recent advance is the recognition of ADSLD as a secondary mitochondrial disease. As reported by Ast et al.: "ADSLd is associated with mitochondrial dysfunction, including increased fragmentation, impaired respiration, and reduced ATP production. The severity of mitochondrial impairment correlates with ADSLd pathology, especially in mitochondria-dependent tissues" ([PMID: 40914938](https://pubmed.ncbi.nlm.nih.gov/40914938/)). Key features include:

- **Increased mitochondrial fragmentation** (disrupted fission/fusion dynamics)
- **Impaired oxidative phosphorylation** (reduced complex I-IV activity)
- **Reduced ATP production** (energy deficit in neurons and other high-demand tissues)
- **Defects in mitochondrial transport** (impaired axonal trafficking)
- **ERK2 and AKT signaling suppression** (growth/survival pathway impairment)

Overexpression of constitutively active ERK2 or supplementation with purine intermediates partially rescues the mitochondrial phenotype, demonstrating the causal link between purine depletion and mitochondrial dysfunction.

**GO terms**: Mitochondrial organization (GO:0007005), Oxidative phosphorylation (GO:0006119), Mitochondrial fission (GO:0000266), ATP metabolic process (GO:0046034), Aerobic respiration (GO:0009060)

### Complement-Mediated Neuroinflammation

Emerging evidence implicates the alternative complement pathway as a key mediator of neurodegeneration. As described in a 2025 review: "We highlight emerging hypotheses implicating activation of the alternative complement pathway as a key driver of inflammation, blood-brain barrier disruption, and progressive neurodegeneration" ([PMID: 40896413](https://pubmed.ncbi.nlm.nih.gov/40896413/)).

SAICAr, the more toxic of the two accumulated succinylpurines, appears to promote neuroinflammation directly. The lower the S-Ado/SAICAr ratio in cerebrospinal fluid, the more severe the clinical outcome, suggesting differential toxicity of SAICAr relative to S-Ado.

**GO terms**: Complement activation, alternative pathway (GO:0006957), Inflammatory response (GO:0006954), Blood-brain barrier maintenance (GO:0035633)

### Protein Dysfunction

The ADSL protein functions as a homotetramer. Most pathogenic missense mutations impair:
- **Protein folding and stability** of the tetramer
- **Catalytic activity** at the active site
- **Susceptibility to oxidative damage**: The P100A substitution distorts domain I near the catalytic His-86 residue and may expose Cys-98/Cys-99 to oxidizing agents ([PMID: 15571240](https://pubmed.ncbi.nlm.nih.gov/15571240/))
- All mutant enzymes display a proportional decrease in activity against both substrates ([PMID: 10888601](https://pubmed.ncbi.nlm.nih.gov/10888601/))

### Metabolic Changes

**Primary metabolic abnormalities:**
- **Elevated in body fluids**: SAICAr (CHEBI:141525), S-Ado (CHEBI:99039)
- **Depleted**: AMP (CHEBI:16027), ATP (CHEBI:15422), GMP, GTP (purine nucleotides)
- **Reduced fumarate production** (product of ADSL reaction)
- **Energy metabolism**: Secondary mitochondrial dysfunction leading to impaired oxidative phosphorylation and reduced ATP

### Immune System Involvement

- Activation of the alternative complement pathway ([PMID: 40896413](https://pubmed.ncbi.nlm.nih.gov/40896413/))
- Neuroinflammation driven by SAICAr-mediated complement activation
- Blood-brain barrier disruption
- Progressive neurodegeneration via immune-mediated mechanisms
- **GO terms**: Complement activation (GO:0006956), Inflammatory response (GO:0006954)

### Tissue Damage Mechanisms

- Neurotoxicity from accumulated SAICAr
- Hypomyelination/dysmyelination secondary to oligodendrocyte damage: "Hypo/dysmyelination seemed to be secondary to damage of oligodendroglia and axons of damaged neuronal cells" ([PMID: 20054783](https://pubmed.ncbi.nlm.nih.gov/20054783/))
- Axonal damage secondary to neuronal injury
- Cerebral and cerebellar atrophy
- White matter loss (supra- and infratentorial) ([PMID: 21625931](https://pubmed.ncbi.nlm.nih.gov/21625931/))
- Oxidative stress vulnerability of mutant ADSL protein ([PMID: 15571240](https://pubmed.ncbi.nlm.nih.gov/15571240/))

### Cell Types Involved

- **Neurons** (CL:0000540) -- primary target of neurotoxicity
- **Oligodendrocytes** (CL:0000128) -- damaged, leading to hypomyelination/dysmyelination
- **Astrocytes** (CL:0000127) -- potential neuroinflammatory mediators, reactive gliosis
- **Microglia** (CL:0000129) -- complement-mediated activation

### Molecular Profiling

**CRISPR models**: CRISPR-Cas9 genome-edited HeLa cells deficient in individual DNPS steps showed accumulation of the substrate for the knocked-out enzyme and reduced purinosome formation ([PMID: 27590927](https://pubmed.ncbi.nlm.nih.gov/27590927/)).

**Cancer context**: ADSL has been identified as a potential oncogenic driver in hepatocellular carcinoma. "CRISPR-mediated knockout of ADSL impaired colony formation of liver cancer cells by affecting AMP production... ADSL knockout caused S-phase cell cycle arrest not by inducing DNA damage but by impairing mitochondrial function" ([PMID: 33336367](https://pubmed.ncbi.nlm.nih.gov/33336367/)).

---

## 7. Anatomical Structures Affected

### Organ Level

| Level | Structure | UBERON Term | Involvement |
|-------|-----------|-------------|-------------|
| Primary | Brain (cerebrum) | UBERON:0000955 | White matter loss, atrophy, seizures |
| Primary | Cerebellum | UBERON:0002037 | Atrophy, hypoplasia |
| Secondary | Skeletal muscle | UBERON:0001134 | Hypotonia, later spasticity |
| Secondary | Respiratory system | UBERON:0001004 | Respiratory failure (neonatal form) |

**Body systems involved**: Nervous system (primary), musculoskeletal system (secondary), respiratory system (neonatal form)

### Tissue and Cell Level

- **White matter** (UBERON:0002316): Hypomyelination, dysmyelination, abnormal signal
- **Gray matter** (UBERON:0001870): Cortical atrophy
- **Cerebellar cortex** (UBERON:0002129): Atrophy
- **Corpus callosum** (UBERON:0002336): Atrophy
- **Cerebellar vermis** (UBERON:0004720): Atrophy

Neuropathological findings revealed "damage of all cellular elements of brain tissue" ([PMID: 20054783](https://pubmed.ncbi.nlm.nih.gov/20054783/)).

**Cell populations affected:**
- Neurons (CL:0000540) -- neurotoxicity, degeneration
- Oligodendrocytes (CL:0000128) -- impaired myelination
- Microglia (CL:0000129) -- neuroinflammatory activation
- Astrocytes (CL:0000127) -- reactive gliosis

### Subcellular Level

- **Cytosol** (GO:0005829): Site of purinosome assembly and ADSL activity
- **Mitochondria** (GO:0005739): Secondary dysfunction, fragmentation ([PMID: 40914938](https://pubmed.ncbi.nlm.nih.gov/40914938/))
- **Nucleus** (GO:0005634): Impaired nucleotide supply for DNA/RNA synthesis
- **Purinosome complex** (GO:0032991)

### Localization

**Anatomical sites (UBERON terms):**
- Cerebral cortex (UBERON:0000956) -- atrophy
- Cerebellum (UBERON:0002037) -- hypoplasia, atrophy
- Corpus callosum (UBERON:0002336) -- atrophy
- Lateral ventricles (UBERON:0002285) -- widening
- Cisterna magna (UBERON:0003028) -- enlargement

**Lateralization**: Bilateral, symmetric involvement of brain structures.

---

## 8. Temporal Development

### Onset

- **Typical age of onset**: 89.2% of patients present within the first year of life ([PMID: 37842880](https://pubmed.ncbi.nlm.nih.gov/37842880/))
- **Fatal neonatal form**: Birth to first days
- **Type I**: First weeks to months (median 0.63 years)
- **Type II**: Months to first years; rare late-onset cases diagnosed in childhood or adolescence

First signs: psychomotor delay (8/18 patients), epilepsy (3/18), combined (3/18), or other neurological signs including apneas, hypotonia, nystagmus ([PMID: 33648541](https://pubmed.ncbi.nlm.nih.gov/33648541/))

**HPO terms**: Infantile onset (HP:0003593), Neonatal onset (HP:0003623), Childhood onset (HP:0011463)

### Diagnostic Delay

The median age at diagnosis (6.4 years) significantly lags behind the median age of onset (0.63 years), indicating substantial diagnostic delay. Seven of 18 patients in one series were diagnosed by exome sequencing, highlighting the role of genomic testing in overcoming diagnostic delays ([PMID: 33648541](https://pubmed.ncbi.nlm.nih.gov/33648541/)).

### Progression

- **Neonatal form**: Rapid, lethal within weeks
- **Type I**: Progressive neurological deterioration over years; some patients develop late-onset spasticity and thoracic deformity ([PMID: 21903433](https://pubmed.ncbi.nlm.nih.gov/21903433/))
- **Type II**: Slow progression; some patients show relative stability or even mild improvement. One patient "began to walk independently at the age of 3 years. From the age of 4 years, her communication skills improved and she presented fewer autistic features" ([PMID: 23504561](https://pubmed.ncbi.nlm.nih.gov/23504561/))

**Disease duration**: Chronic lifelong (types I and II); self-limited by death (neonatal form)

### Critical Periods

- Early therapeutic intervention (younger, less cognitively impaired patients) shows better response to allopurinol treatment ([PMID: 41053929](https://pubmed.ncbi.nlm.nih.gov/41053929/))
- D-ribose withdrawal precipitated status epilepticus and acute neurological deterioration, representing a critical vulnerability window ([PMID: 21903433](https://pubmed.ncbi.nlm.nih.gov/21903433/))

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence**: ~0.00125 per 100,000 (ultra-rare) ([PMID: 40896413](https://pubmed.ncbi.nlm.nih.gov/40896413/))
- **Total cases reported**: >80-100 individuals worldwide; 88 patients identified in systematic literature review ([PMID: 37842880](https://pubmed.ncbi.nlm.nih.gov/37842880/))
- **Incidence**: Unknown precisely; likely underdiagnosed due to nonspecific clinical presentation ([PMID: 28768552](https://pubmed.ncbi.nlm.nih.gov/28768552/))
- A Czech screening program over 13 years identified 8 patients with ADSL deficiency out of approximately 1,600 patients screened for purine/pyrimidine disorders ([PMID: 24940674](https://pubmed.ncbi.nlm.nih.gov/24940674/))

### Genetic Inheritance

- **Inheritance pattern**: Autosomal recessive (AR)
- **Penetrance**: Complete -- all individuals with biallelic pathogenic variants manifest disease
- **Expressivity**: Highly variable, determined by residual enzyme activity and protein stability
- **Genetic anticipation**: Not observed (not a repeat expansion disorder)
- **Germline mosaicism**: Not documented
- **Consanguinity**: Present in a significant proportion of reported families, consistent with AR inheritance; homozygous mutations (e.g., p.R426H, p.D430N) common in consanguineous families
- **Carrier frequency**: Unknown due to rarity; expected to be very low
- **Founder effects**: The p.R426H variant is the most common globally (19/88 patients homozygous), suggesting possible founder effect or recurrent mutation at a CpG site

### Population Demographics

- **Affected populations**: No specific ethnic predisposition established; cases reported across diverse ethnic groups including European, Middle Eastern, Asian, South American, and African populations
- **Geographic distribution**: Worldwide, with larger case series from Belgium, Poland, Czech Republic, Italy, Spain, and Brazil
- **Sex ratio**: 12 males to 6 females in one cohort ([PMID: 33648541](https://pubmed.ncbi.nlm.nih.gov/33648541/)), though this may reflect ascertainment bias; no inherent sex predisposition expected for AR disorder
- **Age distribution**: Predominantly pediatric; survival to adulthood is possible in type II

---

## 10. Diagnostics

### Clinical Tests

#### Biochemical Tests (Primary Diagnostic Approach)

**Urinary Succinylpurine Analysis** (Gold Standard):

| Metabolite | Normal | ADSLD |
|-----------|--------|-------|
| SAICAr (urine) | Undetectable | Markedly elevated |
| S-Ado (urine) | Undetectable | Markedly elevated |
| S-Ado/SAICAr ratio | N/A | <1 (neonatal), <2 (type I), >2 (type II) |

**Methods:**
- **Bratton-Marshall test**: Traditional colorimetric screening assay for SAICAr in urine ([PMID: 12368987](https://pubmed.ncbi.nlm.nih.gov/12368987/))
- **HPLC with diode-array detection (HPLC-DAD)**: More sensitive and specific
- **LC-MS/MS**: Gold standard; also detects deribosylated metabolites SAICA and SA

**CRITICAL CAVEAT**: False-negative screening can occur due to bacterial deribosylation of urinary biomarkers. "Screening methods for the diagnosis of dADSL may be falsely negative due to bacteria-mediated deribosylation of SAICA-riboside and SAdo" ([PMID: 24183879](https://pubmed.ncbi.nlm.nih.gov/24183879/)). HPLC-DAD or LC-MS/MS methods that simultaneously detect ribosylated and deribosylated forms should be used preferentially.

**Enzyme Activity Assay**: ADSL enzyme activity can be measured in red blood cells, lymphocytes, or cultured fibroblasts. Reduced activity confirms the diagnosis.

**Biomarkers:**
- SAICAr -- primary diagnostic biomarker
- S-Ado -- primary diagnostic biomarker
- S-Ado/SAICAr ratio -- prognostic biomarker (value debated, [PMID: 20127976](https://pubmed.ncbi.nlm.nih.gov/20127976/))
- SAICA and SA (deribosylated forms) -- may be detected in urines with bacterial contamination

#### Imaging Studies

**Brain MRI** ([PMID: 21625931](https://pubmed.ncbi.nlm.nih.gov/21625931/); [PMID: 20054783](https://pubmed.ncbi.nlm.nih.gov/20054783/)):
- Delayed or absent myelination
- White matter signal abnormalities (T2 hyperintensity)
- Cerebral and cerebellar atrophy
- Corpus callosum atrophy
- Enlarged ventricles and subarachnoid spaces
- Note: MRI may be normal in mild cases ([PMID: 28768552](https://pubmed.ncbi.nlm.nih.gov/28768552/))

#### Electrophysiology

**EEG** ([PMID: 37842880](https://pubmed.ncbi.nlm.nih.gov/37842880/)):
- Poor background organization with theta-delta slowing
- Hypsarrhythmia (in infantile spasms)
- Multifocal epileptiform discharges

### Genetic Testing

**Recommended approach:**
1. **First-line**: Biochemical screening (urinary succinylpurines by HPLC-DAD or LC-MS/MS)
2. **Confirmatory**: *ADSL* gene sequencing
3. **Alternative route**: Whole exome sequencing (WES) -- increasingly used; diagnosed 7/18 patients in one cohort ([PMID: 33648541](https://pubmed.ncbi.nlm.nih.gov/33648541/))

- **WES utility**: High -- effective for diagnosis, especially in patients with nonspecific neurological presentations ([PMID: 28768552](https://pubmed.ncbi.nlm.nih.gov/28768552/))
- **Gene panels**: Included in metabolic disease, epilepsy, and intellectual disability gene panels
- **Single gene testing**: *ADSL* sequencing with deletion/duplication analysis
- **CMA/Karyotyping/FISH**: Not typically informative (point mutations, not structural variants)

### Clinical Criteria

**Diagnostic criteria:**
1. Clinical presentation with neurological features (developmental delay, seizures, autistic features)
2. Biochemical confirmation: elevated SAICAr and S-Ado in urine, plasma, or CSF
3. Genetic confirmation: biallelic pathogenic variants in *ADSL*
4. Optional: reduced ADSL enzyme activity in erythrocytes or fibroblasts

### Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Angelman syndrome | Similar behavioral phenotype but lacks succinylpurinuria; UBE3A gene |
| Other purine metabolism disorders (HPRT, PNP deficiency) | Different metabolite profiles |
| AICA-ribosiduria (ATIC deficiency) | Elevated AICA riboside; distinct metabolite pattern |
| PAICS deficiency | Different DNPS substrates |
| ADSS deficiency | Different metabolite profile |
| Mitochondrial disorders (primary) | Lactate elevation; different genetic basis |
| Non-specific epileptic encephalopathies | Require metabolic screening to differentiate |
| Leukodystrophies | Based on MRI findings; different metabolic signatures |
| Idiopathic autism spectrum disorder | Metabolic screening distinguishes |

### Screening

- **Newborn screening**: Not currently included in standard newborn screening panels in most countries
- **Selective screening**: Recommended for patients with unexplained neonatal seizures, epileptic encephalopathy, developmental delay, or autistic features. "A search for this disorder should be included in the screening program of children with unexplained neonatal seizures or severe infantile epileptic encephalopathy" ([PMID: 11392513](https://pubmed.ncbi.nlm.nih.gov/11392513/))
- **Cascade screening**: Recommended for siblings of affected individuals
- **Prenatal diagnosis**: Possible through molecular analysis of *ADSL* variants in chorionic villus samples or amniocytes

---

## 11. Outcome/Prognosis

### Survival and Mortality

- **Fatal neonatal form**: Death within days to weeks of life; universally lethal. Primary cause of death is respiratory failure and intractable seizures.
- **Type I (severe)**: Significantly reduced life expectancy; many patients survive into childhood or adolescence but with severe disability. Status epilepticus and complications of severe neurological disability contribute to mortality.
- **Type II (mild/moderate)**: Life expectancy may approach normal; patients survive into adulthood.
- **Overall mortality**: No formal survival statistics available due to rarity.

### Morbidity and Function

- **Type I**: Severe intellectual disability, dependent on caregivers for all activities of daily living, drug-resistant epilepsy, progressive spasticity
- **Type II**: Mild to moderate intellectual disability; some patients attend special education, develop limited communication skills. One patient "began to make statements that form a logical continuity and make progress in simple manual operations" ([PMID: 23504561](https://pubmed.ncbi.nlm.nih.gov/23504561/))

### Complications

- Drug-resistant epilepsy and status epilepticus
- Progressive spasticity and contractures
- Thoracic deformity ([PMID: 21903433](https://pubmed.ncbi.nlm.nih.gov/21903433/))
- Aspiration pneumonia (in severely affected patients)
- Nutritional challenges and growth failure
- Acute neurological deterioration (particularly associated with D-ribose withdrawal)

### Prognostic Factors

| Factor | Better Prognosis | Worse Prognosis |
|--------|-----------------|-----------------|
| S-Ado/SAICAr ratio | Higher (>2) | Lower (<1) |
| Residual enzyme activity | Higher | Lower |
| ADSL tetramer stability | More stable | Less stable |
| Age at onset | Later | Earlier (neonatal) |
| Seizure response | Treatment responsive | Drug-resistant |
| Age at treatment initiation | Younger | Older/more impaired |

---

## 12. Treatment

### Current Standard of Care

**No curative treatment exists.** Management is primarily supportive. "Currently, no effective treatment is available for adenylosuccinate lyase deficiency" ([PMID: 11392513](https://pubmed.ncbi.nlm.nih.gov/11392513/)).

### Pharmacotherapy

#### Allopurinol (Zyloric) -- MAXO:0001298

The most promising pharmacological intervention to date. A Phase II prospective trial reported: "Results showed clinical improvements in younger, less cognitively impaired patients, indicated by better Vineland Adaptive Behavior Scale (VABS II) scores and reduced hyperactivity on the Aberrant Behavior Checklist (ABC) and Conners Rating Scale-Revised (CRSR). These improvements correlated with significant decreases in urinary SAICAr levels and an increased S-Ado/SAICAr ratio" ([PMID: 41053929](https://pubmed.ncbi.nlm.nih.gov/41053929/)).

- **Dose**: 10-20 mg/kg/day (max 400 mg/day children, 900 mg/day adults)
- **Participants**: 8 patients (4 children, 4 young adults)
- **Responders**: Younger, less cognitively impaired patients
- **Non-responders**: Older or more severely affected patients
- **Mechanism**: Xanthine oxidase inhibitor; potentially redirects purine salvage and reduces toxic metabolite accumulation
- **Critical finding**: Suggests a therapeutic window where early intervention is key

#### Anti-epileptic Drugs (AEDs) -- MAXO:0000756

- Multiple AEDs used for seizure control; no specific AED is preferentially effective
- Many patients have drug-resistant epilepsy requiring polytherapy
- Various AEDs documented across case series without clear superiority

#### Ketogenic Diet -- MAXO:0001193

One case report documented a positive effect on seizure control in a type II patient ([PMID: 23504561](https://pubmed.ncbi.nlm.nih.gov/23504561/)).

#### D-Ribose (CAUTION)

D-ribose supplementation was trialed but showed no clinical benefit. "D-ribose must be considered with caution as, in our experience, it returns no clinical benefit and drug withdrawal can precipitate status epilepticus and acute neurological deterioration" ([PMID: 21903433](https://pubmed.ncbi.nlm.nih.gov/21903433/)).

### Advanced Therapeutics

#### Gene Therapy

No gene therapy trials are currently registered for ADSLD. However, the monogenic nature of the disease and the relatively small gene size make it a potential candidate for AAV-mediated gene replacement therapy. Identified as an "urgent need" ([PMID: 40896413](https://pubmed.ncbi.nlm.nih.gov/40896413/)).

#### Targeting Mitochondrial Dysfunction

The identification of ADSLD as a secondary mitochondrial disease opens avenues for:
- Overexpression of constitutively active ERK2 partially rescues the mitochondrial phenotype ([PMID: 40914938](https://pubmed.ncbi.nlm.nih.gov/40914938/))
- Purine intermediate supplementation partially rescues mitochondrial function
- Mitochondrial-targeted therapies (e.g., CoQ10, idebenone)
- ERK2/AKT pathway modulators

#### Complement Pathway Inhibition

The emerging role of complement-mediated neuroinflammation suggests potential for complement inhibitors (e.g., eculizumab, avacopan) as neuroprotective agents ([PMID: 40896413](https://pubmed.ncbi.nlm.nih.gov/40896413/)).

### Supportive and Rehabilitative Care

- **Physical therapy / physiotherapy** (MAXO:0000011)
- **Occupational therapy** (MAXO:0000536)
- **Speech therapy** (MAXO:0000930)
- **Hydrotherapy**, **Hippotherapy**, **Pet therapy**, **Music therapy** ([PMID: 23504561](https://pubmed.ncbi.nlm.nih.gov/23504561/))
- **Nutritional support** for feeding difficulties
- **Special education services**

### Treatment Strategy

Current management algorithm:
1. Seizure control (AEDs, ketogenic diet if refractory)
2. Developmental support (multidisciplinary rehabilitation)
3. Nutritional management
4. Consider allopurinol trial, especially in younger patients with milder phenotype
5. Monitor succinylpurine levels in urine/plasma to assess treatment response
6. Avoid D-ribose

---

## 13. Prevention

### Primary Prevention

- **Genetic counseling** (MAXO:0000079): Recommended for families with affected individuals; 25% recurrence risk for carrier parents
- **Preimplantation genetic diagnosis (PGD)**: Available for families with known pathogenic variants
- **Prenatal diagnosis**: Molecular analysis of *ADSL* variants in chorionic villi or amniotic fluid cells
- **Carrier testing**: Available for at-risk family members

### Secondary Prevention (Early Detection)

- **Selective metabolic screening**: Recommended for patients with unexplained neonatal seizures, epileptic encephalopathy, developmental delay, or autistic features. "ADSL deficiency should be part of the screening to be performed in case of neonatal seizures" ([PMID: 18201882](https://pubmed.ncbi.nlm.nih.gov/18201882/))
- **Bratton-Marshall test**: Colorimetric urine screening test for SAICAr ([PMID: 12368987](https://pubmed.ncbi.nlm.nih.gov/12368987/))
- **WES/WGS**: Increasingly used for undiagnosed neurological disorders, enabling earlier diagnosis
- **Cascade screening**: Siblings of affected patients should be tested
- **Caution**: Fresh urine samples required to avoid false negatives from bacterial deribosylation ([PMID: 24183879](https://pubmed.ncbi.nlm.nih.gov/24183879/))

### Tertiary Prevention

- Seizure management to prevent secondary brain injury
- Nutritional support to prevent malnutrition
- Physical therapy to prevent contractures
- Allopurinol therapy (particularly in younger patients) to potentially slow disease progression
- Avoidance of D-ribose based on adverse outcomes ([PMID: 21903433](https://pubmed.ncbi.nlm.nih.gov/21903433/))

### Immunization

Not applicable. ADSLD is not an infectious or immune-mediated disease.

---

## 14. Other Species / Natural Disease

### Orthologous Genes

The *ADSL* gene is highly conserved across species, reflecting the fundamental importance of purine metabolism:

| Species | Gene | NCBI Gene ID | NCBI Taxon |
|---------|------|-------------|-----------|
| *Homo sapiens* | *ADSL* | 158 | 9606 |
| *Mus musculus* | *Adsl* | 11564 | 10090 |
| *Rattus norvegicus* | *Adsl* | 25283 | 10116 |
| *Danio rerio* | *adsl* | 559111 | 7955 |
| *Drosophila melanogaster* | *raspberry/AdSL* | 38295 | 7227 |
| *Saccharomyces cerevisiae* | *ADE13* | 850687 | 4932 |

### Natural Disease in Other Species

No naturally occurring ADSL deficiency has been reported in domestic or wild animal species. This may reflect:
- Embryonic lethality of complete loss-of-function in other species
- Lack of diagnostic awareness in veterinary medicine
- True absence of naturally occurring disease-causing variants

### Comparative Biology

The ADSL enzyme and purine de novo synthesis pathway are evolutionarily conserved from yeast to humans. The *S. cerevisiae* homolog *ADE13* has been used extensively to study ADSL biochemistry. The *Drosophila* ortholog *raspberry* (*ras*) has been used as a model to study purine metabolism.

The conservation of disease mechanisms across species supports the use of model organisms for understanding ADSLD pathophysiology. Conservation of both catalytic reactions suggests fundamental importance in purine metabolism.

### Transmission

Not applicable. ADSLD is a genetic disorder, not an infectious disease. No zoonotic potential or cross-species susceptibility considerations.

---

## 15. Model Organisms

### Available Models

| Model | Type | Key Features | Reference |
|-------|------|-------------|-----------|
| Patient fibroblasts | In vitro (human) | Purinosome assembly studies, enzyme activity assays | [PMID: 22180458](https://pubmed.ncbi.nlm.nih.gov/22180458/) |
| CRISPR-edited HeLa cells | In vitro (human) | Substrate accumulation, purinosome disruption | [PMID: 27590927](https://pubmed.ncbi.nlm.nih.gov/27590927/) |
| CRISPR *ADSL*-KO liver cancer cells | In vitro (human) | Mitochondrial dysfunction, cell cycle arrest | [PMID: 33336367](https://pubmed.ncbi.nlm.nih.gov/33336367/) |
| Patient-derived cells (mitochondrial studies) | In vitro (human) | Mitochondrial phenotype, signaling studies | [PMID: 40914938](https://pubmed.ncbi.nlm.nih.gov/40914938/) |
| *S. cerevisiae* (*ade13* mutants) | Yeast | Purine pathway studies, functional characterization | Literature |

### Key Model Findings

1. **Patient fibroblasts**: Demonstrated that "various mutations of ATIC and ADSL destabilize to various degrees of purinosome assembly" and "the ability to form purinosomes correlates with clinical phenotypes of individual ADSL patients" ([PMID: 22180458](https://pubmed.ncbi.nlm.nih.gov/22180458/))

2. **CRISPR HeLa models**: "In all model cell lines with the exception of one, an accumulation of the substrate(s) for the knocked out enzyme was identified. The ability to form the purinosome was reduced" ([PMID: 27590927](https://pubmed.ncbi.nlm.nih.gov/27590927/)). These models also enabled development of diagnostic LC-MS/MS methods.

3. **Liver cancer cells (ADSL-KO)**: "CRISPR-mediated knockout of ADSL impaired colony formation of liver cancer cells by affecting AMP production... ADSL knockout caused S-phase cell cycle arrest not by inducing DNA damage but by impairing mitochondrial function" ([PMID: 33336367](https://pubmed.ncbi.nlm.nih.gov/33336367/)). In vivo xenograft models showed retarded tumor growth.

4. **Mitochondrial studies**: Patient-derived cells demonstrated increased mitochondrial fragmentation, impaired respiration, and reduced ATP production, with defects linked to ERK2/AKT suppression ([PMID: 40914938](https://pubmed.ncbi.nlm.nih.gov/40914938/)).

### Model Limitations

- No established animal models (mouse knockout, zebrafish morphant) are widely used for ADSLD research
- Complete ADSL knockout is likely embryonically lethal, necessitating conditional or hypomorphic approaches
- Cell-based models cannot fully recapitulate the neurological phenotype
- Cancer cell lines (HeLa, HCC) may not reflect neuronal pathophysiology
- The blood-brain barrier and CNS-specific effects are difficult to study in vitro
- No validated animal model fully recapitulates the human neurological phenotype

### Proposed Models

Knock-in mice carrying human pathogenic mutations (e.g., equivalent of p.R426H) have been proposed but not yet widely reported. Development of conditional knock-in mouse models and iPSC-derived cerebral organoids are critical research priorities.

---

## Key Findings

### Finding 1: ADSLD is an Ultra-Rare Autosomal Recessive Purine Metabolism Disorder

ADSLD has a global prevalence of approximately 0.00125 per 100,000, with more than 80 patients identified worldwide. The *ADSL* gene on chromosome 22q13.1 consists of 13 exons spanning 23 kb. Three clinical phenotypes are recognized: fatal neonatal, type I (severe), and type II (moderate/mild). Disease onset occurs within the first year of life in 89.2% of cases, and epilepsy is present in 81.8% of patients. This was established through systematic literature review covering 88 patients ([PMID: 40896413](https://pubmed.ncbi.nlm.nih.gov/40896413/); [PMID: 37842880](https://pubmed.ncbi.nlm.nih.gov/37842880/); [PMID: 25112391](https://pubmed.ncbi.nlm.nih.gov/25112391/)).

### Finding 2: ADSLD is a Secondary Mitochondrial Disease with ERK2/AKT Signaling Involvement

Recent research (2025) established that ADSLD causes secondary mitochondrial dysfunction, including increased mitochondrial fragmentation, impaired respiration, and reduced ATP production. "The severity of mitochondrial impairment correlates with ADSLd pathology, especially in mitochondria-dependent tissues" ([PMID: 40914938](https://pubmed.ncbi.nlm.nih.gov/40914938/)). This dysfunction is mediated through suppression of ERK2 and AKT signaling pathways, and can be partially rescued by overexpressing constitutively active ERK2 or supplementing purine intermediates. This finding reframes ADSLD not just as a purine metabolism disorder but as a mitochondrial disease, with implications for therapy.

### Finding 3: Complement Pathway Activation Drives Neuroinflammation

Activation of the alternative complement pathway has been identified as "a key driver of inflammation, blood-brain barrier disruption, and progressive neurodegeneration" ([PMID: 40896413](https://pubmed.ncbi.nlm.nih.gov/40896413/)). SAICAr, the more neurotoxic succinylpurine, promotes neuroinflammation, and lower S-Ado/SAICAr ratios correlate with more severe clinical outcomes. This emerging hypothesis provides a mechanistic link between metabolite accumulation and the progressive neurodegeneration seen in ADSLD.

### Finding 4: Allopurinol Shows Clinical Benefit in Young ADSLD Patients

A Phase II prospective trial of allopurinol (10-20 mg/kg/day) in 8 patients (4 children, 4 young adults) demonstrated clinical improvements in younger, less cognitively impaired patients. "These improvements correlated with significant decreases in urinary SAICAr levels and an increased S-Ado/SAICAr ratio" ([PMID: 41053929](https://pubmed.ncbi.nlm.nih.gov/41053929/)). No changes were observed in older or more severely affected patients, suggesting a critical therapeutic window for intervention.

### Finding 5: Purinosome Assembly Disruption Correlates with Clinical Severity

ADSL mutations destabilize purinosome assembly in patient fibroblasts, and the degree of purinosome disruption correlates with clinical phenotype severity ([PMID: 22180458](https://pubmed.ncbi.nlm.nih.gov/22180458/)). Furthermore, "phenotypic severity in ADSL deficiency is correlated with residual enzymatic activity and structural stability of the corresponding mutant ADSL complexes" ([PMID: 20127976](https://pubmed.ncbi.nlm.nih.gov/20127976/)). This establishes a robust genotype-phenotype correlation framework: variant → protein stability → enzyme activity → purinosome integrity → clinical phenotype.

---

## Mechanistic Model

The pathophysiology of ADSLD can be understood as a cascade of interconnected molecular events operating through multiple parallel and converging pathways:

```
                    ADSL Gene Mutations (biallelic)
                              |
                    Reduced Enzyme Activity
                    & Protein Instability
                              |
               +--------------+---------------+
               |                              |
     TOXIC ACCUMULATION              PURINE DEPLETION
     (SAICAr, S-Ado)                (↓AMP, ↓ATP, ↓GTP)
               |                              |
     +---------+---------+          +---------+---------+
     |                   |          |                   |
  SAICAr            S-Ado      Mitochondrial      ↓DNA/RNA
  neurotoxicity     (less     dysfunction         synthesis
     |              toxic)        |
     |                        Fragmentation
  Complement                  ↓Respiration
  activation                  ↓ATP
  (alternative)                   |
     |                        ERK2/AKT
  BBB disruption              suppression
     |                            |
  Neuroinflammation          Cell growth/
     |                       survival impairment
     |                            |
     +------------+---------------+
                  |
         PROGRESSIVE NEURODEGENERATION
         • White matter loss / dysmyelination
         • Cortical & cerebellar atrophy
         • Seizures / epilepsy
         • Developmental delay / intellectual disability
         • Autistic features
```

This model highlights three key therapeutic intervention points:
1. **Upstream**: Reduce SAICAr accumulation (allopurinol)
2. **Midstream**: Rescue mitochondrial function (ERK2 activation, purine supplementation)
3. **Downstream**: Block complement-mediated neuroinflammation (complement inhibitors)

---

## Evidence Base

| PMID | Year | Key Contribution |
|------|------|-----------------|
| [40896413](https://pubmed.ncbi.nlm.nih.gov/40896413/) | 2025 | Prevalence data; complement pathway neuroinflammation hypothesis |
| [40914938](https://pubmed.ncbi.nlm.nih.gov/40914938/) | 2025 | ADSLD as secondary mitochondrial disease; ERK2/AKT involvement |
| [41053929](https://pubmed.ncbi.nlm.nih.gov/41053929/) | 2025 | Allopurinol Phase II trial results |
| [37842880](https://pubmed.ncbi.nlm.nih.gov/37842880/) | 2023 | Electroclinical features; 89.2% onset <1 year, 81.8% epilepsy |
| [34998670](https://pubmed.ncbi.nlm.nih.gov/34998670/) | 2022 | Comprehensive review of purine biosynthesis disorders |
| [33648541](https://pubmed.ncbi.nlm.nih.gov/33648541/) | 2021 | Clinical/molecular characterization of 18 patients; variant spectrum |
| [33336367](https://pubmed.ncbi.nlm.nih.gov/33336367/) | 2020 | ADSL in liver cancer; mitochondrial function link |
| [28768552](https://pubmed.ncbi.nlm.nih.gov/28768552/) | 2017 | Mild ADSL deficiency diagnosed by WES |
| [27590927](https://pubmed.ncbi.nlm.nih.gov/27590927/) | 2016 | CRISPR models of DNPS defects |
| [25112391](https://pubmed.ncbi.nlm.nih.gov/25112391/) | 2015 | Comprehensive ADSL deficiency review |
| [24940674](https://pubmed.ncbi.nlm.nih.gov/24940674/) | 2014 | Czech screening program results |
| [24183879](https://pubmed.ncbi.nlm.nih.gov/24183879/) | 2014 | False negative screening warning |
| [23504561](https://pubmed.ncbi.nlm.nih.gov/23504561/) | 2013 | Attenuated ADSL deficiency; ketogenic diet benefit |
| [22180458](https://pubmed.ncbi.nlm.nih.gov/22180458/) | 2012 | Purinosome assembly disruption in patient fibroblasts |
| [21903433](https://pubmed.ncbi.nlm.nih.gov/21903433/) | 2011 | Novel features; D-ribose caution |
| [21625931](https://pubmed.ncbi.nlm.nih.gov/21625931/) | 2011 | Brain MRI findings in 7 patients |
| [21401501](https://pubmed.ncbi.nlm.nih.gov/21401501/) | 2011 | Neurological disorders of purine metabolism |
| [20127976](https://pubmed.ncbi.nlm.nih.gov/20127976/) | 2010 | Structural analysis of 14 mutant ADSL complexes; genotype-phenotype |
| [20054783](https://pubmed.ncbi.nlm.nih.gov/20054783/) | 2009 | Severe encephalopathy; neuropathology |
| [18830228](https://pubmed.ncbi.nlm.nih.gov/18830228/) | 2008 | Angelman-like behavioral phenotype |
| [18201882](https://pubmed.ncbi.nlm.nih.gov/18201882/) | 2008 | Neonatal seizures as presenting feature |
| [15796126](https://pubmed.ncbi.nlm.nih.gov/15796126/) | 2005 | Genetic disorders associated with autism |
| [15571240](https://pubmed.ncbi.nlm.nih.gov/15571240/) | 2004 | Biochemical/molecular correlation; oxidative sensitivity |
| [15571235](https://pubmed.ncbi.nlm.nih.gov/15571235/) | 2004 | First British case; novel mutations |
| [12368987](https://pubmed.ncbi.nlm.nih.gov/12368987/) | 2002 | Screening methods and diagnosis |
| [11392513](https://pubmed.ncbi.nlm.nih.gov/11392513/) | 2001 | Neurologic aspects review |
| [11098885](https://pubmed.ncbi.nlm.nih.gov/11098885/) | 2000 | Metabolic approaches to ASD treatment |
| [10888601](https://pubmed.ncbi.nlm.nih.gov/10888601/) | 2000 | ADSL gene structure; cDNA; molecular basis |

---

## Limitations and Knowledge Gaps

1. **Ultra-rare disease limitations**: With fewer than 100 identified patients worldwide, all clinical data come from small case series and single case reports, limiting statistical power and generalizability.

2. **Lack of animal models**: No well-characterized animal model of ADSLD exists, hindering preclinical therapeutic development and detailed mechanistic studies of CNS pathology.

3. **Incomplete genotype-phenotype correlation**: While residual enzyme activity and tetramer stability explain much of the phenotypic variation, the discordance between in vitro activity against both substrates and the differential accumulation of SAICAr vs. S-Ado in CSF remains unexplained. As noted: "All the mutant enzymes studied in vitro displayed a proportional decrease in activity against both of their substrates. However, this was not concordant with strikingly different concentration ratios in the CSF of individual patients" ([PMID: 10888601](https://pubmed.ncbi.nlm.nih.gov/10888601/)).

4. **Complement pathway hypothesis**: The role of complement activation in neuroinflammation is still an emerging hypothesis that requires validation in patient samples and model systems.

5. **Treatment evidence**: The allopurinol trial included only 8 patients without a placebo control; larger, randomized trials are needed to confirm efficacy.

6. **No newborn screening**: ADSLD is not included in standard newborn screening panels, contributing to diagnostic delays averaging ~6 years.

7. **Long-term natural history**: Limited longitudinal data on disease progression, especially for mild type II patients who may survive into adulthood.

8. **Epigenetic and modifier gene effects**: No studies have examined epigenetic modifications or genetic modifiers that might influence disease severity.

9. **Neurotoxicity mechanisms**: The exact molecular mechanisms by which SAICAr exerts neurotoxicity and activates complement remain to be elucidated.

10. **Quality of life data**: No formal quality-of-life assessments using validated instruments have been published.

---

## Proposed Follow-up Experiments and Actions

### Near-Term (1-3 years)

1. **Develop conditional knock-in mouse model** carrying common human ADSL mutations (e.g., p.R426H) with CNS-specific expression to study neuropathology and test therapeutic interventions in vivo.

2. **Validate the complement pathway hypothesis** using patient CSF samples and post-mortem brain tissue to measure complement activation markers (C3a, C5a, MAC) and correlate with disease severity.

3. **Conduct a larger, multi-center, randomized controlled trial of allopurinol** in ADSLD patients, stratifying by age, severity, and genotype to identify optimal treatment windows and confirm Phase II findings.

4. **Perform multi-omics profiling** (transcriptomics, proteomics, metabolomics) on patient-derived iPSC-differentiated neurons to comprehensively characterize molecular disruptions specific to the neuronal context.

5. **Develop iPSC-derived cerebral organoid models** to study ADSLD-associated neurodevelopmental defects and test candidate therapies in a 3D human brain model.

### Medium-Term (3-5 years)

6. **Evaluate complement inhibitors** (e.g., anti-C5 antibodies, factor B inhibitors) in ADSLD cell and animal models as potential neuroprotective therapies.

7. **Test mitochondrial-targeted therapies** (CoQ10, idebenone, NAD+ precursors, ERK2/AKT pathway activators) in ADSLD models and patients.

8. **Investigate AAV-mediated gene therapy** for ADSLD, determining optimal serotype, promoter, and route of administration for CNS delivery.

9. **Advocate for inclusion of ADSLD in newborn screening panels** using tandem mass spectrometry-based detection of SAICAr and S-Ado, potentially reducing the current 6-year diagnostic delay.

### Long-Term (5+ years)

10. **Establish an international ADSLD patient registry** with standardized clinical assessments, longitudinal follow-up, and biobanking to enable natural history studies and clinical trials.

11. **Develop biomarker-guided personalized treatment protocols** based on S-Ado/SAICAr ratios, residual enzyme activity, and genotype.

12. **Explore gene editing approaches** (base editing, prime editing) to correct specific ADSL point mutations in patient cells, potentially offering mutation-specific therapeutic strategies.

---

## Ontology Term Summary

| Category | Terms |
|----------|-------|
| **MONDO** | MONDO:0010041 (Adenylosuccinate lyase deficiency) |
| **HPO** | HP:0001250 (Seizures), HP:0001263 (Global developmental delay), HP:0001249 (Intellectual disability), HP:0001252 (Muscular hypotonia), HP:0000252 (Microcephaly), HP:0000729 (Autistic behavior), HP:0002500 (Abnormality of cerebral white matter), HP:0002188 (Delayed myelination), HP:0001272 (Cerebellar atrophy), HP:0012736 (Neonatal encephalopathy), HP:0001258 (Spasticity), HP:0000639 (Nystagmus), HP:0001510 (Growth delay), HP:0002878 (Respiratory failure) |
| **GO (Biological Process)** | GO:0006164 (Purine nucleotide biosynthetic process), GO:0006189 ('de novo' IMP biosynthetic process), GO:0006167 (AMP biosynthetic process), GO:0007005 (Mitochondrial organization), GO:0006119 (Oxidative phosphorylation), GO:0006956 (Complement activation), GO:0006954 (Inflammatory response), GO:0009060 (Aerobic respiration) |
| **GO (Molecular Function)** | GO:0004018 (Adenylosuccinate lyase activity), GO:0070626 (SAICAR lyase activity), GO:0042802 (Identical protein binding) |
| **GO (Cellular Component)** | GO:0005829 (Cytosol), GO:0005739 (Mitochondrion), GO:0005634 (Nucleus), GO:0032991 (Protein-containing complex/purinosome) |
| **CL (Cell Types)** | CL:0000540 (Neuron), CL:0000128 (Oligodendrocyte), CL:0000127 (Astrocyte), CL:0000129 (Microglial cell) |
| **UBERON (Anatomy)** | UBERON:0000955 (Brain), UBERON:0002037 (Cerebellum), UBERON:0002316 (White matter), UBERON:0002336 (Corpus callosum), UBERON:0000956 (Cerebral cortex), UBERON:0002285 (Lateral ventricle), UBERON:0003028 (Cisterna magna) |
| **CHEBI (Chemicals)** | CHEBI:141525 (SAICAr), CHEBI:99039 (Succinyladenosine), CHEBI:16027 (AMP), CHEBI:15422 (ATP) |
| **MAXO (Treatments)** | MAXO:0000756 (Anticonvulsant therapy), MAXO:0000079 (Genetic counseling), MAXO:0000011 (Physical therapy), MAXO:0000536 (Occupational therapy), MAXO:0000930 (Speech therapy), MAXO:0001298 (Allopurinol administration), MAXO:0001193 (Ketogenic diet therapy) |

---

*Report generated: 2026-05-05*
*Based on systematic review of 31 published papers and disease database entries*
*Comprehensive disease characterization covering 15 knowledge domains*
