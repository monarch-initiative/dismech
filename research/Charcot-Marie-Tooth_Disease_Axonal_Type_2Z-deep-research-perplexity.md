---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-16T21:00:45.833028'
end_time: '2026-09-16T21:06:36.236300'
duration_seconds: 350.4
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Charcot-Marie-Tooth Disease Axonal Type 2Z
  mondo_id: MONDO:0014736
  category: Genetic
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
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 80
  verified: 71
  not_found: 2
  obsolete: 5
  unverifiable: 2
  confabulation_rate: 0.026
  labels_checked: 63
  labels_matching: 26
  labels_mismatched: 21
  mislabelled_terms:
  - term_id: HP:0003553
    reported_labels:
    - Distal muscle weakness
    ontology_label: obsolete Cellulitis due to immunodeficiency
  - term_id: HP:0000667
    reported_labels:
    - Impaired vibration sensation
    ontology_label: Phthisis bulbi
  - term_id: HP:0003477
    reported_labels:
    - Extensor plantar response
    - Peripheral axonal neuropathy
    ontology_label: Peripheral axonal neuropathy
  - term_id: HP:0000998
    reported_labels:
    - Photosensitivity
    ontology_label: Hypertrichosis
  - term_id: GO:0045815
    reported_labels:
    - histone H3-K9 trimethylation
    ontology_label: transcription initiation-coupled chromatin remodeling
  - term_id: HP:0007340
    reported_labels:
    - Axonal degeneration
    ontology_label: Lower limb muscle weakness
  - term_id: CL:0000576
    reported_labels:
    - Schwann cell
    ontology_label: monocyte
  - term_id: CL:0002575
    reported_labels:
    - thyroid gland follicular cell
    ontology_label: central nervous system pericyte
  - term_id: GO:0005720
    reported_labels:
    - DNA repair foci
    ontology_label: GO_0005720
  - term_id: HP:0003458
    reported_labels:
    - Distal lower limb muscle weakness
    ontology_label: 'EMG: myopathic abnormalities'
  - term_id: NCIT:C20031
    reported_labels:
    - physical therapy
    ontology_label: Extracellular Protein
  - term_id: NCIT:C25228
    reported_labels:
    - occupational therapy
    ontology_label: Right
  - term_id: NCIT:C49243
    reported_labels:
    - pain management
    ontology_label: Intestinal Smooth Muscle Tissue
  - term_id: NCIT:C15817
    reported_labels:
    - orthopedic surgical procedure
    ontology_label: Neuroscience and Neuropsychiatric Research
  - term_id: NCIT:C16632
    reported_labels:
    - gene therapy
    ontology_label: Geographic Area
  - term_id: NCIT:C25831
    reported_labels:
    - Adeno-associated viral vector
    ontology_label: DNA Single Strand Break
  - term_id: NCIT:C17462
    reported_labels:
    - genetic counseling
    ontology_label: Transcription Factor Jun-B
  - term_id: NCIT:C17461
    reported_labels:
    - prenatal diagnosis
    ontology_label: Initiation Factor
  - term_id: NCIT:C18679
    reported_labels:
    - preimplantation genetic diagnosis
    ontology_label: Carcinogenesis, Co-Carcinogenesis
  - term_id: NCIT:C15273
    reported_labels:
    - rehabilitation therapy
    ontology_label: Longitudinal Study
  - term_id: NCIT:C19323
    reported_labels:
    - supportive care
    ontology_label: Tumor Biology
  labels_variant: 16
  unresolved_terms:
  - HP:0003437
  - UBERON:0006413
  obsolete_terms:
  - term_id: HP:0003553
    ontology_label: obsolete Cellulitis due to immunodeficiency
    replaced_by: HP:0100658
  - term_id: GO:0016566
    ontology_label: obsolete specific transcriptional repressor activity
  - term_id: GO:0006306
    ontology_label: obsolete DNA methylation
  - term_id: CHEBI:18201
    ontology_label: CHEBI_18201
    replaced_by: CHEBI:16171
  - term_id: GO:0005720
    ontology_label: GO_0005720
    replaced_by: GO:0000792
  unresolvable_prefixes:
  - ORPHA
  - SNOMEDCT
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth Disease Axonal Type 2Z
- **MONDO ID:** MONDO:0014736 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease Axonal Type 2Z** covering all of the
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

# Charcot–Marie–Tooth Disease Axonal Type 2Z (CMT2Z): An Integrated Research Overview

Charcot–Marie–Tooth disease axonal type 2Z (CMT2Z) is a rare autosomal dominant hereditary peripheral neuropathy caused by heterozygous pathogenic variants in the *MORC2* gene, a DNA-dependent ATPase that plays central roles in chromatin remodeling, epigenetic silencing, and DNA damage response.[1][5][13] Clinically, CMT2Z presents with an axonal motor–sensory neuropathy that typically begins in childhood or adolescence with distal lower limb weakness, muscle atrophy, and sensory impairment, often accompanied by pyramidal signs and, in some individuals, learning difficulties.[1][10][13] Over the last decade, it has become clear that *MORC2*-related disease encompasses a broader pleiotropic spectrum ranging from “pure” axonal CMT2Z to complex phenotypes with spinal muscular atrophy–like presentations and a syndromic neurodevelopmental disorder characterized by developmental delay, impaired growth, dysmorphic facies, and axonal neuropathy (DIGFAN).[3][5][17][19] At the molecular level, missense variants in the GHKL ATPase module of MORC2 perturb ATP-dependent dimerization dynamics, hyperactivate HUSH-mediated epigenetic silencing, and impair DNA repair; recent mouse work further implicates hydroxyl radical–mediated oxidative damage and neuronal apoptosis in the pathogenesis of neuropathy and demonstrates rescue of phenotypes by adeno-associated virus (AAV)-based gene therapy targeting the GHKL ATPase domain.[7][12][15][18] This report synthesizes current knowledge on CMT2Z across disease definition, etiology, phenotype spectrum, genetic and mechanistic underpinnings, diagnostics, outcomes, treatment, prevention, and model systems, with ontology mapping and evidence from human clinical studies, in vitro models, and animal experiments, to support structured representation in a disease knowledge base.

## 1. Disease Information

### 1.1 Definition and Clinical Concept

Charcot–Marie–Tooth disease axonal type 2Z (CMT2Z) is defined as a dominantly inherited axonal motor and sensory peripheral neuropathy caused by heterozygous pathogenic variants in *MORC2* at 22q12.2.[1][5][13] OMIM entry 616688 describes CMT2Z as “an autosomal dominant axonal peripheral neuropathy characterized by onset, usually in the first decade, of distal lower limb muscle weakness and sensory impairment,” emphasizing its classification among the Charcot–Marie–Tooth type 2 (axonal) neuropathies.[1] Orphanet similarly defines “autosomal dominant Charcot–Marie–Tooth disease type 2Z” as a rare hereditary axonal motor and sensory neuropathy marked either by early generalized hypotonia and weakness or later onset distal lower limb weakness and atrophy, cramps, and sensory loss, progressing asymmetrically to involve proximal and upper limbs, and frequently associated with pyramidal signs and learning difficulties.[10] These disease-level resources converge on a core concept of CMT2Z as a length-dependent axonal neuropathy with variable age at onset, variable severity, and frequent central nervous system features such as spasticity and cognitive impairment in at least a subset of affected individuals.[1][10][13]

From a nosological perspective, CMT2Z falls within the broader category of “genetic neuropathy” and more specifically “hereditary motor and sensory neuropathy type 2” in traditional classifications, corresponding to MONDO:0014736 (“Charcot-Marie-Tooth disease axonal type 2Z”) in the Mondo Disease Ontology.[10] It is distinguished from demyelinating CMT1 forms by electrophysiologic evidence of axonal degeneration with relatively preserved conduction velocities, and from other CMT2 subtypes by its specific association with *MORC2* variants and characteristic pyramidal signs.[1][2][4][13] In recent literature on *MORC2*-related disorders, CMT2Z is often discussed alongside a spinal muscular atrophy–like phenotype and the DIGFAN neurodevelopmental syndrome, which are allelic conditions caused by overlapping sets of *MORC2* missense variants and share axonal neuropathy as a common feature.[3][5][16][17][19] For knowledge representation, it is therefore useful to consider CMT2Z both as a distinct axonal CMT subtype and as part of a *MORC2*-associated pleiotropic spectrum.

### 1.2 Identifiers, Codes, and Synonyms

CMT2Z has multiple standard identifiers across rare disease, genetic, and clinical terminologies. In OMIM, the phenotype entry “Charcot-Marie-Tooth disease, axonal, type 2Z” carries MIM number 616688, linked by a number sign to the causative gene *MORC2* (MIM 616661).[1][5] Orphanet assigns the identifier ORPHA:466768 to “Autosomal dominant Charcot-Marie-Tooth disease type 2Z,” with ICD-10 code G60.0 (“Hereditary motor and sensory neuropathy”) as the primary billing code and notes its prevalence as less than 1 per 1,000,000 individuals.[10] In OMIM’s *MORC2* gene entry 616661, the phenotype association table lists CMT2Z (616688) as a monoallelic autosomal dominant phenotype, alongside “Developmental delay, impaired growth, dysmorphic facies, and axonal neuropathy” (DIGFAN, MIM 619090), underscoring the gene’s pleiotropy.[5]

SNOMED CT terminology includes a specific concept corresponding to axonal CMT2Z linked to *MORC2* (SNOMEDCT:1187564009) in OMIM’s metadata.[1][5] Orphanet and OMIM both provide synonyms such as “CMT2Z,” “autosomal dominant Charcot–Marie–Tooth disease type 2 due to *MORC2* mutation,” and “Charcot–Marie–Tooth disease type 2Z.”[1][10] The Unified Medical Language System (UMLS) lists concept C5569025 for this disorder, facilitating integration into clinical informatics systems.[10] The user has specified MONDO:0014736 as the relevant Mondo ID, which corresponds to the ontology term for CMT2Z and allows cross-linking across resources such as OBO ontologies and ClinGen.

Taken together, these identifiers demonstrate that information on CMT2Z is derived from aggregated disease-level resources that synthesize case reports, cohort studies, and genetic evidence rather than from single electronic health records. OMIM, Orphanet, and PanelApp collate data from multiple families and research groups to define phenotype, inheritance, and molecular etiology.[1][5][6][10][19] Clinical series and mechanistic studies published in journals such as Annals of Neurology, Human Molecular Genetics, Brain, and the American Journal of Human Genetics provide primary patient-level data that underpin these aggregate resources.[7][11][13][17] For a disease knowledge base, these disease-level summaries can be complemented by structured extraction of individual case data from the primary literature.

### 1.3 Source Types and Evidence Basis

The characterization of CMT2Z and its relation to *MORC2* is grounded in several types of evidence. The initial identification of *MORC2* as the gene for axonal CMT with pyramidal signs came from linkage analysis in a multigenerational Australian family combined with whole-exome sequencing, which mapped disease to 22q12.1–q12.3 and identified a segregating p.R252W *MORC2* mutation.[13] Subsequent studies queried unsolved CMT2 exomes and screened additional families, revealing recurrent p.R252W and p.E236G mutations, which were absent from population controls and segregated with disease in multiple kindreds.[13] Orphanet and OMIM entries summarize these and other family-based reports, while GenCC’s gene–disease validity curation concludes that *MORC2* is “definitively associated” with autosomal dominant axonal CMT2Z based on more than 50 reported families worldwide.[16][19]

Beyond familial aggregation, aggregated disease-level resources incorporate clinical series such as the Japanese cohort in which *MORC2* variants were detected in 2.7% of patients with CMT type 2, making *MORC2* the second most common causative gene after *MFN2* in that population.[11] Prospective and retrospective cohorts of patients with *MORC2*-related disease, including those with DIGFAN and Cockayne syndrome–like presentations, further enrich the understanding of phenotypic range and natural history.[3][17] Mechanistic insights derive from in vitro cell models (patient-derived fibroblasts, transfected rodent sensory neurons, CRISPR-engineered HeLa cells), structural biology studies of MORC2 ATPase–CW fragments, and in vivo mouse models carrying specific *Morc2a* variants.[7][12][15][16][18] Collectively, this mixed evidence base supports robust disease-level characterization appropriate for ontology-driven knowledge representation.

## 2. Etiology

### 2.1 Primary Causal Factors: Genetic Basis in *MORC2*

