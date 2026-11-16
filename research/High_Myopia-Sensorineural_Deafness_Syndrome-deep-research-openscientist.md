---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-11T21:47:51.314504'
end_time: '2026-11-11T22:05:41.217406'
duration_seconds: 1069.9
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: High Myopia-Sensorineural Deafness Syndrome
  mondo_id: MONDO:0009082
  category: Mendelian
  causal_genes: SLITRK6
  omim_id: OMIM:221200
  synonyms: not recorded
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
citation_count: 3
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 6
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.5.1
term_validation:
  total_terms: 19
  verified: 17
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 1
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0009082
    reported_labels:
    - MONDO
    ontology_label: high myopia-sensorineural deafness syndrome
  - term_id: HP:0011962
    reported_labels:
    - Abnormal auditory brainstem response
    ontology_label: Obstructive azoospermia
  - term_id: UBERON:0000970
    reported_labels:
    - Eye
    - Primary organs:** **Eye
    ontology_label: eye
  obsolete_terms:
  - term_id: GO:0005887
    ontology_label: GO_0005887
    replaced_by: GO:0005886
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: High_Myopia-Sensorineural_Deafness_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: High_Myopia-Sensorineural_Deafness_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** High Myopia-Sensorineural Deafness Syndrome
- **MONDO ID:** MONDO:0009082 (if available)
- **Causal gene(s):** SLITRK6
- **OMIM:** OMIM:221200
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **High Myopia-Sensorineural Deafness Syndrome** covering all of the
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

# High Myopia–Sensorineural Deafness Syndrome (DFNMYP) — Comprehensive Disease Report

**Disease:** High Myopia–Sensorineural Deafness Syndrome
**MONDO ID:** MONDO:0009082 · **OMIM:** 221200 (DFNMYP) · **Causal gene:** **SLITRK6** (SLIT and NTRK-like family, member 6)
**Category:** Mendelian, autosomal recessive

---

## Summary

