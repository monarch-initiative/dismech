---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-02T23:51:58.107350'
end_time: '2026-11-03T00:13:34.974902'
duration_seconds: 1296.87
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Megalencephaly-polymicrogyria-polydactyly-hydrocephalus Syndrome 3
  mondo_id: MONDO:0014408
  category: Mendelian
  causal_genes: CCND2
  omim_id: OMIM:615938
  synonyms: megalencephaly-polymicrogyria-polydactyly-hydrocephalus syndrome type
    3; CCND2 megalencephaly-polymicrogyria-postaxial polydactyly-hydrocephalus syndrome;
    megalencephaly-polymicrogyria-postaxial polydactyly-hydrocephalus syndrome caused
    by mutation in CCND2
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
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 9
  quotes_valid: 9
  relevance_assessed: 12
  on_topic: 7
  validator_version: 0.4.0
term_validation:
  total_terms: 43
  verified: 41
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 7
  labels_variant: 1
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
  path: Megalencephaly-polymicrogyria-polydactyly-hydrocephalus_Syndrome_3-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Megalencephaly-polymicrogyria-polydactyly-hydrocephalus_Syndrome_3-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Megalencephaly-polymicrogyria-polydactyly-hydrocephalus Syndrome 3
- **MONDO ID:** MONDO:0014408 (if available)
- **Causal gene(s):** CCND2
- **OMIM:** OMIM:615938
- **Synonyms:** megalencephaly-polymicrogyria-polydactyly-hydrocephalus syndrome type 3; CCND2 megalencephaly-polymicrogyria-postaxial polydactyly-hydrocephalus syndrome; megalencephaly-polymicrogyria-postaxial polydactyly-hydrocephalus syndrome caused by mutation in CCND2
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Megalencephaly-polymicrogyria-polydactyly-hydrocephalus Syndrome 3** covering all of the
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

# Megalencephaly–Polymicrogyria–Polydactyly–Hydrocephalus Syndrome 3 (MPPH3)
### A Comprehensive Disease Characterization Report

**Causal gene: _CCND2_ (cyclin D2).** MPPH3 is the _CCND2_-caused subtype of the megalencephaly–polymicrogyria–polydactyly–hydrocephalus (MPPH) spectrum. It is caused by de novo, activating (protein-stabilizing) heterozygous variants in _CCND2_, which encodes cyclin D2, a G1-phase cell-cycle regulator that partners with CDK4/CDK6. Note: the disease name is a serial number ("...syndrome 3") that does not itself name the gene; per the provided identifiers (MONDO:0014408, OMIM 615938), this report concerns the **_CCND2_** form, distinct from MPPH1 (_PIK3R2_) and MPPH2 (_AKT3_).

> **Evidence-source note:** Because MPPH3 is an ultra-rare Mendelian disorder (<100 total MPPH cases of all genotypes reported), the evidence base is dominated by human case reports/case series and foundational functional genetics, supplemented by mouse models (knockout; in utero electroporation) and in vitro biochemistry. There are no large registries, GWAS, or omics cohorts specific to MPPH3.

---

## 1. Disease Information

**Overview.** MPPH3 is a rare congenital brain-overgrowth (megalencephaly) and malformation-of-cortical-development syndrome. The cardinal tetrad is **megalencephaly** (brain overgrowth), **polymicrogyria** (classically bilateral perisylvian), **postaxial polydactyly**, and **ventriculomegaly/hydrocephalus**. It is one end of a continuum of PI3K–AKT–mTOR "megalencephaly syndromes" that also includes the megalencephaly–capillary malformation syndrome (MCAP).

> "Megalencephaly-polymicrogyria-polydactyly-hydrocephalus syndrome (MPPH)... is characterized by progressive megalencephaly, cortical brain malformations, and distal limb anomalies." (PMID 38700464)

**Key identifiers.**
- **OMIM:** 615938 (MPPH3). The historical MPPH locus entry is OMIM 603387.
- **MONDO:** MONDO:0014408
- **Orphanet:** MPPH spectrum = ORPHA:83473 (megalencephaly–polymicrogyria–postaxial polydactyly–hydrocephalus syndrome)
- **Gene:** _CCND2_ — HGNC:1583; NCBI Gene 894; Ensembl ENSG00000118971; UniProt P30279 (G1/S-specific cyclin-D2); chromosome 12p13.32.
- **MeSH:** closest terms — Megalencephaly; Polymicrogyria; Malformations of Cortical Development; Hydrocephalus.
- **ICD-11:** LD90.0 (megalencephaly) / LA05 (congenital malformations of brain) are the best-fit umbrella codes; no MPPH3-specific code. **ICD-10:** Q04.3 / Q04.8 (other congenital brain malformations).

