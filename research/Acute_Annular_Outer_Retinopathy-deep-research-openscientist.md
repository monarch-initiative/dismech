---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-04T23:29:12.737206'
end_time: '2026-05-04T23:57:26.565227'
duration_seconds: 1693.83
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Annular Outer Retinopathy
  mondo_id: ''
  category: Complex
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
citation_count: 27
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Annular Outer Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acute Annular Outer Retinopathy** covering all of the
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

# Comprehensive Disease Characterization Report: Acute Annular Outer Retinopathy (AAOR)

---

## Summary

**Acute Annular Outer Retinopathy (AAOR)** is an ultra-rare inflammatory retinopathy first described by Fekrat et al. in 2000, now recognized as a distinct variant within the Acute Zonal Occult Outer Retinopathy (AZOOR) spectrum. The disease is characterized by the acute onset of photopsia, scotoma, and visual field loss in association with a pathognomonic annular white ring of outer retinal opacification visible on fundoscopy. AAOR primarily affects young to middle-aged adults (typical age range 18-56 years), with a strong female predominance (male-to-female ratio approximately 1:3). The pathogenesis is believed to be autoimmune in nature, targeting photoreceptor outer segments, as supported by the detection of antiretinal antibodies in affected patients.

The clinical course of AAOR follows three distinct stages: an acutely progressive stage (1-3 weeks), a stationary stage (3 weeks to 3 months), and an atrophic stage (>3 months). Visual prognosis is critically dependent on whether the macula is involved -- eyes without macular involvement typically retain 20/20 visual acuity, while those with macular involvement may deteriorate to hand-motion or 20/400 vision. Despite numerous therapeutic attempts including corticosteroids, immunosuppressants, and antiviral agents, no treatment has been proven effective in controlled trials. The disease remains poorly understood at the molecular level, with no identified causal genes, no established inheritance pattern, and an extremely low prevalence that has precluded large-scale epidemiological or genomic studies.

This report synthesizes evidence from 49 reviewed publications, including the original case series, the largest multicenter cohort studies, and the most recent multimodal imaging analyses, to provide a comprehensive characterization of AAOR across 15 disease domains.

---

## 1. Disease Information

### Overview

