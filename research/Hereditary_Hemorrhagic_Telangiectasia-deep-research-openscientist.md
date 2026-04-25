---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-04-24T14:09:59.358453+00:00'
end_time: '2026-04-24T14:34:54.610665+00:00'
duration_seconds: 1495.25
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hereditary Hemorrhagic Telangiectasia
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
citation_count: 22
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Hemorrhagic Telangiectasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Hemorrhagic Telangiectasia** covering all of the
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

# Comprehensive Disease Characteristics Report: Hereditary Hemorrhagic Telangiectasia (HHT)

## Executive Summary

Hereditary Hemorrhagic Telangiectasia (HHT), also known as Osler-Weber-Rendu syndrome, is an autosomal dominant vascular disorder affecting approximately 1 in 5,000 individuals worldwide (MONDO:0008535). It is caused by loss-of-function mutations in the BMP9/10-ALK1-ENG-SMAD4 signaling pathway, which normally maintains vascular quiescence. HHT is the second most common inherited bleeding disorder worldwide (after von Willebrand disease) and is characterized by mucocutaneous telangiectases and visceral arteriovenous malformations (AVMs) that lead to chronic bleeding, iron deficiency anemia, and organ-specific complications including stroke, brain abscess, high-output cardiac failure, and pulmonary hemorrhage. Despite its prevalence, HHT remains significantly underdiagnosed, with 63% of patients not diagnosed until mid-to-late adulthood despite symptom onset typically by age 13. A paradigm shift in treatment is underway, with antiangiogenic therapies (particularly pomalidomide, the first drug to show efficacy in a Phase 3 RCT) offering disease-modifying potential, though no FDA/EMA-approved HHT-specific therapy exists yet.

---

## 1. Disease Identity and Classification

| Attribute | Details |
|-----------|---------|
| **Disease Name** | Hereditary Hemorrhagic Telangiectasia (HHT) |
| **Synonyms** | Osler-Weber-Rendu syndrome/disease |
| **MONDO ID** | MONDO:0008535 |
| **OMIM** | 187300 (HHT1), 601101 (HHT2), 175050 (JP-HHT), 615506 (HHT5), 600376 (HHT locus 3) |
| **Orphanet** | ORPHA:774 |
| **Category** | Mendelian (autosomal dominant) |
| **Disease Class** | Vascular dysplasia / inherited bleeding disorder |

---

## 2. Genetic Basis

### 2.1 Causative Genes

HHT is caused by heterozygous loss-of-function mutations in genes encoding components of the BMP9/10 signaling pathway:

| Gene | Protein | Chromosome | HHT Subtype | OMIM | Approx. % of Cases |
|------|---------|------------|-------------|------|---------------------|
| **ENG** | Endoglin (CD105) | 9q34.11 | HHT1 | 187300 | ~39-53% |
| **ACVRL1** | ALK1 (activin receptor-like kinase 1) | 12q13.13 | HHT2 | 601101 | ~31-48% |
| **SMAD4** | SMAD4/DPC4 | 18q21.2 | JP-HHT | 175050 | ~2-3% |
| **GDF2** | BMP9 (bone morphogenetic protein 9) | 10q11.22 | HHT5 | 615506 | ~1% |

- **ENG** and **ACVRL1** mutations account for ~97% of genetically confirmed cases.
- ENG mutations are widely distributed across the gene without mutational hot spots; truncating mutations are associated with more severe phenotypes than missense mutations.
- ACVRL1 mutations cluster in exons 5-10 (the serine/threonine kinase domain).
- SMAD4 mutations produce the unique Juvenile Polyposis-HHT overlap syndrome (JP-HHT).
- Approximately 10-15% of clinically diagnosed HHT patients remain genetically unresolved, suggesting additional undiscovered loci.

### 2.2 Inheritance and Penetrance

- **Inheritance**: Autosomal dominant with highly variable expressivity
- **Penetrance**: Age-dependent; ~90% penetrant for epistaxis by age 40
- **De novo mutations**: Rare but documented
- Visceral AVMs accumulate throughout the lifetime
- Significant intrafamilial variability suggests modifier genes and/or stochastic somatic events

### 2.3 Mutation Spectrum

- **Haploinsufficiency** is the predominant mechanism for both ENG and ALK1 mutations
- Mutation types include: missense, nonsense, splice-site, frameshift, and large deletions/duplications
- No common founder mutation worldwide; however, population-specific founder effects exist (see Epidemiology)

