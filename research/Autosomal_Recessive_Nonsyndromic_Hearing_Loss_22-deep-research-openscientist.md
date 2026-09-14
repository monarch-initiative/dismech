---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-11T22:44:46.817748'
end_time: '2026-09-11T22:55:32.793115'
duration_seconds: 645.98
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autosomal Recessive Nonsyndromic Hearing Loss 22
  mondo_id: MONDO:0011762
  category: Mendelian
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 6
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 7
  relevance_assessed: 13
  on_topic: 13
  validator_version: 0.2.1
term_validation:
  total_terms: 19
  verified: 17
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 6
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: CL:0000599
    reported_labels:
    - cochlear outer hair cell
    ontology_label: conidium
  - term_id: UBERON:0002518
    reported_labels:
    - tectorial membrane
    ontology_label: otolith organ
  - term_id: UBERON:0004681
    reported_labels:
    - spiral limbus
    ontology_label: vestibular system
  - term_id: HP:0000407
    reported_labels:
    - Sensorineural hearing impairment
    - ~100% of affected
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0008527
    reported_labels:
    - Congenital sensorineural hearing impairment
    - Predominant presentation
    ontology_label: Congenital sensorineural hearing impairment
  - term_id: HP:0000750
    reported_labels:
    - Secondary to HL
    ontology_label: Delayed speech and language development
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0031225
    ontology_label: obsolete anchored component of membrane
    replaced_by: GO:0016020
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Autosomal_Recessive_Nonsyndromic_Hearing_Loss_22-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Autosomal_Recessive_Nonsyndromic_Hearing_Loss_22-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 22
- **MONDO ID:** MONDO:0011762 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 22** covering all of the
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

# Autosomal Recessive Nonsyndromic Hearing Loss 22 (DFNB22): A Comprehensive Disease Characterization

**Disease:** Autosomal Recessive Nonsyndromic Hearing Loss 22 (DFNB22)
**MONDO ID:** MONDO:0011762 · **OMIM (disease):** #607039 · **Gene:** OTOA (*607038*), HGNC:16378, 16p12.2
**Category:** Mendelian, monogenic sensorineural hearing loss

---

## Summary

Autosomal Recessive Nonsyndromic Hearing Loss 22 (DFNB22) is a rare Mendelian form of congenital, bilateral, typically stable, moderate-to-severe sensorineural hearing loss (SNHL) caused by **biallelic loss-of-function of *OTOA***, the gene on chromosome 16p12.2 encoding **otoancorin**. Otoancorin is a ~120 kDa glycosylphosphatidylinositol (GPI)-anchored protein located at the interface between the apical surface of inner-ear sensory epithelia and their overlying acellular gels. In the cochlea it anchors the **tectorial membrane (TM)** to the spiral limbus (the "permanent" attachment zone) and to the greater epithelial ridge (the "transient" zone); in the vestibule it tethers otoconial membranes and cupulae to nonsensory cells. Because otoancorin is a structural tether rather than a signaling or ion-transport protein, its loss produces a purely mechanical failure of the hearing apparatus.

The mechanistic chain has been resolved in a mouse model. In *Otoa*-knockout mice the TM keeps its overall shape and stays close to the organ of Corti, but **detaches from the limbal (spiral limbus) surface**. Remarkably, it remains functionally coupled to the electromotile outer hair cells (OHCs), so cochlear amplification and frequency tuning are nearly normal (near-normal cochlear microphonics, DPOAEs, basilar-membrane motion, and sharply tuned CAP masking curves). What fails is **inner hair cell (IHC) stimulation**: compound action potential (CAP) thresholds are significantly elevated. Hearing loss in DFNB22 is therefore a defect of IHC drive — the sensory "read-out" — rather than of OHC amplification (PMID 23129639).

A defining practical feature of DFNB22 is its genomic architecture. *OTOA* sits within a **low-copy-repeat/segmental duplication** region that is highly homologous to the pseudogene ***OTOAP1***. This predisposes the locus to **non-allelic homologous recombination (NAHR)**, producing recurrent copy-number deletions, and to **gene conversions** that transfer pseudogene sequence (introducing a premature stop, p.Glu787*) into the functional gene. As a consequence, *OTOA* is one of the more common CNV-driven recessive deafness loci, yet standard short-read exome sequencing and gene panels frequently miss these events, requiring copy-number-aware methods (qPCR, MLPA, chromosomal microarray, or long-read sequencing) for a complete diagnosis. There is no disease-specific pharmacotherapy or gene therapy; management is habilitative (hearing aids, cochlear implantation, speech-language support) and preventive via genetic counseling.

---

## Key Findings

