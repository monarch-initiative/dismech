---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-16T10:34:56.460986'
end_time: '2026-05-16T11:03:52.593112'
duration_seconds: 1736.13
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Flaccid Myelitis
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
citation_count: 78
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Flaccid Myelitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acute Flaccid Myelitis** covering all of the
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

# Comprehensive Disease Characterization: Acute Flaccid Myelitis (AFM)

---

## 1. Disease Information

### Overview
Acute flaccid myelitis (AFM) is a rare but serious neurologic condition characterized by the acute onset of flaccid limb weakness with magnetic resonance imaging (MRI) evidence of spinal cord gray matter lesions. It primarily affects children and has been described as a "polio-like" illness due to striking clinical similarities to poliomyelitis (PMID: 32143233). AFM was first recognized as a distinct clinical entity in 2012 when a cluster of acute flaccid paralysis cases of unknown etiology was identified in California (PMID: 26720027). The US Centers for Disease Control and Prevention (CDC) began national surveillance in 2014 following 120 confirmed cases (PMID: 38300829).

### Key Identifiers
- **MONDO:** MONDO:0100115 (acute flaccid myelitis) [validated via OLS4 API]
- **ICD-10:** G04.82 (Acute flaccid myelitis)
- **ICD-11:** 8B44.0 (Acute flaccid myelitis)
- **MeSH:** D000080524 (Myelitis, Acute Flaccid)
- **OMIM:** Not applicable (not a Mendelian disorder)
- **Orphanet:** ORPHA:542389

### Synonyms and Alternative Names
- Acute flaccid myelitis (AFM)
- Polio-like illness / polio-like syndrome
- Enteroviral acute flaccid myelitis
- Non-polio enterovirus-associated acute flaccid paralysis
- AFM is a specific subtype within the broader category of acute flaccid paralysis (AFP)

### Information Sources
Disease-level characterization is derived from aggregated surveillance data (CDC national AFM surveillance, European Non-Polio Enterovirus Network [ENPEN]), multicenter clinical cohorts, population-based studies (e.g., Kaiser Permanente Northern California), and individual patient case series.

---

## 2. Etiology

### Disease Causal Factors

AFM is an infectious/post-infectious neurologic disease. The primary causal agent is **Enterovirus D68 (EV-D68)**, a non-polio enterovirus belonging to the *Enterovirus* genus, species *Enterovirus D*, family *Picornaviridae*.

**Evidence for EV-D68 causation:**
- Temporal correlation: Biennial peaks in AFM cases (2014, 2016, 2018) coincided with increased EV-D68 respiratory circulation (PMID: 38300829).
- In Europe, 70% of AFM cases (n=91/130) occurred in years of increased EV-D68 circulation (2016, 2018, 2022), and 37% (48/130) were EV-D68 laboratory-confirmed (PMID: 40444374).
- Mouse models fulfill Koch's postulates: EV-D68 2014 outbreak strains cause paralytic myelitis with infection and loss of spinal cord motor neurons in neonatal mice (PMID: 28231269).
- A systematic review and meta-analysis confirmed the association between EV-D68 detection and acute neurologic outcomes (PMID: 42066114).

Other viruses have been associated with AFM in smaller numbers, including:
- Enterovirus A71 (EV-A71)
- Coxsackieviruses (A and B)
- West Nile virus (PMID: 40622703)
- Adenoviruses
- Other non-polio enteroviruses

### Risk Factors

#### Environmental/Host Risk Factors
> **Search source:** PubMed, CDC, population-based studies

- **Age:** Predominantly affects children; median age 4-9 years depending on cohort (PMID: 33218883, PMID: 30985511). Children under 5 are most susceptible to EV-D68 infection (41.6% of cases) (PMID: 40492725).
- **Sex:** Male sex is a risk factor (PMID: 30985511). In the Turkish cohort, 55.9% were boys (PMID: 33218883).
- **Atopy/Asthma:** History of asthma, atopic dermatitis, or reactive airway disease is a risk factor (PMID: 30985511). EV-D68-positive cases in 2024 were predominantly young children receiving asthma medications (PMID: 40431685).
- **Ancestry:** Asian ancestry was identified as a risk factor in the KPNC population study (PMID: 30985511).
- **Season:** Late summer and early fall, coinciding with enterovirus seasonal circulation (August-November).
- **Preceding viral illness:** Prodromal fever or respiratory symptoms occur in most cases; febrile illness was reported in all patients in the Turkish cohort with a median of 4 days before symptom onset (PMID: 33218883).
- **Low vitamin D levels:** Noted in all patients tested in a post-pandemic case series, though causality is unclear (PMID: 41138534).

#### Genetic Risk Factors
No specific human genetic susceptibility loci have been identified for AFM. The disease is not a Mendelian disorder. Host genetic factors influencing susceptibility remain an area of active investigation. The association with atopy/asthma suggests possible immune genetic modifiers.

### Protective Factors

- **COVID-19 non-pharmaceutical interventions (NPIs):** The biennial AFM pattern was disrupted in 2020, with only 32 cases (compared to expected peak), likely due to masking, hand hygiene, and social distancing measures that reduced EV-D68 circulation (PMID: 34735423, PMID: 40431685).
- **Maternal antibodies/passive immunization:** In mouse models, maternal immunization with inactivated EV-D68 vaccine protected neonatal mice, and antisera transfer showed cross-protective effects (PMID: 29385753).
- **Neutralizing antibodies:** hIVIG containing EV-D68 neutralizing antibodies reduced paralysis in mouse models (PMID: 28968718).

### Gene-Environment Interactions
The interaction between host immune status (particularly innate interferon responses) and viral exposure determines disease outcome. The respiratory epithelium induces a robust type III interferon response that restricts EV-D68 infection, while intestinal epithelium does not (PMID: 34196272). Children with asthma/atopy may have altered antiviral immune responses that increase susceptibility to severe EV-D68 disease.

---

## 3. Phenotypes

### Core Clinical Phenotype

#### Acute Flaccid Limb Weakness
- **Type:** Clinical sign / physical manifestation
- **HPO:** HP:0001371 (Flexion contracture), HP:0001252 (Hypotonia), HP:0003470 (Paralysis), HP:0002460 (Distal muscle weakness), HP:0002515 (Waddling gait)
- **Onset:** Acute; preceded by 1-7 days of prodromal illness. Maximum weakness reached within 4 days from onset (PMID: 30169722).
- **Severity:** Variable, from monoplegia to quadriplegia. 30% require intubation (PMID: 37465770).
- **Pattern:** Typically asymmetric (58% asymmetric in AFM vs 0% in GBS; p<0.001) (PMID: 34747551).
- **Frequency:** 100% (defining feature)
- **Progression:** Acute onset, rapid nadir (median 3 days, shorter than GBS at 8 days; p<0.001) (PMID: 34747551).
- **Quality of life:** Devastating; most patients have persistent weakness. Less than 10% have full recovery (PMID: 37465770). In the KPNC study, 41% had full recovery at 12 months, but several had significant deficits (PMID: 30985511).
- **HPO terms:** HP:0002460 (Distal muscle weakness), HP:0009053 (Flaccid paralysis of limbs)

#### Prodromal Respiratory/Febrile Illness
- **Type:** Symptom
- **HPO:** HP:0001945 (Fever), HP:0002788 (Upper respiratory tract infection)
- **Onset:** 1-7 days before weakness onset
- **Frequency:** ~90% in peak years; lower in non-peak years (PMID: 38300829, PMID: 33218883)
- **Severity:** Mild to moderate
- **Quality of life:** Transient; self-limited

#### Spinal Cord Gray Matter Lesions on MRI
- **Type:** Radiological finding / laboratory abnormality
- **HPO:** HP:0002196 (Myelopathy)
- **Description:** T2 hyperintensity predominantly involving central gray matter of the spinal cord (PMID: 33218883, PMID: 26720027)
- **Frequency:** >90% (56/59 in California series) (PMID: 26720027)
- **Specificity:** Distinguishing feature from GBS (spinal cord lesions only found in AFM, not GBS) (PMID: 34747551)
- **LOINC consideration:** MRI spinal cord evaluation

#### Cerebrospinal Fluid Pleocytosis
- **Type:** Laboratory abnormality
- **HPO:** HP:0012229 (CSF pleocytosis)
- **Description:** Elevated CSF white blood cell count; CSF leukocyte counts higher in AFM than GBS, while protein concentrations were lower (PMID: 34747551)
- **Frequency:** Variable; ~73% in California series (43/59) (PMID: 26720027), 58% (18/31) in Turkish cohort (PMID: 33218883). Lower frequency in non-peak years (PMID: 38300829).
- **Severity:** Typically mild to moderate pleocytosis

