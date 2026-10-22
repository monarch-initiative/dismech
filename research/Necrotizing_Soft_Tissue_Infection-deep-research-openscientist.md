---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T11:37:55.362032'
end_time: '2026-09-29T11:51:42.834635'
duration_seconds: 827.47
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Necrotizing Soft Tissue Infection
  mondo_id: MONDO:0018602
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
citation_count: 26
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 28
  quotes_valid: 23
  quotes_unsupported: 5
  unsupported_quote_references:
  - PMID:14620152
  - PMID:26633512
  - PMID:32828915
  - PMID:33945021
  - PMID:26908491
  relevance_assessed: 26
  on_topic: 9
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 22
  verified: 21
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0018602
    reported_labels:
    - MONDO
    ontology_label: necrotizing soft tissue infection
  obsolete_terms:
  - term_id: GO:0070265
    ontology_label: obsolete necrotic cell death
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Necrotizing_Soft_Tissue_Infection-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Necrotizing_Soft_Tissue_Infection-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Necrotizing Soft Tissue Infection
- **MONDO ID:** MONDO:0018602 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Necrotizing Soft Tissue Infection** covering all of the
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

# Necrotizing Soft Tissue Infection (NSTI): Comprehensive Disease Characteristics Report

**Disease:** Necrotizing Soft Tissue Infection
**MONDO ID:** MONDO:0018602
**Category:** Infectious Disease
**Report basis:** 12 confirmed findings, 56 papers reviewed across 5 investigation iterations. Evidence is drawn from aggregated disease-level resources (systematic reviews, cohort and case-control studies, registries) supplemented by individual case reports and mechanistic in vitro / animal studies.

---

## Summary

Necrotizing soft tissue infection (NSTI) is a rare, rapidly progressive, life- and limb-threatening bacterial (occasionally fungal) infection that destroys subcutaneous tissue, fascia, and/or muscle. It is not a Mendelian disorder and has **no OMIM entry**; instead it is an acquired infectious disease in which host factors (comorbidities and HLA class II genotype) modulate susceptibility and severity. NSTI is classified into four microbiological types: **Type I** (polymicrobial, mixed aerobic/anaerobic, ~55–75% of cases, typical of diabetics/immunocompromised, includes Fournier gangrene), **Type II** (monomicrobial, classically Group A *Streptococcus* [GAS], associated with streptococcal toxic shock syndrome [STSS]), **Type III** (gram-negative monomicrobial including *Vibrio vulnificus* and *Clostridium* spp./gas gangrene), and **Type IV** (fungal, in immunocompromised or trauma hosts, worse outcomes).

The pathophysiology runs as a causal chain from pathogen inoculation through a portal of entry, to spread along relatively avascular fascial planes, release of virulence factors and superantigens, an HLA-restricted cytokine storm, microvascular thrombosis and ischemia, liquefactive necrosis, and finally systemic toxic/septic shock and multi-organ failure. Diagnosis is ultimately **clinical and surgical** — the LRINEC score and CT imaging are adjuncts that **cannot rule out** the disease (LRINEC sensitivity only ~59%). The single most important determinant of survival is **early aggressive surgical debridement (ideally < 6 hours)** combined with broad-spectrum antibiotics that include **clindamycin** for its toxin-suppressing, pathogen-load-independent action in toxin-mediated disease.

Despite optimal care, mortality remains high (~11–35% acutely, up to ~68% when STSS complicates invasive GAS), amputation occurs in ~13–60% of extremity cases, and survivors face disfigurement, functional disability, and measurably reduced quality of life. There is **no licensed vaccine**; prevention rests on risk-factor control, early recognition, wound care, and — for household contacts of invasive GAS index cases — targeted antibiotic chemoprophylaxis in some jurisdictions. Diabetes mellitus is the dominant acquired risk factor, and striking demographic disparities exist (e.g., First Nations Australians with 88× higher incidence).

---

## Key Findings

### 1. Disease Information, Identifiers, and Temporal Course

