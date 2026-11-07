---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T20:09:25.834133'
end_time: '2026-10-31T20:36:08.594885'
duration_seconds: 1602.76
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Craniofrontonasal Syndrome
  mondo_id: MONDO:0010570
  category: Mendelian
  causal_genes: EFNB1
  omim_id: OMIM:304110
  synonyms: craniofrontonasal dysplasia, X-linked dominant; CFND; CFNS; Craniofrontonasal
    Dysplasia
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
citation_count: 21
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 21
  on_topic: 20
  validator_version: 0.4.0
term_validation:
  total_terms: 29
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 3
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: NCIT:C15312
    reported_labels:
    - Supportive:** speech/language therapy
    ontology_label: Radiation Dosimetry
  labels_variant: 6
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
  path: Craniofrontonasal_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Craniofrontonasal_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Craniofrontonasal Syndrome
- **MONDO ID:** MONDO:0010570 (if available)
- **Causal gene(s):** EFNB1
- **OMIM:** OMIM:304110
- **Synonyms:** craniofrontonasal dysplasia, X-linked dominant; CFND; CFNS; Craniofrontonasal Dysplasia
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Craniofrontonasal Syndrome** covering all of the
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

# Craniofrontonasal Syndrome (CFNS): Comprehensive Disease Characterization Report

**Disease:** Craniofrontonasal Syndrome (CFNS) / Craniofrontonasal Dysplasia (CFND)
**MONDO:** MONDO:0010570 | **OMIM:** 304110 | **Orphanet:** ORPHA:1520 | **UMLS:** C0431147
**Causal gene:** **EFNB1** (ephrin-B1), Xq13.1 — HGNC:3226, NCBI Gene 1947, Ensembl ENSG00000090776, UniProt P98172, gene OMIM 300035
**Category:** Mendelian, X-linked dominant (with paradoxical sex-reversed severity)

---

## Summary

**Craniofrontonasal syndrome is a rare X-linked developmental craniofacial disorder caused by loss-of-function variants in the gene EFNB1, which encodes the transmembrane Eph-receptor ligand ephrin-B1.** The condition is defined clinically by coronal craniosynostosis (uni- or bilateral), frontonasal dysplasia, orbital hypertelorism, a bifid or grooved nasal tip, longitudinal nail ridging/splitting, wiry ("woolly") hair, and a range of minor skeletal and limb anomalies. Intelligence is usually normal. The gene was identified in 2004, and CFNS remains the only human disease known to be caused by mutation in the ephrin/Eph receptor signaling system.

The disorder's most striking and scientifically important feature is its **paradoxical inheritance**: heterozygous females are characteristically *more* severely affected than hemizygous males, inverting the usual pattern of X-linked disease. This paradox is explained by **cellular interference** driven by random X-inactivation. In a heterozygous female, X-inactivation produces a mosaic of ephrin-B1-positive and ephrin-B1-negative cells; the resulting mismatch at tissue boundaries triggers aberrant Eph/ephrin-mediated cell segregation and disrupts normal tissue-boundary formation at the developing coronal suture. A hemizygous male, lacking ephrin-B1 uniformly, has no mosaic mismatch and so relies on an alternative boundary-maintenance mechanism, producing a milder phenotype. This model is supported by direct evidence from patient iPSC-derived neuroepithelial cells, Efnb1 mouse models, and the observation that mosaic males (not true hemizygotes) develop a severe, female-like phenotype.

Management is entirely **supportive and surgical** — there is no pharmacologic or gene-targeted therapy. Multidisciplinary staged craniofacial reconstruction (fronto-orbital advancement, cranial vault remodeling, hypertelorism correction by facial bipartition or box osteotomy) addresses the structural anomalies, supplemented by speech/language therapy, audiology, and developmental/educational support. Life expectancy is normal and intelligence is usually preserved; disease burden stems from craniofacial deformity, variable speech/language delay, and the cumulative surgical burden rather than from mortality.

---

## Key Findings

### 1. EFNB1 loss-of-function is the sole cause of CFNS

CFNS (OMIM 304110; MONDO:0010570) is an X-linked developmental disorder caused by loss-of-function variants in **EFNB1** at Xq13.1, encoding the transmembrane Eph-receptor ligand **ephrin-B1**. The majority of mutations create premature termination codons (nonsense, frameshift, splice-site), while missense variants cluster in the extracellular ephrin domain that mediates Eph-receptor recognition and higher-order complex formation. By 2005, at least 46 distinct EFNB1 mutations had been catalogued.

