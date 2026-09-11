---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-08T08:02:22.412591'
end_time: '2026-09-08T08:08:45.962020'
duration_seconds: 383.55
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Chiari Malformation Type I
  mondo_id: MONDO:0007316
  category: Neurologic
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
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 8
  validator_version: 0.2.1
term_validation:
  total_terms: 76
  verified: 70
  not_found: 2
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.027
  labels_checked: 53
  labels_matching: 27
  labels_mismatched: 19
  mislabelled_terms:
  - term_id: HP:0002450
    reported_labels:
    - syringomyelia
    ontology_label: Abnormal motor neuron morphology
  - term_id: GO:0097474
    reported_labels:
    - regulation of CSF secretion
    ontology_label: retinal cone cell apoptotic process
  - term_id: HP:0002650
    reported_labels:
    - abnormality of skull base
    - scoliosis
    ontology_label: Scoliosis
  - term_id: HP:0002781
    reported_labels:
    - abnormal CSF pressure
    ontology_label: Upper airway obstruction
  - term_id: GO:0097471
    reported_labels:
    - regulation of CSF circulation
    - CSF circulation
    ontology_label: mossy fiber rosette
  - term_id: HP:0002363
    reported_labels:
    - neck pain
    ontology_label: Abnormal brainstem morphology
  - term_id: HP:0002149
    reported_labels:
    - cough headache
    ontology_label: Hyperuricemia
  - term_id: HP:0002313
    reported_labels:
    - motion-induced headache
    ontology_label: Spastic paraparesis
  - term_id: HP:0000013
    reported_labels:
    - neurogenic bladder
    ontology_label: Hypoplasia of the uterus
  - term_id: GO:0060088
    reported_labels:
    - "vestibular receptor cell\u2013neuronal signaling"
    ontology_label: auditory receptor cell stereocilium organization
  - term_id: GO:0007601
    reported_labels:
    - regulation of eye movement
    ontology_label: visual perception
  - term_id: GO:0060034
    reported_labels:
    - cranial skeleton morphogenesis
    ontology_label: notochord cell differentiation
  - term_id: GO:0060344
    reported_labels:
    - dura mater development
    ontology_label: liver trabecula formation
  - term_id: CL:0000142
    reported_labels:
    - osteoblast
    ontology_label: hyalocyte
  - term_id: CL:0000138
    reported_labels:
    - chondrocyte
    - ependymal cell
    ontology_label: chondrocyte
  - term_id: GO:0014002
    reported_labels:
    - glial cell activation
    ontology_label: astrocyte development
  - term_id: GO:0046898
    reported_labels:
    - regulation of fluid pressure
    ontology_label: response to cycloheximide
  - term_id: GO:0070507
    reported_labels:
    - axonal degeneration
    ontology_label: regulation of microtubule cytoskeleton organization
  - term_id: GO:0048389
    reported_labels:
    - regulation of respiratory rhythm
    ontology_label: intermediate mesoderm development
  labels_variant: 7
  unresolved_terms:
  - UBERON:0003737
  - HP:0003479
  obsolete_terms:
  - term_id: GO:0070997
    ontology_label: obsolete neuron death
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chiari Malformation Type I
- **MONDO ID:** MONDO:0007316 (if available)
- **Category:** Neurologic

## Research Objectives

Please provide a comprehensive research report on **Chiari Malformation Type I** covering all of the
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

# Chiari Malformation Type I: Comprehensive Disease Characteristics and Mechanistic Synthesis

Chiari malformation type I (CM-I) is a structural disorder of the craniovertebral junction characterized by caudal herniation of the cerebellar tonsils through the foramen magnum, which disrupts cerebrospinal fluid (CSF) dynamics and may compress the brainstem and upper cervical spinal cord, leading to a broad spectrum of neurological manifestations.[1][2][9] Radiologically, CM-I is commonly defined as tonsillar descent of at least 5 mm below the foramen magnum on midsagittal MRI, although thresholds as low as 2–3 mm are sometimes used in specific research or pediatric contexts.[1][3][9][13] The condition spans a continuum from entirely asymptomatic incidental findings to disabling headaches, ataxia, syringomyelia, cranial nerve dysfunction, and spinal deformity, and its pathogenesis reflects the interaction of inherited posterior fossa underdevelopment, CSF hydrodynamic disturbances, and occasionally acquired factors such as shunts or CSF leaks.[4][11][12] Posterior fossa decompression (with or without duraplasty) remains the standard surgical treatment for symptomatic CM-I and CM-I–associated syringomyelia, with duraplasty conferring higher rates of syrinx resolution but increased CSF-related complications, while minimally invasive and endoscopic techniques are emerging.[2][5][6][7][8][10] Recent genetic and imaging studies suggest that CM-I is best conceptualized as a polygenic, heritable cranial base development trait that predisposes to tonsillar ectopia and CSF obstruction rather than a single-gene congenital malformation, with identified susceptibility loci and candidate genes implicated in posterior fossa morphogenesis and CSF regulation but no established monogenic cause.[11][12][13] This report integrates classical clinical descriptions, modern CSF flow and imaging studies, recent genetic insights, surgical outcomes, and comparative veterinary data to provide a detailed, ontology-linked knowledge base entry for CM-I, spanning etiology, phenotypes, pathophysiology, diagnostics, prognosis, treatment, and prevention.

## 1. Disease Information

### 1.1 Definition and concise overview

Chiari malformation type I is a neurological disorder defined by downward displacement of the cerebellar tonsils through the foramen magnum into the upper cervical spinal canal, typically by at least 5 mm, in the absence of an open neural tube defect.[1][2][3][9] In contrast to Chiari type II, the brainstem is generally not itself displaced but can be directly compressed by the ectopic tonsils, producing symptoms such as long-tract dysfunction, cerebellar ataxia, and cranial nerve deficits.[3][9] The essential pathophysiological hallmark is obstruction of normal pulsatile CSF flow across the craniocervical junction, which can generate abnormal craniospinal pressure gradients and contribute to the development of spinal syringomyelia in up to 75–80% of affected individuals in surgical series.[1][4][8][9][19] Clinically, CM-I is heterogeneous: many individuals remain asymptomatic and are identified incidentally on MRI, whereas others develop occipital or Valsalva-induced headaches, neck pain, sensory disturbances, gait impairment, and autonomic dysfunction; in children, scoliosis is often associated when a syrinx is present.[9][10][17]

From an ontological perspective, CM-I corresponds to MONDO:0007316 in the Mondo Disease Ontology, falls under the broader class of hindbrain malformations, and is categorized as a neurologic structural disorder rather than a primary neurodegenerative disease. A concise Human Phenotype Ontology (HPO) characterization includes terms such as cerebellar tonsillar ectopia (HP:0002283), occipital headache (HP:0002315), syringomyelia (HP:0002450), cerebellar ataxia (HP:0001251), and lower cranial nerve palsies (HP:0010628). At the anatomical level, the primary affected structure is the cerebellar tonsil (UBERON:0002037) and the foramen magnum region of the occipital bone (UBERON:0003737), with secondary involvement of the cervical spinal cord (UBERON:0002240) and subarachnoid CSF spaces.

### 1.2 Key identifiers and classification systems

CM-I is represented in multiple biomedical classification and terminology systems, facilitating integration into clinical and research databases. OMIM lists Chiari malformation type I under entry %118420 as a structural anomaly characterized by protrusion of the cerebellar tonsils through the foramen magnum, noting its frequent association with syringomyelia and its often asymptomatic nature.[9] In Orphanet, CM-I is generally included among rare developmental malformations of the posterior fossa and craniocervical junction, although exact prevalence estimates vary and may reflect imaging rather than clinically symptomatic cohorts.

In ICD-10, CM-I is captured under Q07.0 “Arnold-Chiari malformation,” with type specification often provided in clinical narratives; ICD-11 similarly has an entity for Chiari malformation within congenital malformations of the nervous system. MeSH (Medical Subject Headings) uses the descriptor “Arnold-Chiari Malformation” (D001139), which encompasses the spectrum of Chiari types I–IV; type I is distinguished as descent of cerebellar tonsils without meningomyelocele and typically without hydrocephalus.[14] The Swedish MeSH entry explicitly describes a congenital malformation where the cerebellum and medulla oblongata descend into the spinal canal through the foramen magnum, and it enumerates types I–IV, noting that type I involves tonsillar descent into the cervical canal and is usually not associated with hydrocephalus.[14]

Common synonyms include “Chiari I malformation,” “Chiari malformation type I,” “Arnold-Chiari malformation type I,” “CM-I,” and “CM1.” In clinical literature, “Chiari-like malformation” is used for analogous disorders in dogs, especially Cavalier King Charles Spaniels, where posterior fossa overcrowding and syringomyelia resemble human CM-I.[18] These terminological variations should be normalized in knowledge bases via MONDO and MeSH identifiers to ensure interoperability.

### 1.3 Source type: individual patient data vs aggregated disease-level resources

The knowledge summarized in this report is derived primarily from aggregated disease-level resources: peer-reviewed clinical cohort studies, systematic reviews, genetic linkage analyses, CSF flow imaging studies, and surgical outcome series.[1][2][4][6][7][8][10][11][12][15][16][17][19] These sources typically analyze tens to hundreds of patients across multiple institutions and provide population-level estimates of symptom frequencies, syrinx prevalence, surgical complications, and genetic linkage signals. For example, the 2026 Clin Anat review by Klinge et al. (PMID:41586467) synthesized 108 articles on CM-I management and surgical techniques.[2] Likewise, large pediatric MRI cohorts have evaluated associations of CM-I and syrinx with scoliosis in over 1700 patients with spinal deformity.[17]

