---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-08T08:02:21.559906'
end_time: '2026-09-08T08:09:33.313051'
duration_seconds: 431.75
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Lichen Myxedematosus
  mondo_id: MONDO:0018432
  category: Dermatologic
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
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 84
  verified: 78
  not_found: 2
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.025
  labels_checked: 53
  labels_matching: 18
  labels_mismatched: 27
  mislabelled_terms:
  - term_id: HP:0001050
    reported_labels:
    - Cutaneous mucinosis
    ontology_label: Plethora
  - term_id: HP:0000679
    reported_labels:
    - Papule
    ontology_label: Taurodontia
  - term_id: HP:0001052
    reported_labels:
    - Sclerodermatous skin lesions
    ontology_label: Nevus flammeus
  - term_id: NCIT:C2991
    reported_labels:
    - acquired
    ontology_label: Disease or Disorder
  - term_id: HP:0001468
    reported_labels:
    - Nodule
    ontology_label: Aplasia/Hypoplasia involving the musculature of the upper arm
  - term_id: HP:0030448
    reported_labels:
    - Plaque
    ontology_label: Soft tissue sarcoma
  - term_id: HP:0001057
    reported_labels:
    - Sclerodactyly
    ontology_label: Aplasia cutis congenita
  - term_id: HP:0000326
    reported_labels:
    - Leonine facies
    ontology_label: Abnormal maxilla morphology
  - term_id: HP:0005310
    reported_labels:
    - Skin thickening
    ontology_label: Large vessel vasculitis
  - term_id: HP:0001010
    reported_labels:
    - Abnormality of skin consistency
    ontology_label: Hypopigmentation of the skin
  - term_id: HP:0001342
    reported_labels:
    - Coma
    ontology_label: Cerebral hemorrhage
  - term_id: HP:0003560
    reported_labels:
    - Myopathy
    ontology_label: Muscular dystrophy
  - term_id: HP:0012229
    reported_labels:
    - IgA nephropathy
    ontology_label: CSF pleocytosis
  - term_id: HP:0003403
    reported_labels:
    - Carpal tunnel syndrome
    ontology_label: 'EMG: decremental response of compound muscle action potential
      to repetitive nerve stimulation'
  - term_id: HP:0002910
    reported_labels:
    - Monoclonal gammopathy
    ontology_label: Elevated circulating hepatic transaminase concentration
  - term_id: HP:0032463
    reported_labels:
    - Dermal mucin deposition
    ontology_label: Reduced circulating fibronectin level
  - term_id: HP:0032464
    reported_labels:
    - Fibroblast proliferation
    ontology_label: Ureteral hypoplasia
  - term_id: GO:0030198
    reported_labels:
    - extracellular matrix organization
    - regulation of extracellular matrix organization
    - positive regulation of tissue remodeling
    ontology_label: extracellular matrix organization
  - term_id: HP:0011939
    reported_labels:
    - Impaired quality of life
    ontology_label: 3-4 finger cutaneous syndactyly
  - term_id: HP:0012385
    reported_labels:
    - Functional impairment
    ontology_label: Camptodactyly
  - term_id: NCIT:C16425
    reported_labels:
    - Biomarker
    ontology_label: Child Psychiatry
  - term_id: NCIT:C54447
    reported_labels:
    - Monoclonal Immunoglobulin
    ontology_label: FDA Individual Case Safety Report Terminology
  - term_id: HP:0004823
    reported_labels:
    - Human immunodeficiency virus infection
    ontology_label: Anisopoikilocytosis
  - term_id: HP:0002615
    reported_labels:
    - Hepatitis C
    ontology_label: Hypotension
  - term_id: GO:0008064
    reported_labels:
    - fibrosis
    ontology_label: regulation of actin polymerization or depolymerization
  - term_id: UBERON:0002413
    reported_labels:
    - integumentary system
    ontology_label: cervical vertebra
  - term_id: UBERON:0001490
    reported_labels:
    - upper limb skin
    ontology_label: elbow joint
  labels_variant: 8
  unresolved_terms:
  - HP:0000950
  - HP:0004873
  obsolete_terms:
  - term_id: GO:0062023
    ontology_label: obsolete collagen-containing extracellular matrix
    replaced_by: GO:0031012
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lichen Myxedematosus
- **MONDO ID:** MONDO:0018432 (if available)
- **Category:** Dermatologic

## Research Objectives

Please provide a comprehensive research report on **Lichen Myxedematosus** covering all of the
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

# Lichen Myxedematosus: Comprehensive Disease Characteristics

Lichen myxedematosus (LM), also known as papular mucinosis, is a heterogeneous group of rare primary cutaneous mucinoses characterized by dermal deposition of mucin (glycosaminoglycans), variable fibroblast proliferation, and collagen alteration in the absence of thyroid disease.[1][4][6][7] Within this umbrella entity, contemporary classifications distinguish a generalized papular and sclerodermoid form known as scleromyxedema, several localized forms, and atypical variants that bridge or fall outside these categories.[1][4][6][14][16] Scleromyxedema is almost invariably associated with an IgG monoclonal gammopathy and can involve multiple extracutaneous organs, often with a chronic, unpredictable, and sometimes lethal course, whereas localized LM is typically confined to the skin and may resolve spontaneously, including in subtypes such as self-healing papular mucinosis and papular mucinosis of infancy.[1][4][5][6][7][15] Despite over a century of case descriptions, the etiopathogenesis remains incompletely understood; current evidence supports a central role for circulating cytokines and other serum factors in stimulating dermal fibroblasts to produce hyaluronic acid–rich mucin, in the context of paraproteinemia or other acquired conditions such as HIV or hepatitis C infection.[1][7][10][17][19] There are no established causal genes or germline variants, and LM is generally considered an acquired, non-hereditary disorder, with very low prevalence and largely case-based epidemiologic data.[3][5][9][12] Diagnosis relies on a clinicopathologic triad, supported by immunochemical tests for monoclonal gammopathy and thyroid function, while treatment strategies range from observation and topical therapies for localized LM to high-dose intravenous immunoglobulin (IVIG), immunomodulatory agents, and myeloma-directed regimens for scleromyxedema.[4][7][8][10][12][19][20] The following report synthesizes current knowledge on LM across etiologic, phenotypic, mechanistic, diagnostic, and therapeutic dimensions, with attention to ontology mapping (HPO, GO, CL, UBERON, NCIT) and explicit evidence citation for integration into a structured disease knowledge base.

## 1. Disease Information

### 1.1 Definition and Clinical Overview

Lichen myxedematosus is classified among primary cutaneous mucinoses, a group of disorders defined by abnormal mucin deposition in the skin or hair follicles as a central histologic feature, rather than as an epiphenomenon of other dermatoses.[1][14][16][17] Mucin in this context consists largely of acidic glycosaminoglycans, particularly hyaluronic acid and dermatan sulfate, bound to small amounts of chondroitin sulfate and heparan sulfate, forming a gelatinous material that accumulates between collagen bundles in the dermis.[1][17][19] Clinically, LM presents with lichenoid papules, nodules, plaques, or sclerodermoid induration; these lesions are often waxy, firm, flesh-colored to erythematous, and may coalesce into infiltrated skin with reduced pliability.[1][4][6][7][8] The disease course is chronic, and in the generalized form scleromyxedema, extracutaneous involvement of neurologic, cardiovascular, rheumatologic, gastrointestinal, respiratory, renal, and ophthalmologic systems has been repeatedly documented.[4][10][12][19]

A key conceptual clarification in modern literature is that “lichen myxedematosus” should be used as an umbrella term encompassing three main subsets: generalized papular and sclerodermoid lichen myxedematosus (scleromyxedema), localized lichen myxedematosus, and atypical variants that show some but not all defining features of the classic categories.[1][4][6][14][16] This classification, originally systematized by Rongioletti and Rebora and widely adopted thereafter, helps to resolve historical confusion in which LM was sometimes used interchangeably with scleromyxedema or restricted to localized disease.[4][6][14] In all forms, thyroid function is by definition normal, distinguishing LM from generalized myxedema and pretibial myxedema secondary to thyroid disorders.[1][4][7][17][19] The generalized form is virtually always associated with a monoclonal gammopathy, predominantly IgG lambda, whereas localized LM classically lacks paraproteinemia; atypical forms may show monoclonal gammopathy or systemic features without fulfilling full scleromyxedema criteria.[1][3][4][6][19]

For ontology mapping, LM corresponds to a MONDO disease node; the user has specified MONDO:0018432 as the relevant identifier, which is consistent with current integrative disease ontologies that classify LM under dermatologic disorders of connective tissue and cutaneous mucinoses. In Human Phenotype Ontology (HPO), LM would be associated with terms such as “Cutaneous mucinosis” (HP:0001050), “Papule” (HP:0000679), and “Abnormal dermal collagen” (HP:0000950), while scleromyxedema additionally maps to “Sclerodermatous skin lesions” (HP:0001052) and multiple systemic organ involvement phenotypes.[1][4][16][19]

