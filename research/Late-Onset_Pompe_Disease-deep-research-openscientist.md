---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T10:43:21.355118'
end_time: '2026-09-01T11:04:16.178208'
duration_seconds: 1254.82
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Late-Onset Pompe Disease
  mondo_id: ''
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
citation_count: 52
reference_validation:
  total_references: 52
  verified: 52
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 52
  on_topic: 45
  validator_version: 0.2.1
term_validation:
  total_terms: 33
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 3
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0001638
    reported_labels:
    - Minor/mild cardiac involvement
    ontology_label: Cardiomyopathy
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
  path: Late-Onset_Pompe_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Late-Onset_Pompe_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Late-Onset Pompe Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Late-Onset Pompe Disease** covering all of the
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

# Late-Onset Pompe Disease (LOPD): Comprehensive Disease Characteristics Report

**Disease:** Late-Onset Pompe Disease (LOPD)
**Synonyms:** Glycogen storage disease type II (GSD-II), acid maltase deficiency (AMD), acid α-1,4-glucosidase deficiency, glycogenosis type II
**Category:** Mendelian, autosomal recessive lysosomal storage disorder
**Suggested MONDO ID:** MONDO:0009290 (Pompe disease); **OMIM:** 232300; **Gene:** *GAA* (HGNC:4065, 17q25.3)

---

## Summary

Late-Onset Pompe Disease (LOPD) is an autosomal-recessive lysosomal storage disorder caused by biallelic **partial** loss-of-function variants in the *GAA* gene, which encodes the lysosomal enzyme acid α-1,4-glucosidase (acid maltase). Residual enzyme deficiency leads to progressive intralysosomal glycogen accumulation, secondary failure of autophagy, and disruption of the contractile apparatus — preferentially in **type II (fast-twitch) skeletal and respiratory muscle fibers**. Unlike the infantile-onset form (IOPD), which is dominated by lethal hypertrophic cardiomyopathy, LOPD presents after the first year of life (childhood through late adulthood) as a **slowly progressive limb-girdle and axial myopathy with disproportionately early diaphragmatic/respiratory insufficiency and minimal cardiac involvement**. Respiratory failure is the leading cause of death.

The molecular hallmark is the "leaky" splice variant **c.-32-13T>G (IVS1)**, which appears in ~90% of Caucasian late-onset patients and permits low-level production of functional enzyme (hence a comparatively mild, adult phenotype and generally CRIM-positive immunological status). Diagnosis rests on demonstrating reduced GAA activity on a **dried blood spot** (fluorometry or FIA-MS/MS), confirmed by *GAA* sequencing, with urinary **glucose tetrasaccharide (Glc4/Hex4)** and serum creatine kinase (CK) as supporting biomarkers. Pseudodeficiency alleles (notably p.[G576S;E689K], common in East Asians) are an important cause of screening false positives.

Management centers on **enzyme replacement therapy (ERT)**. Three agents are now approved: alglucosidase alfa (>15 years standard of care), avalglucosidase alfa (enhanced bis-M6P mannose-6-phosphate uptake), and cipaglucosidase alfa co-administered with the chaperone miglustat. ERT modifies but does not halt the disease: respiratory and ambulatory function improve initially then decline gradually over 10–15 years. Next-generation ERTs show superiority signals over alglucosidase alfa in walk distance, lung function, biomarker normalization, and patient-reported outcomes. Multidisciplinary supportive care — respiratory support, supervised resistance/respiratory-muscle training, and high-protein nutrition — provides meaningful adjuvant benefit. Gene therapy (AAV-*GAA*) is in trials but has documented risks (dorsal-root-ganglion sensory neuronopathy).

---

## Section 1 — Disease Information

LOPD is a rare inherited neuromuscular glycogen storage disorder resulting from deficiency of the lysosomal enzyme acid α-glucosidase (GAA), which normally degrades lysosomal glycogen to glucose. When enzyme activity is only partially reduced and symptoms appear after 12 months of age, the condition is termed **late-onset** to distinguish it from the severe classic infantile form.

**Key identifiers (suggested):**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0009290 (Pompe disease) |
| OMIM | 232300 (Glycogen storage disease II) |
| Gene (HGNC) | *GAA*, HGNC:4065 |
| ICD-10 | E74.02 (Pompe disease) |
| MeSH | D006009 (Glycogen Storage Disease Type II) |
| Orphanet | ORPHA:308552 (late-onset form) / ORPHA:365 (GSD-II) |

**Synonyms/alternative names:** Glycogen storage disease type II (GSD-II), acid maltase deficiency, acid α-1,4-glucosidase deficiency, glycogenosis type II, adult/juvenile-onset Pompe disease.

