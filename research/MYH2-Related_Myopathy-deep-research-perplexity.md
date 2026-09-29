---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-28T13:09:41.921324'
end_time: '2026-09-28T13:16:19.996345'
duration_seconds: 398.08
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: MYH2-Related Myopathy
  mondo_id: MONDO:0011577
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
citation_count: 19
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 10
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 44
  verified: 38
  not_found: 2
  obsolete: 2
  unverifiable: 2
  confabulation_rate: 0.048
  labels_checked: 39
  labels_matching: 14
  labels_mismatched: 18
  mislabelled_terms:
  - term_id: HP:0000622
    reported_labels:
    - External ophthalmoplegia
    ontology_label: Blurred vision
  - term_id: HP:0001769
    reported_labels:
    - Scapular winging
    ontology_label: Broad foot
  - term_id: HP:0007340
    reported_labels:
    - Cytoplasmic inclusion bodies in muscle fibers
    ontology_label: Lower limb muscle weakness
  - term_id: HP:0003457
    reported_labels:
    - Myopathic EMG pattern
    ontology_label: EMG abnormality
  - term_id: HP:0003215
    reported_labels:
    - Abnormal muscle MRI
    ontology_label: Elevated urinary dicarboxylic acid level
  - term_id: HP:0001324
    reported_labels:
    - Fatigue
    ontology_label: Muscle weakness
  - term_id: HP:0002355
    reported_labels:
    - Reduced activity tolerance
    ontology_label: obsolete Difficulty walking
  - term_id: GO:0048747
    reported_labels:
    - muscle fiber maturation
    ontology_label: GO_0048747
  - term_id: HP:0100806
    reported_labels:
    - Autophagic vacuoles in muscle fibers
    ontology_label: Sepsis
  - term_id: GO:0048754
    reported_labels:
    - branching involved in skeletal muscle organ development
    ontology_label: branching morphogenesis of an epithelial tube
  - term_id: GO:0009898
    reported_labels:
    - cytoplasmic protein catabolic process
    ontology_label: cytoplasmic side of plasma membrane
  - term_id: CL:0000670
    reported_labels:
    - fast-twitch skeletal muscle fiber
    ontology_label: primordial germ cell
  - term_id: CL:0000700
    reported_labels:
    - extraocular muscle cell
    ontology_label: dopaminergic neuron
  - term_id: UBERON:0002106
    reported_labels:
    - skeletal muscle tissue
    ontology_label: spleen
  - term_id: UBERON:0001630
    reported_labels:
    - extraocular skeletal muscle
    ontology_label: muscle organ
  - term_id: UBERON:0000948
    reported_labels:
    - thigh
    ontology_label: heart
  - term_id: UBERON:0008891
    reported_labels:
    - eyelid
    ontology_label: external gill
  - term_id: UBERON:0002108
    reported_labels:
    - skeletal muscle of head
    ontology_label: small intestine
  labels_variant: 7
  unresolved_terms:
  - HP:0003483
  - HP:0003723
  obsolete_terms:
  - term_id: HP:0002355
    ontology_label: obsolete Difficulty walking
    replaced_by: HP:0001288
  - term_id: GO:0048747
    ontology_label: GO_0048747
    replaced_by: GO:0055001
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MYH2-Related Myopathy
- **MONDO ID:** MONDO:0011577 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MYH2-Related Myopathy** covering all of the
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

# MYH2-Related Myopathy (MONDO:0011577): Comprehensive Disease Characteristics and Mechanisms

MYH2-related myopathy is a rare Mendelian muscle disease caused by germline variants in the *MYH2* gene encoding the fast type IIa skeletal muscle myosin heavy chain, and it presents as a spectrum of autosomal dominant and autosomal recessive congenital myopathies characterized by proximal limb weakness and chronic external ophthalmoplegia, with distinctive fiber-type–specific pathology involving selective reduction or loss of type 2A fibers and, in dominant forms, rimmed vacuoles and inclusion-body–like changes.[2][4][5][7][15] Clinical series and gene curation efforts indicate that MYH2-associated disease, also catalogued as “congenital myopathy 6 with ophthalmoplegia” (CMYO6; OMIM 605637), is typically mild to moderate in severity, with onset in childhood or adolescence and a slowly progressive or nonprogressive course, although recent reports have expanded the spectrum to include adult-onset chronic progressive external ophthalmoplegia (CPEO) with minimal limb involvement and dominant myopathy without congenital contractures or ocular signs.[5][9][10] From a mechanistic perspective, dominantly acting missense mutations, exemplified by the classic E706K substitution in the SH1 helix of the myosin motor domain, are thought to exert a dominant-negative effect that perturbs sarcomeric assembly, induces myofibrillar disorganization, and promotes protein aggregation with rimmed vacuole formation, whereas recessive truncating and splice-site variants cause loss of functional MyHC IIa, leading to developmental absence of type 2A fibers and a different histopathological and clinical profile.[3][7][12][15] Experimental models, including expression of IBM3 mutations in muscle cells and invertebrate myosin systems, support the view that MYH2 dysfunction disturbs actin–myosin cross-bridge cycling, fiber-type specification, and proteostasis, thereby linking a single gene defect to complex tissue-level and clinical manifestations.[12][15] This report synthesizes current knowledge on MYH2-related myopathy across domains of disease information, etiology, phenotypes, molecular genetics, pathophysiology, anatomy, natural history, diagnostics, outcome, treatment, prevention, comparative biology, and model organisms, with emphasis on primary literature and recent work refining the clinical spectrum.[3][4][7][9][10][14][15][16]  

## 1. Disease Information  

### 1.1 Definition and Overview  

MYH2-related myopathy is a hereditary skeletal muscle disorder caused by germline variants in the *MYH2* gene that encodes the fast type IIa myosin heavy chain (MyHC IIa), an essential motor protein of fast-twitch skeletal muscle fibers.[2][4][7][15] OMIM lists the clinical phenotype under entry #605637, “congenital myopathy 6 with ophthalmoplegia” (CMYO6), and notes that it is “a relatively mild muscle disorder characterized by childhood onset of symptoms,” with both autosomal dominant and autosomal recessive forms linked to *MYH2* mutations at 17p13.1.[5] The disease is part of the broader group of “hereditary myosin myopathies,” which comprises disorders caused by mutations in skeletal myosin heavy chain genes (*MYH2*, *MYH3*, *MYH7*, *MYH8*), distinguished by fiber-type specificity and clinical presentation.[4][7] In MYH2-related disease, the most consistent clinical feature across inheritance patterns is external ophthalmoplegia—restriction of extraocular movements often accompanied by ptosis—reflecting involvement of extraocular muscles that normally express MyHC IIa.[3][4][5][7][9] Limb-girdle and proximal muscle weakness, sometimes preceded by transient congenital joint contractures (arthrogryposis), constitutes the major systemic manifestation, and muscle biopsy reveals characteristic alterations of fiber type composition and structure, which differ between dominant and recessive forms.[3][4][7][14][15]  

Early reports adopted the term “hereditary inclusion-body myopathy type 3” (IBM3) for the dominantly inherited form associated with the E706K MYH2 mutation, because muscle biopsies showed dystrophic changes, rimmed vacuoles, and intranuclear and cytoplasmic inclusions reminiscent of inclusion body myositis.[12][14] Darin and colleagues first mapped the disease locus to chromosome 17p13.1 and later studies identified the MYH2 missense mutation as causative, renaming the condition as “MyHC IIa myopathy.”[2][5][7][12] Subsequent series from Tajsharghi, Lossos, and others described recessively inherited MYH2 myopathy with external ophthalmoplegia, mild to moderate generalized weakness, and complete absence of type 2A fibers, thereby establishing that both dominant negative and loss-of-function mechanisms affecting the same fast myosin isoform can produce overlapping yet distinguishable clinical entities.[3][15][16] ClinGen has curated MYH2 as a gene with definitive evidence for autosomal recessive proximal myopathy and ophthalmoplegia (MONDO:0011577), and notes separate evidence for autosomal dominant disease via distinct mutational mechanisms.[15][16]  

### 1.2 Key Identifiers and Classification  

The key identifiers for MYH2-related myopathy span multiple clinical and ontological databases. OMIM assigns the disease entry #605637, “congenital myopathy 6 with ophthalmoplegia,” and links it to the gene entry 160740 for “MYOSIN, HEAVY CHAIN 2, SKELETAL MUSCLE,” located at cytogenetic band 17p13.1.[2][5] The gene itself is designated *MYH2* by HGNC (HGNC:7572) and is annotated in NCBI Gene (Gene ID: 4620) as “myosin heavy chain 2,” described as a conventional class II myosin heavy chain that functions in skeletal muscle contraction and resides within a cluster of myosin heavy chain genes on chromosome 17.[1][2] The MONDO ontology assigns MONDO:0011577 to “myopathy, proximal, and ophthalmoplegia,” a concept used in ClinVar and ClinGen to capture MYH2-associated disease.[15][17] Orphanet recognizes MYH2-related conditions within the group of congenital myopathies and links them to the same OMIM identifier, though detailed Orphanet entries are not fully represented in the provided search results.[5][17]  

