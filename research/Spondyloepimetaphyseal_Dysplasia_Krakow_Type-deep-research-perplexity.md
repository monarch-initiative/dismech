---
provider: perplexity
model: sonar-reasoning-pro
cached: false
start_time: '2026-09-15T20:27:04.342786'
end_time: '2026-09-15T20:29:52.306086'
duration_seconds: 167.96
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spondyloepimetaphyseal Dysplasia Krakow Type
  mondo_id: MONDO:0032571
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
citation_count: 15
reference_validation:
  total_references: 1
  verified: 1
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 1
  on_topic: 0
  validator_version: 0.2.1
term_validation:
  total_terms: 44
  verified: 40
  not_found: 1
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.024
  labels_checked: 37
  labels_matching: 13
  labels_mismatched: 18
  mislabelled_terms:
  - term_id: HP:0002650
    reported_labels:
    - Spondyloepimetaphyseal dysplasia
    - Key HPO terms:** Spondyloepimetaphyseal dysplasia
    ontology_label: Scoliosis
  - term_id: HP:0000947
    reported_labels:
    - Abnormal metaphysis morphology
    ontology_label: Dumbbell-shaped long bone
  - term_id: HP:0008964
    reported_labels:
    - Rhizomelia
    ontology_label: Nonprogressive muscular atrophy
  - term_id: HP:0003002
    reported_labels:
    - Bowing of long bones
    ontology_label: Breast carcinoma
  - term_id: GO:0030212
    reported_labels:
    - Chondrocyte differentiation
    ontology_label: hyaluronan metabolic process
  - term_id: CL:0000120
    reported_labels:
    - Osteoblast
    ontology_label: granule cell
  - term_id: UBERON:0002413
    reported_labels:
    - 'Suggested UBERON: Vertebral column'
    - UBERON anatomical locations:** Vertebral column
    ontology_label: cervical vertebra
  - term_id: UBERON:0002445
    reported_labels:
    - 'Suggested UBERON: Long bone'
    ontology_label: ulnare
  - term_id: UBERON:0003840
    reported_labels:
    - Epiphysis of long bone
    ontology_label: hindlimb joint
  - term_id: UBERON:0003841
    reported_labels:
    - Metaphysis of long bone
    ontology_label: autopod joint
  - term_id: UBERON:0002106
    reported_labels:
    - 'Suggested UBERON: Spleen'
    ontology_label: spleen
  - term_id: UBERON:0002048
    reported_labels:
    - 'Suggested UBERON: Lung'
    ontology_label: lung
  - term_id: UBERON:0002414
    reported_labels:
    - 'Suggested UBERON: Hyaline cartilage'
    ontology_label: lumbar vertebra
  - term_id: CL:0000121
    reported_labels:
    - Osteoclast
    ontology_label: Purkinje cell
  - term_id: NCIT:C77209
    reported_labels:
    - 'Suggested NCIT terms: Antibiotic Therapy'
    ontology_label: CHFR Gene
  - term_id: NCIT:C15410
    reported_labels:
    - 'Suggested NCIT: Immunoglobulin Replacement Therapy'
    ontology_label: Biological Response Modifier Therapy
  - term_id: NCIT:C15273
    reported_labels:
    - 'Suggested NCIT: Orthopedic Surgery Procedure'
    - NCIT interventions:** Orthopedic Surgery Procedure
    ontology_label: Longitudinal Study
  - term_id: NCIT:C15429
    reported_labels:
    - 'Suggested NCIT: Physical Therapy'
    ontology_label: Research Activity
  labels_variant: 6
  unresolved_terms:
  - HP:0010572
  obsolete_terms:
  - term_id: NCIT:C15410
    ontology_label: Biological Response Modifier Therapy
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spondyloepimetaphyseal Dysplasia Krakow Type
- **MONDO ID:** MONDO:0032571 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spondyloepimetaphyseal Dysplasia Krakow Type** covering all of the
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

Spondyloepimetaphyseal dysplasia, Krakow type (SEMDK) is an ultra‑rare, autosomal recessive immuno‑osseous skeletal dysplasia caused by biallelic missense mutation in the serine/threonine kinase gene SIK3 and characterized by severe spondyloepimetaphyseal skeletal changes, profound immunodeficiency, and developmental delay.[1][3][4][10][12] Only a single nuclear family with two affected siblings has been reported in detail to date, so most knowledge derives from that case report and aggregated database summaries.[1][3][10][13]

---

## 1. Disease Information

**Definition and overview**

SEMDK is a Mendelian skeletal dysplasia within the spondyloepimetaphyseal dysplasia group, distinguished by the combination of severe vertebral, epiphyseal and metaphyseal abnormalities, rhizomelia and mesomelia with pronounced anterior bowing of long bones, severe primary immunodeficiency, and global developmental delay.[1][3][4][5][13] The condition has been described in two siblings from a consanguineous family, establishing it as a recessive immuno‑osseous dysplasia rather than a purely skeletal disorder.[1][10][13]

**Key identifiers**

- OMIM: 618162 – “Spondyloepimetaphyseal dysplasia, Krakow type; SEMDK”.[1][8][9]  
- MONDO: MONDO:0032571 – “spondyloepimetaphyseal dysplasia, Krakow type”.[7][12]  
- MedGen Concept ID: 1648323 – “Spondyloepimetaphyseal dysplasia, Krakow type”.[2][4]  
- UniProt disease ID: DI‑05362 – “Spondyloepimetaphyseal dysplasia, Krakow type”.[11]  
- KEGG disease: H02187 – “Spondyloepimetaphyseal dysplasia (includes SEMD Krakow type as a subtype)”.[14]

