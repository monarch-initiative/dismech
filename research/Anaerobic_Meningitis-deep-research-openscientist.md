---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T20:17:26.295852'
end_time: '2026-09-29T20:32:44.673464'
duration_seconds: 918.38
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Anaerobic meningitis
  mondo_id: MONDO:0002000
  category: Infectious Disease
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
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 26
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 18
  quotes_valid: 18
  relevance_assessed: 28
  on_topic: 9
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 32
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 24
  labels_matching: 13
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: HP:0001945
    reported_labels:
    - Symptom
    ontology_label: Fever
  - term_id: HP:0002315
    reported_labels:
    - Symptom
    ontology_label: Headache
  - term_id: HP:0011446
    reported_labels:
    - Symptom/sign
    ontology_label: Abnormality of mental function
  - term_id: HP:0001250
    reported_labels:
    - Clinical sign
    ontology_label: Seizure
  - term_id: HP:0034332
    reported_labels:
    - Sign
    ontology_label: Cognitive regression
  - term_id: HP:0000613
    reported_labels:
    - Symptom
    ontology_label: Photophobia
  - term_id: HP:0025432
    reported_labels:
    - CSF pleocytosis
    ontology_label: Acanthoma
  - term_id: CL:0000775
    reported_labels:
    - neutrophil
    - Tissue/cell level:** vascular endothelium of the BBB, neutrophils
    ontology_label: neutrophil
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Anaerobic_Meningitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Anaerobic_Meningitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Anaerobic meningitis
- **MONDO ID:** MONDO:0002000 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Anaerobic meningitis** covering all of the
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

# Anaerobic Meningitis (MONDO:0002000): A Comprehensive Disease Characterization

**Category:** Infectious Disease | **Disease type:** Acquired bacterial CNS infection (non-heritable)
*Evidence base: literature synthesis (no primary datasets provided). PMIDs cited throughout; evidence type noted as human clinical, animal/model, or in vitro.*

---

## Summary

**Anaerobic meningitis is a rare, acquired infection of the leptomeninges caused by obligate or aerotolerant anaerobic bacteria, accounting for only about 2.4% of adult culture-proven bacterial meningitis.** It is not a genetic or heritable disorder; instead it is a mechanistically driven infectious disease that arises almost exclusively in hosts with an anatomic or immunologic predisposition. The dominant routes of meningeal invasion are (i) contiguous spread from ear/nose/throat (ENT), odontogenic, or sinus foci; (ii) direct inoculation via neurosurgery, penetrating trauma, or indwelling CNS hardware (ventriculoperitoneal shunts, external ventricular drains); and (iii) hematogenous seeding or gut translocation. The principal causative organisms are Gram-negative anaerobes *Fusobacterium* (*necrophorum*, *nucleatum*), *Bacteroides fragilis*, and *Prevotella* species, together with Gram-positive anaerobes *Cutibacterium (Propionibacterium) acnes* and *Parvimonas micra (Peptostreptococcus micros)*, with mixed/polymicrobial infection in nearly half of adult cases.

The pathophysiology follows the canonical bacterial-meningitis inflammatory cascade: after anaerobes reach the subarachnoid space, bacterial components are recognized by Toll-like receptors, activating NF-κB and MAPK signaling, driving a surge of proinflammatory cytokines (TNF-α, IL-1β, IL-6) and chemokines, recruiting neutrophils that generate superoxide and nitric oxide, producing peroxynitrite-mediated oxidative stress, blood-brain-barrier breakdown, and ultimately neuronal injury. Pathogen-specific virulence factors amplify this process — notably the *B. fragilis* capsular polysaccharide (a direct abscess-forming, antiphagocytic factor) and the *F. necrophorum* leukotoxin.

Because fastidious anaerobes are frequently missed by routine culture, diagnosis increasingly depends on 16S rRNA PCR and metagenomic next-generation sequencing (mNGS), supported by CSF lactate (highly discriminatory for bacterial vs. aseptic meningitis) and neuroimaging for complications (mastoiditis, abscess, cavernous sinus/internal jugular thrombosis). Treatment combines metronidazole (excellent CSF penetration, bactericidal against obligate anaerobes) with a broad-spectrum β-lactam, plus surgical source control and adjunctive corticosteroids. Despite therapy, adult mortality is ~30%, and the majority of survivors have neurological sequelae, making this a high-morbidity condition even though it is uncommon.

---

## Disease Information (Section 1)

**Overview.** Anaerobic meningitis is inflammation of the meninges caused by anaerobic bacteria. It is best regarded as a rare microbiological subset of bacterial meningitis rather than a distinct nosological entity. It is defined by the recovery (by culture or molecular methods) of obligate/aerotolerant anaerobes from cerebrospinal fluid (CSF) in a patient with clinical and CSF evidence of meningitis.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0002000 (anaerobic meningitis) |
| MeSH | "Meningitis, Bacterial" (D016920); anaerobic infection is not separately termed |
| ICD-10 | G00–G03; specifically G00.8 (other bacterial meningitis), G03.8/G03.9 for unspecified/other |
| ICD-11 | 1D01 (bacterial meningitis) |
| SNOMED CT | Bacterial meningitis (concept) |
| OMIM / Orphanet | Not applicable — no Mendelian/rare-genetic entry (acquired infection) |

**Synonyms / alternative names.** Anaerobic bacterial meningitis; meningitis due to anaerobic bacteria; organism-specific descriptors such as *Fusobacterium* meningitis, *Bacteroides fragilis* meningitis, *Cutibacterium/Propionibacterium acnes* meningitis, *Prevotella* meningitis, and *Parvimonas/Peptostreptococcus* meningitis.

**Information source.** The evidence base derives from a mixture of individual case reports/case series (EHR-derived clinical data) and aggregated single-center/national cohort studies; there are no disease-level genetic resources because the condition is not heritable.

---