In clinical taxonomies, MYH2-related myopathy falls within the category of congenital myopathies and hereditary myosin myopathies, and more broadly under neuromuscular diseases involving skeletal muscle.[4][7] ICD-10 and ICD-11 do not provide a fully specific code for MYH2-related disease, and affected individuals are generally coded under categories such as “other specified myopathies” (e.g., ICD-10 G72.8) or “hereditary progressive muscular dystrophies” depending on local coding practices. The Human Phenotype Ontology (HPO) maps key clinical manifestations such as proximal muscle weakness (HP:0003690), external ophthalmoplegia (HP:0000622), ptosis (HP:0000508), arthrogryposis (HP:0002829), and rimmed vacuoles on muscle biopsy (HP:0003483), providing standardized phenotype terms that can be linked to the disease concept MONDO:0011577.[5][7][14][15][16]  

The gene and disease are also represented in specialty resources. PanelApp (Australia) includes *MYH2* on the “Muscular dystrophy and myopathy – Paediatric” panel, describing both monoallelic and biallelic variants causing proximal myopathy and ophthalmoplegia and summarizing more than ten families with bi-allelic variants and at least two missense variants with monoallelic disease.[16] ClinVar lists multiple variants in *MYH2* associated with “myopathy, proximal, and ophthalmoplegia,” including pathogenic splice-site and truncating mutations as well as variants of uncertain significance (VUS) such as NM_017534.6(MYH2):c.1266+5G>C.[17] ClinVarMiner and related tools catalog benign MYH2 variants with relatively high allele frequencies in gnomAD, underscoring the importance of variant-level interpretation for this gene.[11][13] Collectively, these identifiers and classifications confirm that MYH2-related myopathy is recognized as a distinct Mendelian neuromuscular disease entity in major biomedical ontologies and databases.[2][5][7][15][16][17]  

### 1.3 Nomenclature and Synonyms  

MYH2-related myopathy has accumulated several synonyms and alternative names over the course of its characterization, reflecting evolving understanding of its pathology and genetics. OMIM uses the term “congenital myopathy 6 with ophthalmoplegia” (CMYO6) to describe the unified phenotype associated with *MYH2* mutations, noting that both autosomal dominant and autosomal recessive forms share a broadly similar clinical picture of childhood-onset muscle weakness with ophthalmoplegia.[5] The dominant form originally received the designation “hereditary inclusion body myopathy type 3” (IBM3) or “inclusion body myopathy-3,” due to the presence of rimmed vacuoles and inclusion bodies on muscle biopsy that resembled inclusion body myositis.[2][5][7][12][14] ClinVar and MedGen list synonyms such as “MYOPATHY WITH CONGENITAL JOINT CONTRACTURES, OPHTHALMOPLEGIA, AND RIMMED VACUOLES,” “inclusion body myopathy autosomal dominant,” and “myopathy, proximal, and ophthalmoplegia,” integrating both clinical and pathological descriptors.[5][17]  

In specialist literature, the dominant phenotype is often referred to as “MyHC IIa myopathy” or “MYH2 myopathy,” emphasizing the specific isoform and gene.[4][7][12] Tajsharghi and colleagues introduced the term “recessive myosin myopathy with external ophthalmoplegia” for bi-allelic MYH2 loss-of-function variants, highlighting the recessive nature and the myosin basis of disease.[3] More recently, the JND report by Baskar et al. used “MYH2-related myopathy” in the context of chronic progressive external ophthalmoplegia (CPEO), and stressed that “MYH2 myopathy has to be considered in adult patients with CPEO,” thereby integrating the disease into the wider CPEO spectrum.[9] Cassini et al. likewise used “MYH2-associated myopathy” for a family with a novel splice-site variant and atypical phenotype lacking ophthalmoplegia, indicating that the MYH2 term can encompass diverse clinical presentations linked by the underlying gene defect.[10]  

These various names map onto the same underlying gene–disease relationship. For the purposes of knowledge-base integration, “MYH2-related myopathy” and “myopathy, proximal, and ophthalmoplegia (MONDO:0011577)” can be treated as umbrella terms encompassing autosomal dominant MyHC IIa myopathy (IBM3), autosomal recessive myosin myopathy with external ophthalmoplegia, and emerging atypical presentations such as MYH2-associated CPEO without skeletal abnormalities.[3][4][5][7][9][10][14][15][16]  

### 1.4 Data Sources and Evidence Types  

Information on MYH2-related myopathy is largely derived from aggregated disease-level resources and case-series in the published literature rather than from large-scale individual EHR datasets, reflecting the rarity of the condition. OMIM summarizes clinical, genetic, and mapping data from family studies and linkage analyses, including the mapping of IBM3 to chromosome 17p13.1 and subsequent identification of MYH2 mutations.[2][5] ClinGen curations synthesize evidence from multiple probands and families with bi-allelic MYH2 variants, citing key publications such as Tajsharghi et al. (2010, PMID: 20418530), Lossos et al. (2013, PMID: 23388406), and Tajsharghi et al. (2014, PMID: 24193343), and rate the gene–disease relationship as “definitive” for autosomal recessive proximal myopathy and ophthalmoplegia.[15]  

Primary clinical data are provided by human case reports and series describing individuals and kindreds with specific MYH2 variants, supported by detailed clinical examination, neurophysiology, imaging, and histopathology.[3][4][9][10][12][14] For example, Tajsharghi et al. reported families with homozygous or compound heterozygous truncating MYH2 mutations, documenting muscle biopsies with small or absent type 2A fibers and reduced MyHC IIa expression, and concluded that “mild muscle weakness and ophthalmoplegia in combination with muscle biopsy demonstrating small or absent type 2A muscle fibers are the hallmark of recessive myopathy associated with MYH2 mutations.”[3] Cassini et al. presented three affected individuals from a four-generation family with a novel splice-site variant c.5673+1G>C, demonstrating segregation of the variant with disease and functional evidence of abnormal splicing.[10]  

Experimental evidence arises from model systems and in vitro studies examining the IBM3 mutation and other MYH2 variants. A notable example is the expression of the inclusion-body myopathy 3 E706K mutation in myosin heavy chain IIa, which was shown to cause misfolding, myofibrillar disorganization, and inclusion-body formation in cellular models.[12] ClinGen highlights expression evidence of MyHC IIa in type IIa muscle fibers (PMID: 7545970) and a *Caenorhabditis elegans* model (PMID: 16130113) supporting the biological role of MYH2 orthologs in fast muscle function.[15] Together, these aggregated resources and primary studies provide a robust evidence base for articulating the disease characteristics of MYH2-related myopathy.  

## 2. Etiology  

### 2.1 Primary Causal Factors: Genetic Basis  

The primary causal factor in MYH2-related myopathy is germline mutation in the *MYH2* gene, which encodes the myosin heavy chain isoform expressed in fast type 2A muscle fibers and, in some species, also in 2B fibers.[2][4][7][15] OMIM explains that “The MYH2 gene encodes the myosin heavy chain isoform that is expressed in fast type 2A muscle fibers,” and notes that heterozygous, compound heterozygous, or homozygous mutations can cause CMYO6.[2][5] ClinGen’s gene–disease curation explicitly concludes that “MYH2 is definitively associated with autosomal recessive proximal myopathy and ophthalmoplegia” and separately acknowledges autosomal dominant MYH2 myopathy with a proposed dominant-negative mechanism.[15]  

Dominant disease is primarily linked to missense mutations in highly conserved regions of the myosin motor domain, most famously the E706K substitution in the SH1 helix.[2][7][12][14] This mutation replaces a negatively charged glutamate at position 706 with a positively charged lysine, and is located in the core of the motor domain, a region highly conserved through evolution.[2][7] Martinsson et al. (2000) identified E706K in affected members of a Swedish family with autosomal dominant congenital myopathy-6 with ophthalmoplegia, confirming its pathogenic role.[2] Subsequent functional work showed that expression of E706K MyHC IIa in muscle cells produces misfolded myosin, myofibrillar disarray, rimmed vacuoles, and cytoplasmic inclusions, justifying the original label “hereditary inclusion body myopathy 3.”[12]  

Recessive disease is typically caused by truncating or severe missense variants that result in loss of fast IIa myosin heavy chain function.[3][4][15] Tajsharghi et al. (2010; PMID: 20418530) described homozygous or compound heterozygous truncating MYH2 mutations as causing recessive myopathy with external ophthalmoplegia, mild-to-moderate muscle weakness, and complete lack of type 2A fibers, and emphasized the loss-of-function mechanism.[3][15] Lossos et al. (2013; PMID: 23388406) identified MYH2 mutations in recessive myopathy with external ophthalmoplegia in Arab families linked to chromosome 17p13.1-p12, further supporting the causal role of biallelic variants.[15] Tajsharghi et al. (2014; PMID: 24193343) expanded the series of recessive cases and reinforced the characterization of recessive MYH2 myopathy as an early-onset, largely nonprogressive disease with absent type 2A fibers.[3][15]  

Newer reports have added splice-site and frameshift variants to the pathogenic spectrum. Cassini et al. reported a novel splice-site variant c.5673+1G>C in intron 32, which was shown to affect splicing and generate abnormal transcripts, and segregation analysis in the family supported causality.[10] Baskar et al. documented two adult patients with CPEO due to novel homozygous MYH2 mutations: a 5′ splice variation in intron 4 (c.348+2dup) and a frameshift in exon 32 (p.Ala1480ProfsTer11), both consistent with loss of MyHC IIa.[9] Taken together, MYH2-related myopathy is unequivocally a genetically determined condition with a clear single-gene etiology, and environmental or infectious causation has not been implicated.[2][3][4][5][7][9][10][14][15][16]  

### 2.2 Genetic Risk Factors and Variant Spectrum  