No dedicated ICD‑10/ICD‑11 or MeSH term has been identified; SEMDK is typically grouped under broader categories for congenital skeletal dysplasia and primary immunodeficiency in coding systems.[1][2][3]

**Synonyms and alternative names**

- Spondyloepimetaphyseal dysplasia, Krakow type (SEMDK).[1][3][4][5]  
- Immunoosseous dysplasia, Krakow type.[5][13]  
- Spondylo‑epi‑metaphyseal dysplasia, Krakow type.[13]  

**Source type**

The core clinical and genetic information comes from an individual family case report (human clinical evidence; Csukasi et al., 2018, PMID:30232230) and is aggregated in disease‑level resources such as OMIM, MedGen, MalaCards, rarediseases.org, KEGG, UniProt and PanelApp.[1][3][4][5][10][11][12][13]

---

## 2. Etiology

### Disease causal factors

**Genetic cause**

SEMDK is caused by homozygous germline missense mutation in SIK3 (salt‑inducible kinase 3), a serine/threonine protein kinase located on chromosome 11q23.3.[1][6][10][12]  

- OMIM 618162 assigns a “number sign” to the phenotype, indicating causation by SIK3 mutation and notes autosomal recessive inheritance.[1]  
- The reported pathogenic variant is NM_001366686.3(SIK3):c.559C>T, resulting in p.Arg187Cys in the canonical SIK3 isoform; the original case report described the same change as p.Arg129Cys in an alternative isoform.[1][6][10]  
- ClinVar classifies NM_001366686.3(SIK3):c.559C>T (p.Arg187Cys) as pathogenic for SEMDK, with germline origin and single‑nucleotide variant type.[6]  

SIK3 (HGNC:28980; OMIM:614776) encodes a member of the salt‑inducible kinase family involved in regulation of CREB‑dependent transcription and cartilage and bone growth plate function, providing a plausible mechanistic link to skeletal development and potentially immune cell function.[1][10][11]

No non‑genetic primary causes (environmental, infectious, toxic) have been implicated.[1][3][10]

### Genetic risk factors

- **Causal variant:** Homozygous SIK3 c.559C>T (p.Arg187Cys/p.Arg129Cys) is the only variant reported to date in association with SEMDK.[1][6][10]  
- **Inheritance:** Autosomal recessive; both affected siblings in the reported family were homozygous for the variant, with heterozygous carrier parents.[1][10][12]  
- **Allele frequency:** The variant was absent from major population databases at the time of publication and is treated as private to the family; databases summarizing the case note no population frequency data.[1][6][10]  
- **Consanguinity:** The original family was consanguineous, suggesting parental relatedness as a risk factor for homozygosity of a rare deleterious allele (human clinical evidence).[1][10][13]  

No susceptibility loci or modifier genes have been described; the evidence base is limited to a single pedigree.[1][3][10]

### Environmental risk factors

No specific environmental, lifestyle, occupational, or infectious risk factors have been linked to disease onset; the condition appears fully penetrant in the presence of biallelic SIK3 mutation.[1][3][10]

### Protective factors

No genetic or environmental protective factors have been reported for SEMDK.[1][3][10]

### Gene–environment interactions

No gene–environment interaction data are currently available for SEMDK.[1][3][10] Management recommendations emphasize minimizing infectious exposures due to underlying immunodeficiency, but this relates to prognosis rather than disease causation.[10]

---

## 3. Phenotypes

Available phenotype information is derived from the two affected siblings and summarized consistently across OMIM, MedGen, MalaCards, rarediseases.org and case‑based literature.[1][3][4][5][13]

### Core skeletal phenotypes (symptoms/signs)

- **Severe spondyloepimetaphyseal dysplasia**: Involvement of vertebral bodies, epiphyses and metaphyses with marked growth plate abnormalities.[1][3][13]  
  - Type: Clinical signs/physical manifestations (radiographic and morphologic).  
  - Onset: Congenital/early infancy (radiographs abnormal from early life).[1][13]  
  - Severity: Severe, leading to disproportionate short stature.[1][3][13]  
  - Progression: Progressive bone deformity during growth.[1][3][13]  
  - Frequency: Present in all described affected individuals (2/2) – ~100% in known cases.[1][3][13]  
  - Quality of life impact: Major impairment of mobility, growth, and musculoskeletal function (inferred from severity of dysplasia).[1][3][13]  
  - Suggested HPO:  
    - Spondyloepimetaphyseal dysplasia (HP:0002650).  
    - Abnormal epiphysis morphology (HP:0010572).  
    - Abnormal metaphysis morphology (HP:0000947).  
    - Platyspondyly (HP:0000926).

- **Rhizomelia and mesomelia with anterior bowing of limbs**: Proximal and middle limb segment shortening and pronounced anterior bowing of long bones.[3][13]  
  - Type: Physical manifestations.  
  - Onset: Recognizable in infancy.[13]  
  - Severity: Marked limb deformity.[3][13]  
  - Progression: Structural; may worsen as growth proceeds (inferred).  
  - Frequency: Present in the reported siblings.[3][13]  
  - Quality of life impact: Limits ambulation; may require orthopedic support (inferred).[13]  
  - Suggested HPO:  
    - Rhizomelia (HP:0008964).  
    - Mesomelia (HP:0003027).  
    - Bowing of long bones (HP:0003002).  

