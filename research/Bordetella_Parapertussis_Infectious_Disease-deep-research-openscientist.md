---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T23:07:20.868230'
end_time: '2026-09-29T23:21:38.524111'
duration_seconds: 857.66
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Bordetella Parapertussis Infectious Disease
  mondo_id: MONDO:0001353
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
citation_count: 27
reference_validation:
  total_references: 33
  verified: 33
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 33
  on_topic: 28
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 30
  verified: 29
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 11
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0002102
    reported_labels:
    - Cough
    ontology_label: Pleuritis
  - term_id: HP:0031251
    reported_labels:
    - Paroxysmal cough
    ontology_label: Abnormal subclavian artery morphology
  labels_variant: 6
  obsolete_terms:
  - term_id: GO:0009405
    ontology_label: obsolete pathogenesis
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Bordetella_Parapertussis_Infectious_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Bordetella_Parapertussis_Infectious_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bordetella Parapertussis Infectious Disease
- **MONDO ID:** MONDO:0001353 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Bordetella Parapertussis Infectious Disease** covering all of the
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

# Bordetella parapertussis Infectious Disease — Comprehensive Disease Characterization

**MONDO ID:** MONDO:0001353 | **Category:** Infectious Disease | **Report date:** 2026-09-30

---

## Summary

**Bordetella parapertussis** is a Gram-negative, aerobic coccobacillus of the *B. bronchiseptica* cluster that causes **parapertussis** — a whooping-cough (pertussis-like) illness in humans and, in a genetically distinct ovine-adapted lineage, a chronic non-progressive pneumonia in sheep. In humans it colonizes the ciliated respiratory epithelium of the upper and lower airways and deploys a set of BvgAS-regulated virulence factors that it shares with *B. pertussis* (filamentous hemagglutinin, fimbriae, pertactin, the bifunctional adenylate cyclase/hemolysin toxin CyaA, dermonecrotic toxin, and tracheal cytotoxin), while **notably lacking pertussis toxin** and instead expressing an **O-antigen lipopolysaccharide** that *B. pertussis* does not make. The disease it produces is on average milder and shorter than classic pertussis and lacks the marked lymphocytosis that pertussis toxin drives — yet it is **not benign**: it produces measurable morbidity, hospitalizations, ICU admissions, and rare deaths, and in older children has been associated with *higher* odds of severe outcomes than *B. pertussis*.

The single most consequential public-health feature of this organism is that **current pertussis vaccines provide little to no cross-protection against it**. Acellular pertussis (aP) vaccines are built primarily around pertussis toxin and a handful of *B. pertussis* surface antigens, and because *B. parapertussis* neither expresses pertussis toxin nor shares the O-antigen, immunity generated by vaccination does not neutralize it. A large meta-analysis found no significant protective effect, and animal work shows aP vaccination can paradoxically *facilitate* *B. parapertussis* infection by dampening the innate/neutrophil response that would otherwise limit it. This has evolutionary and epidemiological implications: as pertussis-toxin-directed immunity suppresses *B. pertussis*, an ecological niche may open for the vaccine-escaping *B. parapertussis*.

This report synthesizes the mechanistic and clinical picture assembled over the investigation. Because *B. parapertussis* infection is an **acquired infectious disease with no human genetic cause**, the sections of the research template that concern causal genes, pathogenic variants, inheritance patterns, penetrance, and germline genetics are **not applicable**; the relevant "genetics" is that of the bacterial pathogen and its virulence loci, which are covered under Etiology, Mechanism, and Molecular Profiling. Ten findings were confirmed across 45 reviewed papers; all key claims below are anchored to primary literature with PMIDs and verified abstract quotes.

---

## Key Findings

### F001 — Current pertussis vaccines provide little to no protection against *B. parapertussis*

