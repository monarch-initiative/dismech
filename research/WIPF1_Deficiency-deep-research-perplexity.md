---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-11-06T13:05:48.025650'
end_time: '2026-11-06T13:11:43.114358'
duration_seconds: 355.09
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: WIPF1 Deficiency
  mondo_id: MONDO:0013779
  category: Mendelian
  causal_genes: WIPF1
  omim_id: OMIM:277970, OMIM:614493
  synonyms: Wiskott-Aldrich syndrome type 2; WIPF1 Wiskott-Aldrich syndrome; Wiskott-Aldrich
    syndrome caused by mutation in WIPF1
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 20
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.5.1
term_validation:
  total_terms: 70
  verified: 68
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 29
  labels_matching: 12
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0000974
    reported_labels:
    - Eczematoid dermatitis
    ontology_label: Hyperextensible skin
  - term_id: HP:0002720
    reported_labels:
    - Lymphopenia
    ontology_label: Decreased circulating IgA concentration
  - term_id: HP:0002723
    reported_labels:
    - Abnormality of T-cell subsets
    ontology_label: Absence of bactericidal oxidative respiratory burst in phagocytes
  - term_id: HP:0002721
    reported_labels:
    - Abnormal immunologic reaction
    ontology_label: Immunodeficiency
  - term_id: HP:0003236
    reported_labels:
    - Decreased proportion of CD8-positive T cells
    ontology_label: Elevated circulating creatine kinase activity
  - term_id: HP:0002758
    reported_labels:
    - Abnormal T cell proliferation
    ontology_label: Osteoarthritis
  - term_id: HP:0002725
    reported_labels:
    - Abnormal NK cell function
    ontology_label: Systemic lupus erythematosus
  - term_id: HP:0002722
    reported_labels:
    - Abnormal immunoglobulin level
    ontology_label: Recurrent abscess formation
  - term_id: HP:0002019
    reported_labels:
    - Inflammatory bowel disease
    ontology_label: Constipation
  - term_id: UBERON:0002107
    reported_labels:
    - intestinal tract
    ontology_label: liver
  labels_variant: 7
  unresolvable_prefixes:
  - Orphanet
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** WIPF1 Deficiency
- **MONDO ID:** MONDO:0013779 (if available)
- **Causal gene(s):** WIPF1
- **OMIM:** OMIM:277970, OMIM:614493
- **Synonyms:** Wiskott-Aldrich syndrome type 2; WIPF1 Wiskott-Aldrich syndrome; Wiskott-Aldrich syndrome caused by mutation in WIPF1
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **WIPF1 Deficiency** covering all of the
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

# WIPF1 Deficiency (Wiskott–Aldrich Syndrome 2)

WIPF1 deficiency, also known as **Wiskott–Aldrich syndrome 2 (WAS2)**, is a rare autosomal recessive primary immunodeficiency caused by biallelic pathogenic variants in the **WIPF1** gene, which encodes the WAS/WASL-interacting protein (WIP).[1][10][16] This disorder produces a clinical picture that closely resembles classic Wiskott–Aldrich syndrome (WAS), including early-onset recurrent infections, eczema, and thrombocytopenia, but with a distinct genetic basis and inheritance pattern.[1][11][12][16] At the molecular level, WIPF1 loss-of-function leads to loss or marked reduction of WIP protein, destabilization and degradation of WASP despite normal WAS mRNA, disruption of actin cytoskeleton dynamics, and consequent combined immunodeficiency with impaired T-cell proliferation and migration, defective natural killer (NK) cell cytotoxicity, and abnormal platelet function.[10][11][15][16] Fewer than ten patients have been reported worldwide, but based on functional, genetic, and animal model data, ClinGen has classified the WIPF1–WAS2 association as **definitive**, with loss of function as the disease mechanism.[10] Allogeneic hematopoietic stem cell transplantation (HSCT) is currently the only curative treatment and has restored immune competence and platelet counts in reported patients, although outcomes vary with disease severity at the time of transplant and associated complications such as severe cytomegalovirus (CMV) infection.[11][12][16]  

## 1. Disease Information

WIPF1 deficiency is a Mendelian primary immunodeficiency characterized by **combined immunodeficiency with thrombocytopenia and eczema**, clinically overlapping with classical Wiskott–Aldrich syndrome but arising from autosomal recessive mutations in WIPF1 rather than X-linked mutations in WAS.[1][11][12][16][18] The disorder has been formalized under the name **Wiskott–Aldrich syndrome 2 (WAS2)** and is classified as an autosomal recessive immunologic disease with onset of recurrent infections in infancy, thrombocytopenia with normal platelet volume, eczema, decreased CD8\(^+\) T cells, aberrant T- and NK-cell function, and impaired T-cell migration, attributed to defective F-actin polymerization.[1][16][18] The key causal gene is **WIPF1** (HGNC:12736), located on chromosome 2q31.1, encoding the WAS/WASL-interacting protein (WIP), which plays a central role in actin cytoskeleton organization and in stabilizing WASP.[1][2][3][4][16]

In terms of key identifiers, WIPF1 deficiency/WAS2 is registered in multiple rare disease resources. OMIM lists **Wiskott–Aldrich syndrome 2** under entry **OMIM 614493**, mapped to WIPF1 at 2q31.1, with autosomal recessive inheritance and phenotype mapping key 3, indicating a known molecular basis.[16] MedGen designates the condition with Concept ID **C3281001**, under the preferred name **Wiskott-Aldrich syndrome 2 (WAS2)**, with synonyms including **WIPF1 deficiency** and **WIP deficiency**.[1] The Monarch Initiative/MONDO ontology assigns MONDO:0013779 to Wiskott–Aldrich syndrome 2.[1][10] Orphanet recognizes the disorder (Orphanet:906), also linking it to WIPF1.[1][10] Genetic testing registries such as the NCBI Genetic Testing Registry (GTR) list specific tests for “Wiskott-Aldrich syndrome 2, 614493; WAS2 (WIPF1 gene)” that analyze all coding exons of WIPF1.[18]  

The naming of WIPF1 deficiency has evolved to distinguish it from classic X-linked WAS. OMIM and related resources consistently use **Wiskott–Aldrich syndrome 2**, while many clinical reports refer to **WIP deficiency**, **WIPF1-related combined immunodeficiency with thrombocytopenia**, or **autosomal recessive Wiskott–Aldrich–like syndrome**.[10][11][12][16][19] Wikipedia and other secondary sources discuss WIPF1 as the gene encoding WIP and note that patients lacking WIPF1 exhibit WAS-like symptoms due to WASP depletion.[3][4] For clarity, the disease entry in this report is keyed to the combination of MONDO:0013779 and WIPF1, which unambiguously specifies the autosomal recessive WAS-like immunodeficiency caused by WIPF1 mutations.[1][10]

The information summarized here is primarily derived from **aggregated disease-level resources** (OMIM, MedGen, ClinGen, Orphanet, GTR) and **primary case reports and small case series** rather than large electronic health record–based studies.[1][10][11][12][16][18][19] The seminal case was reported in 2012 by Lanzi et al., who described “a novel primary human immunodeficiency due to deficiency in the WASP-interacting protein WIP” caused by a homozygous stop codon mutation in WIPF1.[11][13][15] Subsequent patients have been reported in a large Saudi kindred and a multinational series summarized in 2018, as well as an individual with combined ICOS and WIPF1 mutations.[12][16][19] Given the extreme rarity of WIPF1 deficiency, virtually all clinical and mechanistic knowledge stems from these few pedigrees and supporting experimental studies.

## 2. Etiology

WIPF1 deficiency is fundamentally a **genetic disease** caused by biallelic loss-of-function variants in the WIPF1 gene. There is no evidence that environmental exposures, infections, or lifestyle factors can cause this syndrome in the absence of such mutations, although these factors may modify the clinical course. The etiologic framework therefore centers on the **molecular function of WIPF1 and its interaction with WASP**, and on how its disruption gives rise to a combined immunodeficiency with thrombocytopenia.[3][4][10][11][15][16]  

WIPF1 encodes the WAS/WASL-interacting protein (WIP), a cytosolic adaptor protein that binds to the Wiskott–Aldrich syndrome protein (WASP, encoded by WAS) and the ubiquitously expressed WASP ortholog N-WASP (WASL).[3][4][16] WIP plays a critical role in actin cytoskeleton organization: overexpression of WIP in mammalian cells increases actin polymerization, while WIP deficiency impairs actin-dependent processes.[3][4] A major function of WIPF1 is to **stabilize WASP and prevent its degradation**, and it has been shown that WASP is almost totally complexed with WIPF1 in T cells.[10][16] In the absence of WIP, WASP protein expression is markedly reduced or absent despite normal WAS mRNA levels, demonstrating that WIP is a post-translational chaperone for WASP.[10][11][15][16]  

ClinGen’s SCID/CID Gene Curation Expert Panel concluded in 2023 that the **mechanism of pathogenicity is loss of function** of WIPF1.[10] They reviewed three nonsense variants in WIPF1 reported in three probands across three publications, along with functional studies and animal models, and found strong evidence that WIPF1 loss-of-function causes autosomal recessive WIPF1-related combined immunodeficiency with thrombocytopenia.[10] In the index case described by Lanzi et al., sequencing revealed a homozygous c.1301C>G mutation in exon 6 of WIPF1, resulting in a p.Ser434Ter (S434X) truncating variant located just upstream of the WASP-binding domain of WIP.[11][15][16] WIP protein was undetectable in patient cells, and WASP protein was also absent, despite normal WAS mRNA; reintroduction of WIP corrected WASP expression, providing direct functional evidence that the stop codon mutation caused WIP deficiency and WASP instability.[11][15]