- **Severe short stature/dwarfism**: Height markedly below age norms due to skeletal dysplasia.[1][3][13]  
  - Type: Symptom/clinical sign.  
  - Onset: Early childhood.[1][13]  
  - Severity: Severe (proportionate to skeletal involvement).[1][3]  
  - Progression: Persistent; likely worsens with age relative to peers.  
  - Frequency: Universal in affected siblings.[1][3][13]  
  - Quality of life impact: Functional limitations, psychosocial impact (inferred).  
  - Suggested HPO: Short stature (HP:0004322).

### Immune and infection‑related phenotypes

- **Severe immunodeficiency**: Profound primary immunodeficiency with recurrent, severe infections.[1][3][4][5][10][13]  
  - Type: Clinical sign/laboratory abnormality.  
  - Onset: Early childhood, with severe infections occurring in infancy/early childhood.[1][10][13]  
  - Severity: Severe; one child reportedly died from infection‑related complications (human clinical evidence).[1][10][13]  
  - Progression: Persistent; no spontaneous remission described.[1][3][10]  
  - Frequency: Universal in reported cases.[1][3][10][13]  
  - Quality of life impact: Life‑threatening; major morbidity due to recurrent infections.[1][3][10][13]  
  - Suggested HPO:  
    - Primary immunodeficiency (HP:0002721).  
    - Recurrent infections (HP:0002719).  
    - Recurrent respiratory infections (HP:0002205).

### Neurodevelopmental phenotypes

- **Global developmental delay**: Delayed attainment of developmental milestones.[1][3][4][5][13]  
  - Type: Behavioral/neurological symptom.  
  - Onset: Recognized in infancy/early childhood.[1][13]  
  - Severity: Moderate to severe (inferred from description of “developmental delay”).[1][3]  
  - Progression: Persistent; no evidence for catch‑up.[1][3]  
  - Frequency: Present in both affected siblings.[1][3][13]  
  - Quality of life impact: Significant impact on independence and learning (inferred).  
  - Suggested HPO: Global developmental delay (HP:0001263).

### Other possible features

Database summaries suggest involvement of endocrine and neurologic manifestations in the clinical spectrum, but detailed phenotyping beyond skeletal, immunological and developmental domains is limited in published sources.[3][10][13]  

Quality‑of‑life and standardized patient‑reported outcome measures (EQ‑5D, SF‑36) have not been formally reported for SEMDK.[1][3][10]

---

## 4. Genetic/Molecular Information

### Causal gene

- **Gene:** SIK3 (Salt‑Inducible Kinase 3).  
  - OMIM gene ID: 614776.[1]  
  - HGNC ID: 28980 (standard gene catalog; general knowledge).  
  - Cytogenetic location: 11q23.3.[1][6][10]  
  - SIK3 is a protein‑coding serine/threonine kinase of the AMPK family, implicated in regulation of CREB/CRTC transcription and endochondral bone growth.[1][10][11]

### Pathogenic variants

- **Reported variant:** NM_001366686.3(SIK3):c.559C>T (p.Arg187Cys) – single‑nucleotide missense variant.[6][10]  
  - ClinVar classification: Pathogenic, germline.[6]  
  - Type: Missense SNV.[6]  
  - Disease association: Spondyloepimetaphyseal dysplasia, Krakow type.[6][10][12]  
- **Isoform notation:** The original case report describes the same substitution as p.Arg129Cys in a shorter SIK3 isoform; OMIM notes this and links the variant to SEMDK.[1][10]  
- **Allele frequency:** Not found in large population datasets at time of reporting, consistent with an ultra‑rare, private variant.[1][6][10]  
- **Functional consequence:** The variant is inferred to be loss‑of‑function or hypomorphic, disrupting SIK3 kinase activity in growth plate chondrocytes and possibly immune cells.[1][10][11] This is inferred from the gene’s known role rather than direct biochemical data in SEMDK.

No other SIK3 variants or other genes have been definitively associated with SEMDK, and SIK3 remains the sole gene with moderate evidence for the phenotype in curated panels.[1][10][12]

### Modifier genes and epigenetic information

No modifier genes or epigenetic alterations have been described for SEMDK.[1][3][10]  

### Chromosomal abnormalities

No chromosomal structural changes (aneuploidy, translocations, CNVs) are reported in association with SEMDK; the disease is due to a single missense variant in an otherwise structurally normal chromosome.[1][6][10]

---

## 5. Environmental Information

Published information and database summaries do not identify specific environmental, toxic, occupational, or lifestyle factors that contribute to SEMDK risk or severity.[1][3][10]  

Given the primary immunodeficiency, clinicians recommend minimizing infectious exposures and using standard infection prophylaxis strategies, but this is supportive management rather than a disease cause.[10]

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (with inferred steps noted)

