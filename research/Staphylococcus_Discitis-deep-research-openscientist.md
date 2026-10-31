---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T02:35:09.506935'
end_time: '2026-09-30T02:48:56.926030'
duration_seconds: 827.42
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Staphylococcus Discitis
  mondo_id: MONDO:8000001
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
citation_count: 28
reference_validation:
  total_references: 29
  verified: 29
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 29
  on_topic: 19
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 21
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 7
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: UBERON:0002103
    reported_labels:
    - intervertebral disc
    ontology_label: hindlimb
  - term_id: HP:0500152
    reported_labels:
    - radicular pain
    ontology_label: Hypocystinemia
  - term_id: HP:0012062
    reported_labels:
    - epidural abscess
    ontology_label: Bone cyst
  - term_id: NCIT:C1338
    reported_labels:
    - Vancomycin
    ontology_label: Didox
  - term_id: NCIT:C61735
    reported_labels:
    - Linezolid
    ontology_label: Dolasetron
  - term_id: NCIT:C157866
    reported_labels:
    - Daptomycin
    ontology_label: Gluten Free Diet
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Staphylococcus_Discitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Staphylococcus_Discitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Staphylococcus Discitis
- **MONDO ID:** MONDO:8000001 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Staphylococcus Discitis** covering all of the
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

# Staphylococcus Discitis: A Comprehensive Disease Characterization

*Infectious Disease | MONDO:8000001 | Category: Infectious Disease*

---

## Summary