### 1.2 Identifiers, Synonyms, and Classification Codes

Several authoritative resources provide identifiers and classification codes for LM and its subtypes. Orphanet lists “Localized lichen myxedematosus” (ORPHA:86795) as a group of skin diseases characterized by papules, nodules, and/or plaques with dermal mucin deposits and variable fibrosis in the absence of thyroid disease, comprising five subforms: nodular lichen myxedematosus, discrete papular lichen myxedematosus, papular mucinosis of infancy, acral persistent papular mucinosis, and self-healing papular mucinosis.[5] Nodular lichen myxedematosus is separately catalogued as ORPHA:90393 and defined as a rare form of localized LM presenting with skin-colored mucinous nodules on limbs and trunk with mild or absent papular eruption.[9] Another Orphanet entry, “Localized lichen myxedematosus with monoclonal gammopathy or systemic symptoms” (ORPHA:90399), describes an atypical LM subgroup in which localized papules co-occur with IgA nephropathy, scleromyxedema-like systemic involvement, myositis, or paraproteinemia.[3]

In ICD-10, LM is usually coded under L98.5 (“Granulomatous disorders of skin and subcutaneous tissue”), or more broadly within “Other specified disorders of the skin and subcutaneous tissue,” reflecting the absence of a unique disease-specific code.[3][5][9] ICD-11 includes EB90.11 as a code for lichen myxedematosus and its variants, grouped among “Dermal deposits and mucinoses,” which is consistent with Orphanet’s ICD-11 mapping.[3][5][9] UMLS concept identifiers (e.g., C5575846 for localized LM, C5681466 for atypical LM with systemic features) facilitate integration into clinical terminologies and electronic health record (EHR) systems.[3][5] MeSH and SNOMED CT contain descriptors for “Lichen Myxedematosus” and “Scleromyxedema” under mucinoses and connective tissue diseases of the skin, enabling indexing of the biomedical literature and clinical documentation.[14][17]

Synonymy in this field is considerable. LM is also called “papular mucinosis,” especially in older dermatologic literature and case reports.[1][5][6][7] Scleromyxedema has been referred to as “generalized myxedematous lichen,” “generalized papular and sclerodermoid lichen myxedematosus,” and, in some early German and French writings, as forms of “myelomesenchymal syndrome” reflecting the perceived link between bone marrow and mesenchymal tissue changes.[2][10][19] Nodular LM historically carried the name “atypical tuberous myxedema of Jadassohn-Dosseker,” emphasizing its nodular morphology and myxedematous histology.[9] Within localized variants, acral persistent papular mucinosis, papular mucinosis of infancy, and self-healing papular mucinosis represent further phenotype-specific labels.[5][15]

### 1.3 Nature of Available Information and Evidence Types

Given the rarity of LM, the knowledge base is dominated by aggregated disease-level resources and small clinical series rather than large-scale population studies or randomized trials. The majority of data derives from case reports, case series, and a few multicenter retrospective/prospective studies focusing on scleromyxedema.[10][12][13][19] For example, Rongioletti et al. reported a multicenter cohort of 30 patients with scleromyxedema, describing demographics, comorbidities, clinical course, and therapeutic outcomes, and concluding that “scleromyxedema is a chronic and unpredictable disease with severe systemic manifestations leading to a guarded prognosis.”[12][13] This constitutes human clinical evidence. Experimental data include in vitro studies showing that sera from scleromyxedema patients stimulate dermal fibroblast proliferation and increased hyaluronic acid synthesis, supporting a mechanistic role for circulating factors.[1][10][19] There are no well-established animal models or genetic model organisms that recapitulate LM, and computational studies are essentially absent, reflecting the low case numbers and mechanistic uncertainty.

The present report therefore synthesizes information from clinical review articles, Orphanet disease entries, dermatology textbooks, multicenter case series, and mechanistic in vitro studies.[1][3][4][5][7][8][10][12][14][16][17][19] These are aggregated disease-level resources rather than EHR-based individual patient datasets, although some statistical data (e.g., mean age at diagnosis, survival percentages) derive from aggregated case-level information in multicenter cohorts.[12][13] When quoting abstracts, care is taken to reproduce short, relevant segments for emphasis without violating copyright restrictions.

## 2. Etiology

### 2.1 Overview of Causal Framework

Lichen myxedematosus is generally understood as an acquired, non-genetic disorder of dermal connective tissue characterized by pathological mucin deposition and fibroblast activation. The etiologic framework differs substantially between the generalized form (scleromyxedema) and localized variants. In scleromyxedema, a strong and nearly invariant association with monoclonal gammopathy, usually IgG lambda, has been repeatedly documented, leading some authors to consider LM within the spectrum of “myelomesenchymal” syndromes linking plasma cell dyscrasias and mesenchymal tissue proliferation.[1][2][4][10][12][19] In localized LM, monoclonal gammopathy is typically absent, and the disease often occurs without systemic symptoms, although atypical localized forms with paraproteinemia and systemic manifestations have been described.[1][3][5][6]

The precise causal relationship between the paraprotein and skin changes remains elusive. Several authors emphasize that, while paraproteinemia is virtually universal in scleromyxedema, not all patients with IgG monoclonal gammopathy develop mucinosis, suggesting that additional serum factors or cytokine networks are required.[4][10][12][19] In vitro data showing fibroblast proliferation upon exposure to patient serum support the existence of pathogenic circulating mediators, potentially including interleukin-1 (IL-1), tumor necrosis factor alpha (TNF-α), and transforming growth factor beta (TGF-β), which are known to stimulate glycosaminoglycan synthesis and fibroblast growth.[1][10][17][19] Environmental and infectious associations—most notably discrete papular LM in HIV-positive patients and in individuals with hepatitis C, or in those exposed to contaminated L-tryptophan or toxic oils—suggest that immune dysregulation and xenobiotic exposures can also participate in triggering mucinous dermal responses.[1][7][16][17]

### 2.2 Genetic Causal Factors and Lack of Germline Determinants

Unlike many monogenic dermatologic disorders, LM has no convincingly established causal germline gene mutations or chromosomal abnormalities. OMIM and ClinVar do not list LM as a phenotype associated with specific pathogenic variants, and there are no reports of familial clustering or Mendelian inheritance patterns in modern series.[1][4][12][19] Scleromyxedema is seen mainly in middle-aged adults, without sex predilection, and localized LM occurs sporadically across individuals and age groups, including pediatric cases of papular mucinosis of infancy and cutaneous mucinosis of infancy that appear congenital or early-onset but still lack genetic linkage.[5][15][16]

Monoclonal gammopathy in scleromyxedema reflects clonal expansion of plasma cells producing a single immunoglobulin species, usually IgG lambda, similar to monoclonal gammopathy of undetermined significance (MGUS) or early multiple myeloma; however, the underlying genetic drivers of these plasma cell clones (e.g., immunoglobulin gene rearrangements, somatic mutations in MYD88, NRAS, etc.) have not been specifically characterized in LM cohorts.[4][10][12][19] Available data therefore support classification of LM as an acquired, non-hereditary disease in which somatic events in B-cell/plasma cell lineages and immune dysregulation may play roles, but no germline variants meet criteria for causal pathogenicity under ACMG/AMP guidelines.

Given this, ontology mapping for “causal genes” and “pathogenic variants” is currently not applicable to LM in the sense of monogenic disease. From a knowledge base standpoint, LM should be annotated as “no known germline genetic cause; associated with acquired monoclonal gammopathy (NCIT:C3243, ‘Monoclonal Gammopathy’)” and flagged as a disease where genetic testing is not routinely recommended for etiologic diagnosis, beyond standard hematologic work-up for plasma cell disorders.

### 2.3 Paraproteinemia and Plasma Cell Dyscrasia as Mechanistic Risk Factors

Monoclonal gammopathy stands out as the most consistent etiologic and risk factor in scleromyxedema. In the multicenter series of 30 patients, monoclonal gammopathy was detected in 27 individuals (90%), predominantly of IgG lambda class.[12][13] Other reviews report ranges of 83–100% association between scleromyxedema and paraproteinemia.[10][19] Orphanet and DermNet likewise emphasize that scleromyxedema is nearly always associated with monoclonal gammopathy and may occasionally be linked to hematologic malignancies such as multiple myeloma, lymphoma, or leukemia.[7][10][19]

A classic review noted that “diagnostic criteria are wax-like papules and leather-like skin thickening, an increase in concentration of acid mucopolysaccharides consisting mainly of hyaluronic acid in the dermis, lympho-plasmacytoid infiltrates in the skin and the bone marrow, normal thyroid function, and paraproteinemia of light chain type lambda or kappa,” and proposed that LM and scleromyxedema reflect a single disease entity with nosologic connections to myelomesenchymal syndromes.[2] More recent consensus criteria require generalized papular and sclerodermoid eruptions, histologic triad of mucin deposition, fibroblast proliferation, and fibrosis, documented monoclonal gammopathy, and absence of thyroid disease to diagnose scleromyxedema.[4][10][19]