Additional nonsense variants have been reported. In a multigenerational consanguineous Saudi Arabian kindred, Al-Mousa et al. identified a homozygous Q237X nonsense mutation in WIPF1 (c.709C>T, p.Gln237Ter), which segregated with disease in four affected patients, though detailed functional studies were not reported.[16] In a 2018 review of WIP deficiency cases, a novel stop-gain mutation c.373C>T (p.R125X) was reported, associated with very early-onset severe combined immunodeficiency and life-threatening viral infections, including CMV.[12] ClinVar now catalogues several additional WIPF1 loss-of-function variants classified as pathogenic or likely pathogenic, including c.284del (p.Gly95Alafs*17), a frameshift leading to a premature stop codon, and c.587C>G (p.Ser196Ter), a nonsense variant; these variants are predicted to result in absent or truncated WIP protein and are consistent with loss of function as the disease mechanism.[2][7]  

Other variants in WIPF1 have been submitted to ClinVar with classifications such as **uncertain significance** or **likely benign**. For example, c.374G>A (p.Arg125Gln) is a rare missense variant present in gnomAD (frequency approximately 0.004%), with no reported association with disease, leading to its classification as a **variant of uncertain significance (VUS)**.[6] Synonymous variants such as c.177G>A (p.Leu59=) and c.843G>C (p.Ala281=) have been classified as **likely benign**, reflecting their lack of predicted effect on protein structure and the absence of disease association.[8][9] These data highlight that not all WIPF1 variants are pathogenic and that **truncating or clearly disruptive variants in a biallelic state** appear to be the hallmark of WIPF1 deficiency.[2][7][10]

### Genetic Risk Factors

The primary genetic risk factor for WIPF1 deficiency is **biallelic (homozygous or compound-heterozygous) loss-of-function mutations in WIPF1**.[10][11][12][16] Because the disease is autosomal recessive, heterozygous carriers are typically asymptomatic; in the Moroccan index family, both parents were heterozygous for the S434X mutation and had approximately half-normal levels of WIPF1 protein but no clinical disease.[16] Consanguinity has been a prominent feature in reported cases. The first patient described by Lanzi et al. was a female offspring of consanguineous parents, while the Saudi kindred reported by Al-Mousa et al. involved a large consanguineous family.[11][15][16] Similarly, patients summarized in the 2018 Frontiers in Immunology review were often from consanguineous marriages.[12] These observations underscore **consanguinity as an important risk factor** for WIPF1 deficiency, consistent with its autosomal recessive inheritance and extreme rarity in outbred populations.[11][12][16]

Beyond WIPF1 itself, there is emerging evidence that **additional genetic defects can coexist and shape phenotype**. A Turkish report described a patient with coexisting **ICOS deficiency** and **WIPF1 mutation (c.310T>C)**, both inherited in an autosomal recessive manner, leading to a complex phenotype combining features of combined immunodeficiency, recurrent infections, eczema, arthritis, and severe lung infections.[19] The authors emphasized that ICOS deficiency is classified as a combined immunodeficiency and that WIPF1 mutation causes WIP deficiency, characterized by thrombocytopenia, immunodeficiency, and eczema; the coexistence of these defects likely amplified immune dysfunction.[19] This case illustrates that **modifier genes or dual primary immunodeficiencies** can influence clinical expression in individual patients, though systematic evidence for specific modifier genes in WIPF1 deficiency is not yet available.

### Environmental and Other Risk Factors

To date, **no environmental or lifestyle risk factors** are known to cause WIPF1 deficiency in the absence of pathogenic WIPF1 variants. The disorder appears entirely driven by germline genetic defects, as supported by the absence of somatic WIPF1 mutations in tumor or somatic mutation databases and the autosomal recessive familial clustering with segregation of truncating variants.[10][16] However, environmental factors, particularly infectious exposures, have a profound impact on **disease course and complications**. The 2018 review noted that all patients had an increased risk of infections, chronic diarrhea, and respiratory symptoms, with many experiencing severe or recurrent viral infections such as CMV, which could be life-threatening in the setting of severe immunodeficiency.[12] One patient in that series died from CMV-related respiratory distress syndrome shortly after HSCT, underscoring how environmental exposure to CMV interacts with underlying genetic immunodeficiency to influence outcomes.[12]  

No specific **protective environmental factors** have been documented, though standard infection prevention measures, prophylactic antimicrobials, and immunoglobulin replacement therapy can reduce infection burden, analogous to other primary immunodeficiencies.[12] There is also no evidence of **protective WIPF1 alleles** or polymorphisms that reduce disease risk; population variants in WIPF1 catalogued in gnomAD and ClinVar are generally rare, and only truncating variants in the homozygous state have been associated with disease.[6][8][9][10]

### Gene–Environment Interactions

Because WIPF1 deficiency is rare and only a handful of cases have been reported, **gene–environment interactions** have not been systematically studied. Nonetheless, mechanistic logic and case descriptions suggest several interaction patterns. First, the loss of WIP–WASP complex function leads to impaired T-cell and NK-cell cytoskeletal dynamics, which in turn impairs responses to infectious agents; this means that **exposure to common viral and bacterial pathogens** can produce unusually severe disease manifestations, such as life-threatening CMV infection or recurrent severe pneumonia.[11][12][15][19] Second, vaccinations and infections that stimulate the immune system may unmask or exacerbate immune dysregulation, though formal data in WIPF1 deficiency are lacking; by analogy with WAS, immune activation in the context of defective actin remodeling can contribute to eczema and inflammatory complications.[12][16] Third, HSCT, antiviral therapies, and immune reconstitution strategies provide examples of **therapeutic gene–environment modulation**, where environmental interventions (donor cells, antiviral drugs, donor lymphocyte infusions) interact with the residual host immune system to reshape disease trajectory.[11][12][16]

At present, databases such as CTD, GWAS Catalog, or PheGenI do not report gene–environment association data specific to WIPF1 deficiency, reflecting the rarity and the absence of population-based studies. Thus, gene–environment interactions in this disorder are best conceptualized qualitatively: the **necessary and sufficient cause** is biallelic WIPF1 loss-of-function, while environmental factors predominantly modulate **disease severity, infection burden, and treatment outcomes** rather than primary disease risk.

## 3. Phenotypes

Clinically, WIPF1 deficiency presents as an **early-onset combined immunodeficiency with thrombocytopenia and eczema**, with features that overlap but do not entirely recapitulate classical X-linked Wiskott–Aldrich syndrome.[1][11][12][16][17][18] Because of the small number of reported patients, the phenotypic spectrum is still being defined, but existing reports allow reconstruction of a core phenotype and its variability. The most comprehensive phenotype overview currently available comes from OMIM, MedGen, ClinGen, and the 2018 Frontiers in Immunology synopsis of six WIP-deficient patients from three pedigrees.[1][10][12][16][17][18]

### Core Clinical Phenotypes

The core triad of **recurrent infections, thrombocytopenia, and eczema** is a defining feature of WIPF1 deficiency, paralleling the classic WAS triad.[1][11][12][16][17][18] MedGen and OMIM describe WAS2 as an autosomal recessive disorder with recurrent infections beginning in infancy, thrombocytopenia with normal platelet volume, and eczema.[1][16][18] The Mendelian rare disease aggregation site Mendelian lists WIPF1-related WAS2 with very high frequencies for several phenotypes: eczema, recurrent infections, and thrombocytopenia are each rated as “very common” (seen in 80–100% of cases), along with decreased CD8-positive T cells and defective T-cell proliferation.[17] These frequencies, while approximate, reflect that these features were present in virtually all described patients.[11][12][16][17]

In the index patient reported by Lanzi et al., a Moroccan girl, symptoms began in early infancy and included recurrent infections, eczema, thrombocytopenia, and severe immunological abnormalities.[11][15][16] The authors summarized:

> “A female offspring of consanguineous parents, showed features of Wiskott-Aldrich syndrome (WAS), including recurrent infections, eczema, thrombocytopenia, defective T cell proliferation and chemotaxis, and impaired natural killer cell function.”[11][13][15]  

Laboratory evaluation revealed T-cell lymphopenia, particularly affecting CD8\(^+\) T cells, reduced T-cell proliferation in response to immobilized anti-CD3, defective T-cell chemotaxis, increased NK-cell numbers but decreased NK-cell function, and thrombocytopenia with normal platelet volume.[11][15][16] These findings collectively define the core immunologic phenotype of WIPF1 deficiency: **combined immunodeficiency with defective T-cell and NK-cell function, quantitative T-cell deficits, and platelet abnormalities**.[1][10][11][12][16][18]

The 2018 synopsis of six WIP-deficient patients from three pedigrees confirmed this core phenotype but also highlighted variability. All patients exhibited early-onset severe infections (respiratory infections, chronic diarrhea, invasive viral infections, including CMV), failure to thrive, and laboratory evidence of combined immunodeficiency, yet the presence and severity of thrombocytopenia and eczema varied.[12] In that series, platelet phenotypes ranged from **normal-sized platelets with moderate thrombocytopenia** to **microthrombocytopenia with severe thrombocytopenia**, suggesting that WIPF1 deficiency can produce variable platelet size and count, unlike classic WAS where microthrombocytopenia is nearly universal.[12][16] Skin manifestations also varied, with some patients having eczematous lesions, peeling skin, or eczema-like dermatitis, while others had milder or less specific skin findings.[12][19]  

