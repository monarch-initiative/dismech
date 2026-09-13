---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-07T16:57:01.850540'
end_time: '2026-09-07T17:12:21.402077'
duration_seconds: 919.55
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 96
  mondo_id: MONDO:0030693
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 2
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 56
  verified: 53
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 30
  labels_matching: 14
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0000003
    reported_labels:
    - Multicystic kidney dysplasia
    - 2/5; Maffucci 2018
    ontology_label: Multicystic kidney dysplasia
  - term_id: HP:0000964
    reported_labels:
    - Eczematoid dermatitis
    - 1/5; Maffucci 2018
    ontology_label: Eczematoid dermatitis
  - term_id: HP:0000403
    reported_labels:
    - Recurrent otitis media
    - 1/1; 46BR
    ontology_label: Recurrent otitis media
  - term_id: HP:0001510
    reported_labels:
    - Growth delay
    - 1/1; Webster/Barnes 1992
    ontology_label: Growth delay
  - term_id: HP:0001270
    reported_labels:
    - Motor delay
    - 1/1; 46BR
    ontology_label: Motor delay
  - term_id: HP:0000524
    reported_labels:
    - Conjunctival telangiectasia
    - 1/1; 46BR
    ontology_label: Conjunctival telangiectasia
  - term_id: HP:0000992
    reported_labels:
    - Webster 1992
    ontology_label: Cutaneous photosensitivity
  labels_variant: 9
  obsolete_terms:
  - term_id: GO:0006266
    ontology_label: obsolete DNA ligation
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immunodeficiency_96-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_96-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 96
- **MONDO ID:** MONDO:0030693 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 96** covering all of the
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

# Immunodeficiency 96 (IMD96) — Comprehensive Disease Characterization

**MONDO:0030693 · OMIM #619774 · LIG1 (DNA ligase I) deficiency**

*Prepared as a disease knowledge-base entry. Evidence source types are indicated
(human clinical, model organism, in vitro/biochemical, computational/database).
Because this is an ultra-rare disorder, the entire primary human literature
consists of a small number of reports (~6 patients total); claims are cited to
those primary sources plus the founding biochemical and mouse-model studies.*

---

## Summary (answer to the research question)

Immunodeficiency 96 (IMD96) is a rare **autosomal recessive inborn error of
immunity caused by biallelic hypomorphic/amorphic mutations in *LIG1***, the gene
encoding **DNA ligase I**, the principal replicative DNA ligase in dividing
mammalian cells. Loss of ligase activity impairs joining of Okazaki fragments on
the lagging strand and completion of excision repair, producing replication
stress and genome instability that most affect rapidly proliferating lymphoid and
erythroid precursors. The clinical picture is a **combined/antibody
immunodeficiency of variable severity** — recurrent (mainly viral) respiratory,
gastrointestinal and urinary infections from infancy — accompanied by a
characteristic laboratory signature of **hypogammaglobulinemia, lymphopenia,
increased circulating γδ T cells, and erythrocyte macrocytosis**, with
predisposition to growth retardation, photosensitivity and lymphoma.

---

## 1. Disease Information

- **Overview.** IMD96 is a Mendelian, autosomal recessive DNA-repair/DNA-
  replication defect presenting as an immunodeficiency. It results from partial
  deficiency of DNA ligase I. Onset of recurrent, usually viral, respiratory
  infections occurs in infancy/early childhood; gastrointestinal and urinary
  tract infections also occur. (Source: OMIM/MONDO disease definition; human
  clinical — Maffucci 2018, PMID 30395541.)
- **Key identifiers.**
  - **MONDO:** MONDO:0030693 (immunodeficiency 96)
  - **OMIM (phenotype):** #619774
  - **OMIM (gene LIG1):** 126391
  - **DOID:** DOID:0061066
  - **MedGen:** C5676930 · **UMLS:** C5676930
  - **Orphanet:** No dedicated ORPHA code is firmly established for "IMD96"; the
    entity historically overlaps "DNA ligase I deficiency." *(Not confidently
    available — flag for curator verification.)*
  - **ICD-10:** D84.9 (Immunodeficiency, unspecified) / D80.x (predominantly
    antibody defects) as closest available codes; **ICD-11:** 4A00.x (primary
    immunodeficiencies). No IMD96-specific code. *(Approximate.)*
  - **MeSH:** No specific descriptor; nearest terms "Ligases"/"DNA Ligase ATP"
    and "Immunologic Deficiency Syndromes."