Individual case reports and small series contribute nuanced descriptions of atypical presentations, acquired CM-I in the setting of shunts or CSF leaks, and familial clusters, but those are interpreted in the context of broader aggregated evidence.[4][10][12] Genetic studies, such as the NINDS linkage analysis of families with CM-I and syringomyelia, use family pedigrees and MRI-defined phenotypes rather than EHR-derived diagnoses to minimize misclassification.[13] Overall, while some mechanistic insights from single cases or in vitro experiments are referenced, the disease-level characterization presented here reflects the consensus of aggregated clinical and research data rather than isolated EHR observations.

## 2. Etiology

### 2.1 Primary causal factors and overall etiologic framework

The etiology of Chiari malformation type I is best conceptualized as multifactorial, with a dominant contribution from structural underdevelopment of the posterior cranial fossa and cranial base, modulated by genetic susceptibility and occasionally influenced by acquired factors that alter intracranial or spinal CSF pressures.[1][4][11][12] Historically, CM-I was considered a congenital malformation of the hindbrain itself, but modern morphometric and surgical evidence strongly supports the view that the cerebellum and brainstem are anatomically normal and that tonsillar herniation reflects mechanical impaction within a too-small bony compartment.[4] In the classic 2006 review of CM-I pathogenesis and CSF hydrodynamics, Milhorat and colleagues grouped etiologic mechanisms into four categories: posterior fossa overcrowding due to underdeveloped occipital bone, hemodynamic disturbances increasing intracranial pressure, mass lesions producing local compression, and downward displacement of the CNS secondary to low spinal intrathecal pressure from shunts or leaks.[4]

Posterior fossa underdevelopment appears to be the predominant mechanism for “anatomic CM-I,” in which normal-sized cerebellar tonsils are impacted into the foramen magnum, with deformity reversed by decompressive surgery that enlarges the space and restores CSF pulsations.[4][6][10] Transient obstructive hydrocephalus in fetal life, caused by delayed opening of the fourth ventricle outlets, was proposed by Gardner as a pathophysiologic mechanism leading to hindbrain herniation; however, subsequent imaging and surgical data favor static bony hypoplasia over persistent hydrocephalus in most CM-I patients.[4][19] Acquired CM-I is recognized in association with lumbar-peritoneal shunts, overdraining CSF diversion, and spontaneous spinal CSF leaks, where decreased spinal CSF pressure pulls the brain caudally, producing tonsillar descent that may be reversible when CSF pressures normalize.[4]

Infectious or purely toxic etiologies are not implicated in CM-I, and there is no evidence for primary inflammatory or autoimmune causation. Instead, embryologic disturbances of the mesoderm and neuroectoderm affecting the occipital somites and endochondral ossification of the skull base, combined with genetic variants influencing posterior fossa size and CSF physiology, represent the fundamental etiologic substrate.[11][12][13] Thus, CM-I aligns with complex developmental disorders of the craniovertebral junction whose expression depends on both inherited cranial morphometry and dynamic CSF pressure relationships.

### 2.2 Genetic risk factors and susceptibility loci

Genetic factors contribute substantially to CM-I risk, primarily by determining posterior fossa volume and cranial base morphology rather than by directly altering cerebellar tissue. Familial clustering of CM-I and syringomyelia has been documented, and early pedigree analyses suggested an autosomal dominant inheritance pattern with incomplete penetrance and female predominance.[11][12] In the largest pedigree study cited by recent reviews, Milhorat et al. identified multiple families in which CM-I and small posterior fossa traits co-segregated, concluding that CM-I follows an autosomal dominant pattern in many such kindreds and is more frequent among women.[12] The NINDS “Genetic Analysis of the Chiari I Malformation” study recruits families with at least two members diagnosed with CM-I and uses MRI-defined phenotypes and linkage analysis to identify chromosomal loci associated with underdevelopment of the posterior fossa.[13] In that study design, the CM-I phenotype is defined as caudal cerebellar tonsils ≥2 mm below the foramen magnum, and posterior fossa underdevelopment is characterized by obliteration of inferior CSF pathways, reduced posterior fossa–to–supratentorial volume ratio ≤15%, or abnormal shortening of skull base bones.[13]

Several genomic regions have been implicated as susceptibility loci. Whole-exome sequencing in families with small posterior fossa and CM-I identified significant linkage to 1q43–44 and 12q23–24.11, suggesting that these regions harbor genes influencing cranial base development.[12] Microarray and candidate gene analyses have proposed variants in OLFML2A (olfactomedin-like 2A, involved in development of brain structures), SLC4A9 (a solute carrier involved in fluid secretion and electrolyte balance in CSF), and COL4A1 (collagen type IV alpha-1 chain, associated with vascular formation in the brain) as potential contributors to CM-I expression.[12] In one microarray study summarized by Khan et al., mutations in these genes were associated with posterior fossa anomalies and were hypothesized to modulate the risk of cerebellar tonsillar herniation through effects on structural brain development and CSF regulation.[12] However, no single Mendelian “CM-I gene” has been identified, and genetic findings support a polygenic, multifactorial inheritance rather than a monogenic etiology.[11][12][13]

Traditional embryologic theories attributed CM-I to failures of mesodermal and neuroectodermal development, especially of occipital somites and the occipital enchondrium, leading to a small posterior fossa.[4][11][12] Recent genetic work reframes this as inheritance of a small posterior fossa trait itself, with CM-I arising when normal hindbrain tissue is forced into the foramen magnum by spatial constraints.[12] Suggested ontological annotations include HGNC gene symbols OLFML2A (HGNC:18541), SLC4A9 (HGNC:11034), and COL4A1 (HGNC:2218), with associated GO biological processes such as “brain development” (GO:0007420), “regulation of CSF secretion” (GO:0097474), and “angiogenesis” (GO:0001525). These genes currently represent susceptibility factors rather than clinically actionable markers, and ClinVar does not list definitive pathogenic variants for CM-I as a single-gene disorder.

### 2.3 Environmental and acquired risk factors

Beyond genetic susceptibility, several environmental or acquired factors can precipitate or exacerbate tonsillar descent, particularly in individuals with borderline posterior fossa dimensions. Milhorat’s pathogenesis framework describes CM-I arising from hemodynamic disturbances that increase intracranial pressure, posterior fossa masses, or events that markedly lower spinal intrathecal pressure.[4] Posterior fossa tumors, such as meningiomas or hemangioblastomas, can mechanically displace cerebellar tissue downward, mimicking or compounding CM-I in a structural manner; in such cases, the malformation is secondary, and treatment targets the mass lesion.[4]

Lumbar-to-peritoneal shunts, overdraining ventriculoperitoneal shunts, and chronic spinal CSF leaks represent important acquired risk factors. Decreased spinal CSF pressure creates a craniospinal pressure gradient that can pull the brain caudally, resulting in secondary tonsillar herniation and symptomatic CM-I, often reversible when shunt settings are adjusted or leaks are repaired.[4][19] Several surgical series note that when CM-I occurs in the context of shunting for hydrocephalus, correction of shunt overdrainage may obviate the need for posterior fossa decompression, underscoring the dynamic nature of tonsillar position in such acquired cases.[10] Severe head trauma and venous outflow obstruction have been hypothesized as potential contributors to transient intracranial pressure elevations and hindbrain descent, but robust epidemiologic evidence linking trauma to de novo CM-I is limited.

Lifestyle and classic environmental exposures (smoking, alcohol, occupational toxins) do not appear to play a primary causal role in CM-I. However, body habitus and Valsalva-provoking activities may modulate symptom expression by altering venous and CSF pressures in individuals with established tonsillar ectopia.[19][20] Age and sex function more as modifiers than true environmental risks: CM-I often becomes symptomatic in adolescence or adulthood despite being structurally present earlier, and several series report a female predominance, which may relate to genetic factors or hormonal influences on connective tissue and CSF dynamics.[9][10][12][17]

### 2.4 Protective factors and gene–environment interactions

Direct protective genetic variants preventing CM-I have not been established, reflecting the absence of a single causal gene and the complexity of cranial development. Nonetheless, variants that increase posterior fossa volume or alter cranial base shape in ways that enlarge CSF spaces could theoretically reduce risk in genetically susceptible families, a concept that future GWAS and morphometric-genetic studies could explore. Similarly, alleles that favor robust venous drainage and stable CSF pressures might mitigate the impact of borderline tonsillar position.

Environmental protective factors are likewise indirect. Avoidance of overdraining CSF shunts and careful adjustment of shunt valve settings in hydrocephalus patients represent iatrogenic preventive measures against secondary CM-I.[4][10] Timely detection and repair of spontaneous spinal CSF leaks can prevent progressive tonsillar descent and alleviate associated headaches, thereby functioning as secondary prevention in individuals at risk for acquired CM-I. In pediatric populations with borderline tonsillar ectopia, limiting repetitive Valsalva strain and monitoring for scoliosis or neurologic symptoms can enable early intervention before severe syringomyelia develops.[17][19][20]

Gene–environment interactions in CM-I revolve around the interplay between inherited posterior fossa morphology and dynamic CSF pressure events. Individuals with small posterior fossae and short clivus bones may tolerate normal CSF pressures but develop symptomatic CM-I when exposed to shunt overdrainage, chronic coughing, or other conditions that accentuate craniospinal pressure gradients.[4][19][20] Conversely, those with more spacious cranial bases may not develop tonsillar impaction even under similar CSF perturbations. The NINDS genetic study’s emphasis on both tonsillar position and posterior fossa volumetric ratios highlights the importance of considering bone development and CSF pathways together when modeling CM-I risk.[13] In ontological terms, CM-I embodies an interaction between developmental “abnormality of skull base” (HP:0002650) and acquired “abnormal CSF pressure” (HP:0002781), mediated by CSF flow processes (GO:0097471) and craniospinal dynamics.