Suggested HPO terms for these core phenotypes include: HP:0002719 (*Recurrent infections*), HP:0000964 (*Eczema*), HP:0001873 (*Thrombocytopenia*), HP:0000974 (*Eczematoid dermatitis*), and HP:0001876 (*Abnormal platelet count*). For the immunologic abnormalities, appropriate HPO terms include HP:0005403 (*Abnormal T cell morphology*), HP:0002720 (*Lymphopenia*), HP:0002723 (*Abnormality of T-cell subsets*), HP:0002721 (*Abnormal immunologic reaction*), and HP:0003236 (*Decreased proportion of CD8-positive T cells*)—the latter explicitly mentioned in MedGen and OMIM for WAS2.[1][16][18]

### Age of Onset, Severity, and Course of Phenotypes

WIPF1 deficiency **consistently presents in early infancy**, often within the first months of life.[1][11][12][16][18] In Lanzi’s Moroccan index case, the girl presented in early infancy with recurrent infections and thrombocytopenia; she underwent unrelated cord blood transplantation at 4.5 months.[11][15][16] Another Moroccan infant was diagnosed at 11 days of age due to a family history and laboratory findings.[16] In the 2018 review, all patients displayed extremely early onset of symptoms of primary immunodeficiency, with some presenting in the neonatal period.[12] Thus, the appropriate HPO term for onset is HP:0003593 (*Neonatal onset*) or HP:0003623 (*Infantile onset*), depending on precise timing.

Symptom severity is typically **severe**, especially regarding infectious complications. The 2018 series noted that WIP-deficient patients often had “very early onset of severe, life-threatening immunodeficiency,” and one patient died of CMV-related respiratory distress shortly after HSCT.[12] Infections include recurrent pneumonia, chronic diarrhea, sepsis, and invasive viral infections such as CMV; one report detailed a patient with frequent lung infections “at least every month” and 20 episodes of otitis per year.[19] These infections have major impacts on quality of life, causing prolonged hospitalizations, failure to thrive, and high morbidity.[12][19]  

Thrombocytopenia can range from moderate to severe; some patients have chronic severe microthrombocytopenia requiring transfusions or leading to bleeding complications, while others have milder thrombocytopenia without major bleeding.[12][16][19] In the Turkish patient with coexisting ICOS and WIPF1 mutations, severe skin peeling and bleeding were noted at 6 months of age, and thrombocytopenia was part of the syndrome.[19] Eczema and skin lesions contribute to discomfort, pruritus, risk of skin infections, and psychosocial burden, particularly in older children, though detailed quality-of-life surveys have not been performed in this rare population.[12][19]  

Laboratory abnormalities, while less subjectively experienced, are crucial for diagnosis and reflect the underlying pathophysiology. Reduced naïve T cells, particularly CD8\(^+\) T cells, reduced T-cell proliferation in vitro, increased proportion of TCRγδ-positive T cells, and impaired NK cytotoxicity have been repeatedly documented.[11][12][16][18] For example, in one patient reported by the 2018 series, immunologic analyses at 4–5 months showed reduced naïve T cells, reduced T-cell proliferation, and increased TCRγδ-positive T cells, indicative of combined immunodeficiency.[12] Appropriate HPO terms include HP:0002720 (*Lymphopenia*), HP:0005403 (*Abnormal T cell morphology*), HP:0002758 (*Abnormal T cell proliferation*), HP:0002725 (*Abnormal NK cell function*), and HP:0002722 (*Abnormal immunoglobulin level*), as variable immunoglobulin levels (particularly elevated IgE) have been reported.[1][16][18]

### Additional and Variable Phenotypes

A number of **additional phenotypes** have been reported in individual WIPF1-deficient patients, though their frequency and specificity remain uncertain due to limited case numbers. Autoimmunity appears less prominent than in classic WAS, but some patients have had inflammatory manifestations such as pneumonitis, arthritis, or colitis.[1][10][12][16][19] For example, the Moroccan index patient developed inflammatory complications including pneumonitis; WIPF1 knockout mice also develop inflammatory diseases such as ulcerative colitis and interstitial pneumonitis, suggesting that immune dysregulation and inflammatory responses are part of the pathophysiologic spectrum.[10][16] The Turkish patient with combined ICOS and WIPF1 mutations experienced arthritis attacks in the arms and legs at age 6, reflecting autoimmune or inflammatory joint disease in the context of combined immunodeficiency.[19] Corresponding HPO terms would include HP:0001369 (*Arthritis*), HP:0002090 (*Pneumonitis*), and HP:0002019 (*Inflammatory bowel disease*), though their association with pure WIPF1 deficiency needs further confirmation.

Failure to thrive, growth retardation, and developmental complications, including seizures, have been reported. The Turkish patient had convulsions starting at one month of age and required antiepileptic drugs, although it is unclear whether seizures were directly attributable to WIPF1 deficiency or secondary to infections, metabolic disturbances, or coexisting genetic defects (e.g., ICOS deficiency).[19] Failure to thrive was noted in several patients, largely driven by chronic infections and malabsorption from chronic diarrhea.[12][19] HPO terms such as HP:0001510 (*Growth delay*), HP:0001508 (*Failure to thrive in infancy*), and HP:0001250 (*Seizures*) may therefore be relevant in some cases.

In summary, the **phenotype spectrum of WIPF1 deficiency** spans early-onset severe combined immunodeficiency with recurrent infections and failure to thrive; thrombocytopenia with normal or small platelets; eczema and other skin manifestations; variable inflammatory and autoimmune features; and characteristic immunologic abnormalities of T and NK cells. Symptom onset is neonatal or infantile, severity is generally high without treatment, and progression is driven by accumulating infections and inflammatory damage, though HSCT can dramatically alter the course.[1][10][11][12][16][18]

## 4. Genetic and Molecular Information

### Causal Gene and Gene Product

The causal gene for WIPF1 deficiency is **WIPF1 (WAS/WASL Interacting Protein Family Member 1)**, located at chromosome **2q31.1**.[1][2][4][16] OMIM entry 602357 describes WIPF1 as a protein-coding gene whose major function is to stabilize WASP and prevent its degradation.[16] Two transcript variants encoding the same protein have been identified, and the protein is widely referred to as **WIP** (WASP-interacting protein).[3][4] WIP contains proline-rich regions and a C-terminal WASP-binding domain (amino acids 451–485), through which it associates with WASP.[3][11][15][16]  

WIP plays a crucial role in actin cytoskeleton organization. Overexpression of WIP increases actin polymerization and redistribution in lymphoid cells, while WIP deficiency impairs actin-dependent processes.[3][4] WIP1 interacts with WASP and N-WASP (WASL) as well as adaptor proteins such as NCK1 and GRB2, contributing to recruitment and activation of WASL and to regulation of actin dynamics in processes such as phagocytic cup formation and immune response signaling in NK cells.[4][10] WIP also plays a role in vaccinia virus intracellular motility by acting as an adaptor for WASL recruitment to the virus, underscoring its broader role in actin-based motility.[4] These functions are captured by Gene Ontology (GO) terms such as **GO:0030036** (*actin cytoskeleton organization*), **GO:0030833** (*regulation of actin filament polymerization*), and **GO:0042110** (*T cell activation*), all of which are highly relevant to WIPF1 deficiency.

### Pathogenic Variants: Types and Consequences

The known pathogenic variants in WIPF1 associated with WAS2 are mainly **nonsense and frameshift variants** that introduce premature stop codons, leading to truncated proteins lacking critical domains or triggering nonsense-mediated decay.[10][11][12][16] The first such variant, reported by Lanzi et al., was c.1301C>G in exon 6, resulting in p.Ser434Ter (S434X), located immediately upstream of the WASP-binding domain.[11][15][16] This truncation eliminates the C-terminal region necessary for WASP binding, leading to absence of WIP protein expression (likely due to instability or degradation of the truncated protein) and consequent loss of WASP stability.[11][15][16]  

In the Saudi kindred, a homozygous C>T transition in exon 6 produced a p.Gln237Ter (Q237X) variant; this truncation is even more upstream, eliminating large portions of WIP, including regions required for actin regulation and WASP binding.[16] In another pedigree summarized by the 2018 review, a novel stop-gain mutation c.373C>T (p.R125X) was identified by next-generation sequencing, again producing a short truncated protein and WIP deficiency.[12] ClinVar has registered additional truncating variants: c.284del (p.Gly95Alafs*17) produces a frameshift and premature stop codon at position 111, and c.587C>G (p.Ser196Ter) introduces a stop codon at position 196; both variants are classified as **pathogenic** and expected to result in absent or severely truncated WIP.[2][7]

These truncating variants share a common functional consequence: **loss of function of WIPF1**, resulting in absent or severely reduced WIP protein. Functional studies in patient cells have demonstrated that WIP is undetectable by immunoblotting in individuals with homozygous truncating mutations, while WASP protein is also absent or markedly reduced despite normal WAS mRNA levels.[11][15][16] Reintroduction of wild-type WIP into patient T cells restores WASP expression, demonstrating that the primary defect is lack of WIP and that WASP instability is a secondary consequence.[11][15] ClinGen summarized these findings, stating that “one normal function of WIP is to bind to WASP, stabilizing the protein and preventing its degradation… In the absence of WIP, WASP expression is reduced or absent despite normal levels of mRNA. Introduction of wild type WIPF1 corrects this defect.”[10]  