Information is derived predominantly from **aggregated disease-level resources** — international patient registries (e.g., the International Pompe Registry, n=485), newborn screening cohorts, and randomized controlled trials — rather than from single-patient EHR data. LOPD is described in the literature as *"a rare autosomal recessive multisystemic disorder"* that substantially impacts daily activities and health-related quality of life ([PMID: 39535661](https://pubmed.ncbi.nlm.nih.gov/39535661/)).

---

## Section 2 — Etiology

**Primary cause (genetic):** LOPD is caused by biallelic pathogenic variants in *GAA* producing **partial** (rather than complete) loss of acid α-glucosidase function. The dominant late-onset allele is the intron-1 leaky splice variant **c.-32-13T>G**, which allows a small fraction of normally spliced transcript and thus residual enzyme. *"This splicing variant occurs in 90% of Caucasian late onset patients, and is associated with a broad range of symptom onset"* ([PMID: 30922962](https://pubmed.ncbi.nlm.nih.gov/30922962/)).

**Genetic risk/modifier factors:** The *cis* synonymous variant **c.510C>T** acts as a genetic modifier — *"c.510C>T is a genetic modifier in compound heterozygous and homozygous IVS1 patients"* — reducing residual wild-type splicing and lowering the age of onset ([PMID: 30922962](https://pubmed.ncbi.nlm.nih.gov/30922962/)). Rare variants in autophagy and non-autophagy genes have been proposed as additional disease modifiers explaining variable severity among patients sharing the same *GAA* genotype ([PMID: 33807278](https://pubmed.ncbi.nlm.nih.gov/33807278/)).

**Environmental/lifestyle risk factors:** No established environmental cause; this is a Mendelian disorder. Physical deconditioning may exacerbate weakness; conversely, structured exercise is protective of function (see Section 12). No infectious agents are involved.

**Protective factors:** The single most important "protective" genetic feature is the leaky c.-32-13T>G allele itself, whose residual enzyme production yields the milder late-onset phenotype. There are no established dietary or lifestyle protective factors that prevent disease, though high-protein diet and exercise mitigate functional decline.

**Gene–environment interactions:** Minimal. The main modifiable interaction is treatment (ERT) and supportive exercise/nutrition acting on the genetically determined enzyme deficiency.

---

## Section 3 — Phenotypes

LOPD is a **progressive proximal and axial myopathy with early respiratory involvement**. Key phenotypes, with suggested HPO terms and frequencies:

| Phenotype | HPO term (suggested) | Type | Frequency / notes |
|---|---|---|---|
| Limb-girdle / proximal muscle weakness | HP:0003701 (proximal muscle weakness) | Clinical sign | ~85% (limb-girdle phenotype 85.3%) |
| Respiratory / ventilatory insufficiency (diaphragm) | HP:0002093 (respiratory insufficiency); HP:0002878 | Clinical sign | ~61% |
| Axial / paraspinal weakness | HP:0003327 (axial muscle weakness) | Clinical sign | Common; early-degenerating |
| Elevated serum creatine kinase (hyperCKemia) | HP:0003236 | Lab abnormality | Common |
| Exercise intolerance / fatigue | HP:0003546; HP:0012378 | Symptom | Common |
| Minor/mild cardiac involvement | HP:0001638 | Clinical sign | Minor (contrast with IOPD) |
| Rigid spine / scoliosis | HP:0003306; HP:0002650 | Physical manifestation | Subset |

The most common clinical presentation in confirmed LOPD is *"a limb-girdle phenotype (85.3%) combined with ventilatory insufficiency (61%)"* ([PMID: 27170567](https://pubmed.ncbi.nlm.nih.gov/27170567/)). LOPD *"typically show[s] progressive muscle weakness, respiratory dysfunction and minor cardiac involvement"* — distinguishing it from IOPD ([PMID: 31811531](https://pubmed.ncbi.nlm.nih.gov/31811531/)).

**Characteristics:** onset ranges from childhood to late adulthood (age-of-onset HPO: HP:0003581 adult onset); severity variable; progression slow but relentless; respiratory failure often precedes loss of ambulation.

**Quality of life:** LOPD *"substantially impacts patients' day-to-day activities, outcomes, and health-related quality of life"* ([PMID: 39535661](https://pubmed.ncbi.nlm.nih.gov/39535661/)). Validated instruments used include PROMIS Physical Function/Fatigue, R-PAct (Pompe-specific activity), EQ-5D-5L, SF-36, and 6-minute walk distance.

---

## Section 4 — Genetic / Molecular Information

**Causal gene:** *GAA* (acid alpha-glucosidase), chromosome 17q25.3, HGNC:4065, OMIM 606800. LOPD is *"a rare autosomal recessive lysosomal disorder caused by loss-of-function of the [GAA gene]"* ([PMID: 40225932](https://pubmed.ncbi.nlm.nih.gov/40225932/)).

**Pathogenic variants:**

| Feature | Detail |
|---|---|
| Most common late-onset allele | c.-32-13T>G (IVS1), splice-site, "leaky" — ~90% of Caucasian LOPD |
| Genetic modifier | c.510C>T (cis synonymous), lowers age of onset |
| Variant classes | splice-site, missense, nonsense, frameshift/indels |
| Pseudodeficiency alleles | c.[1726G>A;2065G>A] p.[G576S;E689K] — ~4% homozygous in East Asians |
| Origin | germline (biallelic) |
| Functional consequence | loss of function (partial residual activity in LOPD) |

Variant classification follows ACMG/AMP criteria (pathogenic / likely pathogenic / VUS); ClinVar and HGMD are primary catalogs. In LOPD, at least one allele is typically the leaky c.-32-13T>G producing residual enzyme; pairing with a "null" second allele yields disease. Pseudodeficiency alleles reduce measured enzyme activity **without** causing disease and *"may present as false positives in newborn screening programs especially in Asian populations"* ([PMID: 18301443](https://pubmed.ncbi.nlm.nih.gov/18301443/)).

**Modifier genes/epigenetics:** Beyond c.510C>T, rare variants in autophagy-related genes have been proposed as modifiers ([PMID: 33807278](https://pubmed.ncbi.nlm.nih.gov/33807278/)). No established disease-specific DNA-methylation/histone signature. **Chromosomal abnormalities:** none characteristic.

---

## Section 5 — Environmental Information

LOPD is a **monogenic Mendelian disorder with no environmental, toxic, occupational, or infectious cause.** No lifestyle factor initiates disease. Physical activity and nutrition modulate *functional outcome* rather than disease occurrence (see Section 12). No infectious agents are implicated.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic partial-LoF *GAA* variants** (commonly c.-32-13T>G) → **reduced synthesis/activity of acid α-glucosidase** in the lysosome (demonstrated).
2. Deficient GAA → **failure to degrade lysosomal glycogen** → **progressive intralysosomal glycogen accumulation**, first in cardiac and skeletal muscle (demonstrated).
3. Glycogen-laden lysosomes swell and **rupture**, spilling glycogen and hydrolases into the cytoplasm; concurrently an **acidification defect** develops in a subset of late endosomes/lysosomes (demonstrated in Gaa-KO myoblasts).
4. In parallel (branch), **autophagy fails at the termination stage** — impaired autophagosome–lysosome fusion → massive **autophagic buildup** restricted to **type II-rich fibers** (demonstrated).
5. Autophagic buildup **disrupts the contractile apparatus** → progressive myofiber damage and weakness; it also **acts as a sink for recombinant enzyme**, reducing ERT delivery/efficacy (demonstrated → mechanism of ERT resistance).
6. Downstream: **lipofuscin accumulation, mitochondrial dysfunction/defective oxidative phosphorylation, inflammation, apoptosis, and muscle regeneration** in vacuolated fibers (demonstrated by transcriptomics).
7. Preferential involvement of **diaphragm and axial/proximal muscles** → **respiratory insufficiency and limb-girdle weakness** → clinical LOPD, with respiratory failure as the leading cause of death (demonstrated).
8. (Branch, largely inferred for LOPD but demonstrated in models) **CNS lysosomal glycogen accumulation** occurs and is **not corrected by current ERTs** (which do not cross the blood–brain barrier).

### Detail by category

**Molecular pathways / cellular processes:** The core lesion is a **lysosomal catabolism defect** (GO:0005764 lysosome; GO:0005980 glycogen catabolic process) with secondary **macroautophagy** dysfunction (GO:0016236; GO:0000045 autophagosome assembly; GO:0061909 autophagosome-lysosome fusion). *"The autophagic process in Pompe skeletal muscle is affected at the termination stage—impaired autophagosomal-lysosomal fusion"* ([PMID: 25183957](https://pubmed.ncbi.nlm.nih.gov/25183957/)). *"Progressive accumulation of autophagic vesicles is restricted to Type II-rich muscle fibers"* and *"it also interferes with enzyme replacement therapy by acting as a sink for the recombinant enzyme and preventing its efficient delivery to the lysosomes"* ([PMID: 20040311](https://pubmed.ncbi.nlm.nih.gov/20040311/)).

**Protein dysfunction / biochemical abnormality:** Loss of function of acid α-glucosidase (EC 3.2.1.20), a lysosomal exo-1,4-α-glucosidase. Substrate CHEBI: glycogen (CHEBI:28087); product glucose (CHEBI:17234).

**Transcriptomic profiling:** Single-nucleus RNA-seq plus spatial transcriptomics of LOPD muscle showed *"an increase in the proportion of slow and regenerative muscle fibres and macrophages,"* reduced glycolysis, increased lipid/amino-acid metabolism in non-vacuolated fibers (early metabolic abnormality), *"upregulation of autophagy genes and downregulation of the genes involved in ribosomal and mitochondrial function leading to defective oxidative phosphorylation,"* with inflammation/apoptosis/regeneration confined to vacuolated fibers ([PMID: 39045638](https://pubmed.ncbi.nlm.nih.gov/39045638/)).

**Early pathology:** Even in asymptomatic patients, residual glycogen accumulates in muscle lysosomes with early glycogenin/STBD1 detection, suggesting a pre-symptomatic window and candidate biomarker ([PMID: 41923452](https://pubmed.ncbi.nlm.nih.gov/41923452/)).

**Immune involvement:** Immunometabolic profiling of Pompe patient and mouse cells revealed *"heightened expression of activation markers in effector T cells compared to controls,"* reduced regulatory T cells, and mitophagy defects — relevant to anti-rhGAA antibody responses ([PMID: 41840212](https://pubmed.ncbi.nlm.nih.gov/41840212/)).

**Cell types (suggested CL terms):** fast-twitch/type II skeletal myocyte (CL:0000190 striated muscle cell; CL:0002211 fast muscle cell), cardiac muscle cell (CL:0000746), macrophage (CL:0000235), motor neuron / CNS neurons (CL:0000100).

---

## Section 7 — Anatomical Structures Affected

**Organ/system level (primary):** skeletal muscle (UBERON:0001134), especially proximal limb-girdle and axial/paraspinal muscles; diaphragm (UBERON:0001103) → respiratory system involvement. Secondary/minor: heart (UBERON:0000948) — minor in LOPD.

**Muscle involvement pattern (imaging):** *"The first muscles to degenerate in Pompe disease are hamstring and paraspinals"* with elevated glycogen (1.8–2.2× controls) preceding fatty replacement; calves are relatively spared ([PMID: 41093637](https://pubmed.ncbi.nlm.nih.gov/41093637/)). Quantitative MRI identifies the adductor magnus and the age-independent adductor-magnus/rectus-femoris fat-fraction ratio as sensitive early markers ([PMID: 41554264](https://pubmed.ncbi.nlm.nih.gov/41554264/); [PMID: 42223341](https://pubmed.ncbi.nlm.nih.gov/42223341/)).

**Tissue/cell level:** striated muscle tissue; type II (fast-twitch) myofibers preferentially; macrophage infiltration in vacuolated fibers. CNS neurons (motor neurons, anterior horn) in models.

**Subcellular level (GO cellular component):** lysosome (GO:0005764) — primary site of glycogen storage; autophagosome (GO:0005776); late endosome (GO:0005770) with acidification defect; mitochondria (GO:0005739) — secondary dysfunction.

**Localization/lateralization:** bilateral, symmetric proximal and axial muscle involvement.

---

## Section 8 — Temporal Development

**Onset:** After 12 months of age by definition; ranges from childhood to the seventh–eighth decade. Insidious, chronic onset. In the Pompe Registry (n=485), *"median ages at symptom onset, diagnosis, and alglucosidase alfa initiation were 34.3, 41.1, and 44.9 years"* ([PMID: 38896264](https://pubmed.ncbi.nlm.nih.gov/38896264/)) — highlighting a substantial diagnostic delay of ~7 years.

**Progression:** Slowly progressive and lifelong. Without ERT, forced vital capacity and ambulation decline steadily; respiratory muscle weakness drives morbidity and mortality. With alglucosidase alfa, FVC%predicted rose during the first 6 months (*"slope 1.83%/year"*) then declined (−0.54%/yr from >6 months–5 years; −1.00%/yr from >5–13 years) ([PMID: 38896264](https://pubmed.ncbi.nlm.nih.gov/38896264/)). Network/observational data show initial 1–3 year gains followed by gradual 10–15 year decline ([PMID: 41696977](https://pubmed.ncbi.nlm.nih.gov/41696977/)).

**Critical periods:** Pre-symptomatic residual-glycogen accumulation ([PMID: 41923452](https://pubmed.ncbi.nlm.nih.gov/41923452/)) and subclinical qMRI changes preceding clinical decline ([PMID: 42223341](https://pubmed.ncbi.nlm.nih.gov/42223341/)) define a window for early intervention. No spontaneous remission occurs.

---

## Section 9 — Inheritance and Population

**Inheritance:** Autosomal recessive. Penetrance is effectively complete for biallelic pathogenic genotypes but **age of onset and expressivity are highly variable**, partly explained by the residual activity of the leaky allele and by modifier variants (c.510C>T; autophagy-gene variants). No anticipation (not a repeat-expansion disorder).

**Epidemiology (birth prevalence from newborn screening):** LOPD *"ranged from 1 in 82,914 in Taiwan to 1 in 17,133 in Pennsylvania"* ([PMID: 40329343](https://pubmed.ncbi.nlm.nih.gov/40329343/)). In the Pennsylvania program, 531,139 newborns were screened; combined IOPD+LOPD incidence was **1:16,095** (rising to 1:8,431 including suspected LOPD) ([PMID: 33202836](https://pubmed.ncbi.nlm.nih.gov/33202836/)). In Chinese newborn genomic screening, GSD-II was among the more common lysosomal disorders detected ([PMID: 40355959](https://pubmed.ncbi.nlm.nih.gov/40355959/)).

**Enriched clinical populations:** Among adults with hyperCKemia and/or limb-girdle weakness, LOPD prevalence is **2.4% (74/3076)**, with ~95% carrying the common c.-32-13T>G splice variant ([PMID: 27170567](https://pubmed.ncbi.nlm.nih.gov/27170567/)).

**Carrier frequency / founder effects:** *GAA* carriers are appreciable in the general population; in Taiwanese carrier screening, *GAA* was among the top autosomal-recessive genes identified, supporting reverse cascade testing ([PMID: 38135707](https://pubmed.ncbi.nlm.nih.gov/38135707/); [PMID: 40673334](https://pubmed.ncbi.nlm.nih.gov/40673334/)). The c.-32-13T>G allele constitutes a Northern-European–enriched allele; pseudodeficiency alleles are enriched in East Asians (~4% homozygous) ([PMID: 18301443](https://pubmed.ncbi.nlm.nih.gov/18301443/)).

**Sex ratio:** Approximately equal (autosomal). **Consanguinity** increases risk of biallelic disease as for any AR disorder.

---

## Section 10 — Diagnostics

**First-line enzyme test:** Reduced GAA activity on a **dried blood spot (DBS)** by fluorometry or flow-injection tandem mass spectrometry (FIA-MS/MS). In Pennsylvania NBS, *"Alpha-Glucosidase (GAA) enzyme activity is measured by flow-injection tandem mass spectrometry"* with reflex full *GAA* sequencing ([PMID: 33202836](https://pubmed.ncbi.nlm.nih.gov/33202836/)).

**Confirmatory genetic test:** *GAA* sequencing (single-gene or multigene NGS panel). Large biochemical + genetic testing programs confirm this two-step approach in >30,000 symptomatic patients ([PMID: 40225932](https://pubmed.ncbi.nlm.nih.gov/40225932/)). NGS panels effectively distinguish LOPD from LGMD: *"NGS effectively diagnosed 86.2% and 13.8% of patients with LGMD and Pompe disease, respectively"* ([PMID: 39678382](https://pubmed.ncbi.nlm.nih.gov/39678382/)).

**Biomarkers:** Urinary glucose tetrasaccharide **Glc4/Hex4** (Glcα1-6Glcα1-4Glcα1-4Glc) and serum CK. Baseline urinary Glc4 (34.2±11.3 mmol/mol creatinine) and plasma Hex4 (1.7±0.8 µM) are elevated vs controls (6.1±5.1; 0.22±0.15) and *"both urinary Glc4 and plasma Hex4 levels decreased after initiation of ERT for all patients"* ([PMID: 15886040](https://pubmed.ncbi.nlm.nih.gov/15886040/)).

**Imaging:** Quantitative muscle MRI (Dixon fat fraction, water T2) detects subclinical involvement and disease progression before clinical decline ([PMID: 41554264](https://pubmed.ncbi.nlm.nih.gov/41554264/); [PMID: 42223341](https://pubmed.ncbi.nlm.nih.gov/42223341/)); 7-Tesla imaging quantifies muscle glycogen distribution ([PMID: 41093637](https://pubmed.ncbi.nlm.nih.gov/41093637/)).

**Electrophysiology / biopsy:** EMG shows myopathic ± myotonic discharges, especially in paraspinals; muscle biopsy shows rimmed/autophagic vacuoles with PAS-positive glycogen and acid-phosphatase positivity ([PMID: 32419263](https://pubmed.ncbi.nlm.nih.gov/32419263/)).

**Differential diagnosis:** LGMD subtypes (GNE, LDB3/ZASP, MYOT, DES, GYG1, TRIM32), Danon disease (LAMP2), inflammatory myopathies, and other late-onset vacuolar myopathies. *"An important differential diagnosis among patients presenting with proximal muscle weakness (PMW) is late-onset Pompe disease (LOPD)... which often presents with early respiratory insufficiency"* ([PMID: 31931849](https://pubmed.ncbi.nlm.nih.gov/31931849/)). Danon disease (X-linked *LAMP2*) is a key mimic with glycogen-filled autophagic vacuoles ([PMID: 42154863](https://pubmed.ncbi.nlm.nih.gov/42154863/)).

**Screening:** Newborn screening (DBS enzyme + reflex sequencing); carrier and reverse cascade testing in families ([PMID: 40673334](https://pubmed.ncbi.nlm.nih.gov/40673334/)). Pseudodeficiency alleles must be recognized to avoid false positives ([PMID: 18301443](https://pubmed.ncbi.nlm.nih.gov/18301443/)).

---

## Section 11 — Outcome / Prognosis

**Mortality:** Respiratory failure from progressive diaphragmatic weakness is the leading cause of death. ERT substantially improves survival: in a Chinese single-center cohort (n=68), *"the mortality rate was 6.4%, compared to 57.1% in the 21 patients who did not receive ERT"* ([PMID: 42131243](https://pubmed.ncbi.nlm.nih.gov/42131243/)).

**Morbidity / function:** Progressive loss of ambulation and respiratory capacity; many patients ultimately require ventilatory support and mobility aids. Quality-of-life burden is substantial across PROMIS, R-PAct, EQ-5D-5L, and SF-36 measures ([PMID: 39535661](https://pubmed.ncbi.nlm.nih.gov/39535661/); [PMID: 39318718](https://pubmed.ncbi.nlm.nih.gov/39318718/)).

**Disease course with treatment:** ERT changes the natural history but effectiveness wanes over time; initial 1–3 year gains are followed by gradual decline over 10–15 years ([PMID: 41696977](https://pubmed.ncbi.nlm.nih.gov/41696977/)). A proposed "therapeutic corridor of stability" defines FVC change of approximately −1% to +5%/year and 6MWD stability within ±25 m of peak as adequate response ([PMID: 42538546](https://pubmed.ncbi.nlm.nih.gov/42538546/)).

**Prognostic factors/biomarkers:** Age at ERT initiation, baseline muscle involvement (qMRI fat fraction), FVC, 6MWD, and biomarker trajectory (Glc4/Hex4, CK). Persistently elevated Glc4 tracks limited motor improvement ([PMID: 15886040](https://pubmed.ncbi.nlm.nih.gov/15886040/)).

---

## Section 12 — Treatment

### Enzyme replacement therapy (ERT) — mainstay

Three approved agents (suggested NCIT: Enzyme Replacement Therapy):

| Agent | Key feature | Pivotal trial |
|---|---|---|
| Alglucosidase alfa | Standard of care >15 years | LOTS |
| Avalglucosidase alfa | Enhanced bis-M6P → improved muscle uptake | COMET (NCT02782741) |
| Cipaglucosidase alfa + miglustat | Enzyme + chaperone stabilizer | PROPEL (NCT03729362) |

Alglucosidase alfa *"has been available for more than 15 years and is the standard treatment... although the effectiveness of the treatment reduces over time"* ([PMID: 41453611](https://pubmed.ncbi.nlm.nih.gov/41453611/)).

**Comparative efficacy:** In network meta-analysis, ERT-naïve patients showed *"significant 6MWD improvements vs. placebo: ~25 m with alglucosidase alfa and ~54 m with avalglucosidase alfa"* at ~1 year ([PMID: 40842017](https://pubmed.ncbi.nlm.nih.gov/40842017/); [PMID: 41696977](https://pubmed.ncbi.nlm.nih.gov/41696977/)). Real-world data confirm *"avalglucosidase alfa and cipaglucosidase alfa plus miglustat have demonstrated that both treatments are at least as efficacious as alglucosidase alfa"* ([PMID: 40471681](https://pubmed.ncbi.nlm.nih.gov/40471681/)). Indirect comparisons numerically favor avalglucosidase over cipa+mig for FVC and 6MWT ([PMID: 40920287](https://pubmed.ncbi.nlm.nih.gov/40920287/); [PMID: 41757410](https://pubmed.ncbi.nlm.nih.gov/41757410/)).

**Switching:** ERT-experienced patients switched from alglucosidase to cipaglucosidase alfa+miglustat improved or stabilized across most outcomes, with SGIC responder rates *"90 vs. 59% responders in the cipa+mig vs. the alg+pbo group"* ([PMID: 39535661](https://pubmed.ncbi.nlm.nih.gov/39535661/); [PMID: 40342075](https://pubmed.ncbi.nlm.nih.gov/40342075/)). Switching to avalglucosidase is likewise feasible and safe ([PMID: 38313679](https://pubmed.ncbi.nlm.nih.gov/38313679/)).

### Advanced therapeutics

**Gene therapy:** Systemic AAV9-*GAA* is in development, including novel liver/muscle-restricted promoters (G6PC, CRM4-G6PC) that evade transgene-specific immune responses in mice ([PMID: 41485391](https://pubmed.ncbi.nlm.nih.gov/41485391/)). However, safety risks exist: *"a late onset Pompe disease patient who developed sensory neuronopathy after initiating gene therapy with AT845"* (DRG toxicity) ([PMID: 42142433](https://pubmed.ncbi.nlm.nih.gov/42142433/)).

### Supportive / rehabilitative (adjuvant to ERT)

Supervised **resistance training (24 weeks) plus respiratory-muscle training** improved leg extensor strength (+10.5±3.2 Nm, p<0.01), leg flexors (+12.1±4.1 Nm, p<0.01) and maximal inspiratory pressure (+8.5±3.7 cmH₂O) in ERT-treated LOPD patients ([PMID: 35365393](https://pubmed.ncbi.nlm.nih.gov/35365393/)). **High-protein diet plus physical training** improved muscle strength, fatigue, and physical QoL in pediatric Pompe patients ([PMID: 37002894](https://pubmed.ncbi.nlm.nih.gov/37002894/)). Structured adapted physical activity and pulmonary rehabilitation are recommended ([PMID: 31811531](https://pubmed.ncbi.nlm.nih.gov/31811531/); [PMID: 31970320](https://pubmed.ncbi.nlm.nih.gov/31970320/)).

### Immunogenicity considerations

Anti-rhGAA antibodies can reduce ERT efficacy. *"ERT response depends on several factors, including ERT initiation age, dose, and cross-reactive immunological material (CRIM) status, especially in infantile-onset Pompe disease"* ([PMID: 41583481](https://pubmed.ncbi.nlm.nih.gov/41583481/)). Most LOPD patients carry the leaky allele producing some GAA protein (CRIM-positive) and develop lower titers, but immunomodulation (rituximab + methotrexate + IVIG) is critical mainly for CRIM-negative IOPD, where *"the inability of CRIM-negative IOPD patients to produce native GAA exposes them to a high risk of development of anti-rhGAA IgG antibody titers, leading to treatment failure"* ([PMID: 39314994](https://pubmed.ncbi.nlm.nih.gov/39314994/)).

---

## Section 13 — Prevention

There is no primary prevention for this Mendelian disorder. **Secondary prevention** relies on early detection: **newborn screening** (DBS GAA enzyme + reflex sequencing) enables presymptomatic identification and timely ERT ([PMID: 33202836](https://pubmed.ncbi.nlm.nih.gov/33202836/); [PMID: 40355959](https://pubmed.ncbi.nlm.nih.gov/40355959/)), and **carrier / reverse cascade testing** identifies at-risk relatives ([PMID: 40673334](https://pubmed.ncbi.nlm.nih.gov/40673334/); [PMID: 38135707](https://pubmed.ncbi.nlm.nih.gov/38135707/)). **Genetic counseling**, carrier screening, prenatal testing, and preimplantation genetic diagnosis inform reproductive decisions. **Tertiary prevention** (preventing complications) comprises ERT, respiratory support, vaccination against respiratory infections, exercise/nutrition, and multidisciplinary follow-up per LOPD management recommendations ([PMID: 41453611](https://pubmed.ncbi.nlm.nih.gov/41453611/)).

---

## Section 14 — Other Species / Natural Disease

Naturally occurring GAA/Pompe disease ("generalized glycogenosis") is well documented in animals. *"Generalized glycogenosis is a lethal autosomal recessive disease caused by a deficient activity of the acidic 1,4-α-glucosidase enzyme and characterized by an accumulation of glycogen within lysosomes"* in cattle ([PMID: 31377960](https://pubmed.ncbi.nlm.nih.gov/31377960/)).

**Cattle (Bos taurus, NCBI:txid9913):** Loss-of-function *GAA* alleles are established in **Brahman** (E13, 1783C>T), **Shorthorn** (E18, 2454delCA), and **Droughtmaster/Braford** (E7, 1057delTA), all causing premature translation termination; carrier frequency ~12% in Argentinean Brahman-derived herds. Homozygous calves show multisystem pathology: *"Pathology consistent with generalised glycogenosis was found in the skeletal and cardiac muscle and spinal cord of both of the affected calves"* ([PMID: 28444756](https://pubmed.ncbi.nlm.nih.gov/28444756/)). Bovine *GAA* is *"highly conserved compared with the human alpha-glucosidase gene (86% and 83% identity respectively)"* ([PMID: 10723725](https://pubmed.ncbi.nlm.nih.gov/10723725/)). Heterozygote detection can be confounded by haemopoietic chimaerism in twin cattle ([PMID: 8161014](https://pubmed.ncbi.nlm.nih.gov/8161014/)).

**Other species:** Naturally occurring acid maltase deficiency is reported in **dogs** (e.g., Lapland dog), **cats**, **sheep**, and **Japanese quail** — the last historically used as an avian therapy-development model. **Orthologous gene:** *GAA* is conserved; suggested resources: OMIA, NCBI Gene, HomoloGene.

---

## Section 15 — Model Organisms

**Mammalian genetic models:** The **Gaa-knockout mouse** is the principal model; newer CRISPR knock-in / compound-heterozygous mice recapitulate the metabolic hallmark. *"CHet mice exhibited reduced GAA activity and elevated plasma glycogen levels, recapitulating the metabolic hallmark of human PD"* ([PMID: 41742217](https://pubmed.ncbi.nlm.nih.gov/41742217/)). Models reproduce cardiac, skeletal, diaphragmatic and hepatic glycogenosis with **type II fiber-restricted autophagic buildup** and an endosomal/lysosomal acidification defect ([PMID: 16532490](https://pubmed.ncbi.nlm.nih.gov/16532490/); [PMID: 20040311](https://pubmed.ncbi.nlm.nih.gov/20040311/)).

**Applications & extensions:**
- **CNS involvement:** *"none of the approved therapies are known to cross the blood brain barrier (BBB) and patients with PD have progressive central nervous system (CNS)-associated impairments due to lysosomal glycogen accumulation in the CNS"* — motivating focused-ultrasound BBB opening for ERT delivery ([PMID: 41349290](https://pubmed.ncbi.nlm.nih.gov/41349290/)).
- **Gene therapy:** AAV9-*GAA* with novel promoters evading immune responses ([PMID: 41485391](https://pubmed.ncbi.nlm.nih.gov/41485391/)).
- **Immunometabolism:** heightened effector T-cell activation and mitophagy defects in Gaa-/- immune cells ([PMID: 41840212](https://pubmed.ncbi.nlm.nih.gov/41840212/)).

**Limitations:** Mouse models show variable fidelity to the slowly progressive, respiratory-predominant adult human phenotype; the human leaky splice allele (a splicing phenomenon) is difficult to model directly. Satellite-cell dysfunction may contribute to impaired regeneration across neuromuscular disorders including Pompe ([PMID: 35302338](https://pubmed.ncbi.nlm.nih.gov/35302338/)). **Databases:** MGI, IMPC, IMSR; cellular models include patient iPSC-derived myotubes.

---

## Mechanistic Model / Interpretation

```
 Biallelic partial-LoF GAA variants (leaky c.-32-13T>G + null allele)
                    │  (partial residual acid α-glucosidase)
                    ▼
   Impaired lysosomal glycogen degradation → intralysosomal glycogen ↑
                    │
      ┌─────────────┴──────────────┐
      ▼                            ▼
 Lysosomal swelling/rupture   Autophagy termination defect
 + acidification defect       (impaired autophagosome–lysosome fusion)
      │                            │ (restricted to TYPE II fibers)
      │                            ▼
      │                    Massive autophagic buildup
      │                    ── acts as SINK for recombinant enzyme → ERT resistance
      └──────────────┬─────────────┘
                     ▼
   Disruption of contractile apparatus; mitochondrial dysfunction,
   lipofuscin, inflammation, apoptosis, impaired regeneration
                     │
      ┌──────────────┼───────────────────────┐
      ▼              ▼                        ▼
 Proximal/axial   Diaphragm weakness    CNS glycogen accumulation
 limb-girdle       → respiratory         (not corrected by current
 weakness           insufficiency         ERTs — no BBB penetration)
      │              │
      └──────┬───────┘
             ▼
     Progressive LOPD; respiratory failure = leading cause of death
```

The unifying insight is that LOPD is **not simply a lysosomal storage problem but a disorder of failed autophagy in a specific fiber type.** The type II-fiber-restricted autophagic buildup both damages muscle and blunts ERT delivery, explaining why enzyme therapy modifies without curing the disease and why next-generation, higher-uptake enzymes and adjuvant strategies matter.

---

## Evidence Base — Key Literature

| PMID | Contribution | Relationship to findings |
|---|---|---|
| [30922962](https://pubmed.ncbi.nlm.nih.gov/30922962/) | c.-32-13T>G in ~90% of Caucasian LOPD; c.510C>T modifier | Supports F001 (genetics) |
| [20040311](https://pubmed.ncbi.nlm.nih.gov/20040311/) | Type II-restricted autophagic buildup; ERT "sink" | Supports F002 (mechanism) |
| [25183957](https://pubmed.ncbi.nlm.nih.gov/25183957/) | Impaired autophagosome-lysosome fusion | Supports F002 |
| [16532490](https://pubmed.ncbi.nlm.nih.gov/16532490/) | Endocytic/autophagic dysfunction, acidification defect | Supports F002 |
| [40329343](https://pubmed.ncbi.nlm.nih.gov/40329343/) | NBS birth prevalence range | Supports F003 (epidemiology) |
| [27170567](https://pubmed.ncbi.nlm.nih.gov/27170567/) | 2.4% LOPD in hyperCKemia/LGMW; phenotype frequencies | Supports F003, F004 |
| [18301443](https://pubmed.ncbi.nlm.nih.gov/18301443/) | Pseudodeficiency alleles → NBS false positives | Supports F003 |
| [38896264](https://pubmed.ncbi.nlm.nih.gov/38896264/) | Registry timeline; FVC trajectory on ERT | Supports F004 |
| [42131243](https://pubmed.ncbi.nlm.nih.gov/42131243/) | Mortality 6.4% (ERT) vs 57.1% (no ERT) | Supports F004 |
| [40842017](https://pubmed.ncbi.nlm.nih.gov/40842017/) / [41696977](https://pubmed.ncbi.nlm.nih.gov/41696977/) | ERT 6MWD network meta-analysis | Supports F005 |
| [40471681](https://pubmed.ncbi.nlm.nih.gov/40471681/) | Next-gen ERTs ≥ alglucosidase | Supports F005 |
| [42142433](https://pubmed.ncbi.nlm.nih.gov/42142433/) | Gene therapy AT845 sensory neuronopathy | Supports F005 (risk) |
| [41742217](https://pubmed.ncbi.nlm.nih.gov/41742217/) | Compound-het mouse recapitulates hallmark | Supports F006 |
| [41349290](https://pubmed.ncbi.nlm.nih.gov/41349290/) | CNS glycogen; ERT no BBB penetration | Supports F006 |
| [41840212](https://pubmed.ncbi.nlm.nih.gov/41840212/) | Immunometabolic dysregulation | Supports F006 |
| [39535661](https://pubmed.ncbi.nlm.nih.gov/39535661/) | Multisystem/QoL; PRO on switching | Supports F007 |
| [39678382](https://pubmed.ncbi.nlm.nih.gov/39678382/) / [31931849](https://pubmed.ncbi.nlm.nih.gov/31931849/) / [32419263](https://pubmed.ncbi.nlm.nih.gov/32419263/) | LGMD/vacuolar-myopathy differential; NGS | Supports F008 |
| [41583481](https://pubmed.ncbi.nlm.nih.gov/41583481/) / [39314994](https://pubmed.ncbi.nlm.nih.gov/39314994/) | CRIM/immunogenicity | Supports F009 |
| [28444756](https://pubmed.ncbi.nlm.nih.gov/28444756/) / [31377960](https://pubmed.ncbi.nlm.nih.gov/31377960/) / [10723725](https://pubmed.ncbi.nlm.nih.gov/10723725/) | Bovine natural disease; GAA conservation | Supports F010 |
| [31811531](https://pubmed.ncbi.nlm.nih.gov/31811531/) / [35365393](https://pubmed.ncbi.nlm.nih.gov/35365393/) / [37002894](https://pubmed.ncbi.nlm.nih.gov/37002894/) | Rehab/nutrition adjuncts; minor cardiac | Supports F011 |
| [15886040](https://pubmed.ncbi.nlm.nih.gov/15886040/) | Glc4/Hex4 biomarker | Supports F012 |

---

## Limitations and Knowledge Gaps

- **Prevalence estimates** vary widely by ascertainment method (newborn screening vs. clinical cohorts) and geography (1:17,133 to 1:82,914 for LOPD from NBS); true adult clinical prevalence is uncertain because of diagnostic delay (~7 years).
- **Genotype–phenotype correlation is imperfect:** patients with identical *GAA* genotypes vary in onset and severity, implicating incompletely characterized modifier genes and epigenetic factors ([PMID: 33807278](https://pubmed.ncbi.nlm.nih.gov/33807278/)).
- **Comparative ERT efficacy** rests largely on indirect/network comparisons rather than head-to-head trials; long-term (10–15 year) comparative outcomes for next-generation agents are immature ([PMID: 41696977](https://pubmed.ncbi.nlm.nih.gov/41696977/)).
- **CNS involvement in human LOPD** is inferred largely from models; its clinical significance and the value of BBB-crossing therapies remain to be established.
- **Gene therapy** safety (DRG toxicity) requires resolution before broad application.
- **Biomarkers** (Glc4/Hex4, qMRI) need longitudinal validation as surrogate endpoints and for optimal timing of therapy initiation.

---

## Proposed Follow-up Experiments / Actions

1. **Longitudinal qMRI + biomarker validation:** Prospectively validate adductor-magnus fat fraction and urinary Glc4 as surrogate endpoints and triggers for pre-symptomatic ERT initiation.
2. **Modifier-gene discovery:** Genome-wide/whole-genome sequencing of discordant siblings sharing *GAA* genotype to identify severity modifiers beyond c.510C>T and autophagy-gene variants.
3. **Head-to-head next-generation ERT trial:** Randomized comparison of avalglucosidase alfa vs. cipaglucosidase alfa+miglustat with harmonized endpoints (FVC, 6MWD, Glc4, PROs).
4. **CNS-directed therapy translation:** Advance focused-ultrasound BBB-opening and CNS-tropic AAV-*GAA* approaches, with rigorous DRG-toxicity monitoring informed by the AT845 signal.
5. **Autophagy-targeted adjuvant strategies:** Test agents that restore autophagosome-lysosome fusion to relieve the "enzyme sink" and improve ERT delivery to type II fibers.
6. **Standardized exercise/nutrition protocols:** Multi-center RCT of resistance + respiratory-muscle training plus high-protein diet as adjuvant to next-generation ERT.
7. **Reverse cascade testing implementation:** Operationalize family-wide screening following NBS-positive LOPD to shorten diagnostic delay in relatives.

---

*Evidence source types: findings are drawn from human clinical cohorts and registries, randomized controlled trials, newborn-screening programs, model-organism (mouse, cattle) studies, in vitro/muscle-biopsy transcriptomics, and quantitative imaging. All mechanistic and clinical claims are cited to primary literature by PMID.*


## Artifacts

- [OpenScientist final report](Late-Onset_Pompe_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Late-Onset_Pompe_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 52 |
| Resolved | 52 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 52 |
| On topic | 45 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 5 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001638` (1 mention) - the report calls it "Minor/mild cardiac involvement"; HP calls it **Cardiomyopathy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003236` (1 mention) - the report calls it "Elevated serum creatine kinase (hyperCKemia)"; HP calls it **Elevated circulating creatine kinase activity**, and lists "Elevated serum creatine kinase" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.