1. **Biallelic SIK3 missense mutation (c.559C>T, p.Arg187Cys) leads to altered SIK3 kinase structure and activity in growth plate chondrocytes and immune cells** (inferred from kinase domain location and gene function).[1][6][10][11]  
2. **Impaired SIK3 signaling leads to dysregulation of CREB/CRTC‑dependent transcription and other downstream pathways controlling chondrocyte proliferation and hypertrophy** (inferred from general SIK3 biology).[11]  
3. **Abnormal chondrocyte differentiation and endochondral ossification result in defective vertebral, epiphyseal and metaphyseal development, leading to spondyloepimetaphyseal dysplasia with rhizomelia, mesomelia and bowed limbs.**[1][3][13]  
4. **Defective SIK3 function in immune cells (e.g., B/T lymphocytes) leads to impaired immune signaling and lymphocyte maturation, resulting in severe primary immunodeficiency with recurrent infections** (inferred; human clinical evidence of immunodeficiency without detailed cellular work‑up).[1][3][10][13]  
5. **Chronic skeletal deformity and impaired growth plate function lead to severe short stature and musculoskeletal disability.**[1][3][13]  
6. **Recurrent severe infections and immunodeficiency result in high morbidity and at least one early childhood death, defining the prognosis of SEMDK.**[1][10][13]  
7. **Global developmental delay may result from a combination of systemic illness, possible direct CNS effects of SIK3 dysfunction, and musculoskeletal limitations** (largely inferred; human clinical evidence for delay).[1][3][13]

### Molecular pathways (inferred from SIK3 biology)

- SIK3 belongs to the **AMPK‑related kinase family** and regulates transcription via phosphorylation of CRTC and class IIa histone deacetylases, affecting **CREB‑dependent gene expression** in multiple tissues.[11]  
- In cartilage, SIK3 is implicated in **endochondral bone growth and growth plate maturation**, linking it to pathways controlling chondrocyte hypertrophy and ossification (e.g., PTHrP–IHH axis, Wnt signaling) by modulation of transcription factors.[11][14]  
- Direct mapping of SEMDK to specific curated pathways (e.g., KEGG, Reactome) has not yet been reported; KEGG lists SEMD (including Krakow type) as a heterogeneous group of dwarfing disorders associated with multiple genes.[14]

Suggested GO biological process terms:  
- Endochondral bone morphogenesis (GO:0060350).  
- Cartilage development (GO:0051216).  
- Chondrocyte differentiation (GO:0030212).  
- Immune system process (GO:0002376).  

### Cellular processes

- **Chondrocyte proliferation and hypertrophy**: SIK3 dysfunction is inferred to disturb normal growth plate chondrocyte proliferation and maturation, leading to disorganized columns and abnormal ossification.[11][14]  
- **Immune cell development and signaling**: The severe immunodeficiency suggests disrupted lymphocyte function, possibly via altered transcriptional programs in B and T cells; however, specific defects (e.g., class‑switched memory B cells) have not been characterized.[1][3][10]  

Suggested CL cell types:  
- Growth plate chondrocyte (CL:0000138).  
- Osteoblast (CL:0000120).  
- B cell (CL:0000236).  
- T cell (CL:0000084).

### Protein dysfunction

- The disease‑causing variant lies in the N‑terminal kinase domain of SIK3, and a missense substitution of a conserved arginine is expected to perturb ATP binding or substrate interaction, causing reduced or aberrant kinase activity (inferred).[6][11]  
- UniProt annotates SIK3 as a serine/threonine kinase with regulatory roles in transcription and metabolism, supporting the idea that missense mutation leads to **loss‑of‑function or hypomorphic activity**.[11]

### Metabolic and biochemical changes

No direct metabolomic or biochemical profiling data are available for SEMDK; any changes are inferred to be downstream of disrupted growth plate biology and immune cell function.[1][3][10]

### Immune system involvement

- Severe, recurrent infections and immunodeficiency are core features of SEMDK, indicating a major **immune system involvement**.[1][3][4][5][10][13]  
- The specific immunologic defect (humoral, cellular, combined) has not been described in detail; published summaries simply report “severe immunodeficiency”.[1][3][5][10]

Suggested GO terms:  
- Adaptive immune response (GO:0002250).  
- Lymphocyte activation (GO:0046649).  

### Tissue damage mechanisms

- Skeletal tissues: Chronic mechanical stress on malformed bones leads to secondary joint damage and pain (inferred from general skeletal dysplasia pathology).[1][3][13]  
- Immune system: Recurrent infections cause inflammatory damage in lungs and other organs; in the reported family, infection‑related complications contributed to mortality.[1][10][13]

### Epigenetic, molecular profiling, and advanced technologies

No epigenetic, transcriptomic, proteomic, metabolomic, single‑cell, spatial transcriptomic or functional genomics studies are available for SEMDK specifically.[1][3][10][11] Studies of SIK3 in other contexts support its role in transcriptional regulation and cartilage biology, but these have not yet been integrated as disease‑specific multi‑omics in SEMDK.[11][14]

---

## 7. Anatomical Structures Affected

### Organ‑level

Primary organs and systems:

- **Axial skeleton (vertebral column)**: Platyspondyly and vertebral abnormalities.[1][3][13]  
  - Suggested UBERON: Vertebral column (UBERON:0002413).  
- **Appendicular skeleton (long bones and joints)**: Rhizomelic and mesomelic shortening; bowed long bones; abnormal epiphyses and metaphyses.[1][3][13]  
  - Suggested UBERON: Long bone (UBERON:0002445).  
  - Epiphysis of long bone (UBERON:0003840).  
  - Metaphysis of long bone (UBERON:0003841).  
- **Immune system organs**: Likely involvement of lymphoid tissues (bone marrow, thymus, spleen, lymph nodes) associated with immunodeficiency, although specific organ pathology is not described.[1][3][10]  
  - Suggested UBERON: Spleen (UBERON:0002106); Thymus (UBERON:0002370); Lymph node (UBERON:0000029).

Secondary involvement:

- **Respiratory system**: Recurrent respiratory infections and pneumonia due to immunodeficiency.[1][10][13]  
  - Suggested UBERON: Lung (UBERON:0002048).  
- **Neurological system**: Global developmental delay implies CNS functional involvement, though structural brain abnormalities are not reported.[1][3][13]  

### Tissue and cell level

- **Tissues:** Cartilage and bone (growth plate cartilage, subchondral bone) and lymphoid tissues.[1][3][10][13]  
  - Suggested UBERON: Hyaline cartilage (UBERON:0002414); Bone tissue (UBERON:0002481).  
- **Cells:** Growth plate chondrocytes, osteoblasts, osteoclasts, and lymphocytes (B and T cells).[11][14]  

Suggested CL terms:  
- Chondrocyte (CL:0000138).  
- Osteoblast (CL:0000120).  
- Osteoclast (CL:0000121).  
- B cell (CL:0000236).  
- T cell (CL:0000084).

### Subcellular level

Subcellular compartments relevant to SIK3:

- Cytoplasm and nucleus (location of SIK3 and its substrates).[11]  
- Protein kinase complexes and transcriptional regulation machinery.[11]  

Suggested GO cellular component terms:  
- Cytoplasm (GO:0005737).  
- Nucleus (GO:0005634).  
- Protein kinase complex (GO:1902554).

### Localization and lateralization

- Skeletal abnormalities are systemic and bilateral, affecting all limbs and the spine.[1][3][13]  
- No lateralization (left–right asymmetry) has been reported.[1][3][13]

---

## 8. Temporal Development

### Onset

- **Age of onset:** Congenital/early pediatric; skeletal abnormalities and growth impairment are evident from infancy, with immunodeficiency and developmental delay recognized in early childhood.[1][3][13]  
- **Onset pattern:** Chronic and insidious; there is no acute onset event, but symptoms manifest as growth proceeds.[1][3][13]

### Progression

- **Disease stages:** Not formally defined, but clinical course can be conceptualized as:  
  - Early stage: Recognition of skeletal dysplasia, growth failure, and early developmental delay.  
  - Intermediate stage: Progressive limb deformities, mobility limitations, and recurrent severe infections.  
  - Advanced stage: Severe musculoskeletal disability, recurrent life‑threatening infections, and possible early mortality.[1][10][13]  
- **Progression rate:** Slowly progressive skeletal abnormalities; immunodeficiency manifests early with recurrent episodes.[1][3][10][13]  
- **Course pattern:** Chronic, lifelong; no remission described.[1][3][10]

### Duration and critical periods

- Disease appears lifelong, with significant morbidity and risk of early childhood death due to infection, based on the reported family.[1][10][13]  
- Critical periods likely include infancy and early childhood when infections are frequent and skeletal growth is rapid, offering windows for early diagnosis and prophylactic interventions.[10][13]

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence and incidence:** Not known; SEMDK is ultra‑rare, with only a single family described in detail and no registry‑based prevalence estimates.[1][3][4][5][10][13]  
- Orphanet‑level estimates are not yet established for this specific subtype.[1][3]

### Inheritance pattern

- **Autosomal recessive:** Both affected siblings were homozygous for the SIK3 variant, with heterozygous carrier parents in a consanguineous pedigree, consistent with autosomal recessive inheritance.[1][10][12]  
- PanelApp and clinical genomic databases list SEMDK under autosomal recessive skeletal dysplasia conditions.[10][12]

### Penetrance, expressivity, and other genetic features

- **Penetrance:** Appears complete within the reported family; all homozygous individuals were affected.[1][10]  
- **Expressivity:** Limited data from two siblings suggest similar severity and phenotype, but overall expressivity is unknown.[1][3][10][13]  
- **Genetic anticipation, germline mosaicism, founder effects:** No evidence for these phenomena; the variant is considered a private mutation in a single consanguineous family.[1][3][10]  
- **Carrier frequency:** Unknown; given absence from population databases, carrier frequency is presumed extremely low.[1][6][10]

### Population demographics

- The reported family appears to have origins consistent with the Krakow label, but detailed ethnicity and geographic distribution are not systematically documented; SEMDK is not known to be endemic in any region.[1][3][10][13]  
- Sex ratio: With only two affected siblings, sex predilection cannot be established.[1][3][10][13]  
- Age distribution: Manifestation in infancy and early childhood; adult cases have not been reported.[1][3][10][13]

---

## 10. Diagnostics

### Clinical and laboratory evaluation

Key elements of diagnosis:

- **Clinical suspicion:** Disproportionate short stature with rhizomelic/mesomelic limb shortening, pronounced anterior bowing of long bones, vertebral flattening, severe immunodeficiency, and developmental delay.[1][3][4][5][13]  
- **Imaging:** Skeletal survey with radiographs of spine and long bones revealing platyspondyly and epimetaphyseal abnormalities typical of SEMD, plus distinctive bowing and limb segment shortening.[1][3][13]  
  - Suggested RadLex concept: Skeletal survey; platyspondyly.  
- **Immune work‑up:** Basic immunologic tests (immunoglobulin levels, lymphocyte subsets) are expected but not detailed in published summaries; diagnosis of “severe immunodeficiency” is clinical.[1][3][10][13]  
- **Developmental assessment:** Standard neurodevelopmental evaluations to document global delay.[1][3][13]

No specific biochemical biomarkers have been validated for SEMDK beyond genetic testing.[1][3][6][10]

### Genetic testing

Given the rarity and phenotypic overlap with other skeletal dysplasias, advanced genomic testing is central:

- **Whole exome sequencing (WES):** Used in the original family after PTH1R mutation was excluded, leading to identification of homozygous SIK3 missense variant.[1][10][13]  
- **Single‑gene or targeted panel testing:** SIK3 is now included in skeletal dysplasia gene panels (e.g., Genomics England PanelApp skeletal dysplasia panel).[12]  
  - PanelApp lists SIK3 with moderate evidence for SEMDK, inheritance “biallelic (autosomal)”.[12]  
- **Clinical variant interpretation:** ClinVar provides classification and basic annotations for NM_001366686.3(SIK3):c.559C>T (p.Arg187Cys).[6]

Chromosomal microarray, karyotyping, FISH, mitochondrial DNA analysis, and repeat expansion tests are not indicated in typical SEMDK work‑ups unless broader differential diagnoses are considered.[1][3][10]

### Clinical criteria and differential diagnosis

No formal, society‑endorsed diagnostic criteria exist for SEMDK due to the very small evidence base.[1][3][10]

**Differential diagnosis:**

- Other forms of spondyloepimetaphyseal dysplasia (e.g., Isidor‑Toutain type, Maroteaux type), which may share skeletal features but lack severe immunodeficiency.[14][13]  
- Other immuno‑osseous dysplasias (e.g., Schimke immuno‑osseous dysplasia), which combine skeletal dysplasia with immunodeficiency and can present similarly.[13]  
- Primary immunodeficiency disorders without skeletal dysplasia.  

Distinguishing features include the specific pattern of limb bowing, vertebral and epimetaphyseal involvement, and association with SIK3 mutation.[1][3][10][13][14]

### Screening

No population screening programs exist for SEMDK.[1][3][10] Genetic testing is recommended for:  

- Symptomatic individuals with compatible phenotype.  
- At‑risk siblings in families with known SIK3 pathogenic variants (cascade testing).[10][12]  

Newborn screening does not include SEMDK.[1][3][10]

---

## 11. Outcome / Prognosis

### Survival and mortality

- Published information indicates severe morbidity and at least one early childhood death due to infection‑related complications in the reported family (human clinical evidence).[1][10][13]  
- Formal survival rates, life expectancy estimates, and disease‑specific mortality statistics are not available given the extremely small case number.[1][3][10]

### Morbidity and function

- Morbidity is substantial, driven by skeletal deformities, profound short stature, recurrent severe infections, and developmental delay.[1][3][4][5][10][13]  
- Long‑term functional impairments include mobility limitations, dependence on caregivers, and vulnerability to serious infections.[1][3][10][13]  

No standardized disability metrics (e.g., ICF coding) or quality‑of‑life scores (EQ‑5D, SF‑36, PROMIS) have been reported specifically for SEMDK.[1][3][10]

### Disease course and complications

- **Complications:**  
  - Recurrent pneumonia and severe respiratory infections.[1][10][13]  
  - Orthopedic complications from limb deformities (e.g., joint contractures, pain, gait disturbance).[1][3][13]  
- **Recovery potential:** Structural skeletal abnormalities are permanent; immunodeficiency may be partially mitigated by prophylactic measures and immunoglobulin replacement (inferred from immunodeficiency management principles).[10]  

### Prognostic factors

- Severity of immunodeficiency and frequency of infections are likely major determinants of survival and morbidity.[1][3][10][13]  
- Access to aggressive infection prophylaxis and treatment may improve outcomes (clinical genomic database recommendation).[10]

No validated prognostic biomarkers or risk models exist for SEMDK.[1][3][10]

---

## 12. Treatment

### Pharmacotherapy and supportive care

No disease‑specific curative pharmacologic therapy exists; management is supportive and extrapolated from principles of skeletal dysplasia and primary immunodeficiency.[1][3][10][13]

Key components (clinical genomic database and case‑based guidance):[10][13]

1. **Infection prophylaxis and treatment**  
   - Early and aggressive antibiotic therapy for infections.[10][13]  
   - Consideration of prophylactic antibiotics in high‑risk periods (inferred).  
   - Suggested NCIT terms: Antibiotic Therapy (NCIT:C77209).

2. **Immunoglobulin replacement**  
   - For patients with significant humoral immunodeficiency, intravenous or subcutaneous immunoglobulin may be considered (inferred from standard immunodeficiency care).[10]  
   - Suggested NCIT: Immunoglobulin Replacement Therapy (NCIT:C15410).

3. **Orthopedic management**  
   - Orthopedic interventions (bracing, corrective osteotomies) to manage limb deformities and improve function (inferred from skeletal dysplasia care).[13]  
   - Suggested NCIT: Orthopedic Surgery Procedure (NCIT:C15273).

4. **Physical and occupational therapy**  
   - To maximize mobility and function.[13]  
   - Suggested NCIT: Physical Therapy (NCIT:C15429); Occupational Therapy (NCIT:C15432).

5. **Developmental and educational support**  
   - Early intervention services for developmental delay.[1][3][13]

No specific pharmacogenomic data exist for SEMDK; standard antibiotic and immunoglobulin pharmacogenomics apply generically.[10]

### Advanced therapeutics

- **Gene therapy, cell therapy, RNA‑based therapies, targeted molecular therapies, immunotherapies:** None have been developed or trialed specifically for SEMDK as of current literature.[1][3][10][12]  
- The rarity of the condition and limited mechanistic detail have prevented disease‑specific clinical trials.[1][3][10]