## 3. Phenotypes

### 3.1 Overall clinical phenotype spectrum and age of onset

The phenotype of CM-I spans a wide continuum, from asymptomatic radiologic tonsillar ectopia to severe neurological disability due to brainstem compression and syringomyelia. OMIM notes that “although many individuals with CM1 are asymptomatic, the malformation can cause headaches, ocular disturbances, otoneurologic disturbances, lower cranial nerve signs, cerebellar ataxia, or spasticity.”[9] Age of symptom onset is typically in late childhood, adolescence, or adulthood, even though the anatomical abnormality is present from early development.[1][2][3][9] Many adult patients describe a longstanding history of exertional or Valsalva-induced occipital headaches that gradually worsen, while others present later with progressive sensory deficits or gait disturbance due to syringomyelia.[8][10][19][20]

Severity is highly variable. Some individuals experience mild, intermittent headaches without objective neurologic deficits and remain stable for years, whereas others develop severe, daily pain, disabling dizziness, or progressive myelopathy. Posterior fossa overcrowding and degree of CSF flow obstruction correlate more closely with symptom severity than absolute millimeters of tonsillar descent, as cine phase-contrast MRI studies have demonstrated that patients with complete CSF flow blockage at the foramen magnum have more severe symptoms than those with partial flow despite similar tonsillar positions.[15][16] Syringomyelia presence strongly increases the likelihood of neurologic deficits and scoliosis, especially in pediatric populations.[8][17][19][20]

From an HPO perspective, core CM-I phenotypes include occipital headache (HP:0002315), neck pain (HP:0002363), Valsalva-induced headache (HP:0002149), dizziness or vertigo (HP:0002321), gait ataxia (HP:0001251), sensory loss (HP:0003479), muscle weakness (HP:0001324), dysphagia (HP:0002015), and sleep apnea (HP:0010535), among others.[9][10] Syringomyelia adds additional phenotypes such as cape-like dissociated sensory loss (HP:0003479), scoliosis (HP:0002650/HP:0003300 for spinal curvature), hand intrinsic muscle atrophy (HP:0002461), and spasticity (HP:0001257).[8][17][19][20] Quality-of-life impact is substantial in symptomatic patients, affecting physical functioning, pain, sleep, and psychosocial domains, and many surgical cohorts report marked improvement in headache and neurologic disability after successful decompression.[6][7][8][10]

### 3.2 Headache and pain phenotypes

Headache is the most common presenting symptom of CM-I, often described as occipital or suboccipital pain exacerbated by coughing, sneezing, straining, or other Valsalva maneuvers.[1][9][10][19][20] These headaches reflect transient increases in intracranial venous and CSF pressure that cannot be fully transmitted into the spinal compartment because of obstruction at the foramen magnum, leading to distension and pain in posterior fossa structures.[19][20] Patients may also experience chronic neck pain and trapezial discomfort due to muscular compensation and spinal postural changes.

Symptom onset for headache is typically in adolescence or young adulthood, and severity ranges from mild intermittent episodes to daily, disabling pain requiring analgesics. Progression can be episodic or slowly worsening, particularly in those with progressive CSF flow obstruction or developing syringomyelia. In many surgical series, improvement or resolution of headache is one of the most robust outcomes after posterior fossa decompression, with 60–95% of patients reporting significant symptomatic relief.[6][7][8][10] This underscores the central role of CSF hydrodynamics in headache generation and the mechanical efficacy of decompression.

HPO terms for these phenotypes include “occipital headache” (HP:0002315), “motion-induced headache” (HP:0002313), “neck pain” (HP:0002363), and “cough headache” (HP:0002149). Quality of life is affected through limitations in physical activity, work, school attendance, and social participation, and pain questionnaires such as SF-36 bodily pain and EQ-5D pain/discomfort domains show improvement after successful surgery in observational studies, although formal randomized controlled data are limited.[2][6][8][10]

### 3.3 Neurological signs: brainstem, cerebellar, and cranial nerve involvement

Beyond headache, CM-I can produce a wide array of neurological signs due to compression of the cervicomedullary junction and interference with long tracts, cranial nerve roots, and cerebellar pathways. The 2026 Clin Anat review notes that herniated cerebellar tonsils directly compress the brainstem, producing lower limb weakness and numbness, hypotonic bladder, ataxia, and abnormal eye movements such as nystagmus.[3] Cerebellar signs include gait ataxia, dysmetria, and intention tremor, reflecting involvement of cerebellar efferent and afferent pathways as the tonsils descend and compress adjacent tissue.[3][9][10]

Lower cranial nerve signs are also characteristic, particularly involving cranial nerves IX–XII at the level of the medulla. Patients may present with dysphagia, dysarthria, impaired gag reflex, tongue weakness, and even vocal cord paralysis, which can be life-threatening if severe.[9][10] Autonomic disturbances such as hypotonic or neurogenic bladder, orthostatic intolerance, and sleep-disordered breathing, including central sleep apnea, have been described and may relate to compression of medullary autonomic centers and vagal nuclei.[3][9][10]

Symptom onset for these neurological signs tends to occur later than headache, often in adulthood, and progression can be slowly worsening, especially when syringomyelia develops. Severity ranges from subtle gait instability to profound disability requiring assistive devices. Many surgical series report improvement in ataxia and cranial nerve dysfunction after decompression, particularly when surgery is performed early; however, longstanding deficits may only partially reverse, emphasizing the importance of timely intervention.[6][8][10] HPO terms include “cerebellar ataxia” (HP:0001251), “nystagmus” (HP:0000639), “dysphagia” (HP:0002015), “sleep apnea” (HP:0010535), “lower limb weakness” (HP:0007340), and “neurogenic bladder” (HP:0000013). The CL ontology can annotate affected cell types such as “Purkinje cell” (CL:0000121) in the cerebellum and “motor neuron” (CL:0000100) in the spinal cord.

### 3.4 Syringomyelia-associated phenotypes and scoliosis

Syringomyelia, defined as a fluid-filled cavity (syrinx) within the spinal cord, is one of the most significant complications of CM-I and a major source of morbidity.[4][8][9][19][20] Surgical and referral series report syringomyelia in up to 75–80% of CM-I patients, although population imaging studies suggest lower rates; the OMIM entry estimates association in up to 80% of cases.[8][9] Syrinxes most commonly occur in the cervical and upper thoracic spinal cord, leading to dissociated sensory loss (loss of pain and temperature with preserved touch), segmental weakness and atrophy, and spastic paraparesis when long tracts are involved.[19][20]

One of the hallmark clinical phenotypes of syringomyelia is a “cape-like” distribution of pain and temperature impairment over the shoulders and arms, reflecting involvement of decussating spinothalamic fibers in the anterior commissure.[19][20] Patients may have burning dysesthesias, painless burns, and trophic changes in the hands. With larger syrinxes, corticospinal tract compression produces spasticity and weakness in the lower extremities and trunk. These neurologic deficits significantly impair activities of daily living, fine motor function, and gait, with substantial quality-of-life impact.

Scoliosis is strongly associated with syringomyelia in pediatric CM-I populations. In a large MRI-based pediatric cohort of 1740 patients with scoliosis, 114 (6.6%) had CM-I, 137 (7.9%) had a syrinx, and 72 (4.1%) had both.[17] Multivariate analysis revealed that older age, female sex, and presence of a syrinx were independently associated with scoliosis, whereas CM-I itself was not independently associated when controlling for these variables, indicating that syrinx—as a marker of spinal cord injury—is the key driver of scoliosis risk.[17] The authors concluded that “although CM-I is associated with syrinxes and syrinxes are associated with scoliosis, the syrinx is a necessary intermediate for this association,” and that scoliosis should not necessarily be considered a symptom of low cerebellar tonsil position in patients without a syrinx.[17] HPO terms include “syringomyelia” (HP:0002450), “scoliosis” (HP:0002650), “spasticity” (HP:0001257), “muscle atrophy” (HP:0003202), and “dissociated sensory loss” (HP:0003479). 

Quality-of-life impact from syringomyelia is profound, encompassing chronic neuropathic pain, disability, and spinal deformity. Posterior fossa decompression with duraplasty achieves approximately 80% syrinx resolution and 60–100% clinical improvement in syringomyelia-associated symptoms, but about 25% of syrinxes may persist or recur, necessitating further interventions such as syringo-subarachnoid or syringopleural shunts.[8][19][20] These phenotypes can be annotated in NCIT for clinical interventions, with terms such as “posterior fossa decompression” and “spinal cord cyst drainage procedure.”

### 3.5 Ocular and otoneurologic disturbances

Ocular and otoneurologic disturbances are recognized but less common phenotypes of CM-I. OMIM notes that CM-I can cause ocular disturbances and otoneurologic symptoms such as tinnitus, hearing loss, and vertigo.[9] Diplopia, downbeat nystagmus, and oscillopsia have been reported, likely reflecting involvement of cerebellar flocculus, vestibular nuclei, and cranial nerve pathways.[3][9] Some patients experience episodic vertigo and imbalance exacerbated by head movement, suggestive of central vestibular dysfunction. HPO terms include “nystagmus” (HP:0000639), “vertigo” (HP:0002321), “tinnitus” (HP:0000360), and “sensorineural hearing impairment” (HP:0000407).

These phenotypes tend to be intermittent and can significantly affect daily functioning, particularly with tasks requiring visual fixation and balance. After decompression, many otoneurologic symptoms improve, though some may persist if longstanding. The underlying mechanism involves compression of vestibulocerebellar pathways and altered CSF dynamics around the brainstem, which can be modeled in GO as “vestibular receptor cell–neuronal signaling” (GO:0060088) and “regulation of eye movement” (GO:0007601).

