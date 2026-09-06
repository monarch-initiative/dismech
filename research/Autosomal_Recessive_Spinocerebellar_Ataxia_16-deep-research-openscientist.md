---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-05T22:41:12.140780'
end_time: '2026-09-05T22:59:01.864918'
duration_seconds: 1069.73
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autosomal Recessive Spinocerebellar Ataxia 16
  mondo_id: MONDO:0014339
  category: Mendelian
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
citation_count: 20
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 27
  quotes_valid: 25
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:39117117
  - PMID:24312598
  relevance_assessed: 21
  on_topic: 18
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 33
  verified: 30
  not_found: 1
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.031
  labels_checked: 19
  labels_matching: 4
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0014339
    reported_labels:
    - MONDO
    ontology_label: autosomal recessive spinocerebellar ataxia 16
  - term_id: UBERON:0002037
    reported_labels:
    - cerebellum
    - Primary organ:** brain, specifically the **cerebellum
    ontology_label: cerebellum
  - term_id: NCIT:C15367
    reported_labels:
    - Physical Therapy
    ontology_label: Health Risk Assessment
  - term_id: NCIT:C15451
    reported_labels:
    - Speech Therapy
    ontology_label: Prior Anthracycline Therapy
  - term_id: NCIT:C15329
    reported_labels:
    - Occupational Therapy
    ontology_label: Surgical Procedure
  - term_id: NCIT:C376
    reported_labels:
    - Baclofen
    ontology_label: Cisplatin
  - term_id: NCIT:C15667
    reported_labels:
    - Hormone Replacement Therapy
    ontology_label: Sentinel Lymph Node Biopsy
  labels_variant: 8
  unresolved_terms:
  - HP:0000990
  obsolete_terms:
  - term_id: GO:0061077
    ontology_label: obsolete chaperone-mediated protein folding
    replaced_by: GO:0006457
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
  path: Autosomal_Recessive_Spinocerebellar_Ataxia_16-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Autosomal_Recessive_Spinocerebellar_Ataxia_16-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Spinocerebellar Ataxia 16
- **MONDO ID:** MONDO:0014339 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Spinocerebellar Ataxia 16** covering all of the
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

# Autosomal Recessive Spinocerebellar Ataxia 16 (SCAR16): Comprehensive Disease Characterization

**Disease:** Autosomal Recessive Spinocerebellar Ataxia 16 (SCAR16)
**MONDO ID:** MONDO:0014339 · **OMIM:** #615768 · **Orphanet:** ORPHA:363432
**Category:** Mendelian (autosomal recessive)
**Causal gene:** *STUB1* (16p13.3), encoding CHIP (C-terminus of HSC70-Interacting Protein)

---

## Summary

Autosomal Recessive Spinocerebellar Ataxia 16 (SCAR16) is an ultra-rare, progressive, autosomal recessive multisystem neurodegenerative disorder caused by **biallelic loss-of-function mutations in *STUB1*** on chromosome 16p13.3. *STUB1* encodes **CHIP**, a dual-function protein that acts both as an **E3 ubiquitin ligase** and as a **co-chaperone of HSP70/HSP90**, placing it at the center of the cell's protein quality-control (proteostasis) machinery. Disease was originally described in a small number of kindreds (~16 as of 2020) and remains an uncommon cause of hereditary ataxia, accounting for only ~0.4% (2/512) of one Taiwanese cerebellar-ataxia cohort ([PMID: 32342324](https://pubmed.ncbi.nlm.nih.gov/32342324/); [PMID: 32367277](https://pubmed.ncbi.nlm.nih.gov/32367277/)).

