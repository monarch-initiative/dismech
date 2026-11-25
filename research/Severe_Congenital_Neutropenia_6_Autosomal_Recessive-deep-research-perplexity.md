---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-11-24T16:15:37.725869'
end_time: '2026-11-24T16:21:03.069183'
duration_seconds: 325.34
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Severe Congenital Neutropenia 6, Autosomal Recessive
  mondo_id: MONDO:0014456
  category: Mendelian
  causal_genes: JAGN1
  omim_id: OMIM:616022
  synonyms: SCN6; neutropenia, severe congenital, 6, autosomal recessive; JAGN1 deficiency;
    SCN due to JAGN1 deficiency; Severe congenital neutropenia due to jagunal homolog
    1 deficiency; JAGN1-CDG
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 15
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 3
  validator_version: 0.8.0
term_validation:
  total_terms: 65
  verified: 57
  not_found: 0
  obsolete: 2
  unverifiable: 6
  confabulation_rate: 0.0
  labels_checked: 45
  labels_matching: 22
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: HP:0005532
    reported_labels:
    - Severe neutropenia
    ontology_label: Macrocytic dyserythropoietic anemia
  - term_id: HP:0001678
    reported_labels:
    - Bone marrow maturation arrest
    ontology_label: Atrioventricular block
  - term_id: HP:0001919
    reported_labels:
    - Abnormal myelopoiesis
    ontology_label: Acute kidney injury
  - term_id: HP:0002723
    reported_labels:
    - Sepsis
    ontology_label: Absence of bactericidal oxidative respiratory burst in phagocytes
  - term_id: HP:0005411
    reported_labels:
    - Impaired neutrophil chemotaxis
    ontology_label: Chronic intestinal candidiasis
  - term_id: HP:0006520
    reported_labels:
    - Frequent hospitalizations
    ontology_label: Progressive pulmonary function impairment
  - term_id: HP:0000736
    reported_labels:
    - Reduced social interaction
    ontology_label: Short attention span
  - term_id: UBERON:0001741
    reported_labels:
    - bone marrow
    ontology_label: corniculate cartilage
  - term_id: GO:0005544
    reported_labels:
    - calpain-mediated signaling
    ontology_label: calcium-dependent phospholipid binding
  labels_variant: 14
  obsolete_terms:
  - term_id: GO:0006486
    ontology_label: obsolete protein glycosylation
    replaced_by: GO:0009101
  - term_id: NCIT:C2113
    ontology_label: Miscellaneous Chemoprotective Agent
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - ID
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Severe Congenital Neutropenia 6, Autosomal Recessive
- **MONDO ID:** MONDO:0014456 (if available)
- **Causal gene(s):** JAGN1
- **OMIM:** OMIM:616022
- **Synonyms:** SCN6; neutropenia, severe congenital, 6, autosomal recessive; JAGN1 deficiency; SCN due to JAGN1 deficiency; Severe congenital neutropenia due to jagunal homolog 1 deficiency; JAGN1-CDG
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Severe Congenital Neutropenia 6, Autosomal Recessive** covering all of the
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

# Severe Congenital Neutropenia 6, Autosomal Recessive (JAGN1 Deficiency)

Severe congenital neutropenia 6, autosomal recessive (SCN6) is a rare, monogenic primary immunodeficiency caused by biallelic germline mutations in the **JAGN1** gene, which encodes an endoplasmic reticulum–resident transmembrane protein essential for neutrophil differentiation, survival, and secretory pathway function.[4][8][11] Patients present in early infancy with profound, chronic neutropenia, recurrent and often life-threatening bacterial infections, bone marrow maturation arrest at the promyelocyte/myelocyte stage, and a characteristic constellation of extra‑hematologic features including failure to thrive, short stature, skeletal abnormalities, endocrine and pancreatic dysfunction, and variable developmental delay.[3][5][11][15] Mechanistic work has shown that JAGN1 deficiency disrupts early secretory pathway and N‑glycosylation, impairs granulocyte colony-stimulating factor receptor (CSF3R) expression and signaling, and unleashes a calcium- and calpain‑dependent non‑apoptotic cell death program in myeloid cells, thereby coupling an ER-centred cellular stress phenotype to the clinical hallmark of severe neutropenia.[6][7][10][11] Clinically, SCN6 is distinguished from other forms of severe congenital neutropenia by its autosomal recessive inheritance, poor or erratic response to recombinant human G‑CSF, and curability with allogeneic hematopoietic stem cell transplantation (HSCT), with ongoing work exploring its classification as a congenital disorder of glycosylation (JAGN1‑CDG) and refining genotype–phenotype correlations.[3][4][11][14][15]

## 1. Disease Information

### Overview and Core Definition

Severe congenital neutropenia 6, autosomal recessive (SCN6) is a genetically defined subtype of severe congenital neutropenia characterized by early‑onset, persistent, and severe reduction in absolute neutrophil counts (ANC) associated with maturation arrest of granulopoiesis and a markedly increased susceptibility to recurrent, life‑threatening bacterial infections.[5][9][15] MedGen, summarizing OMIM and Orphanet data, defines autosomal recessive severe congenital neutropenia due to JAGN1 deficiency as a rare primary immunodeficiency disorder with early‑onset recurrent severe bacterial infections, granulopoiesis maturation arrest at the promyelocyte/myelocyte stage, and markedly reduced ANC, resulting from recessively inherited mutations in the JAGN1 gene.[5][15] Boztug and colleagues first delineated SCN6 as a distinct clinical and genetic entity in 2014, identifying homozygous JAGN1 mutations in 14 patients from nine families with severe congenital neutropenia and demonstrating aberrant myeloid cell homeostasis as a mechanistic hallmark.[4][11] Clinically, SCN6 fits within the broader category of severe congenital neutropenia (also known as Kostmann disease), which is defined by persistent ANC below approximately \(0.5 \times 10^{9}/\text{L}\) and early, severe bacterial infections, but SCN6 patients display unique features including partial or complete refractoriness to G‑CSF and specific extra‑hematologic manifestations.[6][9][10][11]

From a disease ontology perspective, SCN6 is catalogued in the **Mondo Disease Ontology** as MONDO:0014456, “autosomal recessive severe congenital neutropenia due to JAGN1 deficiency,” aligning with the MedGen concept C4014954.[5][15] OMIM assigns the phenotype entry **OMIM:616022** to “Neutropenia, severe congenital, 6, autosomal recessive,” which is explicitly mapped to the JAGN1 gene at chromosome 3p25.3.[1][4] JAGN1 itself is assigned **OMIM:616012** and is annotated as an endoplasmic reticulum–resident protein functioning in the early secretory pathway and necessary for neutrophil differentiation and survival, with mutations causing SCN6.[4][8][11] Orphanet lists “Severe congenital neutropenia due to JAGN1 deficiency” under ORPHA:423384 as a specific entity within the broader Orphanet category of severe congenital neutropenia (ORPHA:42738).[9][15] These convergent definitions underscore that SCN6 is not merely neutropenia of unknown pathogenesis, but a discrete Mendelian disorder arising from disruption of a conserved ER protein.

### Key Identifiers, Synonyms, and Classification

The disease is known by several overlapping names that must be carefully disambiguated, especially given the large number of genetically distinct SCN subtypes. OMIM uses the formal name **“Neutropenia, severe congenital, 6, autosomal recessive”** with the short form **SCN6**.[1][4] MedGen and Mondo employ the term **“Autosomal recessive severe congenital neutropenia due to JAGN1 deficiency”** and list the synonym “Severe congenital neutropenia 6, autosomal recessive.”[5][15] Clinical and research literature commonly refer to **“severe congenital neutropenia due to JAGN1 deficiency,” “JAGN1-associated SCN,” “SCN6 due to JAGN1,”** or simply **“JAGN1 deficiency”** when the context of neutropenia is clear.[3][6][7][10][11] Because JAGN1 mutations primarily affect neutrophil maturation and survival via secretory pathway and glycosylation defects, some authors have proposed inclusion of the disorder within the expanding group of congenital disorders of glycosylation, using the term **“JAGN1-CDG”** to emphasize the underlying glycosylation abnormality; this terminology is not yet universally codified in major databases but reflects an important mechanistic nuance.[3][11]

Several other identifiers support integration of SCN6 into ontological and clinical coding frameworks. In MedGen, the concept C4014954 is explicitly linked to OMIM:616022 and Orphanet ORPHA:423384.[5][15] NCBI Gene lists JAGN1 as “jagunal vesicle mediated transporter 1” with Gene ID 84522 and cross‑references to OMIM:616012 and HGNC:26926.[8] Severe congenital neutropenia as a category is indexed in Orphanet as ORPHA:42738 and described as a rare primary immunodeficiency without associated lymphocyte deficit, characterized by impaired neutrophil maturation and function, severe infections, and increased risk of leukemic transformation.[9] ICD‑10 and ICD‑11 do not provide subtype‑specific codes for JAGN1‑related neutropenia; clinically, SCN6 is coded under the general neutropenia (e.g., D70) or primary immunodeficiency categories, with genomic information carried separately in genetic and rare disease registries. MeSH currently uses broad headings such as “Neutropenia” and “Immunologic Deficiency Syndromes,” under which SCN6 can be manually indexed in PubMed searches, but lacks a dedicated descriptor for the JAGN1 subtype.

### Source and Nature of Information

Knowledge about SCN6 and JAGN1 deficiency is derived almost entirely from aggregated disease‑level resources and primary literature rather than from large, anonymized EHR‑based cohorts, reflecting its rarity and relatively recent discovery. OMIM, Orphanet, MedGen, and NCBI Gene synthesize information from case series, individual case reports, and mechanistic studies, particularly Boztug et al. 2014 and subsequent experimental work in cell lines.[1][4][5][8][9][11][15] Boztug and colleagues analyzed a cohort of 90 patients with severe congenital neutropenia and identified nine distinct homozygous JAGN1 mutations in 14 patients from 9 families, establishing SCN6 as a novel monogenic variant that accounts for about 10% of SCN cases in that series.[4][7][11] Case reports, such as the detailed description of a 4‑year‑old boy with JAGN1‑associated SCN and recurrent intracranial hemorrhage, further expand the phenotypic spectrum and provide granular clinical timelines.[3] Mechanistic and cell biology data arise from in vitro studies using patient neutrophils, human bone marrow, and the HL‑60 promyelocytic leukemia cell line overexpressing mutant JAGN1; these experiments demonstrate ER stress, altered granule morphology, defective glycosylation, and calpain‑dependent cell death.[6][10][11] 

Because SCN6 is rare, population‑level epidemiologic data (prevalence, incidence, survival curves) are sparse and usually extrapolated from broader SCN registries, where JAGN1‑mutant patients form a small subset.[9][10][11] No large randomized trials or EHR‑derived real‑world evidence datasets exist specifically for JAGN1 deficiency; clinical management recommendations are deduced from SCN guidelines and adapted based on the distinctive mechanistic and therapeutic response profile of SCN6.[9][10] Thus, while disease‑level resources provide structured, curated knowledge, much of the mechanistic and clinical nuance is best accessed through primary literature and interpreted in light of small patient numbers and experimental models.

## 2. Etiology

### Genetic Causal Factors

The primary and defining cause of SCN6 is **biallelic germline mutation in the JAGN1 gene** on chromosome 3p25.3, following an autosomal recessive mode of inheritance.[1][4][5][11][15] JAGN1 encodes an evolutionarily conserved endoplasmic reticulum (ER) membrane protein that functions in the early secretory pathway, with roles in ER organization and vesicular trafficking first described in Drosophila oogenesis.[8][11][13] In their seminal 2014 Nature Genetics study, Boztug et al. used whole‑exome sequencing to identify nine distinct homozygous mutations in JAGN1 in 14 patients from 9 families with severe congenital neutropenia, concluding that “JAGN1 deficiency causes aberrant myeloid cell homeostasis and congenital neutropenia.”[4][11] These variants included truncating mutations, in‑frame deletions, and missense changes affecting highly conserved residues, consistent with a loss‑of‑function mechanism.[4][11][12][14]