### Treatment outcomes and strategies

- Published outcomes are limited to the original family and case‑based descriptions, with variable infection control and severe skeletal morbidity.[1][10][13]  
- Clinical genomic databases highlight awareness of SEMDK as a means to implement anti‑infectious prophylaxis and aggressive infection treatment, suggesting this may improve prognosis.[10]

No formal treatment algorithms or guidelines exist; treatment is individualized by multidisciplinary teams (pediatrics, immunology, orthopedics, rehabilitation).[1][3][10][13]

---

## 13. Prevention

### Primary prevention

- **Genetic counseling:** For families with known SIK3 pathogenic variants, counseling can inform reproductive decisions and reduce recurrence risk through carrier testing.[10][12]  
- **Avoidance of consanguinity:** In populations where consanguineous marriage is common, education about autosomal recessive risks may reduce likelihood of homozygous rare variants like SIK3 c.559C>T (inferred).[1][10][13]

### Secondary prevention (early detection)

- **Cascade genetic testing:** Testing siblings and close relatives of affected individuals for SIK3 variants enables early diagnosis and monitoring.[10][12]  
- **Prenatal or preimplantation genetic diagnosis:** Could be offered to carrier couples with known pathogenic SIK3 variants (inferred from standard Mendelian disease practice).[10][12]

No population‑level screening programs for SEMDK exist.[1][3][10]

### Tertiary prevention

- **Infection prophylaxis:** Implementation of vaccination schedules, prophylactic antibiotics, and immunoglobulin replacement to prevent severe infections.[10]  
- **Orthopedic and rehabilitation interventions:** To prevent secondary musculoskeletal complications (e.g., contractures, chronic pain).[13]

Public health and environmental interventions are not disease‑specific but align with general infection control and skeletal health measures.[10][13]

---

## 14. Other Species / Natural Disease

### Taxonomy and orthologous genes

- SIK3 has orthologs in multiple species, including rodents; rat Sik3 is annotated with disease cross‑references to human SEMDK in rat gene databases (association by orthology, not natural disease).[15]  
- NCBI Gene IDs and orthology relationships indicate evolutionary conservation of SIK3, but specific SEMDK‑like phenotypes have not been described in animals.[11][15]

### Natural disease and comparative biology

- No naturally occurring SEMDK or identical immuno‑osseous dysplasia due to Sik3 mutation has been reported in companion animals or livestock.[1][3][15]  
- Comparative pathology data are limited; however, conservation of SIK3 function in skeletal development across vertebrates suggests animal models could recapitulate aspects of human bone pathology (inferred).[11][15]

Zoonotic potential and cross‑species transmission are not applicable: SEMDK is a non‑infectious genetic disorder.[1][3][10]

---

## 15. Model Organisms

No dedicated SEMDK animal models have been reported in curated model organism databases, although Sik3 manipulation in rodents and other organisms has been used to study skeletal development in general.[11][15]

### Model types and characteristics

- **Genetic models (inferred):**  
  - Sik3 knockout or knock‑in models in mice or rats would be expected to show growth plate and skeletal phenotypes, but detailed recapitulation of SEMDK’s combined skeletal and immunologic phenotype has not been documented.[11][15]  
- **Phenotype recapitulation:**  
  - Existing Sik3 models (where studied) likely reflect aspects of bone growth defects but may not capture the full immunologic and neurodevelopmental spectrum observed in SEMDK.[11][15]  
- **Limitations:**  
  - Lack of published data on immunodeficiency in Sik3 models limits their direct use for studying SEMDK’s immune component.[11][15]

### Applications and resources

- SIK3 ortholog models can be used to investigate:  
  - Growth plate biology and chondrocyte maturation.  
  - Downstream signaling pathways of SIK3 in cartilage and immune cells.[11][15]  

Model resources are referenced indirectly via orthologous gene annotations rather than disease‑specific repositories.[11][15]

---

## Summary of Ontology and Evidence Mapping

- **Disease ontology:** MONDO:0032571 – Spondyloepimetaphyseal dysplasia, Krakow type.[7][12]  
- **Gene/protein:** SIK3 (HGNC:28980; OMIM:614776).[1][10][11]  
- **Key HPO terms:** Spondyloepimetaphyseal dysplasia (HP:0002650), Short stature (HP:0004322), Rhizomelia (HP:0008964), Mesomelia (HP:0003027), Bowing of long bones (HP:0003002), Primary immunodeficiency (HP:0002721), Recurrent infections (HP:0002719), Global developmental delay (HP:0001263).[1][3][4][5][13]  
- **GO biological processes:** Endochondral bone morphogenesis (GO:0060350), Cartilage development (GO:0051216), Chondrocyte differentiation (GO:0030212), Immune system process (GO:0002376).[11][14]  
- **CL cell types:** Chondrocyte (CL:0000138), Osteoblast (CL:0000120), B cell (CL:0000236), T cell (CL:0000084).[11][14]  
- **UBERON anatomical locations:** Vertebral column (UBERON:0002413), Long bone (UBERON:0002445), Epiphysis of long bone (UBERON:0003840), Metaphysis of long bone (UBERON:0003841), Spleen (UBERON:0002106), Thymus (UBERON:0002370).[1][3][10][13]  
- **NCIT interventions:** Orthopedic Surgery Procedure (NCIT:C15273), Physical Therapy (NCIT:C15429), Immunoglobulin Replacement Therapy (NCIT:C15410), Antibiotic Therapy (NCIT:C77209).[10][13]