#### Respiratory Failure
- **Type:** Clinical sign
- **HPO:** HP:0002878 (Respiratory failure)
- **Description:** Due to phrenic nerve/diaphragm involvement or bulbar weakness
- **Frequency:** ~30% require intubation (PMID: 37465770)
- **Severity:** Life-threatening; deaths related to AFM are due to respiratory complications
- **Quality of life:** Major impact; some require long-term ventilatory support

#### Cranial Nerve Dysfunction
- **Type:** Clinical sign
- **HPO:** HP:0001291 (Cranial nerve palsy)
- **Description:** Facial, bulbar, or extraocular muscle weakness
- **Frequency:** Present in a subset of patients
- **Severity:** Variable

#### Bowel/Bladder Dysfunction
- **Type:** Clinical sign
- **HPO:** HP:0000020 (Urinary incontinence), HP:0002607 (Bowel incontinence)
- **Description:** Autonomic involvement; all 4 post-pandemic cases experienced bowel/bladder dysfunction (PMID: 41138534)
- **Frequency:** Variable; 36% with persistent sphincter dysfunction requiring catheterization in plasmapheresis cohort (PMID: 41251130)

#### Limb Pain/Myalgia
- **Type:** Symptom
- **HPO:** HP:0003326 (Myalgia)
- **Description:** Limb myalgia concurrent with or preceding weakness
- **Frequency:** ~70% (41/59 in California series) (PMID: 26720027)

---

## 4. Genetic/Molecular Information

### Causal Genes (Viral)
AFM is not caused by human genetic mutations. The causal genetic elements are viral:

- **EV-D68 VP1 capsid protein gene:** The primary determinant of neurovirulence. Four amino acid differences in VP1 between neurovirulent strain IL52 and non-neurovirulent strain CA4231 completely controlled paralysis phenotype in mouse models (PMID: 38869283).
- **VP3 amino acid 88:** A single isoleucine-to-valine change at position 88 in VP3 attenuated neurovirulence by reducing virus replication in brain and spinal cord (PMID: 32784424).
- **2Apro gene:** The 2A protease cleaves host TRAF3; alterations at the 2Apro/TRAF3 cleavage site affect immune evasion and viral pathogenicity (PMID: 41600837).
- **3Cpro gene:** The 3C protease cleaves host proteins involved in translation and autophagy, including Mitofusin 2 (PMID: 42018625); variations affect replication efficiency and antiviral responses (PMID: 41600837).

### Viral Genomic Evolution (Updated Iteration 3)
- EV-D68 has evolved into multiple clades: A (A1, A2), B (B1, B2, B3), C, D (D1, D2, D3)
- **Molecular origin:** Canada, ~1995; disseminated to France (1997), USA (1999), Asia (2008), with B3 MRCA dated to 2011-01-15 in China (PMID: 37804367)
- **European 2014-2024 surveillance (18 countries, 3,541 EV-D68 of 61,297 EV-positive):** B3 (59.8%) and A2/D (28.0%) predominant; A2/D reemerged as dominant in 2024; mutation analyses revealed changes in antigenic regions (PMID: 41986256)
- In 2024 US, co-circulation of subclades B3 (71%) and A2 (29%) observed (PMID: 40492725)
- B3 subclade primarily associated with pediatric infections (median age 5 years), while A2 more common in adults (median age 42 years) (PMID: 40492725)
- Four amino acid substitutions identified in 2024 B3 genomes: VP2 T145S, 3C I597V, 3D I950V, 3D T2173A (PMID: 40492725)
- Key neuropathogenic site T650A mutation identified in B3 strains (PMID: 40661021)
- **2021-2022 European upsurge:** Two novel B3-derived lineages emerged; 10,481 EV-positive, 1,004 EV-D68 (9.6%); neurological problems in 6.4% of cases but only 6 AFM (PMID: 38547499)
- **Structural biology:** Cryo-EM structures of native virion (2.2 A) and A-particle uncoating intermediate (2.7 A) resolved; revealed acid-initiated uncoating pathway through E1 particle intermediate (PMID: 30530701)
- **Critical unresolved question:** EV-D68 respiratory outbreaks in 2022 and 2024 were NOT associated with AFM surges, despite biennial pattern in 2014-2018 (PMID: 38300829, PMID: 40492725). Possible explanations: (1) evolved strains with reduced neurovirulence, (2) altered population immunity post-pandemic, (3) surveillance gaps, (4) mutations in neurovirulence determinants

### Host Molecular Factors
- **ICAM-5 (Intercellular Adhesion Molecule 5):** Neuron-specific receptor for EV-D68; provides molecular basis for neurotropism (PMID: 41467840)
  - Gene: *ICAM5* (HGNC:5348)
  - Function: Cell adhesion molecule expressed predominantly on telencephalic neurons
- **MFSD6 (Major Facilitator Superfamily Domain Containing 6):** Essential entry receptor for EV-D68 in respiratory and neuronal cells (PMID: 41467840)
  - Gene: *MFSD6* (HGNC:24711)
- **Sialic acid (Neu5Ac):** α2,6-linked sialic acid serves as attachment factor for historical EV-D68 strains
  - CHEBI: CHEBI:26667 (sialic acid)
- **Mitofusin 2 (MFN2):** Cleaved by EV-D68 3C protease, inducing mitochondrial fragmentation and mitophagosome formation (PMID: 42018625)
  - Gene: *MFN2* (HGNC:16877)
- **TRAF3:** Cleaved by EV-D68 2A protease to evade innate immunity (PMID: 41600837)
- **STING (STING1/TMEM173):** Hijacked by EV-D68 for a non-canonical pro-viral function — formation of specialized lipid replication organelles; co-localizes with glycolytic enzymes within ROs (PMID: 39459875)
  - Gene: *STING1* (HGNC:27962)
- **Piezo1:** Mechanosensitive ion channel; mediates the mechano-antiviral response system (MARS), a non-canonical antiviral pathway that reduces membrane fluidity to restrict viral entry. Piezo1 agonists protect against EV-D68 neurological damage in vivo (PMID: 41650963)
  - Gene: *PIEZO1* (HGNC:13680)
- **ARRDC3:** Host antiviral factor induced by enterovirus infection; promotes lysosomal degradation of YAP, which otherwise facilitates viral replication by suppressing IFN responses (PMID: 40701343)
  - Gene: *ARRDC3* (HGNC:28633)

### Epigenetic Information
No specific epigenetic alterations have been reported for AFM susceptibility in host cells.

### Chromosomal Abnormalities
Not applicable; AFM is not associated with chromosomal abnormalities.

---

## 5. Environmental Information

### Environmental Factors
- **Seasonality:** Late summer through fall (August-November) in temperate climates, corresponding to enterovirus circulation season. Wastewater surveillance confirms national US peak in September, with seasonal peaks occurring 28-31 days earlier in regions with 5°C higher temperatures/dew points (PMID: 41853773).
- **Geographic clustering:** Cases cluster in association with regional EV-D68 respiratory outbreaks. Season duration is longer by 7-11 weeks in dense, urban catchments with more childcare facilities, crowded households, and hospitals (PMID: 41853773).
- **Non-pharmaceutical interventions:** COVID-19 pandemic NPIs (masking, hand hygiene, social distancing) disrupted EV-D68 transmission and the biennial AFM pattern in 2020 (PMID: 34735423).
- **Climate factors:** Temperature and dew point influence seasonal timing; warmer regions see earlier EV-D68 peaks (PMID: 41853773).

### Lifestyle Factors
No specific lifestyle factors have been identified beyond the association with atopy/asthma, which may reflect underlying immune phenotype rather than modifiable lifestyle factors.

### Infectious Agents

**Primary agent:**
- **Enterovirus D68 (EV-D68)**
  - NCBI Taxonomy: TaxID 42789
  - Family: Picornaviridae
  - Genus: Enterovirus
  - Species: Enterovirus D
  - Genome: Positive-sense single-stranded RNA (~7.4 kb)
  - First isolated: 1962 from children with pneumonia (Fermon strain)
  - Unique among enteroviruses: resembles human rhinoviruses in acid lability and temperature sensitivity (PMID: 41868141)

**Other associated agents:**
- Enterovirus A71 (EV-A71) - NCBI TaxID 39054
- Coxsackieviruses (A and B species)
- West Nile virus (rare AFM cause in adults)
- Adenoviruses (rarely)

---

## 6. Mechanism / Pathophysiology

### Causal Chain: From Viral Infection to Clinical Paralysis

The pathophysiological cascade of AFM proceeds through the following steps:

**1. Respiratory Entry and Replication (Upstream)**
- EV-D68 enters via the respiratory tract, binding to α2,6-linked sialic acid and/or MFSD6 on respiratory epithelial cells (PMID: 41467840)
- Viral replication in the respiratory epithelium triggers a type III interferon response (PMID: 34196272)
- The virus can use clathrin-mediated endocytosis and compensatory macropinocytosis for entry (PMID: 42037410)

**2. Systemic/Neural Spread (Intermediate)**
- EV-D68 spreads from respiratory tract to the central nervous system, likely via retrograde axonal transport from infected skeletal muscle to spinal cord motor neurons
- In mouse models, skeletal muscle and spinal cord had the highest viral titers (PMID: 41305500)
- Viremia may also contribute to neural spread

**3. Motor Neuron Infection (Intermediate)**
- EV-D68 binds ICAM-5 (neuron-specific receptor) for entry into spinal cord motor neurons (PMID: 41467840)
- Viral replication in motor neurons of the anterior horn cells
- GO terms: GO:0019058 (viral life cycle), GO:0044409 (entry into host cell)

**4. Cell Death and Immune-Mediated Damage (Downstream)**
- **Direct cytopathology:** EV-D68 infection causes motor neuron death through:
  - Mitochondrial dysfunction: EV-D68 3C protease cleaves Mitofusin 2, causing mitochondrial fragmentation (PMID: 42018625)
  - Oxidative stress: RNA-seq of infected spinal cords shows mitochondrial dysfunction and oxidative stress pathways (PMID: 41305500)
  - GO terms: GO:0008219 (cell death), GO:0006915 (apoptosis)

- **Immune-mediated secondary injury:**
  - EV-D68 activates innate and adaptive immunity with significant CD8+ T cell infiltration into spinal cord (PMID: 41305500)
  - Interferon signaling and cytokine storm pathways activated (PMID: 41305500)
  - Human spinal cord organoids infected with EV-D68 show productive infection for 2+ weeks without appreciable cytopathic effect, suggesting immune-mediated mechanisms are important contributors to pathology in vivo (PMID: 37535397)
  - GO terms: GO:0006955 (immune response), GO:0006954 (inflammatory response)

**5. Motor Neuron Loss and Clinical Paralysis (Downstream)**
- Loss of anterior horn motor neurons produces lower motor neuron paralysis
- Wallerian degeneration of motor axons follows
- Clinical manifestation as acute flaccid limb weakness
- CL terms: CL:0011001 (spinal cord motor neuron), CL:0000100 (motor neuron)
- UBERON terms: UBERON:0002257 (ventral horn of spinal cord), UBERON:0014621 (cervical spinal cord ventral horn)

### Molecular Pathways

- **Interferon signaling:** Type I and Type III interferon responses activated in respiratory and neural tissues; type I IFN receptor is important for host defense (mice lacking IFNAR are highly susceptible) (PMID: 32784424)
  - Reactome: R-HSA-913531 (Interferon Signaling)

- **Autophagy/Mitophagy:** EV-D68 induces nonselective autophagy and mitophagy via Mitofusin 2 cleavage; mitophagosomes serve as vectors for nonlytic viral release (PMID: 42018625)
  - GO: GO:0006914 (autophagy), GO:0000422 (autophagy of mitochondria)

- **NF-kB/TRAF3 pathway:** EV-D68 2A protease cleaves TRAF3 to evade innate immunity (PMID: 41600837)
  - Reactome: R-HSA-975138 (TRAF6-mediated NF-kB activation)

- **Cytokine signaling:** DEGs enriched in cytokine-cytokine receptor interaction and JAK-STAT pathways (PMID: 41305500)
  - KEGG: hsa04630 (JAK-STAT signaling pathway)

### Immune Evasion Mechanisms (Iteration 2 Addition)

EV-D68 employs a multi-layered immune evasion strategy targeting the type I IFN pathway at three distinct nodes:

1. **VP3-MAVS interaction (receptor-proximal):** VP3 structural protein co-localizes and interacts with MAVS, disrupts mitochondrial membrane potential, releases MAVS from mitochondria, and inhibits NF-kB signaling. VP3 binds to the transmembrane domain of MAVS. This is a broad-spectrum enterovirus strategy (PMID: 40042308).

2. **3C protease-STAT1 cleavage (downstream signaling):** EV-D68 3C protease cleaves STAT1 at the 131Q residue, abolishing STAT1 nuclear translocation and attenuating IFN signal transduction. Notably, this ability is shared with poliovirus 3C protease but NOT with EV-A71, CVA16, or echoviruses — potentially explaining the shared polio-like phenotype between EV-D68 and poliovirus (PMID: 38240591).

3. **USP5 deubiquitinase exploitation (upstream of IFN induction):** EV-D68 infection upregulates USP5, which reduces K63-linked polyubiquitination of MAVS and IRF3, decreasing IFN-I production. Pharmacological USP5 inhibition with PR-619 potentiated antiviral IFN effects, suggesting a therapeutic target (PMID: 41352537).

4. **3C protease-MDA5 disruption:** EV-D68 3C protein cleaves MDA5, a key cytoplasmic viral RNA sensor, disrupting innate immune detection of viral RNA (PMID: 28424289).

### Novel Host Defense Mechanisms (Iteration 4 Addition)

1. **Mechano-Antiviral Response System (MARS) via Piezo1:** Cellular compression or fluid pressure activates Piezo1-dependent antiviral resistance by reducing host cell membrane fluidity, restricting viral entry. Piezo1 agonists or mechanical stimuli alleviate EV-D68-induced neurological damage and lethality in vivo. This represents a non-canonical antiviral strategy distinct from interferon signaling (PMID: 41650963).

2. **STING hijacking for replication organelles:** EV-D68 hijacks STING (stimulator of interferon genes) for a non-canonical, pro-viral function — formation of specialized lipid replication organelles (ROs). STING co-localizes with glycolytic enzymes within ROs, and its inhibition modulates glucose metabolism in infected cells. This reveals that STING has dual roles: canonical antiviral DNA sensing AND non-canonical pro-viral membrane remodeling exploited by RNA viruses (PMID: 39459875).

3. **ARRDC3-YAP antiviral pathway:** Enterovirus infection induces ARRDC3 (Arrestin Domain Containing 3), which promotes lysosomal degradation of YAP (Yes-associated protein). YAP facilitates enterovirus replication by suppressing the interferon pathway during later stages of infection. The ARRDC3-YAP axis exhibits broad-spectrum antiviral activity (PMID: 40701343).

4. **TRIM25 restoration of RIG-I:** EV-D68 3C protease reduces both RIG-I and TRIM25 expression. Overexpression of TRIM25 restores RIG-I expression and IFN-β production, suggesting TRIM25 as a potential therapeutic target (PMID: 34170466).

### Cellular Processes
- **Apoptosis** of motor neurons (GO:0006915)
- **Neuroinflammation** with CD8+ T cell, macrophage infiltration (GO:0006954)
- **Mitochondrial dysfunction** and oxidative stress (GO:0006979)
- **Mitochondrial fission** via MFN2 cleavage (GO:0000266)
- **Viral immune evasion** via protease-mediated host protein cleavage (GO:0030683)
- **Type I interferon signaling suppression** (GO:0060339 - negative regulation of type I interferon-mediated signaling pathway)

### Protein Dysfunction
- **Mitofusin 2 cleavage:** EV-D68 3C protease cleaves MFN2 near C-terminal HR2 domain, causing mitochondrial fragmentation (PMID: 42018625)
- **TRAF3 degradation:** 2A protease cleaves TRAF3, impairing innate immune signaling (PMID: 41600837)
- **Host translation shutoff:** Enteroviral proteases cleave eIF4G and other translation factors

### Metabolic Changes
- Mitochondrial dysfunction leads to altered energy metabolism in infected motor neurons (PMID: 41305500)
- Oxidative stress pathways activated

### Immune System Involvement
- **Innate immunity:** Type III interferon response in respiratory epithelium restricts EV-D68 (PMID: 34196272); type I IFN critical for limiting CNS infection
- **Adaptive immunity:** CD8+ T cell response in spinal cord; may contribute to immunopathology (PMID: 41305500)
- **Immune evasion:** EV-D68 employs multiple strategies including TRAF3 cleavage, translational shutoff, and autophagy manipulation
- **Autoimmunity:** Not the primary mechanism, distinguishing AFM from autoimmune myelitis

### Tissue Damage Mechanisms
- Direct viral cytopathic effect on motor neurons
- Immune-mediated inflammatory damage in spinal cord
- Oxidative stress (GO:0006979)
- Mitochondrial dysfunction and energy failure

### Molecular Profiling

#### Transcriptomics
- RNA sequencing of EV-D68-infected mouse spinal cord revealed DEGs significantly enriched in antiviral immunity, interferon responses, cytokine signaling, mitochondrial dysfunction, and oxidative stress pathways (PMID: 41305500)
- GEO datasets available for EV-D68-infected cells and tissues

