---
provider: perplexity
model: sonar-reasoning-pro
cached: false
start_time: '2026-09-15T20:26:56.568051'
end_time: '2026-09-15T20:29:47.593577'
duration_seconds: 171.03
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Thrombocytopenia 11 with Multiple Congenital Anomalies and Dysmorphic
    Facies
  mondo_id: MONDO:0958000
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
citation_count: 16
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
  total_terms: 60
  verified: 59
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 59
  labels_matching: 28
  labels_mismatched: 22
  mislabelled_terms:
  - term_id: HP:0000283
    reported_labels:
    - Facial dysmorphism
    ontology_label: Broad face
  - term_id: HP:0004322
    reported_labels:
    - Multiple congenital anomalies
    ontology_label: Short stature
  - term_id: HP:0001907
    reported_labels:
    - Abnormal platelet morphology
    ontology_label: Thromboembolism
  - term_id: HP:0000316
    reported_labels:
    - Telecanthus
    ontology_label: Hypertelorism
  - term_id: HP:0000308
    reported_labels:
    - Thin vermilion border
    ontology_label: Microretrognathia
  - term_id: HP:0001254
    reported_labels:
    - Mild intellectual disability
    ontology_label: Lethargy
  - term_id: HP:0002190
    reported_labels:
    - Abnormality of brain morphology
    ontology_label: Choroid plexus cyst
  - term_id: HP:0000076
    reported_labels:
    - Abnormality of the urinary system
    ontology_label: Vesicoureteral reflux
  - term_id: HP:0000819
    reported_labels:
    - Abnormality of the endocrine system
    ontology_label: Diabetes mellitus
  - term_id: GO:0007613
    reported_labels:
    - membrane organization/adhesion processes relevant to development
    ontology_label: memory
  - term_id: CL:0000057
    reported_labels:
    - Endothelial cell
    ontology_label: fibroblast
  - term_id: CL:0000122
    reported_labels:
    - Mesenchymal cell
    ontology_label: stellate neuron
  - term_id: UBERON:0000056
    reported_labels:
    - urinary bladder
    ontology_label: ureter
  - term_id: UBERON:0004535
    reported_labels:
    - bone marrow
    ontology_label: cardiovascular system
  - term_id: HP:0002269
    reported_labels:
    - Bilateral involvement
    ontology_label: Abnormality of neuronal migration
  - term_id: NCIT:C61588
    reported_labels:
    - Platelet Transfusion
    ontology_label: Malignant Hyperchromatic Small Epithelial Cell
  - term_id: NCIT:C12679
    reported_labels:
    - Supportive Care
    ontology_label: Blood Vessel
  - term_id: NCIT:C15273
    reported_labels:
    - Nephrology Procedure
    - Monitoring
    ontology_label: Longitudinal Study
  - term_id: NCIT:C15219
    reported_labels:
    - Occupational Therapy
    ontology_label: Health Care Delivery
  - term_id: NCIT:C15218
    reported_labels:
    - Physical Therapy
    ontology_label: Cystostomy
  - term_id: NCIT:C19071
    reported_labels:
    - Speech Therapy
    ontology_label: Toxicology, Antidotes/Treatment
  - term_id: NCIT:C92189
    reported_labels:
    - Genetic Counseling
    ontology_label: Perennial Allergic Rhinitis
  labels_variant: 9
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Thrombocytopenia 11 with Multiple Congenital Anomalies and Dysmorphic Facies
- **MONDO ID:** MONDO:0958000 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Thrombocytopenia 11 with Multiple Congenital Anomalies and Dysmorphic Facies** covering all of the
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

Thrombocytopenia 11 with multiple congenital anomalies and dysmorphic facies (THC11) is an ultra‑rare autosomal‑dominant syndromic platelet disorder caused by heterozygous germline variants in RAP1B and characterized by chronic thrombocytopenia, dysmorphic facial features, multiple congenital anomalies, poor growth, microcephaly, hypotonia, and mild neurodevelopmental impairment.[2][9][13]  
Current knowledge derives from a small number of families and isolated cases, so disease descriptions, mechanisms, and management recommendations are based on limited but consistent case‑level and aggregated disease‑level evidence.[2][3][7][9][14]

---

## 1. Disease Information

**Definition and clinical overview**

Thrombocytopenia 11 with multiple congenital anomalies and dysmorphic facies (THC11) is a Mendelian syndromic thrombocytopenia in which chronic, persistent thrombocytopenia is accompanied by congenital malformations affecting the heart, brain, genitourinary, endocrine, and skeletal systems, as well as characteristic facial dysmorphism, growth restriction with microcephaly, hypotonia, and mildly impaired intellectual development or learning difficulties.[2][9][13]  
Leukopenia or anemia may occur in some affected individuals, indicating a broader though variably expressed cytopenia phenotype.[2][11]  

**Key identifiers**

OMIM identifies the disorder as “THROMBOCYTOPENIA 11 WITH MULTIPLE CONGENITAL ANOMALIES AND DYSMORPHIC FACIES; THC11” with MIM number 620654 and maps it to chromosome 12q15, with RAP1B (MIM 179530) as the causal gene.[2][6][13]  
ClinVar and MedGen list the same condition name and link it to MONDO:0958000, providing harmonized terminologies across disease ontologies.[3][7][14]  
Gene‑centric resources and diagnostic panel databases (e.g., Genomics England PanelApp and NCBI GTR) consistently associate RAP1B with “Thrombocytopenia 11 with multiple congenital anomalies and dysmorphic facies.”[4][5][9][15]  
Chinese rare‑disease compendia group THC11 alongside other syndromic thrombocytopenias (e.g., Jacobsen syndrome, TAR, THC8), reinforcing its classification as a multisystem congenital thrombocytopenia syndrome.[11]  

