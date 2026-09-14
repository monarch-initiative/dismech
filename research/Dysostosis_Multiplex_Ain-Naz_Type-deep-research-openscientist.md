---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-07T17:02:26.522713'
end_time: '2026-09-07T17:50:17.592465'
duration_seconds: 2871.07
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dysostosis Multiplex, Ain-Naz Type
  mondo_id: MONDO:0859156
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
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 17
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 9
  quotes_valid: 9
  relevance_assessed: 17
  on_topic: 13
  validator_version: 0.2.1
term_validation:
  total_terms: 34
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 6
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0859156
    reported_labels:
    - MONDO
    ontology_label: dysostosis multiplex, Ain-Naz type
  - term_id: HP:0000943
    reported_labels:
    - Core (all)
    ontology_label: Dysostosis multiplex
  - term_id: HP:0004322
    reported_labels:
    - Core (all)
    ontology_label: Short stature
  - term_id: HP:0001538
    reported_labels:
    - Frequent
    ontology_label: Protuberant abdomen
  - term_id: HP:0001629
    reported_labels:
    - 1 patient
    ontology_label: Ventricular septal defect
  - term_id: HP:0003128
    reported_labels:
    - Where tested
    ontology_label: Lactic acidosis
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Dysostosis_Multiplex_Ain-Naz_Type-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Dysostosis_Multiplex_Ain-Naz_Type-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dysostosis Multiplex, Ain-Naz Type
- **MONDO ID:** MONDO:0859156 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dysostosis Multiplex, Ain-Naz Type** covering all of the
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

# Dysostosis Multiplex, Ain-Naz Type (DMAN): A Comprehensive Disease Report

**Disease:** Dysostosis Multiplex, Ain-Naz Type (DMAN)
**MONDO ID:** MONDO:0859156 | **OMIM:** #619345 | **MedGen:** C5444223
**Causal gene:** *LYSET* (formerly *TMEM251*; alias *GCAF*) — HGNC:20218, 14q32.12
**Category:** Mendelian, autosomal recessive lysosomal storage disorder (mucolipidosis-like)

---

## Summary

Dysostosis Multiplex, Ain-Naz Type (DMAN) is an **ultra-rare, autosomal-recessive skeletal dysplasia** caused by **biallelic loss-of-function variants in *LYSET*** (formerly *TMEM251*, alias *GCAF*), a small Golgi-resident two-transmembrane protein. The disease was first defined in 2020–2021 by whole-exome sequencing of two unrelated consanguineous families, and the clinical picture is that of a **mucopolysaccharidosis (MPS)-like dysostosis multiplex** with extreme short stature (−8 to −11 SD), progressively coarse facial features, protruding abdomen, progressive skeletal deformity, loss of mobility, and premature death (two oldest reported patients died in their twenties; one child died at age 5).

Mechanistically, DMAN is a **mannose-6-phosphate (M6P) pathway disorder** that is biochemically and clinically convergent with **mucolipidosis II/III (I-cell disease)**. LYSET is required to stabilize and retain **GlcNAc-1-phosphotransferase (GNPT)** in the *cis*-Golgi. When LYSET is lost, GNPT — which has a hydrophilic transmembrane domain — becomes unstable and is mislocalized from the Golgi to the lysosome. This abolishes **M6P tagging** of the ~60 soluble lysosomal hydrolases, so these enzymes are **hyper-secreted into plasma rather than trafficked to lysosomes**, producing an intracellular lysosomal-storage state. The result is the classic "I-cell" biochemical signature: **elevated lysosomal enzymes in plasma, reduced enzymes in fibroblasts**, and abnormal urinary glycosaminoglycans and sialic acid. For this reason, functional groups have proposed the alternative disease names **"LYSET-related mucolipidosis"** and **"Mucolipidosis Type V,"** and classify the disorder among the **"Golgipathies."**

There is **no disease-specific cure**. Management is supportive, and candidate disease-modifying strategies are extrapolated from mucolipidosis II research: hematopoietic stem cell transplantation (partial biochemical benefit but skeletal/airway disease progresses), bisphosphonates (zoledronic acid partially restored hydrolase activity and reduced storage in an MLII mouse model), enzyme cross-correction using M6P-tagged supernatant, and variant-specific ASO exon-skipping. A **zebrafish *tmem251/lyset* knockout** phenocopies mucolipidosis II (heart edema, skeletal dysplasia) and serves as the principal validated animal model.

---

## Section 1 — Disease Information