Within the etiological framework, specific genetic variants in *MYH2* constitute both causal and risk factors for developing disease. Dominant missense variants in the motor domain, especially E706K, have high penetrance for MyHC IIa myopathy in carriers.[2][7][12][14] Myosinopathies reviews note that “The disease was mapped to chromosome 17p13.1 and later demonstrated to be caused by a heterozygous missense mutation in MYH2 encoding MyHC IIa,” underscoring the strength of linkage and segregation evidence.[7] PanelApp summarizes that more than ten families with bi-allelic variants and at least two missense variants with monoallelic disease have been reported, providing a minimal count of known pathogenic alleles.[16]  

Recessive pathogenic variants include nonsense mutations, frameshifts, splice-site changes, in-frame deletions, and severe missense substitutions in functional domains.[3][4][15] Tajsharghi et al. catalogued multiple truncating mutations and showed that they abolish expression of MyHC IIa protein in muscle, leading to absence of type 2A fibers.[3] Lossos et al. and subsequent authors added additional alleles, including variants affecting the rod region and tailpiece of the myosin heavy chain.[3][15] Baskar et al. identified a homozygous intronic duplication at c.348+2 and a homozygous frameshift at p.Ala1480ProfsTer11, both predicted to disrupt proper splicing or protein coding sequence.[9]  

Population databases highlight many *MYH2* variants that are benign and relatively common, indicating that not all sequence changes in this gene confer disease risk. ClinVarMiner’s list of variants reported as benign for inclusion body myositis includes several MYH2 variants such as NM_017534.6(MYH2):c.324A>G (p.Glu108=; rs12600539) with a gnomAD frequency of 0.43843, c.742-30A>C (rs11078849; 0.41970), and c.2697+25A>G (rs3744565; 0.41121), among others, many of which are synonymous or deep intronic.[13] These high-frequency benign variants illustrate that only specific changes, typically affecting conserved residues or splice motifs, act as pathogenic risk factors. ClinVar also lists variants of uncertain significance, such as c.1266+5G>C, which are present in population databases at low frequency (0.03%) and have at least one homozygous carrier but lack clear evidence of disease association, underscoring ongoing challenges in variant interpretation.[17]  

To date, no susceptibility loci outside *MYH2* have been robustly associated with MYH2-related myopathy, and there is no evidence for polygenic or multifactorial risk in this condition. The gene appears to act in a highly penetrant Mendelian fashion, with disease risk closely tied to specific pathogenic alleles. The concept of modifier genes—including other myosin isoforms or fiber-type regulatory genes—remains hypothetical, and data supporting genetic modifiers of severity are limited, although phenotypic variability among carriers of the same mutation suggests that additional genetic or environmental factors may influence expressivity.[4][7][10][14][15]  

### 2.3 Environmental and Lifestyle Risk Factors  

Current evidence does not implicate environmental, occupational, or lifestyle factors as primary causes or strong modifiers of MYH2-related myopathy. The disease has been consistently observed in familial clusters with segregation of MYH2 variants, and no case series have reported toxin exposures, infections, or lifestyle elements such as smoking or physical activity patterns as triggers or determinants of disease occurrence.[3][4][5][7][9][10][14][15][16] Neuromuscular clinicians generally recognize MYH2-related myopathy as a hereditary disorder, and diagnostic workup focuses on genetic testing rather than on environmental epidemiology.  

Nevertheless, general principles of muscle physiology suggest that environmental factors could influence disease course or symptom severity without altering underlying risk. For example, disuse atrophy due to sedentary lifestyle or immobilization might exacerbate weakness in individuals with MYH2 myopathy, while regular tailored exercise might help preserve function, as is true for other congenital myopathies. Similarly, intercurrent illnesses or malnutrition could transiently worsen strength and fatigue. However, these influences are not disease-specific and have not been systematically studied in MYH2 cohorts, so they cannot be considered established risk factors. There is no evidence that chemical exposures, radiation, or specific infections precipitate MYH2-related myopathy in genetically susceptible individuals.[3][4][7][9][10][14][15][16]  

### 2.4 Protective Factors  

Protective factors specific to MYH2-related myopathy have not been identified. Population-level data from gnomAD and ClinVarMiner show many benign MYH2 variants at appreciable frequencies, implying that neutral variation in this gene is common, but there is no indication that any particular allele confers protection against disease in the presence of a pathogenic variant.[11][13] For example, rs12600539 (p.Glu108=) is a synonymous variant with a gnomAD frequency of 0.43843, but it is classified as benign and simply represents normal variation rather than a protective modifier.[13]  

At a broader level, general health-promoting behaviors such as balanced nutrition, avoidance of extreme muscle overuse or injury, and maintenance of cardiovascular fitness may help individuals with MYH2-related myopathy optimize their functional status and delay secondary complications such as contractures or respiratory compromise. However, these measures are nonspecific and apply to many neuromuscular diseases. There are no data indicating that any pharmacological agents, nutraceuticals, or dietary patterns reduce the risk of developing MYH2 myopathy in carriers of pathogenic variants. Thus, etiological protective factors are best regarded as absent or unknown in this disease context.[3][4][7][9][10][14][15][16]  

### 2.5 Gene–Environment Interactions  

Given the strong Mendelian nature of MYH2-related myopathy, gene–environment (GxE) interactions have not been a major focus of research, and no specific interactions have been documented. Case reports do not mention environmental triggers preceding onset of weakness or ophthalmoplegia, and there is no evidence that environmental exposures modulate penetrance or expressivity of MYH2 mutations to a clinically significant degree.[3][4][5][7][9][10][14][15][16]  

In theory, gene–environment interactions could influence aspects such as muscle fiber-type plasticity, proteostasis capacity, or mitochondrial function, thereby shaping the tissue response to MYH2 dysfunction. Factors such as physical training, hormonal milieu, or nutritional status can affect fiber-type composition and contractile properties, which might modulate the impact of losing type IIa fibers or expressing dysfunctional myosin. Yet such hypotheses remain speculative, and no mechanistic or epidemiologic studies have directly addressed them in MYH2 disease. Accordingly, the etiology of MYH2-related myopathy is best characterized as monogenic, with minimal or unproven gene–environment interaction.  

## 3. Phenotypes  

### 3.1 Core Neuromuscular Phenotype: Proximal Weakness and Muscle Involvement  

The cardinal systemic manifestation of MYH2-related myopathy is proximal muscle weakness, predominantly affecting limb-girdle muscles of the shoulder and hip.[3][4][5][7][9][10][14][15][16] OMIM describes CMYO6 as “a relatively mild muscle disorder characterized by childhood onset of symptoms,” noting that affected individuals retain ambulation but exhibit mild to moderate weakness, especially in proximal muscle groups.[5] Myosinopathies reviews state that autosomal dominant MyHC IIa myopathy features “Mild proximal muscle weakness in childhood” with a progressive course in some adults affecting ambulation, and that recessive myopathy presents with “mild to moderate muscle weakness, usually mild facial involvement.”[7] Cassini et al. reported an autosomal dominant family with a slowly progressive, predominantly proximal myopathy, without congenital contractures or ophthalmoplegia, illustrating the core limb involvement.[10]  

Clinically, patients often report difficulty climbing stairs, rising from a seated position, or lifting objects overhead, consistent with involvement of hip and shoulder girdle muscles. Weakness may be symmetric and insidiously progressive over years, though some recessive cases appear stable or minimally progressive.[3][5][7][15][16] Distal muscles are generally less affected, though some individuals exhibit mild distal weakness or atrophy, particularly in dominant forms with longer disease duration.[4][7][10][14] Fasciculations are not typical, and tendon reflexes may be preserved or reduced depending on severity.  

Muscle bulk is often mildly reduced in affected regions, with possible scapular winging or lordotic posture reflecting core muscle involvement. EMG studies typically demonstrate a myopathic pattern with low-amplitude, short-duration motor unit potentials and early recruitment, without significant neurogenic changes, supporting primary muscle pathology.[4][7][10][14] Imaging studies such as muscle MRI reveal variable fatty infiltration of proximal muscles, occasionally with selective involvement patterns that can aid diagnosis.[10] The HPO term HP:0003690 (Proximal muscle weakness) captures this phenotype, and associated terms such as HP:0001769 (Scapular winging) and HP:0003723 (Gait disturbance) may be relevant in some cases.  

### 3.2 Ocular Phenotype: Ptosis and External Ophthalmoplegia  

External ophthalmoplegia is the most consistent and distinctive clinical feature across MYH2-related myopathy subtypes. OMIM and multiple case reports highlight ophthalmoplegia as an important clinical finding, often accompanied by ptosis.[3][4][5][7][9][14][15][16] Tajsharghi et al. concluded that “mild muscle weakness and ophthalmoplegia in combination with muscle biopsy demonstrating small or absent type 2A muscle fibers are the hallmark of recessive myopathy associated with MYH2 mutations,” emphasizing the diagnostic value of ocular involvement.[3] Myosinopathies reviews describe autosomal dominant MyHC IIa myopathy with “Ophthalmoplegia” as a major characteristic, and recessive myopathy similarly with “Ophthalmoplegia” as a consistent feature.[7]  

Clinically, patients present with bilateral, symmetric limitation of extraocular movements, often starting in adolescence or early adulthood, and sometimes preceded or accompanied by ptosis.[4][5][7][9][14][15][16] The condition may initially be subtle, with impaired upgaze or mild diplopia, but typically progresses to chronic progressive external ophthalmoplegia (CPEO) with near-complete fixation of the globe and prominent ptosis.[9] Baskar et al. studied two adult patients with MYH2 myopathy presenting with CPEO and muscle weakness, noting novel “features such as adult onset, isolated CPEO, proptosis, esophageal reflux disease and absence of skeletal abnormalities,” and argued that “MYH2 myopathy has to be considered in adult patients with CPEO.”[9] This expands the phenotype towards isolated ocular disease in some individuals.  

