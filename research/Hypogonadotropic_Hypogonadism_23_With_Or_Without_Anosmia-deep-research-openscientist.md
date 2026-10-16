---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-16T20:14:54.412775'
end_time: '2026-10-16T20:28:11.358233'
duration_seconds: 796.95
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hypogonadotropic Hypogonadism 23 With or Without Anosmia
  mondo_id: MONDO:0009223
  category: Mendelian
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 11
  off_topic: 1
  off_topic_references:
  - PMID:40788678
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 49
  verified: 47
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 6
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0007686
    reported_labels:
    - Absent/hypoplastic olfactory bulbs
    ontology_label: Abnormal pupillary function
  - term_id: HP:0004122
    reported_labels:
    - abnormal nasal morphology
    ontology_label: Midline defect of the nose
  - term_id: HP:0001522
    reported_labels:
    - absent
    ontology_label: Death in infancy
  - term_id: GO:0042755
    reported_labels:
    - not applicable
    ontology_label: eating behavior
  - term_id: NCIT:C1947
    reported_labels:
    - hCG
    - Fertility induction:** **hCG
    ontology_label: Organic Oxoacids
  - term_id: NCIT:C15681
    reported_labels:
    - Genetic Counseling
    ontology_label: Cytotoxic Chemotherapy
  - term_id: NCIT:C15417
    reported_labels:
    - Prenatal Diagnosis
    ontology_label: Randomized Clinical Trial
  labels_variant: 1
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hypogonadotropic_Hypogonadism_23_With_Or_Without_Anosmia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hypogonadotropic_Hypogonadism_23_With_Or_Without_Anosmia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypogonadotropic Hypogonadism 23 With or Without Anosmia
- **MONDO ID:** MONDO:0009223 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypogonadotropic Hypogonadism 23 With or Without Anosmia** covering all of the
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

# Hypogonadotropic Hypogonadism 23 With or Without Anosmia (HH23) — Comprehensive Disease Report

**Disease:** Hypogonadotropic Hypogonadism 23 With or Without Anosmia (HH23)
**Causal gene:** *SMCHD1* (Structural Maintenance of Chromosomes flexible Hinge Domain containing 1)
**MONDO:** MONDO:0009223 · **Category:** Mendelian, autosomal dominant
**Evidence base:** Human clinical case reports/series, in vitro biochemistry, mouse/Xenopus models, and human iPSC systems. No patient-level dataset was provided; this report is synthesized from aggregated disease-level resources and primary literature.

---

## Summary (Answer to the Research Question)

HH23 is a rare Mendelian form of congenital hypogonadotropic hypogonadism (GnRH deficiency), with or without anosmia, caused by heterozygous variants in the epigenetic regulator **SMCHD1**. It lies at the hypogonadism-predominant end of the **SMCHD1 allelic spectrum** whose severe extreme is **Bosma arhinia microphthalmia syndrome (BAMS; OMIM 603457)** — characterized by arhinia (absent nose), anosmia with absent olfactory bulbs, microphthalmia/coloboma, hypogonadotropic hypogonadism and cryptorchidism, with normal cognition (PMID 28067911, 26842768, 38808953). Disease-causing variants cluster in the **N-terminal extended GHKL-type ATPase domain** and behave as gain/altered-function alleles, in contrast to the loss-of-function *SMCHD1* alleles that cause facioscapulohumeral muscular dystrophy type 2 (FSHD2) (PMID 28067911, 28222895). The hypogonadism component is managed as for congenital hypogonadotropic hypogonadism generally — sex-steroid replacement and gonadotropin/pulsatile-GnRH therapy for fertility (PMID 26194704, 27467188).

---

## 1. Disease Information

**Overview.** HH23 is a congenital GnRH-deficiency disorder (central/secondary hypogonadism) presenting with absent or incomplete puberty and infertility, which may be accompanied by impaired olfaction (anosmia/hyposmia) — the Kallmann-syndrome phenotype — and, at its most severe, by the craniofacial malformation complex of BAMS. It is one of the numbered loci (PS147950 phenotypic series) of congenital hypogonadotropic hypogonadism (CHH), attributed to *SMCHD1*.