#### Functional Genomics
- VP1 chimeric virus studies identified four key amino acid positions controlling neurovirulence (PMID: 38869283)
- VP3 position 88 (Ile>Val) as single attenuation determinant (PMID: 32784424)

---

## 7. Anatomical Structures Affected

### Organ Level
**Primary organs:**
- **Spinal cord** (UBERON:0002240) - Primary site of pathology; gray matter predominantly affected
- **Skeletal muscle** (UBERON:0001134) - Secondary to denervation and direct viral infection

**Secondary organ involvement:**
- **Brain/brainstem** (UBERON:0002298) - Brainstem involvement with cranial nerve nuclei in some cases; posterior brainstem T2 signal changes reported (PMID: 38405019)
- **Lungs** (UBERON:0002048) - Respiratory failure due to diaphragm paralysis; respiratory tract as primary site of viral entry
- **Bladder** (UBERON:0001255) - Autonomic dysfunction with urinary retention

**Body systems involved:**
- Nervous system (central and peripheral)
- Respiratory system
- Musculoskeletal system
- Autonomic nervous system

### Tissue and Cell Level
- **Spinal cord gray matter** (UBERON:0002315) - Anterior horn cells predominantly affected
- **Motor neurons** (CL:0000100) - Primary cellular target; infection and loss documented
- **Skeletal muscle fibers** - Denervation atrophy secondary to motor neuron loss; direct viral tropism to muscle also documented (PMID: 41305500)
- **Respiratory epithelial cells** (CL:0002368) - Initial site of infection
- **Neurons** broadly (CL:0000540) - ICAM-5-expressing neurons susceptible

### Subcellular Level
- **Mitochondria** (GO:0005739) - Fragmentation due to Mitofusin 2 cleavage (PMID: 42018625)
- **Endoplasmic reticulum** - Viral replication complexes
- **Autophagosomes/mitophagosomes** (GO:0005776) - Formed during infection for viral release (PMID: 42018625)
- **Cell membrane** - Receptor interactions and viral entry

### Localization
- **Spinal cord:** Cervical cord most commonly affected (especially for upper extremity weakness); thoracic and lumbar segments also involved
- **UBERON:** UBERON:0002726 (cervical spinal cord), UBERON:0002257 (ventral horn of spinal cord)
- **Lateralization:** Typically asymmetric (58% of cases), though bilateral involvement occurs; one limb may be affected more severely than contralateral (PMID: 34747551)
  - HPO: HP:0003685 (Asymmetric limb weakness)

---

## 8. Temporal Development

### Onset
- **Typical age of onset:** Predominantly pediatric; median age 4-9 years across studies (PMID: 33218883, PMID: 30985511, PMID: 26720027). The median age has been observed to decrease with successive outbreaks (PMID: 33218883).
- **Onset pattern:** **Acute**; prodromal febrile/respiratory illness 1-7 days prior, followed by rapid onset of flaccid weakness
- **Seasonality:** Late summer through fall (August-November)

### Progression
- **Prodromal phase (days 1-7):** Fever, upper respiratory infection, gastrointestinal illness
- **Acute paralytic phase (hours to days):** Rapid onset flaccid weakness; maximum weakness reached within median 3 days from onset of limb weakness (PMID: 34747551)
- **Nadir phase (days to weeks):** Stabilization of weakness at maximal severity
- **Recovery phase (months to years):** Slow, incomplete recovery in most patients

- **Progression rate:** Rapid to nadir; much faster than GBS (3 vs 8 days, p<0.001) (PMID: 34747551)
- **Disease course:** Monophasic (single acute episode); not relapsing-remitting
- **Disease duration:** Acute phase resolves over weeks, but deficits are often chronic/permanent

### Patterns
- **Spontaneous recovery:** Limited; among patients with complete paralysis (MRC grade 0) at >6 months with hip adductor paralysis, no patient improved to better than MRC grade 2 (PMID: 38815052). Recovery plateaus around 6-9 months (PMID: 32951650).
- **Critical periods:**
  - First 6-9 months: Window for maximal spontaneous recovery
  - Nerve transfer surgery: Best outcomes when performed within 8 months of paralysis onset (PMID: 38815052)
  - Antiviral treatment: Mouse models show benefit even when initiated 4-6 days post-infection (PMID: 41667472)

---

## 9. Inheritance and Population

### Epidemiology

#### Incidence
- **United States:**
  - 2014: 120 confirmed cases
  - 2016: 153 confirmed cases
  - 2018: 238 confirmed cases (peak year)
  - 2019: 47 cases
  - 2020: 32 cases (pandemic-related reduction)
  - Overall: Approximately 1 per million children per year in non-peak years; higher in peak years
  - KPNC population-based estimate: 1.46 per 100,000 person-years (children 1-18 years, 2011-2016) (PMID: 30985511)

- **Europe:** 130 reported cases across 14 countries (2016-2023), though significant underreporting suspected due to lack of systematic surveillance in most countries (PMID: 40444374)

#### Prevalence
- AFM is an acute disease; point prevalence is very low
- Estimated thousands of patients living with chronic sequelae from past outbreaks

#### EV-D68 Seroprevalence (Updated Iteration 4)
- **Systematic review of global age-stratified seroprevalence** (10 studies, 6 countries): Seroprevalence increases rapidly with age, reaching ~100% by age 20 years with no decline throughout adulthood, suggesting continuous or frequent exposure. Studies with multiple cross-sectional surveys reported consistently higher seroprevalence at later timepoints, indicating global increase in transmission over time. Standardization of serological protocols and understanding cross-reactivity remain key research priorities (PMID: 39332429).
- Beijing healthy population: seroprevalence 89.4% (2012) to 98.4% (2017); GMT rose from 92.82 to 242.91 (PMID: 32492201)
- Acute-phase sera from EV-D68 patients had NtAb titers ≤1:64; convalescent sera >1:64, suggesting titer ≤1:64 may indicate susceptibility
- Most EV-D68 infections are subclinical; AFM occurs in a tiny fraction of infected individuals
- Population immunity levels fluctuate with exposure cycles, contributing to biennial outbreak pattern

### Inheritance Pattern
- **Not applicable for genetic inheritance** - AFM is an infectious disease, not a Mendelian disorder
- No familial clustering has been reported
- Host susceptibility is likely polygenic/multifactorial

### Population Demographics

#### Affected Populations
- **Age:** Predominantly children; median age 4-9 years; >90% cases in children under 16 years (PMID: 39246649)
- **Sex ratio:** Male predominance; approximately 56% male (PMID: 33218883); male sex identified as risk factor (PMID: 30985511)
- **Ancestry:** Asian ancestry identified as a risk factor in one US population study (PMID: 30985511); further studies needed
- **Atopic individuals:** Higher risk with history of asthma/atopic dermatitis

#### Geographic Distribution
- **Global:** Cases reported worldwide including North America, Europe, Asia, Australia, India
- **United States:** Nationwide distribution with biennial outbreaks
- **Europe:** Cases reported in at least 14 countries (PMID: 40444374)
- **Asia:** Cases reported in Turkey, China, India, Japan, and others
- **Australia:** Previously unrecognized cluster identified (PMID: 32178602)

#### Age Distribution
- Peak incidence: 2-8 years old
- Occasional cases in adolescents and adults (more common post-pandemic) (PMID: 41138534)
- Adult cases are atypical and may have different etiologies

---

## 10. Diagnostics

### Clinical Tests

#### Laboratory Tests
- **Cerebrospinal fluid (CSF) analysis:**
  - Pleocytosis (elevated WBC count) in 50-73% of cases
  - Protein typically normal or mildly elevated (lower than in GBS)
  - Glucose normal
  - EV-D68 rarely detected in CSF by RT-PCR (<2% of cases)
  - LOINC: 26465-7 (WBC count in CSF)

- **Respiratory specimen RT-PCR:**
  - Nasopharyngeal swab for rhinovirus/enterovirus testing
  - EV-D68-specific RT-PCR on RV/EV-positive specimens
  - Best sensitivity if collected within first few days of respiratory illness
  - LOINC: 92141-1 (Enterovirus D68 RNA in specimen by NAA)

- **Stool specimen:** For enterovirus detection; lower yield for EV-D68 than for other enteroviruses