Clinically recognized JAGN1 variants have been curated in ClinVar, OMIM, and MedGen. ClinVar, for example, lists the in‑frame deletion c.35_43del (p.Thr12_Gly14del) in NM_032492.4(JAGN1) as associated with autosomal recessive severe congenital neutropenia due to JAGN1 deficiency, noting that this variant has been observed in individuals with neutropenia and was identified by Boztug et al. in a 25‑year‑old woman with SCN6.[12][14] MedGen and OMIM catalogue JAGN1 as the sole gene directly associated with SCN6, with no evidence for locus heterogeneity within this subtype, although severe congenital neutropenia as a broader category involves at least 25 different genes (including ELANE, HAX1, G6PC3, GFI1, VPS45, and others).[4][6][9][10][11] The autosomal recessive pattern means affected individuals are either homozygotes for a single pathogenic allele or compound heterozygotes for two distinct pathogenic alleles, with carriers typically clinically asymptomatic.[5][7][15]

Mechanistically, pathogenic JAGN1 mutations lead to either truncation of the protein, disruption of its N‑terminal signal peptide, mislocalization within the ER, or structural perturbations that impair its role in ER organization, vesicle trafficking, and N‑glycosylation.[4][6][11][13] Boztug et al. showed that JAGN1 is ubiquitously expressed, yet the only consistent phenotype of JAGN1 deficiency in humans is congenital neutropenia, implying a particularly critical role for JAGN1 in myeloid cell homeostasis.[11] Subsequent functional work demonstrated that expression of patient‑derived mutant JAGN1 in HL‑60 cells confers increased sensitivity to pro‑apoptotic stimuli and to agonists of degranulation, leading to calcium‑dependent, calpain‑mediated cell death.[6] This chain of events firmly establishes JAGN1 as the causal gene and its loss of function as the initiating lesion in SCN6.

### Genetic Risk Factors and Susceptibility Loci

Beyond the causal JAGN1 mutations themselves, no additional susceptibility loci or common genetic modifiers have been conclusively linked to SCN6. Given the rarity of the disorder and the autosomal recessive nature of causative variants, classical genome‑wide association studies (GWAS) are not feasible, and no entries for JAGN1‑related neutropenia appear in GWAS Catalog or similar databases. Population databases such as gnomAD indicate that some JAGN1 variants, including c.35_43del (p.Thr12_Gly14del), occur at extremely low frequencies in the general population (approximately 0.002%), reflecting carrier status without disease in heterozygotes.[14] This supports the notion that JAGN1‑mediated SCN6 is a **highly penetrant Mendelian disorder** where the presence of two pathogenic alleles is usually sufficient to cause disease, independent of common polygenic background.

However, genetic heterogeneity within the broader SCN category introduces potential complexities in differential diagnosis and risk stratification. ELANE and HAX1 mutations, for example, cause autosomal dominant and autosomal recessive forms of SCN, respectively, with overlapping but distinct phenotypic profiles.[6][9][10] Some pathways implicated in other SCN genes, such as intrinsic apoptosis or mitochondrial dysfunction, may intersect with ER stress and calcium signaling pathways modulated by JAGN1, raising the possibility of shared downstream mechanisms even in genetically distinct forms.[6][10][11] At present, though, no modifier genes have been systematically identified that alter the penetrance, age of onset, or severity of JAGN1‑mediated SCN6 in human cohorts.

### Environmental, Demographic, and Family History Risk Factors

In contrast to many complex diseases, environmental risk factors do not cause SCN6; rather, they shape the clinical course and burden of infections once the genetic lesion in JAGN1 is present. The crucial etiologic determinant is the **germline JAGN1 mutation**, and environmental influences such as pathogen exposure, vaccination status, household crowding, and access to antimicrobial therapy function as modifiers of disease expression. Patients with SCN6 often present in settings of high infectious burden and limited early access to tertiary care, which may exacerbate morbidity and mortality, but the underlying neutropenia and maturation arrest are present irrespective of environment.[3][9][11][15]

Family history is highly relevant as a risk factor in the sense of recurrence risk and carrier status, because SCN6 follows an autosomal recessive inheritance pattern and is frequently observed in families with consanguinity.[4][7][11][15] Boztug et al. reported that many of the families with JAGN1 mutations were consanguineous, consistent with enrichment of rare recessive variants in such populations.[4][11] Thus, children born to consanguineous parents or to parents from populations with known founder mutations in JAGN1 may have an elevated risk of SCN6 if both parents carry a pathogenic allele. Sex does not appear to be a significant risk factor; reported patients include both males and females, and there is no evidence of sex-linked inheritance or sexual dimorphism in penetrance.[3][4][7][11]

### Protective Factors and Gene–Environment Interactions

Because SCN6 is a monogenic, highly penetrant disorder, true genetic protective factors in the sense of common alleles that prevent disease have not been identified. Heterozygous carriers of JAGN1 pathogenic variants are typically asymptomatic, supporting a recessive threshold for disease manifestation, but this carrier status is better understood as absence of disease rather than protective modification. It remains theoretically possible that rare alleles in genes involved in ER stress responses, calpain regulation, or CSF3R trafficking could confer mild protection by buffering JAGN1 loss, yet such interactions have not been demonstrated in human cohorts.

Environmental and clinical interventions can exert **protective effects on disease course** even though they do not modify the underlying genetic etiologic lesion. Early institution of recombinant human G‑CSF therapy has dramatically reduced infection‑related mortality in SCN overall, providing a clear example of treatment‑induced protection.[9][10] In JAGN1 deficiency, patients often show partial or poor response to G‑CSF, yet some benefit may still be achieved; Boztug et al. report that JAGN1‑deficient neutrophils have decreased expression of G‑CSF receptors due to N‑glycosylation defects, explaining refractoriness but not total lack of effect.[4][7][11] Case reports suggest that **granulocyte-macrophage colony-stimulating factor (GM‑CSF)** may improve N‑glycosylation and thereby enhance neutrophil function, introducing a potential pharmacologic protective factor at the cellular level.[3] Rigorous infection prophylaxis, including vaccinations, antibiotic prophylaxis, and avoidance of environmental exposures to high pathogen loads, can likewise reduce the incidence and severity of infections, functioning as secondary protective factors.

Gene–environment interactions in SCN6 primarily involve the interplay between intrinsic neutrophil defect and extrinsic infectious exposure. Mechanistically, when myeloid cells expressing mutant JAGN1 are confronted with stimuli that normally trigger degranulation, such as infection‑induced activation of neutrophil granules, they undergo calcium‑dependent, calpain‑mediated cell death.[6][10] Khandagale et al. showed in HL‑60 cells that mutant JAGN1 dramatically increases susceptibility to such stimuli, implying that infectious triggers interact with the genetic defect to precipitate accelerated loss of neutrophils, thereby exacerbating the neutropenia.[6] Thus, while JAGN1 mutations are the primary etiologic factor, environmental exposures to pathogens act as **downstream amplifiers** of neutrophil depletion and clinical infection burden.

## 3. Phenotypes

### Hematologic and Immunologic Phenotypes

The core phenotype of SCN6 is **severe, chronic neutropenia**, defined by markedly reduced absolute neutrophil counts and impaired maturation of myeloid precursors.[5][6][9][11][15] Severe congenital neutropenia in general is characterized by ANC persistently below \(0.5 \times 10^{9}/\text{L}\), and JAGN1‑deficient patients fall within this range or lower; Khandagale et al. cite ANC values well below the severe threshold in their Kostmann‑like SCN patients with JAGN1 mutations.[6][10] Boztug et al. and subsequent case reports emphasize that neutrophil counts are persistently decreased, often with minimal fluctuations, and that bone marrow examination reveals granulopoiesis maturation arrest at the promyelocyte/myelocyte stage.[4][5][11][15] The Human Phenotype Ontology (HPO) term **“Neutropenia” (HP:0001875)** is thus central, with the more specific “Severe neutropenia” (HP:0005532) appropriate for many cases.

Bone marrow findings in SCN6 show **maturation arrest**, manifested as increased proportions of immature myeloid cells and paucity of mature neutrophils.[4][5][11][15] MedGen explicitly lists “Bone marrow maturation arrest” as a clinical feature associated with autosomal recessive severe congenital neutropenia due to JAGN1 deficiency.[15] Histologically, the marrow may appear hypercellular with accumulation of promyelocytes and myelocytes, reflecting abortive differentiation rather than global aplasia. This phenotype corresponds to HPO term **“Bone marrow maturation arrest” (HP:0001678)** or “Abnormal myelopoiesis” (HP:0001919). Functional studies show increased apoptosis or calpain‑dependent cell death in neutrophil precursors, providing a mechanistic explanation for this arrest.[6][7][11]

Clinically, neutropenia translates into **recurrent, severe bacterial infections** starting in early infancy.[3][5][9][11][15] The Orphanet and MedGen definitions stress “early-onset, recurrent, severe bacterial infections” as cardinal features.[5][9][15] Patients experience recurrent pneumonia, otitis media, sinusitis, skin and soft tissue infections, sepsis, and sometimes intracranial infections or hemorrhage associated with infectious or inflammatory events.[3][7][9][11] HPO terms such as **“Recurrent bacterial infections” (HP:0002719), “Recurrent respiratory infections” (HP:0002205), “Sepsis” (HP:0002723),** and “Recurrent skin infections” (HP:0002718) are commonly applicable. Fungal infections, including aspergillosis, have been reported in some patients, particularly when neutropenia is longstanding and profound, warranting terms like **“Recurrent fungal infections” (HP:0002841)**.[3][7]

Immunologically, SCN6 is primarily an isolated neutrophil defect, with lymphocyte counts often preserved and no systemic lymphopenia.[9][11] Orphanet’s general severe congenital neutropenia entry explicitly notes that SCN is a primary immunodeficiency “without an associated lymphocyte deficit” and that neutrophils are the main affected population.[9] However, clinical features such as recurrent infections and poor inflammatory response can mimic more generalized immunodeficiency states, and specific functional assays (oxidative burst, phagocytosis) may reveal subtle defects in neutrophil function beyond numerical deficiency. HPO terms **“Primary immunodeficiency” (HP:0002721)** and “Impaired neutrophil chemotaxis” (HP:0005411) may be considered in some patients, though not all cases have such detailed functional studies reported.

### Extra‑hematologic Systemic Features

One of the distinctive aspects of JAGN1‑mediated SCN6 is the presence of **extra‑hematologic manifestations** affecting growth, skeletal development, endocrine function, and organs such as pancreas and thyroid.[3][4][7][11][15] MedGen lists short stature, failure to thrive, hypothyroidism, pancreatic insufficiency, coarctation of the aorta, bone abnormalities, urogenital abnormalities, and mild facial dysmorphism (triangular face) as possible associated features.[15] Boztug et al. similarly report failure to thrive, developmental delay, and skeletal abnormalities across their cohort, noting that the only universal feature was neutropenia but that many patients had broader systemic involvement.[4][7][11]

Growth disturbances include **short stature** and **failure to thrive**, with height often more than two standard deviations below the mean for age and gender and weight gain below expected percentiles.[15] HPO terms **“Short stature” (HP:0004322)** and **“Failure to thrive” (HP:0001508)** are appropriate. Facial dysmorphism, particularly a triangular face, has been noted, aligning with **“Triangular face” (HP:0000325)**.[7][15] Developmental delay, including motor and cognitive delays, is present in some patients, prompting use of **“Global developmental delay” (HP:0001263)** or specific subterms depending on detailed neurodevelopmental assessment.[3][7][11][15]

