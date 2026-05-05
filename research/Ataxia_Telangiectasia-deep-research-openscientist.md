---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-05T07:20:43.781584'
end_time: '2026-05-05T07:46:59.040347'
duration_seconds: 1575.26
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ataxia-telangiectasia
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
citation_count: 46
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ataxia-telangiectasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Ataxia-telangiectasia** covering all of the
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

# Ataxia-Telangiectasia: Comprehensive Disease Characterization Report

## Summary

Ataxia-telangiectasia (A-T) is an autosomal recessive, multisystem disorder caused by biallelic loss-of-function mutations in the **ATM** gene (chromosome 11q22.3), which encodes a 3,056-amino-acid serine/threonine protein kinase of the phosphatidylinositol 3-kinase-related kinase (PIKK) family. ATM is the master regulator of the cellular DNA double-strand break (DSB) response, and its absence disrupts DNA repair, cell cycle checkpoints, apoptosis, redox homeostasis, and mitochondrial function. The disease presents as a phenotypic continuum from severe classical childhood-onset A-T—characterized by progressive cerebellar ataxia, oculocutaneous telangiectasia, combined immunodeficiency, a 56-fold increased cancer risk, and progressive pulmonary disease—to milder adult-onset variant forms, with disease severity determined by residual ATM kinase activity.

Epidemiologically, A-T affects approximately 1 in 40,000 to 1 in 100,000 live births worldwide, with autosomal recessive inheritance and a carrier frequency of approximately 1–3% in the general population. The Kaplan-Meier 20-year survival rate is 53.4%, with cancer and respiratory tract infections independently associated with mortality. Patients with null ATM mutations experience earlier cancer onset (primarily hematologic malignancies), while those with hypomorphic mutations more often succumb to respiratory infections. There is no curative therapy, but multidisciplinary supportive care—including immunoglobulin replacement, aggressive pulmonary management, and cancer surveillance—improves quality of life. Emerging therapies including triheptanoin (targeting mitochondrial dysfunction) and intra-erythrocyte dexamethasone (sustained corticosteroid delivery) have shown promise in clinical trials.

The pathophysiology involves interconnected mechanisms of defective DSB repair, oxidative stress targeting cerebellar Purkinje cells, mitochondrial dysfunction with impaired ER-mitochondrial connectivity, neuroinflammation via the cGAS-STING pathway driven by cytosolic DNA accumulation, and impaired V(D)J/class-switch recombination leading to immunodeficiency. This report provides a comprehensive characterization across 15 disease dimensions with ontology annotations and evidence citations to support knowledge base population.

---

## 1. Disease Information

### Overview

