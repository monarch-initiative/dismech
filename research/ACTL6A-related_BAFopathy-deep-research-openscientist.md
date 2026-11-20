---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-07T02:28:35.022792'
end_time: '2026-11-07T02:48:27.246634'
duration_seconds: 1192.22
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: ACTL6A-related BAFopathy
  mondo_id: MONDO:0700121
  category: Mendelian
  causal_genes: ACTL6A
  omim_id: not recorded
  synonyms: ACTL6A-related neurodevelopmental disorder; BAF53A-related disorder
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
citation_count: 21
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 22
  on_topic: 14
  validator_version: 0.5.1
term_validation:
  total_terms: 33
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 1
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0001249
    reported_labels:
    - Cognitive sign
    ontology_label: Intellectual disability
  - term_id: HP:0002463
    reported_labels:
    - Behavioral/cognitive
    ontology_label: Language impairment
  - term_id: HP:0011968
    reported_labels:
    - Sign
    ontology_label: Feeding difficulties
  - term_id: HP:0002719
    reported_labels:
    - Sign
    ontology_label: Recurrent infections
  - term_id: HP:0001252
    reported_labels:
    - Sign
    ontology_label: Hypotonia
  - term_id: NCIT:C15402
    reported_labels:
    - physical therapy
    ontology_label: Conization
  - term_id: NCIT:C15214
    reported_labels:
    - occupational therapy
    ontology_label: Craniotomy
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ACTL6A-related_BAFopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ACTL6A-related_BAFopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ACTL6A-related BAFopathy
- **MONDO ID:** MONDO:0700121 (if available)
- **Causal gene(s):** ACTL6A
- **OMIM:** not recorded
- **Synonyms:** ACTL6A-related neurodevelopmental disorder; BAF53A-related disorder
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **ACTL6A-related BAFopathy** covering all of the
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

# ACTL6A-related BAFopathy (MONDO:0700121): Comprehensive Disease Characteristics Report

**Causal gene: _ACTL6A_ (encoding BAF53a / Actin-like protein 6A; HGNC:24124; NCBI Gene 86; UniProt O96019; chromosome 3q26.33).** This report concerns the rare Mendelian neurodevelopmental disorder caused by germline heterozygous variants in **ACTL6A** — not the somatic 3q26 _ACTL6A_ amplification seen in squamous cell carcinoma, and not the paralogous _ACTL6B_ (BAF53b) disorder. Throughout, "BAF53a" and "ACTL6A" refer to the same product.

---

## Summary

**ACTL6A-related BAFopathy** is a rare, autosomal-dominant neurodevelopmental disorder caused by germline (usually de novo) heterozygous variants in **ACTL6A**, which encodes **BAF53a**, a dosage-sensitive actin-related subunit shared by the BAF/mSWI/SNF, NuA4/TIP60 histone-acetyltransferase, and INO80 chromatin-remodeling complexes. The disorder sits within the **Coffin-Siris syndrome (CSS) / BAFopathy / SWI/SNF-related intellectual disability disorders (SSRIDD)** spectrum, presenting with intellectual disability/developmental delay (with prominent speech and language involvement), facial dysmorphism, and variable acral/fifth-digit (nail and distal phalanx) anomalies. It was first established as a disease gene by Marom et al. (2017), with a recurrent, recognizable p.Arg377Trp phenotype reported by Pascolini et al. (2020) and independent cohort support from Chen et al. (2022).

Mechanistically, BAF53a is the **neural-progenitor** actin-related BAF subunit. Its programmed replacement by BAF53b (ACTL6B) at mitotic exit — driven by miR-9*/miR-124 — gates the switch from proliferating neural progenitors to post-mitotic neurons. Pathogenic ACTL6A variants perturb this dosage-sensitive system: loss or impairment of BAF53a stalls the progenitor cell cycle, allows Polycomb accumulation, and reduces chromatin accessibility at pioneer-factor sites (SOX2, ASCL1), blocking normal neurogenesis. Population-genetic constraint data (gnomAD pLI = 0.997, LOEUF = 0.25) independently corroborate strong intolerance to loss-of-function, consistent with haploinsufficiency/dosage sensitivity.

The disorder is ultra-rare and recently delineated: MONDO:0700121 has **no OMIM or Orphanet cross-references**, and curated phenotype/gene-disease association counts remain near zero in aggregated resources. Diagnosis rests on trio exome/genome sequencing; a validated BAFopathy DNA-methylation episignature exists for several BAF subunits but **does not yet include ACTL6A**. There is no disease-specific therapy — management is supportive (early intervention, speech/physical/occupational therapy, surveillance for BAFopathy-associated complications). Much of the clinical granularity typical of established disorders (precise frequencies, natural history, prognosis) is not yet available because fewer than ~10 patients have been reported.

---

## 1. Disease Information