Skeletal abnormalities constitute a noteworthy component of the phenotype. Case reports describe severe osteoporosis and repeated bone fractures, especially in older patients with longstanding disease and G‑CSF exposure.[3][7] HPO terms **“Osteoporosis” (HP:0000939)**, “Pathologic fractures” (HP:0002757), and “Bone pain” (HP:0002653) may apply. Boztug et al. mention “bone skeletal abnormalities” without exhaustive detail, suggesting variability in expression.[7][11] Endocrine abnormalities, including hypothyroidism, and pancreatic insufficiency have been recorded in MedGen and individual case reports, consistent with **“Hypothyroidism” (HP:0000821)** and “Exocrine pancreatic insufficiency” (HP:0001738).[3][15] Cardiovascular anomalies such as coarctation of the aorta, while reported in only a handful of cases, underscore the multisystem nature of the disorder and can be annotated as **“Coarctation of the aorta” (HP:0001680)**.[15]

Bleeding manifestations, including recurrent intracranial hemorrhage, have been documented in JAGN1 deficiency.[3] In the case described by El‑Sayed et al., a 4‑year‑old boy with SCN due to JAGN1 mutations presented not only with recurrent infections but also with recurrent intracranial hemorrhage, raising the possibility of vascular fragility or platelet dysfunction secondary to underlying glycosylation defects.[3] This suggests HPO terms such as **“Intracranial hemorrhage” (HP:0002170)** and “Easy bruising” (HP:0000978) in some patients. These features, together with pancreatic and endocrine abnormalities, lend credence to the concept of JAGN1 deficiency as a systemic disorder of glycosylation affecting multiple organ systems.

### Symptom Onset, Severity, Progression, and Frequency

SCN6 is typically **congenital or very early‑onset**, with symptoms of severe infection and evidence of neutropenia appearing in the neonatal period or early infancy.[3][4][5][9][11][15] Rolf Kostmann’s original description of severe congenital neutropenia highlighted infants presenting with severe bacterial infections and ANC persistently below \(0.5 \times 10^{9}/\text{L}\); in JAGN1 deficiency, similar timelines are observed, although recognition of the specific genetic cause has only been possible in recent decades.[6][9][10] El‑Sayed et al.’s case report describes manifestations beginning in infancy, and Boztug’s cohort includes children diagnosed in childhood with retrospective evidence of early infectious vulnerability.[3][11] Thus, the HPO term **“Congenital onset” (HP:0003577)** or “Neonatal onset” (HP:0003623) is appropriate for neutropenia and infections in many cases.

Symptom severity is generally **marked**, given the combination of profound neutropenia and high risk of life‑threatening infections.[6][9][11][15] ANC is often extremely low, and infections include sepsis, deep organ abscesses, and invasive fungal disease, all of which carry high morbidity and mortality if untreated. The increased risk of myelodysplastic syndrome or acute myeloblastic leukemia observed across SCN cohorts further amplifies disease severity.[3][6][9] However, Boztug et al. and subsequent authors note that the clinical phenotype among JAGN1‑deficient patients is **heterogeneous**, with variable expression of extra‑hematologic manifestations, refractoriness to G‑CSF, and complication rates, indicating **variable expressivity** despite high penetrance for neutropenia.[4][7][11][15]

Symptom progression is best characterized as **chronic and lifelong**, with neutropenia present from infancy and persisting unless corrected by HSCT.[3][4][6][11][14] The course of infections can be episodic, with recurrent bouts separated by periods of relative stability, especially under G‑CSF therapy, but the underlying cellular defect is stable and progressive in the sense of cumulative damage, such as osteoporosis and leukemic transformation risk.[6][7][9][10] Bone marrow maturation arrest persists over time, and in some patients, clonal evolution leads to myelodysplastic syndrome or acute myeloid leukemia, altering the disease trajectory towards malignant transformation.[3][6][9] The frequency of core features—severe neutropenia, recurrent infections, bone marrow maturation arrest—is high and near‑universal among molecularly confirmed SCN6 patients, whereas extra‑hematologic features such as pancreatic insufficiency, coarctation of aorta, and intracranial hemorrhage occur in subsets of patients.[3][4][7][11][15]

### Quality of Life Impact and HPO Mapping

SCN6 exerts a profound impact on **quality of life**, affecting daily functioning, social participation, schooling, and mental health. Children with JAGN1 deficiency frequently experience prolonged hospitalizations for infections, recurrent courses of intravenous antibiotics, repeated invasive procedures (bone marrow biopsies, central line placements), and the psychological stress associated with a chronic life‑threatening illness.[3][7][9][11] Growth failure and developmental delay further limit participation in age‑appropriate activities, while skeletal abnormalities and fractures reduce mobility and increase chronic pain.[3][7][15] Parents and caregivers face substantial burdens in managing infection prophylaxis, treatment adherence, and the logistics of specialized care, contributing to family‑level quality of life issues.

Standardized quality of life instruments, such as SF‑36 or EQ‑5D, have not been systematically reported specifically for JAGN1 deficiency, but studies in broader SCN populations indicate lower scores in physical functioning and vitality domains, improved to some extent by G‑CSF therapy but still below population norms.[9][10] JAGN1‑deficient patients may fare worse if they are refractory to G‑CSF, as recurrent severe infections and complications persist. HSCT, when successful, can dramatically improve quality of life by normalizing neutrophil counts and eliminating the constant threat of infection, though it introduces its own acute and chronic risks, such as graft‑versus‑host disease (GVHD) and long‑term immunosuppression.

From an ontology standpoint, in addition to the primary HPO terms already mentioned, SCN6 is associated with broader quality of life‑related phenotypes such as **“Chronic fatigue” (HP:0012378)**, “Frequent hospitalizations” (HP:0006520), and “Reduced social interaction” (HP:0000736), although these are not yet routinely annotated in major databases. Capturing these aspects will be important as more comprehensive natural history and patient‑reported outcome studies are conducted.

## 4. Genetic and Molecular Information

### JAGN1 Gene and Protein Overview

The **JAGN1** gene (jagunal vesicle mediated transporter 1) is located on chromosome **3p25.3** and encodes a transmembrane protein that resides in the endoplasmic reticulum and participates in the early secretory pathway.[1][4][8][11] NCBI Gene (Gene ID:84522) describes JAGN1 as a transmembrane protein necessary for neutrophil differentiation and survival, with mutations resulting in severe congenital neutropenia.[8] OMIM similarly notes that JAGN1 is an ER‑resident protein functioning in the early secretory pathway and that JAGN1 deficiency causes aberrant myeloid cell homeostasis and congenital neutropenia.[4][11] The protein is evolutionarily conserved, with homologs identified in Drosophila and other species; in Drosophila, the jagunal gene is required for reorganizing the ER into subcortical clusters during oogenesis, thereby facilitating vesicular traffic.[13]

Structurally, JAGN1 contains an N‑terminal signal sequence, luminal domains, and transmembrane segments that anchor it to the ER membrane. The precise domain organization in humans has been inferred from sequence homology and experimental localization studies, which demonstrate colocalization with ER markers and exclusion from Golgi apparatus markers.[11][13] Functional data from Drosophila suggest that Jagunal is essential for ER clustering and membrane trafficking, with loss of jagunal leading to reduced vesicular traffic and slowed cell growth.[13] In human neutrophils, JAGN1 appears to interact with components of the secretory pathway required for granule formation, receptor trafficking, and protein glycosylation; JAGN1‑deficient neutrophils display aberrant granule morphology and impaired glycosylation of key surface receptors such as CSF3R.[4][6][7][11]

From an ontology perspective, JAGN1 can be annotated with Gene Ontology (GO) terms including **“endoplasmic reticulum” (GO:0005783)** for cellular component, “protein glycosylation” (GO:0006486) and “vesicle-mediated transport” (GO:0016192) for biological processes, and “protein binding” (GO:0005515) for molecular function. The HGNC gene symbol is **JAGN1** (HGNC:26926), and UniProt provides detailed structural predictions, including transmembrane topology and potential glycosylation sites, though these data are not explicitly referenced in the search results.

### Spectrum and Classification of Pathogenic Variants

Boztug et al. identified **nine distinct homozygous mutations** in JAGN1 among 14 patients from 9 families with SCN6, covering a range of variant types including truncating mutations, in‑frame deletions, and missense changes.[4][11] The variants included c.3G>A in exon 1, which disrupts the defined start of translation; c.35_43del, an in‑frame deletion of three residues (Thr12_Gly14del); and several nonsense and missense variants affecting conserved residues.[4][11][12][14] These mutations were located predominantly in the N‑terminal region and luminal domains of JAGN1, consistent with disruption of ER targeting, stability, or function. Sanger sequencing confirmed homozygosity in affected individuals and carrier status in parents, fitting the autosomal recessive pattern.[4][11]

ClinVar provides detailed classification for some of these variants. The c.35_43del (p.Thr12_Gly14del) variant has multiple submissions, with aggregate germline classification ranging from “uncertain significance” to “pathogenic,” reflecting evolving evidence as more cases are reported.[12][14] The Klein laboratory submission, based on the Boztug study, classifies the variant as pathogenic for severe congenital neutropenia with autosomal recessive inheritance, noting poor response to recombinant human G‑CSF and successful treatment with bone marrow transplant.[14] OMIM lists this variant in the context of SCN6, emphasizing its association with autosomal recessive severe congenital neutropenia.[4][11][14] Overall, the ACMG/AMP classification for well‑studied variants is **pathogenic** or **likely pathogenic**, supported by segregation data, functional studies, and absence or extreme rarity in population databases.[4][11][14]

Functionally, these variants are best described as **loss‑of‑function** alleles, as they either truncate JAGN1, delete conserved residues critical for ER localization or function, or introduce missense changes that destabilize the protein or disrupt its interactions.[4][6][11][13] Overexpression of patient-derived mutant JAGN1 in HL‑60 cells causes increased susceptibility to cell death upon pro‑apoptotic or degranulation stimuli, indicating that the mutant proteins exert a deleterious effect on cell survival.[6] Interestingly, Khandagale et al. observed that silencing JAGN1 using small interfering RNAs did not replicate the full phenotype of mutant overexpression, suggesting that some mutants may exert **dominant‑negative effects** in experimental systems despite the autosomal recessive inheritance pattern in patients.[6][10] This nuanced functional behavior underscores the importance of considering both loss‑of‑function and toxic‑gain‑of‑function mechanisms in mechanistic models.

### Variant Frequency, Population Data, and Germline Origin

JAGN1 variants associated with SCN6 are **rare in the general population**, consistent with the low prevalence of severe congenital neutropenia. ClinVar and gnomAD data indicate that the c.35_43del variant has a minor allele frequency of about 0.002%, reflecting rare carrier status.[14] Most pathogenic variants were initially identified in families of Turkish, Israeli, and European origin, often with consanguinity, suggesting that population‑specific founder effects may exist, although detailed founder mutation studies have not been systematically published.[4][7][11] Boztug’s cohort included patients from diverse geographic backgrounds, implying that JAGN1 mutations can arise in multiple populations without strong restriction to a particular ethnic group.[4][11]

All documented pathogenic JAGN1 variants are **germline** and present in all tissues, fitting the Mendelian inherited pattern rather than somatic mosaicism. There is currently no evidence that somatic JAGN1 mutations contribute to sporadic neutropenia in individuals without germline defects. Structural variants (large deletions, duplications, translocations) involving JAGN1 have not been widely reported; most causative changes are single-nucleotide variants or small insertions/deletions detected by sequencing.[4][11][12][14] Consequently, chromosomal microarray or karyotyping are not primary diagnostic tools for SCN6, and high‑resolution sequencing methods (targeted gene sequencing, whole‑exome sequencing) remain the gold standard.

### Modifier Genes, Epigenetics, and Chromosomal Abnormalities

To date, no **modifier genes** have been conclusively implicated in altering disease severity or expression in SCN6. JAGN1 deficiency itself is sufficient to produce the neutropenia phenotype, and the variability in extra‑hematologic features is thought to reflect stochastic factors, environmental exposures, and perhaps subtle background genetic differences that have not been systematically mapped.[4][7][11][15] Unlike some immunodeficiencies where polymorphisms in cytokine genes or HLA loci modulate severity, such interactions are not yet described for JAGN1‑mediated SCN.