A systematic review and meta-analysis encompassing **46,533 participants** found no statistically significant protective effect of pertussis vaccination against *B. parapertussis* ([PMID: 38543887](https://pubmed.ncbi.nlm.nih.gov/38543887/)). The mechanistic explanation is straightforward and well supported: acellular vaccines are constructed around *B. pertussis* antigens — chiefly **pertussis toxin (PT)**, which *B. parapertussis* does not express at all — while *B. parapertussis* produces an **O-antigen LPS** that is absent from *B. pertussis*, so there is little antigenic overlap on which cross-immunity could be built. A complementary study developing a recombinant iron-transport protein antigen explicitly concluded that *"New protective antigens are needed to improve the efficacy of current vaccines against both species"* ([PMID: 28857261](https://pubmed.ncbi.nlm.nih.gov/28857261/)). Consistent with the meta-analysis, a large German efficacy trial found the multicomponent DTaP vaccine had at best a weak, non-significant point estimate of efficacy against *B. parapertussis* (31%, 95% CI −10 to 56 for cough ≥7 days) ([PMID: 9417143](https://pubmed.ncbi.nlm.nih.gov/9417143/)). The take-home is that parapertussis is a genuine **vaccine-escape phenotype**, not merely an under-vaccinated population effect.

### F002 — *B. parapertussis* causes clinically significant disease, with higher odds of severe outcomes than *B. pertussis* in older children

A multicentre retrospective, propensity-matched study comparing **2,554 *B. parapertussis* cases with 8,058 *B. pertussis* cases** found that, overall after matching, the odds ratios for hospitalization and critical-care admission in the *B. parapertussis* group were **1.75 (95% CI 1.46–2.10; p < 0.001)** and **1.94 (95% CI 1.28–2.93; p = 0.001)** respectively ([PMID: 41314606](https://pubmed.ncbi.nlm.nih.gov/41314606/)). The age-stratified pattern is important and nuanced: in infants under 1 year the hospitalization OR was *below* 1 (0.69, 95% CI 0.49–0.96), i.e., *B. pertussis* was more severe in the youngest, but in older age bands *B. parapertussis* was associated with markedly higher odds of hospitalization — 1–4 years OR 3.34 (2.27–4.91), 5–17 years OR 4.22 (2.62–6.79), and ≥18 years OR 1.76 (1.06–2.94). This directly refutes the notion that parapertussis is trivially mild across the board. Corroborating case-level evidence comes from a Turkish five-year hospital series in which **2 of 13 *B. parapertussis* patients died**, and the authors noted that *"infections due to B.parapertussis can also be severe and fatal"* and that most *B. parapertussis* patients were vaccinated — reinforcing both severity and vaccine escape ([PMID: 40277262](https://pubmed.ncbi.nlm.nih.gov/40277262/)).

### F003 — Virulence factors are BvgAS-regulated and overlap with *B. pertussis* but lack pertussis toxin

The three classical bordetellae (*B. pertussis*, *B. bronchiseptica*, *B. parapertussis*) produce a **nearly identical set of virulence factors**: adhesins (filamentous hemagglutinin FHA, fimbriae, pertactin) and toxins (the bifunctional adenylate cyclase/hemolysin CyaA, dermonecrotic toxin, tracheal cytotoxin). The abstract of the landmark pathogenesis review lists *"toxins such as a bifunctional adenylate cyclase/hemolysin, dermonecrotic toxin, tracheal cytotoxin, a B. pertussis specific pertussis toxin"* — explicitly flagging PT as *B. pertussis*-specific — and states that *"Expression of nearly all of these virulence factors is positively regulated by the products of the bvgAS locus"* ([PMID: 11689354](https://pubmed.ncbi.nlm.nih.gov/11689354/)). The **BvgAS two-component signal-transduction system** is therefore the master regulator that switches the bacterium between its virulent (Bvg+) and avirulent/environmental (Bvg−) phases. The absence of PT is the central molecular distinction that explains both the milder systemic phenotype (no PT-driven lymphocytosis or islet-activation effects) and the failure of PT-based vaccines.

### F004 — O-antigen LPS is a key immune-evasion/colonization factor unique to *B. parapertussis* (absent in *B. pertussis*)

The **wbm locus** genes assemble the O-antigen in *B. parapertussis* and *B. bronchiseptica* but are **absent in *B. pertussis***. In vitro, *"Complement was not activated or depleted by wild-type bordetellae expressing O antigen, but both Deltawbm mutants activated complement and were highly sensitive to complement-mediated killing"* ([PMID: 12496152](https://pubmed.ncbi.nlm.nih.gov/12496152/)). Critically, the O-antigen is also required for colonization: *"The B. parapertussis Deltawbm mutant was severely defective in colonization of the tracheas and lungs of mice"* (same study). The O-antigen thus performs a **dual immune-evasion + colonization** role and is simultaneously the antigen most responsible for the vaccine gap (since *B. pertussis*-based vaccines contain no O-antigen). A second shared adhesin, **pertactin (PRN)** — an autotransporter that is itself a component of most acellular vaccines — is required to resist neutrophil-mediated clearance: *"PRN plays a critical role in allowing Bordetella to resist neutrophil-mediated clearance"* ([PMID: 20421378](https://pubmed.ncbi.nlm.nih.gov/20421378/)).

### F005 — Two host-associated forms: human (whooping cough) and ovine (chronic non-progressive pneumonia in sheep)

*B. parapertussis* exists as two host-restricted lineages. The **ovine** lineage causes **chronic non-progressive pneumonia** in sheep and lambs and is a veterinary pathogen of economic importance. Intranasal inoculation of mice with ovine isolates *"produced a subacute bronchopneumonia morphologically similar to early lesions of naturally occurring ovine chronic non-progressive pneumonia"* ([PMID: 2918110](https://pubmed.ncbi.nlm.nih.gov/2918110/)), with neutrophil/macrophage infiltration, peribronchiolar lymphoid hyperplasia, and interalveolar septal fibrosis. Electron microscopy identified the cellular targets of tissue damage: *"Electron microscopy showed damage to ciliated cells, type 1 pneumocytes and alveolar macrophages"* ([PMID: 2300709](https://pubmed.ncbi.nlm.nih.gov/2300709/)). Notably, **cell-free culture fluid alone reproduced milder lesions**, implicating secreted toxins in the pathology. Co-infection with *Pasteurella haemolytica* produced synergistically more severe bronchopneumonia ([PMID: 2061424](https://pubmed.ncbi.nlm.nih.gov/2061424/)). Clearance studies showed the organism is cleared faster from trachea (~100% by 48 h) than lung (~55%) ([PMID: 16031626](https://pubmed.ncbi.nlm.nih.gov/16031626/)). The human and ovine lineages are genetically and phenotypically distinct despite the shared species name.

### F006 — Acellular pertussis vaccination and *B. pertussis* co-infection can *facilitate* *B. parapertussis* infection

Two independent animal studies show that immunity or co-infection directed at *B. pertussis* can *help* *B. parapertussis*. In a rodent model, *"aP vaccination helped clear B. pertussis but resulted in an approximately 40-fold increase in B. parapertussis lung colony-forming units (CFUs)"*, with reduced lung inflammatory and neutrophil responses ([PMID: 20200027](https://pubmed.ncbi.nlm.nih.gov/20200027/)). In a mouse co-infection model, *"Infection of the mouse respiratory tract by B. parapertussis was not only enhanced by the presence of B. pertussis, but B. parapertussis significantly outcompeted B. pertussis"* — an enhancement that required pertussis toxin and was reversed by airway macrophage depletion ([PMID: 21707780](https://pubmed.ncbi.nlm.nih.gov/21707780/)). Together these suggest a mechanism whereby PT-mediated suppression of innate immunity, whether from co-infecting *B. pertussis* or (paradoxically) the immune landscape after aP vaccination, creates a permissive environment for the vaccine-escaping species.

### F007 — Parapertussis is on average milder and shorter than pertussis, with measurable incidence

In an Italian acellular-pertussis efficacy cohort of **15,601 children**, 76 *B. parapertussis* infections were diagnosed, giving an incidence of **2.1 laboratory-confirmed parapertussis cases per 1,000 person-years** ([PMID: 9542925](https://pubmed.ncbi.nlm.nih.gov/9542925/)). The same study found that *"Children affected by B. parapertussis infections showed a less severe clinical picture both in the duration of symptoms and in the percentage of patients affected, even when compared with vaccinated children with pertussis"* — and that *B. parapertussis* strains showed high genetic stability across time and geography. Surveillance studies consistently show *B. parapertussis* as a **minority of Bordetella detections**: 0.1% (10/7732) in China ([PMID: 39002934](https://pubmed.ncbi.nlm.nih.gov/39002934/)), ~6% in Tunisia ([PMID: 22313629](https://pubmed.ncbi.nlm.nih.gov/22313629/)), and ~5.9% in a 9-year Tunisian series ([PMID: 30526740](https://pubmed.ncbi.nlm.nih.gov/30526740/)). The "milder on average" finding (F007) and the "higher odds of severe outcome in older children" finding (F002) are not contradictory: the *population average* is milder, but the *conditional* risk given infection in older age groups can be higher than for *B. pertussis*.

### F008 — Clinical phenotype spectrum (applicable to *B. parapertussis*) with HPO terms and frequencies

Because parapertussis is clinically a whooping-cough syndrome, the phenotype spectrum mirrors pertussis, generally attenuated. In a series of 247 children with whooping cough, **paroxysmal cough occurred in 96.4% (238/247)** and **inspiratory whoop in 24.7% (61/247)**, with cyanosis, apnea and suffocation concentrated in infants under 3 months ([PMID: 26757969](https://pubmed.ncbi.nlm.nih.gov/26757969/)). A Taiwan series reported whooping cough 69.6%, post-tussive vomiting 22.2%, cyanosis 59.1%, leukocytosis (WBC ≥15,000) 47.2%, lymphocytosis 44.4%, and complications in 30.4% — of which *"pneumonia was the most common (92.3%)"* ([PMID: 15497010](https://pubmed.ncbi.nlm.nih.gov/15497010/)). Severe complications documented for the syndrome include severe pneumonia, encephalopathy, apnea, pulmonary hypertension, extreme leukocytosis, and seizures ([PMID: 41749225](https://pubmed.ncbi.nlm.nih.gov/41749225/)). **Important nuance:** the marked leukocytosis/lymphocytosis is pertussis-toxin driven and therefore expected to be *less pronounced or absent* in *B. parapertussis*, since it lacks PT.

**Phenotype → HPO mapping:**

| Phenotype | HPO term | Frequency (whooping-cough series) |
|---|---|---|
| Paroxysmal cough | HP:0002102 (Cough) | 96.4% |
| Inspiratory whoop | HP:0031251 (Paroxysmal cough)/whoop | 24.7% |
| Post-tussive vomiting | HP:0002013 (Vomiting) | 22.2% |
| Cyanosis | HP:0000961 (Cyanosis) | 59.1% (series-dependent) |
| Apnea | HP:0002104 (Apnea) | infants <3 mo |
| Pneumonia | HP:0002090 (Pneumonia) | most common complication (92.3% of complications) |
| Leukocytosis | HP:0001974 (Leukocytosis) | 47.2% (PT-driven; less in parapertussis) |
| Lymphocytosis | HP:0100827 (Lymphocytosis) | 44.4% (PT-driven; less in parapertussis) |
| Seizure / encephalopathy | HP:0001250 / HP:0001298 | severe cases |

### F009 — Pathophysiology causal chain: adhesion → adenylate cyclase immune paralysis → TCT/endotoxin-mediated ciliated-cell destruction

The shared virulence factors act in sequence. The **adenylate cyclase toxin (CyaA)** targets CD11b/CD18-expressing innate immune cells — *"targeting innate immune cells which express CD11b/CD18, the cellular receptor of CyaA"* — translocates its catalytic domain into the cytosol where calmodulin activates it to produce supraphysiologic cAMP, causing cell rounding, cytoskeletal remodeling, and inhibition of migration and epithelial repair at concentrations as low as ~0.5 nM ([PMID: 32392246](https://pubmed.ncbi.nlm.nih.gov/32392246/)). **Tracheal cytotoxin (TCT)**, a peptidoglycan-derived glycopeptide, synergizes with **endotoxin (LPS)** to drive iNOS/nitric-oxide production in non-ciliated airway epithelial cells, causing the selective destruction of neighboring **ciliated cells**: *"TCT and endotoxin are both important virulence factors of B. pertussis, combining synergistically to cause the specific epithelial pathology of pertussis"* ([PMID: 11207540](https://pubmed.ncbi.nlm.nih.gov/11207540/)). The ovine data close the loop by showing that *B. parapertussis* **cell-free culture fluid alone** reproduces bronchopneumonia with ciliated-cell and type-1-pneumocyte damage ([PMID: 2300709](https://pubmed.ncbi.nlm.nih.gov/2300709/)), demonstrating that secreted toxins — not just live bacterial invasion — mediate the tissue injury.

### F010 — Diagnosis relies on IS1001 PCR (not anti-PT serology); treatment is macrolides (azithromycin first-line)

Species-specific real-time PCR on nasopharyngeal specimens identifies *B. parapertussis* by the insertion sequence **IS1001**, distinguishing it from *B. pertussis* (IS481+/ptxP+) and *B. holmesii* (hIS1001+): the triplex assay targets *"the insertion sequence IS481 and the pertussis toxin promoter region (ptxP) for B. pertussis, and the insertion sequence IS1001 for B. parapertussis"* and detects ~1 CFU per reaction ([PMID: 20718721](https://pubmed.ncbi.nlm.nih.gov/20718721/); corroborated by [PMID: 21393459](https://pubmed.ncbi.nlm.nih.gov/21393459/), [PMID: 22313629](https://pubmed.ncbi.nlm.nih.gov/22313629/), [PMID: 24586447](https://pubmed.ncbi.nlm.nih.gov/24586447/)). **Anti-pertussis-toxin serology is *B. pertussis*-specific and useless for *B. parapertussis*** because the organism lacks PT. For treatment, susceptibility testing showed *"The most active antibiotic against all strains was azithromycin (MIC90 = 0.06 mg/l)"*, with erythromycin also effective (MIC90 ~0.25 mg/L) and no significant resistance drift between 1968 and 1997–99 isolates ([PMID: 11757403](https://pubmed.ncbi.nlm.nih.gov/11757403/)). Macrolides — **azithromycin first-line** — are therefore the mainstay, mirroring pertussis therapy.

---

## Section-by-Section Disease Characterization

### 1. Disease Information
- **Overview:** Parapertussis is an acute respiratory infection caused by *B. parapertussis*, presenting as a whooping-cough (pertussis-like) illness in humans, generally milder and shorter than classic pertussis. A separate ovine-adapted lineage causes chronic non-progressive pneumonia in sheep.
- **Identifiers:** MONDO:0001353; MeSH "Whooping Cough" / "Bordetella parapertussis"; ICD-10 **A37.1** (Whooping cough due to *Bordetella parapertussis*); ICD-11 **1C12** (Whooping cough) with pathogen specification. NCBI Taxonomy **txid519**. No OMIM/Orphanet entry (not a Mendelian disease).
- **Synonyms:** Parapertussis; *B. parapertussis* whooping cough; parapertussis pertussis-like syndrome.
- **Data source:** Aggregated disease-level resources plus clinical case series and surveillance cohorts (EHR-derived retrospective studies such as PMID 41314606). Not a genetic/EHR-variant resource.

### 2. Etiology
- **Causal factor:** Infectious — the Gram-negative coccobacillus *B. parapertussis* (BvgAS-regulated virulence program; F003). No human genetic cause.
- **Risk factors (environmental/host):** Young age (infants at highest risk of severe outcomes; PMID 41314606), close respiratory contact (household transmission; siblings and mothers as sources, PMID 22313629, PMID 39565788), lack of/incomplete vaccination for *B. pertussis* offers **no protection** here (F001), crowding, and co-circulation of *B. pertussis*. **Human genetic risk/protective factors: not applicable / none established.**
- **Gene–environment interactions:** The key interaction is at the pathogen–host-immunity level: prior *B. pertussis*-directed immunity or co-infection can facilitate *B. parapertussis* (F006). No human GxE evidence.
- **Protective factors:** Whole-cell pertussis vaccines and natural immunity provide partial/uncertain cross-protection at best; O-antigen-based or novel-antigen vaccines (e.g., recombinant iron-transport protein, PMID 28857261; live-attenuated BPZE1, PMID 35196124) are experimental.

### 3. Phenotypes
See **F008** table. Phenotype type: symptoms/signs (paroxysmal cough, whoop, post-tussive vomiting, cyanosis, apnea) and laboratory abnormalities (leukocytosis/lymphocytosis, generally *less* than pertussis due to absent PT). **Onset:** childhood-predominant, all ages affected. **Severity:** mild-to-moderate on average, severe in a minority (F002, F007). **Progression:** self-limited, episodic paroxysms over days–weeks. **QoL impact:** cough paroxysms, sleep disruption, post-tussive vomiting; hospitalization in severe cases.

### 4. Genetic/Molecular Information
**Not applicable in the human-genetic sense** — parapertussis has no causal human genes, pathogenic variants, inheritance pattern, penetrance, or chromosomal abnormalities. The relevant molecular information is **bacterial**:
- **Virulence loci:** *bvgAS* (master regulator), *cyaA* (adenylate cyclase toxin), *fhaB* (FHA), *prn* (pertactin), *fim* (fimbriae), *dnt* (dermonecrotic toxin), *wbm* locus (O-antigen biosynthesis, unique vs *B. pertussis*), TCT (peptidoglycan-derived, released during cell-wall turnover). **Pertussis toxin operon (ptx) is absent/non-functional.**
- **Comparative genomics:** *B. parapertussis* retains functional genes and expresses proteins absent or pseudogenized in *B. pertussis* (proteomic evidence, including O-antigen and stress-resistance/virulence determinants; PMID 31325608). Human *B. parapertussis* strains show high genetic stability (PMID 9542925). The BatB immunoglobulin-binding autotransporter is deleted/truncated in human *B. parapertussis* relative to *B. bronchiseptica* (PMID 18426869).

### 5. Environmental Information
- **Infectious agent:** *B. parapertussis* (NCBI txid519), *B. bronchiseptica* cluster.
- **Transmission:** Respiratory droplets, human-to-human (human lineage); host-restricted ovine lineage in sheep.
- **Environmental/lifestyle factors:** Crowding, close contact; no established toxin/pollution/dietary etiology.

### 6. Mechanism / Pathophysiology — Ordered Causal Chain

```
1. Inhalation of B. parapertussis → deposition on ciliated respiratory epithelium (trachea, bronchi, lung)
        │
2. BvgAS two-component system senses host environment → switches to Bvg+ (virulent) phase
   → transcribes virulence factors (INFERRED to mirror B. pertussis regulation; PMID 11689354)
        │
3. Adhesins (FHA, fimbriae, pertactin) + O-antigen LPS → firm attachment & colonization of ciliated epithelium
   → pertactin resists neutrophil clearance (PMID 20421378); O-antigen resists complement killing (PMID 12496152)
        │        └── BRANCH (immune evasion): O-antigen blocks complement activation/deposition → bacterial survival
        │
4. Adenylate cyclase toxin (CyaA) binds CD11b/CD18 on innate immune cells → delivers catalytic domain
   → calmodulin-activated supraphysiologic cAMP → phagocyte paralysis, impaired migration & epithelial repair (PMID 32392246)
        │
5. Tracheal cytotoxin (TCT) + endotoxin (LPS) synergize → induce iNOS/nitric oxide in non-ciliated epithelial cells
   → selective destruction of neighboring ciliated cells (PMID 11207540)
        │
6. Loss of ciliated cells + mucociliary clearance failure + secreted-toxin injury (reproduced by cell-free fluid; PMID 2300709)
   → airway inflammation, epithelial damage, mucus accumulation
        │
7. Clinical manifestation → paroxysmal cough, whoop, post-tussive vomiting; in severe cases pneumonia,
   apnea (infants), and rare death (PMID 26757969, 15497010, 41314606)
```

- **Upstream drivers:** BvgAS regulation, adhesion, immune evasion (O-antigen, pertactin, CyaA).
- **Downstream effectors:** TCT/LPS-mediated ciliated-cell destruction, inflammation, cough reflex.
- **Key distinction from pertussis:** absence of PT means no PT-driven systemic effects (lymphocytosis, hypoglycemia, histamine sensitization) → milder average phenotype.
- **GO terms:** GO:0009405 (pathogenesis), GO:0044179 (hemolysis in another organism), GO:0052572 (response to host immune response), GO:0006954 (inflammatory response), GO:0071731 (response to nitric oxide). **CL terms:** CL:0000064 (ciliated cell), CL:0002370 (respiratory ciliated epithelial cell), CL:0002062 (type I pneumocyte), CL:0000583 (alveolar macrophage), CL:0000775 (neutrophil).

### 7. Anatomical Structures Affected
- **Primary organs:** Trachea (UBERON:0003126), bronchus (UBERON:0002185), lung (UBERON:0002048), nasopharynx (UBERON:0001728). Respiratory system (UBERON:0001004).
- **Secondary:** Lung parenchyma in pneumonia; rare systemic/CNS effects (encephalopathy — brain, UBERON:0000955).
- **Tissue/cell level:** Respiratory epithelium (epithelial tissue); target cells = ciliated epithelial cells (CL:0000064), type I pneumocytes (CL:0002062), alveolar macrophages (CL:0000583), with neutrophil infiltration.
- **Subcellular:** Cytoplasm (cAMP dysregulation; GO:0005737), plasma membrane receptor CD11b/CD18 (GO:0005886), bacterial outer membrane (O-antigen; GO:0009279).
- **Lateralization:** Bilateral airway involvement.

### 8. Temporal Development
- **Onset:** Any age; childhood-predominant. Incubation ~7–10 days. Acute onset with catarrhal stage → paroxysmal stage → convalescence, generally shorter than pertussis (F007).
- **Progression:** Self-limited, episodic paroxysms; most resolve over weeks. Severe/complicated course in a minority (infants, or older children per F002).
- **Duration:** Self-limited (not chronic in humans). Ovine lineage causes *chronic* non-progressive pneumonia in sheep (F005).
- **Remission:** Spontaneous resolution typical; antibiotics shorten infectivity and may attenuate course if given early.

### 9. Inheritance and Population
- **Inheritance:** **Not applicable** — infectious, not heritable. Penetrance/expressivity/anticipation/founder-effect/carrier-frequency concepts do not apply.
- **Epidemiology:** Incidence ~**2.1 laboratory-confirmed cases per 1,000 person-years** in one pediatric cohort (F007, PMID 9542925). Represents a **minority of Bordetella detections** — 0.1% (China, PMID 39002934) to ~6% (Tunisia, PMID 22313629 / 30526740). Global distribution wherever pertussis circulates.
- **Demographics:** Affects children of all ages; infants at highest risk of severe disease; older children/adults also affected. No strong ethnic predisposition (host-genetic factors not established). Sex ratio not clearly skewed.

### 10. Diagnostics
- **Gold standard:** **Species-specific real-time PCR targeting IS1001** on nasopharyngeal specimens (F010, PMID 20718721). *B. parapertussis* = IS481−/IS1001+/ptxP−.
- **Culture:** Possible on Bordet-Gengou / Regan-Lowe media but low sensitivity.
- **Serology:** **Anti-PT serology is NOT useful** (organism lacks PT).
- **Laboratory:** Leukocytosis/lymphocytosis are typically **less pronounced** than in pertussis (PT-dependent).
- **Imaging:** Chest radiograph for suspected pneumonia complication.
- **Differential diagnosis:** *B. pertussis*, *B. holmesii* (hIS1001+), *B. bronchiseptica*, RSV and other viral respiratory infections (RSV frequently co-tested, PMID 21393459), *Mycoplasma*, chlamydial pneumonitis.

### 11. Outcome / Prognosis
- **Prognosis:** Generally good — most cases self-limited and milder than pertussis (F007).
- **Mortality:** Low but non-zero; deaths reported (e.g., 2/13 in one series, PMID 40277262).
- **Severe outcomes:** Higher odds of hospitalization/ICU than *B. pertussis* in older children (F002); infants at risk of apnea/pneumonia.
- **Complications:** Pneumonia (most common), apnea, rarely encephalopathy/seizures, pulmonary hypertension in severe whooping-cough-syndrome cases (PMID 15497010, 41749225).
- **Prognostic factors:** Young age, comorbidities, extreme leukocytosis, pulmonary hypertension (adverse markers in the broader whooping-cough syndrome).

### 12. Treatment
- **First-line pharmacotherapy:** **Macrolides — azithromycin** (most active, MIC90 ~0.06 mg/L), erythromycin, clarithromycin (F010, PMID 11757403). Trimethoprim-sulfamethoxazole as alternative. NCIT: Azithromycin (C1029), Erythromycin (C376), Clarithromycin (C614).
- **Note on macrolide resistance:** High-level macrolide resistance is well documented in *B. pertussis* in some regions (PMID 33021592); *B. parapertussis* has not shown comparable resistance drift, but β-lactams (e.g., piperacillin) are potential alternatives.
- **Supportive care:** Hydration, respiratory support, oxygen; ICU/mechanical ventilation for severe cases.
- **Advanced/experimental:** Live-attenuated BPZE1 and Bbvac candidates confer cross-protection in models (PMID 35196124, 22814407); recombinant iron-transport-protein antigen protective in mice (PMID 28857261). No gene/cell/RNA therapy applicable.

### 13. Prevention
- **Primary prevention:** **Current pertussis vaccines do NOT reliably prevent parapertussis** (F001). This is the central prevention gap. Whole-cell vaccines may offer marginal cross-protection; acellular vaccines essentially none and may facilitate infection (F006).
- **Novel vaccine strategies:** O-antigen-inclusive or shared-antigen vaccines, live-attenuated BPZE1/Bbvac (Th17/Th1-mediated cross-protection), recombinant iron-transport protein.
- **Secondary/tertiary:** Early PCR diagnosis, macrolide treatment to reduce transmission, isolation of cases, household contact tracing.
- **Public health:** Maternal vaccination protects infants against *B. pertussis* (PMID 29346585) but **not** against *B. parapertussis*; surveillance with species-specific PCR is essential to detect vaccine escape.

### 14. Other Species / Natural Disease
- **Taxonomy:** *B. parapertussis* NCBI **txid519**; *B. bronchiseptica* cluster.
- **Ovine natural disease:** Chronic non-progressive pneumonia in **sheep** (*Ovis aries*, NCBI txid9940) — a distinct host-adapted lineage of veterinary importance (F005). Recapitulated in mice; synergy with *Pasteurella haemolytica* (PMID 2918110, 2300709, 2061424, 16031626).
- **Comparative pathology:** Both human and ovine lineages target ciliated epithelium via shared toxins; ovine disease is chronic/pneumonic rather than the acute cough syndrome of humans.
- **Zoonotic potential:** Human and ovine lineages are host-restricted; no significant documented zoonotic cross-over.

### 15. Model Organisms
- **Mouse** (*Mus musculus*): Primary model — intranasal challenge reproduces colonization, bronchopneumonia (ovine isolates), and the vaccine-facilitation and co-infection phenomena (PMID 2918110, 2300709, 20200027, 21707780, 12496152). Recapitulates ciliated-cell/type-1-pneumocyte damage and colonization defects of Δwbm mutants.
- **Rat:** Rodent bordetellosis model used for aP-vaccination facilitation study (PMID 20200027).
- **Baboon:** Used for pertussis maternal-vaccination studies (PMID 29346585) — relevant to comparative vaccine biology.
- **In vitro:** Epithelial cell invasion assays for CyaA (PMID 32392246); complement-killing assays for O-antigen mutants (PMID 12496152).
- **Recapitulation/limitations:** Mouse models reproduce colonization, tissue tropism, and immune evasion well, but the human paroxysmal-cough/whoop phenotype is not fully modeled; ovine natural disease differs from the human syndrome.

---

## Mechanistic Model / Interpretation

The unifying narrative is that ***B. parapertussis* is a "pertussis-toxin-null, O-antigen-positive" sibling of *B. pertussis***, and these two molecular differences explain nearly its entire distinctive clinical and public-health profile:

| Feature | *B. pertussis* | *B. parapertussis* | Consequence |
|---|---|---|---|
| Pertussis toxin (PT) | **Present** | **Absent** | Milder systemic disease, less lymphocytosis; anti-PT serology & PT-based vaccines useless for parapertussis |
| O-antigen LPS (wbm) | **Absent** | **Present** | Complement resistance + colonization; a vaccine target the current vaccines lack |
| Shared factors (FHA, fimbriae, pertactin, CyaA, TCT, DNT) | Present | Present | Common adhesion / immune-evasion / ciliated-cell-killing mechanism |
| BvgAS regulation | Yes | Yes | Coordinated virulence expression |
| PCR signature | IS481+ / ptxP+ | IS1001+ | Species-specific diagnosis |

The **O-antigen is simultaneously the reason for immune evasion AND the reason for vaccine escape** — an elegant, if unfortunate, convergence. Meanwhile the **absence of PT** softens the systemic disease but does *not* make it benign, because the ciliated-epithelium destruction is driven by TCT + endotoxin + CyaA, all of which *B. parapertussis* retains. The evolutionary corollary (F006) is that PT-directed vaccination, by suppressing *B. pertussis* and its innate-immune-dampening PT, may **open an ecological niche** for the vaccine-escaping *B. parapertussis* — a hypothesis supported by animal facilitation data and consistent with the observed persistence of parapertussis in vaccinated populations.

---

## Evidence Base

| PMID | Paper (abbrev.) | Supports | Evidence type |
|---|---|---|---|
| [38543887](https://pubmed.ncbi.nlm.nih.gov/38543887/) | Pertussis vaccines scarcely protect vs *B. parapertussis* | F001 | Meta-analysis (human) |
| [28857261](https://pubmed.ncbi.nlm.nih.gov/28857261/) | Recombinant iron-transport protein vaccine | F001, F004 | Model organism |
| [41314606](https://pubmed.ncbi.nlm.nih.gov/41314606/) | Clinical outcomes vs *B. pertussis* | F002 | Human retrospective |
| [40277262](https://pubmed.ncbi.nlm.nih.gov/40277262/) | 5-year hospital series (deaths) | F002 | Human case series |
| [11689354](https://pubmed.ncbi.nlm.nih.gov/11689354/) | Mechanisms of Bordetella pathogenesis | F003 | Review |
| [12496152](https://pubmed.ncbi.nlm.nih.gov/12496152/) | Role of O-antigen in respiratory infection | F004 | Model organism / in vitro |
| [20421378](https://pubmed.ncbi.nlm.nih.gov/20421378/) | Pertactin resists neutrophil clearance | F004 | Model organism |
| [2918110](https://pubmed.ncbi.nlm.nih.gov/2918110/) | Ovine pneumonia in mice | F005 | Model organism |
| [2300709](https://pubmed.ncbi.nlm.nih.gov/2300709/) | Cell-free extract pneumonia | F005, F009 | Model organism |
| [20200027](https://pubmed.ncbi.nlm.nih.gov/20200027/) | aP vaccination facilitates *B. parapertussis* | F006 | Model organism |
| [21707780](https://pubmed.ncbi.nlm.nih.gov/21707780/) | *B. pertussis* enhances *B. parapertussis* | F006 | Model organism |
| [9542925](https://pubmed.ncbi.nlm.nih.gov/9542925/) | Epidemiology/clinical/molecular | F007 | Human cohort |
| [26757969](https://pubmed.ncbi.nlm.nih.gov/26757969/) | 247 children whooping cough | F008 | Human case series |
| [15497010](https://pubmed.ncbi.nlm.nih.gov/15497010/) | Taiwan pertussis series | F008 | Human case series |
| [32392246](https://pubmed.ncbi.nlm.nih.gov/32392246/) | CyaA epithelial invasion | F009 | In vitro |
| [11207540](https://pubmed.ncbi.nlm.nih.gov/11207540/) | TCT + endotoxin NO signaling | F009 | In vitro |
| [20718721](https://pubmed.ncbi.nlm.nih.gov/20718721/) | Triplex PCR IS1001 | F010 | Diagnostic |
| [11757403](https://pubmed.ncbi.nlm.nih.gov/11757403/) | Macrolide susceptibility | F010 | In vitro |

Supporting/context papers: PMID 39002934, 22313629, 30526740, 21393459, 24586447 (surveillance/diagnostics); 9417143 (DTaP efficacy); 31325608, 18426869 (comparative proteomics/genomics); 35196124, 22814407 (experimental cross-protective vaccines); 29346585 (maternal vaccination); 33021592 (macrolide resistance in *B. pertussis*); 16031626, 2061424 (ovine model).

---

## Limitations and Knowledge Gaps

1. **Not a genetic disease:** Template sections on causal human genes, pathogenic variants, inheritance, penetrance, and germline genetics are inapplicable; the "molecular genetics" here is bacterial.
2. **Much mechanistic data is extrapolated from *B. pertussis*.** CyaA and TCT mechanisms (F009) are best characterized in *B. pertussis*; while the shared-factor evidence (F003) and cell-free-fluid ovine data (F005/F009) make extrapolation reasonable, *B. parapertussis*-specific quantitative mechanistic data are sparse.
3. **Animal-model reliance:** Vaccine-facilitation and O-antigen findings (F004, F006) are from mouse/rat models; human confirmation of the facilitation phenomenon is lacking.
4. **Underdiagnosis:** Because many labs use IS481-only PCR or anti-PT serology, *B. parapertussis* is likely under-detected, biasing incidence estimates downward.
5. **Severity heterogeneity:** The apparent contradiction between "milder on average" (F007) and "higher odds of severe outcome in older children" (F002) needs prospective, age-stratified study to resolve confounders (testing bias, comorbidity).
6. **No human genetic susceptibility/protective factors** have been established.

## Proposed Follow-up Experiments / Actions

1. **Prospective, species-specific surveillance** using triplex IS481/ptxP/IS1001 PCR to obtain unbiased incidence and severity estimates across age strata, resolving the F002/F007 tension.
2. **Human immuno-epidemiology of vaccine facilitation:** test whether aP-vaccinated individuals show altered susceptibility to *B. parapertussis* (F006), currently shown only in rodents.
3. **O-antigen-based or shared-antigen vaccine development** (building on PMID 28857261, 35196124) with head-to-head cross-protection testing against both species.
4. ***B. parapertussis*-specific mechanistic studies** of CyaA and TCT-mediated ciliated-cell killing to confirm extrapolations from *B. pertussis* (F009).
5. **Genomic monitoring** of human *B. parapertussis* lineages for antigenic/antibiotic-resistance drift (baseline: high stability, PMID 9542925; no macrolide drift, PMID 11757403).
6. **Clinical guidance update** emphasizing that anti-PT serology cannot diagnose parapertussis and that macrolide (azithromycin) therapy plus IS1001 PCR is the correct standard.

---

*Report compiled from 10 confirmed findings across 45 reviewed papers. Evidence types are labeled human clinical, model organism, in vitro, or review throughout. This disease is an acquired bacterial infection; human-genetic, inheritance, and germline sections are not applicable and are marked as such.*


## Artifacts

- [OpenScientist final report](Bordetella_Parapertussis_Infectious_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Bordetella_Parapertussis_Infectious_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 33 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 33 |
| On topic | 28 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 19 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002102` (1 mention) - the report calls it "Cough"; HP calls it **Pleuritis**
- `HP:0031251` (1 mention) - the report calls it "Paroxysmal cough"; HP calls it **Abnormal subclavian artery morphology**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0009405` (obsolete pathogenesis) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001974` (1 mention) - the report calls it "Leukocytosis"; HP calls it **Increased total leukocyte count**, and lists "Leukocytosis" among its other names
- `HP:0100827` (1 mention) - the report calls it "Lymphocytosis"; HP calls it **Increased total lymphocyte count**, and lists "Lymphocytosis" among its other names
- `GO:0009405` (1 mention) - the report calls it "pathogenesis"; GO calls it **obsolete pathogenesis**
- `CL:0002370` (1 mention) - the report calls it "respiratory ciliated epithelial cell"; CL calls it **respiratory tract goblet cell**, and lists "respiratory goblet cell" among its other names
- `CL:0002062` (2 mentions) - the report calls it "type I pneumocyte"; CL calls it **pulmonary alveolar type 1 cell**, and lists "type I pneumocyte" among its other names
- `UBERON:0003126` (1 mention) - the report calls it "Primary organs:** Trachea"; UBERON calls it **trachea**, and lists "cartilaginous trachea" among its other names