**Synonyms / alternative names:** megalencephaly-polymicrogyria-polydactyly-hydrocephalus syndrome type 3; CCND2 megalencephaly-polymicrogyria-postaxial polydactyly-hydrocephalus syndrome; MPPH caused by mutation in CCND2.

**Data source type:** Aggregated from individual-patient case reports/series and functional-genetics studies; not derived from EHR or disease-level omics aggregation.

---

## 2. Etiology

**Primary cause — genetic.** De novo heterozygous **gain-of-function** (protein-stabilizing) variants in _CCND2_.

> "individuals with MPPH lacking upstream PI3K-AKT pathway mutations carry de novo mutations in CCND2 (encoding cyclin D2) that are clustered around a residue that can be phosphorylated by glycogen synthase kinase 3β (GSK-3β). Mutant CCND2 was resistant to proteasomal degradation in vitro compared to wild-type CCND2." (Mirzaa et al. 2014, PMID 24705253)

**Genetic risk factors.** The disease-defining lesions are the de novo _CCND2_ variants themselves (see §4). There are no established common susceptibility loci or modifier genes; disease is monogenic/Mendelian with essentially complete penetrance for carriers of the stabilizing variants.

**Environmental risk factors.** None established. The causal mutations are de novo germline (or rarely postzygotic mosaic) events; no toxin, infection, maternal exposure, or lifestyle factor is implicated. Advanced parental age is a general (non-specific) correlate of de novo mutation rate but has not been specifically demonstrated for _CCND2_.

**Protective factors.** None identified. Conceptually, enhancing GSK-3β-dependent cyclin D2 degradation or inhibiting upstream PI3K–AKT signaling would be predicted to be "protective" (basis for targeted-therapy rationale), but no genetic protective allele is known.

**Gene–environment interactions.** Not applicable/none documented for this monogenic developmental disorder.

---

## 3. Phenotypes

All frequencies are qualitative/approximate given small case numbers. Onset is **prenatal/congenital** for structural features; neurological features (seizures, delay) manifest in infancy. Course is generally **stable-structural but with progressive megalencephaly and often progressive ventriculomegaly**; neurodevelopmental impairment is lifelong.

| Phenotype | Type | HPO term | Frequency | Onset / course | QoL impact |
|---|---|---|---|---|---|
| Megalencephaly / macrocephaly (HC > +2 to +3 SD) | physical sign / imaging | HP:0001355 Megalencephaly; HP:0000256 Macrocephaly | Near-universal (defining) | Congenital, progressive | High — mechanical, cosmetic, comorbidity driver |
| Polymicrogyria (bilateral perisylvian typical) | imaging / structural | HP:0002126 Polymicrogyria | Very frequent (defining) | Prenatal | High — drives epilepsy & delay |
| Ventriculomegaly / hydrocephalus | imaging / clinical | HP:0002119 Ventriculomegaly; HP:0000238 Hydrocephalus | Frequent (defining) | Pre/perinatal, often progressive | High — may need CSF diversion |
| Postaxial polydactyly | physical malformation | HP:0100259 Postaxial polydactyly | Variable; often absent in _CCND2_ cases | Congenital | Low–moderate (surgically correctable) |
| Developmental delay / intellectual disability | behavioral / cognitive | HP:0001263 Global developmental delay; HP:0001249 Intellectual disability | Near-universal | Infancy, lifelong | Severe |
| Epilepsy / seizures (incl. infantile spasms) | neurological sign | HP:0001250 Seizure; HP:0012469 Infantile spasms | Common | Infancy–childhood | Severe |
| Hypotonia | neurological sign | HP:0001252 Hypotonia | Common | Infancy | Moderate–severe |
| Cerebellar tonsillar ectopia / Chiari-like | imaging | HP:0002707 Cerebellar tonsillar herniation-related | Reported in MPPH spectrum | Congenital | Variable |
| Distinctive facies / prominent forehead (frontal bossing, hypertelorism, low nasal bridge) | physical | HP:0011220 Prominent forehead; HP:0002007 Frontal bossing; HP:0000316 Hypertelorism | Frequent | Congenital | Low |
| Thick corpus callosum | imaging / structural | HP:0007074 Thick corpus callosum | Recognized MPPH feature | Congenital | Variable |
| Severe intellectual disability / absent speech | cognitive / behavioral | HP:0010864 Severe intellectual disability; HP:0001344 Absent speech | Common | Childhood, lifelong | Severe |
| Syndactyly | physical malformation | HP:0001159 Syndactyly | Variable | Congenital | Low |
| Intraventricular hemorrhage (reported) | clinical | HP:0030746 Intracerebral hemorrhage | Reported (CCND2 p.Thr280Ile case) | Perinatal | High when present |

