---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-05T22:40:58.281844'
end_time: '2026-09-05T22:56:14.685849'
duration_seconds: 916.4
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Amyotrophic Lateral Sclerosis Type 1
  mondo_id: MONDO:0007103
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
citation_count: 38
reference_validation:
  total_references: 38
  verified: 38
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 23
  quotes_valid: 18
  quotes_unsupported: 5
  unsupported_quote_references:
  - PMID:25613506
  - PMID:32958236
  - PMID:42661170
  - PMID:40364643
  - PMID:39257530
  relevance_assessed: 38
  on_topic: 27
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 31
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 25
  labels_matching: 15
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0007103
    reported_labels:
    - MONDO
    ontology_label: amyotrophic lateral sclerosis type 1
  - term_id: HP:0003323
    reported_labels:
    - Clinical sign
    ontology_label: Progressive muscle weakness
  - term_id: HP:0007340
    reported_labels:
    - Symptom
    ontology_label: Lower limb muscle weakness
  - term_id: HP:0002380
    reported_labels:
    - Clinical sign
    ontology_label: Fasciculations
  - term_id: HP:0001257
    reported_labels:
    - Clinical sign
    ontology_label: Spasticity
  - term_id: HP:0002093
    reported_labels:
    - Clinical sign
    ontology_label: Respiratory insufficiency
  - term_id: NCIT:C1289
    reported_labels:
    - Glutamate antagonist / anti-excitotoxic
    ontology_label: Recombinant Interleukin-8
  - term_id: NCIT:C65331
    reported_labels:
    - Free-radical scavenger / antioxidant
    ontology_label: Cinnamon
  labels_variant: 2
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
  path: Amyotrophic_Lateral_Sclerosis_Type_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Amyotrophic_Lateral_Sclerosis_Type_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Amyotrophic Lateral Sclerosis Type 1
- **MONDO ID:** MONDO:0007103 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Amyotrophic Lateral Sclerosis Type 1** covering all of the
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

# Amyotrophic Lateral Sclerosis Type 1 (ALS1 / SOD1-ALS): Comprehensive Disease Characterization

**Disease:** Amyotrophic Lateral Sclerosis Type 1 (ALS1)
**MONDO ID:** MONDO:0007103 · **OMIM:** #105400 · **Category:** Mendelian (autosomal dominant, D90A often recessive)
**Causal gene:** *SOD1* (Cu/Zn superoxide dismutase 1), chromosome 21q22.11
**Prepared:** 2026-09-05 · Evidence sources: human clinical, model organism, in vitro, and computational literature (PMIDs cited throughout)

---

## Summary

