---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T08:57:59.990932'
end_time: '2026-10-31T09:24:55.345119'
duration_seconds: 1615.35
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: X-Linked Intellectual Disability-Cerebellar Hypoplasia Syndrome
  mondo_id: MONDO:0010337
  category: Mendelian
  causal_genes: OPHN1
  omim_id: OMIM:300486
  synonyms: intellectual developmental disorder, X-linked syndromic, Billuart type,
    X-linked recessive; OPHN1 syndrome; Oligophrenin-1 syndrome
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
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 6
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:33638601
  relevance_assessed: 22
  on_topic: 19
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 55
  verified: 53
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 1
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0001249
    reported_labels:
    - cognitive/behavioral
    ontology_label: Intellectual disability
  - term_id: HP:0001270
    reported_labels:
    - sign
    ontology_label: Motor delay
  - term_id: HP:0000750
    reported_labels:
    - sign
    ontology_label: Delayed speech and language development
  - term_id: HP:0000639
    reported_labels:
    - sign
    ontology_label: Nystagmus
  - term_id: HP:0001251
    reported_labels:
    - sign
    ontology_label: Ataxia
  - term_id: HP:0000811
    reported_labels:
    - physical
    ontology_label: Abnormal external genitalia morphology
  - term_id: HP:0000271
    reported_labels:
    - physical
    ontology_label: Abnormality of the face
  - term_id: NCIT:C15193
    reported_labels:
    - speech/language therapy
    ontology_label: Bone Marrow Biopsy
  - term_id: NCIT:C15335
    reported_labels:
    - occupational therapy
    ontology_label: Technology Assessment
  - term_id: NCBITaxon:10090
    reported_labels:
    - Mus musculus
    - Taxonomy of experimental hosts:** *Mus musculus
    ontology_label: Mus musculus
  labels_variant: 6
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
  path: X-linked_Intellectual_Disability-cerebellar_Hypoplasia_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: X-linked_Intellectual_Disability-cerebellar_Hypoplasia_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** X-Linked Intellectual Disability-Cerebellar Hypoplasia Syndrome
- **MONDO ID:** MONDO:0010337 (if available)
- **Causal gene(s):** OPHN1
- **OMIM:** OMIM:300486
- **Synonyms:** intellectual developmental disorder, X-linked syndromic, Billuart type, X-linked recessive; OPHN1 syndrome; Oligophrenin-1 syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **X-Linked Intellectual Disability-Cerebellar Hypoplasia Syndrome** covering all of the
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

# X-Linked Intellectual Disability–Cerebellar Hypoplasia Syndrome (OPHN1 / Oligophrenin-1 Syndrome)

**Comprehensive Disease Characteristics Report**
**Target:** MONDO:0010337 · OMIM:300486 · **Causal gene: *OPHN1* (oligophrenin-1), Xq12**
Evidence sources are tagged as **[Human clinical]**, **[Mouse]**, **[in vitro/iPSC]**, or **[Computational/aggregated]**.

---

## Summary / Direct Answer

X-Linked Intellectual Disability–Cerebellar Hypoplasia Syndrome is a rare X-linked recessive neurodevelopmental disorder caused by **loss-of-function variants in *OPHN1*** (Xq12), which encodes **oligophrenin-1, a 91-kDa Rho-GTPase-activating protein (RhoGAP)** highly expressed in fetal brain (Billuart et al., 1998, *Nature*, PMID 9582072). Loss of oligophrenin-1's GAP activity removes negative control of RhoA, causing **constitutive RhoA/ROCK/MLC2 pathway hyperactivation** plus brain-region–specific **cAMP/PKA dysregulation**, which impairs dendritic spine maturation, AMPA-receptor recycling and synaptic-vesicle endocytosis. Clinically this produces intellectual disability with early hypotonia, motor/speech delay, behavioral problems, seizures, strabismus, and the hallmark neuroimaging triad of **cerebellar vermis hypoplasia, ventriculomegaly, and fronto-temporal atrophy** (Bergmann et al., 2003, PMID 12805098). The disorder is non-degenerative and compatible with long survival; no approved disease-modifying therapy exists, but **the ROCK/PKA inhibitor fasudil reverses behavioral and anatomical deficits in adult Ophn1 mice** (Meziane et al., 2016, PMID 27146843), establishing a mechanism-based therapeutic rationale.

---

## 1. Disease Information