> **Authoritative HPO annotation set (Monarch/HPO for MONDO:0014408, 12 curated terms):** HP:0001355 Megalencephaly · HP:0000256 Macrocephaly · HP:0002126 Polymicrogyria · HP:0002119 Ventriculomegaly · HP:0000238 Hydrocephalus · HP:0007074 Thick corpus callosum · HP:0001263 Global developmental delay · HP:0010864 Severe intellectual disability · HP:0001344 Absent speech · HP:0001162 Postaxial hand polydactyly · HP:0001159 Syndactyly · HP:0011220 Prominent forehead. (Explicit frequency qualifiers not provided by the source.)

> A reported _CCND2_ (p.Thr280Ile) case had "ventriculomegaly, grade 3 IVH, bilateral polymicrogyria, and restricted diffusion in the caudate nuclei prenatally. No polydactyly was observed. The patient developed infantile spasms at age 5 months... By age 2 years, the patient continued to have significant developmental delays, including having poor tone and being nonverbal." (PMID 39395260) — illustrating that **polydactyly is variable/often absent** while neurodevelopmental and CSF phenotypes dominate.

**Quality of life.** Dominated by severe/profound neurodevelopmental disability, drug-resistant epilepsy in a subset, and complications of hydrocephalus; no disease-specific QoL instruments reported.

---

## 4. Genetic / Molecular Information

**Causal gene.** _CCND2_ (cyclin D2); HGNC:1583; NCBI Gene 894; UniProt P30279; chr12p13.32; OMIM gene 123833; disease OMIM 615938.

**Pathogenic variants.**
- **Location/clustering:** De novo variants cluster in the **terminal (last) exon** around the C-terminal **GSK-3β phosphodegron (Thr280, "T280")**. Examples: p.Thr280Ala, p.Thr280Ile (c.839C>T), and nearby residues; splice/truncating changes that remove the C-terminal degron also occur.
- **ClinVar-cataloged MPPH3 alleles (transcript NM_001759.4; accessed 2026-11):** c.838A>C **p.(Thr280Pro)** [Pathogenic/Likely pathogenic]; c.802G>T **p.(Gly268Ter)** [Likely pathogenic]; c.812C>A **p.(Ser271Ter)** [Likely pathogenic]; c.829C>T **p.(Gln277Ter)** [Pathogenic/Likely pathogenic], all annotated to MPPH3/CCND2-related disorder and located in the final exon (≈codons 268–284). **Key nuance:** C-terminal **nonsense/frameshift** variants escape nonsense-mediated decay and delete the phosphodegron, yielding the same stabilized, degradation-resistant protein as the Thr280 missense alleles (gain of function). In contrast, **proximal truncating** variants (e.g., c.416_419dup p.Leu141fs, c.643C>T p.Gln215Ter) are true loss-of-function and cause the reciprocal **microcephaly** phenotype (PMID 34087052). Of 94 P/LP CCND2 ClinVar records, most are large 12p copy-number changes unrelated to the single-gene MPPH3 mechanism.
  > "Megalencephaly-associated CCND2 variants are localized to the terminal exon and result in accumulation of degradation-resistant protein." (PMID 34087052)