Acute Annular Outer Retinopathy (AAOR) is a rare inflammatory disease of the outer retina, classified within the white dot syndrome (WDS) family and the AZOOR complex. It was first described as a distinct entity by Fekrat et al. (2000), who reported four healthy patients who developed "acute onset of visual field loss associated with a localized, white annular outer retinopathy" ([PMID: 11078842](https://pubmed.ncbi.nlm.nih.gov/11078842/)). AAOR is now considered a clinical variant of AZOOR, which was originally described by Gass in 1993 ([PMID: 8340485](https://pubmed.ncbi.nlm.nih.gov/8340485/)).

### Key Identifiers

| Database | Identifier | Notes |
|----------|-----------|-------|
| **OMIM** | Not assigned | Too rare for independent OMIM entry |
| **Orphanet** | Not independently listed | Falls under AZOOR spectrum |
| **ICD-10** | H35.8 (Other specified retinal disorders) | No specific code for AAOR |
| **ICD-11** | 9B76.Y (Other specified disorders of retina) | No specific code for AAOR |
| **MeSH** | Not independently indexed | Indexed under broader terms |
| **MONDO** | Not assigned | |

### Synonyms and Alternative Names

- Acute Annular Outer Retinopathy (AAOR) -- primary name
- Acute Outer Retinopathy (AOR) -- expanded spectrum term, proposed 2025
- AZOOR variant / AZOOR with annular pattern
- Annular variant of AZOOR
- Part of: AZOOR complex, White dot syndromes

### Information Source

All information is derived primarily from aggregated disease-level resources (case reports and small case series). The largest published series includes 23 patients (Ramtohul et al. 2025, [PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/)) and 9 patients (Chen et al. 2025, [PMID: 40446848](https://pubmed.ncbi.nlm.nih.gov/40446848/)).

---

## 2. Etiology

### Disease Causal Factors

The etiology of AAOR remains **unknown** ([PMID: 30455116](https://pubmed.ncbi.nlm.nih.gov/30455116/)). The condition is considered to have a complex, non-genetic, likely autoimmune or post-infectious pathogenesis. Key etiological hypotheses include:

**Autoimmune mechanism**: Tagami et al. (2014) demonstrated that "AZOOR could be an autoimmune disease. All AZOOR patients tested using molecular biological methods had antiretinal antigens" ([PMID: 25266678](https://pubmed.ncbi.nlm.nih.gov/25266678/)). Autologous antibodies targeting outer retinal photoreceptors were found in all 5 AZOOR patients studied. Shimazaki et al. (2008) also reported the association of antiretinal antibodies specifically in AAOR ([PMID: 18195232](https://pubmed.ncbi.nlm.nih.gov/18195232/)).

**Post-viral/post-infectious trigger**: A preceding viral illness has been reported in several cases. Kitamura et al. (2018) described a 56-year-old man who "had fever one month and a half before presenting" and "noticed bilateral visual loss after lowering of fever" ([PMID: 30079710](https://pubmed.ncbi.nlm.nih.gov/30079710/)). The original AZOOR description by Gass (1993) noted this association frequently ([PMID: 8340485](https://pubmed.ncbi.nlm.nih.gov/8340485/)).

**Possible paraneoplastic association**: Gupta et al. (2022) reported the first case of AAOR in a patient with invasive ductal breast carcinoma, where "the patient presented with photopsias and visual loss approximately 3 weeks prior to a diagnosis of invasive ductal breast carcinoma" ([PMID: 36434575](https://pubmed.ncbi.nlm.nih.gov/36434575/)).

### Risk Factors

#### Genetic Risk Factors
- No genetic risk factors have been identified
- Roy & Dutta Majumder (2024) stated that AZOOR is "distinct from genetic disorders like retinitis pigmentosa, lacks a hereditary basis" ([PMID: 38454854](https://pubmed.ncbi.nlm.nih.gov/38454854/))
- No GWAS or candidate gene studies have been performed for AAOR

#### Environmental/Demographic Risk Factors
- **Age**: Young to middle-aged adults predominantly affected. Chen et al. (2025): ages 18-39 years ([PMID: 40446848](https://pubmed.ncbi.nlm.nih.gov/40446848/)); Ramtohul et al. (2025): mean age 41.8 +/- 18.6 years, range 14-86 ([PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/))
- **Sex**: Female predominance. Monson & Smith (2011): male:female ratio 1:3.2 ([PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/)). Ramtohul et al. (2025): 15 female, 8 male (1:1.875)
- **Race/Ethnicity**: Predominantly affects white/Caucasian individuals ([PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/))
- **Preceding viral illness**: Febrile illness preceding onset reported in multiple cases
- **HIV infection**: Garcia-Torre & Castro-Florez (2019) reported the first AAOR case in an HIV-positive patient ([PMID: 30455116](https://pubmed.ncbi.nlm.nih.gov/30455116/))
- **Malignancy**: Breast carcinoma reported in temporal association ([PMID: 36434575](https://pubmed.ncbi.nlm.nih.gov/36434575/))
- **Epilepsy**: An AZOOR case was reported in a patient with epilepsy, with the authors noting that "epileptic episodes contribute to an inflammatory response both in the brain and the retina" ([PMID: 34833494](https://pubmed.ncbi.nlm.nih.gov/34833494/))

### Protective Factors

No genetic or environmental protective factors have been identified. This reflects the unknown etiology and extreme rarity of the condition.

### Gene-Environment Interactions

Not characterized due to the absence of identified genetic risk factors and the extremely low prevalence of the disease. The disease appears to be entirely acquired rather than inherited.

---

## 3. Phenotypes

### Symptoms and Clinical Signs

The largest multicenter study by Ramtohul et al. (2025) of 23 patients with AOR (38 eyes) quantified presenting symptoms: "photopsia (87%), blurred vision (57%), and scotoma (57%)" ([PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/)).

#### 1. Photopsia (Flashing/Flickering lights)
- **Type**: Symptom (visual)
- **HPO term**: HP:0030786 (Photopsia)
- **Frequency**: 87% of patients ([PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/)); chronic photopsia reported in most patients
- **Onset**: Acute onset, typically the presenting symptom
- **Severity**: Variable; can be persistent
- **Progression**: Often chronic; Gass (1993) noted "most had chronic photopsia" ([PMID: 8340485](https://pubmed.ncbi.nlm.nih.gov/8340485/))
- **QoL impact**: Significant; disturbing visual phenomenon affecting daily activities

#### 2. Visual Field Defects / Scotoma
- **Type**: Clinical sign / Symptom
- **HPO terms**: HP:0000572 (Visual field defect), HP:0000575 (Scotoma), HP:0001133 (Constriction of peripheral visual field)
- **Frequency**: 57% presented with scotoma ([PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/)); blind spot enlargement in 75% of tested eyes ([PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/))
- **Onset**: Acute onset; progressive during the acute phase (1-3 weeks)
- **Severity**: Mild to severe; Gass (1993): "all had permanent visual field loss that in some cases was severe" ([PMID: 8340485](https://pubmed.ncbi.nlm.nih.gov/8340485/))
- **Progression**: Usually stabilizes within 6 months ([PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/)), but long-term progressive atrophy possible over years ([PMID: 23591538](https://pubmed.ncbi.nlm.nih.gov/23591538/))
- **QoL impact**: Major; permanent scotomas affect reading, driving, and spatial navigation

#### 3. Blurred Vision / Decreased Visual Acuity
- **Type**: Symptom
- **HPO terms**: HP:0000505 (Visual impairment), HP:0007663 (Reduced visual acuity)
- **Frequency**: 57% of patients ([PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/))
- **Onset**: Acute onset
- **Severity**: Highly variable depending on macular involvement. Chen et al. (2025): BCVA 20/20 without macular involvement vs. HM-20/400 with macular involvement ([PMID: 40446848](https://pubmed.ncbi.nlm.nih.gov/40446848/)). Monson & Smith (2011): "Visual acuity was 20/40 or better in 74% of tested eyes" ([PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/))
- **QoL impact**: Ranges from minimal to devastating depending on macular involvement

#### 4. Annular White Ring (Outer Retinal Whitening)
- **Type**: Clinical sign (ophthalmoscopic finding)
- **HPO terms**: HP:0007703 (Abnormality of retinal pigmentation) [late stage]
- **Frequency**: Defining feature of AAOR (100% during acute phase)
- **Characteristics**: Gray-white, peripapillary, annular band of deep retinal opacification ([PMID: 11078842](https://pubmed.ncbi.nlm.nih.gov/11078842/)). Chen et al. (2025) noted "advancement of peripapillary annular band" during the acute progressive stage, which disappeared during the stationary stage ([PMID: 40446848](https://pubmed.ncbi.nlm.nih.gov/40446848/))
- **Progression**: Transient; resolves into depigmented areas with scattered pigmentation (atrophic stage)

#### 5. Electroretinographic (ERG) Abnormalities
- **Type**: Laboratory abnormality (electrophysiology)
- **HPO terms**: HP:0000654 (Abnormal ERG), HP:0030464 (Abnormal full-field ERG)
- **Frequency**: 99% of AZOOR patients tested ([PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/))
- **Characteristics**: Reduced amplitudes, predominantly affecting rod-mediated responses in some cases ([PMID: 19847620](https://pubmed.ncbi.nlm.nih.gov/19847620/))
- **Significance**: Critical diagnostic marker; may be abnormal even with normal-appearing fundus

#### 6. Fundus Autofluorescence Abnormalities
- **Type**: Clinical sign (imaging finding)
- **HPO term**: HP:0030624 (Abnormal fundus autofluorescence imaging)
- **Frequency**: Present in virtually all cases on imaging
- **Characteristics**: Hyperautofluorescent ring corresponding to advancing edge of disease; trizonal pattern (hyperautofluorescent, hypoautofluorescent, and normal zones) in chronic stage; ring-like hyperautofluorescent lesions surrounding optic disc in 18% of eyes ([PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/))

#### 7. OCT Abnormalities (Ellipsoid Zone Disruption)
- **Type**: Clinical sign (imaging finding)
- **HPO term**: HP:0030329 (Retinal thinning)
- **Frequency**: Universal on OCT imaging
- **Characteristics**: Absent/disrupted ellipsoid zone (EZ), thinned outer nuclear layer (ONL), angular sign of Henle fiber layer hyperreflectivity (ASHH) ([PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/)), hyperreflective foci in inner retina ([PMID: 30079710](https://pubmed.ncbi.nlm.nih.gov/30079710/)), increased choroidal thickness acutely, decreased choroidal thickness in atrophic stage ([PMID: 40446848](https://pubmed.ncbi.nlm.nih.gov/40446848/))

#### 8. Retinal Pigment Epithelium Changes (Late)
- **Type**: Clinical sign
- **HPO terms**: HP:0007703 (Abnormality of retinal pigmentation), HP:0000580 (Pigmentary retinopathy)
- **Frequency**: Common in late/atrophic stage
- **Progression**: Develops over months to years; Gass (1993): "most had... zones of pigment epithelial atrophy" ([PMID: 8340485](https://pubmed.ncbi.nlm.nih.gov/8340485/))

### Summary of HPO Terms

| HPO Term | ID | Frequency |
|---|---|---|
| Photopsia | HP:0030786 | ~87% |
| Visual field defect | HP:0000572 | ~57% |
| Scotoma | HP:0000575 | ~57% |
| Visual impairment | HP:0000505 | ~57% |
| Abnormal ERG | HP:0000654 | ~99% |
| Abnormal FAF | HP:0030624 | ~100% |
| Retinal thinning | HP:0030329 | ~100% |
| Pigmentary retinopathy | HP:0000580 | Common (late stage) |
| Enlarged blind spot | HP:0030532 | ~75% |

---

## 4. Genetic/Molecular Information

### Causal Genes

**No causal genes have been identified** for AAOR. Roy & Dutta Majumder (2024) explicitly stated the condition is "distinct from genetic disorders like retinitis pigmentosa, lacks a hereditary basis" ([PMID: 38454854](https://pubmed.ncbi.nlm.nih.gov/38454854/)). Ramtohul et al. (2025) performed genetic testing as part of their evaluation but did not identify causal variants ([PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/)).

### Pathogenic Variants

Not applicable; AAOR is not a Mendelian genetic disorder.

### Modifier Genes / Epigenetic Information / Chromosomal Abnormalities

None identified. No epigenetic studies or chromosomal analyses have been performed on AAOR.

### Molecular Findings

The primary molecular finding is the presence of **antiretinal antibodies** in affected patients:

- Tagami et al. (2014) found autologous antibodies targeting outer retinal antigens in all 5 AZOOR patients tested. Immunohistochemical staining revealed the target antigen was present in all photoreceptors ([PMID: 25266678](https://pubmed.ncbi.nlm.nih.gov/25266678/))
- Shimazaki et al. (2008) reported antiretinal antibody association specifically in AAOR ([PMID: 18195232](https://pubmed.ncbi.nlm.nih.gov/18195232/))
- Related work on autoimmune retinopathy has identified recoverin, alpha-enolase, TULP1, and carbonic anhydrase II as retinal autoantigens ([PMID: 40141211](https://pubmed.ncbi.nlm.nih.gov/40141211/), [PMID: 24428923](https://pubmed.ncbi.nlm.nih.gov/24428923/)), though these have not been specifically confirmed in AAOR

---

## 5. Environmental Information

### Environmental Factors

No specific environmental toxins, radiation, pollution, or occupational exposures have been linked to AAOR.

### Lifestyle Factors

No lifestyle factors (smoking, diet, exercise, alcohol consumption) have been identified as contributing factors.

### Infectious Agents

Viral infections are suspected as potential triggers:

- **Preceding febrile illness**: Multiple cases report fever or viral prodrome weeks before onset
- **HIV**: First case of AAOR in an HIV-positive patient reported ([PMID: 30455116](https://pubmed.ncbi.nlm.nih.gov/30455116/)), though "the precise role played by HIV infection or secondary immunosuppression in the development of the AAOR is not known"
- **Coxsackievirus**: In the related condition APMPPE, elevated Coxsackievirus B titers were found in 6 of 7 patients ([PMID: 32834009](https://pubmed.ncbi.nlm.nih.gov/32834009/)), suggesting enteroviruses may serve as immune triggers in white dot syndromes more broadly
- No specific pathogen has been definitively identified as causative in AAOR

---

## 6. Mechanism / Pathophysiology

### Overview of Pathogenic Cascade

The current understanding of AAOR pathophysiology, based primarily on multimodal imaging studies and autoantibody detection, is:

1. **Trigger event** (unknown; possibly viral infection or autoimmune activation)
2. **Primary photoreceptor outer segment damage** (autoimmune-mediated attack on photoreceptors)
3. **Inflammatory phase** with choroidal thickening and advancing annular lesion
4. **Stabilization** with partial recovery possible
5. **Secondary RPE and choriocapillaris involvement** during chronic atrophic phase

### Molecular Pathways

No specific signaling pathways have been definitively implicated. **Autoimmune/inflammatory signaling** is suspected based on:
- Antiretinal antibodies ([PMID: 25266678](https://pubmed.ncbi.nlm.nih.gov/25266678/))
- Response to immunosuppressive therapy in some cases
- Anti-TNF-alpha therapy (adalimumab) showing benefit in AZOOR overlap ([PMID: 23765682](https://pubmed.ncbi.nlm.nih.gov/23765682/))

### Cellular Processes

**Photoreceptor degeneration/apoptosis**: The primary pathology. Herbort et al. (2021) established through multimodal imaging that "the primary damage was identified at the level of the photoreceptor outer segments with an intact choriocapillaris and retinal pigment epithelium (RPE) layer, these structures being only secondarily involved" ([PMID: 34209956](https://pubmed.ncbi.nlm.nih.gov/34209956/)).

Seetharam et al. (2015) confirmed at the structural level: "hyperreflectivity in the outer nuclear layer and the Henle fiber layer along with marked atrophy of the outer retina within the white ring" ([PMID: 25383859](https://pubmed.ncbi.nlm.nih.gov/25383859/)). Importantly, restoration of foveal photoreceptors correlated with visual recovery, supporting the photoreceptor as the critical target.

**Relevant GO terms**: GO:0006915 (apoptotic process), GO:0001895 (retinal homeostasis), GO:0007601 (visual perception)

### Protein Dysfunction

Tagami et al. (2014) found that "the target antigen was present in all photoreceptors of the mouse sensory retina" when testing AZOOR patient sera. Candidate antigens were identified by mass spectrometry but not definitively characterized ([PMID: 25266678](https://pubmed.ncbi.nlm.nih.gov/25266678/)). Related work on autoimmune retinopathy has identified recoverin, alpha-enolase, TULP1, and CRMP-5 as retinal autoantigens ([PMID: 40141211](https://pubmed.ncbi.nlm.nih.gov/40141211/), [PMID: 24428923](https://pubmed.ncbi.nlm.nih.gov/24428923/)).

### Immune System Involvement

**Autoimmunity** is the leading pathogenic hypothesis:
- Antiretinal antibodies found in AZOOR/AAOR patients ([PMID: 25266678](https://pubmed.ncbi.nlm.nih.gov/25266678/), [PMID: 18195232](https://pubmed.ncbi.nlm.nih.gov/18195232/))
- Female predominance (characteristic of autoimmune diseases)
- Some response to immunosuppressive therapy
- Post-infectious trigger consistent with molecular mimicry or immune dysregulation
- Mouse models of recoverin-associated AIR demonstrate complement deposition (C1q, C3), CD4+ T cell and CD68+ macrophage infiltration ([PMID: 21031137](https://pubmed.ncbi.nlm.nih.gov/21031137/))

**Suggested GO terms**: GO:0006955 (immune response), GO:0002377 (immunoglobulin production), GO:0006958 (complement activation, classical pathway), GO:0006959 (humoral immune response)

### Important Mechanistic Distinction

Herbort et al. (2021) critically distinguished AZOOR (including AAOR) from choriocapillaritis diseases (such as multifocal choroiditis, punctate inner choroidopathy), demonstrating that AZOOR "results from a clinicopathological mechanism different from choriocapillaritis diseases" ([PMID: 34209956](https://pubmed.ncbi.nlm.nih.gov/34209956/)). In choriocapillaritis, the primary target is the choroidal vasculature; in AZOOR/AAOR, it is the photoreceptor layer.

### Cell Types Involved

| Cell Type | CL Term | Role |
|---|---|---|
| Photoreceptor (rod) | CL:0000604 | Primary target; rod loss may predominate early |
| Photoreceptor (cone) | CL:0000573 | Secondary/concurrent target |
| Retinal pigment epithelium cell | CL:0002586 | Secondary involvement |
| Muller glia | CL:0000636 | Reactive gliosis |
| T lymphocyte (CD4+) | CL:0000624 | Immune-mediated damage |
| Macrophage (CD68+) | CL:0000235 | Inflammatory infiltration |

### Molecular Profiling

No transcriptomic, proteomic, metabolomic, lipidomic, or epigenomic profiling studies have been performed specifically on AAOR tissue. This represents a major knowledge gap. No single-cell, spatial transcriptomic, or functional genomic screens have been conducted.

### Proposed Causal Chain Diagram

```
TRIGGER PHASE
+-- Viral infection (febrile illness, HIV, unknown pathogen)
+-- Paraneoplastic stimulus (rare; breast carcinoma reported)
+-- Idiopathic immune activation
         |
         v
IMMUNE PHASE
+-- Molecular mimicry or antigen release
+-- Generation of antiretinal autoantibodies
|   +-- Target: photoreceptor outer segment antigens
+-- Complement activation (C1q, C3 deposition)
+-- Cellular immune infiltration (CD4+ T cells, CD68+ macrophages)
         |
         v
ACUTE PROGRESSIVE STAGE (1-3 weeks)
+-- Photoreceptor outer segment destruction (ellipsoid zone loss)
+-- Outer nuclear layer thinning
+-- Annular white ring visible on fundoscopy
+-- Increased choroidal thickness (inflammatory edema)
+-- Hyperautofluorescence at active margins
         |
         v
STATIONARY STAGE (3 weeks - 3 months)
+-- Resolution of annular band
+-- Partial ONL recovery possible
+-- Immune response waning
+-- Beginning of reparative processes
         |
         v
ATROPHIC STAGE (>3 months)
+-- RPE depigmentation and scattered pigmentation
+-- Permanent retinal atrophy
+-- Decreased choroidal thickness
+-- Risk of choroidal neovascularization
+-- Stable visual field defects
```

---

## 7. Anatomical Structures Affected

### Organ Level

- **Primary organ**: Eye (specifically the retina)
  - UBERON:0000966 (retina), UBERON:0000019 (camera-type eye)
- **Body system**: Visual/nervous system
- **Laterality**: Can be unilateral or bilateral. Mrejen et al. (2014): 18 of 30 AZOOR patients had bilateral lesions, mostly asymmetric ([PMID: 24945598](https://pubmed.ncbi.nlm.nih.gov/24945598/)). Ramtohul et al. (2025): 38 eyes from 23 patients (bilateral in many) ([PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/))
- **No secondary organ involvement**: AAOR is confined to the eye

### Tissue and Cell Level

**Tissues affected (in order of involvement):**

| Structure | UBERON Term | Involvement |
|---|---|---|
| Photoreceptor layer of retina | UBERON:0001787 | Primary target -- outer segment destruction |
| Retinal pigment epithelium | UBERON:0001782 | Secondary -- atrophy and depigmentation |
| Choroid | UBERON:0001776 | Thickness changes; secondary atrophy in late stage |
| Optic disc region | UBERON:0001783 | Peripapillary involvement common |
| Macula/fovea | UBERON:0000053 / UBERON:0001785 | Variable involvement; critical for prognosis |

**Cell populations affected:**
- **Photoreceptor cells (rods and cones)**: Primary target -- CL:0000604 (retinal rod cell), CL:0000573 (retinal cone cell)
- **Retinal pigment epithelial cells**: Secondary -- CL:0002586
- Yokoyama et al. (2009) noted "predominant loss of rod-mediated electroretinogram response," suggesting rods may be preferentially affected in some cases ([PMID: 19847620](https://pubmed.ncbi.nlm.nih.gov/19847620/))

### Subcellular Level

- **Photoreceptor outer segments**: Site of primary damage -- GO:0001750 (photoreceptor outer segment)
- **Ellipsoid zone** (photoreceptor inner segment mitochondria): Disrupted on OCT -- GO:0001917 (photoreceptor inner segment)
- **Interdigitation zone** (RPE-photoreceptor interface): Indistinct on imaging ([PMID: 30079710](https://pubmed.ncbi.nlm.nih.gov/30079710/))

### Localization

- **Peripapillary region**: The annular lesion typically originates around the optic disc (UBERON:0001783)
- **Posterior pole/macula**: May or may not be involved; macular involvement determines prognosis (UBERON:0000053, UBERON:0001785)
- **Pattern**: Annular (ring-shaped), expanding centrifugally from the optic disc
- **Lateralization**: Can be unilateral or bilateral, often asymmetric when bilateral

---

## 8. Temporal Development

### Onset

- **Typical age of onset**: Young to middle-aged adults
  - Chen et al. (2025): 18-39 years ([PMID: 40446848](https://pubmed.ncbi.nlm.nih.gov/40446848/))
  - Ramtohul et al. (2025): mean 41.8 years (range 14-86) ([PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/))
  - Monson & Smith (2011): average 36.7 years ([PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/))
  - Fekrat et al. (2000): two patients aged 29/32 and two aged 71/79, suggesting possible bimodal distribution ([PMID: 11078842](https://pubmed.ncbi.nlm.nih.gov/11078842/))
- **Onset pattern**: **Acute** -- sudden onset of symptoms (photopsia, scotoma, visual loss)

### Three-Stage Clinical Course

Chen et al. (2025) provided the first systematic staging of AAOR: "The clinical course was subdivided acutely progressive stage (APS), stationary stage (SS) and atrophic stage (AS) (1-3 weeks, 3 weeks to 3 months and >3 months, respectively)" ([PMID: 40446848](https://pubmed.ncbi.nlm.nih.gov/40446848/)).

| Stage | Duration | Key Features |
|---|---|---|
| **Acutely Progressive (APS)** | 1-3 weeks | Advancing peripapillary annular band; absent ellipsoid zone; increased choroidal thickness; thinned ONL |
| **Stationary (SS)** | 3 weeks - 3 months | Disappearance of annular band; improved ONL |
| **Atrophic (AS)** | >3 months | Depigmentation; scattered pigmentation; retinal atrophy; decreased choroidal thickness |

### Progression

- **Progression rate**: Rapid during acute phase (1-3 weeks), then stabilizes
- **Disease course**: Monophasic in most cases; Monson & Smith (2011): "unusual for visual field loss to continue beyond six months" ([PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/))
- **Disease duration**: Self-limited acute phase; chronic permanent residual damage
- **Long-term**: Hoang et al. (2013) reported 13-year follow-up showing "chorioretinal atrophy progressed significantly" and that "the prognosis of cases with AZOOR should be cautiously considered" ([PMID: 23591538](https://pubmed.ncbi.nlm.nih.gov/23591538/))

### Patterns

- **Remission**: The acute inflammatory phase is self-limited. Partial recovery of photoreceptor function can occur at the fovea; Seetharam et al. (2015) documented "restoration of foveal photoreceptors, which corresponded with visual recovery" ([PMID: 25383859](https://pubmed.ncbi.nlm.nih.gov/25383859/))
- **Recurrence**: Generally considered a monophasic disorder, but recurrent episodes are possible
- **Critical period**: The acute progressive stage (1-3 weeks) represents the window for potential therapeutic intervention

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence**: Unknown; extremely rare. Only approximately 131 cases of AZOOR (including AAOR) were compiled in the English literature by 2011 ([PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/)). AAOR specifically has fewer than 50 reported cases.
- **Incidence**: Not established; too rare for population-based estimates
- Classified as an ultra-rare disease

### Genetic Inheritance

Not applicable: AAOR is not a hereditary disease. Roy & Dutta Majumder (2024): AZOOR "lacks a hereditary basis" ([PMID: 38454854](https://pubmed.ncbi.nlm.nih.gov/38454854/)).

### Population Demographics

| Demographic | Data | Source |
|---|---|---|
| **Sex ratio** | ~1:3.2 (male:female) | [PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/) |
| **Race/ethnicity** | Predominantly Caucasian/white | [PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/) |
| **Age distribution** | 14-86 years; peak in 3rd-4th decades | [PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/) |
| **Geographic distribution** | Worldwide (USA, Europe, Japan, South America) | Multiple sources |

---

## 10. Diagnostics

### Clinical Tests

#### Ophthalmoscopy/Funduscopy
- Acute phase: Gray-white annular band of deep retinal opacification (defining feature of AAOR)
- Late phase: Depigmentation with scattered pigmentation, RPE atrophy
- In classic AZOOR, fundus may appear normal; AAOR is distinguished by visible fundus changes

#### Optical Coherence Tomography (OCT)
- **Critical diagnostic tool**
- Disrupted/absent ellipsoid zone (EZ), thinned outer nuclear layer (ONL), hyperreflectivity in ONL and Henle fiber layer
- Angular sign of Henle fiber layer hyperreflectivity (ASHH) ([PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/), [PMID: 25383859](https://pubmed.ncbi.nlm.nih.gov/25383859/))
- Increased choroidal thickness in acute phase; decreased in chronic phase ([PMID: 40446848](https://pubmed.ncbi.nlm.nih.gov/40446848/))
- Hyperreflective foci in inner retina and indistinct interdigitation zone even in ophthalmoscopically normal areas ([PMID: 30079710](https://pubmed.ncbi.nlm.nih.gov/30079710/))

#### Fundus Autofluorescence (FAF)
- Hyperautofluorescent ring at the advancing edge of disease
- Trizonal pattern in chronic stage: hyperautofluorescent, hypoautofluorescent, and normal zones ([PMID: 24945598](https://pubmed.ncbi.nlm.nih.gov/24945598/), [PMID: 34833494](https://pubmed.ncbi.nlm.nih.gov/34833494/))
- Ring-like hyperautofluorescent lesions surrounding the optic disc in 18% of eyes ([PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/))

#### OCT Angiography (OCTA)
- Enlarged foveal avascular zone, especially in atrophic stage ([PMID: 40446848](https://pubmed.ncbi.nlm.nih.gov/40446848/))
- Useful for detecting choriocapillaris changes and differentiating from choriocapillaritis diseases

#### Fluorescein Angiography (FA) / Indocyanine Green Angiography (ICGA)
- FA: Variable findings; may show transmission defects in areas of RPE atrophy
- ICGA: Can demonstrate choroidal involvement; helps differentiate from choriocapillaritis

#### Visual Field Testing
- Blind spot enlargement (75% of cases, [PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/))
- Scotomas corresponding to areas of photoreceptor damage
- Essential for documenting functional loss and monitoring progression

#### Electroretinography (ERG)
- **Highly sensitive diagnostic test**: abnormal in 99% of AZOOR patients tested ([PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/))
- Full-field ERG: Reduced amplitudes, particularly scotopic responses
- Multifocal ERG: Reduced amplitudes in areas corresponding to scotomas
- May show predominantly rod-mediated loss ([PMID: 19847620](https://pubmed.ncbi.nlm.nih.gov/19847620/))

#### Adaptive Optics Imaging
- Can reveal indistinct cone mosaic patterns in ophthalmoscopically normal areas ([PMID: 30079710](https://pubmed.ncbi.nlm.nih.gov/30079710/))

### Biomarkers
- **Antiretinal antibodies**: Found in AZOOR patients ([PMID: 25266678](https://pubmed.ncbi.nlm.nih.gov/25266678/), [PMID: 18195232](https://pubmed.ncbi.nlm.nih.gov/18195232/)); not yet validated as a clinical biomarker but may support diagnosis

### Genetic Testing
- **Not indicated** for AAOR as it is not a genetic disease
- May be performed to exclude genetic mimics (e.g., retinitis pigmentosa) ([PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/))

### Clinical Criteria

No formally standardized diagnostic criteria exist. Diagnosis is based on:
1. Acute onset of photopsia and/or scotoma
2. Visible annular white ring of outer retinal opacification on funduscopy (distinguishes from classic AZOOR)
3. OCT evidence of outer retinal damage (EZ disruption, ONL thinning)
4. ERG abnormalities
5. FAF changes (hyperautofluorescent margins, trizonal pattern)
6. Exclusion of other causes (syphilis, cancer-associated retinopathy, retinitis pigmentosa, toxic retinopathy, etc.)

### Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Classic AZOOR** | Normal fundus appearance (no visible white ring) |
| **MEWDS** | White dots visible, self-limited, typically unilateral young females |
| **MORR** | Multizonal progressive variant; more extensive RPE involvement |
| **Multifocal choroiditis (MFC)** | Discrete choroidal lesions, choriocapillaris involvement primary |
| **PIC** | Small punched-out choroidal lesions, myopic young women |
| **Cancer-associated retinopathy (CAR)** | Anti-recoverin/anti-enolase antibodies, underlying malignancy |
| **Retinitis pigmentosa** | Hereditary, progressive, bone spicule pigmentation, positive family history |
| **Syphilitic outer retinitis** | RPR/VDRL positive, responds to penicillin treatment ([PMID: 28297032](https://pubmed.ncbi.nlm.nih.gov/28297032/)) |
| **APMPPE** | Placoid lesions at RPE level, preceding flu-like illness |
| **Deferoxamine retinal toxicity** | History of deferoxamine use, bilateral, reversible on drug cessation ([PMID: 25372319](https://pubmed.ncbi.nlm.nih.gov/25372319/)) |
| **Birdshot chorioretinopathy** | HLA-A29 positive, vitritis, cream-colored lesions |

---

## 11. Outcome/Prognosis

### Visual Acuity Outcomes

The critical prognostic determinant is **macular involvement**:

- Chen et al. (2025): "Seven eyes of 5 patients showed no macular involvement with best corrected visual acuity (BCVA) of 20/20, while 5 eyes of 5 patients showed macular involvement with poorer BCVA of HM-20/400 at the last visit" ([PMID: 40446848](https://pubmed.ncbi.nlm.nih.gov/40446848/))
- Monson & Smith (2011): "Visual acuity was 20/40 or better in 74% of tested eyes" across the AZOOR/AAOR spectrum ([PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/))
- Ramtohul et al. (2025): mean follow-up 3.7 +/- 1.5 years ([PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/))

### Visual Field Outcomes
- All patients have permanent visual field loss ([PMID: 8340485](https://pubmed.ncbi.nlm.nih.gov/8340485/))
- Typically stabilizes within 6 months ([PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/))
- Some patients may show progressive loss over years ([PMID: 23591538](https://pubmed.ncbi.nlm.nih.gov/23591538/))

### Survival and Mortality
- AAOR does not affect survival or mortality
- Life expectancy is normal

### Morbidity
- Visual field defects are permanent and can be disabling
- Central vision loss when macula is involved
- Chronic photopsia can affect quality of life

### Complications
- **Choroidal neovascularization (CNV)**: Introini et al. (2018) reported type 2 subretinal CNV as a complication of AZOOR, treatable with anti-VEGF ([PMID: 30181904](https://pubmed.ncbi.nlm.nih.gov/30181904/))
- **Progressive chorioretinal atrophy**: Long-term follow-up shows continued atrophic changes ([PMID: 23591538](https://pubmed.ncbi.nlm.nih.gov/23591538/))
- **RPE disturbances**: Commonly develop over time ([PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/))

### Recovery Potential
- Foveal photoreceptor restoration possible in some cases; Seetharam et al. (2015): documented "restoration of foveal photoreceptors, which corresponded with visual recovery" ([PMID: 25383859](https://pubmed.ncbi.nlm.nih.gov/25383859/))
- However, peripheral photoreceptor loss is generally permanent

### Prognostic Factors

| Factor | Prognosis |
|---|---|
| No macular involvement | Favorable -- BCVA typically 20/20 |
| Macular involvement | Poor -- BCVA HM to 20/400 |
| Unilateral disease | Better overall functional outcome |
| Early stabilization (<6 months) | Favorable |
| Extensive retinal involvement | Risk of progressive atrophy |

---

## 12. Treatment

### Overview

There is **no proven effective treatment** for AAOR. Monson & Smith (2011) concluded: "Various treatments have been attempted in patients with AZOOR--including systemic corticosteroids, other systemic immunosuppressive agents, and different antimicrobials--but none have been proven effective" ([PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/)). All treatment evidence comes from case reports and small case series.

### Pharmacotherapy

| Treatment | Evidence | MAXO Term |
|---|---|---|
| **Systemic corticosteroids** | Most commonly tried; no proven efficacy | MAXO:0000756 (corticosteroid therapy) |
| **Immunosuppressive agents** (mycophenolate, azathioprine, cyclosporine) | Anecdotal; inconsistent efficacy | MAXO:0000757 (immunosuppressive therapy) |
| **Antiviral agents** (acyclovir, valacyclovir) | Theoretical basis from viral trigger hypothesis | MAXO:0001001 (antiviral therapy) |
| **Combined antiviral + immunosuppressive** | Bemme et al. (2016): "further progression could be stopped" in one case ([PMID: 25930180](https://pubmed.ncbi.nlm.nih.gov/25930180/)) | -- |
| **Intravitreal dexamethasone (Ozurdex)** | One AZOOR case showed improvement ([PMID: 29207977](https://pubmed.ncbi.nlm.nih.gov/29207977/)) | MAXO:0001298 (intravitreal injection) |
| **Adalimumab (anti-TNF-alpha)** | One case of overlapping MFC/AZOOR responded ([PMID: 23765682](https://pubmed.ncbi.nlm.nih.gov/23765682/)) | MAXO:0001046 (biologic therapy) |
| **Anti-VEGF injections** | For CNV complication only ([PMID: 30181904](https://pubmed.ncbi.nlm.nih.gov/30181904/)) | MAXO:0001298 (intravitreal injection) |
| **Calcium channel blockers** | Tried without success ([PMID: 29207977](https://pubmed.ncbi.nlm.nih.gov/29207977/)) | -- |

### Surgical and Interventional

- No surgical interventions are indicated for primary AAOR
- Photodynamic therapy (PDT) used for CNV complication in one patient ([PMID: 30181904](https://pubmed.ncbi.nlm.nih.gov/30181904/))

### Supportive and Rehabilitative Care

- Low vision aids for patients with significant visual field or acuity loss (MAXO:0001305)
- Regular monitoring with multimodal imaging to track progression
- Patient education and counseling (MAXO:0000540)

### Treatment Strategy

- No standardized treatment algorithm exists
- Observation is reasonable given the self-limited acute phase
- Early immunosuppression may be considered during the acute progressive stage based on anecdotal evidence
- Treatment of complications (CNV) as they arise

### Experimental Treatments

No active clinical trials specifically for AAOR are registered on ClinicalTrials.gov. The extreme rarity of the condition makes randomized controlled trials impractical.

---

## 13. Prevention

### Primary Prevention
- **Not possible** given the unknown etiology
- No modifiable risk factors have been identified

### Secondary Prevention (Early Detection)
- No screening programs exist
- High clinical suspicion is needed in young adults presenting with acute photopsia and scotoma
- Roy & Dutta Majumder (2024) emphasized "the necessity of high clinical suspicion and the role of advanced imaging in diagnosis and management" ([PMID: 38454854](https://pubmed.ncbi.nlm.nih.gov/38454854/))

### Tertiary Prevention (Preventing Complications)
- Regular ophthalmologic follow-up to monitor for progressive atrophy, choroidal neovascularization ([PMID: 30181904](https://pubmed.ncbi.nlm.nih.gov/30181904/)), and fellow eye involvement
- OCTA monitoring may detect early CNV development

### Genetic Counseling
- **Not indicated** as the disease is not hereditary

---

## 14. Other Species / Natural Disease

### Natural Disease in Animals
- **No naturally occurring animal model** of AAOR has been identified
- AZOOR/AAOR appears to be a uniquely human disease

### Comparative Biology

Autoimmune retinopathies have been studied in animal models (mouse), but these model the broader concept of anti-retinal autoimmunity rather than AAOR specifically. Lu et al. (2010) created mouse models of recoverin-associated autoimmune retinopathy, demonstrating that anti-recoverin antibodies cause "significantly reduced scotopic and photopic responses on the ERGs" and "photoreceptor and outer nuclear layer swelling" ([PMID: 21031137](https://pubmed.ncbi.nlm.nih.gov/21031137/)).

### Zoonotic Potential
- Not applicable

---

## 15. Model Organisms

### Available Models

**No specific AAOR animal models exist.** Related models include:

| Model | Type | Relevance | Limitations |
|---|---|---|---|
| Recoverin-immunized LPR mice | Induced autoimmune | Demonstrates autoantibody-mediated retinal damage | Inner retinal emphasis; not specific to annular pattern |
| Recoverin hybridoma Balb/cJ mice | Induced autoimmune | Shows photoreceptor/ONL damage more relevant to AAOR | Lacks annular spatial pattern; single antigen |
| CSF1R-antagonist light damage mice | Microglial depletion | Studies role of microglia in retinal degeneration | Mechanism (light) differs from autoimmune |

#### Autoimmune Retinopathy Mouse Models Detail

Lu et al. (2010, [PMID: 21031137](https://pubmed.ncbi.nlm.nih.gov/21031137/)):
- **Recoverin-immunized LPR mice**: B6.MRL-Fas(lpr)/J mice immunized with recombinant recoverin showed "swollen cell bodies in the inner nuclear layer," reduced ERG, and increased GFAP staining indicating Muller cell and astrocyte reactive gliosis
- **Recoverin hybridoma-injected Balb/cJ mice**: "photoreceptor and outer nuclear layer swelling" with complement C1q and C3 deposits and "increased numbers of CD4+ and CD68+ cells from retinas"
- Both models demonstrated "leukocyte invasion, complement deposition, reactive gliosis in the retina, and selective retinal degeneration"

### Model Limitations
- No model reproduces the characteristic annular spreading pattern of AAOR
- Mouse retinal anatomy differs from human (no fovea, rod-dominant)
- The specific autoantigen(s) in AAOR remain unidentified, limiting targeted model development

### Research Applications
Mouse autoimmune retinopathy models may be useful for:
- Testing immunomodulatory therapies
- Understanding photoreceptor autoimmune destruction mechanisms
- Characterizing candidate retinal autoantigens

---

## Key Findings Summary

### Finding 1: AAOR is a distinct entity within the AZOOR spectrum
Fekrat et al. (2000) established AAOR as a specific clinical variant by describing four patients with "acute onset of visual field loss associated with a localized, white annular outer retinopathy" ([PMID: 11078842](https://pubmed.ncbi.nlm.nih.gov/11078842/)). Monson & Smith (2011) subsequently compiled 131 AZOOR cases including AAOR, confirming: "predominantly white individuals, average age at presentation was 36.7 years, and the male:female ratio was 1:3.2" ([PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/)). Chen et al. (2025) reported 9 AAOR patients (12 eyes) aged 18-39 years ([PMID: 40446848](https://pubmed.ncbi.nlm.nih.gov/40446848/)), and Ramtohul et al. (2025) expanded the concept to 23 patients under "Acute Outer Retinopathy" ([PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/)).

### Finding 2: Three-stage clinical course
Chen et al. (2025) provided the first systematic staging: "The clinical course was subdivided acutely progressive stage (APS), stationary stage (SS) and atrophic stage (AS) (1-3 weeks, 3 weeks to 3 months and >3 months, respectively)" ([PMID: 40446848](https://pubmed.ncbi.nlm.nih.gov/40446848/)). This staging framework enables clinicians to anticipate disease evolution and time interventions.

### Finding 3: Symptom frequencies quantified
Ramtohul et al. (2025) provided the most robust data: "Presenting symptoms included photopsia (87%), blurred vision (57%), and scotoma (57%)" from 23 patients. They also identified the "angular sign of Henle fiber layer hyperreflectivity (ASHH)" as an important OCT biomarker ([PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/)).

### Finding 4: Photoreceptor outer segment damage is the primary pathology
Herbort et al. (2021) established that "the primary damage was identified at the level of the photoreceptor outer segments with an intact choriocapillaris and retinal pigment epithelium (RPE) layer, these structures being only secondarily involved" ([PMID: 34209956](https://pubmed.ncbi.nlm.nih.gov/34209956/)). Tagami et al. (2014) demonstrated autoantibodies targeting photoreceptors ([PMID: 25266678](https://pubmed.ncbi.nlm.nih.gov/25266678/)). Seetharam et al. (2015) confirmed "hyperreflectivity in the outer nuclear layer and the Henle fiber layer along with marked atrophy of the outer retina within the white ring" ([PMID: 25383859](https://pubmed.ncbi.nlm.nih.gov/25383859/)).

### Finding 5: Visual prognosis depends on macular involvement; no proven treatment
Chen et al. (2025): "Seven eyes of 5 patients showed no macular involvement with best corrected visual acuity (BCVA) of 20/20, while 5 eyes of 5 patients showed macular involvement with poorer BCVA of HM-20/400" ([PMID: 40446848](https://pubmed.ncbi.nlm.nih.gov/40446848/)). Monson & Smith (2011): "Various treatments have been attempted in patients with AZOOR--including systemic corticosteroids, other systemic immunosuppressive agents, and different antimicrobials--but none have been proven effective" ([PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/)). Bemme et al. (2016) reported anecdotal success: "further progression could be stopped by a combination of antiviral and immunosuppressive therapy" ([PMID: 25930180](https://pubmed.ncbi.nlm.nih.gov/25930180/)).

---

## Evidence Base

### Landmark Papers

| Paper | PMID | Contribution |
|---|---|---|
| Gass (1993) -- AZOOR original description | [8340485](https://pubmed.ncbi.nlm.nih.gov/8340485/) | Described the AZOOR syndrome spectrum; 13 patients |
| Fekrat et al. (2000) -- Original AAOR description | [11078842](https://pubmed.ncbi.nlm.nih.gov/11078842/) | First description of AAOR as a distinct entity; 4 patients |
| Monson & Smith (2011) -- Comprehensive review | [21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/) | Compiled 131 AZOOR/AAOR cases; demographics and prognosis |
| Mrejen et al. (2014) -- AZOOR imaging classification | [24945598](https://pubmed.ncbi.nlm.nih.gov/24945598/) | Imaging-based AZOOR classification; trizonal pattern; 30 cases |
| Tagami et al. (2014) -- Autoimmune evidence | [25266678](https://pubmed.ncbi.nlm.nih.gov/25266678/) | Antiretinal antibodies in all AZOOR patients tested |
| Seetharam et al. (2015) -- OCT characterization | [25383859](https://pubmed.ncbi.nlm.nih.gov/25383859/) | Detailed OCT findings; photoreceptor restoration documented |
| Herbort et al. (2021) -- Pathology mechanism | [34209956](https://pubmed.ncbi.nlm.nih.gov/34209956/) | Established photoreceptor-first pathology via multimodal imaging |
| Roy & Dutta Majumder (2024) -- Current understanding | [38454854](https://pubmed.ncbi.nlm.nih.gov/38454854/) | Comprehensive review of AZOOR including AAOR variant |
| Chen et al. (2025) -- Clinical staging | [40446848](https://pubmed.ncbi.nlm.nih.gov/40446848/) | First systematic staging of AAOR; 9 patients, 12 eyes |
| Ramtohul et al. (2025) -- Largest multicenter study | [40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/) | 23 patients, 38 eyes; symptom frequencies; ASHH sign |

---

## Limitations and Knowledge Gaps

1. **Extremely small sample sizes**: The largest AAOR-specific study includes only 23 patients. All evidence is Level 4 (case series) or Level 5 (case reports).

2. **No molecular characterization of target antigens**: The specific photoreceptor antigens targeted by autoantibodies in AAOR remain unidentified.

3. **No genetic studies**: No GWAS, exome sequencing, or candidate gene studies have been performed. HLA typing has not been systematically reported.

4. **No controlled treatment trials**: The extreme rarity precludes randomized controlled trials. All treatment evidence is anecdotal.

5. **No tissue pathology**: No histopathological or immunohistochemical analysis of AAOR retinal tissue has been published. All structural understanding derives from in vivo imaging.

6. **Inconsistent nomenclature**: The relationship between AAOR, AOR, AZOOR, and MORR remains debated, complicating literature synthesis.

7. **No standardized diagnostic criteria**: Diagnosis remains clinical and exclusionary, without formally validated criteria.

8. **No biomarkers for prognosis**: Beyond macular involvement on imaging, no molecular or imaging biomarkers predict which patients will progress.

9. **Absence of formal QoL studies**: No patient-reported outcome measures have been assessed.

10. **No animal model specific to AAOR**: Existing autoimmune retinopathy models do not recapitulate the annular spatial pattern.

---

## Proposed Follow-up Experiments/Actions

### High Priority

1. **Characterization of target autoantigens**: Perform immunoprecipitation and mass spectrometry on sera from AAOR patients against retinal protein extracts to identify the specific photoreceptor antigens targeted.

2. **HLA typing study**: Collect HLA data from AAOR patients to identify susceptibility alleles, as done for other autoimmune ocular conditions (e.g., HLA-A29 in birdshot chorioretinopathy).

3. **International registry**: Establish a multicenter AAOR/AOR registry to accumulate sufficient patients for epidemiological and genetic analyses.

4. **Standardized diagnostic criteria**: Develop and validate formal diagnostic criteria using Delphi consensus methodology among retina specialists.

### Medium Priority

5. **Longitudinal imaging biomarker study**: Correlate baseline multimodal imaging features (FAF patterns, choroidal thickness, ellipsoid zone disruption extent) with long-term visual outcomes to develop prognostic biomarkers.

6. **Aqueous humor proteomics**: Analyze aqueous humor samples from AAOR patients for cytokine profiles and antibody characterization.

7. **Pilot treatment study**: Design a prospective, multicenter observational study comparing early immunosuppression versus observation, given the impossibility of a RCT.

### Lower Priority

8. **Development of AAOR-specific animal model**: Once target antigens are identified, immunize animal models with specific antigens to create a more faithful disease model.

9. **Single-cell transcriptomics**: If surgical biopsy becomes available, perform single-cell RNA sequencing to characterize the immune cell populations infiltrating affected retina.

10. **Viral metagenomic analysis**: Perform metagenomic sequencing on aqueous/vitreous samples during acute phase to identify potential viral triggers.

---

## Ontology Term Summary

| Category | Terms |
|---|---|
| **Disease** | MONDO: not assigned; closest: AZOOR spectrum |
| **Phenotypes (HPO)** | HP:0030786 (Photopsia), HP:0000572 (Visual field defect), HP:0000575 (Scotoma), HP:0000505 (Visual impairment), HP:0000654 (Abnormal ERG), HP:0030624 (Abnormal FAF), HP:0030329 (Retinal thinning), HP:0000580 (Pigmentary retinopathy), HP:0030532 (Enlarged blind spot) |
| **Anatomy (UBERON)** | UBERON:0000966 (retina), UBERON:0001787 (photoreceptor layer), UBERON:0001782 (RPE), UBERON:0001776 (choroid), UBERON:0000019 (eye), UBERON:0001783 (optic disc), UBERON:0000053 (macula), UBERON:0001785 (fovea) |
| **Cell Types (CL)** | CL:0000604 (retinal rod cell), CL:0000573 (retinal cone cell), CL:0002586 (RPE cell), CL:0000636 (Mueller cell), CL:0000624 (CD4+ T cell), CL:0000235 (macrophage) |
| **Biological Processes (GO)** | GO:0006955 (immune response), GO:0006915 (apoptotic process), GO:0006958 (complement activation), GO:0007601 (visual perception), GO:0001750 (photoreceptor outer segment), GO:0001917 (photoreceptor inner segment) |
| **Treatments (MAXO)** | MAXO:0000756 (corticosteroid therapy), MAXO:0000757 (immunosuppressive therapy), MAXO:0001001 (antiviral therapy), MAXO:0001298 (intravitreal injection), MAXO:0001046 (biologic therapy), MAXO:0001305 (low vision rehabilitation), MAXO:0000540 (counseling) |

---

## Key References

1. Gass JDM. Acute zonal occult outer retinopathy. 1993. [PMID: 8340485](https://pubmed.ncbi.nlm.nih.gov/8340485/)
2. Fekrat S, et al. Acute annular outer retinopathy: report of four cases. 2000. [PMID: 11078842](https://pubmed.ncbi.nlm.nih.gov/11078842/)
3. Monson DM, Smith JR. Acute zonal occult outer retinopathy. 2011. [PMID: 21056448](https://pubmed.ncbi.nlm.nih.gov/21056448/)
4. Mrejen S, et al. Acute zonal occult outer retinopathy: a classification based on multimodal imaging. 2014. [PMID: 24945598](https://pubmed.ncbi.nlm.nih.gov/24945598/)
5. Tagami M, et al. Autologous antibodies to outer retina in acute zonal occult outer retinopathy. 2014. [PMID: 25266678](https://pubmed.ncbi.nlm.nih.gov/25266678/)
6. Seetharam SD, et al. New insights into acute annular outer retinopathy. 2015. [PMID: 25383859](https://pubmed.ncbi.nlm.nih.gov/25383859/)
7. Bemme S, et al. Progressive scotoma with perception of photopsia. 2016. [PMID: 25930180](https://pubmed.ncbi.nlm.nih.gov/25930180/)
8. Herbort CP, et al. AZOOR Results from a Clinicopathological Mechanism Different from Choriocapillaritis Diseases. 2021. [PMID: 34209956](https://pubmed.ncbi.nlm.nih.gov/34209956/)
9. Hoang QV, et al. Long-term follow-up of acute zonal occult outer retinopathy. 2013. [PMID: 23591538](https://pubmed.ncbi.nlm.nih.gov/23591538/)
10. Roy R, Dutta Majumder P. Current understanding of acute zonal occult outer retinopathy. 2024. [PMID: 38454854](https://pubmed.ncbi.nlm.nih.gov/38454854/)
11. Chen B, et al. Acute annular outer retinopathy: initial insights into clinical course variations with multimodal imaging. 2025. [PMID: 40446848](https://pubmed.ncbi.nlm.nih.gov/40446848/)
12. Ramtohul P, et al. Clinical and Multimodal Imaging of Acute Outer Retinopathy. 2025. [PMID: 40436146](https://pubmed.ncbi.nlm.nih.gov/40436146/)
13. Gupta V, et al. Acute annular outer retinopathy preceded by invasive ductal breast carcinoma. 2022. [PMID: 36434575](https://pubmed.ncbi.nlm.nih.gov/36434575/)
14. Garcia-Torre A, Castro-Florez M. AAOR associated with HIV. 2019. [PMID: 30455116](https://pubmed.ncbi.nlm.nih.gov/30455116/)
15. Introini U, et al. Clinical course of AZOOR complicated by choroidal neovascularization. 2018. [PMID: 30181904](https://pubmed.ncbi.nlm.nih.gov/30181904/)
16. Neri P, et al. Successful treatment of overlapping choriocapillaritis with adalimumab. 2014. [PMID: 23765682](https://pubmed.ncbi.nlm.nih.gov/23765682/)
17. Lu L, et al. Two mouse models for recoverin-associated autoimmune retinopathy. 2010. [PMID: 21031137](https://pubmed.ncbi.nlm.nih.gov/21031137/)

---

*Report generated: 2026-05-05 | Based on review of 49 publications | 5 confirmed findings*