## Etiology (Section 2)

**Primary cause — infectious/mechanistic.** Anaerobic meningitis is caused by anaerobic bacteria that are normal commensals of the oral cavity, gut, and skin gaining access to the subarachnoid space. In a 30-year single-center series of 540 culture-proven adult bacterial meningitis cases, 13 (2.4%) were anaerobic, from which 14 strains were isolated: *Fusobacterium nucleatum* (3), *Prevotella* spp. (3), *Bacteroides fragilis* (3), *Cutibacterium/Propionibacterium acnes* (3), and *Parvimonas micra/Peptostreptococcus micros* (2) ([PMID: 29396061](https://pubmed.ncbi.nlm.nih.gov/29396061/)).

> "including nine Gram-negative (G(-)) strains: Fusobacterium nucleatum (3), Prevotella species (3) and Bacteroides fragilis (3), and five Gram-positive (G(+)) strains: Propionibacterium acnes (3) and Peptostreptococcus micros (also known as Parvimonas micra) (2)" — [PMID: 29396061](https://pubmed.ncbi.nlm.nih.gov/29396061/)

**Risk factors (environmental / acquired).** There are essentially no *genetic* causal risk factors. The dominant risk factors are anatomic and clinical:

- **Postneurosurgical state** — 53.8% (7/13) in the adult series ([PMID: 29396061](https://pubmed.ncbi.nlm.nih.gov/29396061/)).
- **Underlying medical conditions** — 79.6% (10/13): diabetes mellitus, malignancy, liver cirrhosis, cerebral infarct, alcoholism ([PMID: 29396061](https://pubmed.ncbi.nlm.nih.gov/29396061/)).
- **Head trauma, prior neurosurgical procedures, and implanted devices** (VP shunts, ventricular drains) ([PMID: 32717475](https://pubmed.ncbi.nlm.nih.gov/32717475/)).
- **ENT infections** — near-universal precursor in pediatric *F. necrophorum* meningitis (acute otitis media in 21/27) ([PMID: 41479136](https://pubmed.ncbi.nlm.nih.gov/41479136/)).
- **Odontogenic sources** — recent molar extraction, periodontitis ([PMID: 41330476](https://pubmed.ncbi.nlm.nih.gov/41330476/), [PMID: 35692070](https://pubmed.ncbi.nlm.nih.gov/35692070/)).

> "53.8% (7/13) had a postneurosurgical state as the preceding event, and 79.6% (10/13) had underlying medical conditions including diabetes mellitus, malignancy, liver cirrhosis, cerebral infarct and alcoholism" — [PMID: 29396061](https://pubmed.ncbi.nlm.nih.gov/29396061/)

**Genetic modifiers (not causal).** Host genetic variation modifies the *inflammatory response and outcome*, not susceptibility to infection per se: single-nucleotide polymorphisms in inflammasome genes **CARD8 (rs2043211)** and **NLRP1 (rs11621270)** are associated with poor outcome in bacterial meningitis ([PMID: 23053059](https://pubmed.ncbi.nlm.nih.gov/23053059/)).

**Protective factors.** Prompt treatment/source control of predisposing ENT, dental, and abdominal infections; strict neurosurgical/device asepsis. No genetic protective alleles are established. Anticapsular antibody protects against *B. fragilis* bacteremia while T-cell-mediated immunity protects against abscess in animal models ([PMID: 549184](https://pubmed.ncbi.nlm.nih.gov/549184/)).

**Gene-environment interactions.** The only demonstrable GxE interplay is that inflammasome/complement genotype (CARD8, NLRP1; MASP-2) shapes how severely the host responds to the anaerobic infectious trigger ([PMID: 23053059](https://pubmed.ncbi.nlm.nih.gov/23053059/), [PMID: 28086930](https://pubmed.ncbi.nlm.nih.gov/28086930/)).

---

## Phenotypes (Section 3)

Clinical phenotypes are those of bacterial meningitis generally, though anaerobic cases are more likely to be subacute or atypical. In 696 adults with community-acquired bacterial meningitis, the classic triad of fever, neck stiffness, and altered mental status was present in only 44%, but 95% had ≥2 of the 4 cardinal features; 14% were comatose and 33% had focal neurologic deficits ([PMID: 15509818](https://pubmed.ncbi.nlm.nih.gov/15509818/)).

> "The classic triad of fever, neck stiffness, and a change in mental status was present in only 44 percent of episodes; however, 95 percent had at least two of the four symptoms of headache, fever, neck stiffness, and altered mental status." — [PMID: 15509818](https://pubmed.ncbi.nlm.nih.gov/15509818/)

| Phenotype | Type | HPO suggestion | Frequency / notes |
|---|---|---|---|
| Fever | Symptom | HP:0001945 | Common; may be absent in host-defective/atypical cases |
| Headache | Symptom | HP:0002315 | Very common; may be subacute in anaerobic cases |
| Neck stiffness / meningismus | Clinical sign | HP:0031179 (nuchal rigidity) | Part of triad; absent in ~half |
| Altered mental status | Symptom/sign | HP:0011446 | Part of triad; 14% comatose |
| Seizures | Clinical sign | HP:0001250 | Reported, esp. with abscess |
| Focal neurologic deficit | Sign | HP:0034332 | ~33% in bacterial meningitis |
| Cranial nerve palsy (e.g., VI) | Sign | HP:0006802 / HP:0000651 | With cavernous sinus thrombosis ([PMID: 41330476](https://pubmed.ncbi.nlm.nih.gov/41330476/)) |
| Photophobia | Symptom | HP:0000613 | Reported ([PMID: 41330476](https://pubmed.ncbi.nlm.nih.gov/41330476/)) |
| CSF pleocytosis (neutrophilic) | Lab abnormality | HP:0025432 (CSF pleocytosis) | Characteristic; occasionally absent in immunocompromised |
| Elevated CSF protein / low glucose | Lab abnormality | HP:0002922 / HP:0032672 | Typical bacterial pattern |
| Elevated CSF lactate | Lab abnormality | — | Discriminatory marker |

**Onset/severity/progression.** Age of onset is bimodal in practice — a pediatric cluster (median 4 years, *F. necrophorum*, ENT-driven) and adults (22–77 years), plus rare neonatal *B. fragilis* disease. Severity is typically severe; progression is acute to subacute. Anaerobic-specific atypical presentations include subacute headache without fever/neck stiffness in otogenic polymicrobial cases ([PMID: 37629718](https://pubmed.ncbi.nlm.nih.gov/37629718/)) and cranial-nerve palsy with cavernous sinus thrombosis ([PMID: 41330476](https://pubmed.ncbi.nlm.nih.gov/41330476/)).

**Quality of life impact.** Substantial — the majority of survivors carry neurological deficits (see Prognosis).

---

## Genetic / Molecular Information (Section 4)

**Not applicable as a heritable disease.** Anaerobic meningitis has **no causal genes, no pathogenic germline variants, no inheritance pattern, no penetrance, and no carrier frequency** ([PMID: 29396061](https://pubmed.ncbi.nlm.nih.gov/29396061/); acquired-infection framing). The only host-genetic contribution is as an *outcome modifier*:

- **CARD8** (rs2043211) and **NLRP1** (rs11621270) inflammasome polymorphisms — associated with poor outcome ([PMID: 23053059](https://pubmed.ncbi.nlm.nih.gov/23053059/)).
- **MASP-2** (complement lectin pathway) — higher CSF levels correlate with poor functional outcome ([PMID: 28086930](https://pubmed.ncbi.nlm.nih.gov/28086930/)).

> "single-nucleotide polymorphisms in the inflammasome genes CARD8 (rs2043211) and NLRP1 (rs11621270) are associated with poor disease outcome" — [PMID: 23053059](https://pubmed.ncbi.nlm.nih.gov/23053059/)

The relevant "molecular" genetics are microbial: bacterial virulence loci encoding the *B. fragilis* capsular polysaccharide biosynthesis genes and the *F. necrophorum* leukotoxin operon (see Mechanism).

---

## Environmental Information (Section 5)

**Environmental / lifestyle contributors** operate by predisposing to anaerobic invasion: chronic otitis media, sinusitis, periodontal disease, dental extraction, alcoholism, diabetes mellitus, malignancy, cirrhosis, and neurosurgery/indwelling devices ([PMID: 29396061](https://pubmed.ncbi.nlm.nih.gov/29396061/), [PMID: 32717475](https://pubmed.ncbi.nlm.nih.gov/32717475/), [PMID: 41330476](https://pubmed.ncbi.nlm.nih.gov/41330476/)).

**Infectious agents (NCBI Taxonomy).**

| Organism | NCBI Taxon | Gram | Typical source |
|---|---|---|---|
| *Fusobacterium necrophorum* | txid859 | – | Oropharynx/ENT; Lemierre |
| *Fusobacterium nucleatum* | — | – | Oral; odontogenic |
| *Bacteroides fragilis* | txid817 | – | Gut; neonatal/abdominal |
| *Prevotella* spp. | — | – | Oral/ENT |
| *Parvimonas micra* | — | + | Oral |
| *Cutibacterium acnes* | txid1747 | + | Skin; neurosurgical device |
| *Clostridium perfringens* | txid1502 | + | Trauma/gut |

---

## Mechanism / Pathophysiology (Section 6)

### Ordered causal chain

1. Endogenous anaerobes colonize a mucosal/skin site (oropharynx, gut, skin) → serve as the reservoir.
2. A predisposing lesion (ENT/odontogenic infection, neurosurgery, trauma, device, immunosuppression) **breaches** the normal barrier → **leads to** anaerobic access to blood or contiguous CNS tissue.
3. Anaerobes reach the subarachnoid space by contiguous spread, direct inoculation, or hematogenous/gut translocation → **results in** subarachnoid bacterial replication (favored by the immune-privileged, complement-poor CSF).
   - *Branch (F. necrophorum):* oropharyngeal infection → septic internal jugular vein thrombophlebitis (**Lemierre syndrome**) → septic emboli → CNS seeding ([PMID: 42568628](https://pubmed.ncbi.nlm.nih.gov/42568628/), [PMID: 41479136](https://pubmed.ncbi.nlm.nih.gov/41479136/)).
   - *Branch (B. fragilis):* capsular polysaccharide → abscess formation independent of other organisms ([PMID: 6954635](https://pubmed.ncbi.nlm.nih.gov/6954635/)).
4. Bacterial components are recognized by **Toll-like receptors** on antigen-presenting/brain cells → **activates** NF-κB and MAPK pathways ([PMID: 22618789](https://pubmed.ncbi.nlm.nih.gov/22618789/)).
5. Transcriptional activation → **up-regulates** proinflammatory mediators **TNF-α, IL-1β, IL-6**, and chemokines ([PMID: 22618789](https://pubmed.ncbi.nlm.nih.gov/22618789/), [PMID: 24105840](https://pubmed.ncbi.nlm.nih.gov/24105840/)).
6. Cytokine/chemokine surge → **recruits and activates** polymorphonuclear neutrophils into the subarachnoid space.
7. Activated neutrophils → **release** superoxide anion and nitric oxide → **form** peroxynitrite → **generate** oxidative stress ([PMID: 22618789](https://pubmed.ncbi.nlm.nih.gov/22618789/)).
8. Oxidative stress → **causes** lipid peroxidation, mitochondrial damage, and **blood-brain-barrier breakdown** ([PMID: 22618789](https://pubmed.ncbi.nlm.nih.gov/22618789/)).
9. BBB breakdown + inflammation → **produces** cerebral edema, raised intracranial pressure, impaired cerebral blood flow, and **neuronal injury** → clinical meningitis, deficits, death.
10. Host genetic modifiers (CARD8/NLRP1 inflammasome, MASP-2 complement) **tune** the magnitude of steps 5–9 and thereby outcome ([PMID: 23053059](https://pubmed.ncbi.nlm.nih.gov/23053059/), [PMID: 28086930](https://pubmed.ncbi.nlm.nih.gov/28086930/)).

```
Reservoir → Barrier breach → Subarachnoid invasion/replication
     │                                   │
     │                            TLR recognition
     │                          (NF-κB / MAPK)  ← [GO:0038123 TLR signaling]
     │                                   │
     │                     TNF-α / IL-1β / IL-6 / chemokines
     │                                   │
     │                        Neutrophil recruitment (CL:0000775)
     │                                   │
     │                   Superoxide + NO → peroxynitrite (oxidative stress)
     │                                   │
     │                 Lipid peroxidation, mitochondrial damage, BBB breakdown
     │                                   │
Virulence branches:              Cerebral edema / ↑ICP / neuronal injury
 • B. fragilis capsule → abscess            │
 • F. necrophorum leukotoxin           Clinical meningitis → deficits / death
 • Lemierre (IJV thrombophlebitis)
```

### Supporting detail

> "S. pneumoniae is recognized by antigen-presenting cells through the binding of Toll-like receptors inducing the activation of factor nuclear kappa B or mitogen-activated protein kinase pathways" — [PMID: 22618789](https://pubmed.ncbi.nlm.nih.gov/22618789/)

> "polymorphonuclear are attracted, activated and released in large amounts of superoxide anion and nitric oxide, leading to the peroxynitrite formation, generating oxidative stress. This cascade leads to lipid peroxidation, mitochondrial damage, blood-brain barrier breakdown" — [PMID: 22618789](https://pubmed.ncbi.nlm.nih.gov/22618789/)

**Virulence factors.** The *B. fragilis* **capsular polysaccharide (CP)** is the key virulence factor: encapsulated strains form abscesses directly attributable to CP, and CP protects against phagocytosis ([PMID: 6954635](https://pubmed.ncbi.nlm.nih.gov/6954635/), [PMID: 3865350](https://pubmed.ncbi.nlm.nih.gov/3865350/)). By contrast, *B. fragilis* **LPS is chemically incomplete and weakly endotoxic** — the abscess-inducing LPS dose is ~5× higher than that of CP — explaining infrequent DIC/purpura in *Bacteroides* sepsis ([PMID: 549184](https://pubmed.ncbi.nlm.nih.gov/549184/), [PMID: 3711690](https://pubmed.ncbi.nlm.nih.gov/3711690/)).

> "The abscesses caused by encapsulated strains were shown to be directly attributable to the capsular polysaccharide, which is an important virulence factor of this organism." — [PMID: 6954635](https://pubmed.ncbi.nlm.nih.gov/6954635/)

> "the lipopolysaccharides of Bacteroides lack the biologic potency characteristic of endotoxin" — [PMID: 549184](https://pubmed.ncbi.nlm.nih.gov/549184/)

**Model-organism corroboration.** In Wistar rats, experimental Gram-negative (Klebsiella) meningitis produced a TNF-α/IL-1β/IL-6/CINC-1 surge within 6–24 h and long-term memory impairment ([PMID: 24105840](https://pubmed.ncbi.nlm.nih.gov/24105840/)).

**Ontology suggestions.** GO:0038123 (Toll-like receptor signaling), GO:0006954 (inflammatory response), GO:0006979 (response to oxidative stress), GO:0097529 (myeloid leukocyte migration); CL:0000775 (neutrophil), CL:0000129 (microglial cell), CL:0000540 (neuron); CHEBI:16240 (hydrogen peroxide), CHEBI:18421 (superoxide), CHEBI:25812 (peroxynitrite); metronidazole (CHEBI:6909).

---

## Anatomical Structures Affected (Section 7)

- **Primary organ / body system:** the **leptomeninges** (pia-arachnoid) and subarachnoid space of the **central nervous system** — UBERON:0002360 (meninx), UBERON:0002361 (pia mater), UBERON:0002362 (arachnoid mater), UBERON:0001359 (CSF), UBERON:0001017 (CNS).
- **Secondary involvement:** brain parenchyma (cerebritis/abscess, UBERON:0000955), ventricles (ventriculitis), cranial nerves, cavernous sinus and internal jugular vein (thrombosis), mastoid air cells and paranasal sinuses (contiguous foci).
- **Tissue/cell level:** vascular endothelium of the BBB, neutrophils (CL:0000775), microglia (CL:0000129), astrocytes (CL:0000127), neurons (CL:0000540).
- **Subcellular:** mitochondria (GO:0005739; oxidative damage), plasma membrane lipids (peroxidation), nucleus (NF-κB translocation).
- **Localization / lateralization:** the meningitis itself is typically diffuse/bilateral; complications (mastoiditis, subperiosteal/epidural abscess, IJV thrombosis, cavernous sinus thrombosis) may be unilateral or bilateral ([PMID: 41479136](https://pubmed.ncbi.nlm.nih.gov/41479136/), [PMID: 42568628](https://pubmed.ncbi.nlm.nih.gov/42568628/)).

---

## Temporal Development (Section 8)

- **Onset:** acute to subacute; anaerobic cases skew more subacute/insidious than pyogenic aerobic meningitis, sometimes without fever or neck stiffness ([PMID: 37629718](https://pubmed.ncbi.nlm.nih.gov/37629718/)).
- **Age of onset:** pediatric cluster (median 4 y for *F. necrophorum*), adults 22–77 y, and rare neonates (*B. fragilis*) ([PMID: 41479136](https://pubmed.ncbi.nlm.nih.gov/41479136/), [PMID: 29396061](https://pubmed.ncbi.nlm.nih.gov/29396061/), [PMID: 31838318](https://pubmed.ncbi.nlm.nih.gov/31838318/)).
- **Progression:** rapid if untreated; complicated meningitis (20/27 pediatric cases) with mastoiditis, subperiosteal/epidural abscess, or Lemierre syndrome, 12/27 requiring surgical drainage ([PMID: 41479136](https://pubmed.ncbi.nlm.nih.gov/41479136/)).
- **Course/duration:** typically requires prolonged therapy (often 4–8 weeks when abscess present); not relapsing-remitting, though superinfection/recurrence occurs with retained devices ([PMID: 28089421](https://pubmed.ncbi.nlm.nih.gov/28089421/)).
- **Critical period for intervention:** early antibiotic + corticosteroid administration (steroids before/with antibiotics) is the key therapeutic window ([PMID: 41675892](https://pubmed.ncbi.nlm.nih.gov/41675892/), [PMID: 40113367](https://pubmed.ncbi.nlm.nih.gov/40113367/)).

---

## Inheritance and Population (Section 9)

**Inheritance:** none — acquired infectious disease; inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effects, consanguinity, and carrier frequency are all **not applicable**.

**Epidemiology.**

| Metric | Value | Source |
|---|---|---|
| Fraction of adult culture-proven bacterial meningitis | ~2.4% (13/540 over 30 y) | [PMID: 29396061](https://pubmed.ncbi.nlm.nih.gov/29396061/) |
| Positive anaerobic CSF cultures (5-y study) | 24/594 (4%), only 3 clinically true | [PMID: 32717475](https://pubmed.ncbi.nlm.nih.gov/32717475/) |
| Pediatric *F. necrophorum* meningitis (2001–2024, France) | 27 cases; median age 4 y | [PMID: 41479136](https://pubmed.ncbi.nlm.nih.gov/41479136/) |
| Adult age range | 22–77 y; 8M:5F (slight male predominance) | [PMID: 29396061](https://pubmed.ncbi.nlm.nih.gov/29396061/) |

> "We enrolled 540 patients with culture-proven bacterial meningitis during a study period of 30 years (1986-2015), of whom 13 (2.4%) had anaerobic infections." — [PMID: 29396061](https://pubmed.ncbi.nlm.nih.gov/29396061/)

> "24/594 (4%) anaerobic cultures from 14 patients were positive for anaerobes. Only 3 of those patients were diagnosed clinically with anaerobic meningitis, each with predisposing factors" — [PMID: 32717475](https://pubmed.ncbi.nlm.nih.gov/32717475/)

**Population demographics.** No ethnic or geographic predilection is established; distribution reflects the prevalence of predisposing conditions (ENT infection, neurosurgery, immunocompromise). Sex ratio is roughly balanced with slight male predominance in adults.

---

## Diagnostics (Section 10)

**Core principle:** routine aerobic culture misses fastidious anaerobes, and anaerobic culture is low-yield and contamination-prone (many *C. acnes* isolates are contaminants) ([PMID: 32717475](https://pubmed.ncbi.nlm.nih.gov/32717475/)).

> "In the majority of situations, recovery of C. acnes from CSF or ventricular fluid was regarded as contamination." — [PMID: 32717475](https://pubmed.ncbi.nlm.nih.gov/32717475/)

**Laboratory / CSF.** Neutrophilic pleocytosis, elevated protein, low glucose; **CSF lactate** is the most useful discriminator — pooled sensitivity 0.93 (95% CI 0.89–0.96) and specificity 0.96 (95% CI 0.93–0.98) at ~35 mg/dL, generated by bacterial anaerobic metabolism ([PMID: 21382412](https://pubmed.ncbi.nlm.nih.gov/21382412/)).

> "The pooled test characteristics of CSF lactate were sensitivity 0.93 (95% CI: 0.89-0.96), specificity 0.96 (95% CI: 0.93-0.98)" — [PMID: 21382412](https://pubmed.ncbi.nlm.nih.gov/21382412/)

**Molecular diagnostics (increasingly first-line for anaerobes).** 16S rRNA PCR and metagenomic next-generation sequencing (mNGS) recover pathogens when culture fails ([PMID: 35692070](https://pubmed.ncbi.nlm.nih.gov/35692070/), [PMID: 37775739](https://pubmed.ncbi.nlm.nih.gov/37775739/), [PMID: 41479136](https://pubmed.ncbi.nlm.nih.gov/41479136/)).

**Imaging.** Contrast CT/MRI to detect meningeal enhancement, brain abscess, mastoiditis/sinusitis, and cavernous sinus / internal jugular vein thrombosis ([PMID: 41330476](https://pubmed.ncbi.nlm.nih.gov/41330476/), [PMID: 42568628](https://pubmed.ncbi.nlm.nih.gov/42568628/)).

**Differential diagnosis.** Aerobic bacterial meningitis; aseptic/viral meningitis; tuberculous meningitis; drug-induced aseptic meningitis (e.g., trimethoprim-sulfamethoxazole, [PMID: 39540422](https://pubmed.ncbi.nlm.nih.gov/39540422/)); primary amebic meningoencephalitis (*Naegleria fowleri*), which mimics bacterial meningitis ([PMID: 42426619](https://pubmed.ncbi.nlm.nih.gov/42426619/)). Genetic testing (WGS/WES/panels/karyotype/CMA) is **not applicable**.

---

## Outcome / Prognosis (Section 11)

**Prognosis is poor**, driven by delayed diagnosis and host comorbidity.

| Outcome | Value | Source |
|---|---|---|
| Adult mortality | 30.8% (4/13) | [PMID: 29396061](https://pubmed.ncbi.nlm.nih.gov/29396061/) |
| Full recovery among survivors | 22.2% (2/9) | [PMID: 29396061](https://pubmed.ncbi.nlm.nih.gov/29396061/) |
| Neurological deficits among survivors | 77.8% (7/9) | [PMID: 29396061](https://pubmed.ncbi.nlm.nih.gov/29396061/) |
| mNGS CNS-anaerobic cohort mortality | 3/8 | [PMID: 35692070](https://pubmed.ncbi.nlm.nih.gov/35692070/) |
| Pediatric *F. necrophorum* deaths | 4/27; 20/27 complicated | [PMID: 41479136](https://pubmed.ncbi.nlm.nih.gov/41479136/) |

> "Despite treatment, 30.8% (4/13) of the patients died. Of the nine survivors, 22.2% (2/9) had a full recovery, while the other 77.8% (7/9) had varying degrees of neurological deficits." — [PMID: 29396061](https://pubmed.ncbi.nlm.nih.gov/29396061/)

**Complications:** brain abscess, subdural empyema, ventriculitis, cavernous sinus/IJV thrombosis, mastoiditis, Lemierre syndrome with septic pulmonary emboli, hydrocephalus, seizures, sensorineural deficits. **Prognostic factors:** promptness of therapy, source control, host comorbidity, host inflammasome/complement genotype (CARD8, NLRP1, MASP-2), and CSF cytokine levels ([PMID: 23053059](https://pubmed.ncbi.nlm.nih.gov/23053059/), [PMID: 28086930](https://pubmed.ncbi.nlm.nih.gov/28086930/)).

---

## Treatment (Section 12)

**Pharmacotherapy — antimicrobial mainstay.** **Metronidazole** (CHEBI:6909; NCIT: Metronidazole) is bactericidal against obligate anaerobes with excellent CSF penetration; it eradicated anaerobic pathogens in CNS infection with 5/6 patients recovering in an early series ([PMID: 434970](https://pubmed.ncbi.nlm.nih.gov/434970/)). Modern regimens combine metronidazole with a **third-generation cephalosporin** (ceftriaxone/cefotaxime) for Gram-negative/streptococcal coverage ([PMID: 41330476](https://pubmed.ncbi.nlm.nih.gov/41330476/)). Alternatives: carbapenems (meropenem) and β-lactam/β-lactamase-inhibitor combinations (piperacillin-tazobactam). Gram-positive anaerobes (*Cutibacterium*, *Parvimonas*) are usually penicillin-susceptible ([PMID: 29396061](https://pubmed.ncbi.nlm.nih.gov/29396061/)).

> "In all cases the anaerobic pathogens were eradicated. Five of the six patients recovered." — [PMID: 434970](https://pubmed.ncbi.nlm.nih.gov/434970/)

**Source control / surgery.** Surgical excision or drainage of abscess and replacement of infected devices, with prolonged antibiotics (usually 4–8 weeks) when abscess is present ([PMID: 28089421](https://pubmed.ncbi.nlm.nih.gov/28089421/), [PMID: 32717475](https://pubmed.ncbi.nlm.nih.gov/32717475/)).

> "surgical excision or drainage combined with prolonged antibiotics (usually 4-8weeks) remains the treatment of choice." — [PMID: 28089421](https://pubmed.ncbi.nlm.nih.gov/28089421/)

**Adjunctive corticosteroids.** Dexamethasone reduces mortality and neurological sequelae in acute bacterial (especially pneumococcal) meningitis when given before/with antibiotics ([PMID: 41675892](https://pubmed.ncbi.nlm.nih.gov/41675892/)); pediatric data support dexamethasone 0.15 mg/kg q6h × 4 days within 12 h (adjusted 30-day death 6% vs 12%) ([PMID: 40113367](https://pubmed.ncbi.nlm.nih.gov/40113367/)).

> "Corticosteroids significantly reduce mortality and neurological sequelae in acute bacterial meningitis (particularly pneumococcal), especially when administered before or with antibiotics." — [PMID: 41675892](https://pubmed.ncbi.nlm.nih.gov/41675892/)

**Anticoagulation** is used for associated cavernous sinus/IJV thrombosis (Lemierre) though evidence remains debated ([PMID: 41330476](https://pubmed.ncbi.nlm.nih.gov/41330476/), [PMID: 42568628](https://pubmed.ncbi.nlm.nih.gov/42568628/)).

**NCIT clinical-intervention terms:** Metronidazole, Ceftriaxone, Cefotaxime, Meropenem, Piperacillin-Tazobactam, Dexamethasone, Surgical Drainage.

---

## Prevention (Section 13)

Prevention is **non-vaccine** (no licensed vaccine targets these anaerobes):

- **Primary:** prompt treatment/source control of predisposing ENT, dental, sinus, and abdominal infections; strict neurosurgical and device asepsis; judicious device management.
- **Secondary:** early recognition of complicated ENT infection and Lemierre-associated thrombophlebitis to prevent CNS extension.
- **Tertiary:** prolonged antibiotics, surgical drainage, and device replacement to prevent relapse/complications.
- **Public health:** dental/oral hygiene, timely otitis media/sinusitis management.

No genetic counseling or carrier/newborn screening applies (non-heritable).

---

## Other Species / Natural Disease (Section 14)

Anaerobes cause naturally occurring disease in animals — **necrobacillosis**. *Fusobacterium necrophorum* (NCBI:txid859) is an opportunistic pathogen causing calf diphtheria, foot rot, and liver abscesses in cattle; its **leukotoxin (Lkt)** is the major virulence factor and a protective antigen, with subsp. *necrophorum* more leukotoxic than subsp. *funduliforme* ([PMID: 30771459](https://pubmed.ncbi.nlm.nih.gov/30771459/)).

> "In animals, it is an opportunistic pathogen frequently associated with necrotic infections, generally called necrobacillosis, such as calf diphtheria, foot rot and liver abscesses in cattle." — [PMID: 30771459](https://pubmed.ncbi.nlm.nih.gov/30771459/)

> "Among several virulence factors, leukotoxin (Lkt) is considered to be a major factor and a protective antigen." — [PMID: 30771459](https://pubmed.ncbi.nlm.nih.gov/30771459/)

Other implicated anaerobes span species: *B. fragilis* (txid817), *Prevotella*, *Parvimonas micra*, *Clostridium perfringens* (txid1502), *Cutibacterium acnes* (txid1747). Comparative pathology: abscess-forming, tissue-necrotizing anaerobic infection is broadly conserved across mammals, but frank anaerobic *meningitis* is documented predominantly in humans; veterinary anaerobic disease more often manifests as abscesses/soft-tissue necrosis. Zoonotic transmission of these commensal anaerobes is not a recognized route of human meningitis.

---

## Model Organisms (Section 15)

There is no dedicated model of anaerobic meningitis, but **rodent bacterial-meningitis models** (Wistar rats; intracisternal *S. pneumoniae* or *K. pneumoniae*) recapitulate the shared downstream pathophysiology: a TNF-α/IL-1β/IL-6/CINC-1 cytokine surge within 6–24 h, BBB disruption, and long-term cognitive/memory impairment ([PMID: 24105840](https://pubmed.ncbi.nlm.nih.gov/24105840/), [PMID: 23085269](https://pubmed.ncbi.nlm.nih.gov/23085269/)). **Anaerobe-specific animal models** exist for *B. fragilis* abscess pathogenesis (mouse/rat intra-abdominal abscess models establishing capsular polysaccharide as the virulence factor; [PMID: 6954635](https://pubmed.ncbi.nlm.nih.gov/6954635/), [PMID: 3865350](https://pubmed.ncbi.nlm.nih.gov/3865350/), [PMID: 3711690](https://pubmed.ncbi.nlm.nih.gov/3711690/)) and for *F. necrophorum* necrobacillosis/leukotoxin ([PMID: 30771459](https://pubmed.ncbi.nlm.nih.gov/30771459/)). **Limitations:** these models capture the inflammatory cascade and virulence-factor biology but not the specific meningeal invasion route of anaerobes in humans. **Resources:** MGI, RGD (rat), and standard laboratory rodent strains; no organoid/iPSC anaerobic-meningitis model is established.

---

## Mechanistic Model / Interpretation

The unifying model is a **two-hit process**: (Hit 1) a barrier-breaching predisposing lesion allows endogenous anaerobic flora to reach the CSF; (Hit 2) subarachnoid replication triggers a stereotyped, TLR-driven innate inflammatory cascade whose intensity — modulated by pathogen virulence factors and host inflammasome/complement genotype — determines the degree of BBB breakdown and neuronal injury. Anaerobe-specific features graft onto this shared backbone: the *B. fragilis* capsule biases toward walled-off abscess (with weak systemic endotoxicity), while *F. necrophorum* biases toward septic thrombophlebitis (Lemierre) and leukotoxin-mediated tissue necrosis. Therapeutically, the model rationalizes the triad of (1) anaerobe-active antibiotics (metronidazole ± β-lactam) to remove the Hit-2 stimulus, (2) source control to remove the Hit-1 nidus, and (3) corticosteroids to blunt the injurious inflammatory amplification.

| Axis | Aerobic/pyogenic meningitis (e.g., pneumococcal) | Anaerobic meningitis |
|---|---|---|
| Frequency | Common | Rare (~2.4% of adult culture-proven) |
| Typical host | Often previously healthy | Predisposed (ENT/neurosurgery/immunocompromise) |
| Presentation | Acute, classic triad | Often subacute/atypical |
| Diagnosis | Routine culture usually positive | Culture low-yield; needs 16S/mNGS |
| Key virulence | Pneumolysin, capsule | B. fragilis capsule; F. necrophorum leukotoxin |
| First-line drug | Ceftriaxone (± vancomycin) | Metronidazole + β-lactam |

---

## Evidence Base

| PMID | Role in report | Key contribution |
|---|---|---|
| [29396061](https://pubmed.ncbi.nlm.nih.gov/29396061/) | Core | Rarity (2.4%), species spectrum, risk factors, mortality/morbidity |
| [32717475](https://pubmed.ncbi.nlm.nih.gov/32717475/) | Core | Low culture yield, contamination, device/procedure risk |
| [41479136](https://pubmed.ncbi.nlm.nih.gov/41479136/) | Core | Pediatric *F. necrophorum*, ENT precursor, complications |
| [42568628](https://pubmed.ncbi.nlm.nih.gov/42568628/) | Supporting | Defines Lemierre syndrome / thrombophlebitis route |
| [21382412](https://pubmed.ncbi.nlm.nih.gov/21382412/) | Diagnostics | CSF lactate diagnostic performance |
| [434970](https://pubmed.ncbi.nlm.nih.gov/434970/) | Treatment | Metronidazole eradication of anaerobic CNS infection |
| [22618789](https://pubmed.ncbi.nlm.nih.gov/22618789/) | Mechanism | TLR→NF-κB/MAPK→oxidative injury cascade |
| [23053059](https://pubmed.ncbi.nlm.nih.gov/23053059/) | Mechanism/modifier | CARD8/NLRP1 inflammasome outcome association |
| [28086930](https://pubmed.ncbi.nlm.nih.gov/28086930/) | Mechanism/modifier | MASP-2 complement worsens outcome |
| [24105840](https://pubmed.ncbi.nlm.nih.gov/24105840/) | Model organism | Rat cytokine surge, memory impairment |
| [6954635](https://pubmed.ncbi.nlm.nih.gov/6954635/) | Virulence | *B. fragilis* capsule = abscess factor |
| [3865350](https://pubmed.ncbi.nlm.nih.gov/3865350/) | Virulence | Capsule antiphagocytic |
| [549184](https://pubmed.ncbi.nlm.nih.gov/549184/) | Virulence | Weak *Bacteroides* LPS endotoxicity |
| [3711690](https://pubmed.ncbi.nlm.nih.gov/3711690/) | Virulence | LPS dose ~5× CP for abscess |
| [15509818](https://pubmed.ncbi.nlm.nih.gov/15509818/) | Phenotype | Frequency of meningitis triad/features |
| [28089421](https://pubmed.ncbi.nlm.nih.gov/28089421/) | Treatment/abscess | Source control, 4–8 wk antibiotics, anaerobes lead abscess |
| [41675892](https://pubmed.ncbi.nlm.nih.gov/41675892/) | Treatment | Corticosteroid benefit/timing |
| [40113367](https://pubmed.ncbi.nlm.nih.gov/40113367/) | Treatment | Pediatric dexamethasone mortality benefit |
| [30771459](https://pubmed.ncbi.nlm.nih.gov/30771459/) | Veterinary | Necrobacillosis, leukotoxin |
| [35692070](https://pubmed.ncbi.nlm.nih.gov/35692070/) / [37775739](https://pubmed.ncbi.nlm.nih.gov/37775739/) | Diagnostics | mNGS for CNS anaerobes |
| [41330476](https://pubmed.ncbi.nlm.nih.gov/41330476/) | Case/complication | *F. nucleatum* meningitis + cavernous sinus thrombosis |
| [31838318](https://pubmed.ncbi.nlm.nih.gov/31838318/) | Epidemiology | Neonatal anaerobic meningitis rarity |

**Evidence source types:** the mechanism is largely extrapolated from broader bacterial-meningitis literature (human cohort + rodent models + in vitro virulence studies), while anaerobe-specific clinical data come from small human case series and single-/multi-center cohorts.

---

## Limitations and Knowledge Gaps

1. **No anaerobe-specific mechanistic studies of meningitis** — the inflammatory cascade is inferred from pneumococcal/Klebsiella models, not from anaerobe-induced meningitis directly.
2. **Small sample sizes** — the largest dedicated adult series has only 13 cases; pediatric data 27 cases. No prospective trials of anaerobic meningitis specifically exist.
3. **Diagnostic under-ascertainment** — routine practice omits anaerobic culture, so true incidence is likely underestimated; molecular detection is reshaping the epidemiology.
4. **Corticosteroid evidence is indirect** — benefit is established for pneumococcal/general bacterial meningitis, not specifically anaerobic; TBM data show genotype-dependent heterogeneity ([PMID: 41540106](https://pubmed.ncbi.nlm.nih.gov/41540106/)).
5. **No genetic architecture** — beyond a few inflammasome/complement modifiers, host susceptibility genetics are unexplored.
6. **Optimal antibiotic duration, and the role/timing of anticoagulation** in Lemierre-associated CNS disease remain undefined.

---

## Proposed Follow-up Experiments / Actions

1. **Multicenter registry with routine mNGS/16S** on all culture-negative meningitis CSF to establish true incidence and species distribution of anaerobic meningitis.
2. **Prospective validation of CSF lactate + molecular panels** as a rapid rule-in pathway for anaerobic meningitis, with cost-effectiveness analysis.
3. **Develop an anaerobe-specific meningitis model** (e.g., intracisternal *F. necrophorum* or *B. fragilis*) to directly test the TLR/inflammasome cascade and the effect of capsule/leukotoxin knockouts on CNS injury.
4. **Genotype-stratified adjunctive corticosteroid evaluation** (CARD8/NLRP1/MASP-2) in bacterial meningitis cohorts including anaerobic cases, mirroring the LTA4H-stratified TBM approach.
5. **Structured outcome study** of anticoagulation timing in anaerobic meningitis complicated by cavernous sinus/IJV thrombosis.
6. **Preventive audit** of ENT/odontogenic source control and neurosurgical device asepsis protocols to quantify modifiable risk.

---

*Report compiled from 5 investigation iterations, 11 confirmed findings, and 56 reviewed papers. Evidence is graded by source type (human clinical cohort/case series, model organism, in vitro virulence, computational/meta-analytic). Anaerobic meningitis is a non-heritable, acquired infectious disease; sections pertaining to Mendelian genetics, inheritance, and genetic screening are marked not applicable throughout.*


## Artifacts

- [OpenScientist final report](Anaerobic_Meningitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Anaerobic_Meningitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 18 |
| Quoted claims found in source | 18 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 28 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 24 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001945` (1 mention) - the report calls it "Symptom"; HP calls it **Fever**
- `HP:0002315` (1 mention) - the report calls it "Symptom"; HP calls it **Headache**
- `HP:0011446` (1 mention) - the report calls it "Symptom/sign"; HP calls it **Abnormality of mental function**
- `HP:0001250` (1 mention) - the report calls it "Clinical sign"; HP calls it **Seizure**
- `HP:0034332` (1 mention) - the report calls it "Sign"; HP calls it **Cognitive regression**
- `HP:0000613` (1 mention) - the report calls it "Symptom"; HP calls it **Photophobia**
- `HP:0025432` (1 mention) - the report calls it "CSF pleocytosis"; HP calls it **Acanthoma**
- `CL:0000775` (3 mentions) - the report calls it "neutrophil", "Tissue/cell level:** vascular endothelium of the BBB, neutrophils"; CL calls it **neutrophil**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0038123` (2 mentions) - the report calls it "Toll-like receptor signaling"; GO calls it **toll-like receptor TLR1:TLR2 signaling pathway**
- `CHEBI:25812` (1 mention) - the report calls it "peroxynitrite"; CHEBI calls it **ozone**, and lists "trioxygene" among its other names
- `UBERON:0001359` (1 mention) - the report calls it "CSF"; UBERON calls it **cerebrospinal fluid**, and lists "CSF" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000775` - called "neutrophil", "Tissue/cell level:** vascular endothelium of the BBB, neutrophils"