---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-20T19:37:18.940173'
end_time: '2026-10-20T20:01:30.174795'
duration_seconds: 1451.23
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Severe Congenital Neutropenia 9
  mondo_id: MONDO:0030726
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
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 18
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 18
  quotes_valid: 18
  relevance_assessed: 18
  on_topic: 13
  validator_version: 0.3.0
term_validation:
  total_terms: 33
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 10
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: NCIT:C15847
    reported_labels:
    - antibiotics
    ontology_label: Non-Ionizing Radiotherapy
  labels_variant: 2
  unresolvable_prefixes:
  - OMIM
  - UMLS
  - GARD
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Severe_Congenital_Neutropenia_9-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Severe_Congenital_Neutropenia_9-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Severe Congenital Neutropenia 9
- **MONDO ID:** MONDO:0030726 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Severe Congenital Neutropenia 9** covering all of the
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

# Severe Congenital Neutropenia 9 (SCN9): A Comprehensive Disease Characterization

**Disease:** Severe Congenital Neutropenia 9 (SCN9)
**MONDO ID:** MONDO:0030726 · **OMIM:** 619813 · **Gene:** *CLPB* (SKD3; HGNC:30664)
**Category:** Mendelian (autosomal dominant)

---

## Summary

**Severe Congenital Neutropenia 9 (SCN9)** is a rare, autosomal-dominant inborn error of granulopoiesis caused by **heterozygous, dominant-negative missense variants in *CLPB*** (also called SKD3), a gene on chromosome 11q13.4 encoding a mitochondrial intermembrane-space (IMS) AAA+ ATPase that functions as a protein **disaggregase/refoldase**. The disease was formally delineated in 2021–2022 when two groups independently showed that monoallelic *CLPB* variants, clustering near the ATP-binding pocket, poison the wild-type CLPB oligomer and impair its disaggregase activity — a true dominant-negative mechanism rather than haploinsufficiency ([PMID: 34115842](https://pubmed.ncbi.nlm.nih.gov/34115842/); [PMID: 34140661](https://pubmed.ncbi.nlm.nih.gov/34140661/)). This molecular lesion blocks granulocytic differentiation of hematopoietic progenitors and increases apoptosis of neutrophil precursors, producing a fully penetrant myeloid maturation arrest and severe neutropenia with recurrent bacterial infections beginning in infancy.

A central theme of this disease is its **zygosity-dependent severity spectrum**. The same gene, *CLPB*, causes two distinct Mendelian disorders: the **monoallelic (dominant) form** described here — SCN9 — which is typically **isolated severe neutropenia**; and a **biallelic (recessive) form** (OMIM 616271; 3-methylglutaconic aciduria type VII) that combines neutropenia with 3-methylglutaconic aciduria (3-MGA), cataracts, progressive brain atrophy, intellectual disability, movement disorder, epilepsy, and high early-childhood mortality. Critically, the metabolic hallmark 3-MGA-uria is characteristically **absent** in SCN9 (0/5 tested cases), and the monoallelic form carries a substantially better prognosis (4-year survival ~82% vs ~50% for biallelic disease).

Management parallels other severe congenital neutropenias: **granulocyte colony-stimulating factor (G-CSF)** maintains protective neutrophil counts and reduces infections, while **allogeneic hematopoietic stem cell transplantation (HSCT)** remains the only curative option, reserved for G-CSF non-response or malignant (MDS/AML) transformation. Mechanistic work in cellular models points to **ROS-driven apoptosis** at the onset of differentiation, with experimental rescue by antioxidants (N-acetylcysteine), free fatty acids, or citrate — candidate future metabolic therapies. This report synthesizes 10 confirmed findings across 34 reviewed papers into a full, section-by-section disease knowledge base entry.

---

## Key Findings

### Finding 1 — SCN9 is caused by heterozygous dominant-negative *CLPB* variants (autosomal dominant)

SCN9 maps to **MONDO:0030726** ("Neutropenia, severe congenital, 9, autosomal dominant"), cross-referenced to **OMIM:619813**, **UMLS:C5676954**, and **GARD:0025625**, with material basis in germline mutation in ***CLPB*** (HGNC:30664). The defining study, Warren et al. 2022 (*Blood*), used exome sequencing of 104 persons with congenital neutropenia to identify heterozygous missense *CLPB* variants in 5 severe congenital neutropenia cases, with 5 additional cases identified through supplementary sequencing — 10 total. The variants are not scattered but **cluster near the adenosine-triphosphate–binding pocket** of CLPB.

> "Exome sequencing of 104 persons with congenital neutropenia identified heterozygous missense variants of CLPB (caseinolytic peptidase B) in 5 severe congenital neutropenia cases, with 5 more cases identified through additional sequencing efforts or clinical sequencing." — [PMID: 34115842](https://pubmed.ncbi.nlm.nih.gov/34115842/)

> "the CLPB variants are distinct, consisting of heterozygous variants that cluster near the adenosine triphosphate-binding pocket" — [PMID: 34115842](https://pubmed.ncbi.nlm.nih.gov/34115842/)

This dominant form is molecularly and clinically distinct from the biallelic *CLPB* disease (OMIM 616271, 3-MGA-uria type VII, autosomal recessive).

### Finding 2 — Mechanism: dominant-negative CLPB impairs mitochondrial disaggregase activity, blocking granulopoiesis and increasing apoptosis

CLPB (SKD3) is an **AAA+ ATPase disaggregase/refoldase** residing in the **mitochondrial intermembrane space (IMS)**. SCN9 variants physically **associate with wild-type CLPB and inhibit both its ATPase and disaggregase activities in a dominant-negative fashion**. Both genetic loss of CLPB and expression of the variant protein impair granulocytic differentiation of human hematopoietic progenitors and increase apoptosis.

> "These CLPB variants associate with wild-type CLPB and inhibit its adenosine triphosphatase and disaggregase activity in a dominant-negative fashion." — [PMID: 34115842](https://pubmed.ncbi.nlm.nih.gov/34115842/)

> "Both genetic loss of CLPB and expression of CLPB variants result in impaired granulocytic differentiation of human hematopoietic progenitor cells and increased apoptosis." — [PMID: 34115842](https://pubmed.ncbi.nlm.nih.gov/34115842/)

A key mechanistic link is to **HAX1**, the protein mutated in SCN3 (Kostmann disease). CLPB maintains the solubility of HAX1, and HAX1 in turn acts as a direct stimulatory cofactor that oligomerizes and activates CLPB — tying two distinct neutropenia genes into one IMS proteostasis axis.

> "loss of function in either gene causes severe congenital neutropenia as well as neuropathology and causes many proteins in the IMS and its bounding membranes to become insoluble" — [PMID: 42244541](https://pubmed.ncbi.nlm.nih.gov/42244541/)

In CLPB-deficient myeloblasts, the downstream picture is reduced mitochondrial membrane potential, insoluble HAX1 aggregates, and ROS-driven apoptosis precisely at the onset of G-CSF-induced differentiation ([PMID: 39644357](https://pubmed.ncbi.nlm.nih.gov/39644357/)). Monoallelic variants disturb refoldase activity (and to a lesser extent ATPase activity) dominant-negatively ([PMID: 34140661](https://pubmed.ncbi.nlm.nih.gov/34140661/)).

### Finding 3 — SCN9 phenotype is typically isolated severe neutropenia, lacking the neuro/metabolic features of biallelic disease

In Warren et al. 2022, heterozygous *CLPB* carriers had severe congenital neutropenia but — unlike biallelic disease — **3-methylglutaconic aciduria was not observed**, and syndromic features (cataracts, neurological disease) were uncommon.

> "3-methylglutaconic aciduria was not observed and, other than neutropenia, these clinical features were uncommon in our series" — [PMID: 34115842](https://pubmed.ncbi.nlm.nih.gov/34115842/)

By contrast, the biallelic recessive syndrome (OMIM 616271) spans a neurological phenotype from nonprogressive intellectual disability to prenatal encephalopathy:

> "a neurological phenotype ranging from nonprogressive intellectual disability to a prenatal encephalopathy with progressive brain atrophy, movement disorder, cataracts, and early death" — [PMID: 25597510](https://pubmed.ncbi.nlm.nih.gov/25597510/)

A subset of monoallelic (de novo) cases do show some neurodevelopmental involvement (seizures, developmental delay), indicating a phenotypic spectrum rather than a clean dichotomy ([PMID: 34140661](https://pubmed.ncbi.nlm.nih.gov/34140661/)).

### Finding 4 — Zygosity predicts outcome: monoallelic disease is milder with better survival

Heath et al. 2026 assembled a cohort of **63 individuals (41 biallelic, 22 monoallelic)** and quantified the zygosity-outcome relationship.

> "Death occurred in 66% of biallelic and 23% of monoallelic individuals, with earlier median age at death in biallelic cases (6 months vs 2.4 years). Biallelic cases had significantly higher DBI scores and poorer survival (4-year survival: 50% vs 82%)." — [PMID: 41719910](https://pubmed.ncbi.nlm.nih.gov/41719910/)

Notably, **structural predictions** (nonsense-mediated decay or ankyrin-repeat-domain disruption) were stronger predictors of survival than zygosity or age of onset alone, and stop/stop genotypes conferred greater disease burden than missense combinations. Early onset (<12 months) correlated with more severe progression.

### Finding 5 — Treatment: G-CSF maintains counts and reduces infections; HSCT is definitive; antioxidant/metabolic rescue is experimental

In a CLPB-neutropenia case report, intermittent G-CSF successfully maintained protective neutrophil counts and cut respiratory infections:

> "Administration of granulocyte colony-stimulating factor successfully maintained neutrophil counts above 0.5 × 109/L and significantly reduced the frequency of respiratory tract infections." — [PMID: 41560087](https://pubmed.ncbi.nlm.nih.gov/41560087/)

Across congenital neutropenia syndromes, G-CSF responders retain residual risk of bone marrow failure, MDS, and AML ([PMID: 38589208](https://pubmed.ncbi.nlm.nih.gov/38589208/)); HSCT is the only curative option for transformation or G-CSF non-response ([PMID: 15640815](https://pubmed.ncbi.nlm.nih.gov/15640815/); [PMID: 15489867](https://pubmed.ncbi.nlm.nih.gov/15489867/)). Mechanistic rescue experiments identify candidate metabolic strategies:

> "N-acetylcysteine, exogenous free fatty acids, or exogenous citrate protected CLPB-deficient 32Dcl3 cells from apoptosis at the onset of differentiation" — [PMID: 39644357](https://pubmed.ncbi.nlm.nih.gov/39644357/)

### Finding 6 — Model systems: zebrafish morphant, CLPB-KO 32Dcl3 myeloblasts, cross-species orthology

The zebrafish *clpb* morphant recapitulates the CNS phenotype of the recessive syndrome, with rescue specificity establishing variant pathogenicity:

> "Suppression of clpb in zebrafish embryos induced a central nervous system phenotype that was consistent with cerebellar and cerebral atrophy that could be rescued by wild-type, but not mutant, human CLPB mRNA" — [PMID: 25597510](https://pubmed.ncbi.nlm.nih.gov/25597510/)

The most neutropenia-relevant model is the **CRISPR CLPB-knockout of the IL-3-dependent mouse 32D clone 3 (32Dcl3) myeloblastic line**, which reproduces the differentiation/apoptosis defect:

> "we used 32D clone 3 (32Dcl3) cells, an interleukin-3 (IL-3)-dependent mouse myeloblastic cell line model, to investigate the effects of CLPB knockout on myeloblast-to-neutrophil differentiation" — [PMID: 39644357](https://pubmed.ncbi.nlm.nih.gov/39644357/)

### Finding 7 — Inheritance & population genetics: AD via de novo dominant-negative missense; CLPB is LoF-tolerant

SCN9 arises through de novo monoallelic missense variants acting dominant-negatively:

> "we identified one of four different de novo monoallelic missense variants in CLPB. We show that these variants disturb refoldase and to a lesser extent ATPase activity of CLPB in a dominant-negative manner" — [PMID: 34140661](https://pubmed.ncbi.nlm.nih.gov/34140661/)

Critically, **gnomAD constraint metrics exclude haploinsufficiency**: pLI ≈ 2.4×10⁻⁵, observed/expected LoF = 40/78.4 (oe_lof 0.51, LOEUF 0.66), missense Z = 1.53 — i.e., heterozygous loss-of-function is tolerated. This confirms that disease requires a *poison* (dominant-negative) allele, not simple gene-dosage reduction. The biallelic form shows a Greenlandic founder cohort:

> "Four of the individuals were of Greenlandic descent, and one was North American" — [PMID: 25597511](https://pubmed.ncbi.nlm.nih.gov/25597511/)

### Finding 8 — Diagnostics & anatomy: severe neonatal neutropenia with marrow maturation arrest; diagnosis by NGS/WES

Severe congenital neutropenia is defined hematologically by myeloid maturation arrest:

> "characterized by a maturation arrest of myelopoiesis at the promyelocyte/myelocyte stage of development. This arrest results in severe neutropenia with absolute neutrophil counts (ANC) less than 0.2 x 10(9)/l associated with severe systemic bacterial infections from early infancy" — [PMID: 10994541](https://pubmed.ncbi.nlm.nih.gov/10994541/)

Molecular diagnosis of CLPB-SCN relies on NGS gene panels / whole-exome or whole-genome sequencing; *CLPB* is now routinely included on congenital neutropenia panels ([PMID: 40510848](https://pubmed.ncbi.nlm.nih.gov/40510848/); [PMID: 41383606](https://pubmed.ncbi.nlm.nih.gov/41383606/)), and reanalysis of previously negative exomes can reveal *CLPB* ([PMID: 41560087](https://pubmed.ncbi.nlm.nih.gov/41560087/)).

### Finding 9 — Downstream consequences & complications: IMS proteostasis collapse, infection susceptibility, MDS/AML risk

CLPB loss triggers stress-specific IMS protein aggregation that cripples mitochondrial quality control:

> "CLPB deficiency impeding SPY complex function by virtue of protein aggregation in the intermembrane space" — [PMID: 38270563](https://pubmed.ncbi.nlm.nih.gov/38270563/)

Clinically, the neutropenia drives recurrent severe bacterial infections, and like other SCN subtypes carries malignant transformation risk:

> "neutropenia that can develop into leukemia" — [PMID: 25597510](https://pubmed.ncbi.nlm.nih.gov/25597510/)

### Finding 10 — Official HPO phenotype frequencies for SCN9

The HPO disease annotation for OMIM:619813 (source PMID 34115842, n≈10) formalizes the phenotype frequencies, with the 0/5 for 3-MGA-uria confirming the metabolic hallmark of biallelic disease is absent in SCN9.

> "3-methylglutaconic aciduria was not observed and, other than neutropenia, these clinical features were uncommon in our series" — [PMID: 34115842](https://pubmed.ncbi.nlm.nih.gov/34115842/)

| HPO term | ID | Frequency in SCN9 |
|---|---|---|
| Myeloid maturation arrest | HP:0410253 | 10/10 (100%) |
| Infantile onset | HP:0003593 | 5/10 |
| Childhood onset | HP:0011463 | 4/10 |
| Congenital onset | HP:0003577 | 1/10 |
| Cataract | HP:0000518 | 2/10 (20%) |
| Splenomegaly | HP:0001744 | 2/10 |
| Seizure | HP:0001250 | 2/10 |
| Global developmental delay | HP:0001263 | 1/10 |
| 3-Methylglutaconic aciduria | HP:0003535 | 0/5 (0%) |
| Autosomal dominant inheritance | HP:0000006 | — |

---

## Full Section-by-Section Report

### 1. Disease Information

SCN9 is a rare Mendelian disorder of granulopoiesis producing severe, persistent neutropenia from early infancy, caused by heterozygous dominant-negative variants in *CLPB*. Key identifiers: **MONDO:0030726**, **OMIM:619813**, **UMLS:C5676954**, **GARD:0025625**. It falls under the broader ICD-10 category D70 (neutropenia) / ICD-11 4B00.0 (congenital neutropenia); MeSH maps to "Congenital Bone Marrow Failure Syndromes" / "Neutropenia." **Synonyms/alternative names:** Severe congenital neutropenia type 9; autosomal dominant *CLPB*-related neutropenia; CLPB-associated congenital neutropenia (monoallelic form). The information is derived primarily from aggregated disease-level resources (OMIM, Orphanet, HPO) and from small published case series/cohorts (Warren 2022, Wortmann 2021, Heath 2026) rather than from EHR.

### 2. Etiology

**Primary cause — genetic:** heterozygous (monoallelic) missense variants in *CLPB*/SKD3 that cluster near the ATP-binding pocket and act in a dominant-negative manner ([PMID: 34115842](https://pubmed.ncbi.nlm.nih.gov/34115842/); [PMID: 34140661](https://pubmed.ncbi.nlm.nih.gov/34140661/)). Many arise **de novo**. **Genetic risk factors:** the causal variant is the sole established risk factor; no susceptibility loci or modifier genes are established for the dominant form, though structural impact (NMD vs ankyrin-domain disruption) modifies severity in the broader CLPB spectrum ([PMID: 41719910](https://pubmed.ncbi.nlm.nih.gov/41719910/)). **Environmental risk/protective factors:** none identified — this is a monogenic disorder. **Gene–environment interactions:** none established; infection exposure determines clinical severity of complications but does not cause the disease.

### 3. Phenotypes

The core phenotype is a **laboratory/hematologic abnormality** — severe neutropenia (ANC often <0.2–0.5×10⁹/L) with bone-marrow myeloid maturation arrest (HP:0410253, 100%) — manifesting clinically as **recurrent severe bacterial infections** (HP:0002718) from early infancy. Onset is congenital/infantile (HP:0003593/HP:0003577). Severity is severe; course is chronic and lifelong but stabilizable with G-CSF. Non-hematologic features (cataract HP:0000518 20%; splenomegaly HP:0001744; seizure HP:0001250) occur at low frequency; 3-MGA-uria (HP:0003535) is characteristically absent (0/5). **Quality-of-life impact:** chronic infection susceptibility, repeated hospitalization, need for lifelong G-CSF injections and infection prophylaxis; well-managed patients can achieve good functional status, but transformation to MDS/AML is a severe QoL and survival threat.

### 4. Genetic / Molecular Information

**Causal gene:** *CLPB* (SKD3), HGNC:30664, OMIM gene 616254, Entrez 81570, Ensembl ENSG00000162129, UniProt Q9H078, locus **11q13.4** (GRCh38 chr11:72,285,495–72,434,680). **Pathogenic variants:** heterozygous **missense** variants near the ATP-binding pocket (dominant SCN9); biallelic missense/frameshift/nonsense (recessive 3-MGA-uria VII). Example recessive variants: c.1016delT (p.L339Rfs*5), c.1087A>G (p.R363G) ([PMID: 37906145](https://pubmed.ncbi.nlm.nih.gov/37906145/)); p.Arg408Gly abolishes ATPase function ([PMID: 25597510](https://pubmed.ncbi.nlm.nih.gov/25597510/)). **Classification:** pathogenic/likely pathogenic per ACMG. **Allele frequency:** ultra-rare; gnomAD shows CLPB is LoF-tolerant (oe_lof 0.51, LOEUF 0.66), excluding haploinsufficiency. **Origin:** germline. **Functional consequence:** dominant-negative (SCN9) vs loss-of-function (recessive disease). **Modifier genes:** none validated; structural class of the variant is the main severity modifier. **Epigenetic/chromosomal abnormalities:** none described.

### 5. Environmental Information

Not applicable as a cause — SCN9 is monogenic. Environmental **triggers of complications** include bacterial and viral pathogens (recurrent sepsis, respiratory/skin/oral infections; EBV reactivation has been reported in the CLPB/VPS45 neutropenia spectrum). No toxins, lifestyle, or occupational exposures contribute to disease causation.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **heterozygous dominant-negative missense variant in *CLPB*** (near the ATP-binding pocket) **leads to** a mutant CLPB subunit that is translated and imported into the mitochondrial IMS.
2. The mutant subunit **co-assembles with wild-type CLPB** into mixed oligomers and **inhibits** the complex's ATPase and disaggregase/refoldase activity (dominant-negative poisoning) — *demonstrated biochemically* ([PMID: 34115842](https://pubmed.ncbi.nlm.nih.gov/34115842/)).
3. Loss of disaggregase activity **results in** failure to maintain solubility of IMS clients — notably **HAX1 aggregation** — and impairment of the proteolytic **SPY complex (STOML2–PARL–YME1L1)** ([PMID: 42244541](https://pubmed.ncbi.nlm.nih.gov/42244541/); [PMID: 38270563](https://pubmed.ncbi.nlm.nih.gov/38270563/)).
4. IMS proteostasis collapse **leads to** reduced mitochondrial membrane potential and **ROS accumulation** in myeloid precursors ([PMID: 39644357](https://pubmed.ncbi.nlm.nih.gov/39644357/)).
5. ROS/stress **triggers apoptosis specifically at the onset of G-CSF–induced granulocytic differentiation**, i.e., CLPB is a pro-survival factor at this checkpoint ([PMID: 39644357](https://pubmed.ncbi.nlm.nih.gov/39644357/)).
6. Precursor apoptosis **produces** myeloid maturation arrest at the promyelocyte/myelocyte stage → **severe peripheral neutropenia** → **recurrent bacterial infections** from infancy.
7. *Branch (downstream, inferred):* chronic proliferative stress on the marrow **contributes to** clonal evolution and **MDS/AML transformation** risk, as in other SCN subtypes.

**Molecular pathways:** mitochondrial protein quality control / disaggregation; HAX1–CLPB axis; SPY proteolytic complex. **Cellular processes:** apoptosis (GO:0006915), response to ROS (GO:0000302), neutrophil differentiation (GO:0030223), protein refolding/disaggregation (GO:0042026). **Protein dysfunction:** dominant-negative impairment of an AAA+ ATPase disaggregase. **Cell types:** neutrophil (CL:0000775), promyelocyte (CL:0000836), granulocyte-monocyte progenitor (CL:0000557), hematopoietic stem cell (CL:0000037). **Subcellular:** mitochondrial intermembrane space (GO:0005758). CLPB assembles into homo-tetradecamers (apo) / homo-dodecamers (substrate-bound) with an essential N-terminal ankyrin-repeat domain ([PMID: 36745679](https://pubmed.ncbi.nlm.nih.gov/36745679/)).

### 7. Anatomical Structures Affected

**Organ level:** bone marrow (UBERON:0002371) and blood (UBERON:0000178) are primary; spleen (splenomegaly in some) secondary. **Body system:** hematopoietic/immune. **Cell level:** neutrophils and their myeloid precursors (promyelocytes, GMPs, HSCs). **Subcellular:** mitochondria, specifically the intermembrane space (GO:0005758). **Lateralization:** not applicable (systemic hematologic disease). In the biallelic form, additional organs are involved — CNS (UBERON:0000955, brain atrophy), lens/eye (cataract), and ovary (premature ovarian insufficiency, [PMID: 36074910](https://pubmed.ncbi.nlm.nih.gov/36074910/)).

### 8. Temporal Development

**Onset:** congenital/neonatal to infantile; neutropenia detectable from early infancy. **Onset pattern:** chronic from birth. **Progression:** generally stable neutropenia maintainable with G-CSF; risk of progression to marrow failure or MDS/AML over time. Early onset (<12 months) predicts more severe progression across the CLPB spectrum ([PMID: 41719910](https://pubmed.ncbi.nlm.nih.gov/41719910/)). **Course:** chronic, lifelong. **Remission:** treatment-induced count normalization with G-CSF; no spontaneous cure. **Critical period:** the onset of granulocytic differentiation is the vulnerable checkpoint (where CLPB-dependent apoptosis occurs), and infancy is the window of greatest infection risk.

### 9. Inheritance and Population

**Inheritance:** autosomal dominant (SCN9, OMIM 619813), frequently de novo, dominant-negative ([PMID: 34140661](https://pubmed.ncbi.nlm.nih.gov/34140661/)). **Penetrance:** myeloid maturation arrest appears fully penetrant (100%) in reported carriers; expressivity variable for non-hematologic features. **Epidemiology:** ultra-rare — dozens of families worldwide; the largest CLPB cohort assembled only 63 individuals across both zygosity forms ([PMID: 41719910](https://pubmed.ncbi.nlm.nih.gov/41719910/)). **Founder effects:** a Greenlandic founder cohort exists for the biallelic form ([PMID: 25597511](https://pubmed.ncbi.nlm.nih.gov/25597511/)); consanguinity enriches the recessive disease. **Carrier frequency:** not established (dominant form typically de novo). **Sex ratio:** both sexes affected, no strong skew. **Age distribution:** presents in infancy.

### 10. Diagnostics

**Hematology:** CBC showing severe neutropenia (ANC <0.2–0.5×10⁹/L); bone marrow aspirate showing promyelocyte/myelocyte maturation arrest ([PMID: 10994541](https://pubmed.ncbi.nlm.nih.gov/10994541/)). **Genetic testing (definitive):** NGS congenital-neutropenia gene panels, WES, or WGS, now including *CLPB*; reanalysis of prior negative exomes is warranted ([PMID: 40510848](https://pubmed.ncbi.nlm.nih.gov/40510848/); [PMID: 41383606](https://pubmed.ncbi.nlm.nih.gov/41383606/); [PMID: 41560087](https://pubmed.ncbi.nlm.nih.gov/41560087/)). **Supportive discriminators:** urine organic acids (3-MGA — normal in SCN9, elevated in biallelic disease; CHEBI:1890), slit-lamp exam (cataract), neuro-exam/MRI (recessive syndrome). **Differential diagnosis:** other SCN genes — *ELANE* (SCN1), *GFI1* (SCN2), *HAX1* (SCN3/Kostmann), *G6PC3* (SCN4), *VPS45* (SCN5), *CSF3R* (SCN7), *SRP54* (SCN8), *JAGN1*, *WAS* — plus Shwachman-Diamond and cyclic neutropenia. **Screening:** no population newborn screening; cascade family genetic testing applies once a variant is known.

### 11. Outcome / Prognosis

**Survival:** monoallelic (SCN9) ~82% 4-year survival vs ~50% biallelic; death in 23% monoallelic vs 66% biallelic; median age at death 2.4 years (monoallelic) vs 6 months (biallelic) ([PMID: 41719910](https://pubmed.ncbi.nlm.nih.gov/41719910/)). **Morbidity:** recurrent infections, hospitalizations; complications include sepsis, oral/periodontal and respiratory infections, hypersplenism, and MDS/AML transformation. **Recovery potential:** neutropenia is controllable (not curable) with G-CSF; HSCT can cure. **Prognostic factors:** zygosity, variant structural class (NMD/ankyrin-domain disruption > zygosity as predictor), age of onset (<12 months worse), disease burden index.

### 12. Treatment

**Pharmacotherapy:** **G-CSF / filgrastim** (NCIT:C1705-class) is first-line, maintaining ANC >0.5×10⁹/L and reducing infections ([PMID: 41560087](https://pubmed.ncbi.nlm.nih.gov/41560087/)); pathogen-directed **antibiotics** (NCIT:C15847) for infections. **Advanced therapeutics:** **allogeneic HSCT** (NCIT:C15431) is the only curative option, indicated for G-CSF non-response, marrow failure, or MDS/AML ([PMID: 15640815](https://pubmed.ncbi.nlm.nih.gov/15640815/); [PMID: 15489867](https://pubmed.ncbi.nlm.nih.gov/15489867/)). **Experimental/metabolic:** N-acetylcysteine (NCIT:C291), free fatty acids, or citrate rescued CLPB-deficient myeloblasts from apoptosis in vitro ([PMID: 39644357](https://pubmed.ncbi.nlm.nih.gov/39644357/)) — candidate antioxidant/metabolic strategies not yet clinically validated. **Supportive care:** infection prophylaxis, prompt treatment of febrile episodes, dental/periodontal care. **Pharmacogenomics / gene therapy / RNA therapy:** none established.

### 13. Prevention

No primary prevention exists for this monogenic disease. **Secondary prevention:** early genetic diagnosis enabling prompt G-CSF and infection surveillance; routine monitoring for MDS/AML (serial CBC, marrow exams). **Tertiary prevention:** infection prophylaxis, timely HSCT before leukemic progression. **Genetic counseling:** autosomal dominant recurrence risk (often de novo); prenatal/preimplantation testing possible once the familial variant is known. **Immunization/public health/environmental interventions:** not applicable to disease causation (standard vaccination and infection control apply to the immunocompromised patient).

### 14. Other Species / Natural Disease

*CLPB* is evolutionarily conserved in the **ClpB/Hsp100 AAA+ disaggregase family**, with a bacterial ClpB homolog. **Orthologs (NCBI Gene):** mouse *Clpb* (GeneID 20480), rat *Clpb* (65041), zebrafish *clpb* (100331587); human *CLPB* Entrez 81570. No naturally occurring companion-animal or wildlife disease is documented (no OMIA entry noted). No zoonotic potential. The deep conservation of the disaggregase mechanism underpins the utility of zebrafish and rodent/cellular models.

### 15. Model Organisms

**Zebrafish:** morpholino *clpb* knockdown produces cerebellar/cerebral atrophy, rescued by wild-type but not mutant human *CLPB* mRNA — validating variant pathogenicity ([PMID: 25597510](https://pubmed.ncbi.nlm.nih.gov/25597510/)). **Cellular:** CRISPR CLPB-knockout of IL-3-dependent mouse **32Dcl3 myeloblasts** recapitulates the neutropenia-relevant defect — reduced mitochondrial membrane potential, insoluble HAX1 aggregates, ROS-driven apoptosis at G-CSF-induced differentiation ([PMID: 39644357](https://pubmed.ncbi.nlm.nih.gov/39644357/)). **Biochemical reconstitution:** purified human CLPB + HAX1 systems ([PMID: 42244541](https://pubmed.ncbi.nlm.nih.gov/42244541/)) and cryo-EM structural models ([PMID: 36745679](https://pubmed.ncbi.nlm.nih.gov/36745679/)). **Phenotype recapitulation:** zebrafish captures the neurological (recessive) phenotype; 32Dcl3 captures the myeloid differentiation defect. **Limitations:** no dedicated mouse model of the dominant SCN9 phenotype is yet reported; morphant models have known off-target caveats.

---

## Mechanistic Model / Interpretation

```
 Heterozygous dominant-negative CLPB missense variant (near ATP-binding pocket)
                         │
                         ▼
   Mutant subunit co-assembles with WT CLPB in mitochondrial IMS
                         │  (dominant-negative poisoning — demonstrated)
                         ▼
     ↓ CLPB ATPase & disaggregase/refoldase activity
                         │
            ┌────────────┴─────────────┐
            ▼                          ▼
   HAX1 aggregation          Impaired SPY complex
   (insoluble IMS clients)   (STOML2–PARL–YME1L1)
            └────────────┬─────────────┘
                         ▼
     ↓ mitochondrial membrane potential → ROS accumulation
                         │
                         ▼
   Apoptosis at ONSET of G-CSF-induced granulocytic differentiation
                         │
                         ▼
   Myeloid maturation arrest (promyelocyte/myelocyte)  ──► SEVERE NEUTROPENIA
                         │                                        │
                         ▼                                        ▼
         Recurrent bacterial infections (infancy)        MDS/AML risk (downstream, inferred)
```

**Zygosity–mechanism–outcome synthesis:**

| Feature | Monoallelic (SCN9, AD) | Biallelic (3-MGA-uria VII, AR) |
|---|---|---|
| OMIM | 619813 | 616271 |
| Mechanism | Dominant-negative missense | Loss of function (biallelic) |
| Neutropenia | Yes (100% maturation arrest) | Yes |
| 3-MGA-uria | Absent (0/5) | Characteristic |
| Cataracts / CNS / movement disorder | Uncommon | Frequent |
| 4-year survival | ~82% | ~50% |
| Median age at death | 2.4 years | 6 months |

The unifying insight is that *CLPB* sits at the heart of a **mitochondrial IMS proteostasis network** linking it to **HAX1** (SCN3/Kostmann) — explaining why two genetically distinct congenital neutropenias converge on the same disaggregase pathway. gnomAD LoF-tolerance proves that one functional allele suffices for neutrophil production; disease in SCN9 therefore requires an actively interfering allele, and the poisoned oligomer tips neutrophil precursors into ROS-driven apoptosis at their most vulnerable differentiation checkpoint.

---

## Evidence Base

| PMID | Title / Focus | Role in this report |
|---|---|---|
| [34115842](https://pubmed.ncbi.nlm.nih.gov/34115842/) | *Heterozygous variants of CLPB are a cause of severe congenital neutropenia* | **Defining paper**; dominant-negative mechanism, phenotype, HPO frequencies |
| [34140661](https://pubmed.ncbi.nlm.nih.gov/34140661/) | *Neutropenia and intellectual disability are hallmarks of biallelic and de novo CLPB deficiency* | De novo dominant-negative inheritance; refoldase>ATPase defect |
| [41719910](https://pubmed.ncbi.nlm.nih.gov/41719910/) | *From genotype to outcome: zygosity-specific insights in 63 cases* | Quantitative survival/outcome by zygosity |
| [39644357](https://pubmed.ncbi.nlm.nih.gov/39644357/) | *Mitochondrial CLPB is a pro-survival factor at onset of granulocytic differentiation* | 32Dcl3 model; ROS apoptosis; NAC/FFA/citrate rescue |
| [42244541](https://pubmed.ncbi.nlm.nih.gov/42244541/) | *HAX1 drives assembly and activation of CLPB* | CLPB–HAX1 axis; IMS insolubility |
| [38270563](https://pubmed.ncbi.nlm.nih.gov/38270563/) | *CLPB dysfunction impacts the proteolytic SPY complex* | Downstream IMS proteostasis collapse |
| [25597510](https://pubmed.ncbi.nlm.nih.gov/25597510/) | *CLPB mutations cause 3-MGA-uria, brain atrophy...* | Biallelic phenotype; zebrafish model; leukemia risk |
| [25597511](https://pubmed.ncbi.nlm.nih.gov/25597511/) | *CLPB variants — AR mitochondrial disorder* | Greenlandic founder effect |
| [41560087](https://pubmed.ncbi.nlm.nih.gov/41560087/) | *CLPB deficiency-associated congenital neutropenia: case report* | G-CSF efficacy; exome reanalysis |
| [10994541](https://pubmed.ncbi.nlm.nih.gov/10994541/) | *Severe congenital neutropenia: diagnosis & therapy* | SCN diagnostic definition |
| [36745679](https://pubmed.ncbi.nlm.nih.gov/36745679/) | *Structural characterization of human CLPB disaggregase* | Oligomerization; ankyrin domain |
| [38589208](https://pubmed.ncbi.nlm.nih.gov/38589208/) | *Clinicopathological features of congenital neutropenia syndromes* | MDS/AML risk; differential diagnosis |
| [15640815](https://pubmed.ncbi.nlm.nih.gov/15640815/), [15489867](https://pubmed.ncbi.nlm.nih.gov/15489867/) | HSCT in SCN | Curative transplant evidence |
| [40510848](https://pubmed.ncbi.nlm.nih.gov/40510848/), [41383606](https://pubmed.ncbi.nlm.nih.gov/41383606/) | WES/WGS & national neutropenia screening | Genetic diagnostic approach |
| [36074910](https://pubmed.ncbi.nlm.nih.gov/36074910/) | *POI in CLPB deficiency* | Adult/ovarian complication (biallelic) |

---

## Limitations and Knowledge Gaps

1. **Very small sample sizes.** The disease rests on ~10 heterozygous cases (Warren 2022) and a combined cohort of 63 across both zygosity forms (Heath 2026). HPO frequencies (e.g., cataract 2/10) have wide confidence intervals.
2. **No dedicated dominant-model organism.** Mechanistic data derive from CLPB-knockout cell lines and morphant zebrafish that model loss of function/recessive phenotypes, not the dominant-negative SCN9 state specifically.
3. **Spectrum vs dichotomy.** Some monoallelic cases show neurodevelopmental features, blurring the clean "isolated neutropenia" picture; genotype–phenotype rules remain incompletely defined.
4. **No validated epidemiologic prevalence/incidence** for SCN9 specifically (ultra-rare; registry data limited).
5. **Metabolic/antioxidant rescue is in vitro only** — NAC, FFA, and citrate have not been tested clinically.
6. **Leukemic transformation risk is extrapolated** from SCN broadly; CLPB-specific transformation rates are not quantified.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a knock-in mouse** carrying a human SCN9 dominant-negative *CLPB* missense allele to establish an in-vivo dominant model and quantify neutrophil, survival, and MDS/AML outcomes.
2. **Prospective natural-history registry** for CLPB-neutropenia to firm up prevalence, penetrance, transformation rates, and genotype–phenotype correlations (expanding the Heath 2026 cohort).
3. **Preclinical trial of antioxidant/metabolic rescue** (N-acetylcysteine, citrate, free fatty acids) in CLPB-deficient primary human CD34⁺ progenitors and the knock-in mouse, moving toward a pilot clinical study.
4. **Structural/biochemical dissection** of how each variant class (ATP-pocket missense vs ankyrin-domain disruption) poisons the oligomer, to build a variant-to-severity predictor usable in counseling.
5. **Longitudinal MDS/AML surveillance protocol** specific to CLPB-SCN, correlating clonal markers (e.g., *CSF3R*/*RUNX1* mutations) with transformation.
6. **Systematic HAX1–CLPB interaction mapping** in patient-derived cells to test whether HAX1 stabilization can bypass the CLPB defect therapeutically.

---

*Evidence source types represented: human clinical (cohorts/case reports), model organism (zebrafish), in vitro (32Dcl3 knockout, biochemical reconstitution, cryo-EM), and computational (gnomAD constraint, structural prediction).*


## Artifacts

- [OpenScientist final report](Severe_Congenital_Neutropenia_9-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Severe_Congenital_Neutropenia_9-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 18 |
| Quoted claims found in source | 18 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 18 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 13 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C15847` (1 mention) - the report calls it "antibiotics"; NCIT calls it **Non-Ionizing Radiotherapy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002718` (1 mention) - the report calls it "recurrent severe bacterial infections"; HP calls it **Recurrent bacterial infections**
- `NCIT:C15431` (1 mention) - the report calls it "allogeneic HSCT"; NCIT calls it **Hematopoietic Cell Transplantation**, and lists "HSCT" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `UMLS`, `GARD`.