> *"Using a combination of positional approach and candidate gene strategy the EFNB1 gene in Xq12 was identified as the major causative gene of this condition. So far, 46 EFNB1 mutations have been detected in CFNS patients. The majority of the mutations lead to premature termination codons."* — [PMID: 16143553](https://pubmed.ncbi.nlm.nih.gov/16143553/)

> *"Craniofrontonasal syndrome (CFNS) is an X-linked developmental disorder caused by loss of function variants (LOFVs) in the ephrin B1 (EFNB1) gene located on Xq13.1."* — [PMID: 39643662](https://pubmed.ncbi.nlm.nih.gov/39643662/)

**Variant types observed** include nonsense (e.g., p.R66X, p.Trp12*, p.Glu210*), frameshift (e.g., c.614_615delCT, p.Tyr73Metfs*86), splice-site (c.406+2T>C), missense (p.P54L, p.T111I, p.G151S, p.M158T), whole/partial-gene deletions (e.g., deletion of exons 2–5; exons 1–5), and rare structural variants — including a pericentric **inv(X)(p22.2q13.1)** that separates EFNB1 from a downstream enhancer, causing disease without altering the coding sequence ([PMID: 39643662](https://pubmed.ncbi.nlm.nih.gov/39643662/)). Functional work shows truncating alleles are handled by nonsense-mediated decay in cell-type-specific ways, and that missense alleles such as p.P54L impair Eph-receptor-mediated clustering and reduce ephrin-B1 Tyr324/Tyr329 phosphorylation (reverse signaling) ([PMID: 20565770](https://pubmed.ncbi.nlm.nih.gov/20565770/)).

### 2. Paradoxical X-linked inheritance: females more severely affected than males

CFNS shows **sex-reversed severity**. Heterozygous females characteristically have frontonasal dysplasia, coronal craniosynostosis, facial asymmetry, hypertelorism, bifid nasal tip, and minor malformations; hemizygous males are usually only mildly affected (often hypertelorism alone). This inverts the typical X-linked pattern and is explained by random X-inactivation generating **functional mosaicism** for ephrin-B1.

> *"The more severe manifestation in females may be explained by cellular interference that is caused by the combination of ephrin ligand/receptor promiscuity and the consequences of random X inactivation in distinct cellular compartments."* — [PMID: 16143553](https://pubmed.ncbi.nlm.nih.gov/16143553/)

The decisive experimental test came from sporadic **males who present with a severe, female-like phenotype**. Twigg et al. (2013) hypothesized these males were mosaic and confirmed it: in all six sporadic severe males studied, mosaicism for EFNB1 mutations was demonstrated (15–69% mutant cells across tissues). This shows that it is **mosaicism — not hemizygosity — that produces the severe phenotype**, providing direct evidence for cellular interference.

> *"males occasionally present with a more severe female-like CFNS phenotype. We hypothesized that such individuals might be mosaic for EFNB1 mutations and investigated this possibility in multiple tissue samples from six sporadically presenting males"* — [PMID: 23335590](https://pubmed.ncbi.nlm.nih.gov/23335590/)

### 3. Mechanism: ephrin-B1 mosaicism drives Eph/ephrin-mediated cell segregation at tissue boundaries

Patient-derived human iPSCs provide direct human evidence: mosaicism for EPHRIN-B1 expression (induced by random X-inactivation) drives **robust cell segregation in human neuroepithelial cells**, confirming that Eph/ephrin-mediated cell sorting is relevant to human CFNS pathogenesis.

> *"mosaicism for EPHRIN-B1 expression induced by random X inactivation in heterozygous females results in robust cell segregation in human neuroepithelial cells, thus supplying experimental evidence that Eph/ephrin-mediated cell segregation is relevant to pathogenesis in human CFNS patients"* — [PMID: 28238796](https://pubmed.ncbi.nlm.nih.gov/28238796/)

In Efnb1 heterozygous mice, ephrin-B1 mosaicism causes cell sorting and more severe craniofacial phenotypes than in hemizygous males. Niethamer et al. (2020) showed ephrin-B1 regulates cell segregation independently in early neural development and later in craniofacial development, with cell sorting correlating with the emergence of quantitative face-shape differences. Critically, mosaicism **exacerbates loss-of-function rather than creating a neomorphic (gain-of-function) effect**.

> *"heterozygous embryos are quantitatively more severely affected, indicating that Efnb1 mosaicism exacerbates loss of function phenotypes rather than having a neomorphic effect"* — [PMID: 32092051](https://pubmed.ncbi.nlm.nih.gov/32092051/)

### 4. Core phenotype in affected females (with HPO terms)

Universal/near-universal features in affected females include **orbital hypertelorism** (HP:0000316), **wide nasal bridge** (HP:0000431), and **bifid/grooved nasal tip** (HP:0000456). Very common features include **coronal craniosynostosis** (uni- HP:0004440 / bilateral HP:0004442) producing brachycephaly (HP:0000248) and frontonasal dysplasia, facial asymmetry/plagiocephaly, and frontal bossing (HP:0002007). Characteristic ectodermal signs are **longitudinal nail ridging/splitting** (HP:0001807) and **wiry/curly "woolly" hair** (HP:0002212). Skeletal/limb features include cutaneous syndactyly (HP:0012725), broad/bifid halluces/thumbs, polydactyly (HP:0010442), clavicular/shoulder anomalies, and scoliosis. Other reported findings: variable cleft lip/palate, short/webbed neck, dental malocclusion, Sprengel deformity, and rare diaphragmatic hernia. **Intelligence is usually normal.**

> *"It is characterized by coronal synostosis, facial asymmetry, hypertelorism, bifid nasal tip, woolly hair, longitudinal nail ridging, and skeletal anomalies in heterozygous females. Hemizygous males paradoxically display a less severe phenotype."* — [PMID: 40094327](https://pubmed.ncbi.nlm.nih.gov/40094327/)

> *"It is characterized by brachycephaly, frontonasal dysplasia, palate/lip defects, dental malocclusion, short neck, split nails, syndactyly, toe and finger defects, and minor skeletal defects. Intelligence is usually unaffected."* — [PMID: 27194971](https://pubmed.ncbi.nlm.nih.gov/27194971/)

Van den Elzen et al. (2014, 23 patients, 21F/2M) found that **hypertelorism, longitudinal nail ridging/splitting, mild webbed neck, and clinodactyly of toes were present in ALL patients** — the fully-penetrant core — with bifid nasal tip (91%), columellar indentation (91%), and low breast implantation (90%) frequent.

> *"Hypertelorism, longitudinal ridging and/or splitting of nails, a (mild) webbed neck and a clinodactyly of one or more toes were the only consistent features observed in all patients."* — [PMID: 24281372](https://pubmed.ncbi.nlm.nih.gov/24281372/)

#### Phenotype frequency table

| Phenotype | HPO term | Frequency | Source |
|---|---|---|---|
| Orbital hypertelorism | HP:0000316 | Universal | [PMID: 24281372](https://pubmed.ncbi.nlm.nih.gov/24281372/) |
| Longitudinal nail ridging/splitting | HP:0001807 | Universal | [PMID: 24281372](https://pubmed.ncbi.nlm.nih.gov/24281372/) |
| Mild webbed neck | HP:0000465 | Universal | [PMID: 24281372](https://pubmed.ncbi.nlm.nih.gov/24281372/) |
| Clinodactyly of toes | HP:0001863 | Universal | [PMID: 24281372](https://pubmed.ncbi.nlm.nih.gov/24281372/) |
| Bifid nasal tip | HP:0000456 | ~91% | [PMID: 24281372](https://pubmed.ncbi.nlm.nih.gov/24281372/) |
| Coronal craniosynostosis | HP:0004440/HP:0004442 | Very common (females) | [PMID: 40094327](https://pubmed.ncbi.nlm.nih.gov/40094327/) |
| Woolly/wiry hair | HP:0002212 | Common | [PMID: 40094327](https://pubmed.ncbi.nlm.nih.gov/40094327/) |
| Facial asymmetry | HP:0000324 | Common (females) | [PMID: 40094327](https://pubmed.ncbi.nlm.nih.gov/40094327/) |
| Cutaneous syndactyly | HP:0012725 | Variable | [PMID: 27194971](https://pubmed.ncbi.nlm.nih.gov/27194971/) |
| Normal intelligence | — | Usual | [PMID: 27194971](https://pubmed.ncbi.nlm.nih.gov/27194971/) |

### 5. Neurodevelopmental outcome: generally normal IQ but frequent speech/language difficulties; large deletions worsen cognition

In the Oxford cohort of 25 female EFNB1-mutation patients (mean follow-up 12.6 y; Dupré et al. 2020), full-scale IQ ranged 69–100. Speech/language difficulties were common: receptive 57% (4/7), expressive 88% (8/9), speech 55% (6/11); 41% (7/17) required additional educational support. Importantly, **contiguous-gene deletions extending beyond EFNB1** were associated with more severe neurodevelopmental impairment.

> *"57% had receptive language difficulties (n = 4/7) and 88% had expressive language difficulties (n = 8/9). 55% presented with speech difficulties (n = 6/11)."* — [PMID: 32371695](https://pubmed.ncbi.nlm.nih.gov/32371695/)

> *"Three children had deletions extending beyond the EFNB1 gene; the 2 with available data presented with speech, language, or cognitive delay."* — [PMID: 32371695](https://pubmed.ncbi.nlm.nih.gov/32371695/)

### 6. Ephrin-B1 is a coronal-suture boundary marker (landmark 2004 identification)

The original gene-identification work (Twigg et al. 2004; Wieland et al. 2004) established the developmental mechanism. The orthologous mouse **Efnb1 is expressed in frontonasal neural crest and demarcates the position of the future coronal suture.** Females with CFNS do not show markedly skewed X-inactivation in blood or cranial periosteum, indicating ephrin-B1 loss does not compromise cell viability; instead, patchwork mosaic loss disturbs tissue-boundary formation.

> *"the orthologous Efnb1 gene is expressed in the frontonasal neural crest and demarcates the position of the future coronal suture"* — [PMID: 15166289](https://pubmed.ncbi.nlm.nih.gov/15166289/)

> *"patchwork loss of ephrin-B1 disturbs tissue boundary formation at the developing coronal suture, whereas in males deficient in ephrin-B1, an alternative mechanism maintains the normal boundary"* — [PMID: 15166289](https://pubmed.ncbi.nlm.nih.gov/15166289/)

Wieland et al. (2004) independently confirmed causation, reporting a deletion of exons 2–5 and the missense variants P54L and T111I located in the multimerization/receptor-interaction motifs of the extracellular domain ([PMID: 15124102](https://pubmed.ncbi.nlm.nih.gov/15124102/)).

### 7. Mutational origin: paternal germline bias, frequent mosaicism, and the paucity of carrier males

Twigg et al. (2006) surveyed 59 CFNS families: of 17 germline mutations with determinable parental origin, **15 (88%) arose from the father**; somatic mosaicism was demonstrated in 6 of 53 informative families. The paternal-origin bias means de novo mutations arising in the paternal germline are transmitted on the paternal X and so present as **affected daughters rather than carrier sons** — which, combined with the reduced reproductive fitness of affected females, explains why carrier/affected males are underrepresented in CFNS pedigrees.

> *"Somatic mosaicism was demonstrated in 6 of 53 informative families, and, of 17 germline mutations in individuals for whom the parental origin of mutation could be demonstrated, 15 arose from the father."* — [PMID: 16685650](https://pubmed.ncbi.nlm.nih.gov/16685650/)

> *"the major factor accounting for the relative scarcity of carrier males is the bias toward mutations in the paternal germline (which present as affected female offspring) combined with reduced reproductive fitness in affected females"* — [PMID: 16685650](https://pubmed.ncbi.nlm.nih.gov/16685650/)

### 8. Mouse models: ephrin-B1 acts cell-autonomously in neural crest via forward AND reverse (PDZ) signaling

Davy, Aubin & Soriano (2004) generated efnb1-mutant mouse lines. Complete ablation caused perinatal lethality with defects in neural crest cell (NCC)-derived tissues, incomplete body-wall closure, and abnormal skeletal patterning. Conditional deletion showed ephrin-B1 acts **cell-autonomously in NCCs** to control their migration. A mutation restricted to the PDZ-binding domain demonstrated that ephrin-B1-induced **reverse signaling** is specifically required in NCCs. Thus ephrin-B1 functions both as a ligand (forward signaling to Eph receptors) and as a receptor (reverse signaling) in a tissue-specific manner.

> *"Complete ablation of ephrin-B1 resulted in perinatal lethality associated with a range of phenotypes, including defects in neural crest cell (NCC)-derived tissues, incomplete body wall closure, and abnormal skeletal patterning."* — [PMID: 15037550](https://pubmed.ncbi.nlm.nih.gov/15037550/)

> *"a mutation in the PDZ binding domain indicated that ephrin-B1-induced reverse signaling is required in NCCs. Our results demonstrate that ephrin-B1 acts both as a ligand and as a receptor in a tissue-specific manner"* — [PMID: 15037550](https://pubmed.ncbi.nlm.nih.gov/15037550/)

Efnb1 heterozygous female mice develop polydactyly and skeletal defects more severe than hemizygous males, driven by ephrin-B1 mosaicism / cell sorting (Compagni 2003; Bush & Soriano; Niethamer 2020), recapitulating the paradoxical heterozygote > hemizygote severity of human CFNS.

### 9. Management, survival, and classification

No pharmacologic or gene-targeted therapy exists; management is **surgical and supportive**. Craniofacial reconstruction addresses craniosynostosis (fronto-orbital advancement, total cranial vault remodeling in infancy/childhood, especially for raised intracranial pressure) and hypertelorism (facial bipartition or box osteotomy, typically deferred to later childhood/adolescence once facial skeletal growth is largely complete). Raposo-Amaral et al. (2021) reported 10 late-presenting CFND patients (all female) treated by facial bipartition or box osteotomy, with complications limited to one frontal-bone infection and one CSF leak (mean age 13.4 y).

> *"All patients in this study underwent hypertelorism correction by facial bipartition or box osteotomy. A total of ten late presenting CFND patients (all female) were treated at our hospital during the study period."* — [PMID: 33864106](https://pubmed.ncbi.nlm.nih.gov/33864106/)

Multidisciplinary care — craniofacial surgery, clinical genetics, speech/language therapy, audiology, and developmental/educational support — is recommended, reflecting the frequent need for educational support.

> *"The complex, multifactorial presentation of patients with CFNS contributed to 41% (n = 7/17) of patients requiring additional educational support."* — [PMID: 32371695](https://pubmed.ncbi.nlm.nih.gov/32371695/)

CFNS is classified among the **syndromic craniosynostoses** (alongside Apert [FGFR2], Crouzon [FGFR2], Pfeiffer [FGFR1/2], Muenke [FGFR3], Saethre-Chotzen [TWIST1]), distinguished by its X-linked EFNB1 etiology and female-predominant severity.

> *"The most common syndromes are Apert, Crouzon, Pfeiffer, Muenke, and Saethre-Chotzen syndromes and craniofrontonasal syndrome. Each of these syndromes has distinct genetic mutations that contribute to their development. Mutations in genes such as FGFR, TWIST, and EFNB1 have been identified"* — [PMID: 38222144](https://pubmed.ncbi.nlm.nih.gov/38222144/)

---

## Section-by-Section Detail

### 1. Disease Information
CFNS is a congenital, X-linked developmental craniofacial dysplasia. **Identifiers:** MONDO:0010570; OMIM phenotype 304110; Orphanet ORPHA:1520; UMLS C0431147; MeSH mapped under craniofacial abnormalities/craniosynostoses; ICD-10 best fit Q75.8/Q87.0; ICD-11 under LD2 (developmental anomalies of craniofacial bones). **Synonyms:** craniofrontonasal dysplasia (CFND), craniofrontonasal syndrome (CFNS), CFNS, craniofrontonasal dysplasia X-linked. Information is derived largely from **aggregated disease-level resources** (OMIM/Orphanet/HPO/MGI) plus individual-patient clinical/molecular case series and cohorts; no EHR-level individual data were used.

### 2. Etiology
**Causal factor:** genetic — loss-of-function variants in **EFNB1** (Xq13.1). **Genetic risk factors:** the EFNB1 pathogenic variant itself is both necessary and sufficient; contiguous-gene deletions extending beyond EFNB1 add neurodevelopmental burden ([PMID: 32371695](https://pubmed.ncbi.nlm.nih.gov/32371695/)). **Sex** is the dominant modifier of severity through X-inactivation mosaicism (female > male). **No environmental, infectious, lifestyle, or protective factors** are established; there are no known gene–environment interactions. The disease is monogenic and highly penetrant in females.

### 3. Phenotypes
See Finding 4 and the frequency table above. Onset is **congenital** (craniofacial features present at birth). Severity is **variable** even within families and between monozygotic twins carrying identical variants (e.g., discordant MZ twins with p.Glu210*; [PMID: 34174922](https://pubmed.ncbi.nlm.nih.gov/34174922/)). The structural features are **stable/non-progressive** (developmental, not degenerative), though craniosynostosis-related deformity and raised intracranial pressure can worsen with growth until surgically corrected. **Quality-of-life impact** derives mainly from facial appearance, the surgical burden, and speech/language difficulties; intelligence and life expectancy are preserved.

### 4. Genetic / Molecular Information
**Causal gene:** EFNB1 (HGNC:3226, NCBI Gene 1947, UniProt P98172). **Variant classes:** nonsense, frameshift, splice-site (collectively the majority, producing premature termination codons), missense (clustered in the extracellular ephrin domain / receptor-interaction & multimerization motifs), whole/partial-gene deletions, and rare structural variants (inv(X) separating EFNB1 from its enhancer). **Classification:** pathogenic/likely pathogenic per ACMG for recurrent and functionally validated alleles. **Allele frequency:** pathogenic alleles are essentially absent from population databases (1000 Genomes, ExAC, gnomAD) ([PMID: 37212007](https://pubmed.ncbi.nlm.nih.gov/37212007/)). **Origin:** germline (frequently de novo, paternal-biased) and frequent somatic/germline mosaicism. **Functional consequence:** loss of function; mosaicism exacerbates LoF rather than acting as a neomorph. **Modifier:** deletion size (contiguous-gene deletions worsen cognition). No disease-specific epigenetic mechanism is established.

### 5. Environmental Information
**Not applicable.** CFNS is a monogenic Mendelian disorder with no documented environmental, lifestyle, toxic, or infectious contributors.

### 6. Mechanism / Pathophysiology — causal chain

```
1. Loss-of-function variant in EFNB1 (Xq13.1)
        │  results in →
2. Reduced/absent functional ephrin-B1 protein on the cell surface
        │  (in heterozygous females) random X-inactivation →
3. MOSAIC tissue: patches of ephrin-B1-positive and ephrin-B1-negative cells
        │  leads to →
4. Mismatched Eph receptor / ephrin-B1 bidirectional (forward + reverse) signaling
   across cell populations  [impaired reverse signaling: ↓Tyr324/329 phosphorylation]
        │  drives →
5. Aberrant Eph/ephrin-mediated cell segregation / cell sorting
   (demonstrated in patient iPSC neuroepithelium and Efnb1 het mice)
        │  disrupts →
6. Tissue-boundary formation at the developing coronal suture
   (ephrin-B1 marks the future coronal suture in frontonasal neural crest)
        │  results in →
7. Coronal craniosynostosis, frontonasal dysplasia, hypertelorism,
   bifid nasal tip, facial asymmetry + skeletal/ectodermal anomalies

   BRANCH (males): uniform ephrin-B1 loss → NO mosaic mismatch →
   alternative boundary mechanism maintains boundary → MILD phenotype
```

**Molecular pathway:** Eph/ephrin bidirectional signaling (GO:0048013 ephrin receptor signaling pathway). **Cellular processes:** cell segregation/sorting (GO:0016477 cell migration; GO:0045216 cell-cell junction organization), tissue-boundary formation, neural crest cell migration (GO:0001755). **Protein dysfunction:** loss of ephrin-B1 ligand function and impaired reverse (PDZ-domain) signaling. **Cell types:** cranial neural crest cells (CL:0000333 migratory neural crest cell), neuroepithelial cells (CL:0000710), osteoblasts/suture mesenchyme. The initiating lesion is the EFNB1 mutation (upstream); cell segregation and boundary disruption are the critical intermediate steps; craniofacial dysmorphology is the downstream clinical output. No metabolic, immune, or infectious mechanism is implicated.

### 7. Anatomical Structures Affected
**Primary organ/structure:** skull and facial skeleton — coronal suture (UBERON:0000210), frontal/frontonasal region, orbit (UBERON:0001697) with hypertelorism, nasal structures (bifid nasal tip). **Body systems:** skeletal/craniofacial; integumentary (nails UBERON:0001705, hair); occasionally musculoskeletal limb (digits), neck. **Tissue/cell level:** cranial neural crest-derived mesenchyme, suture osteogenic fronts. **Subcellular:** plasma membrane (ephrin-B1 is a transmembrane protein; GO:0005886) and its cytoplasmic PDZ-binding tail. **Lateralization:** coronal synostosis and plagiocephaly are frequently **unilateral/asymmetric**, reflecting the stochastic mosaic nature of the underlying defect.

### 8. Temporal Development
**Onset:** congenital; craniofacial anomalies are present at birth and often detected prenatally in severe cases. **Course:** developmental and non-progressive at the molecular level; secondary deformity and raised intracranial pressure can evolve with skull growth. **Critical periods:** embryonic neural crest migration and coronal-suture boundary formation (the window in which ephrin-B1 mosaicism acts); for intervention, infancy/early childhood for synostosis/ICP, and later childhood/adolescence for hypertelorism correction once facial growth is substantially complete. **Duration:** chronic/lifelong structural condition.

### 9. Inheritance and Population
**Inheritance:** X-linked, with paradoxical female-predominant severity. **Penetrance:** high in females (core features fully penetrant in some series), low/mild in hemizygous males. **Expressivity:** highly variable (including discordant MZ twins). **De novo rate:** high, with **~88% paternal germline origin**; frequent somatic/germline mosaicism. **Carrier males are scarce**, explained by paternal-origin bias plus reduced female reproductive fitness. **Epidemiology:** rare (Orphanet-listed rare disease); precise prevalence/incidence are not well established. No founder effect, consanguinity role, or ethnic predilection is established; cases are reported worldwide. **Sex ratio:** clinically affected individuals are predominantly female.

### 10. Diagnostics
**Clinical diagnosis** rests on the characteristic gestalt (hypertelorism, bifid nasal tip, coronal synostosis, nail ridging, woolly hair) in a female. **Imaging:** CT/3D-CT of the skull documents coronal synostosis and craniofacial morphology; MRI may reveal associated CNS findings (e.g., enlarged cisterna magna). **Confirmatory genetic testing:** single-gene EFNB1 sequencing, targeted NGS panels (craniosynostosis panels including EFNB1), or trio whole-exome sequencing; MLPA/qPCR or chromosomal microarray to detect EFNB1 deletions and contiguous-gene deletions. In silico tools (REVEL, AlphaFold/AlphaFold3 modeling, docking/MD) support VUS classification ([PMID: 40816004](https://pubmed.ncbi.nlm.nih.gov/40816004/), [PMID: 37212007](https://pubmed.ncbi.nlm.nih.gov/37212007/)). **Differential diagnosis:** frontonasal dysplasia (ALX1/ALX3/ALX4), other causes of orbital hypertelorism (Teebi hypertelorism syndrome), Greig cephalopolysyndactyly (GLI3), and FGFR-related craniosynostoses (Apert/Crouzon/Pfeiffer/Muenke) and Saethre-Chotzen (TWIST1). EFNB1 testing plus the female > male severity pattern distinguishes CFNS.

### 11. Outcome / Prognosis
**Life expectancy is normal**; **intelligence is usually normal** (though speech/language difficulties are common and some patients require educational support). **Mortality** is not disease-driven. **Morbidity** stems from craniofacial deformity, potential raised intracranial pressure from synostosis, variable neurodevelopmental/speech issues, and the cumulative surgical burden. **Prognostic factors:** deletion size (contiguous-gene deletions worsen neurodevelopmental outcome) and severity of synostosis/ICP. Rare severe complications have been reported (e.g., co-occurring myelomeningocele/Chiari II; diaphragmatic hernia; a case of necrotizing enterocolitis from mesenteric thrombosis).

### 12. Treatment
**No pharmacologic or gene-targeted therapy** exists. Management is **surgical + supportive/multidisciplinary**:
- **Fronto-orbital advancement** and **total cranial vault remodeling** (infancy/childhood) for coronal synostosis and raised ICP — NCIT: Cranial Vault Remodeling, Fronto-orbital Advancement.
- **Hypertelorism correction** by **facial bipartition** or **box osteotomy** (later childhood/adolescence) — NCIT: Osteotomy, Craniofacial Reconstruction.
- **Soft-tissue refinement:** medial canthopexy, local flaps ([PMID: 27740959](https://pubmed.ncbi.nlm.nih.gov/27740959/)).
- **Supportive:** speech/language therapy (NCIT:C15312), audiology, developmental/educational support, genetic counseling (NCIT:C15834).
No clinical trials of disease-modifying therapy are available; treatment outcomes from surgical series are generally favorable with low complication rates.

### 13. Prevention
No primary prevention exists (monogenic congenital disorder). **Genetic counseling** is central given X-linked inheritance, high de novo/paternal-origin rate, and mosaicism. **Reproductive options:** prenatal diagnosis and **preimplantation genetic testing for monogenic disorders (PGT-M)** have been used successfully to block transmission, including SNP-linkage PGT-M for a large EFNB1 deletion ([PMID: 41811039](https://pubmed.ncbi.nlm.nih.gov/41811039/)). Cascade testing of at-risk relatives and prenatal imaging/molecular testing constitute secondary prevention. Tertiary prevention = staged surgical correction and monitoring for raised ICP.

### 14. Other Species / Natural Disease
The orthologous gene is mouse **Efnb1** (NCBI Gene 13641; Mus musculus, NCBI Taxon 10090). No naturally occurring companion-animal or wildlife CFNS disease is established (not catalogued in OMIA). Comparative biology relies on engineered mouse models (below). Evolutionary conservation of Eph/ephrin boundary-formation mechanisms is high across vertebrates. No zoonotic potential (non-infectious disorder).

### 15. Model Organisms
**Mouse (Mus musculus, NCBI Taxon 10090)** is the principal model. **Models:** Efnb1 null (knockout; perinatal lethal with NCC/body-wall/skeletal defects), conditional/tissue-specific deletions (cell-autonomous NCC role), PDZ-binding-domain mutants (isolate reverse signaling), and heterozygous females (recapitulate mosaic cell sorting and heterozygote > hemizygote severity). **Human iPSC-derived neuroepithelial cells** from CFNS patients model mosaic cell segregation in vitro. **Phenotype recapitulation:** mouse models reproduce craniofacial dysmorphology, skeletal/limb anomalies, and the paradoxical sex-reversed severity — strong recapitulation of core disease biology. **Limitations:** complete nulls are perinatal-lethal (limiting adult study); species differences in craniofacial morphology; incomplete capture of human speech/cognitive features. **Resources:** MGI, IMPC.

---

## Mechanistic Model / Interpretation

The unifying theme of CFNS is that **the disease is caused not by cell-intrinsic loss of ephrin-B1 per se, but by the juxtaposition of cells with and without ephrin-B1** — i.e., mosaicism, not deficiency, is the pathogenic driver. This is why heterozygous females (mosaic) are more severely affected than hemizygous males (uniformly deficient), and why sporadic males who are *somatically mosaic* phenocopy the severe female presentation.

```
   UNIFORM ephrin-B1 LOSS (hemizygous male)      MOSAIC ephrin-B1 (heterozygous female
   ──────────────────────────────────────        OR mosaic male)
   all cells "−"  →  no boundary mismatch         "+"/"−" patches → Eph/ephrin mismatch
   alternative boundary mechanism holds           → cell segregation at wrong positions
   → MILD phenotype                                → disrupted coronal-suture boundary
                                                   → SEVERE craniofacial dysmorphology
```

The upstream lesion (EFNB1 LoF) is the same; the downstream clinical severity is governed by the *tissue architecture of mosaicism*. Experimental proof spans three systems — human iPSC neuroepithelium (cell segregation), Efnb1 mouse (cell sorting correlates with face-shape change; mosaicism exacerbates LoF), and clinical genetics (mosaic severe males) — making this one of the best-worked-out examples of "cellular interference" in human genetics.

---

## Evidence Base

| PMID | Role | Key contribution |
|---|---|---|
| [16143553](https://pubmed.ncbi.nlm.nih.gov/16143553/) | Review | EFNB1 as causal gene; 46 mutations; cellular interference concept |
| [15166289](https://pubmed.ncbi.nlm.nih.gov/15166289/) | Landmark | Gene identification; ephrin-B1 marks coronal suture; boundary model |
| [15124102](https://pubmed.ncbi.nlm.nih.gov/15124102/) | Landmark | Independent confirmation (del exons 2–5; P54L, T111I) |
| [23335590](https://pubmed.ncbi.nlm.nih.gov/23335590/) | Key mechanism | Mosaic severe males — direct evidence for cellular interference |
| [28238796](https://pubmed.ncbi.nlm.nih.gov/28238796/) | Human iPSC | Ephrin-B1 mosaicism drives cell segregation in human neuroepithelium |
| [32092051](https://pubmed.ncbi.nlm.nih.gov/32092051/) | Mouse | Mosaicism exacerbates LoF (not neomorphic); cell sorting ↔ face shape |
| [15037550](https://pubmed.ncbi.nlm.nih.gov/15037550/) | Mouse | Efnb1 null phenotype; NCC cell-autonomy; reverse (PDZ) signaling required |
| [16685650](https://pubmed.ncbi.nlm.nih.gov/16685650/) | Genetics | Paternal-origin bias (88%); mosaicism; paucity of carrier males |
| [24281372](https://pubmed.ncbi.nlm.nih.gov/24281372/) | Cohort | Fully-penetrant core features; frequency data |
| [40094327](https://pubmed.ncbi.nlm.nih.gov/40094327/) | Cohort | Canonical female phenotype; mild-end spectrum |
| [27194971](https://pubmed.ncbi.nlm.nih.gov/27194971/) | Case/review | Skeletal/ectodermal/dental features; normal intelligence; p.G151S |
| [32371695](https://pubmed.ncbi.nlm.nih.gov/32371695/) | Cohort | Neurodevelopmental outcome; deletion effect; multidisciplinary need |
| [20565770](https://pubmed.ncbi.nlm.nih.gov/20565770/) | Functional | Impact of variants on ephrin-B1 signaling/phosphorylation |
| [33864106](https://pubmed.ncbi.nlm.nih.gov/33864106/) | Surgical | Hypertelorism correction (facial bipartition/box osteotomy) |
| [38222144](https://pubmed.ncbi.nlm.nih.gov/38222144/) | Review | Classification among syndromic craniosynostoses |
| [39643662](https://pubmed.ncbi.nlm.nih.gov/39643662/) | Case | Structural variant (inv(X)) separating EFNB1 from enhancer |
| [41811039](https://pubmed.ncbi.nlm.nih.gov/41811039/) | Reproductive | Successful PGT-M for EFNB1 deletion |

---

## Limitations and Knowledge Gaps

- **Epidemiology is poorly quantified.** No reliable prevalence/incidence figures exist; CFNS is listed only as a rare disease.
- **Genotype–phenotype correlation is weak.** Variable expressivity, including discordant monozygotic twins sharing an identical variant ([PMID: 34174922](https://pubmed.ncbi.nlm.nih.gov/34174922/)), indicates stochastic X-inactivation and mosaic tissue architecture dominate over variant identity; this limits prognostic precision.
- **Quantitative severity determinants** (degree/pattern of mosaicism per tissue) are not measurable in the clinic.
- **Neurodevelopmental mechanism** is incompletely understood; whether intragenic EFNB1 LoF contributes to speech/language difficulty independent of deletion size is unresolved.
- **No disease-modifying therapy or clinical trials** exist; all evidence for treatment is from surgical case series.
- **Natural animal disease** is absent; model evidence is from engineered systems only, with perinatal lethality of nulls limiting some studies.
- Many identifiers (ICD, MeSH mappings) are approximate best-fits rather than CFNS-specific codes.

## Proposed Follow-up Experiments / Actions

1. **Quantify tissue-specific mosaicism vs. severity** — correlate per-tissue mutant-allele fraction / X-inactivation skew (e.g., in periosteum, skin, blood) with objective craniofacial severity metrics to test whether mosaicism degree predicts phenotype.
2. **Single-cell / spatial transcriptomics of CFNS iPSC neural-crest organoids** to map boundary-formation failure and identify druggable nodes in Eph/ephrin cell sorting.
3. **Natural-history registry** to establish prevalence, incidence, long-term surgical outcomes, and standardized neurodevelopmental/QoL (speech, PROMIS) data.
4. **Modifier screen** — assess whether deletion breakpoints / contiguous genes (beyond EFNB1) explain neurodevelopmental variability; define the contiguous-gene deletion phenotype.
5. **Functional classification pipeline** combining AlphaFold3 modeling, docking/MD, and cell-segregation assays to resolve EFNB1 VUS for clinical reporting.
6. **Mechanistic test of "boundary-sharpening" intervention** — determine in mouse/iPSC models whether modulating Eph/ephrin signaling can reduce aberrant cell sorting, as a conceptual basis for future therapy.

---

*Evidence-source legend:* human clinical (cohorts/case reports), model organism (mouse Efnb1), in vitro (patient iPSC, NIH 3T3/transfection), and computational (AlphaFold/docking/MD, in silico predictors). All mechanistic and clinical claims above are attributed to the cited PMIDs.


## Artifacts

- [OpenScientist final report](Craniofrontonasal_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Craniofrontonasal_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 20 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 10 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C15312` (1 mention) - the report calls it "Supportive:** speech/language therapy"; NCIT calls it **Radiation Dosimetry**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000316` (2 mentions) - the report calls it "orbital hypertelorism", "Orbital hypertelorism"; HP calls it **Hypertelorism**, and lists "Ocular hypertelorism" among its other names
- `HP:0000456` (2 mentions) - the report calls it "bifid/grooved nasal tip", "Bifid nasal tip"; HP calls it **Bifid nasal tip**
- `HP:0001807` (2 mentions) - the report calls it "longitudinal nail ridging/splitting", "Longitudinal nail ridging/splitting"; HP calls it **Ridged nail**, and lists "Longitudinal ridging" among its other names
- `HP:0002212` (2 mentions) - the report calls it "wiry/curly "woolly" hair", "Woolly/wiry hair"; HP calls it **Curly hair**
- `HP:0000465` (1 mention) - the report calls it "Mild webbed neck"; HP calls it **Webbed neck**
- `HP:0001863` (1 mention) - the report calls it "Clinodactyly of toes"; HP calls it **Toe clinodactyly**, and lists "Clinodactyly of feet" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000316` - called "orbital hypertelorism", "Orbital hypertelorism"
- `HP:0000456` - called "bifid/grooved nasal tip", "Bifid nasal tip"
- `HP:0001807` - called "longitudinal nail ridging/splitting", "Longitudinal nail ridging/splitting"
- `HP:0002212` - called "wiry/curly "woolly" hair", "Woolly/wiry hair"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.