The HPO terms HP:0000622 (External ophthalmoplegia) and HP:0000508 (Ptosis) accurately capture these ocular manifestations. Quality of life impact is considerable, as severe ptosis can interfere with vision and external ophthalmoplegia restricts eye movements, often causing cosmetic concerns and functional impairment in activities requiring rapid gaze shifts such as driving or reading. Surgical interventions for ptosis may be required, and prism glasses or other aids may be helpful to manage diplopia, though in many cases diplopia decreases as ocular motility becomes severely restricted.[4][7][9][14][15]  

### 3.3 Congenital and Joint Phenotypes: Arthrogryposis and Contractures  

In the autosomal dominant form, congenital joint contractures are a characteristic but transient feature. Myosinopathies reviews note that dominant MyHC IIa myopathy is characterized by “Congenital, reversible joint contractures,” and OMIM similarly mentions congenital joint contractures that resolve with time.[5][7] Darin et al. and Martinsson et al. described affected individuals with arthrogryposis—multiple joint contractures at birth—who later experienced resolution of contractures but developed proximal weakness and ophthalmoplegia in adolescence.[2][7][14] The HPO term HP:0002829 (Arthrogryposis) or HP:0001371 (Joint contracture) reflects this aspect of the phenotype.  

The presence of congenital contractures suggests intrauterine or early postnatal muscle dysfunction, perhaps reflecting impaired fast-twitch muscle development due to dominant-negative MYH2 mutations. Over time, as muscle growth continues and neuromuscular adaptation occurs, these contractures may diminish, but underlying muscle weakness remains.[2][7][14] Not all dominant cases show arthrogryposis; Cassini et al.’s family with a splice-site variant c.5673+1G>C had no congenital contractures, indicating phenotypic variability even within the dominant category.[10] Recessive cases generally do not feature prominent congenital contractures but may have mild facial weakness and subtle craniofacial features.[3][15]  

Quality of life impact of congenital contractures includes difficulty with neonatal care, delayed motor milestones, and potential need for orthopedic interventions. However, because contractures are often reversible in MyHC IIa myopathy, long-term disability from joint deformities is limited, and proximal muscle weakness and ophthalmoplegia represent the more enduring sources of morbidity.[5][7][14]  

### 3.4 Histopathological Phenotypes: Fiber-Type Changes, Rimmed Vacuoles, and Inclusions  

Histopathological findings on muscle biopsy are central to the characterization and diagnosis of MYH2-related myopathy, and they differ markedly between autosomal dominant and autosomal recessive forms. In dominant MyHC IIa myopathy, muscle biopsies from adults often show dystrophic changes, rimmed vacuoles, and intranuclear and cytoplasmic inclusions, prompting the original designation of hereditary inclusion body myopathy 3.[4][7][12][14] Myosinopathies reviews describe “Rimmed vacuoles with protein aggregates, composed of 15–20 nm tubulofilaments, in adults with progressive course and dystrophic muscle changes,” as well as “Structural alterations with minicores in type 2 fibers in childhood and in mildly affected muscles of adults,” and “Reduced number and small type 2 fibers in some cases.”[7]  

Experimental expression of the E706K IBM3 mutation confirmed its propensity to cause myofibrillar disorganization and inclusion-body formation. In the PMC3364171 article, the authors state that “Biopsies reveal dystrophic changes, rimmed vacuoles with cytoplasmic inclusions, and focal disorganization of myofilaments,” when describing IBM3.[12] These features closely resemble inclusion body myositis, with tubulofilamentous inclusions and rimmed vacuoles, but the pattern of fiber-type involvement and genetic basis distinguish MYH2 myopathy as a separate entity.[7][12][14] The HPO term HP:0003483 (Rimmed vacuoles on muscle biopsy) and HP:0007340 (Cytoplasmic inclusion bodies in muscle fibers) are appropriate phenotype descriptors.  

In recessive MYH2 myopathy, the hallmark biopsy finding is near-complete absence of type 2A fibers and reduced or absent expression of MyHC IIa transcript and protein.[3][4][7][15] Tajsharghi et al. reported that “Muscle biopsy demonstrated small or absent type 2A muscle fibers and reduced or absent expression of the corresponding MyHC IIa transcript and protein,” and concluded that this pattern is the hallmark of recessive MYH2 disease.[3] Myosinopathies reviews summarize recessive pathology as “Complete absence of type 2A muscle fibers. Variable, unspecific myopathic changes with fatty infiltration. Type 2B fibers may be lacking,” reflecting a fiber-type–specific and noninflammatory myopathic process.[7] Rimmed vacuoles and inclusions are notably absent in recessive cases, distinguishing them from dominant IBM3.[3][4][7][14][15]  

These histopathological phenotypes have significant diagnostic and mechanistic implications. They provide direct evidence of MYH2 protein dysfunction, fiber-type specificity, and downstream proteostasis changes, and correlate with clinical features such as ophthalmoplegia and proximal weakness. The absence of inflammatory infiltrates or significant necrosis suggests that MYH2-related myopathy is primarily a structural and fiber-type disease rather than an inflammatory myositis.[4][7][12][14]  

### 3.5 Imaging, Electrophysiology, and Laboratory Phenotypes  

Beyond histology, MYH2-related myopathy manifests in characteristic radiological and electrophysiological patterns. Muscle MRI in affected individuals often shows fatty infiltration of proximal muscles, with variable severity and muscle group involvement. Cassini et al. noted that “This is radiographically characterized by fatty infiltration of variable severity and muscle group involvement,” referring to MYH2 variants.[10] The distribution pattern may highlight selective involvement of thigh and pelvic girdle muscles while sparing distal muscles, akin to other congenital myopathies, although systematic MRI studies remain limited.[4][7][10]  

Electromyography (EMG) usually demonstrates a myopathic pattern. In the series summarized by Tajsharghi and others, EMG showed low-amplitude, short-duration motor unit potentials, early recruitment, and absence of neurogenic changes, consistent with primary muscle disease.[3][4][7][14][15] Baskar et al. emphasized that in their CPEO patients, the absence of decremental response in repetitive nerve stimulation (RNS) helped differentiate MYH2 myopathy from congenital myasthenic syndromes.[9] Nerve conduction studies are typically normal, further supporting a myopathic rather than neuropathic etiology.[4][7][10][14]  

Routine laboratory tests such as serum creatine kinase (CK) may be normal or mildly elevated, reflecting the relatively nondystrophic nature of many MYH2 cases. In Tajsharghi’s recessive series, CK levels were often within the normal range or only modestly raised, and myopathic changes were subtle.[3][4][15] In some dominant IBM3 cases with progressive degeneration, CK may be more elevated, but data are variable.[4][7][12][14] Pulmonary function tests and cardiac evaluations are usually normal, as MYH2 myopathy primarily affects skeletal muscle and extraocular muscles, with minimal involvement of respiratory or cardiac muscle.[4][7][15][16]  

The HPO terms HP:0003457 (Myopathic EMG pattern) and HP:0003215 (Abnormal muscle MRI) capture these diagnostic phenotypes. Together, imaging, electrophysiology, and laboratory findings contextualize the clinical picture and help differentiate MYH2-related myopathy from inflammatory myopathies, neuropathies, and mitochondrial myopathies.[4][7][9][10][14][15][16]  

### 3.6 Quality of Life Impact  

The cumulative impact of proximal muscle weakness, chronic external ophthalmoplegia, and, in some cases, congenital contractures contributes to notable but often moderate impairment in quality of life for individuals with MYH2-related myopathy. OMIM notes that CMYO6 is generally mild and that affected individuals retain ambulation, suggesting that many patients can perform basic activities of daily living, though with limitations in strenuous tasks.[5] Proximal weakness can restrict mobility, reduce endurance, and complicate employment in physically demanding occupations, thereby affecting social and economic participation. Ophthalmoplegia and ptosis impose visual and cosmetic burdens, with potential psychosocial consequences due to altered appearance and gaze.[4][7][9][14][15]  

The early onset and chronic nature of symptoms mean that patients must adapt over the lifespan, potentially requiring assistive devices, orthotics, or surgical interventions. Children with congenital contractures may need orthopedic care and physical therapy to achieve optimal motor development, while adults may require muscle-strengthening programs and occupational therapy to maintain independence.[4][7][14][15][16] Despite these challenges, many individuals have stable or slowly progressive disease and can live full lives with appropriate supportive care. In the absence of large QoL survey studies specifically targeting MYH2 myopathy, the impact can be inferred from common neuromuscular outcome measures such as SF-36 or EQ-5D, which typically show moderate reductions in physical functioning but relatively preserved mental health domains.  

From an ontological perspective, quality-of-life aspects may be captured using terms such as HP:0001324 (Fatigue), HP:0002355 (Reduced activity tolerance), and WHOQOL categories of physical health, psychological health, social relationships, and environment. Research gaps remain in quantifying these aspects systematically in MYH2 cohorts and understanding how interventions can optimize quality of life.  

## 4. Genetic and Molecular Information  

### 4.1 Causal Gene: MYH2  