- **Variant type/class:** Predominantly **missense** at/near Thr280, plus splice-site variants affecting the terminal exon; all converge on **loss of the degron → protein stabilization**.
- **Classification (ACMG/AMP):** Recurrent distal/Thr280 variants are classified **pathogenic/likely pathogenic** (de novo occurrence PS2, functional evidence PS3, clustering/absence from controls).
- **Allele frequency:** Absent from population databases (gnomAD) — de novo, not polymorphic (ACMG PM2).
- **Gene constraint (gnomAD, computational):** CCND2 is highly dosage-sensitive — **pLI = 0.999**, **LOEUF (oe_lof upper) = 0.39**, observed/expected LoF = 6/30.2, LoF Z = 3.74; **missense Z = 3.06** (obs/exp 235/373). This strong intolerance to both LoF and missense variation is the population-genetics correlate of the bidirectional "inverse phenotype" (LoF → microcephaly; degron-disrupting gain of function → megalencephaly/MPPH3).
- **Protein-level annotation (UniProt P30279, G1/S-specific cyclin-D2, 289 aa):** The pathogenic cluster maps to the intrinsically **disordered C-terminal region (begins ≈residue 264)** that carries the phosphodegron. UniProt independently annotates **Thr280 as a phosphothreonine** and the adjacent **Ser271 as a phosphoserine** modified residue — directly corroborating that the GSK-3β-targeted degron (Thr280) and the codon-268–284 variant hotspot sit within the degradation-control module. Loss of this phosphothreonine (missense or C-terminal truncation) is therefore the structural basis for the stabilized gain-of-function protein.
- **Germline vs somatic:** Typically **de novo germline**; postzygotic mosaicism occurs across the broader PI3K–AKT megalencephaly spectrum (relevant for recurrence risk and tissue-specific testing).
- **Functional consequence:** **Gain of function** via increased protein stability/abundance (not altered intrinsic enzymatic activity of the complex).

> Reciprocal (inverse) phenotype: **proximal loss-of-function** _CCND2_ variants cause **microcephaly, short stature, developmental delay** — "distinct classes of CCND2 variants are associated with reciprocal effects on human brain growth (microcephaly and megalencephaly due to possible loss or gain of protein function, respectively)." (PMID 34087052)

**Modifier genes.** None established; phenotypic variability (e.g., presence/absence of polydactyly, seizure severity) is unexplained and may reflect variant identity and stochastic/developmental factors.

**Epigenetic / chromosomal.** No recurrent methylation signature or chromosomal abnormality defines MPPH3; it is a single-nucleotide/small-variant disorder. Chromosomal microarray is typically normal (e.g., PMID 38700464 reported no CNVs).

---

## 5. Environmental Information

Not applicable. MPPH3 is a monogenic developmental disorder caused by de novo mutation. No environmental toxin, radiation, lifestyle, dietary, or infectious trigger is implicated or expected.

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. A **de novo _CCND2_ variant** disrupts the C-terminal GSK-3β phosphodegron (Thr280) → **leads to** loss of the phosphorylation site that normally marks cyclin D2 for destruction.
2. Loss of Thr280 phosphorylation → **results in** failure of SCF/proteasome-mediated degradation → **cyclin D2 protein accumulates** (degradation-resistant). (Demonstrated in vitro — PMID 24705253.)
3. Elevated cyclin D2 → **leads to** sustained assembly of **cyclin D2–CDK4/CDK6** complexes and prolonged kinase activity (overriding INK4/CIP-KIP inhibitors). (Biochemistry — PMID 16357141.)
4. Active CDK4/6 → **results in** hyperphosphorylation/inactivation of **retinoblastoma protein (pRb)** → **release of E2F** transcription factors → G1→S transition. (Inferred for neural progenitors from canonical D-cyclin biology — PMIDs 15684604, 16357141.)
5. In neural progenitors (radial glia), persistent G1/S drive → **leads to** **more cells remaining in cycle and fewer exiting to differentiate** (demonstrated by in utero electroporation of mutant CCND2 — PMID 24705253).
6. Excess/prolonged progenitor proliferation → **results in** **brain overgrowth (megalencephaly)** and **disordered cortical architecture/lamination → polymicrogyria**; enlarged brain + altered CSF dynamics → **ventriculomegaly/hydrocephalus** (step partly inferred).
7. Convergent branch: **Upstream PI3K–AKT–mTOR activation** (PIK3CA/MCAP, PIK3R2/MPPH1, AKT3/MPPH2) → inhibits GSK-3β → **same cyclin D2 stabilization** → phenocopy.
   > "cells from individuals with PIK3CA, PIK3R2 or AKT3 mutations showed similar CCND2 accumulation... cyclin D2 stabilization, caused by CCND2 mutation or PI3K-AKT activation, is a unifying mechanism in PI3K-AKT-related megalencephaly syndromes." (PMID 24705253)