**Overview.** A monogenic (Mendelian) syndromic form of X-linked intellectual disability (XLID). Core features: non-progressive intellectual disability (mild–severe), neonatal hypotonia, delayed motor/speech milestones, behavioral disturbance (hyperactivity, attention problems), epilepsy, ocular abnormalities (strabismus, nystagmus), and distinctive brain MRI showing cerebellar (vermis) hypoplasia with enlarged lateral ventricles. Originally described as a cause of *nonspecific* XLID, it was later recognized as a distinct, recognizable syndrome once brain imaging was systematically applied (Bergmann 2003, PMID 12805098; Zanni 2005, PMID 16221952). **[Human clinical]**

**Key identifiers.**
- **MONDO:** 0010337
- **OMIM:** 300486 (Intellectual developmental disorder, X-linked syndromic, Billuart type / "Mental retardation, X-linked, with cerebellar hypoplasia and distinctive facial appearance")
- **Gene OMIM:** *OPHN1* 300127 · **HGNC:** 8183 · **NCBI Gene:** 4983 · **Ensembl:** ENSG00000079482 · **UniProt:** O60890
- **Orphanet:** OPHN1 syndrome (ORPHA grouping under non-specific/syndromic XLID)
- **ICD-10:** Q04.3 (other reduction deformities of brain) + F70–F79 (intellectual disability) as applicable; **ICD-11:** LD90.Y / 6A00 (disorders of intellectual development) with imaging-based coding
- **MeSH:** "Mental Retardation, X-Linked"; "Intellectual Disability"; "Cerebellar Diseases"

**Synonyms / alternative names.** OPHN1 syndrome; Oligophrenin-1 syndrome; X-linked intellectual developmental disorder, Billuart type; MRX60 (historical non-syndromic designation); X-linked mental retardation with cerebellar hypoplasia and distinctive facial appearance.

**Information source.** Derived from aggregated disease-level resources (OMIM, Orphanet, HPO) and individual-patient case reports/small cohorts; there is no large EHR-based registry for this ultra-rare disorder.

**Phenotypic spectrum note.** Beyond classic syndromic/non-syndromic XLID, rare *OPHN1* variants have also been reported in **autism spectrum disorder** and **(childhood-onset) schizophrenia** cohorts (PMID 20479760, 30378261; "Variants of this gene have been also identified in autism spectrum disorder and schizophrenia," PMID 27146843), consistent with a shared synaptic-plasticity pathophysiology. **[Human clinical]**

---

## 2. Etiology

**Primary cause — genetic.** Hemizygous loss-of-function variants in *OPHN1* in males. "Here we report the characterization of a new gene on the long arm of the X-chromosome (position Xq12) and the identification in unrelated individuals of different mutations that are predicted to cause a loss of function" (Billuart 1998, PMID 9582072). **[Human clinical]**

**Genetic risk factors.**
- **Causal variants:** nonsense, frameshift (small indels), splice-site, whole/partial-gene and exonic deletions (e.g., exon 19 frameshift deletion, PMID 12805098; exon 21 deletion, PMID 32872024; exons 21–22 deletion, PMID 18261018; intragenic deletions, PMID 30534410), and rarer non-disruptive in-frame/missense variants affecting the BAR or C-terminal proline-rich domains (PMID 33638601, 24105372).
- **Dosage sensitivity:** a Xq12q13.1 **duplication** encompassing *OPHN1* also produced syndromic MR (PMID 18512229), indicating sensitivity to both loss and gain of copy number.
- **Sex:** male sex is the principal risk factor (X-linked recessive); heterozygous females are usually unaffected carriers.

**Environmental risk factors.** None established; this is a monogenic disorder. No toxin, infectious, dietary, or occupational exposure is implicated as causal.

**Protective factors.** In carrier females, **favorably skewed X-inactivation** (preferential silencing of the mutant X) is protective against manifestation; conversely, skewing toward the mutant allele can unmask disease in females (PMID 23416624). No protective pharmacologic/dietary factors are known. **[Human clinical]**

**Gene–environment interactions.** Not applicable/none documented.

---

## 3. Phenotypes

Onset is **congenital/neonatal** (hypotonia) with developmental features emerging in infancy–early childhood; the cognitive deficit is **stable (non-progressive)**, while epilepsy and behavior can **fluctuate**. Severity is **highly variable, even within families** (PMID 33638601, 29510240). Frequencies below are qualitative estimates aggregated from case series.