*MYH2* is the sole gene currently implicated as a causal locus in MYH2-related myopathy. NCBI Gene describes *MYH2* (Gene ID: 4620) as encoding “a member of the class II or conventional myosin heavy chains, and functions in skeletal muscle contraction,” located in a cluster of myosin heavy chain genes on chromosome 17.[1] OMIM gene entry 160740 notes that MYH2 encodes the myosin heavy chain isoform expressed in fast type 2A muscle fibers and summarizes mapping and mutation data linking it to congenital myopathy 6 with ophthalmoplegia.[2][5] Cytogenetically, *MYH2* is situated at 17p13.1, and genomic coordinates (GRCh38) are 17:10,521,148–10,549,658, reflecting a ~28.5 kb locus with multiple exons.[2]  

At the protein level, MYH2 encodes the myosin heavy chain IIa (MyHC IIa), a ~2,000 amino acid motor protein comprising an N-terminal head (motor) domain responsible for ATP hydrolysis and actin binding, a neck region that binds light chains, and a long C-terminal coiled-coil rod that forms the backbone of thick filaments.[2][4][7] MyHC IIa partners with regulatory and essential light chains to form the myosin II hexamer, and the heavy chain head domain undergoes conformational changes that translate chemical energy from ATP hydrolysis into mechanical movement along actin filaments.[4][7] The SH1 helix within the motor domain is crucial for coupling nucleotide state to lever arm rotation, and mutations such as E706K in this region have profound effects on motor function.[2][7][12]  

In human skeletal muscle, MYH2 is predominantly expressed in fast type 2A fibers, which exhibit intermediate contraction speeds and oxidative capacity, and in some species also in 2B fibers.[4][7] ClinGen cites expression evidence (PMID: 7545970) showing MyHC IIa localization to type IIa muscle fibers, and notes a *C. elegans* ortholog with similar functional roles.[15] The gene cluster on chromosome 17 also includes MYH1 and MYH3, indicating coordinated regulation of myosin isoforms during development and in adult muscle.[2][7]  

### 4.2 Pathogenic Variant Classes and ACMG Classification  

Pathogenic variants in *MYH2* span multiple ACMG/AMP classes and include missense, nonsense, frameshift, splice-site, and in-frame deletions. Dominant variants are typically missense changes in highly conserved residues of the motor domain, with strong functional and segregation evidence, fulfilling criteria for “pathogenic” or “likely pathogenic” classification under ACMG guidelines.[2][7][12][14][15][16] The E706K substitution is the prototypical dominant pathogenic variant, with clear causality demonstrated by co-segregation in families, absence in controls, location in a critical functional region, and mechanistic studies showing deleterious effects.[2][7][12][14] Other reported dominant missense mutations include variants in adjacent helices or loops that affect motor performance, though fewer families have been described.[7][16]  

Recessive pathogenic variants include truncating mutations (nonsense and frameshift), essential splice-site changes, and severe missense or in-frame deletions that abolish or markedly reduce MyHC IIa expression.[3][4][15] Tajsharghi et al. and Lossos et al. documented multiple such variants and provided evidence of loss of MyHC IIa protein in muscle, satisfying ACMG criteria for loss-of-function in a gene where LoF is a known disease mechanism.[3][15] ClinGen lists ten unique variants across eight probands in three key publications, including missense, in-frame deletions, frameshifts, and splice-site variants, and explicitly notes a loss-of-function mechanism for recessive disease.[15] Baskar et al.’s splice-site and frameshift variants and Cassini’s c.5673+1G>C splice-site variant further expand the LoF variant catalog.[9][10]  

ClinVar hosts numerous MYH2 entries with varying significance. For instance, RCV000809069.5 describes NM_017534.6(MYH2):c.1266+5G>C in intron 13 as a single nucleotide variant affecting a consensus splice-site nucleotide, present in gnomAD at 0.03% including homozygotes, but with in silico predictions suggesting it is not likely to affect splicing and no reported affected individuals, leading to classification as a variant of uncertain significance (VUS).[17] ClinVarMiner’s benign variant table lists several synonymous and intronic MYH2 variants with high allele frequencies, reflecting their non-pathogenic nature.[13] These resources highlight the need for careful ACMG interpretation incorporating population data, computational predictions, functional assays, and segregation analyses when assessing MYH2 variants.  

### 4.3 Allele Frequency and Population Distribution  

Population allele frequency data from gnomAD and related databases, as summarized by ClinVarMiner, show that many MYH2 variants are common and benign, while pathogenic variants are rare.[11][13][17] For example, rs12600539 (p.Glu108=) has a gnomAD frequency of 0.43843, rs11078849 (c.742-30A>C) 0.41970, and rs3744565 (c.2697+25A>G) 0.41121, all classified as benign in the context of inclusion body myositis and MYH2-related conditions.[13] Several other synonymous and splice-region variants have frequencies in the 0.01–0.2 range and are also benign, indicating that *MYH2* tolerates considerable variation outside critical domains.[13]  

In contrast, pathogenic MYH2 variants described in families with myopathy are usually absent or extremely rare in population databases, reflecting their deleterious nature. Baskar et al.’s homozygous c.348+2dup and p.Ala1480ProfsTer11 variants were novel and not present in public databases.[9] Cassini’s c.5673+1G>C splice-site variant, while present in the proband’s family, was not reported as common in the general population.[10] ClinGen’s recessive variant catalog underscores that most LoF alleles are family-specific or very rare.[15]  

Geographically, MYH2 pathogenic variants have been reported in Swedish, Arab, Indian, and other populations, suggesting broad distribution without a strong founder effect, although small series may reflect local genetic backgrounds.[2][3][9][15][16] The overall carrier frequency of pathogenic MYH2 variants is expected to be extremely low, consistent with the rarity of clinically manifest MYH2 myopathy, but precise carrier estimates are not available.  

### 4.4 Somatic versus Germline Origin  

All documented MYH2-related myopathy cases are associated with germline variants, present in constitutional DNA and segregating within families according to autosomal dominant or recessive patterns.[2][3][4][5][7][9][10][14][15][16] There is no evidence that somatic mutations in *MYH2* cause acquired muscle disease, nor has MYH2 emerged as a recurrent somatic driver in cancer or other contexts in databases such as COSMIC. Muscle biopsies in MYH2 myopathy reveal structural pathology but not somatic mosaicism of MYH2 expression that would suggest acquired gene lesions.[4][7][12][14]  

Germline origin is confirmed by sequencing of blood DNA from probands and relatives, with consistent detection of the same variant in affected individuals and absence in unaffected family members, supporting Mendelian inheritance.[2][3][9][10][14][15] Thus, MYH2-related myopathy should be considered a purely hereditary disorder, and somatic mutation data are largely irrelevant to its pathogenesis.  

### 4.5 Functional Consequences: Loss of Function and Dominant Negative  

Mechanistically, MYH2 pathogenic variants fall into two broad categories: loss-of-function (LoF) variants causing recessive disease and dominant-negative missense variants causing dominant disease with inclusion-body pathology.[3][4][7][12][14][15][16] Tajsharghi et al. and ClinGen emphasize that recessive MYH2 myopathy results from loss of fast IIa myosin heavy chain due to truncating or disruptive mutations, leading to complete absence of type 2A fibers.[3][15] Functional studies show reduced or absent MYH2 transcript and protein in muscle biopsies, and immunohistochemistry confirms the lack of MyHC IIa.[3] In recessive disease, heterozygous carriers generally remain asymptomatic, consistent with haplosufficiency of MYH2 in most tissues.[3][15]  

In dominant MyHC IIa myopathy (IBM3), missense mutations such as E706K in the SH1 helix cause structural perturbation of the myosin motor domain that exerts a dominant-negative effect. The mutated myosin heavy chain integrates into thick filaments but impairs motor function and promotes misfolding, leading to aggregation and inclusion formation.[7][12][14] The location of E706K in a highly conserved, functionally critical helix supports a significant impact on ATPase activity and actin interaction. Expression studies of E706K MYH2 demonstrate misfolded protein, disorganized myofilaments, dystrophic changes, rimmed vacuoles, and cytoplasmic inclusions, providing direct evidence of dominant-negative behavior.[12]  

Some splice-site variants, such as Cassini’s c.5673+1G>C, may produce aberrant transcripts that encode altered carboxy-terminal regions of MyHC IIa or lead to nonsense-mediated decay, and the precise functional consequence may lie between pure LoF and dominant-negative effects depending on the nature of transcripts and protein expression.[10] Cassini et al. observed novel transcripts and histologic hallmarks of MYH2 myopathy (small, paucity of type 2A fibers, rimmed vacuoles), suggesting that their variant had pathogenic impact consistent with dominant disease even in the absence of classic ophthalmoplegia.[10]  

Overall, the functional landscape of MYH2 mutations illustrates how different classes of variants can perturb the same protein in distinct ways, producing overlapping yet differentiable phenotypes. Dominant-negative motor domain mutations lead to toxic gain-of-function at the level of protein misfolding and inclusion formation, while recessive LoF variants cause developmental absence of MyHC IIa and fiber-type defects without inclusion pathology.[3][4][7][12][14][15][16]  

### 4.6 Modifier Genes and Epigenetic Information  

At present, no specific modifier genes have been convincingly shown to alter the severity or expression of MYH2-related myopathy. It is plausible that genes controlling muscle fiber-type specification (e.g., transcription factors regulating fast versus slow fiber differentiation) or proteostasis (e.g., autophagy and ubiquitin–proteasome pathway components) could modulate disease phenotype, but such modifiers remain hypothetical in the absence of genetic or functional data.[4][7][12][14] Similarly, epigenetic mechanisms such as DNA methylation or histone modifications that influence MYH2 expression have not been systematically studied in this disease context.  

