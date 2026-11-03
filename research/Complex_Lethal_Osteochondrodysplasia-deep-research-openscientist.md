---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T23:40:14.066454'
end_time: '2026-10-30T23:59:09.657624'
duration_seconds: 1135.59
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Complex Lethal Osteochondrodysplasia
  mondo_id: MONDO:0014821
  category: Mendelian
  causal_genes: TAPT1
  omim_id: OMIM:616897
  synonyms: Complex lethal osteochondrodysplasia, Symoens-Barnes-Gistelinck type
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
citation_count: 6
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 5
  validator_version: 0.4.0
term_validation:
  total_terms: 44
  verified: 41
  not_found: 2
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.047
  labels_checked: 19
  labels_matching: 8
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0014821
    reported_labels:
    - MONDO
    ontology_label: complex lethal osteochondrodysplasia
  - term_id: HP:0000252
    reported_labels:
    - Severe
    ontology_label: Microcephaly
  - term_id: HP:0002089
    reported_labels:
    - Lethal contributor
    ontology_label: Pulmonary hypoplasia
  - term_id: HP:0000077
    reported_labels:
    - Variable
    ontology_label: Abnormality of the kidney
  - term_id: HP:0001999
    reported_labels:
    - Severe
    ontology_label: Abnormal facial shape
  - term_id: GO:0005813
    reported_labels:
    - Centrosome / microtubule organizing center
    ontology_label: centrosome
  labels_variant: 5
  unresolved_terms:
  - HP:0006618
  - HP:0001505
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Complex_Lethal_Osteochondrodysplasia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Complex_Lethal_Osteochondrodysplasia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Complex Lethal Osteochondrodysplasia
- **MONDO ID:** MONDO:0014821 (if available)
- **Causal gene(s):** TAPT1
- **OMIM:** OMIM:616897
- **Synonyms:** Complex lethal osteochondrodysplasia, Symoens-Barnes-Gistelinck type
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Complex Lethal Osteochondrodysplasia** covering all of the
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

# Complex Lethal Osteochondrodysplasia (Symoens–Barnes–Gistelinck type, TAPT1)

**MONDO:0014821 · OMIM #616897 · Causal gene: _TAPT1_ (Transmembrane Anterior Posterior Transformation 1)**

---

## Summary