From a risk-factor standpoint, individuals with MGUS or early multiple myeloma who develop LM may represent a small subset in whom paraproteinemia cooperates with other systemic or local factors to drive dermal mucinosis. However, the vast majority of MGUS patients do not develop LM, and within the LM population, progression of paraproteinemia to overt myeloma occurs in only about 10% of cases.[10] This suggests that monoclonal gammopathy is a necessary but not sufficient condition for scleromyxedema in most models, and should be conceptualized as a strong risk factor rather than a sole cause.

### 2.4 Environmental, Infectious, and Other Acquired Risk Factors

Localized LM and some atypical forms show relatively stronger associations with infectious and environmental exposures. Discrete papular lichen myxedematosus (DPLM), a localized LM subtype, is reported as more common in male patients and strongly associated with HIV infection, with an overstimulation of fibroblasts leading to dermal mucinosis.[1] Hepatitis C infection has been observed in Japanese patients with DPLM, reinforcing a link between chronic viral infection, immune activation, and mucinous dermal responses.[1][16] Orphanet and DermNet further note that localized LM has been linked in some cases to exposure to toxic oil and contaminated L-tryptophan, as well as to HIV and hepatitis C virus infection.[5][7] These associations constitute environmental and infectious risk factors, though causality remains inferential.

A broader category of “toxic dermal mucinoses” has been delineated in recent reviews of acquired cutaneous mucinoses, encompassing mucinoses associated with drug exposure including biologic therapies, anti-CSF1R agents, and subcutaneous interferons, as well as mucinosis following physical agents such as mechanical trauma and knee replacement surgery.[16] While these are not always LM per se, they demonstrate that dermal mucin deposition can be triggered by exogenous agents and mechanical insults and suggest analogous mechanisms in LM subtypes where discrete trauma or drug exposure precedes lesion onset.

Age is a clear risk factor; most scleromyxedema patients are diagnosed in their fifth to sixth decade of life, with mean age around 59 years in the multicenter series.[10][12][19] Localized LM may occur in adults or elderly individuals but also presents in infancy in the form of papular mucinosis of infancy and cutaneous mucinosis of infancy.[5][15] Sex distribution appears roughly equal for scleromyxedema, while discrete papular LM in HIV-positive populations may show male predominance, likely reflecting underlying HIV epidemiology rather than a sex-specific predisposition.[1][12][19] Family history does not seem to confer risk, and there is no evidence of consanguinity effects or founder mutations.

### 2.5 Protective Factors and Gene–Environment Interactions

Specific protective factors for LM have not been identified. There are no reports of genetic variants conferring reduced risk of dermal mucinosis in the presence of monoclonal gammopathy or chronic viral infection, and no known environmental exposures that demonstrably protect against LM. Standard measures that reduce risk of plasma cell dyscrasia (e.g., avoidance of certain carcinogens) or chronic infection (e.g., HIV prevention) are likely to decrease LM risk indirectly, but this remains speculative rather than demonstrated.

Gene–environment interaction models are largely conjectural, given the absence of known susceptibility alleles. It is plausible that individual variation in immune regulation, cytokine signaling, or fibroblast responsiveness—perhaps governed by common polymorphisms in genes such as IL1B, TNFA, TGFB1, or extracellular matrix regulators—modulates the likelihood of developing LM in the setting of monoclonal gammopathy or chronic infection. However, no GWAS, PheWAS, or candidate gene studies have been published in LM populations, and environmental triggers such as contaminated L-tryptophan or toxic oil have been implicated mainly through case clustering and temporal association.[7][16][17]

From an ontology perspective, LM’s etiologic profile should be coded as “acquired” (NCIT:C2991) with “association with monoclonal gammopathy” and “association with chronic infection (HIV, HCV)” as high-level risk-factor annotations. Gene–environment interaction fields would note “no data available” or “mechanistic hypotheses only” for current knowledge base entries.

## 3. Phenotypes

### 3.1 Cutaneous Phenotypes: Generalized (Scleromyxedema) and Localized Forms

The hallmark phenotype of LM is cutaneous mucinosis manifesting as papules, nodules, plaques, or diffuse induration. In scleromyxedema, cutaneous manifestations are typically generalized, consisting of numerous 2–3 mm dome-shaped or flat-topped, waxy, slightly red to skin-colored papules and sclerodermoid induration of the skin.[1][4][7][10][19] These papules are closely spaced and often arranged in linear or grouped patterns, particularly on the trunk, face, and extremities, and may coalesce into infiltrated skin with decreased mobility, producing a “mask-like” facies or leonine appearance when facial involvement is pronounced.[1][4][10][19] Over time, thickening and hardening of the skin can lead to decreased range of motion, especially around joints, and may mimic scleroderma clinically.[4][18][19]

Localized LM displays a more restricted distribution of lesions, confined to specific sites such as acral regions, limbs, trunk, or facial areas.[1][5][6][7] Nodular LM presents with skin-colored mucinous nodules on limbs and trunk, usually without diffuse papular eruptions.[9] Discrete papular LM shows scattered erythematous waxy papules of 2–4 mm confined to limited regions, often in association with HIV or HCV infection.[1][3][5] Acral persistent papular mucinosis consists of persistent small papules on the hands and sometimes feet, while self-healing papular mucinosis is characterized by papular eruptions that spontaneously regress over months without scarring.[5][7] Papular mucinosis of infancy and cutaneous mucinosis of infancy present with congenital or early-onset papules and plaques, frequently on trunk and extremities, with variable progression and partial spontaneous resolution.[5][15]

Phenotypically, LM is associated with HPO terms such as “Papule” (HP:0000679), “Nodule” (HP:0001468), “Plaque” (HP:0030448), “Sclerodactyly” (HP:0001057) when fingers become indurated, “Leonine facies” (HP:0000326) in severe facial involvement, and “Cutaneous mucinosis” (HP:0001050).[1][4][5][7][19] Clinical signs include “Waxy skin” and “Skin induration,” which can be mapped to “Skin thickening” (HP:0005310) and “Abnormality of skin consistency” (HP:0001010). Symptom onset in scleromyxedema is typically adult, with insidious development of papules over months, while localized LM can be adult or pediatric onset, including neonatal or infantile cases.[5][12][15]

Severity and progression vary. Scleromyxedema generally evolves slowly and chronically, with progressive papule formation and sclerosis; however, acute exacerbations and dermato-neuro syndrome with rapid neurologic decline have been reported.[4][10][12][19] Localized LM is often mild to moderate, with lesions that may remain stable or regress spontaneously, particularly in self-healing papular mucinosis and some cases of cutaneous mucinosis of infancy.[5][7][15] Frequency among affected individuals is difficult to quantify due to rarity, but within LM cohorts, papular lesions and dermal mucinosis are essentially universal, while specific morphologies (nodular, acral, infantile) vary by subtype.[1][5][9][15]

### 3.2 Extracutaneous Phenotypes in Scleromyxedema and Atypical LM

Extracutaneous manifestations define the systemic burden of scleromyxedema. In the 30-patient multicenter study, 19 patients (63%) had extracutaneous involvement, including neurologic manifestations in 30%, rheumatologic in 23.3%, and cardiac in 20%.[12][13] Neurologic features range from headaches and cognitive changes to seizures and coma in the context of dermato-neuro syndrome, a serious and potentially lethal complication characterized by flu-like prodromes followed by fever, convulsions, and coma.[4][10][12][19] Rheumatologic manifestations include arthralgia, myalgia, and myositis; cardiac involvement can present as heart failure or arrhythmias; gastrointestinal symptoms include dysphagia and esophageal dysmotility; pulmonary manifestations involve restrictive ventilatory defects or interstitial changes; renal involvement may relate to IgA nephropathy or paraprotein-related damage; and ophthalmologic manifestations include visual disturbances and orbital involvement.[3][4][10][12][19]

Atypical localized LM with monoclonal gammopathy or systemic symptoms, as defined by Orphanet (ORPHA:90399), shows systemic features similar to scleromyxedema despite limited skin involvement. These may include dysphagia, hoarseness, pulmonary involvement, carpal tunnel syndrome, myositis without skin sclerosis, or IgA nephropathy in patients with acral persistent papular mucinosis.[3] Thus, in knowledge bases, systemic phenotypes should be associated not only with scleromyxedema but also with atypical LM categories.

Relevant HPO terms include “Seizures” (HP:0001250), “Coma” (HP:0001342), “Myopathy” (HP:0003560), “Arthralgia” (HP:0002829), “Cardiomyopathy” (HP:0001638), “Heart failure” (HP:0001635), “Dysphagia” (HP:0002015), “Restrictive ventilatory defect” (HP:0004873), “IgA nephropathy” (HP:0012229), and “Carpal tunnel syndrome” (HP:0003403).[3][4][12][19] Age of onset for systemic features parallels skin disease onset, typically in middle age, and severity ranges from mild arthralgia to life-threatening neurologic crises. Progression can be insidious, with cumulative organ involvement over years, or acute in dermato-neuro syndrome. Frequency of specific systemic manifestations varies by series, but neurologic and rheumatologic features appear among the most common.[4][12][19]