ENCODE and Roadmap Epigenomics data characterize chromatin states in skeletal muscle tissue, including regulatory elements that may govern *MYH2* transcription, but these resources have not yet been integrated into MYH2 myopathy-specific research. MGI notes that the mouse *Myh2* locus is regulated by several regulatory regions (Rr194, Rr195, Rr196), including a locus control region, suggesting complex regulation of fast myosin expression.[8] Whether analogous regulatory structures exist in human MYH2 and whether epigenetic changes at these sites contribute to variability in disease expression is unknown. For now, epigenetic information should be considered a research frontier rather than a defined component of MYH2 myopathy etiology.  

### 4.7 Chromosomal Abnormalities  

Chromosomal abnormalities such as large deletions, duplications, translocations, or aneuploidy involving the MYH2 locus have not been reported as causes of MYH2-related myopathy. Linkage and mapping studies localized IBM3 and recessive myopathy loci to 17p13.1–p12, but subsequent fine mapping identified point mutations and small-scale sequence variants within *MYH2* rather than structural rearrangements.[2][5][15] Genomewide linkage analyses by Lossos et al. found significant linkage to a 12-cM region on chromosome 17p13.1–p12 between markers D17S1812 and D17S947, but the disease locus was ultimately attributed to *MYH2* sequence variants rather than copy number changes.[5][15]  

ClinVar and DECIPHER do not highlight recurrent chromosomal syndromes involving MYH2 linked to congenital myopathy 6, and karyotyping in affected individuals is generally normal.[2][3][5][15][16][17] Therefore, MYH2-related myopathy is best conceptualized as a single-gene sequence variant disorder, and chromosomal abnormalities are not part of its typical genetic architecture.  

## 5. Environmental Information  

### 5.1 Environmental Factors  

As noted earlier, there is no current evidence that environmental exposures play a causal role in MYH2-related myopathy. The disease consistently arises in individuals carrying germline MYH2 mutations, and no reports implicate specific toxins, pollutants, radiation, or occupational hazards in precipitating or exacerbating the condition.[3][4][5][7][9][10][14][15][16] Comparative toxicogenomics databases like CTD do not list MYH2 as a common target of environmental toxicants in muscle disease, and myosinopathies reviews solely discuss genetic mechanisms.  

Experimental exposures could, in principle, modulate myosin function or muscle proteostasis, but any such effects would be nonspecific and not recognized as MYH2-specific environmental factors. For example, oxidative stress from toxins might exacerbate protein aggregation in dominant MYH2 myopathy, or endocrine disruptors might alter fiber-type ratios, but these hypotheses lack empirical support. Thus, the environmental factor dimension in MYH2-related myopathy is minimal and largely limited to generic considerations of muscle health.  

### 5.2 Lifestyle Factors  

Lifestyle factors such as physical activity, diet, and substance use have not been systematically studied in relation to MYH2 myopathy risk or progression. In clinical practice, neuromuscular specialists advise patients with congenital myopathies to maintain moderate, non-excessive exercise, avoid extreme overuse or immobilization, and follow balanced nutrition, but these recommendations are not disease-specific.[4][7][15][16] Smoking, alcohol consumption, and obesity can influence overall health and comorbidities but have not been linked to specific changes in MYH2 disease course.  

Given the rarity of MYH2 myopathy, large-scale epidemiologic studies exploring lifestyle correlates are unlikely in the near term. For now, lifestyle should be considered an adjunct to supportive care rather than an etiological or major phenotypic driver.  

### 5.3 Infectious Agents  

No infectious agents are known to cause or trigger MYH2-related myopathy. The disease lacks inflammatory histopathology typical of infectious or autoimmune myositis, and there are no reports of specific viral or bacterial infections preceding symptom onset.[4][7][12][14][15] Chronic progressive external ophthalmoplegia due to mitochondrial disease can be precipitated or worsened by infections, but MYH2-related CPEO appears purely genetic and noninfectious.[9]  

Therefore, infectious factors and zoonotic agents are not relevant to MYH2 myopathy etiology, and infection management in affected individuals follows general medical guidelines rather than disease-specific protocols.  

## 6. Mechanism / Pathophysiology  

### 6.1 Ordered Causal Chain from Mutation to Clinical Manifestation  

Step 1: Germline pathogenic variants in *MYH2* (missense, truncating, splice-site) alter the sequence or expression of the MyHC IIa protein in fast skeletal muscle fibers, leading to impaired myosin motor function or loss of MyHC IIa expression.  

Step 2: Altered MyHC IIa function or absence results in defective sarcomeric assembly and actin–myosin interaction in type 2A (and sometimes 2B) muscle fibers, causing fiber-type–specific structural and functional abnormalities.  

Step 3: In dominant missense variants, misfolded or dysfunctional MyHC IIa integrates into thick filaments, leading to myofibrillar disorganization, protein aggregation, and activation of proteostasis pathways that culminate in rimmed vacuole and inclusion formation; in recessive LoF variants, developmental absence of MyHC IIa causes failure to form or maintain type 2A fibers, leading to selective fiber-type loss without inclusion pathology.  

Step 4: These fiber-type–specific changes in fast skeletal muscle, particularly in proximal limb and extraocular muscles, result in reduced contractile strength and endurance, manifesting clinically as proximal muscle weakness and external ophthalmoplegia with ptosis.  

Step 5: Over time, chronic dysfunction and structural damage lead to fatty infiltration of affected muscles, minor dystrophic changes, and sometimes minicores in type 2 fibers, further reducing muscle performance and contributing to progressive weakness in some dominant cases, while recessive cases remain relatively stable.  

Step 6: The absence of significant inflammatory infiltrates or immune activation indicates that the pathophysiology is primarily structural and proteostatic rather than autoimmune, and secondary complications such as contractures or respiratory compromise arise primarily from mechanical and functional limitations rather than systemic pathology.  

### 6.2 Molecular Pathways and Myosin Motor Dysfunction  

At the molecular level, MYH2-related myopathy centers on disruption of actin–myosin cross-bridge cycling and thick filament assembly, processes governed by the myosin II ATPase cycle. MyHC IIa, encoded by MYH2, has specific kinetic properties optimized for fast-twitch muscle function, including rapid ATP hydrolysis and cross-bridge turnover.[2][4][7] Dominant missense mutations like E706K in the SH1 helix are expected to perturb the coupling between ATP binding/hydrolysis and lever arm rotation, thereby altering the duty cycle and force generation. The SH1 helix plays a key role in transmitting conformational changes from the nucleotide-binding pocket to the rest of the head domain, and substitution of a negatively charged glutamate with a positively charged lysine can disrupt local interactions and stability.[2][7][12]  

Experimental expression of E706K MYH2 in muscle cells has shown misfolded protein and disorganized myofilaments, indicating that mutant myosin fails to assemble properly into thick filaments or to maintain filament integrity.[12] This misassembly is likely to engage cellular quality-control pathways such as the ubiquitin–proteasome system and autophagy, leading to the formation of protein aggregates and rimmed vacuoles characteristic of IBM3.[7][12][14] The precise signaling cascades are not fully delineated, but parallels can be drawn to other protein-aggregation myopathies, where misfolded proteins induce autophagic vacuoles and tubulofilament aggregates. Gene Ontology (GO) terms relevant here include GO:0030048 (actin filament-based movement), GO:0006936 (muscle contraction), GO:0016071 (protein catabolic process), and GO:0006914 (autophagy), reflecting both contractile and proteostasis aspects.  

In recessive LoF variants, the key molecular change is the absence or severe reduction of MyHC IIa. This leads to failure of type IIa fibers to develop or persist, and muscle fiber pools shift towards other types such as type I or IIx, or show atrophy and fatty replacement.[3][4][7][15] Transcriptomic and immunohistochemical data from recessive cases indicate that MYH2 transcripts and protein are markedly reduced or absent, confirming the LoF mechanism.[3] GO terms such as GO:0007507 (muscle fiber development) and GO:0048747 (muscle fiber maturation) are pertinent in describing how MYH2 deficiency affects fiber-type specification.  

### 6.3 Cellular Processes: Autophagy, Protein Aggregation, and Fiber-Type Loss  

At the cellular level, MYH2-related myopathy engages processes of protein quality control, autophagy, and structural maintenance of sarcomeres. In dominant IBM3, rimmed vacuoles and filamentous aggregates indicate activation of autophagic pathways and accumulation of undigested material.[7][12][14] These vacuoles typically contain 15–20 nm tubulofilaments and protein aggregates, suggesting that misfolded myosin and associated proteins were targeted for degradation but incompletely cleared.[7] The HPO term HP:0100806 (Autophagic vacuoles in muscle fibers) and GO:0006914 (autophagy) capture these processes.  

Myosinopathies reviews describe “Structural alterations with minicores in type 2 fibers in childhood and in mildly affected muscles of adults,” implying that oxidative and calcium-handling defects may accompany structural disruption.[7] Minicores are focal areas of myofibrillar disorganization and mitochondrial depletion, often associated with defects in excitation–contraction coupling and energy metabolism, and they are common in core myopathies involving other structural proteins. In IBM3, minicores may represent localized failure of sarcomeric maintenance due to chronic presence of mutant myosin.  