Epigenetic studies specifically focused on JAGN1 expression or chromatin structure in SCN6 are lacking. Given the clearly pathogenic germline mutations, epigenetic modulation may play a secondary role, for instance in determining JAGN1 expression levels or in regulating stress response pathways, but no disease-defining methylation signatures or histone modification patterns have been reported.[11] Similarly, **chromosomal abnormalities** such as aneuploidy or translocations do not form part of the etiologic spectrum in SCN6; however, clinically, SCN patients (including those with JAGN1 mutations) are at increased risk of developing myelodysplastic syndrome and acute myeloid leukemia, conditions that often involve acquired chromosomal abnormalities in hematopoietic cells.[3][6][9][11] These are downstream, secondary events, not primary etiologic features, and arise from clonal evolution under chronic stress rather than from germline JAGN1 alterations.

## 5. Environmental Information

### Environmental and Lifestyle Modifiers of Clinical Course

While environmental factors do not cause SCN6, they substantially influence the **clinical course, infection burden, and long‑term outcomes** of patients. Children with JAGN1 deficiency are inherently susceptible to bacterial and fungal infections due to severe neutropenia; exposure to contaminated water, poor sanitation, crowded living conditions, or endemic pathogens can dramatically increase the number and severity of infectious episodes.[3][9][11][15] Conversely, environments with robust public health infrastructure, vaccination programs, and ready access to antibiotics and tertiary care reduce infection-related morbidity and mortality. These influences are best conceptualized as modifiers of disease expression rather than etiologic factors.

Lifestyle factors in early childhood, such as nutritional status, may exacerbate or ameliorate some extra‑hematologic features. Failure to thrive and growth delay can be worsened by poor nutrition, malabsorption, or chronic illness; rigorous nutritional support can partially correct weight and height trajectories, though underlying endocrine or pancreatic insufficiency may persist.[3][7][15] Smoking and alcohol consumption are not typically relevant to pediatric SCN6 patients but may become considerations in older survivors; chronic exposure to tobacco smoke could increase respiratory infection risk, and alcohol might modulate bone health or immune responses. Exercise, physiotherapy, and measures to prevent fractures can influence skeletal outcomes, particularly in patients with osteoporosis and repeated fractures.[3][7]

### Infectious Agents and Clinical Triggers

Infectious agents act as **clinical triggers** that unmask or exacerbate the underlying neutrophil defect in SCN6. Bacterial pathogens such as Staphylococcus aureus, Escherichia coli, Pseudomonas aeruginosa, and Streptococcus pneumoniae commonly cause sepsis, pneumonia, skin and soft tissue infections, and osteomyelitis in neutropenic patients.[3][9][11] Fungal pathogens, especially Aspergillus species, can cause invasive pulmonary disease or disseminated infection, as exemplified by the JAGN1‑deficient patient with severe osteoporosis and repeated bone fractures who also had aspergillosis.[3][7] Viral infections typically do not dominate the clinical picture but may complicate bacterial or fungal infections and contribute to systemic illness.

Mechanistically, infectious stimuli trigger neutrophil activation and degranulation. In JAGN1‑mutant cells, Khandagale et al. showed that agonists that normally trigger degranulation instead precipitate a calcium‑dependent, calpain‑mediated cell death program, leading to increased loss of myeloid cells.[6][10] This implies that exposure to pathogens, which drive degranulation through toll‑like receptor and Fc receptor signaling, may accelerate neutrophil depletion in SCN6 beyond baseline defects, thereby worsening neutropenia at times of highest need. Preventing infections through vaccinations, prophylactic antibiotics, antifungals, and environmental hygiene is therefore a crucial therapeutic strategy that directly modulates the downstream impact of the genetic lesion.

No specific toxins, pollutants, or occupational exposures have been linked to onset or progression of JAGN1‑mediated SCN6. As a pediatric, congenital immunodeficiency, the primary environmental health considerations are infection control and supportive care.

## 6. Mechanism / Pathophysiology

### Ordered Causal Chain from JAGN1 Mutation to Clinical Manifestations

Step 1: Germline biallelic pathogenic mutations in JAGN1 lead to defective or absent JAGN1 protein in endoplasmic reticulum membranes of hematopoietic cells, particularly myeloid progenitors and neutrophils.[4][8][11][12][14]

Step 2: Loss or dysfunction of JAGN1 results in disorganization of the early secretory pathway and ER architecture, impairing vesicle trafficking, ER clustering, and N‑glycosylation of nascent proteins, especially in myeloid cells.[11][13]

Step 3: ER disorganization and glycosylation defects lead to accumulation of misfolded proteins, ER stress, and induction of unfolded protein response (UPR), inferred from increased levels of ER chaperones such as Grp78/BiP in mutant cells.[3][11]

Step 4: Impaired glycosylation and trafficking of the granulocyte colony‑stimulating factor receptor (CSF3R) result in decreased surface expression and defective G‑CSF signaling, limiting proliferative and survival signals to neutrophil precursors and mature cells.[4][7][11]

Step 5: ER stress and defective CSF3R signaling together lead to impaired neutrophil maturation, manifested as granulopoiesis maturation arrest at the promyelocyte/myelocyte stage in the bone marrow.[4][5][11][15]

Step 6: Concurrently, JAGN1 mutations cause increased sensitivity of myeloid cells to calcium influx and activation of calpain‑dependent, non‑apoptotic cell death pathways in response to pro‑apoptotic stimuli and degranulation agonists.[6][10]

Step 7: Enhanced calpain-mediated cell death leads to excessive loss of neutrophil precursors and mature neutrophils, further reducing ANC and exacerbating neutropenia.[6][7][10][11]

Step 8: Severe chronic neutropenia leads to impaired innate immune responses, resulting in recurrent, severe bacterial and fungal infections, tissue damage, and systemic inflammation.[3][5][9][11][15]

Step 9: Chronic proliferative stress in the bone marrow, combined with ER stress and recurrent infections, predisposes to clonal hematopoietic evolution and increased risk of myelodysplastic syndrome and acute myeloid leukemia, inferred from broader SCN cohorts.[3][6][9][11]

Step 10: Systemic glycosylation defects and ER stress in non‑hematopoietic tissues, inferred from multisystem features and Drosophila jagunal data, contribute to extra‑hematologic manifestations such as growth failure, endocrine abnormalities, pancreatic insufficiency, skeletal defects, and vascular anomalies.[3][7][11][13][15]

In this chain, Steps 1–4 represent **upstream molecular and cellular lesions**, Steps 5–7 represent **intermediate cellular and tissue-level consequences**, and Steps 8–10 represent **downstream clinical and systemic manifestations**.

### Initiating Lesion: JAGN1 Mutation and ER Dysfunction

The initiating lesion in SCN6 is the **germline mutation in JAGN1**, which alters the structure and function of an ER-resident transmembrane protein.[1][4][8][11][12][14] JAGN1 localizes to the endoplasmic reticulum, and its role in ER organization and vesicular trafficking is well documented in Drosophila oocytes, where jagunal mutants fail to form subcortical ER clusters and exhibit reduced vesicular traffic to the lateral membrane.[13] Boztug et al. extended these insights to human neutrophils, demonstrating that JAGN1 is ubiquitously expressed but critically required for myeloid cell homeostasis.[11] In JAGN1‑deficient neutrophils and myeloid cells, ultrastructural analysis reveals aberrant granule morphology and altered ER organization, reflecting disruption of the early secretory pathway.[7][11]

Mechanistically, loss or dysfunction of JAGN1 perturbs **ER morphology and secretory pathway dynamics**, leading to mislocalization or instability of proteins destined for secretory granules or the cell surface.[11][13] This includes receptors like CSF3R, adhesion molecules, and components of granules such as proteases and antimicrobial peptides. ER disorganization also impedes the co‑translational N‑glycosylation of proteins, a process that is intimately linked to ER function and that affects protein folding, trafficking, and stability.[11] El‑Sayed et al. emphasize that severe congenital neutropenia caused by JAGN1 mutation is a rare condition resulting from maturation arrest secondary to “endoplasmic reticulum stress response from impaired neutrophil protein glycosylation,” directly linking JAGN1 function to glycosylation and ER stress.[3]

The ER dysfunction in JAGN1 deficiency can be annotated with GO terms such as **“endoplasmic reticulum organization” (GO:0005788)** and “response to endoplasmic reticulum stress” (GO:0034976). The primary affected cell types are **myeloid progenitor cells** and **neutrophils**, corresponding to Cell Ontology terms **CL:0000048 (myeloid progenitor cell)** and CL:0000775 (neutrophil). The tissue context is predominantly the **bone marrow** (UBERON:0001741), where granulopoiesis occurs, but ER dysfunction may also affect other tissues.

### Secretory Pathway, Glycosylation Defects, and G‑CSF Signaling

A central mechanistic theme in SCN6 is the **defect in secretory pathway and protein glycosylation**, particularly affecting CSF3R and neutrophil granule components.[4][6][7][11] Boztug et al. showed that JAGN1 participates in the secretory pathway and is required for G‑CSF receptor–mediated signaling.[7][11] JAGN1‑deficient neutrophils display decreased amounts of G‑CSF receptors, which is thought to result from N‑glycosylation defects that impair receptor maturation and trafficking to the cell surface.[4][7][11] This has profound consequences, as G‑CSF signaling is the primary driver of neutrophil proliferation and survival in granulopoiesis, and recombinant G‑CSF (filgrastim) is the mainstay treatment for SCN.[9][10]

El‑Sayed et al. highlight that GM‑CSF can improve N‑glycosylation and is therefore used as a treatment for congenital neutropenia in JAGN1 mutation, implying that modulating secretory pathway function can partially correct downstream defects.[3] This suggests that glycosylation defects extend beyond CSF3R, affecting broader sets of proteins within neutrophils. Glycosylation pathways involve multiple enzymes and chaperones; while JAGN1 is not an enzyme per se, its role in ER organization may be necessary for proper assembly and function of glycosylation machinery. The glycosylation defect can be annotated with GO term **“protein N‑linked glycosylation” (GO:0006487)** and might intersect with congenital disorders of glycosylation (CDG) ontologies.

Impaired CSF3R signaling leads to **reduced responsiveness to G‑CSF**, which is a hallmark of SCN6. Boztug et al. and KlinVar submissions note that JAGN1‑deficient patients show partial or complete refractoriness to recombinant human G‑CSF therapy.[4][7][10][11][14] From a pathophysiological standpoint, this means that endogenous and exogenous G‑CSF cannot fully rescue neutrophil production, leaving patients at high risk of infections despite therapy. Conversely, GM‑CSF signaling, which uses different receptors and pathways, may be less dependent on JAGN1-mediated glycosylation and thus retain more function, explaining its therapeutic efficacy in some cases.[3] The molecular pathways involved include **JAK–STAT signaling**, **PI3K–AKT**, and **MAPK cascades**, which transduce G‑CSF and GM‑CSF signals to transcriptional programs of proliferation and survival, though specific alterations in these pathways in JAGN1 deficiency have not been exhaustively mapped.

### Cell Death Pathways in Myeloid Cells: Calcium and Calpain

Khandagale et al. provided critical mechanistic insights into cell death pathways in JAGN1‑mutant myeloid cells, showing that **SCN‑associated JAGN1 mutations unleash a calcium‑ and calpain‑dependent cell death program**.[6][10] Using HL‑60 cells as a model, they found that overexpression of patient-derived JAGN1 mutants increased cell death in response to pro‑apoptotic stimuli such as etoposide, staurosporine, and thapsigargin, but that this cell death was not primarily caspase-dependent.[6] Instead, cells expressing mutant JAGN1 were remarkably susceptible to agonists that normally trigger degranulation and succumbed to a calcium‑dependent cell death program that was completely prevented by pharmacologic inhibition of calpain but unaffected by caspase inhibition.[6][10]

