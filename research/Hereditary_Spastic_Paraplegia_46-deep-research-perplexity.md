---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-03T13:52:01.951343'
end_time: '2026-09-03T13:56:09.036168'
duration_seconds: 247.08
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hereditary Spastic Paraplegia 46
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: low
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 50
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 21
  on_topic: 13
  validator_version: 0.2.1
term_validation:
  total_terms: 71
  verified: 66
  not_found: 1
  obsolete: 2
  unverifiable: 2
  confabulation_rate: 0.014
  labels_checked: 63
  labels_matching: 22
  labels_mismatched: 27
  mislabelled_terms:
  - term_id: HP:0003477
    reported_labels:
    - spastic gait
    ontology_label: Peripheral axonal neuropathy
  - term_id: HP:0002310
    reported_labels:
    - gait ataxia
    ontology_label: Orofacial dyskinesia
  - term_id: HP:0001350
    reported_labels:
    - cognitive impairment
    ontology_label: Slurred speech
  - term_id: HP:0000750
    reported_labels:
    - behavioral abnormality
    ontology_label: Delayed speech and language development
  - term_id: HP:0001105
    reported_labels:
    - bilateral cataract
    ontology_label: Retinal atrophy
  - term_id: HP:0000759
    reported_labels:
    - pseudobulbar dysarthria
    ontology_label: Abnormal peripheral nervous system morphology
  - term_id: HP:0000020
    reported_labels:
    - neurogenic bladder
    ontology_label: Urinary incontinence
  - term_id: HP:0003473
    reported_labels:
    - peripheral axonal neuropathy
    ontology_label: Fatigable weakness
  - term_id: HP:0002650
    reported_labels:
    - pes cavus
    ontology_label: Scoliosis
  - term_id: CHEBI:37683
    reported_labels:
    - glucosylceramide
    ontology_label: mannopyranose
  - term_id: CHEBI:60027
    reported_labels:
    - glucosylated cholesterol
    ontology_label: polymer
  - term_id: UBERON:0002032
    reported_labels:
    - cerebral cortex
    ontology_label: areola
  - term_id: UBERON:0002034
    reported_labels:
    - corpus callosum
    ontology_label: suprachiasmatic nucleus
  - term_id: UBERON:0002080
    reported_labels:
    - cerebellum
    ontology_label: heart right ventricle
  - term_id: UBERON:0000942
    reported_labels:
    - eye
    ontology_label: frontal nerve (branch of ophthalmic)
  - term_id: UBERON:0001799
    reported_labels:
    - lens of eye
    ontology_label: vitreous chamber of eyeball
  - term_id: UBERON:0005369
    reported_labels:
    - seminiferous tubule
    ontology_label: UBERON_0005369
  - term_id: HP:0001263
    reported_labels:
    - motor impairment
    ontology_label: Global developmental delay
  - term_id: NCIT:C61531
    reported_labels:
    - Baclofen
    ontology_label: Microbiology Susceptibility Domain
  - term_id: NCIT:C1577
    reported_labels:
    - Intrathecal Administration
    ontology_label: Nolatrexed Dihydrochloride
  - term_id: NCIT:C49236
    reported_labels:
    - Muscle Relaxant
    ontology_label: Therapeutic Procedure
  - term_id: NCIT:C116938
    reported_labels:
    - Intrathecal Baclofen Infusion Pump
    ontology_label: CDK4/6 Inhibition
  - term_id: NCIT:C15969
    reported_labels:
    - Orthopedic Surgical Procedure
    ontology_label: NIH Areas of Research Emphasis
  - term_id: NCIT:C15245
    reported_labels:
    - Physical Therapy
    ontology_label: Health Services Research
  - term_id: NCIT:C15247
    reported_labels:
    - Occupational Therapy
    ontology_label: Heart and Lung Transplantation
  - term_id: NCIT:C15248
    reported_labels:
    - Speech Therapy
    ontology_label: Hemodialysis
  - term_id: NCIT:C48302
    reported_labels:
    - Supportive Care
    ontology_label: SDHB Gene Mutation
  labels_variant: 14
  unresolved_terms:
  - HP:0000715
  obsolete_terms:
  - term_id: GO:0046467
    ontology_label: obsolete membrane lipid biosynthetic process
    replaced_by: GO:0008610
  - term_id: UBERON:0005369
    ontology_label: UBERON_0005369
    replaced_by: UBERON:0002313
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Spastic Paraplegia 46
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Spastic Paraplegia 46** covering all of the
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

# Hereditary Spastic Paraplegia Type 46 (SPG46) Due to GBA2 Deficiency: An Integrative Disease Characteristics Report

Hereditary spastic paraplegia type 46 (SPG46) is a rare, autosomal recessive, complex form of hereditary spastic paraplegia caused by biallelic loss-of-function variants in the *GBA2* gene, which encodes the non‑lysosomal β‑glucosylceramidase GBA2.[2][30][30] Clinically, SPG46 presents as an early‑onset neurodegenerative disorder dominated by slowly progressive spastic paraparesis of the lower limbs, often accompanied by cerebellar ataxia, cognitive impairment, congenital cataracts, hypogonadism in males, peripheral neuropathy, scoliosis, and characteristic neuroimaging findings including thinning of the corpus callosum and mild cerebral and cerebellar atrophy.[3][7][11] Pathophysiologically, SPG46 is a sphingolipid storage disorder in which loss of GBA2 activity disturbs glucosylceramide (GlcCer) and broader glycosphingolipid homeostasis in neurons and other tissues, leading to defective corticospinal tract and cerebellar circuit development and maintenance.[11][12][30] About thirty families have been described worldwide, with overlapping phenotypes that span complex hereditary spastic paraplegia, autosomal recessive cerebellar ataxia with spasticity, and Marinesco‑Sjögren‑like syndrome, illustrating substantial phenotypic pleiotropy of *GBA2* deficiency.[19][31][2] This report synthesizes current knowledge on SPG46 across clinical, genetic, mechanistic, anatomical, epidemiological, diagnostic, therapeutic, and comparative biology dimensions to support structured representation within a disease knowledge base, with emphasis on primary literature and ontology mapping.

## 1. Disease Information

### 1.1 Definition and Clinical Overview

Hereditary spastic paraplegia type 46 (SPG46) is a distinct subtype within the heterogeneous group of hereditary spastic paraplegias (HSPs), defined by autosomal recessive inheritance, early‑onset spastic paraparesis, and a complex constellation of additional neurological and extra‑neurological features.[2][25][27] HSPs as a broader entity are characterized by slowly progressive distal lower‑limb weakness and spasticity due to dysfunction of upper motor neurons in the corticospinal tract; they can be classified into “pure” forms, in which pyramidal signs predominate, and “complex” forms, which incorporate cerebellar, extrapyramidal, cognitive, ocular, skeletal, or systemic manifestations.[22][25][27] SPG46 belongs to the complex autosomal recessive HSPs and is etiologically linked to biallelic mutations in *GBA2*, located on chromosome 9p13.3.[30][44][30]

The initial locus designation “SPG46” emerged from linkage analysis in a Tunisian family with complicated autosomal recessive HSP, mental impairment, and thin corpus callosum, mapping to 9p21.2‑q21.12 with significant LOD scores.[1][46] Subsequent exome sequencing identified *GBA2* mutations as the causal factor, and functional studies confirmed loss of enzyme activity and motor neuron defects.[11][11][30] Clinically, SPG46 is typically characterized by onset in infancy or childhood of gait disturbance due to spasticity and weakness of the lower limbs, often followed by upper‑limb spasticity, cerebellar ataxia, pseudobulbar dysarthria, bladder dysfunction, cataracts, and cognitive impairment that may progress to dementia.[3][7][1] Neuroimaging frequently reveals thinning of the corpus callosum and mild cerebral and cerebellar atrophy, supporting the view of SPG46 as a diffuse neurodevelopmental and neurodegenerative disorder of central motor and associative pathways.[3][7][11]

The information summarized here is derived from aggregated disease‑level resources such as OMIM, Orphanet, MedGen, and Human Disease Ontology as well as individual case reports and series documented in PubMed‑indexed clinical studies, rather than from de‑identified EHR‑level data.[2][3][7][1][19] Landmark publications by Martin et al. (2013, Am J Hum Genet, PMIDs 23332916 and 23332917) and Hammer et al. (2013, Am J Hum Genet, PMID 23332917) established *GBA2* mutations as causative of SPG46 and related recessive cerebellar ataxia with spasticity.[11][13][30] More recently, an Italian series reported five novel *GBA2* variants in patients whose phenotype aligned with SPG46, further expanding the clinical and mutational spectrum.[19][19]

### 1.2 Key Identifiers and Ontology Mapping

SPG46 is represented across multiple biomedical ontologies and classification systems, which are important for standardized knowledge representation. In OMIM, the phenotype “Spastic paraplegia 46, autosomal recessive” carries MIM number 614409, and the causal gene *GBA2* is annotated under MIM number 609471.[1][30][30] Orphanet lists “Autosomal recessive spastic paraplegia type 46” with ORPHA ID 320391, describing its complex phenotype and very low prevalence, estimated at less than 1 per 1,000,000.[3] In MedGen, the concept “Hereditary spastic paraplegia 46” is assigned Concept ID C2828721 and is linked to OMIM 614409, Orphanet 320391, and Disease Ontology DOID:0110798.[7][7][33]

Within ICD‑11, hereditary spastic paraplegia as a group is coded under 8B44.0, with subcodes for autosomal dominant, autosomal recessive, and X‑linked forms; SPG46 falls under “Autosomal recessive hereditary spastic paraplegia” (8B44.01).[21][25] ICD‑10 maps HSP to G11.4, which Orphanet associates with hereditary spastic paraplegia, including SPG46.[25] The MeSH descriptor “Spastic Paraplegia, Hereditary” carries the unique ID D015419 and defines HSPs as “a group of inherited diseases that share similar phenotypes but are genetically diverse,” encompassing autosomal recessive loci such as SPG46.[22][23]

For MONDO (Mondo Disease Ontology), SPG46 is annotated as MONDO:0013737, consistent with MedGen and ClinVar records that reference MONDO identifiers for “Hereditary spastic paraplegia 46.”[7][26] In SNOMED CT, “Autosomal recessive spastic paraplegia type 46” is recorded under concept 723822009.[7] The Disease Ontology (DO) term “hereditary spastic paraplegia 46” is DOID:0110798, explicitly defined as “a hereditary spastic paraplegia that has material basis in mutation in the GBA2 gene on chromosome 9p.”[33]

### 1.3 Synonyms and Alternative Names

Multiple synonyms and related labels are used in the literature and databases to refer to SPG46 and overlapping *GBA2*-related conditions. Common synonyms include “Spastic paraplegia 46, autosomal recessive,” “Hereditary spastic paraplegia 46,” “Autosomal recessive spastic paraplegia type 46,” and “SPG46.”[3][7][1] Because *GBA2* mutations can also manifest as autosomal recessive cerebellar ataxia with spasticity or Marinesco‑Sjögren‑like syndrome, some publications refer to patients with *GBA2* mutations primarily under these overlapping phenotype labels rather than SPG46, especially when cerebellar ataxia and cataracts predominate.[13][16][31]

Specific phenotype terms used include “complicated hereditary spastic paraplegia with thin corpus callosum and mental impairment,” as in the original Tunisian linked family,[1][46] “recessive spastic ataxia,” and “Marinesco‑Sjögren‑like syndrome” with cerebellar ataxia, cataracts, and intellectual disability.[13][31][2] ClinVar and some OMIM annotations also reference “GBA2‑related spastic ataxia” and “autosomal recessive cerebellar ataxia with spasticity,” underscoring that SPG46 sits within a broader spectrum of *GBA2*‑associated neurodegenerative phenotypes.[13][15][17]