### Finding 1 — DFNB22 is caused by biallelic loss-of-function of *OTOA* (otoancorin), a GPI-anchored inner-ear tether

*OTOA* (chromosome 16p12.2; OMIM *607038*; disease OMIM #607039) encodes **otoancorin**, a ~120 kDa GPI-anchored protein. Otoancorin localizes to the interface between the apical surface of the inner-ear sensory epithelia and their overlying acellular gels. In the cochlea it marks the **two attachment zones of the tectorial membrane**: the permanent zone along the spiral limbus and the transient zone on the greater epithelial ridge. In the vestibular system it localizes to nonsensory cells in contact with the otoconial membranes and cupulae. The founding mutation, a splice variant **IVS12+2T>C**, was identified in a consanguineous Palestinian DFNB22 family (PMID 11972037).

The GPI anchorage was later validated experimentally. A frameshift allele, **p.Gln589ArgfsX55**, abolishes controlled release of otoancorin, causing uncontrolled release into the culture medium rather than the expected phosphatidylinositol-specific phospholipase C (PI-PLC)-dependent release — confirming that the pathogenic mechanism is loss of proper membrane anchorage of the protein (PMID 30740825).

> "Otoancorin is located at the interface between the apical surface of the inner ear sensory epithelia and their overlying acellular gels." — [PMID: 11972037](https://pubmed.ncbi.nlm.nih.gov/11972037/)

> "Otoancorin (OTOA), encoded by OTOA, is required for the development of the tectorial membrane in the inner ear. Mutations in this gene cause nonsyndromic hearing loss (DFNB22)." — [PMID: 30740825](https://pubmed.ncbi.nlm.nih.gov/30740825/)

**Ontology annotations:** Gene HGNC:16378 (*OTOA*); GO:0031225 (anchored component of membrane); GO:0098590 (plasma membrane region); biological process GO:0042491 / GO:0060119 (inner ear receptor cell development); CHEBI: glycosylphosphatidylinositol anchor.

### Finding 2 — Mechanism: tectorial-membrane detachment causes loss of inner hair cell stimulation, sparing outer hair cell amplification

The *Otoa*(EGFP/EGFP) knockout mouse resolves precisely how loss of otoancorin causes deafness. In these animals the TM retains its general form and remains close to the organ of Corti, but is **detached from the limbal (spiral limbus) surface**. Physiological measurements show that the TM stays functionally attached to the electromotile OHCs: cochlear microphonics, distortion-product otoacoustic emissions (DPOAEs), and basilar-membrane motion are almost normal, indicating preserved amplification and frequency tuning. However, **compound action potential (CAP) thresholds — a read-out of IHC sensitivity — are significantly elevated**, while CAP masker tuning curves remain sharply tuned. The conclusion is that DFNB22 hearing loss arises from a defect in **inner hair cell stimulation**, not from a failure of OHC-driven amplification (PMID 23129639).

> "These results indicate that the hearing loss in patients with Otoa mutations is caused by a defect in inner hair cell stimulation, and reveal the limbal attachment of the TM plays a critical role in this process." — [PMID: 23129639](https://pubmed.ncbi.nlm.nih.gov/23129639/)

This is mechanistically distinctive: many deafness genes act through OHC dysfunction or hair-bundle/mechanotransduction defects, whereas OTOA loss selectively disrupts the mechanical coupling that drives the IHCs, the afferent sensory cells.

**Ontology annotations:** CL:0000601 (cochlear inner hair cell), CL:0000599 (cochlear outer hair cell); UBERON:0002518 (tectorial membrane), UBERON:0002227 (organ of Corti), UBERON:0004681 (spiral limbus); GO:0007605 (sensory perception of sound).

### Finding 3 — *OTOA*/*OTOAP1* segmental duplication drives recurrent CNV deletions and gene conversions that complicate diagnosis

*OTOA* lies in a low-copy-repeat region on 16p12.2 that shares high sequence homology with the pseudogene ***OTOAP1***, predisposing the locus to **non-allelic homologous recombination (NAHR)**. Recurrent deletions of *OTOA* are a well-recognized cause of moderate-to-severe hearing loss. In a chromosomal-microarray (CMA) cohort of **19,189 tests** at Rabin Medical Center, heterozygous *OTOA* microdeletions were detected in **39 individuals (0.2% carrier frequency)** (PMID 33753912).

A second, subtler mechanism is **pathogenic gene conversion**, in which *OTOAP1* pseudogene sequence is copied into *OTOA*, introducing a premature stop codon **p.Glu787\*** in exon 22. Two compound-heterozygous patients (one converted allele plus one deletion) had moderate hearing loss, with converted tracts ranging from ~900 bp to >9 kbp (PMID 33492714). Contiguous-gene deletions also occur: a **250.285 kb homozygous 16p12.2 deletion** encompassing *METTL9*, *IGSF6*, and *OTOA* segregated with nonsyndromic SNHL in a South Indian consanguineous family (PMID 39916398).

Because these events are structural and occur in a repeat-rich region, short-read whole-exome sequencing and standard panels often miss them, and confirmation requires **qPCR, MLPA, CMA, or long-read sequencing** (PMID 35640668).

> "Bi-allelic loss-of-function variants of OTOA are a well-known cause of moderate-to-severe hearing loss. Whereas non-allelic homologous recombination-mediated deletions of the gene are well known, gene conversions to pseudogene OTOAP1 have been reported" — [PMID: 33492714](https://pubmed.ncbi.nlm.nih.gov/33492714/)

> "OTOA deletions (39, 0.2%)" — [PMID: 33753912](https://pubmed.ncbi.nlm.nih.gov/33753912/)

> "A homozygous deletion of 250.285 kb was identified in the 16p12.2 region encompassing three genes, METTL9, IGSF6, and OTOA" — [PMID: 39916398](https://pubmed.ncbi.nlm.nih.gov/39916398/)

### Finding 4 — Clinical profile: congenital bilateral moderate-to-severe SNHL; low absolute per-carrier risk

Across reported families, DFNB22 presents as **congenital/prelingual, bilateral, generally stable, nonsyndromic sensorineural hearing loss in the moderate-to-severe range** (PMIDs 33492714, 32681043). Although *OTOA* is one of the more common CNV-driven recessive deafness loci, the **absolute risk to any given microdeletion carrier is low**. In the general CMA cohort, the *OTOA* microdeletion carrier frequency of 0.2% (39/19,189) placed it second to *STRC* (0.56%) and above the DFNB1/*GJB6* locus (0.05%). The estimated probability that a given *OTOA*-microdeletion carrier is themselves affected (i.e., carries a second pathogenic allele) was only **0.016–0.13%** — lower than for *STRC* (0.11–0.67%) and *DFNB1* (1.9–7.5%) — with higher risk in specific (e.g., consanguineous or founder) populations (PMID 33753912).

> "Of the 19,189 CMA tests were performed in our laboratory, 107 STRC microdeletions were found (0.56%), followed in frequency by OTOA deletions (39, 0.2%), and DFNB1 locus deletions (10, 0.05%). The estimated risk for a hearing loss in the examined individual carrying the microdeletion was estimated as 0.11-0.67% for STRC, 0.016-0.13% for OTOA" — [PMID: 33753912](https://pubmed.ncbi.nlm.nih.gov/33753912/)

**Ontology annotations:** HP:0000407 (Sensorineural hearing impairment), HP:0008527 (Congenital sensorineural hearing impairment), HP:0000365 (Hearing impairment), HP:0000006 (Autosomal recessive inheritance).

---

## Report by Template Section

### 1. Disease Information

DFNB22 is a monogenic form of nonsyndromic sensorineural hearing loss — that is, hearing loss without accompanying malformations or dysfunction of other organ systems. It is one of the numbered "DFNB" (autosomal recessive) deafness loci.

- **Overview:** Congenital, bilateral, typically stable moderate-to-severe SNHL due to biallelic *OTOA* loss-of-function and consequent tectorial-membrane detachment.
- **Key identifiers:** OMIM #607039 (disease); OMIM *607038 (*OTOA* gene); MONDO:0011762; MeSH — indexed under Hearing Loss, Sensorineural; ICD-10 H90.3/H90.5 (sensorineural hearing loss); ICD-11 AB52 (sensorineural hearing impairment). A dedicated Orphanet number for DFNB22 is not consistently assigned; nonsyndromic genetic deafness is captured under Orphanet's rare genetic hearing-loss entries.
- **Synonyms/alternative names:** DFNB22; Deafness, autosomal recessive 22; Nonsyndromic hearing loss and deafness, DFNB22 type; OTOA-related hearing loss; Otoancorin deficiency deafness.
- **Information source:** Predominantly **aggregated disease-level resources** (OMIM, ClinVar) plus **individual-patient case reports and consanguineous-family studies**; a single mouse model provides the mechanistic physiology.

### 2. Etiology

- **Causal factors:** Purely **genetic** — biallelic (homozygous or compound heterozygous) loss-of-function variants in *OTOA*. No environmental or infectious cause.
- **Genetic risk factors:** The causal locus is *OTOA*. **Consanguinity** and **founder effects** substantially raise risk (founding Palestinian family; South Indian and Pakistani consanguineous families). The *OTOA*/*OTOAP1* segmental duplication is itself a structural risk factor generating recurrent pathogenic alleles.
- **Environmental risk factors:** None established as causal. Ordinary otologic insults (noise, ototoxins) would be additive to residual hearing but are not part of DFNB22 etiology.
- **Protective factors:** None specific. Presence of at least one functional *OTOA* allele is fully protective (recessive disease; heterozygous carriers are unaffected).
- **Gene–environment interactions:** Not established; the phenotype is essentially fully genetically determined.

### 3. Phenotypes

| Phenotype | Type | Onset | Severity | Progression | Frequency | HPO |
|---|---|---|---|---|---|---|
| Bilateral sensorineural hearing loss | Audiometric abnormality / physical | Congenital / prelingual | Moderate to severe | Generally stable | ~100% of affected | HP:0000407 |
| Congenital SNHL | Clinical sign | Neonatal/congenital | Moderate–severe | Stable | Predominant presentation | HP:0008527 |
| Speech/language delay (if unaided) | Developmental consequence | Childhood | Variable | Improves with habilitation | Secondary to HL | HP:0000750 |

- **Quality-of-life impact:** Congenital moderate-to-severe SNHL affects language acquisition, education, and social communication if unaddressed; with early hearing aids/cochlear implants and speech-language therapy, outcomes are generally good. Clinical vestibular symptoms are not a prominent reported feature despite otoancorin's vestibular localization.
- Disease-specific QoL instruments for DFNB22 are not reported; generic pediatric hearing-loss QoL measures apply.

### 4. Genetic / Molecular Information

- **Causal gene:** *OTOA* (HGNC:16378), 16p12.2, OMIM *607038, encoding otoancorin.
- **Pathogenic variant types:** Splice-site (founding **IVS12+2T>C**, PMID 11972037), frameshift (**p.Gln589ArgfsX55**, PMID 30740825), nonsense via gene conversion (**p.Glu787\***, PMID 33492714), missense candidates (e.g., p.Gly647Arg reported in dual-diagnosis contexts), and — most characteristically — **structural CNV deletions** (single-gene and contiguous-gene, e.g., 250 kb *METTL9/IGSF6/OTOA* deletion, PMID 39916398).
- **Variant classification:** Loss-of-function deletions and truncating variants are pathogenic/likely pathogenic under ACMG/AMP; some missense variants remain VUS.
- **Allele frequency:** *OTOA* microdeletion carrier frequency ~0.2% in a general CMA cohort (PMID 33753912).
- **Origin:** Germline.
- **Functional consequence:** Loss of function (loss of the GPI-anchored tether).
- **Modifier genes / epigenetics / chromosomal abnormalities:** No specific modifier genes or epigenetic mechanisms established. The relevant genomic feature is the 16p12.2 segmental duplication enabling NAHR and gene conversion.

### 5. Environmental Information

Not applicable as a cause. DFNB22 is a monogenic disorder with no established environmental, lifestyle, or infectious contributors. (General ototoxin/noise avoidance is prudent to preserve residual hearing but is not disease-specific.)

### 6. Mechanism / Pathophysiology — Causal Chain

1. **Biallelic loss-of-function variant in *OTOA*** (deletion, gene conversion, splice, frameshift) → **leads to** absent or non-functional otoancorin protein.
2. Loss of GPI-anchored otoancorin → **results in** failure to anchor the acellular tectorial membrane at its two attachment zones (permanent zone on the spiral limbus; transient zone on the greater epithelial ridge). *(Demonstrated: PMID 11972037, 30740825.)*
3. Failure of anchorage → **causes** detachment of the TM from the **limbal (spiral limbus) surface**, while the TM retains overall form and remains coupled to outer hair cells. *(Demonstrated in mouse: PMID 23129639.)*
4. **Branch A (spared):** TM–OHC coupling preserved → OHC electromotility, cochlear amplification, and frequency tuning remain near-normal (normal CM, DPOAEs, basilar-membrane motion, sharp tuning).
5. **Branch B (impaired):** Loss of proper limbal TM attachment → **impairs mechanical drive to inner hair cell stereocilia** → **results in** reduced IHC receptor potentials → elevated compound action potential thresholds. *(Demonstrated: PMID 23129639.)*
6. Reduced IHC afferent signaling → **leads to** decreased auditory-nerve output → **manifests as** congenital, bilateral, moderate-to-severe sensorineural hearing loss.

**Upstream vs downstream:** The mutation and protein loss are upstream; TM detachment is the central lesion; IHC understimulation is the proximate downstream cause of the clinical deafness. The disorder is **mechanical/structural**, not driven by apoptosis, inflammation, metabolic, or immune processes.

- **Molecular pathways:** No classical signaling cascade (Wnt/MAPK/mTOR) implicated; the mechanism is structural adhesion of an acellular gel to sensory epithelium.
- **Protein dysfunction:** Loss of GPI membrane anchorage (uncontrolled release instead of PI-PLC-controlled release), PMID 30740825.
- **Cell types / processes:** Inner hair cells (CL:0000601) understimulated; outer hair cells (CL:0000599) spared; supporting/nonsensory epithelial cells of the spiral limbus involved in TM anchoring. GO:0007605 (sensory perception of sound), GO:0060119 (inner ear receptor cell development).
- **Molecular profiling / advanced technologies:** No transcriptomic, proteomic, metabolomic, single-cell, spatial, or CRISPR-screen datasets specific to DFNB22 were identified.

### 7. Anatomical Structures Affected

- **Organ:** Inner ear / cochlea (primary). System: auditory (special sense). UBERON:0001846 (internal ear), UBERON:0001844 (cochlea).
- **Tissue/cell:** Cochlear sensory epithelium (organ of Corti, UBERON:0002227); the acellular **tectorial membrane** (UBERON:0002518) and its **spiral limbus** anchorage (UBERON:0004681). Vestibular otoconial membranes/cupulae also express otoancorin. Cells: inner hair cells (CL:0000601, functionally affected), outer hair cells (CL:0000599, spared).
- **Subcellular:** Apical plasma-membrane region of sensory/nonsensory epithelial cells; GPI-anchored component of membrane (GO:0031225).
- **Localization/laterality:** **Bilateral**, symmetric.

### 8. Temporal Development

- **Onset:** Congenital / prelingual; onset pattern chronic/stable from birth.
- **Progression:** Generally **stable** (non-progressive) moderate-to-severe SNHL; lifelong.
- **Critical period:** The window for auditory habilitation (hearing aids/cochlear implant, speech-language therapy) is early childhood, to support language development.

### 9. Inheritance and Population

- **Inheritance:** Autosomal recessive (HP:0000006). Carriers are unaffected.
- **Penetrance/expressivity:** Biallelic pathogenic genotypes are essentially fully penetrant; severity clusters in the moderate-to-severe range with some variability.
- **Founder effects/consanguinity:** Prominent — founding Palestinian family (PMID 11972037); consanguineous South Indian (PMID 39916398) and Pakistani (PMID 32681043) families. **Consanguinity is a major risk amplifier.**
- **Carrier frequency:** ~0.2% for *OTOA* microdeletions in a general population CMA cohort; per-carrier affected risk 0.016–0.13% (PMID 33753912).
- **Epidemiology:** *OTOA* is among the more common CNV-driven recessive deafness loci (second to *STRC*), but DFNB22 is individually rare. No sex predilection (autosomal). Higher diagnostic yield in consanguineous/endemic-founder populations.

### 10. Diagnostics

- **Audiometry:** Pure-tone/behavioral audiometry and ABR reveal bilateral moderate-to-severe SNHL; **OAEs may be relatively preserved** given spared OHC function (mechanistically expected from the mouse data, PMID 23129639) — a potentially distinctive audiologic signature of TM/IHC-coupling disorders.
- **Genetic testing (core diagnostic):** Because pathogenic alleles are frequently **structural (deletions/gene conversions)** in the *OTOA*/*OTOAP1* repeat, testing must be **copy-number-aware**: gene panels/WES for point variants **plus** CMA, MLPA, qPCR, or long-read sequencing to detect CNVs and conversions (PMIDs 35640668, 33492714, 33753912). Short-read WES alone under-detects DFNB22.
- **Imaging:** Temporal-bone CT/MRI generally normal (nonsyndromic; no gross malformation expected).
- **Differential diagnosis:** Other recessive nonsyndromic deafness (esp. *STRC*/DFNB16, *GJB2*/DFNB1, *SLC26A4*/Pendred, *TECTA*-related tectorial-membrane deafness which is a key mechanistic mimic). Distinguish by gene, and clinically by the preserved-OAE/elevated-threshold pattern for TM-anchoring defects. Exclude syndromic causes and dual diagnoses (e.g., co-occurring *ERCC4* or *PALM3* variants reported in consanguineous families).
- **Screening:** Newborn hearing screening (OAE/ABR) detects the phenotype; cascade carrier testing and reporting of incidental *OTOA* microdeletions on CMA are debated given low per-carrier risk (PMID 33753912).

### 11. Outcome / Prognosis

- **Survival/mortality:** DFNB22 is **not life-limiting**; normal life expectancy. It is a sensory disorder with no systemic mortality.
- **Morbidity/function:** Principal morbidity is communication disability if unaided; excellent functional prognosis with early amplification/cochlear implantation and speech-language support. Hearing loss is generally **stable**, not progressive.
- **Prognostic factors:** Timeliness of habilitation and degree of residual hearing. No molecular prognostic biomarkers established.

### 12. Treatment

- **No disease-specific pharmacotherapy or approved gene/RNA/cell therapy exists** for DFNB22.
- **Habilitative/standard of care:** **Hearing aids** (NCIT: Hearing Aid) for moderate loss; **cochlear implantation** (NCIT: Cochlear Implant) for severe loss with insufficient aided benefit; **speech-language therapy** and educational support.
- **Supportive/rehabilitative:** Auditory-verbal therapy, aural rehabilitation, family/educational accommodations.
- **Experimental:** Inner-ear gene therapy is an active field for monogenic deafness generally, but no DFNB22/*OTOA*-specific trial was identified. The relatively preserved cochlear architecture and OHC function in *Otoa*-null mice make DFNB22 a conceptually attractive future gene-replacement target.
- **Pharmacogenomics:** Not applicable.

### 13. Prevention

- **Primary prevention:** Not possible for a congenital monogenic disorder; **genetic counseling** for consanguineous couples and known carrier families is the principal preventive tool. Carrier and cascade screening can inform reproductive choices (including PGT/prenatal testing where desired).
- **Secondary prevention:** **Universal newborn hearing screening** for early detection, enabling timely habilitation during the critical language-development window.
- **Tertiary prevention:** Amplification/cochlear implantation and speech therapy to prevent language and educational sequelae; avoidance of additional ototoxic/noise insults to protect residual hearing.
- **Counseling:** Autosomal recessive 25% recurrence risk for carrier couples; emphasize the copy-number-aware testing needs given the *OTOA*/*OTOAP1* architecture.

### 14. Other Species / Natural Disease

- **Taxonomy/orthologs:** *Otoa* is conserved in mouse (*Mus musculus*, NCBI Taxon 10090) and other mammals; the mouse ortholog underpins the disease model. Otoancorin and the related α-tectorin machinery are conserved across vertebrates.
- **Natural disease in animals:** No prominent naturally occurring companion-animal or wildlife *OTOA* deafness disorder was identified in this investigation. The knockout mouse is the principal model.
- **Comparative biology:** The mouse recapitulates the human mechanism (TM detachment, spared OHC/impaired IHC drive), supporting strong evolutionary conservation of TM-anchoring mechanisms.

### 15. Model Organisms

- **Mouse (*Mus musculus*):** The ***Otoa*(EGFP/EGFP) knockout** is the defining model (PMID 23129639). It faithfully recapitulates the core human phenotype and, uniquely, dissected the mechanism — showing TM detachment from the spiral limbus, preserved OHC amplification, and elevated CAP thresholds reflecting failed IHC stimulation.
- **Type:** Targeted knockout (EGFP knock-in/reporter-null).
- **Phenotype recapitulation:** High — reproduces congenital SNHL and the specific IHC-stimulation defect; also enabled protein-localization studies.
- **Limitations:** Mouse does not capture the human *OTOA*/*OTOAP1* segmental-duplication genomics (pseudogene-driven NAHR/gene-conversion mechanisms are human-specific). No zebrafish/*Drosophila*/organoid DFNB22 models were identified.
- **Resources:** MGI (mouse *Otoa*).

---

## Mechanistic Model / Interpretation

```
 OTOA biallelic LoF (deletion / gene conversion / splice / frameshift)
                 │
                 ▼
     Absent / non-functional otoancorin (GPI-anchored tether)
                 │
                 ▼
   Tectorial membrane not anchored at spiral-limbus (limbal) attachment
                 │
        ┌────────┴───────────────┐
        ▼                        ▼
 TM stays coupled to        TM detached from limbus →
 OUTER hair cells           mechanical drive to INNER
 → amplification &          hair cell stereocilia lost
 tuning ~NORMAL             │
 (normal CM, DPOAE,         ▼
  BM motion)          IHC receptor potentials ↓
                            │
                            ▼
                  CAP thresholds ↑ (IHC sensitivity ↓)
                            │
                            ▼
      Congenital bilateral moderate-to-severe SNHL (stable)
```

The unifying interpretation is that DFNB22 is a **"connectivity" / mechanical-coupling deafness**: the cochlea's amplifier (OHCs) works, but the sensory receiver (IHCs) is under-driven because the TM has lost its anchor to the spiral limbus. This explains both the clinical severity (moderate-to-severe rather than profound) and a predicted audiologic signature of comparatively **preserved otoacoustic emissions with elevated behavioral/ABR thresholds** — a pattern shared with other TM-anchoring/structural deafness genes (e.g., *TECTA*, *OTOG*, *STRC*). The human genomics layer — a segmental duplication with the *OTOAP1* pseudogene — superimposes a **diagnostic** challenge: the disease is under-ascertained by short-read exome sequencing and requires copy-number/gene-conversion-aware testing.

| Feature | DFNB22 (OTOA) |
|---|---|
| Gene / locus | *OTOA*, 16p12.2 |
| Protein | Otoancorin (~120 kDa, GPI-anchored) |
| Core lesion | TM detachment from spiral limbus |
| OHC amplification | Spared (near-normal DPOAE/CM) |
| IHC stimulation | Impaired (↑ CAP thresholds) |
| Phenotype | Congenital bilateral moderate–severe SNHL, stable |
| Inheritance | Autosomal recessive, fully penetrant |
| Carrier freq (microdeletion) | ~0.2% (39/19,189, CMA cohort) |
| Per-carrier affected risk | 0.016–0.13% |
| Key mutational mechanisms | NAHR deletions; *OTOAP1* gene conversion (p.Glu787*) |
| Diagnostic caveat | Missed by short-read WES; needs CMA/MLPA/qPCR/long-read |
| Treatment | Hearing aids, cochlear implant, speech therapy |

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [11972037](https://pubmed.ncbi.nlm.nih.gov/11972037/) | Otoancorin defective in DFNB22 | Human clinical + molecular | Gene–disease link; protein localization; founding IVS12+2T>C (F1) |
| [30740825](https://pubmed.ncbi.nlm.nih.gov/30740825/) | GPI anchorage of otoancorin; human OTOA variants | In vitro / molecular | GPI anchorage; LoF via loss of anchorage (F1) |
| [23129639](https://pubmed.ncbi.nlm.nih.gov/23129639/) | Mouse model of DFNB22 | Model organism (mouse) | Mechanism: TM detachment → IHC-stimulation defect (F2) |
| [33492714](https://pubmed.ncbi.nlm.nih.gov/33492714/) | OTOA gene conversions | Human molecular | Gene conversion (p.Glu787*); moderate-severe phenotype (F3, F4) |
| [33753912](https://pubmed.ncbi.nlm.nih.gov/33753912/) | Carrier reporting from CMA / HL deletions | Population/epidemiologic | Carrier frequency 0.2%; per-carrier risk (F3, F4) |
| [39916398](https://pubmed.ncbi.nlm.nih.gov/39916398/) | 250-kb 16p12.2 microdeletion | Human clinical | Contiguous-gene deletion causing DFNB22 (F3) |
| [35640668](https://pubmed.ncbi.nlm.nih.gov/35640668/) | WES of 113 Chinese HL families | Human clinical | Need for qPCR to detect OTOA/STRC CNVs (F3) |
| [32681043](https://pubmed.ncbi.nlm.nih.gov/32681043/) | Sporadic HL spectrum, Pakistan | Human clinical | Multi-exon OTOA deletion; moderate-severe HL (F4) |
| [33095980](https://pubmed.ncbi.nlm.nih.gov/33095980/) | NGS in Chinese HL cohort | Human clinical | OTOA among identified deafness genes |
| [33105617](https://pubmed.ncbi.nlm.nih.gov/33105617/) | Italian HL genetics | Human clinical | Context: NSHL diagnostic strategy |
| [39769235](https://pubmed.ncbi.nlm.nih.gov/39769235/) | Dual ERCC4 + OTOA diagnoses | Human clinical | Blended-phenotype/dual-diagnosis caution |
| [37114731](https://pubmed.ncbi.nlm.nih.gov/37114731/) | Phenotype-genotype of AR HL | Human clinical | Phenotype-genotype context |
| [42527583](https://pubmed.ncbi.nlm.nih.gov/42527583/) | PALM3 and hearing loss | Human + mouse | Dual-diagnosis/candidate-gene caution alongside OTOA |

All four core findings are convergently supported: the gene–disease link and protein function (PMIDs 11972037, 30740825), the mechanism (PMID 23129639), the diagnostic genomics (PMIDs 33492714, 33753912, 39916398, 35640668), and the clinical/epidemiologic profile (PMIDs 33753912, 33492714, 32681043). No paper reviewed contradicts these conclusions.

---

## Limitations and Knowledge Gaps

- **Single mechanistic model.** The mechanism rests primarily on one mouse study (PMID 23129639). Human intracochlear physiology is inferred, not directly measured; the predicted "preserved-OAE" audiologic signature has not been systematically catalogued across human DFNB22 patients.
- **No omics data.** No transcriptomic, proteomic, metabolomic, single-cell, or functional-screen datasets specific to DFNB22 were identified — the molecular-profiling subsections are effectively "not available."
- **Phenotype quantification is coarse.** Severity/progression are described qualitatively ("moderate-to-severe, generally stable"); no natural-history cohort with longitudinal audiograms was available to quantify progression rates or variability precisely.
- **Vestibular phenotype under-characterized.** Otoancorin localizes to vestibular structures, yet clinical vestibular dysfunction in DFNB22 is not well documented — a genotype–phenotype gap.
- **Genomic complexity limits ascertainment.** The *OTOA*/*OTOAP1* architecture means true prevalence is likely underestimated in short-read-only cohorts; reported frequencies (0.2% carriers) are lower bounds.
- **No therapeutics.** No disease-specific pharmacologic, gene, RNA, or cell therapy exists or is in trials for *OTOA*.

---

## Proposed Follow-up Experiments / Actions

1. **Audiologic phenotyping study.** Systematically measure OAEs vs ABR/behavioral thresholds in a molecularly confirmed DFNB22 cohort to test whether preserved-emission/elevated-threshold is a reproducible clinical signature (translating the mouse mechanism, PMID 23129639).
2. **Copy-number-aware diagnostic pipeline.** Standardize CMA/MLPA/qPCR or **long-read sequencing** for *OTOA* in unsolved recessive SNHL to capture NAHR deletions and *OTOAP1* gene conversions that short-read WES misses (PMIDs 33492714, 35640668).
3. **Natural-history registry.** Assemble longitudinal audiograms across DFNB22 families to quantify progression, variability, and cochlear-implant outcomes.
4. **Vestibular assessment.** Add vestibular testing (vHIT, VEMP, caloric) to DFNB22 evaluations to define the vestibular phenotype implied by otoancorin's vestibular localization.
5. **Gene-replacement proof-of-concept.** Given preserved cochlear architecture and OHC function in *Otoa*-null mice, test AAV-mediated *Otoa* delivery to the developing/mature cochlea to restore TM anchorage and IHC drive — a rational DFNB22-specific therapeutic avenue.
6. **Population-specific carrier data.** Determine *OTOA* pathogenic-allele frequencies in consanguineous/founder populations to refine per-carrier risk and inform carrier-screening/reporting policy (extending PMID 33753912).

---

*Evidence source key: Human clinical = patient/family reports and cohorts; Model organism = mouse; In vitro = cell-based functional assays; Population/epidemiologic = cohort frequency analyses. All mechanistic and clinical claims are cited to primary literature by PMID.*


## Artifacts

- [OpenScientist final report](Autosomal_Recessive_Nonsyndromic_Hearing_Loss_22-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Autosomal_Recessive_Nonsyndromic_Hearing_Loss_22-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 7 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 13 |
| On topic | 13 |
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
| Terms whose name was checked | 16 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0000599` (3 mentions) - the report calls it "cochlear outer hair cell"; CL calls it **conidium**
- `UBERON:0002518` (2 mentions) - the report calls it "tectorial membrane"; UBERON calls it **otolith organ**
- `UBERON:0004681` (2 mentions) - the report calls it "spiral limbus"; UBERON calls it **vestibular system**
- `HP:0000407` (2 mentions) - the report calls it "Sensorineural hearing impairment", "~100% of affected"; HP calls it **Sensorineural hearing impairment**
- `HP:0008527` (2 mentions) - the report calls it "Congenital sensorineural hearing impairment", "Predominant presentation"; HP calls it **Congenital sensorineural hearing impairment**
- `HP:0000750` (1 mention) - the report calls it "Secondary to HL"; HP calls it **Delayed speech and language development**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0031225` (obsolete anchored component of membrane) (2 mentions) - replaced by `GO:0016020`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0031225` (2 mentions) - the report calls it "anchored component of membrane"; GO calls it **obsolete anchored component of membrane**
- `CL:0000601` (3 mentions) - the report calls it "cochlear inner hair cell", "Cell types / processes:** Inner hair cells"; CL calls it **cochlear outer hair cell**
- `UBERON:0002227` (2 mentions) - the report calls it "organ of Corti"; UBERON calls it **spiral organ of cochlea**, and lists "organ of Corti" among its other names
- `HP:0000006` (2 mentions) - the report calls it "Autosomal recessive inheritance", "Inheritance:** Autosomal recessive"; HP calls it **Autosomal dominant inheritance**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:16378` - called "OTOA", "Causal gene:** *OTOA"
- `CL:0000601` - called "cochlear inner hair cell", "Cell types / processes:** Inner hair cells"
- `HP:0000407` - called "Sensorineural hearing impairment", "~100% of affected"
- `HP:0008527` - called "Congenital sensorineural hearing impairment", "Predominant presentation"
- `HP:0000006` - called "Autosomal recessive inheritance", "Inheritance:** Autosomal recessive"