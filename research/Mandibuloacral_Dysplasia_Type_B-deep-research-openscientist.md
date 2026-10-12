---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-05T11:32:34.845633'
end_time: '2026-10-05T11:48:43.827365'
duration_seconds: 968.98
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mandibuloacral Dysplasia Type B
  mondo_id: MONDO:0012074
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
citation_count: 24
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 21
  validator_version: 0.3.0
term_validation:
  total_terms: 37
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 24
  labels_matching: 12
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: MONDO:0012074
    reported_labels:
    - MONDO
    ontology_label: mandibuloacral dysplasia with type B lipodystrophy
  - term_id: HP:0004322
    reported_labels:
    - Physical
    ontology_label: Short stature
  - term_id: HP:0000347
    reported_labels:
    - Clinical sign
    ontology_label: Micrognathia
  - term_id: HP:0006660
    reported_labels:
    - Clinical sign
    ontology_label: Aplastic clavicle
  - term_id: HP:0000270
    reported_labels:
    - Clinical sign
    ontology_label: Delayed cranial suture closure
  - term_id: HP:0000218
    reported_labels:
    - Clinical sign
    ontology_label: High palate
  - term_id: HP:0000678
    reported_labels:
    - Clinical sign
    ontology_label: Dental crowding
  - term_id: HP:0009771
    reported_labels:
    - Radiographic
    ontology_label: Osteolytic defects of the phalanges of the hand
  - term_id: HP:0009125
    reported_labels:
    - Physical/metabolic
    ontology_label: Lipodystrophy
  - term_id: HP:0002155
    reported_labels:
    - Laboratory
    ontology_label: Hypertriglyceridemia
  - term_id: HP:0003198
    reported_labels:
    - Clinical sign
    ontology_label: Myopathy
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Mandibuloacral_Dysplasia_Type_B-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Mandibuloacral_Dysplasia_Type_B-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mandibuloacral Dysplasia Type B
- **MONDO ID:** MONDO:0012074 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mandibuloacral Dysplasia Type B** covering all of the
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

# Mandibuloacral Dysplasia Type B (MAD-B): Comprehensive Disease Characteristics Report

**Disease:** Mandibuloacral Dysplasia Type B (MAD-B / MADB)
**MONDO ID:** MONDO:0012074 · **OMIM:** #608612 · **Causal gene:** *ZMPSTE24* (FACE1), OMIM 606480, HGNC:12877, chromosome 1p34.2
**Category:** Mendelian, autosomal recessive progeroid laminopathy

---

## Summary

Mandibuloacral dysplasia type B (MAD-B) is an ultra-rare, autosomal recessive progeroid laminopathy caused by biallelic **hypomorphic** (residual-activity) mutations in **ZMPSTE24 (FACE1)**, the zinc metalloprotease that performs the final endoproteolytic maturation of prelamin A into mature lamin A. When ZMPSTE24 activity is reduced, toxic **farnesylated, carboxymethylated prelamin A** accumulates at the inner nuclear membrane, disrupting nuclear lamina architecture and triggering a cascade of downstream pathology: defective DNA-damage repair, epigenetic/chromatin dysregulation (H4K16 hypoacetylation, aberrant H3K9me3), AKT–mTOR pathway activation, oxidative/mitochondrial stress, and premature cellular senescence. These converge on the characteristic multisystem clinical picture of growth failure, craniofacial and skeletal dysplasia (mandibular and clavicular hypoplasia, delayed cranial suture closure, acro-osteolysis of distal phalanges), **generalized (type B) lipodystrophy** with insulin resistance and metabolic complications, and progeroid skin/hair changes (mottled atrophic skin, sparse brittle hair, hypoplastic nails).

A central organizing principle of this disease is a **gene-dosage/enzyme-activity severity gradient** shared with its allelic disorder restrictive dermopathy (RD): complete ZMPSTE24 loss-of-function (biallelic null) causes neonatally lethal RD, whereas variants that preserve residual prelamin A-processing activity cause the milder, survivable MAD-B. This genotype–phenotype correlation is quantitatively supported across case series and is biologically mirrored in *Zmpste24*-deficient mouse models, which recapitulate the bone, muscle, lipodystrophy, immune, and epigenetic phenotypes and have supported mechanism-targeted therapeutic proof-of-concept (isoprenylcysteine methylation inhibition, RCE1/ICMT targeting, SUV39H1 depletion, RANKL inhibition).

There is **no approved disease-modifying therapy** for MAD-B. Management is multidisciplinary and symptomatic, targeting the disease components: metabolic control of the lipodystrophy/diabetes/hypertriglyceridemia (including leptin replacement with **metreleptin**, the only approved therapy for generalized lipodystrophy), bone/orthopedic care, and dermatologic and dental surveillance. Prenylation-targeted drugs borrowed from the Hutchinson–Gilford progeria (HGPS) paradigm — notably the farnesyltransferase inhibitor **lonafarnib**, which rescues nuclear morphology in MAD-B patient fibroblasts — represent the most mechanistically rational experimental strategy.

> Evidence-source key: **[H]** human clinical · **[M]** model organism · **[V]** in vitro · **[C]** computational/database. Primary citations are given as PMIDs; database-level identifiers are aggregated resource knowledge.

---

## 1. Disease Information

**Overview.** MAD-B is a rare autosomal recessive progeroid disorder of the mandibuloacral dysplasia (MAD) spectrum, defined molecularly by mutations in *ZMPSTE24* and clinically by the combination of mandibular and clavicular hypoplasia, acro-osteolysis, delayed cranial suture closure, generalized lipodystrophy, and progeroid skin features. It belongs to the **laminopathies** — disorders of the nuclear lamina — and specifically to the subgroup caused by defective post-translational processing of prelamin A.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0012074 |
| OMIM (phenotype) | #608612 (Mandibuloacral dysplasia with type B lipodystrophy; MADB) |
| Causal gene | *ZMPSTE24* / *FACE1* (OMIM 606480, HGNC:12877, 1p34.2) |
| Disease class | Autosomal recessive progeroid laminopathy |