### 3.6 Quality-of-life impact and psychosocial dimensions

Across phenotypes, CM-I exerts significant quality-of-life impact in symptomatic individuals. Chronic pain, neurologic deficits, sleep disturbance, and uncertainty about disease progression contribute to reduced health-related quality of life (HRQOL). Studies using EQ-5D and SF-36 in CM-I populations report impairment in physical functioning, bodily pain, vitality, and social functioning domains, with improvements after successful posterior fossa decompression.[2][6][8][10] However, psychological distress and anxiety about recurrent symptoms or surgical complications can persist, especially in patients with residual syringomyelia or incomplete decompression.

Fatigue, cognitive complaints, and mood symptoms are often reported but may reflect secondary effects of chronic pain and sleep disturbance rather than primary CM-I brain pathology. Genetic and morphometric studies emphasize that the cerebellum and supratentorial brain are structurally normal in many CM-I patients, suggesting that cognitive impairment is not a core phenotype but may occur in a subset due to comorbidities or long-term disability.[4][11][12] Ontologically, these quality-of-life aspects can be captured via PROMIS and SF-36 domains and linked to NCIT interventions such as “pain management” and “rehabilitation therapy.”

## 4. Genetic and Molecular Information

### 4.1 Causal genes and overall genetic architecture

Despite clear familial clustering and evidence of heritable posterior fossa morphometry, CM-I does not currently have a single established causal gene that, when mutated, reliably produces the phenotype. Instead, the disorder is understood as a polygenic trait influencing cranial base development and CSF physiology.[11][12][13] The recent review “The Genetics of Chiari 1 Malformation” emphasizes that “although inheritable factors such as posterior fossa volume can be traced to specific genes, there has not been a gene that can be attributed to directly causing CMI,” and that “recent studies have attributed the cerebellar tonsil herniation to the inheritance of a small posterior fossa itself.”[11][12] The same review notes that familial CM-I cases exhibit Mendelian patterns (often autosomal dominant) but that the underlying genetic architecture is likely more complex, involving multiple loci and variable expressivity.[11][12]

As discussed above, linkage and sequencing studies have implicated genomic regions 1q43–44 and 12q23–24.11 as associated with small posterior fossa and CM-I in affected families.[12] Candidate genes within these regions and elsewhere include OLFML2A, SLC4A9, and COL4A1, all of which have plausible roles in brain structural development, CSF secretion, and vascular formation.[12] However, these genes currently function as susceptibility loci rather than definitive causal genes, and most CM-I patients do not undergo routine genetic testing targeted at them.

In terms of gene ontology and molecular pathways, CM-I’s genetic architecture touches processes such as “cranial skeleton morphogenesis” (GO:0060034), “brain morphogenesis” (GO:0048854), “regulation of CSF secretion” (GO:0097474), and “vasculature development” (GO:0001944). HGNC IDs can be associated with candidate genes (OLFML2A: HGNC:18541; SLC4A9: HGNC:11034; COL4A1: HGNC:2218), and NCBI Gene IDs used for cross-species ortholog mapping. Nonetheless, it is critical for knowledge bases to represent CM-I as a complex, likely polygenic developmental trait rather than a single-gene disorder.

### 4.2 Pathogenic variants and variant classifications

Because no single gene is recognized as the principal CM-I gene, the literature does not yet provide a catalog of “pathogenic CM-I variants” in the ACMG sense. Instead, genetic studies report variants that alter posterior fossa size and skull base morphology, which in turn increase CM-I risk. Microarray analyses by Avşar et al. identified mutations in OLFML2A, SLC4A9, and COL4A1 in CM-I families, suggesting that these variants may play a role in the expression of CM-I phenotypes.[12] These could tentatively be classified as “likely pathogenic” or “risk alleles” for posterior fossa hypoplasia, but robust evidence and ClinVar annotations are still evolving, and their allele frequencies in population databases such as gnomAD are not yet fully interpreted in the context of CM-I.

Moreover, whole exome sequencing studies have identified linkage peaks rather than single variants, implying the presence of multiple rare variants across families. The NINDS study uses DNA polymorphic markers to identify chromosomal loci linked to the small posterior fossa phenotype, with a lod score of 3.0 taken as proof of linkage.[13] These findings underscore that structural traits like posterior fossa volume may be influenced by numerous variants with moderate effect sizes, and that CM-I arises when these variants combine with other developmental and environmental factors.

In knowledge bases, CM-I should be annotated with “Susceptibility variants associated with posterior fossa morphometry,” and variant types may include missense, nonsense, and regulatory variants affecting expression of developmental genes. These variants are germline rather than somatic, reflecting congenital cranial development. Functional consequences involve altered bone growth, CSF regulation, and vascular structure rather than direct neuronal loss-of-function or gain-of-function in classic signaling pathways.

### 4.3 Modifier genes, epigenetic information, and chromosomal abnormalities

Modifier genes likely play a role in determining CM-I severity and associated features such as syringomyelia, scoliosis, and cranial nerve involvement. For example, genes involved in connective tissue integrity, dural elasticity, and venous outflow might modulate how posterior fossa underdevelopment translates into clinical symptoms. Genetic syndromes such as achondroplasia, Klippel-Feil, Goldenhar, and X-linked aqueductal stenosis are reported in association with CM-I, reflecting shared cranial base development pathways, but none of these conditions have been genetically linked to CM-I in a direct causal manner.[12] Instead, they may represent overlapping developmental spectra with common pathways affecting skull base bone and CSF spaces.

Epigenetic mechanisms in CM-I have not been extensively studied. DNA methylation or histone modification changes affecting cranial base developmental genes could influence posterior fossa size, but no specific epigenetic signatures have been reported in CM-I patients. Likewise, chromosomal abnormalities such as large deletions or duplications are not characteristic of CM-I; rather, CNVs impacting cranial development genes might contribute in individual cases. DECIPHER and similar databases may eventually include structural variations associated with small posterior fossa traits, but current evidence remains limited.

Ontology suggestions for potential modifier processes include GO terms such as “regulation of ossification” (GO:0030278), “dura mater development” (GO:0060344), and “regulation of CSF circulation” (GO:0097471). CL terms for affected cell types might include “osteoblast” (CL:0000142) and “chondrocyte” (CL:0000138) in the cranial base, as well as “ependymal cell” (CL:0000138) lining the ventricles and “meningeal cell” (CL:0002494) in the dura.

### 4.4 Molecular profiling and advanced technologies

To date, CM-I has not been the focus of extensive transcriptomic, proteomic, or metabolomic profiling, likely because it is a structural disorder primarily managed surgically rather than a systemic molecular disease. There are no widely cited RNA-seq datasets comparing gene expression in CM-I posterior fossa tissue versus controls, nor proteomic studies of CSF in CM-I populations. However, CSF flow imaging studies using cine phase-contrast MRI provide a kind of “functional molecular imaging,” demonstrating altered CSF pulsation waveforms and velocities at the foramen magnum.[15][16] For example, Radiology 1995 work by Haughton et al. showed impaired systolic CSF flow pulsations immediately below the foramen magnum in CM-I patients, with improvement after decompressive surgery and good correlation with clinical improvement.[15]

Advanced technologies such as single-cell analysis and spatial transcriptomics have not yet been applied to CM-I in a systematic way, but future research could examine cell-type-specific responses in medullary and cerebellar tissue subjected to chronic compression, including astrocyte and microglial activation. Functional genomics screens, such as CRISPR or RNAi knockdown of candidate cranial development genes in model organisms, may eventually clarify which genes most strongly influence posterior fossa volume.

From an ontology perspective, these potential molecular studies would involve GO processes like “response to mechanical stimulus” (GO:0009612) and “glial cell activation” (GO:0014002), and CL terms such as “astrocyte” (CL:0000127) and “microglial cell” (CL:0000129). However, current CM-I knowledge is predominantly anatomical and hydrodynamic rather than molecular.

## 5. Environmental Information

### 5.1 Non-genetic contributing factors and CSF pressure environments

Non-genetic contributing factors to CM-I center on conditions that alter intracranial and spinal CSF pressure, particularly those that create sustained craniospinal gradients capable of pulling or pushing hindbrain structures through the foramen magnum. Milhorat’s pathogenesis review identifies hemodynamic disturbances such as hydrocephalus and bilateral chronic subdural hematomas as producing tonsillar herniation due to increased intracranial pressure.[4] In these settings, an otherwise normal posterior fossa can become functionally overcrowded, and the cerebellar tonsils may herniate downward in response to persistent pressure forces.

Mass lesions in the posterior fossa, including tumors or vascular malformations, can also cause local compression and displacement of cerebellar tissue into the foramen magnum, creating a secondary CM-I–like picture.[4] Surgical removal of the mass often relieves tonsillar impaction without the need for separate decompressive craniectomy, although CSF flow restoration must be monitored.

On the other side of the pressure spectrum, low spinal CSF pressure states such as lumbar-peritoneal shunts, overdraining ventriculoperitoneal shunts, or spontaneous spinal CSF leaks can cause downward traction on the brain and cerebellum.[4][19] As spinal CSF volume decreases, intracranial CSF redistributes and the brain descends to equalize pressures, leading to acquired tonsillar herniation and CM-I symptoms. The pathogenesis article notes that each mechanism acts on normal cerebellar tonsils to deform them by impacting them in the foramen magnum, and that this deformation is consistently reversed by surgery or correction of CSF flow that provides extra room at the foramen magnum.[4] This observation reinforces the notion that CM-I pathogenesis reflects mechanical impaction rather than intrinsic malformation of the tonsillar tissue.