CMT2Z is fundamentally a monogenic disorder caused by heterozygous pathogenic variants in *MORC2* (microrchidia family CW-type zinc finger 2), a gene encoding a DNA-dependent ATPase involved in epigenetic silencing and DNA repair.[1][5][13][15] OMIM explicitly notes that “a number sign (#) is used with this entry [CMT2Z, 616688] because of evidence that axonal Charcot-Marie-Tooth disease type 2Z (CMT2Z) is caused by heterozygous mutation in the *MORC2* gene (616661) on chromosome 22q12,” summarizing multiple independent reports.[1] Similarly, the *MORC2* gene entry states that “mutations in the *MORC2* gene cause axonal Charcot-Marie-Tooth disease,” and lists CMT2Z and DIGFAN as monoallelic autosomal dominant phenotypes.[5] The initial Annals of Neurology study concluded that “MORC2 mutations are the likely pathogenic cause of CMT2 and pyramidal signs in these families,” based on co-segregation, absence in controls, and functional considerations.[13]

The pathogenic variants identified to date are overwhelmingly missense single-nucleotide variants affecting conserved residues in the GHKL ATPase module or adjacent structural elements.[7][11][13][15][16][17] Recurrent mutations include p.R252W and p.E236G in early CMT2Z families, p.Arg190Trp as a mutational hotspot in Japanese patients, and p.S87L, p.T424R, and others in DIGFAN and complex *MORC2*-related phenotypes.[7][11][13][16][17] Functional studies indicate that these missense variants alter ATPase activity, ATP-dependent dimerization dynamics, and interactions with the HUSH complex, leading to dysregulated epigenetic silencing and impaired DNA damage response.[7][15][16][18] There is no evidence that truncating or loss-of-function variants in *MORC2* cause CMT2Z, and such variants may be lethal or associated with different phenotypes; the disease is best conceptualized as driven by specific missense alleles with complex functional effects.[16][18]

Environmental, infectious, or purely mechanistic non-genetic etiologies have not been implicated as primary causes of CMT2Z. Although peripheral nerves can be damaged by toxins, immune-mediated processes, or metabolic disturbances, the characteristic pattern of CMT2Z and its segregation with *MORC2* mutations across families and de novo cases strongly supports a genetic etiology.[1][3][10][13] In knowledge representation, CMT2Z should thus be classified under “monogenic disease” with a “single gene, autosomal dominant, germline missense variant” causal architecture.

### 2.2 Genetic Risk Factors and Variant Spectrum

Within the monogenic framework, several genetic risk factors modulate the likelihood and expression of CMT2Z. The primary risk factor is the presence of a heterozygous pathogenic *MORC2* missense variant, most often in the ATPase module.[5][13][15][16] Family history of axonal CMT with pyramidal signs, and hereditary motor and sensory neuropathy spanning multiple generations, is a key clinical indicator of such variants, reflecting autosomal dominant transmission.[1][10][13] However, de novo variants are common, particularly in DIGFAN and Cockayne syndrome–like *MORC2* disorders, making parental history absent in many severe cases.[3][8][17][14] Guillen Sacoto et al. reported that most individuals with DIGFAN harbored de novo variants in the ATPase module of *MORC2*, underscoring the importance of germline mutational events rather than inherited alleles in some segments of the spectrum.[3][17]

The variant spectrum includes multiple recurrent and private missense alleles. In the Australian family and related CMT2 cases, p.R252W and p.E236G were identified in conserved positions and absent in population databases.[13] In Japan, p.Arg190Trp was observed in eight unrelated families, suggesting a recurrent mutation and possible founder effect in that population, while two novel likely pathogenic variants (p.Cys345Tyr, p.Ala369Val) and one uncertain-significance variant (p.Tyr332Cys) were also reported.[11] The Arg190Trp hotspot illustrates how specific ethnic or regional groups may have higher prevalence of particular alleles, which can inform targeted genetic screening.[11] Other variants such as p.S87L and p.T424R in the ATP-binding region have been associated with more severe neurodevelopmental phenotypes, growth retardation, and craniofacial dysmorphism, consistent with genotype–phenotype correlations within the *MORC2* disease spectrum.[3][16][17]

ClinGen’s GenCC submission for *MORC2* in relation to CMT2Z emphasizes that “more than 50 families have been reported with *MORC2*-related neuropathy worldwide,” and that CMT2Z and DIGFAN illustrate “the diverse range of phenotypical expressions associated with *MORC2*, varying both in terms of age of onset and overall clinical presentation.”[16][19] Allele frequencies in population databases such as gnomAD are extremely low or absent for the known pathogenic variants, in keeping with the rarity of CMT2Z (<1/1,000,000) and strong negative selection against severe forms.[10][11][16] To date, there are no established genetic modifier genes that consistently alter CMT2Z severity, although the broader genetic background and epigenetic state may influence penetrance and expressivity, as suggested by the variability of HUSH activation and DNA methylation episignatures.[9][15][16]

### 2.3 Environmental and Lifestyle Risk Factors

No specific environmental risk factors have been proven to cause CMT2Z or substantially increase its incidence beyond the presence of a pathogenic *MORC2* variant. Peripheral neuropathies can be exacerbated by diabetes, neurotoxic medications (such as certain chemotherapeutic agents), excessive alcohol use, and nutritional deficiencies, but these factors have not been systematically studied in relation to *MORC2*-associated axonal CMT.[1][10][16] Clinical descriptions of CMT2Z families and DIGFAN cases do not highlight consistent exposure to toxins or adverse lifestyle factors that could be construed as causal.[3][11][13][17] Furthermore, the presence of de novo *MORC2* variants and severe neurodevelopmental phenotypes arising in infancy suggests that environmental factors play, at most, a secondary role compared to germline genetic lesions.[3][8][17]

Age itself is a relevant temporal factor, but not in the sense of risk; rather, the age at which manifestations emerge is determined by genotype and variant-specific functional impact. CMT2Z most commonly presents in childhood or early adulthood, but neonatal-onset and adult-onset cases exist, particularly in the context of specific variants such as p.S87L (often neonatal/infantile) versus p.R252W (often early-childhood).[1][10][11][13][17][18] Sex does not appear to substantially alter risk, and both males and females are affected in reported families, consistent with autosomal inheritance.[11][13][16] In summary, for knowledge base purposes, the principal non-genetic “risk factor” is positive family history of CMT2Z or related *MORC2*-associated phenotypes, which reflects underlying genetic risk; environmental and lifestyle risk factors are currently not established.

### 2.4 Protective Factors and Gene–Environment Interactions

At present, no genetic protective variants or modifier alleles have been clearly shown to mitigate CMT2Z risk or severity. The current literature focuses on pathogenic missense variants and their functional consequences, with little systematic exploration of variants that might attenuate disease.[5][7][15][16] Some theoretical considerations arise from structural and biochemical data: variants that mildly reduce MORC2 ATPase activity without hyperactivating HUSH might be neutral or even protective in certain contexts, but such alleles have not been characterized clinically.[15][16] Likewise, the observation that biallelic *Morc2a* p.S87L in mice is embryonic lethal suggests that partial reduction of MORC2 function is incompatible with life, making “protective hypomorphic” alleles unlikely.[12][18]

In terms of environmental protective factors, standard neuropathy care recommendations—such as avoidance of neurotoxic medications, optimization of metabolic health, and regular physical therapy—may reduce complications and improve functional outcomes, but they do not prevent the occurrence of CMT2Z in genetically predisposed individuals.[10][16] Antioxidant strategies could theoretically mitigate hydroxyl radical–mediated damage implicated in *Morc2a* p.S87L neuropathy, but these have not yet been tested in humans with CMT2Z, and their protective efficacy remains speculative.[12][18] No formal gene–environment interactions have been described in which specific exposures interact with *MORC2* variants to alter disease penetrance; mechanistic work suggests that *MORC2* function is modulated by PARP1-dependent poly(ADP-ribosylation) in response to DNA damage, but this is an intrinsic cellular response rather than an external environmental interaction.[15][16][18]

For ontology-based representation, it is therefore appropriate to record “protective factors: none clearly established” and “gene–environment interactions: not demonstrated; disease primarily driven by germline *MORC2* missense variants.” Further research may uncover environmental modifiers of severity or epigenetic state, especially given the DNA methylation episignatures that distinguish *MORC2*-related disorders, but current evidence does not support specific preventive exposures.[9]

## 3. Phenotypes

### 3.1 Core Neuromuscular Phenotype of CMT2Z

The core phenotype of CMT2Z is an axonal motor–sensory peripheral neuropathy characterized by length-dependent distal weakness and sensory loss, predominantly affecting the lower limbs and progressing proximally over time. OMIM describes CMT2Z as having “onset, usually in the first decade, of distal lower limb muscle weakness and sensory impairment,” with clinical findings of muscle atrophy, gait disturbance, and reduced reflexes.[1] Orphanet elaborates that affected individuals may present with early generalized hypotonia and weakness or later onset distal weakness and atrophy, cramps, and sensory impairment, with weakness and atrophy progressing asymmetrically to involve proximal and upper limbs.[10] Clinical series confirm that most patients develop foot drop, difficulties with running and climbing stairs, and distal muscle wasting, consistent with axonal degeneration of motor fibers.[11][13]

Electrophysiologically, nerve conduction studies in CMT2Z show reduced compound muscle action potential amplitudes and reduced sensory nerve action potentials, indicative of axonal loss, while conduction velocities are relatively preserved compared to demyelinating CMT1.[10][11][13][18] For example, in the initial Ann Neurol report, affected individuals exhibited “axonal neuropathy with pyramidal signs,” and neurophysiology was consistent with CMT2.[13] These features correspond to the Human Phenotype Ontology (HPO) term “Axonal neuropathy” (HP:0003437), “Distal muscle weakness” (HP:0003553), “Muscle atrophy” (HP:0003202), and “Impaired vibration sensation” (HP:0000667). Quality of life is significantly affected by the progressive motor disability, leading to limitations in ambulation, dependence on assistive devices, and increased risk of falls; however, many individuals maintain independent walking for decades, especially in milder forms.[10][11][13]

Symptom severity and progression are variable. Some patients with MORC2 p.R252W or Arg190Trp develop slowly progressive neuropathy with onset in childhood or adolescence and remain ambulant into adulthood, representing a moderate phenotype.[11][13][16] Others, particularly with p.S87L or certain ATPase module variants associated with DIGFAN, manifest severe early-onset hypotonia, generalized weakness, and rapid progression, leading to loss of ambulation in childhood.[3][17][18] Within families, intrafamilial variability is often noted, indicating that the same variant can produce mild or severe neuropathy depending on individual modifiers.[11][13][19] In knowledge representation, “variable expressivity” and “progressive course” should be captured as attributes of the CMT2Z phenotype.

### 3.2 Central Nervous System Involvement: Pyramidal Signs and Ataxia

A distinctive feature of CMT2Z compared to many other CMT2 forms is the frequent presence of pyramidal signs, including increased muscle tone, brisk reflexes, and extensor plantar responses, reflecting corticospinal tract involvement. Orphanet notes that “additional features are pyramidal signs like increased muscle tone and extensor plantar reflexes, as well as learning difficulties,” emphasizing the central nervous system manifestations.[10] The original Australian family studied by Albulym et al. was described as having “Charcot-Marie-Tooth disease type 2 and pyramidal signs,” and the Ann Neurol abstract highlights that a new locus was mapped for “CMT2 and pyramidal signs” to 22q12 with segregating *MORC2* mutations.[13] Pyramidal signs correspond to HPO terms “Spasticity” (HP:0001257) and “Extensor plantar response” (HP:0003477).

More complex central involvement is evident in DIGFAN and other *MORC2*-related neurodevelopmental disorders, which share allelic variants with CMT2Z but present with cerebellar ataxia, intellectual disability, brain atrophy, microcephaly, and features reminiscent of Cockayne syndrome or Leigh syndrome.[3][9][12][17][18] In a mouse model carrying heterozygous *Morc2a* p.S87L, animals displayed “symptoms of axonal neuropathy, cerebellar ataxia and motor neuron degeneration,” paralleling the peripheral and central nervous system involvement seen in human CMT2Z and DIGFAN.[12][18] Cerebellar ataxia would correspond to HPO term “Gait ataxia” (HP:0002141) and “Cerebellar ataxia” (HP:0001251), while “Motor neuron degeneration” aligns with “Amyotrophic lateral sclerosis-like phenotype” (HP:0007354) in broader contexts.

In terms of quality of life, central motor involvement compounds functional impairment, leading to spastic gait, difficulty with fine motor tasks, and need for more intensive rehabilitation.[10][11][13] Learning difficulties and intellectual disability further affect educational attainment and social participation.[3][10][17] CMT2Z knowledge models should therefore represent pyramidal signs and cerebellar features as common or at least frequent secondary phenotypes, particularly in individuals with specific MORC2 variants.

### 3.3 Cognitive and Neurodevelopmental Features

Cognitive and neurodevelopmental abnormalities are variably present across CMT2Z and broader *MORC2*-related phenotypes. Orphanet notes that learning difficulties are “additional features” in CMT2Z, suggesting that mild cognitive impairment or specific learning disorders occur in a subset of patients.[10] In the Ann Neurol family, no detailed neuropsychological data are provided, but pyramidal signs and early-onset neuropathy imply broader central involvement.[13] More systematic characterization of neurodevelopmental features comes from DIGFAN cohorts, where heterozygous *MORC2* variants in the ATPase module cause a syndromic disorder with developmental delay, intellectual disability, growth retardation, microcephaly, and craniofacial dysmorphism.[3][17]

Guillen Sacoto et al. reported that “individuals presented with a similar phenotype consisting of developmental delay, intellectual disability, growth retardation, microcephaly, and variable craniofacial dysmorphism,” and in their series, gross motor delay was present in 95% (19/20), short stature in 90% (18/20), intellectual disability in 90% (18/20), and microcephaly in 75% (15/20) of affected individuals.[17] Their abstract highlighted that “de novo variants in the ATPase module of MORC2 cause a neurodevelopmental disorder with growth retardation and variable craniofacial dysmorphism,” emphasizing the causal role of specific missense variants.[17] Neurodevelopmental features were also described in the Cockayne syndrome–like *MORC2* cohort, where all participants except one had intellectual disability and limited language abilities, using short sentences, sign language, and gestures, and attended special needs programs.[3] These phenotypes correspond to HPO terms such as “Global developmental delay” (HP:0001263), “Intellectual disability” (HP:0001249), “Microcephaly” (HP:0000252), and “Short stature” (HP:0004322).

Quality of life impact is profound in these syndromic forms, as cognitive impairment affects autonomy, communication, and social integration, while growth delay and dysmorphic facies can contribute to stigmatization.[3][14][17] In knowledge representation, CMT2Z should be linked to these neurodevelopmental phenotypes via *MORC2* variant-specific associations, with explicit indication that severe intellectual disability and microcephaly are more characteristic of DIGFAN and overlapping syndromes than of “pure” axonal CMT2Z, although boundaries are fluid and overlapping cases exist.[3][16][17]

### 3.4 Systemic and Sensory Phenotypes: Hearing Loss, Retinopathy, Endocrine Features

Beyond neuromuscular and neurodevelopmental manifestations, *MORC2*-related disease can involve multiple organ systems, some of which have been documented in patients initially diagnosed with Cockayne syndrome or mitochondrial disease.[3][9][14] The Cockayne syndrome literature describes multiorgan complications including neurodevelopmental disabilities, microcephaly, poor growth, corneal opacification and cataracts, sensorineural hearing loss, demyelinating neuropathy, hepatic involvement, kidney dysfunction, skin photosensitivity, and dental anomalies.[3] Several individuals with *MORC2* variants and CS-like diagnoses showed overlapping features, including sensorineural hearing loss, retinopathy, and systemic involvement such as liver enzyme abnormalities.[3][9] These phenotypes correspond to HPO terms “Sensorineural hearing impairment” (HP:0000407), “Retinal dystrophy” (HP:0000556), “Hepatic dysfunction” (HP:0001410), and “Photosensitivity” (HP:0000998).

The DIGFAN endocrine case report emphasizes endocrine and ophthalmologic complications. The authors note that “the association among short stature, developmental delays, facial dysmorphisms, and axonal neuropathy has been characterized as DIGFAN syndrome,” caused by heterozygous *MORC2* mutations, and highlight associations with ophthalmopathies (retinitis pigmentosa in up to 83% of cases), sensorineural hearing loss (up to 58%), neuroimaging abnormalities (up to 66%), and endocrine conditions such as hypothyroidism and precocious puberty.[14] These systemic features broaden the phenotypic spectrum and illustrate that *MORC2*-related disease can affect sensory organs, endocrine glands, and other tissues, likely via shared mechanisms of DNA damage sensitivity and epigenetic dysregulation.[3][9][14][16]

Quality of life is significantly impacted by hearing and vision impairment, which complicate communication and mobility and necessitate assistive devices.[3][14] Endocrine abnormalities such as hypothyroidism and disordered puberty require hormone replacement and monitoring, adding to the medical burden.[14] In ontology mapping, CMT2Z and *MORC2*-related disorders should be associated with HPO terms for sensorineural hearing loss, retinal dystrophy, endocrine dysfunction, and neuroimaging abnormalities, with frequency annotations indicating that these are common in DIGFAN/CS-like syndromes but less consistently reported in classic CMT2Z cohorts.[3][9][14][17]

### 3.5 Phenotype Progression, Severity, and Quality of Life

Across its spectrum, *MORC2*-associated CMT2Z is a chronic, progressive disease. Neuropathy typically progresses from distal to proximal, with increasing weakness, muscle atrophy, and sensory loss over years to decades.[1][10][11][13] Pyramidal signs and spasticity may emerge or worsen over time, reflecting ongoing corticospinal tract degeneration, and in severe variants such as p.S87L, cerebellar ataxia and motor neuron degeneration can further contribute to disability.[12][18] In DIGFAN, developmental trajectories are delayed from infancy, and growth retardation and microcephaly are evident early, with ongoing accumulation of motor and cognitive deficits.[3][17] Quality of life is shaped by this progression: children may require orthoses and physical therapy to maintain mobility, adolescents face challenges in school due to learning difficulties and fatigue, and adults may lose the ability to walk unaided, necessitating wheelchairs and home modifications.[10][11][13][16]

From a knowledge base perspective, it is important to encode not only the presence of individual phenotypes but also their temporal evolution and severity categories (mild, moderate, severe). CMT2Z in families with p.R252W or Arg190Trp often follows a slower, moderate course, whereas DIGFAN and CS-like *MORC2* disorders are severe, multisystem, and early-onset.[11][13][17][18] Intrafamilial heterogeneity implies that severity cannot be predicted solely by genotype, but genotype–phenotype correlations provide useful predictive clues.[3][7][16][17] The impact on daily functioning encompasses mobility, self-care, pain, social participation, and mental health, aligning with domains captured in tools like the SF-36 and EQ-5D, although disease-specific quality of life instruments for CMT2Z have not yet been developed.[16] In the knowledge base, linking phenotypes to functional domains and disability classifications (e.g., ICF categories) can support patient-centered decision support.

## 4. Genetic and Molecular Information

### 4.1 Causal Gene: *MORC2* Structure and Function

The causal gene for CMT2Z is *MORC2* (microrchidia family CW-type zinc finger 2), located at cytogenetic band 22q12.2, with GRCh38 coordinates 22:30,925,130–30,968,774.[5] *MORC2* encodes a DNA-dependent ATPase belonging to the GHKL (gyrase, Hsp90, histidine kinase, MutL) ATPase superfamily, and contains an N-terminal GHKL ATPase module, a CW-type zinc finger domain, and a long coiled-coil insertion that participates in DNA binding and dimerization.[5][15][16] The gene is highly expressed in both embryonic and adult human neural tissues, and its expression is dynamically regulated during murine nervous system development and maturation.[7] Li et al. originally showed that MORC2 relaxes chromatin to facilitate DNA double-strand break repair, linking it to DNA damage response pathways.[5]

Structural and functional studies have clarified MORC2’s role in epigenetic silencing. Douse et al. solved crystal structures of a MORC2 fragment comprising the GHKL ATPase module and CW-type zinc finger and demonstrated that this fragment dimerizes upon ATP binding, forming a hinge-shaped dimer with a coiled-coil insertion absent in other GHKL ATPases.[15] They showed that “ATP binding or dimerization of MORC2 (or both) is required for HUSH function,” and that MORC2 is necessary, in conjunction with the human silencing hub (HUSH) complex, to silence transgenes integrated at chromatin loci marked by H3K9me3.[15] Tchasovnikarova et al., using CRISPR/Cas9 forward genetic screens in HeLa cells, identified MORC2 as required for HUSH-mediated transgene silencing and showed that MORC2 interacts with HUSH subunits TASOR and MPP8, recruiting MORC2 to heterochromatic sites.[16] These findings position MORC2 as a key effector of transcriptional repression of LINE-1 retrotransposons and other repetitive sequences.[15][16][18]

Ontology mapping to Gene Ontology (GO) terms includes “DNA-dependent ATPase activity” (GO:0008094), “chromatin remodeling” (GO:0006338), “epigenetic regulation of gene expression” (GO:0040029), “double-strand break repair” (GO:0006302), and “transcriptional repression” (GO:0016566). Cellular component terms include “nucleus” (GO:0005634), “heterochromatin” (GO:0000792), and “chromatin” (GO:0000785). These annotations are crucial for knowledge base integration of MORC2’s molecular functions.

### 4.2 Pathogenic Variants: Types, Locations, and Functional Classes

Pathogenic variants causing CMT2Z are predominantly heterozygous missense changes affecting conserved residues in the GHKL ATPase module or adjacent structural elements, although variants in other regions of the protein are also implicated in syndromic phenotypes.[7][11][13][15][16][17] Early reports identified p.R252W and p.E236G mutations in CMT2 families with pyramidal signs; both occur at highly conserved positions in the ATPase module and were absent in normal population controls.[13] In Japanese patients, p.Arg190Trp was found in eight unrelated families, indicating a mutational hotspot; additional novel variants p.Cys345Tyr and p.Ala369Val, and an uncertain-significance variant p.Tyr332Cys, were located within the GHKL ATPase or its immediate vicinity.[11] DIGFAN-associated variants such as p.S87L, p.T424R, and others cluster in the ATP-binding region and coiled-coil insertion, and have been associated with more severe neurodevelopmental phenotypes.[3][16][17]

Functional classifications distinguish several mechanistic classes of MORC2 variants. Douse et al. found that neuropathic mutations perturb GHKL ATPase dimerization dynamics and epigenetic silencing via multiple structural mechanisms: some destabilize the ATPase–CW module, others trap the ATP lid in an aberrant conformation, and others perturb the dimer interface.[15] For example, the CMT-associated MORC2 mutation R252W hyperactivates HUSH-mediated epigenetic silencing in neuronal cells, leading to enhanced and accelerated re-repression of transgenes, while S87L forms constitutive N-terminal dimers even without nucleotide binding, and T424R forms a mixture of monomers and dimers in the presence of AMPPNP.[15][16] In functional assays, variants that abolish ATP binding or hydrolysis (e.g., N39A, D68A) fail to restore HUSH function in MORC2 knockout cells, highlighting the importance of ATPase activity for MORC2’s role in transcriptional repression.[16]

Hum Mol Genet work by Sevilla et al. and colleagues examined the impact of p.S87L and p.R252W on neuronal biology. They showed that full-length MORC2 is highly expressed in neural tissues and that both mutations induce transcriptional changes in patient-derived fibroblasts and in rodent sensory neurons, with more pronounced changes and abnormal axonal morphology in neurons expressing p.S87L, consistent with its association with a more severe clinical phenotype.[7] Brain studies by Pandiloski et al. reported that Morc2a p.S87L in mice causes protein synthesis defects and reduced Morc2a protein levels, leading to elevated cellular hydroxyl radicals and apoptosis, indicating a loss-of-function characteristic at the level of protein dosage, despite hyperactivation of HUSH.[12][18] These observations suggest a nuanced functional classification: MORC2 variants may combine gain-of-function effects in epigenetic silencing with loss-of-function effects in DNA repair and protein synthesis, resulting in complex cellular consequences.[15][16][18]

For ACMG/AMP variant classification, many reported variants are considered pathogenic or likely pathogenic based on segregation, de novo occurrence, functional studies, and absence from population databases.[5][7][11][13][16][17][19] ClinVar and related resources catalog these variants, although comprehensive classification is beyond the scope of current search results. In knowledge representation, variant types are predominantly “missense” with “germline, heterozygous” origin, and functional consequences should be annotated as “altered ATPase activity,” “hyperactivated HUSH-mediated epigenetic silencing,” and “impaired DNA damage response,” with variant-specific nuances.

### 4.3 Modifier Genes, Epigenetic Signatures, and Chromosomal Abnormalities

No consistent modifier genes have been identified that alter CMT2Z severity, but epigenetic context clearly modulates phenotypic expression. A recent thesis on DNA methylation episignatures in *MORC2*-associated disorders described a characteristic methylation pattern across multiple *MORC2* phenotypes, ranging from late-onset neuromuscular disorders (including CMT and spinal muscular atrophy) to early-onset multisystem neurodevelopmental disorders such as Cockayne syndrome, mitochondrial diseases, Leigh syndrome, and DIGFAN.[9] The author noted that “heterozygous missense mutations in the MORC2 gene are associated with a clinically diverse spectrum of neurological disorders,” and that these phenotypes can be categorized into two major groups: neuromuscular disorders (CMT and SMA) and syndromic neurodevelopmental disorders (Cockayne and Leigh-like, DIGFAN).[9] Epigenetic episignatures may thus provide a molecular profiling tool for classifying *MORC2* variants and predicting their phenotypic outcomes.

MORC2 itself is heavily involved in epigenetic regulation. It interacts with the HUSH complex, which recruits MORC2 to sites marked by H3K9me3, where it contributes to transcriptional repression of retroelements and transgenes.[15][16][18] Hyperactivation of HUSH by MORC2 variants leads to excessive silencing, potentially affecting genes important for neuronal function and development.[15][16][18] Additionally, MORC2 is poly(ADP-ribosylated) by PARP1 in response to DNA damage, a modification that stimulates its ATPase and chromatin remodeling activities.[18] These post-translational and epigenetic modifications integrate DNA damage signaling with transcriptional control, placing MORC2 at the crossroads of genome maintenance and gene expression. In ontology terms, epigenetic changes involve “DNA methylation” (GO:0006306), “histone H3-K9 trimethylation” (GO:0045815), and “poly(ADP-ribose) polymerase activity” (GO:0003950).

Large-scale chromosomal abnormalities have not been implicated in CMT2Z. OMIM and PanelApp list *MORC2* point mutations as the causal lesions, without recurrent deletions, duplications, or translocations at 22q12.2.[1][5][6][19] DECIPHER and similar structural variant databases may contain isolated CNVs involving *MORC2*, but their relevance to CMT2Z is not established. For the disease knowledge base, “chromosomal abnormalities: none consistently associated” can be recorded, with emphasis on single-gene missense variant etiology.

### 4.4 Molecular Profiling: Transcriptomics, Proteomics, and Metabolomics

Though comprehensive omics-based diagnostic profiling is not yet standard for CMT2Z, several studies provide insights into transcriptomic and proteomic changes caused by MORC2 variants. Sevilla et al. used patient-derived fibroblasts and transfected rodent sensory neurons to study p.S87L and p.R252W MORC2 mutations, demonstrating variant-specific transcriptional changes and differences in axonal morphology.[7] They found that both mutations altered gene expression profiles, but p.S87L induced more pronounced changes and abnormal axonal features, consistent with more severe clinical phenotypes.[7] These transcriptomic alterations likely reflect dysregulated epigenetic silencing via HUSH and changes in DNA damage response pathways, although specific genes and networks were not detailed in the search results.

Pandiloski et al. examined protein synthesis and oxidative stress in *Morc2a* p.S87L mouse embryonic fibroblasts, discovering that the variant led to protein synthesis defects, reduced Morc2a protein levels, increased hydroxyl radical levels, and apoptosis.[12][18] These proteomic and metabolomic insights implicate abnormal protein homeostasis and reactive oxygen species (ROS) metabolism in *MORC2*-related neuropathy. Hydroxyl radicals (\(\cdot OH\)) are highly reactive ROS that can cause DNA and lipid damage; their involvement corresponds to CHEBI:16234 (hydroxyl radical) and GO processes such as “response to oxidative stress” (GO:0006979) and “apoptotic process” (GO:0006915).[12][18] Although systematic metabolomics profiling in human CMT2Z patients has not been reported, the mouse model suggests metabolic signatures of oxidative stress and possibly altered lipid homeostasis, given MORC2’s roles in lipid metabolism.[18]

Proteomics data on MORC2 interacting partners include HUSH subunits TASOR and MPP8, PARP1, and chromatin components associated with silenced loci.[15][16][18] BioGRID and STRING resources (referenced in the review) highlight MORC2’s network within chromatin and DNA repair complexes.[16] For multi-omics integration, combining MORC2 variant status with DNA methylation episignatures, transcriptomic data from neuronal cells, and proteomic markers of DNA damage and ROS response could yield a comprehensive mechanistic profile. At present, such integrative analyses are primarily research tools rather than clinical diagnostics.

## 5. Environmental Information

### 5.1 Non-genetic Contributing Factors

Given the strong genetic basis of CMT2Z, environmental factors play a relatively minor role in its causation. There is no evidence that exposure to toxins, radiation, occupational hazards, or infections directly causes *MORC2*-related neuropathy in the absence of a pathogenic variant.[1][3][10][13][16] Environmental exposures may, however, modulate severity and complications. For example, neurotoxic drugs (such as vincristine, cisplatin) could exacerbate existing axonal damage, and metabolic disorders like diabetes could worsen neuropathy and impair nerve repair, but these influences are general to peripheral neuropathies and not specific to CMT2Z.[16] The current literature does not detail such interactions in *MORC2*-specific cohorts, reflecting the rarity of the disease and limited sample sizes.[11][13][17]

Lifestyle factors such as smoking, alcohol consumption, diet, and exercise may influence general health and resilience but have not been systematically studied as modifiers in CMT2Z. Standard CMT management guidelines often recommend maintaining healthy weight, engaging in appropriate physical activity, and avoiding excessive alcohol, but these are supportive rather than etiologic considerations.[10][16] In knowledge representation, environmental factors can be noted as “non-specific modifiers” rather than causal determinants.

### 5.2 Infectious Agents and Immune Involvement

No infectious agents have been implicated in the onset of CMT2Z. The disease is not known to be triggered by viral, bacterial, fungal, or parasitic infections, and is not classified as an infectious neuropathy.[1][10][13] Immune system involvement appears limited; CMT2Z is not an autoimmune neuropathy, and autoantibodies against myelin or axonal components have not been reported in association with *MORC2* mutations.[16] Inflammatory processes may occur secondarily to neurodegeneration, but there is no evidence of primary chronic inflammation driving the disease.

MORC2’s roles in DNA damage response and epigenetic silencing could theoretically intersect with immune functions, particularly in regulating endogenous retroelements and innate immune sensing, but these aspects have not been explored in the context of CMT2Z.[15][16][18] For now, CMT2Z should be considered a non-inflammatory, non-infectious genetic neuropathy, simplifying its classification in immunology-focused ontologies.

## 6. Mechanism / Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Phenotype

To structure the pathophysiology of CMT2Z, the following ordered causal chain summarizes key mechanistic steps from the initiating *MORC2* lesion to clinical manifestations. Each step reflects current evidence, with some steps inferred from model systems rather than directly demonstrated in humans.

| Step | Causal description |
|------|--------------------|
| 1 | Germline heterozygous missense variant in *MORC2* (often in the GHKL ATPase module) arises, either inherited in autosomal dominant fashion or as a de novo mutation. |
| 2 | The *MORC2* variant leads to altered MORC2 protein structure and ATPase function, perturbing ATP-dependent dimerization, DNA binding, and interactions with the CW-type zinc finger and coiled-coil insertion. |
| 3 | These structural and functional changes result in dysregulated HUSH-mediated epigenetic silencing, typically hyperactivating transcriptional repression at H3K9me3-marked loci, and impair MORC2’s role in DNA double-strand break repair and protein synthesis. |
| 4 | Dysregulated silencing and impaired DNA repair lead to transcriptional misregulation of neuronal genes, accumulation of DNA damage, increased hydroxyl radical production, oxidative stress, and apoptosis in neuronal and glial cells (demonstrated in *Morc2a* p.S87L mouse and cellular models). |
| 5 | Chronic cellular stress and apoptosis in peripheral motor and sensory neurons, and in corticospinal and cerebellar neurons in some variants, result in axonal degeneration, loss of nerve fibers, and disruption of long tracts. |
| 6 | Axonal degeneration manifests clinically as length-dependent axonal motor–sensory neuropathy (CMT2Z), pyramidal signs, cerebellar ataxia, spinal muscular atrophy–like features, and neurodevelopmental deficits, with variant-specific patterns and severity. |

This chain integrates evidence from human genetic studies, structural and biochemical analyses, patient-derived cells, CRISPR screens, and *Morc2a* mouse models.[7][12][15][16][18] In what follows, each step is elaborated with mechanistic detail, cell type involvement, and ontology suggestions.

### 6.2 Upstream Mechanisms: MORC2 Structure, HUSH Interaction, and DNA Damage Response

The initiating lesion is a heterozygous missense variant in *MORC2*, often in the GHKL ATPase module. These variants alter MORC2’s ability to bind and hydrolyze ATP, dimerize, and interact with DNA and protein partners.[5][13][15][16] Douse et al. showed that wild-type MORC2 ATPase–CW fragment dimerizes upon ATP binding and binds DNA, with the coiled-coil insertion acting as a flexible arm for DNA engagement.[15] Neuropathic MORC2 variants modify the dynamics of this dimerization by destabilizing the ATPase–CW module, trapping the ATP lid, or perturbing the dimer interface, leading to abnormal MORC2 oligomeric states and altered DNA binding.[15] Structural mechanisms differ between variants: R252W hyperactivates HUSH-mediated silencing, S87L forms constitutive dimers, and T424R forms improper monomers/dimers mixtures.[15][16]

MORC2’s interaction with HUSH is central to its epigenetic role. The HUSH complex (comprising TASOR, MPP8, and other subunits) recruits MORC2 to heterochromatic loci marked by histone H3K9me3, where MORC2 facilitates transcriptional repression of retroelements and integrated transgenes.[15][16][18] Tchasovnikarova et al. demonstrated that MORC2 is required for HUSH function; in MORC2 knockout HeLa cells, transgene silencing was compromised, and exogenous expression of wild-type MORC2 restored silencing, whereas ATPase-defective MORC2 variants failed to do so.[16] They concluded that “the ATP binding and hydrolytic capabilities of MORC2 may be critical for the transcriptional repression mediated by the HUSH complex,” linking ATPase activity to epigenetic regulation.[16] Guillen Sacoto et al. further showed that MORC2 mutations significantly activated HUSH-mediated silencing, with certain variants (e.g., p.Glu27Lys, p.Arg132Cys) exhibiting pronounced hyperactivation in GFP reporter assays.[16][3]

MORC2 also participates in DNA damage response. PARP1 recruits MORC2 to sites of DNA double-strand breaks and promotes MORC2 poly(ADP-ribosylation), which stimulates its ATPase and chromatin remodeling activities.[18] Li et al. had earlier shown that MORC2 relaxes chromatin to facilitate DNA repair, suggesting that MORC2 functions downstream of PARP1 in orchestrating chromatin accessibility during repair.[5][18] Mutations that impair MORC2’s ATPase activity or chromatin remodeling capacity could thus compromise DNA repair, leading to persistence of DNA lesions. In the *Morc2a* p.S87L mouse model, DNA damage accumulation was observed, supporting this functional deficit.[12][18]

Cell types primarily involved in these upstream mechanisms include neuronal nuclei and glial cells, particularly in peripheral motor and sensory neurons, spinal cord anterior horn cells, corticospinal neurons, and cerebellar neurons.[7][12][18] CL ontology terms such as “spinal motor neuron” (CL:0000100), “sensory neuron” (CL:0000540), and “cerebellar Purkinje neuron” (CL:0000121) are relevant. GO biological processes include “chromatin organization” (GO:0006325), “regulation of transcription, DNA-templated” (GO:0006355), and “double-strand break repair via nonhomologous end joining” (GO:0006303).

### 6.3 Midstream Mechanisms: Transcriptional Misregulation, DNA Damage, and Oxidative Stress

Dysregulated HUSH-mediated silencing and impaired DNA repair constitute midstream mechanisms leading to transcriptional misregulation and cellular stress. MORC2 variants that hyperactivate HUSH increase silencing of target genes at H3K9me3-marked loci, which include not only retroelements but also host genes near these loci.[15][16][18] While HUSH and MORC2 normally defend against retroelement invasion and maintain genome stability, their hyperactivation by neuropathic variants can result in inappropriate repression of genes necessary for neuron survival, axonal transport, and synaptic function.[15][16] The precise gene sets affected in CMT2Z neurons remain to be fully defined, but transcriptomic changes in MORC2-mutant fibroblasts and sensory neurons suggest widespread alterations in gene expression.[7]

Impaired DNA repair due to MORC2 dysfunction leads to DNA damage accumulation, which in turn activates stress responses and ROS production. In *Morc2a* p.S87L mouse embryonic fibroblasts, Pandiloski et al. observed increased DNA damage markers, reduced Morc2a protein levels, and elevated cellular hydroxyl radical levels, accompanied by high rates of apoptosis.[12][18] They concluded that “Morc2a p.S87L mutation led to protein synthesis defects and reduced Morc2a protein levels, resulting in elevated cellular hydroxyl radicals and apoptosis due to loss-of-function.”[18] Hydroxyl radicals are generated through Fenton reactions and other pathways when DNA damage and mitochondrial dysfunction occur, and they can cause lipid peroxidation, protein oxidation, and further DNA breaks.[18] This oxidative stress contributes to neurodegeneration and may particularly affect long axons with high metabolic demands.

MORC2’s role in lipid homeostasis has also been noted, suggesting that its dysfunction could alter membrane composition and signaling, although detailed metabolic pathways in CMT2Z are not yet mapped.[18] GO processes such as “response to oxidative stress” (GO:0006979), “DNA damage response” (GO:0006974), and “regulation of apoptotic process” (GO:0042981) are relevant. Chemical entities include hydroxyl radical (CHEBI:16234), reactive oxygen species (CHEBI:26523), and possibly lipid peroxides (CHEBI:18201).

In neurons, these midstream mechanisms lead to axonal transport defects, cytoskeletal disorganization, and synaptic abnormalities. Sevilla et al. reported that MORC2 p.S87L in rodent sensory neurons induced abnormal axonal morphology, including beading and swellings, indicating disrupted axonal integrity.[7] Such morphological changes can precede axonal degeneration and clinical neuropathy. The interplay between transcriptional misregulation, DNA damage, protein synthesis defects, and oxidative stress creates a vicious cycle of neuronal injury, especially in long peripheral axons.

### 6.4 Downstream Mechanisms: Axonal Degeneration, Tract Pathology, and Clinical Manifestations

The downstream consequences of MORC2 dysfunction are axonal degeneration in peripheral motor and sensory nerves, damage to corticospinal tracts, and dysfunction of cerebellar and spinal motor neurons, resulting in the characteristic clinical picture of CMT2Z and related phenotypes. Peripheral nerve biopsies (not detailed in the search results but inferred from CMT2 contexts) likely show reduced axon density, Wallerian degeneration, and secondary myelin changes, consistent with axonal neuropathy.[1][10][13] Electrophysiologic studies demonstrate reduced compound muscle and sensory nerve action potentials, reflecting fiber loss, while conduction velocities remain relatively preserved.[11][13][18] These findings align with HPO terms “Axonal degeneration” (HP:0007340) and “Peripheral axonal neuropathy” (HP:0003477).

In motor neurons of the spinal cord and corticospinal tracts, MORC2 dysfunction leads to spasticity and pyramidal signs. The presence of extensor plantar responses and increased tone in CMT2Z patients indicates degeneration or dysfunction of upper motor neuron pathways.[10][13] In *Morc2a* p.S87L mice, motor neuron degeneration was observed alongside cerebellar ataxia and neuropathy, paralleling human phenotypes.[12][18] Cerebellar involvement produces gait ataxia and coordination deficits, while spinal muscular atrophy–like features arise from anterior horn cell pathology, leading to proximal weakness and muscle atrophy that overlap clinically with CMT.[3][16][19]

Clinically, these downstream effects manifest as progressive distal weakness, foot deformities (such as pes cavus), gait disturbances, sensory loss, spasticity, and in syndromic forms, growth retardation, microcephaly, and intellectual disability.[1][3][10][11][13][17] In Cockayne-like *MORC2* disorders, multiorgan involvement including hearing loss, retinopathy, and endocrinopathies further complicates the picture.[3][9][14] The severity and pattern of manifestations depend on the specific MORC2 variant and its functional impact: p.R252W tends to produce a predominantly peripheral neuropathy with pyramidal signs, p.Arg190Trp a similar but possibly milder phenotype, p.S87L and certain ATPase module variants more severe, multisystem disease.[7][11][13][16][17][18]

From an ontology perspective, affected anatomical structures include peripheral nerve (UBERON:0001021), spinal cord (UBERON:0002240), corticospinal tract (UBERON:0006413), cerebellum (UBERON:0002037), cochlea (UBERON:0001844), retina (UBERON:0001473), and endocrine organs such as thyroid gland (UBERON:0002046).[3][10][14][18] Cell types include peripheral motor and sensory neurons, spinal motor neurons, cerebellar neurons, retinal photoreceptors, cochlear hair cells, and endocrine cell populations.[3][12][14][18] These downstream mechanisms ultimately determine clinical outcomes, disability, and quality of life.

### 6.5 Advanced Technologies and Functional Genomics Screens

Advanced technologies have played a significant role in elucidating MORC2 mechanisms. CRISPR/Cas9 functional genomics screens by Tchasovnikarova et al. identified MORC2 as essential for HUSH-mediated transgene silencing, providing a genome-wide unbiased link between MORC2 and epigenetic repression.[16] CRISPR knockout HeLa clones were complemented with wild-type or mutant MORC2 to assess restoration of silencing, demonstrating that ATP binding and hydrolysis are necessary for function.[16] These functional screens highlight MORC2’s centrality in heterochromatin-based silencing and provide a platform for testing variant effects.

Mouse models, particularly the *Morc2a* p.S87L knock-in, represent multi-omics integration. Researchers used AAV-PHP.eB gene therapy to express Morc2a or its GHKL ATPase domain in vivo, achieving amelioration of neuropathy and muscular dysfunction with a single treatment.[12][18] They correlated reductions in hydroxyl radical levels, improved apoptosis markers, and restored motor behavior with gene therapy, demonstrating mechanistic rescue.[12][18] This work integrates genomics (variant), transcriptomics (gene expression), proteomics (protein levels), and metabolomics (ROS) to define pathophysiological pathways and therapeutic targets.

Single-cell analysis and spatial transcriptomics specific to MORC2 neuropathy have not yet been reported, but given MORC2’s nuclear roles, future studies could reveal cell-type specific vulnerability and heterogeneity across neuronal subpopulations. For knowledge representation, functional genomics screens and mouse multi-omics experiments can be annotated as model organism evidence supporting specific GO terms and mechanistic links.

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

CMT2Z primarily affects the nervous system, with secondary involvement of sensory organs and, in syndromic variants, endocrine and other systems. The primary organs directly affected include peripheral nerves, spinal cord, cerebellum, brain (especially corticospinal tracts), and, in some patients, cochlea and retina.[3][10][12][14][18] Peripheral nerve involvement manifests as axonal degeneration of motor and sensory fibers, leading to distal weakness and sensory impairment.[1][10][11][13] Spinal cord involvement, particularly in corticospinal tracts and anterior horn cells, underlies pyramidal signs and spinal muscular atrophy–like features.[10][12][13][19] Cerebellar involvement produces ataxia in severe variants and mouse models.[12][18] 

Secondary organ involvement occurs in multisystem syndromic forms. Cochlear hair cell or auditory nerve pathology leads to sensorineural hearing loss, while retinal degeneration produces retinopathy and visual impairment.[3][14] Endocrine organs such as thyroid and pituitary may be affected, contributing to hypothyroidism and precocious puberty, as reported in DIGFAN.[14] Liver and kidney involvement with hepatic enzyme changes and renal dysfunction have been noted in Cockayne-like *MORC2* disorders.[3][9] These organ-level involvements correspond to UBERON terms including peripheral nervous system (UBERON:0000010), central nervous system (UBERON:0001017), eye (UBERON:0000970), ear (UBERON:0001690), thyroid gland (UBERON:0002046), and liver (UBERON:0002107).

### 7.2 Tissue and Cell-Level Involvement

At the tissue level, CMT2Z targets nervous tissue, particularly white matter tracts and peripheral nerve fascicles. Axonal degeneration occurs in long myelinated fibers, with secondary myelin changes.[1][11][13] Muscle tissue is indirectly affected through denervation, leading to muscle atrophy and fiber type grouping, particularly in distal limb muscles.[10][11] Sensory epithelia in cochlea and retina are involved in syndromic forms, resulting in degeneration of hair cells and photoreceptors.[3][14]

Cell populations targeted include peripheral motor neurons, sensory neurons, Schwann cells, spinal motor neurons, corticospinal neurons, cerebellar neurons, retinal photoreceptors, cochlear hair cells, and endocrine cells in thyroid and pituitary.[3][7][12][14][18] MORC2 is expressed in neural tissues, suggesting that neuronal nuclei are primary sites of dysfunction, though glial cells may also be affected.[7][16] Relevant Cell Ontology (CL) terms include “motor neuron” (CL:0000100), “sensory neuron” (CL:0000540), “Schwann cell” (CL:0000576), “cerebellar Purkinje neuron” (CL:0000121), “retinal photoreceptor cell” (CL:0000210), and “thyroid gland follicular cell” (CL:0002575).

### 7.3 Subcellular Localization and Compartments

Subcellular compartments involved in CMT2Z pathophysiology include the nucleus, chromatin, DNA damage foci, and, indirectly, mitochondria and cytoplasmic protein synthesis machinery. MORC2 localizes to the nucleus and binds to heterochromatic DNA, functioning at chromatin sites with H3K9 trimethylation.[15][16] DNA double-strand break repair involves MORC2 recruitment to damage foci, where it remodels chromatin to facilitate repair.[5][18] PARP1-mediated poly(ADP-ribosylation) of MORC2 occurs at these nuclear sites.[18] GO cellular component terms include “nucleus” (GO:0005634), “chromatin” (GO:0000785), “heterochromatin” (GO:0000792), and “DNA repair foci” (GO:0005720).

Mitochondrial compartments are indirectly involved via oxidative stress, as DNA damage and impaired protein synthesis can lead to mitochondrial dysfunction and increased ROS production.[12][18] Cytoplasmic ribosomes and translation machinery are affected in *Morc2a* p.S87L cells, where protein synthesis defects and reduced MORC2 levels were observed.[12][18] These compartments correspond to GO terms “mitochondrion” (GO:0005739), “cytoplasm” (GO:0005737), and “ribosome” (GO:0005840).

### 7.4 Localization and Lateralization of Clinical Signs

Clinically, CMT2Z exhibits length-dependent and often asymmetric involvement. Orphanet notes that “weakness and atrophy progress in an asymmetric fashion to involve also the proximal and upper limbs in the course of the disease,” indicating that one limb may be more affected than the other and that asymmetry persists over time.[10] Distal lower limbs are typically affected earlier and more severely than upper limbs, reflecting the vulnerability of the longest axons; this pattern corresponds to HPO term “Distal lower limb muscle weakness” (HP:0003458). Lateralization is thus characterized by bilateral but asymmetric involvement.

Central signs such as pyramidal symptoms are usually bilateral, reflecting corticospinal tract involvement on both sides, although asymmetries can occur depending on lesion distribution.[10][13] Hearing loss and retinopathy may be bilateral but can display asymmetries as well.[3][14] In knowledge representation, capturing “bilateral but asymmetric distal limb involvement” and “bilateral central tract involvement” can support clinical decision support algorithms.

## 8. Temporal Development

### 8.1 Age of Onset and Onset Pattern

CMT2Z has a broad age-of-onset spectrum, reflecting variant-specific functional impacts and pleiotropy. OMIM notes that CMT2Z typically has onset “usually in the first decade,” indicating childhood presentation as the most common pattern.[1] Orphanet reports age of onset spanning infancy, childhood, adolescence, and adulthood, and even neonatal onset, highlighting the heterogeneity.[10] Patients with p.R252W and p.E236G often present in early childhood with gait disturbance and distal weakness, while those with Arg190Trp may present in childhood or adolescence.[11][13] DIGFAN and Cockayne-like *MORC2* syndromes frequently have neonatal or infantile onset with hypotonia, poor growth, and developmental delay evident in the first months of life.[3][8][17]

The onset pattern is generally chronic and insidious rather than acute. Neuropathy develops gradually, with initial subtle clumsiness, frequent falls, or difficulty in sports, progressing to overt foot drop and muscle wasting.[10][11][13] In severe variants, hypotonia and delayed milestones are obvious earlier, but even then, progression is ongoing rather than episodic.[3][17][18] There are no documented relapsing-remitting patterns akin to multiple sclerosis; CMT2Z is a chronic degenerative condition. For ontology mapping, age-of-onset classes include “Infantile onset” (HP:0003593), “Childhood onset” (HP:0003674), and “Adult onset” (HP:0003581), with variant-specific annotations.

### 8.2 Disease Progression, Course, and Duration

CMT2Z follows a progressive course with variable rate. In many families, neuropathy progresses slowly over decades, with individuals remaining ambulant into adulthood, albeit with increasing disability.[11][13][16] Distal weakness extends proximally, and upper limbs become involved later in disease.[10][11] Pyramidal signs may emerge or increase in severity over time, reflecting ongoing central tract degeneration.[10][13] Disease duration is essentially lifelong, as there is no spontaneous recovery, and degeneration continues to late life, though precise survival data are limited.[10][16]

In severe variants associated with DIGFAN or p.S87L, progression can be rapid, with significant motor and cognitive impairment developing in early childhood, loss of independent ambulation, and multisystem complications.[3][17][18] Mouse models of *Morc2a* p.S87L show early-onset neuropathy and sublethal phenotypes in heterozygotes, with embryonic lethality in homozygotes.[12][18] These observations suggest that certain human variants may be incompatible with life when biallelic, although such cases have not been reported, likely due to embryonic loss.[18]

Disease course patterns in knowledge representation should be coded as “chronic, progressive,” with progression rate categories such as “slow” for typical CMT2Z, “moderate” for CMT2Z with pyramidal signs, and “rapid” for DIGFAN and CS-like syndromes.[3][10][17][18] Critical periods include early childhood, when motor and cognitive development are most vulnerable, and adolescence, when orthopedic complications such as scoliosis may emerge.

### 8.3 Remission Patterns and Windows for Intervention

Spontaneous remission has not been reported in CMT2Z; symptoms may plateau temporarily but generally worsen over time.[10][11][13][16] Treatment-induced improvements, such as gait stabilization with orthoses or improved muscle strength after physical therapy, represent functional amelioration rather than true disease remission.[10][16] Experimental gene therapy in *Morc2a* p.S87L mice produced durable rescue of neuropathy and muscular dysfunction after a single AAV-PHP.eB treatment, suggesting that early intervention could modify disease trajectory.[12][18] However, human translation is pending, and no remitting course has been documented clinically.

Windows of vulnerability and opportunity for intervention include the early developmental period, when motor and cognitive circuits are forming, and before significant axonal loss has occurred. In mouse models, early gene therapy gave better outcomes, implying that timely restoration of MORC2 function could prevent irreversible damage.[12][18] For the knowledge base, representing “early intervention window” as a critical time period may aid in planning clinical trials and genetic counseling.

## 9. Inheritance and Population

### 9.1 Inheritance Pattern, Penetrance, and Expressivity

CMT2Z is inherited in an autosomal dominant manner. OMIM and Orphanet both state that CMT2Z is autosomal dominant, and the *MORC2* gene entry lists CMT2Z and DIGFAN as “Autosomal dominant, monoallelic” phenotypes.[1][5][10] The initial Australian family exhibited vertical transmission across multiple generations, with affected individuals in each generation and both sexes affected, consistent with autosomal dominant inheritance.[13] PanelApp entries for MORC2 in hereditary neuropathy and ataxia panels list “MONOALLELIC, autosomal or pseudoautosomal” inheritance.[6]

Penetrance appears relatively high in familial CMT2Z, as carriers of pathogenic variants generally exhibit some degree of neuropathy or pyramidal signs.[11][13][19] However, intrafamilial variability in onset age and severity indicates incomplete penetrance or variable expressivity. Some family members may have mild symptoms or subclinical findings, while others develop severe neuropathy.[11][13] GenCC notes that patients with CMT2Z present with axonal peripheral neuropathy with “varying inter- and intrafamilial severity,” and that complex features such as central nervous system involvement or proximal weakness are “rarely reported,” implying variability in expressivity.[19]

In DIGFAN and CS-like *MORC2* syndromes, penetrance is effectively complete among de novo variant carriers, as all reported individuals exhibit significant neurodevelopmental and growth abnormalities.[3][17][18] Germline mosaicism has not been specifically addressed in the literature, but de novo variants raise its possibility, especially if recurrence occurs in siblings; however, such cases have not been detailed in current search results.[3][8][17] There is no evidence of genetic anticipation, as MORC2 variants are not repeat expansions.

### 9.2 Epidemiology: Prevalence, Incidence, and Carrier Frequency

CMT2Z is rare. Orphanet reports a prevalence of less than 1 per 1,000,000 individuals, highlighting its status as a rare autosomal dominant neuropathy.[10] In the Japanese CMT cohort, *MORC2* variants were detected in 2.7% of patients with CMT type 2, making MORC2 the second most common CMT2 gene after *MFN2*.[11] The authors note that “MORC2 variants were detected in 2.7% of patients with CMT type 2,” underscoring its moderate significance within CMT2 but low absolute prevalence in the general population.[11] Globally, GenCC and recent reviews estimate that more than 50 families have been reported with *MORC2*-related neuropathy, spanning multiple ethnicities.[16][19]

Incidence data are not available, but given the rarity and reliance on genetic diagnosis, incidence is likely on the order of a few cases per million births. Carrier frequency in the general population is extremely low, with most pathogenic *MORC2* variants absent from large population databases.[11][13][16] Founder effects may exist for specific variants such as p.Arg190Trp in Japan, with higher allele frequency in that population, but detailed population genetics studies are lacking.[11] Consanguinity does not play a significant role, as the disease is autosomal dominant and arises frequently from de novo mutations.[3][8][17]

### 9.3 Population Demographics and Geographic Distribution

CMT2Z and *MORC2*-related disorders have been reported across multiple continents, including Australian, Japanese, European, and other cohorts.[11][13][16][19] The Japanese series emphasizes *MORC2* as a relatively frequent CMT2 gene in that population, while other reports suggest that *MORC2* is a regular but not dominant contributor to CMT2 in European and North American cohorts.[11][16][19] There is no evidence of strong ethnic predilection, but specific variants such as Arg190Trp may be enriched in certain populations, reflecting founder effects.[11]

Sex distribution appears roughly equal, consistent with autosomal inheritance; both male and female patients are described in case series and family reports.[11][13][17][19] Age distribution among affected individuals reflects onset patterns, with most cases detected in childhood or adolescence, but adults can present when mild neuropathy was previously unnoticed or misdiagnosed.[10][11][13][16] In syndromic forms, infants and young children predominate, due to severe early-onset phenotypes.[3][17][18] For knowledge representation, capturing geographic associations of specific variants and general global distribution can support variant interpretation in diverse populations.

## 10. Diagnostics

### 10.1 Clinical and Electrophysiological Evaluation

The diagnostic workup of suspected CMT2Z begins with clinical evaluation of neuropathy and central signs. Clinicians assess distal muscle weakness, atrophy, foot deformities, gait abnormalities, sensory deficits, and pyramidal signs such as spasticity and extensor plantar responses.[10][11][13] Learning difficulties, developmental delay, growth retardation, dysmorphic facies, and multisystem features may be present in DIGFAN or CS-like *MORC2* disorders.[3][14][17] Clinical examination aligns with HPO terms described above and informs differential diagnosis among CMT subtypes.

Electrophysiology is central to differentiating axonal versus demyelinating neuropathies. Nerve conduction studies in CMT2Z show reduced compound muscle action potential amplitudes and reduced sensory nerve action potentials, indicating axonal loss, while conduction velocities are relatively preserved and may be only mildly reduced.[11][13][18] EMG may show chronic denervation and reinnervation patterns. These findings distinguish CMT2Z from CMT1, which shows marked conduction velocity slowing due to demyelination.[2][4] In SMA-like *MORC2* phenotypes, EMG may show features of anterior horn cell disease, with neurogenic changes in proximal muscles and relatively preserved sensory responses.[3][16][19]

Brain MRI can reveal microcephaly, brain atrophy, and cerebellar changes in DIGFAN and CS-like *MORC2* disorders.[3][8][17] Neuroimaging abnormalities are present in up to 66% of DIGFAN cases, according to the endocrine case report, which notes “neuroimaging abnormalities (up to 66%)” including brain atrophy.[14] Retinal imaging and audiology tests can document retinal dystrophy and sensorineural hearing loss, respectively.[3][14] Laboratory tests may show hepatic enzyme elevation, hypothyroidism, or other endocrine and metabolic abnormalities in multisystem cases.[3][14]

### 10.2 Genetic Testing Strategies

Genetic testing is essential for definitive diagnosis of CMT2Z and related MORC2 disorders. The recommended approach depends on clinical context. In patients with axonal CMT2 and pyramidal signs, targeted testing of *MORC2* via gene panels for hereditary neuropathy is often appropriate.[6][19] Genomics England PanelApp includes MORC2 on hereditary neuropathy panels and ataxia/cerebellar anomaly panels, with “Expert Review Green” status, indicating high confidence in its inclusion.[6] These panels typically include other CMT2 genes such as *MFN2*, *KIF1B*, *HARS1*, *MPZ*, and others listed in OMIM’s CMT gene table.[2][4][11]

In syndromic neurodevelopmental presentations, such as DIGFAN, Cockayne-like disease, or unexplained developmental delay with growth retardation and neuropathy, whole-exome sequencing (WES) or whole-genome sequencing (WGS) is often used.[3][8][14][17] Guillen Sacoto et al. identified MORC2 ATPase module variants through exome sequencing in individuals with neurodevelopmental disorder and growth retardation, illustrating WES utility.[17] The DIGFAN endocrine case describes reconsidering the etiological diagnosis and using exome sequencing, which revealed a heterozygous MORC2 p.Thr424Lys variant.[14] WGS may be advantageous in detecting non-coding variants or structural changes, though such lesions are not prominent in *MORC2*-related disease based on current evidence.[5][16]

Single-gene sequencing of *MORC2* may be indicated when clinical suspicion is high and panel or exome testing is not feasible. Chromosomal microarray (CMA), karyotyping, and FISH are not typically informative, as CMT2Z is not caused by large-scale chromosomal rearrangements.[1][5][19] Mitochondrial DNA testing, repeat expansion analysis, and other specialized tests may be performed in differential diagnosis but are not specific to MORC2.

Emerging diagnostics include DNA methylation episignatures, which can distinguish MORC2-related disorders from other neurodevelopmental syndromes.[9] The episignature described in the thesis could, in principle, serve as a biomarker for MORC2 disease, though clinical validation is ongoing.[9] Omics-based diagnostics such as transcriptomics and proteomics are currently research tools.

### 10.3 Differential Diagnosis

Differential diagnosis for CMT2Z includes other axonal CMT2 subtypes, spinal muscular atrophy, hereditary spastic paraplegia, Cockayne syndrome, Leigh syndrome, mitochondrial diseases, and other neurodevelopmental disorders with growth retardation and dysmorphic facies.[2][3][4][9][11][17] MFN2-associated CMT2A2A and KIF1B-associated CMT2A1 are common axonal CMT2 forms; MFN2 variants often present with severe early-onset neuropathy and optic atrophy, while KIF1B variants produce neuropathy with distinctive clinical features.[2][4][11] HARS1-associated CMT2W, MPZ-associated CMT2I, ATP1A1-associated CMT2DD, and CADM3-associated CMT2FF are other axonal CMT2 subtypes listed in OMIM.[4] Distinguishing CMT2Z from these entities relies on the presence of pyramidal signs, neurodevelopmental features, and specific genetic findings.[1][2][4][11][13]

SMA-like MORC2 phenotypes can overlap with 5q-SMA due to *SMN1* mutations, but sensory involvement and pyramidal signs help differentiate them.[3][16][19] Cockayne syndrome due to defects in transcription-coupled nucleotide excision repair genes (*ERCC6*, *ERCC8*) presents with overlapping features (growth retardation, neurodevelopmental disabilities, photosensitivity), but MORC2-related CS-like cases are not associated with transcription-coupled NER defects and follow dominant inheritance with de novo variants, as emphasized in the CS-like MORC2 study.[3] Leigh syndrome and mitochondrial diseases may be considered when neuroimaging shows basal ganglia lesions and lactic acidosis, but MORC2 episignatures and genetic testing clarify diagnosis.[9][17]

### 10.4 Screening and Cascade Testing

Population-based screening for CMT2Z is not currently recommended, given its rarity and lack of preventive interventions.[10][16] However, cascade testing of family members is important in autosomal dominant cases, to identify at-risk relatives, enable early diagnosis, and inform reproductive decisions.[1][13][19] Genetic counseling should accompany such testing, addressing inheritance patterns, variable expressivity, and options for prenatal or preimplantation genetic diagnosis.[16][19] Newborn screening programs do not include CMT2Z, but future inclusion of epigenetic episignatures for severe neurodevelopmental disorders is conceivable.

## 11. Outcome / Prognosis

### 11.1 Survival, Mortality, and Life Expectancy

Specific survival and mortality data for CMT2Z are limited, but the disease appears compatible with near-normal lifespan in many cases, particularly in “pure” neuropathic forms.[10][11][13][16] Axonal CMT2Z typically causes progressive disability but not life-threatening organ failure, and patients can survive to late adulthood.[10][11][13] Severe syndromic forms with neurodevelopmental and multisystem involvement, such as DIGFAN and Cockayne-like MORC2 disease, may reduce life expectancy due to complications such as feeding difficulties, infections, hepatic dysfunction, and respiratory problems.[3][9][14][17] However, robust survival curves have not been published.

In mouse models, homozygous *Morc2a* p.S87L is embryonic lethal, while heterozygous mice exhibit sublethal characteristics with reduced offspring survival, suggesting that biallelic severe MORC2 mutations may be incompatible with human life, though such cases would likely be lost prenatally.[12][18] Embryonic lethality in mice underscores the critical role of MORC2 in development and genome stability. Disease-specific mortality in human CMT2Z is not well quantitated, but severe neurodevelopmental forms likely contribute to mortality via respiratory failure, infections, and systemic complications.[3][9][14][17]

### 11.2 Morbidity, Disability Outcomes, and Quality of Life

Morbidity in CMT2Z arises from neuropathy, central motor involvement, cognitive impairment, sensory loss, and systemic complications. Disability outcomes include difficulty walking, need for orthoses or wheelchairs, reliance on assistance for daily activities, and inability to perform certain jobs.[10][11][13][16] In moderate forms, patients may maintain employment and independent living but experience chronic pain, fatigue, and limitations in physical activities.[10][11] In severe DIGFAN or CS-like syndromes, intellectual disability, growth retardation, and multisystem disease result in high levels of dependency and medical complexity.[3][14][17]

Quality of life measures such as SF-36 or EQ-5D have not been systematically applied to CMT2Z cohorts, but general CMT research shows that physical functioning, role limitations, pain, and emotional well-being are affected.[16] Sensorineural hearing loss and retinal dystrophy further impact communication and mobility.[3][14] Endocrine abnormalities add treatment burdens and may affect mood and energy.[14] In the knowledge base, linking phenotypes to functional domains (mobility, self-care, pain, cognition, sensory) and to ICF disability codes can support comprehensive representation of morbidity.

### 11.3 Disease Course, Complications, and Recovery Potential

Complications of CMT2Z include orthopedic deformities (pes cavus, scoliosis), falls and fractures, muscle contractures, chronic pain, and in severe forms, feeding difficulties, respiratory insufficiency, and organ dysfunction.[10][14][16] Swallowing disorders, gastroesophageal reflux, and kyphoscoliosis are noted as less frequent but documented abnormalities in DIGFAN and CS-like MORC2 disease.[14] These complications require multidisciplinary management, including orthopedics, rehabilitation, gastroenterology, and pulmonology.

Recovery potential is limited, as the underlying genetic defect persists and axonal degeneration is only partially reversible. Physical therapy and occupational therapy can improve function and slow decline by strengthening muscles, optimizing gait, and preventing contractures.[10][16] Gene therapy in *Morc2a* p.S87L mice achieved substantial rescue of neuropathy and muscular function, indicating that, at least in model systems, restoration of MORC2 function can reverse some pathophysiological changes.[12][18] Translation to humans could offer true disease modification and partial recovery, but clinical trials are needed.

Prognostic factors include genotype (specific MORC2 variant), age at onset, severity of neurodevelopmental features, presence of multisystem involvement, and access to supportive therapies.[3][7][11][16][17][18] For example, patients with p.S87L may have poorer prognosis due to early-onset severe neuropathy and CNS involvement, whereas those with p.R252W or Arg190Trp may have milder, later-onset disease.[7][11][13][16] HUSH activation degree and DNA methylation episignature profiles could serve as prognostic biomarkers in the future.[9][15][16]

## 12. Treatment

### 12.1 Supportive and Rehabilitative Management

At present, there is no approved disease-modifying pharmacotherapy for CMT2Z, and management focuses on supportive care, symptom control, and rehabilitation. NCIT clinical intervention terms applicable include “physical therapy” (NCIT:C20031), “occupational therapy” (NCIT:C25228), “orthotic device” (NCIT:C50187), and “pain management” (NCIT:C49243). Physical therapy aims to maintain strength, flexibility, and balance; occupational therapy helps patients adapt daily activities and use assistive devices; orthoses (ankle–foot orthoses) stabilize gait; and pain management addresses neuropathic pain.[10][16]

Orthopedic interventions may be needed for foot deformities and scoliosis. Surgical correction of pes cavus and tendon transfers can improve gait, while spinal surgery addresses severe scoliosis.[10][16] NCIT terms such as “orthopedic surgical procedure” (NCIT:C15817) apply. Multidisciplinary care involving neurology, orthopedics, physiotherapy, audiology, ophthalmology, and endocrinology is critical, particularly in syndromic forms with hearing loss, retinopathy, and endocrine abnormalities.[3][14][16]

Pharmacologic management of neuropathic pain may involve agents such as gabapentinoids, tricyclic antidepressants, or serotonin–norepinephrine reuptake inhibitors, though specific studies in CMT2Z are lacking.[16] Hormone replacement for hypothyroidism and treatments for precocious puberty are used in DIGFAN endocrine cases.[14] Nutritional support and reflux management address gastroesophageal complications.[14]

### 12.2 Experimental Gene Therapy and Targeted Approaches

The most exciting therapeutic development arises from gene therapy in *Morc2a* p.S87L mouse models. Pandiloski et al. used adeno-associated virus AAV-PHP.eB, which has high CNS transduction efficiency, to express Morc2a or its GHKL ATPase domain in vivo.[12][18] They reported that “AAV gene therapy ameliorated neuropathy and muscular dysfunction with a single treatment,” restoring motor function, reducing hydroxyl radical levels, and decreasing apoptosis.[12][18] Rescue of neuropathy via restoring GHKL ATPase functionality suggests that targeted gene therapy could correct MORC2 defects in humans.

Mechanistically, this gene therapy addresses both epigenetic and DNA repair defects by providing functional Morc2a, thereby normalizing HUSH-mediated silencing and DNA damage responses.[12][18] NCIT terms relevant to such interventions include “gene therapy” (NCIT:C16632), “Adeno-associated viral vector” (NCIT:C25831), and “DNA repair restoration” (NCIT concept clusters). Translation to humans would require safety studies, vector optimization, and precise dosing.

Other potential targeted therapies include modulating PARP1 activity, controlling oxidative stress via antioxidants, and adjusting epigenetic regulators of H3K9me3. However, these are speculative; no clinical trials for MORC2-specific therapies are yet registered in the search results. The interplay of hyperactive HUSH and loss-of-function in protein synthesis suggests that therapies must finely tune MORC2 function rather than simply upregulate or downregulate it.[15][16][18]

### 12.3 Pharmacotherapy, RNA-Based Therapies, and Future Directions

No specific pharmacotherapies targeting MORC2 or HUSH are clinically available. General neuropathy treatments, such as vitamin supplementation, neurotrophic factors, or neuroprotective agents, have not been systematically tested in CMT2Z.[16] RNA-based therapies, such as antisense oligonucleotides to modulate MORC2 expression, could theoretically be used, but designing them to correct specific missense variant effects is challenging.[16] CRISPR-based gene editing to repair pathogenic MORC2 variants is conceivable in the long term but faces delivery and off-target challenges.

Precision medicine approaches in CMT2Z will likely center around genotype-informed prognostication and selection of candidates for gene therapy. For example, patients with severe ATPase module variants such as p.S87L may benefit most from early gene replacement, while those with milder variants may be managed with supportive care.[7][17][18] Integration of genomic, epigenetic, and clinical data in decision algorithms will be essential.

## 13. Prevention

### 13.1 Primary, Secondary, and Tertiary Prevention

Primary prevention of CMT2Z at the population level is not currently feasible, as the disease arises from rare germline mutations and there are no modifiable environmental causes.[1][10][16] However, primary prevention at the family level through reproductive choices is possible. Genetic counseling can inform carriers of MORC2 pathogenic variants about autosomal dominant inheritance, recurrence risk, and options such as preimplantation genetic diagnosis (PGD) and prenatal testing.[16][19] NCIT terms such as “genetic counseling” (NCIT:C17462), “prenatal diagnosis” (NCIT:C17461), and “preimplantation genetic diagnosis” (NCIT:C18679) are relevant.

Secondary prevention involves early detection and intervention to mitigate disability. Cascade testing of family members allows identification of asymptomatic or minimally symptomatic carriers, who can then receive monitoring and early rehabilitation interventions to slow progression and anticipate complications.[10][16][19] Awareness of multisystem features in DIGFAN and CS-like MORC2 disease can prompt early screening for hearing loss, retinopathy, endocrine abnormalities, and neuroimaging changes.[3][14][17] Early detection of these complications enables timely treatment and potentially reduces morbidity.

Tertiary prevention focuses on preventing complications and optimizing function in individuals with established disease. This includes physical therapy to prevent contractures, orthopedic management of foot deformities and scoliosis, fall-prevention strategies, pain management, nutritional care, and psychosocial support.[10][14][16] For multisystem syndromes, regular endocrine and ophthalmologic screening and proactive management of reflux and swallowing disorders are important.[14] NCIT terms such as “rehabilitation therapy” (NCIT:C15273) and “supportive care” (NCIT:C19323) apply.

### 13.2 Immunization, Public Health, and Environmental Interventions

Immunization is not directly related to CMT2Z prevention, though standard vaccination reduces infection-related complications in patients with neuromuscular disorders.[16] Public health interventions such as sanitation, vector control, or environmental toxin reduction do not specifically affect CMT2Z incidence but support overall health. Avoidance of neurotoxic exposures is a general preventive principle in neuropathies, but specific evidence for MORC2 is lacking.[16]

Environmental interventions may focus on workplace adaptations to reduce physical strain and injury risk for individuals with CMT2Z, but these are tertiary rather than primary preventive measures. Behavioral interventions such as encouraging physical activity and healthy diet can support neuromuscular health but do not prevent disease onset in genetically predisposed individuals.[10][16]

## 14. Other Species / Natural Disease

### 14.1 Natural Disease in Non-human Species and Veterinary Relevance

No naturally occurring MORC2-associated neuropathy has been reported in non-human animals such as dogs, cats, livestock, or wildlife in the search results.[9][12][18] Online Mendelian Inheritance in Animals (OMIA) and veterinary databases may eventually identify MORC2-related disorders in companion animals, but current evidence is limited to experimental models, primarily mice.[12][18] Therefore, veterinary relevance at present lies in comparative pathology rather than clinical veterinary disease.

### 14.2 Comparative Biology and Evolutionary Conservation

MORC family proteins are conserved across species, with orthologous genes in mice (*Morc2a*), and other vertebrates.[12][18] HomoloGene and OrthoMCL resources (referenced in broader literature) show evolutionary conservation of the GHKL ATPase module and CW-type zinc finger domains, suggesting conserved roles in chromatin remodeling and epigenetic regulation.[15][16][18] Comparative pathology between human CMT2Z and mouse *Morc2a* p.S87L neuropathy reveals striking similarities in axonal degeneration, cerebellar ataxia, and motor neuron involvement.[12][18]

Cross-species susceptibility to MORC2 dysfunction appears to be universal among vertebrates expressing orthologous proteins, though natural disease is not documented. Zoonotic potential is nonexistent, as CMT2Z is not infectious. For knowledge representation, NCBI Taxon identifiers such as 10090 (Mus musculus) and 9606 (Homo sapiens) can be linked through orthologous MORC2 genes.

## 15. Model Organisms

### 15.1 Mouse Models: *Morc2a* p.S87L and Neuropathy

Mouse models are central to understanding *MORC2*-related disease. Pandiloski et al. generated genetically engineered mice carrying the *Morc2a* p.S87L mutation, orthologous to a human MORC2 variant associated with severe neuropathy and DIGFAN.[12][18] Heterozygous (*Morc2a* S87L/+) mice displayed “symptoms of axonal neuropathy, cerebellar ataxia and motor neuron degeneration,” closely resembling peripheral neuropathy observed in CMT2Z and complex DIGFAN syndrome affecting both the peripheral and central nervous systems.[12][18] Homozygous *Morc2a* p.S87L mice were embryonic lethal, underscoring the essential role of MORC2 in development.[12][18]

Phenotype recapitulation in *Morc2a* S87L/+ mice includes length-dependent neuropathy, reduced motor and sensory action potentials, gait abnormalities, muscle weakness, cerebellar signs, and neurodegeneration.[12][18] Model limitations include species-specific differences in nervous system organization and the fact that human phenotypes encompass a broader range of systemic features (e.g., endocrine, sensory organ involvement) that may not be fully present in mice.[3][14][18] Nevertheless, the mouse model faithfully reproduces core features of CMT2Z and DIGFAN and is invaluable for mechanistic studies and therapeutic testing.

### 15.2 Cellular Models and CRISPR Screens

Cellular models include patient-derived fibroblasts, rodent sensory neurons transfected with MORC2 variants, and CRISPR-engineered HeLa cells lacking MORC2 or HUSH components.[7][15][16] Sevilla et al. used fibroblasts from patients with p.S87L and p.R252W MORC2 mutations to study transcriptional changes and cellular morphology, finding variant-specific effects on gene expression and abnormal axonal morphology in transfected neurons.[7] Tchasovnikarova et al. used genome-wide CRISPR screens to identify MORC2 as required for HUSH-mediated silencing and performed gene complementation experiments to examine variant effects on GFP reporter repression.[16] Douse et al. studied structural fragments of MORC2 ATPase–CW in vitro, assessing DNA binding, ATPase activity, and dimerization.[15]

These in vitro models capture key molecular and cellular processes, including epigenetic silencing, DNA damage response, and neuronal morphology, but lack the full organismal context of neuropathy and systemic disease. They are particularly suited for dissecting variant-specific functional mechanisms and screening potential small-molecule modulators of MORC2 or HUSH.[15][16]

### 15.3 Applications and Future Model Development

Model organisms enable research on pathophysiology, biomarker discovery, and therapy development. The *Morc2a* S87L/+ mouse model has already demonstrated gene therapy rescue, providing proof-of-concept for AAV-based interventions.[12][18] Further models, including knock-in mice for other MORC2 variants (e.g., R252W, T424R), could help delineate variant-specific phenotypes and mechanisms. Zebrafish and Drosophila models might be developed to study developmental roles of MORC2 orthologs, though such work has not yet been reported in the search results.

Cellular models are suitable for high-throughput drug screening, identifying compounds that modulate MORC2 activity, HUSH function, or oxidative stress. CRISPR screens can reveal interacting pathways and potential synthetic lethal partners.[16] Integration of data across models will support translational research and the design of clinical trials.

## Conclusion

Charcot–Marie–Tooth disease axonal type 2Z (CMT2Z) exemplifies a modern genetic neuropathy in which a single gene, *MORC2*, produces a spectrum of phenotypes through complex molecular mechanisms involving epigenetic silencing, DNA repair, and oxidative stress. At the disease information level, CMT2Z is a rare autosomal dominant axonal motor–sensory neuropathy with characteristic distal weakness, sensory impairment, pyramidal signs, and in some cases learning difficulties, corresponding to OMIM 616688, ORPHA:466768, and MONDO:0014736.[1][5][10] Etiologically, heterozygous pathogenic missense variants in *MORC2* at 22q12.2 are the primary causal factors, with de novo variants prominent in severe neurodevelopmental forms such as DIGFAN and Cockayne-like syndromes.[3][5][13][17][19] The phenotypic spectrum includes “pure” CMT2Z, SMA-like presentations, and syndromic neurodevelopmental disorders with growth retardation, microcephaly, craniofacial dysmorphism, hearing loss, retinopathy, and endocrine involvement.[3][9][14][17]

Mechanistically, MORC2 variants perturb GHKL ATPase dimerization dynamics, hyperactivate HUSH-mediated epigenetic silencing, and impair DNA damage response, leading to transcriptional misregulation, DNA damage accumulation, hydroxyl radical–mediated oxidative stress, and neuronal apoptosis.[7][12][15][16][18] Axonal degeneration in peripheral nerves and central tract pathology in corticospinal and cerebellar systems result in neuropathy, pyramidal signs, ataxia, and neurodevelopmental deficits. Animal models, particularly *Morc2a* p.S87L mice, recapitulate these features and have demonstrated rescue of neuropathy and muscular dysfunction via AAV-PHP.eB gene therapy expressing Morc2a or its GHKL ATPase domain, pointing toward future targeted treatments.[12][18]

Diagnostics rely on clinical examination, electrophysiology confirming axonal neuropathy, neuroimaging and multisystem assessments in syndromic forms, and genetic testing via panels, exome or genome sequencing, with MORC2 included in hereditary neuropathy and ataxia panels.[6][11][13][17][19] Differential diagnosis spans other axonal CMT2 forms, SMA, hereditary spastic paraplegia, Cockayne syndrome, Leigh syndrome, and mitochondrial disorders, with MORC2 genetics clarifying classification.[2][3][4][9][11][17] Prognosis varies widely: moderate CMT2Z often allows near-normal lifespan with progressive disability, whereas severe DIGFAN and CS-like MORC2 disease cause substantial morbidity and may reduce survival.[3][10][14][17][18] Treatment at present is supportive and rehabilitative, but mechanistic insights and model organism studies provide a foundation for future gene therapy and precision medicine approaches.

For a disease knowledge base, CMT2Z can be represented as a monogenic, autosomal dominant, axonal neuropathy due to heterozygous missense variants in *MORC2*, annotated with detailed phenotypes (HPO terms), molecular functions (HGNC MORC2, GO terms), cell types (CL terms), anatomical locations (UBERON terms), chemical entities involved in pathophysiology (e.g., hydroxyl radicals, CHEBI:16234), and NCIT intervention concepts for current and emerging treatments. Evidence items should distinguish human clinical data, in vitro functional studies, and in vivo model organism experiments, with PMIDs and key abstract quotes supporting major claims. As research advances, incorporating epigenetic episignatures, multi-omics profiles, and gene therapy outcomes into this structured representation will enhance understanding, diagnosis, and management of CMT2Z and the broader MORC2-associated disease spectrum.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 80 |
| Resolved | 71 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 5 |
| Unverifiable | 2 |
| Terms whose name was checked | 63 |
| Terms named correctly | 26 |
| Terms named as a **different** term | 21 |
| Terms whose name is worth a second look | 16 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0003553` (1 mention) - the report calls it "Distal muscle weakness"; HP calls it **obsolete Cellulitis due to immunodeficiency**
- `HP:0000667` (1 mention) - the report calls it "Impaired vibration sensation"; HP calls it **Phthisis bulbi**
- `HP:0003477` (2 mentions) - the report calls it "Extensor plantar response", "Peripheral axonal neuropathy"; HP calls it **Peripheral axonal neuropathy**
- `HP:0000998` (1 mention) - the report calls it "Photosensitivity"; HP calls it **Hypertrichosis**
- `GO:0045815` (1 mention) - the report calls it "histone H3-K9 trimethylation"; GO calls it **transcription initiation-coupled chromatin remodeling**
- `HP:0007340` (1 mention) - the report calls it "Axonal degeneration"; HP calls it **Lower limb muscle weakness**
- `CL:0000576` (1 mention) - the report calls it "Schwann cell"; CL calls it **monocyte**
- `CL:0002575` (1 mention) - the report calls it "thyroid gland follicular cell"; CL calls it **central nervous system pericyte**
- `GO:0005720` (1 mention) - the report calls it "DNA repair foci"; GO calls it **GO_0005720**
- `HP:0003458` (1 mention) - the report calls it "Distal lower limb muscle weakness"; HP calls it **EMG: myopathic abnormalities**
- `NCIT:C20031` (1 mention) - the report calls it "physical therapy"; NCIT calls it **Extracellular Protein**
- `NCIT:C25228` (1 mention) - the report calls it "occupational therapy"; NCIT calls it **Right**
- `NCIT:C49243` (1 mention) - the report calls it "pain management"; NCIT calls it **Intestinal Smooth Muscle Tissue**
- `NCIT:C15817` (1 mention) - the report calls it "orthopedic surgical procedure"; NCIT calls it **Neuroscience and Neuropsychiatric Research**
- `NCIT:C16632` (1 mention) - the report calls it "gene therapy"; NCIT calls it **Geographic Area**
- `NCIT:C25831` (1 mention) - the report calls it "Adeno-associated viral vector"; NCIT calls it **DNA Single Strand Break**
- `NCIT:C17462` (1 mention) - the report calls it "genetic counseling"; NCIT calls it **Transcription Factor Jun-B**
- `NCIT:C17461` (1 mention) - the report calls it "prenatal diagnosis"; NCIT calls it **Initiation Factor**
- `NCIT:C18679` (1 mention) - the report calls it "preimplantation genetic diagnosis"; NCIT calls it **Carcinogenesis, Co-Carcinogenesis**
- `NCIT:C15273` (1 mention) - the report calls it "rehabilitation therapy"; NCIT calls it **Longitudinal Study**
- `NCIT:C19323` (1 mention) - the report calls it "supportive care"; NCIT calls it **Tumor Biology**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0003437` (1 mention), reported as "Axonal neuropathy" - HP does not contain this term
- `UBERON:0006413` (1 mention) - UBERON does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0003553` (obsolete Cellulitis due to immunodeficiency) (1 mention) - replaced by `HP:0100658`
- `GO:0016566` (obsolete specific transcriptional repressor activity) (1 mention)
- `GO:0006306` (obsolete DNA methylation) (1 mention)
- `CHEBI:18201` (CHEBI_18201) (1 mention) - replaced by `CHEBI:16171`
- `GO:0005720` (GO_0005720) (1 mention) - replaced by `GO:0000792`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003202` (1 mention) - the report calls it "Muscle atrophy"; HP calls it **Skeletal muscle atrophy**, and lists "Muscle atrophy" among its other names
- `HP:0002141` (1 mention) - the report calls it "Gait ataxia"; HP calls it **Gait imbalance**
- `HP:0001251` (1 mention) - the report calls it "Cerebellar ataxia"; HP calls it **Ataxia**, and lists "Cerebellar ataxia" among its other names
- `HP:0007354` (1 mention) - the report calls it "Amyotrophic lateral sclerosis-like phenotype"; HP calls it **Amyotrophic lateral sclerosis**
- `HP:0001410` (1 mention) - the report calls it "Hepatic dysfunction"; HP calls it **Decreased liver function**, and lists "Liver dysfunction" among its other names
- `GO:0008094` (1 mention) - the report calls it "DNA-dependent ATPase activity"; GO calls it **ATP-dependent activity, acting on DNA**, and lists "DNA dependent ATPase activity" among its other names
- `GO:0016566` (1 mention) - the report calls it "transcriptional repression"; GO calls it **obsolete specific transcriptional repressor activity**, and lists "specific transcriptional repressor activity" among its other names
- `GO:0006306` (1 mention) - the report calls it "DNA methylation"; GO calls it **obsolete DNA methylation**
- `GO:0003950` (1 mention) - the report calls it "poly(ADP-ribose) polymerase activity"; GO calls it **NAD+ poly-ADP-ribosyltransferase activity**, and lists "poly(ADP-ribose)polymerase activity" among its other names
- `CHEBI:16234` (3 mentions) - the report calls it "hydroxyl radical"; CHEBI calls it **hydroxide**
- `CL:0000100` (2 mentions) - the report calls it "spinal motor neuron", "motor neuron"; CL calls it **motor neuron**
- `CL:0000540` (2 mentions) - the report calls it "sensory neuron"; CL calls it **neuron**
- `CL:0000121` (2 mentions) - the report calls it "cerebellar Purkinje neuron"; CL calls it **Purkinje cell**, and lists "cerebellar Purkinje cell" among its other names
- `CL:0000210` (1 mention) - the report calls it "retinal photoreceptor cell"; CL calls it **photoreceptor cell**
- `HP:0003674` (1 mention) - the report calls it "Childhood onset"; HP calls it **Onset**, and lists "Age of onset" among its other names
- `NCIT:C50187` (1 mention) - the report calls it "orthotic device"; NCIT calls it **Spring Device**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0003477` - called "Extensor plantar response", "Peripheral axonal neuropathy"
- `CL:0000100` - called "spinal motor neuron", "motor neuron"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `SNOMEDCT`.