In recessive MYH2 myopathy, cellular processes center on fiber-type loss rather than aggregation. Muscles show “Complete absence of type 2A muscle fibers. Variable, unspecific myopathic changes with fatty infiltration. Type 2B fibers may be lacking,” according to myosinopathies reviews.[7] This suggests that muscle fiber-type plasticity is altered, with surviving fibers being primarily slow-twitch or other fast subtypes, and that chronic underuse or lack of proper innervation leads to fatty replacement. GO terms such as GO:0001764 (neuron adhesion), GO:0048754 (branching involved in skeletal muscle organ development), and GO:0005518 (collagen binding) may be involved in broader structural and extracellular matrix remodeling.  

Importantly, both dominant and recessive MYH2 myopathies lack significant inflammatory infiltrates or necrosis, distinguishing them from immune-mediated myositis. Immune system involvement is minimal, and biomarkers of autoimmunity (e.g., myositis-specific antibodies) are typically negative.[4][7][12][14][15] Thus, cellular pathophysiology is primarily structural and proteostatic rather than immune-mediated.  

### 6.4 Metabolic Changes and Energy Utilization  

Type IIa fibers are characterized by fast contraction and intermediate oxidative capacity, contributing substantially to muscle power and endurance. Loss or dysfunction of MyHC IIa is expected to alter muscle energy metabolism, though direct metabolomic studies in MYH2 myopathy are lacking. In recessive disease, absence of type 2A fibers may shift fiber-type composition towards type I fibers, which are more oxidative, or towards other fast subtypes with different metabolic profiles.[3][4][7][15] This could influence fatigue resistance and overall metabolic efficiency during exercise, leading to early fatigue or altered performance.  

In dominant IBM3, inclusion formation and chronic proteostasis stress may increase energy demands for protein turnover and autophagy, potentially affecting mitochondrial function and ATP supply, though this has not been extensively studied. Minicores suggest localized mitochondrial depletion or dysfunction within fibers, which could impair oxidative metabolism.[7][12][14] GO terms such as GO:0006091 (generation of precursor metabolites and energy), GO:0006119 (oxidative phosphorylation), and GO:0005739 (mitochondrion) are relevant.  

Despite these implications, systemic metabolic abnormalities such as lactic acidosis, hypoglycemia, or lipid disorders have not been reported in MYH2 patients, and standard metabolic labs are typically normal.[3][4][7][10][15] Thus, metabolic changes are likely confined to muscle tissue and manifest primarily as reduced endurance and fatigue rather than systemic metabolic disease.  

### 6.5 Immune System Involvement and Tissue Damage  

As noted, immune system involvement in MYH2-related myopathy is minimal. Muscle biopsies do not show significant inflammatory infiltrates or complement deposition, distinguishing the disease from autoimmune myositis such as polymyositis or dermatomyositis.[4][7][12][14] Rimmed vacuoles in IBM3 are associated with degenerative autophagic processes rather than immune attack, and tubulofilament inclusions do not appear to provoke robust immune responses.  

Tissue damage mechanisms center on structural failure, proteostatic overload, and fatty infiltration. In dominant IBM3, chronic presence of misfolded myosin causes slow fiber degeneration, with muscle fibers being replaced by fat and connective tissue over years, resulting in progressive weakness.[7][12][14] In recessive disease, early inability to form type 2A fibers leads to muscle hypoplasia and gradual fatty infiltration, but the process is relatively stable and nonprogressive.[3][4][7][15] GO terms such as GO:0008219 (cell death) and GO:0009898 (cytoplasmic protein catabolic process) are applicable.  

Oxidative stress and mitochondrial dysfunction may contribute to tissue damage in IBM3, as in other inclusion-body myopathies, but explicit data in MYH2 disease are limited. No fibrosis-related severe cardiomyopathy or respiratory failure has been reported, consistent with the mild systemic impact of MYH2 myopathy.[4][5][7][10][15][16]  

### 6.6 Epigenetic Changes and Molecular Profiling  

Specific epigenetic changes in MYH2-related myopathy have not been described, and large-scale molecular profiling data (transcriptomics, proteomics, metabolomics) are sparse. However, muscle biopsies in recessive disease show reduced or absent expression of MYH2 mRNA and protein, implying transcriptional or post-transcriptional regulation of mutant alleles.[3][4][15] Cassini et al. demonstrated that their splice-site variant c.5673+1G>C affects splicing, resulting in novel transcripts, although detailed transcriptome profiling was not reported.[10]  

Given the role of MYH2 in fiber-type identity, global gene expression changes involving other myosin isoforms, troponins, and fiber-type transcription factors are likely in affected muscle, but these have not yet been systematically catalogued in public datasets such as GEO or ArrayExpress. Similarly, proteomic studies of IBM3 inclusions could reveal the composition of aggregates, including myosin, ubiquitin, p62, and other proteostasis-related proteins, but such work has not been widely published. Metabolomic and lipidomic signatures in MYH2 muscle have not been explored.  

Future multi-omics studies integrating genomic, transcriptomic, and proteomic data in MYH2 myopathy could clarify pathways involved in fiber-type specification, autophagy, and sarcomeric maintenance, and provide new therapeutic targets. For now, molecular profiling remains a promising but underdeveloped domain in MYH2 research.  

### 6.7 Advanced Technologies and Functional Genomics  

Advanced technologies such as single-cell RNA sequencing, spatial transcriptomics, and CRISPR-based functional genomics have not yet been specifically applied to MYH2-related myopathy. However, the disease provides an attractive target for such methodologies because it affects specific fiber types and involves distinct cell populations such as extraocular muscle fibers and fast-twitch limb muscle fibers.[3][4][7][9][15] Single-cell analysis of muscle biopsies could reveal how MYH2 mutations alter fiber-type composition, satellite cell behavior, and immune cell involvement at high resolution, while spatial transcriptomics could map expression of MYH2 and other myosin isoforms within muscle architecture.  

Functional genomics screens, such as CRISPR knockout or CRISPR base editing in myoblasts or myotubes, could be used to model MYH2 mutations in vitro and identify pathways that modulate proteostasis and autophagy in IBM3. The *C. elegans* model referenced by ClinGen, which likely involves mutation of an MYH2 ortholog, demonstrates the feasibility of using invertebrate systems to study myosin function and muscle phenotypes.[15] DepMap and other cancer-focused resources are less relevant, as MYH2 is not a common oncogenic driver.  

In summary, mechanistic understanding of MYH2-related myopathy is grounded in classical molecular and histological studies, and cutting-edge multi-omics and functional genomics approaches remain opportunities for future research rather than current sources of data.  

### 6.8 Suggested GO and CL Terms for Mechanisms and Cell Types  

Based on the mechanistic narrative, key GO biological process terms include GO:0030048 (actin filament-based movement), GO:0006936 (muscle contraction), GO:0007507 (muscle fiber development), GO:0006914 (autophagy), GO:0009898 (cytoplasmic protein catabolic process), GO:0008219 (cell death), GO:0006119 (oxidative phosphorylation), and GO:0005739 (mitochondrion). Cell Ontology (CL) terms relevant to cell types include CL:0000746 (skeletal muscle fiber), CL:0000670 (fast-twitch skeletal muscle fiber), and CL:0000700 (extraocular muscle cell). These terms can be used to annotate mechanistic statements in ontological frameworks and knowledge bases.  

## 7. Anatomical Structures Affected  

### 7.1 Organ-Level Involvement  

The primary organs affected in MYH2-related myopathy are skeletal muscles, particularly limb-girdle muscles and extraocular muscles. Uberon terms such as UBERON:0002106 (skeletal muscle tissue) and UBERON:0001630 (extraocular skeletal muscle) capture these structures. Clinical reports describe proximal limb involvement in the shoulders and hips, reflecting weakness of muscles like the deltoid, gluteus maximus, and quadriceps.[3][4][5][7][10][15][16] Extraocular muscles, including the superior rectus, inferior rectus, lateral rectus, medial rectus, superior oblique, and inferior oblique, are consistently affected, leading to external ophthalmoplegia.[4][7][9][14][15]  

Secondary organ involvement is minimal. Cardiac muscle, smooth muscle, and central nervous system are generally spared, with echocardiography and neuroimaging often normal.[4][7][15][16] Respiratory muscles, such as the diaphragm and intercostals, are usually preserved sufficiently to avoid severe respiratory failure, though mild restrictive changes may occur in advanced cases, as in other myopathies. Gastrointestinal involvement is limited, though Baskar et al. noted esophageal reflux disease in a CPEO patient, which may reflect nonspecific comorbidity rather than direct MYH2 pathology.[9]  

Body systems most prominently involved include the musculoskeletal system (skeletal muscle and joints), ocular motor system (extraocular muscles and eyelids), and, to a lesser extent, the neuromuscular junction and cranial nerves controlling eye movements and facial expression. However, neuromuscular junction physiology is typically normal, differentiating MYH2 myopathy from congenital myasthenic syndromes.[4][7][9][15]  

### 7.2 Tissue and Cell-Level Involvement  

At the tissue level, MYH2-related myopathy primarily affects striated skeletal muscle, a type of connective tissue specialized for contraction. Muscle fibers expressing MyHC IIa, particularly type 2A and 2B fibers, bear the brunt of pathology.[4][7][15] In dominant IBM3, type 2 fibers show minicores, rimmed vacuoles, and inclusions, indicating structural and proteostatic stress.[7][12][14] In recessive MYH2 myopathy, type 2A fibers are absent or greatly reduced, and surviving fibers may be type I or other fast subtypes.[3][4][7][15]  