8. Limb branch: PI3K–AKT signaling in limb buds (and, by inference, cyclin D2 dosage) contributes to **postaxial polydactyly** — "Our data highlight the central role of PI3K-AKT signaling in vascular, limb and brain development." (PMID 22729224)

**Molecular pathways:** PI3K–AKT–mTOR (KEGG hsa04151); Cell cycle (KEGG hsa04110); Rb–E2F/G1-S. **Cellular processes:** positive regulation of cell-cycle progression, reduced cell-cycle exit/differentiation of neural progenitors, altered neuronal migration (abnormal migration noted clinically, PMID 38700464). **Protein dysfunction:** gain-of-function by stabilization/accumulation, not misfolding. **Metabolic link:** PI3K–AKT activation can cause **hypoketotic hypoinsulinaemic hypoglycaemia** in the broader pathway — relevant comorbidity to monitor (PMIDs 29883676, 28566443). **Immune involvement:** none. **Upstream vs downstream:** CCND2 is the **downstream effector/convergence node**; PIK3CA/PIK3R2/AKT3 are upstream.

**Suggested ontology terms (CCND2 GO Biological Process annotations, verified via MyGene.info/GO):** GO:0000082 (G1/S transition of mitotic cell cycle); GO:1900087 (positive regulation of G1/S transition of mitotic cell cycle); GO:2000045 (regulation of G1/S transition of mitotic cell cycle); GO:1901992 (positive regulation of mitotic cell cycle phase transition); GO:0008284 (positive regulation of cell population proliferation); **GO:0043066 (negative regulation of apoptotic process)** — relevant because reduced progenitor apoptosis compounds the overgrowth. Additional relevant: GO:0045737 (positive regulation of CDK activity); GO:0021846 (cell proliferation in forebrain). **Cell types (CL):** CL:0000031 neuroblast, CL:0000681 radial glial cell, CL:0000127 astrocyte, CL:0000120 cerebellar granule cell.

---

## 7. Anatomical Structures Affected

**Organ level (primary):** Brain — cerebral cortex (perisylvian/opercular regions), white matter, ventricular system; cerebellum (granule/stellate neurons; tonsillar ectopia). **Body systems:** central nervous system (primary); musculoskeletal (limb — polydactyly); occasionally ocular (e.g., persistent hyperplastic primary vitreous reported in the spectrum, PMID 38008077).
**Secondary involvement:** hydrocephalus-related raised intracranial pressure; epilepsy-related networks.
**Tissue/cell level:** neuroepithelial/neural progenitor (radial glia) proliferative zones (ventricular/subventricular zones); cortical neurons; cerebellar granule and interneurons.
**Subcellular (GO Cellular Component / UniProt P30279):** nucleus (GO:0005634, where cyclin D2–CDK acts on Rb/E2F); cytoplasm; nucleus membrane (UniProt-annotated localizations for G1/S-specific cyclin-D2); cyclin-dependent protein kinase holoenzyme complex (GO:0000307); cytoplasm also hosts the degradation machinery.
**Localization / lateralization:** Brain involvement is **bilateral**; polymicrogyria is characteristically **bilateral perisylvian/symmetric**. **UBERON:** UBERON:0000955 brain; UBERON:0000956 cerebral cortex; UBERON:0002037 cerebellum; UBERON:0002285 lateral ventricle; UBERON:0002544 digit (limb).

---

## 8. Temporal Development

- **Onset:** Congenital/prenatal — megalencephaly, polymicrogyria, ventriculomegaly, and polydactyly are detectable in utero (prenatal ultrasound/MRI diagnoses reported, PMIDs 38008077, 39395260). **Pattern:** chronic/developmental (insidious structural, then infantile neurological onset).
- **Progression:** Megalencephaly is **progressive** ("progressive megalencephaly," PMID 38700464); ventriculomegaly may progress to hydrocephalus requiring intervention; cortical malformation is static once formed but its functional consequences (epilepsy, delay) evolve.
- **Course:** Chronic, lifelong; no spontaneous remission of structural disease. Seizures may be controllable (e.g., spasms resolving with topiramate in one case, PMID 39395260) or drug-resistant.
- **Critical period:** Fetal corticogenesis (progenitor proliferation/neuronal migration) is the window in which the malformation is established; this is the mechanistic rationale/limitation for any disease-modifying therapy (post-natal therapy cannot reverse already-formed cortex).