### 3.3 Laboratory Abnormalities and Histopathologic Phenotypes

Laboratory phenotypes in LM center on paraproteinemia and histologic findings. In scleromyxedema, serum and urine protein electrophoresis with immunofixation typically reveal a monoclonal IgG peak, often lambda light-chain, with or without bone marrow plasma cell proliferation.[1][4][7][10][12][19] Bone marrow biopsy may show increased plasma cells but usually does not meet diagnostic criteria for multiple myeloma at initial LM presentation.[1][10][12] HPO terms such as “Monoclonal gammopathy” (HP:0002910) and “Abnormal immunoglobulin level” (HP:0002715) apply.

Histopathologically, LM is defined by a triad of diffuse mucin deposition, proliferation of irregularly arranged fibroblasts, and increased collagen deposition.[1][4][10][19] Mucin accumulates predominantly in the upper and mid-reticular dermis, separating collagen bundles and appearing as pale basophilic material on routine staining; special stains such as alcian blue at pH 2.5 and colloidal iron confirm acidic mucopolysaccharides, while hyaluronidase digestion can remove hyaluronic acid, verifying its presence.[1][17][19] Congo red and periodic acid–Schiff stains are negative, helping to distinguish mucin from amyloid or glycoprotein deposits.[19] Fibroblasts appear increased in number, with stellate or spindle-shaped morphology and enlarged nuclei, and collagen bundles are thickened and irregularly arranged.[1][4][19] In scleromyxedema, the triad is diffuse and generalized; in localized LM, mucin deposition may be focal or diffuse, with variable fibroblast proliferation.[4][5][6][7][9]

These histologic features map to HPO terms such as “Dermal mucin deposition” (HP:0032463), “Abnormal dermal collagen” (HP:0000950), and “Fibroblast proliferation” (HP:0032464). They also align with GO biological process terms for “extracellular matrix organization” (GO:0030198) and “glycosaminoglycan biosynthetic process” (GO:0006024), and CL cell-type terms for “dermal fibroblast” (CL:0002620).[17][19] Laboratory abnormalities in thyroid function are notably absent; normal thyroid-stimulating hormone and thyroxine levels constitute a diagnostic feature distinguishing LM from thyroid-associated mucinoses.[1][4][7][17][19]

### 3.4 Quality of Life Impact

LM’s impact on quality of life varies widely by subtype. Localized LM often has modest effects, primarily cosmetic or psychosocial, due to visible papules or nodules on exposed skin. Patients may experience pruritus, discomfort, or concern about appearance, but physical functioning is usually preserved, and spontaneous resolution in some variants (self-healing papular mucinosis, cutaneous mucinosis of infancy) mitigates long-term disability.[5][7][15] Formal quality-of-life studies specific to LM are lacking, but generic instruments such as the Dermatology Life Quality Index (DLQI) or SF-36 could be used in future research.

Scleromyxedema, by contrast, can severely compromise daily functioning and well-being. Skin sclerosis around joints reduces mobility and dexterity, facial induration alters appearance and expression, and systemic manifestations such as myopathy, arthralgia, cardiopulmonary compromise, and neurologic episodes can produce significant disability.[4][10][12][19] The unpredictable course and guarded prognosis, including risk of acute dermato-neuro syndrome and hematologic malignancies, contribute to psychological distress and anxiety. In the multicenter series, five of 21 patients with long-term follow-up died over an average 33.5-month period, underscoring substantial disease burden.[12][13] While disease-specific quality-of-life scales have not been validated in LM, mapping to general health dimensions such as physical functioning, role limitations, pain, emotional well-being, and social functioning (as in SF-36 or EQ-5D frameworks) suggests a profound impact in many scleromyxedema cases.

For ontology integration, LM could be associated with “Impaired quality of life” (HP:0011939) and “Functional impairment” (HP:0012385), with severity qualifiers distinguished between localized and generalized forms. Future natural history studies should explicitly measure PROMIS or SF-36 outcomes to quantify this impact.

## 4. Genetic and Molecular Information

### 4.1 Absence of Germline Causal Genes and Variant Profiles

Current evidence supports the view that LM, including scleromyxedema and localized variants, is not driven by inherited pathogenic mutations in specific genes. There are no entries in OMIM or ClinVar linking LM phenotypes to defined germline variants, and familial clusters have not been described.[1][4][12][19] Thus, unlike genodermatoses such as epidermolysis bullosa or Ehlers–Danlos syndromes, LM does not have a recognized monogenic basis or characteristic variant spectrum (missense, frameshift, nonsense, etc.) that can be catalogued with HGNC symbols and ACMG classifications.

From a knowledge base perspective, the “causal gene” field for LM should state “none established” and reference the acquired, non-hereditary nature of the disease. “Somatic variants” may exist within plasma cell clones in associated monoclonal gammopathy or myeloma, but these have not been systematically studied in LM cohorts and are better captured under hematologic disease entries rather than LM itself.[10][12][19] Allele frequencies, penetrance, and expressivity metrics relevant to monogenic disorders are therefore not applicable.

### 4.2 Monoclonal Gammopathy and Immunoglobulin Biology

The most consistent molecular abnormality in scleromyxedema is monoclonal gammopathy, usually IgG lambda. This reflects clonal expansion of B-cell–derived plasma cells producing an immunoglobulin of single heavy- and light-chain isotype, detectable as an M spike on serum protein electrophoresis and immunofixation.[4][7][10][12][19] In the multicenter study, 27 of 30 scleromyxedema patients had detectable monoclonal gammopathy, and two later developed hematologic malignancies (myeloid leukemia and Hodgkin lymphoma), consistent with the recognized progression risk of MGUS.[12][13] Another series cited 83–100% paraproteinemia in scleromyxedema, with progression to multiple myeloma in about 10% of cases.[10]

Immunoglobulins (IG) as molecules can be mapped to UniProt entries for IgG heavy chain and lambda light chain, with GO terms such as “immune response” (GO:0006955) and “humoral immune response mediated by circulating immunoglobulin” (GO:0002925). In LM knowledge bases, the paraprotein could be annotated as a “biomarker” rather than as a causal gene product, using NCIT terms like “Biomarker” (NCIT:C16425) and “Monoclonal Immunoglobulin” (NCIT:C54447). The relationship “LM is associated with monoclonal IgG lambda paraproteinemia” should be encoded with evidence references.[4][10][12][19]

Despite the strong association, an unequivocal causal relationship between paraproteinemia and LM manifestations has not been established. Some individuals with MGUS never develop LM, and experimental data suggest that non-paraprotein serum factors may be responsible for fibroblast activation.[10][19] Scleromyxedema thus occupies an intermediate conceptual space between purely dermatologic mucinosis and systemic plasma cell disorders, reflecting a pathobiologic linkage without a defined genetic cause.

### 4.3 Fibroblast Biology, Glycosaminoglycans, and Extracellular Matrix

Mechanistically, LM involves dermal fibroblast activation and altered extracellular matrix (ECM) metabolism. In vitro studies have shown that fibroblasts from scleromyxedema patients synthesize more hyaluronic acid than normal controls and that patient serum stimulates proliferation of dermal fibroblasts and increased production of hyaluronic acid and prostaglandin E.[10] These observations align with GO processes such as “glycosaminoglycan biosynthetic process” (GO:0006024), “hyaluronan biosynthetic process” (GO:0030213), and “fibroblast proliferation” (GO:0048147), and CL terms for “dermal fibroblast” (CL:0002620).[17][19]

Mucin deposition primarily reflects accumulation of hyaluronic acid and dermatan sulfate, which can be annotated using CHEBI identifiers (e.g., CHEBI:16337 for hyaluronic acid, CHEBI:27650 for dermatan sulfate). Histologic evidence shows these glycosaminoglycans filling spaces between collagen fibers in the dermis, causing separation and altered architecture.[1][4][17][19] Increased collagen deposition and irregular bundling further contribute to dermal thickening and sclerosis, mapping to GO terms such as “collagen fibril organization” (GO:0030199) and “extracellular matrix organization” (GO:0030198).[17][19]

Deranged ECM metabolism likely involves upregulation of enzymes like hyaluronan synthases (HAS1–3) and downregulation or inadequate activity of hyaluronidases, as well as altered production of collagens (COL1A1, COL1A2, COL3A1) and matrix metalloproteinases (MMPs). However, specific gene expression profiles have not been published for LM skin, and there are no transcriptomic datasets in GEO or ArrayExpress explicitly labeled as LM.[16][19] The molecular profiling section in the knowledge base should therefore note “no disease-specific transcriptomics or proteomics datasets available; mechanistic inferences based on general fibroblast and ECM biology.”

