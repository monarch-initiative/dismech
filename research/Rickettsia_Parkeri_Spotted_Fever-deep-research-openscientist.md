---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-27T16:53:50.714720'
end_time: '2026-09-27T17:07:49.644125'
duration_seconds: 838.93
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Rickettsia Parkeri Spotted Fever
  mondo_id: MONDO:0000234
  category: Infectious Disease
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
citation_count: 24
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 25
  on_topic: 21
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 29
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 2
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0000234
    reported_labels:
    - MONDO
    - Rickettsia parkeri rickettsiosis
    ontology_label: Rickettsia parkeri spotted fever
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Rickettsia_Parkeri_Spotted_Fever-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Rickettsia_Parkeri_Spotted_Fever-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rickettsia Parkeri Spotted Fever
- **MONDO ID:** MONDO:0000234 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Rickettsia Parkeri Spotted Fever** covering all of the
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

# Rickettsia parkeri Spotted Fever: A Comprehensive Disease Characterization

**Disease:** Rickettsia parkeri rickettsiosis (Rickettsia parkeri spotted fever)
**MONDO ID:** MONDO:0000234
**Category:** Infectious Disease (tick-borne, spotted fever group rickettsiosis)
**Report basis:** 5-iteration autonomous literature investigation; 14 confirmed findings; 34 papers reviewed

---

## Summary