---

## 9. Inheritance and Population

- **Epidemiology:** Ultra-rare; MPPH (all genotypes) has **fewer than 100 reported cases** (PMID 39395260); MPPH3 (_CCND2_) is a subset. No reliable prevalence/incidence figures exist (Orphanet "<1/1,000,000").
- **Inheritance:** **Autosomal dominant**, essentially always arising **de novo** (sporadic). Recurrence risk to siblings is low but non-zero due to possible **gonadal/germline mosaicism**.
- **Penetrance / expressivity:** Penetrance for the stabilizing variants is effectively **complete**; **expressivity is variable** (e.g., polydactyly present in some, absent in others; seizure severity varies).
- **Anticipation:** Not applicable (not a repeat-expansion disorder).
- **Founder effects / carrier frequency / consanguinity:** Not applicable — de novo dominant; no founder alleles, no carrier state, consanguinity not a factor.
- **Demographics:** No ethnic predilection reported; both sexes affected (no strong sex bias documented). Age distribution: pediatric (diagnosed prenatally to early childhood).

---

## 10. Diagnostics

**Imaging (central to diagnosis).** Brain **MRI** is the key test: megalencephaly, **bilateral perisylvian polymicrogyria**, ventriculomegaly/hydrocephalus, ± cerebellar tonsillar ectopia, ± abnormal neuronal migration/white-matter changes. Prenatal **ultrasound/fetal MRI** can detect megalencephaly, abnormal gyration, and ventriculomegaly (PMIDs 38008077, 39395260). **EEG** for seizures/infantile spasms.

**Genetic testing (confirmatory).**
- **Exome/genome sequencing (WES/WGS)** or **targeted NGS gene panels** covering the PI3K–AKT–mTOR megalencephaly genes (_CCND2_, _AKT3_, _PIK3R2_, _PIK3CA_) — the recommended first-line molecular approach.
- **Single-gene / targeted _CCND2_ sequencing** of the terminal exon/Thr280 region confirms MPPH3.
- **Deep/mosaic-aware sequencing of affected tissue** may be needed when mosaicism is suspected (low variant allele fraction in blood) — "Sanger sequencing is ineffective for the detection of a causal variant because of the mosaic nature of these variants, whereas targeted next-generation sequencing technology offers a deeper sequencing coverage and allows the detection of low-level mosaicism." (PMID 28502730)
- **Chromosomal microarray/karyotype:** typically normal; used to exclude CNVs (PMID 38700464).
- Mitochondrial/repeat-expansion testing: not indicated.

**Biomarkers / labs:** No specific circulating biomarker. **Monitor blood glucose** given the pathway's association with hypoinsulinaemic, hypoketotic **hypoglycaemia** (PMIDs 29883676, 28566443). Metabolic screening (tandem MS) is typically normal (PMID 38700464).

**Clinical criteria / differential diagnosis.** Diagnosis = megalencephaly + cortical malformation (polymicrogyria) ± polydactyly ± hydrocephalus, confirmed by a pathogenic PI3K–AKT–pathway variant. **Differentials:** MCAP (has capillary malformation/somatic overgrowth, usually _PIK3CA_ mosaic); MPPH1 (_PIK3R2_), MPPH2 (_AKT3_); other megalencephaly/overgrowth syndromes (e.g., PTEN, Sotos, hemimegalencephaly); isolated polymicrogyria. Distinguishing feature of MPPH vs MCAP: **absence of capillary/cutaneous vascular malformation and segmental somatic overgrowth** in MPPH.

**Screening:** No population newborn screening. Cascade testing of parents is generally uninformative (de novo) but relevant for recurrence counseling (mosaicism).

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No formal survival statistics; severe cases with marked hydrocephalus, drug-resistant epilepsy, or complications carry risk, but many survive into childhood/adulthood with disability. A rare report documents **medulloblastoma** arising in an MPPH patient (PMID 33634562), consistent with cyclin D2/PI3K-pathway oncogenic potential — a possible tumor-surveillance consideration.
- **Morbidity/function:** Dominated by **moderate-to-severe/profound intellectual disability and motor impairment**, epilepsy, and hydrocephalus-related morbidity; many patients are nonverbal with hypotonia (PMID 39395260).
- **Disease course:** Chronic, lifelong; complications include progressive hydrocephalus (may need shunt/ETV), refractory seizures, and feeding/airway issues in severe cases.
- **Prognostic factors:** Severity of megalencephaly/cortical malformation, hydrocephalus requiring diversion, epilepsy control, and presence of complications (e.g., IVH). No validated molecular prognostic biomarker.