Ataxia-telangiectasia (A-T), also known as **Louis-Bar syndrome**, is a rare autosomal recessive neurodegenerative disorder first described in 1926 and later characterized by Madame Louis-Bar in 1941. It is classified as both a primary immunodeficiency and a genomic instability syndrome. A-T is characterized by progressive cerebellar ataxia typically manifesting in early childhood, oculocutaneous telangiectasia, variable immunodeficiency, radiosensitivity, susceptibility to malignancies, and metabolic abnormalities including insulin resistance and endocrine dysfunction. As summarized in a comprehensive review: "Ataxia-telangiectasia (A-T) is an autosomal recessive primary immunodeficiency (PID) disease that is caused by mutations in ataxia-telangiectasia mutated (ATM) gene encoding a serine/threonine protein kinase. A-T patients represent a broad range of clinical manifestations including progressive cerebellar ataxia, oculocutaneous telangiectasia, variable immunodeficiency, radiosensitivity, susceptibility to malignancies, and increased metabolic diseases" ([PMID: 30685876](https://pubmed.ncbi.nlm.nih.gov/30685876/)).

### Key Identifiers

| Database | Identifier |
|----------|-----------|
| OMIM | #208900 (phenotype); *607585 (ATM gene) |
| Orphanet | ORPHA:100 |
| ICD-10 | G11.3 (Cerebellar ataxia with defective DNA repair) |
| ICD-11 | 8A03.11 |
| MeSH | D001260 |
| MONDO | MONDO:0008840 |
| GARD | 5862 |

### Synonyms and Alternative Names

- Ataxia-telangiectasia (A-T)
- Louis-Bar syndrome
- Boder-Sedgwick syndrome
- ATM syndrome / ATM deficiency
- Cerebello-oculocutaneous telangiectasia

### Data Sources

This report is derived from aggregated disease-level resources including OMIM, Orphanet, GeneReviews, ClinVar, published cohort studies (particularly European A-T registries from France, Netherlands, Germany, and the UK), clinical trials, and primary research literature comprising 78 reviewed papers.

---

## 2. Etiology

### Disease Causal Factors

A-T is a monogenic Mendelian disorder caused exclusively by biallelic pathogenic variants in the **ATM** gene (OMIM *607585), located on chromosome 11q22.3. ATM encodes a 3,056-amino-acid serine/threonine protein kinase belonging to the phosphatidylinositol 3-kinase-related kinase (PIKK) family. The ATM protein is the master regulator of the cellular DNA damage response (DDR), specifically activated by DNA double-strand breaks (DSBs). "ATM is a central kinase that activates an extensive network of responses to cellular stress via a signaling role. ATM is activated by DNA double strand breaks (DSBs) and by oxidative stress, subsequently phosphorylating a plethora of target proteins" ([PMID: 34573351](https://pubmed.ncbi.nlm.nih.gov/34573351/)). The disease is genetic in origin with no environmental or infectious causative factors ([PMID: 9735376](https://pubmed.ncbi.nlm.nih.gov/9735376/)).

### Genetic Risk Factors

- **Causal variants**: Over 600 distinct pathogenic variants reported in ATM, including truncating (nonsense, frameshift), splice-site, missense, and large genomic rearrangements (e.g., a 90-kb duplication spanning exons 17–61; [PMID: 30888062](https://pubmed.ncbi.nlm.nih.gov/30888062/))
- **Genotype-phenotype correlation**: The definitive genotype-phenotype study of 51 patients established that "patients without ATM kinase activity showed the classical phenotype. The presence of ATM protein, correlated with slightly better immunological function. Residual kinase activity correlated with a milder and essentially different neurological phenotype, absence of telangiectasia, normal endocrine and pulmonary function, normal immunoglobulins, significantly lower X-ray hypersensitivity in lymphocytes, and extended lifespan" ([PMID: 22213089](https://pubmed.ncbi.nlm.nih.gov/22213089/))
- **Founder mutations**: Population-specific founder mutations identified in North Caucasus ethnic groups ([PMID: 37851290](https://pubmed.ncbi.nlm.nih.gov/37851290/)), Kyrgyzstan (homozygous c.5932G>A; [PMID: 41451872](https://pubmed.ncbi.nlm.nih.gov/41451872/)), Ashkenazi Jewish, and other populations
- **Consanguinity**: Significantly increases risk; "the findings confirm that consanguineous unions increase the risk of developing Louis-Bar syndrome, as they elevate the likelihood of inheriting identical mutant alleles" ([PMID: 41451872](https://pubmed.ncbi.nlm.nih.gov/41451872/))
- **Modifier genes**: The DNA damage checkpoint gene **HUS1** modifies A-T severity; simultaneous ATM and HUS1 defects cause synthetic lethality in mice ([PMID: 22575700](https://pubmed.ncbi.nlm.nih.gov/22575700/))

### Heterozygous Carrier Risk

ATM heterozygous carriers (~1–3% of the general population) have a moderately increased cancer risk. "ATM germline pathogenic variants (GPVs) are associated with a moderately increased risk of female breast cancer, pancreatic cancer, and prostate cancer" ([PMID: 39636577](https://pubmed.ncbi.nlm.nih.gov/39636577/)). The pooled prevalence of ATM variants in breast cancer patients was 7% (95% CI: 5–8%) ([PMID: 34493284](https://pubmed.ncbi.nlm.nih.gov/34493284/)).

### Environmental Risk Factors

- **Ionizing radiation**: A-T patients are exquisitely radiosensitive; exposure to therapeutic radiation can cause severe, potentially fatal toxicity. Diagnostic imaging with ionizing radiation should be avoided when possible; radiation-free techniques (US, MRI) are recommended ([PMID: 36186632](https://pubmed.ncbi.nlm.nih.gov/36186632/))
- **Genotoxic chemicals**: Radiomimetic agents and topoisomerase inhibitors pose increased risk due to defective DSB repair

### Protective Factors

- **Residual ATM kinase activity**: The single most important modifier; even small amounts of residual kinase activity significantly ameliorate disease course ([PMID: 22213089](https://pubmed.ncbi.nlm.nih.gov/22213089/))
- **Antioxidants**: The antioxidant CTMIO was shown to correct neurobehavioral deficits and reduce oxidative damage to Purkinje cells in Atm−/− mice, dramatically delaying thymic lymphoma onset ([PMID: 16934683](https://pubmed.ncbi.nlm.nih.gov/16934683/))
- **NAD+ supplementation**: Boosting intracellular NAD+ alleviates senescence phenotypes and mitochondrial dysfunction in ATM-deficient cells ([PMID: 33734555](https://pubmed.ncbi.nlm.nih.gov/33734555/))

### Gene-Environment Interactions

ATM heterozygotes carrying rare missense variants of uncertain significance showed increased risk of radiation-associated contralateral breast cancer (carriers with RT: RR = 2.98, 95% CI 1.31–6.80 vs. without RT: RR = 0.38, 95% CI 0.09–1.55), suggesting gene-radiation interaction ([PMID: 32119081](https://pubmed.ncbi.nlm.nih.gov/32119081/)). In homozygous A-T patients, elevated Cu/Zn-SOD paradoxically exacerbated radiosensitivity and hematopoietic abnormalities, consistent with oxidative stress contributing to the phenotype ([PMID: 11285218](https://pubmed.ncbi.nlm.nih.gov/11285218/)).

---

## 3. Phenotypes

### Neurological Phenotypes

| Phenotype | HPO Term | Onset | Frequency | Progression |
|-----------|----------|-------|-----------|-------------|
| Progressive cerebellar ataxia | HP:0001251 | 1–4 years | >95% | Progressive, wheelchair by age 10–12 |
| Oculomotor apraxia | HP:0000657 | Early childhood | ~90% | Progressive |
| Dysarthria/slurred speech | HP:0001260 | Childhood | >80% | Progressive |
| Choreoathetosis | HP:0001266 | Variable | 30–50% | Variable |
| Dystonia | HP:0001332 | Variable | 20–40% | May predominate in variant A-T ([PMID: 37009283](https://pubmed.ncbi.nlm.nih.gov/37009283/)) |
| Peripheral neuropathy | HP:0009830 | Late childhood | 50–70% | Progressive |
| Cognitive slowing | HP:0100543 | Adolescence | Variable | Progressive |

### Dermatological Phenotypes

| Phenotype | HPO Term | Onset | Frequency |
|-----------|----------|-------|-----------|
| Oculocutaneous telangiectasia | HP:0000989, HP:0000565 | Age 3–6 years | ~80–90% classical; absent in variant |
| Café-au-lait spots | HP:0000957 | Variable | 10–30% |
| Cutaneous granulomas | HP:0100764 | Variable | 5–10% |
| Premature graying of hair | HP:0002216 | Adolescence | Variable |
| Progeric skin changes | HP:0007495 | Variable | Variable |

### Immunological Phenotypes

| Phenotype | HPO Term | Onset | Frequency |
|-----------|----------|-------|-----------|
| IgA deficiency | HP:0004313 | Congenital | 60–80% |
| IgG subclass deficiency | HP:0004315 | Congenital | 50–70% |
| Hyper-IgM phenotype | HP:0002790 | Variable | 10–20% |
| T-cell lymphopenia | HP:0001888 | Congenital | >80% |
| Decreased switched memory B cells | HP:0002846 | Congenital | >80% |
| Recurrent sinopulmonary infections | HP:0002783 | Early childhood | >80% |

Detailed immunological analysis confirmed that "patients with AT have a broad spectrum of cellular and humoral deficiencies" ([PMID: 33052516](https://pubmed.ncbi.nlm.nih.gov/33052516/)), and "immunoglobulin deficiency in AT is caused by disturbed development of class-switched memory B cells. ATM deficiency affects both germinal center reaction and choice of DNA-repair pathway in class switching" ([PMID: 38280573](https://pubmed.ncbi.nlm.nih.gov/38280573/)).

### Pulmonary Phenotypes

| Phenotype | HPO Term | Onset | Frequency |
|-----------|----------|-------|-----------|
| Recurrent respiratory infections | HP:0002205 | Early childhood | >80% |
| Bronchiectasis | HP:0002110 | Childhood–adolescence | 40–60% |
| Restrictive lung disease | HP:0002091 | Progressive | >70% |
| Interstitial lung disease | HP:0006530 | Variable | 20–30% |
| Bronchiolitis obliterans | HP:0011946 | Variable | Documented at autopsy ([PMID: 9083516](https://pubmed.ncbi.nlm.nih.gov/9083516/)) |

FVC declines from 67 ± 8% predicted while walking to 19 ± 6% predicted at end-stage. A sharp elevation in FEF25-75/FVC ratio was observed when FEV1 was ~45% predicted, approximately 2 years prior to death ([PMID: 26033643](https://pubmed.ncbi.nlm.nih.gov/26033643/)). Lung disease in A-T "shows similarities to the lung disease seen in cystic fibrosis" ([PMID: 23761391](https://pubmed.ncbi.nlm.nih.gov/23761391/)).

### Oncological Phenotypes

Cancer risk is 56-fold increased overall (SIR = 56, 95% CI: 33–88) in a population-based German cohort: "Among the 160 patients with AT, we observed 19 cases of childhood cancer (15 cases of lymphoma, three cases of leukemia, and one case of medulloblastoma) versus 0.32 expected" ([PMID: 34597127](https://pubmed.ncbi.nlm.nih.gov/34597127/)). Non-Hodgkin lymphoma SIR = 470 (95% CI: 225–865); Hodgkin lymphoma SIR = 215 (95% CI: 58–549). Approximately 14% of patients develop cancer by age 18.

### Endocrine and Metabolic Phenotypes

| Phenotype | HPO Term | Onset | Frequency |
|-----------|----------|-------|-----------|
| Growth failure | HP:0001510 | After age 8 | >60% |
| Insulin resistance/diabetes | HP:0000855 | Adolescence | 20–40% |
| Gonadal failure | HP:0000135 | Puberty | Variable ([PMID: 40270454](https://pubmed.ncbi.nlm.nih.gov/40270454/)) |

Mean weight, height, and BMI Z-scores were −1.0, −1.2, and −0.4 respectively, with 35/101 children having weight Z-scores below −2. Decline was most obvious after age 8 ([PMID: 27573920](https://pubmed.ncbi.nlm.nih.gov/27573920/)).

### Laboratory Abnormalities

| Finding | HPO Term | Frequency |
|---------|----------|-----------|
| Elevated alpha-fetoprotein | HP:0006254 | >95% |
| Elevated transaminases | HP:0002910 | 40–60% |
| Chromosomal instability | HP:0003220 | Universal |
| Radiosensitivity | HP:0200144 | Universal |

### Quality of Life Impact

A-T profoundly impacts quality of life across multiple domains: progressive loss of ambulation (typically by age 10–12), speech deterioration, swallowing difficulty, increasing dependence for all activities of daily living, chronic respiratory symptoms, frequent infections, fatigue, and social isolation. Cancer treatment is further complicated by radiosensitivity.

---

## 4. Genetic/Molecular Information

### Causal Gene

- **Gene**: ATM (Ataxia-Telangiectasia Mutated)
- **HGNC ID**: HGNC:795
- **NCBI Gene ID**: 472
- **OMIM**: *607585
- **Chromosomal location**: 11q22.3
- **Gene structure**: 66 exons spanning ~150 kb of genomic DNA
- **Protein**: 3,056 amino acids, ~370 kDa

ATM belongs to the PIKK family, sharing structural features including N-terminal HEAT repeats, FAT domain, kinase domain, and C-terminal FATC domain. "A characteristic PIKK member comprises of an N-terminal HEAT domain, followed by FAT domain, a highly conserved kinase catalytic domain, and a C-terminal FATC domain" ([PMID: 32114444](https://pubmed.ncbi.nlm.nih.gov/32114444/)). "The FATC domain of ATM mediates the interaction between ATM and Tip60, a histone acetyltransferase that regulates activation of ATM" ([PMID: 16603769](https://pubmed.ncbi.nlm.nih.gov/16603769/)). The three-dimensional structure reveals that "the highly conserved C-terminal PIKK catalytic domain forms a central structure from which FAT and FATC domains protrude" ([PMID: 15698568](https://pubmed.ncbi.nlm.nih.gov/15698568/)).

### Pathogenic Variants

- **Variant types**: Truncating (~85% in classical A-T: nonsense, frameshift), splice-site (~15%), missense (~10% overall), large deletions/duplications
- **Classification**: >800 variants in ClinVar; majority classified as pathogenic or likely pathogenic
- **Novel variants**: Continuously identified, including a 90-kb duplication spanning exons 17–61 detected by NGS ([PMID: 30888062](https://pubmed.ncbi.nlm.nih.gov/30888062/)) and compound heterozygous mutations in diverse populations ([PMID: 37009283](https://pubmed.ncbi.nlm.nih.gov/37009283/); [PMID: 41044616](https://pubmed.ncbi.nlm.nih.gov/41044616/))
- **Functional consequence**: Predominantly **loss-of-function**; null mutations abolish kinase activity (classical A-T); hypomorphic mutations retain residual activity (variant A-T)
- **Somatic vs. germline**: A-T is caused by germline biallelic mutations. Somatic ATM mutations are frequent in various cancers; approximately 3% of lung cancers harbor biallelic ATM mutations ([PMID: 38807759](https://pubmed.ncbi.nlm.nih.gov/38807759/))
- **Population frequency**: Carrier frequency ~1–3% (1 in 50–100). Individually rare variants but collectively common

### Modifier Genes

- **HUS1**: Modifies A-T severity; simultaneous ATM and HUS1 defects cause synthetic lethality, while partial Hus1 impairment with Atm loss produces synergistic increases in genomic instability and developmental defects ([PMID: 22575700](https://pubmed.ncbi.nlm.nih.gov/22575700/))
- **SOD1**: Elevated Cu/Zn-SOD exacerbates the A-T phenotype, suggesting redox balance is a modifier ([PMID: 11285218](https://pubmed.ncbi.nlm.nih.gov/11285218/))

### Epigenetic Information

ATM deficiency leads to impaired DNA damage-induced histone modifications, particularly γH2AX phosphorylation. ATM regulates chromatin remodeling through its interaction with the Tip60 histone acetyltransferase and through phosphorylation of KAP1/TRIM28. ATM phosphorylates SPOP at Ser119, promoting non-degradative ubiquitination of HIPK2, which then phosphorylates HP1γ to promote dissociation from H3K9me3 marks for DNA damage repair ([PMID: 34133717](https://pubmed.ncbi.nlm.nih.gov/34133717/)). ATM-mediated senescence involves STING-dependent pathways and SASP ([PMID: 33734555](https://pubmed.ncbi.nlm.nih.gov/33734555/)).

### Chromosomal Abnormalities

Characteristic cytogenetic findings include inversions and translocations involving chromosomes 7 and 14 at TCR and immunoglobulin gene loci: inv(7)(p14q35), t(7;14)(p14;q11.2), t(14;14)(q11.2;q32). "At the cellular level, one of the most prominent features of A-T cells is chromosome rearrangement, especially that in T lymphocytes" ([PMID: 34440406](https://pubmed.ncbi.nlm.nih.gov/34440406/)).

---

## 5. Environmental Information

### Environmental Factors

- **Ionizing radiation**: The most critical environmental factor. A-T patients are extremely radiosensitive; diagnostic imaging should use non-ionizing methods (US, MRI) whenever possible ([PMID: 36186632](https://pubmed.ncbi.nlm.nih.gov/36186632/))
- **Genotoxic chemicals**: Radiomimetic agents and topoisomerase inhibitors pose increased risk

### Lifestyle Factors

- **Nutrition**: Growth failure is progressive; PEG tube feeding should be considered proactively from age 8 ([PMID: 27573920](https://pubmed.ncbi.nlm.nih.gov/27573920/))
- **Physical activity**: Adapted exercise encouraged for respiratory and general health; limited by progressive ataxia
- **Respiratory care**: Avoidance of respiratory irritants is critical given pulmonary vulnerability

### Infectious Agents

A-T patients are susceptible to common bacterial respiratory pathogens due to immunodeficiency. In younger patients (<15 years), *Staphylococcus aureus*, *Haemophilus influenzae*, and *Streptococcus pneumoniae* predominate (25/27 cultured positive), while in older patients, *Pseudomonas aeruginosa* becomes prevalent (35/47 cultured positive). "Opportunistic infections of the lungs were not observed" ([PMID: 23761391](https://pubmed.ncbi.nlm.nih.gov/23761391/)). Chronic EBV infection has been associated with more severe outcomes in hyper-IgM A-T patients ([PMID: 36340711](https://pubmed.ncbi.nlm.nih.gov/36340711/)).

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

ATM is the central kinase of the DSB response. Upon DSB induction, the MRN complex (MRE11-RAD50-NBS1) recognizes breaks and recruits ATM, which undergoes autophosphorylation and monomerization. Active ATM phosphorylates >1,000 downstream substrates including H2AX (γH2AX), CHK2 (Thr68), p53 (Ser15), SMC1 (Ser966), KAP1/TRIM28 (Ser824), BRCA1, and NBS1.

Key disrupted pathways: DNA damage response (GO:0006974), p53 signaling (KEGG: hsa04115), homologous recombination (KEGG: hsa03440), non-homologous end joining (KEGG: hsa03450), V(D)J recombination (GO:0033151), and cell cycle checkpoint control (GO:0000077).

### Cellular Processes and Causal Chains

**DNA Repair Deficiency (Upstream)**

ATM-deficient neurons exhibit "defective repair of DNA double-strand breaks (DSBs) and repressed phosphorylation of ATM substrates (e.g., γH2AX, Smc1-S966, Kap1-S824, Chk2-T68, p53-S15), but normal repair of single-strand breaks" and "abnormal accumulation of topoisomerase 1-DNA covalent complexes (Top1-ccs)" ([PMID: 25032865](https://pubmed.ncbi.nlm.nih.gov/25032865/)).

**Oxidative Stress (Parallel/Amplifying)**

"Organs which develop pathologic changes in the Atm-deficient mice are targets of oxidative damage, and cerebellar Purkinje cells are particularly affected" ([PMID: 10449794](https://pubmed.ncbi.nlm.nih.gov/10449794/)). Chronic oxidative stress involves endogenous ROS overproduction, NADPH oxidase 4 (NOX4) activation, and impaired antioxidant defense ([PMID: 28063379](https://pubmed.ncbi.nlm.nih.gov/28063379/)).

**Mitochondrial Dysfunction (Intermediate)**

"A-T cells demonstrate defective endoplasmic reticulum-mitochondrial connectivity disrupting calcium homoeostasis and mitochondrial fusion, which are corrected in vitro by the triheptanoin metabolite, heptanoate" ([PMID: 40616902](https://pubmed.ncbi.nlm.nih.gov/40616902/)). Senescence phenotypes and SASP in ATM-deficient cells are mediated through STING and involve ectopic cytoplasmic DNA ([PMID: 33734555](https://pubmed.ncbi.nlm.nih.gov/33734555/)).

**Neuroinflammation via cGAS-STING (Downstream)**

"Loss of Atm in neurons and glia leads to accumulation of cytosolic DNA, increased cytokine production and constitutive activation of microglia consistent with a neuroinflammatory phenotype. Rats lacking ATM had significant loss of motor neurons and microgliosis in the spinal cord, consistent with onset of paralysis" ([PMID: 28007901](https://pubmed.ncbi.nlm.nih.gov/28007901/)).

**Impaired Class-Switch Recombination (Downstream)**

"Immunoglobulin deficiency in AT is caused by disturbed development of class-switched memory B cells. ATM deficiency affects both germinal center reaction and choice of DNA-repair pathway in class switching" ([PMID: 38280573](https://pubmed.ncbi.nlm.nih.gov/38280573/)).

### Pathophysiology Model

```
ATM Gene Mutation (Biallelic Loss-of-Function)
         │
         ▼
    Loss of ATM Kinase Activity
         │
    ┌────┼────────────────────┬──────────────────────────┐
    ▼    ▼                    ▼                          ▼
Defective   Impaired Redox   Impaired V(D)J    Defective Cell
DSB Repair  Regulation        & CSR             Cycle Checkpoints
    │         │                  │                    │
    ▼         ▼                  ▼                    ▼
Genomic     Oxidative         Immunodeficiency   Radiosensitivity
Instability Stress            ↓IgA, IgG, Hyper-IgM
    │         │                  │
    ▼         ▼                  ▼
Cancer     Mitochondrial     Recurrent Infections
Predisposition Dysfunction    Pulmonary Disease
    │         │                  │
    │         ▼                  ▼
    │    Cytosolic DNA       Respiratory Failure
    │    Accumulation
    │         │
    │         ▼
    │    cGAS-STING Activation
    │    Neuroinflammation
    │         │
    │         ▼
    │    Progressive Cerebellar
    │    Neurodegeneration
    └─────────┘
         │
         ▼
   Multisystem Disease
```

### Cell Types Involved

| Cell Type | CL Term | Role |
|-----------|---------|------|
| Purkinje cell | CL:0000121 | Primary target of cerebellar neurodegeneration |
| Microglial cell | CL:0000129 | Constitutive activation drives neuroinflammation |
| T lymphocyte | CL:0000084 | Impaired development, V(D)J recombination defects |
| B lymphocyte | CL:0000236 | Defective class-switch recombination |
| Naive B cell | CL:0000788 | Decreased numbers |
| Class-switched memory B cell | CL:0000972 | Severely reduced |
| Motor neuron | CL:0000100 | Loss documented in ATM-deficient rats |
| Respiratory epithelial cell | CL:0002368 | Increased cell death |
| Endothelial cell | CL:0000115 | Telangiectasia formation |

### GO Terms for Key Processes

- GO:0006302 — Double-strand break repair
- GO:0006974 — Cellular response to DNA damage stimulus
- GO:0000723 — Telomere maintenance
- GO:0007050 — Cell cycle arrest
- GO:0006915 — Apoptotic process
- GO:0006955 — Immune response
- GO:0033151 — V(D)J recombination
- GO:0045087 — Innate immune response (cGAS-STING)
- GO:0006979 — Response to oxidative stress
- GO:0000077 — DNA damage checkpoint signaling

### Metabolic Changes

A-T patients exhibit insulin resistance and glucose intolerance. Mitochondrial dysfunction leads to altered energy metabolism. Chronic DNA damage activates PARP, depleting NAD+ stores ([PMID: 33734555](https://pubmed.ncbi.nlm.nih.gov/33734555/)). Triheptanoin provides heptanoate to bypass ER-mitochondrial connectivity disruption through anaplerosis ([PMID: 40616902](https://pubmed.ncbi.nlm.nih.gov/40616902/)).

### Biochemical Abnormalities

- Elevated serum AFP (>95% of patients; mechanism not fully understood)
- Absent or reduced ATM protein (Western blot) and kinase activity
- Deficient γH2AX foci formation after radiation
- Radioresistant DNA synthesis (absent intra-S phase checkpoint)
- Elevated liver transaminases (40–60%)

---

## 7. Anatomical Structures Affected

### Organ Level

| Organ/System | UBERON Term | Involvement | Details |
|-------------|------------|-------------|---------|
| Cerebellum | UBERON:0002037 | Primary | Progressive atrophy, Purkinje/granule cell loss |
| Thymus | UBERON:0002370 | Primary | Hypoplasia, impaired T cell production |
| Lungs | UBERON:0002048 | Primary | Bronchiectasis, fibrosis, infections |
| Liver | UBERON:0002107 | Secondary | Steatosis, granulomatous disease, elevated AFP |
| Skin/Conjunctiva | UBERON:0001811 | Primary | Telangiectasia, granulomas |
| Bone marrow | UBERON:0002371 | Primary | Impaired lymphopoiesis |
| Gonads | UBERON:0000991 | Primary | Gonadal dysgenesis/failure |
| Spinal cord | UBERON:0002240 | Secondary | Motor neuron loss (documented in rat model) |

### Subcellular Level

| Compartment | GO CC Term | Role |
|-------------|-----------|------|
| Nucleus | GO:0005634 | DSB sensing and repair; γH2AX foci |
| Mitochondria | GO:0005739 | Dysfunction, ROS overproduction |
| Cytoplasm | GO:0005737 | Cytosolic DNA accumulation → cGAS-STING |
| Endoplasmic reticulum | GO:0005783 | Impaired ER-mitochondrial connectivity |
| Chromatin | GO:0000785 | Defective H2AX phosphorylation, KAP1 regulation |

### Localization

Neurological and vascular manifestations are bilateral and symmetric: cerebellar atrophy (UBERON:0002129), conjunctival telangiectasia (UBERON:0001811), and bronchial disease (UBERON:0001555) all affect both sides.

---

## 8. Temporal Development

### Onset

- **Typical age**: 1–4 years for gait ataxia (insidious onset)
- **Variant A-T**: Later onset (adolescence to adulthood); dystonia may be initial symptom ([PMID: 37009283](https://pubmed.ncbi.nlm.nih.gov/37009283/))

### Progression

| Stage | Age (Classical) | Key Features |
|-------|----------------|--------------|
| Early | 1–5 years | Gait ataxia, frequent falls, early infections |
| Intermediate | 5–12 years | Wheelchair dependence, telangiectasia, speech deterioration |
| Advanced | 12–20 years | Severe dysarthria, dysphagia, progressive lung disease |
| End-stage | >20 years | Respiratory failure, severe disability, high cancer risk |

- **Progression rate**: Relentlessly progressive for neurological features; respiratory decline accelerates in adolescence
- **Disease course**: Progressive, chronic, lifelong; no remissions
- **Historical median survival**: ~19–25 years for classical A-T

### Critical Periods

- **Age 8 years**: Growth decline accelerates; proactive nutritional intervention recommended ([PMID: 27573920](https://pubmed.ncbi.nlm.nih.gov/27573920/))
- **Adolescence**: Cancer risk peaks; pulmonary function rapidly declines
- **FVC ~45% predicted**: Sharp elevation in FEF25-75/FVC ratio signals imminent respiratory decompensation, approximately 2 years prior to death ([PMID: 26033643](https://pubmed.ncbi.nlm.nih.gov/26033643/))

---

## 9. Inheritance and Population

### Epidemiology

| Measure | Value |
|---------|-------|
| Prevalence | 1:40,000–1:100,000 live births |
| Carrier frequency | ~1–3% (~1 in 50–100) |

### Inheritance

- **Pattern**: Autosomal recessive (AR)
- **Penetrance**: Complete for biallelic null mutations; variable for hypomorphic alleles
- **Expressivity**: Variable; correlates with residual ATM kinase activity
- **Genetic anticipation**: Not observed (not a repeat expansion disorder)
- **Consanguinity**: Important factor, particularly in Central Asian and Middle Eastern communities ([PMID: 41451872](https://pubmed.ncbi.nlm.nih.gov/41451872/))

### Founder Effects

Population-specific founder mutations documented in:
- North Caucasus ethnic groups (BRCA1/ATM; [PMID: 37851290](https://pubmed.ncbi.nlm.nih.gov/37851290/))
- Kyrgyz population (c.5932G>A; [PMID: 41451872](https://pubmed.ncbi.nlm.nih.gov/41451872/))
- Ashkenazi Jewish, Amish/Mennonite, Japanese, and other populations

### Population Demographics

- **Sex ratio**: Approximately 1:1 (autosomal recessive, no sex predilection)
- **Ethnic distribution**: All ethnicities affected; higher in consanguineous populations
- **Geographic distribution**: Worldwide; registries in Europe, North America, and other regions

---

## 10. Diagnostics

### Clinical Tests

| Test | Finding | Utility |
|------|---------|---------|
| Serum AFP | Elevated (>10 ng/mL, often >50) | >95% sensitive screening test |
| Immunoglobulins | Low IgA, IgG subclasses; variable IgM | Immune function assessment |
| Lymphocyte subsets | T cell lymphopenia, ↓naive/memory B cells | Immune profiling ([PMID: 33052516](https://pubmed.ncbi.nlm.nih.gov/33052516/)) |
| ATM protein (Western blot) | Absent or reduced | Diagnostic confirmation |
| Radiosensitivity assay | Increased sensitivity | Functional confirmation |
| Brain MRI | Cerebellar atrophy | Non-ionizing; progressive finding |
| Lung US/MRI | Bronchiectasis, consolidations | Preferred over CT ([PMID: 36186632](https://pubmed.ncbi.nlm.nih.gov/36186632/)) |
| Spirometry | Progressive restrictive/obstructive pattern | Monitoring ([PMID: 26033643](https://pubmed.ncbi.nlm.nih.gov/26033643/)) |
| Karyotype | 7;14 translocations | Diagnostic support |

### Genetic Testing

The recommended approach is:
1. Clinical suspicion based on progressive ataxia + elevated AFP ± immunodeficiency
2. ATM gene sequencing (Sanger or NGS) as confirmatory test
3. MLPA or array CGH for large deletions/duplications
4. WES/WGS for atypical presentations

"Next-generation sequencing (NGS) revealed two novel heterozygous mutations in the ATM gene... demonstrating the utility of targeted NGS in the detection of copy number variation" ([PMID: 30888062](https://pubmed.ncbi.nlm.nih.gov/30888062/)).

### Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|----------------------|
| Ataxia-telangiectasia-like disorder (ATLD) | MRE11 mutations; similar but milder; no telangiectasia |
| Nijmegen breakage syndrome (NBS) | NBS1/NBN mutations; microcephaly; no ataxia |
| Ataxia with oculomotor apraxia types 1/2 | No telangiectasia or immunodeficiency; AOA2 has elevated AFP |
| Friedreich ataxia | FXN GAA expansion; cardiomyopathy; sensory neuropathy |
| Cerebral palsy | Non-progressive; may initially mimic early A-T |

### Screening

- **Newborn screening**: Not standard; TREC-based SCID screening may incidentally identify severe cases
- **Carrier screening**: ATM included in expanded carrier screening panels
- **Prenatal testing**: Available for families with known mutations (CVS, amniocentesis)
- **PGD**: Available for carrier couples

---

## 11. Outcome/Prognosis

### Survival and Mortality

The French cohort of 240 A-T patients demonstrated: "the Kaplan-Meier 20-year survival rate was 53.4%; the prognosis for these patients has not changed since 1954. Life expectancy was lower among patients with mutations in ATM that caused total loss of expression or function of the gene product (null mutations) compared with that seen in patients with hypomorphic mutations because of earlier onset of cancer (mainly hematologic malignancies). Cancer (hazard ratio, 2.7; 95% CI, 1.6-4.5) and respiratory tract infections (hazard ratio, 2.3; 95% CI, 1.4-3.8) were independently associated with mortality" ([PMID: 21665257](https://pubmed.ncbi.nlm.nih.gov/21665257/)).

The Dutch cohort confirmed: "classical AT patients had a shorter survival than variant patients (HR 5.9, 95%CI 2.0-17.7), especially once a malignancy was diagnosed (HR 2.5, 95%CI 1.1-5.5, compared to classical AT patients without malignancy)" ([PMID: 28126470](https://pubmed.ncbi.nlm.nih.gov/28126470/)).

### Genotype-Stratified Mortality

| Cause of Death | Overall HR | Null Mutations HR | Hypomorphic Mutations HR |
|---------------|-----------|-------------------|-------------------------|
| Cancer | 2.7 (95% CI 1.6–4.5) | 5.8 (95% CI 2.9–11.6) | — |
| Respiratory infections | 2.3 (95% CI 1.4–3.8) | — | 4.1 (95% CI 1.8–9.1) |

### Prognostic Factors

| Factor | Impact |
|--------|--------|
| ATM genotype (null vs. hypomorphic) | Most important prognostic factor |
| Residual ATM kinase activity | Higher activity → milder disease, longer survival |
| Hyper-IgM phenotype | Significantly worsens prognosis ([PMID: 28126470](https://pubmed.ncbi.nlm.nih.gov/28126470/)) |
| Baseline FVC | Lower FVC predicts worse respiratory outcome |
| Cancer development | Once diagnosed, survival significantly shortened |

---

## 12. Treatment

### Pharmacotherapy

There is currently **no curative pharmacotherapy** for A-T. Treatment is primarily supportive and multidisciplinary.

| Treatment | MAXO Term | Purpose |
|-----------|-----------|---------|
| Immunoglobulin replacement (IVIG/SCIG) | MAXO:0001298 | Immunodeficiency management |
| Prophylactic antibiotics | MAXO:0000747 | Infection prevention |
| Bronchodilators | MAXO:0000165 | Airway management |
| Corticosteroids | MAXO:0000609 | Neurological improvement (transient) |

### Advanced Therapeutics

**Triheptanoin** (Phase 2a/b trial, 31 participants): An anaplerotic medium-chain triglyceride targeting mitochondrial dysfunction. Results showed significant improvements at maximum dose vs. placebo ([PMID: 40616902](https://pubmed.ncbi.nlm.nih.gov/40616902/)):
- Nasal cell death: MD = −9.7% (95% CI −16.0, −4.6)
- SARA kinetic function: MD = −5.8 (95% CI −10.4, −1.2)
- ICARS gait: MD = −0.5 (95% CI −0.9, −0.1)
- Speech intelligibility: MD = −12.8 (95% CI −21.2, −4.3)
- Swallowing safety: MD = −0.9 (95% CI −1.6, −0.3)

**Intra-erythrocyte dexamethasone** (ATTeST Phase 3 trial): "Corticosteroids can improve neurological functioning in patients with the disorder but adrenal suppression and symptom recurrence on treatment discontinuation has limited their use, prompting the development of novel steroid delivery systems." Multicentre, randomised, double-blind, placebo-controlled at 22 centres in 12 countries ([PMID: 39152028](https://pubmed.ncbi.nlm.nih.gov/39152028/)).

**Antioxidant therapy**: CTMIO "dramatically delays the onset of thymic lymphomas in Atm(−/−) mice" and "corrects neurobehavioral deficits in these mice and reduces oxidative damage to Purkinje cells" ([PMID: 16934683](https://pubmed.ncbi.nlm.nih.gov/16934683/)).

**NAD+ supplementation**: Ameliorates senescence and mitochondrial dysfunction in ATM-deficient cells through STING pathway modulation ([PMID: 33734555](https://pubmed.ncbi.nlm.nih.gov/33734555/)).

**Cell therapy**: Adipose-derived MSCs explored for pulmonary tissue regeneration ([PMID: 32531978](https://pubmed.ncbi.nlm.nih.gov/32531978/)).

### Supportive and Rehabilitative Care

| Intervention | MAXO Term | Details |
|-------------|-----------|---------|
| Physical therapy | MAXO:0000487 | Maintain mobility, prevent contractures |
| Occupational therapy | MAXO:0000536 | Adaptive equipment, independence |
| Speech therapy | MAXO:0000930 | Dysphagia management, communication aids |
| PEG tube feeding | MAXO:0001001 | From age 8 proactively ([PMID: 27573920](https://pubmed.ncbi.nlm.nih.gov/27573920/)) |
| Chest physiotherapy | MAXO:0000168 | Airway clearance |

### Cancer Treatment Considerations

- **Radiation therapy**: Must be avoided or drastically reduced; standard doses can be fatal
- **Chemotherapy**: Modified protocols; radiomimetic agents require dose modification
- **PARP inhibitors**: Show synthetic lethality with ATM loss in cancer cells, relevant for somatic ATM-mutant tumors ([PMID: 38807759](https://pubmed.ncbi.nlm.nih.gov/38807759/))

---

## 13. Prevention

### Primary Prevention

- **Genetic counseling** (MAXO:0000079): Essential for families with affected children and consanguineous populations
- **Carrier screening**: ATM included in expanded carrier screening panels
- **Prenatal diagnosis**: CVS or amniocentesis available when familial mutations known
- **Preimplantation genetic diagnosis (PGD)**: Available for carrier couples

### Secondary Prevention

- **Elevated AFP + ataxia** → immediate ATM genetic testing; "early ATM genetic testing should be considered for those patients with predominant dystonia, despite without accompanying ataxia or telangiectasia" ([PMID: 37009283](https://pubmed.ncbi.nlm.nih.gov/37009283/))
- **TREC-based newborn screening**: May incidentally identify severe cases
- **Cancer surveillance**: Regular clinical assessment; avoid ionizing radiation; use US/MRI ([PMID: 39264246](https://pubmed.ncbi.nlm.nih.gov/39264246/))

### Tertiary Prevention

| Complication | Prevention Strategy |
|-------------|-------------------|
| Respiratory infections | IVIG, prophylactic antibiotics, vaccination (inactivated only) |
| Nutritional failure | Proactive PEG from age 8 |
| Cancer | Enhanced surveillance; minimize radiation |
| Radiation injury | Strict avoidance; medical alert identification |

### ATM Heterozygote Cancer Screening

"ATM GPV heterozygotes should generally be offered enhanced breast surveillance according to their personalized risk estimate and country-specific guidelines and, generally, risk-reducing mastectomy is not recommended. Prostate cancer surveillance should be considered. Pancreatic cancer surveillance should be considered based on assessment of family history" ([PMID: 39636577](https://pubmed.ncbi.nlm.nih.gov/39636577/)).

---

## 14. Other Species / Natural Disease

### Orthologous Genes

| Species | Gene | NCBI Gene ID | Notes |
|---------|------|-------------|-------|
| *Mus musculus* (mouse) | Atm | 11920 | Knockout models available |
| *Rattus norvegicus* (rat) | Atm | 300711 | Superior neurological model |
| *Danio rerio* (zebrafish) | atm | 403065 | Developmental studies |
| *Drosophila melanogaster* | tefu | 42953 | ATM ortholog |
| *Saccharomyces cerevisiae* | TEL1 | 854225 | Yeast ATM ortholog |
| *Caenorhabditis elegans* | atm-1 | 172394 | Genetic studies |

### Comparative Biology

ATM function is evolutionarily ancient and conserved from yeast to humans. In *S. cerevisiae*, "the Tel1 kinase (ortholog of human ATM) is activated at DNA double-strand breaks (DSBs) and short telomeres" and controls "telomere maintenance, suppression of chromosomal rearrangements, activation of cell cycle checkpoints, and repair of DSBs" ([PMID: 39826692](https://pubmed.ncbi.nlm.nih.gov/39826692/)). Novel phosphoproteomic analysis revealed a D/E-S/T motif unique to Tel1 signaling, providing insights into specialized ATM functions.

A-T has not been widely documented as a naturally occurring disease in companion animals. The disease is not zoonotic.

---

## 15. Model Organisms

### Mouse Models (Atm−/−)

- **Types**: Conventional knockouts (multiple alleles), conditional knockouts
- **Phenotype recapitulation**:
  - ✅ Thymic lymphomas (100% penetrance by ~4–6 months)
  - ✅ Immunodeficiency (T/B cell defects, CSR impairment)
  - ✅ Radiosensitivity, growth retardation, infertility, chromosomal instability
  - ❌ **Does NOT recapitulate progressive cerebellar degeneration** (major limitation)
  - ⚠️ Subtle neurobehavioral deficits and oxidative damage to Purkinje cells detectable ([PMID: 10449794](https://pubmed.ncbi.nlm.nih.gov/10449794/))
- **Antioxidant studies**: CTMIO "dramatically delays the onset of thymic lymphomas" and "corrects neurobehavioral deficits" ([PMID: 16934683](https://pubmed.ncbi.nlm.nih.gov/16934683/))
- **Modifier studies**: Hus1 impairment + Atm loss → synthetic lethality or synergistic genomic instability ([PMID: 22575700](https://pubmed.ncbi.nlm.nih.gov/22575700/)); SOD1 overexpression exacerbates phenotype ([PMID: 11285218](https://pubmed.ncbi.nlm.nih.gov/11285218/))

### Rat Models

- **Superior neurological model**: "Loss of Atm in neurons and glia leads to accumulation of cytosolic DNA, increased cytokine production and constitutive activation of microglia consistent with a neuroinflammatory phenotype. Rats lacking ATM had significant loss of motor neurons and microgliosis in the spinal cord, consistent with onset of paralysis" ([PMID: 28007901](https://pubmed.ncbi.nlm.nih.gov/28007901/))
- ✅ Neuroinflammation, motor neuron loss, cytosolic DNA accumulation, paralysis

### Cellular Models

- **iPSC-derived neurons**: Recapitulate DSB repair defects, repressed ATM substrate phosphorylation, Top1-cc accumulation ([PMID: 25032865](https://pubmed.ncbi.nlm.nih.gov/25032865/))
- **Brain-derived and iPSC-derived neural stem cells**: Model neurodegeneration ([PMID: 23598976](https://pubmed.ncbi.nlm.nih.gov/23598976/))
- **Patient fibroblasts**: Show mitochondrial dysfunction, senescence, SASP ([PMID: 33734555](https://pubmed.ncbi.nlm.nih.gov/33734555/))

### Yeast (S. cerevisiae)

- **TEL1** ortholog: Telomere maintenance, DSB signaling; novel D/E-S/T motif identified ([PMID: 39826692](https://pubmed.ncbi.nlm.nih.gov/39826692/))

### Model Limitations

| Model | Key Limitation |
|-------|---------------|
| Atm−/− mouse | No cerebellar degeneration |
| Atm−/− rat | Spinal cord rather than cerebellar pathology |
| iPSC neurons | In vitro; lacks tissue context |
| Yeast (TEL1) | No multicellular phenotypes |

---

## Key Findings — Detailed Evidence

### Finding 1: Biallelic ATM Mutations Cause A-T with Genotype-Phenotype Correlation

The ATM gene on chromosome 11q22.3 encodes a 3,056-amino-acid serine/threonine kinase that is the master regulator of the DNA double-strand break response. Biallelic loss-of-function mutations cause autosomal recessive A-T. A landmark genotype-phenotype study of 51 patients demonstrated that patients without ATM kinase activity display classical A-T, while "residual kinase activity correlated with a milder and essentially different neurological phenotype, absence of telangiectasia, normal endocrine and pulmonary function, normal immunoglobulins, significantly lower X-ray hypersensitivity in lymphocytes, and extended lifespan" ([PMID: 22213089](https://pubmed.ncbi.nlm.nih.gov/22213089/)). This genotype-phenotype correlation—centered on residual ATM kinase activity—is the single most important prognostic factor and has transformed our understanding of A-T as a disease continuum rather than a single entity. Prevalence is estimated at 1:40,000–1:100,000 live births, with a cancer risk 56-fold increased (SIR = 56; [PMID: 34597127](https://pubmed.ncbi.nlm.nih.gov/34597127/)).

### Finding 2: Cerebellar Neurodegeneration Driven by DNA Damage and cGAS-STING Neuroinflammation

The most debilitating feature of A-T—progressive cerebellar degeneration—results from a cascade beginning with defective DSB repair and culminating in neuroinflammation. ATM-deficient neurons show "defective repair of DNA double-strand breaks (DSBs) and repressed phosphorylation of ATM substrates" and "abnormal accumulation of topoisomerase 1-DNA covalent complexes" ([PMID: 25032865](https://pubmed.ncbi.nlm.nih.gov/25032865/)). Cerebellar Purkinje cells are selectively vulnerable to oxidative damage ([PMID: 10449794](https://pubmed.ncbi.nlm.nih.gov/10449794/)). Unrepaired DNA leads to cytosolic DNA accumulation that activates the cGAS-STING innate immune pathway: "Loss of Atm in neurons and glia leads to accumulation of cytosolic DNA, increased cytokine production and constitutive activation of microglia" ([PMID: 28007901](https://pubmed.ncbi.nlm.nih.gov/28007901/)). The nitroxide antioxidant CTMIO "corrects neurobehavioral deficits in these mice and reduces oxidative damage to Purkinje cells" ([PMID: 16934683](https://pubmed.ncbi.nlm.nih.gov/16934683/)), confirming oxidative stress as a tractable therapeutic target.

### Finding 3: Survival Determined by Cancer and Respiratory Infections with Genotype Stratification

In the French cohort of 240 A-T patients, "the Kaplan-Meier 20-year survival rate was 53.4%; the prognosis for these patients has not changed since 1954." Cancer (HR 2.7, 95% CI 1.6–4.5) and respiratory tract infections (HR 2.3, 95% CI 1.4–3.8) were independently associated with mortality. For null mutations, cancer is the major risk factor (HR 5.8, 95% CI 2.9–11.6); for hypomorphic mutations, respiratory infections lead (HR 4.1, 95% CI 1.8–9.1) ([PMID: 21665257](https://pubmed.ncbi.nlm.nih.gov/21665257/)). The Dutch cohort confirmed that "classical AT patients had a shorter survival than variant patients (HR 5.9, 95% CI 2.0–17.7)" ([PMID: 28126470](https://pubmed.ncbi.nlm.nih.gov/28126470/)).

### Finding 4: Immunodeficiency from Defective Class-Switch Recombination

The immunodeficiency in A-T reflects fundamental defects in lymphocyte development and function. "Immunoglobulin deficiency in AT is caused by disturbed development of class-switched memory B cells. ATM deficiency affects both germinal center reaction and choice of DNA-repair pathway in class switching" ([PMID: 38280573](https://pubmed.ncbi.nlm.nih.gov/38280573/)). Comprehensive analysis revealed "a broad spectrum of cellular and humoral deficiencies" ([PMID: 33052516](https://pubmed.ncbi.nlm.nih.gov/33052516/)). The hyper-IgM phenotype is particularly significant as a poor prognostic marker, associated with chronic EBV expansion and liver failure ([PMID: 36340711](https://pubmed.ncbi.nlm.nih.gov/36340711/)).

### Finding 5: Triheptanoin and Intra-Erythrocyte Dexamethasone Show Clinical Promise

Two therapeutic approaches have advanced to clinical trials. Triheptanoin showed significant improvements in a Phase 2a/b trial across multiple endpoints (nasal cell death MD = −9.7%, SARA kinetic MD = −5.8, speech intelligibility MD = −12.8), targeting mitochondrial dysfunction as "A-T cells demonstrate defective endoplasmic reticulum-mitochondrial connectivity disrupting calcium homoeostasis and mitochondrial fusion, which are corrected in vitro by the triheptanoin metabolite, heptanoate" ([PMID: 40616902](https://pubmed.ncbi.nlm.nih.gov/40616902/)). The ATTeST Phase 3 trial of intra-erythrocyte dexamethasone leverages corticosteroid neurological benefits while minimizing systemic effects through encapsulated delivery ([PMID: 39152028](https://pubmed.ncbi.nlm.nih.gov/39152028/)).

---

## Evidence Base

### Landmark Papers

| PMID | Key Contribution |
|------|-----------------|
| [9735376](https://pubmed.ncbi.nlm.nih.gov/9735376/) | Foundational ATM gene-to-function review |
| [22213089](https://pubmed.ncbi.nlm.nih.gov/22213089/) | Definitive genotype-phenotype correlation (n=51) |
| [21665257](https://pubmed.ncbi.nlm.nih.gov/21665257/) | French cohort survival analysis (n=240) |
| [28126470](https://pubmed.ncbi.nlm.nih.gov/28126470/) | Dutch cohort survival and prognostic factors |
| [28007901](https://pubmed.ncbi.nlm.nih.gov/28007901/) | Rat model: cGAS-STING neuroinflammation |
| [10449794](https://pubmed.ncbi.nlm.nih.gov/10449794/) | Oxidative damage targeting Purkinje cells |
| [34597127](https://pubmed.ncbi.nlm.nih.gov/34597127/) | Population-based cancer risk (SIR=56, German registry) |
| [38280573](https://pubmed.ncbi.nlm.nih.gov/38280573/) | Mechanism of immunoglobulin deficiency via CSR |
| [40616902](https://pubmed.ncbi.nlm.nih.gov/40616902/) | Triheptanoin Phase 2a/b trial results |
| [39152028](https://pubmed.ncbi.nlm.nih.gov/39152028/) | ATTeST Phase 3 trial of intra-erythrocyte dexamethasone |
| [30685876](https://pubmed.ncbi.nlm.nih.gov/30685876/) | Comprehensive A-T clinical and molecular review |
| [25032865](https://pubmed.ncbi.nlm.nih.gov/25032865/) | iPSC-derived A-T neuron functional defects |
| [16934683](https://pubmed.ncbi.nlm.nih.gov/16934683/) | Antioxidant therapy in Atm−/− mice |
| [33734555](https://pubmed.ncbi.nlm.nih.gov/33734555/) | NAD+ supplementation for mitochondrial dysfunction |
| [39636577](https://pubmed.ncbi.nlm.nih.gov/39636577/) | ACMG guidelines for ATM heterozygote management |

### Evidence Types

The evidence base comprises 78 papers spanning:
- **Human clinical data**: Cohort studies from France (n=240; [PMID: 21665257](https://pubmed.ncbi.nlm.nih.gov/21665257/)), Netherlands ([PMID: 28126470](https://pubmed.ncbi.nlm.nih.gov/28126470/)), Germany (n=160; [PMID: 34597127](https://pubmed.ncbi.nlm.nih.gov/34597127/)), and multinational clinical trials
- **Model organism data**: Mouse ([PMID: 10449794](https://pubmed.ncbi.nlm.nih.gov/10449794/); [PMID: 16934683](https://pubmed.ncbi.nlm.nih.gov/16934683/)), rat ([PMID: 28007901](https://pubmed.ncbi.nlm.nih.gov/28007901/)), yeast ([PMID: 39826692](https://pubmed.ncbi.nlm.nih.gov/39826692/))
- **In vitro data**: iPSC-derived neurons ([PMID: 25032865](https://pubmed.ncbi.nlm.nih.gov/25032865/)), patient fibroblasts ([PMID: 33734555](https://pubmed.ncbi.nlm.nih.gov/33734555/))
- **Clinical trials**: Triheptanoin Phase 2a/b ([PMID: 40616902](https://pubmed.ncbi.nlm.nih.gov/40616902/)), ATTeST Phase 3 ([PMID: 39152028](https://pubmed.ncbi.nlm.nih.gov/39152028/))

---

## Ontology Term Summary

### HPO Terms (Phenotype)
HP:0001251 (Cerebellar ataxia), HP:0000657 (Oculomotor apraxia), HP:0000989 (Telangiectasia), HP:0000565 (Conjunctival telangiectasia), HP:0002721 (Immunodeficiency), HP:0002664 (Neoplasm), HP:0006254 (Elevated AFP), HP:0200144 (Radiosensitivity), HP:0003220 (Chromosomal instability), HP:0001260 (Dysarthria), HP:0001332 (Dystonia), HP:0001266 (Choreoathetosis), HP:0009830 (Peripheral neuropathy), HP:0001888 (Lymphopenia), HP:0004313 (↓IgA), HP:0004315 (↓IgG), HP:0002790 (Hyper-IgM), HP:0002205 (Recurrent respiratory infections), HP:0002110 (Bronchiectasis), HP:0001510 (Growth delay), HP:0000855 (Insulin resistance), HP:0000135 (Hypogonadism), HP:0007495 (Premature aging)

### GO Terms (Biological Process)
GO:0006302 (DSB repair), GO:0006974 (DNA damage response), GO:0000077 (DNA damage checkpoint), GO:0006915 (Apoptosis), GO:0033151 (V(D)J recombination), GO:0045087 (Innate immune response), GO:0006979 (Oxidative stress response), GO:0000723 (Telomere maintenance)

### GO Terms (Cellular Component)
GO:0005634 (Nucleus), GO:0005739 (Mitochondrion), GO:0005783 (ER), GO:0005737 (Cytoplasm), GO:0000785 (Chromatin)

### CL Terms (Cell Types)
CL:0000121 (Purkinje cell), CL:0000084 (T cell), CL:0000236 (B cell), CL:0000129 (Microglia), CL:0000100 (Motor neuron), CL:0000788 (Naive B cell), CL:0000972 (Class-switched memory B cell), CL:0002368 (Respiratory epithelial cell), CL:0000115 (Endothelial cell)

### UBERON Terms (Anatomy)
UBERON:0002037 (Cerebellum), UBERON:0002370 (Thymus), UBERON:0002048 (Lung), UBERON:0001811 (Conjunctiva), UBERON:0002107 (Liver), UBERON:0002240 (Spinal cord), UBERON:0002371 (Bone marrow), UBERON:0000991 (Gonad)

### MAXO Terms (Treatment)
MAXO:0001298 (Immunoglobulin replacement), MAXO:0000747 (Antimicrobial therapy), MAXO:0000079 (Genetic counseling), MAXO:0001001 (Gastrostomy), MAXO:0000487 (Physical therapy), MAXO:0000536 (Occupational therapy), MAXO:0000930 (Speech therapy)

### MONDO Term
MONDO:0008840 (Ataxia-telangiectasia)

---

## Limitations and Knowledge Gaps

1. **Neurodegeneration mechanism**: The precise reason why cerebellar Purkinje cells are selectively vulnerable to ATM loss remains incompletely understood. The relative contributions of DSB repair failure, oxidative stress, mitochondrial dysfunction, and neuroinflammation are still debated ([PMID: 32871349](https://pubmed.ncbi.nlm.nih.gov/32871349/)).

2. **Mouse model limitations**: Atm knockout mice do not develop progressive cerebellar ataxia or Purkinje cell loss, making preclinical neurological studies challenging. The rat model is superior but still shows spinal cord rather than cerebellar pathology ([PMID: 28007901](https://pubmed.ncbi.nlm.nih.gov/28007901/); [PMID: 23598976](https://pubmed.ncbi.nlm.nih.gov/23598976/)).

3. **Stagnant prognosis**: Despite decades of study, "the prognosis for these patients has not changed since 1954" ([PMID: 21665257](https://pubmed.ncbi.nlm.nih.gov/21665257/)), highlighting the urgent need for disease-modifying therapies.

4. **Limited trial data**: Clinical trials are constrained by small sample sizes inherent to rare diseases (triheptanoin trial: n=31). Long-term efficacy data are lacking for all emerging therapies.

5. **Variant A-T underdiagnosis**: Atypical presentations (dystonia-predominant, adult-onset) are likely underdiagnosed; the full phenotypic spectrum of hypomorphic ATM mutations is not yet defined ([PMID: 37009283](https://pubmed.ncbi.nlm.nih.gov/37009283/)).

6. **Heterozygote cancer risk**: Precise penetrance estimates for different ATM variant types and cancer types remain uncertain ([PMID: 39636577](https://pubmed.ncbi.nlm.nih.gov/39636577/)).

7. **Multi-omic characterization**: Comprehensive epigenomic, proteomic, and metabolomic profiling of A-T tissues—particularly at single-cell resolution—is still limited.

8. **Pulmonary pathogenesis**: The etiology of progressive pulmonary deterioration beyond immunodeficiency is unclear; direct ATM roles in respiratory epithelium require investigation ([PMID: 17524020](https://pubmed.ncbi.nlm.nih.gov/17524020/)).

---

## Proposed Follow-up Experiments/Actions

1. **Single-cell transcriptomics of A-T cerebellum**: Profile Purkinje cells, granule cells, and microglia from A-T patient post-mortem tissue to define cell-type-specific transcriptional changes and validate the cGAS-STING neuroinflammation axis in human tissue.

2. **STING inhibitor trials**: Given demonstrated cGAS-STING involvement in neuroinflammation ([PMID: 28007901](https://pubmed.ncbi.nlm.nih.gov/28007901/)), evaluate STING pathway inhibitors in the ATM-deficient rat model.

3. **NAD+ supplementation clinical trial**: Translate preclinical findings that NAD+ boosting ameliorates senescence and mitochondrial dysfunction ([PMID: 33734555](https://pubmed.ncbi.nlm.nih.gov/33734555/)) into a clinical trial.

4. **Long-term triheptanoin follow-up**: Extend the Phase 2a/b trial to assess disease progression rate modification and survival benefit.

5. **Global genotype-phenotype registry**: Establish a registry linking detailed ATM genotype (including residual kinase activity) with longitudinal clinical outcomes.

6. **Biomarker development**: Develop non-invasive biomarkers (neurofilament light chain, cytokine panels, circulating cytosolic DNA) for disease monitoring and clinical trial design.

7. **Gene therapy approaches**: Investigate dual-AAV, lentiviral, or base editing strategies for ATM restoration in neural progenitors and HSCs.

8. **ATM heterozygote prospective cohort**: Establish prospective surveillance to refine cancer penetrance estimates.

---

*Report generated: 2026-05-05*
*Data sources: OMIM, Orphanet, ClinVar, PubMed, and 78 reviewed publications*
*Evidence quality: High for genetic/molecular mechanisms; moderate for clinical outcomes; emerging for therapeutic interventions*