### 4.4 Cytokine Networks and Immune Modulation

The involvement of circulating cytokines—IL-1, TNF-α, TGF-β—as stimulators of mucin production is a key molecular hypothesis. These cytokines are known to upregulate glycosaminoglycan synthesis and fibroblast proliferation in various systems, including in scleroderma and other fibrotic disorders.[1][10][17][19] In LM, in vitro serum stimulation of fibroblasts suggests that patient sera contain soluble factors that activate these pathways; though the precise cytokine levels in LM have not been systematically quantified, IL-1, TNF-α, and TGF-β have been repeatedly cited as likely mediators.[1][10][19]

These cytokines map to UniProt entries (e.g., IL1B: P01584, TNF: P01375, TGFB1: P01137) and GO terms such as “positive regulation of fibroblast proliferation” (GO:0048147), “positive regulation of glycosaminoglycan biosynthetic process” (GO:0010628), and “regulation of extracellular matrix organization” (GO:0030198). Immune involvement could be annotated under “inflammatory response” (GO:0006954) and “immune system process” (GO:0002376), and cell types such as “T cell” (CL:0000084) and “monocyte” (CL:0000576) may participate in cytokine production. However, direct LM-specific immune profiling (e.g., single-cell RNA-seq of lesional skin) is not available.

### 4.5 Epigenetics, Chromosomal Abnormalities, and Multi-omics

There are no published epigenetic studies—DNA methylation profiling, histone modification maps, chromatin accessibility assays—specifically in LM skin or associated plasma cells. Likewise, chromosomal abnormalities beyond those seen in generalized MGUS/myeloma (e.g., 13q deletion, t(4;14)) have not been reported as LM-specific.[10][12][19] Without dedicated multi-omics datasets, LM’s epigenomic and structural genomic features remain unknown.

Consequently, knowledge base entries should note “no LM-specific epigenetic or chromosomal abnormality data” and avoid inferring mechanisms beyond generic MGUS or connective tissue disease knowledge. Molecular profiling fields for transcriptomics, proteomics, metabolomics, lipidomics, and multi-omics integration should state “data not available; research gap.”

## 5. Environmental Information

### 5.1 Environmental and Toxic Exposures

Several environmental factors have been implicated in localized LM or broader cutaneous mucinoses. DermNet and Orphanet note that localized LM has been reported in association with exposure to toxic oil and contaminated L-tryptophan, as well as HIV infection and hepatitis C virus.[5][7] The contaminated L-tryptophan episodes recall the eosinophilia–myalgia syndrome outbreaks in which toxic tryptophan derivatives caused systemic and cutaneous manifestations, including mucinosis. While LM-specific case details are sparse, these associations suggest that xenobiotics capable of altering immune regulation and fibroblast activity may trigger dermal mucinosis.

Recent reviews of acquired cutaneous mucinoses describe “toxic dermal mucinoses” as a distinct category of mucin deposition disorders associated with drug exposure, including biologic therapies and anti-CSF1R agents, as well as with mechanical trauma and surgical implants.[16] Nodular mucinosis of the breast, obesity-associated lymphedematous mucinosis, and pretibial stasis mucinosis are examples wherein local environmental or structural factors—obesity-related lymphedema, venous stasis, or chronic mechanical stress—contribute to mucin deposition.[16] While these conditions are not LM per se, they illustrate the broader principle that environmental influences can drive cutaneous mucinosis.

In LM knowledge bases, environmental factor annotations should include “contaminated L-tryptophan exposure” (CHEBI:18050, tryptophan) and “toxic oil exposure” under general xenobiotic categories, with evidence status “case reports; causality not definitively established.” The presence of HIV and HCV infection should be flagged as infectious risk factors, with NCBI Taxon identifiers for human immunodeficiency virus (taxon:11676) and hepatitis C virus (taxon:11103).[1][7][16] Occupational exposures do not appear prominently in LM literature, though environmental factors such as UV radiation or chemical irritants might theoretically modulate disease course.

### 5.2 Lifestyle Factors

Lifestyle factors such as smoking, diet, exercise, and alcohol consumption have not been systematically studied in LM. Given the rarity of the disease and the dominance of case-based evidence, there is no established link between specific lifestyle patterns and LM onset or severity. However, lifestyle factors that influence plasma cell dyscrasia risk (e.g., obesity, chronic inflammatory states) or infection risk (e.g., unsafe sexual practices, injection drug use) may indirectly affect LM incidence by modulating underlying monoclonal gammopathy or chronic viral infections.

On a pragmatic level, LM patients may be advised to follow general health recommendations—balanced diet, regular exercise, smoking cessation—but these constitute general preventive medicine rather than LM-specific protective factors. Knowledge bases should therefore mark lifestyle factor fields as “no LM-specific data; general health measures recommended by extrapolation.”

### 5.3 Infectious Agents and Immune Context

As noted, discrete papular LM is strongly associated with HIV infection in several series, and hepatitis C has been reported in Japanese patients with discrete papular LM.[1] HIV infection leads to profound immune dysregulation, including chronic immune activation, altered cytokine production, and increased susceptibility to opportunistic infections, all of which could promote dermal fibroblast activation and mucin production. Hepatitis C chronic infection similarly drives systemic immune responses and may produce cryoglobulinemia and other immune complex phenomena that could influence dermal vasculature and fibroblast function.

These infectious agents can be annotated in LM knowledge bases with NCBI Taxon identifiers and linked to “association with LM” with evidence type “case reports/series.” HPO terms such as “Human immunodeficiency virus infection” (HP:0004823) and “Hepatitis C” (HP:0002615) may be attached as comorbid conditions. Other infectious agents—bacteria, fungi, parasites—have not been specifically implicated in LM pathogenesis beyond occasional case-level coincidences.

## 6. Mechanism / Pathophysiology

### 6.1 Ordered Causal Chain from Initiating Lesions to Clinical Manifestations

To conform with the requirement for an ordered causal chain while avoiding list formatting, the mechanistic sequence for scleromyxedema and LM can be presented in tabular form, with each row representing one step leading to the next.

| Step | Mechanistic description |
|------|-------------------------|
| 1 | Acquired monoclonal gammopathy (IgG lambda or kappa) or chronic infection/immune dysregulation leads to production of abnormal serum factors, including paraprotein and pro-inflammatory/pro-fibrotic cytokines (IL-1, TNF-α, TGF-β), as inferred from clinical associations and in vitro serum effects.[1][2][4][10][12][19] |
| 2 | These circulating factors lead to activation and proliferation of dermal fibroblasts, as demonstrated by increased fibroblast DNA synthesis and proliferation when exposed to patient sera in vitro.[1][10][19] |
| 3 | Activated fibroblasts lead to upregulated synthesis and secretion of acidic glycosaminoglycans (hyaluronic acid, dermatan sulfate) and altered collagen production, resulting in mucin accumulation and ECM remodeling in the upper and mid-reticular dermis, as shown by histologic triad and mucin staining characteristics.[1][4][10][17][19] |
| 4 | Dermal mucin deposition and collagen thickening lead to separation and reorganization of collagen bundles, causing skin thickening, induration, and the clinical appearance of waxy papules, nodules, plaques, and sclerodermoid skin changes.[1][4][7][10][19] |
| 5 | Progressive dermal fibrosis and induration lead to decreased skin elasticity and joint mobility, contributing to sclerodactyly, mask-like facies, and functional impairment, in analogy to scleroderma and supported by clinical observations.[4][10][18][19] |
| 6 | Systemic dissemination or systemic effects of circulating factors lead to involvement of other organs (neurologic, rheumatologic, cardiac, pulmonary, renal, gastrointestinal), causing manifestations such as myopathy, arthralgia, dysphagia, cardiomyopathy, restrictive lung disease, IgA nephropathy, and dermato-neuro syndrome.[3][4][10][12][19] |
| 7 | Chronic persistence of mucin deposition and fibroblast activation leads to a long-term, unpredictable disease course with risk of progression to hematologic malignancies (multiple myeloma, leukemia, lymphoma) and acute complications (dermato-neuro syndrome), as documented in multicenter series.[10][12][19] |
| 8 | In localized LM, similar dermal fibroblast activation and mucin deposition occur but remain anatomically confined, possibly due to localized triggering factors (trauma, acral microenvironment, localized infection) and lack of systemic paraproteinemia, resulting in milder, often self-limited clinical phenotypes.[1][3][5][7][15][16] |

Where indicated, several steps are inferred based on analogy to other fibromucinous and fibrotic diseases rather than directly demonstrated in LM; explicit experimental data exist for steps involving serum stimulation of fibroblasts and histologic demonstration of mucin and collagen changes.[1][10][19]

### 6.2 Molecular Pathways and Cellular Processes

