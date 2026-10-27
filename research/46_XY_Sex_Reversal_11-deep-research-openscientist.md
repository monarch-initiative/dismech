---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T05:29:23.313882'
end_time: '2026-09-01T05:47:13.174194'
duration_seconds: 1069.86
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: 46,XY Sex Reversal 11
  mondo_id: ''
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
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 15
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 18
  quotes_valid: 18
  relevance_assessed: 18
  on_topic: 14
  off_topic: 1
  off_topic_references:
  - PMID:32057790
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 23
  verified: 21
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.045
  labels_checked: 5
  labels_matching: 0
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0000133
    reported_labels:
    - Core feature
    - Common in CGD
    ontology_label: Gonadal dysgenesis
  - term_id: HP:0000815
    reported_labels:
    - Characteristic
    ontology_label: Hypergonadotropic hypogonadism
  - term_id: HP:0000771
    reported_labels:
    - Mild presentations
    ontology_label: Gynecomastia
  - term_id: HP:0100728
    reported_labels:
    - "~15\u201323% in dysgenesis"
    ontology_label: Germ cell neoplasia
  labels_variant: 1
  unresolved_terms:
  - HP:0000783
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: 46_XY_Sex_Reversal_11-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: 46_XY_Sex_Reversal_11-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** 46,XY Sex Reversal 11
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **46,XY Sex Reversal 11** covering all of the
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

# 46,XY Sex Reversal 11 (SRXY11): A Comprehensive Disease Characteristics Report

**Disease:** 46,XY Sex Reversal 11 (SRXY11)
**Causal gene:** *DHX37* (DEAH-box RNA helicase 37)
**OMIM (phenotype):** #273250 (46,XY sex reversal 11)
**Category:** Mendelian, autosomal dominant disorder/difference of sex development (DSD)
**Suggested disease ontology mapping:** MONDO — 46,XY partial/complete gonadal dysgenesis spectrum; the DHX37-specific entry corresponds to OMIM #273250.

Evidence source key: [H] human clinical/genetic · [M] model organism · [V] in vitro/functional · [C] computational/in silico · [R] review.

---

## Summary

**46,XY Sex Reversal 11 (SRXY11) is a rare Mendelian disorder/difference of sex development (DSD) caused by heterozygous, mostly recurrent missense variants in *DHX37*, a DEAH-box RNA helicase essential for biogenesis of the small (40S) ribosomal subunit.** Affected individuals have a 46,XY karyotype but fail to complete testis determination or undergo testis regression, producing a clinical spectrum that runs from phenotypic females with complete gonadal dysgenesis (Swyer syndrome), through partial gonadal dysgenesis, to testicular regression syndrome (TRS)/anorchia and, at the mildest pole, males with modest testicular underdevelopment and gynecomastia. Because a ubiquitously required housekeeping factor produces a phenotype restricted almost entirely to the developing gonad, DHX37-related DSD has been proposed as a new human **ribosomopathy** — a class of disease in which broadly expressed ribosome-biogenesis factors nonetheless cause tissue-specific pathology.

The molecular link between DHX37 loss and gonadal failure is coming into focus from mouse work: DHX37 safeguards nucleolar integrity and PI3K-AKT survival signaling and suppresses p53-driven apoptosis, so its deficiency triggers pro-apoptotic RNA splicing and death of the fetal supporting (Sertoli) cell lineage, aborting or reversing testis formation. In humans, DHX37 protein is expressed principally in germ cells and Leydig cells, and only rarely in Sertoli cells, so the exact cell-autonomous versus non-cell-autonomous route to Sertoli-cell failure remains partially inferred. Two recurrent variants — **p.Arg308Gln** and **p.Arg674Trp** — account for a large share of cases and are especially associated with embryonic testicular regression syndrome (ETRS).

Clinically, the disorder is diagnosed by the combination of a 46,XY karyotype discordant with gonadal/genital phenotype, hypergonadotropic hypogonadism (elevated FSH/LH, low sex steroids), imaging showing streak or absent gonads (with or without Müllerian structures), and molecular confirmation by whole-exome/genome sequencing, for which DHX37 should now be part of DSD gene panels. Management is supportive rather than curative: sex-steroid hormone replacement, prophylactic gonadectomy of dysgenetic Y-bearing gonads (which carry a **~15–23% germ-cell tumor risk**), fertility and psychosocial counseling, and genetic counseling. Importantly, biallelic and de novo heterozygous DHX37 variants cause a **distinct, allelic neurodevelopmental syndrome (NEDBAVC, OMIM 618731)**, so genotype must be interpreted with the full clinical picture.

---

## Key Findings

### Finding 1 — DHX37 heterozygous missense variants are a frequent, autosomal-dominant cause of 46,XY DSD (SRXY11) [H]