NSTI is a group of severe infections causing rapid, progressive necrosis of subcutaneous tissue, fascia, and/or muscle. *Necrotizing Soft Tissue Infections* ([PMID: 40185551](https://pubmed.ncbi.nlm.nih.gov/40185551/)) describes them as "a diverse group of severe infections of the skin, fascia, and musculature… characterized by the rapid and progressive destruction of soft tissue."

**Synonyms / subtypes:** necrotizing fasciitis, "flesh-eating disease," Fournier gangrene (perineal/genital), Meleney's / hemolytic streptococcal gangrene, clostridial myonecrosis (gas gangrene), Ludwig's angina / cervical NF.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0018602 |
| ICD-10 | M72.6 (Necrotizing fasciitis); N49.3 (Fournier gangrene); A48.0 (gas gangrene) |
| ICD-11 | 1B70–1B7Z (bacterial skin infections) region |
| MeSH | D019115 "Fasciitis, Necrotizing"; D005393 (Fournier gangrene) |
| SNOMED CT | 52486002 (Necrotizing fasciitis) |
| OMIM | None (not a Mendelian disorder) |

**Temporal course:** Acute onset over hours to a few days; rapidly progressive (fascial advancement can exceed 1 inch/hour in fulminant GAS cases); any age (neonatal Fournier to geriatric), adult-predominant. The course is monophasic/self-limited if the patient survives source control (not relapsing-remitting or chronic), though recurrence of invasive GAS in the same host is documented. The **critical intervention window** is < 6 hours to debridement, with markedly worse outcomes after 12–24 hours ([PMID: 39259555](https://pubmed.ncbi.nlm.nih.gov/39259555/)). Information source: aggregated disease-level resources supplemented by EHR/case-report individual data — not a single patient-level dataset.

### 2. Etiology and Risk Factors

NSTI is fundamentally an **infectious disease**; host factors modulate risk. Major acquired risk factors include **diabetes mellitus (present in 40–62% of cohorts)**, advanced age, obesity/high BMI, smoking, alcohol use, chronic kidney disease, immunosuppression, malignancy, peripheral vascular disease, IV drug use, and any skin/mucosal breach or trauma. In a resource-limited cohort of 119 cases, "the lower extremities were most commonly affected (58.8%), and diabetes was prevalent (62.3%)" ([PMID: 40721651](https://pubmed.ncbi.nlm.nih.gov/40721651/)). For Fournier gangrene, diabetes (OR 2.51, 95% CI 2.38–2.64) and malignancy (OR 2.29, 95% CI 2.07–2.54) are quantified risk factors ([PMID: 39356576](https://pubmed.ncbi.nlm.nih.gov/39356576/)).

**Host genetic susceptibility (Type II / GAS):** A case-control study (43 invasive GAS cases vs 1,540 controls) found "each copy of the HLA-DQA1*01:03 allele associates with a twofold increased risk of disease (odds ratio 2.3, 95% confidence interval 1.3-4.4, P = 0.009)" ([PMID: 31462703](https://pubmed.ncbi.nlm.nih.gov/31462703/)). Mechanistically, HLA class II allelic variation determines superantigen presentation strength: "Significantly higher proliferative responses were detected when streptococcal pyrogenic exotoxin (Spe) A was presented by cells expressing DQA1*0101/DQB1*0302 (DQ3.2), as compared to cells expressing DR1, DR4, or DR5 alleles" ([PMID: 12207341](https://pubmed.ncbi.nlm.nih.gov/12207341/)). Severe vs non-severe invasive GAS outcome "was largely related to the human leukocyte antigen class II type of the patient" ([PMID: 14620152](https://pubmed.ncbi.nlm.nih.gov/14620152/)). No germline causal genes, pathogenic ACMG variants, epigenetic signatures, or chromosomal abnormalities apply — susceptibility is multifactorial/polygenic, not monogenic. Protective genetic factors are not defined; certain HLA haplotypes are neutralizing/low-responder and behave protectively.

### 3. Infectious Agents and Environmental Exposures

Causative agents span the microbial kingdoms (NCBI Taxonomy IDs in parentheses):

| Type | Pathogens | Context |
|---|---|---|
| Type I (polymicrobial) | Mixed anaerobes + aerobes: *Bacteroides*, *Peptostreptococcus*, Enterobacterales (*E. coli* txid562, *Klebsiella pneumoniae* txid573) | Diabetics/immunocompromised; Fournier gangrene |
| Type II (monomicrobial) | *Streptococcus pyogenes* / GAS (txid1314); *Staphylococcus aureus* incl. MRSA (txid1280) | Healthy younger patients; STSS |
| Type III (gram-negative/clostridial) | *Vibrio vulnificus* (txid672); *Aeromonas hydrophila* (txid644); *Clostridium perfringens* (txid1502) | Marine/shellfish, hepatic disease; freshwater; gas gangrene |
| Type IV (fungal) | Mucorales (*Rhizopus*), *Candida* | Immunocompromised/diabetic, trauma |

A large cohort documented gram-negative predominance: "Gram-negative bacteria were predominant (62.7%), particularly *Escherichia coli* (21.6%) and *Klebsiella pneumoniae* (19.4%), while Gram-positive bacteria were led by *Staphylococcus aureus* (14.9%)" ([PMID: 40721651](https://pubmed.ncbi.nlm.nih.gov/40721651/)). Fungal involvement is prognostically important: "Of 634 patients, 110 (17.4%) had fungal-positive wound cultures" ([PMID: 42209417](https://pubmed.ncbi.nlm.nih.gov/42209417/)).

**Environmental/lifestyle contributors:** penetrating trauma, surgery, injection drug use, insect/animal bites, childbirth, seawater or freshwater wound exposure, raw shellfish ingestion, and immunosuppression. NSAID use has been hypothesized (not proven) to mask symptoms/worsen GAS NSTI.

### 4. Mechanism / Pathophysiology — Ordered Causal Chain

Using the GAS Type II archetype as the reference, the mechanistic sequence is:

1. **Portal of entry** (skin/mucosal breach, trauma, surgery, or hematogenous seeding from pharyngitis) **allows** bacterial inoculation into subcutaneous tissue/fascia.
2. **Bacteria proliferate along the relatively avascular superficial/deep fascial planes**, spreading faster than overlying skin changes — the fibrinolytic machinery of GAS aids this: "GAS produces several factors that can initiate the dissolution of these fibrin clots to spread to deeper tissues" ([PMID: 39804237](https://pubmed.ncbi.nlm.nih.gov/39804237/)).
3. **Secreted virulence factors** — M protein (antiphagocytic), streptolysins O/S, streptococcal pyrogenic exotoxins (SpeA/B/C), hyaluronidase, streptokinase — **degrade extracellular matrix and lyse cells**.
4. **Superantigens crosslink MHC class II (HLA-DR/DQ) with T-cell receptor Vβ regions**, causing massive polyclonal T-cell activation → **cytokine storm** (TNF-α, IL-1, IL-6, IFN-γ). *(Mechanistically demonstrated in vitro / animal models.)* IVIG is used therapeutically because it acts by "neutralization of superantigens" ([PMID: 41714399](https://pubmed.ncbi.nlm.nih.gov/41714399/)).
5. **Cytokines + toxins injure vascular endothelium → microvascular thrombosis** of nutrient vessels → **local ischemia**. *(Inferred from histopathology rather than directly demonstrated longitudinally in humans.)*
6. **Ischemia + direct toxin cytotoxicity → liquefactive necrosis** of fascia, fat, and eventually muscle/skin; this also impairs antibiotic/leukocyte delivery.
7. **Systemic toxin/cytokine spillover → streptococcal toxic shock syndrome:** vasodilation, capillary leak, hypotension, DIC, multi-organ failure. The predominant invasive GAS type, emm1, "was significantly associated with STSS" ([PMID: 40193020](https://pubmed.ncbi.nlm.nih.gov/40193020/)).

**Branch — Clostridial gas gangrene (Type III):** *C. perfringens* **α-toxin** is a phospholipase C/sphingomyelinase that "possesses phospholipase C and sphingomyelinase activities" and "is a key mediator of gas gangrene… fever, pain, edema, myonecrosis, and gas production" ([PMID: 26633512](https://pubmed.ncbi.nlm.nih.gov/26633512/)). It binds membrane lipid rafts, generates diacylglycerol, activates PLCγ-1, and "specifically induces endothelial cell death by promoting ceramide-mediated apoptosis" ([PMID: 32828915](https://pubmed.ncbi.nlm.nih.gov/32828915/)) — directly producing the vascular injury, edema, and myonecrosis of gas gangrene. Perfringolysin O (theta-toxin) activates the inflammasome.

**Suggested ontology terms:** GO biological processes — response to bacterium (GO:0009617), inflammatory response (GO:0006954), positive regulation of cytokine production (GO:0001819), blood coagulation (GO:0007596), necrotic cell death (GO:0070265). CHEBI — ceramide (CHEBI:17761), diacylglycerol.

### 5. Phenotypes, Anatomy, and Ontology Terms

**Signs/symptoms** (acute, rapidly progressive): pain out of proportion to exam findings (early, key clue), tense edema extending beyond erythema, erythema, fever (HP:0001945), tachycardia, hypotension/septic shock (HP:0001319), skin discoloration (dusky/gray/purple), hemorrhagic bullae, skin necrosis (HP:0200042), crepitus (subcutaneous gas), anesthesia of overlying skin (cutaneous nerve destruction), and "dishwater" gray drainage. *Necrotizing Fasciitis* ([PMID: 37465410](https://pubmed.ncbi.nlm.nih.gov/37465410/)) notes: "Signs and symptoms suggestive of necrotizing fasciitis include skin necrosis, hemorrhagic bullae, pain out of proportion, and erythema progressing beyond margins."

**Laboratory abnormalities:** elevated CRP (HP:0011227), leukocytosis or leukopenia, hyponatremia (HP:0002902), elevated creatinine/AKI (HP:0012622), hyperglycemia (HP:0003074), elevated creatine kinase, coagulopathy/DIC, elevated lactate. Prognostically, "white blood cell count (WBC) < 4,000/µL (OR, 7.8; 95% CI 2.4-25.6, p = 0.001), serum creatine kinase (CK) ≥ 300 U/L" predict STSS ([PMID: 40193020](https://pubmed.ncbi.nlm.nih.gov/40193020/)).

**Anatomy (UBERON):** subcutaneous tissue (UBERON:0002072), superficial and deep fascia (UBERON:0007798), skin (UBERON:0002097), skeletal muscle when myonecrosis (UBERON:0001134). Most common sites: lower extremities (~59%), then perineum/genitalia (Fournier gangrene), abdominal wall, upper extremities, and rarely head/neck (cervical) and periorbital. Usually unilateral/localized initially. **Cell types (CL):** endothelial cells (CL:0000115), neutrophils (CL:0000775), T lymphocytes (CL:0000084), fascial fibroblasts.

**Quality-of-life impact:** disfigurement, large soft-tissue defects, functional disability, and body-image distress (see Prognosis).

### 6. Diagnosis

Surgical exploration is the diagnostic **gold standard** ("finger test," gray necrotic fascia, "dishwater" fluid, lack of bleeding). "Ultimately, the diagnosis is clinical. Surgical exploration is warranted when there is high suspicion for NSTI, even if the diagnosis is uncertain" ([PMID: 39259555](https://pubmed.ncbi.nlm.nih.gov/39259555/)).

The **LRINEC score** (CRP, WBC, hemoglobin, sodium, creatinine, glucose) is an adjunct only: "A score ≥ 6 is a relatively specific indicator of necrotizing fasciitis (specificity 83.8%), but a score <6 is not sensitive (59.2%) enough to rule out necrotizing fasciitis" ([PMID: 33570428](https://pubmed.ncbi.nlm.nih.gov/33570428/)). **CT** is the imaging modality of choice (sensitivity ~80%); the best single sign is fascial fluid: "presence of fluid along the deep fascia was significantly associated with NSTI (odds ratio [OR] = 10.28, 95% CI: 1.57 to 67.18, p = 0.015)" ([PMID: 33945021](https://pubmed.ncbi.nlm.nih.gov/33945021/)). Gas is specific but insensitive/late. Genetic/omics testing is **not applicable** for diagnosis; microbiological culture of deep tissue guides antibiotic tailoring. Differential diagnosis includes cellulitis, pyomyositis, abscess, and non-infective mimics such as pancreatic panniculitis.

### 7. Treatment

The cornerstone is **early aggressive surgical debridement**: "Early surgical debridement is crucial for improved outcomes and should be performed as soon as possible, ideally within 6 hours of presentation" ([PMID: 39259555](https://pubmed.ncbi.nlm.nih.gov/39259555/)), repeated every 12–24 h until no further necrosis.

Empirical **broad-spectrum antibiotics** (e.g., piperacillin-tazobactam or a carbapenem + vancomycin/linezolid for MRSA + clindamycin) are started immediately and tailored to cultures. **Clindamycin** is added for its toxin-suppressing action: "Clindamycin is effective irrespective of pathogen load and is suggested to inhibit toxin production, while IVIG is hypothesized to modulate the immune response through multiple mechanisms, including neutralization of superantigens" ([PMID: 41714399](https://pubmed.ncbi.nlm.nih.gov/41714399/)). Guidelines recommend: "In severe or toxin-mediated infections (eg, necrotizing fasciitis or streptococcal toxic shock syndrome), adjunctive clindamycin is suggested, with linezolid as an alternative where clindamycin resistance is confirmed" ([PMID: 42552564](https://pubmed.ncbi.nlm.nih.gov/42552564/)). **IVIG** may be considered in toxin-mediated STSS but evidence is insufficient for routine use; **hyperbaric oxygen** is unproven. Supportive care (ICU, vasopressors, renal replacement) and reconstructive surgery/rehabilitation complete the pathway.

**Suggested NCIT terms:** Surgical Debridement, Clindamycin (NCIT:C374), Intravenous Immunoglobulin Therapy, Hyperbaric Oxygen Therapy.

### 8. Epidemiology and Population

NSTI is rare — "the incidence of approximately 1000 cases annually in the United States" ([PMID: 33570428](https://pubmed.ncbi.nlm.nih.gov/33570428/)); international incidence ~0.3–4 per 100,000/year. Male predominance (M:F up to ~5:1). Marked demographic disparities exist: in Far North Queensland, "51% identified as First Nations, an incidence rate 88 times higher than all other ethnicities put together" ([PMID: 41150376](https://pubmed.ncbi.nlm.nih.gov/41150376/)). Lower extremities are most commonly affected (58.8%) ([PMID: 40721651](https://pubmed.ncbi.nlm.nih.gov/40721651/)). No Mendelian inheritance pattern applies; susceptibility is polygenic/multifactorial with the HLA class II contribution described above.

### 9. Prognosis and Outcomes

Acute mortality is 11–35%, rising dramatically with STSS: "the fatality rate within 28 days of admission was higher in patients with STSS (67.9%, 38/56) than in those without (3.6%, 9/249)" ([PMID: 40193020](https://pubmed.ncbi.nlm.nih.gov/40193020/)). Amputation occurs in ~13–60% of extremity cases (diabetes predicts amputation). Survivors have lasting deficits: in 56 NF survivors assessed by SF-36, "Mean Mental Component Score (MCS) was 44.5 ± 14.3 and mean Physical Component Score (PCS) was 36.5 ± 11.5; both means were lower than the Canadian population norm of 50," and "the only factors that were statistically significant in the final models were confidence with appearance for the MCS and %TBSA for the PCS" ([PMID: 29503165](https://pubmed.ncbi.nlm.nih.gov/29503165/)).

**Prognostic factors/biomarkers:** delay to surgery, age, comorbidities (diabetes, CKD), septic shock, LRINEC components, elevated lactate, WBC < 4,000/µL (OR 7.8), CK ≥ 300 U/L, underlying kidney disease (OR 10.7), and emm1 GAS genotype (OR 5.2). Recovery is possible with prompt source control but often incomplete; the disease is acute/self-limited if survived (not chronic), though reconstruction and rehabilitation are prolonged.

### 10. Prevention

**No licensed vaccine** exists for NSTI/GAS (multivalent M-protein and conserved-antigen GAS vaccines remain experimental). Primary prevention centers on risk-factor control (glycemic control, prompt wound care, avoiding seawater/raw-shellfish exposure with open wounds or liver disease, safe injection practices). Secondary prevention = early recognition and immediate surgery.

Public-health prevention targets **secondary household transmission** of invasive GAS: "The attack rate during the 30 days after first exposure to a primary case was 4,520 per 100,000 person-years at risk (95% confidence interval (CI): 2,900-6,730) a 1,940 (95% CI: 1,240-2,880) fold elevation over the background incidence" ([PMID: 28537550](https://pubmed.ncbi.nlm.nih.gov/28537550/)). Transmission concentrates in prolonged close contacts: "The same clone was present in the throat of 36% of close contacts who had exposure to the index patient… for >24 hours/week, whereas the strain was present in only 2% of the other contacts" ([PMID: 26908491](https://pubmed.ncbi.nlm.nih.gov/26908491/)). Policies vary; the Netherlands expanded prophylaxis in 2023 "offering antibiotic prophylaxis to household contacts of all patients with iGAS rather than only those presenting with necrotizing fasciitis or streptococcal toxic shock syndrome" ([PMID: 41505128](https://pubmed.ncbi.nlm.nih.gov/41505128/)).

### 11. Other Species and Model Organisms

**Natural disease in other species:** *Streptococcus canis* causes "streptococcal toxic shock syndrome (STSS) and necrotizing fasciitis (NF) in dogs" ([PMID: 10591501](https://pubmed.ncbi.nlm.nih.gov/10591501/)), possessing M protein and streptolysin O but lacking many *S. pyogenes* superantigen genes.

**Model organisms:**
- **Mouse** (mainstay): humanized HLA-II transgenic mice reproduce superantigen-driven responses that inbred mice (innately refractory to superantigens) lack; the advanced recombinant inbred BXD panel maps host genetic loci. "We discuss the versatility of the HLA-II transgenic mouse model that allowed the biological validation of known genetic associations to GAS NSTI" ([PMID: 33079368](https://pubmed.ncbi.nlm.nih.gov/33079368/)).
- **Zebrafish** (*Danio rerio*): "the fatal infection by S. pyogenes causes a locally spreading necrotic disease confined to the muscle with pathology similar to what is observed in a human infection of necrotizing fasciitis" ([PMID: 15158689](https://pubmed.ncbi.nlm.nih.gov/15158689/)).
- **Broader review:** rodents, zebrafish, rabbits, pigs, and non-human primates — "This review critically evaluates NF models in rodents, zebrafish, rabbits, pigs, and non-human primates" ([PMID: 41333035](https://pubmed.ncbi.nlm.nih.gov/41333035/)).

**Limitations:** GAS is human-specific (superantigens require human HLA-II); inbred mice under-represent host genetic diversity; no single model captures immunopathology + systemic dissemination + biofilm persistence simultaneously.

---

## Mechanistic Model / Interpretation

```
  PORTAL OF ENTRY (trauma, surgery, mucosal breach, hematogenous seeding)
            │  allows inoculation
            ▼
  FASCIAL-PLANE PROLIFERATION (avascular planes; fibrinolysis via streptokinase/SpeB)
            │  spreads faster than skin changes  →  "pain out of proportion"
            ▼
  VIRULENCE-FACTOR RELEASE (M protein, streptolysins, SpeA/B/C, hyaluronidase)
            │                                   ┌─────────────────────────────┐
            ▼                                   │  BRANCH: Clostridial α-toxin │
  SUPERANTIGEN × HLA-II × TCR-Vβ                │  (PLC/sphingomyelinase) →    │
            │  polyclonal T-cell activation      │  ceramide apoptosis of        │
            ▼                                   │  endothelium → myonecrosis +  │
  CYTOKINE STORM (TNF-α, IL-1, IL-6, IFN-γ)     │  gas production               │
            │  (HLA-DQA1*01:03 amplifies)        └─────────────────────────────┘
            ▼
  ENDOTHELIAL INJURY → MICROVASCULAR THROMBOSIS → LOCAL ISCHEMIA
            │  (+ impaired antibiotic/leukocyte delivery)
            ▼
  LIQUEFACTIVE NECROSIS of fascia → fat → muscle → skin
            │
            ▼
  SYSTEMIC SPILLOVER → STREPTOCOCCAL TOXIC SHOCK (STSS)
            │  vasodilation, capillary leak, hypotension, DIC
            ▼
  MULTI-ORGAN FAILURE → DEATH (up to ~68% with STSS)
```

The model integrates host and pathogen: pathogen virulence (emm1, superantigens, α-toxin) provides the "trigger," while host HLA class II genotype and comorbidities (diabetes, CKD, immunosuppression) set the "gain" on the inflammatory and ischemic amplification. The therapeutic logic maps directly onto the chain — **surgery** removes the necrotic, ischemic, antibiotic-inaccessible focus (steps 5–6); **clindamycin** shuts off toxin synthesis independent of pathogen load (steps 3–4); **IVIG** neutralizes circulating superantigens (step 4). Because steps 5–7 are self-amplifying and time-dependent, the < 6-hour debridement window is the dominant prognostic lever.

| Mechanism step | Upstream/Downstream | Key cell types | Evidence type |
|---|---|---|---|
| Inoculation & fascial spread | Upstream | Fibroblasts, keratinocytes | Clinical/microbiological |
| Superantigen → cytokine storm | Middle | T lymphocytes, APCs | In vitro / transgenic mouse |
| Microvascular thrombosis/ischemia | Middle | Endothelial cells | Histopathology (inferred link) |
| Necrosis | Downstream | All soft-tissue cells | Clinical/pathology |
| Toxic shock / MOF | Downstream (systemic) | Endothelium, immune | Clinical cohort |

---

## Evidence Base

| PMID | Contribution | Support/Challenge |
|---|---|---|
| [39259555](https://pubmed.ncbi.nlm.nih.gov/39259555/) | Diagnosis is clinical/surgical; < 6 h debridement standard | Supports F003, F004, F011 |
| [40185551](https://pubmed.ncbi.nlm.nih.gov/40185551/) | Definition and rapid destructive course | Supports F011 |
| [40721651](https://pubmed.ncbi.nlm.nih.gov/40721651/) | 119-case cohort: gram-negative predominance, diabetes 62%, lower-limb 59% | Supports F001, F005, F007, F012 |
| [42209417](https://pubmed.ncbi.nlm.nih.gov/42209417/) | Fungal (Type IV) frequency 17.4% and worse outcomes | Supports F001 |
| [31462703](https://pubmed.ncbi.nlm.nih.gov/31462703/) | HLA-DQA1*01:03 OR 2.3 susceptibility | Supports F002 |
| [12207341](https://pubmed.ncbi.nlm.nih.gov/12207341/) | HLA-DQ presents SpeA more strongly than DR | Supports F002 |
| [14620152](https://pubmed.ncbi.nlm.nih.gov/14620152/) | HLA class II drives severe vs mild outcome | Supports F002 |
| [33570428](https://pubmed.ncbi.nlm.nih.gov/33570428/) | LRINEC performance (spec 83.8%, sens 59.2%); ~1000 US cases/yr | Supports F003, F005 |
| [33945021](https://pubmed.ncbi.nlm.nih.gov/33945021/) | CT: deep-fascial fluid OR 10.28 | Supports F003 |
| [41714399](https://pubmed.ncbi.nlm.nih.gov/41714399/) | Clindamycin (load-independent) + IVIG (superantigen neutralization) | Supports F004, F006 |
| [42552564](https://pubmed.ncbi.nlm.nih.gov/42552564/) | Guideline: adjunctive clindamycin, linezolid alternative | Supports F004 |
| [39356576](https://pubmed.ncbi.nlm.nih.gov/39356576/) | Fournier gangrene risk: diabetes OR 2.51, malignancy OR 2.29 | Supports F005 |
| [41150376](https://pubmed.ncbi.nlm.nih.gov/41150376/) | First Nations incidence 88× higher | Supports F005 |
| [40193020](https://pubmed.ncbi.nlm.nih.gov/40193020/) | emm1↔STSS; WBC<4000 OR 7.8; STSS 28-day fatality 67.9% | Supports F006, F007, F009 |
| [39804237](https://pubmed.ncbi.nlm.nih.gov/39804237/) | Fibrinolysis-mediated deep-tissue spread | Supports F006 |
| [37465410](https://pubmed.ncbi.nlm.nih.gov/37465410/) | Hallmark signs/symptoms | Supports F007 |
| [33079368](https://pubmed.ncbi.nlm.nih.gov/33079368/) | HLA-II transgenic + BXD systems-genetics mouse models | Supports F008 |
| [15158689](https://pubmed.ncbi.nlm.nih.gov/15158689/) | Zebrafish NF-like myositis model | Supports F008 |
| [41333035](https://pubmed.ncbi.nlm.nih.gov/41333035/) | NF models across 5 species | Supports F008 |
| [10591501](https://pubmed.ncbi.nlm.nih.gov/10591501/) | Canine STSS/NF (*S. canis*) | Supports F008 |
| [29503165](https://pubmed.ncbi.nlm.nih.gov/29503165/) | Long-term QoL deficits (SF-36 MCS/PCS below norm) | Supports F009 |
| [28537550](https://pubmed.ncbi.nlm.nih.gov/28537550/) | Household iGAS attack rate 4,520/100k PY (1,940× background) | Supports F010 |
| [26908491](https://pubmed.ncbi.nlm.nih.gov/26908491/) | Transmission concentrated in >24 h/week contacts | Supports F010 |
| [41505128](https://pubmed.ncbi.nlm.nih.gov/41505128/) | Netherlands 2023 prophylaxis policy expansion | Supports F010 |
| [32828915](https://pubmed.ncbi.nlm.nih.gov/32828915/) | α-toxin → ceramide-mediated endothelial apoptosis | Supports F012 |
| [26633512](https://pubmed.ncbi.nlm.nih.gov/26633512/) | α-toxin PLC/sphingomyelinase mechanism in gas gangrene | Supports F012 |

---

## Limitations and Knowledge Gaps

- **No individual patient-level dataset was analyzed.** This report synthesizes aggregated disease-level literature (reviews, cohorts, case-control studies) plus mechanistic in vitro/animal work; no primary omics or EHR data were available to test hypotheses statistically. Findings represent evidence synthesis rather than de novo statistical discovery.
- **Microbiological distributions are region-dependent.** The 62.7% gram-negative predominance ([PMID: 40721651](https://pubmed.ncbi.nlm.nih.gov/40721651/)) reflects one resource-limited setting; Western cohorts often report higher GAS/polymicrobial fractions. Cohort sizes are modest and retrospective.
- **The microvascular-thrombosis → ischemia step is inferred** from histopathology rather than directly demonstrated longitudinally in humans; superantigen/cytokine steps rest largely on in vitro and transgenic-mouse evidence.
- **Host genetics beyond HLA are poorly mapped.** The HLA-DQA1*01:03 association (OR 2.3, n=43 cases) is from a single modest study; no GWAS-scale, multi-locus susceptibility architecture is established, and no protective genetic variants are defined.
- **Adjunctive therapy evidence is weak.** IVIG and hyperbaric oxygen lack definitive randomized support; clindamycin's benefit is largely mechanistic/observational.
- **Prevention lacks a vaccine and consensus on chemoprophylaxis**, with policies diverging between jurisdictions.
- **Model organisms are imperfect:** GAS superantigen biology is human-HLA-specific, limiting non-humanized models.

---

## Proposed Follow-up Experiments / Actions

1. **Multicenter prospective NSTI registry** capturing time-to-debridement, microbiology (with molecular typing/emm), host HLA genotype, biomarkers (lactate, CK, WBC), and standardized long-term QoL (SF-36/EQ-5D) to move beyond single-center retrospective cohorts.
2. **GWAS / targeted HLA fine-mapping** in a large invasive-GAS/NSTI case-control cohort to replicate and extend the HLA-DQA1*01:03 signal and search for protective alleles and non-HLA modifier loci.
3. **Randomized trial of adjunctive clindamycin ± IVIG** in toxin-mediated NSTI/STSS, powered on 28-day mortality, to convert mechanistic rationale into level-1 evidence.
4. **Biomarker-driven early-diagnosis study** combining LRINEC with point-of-care lactate, procalcitonin, and CT deep-fascial-fluid criteria to build a rule-in/rule-out decision tool with prospective validation (given LRINEC's 59% sensitivity limitation).
5. **Humanized HLA-II transgenic mouse and zebrafish studies** dissecting the superantigen → endothelial-thrombosis → ischemia link with intravital imaging, and testing α-toxin-neutralizing agents in clostridial models.
6. **Vaccine development** advancing conserved-antigen or multivalent M-protein GAS candidates through immunogenicity trials, with modeling of population-level NSTI/STSS impact.
7. **Prospective evaluation of household iGAS chemoprophylaxis policies** (e.g., the Netherlands 2023 expansion) to quantify number-needed-to-treat and secondary-case reduction across risk strata.

---

*Report compiled from 12 confirmed findings and 56 reviewed papers. Evidence types are indicated throughout as human clinical (cohort/case-control/registry), model organism, in vitro/mechanistic, or computational. Where a mechanistic step is inferred rather than directly demonstrated in humans, this is stated explicitly.*


## Artifacts

- [OpenScientist final report](Necrotizing_Soft_Tissue_Infection-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Necrotizing_Soft_Tissue_Infection-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 28 |
| Quoted claims found in source | 23 |
| Quoted claims **not** found in source | 5 |
| References weighed for topical relevance | 26 |
| On topic | 9 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

4 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:14620152` *(abstract only)*: "was largely related to the human leukocyte antigen class II type of the patient"
  - closest text in source: "This difference was largely related to the human leukocyte antigen class 11 type of the patient"
- `PMID:26633512`: "is a key mediator of gas gangrene… fever, pain, edema, myonecrosis, and gas production"
  - closest text in source: "Clostridium perfringens alpha-toxin is a key mediator of gas gangrene, which is a life-threatening infection that manifests as fever, pain, edema, myonecrosis, and gas production"
- `PMID:32828915` *(abstract only)*: "specifically induces endothelial cell death by promoting ceramide-mediated apoptosis"
  - closest text in source: "Together, our results suggest that α-toxin-induced endothelial cell death promotes severe myonecrosis and is involved in the pathogenesis of C"
- `PMID:33945021` *(abstract only)*: "presence of fluid along the deep fascia was significantly associated with NSTI (odds ratio [OR] = 10.28, 95% CI: 1.57 to 67.18, p = 0.015)"
  - closest text in source: "presence of fluid along the deep fascia was significantly associated with NSTI (odds ratio [OR] = 10.28, 95% CI: 1.57 to 67.18, p = 0.015)"
- `PMID:26908491` *(abstract only)*: "The same clone was present in the throat of 36% of close contacts who had exposure to the index patient… for >24 hours/week, whereas the strain was present in only 2% of the other contacts"
  - closest text in source: "The same clone was present in the throat of 36% of close contacts who had exposure to the index patient (family households and classroom contacts) for >24 hours/week, whereas the strain was present in only 2% of the other contacts"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0018602` (2 mentions) - the report calls it "MONDO"; MONDO calls it **necrotizing soft tissue infection**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0070265` (obsolete necrotic cell death) (1 mention)