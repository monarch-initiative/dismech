---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-14T10:00:06.927310'
end_time: '2026-05-14T10:41:29.929114'
duration_seconds: 2483.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Langerhans Cell Histiocytosis
  mondo_id: ''
  category: Complex
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
citation_count: 52
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Langerhans Cell Histiocytosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Langerhans Cell Histiocytosis** covering all of the
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

# Comprehensive Disease Characterization: Langerhans Cell Histiocytosis

## Summary

**Langerhans Cell Histiocytosis (LCH)** is a rare inflammatory myeloid neoplasia characterized by the clonal accumulation of CD1a+/CD207+ myeloid-derived dendritic cells in virtually any organ system. The disease is universally driven by somatic activating mutations in the mitogen-activated protein kinase (MAPK) signaling pathway, with BRAF V600E accounting for approximately 50% of cases, MAP2K1 mutations ~15%, and BRAF in-frame deletions ~10–18%. These mutations arise in hematopoietic myeloid progenitors, and the differentiation stage at which the mutation occurs determines disease extent—mutations in early CD34+ bone marrow progenitors produce multisystem high-risk disease, while mutations in committed tissue-resident precursors cause localized single-system disease.

LCH affects children at an incidence of 4.46 per million and adults at 1.06 per million, with a slight male predominance. The clinical spectrum ranges from spontaneously resolving single bone lesions to life-threatening multisystem disease involving liver, spleen, and bone marrow ("risk organs"). Treatment has evolved from empiric chemotherapy (vinblastine/prednisone) toward mutation-guided targeted therapy with BRAF and MEK inhibitors, which achieve 98% short-term response rates in refractory disease. However, critical unresolved challenges remain: MAPK inhibitors spare mutant progenitor cells (explaining 61% relapse upon discontinuation), up to 45% of patients develop neurodegeneration even while on MAPK inhibitor therapy, and long-term survivors face a 2-fold elevated secondary malignancy risk.

This report synthesizes evidence from 106 publications, 14 confirmed findings, and comprehensive ontology mapping across 5 research iterations to provide a complete disease knowledge base entry for LCH, covering all aspects from molecular pathogenesis to treatment, prevention, animal models, and quality of life.

{{figure:lch_pathogenesis_overview.png|caption=Pathogenesis overview of Langerhans Cell Histiocytosis showing the MAPK-driven misguided myeloid differentiation model, from somatic mutation in hematopoietic progenitors to granulomatous lesion formation in target organs}}

---

## 1. Disease Information

### Overview