Amyotrophic Lateral Sclerosis Type 1 (ALS1) is the Mendelian, adult-onset form of amyotrophic lateral sclerosis caused by pathogenic variants in *SOD1*, the gene encoding the ubiquitously expressed free-radical scavenging enzyme Cu/Zn superoxide dismutase 1. It is the archetypal "familial ALS" gene — the first ALS gene ever identified — and accounts for approximately **2% of all ALS and ~12–20% of familial ALS** ([PMID: 41661214](https://pubmed.ncbi.nlm.nih.gov/41661214/), [PMID: 18055113](https://pubmed.ncbi.nlm.nih.gov/18055113/)). Clinically it is largely indistinguishable at the bedside from other ALS: progressive upper- and lower-motor-neuron degeneration producing weakness, muscle atrophy, spasticity, bulbar dysfunction, and ultimately death from respiratory failure. What distinguishes ALS1 is its defined molecular cause, its highly variant-dependent natural history (from the rapidly fatal A4V allele to slowly progressive recessive D90A disease), and — uniquely among neurodegenerative diseases — the existence of an **approved, gene-targeted therapy (tofersen)**.

The central mechanistic insight is that mutant SOD1 causes disease through a **toxic gain-of-function**, not loss of enzymatic activity. The most frequent worldwide mutation, D90A, produces a protein with normal enzymatic activity, proving the point ([PMID: 36385230](https://pubmed.ncbi.nlm.nih.gov/36385230/)). Mutant SOD1 misfolds into neurotoxic aggregates that propagate in a **prion-like, templated manner** between motor neurons ([PMID: 41702846](https://pubmed.ncbi.nlm.nih.gov/41702846/), [PMID: 32958236](https://pubmed.ncbi.nlm.nih.gov/32958236/)). Motor neuron death is **non-cell-autonomous**: mutant SOD1 in astrocytes, microglia, skeletal muscle, and T cells actively drives neuroinflammation and degeneration ([PMID: 25613506](https://pubmed.ncbi.nlm.nih.gov/25613506/)). Vulnerable alpha motor neurons transit through a conserved "disease-associated motor neuron" state before dying ([PMID: 42335888](https://pubmed.ncbi.nlm.nih.gov/42335888/)).

Because the genetic cause is known and neurofilament light chain (NfL) rises **presymptomatically**, ALS1 has become the proving ground for precision neurology. Tofersen, an intrathecal antisense oligonucleotide (ASO) that lowers SOD1 synthesis, is the first and only approved genetically targeted ALS therapy; it robustly lowers plasma/CSF neurofilament and, in some carriers, produces a "chronic nonprogressive ALS" phenotype never previously observed ([PMID: 41661214](https://pubmed.ncbi.nlm.nih.gov/41661214/), [PMID: 41850233](https://pubmed.ncbi.nlm.nih.gov/41850233/), [PMID: 41670738](https://pubmed.ncbi.nlm.nih.gov/41670738/)). The presymptomatic NfL biomarker has empowered the **first-ever ALS prevention trial (ATLAS, NCT04856982)** ([PMID: 37382103](https://pubmed.ncbi.nlm.nih.gov/37382103/)).

---

## Section 1 — Disease Information

**Overview.** ALS1 is the *SOD1*-related subtype of amyotrophic lateral sclerosis, a fatal adult-onset motor neuron disease characterized by progressive degeneration of upper (corticospinal) and lower (spinal/bulbar) motor neurons, leading to muscle weakness, atrophy, fasciculations, spasticity, bulbar palsy, and terminal respiratory failure. It was the first genetically defined form of ALS (SOD1 mutations reported 1993) and defines the "Type 1" designation in OMIM.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0007103 |
| OMIM | #105400 (Amyotrophic lateral sclerosis 1) |
| Gene OMIM | *SOD1* 147450 |
| ICD-10 | G12.21 (ALS) |
| ICD-11 | 8B60.0 |
| MeSH | D000690 (Amyotrophic Lateral Sclerosis) |
| Orphanet | ORPHA:803 (ALS); SOD1 subtype within |
| HGNC | HGNC:11179 (*SOD1*) |

**Synonyms / alternative names.** SOD1-ALS; SOD1-related ALS; Cu/Zn superoxide dismutase-related ALS; familial ALS type 1; ALS1; motor neuron disease, SOD1-related. (Historic "Lou Gehrig's disease" and "Charcot's disease" refer to ALS broadly.)

**Data provenance.** The knowledge assembled here is derived from **aggregated disease-level resources** — clinical cohorts, registries (e.g., Rhineland-Palatinate registry, US National ALS Registry), natural-history studies, mouse models, and clinical trials (VALOR/NCT02623699, ATLAS/NCT04856982) — rather than individual EHR records.

---

## Section 2 — Etiology

**Primary cause.** ALS1 is a **monogenic, autosomal-dominant** disorder caused by heterozygous pathogenic variants in *SOD1* (the recessive D90A being the notable exception). More broadly, monogenic determinants account for roughly 20% of all ALS (including ~10% familial cases), while "less well understood multigenetic causes may contribute to another 20% to 80%" ([PMID: 26515627](https://pubmed.ncbi.nlm.nih.gov/26515627/)).

**Genetic risk factors.** The causal factor is the *SOD1* mutation itself (>200 pathogenic variants known). Other major familial ALS genes (C9ORF72, FUS/TLS, TARDBP/TDP-43) define separate subtypes; "about two-thirds of familial cases are triggered by mutations of four genes... C9ORF72, ... SOD1, FUS/TLS, TDP43" ([PMID: 25613506](https://pubmed.ncbi.nlm.nih.gov/25613506/)).

**Environmental risk factors.** For ALS generally, candidate exposures include "male gender..., smoking, military service, exercise, electrical exposure, heavy metals, agricultural chemicals, and geographic clusters" ([PMID: 26515627](https://pubmed.ncbi.nlm.nih.gov/26515627/)). Smoking is the most consistently replicated modifiable risk factor. Military veterans have poorer ALS survival than non-veterans (5-yr survival 47.1% vs 57.4%; median 3.77 vs 4.79 yr), suggesting military history is an important prognostic/risk factor ([PMID: 42669596](https://pubmed.ncbi.nlm.nih.gov/42669596/)). In genetically susceptible individuals, "a combination of insults that induce modest oxidative stress can exert additive deleterious effects on motor neurons" ([PMID: 23797033](https://pubmed.ncbi.nlm.nih.gov/23797033/)).

**Protective factors.** No well-established genetic protective allele is documented for SOD1-ALS specifically; disease-modifying observations relate instead to variant identity (recessive D90A slow course). No robust environmental protective factor is established.

**Gene–environment interaction.** The prevailing model is a multistep, multiple-hit process in which an inherited *SOD1* gain-of-function lowers the threshold, and additional oxidative/environmental insults accelerate motor neuron death — "ALS is possibly a systemic disease" driven by oxidative stress "particularly in genetically susceptive individuals" ([PMID: 23797033](https://pubmed.ncbi.nlm.nih.gov/23797033/)).

---

## Section 3 — Phenotypes

ALS1 is predominantly a motor phenotype, but SOD1 variants show characteristic features and marked variant-dependent variability.

| Phenotype | Type | HPO term (suggested) | Characteristics |
|---|---|---|---|
| Progressive muscle weakness | Clinical sign | HP:0003323 | Adult-onset; progressive; near-universal |
| Lower-limb–onset weakness | Symptom | HP:0007340 | Frequent in SOD1; "legs first" pattern |
| Muscle atrophy | Physical manifestation | HP:0003202 | Progressive; near-universal |
| Fasciculations | Clinical sign | HP:0002380 | Lower-motor-neuron sign |
| Spasticity / hyperreflexia | Clinical sign | HP:0001257 | Upper-motor-neuron sign; less prominent in some SOD1 |
| Bulbar dysfunction (dysarthria/dysphagia) | Clinical sign | HP:0001260 / HP:0002015 | Bulbar-onset less common in SOD1 than sporadic ALS |
| Respiratory insufficiency | Clinical sign | HP:0002093 | Terminal cardinal feature |
| Sensory/autonomic/bladder involvement (D90A) | Symptom | HP:0000708-related | Documented in homozygous D90A |

**Onset & severity.** Predominantly adult-onset but wide range; juvenile-onset occurs — two adolescents (onset 15–16 yr) presented with "lower limb onset of weakness, lower motor neuron examination findings, and rapid progression over months to involve all body regions" ([PMID: 42265995](https://pubmed.ncbi.nlm.nih.gov/42265995/)). Severity is strongly variant-dependent (see Section 8). The D90A recessive phenotype is "stereotypic with slowly evolving motor symptoms beginning in the legs and may also include sensory, autonomic, and urinary bladder involvement" ([PMID: 36385230](https://pubmed.ncbi.nlm.nih.gov/36385230/)).

**Progression.** Relentlessly progressive in most variants; recessive D90A is slowly progressive.

**Quality-of-life impact.** Progressive loss of ambulation, speech, swallowing, and respiration produces severe disability and high symptom/psychosocial burden; early palliative care integration is emphasized given the terminal trajectory ([PMID: 42652396](https://pubmed.ncbi.nlm.nih.gov/42652396/)).

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *SOD1* (HGNC:11179; OMIM 147450), chromosome 21q22.11, encoding the 154-residue homodimeric Cu/Zn superoxide dismutase.

**Pathogenic variants.** >200 mostly missense variants distributed across all five exons. Nomenclature examples: **p.Ala5Val (A4V)** — most common North American variant; **p.Asp90Ala (D90A)** — most common worldwide, often recessive; **p.Gly94Ser / p.Gly93Ala (G93A)** — the canonical mouse-model allele; **p.Gly85Arg (G85R)**; **p.Asp125Gly** — juvenile-onset, incompletely penetrant. Near-splice/intronic variants (e.g., c.358-10T>G) also occur ([PMID: 33785574](https://pubmed.ncbi.nlm.nih.gov/33785574/)).

**Variant type/class.** Predominantly missense; also nonsense, frameshift, and splice-region variants. Classification per ACMG/AMP: most recurrent SOD1 variants are Pathogenic/Likely Pathogenic in ClinVar.

**Allele frequency.** SOD1 pathogenic variants are individually rare in gnomAD; D90A carrier frequency is elevated in Scandinavian populations due to a founder effect.

**Origin.** **Germline** (inherited). The A4V allele is an ancient founder mutation estimated to have arisen ~540 generations (~12,000 years) ago (95% CI 480–700), with a minimal conserved 2.8-kb haplotype more similar to Asian than European populations, "suggesting origination in Asia" and spread via Native Asian-Americans ([PMID: 18055113](https://pubmed.ncbi.nlm.nih.gov/18055113/)).

**Functional consequence.** **Toxic gain-of-function.** Definitive evidence: the D90A mutant "resembles the wild type, with normal content and enzymatic activity in the central nervous system" ([PMID: 36385230](https://pubmed.ncbi.nlm.nih.gov/36385230/)) — i.e., toxicity is not due to loss of dismutase activity. Different variants produce distinct aggregate "strains" (strain A for most mutants and WT; strain B additionally in D90A) ([PMID: 40450581](https://pubmed.ncbi.nlm.nih.gov/40450581/)).

**Modifier genes.** Wild-type SOD1 itself acts as a modifier: "hSOD1WT has high capacity to coaggregate with mutants and enhance neurotoxicity," and coexpression differences may explain the recessive inheritance of D90A ([PMID: 40450581](https://pubmed.ncbi.nlm.nih.gov/40450581/)). TDP-43 can cross-seed SOD1 misfolding ([PMID: 38522514](https://pubmed.ncbi.nlm.nih.gov/38522514/)). For A4V, no closely linked modifier gene was found ([PMID: 18055113](https://pubmed.ncbi.nlm.nih.gov/18055113/)).

**Epigenetic / chromosomal.** No recurrent large-scale chromosomal abnormality defines ALS1 (single-gene disorder). Epigenetic contributions to ALS broadly are under study but are not established as ALS1-defining.

---

## Section 5 — Environmental Information

**Environmental factors.** Heavy metals, agricultural chemicals, electrical exposure, and chronic head trauma have modest associations with ALS risk and are hypothesized to act via oxidative stress ([PMID: 26515627](https://pubmed.ncbi.nlm.nih.gov/26515627/), [PMID: 23797033](https://pubmed.ncbi.nlm.nih.gov/23797033/)).

**Lifestyle factors.** Smoking (most consistent), excessive physical exertion/professional sports, and possibly certain diets are "modestly associated with ALS risk, with a stronger association between risk and smoking" ([PMID: 23797033](https://pubmed.ncbi.nlm.nih.gov/23797033/)).

**Infectious agents.** Not applicable — ALS1 is a genetic (non-infectious) disorder.

---

## Section 6 — Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. **Germline *SOD1* missense mutation** (e.g., A4V, G93A, D90A) → produces a structurally destabilized SOD1 protein while (for D90A) retaining normal enzymatic activity — establishing a **gain-of-function**, not loss-of-function, lesion ([PMID: 36385230](https://pubmed.ncbi.nlm.nih.gov/36385230/)).
2. Destabilized SOD1 → **misfolds into neurotoxic, aggregation-prone conformers** ([PMID: 41702846](https://pubmed.ncbi.nlm.nih.gov/41702846/)).
3. Misfolded SOD1 → **self-templates and seeds further misfolding (prion-like propagation)**; adult mice injected with G93A/G85R seeding homogenates "developed accelerated motor neuron disease" ([PMID: 41702846](https://pubmed.ncbi.nlm.nih.gov/41702846/); [PMID: 32958236](https://pubmed.ncbi.nlm.nih.gov/32958236/)).
4. Aggregates → **released from motor neurons and transmitted to naïve neurons** (P2X7-receptor–mediated release) → spreading pathology cell-to-cell ([PMID: 35478453](https://pubmed.ncbi.nlm.nih.gov/35478453/)).
5. In parallel (branch), mutant SOD1 expressed in **astrocytes, microglia, muscle and T cells** → drives **non-cell-autonomous neuroinflammation** ([PMID: 25613506](https://pubmed.ncbi.nlm.nih.gov/25613506/)); reactive astrocytes upregulate BMP4 and secrete toxic factors ([PMID: 29932880](https://pubmed.ncbi.nlm.nih.gov/29932880/)).
6. Aggregation + oxidative stress + neuroinflammation → vulnerable **alpha motor neurons transition into a conserved "disease-associated motor neuron" (DM) state** preceding death; the human orthologs of these regulatory regions are "enriched for ALS genetic risk variants" ([PMID: 42335888](https://pubmed.ncbi.nlm.nih.gov/42335888/)).
7. DM-state motor neurons → **die** (apoptosis/degeneration) → denervation of neuromuscular junctions → **muscle weakness, atrophy, paralysis**.
8. Progressive motor neuron loss reaches respiratory motor pools → **respiratory failure and death** ([PMID: 40328546](https://pubmed.ncbi.nlm.nih.gov/40328546/)).

```
SOD1 mutation ──> misfolded SOD1 (gain of function)
       │                 │
       │        prion-like templated aggregation
       │                 │
       │        cell-to-cell spread (P2X7 release)
       │                 │
       ├──> glia/muscle/T-cell toxicity (non-cell-autonomous) ──┐
       │                 │                                        │
       └────────────> DM motor-neuron state ────────────────────>┤
                              │                                    │
                     motor neuron death <── oxidative stress + neuroinflammation
                              │
                 NMJ denervation → weakness/atrophy/paralysis
                              │
                    respiratory failure → death
```

**Molecular pathways & processes.** Oxidative stress (Fenton-like ·OH generation by mutant SOD1) coupled to neuroinflammation; impaired proteostasis (the heat-shock response is protective — histamine/histidine induce Hsp70/GRP78 and rescue neurons in G93A mice, [PMID: 31382568](https://pubmed.ncbi.nlm.nih.gov/31382568/)); BMP4–Smad1/5/8 and p38 MAPK glial signaling ([PMID: 29932880](https://pubmed.ncbi.nlm.nih.gov/29932880/)); and protein citrullination (PAD2) contributing to neuroinflammation ([PMID: 42282797](https://pubmed.ncbi.nlm.nih.gov/42282797/)).

**Protein dysfunction.** Misfolding, oligomerization, and amyloid-like aggregation of SOD1; toxic oligomers are a therapeutic target ([PMID: 31017342](https://pubmed.ncbi.nlm.nih.gov/31017342/)). SOD1 also cross-seeds with TDP-43 ([PMID: 38522514](https://pubmed.ncbi.nlm.nih.gov/38522514/)).

**Aggregation pathology proportions.** Across ALS, "the most prevalent aggregation pathology is that of wild-type TDP-43 (97% of cases), with the remaining split between mutant forms of SOD1 (~2%) and FUS (~1%)" ([PMID: 32958236](https://pubmed.ncbi.nlm.nih.gov/32958236/)).

**Molecular profiling.** Single-nucleus RNA-seq/ATAC + spatial transcriptomics of SOD1-G93A mice defined the DM state, validated in human ALS spinal cord ([PMID: 42335888](https://pubmed.ncbi.nlm.nih.gov/42335888/)). Plasma/CSF proteomics identifies NEFL, TNFRSF12A, EDA2R, FABP4 with enrichment for immune-response and extracellular-matrix remodeling pathways ([PMID: 42698373](https://pubmed.ncbi.nlm.nih.gov/42698373/)).

**Suggested ontology terms.** GO:0006979 (response to oxidative stress); GO:0006954 (inflammatory response); GO:0043065 (positive regulation of apoptotic process); GO:0006457 (protein folding); GO:0034976 (response to ER stress). Cell types: CL:0000100 (motor neuron); alpha motor neuron; CL:0000127 (astrocyte); CL:0000129 (microglial cell); CL:0000084 (T cell).

---

## Section 7 — Anatomical Structures Affected

**Organ / system level.** Central and peripheral **nervous system** (motor); secondary **respiratory system** (diaphragm/intercostal denervation → respiratory failure, the terminal event, [PMID: 40328546](https://pubmed.ncbi.nlm.nih.gov/40328546/)); **musculoskeletal system** (neurogenic muscle atrophy).

**Tissue / cell level.** Degeneration of **upper motor neurons** (motor cortex, corticospinal tracts) and **lower motor neurons** (brainstem, spinal cord anterior horn). In homozygous D90A, pathology extends beyond motor pathways: "In addition to degeneration of the corticospinal tracts, all patients had degeneration of the dorsal columns," plus frontotemporal/insular gliosis, and "numerous small granular inclusions immunoreactive for misfolded SOD1 in motor neurons and glial nuclei in the spinal cord and brainstem" ([PMID: 36385230](https://pubmed.ncbi.nlm.nih.gov/36385230/)). Non-neuronal contributors: astrocytes, microglia, skeletal muscle, T cells ([PMID: 25613506](https://pubmed.ncbi.nlm.nih.gov/25613506/)).

**Subcellular level.** Cytoplasmic SOD1 aggregates/inclusions; mitochondrial dysfunction and oxidative injury; ER stress. GO cellular components: GO:0005739 (mitochondrion); GO:0005737 (cytoplasm); GO:0005783 (endoplasmic reticulum); GO:0016234 (inclusion body).

**Localization / lateralization.** Anatomical sites (UBERON): UBERON:0002240 (spinal cord); UBERON:0001896-related (medulla/brainstem); UBERON:0001384 (primary motor cortex); UBERON:0001134 (skeletal muscle tissue). Onset is typically **focal and asymmetric**, spreading contiguously to become **bilateral**; SOD1 frequently shows lower-limb–onset ([PMID: 42265995](https://pubmed.ncbi.nlm.nih.gov/42265995/)).

---

## Section 8 — Temporal Development

**Onset.** Adult-onset typically (mean sporadic ALS onset 58–63 yr; familial/SOD1 often earlier), with juvenile cases documented (onset 15–16 yr) ([PMID: 42265995](https://pubmed.ncbi.nlm.nih.gov/42265995/)). Onset pattern is **insidious**, focal, and asymmetric.

**Progression — strongly variant-dependent.**

| SOD1 variant | Inheritance | Course | Median survival |
|---|---|---|---|
| A4V (p.Ala5Val) | Dominant | Rapid | ~1.4 yr from onset ([PMID: 18055113](https://pubmed.ncbi.nlm.nih.gov/18055113/)) |
| Other dominant variants | Dominant | Variable | ~3–5 yr ([PMID: 18055113](https://pubmed.ncbi.nlm.nih.gov/18055113/)) |
| D90A (homozygous) | Recessive | Slow, stereotypic | Prolonged ([PMID: 36385230](https://pubmed.ncbi.nlm.nih.gov/36385230/)) |
| p.Asp125Gly (juvenile) | Dominant, incomplete penetrance | Rapid over months | Short ([PMID: 42265995](https://pubmed.ncbi.nlm.nih.gov/42265995/)) |

A4V carriers "share a common phenotype with rapid disease progression and death on average occurring at 1.4 years (versus 3-5 years with other dominant SOD1 mutations)" ([PMID: 18055113](https://pubmed.ncbi.nlm.nih.gov/18055113/)).

**Overall ALS course.** Population registry: median survival **2.5 years from symptom onset and 1.5 years from diagnosis; 12% survive ≥10 years** ([PMID: 42661170](https://pubmed.ncbi.nlm.nih.gov/42661170/)). Disease course is **progressive**, chronic, and (untreated) uniformly fatal.

**Patterns / critical periods.** No spontaneous remission. Tofersen can induce a treatment-related "chronic nonprogressive" state in some SOD1 carriers ([PMID: 41670738](https://pubmed.ncbi.nlm.nih.gov/41670738/)). Presymptomatic disease "is not uniformly clinically silent," representing a prodromal window with rising NfL — a critical opportunity for intervention ([PMID: 37382103](https://pubmed.ncbi.nlm.nih.gov/37382103/)).

---

## Section 9 — Inheritance and Population

**Epidemiology (ALS overall).** Incidence ~1.5–2.7 per 100,000/year; prevalence ~4–6 per 100,000 in European/North American populations; lifetime risk ~1 in 300–400; worldwide distribution is "far from uniform" ([PMID: 38870925](https://pubmed.ncbi.nlm.nih.gov/38870925/)). SOD1-ALS = ~2% of all ALS, ~12–20% of familial ALS ([PMID: 41661214](https://pubmed.ncbi.nlm.nih.gov/41661214/), [PMID: 18055113](https://pubmed.ncbi.nlm.nih.gov/18055113/)); SOD1 mutations are found in 2–6% of ALS patients overall ([PMID: 36385230](https://pubmed.ncbi.nlm.nih.gov/36385230/)).

**Inheritance.** Predominantly **autosomal dominant**; D90A "heredity is usually recessive" ([PMID: 36385230](https://pubmed.ncbi.nlm.nih.gov/36385230/)). Rare AR ALS involves other genes ([PMID: 41592170](https://pubmed.ncbi.nlm.nih.gov/41592170/)).

**Penetrance / expressivity.** **Incomplete, age-dependent penetrance** — pathogenic p.Asp125Gly was "inherited from asymptomatic fathers" ([PMID: 42265995](https://pubmed.ncbi.nlm.nih.gov/42265995/)). Expressivity is variable (age of onset, site of onset, rate of progression differ even within a variant).

**Founder effects.** A4V — North American founder allele (~12,000 yr old, Asian origin) ([PMID: 18055113](https://pubmed.ncbi.nlm.nih.gov/18055113/)); D90A — Scandinavian founder haplotype. **Genetic anticipation** is not a feature (SOD1 is not a repeat-expansion gene).

**Population demographics.** D90A enriched in Scandinavia; A4V in North America; sex ratio for ALS overall ~1.3–1.5:1 male:female; male sex is a risk factor ([PMID: 26515627](https://pubmed.ncbi.nlm.nih.gov/26515627/)).

---

## Section 10 — Diagnostics

**Clinical/electrophysiological diagnosis.** ALS is diagnosed clinically with electrophysiologic support. **Gold Coast criteria (GCC)** have the highest sensitivity: "GCC demonstrated higher sensitivity than rEEC and Awaji criteria: 0.96 (95% CI 0.93–0.98) versus 0.87 and 0.87"; specificity 0.68 (GCC) vs 0.73 (rEEC) ([PMID: 42618698](https://pubmed.ncbi.nlm.nih.gov/42618698/)). Diagnosis requires combined upper- and lower-motor-neuron signs, progression, and exclusion of mimics.

**Electrophysiology & imaging.** EMG/nerve conduction studies are "most useful when interpreted by distribution rather than positivity alone"; MRI is "indispensable but not self-interpreting" — critical to exclude degenerative cervical myelopathy and other structural mimics ([PMID: 42625715](https://pubmed.ncbi.nlm.nih.gov/42625715/)).

**Biomarkers.** **Neurofilament light chain (NfL/NEFL)** is the leading biomarker: "NEFL was the most robust biomarker in plasma and CSF, alongside TNFRSF12A in plasma and CSF, EDA2R in plasma, and FABP4" ([PMID: 42698373](https://pubmed.ncbi.nlm.nih.gov/42698373/)); a protein risk-prediction model achieved ROC-AUC 0.72. Emerging inflammatory indices (elevated FGF2, systemic inflammatory response index/SIRI) correlate with severity and early progression ([PMID: 42682425](https://pubmed.ncbi.nlm.nih.gov/42682425/)).

**Genetic testing.** Confirmation of ALS1 is by **single-gene *SOD1* sequencing or ALS gene panels** (also covering C9ORF72, FUS, TARDBP). WES/WGS are used when panels are negative. Genetic testing is now clinically essential because it determines eligibility for tofersen.

**Differential diagnosis.** Degenerative cervical myelopathy, multifocal motor neuropathy, primary lateral sclerosis, spinal muscular atrophy, Kennedy disease, inclusion body myositis ([PMID: 42625715](https://pubmed.ncbi.nlm.nih.gov/42625715/)).

**Screening.** **Cascade genetic testing** of at-risk relatives in SOD1 families; presymptomatic monitoring of NfL enables timing of intervention ([PMID: 37382103](https://pubmed.ncbi.nlm.nih.gov/37382103/)).

---

## Section 11 — Outcome / Prognosis

**Survival & mortality.** Median survival **2.5 yr from symptom onset, 1.5 yr from diagnosis; 12% survive ≥10 yr** ([PMID: 42661170](https://pubmed.ncbi.nlm.nih.gov/42661170/)). Variant-specific: A4V ~1.4 yr vs 3–5 yr for other dominant variants ([PMID: 18055113](https://pubmed.ncbi.nlm.nih.gov/18055113/)). **Respiratory failure** is the cardinal terminal feature and usual cause of death ([PMID: 40328546](https://pubmed.ncbi.nlm.nih.gov/40328546/)).

**Prognostic factors.** Predictors of longer survival: "younger age, low progression rate, absence of FTD, long onset-to-diagnosis interval" ([PMID: 42661170](https://pubmed.ncbi.nlm.nih.gov/42661170/)). Military veteran status predicts poorer survival ([PMID: 42669596](https://pubmed.ncbi.nlm.nih.gov/42669596/)). **Prognostic biomarker:** NfL (higher = faster progression) ([PMID: 42698373](https://pubmed.ncbi.nlm.nih.gov/42698373/)).

**Morbidity & QoL.** Progressive disability across mobility, speech, swallowing, and respiration; high symptom burden; early palliative care recommended ([PMID: 42652396](https://pubmed.ncbi.nlm.nih.gov/42652396/)).

**Recovery.** Historically none; however, tofersen has produced "chronic nonprogressive ALS, a phenotype not previously observed" with CSF NfL normalization and some motor recovery in SOD1 (p.Gly94Ser) carriers ([PMID: 41670738](https://pubmed.ncbi.nlm.nih.gov/41670738/)).

---

## Section 12 — Treatment

**Approved pharmacotherapy.** "The US FDA has approved four drugs for use in delaying the progression of amyotrophic lateral sclerosis: riluzole, edaravone, AMX0035, and tofersen... AMX0035 has been voluntarily withdrawn from both the US and Canadian markets" ([PMID: 40364643](https://pubmed.ncbi.nlm.nih.gov/40364643/)).

| Drug | Class / mechanism | NCIT (suggested) | Note |
|---|---|---|---|
| **Riluzole** | Glutamate antagonist / anti-excitotoxic | NCIT:C1289 | Standard of care; modest survival benefit |
| **Edaravone** | Free-radical scavenger / antioxidant | NCIT:C65331 | Slows decline in a subset; narrow eligibility |
| **AMX0035** (sodium phenylbutyrate–taurursodiol) | Proteostasis / ER-stress modulator | — | Withdrawn after confirmatory Phase III failure |
| **Tofersen** | Intrathecal SOD1 antisense oligonucleotide | NCIT (antisense oligonucleotide therapy) | First gene-targeted ALS therapy; SOD1-specific |

**Tofersen (gene-targeted, ALS1-specific).** "Tofersen, an intrathecal antisense oligonucleotide designed to reduce SOD1 protein synthesis, is the first and only approved therapy for the treatment of ALS in adults who have a variant in the SOD1 gene" ([PMID: 41661214](https://pubmed.ncbi.nlm.nih.gov/41661214/)). It works by "targeted mRNA degradation" of mutant SOD1 ([PMID: 42173382](https://pubmed.ncbi.nlm.nih.gov/42173382/)). Pharmacodynamics: robust **plasma/CSF neurofilament lowering** ([PMID: 41850233](https://pubmed.ncbi.nlm.nih.gov/41850233/)); autopsy tissue confirms 45–84% SOD1 mRNA/protein reduction in lumbar spinal cord ([PMID: 42406382](https://pubmed.ncbi.nlm.nih.gov/42406382/)). VALOR Phase 3 (NCT02623699) randomized 108 participants (42 unique SOD1 variants) 2:1 tofersen vs placebo. Case series shows some carriers reach nonprogressive disease ([PMID: 41670738](https://pubmed.ncbi.nlm.nih.gov/41670738/)). Adverse events include meningeal/perivascular lymphocytic responses ([PMID: 42406382](https://pubmed.ncbi.nlm.nih.gov/42406382/)).

**Advanced/experimental therapeutics.** AAV-mediated SOD1 gene silencing extends survival in mouse models — e.g., "AAV9-mediated SOD1 suppression in motor neurons and astrocytes significantly improves motor function and extends survival" ([PMID: 39257530](https://pubmed.ncbi.nlm.nih.gov/39257530/)); intravenous engineered AAV9 vectors also suppress hSOD1 and extend survival ([PMID: 42350385](https://pubmed.ncbi.nlm.nih.gov/42350385/)). Adaptive platform trials (HEALEY) and precision/combination strategies are reshaping development ([PMID: 42666355](https://pubmed.ncbi.nlm.nih.gov/42666355/)).

**Supportive & rehabilitative.** Non-invasive ventilation (respiratory support, now standard, [PMID: 40328546](https://pubmed.ncbi.nlm.nih.gov/40328546/)), nutritional support/gastrostomy, physical/occupational/speech therapy, and early palliative care ([PMID: 42652396](https://pubmed.ncbi.nlm.nih.gov/42652396/)).

---

## Section 13 — Prevention

**Primary prevention.** No population-level primary prevention; the frontier is **presymptomatic pharmacological prevention** in SOD1 carriers. "The discovery that blood neurofilament light chain (NfL) level increases presymptomatically and may serve as a susceptibility biomarker, predicting timing of phenoconversion in some mutation carriers, has empowered the first-ever prevention trial in SOD1-ALS" ([PMID: 37382103](https://pubmed.ncbi.nlm.nih.gov/37382103/)). The **ATLAS trial (NCT04856982)** initiates tofersen in presymptomatic carriers upon NfL elevation.

**Secondary prevention.** NfL-based monitoring of at-risk carriers for early detection/phenoconversion timing ([PMID: 37382103](https://pubmed.ncbi.nlm.nih.gov/37382103/)).

**Tertiary prevention.** Respiratory support, nutrition, and multidisciplinary/palliative care to prevent complications and preserve function ([PMID: 40328546](https://pubmed.ncbi.nlm.nih.gov/40328546/), [PMID: 42652396](https://pubmed.ncbi.nlm.nih.gov/42652396/)).

**Genetic counseling & screening.** Cascade genetic testing and reproductive counseling (including PGT/prenatal options) for autosomal-dominant SOD1 families; incomplete penetrance complicates counseling ([PMID: 42265995](https://pubmed.ncbi.nlm.nih.gov/42265995/)).

**Immunization / public health.** Not applicable (non-infectious genetic disease).

---

## Section 14 — Other Species / Natural Disease

**Taxonomy & orthologs.** Human *SOD1* (NCBI Taxon 9606). Orthologs: mouse *Sod1* (Mus musculus, Taxon 10090), rat *Sod1* (Rattus norvegicus, Taxon 10116); SOD1 is highly evolutionarily conserved.

**Natural disease.** Naturally occurring adult-onset canine **degenerative myelopathy** is associated with an *SOD1* mutation and is considered a spontaneous large-animal ALS analog (OMIA resource). *Note: this specific cross-species detail was not independently verified within the current investigation's citation set and should be confirmed against OMIA/primary literature before ingestion.*

**Comparative biology.** The transgenic SOD1-G93A mouse recapitulates key human ALS features, and the disease-associated motor neuron (DM) state is **conserved between mouse and human** ("human orthologs of regions differentially accessible in SOD1-G93A mouse motor neurons were enriched for ALS genetic risk variants") ([PMID: 42335888](https://pubmed.ncbi.nlm.nih.gov/42335888/)).

**Transmission.** No zoonotic potential (genetic disease).

---

## Section 15 — Model Organisms

**Standard model.** The **SOD1-G93A transgenic mouse** is the canonical ALS1 model, reproducing progressive motor neuron loss, gliosis, paralysis, and premature death ([PMID: 42335888](https://pubmed.ncbi.nlm.nih.gov/42335888/), [PMID: 29495962](https://pubmed.ncbi.nlm.nih.gov/29495962/)).

**Other genetic models.** hSOD1-G85R, hSOD1-D90A (distinct aggregate strain B), and digenic hSOD1-G85R/WT and G85R/D90A mice used to dissect coaggregation and inheritance ([PMID: 40450581](https://pubmed.ncbi.nlm.nih.gov/40450581/)); transgenic SOD1 **rat** models (BMP4 studies, [PMID: 29932880](https://pubmed.ncbi.nlm.nih.gov/29932880/)); cellular models (NSC-34 motor-neuron line, primary microglia/astrocyte co-cultures) ([PMID: 35478453](https://pubmed.ncbi.nlm.nih.gov/35478453/), [PMID: 29495962](https://pubmed.ncbi.nlm.nih.gov/29495962/)); induced prion-like seeding models (intrathecal seeding homogenates) ([PMID: 41702846](https://pubmed.ncbi.nlm.nih.gov/41702846/)).

**Model characteristics & applications.** These models faithfully reproduce SOD1 gain-of-function toxicity, aggregation, non-cell-autonomous glial toxicity, and DM-state transitions, and serve as the platform for therapeutic testing (AAV gene silencing, ASOs, anti-inflammatory agents, heat-shock inducers) ([PMID: 39257530](https://pubmed.ncbi.nlm.nih.gov/39257530/), [PMID: 42350385](https://pubmed.ncbi.nlm.nih.gov/42350385/), [PMID: 31382568](https://pubmed.ncbi.nlm.nih.gov/31382568/)).

**Limitations.** SOD1 models capture only the ~2% SOD1 subtype and do **not** reproduce TDP-43 proteinopathy (the dominant pathology in 97% of human ALS), contributing to the well-documented translational gap in which preclinically effective drugs fail in Phase III ([PMID: 42666355](https://pubmed.ncbi.nlm.nih.gov/42666355/)).

**Resources.** MGI, IMSR, RGD, Cellosaurus, MMRRC.

---

## Mechanistic Model / Interpretation

ALS1 is best understood as a **toxic gain-of-function proteinopathy with prion-like spread and a non-cell-autonomous amplification loop**. The unifying evidence is that D90A — the world's most common SOD1 mutation — encodes a protein of normal enzymatic activity, so pathology cannot stem from lost dismutase function ([PMID: 36385230](https://pubmed.ncbi.nlm.nih.gov/36385230/)). Instead, mutation-driven **misfolding** ([PMID: 41702846](https://pubmed.ncbi.nlm.nih.gov/41702846/)) generates aggregation-prone conformers that **self-template** and **spread cell-to-cell** ([PMID: 32958236](https://pubmed.ncbi.nlm.nih.gov/32958236/), [PMID: 35478453](https://pubmed.ncbi.nlm.nih.gov/35478453/)). This explains the focal-onset, contiguous-spread clinical pattern. Simultaneously, mutant SOD1 in glia, muscle, and T cells creates a toxic microenvironment ([PMID: 25613506](https://pubmed.ncbi.nlm.nih.gov/25613506/)), which is why correcting multiple cell types (neurons + astrocytes) is more therapeutic than neurons alone ([PMID: 39257530](https://pubmed.ncbi.nlm.nih.gov/39257530/)). The convergent endpoint is a conserved **disease-associated motor neuron** transcriptional state that presages cell death ([PMID: 42335888](https://pubmed.ncbi.nlm.nih.gov/42335888/)), followed by NMJ denervation, paralysis, and respiratory failure.

This model is directly therapeutically actionable: because the toxic species is the mutant protein, **reducing its synthesis** (tofersen ASO, AAV silencing) is disease-modifying, lowering NfL and, in some patients, arresting progression ([PMID: 41661214](https://pubmed.ncbi.nlm.nih.gov/41661214/), [PMID: 41670738](https://pubmed.ncbi.nlm.nih.gov/41670738/)). Variant identity is the dominant prognostic modifier (A4V ~1.4 yr vs recessive D90A slow), reflecting differences in protein destabilization and aggregate strain propensity ([PMID: 18055113](https://pubmed.ncbi.nlm.nih.gov/18055113/), [PMID: 40450581](https://pubmed.ncbi.nlm.nih.gov/40450581/)).

---

## Evidence Base

| PMID | Contribution |
|---|---|
| [41661214](https://pubmed.ncbi.nlm.nih.gov/41661214/) | Long-term tofersen (VALOR); SOD1 = ~2% of ALS; tofersen first/only approved SOD1-ALS therapy |
| [18055113](https://pubmed.ncbi.nlm.nih.gov/18055113/) | A4V founder allele, ~1.4 yr survival; SOD1 ~20% of familial ALS; no linked modifier |
| [36385230](https://pubmed.ncbi.nlm.nih.gov/36385230/) | D90A = most common worldwide; normal enzymatic activity → proves gain-of-function; dorsal-column pathology |
| [41850233](https://pubmed.ncbi.nlm.nih.gov/41850233/) | Tofersen lowers plasma neurofilament (PD biomarker) |
| [41670738](https://pubmed.ncbi.nlm.nih.gov/41670738/) | Tofersen → chronic nonprogressive ALS phenotype |
| [42698373](https://pubmed.ncbi.nlm.nih.gov/42698373/) | NEFL most robust biomarker; proteomic risk model AUC 0.72 |
| [42661170](https://pubmed.ncbi.nlm.nih.gov/42661170/) | Registry survival: median 2.5 yr from onset; 12% ≥10 yr; predictors |
| [42335888](https://pubmed.ncbi.nlm.nih.gov/42335888/) | Disease-associated motor neuron (DM) state; conserved mouse↔human |
| [41702846](https://pubmed.ncbi.nlm.nih.gov/41702846/) | Misfolding gain-of-function; prion-like seeding in vivo |
| [32958236](https://pubmed.ncbi.nlm.nih.gov/32958236/) | Aggregation pathology proportions (TDP-43 97% / SOD1 ~2% / FUS ~1%); prion-like mechanism |
| [40364643](https://pubmed.ncbi.nlm.nih.gov/40364643/) | Four FDA-approved drugs; AMX0035 withdrawn |
| [42265995](https://pubmed.ncbi.nlm.nih.gov/42265995/) | Juvenile SOD1 (p.Asp125Gly); lower-limb LMN onset; incomplete penetrance |
| [26515627](https://pubmed.ncbi.nlm.nih.gov/26515627/) | Genetics ~20% (10% familial); environmental risk factor list |
| [42669596](https://pubmed.ncbi.nlm.nih.gov/42669596/) | Military service predicts poorer ALS survival |
| [42618698](https://pubmed.ncbi.nlm.nih.gov/42618698/) | Gold Coast criteria sensitivity 0.96 |
| [38870925](https://pubmed.ncbi.nlm.nih.gov/38870925/) | Non-uniform worldwide ALS distribution |
| [40328546](https://pubmed.ncbi.nlm.nih.gov/40328546/) | Respiratory involvement cardinal terminal feature |
| [25613506](https://pubmed.ncbi.nlm.nih.gov/25613506/) | Non-cell-autonomous mechanism (microglia/astrocytes/muscle/T cells) |
| [39257530](https://pubmed.ncbi.nlm.nih.gov/39257530/) | AAV9 SOD1 suppression in neurons+astrocytes improves survival |
| [37382103](https://pubmed.ncbi.nlm.nih.gov/37382103/) | Presymptomatic NfL; first ALS prevention trial (ATLAS) |
| [42173382](https://pubmed.ncbi.nlm.nih.gov/42173382/) | Tofersen mechanism (mutant SOD1 mRNA degradation) |
| [40450581](https://pubmed.ncbi.nlm.nih.gov/40450581/) | WT SOD1 coaggregation; aggregate strains; D90A recessivity |
| [42406382](https://pubmed.ncbi.nlm.nih.gov/42406382/) | Tofersen CNS distribution; 45–84% SOD1 reduction in human autopsy |
| [42666355](https://pubmed.ncbi.nlm.nih.gov/42666355/) | Precision medicine, platform trials, translational gaps |

---

## Limitations and Knowledge Gaps

1. **SOD1 is a small minority of ALS (~2%).** Findings from SOD1 models may not generalize to the 97% TDP-43-driven majority; the SOD1 mouse does not model TDP-43 proteinopathy ([PMID: 42666355](https://pubmed.ncbi.nlm.nih.gov/42666355/)).
2. **Some epidemiologic figures** (incidence/prevalence, sex ratio, mean onset age) are drawn from established background knowledge rather than variant-specific SOD1 registries; SOD1-specific incidence is not precisely quantified here.
3. **One citation (PMID:37382103) was flagged as a snippet mismatch** during verification; the presymptomatic-NfL/ATLAS claim should be re-verified against the primary abstract before database ingestion.
4. **Penetrance estimates are qualitative** ("incomplete, age-dependent"); quantitative age-specific penetrance curves per variant are not established here.
5. **Canine degenerative myelopathy / SOD1** and detailed OMIA cross-species data were not independently verified within this investigation's citation set.
6. **No original data analysis** was performed; the report synthesizes published literature (no primary datasets were provided).

---

## Proposed Follow-up Actions

1. **Verify flagged citation (PMID:37382103)** and source quantitative ATLAS design details and interim results from ClinicalTrials.gov (NCT04856982).
2. **Retrieve variant-specific penetrance and survival tables** from ClinVar/ClinGen and large SOD1 cohorts to populate genotype–phenotype annotations.
3. **Confirm cross-species natural disease** (canine degenerative myelopathy *SOD1*) via OMIA and primary literature; add NCBI Gene IDs for orthologs.
4. **Extract precise SOD1-ALS epidemiology** (population-specific carrier frequencies of A4V and D90A) from gnomAD and founder-population studies.
5. **Curate ontology mappings** (HPO frequency data, GO/CL/UBERON/NCIT/CHEBI IDs) into structured fields for knowledge-base ingestion.
6. **Track HEALEY platform and next-generation AAV/gene-editing programs** for updated therapeutic annotations.

---

*Report compiled from 5 investigation iterations, 14 confirmed findings, and 47 reviewed papers. Evidence types span human clinical (registries, trials, autopsy), model organism (SOD1 mouse/rat), in vitro (NSC-34, glial co-cultures), and computational/omics (snRNA-seq, proteomics).*


## Artifacts

- [OpenScientist final report](Amyotrophic_Lateral_Sclerosis_Type_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Amyotrophic_Lateral_Sclerosis_Type_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 38 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 23 |
| Quoted claims found in source | 18 |
| Quoted claims **not** found in source | 5 |
| References weighed for topical relevance | 38 |
| On topic | 27 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:25613506` *(abstract only)*: "about two-thirds of familial cases are triggered by mutations of four genes... C9ORF72, ... SOD1, FUS/TLS, TDP43"
  - closest text in source: "About two-third of familial cases are triggered by mutations of four genes that are chromosome 9 open reading frame 72 (C9ORF72), Cu/Zn superoxide dismutase (SOD1), fused in sarcoma/translocated in liposarcoma (FUS/TLS), TAR-DNA binding protein 43 (TDP43)"
- `PMID:32958236` *(abstract only)*: "developed accelerated motor neuron disease"
  - closest text in source: "ALS is characterized by the rapid and progressive degenerations of motor neurons in the spinal cord and motor cortex, resulting in paralysis of those who suffer from it"
- `PMID:42661170` *(abstract only)*: "younger age, low progression rate, absence of FTD, long onset-to-diagnosis interval"
  - closest text in source: "Multivariate statistics revealed that younger age, a low progression rate, the absence of frontotemporal dementia and a long interval between symptom onset and diagnosis were predictors of long survival"
- `PMID:40364643` *(abstract only)*: "The US FDA has approved four drugs for use in delaying the progression of amyotrophic lateral sclerosis: riluzole, edaravone, AMX0035, and tofersen... AMX0035 has been voluntarily withdrawn from both the US and Canadian markets"
  - closest text in source: "The US Food and Drug Administration has approved four drugs for use in delaying the progression of amyotrophic lateral sclerosis: riluzole, edaravone, AMX0035, and tofersen, with the latter being the most recent to receive approval"
- `PMID:39257530` *(abstract only)*: "AAV9-mediated SOD1 suppression in motor neurons and astrocytes significantly improves motor function and extends survival"
  - closest text in source: "Previously, we shown that AAV9-mediated superoxide dismutase 1 (SOD1) suppression in motor neurons and astrocytes significantly improves motor function and extends survival in ALS mouse models"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 25 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007103` (2 mentions) - the report calls it "MONDO"; MONDO calls it **amyotrophic lateral sclerosis type 1**
- `HP:0003323` (1 mention) - the report calls it "Clinical sign"; HP calls it **Progressive muscle weakness**
- `HP:0007340` (1 mention) - the report calls it "Symptom"; HP calls it **Lower limb muscle weakness**
- `HP:0002380` (1 mention) - the report calls it "Clinical sign"; HP calls it **Fasciculations**
- `HP:0001257` (1 mention) - the report calls it "Clinical sign"; HP calls it **Spasticity**
- `HP:0002093` (1 mention) - the report calls it "Clinical sign"; HP calls it **Respiratory insufficiency**
- `NCIT:C1289` (1 mention) - the report calls it "Glutamate antagonist / anti-excitotoxic"; NCIT calls it **Recombinant Interleukin-8**
- `NCIT:C65331` (1 mention) - the report calls it "Free-radical scavenger / antioxidant"; NCIT calls it **Cinnamon**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003202` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Skeletal muscle atrophy**, and lists "Muscle degeneration" among its other names
- `GO:0034976` (1 mention) - the report calls it "response to ER stress"; GO calls it **response to endoplasmic reticulum stress**, and lists "response to ER stress" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.