The experiments showed that mutant JAGN1 alters the sensitivity of myeloid cells to conventional pro‑apoptotic stimuli and leads to drastic increases in cytosolic calcium and subsequent drops in mitochondrial membrane potential upon stimulation.[6][10] These findings indicate that JAGN1 plays a role in regulating intracellular calcium homeostasis and in preventing inappropriate activation of calpain, a calcium‑dependent protease that can mediate non‑apoptotic cell death. The authors concluded that “SCN-associated JAGN1 mutations unleash a calcium- and calpain-dependent cell death in myeloid cells” and suggested that neutropenia-associated JAGN1 mutations promote a non-apoptotic, calpain-dependent form of cell death.[6]

From a mechanistic ontology standpoint, these processes can be annotated with GO terms such as **“calcium‑dependent cell death” (GO:0008219)**, “calpain-mediated signaling” (GO:0005544), and “regulation of mitochondrial membrane potential” (GO:0051881). The affected cell types are myeloid progenitors and neutrophils (CL:0000048, CL:0000775), and the subcellular compartments involved include the **cytosol** (GO:0005829), **mitochondria** (GO:0005739), and **endoplasmic reticulum** (GO:0005783). Clinically, this calpain‑dependent cell death contributes to the **accelerated loss of neutrophils**, amplifying the impact of maturation arrest and further reducing ANC.

An intriguing aspect of Khandagale’s findings is that **silencing JAGN1** with small interfering RNA did not increase susceptibility to cell death, whereas overexpression of mutant JAGN1 did.[6][10] This suggests that mutant JAGN1 proteins may exert a **dominant pathophysiologic effect** on calcium and calpain regulation, at least in the experimental context, despite the autosomal recessive inheritance pattern in patients. In vivo, homozygous expression of mutant JAGN1 likely combines loss of normal function and gain of abnormal function. Pharmacologic inhibition of calpain or modulation of calcium signaling could thus represent future therapeutic avenues.

### Tissue-level Consequences and Clinical Correlates

The cellular lesions described above translate into **tissue-level consequences** primarily in the bone marrow and immune system, but also in other organs. In the bone marrow, ER stress, impaired glycosylation, defective CSF3R signaling, and calpain-mediated cell death converge to produce **granulopoiesis maturation arrest**, as observed histologically.[4][5][11][15] The marrow becomes enriched in promyelocytes and myelocytes, with relative paucity of mature neutrophils, a pattern typical of SCN.[4][9] This maturation arrest is a direct corollary of impaired differentiation and survival of myeloid progenitors and can be annotated with GO term **“negative regulation of neutrophil differentiation” (GO:0045649)** and HPO term “Bone marrow maturation arrest” (HP:0001678).

Peripheral blood shows **severe neutropenia**, with ANC far below normal, and sometimes relative monocytosis or eosinophilia as compensatory phenomena.[6][9][11] The immune system, particularly innate immunity, is compromised, leading to recurrent infections and tissue damage. Organs affected by infections include lungs (pneumonia, aspergillosis), skin (abscesses, ulcers), bones (osteomyelitis and fractures), central nervous system (intracranial hemorrhage, meningitis), and others.[3][7][9] Chronic infection and inflammation may cause secondary damage, such as bronchiectasis, fibrosis, or organ failure, although detailed natural history for JAGN1‑specific cohorts remains limited.

The increased risk of **myelodysplastic syndrome and acute myeloid leukemia** in SCN broadly has been attributed to chronic proliferative stress on hematopoietic cells under G‑CSF therapy, as well as intrinsic genetic instability.[6][9][11] For JAGN1 deficiency specifically, Boztug et al. report that patients are at risk of malignant transformation similar to other SCN forms, though the small cohort precludes precise risk estimates.[11] Mechanistically, ER stress, chronic inflammation, and proliferative signaling in the setting of defective CSF3R function may create a pro‑mutagenic environment in bone marrow cells, leading to clonal evolution. The acquisition of secondary mutations and chromosomal abnormalities in hematopoietic stem and progenitor cells then drives MDS/AML, altering the clinical course and necessitating interventions such as HSCT.

Extra‑hematologic tissues such as bone, pancreas, thyroid, and vasculature may experience **systemic consequences of glycosylation defects and ER stress**, although this is inferred rather than fully elucidated.[3][7][11][15] Osteoporosis and fractures may reflect impaired collagen and matrix protein glycosylation, as well as chronic inflammation and G‑CSF exposure; pancreatic insufficiency and hypothyroidism may be linked to ER stress in secretory cells of these organs. Vascular abnormalities such as coarctation of the aorta and recurrent intracranial hemorrhage point to possible defects in vascular connective tissues and coagulation pathways, again potentially rooted in glycosylation abnormalities. These systemic manifestations highlight that JAGN1 deficiency may have **multi-organ impact** even though neutropenia is the most clinically visible phenotype.

### Omics and Systems-level Insights

The initial identification of JAGN1 mutations in SCN6 relied on **whole‑exome sequencing (WES)**, underscoring the importance of genomic technologies in elucidating disease mechanisms.[4][6][11] Boztug et al. used WES to scan the exomes of patients with unexplained SCN and discovered JAGN1 as a novel gene implicated in neutrophil differentiation and survival.[11] Khandagale et al. likewise applied WES to a cohort of autosomal recessive SCN patients and identified homozygous JAGN1 mutations in three individuals, confirming and extending Boztug’s findings.[6][10] These genomic data integrate with transcriptomic and proteomic analyses that show altered expression of ER stress markers, granule proteins, and receptors.

Although comprehensive transcriptome or proteome datasets for JAGN1‑deficient neutrophils are not yet widely available, the mechanistic studies suggest altered expression of genes involved in ER stress, calcium signaling, and apoptosis/calpain pathways.[6][11] For example, increased Grp78 (BiP), an ER chaperone, is indicative of unfolded protein response activation.[3] Proteomic analysis of neutrophil granules may reveal aberrant composition, reflecting defective secretory pathway trafficking. Metabolomic and lipidomic signatures have not been systematically reported but may highlight changes in ER-related lipid metabolism or oxidative stress.

Systems-level integration of genomic and functional data suggests that SCN6 can be conceptualized as a **network disorder** involving interconnected modules of ER organization, glycosylation, cytokine signaling, and cell death. Multi‑omics approaches, combining WES with RNA‑seq, proteomics, and phosphoproteomics, could further delineate how JAGN1 mutations propagate through molecular networks to produce the observed phenotypes. Functional genomics screens (CRISPR or RNAi) targeting ER and secretory pathway components may identify synthetic lethal interactions or compensatory pathways that could be exploited therapeutically. As of now, the main functional genomic work has focused on overexpression and knockdown in cell lines rather than high‑throughput screens.[6][10][11]

## 7. Anatomical Structures Affected

### Organ and System-level Involvement

At the organ level, SCN6 primarily involves the **hematopoietic system**, particularly the bone marrow and peripheral blood, but has secondary effects on multiple organ systems through infections and systemic glycosylation defects.[4][5][9][11][15] The bone marrow (UBERON:0001741) is the site of granulopoiesis, where JAGN1 deficiency causes maturation arrest of myeloid lineages. Peripheral blood (UBERON:0000178) reflects the downstream impact in the form of neutropenia. The immune system (UBERON:0002405) is functionally compromised, with innate immunity most affected.

Secondary organ involvement includes the **respiratory system**, with lungs (UBERON:0002048) frequently affected by pneumonia, bronchitis, and aspergillosis.[3][7][9] The **integumentary system** (skin; UBERON:0002097) is impacted by skin ulcers, abscesses, and cellulitis. The **musculoskeletal system**, particularly bones (UBERON:0001474), suffers from osteoporosis and fractures in some patients, compounded by chronic inflammation and possible glycosylation defects in bone matrix proteins.[3][7][15] The **endocrine system** is involved via hypothyroidism and possibly other hormonal disturbances, while the **digestive system**, especially the pancreas (UBERON:0001264), can manifest pancreatic insufficiency.[3][15] Cardiovascular structures such as the aorta (UBERON:0000948) may exhibit structural anomalies such as coarctation.[15] The central nervous system (UBERON:0001016) is affected in cases with intracranial hemorrhage and infections.

### Tissue and Cell-type Specific Vulnerability

Within the bone marrow, the most vulnerable cell populations are **myeloid progenitors** and **neutrophil precursors**, reflecting the specificity of JAGN1’s role in myeloid cell homeostasis.[4][6][7][11] Cell Ontology terms CL:0000048 (myeloid progenitor cell), CL:0000775 (neutrophil), and CL:0000038 (hematopoietic stem cell) are relevant. JAGN1 is ubiquitously expressed, but its deficiency manifests most prominently in neutrophil lineage cells, suggesting lineage-specific reliance on JAGN1-mediated ER and secretory functions.[11] HL‑60 cells, a human promyelocytic cell line (CL:0002028), have been used as an experimental model for myeloid cells expressing mutant JAGN1.[6][10]

In peripheral tissues, secretory cells such as **exocrine pancreatic acinar cells**, **thyroid follicular cells**, and **osteoblasts** may be particularly vulnerable to systemic glycosylation and ER stress defects, as suggested by pancreatic insufficiency, hypothyroidism, and bone abnormalities.[3][7][11][15] However, detailed cell-type mapping is limited. Vascular endothelial cells and smooth muscle cells in the aorta may be affected in cases with coarctation, and neurological cells may be secondarily impacted by hemorrhage rather than primary JAGN1 deficiency.

### Subcellular Localization and ER-centric Pathology

Subcellularly, JAGN1 localizes to the **endoplasmic reticulum (ER)**, and its deficiency leads to ER-centric pathology.[8][11][13] The ER (GO:0005783) is critical for protein folding, glycosylation, and trafficking; ER stress and disorganization disrupt these functions. JAGN1’s role in ER clustering and vesicle trafficking was demonstrated in Drosophila oocytes, where Jagunal is required for reorganizing the ER into subcortical clusters and facilitating vesicle transport.[13] In human neutrophils, JAGN1 deficiency leads to disrupted ER architecture and secretory granule formation.[7][11]

Other subcellular compartments implicated in SCN6 pathophysiology include **secretory granules**, **Golgi apparatus**, **mitochondria**, and the **cytosol**. Secretory granules in JAGN1‑mutant cells show aberrant morphology, suggesting defective biogenesis or protein content.[7][11] The Golgi apparatus (GO:0005794) is indirectly affected by ER trafficking defects. Mitochondria experience changes in membrane potential in response to increased cytosolic calcium, linking ER calcium dysregulation to mitochondrial stress.[6] Calpain activation occurs in the cytosol and at membranes, mediating proteolysis of key substrates that drive cell death.[6][10] These subcellular phenomena integrate into a multi‑compartment pathophysiologic model.

## 8. Temporal Development

### Onset and Early Natural History

SCN6 typically presents with **congenital or very early-onset neutropenia**, with clinical manifestations emerging in the neonatal period or early infancy.[3][4][5][9][11][15] Newborns may have normal appearance at birth, but within weeks to months they develop recurrent bacterial infections such as omphalitis, pneumonia, or sepsis, prompting blood counts that reveal severe neutropenia.[3][9] Bone marrow biopsy at this stage shows granulopoiesis maturation arrest. If genetic testing is performed, JAGN1 mutations can be identified, but historically, diagnosis of specific SCN subtypes was delayed until sequencing technologies became widely available.

The early natural history involves **frequent hospitalizations for infections**, rapid cycling between acute illness and short recovery periods, and trial of G‑CSF therapy to increase neutrophil counts.[9][10][11] In JAGN1 deficiency, G‑CSF may have limited effect, leading clinicians to escalate doses or consider alternative therapies. Extra‑hematologic features such as failure to thrive, developmental delay, and skeletal abnormalities may become evident during infancy and early childhood, especially in patients with severe systemic glycosylation defects.[3][7][15] Early recognition and management are crucial to prevent irreversible organ damage.

### Long-term Progression, Complications, and Treatment Effects

