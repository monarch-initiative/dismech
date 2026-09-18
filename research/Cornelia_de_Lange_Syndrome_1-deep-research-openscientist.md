---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-05T19:09:56.958300'
end_time: '2026-09-05T19:27:44.841555'
duration_seconds: 1067.88
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cornelia de Lange Syndrome 1
  mondo_id: MONDO:0007387
  category: Genetic
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
citation_count: 33
reference_validation:
  total_references: 33
  verified: 33
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 19
  quotes_valid: 19
  relevance_assessed: 33
  on_topic: 21
  off_topic: 1
  off_topic_references:
  - PMID:36053618
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 44
  verified: 40
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 17
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: GO:0032116
    reported_labels:
    - "sister chromatid cohesion \u2014 the *canonical* cohesin function, notably\
      \ NOT the primary disease driver"
    ontology_label: SMC loading complex
  - term_id: HP:0000750
    reported_labels:
    - Delayed speech and language development
    - Absent phrase speech by age 5
    ontology_label: Delayed speech and language development
  - term_id: HP:0002194
    reported_labels:
    - Delayed gross motor development
    - Not walking by age 5
    ontology_label: Delayed gross motor development
  - term_id: HP:0009821
    reported_labels:
    - Forearm undergrowth
    - Upper-limb reduction defects
    ontology_label: Forearm undergrowth
  - term_id: HP:0012443
    reported_labels:
    - Abnormal brain morphology
    - CNS malformation
    ontology_label: Abnormal brain morphology
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0035064
    ontology_label: obsolete methylated histone binding
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Cornelia_de_Lange_Syndrome_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Cornelia_de_Lange_Syndrome_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cornelia de Lange Syndrome 1
- **MONDO ID:** MONDO:0007387 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Cornelia de Lange Syndrome 1** covering all of the
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

# Cornelia de Lange Syndrome 1 (CdLS1): Comprehensive Disease Characteristics Report

**Target Disease:** Cornelia de Lange Syndrome type 1 (CdLS1)
**MONDO ID:** MONDO:0007387 | **OMIM:** #122470 | **Orphanet:** ORPHA:199
**Category:** Genetic (autosomal dominant cohesinopathy / transcriptomopathy)
**Evidence base:** 43 papers reviewed; 10 findings confirmed across 5 investigation iterations

---

## Summary

Cornelia de Lange syndrome type 1 (CdLS1) is a rare, dominantly inherited, multisystem developmental disorder caused by heterozygous loss-of-function variants in **NIPBL** (Nipped-B-like), the gene encoding the principal cohesin-loading factor. NIPBL variants account for **more than 60%** of all molecularly diagnosed CdLS, defining "type 1" and distinguishing it from the ~15% of cases attributable to other cohesin-complex genes (*SMC1A*, *SMC3*, *RAD21*, *HDAC8*). Inheritance is autosomal dominant, and nearly all constitutional cases are *de novo*; there is no measurable parental-age effect and essentially all cases are sporadic. The disorder is defined clinically by a recognizable craniofacial gestalt (synophrys, arched eyebrows, long philtrum, thin down-turned lips), pre- and postnatal growth retardation, upper-limb reduction defects, generalized hirsutism, intellectual disability, and a distinctive neurobehavioral profile featuring self-injurious and repetitive behaviors.

Mechanistically, CdLS1 is best understood as a **transcriptomopathy** rather than a disorder of sister-chromatid cohesion. NIPBL loads the cohesin ring onto chromatin; haploinsufficiency reduces genome-wide cohesin binding — including at CTCF boundaries — collapses cohesin-mediated chromatin loops, and impairs RNA polymerase II transcription initiation and elongation. The net result is thousands of individually modest (<1.5-fold) gene-expression changes that, acting collectively, disrupt developmental programs — with cell-identity and developmental genes preferentially deregulated because NIPBL supports their unique 3D genome conformation near super-enhancers. This model is validated in *Nipbl*+/− mice and *nipbl*-deficient zebrafish, and a candidate therapeutic lead has emerged: inhibition of the MORF acetyltransferase **KAT6B** partially rescues insulator defects in NIPBL-deficient cells.

Clinically, CdLS1 carries substantial morbidity and mortality. Congenital heart defects occur in roughly one-third of patients (pulmonary stenosis most common); feeding difficulty is severe, with about one in four children requiring gastrostomy by age 5; and congenital diaphragmatic hernia (CDH), though less frequent, is a major driver of mortality (cause of death in 5–20% of cases; 76% mortality in CdLS-CDH infants). Population prevalence of the classical form is approximately 1.2–2.2 per 100,000 births, with a broader clinical estimate of 1 in 10,000–30,000 live births when milder phenotypes are included. There is currently no curative therapy; management is symptomatic and multidisciplinary.

---

## Key Findings

### Finding 1 — NIPBL loss-of-function causes the majority (~60%) of CdLS, defining type 1

