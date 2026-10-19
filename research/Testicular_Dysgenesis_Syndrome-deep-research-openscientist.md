---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-18T21:43:18.807230'
end_time: '2026-10-18T21:59:58.374959'
duration_seconds: 999.57
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Testicular Dysgenesis Syndrome
  mondo_id: MONDO:0005437
  category: Complex
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
citation_count: 46
reference_validation:
  total_references: 48
  verified: 48
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 48
  on_topic: 21
  off_topic: 2
  off_topic_references:
  - PMID:28981654
  - PMID:36377604
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 31
  verified: 30
  not_found: 1
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.032
  labels_checked: 13
  labels_matching: 4
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0005437
    reported_labels:
    - MONDO
    ontology_label: testicular dysgenesis syndrome
  - term_id: HP:0000028
    reported_labels:
    - "~1\u20139% of full-term male infants; uni/bilateral"
    ontology_label: Cryptorchidism
  - term_id: HP:0000047
    reported_labels:
    - Variable
    ontology_label: Hypospadias
  - term_id: HP:0010788
    reported_labels:
    - "Most common malignancy in men 15\u201345"
    ontology_label: Testicular neoplasm
  - term_id: HP:0008720
    reported_labels:
    - Variable
    ontology_label: Primary testicular failure
  - term_id: HP:0000062
    reported_labels:
    - Rare, severe subset
    ontology_label: Ambiguous genitalia
  labels_variant: 3
  unresolved_terms:
  - CHEBI:41448
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Testicular_Dysgenesis_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Testicular_Dysgenesis_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Testicular Dysgenesis Syndrome
- **MONDO ID:** MONDO:0005437 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Testicular Dysgenesis Syndrome** covering all of the
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

# Testicular Dysgenesis Syndrome (TDS) — Comprehensive Disease Characterization

**Target disease:** Testicular Dysgenesis Syndrome
**MONDO ID:** MONDO:0005437
**Category:** Complex / multifactorial developmental syndrome
**Report type:** Disease knowledge-base characterization across 15 domains
**Investigation:** 5 iterations · 12 confirmed findings · 57 papers reviewed
*Evidence base: human clinical/epidemiological studies, rodent model-organism experiments, in-vitro/xenograft studies.*

---

## Summary