**Overview.** ACTL6A-related BAFopathy is an autosomal-dominant neurodevelopmental/intellectual-disability disorder caused by heterozygous variants in _ACTL6A_, a gene encoding a core actin-related subunit (BAF53a) of the ATP-dependent BAF (mSWI/SNF) chromatin-remodeling complex. It belongs to the broader BAFopathy / Coffin-Siris syndrome spectrum. First described in three subjects by Marom et al. 2017 ([PMID: 28649782](https://pubmed.ncbi.nlm.nih.gov/28649782/)): *"We identified heterozygous, novel variants in ACTL6A, a gene encoding a component of the BAF complex, in three subjects with varying degrees of intellectual disability."*

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | **MONDO:0700121** — "ACTL6A-related BAFopathy" (*"Any BAFopathy in which the cause of the disease is a mutation in the ACTL6A gene"*) |
| OMIM | Not recorded (no MONDO→OMIM xref) |
| Orphanet | Not recorded (no MONDO→Orphanet xref) |
| ICD-10/ICD-11 | No specific code; coded under broad neurodevelopmental/intellectual-disability categories |
| MeSH | No dedicated descriptor |
| Gene (HGNC) | HGNC:24124 (_ACTL6A_) |
| Gene (NCBI) | 86 |
| Protein (UniProt) | O96019 (BAF53a / Actin-like protein 6A) |

Per Monarch Initiative (2026), the MONDO node has **no external mappings** to OMIM/Orphanet and holds 0 curated disease→phenotype and 0 causal gene→disease associations — a signature of the disorder's rarity and recency (Finding F010).

**Synonyms / alternative names.** ACTL6A-related neurodevelopmental disorder; BAF53A-related disorder; ACTL6A-related intellectual disability; (classified within) BAF-opathies / SSRIDDs (SWI/SNF-related intellectual disability disorders).

**Information source.** Derived from **aggregated disease-level resources** (MONDO, UniProt, gnomAD, ClinVar) plus **individual patient reports** (case reports and small exome cohorts) — not from a large EHR-derived or registry dataset.

---

## 2. Etiology

**Primary cause — genetic.** Germline heterozygous variants in _ACTL6A_, typically **de novo**. Three independent lines of evidence establish causation:
- Marom et al. 2017 ([PMID: 28649782](https://pubmed.ncbi.nlm.nih.gov/28649782/)): three subjects with heterozygous novel variants — two missense in conserved actin-like-domain residues, one splice variant creating an in-frame deletion.
- Pascolini et al. 2020 ([PMID: 31994175](https://pubmed.ncbi.nlm.nih.gov/31994175/)): recurrent de novo **p.Arg377Trp** producing *"a phenotype reminiscent a disorder of the BRG1-associated factor (BAF) complex, including dysmorphic facies and acral malformations."*
- Chen et al. 2022 ([PMID: 34906496](https://pubmed.ncbi.nlm.nih.gov/34906496/)): *"de novo or predicted loss-of-function variants in 4 candidate BAFopathy genes, including ACTL6A"* in a 16,243-patient exome cohort.

**Genetic risk factors.** The causal variant itself is the risk factor; no separate susceptibility loci or modifier genes are established. _ACTL6A_ is highly constrained (gnomAD pLI = 0.997, LOEUF = 0.25; Finding F008), indicating that loss-of-function is rarely tolerated in the general population.

**Environmental risk factors.** None identified. As a Mendelian single-gene disorder, there are no established environmental, lifestyle, occupational, or infectious contributors. Advanced paternal age is a theoretical contributor to de novo mutation rate generally but is not specifically documented for ACTL6A.

**Protective factors.** None identified (no protective alleles or environmental factors described).

**Gene–environment interactions.** None documented for this disorder.

---

## 3. Phenotypes

Because fewer than ~10 patients are reported, phenotype frequencies are **qualitative/approximate**, extrapolated partly from the broader BAFopathy/CSS spectrum. Core features reported specifically in ACTL6A patients: intellectual disability, learning disability, developmental language disorder (Marom 2017); dysmorphic facies and acral malformations (Pascolini 2020).

| Phenotype | Type | Suggested HPO | Onset | Severity/Notes | Frequency (ACTL6A, qualitative) |
|---|---|---|---|---|---|
| Intellectual disability | Cognitive sign | HP:0001249 | Childhood (evident early) | Variable (mild→severe) | Core / most |
| Developmental delay | Cognitive/motor sign | HP:0001263 | Infancy | Variable | Core / most |
| Speech/language disorder | Behavioral/cognitive | HP:0002463 | Early childhood | Prominent | Frequent |
| Facial dysmorphism (coarse facies) | Physical | HP:0001999 / HP:0000280 | Congenital | Variable | Frequent |
| Acral/fifth-digit anomalies (nail/distal phalanx hypoplasia) | Physical | HP:0001829 / HP:0001162 | Congenital | Variable | Reported (p.Arg377Trp) |
| Feeding difficulties | Sign | HP:0011968 | Neonatal/infancy | — | BAFopathy-associated |
| Frequent infections | Sign | HP:0002719 | Childhood | — | BAFopathy-associated |
| Hypotonia | Sign | HP:0001252 | Infancy | — | BAFopathy-associated |

The broader Coffin-Siris core (Kosho et al. 2014, [PMID: 25169878](https://pubmed.ncbi.nlm.nih.gov/25169878/)) is: *"developmental delay or intellectual disability (ID), coarse facial appearance, feeding difficulties, frequent infections, and hypoplasia/aplasia of the fifth fingernails and fifth distal phalanges."* BAF-gene disorders are also associated with congenital diaphragmatic hernia ([PMID: 35796094](https://pubmed.ncbi.nlm.nih.gov/35796094/)) and, for some subunits, pituitary hypoplasia/growth hormone deficiency ([PMID: 36176497](https://pubmed.ncbi.nlm.nih.gov/36176497/)) — potential but not ACTL6A-confirmed associations.

**Quality-of-life impact.** Driven primarily by intellectual disability and language impairment, affecting education, communication, and independent living; formal QoL instrument data (EQ-5D/SF-36/PROMIS) are not available for this ultra-rare disorder.

---

## 4. Genetic / Molecular Information

**Causal gene.** _ACTL6A_ (BAF53a), 3q26.33, ENSG00000136518; GRCh37 chr3:179,280,668–179,306,196. Encodes a 429-aa, ~47.5 kDa nuclear actin-related protein (UniProt O96019: *"Involved in transcriptional activation and repression of select genes by chromatin remodeling... Component of SWI/SNF chromatin remodeling complexes"*).

**Pathogenic variants.** Reported disease variants are predominantly **missense** affecting conserved actin-like-domain residues, plus a **splice** variant causing an in-frame deletion:
- **p.Arg377Trp** — NM_004301.5:c.1129C>T — recurrent; recognizable BAFopathy phenotype (Pascolini 2020).
- **p.His105Arg** — c.314A>G.
- **p.Glu227Gln** — c.679G>C.

**ClinVar landscape (Finding F009; queried Nov 2026, 117 records, NM_004301.5):**

| Classification | Count |
|---|---|
| Uncertain significance (VUS) | 52 |
| Pathogenic | 25 |
| Likely pathogenic | 4 |
| Conflicting | 3 |
| Likely benign | 9 |
| Benign | 2 |

**Critical interpretation caveat:** The three literature-recurrent missense variants (p.Arg377Trp, p.His105Arg, p.Glu227Gln) are currently **Conflicting** in ClinVar, and the large majority of single-nucleotide ACTL6A variants are VUS. Nearly all ClinVar "Pathogenic/Likely pathogenic" entries are **large 3q chromosomal copy-number GAINS** (e.g., 3q26.31–29 ×3; 3q25–29 duplications) that merely span ACTL6A — not ACTL6A-specific point mutations. This reflects both the disorder's recency and the difficulty of classifying single-gene missense variants without functional/episignature confirmation.

**Allele frequency.** Pathogenic variants are absent or vanishingly rare in gnomAD (de novo). The gene is strongly LoF-constrained: pLI = 0.997, oe_lof = 0.078 (90% CI 0.031–0.246), LoF Z = 4.32; missense Z = 2.94 (oe_mis = 0.46) — among the most intolerant genes (Finding F008).

**Somatic vs germline.** Disease variants are **germline** (de novo). This contrasts sharply with the well-documented **somatic** oncogenic role: _ACTL6A_ is amplified early at 3q26 in squamous cell carcinomas (Finding F003; [PMID: 34687603](https://pubmed.ncbi.nlm.nih.gov/34687603/): *"The gene encoding the BAF subunit actin-like 6a (ACTL6A) is amplified early in the development of many squamous cell carcinomas (SCCs)"*; [PMID: 40950224](https://pubmed.ncbi.nlm.nih.gov/40950224/)).

**Functional consequences.** Likely **loss-of-function / haploinsufficiency or dominant-negative** effects on BAF53a's role in chromatin remodeling. (Across CSS genes, SMARCB1/SMARCA4/SMARCE1 variants trend dominant-negative/gain-of-function while ARID1A/ARID1B trend loss-of-function — [PMID: 25168959](https://pubmed.ncbi.nlm.nih.gov/25168959/); the precise mode for ACTL6A missense variants is not yet experimentally resolved.)

**Modifier genes / epigenetic info / chromosomal abnormalities.** No specific modifier genes established. A validated BAFopathy DNA-methylation episignature exists but does not yet cover ACTL6A (Finding F011). Large 3q26 copy-number variants spanning ACTL6A appear in ClinVar but are distinct contiguous-gene events, not point-mutation disease.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious factors are implicated. ACTL6A-related BAFopathy is a monogenic disorder arising from de novo germline variants; there is no established toxin, radiation, dietary, or pathogen contribution.

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. A **de novo heterozygous ACTL6A variant** (missense in the actin-like domain, splice, or LoF) **results in** reduced or altered BAF53a function/dosage.
2. Reduced functional BAF53a **leads to** impaired assembly/function of the **neural-progenitor BAF (npBAF) complex** (BAF53a is the progenitor-specific actin-related subunit).
3. Impaired npBAF function **stalls the neural-progenitor cell cycle** (demonstrated for BAF53a loss; Braun et al. 2021).
4. Cell-cycle stalling/loss of BAF53a **permits Polycomb accumulation**, which **results in decreased chromatin accessibility at pioneer-factor sites SOX2 and ASCL1** (demonstrated).
5. Reduced accessibility at these sites **blocks the normal progenitor-to-neuron transition / neurogenesis** (the programmed npBAF→nBAF, BAF53a→BAF53b switch, driven by miR-9*/miR-124, is disrupted; Yoo et al. 2009).
6. Impaired neurogenesis and cortical development **lead to** the clinical phenotype: **intellectual disability, developmental/language delay**, and — via BAF's broader developmental roles — **facial dysmorphism and acral/limb malformations** (*inferred* for dysmorphism; the mechanism-to-phenotype link for craniofacial/limb features is less directly demonstrated for ACTL6A specifically).

```
ACTL6A variant ──▶ ↓BAF53a function/dosage ──▶ defective npBAF complex
      │                                              │
      │                                    ┌─────────┴─────────┐
      │                              cell-cycle stall     Polycomb ↑
      │                                    │                 │
      │                                    └────────┬────────┘
      │                              ↓ chromatin accessibility
      │                               at SOX2 / ASCL1 sites
      ▼                                        │
 (also: shared subunit of           impaired npBAF→nBAF switch
  NuA4/TIP60 & INO80)               (BAF53a→BAF53b; miR-9*/miR-124)
      │                                        │
      └────────────────────┬───────────────────┘
                           ▼
              impaired neurogenesis / cortical development
                           ▼
       Intellectual disability, language delay, dysmorphism, acral anomalies
```

### Supporting detail

**Molecular identity and complex membership (Finding F004).** ACTL6A/BAF53a is a shared actin-related subunit of **SWI/SNF (BAF), NuA4/TIP60 histone acetyltransferase, and INO80** complexes (Xiao et al. 2021, [PMID: 33408251](https://pubmed.ncbi.nlm.nih.gov/33408251/): *"Actin-like 6A (ACTL6A) is a component of several chromatin remodeling complexes, including SWI/SNF, NuA4/TIP60 histone acetylase, and INO80."*). Functional conservation is deep: the Drosophila ortholog **Bap55** functions in both BRM (SWI/SNF) and TIP60 complexes, and *"the Bap55 mutant phenotype can be rescued by postmitotic expression of Bap55, or its human homologs BAF53a and BAF53b"* ([PMID: 21284845](https://pubmed.ncbi.nlm.nih.gov/21284845/)).

**Developmental switch (Finding F002).** Yoo et al. 2009 ([PMID: 19561591](https://pubmed.ncbi.nlm.nih.gov/19561591/)) showed npBAF complexes containing BAF53a are *"essential for neural-progenitor proliferation, and mice with reduced dosage for the genes encoding its subunits have defects in neural-tube closure similar to those in human spina bifida."* At mitotic exit, miR-9*/miR-124 repress BAF53a to allow the switch to BAF53b-containing nBAF. Braun et al. 2021 ([PMID: 33602870](https://pubmed.ncbi.nlm.nih.gov/33602870/)) showed *"early loss of the npBAF subunit BAF53a stalls the cell cycle to disrupt neurogenesis,"* mediated by Polycomb-driven loss of accessibility at SOX2/ASCL1 pioneer-factor sites.

**Why BAF53a and BAF53b are not interchangeable in neurons.** Though they rescue each other in ESC survival and in Drosophila dendrites, BAF53b has a neuron-specific role in dendritic outgrowth that BAF53a cannot replace, conferred by actin-fold subdomain 2 ([PMID: 17920018](https://pubmed.ncbi.nlm.nih.gov/17920018/)). This paralog specialization underlies the developmental-stage specificity of the BAF switch.

**Cellular processes / GO & CL suggestions.**
- Biological processes (GO): GO:0006338 chromatin remodeling; GO:0045944 positive regulation of transcription by RNA Pol II; GO:0007399 nervous system development; GO:0021895 cerebral cortex neuron differentiation; GO:0007049 cell cycle; GO:0045786 negative regulation of cell cycle.
- Subcellular (GO Cellular Component): GO:0005634 nucleus; GO:0071564 npBAF complex; GO:0016514 SWI/SNF complex; GO:0000812 Swr1/NuA4-related; GO:0031011 Ino80 complex.
- Cell types (CL): CL:0000047 neuronal stem cell / neural progenitor; CL:0000031 neuroblast; CL:0000540 neuron; CL:0002319 neural cell.

**Immune / metabolic / tissue-damage mechanisms.** Not primary in the germline disorder. (ACTL6A's metabolic/Warburg role via AP-1 and HIF1α/HIF2α is a **somatic cancer** mechanism — [PMID: 40950224](https://pubmed.ncbi.nlm.nih.gov/40950224/) — not germline BAFopathy.) "Frequent infections" in the BAFopathy spectrum is a clinical observation rather than a defined immunodeficiency mechanism.

---

## 7. Anatomical Structures Affected

- **Organ/system level — primary:** Central nervous system, especially **cerebral cortex** (UBERON:0000956) and **developing brain** (UBERON:0000955). Body system: nervous system.
- **Secondary/other involvement:** Craniofacial structures (dysmorphism); distal limbs — **digits/fingernails/distal phalanges** (acral anomalies); potential diaphragm (BAFopathy-associated CDH).
- **Tissue/cell level:** Neural tissue; principally **neural progenitor/stem cells** (CL:0000047) and their neuronal progeny (CL:0000540).
- **Subcellular:** **Nucleus** (GO:0005634) — chromatin/BAF, NuA4/TIP60, INO80 complexes. UniProt O96019 subcellular location: Nucleus.
- **Localization / lateralization:** CNS involvement is **bilateral/diffuse** (developmental). Acral anomalies are typically bilateral, with a fifth-digit predilection in the CSS spectrum.
- **UBERON suggestions:** UBERON:0000955 brain; UBERON:0000956 cerebral cortex; UBERON:0001466 manual digit; UBERON:0001705 nail.

---

## 8. Temporal Development

- **Onset:** **Congenital / pediatric.** Developmental concerns typically emerge in infancy/early childhood (delayed milestones, language delay); dysmorphism and acral anomalies are present at birth.
- **Onset pattern:** Insidious/chronic (developmental), not acute.
- **Progression:** The underlying brain developmental lesion is **static/non-progressive** in the neurodegenerative sense; functional impairments are **lifelong**. The trajectory is one of delay rather than regression. (By analogy to CSS, some physical features such as digital hypoplasia may become less noticeable with age — [PMID: 33768696](https://pubmed.ncbi.nlm.nih.gov/33768696/).)
- **Disease course:** Chronic, lifelong, stable-to-slowly-improving with intervention; not relapsing-remitting or episodic.
- **Critical periods:** Prenatal/early postnatal neurogenesis is the mechanistic window of vulnerability (npBAF→nBAF switch). Early-childhood developmental intervention is the practical window of therapeutic opportunity.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal dominant**, overwhelmingly **de novo** heterozygous variants.
- **Epidemiology:** **Ultra-rare**; no prevalence/incidence estimates available. Fewer than ~10 molecularly confirmed patients are described (Marom 2017: 3; Pascolini 2020: p.Arg377Trp; Chen 2022 cohort; Yuan 2021 case report [PMID: 34485408](https://pubmed.ncbi.nlm.nih.gov/34485408/)). No MONDO→Orphanet mapping and 0 curated associations in Monarch (Finding F010).
- **Penetrance:** Presumed high/complete for bona fide pathogenic variants (de novo in affected probands); formal estimates unavailable.
- **Expressivity:** **Variable** (ranging across degrees of intellectual disability — Marom 2017).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism / founder effects / consanguinity / carrier frequency:** Not established; de novo dominant inheritance means carrier screening and consanguinity are not relevant. gnomAD shows essentially no LoF carriers (high constraint).
- **Population demographics:** No ethnic predilection, geographic clustering, or sex bias established. Reported patients are too few to define a sex ratio or age distribution.

---

## 10. Diagnostics

**Recommended approach:** Molecular diagnosis via **trio exome sequencing (WES)** or **genome sequencing (WGS)**, identifying a de novo heterozygous ACTL6A variant. Given that most single-gene ACTL6A SNVs are currently VUS/conflicting in ClinVar (Finding F009), interpretation benefits from trio data (de novo status), phenotype concordance, and — in future — episignature confirmation.

- **Gene panels:** BAFopathy / Coffin-Siris / intellectual-disability panels that include ACTL6A alongside ARID1A/ARID1B, SMARCA4, SMARCB1, SMARCE1, SMARCC2, DPF2, ARID2, SOX11, SOX4, SMARCA2.
- **Single-gene testing:** Possible once ACTL6A suspected, but panel/exome is preferred given phenotypic overlap.
- **Chromosomal microarray (CMA):** Useful to detect/contextualize large 3q26 copy-number variants spanning ACTL6A (which dominate ClinVar "pathogenic" CNV entries) — though these contiguous-gene events are mechanistically distinct from point-mutation BAFopathy.
- **Karyotyping/FISH:** Generally lower yield; relevant only for large structural rearrangements.
- **Not applicable:** Mitochondrial DNA testing; repeat-expansion testing.

**Omics / episignature.** A validated **BAFopathy DNA-methylation episignature** (EpiSign) exists and is used clinically to reclassify VUS for ARID1B, SMARCB1, SMARCA4, SMARCA2 (Aref-Eshghi 2018, [PMID: 30459321](https://pubmed.ncbi.nlm.nih.gov/30459321/): *"We report overlapping peripheral blood DNA methylation epi-signatures in individuals with various subtypes of CSS (ARID1B, SMARCB1, and SMARCA4) and NCBRS (SMARCA2)"*; Trajkova 2024, [PMID: 38751117](https://pubmed.ncbi.nlm.nih.gov/38751117/)), but **ACTL6A is not yet in the validated cohort** (Finding F011). Because paralogous BAF subunits can share episignatures, it is biologically plausible — but unproven — that ACTL6A variants map to the BAFopathy signature.

**Clinical/imaging tests:** Brain MRI (structural brain anomalies, corpus-callosum abnormalities seen across CSS), developmental/neuropsychological assessment, dysmorphology exam, hand/foot radiographs for acral anomalies. No specific biomarker or laboratory abnormality is diagnostic.

**Differential diagnosis:** Other BAFopathies/Coffin-Siris subtypes (ARID1B, SMARCB1, SMARCA4, SMARCE1, ARID1A), Nicolaides-Baraitser syndrome (SMARCA2), ACTL6B-related disorder (BAF53b; distinct — intellectual disability with epilepsy), and other syndromic intellectual-disability disorders. Distinguishing feature: the specific ACTL6A variant on sequencing.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No evidence of reduced life expectancy from the core neurodevelopmental phenotype; most BAFopathy patients survive into adulthood. Severe multi-organ involvement (as can occur in some CSS subtypes, e.g., SMARCB1/ARID1A) could affect prognosis, but ACTL6A-specific mortality data are unavailable.
- **Morbidity/function:** Dominated by **intellectual disability and language impairment**, with lifelong functional/educational impact and variable support needs. Acral anomalies are generally non-disabling.
- **Disease course/complications:** Potential BAFopathy-associated complications (feeding difficulties, recurrent infections, hypotonia, and — rarely — structural anomalies such as CDH or endocrine involvement) warrant surveillance, though their frequency in ACTL6A specifically is undefined.
- **Prognostic factors:** Likely variant type/location and degree of intellectual disability; formal prognostic models do not exist for this ultra-rare disorder.
- **QoL measures:** No disorder-specific instruments reported.

---

## 12. Treatment

**There is no disease-specific or disease-modifying therapy.** Management is **supportive and multidisciplinary**, mirroring Coffin-Siris/BAFopathy care:

- **Developmental/rehabilitative (NCIT suggestions):** Early intervention; **speech-language therapy**, **physical therapy** (NCIT:C15402), **occupational therapy** (NCIT:C15214); special education.
- **Supportive care:** Management of feeding difficulties (nutrition support), treatment of recurrent infections, orthopedic/surveillance management of anomalies, ophthalmologic/audiologic evaluation.
- **Pharmacotherapy:** Symptom-directed only (e.g., anti-seizure medication if seizures occur; behavioral/ADHD management as needed). No pharmacogenomic guidance specific to ACTL6A.
- **Advanced therapeutics (gene/cell/RNA/targeted/immunotherapy):** None approved or in trials for this disorder.
- **Surgical/interventional:** Only for specific structural complications (e.g., CDH repair, if present).
- **Experimental/clinical trials:** No disorder-specific trials (no NCT identifiers) identified.
- **Treatment strategy:** Individualized supportive care guided by the specific phenotype; no algorithm or combination/precision regimen exists.

---

## 13. Prevention

- **Primary prevention:** Not applicable to a de novo dominant disorder; cannot be prevented through lifestyle or environmental measures.
- **Genetic counseling (key preventive/advisory service):** For families, recurrence risk is low (de novo), but gonadal/germline mosaicism cannot be fully excluded, so empiric recurrence risk is quoted as low-but-nonzero. **Prenatal/preimplantation genetic testing** is possible for a known familial variant.
- **Secondary prevention:** Early developmental screening and intervention to optimize functional outcomes; surveillance for BAFopathy-associated complications.
- **Immunization/public-health/environmental measures:** Not applicable (routine childhood immunizations recommended as for any child; no disorder-specific vaccine).
- **Carrier/newborn screening:** Not applicable (dominant, de novo; not on newborn screening panels).

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs (NCBI Gene suggestions):** Human _ACTL6A_ (Gene 86); mouse _Actl6a_ (Gene 56456); Drosophila ortholog **Bap55**. Paralog: _ACTL6B_ (BAF53b).
- **Evolutionary conservation:** Deeply conserved actin-related chromatin-remodeling subunit. Cross-species functional conservation is demonstrated: the Drosophila _Bap55_ mutant dendrite-targeting phenotype is rescued by human BAF53a or BAF53b ([PMID: 21284845](https://pubmed.ncbi.nlm.nih.gov/21284845/)), and the yeast/mammalian SWI/SNF core is conserved ([PMID: 10078207](https://pubmed.ncbi.nlm.nih.gov/10078207/)).
- **Natural disease in other species / veterinary relevance / zoonosis:** None reported; no naturally occurring animal disease, no breed associations (no VBO entries), and no transmissibility (not applicable to a Mendelian disorder).

---

## 15. Model Organisms

| Model | Type | Key finding | PMID |
|---|---|---|---|
| Mouse ES cells (tet-inducible _Baf53a_ cKO) | Cellular/mammalian | _Baf53a_ loss → p53/p21/cleaved-Caspase-3 ↑, ESC death; rescued by Baf53a **or** Baf53b (not M3 mutant) | [29070872](https://pubmed.ncbi.nlm.nih.gov/29070872/) |
| Mouse ES cells | Cellular/mammalian | Actl6a protects ESCs from primitive-endoderm differentiation via Nanog/Sox2 | [25802002](https://pubmed.ncbi.nlm.nih.gov/25802002/) |
| Mouse (npBAF-subunit dosage reduction) | Mammalian, in vivo | Reduced dosage → neural-tube-closure defects (spina bifida-like); BAF53a→BAF53b switch gates neurogenesis | [19561591](https://pubmed.ncbi.nlm.nih.gov/19561591/) |
| Mouse developing cortex (BAF53a loss) | Mammalian, in vivo | BAF53a loss stalls progenitor cell cycle; Polycomb ↑, ↓accessibility at SOX2/ASCL1 | [33602870](https://pubmed.ncbi.nlm.nih.gov/33602870/) |
| Drosophila (_Bap55_ mutant) | Invertebrate | Dendrite/olfactory-projection mistargeting via TIP60 complex; rescued by human BAF53a/BAF53b | [21284845](https://pubmed.ncbi.nlm.nih.gov/21284845/) |

**Genetic model types available:** Conditional/inducible knockouts and rescue constructs in mouse ESCs; Drosophila loss-of-function mutants with human-gene rescue. **No knock-in mouse carrying a patient ACTL6A missense variant (e.g., p.Arg377Trp) has been reported** — a key gap.

**Phenotype recapitulation:** Models robustly recapitulate the **core mechanistic axis** (progenitor proliferation, cell-cycle control, neurogenesis switch, dosage sensitivity), strongly supporting the human mechanism — e.g., Zhu et al. 2017 ([PMID: 29070872](https://pubmed.ncbi.nlm.nih.gov/29070872/)): *"Baf53a is involved in the survival of ES cells by regulating p53 and Caspase3, and that Baf53b is able to compensate for this functional aspect of Baf53a."* **Limitations:** Existing models test null/knockdown rather than the specific heterozygous missense alleles seen in patients; they do not reproduce the full human syndromic phenotype (dysmorphism, acral anomalies, cognition). Resources: MGI (_Actl6a_), FlyBase (_Bap55_), Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation (Synthesis)

ACTL6A-related BAFopathy is best understood as a **dosage-sensitive chromatin-remodeling disorder of neurodevelopment**. BAF53a is the actin-related subunit that defines the **neural-progenitor** BAF complex; its tightly timed, microRNA-driven replacement by BAF53b converts proliferating progenitors into post-mitotic neurons. Germline perturbation of BAF53a dosage or function derails this switch at the point of cell-cycle exit — Polycomb accumulates, pioneer-factor (SOX2/ASCL1) sites lose accessibility, and neurogenesis is blocked — producing intellectual disability with prominent language involvement and, through BAF's broader developmental roles, the craniofacial and acral features that place the disorder within the Coffin-Siris/BAFopathy spectrum.

Three independent evidence streams converge on this model: (1) **human genetics** (recurrent de novo variants; BAFopathy-recognizable phenotype), (2) **population constraint** (pLI 0.997 / LOEUF 0.25 — the gene cannot tolerate loss), and (3) **developmental biology** (mouse/fly models proving BAF53a's progenitor-specific, cell-cycle-gating, dosage-sensitive role). The same gene's **somatic** amplification drives squamous cell carcinoma via the opposite dosage direction — a biological mirror image that reinforces the centrality of **BAF53a dosage** to cell fate. Son & Crabtree (2014, [PMID: 25195934](https://pubmed.ncbi.nlm.nih.gov/25195934/)) frame the broader principle: *"The high frequency of BAF subunit mutations in neurological disorders underscores the rate-determining role of BAF complexes in neural development, homeostasis, and plasticity."*

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [28649782](https://pubmed.ncbi.nlm.nih.gov/28649782/) | Heterozygous ACTL6A variants → intellectual disability | **Establishes disease gene** (first description, 3 subjects) |
| [31994175](https://pubmed.ncbi.nlm.nih.gov/31994175/) | p.Arg377Trp recognizable BAF-opathy | Recurrent variant; dysmorphism + acral malformations |
| [34906496](https://pubmed.ncbi.nlm.nih.gov/34906496/) | BAFopathy exome cohort (16,243) | Independent de novo/pLoF support |
| [19561591](https://pubmed.ncbi.nlm.nih.gov/19561591/) | miRNA-mediated BAF switching | Mechanism: npBAF→nBAF, dosage sensitivity |
| [33602870](https://pubmed.ncbi.nlm.nih.gov/33602870/) | BAF subunit switching / cell-cycle exit | Mechanism: cell-cycle stall, Polycomb, SOX2/ASCL1 |
| [33408251](https://pubmed.ncbi.nlm.nih.gov/33408251/) | ACTL6A in DNA repair | Multi-complex membership (SWI/SNF, TIP60, INO80) |
| [21284845](https://pubmed.ncbi.nlm.nih.gov/21284845/) | Bap55 / TIP60 dendrite targeting | Cross-species conservation; rescue by BAF53a/b |
| [25169878](https://pubmed.ncbi.nlm.nih.gov/25169878/) | CSS/BAFopathy review | Defines BAFopathy/CSS core phenotype |
| [29070872](https://pubmed.ncbi.nlm.nih.gov/29070872/) | Baf53a ESC survival | Model: p53-apoptosis, Baf53b compensation |
| [25802002](https://pubmed.ncbi.nlm.nih.gov/25802002/) | Actl6a protects ESCs | Model: pluripotency via Nanog/Sox2 |
| [30459321](https://pubmed.ncbi.nlm.nih.gov/30459321/) | BAFopathy episignatures | Diagnostic tool (excludes ACTL6A) |
| [38751117](https://pubmed.ncbi.nlm.nih.gov/38751117/) | DNA-methylation in NDD | Paralogous subunits share episignatures |
| [25195934](https://pubmed.ncbi.nlm.nih.gov/25195934/) | BAF in neural development | Rate-determining role of BAF in neurodevelopment |
| [34687603](https://pubmed.ncbi.nlm.nih.gov/34687603/) | ACTL6A in SCC | Contrasting somatic oncogenic role |
| [34485408](https://pubmed.ncbi.nlm.nih.gov/34485408/) | BAF-opathies/SSRIDD case report | Additional ACTL6A patient; SSRIDD terminology |

---

## Limitations and Knowledge Gaps

1. **Very small patient number** (<~10 reported) → no reliable phenotype frequencies, natural history, prognosis, penetrance, or genotype-phenotype correlation.
2. **Variant classification is immature:** the recurrent literature variants (p.Arg377Trp, p.His105Arg, p.Glu227Gln) are **Conflicting** in ClinVar; most single-gene SNVs are VUS. Many ClinVar "pathogenic" entries are large 3q CNVs spanning ACTL6A, not point mutations (Finding F009).
3. **No ACTL6A-specific episignature** yet validated (Finding F011), limiting a powerful variant-reclassification route available for other BAFopathies.
4. **No OMIM/Orphanet entry**, no ICD/MeSH code, and no curated phenotype associations in Monarch (Finding F010).
5. **Mode of action (haploinsufficiency vs dominant-negative) unresolved** for patient missense variants; existing models use null/knockdown, not knock-in patient alleles.
6. **No disease-specific therapy or clinical trials.**

---

## Proposed Follow-up Experiments / Actions

1. **Build a patient registry / GeneMatcher cohort** to aggregate additional ACTL6A cases and define phenotype frequencies, natural history, and genotype-phenotype correlations.
2. **Derive an ACTL6A DNA-methylation episignature** by including confirmed ACTL6A patients in EpiSign cohorts (leveraging paralog-sharing from [PMID: 38751117](https://pubmed.ncbi.nlm.nih.gov/38751117/)) to reclassify the many VUS.
3. **Functional assays for recurrent missense variants** (p.Arg377Trp, p.His105Arg, p.Glu227Gln): BAF53a incorporation into BAF/TIP60/INO80 complexes, β-actin/BRG1 binding, and chromatin accessibility at SOX2/ASCL1 sites — to resolve LoF vs dominant-negative.
4. **Generate knock-in mouse / patient-iPSC-derived cortical organoid models** carrying p.Arg377Trp to test recapitulation of cell-cycle stalling and neurogenesis defects.
5. **Submit structured variant curation to ClinVar/ClinGen** and pursue MONDO→OMIM/Orphanet mapping to formalize the disease entity.
6. **Define surveillance guidelines** for BAFopathy-associated complications (feeding, infection, structural anomalies) adapted to ACTL6A.

---

*Evidence source types: human clinical genetics (Marom 2017, Pascolini 2020, Chen 2022, Yuan 2021); model organism (Yoo 2009, Braun 2021, Zhu 2017, Lu 2015, Tea & Luo 2011); in vitro/biochemical (Xiao 2021, Phelan 1999); computational/database (gnomAD constraint, ClinVar, Monarch/MONDO, UniProt).*


## Artifacts

- [OpenScientist final report](ACTL6A-related_BAFopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ACTL6A-related_BAFopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 22 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 12 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001249` (1 mention) - the report calls it "Cognitive sign"; HP calls it **Intellectual disability**
- `HP:0002463` (1 mention) - the report calls it "Behavioral/cognitive"; HP calls it **Language impairment**
- `HP:0011968` (1 mention) - the report calls it "Sign"; HP calls it **Feeding difficulties**
- `HP:0002719` (1 mention) - the report calls it "Sign"; HP calls it **Recurrent infections**
- `HP:0001252` (1 mention) - the report calls it "Sign"; HP calls it **Hypotonia**
- `NCIT:C15402` (1 mention) - the report calls it "physical therapy"; NCIT calls it **Conization**
- `NCIT:C15214` (1 mention) - the report calls it "occupational therapy"; NCIT calls it **Craniotomy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001263` (1 mention) - the report calls it "Cognitive/motor sign"; HP calls it **Global developmental delay**, and lists "Cognitive delay" among its other names
- `GO:0005634` (2 mentions) - the report calls it "Nucleus", "Subcellular:** **Nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names
- `CL:0000047` (2 mentions) - the report calls it "neural progenitor/stem cells"; CL calls it **neural stem cell**
- `UBERON:0000955` (2 mentions) - the report calls it "developing brain"; UBERON calls it **brain**, and lists "the brain" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005634` - called "Nucleus", "Subcellular:** **Nucleus"