- **Synonyms / alternative names:** IMD96; "immunodeficiency, autosomal recessive
  due to LIG1 deficiency"; DNA ligase I deficiency; DNA ligase 1 deficiency; the
  index cell line/patient is historically referred to as **46BR**.
- **Data provenance:** Aggregated disease-level knowledge derived from a small
  number of **individual patient case reports** (n ≈ 6) plus biochemical and
  mouse-model studies — not from large EHR/registry cohorts.

## 2. Etiology

- **Primary cause — genetic:** Biallelic (homozygous or compound heterozygous)
  pathogenic variants in *LIG1*. Alleles are amorphic (null-like) or hypomorphic
  with residual activity; genotype severity tracks clinical/immunologic severity
  (human clinical/in vitro — Maffucci 2018, PMID 30395541; Barnes 1992, PMID
  1581963).
- **Genetic risk factors:** The disease is monogenic and fully genetically
  determined; the only "risk factor" is inheritance of two defective *LIG1*
  alleles. **Consanguinity** and being from a **kindred segregating LIG1
  variants** raise recurrence risk (AR inheritance). No established
  common-variant susceptibility loci or modifier genes are reported.
- **Environmental risk factors:** No environmental cause. However, because cells
  are hypersensitive to DNA-damaging agents, **exposure to genotoxins/UV/ionizing
  radiation/alkylating chemotherapeutics** may aggravate cellular pathology
  (in vitro — Barnes 1992, PMID 1581963). Photosensitivity is clinically observed.
- **Protective factors:** Retention of **residual LIG1 catalytic activity**
  (hypomorphic rather than null alleles) is protective — it explains survival and
  milder phenotypes, since complete loss is embryonic-lethal in mouse (model
  organism — Bentley 2002, PMID 11896201). No dietary/lifestyle protective
  factors are established.
- **Gene–environment interactions:** Genotoxic environmental exposures interact
  with the underlying repair defect (cells show hypersensitivity to a variety of
  DNA-damaging agents), plausibly increasing mutation load and cancer risk
  (in vitro — Barnes 1992, PMID 1581963). Direct GxE quantification is unavailable.

## 3. Phenotypes

*Frequencies below are the **exact n/N** from the official HPO annotation of
OMIM:619774 (sources: PMID 30395541 [Maffucci cohort] and PMID 1581963 [46BR
index patient]). Because the total described cohort is ~6 patients, "n/N" is the
most precise frequency obtainable.*

**HPO annotation table (curated, with frequencies):**
| HPO term | ID | Frequency | Source |
|---|---|---|---|
| Recurrent infections | HP:0002719 | 5/5 | PMID:30395541 |
| Decreased circulating IgG | HP:0004315 | 6/6 | PMID:30395541, 1581963 |
| Decreased circulating IgA | HP:0002720 | 6/6 | PMID:30395541, 1581963 |
| Decreased circulating IgM | HP:0002850 | 5/5 | PMID:30395541 |
| Increased mean corpuscular volume (macrocytosis) | HP:0005518 | 5/5 | PMID:30395541 |
| Increased γδ T-cell proportion | HP:0500270 | 4/4 | PMID:30395541 |
| Childhood onset | HP:0011463 | 3/5 | PMID:30395541 |
| Infantile onset | HP:0003593 | 2/5 | PMID:30395541 |
| Multicystic kidney dysplasia | HP:0000003 | 2/5 | PMID:30395541 |
| Eczematoid dermatitis | HP:0000964 | 1/5 | PMID:30395541 |
| Recurrent lower respiratory tract infections | HP:0002783 | 1/1 | PMID:1581963 |
| Recurrent otitis media | HP:0000403 | 1/1 | PMID:1581963 |
| Growth delay | HP:0001510 | 1/1 | PMID:1581963 |
| Motor delay | HP:0001270 | 1/1 | PMID:1581963 |
| Conjunctival telangiectasia | HP:0000524 | 1/1 | PMID:1581963 |
| Abnormal T-cell proliferation | HP:0031379 | 1/1 | PMID:1581963 |
| Intellectual disability (ABSENT) | HP:0001249 | 0/5 | PMID:30395541 |
| Autosomal recessive inheritance | HP:0000007 | — | PMID:1581963 |

*Narrative detail follows.*

**Infectious / immunologic (clinical signs & laboratory abnormalities)**
- **Recurrent respiratory infections, usually viral** — infancy/early-childhood
  onset; core presenting feature. HPO: *Recurrent respiratory infections*
  (HP:0002205); *Recurrent viral infections* (HP:0004429).