Langerhans Cell Histiocytosis (LCH) is a rare neoplastic disorder of the mononuclear phagocyte system, characterized by the accumulation and infiltration of pathological CD1a+/CD207+ (langerin-positive) myeloid-derived dendritic cells into various tissues and organs, leading to granulomatous inflammation and tissue destruction. LCH is classified under the "L-group" (Langerhans-related) histiocytoses in the revised 2016 classification by the Histiocyte Society and was recognized in the WHO 2022 Classification of Tumors of Hematopoietic and Lymphoid Tissues as a distinct entity ([PMID: 37814848](https://pubmed.ncbi.nlm.nih.gov/37814848/)).

### Key Identifiers

| Database | Identifier |
|----------|-----------|
| **MONDO** | MONDO:0011906 |
| **OMIM** | 604856 |
| **Orphanet** | ORPHA:389 |
| **ICD-10** | C96.6 (Unifocal LCH), D76.0 (LCH, NEC) |
| **ICD-11** | 2B35.0 |
| **MeSH** | D006646 |

### Synonyms and Alternative Names

- Histiocytosis X (historical)
- Eosinophilic granuloma (unifocal bone disease)
- Hand-Schüller-Christian disease (multifocal bone with diabetes insipidus and exophthalmos)
- Letterer-Siwe disease (disseminated, acute form)
- Hashimoto-Pritzker disease (congenital self-healing form)
- Langerhans cell granulomatosis
- Pulmonary Langerhans cell histiocytosis (PLCH; lung-specific adult form)

### Information Source Type

Information is derived primarily from aggregated disease-level resources including international registries, multi-center clinical trials, molecular profiling studies, and systematic reviews, supplemented by individual patient case series and reports.

---

## 2. Etiology

### Disease Causal Factors

LCH is fundamentally a **clonal neoplastic disorder driven by somatic activating mutations in the MAPK signaling pathway**. The landmark discovery of the BRAF V600E mutation in LCH lesions established its neoplastic nature. An international clinicogenomic study of 377 children found MAPK pathway gene alterations in 300 (79.6%) patients, including 191 (50.7%) with BRAF V600E, 54 with MAP2K1 mutations, 39 with BRAF exon 12 mutations, 13 with rare BRAF alterations, and 3 with ARAF or KRAS mutations ([PMID: 36083130](https://pubmed.ncbi.nlm.nih.gov/36083130/)). In adults, "MAPK/PI3K pathway alterations were observed in 77.6% (n = 197) of the patients. BRAFV600E mutation was the most common (30.7%, n = 78), followed by BRAFindel (18.1%, n = 46) and MAP2K1 mutations (12.6%, n = 32)" ([PMID: 39513946](https://pubmed.ncbi.nlm.nih.gov/39513946/)). A pediatric cohort confirmed: "A total of 30 genomic alterations in 5 genes of the MAPK pathway were identified in 187 of 223 patients (83.9%). BRAF V600E... was the most common mutation (51.6%), followed by MAP2K1... alterations (17.0%) and other BRAF mutations (13.0%)" ([PMID: 38749502](https://pubmed.ncbi.nlm.nih.gov/38749502/)).

### Genetic Risk Factors

- **BRAF V600E** (somatic): Most common driver mutation (~50% of cases); gain-of-function missense mutation constitutively activating the RAS-RAF-MEK-ERK cascade
- **MAP2K1 mutations** (somatic): Second most common (~15%); various missense and in-frame deletion mutations; often mutually exclusive with BRAF V600E
- **BRAF exon 12 in-frame deletions/indels** (somatic): ~10–18% of cases; in adults, BRAF deletions correlate with multisystem disease and poorer outcomes ([PMID: 39513946](https://pubmed.ncbi.nlm.nih.gov/39513946/))
- **ARAF mutations** (somatic): Extremely rare; a novel hotspot somatic mutation c.1046_1051delAGGCTT (p.Q349_F351delinsL) was identified in 4/148 pediatric patients; "this mutation could trigger the MAPKinase pathway and phosphorylate its downstream effectors MEK1/2 and ERK1/2 (relatively weaker than BRAFV600E)" ([PMID: 37572153](https://pubmed.ncbi.nlm.nih.gov/37572153/))
- **KRAS, NRAS mutations** (somatic): Rare; reported in pulmonary LCH and some pediatric cases

### Environmental Risk Factors

- **Cigarette smoking**: The dominant environmental risk factor, particularly for pulmonary LCH (PLCH) in adults. In a UK cohort, 96% of PLCH patients were current or ex-smokers ([PMID: 24482091](https://pubmed.ncbi.nlm.nih.gov/24482091/)). "Pulmonary Langerhans cell histiocytosis (PLCH) is a rare cystic lung disease that affects young adults with exposure to cigarette smoke" ([PMID: 41110924](https://pubmed.ncbi.nlm.nih.gov/41110924/)).
- **Assisted reproductive technology (ART)**: A nationwide cohort study (n=108,776) found ART-conceived children had SIR 4.02 (95% CI 1.08–10.29) for LCH; ICSI-conceived children SIR 5.41 (95% CI 1.11–15.80), suggesting potential epigenetic contributions ([PMID: 39383799](https://pubmed.ncbi.nlm.nih.gov/39383799/)).
- **Age**: Peak incidence in children aged 1–3 years; second peak in young adults (20–40 years) for PLCH
- **Sex**: Slight male predominance (male:female ratio ~1.2–2.3:1)

### Gene-Environment Interactions

A critical gene-environment interaction has been demonstrated in PLCH using a cigarette smoke (CS)-exposed BRAF V600E-mutant mouse model that "recapitulates many hallmark characteristics of PLCH." Specifically, "CD11c-targeted expression of BRAF-V600E increases DC responsiveness to stimuli, including the chemokine CCL20" ([PMID: 31961828](https://pubmed.ncbi.nlm.nih.gov/31961828/)). Smoking promotes recruitment of MAPK-activated circulating myeloid precursors to the lung via CCL20 and CCL7, establishing a synergistic mechanism between somatic MAPK mutations and tobacco exposure.

### Protective Factors

No well-established genetic or environmental protective factors have been identified for LCH. Smoking cessation is the most important modifiable intervention for PLCH.

---

## 3. Phenotypes

LCH presents with a remarkably diverse phenotypic spectrum depending on the organ systems involved.

### Skeletal Phenotypes (Most Common)

| Phenotype | HPO Term | Frequency | Onset | Severity |
|-----------|----------|-----------|-------|----------|
| Osteolytic bone lesions | HP:0002797 (Osteolysis) | ~50–80% of children | Childhood | Variable |
| Skull bone defects | HP:0002684 (Abnormality of the calvaria) | ~40–50% | Childhood | Moderate |
| Vertebral fractures | HP:0002953 (Vertebral compression fracture) | ~10–15% | Variable | Moderate-severe |
| Mastoid involvement | HP:0011450 (Mastoiditis) | ~15–25% | Childhood | Moderate |

### Endocrine Phenotypes

| Phenotype | HPO Term | Frequency | Onset | Severity |
|-----------|----------|-----------|-------|----------|
| Central diabetes insipidus | HP:0000873 (Diabetes insipidus) | 11.5–24% | Variable | Severe, permanent |
| Anterior pituitary deficiency | HP:0040075 (Hypopituitarism) | ~5–15% | Post-DI onset | Severe, progressive |
| Growth hormone deficiency | HP:0000824 (Decreased response to GH) | ~5–10% | Childhood | Moderate |

"The most common central nervous system (CNS) manifestation in LCH is the infiltration of the hypothalamic-pituitary region leading to destruction and neurodegeneration of CNS tissue. The latter causes the most frequent endocrinological manifestation, that is, central diabetes insipidus (CDI), and less often anterior pituitary hormone deficiency (APD). The reported incidence of CDI is estimated between 11.5 and 24%" ([PMID: 34167121](https://pubmed.ncbi.nlm.nih.gov/34167121/)).

### Cutaneous Phenotypes

| Phenotype | HPO Term | Frequency | Onset |
|-----------|----------|-----------|-------|
| Seborrheic dermatitis-like rash | HP:0001051 | ~30–50% in infants | Neonatal-infancy |
| Papulonodular skin lesions | HP:0200034 | ~30% | Variable |
| Scalp lesions | HP:0007536 | ~20% | Childhood |

### Pulmonary Phenotypes

| Phenotype | HPO Term | Frequency | Onset |
|-----------|----------|-----------|-------|
| Pulmonary cysts | HP:0006532 | ~10% children; common adults | Adult |
| Spontaneous pneumothorax | HP:0002107 | ~10% of pulmonary LCH | Variable |
| Restrictive/obstructive lung disease | HP:0002091 | Common in PLCH | Adult |

### Neurological Phenotypes

| Phenotype | HPO Term | Frequency | Onset |
|-----------|----------|-----------|-------|
| CNS neurodegeneration | HP:0002180 | 9–45% long-term | Late, progressive |
| Cerebellar ataxia | HP:0001251 | ~5–10% | Late |
| Cognitive impairment | HP:0100543 | ~20–30% survivors | Late |

Long-term follow-up revealed that 9 of 25 patients had permanent CNS consequences and "psychological testing revealed subtle deficits in short-term auditory memory (STAM) in 14 patients" ([PMID: 16470521](https://pubmed.ncbi.nlm.nih.gov/16470521/)).

### Other Phenotypes

Hepatomegaly (HP:0002240, ~15% MS-LCH), splenomegaly (HP:0001744, ~10% MS-LCH), lymphadenopathy (HP:0002716, ~10–15%), sclerosing cholangitis (HP:0030991, ~5% MS-LCH), otitis media/hearing loss (HP:0000388, ~15–25%), anemia/cytopenias (HP:0001903, ~10–20% MS-LCH).

### Quality of Life Impact

A study of 120 Chinese children with LCH found that 21.7% exhibited behavioral and emotional problems ([PMID: 41761152](https://pubmed.ncbi.nlm.nih.gov/41761152/)). Permanent consequences including DI requiring lifelong desmopressin, growth failure, and neurocognitive deficits significantly impact quality of life. "Psychoneuroendocrine sequelae were found in an unexpectedly high number of patients" ([PMID: 16470521](https://pubmed.ncbi.nlm.nih.gov/16470521/)).

---

## 4. Genetic/Molecular Information

### Causal Genes and Pathogenic Variants

{{figure:lch_mutation_survival_overview.png|caption=MAPK pathway mutation spectrum in LCH showing relative frequencies of BRAF V600E, MAP2K1, BRAF indels, and other mutations, alongside survival curves stratified by disease extent}}

| Gene | HGNC ID | Variant Type | Frequency | Origin | Functional Consequence |
|------|---------|-------------|-----------|--------|----------------------|
| **BRAF** | HGNC:1097 | Missense (V600E) | 30.7–51.6% | Somatic | Gain-of-function; constitutive kinase activation |
| **BRAF** | HGNC:1097 | In-frame deletion (exon 12) | 10–18.1% | Somatic | Gain-of-function; RAF dimerization-independent activation |
| **MAP2K1** | HGNC:6840 | Missense/in-frame deletion | 12.6–17.0% | Somatic | Gain-of-function; constitutive MEK activation |
| **ARAF** | HGNC:646 | In-frame deletion | <3% | Somatic | Gain-of-function; MEK/ERK phosphorylation |
| **KRAS** | HGNC:6407 | Missense | <2% | Somatic | Gain-of-function; RAS hyperactivation |
| **NRAS** | HGNC:7989 | Missense | <1% | Somatic | Gain-of-function |

**Somatic vs. Germline Origin**: All known LCH driver mutations are **somatic** in origin. There is no established germline predisposition. Bone marrow CD34+c-Kit+Flt3+ myeloid progenitors carry BRAF mutations in both high- and low-risk LCH. "Both LC-like and DC offspring from this progenitor carried the BRAF mutation, confirming their common origin" ([PMID: 32750121](https://pubmed.ncbi.nlm.nih.gov/32750121/)).

**Variant Classification**: BRAF V600E in the context of LCH is classified as **pathogenic** per ACMG/AMP guidelines and is cataloged in COSMIC as one of the most recurrent somatic mutations across human cancers.

**Population Allele Frequency**: BRAF V600E (rs113488022) is extremely rare in germline population databases (gnomAD allele frequency ~0.000004), consistent with its somatic origin in LCH.

### Modifier Genes

No well-established genetic modifier genes have been identified. However, RAF-independent MEK mutations (constitutively activating MEK independently of RAF) predict resistance to MEK inhibitors and are associated with "worse progression-free survival with MEK1/2 inhibition as compared to patients with other MEK1/2 mutational classes" ([PMID: 41135521](https://pubmed.ncbi.nlm.nih.gov/41135521/)).

### Epigenetic Information

The association between ART/ICSI and LCH risk (SIR 4.02–5.41) suggests epigenetic mechanisms may contribute to disease susceptibility ([PMID: 39383799](https://pubmed.ncbi.nlm.nih.gov/39383799/)). Cyclin D1, a downstream target of the MAPK pathway, has been proposed as a neoplastic marker in LCH ([PMID: 34797805](https://pubmed.ncbi.nlm.nih.gov/34797805/)). No large-scale epigenomic profiling studies of LCH lesions have been published—this represents a significant knowledge gap.

### Chromosomal Abnormalities

LCH is not characterized by large-scale chromosomal abnormalities. The driving genetic events are point mutations and small in-frame deletions in MAPK pathway genes.

---

## 5. Environmental Information

### Environmental Factors

- **Cigarette smoke**: The primary environmental factor, particularly for adult PLCH. "Cigarette smoking is a recognized causative agent or precipitant of specific diffuse lung diseases" including PLCH ([PMID: 23001806](https://pubmed.ncbi.nlm.nih.gov/23001806/)). PLCH is classified as a smoking-related interstitial lung disease, accounting for 3–5% of all ILD ([PMID: 39423337](https://pubmed.ncbi.nlm.nih.gov/39423337/)).

### Lifestyle Factors

- **Smoking cessation**: Essential intervention for PLCH management. No other lifestyle factors have been conclusively linked.

### Infectious Agents

No confirmed infectious agent has been identified. Historical associations with viruses were investigated but not confirmed. A study searching for retroviral determinants in LCH xenografts found "no type D retroviruses" ([PMID: 26347284](https://pubmed.ncbi.nlm.nih.gov/26347284/)).

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

The central pathogenic mechanism is **constitutive activation of the RAS-RAF-MEK-ERK (MAPK) signaling cascade** (KEGG: hsa04010). "Activation of the mitogen-activated protein kinase (MAPK) pathway is a key molecular mechanism involved in the development of LCH" ([PMID: 33935037](https://pubmed.ncbi.nlm.nih.gov/33935037/)). Additional pathways include PI3K-AKT (KEGG: hsa04151), NF-κB (KEGG: hsa04064), and JAK-STAT (KEGG: hsa04630).

| Pathway | Identifier | Role in LCH |
|---------|-----------|-------------|
| MAPK signaling | KEGG:hsa04010 | Core oncogenic driver |
| PI3K-AKT signaling | KEGG:hsa04151 | Co-activated in subset |
| NF-κB signaling | KEGG:hsa04064 | Inflammatory cytokine production |
| Osteoclast differentiation | KEGG:hsa04380 | Bone lesion formation |
| Oncogenic MAPK signaling | R-HSA-6802957 | Pathological ERK activation |

### The Misguided Myeloid Differentiation Model

The prevailing pathogenic model posits that LCH arises as "a consequence of a misguided differentiation programme of myeloid dendritic cell precursors" ([PMID: 25430560](https://pubmed.ncbi.nlm.nih.gov/25430560/)). This was directly confirmed by demonstrating that bone marrow "CD34+c-Kit+Flt3+ cells from BM of MS-RO+ LCH patients produced Langerhans cell (LC)-like cells in vitro. Both LC-like and DC offspring from this progenitor carried the BRAF mutation, confirming their common origin" ([PMID: 32750121](https://pubmed.ncbi.nlm.nih.gov/32750121/)).

The model was further validated using iPSC technology: "BRAFV600E/WT iPSCs display myelomonocytic skewing during hematopoiesis and spontaneously differentiate into CD1a+/CD207+ cells that are similar to lesional LCH cells and are derived from a CD14+ progenitor" ([PMID: 39630039](https://pubmed.ncbi.nlm.nih.gov/39630039/)).

**Causal chain:**

```
SOMATIC MAPK MUTATION (BRAF V600E / MAP2K1 / BRAF indel / ARAF / KRAS)
        ↓
  Arises in hematopoietic myeloid progenitor (CD34+/c-Kit+/Flt3+)
        ↓
  Constitutive MAPK pathway activation → ERK1/2 phosphorylation
        ↓
  Myelomonocytic skewing during hematopoiesis
        ↓
  Aberrant differentiation into CD1a+/CD207+ pathological cells
        ↓
  Recruitment to tissues via chemokines (CCL20, CCL7)
        ↓
  GRANULOMATOUS LESION FORMATION
  (LCH cells + exhausted T cells + eosinophils + macrophages)
        ↓
  Cytokine storm (OPN/SPP1, IL-1β, TNF-α, IL-6)
        ↓
  TISSUE DESTRUCTION & ORGAN DYSFUNCTION
```

### Immune System Involvement

LCH lesions are characterized by a complex inflammatory microenvironment with **T cell exhaustion**: "Both CD8+ and CD4+ T cells exhibited 'exhausted' phenotypes with high expression of the immune checkpoint receptors. LCH DCs showed robust expression of ligands to checkpoint receptors" ([PMID: 33075814](https://pubmed.ncbi.nlm.nih.gov/33075814/)). Intralesional regulatory T cells demonstrate intact suppressive activity. SPP1 (osteopontin) is a key inflammatory mediator: "several novel genes whose products activate and recruit T cells to sites of inflammation, including SPP1 (osteopontin), were highly overexpressed in LCH CD207(+) cells" ([PMID: 20220088](https://pubmed.ncbi.nlm.nih.gov/20220088/)).

### Neurodegeneration Mechanism

A breakthrough finding identified mutant microglial clones as the driver of LCH-associated neurodegeneration: "We found microglial mutant clones in LCH and ECD patients, whether or not they presented with clinical symptoms of neurodegeneration, associated with microgliosis, astrocytosis, and neuronal loss, predominantly in the rhombencephalon gray nuclei" ([PMID: 40081365](https://pubmed.ncbi.nlm.nih.gov/40081365/)). This identifies a distinct CNS-resident pathway that is independent of active systemic disease.

### Molecular Profiling

**Transcriptomics**: Gene expression profiling identified 2,113 differentially expressed genes (FDR<0.01) in LCH CD207+ cells compared to control epidermal Langerhans cells ([PMID: 20220088](https://pubmed.ncbi.nlm.nih.gov/20220088/)).

**Key Biomarkers**:
- **Osteopontin (SPP1/OPN)**: CSF biomarker for CNS-LCH—"Osteopontin was the only consistently elevated CSF protein in patients with CNS-LCH compared with patients with other brain pathologies" ([PMID: 29624648](https://pubmed.ncbi.nlm.nih.gov/29624648/)). High serum OPN levels correlate with poorer survival in multisystem LCH with high-risk organ involvement ([PMID: 28326824](https://pubmed.ncbi.nlm.nih.gov/28326824/)).
- **MMP-7 and TNF-α**: Proposed as prognostic biomarkers for adult PLCH ([PMID: 41720965](https://pubmed.ncbi.nlm.nih.gov/41720965/)).
- **Cell-free BRAF V600E DNA**: Monitoring biomarker for treatment response ([PMID: 41823178](https://pubmed.ncbi.nlm.nih.gov/41823178/)).

### Key GO Terms

| GO ID | Term | Category |
|-------|------|----------|
| GO:0000165 | MAPK cascade | Biological Process |
| GO:0006954 | Inflammatory response | Biological Process |
| GO:0030099 | Myeloid cell differentiation | Biological Process |
| GO:0030154 | Cell differentiation | Biological Process |
| GO:0045087 | Innate immune response | Biological Process |
| GO:0001774 | Microglial cell activation | Biological Process |
| GO:0004674 | Protein serine/threonine kinase activity | Molecular Function |
| GO:0004708 | MAP kinase kinase activity | Molecular Function |
| GO:0005634 | Nucleus | Cellular Component |
| GO:0005829 | Cytosol | Cellular Component |

### Cell Types Involved

| CL Term | Cell Type | Role in LCH |
|---------|-----------|-------------|
| CL:0000451 | Langerhans cell | Pathological variant (disease hallmark) |
| CL:0000782 | Myeloid dendritic cell | Precursor cell type |
| CL:0000037 | Hematopoietic stem cell | Mutation carrier in high-risk disease |
| CL:0000129 | Microglial cell | CNS neurodegeneration driver |
| CL:0000625 | CD8+ alpha-beta T cell | Exhausted phenotype in lesions |
| CL:0000815 | Regulatory T cell | Suppressive activity in lesions |
| CL:0000771 | Eosinophil | Characteristic inflammatory infiltrate |
| CL:0000235 | Macrophage | Granuloma component |
| CL:0000092 | Osteoclast | Bone resorption in lesions |

---

## 7. Anatomical Structures Affected

### Organ Level

| Organ/System | UBERON Term | Involvement Type | Frequency |
|-------------|-------------|-----------------|-----------|
| Bone | UBERON:0002481 | Primary (osteolytic lesions) | ~80% children |
| Skin | UBERON:0002097 | Primary | ~30–50% |
| Lung | UBERON:0002048 | Primary (PLCH) / secondary | ~10% children; common adults |
| Pituitary gland | UBERON:0000007 | Primary (endocrine) | ~15–25% |
| Liver | UBERON:0002107 | Risk organ | ~10–15% MS-LCH |
| Spleen | UBERON:0002106 | Risk organ | ~5–10% MS-LCH |
| Bone marrow | UBERON:0002371 | Risk organ (hematopoietic) | ~5% |
| Lymph nodes | UBERON:0000029 | Secondary | ~10–15% |
| CNS (brain) | UBERON:0000955 | Secondary (neurodegeneration) | ~10–45% long-term |
| GI tract | UBERON:0001555 | Rare | <5% |

### Subcellular Level

The pathological hallmark at the subcellular level includes **Birbeck granules**—tennis-racket shaped organelles unique to Langerhans cells, visible on electron microscopy. "In the examined 11 cases co-expression of CD1a with langerin and with the presence of Birbeck's granules was noted" ([PMID: 17378241](https://pubmed.ncbi.nlm.nih.gov/17378241/)). However, electron microscopy "is no longer required for diagnosis due to immunohistochemical staining" ([PMID: 32513402](https://pubmed.ncbi.nlm.nih.gov/32513402/)).

### Localization

CNS involvement predominantly affects the rhombencephalon gray nuclei ([PMID: 40081365](https://pubmed.ncbi.nlm.nih.gov/40081365/)). Craniofacial bones (temporal bone, orbital rim, mandible) are the most common skeletal sites. Disease is generally bilateral/multifocal in multisystem disease; unilateral in localized forms.

---

## 8. Temporal Development

### Onset

- **Pediatric LCH**: Peak incidence 1–3 years; can present at birth (neonatal LCH) ([PMID: 41462262](https://pubmed.ncbi.nlm.nih.gov/41462262/))
- **Adult PLCH**: Young to middle-aged adults (median age ~37–38 years)
- **Onset pattern**: Variable—acute (neonatal disseminated), subacute (most cases), insidious (PLCH, pituitary involvement)—one case showed a "10-year diagnostic odyssey" ([PMID: 41189157](https://pubmed.ncbi.nlm.nih.gov/41189157/))

### Progression

- **Single-system LCH**: Often self-limited; "Isolated cutaneous disease should only be treated when symptomatic, because spontaneous resolution is common" ([PMID: 29754886](https://pubmed.ncbi.nlm.nih.gov/29754886/))
- **Multisystem LCH**: Relapsing-remitting; reactivation rate 30–50%. "MS-LCH patients had a higher reactivation rate compared to those with SS-LCH (50.0% vs. 4.3%, p = 0.02)" ([PMID: 41546712](https://pubmed.ncbi.nlm.nih.gov/41546712/))
- **Neurodegeneration**: Progressive and irreversible; "deterioration of radiological ND was noted in 17 patients leading to overt clinical neuropsychological impairment in five" ([PMID: 22183971](https://pubmed.ncbi.nlm.nih.gov/22183971/))

### Critical Periods

First 2 years after diagnosis carry the highest reactivation risk. Age <1 year is an independent risk factor for inferior survival (HR 13.79, 95% CI: 1.5–123.4, p=0.02) ([PMID: 41546712](https://pubmed.ncbi.nlm.nih.gov/41546712/)).

---

## 9. Inheritance and Population

### Epidemiology

| Parameter | Value | Source |
|-----------|-------|--------|
| **Incidence (children 0–14y)** | 4.46 per million/year | [PMID: 36122574](https://pubmed.ncbi.nlm.nih.gov/36122574/) |
| **Incidence (adults ≥15y)** | 1.06 per million/year | [PMID: 36122574](https://pubmed.ncbi.nlm.nih.gov/36122574/) |
| **Prevalence** | 9.95 per million overall | [PMID: 36122574](https://pubmed.ncbi.nlm.nih.gov/36122574/) |
| **1-year OS (children)** | 99% | [PMID: 36122574](https://pubmed.ncbi.nlm.nih.gov/36122574/) |
| **1-year OS (adults)** | 90% | [PMID: 36122574](https://pubmed.ncbi.nlm.nih.gov/36122574/) |
| **Sex ratio (M:F)** | ~1.2–2.3:1 (male predominance) | Multiple series |

These data are derived from the England national registry (2003–2018), n=1,340 patients (856 children, 484 adults), representing the most comprehensive population-level epidemiological data available.

### Genetic Etiology

LCH is **not inherited**. All known driver mutations are somatic. There is no Mendelian inheritance pattern, no germline predisposition gene, no founder effects, and no role for consanguinity. Possible ethnic variation exists: lower BRAF V600E frequency in Asian populations (~21% in Japanese vs ~50% in Western series) ([PMID: 27041734](https://pubmed.ncbi.nlm.nih.gov/27041734/)), implying "the possibility of different genetic backgrounds in the pathogenesis of LCH across various ethnicities."

### Population Demographics

Age distribution is bimodal—pediatric peak at 1–3 years and adult peak at 30–40 years (particularly PLCH). Geographic distribution is worldwide with no clear endemic pattern. Age ≥60 years carries HR 22.12 for mortality ([PMID: 36122574](https://pubmed.ncbi.nlm.nih.gov/36122574/)).

---

## 10. Diagnostics

### Clinical Tests

**Biopsy and Histopathology (Gold Standard)**: Characteristic Langerhans cells with "coffee-bean" cleaved nuclei and eosinophilic cytoplasm, confirmed by **positive immunohistochemistry for CD1a and CD207 (langerin)** ([PMID: 29754886](https://pubmed.ncbi.nlm.nih.gov/29754886/)). S-100 protein positivity is supportive.

**Imaging**: Skeletal survey for bone lesions; HRCT for PLCH (nodules, cavitated nodules, thin/thick-walled cysts); MRI brain for pituitary/CNS; ¹⁸F-FDG PET-CT for staging. "Mean SUVmax was significantly higher in deceased patients than survivors (6.7 ± 1.8 vs. 4.7 ± 3.0; P = 0.01)" ([PMID: 42087703](https://pubmed.ncbi.nlm.nih.gov/42087703/)).

**Biomarkers**: Cell-free BRAF V600E DNA for monitoring; CSF osteopontin for CNS-LCH ([PMID: 29624648](https://pubmed.ncbi.nlm.nih.gov/29624648/)); serum MMP-7 and TNF-α for PLCH prognosis ([PMID: 41720965](https://pubmed.ncbi.nlm.nih.gov/41720965/)).

### Genetic Testing

BRAF V600E testing (allele-specific PCR or NGS) is first-line molecular testing. NGS panels covering BRAF, MAP2K1, ARAF, KRAS are recommended for V600E-negative cases ([PMID: 37572153](https://pubmed.ncbi.nlm.nih.gov/37572153/)). Note: IHC for BRAF V600E may have limited sensitivity in some settings ([PMID: 27041734](https://pubmed.ncbi.nlm.nih.gov/27041734/)).

### Differential Diagnosis

- **Erdheim-Chester disease (ECD)**: CD1a-negative, long bone osteosclerosis, "hairy kidneys" ([PMID: 41728905](https://pubmed.ncbi.nlm.nih.gov/41728905/))
- **Rosai-Dorfman disease (RDD)**: S100+/CD1a-, emperipolesis
- **Juvenile xanthogranuloma (JXG)**: CD1a-/CD207- with Touton giant cells
- **Lymphangioleiomyomatosis**: Cystic lung disease in women
- **Osteomyelitis, Ewing sarcoma**: Bone lesion mimics

"A minimum immunohistochemical panel including CD68 or CD163, S100, CD1a, langerin, and BRAF V600E, combined with morphologic features can establish a histologic diagnosis" ([PMID: 41651609](https://pubmed.ncbi.nlm.nih.gov/41651609/)).

---

## 11. Outcome/Prognosis

### Survival and Mortality

{{figure:lch_final_summary.png|caption=Comprehensive summary of LCH disease characterization showing mutation spectrum, survival stratified by disease extent and risk organ involvement, multi-organ involvement patterns, and knowledge base statistics}}

| Patient Group | 5-year EFS | 10-year OS | Source |
|---------------|------------|------------|--------|
| Single-system LCH | 95.2% | 93.8% | [PMID: 41546712](https://pubmed.ncbi.nlm.nih.gov/41546712/); [PMID: 42087703](https://pubmed.ncbi.nlm.nih.gov/42087703/) |
| MS-LCH RO- | 58.4% | 74.2% (all MS) | [PMID: 41546712](https://pubmed.ncbi.nlm.nih.gov/41546712/) |
| MS-LCH RO+ | 44.1% | 50% | [PMID: 41546712](https://pubmed.ncbi.nlm.nih.gov/41546712/); [PMID: 42087703](https://pubmed.ncbi.nlm.nih.gov/42087703/) |
| Pediatric (SEER) | 96.6% (5yr OS) | — | [PMID: 36758375](https://pubmed.ncbi.nlm.nih.gov/36758375/) |
| Adult (SEER) | 88.5% (5yr OS) | — | [PMID: 36758375](https://pubmed.ncbi.nlm.nih.gov/36758375/) |

**Key prognostic factors**:
- Age <1 year: HR 13.79 for mortality ([PMID: 41546712](https://pubmed.ncbi.nlm.nih.gov/41546712/))
- Age ≥60 years: HR 22.12 for mortality ([PMID: 36122574](https://pubmed.ncbi.nlm.nih.gov/36122574/))
- Multiple site involvement: HR 3.12 ([PMID: 41796299](https://pubmed.ncbi.nlm.nih.gov/41796299/))
- Risk organ involvement: Strongest adverse prognostic factor
- Baseline SUVmax on FDG-PET ([PMID: 42087703](https://pubmed.ncbi.nlm.nih.gov/42087703/))
- BRAF genotype: BRAFindel associated with inferior survival ([PMID: 39513946](https://pubmed.ncbi.nlm.nih.gov/39513946/))

### Secondary Malignancy Risk

Overall SIR **2.07** (95% CI 1.74–2.45) for secondary primary malignancies after LCH ([PMID: 36758375](https://pubmed.ncbi.nlm.nih.gov/36758375/)). Highest risk for hematologic malignancies in children.

### Complications

- Permanent endocrine deficits (DI, GH deficiency, panhypopituitarism)
- Progressive CNS neurodegeneration (45% 5-year risk even on MAPKi)
- Sclerosing cholangitis (hepatic fibrosis requiring transplant)
- Pulmonary fibrosis and chronic respiratory failure
- Pathological fractures and orthopedic deformity

---

## 12. Treatment

### First-Line Pharmacotherapy

| Treatment | MAXO Term | Indication |
|-----------|-----------|------------|
| **Vinblastine + Prednisone** (12 months) | NCIT:C15986 | MS-LCH, multifocal SS-LCH |
| Topical corticosteroids | MAXO:0001479 | Localized skin/bone |
| Smoking cessation | MAXO:0009015 | PLCH |

"Systemic treatment with steroids and vinblastine for 12 months is the standard first-line regimen" with reactivation rates of 30–50% ([PMID: 29754886](https://pubmed.ncbi.nlm.nih.gov/29754886/)).

### Targeted Therapies (MAPK Inhibitors)

| Agent | Target | CHEBI/DrugBank | Evidence |
|-------|--------|---------------|---------|
| **Vemurafenib** | BRAF V600E | CHEBI:63637 / DB08881 | 98% response in refractory BRAF+ LCH |
| **Dabrafenib** | BRAF V600E | CHEBI:75045 / DB08912 | Alternative BRAF inhibitor |
| **Trametinib** | MEK1/2 | CHEBI:75998 / DB08911 | 86.4% PFS during treatment; mutation-agnostic ([PMID: 41823178](https://pubmed.ncbi.nlm.nih.gov/41823178/)) |
| **Cobimetinib** | MEK1/2 | CHEBI:90227 / DB09053 | FDA-approved for adult histiocytoses (2022) |

**Largest MAPKi study** (288 children, 26 countries): "Short-term responses (<8 weeks) ranged from 98% (R-RO+ and R-RO-), to 30% (lung) to none (ND, DI and SC)" with 5-year survival of 98%. However, after 113 patients discontinued MAPKi, 69 (61%) relapsed. Critically, "among the 143 assessable patients without ND-LCH at MAPKi onset, 60 developed ND: 45% 5-year risk" ([PMID: 41678955](https://pubmed.ncbi.nlm.nih.gov/41678955/)).

**Why MAPKi doesn't cure**: iPSC modeling revealed that "MAPKis do not affect myeloid progenitors but reduce only the mature CD14+ cell population" ([PMID: 39630039](https://pubmed.ncbi.nlm.nih.gov/39630039/)), mechanistically explaining relapse upon drug withdrawal.

**Resistance**: RAF-independent MEK mutations are "associated with worse progression-free survival with MEK1/2 inhibition." ERK inhibition may overcome this resistance ([PMID: 41135521](https://pubmed.ncbi.nlm.nih.gov/41135521/)).

### Salvage Therapies

| Treatment | Key Evidence |
|-----------|-------------|
| **Cladribine** | 70% response at 6 months in PLCH ([PMID: 41611252](https://pubmed.ncbi.nlm.nih.gov/41611252/)) |
| **Clofarabine** | Effective for refractory RO- LCH ([PMID: 34725963](https://pubmed.ncbi.nlm.nih.gov/34725963/)); proposed for GI-LCH ([PMID: 40988414](https://pubmed.ncbi.nlm.nih.gov/40988414/)) |
| **Cytarabine** | Salvage for progressive disease |

### Hematopoietic Stem Cell Transplantation

Allo-HSCT is reserved for refractory MS-LCH. Japanese nationwide study (n=30): 17/30 (57%) alive. "The six patients with NAD/AD-r experienced better outcomes than the 20 with AD-s/AD-p (5-year OS, 100% vs. 54.5%, respectively, p = 0.040). Disease state at the time of HSCT was the most important prognostic factor" ([PMID: 31758416](https://pubmed.ncbi.nlm.nih.gov/31758416/)).

### Immunotherapy (Experimental)

Combined MAPKi + anti-PD-1 showed synergy in mouse models: "combined treatment with MAPK inhibitor and anti-PD-1 significantly decreased both CD8+ T cells and myeloid LCH cells in a synergistic fashion" ([PMID: 33075814](https://pubmed.ncbi.nlm.nih.gov/33075814/)).

### Supportive Care

- **Hormone replacement**: Lifelong desmopressin for DI, thyroid/cortisol/GH replacement (MAXO:0000583)
- **Lung transplantation**: For end-stage PLCH
- **Liver transplantation**: For end-stage sclerosing cholangitis

---

## 13. Prevention

### Primary Prevention

No established primary prevention strategies exist given the somatic mutation-driven etiology. **Smoking avoidance/cessation** is the only modifiable risk factor for PLCH. "Smoking cessation is the most important recommendation for PLCH patients" ([PMID: 29083024](https://pubmed.ncbi.nlm.nih.gov/29083024/)).

### Secondary Prevention

No population-based screening programs exist. Early detection relies on clinical awareness. cfBRAF V600E monitoring can detect early relapse.

### Tertiary Prevention

Long-term surveillance for reactivation, endocrine sequelae (annual pituitary hormone panels, MRI), neuropsychological monitoring, and secondary malignancy screening. "Adequate follow-up to monitor for disease progression, relapse, and sequelae is recommended in all patients" ([PMID: 29754886](https://pubmed.ncbi.nlm.nih.gov/29754886/)).

### Genetic Counseling

LCH is not inherited. Genetic counseling provides reassurance; no increased risk to family members. The ART-LCH association may warrant awareness in reproductive medicine.

---

## 14. Other Species / Natural Disease

### Canine LCH

- **Species**: *Canis lupus familiaris* (NCBI Taxon: 9615)
- Cell line FB-LCH01 established; maintained E-cadherin expression consistent with Langerhans cell origin ([PMID: 30884050](https://pubmed.ncbi.nlm.nih.gov/30884050/))
- mRNA sequencing showed MAPK pathway activation in LCH cell lines, mirroring human disease. CDK4/6 inhibitor palbociclib showed growth inhibitory effects ([PMID: 35278028](https://pubmed.ncbi.nlm.nih.gov/35278028/))

### Feline Pulmonary LCH

- **Species**: *Felis catus* (NCBI Taxon: 9685)
- Rare disease of middle-aged to older cats; first antemortem diagnosis via BAL cytology with CD1a immunocytochemistry in a 9-year-old British shorthair ([PMID: 37914537](https://pubmed.ncbi.nlm.nih.gov/37914537/))

### Comparative Biology

The conservation of MAPK pathway-driven histiocytic disorders across humans, dogs, and cats supports the fundamental role of this signaling cascade in dendritic cell biology and disease. "Fragmentation of the E-cadherin cell adhesion molecule may be associated with the loss of cell adhesion and increased abilities of invasion and migration of neoplastic cells" ([PMID: 34907644](https://pubmed.ncbi.nlm.nih.gov/34907644/)).

---

## 15. Model Organisms

### Mouse Models

| Model | Type | Key Application |
|-------|------|----------------|
| BRAF V600E CD11c-Cre + cigarette smoke | Conditional transgenic + environmental | Recapitulates PLCH hallmarks ([PMID: 31961828](https://pubmed.ncbi.nlm.nih.gov/31961828/)) |
| BRAF V600E CD11c LCH mouse | Conditional transgenic | PD-1/MAPKi synergy demonstrated ([PMID: 33075814](https://pubmed.ncbi.nlm.nih.gov/33075814/)) |
| SCID xenograft (canine LCH) | Xenograft | Metastasis modeling ([PMID: 30884050](https://pubmed.ncbi.nlm.nih.gov/30884050/)) |

### Human iPSC Model (2025)

The BRAF V600E/WT iPSC model represents a transformative advance and the first human in vitro model for LCH. It recapitulates key disease features: myelomonocytic skewing, spontaneous CD1a+/CD207+ cell differentiation from CD14+ progenitors, and neurodegeneration in co-culture systems. Critically, it revealed that "MAPKis do not affect myeloid progenitors but reduce only the mature CD14+ cell population" ([PMID: 39630039](https://pubmed.ncbi.nlm.nih.gov/39630039/)), explaining why LCH relapses after MAPKi withdrawal.

### Model Limitations

- Mouse models do not fully recapitulate multisystem dissemination
- iPSC models lack in vivo tissue architecture and systemic immune context
- No single model captures all disease manifestations (bone, skin, CNS, liver)
- Species-specific differences in immune microenvironment composition

---

## Mechanistic Model: Integrated Pathogenesis

```
┌──────────────────────────────────────────────────────────────┐
│              SOMATIC MAPK MUTATION                            │
│  (BRAF V600E ~50% | MAP2K1 ~15% | BRAF indel ~15%)          │
└────────────────────────┬─────────────────────────────────────┘
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
  EARLY PROGENITOR              COMMITTED PRECURSOR
  (CD34+/c-Kit+/Flt3+)         (tissue DC precursor)
          │                             │
          ▼                             ▼
  HIGH-RISK MULTISYSTEM          LOW-RISK SINGLE-SYSTEM
  (liver, spleen, BM)           (bone, skin, lung)
          │                             │
          └──────────────┬──────────────┘
                         ▼
           MISGUIDED MYELOID DIFFERENTIATION
           → CD1a+/CD207+ pathological cells
                         │
           ┌─────────────┼─────────────┐
           ▼             ▼             ▼
      TISSUE         IMMUNE        CYTOKINE
     HOMING        EXHAUSTION       STORM
  (CCL20/CCL7)   (PD-1+ T cells)  (OPN, TNF-α)
           │             │             │
           └─────────────┼─────────────┘
                         ▼
                 GRANULOMATOUS LESION
                         │
           ┌─────────────┼─────────────┐
           ▼             ▼             ▼
      OSTEOLYSIS    FIBROSIS    NEURODEGENERATION
      (bone)        (liver,     (mutant microglia →
                    lung)       neuronal loss)
```

**Key therapeutic insight**: MAPKi eliminates mature pathological cells (↓CD14+ population) but **spares mutant progenitors** → 61% relapse on discontinuation. Neurodegeneration driven by tissue-resident mutant microglia is **not prevented by MAPKi**.

---

## Evidence Base

### Landmark Papers

| Paper | PMID | Key Contribution |
|-------|------|-----------------|
| *Clinicogenomic associations in childhood LCH* | [36083130](https://pubmed.ncbi.nlm.nih.gov/36083130/) | Largest study (n=377) establishing MAPK mutation spectrum |
| *Misguided myeloid differentiation model* | [25430560](https://pubmed.ncbi.nlm.nih.gov/25430560/) | Proposed LCH as inflammatory myeloid neoplasia |
| *BM myeloid progenitors as mutation carriers* | [32750121](https://pubmed.ncbi.nlm.nih.gov/32750121/) | Proved hematopoietic progenitor origin |
| *BRAFV600E iPSC model* | [39630039](https://pubmed.ncbi.nlm.nih.gov/39630039/) | Explained MAPKi failure; first human model |
| *Long-term MAPKi (n=288)* | [41678955](https://pubmed.ncbi.nlm.nih.gov/41678955/) | Largest treatment study; 45% ND risk |
| *Mutant microglia in neurodegeneration* | [40081365](https://pubmed.ncbi.nlm.nih.gov/40081365/) | Identified CNS pathogenic mechanism |
| *CS-BRAF V600E mouse model* | [31961828](https://pubmed.ncbi.nlm.nih.gov/31961828/) | Gene-environment interaction in PLCH |
| *England national registry* | [36122574](https://pubmed.ncbi.nlm.nih.gov/36122574/) | Definitive epidemiological data |
| *SPP1 transcriptomics* | [20220088](https://pubmed.ncbi.nlm.nih.gov/20220088/) | Key biomarker identification |
| *CSF osteopontin* | [29624648](https://pubmed.ncbi.nlm.nih.gov/29624648/) | CNS-specific biomarker |
| *Secondary malignancy risk (SEER)* | [36758375](https://pubmed.ncbi.nlm.nih.gov/36758375/) | SIR 2.07 for secondary cancers |
| *ART/ICSI association* | [39383799](https://pubmed.ncbi.nlm.nih.gov/39383799/) | Novel environmental/epigenetic risk factor |
| *RAF-independent MEK mutations* | [41135521](https://pubmed.ncbi.nlm.nih.gov/41135521/) | Treatment resistance mechanism |
| *Allo-HSCT outcomes (Japan)* | [31758416](https://pubmed.ncbi.nlm.nih.gov/31758416/) | Salvage transplant data |
| *40-year survival (Thailand)* | [41546712](https://pubmed.ncbi.nlm.nih.gov/41546712/) | Comprehensive prognostic data |

---

## Limitations and Knowledge Gaps

1. **Mutation-negative cases (~20%)**: Alternative drivers in MAPK-wild-type LCH remain uncharacterized.

2. **Neurodegeneration prevention**: No therapy prevents or reverses LCH-associated neurodegeneration. The 45% 5-year risk even on MAPKi is the most critical unmet need.

3. **Optimal MAPKi duration**: No consensus on when to stop targeted therapy. 61% relapse on discontinuation, but indefinite treatment carries toxicity.

4. **Adult LCH underrepresentation**: Most trials focus on children. Adult PLCH and non-pulmonary adult LCH lack evidence-based algorithms.

5. **Epigenomic profiling**: No large-scale methylation or chromatin studies of LCH lesions exist.

6. **ART-LCH link**: The SIR 4.02–5.41 association needs replication and mechanistic investigation.

7. **Low-income settings**: Nearly all data come from high-income countries; LCH burden in LMICs is virtually unreported.

8. **Metabolomics**: No metabolomic profiling of LCH has been published.

---

## Proposed Follow-up Experiments/Actions

1. **Target mutant progenitors**: Develop MAPKi + progenitor-directed combination strategies using the iPSC platform ([PMID: 39630039](https://pubmed.ncbi.nlm.nih.gov/39630039/)) for drug screening.

2. **Neurodegeneration prevention trial**: CSF-penetrant MAPK inhibitors or microglial-targeted therapies, given the mutant microglia mechanism ([PMID: 40081365](https://pubmed.ncbi.nlm.nih.gov/40081365/)).

3. **ERK inhibitor clinical trials**: For RAF-independent MEK mutation-driven resistant disease ([PMID: 41135521](https://pubmed.ncbi.nlm.nih.gov/41135521/)).

4. **Combined MAPKi + anti-PD-1 trial**: Clinical translation of preclinical synergy ([PMID: 33075814](https://pubmed.ncbi.nlm.nih.gov/33075814/)).

5. **Prospective CSF osteopontin monitoring**: Validate as neurodegeneration early warning biomarker.

6. **Epigenetic profiling of ART-conceived LCH patients**: Investigate methylation signatures explaining elevated risk.

7. **International adult LCH treatment protocol**: Consensus guidelines for adult LCH.

8. **Whole-genome sequencing of mutation-negative cases**: Identify novel drivers in the ~20% without detectable MAPK alterations.

---

## Comprehensive Ontology Term Compilation

### HPO Terms with Estimated Frequencies

| HPO ID | Term | Frequency |
|--------|------|-----------|
| HP:0002797 | Osteolysis | 50–80% |
| HP:0000988 | Skin rash | 30–50% |
| HP:0000873 | Diabetes insipidus | 11.5–24% |
| HP:0002716 | Lymphadenopathy | 15–30% |
| HP:0002240 | Hepatomegaly | 15–20% (MS-LCH) |
| HP:0001744 | Splenomegaly | 10–15% (MS-LCH) |
| HP:0000388 | Otitis media | 15–25% |
| HP:0002180 | Neurodegeneration | 20–45% (long-term) |
| HP:0001945 | Fever | Common in MS-LCH |
| HP:0006528 | Chronic lung disease | ~10% pediatric |
| HP:0002107 | Pneumothorax | ~10% pulmonary LCH |
| HP:0001876 | Pancytopenia | Rare (BM involvement) |
| HP:0001251 | Cerebellar ataxia | Subset of ND-LCH |
| HP:0100543 | Cognitive impairment | 20–30% survivors |
| HP:0040075 | Hypopituitarism | 5–15% |
| HP:0000824 | Decreased GH response | Variable |
| HP:0001051 | Seborrheic dermatitis | 30–50% infants |
| HP:0002094 | Dyspnea | Adult PLCH |
| HP:0002014 | Diarrhea | Rare (GI involvement) |
| HP:0030991 | Sclerosing cholangitis | ~5% MS-LCH |

### GO Terms

| GO ID | Term | Category |
|-------|------|----------|
| GO:0000165 | MAPK cascade | BP |
| GO:0030099 | Myeloid cell differentiation | BP |
| GO:0006954 | Inflammatory response | BP |
| GO:0045087 | Innate immune response | BP |
| GO:0001774 | Microglial cell activation | BP |
| GO:0043066 | Negative regulation of apoptosis | BP |
| GO:0008283 | Cell population proliferation | BP |
| GO:0006468 | Protein phosphorylation | BP |
| GO:0004674 | Protein Ser/Thr kinase activity | MF |
| GO:0004708 | MAP kinase kinase activity | MF |
| GO:0005634 | Nucleus | CC |
| GO:0005829 | Cytosol | CC |

### CHEBI Terms

| CHEBI ID | Entity | Role |
|----------|--------|------|
| CHEBI:27375 | Vinblastine | First-line |
| CHEBI:8382 | Prednisone | First-line |
| CHEBI:567361 | Cladribine | Second-line |
| CHEBI:28680 | Cytarabine | Salvage |
| CHEBI:681569 | Clofarabine | Salvage |
| CHEBI:63637 | Vemurafenib | BRAF inhibitor |
| CHEBI:75045 | Dabrafenib | BRAF inhibitor |
| CHEBI:75998 | Trametinib | MEK inhibitor |
| CHEBI:90227 | Cobimetinib | MEK inhibitor (FDA-approved) |
| CHEBI:50667 | Mercaptopurine | Maintenance |
| CHEBI:4450 | Desmopressin | DI treatment |
| CHEBI:17489 | Nicotine | Environmental risk factor |

### MAXO Terms

| MAXO ID | Term | Application |
|---------|------|-------------|
| NCIT:C15986 | Chemotherapy | VBL/pred, cladribine |
| MAXO:0001525 | Targeted therapy | BRAF/MEK inhibitors |
| MAXO:0000647 | Hormone replacement | DI, APD |
| MAXO:0000747 | HSCT | Salvage refractory LCH |
| MAXO:0000004 | Surgical procedure | Curettage, biopsy |
| MAXO:0000015 | Biopsy | Diagnostic |
| MAXO:0000502 | Immunohistochemistry | CD1a, CD207 |
| MAXO:0000127 | Genetic testing | BRAF, MAP2K1 |
| MAXO:0000610 | PET-CT | Staging |
| MAXO:0000571 | MRI | CNS evaluation |
| MAXO:0000079 | Smoking cessation | PLCH prevention |
| MAXO:0001494 | Checkpoint inhibitor | Experimental |
| MAXO:0000169 | Topical administration | Localized skin |
| MAXO:0000375 | Intralesional injection | Bone lesions |
| MAXO:0001175 | Lung transplantation | End-stage PLCH |
| MAXO:0001176 | Liver transplantation | Sclerosing cholangitis |

### Pathway Terms

| ID | Pathway |
|----|---------|
| KEGG:hsa04010 | MAPK signaling |
| KEGG:hsa04151 | PI3K-Akt signaling |
| KEGG:hsa04380 | Osteoclast differentiation |
| R-HSA-6802957 | Oncogenic MAPK signaling |
| R-HSA-5684996 | MAPK1/MAPK3 signaling |
| WP382 | MAPK signaling pathway |

---

*Report generated from systematic review of 106 publications across 5 research iterations, with 14 confirmed findings supported by validated citations. Last updated: 2026-05-14.*