The long‑term progression of SCN6 depends heavily on **treatment strategies and presence of complications** such as leukemia. Without effective treatment, severe neutropenia persists, leading to ongoing infections, chronic inflammation, and progressive organ damage. With G‑CSF therapy, many SCN patients see improved ANC and reduced infections; however, JAGN1-deficient patients often exhibit refractoriness, and their infection burden remains substantial.[4][7][10][11][14] Over time, chronic G‑CSF exposure and proliferative stress in the bone marrow increase the risk of myelodysplastic syndrome and acute myeloid leukemia, a complication observed in SCN cohorts, including JAGN1-mutant patients.[3][6][9][11]

Bone health may deteriorate over years, with osteoporosis and fractures emerging as later complications, likely influenced by chronic inflammation, reduced physical activity, endocrine abnormalities, and possibly direct effects of glycosylation defects on bone matrix.[3][7][15] Pancreatic insufficiency and endocrine dysfunction may manifest in later childhood or adolescence, requiring hormone replacement and nutritional support. Neurological complications such as intracranial hemorrhage may occur episodically, posing acute life‑threatening crises.[3]

Allogeneic **hematopoietic stem cell transplantation (HSCT)** represents a major inflection point in the disease course. Successful HSCT can restore normal neutrophil counts and function, eliminating the primary immunodeficiency and substantially reducing infection-related morbidity.[3][11][14] Patients transplanted in adolescence or adulthood may still carry accumulated organ damage from earlier disease and treatment but are protected from ongoing neutropenia. HSCT itself carries risks of GVHD, graft failure, and infections, and long-term follow‑up is needed. The timing of HSCT—the **critical window for intervention**—is often determined by the degree of refractoriness to G‑CSF, severity of infections, and evidence of clonal evolution towards leukemia.

### Critical Windows and Disease Course Patterns

SCN6 exhibits a **chronic, lifelong course** with critical windows for intervention in early childhood and at points of clonal hematopoietic evolution. The neonatal and early infancy period is critical for diagnosis and initiation of infection prophylaxis and G‑CSF therapy. Early genetic testing can identify JAGN1 mutations, enabling targeted counseling and anticipation of refractoriness to G‑CSF.[4][6][11][15] The childhood period is crucial for monitoring growth, development, bone health, endocrine function, and leukemic transformation risk. Regular bone marrow examinations and cytogenetic analyses may detect early signs of clonal evolution.

Disease course patterns can be described as **episodic infections** superimposed on a stable baseline of neutropenia and maturation arrest. Some patients experience relative stability between infections, while others have more continuous low‑grade illness. The onset of leukemia or MDS represents a shift to an advanced disease stage, often prompting HSCT. HSCT, when performed, can change the course to one of stable hematopoiesis and reduced infections, albeit with ongoing need for monitoring GVHD, secondary malignancies, and organ sequelae.

## 9. Inheritance and Population

### Inheritance Pattern, Penetrance, and Expressivity

SCN6 follows a **classical autosomal recessive inheritance pattern**, with affected individuals harboring two pathogenic alleles in JAGN1, either as homozygotes or compound heterozygotes.[1][4][5][11][12][14][15] MedGen describes autosomal recessive inheritance as a mode in which traits manifest in individuals with two pathogenic alleles, either homozygotes or compound heterozygotes, and lists JAGN1 (3p25.3) as the gene directly associated with SCN6.[5][15] Boztug et al. report that all 14 patients in their cohort were homozygous for distinct JAGN1 mutations, and pedigree analysis shows segregation consistent with recessive inheritance.[4][11] ClinVar submissions likewise identify homozygous JAGN1 variants in affected individuals and carrier status in heterozygous relatives.[12][14]

Penetrance for **neutropenia and infection susceptibility** appears to be **complete or near complete** in individuals with biallelic pathogenic JAGN1 mutations, as all reported cases manifest severe neutropenia and recurrent infections.[4][7][11][15] There is no evidence of unaffected homozygotes in published pedigrees, and thus incomplete penetrance is unlikely. Expressivity, however, is **variable**, particularly for extra‑hematologic features such as skeletal abnormalities, endocrine dysfunction, pancreatic insufficiency, and cardiovascular anomalies.[3][7][11][15] Some patients present predominantly with neutropenia and infections, while others also exhibit growth failure, developmental delay, and multisystem involvement.

Genetic anticipation, a phenomenon wherein disease severity increases in successive generations, is not reported in SCN6, which is consistent with the absence of repeat expansion mechanisms. Germline mosaicism has not been described; given consanguinity in many families, new mutations likely arise in ancestral generations and segregate as classical recessive alleles.

### Epidemiology, Prevalence, and Demographics

SCN6 is a rare disease within the already rare category of severe congenital neutropenia. Orphanet classifies severe congenital neutropenia as a rare primary immunodeficiency, without providing subtype-specific prevalence figures.[9] Boztug’s cohort suggests that JAGN1 mutations account for approximately **10% of SCN patients** in their series of 90 individuals, indicating that SCN6 might represent a substantial fraction of autosomal recessive SCN cases but remains rare in absolute terms.[7][11] Given SCN’s estimated prevalence of a few per million, SCN6 likely occurs in fewer than 1 per million individuals, though precise epidemiologic data are lacking.

Population demographics in reported SCN6 cases include patients from **Turkey, Israel, and European countries**, with frequent consanguinity.[3][4][7][11] This suggests that SCN6 may be more commonly detected in populations with high consanguinity rates and in centers with active SCN research programs. However, JAGN1 mutations, like other rare recessive alleles, can arise in any population, and absence of reports in certain regions may reflect underdiagnosis rather than true absence. Sex distribution appears balanced, with both male and female patients documented.[3][4][7][11] Age distribution includes infants, children, adolescents, and adults, particularly those diagnosed in childhood and surviving into adulthood with G‑CSF or HSCT therapy.

Carrier frequency data for JAGN1 pathogenic variants are sparse. gnomAD and ClinVar indicate low frequencies (around 0.002% for c.35_43del), consistent with rarity.[14] Founder effects may exist for particular variants in specific populations, but systematic founder mutation studies have not yet been undertaken. Consanguinity plays a significant role in **increasing the likelihood of homozygosity** for rare pathogenic alleles, and many SCN6 cases occur in consanguineous families.[4][7][11][15]

## 10. Diagnostics

### Clinical and Laboratory Evaluation

Diagnostic evaluation of SCN6 begins with **clinical suspicion** of severe congenital neutropenia in infants or children presenting with recurrent, severe infections and persistently low neutrophil counts.[3][6][9][11] Complete blood counts (CBC) typically show ANC below \(0.5 \times 10^{9}/\text{L}\), with other lineages generally preserved.[6][9][11] HPO term **“Decreased total neutrophil count” (HP:0001875)** describes this laboratory abnormality and is explicitly referenced in MedGen’s description of SCN6.[15] Serial CBCs confirm chronicity rather than transient post-infectious neutropenia.

Bone marrow examination is a cornerstone of diagnosis. Aspirates and biopsies reveal **granulopoiesis maturation arrest** at the promyelocyte/myelocyte stage, with an increased proportion of immature myeloid cells and paucity of mature segmented neutrophils.[4][5][11][15] MedGen lists “Bone marrow maturation arrest” as a defining feature.[15] Histopathology may show hypercellularity and normal or increased numbers of early myeloid precursors, distinguishing SCN6 from aplastic anemia. Immunohistochemistry and flow cytometry can further delineate myeloid maturation stages and rule out leukemia.

Additional laboratory tests include **infection work‑ups**, such as blood and tissue cultures, imaging, and inflammatory markers. Specific functional neutrophil assays, such as nitroblue tetrazolium (NBT) tests or oxidative burst assays, may be performed to distinguish SCN from chronic granulomatous disease and other neutrophil functional disorders.[9] Serum immunoglobulin levels, lymphocyte subsets, and complement assays help rule out broader immunodeficiencies. Thyroid function tests, pancreatic enzyme assessment, bone density measurements, and echocardiography may be indicated if extra‑hematologic features are suspected.[3][7][15]

### Genetic Testing Strategies

Once severe congenital neutropenia is clinically established, **genetic testing** is essential to identify the specific subtype and guide management. Options include targeted gene panels for SCN, single‑gene sequencing of JAGN1, and more comprehensive methods such as whole‑exome or whole‑genome sequencing.[4][6][11] Given the genetic heterogeneity of SCN, gene panels that include ELANE, HAX1, G6PC3, GFI1, VPS45, and JAGN1 are often used as first‑line tests. If these are negative or if clinical suspicion remains high for a rare gene, WES can detect mutations in JAGN1 and other genes.[4][6][10][11]

Boztug et al. used WES to identify JAGN1 mutations in SCN patients, underscoring the utility of exome sequencing in rare immunodeficiencies.[11] Khandagale et al. similarly applied WES to 27 autosomal recessive SCN patients and found homozygous JAGN1 mutations in three, confirming this approach’s value.[6][10] Single‑gene sequencing of JAGN1 can be performed if clinical features strongly suggest JAGN1 deficiency or if family history indicates consanguinity and autosomal recessive inheritance. Chromosomal microarray and karyotyping are less useful for SCN6, as JAGN1 pathogenic variants are point mutations or small indels rather than large structural aberrations.[4][11][12][14]

ClinVar and MedGen provide variant‑level information, which can guide interpretation of genetic results. For example, detection of c.35_43del (p.Thr12_Gly14del) in homozygous form should prompt classification as pathogenic for SCN6, based on available evidence.[12][14] ACMG/AMP guidelines can be applied to classify variants, considering segregation, functional data, and population frequency. Genetic counseling for family members is crucial to identify carriers and guide reproductive decisions.

### Differential Diagnosis and Screening Considerations

Differential diagnosis of SCN6 includes other forms of **severe congenital neutropenia**, cyclic neutropenia, acquired neutropenia due to infections or drugs, and other primary immunodeficiencies presenting with recurrent infections.[9][10] SCN due to ELANE mutations (autosomal dominant), HAX1 mutations (classical Kostmann disease), G6PC3 mutations (SCN type 4), VPS45 and GFI1 mutations, and others must be distinguished based on genetic testing, response to G‑CSF, and extra‑hematologic features.[2][6][9][10][11] For example, G6PC3 deficiency often features prominent ectatic superficial veins and cardiac and urogenital anomalies, while JAGN1 deficiency shows skeletal abnormalities, pancreatic insufficiency, hypothyroidism, and facial dysmorphism.[2][3][7][15]

Cyclic neutropenia, which involves oscillating ANC with periods of near-normal counts, differs from SCN6’s persistent severe neutropenia and can be distinguished by serial CBCs and ELANE sequencing.[9][10] Acquired neutropenia due to drugs (chemotherapy, immunosuppressants), infections (viral), or autoimmune processes must be ruled out through clinical history and laboratory evaluation. Chronic granulomatous disease, leukocyte adhesion deficiency, and other neutrophil functional disorders cause recurrent infections but usually present with normal or near-normal neutrophil counts, differentiating them from SCN6.[9]

Screening for SCN6 is not currently part of population-based newborn screening programs, given its rarity. However, **cascade screening** of family members in affected families is recommended to identify carriers and plan for early diagnosis in future pregnancies. Prenatal or preimplantation genetic diagnosis can be offered if parental carrier status for a pathogenic JAGN1 variant is known. These strategies fall under secondary prevention and reproductive counseling.

### Emerging Omics-based Diagnostics

Beyond DNA sequencing, omics-based diagnostics such as transcriptomics, proteomics, and metabolomics remain primarily research tools at present. RNA sequencing of bone marrow or peripheral blood cells could reveal transcriptional signatures of ER stress, unfolded protein response, and altered cytokine signaling in JAGN1‑deficient patients, potentially serving as biomarkers of disease activity. Proteomics of neutrophil granules might identify aberrant protein compositions characteristic of JAGN1 deficiency. Metabolomics could detect changes in ER-related lipid metabolism or oxidative stress metabolites.

Liquid biopsy approaches, such as circulating cell-free DNA or RNA, are not yet applied to SCN6, but could be useful for monitoring clonal evolution towards leukemia or for non‑invasive detection of ER stress markers. As multi‑omics integration becomes more common in clinical research, SCN6 may benefit from such comprehensive profiling, especially for predicting progression to MDS/AML and identifying therapeutic targets.