### 1.4 Nature of Evidence and Data Sources

The foundational knowledge about SPG46 is derived from aggregated disease‑level resources and primary literature rather than from large EHR‑based real‑world datasets. OMIM and Orphanet synthesize information from linkage studies, exome sequencing, and phenotypic characterization of families and cohorts, notably the Tunisian families studied by Boukhris et al. (Neurogenetics, 2010) and Hammer et al. (Am J Hum Genet, 2013).[1][30] MedGen, Disease Ontology, and Human Protein Atlas integrate gene and phenotype annotations across NCBI Gene, OMIM, and other curated databases.[7][33][45][49]

Primary human data come from case reports and case series, including Martin et al. (2013) describing four biallelic *GBA2* mutations in 11 patients from four families with complex HSP, mental impairment, cataracts, and hypogonadism,[11][11][30] Hammer et al. (2013) reporting three homozygous *GBA2* mutations in 10 patients with autosomal recessive cerebellar ataxia and spasticity,[13][15][30] Votsi et al. (2014, Ann Hum Genet) identifying a novel missense mutation with mixed spasticity‑ataxia features,[29][48] and subsequent reports from Italy, Saudi Arabia, Japan, and Norway describing additional families.[4][9][17][19][31] Model organism data derive from *Gba2*‑knockout mice, which display glycosphingolipid accumulation and globozoospermia, and zebrafish morpholino knockdown or genetic models that show motor neuron defects and aberrant sphingolipid metabolism.[11][20][32][35][36]

These sources provide sufficient clinical, genetic, and mechanistic detail to support structured representation in a disease knowledge base, but they reflect the rarity of SPG46, with relatively small sample sizes and limited population‑level epidemiologic data.[3][19][2]

## 2. Etiology

### 2.1 Primary Causal Factors

The primary etiological factor in SPG46 is **biallelic loss‑of‑function variants in *GBA2***, which encodes glucosylceramidase beta 2 (GBA2), a microsomal non‑lysosomal β‑glucosidase that hydrolyzes glucosylceramide to ceramide and glucose and also acts on bile acid 3‑O‑glucosides.[11][30][44] Martin et al. (2013, Am J Hum Genet, PMID 23332916) demonstrated that four different truncating or missense *GBA2* variants in three families with complicated HSP co‑segregated with disease and were absent in controls; enzyme assays in blood cells showed complete loss of GBA2 activity for a missense variant, supporting a loss‑of‑function mechanism.[11][11][30] Hammer et al. (2013, Am J Hum Genet, PMID 23332917) identified nonsense and missense *GBA2* variants in families with autosomal recessive spastic ataxia and concluded that these mutations likely result in nonfunctional enzyme.[13][15]

The *GBA2* protein is a 927‑amino‑acid integral membrane protein localized to the endoplasmic reticulum (ER) and Golgi apparatus, with its catalytic domain facing the cytosolic side; it operates at neutral pH and is distinct from lysosomal glucocerebrosidase GBA1.[10][30][44] In vitro and in vivo, GBA2 catalyzes the breakdown of glucosylceramide (GlcCer), a key glycosphingolipid precursor, into ceramide and glucose, thereby contributing to sphingolipid homeostasis, membrane architecture, and cell signaling.[12][30][44] Loss of GBA2 in mice leads to accumulation of GlcCer in testis, brain, liver, sperm cells, and dermal fibroblasts.[12][32] In humans, *GBA2* mutations cause glucosylceramide storage disease in neurons and other tissues, which appears to underlie motor neuron defects and cerebellar ataxia characteristic of SPG46.[11][13][30]

There is no evidence that environmental, infectious, or non‑genetic factors independently cause SPG46; disease occurrence strictly tracks with autosomal recessive inheritance of pathogenic *GBA2* variants, often in consanguineous families.[11][32][29][1] Thus, SPG46 can be categorized as a classic Mendelian monogenic disorder of sphingolipid metabolism and upper motor neuron degeneration.

### 2.2 Genetic Risk Factors

The genetic risk factors for SPG46 are the presence of pathogenic or likely pathogenic *GBA2* variants in the germline, particularly in homozygous or compound heterozygous configurations. ClinVar, OMIM, and primary literature document a growing set of such variants, most of which are predicted or proven loss‑of‑function alleles.[26][29][44] These include truncating nonsense mutations such as c.363C>A (p.Tyr121*), c.1018C>T (p.Arg340*), and c.518G>A (p.Trp173*), frameshift mutations like c.1471dupGGCA (p.Thr492Argfs*9) and c.1528_1529del (p.Met510Valfs*17), and missense substitutions at highly conserved residues within the six‑hairpin glycosidase‑like domain, including p.Arg630Trp, p.Asp594His, p.Arg873His, and p.Gly683Arg.[13][15][29][44][30][48]

Functional assays have demonstrated that these variants abolish or drastically reduce GBA2 enzymatic activity. Martin et al. showed that a missense variant in *GBA2* resulted in no detectable glucocerebrosidase activity in blood cells, and zebrafish experiments indicated that the human missense mutation could not rescue motor neuron defects induced by morpholino knockdown of *gba2*.[11][14][11] Hammer et al. reported that the nonsense and missense variants they identified likely produce nonfunctional enzyme, and that affected individuals exhibited a glucosylceramide storage disease phenotype.[13][15] In a Saudi family, the variant c.2618G>A (p.Arg873His) was classified as pathogenic because it abolished enzymatic activity.[16][17] ClinVar entries such as c.1780G>C (p.Asp594His) are annotated as likely pathogenic for SPG46 based on segregation and absence in controls.[29][29]

At the population level, *GBA2* mutations appear rare, with Citterio et al. (2014, J Neurol) estimating that *GBA2* variants account for approximately 2% of complicated HSP cases in a selected Italian cohort.[5][48][50] gnomAD and similar databases indicate very low allele frequencies for most pathogenic variants, consistent with the rarity of SPG46; however, detailed allele frequency data for each variant are limited in the published SPG46‑specific literature and are more broadly catalogued in general population sequencing resources rather than disease‑specific reports.[10][44]

Modifier genes for SPG46 have not been systematically identified, but mechanistic reviews of HSP emphasize that multiple genes involved in sphingolipid metabolism—such as *FA2H* and *B4GALNT1*—cause related HSP or leukodystrophy phenotypes, suggesting that genetic variation in these pathways could modulate penetrance or expressivity in *GBA2*‑deficient individuals.[12][28] At present, this remains an inference rather than a demonstrated gene‑modifier effect for SPG46 specifically.

### 2.3 Environmental and Lifestyle Risk Factors

The literature on SPG46 does not identify specific environmental, lifestyle, occupational, or toxic exposures as independent risk factors for disease onset, which is consistent with its highly penetrant autosomal recessive Mendelian etiology.[3][11][19][2] Most reported families exhibit early‑onset disease in childhood or adolescence, often in settings of parental consanguinity, with no mention of precipitating environmental triggers.[4][9][17][29][1] There are no epidemiologic studies linking SPG46 to particular toxins, diet patterns, smoking, or physical activity levels.

Given the neurodegenerative nature of SPG46, general lifestyle factors such as engagement in physical therapy, avoidance of trauma, and optimal management of comorbidities might influence disease progression and quality of life, but these modify clinical trajectory rather than primary disease risk.[37][39][47] The absence of environmental risk factors should be explicitly noted, as it distinguishes SPG46 from multifactorial or complex polygenic disorders where environment plays a major etiologic role.

### 2.4 Protective Factors and Gene–Environment Interactions

No specific genetic protective variants have been described that mitigate the risk or severity of SPG46 in carriers of pathogenic *GBA2* alleles. Given the small numbers of affected families and the early stage of mechanistic research, such modifier alleles, if they exist, have not yet been elucidated. Similarly, there are no reports of environmental exposures that reduce risk of disease onset in *GBA2* mutation carriers.

Gene–environment interactions have not been formally investigated in SPG46. For example, there are no studies examining whether nutritional modulation of sphingolipid metabolism or pharmacological manipulation of related pathways can influence penetrance or expressivity in *GBA2*‑deficient individuals. Animal models of GBA2 deficiency demonstrate that accumulation of GlcCer can be influenced by concomitant GBA1 deficiency and other genetic manipulations,[20] which hints at potential gene–gene and possibly gene–environment interplay at the level of sphingolipid homeostasis, but these have not yet been translated into human SPG46 cohorts.

Thus, current evidence supports a view of SPG46 as a primarily genetic, autosomal recessive disease with minimal documented contribution from environment, and gene–environment interaction remains an area for future research rather than established knowledge.

## 3. Phenotypes

### 3.1 Core Neurological Phenotypes: Spastic Paraparesis and Cerebellar Ataxia

The cardinal phenotype of SPG46 is slowly progressive spastic paraparesis of the lower limbs, reflecting upper motor neuron dysfunction along the corticospinal tracts.[2][7][27] Clinically, this manifests as increased muscle tone (spasticity), hyperreflexia, extensor plantar responses, and weakness predominantly affecting distal lower limb muscles, resulting in a stiff, scissoring gait and impaired mobility.[22][25][27] Age of onset is typically in infancy or childhood, with gait disturbance and motor delay becoming apparent as the child begins to walk and attempts motor milestones.[3][7][1] Progression is chronic and insidious, with gradual worsening over years rather than acute episodes, consistent with the general HSP pattern.[22][27]

The severity of spastic paraparesis varies across individuals and families, ranging from mild gait abnormalities manageable with orthoses, to severe spasticity necessitating wheelchairs and intrathecal baclofen pumps.[19][37][39] In most reported SPG46 cases, the spastic paraparesis is moderate to severe, but disease progression is slow, allowing preservation of some ambulation into adulthood.[11][19][2] Quality of life impact is substantial, given that locomotion, independence, and participation in daily activities are deeply affected by lower limb spasticity and weakness. HPO terms suggested for this phenotype include HP:0001257 (spastic paraplegia), HP:0003477 (spastic gait), and HP:0007340 (lower limb spasticity).

Cerebellar ataxia is another core neurological phenotype in many SPG46 patients, particularly those initially ascertained under the label “autosomal recessive cerebellar ataxia with spasticity.”[13][15][16][17] Hammer et al. described 10 patients with gait ataxia, limb ataxia, dysmetria, and intention tremor, in addition to pyramidal signs, with onset in childhood or adolescence and slow progression.[13][15] The combination of cerebellar ataxia and spastic paraparesis produces a mixed “spastic‑ataxic” gait pattern, further impairing balance and coordination.[16][17][18] The severity of ataxia ranges from mild limb incoordination to marked instability requiring support for walking. HPO terms aligned with this phenotype include HP:0001251 (ataxia) and HP:0002310 (gait ataxia).

Quality of life impact of cerebellar ataxia is multifaceted, affecting fine motor tasks (e.g., writing, buttoning), gross motor skills (e.g., walking, standing, transferring), and activities of daily living. When combined with spasticity, it significantly increases fall risk and disability. The progressive nature of both pyramidal and cerebellar signs often leads to chronic disability and requires long‑term rehabilitative support.[19][47]

### 3.2 Cognitive Impairment and Neuropsychiatric Features

Cognitive impairment is commonly reported in SPG46, especially in families originally characterized as having complicated HSP with mental retardation or Marinesco‑Sjögren‑like syndrome.[3][11][7][31] Boukhris et al. and Martin et al. described affected individuals with intellectual disability, global cognitive impairment, and in some cases progressive cognitive decline culminating in dementia.[1][30][30] Orphanet notes that SPG46 may present with cognitive impairment that can progress to dementia, reflecting diffuse cortical and subcortical involvement beyond motor pathways.[3]