| Phenotype | Type | HPO term | Frequency | Notes |
|---|---|---|---|---|
| Intellectual disability (mild→severe) | cognitive/behavioral | HP:0001249 | ~100% | Defining feature; variable severity |
| Neonatal hypotonia | clinical sign | HP:0001319 / HP:0008935 | Common | Early presenting sign |
| Motor delay | sign | HP:0001270 | Very common | — |
| Speech/language delay | sign | HP:0000750 | Very common | — |
| Cerebellar vermis hypoplasia | imaging/physical | HP:0001320 / HP:0002335 | Common (not obligate) | Hallmark; absent in a subset (PMID 29510240) |
| Ventriculomegaly / enlarged lateral ventricles | imaging | HP:0002119 / HP:0006956 | Common | Often rostral/frontal predominant |
| Fronto-temporal atrophy | imaging | HP:0012156-related | Frequent | PMID 12805098, 24105372 |
| Seizures (incl. myoclonic-astatic) | sign | HP:0001250 / HP:0200134 | Frequent | PMID 12805098 |
| Strabismus | sign | HP:0000486 | Frequent | — |
| Nystagmus | sign | HP:0000639 | Occasional | PMID 32872024 |
| Ataxia / impaired coordination | sign | HP:0001251 | Frequent | Cerebellar origin |
| Behavioral problems (hyperactivity, frustration intolerance) | behavioral | HP:0000752 / HP:0000708 | Common | PMID 24105372 |
| Hypogenitalism / genital anomalies | physical | HP:0000811 | Subset | PMID 12805098 |
| Facial dysmorphism (prominent nasal root, deep-set eyes, long face) | physical | HP:0000271 | Common, subtle | PMID 24105372 |
| Strain on adaptive function (ADL dependence) | QoL | — | Severity-dependent | Lifelong support frequently required |

> Quote: "The distinctive phenotype comprised moderate to severe mental retardation, myoclonic-astatic epilepsy, ataxia, strabismus and hypogenitalism." (PMID 12805098) **[Human clinical]**

**Quality-of-life impact.** Lifelong intellectual disability affects education, independent living and employment; epilepsy and behavioral/attention problems add caregiver burden. No disease-specific EQ-5D/SF-36/PROMIS datasets exist; impact is inferred from the ID + epilepsy + behavior phenotype.

---

## 4. Genetic / Molecular Information

