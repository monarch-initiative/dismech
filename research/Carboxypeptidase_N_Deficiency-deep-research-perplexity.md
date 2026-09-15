---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-11T12:15:41.753699'
end_time: '2026-09-11T12:21:37.509013'
duration_seconds: 355.76
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Carboxypeptidase N Deficiency
  mondo_id: MONDO:0008910
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 17
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 35
  verified: 33
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.029
  labels_checked: 31
  labels_matching: 14
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: HP:0001873
    reported_labels:
    - Angioedema
    ontology_label: Thrombocytopenia
  - term_id: HP:0000293
    reported_labels:
    - Facial swelling
    ontology_label: Full cheeks
  - term_id: HP:0001099
    reported_labels:
    - Swelling of the hands
    ontology_label: Atrophic fundus lesion
  - term_id: HP:0001761
    reported_labels:
    - Swelling of the feet
    ontology_label: Pes cavus
  - term_id: HP:0011121
    reported_labels:
    - Urticaria
    ontology_label: Abnormal skin morphology
  - term_id: CL:0000761
    reported_labels:
    - Basophils
    ontology_label: type 9 cone bipolar cell (sensu Mus)
  - term_id: UBERON:0002190
    reported_labels:
    - skin of upper limb
    ontology_label: subcutaneous adipose tissue
  - term_id: UBERON:0002191
    reported_labels:
    - skin of lower limb
    ontology_label: subiculum
  - term_id: UBERON:0001830
    reported_labels:
    - lip
    ontology_label: minor salivary gland
  - term_id: NCIT:C80474
    reported_labels:
    - Icatibant
    ontology_label: Device Parameters
  - term_id: NCIT:C82474
    reported_labels:
    - C1 Esterase Inhibitor
    ontology_label: Egg Laying
  - term_id: NCIT:C380
    reported_labels:
    - Tranexamic Acid
    ontology_label: Clonidine
  - term_id: NCIT:C47484
    reported_labels:
    - Montelukast
    ontology_label: Dibenzothiophene
  labels_variant: 4
  unresolved_terms:
  - HP:0001715
  unresolvable_prefixes:
  - DO
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Carboxypeptidase N Deficiency
- **MONDO ID:** MONDO:0008910 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Carboxypeptidase N Deficiency** covering all of the
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

# Carboxypeptidase N Deficiency (CPND): An Integrative Disease Profile

Carboxypeptidase N deficiency is a rare Mendelian disorder of plasma peptide catabolism characterized clinically by recurrent episodes of bradykinin-mediated angioedema, variably accompanied by urticaria, asthma and allergic hypersensitivity, and biochemically by markedly reduced activity of the plasma metalloenzyme carboxypeptidase N (CPN), also known as kininase I and anaphylatoxin inactivator.[1][9][11] At the molecular level, the disease is caused by biallelic loss-of-function variants in the **CPN1** gene on chromosome 10q24.2, which encodes the 50‑kDa catalytic subunit of the CPN tetramer.[2][4][5][8] The resulting failure to cleave C‑terminal arginine and lysine residues from bradykinin, complement anaphylatoxins C3a and C5a, and related peptides leads to their pathological accumulation, triggering increased vascular permeability, endothelial and mast cell activation, and the characteristic angioedema and urticaria in affected individuals.[1][5][11][14] Clinical series and recent description of hereditary angioedema with normal C1 inhibitor associated with CPN deficiency (HAE‑CPN) have broadened the phenotype, demonstrated frequent but not obligatory co‑occurrence of angioedema and urticaria, and identified CPN1 deficiency as a distinct endotype of kinin-driven disease in which excess bradykinin arises solely from impaired catabolism.[10][14][16] Only a small number of families and approximately ten molecularly characterized patients have been reported worldwide, with autosomal recessive inheritance and milder manifestations in heterozygous carriers.[1][6][9][11] Diagnostic workup integrates measurement of circulating CPN activity, demonstration of normal C1 inhibitor and complement levels, and targeted sequencing of CPN1, while treatment parallels other forms of bradykinin-mediated angioedema, using agents such as icatibant and tranexamic acid, careful avoidance of triggers, and genetic counseling for affected families.[10][11][14][16] 

## 1. Disease Information

### 1.1 Definition and Clinical Overview

Carboxypeptidase N deficiency (CPND) is an inborn error of plasma protein metabolism in which the activity or concentration of carboxypeptidase N, a serum α‑globulin zinc metalloenzyme, is severely reduced.[1][8][11] Carboxypeptidase N normally regulates the activity of peptides such as kinins and complement anaphylatoxins by removing C‑terminal basic amino acids, thereby inactivating or modulating their receptor-binding properties.[1][11][15] In the absence of sufficient enzymatic activity, bradykinin, kallidin, C3a, C4a and C5a persist in the circulation and interstitial space, driving episodic increases in vascular permeability that manifest clinically as angioedema of the skin and mucosal surfaces.[1][11][14] 

The Online Mendelian Inheritance in Man (OMIM) entry 212070 describes CPND as an autosomal recessive disorder characterized by episodic angioedema, acute or chronic urticaria, asthma, and allergic hypersensitivities such as hay fever, with low levels of carboxypeptidase N in the serum.[1][3][9] The original familial case series by Mathews and colleagues reported a proband with eleven years of recurrent angioedema (approximately forty episodes) and very low CPN activity, and documented intermediate levels and milder symptoms in heterozygous relatives, establishing a spectrum of clinical severity.[11] More recently, Denis Vincent and collaborators have reported families with hereditary angioedema with normal C1 inhibitor (HAE‑nC1‑INH) in whom CPN deficiency due to CPN1 variants underlies recurrent peripheral, abdominal and laryngeal edema, often accompanied by urticaria and triggered by physical or hormonal factors.[10][16] These observations confirm that CPND is not only a biochemical abnormality but a clinically significant disorder of kinin and anaphylatoxin catabolism that overlaps with, yet is distinct from, classical hereditary angioedema due to SERPING1 mutations.

From a nosological perspective, CPND belongs to the broader group of rare genetic angioedema syndromes and can be classified as a **Mendelian** disease with predominantly **bradykinin-mediated angioedema** rather than histamine-driven allergic angioedema.[1][9][14] The condition is extremely rare, with the Leiden Open Variation Database (LOVD) listing only ten reported individuals and eight phenotype entries associated with CPN1-related carboxypeptidase N deficiency.[6] Because CPND affects systemic plasma enzyme activity, its manifestations can involve multiple organ systems, including the integumentary, respiratory, gastrointestinal and immune systems, and episodes may range from disfiguring facial swelling to life‑threatening laryngeal edema.[1][3][9][11]

### 1.2 Key Identifiers and Nomenclature

The primary disease identifier for carboxypeptidase N deficiency in human genetics is OMIM 212070, which corresponds to “CARBOXYPEPTIDASE N DEFICIENCY; CPND.”[1][3] The causal gene **CPN1** carries OMIM entry 603103 and is recognized by the HGNC-approved gene symbol *CPN1* (carboxypeptidase N, polypeptide 1).[2][5][8] In structured disease ontologies, CPND is included in resources such as the Disease Ontology (DO:0111583) and SNOMED CT under terms associated with carboxypeptidase N deficiency and hereditary angioedema.[1][2] The user has specified the Mondo Disease Ontology identifier MONDO:0008910 for CPND, reflecting its representation as a rare monogenic disorder in integrative disease knowledge graphs, although this identifier is not explicitly referenced in the current search results.

Common synonyms and alternative names include “carboxypeptidase N deficiency,” “CPN deficiency,” “CPND,” “CPN1D” (as used in LOVD), “familial carboxypeptidase N deficiency,” and “hereditary angioedema with carboxypeptidase N deficiency” or “HAE‑CPN” in the context of normal C1 inhibitor hereditary angioedema endotypes.[1][6][9][10][14] Historically, the enzyme itself has been referred to as “kininase I” and “anaphylatoxin inactivator,” and early literature sometimes described affected patients as having “kininase I deficiency” rather than using the term CPN.[11][15] In the NCBI Gene and Genetic Testing Registry (GTR), the gene is listed as *CPN1* (also known as *CPN* or *SCPN*), and associated diagnostic tests are catalogued under “carboxypeptidase N deficiency” or “CPN1-related hereditary angioedema.”[8][10]

There is no evidence from the present sources that CPND is assigned a unique ICD‑10 or ICD‑11 code; instead, clinical coding likely relies on more general codes for angioedema (such as ICD‑10 T78.3, “angioedema”) and allergic conditions, with CPND recognized primarily in specialist immunology and clinical genetics contexts rather than in routine coding systems.[1][9] MeSH terminology for carboxypeptidase N and its deficiency is implicit in PubMed indexing for the key clinical and molecular studies, but a dedicated MeSH descriptor for CPND has not been highlighted in the available data.[4][11]

### 1.3 Nature of Available Information

The information currently available about CPND is derived predominantly from aggregated disease-level resources and a small number of detailed case reports and familial series rather than from large cohort studies or electronic health record (EHR)-based analyses.[1][4][6][9][11] OMIM and Malacards provide structured disease descriptions, inheritance patterns, and phenotypic summaries that synthesize individual case reports, biochemical studies, and genetic analyses.[1][9][11] LOVD and ClinVar curate specific CPN1 variants and their clinical significance, while NCBI Gene and GTR supply gene-level annotations, genomic coordinates, and testing options.[2][6][7][8]

The seminal human clinical evidence arises from the original familial deficiency described by Mathews et al. (1980; PMID:7437116), which documented clinical manifestations, serum CPN levels, and segregation patterns, and from the genomic characterization by Cao and Hegele (2003; PMID:12560874), which sequenced CPN1 in an affected subject and identified causative frameshift and missense mutations.[4][11] More recent clinical evidence comes from the 2024 study of HAE‑nC1‑INH associated with CPN deficiency and its 2025 corrrespondence, which detail clinical presentation, biochemical parameters and response to therapy in several families.[10][14][16] Experimental studies in human plasma and animal models provide mechanistic insight into bradykinin and anaphylatoxin metabolism, but the overall body of literature on CPND remains limited, reflecting the rarity of the disease.[5][12][13][15] 

Given this context, most of the disease characteristics described in this report are based on aggregated interpretations of individual clinical cases, small pedigrees, and experimental work rather than population-level epidemiological data, and many aspects of CPND (such as precise prevalence, penetrance estimates and quality‑of‑life metrics) remain incompletely characterized.

## 2. Etiology, Risk and Protective Factors

### 2.1 Genetic Causal Factors