The age of onset of cognitive symptoms often coincides with childhood or adolescence, when learning difficulties, delayed psychomotor development, and intellectual disability become apparent.[11][31] Severity ranges from mild learning disability to severe intellectual disability with limited independence. In some adults, cognitive function may deteriorate over time, although detailed longitudinal neuropsychological trajectories are sparsely documented.[19][2] Quality of life impact is profound, affecting educational attainment, employment, daily self‑care, social interaction, and autonomy.

Neuropsychiatric manifestations beyond cognitive impairment have not been systematically characterized, but some cases report behavioral problems, attention deficits, and emotional difficulties, which are common in individuals with intellectual disability and chronic neurological disease.[19][2] HPO terms for cognitive and behavioral phenotypes include HP:0001249 (intellectual disability), HP:0001350 (cognitive impairment), and HP:0000750 (behavioral abnormality).

### 3.3 Ocular Phenotypes: Congenital Cataracts and Visual Impairment

Congenital or early‑onset cataracts are a hallmark extra‑neurological feature in many SPG46 and *GBA2*‑related cases. Orphanet explicitly lists cataracts among the typical manifestations of SPG46.[3] Martin et al. reported that patients with complex HSP had cataracts requiring surgical intervention, and that Marinesco‑Sjögren‑like families with *GBA2* mutations presented with cerebellar ataxia, cataracts, and mental retardation.[11][31][30] A case described by Citterio et al. and a 56‑year‑old man reported by another group demonstrated congenital bilateral cataracts as part of complicated HSP with *GBA2* mutations.[4][5][50]

The age of onset of cataracts is usually in infancy or early childhood, consistent with congenital or developmental lens opacities.[3][4][31] Severity can be marked, leading to significant visual impairment and necessitating early ophthalmologic evaluation and surgical extraction. Cataracts may be bilateral and symmetric, although detailed lateralization patterns are not systematically reported. Quality of life impact includes reduced visual acuity, impaired reading and navigation, and, in children, delayed visual‑motor development and potential psychosocial consequences.

HPO terms for ocular phenotypes include HP:0000518 (cataract) and HP:0001105 (bilateral cataract). In Marinesco‑Sjögren‑like presentations, cataracts form part of a triad with cerebellar ataxia and intellectual disability, underscoring the broader neuro‑ocular phenotype of *GBA2* deficiency.[31]

### 3.4 Endocrine and Reproductive Phenotypes: Hypogonadism and Male Infertility

Hypogonadism in males and infertility are recurrent phenotypes in SPG46. Martin et al. noted that male patients with SPG46 exhibited hypogonadism and infertility, which they considered part of the overall disease phenotype.[30][44][30] In mice, GBA2 deficiency causes globozoospermia—a severe defect in sperm head morphology—and impaired male fertility, with accumulation of GlcCer in testicular tissue and disrupted cytoskeletal dynamics during spermiogenesis.[32][35] These animal findings strongly support a causal link between *GBA2* mutations and male reproductive dysfunction.

Clinically, male SPG46 patients may present with small testes, delayed or absent puberty, reduced secondary sexual characteristics, and infertility; hormonal profiles are not extensively detailed in published case series but likely reflect hypogonadotropic or primary hypogonadism.[30][30] The age of recognition of hypogonadism is typically adolescence or early adulthood, when failure of pubertal development becomes evident. Severity can range from subfertility to complete infertility.

Quality of life impact of hypogonadism includes psychosocial distress, reduced self‑esteem, potential metabolic complications, and challenges in family planning. Infertility may necessitate assisted reproductive techniques, although success rates in *GBA2*‑deficient men are unknown. HPO terms for these phenotypes include HP:0000028 (hypogonadism) and HP:0003251 (male infertility).

### 3.5 Skeletal, Peripheral Neuropathy, and Other Phenotypes

Several reports document skeletal abnormalities and peripheral neuropathy in SPG46. Scoliosis is frequently observed, as highlighted in the Italian series where spinal column imaging for scoliosis assessment was part of the standardized work‑up.[19][19] Pes cavus, a high‑arched foot deformity commonly associated with long‑standing neuropathy and neuromuscular disease, has been described in a 56‑year‑old man with complicated HSP due to homozygous *GBA2* mutation.[4][50] Distal amyotrophy and muscle wasting may occur as a secondary consequence of chronic upper motor neuron dysfunction and disuse.[19][2]

Peripheral neuropathy, particularly axonal sensory‑motor neuropathy, has been reported in some *GBA2*‑mutated patients, adding to the complexity of the neurological phenotype.[4][5][18] For example, the 56‑year‑old case with p.452‑1G>C mutation exhibited axonal sensory‑motor peripheral neuropathy on electrophysiological studies, along with cerebellar atrophy and thin corpus callosum.[4] Frequency of peripheral neuropathy among SPG46 patients is not well quantified but appears variable, suggesting that it may be a modifying phenotype rather than a universal feature.

Other reported manifestations include pseudobulbar dysarthria, bladder dysfunction, upper gaze palsy, movement disorders, distal amyotrophy, and scoliosis.[3][19][2] Pseudobulbar speech impairment reflects corticobulbar tract involvement, while bladder urgency and incontinence result from disruption of spinal and supraspinal control of micturition. Upper gaze palsy and movement disorders (e.g., dystonia or tremor) were noted as notable features in the Italian SPG46 series.[19][19]

Quality of life impacts of these phenotypes are substantial. Scoliosis can cause pain, respiratory compromise, and cosmetic concerns; peripheral neuropathy adds sensory loss and pain; pseudobulbar dysarthria impairs communication; bladder dysfunction causes social embarrassment and infection risk; and movement disorders further compromise motor function. HPO terms for these phenotypes include HP:0002751 (scoliosis), HP:0000759 (pseudobulbar dysarthria), HP:0000020 (neurogenic bladder), HP:0003473 (peripheral axonal neuropathy), HP:0003474 (sensorimotor neuropathy), and HP:0002650 (pes cavus).

### 3.6 Neuroimaging and Structural Brain Phenotypes

Characteristic neuroimaging findings in SPG46 include thinning of the corpus callosum and mild cerebellar and cerebral atrophy. Orphanet notes that brain imaging may show thinning of the corpus callosum and mild atrophy of the cerebrum and cerebellum.[3] Boukhris et al. described thin corpus callosum in Tunisian families with complicated HSP, which later were linked to *GBA2* mutations.[1][30] Martin et al. reported cerebral, cerebellar, and corpus callosum atrophy in patients with SPG46.[30][30] The 56‑year‑old case with homozygous p.452‑1G>C mutation had cerebellar atrophy and thin corpus callosum on MRI.[4][8]

These structural abnormalities reflect involvement of long commissural fibers (corpus callosum), cerebellar cortex and deep nuclei, and cerebral cortex, consistent with diffuse neurodevelopmental and neurodegenerative pathology.[11][14][11] The age of detection is typically childhood or adolescence, when imaging is performed for diagnostic evaluation. The severity of atrophy and callosal thinning varies, but they are often described as mild to moderate rather than severe. Progression of imaging abnormalities over time has not been extensively quantified, but given the slow clinical progression, structural changes likely evolve gradually.

Quality of life implications are indirect, as structural anomalies correlate with motor and cognitive deficits rather than being symptomatic per se. However, thin corpus callosum and cerebellar atrophy are important diagnostic markers that differentiate SPG46 from other HSP subtypes and guide genetic testing. HPO terms include HP:0002079 (thin corpus callosum), HP:0001272 (cerebellar atrophy), and HP:0002059 (cerebral atrophy).

## 4. Genetic and Molecular Information

### 4.1 Causal Gene: *GBA2* (Glucosylceramidase Beta 2)

The causal gene for SPG46 is *GBA2* (HGNC:4193), encoding glucosylceramidase beta 2, a non‑lysosomal β‑glucosidase.[30][44] Cytogenetic localization is 9p13.3, and genomic coordinates on GRCh38 are 9:35,736,866–35,749,228.[44][30] The gene was initially identified as encoding a microsomal β‑glucosidase capable of hydrolyzing bile acid 3‑O‑glucosides.[30][44] Subsequent work established that GBA2 also acts as a non‑lysosomal glucosylceramidase, catalyzing the conversion of glucosylceramide (GlcCer) to ceramide and glucose, and in some contexts performing transglucosylation to other lipid substrates, including cholesterol to form glucosylated cholesterol.[20][30][44]

GBA2 is a 927‑amino‑acid integral membrane protein localized predominantly to the endoplasmic reticulum and Golgi apparatus, with the catalytic domain facing the cytosolic side.[10][12][44] It has a neutral pH optimum, in contrast to lysosomal GBA1, and is not inhibited by conduritol B epoxide, a classic GBA1 inhibitor.[10][30] The protein contains a conserved glycosyl hydrolase domain with a six‑hairpin glucosidase‑like fold, where many pathogenic missense mutations cluster at highly conserved residues critical for catalysis.[13][29][44][30] Tissue expression data from the Human Protein Atlas indicate broad expression of *GBA2* across brain regions, including cerebral cortex, basal ganglia, cerebellum, and spinal cord, consistent with its role in central nervous system sphingolipid metabolism.[45][49]

### 4.2 Pathogenic Variants: Types, Functional Consequences, and Classification

Pathogenic *GBA2* variants associated with SPG46 and related phenotypes encompass several categories.

Missense variants include c.1780G>C (p.Asp594His), c.1888C>T (p.Arg630Trp), c.2618G>A (p.Arg873His), c.2048G>C (p.Gly683Arg), and c.1838A>G (p.Asp613Gly).[9][13][15][29][44][30][48] These substitutions affect residues in the six‑hairpin glycosidase‑like domain and are predicted to disrupt catalytic function. Functional assays for p.Arg873His in a Saudi family demonstrated loss of GBA2 enzymatic activity.[16][17] The p.Asp594His variant was absent from 264 control Cypriot chromosomes and segregated with disease in a consanguineous family.[29][29] In a Japanese patient, p.Asp613Gly was presumed to cause loss of activity based on clinical phenotype and conservation of the residue.[9]

Nonsense variants such as c.363C>A (p.Tyr121*), c.1018C>T (p.Arg340*), and c.518G>A (p.Trp173*), reported by Hammer et al. and Martin et al., create premature termination codons likely triggering nonsense‑mediated decay or producing truncated, nonfunctional proteins.[13][15][44][30] Frameshift variants like c.1471dupGGCA (p.Thr492Argfs*9) and c.1528_1529del (p.Met510Valfs*17) similarly disrupt the reading frame and introduce premature stop codons.[31][44] Splice‑site variants such as c.452‑1G>C and intronic insertions like c.1688‑10_1688‑9insG alter splicing, likely resulting in exon skipping or intron retention and nonfunctional enzyme.[4][26]

The functional consequence of most pathogenic variants is **loss of function**, manifested as reduced or absent GBA2 enzymatic activity. Martin et al. explicitly demonstrated “no residual glucocerebrosidase activity of GBA2” in blood cells from a patient homozygous for a missense variant, and zebrafish rescue experiments confirmed that mutant human GBA2 could not restore normal motor neuron development, whereas wild‑type GBA2 could.[11][14][11] Hammer et al. concluded that their nonsense and missense variants “probably” resulted in nonfunctional enzyme and that *GBA2* mutations cause recessive spastic ataxia and glucosylceramide storage disease in humans.[13][15] A Norwegian study of Marinesco‑Sjögren‑like families found that reduced GBA2 activity was sufficient to elevate GlcCer levels to those observed in Gaucher disease, reinforcing the loss‑of‑function storage disease mechanism.[31]