#### Biomarkers
- **CSF cytokine profile:** The pro-inflammatory cytokines/chemokines IP-10 (CXCL10) and IL-6 were significantly elevated in CSF of confirmed AFM patients compared to non-AFM controls, when measured as CSF-to-serum ratios (PMID: 32836175). These biomarkers may reflect intrathecal inflammation and provide insight into pathogenic mechanisms.
- **CSF pleocytosis** and characteristic MRI pattern remain the primary diagnostic markers
- No validated serum biomarkers specific to AFM currently exist
- Neurofilament light chain (NfL), a marker of axonal injury used in other neurologic diseases, has not been systematically studied in AFM but represents a promising candidate biomarker

#### Imaging Studies
- **Spinal cord MRI (T2-weighted):**
  - T2 hyperintensity predominantly involving central gray matter
  - Longitudinally extensive lesions possible
  - Cervical cord most commonly affected
  - Gray matter predominance distinguishes from demyelinating lesions
  - 95% sensitivity for confirmed AFM (PMID: 26720027)

- **Brain MRI:**
  - May show brainstem lesions (posterior brainstem/dorsal pons/medulla) in some cases (PMID: 38405019)
  - Abnormal brain MRI at onset associated with poor prognosis (PMID: 33218883)

#### Electrophysiology
- **EMG/Nerve Conduction Studies (NCS):**
  - Findings consistent with motor neuronopathy/anterior horn cell disease
  - Decreased compound muscle action potential (CMAP) amplitudes
  - Preserved sensory nerve action potentials (SNAPs)
  - Denervation potentials (fibrillations, positive sharp waves) on needle EMG
  - Confirms severe motor neuron injury (PMID: 41138534)
  - Preoperative EMG/NCS predicts outcomes after nerve transfer (PMID: 37981447)

### Genetic Testing
- **Not applicable** for diagnosis of AFM, which is an infectious disease
- No genetic testing panels exist for AFM susceptibility
- Viral genomic sequencing (VP1 gene) is used for EV-D68 strain typing and epidemiological surveillance

### Clinical Criteria

#### CDC Case Definition (Current Standard)
- **Confirmed AFM:** Acute-onset flaccid limb weakness AND MRI showing spinal cord lesion largely restricted to gray matter spanning one or more vertebral segments
- **Probable AFM:** Acute-onset flaccid limb weakness AND CSF showing pleocytosis (WBC >5 cells/mm3)
- Must exclude clear alternative diagnoses

#### Diagnostic Criteria Evaluation (PMID: 36996587)
A Dutch cohort study evaluating AFM diagnostic criteria in 141 children with acute limb weakness found:
- Only 7/9 patients initially classified as "definite AFM" retained this label after expert review
- Patients initially classified as probable/possible AFM were most commonly re-diagnosed with transverse myelitis (16/25)
- When initial classification was "uncertain," GBS was the most common final diagnosis (31/43)
- Highlights the challenge of early AFM diagnosis and the importance of expert neurological evaluation

#### Differential Diagnosis
Key conditions to distinguish from AFM (PMID: 32143233, PMID: 34747551, PMID: 31338675):

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Guillain-Barre syndrome (GBS)** | Symmetric weakness; longer time to nadir (8 vs 3 days); sensory deficits (40% vs 0%); elevated CSF protein; demyelinating pattern on NCS; no spinal cord MRI lesions |
| **Transverse myelitis** | White matter > gray matter on MRI; sensory level; autoimmune markers; responds to immunotherapy |
| **Spinal cord stroke** | Hyperacute onset; vascular risk factors; anterior spinal artery distribution |
| **Poliomyelitis** | Similar presentation; poliovirus detected; travel/exposure history |
| **MOG-antibody myelitis** | MOG-IgG positive; longitudinally extensive T2 lesion; responds to immunotherapy; may relapse (PMID: 30575890) |
| **Spinal cord tumor** | Progressive rather than acute; mass lesion on MRI |

### Screening
- No population-based screening programs exist for AFM
- CDC conducts passive national surveillance
- Active EV-D68 respiratory surveillance at sentinel sites to anticipate potential AFM outbreaks (PMID: 40431685)

---

## 11. Outcome/Prognosis

### Survival and Mortality
- **Mortality:** Low but non-zero; deaths occur due to respiratory failure from diaphragm/bulbar muscle involvement (PMID: 37465770)
- **Life expectancy:** Most patients survive with disability; limited data on long-term life expectancy
- **Disease-specific mortality:** Related to respiratory complications, particularly in patients with quadriplegia or brainstem involvement

### Morbidity and Function
- **Persistent weakness:** 89% (24/27) with persistent weakness in Turkish cohort (PMID: 33218883)
- **Full recovery rate:** <10% overall (PMID: 37465770); 41% in KPNC population study at 12 months (PMID: 30985511)
- **Disability outcomes:**
  - Limb paralysis requiring assistive devices
  - Diaphragm paralysis requiring ventilatory support or phrenic nerve reconstruction
  - Bowel/bladder dysfunction (36% persistent sphincter dysfunction in some cohorts) (PMID: 41251130)
- **Quality of life:** Significant impairment; children may require wheelchair, bracing, or assistive devices. Functional recovery typically plateaus at 6-9 months (PMID: 32951650).
- **Psychosocial impact:** 3/8 children reported depressive symptoms at 1-year follow-up in Colorado cohort (PMID: 28615421).

### Longitudinal Outcome Data (Iteration 2 Addition)

**3-Year Follow-up (Japan, n=33)** (PMID: 33388543):
- Complete recovery rates by initial severity: tetraplegia/triplegia 2/7 (29%), paraplegia 4/13 (31%), monoplegia 2/13 (15%)
- 27% showed continued improvement between 6-month and 3-year timepoints
- Barthel index significantly improved at chronic stage (P<0.001; median difference 53, 95% CI: 40-63)
- All 6 EV-D68-positive patients had persistent motor deficits
- Non-motor neurological findings (cranial nerves, sensory) had better prognosis than motor weakness

**1-Year Follow-up (Colorado, n=12)** (PMID: 28615421):
- 6/8 completing study had persistent motor deficits; 2 fully recovered
- Proximal muscles: minimal to no improvement with significant atrophy
- Distal muscles: all patients improved
- Cranial nerve dysfunction: resolved in 2/5, improved in all
- Repeat MRI showed significant improvement or normalization in all but one
- Repeat EMG: ongoing denervation and chronic reinnervation in those with persistent deficits
- Pain: 2/8 at 1 year; depressive symptoms: 3/8

**Long-term Respiratory Outcomes (KPNC, n=37, median 4.7 years follow-up)** (PMID: 39657203):
- 21.6% had respiratory failure during index hospitalization
- Among those with respiratory failure, 75% required follow-up respiratory support
- Respiratory failure associated with: higher Modified Rankin Scores (mean diff 1.29, 95% CI: 0.34-2.23), higher respiratory-related ED visits (IRR 1.94, 95% CI: 1.27-2.96)
- Overall AFM incidence: 0.6 per 100,000 person-years

**Texas Cohort (n=21, ~2 years follow-up)** (PMID: 32192819):
- 5 fully recovered; 5 able to perform all ADLs independently; 5 mild deficits; 6 substantial caregiver reliance
- No treatment differences detected (IVIG, steroids, plasmapheresis all used)

### Prognostic Factors
- **Poor prognosis:**
  - Quadriplegia (four-limb involvement) (PMID: 33218883)
  - Abnormal brain MRI at onset (PMID: 33218883)
  - Complete paralysis (MRC grade 0) at >6 months with hip adductor involvement (PMID: 38815052)
  - Abundant acute denervation potentials on EMG (PMID: 37981447)

- **Better prognosis:**
  - Monoplegia/limited limb involvement
  - EV-D68 confirmed (potentially related to host immune response) (PMID: 41138534)
  - Shorter hospital stay (PMID: 41138534)
  - Younger age at presentation
  - Earlier nerve transfer surgery (<8 months post-onset) (PMID: 38815052)

---

## 12. Treatment

### Pharmacotherapy

**No FDA-approved treatments exist for AFM.** Management is primarily supportive with empirical immunomodulatory therapies.

#### Empirical Immunotherapy
- **Intravenous immunoglobulin (IVIG):**
  - Most commonly used treatment; rationale based on potential neutralizing antibody content
  - hIVIG containing EV-D68 neutralizing antibodies reduced paralysis in mouse models (PMID: 28968718)
  - Clinical evidence limited to case series; no randomized controlled trials
  - MAXO: MAXO:0001298 (intravenous immunoglobulin therapy)

- **Corticosteroids:**
  - Widely used empirically (42/59 patients in California received IV steroids) (PMID: 26720027)
  - **CAUTION:** Dexamethasone worsened motor impairment, increased mortality, and increased viral loads in mouse model (PMID: 28968718)
  - MAXO: MAXO:0000609 (corticosteroid therapy)