The WIPF1–WAS2 relationship has therefore been classified as **definitively associated** with autosomal recessive WIPF1-related combined immunodeficiency with thrombocytopenia, with **loss-of-function (LOF)** as the mechanism of pathogenicity.[10] This is supported by protein interaction data, functional and rescue assays, and WIPF1 knockout mice that recapitulate the patient phenotype.[10] Suggested HGNC and UniProt annotations include: HGNC:12736 (*WIPF1*), UniProt entry for WAS/WASL-interacting protein, and GO:0007264 (*small GTPase mediated signal transduction*), reflecting its role in actin signaling.

### Variant Classifications and Population Frequencies

ClinVar summaries show a range of variant classifications in WIPF1. Pathogenic and likely pathogenic variants include truncating changes such as c.284del (p.Gly95Alafs*17) and c.587C>G (p.Ser196Ter), as well as the previously reported S434X, Q237X, and R125X variants identified in case reports.[2][7][10][11][12][16] Benign or likely benign variants include synonymous changes such as c.177G>A (p.Leu59=) and c.843G>C (p.Ala281=), which do not alter the amino acid sequence and have no evidence of disease association.[8][9] Variants of uncertain significance (VUS) such as c.374G>A (p.Arg125Gln) are typically rare missense changes observed in population databases (e.g., rs747543329 in gnomAD) without reported cases of WIPF1-related disease.[6]  

Population allele frequencies for pathogenic WIPF1 variants are extremely low, consistent with the rarity of WAS2. For example, pathogenic truncating variants are generally absent from gnomAD or observed only in heterozygous state at very low frequencies, reflecting strong purifying selection. VUS and likely benign variants may have slightly higher frequencies but remain rare, underscoring that WIPF1 deficiency is an **ultra-rare recessive disorder**, likely confined to individuals with consanguineous backgrounds or founder mutations.[6][8][9][10][16]

### Somatic vs Germline Origin

All reported WIPF1 variants causing WAS2 are **germline**, inherited in an autosomal recessive pattern. Parents are heterozygous carriers, and affected children are homozygous, consistent with consanguinity.[11][15][16] There are no reports of **somatic WIPF1 mutations** causing acquired immunodeficiency or malignancies, and databases such as COSMIC do not list WIPF1 as a recurrent somatic driver. Thus, WIPF1 deficiency is best conceptualized as a **heritable germline primary immunodeficiency** rather than a somatic or acquired disease.[10][16]

### Modifier Genes and Epigenetic Information

To date, **specific modifier genes** that alter WIPF1 deficiency severity have not been identified, largely because of the small number of reported patients and the lack of systematic genotype–phenotype correlation studies. However, the Turkish patient with coexisting ICOS and WIPF1 mutations demonstrates that **additional primary immunodeficiencies can coexist** and substantially modify clinical expression, leading to broader manifestations such as autoimmunity, enteropathy, and lymphoproliferation characteristic of ICOS deficiency.[19] Future sequencing of larger cohorts with WAS-like phenotypes may identify other genes that interact functionally with WIPF1–WASP pathways.

There is no evidence of **epigenetic alterations** (e.g., DNA methylation changes, histone modifications) that directly drive WIPF1 deficiency. Since the primary mechanism is loss of function due to truncating variants, and WIPF1 expression is abolished by nonsense mutations, epigenetic regulation is unlikely to be the primary cause. However, epigenetic mechanisms may influence downstream pathways, such as T-cell differentiation and inflammatory responses, but these have not yet been studied specifically in WIPF1-deficient patients. Epigenomic databases such as ENCODE and Roadmap Epigenomics provide general data on WIPF1 locus regulation but do not link specific epigenetic changes to this disease.

### Chromosomal Abnormalities

There are **no reports of chromosomal structural abnormalities** (e.g., deletions, duplications, translocations) involving the 2q31.1 region that cause WIPF1 deficiency. All described pathogenic variants are intragenic point mutations or small indels in WIPF1.[10][11][12][16] Chromosomal microarray or karyotyping is therefore not considered a primary diagnostic tool for WAS2, unless broader genomic evaluation is warranted for differential diagnosis.

In summary, WIPF1 deficiency is a **monogenic loss-of-function disorder** caused by truncating germline variants in WIPF1, leading to absence of WIP protein, instability of WASP, and downstream immunologic defects. The disease is autosomal recessive, ultra-rare, and definitively associated with WIPF1 by ClinGen, with no evidence of somatic forms or epigenetically driven cases.[10][11][12][16]

## 5. Environmental Information

Given its Mendelian basis, WIPF1 deficiency is fundamentally a **genetic disease**, and **no environmental factor is known to be causative** in the absence of a WIPF1 loss-of-function mutation. However, environmental exposures, particularly infectious agents, have significant effects on **disease expression, complications, and outcomes**.

### Environmental and Lifestyle Factors

There is no evidence from CTD, TOXNET, or the primary literature that environmental toxins, pollutants, radiation, or occupational exposures play any role in the pathogenesis of WIPF1 deficiency. Likewise, lifestyle factors such as smoking, diet, or physical activity do not appear to influence the risk of developing the disease, though they could conceivably affect general health and infection susceptibility in affected individuals. The rarity and early-onset nature of the disorder, often manifesting in infancy, further argue against major environmental etiologic contributions.[1][11][12][16][18]

### Infectious Agents

Infectious agents play a **central role in clinical manifestations** of WIPF1 deficiency, because the underlying combined immunodeficiency predisposes patients to severe or recurrent infections. Reported infections include recurrent bacterial respiratory infections, otitis media, chronic diarrhea with presumed enteric infections, and particularly severe viral infections such as challenge with CMV.[11][12][19] The 2018 review describes one patient with life-threatening CMV infection who required serial maternal donor lymphocyte infusions and subsequent HSCT; another patient died from CMV-related respiratory distress syndrome shortly after transplant.[12] These experiences highlight that CMV and other common viruses become **opportunistic pathogens** in the context of WIPF1 deficiency, akin to other severe combined immunodeficiencies.

There is no evidence that specific pathogens act as **primary triggers** of WIPF1 deficiency, but infections clearly accelerate disease progression, cause organ damage (e.g., lungs, intestines), and increase mortality risk. Consequently, infection control and prophylaxis are key elements of disease management, although such strategies do not prevent the underlying genetic disorder.[12][19]

### Lifestyle and Health System Factors

Although not studied systematically, access to **specialized immunology care, early diagnosis, and timely HSCT** likely influences outcomes. Patients in resource-limited settings or without access to advanced diagnostics and transplant facilities may have worse prognosis due to delayed diagnosis and untreated infections. Such health system factors are critical for disease course but do not modify underlying genetic susceptibility.

In summary, **environmental and lifestyle factors do not cause WIPF1 deficiency**, but infections are central to clinical expression, functioning as downstream triggers of complications in an immunodeficient host. The disease remains primarily driven by genetic WIPF1 loss-of-function, with environmental factors modulating severity and outcome.

## 6. Mechanism and Pathophysiology

### Ordered Causal Chain

The mechanistic sequence from genetic lesion to clinical disease in WIPF1 deficiency can be summarized as follows in causal terms, with inference noted where applicable:

Step 1: Biallelic loss-of-function mutations in the **WIPF1** gene lead to absence or severe reduction of functional WIP protein in hematopoietic cells.[10][11][15][16]  

Step 2: Loss of WIP protein leads to destabilization and degradation of WASP, resulting in markedly reduced or absent WASP protein despite normal WAS mRNA levels, as demonstrated in patient cells and inferred from WIP’s role as a WASP chaperone.[10][11][15][16]  

Step 3: Loss of WASP protein leads to defective Arp2/3-mediated actin filament nucleation and impaired actin cytoskeleton organization in T cells, NK cells, and platelets, inferred from the known role of WASP-WIP complexes in actin polymerization.[3][4][10][11][15][16]  

Step 4: Defective actin remodeling leads to impaired immune synapse formation, T-cell receptor (TCR) signaling, T-cell proliferation, and chemotaxis, and to impaired NK-cell cytotoxic granule polarization and degranulation, as demonstrated in WIP-deficient patient cells and mouse models.[10][11][12][15][16]  

Step 5: These cellular defects result in combined immunodeficiency characterized by decreased CD8\(^+\) T cells, reduced naïve T cells, impaired T-cell proliferation and migration, and defective NK-cell function, leading to heightened susceptibility to infections and poor viral clearance.[1][11][12][16][18]  

Step 6: In megakaryocytes and platelets, defective actin dynamics result in abnormal platelet production and function, leading to thrombocytopenia with normal or small platelets and a bleeding tendency, inferred from parallels with WAS and supported by patient phenotypes and WIPF1 knockout mice.[1][10][12][16][17][18]  

Step 7: Chronic infections and immune dysregulation driven by the combined immunodeficiency lead to secondary inflammatory diseases such as eczema, pneumonitis, colitis, and possibly autoimmunity, as observed in patients and WIP-deficient mice.[10][11][12][16][19]  

Step 8: Together, these immune and hematologic defects result in the clinical syndrome of **Wiskott–Aldrich syndrome 2**, with recurrent infections, thrombocytopenia, eczema, and inflammatory complications, culminating in early childhood morbidity and mortality if untreated.[1][10][11][12][16][18]

### Molecular Pathways