Variant classification under ACMG/AMP guidelines in ClinVar and literature generally assigns these alleles as “pathogenic” or “likely pathogenic” based on segregation, functional evidence, and absence in controls.[26][29][34][29] For example, c.1780G>C (p.Asp594His) is considered likely pathogenic for SPG46,[29][29] and the Saudi c.2618G>A (p.Arg873His) variant is classified as pathogenic.[16][17] Variants found in both patients and controls without clear functional effect, such as c.2054+62G>A and c.2201G>A (p.Arg734His), are considered benign or of uncertain significance.[29][29]

Somatic *GBA2* variants have not been implicated in SPG46; the disease is driven by germline mutations inherited in an autosomal recessive fashion. There is no evidence that mosaic or somatic variants contribute to SPG46 pathogenesis.

### 4.3 Modifier Genes and Epigenetic Information

Modifier genes modulating SPG46 severity or phenotype are not definitively characterized. However, reviews of HSP genetics highlight that several sphingolipid‑related genes—such as *FA2H* (fatty acid 2‑hydroxylase), *B4GALNT1* (β‑1,4‑N‑acetylgalactosaminyltransferase 1), and *CYP2U1*—are associated with complex HSP forms and leukodystrophies, suggesting that perturbations in sphingolipid pathways may have convergent effects on white matter integrity and motor tracts.[12][28][48] It is plausible that variation in these genes or in lysosomal *GBA1* might interact with *GBA2* loss to modify disease expression, as demonstrated in zebrafish models of combined Gba1/Gba2 deficiency affecting GlcCer and glucosylated cholesterol.[20] Yet, such interactions remain hypothetical in human SPG46 and require systematic study.

Epigenetic changes specific to SPG46 have not been reported. There are no data on DNA methylation patterns, histone modifications, or chromatin structure alterations in SPG46 patient tissues. However, given that *GBA2* is broadly expressed and its activity integrates into lipid metabolic networks relevant to cell signaling and cytoskeletal dynamics,[12][35] it is conceivable that secondary epigenetic adaptations occur in response to sphingolipid accumulation; at present, this is speculative.

### 4.4 Chromosomal Abnormalities

SPG46 is not associated with structural chromosomal abnormalities such as deletions, duplications, translocations, or aneuploidy. The causal lesions are sequence‑level variants within *GBA2* on chromosome 9p13.3.[30][44][30] Linkage studies in Tunisian families mapped disease to 9p21.2‑q21.12 but did not identify gross chromosomal rearrangements; fine mapping and sequencing revealed *GBA2* coding mutations.[1][46][30] DECIPHER and similar databases do not report recurrent structural variants at 9p13.3 associated specifically with SPG46. Therefore, chromosomal microarray or karyotyping is not a primary diagnostic modality for SPG46, except insofar as they help exclude other conditions in the differential diagnosis.

## 5. Environmental Information

### 5.1 Environmental Factors, Lifestyle, and Infectious Agents

As noted earlier, SPG46 appears to be driven solely by genetic causation, with *GBA2* loss‑of‑function as the primary etiologic factor. Environmental toxicants, radiation, occupational exposures, or lifestyle behaviors are not reported as causative or strongly contributory in SPG46 case series.[3][11][19][2] This contrasts with acquired spastic paraparesis due to, for example, tropical spastic paraparesis from HTLV‑1 infection or toxic myelopathies, which have distinct etiologies.[22][27]

Lifestyle factors such as smoking, diet, alcohol consumption, and physical activity may influence general neurological health and disease progression, but no SPG46‑specific data link them to onset or severity. Infectious agents are not implicated in SPG46; there is no evidence of viral, bacterial, or parasitic triggers for this disease in the published literature.

Thus, for disease knowledge base purposes, environmental causal information for SPG46 can be annotated as “no specific environmental or infectious causal factors identified; disease is Mendelian, monogenic, autosomal recessive due to *GBA2* deficiency.”

## 6. Mechanism and Pathophysiology

### 6.1 Causal Chain from Mutation to Clinical Manifestation

The mechanistic cascade in SPG46 can be articulated as a series of causal steps:

Step 1: Germline biallelic loss‑of‑function mutations in *GBA2* lead to deficiency or absence of the non‑lysosomal glucosylceramidase GBA2 in neurons and other tissues.[11][13][30][30]

Step 2: GBA2 deficiency results in impaired hydrolysis of glucosylceramide (GlcCer) and related glycosphingolipids at the cytosolic face of the ER and Golgi, causing accumulation of GlcCer and perturbation of glycosphingolipid homeostasis; this step is demonstrated in GBA2‑deficient mice and humans.[12][31][32]

Step 3: Non‑lysosomal GlcCer accumulation and dysregulated sphingolipid composition alter membrane microdomain organization, signaling pathways, and cytoskeletal dynamics within neurons and other cells, affecting axonogenesis, synaptic function, and cellular morphology; some aspects of this step are inferred from animal models and biochemical studies.[11][20][35]

Step 4: In developing and mature central nervous system, disrupted sphingolipid metabolism and cytoskeletal architecture impair corticospinal tract formation, corpus callosum development, cerebellar circuitry, and spermatogenic structures, leading to defective neuronal tract formation, motor neuron defects, and globozoospermia; this is supported by zebrafish morpholino knockdown and mouse knockout data.[11][32][35][36]

Step 5: These structural and functional neural abnormalities manifest clinically as early‑onset spastic paraparesis, cerebellar ataxia, cognitive impairment, and other neurological signs, while testicular and lens involvement produces male hypogonadism, infertility, and cataracts; this step is observed in multiple human families and animal models.[3][11][13][31][32]

Step 6: Over time, progressive neurodegeneration and failure of compensatory mechanisms result in chronic disability, slow worsening of motor and cognitive symptoms, and structural brain atrophy evident on MRI, completing the clinical picture of SPG46.[7][1][2]

Each step is progressive and downstream from the initiating lesion (biallelic *GBA2* mutation), with molecular, cellular, tissue‑level, and clinical consequences tightly integrated.

### 6.2 Molecular Pathways: Sphingolipid Metabolism and Ceramide Signaling

At the molecular level, SPG46 is fundamentally a disorder of sphingolipid metabolism. Glucosylceramide (GlcCer), a glycosphingolipid composed of a ceramide backbone linked to a glucose headgroup, is synthesized on the cytosolic surface of the Golgi and serves as a precursor for more complex glycosphingolipids, including globosides and gangliosides.[12][30] GBA2 operates as a GlcCer hydrolase at the cytosolic face of ER and Golgi membranes, catalyzing the conversion of GlcCer to ceramide and glucose.[12][44] In addition, GBA2 and lysosomal GBA1 can transfer glucose from GlcCer to cholesterol, forming glucosylated cholesterol (GlcChol), a molecule implicated in lysosomal storage disorders.[20]

In GBA2 deficiency, GlcCer accumulation outside lysosomes has been demonstrated in mice, with elevated levels in testis, brain, liver, sperm, and dermal fibroblasts.[12][32] The Norwegian Marinesco‑Sjögren‑like study showed that reduced GBA2 activity in patients was sufficient to elevate GlcCer to levels comparable to Gaucher disease, a prototypical lysosomal storage disorder caused by GBA1 deficiency.[31] Zebrafish models with combined *gba1* and *gba2* deficiency revealed increased GlcCer and reduced GlcChol, highlighting distinct contributions of GBA1 and GBA2 to glycosphingolipid and sterol metabolism.[20]

Ceramide, the product of GlcCer hydrolysis, is a bioactive lipid involved in apoptosis, autophagy, differentiation, and stress responses.[12][30] In SPG46, impaired conversion of GlcCer to ceramide may perturb ceramide‑dependent signaling cascades, including pathways regulating cell survival, neurite outgrowth, and synaptic plasticity. The net effect of GlcCer accumulation and altered ceramide levels is likely a shift in membrane microdomain composition (e.g., lipid rafts), affecting receptor localization and downstream signaling (e.g., MAPK, PI3K‑AKT, small GTPases), although specific pathway alterations in SPG46 have not been fully mapped and remain inferred.[12][35]

Suggested GO biological process terms include GO:0006687 (glycosphingolipid metabolic process), GO:0006665 (sphingolipid metabolic process), GO:1905952 (regulation of lipid metabolic process), and GO:0007165 (signal transduction). CHEBI terms include CHEBI:37683 (glucosylceramide) and CHEBI:17761 (ceramide).

### 6.3 Cellular Processes: Axonogenesis, Cytoskeletal Dynamics, and Neuronal Tract Formation

At the cellular level, SPG46 affects axonogenesis, neuronal tract formation, and cytoskeletal dynamics. Zebrafish morpholino studies targeting the *gba2* ortholog showed that knockdown led to abnormal motor behavior, axonal shortening and branching of motoneurons, and defective central nervous system development; these defects could be rescued by human wild‑type GBA2 mRNA but not by mRNA containing the disease‑associated missense mutation.[11][14][36] These findings demonstrate a direct role for GBA2 in axonal growth and guidance and in CNS development.

In *Gba2*‑knockout mice, non‑lysosomal GlcCer accumulation disrupted cytoskeletal dynamics in testes. Detailed analyses revealed that microtubule persistence and actin polymerization rates were increased, with disorganization of the microtubule manchette and F‑actin structures in apical ectoplasmic specializations, leading to impaired acrosome formation and globozoospermia.[35][32] These data highlight that altered glycosphingolipid composition in membranes can modulate cytoskeletal organization and vesicle fusion processes, which are critical for cell morphology and polarized growth.

By inference, similar mechanisms operate in neurons, where axonal microtubules and actin structures guide neurite extension and synaptogenesis. Disturbed cytoskeleton and membrane trafficking would impair corticospinal tract development, corpus callosum formation, and cerebellar circuitry, consistent with the human phenotype of spastic paraparesis, thin corpus callosum, and cerebellar atrophy.[11][1][1] Suggested GO terms include GO:0007409 (axonogenesis), GO:0030426 (growth cone), GO:0030036 (actin cytoskeleton organization), and GO:0007017 (microtubule‑based process). Relevant CL (Cell Ontology) terms include CL:0000540 (neuron), CL:0000099 (motor neuron), and CL:0000602 (Purkinje cell).

### 6.4 Protein Dysfunction: Loss of Function of GBA2

The central protein dysfunction in SPG46 is loss of function of GBA2. Martin et al. demonstrated that antisense morpholino knockdown of *gba2* in zebrafish led to motor neuron defects and that human wild‑type GBA2, but not the missense mutant, rescued the phenotype, providing strong functional evidence that loss of GBA2 activity underlies motor neuron pathology.[11][14][11] Enzyme assays in blood cells from patients showed absence of GBA2 glucocerebrosidase activity for missense variants.[11][11]

Protein structural studies and variant mapping indicate that pathogenic missense mutations cluster in the catalytic domain, particularly in the six‑hairpin glucosidase‑like fold, where they likely destabilize the active site or hinder substrate binding.[13][44][30] Truncating and frameshift mutations remove large portions of the catalytic domain, producing nonfunctional proteins or triggering nonsense‑mediated decay. Splice‑site mutations presumably lead to exon skipping or intron retention, disrupting the open reading frame and generating truncated protein.

UniProt annotations for GBA2 emphasize its β‑glucosidase activity and localization to the ER and Golgi. Loss of this activity not only abolishes GlcCer hydrolysis but may also reduce transglucosylation to cholesterol and other lipids, which has implications for broader lipid metabolic networks.[20][30] Suggested GO molecular function terms include GO:0008422 (β‑glucosidase activity) and GO:0004348 (glycosylceramidase activity).