**Key identifiers.**
- **MONDO:** MONDO:0009223
- **Gene:** *SMCHD1*, HGNC:29090, NCBI Gene 23347, UniProt A6NHR9, chromosome 18p11.32
- **Related OMIM phenotype:** Bosma arhinia microphthalmia syndrome, #603457 (allelic/overlapping)
- **Orphanet (BAMS/arhinia):** ORPHA:1134 (arhinia); **MeSH:** Kallmann Syndrome (D017436); Hypogonadism (D007006)
- **ICD-11:** 5A61.0 (hypogonadotropic hypogonadism); **ICD-10:** E23.0 (hypopituitarism/Kallmann)

**Synonyms / alternative names.** HH23; HH23 with or without anosmia; *SMCHD1*-related hypogonadotropic hypogonadism; isolated GnRH deficiency (*SMCHD1*); within the broader entity Bosma arhinia microphthalmia syndrome (BAMS, Bosma syndrome). Kallmann syndrome denotes the anosmic subtype.

**Data derivation.** Disease-level, derived from aggregated literature (OMIM, Orphanet, PubMed case reports and reviews), not from individual EHR data.

---

## 2. Etiology

**Causal factor — genetic.** Heterozygous **germline** missense variants in *SMCHD1*, predominantly **de novo** (PMID 28067911). The condition is not infectious or primarily environmental.

**Genetic risk factors.**
- Causal variants map to the N-terminal **extended ATPase (GHKL) domain** (exons ~3–11). Reported examples: p.Glu473Val (c.1418A>T; with hypogonadotropic hypogonadism), p.His348Arg (c.1043A>G, de novo), p.Asp398Asn (isolated HH/CPHD spectrum) (PMID 38808953, 33784779, 32620854).
- **Modifier:** for the FSHD2 phenotype, the 4q35 D4Z4 repeat length and permissive 4qA haplotype act as strong modifiers; arhinia patients can co-carry an FSHD2-permissive background and show DUX4 derepression (PMID 35121673). This epigenetic/genetic context likely contributes to the striking phenotypic divergence.

**Environmental risk factors.** None established. Age, sex, and specific exposures are not known contributors; disease is congenital and genetically determined.

**Protective factors.** No genetic or environmental protective factors are documented. (gnomAD: constrained gene; pathogenic ATPase-domain missense variants are absent/ultra-rare in controls.)

**Gene–environment interactions.** None demonstrated. The relevant "interaction" is intrinsic gene–epigenome: the pathogenic effect depends on *SMCHD1*'s chromatin context and, for the muscle phenotype, the D4Z4 locus.

---

## 3. Phenotypes (with HPO terms, frequency, onset, severity)

| Phenotype | HPO term | Type | Onset | Frequency/notes |
|---|---|---|---|---|
| Hypogonadotropic hypogonadism | HP:0000044 | Lab/clinical (endocrine) | Congenital; recognized at puberty (or neonatally as micropenis/cryptorchidism) | Defining; present across the spectrum |
| Absent/delayed puberty | HP:0000823 / HP:0000826 | Clinical sign | Adolescence | Common in untreated patients |
| Anosmia/hyposmia | HP:0000458 | Symptom | Congenital | In the "with anosmia" (Kallmann) subset; variable |
| Absent/hypoplastic olfactory bulbs | HP:0007686 | Imaging sign | Congenital | Correlates with anosmia on MRI |
| Arhinia / absent nose | HP:0004122 (abnormal nasal morphology); arhinia | Physical malformation | Congenital | Severe (BAMS) end |
| Choanal atresia | HP:0000453 | Physical malformation | Congenital | BAMS |
| Microphthalmia | HP:0000568 | Physical malformation | Congenital | BAMS |
| Coloboma | HP:0000589 | Physical malformation | Congenital | BAMS |
| High-arched palate / cleft palate | HP:0000218 / HP:0000175 | Physical malformation | Congenital | BAMS |
| Cryptorchidism | HP:0000028 | Physical sign | Congenital | Males |
| Micropenis | HP:0000054 | Physical sign | Congenital/neonatal | Males |
| Normal intelligence | HP:0001522 (absent) — cognition normal | — | — | Characteristic; distinguishes from midline brain malformations |

- **Severity:** variable — from isolated hypogonadotropic hypogonadism to full BAMS.
- **Progression:** congenital and **stable/non-progressive** structurally; the endocrine deficiency is lifelong unless the ~10–20% reversal occurs (PMID 26194704).
- **Quality-of-life impact:** infertility, delayed/absent sexual development and associated psychosocial burden; anosmia impairs flavor perception and hazard detection; arhinia severely affects breathing/feeding, facial appearance, and lacrimal drainage (PMID 40788678). Cognition and life expectancy are typically preserved in mild forms (PMID 26842768).