**Rickettsia parkeri rickettsiosis is an emerging, tick-borne spotted fever group (SFG) rickettsiosis caused by the obligate intracellular Gram-negative bacterium *Rickettsia parkeri*.** It presents as an acute, self-limited febrile illness whose clinical signature is an **inoculation eschar** (*tache noire*) at the tick-bite site, accompanied by a maculopapular—sometimes vesiculopustular—rash, regional lymphadenopathy, fever, headache, and myalgia. In a systematic review of 77 clinical cases, fever occurred in ~93%, eschar in ~87%, and rash in ~68% of patients ([PMID: 33989945](https://pubmed.ncbi.nlm.nih.gov/33989945/)). The first US case series characterized the disease as "similar to but less severe than classically described Rocky Mountain spotted fever" (RMSF) ([PMID: 18808353](https://pubmed.ncbi.nlm.nih.gov/18808353/)). Crucially, **no confirmed deaths have been reported worldwide** ([PMID: 42745336](https://pubmed.ncbi.nlm.nih.gov/42745336/)), placing it at the benign end of the SFG rickettsiosis severity spectrum.

The disease is transmitted primarily by *Amblyomma maculatum* (the Gulf Coast tick) in the United States, and by *Amblyomma ovale* (the R. parkeri strain Atlantic rainforest), *Amblyomma triste*, and *Amblyomma tigrinum* in South America. Pathophysiology centers on **endothelial infection producing a localized necrotizing vasculitis** ("rickettsial vasculitis"), with the bacterium exploiting a distinctive **two-phase actin-based motility** system (RickA/Arp2/3 early; Sca2/formin-mimic late) to spread cell-to-cell. Host **type I interferon** is a key protective response; interferon-receptor–deficient mice are the tractable animal model that recapitulates the human eschar.

Because this is an infectious disease, the "genetic" sections of a heritable-disease template are **not applicable**: there is no human causal gene, no Mendelian inheritance, and no pathogenic human variant. The relevant genetics is that of the pathogen (e.g., *ompA*, *ompB*, *sca2*, *rickA*, *gltA*). Diagnosis rests on eschar recognition plus IFA serology, PCR of the eschar crust, and immunohistochemistry; species-level confirmation requires molecular methods because SFG serology cross-reacts extensively. Treatment is **doxycycline**, to which cases respond uniformly. There is no vaccine, so prevention relies on tick-bite avoidance, prompt tick removal, and canine ectoparasite/vector control.

---

## Key Findings

### 1. Clinical profile: an eschar-associated febrile illness milder than RMSF (F001)

The defining clinical portrait of R. parkeri rickettsiosis comes from a systematic review of 77 clinical cases (32 confirmed, 45 probable). Pooled phenotype frequencies were: **fever ~93%, eschar ~87%, rash ~68%, headache ~67%, myalgia ~61%**, with ≥60% of cases showing altered laboratory parameters ([PMID: 33989945](https://pubmed.ncbi.nlm.nih.gov/33989945/)):

> "more than 60% of the cases had fever (mean of 93%), eschar (mean of 87%), and rash (mean of 68%). Headache and myalgia were predominant nonspecific symptoms (mean of 67% and 61%, respectively)"

The first 12 US cases (6 confirmed, 6 probable) established the disease as clinically distinct from — and milder than — RMSF ([PMID: 18808353](https://pubmed.ncbi.nlm.nih.gov/18808353/)):

> "The aggregate clinical characteristics of these patients revealed a disease similar to but less severe than classically described Rocky Mountain spotted fever."

It is the **second most prevalent SFG rickettsiosis** in the Americas.

**Suggested HPO terms:** Fever (HP:0001945), Skin ulcer/eschar (HP:0200042), Maculopapular exanthem/abnormality of the skin (HP:0000988), Lymphadenopathy (HP:0002716), Headache (HP:0002315), Myalgia (HP:0003326), Thrombocytopenia (HP:0001873), Elevated hepatic transaminases (HP:0002910), Lymphopenia (HP:0001888).

### 2. Vector biology and strain geography (F002)

R. parkeri exists as pathogenic strains with distinct vector–geography pairings:

| Strain | Primary vector | Geography | Clinical note |
|---|---|---|---|
| *R. parkeri* sensu stricto | *Amblyomma maculatum* (Gulf Coast tick) | Southeastern/South-central USA | First human case 2004 |
| Strain Atlantic rainforest | *Amblyomma ovale* | Brazil / South America | Milder, non-lethal, eschar |
| (regional) | *Amblyomma triste*, *A. tigrinum* | Argentina, Uruguay | Benign course |

The Atlantic rainforest strain is explicitly characterized as causing "a milder non-lethal febrile disease with an eschar (necrosis) at the tick bite site" ([PMID: 36693294](https://pubmed.ncbi.nlm.nih.gov/36693294/)). Vector range is **expanding northward**: *A. maculatum* + R. parkeri are now established in Ohio ([PMID: 42661358](https://pubmed.ncbi.nlm.nih.gov/42661358/)) —

> "We report the establishment of the Gulf Coast tick (Amblyomma maculatum) and Rickettsia parkeri bacteria in Ohio, USA."

— and in southern Illinois, where R. parkeri infection prevalence in *A. maculatum* reached **16.4%** ([PMID: 42314659](https://pubmed.ncbi.nlm.nih.gov/42314659/)). Laboratory competence has also been shown for *A. americanum* and *Dermacentor variabilis* ([PMID: 41749360](https://pubmed.ncbi.nlm.nih.gov/41749360/)). Dogs serve as sentinel hosts.

### 3. Core pathophysiology: endothelial infection and two-phase actin-based motility (F003)

R. parkeri is an obligate intracellular Gram-negative bacterium with tropism for **vascular endothelium**. Infection produces vascular inflammation, loss of vascular integrity, and increased permeability — collectively "rickettsial vasculitis" ([PMID: 19327117](https://pubmed.ncbi.nlm.nih.gov/19327117/)):

> "the pathogen's affinity for endothelium lining the blood vessels, the consequences of which are vascular inflammation, insult to vascular integrity and compromised vascular permeability, collectively termed 'Rickettsial vasculitis'"

Intracellularly, R. parkeri escapes the phagosome into the cytoplasm and drives **actin-based motility in two temporally distinct phases** ([PMID: 24361066](https://pubmed.ncbi.nlm.nih.gov/24361066/)):

> "each protein directs an independent mode of Rickettsia parkeri motility at different times during infection. Early after invasion, motility is slow and meandering, generating short, curved actin tails that are enriched with Arp2/3 complex and cofilin"

Early motility is driven by **RickA** activating the host Arp2/3 complex; late, fast, directionally persistent motility requires **Sca2**, a functional mimic of eukaryotic formins ([PMID: 20972427](https://pubmed.ncbi.nlm.nih.gov/20972427/)):

> "Sca2 nucleates unbranched actin filaments, processively associates with growing barbed ends, requires profilin for efficient elongation, and inhibits the activity of capping protein, all properties shared with formins"

Structural work (cryo-EM) shows Sca2 forms a formin-FH2-like doughnut core ([PMID: 37028467](https://pubmed.ncbi.nlm.nih.gov/37028467/)), and comparative studies reveal divergent motility mechanisms across Rickettsia species (e.g., *R. bellii* Sca2/6; [PMID: 42048062](https://pubmed.ncbi.nlm.nih.gov/42048062/)).

**Suggested GO/CL terms:** actin nucleation (GO:0045010), Arp2/3 complex-mediated actin nucleation (GO:0034314), actin filament-based movement (GO:0030048), host cell cytoplasm (GO:0030430), endothelial cell (CL:0000115).

### 4. Immune mechanism: type I interferon is protective (F004)

Innate immunity controls R. parkeri infection. **Interferon α/β receptor-deficient mice** (and combined IFN-receptor-deficient mice) are susceptible and develop eschar-associated rickettsiosis, whereas immunocompetent wild-type mice are largely resistant ([PMID: 34423779](https://pubmed.ncbi.nlm.nih.gov/34423779/)):

> "Interferon receptor-deficient mice are susceptible to eschar-associated rickettsiosis"

The bacterium in turn **antagonizes type I interferon via inflammasome activity**, and this antagonism enhances pathogenesis ([PMID: 32123346](https://pubmed.ncbi.nlm.nih.gov/32123346/)):

> "Inflammasome-mediated antagonism of type I interferon enhances Rickettsia pathogenesis"

This host–pathogen cross-talk (interferons + inflammasomes) determines the balance between control and disease.

**Suggested GO terms:** type I interferon signaling pathway (GO:0060337), response to interferon-alpha (GO:0035455), inflammasome complex (GO:0061702).

### 5. Diagnosis and treatment (F005)

**Doxycycline is the treatment of choice** for SFG rickettsioses in both adults and children, and early empiric therapy prevents severe morbidity and death ([PMID: 16572105](https://pubmed.ncbi.nlm.nih.gov/16572105/)):

> "the recommendations for doxycycline are the treatment of choice for both adults and children"

R. parkeri cases respond uniformly and promptly. **Diagnosis** relies on: (1) recognition of the inoculation eschar; (2) indirect immunofluorescence antibody assay (IFA) demonstrating seroconversion / ≥4-fold titer rise; (3) PCR of eschar crust or skin biopsy targeting *ompA*, *gltA*, *ompB*; (4) immunohistochemistry; and (5) cell-culture isolation ([PMID: 18808353](https://pubmed.ncbi.nlm.nih.gov/18808353/)):

> "Using indirect immunofluorescence antibody assays, immunohistochemistry, polymerase chain reaction assays, and cell culture isolation, we identified 6 confirmed and 6 probable cases of infection with R. parkeri."

Because SFG rickettsiae share extensive antigenic cross-reactivity, **species-specific confirmation requires PCR/sequencing** (or cross-adsorption serology) ([PMID: 20404224](https://pubmed.ncbi.nlm.nih.gov/20404224/)):

> "The SFG rickettsioses share many clinical manifestations and extensive antigenic cross-reactivity that may hamper specific confirmation of the causative agent."

**Common laboratory abnormalities:** mild thrombocytopenia, lymphopenia, and elevated hepatic transaminases (≥60% of cases have altered labs; [PMID: 33989945](https://pubmed.ncbi.nlm.nih.gov/33989945/)).

**Suggested NCIT terms:** Doxycycline (NCIT:C305); Antibiotic Therapy (NCIT:C15844); Polymerase Chain Reaction (NCIT:C17003); Immunohistochemistry (NCIT:C16681).

### 6. Epidemiology (F006)

R. parkeri rickettsiosis is a reportable SFG rickettsiosis primarily affecting **adults, especially males aged 18–64**, with tick-exposure history in >90% of cases; confirmed/probable cases have been reported in the United States, Argentina, Brazil, Uruguay, and Colombia ([PMID: 33989945](https://pubmed.ncbi.nlm.nih.gov/33989945/)):

> "our results show that R. parkeri rickettsiosis is more frequent in males in the age group of 18-64 years and that a history of tick exposure was frequent (>90%). Cases were described in the United States, Argentina, Brazil, Uruguay and Colombia"

In the US it is reported under the nationally notifiable aggregate category "spotted fever rickettsiosis" (species-nonspecific due to serologic cross-reactivity). US tickborne bacterial/protozoan disease reports more than doubled from 2004 to 2016 ([PMID: 29723166](https://pubmed.ncbi.nlm.nih.gov/29723166/)). In Argentina, two epidemiologic scenarios coexist — severe R. rickettsii (Amblyomma cajennense complex) versus **benign R. parkeri** (vectors *A. triste*, *A. tigrinum*) ([PMID: 30928146](https://pubmed.ncbi.nlm.nih.gov/30928146/)):

> "R. parkeri produces benign and self-limited clinical manifestation"

### 7. Temporal course and prognosis (F007)

Onset is **acute, typically 7–10 days after the tick bite**. Patients develop a progressively enlarging inoculation eschar, then exanthem/maculopapular (sometimes vesiculopustular) rash, regional lymphadenopathy, fever, myalgia, and prostration ([PMID: 42745336](https://pubmed.ncbi.nlm.nih.gov/42745336/)):

> "All patients developed symptoms 7-10 days after the bite, including inoculation eschar with progressive enlargement, exanthema, regional lymphadenopathy, fever, myalgia, and prostration; all responded to doxycycline treatment"

The disease is **self-limited and benign**, and across all reported cases worldwide **none have been fatal**:

> "So far, none of the cases have been associated with death"

This contrasts sharply with RMSF (R. rickettsii), which carries a high case-fatality rate if untreated (pediatric under-treatment concerns highlighted in [PMID: 24252781](https://pubmed.ncbi.nlm.nih.gov/24252781/)).

### 8. Prevention (F008)

**No licensed human vaccine exists** for any SFG rickettsiosis; prevention is behavioral and environmental. Primary prevention includes avoiding tick habitat, using repellents (DEET, permethrin-treated clothing), performing tick checks, and prompt removal of attached ticks. Because dogs are hosts/sentinels that bring vector ticks into peridomestic settings, control programs emphasize canine ectoparasite control and public awareness ([PMID: 35293560](https://pubmed.ncbi.nlm.nih.gov/35293560/)):

> "the results of the present study indicate the importance of implementing programs to control canine ectoparasites and to raise awareness of the risks of infection, signs and symptoms of SF caused by R. parkeri strain Atlantic Rainforest"

Secondary prevention is early eschar recognition and prompt empiric doxycycline. Antibiotic prophylaxis after tick bite is **not** recommended for SFG rickettsioses ([PMID: 16572105](https://pubmed.ncbi.nlm.nih.gov/16572105/)).

### 9. Taxonomy and zoonotic ecology (F009)

Causative agent: ***Rickettsia parkeri* Lackman et al., 1965 (NCBI Taxonomy ID 35792)**, an obligate intracellular Gram-negative alphaproteobacterium of the spotted fever group. It is a tick-borne **zoonosis with no human-to-human transmission**. Ticks are both vector and reservoir, maintaining the bacterium transstadially and transovarially. Dogs are excellent sentinels ([PMID: 42019180](https://pubmed.ncbi.nlm.nih.gov/42019180/)):

> "Dogs have been recognized as good sentinels for these rickettsioses, since they are hosts to different species and stages of ticks, and they sustain a good immunological response after infection"

Natural infection is documented across diverse tick species (*A. maculatum*, *A. ovale*, *A. triste*, *A. tigrinum*, *A. nodosum* strain NOD, *A. parvum*) and in wild carnivores/small mammals across the Americas ([PMID: 41133807](https://pubmed.ncbi.nlm.nih.gov/41133807/); [PMID: 41880873](https://pubmed.ncbi.nlm.nih.gov/41880873/)):

> "three adults of A. nodosum contained DNA of Rickettsia parkeri Lackman et al., 1965 strain NOD"

### 10. Anatomical structures affected (F010)

The **primary anatomical lesion is the skin at the tick-bite site** — an inoculation eschar (*tache noire*): a central zone of dermal–epidermal necrosis with surrounding perivascular lymphohistiocytic inflammation and small-vessel (necrotizing) vasculitis, the histopathologic hallmark of SFG rickettsioses ([PMID: 20404224](https://pubmed.ncbi.nlm.nih.gov/20404224/)):

> "We report 3 cases of SFG rickettsiosis and discuss the epidemiology, clinical presentation, histopathologic features, and laboratory findings that support confirmed or probable diagnoses of R parkeri infection"

Regional (draining) **lymph nodes** are frequently enlarged, and the disseminated rash reflects widespread small-vessel endothelial infection. The **cellular target is the vascular endothelial cell (CL:0000115)**; the bacterium replicates free in the host-cell cytoplasm (GO:0005737). Unlike RMSF, systemic organ involvement (lung, brain, kidney) is minimal or absent because disease remains largely localized and self-limited.

**Suggested UBERON terms:** skin of body (UBERON:0002097), dermis (UBERON:0002067), endothelium of blood vessel (UBERON:0001986), lymph node (UBERON:0000029), integumentary system (UBERON:0002416).

### 11. Genetic/molecular basis is bacterial, not human (F011)

R. parkeri rickettsiosis is an infectious disease with **no human germline/somatic causal gene, no Mendelian inheritance, no pathogenic human variant, and no chromosomal abnormality** — the genetic sections of a heritable-disease template are **not applicable**. Host genetics contributes only to susceptibility via innate immune pathways (e.g., type I interferon signaling; [PMID: 34423779](https://pubmed.ncbi.nlm.nih.gov/34423779/)). The relevant genetics is that of the **pathogen**:

| Gene | Product / role |
|---|---|
| *ompA* (sca0) | Outer membrane protein A; adhesin; diagnostic/typing target |
| *ompB* (sca5) | Outer membrane protein B; cell entry |
| *sca2* | Formin-mimic driving late actin-based motility ([PMID: 20972427](https://pubmed.ncbi.nlm.nih.gov/20972427/)) |
| *rickA* | Arp2/3 activator driving early motility ([PMID: 24361066](https://pubmed.ncbi.nlm.nih.gov/24361066/)) |
| *gltA* | Citrate synthase; molecular typing |
| *sca4* (gene D) | Surface cell antigen |

Phylogenetics supports multiple distinct R. parkeri strains in the New World ([PMID: 29439989](https://pubmed.ncbi.nlm.nih.gov/29439989/)), and inter-tick-species sequence differences occur in cell-entry genes ([PMID: 41749360](https://pubmed.ncbi.nlm.nih.gov/41749360/)):

> "Differences in cellular-entry and pathogen chromosomal genes (OmpA, OmpB, and 16S) were detected within the different tick species"

### 12. Identifiers and synonyms (F012)

**Preferred name:** Rickettsia parkeri rickettsiosis (MONDO:0000234).

| Identifier | Value |
|---|---|
| MONDO | MONDO:0000234 |
| ICD-10 | A77.8 "Other spotted fevers" |
| ICD-11 | 1C30.2 "Spotted fever due to other Rickettsia species" (or 1C30.Y) |
| MeSH | No species-specific descriptor; indexed under "Rickettsia Infections" (D012373); organism "Rickettsia parkeri" |
| OMIM | None (not a heritable disease) |
| Orphanet | No dedicated number (not a rare genetic disorder) |
| NCBI Taxonomy (agent) | 35792 (*Rickettsia parkeri*) |

**Synonyms:** R. parkeri spotted fever; Tidewater spotted fever; American boutonneuse fever; "maculatum infection/disease"; and for the South American strain, Atlantic rainforest spotted fever / mata atlântica spotted fever ([PMID: 18808353](https://pubmed.ncbi.nlm.nih.gov/18808353/); [PMID: 36693294](https://pubmed.ncbi.nlm.nih.gov/36693294/)):

> "Rickettsia parkeri rickettsiosis, a recently identified spotted fever transmitted by the Gulf Coast tick (Amblyomma maculatum), was first described in 2004."

**Information source:** aggregated disease-level literature (case series, systematic reviews, surveillance) — not single-patient EHR resources.

### 13. Model systems (F013)

- **In vivo:** Type I/II interferon-receptor-deficient mice (Ifnar1⁻/⁻, Ifnar1⁻/⁻Ifngr1⁻/⁻) are susceptible and develop eschar-associated rickettsiosis after intradermal inoculation — the first tractable mammalian model recapitulating the human eschar ([PMID: 34423779](https://pubmed.ncbi.nlm.nih.gov/34423779/)). Immunocompetent wild-type mice are largely resistant (a key limitation).
- **In vitro:** Vero cells and human microvascular endothelial cells allow direct visualization of actin-based motility and cell-to-cell spread ([PMID: 24361066](https://pubmed.ncbi.nlm.nih.gov/24361066/); [PMID: 20972427](https://pubmed.ncbi.nlm.nih.gov/20972427/)); tick cell lines model the arthropod host.
- **Historical:** Guinea pigs model SFG rickettsial fever/scrotal reaction.

### 14. Consolidated conclusion (F014)

Across all evidence, R. parkeri rickettsiosis is a mild, self-limited, tick-borne SFG rickettsiosis (fever ~93%, eschar ~87%, rash ~68%; [PMID: 33989945](https://pubmed.ncbi.nlm.nih.gov/33989945/)), with no confirmed deaths ([PMID: 42745336](https://pubmed.ncbi.nlm.nih.gov/42745336/)) and uniform doxycycline responsiveness ([PMID: 16572105](https://pubmed.ncbi.nlm.nih.gov/16572105/)). The single most useful diagnostic discriminator from RMSF is the **inoculation eschar**, characteristic of R. parkeri and essentially absent in RMSF; the first US series framed the disease by "its clinical distinction from Rocky Mountain spotted fever" and found it "similar to but less severe than" RMSF ([PMID: 18808353](https://pubmed.ncbi.nlm.nih.gov/18808353/)).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating exposure → clinical manifestation)

```
1.  Infected Amblyomma tick attaches and feeds on human skin (7–10 day incubation)
        │  leads to
2.  R. parkeri inoculated into the dermis at the bite site
        │  results in
3.  Bacteria adhere to and invade vascular ENDOTHELIAL cells
        │  (adhesins OmpA/OmpB; cell entry) — results in
4.  Phagosomal escape → replication free in host-cell CYTOPLASM
        │  leads to
5.  Two-phase ACTIN-BASED MOTILITY:
        ├─ EARLY: RickA activates host Arp2/3 → slow, meandering motility
        └─ LATE:  Sca2 (formin-mimic) → fast, directional cell-to-cell spread
        │  results in
6.  Local endothelial infection + host innate immune response
        │  (type I IFN protective; bacterium antagonizes IFN via inflammasome)
        │  leads to
7.  Focal NECROTIZING VASCULITIS of small dermal vessels
        │  results in
8.  INOCULATION ESCHAR (tache noire) at bite site  ← hallmark lesion
        │  and (branch) limited hematogenous/lymphatic spread
        ├─ leads to → maculopapular/vesiculopustular RASH (disseminated endothelium)
        ├─ leads to → regional LYMPHADENOPATHY (draining nodes)
        └─ leads to → systemic FEVER, headache, myalgia; mild lab abnormalities
        │  In immunocompetent hosts:
9.  Host immune control (+ doxycycline) → SELF-LIMITED RESOLUTION, no death
```

**Upstream vs downstream:** Steps 1–5 (inoculation, endothelial invasion, cytoplasmic replication, actin motility) are upstream drivers; steps 7–8 (vasculitis, eschar) are the proximate downstream lesions producing the clinical phenotype. The interferon axis (step 6) is a modulating branch that determines whether infection is contained (immunocompetent hosts, most humans) or progresses (interferon-receptor-deficient mice). Steps 3–5 are directly demonstrated in cell culture; step 6's protective role is demonstrated in mouse knockouts and *inferred* for humans.

**Why R. parkeri is milder than RMSF (interpretation):** The disease remains largely **localized** to the inoculation site and skin, with minimal systemic endothelial injury to lung/brain/kidney — the opposite of the widespread, high-permeability endothelial damage that makes R. rickettsii (RMSF) lethal. The eschar is therefore both the pathologic signature and a marker of contained, localized disease.

### Comparison table: R. parkeri vs RMSF (R. rickettsii)

| Feature | R. parkeri rickettsiosis | Rocky Mountain spotted fever |
|---|---|---|
| Vector | *A. maculatum*, *A. ovale*, *A. triste* | *Dermacentor* spp., *A. sculptum* |
| Inoculation eschar | Present (~87%) — hallmark | Typically absent |
| Rash | Maculopapular/vesiculopustular | Maculopapular → petechial |
| Systemic organ injury | Minimal / localized | Severe, multi-organ |
| Case fatality | ~0% (no confirmed deaths) | High if untreated |
| Treatment | Doxycycline (uniform response) | Doxycycline (urgent) |

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [33989945](https://pubmed.ncbi.nlm.nih.gov/33989945/) | *Clinical/epidemiological/lab features: systematic review* | Pooled phenotype frequencies; demographics (F001, F006) |
| [18808353](https://pubmed.ncbi.nlm.nih.gov/18808353/) | *R. parkeri rickettsiosis and its clinical distinction from RMSF* | Milder-than-RMSF; diagnostics; name/first description (F001, F005, F012, F014) |
| [36693294](https://pubmed.ncbi.nlm.nih.gov/36693294/) | *Inoculation eschar in Brazil* | Atlantic rainforest strain/vector; eschar (F002, F012) |
| [42661358](https://pubmed.ncbi.nlm.nih.gov/42661358/) | *Gulf Coast ticks + R. parkeri, Ohio* | Range expansion (F002) |
| [42314659](https://pubmed.ncbi.nlm.nih.gov/42314659/) | *Surveillance, southern Illinois* | 16.4% tick infection; range expansion (F002, F006) |
| [19327117](https://pubmed.ncbi.nlm.nih.gov/19327117/) | *Host-cell interactions with pathogenic Rickettsia* | Endothelial tropism; rickettsial vasculitis (F003, F010) |
| [24361066](https://pubmed.ncbi.nlm.nih.gov/24361066/) | *Actin motility in distinct phases* | Two-phase RickA/Sca2 motility (F003, F011, F013) |
| [20972427](https://pubmed.ncbi.nlm.nih.gov/20972427/) | *Sca2 is a bacterial formin-like mediator* | Sca2 formin-mimic mechanism (F003, F011, F013) |
| [37028467](https://pubmed.ncbi.nlm.nih.gov/37028467/) | *Cryo-EM of Sca2 formin-like core* | Sca2 structure (F003) |
| [42048062](https://pubmed.ncbi.nlm.nih.gov/42048062/) | *Divergent Rickettsia motility mechanisms* | Species divergence in motility (F003) |
| [34423779](https://pubmed.ncbi.nlm.nih.gov/34423779/) | *IFN receptor-deficient mice susceptible* | Protective type I IFN; eschar mouse model (F004, F013) |
| [32123346](https://pubmed.ncbi.nlm.nih.gov/32123346/) | *Inflammasome antagonism of type I IFN* | Immune cross-talk enhances pathogenesis (F004) |
| [16572105](https://pubmed.ncbi.nlm.nih.gov/16572105/) | *Diagnosis/management of tickborne rickettsial diseases* | Doxycycline first-line; no prophylaxis (F005, F008) |
| [20404224](https://pubmed.ncbi.nlm.nih.gov/20404224/) | *Expanding spectrum of eschar-associated rickettsioses* | Histopathology; serologic cross-reactivity (F005, F010) |
| [30928146](https://pubmed.ncbi.nlm.nih.gov/30928146/) | *Spotted fever in Argentina* | Benign course; Argentine vectors (F006, F007) |
| [42745336](https://pubmed.ncbi.nlm.nih.gov/42745336/) | *First outbreak of Atlantic Rainforest SF in NE Brazil* | Incubation, symptom sequence; no deaths (F007, F014) |
| [35293560](https://pubmed.ncbi.nlm.nih.gov/35293560/) | *New focus of SF by R. parkeri in Brazil* | Canine ectoparasite control / prevention (F008) |
| [42019180](https://pubmed.ncbi.nlm.nih.gov/42019180/) | *SFG rickettsiae in dogs of the Americas: meta-analysis* | Dogs as sentinels; zoonotic ecology (F009) |
| [41133807](https://pubmed.ncbi.nlm.nih.gov/41133807/) | *Rickettsia in horses/ticks, Pernambuco* | Multi-tick natural infection; species authority (F009) |
| [41880873](https://pubmed.ncbi.nlm.nih.gov/41880873/) | *Rickettsia in Cerrado carnivores* | Wild reservoir ecology (F009) |
| [29439989](https://pubmed.ncbi.nlm.nih.gov/29439989/) | *Multiple strains of R. parkeri in the New World* | Pathogen strain diversity (F011) |
| [41749360](https://pubmed.ncbi.nlm.nih.gov/41749360/) | *R. parkeri diversity from three tick species* | Cell-entry gene variation; vector competence (F002, F011) |
| [29723166](https://pubmed.ncbi.nlm.nih.gov/29723166/) | *Vital Signs: vectorborne disease trends 2004–2016* | Rising tickborne disease burden (F006) |
| [23440128](https://pubmed.ncbi.nlm.nih.gov/23440128/) | *R. parkeri in A. triste, Argentina* | Molecular typing targets; Argentine vector (F011) |
| [24252781](https://pubmed.ncbi.nlm.nih.gov/24252781/) | *Provider treatment practices, RMSF* | Context: RMSF lethality/doxycycline under-use |

**Evidence source types:** Human clinical (case series, systematic reviews: 33989945, 18808353, 42745336, 30928146, 20404224); epidemiologic/surveillance (42314659, 42661358, 29723166); veterinary/ecologic (42019180, 41880873, 41133807, 32267390); in vitro / cell biology (24361066, 20972427, 37028467, 42048062); model organism (34423779, 32123346); phylogenetic/computational (29439989, 41749360, 23440128).

---

## Limitations and Knowledge Gaps

1. **Under-recognition and surveillance dilution.** In the US, R. parkeri cases are folded into the aggregate "spotted fever rickettsiosis" notifiable category because SFG serology cross-reacts; true incidence and prevalence (cases per 100,000) are therefore **not precisely quantified**. Species-level burden is likely underestimated.
2. **Small evidence base.** The definitive clinical picture rests on 77 pooled cases ([PMID: 33989945](https://pubmed.ncbi.nlm.nih.gov/33989945/)) plus scattered series. No large prospective cohorts or randomized treatment trials exist.
3. **No confirmed deaths, but rare severe cases possible.** The "0% fatality" statement reflects reported cases; immunocompromised or atypical presentations may be under-captured.
4. **Model limitations.** The tractable animal model requires interferon-receptor knockout mice; immunocompetent mice resist infection, so the model does not fully reproduce the mild human course or long-term immunity.
5. **Quality-of-life / long-term outcome data are absent.** Because disease is self-limited, no EQ-5D/SF-36/PROMIS data or disability outcomes have been reported.
6. **Human genetic susceptibility is essentially unstudied.** Beyond the interferon axis inferred from mouse work, no human host-genetic risk/protective factors, GWAS loci, or pharmacogenomic data exist for this disease.
7. **Strain–virulence correlations incomplete.** Whether sequence differences in *ompA/ompB* across strains/tick species translate into clinical severity differences is not established.

---

## Proposed Follow-up Experiments / Actions

1. **Species-specific surveillance:** Advocate for molecular (PCR/sequencing) confirmation in reportable SFG cases to disaggregate R. parkeri from other SFG agents and generate true incidence/prevalence estimates by region.
2. **Prospective clinical registry:** Establish a multi-country (US + South America) registry capturing incubation, symptom frequencies, lab abnormalities, treatment response, and any severe/atypical outcomes to refine natural-history and prognosis data.
3. **Strain-virulence genomics:** Comparative genomics/transcriptomics of R. parkeri sensu stricto vs Atlantic rainforest vs NOD strains, correlating *ompA/ompB/sca2/rickA* variation with in vitro endothelial cytopathology and mouse eschar severity.
4. **Host immunity mechanism:** Dissect the type I interferon ↔ inflammasome axis (building on [PMID: 34423779](https://pubmed.ncbi.nlm.nih.gov/34423779/), [PMID: 32123346](https://pubmed.ncbi.nlm.nih.gov/32123346/)) to explain why R. parkeri is contained (eschar-limited) whereas R. rickettsii disseminates.
5. **Vector-range monitoring:** Continue active tick surveillance in newly colonized northern areas (Ohio, Illinois) to forecast human risk as *A. maculatum* expands ([PMID: 42661358](https://pubmed.ncbi.nlm.nih.gov/42661358/), [PMID: 42314659](https://pubmed.ncbi.nlm.nih.gov/42314659/)).
6. **One-Health prevention trials:** Evaluate canine ectoparasite-control programs as a community-level intervention to reduce peridomestic vector burden ([PMID: 35293560](https://pubmed.ncbi.nlm.nih.gov/35293560/)).
7. **Diagnostic assay development:** Develop rapid, field-deployable species-specific molecular assays for eschar-crust testing to overcome serologic cross-reactivity ([PMID: 20404224](https://pubmed.ncbi.nlm.nih.gov/20404224/)).

---

## Ontology Annotation Summary

| Category | Terms |
|---|---|
| Disease | MONDO:0000234 (Rickettsia parkeri rickettsiosis) |
| Phenotypes (HPO) | HP:0001945 (Fever), HP:0200042 (Skin ulcer/eschar), HP:0002716 (Lymphadenopathy), HP:0002315 (Headache), HP:0003326 (Myalgia), HP:0001873 (Thrombocytopenia), HP:0001888 (Lymphopenia), HP:0002910 (Elevated hepatic transaminases) |
| Cell types (CL) | CL:0000115 (endothelial cell) |
| Anatomy (UBERON) | UBERON:0002097 (skin), UBERON:0002067 (dermis), UBERON:0001986 (endothelium of blood vessel), UBERON:0000029 (lymph node) |
| Biological process (GO) | GO:0030048 (actin filament-based movement), GO:0034314 (Arp2/3-mediated actin nucleation), GO:0045010 (actin nucleation), GO:0060337 (type I interferon signaling), GO:0061702 (inflammasome complex) |
| Cellular component (GO) | GO:0005737 / GO:0030430 (cytoplasm / host cell cytoplasm) |
| Chemical (CHEBI) | CHEBI:50845 (doxycycline) |
| Treatment (NCIT) | NCIT:C305 (Doxycycline), NCIT:C15844 (Antibiotic Therapy) |
| Pathogen (NCBI Taxon) | 35792 (*Rickettsia parkeri*) |

---

*Report compiled from 14 confirmed findings and 34 reviewed papers across a 5-iteration autonomous investigation. All quoted material is verbatim from the cited PubMed abstracts.*


## Artifacts

- [OpenScientist final report](Rickettsia_Parkeri_Spotted_Fever-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Rickettsia_Parkeri_Spotted_Fever-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 25 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 3 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0000234` (4 mentions) - the report calls it "MONDO", "Rickettsia parkeri rickettsiosis"; MONDO calls it **Rickettsia parkeri spotted fever**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0000234` - called "MONDO", "Rickettsia parkeri rickettsiosis"