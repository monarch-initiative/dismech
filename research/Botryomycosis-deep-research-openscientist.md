---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T13:31:36.451578'
end_time: '2026-09-29T13:44:35.857600'
duration_seconds: 779.41
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Botryomycosis
  mondo_id: MONDO:0400006
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
citation_count: 23
reference_validation:
  total_references: 27
  verified: 27
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 16
  quotes_valid: 16
  relevance_assessed: 27
  on_topic: 16
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 20
  verified: 19
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 9
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0031804
    reported_labels:
    - nodular skin lesion
    ontology_label: obsolete Premacular hemorrhage
  - term_id: HP:0100829
    reported_labels:
    - abscess
    ontology_label: Galactorrhea
  - term_id: HP:0030757
    reported_labels:
    - fistula
    ontology_label: Tooth abscess
  - term_id: NCIT:C1055
    reported_labels:
    - TMP-SMX
    ontology_label: Custirsen Sodium
  - term_id: NCIT:C51696
    reported_labels:
    - debridement
    ontology_label: Orthotopic Liver Transplantation
  labels_variant: 5
  obsolete_terms:
  - term_id: HP:0031804
    ontology_label: obsolete Premacular hemorrhage
    replaced_by: HP:0025240
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Botryomycosis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Botryomycosis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Botryomycosis
- **MONDO ID:** MONDO:0400006 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Botryomycosis** covering all of the
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

# Botryomycosis — Comprehensive Disease Characteristics Report

**Disease:** Botryomycosis
**MONDO ID:** MONDO:0400006 · **MeSH:** D001857 · **OMIM:** Not applicable (non-genetic) · **Category:** Infectious Disease (bacterial pseudomycosis)
**Evidence base:** Individual case reports and small case series/reviews only (no registries, cohorts, or clinical trials). All quantitative claims are qualitative/indirect.

---

## Summary

**Botryomycosis is a rare, chronic, suppurative and granulomatous BACTERIAL infection — despite the misleading "-mycosis" suffix, it is not a fungal disease.** It is caused by common, non-filamentous bacteria — most frequently *Staphylococcus aureus* (NCBITaxon:1280), followed by *Pseudomonas aeruginosa* (NCBITaxon:287), with other organisms (*Escherichia coli*, *Proteus*, *Actinobacillus actinomycetemcomitans*) occasionally implicated. The defining feature is that these ordinary bacteria aggregate within tissue into compact colonies ("grains" or "granules") coated by an eosinophilic, amorphous, radiating matrix known as the **Splendore-Hoeppli phenomenon**. Clinically it takes two forms: a common **cutaneous** form (nodules, abscesses, sinuses, fistulae, ulcers, often with deep tissue and bone invasion) and a rare **visceral** form that predominantly affects the lungs and characteristically mimics carcinoma.

Botryomycosis is an **acquired, sporadic, non-genetic** condition — there is no Mendelian inheritance, no causal human gene, and no defined incidence or prevalence. It is best understood as an *aberrant host response* to a common bacterial infection rather than as disease caused by a distinct or exotic pathogen. Its central predisposing factor is **impaired cell-mediated immunity** — HIV/AIDS is the most frequently cited association — with additional risk from immunosuppressive drugs, diabetes mellitus, alcoholism, malnutrition, cystic fibrosis, and local trauma or foreign bodies. The same disease occurs naturally in animals (horses, cattle, swine), and indeed the veterinary and experimental (guinea pig) literature shaped the historical understanding of the entity.

The principal clinical importance of botryomycosis is twofold: (1) it is a **great diagnostic mimic** — of malignancy (lung cancer, sarcoma, liposarcoma, sinonasal tumor), of mycetoma, and of actinomycosis — which has led to unnecessary resections; and (2) it is **curable**. Diagnosis requires tissue biopsy (showing non-filamentous bacterial grains with Splendore-Hoeppli phenomenon) **plus** culture to identify the organism. Treatment combines **prolonged, culture-directed antibiotics** (weeks to many months) with **surgical debridement/excision**, plus restoration of immune function (e.g., antiretroviral therapy) when HIV is the driver. Localized cutaneous disease generally carries a good prognosis, but recurrence is common and disseminated/visceral disease in uncontrolled immunodeficiency can be fatal.

---

## Section-by-Section Report

### 1. Disease Information

Botryomycosis is a chronic granulomatous bacterial infection of skin or (less often) viscera, characterized histologically by aggregated bacterial grains. Key identifiers: **MONDO:0400006**, **MeSH D001857**; there is **no OMIM entry** (it is not a genetic disorder), and it is not a classical Orphanet rare *genetic* disease though it is a rare condition. Common synonyms and historical/related terms include **bacterial pseudomycosis**, **granular bacteriosis**, **cutaneous granular bacteriosis**, "**bacterial ball**" (used for the sinonasal form), and — for animal disease — "botryomycoma" and (for the equine spermatic cord lesion) "scirrhous cord." The name derives from Greek *botryo-* (bunch of grapes) reflecting the grape-cluster appearance of grains. The disease was first described by Bollinger (1870) in horse lung and named by Rivolta.