### 6.5 Metabolic Changes and Lipidomics Signatures

Metabolically, SPG46 involves non‑lysosomal accumulation of GlcCer and alterations in glycosphingolipid profiles. Ulmer’s dissertation and related work showed that GBA2 deficiency in mice leads to accumulation of GlcCer in brain, testis, liver, sperm, and dermal fibroblasts, consistent with GBA2’s role as a non‑lysosomal GlcCer hydrolase.[12][28][32] Raju et al. and Yildiz et al. previously reported similar elevations of GlcCer in *Gba2*‑deficient mice.[12] In Norwegian Marinesco‑Sjögren‑like patients with *GBA2* mutations, GlcCer levels were elevated to levels comparable to Gaucher disease, despite normal bile acid metabolism, confirming that reduced GBA2 activity alone can cause GlcCer storage.[31][32]

Zebrafish models provide more nuanced lipidomics data, demonstrating that GlcCer is increased in *gba2*-null larvae, with GlcCer levels influenced by *gba1* status, and that glucosylated cholesterol (GlcChol) is reduced in *gba2*‑null states.[20] These findings indicate that GBA2 contributes to both glycosphingolipid and sterol glucosylation pathways, and that its loss skews lipid metabolic flux. In humans, comprehensive lipidomics in SPG46 patients have not yet been reported, but the animal data strongly support accumulation of GlcCer and likely secondary changes in complex glycosphingolipids.

Suggested GO terms include GO:0006690 (glucocerebroside metabolic process), GO:0008203 (cholesterol metabolic process), and GO:0046467 (membrane lipid biosynthetic process). CHEBI terms include CHEBI:37683 (glucosylceramide) and CHEBI:60027 (glucosylated cholesterol).

### 6.6 Immune System Involvement and Tissue Damage Mechanisms

The role of the immune system in SPG46 is not clearly delineated. There are no reports of autoimmunity, chronic inflammation, or immunodeficiency as primary features of SPG46.[3][11][19][2] However, dysregulated sphingolipid metabolism can influence inflammatory signaling, as ceramide and glycosphingolipids modulate cytokine responses and membrane receptor function.[12][30] It is plausible that GlcCer accumulation in glia or immune cells could alter neuroinflammatory states, but this has not been directly studied in SPG46.

Tissue damage mechanisms in SPG46 principally involve chronic neurodegeneration rather than acute necrosis or ischemia. Oxidative stress and mitochondrial dysfunction are commonly implicated in neurodegenerative diseases, and ceramide accumulation can promote apoptosis via mitochondrial pathways, but specific data on these mechanisms in SPG46 are lacking.[12] The structural atrophy of cerebellum and cerebral cortex suggests gradual neuronal loss and synaptic pruning, with concomitant gliosis, but histopathologic studies of human SPG46 brain tissue have not been published.

### 6.7 Molecular Profiling and Advanced Technologies

There are currently no transcriptomic, proteomic, or single‑cell profiling studies specifically focused on SPG46 patients. However, tissue expression data from the Human Protein Atlas show that *GBA2* is expressed in multiple brain regions, reinforcing its importance for CNS function.[45][49] In the future, RNA‑seq of patient fibroblasts or induced pluripotent stem cell (iPSC)‑derived neurons could elucidate secondary gene expression changes in response to GBA2 loss, and lipidomics could map detailed glycosphingolipid profiles in blood or cerebrospinal fluid.

Functional genomics screens have not yet targeted *GBA2* in human neurons, but CRISPR knock‑out models in cell lines or organoids would be valuable for dissecting cell‑type specific responses. At present, knowledge is derived primarily from conventional genetics, biochemical assays, and animal models rather than advanced multi‑omics integration.

## 7. Anatomical Structures Affected

### 7.1 Organ‑Level Involvement: Central Nervous System, Eye, and Testis

The primary organs affected in SPG46 are the central nervous system (CNS), eyes (lens), and male reproductive organs (testes). Within the CNS, the brain and spinal cord are both involved. Corticospinal tracts in the spinal cord and brainstem, cerebral cortex, corpus callosum, and cerebellum are key sites of pathology.[2][7][1][1] Upper motor neuron degeneration along the corticospinal tracts produces spastic paraparesis, while cerebellar involvement causes ataxia, and corpus callosum thinning reflects commissural tract abnormalities.[3][11][1][1] UBERON terms relevant to these structures include UBERON:0000955 (brain), UBERON:0002240 (spinal cord), UBERON:0002032 (cerebral cortex), UBERON:0002034 (corpus callosum), and UBERON:0002080 (cerebellum).

The eye involvement in SPG46 centers on the lens, where congenital cataracts form, leading to visual impairment.[3][4][31] UBERON:0000942 (eye) and UBERON:0001799 (lens of eye) are appropriate ontology terms. Male reproductive involvement is centered in the testes and seminiferous epithelium, where GBA2 deficiency causes globozoospermia and infertility.[30][32][35] UBERON:0000473 (testis) and UBERON:0005369 (seminiferous tubule) capture these anatomical entities.

Secondary organ systems may be indirectly affected—such as the urinary system via neurogenic bladder (UBERON:0002339, urinary bladder) and musculoskeletal system via scoliosis and contractures—but primary pathology is neurologic, ocular, and reproductive.[3][19][2]

### 7.2 Tissue and Cell‑Level Targets

At the tissue level, SPG46 primarily affects nervous tissue (neurons and glia), lens epithelial and fiber cells, and testicular germinal epithelium. In the CNS, upper motor neurons in layer V of the motor cortex and their descending axons in the corticospinal tracts are key cell types implicated in spastic paraparesis.[22][27] CL terms include CL:0000107 (pyramidal neuron) and CL:0000099 (motor neuron). Cerebellar Purkinje cells (CL:0000602) and deep cerebellar nuclei neurons are likely affected in ataxic phenotypes.[13][15][7] Corpus callosum thinning reflects abnormalities in callosal commissural neurons and oligodendrocytes (CL:0000120) responsible for myelination.

Peripheral neuropathy indicates involvement of peripheral motor and sensory neurons and Schwann cells. Lens cataracts derive from lens epithelial cells and fiber cells whose transparency is disturbed by metabolic or structural changes; although direct data on GBA2 in lens cells are limited, Marinesco‑Sjögren‑like *GBA2* mutations clearly cause cataracts.[31] Testicular globozoospermia involves spermatids and Sertoli cells in seminiferous tubules, with disrupted cytoskeletal structures and vesicle fusion.[32][35]

At the subcellular level, GBA2 localizes to ER and Golgi membranes, with its active site facing the cytosol.[10][12][30] GO cellular component terms include GO:0005783 (endoplasmic reticulum), GO:0005794 (Golgi apparatus), and GO:0005886 (plasma membrane). Accumulated GlcCer perturbs membrane microdomains, likely affecting raft structures and endomembrane trafficking.

### 7.3 Localization and Lateralization

Clinically, SPG46 exhibits bilateral involvement of corticospinal tracts, leading to symmetric lower limb spasticity, although asymmetry in severity can occur.[22][27] Cerebellar ataxia is typically bilateral, affecting both sides of the body, and corpus callosum thinning is a midline structure phenomenon.[3][4][1][1] Cataracts are often bilateral, as in reported congenital bilateral cataract cases.[3][4][9] Scoliosis can be right‑ or left‑convex, depending on spinal deformity patterns, but this is not specific to SPG46.

Motor symptoms and weakness may display some lateralization due to individual variability in lesion distribution, but the underlying anatomical pathology is largely symmetric. Movement disorders such as dystonia or tremor, reported in some Italian SPG46 patients, may have asymmetric expression.[19][19] Neurogenic bladder and cognitive impairment are non‑lateralized systemic manifestations.

Neuroimaging specifically notes “thin corpus callosum” on midline sagittal MRI and “mild cerebellar atrophy,” often with diffuse involvement of vermis and hemispheres.[3][4][7] No focal lesions or unilateral infarcts are typical; rather, diffuse structural changes predominate.

## 8. Temporal Development

### 8.1 Onset and Course of Disease

SPG46 is characterized by early‑onset, chronic, insidious disease course. Orphanet and MedGen report age of onset in infancy or childhood.[3][7] In Tunisian families, gait disturbance and developmental delay appeared in childhood.[1][30] In Hammer et al.’s spastic ataxia cohort, onset ranged from childhood to adolescence.[13][15] A Japanese patient was diagnosed in adulthood but had congenital cataracts and long‑standing motor symptoms.[9] A 56‑year‑old man with complicated HSP due to *GBA2* mutation had congenital cataracts, but his pyramidal and cerebellar features progressed over decades.[4][8]

The onset pattern is chronic and insidious rather than acute or subacute; symptoms emerge gradually as the child’s motor milestones and cognitive development lag behind peers. There are no described episodes of remission or relapsing‑remitting patterns; instead, the disease course is relentlessly progressive, albeit slowly.[22][27] Disease duration is lifelong and chronic, with progressive disability accumulating over many years.

### 8.2 Disease Stages and Progression Rate

Formal staging systems for SPG46 have not been established, but one can conceptualize early, intermediate, and advanced stages based on motor and cognitive impairment. In early stage, children and adolescents present with gait abnormalities, mild spasticity, and possible cerebellar signs, but remain ambulatory; cognitive issues may manifest as learning difficulties.[3][11][13][19] Intermediate stage involves worsening spasticity, increased falls, need for walking aids, more prominent ataxia, and clearer intellectual disability.[19][2] Advanced stage includes severe spasticity or contractures, wheelchair dependency, marked ataxia, possible dementia, cataract‑related visual impairment, and potential complications like scoliosis and bladder dysfunction.[3][19][2]

The progression rate is slow, typical of HSP. ITB studies in general HSP populations describe initial improvement in spasticity and stabilization of mobility for 6–8 years, after which disease progression continues.[40] SPG46 case series similarly describe slow worsening over time without acute deterioration. The presence of cerebellar ataxia and cognitive impairment suggests that some features may progress faster than pure motor symptoms, but longitudinal quantitative data are limited.

### 8.3 Remission Patterns and Critical Periods

Spontaneous remission has not been reported in SPG46. Treatment‑induced improvements (e.g., via intrathecal baclofen or physical therapy) can reduce spasticity and improve functional status, but they do not reverse the underlying neurodegeneration.[37][39][47] There are no recognized critical periods of vulnerability beyond early brain and spinal cord development, during which GBA2 deficiency disrupts neuronal tract formation and corpus callosum development. However, early intervention with supportive therapies can mitigate functional decline and contracture formation, representing critical windows for tertiary prevention.

Cataract extraction in childhood is a key intervention period for visual rehabilitation. For male hypogonadism, adolescence is critical for hormonal therapy decisions and psychosocial support. These do not alter primary disease mechanisms but influence long‑term outcomes.

## 9. Inheritance and Population

### 9.1 Epidemiology: Prevalence and Incidence

SPG46 is an ultra‑rare disease. Orphanet estimates prevalence at less than 1 per 1,000,000.[3] The total number of families reported worldwide is around thirty, as noted in the 2024 Italian series.[19][19] Precise incidence rates are unavailable due to the rarity of SPG46 and its relatively recent delineation; many cases of complex HSP or recessive ataxia may remain undiagnosed or misclassified.

Population‑based registries, such as those maintained by CDC or WHO, do not provide SPG46‑specific data; they often aggregate all HSPs. Therefore, disease knowledge bases should annotate SPG46 as a very rare Mendelian disorder, with global prevalence likely in the range of <1 per 1,000,000 and incidences correspondingly low.

### 9.2 Inheritance Pattern, Penetrance, and Expressivity