At the molecular level, LM’s pathophysiology revolves around fibroblast activation, glycosaminoglycan biosynthesis, and ECM remodeling. Cytokine-driven signaling pathways such as TGF-β/SMAD, NF-κB (via TNF-α and IL-1), and possibly JAK/STAT play roles in upregulating ECM gene expression and cell proliferation, as inferred from general fibroblast biology and from the recognized pro-fibrotic and pro-inflammatory functions of these cytokines.[1][10][17][19] TGF-β is a potent inducer of collagen synthesis and glycosaminoglycan production in fibroblasts, signaling via the canonical SMAD2/3/4 pathway to activate transcription of COL1A1, COL1A2, and HAS genes. IL-1 and TNF-α, through activation of NF-κB and AP-1, promote expression of matrix metalloproteinases and cytokines that modulate ECM turnover and inflammation.

Cellular processes implicated include fibroblast proliferation, increased ECM synthesis, and altered ECM degradation. Fibroblasts in LM dermis show increased number and morphological activation (stellate shapes, enlarged nuclei), consistent with a proliferative and synthetic phenotype.[1][4][19] Mucin deposition indicates increased synthesis of glycosaminoglycans, while collagen thickening indicates increased collagen synthesis and altered crosslinking. These processes map to GO terms such as “positive regulation of fibroblast proliferation” (GO:0048147), “extracellular matrix organization” (GO:0030198), “glycosaminoglycan biosynthetic process” (GO:0006024), and “collagen fibril organization” (GO:0030199).

Immune cells—T cells, B cells, monocytes/macrophages—likely contribute to cytokine production, though direct immunophenotyping of LM lesions has not been systematically reported. Some histologic descriptions mention lympho-plasmacytoid infiltrates in skin and bone marrow, suggesting participation of plasmacytoid cells and plasma cells in local immune reactions.[2][10][17] These could be mapped to CL terms such as “plasma cell” (CL:0000786) and “plasmacytoid dendritic cell” (CL:0000784), though specificity is uncertain.

### 6.3 Protein Dysfunction and Biochemical Abnormalities

LM does not feature a single dysfunctional protein in the sense of misfolding or enzyme deficiency; instead, it reflects quantitative and qualitative changes in ECM and cytokine milieu. Biochemical abnormalities include increased dermal content of hyaluronic acid and dermatan sulfate, increased collagen deposition, and possibly altered prostaglandin E production by fibroblasts.[1][10][17][19] Hyaluronic acid, a linear glycosaminoglycan composed of repeating disaccharide units of glucuronic acid and N-acetylglucosamine, contributes to dermal hydration and viscoelastic properties; excess accumulation increases tissue volume and pliability but also can contribute to stiffness when combined with fibrotic collagen changes.[17][19]

Prostaglandin E production may modulate local vasodilation, inflammation, and pain, though its role in LM remains incompletely characterized.[10] There is no evidence of specific enzyme deficiencies (e.g., lysosomal storage diseases) or receptor dysfunction in LM, and ion channel abnormalities are not implicated.

Mucin staining properties—alcian blue positivity at pH 2.5, hyaluronidase digestion, negative Congo red and PAS—reflect biochemical composition dominated by acidic glycosaminoglycans rather than neutral glycoproteins or amyloid.[1][17][19] These histochemical profiles can be encoded in pathology knowledge bases as diagnostic features.

### 6.4 Immune System Involvement and Tissue Damage Mechanisms

Immune system involvement in LM is primarily through cytokine-mediated fibroblast activation and potential autoantibody or paraprotein effects. Monoclonal IgG may form immune complexes or bind to skin antigens, though direct evidence of autoantibody targeting in LM is lacking.[10][12][19] Chronic immune activation in HIV and HCV infection likely contributes to cytokine production and mucin deposition in localized LM.[1][16]

Tissue damage mechanisms in LM include fibrosis, mechanical stiffening, and organ dysfunction due to ECM accumulation in skin and possibly other tissues. In scleromyxedema, dermal fibrosis and mucinosis lead to structural damage manifested as reduced skin elasticity, joint contractures, and altered facial features.[4][10][19] Organ-level damage—e.g., myopathy, cardiomyopathy, restrictive lung disease—is thought to arise from similar fibromucinous processes in muscle, myocardium, and pulmonary interstitium, though biopsy confirmation is limited.[3][4][12][19] Neurologic damage in dermato-neuro syndrome may involve inflammatory or metabolic mechanisms rather than direct mucin deposition, and its pathophysiology remains poorly understood.[4][12][19]

From an ontology standpoint, tissue damage processes can be mapped to GO terms such as “fibrosis” (GO:0008064), “positive regulation of tissue remodeling” (GO:0030198), and “inflammatory response” (GO:0006954). CL terms for affected cell types include fibroblasts, endothelial cells, myocytes, and neurons, with UBERON terms for skin (UBERON:0002097), dermis (UBERON:0002072), skeletal muscle (UBERON:0001134), heart (UBERON:0000948), and lung (UBERON:0002048).

### 6.5 Epigenetic Changes and Molecular Profiling

As noted above, no LM-specific epigenetic or multi-omics datasets are currently available. It is plausible that epigenetic reprogramming in dermal fibroblasts—DNA methylation changes in promoters of ECM genes, histone modifications in cytokine-responsive regulatory regions—contributes to sustained fibroblast activation, as seen in scleroderma and other fibrotic diseases. However, without direct data, these remain hypotheses that should be flagged as inferred mechanisms.

Similarly, transcriptomic or proteomic profiling of LM lesions has not been reported. Given this gap, molecular profiling fields should emphasize the need for future RNA-seq, proteomics, and single-cell analysis to delineate the full landscape of fibroblast and immune cell states in LM.

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

The primary organ affected in LM is the skin, specifically the dermis. Clinically, lesions most commonly involve the trunk, extremities, and face, though any cutaneous region can be affected.[1][4][7][10][19] UBERON terms such as “skin” (UBERON:0002097), “integumentary system” (UBERON:0002413), “upper limb skin” (UBERON:0001490), “lower limb skin” (UBERON:0001511), and “facial skin” are appropriate. In acral persistent papular mucinosis, involvement centers on acral regions such as hands (UBERON:0002371) and feet (UBERON:0002375).[5][7]

In scleromyxedema and atypical LM, multiple organ systems may be involved. Neurologic involvement includes brain and central nervous system (UBERON:0000955), manifesting as seizures, encephalopathy, or dermato-neuro syndrome.[4][12][19] Rheumatologic involvement includes joints (UBERON:0001486) and muscles (UBERON:0001134), presenting as arthralgia and myopathy.[3][4][12] Cardiovascular involvement affects heart (UBERON:0000948) and vasculature (UBERON:0004535), causing cardiomyopathy and heart failure.[4][12][19] Pulmonary involvement affects lungs (UBERON:0002048) and respiratory system (UBERON:0001004), leading to restrictive ventilatory defects or interstitial disease.[3][4][12] Renal involvement includes kidney (UBERON:0002113), particularly in IgA nephropathy.[3] Gastrointestinal involvement affects esophagus (UBERON:0001043) and stomach (UBERON:0000945), causing dysphagia and esophageal dysmotility.[3][4] Ophthalmologic involvement may affect orbit and retina (UBERON:0002111), though details are limited.[4][12][19]

Secondary organ involvement occurs through complications such as hemato-logic malignancies (bone marrow, UBERON:0002398), infections, and heart failure. Knowledge bases should encode these organ involvements with qualitative frequencies (e.g., neurologic ~30%, rheumatologic ~23%, cardiac ~20% in scleromyxedema cohorts).[12][13]

### 7.2 Tissue- and Cell-Level Involvement

At the tissue level, LM predominantly affects connective tissue within the dermis, comprising fibroblasts, collagen fibers, ground substance (glycosaminoglycans), and capillaries.[1][4][17][19] Epidermis is typically spared, although in some mucinoses epidermal involvement can occur; LM is generally classified as dermal mucinosis.[14][17] Other tissues involved in systemic LM include skeletal muscle, myocardium, pulmonary interstitium, renal glomeruli (in IgA nephropathy), and gastrointestinal smooth muscle and connective tissue.[3][4][12][19]

Cell types involved include dermal fibroblasts (CL:0002620), plasma cells (CL:0000786) producing monoclonal immunoglobulin, endothelial cells (CL:0000115), pericytes (CL:0000669), immune cells (T cells, B cells, monocytes/macrophages, CL:0000084, CL:0000236, CL:0000576), and possibly smooth muscle cells (CL:0000136) in systemic involvement.[17][19] Histologic descriptions mention irregular fibroblast proliferation, lympho-plasmacytoid infiltrates, and increased collagen deposition, indicating interplay between mesenchymal cells and immune cells.[1][2][4][19] In knowledge bases, the “cell types” field should list these with qualifiers such as “primary effector (fibroblasts)” and “associated (plasma cells, immune cells).”

### 7.3 Subcellular Level and Localization