Classic environmental toxins, radiation, and occupational exposures do not have established roles in CM-I etiology. However, lifestyle factors that influence venous pressure and CSF dynamics (such as chronic straining, heavy lifting, and intense coughing from lung disease) may exacerbate symptoms and contribute to progression in susceptible individuals with structural tonsillar ectopia.[19][20]

### 5.2 Lifestyle factors and infectious agents

Lifestyle factors are more relevant to symptom modulation than to primary causation. Physical activities involving frequent Valsalva maneuvers can provoke headaches and worsen symptoms in CM-I patients by accentuating craniospinal pressure gradients.[19][20] Conversely, avoiding activities that cause repeated high intrathoracic pressure may reduce symptom burden. Sleep hygiene and weight management can improve sleep-disordered breathing and reduce nocturnal hypoxia, indirectly benefiting medullary respiratory centers compressed by low-lying tonsils. Smoking, alcohol, and diet do not have specific documented effects on CM-I incidence or progression.

Infectious agents are not implicated in CM-I causation. CM-I is a non-infectious structural disorder, and while chronic meningitis or arachnoiditis can obstruct CSF flow and mimic some features, they do not cause true cerebellar tonsillar ectopia as defined radiologically. Thus, CM-I knowledge bases should annotate “no known infectious etiology” with reference to NCBI Taxonomy mapping.

### 5.3 Environmental and public health context

From a public health standpoint, CM-I does not arise from environmental contamination, radiation exposure, or endemic infections. However, awareness of iatrogenic factors such as CSF shunting practices is important. Clinical guidelines emphasize careful post-shunt monitoring for signs of low-pressure headache and acquired tonsillar herniation, and radiologists increasingly recognize “secondary Chiari” in patients with long-standing shunts.[4][10] Public health interventions focused on early detection of scoliosis and syringomyelia in pediatric populations with known CM-I can function as secondary prevention, enabling timely surgical decompression before advanced cord injury ensues.[17][19][20]

In ontology terms, environmental factors in CM-I can be represented via CHEBI (for CSF composition but not toxins) and via NCIT concepts such as “CSF shunt” and “spinal CSF leak” as procedural entities that modify disease expression.

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain from initiating lesion to clinical manifestation

The pathophysiology of CM-I can be articulated as a sequence of mechanistic steps connecting developmental posterior fossa underdevelopment and CSF dynamics to clinical phenotypes. Although these steps are derived from a synthesis of anatomical, imaging, and surgical data rather than direct experimental proof for every link, they provide a coherent causal narrative:

Step 1: Developmental underdevelopment of the posterior cranial fossa and occipital bone leads to a reduced bony compartment volume relative to the normal-sized hindbrain, resulting in posterior fossa overcrowding and caudal displacement of the cerebellar tonsils toward the foramen magnum.[1][4][11][12][13] This step is supported by morphometric MRI, genetic linkage, and surgical reversal data, and is considered demonstrated at a structural level.

Step 2: Caudal herniation of the cerebellar tonsils through the foramen magnum leads to mechanical impaction of tonsillar tissue within the osseous foramen and compression of adjacent neural structures, including the cervicomedullary junction and lower cranial nerve rootlets.[1][3][4][9][10] This step is directly visualized on MRI and at surgery.

Step 3: Impaction of the tonsils at the foramen magnum leads to obstruction of normal pulsatile CSF flow across the craniocervical junction, such that systolic CSF waves cannot freely transmit from intracranial subarachnoid spaces into the spinal compartment.[1][4][15][16][19][20] Cine phase-contrast MRI studies have demonstrated impaired systolic and altered diastolic CSF flow pulsations just below the foramen magnum in CM-I patients, with restoration after decompression.[15][16]

Step 4: Obstruction of CSF flow at the foramen magnum leads to abnormal craniospinal CSF pressure gradients, particularly during Valsalva maneuvers and cardiac cycles, resulting in local stretching, distension, and pain in posterior fossa dura and neural tissue, which manifests clinically as occipital and cough-induced headaches.[19][20] This step is inferred from hydrodynamic models (Gardner, Williams) and clinical correlation.

Step 5: Chronic abnormal CSF pressure transmission and mechanical compression at the cervicomedullary junction leads to dysfunction of brainstem nuclei, long tracts, and cerebellar pathways, resulting in neurological signs such as ataxia, cranial nerve deficits, autonomic disturbances, and sleep apnea.[3][9][10] This step is inferred from anatomical relationships and improvement after decompression.

Step 6: In many patients, obstructed CSF flow and craniospinal gradients lead to the development or enlargement of intramedullary syrinx cavities in the spinal cord (syringomyelia), via mechanisms described by Gardner’s hydrodynamic theory, Williams’ craniospinal gradient theory, Oldfield’s tonsillar piston theory, and intramedullary pulse pressure theory, resulting in spinal cord injury and phenotypes such as dissociated sensory loss, weakness, and scoliosis.[4][18][19][20] This step is strongly supported by imaging and surgical data.

Step 7: The combination of brainstem compression, syringomyelia, and chronic pain leads to progressive neurologic disability, scoliosis, and reduced quality of life, which can be partially reversed by interventions that restore CSF flow and relieve tonsillar impaction, such as posterior fossa decompression with or without duraplasty.[2][5][6][7][8][10][15][16] This step is demonstrated in surgical outcome studies.

These steps comprise a chain in which developmental bone underdevelopment (upstream) leads to tonsillar herniation, which leads to CSF flow obstruction and craniospinal pressure gradients, which in turn lead to neural compression, syrinx formation, and clinical disease (downstream). In acquired CM-I, Step 1 is replaced by shunt-induced low spinal pressure or posterior fossa mass, but the downstream CSF obstruction and syrinx mechanisms remain similar.[4][19][20]

### 6.2 CSF hydrodynamics and molecular pathways

At the level of CSF hydrodynamics, CM-I pathophysiology centers on disrupted pulsatile CSF flow and abnormal pressure wave propagation. Milhorat’s review concludes that “the pathophysiology of the Chiari I malformation is simply the obstruction of the normal pulsatile movement of CSF across the foramen magnum.”[4] Cine phase-contrast MRI studies in Radiology have quantitatively demonstrated that CM-I patients exhibit impaired systolic CSF flow pulsations just below the foramen magnum, while diastolic waveforms may remain relatively preserved; after posterior fossa decompression, systolic flow improves and correlates with clinical outcomes.[15] A larger outcome study of 130 patients showed that abnormal preoperative CSF flow (complete obstruction or reduced flow) was present in 81% of CM-I patients; interestingly, normal preoperative hindbrain CSF flow was an independent risk factor for treatment failure after decompression, suggesting that those with less severe obstruction may have more complex symptom drivers.[16]

Several mechanistic theories detail how CSF hydrodynamics lead to syringomyelia, particularly in CM-I. Gardner’s hydrodynamic theory proposes that obstruction of the fourth ventricle outflow through the foramen of Magendie leads to transmission of arterial pulsations into the central canal, with a “water hammer” effect that distends the canal and forms a syrinx; this theory emphasizes congenital obstruction and communication between the ventricle and central canal.[19][20] Williams’ theory focuses on craniospinal pressure gradients during events like coughing or Valsalva maneuvers, suggesting that increased intracranial venous pressure and CSF pressure cannot dissipate into the spinal compartment due to foramen magnum obstruction, creating a “valve-like” effect that drives CSF into the spinal cord and syrinx.[19][20] Oldfield’s theory, supported by dynamic MRI, shows downward movement of the cerebellar tonsils during systole, creating a piston effect in the spinal subarachnoid space that forces CSF through perivascular and interstitial spaces into the spinal cord, enlarging the syrinx.[19][20] Finally, the intramedullary pulsatile pressure theory posits that syringomyelia results from increased pulse pressure within the spinal cord relative to the subarachnoid space, causing accumulation of extracellular fluid and cavity formation.[19][20]

While these theories differ in emphasis, all invoke mechanistic pathways such as “CSF circulation” (GO:0097471), “regulation of fluid pressure” (GO:0046898), and “response to mechanical stimulus” (GO:0009612). They are not classic molecular signaling cascades like MAPK or PI3K-AKT, but they involve mechanobiology and fluid dynamics at the tissue level. Protein dysfunction is largely absent; instead, structural and hydrodynamic abnormalities dominate. One could conceptualize perivascular CSF movement and aquaporin-mediated water flux as molecular contributors, but CM-I is not currently framed in those molecular terms in the literature.

### 6.3 Cellular processes and tissue damage mechanisms

At the cellular and tissue level, CM-I pathophysiology involves several processes: mechanical compression-induced neural injury, astroglial and microglial activation, demyelination, and potential ischemia or microcirculatory compromise in compressed regions. Syringomyelia leads to cavitation within the spinal cord parenchyma, lined by glial cells; over time, expanding syrinxes compress adjacent white matter tracts and gray matter neurons, causing loss of spinothalamic fibers, motor neurons, and interneurons.[19][20] Tissue damage mechanisms include chronic mechanical stress, disruption of microcirculation, and stretch-induced axonal degeneration, which can be modeled via GO terms such as “axonal degeneration” (GO:0070507) and “response to hypoxia” (GO:0001666).

Brainstem compression can similarly cause microstructural damage to nuclei and long tracts. For example, compression of the dorsal columns and corticospinal tracts at the cervicomedullary junction leads to proprioceptive and motor deficits, while compression of respiratory centers and cranial nerve nuclei results in sleep apnea and bulbar dysfunction.[3][9][10] Astrocytes and microglia respond to chronic mechanical insult by proliferating and releasing cytokines, potentially contributing to local inflammation and further neuronal injury. CL ontology terms such as “astrocyte” (CL:0000127), “microglial cell” (CL:0000129), and “oligodendrocyte” (CL:0000128) are relevant cell types affected.