**Staphylococcus discitis is an acquired bacterial infection of the intervertebral disc and adjacent vertebral endplates/bodies, caused predominantly by *Staphylococcus aureus* (MSSA or MRSA).** It is not a genetic or heritable disorder; rather, it is one manifestation along a contiguous spectrum of spine infection that includes discitis, vertebral osteomyelitis, and epidural abscess. A landmark pediatric study concluded that non-tuberculous spondylodiscitis "is truly osteomyelitis of the spine" ([PMID: 11961447](https://pubmed.ncbi.nlm.nih.gov/11961447/)), and contemporary reviews define vertebral osteomyelitis as "a general term for a heterogenous group of spine infections involving the vertebral bone, intervertebral discs, and facet joints" ([PMID: 40204566](https://pubmed.ncbi.nlm.nih.gov/40204566/)). Because it is infectious rather than Mendelian, entire categories in a classic disease template — OMIM inheritance, causal germline variants, penetrance, anticipation, founder effects — are **not applicable**; only polygenic host susceptibility to invasive *S. aureus* is relevant.

The disease chiefly affects **older adults** (mean age ~71 years, ~61% male in a Japanese nationwide cohort of 71,134 patients) with an incidence of roughly **3 cases per 100,000 per year**, plus a distinct **toddler subgroup** (mean age ~4.5 years) in which *S. aureus* and *Kingella kingae* dominate. The **lumbar spine** is most commonly affected (63%), and the classic presentation is **back pain** (~79%) with **fever** (~72%) and elevated inflammatory markers. Diagnosis rests on **contrast-enhanced MRI** (imaging gold standard) supplemented by **18F-FDG PET/CT** and confirmed by **blood culture or image-guided biopsy**. Bone destruction is driven mechanistically by *S. aureus*–induced osteoblast and immune signaling: surface protein A binds osteoblast **TNFR-1**, activating **JNK/TLR2** signaling and driving **RANKL**-mediated osteoclastic bone resorption.

Management combines **pathogen-directed antibiotics** — a **6-week course was proven non-inferior to 12 weeks** in a 359-patient randomized controlled trial — with **surgery** reserved for neurologic deficit, spinal instability, drainable abscess, or medical failure. **Timely surgery (≤14 days)** improved survival in staphylococcal cohorts. Prognosis is generally favorable but not benign: **mortality is ~3–12%**, **relapse ~6–17%**, and **residual disability ~20–30%**, with radicular nerve damage and epidural/paravertebral abscess being frequent complications. Novel salvage options (dalbavancin, bacteriophage therapy) are emerging for refractory or multidrug-resistant disease.

---

## Key Findings

### Finding 1 — *S. aureus* is the leading causative pathogen of pyogenic spondylodiscitis

Across geographically diverse cohorts, *Staphylococcus aureus* is consistently the single most common organism. In a 14-year retrospective study of 98 infectious spondylodiscitis patients from Trieste, *S. aureus* accounted for 34 cases — **64% of pyogenic spondylodiscitis** ([PMID: 41023355](https://pubmed.ncbi.nlm.nih.gov/41023355/)): *"Staphylococcus aureus was the most common pathogen, with 34 cases, representing 64% of pyogenic spondylodiscitis."* A Danish cohort of 106 pyogenic vertebral osteomyelitis patients found **39% *S. aureus*** ([PMID: 34091001](https://pubmed.ncbi.nlm.nih.gov/34091001/)): *"39% were infected with Staphylococcus aureus and 9% with Escherichia coli."* In the largest dataset — a Japanese nationwide database of 71,134 pyogenic spondylodiscitis patients — **MRSA alone comprised 11.9%** ([PMID: 39716636](https://pubmed.ncbi.nlm.nih.gov/39716636/)), and in surgically treated US spinal infections MRSA reached 43%. This establishes *S. aureus* — spanning both methicillin-susceptible (MSSA) and methicillin-resistant (MRSA) strains — as the defining pathogen of the disease entity.

### Finding 2 — Epidemiology: ~3/100,000/yr incidence, elderly male predominance, lumbar predilection

The incidence of infectious spondylodiscitis is reported at **3 cases per 100,000 inhabitants per year** ([PMID: 41023355](https://pubmed.ncbi.nlm.nih.gov/41023355/)). The Japanese nationwide cohort documented a **mean age of 71.05 years and 60.9% male** ([PMID: 39716636](https://pubmed.ncbi.nlm.nih.gov/39716636/)): *"The average age of patients was 71.05 years, and 60.9% of patients were male."* Anatomically, disease favors the **lumbar spine (63%)**, followed by thoracic (25%) and cervical (12%) ([PMID: 41023355](https://pubmed.ncbi.nlm.nih.gov/41023355/)). Presenting symptoms are dominated by back pain (~79%) and fever (~72%). The suggested anatomical ontology anchor is **UBERON:0002103 (intervertebral disc)**, with lumbar region UBERON:0002792.

| Feature | Value | Source |
|---|---|---|
| Incidence | 3 / 100,000 / yr | [PMID: 41023355](https://pubmed.ncbi.nlm.nih.gov/41023355/) |
| Mean age | 71.05 yr | [PMID: 39716636](https://pubmed.ncbi.nlm.nih.gov/39716636/) |
| Male proportion | 60.9% | [PMID: 39716636](https://pubmed.ncbi.nlm.nih.gov/39716636/) |
| Lumbar / thoracic / cervical | 63% / 25% / 12% | [PMID: 41023355](https://pubmed.ncbi.nlm.nih.gov/41023355/) |

### Finding 3 — Pediatric discitis: young children, *S. aureus* and *Kingella kingae*, good outcome

A distinct pediatric form affects toddlers. In 42 children with non-tuberculous spondylodiscitis (mean age 4 years 6 months), bacteria were isolated in 22/35 samples: **55% *S. aureus*, 27% *Kingella kingae***, and one *Coxiella burnetii* ([PMID: 11961447](https://pubmed.ncbi.nlm.nih.gov/11961447/)): *"Bacteria were isolated in 22 of the 35 samples taken (55% Staphylococcus aureus, 27% Kingella kingae; Coxiella burnetii in one sample)."* Diagnosis was frequently delayed (mean 42 days). Functional outcome is generally good with appropriate treatment, though long-term disc fibrosis and occasional vertebral fusion develop. Crucially, the authors framed discitis as a spinal osteomyelitis — *"nontuberculous spondylodiscitis is truly osteomyelitis of the spine"* — reinforcing the unified nosology (Finding 13).

### Finding 4 — MRSA risk factors: smoking, IV drug use, thoracic involvement, more complications

MRSA disease carries a distinct risk profile. In a US cohort of 205 surgical spinal infections, MRSA (43%) versus non-MRSA patients had significantly higher **current smoking (57% vs 40%, p=.021), IV drug use (49% vs 33%, p=.021), thoracic involvement (43% vs 28%, p=.039), and epidural abscess (65% vs 45%, p=.005)** ([PMID: 40653018](https://pubmed.ncbi.nlm.nih.gov/40653018/)). More generally, predictors of inadequate treatment response include **previous spinal surgery (aOR 19.29; 95% CI 2.20–169.08) and severe sepsis (aOR 4.59; 95% CI 1.28–15.41)** ([PMID: 34091001](https://pubmed.ncbi.nlm.nih.gov/34091001/)). Diabetes mellitus, prior spinal instrumentation, bacteremia, and immunosuppression are recurrent risk themes across cohorts.

### Finding 5 — Six weeks of antibiotics is non-inferior to twelve weeks (RCT)

The pivotal therapeutic evidence is an open-label, non-inferiority randomized controlled trial (NCT00764114) of **359 patients across 71 French centers** with microbiologically confirmed pyogenic vertebral osteomyelitis, randomized to 6 versus 12 weeks of antibiotics ([PMID: 25468170](https://pubmed.ncbi.nlm.nih.gov/25468170/)): *"We aimed to establish whether 6 weeks of antibiotic treatment is non-inferior to 12 weeks in patients with pyogenic vertebral osteomyelitis."* Using a masked committee endpoint of cure at 1 year and a non-inferiority margin of 10%, **6 weeks proved non-inferior to 12 weeks**. This finding is now embedded in AO Spine recommendations ([PMID: 39852953](https://pubmed.ncbi.nlm.nih.gov/39852953/)) as a conditional recommendation for a 6-week course in confirmed cases.

### Finding 6 — Mechanism: protein A → TNFR-1 → JNK/TLR2 → RANKL-driven bone destruction

The molecular pathophysiology of staphylococcal bone destruction has been dissected in vitro. *S. aureus* surface **protein A (SpA) binds directly to pre-osteoblastic cells via TNF receptor-1 (TNFR-1)** ([PMID: 26846887](https://pubmed.ncbi.nlm.nih.gov/26846887/)): *"the S. aureus protein SpA binds directly to pre-osteoblastic cells via tumor necrosis factor receptor-1 (TNFR-1)."* Infection decreased osteoblast viability and increased apoptosis, TLR2 expression, and TNF-α/IL-6 secretion, with activation of the **JNK pathway**. Critically, *"Knockdown of TNFR1 not only inhibited the JNK pathway but also reduced TLR2 protein and RANKL levels in S. aureus-infected cells"* — linking the receptor interaction to **RANKL-driven osteoclastic bone resorption**, the effector of the "widespread bone loss and destruction" characteristic of osteomyelitis.

**Suggested ontology terms:** GO:0045672 (regulation of osteoclast differentiation), GO:0007254 (JNK cascade), GO:0002224 (toll-like receptor signaling pathway), GO:0006954 (inflammatory response); CL:0000062 (osteoblast), CL:0000092 (osteoclast).

### Finding 7 — Diagnosis: MRI is the gold standard; 18F-FDG PET/CT is a complementary adjunct

Contrast-enhanced MRI is the imaging cornerstone, with PET/CT adding complementary value. A prospective head-to-head comparison (n=26 haematogenous spondylodiscitis, 18 confirmed) found **18F-FDG PET/CT sensitivity 83%, specificity 88%, PPV 94%, NPV 70%; MRI sensitivity 94%, specificity 38%, PPV 77%, NPV 75%** ([PMID: 25186431](https://pubmed.ncbi.nlm.nih.gov/25186431/)): *"The sensitivity, specificity, and positive and negative predictive value were 83%, 88%, 94% and 70% for (18)F-FDG PET/CT, and 94%, 38%, 77% and 75% for MRI, respectively."* A retrospective cohort (n=191) showed combining modalities raised sensitivity: *"sensitivity was 56% for FDG-PET/CT and 62% for MRI, increasing to 74% when both modalities were combined (p = 0.002)"* ([PMID: 42232200](https://pubmed.ncbi.nlm.nih.gov/42232200/)). MRI accuracy is time-dependent: *"Diagnostic accuracy was 58%, when MRI was performed within 2 weeks after the start of symptoms and improved to 82%, when performed more than 2 weeks after onset of symptoms"* ([PMID: 27317050](https://pubmed.ncbi.nlm.nih.gov/27317050/)). Microbiological confirmation via blood culture or image-guided biopsy remains essential; open/intraoperative sampling yields more positives than percutaneous (RR 1.65, 95% CI 1.34–2.03) ([PMID: 41519476](https://pubmed.ncbi.nlm.nih.gov/41519476/)).

| Modality | Sensitivity | Specificity | PPV | NPV |
|---|---|---|---|---|
| 18F-FDG PET/CT | 83% | 88% | 94% | 70% |
| MRI | 94% | 38% | 77% | 75% |

*Source: [PMID: 25186431](https://pubmed.ncbi.nlm.nih.gov/25186431/)*

### Finding 8 — Prognosis: mortality 3–12%, frequent abscess/neurologic complications, relapse 6–17%

Outcomes are generally favorable but complications are common. The Trieste cohort (n=98) reported **radicular nerve damage (51%), epidural/paravertebral abscesses (45%), endocarditis (14%), need for surgery (8%), persistent neurological sequelae (3%), and infection-related mortality 6%** ([PMID: 41023355](https://pubmed.ncbi.nlm.nih.gov/41023355/)). The Danish PVO cohort reported **13% relapse within 2 years and 1-year crude mortality of 12%** ([PMID: 34091001](https://pubmed.ncbi.nlm.nih.gov/34091001/)). A surgical *Staphylococcus* cohort reported **1-year overall survival 76% and recurrence-free survival 58%** ([PMID: 42314843](https://pubmed.ncbi.nlm.nih.gov/42314843/)): *"The 1-year OS and RFS were 76% and 58%, respectively."* A systematic review of culture-negative versus culture-positive disease reported recurrence 6–17% and residual disability 20–30% ([PMID: 42262500](https://pubmed.ncbi.nlm.nih.gov/42262500/)). Concurrent infections (especially cardiac, CNS, pneumonia) roughly quadruple early mortality (3.3% vs 0.8%) ([PMID: 37148755](https://pubmed.ncbi.nlm.nih.gov/37148755/)).

### Finding 9 — Animal models: the New Zealand White rabbit is the established model

Staphylococcal discitis has a well-validated animal model. Percutaneous fluoroscopy-guided inoculation of *S. aureus* into rabbit lumbar discs reproducibly produces disease. Bierry et al. (12 NZW rabbits) found **disc-space infections in all animals**, with MRI detecting abnormalities 5–10 days post-inoculation ([PMID: 18485785](https://pubmed.ncbi.nlm.nih.gov/18485785/)): *"Disc space infections were present in all animals. MRI detected vertebral and discal abnormalities as soon as, respectively, 5 and 10 days after inoculation."* The model has been used for antibiotic-penetration studies — clindamycin penetrated the nucleus pulposus at 11.9–20% of serum versus cephazolin's 0.68–0.77% ([PMID: 24043368](https://pubmed.ncbi.nlm.nih.gov/24043368/)) — and comparative pathogen studies showing *S. aureus* produces true discitis with higher death rates (2/3) than *P. acnes* ([PMID: 26925420](https://pubmed.ncbi.nlm.nih.gov/26925420/)). Histology recapitulates disc-space narrowing, endplate erosion/hyperostosis, epidural abscess, and paraplegia. **Model organism:** *Oryctolagus cuniculus* (NCBI:txid9986).

### Finding 10 — Host genetic susceptibility to invasive *S. aureus* is polygenic (iron regulation)

There is **no monogenic cause** of staphylococcal discitis — it is an acquired infectious disease. Host susceptibility to invasive *S. aureus* is multifactorial/polygenic. A multi-site African GWAS (n=3,928 children plus replication) found the **CHCHD7/SDR16C5 variant rs73596248**, which increases hepcidin, *"is associated with reduced risk of Klebsiella pneumoniae and Staphylococcus aureus bacteremia"* ([PMID: 41946712](https://pubmed.ncbi.nlm.nih.gov/41946712/)), linking iron regulation to host–pathogen susceptibility. Classic monogenic immunodeficiencies that predispose to staphylococcal disease include Job/hyper-IgE syndrome (**STAT3, DOCK8**), chronic granulomatous disease (**CYBB**/NADPH oxidase), and **IRAK4/MyD88** deficiency (impaired TLR/IL-1 signaling) — but these are rare and not specific to discitis.

### Finding 11 — Salvage/novel therapeutics: dalbavancin and bacteriophage therapy

For refractory or difficult-to-treat staphylococcal spinal infection, novel options are emerging. **Dalbavancin**, a long-acting lipoglycopeptide, was studied in 83 bone/joint infections (48.2% vertebral osteomyelitis/spondylodiscitis) and *"offers a simplified alternative"* to prolonged IV therapy ([PMID: 41305347](https://pubmed.ncbi.nlm.nih.gov/41305347/)). A striking case of **systemic bacteriophage therapy** in a 60-year-old woman with chronic implant-associated MRSA vertebral osteomyelitis and antibiotic hypersensitivity used 35 IV doses of 10⁹ PFU anti-staphylococcal phage ([PMID: 41478341](https://pubmed.ncbi.nlm.nih.gov/41478341/)): *"Systemic bacteriophage therapy was well tolerated, with no adverse events observed. The treatment resulted in sustained clinical improvement and normalization of inflammatory markers,"* with no relapse 6 months after stopping all antibiotics. First-line therapy remains anti-staphylococcal penicillins/cefazolin (MSSA) and vancomycin/daptomycin/linezolid (MRSA), with rifampicin added for implant/biofilm-associated disease.

### Finding 12 — Treatment strategy: antibiotics ± surgery, with defined surgical indications

Management combines pathogen-directed antibiotics (per IDSA 2015 guidelines, [PMID: 26229122](https://pubmed.ncbi.nlm.nih.gov/26229122/)) with surgery for specific indications. Predictors of needing surgery (n=80) include **pyogenic etiology (81.6% vs 38.1%, p<0.001), thoracic localization (36.8% vs 16.7%, p=0.04), epidural abscess (52.6% vs 11.9%, p<0.001), psoas abscess (21.1% vs 4.8%, p<0.001), and Gram-positive coccal infection (50% vs 7.1%, p<0.001)** ([PMID: 40762806](https://pubmed.ncbi.nlm.nih.gov/40762806/)). **Timely surgery (≤14 days)** improved outcomes in staphylococcal spondylodiscitis: *"timely surgery (≤14 days) were associated with improved outcomes, demonstrating significantly better OS (HR: 0.18, p=.003; HR: 0.22, p=.019) and RFS"* ([PMID: 42314843](https://pubmed.ncbi.nlm.nih.gov/42314843/)). Conservative treatment remains viable for neurologically intact patients ([PMID: 39119368](https://pubmed.ncbi.nlm.nih.gov/39119368/)). Standard surgical indications: neurologic deficit, spinal instability/deformity, large/drainable abscess, medical failure, and need for microbiological diagnosis.

### Finding 13 — Nosology: staphylococcal discitis is part of the spondylodiscitis/vertebral osteomyelitis spectrum

Discitis, vertebral osteomyelitis, and epidural abscess form a **contiguous spine-infection spectrum**. A 2025 review defines vertebral osteomyelitis as *"a general term for a heterogenous group of spine infections involving the vertebral bone, intervertebral discs, and facet joints"* that *"spread contiguously to adjacent paraspinal structures, including paravertebral muscles and the epidural space,"* with *"nonspecific and indolent symptoms, which can delay diagnosis"* ([PMID: 40204566](https://pubmed.ncbi.nlm.nih.gov/40204566/)). The pediatric conclusion that discitis *"is truly osteomyelitis of the spine"* ([PMID: 11961447](https://pubmed.ncbi.nlm.nih.gov/11961447/)) reinforces this unified view.

**Suggested identifiers:** MONDO:8000001; ICD-10 **M46.4** (discitis, unspecified) + **B95.6** (*S. aureus* as cause of disease); ICD-11 **FA84** (spondylopathies / infection of intervertebral disc); MeSH **Discitis (D021782)**, **Staphylococcal Infections (D013203)**; primary anatomy **UBERON:0002103** (intervertebral disc).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Bacterial seeding of the disc/endplate.** *S. aureus* reaches the vertebral endplate via **(a) hematogenous seeding** through end-arteriolar vascular arcades (the dominant route in adults and children), **(b) direct inoculation** from spinal surgery/instrumentation, or **(c) contiguous spread** from adjacent infection — *leads to* colonization of the richly vascularized subchondral endplate. *(Well demonstrated across human cohorts and rabbit models — Findings 1, 9.)*
2. **Adherence and receptor engagement.** Bacterial surface protein A (SpA) **binds osteoblast TNFR-1** — *results in* activation of intracellular stress signaling. *(In vitro demonstrated — Finding 6.)*
3. **Signal transduction.** TNFR-1 engagement **activates the JNK pathway and upregulates TLR2** — *leads to* secretion of TNF-α and IL-6 and osteoblast apoptosis. *(In vitro demonstrated — Finding 6.)*
4. **Osteoclast activation.** The same signaling **increases RANKL** on osteoblasts/stromal cells — *results in* RANK-mediated osteoclast differentiation and activation. *(In vitro demonstrated; TNFR1 knockdown reduces RANKL — Finding 6.)*
5. **Bone and disc destruction.** Osteoclast-mediated resorption plus direct bacterial/inflammatory injury **erode the endplate and cartilage**, and the avascular nucleus pulposus (poor antibiotic penetration) becomes a nidus — *leads to* disc-space narrowing, endplate erosion, and hyperostosis. *(Inferred from combined human histology and rabbit models — Findings 9, 6.)*
6. **Local spread / complications.** Infection **extends contiguously** into paravertebral muscle, psoas, and the epidural space — *results in* abscess formation, and where the epidural abscess or vertebral collapse compresses neural elements, *leads to* radiculopathy, cord compression, and paraplegia. *(Human cohorts — Findings 8, 12.)*
7. **Clinical manifestation.** The net result is **back pain, fever, elevated CRP/ESR**, and — in advanced cases — neurologic deficit and spinal instability. *(Human cohorts — Findings 2, 8.)*

```
 S. aureus ──(hematogenous / direct / contiguous)──▶ vertebral endplate
      │
      ▼  SpA binds TNFR-1 (osteoblast)
   JNK↑ / TLR2↑ ──▶ TNF-α, IL-6 ↑ ; osteoblast apoptosis ↑
      │
      ▼  RANKL ↑
   osteoclast differentiation/activation
      │
      ▼
 endplate/disc destruction ──▶ contiguous spread ──▶ epidural/paravertebral abscess
      │                                                     │
      ▼                                                     ▼
 disc-space narrowing, instability                 cord/root compression
      └──────────────┬──────────────────────────────────────┘
                     ▼
        back pain • fever • ↑CRP/ESR • neuro deficit
```

**Upstream vs downstream:** The bacterial receptor engagement (steps 2–3) is upstream; RANKL-driven resorption and abscess/neurologic complications (steps 4–6) are downstream effectors. **Cell types involved:** osteoblasts (CL:0000062), osteoclasts (CL:0000092), neutrophils/macrophages (inflammatory infiltrate), and nucleus pulposus cells. **Biological processes:** inflammatory response (GO:0006954), osteoclast differentiation (GO:0030316), toll-like receptor signaling (GO:0002224), JNK cascade (GO:0007254).

---

## Section-by-Section Synthesis

### 1. Disease Information
Staphylococcal discitis is an infectious inflammation of the intervertebral disc and adjacent endplates caused predominantly by *S. aureus*. Synonyms/related terms: infective/pyogenic spondylodiscitis, septic discitis, vertebral osteomyelitis (when bone-predominant), spinal osteomyelitis. Information derives from **aggregated disease-level resources** (cohorts, registries, guidelines), not single-patient EHR. Identifiers: MONDO:8000001; MeSH Discitis D021782; ICD-10 M46.4 + B95.6; ICD-11 FA84. No OMIM/Orphanet entry applies because it is not a Mendelian disorder.

### 2. Etiology
**Primary cause: infectious** — *S. aureus* (MSSA/MRSA) predominates (Finding 1). Routes: hematogenous, direct inoculation, contiguous. **Risk factors:** advanced age, male sex, diabetes mellitus, IV drug use, prior spinal surgery/instrumentation, bacteremia, immunosuppression, smoking (Findings 2, 4). **Genetic risk** is polygenic host susceptibility to invasive *S. aureus* (Finding 10); no causal disease gene. **Protective factors:** avoidance/treatment of bacteremia sources, aseptic surgical technique, treatment of asymptomatic bacteriuria before urologic instrumentation ([PMID: 42249268](https://pubmed.ncbi.nlm.nih.gov/42249268/)); the hepcidin-raising CHCHD7/SDR16C5 allele is genetically protective against *S. aureus* bacteremia (Finding 10).

### 3. Phenotypes
| Phenotype | Type | Frequency | HPO |
|---|---|---|---|
| Back pain | Symptom | ~79% | HP:0003418 (back pain) |
| Fever | Sign | ~72% | HP:0001945 |
| Elevated CRP/ESR | Lab | very common | HP:0011227 (elevated CRP) |
| Radiculopathy / radicular nerve damage | Sign | ~51% | HP:0500152 (radicular pain) |
| Epidural/paravertebral abscess | Manifestation | ~45% | HP:0012062 (epidural abscess) |
| Neurologic deficit / paraplegia | Sign | variable | HP:0002385 (paraplegia) |

Onset is adult (geriatric peak) or toddler; severity variable; progression subacute/insidious. QoL impact: substantial pain, disability, prolonged hospitalization, residual disability 20–30%.

### 4. Genetic/Molecular Information
**Not applicable as a heritable disorder.** No causal genes, pathogenic germline variants, ACMG classifications, allele frequencies, modifier genes, or chromosomal abnormalities. Host susceptibility is polygenic (Finding 10). Relevant *bacterial* molecular determinants: protein A (*spa*), *sae* regulon (master regulator SaeS, [PMID: 41172037](https://pubmed.ncbi.nlm.nih.gov/41172037/)), Panton-Valentine leukocidin, biofilm genes.

### 5. Environmental Information
Infectious agent: **Staphylococcus aureus** (NCBI:txid1280); pediatric co-agent **Kingella kingae** (NCBI:txid504). Lifestyle: IV drug use and smoking increase MRSA risk (Finding 4). Iatrogenic exposures: spinal surgery, epidural procedures, urologic instrumentation.

### 6. Mechanism / Pathophysiology
See the ordered causal chain above (protein A → TNFR-1 → JNK/TLR2 → RANKL → osteoclastic destruction → contiguous spread).

### 7. Anatomical Structures Affected
**Primary:** intervertebral disc (UBERON:0002103) and vertebral endplate/body; lumbar > thoracic > cervical. **Secondary:** epidural space, paravertebral/psoas muscle, spinal cord/nerve roots; occasionally heart valves (endocarditis, 14%). Body systems: musculoskeletal, nervous (secondary). Cells: osteoblasts, osteoclasts, nucleus pulposus cells, inflammatory infiltrate. Lateralization: typically central/bilateral at the disc, abscesses may be asymmetric.

### 8. Temporal Development
Onset subacute-to-chronic and insidious; symptoms often present for weeks before diagnosis (pediatric mean delay 42 days). Course: progressive if untreated; treatment-induced remission is the norm. Critical window: early diagnosis (MRI accuracy improves after 2 weeks) and timely surgery (≤14 days) improve outcomes (Findings 7, 12).

### 9. Inheritance and Population
Incidence ~3/100,000/yr; elderly, male-predominant, with a toddler subgroup (Findings 2, 3). **No inheritance pattern** — acquired infection. Geographic variation reflects MRSA prevalence and IVDU epidemiology.

### 10. Diagnostics
Contrast MRI (gold standard) + 18F-FDG PET/CT (adjunct) + blood culture/image-guided biopsy (Finding 7). Labs: elevated CRP/ESR, WBC; positive blood cultures. Open sampling improves yield over percutaneous ([PMID: 41519476](https://pubmed.ncbi.nlm.nih.gov/41519476/)). No genetic testing indicated. Differential: tuberculous spondylodiscitis, Brucella, fungal, degenerative Modic changes, malignancy.

### 11. Outcome/Prognosis
Mortality 3–12%; relapse 6–17%; residual disability 20–30%; 1-yr OS 76% in surgical staphylococcal cohorts (Finding 8). Prognostic factors: age, sepsis severity, prior spinal surgery, timely surgery, concurrent infection.

### 12. Treatment
Pathogen-directed antibiotics (6 weeks non-inferior to 12; Finding 5), with anti-staphylococcal β-lactams for MSSA and vancomycin/daptomycin/linezolid for MRSA; rifampicin for biofilm/implant disease. Surgery for defined indications (Finding 12). Salvage: dalbavancin, bacteriophage therapy (Finding 11). **NCIT suggestions:** NCIT:C254 (Antibiotic), NCIT:C1338 (Vancomycin), NCIT:C61735 (Linezolid), NCIT:C15329 (Surgery), NCIT:C157866 (Daptomycin).

### 13. Prevention
Primary: aseptic surgical technique, treat bacteremia sources, screen/treat asymptomatic bacteriuria before urologic procedures, harm-reduction for IVDU. Secondary: early imaging/culture in at-risk patients with back pain and fever. Tertiary: adequate antibiotic duration and timely surgery to prevent relapse/neurologic sequelae. No vaccine exists for *S. aureus*.

### 14. Other Species / Natural Disease
Staphylococcal discitis/spondylitis occurs naturally in veterinary species (e.g., pigs, poultry, dogs). Experimental disease is best characterized in the **rabbit** (*Oryctolagus cuniculus*, NCBI:txid9986; Finding 9). Zoonotic potential exists via livestock-associated MRSA. Orthologous host genes (e.g., TNFRSF1A, TLR2, TNFSF11/RANKL) are conserved across mammals.

### 15. Model Organisms
The **New Zealand White rabbit** percutaneous-inoculation model is the established in vivo system (Finding 9), reproducing disc-space narrowing, endplate erosion, epidural abscess, and paraplegia, and validated by MRI. Limitations: does not model chronic hematogenous seeding or the aged/comorbid human host. Applications: pathogenesis, antibiotic penetration, imaging validation, adjunct therapies (e.g., intradiscal vancomycin + diode laser, [PMID: 22554049](https://pubmed.ncbi.nlm.nih.gov/22554049/)).

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [41023355](https://pubmed.ncbi.nlm.nih.gov/41023355/) | *Infectious spondylodiscitis: 14-year retrospective* | Core epidemiology, microbiology, complications (F1, F2, F8) |
| [39716636](https://pubmed.ncbi.nlm.nih.gov/39716636/) | *Seasonal trends, Japan nationwide (n=71,134)* | Large-scale demographics, MRSA share (F1, F2, F8) |
| [34091001](https://pubmed.ncbi.nlm.nih.gov/34091001/) | *Clinical characteristics of PVO* | *S. aureus* share, relapse/mortality, ITR predictors (F1, F4, F8) |
| [40653018](https://pubmed.ncbi.nlm.nih.gov/40653018/) | *MRSA spinal infection outcomes* | MRSA-specific risk factors (F4) |
| [25468170](https://pubmed.ncbi.nlm.nih.gov/25468170/) | *6 vs 12 weeks antibiotics RCT* | Landmark duration trial (F5) |
| [26846887](https://pubmed.ncbi.nlm.nih.gov/26846887/) | *TNFR1/TLR2 in S. aureus infection* | Core mechanism (F6) |
| [25186431](https://pubmed.ncbi.nlm.nih.gov/25186431/) | *PET/CT vs MRI prospective* | Diagnostic accuracy (F7) |
| [42232200](https://pubmed.ncbi.nlm.nih.gov/42232200/) | *18F-FDG PET/CT in spinal infection* | Combined-modality sensitivity (F7) |
| [27317050](https://pubmed.ncbi.nlm.nih.gov/27317050/) | *MRI vs imaging value* | MRI timing dependence (F7) |
| [11961447](https://pubmed.ncbi.nlm.nih.gov/11961447/) | *Nontuberculous spondylodiscitis in children* | Pediatric microbiology, nosology (F3, F13) |
| [18485785](https://pubmed.ncbi.nlm.nih.gov/18485785/) | *Rabbit disc-space infection model* | Animal model (F9) |
| [24043368](https://pubmed.ncbi.nlm.nih.gov/24043368/) | *Antibiotic penetration in rabbit discitis* | Model application (F9) |
| [26925420](https://pubmed.ncbi.nlm.nih.gov/26925420/) | *P. acnes vs S. aureus rabbit study* | Model comparative pathology (F9) |
| [41946712](https://pubmed.ncbi.nlm.nih.gov/41946712/) | *African GWAS iron loci* | Polygenic host susceptibility (F10) |
| [41478341](https://pubmed.ncbi.nlm.nih.gov/41478341/) | *Systemic phage therapy MRSA spondylodiscitis* | Salvage therapy (F11) |
| [41305347](https://pubmed.ncbi.nlm.nih.gov/41305347/) | *Dalbavancin for bone/joint infection* | Simplified therapy (F11) |
| [40762806](https://pubmed.ncbi.nlm.nih.gov/40762806/) | *Predictors of surgery* | Surgical indications (F12) |
| [42314843](https://pubmed.ncbi.nlm.nih.gov/42314843/) | *Timely surgery in Staphylococcus spondylodiscitis* | Surgical timing, survival (F8, F12) |
| [40204566](https://pubmed.ncbi.nlm.nih.gov/40204566/) | *Pyogenic Vertebral Osteomyelitis review* | Nosology, definition (F13) |
| [26229122](https://pubmed.ncbi.nlm.nih.gov/26229122/) / [26316526](https://pubmed.ncbi.nlm.nih.gov/26316526/) | *IDSA 2015 NVO guidelines* | Treatment framework (F12) |
| [39852953](https://pubmed.ncbi.nlm.nih.gov/39852953/) | *AO Spine recommendations* | Evidence synthesis, early-surgery recommendation |
| [42262500](https://pubmed.ncbi.nlm.nih.gov/42262500/) | *Culture-negative meta-analysis* | Recurrence/disability estimates (F8) |
| [37148755](https://pubmed.ncbi.nlm.nih.gov/37148755/) | *Concurrent infection cohort (n=10,695)* | Mortality with concurrent infection |

**Evidence source types:** Human clinical cohorts/RCT/guidelines (F1–F5, F7, F8, F11–F13); in vitro molecular biology (F6); model organism/rabbit (F9); GWAS/computational (F10).

---

## Limitations and Knowledge Gaps

1. **Template mismatch.** Roughly a third of the requested template (causal genes, pathogenic variants, inheritance, penetrance, expressivity, anticipation, founder effects, carrier frequency) is **not applicable** — staphylococcal discitis is an acquired infection, not a Mendelian disease. Host genetic contribution is polygenic and non-specific.
2. **Mechanism evidence is largely in vitro.** The protein A → TNFR-1 → JNK/TLR2 → RANKL cascade (F6) derives from cell-culture experiments; its quantitative contribution to human disc destruction in vivo is inferred, not directly demonstrated in patients.
3. **Discitis-specific vs spectrum-level data.** Much evidence pools discitis with vertebral osteomyelitis and epidural abscess; few studies isolate disc-only staphylococcal disease, so some frequencies (e.g., complication rates) are spectrum-level.
4. **Heterogeneous cohorts.** Retrospective designs, varying MRSA prevalence, and differing culture practices (culture-negative ~43% of cases) introduce confounding into epidemiologic and prognostic estimates.
5. **Sparse pediatric mechanistic data.** The toddler subgroup is described clinically but not mechanistically.
6. **Emerging therapies lack RCTs.** Dalbavancin and phage evidence is observational/case-based (F11), not randomized.

---

## Proposed Follow-up Experiments / Actions

1. **In vivo validation of the RANKL axis.** Test RANKL/OPG modulation (e.g., anti-RANKL, JNK inhibitors) in the rabbit *S. aureus* discitis model to quantify effect on endplate destruction — bridging the in vitro→in vivo gap in F6.
2. **Discitis-specific registry analysis.** Extract disc-predominant (vs bone-predominant) cases from national databases to derive discitis-specific incidence, complication, and relapse rates.
3. **Host-susceptibility GWAS in spondylodiscitis.** Extend iron-regulation/immune-pathway host genetics (F10) to a spondylodiscitis-specific cohort to identify susceptibility loci beyond bacteremia.
4. **Prospective trial of shortened/oral therapy in staphylococcal subset.** Confirm the 6-week non-inferiority finding (F5) specifically in *S. aureus* discitis, including early oral switch.
5. **Controlled evaluation of salvage therapeutics.** Prospective cohorts/registries for dalbavancin and bacteriophage therapy in refractory MRSA spinal infection (F11).
6. **Biomarker-guided surgical timing.** Prospectively validate predictors (epidural/psoas abscess, Gram-positive cocci, thoracic level) and the ≤14-day surgical window (F12) to build a decision algorithm.

---

## Consensus Answer

Staphylococcus discitis is an acquired bacterial infection of the intervertebral disc and adjacent vertebral endplates — part of the spondylodiscitis/vertebral-osteomyelitis spectrum — caused predominantly by *Staphylococcus aureus* (MSSA/MRSA) reaching the spine hematogenously, by direct inoculation, or by contiguous spread; it chiefly affects older adults (with a toddler subgroup), presents with back pain, fever, and elevated CRP/ESR, and is diagnosed by contrast MRI plus blood/biopsy culture. Bone destruction is driven by *S. aureus*–induced osteoblast/immune signaling (protein A–TNFR-1 → JNK/TLR2 → RANKL) and osteoclastic resorption, and it is treated with roughly six weeks of pathogen-directed antibiotics (6 weeks non-inferior to 12 in an RCT), reserving surgery for neurologic deficit, instability, abscess, or medical failure; mortality is ~3–12%, relapse ~6–17%, and residual disability ~20–30%. It is not a genetic/heritable disorder — there are no causal host genes, only polygenic susceptibility to invasive *S. aureus* — so OMIM/Orphanet, inheritance, and germline-variant categories are not applicable.


## Artifacts

- [OpenScientist final report](Staphylococcus_Discitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Staphylococcus_Discitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 29 |
| On topic | 19 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 17 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0002103` (3 mentions) - the report calls it "intervertebral disc"; UBERON calls it **hindlimb**
- `HP:0500152` (1 mention) - the report calls it "radicular pain"; HP calls it **Hypocystinemia**
- `HP:0012062` (1 mention) - the report calls it "epidural abscess"; HP calls it **Bone cyst**
- `NCIT:C1338` (1 mention) - the report calls it "Vancomycin"; NCIT calls it **Didox**
- `NCIT:C61735` (1 mention) - the report calls it "Linezolid"; NCIT calls it **Dolasetron**
- `NCIT:C157866` (1 mention) - the report calls it "Daptomycin"; NCIT calls it **Gluten Free Diet**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0045672` (1 mention) - the report calls it "regulation of osteoclast differentiation"; GO calls it **positive regulation of osteoclast differentiation**, and lists "upregulation of osteoclast differentiation" among its other names
- `HP:0011227` (1 mention) - the report calls it "elevated CRP"; HP calls it **Elevated circulating C-reactive protein concentration**, and lists "Elevated CRP" among its other names
- `HP:0002385` (1 mention) - the report calls it "paraplegia"; HP calls it **Paraparesis**
- `NCIT:C254` (1 mention) - the report calls it "Antibiotic"; NCIT calls it **Anti-Infective Agent**, and lists "AntiInfectives" among its other names