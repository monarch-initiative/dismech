---
provider: openscientist
model: openscientist-autonomous
cached: false
end_time: '2026-05-05T23:45:23.079662Z'
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: BRAF V600 Mutant Melanoma
  mondo_id: ''
  category: ''
citation_count: 60
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** BRAF V600 Mutant Melanoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **BRAF V600 Mutant Melanoma** covering all of the
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

# Comprehensive Disease Knowledge Base Report: BRAF V600 Mutant Melanoma

## Summary

**BRAF V600 Mutant Melanoma** is a molecular subtype of cutaneous melanoma defined by activating somatic mutations at codon 600 of the BRAF proto-oncogene (chromosome 7q34), present in approximately 40–50% of all cutaneous melanomas. The dominant variant, BRAF V600E (accounting for ~79% of V600 mutations), produces a constitutively active serine/threonine kinase that hyperactivates the RAS–RAF–MEK–ERK (MAPK) signaling cascade independent of extracellular growth factor stimulation. This results in uncontrolled cell proliferation, evasion of apoptosis, metabolic reprogramming toward aerobic glycolysis (the Warburg effect), angiogenesis, and immune evasion. The discovery of the BRAF V600E mutation in 2002 launched a revolution in precision oncology, culminating in FDA-approved BRAF and MEK inhibitor combinations that achieve objective response rates of ~60–70% and have transformed survival outcomes for metastatic disease.

Clinically, BRAF V600 mutant melanomas preferentially arise in younger patients (median age of diagnosis younger than wild-type melanoma), on intermittently sun-exposed body sites such as the trunk, and are strongly associated with a history of intermittent ultraviolet (UV) radiation exposure including indoor tanning. Despite dramatic initial responses to targeted therapy, acquired resistance develops in the majority of patients within 6–12 months, driven by MAPK pathway reactivation, secondary mutations (e.g., NRAS Q61, MEK1 mutations), alternative pathway activation (PI3K/AKT), and metabolic reprogramming toward oxidative phosphorylation. The integration of immune checkpoint inhibitors (anti-PD-1, anti-CTLA-4) with targeted therapy has further improved outcomes, and modern combination approaches have increased 5-year survival from <15% to approximately 50% in metastatic disease. This report provides a comprehensive, 15-section disease characterization suitable for populating a disease knowledge base entry, with ontology terms, statistical evidence, and primary literature citations.

---

## 1. Disease Information

### Overview