**Testicular Dysgenesis Syndrome (TDS)** is a unifying developmental hypothesis, first articulated by Skakkebaek and colleagues, proposing that four common male reproductive disorders — **cryptorchidism** (undescended testis), **hypospadias**, **impaired spermatogenesis / poor semen quality**, and **testicular germ-cell cancer (TGCT)** — are not independent conditions but four downstream manifestations of a single underlying entity: **disturbed fetal testicular development**, specifically dysfunction of the somatic Sertoli and Leydig cell lineages ([PMID: 14671395](https://pubmed.ncbi.nlm.nih.gov/14671395/)). These disorders are mutual risk factors, share risk factors (low birth weight, small-for-gestational-age), and co-vary geographically (high in Denmark, low in Finland), supporting a common origin.

The central mechanistic insight established across this investigation is that TDS originates during the **masculinization programming window (MPW)** — roughly gestational weeks 8–14 in humans (embryonic days 15.5–18.5 in the rat) — a critical period during which fetal androgen (testosterone) and INSL3 action program male reproductive-tract development. Deficient androgen action during the MPW, whether caused by **genetic lesions** (NR5A1/SF-1, INSL3/RXFP2, 45,X/46,XY mosaicism, and polygenic TGCT-risk loci such as KITLG, DMRT1, SPRY4, TERT and BAK1) or **anti-androgenic environmental exposures** (phthalate plasticizers, prenatal analgesics/paracetamol) acting on a genetically susceptible background, produces the full TDS phenotype. Reduced **anogenital distance (AGD)** is a validated non-invasive biomarker of this fetal androgen deficit and correlates with the risk and severity of all TDS disorders.

TDS spans a **severity continuum**: from common, mild subfertility at one end, through isolated cryptorchidism/hypospadias, to severe 46,XY gonadal dysgenesis and the most severe form, 45,X/46,XY mixed gonadal dysgenesis, at the other. The **cancer arm** is itself a developmental disease — adult TGCTs arise from a pre-invasive precursor, **germ cell neoplasia in situ (GCNIS)**, derived from arrested fetal gonocytes that retain embryonic pluripotency (OCT4, NANOG, AP-2γ, LIN28, PLAP). Management is **component-specific**: there is no treatment for "TDS" as a unit. Notably, the TGCT component is highly curable (orchiectomy alone cures ~80% of stage I disease), while the fertility and endocrine deficits are largely irreversible. Rising secular trends in TGCT incidence and declining sperm counts worldwide have been interpreted as evidence of a growing environmental contribution to male reproductive health.

---

## 1. Disease Information

**Overview.** TDS is a constellation / developmental syndrome uniting cryptorchidism, hypospadias, impaired spermatogenesis (poor semen quality), and testicular germ-cell cancer as shared manifestations of disturbed prenatal testicular development ([PMID: 14671395](https://pubmed.ncbi.nlm.nih.gov/14671395/); [PMID: 16522521](https://pubmed.ncbi.nlm.nih.gov/16522521/)). The TDS hypothesis is grounded in epidemiological, clinical, and molecular studies all suggesting that these conditions are interrelated. The most severe form occurs in individuals with 45,X0/46,XY karyotype (mixed gonadal dysgenesis), who present with an intersex phenotype, testicular dysgenesis, undescended testes, hypospadias, severely disrupted spermatogenesis, and high testicular cancer risk ([PMID: 16005920](https://pubmed.ncbi.nlm.nih.gov/16005920/)).

> *"There is evidence that poor semen quality, testicular cancer, undescended testes and hypospadias are symptoms of one underlying entity, testicular dysgenesis syndrome (TDS), which may be increasingly common due to adverse environmental influences."* — [PMID: 14671395](https://pubmed.ncbi.nlm.nih.gov/14671395/)

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0005437 |
| MeSH | Indexed under gonadal/urogenital dysgenesis concepts; component disorders have dedicated MeSH (Cryptorchidism, Hypospadias, Testicular Neoplasms, Oligospermia/Azoospermia) |
| ICD-10 | Q53 (undescended testicle), Q54 (hypospadias), C62 (malignant neoplasm of testis), N46 (male infertility), Q56 (indeterminate sex) |
| OMIM | No single OMIM entry for TDS as a syndrome; monogenic contributors include NR5A1 (184757), INSL3 (146738), RXFP2 (606655) |

**Synonyms / alternative names.** Testicular dysgenesis syndrome; TDS; dysgenetic testis syndrome. Component-focused terms: disorders/differences of sex development (DSD) at the severe end.

**Information source type.** The TDS entity derives predominantly from **aggregated disease-level resources** — epidemiological cohorts, animal models, and molecular/clinical reviews — rather than a single individual-patient registry. Individual-patient data inform the monogenic (DSD) extreme and biomarker studies.

---

## 2. Etiology

**Primary causal factors.** TDS is **multifactorial**, arising from an interaction of genetic and environmental (particularly endocrine-disrupting) factors that converge on deficient fetal androgen action. "The aetiology of TDS is suspected to be related to genetic and/or environmental factors, including endocrine disrupters" ([PMID: 16522521](https://pubmed.ncbi.nlm.nih.gov/16522521/)).

**Genetic risk factors.**
- **Monogenic (severe end):** NR5A1/SF-1 (broad 46,XY DSD spectrum — 188 mutations across 238 cases), INSL3 and RXFP2 (cryptorchidism), sex-chromosome mosaicism (45,X/46,XY) ([PMID: 31513305](https://pubmed.ncbi.nlm.nih.gov/31513305/); [PMID: 41369823](https://pubmed.ncbi.nlm.nih.gov/41369823/); [PMID: 16005920](https://pubmed.ncbi.nlm.nih.gov/16005920/)).
- **Polygenic (cancer arm):** >25 risk SNPs at ~19 loci for TGCT, with per-allele odds ratios among the highest reported for any cancer. Strongest: **KITLG** (P=2.1×10⁻⁴⁸), **SPRY4** (1.4×10⁻²⁹), **DMRT1** (6.7×10⁻²⁵), **TERT** (1.8×10⁻¹⁸), **BAK1** (2.1×10⁻¹⁰) ([PMID: 25598472](https://pubmed.ncbi.nlm.nih.gov/25598472/); [PMID: 23640991](https://pubmed.ncbi.nlm.nih.gov/23640991/)).

**Environmental risk factors.** Anti-androgenic endocrine-disrupting chemicals — most prominently **phthalate plasticizers** (DBP, DEHP, DINP) — and **mild analgesics** (paracetamol/acetaminophen, aspirin) taken during pregnancy. Other recognized risk factors include low birth weight and small-for-gestational-age status.

**Protective factors.** No established genetic protective variants are specifically documented for TDS. By mechanistic logic, avoidance of anti-androgenic exposures during the MPW is protective; the oxidative-stress component of phthalate injury is partly rescued by the antioxidant flavonoid **taxifolin** in a rat model ([PMID: 36198370](https://pubmed.ncbi.nlm.nih.gov/36198370/)), suggesting antioxidant status may be modifying — but human protective-factor data are lacking.

**Gene–environment interactions.** The canonical model is that environmental anti-androgens act on a **genetically susceptible** background. A concrete demonstration: maternal mild-analgesic use was dose-dependently associated with cryptorchidism in the Danish but **not** the Finnish arm of a birth cohort ([PMID: 21059752](https://pubmed.ncbi.nlm.nih.gov/21059752/)). In vitro, inactivating PDE11A variants interact with KITLG risk alleles to elevate familial TGCT risk via cAMP/c-KIT signaling ([PMID: 23771924](https://pubmed.ncbi.nlm.nih.gov/23771924/)).

---

## 3. Phenotypes

TDS comprises four core phenotypes plus endocrine/biomarker abnormalities:

| Phenotype | Type | Onset | Frequency / severity | Suggested HPO |
|---|---|---|---|---|
| Cryptorchidism (undescended testis) | Physical malformation | Congenital (neonatal) | ~1–9% of full-term male infants; uni/bilateral | HP:0000028 |
| Hypospadias | Physical malformation | Congenital | Variable | HP:0000047 |
| Impaired spermatogenesis / poor semen quality | Laboratory abnormality | Post-puberty/adulthood | Most common manifestation; severity variable | HP:0000798 (oligospermia) |
| Testicular germ-cell tumour (seminoma/nonseminoma) | Neoplasm | Young adult (peak 30–40 y) | Most common malignancy in men 15–45 | HP:0010788 |
| Reduced anogenital distance | Physical sign / biomarker | Congenital | Correlates with severity | — |
| Compensated Leydig-cell failure (low T / high LH) | Laboratory abnormality | Adult | Variable | HP:0008720 |
| Ambiguous genitalia / DSD (severe end) | Physical | Congenital | Rare, severe subset | HP:0000062 |

**Characteristics.** Onset of structural components (cryptorchidism, hypospadias) is **congenital**; fertility and cancer components become clinically apparent **post-pubertally / in young adulthood**. Severity is **highly variable** along a continuum. Progression is generally **stable** for the structural malformations (surgically correctable) but the cancer component is progressive if untreated.

**Quality-of-life impact.** Infertility/subfertility carries psychosocial burden and need for assisted reproduction; TGCT diagnosis in young men has major QoL impact but excellent survival; DSD at the severe end has profound impact on gender, surgical, and psychological care. Per-phenotype validated QoL-instrument (EQ-5D/SF-36) data specific to TDS were not identified.

---

## 4. Genetic / Molecular Information

**Causal genes (severe/monogenic end).**
- **NR5A1 (SF-1; OMIM 184757):** essential transcription factor for adrenal/gonadal development and steroidogenesis. 188 mutations across 238 cases span the 46,XY DSD spectrum from severe gonadal dysgenesis to isolated infertility; phenotype includes hypospadias, micropenis, undescended gonads, low AMH/testosterone ([PMID: 31513305](https://pubmed.ncbi.nlm.nih.gov/31513305/); [PMID: 37409232](https://pubmed.ncbi.nlm.nih.gov/37409232/)).

> *"Anti-Müllerian hormone (AMH) and testosterone levels were low, indicating testicular dysgenesis."* — [PMID: 37409232](https://pubmed.ncbi.nlm.nih.gov/37409232/)

- **INSL3 (OMIM 146738) and RXFP2 (OMIM 606655):** control the trans-abdominal phase of testicular descent. Novel homozygous INSL3 frameshift variants (NM_005543: c.176_182del, p.Ala59GlufsTer66; c.148dupC, p.Arg50ProfsTer16) and recessive RXFP2 variants cause familial bilateral cryptorchidism ([PMID: 41369823](https://pubmed.ncbi.nlm.nih.gov/41369823/); [PMID: 31167797](https://pubmed.ncbi.nlm.nih.gov/31167797/)).

**Pathogenic variants — cancer-susceptibility (polygenic).** Common low-penetrance variants near **KITLG, SPRY4, DMRT1, TERT-CLPTM1L, BAK1, ATF7IP** predispose to TGCT (predominantly regulatory/intronic SNPs). Replicated in familial and bilateral TGCT: BAK1 rs210138 (OR 1.80), DMRT1 rs755383 (OR 1.67), TERT-CLPTM1L rs4635969 (OR 1.59), KITLG rs2046971 (OR 2.33) ([PMID: 21617256](https://pubmed.ncbi.nlm.nih.gov/21617256/)). Pediatric and adult germ-cell tumors share overlapping etiology (BAK1, SPRY4, DMRT1, DEPTOR; 18/78 adult loci significant) ([PMID: 41941753](https://pubmed.ncbi.nlm.nih.gov/41941753/)).

**Functional consequences.** NR5A1 and INSL3/RXFP2 variants are **loss-of-function**. The RXFP2 D294G missense (mouse ENU model) reduces cell-surface receptor expression via protein misfolding/mistrafficking ([PMID: 20963592](https://pubmed.ncbi.nlm.nih.gov/20963592/)). TGCT risk SNPs act via altered expression (e.g., KITLG/c-KIT signaling).

**Modifier genes.** PDE11A inactivating variants modify familial TGCT risk and interact with KITLG ([PMID: 23771924](https://pubmed.ncbi.nlm.nih.gov/23771924/)). SNP-based susceptibility scores predict pre-GCNIS in androgen-insensitivity syndrome, with KITLG (rs995030) and ATF7IP (rs2900333) prominent ([PMID: 29121256](https://pubmed.ncbi.nlm.nih.gov/29121256/)).

**Epigenetic information.** GCNIS/TGCT cells retain an embryonic/pluripotent program (OCT4/POU5F1, NANOG) normally silenced in adult germ cells; vitamin D/VDR signaling downregulates NANOG/OCT4 in vitro ([PMID: 23097629](https://pubmed.ncbi.nlm.nih.gov/23097629/)). Disease-defining DNA-methylation signatures specific to TDS were not catalogued.

**Chromosomal abnormalities.** 45,X/46,XY mosaicism (mixed gonadal dysgenesis) is the most severe form; isochromosome 12p is the hallmark somatic marker of invasive TGCT.

---

## 5. Environmental Information

**Environmental factors (toxins).** **Phthalate plasticizers** are best-characterized. In rats, in-utero DBP, DEHP, and (more weakly) DINP during the MPW suppress fetal testosterone and cause TDS phenotypes ([PMID: 28352662](https://pubmed.ncbi.nlm.nih.gov/28352662/); [PMID: 36198370](https://pubmed.ncbi.nlm.nih.gov/36198370/); [PMID: 18174951](https://pubmed.ncbi.nlm.nih.gov/18174951/); [PMID: 25445723](https://pubmed.ncbi.nlm.nih.gov/25445723/)). Combined cadmium + DBP exposure worsens fetal testis defects ([PMID: 32497820](https://pubmed.ncbi.nlm.nih.gov/32497820/)). **CHEBI suggestions:** dibutyl phthalate (CHEBI:41448), DEHP (CHEBI:17747), cadmium (CHEBI:22977), paracetamol (CHEBI:46195), testosterone (CHEBI:17347).

**Important species caveat.** Human fetal testis xenografts are **resistant** to phthalate-induced suppression of steroidogenic gene expression, even though they show multinucleated germ-cell induction — demonstrating a **species-specific** sensitivity and a key limitation in extrapolating rat steroidogenic effects to humans ([PMID: 22511013](https://pubmed.ncbi.nlm.nih.gov/22511013/)).

**Lifestyle factors.** Maternal mild-analgesic (paracetamol, aspirin) use during pregnancy is anti-androgenic and associated with cryptorchidism and shorter infant AGD ([PMID: 21059752](https://pubmed.ncbi.nlm.nih.gov/21059752/); [PMID: 27609981](https://pubmed.ncbi.nlm.nih.gov/27609981/)).

**Infectious agents.** Not applicable — TDS is a developmental/endocrine disorder with no infectious etiology.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

```
1. Genetic lesion (NR5A1, INSL3/RXFP2, 45,X/46,XY, polygenic KITLG/DMRT1 etc.)
   AND/OR anti-androgenic exposure (phthalates, paracetamol)
        │  leads to
        ▼
2. Disrupted fetal Leydig-cell steroidogenesis during the Masculinization
   Programming Window (MPW; human GW 8–14 / rat e15.5–e18.5)
   — down-regulation of SCARB1, CYP11A1, HSD3B1, HSD17B3, INSL3
        │  results in
        ▼
3. Deficient fetal testosterone + INSL3 action  ──┐ (branch point)
        │  leads to                                │
        ▼                                          ▼
4a. Somatic (Sertoli/Leydig) dysgenesis:       4b. Impaired INSL3/RXFP2
    focal dysgenetic tubules, Leydig-cell          signaling at gubernaculum
    aggregation, multinucleated gonocytes,         (dysregulated Wnt/β-catenin
    oxidative stress (↑MDA, ↓SOD2/CAT/SIRT1)       & Notch, AR+ cells)
        │                                          │  results in
        ▼                                          ▼
5a. Reduced anogenital distance (AGD) +        5b. Failure of trans-abdominal
    hypospadias + reduced adult testis size +      testicular descent →
    compensated Leydig-cell failure                CRYPTORCHIDISM
        │                                          │
        ▼                                          ▼
6a. Arrest of fetal gonocyte differentiation   6b. Cryptorchid micro-environment
    — gonocytes retain pluripotency                further impairs spermatogenesis
    (OCT4, NANOG, AP-2γ, LIN28, PLAP)              & raises malignancy risk
        │  leads to (post-puberty)
        ▼
7. GERM CELL NEOPLASIA IN SITU (GCNIS) → (after puberty) → INVASIVE
   TESTICULAR GERM-CELL TUMOUR (seminoma / nonseminoma)
   AND impaired spermatogenesis → POOR SEMEN QUALITY / INFERTILITY
```

Steps 2→3 are **demonstrated** experimentally in rat (MPW-restricted causality of DBP; [PMID: 28352662](https://pubmed.ncbi.nlm.nih.gov/28352662/)). The gonocyte-arrest → GCNIS → TGCT progression (steps 6a–7) is strongly supported but the malignant-transformation trigger at puberty remains **inferred** ([PMID: 18184914](https://pubmed.ncbi.nlm.nih.gov/18184914/)).

> *"We show that DBP suppresses fetal testosterone equally during and after the MPW, but only DBP exposure in the MPW causes reduced AGD, focal testicular dysgenesis, and TDS disorders."* — [PMID: 28352662](https://pubmed.ncbi.nlm.nih.gov/28352662/)

### Molecular pathways
- **Steroidogenesis:** SCARB1 → CYP11A1 → HSD3B1 → HSD17B3 cascade producing testosterone; suppressed by phthalates ([PMID: 36198370](https://pubmed.ncbi.nlm.nih.gov/36198370/)).
- **INSL3–RXFP2 / cAMP** signaling at the gubernaculum, feeding into **Wnt/β-catenin and Notch** pathways and androgen-receptor-positive cell maintenance ([PMID: 21147849](https://pubmed.ncbi.nlm.nih.gov/21147849/); [PMID: 21403659](https://pubmed.ncbi.nlm.nih.gov/21403659/)).
- **KIT/KITLG** receptor-tyrosine-kinase signaling, **telomerase (TERT)**, **DNA-damage repair**, and **microtubule assembly** in TGCT susceptibility ([PMID: 25598472](https://pubmed.ncbi.nlm.nih.gov/25598472/)).
- **cAMP/PDE11A** interaction with c-KIT in familial predisposition ([PMID: 23771924](https://pubmed.ncbi.nlm.nih.gov/23771924/)).

### Cellular processes & protein dysfunction
Fetal **Leydig-cell** steroidogenic failure and **Sertoli-cell** dysfunction are the upstream somatic lesions; **gonocyte** maturation arrest is the pivotal germ-cell event. GCNIS cells aberrantly express embryonic pluripotency factors (OCT4/POU5F1, NANOG, AP-2γ/TFAP2C, LIN28, PLAP) not seen in normal adult germ cells ([PMID: 26306513](https://pubmed.ncbi.nlm.nih.gov/26306513/); [PMID: 15982323](https://pubmed.ncbi.nlm.nih.gov/15982323/)).

### Metabolic / oxidative & tissue-damage mechanisms
Phthalate exposure raises testicular malondialdehyde (lipid peroxidation) and lowers antioxidants (SOD2, CAT, SIRT1, PGC1α); antioxidant rescue (taxifolin) mitigates dysgenesis ([PMID: 36198370](https://pubmed.ncbi.nlm.nih.gov/36198370/)). Tissue injury manifests as focal dysgenetic tubules, Leydig-cell aggregation, and multinucleated gonocytes.

### Suggested ontology terms
- **GO (biological process):** male gonad development (GO:0008584), testosterone biosynthetic process (GO:0061370), Leydig cell differentiation (GO:0033327), Sertoli cell development (GO:0060008), male genitalia development (GO:0030539), response to oxidative stress (GO:0006979).
- **GO (cellular component):** mitochondrion (GO:0005739, steroidogenesis), smooth ER (GO:0005790), nucleus (GO:0005634).
- **CL (cell type):** Leydig cell (CL:0000178), Sertoli cell (CL:0000216), male germ cell / gonocyte (CL:0000015), spermatogonium (CL:0000020).

---

## 7. Anatomical Structures Affected

**Organ level.** Primary: **testis** (UBERON:0000473), including seminiferous tubules (UBERON:0001343) and the interstitial Leydig compartment. Secondary/associated: **gubernaculum** (descent), **penis/urethra** (UBERON:0000989 / UBERON:0000057; hypospadias), **scrotum** (UBERON:0001300). Body system: **male reproductive / endocrine system** (UBERON:0000079).

**Tissue & cell level.** Affected cells: **Sertoli cells** (CL:0000216), **Leydig cells** (CL:0000178), **fetal gonocytes / germ cells** (CL:0000015) giving rise to GCNIS. Gubernacular smooth-muscle/mesenchyme and androgen-receptor-positive cells participate in descent ([PMID: 21147849](https://pubmed.ncbi.nlm.nih.gov/21147849/)).

**Subcellular level.** Mitochondria and smooth ER of fetal Leydig cells (steroidogenic machinery); nuclear transcription-factor dysfunction (NR5A1, OCT4/NANOG).

**Localization / lateralization.** Cryptorchidism may be **unilateral or bilateral**; dysgenetic changes are often **focal** within the testis ([PMID: 28352662](https://pubmed.ncbi.nlm.nih.gov/28352662/)). GCNIS may be unifocal or multifocal.

---

## 8. Temporal Development

**Onset.** The developmental lesion is **congenital / fetal** (MPW, GW 8–14). Structural components present at birth. Fertility and cancer components become clinically evident **post-pubertally** — TGCT peaks in young adulthood (median diagnosis ~37.7 years; incidence highest ages 30–40) ([PMID: 36874603](https://pubmed.ncbi.nlm.nih.gov/36874603/)).

**Progression.** Structural malformations are **stable** and surgically correctable. The cancer arm follows a stepwise **progressive** course: arrested gonocyte → GCNIS (pre-invasive) → invasive TGCT after puberty. Fertility deficits are typically **chronic/lifelong**.

**Critical periods.** The **MPW (GW 8–14)** is the key window of vulnerability; after this window the same exposure suppresses testosterone but does **not** cause TDS phenotypes ([PMID: 28352662](https://pubmed.ncbi.nlm.nih.gov/28352662/)). Puberty is the critical window for malignant transformation of GCNIS. The window of opportunity for intervention is **orchidopexy at 6–18 months** to preserve spermatogonia ([PMID: 33551366](https://pubmed.ncbi.nlm.nih.gov/33551366/); [PMID: 42194159](https://pubmed.ncbi.nlm.nih.gov/42194159/)).

---

## 9. Inheritance and Population

**Epidemiology.** Cryptorchidism affects ~**1–9%** of full-term male infants (2–4% overall; higher in prematurity) ([PMID: 42194159](https://pubmed.ncbi.nlm.nih.gov/42194159/); [PMID: 20610195](https://pubmed.ncbi.nlm.nih.gov/20610195/)). TGCT is the **most common malignancy in men aged 15–45**, with ~500,000 prevalent cases worldwide (2002) and developed-region rates ~6× developing regions ([PMID: 17031378](https://pubmed.ncbi.nlm.nih.gov/17031378/)). Incidence has risen in successive birth cohorts born from ~1920 onward across 14 countries, with parallel seminoma/nonseminoma trends supporting a common fetal rate-limiting step.

> *"incidence has uniformly increased in successive generations born from around 1920 until very recently"* — [PMID: 17031378](https://pubmed.ncbi.nlm.nih.gov/17031378/)

**Inheritance patterns.** Mixed: the monogenic DSD end can be **autosomal dominant** (many NR5A1), **autosomal recessive** (INSL3/RXFP2 familial cryptorchidism), or **sex-chromosome mosaic** (45,X/46,XY). Common forms are **multifactorial / polygenic** — most isolated cryptorchidism is multifactorial ([PMID: 21403659](https://pubmed.ncbi.nlm.nih.gov/21403659/)), and TGCT susceptibility is polygenic with high per-allele ORs ([PMID: 25598472](https://pubmed.ncbi.nlm.nih.gov/25598472/)).

**Penetrance / expressivity.** NR5A1 shows highly **variable expressivity** (same gene → severe gonadal dysgenesis to isolated infertility) and incomplete penetrance ([PMID: 31513305](https://pubmed.ncbi.nlm.nih.gov/31513305/)). Consanguinity contributes to recessive INSL3/RXFP2 cryptorchidism ([PMID: 31167797](https://pubmed.ncbi.nlm.nih.gov/31167797/)).

**Population demographics.** Predominantly affects **Western/Caucasian** populations; historically highest national incidence in **Denmark/Norway**, lowest in **Finland** — mirroring the north-European gradient in cryptorchidism, hypospadias, and semen quality ([PMID: 17031378](https://pubmed.ncbi.nlm.nih.gov/17031378/); [PMID: 16005920](https://pubmed.ncbi.nlm.nih.gov/16005920/)). By definition the disorder affects genetic/phenotypic males.

---

## 10. Diagnostics

**Hormonal / laboratory biomarkers.**
- **Sertoli-cell markers:** inhibin B and anti-Müllerian hormone (AMH). Low inhibin B/FSH and AMH/FSH ratios and high FSH predict impaired germ cells per tubule in bilateral cryptorchid infants (ROC predictors, p=0.004–0.019) ([PMID: 34823367](https://pubmed.ncbi.nlm.nih.gov/34823367/)). AMH correlates with testicular volume and sperm concentration in men with maldescended testes ([PMID: 18423454](https://pubmed.ncbi.nlm.nih.gov/18423454/)).

> *"Anti-Müllerian hormone and inhibin B are essential biomarkers of Sertoli cell function. Also, INSL3 arises as an additional marker of Leydig cell dysfunction."* — [PMID: 23549308](https://pubmed.ncbi.nlm.nih.gov/23549308/)

- **Leydig-cell markers:** testosterone, LH, INSL3.
- **Semen analysis:** sperm concentration/count per WHO criteria.
- **Anogenital distance (AGD):** non-invasive biomarker of fetal androgen action ([PMID: 26846869](https://pubmed.ncbi.nlm.nih.gov/26846869/); [PMID: 23569219](https://pubmed.ncbi.nlm.nih.gov/23569219/)).

**Imaging.** Scrotal/inguinal ultrasound; MRI for non-palpable testis.

**Genetic testing.** Karyotype (detects 45,X/46,XY), chromosomal microarray, and DSD gene panels (NR5A1, INSL3, RXFP2, and other DSD genes); WES/targeted NGS resolves 46,XY DSD etiology ([PMID: 34338568](https://pubmed.ncbi.nlm.nih.gov/34338568/)).

**Histopathology / GCNIS detection.** Testicular biopsy with immunohistochemistry for pluripotency markers **OCT4/POU5F1, PLAP, AP-2γ, LIN28**; these can also detect GCNIS in semen samples ([PMID: 26306513](https://pubmed.ncbi.nlm.nih.gov/26306513/)). Pre-GCNIS shows centrally located OCT3/4+ gonocytes without full GCNIS morphology ([PMID: 40767035](https://pubmed.ncbi.nlm.nih.gov/40767035/)).

**Differential diagnosis.** Klinefelter syndrome, Noonan syndrome (Sertoli-cell-specific primary testicular insufficiency; [PMID: 30325180](https://pubmed.ncbi.nlm.nih.gov/30325180/)), androgen insensitivity syndrome, persistent Müllerian duct syndrome ([PMID: 40767035](https://pubmed.ncbi.nlm.nih.gov/40767035/)), and isolated (non-syndromic) component disorders.

---

## 11. Outcome / Prognosis

**TGCT component — excellent.** "Orchiectomy alone cure 80% of stage I" disease ([PMID: 31582176](https://pubmed.ncbi.nlm.nih.gov/31582176/)). Adjuvant treatments reduce relapse but confer **no overall-survival benefit** with substantial toxicity, so surveillance is now favored. TGCT is among the most curable solid cancers.

> *"Adjuvant treatments decrease the relapse rate after orchiectomy with substantial toxicities without any benefit on overall survival. Recent guidelines accorded utmost importance on SV rather than adjuvants strategies."* — [PMID: 31582176](https://pubmed.ncbi.nlm.nih.gov/31582176/)

**Cryptorchidism component.** Even after orchidopexy, long-term outcomes can be problematic: impaired fertility (~33% unilateral, ~66% bilateral) and a **5–10× increased malignancy risk** ([PMID: 20610195](https://pubmed.ncbi.nlm.nih.gov/20610195/)). Formerly unilateral cryptorchid men have only slightly (non-significantly) reduced paternity rates ([PMID: 33551366](https://pubmed.ncbi.nlm.nih.gov/33551366/)).

**Fertility / endocrine components.** Subfertility and compensated Leydig-cell failure are **largely irreversible**, managed by assisted reproduction and androgen replacement.

**Prognostic factors.** Low inhibin B/AMH, high FSH, reduced AGD, bilaterality, and Leydig-cell function (predicts sperm-retrieval success in Klinefelter: [PMID: 26235799](https://pubmed.ncbi.nlm.nih.gov/26235799/)).

---

## 12. Treatment

**Management is component-specific — there is no unitary "TDS" therapy.**

| Component | Treatment | NCIT suggestion |
|---|---|---|
| Cryptorchidism | **Orchidopexy** at 6–18 mo (ideally <12 mo) to preserve spermatogonia and reduce torsion/subfertility/malignancy risk ([PMID: 42194159](https://pubmed.ncbi.nlm.nih.gov/42194159/); [PMID: 33551366](https://pubmed.ncbi.nlm.nih.gov/33551366/)). Hormonal therapy (hCG/GnRH) has limited efficacy, not recommended as primary treatment ([PMID: 23748056](https://pubmed.ncbi.nlm.nih.gov/23748056/)) | Orchiopexy (C51919) |
| TGCT | **Radical inguinal orchiectomy** first-line; stage I options: active surveillance, single-agent carboplatin (seminoma) or BEP (bleomycin-etoposide-cisplatin)/RPLND (nonseminoma) ([PMID: 31582176](https://pubmed.ncbi.nlm.nih.gov/31582176/)) | Orchiectomy (C51576), Cisplatin (C376) |
| Hypospadias | Surgical urethroplasty | Urethroplasty |
| Infertility / poor semen quality | Assisted reproduction (ICSI/IVF), testicular sperm extraction (TESE/mTESE) | ICSI, IVF |
| Androgen insufficiency | Testosterone replacement | Testosterone therapy (C548) |

> *"Early referral, ideally before 12 months of age, is essential for timely orchidopexy, which aims to position the testes within the scrotum to reduce risks of torsion, trauma, subfertility, and malignancy."* — [PMID: 42194159](https://pubmed.ncbi.nlm.nih.gov/42194159/)

**Pharmacogenomics / experimental.** Taxifolin (antioxidant) rescues phthalate-induced dysgenesis in rats — a mechanistic lead, not a human therapy ([PMID: 36198370](https://pubmed.ncbi.nlm.nih.gov/36198370/)). Vitamin D/VDR downregulates pluripotency factors in TGCT cells in vitro but did not reduce tumor growth in xenografts ([PMID: 23097629](https://pubmed.ncbi.nlm.nih.gov/23097629/)).

---

## 13. Prevention

**Primary prevention.** Reduce maternal exposure to anti-androgenic endocrine disruptors (phthalates) and avoid non-essential **mild analgesics (paracetamol)** during pregnancy, especially during the MPW (GW 8–14) ([PMID: 21059752](https://pubmed.ncbi.nlm.nih.gov/21059752/); [PMID: 27609981](https://pubmed.ncbi.nlm.nih.gov/27609981/)). Environmental/regulatory interventions limiting phthalate exposure are logical public-health measures.

**Secondary prevention.** Early detection and **timely orchidopexy** of cryptorchidism; inclusion of testicular-cancer surveillance in the management of infertile men with poor semen quality ([PMID: 16522521](https://pubmed.ncbi.nlm.nih.gov/16522521/)). GCNIS detection via biopsy/semen immunocytochemistry in high-risk individuals ([PMID: 26306513](https://pubmed.ncbi.nlm.nih.gov/26306513/)).

**Tertiary prevention.** Surveillance of the contralateral testis and GCNIS monitoring; fertility preservation counseling.

**Genetic counseling.** Relevant for monogenic DSD (NR5A1, INSL3/RXFP2) and familial/bilateral TGCT. Prophylactic gonadectomy decisions in AIS should be individualized given low observed malignant progression ([PMID: 29121256](https://pubmed.ncbi.nlm.nih.gov/29121256/)).

---

## 14. Other Species / Natural Disease

**Taxonomy / orthologs.** Rat (*Rattus norvegicus*, NCBI:txid10116) and mouse (*Mus musculus*, NCBI:txid10090) are the principal experimental species. Orthologous genes: *Insl3*, *Rxfp2*, *Nr5a1*, *Kitlg*, *Dmrt1*.

**Comparative biology — key caveat.** Rats show robust phthalate-induced steroidogenic suppression, mice show only multinucleated germ-cell induction, and **human fetal testis xenografts resist steroidogenic suppression** — a critical species difference ([PMID: 22511013](https://pubmed.ncbi.nlm.nih.gov/22511013/); [PMID: 32779695](https://pubmed.ncbi.nlm.nih.gov/32779695/)). This limits direct extrapolation of rodent androgen-suppression mechanisms to humans, though the MPW concept and AGD biomarker translate.

**Natural disease / zoonotic.** No naturally occurring companion-animal or zoonotic form of TDS was identified; this is not a transmissible disease.

---

## 15. Model Organisms

**Rat (principal model).** In-utero phthalate (DBP/DEHP/DINP) exposure during the MPW is the gold-standard **induced model**, recapitulating reduced AGD, cryptorchidism, hypospadias, reduced adult testis size, compensated Leydig-cell failure, focal dysgenesis, Leydig-cell aggregation, and multinucleated gonocytes ([PMID: 28352662](https://pubmed.ncbi.nlm.nih.gov/28352662/); [PMID: 18174951](https://pubmed.ncbi.nlm.nih.gov/18174951/); [PMID: 33086118](https://pubmed.ncbi.nlm.nih.gov/33086118/)). **High phenotypic recapitulation** of the structural TDS components; focal dysgenetic changes resemble human pre-invasive lesions.

**Mouse (genetic models).** *Insl3* and *Rxfp2* knockouts cause cryptorchidism; the ENU **Rxfp2 D294G** missense model impairs descent with Sertoli-cell-only tubules ([PMID: 20963592](https://pubmed.ncbi.nlm.nih.gov/20963592/)); conditional shRNA RXFP2 suppression reveals Wnt/β-catenin and Notch involvement ([PMID: 21147849](https://pubmed.ncbi.nlm.nih.gov/21147849/)).

**Cell lines (in vitro).** NTERA-2 (embryonal carcinoma) and TCam-2 (seminoma) for TGCT pluripotency/differentiation and KITLG/cAMP studies ([PMID: 23097629](https://pubmed.ncbi.nlm.nih.gov/23097629/); [PMID: 23771924](https://pubmed.ncbi.nlm.nih.gov/23771924/)).

**Model limitations.** Rodents do **not** fully replicate the human germ-cell-cancer arm (no spontaneous GCNIS→TGCT progression), and rodent steroidogenic sensitivity to phthalates exceeds that of humans — a major translational caveat ([PMID: 22511013](https://pubmed.ncbi.nlm.nih.gov/22511013/)).

---

## Mechanistic Model / Interpretation

TDS is best understood as a **single fetal-origin lesion with four clinical faces**. The unifying node is **insufficient androgen (and INSL3) action in the masculinization programming window**. Everything upstream (genetic lesions, endocrine disruptors) converges on this node; everything downstream (the four disorders) diverges from it:

```
        UPSTREAM CAUSES                 CENTRAL LESION              DOWNSTREAM PHENOTYPES
 ┌─────────────────────────┐     ┌───────────────────────┐    ┌──────────────────────────┐
 │ Genetic:                │     │                       │    │ • Cryptorchidism         │
 │  NR5A1, INSL3/RXFP2,    │────▶│  Deficient fetal      │───▶│ • Hypospadias            │
 │  45,X/46,XY, KITLG,     │     │  androgen + INSL3      │    │ • Impaired               │
 │  DMRT1, SPRY4, TERT,    │     │  action in the MPW     │    │   spermatogenesis        │
 │  BAK1 (polygenic)       │     │  (GW 8–14)             │    │ • Testicular germ-cell   │
 │ Environmental:          │────▶│  → Sertoli/Leydig      │───▶│   cancer (via GCNIS)     │
 │  phthalates,            │     │    dysgenesis +        │    │                          │
 │  paracetamol            │     │    gonocyte arrest     │    │ Severity continuum:      │
 │ (gene × environment)    │     │                       │    │  mild subfertility ↔     │
 └─────────────────────────┘     └───────────────────────┘    │  46,XY gonadal dysgenesis│
                                            │                  └──────────────────────────┘
                                            ▼
                                  AGD = readout biomarker
```

Two mechanistic subtleties matter for the knowledge base. First, the **cancer arm is developmental**: GCNIS is an arrested, pluripotent fetal gonocyte that only becomes malignant after puberty — explaining both the young-adult incidence peak and the shared pluripotency biomarkers (OCT4/NANOG/AP-2γ/LIN28/PLAP). Second, the **human–rodent discordance** in phthalate steroidogenic sensitivity means the rat model proves *that* MPW androgen suppression causes TDS, but human causation by specific chemicals rests on epidemiology and biomarker (AGD) association rather than direct experimental proof.

---

## Evidence Base

| PMID | Role | Key contribution |
|---|---|---|
| [14671395](https://pubmed.ncbi.nlm.nih.gov/14671395/) | Foundational | Original TDS hypothesis uniting four disorders |
| [16005920](https://pubmed.ncbi.nlm.nih.gov/16005920/) | Supporting | Severe form (45,X/46,XY); geographic co-variation |
| [28352662](https://pubmed.ncbi.nlm.nih.gov/28352662/) | Mechanistic (strong) | MPW-restricted causality of DBP-induced TDS |
| [32779695](https://pubmed.ncbi.nlm.nih.gov/32779695/) | Mechanistic | MPW androgen action; AGD biomarker; human-rodent differences |
| [36198370](https://pubmed.ncbi.nlm.nih.gov/36198370/) | Mechanistic | Steroidogenic gene suppression + oxidative stress; taxifolin rescue |
| [18174951](https://pubmed.ncbi.nlm.nih.gov/18174951/) | Dose-response | Fetal endpoints most sensitive to DBP |
| [22511013](https://pubmed.ncbi.nlm.nih.gov/22511013/) | Challenging/caveat | Human fetal testis resists phthalate steroidogenic suppression |
| [25598472](https://pubmed.ncbi.nlm.nih.gov/25598472/) | Genetic | >25 TGCT risk SNPs at 19 loci; 5 mechanistic categories |
| [23640991](https://pubmed.ncbi.nlm.nih.gov/23640991/) | Genetic | Gene-level P-values (KITLG, DMRT1, SPRY4, TERT, BAK1) |
| [21617256](https://pubmed.ncbi.nlm.nih.gov/21617256/) | Genetic | Replication in familial/bilateral TGCT |
| [31513305](https://pubmed.ncbi.nlm.nih.gov/31513305/) | Genetic (DSD) | 188 NR5A1 mutations; phenotypic spectrum |
| [41369823](https://pubmed.ncbi.nlm.nih.gov/41369823/) | Genetic | Novel INSL3 LoF variants → cryptorchidism |
| [21403659](https://pubmed.ncbi.nlm.nih.gov/21403659/) | Mechanistic | INSL3/testosterone control of descent; multifactorial |
| [21059752](https://pubmed.ncbi.nlm.nih.gov/21059752/) | Gene×environment | Analgesics → cryptorchidism (Danish vs Finnish) |
| [27609981](https://pubmed.ncbi.nlm.nih.gov/27609981/) | Human biomarker | Prenatal paracetamol → shorter AGD |
| [18184914](https://pubmed.ncbi.nlm.nih.gov/18184914/) | Mechanistic (cancer) | CIS/GCNIS from arrested fetal germ cells |
| [26306513](https://pubmed.ncbi.nlm.nih.gov/26306513/) | Diagnostic | Pluripotency biomarkers for GCNIS |
| [15982323](https://pubmed.ncbi.nlm.nih.gov/15982323/) | Mechanistic | NANOG in fetal gonocytes, CIS, GCT |
| [31582176](https://pubmed.ncbi.nlm.nih.gov/31582176/) | Prognosis/treatment | Orchiectomy cures 80% stage I; surveillance favored |
| [42194159](https://pubmed.ncbi.nlm.nih.gov/42194159/) | Treatment/epi | Cryptorchidism 1–9%; orchidopexy <12 mo |
| [34823367](https://pubmed.ncbi.nlm.nih.gov/34823367/) | Diagnostic | Inhibin B/FSH, AMH/FSH predict germ-cell deficiency |
| [23549308](https://pubmed.ncbi.nlm.nih.gov/23549308/) | Diagnostic | AMH, inhibin B, INSL3 as Sertoli/Leydig markers |
| [28981654](https://pubmed.ncbi.nlm.nih.gov/28981654/) | Epidemiology | Sperm-count decline meta-regression |
| [36377604](https://pubmed.ncbi.nlm.nih.gov/36377604/) | Epidemiology | Global extension of sperm-count decline |
| [17031378](https://pubmed.ncbi.nlm.nih.gov/17031378/) | Epidemiology | Geographic/birth-cohort trends in TGCT |
| [36874603](https://pubmed.ncbi.nlm.nih.gov/36874603/) | Epidemiology | Median TGCT diagnosis age 37.7 y |

---

## Limitations and Knowledge Gaps

1. **TDS is a hypothesis, not a discrete molecular diagnosis.** It lacks a single OMIM entry, defined diagnostic criteria, or a unitary genetic test; the four components are also studied as independent disorders. The unifying construct rests on epidemiological co-occurrence and a shared fetal-androgen mechanism.
2. **Human causation by specific chemicals is inferential.** The strongest experimental evidence (MPW-restricted phthalate causality) is from rats; human fetal testis resists phthalate steroidogenic suppression ([PMID: 22511013](https://pubmed.ncbi.nlm.nih.gov/22511013/)). Human evidence is association-based (AGD, cohort studies).
3. **The malignant-transformation trigger** converting quiescent GCNIS to invasive TGCT after puberty is not fully defined.
4. **Genetic architecture is incompletely explained.** Known INSL3/RXFP2 mutations account for only a minority of cryptorchidism; TGCT heritability is polygenic and partly "missing."
5. **Epigenetic and single-cell/spatial profiling** specific to human TDS tissues were not catalogued and represent a gap.
6. **Quality-of-life data** using standardized instruments (EQ-5D/SF-36) specific to TDS were not identified.
7. **No protective genetic variants** have been established.

---

## Proposed Follow-up Experiments / Actions

1. **Human fetal testis organoids / xenografts** to define the molecular basis of the human-specific resistance to phthalate steroidogenic suppression, reconciling rodent and human mechanisms.
2. **Single-cell and spatial transcriptomics** of dysgenetic human fetal/perinatal testis to map Sertoli/Leydig/gonocyte trajectories and the gonocyte-arrest signature at cell resolution.
3. **Prospective AGD-anchored birth cohorts** linking MPW-window chemical/analgesic exposure, AGD, germline genotype (KITLG/DMRT1/NR5A1 polygenic score), and adult reproductive outcomes to formally test gene×environment interaction.
4. **GCNIS progression biomarkers:** define the pubertal signals (and candidate circulating/semen miRNAs) that drive GCNIS→TGCT, enabling earlier risk stratification.
5. **Antioxidant intervention proof-of-concept:** extend the taxifolin rescue finding ([PMID: 36198370](https://pubmed.ncbi.nlm.nih.gov/36198370/)) toward evaluating maternal antioxidant status as a modifier of endocrine-disruptor injury.
6. **Harmonized diagnostic panel:** standardize combined inhibin B/AMH/FSH/INSL3 + AGD + pluripotency-marker IHC into a validated TDS-risk stratification tool.
7. **Knowledge-base curation:** map the suggested ontology terms (HPO, GO, CL, UBERON, CHEBI, NCIT) to each phenotype/mechanism/cell type for structured annotation.

---

*Report generated from a 5-iteration autonomous investigation: 12 confirmed findings, 57 papers reviewed. Evidence types span human clinical/epidemiological, model organism (rat/mouse), in vitro, and computational/GWAS sources, distinguished throughout.*


## Artifacts

- [OpenScientist final report](Testicular_Dysgenesis_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Testicular_Dysgenesis_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 48 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 48 |
| On topic | 21 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:28981654` (1 mention) - Temporal trends in sperm count: a systematic review and meta-regression analysis.
  - shared terms: human
- `PMID:36377604` (1 mention) - Temporal trends in sperm count: a systematic review and meta-regression analysis of samples collected globally in the 20th and 21st centuries.
  - shared terms: human

Weighed against this report's own most characteristic terms: `tds`, `tgct`, `cryptorchidism`, `fetal`, `insl3`, `gcnis`, `cell`, `testis`, `human`, `rxfp2`, `component`, `phthalate`, `agd`, `nr5a1`, `genetic`, `gonocyte`, `mpw`, `testosterone`, `testicular`, `dysgenesis`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 13 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005437` (2 mentions) - the report calls it "MONDO"; MONDO calls it **testicular dysgenesis syndrome**
- `HP:0000028` (1 mention) - the report calls it "~1–9% of full-term male infants; uni/bilateral"; HP calls it **Cryptorchidism**
- `HP:0000047` (1 mention) - the report calls it "Variable"; HP calls it **Hypospadias**
- `HP:0010788` (1 mention) - the report calls it "Most common malignancy in men 15–45"; HP calls it **Testicular neoplasm**
- `HP:0008720` (1 mention) - the report calls it "Variable"; HP calls it **Primary testicular failure**
- `HP:0000062` (1 mention) - the report calls it "Rare, severe subset"; HP calls it **Ambiguous genitalia**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `CHEBI:41448` (1 mention) - CHEBI does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000798` (1 mention) - the report calls it "oligospermia"; HP calls it **Oligozoospermia**, and lists "Oligospermia" among its other names
- `CL:0000015` (2 mentions) - the report calls it "fetal gonocytes / germ cells"; CL calls it **male germ cell**
- `UBERON:0000079` (1 mention) - the report calls it "male reproductive / endocrine system"; UBERON calls it **male reproductive system**