Clinically, SCAR16 presents as **early-onset spastic cerebellar ataxia** with striking cerebellar atrophy on MRI, accompanied by a broad and variable spectrum of features: cognitive dysfunction/dementia, spasticity and hyperreflexia, hyperkinetic movement disorders (chorea, dystonia, myoclonus), epilepsy, peripheral neuropathy, autonomic dysfunction, and hypogonadotropic hypogonadism (the combination of ataxia plus hypogonadism defining **Gordon Holmes syndrome**). The neuropathological hallmark is **selective, massive loss of cerebellar Purkinje cells**, predominantly in the vermis, with relative sparing of pons, hippocampus, and cerebral cortex ([PMID: 32713943](https://pubmed.ncbi.nlm.nih.gov/32713943/)).

Mechanistically, SCAR16 mutations **thermodynamically destabilize and misfold CHIP**, disrupting the U-box domain and abolishing ubiquitin-ligase activity. This impairs clearance of CHIP substrates and clients (e.g., NR2A, PDE9A, HSC70, aggregation-prone proteins such as tau and polyglutamine ataxin-3), dysregulates PINK1/Parkin-mediated mitophagy and cGMP/cAMP signaling, and culminates in Purkinje-neuron apoptosis. The same gene causes autosomal *dominant* SCA48 through heterozygous mutations, and digenic *STUB1*/*TBP* interactions modify penetrance — establishing a **continuous clinical and genetic spectrum**. There is currently **no disease-modifying therapy**; management is entirely supportive, though preclinical work nominates thermostabilizing pharmacological chaperones, PDE9A inhibition (Bay 73-6691), and viral CHIP re-expression as protective strategies.

---

## Section 1 — Disease Information

**Overview.** SCAR16 is a Mendelian, autosomal recessive spinocerebellar ataxia caused by biallelic *STUB1* mutations. It is a progressive multisystem neurodegeneration centered on the cerebellum but extending to pyramidal, extrapyramidal, cognitive, peripheral-nervous, endocrine, and autonomic systems. As one source summarizes, "*SCAR16 is characterized by early onset spastic ataxia and a wide disease spectrum, including cognitive dysfunction, hyperkinetic disorders, epilepsy, peripheral neuropathy, and hypogonadism*" ([PMID: 32342324](https://pubmed.ncbi.nlm.nih.gov/32342324/)).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM | #615768 |
| MONDO | MONDO:0014339 |
| Orphanet | ORPHA:363432 |
| Gene (HGNC) | *STUB1* |
| Protein (UniProt) | CHIP / Q9UNE7 |
| Cytoband | 16p13.3 |

**Synonyms / alternative names:**
- Spinocerebellar ataxia, autosomal recessive 16
- SCAR16
- CHIP-related ataxia / STUB1-related ataxia
- Gordon Holmes syndrome (when ataxia co-occurs with hypogonadotropic hypogonadism)
- STUB1-associated multisystemic ataxia (recessive form)

**Data source type.** Information is derived overwhelmingly from **aggregated disease-level resources** — case reports, small kindred series, and molecular/functional studies — rather than large EHR datasets, consistent with the disease's rarity. The original gene discovery combined linkage mapping with whole-exome sequencing in individual pedigrees ([PMID: 24312598](https://pubmed.ncbi.nlm.nih.gov/24312598/)).

---

## Section 2 — Etiology

**Primary cause (genetic).** SCAR16 is a monogenic disorder caused by **biallelic (homozygous or compound heterozygous) loss-of-function mutations in *STUB1***. "*Biallelic mutations in STUB1, which encodes the E3 ubiquitin ligase CHIP, were originally described in association with SCAR16, a rare autosomal recessive spinocerebellar ataxia, so far reported in 16 kindreds*" ([PMID: 32342324](https://pubmed.ncbi.nlm.nih.gov/32342324/)). A representative patient carried "*compound heterozygous mutations (c.355C>T, c.880A>T) in STUB1*" ([PMID: 29679845](https://pubmed.ncbi.nlm.nih.gov/29679845/)).

**Genetic risk factors.** The causal variants are the *STUB1* mutations themselves. Because the disorder is recessive, **carriers (heterozygotes) are typically unaffected** for SCAR16, though heterozygous *STUB1* variants can cause dominant SCA48. **Modifier genes** shape penetrance and expressivity: "second hits" in **AFG3L2, PRKCG, and TBP** were detected in three families, suggesting synergistic effects ([PMID: 32713943](https://pubmed.ncbi.nlm.nih.gov/32713943/)), and a **digenic *STUB1*/*TBP*** interaction modulates penetrance across the STUB1 disease spectrum ([PMID: 34906452](https://pubmed.ncbi.nlm.nih.gov/34906452/)).

**Environmental risk factors.** None are established. As a Mendelian disorder, disease occurrence is determined by genotype. **Consanguinity** increases the likelihood of homozygous genotypes and thus disease in affected families.

**Protective factors.** No environmental or dietary protective factors are documented. On the genetic side, functional studies imply that **anything restoring CHIP thermostability or activity would be protective** — the biochemical rationale for pharmacological-chaperone therapy ([PMID: 29317501](https://pubmed.ncbi.nlm.nih.gov/29317501/)).

**Gene–environment interactions.** No specific gene–environment interactions are established. The relevant interactions in SCAR16 are **gene–gene (digenic/modifier)** interactions (*STUB1* with *TBP*, *AFG3L2*, *PRKCG*), plus a modifying effect of **sex** (female predominance; see Section 9).

---

## Section 3 — Phenotypes

SCAR16 is a multisystem phenotype with a cerebellar core. The table below maps the principal features to suggested HPO terms with approximate frequencies and onset.

| Phenotype | HPO term | Type | Approx. frequency | Onset / course |
|---|---|---|---|---|
| Progressive cerebellar / gait ataxia | HP:0001251 (ataxia), HP:0002066 (gait ataxia) | Clinical sign | ~100% (defining) | Childhood–adult; progressive |
| Cerebellar atrophy on MRI | HP:0001272 | Imaging/lab | Very frequent | Early; progressive |
| Dysarthria | HP:0001260 | Clinical sign | Frequent | Progressive |
| Cognitive impairment / dementia (frontal syndrome) | HP:0100543 | Symptom | **~54% of STUB1 carriers** | Variable; progressive |
| Lower-limb spasticity / hyperreflexia | HP:0001257, HP:0001347 | Clinical sign | Frequent | Progressive |
| Hypogonadotropic hypogonadism (Gordon Holmes) | HP:0000044 | Lab/clinical | Subset | Variable |
| Epilepsy / seizures | HP:0001250 | Clinical sign | Subset | Variable |
| Peripheral neuropathy | HP:0009830 | Clinical sign | Subset | Progressive |
| Hyperkinetic movement disorders (chorea/dystonia/myoclonus) | HP:0002072, HP:0001332, HP:0001336 | Clinical sign | Subset | Variable |
| Autonomic dysfunction | HP:0000990-related | Clinical sign | Subset | Variable |

The 54% frequency for cognitive impairment is quantified directly: "*Cognitive impairment, predominantly frontal syndrome, was observed in 54% of STUB1 variant carriers*" ([PMID: 32713943](https://pubmed.ncbi.nlm.nih.gov/32713943/)). The multisystem severity is illustrated by a series in which "*All three subjects presented with a severe multisystemic phenotype including severe dementia, spastic tetraparesis, epilepsy, and autonomic dysfunction in addition to cerebellar ataxia, plus hypogonadism in one index patient*" ([PMID: 28193273](https://pubmed.ncbi.nlm.nih.gov/28193273/)).

**Severity and progression.** Severity is **variable** and strongly variant-dependent (see Section 4); the course is **chronic and progressive**. Notably, some patients present with **isolated cerebellar ataxia**, so absence of systemic features does not exclude the diagnosis ([PMID: 32367277](https://pubmed.ncbi.nlm.nih.gov/32367277/)).

**Quality-of-life impact.** No formal EQ-5D/SF-36 studies specific to SCAR16 were identified. By clinical inference, progressive gait ataxia, dysarthria, spasticity, cognitive decline, and (in some) epilepsy produce substantial and cumulative disability affecting mobility, communication, independence, and daily functioning.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *STUB1* (STIP1 Homology and U-box containing protein 1), 16p13.3, encoding **CHIP** (Q9UNE7). CHIP is a 303-amino-acid protein with three functional domains: an N-terminal **TPR (tetratricopeptide repeat)** domain that binds HSP70/HSP90, a central **coiled-coil** dimerization domain, and a C-terminal **U-box** domain conferring E3 ubiquitin-ligase activity.

**Pathogenic variants.** SCAR16 mutations span **all three CHIP domains** (TPR, coiled-coil, U-box) and include missense, nonsense/truncating, and start-loss variants. Representative alleles: **c.737C>T (p.Thr246Met)** — the founding homozygous mutation causing Gordon Holmes syndrome ([PMID: 24113144](https://pubmed.ncbi.nlm.nih.gov/24113144/)); **c.493C>T** identified by linkage + WES ([PMID: 24312598](https://pubmed.ncbi.nlm.nih.gov/24312598/)); compound heterozygous **c.355C>T + c.880A>T** ([PMID: 29679845](https://pubmed.ncbi.nlm.nih.gov/29679845/)); and **p.Asn65Ser** (TPR domain) ([PMID: 25258038](https://pubmed.ncbi.nlm.nih.gov/25258038/)). A start-lost variant **c.3G>A** demonstrates the loss-of-function mechanism (reported in the dominant context) with markedly reduced protein but intact mRNA ([PMID: 33811518](https://pubmed.ncbi.nlm.nih.gov/33811518/)).

**Variant classification.** SCAR16 alleles are generally classified **pathogenic/likely pathogenic** under ACMG/AMP criteria, supported by functional evidence of destabilization and loss of ligase activity. **Functional consequence is loss of function** — through protein destabilization, misfolding, oligomerization, and increased turnover.

**Genotype–phenotype correlation.** Domain-specific biochemical changes correlate with distinct phenotypes and underlie clinical heterogeneity: "*cognitive dysfunction, increased tendon reflex, and ancestry were able to predict 54% of the variation in ataxia severity*" ([PMID: 31619515](https://pubmed.ncbi.nlm.nih.gov/31619515/)).

**Allele frequency.** Individual pathogenic *STUB1* alleles are rare in population databases (gnomAD), consistent with an ultra-rare recessive disorder. **Origin is germline.**

**Modifier genes.** **AFG3L2, PRKCG, TBP** act as candidate modifiers/second hits ([PMID: 32713943](https://pubmed.ncbi.nlm.nih.gov/32713943/)); the **digenic *STUB1*/*TBP*** relationship modulates penetrance and blurs the boundary between SCA48 and SCA17 ([PMID: 34906452](https://pubmed.ncbi.nlm.nih.gov/34906452/)).

**Epigenetic and chromosomal information.** No disease-specific DNA-methylation, histone, or chromosomal-abnormality (aneuploidy/translocation/CNV) findings are established for SCAR16. The disorder is caused by point/small mutations in a single gene, not by large-scale structural changes.

**Relationship to dominant STUB1 disease (SCA48).** The same gene causes **autosomal dominant SCA48** with heterozygous mutations: "*The overlap of several clinical signs between SCAR16 and SCA48 indicates the presence of a continuous clinical spectrum among recessively and dominantly inherited mutations of STUB1*" ([PMID: 32342324](https://pubmed.ncbi.nlm.nih.gov/32342324/)).

---

## Section 5 — Environmental Information

- **Environmental factors:** None established. SCAR16 is a monogenic disorder with no known toxic, radiation, pollution, or occupational contributors.
- **Lifestyle factors:** None established as causal or protective.
- **Infectious agents:** Not applicable. SCAR16 is not caused or triggered by any pathogen.

The only "environmental-like" modifier relevant to disease occurrence is **consanguinity**, which raises the probability of homozygous genotypes but is a population-genetic rather than an environmental exposure.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function mutation in *STUB1*** *leads to* production of destabilized/misfolded CHIP protein. Most SCAR16 mutations "*destabilize CHIP... including increased formation of soluble oligomers, decreased interactions with chaperones, diminished substrate ubiquitination, and reduced steady-state levels in cells*" ([PMID: 29317501](https://pubmed.ncbi.nlm.nih.gov/29317501/)).
2. **CHIP U-box destabilization/misfolding** *results in* abolished E3 ubiquitin-ligase activity. For the founding allele, "*T246M mutation results in structural disorganization and misfolding of the CHIP U-box domain, promoting oligomerization, and increased proteasome-dependent turnover. CHIP-T246M has no ligase activity, but maintains interactions with chaperones*" ([PMID: 30222779](https://pubmed.ncbi.nlm.nih.gov/30222779/)).
3. **Loss of ligase activity + reduced CHIP abundance** *leads to* failure of protein quality control. The p.Asn65Ser substitution "*impairs CHIP's ability to ubiquitinate HSC70 in vitro*" and "*the levels of CHIP are strongly reduced in vivo in patients' fibroblasts compared to controls*" ([PMID: 25258038](https://pubmed.ncbi.nlm.nih.gov/25258038/)).
4. **Impaired quality control** *results in* accumulation of CHIP substrates/clients. This branches:
   - **4a — Excitotoxic branch:** accumulation of the NMDA-receptor subunit **NR2A**. "*Wild-type, but not disease-associated mutant CHIPs promoted the degradation of NR2A, which may underlie the pathogenesis of ataxia*" ([PMID: 24312598](https://pubmed.ncbi.nlm.nih.gov/24312598/)).
   - **4b — cGMP/mitophagy branch:** accumulation of **PDE9A** → "*increased cGMP hydrolysis, and impaired PKG phosphorylation of CHIP at serine 19. This cascade further amplifies PDE9A accumulation, ultimately disrupting mitophagy and triggering neuronal apoptosis*" ([PMID: 39806097](https://pubmed.ncbi.nlm.nih.gov/39806097/)).
   - **4c — Mitophagy-regulation branch:** loss of CHIP's normal negative regulation of PINK1/Parkin mitophagy. CHIP normally "*promot[es] the degradation of PINK1, impairing Parkin translocation... and suppressing mitophagy*"; disease mutations "*impair its ability to negatively regulate mitophagy*" ([PMID: 39117117](https://pubmed.ncbi.nlm.nih.gov/39117117/)).
   - **4d — Aggregation branch:** failure to clear aggregation-prone clients (tau, polyglutamine ataxin-3). CHIP "*is a central component to the homeostatic mechanisms countering toxic polyQ proteins*" ([PMID: 19084066](https://pubmed.ncbi.nlm.nih.gov/19084066/)); CHIP with HSP90 mediates removal of pathological p-tau ([PMID: 17332887](https://pubmed.ncbi.nlm.nih.gov/17332887/)).
5. **Converging proteotoxic stress, disrupted mitophagy, and excitotoxic signaling** *lead to* **Purkinje-cell apoptosis and cerebellar neurodegeneration** — "*massive loss of Purkinje cells in the vermis and major loss in the cerebellar hemispheres*" ([PMID: 32713943](https://pubmed.ncbi.nlm.nih.gov/32713943/)).
6. **Purkinje-cell loss and broader tract degeneration** *result in* the clinical phenotype: progressive ataxia, dysarthria, cognitive impairment, spasticity, and multisystem features. DTI shows "*degeneration of manifold supra- and infratentorial tracts*" ([PMID: 28193273](https://pubmed.ncbi.nlm.nih.gov/28193273/)).

### Upstream vs downstream

- **Upstream (initiating):** *STUB1* mutation → CHIP destabilization/misfolding → loss of ligase activity (Steps 1–3).
- **Downstream (effector):** substrate accumulation (NR2A, PDE9A), mitophagy/cGMP dysregulation, aggregation, apoptosis (Steps 4–5).
- **Terminal:** Purkinje-cell death → clinical manifestation (Step 6).

### Pathways, processes, and suggested ontology terms

- **Molecular pathways:** ubiquitin–proteasome system; HSP70/HSP90 chaperone cycle; PINK1/Parkin mitophagy; cGMP/cAMP (PDE9A/PKG) signaling; NMDA-receptor signaling.
- **Cellular processes / GO:** protein ubiquitination (GO:0016567), chaperone-mediated protein folding (GO:0061077), mitophagy (GO:0000422), regulation of neuron apoptotic process (GO:0043523), proteasome-mediated ubiquitin-dependent protein catabolic process (GO:0043161).
- **Protein dysfunction:** CHIP misfolding, oligomerization, loss of function (U-box), increased proteasomal turnover.
- **Metabolic / mitochondrial:** disrupted mitophagy; CHIP-null mice show skeletal-muscle mitochondrial/SR alterations ([PMID: 28593200](https://pubmed.ncbi.nlm.nih.gov/28593200/)).
- **Cell types / CL:** cerebellar Purkinje cell (CL:0000121); neurons broadly (CL:0000540).

---

## Section 7 — Anatomical Structures Affected

**Organ level.**
- **Primary organ:** brain, specifically the **cerebellum** (UBERON:0002037), with the **cerebellar vermis** (UBERON:0004720) most severely affected.
- **Secondary involvement:** cerebral white-matter tracts (supra- and infratentorial), corticospinal/pyramidal tracts (spasticity), peripheral nerves (neuropathy), and the hypothalamic–pituitary–gonadal axis (hypogonadism).
- **Body systems:** central nervous system (cerebellar, pyramidal, extrapyramidal, cognitive), peripheral nervous system, autonomic nervous system, and endocrine (reproductive) system.

The neuropathology is selective: "*massive loss of Purkinje cells in the vermis and major loss in the cerebellar hemispheres without atrophy of the pons, hippocampus, or cerebral cortex*" ([PMID: 32713943](https://pubmed.ncbi.nlm.nih.gov/32713943/)).

**Tissue and cell level.**
- **Tissue:** nervous tissue (cerebellar cortex).
- **Cell populations:** **cerebellar Purkinje cells (CL:0000121)** are the principal targets; broader neuronal populations are affected along degenerating tracts.

**Subcellular level (GO Cellular Component).**
- **Mitochondria (GO:0005739)** — dysregulated mitophagy.
- **Cytosol / proteasome (GO:0000502)** — ubiquitin–proteasome quality control.
- **Cytoplasmic chaperone complexes** — HSP70/HSP90 interactions.
- **Plasma membrane / postsynaptic density** — NR2A (NMDA receptor) handling.

**Localization / lateralization.** Cerebellar involvement is **bilateral and relatively symmetric**, with vermian predominance; MRI consistently shows "*marked cerebellar atrophy*" ([PMID: 32367277](https://pubmed.ncbi.nlm.nih.gov/32367277/)).

---

## Section 8 — Temporal Development

**Onset.** Onset is typically **early — childhood to early adulthood** ("early onset spastic ataxia," [PMID: 32342324](https://pubmed.ncbi.nlm.nih.gov/32342324/)), though the age is variable and adult-onset presentations occur. Onset pattern is **insidious/chronic** rather than acute.

**Progression.** The course is **chronic, progressive, and currently irreversible**. SCAR16 is described as "*a fatal neurodegenerative disease characterized by truncal and limb ataxia that results in gait instability*" ([PMID: 29317501](https://pubmed.ncbi.nlm.nih.gov/29317501/)). Progression rate is **variable** and influenced by the specific *STUB1* genotype and modifier loci. There is no relapsing-remitting or episodic pattern; disease duration is **lifelong**.

**Patterns.** No spontaneous remission occurs. Because the mechanism is progressive proteostatic failure, the **critical therapeutic window is early** — the rationale for early molecular rescue of CHIP before irreversible Purkinje-cell loss.

---

## Section 9 — Inheritance and Population

**Epidemiology.** SCAR16 is **ultra-rare**. It had been reported in "*16 kindreds*" as of 2020 ([PMID: 32342324](https://pubmed.ncbi.nlm.nih.gov/32342324/)) and accounted for only "*0.4% (2/512) of our cohort with cerebellar ataxia*" in Taiwan ([PMID: 32367277](https://pubmed.ncbi.nlm.nih.gov/32367277/)). No reliable population prevalence/incidence per 100,000 is established; it is best described qualitatively as an uncommon Mendelian ataxia.

**Inheritance genetics.**
- **Pattern:** autosomal recessive (biallelic *STUB1*); the same gene causes dominant SCA48.
- **Penetrance / expressivity:** highly **variable expressivity**; penetrance is modulated by modifier genes and sex.
- **Genetic anticipation:** not a feature (SCAR16 is not a repeat-expansion disorder; anticipation-like effects arise only in the digenic *TBP* context).
- **Consanguinity / founder effects:** homozygous genotypes commonly arise in **consanguineous** pedigrees; the p.T246M allele acted as a founding homozygous mutation in the index Gordon Holmes family ([PMID: 24113144](https://pubmed.ncbi.nlm.nih.gov/24113144/)).
- **Carrier frequency:** not precisely established but low, consistent with rarity of pathogenic alleles in gnomAD.

**Population demographics.**
- **Sex ratio:** a notable **female predominance** — "*the majority of patients were women (70%)*" ([PMID: 32713943](https://pubmed.ncbi.nlm.nih.gov/32713943/)) — suggesting sex modulates penetrance/expressivity.
- **Geographic distribution:** reported worldwide (Europe, Asia including Taiwan, etc.) without a single endemic focus; specific alleles cluster within individual families/populations.
- **Modifier genetics:** "*'second hits' in AFG3L2, PRKCG, and TBP were detected in three families suggesting synergic effects*" ([PMID: 32713943](https://pubmed.ncbi.nlm.nih.gov/32713943/)).

---

## Section 10 — Diagnostics

**Molecular genetic testing (primary diagnostic modality).** Diagnosis is established by identifying **biallelic pathogenic *STUB1* variants**. The gene was discovered by combining linkage with WES: "*By combining the defined linkage region with the whole-exome sequencing results, we identified a homozygous mutation (c.493C>T) in CHIP*" ([PMID: 24312598](https://pubmed.ncbi.nlm.nih.gov/24312598/)). In practice, **whole-exome sequencing** or **hereditary-ataxia gene panels** including *STUB1* are the mainstays ([PMID: 32367277](https://pubmed.ncbi.nlm.nih.gov/32367277/)); WGS and single-gene *STUB1* testing are alternatives. Repeat-expansion, mitochondrial-DNA, karyotype, FISH, and chromosomal-microarray testing are **not diagnostic** for SCAR16 but are relevant to differential diagnosis.

**Neuroimaging.** Brain **MRI shows marked cerebellar atrophy** ([PMID: 32367277](https://pubmed.ncbi.nlm.nih.gov/32367277/)). **Diffusion tensor imaging (DTI)** reveals "*degeneration of manifold supra- and infratentorial tracts*," documenting multisystem tract involvement ([PMID: 28193273](https://pubmed.ncbi.nlm.nih.gov/28193273/)). Importantly, "*the isolated cerebellar ataxia without involvement of other systems cannot be a basis to exclude the possibility of STUB1-related disease*" ([PMID: 32367277](https://pubmed.ncbi.nlm.nih.gov/32367277/)) — genetic testing should be pursued even in isolated cerebellar presentations.

**Supportive laboratory tests.** In the hypogonadism (Gordon Holmes) subset, endocrine testing shows **hypogonadotropic hypogonadism** (low sex steroids with inappropriately low/normal LH/FSH). No specific circulating biochemical biomarker is diagnostic; molecular confirmation is required.

**Cellular / functional confirmation (research).** Patient fibroblasts show markedly reduced CHIP protein ([PMID: 25258038](https://pubmed.ncbi.nlm.nih.gov/25258038/)); iPSC and iPSC-neuron models support functional validation of variant pathogenicity ([PMID: 29679845](https://pubmed.ncbi.nlm.nih.gov/29679845/); [PMID: 33097556](https://pubmed.ncbi.nlm.nih.gov/33097556/)).

**Clinical criteria / differential diagnosis.** There is no formal consensus diagnostic score; diagnosis rests on the clinical triad of early-onset progressive ataxia + cerebellar atrophy + biallelic *STUB1* variants. **Differential diagnosis** includes other early-onset recessive ataxias (Friedreich ataxia, ataxia with oculomotor apraxia, ARSACS, POLG-related ataxia), other Gordon Holmes syndrome genes (*RNF216*, *PNPLA6*, *OTUD4*, *GNRH1*), and dominant SCA48/SCA17 (distinguished by *TBP* CAG status and inheritance).

**Screening.** No newborn or population screening exists. **Cascade/carrier testing** within affected families and prenatal/preimplantation testing are options once the familial variants are known.

---

## Section 11 — Outcome / Prognosis

**Overall prognosis.** SCAR16 is a **progressive, currently incurable neurodegenerative disorder** and is described as "*fatal*" in its more severe multisystem forms ([PMID: 29317501](https://pubmed.ncbi.nlm.nih.gov/29317501/)). Truncal and limb ataxia produce progressive gait instability and loss of independent mobility; cognitive decline, spasticity, dysarthria, and (in subsets) epilepsy and autonomic dysfunction add cumulative morbidity.

**Survival / mortality.** No formal 5- or 10-year survival statistics exist for this ultra-rare disorder. Life expectancy is reduced in severe multisystem cases; milder, ataxia-predominant cases may have a more protracted course.

**Morbidity and function.** Long-term outcomes include loss of ambulation, dependence for activities of daily living, communication impairment (dysarthria), and, where present, cognitive/behavioral disability (frontal syndrome in ~54% of carriers, [PMID: 32713943](https://pubmed.ncbi.nlm.nih.gov/32713943/)).

**Complications.** Aspiration (from dysarthria/dysphagia), falls/injury (from ataxia and spasticity), seizure-related morbidity, and complications of immobility.

**Prognostic factors.** Severity is partly predictable from clinical and genetic features: "*cognitive dysfunction, increased tendon reflex, and ancestry were able to predict 54% of the variation in ataxia severity*" ([PMID: 31619515](https://pubmed.ncbi.nlm.nih.gov/31619515/)). The specific *STUB1* genotype (domain affected, degree of destabilization) and modifier alleles influence course. No validated molecular prognostic biomarker is in clinical use.

---

## Section 12 — Treatment

**Current standard of care: supportive/symptomatic only.** There is **no approved disease-modifying therapy**. Management targets individual manifestations:

| Manifestation | Supportive intervention | Suggested NCIT concept |
|---|---|---|
| Ataxia, gait instability | Physical therapy, gait/balance training, assistive devices | Physical Therapy (NCIT:C15367) |
| Dysarthria | Speech therapy | Speech Therapy (NCIT:C15451) |
| Functional decline (ADLs) | Occupational therapy | Occupational Therapy (NCIT:C15329) |
| Spasticity | Antispasticity agents (e.g., baclofen), stretching | Baclofen (NCIT:C376) |
| Epilepsy | Anticonvulsants | Anticonvulsant Agent (NCIT:C264) |
| Hyperkinetic movement disorders | Symptomatic pharmacotherapy | — |
| Hypogonadotropic hypogonadism | Hormone replacement therapy | Hormone Replacement Therapy (NCIT:C15667) |

**Pharmacogenomics.** No SCAR16-specific pharmacogenomic guidance is established.

**Emerging / preclinical molecular therapies.** Two mechanism-based strategies show preclinical promise:

1. **Pharmacological chaperones / thermostabilizers.** Because most mutations destabilize CHIP and activity is recoverable below the mutant's melting temperature, "*compounds that improve the thermostability of genetic CHIP variants may be beneficial for treating*" the disease ([PMID: 29317501](https://pubmed.ncbi.nlm.nih.gov/29317501/)).
2. **PDE9A inhibition and CHIP restoration.** In CHIP-mutant rodent ataxia models, "*pharmacological inhibition of PDE9A via Bay 73-6691 or virus-mediated CHIP expression restored the balance of cGMP/cAMP signalling. These interventions protect against cerebellar neuropathologies, particularly Purkinje neuron mitophagy dysfunction*" ([PMID: 39806097](https://pubmed.ncbi.nlm.nih.gov/39806097/)).

Additionally, the broader neuroprotective potential of restoring CHIP function is supported by AAV-CHIP overexpression reducing amyloid-β and p-tau and improving cognition in Alzheimer mice ([PMID: 38767490](https://pubmed.ncbi.nlm.nih.gov/38767490/)) — a proof of concept for **CHIP gene-replacement/augmentation** approaches.

**Advanced therapeutics.** Gene therapy (AAV-mediated *STUB1*/CHIP delivery) and small-molecule proteostasis modulators are conceptually attractive but remain **preclinical**; no cell therapy, RNA therapy, or targeted immunotherapy is established. No SCAR16-specific interventional clinical trials with NCT identifiers were identified.

---

## Section 13 — Prevention

Because SCAR16 is a Mendelian recessive disorder with no environmental contribution, prevention is **genetic and reproductive**, not lifestyle-based.

- **Primary prevention:** not applicable in the classical sense (no modifiable exposure). The principal preventive lever is **reproductive genetic counseling** in at-risk families.
- **Genetic counseling:** carriers have a 25% recurrence risk per pregnancy. Once familial *STUB1* variants are known, **carrier testing, prenatal diagnosis, and preimplantation genetic testing (PGT)** are available.
- **Secondary prevention:** early molecular diagnosis (via WES/panels) enables earlier supportive intervention and, prospectively, earlier enrollment in future disease-modifying trials during the critical pre-degeneration window.
- **Tertiary prevention:** rehabilitation, fall prevention, seizure control, aspiration precautions, and management of endocrine deficits to limit complications.
- **Immunization / public-health / environmental interventions:** not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy affected (experimental):** *Homo sapiens* (NCBI:txid9606); disease modeled in *Mus musculus* (NCBI:txid10090) and *Rattus norvegicus* (NCBI:txid10116); mitophagy phenotypes also studied in *Caenorhabditis elegans* (NCBI:txid6239).
- **Orthologous genes:** mouse *Stub1*, rat *Stub1*, *C. elegans chn-1* (a CHIP ortholog). CHIP function is **evolutionarily conserved** across metazoans.
- **Natural disease in other species:** No well-characterized naturally occurring *STUB1*/CHIP ataxia is documented in companion animals or wildlife (no established OMIA entry identified). SCAR16 knowledge derives from human patients and engineered animal models rather than spontaneous veterinary disease.
- **Comparative biology:** CHIP-null mice recapitulate ataxia, reproductive impairment, and skeletal-muscle mitochondrial/SR alterations ([PMID: 24113144](https://pubmed.ncbi.nlm.nih.gov/24113144/); [PMID: 28593200](https://pubmed.ncbi.nlm.nih.gov/28593200/)); mitophagy dysregulation is conserved in *C. elegans* neurons ([PMID: 39117117](https://pubmed.ncbi.nlm.nih.gov/39117117/)), underscoring conserved disease mechanisms.
- **Transmission / zoonosis:** not applicable (non-infectious genetic disease).

---

## Section 15 — Model Organisms

SCAR16 is supported by a robust suite of models:

| Model | Type | Key phenotype recapitulation | Reference |
|---|---|---|---|
| CHIP-null (*Stub1−/−*) mouse | Mammalian knockout | Behavioral + reproductive impairments mimicking ataxia and hypogonadism | [PMID: 24113144](https://pubmed.ncbi.nlm.nih.gov/24113144/) |
| T246M knock-in mouse | Mammalian knock-in | Cognitive + motor cerebellar dysfunction; learning/memory deficits, distinct from null | [PMID: 30222779](https://pubmed.ncbi.nlm.nih.gov/30222779/) |
| T246M knock-in rat | Mammalian knock-in | Cerebellar motor/cognitive dysfunction | [PMID: 30222779](https://pubmed.ncbi.nlm.nih.gov/30222779/) |
| CHIP-null mouse (muscle) | Mammalian knockout | Skeletal-muscle mitochondrial/SR alterations | [PMID: 28593200](https://pubmed.ncbi.nlm.nih.gov/28593200/) |
| *C. elegans* neurons | Invertebrate | Mitophagy dysregulation by disease-associated CHIP mutations | [PMID: 39117117](https://pubmed.ncbi.nlm.nih.gov/39117117/) |
| Patient iPSCs (HIHCNi001-A) | Cellular / in vitro | Compound-het STUB1 (c.355C>T, c.880A>T); disease-in-a-dish | [PMID: 29679845](https://pubmed.ncbi.nlm.nih.gov/29679845/) |
| iPSC-derived neurons vs. fibroblasts | Cellular / in vitro | Cell-type-specific heat-shock/proteostasis defects | [PMID: 33097556](https://pubmed.ncbi.nlm.nih.gov/33097556/) |
| Patient fibroblasts | Cellular / in vitro | Strongly reduced CHIP protein | [PMID: 25258038](https://pubmed.ncbi.nlm.nih.gov/25258038/) |

The knock-in models are particularly valuable: "*Animals homozygous for T246M had both cognitive and motor cerebellar dysfunction distinct from those observed in the CHIP null animal model, as well as deficits in learning and memory, reflective of the cognitive deficits reported in SCAR16 patients*" ([PMID: 30222779](https://pubmed.ncbi.nlm.nih.gov/30222779/)) — demonstrating that a physiologically expressed point mutant captures the human phenotype better than complete knockout.

**Applications:** these models enable study of Purkinje-cell degeneration, mitophagy/cGMP dysregulation, proteostasis, and therapeutic testing (PDE9A inhibitors, CHIP re-expression). **Limitations:** rodent cerebellar circuitry and lifespan differ from humans; iPSC-neurons may not fully replicate mature Purkinje-cell vulnerability; the digenic modifier landscape (TBP/AFG3L2/PRKCG) is not captured by single-gene models.

---

## Mechanistic Model / Interpretation

```
  STUB1 biallelic LoF mutation (16p13.3)
              │
              ▼
  Destabilized / misfolded CHIP  ───►  U-box disorganization,
  (reduced steady-state levels)        oligomerization, ↑ turnover
              │
              ▼
  LOSS of E3 ubiquitin-ligase activity  +  altered co-chaperone function
              │
     ┌────────┼───────────────┬───────────────────┬────────────────┐
     ▼        ▼               ▼                   ▼                ▼
  NR2A ↑   PDE9A ↑        PINK1/Parkin        tau / polyQ       HSC70
 (excito-  → cGMP        mitophagy           aggregate         (chaperone
  toxic)   hydrolysis ↑  dysregulation       accumulation      cycle
           impaired PKG                       (proteotoxic)     disrupted)
           → CHIP-Ser19
           feedback loss
     └────────┴───────────────┴───────────────────┴────────────────┘
                              │
                              ▼
              Purkinje-cell mitochondrial dysfunction + APOPTOSIS
                              │
                              ▼
      Selective Purkinje-cell loss (vermis > hemispheres);
      widespread supra-/infratentorial tract degeneration
                              │
                              ▼
   Progressive ataxia · dysarthria · cognitive decline · spasticity ·
   epilepsy · neuropathy · hypogonadism · autonomic dysfunction
```

The unifying theme is **collapse of neuronal protein quality control**. CHIP sits at the junction of the chaperone (HSP70/HSP90) and degradation (ubiquitin–proteasome, autophagy/mitophagy) systems. Its loss simultaneously (i) permits accumulation of specific toxic substrates (NR2A → excitotoxicity; PDE9A → cGMP/mitophagy collapse), (ii) removes surveillance of aggregation-prone clients (tau, ataxin-3), and (iii) deregulates mitophagy. Purkinje cells — metabolically demanding, morphologically elaborate, and exquisitely dependent on proteostasis — are selectively vulnerable, explaining the vermis-predominant Purkinje-cell loss and the cerebellar core of the phenotype. The variant-specific degree of destabilization, plus sex and modifier genes (TBP, AFG3L2, PRKCG), tunes where a given patient falls on the recessive-SCAR16 ↔ dominant-SCA48 continuum.

---

## Evidence Base

| PMID | Contribution | Findings supported |
|---|---|---|
| [32342324](https://pubmed.ncbi.nlm.nih.gov/32342324/) | Review: SCAR16 = biallelic STUB1; spectrum; SCA48 continuum; 16 kindreds | F001, F002, F004, F013 |
| [29679845](https://pubmed.ncbi.nlm.nih.gov/29679845/) | Patient iPSC line; OMIM #615768; compound-het genotype | F001, F014 |
| [28193273](https://pubmed.ncbi.nlm.nih.gov/28193273/) | Four novel mutations; severe multisystem phenotype; DTI tract degeneration | F002, F009 |
| [32367277](https://pubmed.ncbi.nlm.nih.gov/32367277/) | Taiwan cohort; MRI atrophy; 0.4% frequency; isolated ataxia caveat | F002, F009, F013 |
| [25258038](https://pubmed.ncbi.nlm.nih.gov/25258038/) | p.Asn65Ser impairs HSC70 ubiquitination; reduced CHIP in fibroblasts | F003, F014 |
| [39117117](https://pubmed.ncbi.nlm.nih.gov/39117117/) | CHIP negatively regulates PINK1/Parkin mitophagy; mutations dysregulate | F003 |
| [31619515](https://pubmed.ncbi.nlm.nih.gov/31619515/) | Function-based heterogeneity; predictors explain 54% of severity | F004, F012 |
| [34906452](https://pubmed.ncbi.nlm.nih.gov/34906452/) | Digenic STUB1/TBP modifies penetrance | F004, F008, F013 |
| [24113144](https://pubmed.ncbi.nlm.nih.gov/24113144/) | CHIP-null mice recapitulate ataxia + hypogonadism (founding T246M) | F005 |
| [30222779](https://pubmed.ncbi.nlm.nih.gov/30222779/) | T246M knock-in mouse/rat; U-box misfolding, no ligase activity | F005, F006 |
| [28593200](https://pubmed.ncbi.nlm.nih.gov/28593200/) | CHIP-null skeletal-muscle mitochondrial/SR alterations | F005 |
| [29317501](https://pubmed.ncbi.nlm.nih.gov/29317501/) | Most SCAR16 mutations destabilize CHIP; thermostabilizer therapy rationale | F006, F010 |
| [24312598](https://pubmed.ncbi.nlm.nih.gov/24312598/) | Gene discovery (linkage+WES); NR2A degradation mechanism | F007, F009 |
| [39806097](https://pubmed.ncbi.nlm.nih.gov/39806097/) | PDE9A/cGMP/mitophagy cascade; Bay 73-6691 + CHIP re-expression protective | F007, F010 |
| [19084066](https://pubmed.ncbi.nlm.nih.gov/19084066/) | CHIP suppresses polyQ (ataxin-3) neurotoxicity | F007, F011 |
| [32713943](https://pubmed.ncbi.nlm.nih.gov/32713943/) | Neuropathology (Purkinje loss); 54% cognitive; 70% female; modifiers | F008, F012 |
| [17332887](https://pubmed.ncbi.nlm.nih.gov/17332887/) | CHIP–HSP90 clears pathological p-tau | F011 |
| [38767490](https://pubmed.ncbi.nlm.nih.gov/38767490/) | AAV-CHIP overexpression neuroprotective (Alzheimer model) | F011 |
| [33097556](https://pubmed.ncbi.nlm.nih.gov/33097556/) | Cell-type-specific heat-shock defects (fibroblast vs iPSC-neuron) | F014 |
| [33811518](https://pubmed.ncbi.nlm.nih.gov/33811518/) | De novo start-lost c.3G>A; LoF mechanism (dominant context) | Section 4 |
| [31571321](https://pubmed.ncbi.nlm.nih.gov/31571321/) | SCA48 phenotype in 8 families; SCAR16 overlap | Section 4 |

---

## Limitations and Knowledge Gaps

1. **Epidemiology is imprecise.** With only ~16 originally reported kindreds and cohort-based frequency estimates (~0.4%), true prevalence, incidence, and carrier frequency are unknown; gnomAD-based carrier frequency was not directly computed here.
2. **No natural-history dataset.** Quantitative progression rates, survival statistics, and validated QoL measures (EQ-5D/SF-36/PROMIS) specific to SCAR16 are lacking; prognosis is described qualitatively.
3. **Mechanistic branches partly inferred.** The NR2A excitotoxic branch and the PDE9A/cGMP/mitophagy cascade are demonstrated in cellular and rodent models, not in human cerebellar tissue; their relative contributions to human Purkinje-cell death remain to be weighted.
4. **Genotype–phenotype resolution is incomplete.** Although domain-specific effects predict ~54% of ataxia-severity variance, the remaining variance (including the strong female predominance and modifier-gene effects) is unexplained.
5. **Therapeutics are entirely preclinical.** Thermostabilizers, PDE9A inhibitors, and CHIP gene therapy have not been tested in SCAR16 patients; no NCT-registered trials were identified.
6. **No naturally occurring animal disease** is documented, limiting comparative-pathology insight.

---

## Proposed Follow-up Experiments / Actions

1. **Population genetics:** Estimate *STUB1* pathogenic-allele carrier frequency and predicted disease prevalence from gnomAD/large biobanks; assess sex-specific penetrance to explain the 70% female predominance.
2. **Natural-history registry:** Establish a longitudinal SCAR16/STUB1 registry capturing standardized ataxia scales (SARA), cognitive batteries, MRI volumetrics, and QoL instruments to define progression rates and prognostic biomarkers.
3. **Therapeutic translation:** Advance the two lead preclinical strategies — (a) PDE9A inhibition (Bay 73-6691 and clinical-stage PDE9A inhibitors) and (b) AAV-mediated CHIP re-expression / pharmacological thermostabilizers — through IND-enabling studies in T246M knock-in models, with Purkinje-cell mitophagy and behavior as endpoints.
4. **Human tissue validation:** Use patient iPSC-derived Purkinje-like neurons and, where available, autopsy tissue to test whether NR2A and PDE9A accumulate in human disease and correlate with Purkinje-cell loss.
5. **Modifier dissection:** Systematically genotype *TBP*, *AFG3L2*, and *PRKCG* in STUB1 cohorts and model digenic interactions to quantify penetrance modulation.
6. **Biomarker discovery:** Explore CSF/plasma CHIP levels, neurofilament light chain, and cGMP-pathway metabolites as candidate diagnostic/prognostic biomarkers.

---

*Report compiled from 14 confirmed findings and 24 reviewed papers across 5 investigation iterations. Evidence types span human clinical/genetic studies, model-organism (mouse, rat, C. elegans), in vitro/cellular (patient fibroblasts, iPSCs, iPSC-neurons), and biochemical/structural work.*


## Artifacts

- [OpenScientist final report](Autosomal_Recessive_Spinocerebellar_Ataxia_16-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Autosomal_Recessive_Spinocerebellar_Ataxia_16-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 27 |
| Quoted claims found in source | 25 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 21 |
| On topic | 18 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:39117117` *(abstract only)*: "*impair its ability to negatively regulate mitophagy*"
  - closest text in source: "Furthermore, we find that multiple disease-associated mutations in CHIP dysregulate mitophagy both in vitro and in vivo in C"
- `PMID:24312598`: "*By combining the defined linkage region with the whole-exome sequencing results, we identified a homozygous mutation (c.493C>T) in CHIP*"
  - closest text in source: "By combining the defined linkage region with the whole-exome sequencing results, we identified a homozygous mutation (c.493CT) in CHIP (NM_005861) in this family"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 19 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014339` (2 mentions) - the report calls it "MONDO"; MONDO calls it **autosomal recessive spinocerebellar ataxia 16**
- `UBERON:0002037` (1 mention) - the report calls it "cerebellum", "Primary organ:** brain, specifically the **cerebellum"; UBERON calls it **cerebellum**
- `NCIT:C15367` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Health Risk Assessment**
- `NCIT:C15451` (1 mention) - the report calls it "Speech Therapy"; NCIT calls it **Prior Anthracycline Therapy**
- `NCIT:C15329` (1 mention) - the report calls it "Occupational Therapy"; NCIT calls it **Surgical Procedure**
- `NCIT:C376` (1 mention) - the report calls it "Baclofen"; NCIT calls it **Cisplatin**
- `NCIT:C15667` (1 mention) - the report calls it "Hormone Replacement Therapy"; NCIT calls it **Sentinel Lymph Node Biopsy**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000990` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0061077` (obsolete chaperone-mediated protein folding) (1 mention) - replaced by `GO:0006457`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001272` (1 mention) - the report calls it "Cerebellar atrophy on MRI"; HP calls it **Cerebellar atrophy**
- `HP:0100543` (1 mention) - the report calls it "Cognitive impairment / dementia (frontal syndrome)"; HP calls it **Cognitive impairment**
- `HP:0000044` (1 mention) - the report calls it "Hypogonadotropic hypogonadism (Gordon Holmes)"; HP calls it **Hypogonadotropic hypogonadism**
- `HP:0001250` (1 mention) - the report calls it "Epilepsy / seizures"; HP calls it **Seizure**, and lists "Epileptic seizure" among its other names
- `GO:0016567` (1 mention) - the report calls it "Cellular processes / GO:** protein ubiquitination"; GO calls it **protein ubiquitination**
- `CL:0000121` (2 mentions) - the report calls it "Cell types / CL:** cerebellar Purkinje cell", "Cell populations:** **cerebellar Purkinje cells"; CL calls it **Purkinje cell**, and lists "cerebellar Purkinje cell" among its other names
- `GO:0005739` (1 mention) - the report calls it "Mitochondria"; GO calls it **mitochondrion**, and lists "mitochondria" among its other names
- `GO:0000502` (1 mention) - the report calls it "Cytosol / proteasome"; GO calls it **proteasome complex**, and lists "26S proteasome" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000121` - called "Cell types / CL:** cerebellar Purkinje cell", "Cell populations:** **cerebellar Purkinje cells"
- `UBERON:0002037` - called "cerebellum", "Primary organ:** brain, specifically the **cerebellum"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.