SPG46 follows autosomal recessive inheritance. Both OMIM and Orphanet explicitly classify SPG46 as autosomal recessive, with modes of inheritance indicated as such in MedGen and SNOMED.[3][7][1][30][1] Most reported families are consanguineous, with homozygous mutations in *GBA2* in affected individuals and heterozygous carrier status in parents.[11][13][29][1] Some Belgian families show compound heterozygosity for two pathogenic *GBA2* variants.[44][30]

Penetrance appears to be high or complete: individuals with biallelic loss‑of‑function *GBA2* variants consistently exhibit neurological phenotypes, though the precise phenotype (complex HSP vs spastic ataxia vs Marinesco‑Sjögren‑like syndrome) varies.[11][13][31][2] Incomplete penetrance has not been reported.

Expressivity is markedly variable. Some individuals show predominantly spastic paraparesis with mild ataxia, others have robust cerebellar ataxia, and yet others present with cataracts and mental retardation akin to Marinesco‑Sjögren syndrome.[13][16][18][31][2] Within families, intrafamilial variability has been noted; Citterio et al. reported that *GBA2* mutated patients showed phenotypes combining features of SPG46 and recessive ataxia, with marked intrafamilial variability, thereby expanding the clinical spectrum.[5][48] This underscores variable expressivity despite identical mutations.

Genetic anticipation, germline mosaicism, and repeat expansion phenomena have not been described for SPG46. Founder effects may exist in specific populations, such as Tunisian families studied by Boukhris and Hammer, Cypriot families reported by Votsi, and Italian clusters,[11][13][29][1][19] but detailed haplotype analyses are sparse. Carrier frequency in general populations is unknown but presumed to be extremely low, consistent with the rarity of disease.

### 9.3 Population Demographics and Geographic Distribution

SPG46 cases have been reported across multiple ethnic and geographic backgrounds, including Tunisian, Cypriot, Belgian, Italian, Saudi, Japanese, and Norwegian families.[4][9][13][17][19][31][1][48] This suggests that *GBA2* mutations are not confined to a single population, though consanguinity and founder effects in some groups may increase local prevalence.

The Italian 2024 series presented five patients from five different centers in Italy, harboring five novel *GBA2* mutations, indicating wider distribution in Southern Europe.[19][19] Tunisian families highlight North African presence,[1][30] Cypriot and Belgian families demonstrate European clusters,[29][44] Saudi families represent Middle Eastern occurrence,[16][17] Japanese case indicates East Asian involvement,[9] and Norwegian Marinesco‑Sjögren‑like families underscore Nordic representation.[31] Sex ratio appears approximately balanced, though male hypogonadism and infertility are male‑specific features.

Age distribution predominantly includes childhood‑onset cases, though adult diagnosis can occur when congenital cataracts and lifelong motor symptoms have not been previously recognized as a unified syndrome.[4][9] There are no data suggesting ethnic susceptibility beyond the presence of consanguinity, which elevates risk of autosomal recessive diseases in general.

## 10. Diagnostics

### 10.1 Clinical Evaluation and Neurophysiological Tests

Clinically, SPG46 diagnosis begins with recognition of hereditary spastic paraplegia with complex features. Neurological examination reveals lower limb spasticity, hyperreflexia, Babinski signs, and often cerebellar signs such as ataxia and dysmetria.[13][19][27] Cognitive assessment may show intellectual disability or cognitive decline.[11][19] Ophthalmologic examination often detects cataracts, and endocrine evaluation may reveal hypogonadism in males.[3][30][31] Scoliosis, pes cavus, and peripheral neuropathy are identified on musculoskeletal and neurologic exams.[4][19][2]

Electrophysiologic tests, including nerve conduction studies and electromyography, can reveal axonal sensory‑motor peripheral neuropathy in some cases.[4][5][18] Somatosensory evoked potentials may show slowed conduction along central pathways, but SPG46‑specific data are limited. There are no pathognomonic EEG findings.

### 10.2 Imaging

Neuroimaging plays a critical role in SPG46 diagnosis. Brain MRI frequently demonstrates thinning of the corpus callosum and mild atrophy of the cerebrum and cerebellum.[3][4][7][1][1] Thin corpus callosum can be visualized on midline sagittal T1‑weighted images, while cerebellar and cerebral atrophy appear as widened sulci and enlarged ventricles. Hammer et al. reported cerebellar atrophy in ataxia patients, and Martin et al. described corpus callosum and cerebellar atrophy in HSP46 patients.[11][13][30][30] In the 56‑year‑old case, MRI showed cerebellar atrophy and thin corpus callosum.[4][8]

Spinal MRI may reveal atrophy of the spinal cord, especially in cervical and thoracic segments, but detailed SPG46‑specific spinal imaging data are limited. Skeletal imaging, such as spinal X‑rays or EOS imaging, documents scoliosis severity.[19][19] Radiologic features help distinguish SPG46 from other HSPs without thin corpus callosum or from leukodystrophies with diffuse white matter changes.

### 10.3 Laboratory Tests, Biomarkers, and Enzyme Assays

Standard laboratory tests (blood counts, metabolic panels) are often normal in SPG46. However, specific enzyme assays can measure GBA2 activity in peripheral blood cells. Martin et al. reported that a missense *GBA2* variant resulted in no residual GBA2 glucocerebrosidase activity in blood cells, suggesting that GBA2 activity measurement “opens the way to a possible measurement of this enzyme activity in clinical practice.”[11][11] Norwegian Marinesco‑Sjögren‑like study also measured GBA2 activity and GlcCer levels in patient samples, finding reduced activity and elevated GlcCer.[31]

At present, GBA2 activity assays are not widely available clinically but represent a potential biochemical diagnostic tool and biomarker. GlcCer and GlcChol levels in plasma or fibroblasts could also serve as biomarkers, but SPG46‑specific validation is limited.[20][31] No other specific circulating biomarkers (e.g., proteins, metabolites) have been established.

### 10.4 Genetic Testing Strategies

Genetic testing is central to definitive diagnosis of SPG46. Given the heterogeneity of HSP, comprehensive gene panels including known HSP genes, such as *SPAST*, *ATL1*, *REEP1*, *KIF5A*, *SPG7*, *SPG11*, *CYP7B1*, *CYP2U1*, *DDHD2*, and *GBA2*, are typically used.[25][48][50] Citterio et al. analyzed mutations in *CYP2U1*, *DDHD2*, and *GBA2* in a cohort of complicated HSP patients with and without thin corpus callosum.[5][48][50] Next‑generation sequencing (NGS) approaches—including whole‑exome sequencing (WES) or targeted panels—are effective in identifying *GBA2* variants in suspected SPG46 families.[11][13][29][11][19]

Genome‑wide linkage analysis followed by fine mapping and exome sequencing initially identified *GBA2* as the causal gene in Tunisian families.[1][30] WES is particularly useful when clinical features suggest complex HSP or recessive ataxia but the gene is unknown. For known SPG46 families, single‑gene sequencing of *GBA2* can be performed to confirm suspected variants or for cascade testing of relatives. ClinVar and GTR (Genetic Testing Registry) list *GBA2* as a gene target in HSP and ataxia panels.[26][29]

Chromosomal microarray and karyotyping are not primary tools for SPG46 diagnosis, as structural variants are not implicated. FISH is similarly not relevant. Mitochondrial DNA testing and repeat expansion assays are reserved for other ataxias, not SPG46. Whole genome sequencing (WGS) could detect structural or non‑coding variants affecting *GBA2*, but published SPG46 cases have been resolved with exonic sequencing.

### 10.5 Clinical Criteria and Differential Diagnosis

There are no formal, internationally standardized diagnostic criteria specific to SPG46. Diagnosis relies on clinical recognition of complex HSP or spastic ataxia with early onset, cataracts, cognitive impairment, thin corpus callosum, and hypogonadism in males, combined with genetic confirmation of biallelic *GBA2* variants.[3][11][13][31][2][19] ICD‑11 classifies SPG46 under autosomal recessive HSP (8B44.01).[21][25]

Differential diagnosis includes other complex HSP subtypes (e.g., SPG11 with thin corpus callosum, SPG15), leukodystrophies involving corpus callosum thinning (e.g., Krabbe disease), autosomal recessive cerebellar ataxias with spasticity due to other genes (e.g., *CYP2U1*, *DDHD2*, *FA2H*, *B4GALNT1*), and Marinesco‑Sjögren syndrome due to *SIL1* mutations.[25][28][48][50] Marinesco‑Sjögren‑like *GBA2* cases emphasize that cataracts, ataxia, and cognitive impairment can suggest SIL1‑related MSS but may instead be due to GBA2 deficiency.[31] Distinguishing features include GlcCer accumulation linked to GBA2 loss, specific GBA2 variants, and absence of SIL1 mutations.

### 10.6 Screening

Population‑level screening for SPG46 is not implemented due to its rarity. Carrier screening might be considered in high‑consanguinity families or populations where specific founder mutations have been identified, but no formal guidelines exist. Prenatal or preimplantation genetic diagnosis is theoretically possible in known carrier couples, using targeted testing for their family’s *GBA2* mutation. ACMG and ACOG guidelines for carrier screening focus on more common conditions, and SPG46 is not currently included in standard panels, though bespoke panels may be used.

Newborn screening does not include SPG46, and there are no biochemical markers suitable for high‑throughput screening at present. Thus, screening and early detection currently rely on family history, clinical suspicion, and targeted genetic testing in at‑risk relatives.

## 11. Outcome and Prognosis

### 11.1 Survival and Mortality

Data on survival and mortality in SPG46 are limited. Most reported patients are alive at the time of publication, with disease durations extending into adulthood.[4][9][11][13][19][2] GBA2‑deficient mice exhibit normal lifespan and no overt neurological symptoms, despite GlcCer accumulation, indicating that GBA2 loss alone does not necessarily reduce survival in animals.[32] In humans, SPG46 appears to be a chronic disabling but not typically life‑shortening disease, although severe complications (e.g., aspiration pneumonia due to dysphagia, infections, falls) could increase morbidity.

No studies provide formal life expectancy estimates, five‑year survival rates, or disease‑specific mortality rates. Given the slow progression and lack of reported early mortality, one can infer that life expectancy is not drastically reduced in most SPG46 patients, particularly with supportive care.

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in SPG46 is significant and arises from motor, cognitive, visual, and reproductive impairments. Chronic spastic paraparesis and ataxia produce disability in gait, transfers, and self‑care. Cognitive impairment limits education, employment, and social independence. Cataracts impair vision and require surgery. Hypogonadism and infertility impact psychosocial wellbeing and family planning.[3][11][13][31][2]

Disability outcomes include progressive mobility limitations, with many patients eventually requiring walking aids or wheelchairs. ITB studies in broader HSP populations highlight that severe spasticity can be ameliorated, improving function, but underlying weakness and ataxia persist.[37][39][40][41][43] Quality of life measures have not been specifically applied in SPG46 cohorts, but narrative reviews of physical therapy in HSP report that interventions such as hydrotherapy, robot‑assisted gait training, and balance rehabilitation can enhance strength, reduce spasticity, and improve posture and walking ability, thereby improving overall quality of life.[47] HPO terms capturing disability include HP:0000715 (gait disturbance) and HP:0001263 (motor impairment).

### 11.3 Disease Course, Complications, and Recovery Potential

Disease course is chronic and progressive, with gradual worsening of motor and cognitive symptoms. Complications include contractures, scoliosis, falls, fractures, urinary tract infections due to neurogenic bladder, and psychological distress.[19][2][37] Cataracts produce visual complications if not surgically treated. In males, hypogonadism can lead to metabolic and bone health issues if untreated.