At the molecular level, WIPF1 deficiency disrupts several **actin-regulatory pathways** critical for immune cell function. WIP binds to WASP via its C-terminal domain and stabilizes the protein; in T cells, most WASP is complexed with WIP.[3][4][10][16] WASP, in turn, is a nucleation-promoting factor for the **Arp2/3 complex**, which initiates actin filament branching and polymerization. This actin polymerization is essential for formation of the **immune synapse**, lamellipodia, and filopodia, which underpin T-cell receptor signaling, cell migration, and target cell killing. GO terms that capture these processes include **GO:0007010** (*cytoskeleton organization*), **GO:0030036** (*actin cytoskeleton organization*), **GO:0008154** (*actin polymerization-dependent cell motility*), and **GO:0002250** (*adaptive immune response*).

In WIPF1 deficiency, the absence of WIP leads to **loss of WASP protein**, as demonstrated by immunoblotting in patient cells; WASP mRNA levels remain normal, confirming a post-transcriptional defect.[11][15][16] Lanzi et al. showed that reconstitution of the patient’s T cells with WIP restored WASP levels, indicating that WIP is necessary for WASP stability and that WIP deficiency is the primary defect.[11][15] ClinGen summarized this mechanistic relationship, noting that introduction of wild-type WIPF1 corrects the WASP defect.[10] Because WASP is central to Arp2/3 activation, WIPF1 deficiency results in **defective F-actin polymerization**, consistent with OMIM’s statement that the cellular abnormalities in WAS2 are thought to result from defective F-actin polymerization.[1][16][18]

Additional molecular pathways implicate WIP in **signal transduction and viral motility**. WIP contributes to the recruitment and activation of WASL (N-WASP) together with adaptor proteins NCK1 and GRB2, participating in pathways such as **regulation of actin dynamics for phagocytic cup formation** and **CD16 signaling in NK cells**.[4][10] WIP also acts as an adaptor for WASL recruitment to vaccinia virus, facilitating viral actin-based motility.[4] Although these roles are not directly linked to WIPF1 deficiency in humans, they underscore that WIP is a central hub in actin signaling pathways, suggesting that its loss may broadly disrupt cytoskeleton-dependent processes across immune cell types.

### Cellular Processes and Protein Dysfunction

At the cellular level, WIPF1 deficiency most profoundly affects **T cells, NK cells, and megakaryocytes/platelets**, each corresponding to distinct yet overlapping consequences of disrupted actin dynamics. In T cells, WIP–WASP complexes coordinate actin assembly at the immune synapse, enabling TCR microcluster formation, signaling, and stable interactions with antigen-presenting cells. WIP deficiency leads to defective T-cell proliferation in response to TCR stimulation and impaired chemotaxis, as shown in patient T cells and in WIP-deficient mice.[11][12][15][16][10] These defects manifest as **reduced CD8\(^+\) T cells**, decreased naïve T-cell counts, and impaired proliferation in vitro, as documented in patients.[1][11][12][16][18] GO terms relevant to these processes include **GO:0042110** (*T cell activation*), **GO:0042102** (*positive regulation of T cell proliferation*), and **GO:0002694** (*regulation of leukocyte activation*). The associated cell ontology terms include **CL:0000084** (*T cell*), **CL:0000625** (*CD8-positive, alpha-beta T cell*), and **CL:0000097** (*naïve T cell*).

In NK cells, WIP deficiency impairs cytotoxic function. Lanzi et al. found increased NK-cell numbers but decreased NK-cell function in the index patient, indicating that WIP is necessary for NK-cell cytotoxicity.[11][15][16] WIP participates in CD16 signaling and immune synapse formation in NK cells, and its absence likely disrupts granule polarization and degranulation.[4][10] This is reflected in reduced NK cytotoxic activity in patient assays and contributes to susceptibility to viral infections such as CMV.[11][12] The relevant GO terms include **GO:0001775** (*cell activation*), **GO:0042113** (*B cell activation*—by analogy), and **GO:0034097** (*response to cytokine*), while the cell ontology term is **CL:0000623** (*natural killer cell*).

In megakaryocytes and platelets, WASP and WIP regulate actin cytoskeleton organization required for **proplatelet formation and platelet release**. Although direct functional studies in WIPF1-deficient megakaryocytes are limited, WIPF1 knockout mice show thrombocytopenia, and patients consistently exhibit thrombocytopenia with normal or small platelets.[10][12][16][17] This suggests that WIP deficiency leads to **abnormal platelet production and/or survival**, likely via defects in actin-mediated proplatelet extension and platelet budding. GO terms include **GO:0030220** (*platelet formation*), **GO:0002576** (*platelet degranulation*), and **GO:0007596** (*blood coagulation*), while the relevant cell types are **CL:0000556** (*megakaryocyte*) and **CL:0000233** (*platelet*).

### Immune System Involvement and Tissue Damage

WIPF1 deficiency is classified as a **combined immunodeficiency**, reflecting defects in both cellular and humoral immunity. T-cell lymphopenia, especially affecting CD8\(^+\) T cells, impaired T-cell proliferation, and abnormal T-cell migration indicate a primary T-cell defect.[1][11][12][16][18] NK-cell dysfunction adds to impaired antiviral immunity.[11][12][16] B-cell abnormalities are less prominent but may include low B-cell counts and altered immunoglobulin levels, particularly variably increased IgE, analogous to WAS.[1][16][18] Together, these defects lead to poor adaptive immune responses, increased susceptibility to infections, and impaired immune regulation, which in turn predispose to chronic inflammation and tissue damage.

The tissues most affected by immune-mediated damage are the **skin, lungs, gut, and spleen**. Patients frequently develop eczema or eczematous dermatitis, reflecting chronic skin inflammation, possibly driven by dysregulated T-cell responses and impaired barrier immunity.[1][11][12][17][18][19] Interstitial pneumonitis and ulcerative colitis-like disease have been observed in WIPF1 knockout mice, and pneumonitis has been reported in humans, indicating chronic inflammatory damage in lungs and gut.[10][12][16] Chronic infections and inflammation can also lead to splenomegaly and lymphoid tissue enlargement, as seen in WIP-deficient mice with severe lymphopenia and splenomegaly.[10] These findings align with GO processes such as **GO:0006954** (*inflammatory response*), **GO:0006955** (*immune response*), and **GO:0032602** (*chemokine production*), and with UBERON anatomical terms such as **UBERON:0002048** (*skin*), **UBERON:0002046** (*lung*), **UBERON:0002107** (*intestinal tract*), and **UBERON:0002106** (*spleen*).

### Molecular Profiling and Advanced Technologies

To date, there are no published large-scale **transcriptomic, proteomic, metabolomic, or single-cell sequencing** studies specifically focused on WIPF1-deficient patients. However, the underlying mechanistic framework is well supported by **functional assays in patient cells** and **animal models**, as summarized by ClinGen.[10] For example, WIPF1 knockout mice model the human phenotype, exhibiting severe lymphopenia, splenomegaly, and inflammatory diseases such as ulcerative colitis and interstitial pneumonitis.[10] These models provide in vivo confirmation of the role of WIP in immune system development and function.

Given the limited patient numbers, **multi-omics integration** has not yet been feasible for WIPF1 deficiency, and there are no disease-specific datasets in GEO, PRIDE, or metabolomics databases. Nonetheless, future studies could leverage single-cell RNA-seq and proteomics of patient immune cells to delineate how WIPF1 loss-of-function reshapes transcriptional programs, signaling pathways, and metabolic states, particularly in T and NK cells.

In summary, the pathophysiology of WIPF1 deficiency is a **linear and well-defined chain** from WIPF1 loss-of-function to WIP loss, WASP degradation, defective actin cytoskeleton dynamics, impaired T and NK-cell function, abnormal platelet production, and clinical manifestations of combined immunodeficiency, thrombocytopenia, and eczema.[1][10][11][12][16][18] The key biological processes are captured by GO terms related to actin organization, T-cell activation, NK-cell function, and platelet formation, and the primary cell types involved are T cells, NK cells, and megakaryocytes (CL ontology).  

## 7. Anatomical Structures Affected

### Organ-Level Involvement

WIPF1 deficiency primarily affects **organs of the immune and hematopoietic systems**, along with skin and lungs as target organs of inflammation and infection. The **bone marrow** (UBERON:0002371) is a crucial site, as it produces T-cell precursors, NK cells, and megakaryocytes. Defects in WIP–WASP signaling in hematopoietic progenitors and megakaryocytes lead to lymphopenia and thrombocytopenia.[10][11][12][16][18] The **thymus** (UBERON:0002370) is also involved, given its role in T-cell maturation; although direct histologic studies of WIPF1-deficient thymus are lacking, reduced naïve T-cell output suggests impaired thymic function or survival of thymic emigrants.[11][12][16][18]

Peripheral lymphoid organs such as the **spleen** (UBERON:0002106) and **lymph nodes** (UBERON:0000029) are affected as sites of immune activation and proliferation. WIPF1 knockout mice exhibit splenomegaly and severe lymphopenia, indicating disrupted lymphoid homeostasis.[10] In humans, lymphopenia and altered lymphocyte subsets implicate these organs, although specific imaging or histology data are sparse.[11][12][16] The **skin** (UBERON:0002097) is involved through eczema and eczematoid dermatitis, while the **lungs** (UBERON:0002048) are affected by recurrent infections and pneumonitis, and the **intestinal tract** (UBERON:0002107) by chronic diarrhea and colitis-like inflammation.[10][11][12][16][19]  

These organ-level manifestations mark WIPF1 deficiency as a **multisystem disorder** rooted in the immune and hematopoietic systems (NCIT:C12740 *Immune System*, NCIT:C12679 *Hematopoietic System*), but with significant involvement of the integumentary (skin) and respiratory and gastrointestinal systems.

### Tissue and Cell-Level Involvement