---

## 12. Treatment

No disease-specific curative therapy exists; management is **multidisciplinary and largely supportive**.

- **Neurosurgical:** CSF diversion (**ventriculoperitoneal shunt** or **endoscopic third ventriculostomy**) for hydrocephalus; epilepsy surgery in selected drug-resistant cases.
- **Antiseizure medication:** Standard AEDs; infantile spasms treated per protocol. In one _CCND2_ case, high-dose prednisone failed but **topiramate** achieved spasm control (PMID 39395260). (NCIT examples: C66883 Topiramate; C716 Prednisone.)
- **Rehabilitation/supportive:** Physical, occupational, and speech therapy; developmental/educational support; orthopedic correction of polydactyly.
- **Metabolic monitoring:** Surveillance for **hypoglycaemia** (pathway-associated); treat as indicated (PMIDs 29883676, 28566443).
- **Targeted/experimental (pathway-directed, mostly investigational for brain disease):** Because MPPH converges on PI3K–AKT–mTOR/cyclin D2, pathway inhibitors are mechanistically rational:
  - **mTOR inhibitors (sirolimus/rapamycin)** — partial efficacy in overgrowth phenotypes but durable responses uncommon and recurrence after discontinuation observed (PMID 42747160). NCIT C1212 Sirolimus.
  - **PI3Kα inhibitors (alpelisib; next-gen mutant-selective zovegalisib/RLY-2608)** — established in PIK3CA-related overgrowth spectrum (PMIDs 42747160, 42875408); not established for fixed CNS malformation. NCIT C123846 Alpelisib.
  - **CDK4/6 inhibitors** — a conceptually attractive node directly downstream of cyclin D2, but not clinically tested in MPPH.
  - **Key limitation:** the cortical malformation is established prenatally, so postnatal pathway inhibition is unlikely to reverse structural disease; benefit (if any) would target overgrowth/progression, epilepsy, or tumor risk. Gene/RNA therapies: none.

---

## 13. Prevention

- **Primary prevention:** Not possible (de novo mutation). **Genetic counseling** emphasizes low but non-zero recurrence risk (germline mosaicism).
- **Secondary prevention / prenatal:** **Prenatal ultrasound/fetal MRI** can detect megalencephaly, abnormal gyration, ventriculomegaly, enabling early diagnosis and counseling (PMIDs 38008077, 39395260). **Prenatal/preimplantation genetic testing** is feasible if a familial variant is known (e.g., proven parental mosaicism).
- **Tertiary prevention:** Prevent complications — hydrocephalus management, seizure control, glucose monitoring, developmental intervention.
- **Public health / immunization / behavioral:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs (HomoloGene, verified):** _CCND2_ is broadly conserved. Ortholog NCBI Gene IDs — human 894 (taxon 9606); mouse _Ccnd2_ **12444** (10090); rat **64033** (10116); zebrafish **799608** (_Danio rerio_, 7955); chicken 374047 (9031); dog 611782 (9615); cow 615414 (9913); chimpanzee 747123 (9598); _Xenopus tropicalis_ 100038071 (8364); _Drosophila_ ortholog (CycD) 32551 (7227). Conservation from invertebrates to mammals underscores the ancient role of D-cyclins in cell-cycle control.
- **Natural disease in animals:** No recognized naturally occurring _CCND2_ megalencephaly syndrome in companion animals/wildlife (not in OMIA as a spontaneous disease). MPPH3 is studied via engineered models, not natural animal disease.
- **Comparative biology:** Cyclin D2's role in neural (especially cerebellar granule-cell) proliferation is evolutionarily conserved, supporting cross-species mechanistic relevance.
- **Zoonotic potential:** None (non-infectious genetic disorder).

---

## 15. Model Organisms