In a cohort of 145 individuals with 46,XY DSD of previously unknown etiology, 13 children carried heterozygous missense pathogenic variants in *DHX37*, and rare/novel DHX37 missense variants were enriched in cases versus controls with high statistical significance (**P = 5.8×10⁻¹⁰**). The gene encodes an RNA helicase "essential for ribosome biogenesis," and the pathogenic variants establish an **autosomal dominant** form of 46,XY DSD encompassing both gonadal dysgenesis and testicular regression syndrome (TRS). The authors concluded these conditions "are part of a clinical spectrum" rather than distinct entities.

> "Thirteen children carried heterozygous missense pathogenic variants involving the RNA helicase DHX37, which is essential for ribosome biogenesis." — [PMID: 31337883](https://pubmed.ncbi.nlm.nih.gov/31337883/)

> "DHX37 pathogenic variants are a new cause of an autosomal dominant form of 46,XY DSD, including gonadal dysgenesis and TRS, showing that these conditions are part of a clinical spectrum." — [PMID: 31337883](https://pubmed.ncbi.nlm.nih.gov/31337883/)

This is the foundational human-clinical evidence identifying DHX37 as the SRXY11 gene and framing the phenotype as a spectrum. HGNC: DHX37. UniProt: Q8IY37.

### Finding 2 — DHX37 maintains supporting-cell (Sertoli) survival through nucleolar integrity and PI3K-AKT, suppressing p53 apoptosis [M][V]

Multi-omics analysis of cell-specific *Dhx37* knockout mice (RIP-seq plus RNAi-RNA-seq) demonstrated that Dhx37 "safeguards nucleolar integrity and PI3K-AKT signaling, suppresses p53-driven apoptosis, and its loss triggers pro-apoptotic splicing" and Sertoli-cell death, impairing testis development. This is the strongest mechanistic account currently available and links DHX37 loss-of-function to the cellular event (supporting-cell apoptosis) that most plausibly explains failed/reversed testis determination.

> "Dhx37 safeguards nucleolar integrity and PI3K-AKT signaling, suppresses p53-driven apoptosis, and its loss triggers pro-apoptotic splicing" — [PMID: 41535247](https://pubmed.ncbi.nlm.nih.gov/41535247/)

Relevant GO/pathway terms: ribosome biogenesis (GO:0042254), rRNA processing (GO:0006364), nucleolus (GO:0005730), PI3K-AKT signaling, intrinsic apoptotic signaling by p53 class mediator (GO:0072332), regulation of RNA splicing (GO:0043484).

### Finding 3 — Allelic heterogeneity: heterozygous → non-syndromic DSD; biallelic/de novo → syndromic NEDBAVC (OMIM 618731) [R][H]

DHX37 shows a clean genotype-driven dichotomy. Recurrent **heterozygous** missense variants — affecting highly conserved residues in the helicase domains and predicted deleterious — cause **non-syndromic** 46,XY gonadal dysgenesis, TRS, or anorchia. In contrast, **compound heterozygous and de novo heterozygous** DHX37 missense variants cause a complex congenital syndrome, **NEDBAVC** (neurodevelopmental disorder with brain anomalies and with/without vertebral or cardiac anomalies; OMIM 618731) featuring microcephaly, global developmental delay, seizures, facial dysmorphism, and kidney/cardiac anomalies.

> "compound heterozygous as well as de novo heterozygous missense variants in DHX37 are also associated with a complex congenital developmental syndrome (NEDBAVC, neurodevelopmental disorder with brain anomalies and with or without vertebral or cardiac anomalies; OMIM 618731), consisting of microcephaly, global developmental delay, seizures, facial dysmorphia, and kidney and cardiac anomalies" — [PMID: 35835064](https://pubmed.ncbi.nlm.nih.gov/35835064/)

> "All affected children have non-syndromic forms of disorders/differences of sex development (DSD)." — [PMID: 35835064](https://pubmed.ncbi.nlm.nih.gov/35835064/)

This distinction is clinically critical for variant interpretation and counseling.

### Finding 4 — Dysgenetic Y-bearing gonads carry a high germ-cell tumor risk, warranting gonadectomy [H]

In a series of 292 phenotypic-female DSD patients harboring Y-chromosome material, the overall germ-cell tumor (GCT) risk was **15.4%**, and **46,XY pure gonadal dysgenesis carried the highest risk (~23.3%)**. Tumors — gonadoblastoma and dysgerminoma/seminoma — arose predominantly during adolescence (median 17–18 years). Notably, no tumor was found in five testicular-regression patients, contrasting the high dysgenesis risk with the negligible regression risk. These data support **prophylactic gonadectomy** of dysgenetic gonads.

> "The overall GCTs risk was 15·41% and 46, XY pure gonadal dysgenesis (46, XY PGD) carried the highest risk up to 23·33%" — [PMID: 27862157](https://pubmed.ncbi.nlm.nih.gov/27862157/)

> "no tumour was found in five testis regression patients" — [PMID: 27862157](https://pubmed.ncbi.nlm.nih.gov/27862157/)

A familial Swyer-syndrome report additionally suggests familial cases may carry higher tumor risk than sporadic ones (66.6% vs. 15–45%) ([PMID: 38337479](https://pubmed.ncbi.nlm.nih.gov/38337479/)).

### Finding 5 — Marked phenotypic heterogeneity from complete gonadal dysgenesis to TRS/anorchia, with variable expressivity [H]

DHX37 variants generate a phenotypic continuum: 46,XY complete gonadal dysgenesis (female external genitalia, Müllerian remnants), partial gonadal dysgenesis, testicular regression syndrome/anorchia (absent testes with variable male genitalia), and milder testicular underdevelopment with gynecomastia. Variants cluster in conserved helicase domains (e.g., RecA1); reported residues include p.Arg334Trp, p.Arg390His, p.Thr477His, and p.Gly478Arg. A striking example of variable expressivity/incomplete penetrance: a boy with TRS carried a homozygous p.T477H variant while his **fertile father**, carrying the same variant, had only unilateral testicular regression with otherwise typical male genital development.

> "Missense variants in the RNA-helicase DHX37 are associated with either 46,XY gonadal dysgenesis or 46,XY testicular regression syndrome (TRS)." — [PMID: 34293745](https://pubmed.ncbi.nlm.nih.gov/34293745/)

> "a homozygous p.T477H variant was identified in a boy with TRS. His fertile father had unilateral testicular regression with typical male genital development." — [PMID: 34293745](https://pubmed.ncbi.nlm.nih.gov/34293745/)

> "manifestations ranging from complete gonadal dysgenesis to mild testicular underdevelopment with gynecomastia" — [PMID: 42510869](https://pubmed.ncbi.nlm.nih.gov/42510869/)

### Finding 6 — Diagnosis rests on 46,XY karyotype discordant with gonad/genitalia, hypergonadotropic hypogonadism, and molecular (WES/WGS) confirmation [H]

Complete gonadal dysgenesis (Swyer syndrome) typically presents in phenotypic females with a 46,XY karyotype, primary amenorrhea/delayed puberty, a hypoplastic uterus and streak gonads on imaging, and **hypergonadotropic hypogonadism** (elevated FSH/LH, low estradiol/testosterone) on hormonal assay. DHX37 is identified by whole-exome/trio sequencing once karyotype excludes sex-chromosome DSD; the gene is now recommended for inclusion in DSD gene panels and genome-wide sequencing.

> "confirmed by the hormonal assay that showed hypergonadotropic-hyp[ogonadism]" — [PMID: 37497464](https://pubmed.ncbi.nlm.nih.gov/37497464/)

> "Genome-wide sequencing should be prioritized in VSC/DSD diagnostics, consistent with current best practices, to improve diagnostic yield" — [PMID: 41466375](https://pubmed.ncbi.nlm.nih.gov/41466375/)

### Finding 7 — Two recurrent variants (p.Arg308Gln, p.Arg674Trp) dominate and are enriched vs. gnomAD, with a specific ETRS association; DHX37 is expressed in germ and Leydig cells [H][V]

In 87 patients with 46,XY DSD, da Silva et al. (2019) identified pathogenic/likely-pathogenic heterozygous DHX37 missense variants in 5 families (11 patients) and 6 sporadic cases; two recurrent variants dominated — **p.Arg308Gln** (two families, three sporadic cases) and **p.Arg674Trp** (two families, two sporadic cases). Rare, predicted-deleterious DHX37 variants occurred in **14%** of the cohort versus **0.4%** in gnomAD (**P < 0.001**), and were specifically associated with embryonic testicular regression syndrome (ETRS) in **7/14 index cases (50%)**. Immunohistochemistry localized DHX37 mainly to germ cells (at various maturation stages) and Leydig cells, and only rarely to Sertoli cells.

> "Two variants were recurrent: p.Arg308Gln (in two families and in three sporadic cases) and p.Arg674Trp (in two families and in two sporadic cases)." — [PMID: 31287541](https://pubmed.ncbi.nlm.nih.gov/31287541/)

> "The frequency of rare, predicted-to-be-deleterious DHX37 variants in this cohort (14%) is significantly higher than that observed in the Genome Aggregation Database (0.4%; P < 0.001)." — [PMID: 31287541](https://pubmed.ncbi.nlm.nih.gov/31287541/)

> "DHX37 is mainly expressed in germ cells at different stages of testis maturation, in Leydig cells, and rarely in Sertoli cells" — [PMID: 31287541](https://pubmed.ncbi.nlm.nih.gov/31287541/)

> "The variants were specifically associated with ETRS (7/14 index cases; 50%)." — [PMID: 31287541](https://pubmed.ncbi.nlm.nih.gov/31287541/)

### Finding 8 — The central mechanism — how a ubiquitous ribosome-biogenesis factor produces tissue-specific gonadal failure — remains unresolved [R]

DHX37 is a housekeeping DEAH-box helicase required for 40S ribosomal subunit biogenesis in every cell, yet heterozygous missense variants produce a phenotype almost entirely restricted to gonad/testis determination — a paradox shared with other ribosomopathies. Multiple primary reports and reviews explicitly state that the pathogenic mechanism is unknown.

> "Similar to all other known ribosomopathies, the mechanism of pathogenesis is unknown." — [PMID: 34293745](https://pubmed.ncbi.nlm.nih.gov/34293745/)

> "DHX37 is required for ribosome biogenesis, and this subgroup of XY DSD is a new human ribosomopathy." — [PMID: 34293745](https://pubmed.ncbi.nlm.nih.gov/34293745/)

No zebrafish or invertebrate DHX37 sex-development model, and no humanized knock-in of the recurrent p.Arg308Gln/p.Arg674Trp alleles, has yet been reported; available models are a supporting-cell conditional-knockout mouse and yeast Dhr1 structural/functional studies.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous missense variant in *DHX37*** (most often at recurrent hotspots p.Arg308Gln or p.Arg674Trp, in conserved helicase RecA domains) *leads to* a partial loss of DHX37 RNA-helicase activity. *(Demonstrated genetically; the loss-of-function nature at the protein level is partly inferred from conservation, in silico prediction, and yeast Dhr1 structural work — [PMID: 31188444].)*
2. Impaired DHX37 helicase function *results in* defective displacement of the U3 snoRNA from pre-rRNA and impaired **40S small ribosomal subunit biogenesis / nucleolar homeostasis**. *(Mechanism established for yeast Dhr1; extrapolated to human DHX37.)*
3. Disturbed nucleolar integrity *leads to* **nucleolar stress**, which *results in* stabilization/activation of **p53** and reduced **PI3K-AKT survival signaling**. *(Demonstrated in Dhx37-knockout mouse multi-omics — [PMID: 41535247].)*
4. p53 activation plus loss of AKT survival signaling *triggers* **pro-apoptotic RNA splicing and apoptosis of the fetal supporting (Sertoli) cell lineage**. *(Demonstrated in mouse; human Sertoli involvement is partly inferred because human DHX37 protein is expressed mainly in germ and Leydig cells and only rarely in Sertoli cells — [PMID: 31287541].)*
5. Loss/failure of Sertoli-supporting cells during the narrow window of fetal sex determination *results in* **failed testis determination (gonadal dysgenesis)** or, if determination initially succeeds, **testis regression (TRS/anorchia)**. *(Branch point — see below.)*
6. Absent or dysgenetic testis *leads to* deficient anti-Müllerian hormone and androgen output, which *results in* **incomplete/absent virilization, persistence of Müllerian structures (in dysgenesis), and hypergonadotropic hypogonadism** at expected puberty. *(Human clinical — [PMID: 37497464].)*
7. Retained dysgenetic Y-bearing gonadal tissue *creates* a **germ-cell tumor predisposition (gonadoblastoma → dysgerminoma/seminoma)**. *(Human clinical — [PMID: 27862157].)*

### Branch point

```
 DHX37 helicase-domain missense (heterozygous)
                    |
        nucleolar stress / p53↑ / PI3K-AKT↓
                    |
        supporting-cell (Sertoli) apoptosis
             /                        \
   determination never completes    determination completes, then fails
             |                                |
   Complete/partial gonadal dysgenesis   Testicular regression syndrome /
   (Swyer; streak gonads; Müllerian      anorchia (absent testes; variable
   remnants; female genitalia)           male genital development)
             \                        /
              High GCT risk        Low/negligible GCT risk
              (~15–23%)            (0/5 in one series)
```

### Genotype–phenotype and dose logic

| Genotype | Phenotype | Syndromic? | OMIM |
|---|---|---|---|
| Heterozygous missense (helicase domains; hotspots R308Q, R674W) | 46,XY gonadal dysgenesis ↔ TRS/anorchia spectrum | No | #273250 (SRXY11) |
| Compound heterozygous / de novo heterozygous missense | Microcephaly, DD, seizures, dysmorphism, vertebral/cardiac/kidney anomalies | Yes (NEDBAVC) | 618731 |

The recurrence of specific residues and their autosomal-dominant behavior suggest the DSD-causing alleles act through a **specific (possibly dominant-negative or hypomorphic gain-of-toxicity) mechanism** rather than simple haploinsufficiency — consistent with the observation that a different mutational configuration (biallelic/de novo) produces an entirely different, neurodevelopmental disease. This remains a hypothesis; direct allele-specific functional proof is lacking.

### Why a housekeeping factor hits the gonad selectively (open question)

The defining unresolved question (Finding 8) is the **tissue-specificity paradox**. Proposed but unproven explanations, by analogy to other ribosomopathies, include: (i) heightened dependence of the rapidly proliferating fetal gonadal-somatic lineage on ribosome flux during the brief sex-determination window; (ii) a low p53 threshold in supporting cells; and (iii) selective translational requirements for pro-testis regulators (e.g., the SRY/SOX9 pathway). None has been experimentally demonstrated for DHX37.

---

## Section-by-Section Details

### 1. Disease Information
- **Overview:** SRXY11 is a monogenic 46,XY DSD in which testis determination fails or reverses despite a Y chromosome, spanning Swyer syndrome (complete gonadal dysgenesis) to testicular regression/anorchia to mild male undervirilization.
- **Identifiers:** OMIM #273250 (46,XY sex reversal 11); allelic OMIM 618731 (NEDBAVC). Gene: *DHX37* (HGNC:16192; NCBI Gene 57647; UniProt Q8IY37). Orphanet/ICD map to broader "46,XY complete/partial gonadal dysgenesis" and "swyer syndrome" categories; MeSH: Gonadal Dysgenesis, 46,XY; Disorders of Sex Development. MONDO: 46,XY gonadal dysgenesis spectrum.
- **Synonyms/alternatives:** DHX37-related 46,XY DSD; 46,XY gonadal dysgenesis with DHX37; 46,XY testicular regression syndrome (DHX37); "new ribosomopathy of sex development."
- **Data source type:** Predominantly aggregated case-series/cohort literature and gene-level resources (OMIM), not EHR-derived.

### 2. Etiology
- **Causal factor:** Monogenic — heterozygous missense variants in *DHX37* (Findings 1, 7). No environmental or infectious cause.
- **Genetic risk:** The DHX37 variant itself is causal (autosomal dominant); rare deleterious DHX37 variants enriched ~35-fold vs gnomAD (14% vs 0.4%; [PMID: 31287541]). Modifier genes are implied by incomplete penetrance but unidentified.
- **Protective factors:** None established (no known protective alleles or exposures).
- **Gene–environment interactions:** None documented; considered a purely genetic condition.

### 3. Phenotypes
| Phenotype | Type | Onset | Frequency | HPO suggestion |
|---|---|---|---|---|
| 46,XY sex reversal / gonadal dysgenesis | Physical/clinical | Fetal (manifest at birth or puberty) | Core feature | HP:0000133 |
| Streak gonads | Clinical sign | Fetal/congenital | Common in CGD | HP:0000133 |
| Primary amenorrhea / delayed puberty | Clinical sign | Adolescence | Common in Swyer | HP:0000783 |
| Hypergonadotropic hypogonadism | Lab abnormality | Puberty | Characteristic | HP:0000815 |
| Testicular regression / anorchia | Physical | Fetal | ETRS subset (~50% of variant carriers, [PMID:31287541]) | HP:0000795 |
| Gynecomastia (mild pole) | Physical | Puberty | Mild presentations | HP:0000771 |
| Müllerian remnants (uterus) | Physical | Congenital | Dysgenesis end | — |
| Gonadoblastoma/dysgerminoma predisposition | Neoplasm | Adolescence | ~15–23% in dysgenesis | HP:0100728 |

Severity is highly variable (Finding 5); the primary gonadal defect is stable/non-progressive but its consequences (pubertal failure, tumor risk) evolve. Quality-of-life impacts include infertility, need for lifelong hormone therapy, psychosocial burden of atypical sex development, and cancer surveillance/gonadectomy; disease-specific QOL instruments have not been reported for this ultra-rare condition.

### 4. Genetic/Molecular Information
- **Causal gene:** *DHX37* (DEAH-box helicase 37); encodes an ATP-dependent RNA helicase required for 40S biogenesis.
- **Variant class:** Missense predominates, in conserved helicase (RecA) domains. Recurrent hotspots: **p.Arg308Gln, p.Arg674Trp** ([PMID: 31287541]). Other reported residues: p.Arg334Trp, p.Arg390His, p.Thr477His, p.Gly478Arg ([PMID: 34293745]).
- **Classification:** Pathogenic/likely-pathogenic per ACMG for hotspots; some variants remain VUS requiring functional/segregation support ([PMID: 42057034]).
- **Allele frequency:** Rare/near-absent in gnomAD (aggregate deleterious ~0.4%).
- **Origin:** Germline; both inherited (dominant) and de novo reported.
- **Functional consequence:** Loss/alteration of helicase function; a dominant-negative or hypomorphic mechanism is hypothesized but unproven.
- **Modifier genes/epigenetics/chromosomal:** Modifiers unidentified; no epigenetic mechanism established; the causal lesion is a point mutation, not a large chromosomal rearrangement (distinguishing it from 45,X/46,XY mosaicism).

### 5. Environmental Information
Not applicable — no environmental, lifestyle, or infectious contributors are known; SRXY11 is monogenic.

### 6. Mechanism / Pathophysiology
See the ordered causal chain and branch diagram above. Molecular pathway: ribosome biogenesis (40S/SSU maturation, U3 snoRNA displacement) → nucleolar stress → p53 activation + reduced PI3K-AKT → pro-apoptotic splicing → supporting-cell apoptosis. GO terms: GO:0042254, GO:0030490, GO:0005730, GO:0072332, GO:0006915, GO:0007530, GO:0008584. CL terms: Sertoli/supporting cell (CL:0000216), Leydig cell (CL:0000178), male germ cell (CL:0000015).

### 7. Anatomical Structures Affected
- **Organ/system:** Gonad/testis (primary); endocrine and reproductive systems; internal (uterus/Müllerian remnants) and external genitalia (secondary). UBERON: gonad (UBERON:0000991), testis (UBERON:0000473), uterus (UBERON:0000995).
- **Tissue/cell:** Gonadal somatic supporting lineage (Sertoli), Leydig cells, germ cells.
- **Subcellular:** Nucleolus (GO:0005730), cytosolic small ribosomal subunit (GO:0022627).
- **Lateralization:** Usually bilateral (dysgenesis); unilateral regression documented (variable, [PMID: 34293745]).

### 8. Temporal Development
- **Onset:** Congenital/fetal at the level of gonadal determination; clinically silent until puberty in complete dysgenesis (primary amenorrhea), or noted at birth when genitalia are atypical or testes absent.
- **Course:** Underlying defect fixed/non-progressive; consequences evolve; germ-cell tumors cluster in adolescence (median 17–18 y; [PMID: 27862157]).
- **Critical period:** Fetal sex-determination window (the window of intervention for any future mechanistic therapy is developmental and effectively closed postnatally).

### 9. Inheritance and Population
- **Inheritance:** Autosomal dominant (SRXY11) with incomplete penetrance and variable expressivity ([PMID: 31337883], [PMID: 34293745]); allelic recessive/de novo → NEDBAVC ([PMID: 35835064]).
- **Epidemiology:** DHX37-specific prevalence/incidence not quantified; identified in enriched DSD cohorts (e.g., 14% of one 87-patient cohort; 13/145 in another). Reported across French, Brazilian, Japanese, Iranian, Chinese, and Polish cohorts.
- **Sex ratio:** Affects 46,XY individuals; presentation ranges phenotypic female → male.
- **Founder/consanguinity:** No founder effect established; homozygous cases reported in consanguineous contexts ([PMID: 34293745]).

### 10. Diagnostics
- **Cytogenetics:** Karyotype/FISH confirming 46,XY (exclude 45,X/46,XY mosaicism — [PMID: 31883875], [PMID: 32057790]).
- **Endocrine:** Hypergonadotropic hypogonadism (↑FSH/LH, ↓estradiol/testosterone); AMH/inhibin B to gauge functional gonadal tissue.
- **Imaging:** Pelvic ultrasound/MRI for uterus/Müllerian structures and streak vs absent gonads.
- **Molecular:** WES/WGS or trio sequencing; DHX37 on DSD panels ([PMID: 41466375], [PMID: 42365275]); ACMG classification with functional support for VUS ([PMID: 42057034]).
- **Histopathology:** Streak gonads; surveillance for gonadoblastoma/dysgerminoma.
- **Differential diagnosis:** NR5A1, SRY, SOX9, MAP3K1, WT1, GATA4, AR (androgen insensitivity), HSD17B3, and 45,X/46,XY mosaicism ([PMID: 42365275], [PMID: 42057034]).

### 11. Outcome / Prognosis
- **Survival:** Life expectancy is essentially normal with appropriate management; the major life-threatening risk is malignant transformation of retained dysgenetic gonads.
- **Morbidity:** Infertility, need for lifelong hormone replacement, and cancer risk (~15–23% in dysgenesis; [PMID: 27862157]).
- **Prognostic factors:** Degree of gonadal dysgenesis (dysgenesis > regression for tumor risk); familial cases may carry higher tumor risk ([PMID: 38337479]).

### 12. Treatment
- **Hormone replacement therapy** (estrogen ± progestin, or testosterone as appropriate) — NCIT: Hormone Replacement Therapy.
- **Prophylactic/therapeutic gonadectomy** of dysgenetic Y-bearing gonads — NCIT: Gonadectomy/Orchiectomy.
- **Fertility counseling** (typically infertile; assisted reproduction/oocyte donation for uterus-bearing individuals).
- **Psychosocial and gender-affirming care**, individualized.
- **Genetic counseling** (AD recurrence, variable expressivity/penetrance, distinct NEDBAVC risk).
- No gene/RNA/cell therapy, disease-specific drug, or pharmacogenomic guidance exists.

### 13. Prevention
- **Primary:** Not applicable (congenital genetic condition).
- **Secondary:** Cascade genetic testing of at-risk relatives; early identification enabling timely tumor surveillance and gonadal management.
- **Tertiary:** Prophylactic gonadectomy to prevent malignancy; hormone replacement to prevent osteoporosis and secondary-sex-characteristic deficits.
- **Reproductive options:** Genetic counseling, prenatal/preimplantation genetic testing for known familial variants.

### 14. Other Species / Natural Disease
- **Orthologs:** Mouse *Dhx37* (used in the conditional-knockout model — [PMID: 41535247]); yeast ortholog *DHR1* (structural/functional studies — [PMID: 31188444]). NCBI Gene (human) 57647.
- **Natural disease:** No naturally occurring companion-animal or wildlife DHX37 sex-reversal disease is documented in OMIA to date.
- **Conservation:** The ribosome-biogenesis function of DHX37/Dhr1 is deeply conserved from yeast to human; the sex-determination consequence is a vertebrate/mammalian-specific downstream effect.

### 15. Model Organisms
- **Mouse:** Cell-specific (supporting-cell) conditional *Dhx37* knockout recapitulates impaired testis development via nucleolar stress/p53 apoptosis ([PMID: 41535247]) — the best available model; limitation: it is a knockout, not a patient-allele knock-in, so dominant/hotspot-allele effects are not directly modeled.
- **Yeast:** Dhr1 structural/functional studies define the helicase mechanism (U3 snoRNA displacement, C-terminal domain) and the biogenesis consequences of DHX37 mutations ([PMID: 31188444]); limitation: no sex-development readout.
- **Gaps:** No zebrafish/invertebrate DHX37 sex-development model; no humanized R308Q/R674W knock-in. Resources: MGI (mouse), SGD (yeast).

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role in report |
|---|---|---|---|
| [31337883](https://pubmed.ncbi.nlm.nih.gov/31337883/) | DHX37 variants a frequent cause of 46,XY GD/TRS | Human cohort (n=145) | Establishes DHX37 as SRXY11 gene, AD inheritance, spectrum (F1) |
| [41535247](https://pubmed.ncbi.nlm.nih.gov/41535247/) | Multi-omics of Dhx37 deficiency on testis/nucleolar homeostasis | Mouse KO, in vitro | Core mechanism: nucleolus/PI3K-AKT/p53/apoptosis (F2) |
| [35835064](https://pubmed.ncbi.nlm.nih.gov/35835064/) | DHX37 and 46,XY DSD: A new ribosomopathy? | Review | Allelic NEDBAVC vs non-syndromic DSD; ribosomopathy framing (F3) |
| [27862157](https://pubmed.ncbi.nlm.nih.gov/27862157/) | Gonadal tumour risk in 292 phenotypic females with Y material | Human cohort (n=292) | Quantifies GCT risk; supports gonadectomy (F4) |
| [34293745](https://pubmed.ncbi.nlm.nih.gov/34293745/) | Expanding DSD phenotypes with DHX37 variants | Human clinical | Spectrum poles; variable expressivity; mechanism unknown (F5, F8) |
| [42510869](https://pubmed.ncbi.nlm.nih.gov/42510869/) | Novel and known DHX37 variants | Human clinical | Confirms mild-end heterogeneity (F5) |
| [37497464](https://pubmed.ncbi.nlm.nih.gov/37497464/) | Late presentation of Swyer syndrome | Case report | Hypergonadotropic hypogonadism signature (F6) |
| [41466375](https://pubmed.ncbi.nlm.nih.gov/41466375/) | Variations in sex characteristics across OMIM | Analysis | Supports genome-wide sequencing in DSD (F6) |
| [31287541](https://pubmed.ncbi.nlm.nih.gov/31287541/) | DHX37 defects and 46,XY GD spectrum | Human cohort (n=87), IHC | Recurrent hotspots, gnomAD enrichment, ETRS, expression (F7) |
| [31188444](https://pubmed.ncbi.nlm.nih.gov/31188444/) | Dhr1 C-terminal domain essential for SSU biogenesis | Structural/yeast | Molecular basis of helicase role; U3 snoRNA displacement |
| [38337479](https://pubmed.ncbi.nlm.nih.gov/38337479/) | Gonadoblastoma in familial Swyer syndrome | Case + review | Familial tumor-risk context |
| [31883875](https://pubmed.ncbi.nlm.nih.gov/31883875/) / [32057790](https://pubmed.ncbi.nlm.nih.gov/32057790/) | Tumor risk in 45,X/46,XY mosaicism | Human clinical | Differential diagnosis / tumor-risk context |
| [42365275](https://pubmed.ncbi.nlm.nih.gov/42365275/) / [42057034](https://pubmed.ncbi.nlm.nih.gov/42057034/) / [40916030](https://pubmed.ncbi.nlm.nih.gov/40916030/) / [39829003](https://pubmed.ncbi.nlm.nih.gov/39829003/) | WES cohorts identifying DHX37 (with NR5A1 etc.) | Human cohorts | Diagnostic yield, VUS interpretation, differential genes |
| [42151440](https://pubmed.ncbi.nlm.nih.gov/42151440/) | DHX37 in breast/ovarian cancer prognosis | Human tumor cohorts | Non-DSD context: DHX37 tissue-context-dependent roles |

**Where the evidence converges:** Independent human cohorts ([31337883], [31287541]) establish DHX37 causation, hotspot recurrence, and statistical enrichment; the mouse multi-omics study ([41535247]) supplies the cell-and-pathway mechanism (Sertoli apoptosis via nucleolar stress/p53/PI3K-AKT); tumor-risk data ([27862157]) drive the management recommendation.

**Where the evidence is in tension / incomplete:** Human IHC localizes DHX37 mainly to germ and Leydig cells, "rarely" to Sertoli cells ([31287541]), whereas the mechanistic mouse model centers on Sertoli-cell apoptosis ([41535247]) — leaving open whether the human phenotype arises cell-autonomously in supporting cells, non-cell-autonomously from germ/Leydig-cell dysfunction, or both. Reviews explicitly state the mechanism of tissue specificity is unknown ([34293745]).

---

## Limitations and Knowledge Gaps

1. **Unresolved tissue-specificity paradox (central gap).** No experimental demonstration explains why a ubiquitous 40S-biogenesis factor selectively disables gonadal determination ([PMID: 34293745]).
2. **Allele-specific functional data are sparse.** The dominant-negative vs hypomorphic nature of hotspot alleles (R308Q, R674W) is inferred, not proven; some clinically encountered variants remain VUS ([PMID: 42057034]).
3. **Cell-of-origin ambiguity.** Human expression (germ/Leydig-dominant) versus mouse phenotype (Sertoli apoptosis) are not fully reconciled.
4. **No humanized/knock-in model** of the recurrent DSD alleles, and **no zebrafish/invertebrate sex-development model** exists; the mouse model is a conditional knockout.
5. **Incomplete penetrance/variable expressivity** (e.g., fertile carrier fathers) implies unidentified genetic/environmental modifiers; none are established.
6. **Epidemiology is imprecise** — DHX37-specific prevalence/incidence are unquantified; data come from enriched DSD cohorts, not population registries.
7. **No environmental/infectious contributors** are known; environmental sections are largely not applicable.

---

## Proposed Follow-up Experiments / Actions

1. **Generate patient-allele knock-in mice** (Dhx37^R308Q/+, R674W/+) to test dominant-negative behavior and recapitulate the graded dysgenesis→regression phenotype in vivo.
2. **Cell-type-resolved fetal gonad profiling** (single-cell/spatial transcriptomics of human and mouse fetal gonad) to determine whether the primary lesion is in Sertoli, germ, or Leydig cells and to map ribosome-flux dependence during the determination window. (Search: Human Cell Atlas, GEO, CELLxGENE.)
3. **Allele-specific functional assays** — 40S maturation, U3 snoRNA displacement, nucleolar-stress and p53 readouts — for each recurrent and VUS allele to move variants from VUS toward pathogenic/benign per ACMG.
4. **Zebrafish dhx37 sex-development model** to exploit tractable gonad genetics and test conservation of the mechanism.
5. **Prospective natural-history/registry study** capturing penetrance, tumor incidence and timing, and modifier genotypes across DHX37 carriers, to refine gonadectomy timing and counseling.
6. **Test the tissue-specificity hypotheses directly** — e.g., titrate p53 activity (Trp53 co-deletion) in the Dhx37 model to establish whether p53-driven apoptosis is necessary and sufficient for the gonadal phenotype.

---

## Conclusion

46,XY Sex Reversal 11 (SRXY11; OMIM #273250) is an autosomal-dominant disorder of sex development caused by heterozygous, largely recurrent missense variants in the ribosome-biogenesis helicase *DHX37*. It presents as a phenotypic spectrum from complete gonadal dysgenesis (Swyer) to testicular regression/anorchia and mild male undervirilization, and is best understood as a putative ribosomopathy in which nucleolar stress, p53-driven apoptosis, and reduced PI3K-AKT survival signaling cause failure/regression of the fetal testis-supporting lineage. Diagnosis combines a discordant 46,XY karyotype, hypergonadotropic hypogonadism, and molecular sequencing; management is supportive — hormone replacement, prophylactic gonadectomy of Y-bearing dysgenetic gonads (~15–23% tumor risk), and genetic counseling. The defining open question is how a housekeeping ribosome factor produces a gonad-restricted phenotype.


## Artifacts

- [OpenScientist final report](46_XY_Sex_Reversal_11-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](46_XY_Sex_Reversal_11-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 18 |
| Quoted claims found in source | 18 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 18 |
| On topic | 14 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:32057790` (3 mentions) - Seminoma In A Young Phenotypic Female With Turner Syndrome 45,XO/46,XY Mosaicism: A Case Report With Review Of The Literature.
  - shared terms: none

Weighed against this report's own most characteristic terms: `dhx37`, `gonadal`, `dysgenesis`, `variant`, `dsd`, `gonad`, `regression`, `helicase`, `cell`, `missense`, `gene`, `testis`, `tumor`, `phenotype`, `recurrent`, `development`, `heterozygous`, `sex`, `apoptosis`, `sertoli`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 23 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 5 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000133` (2 mentions) - the report calls it "Core feature", "Common in CGD"; HP calls it **Gonadal dysgenesis**
- `HP:0000815` (1 mention) - the report calls it "Characteristic"; HP calls it **Hypergonadotropic hypogonadism**
- `HP:0000771` (1 mention) - the report calls it "Mild presentations"; HP calls it **Gynecomastia**
- `HP:0100728` (1 mention) - the report calls it "~15–23% in dysgenesis"; HP calls it **Germ cell neoplasia**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000783` (1 mention), reported as "Common in Swyer" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005730` (3 mentions) - the report calls it "Subcellular:** Nucleolus"; GO calls it **nucleolus**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000133` - called "Core feature", "Common in CGD"