At the tissue level, WIPF1 deficiency predominantly affects **hematopoietic tissues and immune effector tissues**, including lymphoid tissue, splenic white pulp, thymic cortex, and bone marrow stromal environments that support lymphopoiesis and thrombopoiesis.[10][11][12][16][18] The relevant tissue ontology terms include **UBERON:0001960** (*lymphoid tissue*), **UBERON:0002108** (*bone marrow*), and **UBERON:0002370** (*thymus*). Skin tissue, specifically the epidermis and dermis, are affected via eczema and dermatitis, reflecting inflammatory infiltrates and barrier dysfunction.

At the cell level, the primary cell types targeted are **T lymphocytes, NK cells, B cells, megakaryocytes, and platelets**, with secondary involvement of dendritic cells and other myeloid cells. Cell Ontology terms include **CL:0000084** (*T cell*), **CL:0000625** (*CD8-positive T cell*), **CL:0000097** (*naïve T cell*), **CL:0000623** (*natural killer cell*), **CL:0000236** (*B cell*), **CL:0000556** (*megakaryocyte*), and **CL:0000233** (*platelet*). WIP and WASP are particularly critical in **T cells and NK cells**, where they orchestrate actin-dependent immune synapse formation; their absence leads to impaired T-cell proliferation and chemotaxis and defective NK cytotoxicity.[3][4][10][11][12][15][16]

In megakaryocytes, WIP–WASP signaling contributes to actin cytoskeleton remodeling necessary for proplatelet extension and platelet release. Although direct microscopic observations are limited in human WIPF1 deficiency, the consistent presence of thrombocytopenia and variable platelet size suggests a primary defect in **megakaryocyte and platelet cytoskeleton function**.[10][12][16][17] In skin and mucosal tissues, T-cell and NK-cell dysfunction, along with impaired innate immune responses, likely contribute to eczema, chronic infections, and inflammatory lesions, though these tissues are primarily targets rather than sources of the primary defect.

### Subcellular Localization and Compartments

At the subcellular level, WIPF1-encoded WIP is a **cytosolic protein** that associates with actin filaments, WASP, and the plasma membrane at sites of active cytoskeleton remodeling. GO Cellular Component terms relevant to WIP include **GO:0005884** (*actin filament*), **GO:0005856** (*cytoskeleton*), **GO:0005938** (*cell cortex*), and **GO:0005925** (*focal adhesion*). WIP’s role in immune synapse formation suggests localization at the **immunological synapse**, a specialized plasma membrane–associated structure where T cells and NK cells interface with target cells; though not explicitly a GO term, it can be approximated by **GO:0001772** (*immunological synapse*).

In WIPF1 deficiency, the absence of WIP disrupts these subcellular structures. WASP, which is almost entirely complexed with WIP in T cells under normal conditions, is degraded in the absence of WIP, leaving the Arp2/3 complex without adequate activation at the membrane and impairing actin nucleation at the immune synapse.[10][11][15][16] This leads to altered cell shape, reduced lamellipodia, impaired formation of actin-rich protrusions, and defective polarization of cytotoxic granules in T and NK cells. These subcellular defects underpin the cellular and tissue-level phenotypes described above.

### Localization and Lateralization

WIPF1 deficiency does not exhibit **specific lateralization** (e.g., unilateral vs bilateral) in its anatomical manifestations. Lymphopenia, thrombocytopenia, and immune deficits are systemic, affecting both sides of the body equally, while eczema and infections can occur in various skin and organ locations without consistent asymmetry. Organ involvement such as pneumonitis, colitis, or splenomegaly is similarly global rather than localized to one side.

In summary, WIPF1 deficiency affects hematopoietic and immune organs (bone marrow, thymus, spleen), skin, lungs, and intestines, with primary defects at the level of T cells, NK cells, B cells, megakaryocytes, and platelets. Subcellularly, WIP functions at the actin cytoskeleton and immunological synapse, and its loss disrupts cytoskeleton-dependent processes that are critical for immune function and platelet production.[3][4][10][11][12][15][16]

## 8. Temporal Development

### Onset

WIPF1 deficiency **typically manifests in the neonatal or early infantile period**, reflecting its role in fundamental immune and hematopoietic processes. In the index case described by Lanzi et al., the female patient presented in early infancy with recurrent infections, eczema, and thrombocytopenia, prompting evaluation for WAS.[11][13][15][16] Another Moroccan infant was diagnosed at 11 days of age based on severe thrombocytopenia and family history, underscoring that the disease can manifest **immediately after birth**.[16] The 2018 synopsis of six WIP-deficient patients emphasized “extremely early onset of symptoms of primary immunodeficiency,” often within the first months of life.[12]  

These data support characterization of WIPF1 deficiency as a **congenital or early infantile-onset disorder**, best represented by HPO terms HP:0003593 (*Neonatal onset*) and HP:0003623 (*Infantile onset*). The onset pattern is **chronic**, in that immunodeficiency and thrombocytopenia are present from birth and persist without spontaneous remission, though infections may occur in episodic bursts.

### Progression and Disease Course

The natural course of WIPF1 deficiency without definitive treatment appears to be **rapidly progressive**, driven largely by cumulative infectious and inflammatory complications. Recurrent infections begin in infancy and may become more frequent and severe over time due to progressive damage to lungs, intestines, and other organs, as well as ongoing immune dysfunction.[11][12][16][19] Thrombocytopenia may be present from birth and can remain stable or worsen, depending on infections, splenic sequestration, and other factors. Eczema and skin manifestations may fluctuate but often persist and can be exacerbated by infections or immune activation.

The 2018 review noted that all patients had **very early onset of severe, life-threatening immunodeficiency**, and without HSCT, the prognosis is poor.[12] One patient died shortly after HSCT due to CMV-related respiratory distress, indicating that disease progression can be fatal even with treatment if infections are not controlled.[12] Another patient, treated with serial donor lymphocyte infusions followed by HSCT, showed resolution of immunodeficiency and thrombocytopenia by one year post-transplant.[12] The Moroccan index patient remained clinically healthy at 16 months after unrelated cord blood transplantation, with restored immune function and improved platelet counts.[16] These cases illustrate that the **pre-transplant course is progressive and life-threatening**, while **post-transplant course can be stabilizing or curative** if successful.

### Patterns and Critical Periods

The disease course of WIPF1 deficiency can be conceptualized in stages:

An **early stage** (neonatal to early infancy) characterized by thrombocytopenia, early infections (often respiratory or gastrointestinal), eczema, and initial recognition of immunodeficiency.  

A **progressive stage** (later infancy through early childhood) marked by recurrent severe infections, chronic diarrhea, failure to thrive, and emerging inflammatory complications such as pneumonitis or colitis, particularly if diagnosis and treatment are delayed.[11][12][16][19]  

A **terminal or advanced stage** (if untreated) characterized by irreversible organ damage (lung, gut, liver), severe malnutrition, and high risk of fatal infections or respiratory failure.  

Critical periods include the **first year of life**, when infections and failure to thrive often become apparent, and the **pre-transplant window**, when HSCT offers the best chance for cure but may be complicated by active infections.[11][12][16][18] Early identification of WIPF1 deficiency and timely HSCT are therefore critical to improving outcomes, analogous to other severe combined immunodeficiencies.

Patterns of remission or relapse have not been described, because **the underlying defect does not remit spontaneously**. However, with successful HSCT, patients may achieve **long-term remission of immunodeficiency and thrombocytopenia**, effectively converting the disease into a cured or stable state.[11][12][16] Post-transplant complications (graft-versus-host disease, infections, mixed chimerism) can influence long-term stability, but in the reported cases, surviving patients have remained clinically well for years after HSCT.[12][16]

In summary, WIPF1 deficiency is a **congenital, rapidly progressive combined immunodeficiency** with critical early-life windows for diagnosis and intervention. Without HSCT, the disease course leads to severe morbidity and early mortality, while early transplant can dramatically alter temporal development, shifting from rapid deterioration to stable long-term health.[11][12][16]

## 9. Inheritance and Population

### Inheritance Pattern

WIPF1 deficiency is unequivocally an **autosomal recessive** disorder. OMIM and MedGen explicitly classify WAS2 as autosomal recessive, and ClinGen’s gene–disease validity curation confirms this inheritance pattern.[1][10][16][18] In all reported families, affected individuals are **homozygous** for pathogenic truncating variants, while both parents are **heterozygous carriers**, often consanguineous.[11][15][16] There is no evidence of dominant inheritance, X-linkage, or mitochondrial transmission.  

The autosomal recessive pattern implies that **male and female children are equally likely to be affected**, in contrast to classic WAS (OMIM 277970), which is X-linked and predominantly affects males. Indeed, the index WIPF1-deficient patient described by Lanzi et al. was a female infant, underscoring this distinction.[11][13][15][16] This reinforces the need to consider WIPF1 deficiency in **both male and female infants** with WAS-like phenotypes but normal WAS sequencing.

### Penetrance and Expressivity

Because of the extremely small number of documented families, precise estimates of **penetrance** are not available. However, all known individuals with biallelic truncating WIPF1 variants have exhibited some combination of recurrent infections, thrombocytopenia, eczema, and immunologic abnormalities, suggesting **high, likely complete penetrance** for clinically significant immunodeficiency in individuals with classic loss-of-function variants.[11][12][16][19] In contrast, heterozygous carriers appear clinically normal, with approximately half-normal WIP levels and no overt immunodeficiency, suggesting **haplosufficiency** for WIPF1.[16]  