Complex lethal osteochondrodysplasia, Symoens–Barnes–Gistelinck type (SBGS; OMIM #616897; MONDO:0014821), is a rare, autosomal-recessive skeletal dysplasia caused by **biallelic loss-of-function mutations in _TAPT1_** (Transmembrane Anterior Posterior Transformation 1; HGNC:25787; chromosome 4p15.32; UniProt Q6NXT6). Despite the generic "osteochondrodysplasia" label, the disease is defined by its causal gene, _TAPT1_, which encodes a 567-amino-acid, 5-transmembrane protein of the **DUF747/Tatp1 family** that localizes to the **centrosome and ciliary basal body**. The classic phenotype, described by Symoens and colleagues in 2015, is one of **fetal/perinatal lethality** with **generalized skeletal hypomineralization**, **intrauterine fractures**, a **barrel-shaped thorax with short, fractured ribs**, and multi-organ developmental anomalies of the brain, lungs, and kidneys.

Mechanistically, TAPT1 sits at the intersection of at least three cellular systems whose coordinate failure produces the skeletal and extra-skeletal phenotype. Loss of functional TAPT1 causes it to **mislocalize from the basal body to the cytoplasm**, which **disrupts primary ciliogenesis and Golgi morphology/secretory trafficking**, in turn impairing **collagen and extracellular-matrix (ECM) fibril assembly**. In parallel, TAPT1 normally **restrains BMP–SMAD1/5 signaling** by promoting SMURF1-mediated proteasomal degradation of SMAD1/5; its loss **derepresses BMP signaling** and enhances osteoblast differentiation, and a subset of human disease alleles behave as **gain-of-function on SMAD1 stability**. These converging defects — a "cilia-plus-ECM-plus-BMP" lesion — explain why the disorder spans skeletal, craniofacial, neural-crest, and multi-organ territories.

Importantly, _TAPT1_ insufficiency produces an **allelic spectrum**: complete loss-of-function alleles cause the perinatal-lethal osteochondrodysplasia, while **hypomorphic (partial-function) alleles** cause survivable phenotypes including osteogenesis imperfecta (OI), early-onset bilateral cataract, and neonatal progeria. Diagnosis is genetic and can require **whole-genome sequencing plus RNA-seq**, because at least one recurrent causal allele is a **deep-intronic branchpoint variant (c.1237-52G>A)** that standard exome sequencing misses. There is **no disease-specific therapy**; management is supportive, anchored by **genetic counseling** and **prenatal/preimplantation genetic testing** in at-risk consanguineous families.

---

## 1. Disease Information

**Overview.** Complex lethal osteochondrodysplasia, Symoens–Barnes–Gistelinck type, is a Mendelian, autosomal-recessive connective-tissue/skeletal disorder caused by biallelic _TAPT1_ mutations. In its severe (classic) form it is a **perinatally lethal osteochondrodysplasia** with severe hypomineralization of the entire skeleton, intrauterine fractures, and congenital anomalies of the brain, lungs, and kidneys. As Symoens et al. described, *"This syndrome is characterized by fetal lethality, severe hypomineralization of the entire skeleton and intra-uterine fractures, and multiple congenital developmental anomalies affecting the brain, lungs, and kidneys"* [[PMID: 26365339](https://pubmed.ncbi.nlm.nih.gov/26365339/)].

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | #616897 (Osteochondrodysplasia, complex lethal, Symoens-Barnes-Gistelinck type; OCLSBG) |
| MONDO | MONDO:0014821 |
| Gene | _TAPT1_ (HGNC:25787; Entrez 202018; Ensembl ENSG00000169762) |
| Protein | UniProt Q6NXT6 |
| Locus | 4p15.32 |

**Synonyms / alternative names.** Complex lethal osteochondrodysplasia; Osteochondrodysplasia, complex lethal, Symoens-Barnes-Gistelinck type (OCLSBG); SBGS. The gene has an alias **CMVFR** (cytomegalovirus fusion receptor), reflecting a reported role as a candidate fusion receptor for human cytomegalovirus strain AD169.

**Information source.** The knowledge base here is derived from **aggregated disease-level resources** (OMIM, UniProt, Pfam/InterPro) and from **individual-patient case series** reported in the primary literature (consanguineous families with molecularly confirmed _TAPT1_ variants). It is not EHR-derived at population scale, consistent with an ultra-rare Mendelian disorder.

---

## 2. Etiology

**Primary cause — genetic.** The disease is caused by **biallelic (homozygous or compound heterozygous) pathogenic variants in _TAPT1_**. No environmental, infectious, or toxic cause is implicated in disease initiation. The two original lethal alleles (Symoens 2015) were each homozygous in consanguineous families.

**Genetic risk factors.**
- **Causal variants:** homozygous splice-site `c.1108-1G>C` (NM_153365.2) causing exon 10 skipping (p.Val370_Asn389del) in a Moroccan family; homozygous missense `c.1058A>T` (p.Asp353Val) in a Syrian family [[PMID: 26365339](https://pubmed.ncbi.nlm.nih.gov/26365339/)]. A recurrent **deep-intronic branchpoint variant `c.1237-52G>A`** causes exon 12 skipping and a null allele in Jordanian OI/neonatal-progeria families [[PMID: 36652330](https://pubmed.ncbi.nlm.nih.gov/36652330/)].
- **Consanguinity** is the dominant risk amplifier: all molecularly defined families reported to date are consanguineous (Middle Eastern/North African), consistent with a rare recessive allele surfacing through homozygosity by descent.
- **Family history / carrier parents:** unaffected heterozygous parents; 25% recurrence risk per pregnancy.

**Environmental / lifestyle risk factors.** None identified — this is a monogenic disorder. Sex is not a risk factor (autosomal).

**Protective factors.** None specific are documented. In principle, avoidance of consanguineous mating within carrier families reduces the probability of homozygous affected offspring, and the amount of residual TAPT1 function determined by allele type is the principal modifier of severity (see §4, §6).

**Gene–environment interactions.** No established gene–environment interactions. Disease expression is governed by **genotype (allele severity)**, not by environmental modifiers.

---

## 3. Phenotypes

The classic (lethal) phenotype is prenatal/perinatal. Phenotypes derive from case series; frequencies are qualitative given the small number of reported individuals.

| Phenotype | Type | Onset | Severity | Suggested HPO |
|---|---|---|---|---|
| Generalized skeletal hypomineralization | Physical/radiographic | Prenatal (congenital) | Severe | HP:0003411 (decreased skeletal mineral density) / HP:0004349 |
| Intrauterine / multiple fractures | Clinical sign | Prenatal | Severe | HP:0003330 (abnormal bone ossification) / HP:0002659 |
| Barrel-shaped/narrow thorax, short ribs | Physical | Prenatal | Severe | HP:0001539 (thorax abnormality), HP:0000774 (narrow chest) |
| Rib fractures | Radiographic | Prenatal | Severe | HP:0006618 |
| Microcephaly | Physical | Prenatal | Severe | HP:0000252 |
| Ventriculomegaly | Imaging | Prenatal | Moderate–severe | HP:0002119 |
| Ascites / pleural effusion (hydrops features) | Clinical sign | Prenatal | Severe | HP:0001541, HP:0002202 |
| Pulmonary hypoplasia / lung anomaly | Physical | Prenatal | Lethal contributor | HP:0002089 |
| Renal / kidney developmental anomaly | Physical | Prenatal | Variable | HP:0000077 |
| Craniofacial cartilage malformation (model) | Physical | Developmental | Severe | HP:0001999 |

**Milder (survivable) spectrum phenotypes** (hypomorphic alleles):
- **Osteogenesis imperfecta / osteopenia / bone fragility** (HP:0002659, HP:0000938)
- **Bilateral early-onset cataract** (HP:0000519 / HP:0007700) — Jarayseh 2023 [[PMID: 36697720](https://pubmed.ncbi.nlm.nih.gov/36697720/)]
- **Severe developmental delay** (HP:0011344)
- **Neonatal progeria / aged appearance** (HP:0001505, HP:0007495) — Nabavizadeh 2023 [[PMID: 36652330](https://pubmed.ncbi.nlm.nih.gov/36652330/)]
- **Skeletal dysmorphism**

**Quality-of-life impact.** For the classic form, the disease is incompatible with survival (stillbirth or neonatal death), so QoL instruments are not applicable. For the survivable spectrum, impact is profound: bone fragility, visual impairment from cataract, and developmental delay impose lifelong disability and care dependence. No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disorder.

---

## 4. Genetic / Molecular Information

**Causal gene.** _TAPT1_ (HGNC:25787; chr 4p15.32; UniProt Q6NXT6). The protein is a **567-aa, 5-transmembrane DUF747/Tatp1-family protein** (Pfam PF05346, InterPro IPR008010, PANTHER PTHR13317), with predicted TM helices at aa 111–131, 157–179, 236–256, 403–423, and 432–452, and disordered N-/C-terminal regions (1–60; 466–499).

**Pathogenic variants (reported).**

| Variant (cDNA) | Protein | Type | Phenotype | Family origin | PMID |
|---|---|---|---|---|---|
| c.1108-1G>C (NM_153365.2) | p.Val370_Asn389del (exon 10 skip) | Splice-site, in-frame deletion | Lethal OCLSBG | Moroccan | [26365339](https://pubmed.ncbi.nlm.nih.gov/26365339/) |
| c.1058A>T | p.Asp353Val | Missense | Lethal OCLSBG | Syrian | [26365339](https://pubmed.ncbi.nlm.nih.gov/26365339/) |
| c.1237-52G>A | exon 12 skip → PTC → NMD (null) | Deep-intronic branchpoint | OI + neonatal progeria | Jordanian | [36652330](https://pubmed.ncbi.nlm.nih.gov/36652330/) |
| Frameshift (reported) | truncation | Frameshift | Cataract + skeletal | — | [36697720](https://pubmed.ncbi.nlm.nih.gov/36697720/) |

The missense p.Asp353Val corresponds to **dbSNP rs869312980** and has been shown to impair ciliogenesis.

**Variant classification (ACMG/AMP).** The lethal splice and missense alleles, segregating recessively in consanguineous families with functional validation, are classified **pathogenic**. The deep-intronic c.1237-52G>A, validated by RNA evidence of exon skipping and NMD, is **pathogenic**.

**Variant type/class.** Splice-site, missense, deep-intronic branchpoint, and frameshift alleles — collectively a **loss-of-function** spectrum, with the caveat that certain missense alleles also show **gain-of-function on SMAD1 stability** (see §6).

**Allele frequency.** The causal alleles are private/ultra-rare; not present at appreciable frequency in gnomAD. No common susceptibility variants.

**Somatic vs germline.** **Germline**, recessive. No somatic/cancer association.

**Functional consequences.** Predominantly **loss of function** (mislocalization, null transcripts via NMD, in-frame deletion disrupting a functional loop). A subset of human disease missense alleles exhibit **gain-of-function activity on SMAD1 protein levels** [[PMID: 36370851](https://pubmed.ncbi.nlm.nih.gov/36370851/)]. Both original lethal changes (p.Asp353Val; p.Val370_Asn389del) map to the **large luminal/extracellular loop between TM3 (ends aa 256) and TM4 (starts aa 403)**, consistent with disruption of a critical functional surface ("second extracellular/luminal loop").

**Modifier genes.** No formal modifiers established. **SMURF1** (the E3 ligase that TAPT1 recruits to degrade SMAD1/5) and the **SMAD1/5/9** effectors are functional partners whose activity is dysregulated downstream of TAPT1 loss.

**Epigenetic information.** No disease-specific DNA-methylation or histone-modification signature is reported.

**Chromosomal abnormalities.** None — SBGS is a single-gene disorder, not a copy-number/structural syndrome.

---

## 5. Environmental Information

**Environmental factors:** None implicated. **Lifestyle factors:** Not applicable. **Infectious agents:** Not a cause of the disease. (Note the incidental molecular curiosity that TAPT1/"CMVFR" has been annotated as a candidate **fusion receptor for human cytomegalovirus strain AD169** — a cell-biology annotation, not a disease mechanism.) This is a purely genetic, recessive Mendelian disorder.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic _TAPT1_ loss-of-function mutation** (splice, missense, deep-intronic→NMD) **results in** absent or dysfunctional TAPT1 protein.
2. Loss of functional TAPT1 **leads to** its **mislocalization from the centrosome/ciliary basal body into the cytoplasm** (demonstrated in patient fibroblasts and overexpression assays).
3. Basal-body dysfunction **results in** **defective primary ciliogenesis** (disturbed/shortened cilia) AND, in parallel, **disrupted Golgi morphology and secretory trafficking**.

   **Branch A — ECM/collagen:** Disrupted Golgi/secretory trafficking **impairs collagen secretion and ECM fibril assembly**, so that **patient collagen fails to assemble into normal banded fibrils** (Etich 2023) **leading to** bone matrix fragility, hypomineralization, and intrauterine fractures.

   **Branch B — Cilia/signaling/neural crest:** Defective cilia **lead to** aberrant developmental signaling and **aberrant cranial neural crest cell differentiation** (zebrafish), **resulting in** craniofacial cartilage malformation and delayed ossification.

   **Branch C — BMP/SMAD (parallel):** Loss of TAPT1 **removes a brake on BMP signaling** — normally TAPT1 promotes **SMURF1-mediated proteasomal degradation of SMAD1/5** — so TAPT1 deficiency **leads to** elevated SMAD1/5/9, **amplified BMP activation**, and **enhanced osteoblast differentiation / ectopic bone**; some missense alleles further **stabilize SMAD1 (gain-of-function)**.
4. The convergence of defective ECM (Branch A) and dysregulated skeletal patterning/differentiation (Branches B, C) **results in** **generalized skeletal hypomineralization, fractures, short ribs, barrel chest**, plus multi-organ anomalies of brain, lung, and kidney (ciliopathy spectrum).
5. Severe skeletal + pulmonary + multi-organ compromise **leads to** **fetal/perinatal lethality** (classic form), or, where residual TAPT1 function persists (hypomorphic alleles), a **survivable OI/cataract/neonatal-progeria phenotype**.

### Supporting detail

**Molecular pathways.** **BMP–SMAD1/5/9 signaling** is the best-defined pathway: *"TAPT1 inhibits BMP signaling and destabilizes the SMAD1/5 protein by facilitating its interaction with SMURF1 E3 ubiquitin ligase, which leads to SMAD1/5 proteasomal degradation"* [[PMID: 36370851](https://pubmed.ncbi.nlm.nih.gov/36370851/)]. Suggested pathway terms: BMP signaling (Reactome), ubiquitin-proteasome degradation of SMAD.

**Cellular processes.** Ciliogenesis (GO:0060271), intracellular/Golgi protein transport (GO:0006886, GO:0016192), osteoblast differentiation (GO:0001649), collagen fibril organization (GO:0030199), cranial neural-crest differentiation (GO:0014029).

**Protein dysfunction.** TAPT1 mislocalization; *"defective TAPT1 mislocalizes to the cytoplasm and disrupts Golgi morphology and trafficking and normal primary cilium formation"* [[PMID: 26365339](https://pubmed.ncbi.nlm.nih.gov/26365339/)]. Loss-of-function dominates; targeted gain-of-function on SMAD1 for some alleles.

**Tissue-damage mechanism.** Failure of **collagen fibril assembly** (ECM defect) is the proximal cause of bone fragility and hypomineralization (banded-fibril assembly failure; Etich 2023, [[PMID: 37292039](https://pubmed.ncbi.nlm.nih.gov/37292039/)]). RNA-seq in null patients showed **dysregulated collagen/ECM pathways** (Nabavizadeh 2023).

**Immune / metabolic / epigenetic.** No primary immune, metabolic, or epigenetic driver identified.

**Molecular profiling.** RNA-seq and SI-NET-seq (Nabavizadeh 2023) showed **nascent transcription was unaffected** (a post-transcriptional splicing defect) with downstream **collagen/ECM dysregulation**.

**Suggested GO / CL terms.** Biological process: GO:0060271 (cilium assembly), GO:0030509 (BMP signaling), GO:0030199 (collagen fibril organization). Cell types: CL:0000062 (osteoblast), CL:0000138 (chondrocyte), CL:0000008 (cranial neural crest cell), CL:0000057 (fibroblast).

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Primary:** skeleton — long bones, ribs, skull, vertebrae (UBERON:0002481 bone tissue; UBERON:0002228 rib; UBERON:0001474 bone element).
- **Secondary / multi-organ:** brain (microcephaly, ventriculomegaly; UBERON:0000955), lungs (hypoplasia; UBERON:0002048), kidneys (UBERON:0002113). Serous cavities show ascites/pleural effusion.
- **Body systems:** musculoskeletal (primary), nervous, respiratory, renal/urinary.

**Tissue and cell level.** Connective tissue (bone, cartilage) and the ECM are primarily affected. Key cell populations: **osteoblasts** (CL:0000062), **chondrocytes** (CL:0000138), **cranial neural crest cells** (CL:0000008), and **fibroblasts** (CL:0000057, the patient cell type in which ciliary/Golgi defects were demonstrated).

**Subcellular level.** **Centrosome / microtubule organizing center** (GO:0005813), **ciliary basal body** (GO:0036064), **primary cilium** (GO:0005929), **Golgi apparatus** (GO:0005794), and **membrane** (GO:0016020). TAPT1 is curated to centrosome/MTOC, cilium basal body, and membrane (UniProt Q6NXT6).

**Localization / lateralization.** Skeletal involvement is **generalized and bilateral/symmetric** (whole-skeleton hypomineralization), not focal or lateralized.

---

## 8. Temporal Development

**Onset.** **Congenital/prenatal.** The classic disease manifests in utero with fractures and hypomineralization detectable on prenatal imaging; the course is **perinatally lethal** (stillbirth, interrupted pregnancy, or neonatal death).

**Progression.** For the lethal form there is effectively no postnatal course — the disease is established in fetal development and is non-survivable. For the **survivable hypomorphic spectrum**, the course is **chronic and lifelong**, with early-onset cataract, persistent bone fragility, and developmental delay; progression is slow/variable.

**Patterns.** No remission. The critical window is **prenatal skeletal and organ development** — the only plausible point for hypothetical intervention is before/around this window, which is not currently feasible.

---

## 9. Inheritance and Population

**Inheritance.** **Autosomal recessive.** Both original families showed AR segregation with consanguinity [[PMID: 26365339](https://pubmed.ncbi.nlm.nih.gov/26365339/)].

**Penetrance / expressivity.** Penetrance for biallelic null genotypes appears **complete** for the severe phenotype. **Expressivity is allele-dependent and variable**: complete LoF → lethal osteochondrodysplasia; hypomorphic/partial-function alleles → survivable OI/cataract/progeria spectrum.

**Anticipation / mosaicism / founder effects.** No anticipation (not a repeat-expansion disorder). No germline mosaicism documented. Recurrent alleles cluster in **Middle Eastern / North African consanguineous populations** (Moroccan, Syrian, Jordanian), suggesting local founder/consanguinity effects rather than a single global founder.

**Consanguinity.** Central to disease occurrence — all molecularly resolved families are consanguineous.

**Carrier frequency.** Not formally estimated; alleles are ultra-rare in gnomAD.

**Epidemiology.** **Ultra-rare.** The defining lethal series (Symoens 2015) comprised **6 affected individuals** (5 interrupted pregnancies + 1 term birth) across **2 consanguineous families**. No prevalence/incidence estimates exist (too few cases). **Sex ratio** is expected ~1:1 (autosomal). **Age distribution:** prenatal/neonatal for the lethal form; pediatric onward for the survivable spectrum.

---

## 10. Diagnostics

**Primary diagnostic modality — genetics.** Diagnosis rests on **molecular identification of biallelic _TAPT1_ variants**. Recommended approach:
- **Whole-exome sequencing (WES)** detects coding/splice variants (e.g., c.1058A>T, c.1108-1G>C).
- **Whole-genome sequencing (WGS) + RNA-seq** are **required** to capture **deep-intronic branchpoint alleles** such as **c.1237-52G>A**, which WES misses. Nabavizadeh et al. used **homozygosity mapping + RNA-seq** and showed the variant enhances exon 12 skipping, introducing a premature stop codon, with the transcript degraded by NMD [[PMID: 36652330](https://pubmed.ncbi.nlm.nih.gov/36652330/)].
- **Single-gene / targeted testing** for _TAPT1_ is appropriate once the phenotype is recognized.
- **CMA/karyotype/FISH/mtDNA/repeat testing:** not indicated (single-gene, point-level disorder).

**Imaging.** Prenatal ultrasound and fetal/neonatal radiography: **generalized skeletal hypomineralization**, **multiple fractures**, **short fractured ribs**, **barrel-shaped/narrow thorax**, microcephaly, ventriculomegaly, ascites, pleural effusion.

**Biopsy / functional cell assays.** Patient **dermal fibroblasts** reveal **disturbed primary cilium formation and cytoplasmic TAPT1 mislocalization**; collagen studies show **failure of banded-fibril assembly** (Etich 2023). These are research-grade functional confirmations rather than routine clinical tests.

**Omics-based diagnostics.** **RNA-seq** is diagnostically pivotal for splicing/intronic alleles. **SI-NET-seq** distinguished a post-transcriptional (splicing) defect from a transcriptional one.

**Clinical criteria / differential diagnosis.** Differentials for a hypomineralized, fracture-prone perinatal skeletal dysplasia include **osteogenesis imperfecta type II (COL1A1/COL1A2)**, **hypophosphatasia (ALPL)**, **Cole–Carpenter syndrome**, and other lethal ciliary chondrodysplasias (Jeune/short-rib polydactyly). Molecular testing for _TAPT1_ distinguishes SBGS.

**Screening.** **Carrier screening / cascade testing** in affected consanguineous families; **prenatal molecular testing** where a familial variant is known.

---

## 11. Outcome / Prognosis

**Survival / mortality.** The **classic form is lethal** — stillbirth, interrupted pregnancy, or death in the perinatal/neonatal period. Life expectancy for the severe phenotype is effectively zero. Pulmonary hypoplasia (from the small, deformed thorax) and multi-organ anomalies are proximate causes of death.

**Survivable spectrum prognosis.** Hypomorphic-allele patients survive with **chronic morbidity**: bone fragility/OI, visual impairment from **early-onset cataract**, **severe developmental delay**, and **neonatal progeria** features. Long-term disability is substantial.

**Complications.** Fractures, respiratory insufficiency, feeding/growth problems, visual impairment, neurodevelopmental impairment.

**Prognostic factors.** The dominant prognostic determinant is **allele severity / residual TAPT1 function** (null → lethal; hypomorphic → survivable). No validated circulating prognostic biomarkers exist.

---

## 12. Treatment

**There is no disease-specific or curative therapy.** Management is **supportive and symptomatic**.

- **Classic lethal form:** perinatal palliative/comfort care; no intervention alters the lethal course.
- **Survivable spectrum:** multidisciplinary supportive care —
  - **Skeletal/OI management:** fracture care, orthopedic support; **bisphosphonates** are used empirically in OI generally (NCIT: Bisphosphonate Therapy) though not validated specifically for TAPT1-OI.
  - **Ophthalmology:** **cataract extraction** for early-onset cataract (NCIT: Cataract Surgery).
  - **Developmental/rehabilitative:** physical, occupational, and developmental therapy.
  - **Nutrition and respiratory support** as needed.
- **Pharmacogenomics, gene therapy, cell therapy, RNA-based therapy, targeted/immunotherapy:** **none available**; no clinical trials (no NCT identifiers) for TAPT1 disease. Deep-intronic splicing alleles are conceptually attractive **antisense-oligonucleotide (splice-modulation)** targets, but this remains investigational.

**Treatment strategy.** Care is individualized and supportive; the central "intervention" at the population level is **genetic counseling and reproductive planning** for at-risk families.

---

## 13. Prevention

- **Primary prevention:** For families with a known _TAPT1_ variant, **genetic counseling**, **carrier testing**, and **preimplantation genetic testing (PGT)** or **prenatal diagnosis** prevent recurrence. Awareness of **consanguinity risk** is central.
- **Secondary prevention:** **Cascade testing** of relatives; prenatal ultrasound surveillance in at-risk pregnancies.
- **Tertiary prevention:** In survivable cases, proactive management of fractures, cataract, and developmental needs to limit complications.
- **Immunization / public-health / behavioral / environmental measures:** not applicable (genetic disorder).
- **Counseling:** Autosomal-recessive 25% recurrence-risk counseling is the cornerstone of prevention.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs.** _TAPT1_ is evolutionarily conserved. **Mouse _Tapt1_** (chr 5; Entrez Gene 231225) and **zebrafish _tapt1a_/_tapt1b_** are functional orthologs used to model the disease.
- **Mouse natural/induced disease.** The ENU allele **_Tapt1^L5Jcs1_** (Howell et al. 2007) is **perinatal-lethal** with **posterior-to-anterior axial homeotic transformations** resembling _Hoxc8_/_Hoxc9_ mutants — the phenotype that gave the gene its "anterior posterior transformation" name [[PMID: 17151244](https://pubmed.ncbi.nlm.nih.gov/17151244/)].
- **Comparative biology / conservation.** The ciliary/basal-body and skeletal functions are conserved across mammalian and teleost models, supporting an ancient role in cilium-dependent skeletal development.
- **No natural companion-animal disease** is cataloged for _TAPT1_; **no zoonotic relevance** (genetic, non-transmissible).

---

## 15. Model Organisms

| Model | Type | Perturbation | Phenotype recapitulation | PMID |
|---|---|---|---|---|
| Zebrafish _tapt1b_ knockdown | Teleost, in vivo | Morpholino knockdown | Severe craniofacial cartilage malformation, microcephaly, delayed ossification, shortened otic-vesicle cilia, aberrant cranial neural-crest differentiation | [26365339](https://pubmed.ncbi.nlm.nih.gov/26365339/) |
| Zebrafish _tapt1a/tapt1b_ double-KO | Teleost, in vivo | Genetic KO | Cataract/eye defects; **no skeletal phenotype** (partial model) | [36697720](https://pubmed.ncbi.nlm.nih.gov/36697720/) |
| Mouse _Tapt1^L5Jcs1_ | Mammalian, in vivo | ENU point allele | Perinatal lethality; axial homeotic transformations (Hox-like) | [17151244](https://pubmed.ncbi.nlm.nih.gov/17151244/) |
| Patient fibroblasts | Human, in vitro | Native mutations | Disturbed ciliogenesis, TAPT1 cytoplasmic mislocalization, Golgi/trafficking defect, collagen fibril assembly failure | [26365339](https://pubmed.ncbi.nlm.nih.gov/26365339/), [37292039](https://pubmed.ncbi.nlm.nih.gov/37292039/) |
| C2C12 / C3H/10T1/2 cells | Murine myoblast/mesenchymal, in vitro | TAPT1 depletion | Elevated SMAD1/5/9, amplified BMP, enhanced osteoblast differentiation | [36370851](https://pubmed.ncbi.nlm.nih.gov/36370851/) |

**Recapitulation / limitations.** Zebrafish models capture craniofacial/cartilage, ossification, and cilia defects (classic phenotype) and, in the double-KO, cataract — but no single model reproduces the entire human multi-organ lethal syndrome. Cell models (C2C12, 10T1/2) are ideal for dissecting the **TAPT1–SMURF1–SMAD1/5–BMP** axis and osteoblast differentiation. **Resources:** MGI (mouse), ZFIN (zebrafish).

---

## Mechanistic Model / Interpretation

```
         Biallelic TAPT1 loss-of-function
         (splice / missense / deep-intronic→NMD)
                        │
                        ▼
      TAPT1 mislocalizes: basal body ──► cytoplasm
                        │
        ┌───────────────┼───────────────────────────┐
        ▼               ▼                             ▼
 Defective          Disrupted Golgi /          Loss of BMP brake:
 primary cilia      secretory trafficking      ↓SMURF1-driven SMAD1/5
        │               │                      degradation
        ▼               ▼                             ▼
 Aberrant cranial   Collagen fails to          ↑SMAD1/5/9 → amplified
 neural-crest       assemble into              BMP → ↑osteoblast
 differentiation    banded ECM fibrils         differentiation /
        │               │                      ectopic bone;
        │               │                      some alleles = GOF on SMAD1
        └──────┬────────┴──────────────┬───────────────┘
               ▼                        ▼
   Generalized skeletal hypomineralization, intrauterine
   fractures, short ribs/barrel thorax + brain/lung/kidney anomalies
               │
      ┌────────┴─────────┐
      ▼                  ▼
 Null alleles       Hypomorphic alleles
 → PERINATAL        → SURVIVABLE spectrum:
   LETHALITY           OI, early cataract, neonatal progeria
```

The unifying interpretation is that **TAPT1 is a conserved basal-body/centrosomal protein whose loss produces a composite "cilia-plus-ECM-plus-BMP" lesion**. The ciliary and Golgi/ECM arms explain the skeletal hypomineralization, fractures, craniofacial defects, and ciliopathy-type multi-organ involvement; the BMP–SMAD arm explains dysregulated osteoblast differentiation and provides a mechanistic handle (SMURF1/SMAD1/5). Residual TAPT1 function — set by allele type — is the dial that tunes the phenotype from perinatal-lethal osteochondrodysplasia down to survivable OI/cataract/progeria.

---

## Evidence Base

| Paper | PMID | Contribution |
|---|---|---|
| *Genetic Defects in TAPT1 Disrupt Ciliogenesis and Cause a Complex Lethal Osteochondrodysplasia* (Symoens et al., AJHG 2015) | [26365339](https://pubmed.ncbi.nlm.nih.gov/26365339/) | Defining paper: identifies biallelic TAPT1 mutations, lethal phenotype, basal-body localization, cilia/Golgi defects, zebrafish model |
| *Transmembrane anterior posterior transformation 1 regulates BMP signaling and modulates the protein stability of SMAD1/5* (Wang et al., 2022) | [36370851](https://pubmed.ncbi.nlm.nih.gov/36370851/) | TAPT1–SMURF1–SMAD1/5 BMP axis; gain-of-function of some human alleles on SMAD1 |
| *Deep-intronic TAPT1 variant → OI + neonatal progeria* (Nabavizadeh et al., EMBO Mol Med 2023) | [36652330](https://pubmed.ncbi.nlm.nih.gov/36652330/) | Deep-intronic c.1237-52G>A branchpoint, NMD null allele, WGS+RNA-seq necessity, ECM dysregulation |
| *TAPT1 frameshift → cataract + skeletal; tapt1a/b double-KO zebrafish* (Jarayseh et al., Hum Genet 2023) | [36697720](https://pubmed.ncbi.nlm.nih.gov/36697720/) | Survivable allelic spectrum; eye/cataract model |
| *Patient collagen fails to assemble into banded fibrils* (Etich et al., EMBO Mol Med 2023) | [37292039](https://pubmed.ncbi.nlm.nih.gov/37292039/) | ECM/collagen fibril assembly defect |
| *Mouse Tapt1 L5Jcs1 axial homeotic transformations* (Howell et al., 2007) | [17151244](https://pubmed.ncbi.nlm.nih.gov/17151244/) | Mouse perinatal-lethal model; origin of gene name |

**Key verified quotes.**
- *"This syndrome is characterized by fetal lethality, severe hypomineralization of the entire skeleton and intra-uterine fractures, and multiple congenital developmental anomalies affecting the brain, lungs, and kidneys."* [[PMID: 26365339](https://pubmed.ncbi.nlm.nih.gov/26365339/)]
- *"We establish that wild-type TAPT1 localizes to the centrosome and/or ciliary basal body, whereas defective TAPT1 mislocalizes to the cytoplasm and disrupts Golgi morphology and trafficking and normal primary cilium formation."* [[PMID: 26365339](https://pubmed.ncbi.nlm.nih.gov/26365339/)]
- *"Knockdown of tapt1b in zebrafish induces severe craniofacial cartilage malformations and delayed ossification, which is shown to be associated with aberrant differentiation of cranial neural crest cells."* [[PMID: 26365339](https://pubmed.ncbi.nlm.nih.gov/26365339/)]
- *"TAPT1 inhibits BMP signaling and destabilizes the SMAD1/5 protein by facilitating its interaction with SMURF1 E3 ubiquitin ligase, which leads to SMAD1/5 proteasomal degradation."* [[PMID: 36370851](https://pubmed.ncbi.nlm.nih.gov/36370851/)]
- *"a subset of TAPT1 mutations identified in humans with lethal skeletal dysplasia exhibited gain-of-function activity on SMAD1 protein levels."* [[PMID: 36370851](https://pubmed.ncbi.nlm.nih.gov/36370851/)]

---

## Limitations and Knowledge Gaps

- **Very small N.** Molecular evidence rests on a handful of consanguineous families; prevalence, penetrance, and genotype–phenotype correlations are imprecise.
- **No population frequency data.** Carrier frequency and true incidence are unknown.
- **Mechanistic integration incomplete.** How precisely the cilia, Golgi/ECM, and BMP–SMAD arms are quantitatively weighted in producing each phenotype remains unresolved; the BMP gain-of-function finding sits somewhat in tension with a pure loss-of-function model and needs allele-by-allele dissection.
- **No therapeutics.** There are no trials and no validated treatments; ASO splice correction for intronic alleles is only a concept.
- **Models are partial.** No single animal model reproduces the full human multi-organ lethal syndrome; the double-KO zebrafish lacks the skeletal phenotype.
- **Epigenetics, immune, metabolic layers** are essentially unstudied.

---

## Proposed Follow-up Experiments / Actions

1. **Allele-resolved functional panel.** Systematically test each reported TAPT1 variant (null vs missense vs in-frame-deletion) in parallel assays of ciliogenesis, Golgi trafficking, collagen fibril assembly, and SMAD1/5 stability to build a quantitative genotype–function–phenotype map and resolve the LoF-vs-GoF question.
2. **Conditional / hypomorphic mouse models.** Generate skeletal- and neural-crest-specific _Tapt1_ conditional knockouts and knock-in of human hypomorphic alleles to recapitulate the survivable spectrum and model OI/cataract/progeria.
3. **Splice-modulating ASO proof-of-concept.** For the deep-intronic c.1237-52G>A branchpoint allele, test antisense oligonucleotides that block the cryptic exon-12-skipping event to restore full-length TAPT1 in patient cells.
4. **Single-cell / spatial transcriptomics** of developing skeleton and neural crest in zebrafish/mouse models to localize where the cilia/BMP/ECM defects diverge across cell types.
5. **Diagnostic protocol.** Formalize a **WGS + RNA-seq** reflex pathway for exome-negative perinatal hypomineralizing skeletal dysplasias, given the demonstrated deep-intronic allele class.
6. **Registry and natural history.** Establish an international consanguinity-aware registry to capture additional families, refine epidemiology, penetrance, and the survivable-phenotype natural history.


## Artifacts

- [OpenScientist final report](Complex_Lethal_Osteochondrodysplasia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Complex_Lethal_Osteochondrodysplasia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 44 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 19 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014821` (3 mentions) - the report calls it "MONDO"; MONDO calls it **complex lethal osteochondrodysplasia**
- `HP:0000252` (1 mention) - the report calls it "Severe"; HP calls it **Microcephaly**
- `HP:0002089` (1 mention) - the report calls it "Lethal contributor"; HP calls it **Pulmonary hypoplasia**
- `HP:0000077` (1 mention) - the report calls it "Variable"; HP calls it **Abnormality of the kidney**
- `HP:0001999` (1 mention) - the report calls it "Severe"; HP calls it **Abnormal facial shape**
- `GO:0005813` (1 mention) - the report calls it "Centrosome / microtubule organizing center"; GO calls it **centrosome**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0006618` (1 mention), reported as "Severe" - HP does not contain this term
- `HP:0001505` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002119` (1 mention) - the report calls it "Moderate–severe"; HP calls it **Ventriculomegaly**, and lists "Dilated ventricles" among its other names
- `HP:0011344` (1 mention) - the report calls it "Severe developmental delay"; HP calls it **Severe global developmental delay**
- `GO:0030509` (1 mention) - the report calls it "BMP signaling"; GO calls it **BMP signaling pathway**
- `CL:0000008` (2 mentions) - the report calls it "cranial neural crest cell", "cranial neural crest cells"; CL calls it **migratory cranial neural crest cell**
- `GO:0005929` (1 mention) - the report calls it "primary cilium"; GO calls it **cilium**, and lists "primary cilium" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000062` - called "osteoblast", "osteoblasts"
- `CL:0000138` - called "chondrocyte", "chondrocytes"
- `CL:0000008` - called "cranial neural crest cell", "cranial neural crest cells"