Subcellular compartments implicated in LM include the extracellular matrix (ECM) of the dermis, where mucin accumulates, and the cytoplasm and nucleus of fibroblasts, where ECM components are synthesized and gene expression changes occur. GO Cellular Component terms such as “extracellular region” (GO:0005576), “collagen-containing extracellular matrix” (GO:0062023), and “cytoplasm” (GO:0005737) apply.[17][19] Fibroblast secretory pathways—endoplasmic reticulum (GO:0005783), Golgi apparatus (GO:0005794)—are involved in synthesizing and processing collagen and glycosaminoglycans.

Localization of skin lesions in LM is often symmetric and bilateral, particularly in scleromyxedema, affecting both sides of the face, trunk, and limbs.[4][10][19] Acral persistent papular mucinosis and nodular LM may show more localized, asymmetric distributions on extremities.[5][9] Lateralization is not a defining feature, though some case reports mention unilateral or segmental patterns. Knowledge bases can annotate “distribution: generalized symmetric (scleromyxedema), localized (acral, nodular, discrete), segmental or unilateral (rare).”

## 8. Temporal Development

### 8.1 Age of Onset and Pattern of Onset

In scleromyxedema, age of onset is typically in the fifth or sixth decade of life. The multicenter study reported mean age at diagnosis of 59 years, with a mean delay of nine months between disease onset and diagnosis.[10][12][19] Most patients are middle-aged adults, though cases in younger and older adults have been described. Onset is usually insidious, with gradual appearance of papules over months, sometimes initially confined to one region before generalizing.[4][10][12][19] HPO terms such as “Adult onset” (HP:0003581) apply.

Localized LM shows broader age distribution. Nodular LM is generally adult onset, while acral persistent papular mucinosis often presents in adults or elderly individuals.[5][9] Papular mucinosis of infancy and cutaneous mucinosis of infancy present at birth or in early childhood, with congenital papules and plaques.[5][15] Onset patterns in these pediatric variants may be progressive, eruptive, or spontaneously involuting, as demonstrated in a case report of cutaneous mucinosis of infancy where congenital papules increased in size and number over two years while some lesions simultaneously regressed.[15]

Onset pattern in LM is almost always chronic/insidious rather than acute, except for dermato-neuro syndrome in scleromyxedema, which can develop acutely on a background of chronic disease.[4][10][12][19] Knowledge bases should encode this as “chronic, insidious onset” with “acute complication (dermato-neuro syndrome) possible” in scleromyxedema.

### 8.2 Disease Progression and Course

Scleromyxedema is characterized by a chronic, unpredictable course. In the multicenter study, 21 patients were followed for a mean of 33.5 months; at that time, 16 were alive (12 with active skin disease, 4 in cutaneous remission), and five had died—two due to dermato-neuro syndrome and one each from myeloid leukemia, Hodgkin lymphoma, and myocardial insufficiency.[12][13] This indicates substantial morbidity and mortality, with incomplete remission rates despite treatment. Authors concluded that “there is no specific definitive treatment” and that IVIG induces complete remission in only a minority of patients, with maintenance infusions required to sustain response.[12][13][19][20]

Progression in scleromyxedema involves gradual expansion of papular eruptions, increased skin induration, and emergence or worsening of systemic manifestations. Some patients experience periods of partial remission, especially under IVIG, thalidomide, or lenalidomide therapy, but relapses are common upon discontinuation.[12][19][20] The disease course pattern can therefore be described as chronic relapsing–remitting with progressive potential and risk of acute neurologic crises.

Localized LM has a more favorable course. Many localized LM variants remain stable over time without progression to generalized disease or systemic involvement.[1][5][6][7] Spontaneous resolution is particularly common in self-healing papular mucinosis and has been reported in localized LM even in HIV-positive patients.[6][7] Cutaneous mucinosis of infancy has traditionally been considered persistent, but cases with spontaneous regression of some lesions, stable others, and emergence of new papules demonstrate a complex pattern of progressive, eruptive, and involuting lesions coexisting over time.[15] Overall, localized LM can be described as chronic but often self-limited, with variable progression and high likelihood of at least partial regression.

From a staging perspective, LM does not have formal stages akin to cancer staging. Clinical stage descriptors could be conceptualized as early localized (limited papules), generalized cutaneous (multiple widespread papules and induration), and systemic (with extracutaneous organ involvement), but these are not codified. Disease duration is typically years in scleromyxedema and can be months to years in localized LM, with self-healing variants resolving within months.

### 8.3 Remission Patterns and Critical Periods

Remission patterns in LM vary by subtype and treatment. In localized LM, spontaneous remission is common in self-healing papular mucinosis and reported in cutaneous mucinosis of infancy, sometimes without any therapy.[5][7][15] Topical treatments may accelerate regression, but their impact is difficult to quantify. In scleromyxedema, IVIG therapy induces complete remission in about 13% (4 of 30 patients) and partial remission in 30% (9 of 30 patients) in the multicenter series, with mean treatment duration of two years.[12][13] These remissions are not permanent; maintenance IVIG infusions are typically required, and discontinuation often leads to relapse.[12][19][20]

Other therapies, such as thalidomide, lenalidomide, melphalan, and phototherapy, can induce partial remissions but are limited by toxicity, incomplete efficacy, and relapse risk.[8][10][19][20] A critical period for intervention may be early in the disease course, before extensive organ involvement or dermato-neuro syndrome develops. Timely recognition of LM in patients with monoclonal gammopathy may allow early IVIG or immunomodulatory therapy to prevent systemic complications, though formal data on timing effects are lacking.

From a prevention and management standpoint, critical periods include onset of neurologic symptoms in scleromyxedema, which should prompt urgent evaluation and management to reduce risk of dermato-neuro syndrome and death.[4][12][19] Early detection of hematologic progression (MGUS to myeloma or leukemia) also represents a critical window for systemic therapy.

## 9. Inheritance and Population

### 9.1 Epidemiology: Prevalence and Incidence

LM is an ultra-rare disease. Orphanet notes that localized LM with monoclonal gammopathy or systemic symptoms has a prevalence of less than 1 per 1,000,000, reflecting its exceptional rarity.[3] Localized LM as a group is categorized as a rare disorder, though specific prevalence numbers are not provided, likely due to limited case ascertainment.[5][9] Scleromyxedema is similarly extremely rare; the multicenter study’s 30 patients were collected from multiple centers over time, highlighting the scarcity of cases.[12][13][19] Population-based incidence estimates are not available.

Given this, LM’s epidemiology in global burden of disease or large registries (CDC, WHO) is effectively unknown; cases appear primarily in dermatology and hematology centers. Knowledge bases should annotate LM as “ultra-rare” or “rare” with prevalence <1/1,000,000 for atypical localized forms and similar order of magnitude for scleromyxedema, based on Orphanet and case series.[3][5][12][19]

### 9.2 Inheritance Patterns and Genetic Characteristics

LM is acquired and non-hereditary. No inheritance pattern—autosomal dominant, recessive, X-linked, mitochondrial—has been identified, and familial clustering has not been reported in the literature.[1][4][12][19] Penetrance and expressivity concepts relevant to Mendelian disorders do not apply. There is no evidence of genetic anticipation, germline mosaicism, or founder effects.

Consanguinity has not been mentioned as a factor in LM case reports, unlike some recessive dermatoses. Carrier frequency is not defined because there is no known germline causal allele. Thus LM should be classified in knowledge bases under “acquired disorders” rather than “hereditary diseases.”

### 9.3 Population Demographics, Sex Ratio, and Age Distribution

Scleromyxedema shows no strong sex predilection. In the multicenter cohort, 17 men and 13 women were identified, yielding a male:female ratio of approximately 1.3:1, which is close to parity.[12][13][19] Age distribution centers on middle age, with mean age at diagnosis of 59 years, though individual ages ranged across mid-adulthood and later adult life.[12][13] Localized LM may occur across a wider age spectrum, including infancy (papular mucinosis of infancy, cutaneous mucinosis of infancy), younger adults (acral persistent papular mucinosis, discrete papular LM), and elderly individuals.[5][9][15]

Ethnic and geographic distribution are poorly characterized. Case reports and series originate from Europe, North America, Asia, and other regions, but no region appears to have markedly increased prevalence.[1][4][10][12][14][16][19] Discrete papular LM associated with HIV may appear more frequently in regions with high HIV prevalence, but LM itself has not been shown to be endemic. Knowledge bases should annotate LM as “occurs worldwide; no known ethnic predilection; case-based distribution.”

## 10. Diagnostics

### 10.1 Clinical and Laboratory Tests

Diagnosis of LM relies on a combination of clinical examination, histopathology, and laboratory assessment of paraproteinemia and thyroid function. Clinically, LM is suspected in patients with waxy papular eruptions, nodules, plaques, or sclerodermoid induration, especially when lesions appear in a generalized pattern or in localized acral or nodular configurations consistent with known LM subtypes.[1][4][6][7][10][19] The presence of normal thyroid function is essential in distinguishing LM from generalized or pretibial myxedema related to hypothyroidism.[1][4][7][17][19] Thus, measurement of serum thyroid-stimulating hormone (TSH) and thyroxine (T4) is a standard diagnostic test, with normal results expected in LM.