**Overview.** DMAN is a Mendelian, autosomal-recessive skeletal dysplasia resembling a mucopolysaccharidosis. Affected individuals present in infancy/early childhood with severe short stature, progressively coarse ("gargoyle-like") facies, protruding abdomen, and a radiographic pattern of **dysostosis multiplex**, with progressive skeletal deformity and loss of mobility ([PMID: 33252156](https://pubmed.ncbi.nlm.nih.gov/33252156/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0859156 |
| OMIM (phenotype) | #619345 (Dysostosis Multiplex, Ain-Naz Type) |
| OMIM (gene) | *619332 (*LYSET*/*TMEM251*) |
| MedGen | C5444223 |
| Gene / HGNC | *LYSET* (TMEM251), HGNC:20218 |
| Ensembl | ENSG00000153485 |
| UniProt | Q8N6I4 |
| ICD-10 / ICD-11 | No specific code; maps to skeletal dysplasia / lysosomal storage disorder categories |
| MeSH | No dedicated term; related to "Mucolipidoses," "Osteochondrodysplasias" |

**Synonyms / alternative names.**
- Dysostosis Multiplex, Ain-Naz Type (DMAN) — OMIM designation
- **LYSET-related mucolipidosis** (proposed; [PMID: 40171858](https://pubmed.ncbi.nlm.nih.gov/40171858/))
- **Mucolipidosis Type V** (proposed from zebrafish/functional work; [PMID: 36096887](https://pubmed.ncbi.nlm.nih.gov/36096887/))
- Severe skeletal dysplasia with extreme short stature, TMEM251-related

**Data source type.** Information is derived from **individual-patient reports** (aggregated across ~4 families / 6+ patients described worldwide), combined with **disease-level/mechanistic resources** (OMIM, functional cell-biology and CRISPR-screen studies). This is an ultra-rare disease with no registry-scale epidemiology.

---

## Section 2 — Etiology

**Primary cause (genetic).** DMAN is caused by **biallelic (homozygous or compound-heterozygous) loss-of-function variants in *LYSET*/*TMEM251***. The founding report identified two homozygous variants in two unrelated consanguineous families: **c.133C>T; p.(Arg45Trp)** (missense) and **c.215dupA; p.(Tyr72Ter)** (frameshift/nonsense) ([PMID: 33252156](https://pubmed.ncbi.nlm.nih.gov/33252156/)):

> "Whole-exome sequencing identified two homozygous variants c.133C>T; p.(Arg45Trp) and c.215dupA; p.(Tyr72Ter), respectively, in the two families, affecting an evolutionary conserved gene TMEM251 (NM_001098621.1)."

**Genetic risk factors.** The only established risk factor is **inheritance of two pathogenic *LYSET* alleles**. **Consanguinity** is a major contributing circumstance — the initial families were consanguineous, and subsequent patients (Iranian brothers) were also from consanguineous unions, consistent with a rare recessive founder/homozygosity pattern.

**Environmental risk factors.** None identified. This is a monogenic Mendelian disorder with no known environmental, toxic, infectious, occupational, lifestyle, dietary, age, or sex-based risk factors contributing to causation.

**Protective factors.** No genetic or environmental protective factors have been described. In principle, any residual GNPT activity (e.g., hypomorphic alleles) would be expected to attenuate severity, analogous to mucolipidosis III versus II, but this has not been formally demonstrated for *LYSET*.

**Gene–environment interactions.** None reported; DMAN penetrance appears driven entirely by genotype.

---

## Section 3 — Phenotypes

The core phenotype is an **MPS-like dysostosis multiplex** with early onset and progressive course ([PMID: 33252156](https://pubmed.ncbi.nlm.nih.gov/33252156/)):

> "affected individuals had a dysostosis multiplex-like skeletal dysplasia and severe short stature (<-8.5 SD). They manifested increasingly coarse facial features, protruding abdomens, and progressive skeletal changes, reminiscent of mucopolysaccharidosis. The patients gradually lost mobility and the two oldest affected individuals died in their twenties."

Additional documented features include craniosynostosis, kyphoscoliosis/scoliosis, hemivertebrae, hip subluxation/dislocation, dental abnormalities, and a ventricular septal defect (VSD) in one patient. The first Western (Brazilian) patient additionally had **valvular disease** (mitral/aortic valve thickening, tricuspid regurgitation), **hand contractures**, and **coarse facies from 5 months of age**; she died in 2018 from respiratory causes ([PMID: 41858182](https://pubmed.ncbi.nlm.nih.gov/41858182/)).

### Phenotype table with suggested HPO terms

| Phenotype | Type | Onset | Severity / Course | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Dysostosis multiplex | Physical / radiographic | Infancy/early childhood | Severe, progressive | Core (all) | HP:0000943 |
| Severe short stature (−8 to −11 SD) | Physical | Infancy | Severe, progressive | Core (all) | HP:0004322 |
| Progressive coarse facial features | Clinical sign | Infancy (from ~5 mo) | Severe, progressive | Core (all) | HP:0000280 |
| Protruding abdomen | Clinical sign | Childhood | Moderate | Frequent | HP:0001538 |
| Kyphoscoliosis / scoliosis | Physical | Childhood | Progressive | Frequent | HP:0002751 / HP:0002650 |
| Hemivertebrae | Skeletal | Congenital | — | Reported | HP:0002937 |
| Craniosynostosis | Skeletal | Congenital/infancy | — | Reported | HP:0001363 |
| Hip subluxation/dislocation | Skeletal | Childhood | Progressive | Reported | HP:0002827 |
| Loss of ambulation / joint contractures | Physical | Progressive | Severe | Frequent | HP:0002505 / HP:0002803 |
| Dental abnormalities | Physical | Childhood | — | Reported | HP:0000164 |
| Valvular heart disease (mitral/aortic thickening, TR) | Clinical sign | Childhood | Progressive | Reported | HP:0001654 |
| Ventricular septal defect | Structural | Congenital | — | 1 patient | HP:0001629 |
| Elevated plasma lysosomal enzymes | Lab abnormality | Congenital | — | Where tested | HP:0003128 |
| Abnormal urinary GAGs | Lab abnormality | Congenital | — | Where tested | Mucopolysacchariduria |
| Premature death | Outcome | 2nd–3rd decade (or childhood) | Fatal | Reported | HP:0001522 |

**Quality-of-life impact.** Severe. Progressive loss of mobility, marked short stature, skeletal deformity, cardiorespiratory involvement, and premature death impose profound functional impairment and dependency. No disease-specific QoL instrument (EQ-5D/SF-36/PROMIS) data exist for DMAN given its rarity.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *LYSET* / *TMEM251* (alias *GCAF*, *C14orf109*, *UPF0694*); HGNC:20218; gene OMIM *619332; locus **14q32.12** (Ensembl ENSG00000153485; GRCh38 chr14:93,184,951–93,188,463, plus strand). A processed pseudogene, *TMEM251P*, lies on chr5 within an *ADGRV1* intron.

**Gene product.** UniProt **Q8N6I4**: a **169-amino-acid** protein (long isoform, ~18.7 kDa, pI ≈ 8.4) containing a **DUF4583** domain (~aa 35–160) and **two transmembrane helices**, with recent experimental consensus that both N- and C-termini face the **cytosol** ([PMID: 39677738](https://pubmed.ncbi.nlm.nih.gov/39677738/)). Two splice isoforms exist.

**Pathogenic variant spectrum.** All reported disease alleles are **biallelic loss-of-function** (nonsense, frameshift, or a conserved-residue missense). Variants are classified **pathogenic/likely pathogenic** under ACMG/AMP criteria (null variants in a LoF-intolerant, conserved gene; segregation in consanguineous families; functional concordance with M6P-pathway loss). All are **germline**; no somatic disease association exists for this Mendelian condition.

| Variant (cDNA) | Protein | Type | Family / origin | Reference |
|---|---|---|---|---|
| c.133C>T | p.(Arg45Trp) | Missense | Family NMD02 (consanguineous) | [PMID: 33252156](https://pubmed.ncbi.nlm.nih.gov/33252156/) |
| c.215dupA | p.(Tyr72Ter) | Frameshift/nonsense | Family ID01 (consanguineous) | [PMID: 33252156](https://pubmed.ncbi.nlm.nih.gov/33252156/) |
| c.197dupA | frameshift | Frameshift | Two Iranian brothers | [PMID: 40171858](https://pubmed.ncbi.nlm.nih.gov/40171858/) |
| c.112C>T (NM_001098621.4) | p.(Gln38Ter) | Nonsense | Brazilian (first Western) patient | [PMID: 41858182](https://pubmed.ncbi.nlm.nih.gov/41858182/) |

**Allele frequency.** These variants are absent or ultra-rare in population databases (gnomAD), consistent with a severe recessive disorder. No common susceptibility alleles.

**Functional consequence.** **Loss of function** — destabilization/mislocalization of GNPT and global loss of M6P tagging (see Section 6).

**Modifier genes.** None formally established for DMAN. Mechanistically plausible modifiers within the same pathway include **GNPTAB/GNPTG** (the phosphotransferase subunits), **GOLPH3/GOLPH3L** (retain the LYSET–GNPT complex in the *cis*-Golgi; [PMID: 39587297](https://pubmed.ncbi.nlm.nih.gov/39587297/)), **MBTPS1/Site-1-Protease** (GNPT cleavage), and **M6PR/IGF2R** (receptor delivery).

**Epigenetic information / chromosomal abnormalities.** None reported. DMAN is a single-gene point/indel disorder; no methylation signature, large structural variant, aneuploidy, translocation, or CNV mechanism has been described.

---

## Section 5 — Environmental Information

Not applicable. DMAN is a purely genetic Mendelian disease. There are **no known environmental factors, lifestyle factors, or infectious agents** that cause or trigger it. (Of note, LYSET is separately required for entry of cathepsin-dependent viruses including SARS-CoV-2 — see Section 6 — but this is a property of the pathway, not an environmental cause of DMAN.)

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function variants in *LYSET*/*TMEM251*** result in absent or nonfunctional LYSET protein in the Golgi. *(demonstrated — [PMID: 33252156](https://pubmed.ncbi.nlm.nih.gov/33252156/))*
2. Loss of LYSET **destabilizes GlcNAc-1-phosphotransferase (GNPT)**, whose hydrophilic transmembrane domain requires LYSET for retention; GNPT is **mislocalized from the *cis*-Golgi to the lysosome** and fails to be properly cleaved by Site-1-Protease. *(demonstrated — [PMID: 36074822](https://pubmed.ncbi.nlm.nih.gov/36074822/), [PMID: 36074821](https://pubmed.ncbi.nlm.nih.gov/36074821/), [PMID: 39677738](https://pubmed.ncbi.nlm.nih.gov/39677738/))*
3. Loss of GNPT activity leads to **global loss of mannose-6-phosphate (M6P) tagging** of the ~60 soluble lysosomal hydrolases. *(demonstrated — [PMID: 36074821](https://pubmed.ncbi.nlm.nih.gov/36074821/))*
4. Untagged hydrolases are **not captured by M6P receptors**, so instead of being routed to the lysosome they are **hyper-secreted into the extracellular space / plasma**. *(demonstrated — elevated plasma enzymes: [PMID: 41858182](https://pubmed.ncbi.nlm.nih.gov/41858182/))*
5. Cells become **depleted of intracellular lysosomal enzymes** → impaired turnover of macropinocytic and autophagic cargoes → **accumulation of undigested substrate (glycosaminoglycans, sialylated glycoconjugates)** = a **lysosomal storage state ("I-cell"/inclusion-cell phenotype)**. *(demonstrated — [PMID: 36074822](https://pubmed.ncbi.nlm.nih.gov/36074822/))*
6. Storage in **chondrocytes, osteoblasts, fibroblasts, and cardiac/valvular tissue** disrupts bone/cartilage growth and connective-tissue homeostasis. *(inferred from MLII pathology + patient biochemistry)*
7. This produces the **clinical manifestations**: dysostosis multiplex, extreme short stature, coarse facies, valvular/cardiac disease, and progressive multisystem decline leading to premature death. *(demonstrated clinically — [PMID: 33252156](https://pubmed.ncbi.nlm.nih.gov/33252156/))*

```
LYSET LoF  →  GNPT destabilized/mislocalized  →  loss of M6P tagging
      │                                                   │
      │                                                   ▼
      │                       lysosomal hydrolases hyper-secreted to plasma
      │                                                   │
      ▼                                                   ▼
Golgi sorting defect  →  intracellular enzyme depletion  →  substrate storage
                                                            (GAGs, sialylglycans)
                                                                    │
                                                                    ▼
                              dysostosis multiplex, short stature, coarse facies,
                              valvular disease  →  progressive decline / early death
```

### Detail

**Molecular pathway.** The **mannose-6-phosphate (M6P) lysosomal enzyme-trafficking pathway** (KEGG/Reactome "lysosome"; N-glycan/M6P biosynthesis). LYSET was independently identified by genome-scale CRISPR and nutrient-selection screens as the key **regulator of the M6P pathway**, acting via GNPT ([PMID: 36074821](https://pubmed.ncbi.nlm.nih.gov/36074821/), [PMID: 36074822](https://pubmed.ncbi.nlm.nih.gov/36074822/)):

> "Without LYSET, GlcNAc-1-phosphotransferase was unstable because of a hydrophilic transmembrane domain. Consequently, LYSET-deficient cells were depleted of lysosomal enzymes and impaired in turnover of macropinocytic and autophagic cargoes." ([PMID: 36074822](https://pubmed.ncbi.nlm.nih.gov/36074822/))

> "LYSET deficiency resulted in global loss of M6P tagging and mislocalization of GlcNAc-1-phosphotransferase from the Golgi complex to lysosomes." ([PMID: 36074821](https://pubmed.ncbi.nlm.nih.gov/36074821/))

> "TMEM251 is a two-transmembrane protein indispensable for GNPT stability, cleavage by Site-1-Protease (S1P), and enzymatic activity." ([PMID: 39677738](https://pubmed.ncbi.nlm.nih.gov/39677738/))

**Cellular processes (GO).** Protein targeting to lysosome (GO:0006622 / GO:0007041), Golgi organization (GO:0007030), autophagy (GO:0006914), and defective substrate catabolism. LYSET interacts with **GOLPH3/GOLPH3L** and retromer to retain the LYSET–GNPT complex in the *cis*-Golgi ([PMID: 39587297](https://pubmed.ncbi.nlm.nih.gov/39587297/)).

**Protein dysfunction.** Loss of function at two levels: (i) loss of LYSET stabilizer function; (ii) consequent destabilization and mislocalization of GNPT. Upstream lesion = LYSET; downstream effectors = GNPT → all M6P-dependent hydrolases.

**Biochemical abnormalities.** The pathognomonic "I-cell" pattern was directly demonstrated in a DMAN/LYSET patient ([PMID: 41858182](https://pubmed.ncbi.nlm.nih.gov/41858182/)):

> "Nine enzymes showed increased levels in plasma, and seven showed decreased levels in fibroblasts. Abnormal sialic acid profile and GAGs (glycosaminoglycans) were detected in urine."

**Convergence with mucolipidosis II.** DMAN and MLII share the identical downstream defect ([PMID: 36074821](https://pubmed.ncbi.nlm.nih.gov/36074821/), [PMID: 36074822](https://pubmed.ncbi.nlm.nih.gov/36074822/)):

> "GlcNAc-1-phosphotransferase deficiency leads to the severe lysosomal storage disorder mucolipidosis II (MLII)." ([PMID: 36074821](https://pubmed.ncbi.nlm.nih.gov/36074821/))

> "LYSET represents a core component of the lysosomal enzyme trafficking pathway, underlies the pathomechanism for hereditary lysosomal storage disorders, and may represent a target to suppress metabolic adaptations in cancer." ([PMID: 36074822](https://pubmed.ncbi.nlm.nih.gov/36074822/))

MLII patients share the clinical hallmarks ([PMID: 33000604](https://pubmed.ncbi.nlm.nih.gov/33000604/)):

> "Patients with MLII alpha/beta present coarse facial features, cessation of statural growth, important skeletal manifestations, impaired neuromotor development and cardiorespiratory involvement."

**Pleiotropy of LYSET.** Beyond DMAN, LYSET is a hub with two additional, mechanistically-linked roles ([PMID: 36074821](https://pubmed.ncbi.nlm.nih.gov/36074821/), [PMID: 36074822](https://pubmed.ncbi.nlm.nih.gov/36074822/)):

> "We used genome-scale CRISPR screens to identify lysosomal enzyme trafficking factor (LYSET, also named TMEM251) as essential for infection by cathepsin-dependent viruses including severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2)." ([PMID: 36074821](https://pubmed.ncbi.nlm.nih.gov/36074821/))

> "Mammalian cells can generate amino acids through macropinocytosis and lysosomal breakdown of extracellular proteins, which is exploited by cancer cells to grow in nutrient-poor tumors." ([PMID: 36074822](https://pubmed.ncbi.nlm.nih.gov/36074822/))

**Suggested ontology terms.** GO biological process: GO:0006622 (protein targeting to lysosome), GO:0016192 (vesicle-mediated transport), GO:0006914 (autophagy). GO cellular component: GO:0005794 (Golgi apparatus), GO:0000139 (Golgi membrane), GO:0005764 (lysosome). CHEBI: mannose-6-phosphate, glycosaminoglycan. CL cell types: chondrocyte (CL:0000138), osteoblast (CL:0000062), fibroblast (CL:0000057).

---

## Section 7 — Anatomical Structures Affected

**Organ level.**
- **Primary:** Skeleton (bone and cartilage) — dysostosis multiplex, short stature, kyphoscoliosis, hip dysplasia, craniosynostosis (UBERON:0001474 bone; UBERON:0002418 cartilage).
- **Secondary:** Heart / cardiac valves (valvular thickening, tricuspid regurgitation, VSD, dilated-cardiomyopathy risk as in MLII; UBERON:0000948 heart, UBERON:0000946 cardiac valve); respiratory tract/airway (cause of death; airway distortion as in MLII); abdominal organs (protruding abdomen, possible organomegaly); teeth (UBERON:0001091); connective tissue broadly.
- **Body systems:** Musculoskeletal (primary), cardiovascular, respiratory.

**Tissue / cell level.** Connective tissue and cartilage are principally affected. Key storage-affected cell populations: **chondrocytes (CL:0000138)**, **osteoblasts (CL:0000062)**, and **fibroblasts (CL:0000057)** — the last directly shown to have reduced intracellular hydrolases and storage inclusions in patients.

**Subcellular level.** The **Golgi apparatus (GO:0005794 / GO:0000139)** is the site of the primary lesion; the **lysosome (GO:0005764)** is the site of pathological substrate accumulation. Autophagosomal cargo turnover is impaired.

**Localization / lateralization.** Skeletal involvement is **generalized and bilateral/symmetric** (a systemic storage disorder), as expected for a metabolic dysplasia rather than a focal malformation.

---

## Section 8 — Temporal Development

**Onset.** **Congenital/early-infantile.** Coarse facies documented from ~5 months of age; short stature and dysostosis evident in infancy/early childhood ([PMID: 41858182](https://pubmed.ncbi.nlm.nih.gov/41858182/), [PMID: 33252156](https://pubmed.ncbi.nlm.nih.gov/33252156/)). Onset pattern is **insidious and chronic-progressive**.

**Progression.** **Progressive** and lifelong. Skeletal changes worsen over time, patients "gradually lost mobility," and facial coarsening increases with age ([PMID: 33252156](https://pubmed.ncbi.nlm.nih.gov/33252156/)). No remission or relapsing-remitting pattern; the course is a monotonic decline.

**Disease duration / critical windows.** Chronic and ultimately fatal. Reported deaths: two oldest patients in their **twenties**; one child at **age 5**; the Brazilian patient died from respiratory causes. Any therapeutic window is presumed to be **early** (pre-symptomatic/early-symptomatic), by analogy to MLII, before irreversible skeletal and airway remodeling.

---

## Section 9 — Inheritance and Population

**Inheritance pattern.** **Autosomal recessive** (biallelic LoF), OMIM #619345.

**Penetrance / expressivity.** Penetrance appears **complete** in reported biallelic individuals; expressivity ranges from severe childhood death to survival into the twenties, indicating **variable expressivity** (partly variant-dependent — e.g., residual function of missense p.Arg45Trp vs. null alleles).

**Epidemiology.** **Ultra-rare.** Only ~4 families / 6+ patients are described worldwide; no prevalence or incidence figures are available. Prevalence is effectively unquantified (well below any registry threshold).

**Consanguinity / founder effects.** **Consanguinity is prominent** — the founding families and the Iranian sibling pair were consanguineous, consistent with rare recessive homozygosity. No broad founder allele is established; variants appear private to families.

**Carrier frequency.** Not established; expected to be extremely low given absence/ultra-rarity in gnomAD.

**Population demographics.** Reported patients span **Middle Eastern (consanguineous), Iranian, and Brazilian (first Western)** backgrounds ([PMID: 40171858](https://pubmed.ncbi.nlm.nih.gov/40171858/), [PMID: 41858182](https://pubmed.ncbi.nlm.nih.gov/41858182/)). **Sex ratio** appears balanced (both sexes affected); no age or geographic clustering beyond consanguineous populations.

---

## Section 10 — Diagnostics

**Biochemical/laboratory testing (the diagnostic key).** The disorder produces a **mucolipidosis-II-like biochemical signature**: multiple lysosomal hydrolases **elevated in plasma/serum** with **reduced activity in cultured fibroblasts/leukocytes**, plus **abnormal urinary glycosaminoglycans and sialic acid** ([PMID: 41858182](https://pubmed.ncbi.nlm.nih.gov/41858182/)):

> "Nine enzymes showed increased levels in plasma, and seven showed decreased levels in fibroblasts. Abnormal sialic acid profile and GAGs (glycosaminoglycans) were detected in urine."

**Imaging.** Skeletal survey (X-ray) shows **dysostosis multiplex** (radiographic hallmark). CT/MRI as needed for craniosynostosis, spine (kyphoscoliosis, hemivertebrae), and hips; echocardiography for valvular disease.

**Genetic testing (definitive).** **Molecular confirmation of biallelic *LYSET*/*TMEM251* variants.** Because DMAN mimics MLII/III, LYSET should be included on MLII/III-like differential panels ([PMID: 40171858](https://pubmed.ncbi.nlm.nih.gov/40171858/)):

> "We propose the term 'LYSET-related mucolipidosis' to describe this disorder and emphasize the importance of including LYSET in the genetic diagnostic panel for MLII/III-like presentations."

Recommended approach: **WES or WGS** (unbiased, first-line for undiagnosed skeletal dysplasia); **targeted panels** for mucolipidosis/dysostosis that include *GNPTAB*, *GNPTG*, and *LYSET*; **single-gene** *LYSET* testing when biochemistry is I-cell-like and a family variant is known. Chromosomal microarray/karyotype are **not informative** (no CNV/structural mechanism).

**Clinical criteria / differential diagnosis.** No formal consensus criteria exist. Diagnosis rests on the triad of (1) dysostosis multiplex + extreme short stature + coarse facies, (2) I-cell biochemistry, (3) biallelic *LYSET* variants. Key **differentials**: mucolipidosis II/III (*GNPTAB*/*GNPTG*), mucopolysaccharidoses (MPS I–VII; distinguished by specific enzyme deficiencies and urinary GAG patterns), oligosaccharidoses (α/β-mannosidosis, fucosidosis, sialidosis, galactosialidosis), and multiple sulfatase deficiency. LYSET testing distinguishes DMAN from GNPT-intrinsic MLII.

**Screening.** No newborn or population screening exists. **Cascade/carrier testing** of at-risk relatives in affected consanguineous families is appropriate once the familial variant is known.

---

## Section 11 — Outcome / Prognosis

**Prognosis is poor.** DMAN is **progressive and life-limiting**. Reported mortality: two oldest patients died in their **twenties**, one child at **age 5**, and the first Western patient died of **respiratory causes** ([PMID: 33252156](https://pubmed.ncbi.nlm.nih.gov/33252156/), [PMID: 41858182](https://pubmed.ncbi.nlm.nih.gov/41858182/)). No formal 5-/10-year survival statistics exist given the tiny cohort.

**Morbidity/function.** High disability: progressive **loss of ambulation**, severe short stature, skeletal deformity, and cardiorespiratory compromise. By analogy to MLII, **airway distortion (saber-sheath trachea, fixed narrowing)** and **cardiac/valvular disease (including dilated cardiomyopathy)** are major morbidity/mortality drivers ([PMID: 32270604](https://pubmed.ncbi.nlm.nih.gov/32270604/), [PMID: 33000604](https://pubmed.ncbi.nlm.nih.gov/33000604/)).

**Complications.** Recurrent respiratory infections/aspiration, airway obstruction, valvular heart disease/heart failure, and progressive orthopedic deformity.

**Prognostic factors.** Likely determined by **residual GNPT activity** (variant severity), extent of cardiorespiratory involvement, and age at diagnosis. No validated prognostic biomarkers exist, though plasma hydrolase levels and urinary GAG/sialic acid could serve as candidate biochemical monitors.

---

## Section 12 — Treatment

**There is no disease-specific or curative therapy for DMAN.** Management is **supportive/symptomatic**, and disease-modifying candidates are **extrapolated from mucolipidosis II** (mechanistically identical GNPT–M6P defect). NCIT-suggested intervention terms are noted below.

### Supportive / symptomatic care (standard of care)
Multidisciplinary management modeled on MLII: respiratory support (**CPAP**, antibiotics for infections/aspiration), cardiac management for valvular disease (**ACE inhibitor — captopril**; **diuretic — spironolactone**), orthopedic/spine care, nutrition, physical/occupational/speech therapy, and genetic counseling ([PMID: 41830382](https://pubmed.ncbi.nlm.nih.gov/41830382/)). *(NCIT: Supportive Care; ACE Inhibitor; Diuretic Therapy)*

### Candidate disease-modifying strategies (from MLII research)

| Strategy | Evidence (in MLII / model) | Key result | Reference |
|---|---|---|---|
| **Hematopoietic stem cell transplantation (HSCT)** | MLII patients | Sustained reduction of lysosomal storage and bone-metabolism markers; some motor/cognitive gains — **but skeletal disease progressed, airway distortion persisted, benefit unclear** | [PMID: 33505859](https://pubmed.ncbi.nlm.nih.gov/33505859/), [PMID: 37484777](https://pubmed.ncbi.nlm.nih.gov/37484777/), [PMID: 32270604](https://pubmed.ncbi.nlm.nih.gov/32270604/) |
| **Zoledronic acid (bisphosphonate)** | *Gnptab* p.R364X knock-in MLII **mouse** | Increased M6P-dependent and -independent luminal hydrolases; reduced GAG storage; improved bone density, cartilage, motor function, hepatomegaly, brain neuroinflammation | [PMID: 42320387](https://pubmed.ncbi.nlm.nih.gov/42320387/) |
| **Enzyme cross-correction** (M6PR/IGF2R double-KO supernatant supplying M6P-tagged enzymes) | MLII **fibroblasts/patient cells** | Restored lysosomal enzyme activity, reduced inclusion bodies, improved autophagy — proof of concept | [PMID: 42665096](https://pubmed.ncbi.nlm.nih.gov/42665096/) |
| **ASO exon-skipping (GNPTAB)** | MLII fibroblasts / HEK293T | Modest, variant-specific benefit; did **not** fully restore GlcNAc-PT activity | [PMID: 42310785](https://pubmed.ncbi.nlm.nih.gov/42310785/) |

**Direct evidence quotes.**
> "HSCT resulted in a sustained reduction of lysosomal storage und bone metabolism markers." ([PMID: 33505859](https://pubmed.ncbi.nlm.nih.gov/33505859/))

> "Zoledronic acid treatment increased both M6P-dependent and M6P-independent luminal hydrolases, and reduced glycosaminoglycan storage in MLII skin fibroblasts." ([PMID: 42320387](https://pubmed.ncbi.nlm.nih.gov/42320387/))

**Important caveat.** DMAN is a **trafficking (M6P-tagging) disorder, not a single-enzyme deficiency**, so conventional single-enzyme **enzyme replacement therapy is not applicable**; therapies must restore the tagging/trafficking machinery or supply pre-tagged enzymes (cross-correction). No genotype-guided pharmacogenomic protocol exists. *(NCIT: Bone Marrow/Stem Cell Transplantation; Bisphosphonate Therapy — Zoledronic Acid; Antisense Oligonucleotide Therapy; Gene Therapy [investigational].)*

---

## Section 13 — Prevention

- **Primary prevention:** Not applicable to disease occurrence in a conceived affected individual. At the population/family level, **genetic counseling** for consanguineous couples and **carrier/cascade testing** once a familial *LYSET* variant is identified are the principal preventive measures.
- **Reproductive options:** For couples with a known biallelic risk, **prenatal diagnosis** and **preimplantation genetic testing (PGT-M)** are options.
- **Secondary prevention:** Early diagnosis (biochemical + molecular) enables anticipatory management of cardiorespiratory and skeletal complications.
- **Tertiary prevention:** Proactive respiratory care (CPAP, infection prophylaxis), cardiac surveillance/echocardiography, and orthopedic monitoring to limit complications.
- **Immunization / public health / environmental interventions:** Not applicable (no infectious or environmental etiology). Routine childhood immunization and aggressive treatment of respiratory infections are prudent given airway vulnerability.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy / orthologs.** *LYSET/TMEM251* is **evolutionarily conserved** ([PMID: 33252156](https://pubmed.ncbi.nlm.nih.gov/33252156/)), with orthologs in mouse (*Tmem251*), zebrafish (*tmem251*), and other vertebrates. NCBI Taxon IDs of relevance: *Homo sapiens* (9606), *Mus musculus* (10090), *Danio rerio* (7955).
- **Natural disease in animals.** No **naturally occurring** *LYSET*-related disease has been reported in companion animals or wildlife (no OMIA entry noted). The related GNPT/M6P disorder mucolipidosis has veterinary analogues, but a spontaneous LYSET disorder is not documented.
- **Comparative biology.** The M6P pathway and the LYSET–GNPT interaction are conserved across vertebrates, so disease mechanisms are expected to translate; the zebrafish knockout recapitulates skeletal and cardiac pathology (Section 15).
- **Transmission / zoonosis.** Not applicable (genetic, non-transmissible).

---

## Section 15 — Model Organisms

**Zebrafish (*Danio rerio*) *tmem251/lyset* knockout — principal validated model.** In a genome-wide CRISPR screen, TMEM251 was identified as the first regulator of M6P modification; its deletion causes mistargeting of most lysosomal enzymes and accumulation of undigested material. Crucially, the whole-animal knockout **phenocopies mucolipidosis II** ([PMID: 36096887](https://pubmed.ncbi.nlm.nih.gov/36096887/)):

> "In zebrafish, TMEM251 deletion leads to severe developmental defects including heart edema and skeletal dysplasia, which phenocopies Mucolipidosis Type II."

> "We name TMEM251 as GNPTAB cleavage and activity factor (GCAF) and its related disease as Mucolipidosis Type V."

This model recapitulates the two most clinically important axes of DMAN — **skeletal dysplasia and cardiac disease** — making it valuable for mechanistic and preclinical therapeutic work. **Limitation:** developmental fish models may not capture the slowly progressive skeletal/airway remodeling and adult mortality seen in humans.

**Cellular / in vitro models.** Extensive: genome-scale CRISPR-knockout human cell lines that revealed the mechanism ([PMID: 36074821](https://pubmed.ncbi.nlm.nih.gov/36074821/), [PMID: 36074822](https://pubmed.ncbi.nlm.nih.gov/36074822/), [PMID: 36096887](https://pubmed.ncbi.nlm.nih.gov/36096887/), [PMID: 39587297](https://pubmed.ncbi.nlm.nih.gov/39587297/)); **patient-derived fibroblasts** demonstrating the I-cell biochemistry ([PMID: 41858182](https://pubmed.ncbi.nlm.nih.gov/41858182/)). These support functional-genomics, trafficking, and cross-correction studies.

**Mouse.** No dedicated *Lyset*/*Tmem251* DMAN mouse is reported here; however, the mechanistically identical ***Gnptab* p.R364X knock-in MLII mouse** is a directly relevant surrogate for testing pathway-restoring therapy (zoledronic acid) ([PMID: 42320387](https://pubmed.ncbi.nlm.nih.gov/42320387/)). A *Lyset* knockout mouse is an obvious high-value gap (see Follow-up).

**Model databases:** ZFIN (zebrafish), MGI/IMPC (mouse), Cellosaurus (patient fibroblast lines).

---

## Mechanistic Model / Interpretation

DMAN is best understood as a **"Golgipathy"** — a disease of the Golgi sorting machinery ([PMID: 36456556](https://pubmed.ncbi.nlm.nih.gov/36456556/)):

> "Association genetic studies and genome-scale CRISPR screens have recently identified ARF3 and TMEM251/LYSET/GCAF as Golgi-resident factors essential to brain and skeletal development."

The disease sits one step **upstream in the same pathway** as classic mucolipidosis II. Whereas MLII results from intrinsic loss of GNPT (the enzyme that writes the M6P tag), DMAN results from loss of **LYSET, the factor that keeps GNPT stable and correctly localized**. Both converge on the same endpoint — no M6P tag, no lysosomal delivery, hydrolase hyper-secretion, and intracellular storage — which is why DMAN is biochemically and clinically an "I-cell disease."

```
        MLII (classic)                     DMAN / LYSET-related ML ("MLV")
        ──────────────                     ──────────────────────────────
        GNPTAB/G mutation                  LYSET/TMEM251 mutation
              │                                     │
              ▼                                     ▼
        GNPT enzyme absent/inactive         GNPT destabilized & mislocalized
              └──────────────┬──────────────────────┘
                             ▼
              LOSS OF M6P TAGGING of ~60 hydrolases
                             ▼
              hydrolase hyper-secretion + intracellular storage
                             ▼
        dysostosis multiplex · short stature · coarse facies · valvular disease
```

This convergence is the **central actionable insight**: the substantial MLII research base (natural history, biomarkers, HSCT, bisphosphonates, cross-correction, ASOs) is directly transferable to DMAN, and DMAN patients should be managed and studied within the mucolipidosis framework.

---

## Evidence Base

| PMID | Contribution | Evidence type |
|---|---|---|
| [33252156](https://pubmed.ncbi.nlm.nih.gov/33252156/) | Founding report: biallelic *TMEM251* variants (p.Arg45Trp, p.Tyr72Ter); core phenotype & mortality | Human clinical / genetics |
| [36074821](https://pubmed.ncbi.nlm.nih.gov/36074821/) | LYSET essential for M6P tagging; GNPT mislocalization; viral-entry role | In vitro / CRISPR |
| [36074822](https://pubmed.ncbi.nlm.nih.gov/36074822/) | GNPT instability without LYSET; enzyme depletion; cancer nutrient scavenging | In vitro / CRISPR |
| [39677738](https://pubmed.ncbi.nlm.nih.gov/39677738/) | TMEM251 required for GNPT stability, S1P cleavage, activity; topology | In vitro / structural |
| [36096887](https://pubmed.ncbi.nlm.nih.gov/36096887/) | Zebrafish knockout phenocopies MLII; "GCAF"/"Mucolipidosis Type V" | Model organism |
| [40171858](https://pubmed.ncbi.nlm.nih.gov/40171858/) | Two Iranian brothers (c.197dupA); "LYSET-related mucolipidosis"; panel inclusion | Human clinical |
| [41858182](https://pubmed.ncbi.nlm.nih.gov/41858182/) | First Western patient (p.Gln38Ter); direct I-cell biochemistry | Human clinical / biochemistry |
| [33000604](https://pubmed.ncbi.nlm.nih.gov/33000604/) | MLII clinical overlap (coarse facies, growth arrest, cardiorespiratory) | Human clinical (MLII) |
| [36456556](https://pubmed.ncbi.nlm.nih.gov/36456556/) | Golgipathy classification | Review |
| [39587297](https://pubmed.ncbi.nlm.nih.gov/39587297/) | GOLPH3/GOLPH3L retain LYSET–GNPT in Golgi | In vitro |
| [33505859](https://pubmed.ncbi.nlm.nih.gov/33505859/) | HSCT partial benefit in MLII | Human clinical (MLII) |
| [42320387](https://pubmed.ncbi.nlm.nih.gov/42320387/) | Zoledronic acid restores hydrolases in MLII mouse | Model organism (MLII) |
| [42665096](https://pubmed.ncbi.nlm.nih.gov/42665096/) | M6PR/IGF2R dKO cross-correction of MLII cells | In vitro (MLII) |
| [42310785](https://pubmed.ncbi.nlm.nih.gov/42310785/) | GNPTAB ASO exon-skipping (modest) | In vitro (MLII) |
| [41830382](https://pubmed.ncbi.nlm.nih.gov/41830382/) | MLII symptomatic care (CPAP, captopril, spironolactone) | Human clinical (MLII) |
| [32270604](https://pubmed.ncbi.nlm.nih.gov/32270604/) | Airway distortion persists post-HSCT in MLII | Human clinical (MLII) |
| [37484777](https://pubmed.ncbi.nlm.nih.gov/37484777/) | HSCT outcomes in MLII (unclear benefit) | Human clinical (MLII) |

---

## Limitations and Knowledge Gaps

1. **Extremely small cohort.** Only ~4 families / 6+ patients are described; there are **no prevalence, incidence, survival, or QoL statistics**, and natural history is anecdotal.
2. **Genotype–phenotype correlation is undefined.** Whether the missense p.Arg45Trp retains residual function (milder course) versus null alleles is unproven.
3. **Therapeutics are entirely extrapolated from MLII.** No DMAN-specific trial or treatment outcome data exist; HSCT benefit is unclear even in MLII, and skeletal/airway disease progresses.
4. **No mammalian (mouse) DMAN model.** Preclinical therapy testing currently relies on zebrafish and on MLII (*Gnptab*) mouse surrogates.
5. **CNS/neurodevelopmental extent under-characterized.** MLII and related glycoproteinoses feature neurodevelopmental involvement; the neurodevelopmental burden in DMAN is not well quantified.
6. **No validated biomarkers** for monitoring disease progression or treatment response specific to DMAN.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a *Lyset*/*Tmem251* knock-in or conditional-knockout mouse** carrying a patient variant (e.g., p.Arg45Trp) to model progressive skeletal/cardiac disease and serve as a preclinical therapeutic platform.
2. **Test pathway-restoring therapies directly in LYSET-deficient systems:** zoledronic acid, and M6PR/IGF2R-dKO cross-correction supernatant, in patient-derived fibroblasts and the zebrafish knockout, to confirm transferability from MLII.
3. **Establish an international DMAN/LYSET registry** with standardized biochemical (plasma/fibroblast hydrolase panels, urinary GAG/sialic acid), radiographic, and cardiorespiratory phenotyping to build natural history and candidate biomarkers.
4. **Add *LYSET* to all mucolipidosis/dysostosis diagnostic gene panels** and reflex-test I-cell-biochemistry patients who are *GNPTAB/GNPTG*-negative, to find undiagnosed cases.
5. **Systematic genotype–function mapping** of *LYSET* variants (missense vs. null) using GNPT-stability and M6P-tagging readouts to predict severity and stratify future trials.
6. **Cardiorespiratory surveillance protocol** (serial echocardiography, airway imaging) developed for DMAN based on MLII experience, given these are the leading causes of death.

---

*Evidence source key: Human clinical/genetic (patient reports); Model organism (zebrafish; MLII mouse); In vitro (CRISPR screens, patient fibroblasts, cell lines); Review/computational. Where DMAN-specific data were unavailable, mechanistically identical mucolipidosis II evidence is clearly labeled as such.*


## Artifacts

- [OpenScientist final report](Dysostosis_Multiplex_Ain-Naz_Type-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Dysostosis_Multiplex_Ain-Naz_Type-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 9 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 17 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 13 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859156` (2 mentions) - the report calls it "MONDO"; MONDO calls it **dysostosis multiplex, Ain-Naz type**
- `HP:0000943` (1 mention) - the report calls it "Core (all)"; HP calls it **Dysostosis multiplex**
- `HP:0004322` (1 mention) - the report calls it "Core (all)"; HP calls it **Short stature**
- `HP:0001538` (1 mention) - the report calls it "Frequent"; HP calls it **Protuberant abdomen**
- `HP:0001629` (1 mention) - the report calls it "1 patient"; HP calls it **Ventricular septal defect**
- `HP:0003128` (1 mention) - the report calls it "Where tested"; HP calls it **Lactic acidosis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000280` (1 mention) - the report calls it "Core (all)"; HP calls it **Coarse facial features**, and lists "Coarse face" among its other names