Pathogenic variants in *NIPBL* are identified in **more than 60%** of patients with CdLS, establishing NIPBL as the major causal gene and defining CdLS type 1 (OMIM #122470). NIPBL encodes a cohesin-loading factor (a regulatory/loader subunit of the cohesin machinery). The remaining molecularly solved cases are distributed across other cohesin-complex genes: pathogenic variants in *SMC1A*, *SMC3*, *RAD21*, and *HDAC8* together account for roughly another 15%. As stated in the *Cornelia de Lange Spectrum* review, "Pathogenic variants in NIPBL, which encodes a protein related to the cohesin complex, have been identified in more than 60% of patients, and pathogenic variants in other genes related to this complex in another 15%: SMC1A, SMC3, RAD21, and HDAC8" ([PMID: 38735830](https://pubmed.ncbi.nlm.nih.gov/38735830/)). The first international consensus statement confirms the cohesinopathy framework: CdLS "is caused by variants in any one of seven genes, all of which have a structural or regulatory function in the cohesin complex" ([PMID: 29995837](https://pubmed.ncbi.nlm.nih.gov/29995837/)).

Inheritance is autosomal dominant and nearly all constitutional cases arise *de novo*. A clinically important genotype–phenotype correlation exists: **truncating (loss-of-function) NIPBL variants generally cause a more severe phenotype than missense variants**, though the correlation is not absolute — "Truncating mutations were generally found to cause a more severe phenotype but this correlation was not absolute" ([PMID: 16236812](https://pubmed.ncbi.nlm.nih.gov/16236812/)). Consistent with this, a start-loss variant (NM_133433.4:c.2T>A; p.Met1Lys) was associated with a comparatively **mild** presentation, hypothesized to reflect use of downstream alternative start sites ([PMID: 42069659](https://pubmed.ncbi.nlm.nih.gov/42069659/)).

**Ontology anchors:** HGNC:28862 (NIPBL); MONDO:0007387; OMIM:122470.

### Finding 2 — Pathogenesis is driven by cohesin-dependent transcriptional dysregulation, not defective cohesion

A central mechanistic insight is that CdLS1 arises from **impaired gene regulation** rather than from failed sister-chromatid cohesion. NIPBL loads cohesin onto chromatin; when NIPBL is haploinsufficient, there is a genome-wide reduction in cohesin binding. In the *Nipbl* haploinsufficient mouse model, investigators "found a global decrease in cohesin binding, including at CCCTC-binding factor (CTCF) binding sites and repeat regions. Cohesin-bound genes were found to be enriched for histone H3 lysine 4 trimethylation (H3K4me3) at their promoters" — with such promoter-bound genes disproportionately downregulated ([PMID: 28855971](https://pubmed.ncbi.nlm.nih.gov/28855971/)).

Downstream of reduced cohesin loading, transcription itself is impaired. In CdLS patient cell lines, "mutant cohesin impairs both RNA polymerase II (Pol II) transcription initiation at promoters and elongation in the gene body" ([PMID: 26581180](https://pubmed.ncbi.nlm.nih.gov/26581180/)). This transcriptional signature is reproducible in disease-relevant human tissue: RNA-seq of NIPBL-mutant human iPSC-derived cardiomyocytes "identified hundreds of mRNAs, pseudogenes, and non-coding RNAs with altered expression" ([PMID: 29348408](https://pubmed.ncbi.nlm.nih.gov/29348408/)).

**Ontology anchors:** GO:0032116 (sister chromatid cohesion — the *canonical* cohesin function, notably NOT the primary disease driver); GO:0006357 (regulation of transcription by RNA polymerase II); GO:0007059 (chromosome segregation).

### Finding 3 — Postzygotic mosaicism is unusually common and undergoes negative selection in blood

CdLS shows an unusually high rate of somatic mosaicism, with major diagnostic implications. In a retrospective cohort plus literature review, mosaicism was found in **13.1% of patients with a positive molecular diagnosis** — "an unusual high prevalence of mosaicism in CdLS, occurring in 13.1% of patients with a positive molecular diagnosis" ([PMID: 34326454](https://pubmed.ncbi.nlm.nih.gov/34326454/)). Critically, there is **negative (purifying) selection against somatic deleterious NIPBL variants in blood**: "we demonstrate a negative selection against somatic deleterious NIPBL variants in blood." This means blood-based testing frequently misses mosaic variants, so buccal-swab or fibroblast testing is often required to reach a diagnosis. Mosaic cases have phenotypes at least as severe as constitutive variants, and mosaic missense substitutions preferentially localize to the HEAT-repeat domain of NIPBL.

**Clinical implication:** In a phenotypically classical patient with negative blood testing, proceed to alternative-tissue (buccal/fibroblast) sequencing before excluding a NIPBL etiology.

### Finding 4 — CdLS1 has a distinctive, more severe neurobehavioral phenotype than SMC1A-related CdLS

The neurobehavioral profile of CdLS1 is a defining feature. In a cohort of 50 children with CdLS, **all had at least one type of repetitive behavior and 44% displayed self-injurious behavior (SIB)**; lower adaptive functioning correlated with higher stereotypy and SIB: "All children had ≥ 1 type of RB; 44% had some form of SIB. 64% spent > 1 h/day displaying RBs. Lower VABS adaptive functioning was associated with higher stereotypy and SIB scores" ([PMID: 32809170](https://pubmed.ncbi.nlm.nih.gov/32809170/)).

Genotype stratifies severity: individuals with NIPBL variants show a more severe behavioral phenotype (more repetitive behaviors, tantrums) and greater developmental delay than those with *SMC1A* variants — "Individuals with SMC1A variants show a higher cognitive level and less SIB than individuals with NIPBL variants" ([PMID: 30295920](https://pubmed.ncbi.nlm.nih.gov/30295920/)). Developmental milestones are markedly delayed: approximately "70% not using phrase speech and 30-50% not walking by 5 years of age. However, those with NIPBL variants showed more severity in behavioral phenotype" ([PMID: 38462617](https://pubmed.ncbi.nlm.nih.gov/38462617/)). A clinical-severity score based on physical features correlates with communicative functioning, especially in NIPBL genotypes ([PMID: 40084492](https://pubmed.ncbi.nlm.nih.gov/40084492/)).

**Suggested HPO terms:** HP:0001249 (Intellectual disability), HP:0000717 (Autism), HP:0000733 (Stereotypy), HP:0100716 (Self-injurious behavior), HP:0000750 (Delayed speech and language development), HP:0002194 (Delayed gross motor development).

### Finding 5 — Vertebrate models recapitulate CdLS through collective small gene-expression changes

The mechanistic model is validated in animals. "Mouse and zebrafish models of CdLS" have been created "by using molecular genetic tools to create Nipbl-deficient mice and zebrafish (Nipbl(+/-) mice, zebrafish nipbl morphants)" ([PMID: 27120001](https://pubmed.ncbi.nlm.nih.gov/27120001/)). *Nipbl*+/− mice, which express roughly 30–75% of normal Nipbl transcript, and zebrafish morphants reproduce CdLS-like defects of gut, heart, craniofacial structures, nervous system, and limbs.

The zebrafish model established the "collective-perturbation" principle: hundreds of genes change expression, but "nearly all such changes are modest, however—usually less than 1.5-fold—raising the intriguing possibility that, in CdLS, severe developmental defects result from the collective action of many otherwise innocuous perturbations" ([PMID: 22039349](https://pubmed.ncbi.nlm.nih.gov/22039349/)). In these morphants, altered endodermal patterning genes (*sox32*, *sox17*, *foxa2*, *gata5*) and left–right patterning genes (*spaw*, *lefty2*, *dnah9*) are deregulated from gastrulation, providing a developmental-timing account of heart and gut defects.

**Suggested model/ontology anchors:** NCBITaxon:10090 (*Mus musculus*), NCBITaxon:7955 (*Danio rerio*); MGI allele resources for *Nipbl*.

### Finding 6 — Congenital heart defects occur in ~33% of patients; pulmonary stenosis predominates

In a prospective echocardiographic cohort of 87 Brachmann–de Lange (CdLS) patients, a cardiac anomaly was found in **29/87 (33.3%)**: "A cardiac anomaly was identified in 29/87 (33.3%) including 28 (32.2%) patients with a structural CHD, and an additional patient (1.2%) with isolated non-obstructive hypertrophic cardiomyopathy (HCM)" ([PMID: 19449412](https://pubmed.ncbi.nlm.nih.gov/19449412/)). The single most common lesion was pulmonary stenosis — "Overall incidence of pulmonary stenosis was 39% (11/28)." Late-onset mitral/tricuspid valve dysplasia appeared in four patients older than 10 years, supporting **ongoing echocardiographic surveillance** rather than a single neonatal screen. (Population registry data give a higher CHD frequency of 45.6% — see Finding 10 — likely reflecting ascertainment differences.)

**Suggested HPO terms:** HP:0001642 (Pulmonic stenosis), HP:0001631 (Atrial septal defect), HP:0001629 (Ventricular septal defect), HP:0001638 (Cardiomyopathy). **UBERON:0000948** (heart).

### Finding 7 — Feeding difficulty is severe: ~1 in 4 children require gastrostomy by age 5

Gastrointestinal and feeding morbidity is a hallmark. The population-based EUROlinkCAT data-linkage study (91,504 children with congenital anomalies vs 1,960,272 reference children across 9 European registries) found that whereas only 0.016% of reference children had a gastrostomy before age 5, "Around one in four children with Cornelia de Lange syndrome and Wolf-Hirschhorn syndrome had a gastrostomy" ([PMID: 36053618](https://pubmed.ncbi.nlm.nih.gov/36053618/)). Children with congenital anomalies overall were ~80× more likely to require gastrostomy. This reflects the combination of severe gastroesophageal reflux disease (GERD), oromotor dysfunction, and failure to thrive that characterizes CdLS1.

**Suggested HPO terms:** HP:0011968 (Feeding difficulties), HP:0002020 (Gastroesophageal reflux), HP:0001508 (Failure to thrive); NCIT intervention: Gastrostomy (NCIT:C15329). **UBERON:0000945** (stomach).

### Finding 8 — Congenital diaphragmatic hernia is a major driver of mortality

Congenital diaphragmatic hernia (CDH) is a well-recognized and lethal association. CDH is "the cause of death in 5%-20% of CdLS cases" ([PMID: 32762940](https://pubmed.ncbi.nlm.nih.gov/32762940/)). In the CDH Study Group cohort (1995–2019; 9,251 CDH patients, 21 with confirmed CdLS), CdLS+CDH infants fared markedly worse than non-CdLS CDH infants across every metric:

| Metric | CdLS + CDH | Non-CdLS CDH | p-value |
|---|---|---|---|
| Birth weight (kg) | 2.2 ± 0.57 | 2.9 ± 0.64 | <0.001 |
| 5-minute Apgar (median) | 6 | 7 | 0.014 |
| Underwent repair | 33% | 84.2% | <0.001 |
| Mortality | 76% | 29% | <0.001 |

"Mortality was 76% for CdLS patients compared with 29% for non-CdLS patients (p<0.001)" ([PMID: 32762940](https://pubmed.ncbi.nlm.nih.gov/32762940/)). Encouragingly, of the 7 CdLS patients who did undergo repair, 5 survived to discharge — suggesting that surgical candidacy, where feasible, can improve outcomes. CdLS is also recognized among the dysmorphic conditions associated with CDH in population registries ([PMID: 26625659](https://pubmed.ncbi.nlm.nih.gov/26625659/)).

**Suggested HPO term:** HP:0000776 (Congenital diaphragmatic hernia). **UBERON:0001103** (diaphragm).

### Finding 9 — NIPBL loss collapses chromatin loops and preferentially deregulates cell-identity genes — with KAT6B inhibition as a candidate rescue

Recent chromatin-conformation work refines the mechanism from "reduced cohesin binding" to "loss of specific regulatory loops." Acute NIPBL depletion in vivo rapidly diminishes many chromatin loops, and "NIPBL specifically regulates cell identity genes by supporting a unique local genome conformation defined by greater spatial proximity to nearby super-enhancers and weaker transcription start site insulation of genomic contacts" ([PMID: 41699137](https://pubmed.ncbi.nlm.nih.gov/41699137/)). This provides a compelling explanation for why a globally acting chromatin factor produces a *developmental* phenotype: the genes most dependent on NIPBL-supported conformation are precisely the cell-identity/developmental genes.

The loop-collapse mechanism is directly demonstrated in a differentiation model: "knockdown of cohesin loader NIPBL disrupts enhancer-promoter interactions and CTCF-mediated loops, leading to widespread transcriptional dysregulation," with increased Polycomb (PRC) domain contacts during pancreatic differentiation ([PMID: 41826481](https://pubmed.ncbi.nlm.nih.gov/41826481/)). Complementary work shows PDS5 proteins limit the cohesin–NIPBL complex lifetime to establish CTCF boundaries ([PMID: 42030945](https://pubmed.ncbi.nlm.nih.gov/42030945/)), and TACL single-cell imaging directly visualizes cohesin loop-extrusion dynamics and NIPBL-MAU2 transport ([PMID: 41102415](https://pubmed.ncbi.nlm.nih.gov/41102415/)).

Most importantly for translation, a druggable node has emerged: "inhibition of Kat6b partially rescues the insulator defects in cells lacking the cohesin loader Nipbl" ([PMID: 40060486](https://pubmed.ncbi.nlm.nih.gov/40060486/)). KAT6B (MORF) is a histone acetyltransferase, and its inhibition partially restores insulator function in NIPBL-deficient cells — a candidate therapeutic lead worth pursuing in disease models.

**Suggested GO terms:** GO:0140588 (chromatin looping), GO:0006357 (regulation of transcription by RNA Pol II), GO:0035064 (methylated histone binding).

### Finding 10 — Population prevalence ~1.2–2.2 per 100,000 births; all cases sporadic, no parental-age effect

The EUROCAT population-based study (8,558,346 births, 1980–2002) established registry-based prevalence: "we found the prevalence of the classical form of CdLS to be 1.24/100,000 births or 1:81,000 births and estimated the overall CdLS prevalence at 1.6-2.2/100,000" ([PMID: 18074387](https://pubmed.ncbi.nlm.nih.gov/18074387/)). Live births constituted 91.5% of cases with high first-week survival (91.4%). Population-level malformation frequencies were: "The most frequent associated congenital malformations were limb defects (73.1%), congenital heart defects (45.6%), central nervous system malformations (40.2%), and cleft palate (21.7%)." Crucially, "All patients were sporadic. Maternal and paternal age did not seem to be risk factors for CdLS."

The Spanish ECEMC registry independently reported a minimum prevalence of 0.97/100,000 live births, 100% limb reduction defects, and relatively young parents ([PMID: 9608092](https://pubmed.ncbi.nlm.nih.gov/9608092/)). A broader clinical estimate including milder cases is "Cornelia de Lange syndrome is estimated to occur in 1 out of every 10,000-30,000 live births" ([PMID: 41499064](https://pubmed.ncbi.nlm.nih.gov/41499064/)).

**Suggested HPO terms:** HP:0009821 (Forearm undergrowth), HP:0000175 (Cleft palate), HP:0012443 (Abnormal brain morphology), HP:0001511 (Intrauterine growth retardation).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous loss-of-function variant in NIPBL** (truncating > missense in severity; ~60% of CdLS) reduces functional NIPBL protein — the cohesin loader — to a haploinsufficient level (~30–75% of normal in models). *(Demonstrated — human genetics + mouse dosage models.)*
2. Reduced NIPBL **leads to** a genome-wide decrease in cohesin loading onto chromatin, including at CTCF boundary sites and repeat regions. *(Demonstrated — ChIP-seq in Nipbl+/− mouse.)*
3. Decreased chromatin-bound cohesin **results in** collapse of cohesin-mediated chromatin loops — weakening enhancer–promoter contacts and CTCF-mediated insulation, and increasing Polycomb-domain contacts. *(Demonstrated — Hi-C / acute-depletion and differentiation models.)*
4. Loop collapse **leads to** impaired RNA polymerase II transcription (both initiation at promoters and elongation in gene bodies), preferentially affecting **cell-identity/developmental genes** that depend on NIPBL-supported super-enhancer proximity. *(Demonstrated — patient cells; acute-depletion in vivo.)*
5. This produces **thousands of individually modest (<1.5-fold) gene-expression changes**. *(Demonstrated — zebrafish/mouse transcriptomics.)*
6. The **collective** action of these many small perturbations **results in** disrupted developmental programs across multiple organ primordia during embryogenesis — limb bud, cardiac/left-right patterning, foregut/diaphragm, craniofacial, and CNS. *(Inferred integration of demonstrated components.)*
7. Organ-specific developmental failure **leads to** the clinical phenotype: limb reduction defects, congenital heart disease (esp. pulmonary stenosis), congenital diaphragmatic hernia, GI/feeding failure, craniofacial gestalt, growth retardation, intellectual disability, and self-injurious/repetitive behavior. *(Demonstrated clinically.)*

```
 NIPBL LoF variant (~60% of CdLS)
        │  (haploinsufficiency, ~30-75% dosage)
        ▼
 ↓ Genome-wide cohesin loading  ──────────────┐
        │                                      │ (CTCF sites, repeats)
        ▼                                      ▼
 Collapse of chromatin loops        Weakened CTCF insulation
 (enhancer–promoter contacts)       ↑ Polycomb-domain contacts
        │                                      │
        └──────────────┬───────────────────────┘
                       ▼
       Impaired RNA Pol II initiation + elongation
       (preferential hit to cell-identity/dev genes)
                       ▼
       Thousands of MODEST (<1.5x) expression changes
                       ▼
        ┌──────────────┼───────────────┬───────────────┐
        ▼              ▼               ▼               ▼
   Limb primordia  Cardiac/L-R    Foregut/diaphragm  CNS/craniofacial
                   patterning
        ▼              ▼               ▼               ▼
   Limb reduction  CHD (PS)     CDH + GERD/feeding   ID, SIB, gestalt
                                                     growth retardation
                       │
                       ▼
        Candidate intervention node:  KAT6B (MORF) inhibition
        partially rescues insulator defects in Nipbl-deficient cells
```

### Upstream vs downstream summary

| Layer | Event | Direction | Evidence |
|---|---|---|---|
| Genetic | NIPBL LoF | Most upstream | [PMID: 38735830](https://pubmed.ncbi.nlm.nih.gov/38735830/), [PMID: 16236812](https://pubmed.ncbi.nlm.nih.gov/16236812/) |
| Chromatin | ↓ cohesin loading; loop collapse | Upstream | [PMID: 28855971](https://pubmed.ncbi.nlm.nih.gov/28855971/), [PMID: 41699137](https://pubmed.ncbi.nlm.nih.gov/41699137/), [PMID: 41826481](https://pubmed.ncbi.nlm.nih.gov/41826481/) |
| Transcription | ↓ Pol II initiation/elongation | Intermediate | [PMID: 26581180](https://pubmed.ncbi.nlm.nih.gov/26581180/) |
| Transcriptome | Thousands of small changes | Intermediate | [PMID: 22039349](https://pubmed.ncbi.nlm.nih.gov/22039349/), [PMID: 29348408](https://pubmed.ncbi.nlm.nih.gov/29348408/) |
| Organ development | Multi-organ dysmorphogenesis | Downstream | [PMID: 27120001](https://pubmed.ncbi.nlm.nih.gov/27120001/) |
| Clinical | CHD, CDH, ID, SIB, limb defects | Most downstream | [PMID: 19449412](https://pubmed.ncbi.nlm.nih.gov/19449412/), [PMID: 32762940](https://pubmed.ncbi.nlm.nih.gov/32762940/), [PMID: 32809170](https://pubmed.ncbi.nlm.nih.gov/32809170/) |

---

## Section-by-Section Reference Content

### 1. Disease Information
CdLS1 is a congenital multisystem developmental disorder of the cohesin pathway. **Key identifiers:** OMIM #122470; Orphanet ORPHA:199; MONDO:0007387; MeSH "De Lange Syndrome" (D003635); ICD-10 Q87.1; ICD-11 LD2F.11. **Synonyms:** Cornelia de Lange syndrome, Brachmann–de Lange syndrome, de Lange syndrome, typus degenerativus amstelodamensis. Information is derived from **aggregated disease-level resources** (OMIM, Orphanet, consensus statements, cohort/registry studies) rather than individual EHR — see the international consensus statement ([PMID: 29995837](https://pubmed.ncbi.nlm.nih.gov/29995837/)) and clinical review ([PMID: 17508425](https://pubmed.ncbi.nlm.nih.gov/17508425/)).

### 2. Etiology
**Primary cause:** heterozygous germline (or postzygotic mosaic) loss-of-function variants in **NIPBL** (~60% of CdLS). **Genetic risk factors:** the causal variant itself; modifier effects include variant type (truncating > missense severity) and possible downstream translation-initiation rescue in start-loss variants. **Environmental risk factors:** none established — maternal and paternal age are NOT risk factors, and all cases are sporadic ([PMID: 18074387](https://pubmed.ncbi.nlm.nih.gov/18074387/)). **Protective factors:** no genetic or environmental protective factors are established; the milder end of the spectrum is driven by variant type and mosaicism. **Gene–environment interactions:** none demonstrated; CdLS1 is a monogenic disorder with variable expressivity attributable primarily to allelic and mosaic factors.

### 3. Phenotypes (with suggested HPO terms and frequencies)

| Phenotype | HPO term | Frequency | Evidence |
|---|---|---|---|
| Synophrys / arched eyebrows | HP:0000664 / HP:0002553 | Very frequent (gestalt-defining) | [PMID: 17508425](https://pubmed.ncbi.nlm.nih.gov/17508425/) |
| Intrauterine + postnatal growth retardation | HP:0001511 / HP:0001510 | Very frequent | [PMID: 9608092](https://pubmed.ncbi.nlm.nih.gov/9608092/) |
| Upper-limb reduction defects | HP:0009821 | 73.1% (registry); 100% (ECEMC severe) | [PMID: 18074387](https://pubmed.ncbi.nlm.nih.gov/18074387/), [PMID: 9608092](https://pubmed.ncbi.nlm.nih.gov/9608092/) |
| Congenital heart defect | HP:0001627 | 33% (echo cohort) – 45.6% (registry) | [PMID: 19449412](https://pubmed.ncbi.nlm.nih.gov/19449412/), [PMID: 18074387](https://pubmed.ncbi.nlm.nih.gov/18074387/) |
| CNS malformation | HP:0012443 | 40.2% | [PMID: 18074387](https://pubmed.ncbi.nlm.nih.gov/18074387/) |
| Cleft palate | HP:0000175 | 21.7% | [PMID: 18074387](https://pubmed.ncbi.nlm.nih.gov/18074387/) |
| Intellectual disability | HP:0001249 | Very frequent | [PMID: 38462617](https://pubmed.ncbi.nlm.nih.gov/38462617/) |
| Self-injurious behavior | HP:0100716 | 44% | [PMID: 32809170](https://pubmed.ncbi.nlm.nih.gov/32809170/) |
| Repetitive behavior | HP:0000733 | ~100% (≥1 type) | [PMID: 32809170](https://pubmed.ncbi.nlm.nih.gov/32809170/) |
| Absent phrase speech by age 5 | HP:0000750 | ~70% | [PMID: 38462617](https://pubmed.ncbi.nlm.nih.gov/38462617/) |
| Not walking by age 5 | HP:0002194 | 30–50% | [PMID: 38462617](https://pubmed.ncbi.nlm.nih.gov/38462617/) |
| Feeding difficulty / gastrostomy | HP:0011968 | ~25% require gastrostomy | [PMID: 36053618](https://pubmed.ncbi.nlm.nih.gov/36053618/) |
| Congenital diaphragmatic hernia | HP:0000776 | Minority, but high lethality | [PMID: 32762940](https://pubmed.ncbi.nlm.nih.gov/32762940/) |
| Hirsutism | HP:0001007 | 76.9% abnormal hair distribution | [PMID: 9608092](https://pubmed.ncbi.nlm.nih.gov/9608092/) |

**Onset:** congenital/prenatal. **Severity:** variable (mild to severe), correlating with genotype. **Progression:** the malformations are static/congenital, but behavioral and some cardiac (valve dysplasia) features can evolve. **Quality of life:** substantial impact — communication deficit, SIB, and feeding/GI morbidity dominate daily functioning ([PMID: 40084492](https://pubmed.ncbi.nlm.nih.gov/40084492/)).

### 4. Genetic / Molecular Information
**Causal gene:** *NIPBL* (HGNC:28862; chromosome 5p13.2; OMIM *608667). **Variant classes:** truncating (nonsense, frameshift, splice-site — most common and generally more severe), missense (often milder), and start-loss. **Functional consequence:** loss of function / haploinsufficiency of the cohesin loader. **Allele frequency:** pathogenic variants are absent from population databases (gnomAD) consistent with *de novo* origin. **Somatic vs germline:** predominantly germline *de novo*; but **13.1% mosaic** with negative selection in blood ([PMID: 34326454](https://pubmed.ncbi.nlm.nih.gov/34326454/)). **Other CdLS genes (non-type-1):** *SMC1A* (X-linked, CdLS2), *SMC3* (CdLS3), *RAD21* (CdLS4), *HDAC8* (CdLS5), plus *BRD4*, *ANKRD11*. **Epigenetic dimension:** the disease mechanism is itself epigenetic/architectural (cohesin loop extrusion, CTCF insulation, H3K4me3-promoter enrichment, Polycomb rewiring). **Chromosomal abnormalities:** rare 5p microdeletions encompassing NIPBL detectable by CMA.

### 5. Environmental Information
No environmental, lifestyle, or infectious contributing factors are established. CdLS1 is a fully genetic (monogenic) disorder with no demonstrated toxin, radiation, occupational, dietary, or pathogen association, and no parental-age effect ([PMID: 18074387](https://pubmed.ncbi.nlm.nih.gov/18074387/)).

### 6. Mechanism / Pathophysiology
Presented as the ordered causal chain above. Molecular pathways: cohesin loop extrusion / 3D genome architecture (not a classic signaling cascade like Wnt/MAPK, though TGF-β and other pathway genes are among the modestly deregulated targets, [PMID: 31516082](https://pubmed.ncbi.nlm.nih.gov/31516082/)). Cellular processes: transcriptional regulation, chromatin looping, developmental patterning. Protein dysfunction: NIPBL haploinsufficiency (loss of function). Subcellular localization: nucleus/chromatin (GO:0005694 chromosome; GO:0000785 chromatin).

### 7. Anatomical Structures Affected
**Primary/organ level:** limbs (UBERON:0002101), heart (UBERON:0000948), diaphragm (UBERON:0001103), brain/CNS (UBERON:0000955), craniofacial skeleton (UBERON:0010313), GI tract (UBERON:0001007), skin/hair (hirsutism). **Body systems:** musculoskeletal, cardiovascular, nervous, digestive, integumentary. **Tissue/cell level:** developing mesenchyme, neural tissue, cardiac and endodermal progenitors. **Subcellular:** nucleus/chromatin (GO:0000785). **Lateralization:** upper limbs predominantly affected, often asymmetric; limb reduction can be unilateral or bilateral.

### 8. Temporal Development
**Onset:** congenital (prenatal — detectable on ultrasound: growth retardation, limb defects, [PMID: 33478103](https://pubmed.ncbi.nlm.nih.gov/33478103/)). **Course:** structural malformations are static; behavioral phenotype and select cardiac valve lesions can progress (late mitral/tricuspid dysplasia >10 years, [PMID: 19449412](https://pubmed.ncbi.nlm.nih.gov/19449412/)). **Duration:** chronic, lifelong. **Critical periods:** embryonic organogenesis (limb, heart/left-right, diaphragm, craniofacial), when NIPBL-dependent developmental transcription is most vulnerable.

### 9. Inheritance and Population
**Prevalence:** classical form 1.24/100,000 (≈1:81,000); overall estimate 1.6–2.2/100,000 ([PMID: 18074387](https://pubmed.ncbi.nlm.nih.gov/18074387/)); broader clinical estimate 1 in 10,000–30,000 ([PMID: 41499064](https://pubmed.ncbi.nlm.nih.gov/41499064/)). **Inheritance:** autosomal dominant, nearly always *de novo*. **Penetrance:** high/complete for a recognizable phenotype; **expressivity:** highly variable. **Anticipation:** not applicable (not a repeat-expansion disorder). **Germline/somatic mosaicism:** common (13.1%). **Founder effects/consanguinity:** none (sporadic). **Sex ratio:** ~equal for NIPBL (autosomal); note SMC1A/HDAC8 are X-linked (different types). **Recurrence risk:** low for parents of a *de novo* case, but germline mosaicism warrants counseling.

### 10. Diagnostics
**Clinical criteria:** international consensus scoring (cardinal + suggestive features), [PMID: 29995837](https://pubmed.ncbi.nlm.nih.gov/29995837/); severity scoring correlates with brain changes and communication, [PMID: 17508425](https://pubmed.ncbi.nlm.nih.gov/17508425/), [PMID: 40084492](https://pubmed.ncbi.nlm.nih.gov/40084492/). **Genetic testing:** first-line molecular confirmation by gene panel or exome/genome sequencing targeting NIPBL and other cohesin genes; **if blood testing is negative in a classical patient, test buccal/fibroblast tissue** to detect blood-selected mosaicism ([PMID: 34326454](https://pubmed.ncbi.nlm.nih.gov/34326454/)). CMA detects 5p/NIPBL deletions. **Prenatal:** ultrasound features (limb defects, growth retardation, nuchal changes) plus molecular testing ([PMID: 33478103](https://pubmed.ncbi.nlm.nih.gov/33478103/)). **Differential diagnosis:** Fryns syndrome (esp. with CDH), fetal alcohol syndrome, Rubinstein–Taybi, Coffin–Siris, and other cohesinopathy subtypes; non-cohesin CdLS-like phenotypes exist ([PMID: 35935361](https://pubmed.ncbi.nlm.nih.gov/35935361/)).

### 11. Outcome / Prognosis
**Survival:** high first-week survival (91.4%) and 91.5% live births in registry data ([PMID: 18074387](https://pubmed.ncbi.nlm.nih.gov/18074387/)); most classical patients survive infancy. **Major mortality drivers:** CDH (cause of death in 5–20%; 76% mortality when present, [PMID: 32762940](https://pubmed.ncbi.nlm.nih.gov/32762940/)), severe congenital heart disease, and aspiration/GI complications. **Morbidity:** intellectual disability, communication impairment, SIB, feeding failure, GERD — chronic and lifelong. **Prognostic factors:** genotype (truncating NIPBL and NIPBL vs SMC1A predict greater severity), presence of CDH/major CHD, and clinical-severity score.

### 12. Treatment
There is **no curative or disease-modifying therapy**; management is symptomatic and multidisciplinary ([PMID: 31704779](https://pubmed.ncbi.nlm.nih.gov/31704779/)). Components: **GI/nutrition** — aggressive GERD management and gastrostomy for feeding failure (NCIT:C15329 Gastrostomy); **cardiac** — surgical/interventional repair of CHD and ongoing echocardiographic surveillance; **surgical** — CDH repair where the infant is a candidate (improves survival in the subset repaired); **behavioral/rehabilitative** — speech, occupational, and physical therapy; behavioral management of SIB; **ENT/audiology, ophthalmology, orthopedics** as indicated. **Experimental/translational lead:** KAT6B (MORF) inhibition partially rescues NIPBL-deficiency insulator defects in cells — a candidate for future preclinical development ([PMID: 40060486](https://pubmed.ncbi.nlm.nih.gov/40060486/)). Modulating cohesin dynamics (e.g., WAPL/PDS5 axis, [PMID: 36449618](https://pubmed.ncbi.nlm.nih.gov/36449618/), [PMID: 42030945](https://pubmed.ncbi.nlm.nih.gov/42030945/)) is a conceptual therapeutic direction.

### 13. Prevention
**Primary prevention:** not applicable for a *de novo* monogenic disorder. **Secondary:** prenatal ultrasound + molecular diagnosis for at-risk pregnancies; preimplantation/prenatal genetic testing where a familial or mosaic variant is known. **Tertiary:** prevent complications — echocardiographic surveillance (including for late valve dysplasia), GERD/aspiration prophylaxis, and multidisciplinary follow-up. **Genetic counseling:** low recurrence for *de novo* cases, but counsel for possible parental germline mosaicism.

### 14. Other Species / Natural Disease
**Model taxa:** *Mus musculus* (NCBITaxon:10090), *Danio rerio* (NCBITaxon:7955). **Orthologs:** mouse *Nipbl*, zebrafish *nipbl*. No well-characterized naturally occurring companion-animal CdLS is established in the reviewed literature; the disease is studied primarily through engineered/knockdown models. Cohesin and NIPBL are **deeply evolutionarily conserved**, underpinning cross-species modeling ([PMID: 27120001](https://pubmed.ncbi.nlm.nih.gov/27120001/)). No zoonotic dimension (non-infectious genetic disorder).

### 15. Model Organisms

| Model | Type | Construction | Recapitulation | Limitation |
|---|---|---|---|---|
| *Nipbl*+/− mouse | Mammalian | Heterozygous LoF (~30–75% transcript) | Gut, heart, craniofacial, CNS, limb defects; genome-wide cohesin/expression changes | Incomplete overlap with human severity; strain effects |
| Zebrafish *nipbl* morphant | Vertebrate | Morpholino knockdown | Heart + gut defects; endodermal & L-R patterning gene changes from gastrulation | Transient knockdown; morpholino caveats |
| Human iPSC-derived cardiomyocytes | In vitro/cellular | NIPBL-mutant patient/edited lines | Hundreds of dysregulated mRNAs/ncRNAs; disease-relevant tissue | 2D culture; lacks whole-organism context |

References: [PMID: 27120001](https://pubmed.ncbi.nlm.nih.gov/27120001/), [PMID: 22039349](https://pubmed.ncbi.nlm.nih.gov/22039349/), [PMID: 28855971](https://pubmed.ncbi.nlm.nih.gov/28855971/), [PMID: 29348408](https://pubmed.ncbi.nlm.nih.gov/29348408/). Resources: MGI (mouse), ZFIN (zebrafish).

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [38735830](https://pubmed.ncbi.nlm.nih.gov/38735830/) | *Cornelia de Lange Spectrum* | NIPBL >60%; cohesin gene list (F1) |
| [29995837](https://pubmed.ncbi.nlm.nih.gov/29995837/) | *First international consensus statement* | Cohesinopathy of 7 genes; diagnostic criteria (F1) |
| [16236812](https://pubmed.ncbi.nlm.nih.gov/16236812/) | *Genotype-phenotype, Dutch experience* | Truncating > missense severity (F1) |
| [42069659](https://pubmed.ncbi.nlm.nih.gov/42069659/) | *Start-loss NIPBL, mild CdLS* | Milder start-loss phenotype (F1) |
| [28855971](https://pubmed.ncbi.nlm.nih.gov/28855971/) | *Nipbl haploinsufficiency, cohesin binding* | Global cohesin loss; H3K4me3 promoters (F2) |
| [26581180](https://pubmed.ncbi.nlm.nih.gov/26581180/) | *Mutant cohesin, Pol II* | Impaired Pol II initiation/elongation (F2) |
| [29348408](https://pubmed.ncbi.nlm.nih.gov/29348408/) | *NIPBL iPSC-cardiomyocytes* | Hundreds of dysregulated transcripts (F2) |
| [34326454](https://pubmed.ncbi.nlm.nih.gov/34326454/) | *Mosaicism & purifying selection* | 13.1% mosaicism; blood negative selection (F3) |
| [32809170](https://pubmed.ncbi.nlm.nih.gov/32809170/) | *Repetitive & self-injurious behaviors* | 44% SIB; universal repetitive behavior (F4) |
| [30295920](https://pubmed.ncbi.nlm.nih.gov/30295920/) | *SMC1A development & behavior* | NIPBL more severe than SMC1A (F4) |
| [38462617](https://pubmed.ncbi.nlm.nih.gov/38462617/) | *Neurobehavioral genotype-phenotype* | Milestone delays; NIPBL severity (F4) |
| [40084492](https://pubmed.ncbi.nlm.nih.gov/40084492/) | *Severity score & communication* | Severity–communication link (F4) |
| [27120001](https://pubmed.ncbi.nlm.nih.gov/27120001/) | *Mouse & zebrafish models* | Vertebrate model validity (F5) |
| [22039349](https://pubmed.ncbi.nlm.nih.gov/22039349/) | *Zebrafish heart/gut defects* | Collective small perturbations (F5) |
| [19449412](https://pubmed.ncbi.nlm.nih.gov/19449412/) | *CHD in 87 CdLS patients* | 33% CHD; pulmonary stenosis (F6) |
| [36053618](https://pubmed.ncbi.nlm.nih.gov/36053618/) | *Gastrostomy & congenital anomalies* | ~1 in 4 gastrostomy (F7) |
| [32762940](https://pubmed.ncbi.nlm.nih.gov/32762940/) | *CdLS & CDH* | CDH mortality driver (F8) |
| [41699137](https://pubmed.ncbi.nlm.nih.gov/41699137/) | *Acute NIPBL depletion, loop extrusion* | Loop loss; cell-identity gene specificity (F9) |
| [41826481](https://pubmed.ncbi.nlm.nih.gov/41826481/) | *Impaired cohesin loading, pancreatic diff.* | E-P/CTCF loop collapse (F9) |
| [42030945](https://pubmed.ncbi.nlm.nih.gov/42030945/) | *PDS5 & cohesin-NIPBL lifetime* | CTCF boundary formation mechanism (F9) |
| [40060486](https://pubmed.ncbi.nlm.nih.gov/40060486/) | *Chromatin architecture, histone modifiers* | KAT6B inhibition rescue (F9) |
| [18074387](https://pubmed.ncbi.nlm.nih.gov/18074387/) | *Descriptive epidemiology (EUROCAT)* | Prevalence; sporadic; malformation freq. (F10) |
| [9608092](https://pubmed.ncbi.nlm.nih.gov/9608092/) | *Brachmann-de Lange, ECEMC* | 0.97/100,000; young parents (F10) |
| [41499064](https://pubmed.ncbi.nlm.nih.gov/41499064/) | *Dermatologist review* | 1:10,000–30,000 estimate (F10) |

**Supporting context papers:** [PMID: 37062615](https://pubmed.ncbi.nlm.nih.gov/37062615/) (NIPBL/cohesin biology), [PMID: 31516082](https://pubmed.ncbi.nlm.nih.gov/31516082/) (cohesinopathy non-cohesion functions, TGF-β), [PMID: 41102415](https://pubmed.ncbi.nlm.nih.gov/41102415/) (TACL live-cell loop extrusion), [PMID: 36449618](https://pubmed.ncbi.nlm.nih.gov/36449618/) (WAPL/cohesin balance), [PMID: 33478103](https://pubmed.ncbi.nlm.nih.gov/33478103/) (prenatal diagnosis), [PMID: 35935361](https://pubmed.ncbi.nlm.nih.gov/35935361/) (non-cohesion CdLS-like), [PMID: 31704779](https://pubmed.ncbi.nlm.nih.gov/31704779/) (molecular diagnosis to therapy), [PMID: 17508425](https://pubmed.ncbi.nlm.nih.gov/17508425/) (clinical review/anticipatory guidance).

---

## Limitations and Knowledge Gaps

1. **CHD frequency discrepancy.** Echocardiographic cohort data give 33% ([PMID: 19449412](https://pubmed.ncbi.nlm.nih.gov/19449412/)) versus 45.6% in registry data ([PMID: 18074387](https://pubmed.ncbi.nlm.nih.gov/18074387/)); differences likely reflect ascertainment (registries capture more severely malformed cases) and CHD definition. A NIPBL-genotype-stratified cardiac frequency is not resolved here.
2. **Small mortality-cohort numbers.** The CDH-mortality figures rest on 21 confirmed CdLS cases; while striking (76% mortality), the absolute numbers are small.
3. **Genotype–phenotype is probabilistic, not deterministic.** Truncating-vs-missense and NIPBL-vs-SMC1A severity trends have real exceptions; individual prediction remains limited.
4. **Life-expectancy and adult-outcome data are sparse.** Natural-history/longitudinal survival data beyond the neonatal period were not quantified in the reviewed literature.
5. **Therapeutic evidence is preclinical.** KAT6B inhibition is a cell-based rescue observation ([PMID: 40060486](https://pubmed.ncbi.nlm.nih.gov/40060486/)); no in vivo or human efficacy data exist. There are no disease-modifying therapies.
6. **QoL instruments.** Formal EQ-5D/SF-36/PROMIS data specific to CdLS1 were not identified; QoL impact is inferred from functional/behavioral outcomes.
7. **Modifier genes.** Beyond variant type and mosaicism, specific genetic modifiers of CdLS1 severity are not established.
8. **Non-type-1 boundary.** Some CdLS-like phenotypes arise from non-cohesin genes ([PMID: 35935361](https://pubmed.ncbi.nlm.nih.gov/35935361/)); the nosological boundary of "CdLS1" (strictly NIPBL) versus the broader spectrum should be kept explicit in the knowledge base.

---

## Proposed Follow-up Experiments / Actions

1. **Genotype-stratified organ-outcome study.** Pool registry + molecular cohorts to report CHD, CDH, and gastrostomy frequencies stratified by NIPBL truncating vs missense vs mosaic status — resolving the 33% vs 45.6% CHD discrepancy.
2. **Preclinical test of KAT6B inhibition in vivo.** Advance the KAT6B/MORF-inhibition rescue from cellular insulator-defect assays into *Nipbl*+/− mouse and zebrafish models, measuring transcriptomic normalization and developmental-phenotype rescue.
3. **Mosaicism-aware diagnostic pathway.** Formalize a reflex protocol: classical phenotype + negative blood NIPBL → buccal/fibroblast deep sequencing, given documented blood-selected mosaicism (13.1%).
4. **Natural-history / survival registry analysis.** Establish CdLS1-specific life-expectancy, cause-of-death distribution, and adult morbidity through longitudinal registry linkage.
5. **Single-cell / multi-omic developmental mapping.** Use single-cell transcriptomics + Hi-C on NIPBL-mutant iPSC-derived organoids (cardiac, limb, neural) to link specific loop-collapse events to cell-identity-gene deregulation and organ-specific malformation.
6. **Validated QoL assessment.** Deploy PROMIS/EQ-5D-style caregiver-report tools in CdLS1 cohorts, mapped per-phenotype (SIB, feeding, communication) for knowledge-base QoL annotation.
7. **Cohesin-dynamics modulation.** Explore WAPL/PDS5-axis modulation to counterbalance reduced cohesin residence time as a conceptual therapeutic strategy ([PMID: 36449618](https://pubmed.ncbi.nlm.nih.gov/36449618/), [PMID: 42030945](https://pubmed.ncbi.nlm.nih.gov/42030945/)).

---

*Report compiled from 5 investigation iterations, 10 confirmed findings, and 43 reviewed papers. All quantitative claims are cited to primary literature with verbatim abstract quotes where indicated.*


## Artifacts

- [OpenScientist final report](Cornelia_de_Lange_Syndrome_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Cornelia_de_Lange_Syndrome_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 33 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 19 |
| Quoted claims found in source | 19 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 33 |
| On topic | 21 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:36053618` (6 mentions) - Gastrostomy and congenital anomalies: a European population-based study.
  - shared terms: congenital

Weighed against this report's own most characteristic terms: `nipbl`, `cohesin`, `cdls`, `gene`, `defect`, `phenotype`, `patient`, `congenital`, `heart`, `genetic`, `model`, `variant`, `cdls1`, `severe`, `developmental`, `limb`, `severity`, `type`, `disease`, `cdh`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 44 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 27 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0032116` (1 mention) - the report calls it "sister chromatid cohesion — the *canonical* cohesin function, notably NOT the primary disease driver"; GO calls it **SMC loading complex**
- `HP:0000750` (2 mentions) - the report calls it "Delayed speech and language development", "Absent phrase speech by age 5"; HP calls it **Delayed speech and language development**
- `HP:0002194` (2 mentions) - the report calls it "Delayed gross motor development", "Not walking by age 5"; HP calls it **Delayed gross motor development**
- `HP:0009821` (2 mentions) - the report calls it "Forearm undergrowth", "Upper-limb reduction defects"; HP calls it **Forearm undergrowth**
- `HP:0012443` (2 mentions) - the report calls it "Abnormal brain morphology", "CNS malformation"; HP calls it **Abnormal brain morphology**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0035064` (obsolete methylated histone binding) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006357` (2 mentions) - the report calls it "regulation of transcription by RNA polymerase II", "regulation of transcription by RNA Pol II"; GO calls it **regulation of transcription by RNA polymerase II**
- `HP:0000733` (2 mentions) - the report calls it "Stereotypy", "Repetitive behavior"; HP calls it **Motor stereotypy**, and lists "Stereotyped" among its other names
- `HP:0011968` (2 mentions) - the report calls it "Feeding difficulties", "Feeding difficulty / gastrostomy"; HP calls it **Feeding difficulties**
- `GO:0035064` (1 mention) - the report calls it "methylated histone binding"; GO calls it **obsolete methylated histone binding**
- `HP:0001627` (1 mention) - the report calls it "Congenital heart defect"; HP calls it **Abnormal heart morphology**, and lists "Congenital heart defect" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0006357` - called "regulation of transcription by RNA polymerase II", "regulation of transcription by RNA Pol II"
- `HP:0000733` - called "Stereotypy", "Repetitive behavior"
- `HP:0000750` - called "Delayed speech and language development", "Absent phrase speech by age 5"
- `HP:0002194` - called "Delayed gross motor development", "Not walking by age 5"
- `HP:0011968` - called "Feeding difficulties", "Feeding difficulty / gastrostomy"
- `HP:0009821` - called "Forearm undergrowth", "Upper-limb reduction defects"
- `HP:0012443` - called "Abnormal brain morphology", "CNS malformation"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`.