- **Mouse — _Ccnd2_ knockout (loss of function):** "The loss of this cyclin primarily affected two neuronal populations: granule cell number was reduced and stellate interneurons were nearly absent" with reduced cerebellar neurogenesis and increased apoptosis (Huard et al. 1999, PMID 10101126). This models the **inverse (hypoplasia/microcephaly)** pole, validating cyclin D2 as a dose-dependent brain-growth regulator. Thyroid-hormone studies confirm cyclin D2 drives cerebellar EGL neuroblast proliferation/anti-apoptosis (PMID 12591240).
- **In utero electroporation of mutant (stabilized) CCND2 in embryonic mouse cortex:** recapitulates the **gain-of-function** mechanism — "produced more proliferating transfected progenitors and a smaller fraction of progenitors exiting the cell cycle compared to cells electroporated with wild-type CCND2" (PMID 24705253). This is the most direct in vivo model of the MPPH3 mechanism.
- **Activated-AKT3 mouse:** shows elevated brain cyclin D2, linking upstream pathway activation to the effector (PMID 24705253).
- **Model types available:** knockout (loss-of-function), in utero electroporation/overexpression (gain-of-function), and transgenic pathway-activation models. **Recapitulation:** overexpression/electroporation models reproduce excess progenitor proliferation; full syndromic replication (polydactyly, hydrocephalus) is incomplete. **Limitations:** no single model reproduces the entire human tetrad; timing/dosage-sensitive.
- **In vitro:** patient-derived cells show cyclin D2 accumulation; biochemical assays confirm degradation resistance (PMID 24705253).
- **Resources:** MGI (mouse _Ccnd2_), IMPC/KOMP for knockout lines.

---

## Supported vs Refuted Hypotheses

**Supported:**
1. MPPH3 is caused by de novo _CCND2_ gain-of-function variants that stabilize cyclin D2 against proteasomal degradation (PMID 24705253).
2. The mechanism is excess/prolonged neural-progenitor proliferation via cyclin D2–CDK4/6–Rb–E2F, converging with upstream PI3K–AKT–mTOR activation (PMIDs 24705253, 16357141, 22729224).
3. Cyclin D2 dosage controls brain size bidirectionally — loss → microcephaly, gain → megalencephaly (PMIDs 10101126, 34087052).

**Refuted / ruled out:**
- Environmental, infectious, or metabolic primary causation (no evidence; disease is monogenic de novo).
- An intrinsic enzymatic gain (the defect is protein **abundance/stability**, not altered catalytic activity).

## Limitations
- Evidence rests on rare case reports and a small number of functional studies; no large cohorts, registries, or omics datasets specific to MPPH3.
- Genotype–phenotype correlations (e.g., variable polydactyly) remain unexplained.
- No clinical trial data for targeted therapy in MPPH3 specifically; pathway-inhibitor evidence is extrapolated from PIK3CA-related overgrowth.

## Future Directions
- Prospective natural-history/registry studies of _CCND2_-specific MPPH3.
- Trials of CDK4/6 or PI3K–AKT–mTOR inhibitors for progressive/overgrowth or epilepsy endpoints, defining therapeutic windows.
- Tumor-risk surveillance guidance given isolated medulloblastoma report (PMID 33634562).

---

### Key references (PMID)
24705253 (Mirzaa 2014, Nat Genet — foundational CCND2/MPPH3); 22729224 (Rivière 2012 — AKT3/PIK3R2/PIK3CA spectrum); 34087052 (Pirozzi 2021 — inverse phenotype); 39395260 (Mok 2024 — CCND2 p.Thr280Ile, infantile spasms); 38700464 (Zhao 2024 — case); 38008077 (Su 2024 — prenatal dx); 29883676 & 28566443 (pathway hypoglycaemia); 28502730 (Akgumus 2017 — mosaic PI3K overgrowth testing); 10101126 (Huard 1999 — Ccnd2-KO cerebellum); 12591240 (cyclin D2 cerebellar target); 16357141 & 15684604 & 11360190 (cyclin D2–CDK–Rb biochemistry); 42747160 & 42875408 (targeted therapy); 33634562 (medulloblastoma in MPPH).


## Artifacts

- [OpenScientist final report](Megalencephaly-polymicrogyria-polydactyly-hydrocephalus_Syndrome_3-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Megalencephaly-polymicrogyria-polydactyly-hydrocephalus_Syndrome_3-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 9 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 12 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 8 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0045737` (1 mention) - the report calls it "positive regulation of CDK activity"; GO calls it **positive regulation of cyclin-dependent protein serine/threonine kinase activity**, and lists "positive regulation of CDK activity" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

41 of 43 terms resolved to a current term; the rest could not be looked up either way.