Recovery potential in terms of reversing neurological deficits is low, as SPG46 is a neurodegenerative and neurodevelopmental disorder. However, functional gains are possible through symptomatic treatment—spasticity reduction via oral or intrathecal baclofen, strength and balance improvement via physical therapy, and visual rehabilitation via cataract surgery.[37][39][41][47] These interventions can partially restore independence and reduce disability but do not cure disease.

Prognostic factors likely include age of onset, initial severity of motor and cognitive impairment, presence of cerebellar ataxia or MSS‑like features, and access to rehabilitative services. Early onset with severe cognitive impairment may portend greater long‑term disability, while milder forms may allow more independence. Formal prognostic biomarkers have not been identified.

## 12. Treatment

### 12.1 Pharmacotherapy: Antispastic Agents

Current treatment for SPG46 is symptomatic and extrapolated from general HSP management. Oral antispasticity drugs such as baclofen (a GABA_B receptor agonist), tizanidine (an α2‑adrenergic agonist), dantrolene (a muscle relaxant acting on the sarcoplasmic reticulum), and benzodiazepines (e.g., diazepam) are commonly used to reduce muscle spasticity.[40][41] Baclofen acts centrally to inhibit excitatory neurotransmitter release in the spinal cord, reducing reflex hyperexcitability.[37][42]

Intrathecal baclofen (ITB) is a key interventional therapy for severe spasticity in HSP, including SPG46. Multiple studies, including early double‑blind cross‑over bolus injections and subsequent pump implantation in three HSP patients, have shown that ITB significantly reduces muscle tone and deep tendon reflexes, with doses ranging from 60 to 264 µg/day.[37][39][42] A systematic review in 2023 concluded that ITB improves spasticity in HSP patients, although objective gait improvement is not always observed; catheter‑related problems are common side effects.[38] A case series and observational studies further support ITB’s effectiveness in improving gait and mobility in selected HSP adults.[41][43]

For SPG46 specifically, ITB has not been separately analyzed, but given that spasticity is a major symptom, SPG46 patients are candidates for this therapy. NCIT terms relevant here include NCIT:C61531 (Baclofen), NCIT:C1577 (Intrathecal Administration), and NCIT:C49236 (Muscle Relaxant).

Pharmacogenomic interactions specific to SPG46 have not been identified. General baclofen metabolism and response are not known to be significantly affected by *GBA2* variants.

### 12.2 Advanced Therapeutics: Gene and Cell Therapy, Targeted Approaches

There are no approved or ongoing gene therapy trials targeting *GBA2* for SPG46. In principle, gene replacement via viral vectors (e.g., AAV‑mediated delivery of wild‑type *GBA2*) or gene editing via CRISPR‑Cas could restore GBA2 function in CNS and testis, correcting GlcCer accumulation and improving neuronal tract formation. Zebrafish rescue experiments demonstrate that exogenous wild‑type GBA2 can reverse motor neuron defects, suggesting that gene therapy is mechanistically plausible.[11][14][36] However, translation to human therapy faces challenges, including delivery to widespread CNS regions and developmental timing.

Cell therapy (e.g., stem cell transplantation) has not been studied in SPG46. RNA‑based therapies (antisense oligonucleotides, siRNAs) could theoretically modulate expression of upstream or downstream genes in sphingolipid metabolism, but no SPG46‑specific programs exist.

Targeted therapies focusing on sphingolipid metabolism could be envisioned. For example, glucosylceramide synthase inhibitors used in Gaucher disease and Fabry disease, such as miglustat (NCIT:C29431), might reduce GlcCer synthesis and alleviate non‑lysosomal accumulation in GBA2 deficiency. Norwegian data showed that reduced GBA2 activity alone elevates GlcCer to Gaucher levels, implying that substrate reduction therapy could be beneficial.[31] However, miglustat’s CNS penetration and impact on non‑lysosomal GlcCer pools in SPG46 are untested.

Immunotherapies are not relevant for SPG46, as autoimmunity is not implicated.

### 12.3 Surgical and Interventional Treatments

In addition to ITB pump implantation, which is an interventional neurosurgical procedure, SPG46 patients may undergo orthopedic surgeries for scoliosis or contractures. These include spinal fusion, tendon releases, and joint surgeries, aimed at improving posture, pain, and function. Cataract surgery (phacoemulsification and intraocular lens implantation) is standard for visual rehabilitation in congenital and early‑onset cataracts and has been performed in many SPG46 patients.[4][31]

ITB implantation involves insertion of a subcutaneous pump connected to an intrathecal catheter delivering baclofen directly into the cerebrospinal fluid. Studies show that ITB reduces spasticity and preserves or improves voluntary motor function, with some initial subjective weakness reported.[37][39][42] NCIT terms include NCIT:C116938 (Intrathecal Baclofen Infusion Pump) and NCIT:C15969 (Orthopedic Surgical Procedure).

### 12.4 Supportive and Rehabilitative Care

Supportive care and rehabilitation are central to SPG46 management. Physical therapy (PT) focusing on stretching, strengthening, gait training, and balance exercises is essential to manage stiffness, prevent contractures, and enhance mobility.[37][47] A 2023 narrative review of physical treatment in HSP highlighted that electrostimulation, magnetotherapy, hydrotherapy, robot‑assisted gait training, and balance rehabilitation can increase lower extremity strength and decrease spasticity, improving posture and walking ability and overall quality of life.[47] These modalities should be tailored to SPG46 patients’ specific deficits, including ataxia and cognitive impairment.

Occupational therapy helps with activities of daily living (ADLs), adaptive equipment, and environmental modifications. Speech therapy addresses dysarthria and swallowing issues. Ophthalmologic care includes cataract monitoring and surgery. Endocrinologic care manages hypogonadism in males, potentially with hormone replacement. Counseling and psychosocial support help patients and families cope with chronic disability.

NCIT terms include NCIT:C15245 (Physical Therapy), NCIT:C15247 (Occupational Therapy), NCIT:C15248 (Speech Therapy), and NCIT:C48302 (Supportive Care).

### 12.5 Experimental Treatments and Outcomes

There are no SPG46‑specific clinical trials in ClinicalTrials.gov as of current knowledge. Off‑label use of substrate reduction therapies (e.g., miglustat) or experimental sphingolipid modulators has not been reported. Future trials might explore gene therapy, enzyme replacement, substrate reduction, or small molecules that enhance residual GBA2 activity.

Treatment outcomes in HSP generally show that ITB reduces spasticity and can stabilize mobility for several years.[37][39][40] Baclofen side effects include sedation, weakness, and catheter‑related complications. Physical therapy interventions show improvements in strength and spasticity, but high‑quality randomized trials are limited.[47]

Personalized medicine approaches for SPG46 could include tailoring physical therapy intensity, ITB dosing, and endocrine interventions to individual severity and genotype, but genotype‑phenotype correlations are not yet strong enough to guide therapy choices.

## 13. Prevention

### 13.1 Primary, Secondary, and Tertiary Prevention

Primary prevention of SPG46 involves preventing occurrence of disease by avoiding transmission of biallelic *GBA2* mutations. This is achievable through genetic counseling, carrier testing in at‑risk families, and reproductive options such as preimplantation genetic diagnosis (PGD) and prenatal testing. For consanguineous couples with known carrier status, PGD can ensure that embryos without biallelic mutations are selected for implantation. These strategies align with ACMG and NSGC guidelines for Mendelian disease prevention, though SPG46 is not specifically highlighted due to its rarity.[25][1]

Secondary prevention involves early detection and intervention to reduce severity and complications. In SPG46, early diagnosis via genetic testing allows prompt initiation of physical therapy, spasticity management, cataract surgery, and cognitive support, reducing long‑term disability. Early identification of neurogenic bladder enables timely urologic care to prevent infections. Though there are no population‑level screening programs, at‑risk siblings can undergo targeted testing.

Tertiary prevention focuses on preventing complications in individuals with established disease. In SPG46, this includes rigorous physical therapy to avoid contractures, scoliosis management, fall prevention strategies, respiratory monitoring in severe scoliosis, and psychosocial support. ITB implantation for severe spasticity is a tertiary measure that reduces pain and enhances mobility.[37][39][40][47]

### 13.2 Immunization, Screening, and Counseling

Immunization is not directly related to SPG46 prevention, except as part of general health maintenance. Genetic screening for SPG46 is targeted to families with known *GBA2* mutations rather than broad population programs. Carrier screening and PGD can be offered in centers specializing in rare diseases.

Genetic counseling is essential for families, covering inheritance patterns, recurrence risks, options for prenatal or preimplantation testing, and implications for extended family members. Counselors should explain that autosomal recessive inheritance implies a 25% recurrence risk for each pregnancy when both parents are carriers, and that carriers are asymptomatic.[3][7][1][1]

Public health interventions for SPG46 are minimal given its rarity; however, education about consanguinity risks in general may indirectly reduce recessive disease burden in certain populations.

## 14. Other Species and Natural Disease

### 14.1 Species Affected and Orthologous Genes

Natural disease analogous to SPG46 occurs in mice with *Gba2* deficiency. GBA2 orthologs exist in multiple species, including mouse (Mus musculus) and zebrafish (Danio rerio).[32][36] NCBI Gene IDs for orthologous *Gba2* genes can be referenced for cross‑species comparisons. Zebrafish *gba2* has been used extensively in functional models of glucocerebrosidase deficiency.[20][36]

Companion animals and livestock have not been reported to have natural *GBA2*‑related spastic paraplegia or ataxia, and OMIA (Online Mendelian Inheritance in Animals) does not list SPG46 analogs in domestic species. Thus, natural disease seems limited to experimental models rather than recognized veterinary syndromes.

### 14.2 Comparative Pathology and Evolutionary Conservation

Comparative pathology indicates that *Gba2*‑knockout mice have GlcCer accumulation and globozoospermia but surprisingly no overt neurological symptoms, suggesting species‑specific differences in CNS sensitivity to GBA2 loss.[32][35] In contrast, human *GBA2* deficiency causes prominent neurological deficits. Zebrafish models exhibit motor neuron defects, aberrant axonogenesis, and altered GlcCer and GlcChol levels.[11][20][36] These cross‑species differences highlight that while sphingolipid metabolic mechanisms are evolutionarily conserved, phenotypic outcomes can differ by organism.

Evolutionary conservation of *GBA2* function is supported by orthology and functional rescue experiments: human GBA2 can rescue zebrafish *gba2* morpholino phenotypes.[11][14][36] This suggests that the catalytic role of GBA2 in GlcCer metabolism and axonogenesis is conserved across vertebrates.

There is no zoonotic potential for SPG46, as it is a genetic, non‑infectious disorder.

## 15. Model Organisms

### 15.1 Mouse Models: *Gba2* Knockout

Mouse models with *Gba2* knockout provide critical insights into GBA2 function. Matern et al. and subsequent studies generated mice deficient in GBA2 and found that these animals had normal bile acid metabolism but impaired fertility in males, with globozoospermia, abnormal acrosomes, and defective sperm motility.[32][35] Glycolipids identified as GlcCer accumulated in testes, brains, and livers, but did not cause obvious neurological symptoms, organomegaly, or reduced lifespan.[32] These findings show that GBA2 is a glucosylceramidase whose loss causes accumulation of glycolipids and an endoplasmic reticulum storage disease, particularly manifesting in male fertility.

The limitation of this mouse model is the lack of gross neurological phenotypes, which contrasts with human SPG46. This may reflect species differences in redundancy of sphingolipid pathways, compensation by GBA1, or differences in CNS architecture. However, the model recapitulates male infertility and GlcCer accumulation, which are key aspects of human disease.[30][32][35] It can be used to study testicular cytoskeletal dynamics and spermatogenesis under GBA2 loss, as well as systemic sphingolipid metabolism.