High Myopia–Sensorineural Deafness Syndrome (DFNMYP; OMIM 221200; MONDO:0009082) is a rare **autosomal-recessive** disorder caused by biallelic **loss-of-function mutations in SLITRK6**, a single-pass leucine-rich-repeat (LRR) transmembrane protein encoded on chromosome **13q31.1** (HGNC:23503, NCBI Gene 84189, UniProt Q9H5Y7, gene OMIM 609681). The syndrome was defined in 2013 by Tekin and colleagues, who identified homozygous nonsense mutations in three families and showed that the mutant proteins fail to reach the cell surface ([PMID: 23543054](https://pubmed.ncbi.nlm.nih.gov/23543054/)). The two cardinal features are **congenital high (axial) myopia** and **progressive bilateral sensorineural hearing loss**, the latter having the electrophysiological signature of an **auditory neuropathy**. Vestibular function is preserved.

Mechanistically, SLITRK6 is a **trans-synaptic synapse-organizing protein**. Its extracellular LRR modules bind presynaptic LAR-family receptor protein tyrosine phosphatases (**PTPδ/PTPRD and PTPσ/PTPRS**), building adhesion complexes that drive synaptogenesis and support the survival and innervation of sensory neurons in the retina and cochlea. Truncating mutations abolish surface localization of SLITRK6, breaking this complex. The downstream consequences — demonstrated in *Slitrk6*-deficient mice — are **increased axial eye length** (the endophenotype of myopia), **auditory function deficits**, and **delayed retinal synaptogenesis** ([PMID: 23543054](https://pubmed.ncbi.nlm.nih.gov/23543054/)). Population genetics support a pure recessive loss-of-function model: gnomAD shows SLITRK6 is tolerant of heterozygous LOF (pLI ≈ 0), and every pathogenic/likely-pathogenic small variant catalogued in ClinVar is truncating.

There is **no disease-modifying therapy**. Management is entirely supportive: refractive and low-vision correction for the myopia, and hearing aids or **cochlear implantation** for the deafness, supplemented by genetic counseling. Because heterozygotes are unaffected and only biallelic complete loss of function causes disease, carrier and cascade testing and reproductive counseling are the principal preventive tools.

---

## Key Findings

### Finding 1 — Biallelic truncating SLITRK6 mutations cause the recessive syndrome

The disease is caused by **biallelic loss-of-function mutations in SLITRK6**. The founding study (Tekin et al., 2013) used homozygosity mapping and sequencing to identify **three homozygous nonsense mutations — p.R181X, p.S297X, and p.Q414X — across three families** with an autosomal-recessive syndrome of high myopia plus sensorineural deafness. Critically, all three mutant proteins showed **defective cell-surface localization**, establishing the functional mechanism as loss of a membrane protein:

> "led to the identification of 3 homozygous nonsense mutations (p.R181X, p.S297X, and p.Q414X) in SLIT and NTRK-like family, member 6 (SLITRK6), a leucine-rich repeat domain transmembrane protein. All 3 mutant SLITRK6 proteins displayed defective cell surface localization." ([PMID: 23543054](https://pubmed.ncbi.nlm.nih.gov/23543054/))

The allelic spectrum has since broadened across populations. An additional recurrent allele, **p.Gln414Ter (c.1240C>T)**, was reported in **9 Amish homozygotes** (Morlet et al., 2014), and a frameshift allele, **c.696delG (p.Trp232Cysfs\*10)**, was found in a homozygous state in a Moroccan family (Salime et al., 2018):

> "identify a novel single deleterious mutation c.696delG, p.Trp232Cysfs\*10 at homozygous state in the exon 2 of the SLITRK6" ([PMID: 29551497](https://pubmed.ncbi.nlm.nih.gov/29551497/))

All reported disease alleles are **nonsense or frameshift (truncating)** changes, consistent with a loss-of-function disease mechanism.

### Finding 2 — The hearing loss is a progressive auditory neuropathy with preserved vestibular function

Detailed audiologic phenotyping of the 9 Amish homozygotes (c.1240C>T, p.Gln414Ter) by Morlet et al. (2014) characterized the deafness as an **auditory neuropathy spectrum disorder** rather than a simple cochlear (sensory) hearing loss. The electrophysiology showed **absent distortion-product otoacoustic emissions (DPOAEs)** in all ears, an **increased-then-absent cochlear microphonic (CM)**, and **dys-synchronised auditory brainstem responses (ABRs)** with no reproducible waves I/III/V at high intensities:

> "Distortion product otoacoustic emissions (DPOAEs) were absent in all ears tested and the cochlear microphonic (CM) was increased in amplitude and duration in young patients and absent in the two oldest subjects. Auditory brainstem responses (ABRs) were dys-synchronised bilaterally with no reproducible waves I, III, or V at high intensities." ([PMID: 23946138](https://pubmed.ncbi.nlm.nih.gov/23946138/))

The hearing loss is **progressive and symmetric**, deteriorating with age to severe-to-profound impairment by early adulthood:

> "Hearing loss and speech reception thresholds deteriorated symmetrically with age, which resulted in severe-to-profound hearing impairment by early adulthood." ([PMID: 23946138](https://pubmed.ncbi.nlm.nih.gov/23946138/))

**Vestibular evoked myogenic potentials were normal**, indicating preserved vestibular function — a clinically useful distinguishing feature. This pattern (absent/abnormal OAEs with present CM, dys-synchronous ABR) is the classic signature of auditory dyssynchrony/neuropathy, pointing to a lesion at the level of inner hair cell synapse / auditory nerve rather than outer hair cell mechanics alone.

### Finding 3 — *Slitrk6*-deficient mice recapitulate the human syndrome

The mouse knockout reproduces both organ phenotypes, providing strong causal evidence. High-resolution MRI of *Slitrk6*-deficient eyes revealed **increased axial length — the endophenotype of myopia** — and the mutant mice displayed **auditory function deficits mirroring the human phenotype**. Retinal histology during postnatal development showed a **delay in synaptogenesis**:

> "High-resolution MRI of WT and Slitrk6-deficient mouse eyes revealed axial length increase in the mutant (the endophenotype of myopia). Additionally, mutant mice exhibited auditory function deficits that mirrored the human phenotype. Histological investigation of WT and Slitrk6-deficient mouse retinas in postnatal development indicated a delay in synaptogenesis in Slitrk6-deficient animals." ([PMID: 23543054](https://pubmed.ncbi.nlm.nih.gov/23543054/))

The biological role unifying both phenotypes is neurotrophic/synaptic:

> "Slitrk6 plays a role in the survival and innervation of sensory neurons in the inner ear, vestibular apparatus, and retina, and also influences axial eye length" ([PMID: 23946138](https://pubmed.ncbi.nlm.nih.gov/23946138/))

### Finding 4 — SLITRK6 is tolerant of heterozygous LOF (gnomAD), confirming recessive inheritance

Gene-constraint metrics from gnomAD (GRCh38) show SLITRK6 is **not haploinsufficient**: **pLI ≈ 1.3×10⁻⁷ (≈0)**, **observed/expected LOF (oe_lof) = 0.63** with LOEUF = 0.83 (observed/expected = 35/55.6, lof_z = 2.34). A pLI near zero means loss of one allele is well tolerated in the general population — exactly what is expected for a recessive disorder in which only **biallelic** LOF causes disease, and heterozygous carriers are unaffected.

Confirmed identifiers anchoring the gene: **UniProt Q9H5Y7** (841 aa), **NCBI Gene 84189**, **HGNC:23503**, gene **OMIM 609681**, cytoband **13q31.1**; mouse ortholog **Slitrk6** (Entrez 239250).

### Finding 5 — ClinVar variant spectrum is exclusively truncating for pathogenic alleles

ClinVar (gene SLITRK6, transcript NM_032229.3) lists **80 variants**: 65 Uncertain significance, 8 Likely benign, 3 Pathogenic, 2 Likely pathogenic. Every pathogenic/likely-pathogenic **small** variant is **truncating** — e.g., **c.698T>A (p.Leu233Ter, nonsense)** and **c.846del (p.Leu283fs, frameshift)**. The "Pathogenic" set also includes **large multi-megabase 13q deletions** that encompass SLITRK6 (e.g., 13q31.1–34; 13q14.3–31.2). The complete absence of pathogenic missense alleles reinforces a **pure loss-of-function** mechanism — there is no evidence for gain-of-function or dominant-negative disease.

### Finding 6 — Protein architecture: single-pass membrane protein with two extracellular LRR modules

UniProt Q9H5Y7 (841 aa) annotates a canonical **SLITRK architecture**: an N-terminal **signal peptide**; a large **extracellular region (~aa 27–608)** containing **two tandem LRR modules** (LRRNT1 27–67 + 5 LRRs + LRRCT1 218–269; LRRNT2 320–361 + 6 LRRs + LRRCT2 517–568); a single **transmembrane helix (aa 609–629)**; and a **cytoplasmic tail (aa 630–841)**. Subcellular location is the **cell membrane**. UniProt's functional summary is "**Regulator of neurite outgrowth required for normal hearing and vision**," and its disease annotation (DFNMYP) reads "an autosomal recessive disorder characterized by prelingual sensorineural hearing loss associated with high myopia." Tissue specificity is highest in **putamen**, with expression in adult/fetal lung, fetal liver, and high levels in some brain tumors (medulloblastoma, PNET).

Truncating mutations at p.R181X, p.Trp232fs, p.Leu233Ter, p.S297X, p.Leu283fs, and p.Q414X all fall within or upstream of the extracellular LRR domains, removing the transmembrane anchor and/or the ligand-binding LRR surface — explaining the observed **loss of cell-surface localization**.

### Finding 7 — SLITRK6's top partners are presynaptic LAR-RPTPs (PTPδ/PTPσ) and IL1RAPL1

STRING (human, confidence ≥0.4) ranks SLITRK6's highest-confidence functional partners as **PTPRD/PTPδ (0.986)**, **IL1RAPL1 (0.986)**, and **PTPRS/PTPσ (0.970)**, with lower-confidence NTRK1/TrkA (0.590) and others (GRK1, PPEF2, OLFM2, BMPR1B, STK4, LRRC20). **PTPδ and PTPσ are the established presynaptic LAR-family receptor protein tyrosine phosphatases** that bind SLITRK extracellular LRR domains to assemble **trans-synaptic adhesion complexes**. This places SLITRK6 squarely in the synapse-organizing pathway and provides the molecular bridge between gene loss and the sensory-neuron synaptic deficits seen in retina and cochlea.

---

## Report by Section

### 1. Disease Information

**Overview.** DFNMYP is a Mendelian, autosomal-recessive syndrome combining **congenital high myopia** and **progressive bilateral sensorineural hearing loss** (auditory-neuropathy type). It is caused by loss of function of **SLITRK6**, a synaptic organizer required for normal development of the eye and inner ear.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (disease) | 221200 (DFNMYP) |
| OMIM (gene) | 609681 (SLITRK6) |
| MONDO | MONDO:0009082 |
| HGNC | 23503 |
| NCBI Gene | 84189 |
| UniProt | Q9H5Y7 |
| Ensembl / cytoband | 13q31.1 |
| Mouse ortholog | Slitrk6 (Entrez 239250) |

**Synonyms / alternative names:** High myopia–sensorineural deafness; Deafness and myopia syndrome; Myopia–deafness syndrome; DFNMYP; SLITRK6-related myopia and deafness. (No additional formal synonyms recorded in the source template.)

**Information source type:** Aggregated disease-level resources (OMIM, UniProt, ClinVar, gnomAD, STRING) combined with **individual-patient clinical reports** from the primary cohorts (families in Tekin 2013; 9 Old Order Amish in Morlet 2014; one Moroccan family in Salime 2018).

### 2. Etiology

**Primary cause:** Genetic — biallelic (homozygous or compound heterozygous) loss-of-function mutations in **SLITRK6**. No environmental or infectious cause.

**Genetic risk factors:** The causal variants are truncating alleles (nonsense/frameshift) and large 13q deletions encompassing SLITRK6. Specific recurrent alleles include **p.R181X, p.S297X, p.Q414X** (Tekin 2013), **p.Gln414Ter / c.1240C>T** (Amish founder allele, Morlet 2014), and **c.696delG / p.Trp232Cysfs\*10** (Moroccan, Salime 2018). **Consanguinity** and **founder effects** (notably the Amish c.1240C>T) are the main population-level risk drivers, as expected for a rare recessive disorder.

**Environmental risk / protective factors:** None established. The myopia here is **syndromic and axial/genetic**, distinct from common multifactorial refractive myopia; near-work and lighting (relevant to common myopia) are not established modifiers of this monogenic form.

**Protective genetic factors / modifier genes:** None reported. No modifier loci or protective alleles have been identified for DFNMYP.

**Gene–environment interactions:** None documented; disease is essentially fully penetrant given biallelic LOF.

### 3. Phenotypes

| Phenotype | Type | HPO term (suggested) | Onset | Severity / Progression | Frequency |
|---|---|---|---|---|---|
| High myopia (axial) | Physical/ophthalmologic | HP:0011003 (High myopia) / HP:0000545 (Myopia) | Congenital / early childhood | Severe; axial elongation | Universal (defining) |
| Sensorineural hearing loss | Clinical sign | HP:0000407 (Sensorineural hearing impairment) | Prelingual/congenital | Progressive, symmetric; severe-to-profound by early adulthood | Universal (defining) |
| Auditory neuropathy pattern | Laboratory/electrophysiology | HP:0011962 (Abnormal auditory brainstem response) | Early | Dys-synchronous ABR, absent DPOAE, abnormal CM | Reported in Amish cohort |
| Preserved vestibular function | (Negative finding) | — | — | Normal VEMP | Reported |

**Quality-of-life impact:** The dual sensory deficit (vision + hearing) has substantial impact on communication, education, and independent living. Early hearing amplification/cochlear implantation and low-vision support materially improve function, but the combined deficit places affected individuals in a **dual-sensory-impairment** category requiring multidisciplinary rehabilitation.

### 4. Genetic / Molecular Information

**Causal gene:** SLITRK6 (gene OMIM 609681; HGNC:23503; NCBI Gene 84189; chr 13q31.1), notable as a gene whose coding sequence lies in a single exon.

**Pathogenic variants (representative):**

| Variant (cDNA) | Protein | Class | Source / population |
|---|---|---|---|
| — | p.R181X | Nonsense | Tekin 2013 |
| — | p.S297X | Nonsense | Tekin 2013 |
| c.1240C>T | p.Gln414Ter (p.Q414X) | Nonsense | Tekin 2013; Amish founder (Morlet 2014) |
| c.696delG | p.Trp232Cysfs\*10 | Frameshift | Salime 2018 (Moroccan) |
| c.698T>A | p.Leu233Ter | Nonsense | ClinVar (Pathogenic) |
| c.846del | p.Leu283fs | Frameshift | ClinVar (Pathogenic) |
| 13q multi-Mb deletions | (whole-gene loss) | Structural | ClinVar (Pathogenic) |

**Variant classification:** Per ACMG/AMP, the recurrent truncating alleles are Pathogenic/Likely pathogenic; the vast majority of ClinVar entries (65/80) are VUS, and 8 are Likely benign. **No pathogenic missense alleles** exist — the spectrum is exclusively LOF.

**Allele frequency:** Disease alleles are rare/private; gnomAD shows SLITRK6 tolerant of heterozygous LOF (pLI ≈ 0, LOEUF 0.83).

**Origin:** Germline. **Functional consequence:** Loss of function (abolished cell-surface localization). No gain-of-function or dominant-negative mechanism.

**Modifier genes / epigenetics:** None reported. **Chromosomal abnormalities:** Large 13q31 deletions encompassing SLITRK6 can produce the phenotype as part of contiguous-gene deletions.

### 5. Environmental Information

Not applicable. DFNMYP is a monogenic recessive disorder with no established environmental, lifestyle, or infectious contributors. (The axial myopia is genetically determined, unlike common environmentally modulated myopia.)

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. **Biallelic truncating mutation in SLITRK6** (nonsense/frameshift, or whole-gene 13q deletion) → produces a truncated protein or no protein.
2. Truncated SLITRK6 **loses its transmembrane anchor and/or LRR ligand-binding surface** → **fails to localize to the cell membrane** (demonstrated for p.R181X, p.S297X, p.Q414X).
3. Absent surface SLITRK6 → **cannot bind presynaptic LAR-family RPTPs (PTPδ/PTPRD, PTPσ/PTPRS)** → **trans-synaptic SLITRK6–LAR-RPTP adhesion complex fails to form** (inferred from STRING interactome + known SLITRK–LAR biology).
4. Loss of synaptic organizing signal → **impaired/delayed synaptogenesis** and **reduced survival/innervation of sensory neurons** in retina and cochlea (demonstrated as delayed retinal synaptogenesis in mouse).
5. **Branch A (eye):** disrupted retinal synaptic development/visual signaling → **dysregulated axial growth of the eye** → **increased axial length** → **high axial myopia** (axial elongation demonstrated by MRI in *Slitrk6* KO).
6. **Branch B (ear):** impaired innervation/survival of cochlear sensory neurons and inner-hair-cell synapse → **auditory dyssynchrony** (absent DPOAE, abnormal CM, dys-synchronous ABR) → **progressive sensorineural hearing loss / auditory neuropathy**, worsening symmetrically to severe-to-profound by early adulthood.
7. Vestibular apparatus relatively spared → **normal vestibular function** (preserved VEMP).

```
SLITRK6 LOF mutation
      │ (loss of surface protein)
      ▼
SLITRK6–PTPδ/PTPσ trans-synaptic complex not formed
      │ (impaired synapse organization)
      ▼
delayed synaptogenesis + poor sensory-neuron innervation/survival
      ├──────────────► RETINA → dysregulated axial growth → HIGH MYOPIA
      └──────────────► COCHLEA → auditory dyssynchrony → PROGRESSIVE SNHL
                       (vestibular system spared)
```

**Molecular pathway:** Trans-synaptic LRR adhesion / **SLITRK–LAR-RPTP synapse organization** (GO:0007416 synapse assembly; GO:0050808 synapse organization). **Cellular process:** neurite outgrowth regulation (GO:0010975), neuron development, synaptogenesis. **Protein dysfunction:** loss of function via mislocalization (not aggregation). **Cell types (CL):** retinal neurons / bipolar neurons (CL:0000540 neuron; CL:0000748 retinal bipolar neuron), cochlear hair cells / spiral ganglion neurons (CL:0000601 cochlear hair cell). **Upstream:** the SLITRK6 mutation and loss of synaptic adhesion. **Downstream:** axial elongation and auditory dyssynchrony.

No immune, metabolic, or inflammatory mechanism is implicated.

### 7. Anatomical Structures Affected

- **Primary organs:** **Eye** (UBERON:0000970) — retina (UBERON:0000966) and globe affecting axial length; **Inner ear / cochlea** (UBERON:0001844 cochlea; UBERON:0001690 ear).
- **Body systems:** Special sense organs — **visual system** and **auditory/sensory system**.
- **Tissue/cell level:** Neural retina (photoreceptor-to-bipolar synaptic layers), cochlear sensory epithelium and spiral ganglion neurons; inner hair cell ribbon synapse implicated by the auditory-neuropathy pattern.
- **Subcellular (GO CC):** cell membrane / plasma membrane (GO:0005886); synapse (GO:0045202); integral component of plasma membrane (GO:0005887).
- **Localization / lateralization:** **Bilateral and symmetric** for both eye and ear involvement.

### 8. Temporal Development

- **Onset:** **Congenital/prelingual.** High myopia present from early childhood; hearing loss prelingual (often congenital).
- **Onset pattern:** Chronic/insidious.
- **Progression:** The **hearing loss is progressive**, deteriorating **symmetrically with age to severe-to-profound by early adulthood** ([PMID: 23946138](https://pubmed.ncbi.nlm.nih.gov/23946138/)). The myopia is high/axial.
- **Disease course:** Chronic, lifelong, progressive (for hearing). No remission; no self-limited course.
- **Critical period:** Early childhood is the window for intervention — early audiologic amplification/cochlear implantation and refractive correction to support language and visual development.

### 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive.** Biallelic LOF required; heterozygous carriers unaffected (consistent with gnomAD pLI ≈ 0).
- **Penetrance:** Essentially complete for biallelic LOF. **Expressivity:** The two cardinal features are consistent, with some variability in hearing-loss severity by age.
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Founder effects:** Yes — the **Amish c.1240C>T (p.Gln414Ter)** allele is a documented founder allele (Morlet 2014, 9 homozygotes).
- **Consanguinity:** A major contributor; most reported families are consanguineous or from genetically isolated populations.
- **Carrier frequency:** Not formally estimated at population scale; rare overall, elevated locally in founder populations.
- **Epidemiology:** **Ultra-rare**; precise prevalence/incidence not established. Reported in a small number of families worldwide.
- **Geographic distribution:** Cases reported in Turkish/Greek/Mennonite, Old Order Amish (USA), and Moroccan populations — clustering in consanguineous or isolated communities.
- **Sex ratio:** No sex predilection (autosomal). **Age distribution:** Affected from birth; hearing worsens through childhood into early adulthood.

### 10. Diagnostics

- **Ophthalmologic:** Refraction and **axial length measurement** (biometry) documenting high axial myopia; fundus examination.
- **Audiologic:** Pure-tone audiometry; **DPOAE** (absent), **cochlear microphonic** (abnormal), **ABR** (dys-synchronous, absent waves I/III/V), middle-ear muscle reflexes (absent in older patients) — together establishing an **auditory neuropathy** pattern. **VEMP** normal (vestibular sparing) — a useful differentiator.
- **Genetic testing (confirmatory):** **Single-gene SLITRK6 sequencing**, deafness/retinal gene panels including SLITRK6, or **whole-exome sequencing (WES)**; **chromosomal microarray (CMA)** detects large 13q deletions encompassing SLITRK6. WES/panel is the practical first-line given the combination of ocular + auditory features; reference transcript NM_032229.3.
- **Clinical criteria:** Diagnosis = **congenital high axial myopia + progressive bilateral sensorineural hearing loss** with **biallelic truncating SLITRK6 variants**.
- **Differential diagnosis:** Other syndromic deafness-with-eye-disease conditions must be excluded — notably **Usher syndrome** (deafness + retinitis pigmentosa, often with vestibular involvement in type 1), **Stickler syndrome** (high myopia + hearing loss + arthro-ophthalmopathy, autosomal dominant COL2A1/COL11), **Marshall syndrome**, and **Wolfram syndrome**. The auditory-neuropathy electrophysiology, preserved vestibular function, isolated high myopia (no retinal dystrophy/arthropathy), and SLITRK6 genotype distinguish DFNMYP.
- **Screening:** Carrier screening in at-risk families; cascade testing of relatives; newborn hearing screening will flag the auditory component.

### 11. Outcome / Prognosis

- **Survival / mortality:** **Normal life expectancy**; the disorder is not life-limiting. No disease-specific mortality.
- **Morbidity:** Substantial sensory morbidity — combined visual and progressive auditory impairment affecting communication, education, and daily function (dual sensory impairment).
- **Disease course:** Hearing loss progresses to severe-to-profound by early adulthood; myopia is high and lifelong. **Recovery potential:** No spontaneous recovery; function is improved (not cured) by devices.
- **Prognostic factors:** Severity/progression of hearing loss and timing of intervention (early amplification/cochlear implantation and refractive support predict better communication and educational outcomes). Genotype is uniformly LOF, so genotype–phenotype gradation is limited.

### 12. Treatment

**No disease-modifying or curative therapy exists.** Management is supportive and device-based (suggested NCIT intervention terms in parentheses):

- **Ophthalmologic:** Corrective **refractive lenses / spectacles / contact lenses** and **low-vision aids**; routine retinal surveillance for high-myopia complications (retinal detachment, myopic maculopathy) (NCIT: Eyeglasses; Corrective Lens).
- **Audiologic:** **Hearing aids**; **cochlear implantation** for severe-to-profound loss. Because the lesion is an auditory neuropathy, cochlear-implant candidacy/benefit should be individually assessed, but implantation is a mainstay for severe-to-profound cases (NCIT: Hearing Aid; Cochlear Implant).
- **Rehabilitation / supportive:** **Speech-language therapy**, educational support, and dual-sensory-impairment services (NCIT: Speech Therapy; Rehabilitation Therapy).
- **Pharmacotherapy / gene therapy / cell therapy / RNA therapy:** None established or in trials specific to SLITRK6/DFNMYP. No pharmacogenomic considerations.
- **Experimental:** No DFNMYP-specific clinical trials identified.

### 13. Prevention

- **Primary prevention:** Not possible (genetic). **Genetic counseling** is the principal tool — 25% recurrence risk per pregnancy for carrier couples.
- **Genetic/carrier screening:** Carrier testing in consanguineous/founder families; **cascade testing**; **prenatal diagnosis** and **preimplantation genetic testing (PGT)** are options for known-variant families.
- **Secondary prevention:** **Newborn hearing screening** and early pediatric refraction enable early intervention during the critical developmental window.
- **Tertiary prevention:** Monitoring and managing high-myopia complications (retinal detachment, maculopathy); optimizing amplification/implantation to prevent language and developmental deficits.
- **Public health / immunization / behavioral:** Not applicable.

### 14. Other Species / Natural Disease

- **Taxonomy / model:** *Mus musculus* (NCBI Taxon 10090) — the principal experimental species. **Orthologous gene:** mouse **Slitrk6** (Entrez 239250).
- **Natural disease in other species:** No naturally occurring companion-animal or wildlife DFNMYP homolog is documented (no OMIA entry noted).
- **Comparative biology / conservation:** SLITRK6's synaptic-organizer function and the SLITRK–LAR-RPTP interaction are evolutionarily conserved among vertebrates, supporting cross-species validity of the mouse model.
- **Zoonosis:** Not applicable (non-infectious).

### 15. Model Organisms

- **Model type:** Mammalian — **Slitrk6 knockout mouse** (the key disease model).
- **Phenotype recapitulation:** **Strong.** The KO reproduces (i) **increased axial eye length** (myopia endophenotype, by high-resolution MRI), (ii) **auditory function deficits** mirroring the human phenotype, and (iii) **delayed retinal synaptogenesis** on postnatal histology ([PMID: 23543054](https://pubmed.ncbi.nlm.nih.gov/23543054/)). Slitrk6 contributes to survival/innervation of sensory neurons in inner ear, vestibular apparatus, and retina ([PMID: 23946138](https://pubmed.ncbi.nlm.nih.gov/23946138/)).
- **Applications:** Mechanistic dissection of axial eye growth control, retinal synaptogenesis, and cochlear neuron innervation; platform for candidate therapeutics.
- **Limitations:** Mouse vision/auditory physiology differs from human; the model does not capture the full progressive human hearing-loss trajectory or the human refractive endpoint directly. Additional cellular/iPSC or organoid models for DFNMYP were not identified.
- **Resources:** MGI (Slitrk6). Cellular models (iPSC/organoid) not reported.

---

## Mechanistic Model / Interpretation

The entire phenotype is parsimoniously explained by **loss of a single trans-synaptic organizing protein**. SLITRK6 is a two-LRR, single-pass membrane protein (Finding 6) whose extracellular LRR surface engages presynaptic **LAR-RPTPs (PTPδ, PTPσ)** to nucleate synapse formation (Finding 7). When truncating mutations (Findings 1, 5) remove the membrane anchor / LRR surface, the protein never reaches the cell surface (Finding 1), so the adhesion complex cannot assemble. Downstream, synaptogenesis is delayed and sensory-neuron innervation/survival is compromised — directly demonstrated in the mouse as **delayed retinal synaptogenesis**, **axial eye elongation**, and **auditory deficits** (Finding 3). The two clinical branches (myopia via disrupted retinal/visual control of eye growth; progressive auditory neuropathy via inner-ear synaptic/innervation failure) share this single upstream lesion, while the vestibular system is relatively spared. Population genetics close the loop: SLITRK6 tolerates monoallelic loss (gnomAD pLI ≈ 0, Finding 4) and only truncating/whole-gene-deletion alleles are pathogenic (Finding 5) — confirming a **recessive, pure loss-of-function** model with no dominant-negative or gain-of-function component.

| Layer | Observation | Evidence |
|---|---|---|
| Gene | Biallelic truncating SLITRK6 variants | Tekin 2013; Morlet 2014; Salime 2018; ClinVar |
| Protein | Loss of cell-surface localization | Tekin 2013 (in vitro) |
| Interactome | Binds PTPδ/PTPσ (LAR-RPTPs), IL1RAPL1 | STRING |
| Cell/tissue | Delayed synaptogenesis; poor sensory innervation | Mouse (Tekin 2013; Morlet 2014) |
| Organ | Axial eye elongation; auditory dyssynchrony | Mouse MRI + human electrophysiology |
| Clinical | High myopia + progressive SNHL, vestibular sparing | Human cohorts |
| Population | Recessive; heterozygotes unaffected | gnomAD |

---

## Evidence Base

| PMID | Title | Type | Contribution |
|---|---|---|---|
| [23543054](https://pubmed.ncbi.nlm.nih.gov/23543054/) | *SLITRK6 mutations cause myopia and deafness in humans and mice.* | Human clinical + mouse model + in vitro | Founding study: 3 homozygous nonsense mutations; defective surface localization; KO mouse recapitulates axial myopia, auditory deficits, delayed retinal synaptogenesis |
| [23946138](https://pubmed.ncbi.nlm.nih.gov/23946138/) | *A homozygous SLITRK6 nonsense mutation is associated with progressive auditory neuropathy in humans.* | Human clinical (9 Amish) | Defines auditory-neuropathy electrophysiology, progressive symmetric hearing loss, vestibular sparing; Slitrk6 neurotrophic role |
| [29551497](https://pubmed.ncbi.nlm.nih.gov/29551497/) | *A novel mutation in SLITRK6 causes deafness and myopia in a Moroccan family.* | Human clinical | Adds frameshift allele c.696delG (p.Trp232Cysfs\*10); extends allelic/population spectrum |

Supporting database evidence (no single PMID): **gnomAD** (constraint, Finding 4), **ClinVar** (variant spectrum, Finding 5), **UniProt Q9H5Y7** (architecture/function, Finding 6), **STRING** (interactome, Finding 7). These resources are mutually consistent and all point to a recessive loss-of-function synaptic-organizer mechanism.

---

## Limitations and Knowledge Gaps

1. **Small human evidence base.** The clinical picture rests on ~3 cohorts/families; prevalence, carrier frequency, and full phenotypic range are not well quantified.
2. **Mechanistic gaps in the eye.** How SLITRK6 loss translates specifically into *axial elongation* (vs. retinal degeneration) is not fully worked out at the molecular level; the SLITRK6→PTPδ/PTPσ→eye-growth link is partly inferred.
3. **Auditory-neuropathy site of lesion** (inner hair cell ribbon synapse vs. spiral ganglion neuron) is inferred from electrophysiology, not confirmed by human histopathology.
4. **No longitudinal natural-history data** quantifying rates of myopia/axial progression or hearing decline; no formal QoL instruments applied.
5. **Cochlear-implant outcomes** specific to SLITRK6 auditory neuropathy are not systematically reported — CI benefit in auditory neuropathy can be variable.
6. **No therapeutic development** (gene/cell/RNA therapy) and no cellular/organoid human models identified.

---

## Proposed Follow-up Experiments / Actions

1. **Natural-history registry** across known families to quantify axial-length and hearing-threshold trajectories and define intervention windows.
2. **Cochlear-implant outcome study** in SLITRK6 patients to determine whether the synaptic/neuropathic lesion permits good electrical-stimulation benefit.
3. **Mechanistic imaging/histology** in the KO mouse (and human iPSC-derived retinal and inner-ear organoids) to map the SLITRK6–PTPδ/PTPσ synaptic deficit to axial growth control and inner-hair-cell synaptopathy.
4. **Structure-function / rescue assays:** test whether re-expression of wild-type SLITRK6 (or isolated LRR domains) restores surface localization and PTPδ/PTPσ binding, and whether gene-replacement rescues the mouse phenotype — proof-of-concept for future gene therapy.
5. **Variant reclassification effort:** functional assays (surface-localization, LAR-RPTP binding) on the 65 ClinVar VUS to resolve their clinical significance.
6. **Carrier-frequency estimation** in founder populations (Amish, North African) to inform targeted carrier-screening programs.

---

*Report generated from a 5-iteration autonomous investigation; 7 findings confirmed and verified against primary literature (PMIDs 23543054, 23946138, 29551497) and database evidence (gnomAD, ClinVar, UniProt Q9H5Y7, STRING).*


## Artifacts

- [OpenScientist final report](High_Myopia-Sensorineural_Deafness_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](High_Myopia-Sensorineural_Deafness_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 6 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 19 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 4 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009082` (3 mentions) - the report calls it "MONDO"; MONDO calls it **high myopia-sensorineural deafness syndrome**
- `HP:0011962` (1 mention) - the report calls it "Abnormal auditory brainstem response"; HP calls it **Obstructive azoospermia**
- `UBERON:0000970` (1 mention) - the report calls it "Eye", "Primary organs:** **Eye"; UBERON calls it **eye**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005887` (GO_0005887) (1 mention) - replaced by `GO:0005886`

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0000970` - called "Eye", "Primary organs:** **Eye"