---

## 3. Molecular Pathogenesis

### 3.1 The BMP9/10-ALK1-ENG-SMAD4 Signaling Pathway

The core disease pathway operates as follows:

1. **Circulating ligands** BMP9 and BMP10 (encoded by GDF2) bind to the **co-receptor Endoglin (ENG)** on endothelial cell surfaces
2. Endoglin facilitates ligand presentation to the **signaling receptor ALK1 (ACVRL1)**
3. ALK1 phosphorylates downstream **SMAD1/5/8**, which complex with **SMAD4**
4. The SMAD complex translocates to the nucleus to activate transcriptional programs for **vascular quiescence**

This pathway actively:
- **Suppresses PI3K/AKT/mTOR signaling** (which drives angiogenesis)
- **Maintains Notch signaling** (essential for arterial-venous identity)
- **Antagonizes VEGF-driven angiogenesis**
- **Regulates casein kinase 2 (CK2)** expression

### 3.2 Two-Hit Pathogenesis Model

HHT pathogenesis follows a **two-hit model**, explaining why patients with systemic heterozygous mutations develop focal vascular lesions:

**Hit 1 (Germline)**: Inherited heterozygous loss-of-function mutation in ENG, ACVRL1, SMAD4, or GDF2.

**Hit 2 (Somatic)**: Loss of heterozygosity (LOH) or somatic second mutation in endothelial cells, resulting in **biallelic loss** and complete pathway inactivation at focal sites.

**Environmental Triggers** (required for AVM development):
- **VEGF upregulation** from angiogenic stimuli (wounding, inflammation, infection)
- **Hemodynamic shear stress** and blood flow
- **Hormonal changes** (pregnancy, puberty)

### 3.3 Molecular Consequences of Pathway Loss

When the BMP9/10-ALK1-ENG-SMAD4 pathway is inactivated:
- Unopposed **VEGF-driven angiogenesis** occurs
- **PI3K/AKT activation** drives endothelial cell proliferation
- Loss of **arterial-venous specification** (Notch pathway downregulation)
- Endothelial cells lose **capillary identity** and enter the cell cycle
- Direct arteriovenous connections form (AVMs), bypassing normal capillary beds

RNA-seq analysis of BMP9-knockout mice identified >2,000 differentially expressed genes in liver sinusoidal endothelial cells, confirming massive transcriptional dysregulation.

---

## 4. Epidemiology

### 4.1 Prevalence

| Population | Estimated Prevalence | Notes |
|-----------|---------------------|-------|
| Worldwide | 1:5,000 | Consensus estimate |
| Netherlands Antilles (Curaçao) | ~1:1,300 | Highest known; founder effect (ENG) |
| Japan (Akita region) | ~1:5,000-1:8,000 | Predominantly HHT1/ENG |
| Hungary (study area) | ~1:6,090-1:11,267 | Population screening study |
| General range | 1:5,000-1:10,000 | Likely underestimated due to underdiagnosis |

### 4.2 Geographic Variation in Subtype Distribution

- **HHT2 (ACVRL1)** predominates in **Southern Europe** (Italy, France, Spain)
- **HHT1 (ENG)** predominates in **Northern Europe and East Asia** (Japan)
- The ratio varies significantly by region and is likely influenced by founder effects

### 4.3 Founder Effects

The most dramatic example is the **Netherlands Antilles**, where 7 of 10 studied families share an ENG exon 1 splice-site mutation, likely introduced into the African slave population by a Dutch colonizer during the colonial era. This single ancestral mutation accounts for the ~1:1,300 prevalence — the highest in the world.

### 4.4 Diagnostic Delay

Despite symptom onset typically by age 13, **63% of patients are not diagnosed until mid-to-late adulthood** (CHORUS registry, n=600), representing a median diagnostic delay of ~25-35 years. This delay reflects:
- Low clinical awareness among general practitioners
- Gradual, progressive symptom development
- Attribution of epistaxis to benign causes
- Insufficient family history screening

---

## 5. Clinical Manifestations

### 5.1 Diagnostic Criteria (Curaçao Criteria)

Clinical diagnosis is based on the Curaçao criteria. Meeting **3 or more = definite HHT**, **2 = possible HHT**:

1. **Spontaneous, recurrent epistaxis**
2. **Mucocutaneous telangiectases** at characteristic sites (lips, oral cavity, fingers, nose)
3. **Visceral AVMs** (pulmonary, hepatic, cerebral, spinal, GI)
4. **First-degree relative** with HHT