**Evidence types:**

- Human clinical: Csukasi et al. 2018 (PMID:30232230) and case‑based reports summarized by OMIM, MedGen, MalaCards, Kauvery Hospital article.[1][3][4][10][13]  
- Computational/aggregated: OMIM, MedGen, MalaCards, rarediseases.org, KEGG, UniProt, PanelApp, ClinVar, Clinical Genomic Database, rat gene databases.[1][2][3][5][6][10][11][12][14][15]  
- Model organism/inferred: Sik3 ortholog annotations in rat and general SIK3 functional studies (not disease‑specific).[11][15]

Overall, SEMDK remains an extremely rare, recently defined immuno‑osseous dysplasia with a single known causative variant in SIK3, a very limited clinical evidence base, and largely inferred mechanistic and management frameworks.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 1 |
| On topic | 0 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 44 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 37 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 18 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002650` (2 mentions) - the report calls it "Spondyloepimetaphyseal dysplasia", "Key HPO terms:** Spondyloepimetaphyseal dysplasia"; HP calls it **Scoliosis**
- `HP:0000947` (1 mention) - the report calls it "Abnormal metaphysis morphology"; HP calls it **Dumbbell-shaped long bone**
- `HP:0008964` (2 mentions) - the report calls it "Rhizomelia"; HP calls it **Nonprogressive muscular atrophy**
- `HP:0003002` (2 mentions) - the report calls it "Bowing of long bones"; HP calls it **Breast carcinoma**
- `GO:0030212` (2 mentions) - the report calls it "Chondrocyte differentiation"; GO calls it **hyaluronan metabolic process**
- `CL:0000120` (3 mentions) - the report calls it "Osteoblast"; CL calls it **granule cell**
- `UBERON:0002413` (2 mentions) - the report calls it "Suggested UBERON: Vertebral column", "UBERON anatomical locations:** Vertebral column"; UBERON calls it **cervical vertebra**
- `UBERON:0002445` (2 mentions) - the report calls it "Suggested UBERON: Long bone"; UBERON calls it **ulnare**
- `UBERON:0003840` (2 mentions) - the report calls it "Epiphysis of long bone"; UBERON calls it **hindlimb joint**
- `UBERON:0003841` (2 mentions) - the report calls it "Metaphysis of long bone"; UBERON calls it **autopod joint**
- `UBERON:0002106` (2 mentions) - the report calls it "Suggested UBERON: Spleen"; UBERON calls it **spleen**
- `UBERON:0002048` (1 mention) - the report calls it "Suggested UBERON: Lung"; UBERON calls it **lung**
- `UBERON:0002414` (1 mention) - the report calls it "Suggested UBERON: Hyaline cartilage"; UBERON calls it **lumbar vertebra**
- `CL:0000121` (1 mention) - the report calls it "Osteoclast"; CL calls it **Purkinje cell**
- `NCIT:C77209` (2 mentions) - the report calls it "Suggested NCIT terms: Antibiotic Therapy"; NCIT calls it **CHFR Gene**
- `NCIT:C15410` (2 mentions) - the report calls it "Suggested NCIT: Immunoglobulin Replacement Therapy"; NCIT calls it **Biological Response Modifier Therapy**
- `NCIT:C15273` (2 mentions) - the report calls it "Suggested NCIT: Orthopedic Surgery Procedure", "NCIT interventions:** Orthopedic Surgery Procedure"; NCIT calls it **Longitudinal Study**
- `NCIT:C15429` (2 mentions) - the report calls it "Suggested NCIT: Physical Therapy"; NCIT calls it **Research Activity**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0010572` (1 mention), reported as "Abnormal epiphysis morphology" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `NCIT:C15410` (Biological Response Modifier Therapy) (2 mentions)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0004322` (2 mentions) - the report calls it "Suggested HPO: Short stature"; HP calls it **Short stature**
- `HP:0002721` (2 mentions) - the report calls it "Primary immunodeficiency"; HP calls it **Immunodeficiency**
- `HP:0001263` (2 mentions) - the report calls it "Suggested HPO: Global developmental delay"; HP calls it **Global developmental delay**
- `GO:0060350` (2 mentions) - the report calls it "Endochondral bone morphogenesis", "GO biological processes:** Endochondral bone morphogenesis"; GO calls it **endochondral bone morphogenesis**
- `CL:0000138` (3 mentions) - the report calls it "Growth plate chondrocyte", "Chondrocyte", "CL cell types:** Chondrocyte"; CL calls it **chondrocyte**
- `GO:1902554` (1 mention) - the report calls it "Protein kinase complex"; GO calls it **serine/threonine protein kinase complex**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0032571` - called "spondyloepimetaphyseal dysplasia, Krakow type", "Spondyloepimetaphyseal dysplasia, Krakow type"
- `HP:0002650` - called "Spondyloepimetaphyseal dysplasia", "Key HPO terms:** Spondyloepimetaphyseal dysplasia"
- `GO:0060350` - called "Endochondral bone morphogenesis", "GO biological processes:** Endochondral bone morphogenesis"
- `CL:0000138` - called "Growth plate chondrocyte", "Chondrocyte", "CL cell types:** Chondrocyte"
- `UBERON:0002413` - called "Suggested UBERON: Vertebral column", "UBERON anatomical locations:** Vertebral column"
- `NCIT:C15273` - called "Suggested NCIT: Orthopedic Surgery Procedure", "NCIT interventions:** Orthopedic Surgery Procedure"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.