Serum and urine protein electrophoresis with immunofixation are performed to detect monoclonal gammopathy. In scleromyxedema, these tests typically reveal an IgG monoclonal spike, often lambda light-chain, with corresponding immunofixation patterns.[1][4][7][10][12][19] Bone marrow biopsy may be conducted to assess plasma cell burden and to exclude overt multiple myeloma or other hematologic malignancies.[10][12][19] Additional laboratory tests may include complete blood count, renal and liver function panels, autoantibody screens (e.g., antinuclear factor), and viral serologies (HIV, HCV) depending on clinical context.[1][7][16][17]

In atypical localized LM with systemic symptoms, laboratory tests may reveal IgA nephropathy, paraproteinemia, or myositis markers. Echocardiogram, pulmonary function tests, and imaging studies (e.g., chest X-ray, CT, MRI) can be used to evaluate systemic organ involvement.[1][3][4][12][19] Electrophysiology (EEG, EMG) may be required in dermato-neuro syndrome or myopathy assessment.[4][12][19]

### 10.2 Histopathology and Pathology Findings

Skin biopsy is the cornerstone diagnostic test for LM. Histologic examination reveals the triad that defines LM: diffuse dermal mucin deposition, proliferation of irregularly arranged fibroblasts, and increased collagen deposition.[1][4][10][19] Mucin appears as pale basophilic material between collagen bundles in the upper and mid-reticular dermis on hematoxylin–eosin staining, with sparing of the epidermis.[1][4][17][19] Special stains using alcian blue at pH 2.5 and colloidal iron demonstrate acidic mucopolysaccharides; hyaluronidase digestion confirms hyaluronic acid composition, while Congo red and PAS negativity exclude amyloid and neutral glycoproteins.[17][19]

Fibroblasts are increased in number, often with large stellate or spindle-shaped nuclei, and collagen bundles are thickened and irregularly arranged.[1][4][19] In some cases, an interstitial granuloma annulare-like pattern has been described, with mucin deposition and histiocytic infiltrates reminiscent of granuloma annulare.[4] Lympho-plasmacytoid infiltrates may be present in the dermis, reflecting immune participation.[2][10][17] In localized LM, mucin deposition may be focal or diffuse, and fibroblast proliferation can be less pronounced; nodular LM shows mucinous nodules with mucin and fibroblast components.[5][9]

Pathology findings can be encoded in SNOMED CT using diagnostic codes for “cutaneous mucinosis” and “dermal mucin deposition.” Knowledge bases should note the requirement for special stains to confirm mucin and recommend hyaluronidase digestion in equivocal cases.

### 10.3 Clinical Criteria and Classification

Diagnostic criteria for scleromyxedema have been defined by Rongioletti, Rebora, and subsequent consensus. They include: (1) generalized papular and sclerodermoid eruption; (2) histologic triad of mucin deposition, fibroblast proliferation, and fibrosis; (3) monoclonal gammopathy; and (4) absence of thyroid disease.[1][4][6][10][19] A recent consensus states that at least three of these four criteria are necessary to confirm scleromyxedema, acknowledging that rare cases may lack one feature.[19] Localized LM criteria include: (1) papular or nodular/plaque eruption; (2) mucin deposition with variable fibroblast proliferation; and (

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 84 |
| Resolved | 78 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 53 |
| Terms named correctly | 18 |
| Terms named as a **different** term | 27 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001050` (2 mentions) - the report calls it "Cutaneous mucinosis"; HP calls it **Plethora**
- `HP:0000679` (2 mentions) - the report calls it "Papule"; HP calls it **Taurodontia**
- `HP:0001052` (1 mention) - the report calls it "Sclerodermatous skin lesions"; HP calls it **Nevus flammeus**
- `NCIT:C2991` (1 mention) - the report calls it "acquired"; NCIT calls it **Disease or Disorder**
- `HP:0001468` (1 mention) - the report calls it "Nodule"; HP calls it **Aplasia/Hypoplasia involving the musculature of the upper arm**
- `HP:0030448` (1 mention) - the report calls it "Plaque"; HP calls it **Soft tissue sarcoma**
- `HP:0001057` (1 mention) - the report calls it "Sclerodactyly"; HP calls it **Aplasia cutis congenita**
- `HP:0000326` (1 mention) - the report calls it "Leonine facies"; HP calls it **Abnormal maxilla morphology**
- `HP:0005310` (1 mention) - the report calls it "Skin thickening"; HP calls it **Large vessel vasculitis**
- `HP:0001010` (1 mention) - the report calls it "Abnormality of skin consistency"; HP calls it **Hypopigmentation of the skin**
- `HP:0001342` (1 mention) - the report calls it "Coma"; HP calls it **Cerebral hemorrhage**
- `HP:0003560` (1 mention) - the report calls it "Myopathy"; HP calls it **Muscular dystrophy**
- `HP:0012229` (1 mention) - the report calls it "IgA nephropathy"; HP calls it **CSF pleocytosis**
- `HP:0003403` (1 mention) - the report calls it "Carpal tunnel syndrome"; HP calls it **EMG: decremental response of compound muscle action potential to repetitive nerve stimulation**
- `HP:0002910` (1 mention) - the report calls it "Monoclonal gammopathy"; HP calls it **Elevated circulating hepatic transaminase concentration**
- `HP:0032463` (1 mention) - the report calls it "Dermal mucin deposition"; HP calls it **Reduced circulating fibronectin level**
- `HP:0032464` (1 mention) - the report calls it "Fibroblast proliferation"; HP calls it **Ureteral hypoplasia**
- `GO:0030198` (5 mentions) - the report calls it "extracellular matrix organization", "regulation of extracellular matrix organization", "positive regulation of tissue remodeling"; GO calls it **extracellular matrix organization**
- `HP:0011939` (1 mention) - the report calls it "Impaired quality of life"; HP calls it **3-4 finger cutaneous syndactyly**
- `HP:0012385` (1 mention) - the report calls it "Functional impairment"; HP calls it **Camptodactyly**
- `NCIT:C16425` (1 mention) - the report calls it "Biomarker"; NCIT calls it **Child Psychiatry**
- `NCIT:C54447` (1 mention) - the report calls it "Monoclonal Immunoglobulin"; NCIT calls it **FDA Individual Case Safety Report Terminology**
- `HP:0004823` (1 mention) - the report calls it "Human immunodeficiency virus infection"; HP calls it **Anisopoikilocytosis**
- `HP:0002615` (1 mention) - the report calls it "Hepatitis C"; HP calls it **Hypotension**
- `GO:0008064` (1 mention) - the report calls it "fibrosis"; GO calls it **regulation of actin polymerization or depolymerization**
- `UBERON:0002413` (1 mention) - the report calls it "integumentary system"; UBERON calls it **cervical vertebra**
- `UBERON:0001490` (1 mention) - the report calls it "upper limb skin"; UBERON calls it **elbow joint**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000950` (2 mentions), reported as "Abnormal dermal collagen" - HP does not contain this term
- `HP:0004873` (1 mention), reported as "Restrictive ventilatory defect" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0062023` (obsolete collagen-containing extracellular matrix) (1 mention) - replaced by `GO:0031012`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002715` (1 mention) - the report calls it "Abnormal immunoglobulin level"; HP calls it **Abnormality of the immune system**
- `CL:0002620` (3 mentions) - the report calls it "dermal fibroblast"; CL calls it **skin fibroblast**
- `GO:0002925` (1 mention) - the report calls it "humoral immune response mediated by circulating immunoglobulin"; GO calls it **positive regulation of humoral immune response mediated by circulating immunoglobulin**, and lists "activation of humoral immune response mediated by circulating immunoglobulin" among its other names
- `GO:0048147` (3 mentions) - the report calls it "fibroblast proliferation", "positive regulation of fibroblast proliferation"; GO calls it **negative regulation of fibroblast proliferation**, and lists "inhibition of fibroblast proliferation" among its other names
- `GO:0010628` (1 mention) - the report calls it "positive regulation of glycosaminoglycan biosynthetic process"; GO calls it **positive regulation of gene expression**
- `UBERON:0002097` (2 mentions) - the report calls it "skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `UBERON:0001511` (1 mention) - the report calls it "lower limb skin"; UBERON calls it **skin of leg**, and lists "leg skin" among its other names
- `GO:0062023` (1 mention) - the report calls it "collagen-containing extracellular matrix"; GO calls it **obsolete collagen-containing extracellular matrix**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0030198` - called "extracellular matrix organization", "regulation of extracellular matrix organization", "positive regulation of tissue remodeling"
- `GO:0048147` - called "fibroblast proliferation", "positive regulation of fibroblast proliferation"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.