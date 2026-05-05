---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-04T23:11:25.945707'
end_time: '2026-05-04T23:40:13.560114'
duration_seconds: 1727.61
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ANK2 Ankyrin-B Syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 15
    timeout: 2400
citation_count: 33
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ANK2 Ankyrin-B Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **ANK2 Ankyrin-B Syndrome** covering all of the
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

# Comprehensive Disease Report: ANK2 Ankyrin-B Syndrome

## Summary

**ANK2 Ankyrin-B Syndrome** (MONDO:0010958; OMIM:600919) is a rare autosomal dominant cardiac arrhythmia disorder caused by loss-of-function variants in the *ANK2* gene (chromosome 4q25-q26), which encodes the multifunctional adapter protein ankyrin-B. Originally described as long QT syndrome type 4 (LQT4), the disease is now recognized as a clinically distinct entity characterized by a complex and variable cardiac phenotype including sinus bradycardia, sinus node dysfunction, atrial fibrillation, variable QT interval prolongation, catecholaminergic polymorphic ventricular tachycardia (CPVT), and risk of sudden cardiac death. The defining molecular mechanism involves disrupted membrane targeting of key cardiac ion transporters — the Na⁺/Ca²⁺ exchanger (NCX1), Na⁺/K⁺-ATPase (NKA), and inositol 1,4,5-trisphosphate receptor (InsP3R) — at T-tubule/sarcoplasmic reticulum junctions in cardiomyocytes, leading to intracellular calcium dysregulation, CaMKII-dependent hyperphosphorylation of ryanodine receptor 2 (RyR2), and triggered arrhythmias.

The syndrome exhibits incomplete penetrance and highly variable expressivity, with clinical manifestations ranging from asymptomatic carrier status to sudden cardiac death. Notably, a ClinGen Channelopathy Expert Panel reappraisal has classified ANK2 as having "limited or disputed evidence" for classical LQTS causation, though robust experimental evidence from multiple mouse models and human genetic studies firmly establishes ankyrin-B dysfunction as a cause of complex cardiac arrhythmia. Treatment is symptom-directed, including beta-blockers, flecainide, avoidance of QT-prolonging drugs, and device therapy (pacemakers for sinus node dysfunction, implantable cardioverter-defibrillators for high-risk individuals). No disease-modifying therapies currently exist, though CaMKII inhibition has shown promise in preclinical models.

This report synthesizes evidence from 43 peer-reviewed publications to provide a comprehensive characterization of ANK2 Ankyrin-B Syndrome across all disease dimensions, from molecular pathophysiology to clinical management, suitable for populating a disease knowledge base entry.

---

## 1. Disease Information

### Overview