## 11. Outcome / Prognosis

### Survival, Mortality, and Life Expectancy

Before the advent of G‑CSF therapy, severe congenital neutropenia carried a high mortality rate in childhood due to recurrent, life‑threatening infections.[9][10] With G‑CSF, survival has improved significantly in SCN cohorts, but patients remain at risk of infections and leukemic transformation.[6][9][10][11] In SCN6, the **prognosis is more guarded** because JAGN1-deficient patients often respond poorly to G‑CSF, limiting the primary therapeutic tool’s effectiveness.[4][7][11][14] Boztug et al. note partial or complete refractoriness to rh‑G‑CSF in JAGN1-deficient patients, implying persisting neutropenia and infection risk despite treatment.[7][11] El‑Sayed et al.’s case report describes a child with recurrent infections and intracranial hemorrhage, highlighting severe morbidity.[3]

Life expectancy in SCN6 depends on **infection control, leukemic transformation, and access to HSCT**. Patients who undergo successful HSCT may achieve near-normal life expectancy, assuming complications are managed. Those who remain on G‑CSF or GM‑CSF alone may experience chronic morbidity and are at increased risk of MDS/AML and infection-related mortality. Precise survival statistics for SCN6 are not available due to small cohorts, but extrapolation from SCN suggests improved survival compared to historical controls, yet still lower than the general population.

### Morbidity, Disability, and Quality of Life

Morbidity in SCN6 includes **frequent severe infections**, chronic hospitalizations, growth failure, skeletal complications, endocrine deficiencies, and potential neurological sequelae.[3][7][9][11][15] These result in substantial disability, particularly in physical functioning and school participation. Osteoporosis and fractures can cause chronic pain, reduced mobility, and need for orthopedic interventions. Developmental delay may impact cognitive and social development. Pancreatic insufficiency and hypothyroidism require lifelong medication and monitoring.

Quality of life measures, though not systematically reported for SCN6, would likely show reduced scores in domains such as physical functioning, general health, and social functioning, similar to broader SCN cohorts but potentially more severe due to G‑CSF refractoriness.[9][10] HSCT can improve quality of life by correcting neutropenia, but introduces new challenges, including GVHD, immunosuppression, and transplant-related toxicity, which may themselves affect quality of life.

### Disease Course, Complications, and Predictive Factors

The disease course in SCN6 is marked by **complications** such as recurrent infections, chronic organ damage, and malignant transformation. Predictive factors of poor prognosis include very low ANC despite maximal G‑CSF therapy, frequent severe infections, evidence of clonal hematopoietic evolution (cytogenetic abnormalities), and presence of multisystem involvement.[6][9][11][15] Prognostic biomarkers may include cytogenetic changes in bone marrow cells, levels of ER stress markers, and specific mutations in secondary leukemia-associated genes.

G‑CSF refractoriness itself is a prognostic factor, indicating more severe intrinsic defects in CSF3R signaling and suggesting early HSCT consideration.[4][7][11][14] The presence of extra‑hematologic features such as pancreatic insufficiency, hypothyroidism, and skeletal abnormalities may signal broader systemic glycosylation defects, which could influence transplant outcomes and late effects.

## 12. Treatment

### Standard Pharmacologic Management: G‑CSF and GM‑CSF

The cornerstone of treatment for severe congenital neutropenia has been **recombinant human granulocyte colony-stimulating factor (G‑CSF; filgrastim)** since its approval by the FDA in 1991.[9][10] Filgrastim (NCIT:C40772) is a cytokine that binds CSF3R on myeloid progenitors and mature neutrophils, stimulating proliferation, differentiation, and survival. In most SCN patients, daily subcutaneous G‑CSF increases ANC and reduces infection frequency.[9][10] However, in SCN6 due to JAGN1 deficiency, patients often show **partial or complete refractoriness** to G‑CSF, reflecting decreased CSF3R expression and signaling due to glycosylation defects.[4][7][11][14] Boztug et al. report that JAGN1-deficient neutrophils have fewer G‑CSF receptors, and ClinVar submissions note poor response to recombinant human G‑CSF in patients with JAGN1 mutations.[4][7][11][14]

As a result, **GM‑CSF (granulocyte‑macrophage colony‑stimulating factor)** has been explored as an alternative or adjunctive therapy. El‑Sayed et al. state that GM‑CSF improves N‑glycosylation and is therefore used as a treatment for congenital neutropenia in JAGN1 mutation, suggesting that GM‑CSF may bypass some JAGN1-dependent defects or stimulate overlapping pathways that can partially compensate.[3] GM‑CSF (NCIT:C2113) binds its own receptor (CSF2R) and activates distinct signaling cascades. Clinical experience with GM‑CSF in SCN6 is limited but promising in select cases.

Antibiotics and antifungals are essential pharmacotherapies for treating infections. Empirical coverage often includes broad-spectrum antibiotics targeting Gram-positive and Gram-negative bacteria, with adjustments based on culture results. Antifungal agents such as voriconazole or amphotericin B are used for invasive fungal infections. Prophylactic regimens, including trimethoprim-sulfamethoxazole and antifungals, may be employed in patients with severe neutropenia and recurrent infections.

Pharmacogenomic considerations for G‑CSF and GM‑CSF in SCN6 primarily involve the **structural and functional status of CSF3R and JAGN1**, rather than drug metabolism genes. Genetic variants in CSF3R could further alter responsiveness, but this has not been systematically studied in JAGN1-deficient patients.

### Hematopoietic Stem Cell Transplantation and Cellular Therapies

Allogeneic **hematopoietic stem cell transplantation (HSCT; NCIT:C17394)** is the most definitive therapy for SCN6, capable of curing the neutropenia by replacing the patient’s hematopoietic system with donor stem cells that express functional JAGN1.[3][11][14] Boztug et al. note that JAGN1 deficiency is curable by HSCT, and ClinVar describes a patient with the c.35_43del variant who was successfully treated with bone marrow transplant at age 20.[11][14] HSCT eliminates the intrinsic neutrophil defect, normalizes ANC, and reduces infection-related morbidity. It also reduces the risk of MDS/AML arising from the defective hematopoietic clone.

HSCT requires careful donor selection (HLA-matched sibling or unrelated donor, haploidentical options), conditioning regimens, and management of GVHD and infections. In the context of SCN6, HSCT is typically considered when G‑CSF and GM‑CSF are insufficient to achieve acceptable ANC and infection control or when clonal evolution towards leukemia is detected. The timing of HSCT balances the risks of transplant-related mortality against those of ongoing severe neutropenia and leukemic transformation.

Emerging cellular therapies, such as autologous stem cell transplantation with gene-corrected cells (ex vivo gene therapy), remain experimental for SCN6. In theory, gene therapy using viral vectors or CRISPR-based gene editing to correct JAGN1 mutations in autologous hematopoietic stem cells could provide a curative option without GVHD risk. However, such approaches are in early stages and have not yet been applied clinically for JAGN1 deficiency.

### Supportive Care, Infection Prophylaxis, and Management of Comorbidities

Supportive care is a critical component of SCN6 management. This includes aggressive **infection prophylaxis**, such as vaccinations (e.g., pneumococcal, Haemophilus influenzae type b, meningococcal, influenza), prophylactic antibiotics and antifungals, and prompt treatment of febrile episodes. Growth and nutritional support, including caloric supplementation and pancreatic enzyme replacement in cases of pancreatic insufficiency, help address failure to thrive.[3][7][15] Hormone replacement for hypothyroidism (levothyroxine) and monitoring of endocrine status are necessary.

Bone health requires attention, with calcium and vitamin D supplementation, bisphosphonates in severe osteoporosis, and orthopedic interventions for fractures.[3][7] Physical and occupational therapy can improve mobility and reduce disability. Psychosocial support for patients and families aids coping with chronic illness. In HSCT recipients, long-term follow‑up for GVHD, secondary malignancies, and organ function is essential.

### Emerging and Experimental Therapeutic Strategies

Experimental approaches include **calpain inhibitors** and modulators of calcium signaling as potential therapies for SCN6, based on Khandagale’s findings that calpain inhibition prevents mutant JAGN1-induced cell death.[6][10] The specific calpain inhibitor PD150606 blocked calpain-mediated cell death in HL‑60 cells expressing mutant JAGN1, suggesting that pharmacologic calpain inhibition could ameliorate neutrophil loss.[6][10] Translating this to clinical therapy would require careful evaluation of systemic effects and off-target consequences.

Therapies targeting ER stress, such as chemical chaperones (e.g., 4‑phenylbutyrate) or modulators of unfolded protein response, might theoretically reduce ER stress in JAGN1-deficient cells and mitigate downstream damage. Agents that enhance glycosylation capacity or optimize secretory pathway function could also be explored. Gene therapy approaches, as mentioned, represent a long-term goal.

### Personalized and Precision Medicine Approaches

Personalized management of SCN6 rests on **genotype-guided diagnosis and treatment**, considering specific JAGN1 variants, degree of G‑CSF refractoriness, and presence of extra‑hematologic features. Genetic testing informs prognosis and HSCT candidacy. For example, patients with variants that severely disrupt JAGN1 function and show profound G‑CSF refractoriness may be candidates for earlier HSCT. Those with milder variants and partial G‑CSF response may benefit from extended pharmacologic management.

Precision medicine may also involve monitoring biomarkers of ER stress, glycosylation, and calpain activity to tailor therapies such as GM‑CSF, calpain inhibitors, or ER stress modulators. As multi‑omics data accumulate, individualized risk profiles for leukemia and organ complications could be generated, guiding surveillance intensity and preventive interventions.

## 13. Prevention

### Primary, Secondary, and Tertiary Prevention

Given the Mendelian etiology, **primary prevention** of SCN6 focuses on **genetic counseling and reproductive planning**. In families with known JAGN1 mutations, carrier testing of parents and potential reproductive partners can inform risk of having affected children.[5][11][15] Prenatal diagnosis through chorionic villus sampling or amniocentesis, and preimplantation genetic diagnosis in the context of in vitro fertilization, allow couples to avoid the birth of affected children if they so choose. Public health-level primary prevention is limited by the rarity of SCN6, but targeted education in communities with high consanguinity may raise awareness of autosomal recessive diseases.

**Secondary prevention** involves early detection and intervention in affected individuals to prevent complications. Newborns and infants with recurrent infections should be evaluated for neutropenia, and if severe congenital neutropenia is identified, genetic testing for JAGN1 and other SCN genes should be pursued promptly.[4][6][9][11] Early institution of infection prophylaxis, G‑CSF or GM‑CSF therapy, and monitoring for leukemia can reduce morbidity and mortality. In families with known SCN6, early testing of siblings and relatives can detect asymptomatic or minimally symptomatic neutropenia before severe infections occur.

**Tertiary prevention** aims to prevent complications in those already affected, such as recurrent infections, organ damage, and leukemic transformation. This includes rigorous infection prophylaxis, management of skeletal and endocrine complications, and timely HSCT to prevent progression to MDS/AML. Rehabilitation services help mitigate disability from fractures and developmental delay. Psychological support and social interventions reduce secondary mental health complications.

### Immunization, Screening, and Counseling

Immunization strategies follow standard pediatric schedules, with emphasis on vaccines that prevent bacterial infections (e.g., pneumococcal conjugate, Hib, meningococcal) and influenza.[9] Live vaccines may be used cautiously, depending on the degree of immunosuppression, but SCN6 does not inherently involve T‑cell defects. Screening for SCN6 in the general population is not currently recommended, but targeted screening in high-risk families and consanguineous communities may be considered.

Genetic counseling is crucial, providing information on autosomal recessive inheritance, carrier risk, reproductive options, and implications for family members. Counselors can guide decisions about prenatal testing and preimplantation genetic diagnosis. Counseling also addresses psychosocial aspects of living with a rare, chronic immunodeficiency.