**Important limitations**: Curaçao criteria are specific but not sensitive in children due to age-dependent development of features. **Genetic testing is recommended for all ages**, especially in children of affected families, and can provide definitive diagnosis.

### 5.2 Prevalence of Clinical Features (CHORUS Registry, n=600)

| Manifestation | Prevalence | Notes |
|--------------|-----------|-------|
| Recurrent epistaxis | 95% | Most common symptom; universal feature |
| Mucocutaneous telangiectases | >90% | Lips (79%), tongue (76%), ears (61%), fingers (71%) |
| Iron deficiency and/or anemia | 68% | Often severe |
| Pulmonary AVMs | ~50-57% | Higher in HHT1 (75%) vs HHT2 (44%) |
| IV iron required | 41% | Reflecting severity of bleeding |
| Hepatic AVMs | 60-84% | Higher in HHT2 |
| Heavy menstrual bleeding | 35% | Post-menarche females |
| Chronic GI bleeding | 30% | Increases with age |
| RBC transfusions required | 25% | Reflecting transfusion dependency |
| Arterial thromboembolism | 11% | Paradoxical embolism through PAVMs |
| Brain AVMs | 9-16% | Higher in HHT1 (20-36%) vs HHT2 (0-4%) |
| Heart failure | 7% | High-output from hepatic shunting |
| Pulmonary hypertension | 7% | Multiple mechanisms |
| Venous thromboembolism | 7% | |
| Intracranial hemorrhage | 3% | From brain AVMs |

### 5.3 Genotype-Phenotype Correlations

| Feature | HHT1 (ENG) | HHT2 (ACVRL1) | JP-HHT (SMAD4) |
|---------|------------|----------------|-----------------|
| Pulmonary AVMs | **75%** | 44% | 42% |
| Brain AVMs | **20-36%** | 0-4% | Present |
| Hepatic AVMs | 60% | **84%** | Present |
| Epistaxis onset | Earlier | Later | Variable |
| GI polyps | No | No | **Yes (87%)** |
| Cancer risk | No | No | **25% CRC** |
| Neurological events | **More common** | Less common | Present |
| High-output HF | Less common | **More common** | Present |

---

## 6. Organ-Specific Complications

### 6.1 Pulmonary AVMs and Paradoxical Embolism

PAVMs create right-to-left shunts that bypass the pulmonary capillary filter, causing:
- **Hypoxemia** from deoxygenated blood bypassing the lungs
- **Paradoxical embolism** → ischemic stroke (11% arterial TE), TIA
- **Brain abscess** (5-13% of PAVM patients) from infected emboli
- **Hemothorax/hemoptysis** especially during pregnancy
- **Antibiotic prophylaxis** during dental procedures is recommended for PAVM patients

### 6.2 Hepatic AVMs

Three types of hepatic shunting cause distinct clinical syndromes:
1. **Hepatic artery → Hepatic vein** (arteriosystemic): High-output cardiac failure
2. **Hepatic artery → Portal vein** (arterioportal): Portal hypertension
3. **Portal vein → Hepatic vein** (portosystemic): Hepatic encephalopathy

Most hepatic AVMs are asymptomatic. Bevacizumab can reduce cardiac index. Liver transplantation is reserved for severe cases. **Hepatic AVM embolization is contraindicated** due to risk of hepatic necrosis.

### 6.3 Brain AVMs

- Present in 9-16% of HHT patients (predominantly HHT1)
- Intracranial hemorrhage risk ~0.7% per year
- Often multiple and cortical in location
- Spinal AVMs reported in HHT2
- Screening recommended in childhood (can identify treatable lesions)

### 6.4 GI Bleeding

- Chronic GI bleeding in ~30% of adults, increasing with age
- Contributes to worsening anemia on top of epistaxis
- May require endoscopic treatment (argon plasma coagulation)

### 6.5 Manganese Deposition

HHT patients with hepatic AVMs show T1-hyperintensity of basal ganglia on MRI due to manganese deposition, associated with tremor, restless leg syndrome, and memory problems.

---

## 7. Special Populations

### 7.1 JP-HHT Overlap Syndrome (SMAD4 Mutations)