ANK2 Ankyrin-B Syndrome is a genetic cardiac arrhythmia disorder caused by loss-of-function variants in *ANK2* (ankyrin-B). The disease was first identified in 2003 when Mohler et al. discovered that a loss-of-function mutation (E1425G) in ankyrin-B caused dominantly inherited type 4 long-QT cardiac arrhythmia ([PMID: 12571597](https://pubmed.ncbi.nlm.nih.gov/12571597/)). Subsequent studies revealed that the phenotype extends well beyond QT prolongation, leading to its reclassification as "ankyrin-B syndrome" — a distinct clinical entity separate from classical long QT syndromes ([PMID: 15178757](https://pubmed.ncbi.nlm.nih.gov/15178757/)).

As stated by Mohler et al. (2004): *"Humans with ankyrin-B mutations display varying degrees of cardiac dysfunction including bradycardia, sinus arrhythmia, idiopathic ventricular fibrillation, catecholaminergic polymorphic ventricular tachycardia, and risk of sudden death. However, a prolonged rate-corrected QT interval was not a consistent feature, indicating that ankyrin-B dysfunction represents a clinical entity distinct from classic long QT syndromes."* ([PMID: 15178757](https://pubmed.ncbi.nlm.nih.gov/15178757/))

### Key Identifiers

| Database | Identifier |
|----------|-----------|
| MONDO | MONDO:0010958 (cardiac arrhythmia, ankyrin-B-related) |
| OMIM | 600919 (Long QT syndrome 4) |
| Gene | *ANK2* (HGNC:493) |
| Chromosome | 4q25-q26 |
| ICD-10 | I49.8 (Other specified cardiac arrhythmias) |
| MeSH | Long QT Syndrome (broader category) |

### Synonyms and Alternative Names

- Ankyrin-B syndrome
- Long QT syndrome type 4 (LQT4) — historical designation
- Cardiac arrhythmia, ankyrin-B-related
- ANK2-related cardiac arrhythmia syndrome

### Information Sources

The information in this report is derived from aggregated disease-level resources including OMIM, ClinVar, ClinGen, and primary literature (43 peer-reviewed publications), supplemented by evidence from animal model studies and computational modeling.

---

## 2. Etiology

### Disease Causal Factors

The primary cause of ANK2 Ankyrin-B Syndrome is **genetic**: loss-of-function variants in the *ANK2* gene encoding ankyrin-B. The disease follows autosomal dominant inheritance with incomplete penetrance and variable expressivity.

The original causative mutation identified was **E1425G** (p.Glu1425Gly), described by Mohler et al. (2003): *"a loss-of-function (E1425G) mutation in ankyrin-B (also known as ankyrin 2), a member of a family of versatile membrane adapters, causes dominantly inherited type 4 long-QT cardiac arrhythmia in humans"* ([PMID: 12571597](https://pubmed.ncbi.nlm.nih.gov/12571597/)).

A novel mechanism was also described involving a **reciprocal chromosomal translocation** between chromosomes 4q25 and 9q26 that transects the *ANK2* gene, resulting in ankyrin-B haploinsufficiency and clinical features of ankyrin-B syndrome ([PMID: 27916589](https://pubmed.ncbi.nlm.nih.gov/27916589/)).

### Genetic Risk Factors

- **Causal variants**: Multiple loss-of-function variants in *ANK2* have been identified, including E1425G, V1516D, T1404I, R1788W, L1622I, Q1283H, and W1535R
- **Susceptibility loci**: The *ANK2* locus has been linked with QTc interval variability in the general human population ([PMID: 19394342](https://pubmed.ncbi.nlm.nih.gov/19394342/))
- **Modifier genes**: *KCNH2* has been shown to functionally interact with *ANK2*, with double mutation carriers (ANK2-E1813K + KCNH2-H562R) displaying markedly more severe phenotypes ([PMID: 30929919](https://pubmed.ncbi.nlm.nih.gov/30929919/))
- **βII spectrin** (*SPTBN1*): A novel human mutation in ankyrin-B that disrupts the ankyrin-B/βII spectrin interaction leads to severe human arrhythmia phenotypes ([PMID: 25632041](https://pubmed.ncbi.nlm.nih.gov/25632041/))

### Environmental Risk Factors and Gene-Environment Interactions

- **Catecholaminergic stress**: Arrhythmias are frequently triggered by adrenergic stimulation (exercise, emotional stress, isoproterenol)
- **QT-prolonging drugs**: Medications that prolong the QT interval may unmask or exacerbate arrhythmias in ANK2 variant carriers
- **Acquired LQTS context**: Four of eight LQTS patients carrying ANK2 mutations in a Japanese cohort had acquired LQTS (aLQTS), suggesting that ANK2 variants may serve as susceptibility factors that manifest with environmental triggers ([PMID: 27784853](https://pubmed.ncbi.nlm.nih.gov/27784853/))
- **Secondary genetic variation**: The common ANK2 p.L1622I variant "may confer arrhythmia susceptibility in the context of secondary risk factors including environment, medication, and/or additional genetic variation" ([PMID: 27298202](https://pubmed.ncbi.nlm.nih.gov/27298202/))

### Protective Factors

No specific genetic or environmental protective factors have been identified for ANK2 Ankyrin-B Syndrome. However, avoidance of catecholaminergic triggers and QT-prolonging medications may reduce arrhythmia risk in carriers.

---

## 3. Phenotypes

### Cardiac Arrhythmia Phenotypes

| Phenotype | HPO Term | Frequency | Onset | Severity |
|-----------|----------|-----------|-------|----------|
| Sinus bradycardia | HP:0001662 | Common | Variable (childhood–adult) | Mild to severe |
| Sinus node dysfunction | HP:0001678 | High penetrance in some families | Variable | Moderate to severe |
| Atrial fibrillation | HP:0005110 | Common | Typically adult | Variable |
| QT interval prolongation | HP:0001657 | Variable/inconsistent | Variable | Mild to moderate |
| Catecholaminergic polymorphic ventricular tachycardia | HP:0031546 | Present in subset | Typically with stress | Severe |
| Ventricular fibrillation | HP:0001663 | Present in subset | Variable | Life-threatening |
| Cardiac conduction defects | HP:0005150 | Present in subset | Progressive, age-related | Variable |
| Sudden cardiac death | HP:0001645 | Risk present | Variable | Fatal |
| Heart rate variability | HP:0007110 | Common | Variable | Mild |
| Torsades de pointes | HP:0001664 | Present in subset | Episodic | Severe |

#### Sinus Node Dysfunction (SND)

Two families with highly penetrant and severe SND were mapped to the *ANK2* locus. As described by Le Scouarnec et al. (2008): *"We mapped two families with highly penetrant and severe SND to the human ANK2 (ankyrin-B/AnkB) locus. Mice heterozygous for AnkB phenocopy human SND displayed severe bradycardia and rate variability. AnkB is essential for normal membrane organization of sinoatrial node cell channels and transporters"* ([PMID: 18832177](https://pubmed.ncbi.nlm.nih.gov/18832177/)).

#### Atrial Fibrillation

Computational modeling predicts that *"defective membrane targeting of the voltage-gated L-type Ca²⁺ channel Cav1.3 leads to action potential shortening that reduces the critical atrial tissue mass needed to sustain reentrant activation"* ([PMID: 23436330](https://pubmed.ncbi.nlm.nih.gov/23436330/)), explaining the susceptibility to atrial fibrillation in ankyrin-B syndrome.

#### Clinical Case Example

A clinical case report describes a young adult patient with *"sinus node dysfunction, atrial fibrillation and prolonged QT syndrome... with a family history of sudden death"* ([PMID: 25456501](https://pubmed.ncbi.nlm.nih.gov/25456501/)), illustrating the multifaceted phenotype.

### Phenotype Variability

A key feature of ankyrin-B syndrome is its remarkable phenotypic variability. In a Japanese cohort of 535 inherited primary arrhythmia syndrome (IPAS) probands, 12 (2.2%) carried 7 different heterozygous *ANK2* mutations, with phenotypes including LQTS (8), Brugada syndrome (2), idiopathic ventricular fibrillation (1), and sick sinus syndrome/atrial fibrillation (1) ([PMID: 27784853](https://pubmed.ncbi.nlm.nih.gov/27784853/)).

### Quality of Life Impact

- **Sinus node dysfunction**: May require permanent pacemaker implantation; affects exercise capacity and daily functioning
- **Atrial fibrillation**: Increased stroke risk, palpitations, fatigue
- **Ventricular arrhythmias/sudden death risk**: Significant psychological burden; may require activity restriction and ICD implantation
- **Drug avoidance**: Need to avoid QT-prolonging medications restricts treatment options for other conditions

---

## 4. Genetic/Molecular Information

### Causal Gene

- **Gene**: *ANK2* (Ankyrin 2 / Ankyrin-B)
- **HGNC ID**: HGNC:493
- **OMIM Gene**: 106410
- **Chromosome location**: 4q25-q26
- **Protein**: Ankyrin-B (220 kDa isoform is the primary cardiac form)
- **UniProt**: Q01484

### Pathogenic Variants

Mohler et al. (2007) characterized the functional impact of nine human ANK2 variants: *"We then characterized the relative severity of loss-of-function properties of all 9 nonsynonymous ANK2 variants identified to date in primary cardiomyocytes and identified a range of in vitro phenotypes, including wild-type, simple loss-of-function, and severe loss-of-function activity, seen with the variants causing severe human phenotypes."* ([PMID: 17242276](https://pubmed.ncbi.nlm.nih.gov/17242276/))

| Variant | Classification | Functional Category | Population Frequency | Clinical Association |
|---------|---------------|---------------------|---------------------|---------------------|
| E1425G | Pathogenic | Severe LOF | Very rare | Original LQT4 family; severe arrhythmias |
| V1516D | Likely pathogenic | Severe LOF | Very rare | Severe phenotype |
| T1404I | Likely pathogenic | LOF | Rare | Arrhythmia |
| Q1283H | Disease-associated | LOF | Rare | Stress-induced arrhythmias |
| W1535R | Likely pathogenic | LOF (predicted damaging) | Rare | Found in 5 LQTS + 1 BrS patient |
| L1622I | Mild LOF / risk variant | Mild LOF | 2% European, 8% West African | Enhanced contractility + arrhythmia risk |
| R1788W | Disputed | Altered obscurin binding | Present in controls | Near obscurin-binding motif |
| E1813K | Disputed/modifier | Functional interaction with KCNH2 | Present in controls | Conduction disease; aggravates KCNH2 mutations |
| T1626N | Disputed | Present in controls | Present in controls | Found in control populations |

#### Allele Frequency Concerns

A critical finding from targeted mutational analysis is that ANK2 variants are surprisingly common in control populations. Cronk et al. (2007) found: *"Overall, 14 distinct nonsynonymous variants (10 novel) were observed in 9 (3.3%) of 269 genotype-negative LQTS patients, 5 (1.8%) of 272 genotype-positive LQTS cases, 4 (4%) of 100 white controls, and 9 (9%) of 100 black controls"* ([PMID: 16253912](https://pubmed.ncbi.nlm.nih.gov/16253912/)). This high frequency of ANK2 variants in control populations complicates pathogenicity assessment and underscores the need for functional characterization of individual variants.

The L1622I variant is particularly notable, with prevalence ranging *"from 2 percent of European individuals to 8 percent in individuals from West Africa"* ([PMID: 17940615](https://pubmed.ncbi.nlm.nih.gov/17940615/)). This variant is considered a "balanced" or "mild" loss-of-function variant that enhances cardiac contractility but also confers arrhythmia susceptibility and premature senescence risk.

#### Chromosomal Abnormality

A reciprocal chromosomal translocation between 4q25 and 9q26 that transects the *ANK2* gene has been described as a novel mechanism causing ankyrin-B haploinsufficiency and the clinical syndrome ([PMID: 27916589](https://pubmed.ncbi.nlm.nih.gov/27916589/)).

### ClinGen Evidence Reappraisal

The ClinGen Channelopathy Expert Panel has provided important reassessments:

1. **For LQTS** (2020): ANK2 was classified among genes with *"limited or disputed evidence"* for LQTS causation. As stated: *"More than half of the genes reported as causing LQTS have limited or disputed evidence to support their disease causation. Genetic variants in these genes should not be used for clinical decision-making, unless accompanied by new and sufficient genetic evidence."* ([PMID: 31983240](https://pubmed.ncbi.nlm.nih.gov/31983240/))

2. **For CPVT** (2022): ANK2 variants were deemed *"too common in the population to be disease-causing"* for CPVT specifically ([PMID: 34557911](https://pubmed.ncbi.nlm.nih.gov/34557911/)).

This does **not** negate the strong experimental evidence for ankyrin-B dysfunction causing cardiac arrhythmia, but rather indicates that the clinical syndrome may not fit neatly into the traditional channelopathy classification framework.

### Modifier Genes and Interacting Proteins

- **KCNH2 (hERG)**: ANK2-E1813K functionally interacts with KCNH2, with double heterozygosity causing markedly severe LQTS ([PMID: 30929919](https://pubmed.ncbi.nlm.nih.gov/30929919/))
- **βII Spectrin (SPTBN1)**: Essential partner for ankyrin-B localization; mutations disrupting the ankyrin-B/βII spectrin interaction cause severe arrhythmias ([PMID: 25632041](https://pubmed.ncbi.nlm.nih.gov/25632041/))
- **Obscurin**: Mediates ankyrin-B targeting to the cardiac M-line; the R1788W variant increases obscurin binding ([PMID: 18782775](https://pubmed.ncbi.nlm.nih.gov/18782775/))
- **EHD3**: Endosome pathway protein critical for ankyrin-B-dependent membrane protein trafficking ([PMID: 24759929](https://pubmed.ncbi.nlm.nih.gov/24759929/))
- **OTUD7A**: Deubiquitinase whose interactions with Ankyrin-B and Ankyrin-G are disrupted by the epilepsy-associated L233F variant ([PMID: 36604605](https://pubmed.ncbi.nlm.nih.gov/36604605/))

---

## 5. Environmental Information

### Environmental Factors

ANK2 Ankyrin-B Syndrome is a purely genetic disorder; no environmental toxins, radiation, or occupational exposures are known to cause the disease. However, environmental factors can modulate disease expression:

- **Catecholaminergic stimulation** (exercise, stress, isoproterenol) is the primary trigger for arrhythmias in carriers
- **QT-prolonging medications** may unmask or worsen the phenotype
- **Acquired factors**: Myocardial infarction causes striking remodeling of ankyrin-B and associated proteins, suggesting that ischemic heart disease may interact with genetic ankyrin-B deficiency ([PMID: 19394342](https://pubmed.ncbi.nlm.nih.gov/19394342/))

### Lifestyle Factors

No specific dietary or lifestyle factors have been identified as causative. Exercise avoidance may be recommended for high-risk patients, similar to other catecholaminergic arrhythmia syndromes.

### Infectious Agents

Not applicable — no infectious etiology.

---

## 6. Mechanism / Pathophysiology

### Molecular Mechanism: The Ankyrin-B Targeting Pathway

The fundamental molecular defect in ankyrin-B syndrome is the failure to properly target and localize key cardiac ion transporters to their correct membrane domains. Ankyrin-B serves as a critical adapter protein that coordinates the assembly of a macromolecular complex at T-tubule/sarcoplasmic reticulum junctions in cardiomyocytes.

Mohler et al. (2003) described the core mechanism: *"Mutation of ankyrin-B results in disruption in the cellular organization of the sodium pump, the sodium/calcium exchanger, and inositol-1,4,5-trisphosphate receptors (all ankyrin-B-binding proteins), which reduces the targeting of these proteins to the transverse tubules as well as reducing overall protein level"* ([PMID: 12571597](https://pubmed.ncbi.nlm.nih.gov/12571597/)).

### Causal Chain: From Genetic Defect to Arrhythmia

```
ANK2 Loss-of-Function Variant
        │
        ▼
Reduced/Dysfunctional Ankyrin-B Protein
        │
        ├──► Reduced NCX1 membrane targeting
        ├──► Reduced Na⁺/K⁺-ATPase membrane targeting
        ├──► Reduced InsP3R targeting to SR
        └──► Reduced Cav1.3 targeting (in SAN)
        │
        ▼
Disrupted Ion Homeostasis
        │
        ├──► Elevated intracellular [Na⁺] (local domains)
        ├──► Reduced Ca²⁺ extrusion via NCX
        └──► Altered SR Ca²⁺ release via InsP3R/RyR2
        │
        ▼
Intracellular Ca²⁺ Overload
        │
        ├──► Increased Ca²⁺ spark frequency
        ├──► CaMKII activation & RyR2 hyperphosphorylation (pS2814)
        └──► SR Ca²⁺ leak
        │
        ▼
Triggered Arrhythmias
        │
        ├──► Delayed afterdepolarizations (DADs)
        ├──► Early afterdepolarizations (EADs)
        ├──► Catecholaminergic polymorphic VT
        ├──► Sinus node dysfunction (via Cav1.3 loss)
        ├──► Atrial fibrillation (via reduced critical mass for reentry)
        └──► Sudden cardiac death
```

### Calcium Dysregulation

The hallmark cellular phenotype is calcium overload with enhanced spontaneous calcium release. Camors et al. (2012) demonstrated: *"The frequency of spontaneous, diastolic Ca sparks (CaSpF) was significantly higher in intact myocytes from AnkB⁺/⁻ vs. WT myocytes (with and without isoproterenol), even when normalized for SR Ca load"* ([PMID: 22406428](https://pubmed.ncbi.nlm.nih.gov/22406428/)).

### CaMKII-Dependent Pathway

A critical downstream mechanism involves CaMKII-dependent hyperphosphorylation of RyR2. Deangelis et al. (2012) showed: *"The cardiac ryanodine receptor (RyR₂), a validated target of kinase/phosphatase regulation in myocytes, displays abnormal CaMKII-dependent phosphorylation (pS2814 hyperphosphorylation) in ankyrin-B⁺/⁻ heart"* ([PMID: 23059182](https://pubmed.ncbi.nlm.nih.gov/23059182/)). Importantly, CaMKII inhibition rescued the proarrhythmic phenotype, identifying a potential therapeutic target.

### NKA-AnkB-NCX Functional Domain

Bhogal et al. (2019) demonstrated that NKA binding to ankyrin-B creates a local ion regulatory domain: disruption of the NKA/AnkB interaction using disruptor peptides leads to increased rate of Ca²⁺ sparks and waves, with the functional effects mediated through the NKAα2 isoform ([PMID: 30949686](https://pubmed.ncbi.nlm.nih.gov/30949686/)). This establishes that the AnkB/NKAα2/NCX domain controls Ca²⁺ fluxes in cardiomyocytes, and its disruption is an important pathophysiological mechanism.

### Protein Phosphatase 2A (PP2A) Dysregulation

Ankyrin-B targets the PP2A regulatory subunit B56α to the cardiac M-line. Reduced ankyrin-B expression leads to disorganized distribution of B56α ([PMID: 17416611](https://pubmed.ncbi.nlm.nih.gov/17416611/)). PP2A dysfunction may further impair regulation of ion channels and calcium handling proteins.

### EHD3-Dependent Endosomal Trafficking

EHD3 (Eps15 homology domain 3) is essential for membrane protein trafficking in heart. EHD3-deficient hearts phenocopy aspects of ankyrin-B syndrome with *"bradycardia and rate variability, conduction block, and blunted response to adrenergic stimulation"* and *"reduced expression/localization of Na/Ca exchanger and L-type Ca channel type 1.2"* ([PMID: 24759929](https://pubmed.ncbi.nlm.nih.gov/24759929/)).

### Ankyrin-B in Neuronal Function

Beyond cardiac roles, ankyrin-B plays important roles in neural development. It has been demonstrated that the cell adhesion molecule L1 elevates cyclic AMP levels in neurons via ankyrin-B, and *"the loss of ankyrin-B expression converts Ca²⁺-triggered attraction to repulsion when the growth cone migrates via an L1-dependent mechanism"* ([PMID: 19110015](https://pubmed.ncbi.nlm.nih.gov/19110015/)). Additionally, OTUD7A interactions with Ankyrin-B are disrupted in the 15q13.3 microdeletion syndrome, linking ankyrin-B to neurodevelopmental disorders ([PMID: 36604605](https://pubmed.ncbi.nlm.nih.gov/36604605/)).

### Relevant GO Terms for Biological Processes

| GO Term | Description | Relevance |
|---------|-------------|-----------|
| GO:0086001 | Cardiac muscle cell action potential | Primary cellular process affected |
| GO:0006816 | Calcium ion transport | Core mechanism disrupted |
| GO:0005516 | Calmodulin binding | CaMKII pathway |
| GO:0019722 | Calcium-mediated signaling | Downstream signaling |
| GO:0086091 | Regulation of heart rate by cardiac conduction | SAN dysfunction |
| GO:0034765 | Regulation of ion transmembrane transport | Ion channel/transporter targeting |
| GO:0016323 | Basolateral plasma membrane | Subcellular localization |
| GO:0030315 | T-tubule | Primary site of ankyrin-B complex |
| GO:0006874 | Cellular calcium ion homeostasis | Core disrupted process |
| GO:0048738 | Cardiac muscle tissue development | Developmental role |
| GO:0007411 | Axon guidance | Neural ankyrin-B role |

### Relevant Cell Types (CL Terms)

| CL Term | Cell Type | Involvement |
|---------|-----------|-------------|
| CL:0000746 | Cardiac muscle cell (cardiomyocyte) | Primary cell type affected |
| CL:0002072 | Nodal myocyte | Sinus node dysfunction |
| CL:0002071 | Atrial cardiac myocyte | Atrial fibrillation substrate |
| CL:0002066 | Purkinje myocyte | Conduction system involvement |
| CL:0000540 | Neuron | Neural developmental roles |

---

## 7. Anatomical Structures Affected

### Organ Level

- **Primary organ**: Heart (UBERON:0000948)
  - Sinoatrial node (UBERON:0002351) — sinus node dysfunction
  - Cardiac atrium (UBERON:0002081) — atrial fibrillation
  - Cardiac ventricle (UBERON:0002082) — ventricular arrhythmias
  - Cardiac conduction system (UBERON:0002350) — conduction defects
- **Secondary organ involvement**: Brain (UBERON:0000955) — via sudden cardiac death, syncope; neuronal roles of ankyrin-B in axon guidance ([PMID: 19110015](https://pubmed.ncbi.nlm.nih.gov/19110015/))
- **Body systems**: Cardiovascular system (primary), nervous system (secondary via neural ankyrin-B roles)

### Tissue and Cell Level

- **Cardiac muscle tissue** (UBERON:0001133): Primary tissue affected
- **Cardiac conduction system** tissue: Specialized myocytes
- **Skeletal muscle**: Congenital myopathy in ankyrin-B⁻/⁻ mice; SERCA and ryanodine receptor mis-localization ([PMID: 10579720](https://pubmed.ncbi.nlm.nih.gov/10579720/))
- **Thymus**: Major loss of thymic lymphocytes in ankyrin-B⁻/⁻ mice ([PMID: 10579720](https://pubmed.ncbi.nlm.nih.gov/10579720/))

### Subcellular Level

| GO Cellular Component | Structure | Role in Disease |
|----------------------|-----------|-----------------|
| GO:0030315 | T-tubule | Primary site of ankyrin-B complex assembly |
| GO:0016529 | Sarcoplasmic reticulum | Ca²⁺ storage and release; InsP3R/RyR2 localization |
| GO:0030314 | Junctional membrane complex | T-tubule/SR junction — key site of dysfunction |
| GO:0005886 | Plasma membrane | NCX1, NKA targeting |
| GO:0031674 | I band | Ankyrin-B localization overlying M-line |
| GO:0030018 | Z disc | Adjacent cardiomyocyte structural domain |
| GO:0005768 | Endosome | EHD3-dependent trafficking pathway |

### Localization

- **Specific anatomical sites**: Bilateral — the disease affects both sides of the heart
- **No lateralization**: Cardiac involvement is generally symmetric

---

## 8. Temporal Development

### Onset

- **Typical age of onset**: Highly variable — congenital/neonatal (in severe cases with sinus node dysfunction) to adult-onset (atrial fibrillation, late-presenting arrhythmias)
- **Onset pattern**: Insidious; many carriers remain asymptomatic until triggered by catecholaminergic stress or medication exposure
- In the Japanese cohort, affected patients ranged from age 0 to 61 years ([PMID: 27784853](https://pubmed.ncbi.nlm.nih.gov/27784853/))
- Sinus node dysfunction may present in childhood with severe bradycardia
- Atrial fibrillation and conduction disease tend to be age-dependent and progressive

### Progression

- **Disease course**: Chronic, lifelong with episodic arrhythmia events
- **Progression pattern**: Some phenotypes (conduction disease, atrial fibrillation) are progressive and age-related
- In one family, sisters carrying only ANK2-E1813K showed *"age-related conduction disease"* ([PMID: 30929919](https://pubmed.ncbi.nlm.nih.gov/30929919/))
- The common L1622I variant is associated with enhanced cardiac contractility but also premature senescence ([PMID: 17940615](https://pubmed.ncbi.nlm.nih.gov/17940615/))
- **Disease duration**: Lifelong genetic condition; arrhythmic events are episodic
- **Disease stages**: Not formally staged; ranges from subclinical carrier to symptomatic arrhythmia to sudden cardiac death

### Critical Periods

- **Neonatal period**: Severe ankyrin-B deficiency (homozygous or compound heterozygous) is neonatal lethal in mice
- **Periods of catecholaminergic stress**: Exercise, emotional stress, and surgery represent windows of vulnerability
- **Drug exposure**: Initiation of QT-prolonging medications represents a critical risk period
- **Myocardial ischemia**: Ankyrin-B remodeling following myocardial infarction may amplify arrhythmic risk ([PMID: 19394342](https://pubmed.ncbi.nlm.nih.gov/19394342/))

---

## 9. Inheritance and Population

### Inheritance Pattern

- **Mode**: Autosomal dominant (AD)
- **Penetrance**: Incomplete — many variant carriers are asymptomatic
- **Expressivity**: Highly variable — even within the same family, individuals may manifest different arrhythmia phenotypes
- **Genetic anticipation**: Not documented
- **Germline mosaicism**: Not specifically documented, but possible given incomplete penetrance patterns
- **Functional consequence**: Loss of function (haploinsufficiency)

### Epidemiology

- **Prevalence**: Unknown; classified as a rare disease
- **Incidence**: Unknown
- Among 535 Japanese IPAS probands, ANK2 mutations were found in 2.2% ([PMID: 27784853](https://pubmed.ncbi.nlm.nih.gov/27784853/))
- Among 541 LQTS patients, ANK2 variants were found in 3.3% of genotype-negative cases ([PMID: 16253912](https://pubmed.ncbi.nlm.nih.gov/16253912/))

### Population Demographics

- **Ethnic variation**: Significant allele frequency differences exist across populations. The L1622I variant prevalence ranges from 2% in Europeans to 8% in West Africans ([PMID: 17940615](https://pubmed.ncbi.nlm.nih.gov/17940615/))
- **Haplotype structure**: An evaluation of variation and haplotype structure in *ANK2* across four populations (African-American, European American, Han Chinese, Mexican American) revealed *"significant allele-frequency differences between populations and clear differences in haplotype structure"* ([PMID: 19530973](https://pubmed.ncbi.nlm.nih.gov/19530973/))
- **First Nations populations**: A novel disease-causing *ANK2* variant was identified in First Nations families of Northern British Columbia, where long QT syndrome is approximately 15× more common than globally ([PMID: 28196901](https://pubmed.ncbi.nlm.nih.gov/28196901/))
- **Sex ratio**: Not well-established; available cohort data suggest both sexes are affected
- **Geographic distribution**: Global; variant frequencies vary across ancestral populations

---

## 10. Diagnostics

### Clinical Tests

#### Electrophysiology
- **12-lead ECG**: May show sinus bradycardia, prolonged QTc (variable), conduction delays
  - QT prolongation is NOT a consistent feature — this distinguishes ankyrin-B syndrome from classical LQTS
- **Holter monitoring**: Sinus node dysfunction, heart rate variability, intermittent arrhythmias
- **Exercise stress testing**: Catecholamine-provoked arrhythmias; blunted chronotropic response
- **Electrophysiology study**: May reveal sinus node dysfunction, AV conduction abnormalities

#### Imaging
- **Echocardiography**: Generally normal cardiac structure; may reveal cardiomyopathy in advanced/severe cases
- **Cardiac MRI**: To exclude structural heart disease

#### Biomarkers
- No specific circulating biomarkers established for ANK2 Ankyrin-B Syndrome

### Genetic Testing

- **Recommended approach**: Next-generation sequencing-based arrhythmia gene panels or whole exome sequencing
- **Gene panels**: *ANK2* is included in many inherited arrhythmia panels, though ClinGen has questioned its inclusion in standard LQTS panels
- **Single gene testing**: Sanger sequencing of *ANK2* (historically used)
- **Whole exome sequencing**: Useful when gene panels are negative; may identify novel variants
- **Whole genome sequencing**: Can detect structural variants including chromosomal translocations
- **Functional characterization**: Given the high frequency of ANK2 variants in control populations, functional studies in cardiomyocytes are critical for determining pathogenicity of novel variants

**Important caveat**: Given ClinGen's classification of ANK2 as having limited/disputed evidence for LQTS, genetic testing results must be interpreted with extreme caution. Variants should not be used for clinical decision-making without additional supporting evidence ([PMID: 31983240](https://pubmed.ncbi.nlm.nih.gov/31983240/)).

### Clinical Criteria

No standardized diagnostic criteria specific to ankyrin-B syndrome exist. Diagnosis relies on:
1. Clinical presentation with characteristic arrhythmia spectrum (especially multiple phenotypes in same patient/family)
2. Identification of a loss-of-function *ANK2* variant
3. Functional characterization demonstrating variant pathogenicity
4. Family segregation analysis

### Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Classical LQTS (types 1-3) | Consistent QT prolongation; specific channel mutations (KCNQ1, KCNH2, SCN5A) |
| Brugada syndrome | ST-segment elevation in V1-V3; SCN5A mutations |
| CPVT (RYR2-related) | Bidirectional VT; isolated calcium channel defect |
| Sick sinus syndrome (non-genetic) | Typically acquired; absence of other arrhythmia features; older age |
| Timothy syndrome | Syndactyly; CACNA1C mutations; multisystem |
| Andersen-Tawil syndrome | Periodic paralysis; dysmorphic features; KCNJ2 mutations |

### Screening

- **Cascade screening**: Recommended for all first-degree relatives of identified carriers
- **Newborn screening**: Not currently included in standard newborn screening programs
- **Carrier screening**: Not included in standard carrier screening panels

---

## 11. Outcome/Prognosis

### Survival and Mortality

- **Sudden cardiac death risk**: Present but not quantified precisely; family histories frequently include sudden death
- **Life expectancy**: Variable; with appropriate treatment (pacemakers, ICDs, drug avoidance), life expectancy may be near-normal in many patients
- The original LQT4 family had a significant history of sudden death across multiple generations ([PMID: 12571597](https://pubmed.ncbi.nlm.nih.gov/12571597/))
- Seven of 12 ANK2 mutation-positive patients in the Japanese cohort had documented malignant ventricular tachyarrhythmias ([PMID: 27784853](https://pubmed.ncbi.nlm.nih.gov/27784853/))

### Morbidity

- Sinus node dysfunction requiring pacemaker implantation
- Atrial fibrillation requiring anticoagulation and rate/rhythm control
- Restriction of physical activity in high-risk patients
- Psychological burden of sudden death risk
- Recurrent syncope from ventricular arrhythmias

### Disease Complications

- **Cardiac**: Heart failure (accelerated in βII spectrin-deficient mice; [PMID: 25632041](https://pubmed.ncbi.nlm.nih.gov/25632041/)), stroke from atrial fibrillation, cardiac arrest
- **Premature senescence**: The L1622I variant is associated with premature senescence alongside enhanced contractility ([PMID: 17940615](https://pubmed.ncbi.nlm.nih.gov/17940615/))

### Prognostic Factors

- **Variant severity**: Severe loss-of-function variants (E1425G, V1516D) associated with worse outcomes ([PMID: 17242276](https://pubmed.ncbi.nlm.nih.gov/17242276/))
- **Compound genetic hits**: Co-occurrence of ANK2 and KCNH2 variants leads to markedly severe phenotype ([PMID: 30929919](https://pubmed.ncbi.nlm.nih.gov/30929919/))
- **Catecholaminergic provocation**: Stress-induced arrhythmias predict higher risk
- **Family history**: Presence of sudden cardiac death in family members
- **Age**: Conduction disease and atrial fibrillation phenotypes are progressive with age

---

## 12. Treatment

### Pharmacotherapy

#### Beta-Blockers (MAXO:0000169 — beta-adrenergic receptor antagonist therapy)
- **Rationale**: Catecholaminergic arrhythmias suggest benefit from beta-blockade
- **Evidence**: Metoprolol prevented stress-induced arrhythmias in AnkB p.Q1283H knock-in mice: *"ANK2 p.Q1283H is a disease-associated variant that confers susceptibility to stress-induced arrhythmias, which may be prevented by the administration of metoprolol or flecainide"* ([PMID: 30571258](https://pubmed.ncbi.nlm.nih.gov/30571258/))
- **Clinical use**: First-line therapy for patients with catecholaminergic arrhythmias; caution needed if significant bradycardia is present

#### Flecainide (MAXO:0001298 — antiarrhythmic drug therapy)
- **Rationale**: Sodium channel blockade; reduces triggered activity
- **Evidence**: Effective in preventing arrhythmias in the Q1283H mouse model ([PMID: 30571258](https://pubmed.ncbi.nlm.nih.gov/30571258/))
- **Clinical use**: May be used as adjunct or alternative to beta-blockers

#### QT-Prolonging Drug Avoidance (MAXO:0000883 — drug avoidance)
- *"The management of Ankyrin-B syndrome may include avoidance of QT prolonging medications"* ([PMID: 25456501](https://pubmed.ncbi.nlm.nih.gov/25456501/))
- Patients should be provided with a list of drugs to avoid (www.crediblemeds.org)

### Device Therapy

#### Permanent Pacemaker (MAXO:0000477 — cardiac pacemaker implantation)
- Indicated for symptomatic sinus node dysfunction with severe bradycardia
- May also be needed to enable beta-blocker therapy without exacerbating bradycardia

#### Implantable Cardioverter-Defibrillator (MAXO:0000451 — implantable cardioverter defibrillator therapy)
- Indicated for high-risk patients with history of ventricular tachycardia/fibrillation or survived cardiac arrest
- *"insertion of a permanent pacemaker for sinus node dysfunction, or a cardioverter defibrillator for those at high-risk of sudden death from torsades de pointes"* ([PMID: 25456501](https://pubmed.ncbi.nlm.nih.gov/25456501/))

### Experimental / Preclinical Approaches

#### CaMKII Inhibition
- CaMKII inhibition rescues proarrhythmic phenotypes in the ankyrin-B⁺/⁻ model ([PMID: 23059182](https://pubmed.ncbi.nlm.nih.gov/23059182/))
- Represents a potential targeted therapy addressing the core downstream mechanism
- No clinical trials currently registered for CaMKII inhibitors in ankyrin-B syndrome

#### Gene Therapy
- No gene therapy approaches have been developed for ANK2 Ankyrin-B Syndrome
- The large size of the ANK2 gene (>400 kb genomic; ~12 kb mRNA for 220 kDa isoform) presents challenges for AAV-based gene replacement

### Treatment Algorithm

```
ANK2 Variant Identified
        │
        ├──► Functional Assessment (LOF severity)
        │
        ├──► Asymptomatic Carrier
        │       ├── Avoid QT-prolonging drugs
        │       ├── Periodic ECG/Holter monitoring
        │       └── Family cascade screening
        │
        ├──► Sinus Node Dysfunction
        │       ├── Symptomatic bradycardia → Permanent pacemaker
        │       └── Beta-blocker (caution re: bradycardia)
        │
        ├──► QT Prolongation / Ventricular Arrhythmias
        │       ├── Beta-blocker (first-line)
        │       ├── Flecainide (adjunct)
        │       ├── Avoid QT-prolonging drugs
        │       └── ICD if high risk / prior cardiac arrest
        │
        └──► Atrial Fibrillation
                ├── Rate/rhythm control per standard guidelines
                └── Anticoagulation per CHA₂DS₂-VASc score
```

---

## 13. Prevention

### Primary Prevention

- **Genetic counseling** (MAXO:0000079): For families with known *ANK2* variants; autosomal dominant with 50% transmission risk to each offspring
- **Cascade genetic screening**: Testing at-risk family members for the familial variant
- **Prenatal/preimplantation genetic diagnosis**: Technically feasible for known familial variants, though the variable expressivity and incomplete penetrance complicate reproductive counseling

### Secondary Prevention (Early Detection)

- **ECG screening**: Regular ECG monitoring for identified carriers
- **Drug avoidance**: Strict avoidance of QT-prolonging medications (www.crediblemeds.org)
- **Activity modification**: Avoidance of intense exercise in high-risk individuals
- **Regular cardiac monitoring**: Periodic ECG, Holter monitoring, and exercise stress testing

### Tertiary Prevention (Complication Prevention)

- **Beta-blocker therapy**: Reduces arrhythmia recurrence
- **Device therapy**: Pacemakers prevent bradycardia-related events; ICDs prevent sudden death
- **Patient education**: Awareness of triggers and emergency protocols
- **Anticoagulation**: For patients with atrial fibrillation to prevent stroke

### Counseling

Genetic counseling is essential and should cover:
- Autosomal dominant inheritance with 50% recurrence risk
- Incomplete penetrance — a positive genetic test does not guarantee symptomatic disease
- Variable expressivity — family members with the same variant may have different phenotypes
- Importance of cascade screening for at-risk relatives
- Reproductive options including preimplantation genetic testing

---

## 14. Other Species / Natural Disease

### Species Affected

No naturally occurring ankyrin-B cardiac disease has been documented in non-human species in clinical veterinary literature. However, the *Ank2* gene is highly conserved across vertebrates and invertebrates.

| Species | Gene | NCBI Taxon | Notes |
|---------|------|-----------|-------|
| *Mus musculus* (mouse) | *Ank2* | NCBITaxon:10090 | Extensive model organism studies |
| *Rattus norvegicus* (rat) | *Ank2* | NCBITaxon:10116 | Used in electrophysiology studies |
| *Danio rerio* (zebrafish) | *ank2a/ank2b* | NCBITaxon:7955 | Orthologous genes present |
| *Drosophila melanogaster* | *Ank2* | NCBITaxon:7227 | Neural ankyrin function studied |
| *Caenorhabditis elegans* | *unc-44* | NCBITaxon:6239 | Neuronal ankyrin ortholog |

### Comparative Biology

Ankyrin-B function is evolutionarily conserved across metazoans. The protein's roles in membrane protein targeting and calcium homeostasis appear conserved from invertebrates to humans, though the specific cardiac arrhythmia phenotype is unique to organisms with complex cardiac electrophysiology. The *unc-44* ortholog in *C. elegans* plays roles in neuronal polarity, and *Drosophila* Ank2 is essential for axonal integrity, highlighting the conserved neuronal function of the ankyrin family.

### Zoonotic and Transmission Considerations

Not applicable — ANK2 Ankyrin-B Syndrome is a non-infectious genetic disorder.

---

## 15. Model Organisms

### Mouse Models

#### Ankyrin-B Heterozygous (AnkB⁺/⁻) Knockout

- **Type**: Conventional heterozygous knockout
- **Phenotype recapitulation**: Phenocopies major features of human ankyrin-B syndrome
  - Sinus node dysfunction with severe bradycardia and rate variability
  - Susceptibility to ventricular arrhythmias with catecholaminergic stimulation
  - Increased Ca²⁺ spark frequency and afterdepolarizations
  - Reduced NCX, NKA, and InsP3R membrane expression
- **Key references**: [PMID: 15178757](https://pubmed.ncbi.nlm.nih.gov/15178757/), [PMID: 18832177](https://pubmed.ncbi.nlm.nih.gov/18832177/), [PMID: 22406428](https://pubmed.ncbi.nlm.nih.gov/22406428/)
- **Limitations**: Heterozygous knockout may overestimate penetrance relative to human point mutations

#### Ankyrin-B Homozygous (AnkB⁻/⁻) Knockout

- **Phenotype**: Neonatal lethal with congenital myopathy and major thymic lymphocyte loss ([PMID: 10579720](https://pubmed.ncbi.nlm.nih.gov/10579720/))
- **Use**: Studying ankyrin-B's essential developmental roles; cell-based rescue experiments
- **Key finding**: Mis-sorting of SERCA2 and RyR2 in cardiomyocytes rescued by 220-kDa ankyrin-B expression

#### AnkB p.E1458G Knock-in (modeling human E1425G)

- **Type**: Knock-in of the original disease-causing variant
- **Phenotype**: At baseline, young mice show mild phenotype; stress reveals cardiac structural and electrical phenotypes ([PMID: 37182735](https://pubmed.ncbi.nlm.nih.gov/37182735/))
- **Significance**: First direct test of a human ANK2 disease variant in vivo; demonstrates incomplete penetrance in animal model, paralleling human disease

#### AnkB p.Q1283H Knock-in

- **Type**: Knock-in of human disease-associated variant
- **Phenotype**: Stress-induced arrhythmias; loss of local PP2A activity causes RyR2 hyperphosphorylation
- **Therapeutic finding**: Arrhythmias *"may be prevented by the administration of metoprolol or flecainide"* ([PMID: 30571258](https://pubmed.ncbi.nlm.nih.gov/30571258/))
- **Significance**: Demonstrated therapeutic potential and identified PP2A/RyR2 as key pathomechanism

#### AnkB p.L1622I Knock-in

- **Type**: Knock-in of common human variant
- **Phenotype**: Changes in heart rate, AV and intraventricular conduction, altered repolarization, catecholamine-dependent arrhythmias, increased action potential duration, severe afterdepolarizations ([PMID: 27298202](https://pubmed.ncbi.nlm.nih.gov/27298202/))
- **Significance**: Demonstrated that a common population variant can confer in vivo arrhythmia risk

#### Cardiac-Specific βII Spectrin Knockout

- **Phenotype**: Lethal arrhythmias, aberrant calcium handling, abnormal expression/localization of NCX, RyR2, ankyrin-B, accelerated heart failure ([PMID: 25632041](https://pubmed.ncbi.nlm.nih.gov/25632041/))
- **Significance**: Validates the ankyrin-B/βII spectrin pathway in cardiac physiology

#### EHD3 Knockout (global and cardiac-specific)

- **Phenotype**: Bradycardia, rate variability, conduction block, reduced NCX and Cav1.2 expression ([PMID: 24759929](https://pubmed.ncbi.nlm.nih.gov/24759929/))
- **Significance**: Identifies endosomal trafficking as a critical component of the ankyrin-B pathway

### In Vitro Models

- **Primary neonatal cardiomyocytes** from AnkB⁺/⁻ and AnkB⁻/⁻ mice: Used extensively for protein localization, calcium imaging, and rescue experiments ([PMID: 14722080](https://pubmed.ncbi.nlm.nih.gov/14722080/), [PMID: 15262991](https://pubmed.ncbi.nlm.nih.gov/15262991/), [PMID: 11781319](https://pubmed.ncbi.nlm.nih.gov/11781319/))
- **Adult ventricular myocytes**: Used for electrophysiology, calcium spark measurements, and action potential recordings ([PMID: 22406428](https://pubmed.ncbi.nlm.nih.gov/22406428/))
- **HEK293 cells**: Used for heterologous expression studies (e.g., KCNH2 trafficking with ANK2 variants; [PMID: 30929919](https://pubmed.ncbi.nlm.nih.gov/30929919/))
- **Xenopus oocytes**: Used for voltage-clamp recordings of KCNH2 with ANK2 co-expression
- **iPSC-derived neurons**: Used in 15q13.3 microdeletion studies involving OTUD7A-ankyrin interactions ([PMID: 36604605](https://pubmed.ncbi.nlm.nih.gov/36604605/))
- **Primary lymphoblasts**: Used to confirm reduced ankyrin-B expression in translocation carriers ([PMID: 27916589](https://pubmed.ncbi.nlm.nih.gov/27916589/))

### Computational Models

- **Ventricular myocyte electrophysiology models**: Used to dissect the distinct contributions of NCX and NKA defects to calcium overload and afterdepolarizations; showed that NCX and NKA play *"related, yet distinct, roles in intracellular Ca²⁺ accumulation, sarcoplasmic reticulum Ca²⁺ overload, and afterdepolarization generation"* ([PMID: 20729400](https://pubmed.ncbi.nlm.nih.gov/20729400/))
- **SAN node models**: Predict that Cav1.3 loss causes pacemaker slowing and exit block; atrial models predict reduced critical mass for reentrant AF ([PMID: 23436330](https://pubmed.ncbi.nlm.nih.gov/23436330/))

---

## Key Evidence Base: Literature Summary

| PMID | Year | Key Contribution | Evidence Type |
|------|------|-----------------|---------------|
| [12571597](https://pubmed.ncbi.nlm.nih.gov/12571597/) | 2003 | Original identification of ANK2 E1425G causing LQT4 | Human genetic + mouse model |
| [15178757](https://pubmed.ncbi.nlm.nih.gov/15178757/) | 2004 | Reclassification as "ankyrin-B syndrome" distinct from classical LQTS | Human clinical + mouse model |
| [16253912](https://pubmed.ncbi.nlm.nih.gov/16253912/) | 2006 | High frequency of ANK2 variants in control populations | Human genetic |
| [17242276](https://pubmed.ncbi.nlm.nih.gov/17242276/) | 2007 | Spectrum of LOF severity across 9 ANK2 variants | In vitro (cardiomyocytes) |
| [17940615](https://pubmed.ncbi.nlm.nih.gov/17940615/) | 2007 | L1622I as balanced variant; enhanced contractility + senescence risk | Human population + mouse |
| [18832177](https://pubmed.ncbi.nlm.nih.gov/18832177/) | 2008 | Highly penetrant SND mapped to ANK2; Cav1.3 mechanism | Human genetic + mouse model |
| [22406428](https://pubmed.ncbi.nlm.nih.gov/22406428/) | 2012 | Enhanced Ca²⁺ spark frequency in AnkB⁺/⁻ myocytes | Mouse (cellular) |
| [23059182](https://pubmed.ncbi.nlm.nih.gov/23059182/) | 2012 | CaMKII-dependent RyR2 hyperphosphorylation; CaMKII inhibition rescue | Mouse model |
| [23436330](https://pubmed.ncbi.nlm.nih.gov/23436330/) | 2013 | Computational model: Cav1.3 loss → AF susceptibility | Computational |
| [25632041](https://pubmed.ncbi.nlm.nih.gov/25632041/) | 2015 | βII spectrin/ankyrin-B interaction in arrhythmogenesis | Human + mouse |
| [27298202](https://pubmed.ncbi.nlm.nih.gov/27298202/) | 2016 | L1622I knock-in mouse: in vivo arrhythmia phenotypes | Mouse knock-in |
| [27916589](https://pubmed.ncbi.nlm.nih.gov/27916589/) | 2016 | Chromosomal translocation as novel mechanism | Human genetic |
| [27784853](https://pubmed.ncbi.nlm.nih.gov/27784853/) | 2016 | Phenotypic variability in Japanese IPAS cohort | Human clinical |
| [28765088](https://pubmed.ncbi.nlm.nih.gov/28765088/) | 2017 | Comprehensive review of ankyrin-B in cardiovascular disease | Review |
| [30571258](https://pubmed.ncbi.nlm.nih.gov/30571258/) | 2018 | Q1283H knock-in: metoprolol and flecainide efficacy | Mouse knock-in |
| [30929919](https://pubmed.ncbi.nlm.nih.gov/30929919/) | 2019 | ANK2-KCNH2 functional interaction aggravating LQTS | Human + in vitro |
| [30949686](https://pubmed.ncbi.nlm.nih.gov/30949686/) | 2019 | NKAα2/AnkB/NCX functional domain in cardiomyocytes | Mouse (cellular) |
| [31983240](https://pubmed.ncbi.nlm.nih.gov/31983240/) | 2020 | ClinGen reappraisal: ANK2 limited/disputed for LQTS | Expert panel evaluation |
| [34557911](https://pubmed.ncbi.nlm.nih.gov/34557911/) | 2022 | ClinGen: ANK2 variants too common for CPVT causation | Expert panel evaluation |
| [37182735](https://pubmed.ncbi.nlm.nih.gov/37182735/) | 2023 | E1458G knock-in mouse: stress-dependent penetrance | Mouse knock-in |

---

## Limitations and Knowledge Gaps

1. **Incomplete penetrance mechanisms unknown**: The molecular basis for why some ANK2 LOF variant carriers are asymptomatic while others have severe disease is not understood. Modifier genes, epigenetic factors, and environmental modulators likely contribute but are not characterized.

2. **ClinGen dispute creates clinical confusion**: The classification of ANK2 as having "limited/disputed evidence" for LQTS creates a challenging clinical scenario where strong experimental evidence coexists with population-level concerns about variant pathogenicity. A revised framework beyond traditional channelopathy classification may be needed.

3. **Absence of natural history studies**: No prospective longitudinal cohort studies have been conducted specifically for ankyrin-B syndrome. The natural history, penetrance rates, and complication rates remain poorly defined.

4. **Limited genotype-phenotype correlations**: While variant severity has been characterized in vitro, the clinical correlation remains imprecise. The same variant can produce different phenotypes in different family members.

5. **No established prevalence data**: The true population prevalence of clinically significant ANK2 variants is unknown, complicated by the high frequency of ANK2 variants in control populations.

6. **Neurological and extracardiac roles underexplored**: Ankyrin-B has critical functions in neurons (axon guidance, growth cone navigation) and other tissues (skeletal muscle, thymus, pancreatic β-cells), but potential extracardiac manifestations of ANK2 variants in humans are largely unexplored.

7. **No disease-specific biomarkers**: There are no circulating biomarkers to identify at-risk individuals or monitor disease progression beyond ECG parameters.

8. **Treatment evidence limited to preclinical data**: Beta-blocker and flecainide efficacy has been demonstrated only in mouse knock-in models; no clinical trials have been conducted specifically for ankyrin-B syndrome.

9. **Epigenetic regulation unknown**: While alternative splicing of ankyrin-B is documented ([PMID: 18782775](https://pubmed.ncbi.nlm.nih.gov/18782775/)), the epigenetic regulation of *ANK2* expression and its contribution to disease variability remains unexplored.

10. **Acquired ankyrin-B dysfunction**: Post-myocardial infarction remodeling of ankyrin-B has been observed, but the clinical significance of acquired ankyrin-B dysfunction in common cardiac disease is unclear.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective international registry**: Establish an international ANK2 variant carrier registry to collect standardized phenotype data, track natural history, and define penetrance rates across variants and populations.

2. **Functional classification pipeline**: Develop a high-throughput iPSC-cardiomyocyte assay platform to systematically classify all reported ANK2 variants by functional severity (wild-type, mild LOF, severe LOF), enabling evidence-based clinical interpretation.

3. **CaMKII inhibitor clinical development**: Given the strong preclinical evidence that CaMKII inhibition rescues arrhythmia phenotypes in AnkB⁺/⁻ mice ([PMID: 23059182](https://pubmed.ncbi.nlm.nih.gov/23059182/)), pursue pharmacological development of CaMKII-selective inhibitors for clinical testing in ankyrin-B syndrome.

4. **Modifier gene discovery**: Perform whole-genome sequencing and genome-wide association studies in phenotyped ANK2 variant carriers to identify genetic modifiers of penetrance and expressivity.

5. **Extracardiac phenotyping**: Systematically evaluate neurological, musculoskeletal, and immune function in ANK2 variant carriers to determine whether extracardiac manifestations observed in mouse models (neonatal myopathy, thymic lymphocyte loss, neuronal defects) translate to subclinical human phenotypes.

6. **Population-specific studies**: Conduct targeted studies in populations with high ANK2 variant frequency (West African, First Nations) to determine the clinical significance of common variants like L1622I in these ancestral contexts and whether additional genetic or environmental modifiers explain variable risk.

7. **Updated ClinGen gene curation**: Collaborate with ClinGen to refine the gene-disease relationship using the "ankyrin-B syndrome" framework rather than classical LQTS/CPVT categories, which may more accurately capture the evidence and prevent misleading clinical interpretations.

8. **Single-cell and spatial transcriptomics**: Perform single-cell RNA-seq and spatial transcriptomics on AnkB⁺/⁻ hearts at multiple developmental stages to identify cell-type-specific transcriptional changes, potential compensatory mechanisms, and novel therapeutic targets.

9. **Clinical trial for beta-blockers**: Design a prospective clinical trial of beta-blocker therapy in ANK2 variant carriers with documented arrhythmias, using validated endpoints including arrhythmia burden reduction and quality of life measures.

10. **Gene therapy exploration**: Investigate AAV-based or RNA-based therapeutic strategies for ankyrin-B restoration, potentially using truncated functional domains or antisense oligonucleotides to enhance expression from the remaining wild-type allele.

---

*Report generated: 2026-05-05*
*Based on systematic review of 43 peer-reviewed publications*
*Disease: ANK2 Ankyrin-B Syndrome (MONDO:0010958; OMIM:600919)*