BRAF V600 Mutant Melanoma is a molecularly defined subtype of cutaneous malignant melanoma characterized by somatic gain-of-function mutations at codon 600 of the BRAF gene (7q34). BRAF is a serine/threonine protein kinase in the MAPK/ERK signaling pathway that regulates cell proliferation, differentiation, and survival. The V600E mutation (a thymine-to-adenine transversion resulting in valine-to-glutamic acid substitution) accounts for the vast majority of cases and produces a constitutively active kinase domain that drives oncogenesis independent of upstream RAS activation ([PMID: 39961465](https://pubmed.ncbi.nlm.nih.gov/39961465/)).

As noted by Paluncic et al., "40-50% of all melanoma patients harbour an activating BRAF mutation (mostly BRAF V600E)" ([PMID: 33801689](https://pubmed.ncbi.nlm.nih.gov/33801689/)). Among BRAF V600 mutations, the distribution is: V600E (79%), V600K (12%), V600R (5%), and V600M (4%) ([PMID: 22536370](https://pubmed.ncbi.nlm.nih.gov/22536370/)).

### Key Identifiers

| Identifier | Value |
|---|---|
| **OMIM** | #164757 (Melanoma, cutaneous malignant); BRAF gene: *164757 |
| **ICD-10** | C43 (Malignant melanoma of skin) |
| **ICD-11** | 2D40-2D4Z (Melanoma of skin) |
| **MeSH** | D008545 (Melanoma); C562395 (BRAF gene mutation) |
| **MONDO** | MONDO:0005012 (melanoma) |
| **HGNC** | HGNC:1097 (BRAF) |
| **ClinVar** | Variation ID 376069 (BRAF V600E) |
| **COSMIC** | COSV56056643 (BRAF p.V600E) |

### Synonyms and Alternative Names

- BRAF V600E-mutated melanoma
- BRAF-mutant melanoma
- BRAF V600E/K melanoma
- V600E-positive melanoma
- Melanoma with activating BRAF mutation
- MAPK-driven melanoma (when referring to mechanism)

### Information Sources

This report is derived from aggregated disease-level resources including published clinical trials, genomic databases (COSMIC, ClinVar, TCGA), epidemiological registries (SEER, GLOBOCAN), and primary research literature (PubMed). Individual patient-level data is referenced from landmark clinical trials (COMBI-d, COLUMBUS, IMspire150) and real-world registries (ADMIRE, Dutch Melanoma Treatment Registry).

---

## 2. Etiology

### Disease Causal Factors

BRAF V600 Mutant Melanoma arises through a multi-step oncogenic process involving both genetic and environmental factors:

**Somatic genetic origin:** The BRAF V600E mutation is a somatic (acquired) missense mutation arising in melanocytes. It is not inherited in the germline but occurs during the lifetime of the individual. The mutation results in constitutive activation of the BRAF kinase, which "results in a constitutively active kinase domain, leading to dysregulated downstream signaling independent of extracellular stimuli. This sustained activation promotes cell proliferation, survival, angiogenesis, and hallmark features of the cancer cells" ([PMID: 39961465](https://pubmed.ncbi.nlm.nih.gov/39961465/)).

**UV radiation as initiating factor:** Ultraviolet radiation, particularly UVB (280–320 nm), is the primary environmental mutagen. UV radiation induces DNA damage in melanocytes, including the characteristic thymine dimer mutations. The BRAF V600E mutation itself (T1799A) is not a classic UV signature mutation (C>T at dipyrimidine sites), suggesting that UV may act indirectly through mutagenic stress, oxidative damage, or proliferative stimulation rather than direct photoproduct formation ([PMID: 27221301](https://pubmed.ncbi.nlm.nih.gov/27221301/)).

### Risk Factors

#### Genetic Risk Factors

- **BRAF V600E somatic mutation** (driver): Present in 40–50% of cutaneous melanomas; constitutive MAPK activation
- **CDKN2A (p16INK4A) germline mutations**: High-penetrance melanoma susceptibility gene; loss of cell cycle control at G1/S checkpoint
- **CDK4 mutations**: Rare high-penetrance susceptibility gene
- **MC1R variants**: Red hair color variants (R151C, R160W, D294H) associated with fair skin, poor tanning, and increased melanoma risk
- **PTEN loss**: Frequently co-occurs with BRAF V600E (seen in ~40% of BRAF-mutant melanomas); synergistic oncogenic effect through PI3K/AKT pathway activation
- **TERT promoter mutations**: Common co-occurring mutations promoting telomere maintenance
- **Co-occurring NRAS mutations**: Mutually exclusive with BRAF V600E in primary tumors but may arise as resistance mutations

#### Environmental Risk Factors

Associations with BRAF mutation were characterized by Colombino et al.: "Associations with BRAF mutation were as follows: male gender [odds ratio (OR) = 2.4], younger age (OR = 2.7), superficial spreading (OR = 15.6) and nodular melanoma (OR = 9.5), trunk localization (OR = 6.3), and intermittent sun exposure (OR = 4.6)" ([PMID: 25357015](https://pubmed.ncbi.nlm.nih.gov/25357015/)).

- **Intermittent UV exposure**: Strong association (OR = 4.6) vs. chronic sun exposure
- **Indoor tanning**: "BRAF V600E genotype was more prevalent in ever-users than in nonusers (42.9% vs 28.3%, two-sided P = .04) and higher in ever-users who initiated indoor tanning prior to age 25 years compared with age 25 years or older (62.2% vs 31.1%, two-sided P = .003)" ([PMID: 30923800](https://pubmed.ncbi.nlm.nih.gov/30923800/))
- **Sunburn history**: Blistering sunburns associated with increased absolute mutation incidence (1.67 vs 1.16 mutations/patient, P = 0.028) ([PMID: 32445930](https://pubmed.ncbi.nlm.nih.gov/32445930/))
- **Fair skin phenotype**: Fitzpatrick skin types I and II
- **High nevus count**: Multiple dysplastic nevi as a risk factor
- **Male sex**: OR = 2.4 for BRAF mutation
- **Younger age**: OR = 2.7 for BRAF mutation (median age younger than BRAF wild-type)
- **Residence in high-UV areas**: OR = 5.54 (95% CI 1.19–25.8) for residing in states with UV index ≥7 vs ≤5 at age 30 ([PMID: 25048604](https://pubmed.ncbi.nlm.nih.gov/25048604/))

#### Possible Non-Traditional Risk Factors

- **Hexavalent chromium exposure**: Epidemiological data suggest heavy metal exposure may contribute; UV accounts for only 40–50% of attributable melanoma risk ([PMID: 21253789](https://pubmed.ncbi.nlm.nih.gov/21253789/))

### Protective Factors

#### Genetic Protective Factors
- **MC1R wild-type**: Associated with darker skin pigmentation and improved UV protection
- **Certain HLA genotypes**: Associated with improved immune surveillance
- **High MITF expression**: May maintain melanocyte differentiation programs

#### Environmental Protective Factors
- **Sun protection behaviors**: Use of sunscreen (high SPF), protective clothing, avoidance of midday sun
- **Avoidance of indoor tanning**, especially before age 25
- **Regular skin self-examination and professional screening**
- **Dietary factors**: Some evidence for vitamin D, antioxidants, though data are inconclusive

### Gene–Environment Interactions

The BRAF V600E mutation appears to arise preferentially in the context of intermittent rather than chronic UV exposure, explaining its association with trunk melanomas (usually covered, intermittently exposed) in younger patients. The B-RafV600E mutation was detected in 85% of trunk melanomas in indoor workers versus 47% in outdoor workers (P = 0.03), indicating that "the B-RafV600E mutation detected in melanoma is not associated with a chronic exposure to the sun" but rather with recreational/intermittent exposure ([PMID: 24424406](https://pubmed.ncbi.nlm.nih.gov/24424406/)). MC1R variants may further modify risk by impairing DNA repair capacity in the setting of UV exposure, creating a synergistic effect.

---

## 3. Phenotypes

### Clinical Signs and Symptoms

| Phenotype | HPO Term | Type | Onset | Severity | Frequency | Progression |
|---|---|---|---|---|---|---|
| Cutaneous melanocytic lesion (primary tumor) | HP:0012056 (Cutaneous melanoma) | Physical sign | Adult (median 50s) | Variable | 100% | Progressive if untreated |
| Asymmetric pigmented lesion | HP:0200040 (Irregular hyperpigmentation) | Physical sign | Adult | Mild–moderate | Very frequent | Progressive |
| Ulceration of primary lesion | HP:0200041 (Skin ulcer) | Physical sign | Later stages | Moderate–severe | ~40–50% | Progressive |
| Lymphadenopathy (regional metastasis) | HP:0002716 (Lymphadenopathy) | Clinical sign | Stage III | Moderate–severe | Variable | Progressive |
| Elevated serum LDH | HP:0025435 (Increased circulating lactate dehydrogenase) | Laboratory abnormality | Advanced disease | Indicator of high tumor burden | ~37.5% at presentation | Progressive |
| Fatigue | HP:0012378 (Fatigue) | Symptom | Advanced disease | Moderate–severe | Frequent | Progressive |
| Brain metastases (neurological symptoms) | HP:0002888 (Brain neoplasm) | Clinical sign | Stage IV | Severe | ~32% of advanced cases | Progressive |
| Hepatomegaly/liver metastases | HP:0002240 (Hepatomegaly) | Clinical sign | Stage IV | Severe | Common | Progressive |
| Pulmonary symptoms (lung metastases) | HP:0002094 (Dyspnea) | Symptom | Stage IV | Moderate–severe | Common | Progressive |

### Phenotype Characteristics Specific to BRAF V600 Mutant Melanoma

- **Age of onset**: Younger than BRAF wild-type melanomas (OR = 2.7 for younger age) ([PMID: 25357015](https://pubmed.ncbi.nlm.nih.gov/25357015/))
- **Histological subtypes**: Strongly associated with superficial spreading melanoma (OR = 15.6) and nodular melanoma (OR = 9.5)
- **Anatomical predilection**: Trunk localization (OR = 6.3); less common on chronically sun-damaged skin (head/neck)
- **Mitotic activity**: BRAF-mutated melanomas tend to be more mitotically active ([PMID: 28424234](https://pubmed.ncbi.nlm.nih.gov/28424234/))

### Quality of Life Impact

Advanced BRAF V600 mutant melanoma significantly impacts quality of life through:
- Physical symptoms of metastatic disease (pain, fatigue, neurological deficits from brain metastases)
- Psychological distress from cancer diagnosis and treatment
- Treatment-related side effects (pyrexia, arthralgia, skin toxicities from targeted therapy; immune-related adverse events from immunotherapy)
- Functional impairment from disease complications

---

## 4. Genetic/Molecular Information

### Causal Gene

**BRAF (B-Raf Proto-Oncogene, Serine/Threonine Kinase)**
- **HGNC ID**: HGNC:1097
- **NCBI Gene ID**: 673
- **OMIM**: *164757
- **Chromosomal location**: 7q34
- **UniProt**: P15056
- **Protein**: 766 amino acid serine/threonine kinase

### Pathogenic Variants

| Variant | HGVS Notation | Type | Frequency Among V600 | Allele Frequency (gnomAD) | Origin | Functional Consequence |
|---|---|---|---|---|---|---|
| **V600E** | c.1799T>A (p.Val600Glu) | Missense | ~79% | Somatic (not in germline databases) | Somatic | Gain of function; ~500-fold kinase activation |
| **V600K** | c.1798_1799delGTinsAA (p.Val600Lys) | Dinucleotide substitution | ~12% | Somatic | Somatic | Gain of function; constitutive kinase activation |
| **V600R** | c.1798_1799delGTinsAG (p.Val600Arg) | Dinucleotide substitution | ~5% | Somatic | Somatic | Gain of function |
| **V600M** | c.1798G>A (p.Val600Met) | Missense | ~4% | Somatic | Somatic | Gain of function |
| **V600D** | c.1799_1800delTGinsAT (p.Val600Asp) | Dinucleotide substitution | Rare | Somatic | Somatic | Gain of function |

Source for variant distribution: "Among BRAF V600 mutations, 79%, 12%, 5%, and 4% were V600E, V600K, V600R, and V600M, respectively" ([PMID: 22536370](https://pubmed.ncbi.nlm.nih.gov/22536370/)).

**Variant classification**: All V600 mutations listed are classified as **pathogenic** (oncogenic driver) in ClinVar and COSMIC.

**Somatic origin**: These mutations are somatic, not germline. They are acquired during the individual's lifetime and are not present in the germline. COSMIC reports BRAF V600E as one of the most frequently mutated positions across all human cancers.

**V600K demographics**: V600K was detected in 23% of men older than 60, compared with 6% in women older than 60 and 2% in both sexes younger than 60 (P < .001), suggesting age and sex-specific patterns ([PMID: 25456393](https://pubmed.ncbi.nlm.nih.gov/25456393/)).

### Modifier Genes and Co-occurring Alterations

- **PTEN (10q23.31)**: Loss-of-function mutations or deletions co-occur in ~40% of BRAF V600E melanomas; activates PI3K/AKT pathway synergistically
- **CDKN2A (9p21.3)**: Homozygous deletion or inactivating mutation; loss of p16INK4A and p14ARF tumor suppressors
- **TP53 (17p13.1)**: Mutations less common in melanoma than other cancers but contribute to genomic instability
- **TERT promoter (5p15.33)**: Activating promoter mutations (C228T, C250T) frequent in BRAF-mutant melanoma
- **APC, CTNNB1**: Occasional Wnt pathway alterations
- **NF1**: Generally mutually exclusive with BRAF V600E but defines a separate molecular subtype

### Epigenetic Information

- **Global DNA hypomethylation**: Common in melanoma progression
- **Promoter hypermethylation**: Silencing of tumor suppressors (RASSF1A, MGMT, DAPK)
- **BRAF V600E suppresses MITF**: Leading to reduced melanocyte differentiation gene expression
- **Histone modifications**: H3K27me3 changes associated with melanoma progression; EZH2 overexpression
- **CpG island methylator phenotype (CIMP)**: Associated with BRAF V600E in colorectal cancer; less well-characterized in melanoma

### Chromosomal Abnormalities

- **Chromosome 7 gain**: Frequently observed (location of BRAF); may increase BRAF dosage
- **Chromosome 10 loss**: Contains PTEN; frequently deleted in BRAF-mutant melanomas
- **9p21 deletion**: Loss of CDKN2A locus
- **6p gain**: Common in melanoma
- **Mutant allele-specific imbalance (MASI)**: BRAF V600E MASI predominantly present in distant organ metastases (79% vs 27% in LN metastases vs 13% in primary tumors, P < .001) ([PMID: 25456393](https://pubmed.ncbi.nlm.nih.gov/25456393/))

---

## 5. Environmental Information

### Environmental Factors

- **Ultraviolet radiation (UVA/UVB)**: The primary environmental carcinogen. UVB (280–320 nm) directly damages DNA; UVA (320–400 nm) induces oxidative damage. "About 95% of ultraviolet A (UVA) and 5% of UVB reach the Earth's surface" ([PMID: 27221301](https://pubmed.ncbi.nlm.nih.gov/27221301/))
- **CHEBI term**: CHEBI:27460 (ultraviolet radiation — as a physical agent)
- **Hexavalent chromium**: Proposed as a co-carcinogen; "UV light exposure accounts for only 40-50% of the attributable risk for cutaneous melanoma" ([PMID: 21253789](https://pubmed.ncbi.nlm.nih.gov/21253789/))

### Lifestyle Factors

- **Indoor tanning**: Strong risk factor; BRAF V600E prevalence of 62.2% in users who started before age 25 ([PMID: 30923800](https://pubmed.ncbi.nlm.nih.gov/30923800/))
- **Intermittent recreational sun exposure**: Stronger association with BRAF mutation than chronic occupational exposure (OR = 4.6) ([PMID: 25357015](https://pubmed.ncbi.nlm.nih.gov/25357015/))
- **Sunburn history**: Particularly childhood/adolescent blistering sunburns

### Infectious Agents

- **Beta-genus HPV**: May accelerate keratinocyte carcinogenesis during BRAF inhibitor therapy. β-HPV-17, HPV-38, HPV-111 were most frequently isolated in BRAFi-associated cutaneous squamous cell carcinomas ([PMID: 25724524](https://pubmed.ncbi.nlm.nih.gov/25724524/)). This is relevant to treatment-related secondary malignancies rather than melanoma etiology itself.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

#### RAS–RAF–MEK–ERK (MAPK) Pathway (Primary)

The central oncogenic pathway in BRAF V600 melanoma. The BRAF V600E mutation produces a constitutively active kinase that signals as a monomer (unlike wild-type BRAF which requires dimerization). This leads to sustained MEK1/2 and ERK1/2 phosphorylation, driving:

1. **Cell proliferation**: Transcriptional activation of cyclin D1, c-Myc, and other cell cycle promoters
2. **Survival**: Suppression of pro-apoptotic BIM, BAD; upregulation of anti-apoptotic MCL-1, BCL-2
3. **Angiogenesis**: Upregulation of VEGF and other pro-angiogenic factors
4. **Invasion and metastasis**: Induction of matrix metalloproteinases (MMPs), epithelial-mesenchymal transition (EMT)

**KEGG pathway**: hsa04010 (MAPK signaling pathway)
**Reactome**: R-HSA-5673001 (RAF/MAP kinase cascade)

#### PI3K/AKT/mTOR Pathway (Cooperating)

Frequently co-activated through PTEN loss. Synergizes with MAPK pathway to promote survival and metabolic adaptation. Important in resistance to BRAF inhibitors.

**KEGG pathway**: hsa04151 (PI3K-Akt signaling pathway)

#### Wnt/β-Catenin Pathway

Contributes to melanoma cell survival, immune evasion, and resistance to immunotherapy.

### Cellular Processes

- **Uncontrolled proliferation**: GO:0008283 (cell population proliferation)
- **Evasion of apoptosis**: GO:0043066 (negative regulation of apoptotic process)
- **Metabolic reprogramming**: GO:0006096 (glycolytic process); GO:0006119 (oxidative phosphorylation)
- **Angiogenesis**: GO:0001525 (angiogenesis)
- **Immune evasion**: GO:0002837 (negative regulation of immune response to tumor cell)
- **Cell migration/invasion**: GO:0016477 (cell migration)

### Protein Dysfunction

The BRAF V600E mutation resides in the activation segment of the kinase domain. The valine-to-glutamic acid substitution mimics the phosphorylation that normally activates the kinase, locking it in a constitutively active conformation. Wild-type BRAF kinase activity is ~70-fold lower than V600E mutant BRAF. The mutant signals as a monomer, unlike wild-type BRAF which requires RAS-dependent dimerization, explaining its RAS-independence.

**UniProt**: P15056 (BRAF_HUMAN)
**PDB**: 1UWH (BRAF kinase domain), 3OG7 (BRAF V600E with vemurafenib)

### Metabolic Changes

BRAF V600E drives a profound metabolic reprogramming:

"BRAF mutations augment glycolysis to promote macromolecular synthesis and proliferation" ([PMID: 38972133](https://pubmed.ncbi.nlm.nih.gov/38972133/)).

The mechanistic basis: "BRAF(V600E) acts to suppress expression of the melanocyte master regulator microphthalmia-associated transcription factor (MITF) and the mitochondrial biogenesis coactivator PGC1α. Accordingly, therapeutic inhibition of BRAF(V600E) reverses metabolic reprogramming in melanoma cells and elevates OXPHOS through increased MITF-PGC1α levels" ([PMID: 24610826](https://pubmed.ncbi.nlm.nih.gov/24610826/)).

This metabolic plasticity is a key resistance mechanism: upon BRAF inhibitor treatment, cells shift from glycolysis to oxidative phosphorylation (OXPHOS), with increased glutamine dependence and mitochondrial biogenesis. NSAIDs (diclofenac, lumiracoxib) can counteract this metabolic reprogramming and synergize with BRAF inhibitors by preventing the shift to OXPHOS ([PMID: 30481565](https://pubmed.ncbi.nlm.nih.gov/30481565/)).

**KEGG pathways**: hsa00010 (Glycolysis/Gluconeogenesis); hsa00190 (Oxidative phosphorylation)
**HMDB**: HMDB0000190 (L-Lactic acid — elevated in glycolytic tumors)

### Immune System Involvement

BRAF V600E melanoma has a complex relationship with the immune system:

- **Tumor immune evasion**: BRAF V600E upregulates immunosuppressive cytokines (IL-6, IL-10, VEGF) and downregulates MHC class I expression
- **PD-L1 expression**: Upregulated in BRAF-mutant tumors, particularly upon BRAF inhibitor treatment
- **T cell infiltration**: BRAF inhibition increases intratumoral CD8+ T cell infiltrate, suggesting immune activation ([PMID: 24903021](https://pubmed.ncbi.nlm.nih.gov/24903021/))
- **B cell involvement**: Tumor-infiltrating B cells may serve as a predictive biomarker; higher B cell signatures associated with better outcomes on dabrafenib + trametinib ([PMID: 34108180](https://pubmed.ncbi.nlm.nih.gov/34108180/))
- **Immune-related adverse events as biomarker**: Vitiligo, panniculitis, and other immune-related skin lesions during BRAF/MEK inhibitor treatment predict better outcomes (HR 0.19 for disease progression, P = 0.043) ([PMID: 30939167](https://pubmed.ncbi.nlm.nih.gov/30939167/)); immune AEs associated with mPFS of 42.8 months vs 6.1 months without (HR 0.22, P = 0.002) ([PMID: 30096703](https://pubmed.ncbi.nlm.nih.gov/30096703/))

### Tissue Damage Mechanisms

- **Local invasion**: Vertical growth phase melanoma invades dermis and subcutaneous tissue
- **Lymphatic spread**: Regional lymph node metastasis (stage III)
- **Hematogenous spread**: Distant metastasis to lung, liver, brain, bone, skin (stage IV)
- **Melanoma-induced stromal remodeling**: Melanoma exosomes reprogram stromal fibroblasts via exosomal miR-155 and miR-210, increasing aerobic glycolysis and extracellular acidification to create a pre-metastatic niche ([PMID: 30150674](https://pubmed.ncbi.nlm.nih.gov/30150674/))

### Resistance Mechanisms

Acquired resistance to BRAF inhibitors is multifactorial:

"Acquired resistance to vemurafenib associated with reactivation of MAPK signaling as observed by elevated ERK1/2 phosphorylation levels in progressive lesions and the appearance of secondary NRAS(Q61) mutations or MEK1(Q56P) or MEK1(E203K) mutations" ([PMID: 23569304](https://pubmed.ncbi.nlm.nih.gov/23569304/)).

Key resistance mechanisms include:
1. **MAPK reactivation**: Secondary NRAS mutations, MEK mutations, BRAF amplification, BRAF splice variants
2. **Alternative pathway activation**: PI3K/AKT, focal adhesion kinase (FAK) signaling
3. **Metabolic reprogramming**: Shift from glycolysis to OXPHOS
4. **Phenotype switching**: Transition from proliferative to invasive state
5. **Microenvironment remodeling**: Stromal cell-mediated resistance
6. **COP1/DET1 mutations**: Acquired after BRAF inhibitor treatment, affecting oncogenic transcriptome regulation ([PMID: 40643496](https://pubmed.ncbi.nlm.nih.gov/40643496/))

### Molecular Profiling

#### Transcriptomics
- BRAF V600E melanomas show distinct gene expression profiles with upregulation of MAPK target genes
- Three tumor subgroups identified by gene expression clustering including an "immune" subgroup associated with improved survival ([PMID: 41537702](https://pubmed.ncbi.nlm.nih.gov/41537702/))
- High IFNγ gene signature scores and cytolytic scores predict better response to encorafenib + binimetinib

#### Proteomics
- Plasma proteome alterations detectable by MAPKi treatment ([PMID: 34246984](https://pubmed.ncbi.nlm.nih.gov/34246984/))
- p-ERK immunohistochemistry serves as a readout of MAPK pathway activity

#### Liquid Biopsy / Circulating Tumor DNA
- BRAF V600 ctDNA detectable by droplet digital PCR (ddPCR) in 93% of pretreatment samples
- Baseline ctDNA positivity rate was 13% in stage III resected disease
- ctDNA detection associated with worse recurrence-free survival (median 3.71 vs 24.41 months in placebo; HR 2.91, P < 0.0001) ([PMID: 40250457](https://pubmed.ncbi.nlm.nih.gov/40250457/))
- On-treatment ctDNA clearance predicts improved outcomes across all treatment arms ([PMID: 33587894](https://pubmed.ncbi.nlm.nih.gov/33587894/); [PMID: 41537702](https://pubmed.ncbi.nlm.nih.gov/41537702/))

---

## 7. Anatomical Structures Affected

### Organ Level

**Primary organ**: Skin (UBERON:0002097)
- Cutaneous melanoma arises from epidermal melanocytes

**Secondary organ involvement** (sites of metastasis):
- **Lymph nodes** (UBERON:0000029): Regional spread; sentinel lymph node most commonly affected
- **Lung** (UBERON:0002048): Most common site of distant metastasis
- **Liver** (UBERON:0002107): Second most common distant site
- **Brain** (UBERON:0000955): ~32% of advanced cases have brain metastases at presentation ([PMID: 34243078](https://pubmed.ncbi.nlm.nih.gov/34243078/))
- **Bone** (UBERON:0002481): Common distant metastatic site
- **Distant skin/subcutaneous tissue**: Transit metastases

**Body systems**: Integumentary (primary), lymphatic, respiratory, hepatobiliary, nervous, musculoskeletal

### Tissue and Cell Level

- **Melanocytes** (CL:0000148): Cell of origin; neural crest-derived pigment cells in the basal epidermis
- **Keratinocytes** (CL:0000312): Surrounding cells affected by paracrine signaling
- **Tumor-infiltrating lymphocytes**: CD8+ T cells (CL:0000625), CD4+ T cells (CL:0000624), B cells (CL:0000236), regulatory T cells (CL:0000815)
- **Dermal fibroblasts** (CL:0000057): Reprogrammed by melanoma exosomes
- **Endothelial cells** (CL:0000115): Involved in tumor angiogenesis

### Subcellular Level

- **Cytoplasm/cytosol** (GO:0005829): Location of BRAF kinase activity and MAPK cascade
- **Cell membrane** (GO:0005886): RAS activation, receptor tyrosine kinase signaling
- **Nucleus** (GO:0005634): ERK-mediated transcriptional activation
- **Mitochondria** (GO:0005739): Site of metabolic reprogramming (OXPHOS vs glycolysis)
- **Lysosomes** (GO:0005764): Autophagy involvement in resistance

### Localization

- **Primary site predilection**: Trunk (UBERON:0002100) — OR = 6.3 for BRAF-mutant melanoma
- **Intermittently sun-exposed skin**: Back, chest, abdomen
- **Less common in chronically sun-damaged sites**: Head and neck (more associated with NRAS or NF1 mutations)
- **Lateralization**: Unilateral; no specific laterality preference

---

## 8. Temporal Development

### Onset

- **Typical age**: Adult-onset, but younger than BRAF wild-type melanomas. Median age ~50–55 years for BRAF-mutant vs ~60–65 for wild-type. BRAF V600K patients tend to be older (>60 years)
- **Onset pattern**: Insidious; typically progresses from a pre-existing nevus or arises de novo over months to years
- **Precursor lesions**: Dysplastic nevi; BRAF V600E is found in ~80% of benign nevi (necessary but not sufficient for melanoma development)

### Progression

**AJCC Staging System (8th Edition)**:

| Stage | Description | 5-Year Survival |
|---|---|---|
| **0 (in situ)** | Confined to epidermis | ~99% |
| **I** | Thin melanoma (≤2 mm), no ulceration | ~92–97% |
| **II** | Thicker primary or ulcerated | ~53–81% |
| **III** | Regional lymph node or in-transit metastasis | ~40–78% (improved to ~75% with adjuvant therapy) |
| **IV** | Distant metastasis | ~15–20% historically; ~50% with modern therapies |

- **Progression rate**: Variable; can be rapid (weeks–months for nodular melanoma) or indolent (years for superficial spreading)
- **Disease course**: Progressive without treatment; potential for long-term remission with modern therapy
- **Duration**: Chronic; lifelong surveillance required even after complete response

### Patterns

- **Remission patterns**: Treatment-induced remissions with BRAF/MEK inhibitors (median duration ~9–12 months); more durable remissions with immunotherapy (years)
- **Critical periods**:
  - Early intervention after diagnosis significantly impacts survival
  - Window of opportunity for adjuvant therapy in resected stage III disease
  - First 3 years post-treatment: highest risk of recurrence with targeted therapy
  - Brain metastasis development: critical period requiring prompt intervention

---

## 9. Inheritance and Population

### Epidemiology

**Global melanoma burden (all subtypes)**: "A worldwide total of 325,000 new melanoma cases (174,000 males, 151,000 females) and 57,000 deaths (32,000 males, 25,000 females) was estimated for 2020" ([PMID: 35353115](https://pubmed.ncbi.nlm.nih.gov/35353115/)). "Cutaneous melanoma causes 55,500 deaths annually" and accounts for 90% of skin cancer mortality ([PMID: 30238891](https://pubmed.ncbi.nlm.nih.gov/30238891/)).

**BRAF V600 mutant melanoma specifically**:
- Represents ~40–50% of cutaneous melanomas
- Estimated ~130,000–162,500 new BRAF V600 mutant melanoma cases worldwide annually
- Highest absolute numbers in populations with high melanoma incidence (Australia/New Zealand, Europe, North America)

**Incidence by region** (all melanoma):
- Australia/New Zealand: Males 42/100,000; Females 31/100,000 (highest worldwide)
- Western Europe: ~19/100,000
- North America: Males 18, Females 14/100,000
- Africa and Asia: <1/100,000

### Genetic Etiology Considerations

- **Not a Mendelian inherited disease**: BRAF V600 mutations are somatic
- **Inheritance pattern**: Multifactorial/polygenic predisposition to melanoma; the specific BRAF mutation is acquired somatically
- **Familial melanoma syndromes**: CDKN2A, CDK4, BAP1, POT1 germline mutations increase melanoma susceptibility but do not guarantee BRAF mutation status
- **Penetrance**: Not applicable to the somatic BRAF mutation itself; familial melanoma gene penetrance varies (CDKN2A: 58–92% by age 80)

### Population Demographics

- **Sex ratio**: Male predominance (OR = 2.4 for BRAF mutation); male:female ~1.15:1 for melanoma overall
- **Ethnic/racial distribution**: Predominantly affects fair-skinned populations of European descent; rare in African, Asian, and Hispanic populations
- **Age distribution**: BRAF-mutant melanomas are younger at diagnosis than BRAF wild-type; V600K specifically more common in older males (>60 years)
- **Geographic distribution**: Higher prevalence in regions with high UV exposure and fair-skinned populations (Australia, Northern Europe, North America)
- **BRAF mutation rate varies by melanoma subtype**: ~50% cutaneous, ~10–15% acral/mucosal ([PMID: 37016119](https://pubmed.ncbi.nlm.nih.gov/37016119/))

---

## 10. Diagnostics

### Clinical Tests

#### Laboratory Tests
- **Serum lactate dehydrogenase (LDH)**: Prognostic biomarker; elevated LDH indicates high tumor burden and is associated with shorter PFS and OS
- **Complete blood count**: Baseline and monitoring; neutrophil/lymphocyte ratio has prognostic value
- **Liver function tests**: Monitoring for hepatic metastases and drug hepatotoxicity
- **Renal function**: Monitoring required due to nephrotoxicity of BRAF inhibitors, especially vemurafenib ([PMID: 26182194](https://pubmed.ncbi.nlm.nih.gov/26182194/))
- **Serum S100B**: Tumor marker for melanoma staging and monitoring

#### Biomarkers
- **BRAF V600 mutation status**: Essential companion diagnostic; determines eligibility for targeted therapy
- **Circulating tumor DNA (ctDNA)**: BRAF V600 ctDNA by ddPCR — prognostic and predictive biomarker; detectable in 93% of pretreatment metastatic samples ([PMID: 33587894](https://pubmed.ncbi.nlm.nih.gov/33587894/)); ctDNA clearance at early timepoints predicts improved survival ([PMID: 40250457](https://pubmed.ncbi.nlm.nih.gov/40250457/))
- **PD-L1 expression**: Relevant for immunotherapy decisions
- **Tumor mutational burden (TMB)**: Higher TMB associated with better response to combination targeted therapy ([PMID: 41537702](https://pubmed.ncbi.nlm.nih.gov/41537702/))
- **IFNγ gene signature**: Immune microenvironment biomarker

#### Imaging
- **Dermoscopy**: Initial evaluation of suspicious lesions
- **CT (chest/abdomen/pelvis)**: Staging for distant metastases
- **PET/CT**: Whole-body staging, recommended from stage IIB/C
- **MRI brain**: Mandatory for staging; brain metastases present in ~32% of advanced cases
- **Ultrasound**: Regional lymph node assessment; recommended from stage IB

#### Biopsy/Pathology
- **Excisional biopsy**: Gold standard for primary diagnosis; provides Breslow depth, mitotic rate, ulceration status
- **Histopathology**: Superficial spreading and nodular subtypes most common in BRAF-mutant melanoma
- **Immunohistochemistry**: Anti-BRAF V600E VE1 clone antibody — sensitivity 86.1%, specificity 96.9%, concordance with PCR 95.1% ([PMID: 28424234](https://pubmed.ncbi.nlm.nih.gov/28424234/))
- **Sentinel lymph node biopsy**: Staging procedure for melanomas ≥0.8 mm with risk factors or ≥1.0 mm ([PMID: 35623961](https://pubmed.ncbi.nlm.nih.gov/35623961/))

### Genetic Testing

#### Recommended Testing Approach
BRAF mutation testing is recommended for all patients with stage IIB/C or higher melanoma, and is mandatory before initiating BRAF/MEK inhibitor therapy ([PMID: 39700658](https://pubmed.ncbi.nlm.nih.gov/39700658/)).

#### Testing Methods

| Method | Turnaround | Sensitivity | Clinical Use |
|---|---|---|---|
| **cobas® 4800 BRAF V600 Mutation Test** (companion diagnostic) | 1–2 days | High | FDA-approved CDx for vemurafenib |
| **Idylla BRAF Mutation Test** | 90 minutes | 98.57% concordance with sequencing | Rapid automated PCR-based testing ([PMID: 26921540](https://pubmed.ncbi.nlm.nih.gov/26921540/)) |
| **Pyrosequencing** | 1–3 days | High; can distinguish V600E/K/R/D | Reference method; lookup tables assist complex result interpretation ([PMID: 24713734](https://pubmed.ncbi.nlm.nih.gov/24713734/)) |
| **Next-generation sequencing (NGS)** | 1–3 weeks | Very high | Comprehensive profiling; detects co-mutations |
| **Sanger sequencing** | 3–5 days | Moderate (~20% mutant allele threshold) | Less commonly used now |
| **VE1 immunohistochemistry** | 1–2 days | 86.1% sensitivity for V600E | Cost-effective screening tool |
| **Droplet digital PCR (ddPCR)** | 1–2 days | Very high (ctDNA detection) | Liquid biopsy monitoring |

Quality assurance: French national EQA achieved false response rate of only 4.8% across 46 laboratories, with improvement from 22 to 12 days turnaround over 6 months ([PMID: 24119386](https://pubmed.ncbi.nlm.nih.gov/24119386/)).

### Clinical Criteria

- **AJCC 8th Edition staging**: Standard staging system
- **Breslow depth**: Most important histological prognostic factor
- **Ulceration status**: Independent prognostic factor
- **Mitotic rate**: Prognostic significance
- **BRAF V600 mutation status**: Determines targeted therapy eligibility

### Differential Diagnosis
- BRAF wild-type melanoma (NRAS, NF1, or triple wild-type subtypes)
- Atypical/dysplastic nevus
- Spitz nevus (may harbor BRAF fusions but not typically V600E)
- Blue nevus
- Melanoma in situ
- Pigmented basal cell carcinoma

---

## 11. Outcome/Prognosis

### Survival and Mortality

**Metastatic BRAF V600 mutant melanoma (with modern therapy)**:

| Treatment | Median PFS | Median OS | 3-Year OS | 5-Year OS |
|---|---|---|---|---|
| Dabrafenib + Trametinib (COMBI-d) | ~11 months | ~25 months | 44% | ~34% |
| Dabrafenib monotherapy (COMBI-d control) | ~8 months | ~18 months | 32% | ~27% |
| Encorafenib + Binimetinib (COLUMBUS) | ~15 months | ~34 months | — | — |
| Real-world BRAFi+MEKi (ADMIRE) | 9.2 months | 22.6 months | — | — |

Source: "3-year PFS was 22% with dabrafenib plus trametinib versus 12% with monotherapy, and 3-year OS was 44% versus 32%, respectively" ([PMID: 28475671](https://pubmed.ncbi.nlm.nih.gov/28475671/)).

Real-world data: ORR 57.4% for combined BRAFi+MEKi vs 39.8% BRAFi monotherapy; median PFS 9.2 months; median OS 22.6 months for first-line combination ([PMID: 34064013](https://pubmed.ncbi.nlm.nih.gov/34064013/)).

**BRAF mutation level as prognostic factor**: High BRAF V600 mutation level (>0.44) associated with worse PFS and OS on multivariate analysis (P = 0.02 for both) ([PMID: 39508497](https://pubmed.ncbi.nlm.nih.gov/39508497/)).

### Prognostic Factors

**Favorable**:
- Normal LDH
- ECOG PS 0
- <3 metastatic sites
- No brain metastases
- Immune-related adverse events during treatment (mPFS 42.8 vs 6.1 months; HR 0.22, P = 0.002) ([PMID: 30096703](https://pubmed.ncbi.nlm.nih.gov/30096703/))
- ctDNA clearance on treatment
- High tumor immune infiltration and TMB

**Unfavorable**:
- Elevated LDH
- ECOG PS ≥1
- ≥3 metastatic sites
- Brain metastases (introduced as major prognostic factor in real-world setting) ([PMID: 34243078](https://pubmed.ncbi.nlm.nih.gov/34243078/))
- High BRAF V600 mutation level
- Detectable ctDNA at baseline and on treatment

### Prognostic Biomarkers

- **ctDNA**: Strongest blood-based prognostic biomarker; "Baseline ctDNA was more strongly associated with survival outcomes than IFNG gene expression or tumour mutational burden" ([PMID: 40250457](https://pubmed.ncbi.nlm.nih.gov/40250457/))
- **LDH**: Standard serum biomarker
- **S100B**: Serum protein biomarker
- **CD8+ TILs**: Higher density associated with better outcomes
- **B cell signatures**: Potential predictive biomarker for targeted therapy ([PMID: 34108180](https://pubmed.ncbi.nlm.nih.gov/34108180/))

---

## 12. Treatment

### Pharmacotherapy

#### FDA-Approved Targeted Therapy Combinations

| Combination | Drug Class | Mechanism | Approval Year |
|---|---|---|---|
| **Dabrafenib + Trametinib** | BRAFi + MEKi | BRAF V600E/K kinase inhibition + MEK1/2 inhibition | 2014 |
| **Vemurafenib + Cobimetinib** | BRAFi + MEKi | BRAF V600E kinase inhibition + MEK1/2 inhibition | 2015 |
| **Encorafenib + Binimetinib** | BRAFi + MEKi | BRAF V600E/K kinase inhibition + MEK1/2 inhibition | 2018 |

**MAXO terms**: MAXO:0001084 (targeted molecular therapy); MAXO:0000058 (pharmacotherapy)

**CHEBI terms**: Vemurafenib (CHEBI:63637), Dabrafenib (CHEBI:75045), Trametinib (CHEBI:75998), Encorafenib (CHEBI:145372), Binimetinib (CHEBI:145371), Cobimetinib (CHEBI:145373)

#### Acceptability and Safety
In a network meta-analysis: "the combination of dabrafenib and trametinib is the preferred combination therapy" for BRAF V600-mutant melanoma, with better acceptability than vemurafenib + cobimetinib (RR for any-grade AEs: 0.94; CrI: 0.89–0.98) ([PMID: 35530323](https://pubmed.ncbi.nlm.nih.gov/35530323/)).

Common adverse events (vemurafenib): arthralgia (37%), alopecia (25%), hyperkeratosis (23%); most common grade 3/4: cutaneous SCC (8%) and keratoacanthoma (8%) ([PMID: 28501764](https://pubmed.ncbi.nlm.nih.gov/28501764/)).

**Nephrotoxicity**: Vemurafenib more nephrotoxic than dabrafenib; 132 cases of AKI reported with vemurafenib vs 13 with dabrafenib; predominantly tubular interstitial injury ([PMID: 26182194](https://pubmed.ncbi.nlm.nih.gov/26182194/)).

**Phototoxicity**: Vemurafenib causes clinical photosensitivity ([PMID: 24154489](https://pubmed.ncbi.nlm.nih.gov/24154489/)).

#### Immunotherapy

| Agent | Drug Class | Mechanism | Use in BRAF+ |
|---|---|---|---|
| **Nivolumab** | Anti-PD-1 | PD-1 checkpoint blockade | First or second-line |
| **Pembrolizumab** | Anti-PD-1 | PD-1 checkpoint blockade | First or second-line |
| **Ipilimumab** | Anti-CTLA-4 | CTLA-4 checkpoint blockade | Combination with anti-PD-1 |
| **Nivolumab + Ipilimumab** | Anti-PD-1 + Anti-CTLA-4 | Dual checkpoint blockade | First-line for aggressive disease |
| **Atezolizumab + Vemurafenib + Cobimetinib** | Anti-PD-L1 + BRAFi + MEKi | Triplet combination | First-line (IMspire150) |

**MAXO terms**: MAXO:0001085 (immune checkpoint inhibitor therapy)

#### Treatment Sequencing

European guidelines recommend: "For first-line treatment particularly in BRAF wild-type patients, immunotherapy with PD-1 antibodies alone or in combination with CTLA-4 antibodies shall be considered. In stage IV melanoma with a BRAF-V600 E/K mutation, first-line therapy with BRAF/MEK inhibitors can be offered as an alternative to immunotherapy" ([PMID: 35623961](https://pubmed.ncbi.nlm.nih.gov/35623961/)).

#### Adjuvant Therapy

For resected stage III disease:
- **Dabrafenib + Trametinib**: Approved adjuvant; 3-year RFS ~60% in COMBI-AD
- **Anti-PD-1 (nivolumab, pembrolizumab)**: Alternative adjuvant option regardless of BRAF status
- Real-world data from China: D+T significantly superior to observation (P = 0.002) and potentially superior to anti-PD-1 monotherapy (P = 0.032) for RFS in BRAF-mutant stage III melanoma ([PMID: 37016119](https://pubmed.ncbi.nlm.nih.gov/37016119/))

### Brain Metastases

Encorafenib + binimetinib achieves brain metastasis response rate >60% ([PMID: 40503961](https://pubmed.ncbi.nlm.nih.gov/40503961/)). Real-world data shows median PFS of 5.5 months and OS of 11.9 months for BRAF V600-mutant melanoma with brain metastases ([PMID: 40411977](https://pubmed.ncbi.nlm.nih.gov/40411977/)). Stereotactic radiosurgery combined with immunotherapy achieves the highest OS rates in brain metastases; BRAF mutation appears to be a favorable prognostic factor ([PMID: 30739835](https://pubmed.ncbi.nlm.nih.gov/30739835/)).

### Surgical Interventions

- **Wide local excision**: Primary treatment; 1–2 cm margins based on Breslow depth
- **Sentinel lymph node biopsy**: Staging procedure for ≥0.8 mm with risk factors
- **Complete lymph node dissection**: For sentinel node-positive disease (increasingly replaced by adjuvant systemic therapy)
- **Metastasectomy**: For oligometastatic disease amenable to complete resection

**MAXO terms**: MAXO:0000004 (surgical procedure); MAXO:0000011 (excision)

### Experimental Therapies and Novel Approaches

- **PHI-501**: Dual RAF/DDR1/2 inhibitor overcomes MAPK resistance ([PMID: 41935307](https://pubmed.ncbi.nlm.nih.gov/41935307/))
- **Avutometinib (RAF-MEK clamp) + FAK inhibitors**: Overcomes resistance to BRAFi+MEKi and immunotherapy ([PMID: 40020669](https://pubmed.ncbi.nlm.nih.gov/40020669/))
- **Metabolic targeting**: NSAIDs (diclofenac, lumiracoxib) + BRAF inhibitors delay resistance ([PMID: 30481565](https://pubmed.ncbi.nlm.nih.gov/30481565/))
- **DCA (dichloroacetate) + elesclomol**: Targeting metabolic reprogramming, effective even in vemurafenib-resistant cells ([PMID: 22865452](https://pubmed.ncbi.nlm.nih.gov/22865452/))
- **Gene-edited stem cell therapy**: Allogeneic twin stem cell system for brain metastatic melanoma ([PMID: 37256936](https://pubmed.ncbi.nlm.nih.gov/37256936/))

### Chemotherapy

Weekly carboplatin + paclitaxel remains a palliative option after immunotherapy failure: median PFS 3.25 months, OS 7.69 months ([PMID: 39354418](https://pubmed.ncbi.nlm.nih.gov/39354418/)).

---

## 13. Prevention

### Primary Prevention

- **UV radiation avoidance**: Limiting sun exposure, especially during peak hours (10 AM – 4 PM)
- **Sunscreen use**: Broad-spectrum SPF 30+ recommended
- **Protective clothing**: Hats, long sleeves, UV-protective fabrics
- **Avoidance of indoor tanning**: Especially before age 25 (62.2% BRAF V600E prevalence in early initiators vs 31.1%, P = .003) ([PMID: 30923800](https://pubmed.ncbi.nlm.nih.gov/30923800/))
- **Education**: USPSTF recommends counseling on UV exposure minimization, especially for patients aged 6 months to 24 years ([PMID: 39418569](https://pubmed.ncbi.nlm.nih.gov/39418569/))
- **Public health campaigns**: Beach-based campaigns can identify high-risk individuals; one campaign found 8.1% suspicious skin cancer lesions and 2.9% possible melanomas among 407 beachgoers ([PMID: 25069660](https://pubmed.ncbi.nlm.nih.gov/25069660/))

**MAXO terms**: MAXO:0000118 (sun protection counseling); MAXO:0000002 (preventive care)

### Secondary Prevention (Screening and Early Detection)

- **Skin self-examination**: ABCDE criteria (Asymmetry, Border, Color, Diameter, Evolution) and "ugly duckling" sign
- **Dermoscopy**: Non-invasive tool enhancing clinical diagnosis; superior to naked-eye examination ([PMID: 20806172](https://pubmed.ncbi.nlm.nih.gov/20806172/))
- **Total body photography and digital dermoscopy**: For high-risk patients to detect early changes
- **Confocal reflectance microscopy**: Improves clinical diagnosis in special cases ([PMID: 39700658](https://pubmed.ncbi.nlm.nih.gov/39700658/))
- **Risk stratification**: Identifying individuals with multiple nevi, family history, fair skin for targeted screening

### Tertiary Prevention

- **Adjuvant therapy**: Dabrafenib + trametinib or anti-PD-1 for resected stage III disease to prevent recurrence
- **Surveillance protocols**: Stage-based follow-up with imaging and clinical examination
- **ctDNA monitoring**: Emerging tool for minimal residual disease detection; patients with favorable ctDNA kinetics (durable undetectable) have markedly better outcomes ([PMID: 40250457](https://pubmed.ncbi.nlm.nih.gov/40250457/))

### Genetic Counseling

- For familial melanoma kindreds (CDKN2A, CDK4, BAP1 mutations)
- BRAF V600E itself is somatic and does not require genetic counseling for family members
- Identification of mole-prone phenotype in adolescents may facilitate early intervention ([PMID: 28593303](https://pubmed.ncbi.nlm.nih.gov/28593303/))

---

## 14. Other Species / Natural Disease

### Taxonomy

BRAF mutations and melanoma occur across species:

| Species | NCBI Taxon ID | BRAF Gene | Melanoma Occurrence |
|---|---|---|---|
| *Homo sapiens* | 9606 | BRAF (Gene ID: 673) | Primary disease |
| *Mus musculus* | 10090 | Braf (Gene ID: 109880) | Engineered models |
| *Danio rerio* (zebrafish) | 7955 | braf (Gene ID: 403065) | Engineered models |
| *Canis lupus familiaris* (dog) | 9615 | BRAF (Gene ID: 475526) | Naturally occurring oral melanoma |
| *Equus caballus* (horse) | 9796 | BRAF | Naturally occurring melanoma (grey horses) |

### Natural Disease in Animals

- **Dogs**: Oral and cutaneous melanoma occurs naturally; BRAF mutations are rare but reported. Canine melanoma serves as a comparative oncology model
- **Horses**: Grey horses develop melanoma with high frequency (>80% of grey horses >15 years); pathogenesis involves STX17 duplication rather than BRAF mutations
- **Fish**: Xiphophorus (swordtail-platyfish) hybrids develop melanoma driven by xmrk oncogene, not BRAF

### Comparative Biology

- The RAS-RAF-MEK-ERK pathway is highly conserved across vertebrates
- BRAF V600E can drive melanocyte transformation in zebrafish, demonstrating evolutionary conservation of the oncogenic mechanism
- Zebrafish BRAF V600E melanomas "show an overall low mutation burden, which has a strong, inverse association with the number of initiating germline drivers" ([PMID: 24148783](https://pubmed.ncbi.nlm.nih.gov/24148783/))

---

## 15. Model Organisms

### Mouse Models

- **BRAF(V600E)/Pten(−/−) syngeneic tumor graft model**: Immunocompetent mouse model used to study BRAF inhibition and immunotherapy combination. "BRAF inhibition leads to a significant increase in the intratumoral CD8(+) T-cell density and cytokine production, similar to the effects of BRAF inhibition in patients" ([PMID: 24903021](https://pubmed.ncbi.nlm.nih.gov/24903021/))
- **ESC-GEMM platform**: Rapid melanoma modeling system incorporating 12 clinically relevant genotypes from combinations of LSL-Braf(V600E) and other driver alleles ([PMID: 31744817](https://pubmed.ncbi.nlm.nih.gov/31744817/))
- **BrafCA/+; Tyr-CreERT2; Ptenfl/fl**: Conditional BRAF V600E activation with PTEN deletion in melanocytes; develops melanoma with ~100% penetrance
- **Global pannexin 1 deletion model**: Combined with BRAF/Pten melanoma; increased tumor-infiltrating lymphocytes ([PMID: 38327091](https://pubmed.ncbi.nlm.nih.gov/38327091/))
- **Syngeneic models**: Enable immunotherapy studies; BP (BRAF V600E/PTEN−/−) model widely used

### Zebrafish Models

- **Tg(mitfa:BRAF(V600E)); p53(−/−)**: Develops melanoma from nevi over months; relatively low mutation burden
- Allows visualization of melanoma development in vivo
- "Melanomas present with variable onset and pathology, implicating additional somatic mutations in a multi-hit tumorigenic process" ([PMID: 24148783](https://pubmed.ncbi.nlm.nih.gov/24148783/))
- Recurrent amplification of protein kinase A pathway in cooperation with BRAF(V600E) and p53−/−

### Cell Line Models

- **A375**: Human melanoma cell line, BRAF V600E mutant; most widely used in vitro model
- **SK-MEL-28**: Human melanoma cell line, BRAF V600E
- **SK-MEL-3**: Used for xenograft studies of drug resistance ([PMID: 41935307](https://pubmed.ncbi.nlm.nih.gov/41935307/))
- **WM266-4, Colo829**: Additional BRAF V600E lines
- Drug-resistant derivatives generated for resistance mechanism studies

### Model Limitations

- Mouse models may not fully recapitulate human tumor microenvironment complexity
- Syngeneic models use murine tumors that may differ in antigen presentation
- Zebrafish lack certain mammalian immune cell populations
- Cell lines may diverge from primary tumor biology after prolonged culture
- Patient-derived xenografts (PDX) better represent heterogeneity but require immunodeficient hosts

### CNS Tumor Models

- Challenges in modeling heterogeneous BRAF-mutant CNS neoplasms; pediatric cancer model development lags behind adult ([PMID: 37920169](https://pubmed.ncbi.nlm.nih.gov/37920169/))

---

## Key Findings (Evidence Summary)

### Finding 1: BRAF V600E Is the Dominant Oncogenic Mutation in ~40–50% of Cutaneous Melanomas

BRAF V600E is the most frequent oncogenic BRAF mutation in melanoma, present in 40–50% of all cutaneous melanomas. Among BRAF V600 mutations specifically, V600E accounts for ~79%, V600K for ~12%, V600R for ~5%, and V600M for ~4%. The V600E substitution results in a constitutively active kinase domain with ~500-fold increased activity, leading to MAPK/ERK pathway hyperactivation independent of extracellular stimuli, driving cell proliferation, survival, angiogenesis, and other hallmark cancer features.

**Key citations**:
- "As widely acknowledged, 40-50% of all melanoma patients harbour an activating BRAF mutation (mostly BRAF V600E)" — [PMID: 33801689](https://pubmed.ncbi.nlm.nih.gov/33801689/)
- "V600E mutation results in a constitutively active kinase domain, leading to dysregulated downstream signaling independent of extracellular stimuli" — [PMID: 39961465](https://pubmed.ncbi.nlm.nih.gov/39961465/)
- "Among BRAF V600 mutations, 79%, 12%, 5%, and 4% were V600E, V600K, V600R, and V600M, respectively" — [PMID: 22536370](https://pubmed.ncbi.nlm.nih.gov/22536370/)

### Finding 2: BRAF V600 Melanoma Is Associated with Younger Age, Intermittent Sun Exposure, and Trunk Location

BRAF mutations are significantly associated with distinct clinicopathological features: male gender (OR = 2.4), younger age (OR = 2.7), superficial spreading melanoma (OR = 15.6), nodular melanoma (OR = 9.5), trunk localization (OR = 6.3), and intermittent sun exposure (OR = 4.6). Indoor tanning users, especially those initiating before age 25, had dramatically higher BRAF V600E prevalence (62.2% vs 31.1%, P = .003).

**Key citations**:
- "Associations with BRAF mutation were as follows: male gender [OR = 2.4], younger age (OR = 2.7), superficial spreading (OR = 15.6) and nodular melanoma (OR = 9.5), trunk localization (OR = 6.3), and intermittent sun exposure (OR = 4.6)" — [PMID: 25357015](https://pubmed.ncbi.nlm.nih.gov/25357015/)
- "BRAF V600E genotype was more prevalent in ever-users than in nonusers (42.9% vs 28.3%, P = .04)" — [PMID: 30923800](https://pubmed.ncbi.nlm.nih.gov/30923800/)

### Finding 3: BRAF+MEK Inhibitor Combination Achieves ~60% ORR but Resistance Develops Within 6–12 Months

The combination of BRAF and MEK inhibitors achieves high initial response rates (~57–70% ORR) but acquired resistance typically develops within 6–12 months. Long-term data from COMBI-d showed 3-year PFS of 22% and 3-year OS of 44% with dabrafenib + trametinib. Resistance mechanisms involve MAPK reactivation through secondary NRAS Q61 mutations, MEK1 mutations (Q56P, E203K), BRAF amplification, and alternative pathway activation.

**Key citations**:
- "3-year PFS was 22% with dabrafenib plus trametinib versus 12% with monotherapy, and 3-year OS was 44% versus 32%, respectively" — [PMID: 28475671](https://pubmed.ncbi.nlm.nih.gov/28475671/)
- "Acquired resistance to vemurafenib associated with reactivation of MAPK signaling...and the appearance of secondary NRAS(Q61) mutations or MEK1(Q56P) or MEK1(E203K) mutations" — [PMID: 23569304](https://pubmed.ncbi.nlm.nih.gov/23569304/)

### Finding 4: BRAF V600E Drives Metabolic Reprogramming; Inhibition Reverses the Shift

BRAF V600E mutations augment glycolysis (Warburg effect) to support macromolecular synthesis and proliferation, while suppressing MITF and PGC1α expression to reduce mitochondrial biogenesis. BRAF inhibition reverses this metabolic program, shifting cells toward oxidative phosphorylation — a metabolic plasticity that contributes to drug resistance.

**Key citations**:
- "BRAF mutations augment glycolysis to promote macromolecular synthesis and proliferation" — [PMID: 38972133](https://pubmed.ncbi.nlm.nih.gov/38972133/)
- "BRAF(V600E) acts to suppress expression of MITF and PGC1α. Therapeutic inhibition of BRAF(V600E) reverses metabolic reprogramming and elevates OXPHOS through increased MITF-PGC1α levels" — [PMID: 24610826](https://pubmed.ncbi.nlm.nih.gov/24610826/)

### Finding 5: Global Melanoma Epidemiology

GLOBOCAN 2020 reported 325,000 new melanoma cases and 57,000 deaths worldwide, with highest incidence in Australia/New Zealand (males 42/100,000; females 31/100,000). BRAF V600 mutations represent 40–50% of these cutaneous melanomas.

**Key citations**:
- "A worldwide total of 325,000 new melanoma cases (174,000 males, 151,000 females) and 57,000 deaths (32,000 males, 25,000 females) was estimated for 2020" — [PMID: 35353115](https://pubmed.ncbi.nlm.nih.gov/35353115/)
- "Cutaneous melanoma causes 55,500 deaths annually" — [PMID: 30238891](https://pubmed.ncbi.nlm.nih.gov/30238891/)

---

## Mechanistic Model

The following causal chain describes the pathogenesis of BRAF V600 Mutant Melanoma:

```
UV Radiation (intermittent) + Genetic Susceptibility (MC1R, CDKN2A, fair skin)
            │
            ▼
    Somatic BRAF V600E Mutation in Melanocyte
            │
            ▼
    Constitutive BRAF Kinase Activation (~500x)
            │
            ├──► MEK1/2 Phosphorylation ──► ERK1/2 Activation
            │         │
            │         ├──► Cell Proliferation (Cyclin D1, c-Myc)
            │         ├──► Survival (BIM suppression, MCL-1 upregulation)
            │         ├──► Angiogenesis (VEGF)
            │         └──► Immune Evasion (PD-L1, IL-10)
            │
            ├──► MITF/PGC1α Suppression ──► Metabolic Shift to Glycolysis
            │
            └──► Cooperating Events (PTEN loss, CDKN2A deletion, TERT activation)
                        │
                        ▼
                 Melanoma Development & Progression
                        │
            ┌───────────┴───────────┐
            ▼                       ▼
    Local Invasion              Metastasis
    (Breslow depth)        (LN → Distant organs)
                                    │
                                    ▼
                            BRAF/MEK Inhibitor Therapy
                                    │
                        ┌───────────┴───────────┐
                        ▼                       ▼
                Initial Response           Acquired Resistance
                (ORR ~60-70%)         (6-12 months median)
                                            │
                        ┌───────────────────┼───────────────────┐
                        ▼                   ▼                   ▼
                MAPK Reactivation    PI3K/AKT/FAK         Metabolic Shift
                (NRAS, MEK mut,      Activation            (Glycolysis → OXPHOS)
                 BRAF amplification)
```

---

## Evidence Base

| Reference | PMID | Key Contribution |
|---|---|---|
| Paluncic et al., 2021 | [33801689](https://pubmed.ncbi.nlm.nih.gov/33801689/) | BRAF V600E prevalence in 40-50% of melanomas |
| Colombino et al., 2014 | [25357015](https://pubmed.ncbi.nlm.nih.gov/25357015/) | Clinicopathological associations with BRAF mutation |
| Ascierto et al., 2012 | [22536370](https://pubmed.ncbi.nlm.nih.gov/22536370/) | V600 mutation subtype distribution |
| Long et al., 2017 | [28475671](https://pubmed.ncbi.nlm.nih.gov/28475671/) | COMBI-d long-term survival data |
| Shi et al., 2014 | [23569304](https://pubmed.ncbi.nlm.nih.gov/23569304/) | Vemurafenib resistance mechanisms |
| Haq et al., 2014 | [24610826](https://pubmed.ncbi.nlm.nih.gov/24610826/) | BRAF-driven metabolic reprogramming |
| Garbe et al., 2022 | [35623961](https://pubmed.ncbi.nlm.nih.gov/35623961/) | European treatment guidelines |
| Arnold et al., 2022 | [35353115](https://pubmed.ncbi.nlm.nih.gov/35353115/) | GLOBOCAN 2020 melanoma burden |
| Schadendorf et al., 2018 | [30238891](https://pubmed.ncbi.nlm.nih.gov/30238891/) | Comprehensive melanoma review |
| Bhatt et al., 2020 | [30923800](https://pubmed.ncbi.nlm.nih.gov/30923800/) | Indoor tanning and BRAF mutation |
| Haq, 2024 | [38972133](https://pubmed.ncbi.nlm.nih.gov/38972133/) | Metabolic changes in BRAF-mutant melanoma |
| Kumar et al., 2025 | [39961465](https://pubmed.ncbi.nlm.nih.gov/39961465/) | BRAF V600E structural and pathway analysis |
| Saiag et al., 2021 | [34243078](https://pubmed.ncbi.nlm.nih.gov/34243078/) | Real-world French study of D+T |
| Nassi et al., 2021 | [34064013](https://pubmed.ncbi.nlm.nih.gov/34064013/) | ADMIRE real-world registry |
| Lee et al., 2026 | [40250457](https://pubmed.ncbi.nlm.nih.gov/40250457/) | ctDNA as prognostic biomarker |

---

## Limitations and Knowledge Gaps

1. **Optimal treatment sequencing**: The ideal order of targeted therapy vs. immunotherapy for BRAF V600-mutant melanoma remains unclear; no head-to-head randomized trial comparing first-line BRAF/MEKi vs. anti-PD-1 vs. combination immunotherapy has been completed.

2. **Resistance prediction**: While mechanisms of acquired resistance are increasingly understood, reliable predictive biomarkers to identify patients who will develop resistance early vs. achieve durable responses are lacking.

3. **Rare BRAF variants**: Treatment evidence for V600R, V600M, V600D, and non-V600 BRAF mutations is limited to retrospective analyses. ORR for rare V600 non-E/K mutations is 45% vs 26% for non-V600 mutations (P = 0.025) ([PMID: 40850313](https://pubmed.ncbi.nlm.nih.gov/40850313/)).

4. **Ethnic diversity**: Most clinical trial data come from predominantly Caucasian populations. BRAF mutation rates and responses may differ in Asian, African, and other populations. A Chinese study found mutation rates of ~50% in cutaneous but only 10–15% in acral/mucosal subtypes ([PMID: 37016119](https://pubmed.ncbi.nlm.nih.gov/37016119/)).

5. **Long-term survivorship**: As patients increasingly achieve long-term responses, the chronic effects of prolonged targeted therapy and immunotherapy on quality of life, organ function, and secondary malignancy risk require further study.

6. **Brain metastases**: While intracranial activity has been demonstrated, brain metastases remain a major prognostic challenge and the optimal management (systemic therapy, SRS, WBRT, or combinations) requires further prospective data.

7. **Minimal residual disease**: ctDNA-guided interventional strategies (escalating therapy in ctDNA-positive patients, de-escalating in ctDNA-negative) are promising but unvalidated in prospective trials.

8. **Gene-environment interactions**: The precise molecular mechanism by which intermittent UV exposure preferentially induces BRAF V600E mutations (vs. other mutation patterns) is not fully elucidated.

---

## Proposed Follow-up Experiments/Actions

1. **Prospective biomarker-guided clinical trials**: Design trials using baseline ctDNA and immune gene signatures to stratify patients to optimal first-line therapy (targeted vs. immunotherapy vs. combination).

2. **ctDNA-guided adjuvant therapy**: Test whether ctDNA-driven escalation/de-escalation strategies improve outcomes in resected stage III BRAF-mutant melanoma.

3. **Novel combination strategies**: Evaluate PHI-501 (pan-RAF/DDR inhibitor) and avutometinib + FAK inhibitor combinations in BRAF/MEK inhibitor-resistant patients.

4. **Metabolic vulnerability exploitation**: Clinical trials combining BRAF/MEK inhibitors with metabolic inhibitors (e.g., OXPHOS inhibitors, glutaminase inhibitors) to prevent metabolic adaptation-based resistance.

5. **Rare BRAF variant registry**: Continue global data collection through resources like the Heidelberg rare BRAF mutations database to establish evidence-based treatment guidelines for V600R, V600M, V600D, and non-V600 mutations.

6. **Single-cell and spatial transcriptomics**: Apply advanced technologies to resistant tumors to understand the spatial organization of resistant clones and immune microenvironment changes.

7. **Diverse population studies**: Conduct BRAF mutation screening and treatment outcome studies in underrepresented populations (African, Asian, Latin American) to ensure equitable access to precision medicine.

8. **Brain metastasis prevention**: Investigate whether early use of brain-penetrant BRAF/MEK inhibitors (e.g., encorafenib) can prevent or delay brain metastasis development in high-risk patients.

---

*Report generated: 2026-05-05*
*Based on analysis of 109 published papers and 5 confirmed findings*
*Disease: BRAF V600 Mutant Melanoma (MONDO:0005012 subtype)*