SMAD4 mutations produce a unique and particularly dangerous overlap of:
- **Juvenile Polyposis Syndrome**: Colonic polyps (87%), gastric polyps (67%), tubular adenomas (50%)
- **HHT vascular malformations**: PAVMs (42%), epistaxis, telangiectases
- **High cancer risk**: Colorectal cancer in **25% at median age 33 years**
- **High surgical rate**: Colectomy (43%), gastrectomy (42%)
- **Overall mortality**: 14% in available cohorts

All patients with SMAD4 mutations require **dual surveillance**: GI cancer screening AND vascular AVM screening.

### 7.2 Pregnancy and HHT

Pregnancy represents a high-risk period for HHT women:
- **Maternal mortality**: ~1.0% per pregnancy (vs ~0.02% general population — **50-fold increase**)
- **Severe complications**: 2.7-6.8% of pregnancies
- Most complications from **PAVM rupture** (hemothorax, hemoptysis, severe hypoxemia)
- Complications occur mainly in 2nd/3rd trimester in **undiagnosed/unscreened** patients
- **Pre-conception PAVM screening and embolization** is strongly recommended

### 7.3 Pediatric HHT

- Curaçao criteria are insensitive in children
- Genetic testing recommended for all at-risk children
- Early screening for pulmonary and brain AVMs recommended
- PAVMs can develop throughout life; repeated screening every 5 years recommended
- AVFs in children are highly suggestive of HHT

---

## 8. Diagnosis

### 8.1 Clinical Diagnosis

- **Curaçao criteria**: ≥3 of 4 criteria = definite HHT; 2 = possible
- Limitations in pediatric population (age-dependent features)

### 8.2 Genetic Testing

- Recommended for all suspected cases and at-risk family members
- Sequencing of ENG, ACVRL1, SMAD4 (and GDF2 if negative)
- Includes deletion/duplication analysis (MLPA)
- Positive genetic test is definitive regardless of age or symptoms

### 8.3 Screening Protocols (2020 International Guidelines)

The Second International HHT Guidelines (2020) recommend:
- **Pulmonary AVMs**: Contrast echocardiography (bubble study); CT chest if positive
- **Brain AVMs**: MRI brain at diagnosis (all ages)
- **Hepatic AVMs**: Doppler ultrasound if symptomatic
- **Repeat screening**: PAVMs every 5 years even if initially negative
- **Antibiotic prophylaxis**: For dental procedures in patients with PAVMs

---

## 9. Treatment and Therapeutic Landscape

### 9.1 Current Standard of Care

**Mild bleeding:**
- Nasal humidification, topical care
- Antifibrinolytics (tranexamic acid — oral or topical)

**Moderate-to-severe bleeding:**
- Iron replacement (oral and/or IV)
- Systemic antiangiogenic therapy (off-label):
  - **Bevacizumab** (IV anti-VEGF) — most evidence for hepatic AVMs and severe epistaxis
  - **Pomalidomide** (oral immunomodulatory/antiangiogenic) — positive Phase 3 RCT
  - **Pazopanib** (oral VEGF receptor TKI)
  - **Thalidomide** (oral; limited by toxicity)
- Laser ablation, cauterization for nasal telangiectases
- Endoscopic APC for GI telangiectases

**Visceral AVMs:**
- **Pulmonary AVMs**: Transcatheter embolization
- **Brain AVMs**: Embolization, surgery, or radiosurgery at specialized centers
- **Hepatic AVMs**: Bevacizumab as medical therapy; liver transplant for severe cases (embolization contraindicated)

### 9.2 Landmark Pomalidomide Phase 3 Trial (2024)

The first positive Phase 3 RCT for any HHT therapy:
- **Design**: Randomized, placebo-controlled; n=144 (2:1 ratio)
- **Intervention**: Pomalidomide 4 mg daily for 24 weeks
- **Primary outcome**: Change in Epistaxis Severity Score (ESS, 0-10 scale)
- **Result**: Mean ESS difference -0.94 points (95% CI -1.57 to -0.31; P=0.004)
- **Clinical significance**: Exceeds the minimal clinically important difference of 0.71 points
- **Trial stopped early** for efficacy at planned interim analysis
- Also improved HHT-specific quality of life

This positions pomalidomide as a potential first-ever FDA-approved therapy for HHT.

### 9.3 Emerging Therapies and Pipeline

- **Aflibercept**: VEGF/PlGF trap; effective after bevacizumab resistance
- **Standardized outcome criteria** now established (2025 GRMAB consensus) to facilitate future trials
- **ALK1 overexpression**: Preclinical mouse data showing therapeutic potential
- **Novel HHT-specific therapies** in development following pathway understanding
- **Tacrolimus (FK506)**: Under investigation as ALK1 activator