- **Gastrointestinal infections / diarrhea** — HP: *Chronic diarrhea*
  (HP:0002028); *Recurrent gastrointestinal infections* (HP:0004798).
- **Urinary tract infections** — HP:0000010.
- **Hypogammaglobulinemia** (laboratory) — reduced immunoglobulins across
  isotypes: **decreased IgG (HP:0004315, 6/6)**, **decreased IgA (HP:0002720,
  6/6)**, **decreased IgM (HP:0002850, 5/5)**; near-universal antibody deficiency
  (Maffucci 2018).
- **Lymphopenia** (laboratory) — HP:0001888.
- **Increased circulating γδ T cells** (laboratory; distinctive) — HP: *Abnormal
  proportion of gamma-delta T cells*/*Abnormal T cell subset distribution*
  (HP:0011848 / HP:0011840).
- **Combined immunodeficiency** in severe cases — HP:0005387 (severe combined
  immunodeficiency spectrum); severe end required HSCT.

**Hematologic**
- **Erythrocyte macrocytosis** (laboratory; distinctive) — HP: *Macrocytic
  anemia*/*Increased mean corpuscular volume* (HP:0001972 / HP:0005518).

**Other organ involvement / dermatologic / renal**
- **Multicystic kidney dysplasia** — HP:0000003 (2/5; Maffucci 2018) — notable
  extra-immune feature.
- **Eczematoid dermatitis** — HP:0000964 (1/5; Maffucci 2018).
- **Conjunctival telangiectasia** — HP:0000524 (1/1; 46BR) — mimics
  ataxia-telangiectasia (differential-diagnosis clue).
- **Recurrent otitis media** — HP:0000403 (1/1; 46BR).

**Growth / neurologic / neoplastic (from index patient, 46BR)**
- **Growth retardation / growth delay** — HP:0001510 (1/1; Webster/Barnes 1992).
- **Motor delay** — HP:0001270 (1/1; 46BR). **Intellectual disability is ABSENT**
  (HP:0001249, 0/5) — helps distinguish from ataxia-telangiectasia.
- **Cutaneous photosensitivity / sun sensitivity** — HP:0000992 (Webster 1992).
- **Predisposition to malignancy — lymphoma** — HP:0002665 (*Lymphoma*); the
  index patient died at 19 with lymphoma (Webster 1992, PMID 1351188).

**Phenotype characteristics.** Age of onset: **infancy/early childhood** (some
features, e.g., growth retardation, congenital/early). Severity: **variable**
(mild isolated antibody deficiency → combined immunodeficiency). Progression:
**chronic**, with risk of progressive immune compromise and late malignancy.
Frequency among affected individuals: infections, hypogammaglobulinemia,
lymphopenia, γδ-T-cell increase and macrocytosis were seen in most reported
patients (small n).

**Quality-of-life impact.** Recurrent infections and, in severe cases, need for
immunoglobulin replacement or HSCT substantially affect daily functioning;
malignancy risk and growth impairment add long-term burden. No formal EQ-5D/SF-36
data exist for this ultra-rare disorder.

## 4. Genetic / Molecular Information

- **Causal gene:** ***LIG1*** — DNA ligase 1. HGNC:6598; NCBI Gene 3978; Ensembl
  ENSG00000105486; OMIM gene 126391; UniProt **P18858**. Locus **19q13.33**
  (GRCh38 chr19:48,115,444–48,170,654, minus strand). (Computational/database —
  MyGene/Ensembl; MONDO xrefs.)