- **Causal gene:** *OPHN1* (HGNC:8183; NCBI Gene 4983; OMIM 300127), Xq12, ~26 exons, encoding oligophrenin-1 (UniProt O60890; 802 aa; ~91 kDa). Protein domains: N-terminal **BAR** domain, PH domain, central **RhoGAP** domain, C-terminal **proline-rich** region.
- **Variant classes (ACMG):** predominantly **pathogenic/likely-pathogenic loss-of-function** — nonsense, frameshift, canonical splice-site, and multi-exon/whole-gene **deletions**. Non-disruptive in-frame deletions/missense variants (BAR or proline-rich domains) are rarer and pose VUS interpretation challenges. "the identified genomic variants involve the region encoding the central RhoGAP domain … predicted to result in a complete loss of function" (PMID 33638601).
- **Functional consequence:** **loss of function** (loss of RhoGAP catalytic activity → failure to terminate RhoA signaling). Copy-number **gain** (duplication) is also pathogenic (PMID 18512229).
- **Origin:** **germline**; inherited from carrier mothers or *de novo*; **somatic mosaicism** reported (a missense variant in mosaic state, PMID 29510240). Not a somatic/cancer gene.
- **Allele frequency:** pathogenic variants are absent/ultra-rare in gnomAD; *OPHN1* shows constraint against LoF. **[Computational/aggregated]**
- **Modifier genes:** none firmly established. The main modifier of female expression is the **X-inactivation ratio** (epigenetic), not a trans-acting gene (PMID 23416624).
- **Epigenetic/post-transcriptional:** *OPHN1* mRNA undergoes **A-to-I RNA editing (ADAR2)** and **alternative splicing** during human brain development, peaking at gestational weeks 20–33 — relevant to normal regulation and potentially to phenotype modulation (Barresi 2014, PMID 24637888). **[Human/in vitro]**
- **Chromosomal abnormalities:** intragenic and contiguous Xq12–q13.1 deletions and one duplication; detectable by array-CGH/MLPA (PMID 18261018, 18512229, 30534410, 32872024).

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributors are implicated — the disease is purely monogenic. Environmental factors, diet, smoking/alcohol, toxins, radiation, and pathogens are **not applicable** as causes. (Standard prenatal/perinatal neuroprotective care applies generically but is not disease-specific.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Loss-of-function variant in *OPHN1*** (nonsense/frameshift/splice/deletion) **results in** absent or non-functional oligophrenin-1 protein (loss of RhoGAP activity). [Demonstrated — PMID 9582072]
2. Loss of RhoGAP activity **leads to** failure to accelerate GTP hydrolysis on RhoA → **constitutive RhoA activation**. [Demonstrated/inferred from GAP biochemistry — PMID 9582072]
3. Constitutive RhoA **leads to** **ROCK (Rho-kinase) hyperactivation**, confirmed in OPHN1-deficient human iPSC neurons where ROCK remains elevated throughout differentiation. [Demonstrated — PMID 27160703]
4. ROCK hyperactivation **results in** increased phosphorylation of myosin phosphatase target subunit (MYPT1) and MLC2 → **excess actomyosin contractility and dysregulated actin cytoskeleton**. [Demonstrated — PMID 27160703, 35563851]
5. **Branch A (postsynaptic):** cytoskeletal dysregulation + loss of OPHN1–Homer1b/c and OPHN1–endophilin A1 interactions **lead to** mispositioned spine endocytic zone, **impaired AMPA-receptor recycling**, and **failure of dendritic spine maturation** (excess immature filopodia). [Demonstrated — PMID 24966368, 19481455, 17728457]
   - *Sub-branch (activity-dependent plasticity):* group-I mGluR activation normally triggers **rapid dendritic OPHN1 translation** (mGluR1-dependent, **FMRP-independent**) required for **mGluR-LTD** and the associated persistent reduction of surface AMPARs via endophilin A2/3; loss of OPHN1 **results in** impaired protein-synthesis-dependent LTD — a role separable from its basal-synaptic Rho-GAP/Homer1b/c function. [Demonstrated — PMID 22017989]
6. **Branch B (presynaptic):** OPHN1 loss **leads to** brain-region-specific **cAMP/PKA pathway dysregulation** and defective synaptic-vesicle endocytosis, abolishing **PKA-dependent presynaptic plasticity** in hippocampus and amygdala. [Demonstrated — PMID 24298161, 19481455]
7. Combined pre/postsynaptic dysfunction **results in** **altered short-term plasticity** (reduced paired-pulse facilitation) and impaired synapse maturation without neuronal loss. [Demonstrated, mouse — PMID 17728457]
8. During development, failure of Rho-GTPase–dependent control of neurite/dendrite outgrowth and migration **contributes to** **cerebellar (vermis) hypoplasia** and **ventricular enlargement**; neuropathology shows **Purkinje-cell heterotopia** in cerebellar white matter. [Demonstrated, human fetus — PMID 23416624]
9. These circuit- and structural-level defects **manifest clinically as** intellectual disability, hypotonia, ataxia, epilepsy, strabismus, and behavioral disturbance. [Human clinical — PMID 12805098, 16221952]

### Detail by category

- **Molecular pathways:** RhoA → ROCK → MYPT1/MLC2 actomyosin pathway (KEGG hsa04810 regulation of actin cytoskeleton; Rho GTPase cycle, Reactome R-HSA-194840); cAMP/PKA signaling (presynaptic). GO: **GO:0007265** Ras/Rho signal transduction; **GO:0043087** regulation of GTPase activity; **GO:0051056** regulation of small GTPase signal transduction.
- **Cellular processes:** dendritic spine morphogenesis (**GO:0060997**), regulation of synaptic plasticity (**GO:0048167**), **long-term synaptic depression (GO:0060292)** / mGluR-dependent LTD, **protein-synthesis-dependent plasticity** (rapid dendritic OPHN1 translation; PMID 22017989), synaptic vesicle endocytosis (**GO:0048488**), receptor recycling (**GO:0001881**), actin cytoskeleton organization (**GO:0030036**), neuron projection development (**GO:0031175**). No apoptosis/neurodegeneration — this is a **developmental/connectivity** disorder, not a neurodegenerative one.
- **Protein dysfunction:** loss of RhoGAP catalytic function (not misfolding/aggregation); some in-frame variants retain stable but hypofunctional protein affecting BAR-domain membrane curvature/hippocampal roles (PMID 24105372).
- **Metabolic / immune / infectious involvement:** none implicated.
- **Molecular profiling:** iPSC-neuron studies show elevated ROCK activity and reduced NR4A1 (neurite-outgrowth nuclear receptor), normalized by fasudil (PMID 27160703); developmental RNA editing/splicing of *OPHN1* (PMID 24637888). No disease-specific large-scale transcriptomic/proteomic/metabolomic datasets published.
- **Functional genomics:** modeled by *Ophn1* knockout/conditional mice and OPHN1-knockdown/knockout iPSC neurons (below).

**Upstream vs downstream:** *OPHN1* LoF → RhoA/ROCK hyperactivation are **upstream**; spine/vesicle/plasticity defects and cerebellar hypoplasia are **downstream**. Cell types (CL): neurons (**CL:0000540**), pyramidal/hippocampal neurons (**CL:0000598**), cerebellar Purkinje cells (**CL:0000121**), glutamatergic neurons (**CL:0000679**).

---

## 7. Anatomical Structures Affected

- **Organ/system:** central nervous system (nervous system, **UBERON:0001016**); principally brain (**UBERON:0000955**).
- **Primary sites:** **cerebellum** (UBERON:0002037), especially **cerebellar vermis** (UBERON:0004086) — hypoplasia/lower-vermian agenesis; **cerebral lateral ventricles** (UBERON:0002285) — enlargement; **frontal and temporal lobes** (UBERON:0016525 / UBERON:0001871) — atrophy; **hippocampus** (UBERON:0002421) — alterations with certain BAR-domain variants (PMID 24105372); **cisterna magna** — cystic dilatation.
- **Secondary involvement:** visual axis (strabismus/nystagmus); genitourinary (hypogenitalism in a subset).
- **Tissue/cell level:** neural tissue; affected cell populations include **cortical/hippocampal pyramidal neurons** and **cerebellar Purkinje cells** (heterotopic in white matter, PMID 23416624).
- **Subcellular compartments (GO CC):** **dendritic spine (GO:0043197)**, **postsynaptic density (GO:0014069)**, **presynaptic active zone / synaptic vesicle (GO:0008021)**, **endocytic zone / clathrin-coated pit**, **actin cytoskeleton (GO:0015629)**.
- **Lateralization:** brain involvement is generally **bilateral**, though **asymmetric cerebellar hypoplasia** has been described (PMID 12805098).

---

## 8. Temporal Development

- **Onset:** congenital/neonatal (hypotonia at birth; some structural anomalies detectable prenatally on fetal MRI/ultrasound, PMID 23416624). Pattern: **chronic, insidious** developmental presentation.
- **Progression:** the intellectual disability is **static/non-progressive** (a neurodevelopmental, not neurodegenerative, condition). Epilepsy may evolve and behavioral issues fluctuate; cerebellar/ventricular findings are stable structural features. Disease duration: **chronic, lifelong**.
- **Remission:** no spontaneous remission of ID; seizures/behavior may improve with treatment.
- **Critical period:** synaptic and cerebellar development (fetal–early postnatal) is the window of structural vulnerability. Importantly, mouse data show **functional deficits remain pharmacologically reversible in adulthood** (PMID 27146843), implying a therapeutic window beyond early development. **[Mouse]**

---

## 9. Inheritance and Population

- **Inheritance:** **X-linked recessive** (OMIM 300486). Affected individuals are predominantly **hemizygous males**; **carrier females** are usually unaffected but can manifest with **skewed X-inactivation** (PMID 23416624).
- **Penetrance:** essentially **complete in hemizygous males**; **expressivity is highly variable**, even among siblings sharing the same variant (PMID 33638601, 29510240).
- **Germline mosaicism / de novo:** both inherited and *de novo* variants occur; **somatic mosaicism** has been documented (PMID 29510240).
- **Anticipation:** not applicable (not a repeat-expansion disorder).
- **Founder effects / consanguinity:** no founder mutation; consanguinity not a driver (X-linked). Recurrent large deletions arise independently.
- **Carrier/allele frequency:** pathogenic alleles ultra-rare; absent from population controls (gnomAD).
- **Epidemiology:** **ultra-rare**; precise prevalence/incidence undefined (Orphanet: prevalence unknown). Background context: nonspecific XLMR affects ~0.15–0.3% of males, of which *OPHN1* accounts for ~1%, rising to ~12% among males with ID **plus** cerebellar anomalies (PMID 9582072, 16221952). Only on the order of dozens of families reported worldwide.
- **Sex ratio:** strongly **male-predominant**; rare symptomatic females with skewed XCI or structural variants.
- **Geographic distribution:** worldwide, no endemic clustering; reported across European, Brazilian, Japanese and other populations (PMID 24105372, 30534410).

---

## 10. Diagnostics

- **Recommended approach:** clinical suspicion (male with ID + hypotonia + cerebellar/ventricular MRI findings ± epilepsy/strabismus) → **brain MRI** → **molecular genetic testing**.
- **Imaging (key diagnostic):** **brain MRI** demonstrating cerebellar vermis hypoplasia, enlarged (often rostral) lateral ventricles, fronto-temporal atrophy, and cisterna magna dilatation (PMID 12805098, 24105372). Fetal MRI/ultrasound may detect ventriculomegaly and vermian hypoplasia prenatally (PMID 23416624). (RadLex imaging features; no disease-specific biomarker on labs.)
- **Genetic testing:**
  - **Exome/genome sequencing (WES/WGS)** and **XLID / epilepsy–ID multigene panels** including *OPHN1* are first-line for undiagnosed ID; "We emphasize the power of next generation techniques (X-exome sequencing, whole-exome sequencing and targeted multi-gene panel) to expand the phenotypic and mutational spectrum of OPHN1-related ID" (PMID 29510240).
  - **Single-gene sequencing** of *OPHN1* where phenotype is classic.
  - **Chromosomal microarray (CMA)/array-CGH** and **MLPA** to detect intragenic/whole-gene **deletions and duplications**, which are a common mutation class (PMID 18261018, 18512229, 30534410, 32872024). "we suggest that MLPA analysis should be performed as an alternative diagnostic test" (PMID 32872024).
- **Laboratory tests/biomarkers:** no specific blood/urine biochemical marker; routine labs normal. Karyotype usually normal. mtDNA/repeat-expansion testing **not applicable**.
- **Electrophysiology:** EEG for seizure characterization (e.g., myoclonic-astatic epilepsy).
- **Histopathology (research/autopsy):** cerebellar Purkinje-cell heterotopia (PMID 23416624).
- **Clinical criteria / differential diagnosis:** no formal diagnostic criteria; diagnosis is molecular. Differentials include other XLID-with-cerebellar-hypoplasia genes (e.g., **CASK**, **OPHN1 vs. ATRX**, **ARX**), Dandy-Walker/pontocerebellar hypoplasias, and syndromic ID with posterior-fossa anomalies; distinguish by gene, facial gestalt, and MRI pattern (PMID 16506132, 30534410).
- **Screening:** no population newborn screening (not actionable/biochemical). **Cascade carrier testing** of at-risk female relatives once the familial variant is known; prenatal/preimplantation testing available for known variants.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** **not life-limiting per se**; the condition is compatible with normal or near-normal lifespan. No disease-specific mortality rate established; risks relate to complications of severe epilepsy or profound disability (generic).
- **Morbidity/disability:** **lifelong intellectual disability** is the dominant morbidity, with variable needs for educational, communication, mobility and behavioral support; epilepsy and strabismus add morbidity. ICF-level impairments in cognition, communication, and adaptive functioning.
- **Disease course:** static cognitive deficit; seizures and behavior may be modifiable with treatment. Recovery of baseline cognition is not expected; early intervention improves functional outcomes (generic rehabilitation evidence).
- **Prognostic factors:** severity correlates loosely with overall phenotype but there is **no robust genotype–phenotype correlation**, limiting individual prognostication (PMID 33638601). Presence/severity of epilepsy and degree of ID are the main functional predictors.
- **Prognostic biomarkers:** none validated.

---

## 12. Treatment

**No approved disease-modifying therapy exists; management is symptomatic and supportive.**

- **Supportive/rehabilitative (standard of care):** special education, **speech/language therapy** (NCIT:C15193), **physical therapy** (NCIT:C15327) and **occupational therapy** (NCIT:C15335) for hypotonia/motor delay, behavioral/psychological support. Ophthalmologic management of strabismus (corrective lenses/surgery).
- **Pharmacotherapy (symptomatic):** **antiseizure medications** for epilepsy (agent chosen by seizure type, e.g., valproate/levetiracetam; NCIT:C264 anticonvulsant class); stimulants/behavioral agents for ADHD-type symptoms as clinically indicated. Pharmacogenomics: no disorder-specific PGx guidance; standard ASM PGx (e.g., HLA-B for carbamazepine) applies generically.
- **Mechanism-based experimental therapy — ROCK/PKA inhibition (fasudil):** the leading translational candidate. "chronic treatment in adult mouse with Fasudil, is able to counteract vertical and horizontal hyperactivities, restores recognition memory and limits the brain ventricular dilatation observed in Ophn1" (PMID 27146843); fasudil "fully rescued" hippocampus/amygdala learning deficits (PMID 24298161) and corrected OPHN1-deficient iPSC neurons (PMID 27160703). CHEBI: fasudil (CHEBI:75172); target NCIT: Rho-associated kinase inhibitor. **Human trials specific to OPHN1 are not yet reported.** **[Mouse / in vitro]**
- **Gene/cell/RNA-based therapy:** none in clinical development; conceptually plausible given defined LoF mechanism, but no vectors/ASOs reported for *OPHN1*.
- **Surgical/interventional:** none disease-specific (standard epilepsy or strabismus surgery as indicated).
- **Treatment strategy:** multidisciplinary (neurology, genetics, developmental pediatrics, ophthalmology, rehabilitation); personalized to seizure type and developmental needs. Combination (pathway inhibitor + symptomatic care) is the envisaged future model.

---

## 13. Prevention

- **Primary prevention:** not possible (genetic); risk reduction centers on **reproductive counseling**.
- **Genetic counseling:** carrier mothers have **50% transmission risk** to each son (affected) and 50% of daughters are carriers (X-linked recessive). **Cascade testing** of maternal relatives once the variant is identified.
- **Secondary prevention (reproductive options for known-variant families):** **prenatal diagnosis** (CVS/amniocentesis) and **preimplantation genetic testing (PGT-M)**; prenatal imaging may detect ventriculomegaly/vermian hypoplasia.
- **Tertiary prevention:** seizure control, early developmental intervention, behavioral and physical therapies to limit secondary complications and maximize function.
- **Immunization / public-health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

- **Orthologous gene:** mouse ***Ophn1*** (NCBI Gene 94190; MGI); rat *Ophn1* (NCBI Gene 309989). Protein is highly conserved; RhoGAP function conserved across vertebrates.
- **Taxonomy of experimental hosts:** *Mus musculus* (NCBITaxon:10090); *Homo sapiens* (NCBITaxon:9606) iPSC-derived neurons.
- **Natural disease in other species:** **no naturally occurring OPHN1 disease reported** in companion animals or wildlife (OMIA: none established); veterinary relevance is limited to engineered models.
- **Comparative biology:** mouse *Ophn1* KO recapitulates ventricular enlargement, spatial-memory and social deficits, hyperactivity, and dendritic-spine immaturity, confirming evolutionary conservation of the RhoGAP–synapse mechanism (PMID 17728457).
- **Transmission/zoonosis:** not applicable (genetic disorder).

---

## 15. Model Organisms

- **Mouse (primary mammalian model):** constitutive and **conditional *Ophn1* knockouts** (Mus musculus). Phenotype recapitulation: enlarged lateral ventricles, impaired spatial memory, impaired social behavior, hyperactivity, reduced paired-pulse facilitation, and reduced mature dendritic spines — "we generated a mouse model of ophn1 deficiency and showed that it mimics the ventricles enlargement without affecting the cerebellum morphoanatomy" (PMID 17728457). **Model limitation:** the mouse does **not** reproduce the human **cerebellar hypoplasia**, an important divergence. Models also revealed presynaptic cAMP/PKA deficits (PMID 24298161) and enabled **fasudil rescue** proof-of-concept (PMID 27146843). **[Mouse]**
- **Human iPSC-derived neurons (in vitro cellular model):** OPHN1 loss-of-function iPSC neurons show sustained ROCK hyperactivity, impaired neuronal differentiation/morphology, and rescue by fasudil/ROCK inhibition (PMID 27160703). Useful for human-specific neurodevelopmental mechanisms and drug testing. **[in vitro]**
- **Primary neuronal cultures / rat hippocampus:** used to dissect OPHN1–Homer1b/c (AMPAR recycling; PMID 24966368) and OPHN1–endophilin A1 (SV endocytosis; PMID 19481455) functions, and postnatal developmental changes in synaptic transmission/plasticity (PMID 35563851).
- **Model types available:** knockout, conditional/floxed (region- and stage-specific), knockdown; patient-derived iPSC lines. **Resources:** MGI (mouse), IMPC/IMSR, Cellosaurus (iPSC lines).
- **Research applications:** synaptic plasticity mechanisms, dendritic spine biology, Rho-GTPase signaling in cognition, and preclinical ROCK-inhibitor pharmacology.

---

## Supported vs. Refuted Hypotheses

**Supported:**
- *OPHN1* LoF causes the disorder via **RhoA/ROCK hyperactivation** (PMID 9582072, 27160703). ✔
- Disease reflects **synaptic dysfunction (pre- and postsynaptic)** rather than neurodegeneration (PMID 17728457, 24298161, 19481455, 24966368). ✔
- **Cerebellar hypoplasia is variable/non-obligate**; phenotype spans non-syndromic to syndromic (PMID 29510240, 33638601). ✔
- **ROCK/PKA inhibition (fasudil) reverses deficits in adulthood** in models (PMID 27146843, 24298161, 27160703). ✔

**Refuted / not supported:**
- That OPHN1 causes *purely* non-syndromic MR — refuted once imaging revealed consistent cerebellar/ventricular signatures (PMID 12805098, 16221952, 24105372).
- A tight genotype–phenotype correlation — not supported; expressivity varies even within families (PMID 33638601).
- An environmental/infectious contribution — none found; disorder is monogenic.

## Limitations and Future Directions

- **Ultra-rare** disorder: epidemiologic parameters (precise prevalence, incidence, natural-history cohorts, QoL metrics) are undefined.
- **No human therapeutic trials**; fasudil evidence is preclinical (mouse/iPSC) — translation and a human treatment window remain to be established.
- **Model gap:** mouse lacks cerebellar hypoplasia, limiting study of that key human feature; new models (e.g., cerebellar organoids) are needed.
- **Variant interpretation** of non-disruptive (BAR/proline-rich, missense) variants is challenging and would benefit from standardized functional assays.
- Roles of **RNA editing/alternative splicing** and **X-inactivation** as modifiers warrant further study.

---

### Key References (PMID)
9582072 (Billuart 1998, *Nature*, gene discovery) · 12805098 (Bergmann 2003, recognizable syndrome) · 16221952 (Zanni 2005, cohort/frequency) · 17728457 (Khelfaoui 2007, KO mouse) · 19481455 (Nakano-Kobayashi 2009, endophilin A1) · 22017989 (Nadif Kasri 2011, mGluR-LTD / rapid OPHN1 synthesis) · 24966368 (Nakano-Kobayashi 2014, Homer1b/c) · 20479760 (Piton 2011, ASD/SCZ X-linked synaptic genes) · 30378261 (Ambalavanan 2019, childhood-onset schizophrenia) · 24298161 (Khelfaoui 2014, cAMP/PKA, fasudil) · 27146843 (Meziane 2016, fasudil adult rescue) · 27160703 (Compagnucci 2016, iPSC/ROCK) · 24637888 (Barresi 2014, RNA editing/splicing) · 24105372 (Santos-Rebouças 2014, BAR domain/hippocampus) · 23416624 (Rocas 2013, female fetus/XCI/Purkinje heterotopia) · 29510240 (Moortgat 2018, no cerebellar anomaly subset) · 33638601 (Nuovo 2021, allelic spectrum) · 32872024 (Bogliş 2020, MLPA/deletion) · 18512229 (Bedeschi 2008, duplication) · 18261018 (Madrigal 2008, deletion/aCGH) · 30534410 (Iida 2019, Dandy-Walker/deletion) · 35563851 (Cresto 2022, postnatal synaptic development) · 16506132 (Guillén-Navarro 2006, XLMR review).


## Artifacts

- [OpenScientist final report](X-linked_Intellectual_Disability-cerebellar_Hypoplasia_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](X-linked_Intellectual_Disability-cerebellar_Hypoplasia_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 6 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 22 |
| On topic | 19 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:33638601` *(abstract only)*: "the identified genomic variants involve the region encoding the central RhoGAP domain … predicted to result in a complete loss of function"
  - closest text in source: "In most of cases so far reported, the identified genomic variants involve the region encoding the central RhoGAP domain of the oligophrenin-1 protein, and are predicted to result in a complete loss of function"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 55 |
| Resolved | 53 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 17 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001249` (1 mention) - the report calls it "cognitive/behavioral"; HP calls it **Intellectual disability**
- `HP:0001270` (1 mention) - the report calls it "sign"; HP calls it **Motor delay**
- `HP:0000750` (1 mention) - the report calls it "sign"; HP calls it **Delayed speech and language development**
- `HP:0000639` (1 mention) - the report calls it "sign"; HP calls it **Nystagmus**
- `HP:0001251` (1 mention) - the report calls it "sign"; HP calls it **Ataxia**
- `HP:0000811` (1 mention) - the report calls it "physical"; HP calls it **Abnormal external genitalia morphology**
- `HP:0000271` (1 mention) - the report calls it "physical"; HP calls it **Abnormality of the face**
- `NCIT:C15193` (1 mention) - the report calls it "speech/language therapy"; NCIT calls it **Bone Marrow Biopsy**
- `NCIT:C15335` (1 mention) - the report calls it "occupational therapy"; NCIT calls it **Technology Assessment**
- `NCBITaxon:10090` (1 mention) - the report calls it "Mus musculus", "Taxonomy of experimental hosts:** *Mus musculus"; NCBITaxon calls it **Mus musculus**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000486` (1 mention) - the report calls it "sign"; HP calls it **Strabismus**, and lists "Squint" among its other names
- `UBERON:0002037` (1 mention) - the report calls it "cerebellum", "Primary sites:** **cerebellum"; UBERON calls it **cerebellum**
- `UBERON:0004086` (1 mention) - the report calls it "cerebellar vermis"; UBERON calls it **brain ventricle**, and lists "cerebral ventricle" among its other names
- `UBERON:0002285` (1 mention) - the report calls it "cerebral lateral ventricles"; UBERON calls it **telencephalic ventricle**, and lists "lateral ventricles" among its other names
- `UBERON:0002421` (1 mention) - the report calls it "hippocampus"; UBERON calls it **hippocampal formation**, and lists "hippocampus" among its other names
- `NCIT:C15327` (1 mention) - the report calls it "physical therapy"; NCIT calls it **Lumbar Puncture**, and lists "Spinal Tap" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002037` - called "cerebellum", "Primary sites:** **cerebellum"
- `NCBITaxon:10090` - called "Mus musculus", "Taxonomy of experimental hosts:** *Mus musculus"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.