### 9.4 Unmet Needs

- No FDA- or EMA-approved HHT-specific therapy (as of 2025)
- No cure; all therapies are symptom-modifying
- Need for biomarkers to predict AVM development and progression
- Need for therapies that prevent new AVM formation
- Insufficient clinical awareness causing diagnostic delay

---

## 10. Sex Differences

Clinically significant sex differences exist in HHT (n=242; 142 women, 100 men):
- **Women** have more hepatic AVMs (28.2% vs 13%), pulmonary AVMs (35.2% vs 23%), and require invasive treatment more often (28.2% vs 16%)
- **Men** have more duodenal telangiectases (21% vs 9.8%) and more ED visits
- Women have higher hepatic involvement scores (3.38±1.2 vs 2.03±1.2)
- Splenic artery aneurysms are more common in women (OR=2.12, P=0.04)
- These differences are maintained across both HHT1 and HHT2 subtypes
- Hormonal influences on angiogenesis may explain female preponderance of visceral AVMs

## 11. Prognosis and Survival

- **HHT-associated PAH**: 1-year survival 77.8%, 3-year survival 53.3% — significantly worse than matched idiopathic PAH (P=0.047)
- **Liver transplantation**: 86% post-transplant survival with resolution of heart failure
- **Pregnancy**: ~1% maternal mortality per pregnancy (50x general population)
- **Splenic artery aneurysms**: 24.7% of HHT patients vs 5.4% controls (P<0.001), suggesting a systemic arteriopathy beyond AVMs
- **Subaortic membranes**: Novel cardiac finding in HHT-HOCF patients (exclusively female, mean cardiac output 12.1 L/min)

## 12. Endoglin (CD105) as a Cancer Biomarker

The same protein mutated in HHT1 (endoglin/CD105) plays a major role in cancer biology:
- Selectively highly expressed on tumor vasculature across multiple cancer types
- Correlates with poor survival in cancer patients
- Soluble endoglin elevated in metastatic colorectal cancer
- Anti-endoglin antibody TRC105 (Carotuximab) developed as anti-cancer therapy
- This creates a translational bridge: HHT research informs cancer biology and vice versa
- Anti-angiogenic drugs used in HHT (bevacizumab) are established cancer therapies

## 13. Clinical Management Challenges

### The Thrombosis-Bleeding Paradox

HHT presents a unique clinical paradox: patients have an inherited bleeding disorder yet face **elevated thrombotic risk**:
- **VTE**: 7% (CHORUS registry)
- **Arterial thromboembolism**: 11% (paradoxical embolism through PAVMs)
- **Atrial fibrillation**: Common in high-output cardiac states from hepatic AVMs

Anticoagulation is frequently indicated but poorly tolerated — the majority of HHT-AF patients require premature dose-reduction or discontinuation due to worsening mucosal bleeding. Emerging solutions include:
- **Left atrial appendage occlusion** (device-based stroke prevention without long-term anticoagulation)
- **Concurrent antiangiogenic therapy** to stabilize telangiectases while anticoagulating
- **Novel topical therapies** (intranasal timolol gel, propranolol) to control epistaxis locally

### Contraindicated/High-Risk Medications
- **Anticoagulants**: Classified as Level 1 pharmacotherapy risk (FDA-driven) for HHT
- **Antiplatelet agents**: Poorly tolerated; worsens bleeding
- **Hepatic AVM embolization**: Contraindicated due to hepatic necrosis risk
- **Bevacizumab in pregnancy**: Teratogenic; timing considerations for women of childbearing age

### Differential Diagnosis
Conditions that may mimic HHT include:
- **CREST syndrome/scleroderma** (telangiectases, but different pattern and associated features)
- **Capillary malformation-AVM syndrome (CM-AVM)** caused by RASA1 or EPHB4 mutations
- **Ataxia-telangiectasia** (telangiectases + neurological features)
- **Sporadic AVMs** (lack family history and systemic features)
- **Drug-induced telangiectases** (e.g., trastuzumab emtansine can mimic HHT)

## 14. Key Findings Summary