- **Therapeutic plasma exchange (TPE) / Plasmapheresis:**
  - Used as second/third-line therapy
  - In a pediatric cohort (n=23), 74% (17/23) showed significant improvement by end of treatment; median mRS improved from 5 to 4 at end of TPE and to 2 at 6 months (PMID: 41251130)
  - Two deaths reported in this cohort (one from venous air embolism)
  - MAXO: MAXO:0001077 (plasmapheresis)

- **Fluoxetine:**
  - Investigated based on in vitro antiviral activity against enteroviruses
  - **No effect** on motor impairment or viral loads in mouse model (PMID: 28968718)
  - Not recommended based on available evidence

### Advanced Therapeutics

#### Antiviral Drug Candidates (Experimental)
No antivirals are currently approved; several candidates are in development:

- **VP1 capsid inhibitors (Jun11787, Jun11695):**
  - Structure-based design; bind hydrophobic canyon in VP1
  - Nanomolar potency against multiple EV-D68 strains in vitro
  - Reduce spinal cord viral titer, prevent paralysis progression in mice even when treatment initiated 4-6 days post-infection (PMID: 41667472)

- **2C helicase inhibitors (Jun6504):**
  - Broad-spectrum activity against EV-D68, EV-A71, CVB3
  - Significantly improves paralysis score in neonatal mouse model (PMID: 40593720)

- **Orally available peptidomimetic 2C inhibitor (2CA-1):**
  - Excellent oral bioavailability; broad enterovirus activity (PMID: 41485562)

- **Fluoxetine analogues (compound 53):**
  - Optimized from (S)-fluoxetine targeting 2C ATPase; improved potency (PMID: 41621223)

- **VP1 protein degraders (PROTACs):**
  - Targeted protein degradation strategy to overcome capsid inhibitor resistance (PMID: 42063851)

- **Matrine (natural product):**
  - Alkaloid with broad-spectrum antiviral activity via autophagy activation (PMID: 41205525)

- **Geranyl-p-trans-coumaric acid (GCA):**
  - Natural product EV-D68 inhibitor (PMID: 41175053)

- **RNA-encoded VHH antibodies:**
  - repRNA-encoded nanobodies protected mice from EV-D68 challenge (PMID: 41964219)

#### Vaccine Candidates (Experimental)
No vaccines are approved; multiple platforms in development:

- **mRNA VLP vaccine:**
  - mRNA expressing EV-D68 virus-like particles elicited potent neutralizing antibodies superior to inactivated whole virion vaccine; protective in mice; also attenuated CVB3 infection (PMID: 41210583)

- **Self-amplifying RNA (saRNA) vaccine:**
  - Clinical-stage RNA vaccine platform induced robust EV-D68-neutralizing antibody responses in both mice and nonhuman primates; prevented upper and lower respiratory tract infections and neurological disease in mice. Characterized antigenic diversity across six EV-D68 genotypes to inform multivalent vaccine composition for optimal breadth of neutralizing responses. Represents proof-of-concept for RNA vaccines against nonenveloped viruses (PMID: 39110777).

- **Inactivated whole virion vaccine:**
  - Formalin-inactivated EV-D68 from serum-free HEK293A suspension culture; induced neutralizing responses including against recent circulating strains (PMID: 42086005)

- **Multi-epitope vaccine (in silico):**
  - Immunoinformatic design targeting VP proteins with T-cell and B-cell epitopes (PMID: 41483695)

### Surgical and Interventional

#### Nerve Transfer Surgery
- **MAXO:** MAXO:0000014 (surgical procedure)
- Primary surgical intervention for AFM patients with persistent severe weakness
- Redirects functioning donor nerves to denervated recipient muscles
- Among muscles with preoperative MRC grade 0, nerve transfers achieved MRC grade 2.17 vs 0 for untreated muscles (P=0.0001) (PMID: 37981447)
- Best outcomes when surgery performed within 8 months of paralysis onset (PMID: 38815052)
- **Upper extremity transfers:**
  - Spinal accessory nerve to suprascapular nerve (most common)
  - Radial nerve to axillary nerve (best functional returns, mean AMS 6.5) (PMID: 32951650)
  - Intercostal nerves to axillary nerve
- **Lower extremity transfers:**
  - Contralateral obturator nerve to femoral nerve (CONFNT) for knee extension; 2/5 patients achieved MRC grade 4 when performed ≤8 months (PMID: 38815052)

#### Phrenic Nerve Reconstruction
- For diaphragm paralysis; 100% of patients with unilateral paralysis showed improvement (PMID: 39933731)
- Improvement documented by fluoroscopic sniff testing, pulmonary function tests, and electrodiagnostic evaluation

### Supportive and Rehabilitative
- **Intensive care support:** Mechanical ventilation for respiratory failure (30% require intubation)
- **Physical therapy:** Crucial for maintaining range of motion and maximizing recovery
- **Occupational therapy:** Adaptive equipment, functional training
- **Orthotic management:** Braces, splints for affected limbs
- **Respiratory rehabilitation:** For those with diaphragm involvement
- **MAXO:** MAXO:0000502 (physical therapy), MAXO:0001001 (respiratory support)

### Comprehensive Surgical Reconstruction (Iteration 3 Addition)

**Upper extremity reconstruction** (PMID: 38774108):
- Study of 39 patients, 50 upper extremities (2011-2019)
- Patients with complete paralysis of shoulder abduction at 6 months showed no later spontaneous recovery
- 22 patients (24 extremities) underwent shoulder surgery: nerve transfer, muscle-tendon transfer, or free muscle transfer
- Both spinal accessory nerve transfer and contralateral C7 nerve root transfer to suprascapular nerve gave similar shoulder abduction recovery
- MAXO: MAXO:0000014 (surgical procedure)

**Rehabilitation following nerve transfer** (PMID: 33016189):
- Interdisciplinary team approach: OT, PT, surgical team, family
- Pre-operative and six phases of post-operative therapy recommended
- Addresses: assessment, strengthening, range of motion, orthoses, functional activities, family support
- Communication between team members identified as vital
- MAXO: MAXO:0000502 (physical therapy), MAXO:0001351 (occupational therapy)

**Functional outcomes (WeeFIM)** (PMID: 32677590):
- Inpatient rehabilitation with neuropsychological evaluation
- Admission and discharge WeeFIM scores showed deficits most pronounced in self-care and mobility domains
- Multiple nerve transfer surgery performed on 13 limbs in 6 children; AMS improvement in 4 of 6

### Treatment Outcomes
- No treatments have demonstrated efficacy in randomized controlled trials
- Recovery is incomplete in most patients regardless of medical treatment
- Nerve transfer surgery provides the most objective evidence of functional benefit for persistent weakness
- Comprehensive surgical reconstruction (nerve + tendon + free muscle transfer) represents the evolving standard for persistent severe weakness

---

## 13. Prevention

### Primary Prevention

#### Immunization
- **No approved vaccine exists** for EV-D68 or AFM prevention
- Multiple vaccine candidates in preclinical development (see Treatment section)
- Annual influenza vaccination is important to distinguish influenza-associated neurologic disease from AFM

#### Non-Pharmaceutical Interventions
- Hand hygiene, respiratory hygiene, and avoidance of sick contacts during enterovirus season
- COVID-19 pandemic NPIs demonstrated effective disruption of EV-D68 transmission (PMID: 34735423)

### Secondary Prevention (Early Detection)
- **Clinician awareness:** Emergency department is the most common site of first medical encounter for AFM cases (PMID: 37465770)
- **Suspect AFM** in any child with acute flaccid limb weakness, especially with preceding respiratory/febrile illness
- **Rapid MRI** of the spine to confirm gray matter involvement
- **Early respiratory specimen collection** for EV-D68 testing before viral shedding decreases

### Tertiary Prevention
- Early rehabilitation to maximize functional recovery
- Timely surgical evaluation for nerve transfer candidacy (optimal window <8 months)
- Respiratory monitoring for patients with proximal weakness or brainstem involvement

### Public Health
- **CDC national AFM surveillance** (since 2014): Passive reporting system
- **EV-D68 sentinel surveillance:** Active monitoring at pediatric sites to detect circulation increases and anticipate AFM outbreaks (PMID: 40431685)
- **European ENPEN network:** Multinational enterovirus surveillance; identified need for improved AFM-specific surveillance (PMID: 40444374)
- **Environmental/wastewater surveillance:** Longitudinal US wastewater study (43,876 samples, 147 treatment plants, 40 states, July 2023-July 2025) confirmed biennial EV-D68 pattern with national peak in September 2024 and extended 20-month detection period in California. Seasonal peaks occurred 28-31 days earlier in regions with 5°C higher temperatures/dew points. Season duration was longer by 7-11 weeks in dense, urban catchments with more childcare facilities, crowded households, and hospitals. Wastewater concentrations correlated positively with clinical enterovirus diagnoses (Spearman ρ = 0.34, p = 0.01) (PMID: 41853773, PMID: 41410465)