Public health interventions, such as improving sanitation, access to antibiotics, and healthcare infrastructure, indirectly benefit SCN6 patients by reducing infection exposure and improving treatment availability. Environmental interventions, such as reducing indoor air pollution and improving ventilation, may reduce respiratory infection risk.

Prophylactic medications, including antibiotics and antifungals, represent pharmacologic prevention of infections in SCN6. Prophylactic G‑CSF or GM‑CSF can be viewed as pharmacologic prophylaxis against neutropenic complications. HSCT, while therapeutic, also functions as a preventive measure against future infections and leukemia.

## 14. Other Species / Natural Disease

### Orthologous Genes and Comparative Biology

JAGN1 has **orthologs in other species**, including Drosophila melanogaster, where the gene *jagunal* was first described as required for reorganizing the endoplasmic reticulum during oogenesis.[13] In Drosophila, jagunal encodes a conserved ER membrane protein that facilitates ER clustering and vesicular traffic to the oocyte lateral membrane. Loss of jagunal reduces vesicular traffic and slows cell growth, demonstrating a key role in secretory pathway function.[13] This evolutionary conservation supports the idea that JAGN1 plays similar roles in ER organization and secretory trafficking in mammalian cells, including human neutrophils.[8][11][13]

NCBI Gene lists JAGN1 orthologs across multiple species, although detailed functional studies beyond Drosophila are limited.[8] In mice and other vertebrates, Jagn1 homologs likely exist and function in ER and secretory pathways, but specific knockout or mutant models have not yet been widely reported in the literature.

### Natural Disease in Other Species and Comparative Pathology

Natural disease analogous to SCN6 has not been widely documented in companion animals or livestock. Neutropenia occurs in veterinary medicine due to infections, drugs, and autoimmune conditions, but JAGN1 mutations have not been reported as a cause. Online Mendelian Inheritance in Animals (OMIA) does not currently list JAGN1-associated neutropenia, reflecting either true rarity or lack of investigation. Comparative pathology thus focuses more on the conserved cellular mechanisms of ER and secretory pathway function rather than specific disease entities.

Drosophila jagunal mutants provide a **comparative model** for studying ER organization and vesicular traffic, which can be extrapolated to human cell biology. The failure of ER clustering and reduced vesicular traffic in jagunal mutants parallels ER disorganization and secretory defects in JAGN1-deficient neutrophils.[11][13] These insights reinforce the role of ER architecture in cell growth and function across species.

Transmission of SCN6 across species is not applicable; the disease is a human Mendelian disorder without zoonotic potential. Cross-species susceptibility to JAGN1-associated defects would require germline mutations in orthologous genes, which have not been described.

## 15. Model Organisms and Experimental Systems

### Cellular Models

Cellular models have been central to elucidating SCN6 mechanisms. The **HL‑60 human promyelocytic leukemia cell line** has been used to study the effects of mutant JAGN1 overexpression and JAGN1 silencing.[6][10] Khandagale et al. transduced HL‑60 cells with patient-derived JAGN1 mutants and observed increased cell death upon pro‑apoptotic and degranulation stimuli, mediated by calcium and calpain.[6][10] Silencing JAGN1 with siRNA did not replicate this phenotype, suggesting that mutant JAGN1 confers a dominant pathophysiologic effect in this system.[6][10]

Primary cells from patients, including **neutrophils and bone marrow myeloid cells**, have also been studied. Boztug et al. examined JAGN1-deficient neutrophil granulocytes and observed increased apoptosis in response to TNFα and staurosporine, defective secretory pathway function, and altered granule morphology.[7][11] These patient-derived cells provide the most physiologically relevant model for JAGN1 deficiency, though access is limited.

### Invertebrate Models: Drosophila jagunal

Drosophila melanogaster serves as an invertebrate model for JAGN1 ortholog function. *Jagunal* mutants demonstrate ER clustering defects and reduced vesicular traffic during oogenesis, providing a robust model for ER organization and secretory pathway biology.[13] While Drosophila does not have neutrophils, the principles of ER clustering and vesicle-mediated transport are conserved, allowing mechanistic extrapolation. Genetic tools in Drosophila (GAL4/UAS, CRISPR) can be used to manipulate jagunal expression and study interactions with other secretory pathway components.

### Prospects for Mammalian Models and Disease Modeling

Mammalian models, such as **mouse Jagn1 knockout or knock-in models**, would be highly valuable for studying SCN6 pathophysiology and testing therapies, but detailed reports of such models are not yet prominent in the literature. Given JAGN1’s ubiquitous expression but neutrophil-specific phenotype, a Jagn1 knockout mouse might exhibit neutropenia and infection susceptibility, though species differences may exist. Conditional knockout models targeting hematopoietic cells could clarify cell-type-specific roles.

Induced pluripotent stem cell (iPSC) models, where patient-derived iPSCs are differentiated into neutrophil-like cells, represent another avenue for modeling JAGN1 deficiency. Such models would allow detailed analysis of ER stress, glycosylation, and cell death pathways in a controlled, human cell context.

### Applications of Models in Mechanistic and Therapeutic Research

Models have been used to elucidate **mechanisms of ER stress, glycosylation defects, and calpain-mediated cell death** in JAGN1 deficiency, as described above.[3][6][10][11][13] Future applications include screening libraries of small molecules to identify compounds that ameliorate ER stress or calpain activation in mutant JAGN1-expressing cells. CRISPR-based functional genomics screens could identify genes that modulate sensitivity to mutant JAGN1, revealing potential drug targets.

In vivo models, once developed, would permit testing of therapies such as calpain inhibitors, ER stress modulators, and gene therapy. They would also allow study of systemic manifestations, including bone and pancreatic abnormalities, which are difficult to model in cell lines alone.

## Conclusion

Severe congenital neutropenia 6, autosomal recessive (SCN6), caused by biallelic mutations in the **JAGN1** gene, exemplifies a rare but mechanistically illuminating primary immunodeficiency that links endoplasmic reticulum organization, secretory pathway function, protein glycosylation, and calcium‑dependent cell death to the clinical phenotype of profound neutropenia and recurrent, life‑threatening infections.[1][4][5][6][8][9][10][11][12][14][15] At the molecular level, JAGN1 deficiency disrupts ER architecture and N‑glycosylation, leading to defective CSF3R expression and signaling, ER stress, and heightened susceptibility of myeloid cells to calpain‑mediated, non‑apoptotic cell death upon activation.[3][6][7][11][13] These upstream lesions manifest as bone marrow granulopoiesis maturation arrest and severe chronic neutropenia, which in turn cause recurrent bacterial and fungal infections, increased risk of myelodysplastic syndrome and acute myeloid leukemia, and a constellation of extra‑hematologic features including growth failure, skeletal abnormalities, endocrine and pancreatic dysfunction, and vascular anomalies.[3][4][7][9][11][15]

Clinically, SCN6 is distinguished from other SCN subtypes by its autosomal recessive inheritance, poor or erratic response to G‑CSF due to CSF3R glycosylation defects, and curability with hematopoietic stem cell transplantation, which replaces the defective hematopoietic compartment with donor cells expressing functional JAGN1.[4][7][10][11][14] Diagnosis relies on recognition of severe congenital neutropenia, bone marrow maturation arrest, and genetic confirmation of JAGN1 mutations via targeted sequencing or exome analysis.[4][6][11][12][14] Management involves aggressive infection prophylaxis, trial of G‑CSF and GM‑CSF, and timely consideration of HSCT, along with supportive care for multisystem complications.[3][7][9][11][15]

From a research perspective, SCN6 has spurred advances in understanding myeloid cell biology, ER stress, and calpain-dependent cell death, with experimental models such as HL‑60 cells expressing mutant JAGN1 and Drosophila jagunal mutants providing mechanistic insight.[6][10][11][13] Future work will likely focus on developing mammalian models, refining our understanding of systemic glycosylation defects, and exploring novel therapeutic strategies such as calpain inhibitors, ER stress modulators, and gene therapy. As multi‑omics approaches and precision medicine evolve, integrating genomic, transcriptomic, proteomic, and functional data will further elucidate the pathophysiology of JAGN1 deficiency and improve prognostication and treatment for affected individuals.

In sum, SCN6 illustrates how a single gene defect in an ER-resident protein can have far-reaching consequences across molecular, cellular, tissue, and clinical levels, and how careful integration of clinical observation, genomic discovery, and experimental modeling can transform a previously unexplained neutropenia into a well-defined, mechanistically understood Mendelian disorder.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 65 |
| Resolved | 57 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 6 |
| Terms whose name was checked | 45 |
| Terms named correctly | 22 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 14 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0005532` (1 mention) - the report calls it "Severe neutropenia"; HP calls it **Macrocytic dyserythropoietic anemia**
- `HP:0001678` (2 mentions) - the report calls it "Bone marrow maturation arrest"; HP calls it **Atrioventricular block**
- `HP:0001919` (1 mention) - the report calls it "Abnormal myelopoiesis"; HP calls it **Acute kidney injury**
- `HP:0002723` (1 mention) - the report calls it "Sepsis"; HP calls it **Absence of bactericidal oxidative respiratory burst in phagocytes**
- `HP:0005411` (1 mention) - the report calls it "Impaired neutrophil chemotaxis"; HP calls it **Chronic intestinal candidiasis**
- `HP:0006520` (1 mention) - the report calls it "Frequent hospitalizations"; HP calls it **Progressive pulmonary function impairment**
- `HP:0000736` (1 mention) - the report calls it "Reduced social interaction"; HP calls it **Short attention span**
- `UBERON:0001741` (2 mentions) - the report calls it "bone marrow"; UBERON calls it **corniculate cartilage**
- `GO:0005544` (1 mention) - the report calls it "calpain-mediated signaling"; GO calls it **calcium-dependent phospholipid binding**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006486` (obsolete protein glycosylation) (1 mention) - replaced by `GO:0009101`
- `NCIT:C2113` (Miscellaneous Chemoprotective Agent) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001875` (2 mentions) - the report calls it "Neutropenia", "Decreased total neutrophil count"; HP calls it **Decreased total neutrophil count**, and lists "Neutropenia" among its other names
- `HP:0002719` (1 mention) - the report calls it "Recurrent bacterial infections"; HP calls it **Recurrent infections**
- `HP:0002718` (1 mention) - the report calls it "Recurrent skin infections"; HP calls it **Recurrent bacterial infections**, and lists "Recurrent pyogenic infections" among its other names
- `HP:0002721` (1 mention) - the report calls it "Primary immunodeficiency"; HP calls it **Immunodeficiency**
- `HP:0002757` (1 mention) - the report calls it "Pathologic fractures"; HP calls it **Recurrent fractures**, and lists "Multiple fractures" among its other names
- `HP:0001680` (1 mention) - the report calls it "Coarctation of the aorta"; HP calls it **Coarctation of aorta**, and lists "Coarctation of the aorta" among its other names
- `HP:0012378` (1 mention) - the report calls it "Chronic fatigue"; HP calls it **Fatigue**
- `GO:0006486` (1 mention) - the report calls it "protein glycosylation"; GO calls it **obsolete protein glycosylation**
- `GO:0005788` (1 mention) - the report calls it "endoplasmic reticulum organization"; GO calls it **endoplasmic reticulum lumen**
- `CL:0000048` (3 mentions) - the report calls it "myeloid progenitor cell"; CL calls it **multi fate stem cell**, and lists "multipotent cell" among its other names
- `GO:0008219` (1 mention) - the report calls it "calcium‑dependent cell death"; GO calls it **cell death**, and lists "accidental cell death" among its other names
- `GO:0005739` (1 mention) - the report calls it "mitochondria"; GO calls it **mitochondrion**, and lists "mitochondria" among its other names
- `GO:0045649` (1 mention) - the report calls it "negative regulation of neutrophil differentiation"; GO calls it **regulation of macrophage differentiation**
- `CL:0000038` (1 mention) - the report calls it "hematopoietic stem cell"; CL calls it **erythroid progenitor cell**, and lists "erythroid stem cell" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001875` - called "Neutropenia", "Decreased total neutrophil count"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `ID`.