Metabolic changes are not a primary focus in CM-I, but chronic compression may induce local shifts in energy metabolism and oxidative stress in neural tissue. Ischemia due to microvascular compromise in syrinx walls or compressed medullary regions could lead to reactive oxygen species production and cell death, aligning with tissue damage mechanisms like “oxidative stress” (GO:0006979) and “neuron death” (GO:0070997). However, these mechanisms are inferred from general neuropathology rather than CM-I-specific molecular studies.

### 6.4 Immune system involvement and epigenetic changes

The immune system is not centrally implicated in CM-I pathogenesis. There is no evidence for autoimmune attack on posterior fossa structures or syrinx cavities, and inflammatory markers are not characteristic. However, local microglial activation and pro-inflammatory cytokine release may occur in chronically compressed regions, representing secondary neuroinflammatory processes rather than primary drivers. These could be annotated with GO terms such as “microglial cell activation” (GO:0001774) and “inflammatory response” (GO:0006954), but data are extrapolated from general CNS injury rather than CM-I-specific studies.

Epigenetic changes, such as DNA methylation or histone modification affecting cranial development genes, could theoretically influence posterior fossa size and CM-I risk, but no direct evidence exists. CM-I is thus not currently associated with disease-specific epigenetic profiles in ENCODE or Roadmap Epigenomics.

### 6.5 Upstream vs downstream mechanisms and cell-type involvement

Upstream mechanisms in CM-I include genetic determinants of posterior fossa bone development, occipital somite differentiation, and skull base ossification, as well as CSF pressure environments established by shunts or hydrocephalus.[4][11][12][13] These upstream processes act predominantly on bone and CSF compartments rather than on neural tissue. Cell types involved upstream include osteoblasts (CL:0000142), chondrocytes (CL:0000138), meningeal cells (CL:0002494), and ependymal cells (CL:0000138) lining ventricles.

Intermediate mechanisms involve mechanical impaction of cerebellar tonsils and obstruction of CSF flow across the foramen magnum. Here, key cell types include cerebellar neurons (Purkinje cells CL:0000121, granule cells CL:0000120), brainstem neurons (motor neurons CL:0000100, autonomic neurons), and endothelial cells (CL:0000115) lining subarachnoid vessels. Fluid dynamics in subarachnoid spaces and perivascular pathways (Virchow–Robin spaces) play a significant role.

Downstream mechanisms encompass neural tissue damage in the spinal cord and brainstem due to syringomyelia and compression, leading to clinical phenotypes. These involve neurons, oligodendrocytes, astrocytes, microglia, and vascular cells within the cord and medulla. GO processes include “myelination” (GO:0042552), “synaptic transmission” (GO:0007268), “muscle contraction” (GO:0006936), and “regulation of respiratory rhythm” (GO:0048389), all of which can be affected.

In summary, CM-I pathophysiology is dominated by structural, hydrodynamic, and mechanical mechanisms involving bone, CSF spaces, and neural tissue, with relatively limited direct involvement of classic molecular signaling cascades and immune pathways. Knowledge bases should emphasize these mechanobiological processes and anatomical relationships when encoding CM-I mechanisms.

## 7. Anatomical Structures Affected

### 7.1 Organ-level and body systems involvement

At the organ level, CM-I primarily affects the cerebellum (UBERON:0002037), specifically the cerebellar tonsils, and the brainstem (UBERON:0002038), particularly the medulla oblongata (UBERON:0002308). The occipital bone and posterior cranial fossa (UBERON:0003737) are key skeletal structures whose underdevelopment initiates the disorder.[1][3][4][9] Secondary organ involvement includes the cervical and upper thoracic spinal cord (UBERON:0002240 and UBERON:0002282), where syringomyelia often develops, and the respiratory system via medullary centers controlling breathing, which may be compromised leading to sleep apnea and respiratory dysrhythmias.[3][9][10]

The primary body system involved is the nervous system (UBERON:0001016), with subcomponents including the central nervous system (UBERON:0000010) and peripheral nervous system. The musculoskeletal system is secondarily affected through scoliosis and spinal deformity associated with syringomyelia.[17] The cardiovascular system plays a role in CSF pressure transmission but is not directly pathologic in CM-I. The endocrine, digestive, and genitourinary systems may be indirectly affected via autonomic dysfunction and neurogenic bladder, which reflect nervous system involvement rather than primary organ disease.[3][9][10]

### 7.2 Tissue and cell-level involvement

CM-I primarily affects neural tissue, including gray and white matter in the cerebellum, brainstem, and spinal cord. Neurons in these regions, such as Purkinje cells (CL:0000121), granule cells (CL:0000120), motor neurons (CL:0000100), sensory neurons, and autonomic neurons, can be functionally compromised by compression and syrinx-related injury.[3][9][19][20] Glial cells such as astrocytes (CL:0000127), oligodendrocytes (CL:0000128), and microglial cells (CL:0000129) are involved in response to chronic mechanical stress and may undergo activation, demyelination, or proliferation in damaged areas.

Connective tissue elements, including dura mater (a dense connective tissue membrane) and arachnoid mater, are also central to CM-I pathophysiology. Dural elasticity and thickness influence posterior fossa decompression outcomes and CSF leak risk, and duraplasty (augmentative graft of dura) is a core surgical technique.[5][6][7][8][10] Bone tissue (osteocytes, osteoblasts) in the occipital bone and cranial base is critical upstream, as underdevelopment of these tissues precipitates posterior fossa overcrowding.[4][11][12]

From a cellular compartment standpoint, subarachnoid spaces, central canal, and syrinx cavities represent tissue-level CSF reservoirs. Ependymal cells lining the central canal and syrinx walls may be disrupted, and perivascular spaces (part of the glymphatic system) contribute to fluid movement into and out of syrinxes.[19][20] CL terms for relevant cell types include “ependymal cell” (CL:0000138) and “meningeal cell” (CL:0002494).

### 7.3 Subcellular compartments and localization

Subcellular compartments are not primary drivers of CM-I, but the mechanical stress of compression may affect organelles such as mitochondria, leading to local energy deficits, and cytoskeleton, leading to axonal transport impairment. GO cellular component terms like “axon” (GO:0030424), “myelin sheath” (GO:0043209), and “node of Ranvier” (GO:0033268) are relevant to syrinx-related spinal cord injury. However, no CM-I-specific subcellular abnormalities have been described in the literature.

Localization in CM-I is strongly anatomical. Tonsillar ectopia occurs midline at the foramen magnum, but syrinxes can be asymmetric or centered, with variable lateralization affecting one side more than the other and contributing to asymmetric scoliosis.[17][19][20] Brainstem compression may be more ventral or dorsal depending on tonsillar shape and dural folds. These spatial patterns can be annotated using NeuroNames or UBERON regional terms such as “cervicomedullary junction” and “upper cervical spinal cord.”

In terms of lateralization, CM-I itself is a midline structural abnormality, but its consequences (syringomyelia, scoliosis, cranial nerve deficits) can be asymmetric. Knowledge bases should distinguish between midline underlying anatomy and lateralized phenotypes.

## 8. Temporal Development

### 8.1 Onset: congenital structure, delayed symptoms

CM-I is fundamentally a congenital structural condition, as posterior fossa underdevelopment and tonsillar position are determined during skull and hindbrain development. However, clinical symptom onset is often delayed, occurring in adolescence or adulthood after years of asymptomatic existence.[1][3][9][10] OMIM and multiple reviews note that CM-I is considered a congenital anomaly that is often asymptomatic in childhood and may become symptomatic later.[3][9][11][12] This delay reflects the time required for CSF dynamics, mechanical stress, and syrinx formation to reach a threshold where symptoms manifest.

Onset pattern is insidious and chronic rather than acute. Patients may report slowly worsening occipital headaches over years, gradually emerging gait instability, or progressive sensory changes in the arms. Sudden onset of severe symptoms is less typical, although acute deterioration can occur if a syrinx expands rapidly or if a CSF leak dramatically alters craniospinal pressure gradients.

### 8.2 Disease progression, stages, and duration

Progression in CM-I varies widely. Some individuals remain stable for years with mild headaches and no syringomyelia, while others experience stepwise or steadily progressive deterioration due to syrinx expansion and brainstem compression.[4][8][9][10][19][20] A conceptual staging might include: stage 1, asymptomatic tonsillar ectopia; stage 2, symptomatic headache and mild neurologic signs without syrinx; stage 3, syringomyelia development with spinal cord symptoms; and stage 4, advanced neurologic disability and scoliosis. However, formal staging systems have not been standardized in the literature.

Disease course patterns include episodic symptom flares (e.g., headache exacerbations) overlaying a chronic, slowly progressive baseline. Syringomyelia tends to progress over months to years, increasing cavity size and symptom burden, though some syrinxes remain stable. The duration of CM-I is lifelong, as the structural abnormality remains unless surgically corrected, but clinical disease can be halted or partially reversed by posterior fossa decompression, especially when performed early.

Posterior fossa decompression often induces a phase of improvement, followed by a stable plateau, though recurrences can occur due to scar tissue, incomplete decompression, or persistent CSF flow abnormalities.[6][7][8][10][16] Longitudinal cohort data show that early intervention in symptomatic children yields better outcomes and may prevent irreversible spinal cord damage.[10][17][19][20]

### 8.3 Remission patterns and critical periods