### Genetic Counseling
- Not applicable; AFM is not a hereditary condition
- Families should be counseled that AFM is an infectious complication, not genetic

---

## 14. Other Species / Natural Disease

### Taxonomy
- EV-D68 is primarily a human pathogen
- **Natural hosts:** Humans (NCBI TaxID: 9606) are the only known natural hosts for EV-D68
- No natural animal reservoirs or zoonotic transmission identified

### Comparative Biology
- Poliovirus (closely related enterovirus) also causes anterior horn cell disease; insights from polio eradication efforts inform AFM research
- EV-D68 does not naturally infect other animal species, necessitating adapted mouse models for research

### Transmission
- **Human-to-human transmission** via respiratory droplets
- Possible fecal-oral transmission (EV-D68 detected in stool and wastewater) (PMID: 34196272, PMID: 41410465)
- **No zoonotic potential** identified
- **No cross-species susceptibility** in natural settings

---

## 15. Model Organisms

### Mouse Models

#### Neonatal Mouse Models (Primary Research Platform)
- **Model type:** Mammalian; neonatal mice (7-10 days old)
- **Species/strains:** Swiss Webster (SW), BALB/c, ICR, type I IFN receptor knockout (IFNAR-/-)
- **Inoculation routes:** Intramuscular (most efficient), intracerebral, intraperitoneal, intranasal (PMID: 28231269)

**Key models:**
1. **Neonatal Swiss Webster IM model** (PMID: 28231269):
   - US/MO/14-18947 and US/IL/14-18952 strains cause progressive paralysis
   - Viral infection and loss of motor neurons in anterior horns
   - Fulfills Koch's postulates
   - Used for therapeutic evaluation

2. **Neonatal BALB/c IP model** (PMID: 30503887):
   - Induces both interstitial pneumonia AND acute flaccid myelitis
   - Recapitulates both respiratory and neurologic disease

3. **Mouse-adapted EV-D68 IM model** (PMID: 41305500):
   - Mouse-adapted strain for consistent disease induction
   - RNA-seq and flow cytometry characterization of pathogenesis
   - Spinal cord and skeletal muscle as highest titer tissues

4. **Neonatal IFNAR-/- IP model** (PMID: 32784424):
   - Type I IFN receptor knockout mice are highly susceptible
   - Used for mapping attenuation determinants

### Phenotype Recapitulation
- **Well recapitulated:**
  - Progressive limb paralysis
  - Viral replication in spinal cord motor neurons
  - Motor neuron loss in anterior horns
  - Muscle tropism with high viral titers
  - Histopathologic changes (neuronal necrosis, inflammation)

- **Limitations:**
  - Only neonatal mice susceptible (adult mice resistant); does not fully model pediatric-specific susceptibility
  - Immune system maturity differences between neonatal mice and human children
  - Some routes of inoculation (IM) bypass natural respiratory entry
  - Species-specific receptor differences may affect viral tropism

### Human Organoid Models

#### Spinal Cord Organoids (PMID: 37535397, PMID: 42037414)
- **Model type:** In vitro; iPSC-derived human spinal cord organoids (hSCOs)
- Two models: (1) primarily spinal motor neurons; (2) multiple neuronal lineages including motor neurons, interneurons, and glial cells
- Infected productively by contemporary EV-D68 B3 clade strains
- Viral antigen colocalizes with neurons
- Produce extracellular virus for 2+ weeks without appreciable cytopathic effect
- **Advantage:** Human-specific receptor expression; models cellular heterogeneity of spinal cord
- **Limitation:** Lacks immune cells; cannot model immune-mediated damage

### Applications
- **Drug evaluation:** Mouse models used to test capsid inhibitors, 2C inhibitors, hIVIG, fluoxetine, dexamethasone (PMID: 28968718, PMID: 41667472, PMID: 40593720)
- **Vaccine evaluation:** Maternal immunization and passive transfer studies (PMID: 29385753, PMID: 41210583)
- **Neurovirulence determinant mapping:** Chimeric virus studies to identify VP1/VP3 mutations (PMID: 38869283, PMID: 32784424)
- **Pathogenesis studies:** RNA-seq, flow cytometry, histopathology (PMID: 41305500)

### Model Resources
- Infectious cDNA clones for B3 clade EV-D68 strains available for reverse genetics studies (PMID: 42037414)
- BEI Resources repository for reference EV-D68 strains
- iPSC lines for spinal cord organoid generation

---

## Summary

Acute flaccid myelitis (AFM) is a rare, devastating neurologic condition primarily affecting children, characterized by acute-onset flaccid paralysis with spinal cord gray matter involvement on MRI. The disease is strongly associated with Enterovirus D68 (EV-D68) infection, with biennial outbreak patterns observed in the United States from 2014-2018 (disrupted by COVID-19 pandemic NPIs and confirmed through wastewater surveillance showing September peak seasonality).

**Viral entry and neurotropism:** EV-D68 neurotropism is mediated through multiple receptor interactions (sialic acid, ICAM-5, MFSD6), with the VP1 capsid protein as the primary determinant of neurovirulence. The virus hijacks STING for formation of specialized lipid replication organelles and exploits host immunometabolism.

**Immune evasion and host defense:** The virus employs multi-layered immune evasion: VP3-MAVS disruption, 3C-STAT1 cleavage (shared with poliovirus), USP5 deubiquitinase exploitation, and 3C-mediated RIG-I/TRIM25 degradation to suppress type I IFN signaling. Host defense mechanisms include the novel Piezo1-mediated mechano-antiviral response system (MARS) that restricts viral entry through membrane remodeling, and the ARRDC3-YAP pathway. CSF biomarkers IP-10 and IL-6 are elevated in AFM, reflecting intrathecal neuroinflammation.

**Pathogenesis:** Both direct viral cytopathology of anterior horn motor neurons and immune-mediated secondary injury (mitochondrial dysfunction via MFN2 cleavage, oxidative stress, CD8+ T cell infiltration) contribute to motor neuron destruction.

**Critical unresolved question:** EV-D68 respiratory outbreaks in 2022 and 2024 were NOT accompanied by AFM surges despite the prior biennial correlation (2014-2018). Global seroprevalence data show ~100% seropositivity by age 20, suggesting near-universal exposure. Possible explanations for the AFM-EV-D68 dissociation include viral genomic evolution (novel B3-derived lineages, A2/D reemergence), altered population immunity post-pandemic, and mutations in key neurovirulence determinants.

**Management and outcomes:** No approved treatments or vaccines exist; management relies on supportive care, empirical immunotherapy (IVIG, plasmapheresis), and comprehensive surgical reconstruction (nerve, tendon, and free muscle transfers) for persistent weakness. Long-term follow-up shows functional independence improves over years (Barthel index P<0.001), but motor deficits persist in the majority, with respiratory failure at presentation predicting worse outcomes. The prognosis remains poor, with <10% achieving full recovery. Active development of VP1 capsid inhibitors, 2C helicase inhibitors, Piezo1 agonists, self-amplifying RNA vaccines, and mRNA VLP vaccines offers hope for future therapeutic and preventive options.

---

## Limitations and Future Directions

### Limitations of Current Knowledge
1. **Diagnostic challenge:** EV-D68 is detected in CSF in <2% of confirmed AFM cases; the low detection rate has complicated efforts to definitively establish causation in individual patients. Evaluation of diagnostic criteria shows significant misclassification between AFM, transverse myelitis, and GBS at initial presentation (PMID: 36996587).
2. **No randomized controlled trials:** All treatment evidence is from case series, retrospective cohorts, or animal models. No RCT data exist for any AFM intervention.
3. **Host susceptibility unknown:** No GWAS or HLA association studies have been performed for AFM susceptibility. Why only a tiny fraction of EV-D68-infected children develop AFM remains unexplained.
4. **Limited neuropathology:** Human autopsy/biopsy data from AFM spinal cords are extremely rare, limiting direct understanding of human neuropathology.
5. **Model limitations:** Neonatal mouse models require immature animals; adult mice are resistant. Human spinal cord organoids lack immune cells. Neither model fully recapitulates pediatric AFM.

### Key Unresolved Questions
1. **Why did 2022/2024 EV-D68 outbreaks NOT cause AFM surges?** Is this due to viral evolution, population immunity shifts, or surveillance gaps?
2. **What determines individual susceptibility?** Among millions of children exposed to EV-D68, why do only ~100-200 develop AFM per biennial cycle?
3. **What is the optimal treatment window?** Can early antiviral therapy (within hours of weakness onset) prevent motor neuron loss?
4. **Will AFM outbreaks return?** The biennial pattern was disrupted; will future EV-D68 strains re-acquire neurovirulence?