**Expressivity** appears **variable**, based on differences in platelet phenotype, skin manifestations, and severity of infections and inflammatory complications. The 2018 series emphasized that WIP-deficient patients displayed “extremely early onset of symptoms of primary immunodeficiency, but varying syndromic and laboratory features,” particularly regarding platelet size, thrombocytopenia, and IgE levels.[12] Some patients had severe microthrombocytopenia, others moderate thrombocytopenia with normal platelet volume; some had marked eczema, others milder skin involvement.[12][16][19] Autoimmune manifestations appear less frequent than in classic WAS, but arthritis and inflammatory symptoms have been reported.[12][19] This variability may reflect differences in the specific variant, genetic background, environmental exposures, or coexisting immunodeficiencies (e.g., ICOS deficiency).[19]

### Epidemiology and Population Demographics

Because WIPF1 deficiency has been reported in only a handful of individuals, there are **no reliable estimates of prevalence or incidence**. It is clearly an **ultra-rare disease**, likely much rarer than classic WAS. Orphanet, OMIM, and other registries note its rarity but do not provide quantitative epidemiologic data.[1][10][16][18] Extrapolation from the small number of published cases suggests that WIPF1 deficiency is currently recognized primarily in **families with consanguinity** and in regions where advanced immunologic and genetic diagnostics are available.

The existing cases span several geographic and ethnic backgrounds. The index patient reported by Lanzi et al. was of **Moroccan** origin, with consanguineous parents.[11][13][15][16] The Saudi Arabian kindred reported by Al-Mousa et al. indicates that WIPF1 deficiency is present in **Middle Eastern** populations with high rates of consanguinity.[16] The 2018 synopsis included patients from multiple countries, reflecting broader global distribution, though still clustered in regions with consanguineous marriages.[12] The Turkish patient with coexisting ICOS and WIPF1 mutations suggests that **Turkish** populations may also harbor WIPF1 variants, again within consanguineous families.[19]  

Specific **founder mutations** have not been definitively established, but the Q237X variant in the Saudi kindred may represent a regional founder mutation, while S434X appears in Moroccan patients.[16] Further studies and carrier screening in these populations would be needed to confirm founder effects. Carrier frequency in the general population is likely extremely low; pathogenic truncating variants are absent or nearly absent from gnomAD, consistent with strong negative selection.[6][8][9][10]

### Sex Ratio and Age Distribution

Unlike classic WAS, which predominantly affects males due to X-linked inheritance, WIPF1 deficiency affects **both sexes** approximately equally, as expected for an autosomal recessive trait. The small number of cases includes both male and female patients; the index patient was female, while some patients in the Saudi kindred and 2018 series were male.[11][12][16]  

The **age distribution** of diagnosis is heavily skewed toward **infancy**, reflecting severe early-onset disease. Most patients are diagnosed in the first year of life, and those who survive to later childhood often do so because of successful HSCT.[11][12][16][18] Without transplant, life expectancy is likely limited to early childhood, though individual outcomes may vary.

In summary, WIPF1 deficiency is an autosomal recessive, ultra-rare primary immunodeficiency with high penetrance for severe disease in biallelic truncating variant carriers and variable expressivity. It predominantly affects children of consanguineous unions, with cases reported in North African, Middle Eastern, and Turkish populations, and equal sex distribution.[11][12][16][19]

## 10. Diagnostics

### Clinical and Laboratory Evaluation

Diagnosis of WIPF1 deficiency begins with recognition of a **WAS-like clinical phenotype**—recurrent infections, eczema, thrombocytopenia, and combined immunodeficiency—particularly in a **female** or in a child with normal WAS sequencing. Standard laboratory tests include **complete blood count** with platelet count and mean platelet volume (MPV), immunoglobulin levels, and lymphocyte subsets. In WAS2, thrombocytopenia with normal platelet volume is typical, differing from the microthrombocytopenia of classic WAS.[1][16][18] Immunoglobulin levels may show variably increased IgE, similar to WAS.[1][16][18]

Immunologic tests assess **T-cell and NK-cell function**. Lanzi et al. measured T-cell proliferation in response to immobilized anti-CD3 and found markedly reduced proliferation, along with defective T-cell chemotaxis; NK-cell functional assays showed increased NK-cell numbers but decreased cytotoxic function.[11][15][16] Flow cytometry for lymphocyte subsets typically reveals **decreased CD8\(^+\) T cells**, reduced naïve T cells, and sometimes low B-cell counts, consistent with combined immunodeficiency.[1][11][12][16][18] The GTR clinical test description for WAS2 specifically lists decreased proportion of CD8-positive T cells and reduced NK-cell activity as key laboratory features.[18] These functional assays, while not pathognomonic, support the diagnosis of a combined immunodeficiency and help distinguish WIPF1 deficiency from isolated thrombocytopenia or eczema.

Biomarkers include **absence or marked reduction of WASP protein** in lymphocytes by immunoblotting or flow cytometry, combined with normal WAS gene sequence and mRNA, and absence of WIP protein.[11][15][16] Lanzi et al. emphasized that WAS cannot be diagnosed solely based on absence of WASP protein; sequence analysis of WAS is required, and if WAS is normal but WASP protein is absent, WIP deficiency should be suspected.[11][15] Therefore, **Western blot or flow cytometric analysis of WASP and WIP** can be a crucial diagnostic clue, particularly in centers that routinely perform these tests for suspected WAS.

Imaging studies (e.g., chest X-ray, CT) and biopsies are guided by clinical manifestations. Severe infections may prompt chest imaging that reveals pneumonia or interstitial lung disease, while chronic diarrhea or suspected colitis may lead to endoscopy and biopsies showing inflammatory changes. However, these findings are nonspecific and reflect complications rather than the primary disease.

### Genetic Testing

Definitive diagnosis of WIPF1 deficiency relies on **genetic testing**. The NCBI Genetic Testing Registry lists tests for “Wiskott-Aldrich syndrome 2, 614493; WAS2 (WIPF1 gene)” that perform **sequence analysis of all coding exons** of WIPF1 in a postnatal setting.[18] The recommended genetic testing strategy typically includes:

1. **Sequencing of the WAS gene** in patients with WAS-like phenotype (especially males), as classic WAS is more common.[11][15][16]  

2. If WAS sequencing is normal but WASP protein is absent or severely reduced, or if the patient is female, consider **targeted sequencing of WIPF1** or inclusion of WIPF1 in a **primary immunodeficiency gene panel**.[11][12][15][16][18]  

3. In settings where targeted testing is not available, **whole exome sequencing (WES)** or **next-generation sequencing (NGS) panels** for combined immunodeficiency can identify WIPF1 variants, as was the case in the 2018 series, where panel sequencing identified a novel stop-gain mutation.[12]  

Single-gene testing of WIPF1 involves Sanger or NGS-based sequencing of all exons and splice junctions, with deletion/duplication analysis if indicated. ClinVar provides a reference for interpreting variants, listing known pathogenic truncating variants and benign/likely benign variants.[2][6][7][8][9] Variants should be classified according to ACMG/AMP guidelines, considering the loss-of-function mechanism and ClinGen’s definitive gene–disease relationship.[10]  

Whole genome sequencing (WGS) is not specifically required for WIPF1 deficiency but may be useful in complex cases where multiple genes are involved (e.g., combined ICOS and WIPF1 mutations) or where structural variants are suspected. Chromosomal microarray, karyotyping, and FISH are generally not informative for WIPF1 deficiency because the disease is caused by intragenic point mutations or small indels rather than large chromosomal abnormalities.[10][11][12][16]

### Clinical Criteria and Differential Diagnosis

There are no formal **society guidelines** or standardized diagnostic criteria for WIPF1 deficiency, given its rarity. Diagnosis is typically based on the combination of clinical, immunologic, and genetic findings:

A WAS-like clinical phenotype (recurrent infections, eczema, thrombocytopenia) with early onset.  

Evidence of combined immunodeficiency (reduced CD8\(^+\) T cells, impaired T-cell proliferation, defective NK function).  

Absence or marked reduction of WASP protein with normal WAS gene sequencing and mRNA levels.[11][15][16]  

Identification of biallelic pathogenic WIPF1 variants by genetic testing.[10][11][12][16]  

The **differential diagnosis** includes classic **Wiskott–Aldrich syndrome (OMIM 277970)**, caused by X-linked mutations in WAS; **other combined immunodeficiencies** with thrombocytopenia and eczema; and **isolated thrombocytopenias** or eczema without immunodeficiency. Key distinguishing features include **sex and inheritance pattern** (WAS affects mostly males and is X-linked, WIPF1 deficiency affects both sexes and is autosomal recessive), **platelet size** (microthrombocytopenia in WAS, normal or small platelets in WIPF1 deficiency), and **genetic findings** (WAS vs WIPF1 mutations).[1][10][11][12][16][18] Combined immunodeficiencies such as DOCK8 deficiency, ICOS deficiency, and others may present with overlapping features, so comprehensive NGS panels are often used to differentiate among them.[12][19]

### Screening

There are currently **no newborn screening programs** specifically targeting WIPF1 deficiency. However, some newborn screening panels for severe combined immunodeficiency (SCID) based on TRECs (T-cell receptor excision circles) may incidentally detect WIPF1-deficient infants due to reduced naïve T-cell output, though this has not been explicitly reported.[12][18] Given the ultra-rare nature of the disease, population-based screening is unlikely to be cost-effective.  

**Carrier screening** may be considered in consanguineous families with known WIPF1 mutations, as part of preconception counseling. **Prenatal testing** and **preimplantation genetic diagnosis (PGD)** could be offered when pathogenic variants are known, using targeted sequencing of WIPF1 in chorionic villus or amniotic samples, though no published cases of such testing in WIPF1 deficiency are available.