Evidence: PMID 26842768, 38808953, 33784779, 32620854.

---

## 4. Genetic / Molecular Information

- **Causal gene:** *SMCHD1* (HGNC:29090; OMIM gene 614982), 18p11.32; encodes a ~2,005-aa non-canonical SMC-family protein with an **N-terminal GHKL-type ATPase** (plus ubiquitin-like domain required for N-terminal dimerization/chromatin localization) and a **C-terminal SMC hinge** that homodimerizes and binds nucleic acid (PMID 34109974, 32546545, 32779700).
- **Variant type/class:** predominantly **missense**, clustered in the extended ATPase domain (PMID 28067911).
- **Classification:** pathogenic / likely pathogenic by ACMG/AMP (de novo occurrence PS2; domain clustering/absence from controls); some rare variants remain VUS (e.g., p.Asp398Asn classified likely pathogenic, PMID 32620854).
- **Allele frequency:** pathogenic variants are absent or ultra-rare in gnomAD; *SMCHD1* is intolerant to such missense in the ATPase region.
- **Origin:** germline; de novo in most BAMS/HH cases (PMID 28067911). No somatic/cancer role in this disease.
- **Functional consequence:** BAMS/HH ATPase-domain variants behave as **gain/altered-function** (Xenopus assays), the opposite directionality to **loss-of-function** FSHD2 alleles (PMID 28067911, 28222895).
- **Modifier genes:** 4q D4Z4 repeat/haplotype (muscle phenotype); other CHH/Kallmann genes may act oligogenically.
- **Epigenetic information:** *SMCHD1* is itself an epigenetic effector; patients carry a reproducible DNA-methylation "episignature," and FSHD2-overlap cases show D4Z4 hypomethylation with DUX4 derepression (PMID 37334829, 35121673).
- **Chromosomal abnormalities:** none characteristic; disease arises from point mutations, not aneuploidy/translocation.

---

## 5. Environmental Information

- **Environmental factors / toxins / radiation:** none implicated.
- **Lifestyle factors:** none causal (relevant only to general reproductive/bone health in management).
- **Infectious agents:** none. This is a non-infectious congenital genetic disorder.