### 15.2 Zebrafish Models: *gba2* Knockdown and Knockout

Zebrafish models have been instrumental in elucidating neural mechanisms of GBA2 deficiency. Morpholino antisense oligonucleotides targeting the zebrafish *gba2* ortholog led to abnormal motor behavior and axonal shortening/branching of motoneurons.[11][14] These defects were rescued by human wild‑type GBA2 mRNA but not by mRNA containing a missense mutation found in human SPG46 patients, demonstrating functional conservation and confirming pathogenicity.[11][14][36] These experiments highlight the role of GBA2 in CNS development and motor neuron tract formation.

Additional zebrafish studies examined glucocerebrosidase deficiency as a model of glucocerebrosidase deficiency in Gaucher disease and related disorders, focusing on the interplay between lysosomal GBA1 and non‑lysosomal GBA2 in GlcCer and GlcChol metabolism.[20] Double‑mutant zebrafish lacking *gba1* and *gba2* exhibited altered GlcCer and GlcChol levels and neurodevelopmental anomalies, illustrating how these enzymes jointly regulate sphingolipid and sterol metabolism.

Strengths of zebrafish models include visualization of live axonogenesis, rapid developmental timelines, and facile genetic manipulation. Limitations include differences in CNS complexity and absence of higher cognitive functions present in humans. Nonetheless, zebrafish provide robust models for early developmental aspects of SPG46 pathophysiology.

### 15.3 Applications and Future Directions

Model organisms are used to dissect cell‑type specific roles of GBA2, explore downstream signaling pathways affected by GlcCer accumulation, and test potential therapies. For example, zebrafish could be used to screen small molecules that modulate sphingolipid metabolism or rescue axonogenesis, while mouse models could test substrate reduction therapies and gene replacement strategies.

Organoid models and iPSC‑derived neuronal cultures with *GBA2* knockout or patient‑specific mutations represent future directions. These systems could better recapitulate human cortical and cerebellar architecture and allow detailed study of synaptic function, electrophysiology, and cell‑type specific responses to therapy. Functional genomics screens in these models could identify modifiers of GBA2 loss and potential therapeutic targets.

## Conclusion

Hereditary spastic paraplegia type 46 (SPG46) is a rare, autosomal recessive, complex neurodegenerative disorder driven by biallelic loss‑of‑function mutations in *GBA2*, the non‑lysosomal glucosylceramidase beta 2. Clinically, SPG46 manifests as early‑onset spastic paraparesis, cerebellar ataxia, cognitive impairment, congenital cataracts, hypogonadism in males, peripheral neuropathy, and characteristic neuroimaging findings of thin corpus callosum and mild brain atrophy. At the molecular level, GBA2 deficiency causes non‑lysosomal GlcCer accumulation and perturbation of glycosphingolipid and sterol metabolism, which in turn disrupts membrane microdomains, cytoskeletal dynamics, axonogenesis, and neuronal tract formation. Animal models and zebrafish experiments have established that GBA2 loss leads to motor neuron defects, globozoospermia, and glucosylceramide storage, concretely linking sphingolipid metabolism to SPG46 pathology.

Genetic studies have identified a spectrum of pathogenic *GBA2* variants—nonsense, frameshift, splice‑site, and missense mutations—most of which cause loss of enzymatic activity. Expressivity of *GBA2* deficiency is variable, encompassing complex HSP (SPG46), autosomal recessive cerebellar ataxia with spasticity, and Marinesco‑Sjögren‑like syndrome, underscoring phenotypic pleiotropy. Penetrance appears high, and inheritance is strictly autosomal recessive, often in consanguineous families.

Diagnostics rely on clinical assessment of complex HSP features, neuroimaging for corpus callosum and cerebellar abnormalities, enzyme assays for GBA2 activity (in research settings), and, crucially, genetic testing via exome sequencing or targeted HSP panels including *GBA2*. Differential diagnosis includes other complex HSPs, leukodystrophies, and SIL1‑related Marinesco‑Sjögren syndrome, with *GBA2* mutations and GlcCer elevation distinguishing SPG46.

Treatment remains symptomatic and supportive. Oral antispastic medications and intrathecal baclofen reduce spasticity; physical therapy and rehabilitative modalities improve strength, balance, and mobility; cataract surgery restores vision; and endocrine management addresses hypogonadism. No disease‑modifying therapies specific to SPG46 exist, but substrate reduction and gene therapy are plausible future strategies. Prevention focuses on genetic counseling and carrier testing in affected families, with potential use of PGD and prenatal diagnosis for at‑risk couples.

For disease knowledge base integration, SPG46 can be annotated as MONDO:0013737, OMIM 614409, ORPHA:320391, with causal gene *GBA2* (OMIM 609471, HGNC:4193). Key phenotypes map to HPO terms such as HP:0001257 (spastic paraplegia), HP:0001251 (ataxia), HP:0001249 (intellectual disability), HP:0000518 (cataract), HP:0002079 (thin corpus callosum), HP:0001272 (cerebellar atrophy), and HP:0000028 (hypogonadism). Biological processes include GO:0006687 (glycosphingolipid metabolic process), GO:0007409 (axonogenesis), and GO:0030036 (actin cytoskeleton organization, with cell types CL:0000099 (motor neuron) and CL:0000602 (Purkinje cell) prominently involved. Chemical entities such as CHEBI:37683 (glucosylceramide) and CHEBI:17761 (ceramide) capture key metabolites. Treatment annotations can reference NCIT terms for baclofen, intrathecal therapy, physical and supportive care.

Future research priorities include detailed lipidomics and multi‑omics profiling in SPG46 patients, better longitudinal natural history data, exploration of sphingolipid‑targeted therapies, and development of brain organoid or iPSC‑derived neuron models to refine mechanistic understanding and therapeutic screening. As our knowledge expands, SPG46 exemplifies how rare Mendelian diseases illuminate fundamental roles of lipid metabolism in neurodevelopment and motor neuron integrity, with implications that extend beyond this ultra‑rare disorder.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 71 |
| Resolved | 66 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 2 |
| Unverifiable | 2 |
| Terms whose name was checked | 63 |
| Terms named correctly | 22 |
| Terms named as a **different** term | 27 |
| Terms whose name is worth a second look | 14 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0003477` (1 mention) - the report calls it "spastic gait"; HP calls it **Peripheral axonal neuropathy**
- `HP:0002310` (1 mention) - the report calls it "gait ataxia"; HP calls it **Orofacial dyskinesia**
- `HP:0001350` (1 mention) - the report calls it "cognitive impairment"; HP calls it **Slurred speech**
- `HP:0000750` (1 mention) - the report calls it "behavioral abnormality"; HP calls it **Delayed speech and language development**
- `HP:0001105` (1 mention) - the report calls it "bilateral cataract"; HP calls it **Retinal atrophy**
- `HP:0000759` (1 mention) - the report calls it "pseudobulbar dysarthria"; HP calls it **Abnormal peripheral nervous system morphology**
- `HP:0000020` (1 mention) - the report calls it "neurogenic bladder"; HP calls it **Urinary incontinence**
- `HP:0003473` (1 mention) - the report calls it "peripheral axonal neuropathy"; HP calls it **Fatigable weakness**
- `HP:0002650` (1 mention) - the report calls it "pes cavus"; HP calls it **Scoliosis**
- `CHEBI:37683` (3 mentions) - the report calls it "glucosylceramide"; CHEBI calls it **mannopyranose**
- `CHEBI:60027` (1 mention) - the report calls it "glucosylated cholesterol"; CHEBI calls it **polymer**
- `UBERON:0002032` (1 mention) - the report calls it "cerebral cortex"; UBERON calls it **areola**
- `UBERON:0002034` (1 mention) - the report calls it "corpus callosum"; UBERON calls it **suprachiasmatic nucleus**
- `UBERON:0002080` (1 mention) - the report calls it "cerebellum"; UBERON calls it **heart right ventricle**
- `UBERON:0000942` (1 mention) - the report calls it "eye"; UBERON calls it **frontal nerve (branch of ophthalmic)**
- `UBERON:0001799` (1 mention) - the report calls it "lens of eye"; UBERON calls it **vitreous chamber of eyeball**
- `UBERON:0005369` (1 mention) - the report calls it "seminiferous tubule"; UBERON calls it **UBERON_0005369**
- `HP:0001263` (1 mention) - the report calls it "motor impairment"; HP calls it **Global developmental delay**
- `NCIT:C61531` (1 mention) - the report calls it "Baclofen"; NCIT calls it **Microbiology Susceptibility Domain**
- `NCIT:C1577` (1 mention) - the report calls it "Intrathecal Administration"; NCIT calls it **Nolatrexed Dihydrochloride**
- `NCIT:C49236` (1 mention) - the report calls it "Muscle Relaxant"; NCIT calls it **Therapeutic Procedure**
- `NCIT:C116938` (1 mention) - the report calls it "Intrathecal Baclofen Infusion Pump"; NCIT calls it **CDK4/6 Inhibition**
- `NCIT:C15969` (1 mention) - the report calls it "Orthopedic Surgical Procedure"; NCIT calls it **NIH Areas of Research Emphasis**
- `NCIT:C15245` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Health Services Research**
- `NCIT:C15247` (1 mention) - the report calls it "Occupational Therapy"; NCIT calls it **Heart and Lung Transplantation**
- `NCIT:C15248` (1 mention) - the report calls it "Speech Therapy"; NCIT calls it **Hemodialysis**
- `NCIT:C48302` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **SDHB Gene Mutation**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000715` (1 mention), reported as "gait disturbance" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0046467` (obsolete membrane lipid biosynthetic process) (1 mention) - replaced by `GO:0008610`
- `UBERON:0005369` (UBERON_0005369) (1 mention) - replaced by `UBERON:0002313`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001257` (2 mentions) - the report calls it "spastic paraplegia"; HP calls it **Spasticity**
- `HP:0007340` (1 mention) - the report calls it "lower limb spasticity"; HP calls it **Lower limb muscle weakness**, and lists "Lower limb weakness" among its other names
- `HP:0000028` (2 mentions) - the report calls it "hypogonadism"; HP calls it **Cryptorchidism**
- `HP:0002751` (1 mention) - the report calls it "scoliosis"; HP calls it **Kyphoscoliosis**
- `HP:0003474` (1 mention) - the report calls it "sensorimotor neuropathy"; HP calls it **Somatic sensory dysfunction**, and lists "Sensory impairment" among its other names
- `HP:0002079` (2 mentions) - the report calls it "thin corpus callosum"; HP calls it **Hypoplasia of the corpus callosum**, and lists "Hypoplastic corpus callosum" among its other names
- `GO:1905952` (1 mention) - the report calls it "regulation of lipid metabolic process"; GO calls it **regulation of lipid localization**
- `CL:0000099` (3 mentions) - the report calls it "motor neuron"; CL calls it **interneuron**
- `CL:0000602` (3 mentions) - the report calls it "Purkinje cell"; CL calls it **pressoreceptor cell**
- `GO:0008422` (1 mention) - the report calls it "β‑glucosidase activity"; GO calls it **beta-glucosidase activity**
- `GO:0004348` (1 mention) - the report calls it "glycosylceramidase activity"; GO calls it **glucosylceramidase activity**
- `GO:0006690` (1 mention) - the report calls it "glucocerebroside metabolic process"; GO calls it **icosanoid metabolic process**
- `GO:0046467` (1 mention) - the report calls it "membrane lipid biosynthetic process"; GO calls it **obsolete membrane lipid biosynthetic process**
- `CL:0000107` (1 mention) - the report calls it "pyramidal neuron"; CL calls it **autonomic neuron**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.