Information about botryomycosis is derived almost entirely from **aggregated disease-level resources** — chiefly case reports, small case series, and narrative reviews — rather than from large EHR cohorts or registries. Only ~200–300 cutaneous cases and fewer than ~20 primary pulmonary cases have been reported historically ([PMID: 37787361](https://pubmed.ncbi.nlm.nih.gov/37787361/); [PMID: 11844127](https://pubmed.ncbi.nlm.nih.gov/11844127/)).

> "The most frequent isolated etiological agents are *Staphylococcus aureus* followed by *Pseudomonas aeruginosa*. The differential diagnosis includes mycetoma, actinomycosis, and carcinomas/sarcomas." — [PMID: 41128794](https://pubmed.ncbi.nlm.nih.gov/41128794/)

### 2. Etiology

**Causal factors are infectious and mechanistic, not genetic.** The primary cause is inoculation of common, non-filamentous bacteria into tissue, most often *Staphylococcus aureus* (including MRSA — [PMID: 33061472](https://pubmed.ncbi.nlm.nih.gov/33061472/)), then *Pseudomonas aeruginosa*, with *E. coli*, *Proteus* spp., and *Actinobacillus actinomycetemcomitans* also reported ([PMID: 17500377](https://pubmed.ncbi.nlm.nih.gov/17500377/)).

**Risk factors** are acquired/environmental and immunologic:
- *Genetic risk factors*: **None identified.** There are no causal variants, susceptibility loci, or modifier genes for botryomycosis. This is a definitive negative finding.
- *Environmental/host risk factors*: local **trauma** or surgery (inoculation route), **HIV/AIDS** and other defects of cell-mediated immunity, **immunosuppressive therapy** (e.g., methotrexate — [PMID: 28034470](https://pubmed.ncbi.nlm.nih.gov/28034470/)), **diabetes mellitus**, **alcoholism**, **malnutrition**, **cystic fibrosis**, and foreign bodies. Apparent **male predominance** and occurrence at **all ages** (including children — [PMID: 32173890](https://pubmed.ncbi.nlm.nih.gov/32173890/); [PMID: 11001122](https://pubmed.ncbi.nlm.nih.gov/11001122/)).

**Protective factors:** No genetic protective variants are described. The most relevant "protective"/curative environmental factor is **restoration of immune competence** — antiretroviral therapy produced remission in HIV-associated disease when antibiotics alone failed ([PMID: 28562771](https://pubmed.ncbi.nlm.nih.gov/28562771/)).

**Gene–environment interactions:** Not applicable in a classical GxE sense. The operative interaction is **host immune status × bacterial infectivity**: "both the host's immune status and microbial infectivity have been implicated in the pathogenesis" ([PMID: 18177488](https://pubmed.ncbi.nlm.nih.gov/18177488/)).

> "It has long been associated with defects of cellular immunity." — [PMID: 28562771](https://pubmed.ncbi.nlm.nih.gov/28562771/)

### 3. Phenotypes

| Phenotype | Type | Suggested HPO | Onset / Course | Frequency |
|---|---|---|---|---|
| Chronic skin nodules | Physical manifestation | HP:0031804 (nodular skin lesion) | Subacute–chronic (weeks–months), progressive | Very common (cutaneous form) |
| Abscess | Clinical sign | HP:0100829 (abscess) | Chronic, relapsing | Common |
| Draining sinus tracts / fistulae | Clinical sign | HP:0030757 (fistula) | Chronic | Common |
| Skin ulcer | Physical manifestation | HP:0200042 (skin ulcer) | Chronic | Common |
| Grain/granule discharge ("sulfur granules"; rarely red) | Laboratory/pathologic sign | — | Ongoing | Characteristic |
| Osteomyelitis / bone invasion | Clinical sign | HP:0002754 (osteomyelitis) | Late, in neglected disease | Occasional (deep cutaneous) |
| Pulmonary mass / cough | Clinical sign | HP:0002090 (pneumonia) / mass mimic | Chronic | Visceral form (rare) |

Phenotype characteristics: **onset** is typically insidious over weeks to months; **severity** ranges from mild localized lesions to severe destructive/disfiguring disease; **progression** is chronic and relapsing. Deep cutaneous disease can invade bone: a progressive 8-year foot swelling showed radiographic/MRI bone invasion ([PMID: 30429406](https://pubmed.ncbi.nlm.nih.gov/30429406/)). Grains are usually white-yellow; a unique red-grain *S. aureus* case is reported ([PMID: 19736413](https://pubmed.ncbi.nlm.nih.gov/19736413/)).

**Quality of life impact:** No formal EQ-5D/SF-36/PROMIS data exist. Impact is inferred from disfigurement, chronic drainage, pain, and functional impairment of affected limbs; scalp/facial mutilating tumors and chronic relapsing lesions are documented ([PMID: 19094129](https://pubmed.ncbi.nlm.nih.gov/19094129/)).

> "Patients with botryomycosis typically present multiple nodules, sinuses, abscesses, fistulae, and ulcers, which develop during weeks or months." — [PMID: 41128794](https://pubmed.ncbi.nlm.nih.gov/41128794/)

### 4. Genetic / Molecular Information

**Not applicable — botryomycosis has no genetic etiology.** There are:
- **No causal genes** (no gene symbols, no OMIM IDs).
- **No pathogenic germline or somatic variants**, no ACMG classifications, no allele frequencies (gnomAD/ClinVar not relevant).
- **No modifier genes, epigenetic signatures, or chromosomal abnormalities** described for the disease itself.

The only "molecular" actors are **bacterial**: *S. aureus* virulence/biofilm factors and a possible protective **glycocalyx/biofilm** around grains. This section is definitively negative for host genetics and should be recorded as such in the knowledge base.

### 5. Environmental Information

- **Environmental factors:** local trauma, surgical wounds, and foreign bodies provide the portal of entry. No chemical toxin, radiation, or pollution etiology.
- **Lifestyle factors:** alcoholism and malnutrition (as immunocompromising states) are contributory; there is no specific smoking/diet association beyond general immune impairment.
- **Infectious agents (central to etiology):** *Staphylococcus aureus* (**NCBITaxon:1280**; principal agent), *Pseudomonas aeruginosa* (**NCBITaxon:287**; second most common, and the likely agent in a fatal disseminated case — [PMID: 13845294](https://pubmed.ncbi.nlm.nih.gov/13845294/) — and in sinonasal "bacterial ball" — [PMID: 15456177](https://pubmed.ncbi.nlm.nih.gov/15456177/)), plus *E. coli*, *Proteus*, and *Actinobacillus actinomycetemcomitans*. Co-infection is possible: *S. aureus* with *Pneumocystis carinii* in AIDS ([PMID: 18177488](https://pubmed.ncbi.nlm.nih.gov/18177488/)).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Bacterial inoculation** — common non-filamentous bacteria (usually *S. aureus*), typically at a site of trauma/surgery, are introduced into tissue → *leads to*
2. **Aberrant host clearance** — in a host with impaired cell-mediated immunity (and/or a low-virulence/low-inoculum balance), the immune response neither eradicates the organism nor forms an ordinary resolving abscess → *results in*
3. **Bacterial aggregation into grains** — organisms clump into compact colonies (grains/granules) → *leads to*
4. **Splendore-Hoeppli coating** (*inferred*) — grains become surrounded by an eosinophilic amorphous matrix of host immunoglobulin, complement, and degranulated eosinophil/neutrophil products, often with radiating "clubs" → *which*
5. **Immune/antibiotic shielding** (*inferred*) — this matrix (± bacterial glycocalyx/biofilm) shields organisms from phagocytosis and antibiotic penetration → *leads to*
6. **Chronic pyogranulomatous inflammation** — persistent influx of neutrophils, macrophages, multinucleated giant cells, and plasma cells with fibrosis → *results in*
7. **Clinical manifestation** — chronic nodules, draining sinus tracts/fistulae, ulcers, and local tissue/bone destruction (or a visceral pulmonary mass).

Where the chain **branches**: with adequate host immunity + eradication → ordinary abscess/healing (no botryomycosis); with continued immune failure → dissemination and potentially fatal visceral disease.

**Categories mapped onto the chain:**
- *Cellular processes:* inflammation (**GO:0006954**, inflammatory response), phagocytosis (**GO:0006909**), humoral immunity (**GO:0002455**).
- *Immune involvement:* impaired cell-mediated immunity is upstream/permissive; chronic granulomatous and humoral responses are downstream.
- *Protein/biochemical:* Splendore-Hoeppli matrix = host immunoglobulin + complement + eosinophil major basic protein; possible bacterial biofilm glycocalyx.
- *Tissue damage:* suppuration, fibrosis, and osteolysis (bone invasion) via chronic pyogranulomatous destruction.
- *Cell types (CL):* neutrophil (**CL:0000775**), macrophage (**CL:0000235**), eosinophil (**CL:0000771**), plus multinucleated giant cells and plasma cells.

Mechanistic caveats are explicit in the literature: botryomycosis is "an atypical reaction of the host to a common bacterial infection" ([PMID: 9435048](https://pubmed.ncbi.nlm.nih.gov/9435048/)) and "an unusual response to infection with common bacteria" ([PMID: 11243368](https://pubmed.ncbi.nlm.nih.gov/11243368/)), but "the pathobiology remains unknown" ([PMID: 23743320](https://pubmed.ncbi.nlm.nih.gov/23743320/)) — steps 4–5 are **inferred**, not fully demonstrated.

> "both the host's immune status and microbial infectivity have been implicated in the pathogenesis of this unusual clinical condition" — [PMID: 18177488](https://pubmed.ncbi.nlm.nih.gov/18177488/)

### 7. Anatomical Structures Affected

- **Organ level (primary):** skin (**UBERON:0002097**) in the cutaneous form; lung (**UBERON:0002048**) in the visceral form. **Secondary:** bone (**UBERON:0001474**; osteomyelitis/invasion), subcutaneous soft tissue, and mucosal sites (sinonasal tract, tongue — [PMID: 5235476](https://pubmed.ncbi.nlm.nih.gov/5235476/), lacrimal sac — [PMID: 29039982](https://pubmed.ncbi.nlm.nih.gov/29039982/)).
- **Body systems:** integumentary (primary), respiratory (visceral), musculoskeletal (bone invasion), and reticuloendothelial/immune.
- **Tissue/cell level:** dermis and subcutis; pyogranulomatous infiltrate of neutrophils (**CL:0000775**), macrophages (**CL:0000235**), eosinophils (**CL:0000771**), giant cells, plasma cells.
- **Subcellular:** no specific human organelle involvement; relevant compartments are the bacterial cell wall and the extracellular Splendore-Hoeppli matrix (GO extracellular region).
- **Localization/lateralization:** cutaneous lesions favor **extremities** (foot/hand), **head/neck**, and unusual sites; typically **unilateral/localized** at the inoculation site, though disseminated bilateral disease occurs in immunodeficiency.

### 8. Temporal Development

- **Onset:** any age; **insidious/chronic** onset over weeks to months, usually after trauma.
- **Progression:** slowly progressive and **relapsing**; neglected cutaneous disease progresses over years (e.g., 8-year foot course — [PMID: 30429406](https://pubmed.ncbi.nlm.nih.gov/30429406/)) to deep/bone destruction; visceral disease can disseminate.
- **Course pattern:** chronic, relapsing-remitting with therapy; **recurrence is common** after treatment.
- **Duration:** chronic if untreated; potentially curable with prolonged combined therapy.
- **Critical period:** early diagnosis (before bone/visceral involvement and before unnecessary oncologic surgery) is the key window for cure.

### 9. Inheritance and Population

- **Epidemiology:** rare; **no defined incidence or prevalence**. ~200–300 cutaneous and <20 primary pulmonary cases historically reported; one review compiled 18 primary pulmonary cases ([PMID: 37787361](https://pubmed.ncbi.nlm.nih.gov/37787361/)); another was the 16th pulmonary case ([PMID: 11844127](https://pubmed.ncbi.nlm.nih.gov/11844127/)).
- **Inheritance:** **None** — not genetic; no inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency applies.
- **Demographics:** worldwide, no defined endemic regions; **apparent male predominance**; **all ages** including children; risk clusters in the immunocompromised. A recent Mexican case series adds regional data ([PMID: 42220824](https://pubmed.ncbi.nlm.nih.gov/42220824/)).

> "Botryomycosis occurs more commonly among immunocompromised patients, although some cases have also been reported in immunocompetent patients." — [PMID: 32173890](https://pubmed.ncbi.nlm.nih.gov/32173890/)

### 10. Diagnostics

**Diagnosis rests on histopathology + culture.**
- **Biopsy/histopathology:** suppurative/pyogranulomatous inflammation with **bacterial grains** surrounded by an **eosinophilic Splendore-Hoeppli** matrix and radiating "clubs"; grains contain Gram-positive cocci or Gram-negative bacilli and are **PAS/Grocott positive but lack filaments** (distinguishing from actinomycosis/mycetoma) ([PMID: 32173890](https://pubmed.ncbi.nlm.nih.gov/32173890/); [PMID: 28034470](https://pubmed.ncbi.nlm.nih.gov/28034470/); [PMID: 15456177](https://pubmed.ncbi.nlm.nih.gov/15456177/)).
- **Microbiology/culture:** essential to identify the organism and guide therapy.
- **Imaging:** X-ray/MRI for bone invasion; CT for pulmonary/sinonasal masses (often reveals a mass mimicking neoplasm with osseous erosion).
- **Genetic/omics testing:** **not applicable.**
- **Clinical criteria:** no formal DSM/ICD diagnostic criteria; diagnosis is pathologic.
- **Differential diagnosis:** **mycetoma** (grains contain filaments; fungal or actinomycetoma), **actinomycosis** (filamentous Gram-positive), and **malignancy** (lung cancer, sarcoma, liposarcoma, sinonasal tumor). Note histologic overlap with fungal infections showing Splendore-Hoeppli (e.g., basidiobolomycosis — [PMID: 42266393](https://pubmed.ncbi.nlm.nih.gov/42266393/)), reinforcing the need for special stains and culture.

> "The diagnosis of botryomycosis is based on culture of the granules revealing gram-positive cocci or gram-negative bacilli." — [PMID: 23743320](https://pubmed.ncbi.nlm.nih.gov/23743320/)

> "In immunocompromised patients, botryomycosis can resemble fungal infection both clinically and histologically; therefore, definitive diagnosis requires tissue sampling along with histological and microbiological analysis." — [PMID: 38036751](https://pubmed.ncbi.nlm.nih.gov/38036751/)

### 11. Outcome / Prognosis

- **Survival/mortality:** generally **good** for localized cutaneous disease with combined therapy; **fatal outcomes** occur with disseminated visceral disease and uncontrolled immunodeficiency (fatal AIDS-associated case — [PMID: 38036751](https://pubmed.ncbi.nlm.nih.gov/38036751/); fatal disseminated visceral case probably due to *P. aeruginosa* — [PMID: 13845294](https://pubmed.ncbi.nlm.nih.gov/13845294/)). No formal survival statistics exist.
- **Morbidity/function:** disfigurement, chronic drainage, limb dysfunction, bone destruction.
- **Complications:** osteomyelitis, sepsis/bacteremia with pulmonary abscesses ([PMID: 28034470](https://pubmed.ncbi.nlm.nih.gov/28034470/)), dissemination.
- **Recovery:** cure achievable; **recurrence is common** and long therapy is required.
- **Prognostic factors:** host immune status (dominant), lesion extent/depth (bone/visceral), organism, and timeliness of diagnosis. No molecular prognostic biomarkers.

### 12. Treatment

**Principle: prolonged, culture-directed antibiotics + surgical debridement/excision, plus immune restoration when relevant.**

| Regimen / intervention | Setting | Outcome | Source |
|---|---|---|---|
| Excision + oral TMP-SMX (240 mg b.i.d.) × 2 wk | Immunocompetent child, cutaneous | No recurrence | [PMID: 32173890](https://pubmed.ncbi.nlm.nih.gov/32173890/) |
| Excision + penicillin G → clindamycin + cotrimoxazole × 18 mo | Scalp granular bacteriosis | Disease-free at 4 y | [PMID: 19094129](https://pubmed.ncbi.nlm.nih.gov/19094129/) |
| Cefazolin | Red-grain *S. aureus* foot | Responded well | [PMID: 19736413](https://pubmed.ncbi.nlm.nih.gov/19736413/) |
| Fluoroquinolone (vs *A. actinomycetemcomitans*) | Hand, dual infection | Resolved only after fluoroquinolone | [PMID: 17500377](https://pubmed.ncbi.nlm.nih.gov/17500377/) |
| Cloxacillin-gentamicin → rifampicin-ofloxacin × 2 mo | *S. aureus* sepsis + pulmonary abscesses | Managed bacteremia | [PMID: 28034470](https://pubmed.ncbi.nlm.nih.gov/28034470/) |
| Antiretroviral therapy (darunavir + raltegravir) | HIV facial pyoderma | Remission at 5 y after ART | [PMID: 28562771](https://pubmed.ncbi.nlm.nih.gov/28562771/) |
| Complete surgical evacuation | Sinonasal "bacterial ball" | Curative | [PMID: 15456177](https://pubmed.ncbi.nlm.nih.gov/15456177/) |

- **Pharmacotherapy classes / NCIT anchors:** TMP-SMX (**NCIT:C1055**), penicillins, clindamycin, cephalosporins (cefazolin), fluoroquinolones (ofloxacin), rifampicin, aminoglycosides (gentamicin) — chosen by culture/sensitivity.
- **Surgical:** debridement/excision (**NCIT:C51696**, debridement); complete evacuation can be curative for localized visceral/mucosal disease.
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno-oncology):** **Not applicable.**
- **Pharmacogenomics:** not applicable.
- **Strategy:** combine surgery + long antibiotics; **always assess/treat immune status** (ART in HIV). Recurrence-prone → extended courses.

> "Surgical debridement is the treatment of choice in such cases with an assessment of the immune status. Long term antibiotic treatment is required in all conditions as recurrence is common." — [PMID: 29039982](https://pubmed.ncbi.nlm.nih.gov/29039982/)

> "The patient was successfully treated by excision and oral trimethoprim/sulfamethoxazole (240 mg b.i.d.) for 2 weeks as adjuvant therapy. No recurrence was noted following treatment." — [PMID: 32173890](https://pubmed.ncbi.nlm.nih.gov/32173890/)

### 13. Prevention

- **Primary prevention:** good **wound care** and prompt treatment of skin infections; management of predisposing conditions (control HIV with ART, control diabetes, address malnutrition/alcoholism).
- **Secondary prevention:** early biopsy of chronic non-healing nodules/sinuses to diagnose before deep/visceral spread and to avoid unnecessary oncologic surgery.
- **Tertiary prevention:** prolonged antibiotics + surgery to prevent recurrence, bone destruction, and dissemination; immune restoration.
- **Immunization / genetic screening / counseling:** **Not applicable** (no vaccine; not heritable).
- **Public health:** general infection-control and immunosuppression management; no vector control needed.

### 14. Other Species / Natural Disease

Botryomycosis is a genuine **cross-species (shared-agent) disease** — the same bacteria and the same host-response pathology occur in animals and humans, though it is not classically transmitted person-to-person or animal-to-person.
- **Taxonomy of hosts:** horse (*Equus caballus*), cattle (*Bos taurus*), swine (*Sus scrofa*), guinea pig (experimental), and human (*Homo sapiens*).
- **Natural disease:** most common as equine **wound infection** (castration site / "scirrhous cord," spermatic-cord granuloma) and as **mastitis** in cows and sows; rare pulmonary disease (documented in a Scottish Highland steer, *S. aureus* cultured — [PMID: 11243368](https://pubmed.ncbi.nlm.nih.gov/11243368/)).
- **Comparative pathology:** histology in animals **matches** human disease — pyogranulomatous inflammation with eosinophilic grains and radiating clubs around Gram-positive cocci — indicating a **conserved host-response mechanism** across mammals.
- **Orthologous genes:** not applicable (no host causal gene).

> "Among domestic species, staphylococcal botryomycosis is most common as a wound infection in horses or as mastitis in cows and sows." — [PMID: 11243368](https://pubmed.ncbi.nlm.nih.gov/11243368/)

### 15. Model Organisms

- **Genetic models:** **None** — because the disease has no genetic basis, there are no knockout/knock-in/transgenic models.
- **Induced/experimental models:** historically, **guinea pigs** were used to study experimental botryomycosis (pulmonary botryomycosis noted "rare in horses, humans, and guinea pigs" — [PMID: 11243368](https://pubmed.ncbi.nlm.nih.gov/11243368/)); naturally occurring disease in **horses, cattle, swine** serves as the comparative/large-animal model.
- **Applications:** these models illuminate grain formation, the Splendore-Hoeppli response, and the host-immunity/bacterial-infectivity balance.
- **Limitations:** no standardized modern model organism system; mechanistic detail (steps 4–5 of the causal chain) remains under-characterized.

---

## Mechanistic Model / Interpretation

```
[Trauma / surgery / foreign body]
            │  inoculation of common bacteria (usually S. aureus)
            ▼
   Bacteria in tissue ──────────────► (adequate immunity) ─► abscess resolves / cured  [NO disease]
            │
            │  impaired cell-mediated immunity  ×  bacterial infectivity balance
            ▼
   Failure to eradicate, failure to form ordinary abscess
            │
            ▼
   Bacterial AGGREGATION into compact colonies (GRAINS)
            │
            ▼
   Splendore-Hoeppli COAT  (host Ig + complement + eosinophil products; ± bacterial glycocalyx)   [INFERRED shielding]
            │  shields from phagocytosis + antibiotic penetration
            ▼
   CHRONIC PYOGRANULOMATOUS INFLAMMATION (neutrophils, macrophages, giant cells, plasma cells, fibrosis)
            │
            ├──► Cutaneous: nodules, sinuses, fistulae, ulcers ─► deep tissue/BONE invasion
            └──► Visceral: pulmonary mass (mimics carcinoma) ─► dissemination ─► FATAL (if immunodeficiency uncontrolled)
```

The unifying interpretation is that **botryomycosis is not a distinct pathogen's disease but an aberrant, grain-forming host response to ordinary bacteria**, gated by host immunity. This explains its three defining clinical truths: it *mimics* malignancy/mycetoma/actinomycosis (because grains + granulomatous mass resemble tumors and other grain diseases); it is *curable* (because the organisms are common and antibiotic-susceptible); and it is *recurrence-prone and dangerous in immunodeficiency* (because the permissive lesion is the host's failed clearance, best fixed by restoring immunity alongside antibiotics and surgery).

---

## Evidence Base

| PMID | Title (abbrev.) | Role in report |
|---|---|---|
| [41128794](https://pubmed.ncbi.nlm.nih.gov/41128794/) | *Cutaneous botryomycosis: a comprehensive review* | Etiology (S. aureus > P. aeruginosa), lesion morphology, treatment, differential dx |
| [37787361](https://pubmed.ncbi.nlm.nih.gov/37787361/) | *Primary pulmonary botryomycosis* | Two forms; visceral rarity; pulmonary predominance |
| [32173890](https://pubmed.ncbi.nlm.nih.gov/32173890/) | *Cutaneous botryomycosis in an 8-yo immunocompetent boy* | Splendore-Hoeppli histology; occurrence in immunocompetent; TMP-SMX cure |
| [38036751](https://pubmed.ncbi.nlm.nih.gov/38036751/) | *Botryomycosis mimicking sarcoma / AIDS presentation* | Immunocompromised predominance; need for tissue + microbiology; fatal outcome |
| [28562771](https://pubmed.ncbi.nlm.nih.gov/28562771/) | *Facial botryomycosis-like pyoderma in HIV* | Cellular immunity link; ART-induced remission |
| [18177488](https://pubmed.ncbi.nlm.nih.gov/18177488/) | *S. aureus + P. carinii in AIDS* | Dual host-immune × microbial pathogenesis |
| [9435048](https://pubmed.ncbi.nlm.nih.gov/9435048/) | *Botryomycosis mimicking a liposarcoma* | "Atypical host reaction" framing; cancer mimicry |
| [23743320](https://pubmed.ncbi.nlm.nih.gov/23743320/) | *Pulmonary botryomycosis mimicking lung cancer* | Culture-based diagnosis; "pathobiology remains unknown" |
| [11844127](https://pubmed.ncbi.nlm.nih.gov/11844127/) | *Primary pulmonary botryomycosis vs lung cancer* | Curable differential of lung cancer; rarity |
| [11243368](https://pubmed.ncbi.nlm.nih.gov/11243368/) | *Pulmonary botryomycosis in a Scottish Highland steer* | Animal disease; conserved pyogranulomatous grain histology |
| [30429406](https://pubmed.ncbi.nlm.nih.gov/30429406/) | *Cutaneous botryomycosis of the foot* | Deep tissue/bone invasion; destruction/disfigurement |
| [15456177](https://pubmed.ncbi.nlm.nih.gov/15456177/) | *Sinonasal "bacterial ball" (P. aeruginosa)* | Mucosal disease; neoplasm mimic; surgical cure |
| [17500377](https://pubmed.ncbi.nlm.nih.gov/17500377/) | *A. actinomycetemcomitans botryomycosis* | Non-staph etiology; fluoroquinolone cure |
| [28034470](https://pubmed.ncbi.nlm.nih.gov/28034470/) | *Cutaneous granular bacteriosis in S. aureus septicaemia* | Splendore-Hoeppli, immunosuppression (MTX), dual antibiotics |
| [19094129](https://pubmed.ncbi.nlm.nih.gov/19094129/) | *Granular bacteriosis of head/neck* | 18-month triple antibiotics + surgery; 4-year cure |
| [29039982](https://pubmed.ncbi.nlm.nih.gov/29039982/) | *Botryomycosis of the lacrimal sac* | Surgery + long antibiotics; immune assessment; recurrence |
| [19736413](https://pubmed.ncbi.nlm.nih.gov/19736413/) | *Red-grain botryomycosis (S. aureus)* | Grain color variant; cefazolin response |
| [13845294](https://pubmed.ncbi.nlm.nih.gov/13845294/) | *Disseminated visceral botryomycosis (fatal)* | Fatal P. aeruginosa dissemination |
| [12602981](https://pubmed.ncbi.nlm.nih.gov/12602981/) | *Botryomycosis in HIV* | AIDS ulcers; excision + antimicrobials |
| [11001122](https://pubmed.ncbi.nlm.nih.gov/11001122/) | *Botryomycosis in a child with AIDS* | Pediatric immunocompromised case |
| [42220824](https://pubmed.ncbi.nlm.nih.gov/42220824/) | *Case series, Mexico* | Regional case series; non-filamentous organisms |
| [33061472](https://pubmed.ncbi.nlm.nih.gov/33061472/) | *MRSA botryomycosis* | MRSA as agent |
| [5235476](https://pubmed.ncbi.nlm.nih.gov/5235476/) | *Botryomycosis of the tongue* | Mucosal (oral) site |

Papers on gastrointestinal basidiobolomycosis ([PMID: 42266393](https://pubmed.ncbi.nlm.nih.gov/42266393/), [42471849](https://pubmed.ncbi.nlm.nih.gov/42471849/), [41634777](https://pubmed.ncbi.nlm.nih.gov/41634777/), [42776653](https://pubmed.ncbi.nlm.nih.gov/42776653/)) are **not botryomycosis** but were reviewed because they share the Splendore-Hoeppli phenomenon and the "mimics malignancy/IBD" behavior — they usefully delimit botryomycosis from its fungal histologic look-alikes and underscore that Splendore-Hoeppli is non-specific.

---

## Limitations and Knowledge Gaps

1. **Evidence quality is low-tier:** the entire knowledge base is case reports/series and narrative reviews — no cohorts, no trials, no registries. All frequencies are qualitative.
2. **No epidemiologic denominators:** true incidence/prevalence, sex ratio, and geographic distribution are unknown.
3. **Mechanism partly inferred:** steps 4–5 (Splendore-Hoeppli shielding, biofilm/glycocalyx role) are hypotheses; "the pathobiology remains unknown" ([PMID: 23743320](https://pubmed.ncbi.nlm.nih.gov/23743320/)). The molecular determinants of why the *same* bacteria cause a grain-forming granuloma in one host and a simple abscess in another are undefined.
4. **No standardized treatment protocol:** antibiotic choice, duration, and the surgery-vs-medical-therapy balance are empirical and heterogeneous.
5. **No molecular/omics data** and no modern model organism system exist for this disease.

## Proposed Follow-up Experiments / Actions

1. **Systematic pooled analysis** of published cases (extract organism, host immune status, site, therapy, duration, recurrence, outcome) to derive quantitative treatment-response and recurrence rates.
2. **Mechanistic studies of grain formation:** compare biofilm/glycocalyx and Splendore-Hoeppli matrix composition (host Ig/complement/eosinophil MBP) between botryomycosis grains and ordinary abscesses; test whether cell-mediated immune deficiency is *necessary* using immunodeficient vs immunocompetent animal inoculation models.
3. **Prospective diagnostic pathway** in chronic non-healing cutaneous nodules/pulmonary masses: mandate biopsy + culture + special stains (Gram/PAS/Grocott) before oncologic resection, to quantify avoided surgeries.
4. **Molecular characterization** of *S. aureus*/*P. aeruginosa* isolates (virulence/biofilm genotypes) from grains vs matched abscesses to test the "microbial infectivity" arm of the causal model.
5. **Immune-restoration studies:** formally evaluate adjunctive ART/immune optimization outcomes in HIV-associated botryomycosis versus antibiotics/surgery alone.

---

*Ontology anchors used in this report:* MONDO:0400006; MeSH D001857; NCBITaxon:1280 (*S. aureus*), NCBITaxon:287 (*P. aeruginosa*); UBERON:0002097 (skin), UBERON:0002048 (lung), UBERON:0001474 (bone); HP:0100829 (abscess), HP:0030757 (fistula), HP:0200042 (skin ulcer), HP:0002754 (osteomyelitis); GO:0006954 (inflammatory response), GO:0006909 (phagocytosis), GO:0002455 (humoral immune response); CL:0000775 (neutrophil), CL:0000235 (macrophage), CL:0000771 (eosinophil); NCIT:C1055 (TMP-SMX), NCIT:C51696 (debridement).


## Artifacts

- [OpenScientist final report](Botryomycosis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Botryomycosis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 16 |
| Quoted claims found in source | 16 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 27 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 19 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0031804` (1 mention) - the report calls it "nodular skin lesion"; HP calls it **obsolete Premacular hemorrhage**
- `HP:0100829` (2 mentions) - the report calls it "abscess"; HP calls it **Galactorrhea**
- `HP:0030757` (2 mentions) - the report calls it "fistula"; HP calls it **Tooth abscess**
- `NCIT:C1055` (2 mentions) - the report calls it "TMP-SMX"; NCIT calls it **Custirsen Sodium**
- `NCIT:C51696` (2 mentions) - the report calls it "debridement"; NCIT calls it **Orthotopic Liver Transplantation**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0031804` (obsolete Premacular hemorrhage) (1 mention) - replaced by `HP:0025240`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:1280` (3 mentions) - the report calls it "Staphylococcus aureus", "S. aureus"; NCBITaxon calls it **Staphylococcus aureus**, and lists "Micrococcus aureus" among its other names
- `NCBITaxon:287` (3 mentions) - the report calls it "Pseudomonas aeruginosa", "P. aeruginosa"; NCBITaxon calls it **Pseudomonas aeruginosa**
- `GO:0002455` (2 mentions) - the report calls it "humoral immune response"; GO calls it **humoral immune response mediated by circulating immunoglobulin**, and lists "humoral immune response mediated by circulating antibody" among its other names
- `UBERON:0002097` (2 mentions) - the report calls it "skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `UBERON:0001474` (2 mentions) - the report calls it "bone"; UBERON calls it **bone element**, and lists "bone" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCBITaxon:1280` - called "Staphylococcus aureus", "S. aureus"
- `NCBITaxon:287` - called "Pseudomonas aeruginosa", "P. aeruginosa"