The primary etiological factor in carboxypeptidase N deficiency is **biallelic loss-of-function mutations in the CPN1 gene**, which encodes the catalytic subunit of the CPN tetramer.[1][2][4][5][8] CPN1 is a protein-coding gene located on chromosome 10q24.2, with genomic coordinates 10:100,042,193–100,081,869 on the GRCh38 assembly, and encodes a 50‑kDa zinc-dependent carboxypeptidase that cleaves C‑terminal arginine and lysine residues from peptides such as bradykinin and complement anaphylatoxins.[2][5][8] The OMIM entry for CPND carries a number sign (#) to indicate that some cases are caused by mutations in CPN1, and genetic linkage and sequencing studies have confirmed that CPN1 is the key causal gene.[1][2][4][5]

Cao and Hegele sequenced the CPN1 gene in archival genomic DNA from a subject with documented carboxypeptidase N deficiency and identified two loss-of-function variants: a frameshift insertion in exon 1 (385fsInsG) and a missense mutation in exon 3 (G178D) affecting a conserved active-site residue.[4][5] These variants were absent or extremely rare in 128 normal Caucasian controls, and the compound heterozygous genotype in the affected individual explained the marked reduction in plasma CPN activity, establishing CPN1 as the gene that causes the CPND enzymatic phenotype.[4][5] ClinVar currently classifies the NM_001308.3(CPN1):c.533G>A (p.Gly178Asp) variant as pathogenic based on literature evidence and its occurrence in patients with CPND.[7] LOVD lists CPN1 as the sole gene associated with disease #01691 (carboxypeptidase N deficiency) and notes autosomal recessive inheritance, further supporting the central etiological role of CPN1.[6]

Malacards conceptualizes CPND as a plasma protein metabolism disease with material basis in homozygous or compound heterozygous mutation in the CPN1 gene, emphasizing that low serum levels of CPN lead to episodic angioedema, chronic urticaria, asthma and allergic hypersensitivity.[9] Although Malacards notes “9 genes associated with carboxypeptidase N deficiency,” the evidence for direct causality beyond CPN1 is limited; these additional genes likely reflect broader association with angioedema phenotypes or related pathways rather than primary causation of CPND itself.[9] In summary, the etiological foundation of CPND is a germline, autosomal recessive loss of function in CPN1, leading to systemic deficiency of carboxypeptidase N activity and impaired catabolism of vasoactive peptides.[1][4][5][7][11]

### 2.2 Environmental and Physiological Risk Factors

While the fundamental cause of CPND is genetic, several environmental and physiological factors modulate the risk, severity and expression of clinical episodes by influencing bradykinin formation, complement activation, or vascular responsiveness. The 2024 HAE‑CPN study and its corrigendum highlight that in affected families, angioedema attacks were often triggered by mechanical pressure, cold exposure, fatigue and hormonal stimuli such as gonadotropin-releasing hormone agonists (e.g., triptorelin), suggesting that physical stressors and endocrine fluctuations can precipitate symptomatic episodes in the setting of underlying CPN1 deficiency.[10][16] In the reported female patient II.1 (family table), angioedema with urticaria was triggered by pressure-induced pruritus and triptorelin, with onset at 41 years and a two-year diagnostic delay.[16] In another male patient, chronic urticaria and angioedema were provoked by pressure, cold and fatigue from age 18, with a fourteen-year delay before diagnosis.[16] These observations indicate that mechanical trauma, temperature changes and systemic stress are key environmental risk factors that act on a genetically vulnerable bradykinin system.

Pharmacologic modulation of the renin–angiotensin system, particularly through angiotensin-converting enzyme inhibitors (ACEi), represents another important environmental risk factor in bradykinin-mediated angioedema more broadly and may be particularly deleterious in CPND.[12][13][14] In human plasma, Kovanen and Kokkonen demonstrated that at low, physiologically relevant nanomolar bradykinin concentrations, ACE is the principal enzyme responsible for inactivating bradykinin by converting it into the inactive metabolite BK-(1–7), whereas at high micromolar concentrations, carboxypeptidase N-like activity becomes the major degrading pathway, converting bradykinin to BK-(1–8).[12][13] Therefore, ACE inhibition elevates circulating bradykinin by impairing its primary catabolic route, and in individuals with concomitant CPN deficiency, both major bradykinin-degrading pathways are compromised, fostering substantial kinin accumulation.[12][13][14] 

The 2025 J Allergy Clin Immunol Glob correspondence explicitly links the pathophysiology of HAE‑CPN to ACEi-induced angioedema, noting that lack of kinin catabolism accumulates ligand at receptors in iatrogenic ACEi angioedema and that rash, including urticaria, is not uncommon in patients with ACEi-associated angioedema.[14] The authors argue that bradykinin-mediated angioedema cannot be ruled out on the basis of urticaria alone and that similar synergistic accumulation of kinins and anaphylatoxins contributes to both HAE‑CPN and ACEi angioedema, underscoring ACEi use as a relevant risk factor in individuals with impaired CPN activity.[14] 

Other potential physiological risk modifiers include atopic status and IgE-mediated hypersensitivity, as suggested by OMIM and Malacards, which report ragweed hay fever, asthma, elevated IgE levels and various allergic hypersensitivities in affected individuals.[1][9] These comorbid allergic conditions may prime mast cells and basophils, sensitize microvasculature, and thereby enhance responsiveness to bradykinin and anaphylatoxins, though robust quantitative data linking atopy to increased attack frequency in CPND are not yet available.[1][9][11]

### 2.3 Genetic and Environmental Protective Factors

Specific genetic protective variants or modifier alleles that attenuate CPND severity have not been clearly delineated in the available literature. Given that CPND is caused by severe loss-of-function alleles in CPN1, the principal protective factor is likely the presence of at least one functional allele, as evidenced by milder manifestations in heterozygous carriers.[4][6][9][11] Mathews et al. reported that family members with intermediate carboxypeptidase N levels (presumably heterozygotes) experienced less frequent and less severe episodes of angioedema compared with the proband, indicating partial protection conferred by residual enzyme activity.[11] Malacards similarly notes that heterozygotes have milder manifestations than homozygous or compound heterozygous individuals, which can be interpreted as a gene dosage-dependent protective effect.[9] 

At the environmental level, avoidance of pharmacologic agents that elevate bradykinin (such as ACE inhibitors), careful management of physical triggers (e.g., minimizing sustained pressure, thermal extremes), and proactive reduction of inflammatory stimuli (e.g., control of asthma and atopic disease) can be considered protective strategies, although direct evidence for their quantitative impact in CPND is limited.[12][13][14][16] In the reported HAE‑CPN families, prophylactic use of tranexamic acid, montelukast and careful trigger avoidance led to reduced attack frequency, suggesting that modulating the fibrinolytic system and leukotriene pathways may provide some protective benefit by decreasing upstream stimuli for kinin generation or mast cell activation.[10][16] 

### 2.4 Gene–Environment Interactions

The interplay between CPN1 genotype and environmental exposures is central to the clinical expression of CPND. On the genetic side, CPN1 loss-of-function variants create a baseline vulnerability by impairing catabolism of bradykinin and anaphylatoxins, effectively lowering the threshold at which physiological stimuli translate into pathological vascular leakage.[4][5][11][14] On the environmental side, factors that increase kinin generation (such as trauma, surgery, infections, hormonal fluctuations or ACE inhibition) or that amplify inflammatory signaling (such as allergens, cold, pressure and fatigue) act as triggers that tip the system into overt angioedema.[12][13][14][16]

The HAE‑CPN literature emphasizes that accumulation of both kinins and anaphylatoxins in the context of defective catabolism produces a **synergistic effect on endothelial and mast cell receptors**, driving combined activation and leading to angioedema with or without concomitant urticaria.[14] This synergy highlights a gene–environment interaction in which the genetic defect in CPN1 amplifies the impact of environmental complement activation and contact system stimuli. The authors specifically note that in ACEi-induced angioedema, lack of kinin catabolism likewise accumulates ligand on receptors, and the presence of urticaria does not exclude bradykinin-mediated disease, suggesting that ACE inhibition constitutes an environmental exposure that unmask or exacerbates latent susceptibility due to CPN1 deficiency.[14]

Although large-scale gene–environment interaction studies for CPND are not available, the mechanistic evidence supports a conceptual model in which CPN1 loss-of-function interacts with ACE inhibition, mechanical stress, cold, fatigue and hormonal therapies to determine the timing, severity and pattern (angioedema versus urticaria) of clinical episodes. In this sense, CPND can be viewed as a monogenic disease whose penetrance and expressivity are heavily modulated by environmental inputs into the kinin–complement–mast cell axis.

## 3. Phenotypes and Clinical Manifestations

### 3.1 Cutaneous and Subcutaneous Angioedema

The cardinal clinical manifestation of carboxypeptidase N deficiency is **episodic angioedema**, a rapid-onset, non-pitting, localized swelling of the deep dermis and subcutaneous or submucosal tissues, driven by increased vascular permeability rather than inflammatory cell infiltration.[1][3][9][11] OMIM’s clinical synopsis for CPND lists facial swelling, swelling of the lips and tongue, swelling of the hands and feet, and episodic angioedema affecting various soft tissues, reflecting the broad anatomical distribution of swellings.[3][9] Malacards similarly enumerates urticaria and episodic angioedema under “Skin, Nails, Hair” phenotypes, and notes peripheral angioedema of the extremities as a common feature.[9] 

In the Mathews family, the proband experienced approximately forty episodes of angioedema over eleven years, involving the face, extremities and gastrointestinal tract, often accompanied by discomfort but typically without pruritus, consistent with bradykinin-mediated edema.[11] The HAE‑CPN families reported by Vincent et al. also showed frequent peripheral angioedema, with swelling of the limbs and, in some cases, macroglossia, reinforcing the observation that CPND predominantly affects subcutaneous and submucosal tissues supplied by rich microvascular networks.[10][16] These episodes correspond to the Human Phenotype Ontology (HPO) term *Angioedema* (HP:0001873), often further specified as *Facial swelling* (HP:0000293), *Swelling of the hands* (HP:0001099), *Swelling of the feet* (HP:0001761), and *Macroglossia* (HP:0000154).

Age of onset for cutaneous angioedema in CPND appears to be in adolescence or adulthood in documented cases, with the Mathews proband presenting at age 54 (with a history starting circa age 54) and HAE‑CPN patients developing symptoms between late adolescence and early middle age (18–41 years).[11][16] Severity is variable, ranging from disfiguring but self-limited facial or extremity swelling to potentially fatal laryngeal edema, and progression is episodic rather than chronic, with individual attacks evolving over hours and resolving over days.[1][3][9][11][16] The frequency of angioedema episodes varies widely, from several per year to multiple per month, and may fluctuate with triggers and treatment, but quantitative frequency data are limited due to the small number of reported patients.[11][16]

Quality of life impact from recurrent angioedema is substantial. Patients often experience anxiety related to unpredictable attacks, social embarrassment due to facial swelling, functional impairment from extremity edema, and fear of suffocation in laryngeal episodes, similar to other forms of hereditary angioedema.[11][14][16] These effects would map onto generic QOL instruments such as the SF‑36 domains of physical functioning, role limitations and emotional well-being, and disease-specific tools used in hereditary angioedema research, though formal QOL studies in CPND have not yet been published.

### 3.2 Urticaria and Skin Rash

An important and somewhat distinctive feature of CPND compared with classical bradykinin-mediated angioedema is the frequent occurrence of **urticaria**, or urticarial rash, temporally associated with angioedema episodes.[1][9][14][16] OMIM and Malacards both list acute or chronic urticaria among the characteristic features of CPND, and Malacards notes that urticarial lesions accompanied nearly 60% of symptomatic angioedema episodes in CPN-deficient patients.[1][9][16] The corrigendum summarizing the HAE‑CPN experience states that urticarial lesions developed frequently, though not consistently, in association with angioedema attacks and that an urticarial rash accompanied approximately 60% of symptomatic episodes.[16] This pattern is captured by HPO terms such as *Urticaria* (HP:0011121) and *Chronic spontaneous urticaria*, though the latter is more a clinical descriptor than a specific HPO term.

The presence of urticaria in bradykinin-mediated angioedema challenges the traditional teaching that urticaria is absent in hereditary angioedema and that its presence favors histamine-mediated allergic angioedema.[14] The HAE‑CPN correspondence explicitly notes that HAE‑CPN is the first hereditary angioedema endotype in which kinin accumulation depends solely on defective bradykinin and anaphylatoxin catabolism and that angioedema and urticarial manifestations may or may not be concomitant.[14] The authors argue that bradykinin-angioedema cannot be ruled out on the basis of a history of urticaria and that erythema marginatum in HAE can be misdiagnosed as urticaria, delaying correct diagnosis.[14] In their nationwide analysis of hereditary angioedema more broadly, Rasmussen et al. reported that 25% of patients experienced at least one episode of urticaria, underscoring that the boundary between bradykinin-mediated angioedema and urticaria is more permeable than previously assumed.[14]

Clinically, urticarial lesions in CPND appear as erythematous, edematous wheals, often with pitting, rather than classic pruritic papules, and may be induced by physical triggers such as pressure or cold.[14][16] One HAE‑CPN patient had chronic urticaria as a prominent manifestation, influencing daily comfort and social activities.[16] The pathophysiological explanation, discussed in section 6, likely involves synergistic activation of endothelial cells and mast cells by accumulated kinins and anaphylatoxins, leading to both deeper angioedema and more superficial urticarial wheals.[5][11][14][16] From a quality of life perspective, chronic urticaria is known to disrupt sleep, work performance and overall well-being, and its coexistence with recurrent angioedema further compounds disease burden.

### 3.3 Respiratory and Gastrointestinal Involvement

CPND frequently affects the **upper airway and gastrointestinal tract**, reflecting the role of vasoactive peptides in mucosal microcirculation and smooth muscle tone. OMIM’s clinical synopsis lists laryngeal edema as a respiratory manifestation and abdominal angioedema as a gastrointestinal manifestation.[3][9] Malacards similarly catalogs asthma and airway occlusion under “Respiratory – Airways,” laryngeal edema under “Respiratory – Larynx,” and abdominal angioedema under “Abdomen – Gastrointestinal.”[9] The Mathews proband experienced episodes of laryngeal edema, which are particularly dangerous due to the risk of asphyxiation, and abdominal attacks characterized by crampy pain, nausea and vomiting, linked to bowel wall edema.[11] HAE‑CPN families have reported abdominal and laryngeal attacks, often in association with peripheral angioedema and occasionally macroglossia.[10][16]

These features correspond to HPO terms such as *Laryngeal edema* (HP:0001715), *Asthma* (HP:0002099), *Abdominal pain* (HP:0002027) and *Gastrointestinal angioedema*. Onset of respiratory and gastrointestinal manifestations typically parallels that of peripheral angioedema, with attacks occurring episodically and often triggered by stress, hormonal changes or physical stimuli.[11][16] Severity ranges from mild discomfort to life-threatening airway compromise, and progression within an attack is usually subacute, with swelling peaking over several hours and resolving within 1–3 days.[11] 

Asthma and hay fever (ragweed allergy) are reported in some CPND patients, suggesting a broader dysregulation of the immune–allergic axis.[1][9] Elevated IgE levels, noted in Malacards under “Immunology,” indicate atopic predisposition, which may interact with kinin–complement dysregulation to produce more severe or complex respiratory symptoms.[9] The combined impact of asthma and angioedema on pulmonary function can be substantial, affecting exercise capacity, sleep and daily activities, though specific spirometric data in CPND are not available in these sources.[9][10]

### 3.4 Laboratory Abnormalities and Biochemical Phenotypes

The defining laboratory abnormality in CPND is **markedly decreased circulating carboxypeptidase N activity or concentration** in serum or plasma.[1][9][11] OMIM emphasizes low levels of carboxypeptidase N in affected individuals, and Malacards lists “decreased circulating carboxypeptidase N activity” (HPO ID HP:6000560) as a very rare but characteristic laboratory phenotype.[1][9] Mathews et al. measured CPN activity in the proband and family members, showing severely reduced activity in the affected individual and intermediate levels in heterozygous relatives compared with normal controls.[11] These assays typically involve spectrophotometric or fluorometric measurements of peptide cleavage, using bradykinin or synthetic substrates.

Other laboratory features reported in CPND include elevated serum IgE and evidence of atopic sensitization, as noted in OMIM and Malacards.[1][9] Complement levels (C4, C1 inhibitor) are generally normal in HAE‑CPN patients, distinguishing CPND-associated angioedema from classical hereditary angioedema due to C1 inhibitor deficiency.[10][14] In the Vincent study, patients with HAE‑CPN had normal C1 inhibitor antigen and function but reduced CPN activity, supporting the notion that CPND defines a distinct biochemical endotype within the hereditary angioedema spectrum.[10][16] 

From a pathophysiological standpoint, one would expect increased levels of bradykinin and complement anaphylatoxins (particularly C5a) during attacks, as well as enhanced metabolites such as BK-(1–8) when CPN activity is partially preserved, but direct measurements of these peptides in CPND patients are not detailed in the current search results.[11][12][13][15] Experimental mouse models and in vitro studies demonstrate that CPN1 activity is required to inactivate C5a and that CPN1 knockout mice are hypersensitive to lethal histamine-mediated anaphylactic shock due to excessive C5a/C5aR signaling, suggesting that measuring complement activation products could serve as a biomarker in human CPND.[5] However, such translational biomarker work remains to be systematically reported.

### 3.5 Impact on Daily Function and Well-Being

Across the phenotypic spectrum, CPND exerts considerable impact on daily functioning and well-being. Recurrent angioedema episodes affect physical appearance, mobility and occupational performance, particularly when facial swelling or extremity edema occurs unpredictably.[11][16] Laryngeal attacks create fear of suffocation and may necessitate emergency medical interventions, causing psychological distress and possible post-traumatic stress symptoms similar to other forms of HAE.[11][14] Chronic or recurrent urticaria interferes with sleep, concentration and social comfort, particularly when induced by physical stimuli unavoidable in everyday life (pressure, cold, fatigue).[14][16] Asthma and allergic comorbidities further diminish exercise capacity and increase healthcare utilization.

Although disease-specific quality-of-life studies focused on CPND have not been published, evidence from hereditary angioedema more broadly indicates substantial reductions in EQ‑5D and SF‑36 scores, with physical functioning, vitality and mental health domains most affected.[14] In HAE‑CPN families, the prolonged diagnostic delays (e.g., fourteen years in one patient) and misinterpretation of urticarial rashes as purely allergic or histamine-mediated conditions underscore the psychosocial burden of living with a misunderstood and underdiagnosed disease.[16] Appropriate diagnosis, patient education and access to effective acute and prophylactic therapies can significantly improve quality of life, reducing attack frequency and mitigating anxiety about future episodes.[10][14][16]

## 4. Genetic and Molecular Information

### 4.1 The CPN1 Gene and Carboxypeptidase N Protein

**CPN1** (carboxypeptidase N subunit 1) is a protein-coding gene located on chromosome 10q24.2, encoding the 50‑kDa catalytic subunit of carboxypeptidase N.[2][5][8] The genomic coordinates for CPN1 on the GRCh38 assembly are 10:100,042,193–100,081,869 on the complement strand, and PCR mapping on somatic cell hybrid DNA panels originally localized the gene to chromosome 10.[2][5] The gene is also known by alternative symbols *CPN* and *SCPN* in some databases.[8] 

Carboxypeptidase N itself is a tetrameric serum α‑globulin comprising two identical catalytic subunits (encoded by CPN1) and two identical regulatory subunits, forming a regulatory B-type zinc metalloprotease that circulates in plasma.[5][8][11] The enzyme belongs to the broader family of carboxypeptidase B-type enzymes and liberates C‑terminal basic amino acids (arginine or lysine) from proteins and peptides such as kinins, complement anaphylatoxins, enkephalin hexapeptides, fibrinopeptides and protamine.[11][15] The enzyme requires zinc for catalytic activity and has been historically referred to as *kininase I* and *anaphylatoxin inactivator* due to its role in inactivating bradykinin and complement fragments.[11][15] 

UniProt and experimental structural studies have shown that the catalytic subunit contains the typical metallocarboxypeptidase active site with conserved residues coordinating the zinc ion and binding the substrate’s C‑terminal carboxylate.[5][15] The missense mutation G178D identified in CPND affects a conserved active-site residue, likely disrupting substrate binding or catalytic efficiency.[4][5][7] In addition to its plasma localization, recent work summarized by Affinage indicates that a mitochondrial and cytosolic pool of CPN1 is activated downstream of electron transport chain damage during cardiac ischemia–reperfusion, where it cleaves the complex I subunit NDUFS7 and the inner-membrane protein mitofilin, thereby impairing oxidative phosphorylation and mitophagy, promoting mitochondrial permeability transition pore opening, and triggering apoptosis.[5] This suggests that CPN1 exerts functions beyond its classic extracellular role in kinin and complement metabolism, with potential implications for cardiac injury and cell death pathways.

### 4.2 Pathogenic Variants and Functional Consequences

The best-characterized pathogenic variants in CPN1 are those described by Cao and Hegele in their 2003 study, which sought to identify the genomic basis of documented carboxypeptidase N deficiency.[4][5] Sequencing of CPN1 in an affected patient revealed two mutations: a frameshift insertion designated 385fsInsG in exon 1 and a missense mutation in exon 3 resulting in a glycine-to-aspartate substitution at position 178 (G178D).[4][5] The frameshift insertion is predicted to produce a truncated, non-functional protein via disruption of the open reading frame and potential nonsense-mediated decay of the mRNA, while the G178D missense variant alters a conserved active-site residue critical for enzymatic function.[4][5]

ClinVar records the NM_001308.3(CPN1):c.533G>A (p.Gly178Asp) variant as pathogenic, with submission by OMIM and classification based on literature only, indicating its strong association with CPND.[7] The variant is catalogued in UniProt (P15169 VAR_042415) and dbSNP (rs61751507), and is described in OMIM variant entry 603103.0002.[7] The literature notes that the G178D variant was found in compound heterozygous state with the frameshift insertion in the affected patient, and both alleles were absent or extremely rare in 128 normal Caucasian controls, supporting their pathogenicity.[4][5] Malacards indicates that homozygous or compound heterozygous CPN1 mutations underlie CPND and that heterozygous carriers may exhibit milder disease manifestations, consistent with autosomal recessive inheritance and gene dosage effects.[9]

From a functional standpoint, CPN1 pathogenic variants are **loss-of-function alleles**, reducing or abolishing catalytic activity of the plasma enzyme.[4][5][11] Experimental data in humans and mice show that loss-of-function coding variants reduce plasma CPN activity and cause carboxypeptidase N deficiency and hereditary angioedema with normal C1 inhibitor, attributed to accumulation of bradykinin and anaphylatoxins.[5][10][14] CPN1 knockout mice exhibit hypersensitivity to lethal histamine-mediated anaphylactic shock that depends on C5a/C5aR signaling rather than C3a/C3aR, emphasizing that CPN1 is required to inactivate C5a and that its deficiency shifts the balance of complement-mediated inflammation toward more severe, C5a-driven responses.[5] 

Allele frequencies of CPN1 pathogenic variants in population databases such as gnomAD are not explicitly given in the current sources, but the reported variants are stated to be absent or extremely rare in control cohorts, reflecting their rarity and consistent with the low prevalence of CPND.[4][5] All known disease-causing variants are germline rather than somatic, in line with the congenital and familial nature of CPND.[4][7][11]

### 4.3 Modifier Genes and Genetic Architecture

Malacards notes that nine genes are associated with carboxypeptidase N deficiency, with CPN1 identified as the “elite gene” and others likely included due to involvement in related angioedema pathways or immune processes.[9] Although specific modifier genes for CPND are not clearly delineated in these sources, one can infer that genes involved in the kallikrein–kinin system (e.g., *F12*, *KNG1*, *KLKB1*), complement components (*C3*, *C5*) and mast cell activation pathways might modify disease severity by influencing upstream production of kinins and anaphylatoxins or downstream responsiveness to these peptides.[5][12][14] 

For example, hereditary angioedema with normal C1 inhibitor has been associated with mutations in *F12* (factor XII), *PLG* (plasminogen), *ANGPT1* (angiopoietin-1) and *KNG1*, among others, which increase bradykinin generation.[14] In CPND, the defect lies in catabolism rather than production, but coexisting variants in kinin-generating genes could exacerbate attack frequency by “pushing” more substrate into an impaired degradative pathway, while variants that reduce complement activation might attenuate anaphylatoxin accumulation and ameliorate symptoms.[5][14] However, such modifier effects remain hypothetical, as specific gene–gene interaction studies in CPND have not yet been reported.

### 4.4 Epigenetic and Structural Genomic Features

The current literature and database entries do not report epigenetic alterations (such as DNA methylation or histone modifications) specific to CPN1 or CPND, nor do they describe large-scale chromosomal abnormalities (aneuploidy, translocations, inversions) associated with the disease.[1][2][4][6][9] CPN1 maps to a stable region of chromosome 10q24.2, and pathogenicity appears to arise from point mutations and small insertions in the coding sequence rather than structural genomic changes.[2][4][5][7]

Epigenomic resources such as ENCODE and Roadmap Epigenomics undoubtedly contain data on CPN1 promoter methylation and histone marks in various tissues, but no disease-specific patterns have been linked to CPND in peer-reviewed studies so far. Likewise, transcriptomic, proteomic, metabolomic and lipidomic profiling specifically targeted at CPND has not been published, reflecting both the rarity of the disease and its relatively recent molecular characterization.[4][5][10][14] As such, the current understanding of CPND’s molecular basis focuses on classical Mendelian coding variants in CPN1, with epigenetic and structural genomic dimensions remaining largely unexplored.

## 5. Environmental and Lifestyle Influences

### 5.1 Physical and Hormonal Triggers

Clinical case series of CPND and HAE‑CPN highlight the importance of physical and hormonal triggers in eliciting angioedema and urticaria attacks in genetically susceptible individuals. In the Denis Vincent study and its corrigendum, patients reported that peripheral and abdominal edema, laryngeal swelling and urticarial lesions were precipitated by mechanical pressure (e.g., tight clothing, leaning on objects), cold exposure (e.g., low ambient temperature), and physical fatigue.[10][16] These triggers align with classical “physical urticarias,” such as pressure-induced and cold urticaria, but in CPND they appear to interact with bradykinin–complement dysregulation to produce deeper angioedema alongside more superficial wheals.[14][16]

Hormonal influences are also evident. One HAE‑CPN patient developed angioedema and urticaria associated with administration of triptorelin, a gonadotropin-releasing hormone agonist, suggesting that exogenous hormone modulation of the reproductive axis can trigger attacks in the context of CPN1 deficiency.[16] In other hereditary angioedema forms, estrogen-containing medications and pregnancy are known to exacerbate attacks, presumably by enhancing factor XII and kallikrein activity and therefore bradykinin generation; similar mechanisms likely apply in CPND, compounding the burden introduced by impaired bradykinin catabolism.[14] 

These observations underscore the need for patients with CPND to be counseled about physical and hormonal triggers and for clinicians to consider alternative contraceptive and endocrine therapies that minimize bradykinin-related risks. They also suggest that CPND shares common trigger profiles with other bradykinin-mediated angioedema disorders, but with added complexity due to its unique defect in peptide degradation.

### 5.2 Pharmacologic Factors: ACE Inhibitors and Related Agents

Angiotensin-converting enzyme inhibitors are central pharmacologic risk factors in bradykinin-mediated angioedema, and their relevance to CPND is reinforced by mechanistic and clinical evidence. In human plasma, Kovanen and Kokkonen demonstrated that ACE is the principal enzyme responsible for bradykinin inactivation at low substrate concentrations, converting BK to BK-(1–7) and then to BK-(1–5), whereas carboxypeptidase N-like activity dominates bradykinin degradation at high concentrations, producing BK-(1–8).[12][13] ACE inhibition therefore leads to increased bradykinin by blocking its main catabolic route under physiologic conditions, while CPN deficiency compromises the alternative route operative at higher substrate levels.[12][13] The combination of ACEi exposure and CPN1 deficiency can thus be expected to substantially increase bradykinin accumulation, with high risk of angioedema.

The HAE‑CPN correspondence explicitly highlights that lack of kinin catabolism likely accumulates ligands on receptors in ACEi angioedema, and notes that rash, including urticaria, is not uncommon in a consistent number of patients with angioedema due to ACEi or angiotensin II receptor-blocking agents, refuting the dogma that urticaria excludes ACEi-related angioedema.[14] This suggests that patients with CPND are particularly vulnerable to ACEi-induced attacks and that ACE inhibitors should generally be avoided in this population. Similarly, other drugs that increase bradykinin, such as neprilysin inhibitors, might pose heightened risk, although direct data in CPND are not yet available.

Medications that modulate fibrinolysis and leukotriene pathways, such as tranexamic acid and montelukast, have been used prophylactically in HAE‑CPN patients, and appear to reduce attack frequency.[10][16] Tranexamic acid inhibits plasmin formation and can decrease activation of the contact system, thereby reducing bradykinin generation, while montelukast reduces leukotriene-mediated inflammation, potentially dampening mast cell activation.[10][16] These agents might be considered protective environmental modifiers when used judiciously, although their precise impact on disease course in CPND remains to be quantified in controlled studies.

### 5.3 Infectious and Inflammatory Contexts

Although the current sources do not detail specific infectious agents or inflammatory diseases as triggers for CPND attacks, it is reasonable to infer that infections, particularly those that activate complement or induce tissue injury, could exacerbate symptoms in individuals with CPN1 deficiency. Complement activation generates C3a and C5a, both substrates of CPN1, and in the absence of adequate CPN activity, these anaphylatoxins may persist at high levels, promoting leukocyte recruitment, mast cell degranulation and vascular permeability.[5][11][15] 

Similarly, systemic inflammatory states that stimulate the kallikrein–kinin system could increase bradykinin production. In CPND, the inability to effectively degrade bradykinin would manifest as prolonged and more severe attacks of angioedema. Experimental evidence from CPN1 knockout mice, which are hypersensitive to lethal anaphylactic shock dependent on C5a/C5aR signaling, supports the idea that inflammatory stimuli are particularly dangerous in the absence of CPN1.[5] However, specific human data linking particular infections (e.g., upper respiratory tract infections) or inflammatory conditions (e.g., autoimmune disease) to CPND attack frequency are not yet reported.

### 5.4 Lifestyle Factors and Behavioral Modifiers

Direct evidence linking lifestyle factors such as diet, smoking, alcohol consumption or exercise to CPND severity is lacking in the present literature. Nevertheless, general principles from hereditary angioedema management suggest that avoiding strenuous activity that leads to fatigue, minimizing prolonged standing or pressure (e.g., tight belts, heavy backpacks), and maintaining good control of comorbid asthma and allergies may reduce attack frequency and improve quality of life.[14][16] In the HAE‑CPN families, cold exposure and physical fatigue were reported triggers, implying that patient education on appropriate clothing, environmental temperature management and pacing of physical exertion could be beneficial.[16] 

Dietary factors that influence systemic inflammation or vascular reactivity have not been specifically studied in CPND, but caution regarding alcohol intake (which can dilate blood vessels and trigger flushing) and recognition of food allergens in atopic individuals are reasonable, given the interplay between allergy and bradykinin pathways.[9][14] Smoking, by inducing chronic airway inflammation, could exacerbate asthma in CPND patients and potentially increase vulnerability to respiratory angioedema, though direct data are not available.

In summary, environmental and lifestyle influences in CPND largely mirror those in other bradykinin-mediated angioedema disorders, with physical trauma, cold, fatigue, hormonal therapies and certain drugs acting as key risk factors, and avoidance of these triggers representing a pragmatic preventive approach in the absence of more detailed evidence.

## 6. Mechanisms and Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Manifestation

The mechanistic sequence linking CPN1 mutations to CPND clinical features can be summarized as follows, with each step representing a causally connected event:

| Step | Mechanistic event |
|------|-------------------|
| 1 | Germline loss-of-function variants in **CPN1** (frameshift and missense mutations) lead to reduced or absent expression and catalytic activity of the carboxypeptidase N catalytic subunit in plasma.[1][2][4][5][7][11] |
| 2 | Deficient CPN1 activity results in impaired cleavage of C-terminal arginine and lysine residues from bradykinin, kallidin, complement anaphylatoxins C3a, C4a and C5a, and fibrinopeptides, causing prolonged half-life and increased bioavailability of these vasoactive peptides in the circulation and interstitial spaces.[1][5][11][12][13][15] |
| 3 | Accumulation of bradykinin and related kinins enhances activation of bradykinin B2 receptors on endothelial cells and smooth muscle, leading to increased nitric oxide and prostacyclin production, endothelial cell contraction and widening of intercellular junctions, which collectively increase vascular permeability and cause local plasma extravasation (angioedema).[11][12][13][14] |
| 4 | Accumulation of complement anaphylatoxins, particularly C5a, leads to sustained activation of C5a receptors on mast cells, basophils, neutrophils and endothelial cells, promoting histamine release, leukocyte chemotaxis and additional increases in microvascular permeability, which synergize with bradykinin effects.[5][11][14][15] |
| 5 | The combined and prolonged action of kinins and anaphylatoxins on endothelial and mast cell receptors results in episodic angioedema of subcutaneous and submucosal tissues and, in many patients, urticarial wheals in the superficial dermis, especially when triggers such as pressure, cold or hormonal changes further increase kinin or complement generation.[9][10][14][16] |
| 6 | In the context of ACE inhibition or other conditions that reduce alternative bradykinin-degrading pathways, the impact of CPN1 deficiency is magnified, as both major catabolic routes for bradykinin are compromised, leading to more severe or frequent attacks of bradykinin-mediated angioedema.[12][13][14] |
| 7 | In specific tissues, such as the heart, mitochondrial and cytosolic pools of CPN1 may be activated in response to electron transport chain damage, and their aberrant activity (or lack thereof) can influence mitochondrial integrity, oxidative phosphorylation and apoptosis; however, the direct role of mitochondrial CPN1 in systemic CPND phenotypes remains inferred rather than fully demonstrated.[5] |
| 8 | Over time, recurrent episodes of angioedema and urticaria, combined with the psychological impact of an unpredictable, underdiagnosed disease, lead to chronic morbidity, reduced quality of life and, in severe cases, life-threatening complications such as airway obstruction during laryngeal edema.[11][14][16] |

This chain integrates upstream molecular defects (CPN1 mutations) with downstream clinical manifestations (angioedema and urticaria) through intermediate biochemical and cellular events, as detailed in the subsections below.

### 6.2 CPN1 in Kinin Metabolism and Bradykinin Pathways

Bradykinin is a nonapeptide (Arg–Pro–Pro–Gly–Phe–Ser–Pro–Phe–Arg) generated by the kallikrein–kinin system and is a potent vasoactive mediator that increases vascular permeability, dilates blood vessels and can induce pain.[12][13][15] In human plasma, bradykinin is normally rapidly inactivated by enzymatic cleavage at the C‑terminus and within the peptide chain. Kovanen and Kokkonen demonstrated that carboxypeptidase N (CPN), designated EC 3.4.17.3 and historically known as kininase I, degrades bradykinin to BK-(1–8) by removing the C-terminal arginine, whereas angiotensin-converting enzyme (ACE; kininase II) and neutral endopeptidase (NEP) degrade bradykinin to BK-(1–7) by cleaving internal peptide bonds.[12][13][15] ACE further converts BK-(1–7) to BK-(1–5), leading to accumulation of this active metabolite.[12][13]

The relative importance of these pathways depends on bradykinin concentration. At high micromolar bradykinin concentrations, CPN-like activity accounts for more than 90% of bradykinin degradation, making CPN the major enzyme under these conditions.[12][13] In striking contrast, at low nanomolar bradykinin concentrations, which approximate physiological levels, ACE-mediated conversion to BK-(1–7) and BK-(1–5) accounts for more than 90% of bradykinin inactivation, with CPN playing only a minor role.[12][13] The present study concluded that “the most critical step in plasma kinin metabolism, i.e., inactivation of BK, is mediated by ACE,” and suggested that ACE inhibition elevates circulating bradykinin and could be cardioprotective.[12][13] 

In CPND, loss-of-function mutations in CPN1 reduce or abolish CPN activity, particularly affecting bradykinin degradation at high local concentrations, such as those occurring near sites of injury, inflammation or high kallikrein activity.[4][5][11][15] Without CPN, bradykinin’s C‑terminal arginine is not removed, and the peptide persists longer, continuing to activate B2 receptors on endothelial cells and smooth muscle. This leads to prolonged episodes of increased vascular permeability and edema, particularly in tissues where bradykinin production is intense or where ACE activity is limited.[11][12][13] In the presence of ACE inhibitors, which block the major bradykinin-degrading pathway at physiologic concentrations, CPN1 deficiency becomes particularly consequential, as the alternative pathway is also compromised.[12][13][14]

From a Gene Ontology perspective, CPN1 participates in biological processes such as *kinin catabolic process*, *regulation of humoral immune response*, *negative regulation of inflammatory response* and *regulation of vascular permeability*, and its deficiency represents a failure of these processes. Endothelial cells (CL:0000115) and smooth muscle cells (CL:0000192) are key cellular targets of bradykinin; upon activation of bradykinin B2 receptors, they produce nitric oxide and prostacyclin, causing vasodilation and increased permeability. In CPND, the lack of kinin catabolism prolongs and amplifies these events.

### 6.3 CPN1 in Complement Anaphylatoxin Metabolism

Carboxypeptidase N also plays a crucial role in the metabolism of complement anaphylatoxins, particularly C3a, C4a and C5a, which are generated during complement activation and act as potent chemoattractants and inflammatory mediators.[1][5][11][15] CPN removes the C‑terminal arginine from these peptides, yielding des-Arg forms (C3a des-Arg, C4a des-Arg, C5a des-Arg) with substantially reduced biological activity.[11][15] Mathews et al. emphasized that CPN inactivates C3a, C4a and C5a, bradykinin, kallidin and fibrinopeptides, highlighting its central role in controlling inflammation and vascular tone.[11] 

Affinage summarizes in vivo evidence showing that CPN1 enzymatic activity is required to inactivate C5a, and that CPN1 knockout mice are hypersensitive to lethal, histamine-mediated anaphylactic shock dependent on C5a/C5aR signaling rather than C3a/C3aR.[5] This indicates that CPN1 deficiency allows C5a to persist and act on C5a receptors (C5aR1) on mast cells, basophils, neutrophils and endothelial cells, promoting histamine release, leukocyte recruitment, and increased vascular permeability.[5] In the human context, CPND is likely to cause similar prolongation of C5a activity during complement activation (e.g., infections, immune complex deposition), thereby enhancing inflammatory responses and contributing to angioedema and urticaria.

The HAE‑CPN correspondence explicitly states that CPND is the first hereditary angioedema endotype in which kinin accumulation depends only on defective bradykinin and anaphylatoxin catabolism, emphasizing the dual role of CPN1 in both kinin and complement pathways.[14] The authors propose that accumulation of kinins and anaphylatoxins in the context of lack of their catabolism develops a synergistic effect on their receptors on endothelial and mast cells, driving combined activation and leading to both angioedema and urticaria.[14] Mast cells (CL:0000097), basophils (CL:0000761) and neutrophils (CL:0000776) thus emerge as key effector cells in CPND pathophysiology, integrating signals from C5a and bradykinin to produce complex vascular and inflammatory responses.

In terms of Gene Ontology, CPN1’s role in complement regulation maps onto *regulation of complement activation*, *negative regulation of inflammatory response*, and *regulation of mast cell activation*. Its deficiency therefore contributes to *abnormal complement activation* and *increased mast cell activation*, which manifest clinically as urticaria and angioedema.

### 6.4 Endothelial and Mast Cell Activation: From Molecules to Tissue Edema

The convergence of bradykinin and anaphylatoxin accumulation on endothelial and mast cell targets provides a coherent pathophysiological explanation for the coexistence of angioedema and urticaria in CPND. Bradykinin B2 receptors (BDKRB2) are expressed on endothelial cells and some immune cells; their activation leads to intracellular signaling cascades involving phospholipase C, protein kinase C, and nitric oxide synthase, resulting in increased intracellular calcium, nitric oxide production, and changes in cytoskeletal dynamics.[11][12][13] These changes cause endothelial cells to retract from each other, widening intercellular junctions and allowing plasma and proteins to leak into the interstitial space, forming edema.[11][12][13] In the skin and mucosa, this process manifests as deep, non-pitting angioedema in the subcutaneous and submucosal layers.

Complement anaphylatoxins, particularly C5a, bind to G protein-coupled receptors (C5aR1) on mast cells and basophils, triggering degranulation and release of histamine, leukotrienes, prostaglandins and cytokines.[5][11][15] Histamine and leukotrienes further increase vascular permeability and cause superficial dermal edema, generating urticarial wheals. C5a also acts on endothelial cells to upregulate adhesion molecules and induce contraction, reinforcing bradykinin’s effects on microvascular permeability.[5][11][15] 

In CPND, the persistence of bradykinin and C5a due to defective CPN1-mediated catabolism leads to prolonged and intensified activation of these receptors, amplifying microvascular leakage and inflammatory responses. The HAE‑CPN correspondence emphasizes that accumulation of both kinins and anaphylatoxins in the context of impaired catabolism synergistically activates endothelial and mast cells, producing combined angioedema and urticaria.[14] This synergy explains why HAE‑CPN patients frequently exhibit urticarial lesions alongside typical bradykinin-mediated angioedema, contrary to the classical dichotomy between histamine-mediated urticaria and bradykinin-mediated angioedema.[14][16]

Cell types involved in this process include microvascular endothelial cells (CL:0000115), dermal mast cells (CL:0000097), basophils (CL:0000761), neutrophils (CL:0000776) and, in airway manifestations, bronchial smooth muscle cells (CL:0000192). Biological processes encompass *positive regulation of vascular permeability*, *mast cell degranulation*, *histamine secretion*, *kinin signaling* and *complement-mediated inflammation*. The net effect is episodic tissue edema in the skin, airway and gastrointestinal tract.

### 6.5 Mitochondrial CPN1 and Cardiac Ischemia-Reperfusion Injury

Beyond its classical extracellular role, recent studies have uncovered a mitochondrial and cytosolic pool of CPN1 that is activated downstream of electron transport chain damage during cardiac ischemia–reperfusion.[5] Affinage summarizes that this intracellular CPN1 cleaves the complex I subunit NDUFS7 and the inner-membrane protein mitofilin, impairing oxidative phosphorylation and mitophagy, promoting mitochondrial permeability transition pore opening, and triggering apoptosis.[5] These findings suggest that CPN1 is involved in mitochondrial quality control and cell death pathways in cardiomyocytes, and that dysregulation of CPN1 could contribute to cardiac injury independent of its plasma function.

In the context of CPND, which is defined by deficiency of plasma CPN activity, the status of mitochondrial CPN1 is less clear. If the same loss-of-function mutations affecting plasma CPN1 also impair mitochondrial targeting or function, one might expect increased susceptibility to cardiac ischemia–reperfusion injury and altered mitochondrial dynamics in affected individuals. Conversely, if intracellular CPN1 is regulated differently or partially preserved, systemic CPND may not directly translate into mitochondrial dysfunction. At present, this connection remains largely inferred, as no clinical studies have specifically assessed cardiac mitochondrial function in CPND patients.[5]

Nevertheless, the existence of mitochondrial CPN1 invites an expanded mechanistic framework in which CPN1 participates not only in extracellular regulation of kinins and complement but also in intracellular regulation of mitochondrial integrity and apoptosis. Gene Ontology terms relevant to this role include *mitochondrial protein catabolic process*, *regulation of mitochondrial membrane permeability* and *regulation of apoptosis*. If future studies confirm that CPN1 deficiency affects these processes, the disease spectrum of CPND may broaden beyond angioedema to include subtle cardiac or metabolic phenotypes.

### 6.6 Integration with Hereditary Angioedema Pathophysiology

Hereditary angioedema is a heterogeneous group of disorders characterized by recurrent episodes of bradykinin-mediated angioedema. Classical forms are due to quantitative or functional deficiency of C1 inhibitor (SERPING1) and involve uncontrolled activation of the complement and contact systems, leading to excessive bradykinin generation.[14] More recently, several forms of hereditary angioedema with normal C1 inhibitor (HAE‑nC1‑INH) have been described, including those caused by mutations in *F12*, *PLG*, *ANGPT1*, *KNG1* and now *CPN1*.[10][14] These disorders share the common pathway of increased bradykinin activity but differ in the upstream molecular lesions.

HAE‑CPN represents a unique endotype among HAE‑nC1‑INH forms because it is the first in which kinin accumulation depends solely on defective bradykinin and anaphylatoxin catabolism rather than on increased production.[10][14] In HAE‑F12 and related forms, mutations increase factor XII activity or alter interactions in the contact system, boosting bradykinin generation. In CPND, bradykinin generation may be normal, but its degradation is impaired, leading to accumulation of bradykinin and complement fragments.[4][5][10][14] This distinction has important therapeutic and diagnostic implications, as strategies targeting upstream generation (e.g., C1 inhibitor replacement) may be less effective in HAE‑CPN compared with agents targeting bradykinin receptors (e.g., icatibant) or enhancing catabolism.

The recognition of HAE‑CPN has broken conventional paradigms that equated urticaria with histamine-mediated angioedema and excluded bradykinin-mediated disease in the presence of rash.[14] It has prompted a re-evaluation of clinical criteria for HAE, emphasizing that urticaria and erythema marginatum may co-exist with bradykinin-driven angioedema and that diagnosis should incorporate biochemical and genetic testing rather than rely solely on rash characteristics.[14][16] CPND thus enriches the pathophysiological landscape of hereditary angioedema and underscores the importance of peptide catabolism in vascular homeostasis.

## 7. Anatomical Structures and Biological Context

### 7.1 Organ-Level Involvement

Carboxypeptidase N deficiency affects multiple organ systems due to the systemic distribution of bradykinin, complement anaphylatoxins and plasma CPN. The **skin and subcutaneous tissues** are primary sites of involvement, manifesting as facial swelling, swelling of the hands and feet, and generalized peripheral angioedema.[3][9][11][16] These tissues correspond to UBERON terms such as *skin of face* (UBERON:0001456), *skin of upper limb* (UBERON:0002190) and *skin of lower limb* (UBERON:0002191). The **head and neck region** is particularly vulnerable, with swelling of the lips, tongue and face, and laryngeal edema, mapped to structures such as *tongue* (UBERON:0001723), *lip* (UBERON:0001830) and *larynx* (UBERON:0001737).[3][9][11]

The **respiratory system** is involved through asthma, airway occlusion and laryngeal edema.[1][9][11] Asthma affects the *lower respiratory tract* (UBERON:0001558) and involves bronchial smooth muscle, airway epithelium and immune cells, while laryngeal edema threatens the upper airway, potentially leading to suffocation.[9][11] The **gastrointestinal tract** is involved via abdominal angioedema, affecting structures such as the *small intestine* (UBERON:0002108) and *colon* (UBERON:0001155), where edema of the bowel wall causes pain and digestive symptoms.[9][11][16] 

The **immune system** is implicated both functionally and structurally, with elevated IgE, asthma, hay fever and hypersensitivity reactions pointing to involvement of lymphoid organs, mast cells and basophils.[1][9][11] The **cardiovascular system** may be indirectly affected through altered vascular tone and microcirculatory dynamics, although overt cardiovascular phenotypes in CPND have not been systematically reported.[5][11] 

The distribution of angioedema in CPND is typically bilateral and symmetric, particularly in the extremities and face, but can be localized depending on triggers (e.g., pressure on one limb or localized trauma). Laryngeal and gastrointestinal involvement reflect systemic circulation of kinins and anaphylatoxins, with episodes often involving multiple organ systems concurrently.

### 7.2 Tissue and Cell Types

At the tissue level, CPND predominantly affects **connective tissue** and **mucosal tissues** in regions rich in microvasculature. The deep dermis and subcutaneous tissue of the skin, submucosa of the gastrointestinal tract and mucosa of the upper airway are key sites where increased vascular permeability translates into clinically recognizable swelling.[3][9][11] These tissues contain microvascular endothelial cells, perivascular mast cells, and resident immune cells that respond to bradykinin and anaphylatoxins.

Cell types critical to CPND pathophysiology include:

- **Endothelial cells** (CL:0000115), which line blood vessels and regulate permeability. They respond to bradykinin and C5a by altering cytoskeletal organization and junctional proteins, leading to enhanced leakage of plasma into interstitial spaces.[11][12][13] 

- **Mast cells** (CL:0000097), located in the dermis and mucosa, which degranulate in response to C5a and other stimuli, releasing histamine, leukotrienes and cytokines that further increase vascular permeability and produce urticarial wheals.[5][11][14][15] 

- **Basophils** (CL:0000761) and **neutrophils** (CL:0000776), which respond to C5a by migrating to sites of complement activation and releasing inflammatory mediators.[5][11][15] 

- **Smooth muscle cells** (CL:0000192) in the bronchial and vascular walls, which respond to bradykinin with contraction or relaxation, contributing to asthma symptoms and vasodilation.[1][9][12][13] 

- **Cardiomyocytes** (CL:0000746) and other cells harboring mitochondrial CPN1, which may be affected in settings of ischemia–reperfusion injury, although their direct involvement in CPND clinical phenotypes is not yet demonstrated.[5]

These cellular interactions occur within the microenvironment of tissues such as the skin, airway, gut and heart, and are modulated by systemic factors like ACE activity, complement activation and hormonal milieu.

### 7.3 Subcellular Localization and Components

At the subcellular level, CPN1 is predominantly localized to the **extracellular space and plasma**, associated with the serum α‑globulin fraction, where it interacts with circulating peptides.[1][5][11][15] This corresponds to the Gene Ontology cellular component term *extracellular region* (GO:0005576) and *blood microparticle* in the context of plasma proteins. The catalytic subunit of CPN1 contains a signal peptide and domains that target it for secretion and assembly into the tetrameric complex.

The recently described mitochondrial and cytosolic pools of CPN1 add complexity to its subcellular localization. In cardiomyocytes, CPN1 has been found in the **mitochondrial inner membrane** and **cytosol**, where it cleaves mitochondrial proteins such as NDUFS7 and mitofilin.[5] These locations correspond to GO cellular component terms such as *mitochondrion* (GO:0005739), *mitochondrial inner membrane* (GO:0005743) and *cytosol* (GO:0005829). The mitochondrial functions of CPN1 relate to regulation of oxidative phosphorylation and apoptosis, while its plasma functions relate to regulation of vascular permeability and inflammatory responses.

Complement anaphylatoxins and bradykinin interact with receptors on the **plasma membrane** of endothelial cells, mast cells and other effector cells, triggering intracellular signaling cascades in compartments such as the cytosol and nucleus. These processes involve signaling pathways (e.g., GPCR signaling, calcium mobilization) that ultimately impact cytoskeletal elements and junctional complexes, such as VE‑cadherin and tight junction proteins, leading to increased vascular permeability.

In summary, the anatomical and biological context of CPND spans from the molecular level (plasma and mitochondrial CPN1) to the cellular level (endothelial and mast cells) and organ systems (skin, airway, gut), forming an integrated axis of peptide catabolism and vascular regulation.

## 8. Temporal Development and Disease Course

### 8.1 Age of Onset and Onset Pattern

Available clinical data indicate that carboxypeptidase N deficiency typically presents in **adulthood**, although adolescence onset has also been reported. In the Mathews familial case, the proband was a 65‑year‑old man with an 11‑year history of episodic angioedema, suggesting onset around age 54.[11] HAE‑CPN families described by Vincent et al. reported onset ages ranging from 18 to 41 years, with one male patient developing symptoms at 18 and one female at 41.[16] These observations place CPND in the category of *adult-onset* Mendelian disorders, with variable age at first attack depending on genetic, environmental and hormonal factors.

The onset pattern of CPND symptoms is **episodic and acute**, with attacks characterized by relatively sudden onset of swelling over hours, reaching a peak and then resolving over several days.[11][16] Unlike chronic inflammatory diseases, CPND does not typically cause continuous symptoms but rather discrete episodes of angioedema and urticaria that recur over time. In some patients, the disease may remain quiescent for months or years between attacks, while in others it may manifest more frequently.

### 8.2 Progression, Disease Course and Duration

The disease course of CPND is best described as **relapsing-remitting**, with repeated episodes of angioedema and urticaria over years, but without progressive structural organ damage or permanent disfigurement in most documented cases.[11][16] The Mathews proband experienced ~40 episodes over 11 years, indicating significant morbidity but not necessarily progressive worsening over time.[11] HAE‑CPN patients showed variable attack frequency and severity, with some requiring prophylactic therapy to reduce episodes.[10][16]

Within individual attacks, progression is subacute, with symptoms developing over hours and resolving spontaneously within 1–3 days, although severe laryngeal edema may necessitate emergency intervention.[11][16] The disease is **chronic lifelong**, as the underlying genetic defect persists and the risk of future attacks remains, even if prophylactic therapy reduces their frequency. There is no evidence of distinct “stages” of CPND akin to cancer staging; instead, disease course is measured by attack frequency, severity and impact on quality of life.

### 8.3 Remission Patterns and Critical Periods

Remission in CPND is characterized by intervals free of angioedema and urticaria, whose duration depends on trigger exposure and prophylactic management. Some patients may experience spontaneous remissions, with long attack-free periods, while others may have frequent episodes despite therapy.[11][16] Treatment with tranexamic acid and trigger avoidance has been reported to reduce attack frequency, suggesting that both treatment-induced and spontaneous remissions occur.[10][16]

Critical periods for disease expression include phases of hormonal change (puberty, pregnancy, menopause, initiation of hormonal therapies) and exposure to ACE inhibitors or other bradykinin-modulating drugs.[12][13][14][16] These periods represent windows of heightened vulnerability during which the risk of severe attacks may increase, necessitating careful monitoring and tailored management. Similarly, surgical procedures, trauma and acute infections may serve as critical events that precipitate attacks due to increased kinin and complement activation.

Overall, temporal development of CPND is characterized by adult onset, episodic acute attacks, chronic lifelong risk and variable remission patterns, shaped by genetic susceptibility and environmental triggers.

## 9. Inheritance Patterns and Population Characteristics

### 9.1 Autosomal Recessive Inheritance, Penetrance and Expressivity

Carboxypeptidase N deficiency is inherited in an **autosomal recessive** manner, with homozygous or compound heterozygous mutations in CPN1 causing disease and heterozygous carriers exhibiting partial enzyme deficiency and milder manifestations.[1][4][6][9][11] OMIM and LOVD explicitly state autosomal recessive inheritance, and familial studies confirm segregation of CPN1 loss-of-function alleles with disease.[1][6][11] In the Mathews family, the proband’s markedly low CPN levels contrasted with intermediate levels in heterozygous relatives, and symptoms were more severe in the proband than in carriers, consistent with recessive inheritance and gene dosage effects.[11]

Penetrance in CPND appears to be **high** among individuals with homozygous or compound heterozygous CPN1 mutations, as documented patients exhibit clear clinical manifestations. However, given the small number of reported cases, formal penetrance estimates are not available. Expressivity is **variable**, with some patients experiencing frequent, severe attacks including laryngeal edema and chronic urticaria, while others have milder, infrequent episodes.[9][11][16] Heterozygotes may have minor symptoms or remain clinically silent, further illustrating variable expressivity and partial penetrance in carriers.[9][11]

There is no evidence of genetic anticipation (increasing severity in successive generations) or germline mosaicism in CPND, as the disease arises from classical loss-of-function mutations and is not associated with repeat expansions or dynamic mutations.[1][4][7][11] Founder effects have not been clearly identified, and CPND cases reported to date originate from diverse backgrounds, though comprehensive population studies are lacking.[4][6][9][11]

### 9.2 Epidemiology, Prevalence and Demographics

CPND is an **extremely rare** disorder. LOVD lists only ten individuals reported to have CPN1D (carboxypeptidase N deficiency), and eight phenotype entries associated with this disease, reflecting the scarcity of documented cases.[6] OMIM and Malacards describe the disease as rare, but do not provide precise prevalence or incidence figures, likely due to underdiagnosis and the limited number of published reports.[1][9][11] It is reasonable to categorize CPND as an ultra-rare disease, with prevalence likely well below 1 per 100,000, but accurate epidemiological data are lacking.

Sex ratio among reported CPND patients appears roughly balanced, with both males and females affected in familial series.[11][16] Age distribution reflects adult onset, with most patients presenting in middle age, although adolescent-onset cases also exist.[11][16] Geographic distribution is poorly defined; early reports originated from North America, and recent HAE‑CPN families were described in Europe, suggesting a global distribution but limited recognition.[4][10][11][16] 

Carrier frequency for CPN1 pathogenic variants in the general population is unknown but presumed to be very low, given the rarity of disease and the absence or extreme rarity of reported variants in control cohorts.[4][5] Population databases such as gnomAD likely contain rare CPN1 variants, but specific data have not been integrated into the current literature.

### 9.3 Consanguinity and Family Structure

Given the autosomal recessive inheritance pattern, consanguinity could increase the likelihood of homozygosity for CPN1 pathogenic alleles and therefore elevate CPND risk in certain populations. However, the available case reports do not explicitly mention consanguinity, and documented families include compound heterozygotes as well as presumed heterozygous carriers, suggesting that CPND can arise in non-consanguineous pedigrees through independent inheritance of rare loss-of-function alleles.[4][11][16] 

Family structures in reported CPND cases show vertical transmission of heterozygous alleles and horizontal clustering of affected siblings or cousins, consistent with autosomal recessive disease. Genetic counseling for families with CPND should address the 25% recurrence risk in future pregnancies when both parents are carriers, as well as the possibility of milder manifestations in heterozygous offspring, although precise penetrance in carriers remains to be defined.[1][6][9][11]

## 10. Diagnostics and Clinical Evaluation

### 10.1 Clinical Suspicion and Diagnostic Criteria

Clinicians should suspect carboxypeptidase N deficiency in patients with **recurrent angioedema episodes, with or without urticaria, in the absence of urticarial pruritic papules, and with normal C1 inhibitor levels**, particularly when attacks are not responsive to antihistamines and corticosteroids and may be triggered by physical or hormonal stimuli.[1][9][10][11][14][16] The presence of asthma, hay fever, elevated IgE and other allergic manifestations may coexist but should not preclude consideration of bradykinin-mediated angioedema.[1][9][14] HAE‑CPN has emphasized that urticaria can accompany bradykinin-angioedema and that rash does not rule out CPND.[14][16]

Standardized diagnostic criteria for bradykinin-mediated hereditary angioedema include recurrent angioedema without urticaria, low C4, low C1 inhibitor antigen and/or function (for classical HAE), and family history, but HAE‑CPN modifies these criteria by presenting normal C1 inhibitor and complement levels alongside reduced CPN activity.[10][14] Therefore, HAE‑nC1‑INH patients with reduced CPN activity and CPN1 mutations fulfill criteria for HAE‑CPN.[10][16] Diagnosis of CPND requires integration of clinical features, biochemical evidence of CPN deficiency and molecular confirmation of CPN1 loss-of-function variants.

### 10.2 Laboratory Testing: Carboxypeptidase N Activity and Complement

The **key laboratory test** for CPND is measurement of **serum or plasma carboxypeptidase N activity or concentration**. Mathews et al. demonstrated markedly low CPN activity in the proband and intermediate levels in carriers using enzymatic assays.[11] Malacards lists decreased circulating CPN activity (HP:6000560) as a characteristic laboratory phenotype.[9] These assays typically involve incubating plasma with bradykinin or synthetic substrates and measuring the rate of C‑terminal arginine or lysine cleavage, using chromatographic or spectrophotometric methods.[11][12][13][15]

Complement and C1 inhibitor testing help differentiate CPND from classical HAE. In HAE‑CPN, C1 inhibitor antigen and function are normal, and C4 levels may also be normal, distinguishing it from SERPING1-related HAE in which C1 inhibitor is low and C4 is reduced.[10][14] Complement anaphylatoxin levels (C3a, C5a) could theoretically be elevated in CPND due to impaired catabolism, but routine clinical assays for these peptides are uncommon, and specific data in CPND are not yet reported.[5][11][15] Standard allergy testing (IgE, skin prick tests) may show atopy, but is not diagnostic for CPND.[1][9]

### 10.3 Genetic Testing Strategies

Genetic testing is central for confirming CPND and distinguishing it from other HAE‑nC1‑INH forms. Single-gene sequencing of **CPN1** can identify loss-of-function variants such as frameshift insertions and pathogenic missense mutations (e.g., G178D).[4][5][7] The NCBI Genetic Testing Registry lists tests for CPN1 in the context of hereditary angioedema with normal C1 inhibitor and carboxypeptidase N deficiency, suggesting that targeted sequencing is available in clinical laboratories.[8][10] 

In patients with HAE‑nC1‑INH, gene panels covering *SERPING1*, *F12*, *PLG*, *KNG1*, *ANGPT1*, *CPN1* and other relevant genes can be used to identify the specific endotype.[10][14] Whole exome sequencing (WES) or whole genome sequencing (WGS) may be useful when panel testing is negative or when another rare endotype is suspected, but CPN1 is a small gene and targeted testing is generally efficient.[2][4][5][8] 

ClinVar and LOVD provide variant-level information, including clinical significance and literature support, allowing laboratories to interpret identified variants according to ACMG/AMP guidelines.[6][7] For example, NM_001308.3(CPN1):c.533G>A (p.Gly178Asp) is classified as pathogenic based on the presence in a CPND patient, location in a conserved active site and absence from controls.[4][5][7] Genetic testing in family members can clarify carrier status and assist with reproductive planning.[6][9][11]

Chromosomal microarray, karyotyping, FISH and mitochondrial DNA testing are not generally indicated in CPND, as the disease arises from coding mutations in CPN1 rather than structural abnormalities or mitochondrial genome defects.[2][4][7][8] Repeat expansion testing is likewise unnecessary.

### 10.4 Imaging, Functional Tests and Pathology

Imaging studies are rarely needed specifically for diagnosing CPND, but may be used to evaluate complications of angioedema. CT or ultrasound imaging of the abdomen can show bowel wall edema during abdominal attacks, and laryngoscopy can visualize laryngeal edema during airway involvement.[9][11][16] Functional tests such as pulmonary function tests may be used to assess asthma severity, but they do not diagnose CPND.[1][9]

Biopsy and histopathology are not routinely performed, as angioedema and urticaria are clinical diagnoses and tissue sampling during acute episodes is often impractical. If biopsies are obtained, they would likely show dermal and submucosal edema without significant inflammatory cell infiltration, consistent with bradykinin-mediated edema.[11][14] Immunohistochemistry for complement components or mast cell markers could theoretically demonstrate complement deposition or mast cell activation, but such studies have not been reported in CPND.

### 10.5 Differential Diagnosis

Differential diagnosis for CPND includes:

- **Classical hereditary angioedema (HAE‑C1INH)** due to SERPING1 mutations, characterized by recurrent angioedema without urticaria, low C1 inhibitor and C4 levels. CPND differs by normal C1 inhibitor and complement levels and frequent urticaria.[10][14] 

- **Other HAE‑nC1‑INH endotypes** (HAE‑F12, HAE‑PLG, HAE‑KNG1, HAE‑ANGPT1), which may present similarly but have different genetic bases and may not feature urticaria as prominently.[14] Genetic testing distinguishes these entities.[10][14] 

- **Histamine-mediated allergic angioedema and urticaria**, which respond to antihistamines and corticosteroids and often involve pruritic wheals. In CPND, attacks are often refractory to antihistamines, may lack pruritus and involve deeper angioedema.[11][14][16] 

- **ACE inhibitor-induced angioedema**, which can mimic CPND but is drug-induced and lacks a genetic CPN1 defect. However, ACEi exposure may exacerbate CPND and complicate diagnosis.[12][13][14] 

- **Physical urticarias**, such as pressure or cold urticaria, which can overlap with CPND triggers but usually do not involve deep angioedema unless combined with underlying CPN deficiency.[14][16] 

Distinguishing features include family history, age of onset, presence of urticaria, response to antihistamines, complement and C1 inhibitor levels, CPN activity and genetic testing results.

### 10.6 Screening and Early Detection

Given the rarity of CPND, population-based screening is not currently feasible or recommended. However, **cascade screening** in families with identified CPN1 mutations can detect heterozygous carriers and affected individuals before onset of severe symptoms, allowing early counseling and prophylactic planning.[6][9][11] Carrier screening in the general population is unlikely to be cost-effective due to the extremely low frequency of pathogenic CPN1 variants.[4][5][6]

Newborn screening for CPND has not been implemented, and there are no established biomarker-based screening programs. Nevertheless, in patients with HAE‑nC1‑INH whose genetic etiology remains unknown after initial testing, measurement of CPN activity and targeted sequencing of CPN1 can serve as a focused diagnostic screen.[8][10][14][16]

## 11. Outcomes, Prognosis and Quality of Life

### 11.1 Survival, Mortality and Acute Risk

Direct data on mortality rates and life expectancy in CPND are lacking due to the small number of reported cases. However, extrapolating from other forms of hereditary angioedema, the primary **acute mortality risk** arises from laryngeal angioedema leading to airway obstruction and asphyxiation.[11][14][16] In the Mathews family, episodes of laryngeal edema were described, but no deaths were reported in the published case, suggesting that timely intervention can prevent fatal outcomes.[11] HAE‑CPN patients have experienced laryngeal attacks that required emergency treatment with agents like icatibant or C1 inhibitor concentrate, highlighting the potential for life-threatening episodes but also the efficacy of modern therapies.[10][16]

Overall survival in CPND is likely favorable when the disease is recognized and appropriate management is provided. Life expectancy with treatment should approximate that of the general population, assuming no major comorbidities. However, misdiagnosis or delayed diagnosis can prolong exposure to uncontrolled attack risk, and patients in settings without access to modern bradykinin-targeted therapies may face higher mortality.

### 11.2 Morbidity, Disability and Quality of Life

Morbidity in CPND is substantial due to the **frequency and severity of angioedema and urticaria episodes**. As noted, the Mathews proband experienced ~40 episodes over 11 years, each causing discomfort and functional impairment.[11] HAE‑CPN families reported recurrent peripheral, abdominal and laryngeal attacks, chronic urticaria and significant trigger-related restrictions on daily activities.[10][16] Chronic angioedema and urticaria can disrupt work, school and social life, leading to disability in terms of reduced work capacity, limitations in physical activities and avoidance of social situations due to fear of facial swelling.

Quality of life is further impacted by the psychological burden of an unpredictable disease. The fear of sudden laryngeal edema and asphyxiation, the embarrassment associated with facial and extremity swelling, and the frustration of ineffective antihistamine-based treatments can contribute to anxiety, depression and reduced health-related QOL.[11][14][16] In hereditary angioedema more broadly, studies have documented significant impairments in EQ‑5D and SF‑36 scores, and it is reasonable to infer that CPND patients experience similar burdens, particularly given the added complexity of urticaria and asthma.[14]

Diagnostic delays pose an additional source of morbidity. In HAE‑CPN, one patient had a 14‑year delay between symptom onset and diagnosis, during which attacks were misattributed to chronic urticaria or allergic conditions.[16] Such delays prolong exposure to ineffective therapies and prevent access to bradykinin-targeted treatments, exacerbating morbidity and lowering QOL. Once diagnosed, prophylactic therapies such as tranexamic acid and montelukast, and acute treatments such as icatibant, can substantially improve outcomes and QOL.[10][16]

### 11.3 Prognostic Factors and Biomarkers

Prognostic factors in CPND likely include:

- **Baseline CPN activity**: Patients with extremely low CPN activity may have more frequent or severe attacks than those with partial deficiency, as residual enzyme activity provides some protection.[11][9] 

- **Presence of asthma and atopy**: Coexisting allergic conditions may exacerbate symptoms and complicate management.[1][9][14] 

- **Exposure to ACE inhibitors and triggers**: Continued use of ACEi or frequent exposure to triggers such as pressure, cold and hormonal therapies can increase attack frequency and severity.[12][13][14][16] 

- **Access to effective therapies**: Availability and use of bradykinin-targeted agents and prophylactic medications greatly influence prognosis.[10][14][16] 

Potential prognostic biomarkers include CPN activity levels and CPN1 genotype, which can inform risk stratification and treatment planning. Elevated baseline complement anaphylatoxins or bradykinin levels, if measurable, could also serve as indicators of heightened risk, but such biomarkers remain underexplored in CPND.

## 12. Therapeutic Approaches and Management

### 12.1 Acute Treatment of Angioedema Attacks

Acute management of angioedema attacks in CPND parallels treatment strategies in other bradykinin-mediated hereditary angioedema forms. **Icatibant**, a selective bradykinin B2 receptor antagonist, has been used effectively in HAE‑CPN patients to abort attacks by blocking bradykinin signaling on endothelial cells and smooth muscle.[10][16] In the HAE‑CPN families, icatibant administered on demand led to rapid improvement in peripheral, abdominal and laryngeal edema, demonstrating its efficacy in a setting where bradykinin accumulation is driven by defective catabolism.[10][16] Icatibant corresponds to the NCI Thesaurus term “Icatibant” (NCIT:C80474) and is approved for acute treatment of hereditary angioedema.

**C1 inhibitor concentrate** has also been used on demand in HAE‑CPN patients, particularly when bradykinin generation via the contact system is suspected to be high.[16] Although C1 inhibitor is normal in CPND, exogenous C1 inhibitor can suppress factor XII and kallikrein activity, thereby reducing bradykinin production upstream.[14] Its efficacy in HAE‑CPN suggests that reducing production can compensate partially for impaired catabolism. C1 inhibitor concentrate maps to NCIT term “C1 Esterase Inhibitor” (NCIT:C82474).

Standard antihistamines and corticosteroids, effective in histamine-mediated angioedema and urticaria, are often less effective in CPND because the primary mediator is bradykinin rather than histamine.[11][14] However, given the role of C5a and mast cell activation, antihistamines may provide adjunctive benefit, particularly for urticarial lesions, but they do not address the underlying bradykinin excess. Epinephrine may be used in emergency situations for airway compromise, but its impact on bradykinin pathways is limited.

### 12.2 Prophylactic Therapies

Prophylactic treatment aims to reduce attack frequency and severity by modulating upstream pathways or triggers. In HAE‑CPN families, **tranexamic acid** has been used as a prophylactic agent, with apparent benefit in reducing attack frequency.[10][16] Tranexamic acid is an antifibrinolytic that inhibits plasmin formation and can decrease activation of the contact system, thereby reducing bradykinin generation.[10][14] It maps to NCIT term “Tranexamic Acid” (NCIT:C380). 

**Montelukast**, a leukotriene receptor antagonist, has been employed as prophylaxis in at least one HAE‑CPN patient with chronic urticaria, aiming to dampen leukotriene-mediated inflammation and mast cell activation.[16] Montelukast corresponds to NCIT term “Montelukast” (NCIT:C47484). The combination of tranexamic acid and montelukast, alongside trigger avoidance, proved effective in reducing angioedema and urticarial episodes, though controlled trial data are lacking.[10][16]

Long-term prophylaxis with attenuated androgens such as danazol, used in classical HAE, has not been specifically reported in CPND, but may be considered if other options fail, with attention to side effects. Recent developments in HAE prophylaxis, such as plasma kallikrein inhibitors (e.g., lanadelumab), might theoretically benefit CPND patients by lowering bradykinin production, but direct evidence is not yet available.

### 12.3 Advanced and Experimental Therapeutics

No gene therapy or RNA-based therapies have yet been developed specifically for CPND. Gene replacement or editing strategies targeting CPN1 could theoretically restore normal CPN activity, but the rarity of disease and the complexity of systemic enzyme replacement pose challenges. Similarly, cell therapy approaches (e.g., stem cell transplantation) are unlikely to be needed, as the defect lies in a secreted plasma enzyme produced by the liver and other tissues.

Targeted therapies that enhance CPN1 expression or function, or that mimic its activity, could provide novel treatments. For example, recombinant CPN1 or small molecules that increase CPN1 transcription or translation might compensate for partial deficiency. However, such approaches remain speculative. Most current experimental therapies focus on broad bradykinin or complement pathways, such as bradykinin receptor antagonists, kallikrein inhibitors and C5a receptor antagonists, which could be repurposed for CPND.

### 12.4 Treatment Outcomes and Adverse Events

Treatment outcomes in CPND have been favorable when bradykinin-targeted agents are used. Icatibant has produced rapid resolution of angioedema in HAE‑CPN patients, reducing hospitalizations and improving quality of life.[10][16] Tranexamic acid prophylaxis has decreased attack frequency, though its efficacy may vary among individuals.[10][16] Side effects of these medications, such as injection-site reactions (icatibant) and gastrointestinal discomfort or thrombotic risk (tranexamic acid), must be monitored, but serious adverse events appear infrequent in reported cases.

Montelukast’s side effects include neuropsychiatric symptoms in some patients, requiring careful assessment. C1 inhibitor concentrate carries risks of hypersensitivity and thrombosis, particularly at high doses, though it is generally safe when used appropriately.[14][16] Overall, the risk–benefit profile of these treatments is favorable in the context of a potentially life-threatening disease like CPND.

### 12.5 Personalized Medicine and Treatment Algorithms

Personalized medicine approaches in CPND involve tailoring prophylaxis and acute treatment to individual attack patterns, trigger profiles and comorbidities. For example, patients with frequent laryngeal attacks may benefit from prophylactic tranexamic acid and ready access to icatibant, while those with predominant urticaria may need montelukast and antihistamines in addition to bradykinin-targeted therapies.[10][16] Avoidance of ACE inhibitors and careful selection of hormonal therapies are critical components of individualized management.[12][13][14][16]

Treatment algorithms for hereditary angioedema can be adapted to CPND, with diagnostic confirmation via CPN activity and CPN1 sequencing, initial evaluation of attack severity and frequency, selection of prophylactic and acute therapies, and ongoing monitoring of outcomes and side effects.[10][14][16] Incorporation of NCIT clinical-intervention terms such as “Icatibant,” “Tranexamic Acid,” “Montelukast” and “C1 Esterase Inhibitor” can facilitate standardized annotation of interventions in disease knowledge bases.

## 13. Prevention, Counseling and Public Health Aspects

### 13.1 Primary Prevention

Primary prevention of CPND at the population level is challenging due to its rarity and genetic basis. There are no vaccines or widespread preventive measures analogous to infection-related diseases. However, **genetic counseling** and reproductive planning in families with known CPN1 mutations can help prevent occurrence of homozygous or compound heterozygous offspring.[1][6][9][11] Options such as carrier testing in relatives, preimplantation genetic diagnosis (PGD) and prenatal testing may be considered in high-risk families, though their use must be balanced against ethical and practical considerations.

Avoidance of environmental factors that precipitate attacks—such as ACE inhibitors, certain hormonal therapies and extreme physical triggers—can be considered primary preventive measures in individuals known to be at risk or carriers with partial deficiency, potentially reducing disease expression even before overt symptoms manifest.[12][13][14][16]

### 13.2 Secondary Prevention and Early Detection

Secondary prevention focuses on **early detection** of CPND in symptomatic individuals and at-risk family members, enabling timely initiation of appropriate management. Clinicians should consider measuring CPN activity and sequencing CPN1 in patients with recurrent angioedema and urticaria, especially when C1 inhibitor and complement levels are normal and standard allergy treatments fail.[1][9][10][11][14][16] Families with documented CPND should undergo cascade screening to identify affected individuals and carriers.

Diagnostic algorithms for hereditary angioedema now increasingly include evaluation of HAE‑nC1‑INH endotypes, and recognizing HAE‑CPN as a distinct endotype facilitates secondary prevention by targeting biochemical and genetic tests accordingly.[10][14][16] Early diagnosis reduces morbidity, allows prophylactic treatment and mitigating trigger exposure, and improves quality of life.

### 13.3 Tertiary Prevention and Complication Management

Tertiary prevention in CPND involves **preventing complications and reducing disability** in individuals with established disease. This includes:

- Ensuring access to effective acute therapies (icatibant, C1 inhibitor concentrate) and educating patients on early self-administration during laryngeal or abdominal attacks to prevent severe complications.[10][16] 

- Implementing prophylactic regimens (tranexamic acid, montelukast) tailored to attack patterns, to reduce episode frequency and severity.[10][16] 

- Advising on trigger avoidance and lifestyle adaptations (e.g., minimizing pressure, cold exposure, fatigue) to decrease attack risk.[14][16] 

- Providing psychological support and educational resources to address anxiety, depression and coping strategies, thereby improving long-term outcomes.

Public health interventions specific to CPND are limited due to its rarity, but broader educational efforts in the allergy and immunology community about HAE‑CPN and the possibility of bradykinin-mediated angioedema with urticaria can reduce misdiagnosis and improve care.[14][16]

## 14. Other Species, Natural Disease and Comparative Biology

### 14.1 Orthologous Genes and Evolutionary Conservation

Carboxypeptidase N and its catalytic subunit CPN1 are conserved across vertebrates, with orthologous genes in species such as mice and rats. NCBI Gene and comparative genomics resources identify CPN1 orthologs with similar domain structure and catalytic motifs, reflecting evolutionary conservation of kinin and complement regulation.[5] 

The presence of CPN1 orthologs and conserved function in multiple species suggests that mechanisms of peptide catabolism and vascular regulation are shared, providing opportunities to study CPND-related pathways in model organisms and to extrapolate findings to human disease.

### 14.2 Natural Disease in Animals and Veterinary Relevance

To date, there are no reported cases of natural carboxypeptidase N deficiency in companion animals or livestock analogous to human CPND, as documented in OMIA or veterinary case reports.[5] However, angioedema and urticaria are observed in animals, and complement and kinin systems exist in these species, indicating that CPN1 dysfunction could theoretically produce similar phenotypes. Veterinary relevance of CPN1 has been more focused on basic physiology than disease, and only future discoveries will clarify whether CPND-like syndromes occur in animals.

### 14.3 Comparative Pathology and Cross-Species Mechanisms

Comparative pathology highlights similarities in kinin and complement regulation across species. CPN1 knockout mice, as discussed, exhibit hypersensitivity to lethal anaphylactic shock, emphasizing the role of CPN1 in controlling C5a-mediated responses.[5] This model recapitulates aspects of human CPND pathophysiology (anaphylatoxin accumulation and vascular permeability), albeit in a more extreme, acute setting.

Evolutionary conservation of CPN1’s catalytic motifs and substrate specificity suggests that mechanisms discovered in mice, such as mitochondrial CPN1’s role in ischemia–reperfusion injury, may apply to humans and inform understanding of CPND beyond angioedema.[5] Cross-species susceptibility to anaphylactic shock and angioedema in the context of CPN1 deficiency can thus be studied in animal models to refine mechanistic hypotheses and test therapies.

There is no evidence of zoonotic transmission or cross-species infection in CPND, as the disease is genetic and non-infectious.

## 15. Model Organisms and Experimental Systems

### 15.1 CPN1 Knockout Mice

The primary model organism for studying CPN1 function and related pathophysiology is the **CPN1 knockout mouse**. Affinage notes that in vivo, CPN1 enzymatic activity is required to inactivate C5a, and that CPN1 knockout mice are hypersensitive to lethal histamine-mediated anaphylactic shock dependent on C5a/C5aR signaling rather than C3a/C3aR.[5] This phenotype demonstrates that loss of CPN1 leads to prolonged C5a activity, excessive mast cell activation and severe vascular permeability, analogous to the human situation in CPND.

The mouse model reproduces key aspects of human CPND at the mechanistic level: impaired anaphylatoxin catabolism, increased complement-mediated inflammation, and heightened susceptibility to shock. It also provides a platform to test interventions targeting C5a or C5aR, and to study tissue-specific effects of CPN1 deficiency, including cardiac and mitochondrial phenomena. However, the mouse model may not fully capture the chronic, episodic nature of human CPND angioedema, as experimental anaphylactic shock models often involve acute, severe reactions to antigen challenge.

### 15.2 Cardiac Ischemia-Reperfusion Models

Experimental models of cardiac ischemia–reperfusion have been used to study intracellular CPN1 function. As noted, CPN1 in mitochondria and cytosol is activated downstream of electron transport chain damage and cleaves NDUFS7 and mitofilin, affecting oxidative phosphorylation, mitophagy and apoptosis.[5] These models demonstrate CPN1’s role in mitochondrial integrity and cell death pathways in cardiomyocytes, and suggest that modulating CPN1 activity could influence outcomes after myocardial infarction.

Although these models are not specifically designed to study CPND, they inform potential broader consequences of CPN1 deficiency in human disease and provide mechanistic insights that may eventually translate into clinical considerations.

### 15.3 Applications and Limitations of Model Systems

Model organisms and experimental systems are invaluable for dissecting CPN1’s roles in kinin and complement metabolism, vascular permeability and mitochondrial function. They allow controlled manipulation of gene expression, environmental triggers and pharmacologic interventions, and facilitate detailed mechanistic analyses. However, limitations include species differences in immune and vascular systems, differences in attack patterns and disease course, and the experimental focus on acute phenomena rather than chronic, episodic disease.

Mouse models may overemphasize complement-mediated shock relative to bradykinin-mediated angioedema, and mitochondrial CPN1’s role in cardiac injury may not directly correspond to systemic CPND phenotypes. Nonetheless, these models provide a framework for understanding core mechanisms and testing therapies that might be applicable to CPND.

## Conclusion

Carboxypeptidase N deficiency (CPND) is a rare but clinically significant Mendelian disorder of plasma peptide catabolism, defined by biallelic loss-of-function variants in the CPN1 gene and characterized by episodic bradykinin-mediated angioedema, frequent urticaria, asthma and allergic hypersensitivity.[1][2][4][5][9][11] The disease’s pathophysiology centers on impaired degradation of bradykinin and complement anaphylatoxins, leading to their pathological accumulation and synergistic activation of endothelial and mast cell receptors, which in turn increase vascular permeability and generate both deep angioedema and superficial urticarial wheals.[5][11][12][13][14][16] The recognition of HAE‑CPN as a distinct hereditary angioedema endotype, in which kinin accumulation depends solely on defective catabolism rather than increased production, has expanded understanding of bradykinin-mediated diseases and challenged the dogma that urticaria excludes bradykinin-driven angioedema.[10][14][16]

From a genetic standpoint, CPND exemplifies autosomal recessive inheritance with high penetrance in homozygous or compound heterozygous individuals and milder manifestations in heterozygous carriers.[1][4][6][9][11] Pathogenic variants such as the frameshift insertion 385fsInsG and the missense G178D affect key structural and functional elements of the CPN1 catalytic subunit, abolishing or severely reducing enzyme activity.[4][5][7] The disease remains ultra-rare, with only a handful of documented patients worldwide, and epidemiological data are sparse.[6][9][11] Clinical manifestations span multiple organ systems, including skin (facial and limb angioedema, urticaria), respiratory tract (asthma, laryngeal edema), gastrointestinal tract (abdominal angioedema) and immune system (elevated IgE, hay fever).[1][3][9][11][16] Quality of life is substantially affected by recurrent attacks, diagnostic delays and anxiety about airway compromise.[11][14][16]

Diagnosis of CPND integrates clinical suspicion in patients with recurrent angioedema and urticaria, measurement of CPN activity, demonstration of normal C1 inhibitor and complement levels, and targeted sequencing of CPN1.[1][9][10][11][14][16] Differential diagnosis encompasses classical HAE, other HAE‑nC1‑INH endotypes, histamine-mediated allergic angioedema and ACE inhibitor-induced angioedema.[10][14] Treatment follows principles of bradykinin-mediated disease, using icatibant for acute attacks, C1 inhibitor concentrate in selected cases, and prophylactic agents such as tranexamic acid and montelukast.[10][14][16] Avoidance of ACE inhibitors, careful management of physical and hormonal triggers, and genetic counseling for affected families are critical components of prevention and long-term care.[12][13][14][16]

Mechanistic insights from human plasma studies and animal models underscore the dual role of CPN1 in kinin and complement anaphylatoxin metabolism, as well as emerging intracellular functions in mitochondria.[5][11][12][13][15] CPN1 knockout mice highlight the consequences of impaired C5a catabolism, and cardiac ischemia–reperfusion models reveal mitochondrial CPN1’s role in apoptosis.[5] These findings point to broader biological significance of CPN1 and suggest that CPND’s impact may extend beyond visible angioedema to subtler influences on inflammatory and mitochondrial pathways.

Future research directions include systematic characterization of CPND’s epidemiology, natural history and quality-of-life impact; identification of additional CPN1 variants and potential modifier genes; elucidation of mitochondrial CPN1’s role in human disease; and development of targeted therapies that enhance CPN1 function or compensate for its deficiency. Increased awareness among clinicians about HAE‑CPN and the possibility of bradykinin-mediated angioedema with urticaria is essential to reduce diagnostic delays and improve patient outcomes. Integrating CPND into disease knowledge bases with detailed annotations of genes, pathways, phenotypes, cell types, anatomical structures and treatments, as outlined in this report, will facilitate data-driven advances in understanding and managing this intriguing and complex disorder.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 31 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001873` (1 mention) - the report calls it "Angioedema"; HP calls it **Thrombocytopenia**
- `HP:0000293` (1 mention) - the report calls it "Facial swelling"; HP calls it **Full cheeks**
- `HP:0001099` (1 mention) - the report calls it "Swelling of the hands"; HP calls it **Atrophic fundus lesion**
- `HP:0001761` (1 mention) - the report calls it "Swelling of the feet"; HP calls it **Pes cavus**
- `HP:0011121` (1 mention) - the report calls it "Urticaria"; HP calls it **Abnormal skin morphology**
- `CL:0000761` (3 mentions) - the report calls it "Basophils"; CL calls it **type 9 cone bipolar cell (sensu Mus)**
- `UBERON:0002190` (1 mention) - the report calls it "skin of upper limb"; UBERON calls it **subcutaneous adipose tissue**
- `UBERON:0002191` (1 mention) - the report calls it "skin of lower limb"; UBERON calls it **subiculum**
- `UBERON:0001830` (1 mention) - the report calls it "lip"; UBERON calls it **minor salivary gland**
- `NCIT:C80474` (1 mention) - the report calls it "Icatibant"; NCIT calls it **Device Parameters**
- `NCIT:C82474` (1 mention) - the report calls it "C1 Esterase Inhibitor"; NCIT calls it **Egg Laying**
- `NCIT:C380` (1 mention) - the report calls it "Tranexamic Acid"; NCIT calls it **Clonidine**
- `NCIT:C47484` (1 mention) - the report calls it "Montelukast"; NCIT calls it **Dibenzothiophene**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0001715` (1 mention), reported as "Laryngeal edema" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000154` (1 mention) - the report calls it "Macroglossia"; HP calls it **Wide mouth**, and lists "Macrostomia" among its other names
- `CL:0000776` (3 mentions) - the report calls it "neutrophils"; CL calls it **immature neutrophil**
- `UBERON:0001456` (1 mention) - the report calls it "skin of face"; UBERON calls it **face**
- `CL:0000746` (1 mention) - the report calls it "Cardiomyocytes"; CL calls it **cardiac muscle cell**, and lists "cardiomyocyte" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `DO`.