(Section not applicable beyond stating absence of environmental/infectious etiology.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **de novo heterozygous missense variant** in the *SMCHD1* N-terminal extended ATPase (GHKL) domain **alters** SMCHD1 enzymatic/chromatin activity (gain/altered-function; demonstrated biochemically and in Xenopus) (PMID 28067911).
2. Altered SMCHD1 **perturbs** its normal role in long-range chromatin compaction and heterochromatin maintenance — recruitment to targets via the Xist–HnrnpK–PRC1/H2AK119ub pathway and deposition/maintenance of H3K9me3 and H3K27me3 blocks and CpG-island methylation (PMID 30428357, 35831949, 30126901, 18425126). *(Mechanism at targets well demonstrated; the precise mis-silenced genes driving human nasal/HH phenotypes are inferred.)*
3. Dysregulated silencing **leads to** mis-expression of developmental master regulators (e.g., Hox clusters, clustered protocadherins, imprinted/neural-crest fate genes) in euchromatin and repressed chromatin of **neural crest stem cells** and craniofacial/olfactory placode progenitors (PMID 37334829). *(Inferred effector loci.)*
4. This **results in** failed morphogenesis of the **nasal placode/olfactory system** → arhinia and absent/hypoplastic olfactory bulbs (branch A) and disrupted **craniofacial/ocular** development → microphthalmia, coloboma, palatal/choanal defects (branch B) (PMID 28067911, 26842768).
5. Branch C — **reproductive axis:** absent/defective olfactory bulb scaffolding and/or independent hypothalamic effects **impair embryonic migration of GnRH-synthesizing neurons** from the olfactory placode to the hypothalamus (the canonical Kallmann mechanism), and/or GnRH-neuron function, **leading to** deficient hypothalamic GnRH secretion (PMID 26194704). *(For SMCHD1 specifically, the GnRH-neuron step is inferred by analogy to Kallmann biology rather than directly demonstrated.)*
6. GnRH deficiency **causes** low pituitary LH/FSH secretion → **results in** low gonadal sex-steroid output (testosterone/estradiol) and impaired gametogenesis → **manifests as** hypogonadotropic hypogonadism, absent puberty, cryptorchidism/micropenis, and infertility (PMID 26194704, 28833369).
7. Chronic untreated hypogonadism **leads to** downstream osteoporosis and metabolic syndrome (PMID 30352392).

### Supporting detail
- **Molecular pathways:** epigenetic silencing (Polycomb PRC1/PRC2, H2AK119ub → H3K27me3; H3K9me3 heterochromatin), 3D genome organization (TAD/compartment regulation on Xi). Downstream, the reproductive phenotype funnels into the **hypothalamic–pituitary–gonadal (GnRH→LH/FSH→sex steroid) axis** (PMID 30604745, 26194704).
- **Cellular processes:** chromatin compaction, dosage compensation, cell-fate determination/differentiation of neural crest; **GnRH neuron migration** (olfactory placode → hypothalamus).
- **Protein dysfunction:** altered ATPase/dimerization behavior of mutant SMCHD1; UBL domain needed for N-terminal dimerization and chromatin localization (PMID 34109974).
- **Immune/metabolic:** no primary immune involvement; metabolic syndrome is a late consequence of hypogonadism.
- **GO terms:** GO:0031507 heterochromatin formation; GO:0040029 epigenetic regulation of gene expression; GO:0009048 dosage compensation by inactivation of X chromosome; GO:0006346 methylation-dependent chromatin silencing; GO:0001945/GO:0097475 neuron migration (GnRH neuron migration); GO:0042755 (not applicable). **CL terms:** CL:0000333 neural crest cell; CL:0011111 GnRH neuron; CL:0000207 olfactory receptor neuron; CL:0000216 gonadotroph (Sertoli/Leydig downstream).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** hypothalamus (UBERON:0001898) and pituitary gland (UBERON:0000007) — reproductive axis; olfactory system (olfactory bulb UBERON:0002264, olfactory epithelium UBERON:0001997); external/internal nose (UBERON:0000004) in BAMS; eye (UBERON:0000970); gonads — testis (UBERON:0000473)/ovary (UBERON:0000992).
- **Secondary involvement:** bone (osteoporosis), cardiovascular/metabolic (metabolic syndrome), lacrimal system (in arhinia); airway/respiratory compromise neonatally (arhinia/choanal atresia).
- **Body systems:** endocrine (reproductive), nervous (olfactory), craniofacial/skeletal, ocular, respiratory (secondary).
- **Tissue/cell level:** neural crest–derived craniofacial mesenchyme; olfactory placode epithelium; GnRH neurons; gonadal germ/somatic cells (CL:0000333, CL:0011111, CL:0000207).
- **Subcellular (GO Cellular Component):** nucleus (GO:0005634), chromatin/heterochromatin (GO:0000785/GO:0000792), inactive X chromosome (Barr body, GO:0001739).
- **Lateralization:** malformations are usually **bilateral** (arhinia, olfactory bulb aplasia, microphthalmia) but **hemiarhinia (unilateral)** occurs as a milder form (PMID 38808953, 40788678).

---

## 8. Temporal Development

- **Onset:** **congenital.** Structural anomalies present at birth (arhinia, microphthalmia, choanal atresia); hypogonadism is congenital but often first recognized at expected puberty (or neonatally via micropenis/cryptorchidism/absent mini-puberty).
- **Onset pattern:** chronic/insidious for the endocrine component; the nasal/airway malformation is an acute neonatal emergency in severe cases.
- **Progression:** **non-progressive/stable** structurally; endocrine deficiency is **lifelong/chronic** barring the ~10–20% spontaneous reversal seen in CHH generally (PMID 26194704).
- **Critical periods:** embryonic craniofacial/olfactory morphogenesis and GnRH-neuron migration (first trimester) for the malformations; **mini-puberty (0–6 months)** and expected pubertal window for diagnosis and hormonal intervention; neonatal period for airway management.
- **Remission:** treatment-induced puberty/fertility; a minority show spontaneous recovery of reproductive function.

---

## 9. Inheritance and Population

- **Epidemiology:** ultra-rare. BAMS has **<50 reported cases/series**; arhinia overall **<30–40 documented worldwide** (PMID 26842768, 41832654). No reliable prevalence/incidence figures exist; it is far rarer than Kallmann syndrome overall (~1/10,000 males, ~1/50,000 females for CHH/KS; PMID 30352392).
- **Inheritance:** **autosomal dominant**, heterozygous *SMCHD1* variants on 18p11; **predominantly de novo** (PMID 38808953, 28067911).
- **Penetrance/expressivity:** **incomplete penetrance** and **markedly variable expressivity** (isolated HH → hemiarhinia → full BAMS; and distinct FSHD2 for LoF alleles) (PMID 35121673, 28222895).
- **Anticipation:** not a repeat-expansion disorder; no anticipation.
- **Germline mosaicism:** possible (relevant to recurrence counseling); not well quantified.
- **Founder effects / consanguinity / carrier frequency:** none established; de novo origin makes carrier screening non-applicable.
- **Demographics:** reported across diverse ethnicities and geographies with no clustering; both sexes affected (males more readily recognized via genital findings; BAMS diagnostic criteria emphasize HH in males). No defined sex ratio.

---

## 10. Diagnostics

**Clinical/biochemical.**
- Reproductive hormone panel: low/low-normal **LH** and **FSH** with low **testosterone/estradiol**; low **inhibin B** and **AMH**; **GnRH and hCG stimulation** tests to assess axis integrity (PMID 28833369). LOINC-type analytes: LH, FSH, testosterone, estradiol, inhibin B.
- Evaluate other pituitary axes to exclude **combined pituitary hormone deficiency / septo-optic dysplasia** overlap (PMID 32620854).

**Olfactory testing.** Objective and subjective **olfactometry**; results correlate with olfactory-bulb volume on MRI (PMID 25553765).

**Imaging.** Dedicated **MRI of the olfactory system** (bulb/sulcus aplasia or hypoplasia; may show anterior pituitary hypoplasia) (PMID 26571055, 25553765); craniofacial **CT/MRI** for arhinia, choanal atresia, microphthalmia/coloboma; **fetal MRI/ultrasound** can detect arhinia prenatally (PMID 39295111).

**Genetic testing.** **Molecular diagnosis = *SMCHD1* sequencing**, best delivered within a **multigene CHH/Kallmann panel** or **WES/WGS**, given genetic heterogeneity (PMID 41902607, 32620854). Chromosomal microarray/karyotype/FISH are generally **not** diagnostic (point mutations). For patients with a *SMCHD1* variant, consider FSHD2 risk assessment (4q D4Z4 methylation/haplotype).

**Clinical criteria.** Proposed BAMS criteria: **arhinia, hypoplastic maxilla, normal cognition, and hypogonadotropic hypogonadism (in males)** (PMID 26842768).

**Differential diagnosis.** Other Kallmann/CHH genes (ANOS1, FGFR1, FGF8, PROK2/PROKR2, CHD7, SOX10, GNRHR, KISS1/KISS1R, etc.); CHARGE syndrome; septo-optic dysplasia; holoprosencephaly (for arhinia); constitutional delay of puberty (PMID 26194704, 41902607).

**Screening.** No population/newborn screening. Cascade testing has low yield (de novo); prenatal/PGT applies when a familial variant is known.

---

## 11. Outcome / Prognosis

- **Survival/life expectancy:** normal in isolated/mild HH23; **neonatal airway obstruction** from arhinia/choanal atresia is the chief early-life mortality risk in severe BAMS, often requiring intubation/tracheostomy (PMID 33784779).
- **Cognition:** normal intelligence and brain structure (PMID 26842768).
- **Morbidity:** untreated hypogonadism → **infertility, osteoporosis, metabolic syndrome** (PMID 30352392); anosmia (safety/flavor); ocular impairment from microphthalmia; facial disfigurement/airway/lacrimal issues from arhinia.
- **Recovery/treatment response:** fertility inducible in most CHH with gonadotropins/GnRH; normal final testicular volume attained in ~70–74% and sperm in ejaculate in 91–95% with combined gonadotropin therapy; ~10–20% spontaneous reversal (PMID 27467188, 26194704).
- **Prognostic factors:** completeness of GnRH deficiency, severity of arhinia/microphthalmia, timeliness of hormone replacement and neonatal airway/surgical management. No molecular prognostic biomarker beyond genotype/phenotype correlation.

---

## 12. Treatment

**Pharmacotherapy (hypogonadism).**
- **Sex-steroid replacement** to induce/maintain puberty and secondary sex characteristics and protect bone: **testosterone** (males; NCIT:C2270, CHEBI:17347) or **estrogen/progesterone** (females; estradiol CHEBI:16469). Does not restore fertility.
- **Fertility induction:** **hCG** (NCIT:C1947) + **recombinant FSH/hMG** (FSH NCIT:C105867), or **pulsatile GnRH** (gonadorelin; NCIT:C76341, CHEBI:5520). Restores testicular growth and spermatogenesis in the large majority; ovulation induction in females (PMID 27467188, 33894111, 30519672, 40463510, 26194704).
- **Infancy:** gonadotropin therapy during mini-puberty can increase penile length and inhibin B and promote testicular descent (PMID 39673783).

**Surgical/interventional (BAMS features).** Staged **nasal reconstruction** (e.g., costal-cartilage framework with forehead/expander flaps), **Le Fort II** midface procedures, choanal atresia repair, ophthalmologic management, and **dacryocystorhinostomy** for lacrimal obstruction (PMID 41902607, 41832654, 40788678). Neonatal airway stabilization (oral airway/tracheostomy).

**Advanced/experimental.** No gene-, cell-, RNA-based, or SMCHD1-targeted therapy exists for HH23. No disease-specific clinical trials; management follows CHH guidelines (PMID 26194704).

**Pharmacogenomics / personalized medicine.** None specific; treatment is genotype-agnostic for the endocrine axis (same across CHH genes).

**Outcomes/adverse events:** gonadotropin/testosterone therapies are generally well tolerated; monitor erythrocytosis, acne, gynecomastia, injection burden; surgical risks per procedure.

**Strategy.** Multidisciplinary: endocrinology (hormone replacement/fertility), ENT/craniofacial & plastic surgery, ophthalmology, genetics/counseling, psychology.

---

## 13. Prevention

- **Primary prevention:** not feasible (predominantly de novo genetic disorder).
- **Secondary prevention / early detection:** prenatal fetal MRI/ultrasound can detect arhinia (PMID 39295111); early recognition of micropenis/cryptorchidism/absent mini-puberty enables timely endocrine diagnosis.
- **Tertiary prevention:** timely sex-steroid and gonadotropin therapy to prevent osteoporosis, metabolic syndrome, and infertility (PMID 30352392, 26194704); **bone-density monitoring**; anticipatory **neonatal airway planning** for arhinia (PMID 33784779).
- **Genetic counseling:** explain de novo origin (low but non-zero recurrence from possible gonadal mosaicism), ~50% transmission from an affected reproducing proband (AD), and variable expressivity/incomplete penetrance; offer **prenatal/preimplantation genetic testing** when a pathogenic *SMCHD1* variant is identified. NCIT:C15681 (Genetic Counseling), NCIT:C15417 (Prenatal Diagnosis).
- **Immunization / public-health / environmental measures:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *Homo sapiens* (NCBI Taxon 9606), *SMCHD1* (Gene 23347); *Mus musculus* (10090), *Smchd1* (Gene 74355); *Xenopus laevis* (8355). *Smchd1* is evolutionarily conserved; the related plant GHKL ATPase (DMS11) participates in RNA-directed DNA methylation, underscoring deep conservation of GHKL-ATPase epigenetic function (PMID 22560611).
- **Natural disease / veterinary relevance:** no naturally occurring *SMCHD1*-arhinia/HH disorder is documented in companion animals or wildlife (no OMIA entry reported here). Not zoonotic; no cross-species transmission.
- **Comparative biology:** mouse *Smchd1* loss affects X-inactivation and autosomal (Hox/imprinted) silencing, conserving the human molecular role, but does not reproduce arhinia or hypogonadism.

---

## 15. Model Organisms

- **Mouse (*Smchd1*):** the *MommeD1* ENU allele / *Smchd1*-null causes **female-specific mid-gestation lethality** with failed X-inactivation maintenance and X-linked gene derepression (PMID 18425126); *Smchd1*-deficient epiblast stem cells/MEFs show loss of Xi H3K9me3/H3K27me3 and altered chromosome architecture (PMID 35831949, 30604745, 30126901). Resources: MGI, IMPC/KOMP, IMSR.
- **Xenopus laevis:** human BAMS/HH ATPase-domain variants expressed in embryos behave as **gain/altered-function** alleles affecting development — key evidence for variant directionality (PMID 28067911).
- **Human cellular / iPSC:** iPSC-derived **neural crest stem cells** and FSHD2/BAMS primary cells define SMCHD1 **episignatures** and tissue-specific gene-regulatory effects (PMID 37334829).
- **Phenotype recapitulation / limitations:** models capture the **epigenetic silencing (FSHD2/LoF) biology** well but **do not reproduce arhinia or hypogonadotropic hypogonadism** (the gain/altered-function BAMS/HH phenotype); constitutive null is female-lethal. No validated mouse or zebrafish model of HH23 arhinia/HH is established, so developmental mechanism is studied mainly in Xenopus and human iPSC systems.

---

## Supported vs. Refuted Hypotheses

**Supported.**
1. HH23 is caused by heterozygous *SMCHD1* ATPase-domain variants (PMID 28067911, 38808953, 32620854).
2. *SMCHD1* is a non-canonical SMC epigenetic silencer; BAMS/HH variants are gain/altered-function, opposite to FSHD2 LoF (PMID 28222895, 28067911).
3. The phenotype is congenital, AD, predominantly de novo, with variable expressivity and incomplete penetrance (PMID 28067911, 38808953, 35121673).
4. Hypogonadism is treatable with sex steroids + gonadotropins/GnRH (PMID 26194704, 27467188).

**Refuted / not supported.**
- No evidence for environmental, infectious, or lifestyle causation.
- No founder effect, sex-linked inheritance, anticipation, or somatic/cancer mechanism.
- Arhinia+IHH is **not** exclusively *SMCHD1* — other genes (e.g., GNRHR/KISS1) can produce a similar presentation (PMID 41902607), so genotype must be confirmed.

## Limitations and Future Directions

- Ultra-rarity → no registries, prevalence/incidence estimates, penetrance quantification, or QoL instrument data specific to HH23.
- The **direct molecular link** from mutant SMCHD1 to GnRH-neuron/olfactory failure is **inferred**, not demonstrated; mis-silenced effector loci driving the human nasal/HH phenotype are unknown.
- No faithful animal model of the gain-of-function BAMS/HH phenotype; needed for mechanism and therapeutics.
- Genotype–phenotype rules (why the same domain yields isolated HH vs. full BAMS) remain unresolved; epigenetic/modifier context is a priority research area.

---

*Evidence types: human clinical (case reports/series, cohort/consensus), in vitro biochemistry/structural biology, mouse and Xenopus models, and human iPSC systems, as cited by PMID throughout.*


## Artifacts

- [OpenScientist final report](Hypogonadotropic_Hypogonadism_23_With_Or_Without_Anosmia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hypogonadotropic_Hypogonadism_23_With_Or_Without_Anosmia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 11 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:40788678` (1 mention) - Endoscopic Dacryocystorhinostomy in a Patient With Hemi-Arrhinia.
  - shared terms: congenital

Weighed against this report's own most characteristic terms: `smchd1`, `arhinia`, `hypogonadism`, `bams`, `gene`, `phenotype`, `variant`, `gnrh`, `syndrome`, `olfactory`, `absent`, `hypogonadotropic`, `hh23`, `microphthalmia`, `congenital`, `epigenetic`, `novo`, `chh`, `domain`, `fshd2`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 49 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 14 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0007686` (1 mention) - the report calls it "Absent/hypoplastic olfactory bulbs"; HP calls it **Abnormal pupillary function**
- `HP:0004122` (1 mention) - the report calls it "abnormal nasal morphology"; HP calls it **Midline defect of the nose**
- `HP:0001522` (1 mention) - the report calls it "absent"; HP calls it **Death in infancy**
- `GO:0042755` (1 mention) - the report calls it "not applicable"; GO calls it **eating behavior**
- `NCIT:C1947` (1 mention) - the report calls it "hCG", "Fertility induction:** **hCG"; NCIT calls it **Organic Oxoacids**
- `NCIT:C15681` (1 mention) - the report calls it "Genetic Counseling"; NCIT calls it **Cytotoxic Chemotherapy**
- `NCIT:C15417` (1 mention) - the report calls it "Prenatal Diagnosis"; NCIT calls it **Randomized Clinical Trial**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000458` (1 mention) - the report calls it "Anosmia/hyposmia"; HP calls it **Anosmia**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C1947` - called "hCG", "Fertility induction:** **hCG"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.