Spontaneous remission of CM-I symptoms is uncommon, though fluctuations occur. True remission, in which headaches and neurologic signs disappear without surgical intervention, may be seen in milder cases or those with reversible acquired components, such as shunt-related low pressure states that are corrected.[4][19] Treatment-induced remission is more common: posterior fossa decompression plus duraplasty frequently results in disappearance of headaches and gradual improvement in syringomyelia-related neurologic deficits, amounting to partial remission of clinical disease.[5][6][7][8][10][15][16]

Critical periods for intervention include adolescence and early adulthood when syringomyelia begins to develop and scoliosis emerges. Surgical series and pediatric neurosurgical guidelines emphasize that early decompression in symptomatic children is associated with better outcomes and less permanent neurologic deficit.[10][17] Dyste and Menezes suggested that symptomatic children with CM-I should undergo immediate surgery to optimize outcome, and multiple clinical series report 95–97% improvement in preoperative symptomatology following ample posterior fossa craniectomy and atlas laminectomy with duraplasty.[10]

In ontological terms, the temporal dimension can be captured with HPO onset modifiers (e.g., “adult onset” HP:0003581) and course descriptors (e.g., “progressive” HP:0003677, “episodic” HP:0002354). Knowledge bases should link age of onset and disease course to prognosis and intervention timing.

## 9. Inheritance and Population

### 9.1 Epidemiology: prevalence and incidence

Epidemiologic estimates of CM-I prevalence vary depending on whether radiologic or clinically symptomatic cases are counted. With increasing MRI use, incidental tonsillar ectopia is more commonly detected, suggesting that CM-I and low-lying tonsils may be present in 0.1–1% of the general population, though many remain asymptomatic. Orphanet and population imaging studies provide ranges but are not exhaustively cited in the provided sources. Surgical series represent a minority subset with symptomatic disease requiring intervention.

Incidence of clinically significant CM-I is lower, reflecting the proportion of patients who become symptomatic and are diagnosed. There are no robust global incidence data, but CM-I is generally classified as a rare disease in Orphanet. However, the boundary between “normal variant” tonsillar position and CM-I is somewhat arbitrary (e.g., ≥3–5 mm), complicating incidence estimates.

### 9.2 Inheritance pattern, penetrance, and expressivity

For familial CM-I, inheritance appears predominantly autosomal dominant with incomplete penetrance and variable expressivity. The largest pedigree study cited by the genetics review concluded an autosomal dominant inheritance pattern and higher incidence among women.[12] However, other studies support variable inheritance patterns, including autosomal recessive or multifactorial models, and emphasize that penetrance is incomplete, meaning that individuals carrying susceptibility alleles may have small posterior fossae without overt CM-I or symptoms.[11][12][13]

Expressivity is highly variable: some family members have severe CM-I with syringomyelia and scoliosis, while others have mild tonsillar descent and no symptoms. This variability reflects the interplay of genetic background, environmental exposures, and stochastic developmental factors. Genetic anticipation has not been described, and germline mosaicism is not a recognized phenomenon in CM-I.

Founder mutations have not been identified, consistent with the polygenic nature of the trait. Consanguinity does not have a clear role, as autosomal dominant and complex inheritance predominate. Carrier frequency for specific susceptibility variants is unknown, though posterior fossa morphology traits likely have continuous distribution in the population.

### 9.3 Population demographics and sex ratio

Population demographics show that CM-I affects both sexes, with several series reporting a female predominance, particularly in familial cases.[9][10][12][17] For example, the scoliosis–CM-I–syrinx study found that female sex was independently associated with scoliosis in the pediatric MRI cohort, and syrinx presence (rather than CM-I alone) was strongly associated with spinal deformity.[17] Age distribution of CM-I diagnoses is skewed toward adolescence and young adulthood, reflecting both symptom onset and increased use of MRI in these age groups.

Geographic distribution of CM-I is global, with cases reported in multiple countries. There are no well-established ethnic differences in prevalence, though genetic susceptibility loci may vary in frequency across populations. Knowledge bases may annotate CM-I as not restricted to specific ancestries, with gnomAD providing general variant frequencies for candidate genes.

In summary, CM-I exhibits complex inheritance, incomplete penetrance, variable expressivity, and modest female predominance, with a global distribution and rare disease classification in clinical registries.

## 10. Diagnostics

### 10.1 Imaging studies and CSF flow assessment

MRI of the brain and cervical spine is the cornerstone of CM-I diagnosis. Radiologically, CM-I is defined as descent of the cerebellar tonsils of 5 mm or more below the foramen magnum on midsagittal MRI, though thresholds vary; the OMIM entry and multiple clinical reviews adopt this definition.[1][3][9] The NINDS genetic study uses a threshold of ≥2 mm below the foramen magnum to define a CM-I phenotype for linkage analysis, reflecting a more inclusive radiologic criterion.[13] MRI also assesses posterior fossa volume, skull base bone length, and presence of associated anomalies such as syringomyelia, scoliosis, and hydrocephalus.

Cine phase-contrast MRI provides dynamic assessment of CSF flow. Radiology studies by Haughton and subsequent work have examined cardiac cycle-related CSF flow pulsations in CM-I, demonstrating impaired systolic flow immediately below the foramen magnum and improvement after decompressive surgery.[15] A large outcome study in Neurosurgery (PMID:16823310) found that abnormal hindbrain CSF flow (complete obstruction or reduced flow) was present in 81% of CM-I patients preoperatively, and that normal preoperative CSF flow was an independent risk factor for treatment failure after decompression, with a relative risk of symptom recurrence of 4.85.[16] These findings suggest that cine MRI can help identify which patients are most likely to improve with posterior fossa decompression.

Imaging of the spinal cord, particularly cervical and upper thoracic segments, is critical to detect syringomyelia and to characterize syrinx size, location, and morphology.[8][17][19][20] Scoliosis is assessed via spinal radiographs and correlated with syrinx presence. CT scans are less useful for CM-I but can evaluate bony posterior fossa anatomy.

RadLex and SNOMED CT provide imaging procedure codes and diagnostic concept mappings for “MRI of brain and cervical spine,” “cine phase-contrast MRI,” and “syringomyelia.” Knowledge bases should link CM-I diagnostics to imaging ontologies.

### 10.2 Clinical tests, biomarkers, and electrophysiology

There are no specific blood, urine, or CSF biochemical biomarkers for CM-I. Routine laboratory tests are generally normal, and CSF composition is not characteristic. Biopsy of posterior fossa tissue is not performed, given the structural nature of the disease and the risks involved.

Electrophysiology, such as EMG and nerve conduction studies, may be used to assess peripheral nerve and muscle function in syringomyelia-associated weakness, but these tests are not specific to CM-I. EEG is generally normal and not part of CM-I diagnostics. Sleep studies (polysomnography) may be indicated in patients with suspected sleep apnea due to brainstem compression, providing functional assessment of respiratory control.[3][9][10]

Thus, CM-I diagnostics rely overwhelmingly on imaging and clinical neurological examination rather than laboratory or electrophysiologic biomarkers. Future research might explore CSF proteomics or metabolomics, but current practice does not include such tests.

### 10.3 Genetic testing approaches

Given the absence of a single causal gene, genetic testing for CM-I is not routine. The NINDS genetic linkage study uses genomic DNA from affected families to identify chromosomal loci associated with posterior fossa underdevelopment, but this is research rather than clinical testing.[13] ClinVar and GTR do not list dedicated CM-I gene panels; instead, craniofacial and skeletal anomaly panels may include candidate genes that overlap with CM-I susceptibility.

Whole exome or genome sequencing may be considered in families with multiple affected members and other craniofacial anomalies, but the yield for CM-I-specific diagnostics is uncertain. Chromosomal microarray and karyotyping may detect large structural variants in syndromic cases, but these are not characteristic for isolated CM-I. Thus, genetic testing is more exploratory and research-focused in CM-I than in well-defined monogenic disorders.

### 10.4 Clinical diagnostic criteria and differential diagnosis

Clinical diagnosis of CM-I integrates imaging criteria (tonsillar descent, posterior fossa morphology, syringomyelia) with symptoms and neurological signs. Society guidelines and review articles emphasize that surgical treatment is reserved for symptomatic CM-I patients with radiographic evidence of hindbrain abnormalities; asymptomatic individuals are generally observed.[10] The Pediatric Section of the American Association of Neurological Surgeons has clearly stated that surgical decompression has no indication as prophylactic treatment in asymptomatic children.[10]

Differential diagnosis includes conditions that can mimic CM-I symptoms or imaging findings: intracranial hypotension with downward brain sagging, posterior fossa tumors, hydrocephalus-related tonsillar descent, craniosynostosis, and normal variants of tonsillar position. Distinguishing features include clinical history (e.g., orthostatic headache in intracranial hypotension), imaging signs (e.g., pachymeningeal enhancement), and presence of mass lesions. Radiologists must differentiate true CM-I from incidental low tonsils and secondary tonsillar herniation due to other pathologies.

### 10.5 Screening and early detection

Population screening for CM-I is not recommended, and newborn screening does not include CM-I. However, targeted imaging may be considered in certain high-risk contexts: children with unexplained scoliosis and neurologic signs, individuals with familial CM-I, or patients with chronic cough headaches. MRI is the screening method of choice, and cine MRI can be used to assess CSF flow.

Genetic screening for CM-I risk is not currently available, though future identification of robust susceptibility loci could enable risk stratification in families. Genetic counseling may be offered to families with multiple affected members, focusing on recurrence risk and early symptom recognition rather than specific gene testing.[11][12][13]

## 11. Outcome and Prognosis

### 11.1 Survival, life expectancy, and mortality

CM-I is rarely directly fatal, and life expectancy for individuals with CM-I is generally near normal when appropriately managed. Mortality rates are low in surgical series, and posterior fossa decompression is associated with low perioperative mortality and acceptable morbidity.[6][8][10] However, severe brainstem compression, advanced syringomyelia, and untreated sleep apnea can contribute to increased morbidity and, in rare cases, mortality.