In summary, diagnosis of WIPF1 deficiency relies on the integration of clinical features, immunologic studies, protein analyses of WASP and WIP, and definitive **genetic confirmation** of biallelic WIPF1 loss-of-function variants, with WES or panel sequencing as key tools in current practice.[10][11][12][16][18]

## 11. Outcome and Prognosis

### Survival, Mortality, and Life Expectancy

Because of the small number of reported patients, precise **survival rates** and life expectancy estimates for WIPF1 deficiency are not available. However, the clinical course described in case series suggests **high mortality in early childhood without definitive treatment**, primarily due to severe infections and their complications.[11][12][16] In the initial report by Lanzi et al., the Moroccan index patient underwent unrelated cord blood transplantation at 4.5 months of age and was alive and clinically healthy 16 months later, indicating that early HSCT can rescue survival.[11][15][16] In the Saudi kindred and the 2018 series, some patients survived for years after HSCT, while at least one patient died from CMV-related respiratory distress shortly after transplant.[12][16]  

Without HSCT, WIPF1 deficiency is expected to carry a **poor prognosis**, analogous to severe combined immunodeficiency, with fatal outcomes in early childhood due to recurrent infections, failure to thrive, and organ damage. With HSCT, life expectancy can approximate that of the general population, provided engraftment is successful and complications are managed, though long-term data beyond a decade are limited.[11][12][16]

### Morbidity, Disability, and Quality of Life

Morbidity in WIPF1 deficiency is substantial, driven by repeated hospitalizations for infections, chronic diarrhea, eczema, bleeding episodes due to thrombocytopenia, and complications of immune dysregulation such as pneumonitis and colitis.[11][12][16][19] Failure to thrive and growth delay are common, impairing physical development and potentially cognitive development through prolonged illness and malnutrition. Chronic eczema and skin lesions contribute to discomfort, pruritus, and risk of secondary skin infections, affecting quality of life and social participation.[12][19]  

No formal **quality-of-life** studies (EQ-5D, SF-36, PROMIS) have been conducted specifically in WIPF1-deficient patients, but by analogy with WAS and other combined immunodeficiencies, affected children and their families face significant psychosocial stress, economic burden, and limitations in daily functioning due to frequent medical care, infection precautions, and invasive treatments. HSCT, if successful, can dramatically improve quality of life by restoring immune function and normalizing platelet counts, though the process itself carries risks and requires prolonged hospitalization and follow-up.[11][12][16]

### Prognostic Factors

Key **prognostic factors** in WIPF1 deficiency include:

Age at diagnosis and initiation of HSCT: earlier diagnosis and transplant, particularly before severe infections or organ damage, are associated with better outcomes, as seen in the Moroccan index patient.[11][16]  

Infection burden and control, especially with CMV, which has been a major cause of morbidity and mortality in reported patients.[12][19]  

Donor type and transplant conditioning regimen: matched sibling donor HSCT may offer better outcomes than unrelated or cord blood donors, though specific comparative data are limited; reduced-intensity conditioning may be considered to reduce toxicity.[12][16]  

Presence of additional immunodeficiencies or genetic defects (e.g., ICOS deficiency), which may complicate HSCT and long-term immune reconstitution.[19]  

Residual immune function and chimerism post-transplant: patients with good donor chimerism in T, B, and myeloid lineages tend to have better immune reconstitution and fewer complications.[12][16]  

There are no validated **prognostic biomarkers** unique to WIPF1 deficiency beyond these clinical factors, though T-cell counts, NK-cell function, and WASP/WIP expression levels may be useful in monitoring disease activity and transplant success.

In summary, prognosis in WIPF1 deficiency is **guarded without HSCT** but can be **excellent with early and successful HSCT**, particularly when infections are controlled and appropriate donors and conditioning regimens are available.[11][12][16]

## 12. Treatment

### Pharmacotherapy and Supportive Care

At present, there is **no disease-specific pharmacotherapy** that corrects the underlying WIPF1 defect. Treatment focuses on **supportive care**, **infection prophylaxis and treatment**, and **management of thrombocytopenia and eczema**, similar to other combined immunodeficiencies and WAS. Supportive care strategies include:

Prophylactic antibiotics and antivirals to reduce the risk of bacterial and viral infections, particularly for CMV, which has been a major pathogen in reported cases.[12][19] This corresponds to NCIT terms such as **NCIT:C28194** (*Anti-Infective Agent*).  

Intravenous immunoglobulin (IVIG) replacement therapy to support humoral immunity and reduce infection frequency, especially in patients with hypogammaglobulinemia; this aligns with **NCIT:C62016** (*Immune Globulin Therapy*).[12][19]  

Platelet transfusions or thrombopoietic agents in cases of severe thrombocytopenia with bleeding, though specific data in WIPF1 deficiency are limited; these interventions correspond to **NCIT:C1502** (*Platelet Transfusion*).  

Topical and systemic therapies for eczema and dermatitis, such as emollients, topical corticosteroids, and immunomodulators, though these are symptomatic and do not address the underlying immune defect.  

In the Turkish patient with coexisting ICOS and WIPF1 mutations, supportive measures included antiepileptic drugs for seizures, prolonged antibiotic therapy, and multiple hospitalizations for infections.[19] These supportive interventions are essential but may be insufficient to prevent progression without definitive therapy.

### Hematopoietic Stem Cell Transplantation (HSCT)

Allogeneic **hematopoietic stem cell transplantation (HSCT)** is currently the **treatment of choice and the only curative therapy** for WIPF1 deficiency, as it can reconstitute a functional immune system and normalize platelet counts.[1][11][12][16][18] Orphanet and OMIM note that “hematopoietic stem cell transplantation is curative” for WAS2, and the 2018 review emphasizes that allogeneic HSCT is the treatment of choice if an appropriate donor is available.[1][12][18] HSCT corresponds to NCIT term **NCIT:C15313** (*Hematopoietic Stem Cell Transplantation*).

In the Moroccan index patient, an unrelated cord blood transplantation at 4.5 months of age led to restoration of immunologic function and resolution of thrombocytopenia, with the patient clinically healthy and with full T- and B-cell donor chimerism at 16 months follow-up.[11][15][16] In the 2018 series, multiple HSCT approaches were used, including matched sibling donor HSCT and cord blood transplantation, with three of four transplanted patients surviving and doing well 2–12 years post-transplant.[12] One patient died from CMV-related respiratory distress shortly after HSCT, highlighting the importance of infection control at the time of transplant.[12]

An especially instructive case described in the 2018 review involved a patient with life-threatening invasive CMV infection and WIPF1 deficiency. Because the patient’s condition was too unstable for conditioning chemotherapy, clinicians administered **serial, unconditioned, maternal, HLA-identical donor lymphocyte infusions (DLI)** to reduce viral load and stabilize the patient.[12] Once stabilized, the patient underwent a treosulfan/melphalan-conditioned peripheral blood HSCT with TCRαβ/CD19-depleted graft, followed by CMV-specific DLI to prevent reactivation. At one year post-HSCT, the patient was alive and well, with restored immune system and platelet counts.[12] This case demonstrates

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 70 |
| Resolved | 68 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 29 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000974` (1 mention) - the report calls it "Eczematoid dermatitis"; HP calls it **Hyperextensible skin**
- `HP:0002720` (2 mentions) - the report calls it "Lymphopenia"; HP calls it **Decreased circulating IgA concentration**
- `HP:0002723` (1 mention) - the report calls it "Abnormality of T-cell subsets"; HP calls it **Absence of bactericidal oxidative respiratory burst in phagocytes**
- `HP:0002721` (1 mention) - the report calls it "Abnormal immunologic reaction"; HP calls it **Immunodeficiency**
- `HP:0003236` (1 mention) - the report calls it "Decreased proportion of CD8-positive T cells"; HP calls it **Elevated circulating creatine kinase activity**
- `HP:0002758` (1 mention) - the report calls it "Abnormal T cell proliferation"; HP calls it **Osteoarthritis**
- `HP:0002725` (1 mention) - the report calls it "Abnormal NK cell function"; HP calls it **Systemic lupus erythematosus**
- `HP:0002722` (1 mention) - the report calls it "Abnormal immunoglobulin level"; HP calls it **Recurrent abscess formation**
- `HP:0002019` (1 mention) - the report calls it "Inflammatory bowel disease"; HP calls it **Constipation**
- `UBERON:0002107` (2 mentions) - the report calls it "intestinal tract"; UBERON calls it **liver**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001876` (1 mention) - the report calls it "Abnormal platelet count"; HP calls it **Pancytopenia**, and lists "Low blood cell count" among its other names
- `HP:0005403` (2 mentions) - the report calls it "Abnormal T cell morphology"; HP calls it **Decreased total T cell count**, and lists "T cell lymphopenia" among its other names
- `HP:0003593` (2 mentions) - the report calls it "Neonatal onset"; HP calls it **Infantile onset**
- `HP:0003623` (2 mentions) - the report calls it "Infantile onset"; HP calls it **Neonatal onset**
- `HP:0002090` (1 mention) - the report calls it "Pneumonitis"; HP calls it **Pneumonia**
- `HP:0001508` (1 mention) - the report calls it "Failure to thrive in infancy"; HP calls it **Failure to thrive**
- `UBERON:0002097` (1 mention) - the report calls it "skin"; UBERON calls it **skin of body**, and lists "skin" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Orphanet`.