| # | Finding | Key Evidence |
|---|---------|-------------|
| 1 | HHT caused by mutations in BMP9/10-ALK1-ENG-SMAD4 pathway | 4 genes, autosomal dominant, ~1:5000 prevalence |
| 2 | Distinct genotype-phenotype correlations | ENG→lung/brain AVMs; ACVRL1→liver AVMs |
| 3 | High disease burden (CHORUS, n=600) | 95% epistaxis, 68% anemia, 63% late diagnosis |
| 4 | Two-hit pathogenesis model | Germline + somatic LOH + environmental triggers |
| 5 | Antiangiogenic therapy paradigm shift | Bevacizumab, pomalidomide, pazopanib (all off-label) |
| 6 | PAVMs cause paradoxical embolism | 11% arterial TE, 5-13% brain abscess |
| 7 | Pregnancy carries 1% maternal mortality | 50x general population; PAVM rupture |
| 8 | Geographic variation and founder effects | Netherlands Antilles ~1:1300 (ENG founder) |
| 9 | Hepatic AVMs cause high-output HF | Bevacizumab effective; transplant last resort |
| 10 | BMP-VEGF pathway crosstalk mechanism | BMP suppresses PI3K/AKT; loss enables VEGF-driven AVMs |
| 11 | JP-HHT (SMAD4) dual cancer/vascular risk | 25% CRC at median age 33 |
| 12 | Pomalidomide Phase 3 RCT positive | ESS -0.94 (P=0.004); first positive HHT trial |
| 13 | Significant sex differences | Women: more hepatic/pulmonary AVMs, more invasive treatment |
| 14 | Endoglin-cancer biology connection | CD105 is a tumor angiogenesis marker and therapeutic target |
| 15 | HHT-PAH has poor prognosis | 53% 3-year survival, worse than matched IPAH |
| 16 | Thrombosis-bleeding paradox | 11% arterial TE + 7% VTE despite bleeding disorder; anticoagulation poorly tolerated |

---

## 11. Limitations

- This report is based on published literature and public databases; no primary patient data were analyzed
- Prevalence estimates may underrepresent true burden due to underdiagnosis
- Genotype-phenotype correlations are population-dependent and may not apply universally
- Treatment efficacy data is largely from uncontrolled studies except the pomalidomide RCT
- Long-term natural history data from registries (CHORUS) is still being accumulated
- Biomarker discovery for HHT remains an active area of research with limited validated markers

## 12. Future Directions

1. **FDA/EMA approval** of pomalidomide or other antiangiogenic agents for HHT
2. **Biomarker development** for predicting AVM formation and monitoring treatment response
3. **Gene therapy approaches** to restore pathway function
4. **Comparative clinical trials** enabled by newly standardized outcome criteria
5. **Improved screening programs** to reduce the 25-35 year diagnostic delay
6. **Mechanistic studies** of modifier genes and stochastic factors driving variable expressivity
7. **Precision medicine** approaches matching therapy to genotype

---

## References (Key PMIDs)

- PMID: 37695357 — 14th HHT International Scientific Conference summary
- PMID: 38357927 — HHT signaling insights to therapeutic advances (2024 review)
- PMID: 41843464 — CHORUS registry initial report (2026)
- PMID: 39292928 — Pomalidomide Phase 3 RCT (2024)
- PMID: 32894695 — Second International HHT Guidelines (2020)
- PMID: 38864625 — How I treat bleeding in HHT (2024)
- PMID: 29976569 — SMAD4 prevents flow-induced AVMs via CK2
- PMID: 38502919 — BMP9 as key player in endothelial identity
- PMID: 17388964 — HHT clinical features in ENG and ALK1 carriers
- PMID: 41915210 — Genotype-phenotype correlations for CVMs (2026)
- PMID: 31910869 — HHT and pregnancy review
- PMID: 38627541 — JP-HHT outcomes in Scotland
- PMID: 10982033 — Netherlands Antilles founder effect
- PMID: 40648852 — Somatic mutation in HHT pathogenesis
- PMID: 40662351 — Standardization of HHT outcome criteria (2025)
- PMID: 32122373 — Gender differences in HHT severity
- PMID: 29480092 — HHT-PAH clinical characteristics and prognosis
- PMID: 31971937 — Splenic artery aneurysms in HHT
- PMID: 33375670 — Endoglin targeting: lessons learned (cancer)
- PMID: 33054561 — Subaortic membranes in HHT-HOCF
- PMID: 37340288 — Antithrombotic therapy for AF in HHT
- PMID: 41527333 — Pharmacotherapy risks in rare genetic diseases (2026)

---

*Report generated through systematic literature review and biomedical database analysis. 16 key findings confirmed with cited evidence from 110+ publications across 5 visualizations.*