Disease-specific mortality—deaths directly attributable to CM-I—is uncommon but may occur in patients with severe bulbar dysfunction, respiratory failure, or complications of surgery such as malignant brainstem edema. Overall, CM-I prognosis in terms of survival is favorable compared to many neurological disorders, but quality of life and disability can be significantly impacted.

### 11.2 Morbidity, disability outcomes, and quality of life

Morbidity in CM-I is substantial, particularly in symptomatic patients with syringomyelia. Chronic pain, neurologic deficits, scoliosis, and sleep disturbance lead to long-term disability and reduced HRQOL. Many patients are unable to work full-time or engage in normal activities due to headaches, dizziness, and limb weakness. Disability outcomes vary: some patients achieve near-complete functional recovery after decompression, while others have persistent deficits, particularly if intervention was delayed.

Quality-of-life measures such as EQ-5D and SF-36 have been applied in CM-I cohorts, showing impairment in physical functioning, pain, and social domains, with improvement after surgery.[2][6][8][10] For example, posterior fossa decompression plus duraplasty in syringomyelia-associated CM-I has been reported to achieve 60–100% clinical improvement, including reduced pain and improved neurologic function.[8] However, CSF-related complications such as pseudomeningocele, CSF leak, and aseptic meningitis can temporally worsen quality of life.

Disability registries and ICF (International Classification of Functioning) frameworks can annotate CM-I-related impairments in domains such as mobility, self-care, and interpersonal interactions. Knowledge bases should link CM-I to such disability descriptions.

### 11.3 Disease course, complications, and recovery potential

Complications of CM-I include syringomyelia, scoliosis, sleep apnea, neurogenic bladder, and cranial nerve palsies. Surgical complications include CSF leaks, pseudomeningocele, aseptic meningitis, infection, and, rarely, new neurological deficits.[6][7][8][10] A systematic review and meta-analysis comparing posterior fossa decompression with and without duraplasty found that duraplasty was associated with higher CSF-related complication rates but lower recurrence rates and better syrinx resolution in patients with syringomyelia.[7]

Recovery potential hinges on early diagnosis and intervention. Syringomyelia-related symptoms can improve after decompression, especially when syrinx size decreases; syrinx resolution rates of ~80% have been reported with posterior fossa decompression plus duraplasty in CM-I–associated syringomyelia.[8] However, longstanding spinal cord damage may be irreversible, and some patients continue to experience pain and weakness despite syrinx shrinkage. Brainstem-related symptoms and headaches often improve significantly after decompression, reflecting restoration of CSF flow and relief of mechanical compression.[6][8][10][15][16]

Prognostic factors include age at diagnosis, severity of syringomyelia, degree of CSF flow obstruction, presence of scoliosis, and timing of surgery. Abnormal hindbrain CSF flow on cine MRI correlates with better response to decompression, whereas normal preoperative CSF flow is associated with higher risk of treatment failure.[16] These imaging findings can serve as prognostic biomarkers.

### 11.4 Prognostic biomarkers and prediction

Prognostic biomarkers in CM-I are primarily imaging-based rather than molecular. Cine phase-contrast MRI CSF flow patterns, syrinx size and morphology, and posterior fossa morphometry provide predictive information. As noted, normal preoperative CSF flow at the foramen magnum was an independent risk factor for symptom recurrence after decompression, with a hazard ratio of 4.85, suggesting that patients whose symptoms are not driven by severe CSF obstruction may have more complex or non-mechanical pain mechanisms.[16]

Syrinx characteristics (length, diameter, location) and scoliosis severity also predict outcomes. Larger syrinxes and more severe scoliosis may require more complex interventions and carry greater risk of incomplete recovery.[8][17][19][20] Age and sex may influence prognosis, with younger patients and those with shorter symptom duration experiencing better outcomes.

In ontology terms, NCIT can link these imaging biomarkers to concepts such as “prognostic factor” and “radiologic biomarker.” Knowledge bases should encode the association between CSF flow obstruction and surgical outcome in CM-I.

## 12. Treatment

### 12.1 Surgical and interventional therapies

Surgical intervention is the mainstay of treatment for symptomatic CM-I, particularly when syringomyelia or significant neurologic deficits are present. Posterior fossa decompression (PFD), often combined with C1 laminectomy and duraplasty, is the standard approach.[2][5][6][7][8][10] The basic goal of all modern surgical procedures is to restore normal CSF circulation at the level of the foramen magnum by decompressing the inferior cerebellum and cervicomedullary region, reestablishing pressure balance between intracranial and intraspinal subarachnoid spaces.[10]

PFD typically involves suboccipital craniectomy to enlarge the posterior fossa, removal of the posterior arch of C1 (atlas laminectomy), and, in many cases, opening the dura and expanding it with a graft (duraplasty).[5][6][10] A simplified technique described by Iskandar et al. uses a curvilinear dural incision and autologous pericranial graft; in a series of 14 symptomatic CM-I patients, including eight with syrinx, neurologic signs and symptoms improved or were unchanged in all, syrinx size decreased in all, and no patient developed new neurologic deficits, CSF leak, pseudomeningocele, or infection.[6] This supports posterior fossa decompression with duraplasty as a safe and effective procedure for CM-I.

A systematic review and meta-analysis comparing PFD without duraplasty versus PFD with duraplasty (PFDD) found that PFDD led to greater clinical improvement in patients with syringomyelia, lower recurrence rates, but higher CSF-related complication rates, including CSF leak, aseptic meningitis, and pseudomeningocele.[7] In patients without syringomyelia, PFD without duraplasty achieved similar clinical improvement with fewer complications and lower costs, suggesting that duraplasty can be reserved for those

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 76 |
| Resolved | 70 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 53 |
| Terms named correctly | 27 |
| Terms named as a **different** term | 19 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002450` (2 mentions) - the report calls it "syringomyelia"; HP calls it **Abnormal motor neuron morphology**
- `GO:0097474` (2 mentions) - the report calls it "regulation of CSF secretion"; GO calls it **retinal cone cell apoptotic process**
- `HP:0002650` (3 mentions) - the report calls it "abnormality of skull base", "scoliosis"; HP calls it **Scoliosis**
- `HP:0002781` (1 mention) - the report calls it "abnormal CSF pressure"; HP calls it **Upper airway obstruction**
- `GO:0097471` (3 mentions) - the report calls it "regulation of CSF circulation", "CSF circulation"; GO calls it **mossy fiber rosette**
- `HP:0002363` (2 mentions) - the report calls it "neck pain"; HP calls it **Abnormal brainstem morphology**
- `HP:0002149` (2 mentions) - the report calls it "cough headache"; HP calls it **Hyperuricemia**
- `HP:0002313` (1 mention) - the report calls it "motion-induced headache"; HP calls it **Spastic paraparesis**
- `HP:0000013` (1 mention) - the report calls it "neurogenic bladder"; HP calls it **Hypoplasia of the uterus**
- `GO:0060088` (1 mention) - the report calls it "vestibular receptor cell–neuronal signaling"; GO calls it **auditory receptor cell stereocilium organization**
- `GO:0007601` (1 mention) - the report calls it "regulation of eye movement"; GO calls it **visual perception**
- `GO:0060034` (1 mention) - the report calls it "cranial skeleton morphogenesis"; GO calls it **notochord cell differentiation**
- `GO:0060344` (1 mention) - the report calls it "dura mater development"; GO calls it **liver trabecula formation**
- `CL:0000142` (2 mentions) - the report calls it "osteoblast"; CL calls it **hyalocyte**
- `CL:0000138` (5 mentions) - the report calls it "chondrocyte", "ependymal cell"; CL calls it **chondrocyte**
- `GO:0014002` (1 mention) - the report calls it "glial cell activation"; GO calls it **astrocyte development**
- `GO:0046898` (1 mention) - the report calls it "regulation of fluid pressure"; GO calls it **response to cycloheximide**
- `GO:0070507` (1 mention) - the report calls it "axonal degeneration"; GO calls it **regulation of microtubule cytoskeleton organization**
- `GO:0048389` (1 mention) - the report calls it "regulation of respiratory rhythm"; GO calls it **intermediate mesoderm development**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `UBERON:0003737` (2 mentions) - UBERON does not contain this term
- `HP:0003479` (3 mentions), reported as "dissociated sensory loss" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0070997` (obsolete neuron death) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002315` (3 mentions) - the report calls it "occipital headache"; HP calls it **Headache**
- `HP:0001251` (3 mentions) - the report calls it "cerebellar ataxia"; HP calls it **Ataxia**, and lists "Cerebellar ataxia" among its other names
- `HP:0003202` (1 mention) - the report calls it "muscle atrophy"; HP calls it **Skeletal muscle atrophy**, and lists "Muscle atrophy" among its other names
- `CL:0002494` (3 mentions) - the report calls it "meningeal cell"; CL calls it **cardiocyte**, and lists "heart cell" among its other names
- `GO:0006979` (1 mention) - the report calls it "oxidative stress"; GO calls it **response to oxidative stress**
- `GO:0070997` (1 mention) - the report calls it "neuron death"; GO calls it **obsolete neuron death**, and lists "neuron cell death" among its other names
- `GO:0007268` (1 mention) - the report calls it "synaptic transmission"; GO calls it **chemical synaptic transmission**, and lists "synaptic transmission" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0002650` - called "abnormality of skull base", "scoliosis"
- `GO:0097471` - called "regulation of CSF circulation", "CSF circulation"
- `CL:0000138` - called "chondrocyte", "ependymal cell"