- **Pathogenic variants.**
  - *Variant class/type:* Predominantly **missense** hypomorphic alleles in the
    conserved catalytic domain, plus **frameshift/null** alleles. The index 46BR
    patient was **compound heterozygous** for **p.Glu566Lys (c.1696G>A)** and
    **p.Arg771Trp (c.2311C>T)** (NM_000234.3); p.Arg771 lies in the
    adenylation/AMP-binding active-site pocket, and p.Glu566Lys behaves as a
    near-null (Barnes 1992, PMID 1581963; Webster 1992, PMID 1351188). Maffucci
    2018 expanded the spectrum across 3 kindreds. Additional ClinVar
    Pathogenic/Likely-pathogenic loss-of-function alleles include **c.1244del
    (p.Thr415fs)** and **c.2444del (p.Leu815fs)**. (Database — ClinVar.)
  - *Classification (ACMG/AMP):* Reported disease alleles are **pathogenic /
    likely pathogenic** (e.g., p.Glu566Lys = Pathogenic in ClinVar), supported by
    segregation, functional (enzymatic) assays, and cellular repair-deficiency
    phenotypes.
  - *Functional consequence:* **Loss of function** — amorphic or hypomorphic
    alleles with **variably decreased ligase enzymatic activity** and a
    **strongly reduced ability to form the enzyme–adenylate intermediate**,
    leading to **premature release of unligated adenylated DNA** (in vitro —
    Barnes 1992, PMID 1581963; Maffucci 2018, PMID 30395541).
  - *Allele frequency:* Individual pathogenic alleles are ultra-rare in gnomAD;
    biallelic loss is extremely rare (carrier frequency not formally established).
    gnomAD v2.1.1 gene constraint shows LIG1 is **not haploinsufficient**
    (pLI≈0.004; oe_lof≈0.29, 90% CI 0.19–0.45; missense Z≈0.82), i.e.
    heterozygous loss is tolerated — consistent with recessive inheritance and
    healthy obligate carriers (index patient's mother and two brothers).
  - *Somatic vs germline:* **Germline**, inherited.
- **Modifier genes:** None established; residual *LIG1* activity itself is the
  main modifier of severity. Functional redundancy from DNA ligase III (LIG3)/XRCC1
  in some repair contexts may partially compensate (biological rationale).
- **Epigenetic information:** No disease-specific epigenetic signatures reported.
- **Chromosomal abnormalities:** None; IMD96 is a single-gene point-mutation
  disorder (chromosome 19). No aneuploidy/translocation etiology.

## 5. Environmental Information

- **Environmental factors:** Not causal. Cellular **hypersensitivity to
  DNA-damaging agents** (UV, ionizing radiation, alkylating agents) means such
  exposures are biologically relevant aggravators (in vitro — Barnes 1992,
  PMID 1581963); photosensitivity is clinically evident.
- **Lifestyle factors:** No established lifestyle contributors; sun protection is
  prudent given photosensitivity.
- **Infectious agents:** Infections are a **consequence** of immunodeficiency, not
  a cause. Reported/expected pathogens: **respiratory viruses** predominate;
  bacterial respiratory, gastrointestinal and urinary infections also occur.

## 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic hypomorphic/amorphic *LIG1* mutations** *lead to* reduced or absent
   functional DNA ligase I protein / enzymatic activity (in vitro — Maffucci 2018;
   Barnes 1992).
2. Impaired formation of the **enzyme–adenylate intermediate** *results in*
   inefficient nick sealing and **premature release of unligated, adenylated DNA**
   (in vitro — Barnes 1992, PMID 1581963; Maffucci 2018, PMID 30395541).
3. This *leads to* **retarded joining of Okazaki fragments** during lagging-strand
   DNA replication and **incomplete excision repair** (in vitro — Barnes 1992).
4. Which *results in* **accumulation of DNA replication intermediates, unligated
   nicks, replication stress and genome instability** (model organism — Bentley
   2002, PMID 11896201; *inferred* to operate similarly in human hematopoietic
   precursors).
5. Genome instability + replication stress *lead to* **reduced proliferation and
   survival of rapidly dividing cells**, disproportionately affecting **lymphoid
   and erythroid precursors** (model organism — Bentley 2002; *inferred* for human
   lineage-specific effects).
6. Branch A (lymphoid): *results in* **lymphopenia, impaired B-cell/antibody
   output (hypogammaglobulinemia), skewed T-cell subsets with increased γδ T
   cells** → **recurrent viral/bacterial infections and combined
   immunodeficiency**.
7. Branch B (erythroid): *results in* **impaired erythropoiesis with erythrocyte
   macrocytosis** (phenocopying impaired DNA synthesis).
8. Branch C (genome-wide, long-term): cumulative genome instability *leads to*
   **cancer predisposition (lymphoma)**, and in skin, UV-hypersensitivity
   *contributes to* **photosensitivity**; systemic replication impairment
   *contributes to* **growth retardation** (human clinical — Webster 1992,
   PMID 1351188).

**Category detail supporting these steps**
- **Molecular pathways / processes:** DNA replication (lagging-strand Okazaki
  fragment maturation), **long-patch base excision repair**, nucleotide/excision
  repair completion. GO: *DNA ligation* (GO:0006266), *DNA replication*
  (GO:0006260), *base-excision repair* (GO:0006284), *DNA repair* (GO:0006281),
  *lagging strand elongation* (GO:0006273).
- **Cellular processes:** Replication stress, cell-cycle impairment, reduced
  proliferation/survival of precursors, genome instability. GO: *cellular
  response to DNA damage stimulus* (GO:0006974).
- **Protein dysfunction:** Loss/hypomorphic **DNA ligase I** (UniProt **P18858**,
  919 aa; ATP-dependent ligase; PCNA-interacting replicative ligase). Domain map:
  N-terminal disordered regulatory region (1–270) carrying the **PCNA-interacting/
  replication-factory-targeting sequence** and CDK phosphosites; central
  **adenylation (catalytic) domain** with **active-site Lys568** (forms the
  N6-AMP-lysine enzyme–adenylate intermediate) and AMP/ATP-binding residues at
  566, 573, 621, 720, 725, 744; C-terminal **OB-fold DNA-binding domain**.
  Disease variants map directly onto catalysis: **p.Glu566Lys alters an
  AMP-binding residue adjacent to catalytic Lys568** (abolishing adenylation —
  matching the measured loss of enzyme–adenylate formation), and **p.Arg771Trp**
  disrupts the OB-fold DNA/nick-binding surface. GO cellular component:
  *nucleus* (GO:0005634), *replication fork* (GO:0005657). PDB: **1X9N**
  (human LIG1–DNA complex). (Database — UniProt/PDB; in vitro — Barnes 1992.)
- **Immune system involvement:** **Immunodeficiency** (combined + humoral) from
  impaired lymphocyte development/proliferation and antibody production.
- **Tissue-damage mechanism:** Genotoxic stress/genome instability rather than
  inflammation or ischemia.
- **Cell types (CL):** hematopoietic stem/progenitor cell (CL:0000037), T cell
  (CL:0000084) incl. γδ T cell (CL:0000798), B cell (CL:0000236), erythroid
  progenitor (CL:0000038).
- **Molecular profiling:** No large omics datasets; functional biochemistry
  (ligase/adenylation assays) and cellular DNA-damage survival assays are the
  principal readouts (Barnes 1992; Maffucci 2018).

## 7. Anatomical Structures Affected

- **Organ/system level:** **Immune (hematolymphoid) system** is primary —
  bone marrow, thymus, lymphoid tissues (UBERON:0002405 immune system;
  UBERON:0002371 bone marrow; UBERON:0002370 thymus). Secondary involvement:
  **respiratory tract** (recurrent infection; UBERON:0001004), **gastrointestinal
  tract** (UBERON:0001555), **urinary tract** (UBERON:0011143), **kidney**
  (UBERON:0002113; multicystic kidney dysplasia in 2/5 — developmental/structural
  involvement), **skin** (UBERON:0002097; eczema, photosensitivity, conjunctival
  telangiectasia), and systemic growth.
- **Tissue/cell level:** Hematopoietic tissue; **lymphocytes** (T incl. γδ, B),
  **erythroid lineage**; skin epithelium (UV sensitivity). CL terms as in §6.
- **Subcellular level:** **Nucleus** (GO:0005634) — site of DNA replication/repair
  where DNA ligase I acts (GO cellular component: *replication fork*, GO:0005657;
  *nuclear replication fork*, GO:0043596).
- **Localization / lateralization:** Systemic (not lateralized); infections and
  manifestations are bilateral/diffuse.

## 8. Temporal Development

- **Onset:** **Infancy/early childhood** for infections; growth retardation and
  photosensitivity may be evident early. Pattern: **chronic/insidious** with
  recurrent acute infective episodes.
- **Progression:** Variable — from **stable mild antibody deficiency** to
  **progressive combined immunodeficiency**. Genome instability confers
  **late-onset malignancy risk** (lymphoma in the index patient at age 19).
- **Course & duration:** **Chronic, lifelong.** Recurrent-infection pattern;
  severe cases progress to transplant dependence.
- **Remission / critical windows:** No spontaneous remission; **HSCT can be
  curative** for the immune defect. Early diagnosis before severe infections or
  malignancy is the key intervention window.

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** (homozygous or compound heterozygous
  *LIG1*); parents are typically asymptomatic carriers (Webster 1992: one mutation
  inherited from the mother and also present in two healthy brothers — carriers).
- **Penetrance / expressivity:** Presumed high penetrance for biallelic damaging
  genotypes but **markedly variable expressivity/severity**, correlating with
  residual ligase activity (Maffucci 2018, PMID 30395541).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism / founder effects:** None reported.
- **Consanguinity:** Relevant, as for AR disorders (homozygous cases).
- **Carrier frequency:** Not established; individual alleles ultra-rare in gnomAD.
- **Epidemiology:** **Ultra-rare** — only ~6 molecularly confirmed patients
  described (1 index case + 5 in Maffucci 2018). Prevalence/incidence per 100,000
  are not calculable and are effectively unknown/<1 in 10^6.
- **Demographics:** Reported across more than one kindred/ethnicity; no strong
  sex predilection established (index case female). No defined geographic focus.

## 10. Diagnostics

- **Laboratory tests (LOINC-type):** CBC showing **erythrocyte macrocytosis
  (elevated MCV)** and **lymphopenia**; **serum immunoglobulins** showing
  **hypogammaglobulinemia**; specific antibody responses (impaired).
- **Immunophenotyping (flow cytometry):** **Increased proportion of circulating
  γδ T cells**, altered T-cell subsets; a distinctive combination with macrocytosis
  and hypogammaglobulinemia should prompt LIG1 testing (Maffucci 2018).
- **Functional/cellular assays (in vitro):** **Cellular hypersensitivity to
  DNA-damaging agents**; **retarded Okazaki-fragment joining**; **reduced DNA
  ligase I adenylation/enzymatic activity** — historically used to characterize
  46BR (Barnes 1992, PMID 1581963).
- **Biomarkers:** The **triad (macrocytosis + γδ-T-cell increase +
  hypogammaglobulinemia)** is a useful clinical flag; premature release of
  unligated adenylated DNA is a research biochemical marker.
- **Genetic testing (primary confirmatory):** **WES/WGS or IEI gene panels**
  including *LIG1*; confirm biallelic variants by **Sanger**. Single-gene *LIG1*
  sequencing where phenotype is suggestive. CMA/karyotype/FISH generally
  uninformative (point-mutation disorder).
- **Clinical criteria / differential diagnosis:** Distinguish from **Bloom
  syndrome** (BLM; the index patient resembled Bloom's but lacked BLM mutation —
  Webster 1992), other **DNA-repair/genome-instability syndromes** (Fanconi
  anemia, ataxia-telangiectasia, Nijmegen breakage syndrome), **common variable
  immunodeficiency**, and combined immunodeficiencies. Macrocytosis + γδ-T-cell
  increase help separate IMD96 from typical CVID.
- **Screening:** Cascade/carrier testing within affected families; no
  population newborn screening.

## 11. Outcome / Prognosis

- **Severity spectrum:** From **mild antibody deficiency** (favorable with Ig
  replacement) to **severe combined immunodeficiency requiring HSCT** (Maffucci
  2018).
- **Mortality/survival:** No formal survival statistics (ultra-rare). Severe,
  untreated disease carries risk of fatal infection; **the index patient died at
  age 19 of lymphoma** (Webster 1992), illustrating malignancy-related mortality.
- **Morbidity:** Recurrent infections, growth retardation, treatment burden
  (immunoglobulin therapy, transplant), and long-term cancer risk.
- **Prognostic factors:** **Residual LIG1 enzymatic activity / genotype** is the
  key determinant; earlier diagnosis and definitive therapy (HSCT) improve
  immune outcomes. No validated QoL instruments for this disease.

## 12. Treatment

*No disease-specific approved drug exists; management follows inborn-errors-of-
immunity principles.*
- **Supportive / pharmacotherapy:** **Immunoglobulin replacement therapy (IVIG/
  SCIG)** for hypogammaglobulinemia; **antimicrobial prophylaxis and aggressive
  treatment of infections**. NCIT: *Intravenous Immunoglobulin Therapy*
  (approx.), *Antibiotic Therapy*.
- **Definitive/advanced therapy:** **Allogeneic hematopoietic stem cell
  transplantation (HSCT)** for the severe combined-immunodeficiency end of the
  spectrum (used in Maffucci 2018 cohort). NCIT: *Hematopoietic Stem Cell
  Transplantation* (C15431). Gene therapy is conceptually plausible but **not**
  reported/established for IMD96.
- **Caution — genotoxic agents:** Given DNA-repair deficiency and cellular
  hypersensitivity, use **radiation and alkylating/DNA-damaging chemotherapeutics
  with caution** (e.g., in transplant conditioning or any cancer therapy)
  (in vitro rationale — Barnes 1992).
- **Pharmacogenomics / personalized:** Genotype (residual ligase activity) informs
  whether Ig replacement suffices vs. need for HSCT.
- **Treatment outcomes / adverse events:** HSCT can restore immune function;
  standard transplant risks apply, potentially heightened by conditioning-related
  genotoxic sensitivity. Formal response-rate data are lacking (small n).

## 13. Prevention

- **Primary prevention:** Not preventable (germline). **Genetic counseling** for
  AR recurrence risk (25% per pregnancy for carrier couples); **carrier/cascade
  testing** in affected families; **prenatal or preimplantation genetic testing**
  where a familial variant is known.
- **Secondary prevention:** Early recognition of the lab triad → early molecular
  diagnosis → early institution of Ig replacement/prophylaxis or HSCT before
  irreversible complications; **malignancy surveillance** given lymphoma risk.
- **Tertiary prevention:** Infection prophylaxis, immunizations as appropriate for
  immune status, **sun protection** (photosensitivity), avoidance of unnecessary
  genotoxic exposures.
- **Public health / behavioral:** No population-level measures beyond counseling.

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *LIG1* is highly conserved. Mouse *Lig1* (NCBI Gene
  16881; NCBI Taxon 10090); orthologs across vertebrates and lower eukaryotes
  (CDC9 in *S. cerevisiae*). Evolutionary conservation of the replicative-ligase
  function is strong.
- **Natural disease in animals:** No well-characterized spontaneous *LIG1*
  immunodeficiency reported in companion animals/wildlife (OMIA — none prominent).
- **Comparative biology:** Complete loss is **embryonic lethal in mouse** (Bentley
  2002, PMID 11896201), underscoring conserved essentiality; human patients
  survive due to residual activity of hypomorphic alleles — a key cross-species
  contrast.
- **Transmission / zoonosis:** Not applicable (non-infectious genetic disease).

## 15. Model Organisms

- **Mouse (*Mus musculus*, NCBI Taxon 10090):** ***Lig1* knockout** — two
  independent null alleles; **embryos develop normally to mid-gestation then die
  from a specific hematopoietic (fetal-liver) defect** that is a **quantitative
  proliferation deficiency** rather than a lineage block; *Lig1*-null fibroblasts
  accumulate replication intermediates and show **increased genome instability**
  despite grossly normal repair activity (Bentley 2002, PMID 11896201). MGI-type
  resources apply.
- **Cellular models (in vitro):** The human **46BR fibroblast strain** (index
  patient) and **engineered LIG1-deficient cell lines** demonstrating chemical/
  radiation repair defects and reduced ligase activity (Barnes 1992, PMID 1581963;
  Maffucci 2018, PMID 30395541).
- **Phenotype recapitulation:** Mouse null captures the **hematopoietic
  proliferation defect and genome instability** central to human pathology but is
  **more severe (lethal)** and does not model the survivable, variable human
  immunodeficiency (embryonic lethality precludes study of mature adaptive
  immunity). Human hypomorphic cell lines better model the partial-deficiency
  disease.

---

## Supported vs. refuted hypotheses

- **Supported:** IMD96 = autosomal recessive **LIG1 (DNA ligase I) deficiency**
  (MONDO:0030693 / OMIM 619774). Mechanism = impaired Okazaki-fragment ligation +
  excision-repair completion → genome instability → lymphoid/erythroid
  proliferation failure. Characteristic labs: hypogammaglobulinemia, lymphopenia,
  increased γδ T cells, erythrocyte macrocytosis. HSCT curative for severe cases.
- **Supported (residue-level mechanism):** disease variants map onto the LIG1
  catalytic pocket — **p.Glu566Lys** hits an AMP-binding residue adjacent to
  **active-site Lys568** (abolishing the enzyme–adenylate step measured by Barnes
  1992), while **p.Arg771Trp** disrupts the OB-fold DNA-binding domain — a direct
  structural explanation for the loss-of-function biochemistry. gnomAD confirms
  LIG1 is not haploinsufficient (pLI≈0.004), consistent with recessive inheritance
  and healthy carriers.
- **Supported (phenotype frequencies):** curated HPO annotations give
  near-complete penetrance for decreased IgG/IgA (6/6), decreased IgM (5/5),
  macrocytosis (5/5), increased γδ T cells (4/4) and recurrent infections (5/5);
  intellectual disability is explicitly absent (0/5), and renal (multicystic
  kidney dysplasia 2/5) plus dermatologic features broaden the spectrum.
- **Refuted / corrected:** Initial assumption that "Immunodeficiency 96" was the
  REL/c-Rel disorder was **wrong** — c-Rel deficiency is **Immunodeficiency 92
  (IMD92)**. This was corrected by resolving MONDO:0030693 to LIG1.
- **Refuted historically:** The index patient was NOT Bloom syndrome despite
  clinical resemblance (Webster 1992) — a distinct genetic entity.

## Limitations & future directions

- **Ultra-rare** with ~6 molecularly confirmed patients; frequencies, penetrance,
  survival and QoL are not quantifiable. Orphanet/ICD-specific codes are
  uncertain and need curator confirmation.
- No omics (transcriptomic/proteomic/metabolomic) disease datasets; no dedicated
  gene therapy program.
- Future work: define exact recurrent *LIG1* alleles and genotype–phenotype/
  residual-activity correlations; systematic malignancy-risk surveillance;
  conditional/hypomorphic mouse or patient-iPSC models to study lineage-specific
  immune defects and to test safer (reduced-genotoxicity) transplant conditioning.

## Key references (PMID)

- **30395541** — Maffucci et al. 2018, *J Clin Invest*: biallelic LIG1 mutations
  underlie a spectrum of immune deficiencies (5 patients/3 kindreds). *(Human
  clinical + in vitro.)*
- **1351188** — Webster et al. 1992, *Lancet*: growth retardation and
  immunodeficiency with LIG1 mutations (index patient; lymphoma at 19). *(Human
  clinical.)*
- **1581963** — Barnes et al. 1992, *PNAS*: LIG1 mutations in 46BR; Okazaki-
  fragment/excision-repair defect; reduced enzyme-adenylate formation. *(In vitro/
  biochemical.)*
- **11896201** — Bentley et al. 2002: *Lig1*-null mouse; embryonic-lethal
  hematopoietic proliferation defect and genome instability. *(Model organism.)*


## Artifacts

- [OpenScientist final report](Immunodeficiency_96-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_96-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 56 |
| Resolved | 53 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 30 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000003` (2 mentions) - the report calls it "Multicystic kidney dysplasia", "2/5; Maffucci 2018"; HP calls it **Multicystic kidney dysplasia**
- `HP:0000964` (2 mentions) - the report calls it "Eczematoid dermatitis", "1/5; Maffucci 2018"; HP calls it **Eczematoid dermatitis**
- `HP:0000403` (2 mentions) - the report calls it "Recurrent otitis media", "1/1; 46BR"; HP calls it **Recurrent otitis media**
- `HP:0001510` (2 mentions) - the report calls it "Growth delay", "1/1; Webster/Barnes 1992"; HP calls it **Growth delay**
- `HP:0001270` (2 mentions) - the report calls it "Motor delay", "1/1; 46BR"; HP calls it **Motor delay**
- `HP:0000524` (2 mentions) - the report calls it "Conjunctival telangiectasia", "1/1; 46BR"; HP calls it **Conjunctival telangiectasia**
- `HP:0000992` (1 mention) - the report calls it "Webster 1992"; HP calls it **Cutaneous photosensitivity**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006266` (obsolete DNA ligation) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0004315` (2 mentions) - the report calls it "Decreased circulating IgG"; HP calls it **Decreased circulating IgG concentration**, and lists "Decreased circulating IgG level" among its other names
- `HP:0002720` (2 mentions) - the report calls it "Decreased circulating IgA"; HP calls it **Decreased circulating IgA concentration**, and lists "Decreased circulating IgA level" among its other names
- `HP:0002850` (2 mentions) - the report calls it "Decreased circulating IgM"; HP calls it **Decreased circulating IgM concentration**
- `HP:0005518` (2 mentions) - the report calls it "Increased mean corpuscular volume (macrocytosis)"; HP calls it **Increased mean corpuscular volume**
- `HP:0500270` (1 mention) - the report calls it "Increased γδ T-cell proportion"; HP calls it **Increased gamma-delta T cell proportion**
- `HP:0001249` (2 mentions) - the report calls it "Intellectual disability (ABSENT)"; HP calls it **Intellectual disability**
- `GO:0006266` (1 mention) - the report calls it "DNA ligation"; GO calls it **obsolete DNA ligation**
- `GO:0005634` (2 mentions) - the report calls it "nucleus", "Nucleus", "Subcellular level:** **Nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names
- `UBERON:0011143` (1 mention) - the report calls it "urinary tract"; UBERON calls it **upper urinary tract**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000003` - called "Multicystic kidney dysplasia", "2/5; Maffucci 2018"
- `HP:0000964` - called "Eczematoid dermatitis", "1/5; Maffucci 2018"
- `HP:0000403` - called "Recurrent otitis media", "1/1; 46BR"
- `HP:0001510` - called "Growth delay", "1/1; Webster/Barnes 1992"
- `HP:0001270` - called "Motor delay", "1/1; 46BR"
- `HP:0000524` - called "Conjunctival telangiectasia", "1/1; 46BR"
- `GO:0005634` - called "nucleus", "Nucleus", "Subcellular level:** **Nucleus"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.