### Promising Future Directions
1. **Antiviral drug development:** VP1 capsid inhibitors and 2C helicase inhibitors show strong preclinical efficacy; clinical trials needed
2. **Vaccine development:** Self-amplifying RNA and mRNA VLP platforms have shown efficacy in mice and nonhuman primates; multivalent formulations addressing antigenic diversity across clades are being designed (PMID: 39110777)
3. **Biomarker discovery:** CSF IP-10/IL-6 (PMID: 32836175) and neurofilament light chain need validation in larger cohorts
4. **Host genetics studies:** GWAS and HLA typing of AFM cohorts could identify susceptibility factors
5. **Piezo1 agonist therapy:** MARS pathway modulation as a novel non-immunological antiviral strategy (PMID: 41650963)
6. **Wastewater surveillance:** Integration of EV-D68 wastewater monitoring with clinical surveillance for early outbreak detection (PMID: 41853773)

---

## Key Evidence Citations

| PMID | Key Contribution |
|------|-----------------|
| 32143233 | Comprehensive clinical review of AFM |
| 38300829 | CDC surveillance 2018-2022 |
| 40444374 | European AFM epidemiology |
| 28231269 | Mouse model fulfilling Koch's postulates |
| 38869283 | VP1 as neurovirulence determinant |
| 41467840 | Receptor biology (ICAM-5, MFSD6) |
| 42018625 | Mitofusin 2 cleavage mechanism |
| 41305500 | Spinal cord RNA-seq pathogenesis |
| 37535397 | Human spinal cord organoid model |
| 28968718 | Preclinical therapeutic evaluation |
| 34747551 | AFM vs GBS differentiation |
| 30985511 | Population-based incidence and risk factors |
| 41667472 | VP1 capsid inhibitor development |
| 41210583 | mRNA VLP vaccine |
| 37981447 | Nerve transfer surgery outcomes |
| 41251130 | Plasmapheresis in pediatric AFM |
| 34735423 | CDC surveillance 2018-2020 |
| 41868141 | EV-D68 virology and therapeutic review |
| 41600837 | EV-D68 genomic virulence determinants |
| 30985511 | Risk factors: male sex, asthma, Asian ancestry |
| 33388543 | 3-year longitudinal motor outcomes (Japan) |
| 28615421 | 1-year outcomes including psychosocial impact (Colorado) |
| 39657203 | Long-term respiratory outcomes (4.7-year follow-up) |
| 32192819 | Texas cohort treatment and functional outcomes |
| 40042308 | VP3-MAVS immune evasion mechanism |
| 38240591 | 3C protease cleaves STAT1 for IFN evasion |
| 41352537 | USP5 deubiquitinase in enterovirus immune evasion |
| 32492201 | EV-D68 seroprevalence in Beijing |
| 32836175 | CSF cytokine biomarkers (IP-10, IL-6) in AFM |
| 41650963 | Piezo1/MARS mechano-antiviral defense |
| 39459875 | STING hijacking for replication organelles |
| 40701343 | ARRDC3-YAP antiviral pathway |
| 34170466 | TRIM25 restoration of RIG-I against EV-D68 |
| 39332429 | Global age-stratified EV-D68 seroprevalence review |
| 41853773 | US wastewater EV-D68 longitudinal surveillance |
| 36996587 | Evaluation of AFM diagnostic criteria (Netherlands) |
| 39110777 | Self-amplifying RNA vaccine (mouse + NHP) |

---

## Appendix: Validated Ontology Terms for Knowledge Base Population

### Disease Ontology
| Ontology | ID | Label |
|----------|------|-------|
| MONDO | MONDO:0100115 | acute flaccid myelitis |
| MONDO | MONDO:0005747 | enterovirus infectious disease |
| ICD-10 | G04.82 | Acute flaccid myelitis |
| MeSH | D000080524 | Myelitis, Acute Flaccid |

### Phenotype (HPO) Terms
| HPO ID | Label | Frequency in AFM |
|--------|-------|-----------------|
| HP:0012486 | Myelitis | 100% (defining) |
| HP:0003690 | Limb muscle weakness | 100% (defining) |
| HP:0002398 | Degeneration of anterior horn cells | ~100% (pathological basis) |
| HP:0006802 | Abnormal anterior horn cell morphology | ~100% |
| HP:0001252 | Hypotonia | ~100% |
| HP:0001284 | Areflexia | ~90% (affected limbs) |
| HP:0012229 | CSF pleocytosis | 50-73% |
| HP:0002878 | Respiratory failure | ~21-30% |
| HP:0006824 | Cranial nerve paralysis | ~20-30% |
| HP:0000016 | Urinary retention | Variable |
| HP:0003326 | Myalgia | ~70% (prodromal/concurrent) |
| HP:0003202 | Skeletal muscle atrophy | Common (chronic phase) |
| HP:0002015 | Dysphagia | Variable (bulbar involvement) |

### Anatomical (UBERON) Terms
| UBERON ID | Label |
|-----------|-------|
| UBERON:0002257 | ventral horn of spinal cord |
| UBERON:0014621 | cervical spinal cord ventral horn |
| UBERON:0002315 | gray matter of spinal cord |
| UBERON:0002726 | cervical spinal cord |
| UBERON:0001884 | phrenic nerve |
| UBERON:0002240 | spinal cord |
| UBERON:0001134 | skeletal muscle tissue |

### Cell Type (CL) Terms
| CL ID | Label |
|-------|-------|
| CL:0011001 | spinal cord motor neuron |
| CL:0000100 | motor neuron |
| CL:0002368 | respiratory tract epithelial cell |

### Gene Ontology (GO) Biological Process Terms
| GO ID | Label |
|-------|-------|
| GO:0046718 | symbiont entry into host cell |
| GO:0045087 | innate immune response |
| GO:0060337 | type I interferon-mediated signaling pathway |
| GO:0060339 | negative regulation of type I interferon-mediated signaling pathway |
| GO:0000266 | mitochondrial fission |
| GO:0006914 | autophagy |
| GO:0000422 | autophagy of mitochondrion |
| GO:0006915 | apoptotic process |
| GO:0006954 | inflammatory response |
| GO:0006979 | response to oxidative stress |
| GO:0071260 | cellular response to mechanical stimulus |
| GO:0019058 | viral life cycle |

### Chemical Entity (CHEBI) Terms
| CHEBI ID | Label | Role in AFM |
|----------|-------|-------------|
| CHEBI:26667 | sialic acid | EV-D68 attachment factor |
| CHEBI:5118 | fluoxetine | Investigated antiviral (no efficacy in mouse model) |
| CHEBI:41879 | dexamethasone | Corticosteroid (worsened outcomes in mouse model) |
| CHEBI:24579 | immunoglobulin G | IVIG therapy (empirical treatment) |

### Treatment (MAXO) Terms
| MAXO ID | Label |
|---------|-------|
| MAXO:0001298 | intravenous immunoglobulin therapy |
| MAXO:0000609 | corticosteroid therapy |
| MAXO:0001077 | plasmapheresis |
| MAXO:0000014 | surgical procedure (nerve transfer) |
| MAXO:0000502 | physical therapy |
| MAXO:0001001 | respiratory support |

### Host Gene Annotations
| Gene Symbol | HGNC ID | Role in AFM |
|-------------|---------|-------------|
| *ICAM5* | HGNC:5348 | Neuron-specific EV-D68 receptor |
| *MFSD6* | HGNC:24711 | Essential EV-D68 entry receptor |
| *MFN2* | HGNC:16877 | Cleaved by 3C protease; mitochondrial fission |
| *MAVS* | HGNC:29233 | Targeted by VP3 for immune evasion |
| *STAT1* | HGNC:11362 | Cleaved by 3C protease; IFN signaling |
| *TRAF3* | HGNC:12033 | Cleaved by 2A protease; NF-kB pathway |
| *USP5* | HGNC:12628 | Exploited by EV-D68 to suppress IFN |
| *IRF3* | HGNC:6118 | De-ubiquitinated via USP5; IFN induction |
| *IRF7* | HGNC:6122 | Targeted by VP3 for IFN suppression |
| *PIEZO1* | HGNC:13680 | Mechano-antiviral response (MARS); membrane remodeling |
| *STING1* (TMEM173) | HGNC:27962 | Hijacked for replication organelle formation |
| *ARRDC3* | HGNC:28633 | Host antiviral factor; degrades YAP via lysosome |
| *TRIM25* | HGNC:10544 | E3 ubiquitin ligase; restores RIG-I expression |
| *YAP1* | HGNC:16262 | Facilitates enterovirus replication; suppresses IFN |