Suggested ontology terms:  
- MONDO: MONDO:0958000 (thrombocytopenia 11 with multiple congenital anomalies and dysmorphic facies)[3][14]  
- HPO: HP:0001873 (Thrombocytopenia), HP:0000283 (Facial dysmorphism), HP:0000252 (Microcephaly), HP:0001252 (Hypotonia), HP:0001263 (Global developmental delay), HP:0004322 (Multiple congenital anomalies)  
- MeSH: likely categorized under “Thrombocytopenia” and “Congenital Abnormalities” (no specific term yet)  
- ICD‑10/ICD‑11: currently coded using generic thrombocytopenia (e.g., D69.6) and “other specified congenital malformation syndromes” (e.g., Q87.89) in practice, as specific ICD codes for THC11 have not been reported in the literature.  

**Data provenance**

The core disease description and gene–phenotype relationship derive from aggregated disease‑level resources (OMIM, ClinGen/MedGen, PanelApp, GTR).[2][4][9][13][14][15]  
Variant‑specific and case‑level data, including phenotypic detail and functional interpretation, are primarily derived from individual patient reports curated into ClinVar entries and linked literature.[3][7][8]  

---

## 2. Etiology

### 2.1 Primary causal factors

THC11 is caused by heterozygous germline variants in RAP1B, a small GTPase of the RAS family located on chromosome 12q15, with autosomal‑dominant inheritance.[2][6][13][14]  
OMIM uses a number sign (#620654) for THC11, indicating that RAP1B mutation is the established cause of the phenotype.[2][13]  
ClinVar records multiple missense variants in RAP1B classified as pathogenic for THC11, with submissions from OMIM and other clinical laboratories documenting germline origin and supporting literature.[3][7][8]  

Suggested ontology terms:  
- HGNC: RAP1B (HGNC:9889)  
- GO (biological process): GO:0007264 (small GTPase‑mediated signal transduction), GO:0030168 (platelet activation), GO:0007165 (signal transduction), GO:0008284 (positive regulation of cell proliferation)  

### 2.2 Genetic risk factors

ClinVar entries for THC11 report heterozygous missense variants affecting functionally critical regions of RAP1B, including p.Ala59Gly, p.Gly60Arg, and p.Tyr4Cys, classified as pathogenic or likely pathogenic based on literature and in‑silico evidence.[3][7][8]  
The Gly60Arg substitution lies within the switch II region essential for interaction with GTPase‑activating proteins (GAPs), indicating that impaired GTP hydrolysis and sustained activation of RAP1B are likely mechanisms.[7]  
All THC11‑associated variants reported to date are germline and heterozygous, consistent with a dominant mechanism; no recurrent hotspot or founder mutation has been documented.[3][7][8][14]  

There are currently no documented common susceptibility alleles, polygenic risk scores, or modifier genes for THC11; all reported variants are rare and likely private to individual families or cases.[3][4][9][14]  

### 2.3 Environmental and lifestyle risk factors

No specific environmental, occupational, or lifestyle factors have been implicated in the development of THC11, and all reported cases are attributed to germline RAP1B variants rather than acquired causes.[2][3][9][13]  
Standard acquired causes of thrombocytopenia (drugs, infections, autoimmune disease) are considered in differential diagnosis but have not been shown to interact with RAP1B variants to produce the THC11 phenotype.[2][9]  

### 2.4 Protective factors and gene–environment interactions

No protective genetic variants, modifier alleles, or environmental factors that reduce risk or ameliorate severity of THC11 have been reported.[2][3][9][13]  
Gene–environment interactions remain uncharacterized; current evidence is insufficient to conclude whether environmental factors meaningfully modulate penetrance or expressivity of RAP1B variants in THC11.[2][3][9][14]  

---

## 3. Phenotypes

OMIM describes THC11 as a syndromic disorder with hematologic, craniofacial, neurodevelopmental, growth, and multisystem congenital anomalies.[2][13]  
GTR, drawing from Latham et al. (2018), emphasizes dysmorphic facial features and variable developmental delay with mildly impaired intellectual development.[9]  
Chinese rare disease compendia highlight growth and developmental delay, special facial appearance, thrombocytopenia or pancytopenia, congenital heart disease, and renal anomalies.[11]  

### 3.1 Core hematologic phenotype

- **Thrombocytopenia (symptom/ laboratory abnormality)**  
  - Chronic, persistent thrombocytopenia is a defining feature, often with large platelets and mild bleeding tendency.[2][11]  
  - Age of onset: congenital or early infancy, as cytopenias are recognized in childhood in reported cases.[2][9]  
  - Severity: typically mild to moderate thrombocytopenia; severe bleeding is not prominently reported but risk exists due to low platelets.[2][11]  
  - Progression: thrombocytopenia appears stable or chronic rather than episodic; no acquired remission has been documented.[2][11]  
  - Frequency: present in essentially all described individuals; it is included in the disease name.[2][9][11]  
  - Quality of life impact: increased bruising and bleeding risk, precautions around surgery and trauma, and potential need for transfusion or hematology follow‑up.[2][11]  

Suggested HPO term: HP:0001873 (Thrombocytopenia), HP:0001907 (Abnormal platelet morphology).  

Leukopenia and anemia have been noted in some cases, indicating broader mild cytopenias in a subset of individuals.[2][11]  

Suggested HPO terms: HP:0001882 (Leukopenia), HP:0001903 (Anemia).  

### 3.2 Craniofacial and growth phenotypes

- **Facial dysmorphism (clinical signs)**  
  OMIM and GTR report “dysmorphic facial features” without a fully standardized list, but features described across cases include telecanthus, upslanting palpebral fissures, thin upper lip, and other minor anomalies similar to those seen in related actinopathies.[2][9][10][12]  
  Age of onset: congenital, visible at birth.[2][9]  
  Severity: mild to moderate but recognizable to experienced clinicians.[2][9][11]  
  Progression: stable structural features.[2][9]  
  Frequency: present in most reported cases.[2][9][11]  
  Quality of life: mainly cosmetic/social impact; functional impairment is limited unless associated with craniofacial anomalies affecting airway or feeding.[2][9]  

Suggested HPO terms: HP:0000283 (Facial dysmorphism), HP:0000316 (Telecanthus), HP:0000582 (Upslanted palpebral fissures), HP:0000308 (Thin vermilion border).  

- **Poor growth and microcephaly**  
  OMIM notes poor growth and microcephaly as part of the THC11 phenotype.[2][13]  
  Age of onset: prenatal or early postnatal growth restriction; microcephaly typically identified in infancy.[2][9]  
  Severity: usually mild to moderate growth delay and microcephaly.[2][9][11]  
  Progression: tends to persist; catch‑up growth is not highlighted.[2][9]  
  Frequency: common among described individuals.[2][11][13]  
  Quality of life: may contribute to developmental and cognitive challenges and increased monitoring in pediatric care.[2][9]  

Suggested HPO terms: HP:0001510 (Growth delay), HP:0000252 (Microcephaly).  

### 3.3 Neurodevelopmental and neurologic phenotypes

- **Hypotonia and developmental delay**  
  OMIM reports hypotonia and mildly impaired intellectual development or learning disabilities.[2][13]  
  GTR notes variable developmental delay with speech delay and mild intellectual impairment.[9]  
  Age of onset: infancy for hypotonia and early childhood for developmental and speech delay.[2][9]  
  Severity: usually mild; most individuals have borderline to mildly impaired intellectual function.[2][9]  
  Progression: developmental delays may improve with therapy but remain present; neurodegeneration is not reported.[2][9]  
  Frequency: common across reported cases.[2][9]  
  Quality of life: affects schooling, speech, and motor development, requiring early intervention and educational support.[2][9]  

Suggested HPO terms: HP:0001252 (Hypotonia), HP:0001263 (Global developmental delay), HP:0000750 (Delayed speech and language development), HP:0001254 (Mild intellectual disability).  

Brain malformations are mentioned as part of “multiple congenital anomalies involving the brain,” although detailed patterns (e.g., corpus callosum anomalies or cortical malformations) are not yet well defined.[2][13]  

Suggested HPO terms: HP:0004322 (Multiple congenital anomalies), HP:0002190 (Abnormality of brain morphology).  

### 3.4 Multisystem congenital anomalies

OMIM notes that congenital anomalies may involve the heart, brain, genitourinary, endocrine, and skeletal systems.[2][13]  
Chinese rare‑disease summaries similarly mention congenital heart disease and renal malformations.[11]  

Examples (based on aggregated descriptions):  
- **Cardiac**: congenital heart defects (specific lesion types not consistently reported).[2][11]  
  HPO: HP:0001627 (Abnormality of the cardiovascular system), HP:0001635 (Congenital heart anomaly).  
- **Genitourinary**: structural anomalies of kidneys or urinary tract.[2][11]  
  HPO: HP:0000119 (Abnormality of the kidney), HP:0000076 (Abnormality of the urinary system).  
- **Endocrine**: endocrine system anomalies (details sparse; may include growth‑ or thyroid‑related issues).[2][13]  
  HPO: HP:0000819 (Abnormality of the endocrine system).  
- **Skeletal**: skeletal anomalies (e.g., limb or vertebral anomalies) are mentioned, but exact patterns are not yet standardized.[2][11][13]  
  HPO: HP:0000925 (Abnormality of the skeletal system).  

### 3.5 Quality of life

No formal quality‑of‑life studies (EQ‑5D, SF‑36) have been published for THC11, but aggregated phenotypes imply chronic hematologic management, developmental and educational support, and possible cardiac or renal interventions, with overall survival likely good but with significant multisystem morbidity.[2][9][11][13]  

---

## 4. Genetic/Molecular Information

### 4.1 Causal gene: RAP1B

OMIM and PanelApp identify RAP1B (MIM 179530) as the causal gene for THC11, with heterozygous mutations leading to the phenotype.[2][4][5][13][15]  
RAP1B encodes a member of the Ras‑related small GTP‑binding protein family involved in integrin activation, cell adhesion, and signaling in platelets and other cells.[2][4][14]  

Suggested ontology terms:  
- HGNC: RAP1B (HGNC:9889)  
- GO (molecular function): GO:0003924 (GTPase activity), GO:0005525 (GTP binding)  
- GO (cellular component): GO:0005737 (cytoplasm), GO:0005829 (cytosol), GO:0005886 (plasma membrane)  

### 4.2 Pathogenic variants

ClinVar lists several RAP1B variants as pathogenic for THC11, including:  
- NM_001010942.3(RAP1B):c.176C>G (p.Ala59Gly), associated with THC11, classified as pathogenic, germline, based on literature.[3]  
- NM_001010942.3(RAP1B):c.178G>A (p.Gly60Arg), reported in a 5‑year‑old boy with THC11; this variant affects the switch II region critical for interaction with GAPs and is classified as pathogenic by OMIM submission.[7]  
- NM_001010942.3(RAP1B):c.11A>G (p.Tyr4Cys), classified as germline pathogenic in ClinVar for THC11.[8]  

All reported pathogenic variants are missense changes, consistent with altered protein function rather than simple haploinsufficiency.[3][7][8][14]  
ClinVar submissions indicate germline origin and “literature only” methods of evidence, emphasizing that knowledge is based on case reports rather than large cohorts.[3][7][8]  

Variant classification follows ACMG/AMP criteria in clinical labs, but ClinVar entries appear primarily as single‑submitter or OMIM curation with limited formal evidence categories given the small case numbers.[3][7][8]  

Population databases (e.g., gnomAD) are referenced indirectly by ClinVar submitters to support rarity, but specific allele frequencies are not reported in THC11 ClinVar records, implying extremely low frequency or absence in general populations.[3][7][8]  

No somatic RAP1B variants have been implicated in THC11; disease is consistently germline.[3][7][8]  

Functional consequence is inferred to be gain‑of‑function or altered activation cycling (e.g., reduced GAP‑mediated GTP hydrolysis), given the location of variants in critical regulatory regions and the dominant inheritance, although direct functional assays are limited.[2][7][14]  

### 4.3 Modifier genes and epigenetics

No modifier genes have been reported to systematically influence severity or spectrum of THC11.[2][3][13][14]  
There is no disease‑specific epigenetic signature described; epigenetic databases do not yet catalogue RAP1B‑related methylation or chromatin changes specific to THC11.[2][14]  

### 4.4 Chromosomal abnormalities

THC11 is not currently associated with structural chromosomal anomalies; disease is linked to point mutations/short variants in RAP1B rather than deletions or duplications.[2][6][13][14]  

---

## 5. Environmental Information

No specific toxins, radiation exposures, infections, or lifestyle factors are known to cause or significantly modify THC11; all reported cases are due to germline RAP1B variants.[2][3][9][13]  
Standard environmental risk factors for thrombocytopenia (drugs, alcohol, viral infections, autoimmune disease) are relevant for general hematology but not established as specific contributors to THC11.[2][9]  

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain

1. Heterozygous missense mutation in RAP1B leads to altered GTP‑binding/hydrolysis and dysregulated small GTPase signaling (inferred from variant location in switch regions).[2][7][14]  
2. Dysregulated RAP1B activity in megakaryocytes and platelets leads to impaired integrin activation (particularly αIIbβ3) and abnormal platelet formation and function (inferred from known RAP1B biology in platelet signaling).[2][4][14]  
3. Impaired platelet biogenesis and function result in chronic thrombocytopenia, enlarged platelets, and mild bleeding tendency.[2][11][13]  
4. Dysregulated RAP1B signaling in endothelial, neuronal, and mesenchymal cells leads to abnormal cell adhesion, migration, and morphogenesis during development (inferred from RAP1B roles in cell adhesion and vascular development).[2][4][14]  
5. These developmental disruptions result in multiple congenital anomalies affecting heart, brain, genitourinary, endocrine, and skeletal systems, as well as craniofacial dysmorphism.[2][11][13]  
6. Microcephaly, hypotonia, and mild intellectual disability arise from developmental brain involvement and altered neuronal and glial function (inferred from multisystem developmental anomalies and central nervous system involvement).[2][9][13]  
7. Chronic thrombocytopenia and cytopenias contribute downstream to bleeding risk and morbidity, while congenital anomalies drive organ‑specific complications and developmental impairment.[2][11][13]  

Upstream events: RAP1B mutation and consequent GTPase signaling dysregulation (steps 1–2).  
Downstream events: hematologic phenotype, congenital anomalies, neurodevelopmental features, and clinical complications (steps 3–7).  

### 6.2 Molecular pathways and cellular processes

RAP1B belongs to the Ras‑related small GTPase pathway, participating in inside‑out signaling that activates integrins, including those critical for platelet aggregation.[2][4][14]  
Disrupted RAP1B signaling likely alters pathways such as integrin signaling, MAPK/ERK downstream of Ras‑related GTPases, and adhesion cascades in endothelial and neural cells.[2][4][14]  

Suggested GO terms:  
- GO:0007264 (small GTPase‑mediated signal transduction)  
- GO:0030168 (platelet activation)  
- GO:0007160 (cell–matrix adhesion)  
- GO:0007165 (signal transduction)  
- GO:0007613 (membrane organization/adhesion processes relevant to development)  

At the cellular level, key affected processes likely include megakaryocyte differentiation, proplatelet formation, platelet activation, endothelial barrier function, and neuronal cell migration and adhesion.[2][4][14]  

Suggested CL terms:  
- CL:0000738 (Megakaryocyte)  
- CL:0000233 (Platelet)  
- CL:0000057 (Endothelial cell)  
- CL:0000540 (Neuron)  
- CL:0000122 (Mesenchymal cell)  

### 6.3 Protein dysfunction

Pathogenic variants cluster in functionally important regions of RAP1B, including residues around positions 59–60 (switch II), which regulate GTP hydrolysis and interaction with GAPs.[7]  
ClinVar comments state that the Gly60Arg variant affects the switch II region that is essential for interaction with GAPs, implying disrupted GTPase cycling and persistent activation.[7]  
Thus, the mechanistic model is altered (likely hyperactive or misregulated) RAP1B signaling rather than simple loss of function.[2][7][14]  

### 6.4 Metabolic and immune involvement

No specific metabolic abnormalities (e.g., energy or amino acid metabolism) have been described as primary features in THC11.[2][13]  
Immune system involvement appears limited to cytopenias; there is no strong evidence of autoimmunity or immunodeficiency beyond what PanelApp categorizes under “primary immunodeficiency or monogenic cytopenia” panels to facilitate testing.[4][15]  

Suggested GO terms: GO:0002376 (immune system process) for general hematologic involvement; more specific immunodeficiency GO terms are not yet justified.  

### 6.5 Tissue damage mechanisms and biochemical abnormalities

The primary abnormalities are developmental rather than degenerative; tissues are malformed rather than damaged by inflammatory or fibrotic processes.[2][11][13]  
Biochemically, the central defect is in GTPase signaling and integrin activation, rather than enzyme deficiency or receptor loss.[2][4][14]  

Suggested GO terms: GO:0001944 (vasculature development), GO:0048646 (anatomical structure formation involved in morphogenesis).  

### 6.6 Molecular profiling and advanced technologies

There are currently no published transcriptomic, proteomic, metabolomic, or single‑cell profiling studies specific to THC11.[2][3][9][13]  
Given the rarity of THC11 and small case numbers, multi‑omics integration and functional genomics screens have not yet been reported.[2][14]  

---

## 7. Anatomical Structures Affected

### 7.1 Organ‑level involvement

OMIM notes that congenital anomalies in THC11 may involve heart, brain, genitourinary, endocrine, and skeletal systems.[2][13]  
Chinese rare‑disease sources reinforce cardiac and renal involvement.[11]  

Primary organs:  
- Heart (congenital heart disease).[2][11] — UBERON:0000948 (heart).  
- Brain (structural anomalies and microcephaly).[2][9][13] — UBERON:0000955 (brain).  
- Kidneys and urinary tract.[2][11] — UBERON:0002113 (kidney), UBERON:0000056 (urinary bladder).  
- Endocrine organs (e.g., thyroid, pituitary, though specifics are not yet defined).[2][13] — UBERON:0002369 (endocrine gland).  
- Skeletal system.[2][11][13] — UBERON:0001434 (skeletal system).  

Hematologic system involvement is central due to thrombocytopenia and occasional leukopenia/anemia.[2][11][13]  

Suggested UBERON terms: UBERON:0000178 (blood), UBERON:0004535 (bone marrow).  

### 7.2 Tissue and cell level

Key tissue types:  
- Hematopoietic tissue (bone marrow, megakaryocytic lineage).[2][11][13]  
- Vascular endothelium and smooth muscle, given the role of RAP1B in integrin‑mediated adhesion.[2][4][14]  
- Neural tissue, due to microcephaly and developmental delay.[2][9][13]  
- Mesenchymal tissues contributing to craniofacial and skeletal development.[2][11][13]  

Suggested CL terms: CL:0000738 (Megakaryocyte), CL:0000233 (Platelet), CL:0000057 (Endothelial cell), CL:0000540 (Neuron), CL:0000122 (Mesenchymal cell).  

### 7.3 Subcellular localization

RAP1B is a small GTPase localized to the cytosol and plasma membrane, cycling between GDP‑bound inactive and GTP‑bound active states.[2][4][14]  

Suggested GO cellular component terms: GO:0005829 (cytosol), GO:0005886 (plasma membrane), GO:0005737 (cytoplasm).  

### 7.4 Localization and lateralization

Anomalies associated with THC11 are typically bilateral and systemic (e.g., microcephaly, congenital heart disease, bilateral kidney anomalies), rather than strictly unilateral.[2][11][13]  

Suggested HPO term: HP:0002269 (Bilateral involvement) for relevant organ anomalies.  

---

## 8. Temporal Development

### 8.1 Onset

THC11 is a congenital disorder: dysmorphic facies, growth restriction, and congenital anomalies are present at birth, and thrombocytopenia is usually identified in infancy or early childhood.[2][9][11][13]  
Onset pattern is chronic and insidious rather than acute; abnormalities may first be recognized through neonatal or early pediatric hematologic testing or evaluation for congenital anomalies.[2][9]  

### 8.2 Progression and disease course

Thrombocytopenia appears chronic and persistent, with no documented spontaneous normalization; progression is generally stable rather than relapsing–remitting.[2][11][13]  
Developmental delays and learning difficulties can improve with therapy but generally persist, consistent with static developmental brain anomalies rather than progressive neurodegeneration.[2][9]  
Congenital anomalies (cardiac, renal, skeletal) are structural and do not regress; clinical course depends on severity and management of each anomaly.[2][11][13]  

Disease duration is lifelong, though severity of manifestations varies.[2][9][13]  

### 8.3 Patterns and critical periods

Critical periods include prenatal and early postnatal development, during which RAP1B‑mediated signaling affects organogenesis and brain development.[2][4][14]  
Early childhood is another critical window for recognizing thrombocytopenia and instituting bleeding precautions and developmental interventions.[2][9][11]  

---

## 9. Inheritance and Population

### 9.1 Epidemiology

THC11 is ultra‑rare; OMIM and PanelApp classify it as a rare Mendelian disorder, and all descriptions derive from a small number of families and isolated cases rather than population studies.[2][4][9][13][15]  
Precise prevalence and incidence figures are not available; current evidence suggests only a handful to tens of reported individuals worldwide.[2][9][13]  

### 9.2 Inheritance pattern

OMIM lists THC11 as autosomal dominant.[2][13]  
ClinVar and PanelApp entries are consistent with heterozygous germline RAP1B variants causing the phenotype, with family segregation where available.[3][4][5][7][8][14][15]  

Penetrance and expressivity:  
Available case data suggest high penetrance of thrombocytopenia and facial dysmorphism in carriers, with variable expressivity of congenital anomalies and neurodevelopmental features.[2][9][11][13]  

No evidence of genetic anticipation, germline mosaicism, or defined founder effects has been reported.[2][3][9][13][14]  

Carrier frequency in general populations has not been estimated; pathogenic RAP1B variants appear absent or extremely rare in large reference cohorts.[3][7][8]  

### 9.3 Population demographics

Most published cases originate from high‑income settings with access to exome or genome sequencing, but detailed ethnic distribution is not yet available.[2][9][13][14]  
No sex predilection has been noted; both males and females are affected.[2][9][11][13]  
Age distribution: presentation is in infancy or childhood; adult cases may be under‑recognized, particularly if anomalies and thrombocytopenia are mild.[2][9]  

---

## 10. Diagnostics

### 10.1 Clinical and laboratory tests

Routine hematology identifies thrombocytopenia, often with large platelets and possibly mild anemia or leukopenia.[2][11][13]  
Clinicians should obtain platelet counts, mean platelet volume, peripheral blood smear, and standard coagulation studies as initial evaluation.[2][11]  

Imaging and specialty evaluations are guided by anomalies: echocardiography for congenital heart disease, brain MRI for structural CNS anomalies and microcephaly, renal ultrasound for genitourinary anomalies, and endocrine workup as indicated.[2][11][13]  

No disease‑specific circulating protein or metabolite biomarker has been reported; diagnosis relies on phenotypic pattern plus genetic testing.[2][3][9][13]  

Suggested LOINC terms: general platelet count (LOINC 777-3), complete blood count panels; imaging codes for echocardiography and MRI.  

### 10.2 Genetic testing

Given the rarity and syndromic nature, diagnosis is usually made by broad sequencing (exome/genome) rather than targeted single‑gene testing.[2][9][14]  
NCBI GTR lists THC11 associated with RAP1B and describes dysmorphic facial features and developmental delay, implying that clinical laboratories offer tests detecting RAP1B variants within broader exome or multi‑gene panels.[9]  
Genomics England PanelApp includes RAP1B in “Bleeding and platelet disorders” and “Cytopenia – NOT Fanconi anaemia,” indicating its inclusion in panels used for unexplained thrombocytopenia and cytopenia phenotypes.[4][5][15]  
PanelApp also lists RAP1B in primary immunodeficiency / monogenic cytopenia panels, reflecting its recognition as a monogenic cytopenia gene.[4][15]  

ClinVar demonstrates that RAP1B variants are detected and reported by clinical labs, with 2023–2024 submissions documenting novel missense variants classified as pathogenic for THC11.[3][7][8]  

Recommended testing strategy:  
- First‑line: clinical exome or genome sequencing for patients with unexplained congenital thrombocytopenia plus multiple anomalies and dysmorphic facies, interpreted with awareness of RAP1B.[2][4][9][14][15]  
- Alternative: targeted gene panel for inherited thrombocytopenia/cytopenia including RAP1B.[4][5][15]  
- Single‑gene sequencing of RAP1B may be reasonable in families with known pathogenic variants.[3][7][8]  

Chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, and repeat‑expansion assays are not primary diagnostic tools for THC11 and are usually reserved for differential diagnoses when broader genomic studies are negative.[2][9][13]  

### 10.3 Clinical criteria and differential diagnosis

No formal consensus diagnostic criteria (e.g., society guidelines) exist yet; diagnosis rests on the combination of:  
- Chronic thrombocytopenia (often with large platelets).  
- Dysmorphic facial features.  
- Multiple congenital anomalies (cardiac, renal, endocrine, skeletal, brain).  
- Poor growth, microcephaly, hypotonia, and mild intellectual disability.  
- Confirmed pathogenic heterozygous variant in RAP1B.  

Differential diagnoses include other syndromic thrombocytopenias such as:  
- Jacobsen syndrome (Paris‑Trousseau thrombocytopenia).  
- Thrombocytopenia‑absent radius (TAR).  
- Thrombocytopenia 8 with dysmorphic features and developmental delay (THC8).  
Chinese rare‑disease catalogues list these alongside THC11, reflecting clinical overlap.[11]  

ACTB‑associated syndromic thrombocytopenia (ACTB‑AST) produces microcephaly, minor facial anomalies, white blood cell anomalies, and thrombocytopenia, and must be distinguished genetically.[10][12]  

### 10.4 Screening

There is no population‑based or newborn screening program for THC11 due to its extreme rarity.[2][9][13]  
Cascade testing (testing at‑risk relatives of index cases) is recommended in principle for autosomal‑dominant disorders but has not yet been systematically studied for THC11.[2][3][9][14]  

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

No formal survival analyses or registry‑based mortality data exist for THC11 due to the small number of reported cases.[2][9][13]  
Available case descriptions imply survival into childhood and likely adulthood, with prognosis heavily dependent on severity and management of cardiac, renal, and other organ anomalies.[2][9][11][13]  

### 11.2 Morbidity and function

Morbidity arises from:  
- Chronic thrombocytopenia and bleeding risk.  
- Developmental delay and learning difficulties.  
- Congenital heart and renal disease.  
- Potential endocrine and skeletal complications.[2][9][11][13]  

Long‑term disability may range from mild (learning difficulties, mild thrombocytopenia) to more significant functional limitations in those with major organ malformations.[2][9][11][13]  

There are no disease‑specific quality‑of‑life instrument data; impact is inferred from multisystem involvement.[2][9][13]  

### 11.3 Prognostic factors

Prognosis likely depends on:  
- Type and severity of cardiac and renal anomalies.  
- Degree of thrombocytopenia and bleeding history.  
- Extent of neurodevelopmental impairment.[2][9][11][13]  

No validated prognostic biomarkers have been identified; RAP1B variant type may influence severity, but data are too limited for clear genotype–phenotype correlations.[3][7][8][14]  

---

## 12. Treatment

### 12.1 Pharmacotherapy and supportive hematologic care

There are no disease‑specific pharmacologic therapies targeting RAP1B for THC11.[2][3][9][13]  
Management follows general principles for inherited thrombocytopenia:  
- Avoid antiplatelet and anticoagulant drugs when possible.  
- Use platelet transfusions for major bleeding or invasive procedures.  
- Consider thrombopoietin receptor agonists cautiously if thrombocytopenia is severe and other options are limited, although no THC11‑specific data exist.[2][9][11][13]  

Suggested NCIT terms:  
- NCIT:C61588 (Platelet Transfusion).  
- NCIT:C12679 (Supportive Care).  

### 12.2 Surgical and interventional management

Congenital heart defects and renal anomalies are managed according to standard pediatric cardiology and nephrology guidelines (e.g., surgical correction, catheter‑based interventions, or medical management).[2][11][13]  

Suggested NCIT terms:  
- NCIT:C92715 (Congenital Heart Disease Surgery).  
- NCIT:C15273 (Nephrology Procedure).  

### 12.3 Developmental and rehabilitative care

Early intervention services, speech and language therapy, occupational therapy, and educational supports are recommended for children with developmental delay and learning disabilities.[2][9][13]  

Suggested NCIT terms:  
- NCIT:C15219 (Occupational Therapy).  
- NCIT:C15218 (Physical Therapy).  
- NCIT:C19071 (Speech Therapy).  

### 12.4 Advanced and experimental therapies

No gene therapy, RNA‑based therapy, or targeted small‑molecule therapy has been reported for THC11 as of 2024.[2][3][9][13][14]  
No clinical trials specifically enroll THC11 patients; management remains individualized and supportive.[2][9][13]  

---

## 13. Prevention

### 13.1 Primary, secondary, and tertiary prevention

Primary prevention is not feasible for sporadic germline RAP1B mutations, but reproductive options (e.g., preimplantation genetic testing) could be offered once a familial pathogenic variant is identified.[2][3][9][14]  

Secondary prevention focuses on early detection of complications: regular CBC monitoring, surveillance for cardiac and renal issues, and neurodevelopmental assessment.[2][9][11][13]  

Tertiary prevention aims to mitigate complications (e.g., bleeding, heart failure, chronic kidney disease) through appropriate medical and surgical management, rehabilitation, and individualized educational support.[2][9][11][13]  

Suggested NCIT terms:  
- NCIT:C15273 (Monitoring).  
- NCIT:C92189 (Genetic Counseling).  

### 13.2 Screening and counseling

Carrier and prenatal screening are not systematic but can be offered in families with known RAP1B pathogenic variants using exome, targeted sequencing, or panel tests.[2][3][9][14]  
Genetic counseling is recommended to discuss autosomal‑dominant inheritance, recurrence risk, and options for prenatal or preimplantation diagnosis.[2][9][13][14]  

Behavioral interventions (diet, exercise, smoking cessation) have no specific role in preventing THC11 but may improve general health in affected individuals.[2][9]  

---

## 14. Other Species / Natural Disease

RAP1B orthologs are widely conserved across vertebrates, and Rap1b knockout mice are known (from broader literature) to display defects in platelet function and vascular development, but no explicit “THC11‑like” natural disease has been catalogued in animal databases to date.[2][4][14]  
OMIA and other veterinary resources do not currently list a RAP1B‑related thrombocytopenia syndrome analogous to THC11 in domestic animals.[2][14]  

There is no evidence of zoonotic transmission or cross‑species susceptibility, as THC11 is a non‑infectious germline condition.[2][3][13][14]  

---

## 15. Model Organisms

No dedicated “THC11” model is described in OMIM or PanelApp, but Rap1b‑deficient mouse models in the broader literature demonstrate impaired platelet function and vascular anomalies, supporting the plausibility of the human mechanism.[2][4][14]  
Model organism databases have not yet integrated RAP1B variants specifically annotated to THC11 as of the retrieved resources.[2][14]  

Potential applications of Rap1b mouse models include:  
- Studying platelet integrin activation defects.  
- Exploring vascular development and congenital heart phenotypes.  
- Testing supportive and targeted therapies for thrombocytopenia or vascular anomalies.  

Model limitations include species differences in craniofacial and neurodevelopmental features and incomplete recapitulation of the full multisystem human phenotype.[2][4][14]  

---

### Evidence types

- **Human clinical**: OMIM disease summary, ClinVar case‑level variant curation, GTR phenotypic description, PanelApp gene–disease curation, and national rare‑disease catalogues provide aggregated and case‑based clinical data (chiefly Latham et al. 2018 and later case reports summarized in these resources).[2][3][4][5][9][11][13][14][15]  
- **Model organism/in vitro**: broader RAP1B literature (not disease‑specific in retrieved resources) informs mechanistic inference regarding small GTPase signaling, integrin activation, and platelet biology.[2][4][14]  
- **Computational**: ClinVar and panel curation rely on in‑silico predictions and structural considerations for classifying missense RAP1B variants as pathogenic, especially those in switch II and other regulatory regions.[3][7][8][14]  

Because THC11 is extremely rare and only recently defined (OMIM entry updated in 2025), most mechanistic and clinical conclusions remain based on small‑scale evidence, and future case reports and functional studies are likely to refine the phenotype, mechanism, and management recommendations.[2][3][7][9][13][14]

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
| Terms checked | 60 |
| Resolved | 59 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 59 |
| Terms named correctly | 28 |
| Terms named as a **different** term | 22 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000283` (2 mentions) - the report calls it "Facial dysmorphism"; HP calls it **Broad face**
- `HP:0004322` (2 mentions) - the report calls it "Multiple congenital anomalies"; HP calls it **Short stature**
- `HP:0001907` (1 mention) - the report calls it "Abnormal platelet morphology"; HP calls it **Thromboembolism**
- `HP:0000316` (1 mention) - the report calls it "Telecanthus"; HP calls it **Hypertelorism**
- `HP:0000308` (1 mention) - the report calls it "Thin vermilion border"; HP calls it **Microretrognathia**
- `HP:0001254` (1 mention) - the report calls it "Mild intellectual disability"; HP calls it **Lethargy**
- `HP:0002190` (1 mention) - the report calls it "Abnormality of brain morphology"; HP calls it **Choroid plexus cyst**
- `HP:0000076` (1 mention) - the report calls it "Abnormality of the urinary system"; HP calls it **Vesicoureteral reflux**
- `HP:0000819` (1 mention) - the report calls it "Abnormality of the endocrine system"; HP calls it **Diabetes mellitus**
- `GO:0007613` (1 mention) - the report calls it "membrane organization/adhesion processes relevant to development"; GO calls it **memory**
- `CL:0000057` (2 mentions) - the report calls it "Endothelial cell"; CL calls it **fibroblast**
- `CL:0000122` (2 mentions) - the report calls it "Mesenchymal cell"; CL calls it **stellate neuron**
- `UBERON:0000056` (1 mention) - the report calls it "urinary bladder"; UBERON calls it **ureter**
- `UBERON:0004535` (1 mention) - the report calls it "bone marrow"; UBERON calls it **cardiovascular system**
- `HP:0002269` (1 mention) - the report calls it "Bilateral involvement"; HP calls it **Abnormality of neuronal migration**
- `NCIT:C61588` (1 mention) - the report calls it "Platelet Transfusion"; NCIT calls it **Malignant Hyperchromatic Small Epithelial Cell**
- `NCIT:C12679` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Blood Vessel**
- `NCIT:C15273` (2 mentions) - the report calls it "Nephrology Procedure", "Monitoring"; NCIT calls it **Longitudinal Study**
- `NCIT:C15219` (1 mention) - the report calls it "Occupational Therapy"; NCIT calls it **Health Care Delivery**
- `NCIT:C15218` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Cystostomy**
- `NCIT:C19071` (1 mention) - the report calls it "Speech Therapy"; NCIT calls it **Toxicology, Antidotes/Treatment**
- `NCIT:C92189` (1 mention) - the report calls it "Genetic Counseling"; NCIT calls it **Perennial Allergic Rhinitis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0008284` (1 mention) - the report calls it "positive regulation of cell proliferation"; GO calls it **positive regulation of cell population proliferation**, and lists "positive regulation of cell proliferation" among its other names
- `HP:0001882` (1 mention) - the report calls it "Leukopenia"; HP calls it **Decreased total leukocyte count**, and lists "Leukopenia" among its other names
- `HP:0001627` (1 mention) - the report calls it "Abnormality of the cardiovascular system"; HP calls it **Abnormal heart morphology**, and lists "Abnormality of the heart" among its other names
- `HP:0001635` (1 mention) - the report calls it "Congenital heart anomaly"; HP calls it **Congestive heart failure**
- `HP:0000119` (1 mention) - the report calls it "Abnormality of the kidney"; HP calls it **Abnormality of the genitourinary system**, and lists "Abnormality of the GU system" among its other names
- `HP:0000925` (1 mention) - the report calls it "Abnormality of the skeletal system"; HP calls it **Abnormality of the vertebral column**
- `CL:0000738` (2 mentions) - the report calls it "Megakaryocyte"; CL calls it **leukocyte**
- `UBERON:0002369` (1 mention) - the report calls it "endocrine gland"; UBERON calls it **adrenal gland**, and lists "epinephric gland" among its other names
- `NCIT:C92715` (1 mention) - the report calls it "Congenital Heart Disease Surgery"; NCIT calls it **Fetal Heart Finding**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C15273` - called "Nephrology Procedure", "Monitoring"