**Synonyms / alternative names.** Mandibuloacral dysplasia with type B lipodystrophy; MADB; MAD type B; MAD-B; ZMPSTE24-related mandibuloacral dysplasia; mandibuloacral dysplasia with generalized lipodystrophy.

**Information source.** The knowledge base here derives from **aggregated resources plus individual patient case reports and small case series** — MAD-B is ultra-rare, and the strongest clinical dataset is an aggregate of 20 genetically confirmed patients, anchored by an 8-patient Suriname founder cohort **[H]** ([PMID: 31856865](https://pubmed.ncbi.nlm.nih.gov/31856865/)).

---

## 2. Etiology

**Primary cause — genetic.** MAD-B is caused by **biallelic (homozygous or compound heterozygous) mutations in *ZMPSTE24***, reducing zinc-metalloprotease activity and impairing prelamin A processing. This is a Mendelian, monogenic disease; it is not infectious, and there is no primary environmental cause.

> *"MADB is caused by reduced activity of the enzyme zinc metalloprotease ZMPSTE24 resulting from compound heterozygous or homozygous mutations in ZMPSTE24."* — **[H]** [PMID: 31856865](https://pubmed.ncbi.nlm.nih.gov/31856865/)

> *"Mutation in ZMPSTE24 gene, encoding a major metalloprotease, leads to defective prelamin A processing and causes type B mandibuloacral dysplasia, as well as the lethal neonatal restrictive dermopathy syndrome."* — **[H]** [PMID: 21267004](https://pubmed.ncbi.nlm.nih.gov/21267004/)

**Genetic risk factors.** The causal variants themselves are the risk determinant. Severity depends on the **residual enzyme activity** conferred by the specific genotype (Finding F002). **Consanguinity and founder effects** increase recurrence risk — the Suriname cohort (n=8) is homozygous for a single founder allele, c.1196A>G p.(Tyr399Cys).

**Environmental / iatrogenic modifiers.** Although MAD-B is genetic, the same enzymatic pathway can be inhibited pharmacologically: **HIV protease inhibitors** (notably lopinavir) inhibit ZMPSTE24 and phenocopy prelamin A pathology, causing acquired lipodystrophy (Finding F009). This is an acquired/iatrogenic analogue rather than a cause of Mendelian MAD-B, but it establishes a key gene–environment convergence on ZMPSTE24.

**Protective factors.** No established genetic or environmental protective alleles are documented for MAD-B. Mechanistically, interventions that **reduce prelamin A prenylation/methylation** (e.g., ICMT or RCE1 loss, FTIs) are protective in models — a therapeutic inference, not a naturally occurring protective factor.

---

## 3. Phenotypes

The phenotype is a multisystem progeroid syndrome. Major clinical criteria were defined across all 20 genetically confirmed patients, each present in **85–100%** of affected individuals **[H]** ([PMID: 31856865](https://pubmed.ncbi.nlm.nih.gov/31856865/)).

> *"Major criteria were found to be: short stature, clavicular hypoplasia, delayed closure of cranial sutures, high palate, mandibular hypoplasia, dental crowding, acro-osteolysis of the distal phalanges, hypoplastic nails, brittle and/or sparse hair, mottled pigmen[tation]..."* — [PMID: 31856865](https://pubmed.ncbi.nlm.nih.gov/31856865/)

> *"MADB is characterized by brittle hair, mottled, atrophic skin, generalized lipodystrophy, insulin resistance, metabolic complications and skeletal features like stunted growth, mandibular and clavicular hypoplasia and acro-osteolysis of the distal phalanges."* — [PMID: 31856865](https://pubmed.ncbi.nlm.nih.gov/31856865/)

| Phenotype | Type | Suggested HPO term | Frequency | Onset / course |
|---|---|---|---|---|
| Short stature / growth failure | Physical | HP:0004322 | High (major, 85–100%) | Childhood; progressive |
| Mandibular hypoplasia | Clinical sign | HP:0000347 | High (major) | Childhood |
| Clavicular hypoplasia | Clinical sign | HP:0006660 | High (major) | Childhood |
| Delayed cranial suture closure | Clinical sign | HP:0000270 | High (major) | Childhood |
| High/narrow palate | Clinical sign | HP:0000218 | High (major) | Congenital/childhood |
| Dental crowding | Clinical sign | HP:0000678 | High (major) | Childhood |
| Acro-osteolysis of distal phalanges | Radiographic | HP:0009771 | High (major) | Childhood; progressive |
| Hypoplastic nails | Physical | HP:0001792 | High (major) | Childhood |
| Brittle / sparse hair | Physical | HP:0002213 / HP:0008070 | High (major) | Childhood |
| Mottled pigmentation / atrophic skin | Physical | HP:0001000 / HP:0000963 | High (major) | Childhood; progressive |
| Generalized (type B) lipodystrophy | Physical/metabolic | HP:0009125 | Core feature | Childhood; progressive |
| Insulin resistance / diabetes mellitus | Laboratory | HP:0000855 / HP:0000857 | Common | Childhood–adolescence |
| Hypertriglyceridemia | Laboratory | HP:0002155 | Common | Childhood–adolescence |
| Congenital myopathy (reported) | Clinical sign | HP:0003198 | Variable/rare | Homozygous missense case ([PMID: 21267004](https://pubmed.ncbi.nlm.nih.gov/21267004/)) |

**Severity / progression.** Features are generally **progressive and chronic** (bone resorption, lipodystrophy, skin atrophy worsen over time), but the overall course is slowly progressive and survivable into adulthood (contrast lethal RD — Section 8). **Expressivity is variable**, even within the same genotype.

**Quality-of-life impact.** Short stature, craniofacial/orthopedic abnormalities, and skin/hair changes affect appearance, dentition, and mobility; metabolic complications (diabetes, hypertriglyceridemia) impose chronic disease burden. Disease-specific validated QoL instruments for MAD-B are not available; impact is inferred from the lipodystrophy and progeroid literature.

---

## 4. Genetic / Molecular Information

**Causal gene.** *ZMPSTE24* (also *FACE1*; zinc metallopeptidase STE24), encoding a membrane-bound zinc metalloprotease of the inner nuclear/ER membrane that cleaves farnesylated prelamin A. Gene OMIM 606480; phenotype OMIM #608612.

**Variant spectrum (Finding F007).** MAD-B variants span **missense, frameshift, and splice-site** classes, unified by preservation of some residual enzyme activity:

| Variant (cDNA) | Protein | Type | Note | Source |
|---|---|---|---|---|
| c.1196A>G | p.(Tyr399Cys) | Missense | Suriname homozygous founder allele (n=8) | [PMID: 31856865](https://pubmed.ncbi.nlm.nih.gov/31856865/) |
| c.281T>C | p.(Leu94Pro) | Missense | Reported MAD-B | literature spectrum |
| c.794A>G | p.(Asn265Ser) | Missense | Compound het with frameshift | [PMID: 30919593](https://pubmed.ncbi.nlm.nih.gov/30919593/) |
| c.1085dup | p.(Leu362Phefs*19) | Frameshift | Compound het (Chile case) | [PMID: 30919593](https://pubmed.ncbi.nlm.nih.gov/30919593/) |
| c.1077dupT | p.(Leu362fsX18) | Frameshift | Mosaic UPD chr1; intermediate phenotype | [PMID: 29341437](https://pubmed.ncbi.nlm.nih.gov/29341437/) |
| c.28_29insA | p.(Leu10Tyrfs*37) | N-terminal frameshift | Rescued by downstream alternative start codon | [PMID: 35597529](https://pubmed.ncbi.nlm.nih.gov/35597529/) |
| c.378+1G>A | — | Splice-site | Homozygous (Chinese MAD case report) | [PMID: 38544690](https://pubmed.ncbi.nlm.nih.gov/38544690/) |

A notable molecular phenomenon is **alternative translation initiation rescue**: N-terminal frameshifts predicted to be null instead use a downstream in-frame start codon, yielding a hypomorphic (residual-activity) protein that produces survivable MAD-B rather than lethal RD.

> *"the one base pair insertion creates a novel downstream in-frame start codon, which supposedly serves as an alternative translation initiation site (TIS)"* — **[H/V]** [PMID: 35597529](https://pubmed.ncbi.nlm.nih.gov/35597529/)

> *"mutations preserving residual enzymatic activity of the ZMPSTE24 protein lead to the milder mandibuloacral dysplasia with type B lipodystrophy (MADB) phenotype"* — **[H/V]** [PMID: 37270786](https://pubmed.ncbi.nlm.nih.gov/37270786/)

**Variant classification.** Reported MAD-B alleles are classified **pathogenic/likely pathogenic** (ACMG/AMP), supported by segregation, recessive genotype, functional reduction in prelamin A processing, and phenotype concordance. **Allele frequencies** in population databases (gnomAD) are very low/absent, consistent with recessive disease.

**Functional consequence.** **Loss of function** of ZMPSTE24 protease activity → toxic accumulation of **farnesylated prelamin A** (a gain-of-toxic-function at the substrate level). Severity scales inversely with residual activity (Finding F002).

**Origin.** **Germline**, biallelic. One reported patient had an unusual **mosaic uniparental isodisomy of chromosome 1** unmasking a ZMPSTE24 variant ([PMID: 29341437](https://pubmed.ncbi.nlm.nih.gov/29341437/)).

**Modifier genes / epigenetics.** In models, modifiers of the prelamin A pathway alter severity: *SUV39H1* (H3K9 methyltransferase) depletion improves DNA repair and lifespan; *ICMT* and *RCE1* (prenyl-processing enzymes) modulate prelamin A toxicity. Epigenetic changes downstream of ZMPSTE24 loss include **H4K16 hypoacetylation** and altered H3K9me3 (Section 6).

---

## 5. Environmental Information

MAD-B is a **monogenic genetic disease**; no environmental, lifestyle, or infectious agent causes it. However, the **ZMPSTE24 enzyme is a documented pharmacologic target**: HIV protease inhibitors inhibit ZMPSTE24 and phenocopy prelamin A disease (acquired lipodystrophy, accelerated cellular senescence), establishing an environmental/iatrogenic analogue of the genetic defect (Finding F009).

> *"lopinavir accelerated cellular senescence by inhibiting Zmpste24 and interfering nuclear membrane stability, which leads to decreased binding between nuclear membrane-binding protein Usp7 and Mdm2 and activates Usp7/Mdm2/p53 pathway"* — **[M/H]** [PMID: 40461512](https://pubmed.ncbi.nlm.nih.gov/40461512/)

No infectious agents are implicated.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic hypomorphic *ZMPSTE24* mutation** reduces zinc-metalloprotease activity *(demonstrated)*.
2. This **results in** defective endoproteolytic maturation of prelamin A → lamin A *(demonstrated)*.
3. Which **leads to** accumulation of **farnesylated, carboxymethylated prelamin A** anchored at the inner nuclear membrane *(demonstrated)*.
4. Accumulated prelamin A **disrupts nuclear lamina architecture / nuclear morphology** (misshapen nuclei) *(demonstrated in patient fibroblasts; rescued by FTI)*.
5. Lamina disruption **branches** into several downstream effects:
   - **5a.** **Impaired DNA-damage repair** via **H4K16 hypoacetylation** (reduced Mof association with nuclear matrix) and aberrant **H3K9me3** (SUV39H1-dependent) → genomic instability *(demonstrated in mouse)*.
   - **5b.** **Prelamin A–dependent activation of AKT–mTOR signaling** (prelamin A–AKT interaction) → altered proliferation/senescence balance *(demonstrated)*.
   - **5c.** **Mitochondrial dysfunction and oxidative stress**, prominent in adipose tissue *(demonstrated proteomically)*.
6. These **converge on premature cellular senescence** and tissue-specific stem/progenitor depletion *(demonstrated)*.
7. **Senescence + progenitor depletion** in skeletal stem/progenitor cells, adipocytes, osteocytes, and other lineages **results in** the clinical phenotype: bone dysplasia/acro-osteolysis, generalized lipodystrophy with insulin resistance, progeroid skin/hair, and growth failure *(inferred from model + human concordance)*.

### Detailed mechanism

**Molecular pathways.** The central lesion is in the **prelamin A post-translational processing pathway** (farnesylation → –AAX cleavage → carboxymethylation → ZMPSTE24-mediated 15-residue upstream cleavage to mature lamin A). Downstream signaling nodes include **AKT–mTOR** (activated by prelamin A), the **Usp7/Mdm2/p53** senescence axis (shown pharmacologically with lopinavir), and **NF-κB** (B-lymphopoiesis in marrow).

> *"triggered prelamin A-dependent activation of AKT-mammalian target of rapamycin (mTOR) signaling, which abolished the premature senescence of Zmpste24-deficient fibroblasts."* — **[M/V]** [PMID: 23686339](https://pubmed.ncbi.nlm.nih.gov/23686339/)

**Cellular processes.** Premature **cellular senescence** (GO:0090398), **cell-cycle dysregulation**, **DNA-damage response** (GO:0006974), and **stem/progenitor cell depletion** are core. scRNA-seq of conditional *Zmpste24* deletion shows loss of skeletal stem/progenitor cell populations drives bone loss **[M]** ([PMID: 37407584](https://pubmed.ncbi.nlm.nih.gov/37407584/)).

**Protein dysfunction.** Loss of ZMPSTE24 catalytic function → persistent farnesyl/methyl modification of prelamin A, which anchors it to the nuclear envelope as a toxic species (gain-of-toxic-function at the substrate).

**Epigenetic changes.** **H4K16 hypoacetylation** (reduced Mof HAT at nuclear matrix) and **SUV39H1-dependent H3K9me3** dysregulation link lamina disruption to defective DNA repair.

> *"histone H4 was hypoacetylated at a lysine 16 residue (H4K16), and this defect was attributed to the reduced association of a histone acetyltransferase, Mof, to the nuclear matrix"* — **[M]** [PMID: 21746928](https://pubmed.ncbi.nlm.nih.gov/21746928/)

**Metabolic / mitochondrial.** Adipose-tissue proteomics in *Zmpste24-/-* mice reveal major mitochondrial changes and vimentin processing alterations, tying defective prelamin A processing to lipoatrophy and oxidative damage.

> *"support the relationship between defective prelamin A processing and mitochondrial dysfunction and highlight the relevance of oxidative damage in lipoatrophy and aging"* — **[M]** [PMID: 21828285](https://pubmed.ncbi.nlm.nih.gov/21828285/)

**Immune involvement.** Prelamin A accumulation compromises **NF-κB-regulated B-lymphopoiesis** via the bone-marrow microenvironment in the progeria mouse model **[M]** ([PMID: 24764515](https://pubmed.ncbi.nlm.nih.gov/24764515/)).

**Ontology suggestions.** Biological processes: GO:0006508 (proteolysis), GO:0006974 (DNA damage response), GO:0090398 (cellular senescence), GO:0006629 (lipid metabolic process). Cell types: CL:0000136 (adipocyte), CL:0000062 (osteoblast), CL:0000137 (osteocyte), CL:0000057 (fibroblast), skeletal stem/progenitor cell. Cellular components: GO:0005637 (nuclear inner membrane), GO:0005635 (nuclear envelope), GO:0005739 (mitochondrion). Chemicals: CHEBI:24017 (farnesyl group); farnesyltransferase inhibitor class.

### Mechanistic schematic

```
ZMPSTE24 biallelic hypomorphic mutation
            │ (reduced zinc-metalloprotease activity)
            ▼
Defective prelamin A → lamin A maturation
            │
            ▼
Accumulation of FARNESYLATED PRELAMIN A at inner nuclear membrane
            │
            ▼
Nuclear lamina disruption / abnormal nuclear morphology ──► (rescued by lonafarnib)
     │              │                 │
     ▼              ▼                 ▼
 Impaired       AKT–mTOR          Mitochondrial
 DNA repair     activation        dysfunction &
 (H4K16↓,                         oxidative stress
 H3K9me3 dysreg)                  (adipose)
     │              │                 │
     └──────────────┴─────────────────┘
                    ▼
         PREMATURE CELLULAR SENESCENCE +
         stem/progenitor depletion
                    ▼
 ┌──────────────┬──────────────────┬─────────────────┐
 ▼              ▼                  ▼                 ▼
Bone dysplasia  Generalized       Progeroid         Growth
acro-osteolysis lipodystrophy +   skin/hair         failure
                insulin resistance
```

---

## 7. Anatomical Structures Affected

- **Skeletal system (primary).** Mandible (UBERON:0001684), clavicle (UBERON:0001105), cranial sutures (UBERON:0007842), distal phalanges (acro-osteolysis; UBERON:0004248), skull/palate. Bone loss is driven by skeletal stem/progenitor cell senescence and osteocyte–RANKL signaling.
- **Adipose tissue (primary).** Generalized loss of subcutaneous and visceral adipose tissue (UBERON:0001013); mitochondrial dysfunction in adipocytes.
- **Skin and appendages.** Skin (UBERON:0002097) — mottled, atrophic; hair (brittle/sparse); nails (hypoplastic).
- **Endocrine/metabolic (secondary).** Insulin resistance, diabetes mellitus, hypertriglyceridemia — consequences of lipodystrophy and leptin deficiency.
- **Muscle.** Congenital myopathy reported in a homozygous missense case ([PMID: 21267004](https://pubmed.ncbi.nlm.nih.gov/21267004/)); muscle wasting prominent in *Zmpste24-/-* mice.
- **Hematopoietic/immune (model-level).** Impaired B-lymphopoiesis in the marrow microenvironment (mouse).
- **Subcellular.** Nuclear envelope / inner nuclear membrane (GO:0005637), nuclear lamina, mitochondria (GO:0005739).
- **Lateralization.** Skeletal features are generally **bilateral/symmetric**.

---

## 8. Temporal Development

**Onset.** **Postnatal / childhood** onset; chronic, insidious course (Finding F011). This contrasts sharply with the allelic **restrictive dermopathy (RD)**, the ZMPSTE24-null disorder with congenital taut translucent skin, joint contractures, and **death usually within the first month of life**.

> *"death usually occurring within the first month of life"* (lethal neonatal RD) — **[H]** [PMID: 41877632](https://pubmed.ncbi.nlm.nih.gov/41877632/)

**Progression.** Slowly progressive and chronic/lifelong; skeletal resorption, lipodystrophy, and skin atrophy worsen over time. A **30-year longitudinal clinical survey** of a ZMPSTE24-mutant progeroid patient documents survival into and through adulthood.

> *"we report a 30-year longitudinal clinical survey of a patient"* — **[H]** [PMID: 21267004](https://pubmed.ncbi.nlm.nih.gov/21267004/)

**Severity continuum.** Position on the RD ↔ MAD-B continuum is set by **residual ZMPSTE24 activity / prelamin A burden** (Finding F002). An "intermediate form" genocopying severe progeria has been described ([PMID: 29341437](https://pubmed.ncbi.nlm.nih.gov/29341437/)).

**Critical window.** Mechanism-targeted interventions in models work best when started early (e.g., *Rce1* knockout at postnatal week 4–5 doubled median survival), suggesting an early-childhood window of opportunity.

---

## 9. Inheritance and Population

- **Inheritance.** **Autosomal recessive** (biallelic ZMPSTE24).
- **Penetrance.** Effectively complete for biallelic pathogenic genotypes; **expressivity is variable** across (and within) genotypes.
- **Prevalence/incidence.** Ultra-rare; precise prevalence not established. Only ~20 genetically confirmed patients form the aggregate clinical dataset; reported as isolated cases and small series worldwide.
- **Founder effects / consanguinity.** A **homozygous founder mutation (c.1196A>G, p.Tyr399Cys)** underlies the 8-patient **Suriname** cohort — a clear founder effect. Consanguinity increases recurrence risk; several reported cases arise from consanguineous or isolated-population backgrounds.
- **Geographic distribution.** Reported globally (Suriname, Chile, China, and others); no single endemic region beyond founder clusters.
- **Sex ratio.** Autosomal recessive — expected **1:1 male:female**.
- **Carrier frequency.** Not formally established; expected very low given rarity.

---

## 10. Diagnostics

**Clinical/imaging.** Diagnosis is suspected from the characteristic constellation: short stature, mandibular/clavicular hypoplasia, delayed cranial suture closure, high palate, dental crowding, **radiographic acro-osteolysis of distal phalanges**, hypoplastic nails, sparse brittle hair, mottled atrophic skin, and generalized lipodystrophy. Skeletal survey/radiography demonstrates clavicular hypoplasia and acro-osteolysis. **Metabolic labs** show insulin resistance, hyperglycemia/diabetes, and hypertriglyceridemia.

**Cellular/functional.** Skin fibroblasts show **abnormal nuclear morphology** (misshapen nuclei) from prelamin A accumulation — a supportive in vitro finding reversible with FTI (lonafarnib).

**Genetic testing (confirmatory, gold standard).**
- **Single-gene sequencing of *ZMPSTE24*** confirms the diagnosis.
- **Gene panels** (lipodystrophy / laminopathy / progeroid panels including *LMNA*, *ZMPSTE24*, *POLD1*, *MTX2*) and **whole-exome sequencing (WES)** are effective when phenotypes overlap other MAD/progeroid syndromes.
- **WGS/WES** also detect unusual mechanisms (e.g., mosaic uniparental isodisomy of chromosome 1 unmasking a ZMPSTE24 allele — [PMID: 29341437](https://pubmed.ncbi.nlm.nih.gov/29341437/)).
- Functional confirmation: reduced prelamin A processing / prelamin A accumulation on immunoblot.

**Clinical diagnostic criteria.** Formal **major/minor criteria and management guidelines** were proposed from the 20-patient aggregate ([PMID: 31856865](https://pubmed.ncbi.nlm.nih.gov/31856865/); Finding F003).

**Differential diagnosis (Finding F006).**

| Disorder | Gene | Distinguishing feature |
|---|---|---|
| MAD type A | *LMNA* | Partial (type A) lipodystrophy |
| **MAD type B** | ***ZMPSTE24*** | **Generalized (type B) lipodystrophy** |
| Restrictive dermopathy | *ZMPSTE24* (null) | Neonatal lethal; taut translucent skin, contractures |
| Hutchinson–Gilford progeria | *LMNA* (progerin) | Severe vascular disease; distinct skeletal pattern |
| MDPL | *POLD1* | Deafness, male hypogonadism |
| MDPS | *MTX2* (null) | Arterial calcification, renal glomerulosclerosis, hypertension |
| MDP syndrome | unknown | Sensorineural deafness; no clavicular hypoplasia/acro-osteolysis ([PMID: 20631028](https://pubmed.ncbi.nlm.nih.gov/20631028/)) |
| Hallermann–Streiff syndrome | unknown (not a laminopathy) | Congenital cataracts; no ZMPSTE24/LMNA pathogenic variants ([PMID: 22570643](https://pubmed.ncbi.nlm.nih.gov/22570643/)) |

> *"The molecular defects associated with MAD are mutations in LMNA or ZMPSTE24 (FACE1) gene, causing type A or type B MAD, respectively."* — **[H]** [PMID: 29208544](https://pubmed.ncbi.nlm.nih.gov/29208544/)

> *"We report five homozygous null mutations in MTX2, encoding Metaxin-2 (MTX2), an outer mitochondrial membrane protein, in patients presenting with a severe laminopathy-like mandibuloacral dysplasia"* — **[H]** [PMID: 32917887](https://pubmed.ncbi.nlm.nih.gov/32917887/)

**Screening.** Carrier screening / cascade testing in affected families (especially founder populations); prenatal / preimplantation genetic diagnosis is feasible once familial variants are known.

---

## 11. Outcome / Prognosis

- **Survival.** Unlike lethal neonatal RD, MAD-B is **survivable into adulthood**; a 30-year longitudinal survey documents long-term survival ([PMID: 21267004](https://pubmed.ncbi.nlm.nih.gov/21267004/)). Prognosis is set by residual enzyme activity.
- **Morbidity.** Substantial chronic morbidity from skeletal dysplasia (acro-osteolysis, fractures, deformity), lipodystrophy-driven **metabolic disease** (diabetes, severe hypertriglyceridemia with pancreatitis risk, hepatic steatosis), and progeroid skin/dental problems.
- **Complications.** Metabolic complications of generalized lipodystrophy; orthopedic complications; potential cardiac repolarization abnormalities reported in prelamin A disorders (progeroid models/HGPS) warrant surveillance.
- **Prognostic factors.** Degree of residual ZMPSTE24 activity / prelamin A accumulation (molecular prognostic axis); severity of metabolic complications.
- **Recovery.** No cure; recovery is not expected, but metabolic management substantially modifies morbidity.

---

## 12. Treatment

**No disease-modifying therapy is approved for MAD-B; management is multidisciplinary and symptomatic** (Finding F010). Management guidelines accompany the diagnostic criteria ([PMID: 31856865](https://pubmed.ncbi.nlm.nih.gov/31856865/)).

**Metabolic / lipodystrophy management.**
- **Metreleptin** (recombinant leptin; NCIT: leptin replacement therapy / metreleptin) — the **only approved therapy for generalized lipodystrophy** and mechanistically applicable to MAD-B's leptin-deficient generalized lipodystrophy. In generalized lipodystrophy cohorts it produced significant reductions in HbA1c and triglycerides.

> *"Significant short-term median reductions from baseline were observed for HbA1c (- 1.4%; n = 26), fasting plasma glucose (- 0.5 mmol/L; n = 21); fasting triglycerides (TG; -1.5 mmol/L; n = 26)"* — **[H]** [PMID: 42507316](https://pubmed.ncbi.nlm.nih.gov/42507316/)

- Standard metabolic agents (insulin sensitizers, lipid-lowering agents), diet, and exercise for diabetes/hypertriglyceridemia.

**Mechanism-targeted / experimental (prenylation-directed).**
- **Lonafarnib** (farnesyltransferase inhibitor; NCIT: farnesyltransferase inhibitor) **improves abnormal nuclear morphology in ZMPSTE24-deficient MAD-B patient fibroblasts**, providing direct in vitro rationale.

> *"Several related progeroid disorders are caused by defective post-translational processing of prelamin A, the precursor of the nuclear scaffold protein lamin A..."* — **[V]** [PMID: 38050983](https://pubmed.ncbi.nlm.nih.gov/38050983/)

- The HGPS **triple-therapy** paradigm (lonafarnib + pravastatin + zoledronic acid) improved bone mineral density and weight gain in trial, supporting translation to prelamin A disorders.

> *"Secondary improvements included increased areal (P=0.001) and volumetric (P<0.001-0.006) bone mineral density and 1.5- to 1.8-fold increases in radial bone structure (P<0.001)."* — **[H]** [PMID: 27400896](https://pubmed.ncbi.nlm.nih.gov/27400896/)

- Model-level strategies with translational promise: **ICMT inhibition** (delays senescence), **RCE1 targeting** (doubled median survival in mice), **SUV39H1 depletion** (~60% lifespan extension in mice), **RANKL inhibition** (antiresorptive; improves bone, muscle, lifespan in progeroid mice), and **mTOR modulation**.

**Supportive / surgical.** Orthopedic/dental surveillance and intervention; physical therapy; dermatologic care; growth and nutritional management.

**Pharmacovigilance.** **Avoid HIV protease inhibitors where alternatives exist**, since they inhibit ZMPSTE24 and could worsen prelamin A pathology (Finding F009).

---

## 13. Prevention

- **Primary prevention.** Not possible for a Mendelian disease; prevention centers on **genetic counseling** and reproductive options.
- **Genetic counseling / carrier & cascade testing.** Autosomal recessive recurrence risk of 25% for carrier couples; cascade testing in founder populations (e.g., Suriname). **Prenatal diagnosis and preimplantation genetic testing** available once familial variants are known.
- **Secondary prevention.** Early detection and management of metabolic complications (diabetes, hypertriglyceridemia) and bone disease.
- **Tertiary prevention.** Multidisciplinary surveillance to prevent complications (orthopedic, metabolic, dental, cardiac).
- **Iatrogenic avoidance.** Caution with ZMPSTE24-inhibiting drugs (HIV protease inhibitors).

---

## 14. Other Species / Natural Disease

- **Orthology.** *ZMPSTE24* is evolutionarily conserved (yeast Ste24 ortholog); mouse *Zmpste24* is the functional ortholog used to model the disease. The prelamin A processing pathway is conserved across mammals.
- **Natural disease in other species.** No well-characterized naturally occurring animal analogue of MAD-B is documented; disease knowledge comes from engineered mouse models rather than spontaneous veterinary cases.
- **Comparative biology.** *Zmpste24-/-* mice recapitulate core human features (progeroid phenotype, osteoporosis, lipodystrophy, muscle wasting), supporting strong cross-species mechanism conservation.
- **Zoonotic potential.** Not applicable (non-infectious genetic disease).

---

## 15. Model Organisms

The principal model is the ***Zmpste24*-deficient (knockout) mouse**, which accumulates prelamin A and develops progeroid features closely paralleling human prelamin A disorders (Finding F008).

| Model | Type | Key phenotype / finding | Source |
|---|---|---|---|
| *Zmpste24-/-* mouse | Global knockout | Prelamin A accumulation; osteoporosis/fractures, muscle wasting, lipodystrophy, short lifespan | multiple |
| *Suv39h1*-depleted *Zmpste24-/-* | Compound genetic | Improved DNA repair; **~60% lifespan extension** | [PMID: 23695662](https://pubmed.ncbi.nlm.nih.gov/23695662/) |
| *Rce1*-knockout *Zmpste24-/-* | Compound genetic | Delayed senescence; **doubled median survival** | [PMID: 32910507](https://pubmed.ncbi.nlm.nih.gov/32910507/) |
| RANKL-targeted progeroid mice | Therapeutic | Prevented bone loss, improved muscle function, extended lifespan | [PMID: 42572248](https://pubmed.ncbi.nlm.nih.gov/42572248/) |
| Prx1-Cre; *Zmpste24* conditional | Conditional KO | SSPC depletion drives bone loss (scRNA-seq) | [PMID: 37407584](https://pubmed.ncbi.nlm.nih.gov/37407584/) |
| *Zmpste24-/-* B-lymphopoiesis | Global KO | Prelamin A impairs NF-κB-dependent B-lymphopoiesis via marrow niche | [PMID: 24764515](https://pubmed.ncbi.nlm.nih.gov/24764515/) |
| MAD-B patient fibroblasts | In vitro | Abnormal nuclear morphology; rescued by lonafarnib | [PMID: 38050983](https://pubmed.ncbi.nlm.nih.gov/38050983/) |

> *"loss of Suv39h1 in Zmpste24(-/-) mice delays body weight loss, increases bone mineral density and extends lifespan by ∼60%"* — **[M]** [PMID: 23695662](https://pubmed.ncbi.nlm.nih.gov/23695662/)

> *"Lack of Zmpste24, a metalloproteinase responsible for prelamin A processing, leads to progeroid features resembling HGPS."* — **[M]** [PMID: 24764515](https://pubmed.ncbi.nlm.nih.gov/24764515/)

> *"an antiresorptive strategy, based on RANKL targeting, ameliorated the bone loss phenotype of progeroid mice"* — **[M]** [PMID: 42572248](https://pubmed.ncbi.nlm.nih.gov/42572248/)

**Recapitulation / limitations.** The mouse recapitulates bone, muscle, lipodystrophy, immune, and epigenetic phenotypes and supports therapeutic proof-of-concept. Limitations include species differences in lifespan and that complete-null mouse models represent the more severe end of the ZMPSTE24-deficiency spectrum (closer to RD) rather than hypomorphic MAD-B; patient fibroblasts better capture the residual-activity MAD-B state.

---

## Key Findings (with evidence)

1. **MAD-B is an autosomal recessive laminopathy caused by biallelic *ZMPSTE24* mutations reducing prelamin A processing** (F001). Case series and reviews consistently attribute MAD-B to compound heterozygous/homozygous ZMPSTE24 mutations reducing zinc-metalloprotease activity and causing accumulation of unprocessed farnesylated prelamin A; the Suriname founder cohort (n=8) all carried homozygous c.1196A>G p.(Tyr399Cys). [PMID: 31856865, 21267004]

2. **Residual ZMPSTE24 activity sets an allelic severity gradient from lethal RD to MAD-B** (F002). Complete LoF (biallelic null) → neonatally lethal restrictive dermopathy; residual-activity variants → survivable MAD-B; severity correlates with residual activity and prelamin A burden. [PMID: 41877632, 21267004]

3. **Clinical diagnostic criteria defined from a 20-patient aggregate** (F003). Major criteria present in 85–100%: short stature, clavicular hypoplasia, delayed suture closure, high palate, mandibular hypoplasia, dental crowding, acro-osteolysis, hypoplastic nails, brittle/sparse hair, mottled pigmentation, plus generalized lipodystrophy and metabolic complications. [PMID: 31856865]

4. **Prelamin A accumulation drives downstream AKT–mTOR activation, senescence, DNA-repair defects, and oxidative/mitochondrial stress** (F004). [PMID: 23686339, 21746928, 21828285]

5. **Lonafarnib (FTI) rescues nuclear morphology in MAD-B fibroblasts**, supporting prenylation-targeted therapy; HGPS triple-therapy trial improved bone density and weight (F005). [PMID: 38050983, 27400896]

6. **MAD-B sits within a gene-defined classification of mandibuloacral dysplasias/progeroid differentials** (F006). [PMID: 29208544, 32917887]

7. **ZMPSTE24 variant spectrum spans missense, frameshift, and splice variants, with N-terminal frameshifts rescued by alternative translation initiation** (F007). [PMID: 37270786, 35597529, 30919593]

8. **The *Zmpste24-/-* mouse is the principal model**, recapitulating bone, muscle, lipodystrophy, immune, and epigenetic defects and supporting therapeutic targets (F008). [PMID: 23695662, 24764515, 42572248, 37407584]

9. **Pharmacologic ZMPSTE24 inhibition (HIV protease inhibitors) phenocopies prelamin A disease** (F009). [PMID: 40461512]

10. **Management is multidisciplinary/symptomatic; metreleptin addresses the leptin-deficient generalized lipodystrophy and metabolic complications** (F010). [PMID: 42507316, 31856865]

11. **MAD-B has postnatal/childhood onset with a chronic, slowly progressive course and survival into adulthood**, unlike lethal neonatal RD (F011). [PMID: 41877632, 21267004]

---

## Evidence Base (selected literature)

| PMID | Role | Contribution |
|---|---|---|
| [31856865](https://pubmed.ncbi.nlm.nih.gov/31856865/) | Anchor clinical | Suriname cohort, founder mutation, diagnostic criteria & management |
| [21267004](https://pubmed.ncbi.nlm.nih.gov/21267004/) | Clinical/mechanism | MAD-B with congenital myopathy; genotype–severity correlation; 30-yr survey |
| [41877632](https://pubmed.ncbi.nlm.nih.gov/41877632/) | Allelic contrast | RD vs MAD-B activity gradient; lethal neonatal course of RD |
| [37270786](https://pubmed.ncbi.nlm.nih.gov/37270786/) / [35597529](https://pubmed.ncbi.nlm.nih.gov/35597529/) | Variant biology | Alternative translation initiation rescue converting null→hypomorph |
| [30919593](https://pubmed.ncbi.nlm.nih.gov/30919593/) | Variant | Compound het variants (Chile) |
| [29341437](https://pubmed.ncbi.nlm.nih.gov/29341437/) | Variant/mechanism | Mosaic UPD chr1; phenotypic heterogeneity; intermediate form |
| [23686339](https://pubmed.ncbi.nlm.nih.gov/23686339/) | Mechanism | AKT–mTOR activation by prelamin A; ICMT targeting |
| [21746928](https://pubmed.ncbi.nlm.nih.gov/21746928/) | Mechanism | H4K16 hypoacetylation and DNA-repair defect |
| [21828285](https://pubmed.ncbi.nlm.nih.gov/21828285/) | Mechanism | Adipose mitochondrial dysfunction/oxidative stress |
| [38050983](https://pubmed.ncbi.nlm.nih.gov/38050983/) | Therapy | Lonafarnib rescues nuclear morphology in MAD-B fibroblasts |
| [27400896](https://pubmed.ncbi.nlm.nih.gov/27400896/) | Therapy | HGPS triple-therapy trial outcomes |
| [23695662](https://pubmed.ncbi.nlm.nih.gov/23695662/) / [32910507](https://pubmed.ncbi.nlm.nih.gov/32910507/) / [42572248](https://pubmed.ncbi.nlm.nih.gov/42572248/) / [24764515](https://pubmed.ncbi.nlm.nih.gov/24764515/) / [37407584](https://pubmed.ncbi.nlm.nih.gov/37407584/) | Models | Zmpste24-/- mouse mechanisms & therapeutic modifiers |
| [40461512](https://pubmed.ncbi.nlm.nih.gov/40461512/) | Environmental | HIV protease inhibitor ZMPSTE24 inhibition phenocopy |
| [42507316](https://pubmed.ncbi.nlm.nih.gov/42507316/) | Therapy | Metreleptin metabolic benefit in generalized lipodystrophy |
| [29208544](https://pubmed.ncbi.nlm.nih.gov/29208544/) / [32917887](https://pubmed.ncbi.nlm.nih.gov/32917887/) | Classification | MAD A/B gene definitions; MTX2/MDPS differential |

**Evidence source types.** Human clinical (case series/reports, diagnostic-criteria aggregate), in vitro (patient fibroblasts, FTI rescue), and model organism (mouse genetic/therapeutic studies) all contribute. Mechanistic depth is strongest from mouse models and shared prelamin A/HGPS biology; MAD-B-specific clinical data are limited by rarity.

---

## Limitations and Knowledge Gaps

- **Small clinical denominator.** The strongest clinical dataset is ~20 genetically confirmed patients; frequencies, QoL, and natural-history metrics carry wide uncertainty. No formal prevalence/incidence exists.
- **Mechanism extrapolation.** Much mechanistic detail (AKT–mTOR, H4K16, mitochondrial, immune) derives from *Zmpste24-/-* **null** mice and HGPS, which model the severe end; the **hypomorphic residual-activity state specific to MAD-B** is less directly studied in vivo.
- **No MAD-B-specific therapeutic trials.** Metreleptin and FTI evidence is extrapolated from generalized lipodystrophy and HGPS cohorts, not MAD-B trials.
- **Genotype–phenotype quantitation.** The activity gradient is well-supported qualitatively but lacks systematic quantitative mapping of residual activity to specific phenotype severity across the full variant spectrum.
- **Cardiac risk** in MAD-B specifically (vs HGPS/model repolarization data) is under-characterized.
- **Validated QoL instruments** for MAD-B are absent.

---

## Proposed Follow-up Experiments / Actions

1. **Patient-derived iPSC and organoid models** (bone, adipose) carrying defined MAD-B hypomorphic alleles (e.g., p.Tyr399Cys) to study the residual-activity state and test prenylation-targeted drugs in a disease-specific context.
2. **Quantitative residual-activity assays** across the reported ZMPSTE24 variant spectrum, correlated to clinical severity scores, to formalize genotype–phenotype prediction.
3. **Prospective registry / natural-history study** (leveraging founder populations such as Suriname) to establish prevalence, progression rates, metabolic outcomes, cardiac surveillance needs, and validated QoL metrics.
4. **Pilot trials of metreleptin** specifically in MAD-B generalized lipodystrophy, with metabolic endpoints (HbA1c, triglycerides, hepatic fat).
5. **Mechanism-targeted combination testing** (FTI ± statin ± bisphosphonate; RANKL inhibition; mTOR/senolytic approaches) in MAD-B models, prioritizing early-window intervention informed by mouse survival data.
6. **Cardiac phenotyping** (ECG/repolarization, imaging) in MAD-B patients given prelamin A cardiac electrical defects seen in progeroid models.
7. **Pharmacovigilance guidance** formalizing avoidance of ZMPSTE24-inhibiting drugs (HIV protease inhibitors) in patients with prelamin A disorders.

---

*Report compiled from 11 confirmed findings and 47 reviewed papers across 5 investigation iterations. Evidence spans human clinical case series, in vitro patient-fibroblast studies, and mouse model work; claims are cited to primary literature by PMID.*


## Artifacts

- [OpenScientist final report](Mandibuloacral_Dysplasia_Type_B-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Mandibuloacral_Dysplasia_Type_B-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 24 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012074` (2 mentions) - the report calls it "MONDO"; MONDO calls it **mandibuloacral dysplasia with type B lipodystrophy**
- `HP:0004322` (1 mention) - the report calls it "Physical"; HP calls it **Short stature**
- `HP:0000347` (1 mention) - the report calls it "Clinical sign"; HP calls it **Micrognathia**
- `HP:0006660` (1 mention) - the report calls it "Clinical sign"; HP calls it **Aplastic clavicle**
- `HP:0000270` (1 mention) - the report calls it "Clinical sign"; HP calls it **Delayed cranial suture closure**
- `HP:0000218` (1 mention) - the report calls it "Clinical sign"; HP calls it **High palate**
- `HP:0000678` (1 mention) - the report calls it "Clinical sign"; HP calls it **Dental crowding**
- `HP:0009771` (1 mention) - the report calls it "Radiographic"; HP calls it **Osteolytic defects of the phalanges of the hand**
- `HP:0009125` (1 mention) - the report calls it "Physical/metabolic"; HP calls it **Lipodystrophy**
- `HP:0002155` (1 mention) - the report calls it "Laboratory"; HP calls it **Hypertriglyceridemia**
- `HP:0003198` (1 mention) - the report calls it "Clinical sign"; HP calls it **Myopathy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001792` (1 mention) - the report calls it "Physical"; HP calls it **Small nail**, and lists "Hypoplastic nail" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0006974` - called "DNA-damage response", "DNA damage response"