Specific cell populations affected include fast-twitch skeletal muscle fibers (CL:0000670), extraocular muscle fibers (CL:0000700), and, secondarily, slow-twitch fibers that may compensate for absent fast fibers. Satellite cells, the muscle stem cells responsible for regeneration, may be involved in ongoing attempts to repair damaged fiber architecture, though their behavior in MYH2 myopathy has not been specifically studied. Myonuclei within fibers must cope with misfolded myosin and autophagic processes in IBM3, suggesting nuclear stress as well.  

Connective tissue cells such as fibroblasts contribute to fibrosis and fatty infiltration over time, particularly in dominant cases with progressive degeneration. Adipocytes increase within muscle tissue as fibers atrophy and are replaced by fat. Endothelial cells and intramuscular nerve fibers remain structurally intact, consistent with nonvascular, nonneuropathic pathology.[4][7][12][14][15]  

### 7.3 Subcellular Level: Sarcomeres, Myofibrils, and Vacuoles  

At the subcellular level, MYH2-related myopathy involves key compartments such as sarcomeres, myofibrils, lysosomes/autophagic vacuoles, and the cytoskeleton. GO Cellular Component terms relevant include GO:0030017 (sarcomere), GO:0030016 (myofibril), GO:0005776 (autophagosome), GO:0005829 (cytosol), and GO:0005884 (actin filament).[4][7][12][14]  

In dominant IBM3, mutated MyHC IIa disrupts sarcomere organization, leading to focal breakdown of A-bands and I-bands and formation of minicores—localized regions lacking normal myofibrillar structure.[7][12][14] Aggregated proteins and tubulofilaments accumulate in rimmed vacuoles, which are autophagic lysosomal structures attempting to degrade misfolded proteins. These vacuoles often line up at the periphery of fibers, giving the characteristic “rimmed” appearance on histology.[7][12][14]  

In recessive disease, subcellular pathology centers on absence of MyHC IIa from thick filaments in type 2A fibers, preventing normal sarcomeric assembly. Fibers may show mild myofibrillar disarray but lack the prominent vacuoles and inclusions seen in IBM3.[3][4][7][15] Mitochondria remain relatively intact, though minicores may show mitochondrial depletion in some dominant cases. Nuclear morphology is generally normal, and neuromuscular junction structures appear unremarkable.  

### 7.4 Localization and Lateralization  

Clinically, weakness and ophthalmoplegia in MYH2-related myopathy are generally bilateral and symmetric, reflecting diffuse involvement of muscle populations expressing MyHC IIa.[3][4][5][7][9][10][14][15][16] There is no strong lateralization, and asymmetric weakness or ocular involvement would prompt consideration of alternative diagnoses such as cranial nerve palsies or acquired myopathies.  

Anatomical localization of pathology has been detailed in imaging and biopsies. Thigh muscles (e.g., quadriceps, hamstrings) often show fatty infiltration in MRI, and biopsies are typically taken from proximal muscles such as vastus lateralis or biceps brachii.[4][7][10][14][15] Extraocular muscles show atrophy and fibrosis on imaging in CPEO but are rarely biopsied due to surgical challenges. In the head and neck, levator palpebrae superioris muscle involvement leads to ptosis. Uberon terms UBERON:0000948 (thigh), UBERON:0008891 (eyelid), and UBERON:0002108 (skeletal muscle of head) may be used to annotate localization.  

## 8. Temporal Development  

### 8.1 Age of Onset and Onset Pattern  

MYH2-related myopathy typically presents in childhood or adolescence, though recessive and dominant subtypes differ somewhat in onset characteristics. OMIM describes CMYO6 as having “childhood onset of symptoms,” indicating that weakness and ophthalmoplegia generally begin before adulthood.[5] Dominant MyHC IIa myopathy often features congenital joint contractures at birth, which resolve over time, followed by adolescent-onset external ophthalmoplegia and proximal weakness.[2][5][7][14] Darin et al. and Martinsson et al. described individuals with arthrogryposis at birth who later developed ocular and limb-girdle symptoms, demonstrating a biphasic course with an early structural phase and later functional phase.[2][7][14]  

Recessive MYH2 myopathy presents with early-onset, nonprogressive diffuse weakness and ophthalmoplegia. Tajsharghi et al. and ClinGen summarize recessive disease as “early onset, non-progressive, diffuse weakness and ophthalmoplegia,” usually arising in childhood and remaining relatively stable thereafter.[3][15] Patients may have delayed motor milestones, mild facial weakness, and ocular limitations from early in life.  

Recent reports indicate that adult-onset variants exist. Baskar et al. described adult patients with MYH2 mutations presenting with CPEO and minimal skeletal abnormalities, with onset in adulthood.[9] Cassini et al. reported a family with slowly progressive proximal myopathy with onset in adolescence or early adulthood, lacking congenital contractures or ophthalmoplegia.[10] These cases expand the age-of-onset spectrum and suggest that some MYH2 variants may cause late-onset disease. Overall, onset is chronic and insidious rather than acute or subacute.  

### 8.2 Disease Progression, Stages, and Duration  

The progression of MYH2-related myopathy varies by subtype and mutation but is generally mild to moderate. OMIM notes that CMYO6 is “either slowly progressive or nonprogressive, and affected individuals retain ambulation, although there is variable severity.”[5] Recessive cases are often nonprogressive or minimally progressive, with stable weakness and ophthalmoplegia over decades, reflecting developmental absence of type 2A fibers rather than ongoing degeneration.[3][4][7][15]  

Dominant IBM3 can be more progressive, especially in adults with rimmed vacuoles and dystrophic changes. Myosinopathies reviews describe a “Progressive course in some adults affecting ambulation,” and note that rimmed vacuoles are seen in adults with progressive course and dystrophic muscle changes.[7] Over time, muscle fibers degenerate and are replaced by fat and connective tissue, leading to increased weakness and, in some cases, difficulty with independent

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 44 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 2 |
| Unverifiable | 2 |
| Terms whose name was checked | 39 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 18 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000622` (2 mentions) - the report calls it "External ophthalmoplegia"; HP calls it **Blurred vision**
- `HP:0001769` (1 mention) - the report calls it "Scapular winging"; HP calls it **Broad foot**
- `HP:0007340` (1 mention) - the report calls it "Cytoplasmic inclusion bodies in muscle fibers"; HP calls it **Lower limb muscle weakness**
- `HP:0003457` (1 mention) - the report calls it "Myopathic EMG pattern"; HP calls it **EMG abnormality**
- `HP:0003215` (1 mention) - the report calls it "Abnormal muscle MRI"; HP calls it **Elevated urinary dicarboxylic acid level**
- `HP:0001324` (1 mention) - the report calls it "Fatigue"; HP calls it **Muscle weakness**
- `HP:0002355` (1 mention) - the report calls it "Reduced activity tolerance"; HP calls it **obsolete Difficulty walking**
- `GO:0048747` (1 mention) - the report calls it "muscle fiber maturation"; GO calls it **GO_0048747**
- `HP:0100806` (1 mention) - the report calls it "Autophagic vacuoles in muscle fibers"; HP calls it **Sepsis**
- `GO:0048754` (1 mention) - the report calls it "branching involved in skeletal muscle organ development"; GO calls it **branching morphogenesis of an epithelial tube**
- `GO:0009898` (2 mentions) - the report calls it "cytoplasmic protein catabolic process"; GO calls it **cytoplasmic side of plasma membrane**
- `CL:0000670` (2 mentions) - the report calls it "fast-twitch skeletal muscle fiber"; CL calls it **primordial germ cell**
- `CL:0000700` (2 mentions) - the report calls it "extraocular muscle cell"; CL calls it **dopaminergic neuron**
- `UBERON:0002106` (1 mention) - the report calls it "skeletal muscle tissue"; UBERON calls it **spleen**
- `UBERON:0001630` (1 mention) - the report calls it "extraocular skeletal muscle"; UBERON calls it **muscle organ**
- `UBERON:0000948` (1 mention) - the report calls it "thigh"; UBERON calls it **heart**
- `UBERON:0008891` (1 mention) - the report calls it "eyelid"; UBERON calls it **external gill**
- `UBERON:0002108` (1 mention) - the report calls it "skeletal muscle of head"; UBERON calls it **small intestine**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0003483` (2 mentions), reported as "Rimmed vacuoles on muscle biopsy" - HP does not contain this term
- `HP:0003723` (1 mention), reported as "Gait disturbance" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0002355` (obsolete Difficulty walking) (1 mention) - replaced by `HP:0001288`
- `GO:0048747` (GO_0048747) (1 mention) - replaced by `GO:0055001`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003690` (2 mentions) - the report calls it "Proximal muscle weakness"; HP calls it **Limb muscle weakness**
- `HP:0002829` (2 mentions) - the report calls it "Arthrogryposis"; HP calls it **Arthralgia**
- `HP:0001371` (1 mention) - the report calls it "Joint contracture"; HP calls it **Flexion contracture**
- `GO:0016071` (1 mention) - the report calls it "protein catabolic process"; GO calls it **mRNA metabolic process**
- `GO:0007507` (2 mentions) - the report calls it "muscle fiber development"; GO calls it **heart development**
- `GO:0001764` (1 mention) - the report calls it "neuron adhesion"; GO calls it **neuron migration**
- `CL:0000746` (1 mention) - the report calls it "skeletal muscle fiber"; CL calls it **cardiac muscle cell**, and lists "cardiac muscle fiber" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.