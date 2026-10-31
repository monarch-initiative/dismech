---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-19T04:21:54.391617'
end_time: '2026-10-19T04:39:28.221776'
duration_seconds: 1053.83
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Intellectual Developmental Disorder With Muscle Tone Abnormalities
    And Distal Skeletal Defects
  mondo_id: MONDO:0859277
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
citation_count: 11
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 12
  on_topic: 6
  validator_version: 0.3.0
term_validation:
  total_terms: 37
  verified: 34
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 23
  labels_matching: 20
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0859277
    reported_labels:
    - MONDO
    ontology_label: intellectual developmental disorder with muscle tone abnormalities
      and distal skeletal defects
  labels_variant: 2
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  unresolvable_prefixes:
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Intellectual_Developmental_Disorder_With_Muscle_Tone_Abnormalities_And_Distal_Skeletal_Defects-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Intellectual_Developmental_Disorder_With_Muscle_Tone_Abnormalities_And_Distal_Skeletal_Defects-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Developmental Disorder With Muscle Tone Abnormalities And Distal Skeletal Defects
- **MONDO ID:** MONDO:0859277 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Developmental Disorder With Muscle Tone Abnormalities And Distal Skeletal Defects** covering all of the
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

# Intellectual Developmental Disorder With Muscle Tone Abnormalities And Distal Skeletal Defects (IDDMTAD)

**Disease identifiers:** OMIM #620007 · MONDO:0859277 · MedGen/UMLS C5774199
**Causal gene:** *LGI3* (HGNC:18711; 8p21.3; ENSG00000168481; UniProt Q8N145)
**Inheritance:** Autosomal recessive (biallelic loss-of-function)
**Category:** Mendelian, ultra-rare neurodevelopmental / peripheral-nerve disorder

---

## Summary

Intellectual developmental disorder with muscle tone abnormalities and distal skeletal defects (IDDMTAD) is an ultra-rare, autosomal recessive neurodevelopmental disorder defined in 2022 by Marafi and colleagues, who identified 16 affected individuals from 8 unrelated, largely consanguineous families carrying **biallelic loss-of-function variants in *LGI3*** ([PMID: 35948005](https://pubmed.ncbi.nlm.nih.gov/35948005/)). The disorder couples global developmental delay and intellectual disability with a distinctive **peripheral nerve hyperexcitability syndrome (PNHS)**—visible facial myokymia, tongue fasciculations, diminished reflexes, and abnormal electromyography—together with abnormal muscle tone (axial and appendicular hypotonia) and distal skeletal deformities (hip dysplasia, pectus carinatum, kyphosis, short stature).

The mechanistic core of the disease is now well understood at the molecular level. *LGI3* encodes a **secreted leucine-rich-repeat / EPTP (epitempin) adaptor protein** that binds the axonal receptor **ADAM23** and, through this interaction, clusters **Shaker-type Kv1 (KCNA) potassium channels** at the **juxtaparanode** of myelinated axons. Loss of LGI3 removes the ligand that organizes this channel platform: *Lgi3*-null mice show reduced and mislocalized Kv1 channel complexes in myelinated peripheral axons, and LGI3 secreted from oligodendrocytes in the CNS is required for juxtaparanodal clustering of ADAM23 and Kv1 and for Kv1-mediated short-term synaptic plasticity ([PMID: 35948005](https://pubmed.ncbi.nlm.nih.gov/35948005/); [PMID: 38194969](https://pubmed.ncbi.nlm.nih.gov/38194969/); [PMID: 36828548](https://pubmed.ncbi.nlm.nih.gov/36828548/)). IDDMTAD is therefore best classified as an **LGI3-ADAM23-Kv1 channelopathy** spanning both the central and peripheral nervous systems.

This report synthesizes the available human genetic, clinical, and model-organism evidence into a coherent gene→mechanism→phenotype model. Because the disorder was only delineated in 2022 and comprises roughly 16 reported patients worldwide, several sections (natural history, prognosis, treatment, quality of life, prevalence) are necessarily data-sparse and are flagged as such. No disease-specific therapy exists; management is symptomatic (membrane-stabilizing agents, rehabilitation, orthopedic care) with genetic counseling for a 25% sibling recurrence risk.

---

## 1. Disease Information

**Overview.** IDDMTAD is a Mendelian neurodevelopmental disorder characterized by the triad implied in its name: (1) intellectual developmental disorder / global developmental delay, (2) muscle tone abnormalities (predominantly hypotonia, both axial and appendicular), and (3) distal skeletal defects. Superimposed on this is a clinically recognizable **peripheral nerve hyperexcitability** trait—visible facial myokymia, fasciculations, hyporeflexia, and characteristic EMG findings suggesting motor nerve instability ([PMID: 35948005](https://pubmed.ncbi.nlm.nih.gov/35948005/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | #620007 |
| MONDO | MONDO:0859277 |
| MedGen / UMLS | C5774199 |
| Causal gene | *LGI3*, HGNC:18711 |
| Gene locus | 8p21.3 (chr8:22,146,830–22,157,084, GRCh38) |
| Ensembl | ENSG00000168481 |
| UniProt | Q8N145 |
| Orphanet / ICD-10 / ICD-11 / MeSH | No dedicated entry located (ultra-rare, newly described) |

**Synonyms / alternative names.** The disorder is referred to by its OMIM descriptive title (IDDMTAD) and, mechanistically, as an **LGI3-related peripheral nerve hyperexcitability syndrome (PNHS)**. No eponym is in use.

**Information source.** Findings derive from **aggregated disease-level resources** (OMIM, ClinVar, Monarch/HPO) and a single primary research cohort ([PMID: 35948005](https://pubmed.ncbi.nlm.nih.gov/35948005/)) supplemented by mechanistic mouse studies—not from large EHR or registry data.

---

## 2. Etiology

**Disease causal factors.** The disease is **monogenic and genetic**, caused by biallelic (homozygous or compound heterozygous) **loss-of-function variants in *LGI3***. There is no environmental, infectious, or toxic contribution to disease causation. Complete LGI3 deficiency—through nonsense, frameshift, canonical splice-site, or secretion-abolishing missense alleles—is the proximal cause ([PMID: 35948005](https://pubmed.ncbi.nlm.nih.gov/35948005/); [PMID: 38194969](https://pubmed.ncbi.nlm.nih.gov/38194969/)). As the defining study states, the authors *"identified 16 individuals from eight unrelated families with loss-of-function (LoF) bi-allelic variants in LGI3."*

**Genetic risk factors.** The sole established genetic risk factor is carriage of **two loss-of-function *LGI3* alleles**. Consanguinity is the dominant epidemiologic risk context, concentrating homozygous LoF genotypes. gnomAD constraint metrics (pLI ≈ 0, LOEUF ≈ 1.08) show that LoF alleles are **tolerated in the heterozygous state**, confirming that single carriers are unaffected and that the mechanism is strictly recessive.

**Environmental risk factors / protective factors / gene–environment interactions.** None identified or expected for a fully penetrant recessive single-gene disorder. No protective modifier alleles, dietary factors, or GxE interactions have been reported. (Data not available — not applicable.)

---

## 3. Phenotypes

The phenotypic spectrum is drawn from the defining cohort ([PMID: 35948005](https://pubmed.ncbi.nlm.nih.gov/35948005/)) and Monarch/HPO annotations for MONDO:0859277. Features cluster into three domains: **neurodevelopmental**, **peripheral-nerve hyperexcitability**, and **skeletal/growth**.

| Phenotype | HPO term | Domain | Type |
|---|---|---|---|
| Intellectual disability | HP:0001249 | Neurodevelopmental | Cognitive |
| Global developmental delay | HP:0001263 | Neurodevelopmental | Developmental |
| Axial hypotonia | HP:0008936 | Muscle tone | Clinical sign |
| Appendicular hypotonia | HP:0012389 | Muscle tone | Clinical sign |
| Facial myokymia | HP:0000317 | PNHS | Clinical sign |
| Myokymia | HP:0002411 | PNHS | Clinical sign |
| Tongue fasciculations | HP:0001308 | PNHS | Clinical sign |
| Hyporeflexia | HP:0001265 | PNHS | Clinical sign |
| Ataxia | HP:0001251 | Neurological | Clinical sign |
| Hypokinesia | HP:0002375 | Neurological | Clinical sign |
| Progressive microcephaly | HP:0000253 | Neurodevelopmental | Physical |
| Hip dysplasia | HP:0001385 | Skeletal | Physical |
| Pectus carinatum | HP:0000768 | Skeletal | Physical |
| Kyphosis | HP:0002808 | Skeletal | Physical |
| Short stature | HP:0004322 | Growth | Physical |
| Failure to thrive | HP:0001508 | Growth | Physical |
| Narrow mouth | HP:0000160 | Craniofacial | Physical |
| ADHD | HP:0007018 | Behavioral | Behavioral |
| Anxiety | HP:0000739 | Behavioral | Behavioral |
| Eczematoid dermatitis | HP:0000964 | Dermatologic | Physical |

**Phenotype characteristics.** Onset is **congenital to early childhood** (developmental delay and hypotonia apparent in infancy). Severity is **variable but generally moderate**, with intellectual disability present consistently. The PNHS features (facial myokymia, fasciculations) are a distinctive, clinically recognizable marker: the defining report describes *"global developmental delay, intellectual disability, distal deformities with diminished reflexes, visible facial myokymia, and distinctive electromyographic features suggestive of motor nerve instability."* Microcephaly is noted as **progressive**, suggesting a developmental rather than purely static component. Because the cohort is small (~16 individuals), precise per-feature frequencies are not robustly established; features should be regarded as **qualitatively characteristic** rather than quantitatively penetrant.

**Quality-of-life impact.** No formal QoL instruments (EQ-5D, PROMIS, SF-36) have been applied. Impact is inferred to be substantial given intellectual disability, motor/tone abnormalities, feeding difficulties (failure to thrive), and skeletal deformity requiring orthopedic care. (Formal data not available.)

---

## 4. Genetic / Molecular Information

**Causal gene.** *LGI3* (leucine-rich glioma inactivated 3), HGNC:18711, 8p21.3, disease OMIM #620007. The gene encodes a 548-amino-acid secreted glycoprotein (UniProt Q8N145).

**Pathogenic variants.** Disease is caused by **biallelic loss-of-function variants**: nonsense, frameshift, and canonical splice-site alleles that abolish functional, secreted LGI3 ([PMID: 35948005](https://pubmed.ncbi.nlm.nih.gov/35948005/)). ClinVar (accessed 2026; transcript NM_139278.4) lists 225 *LGI3* variant records. Variants explicitly curated under the IDDMTAD disease name include:

| Variant (cDNA) | Protein | Class | Note |
|---|---|---|---|
| c.1495C>T | p.Arg499Ter | Nonsense (LoF) | Curated to IDDMTAD |
| c.425C>T | p.Ser142Leu | Missense | Curated to IDDMTAD |
| c.10_13del | p.Leu4fs | Frameshift (LoF) | Likely pathogenic |

Disease-associated **missense** variants act by a loss-of-function route—**defective secretion** of the mutant protein ([PMID: 38194969](https://pubmed.ncbi.nlm.nih.gov/38194969/))—which reconciles missense alleles with the LoF mechanism and aids ACMG/AMP variant interpretation. Most remaining ClinVar missense entries are **variants of uncertain significance (VUS)**, reflecting the gene's rarity and the fact that single heterozygous alleles are non-pathogenic.

**Allele frequency / constraint.** gnomAD shows LoF is **tolerated in heterozygotes** (pLI ≈ 0, LOEUF ≈ 1.08), consistent with recessive inheritance and unaffected carriers.

**Functional consequence.** **Complete loss of function** (null) — absence or non-secretion of the LGI3 ligand. No gain-of-function or dominant-negative mechanism is implicated.

**Somatic vs germline.** Disease variants are **germline**. (Separately, somatic *LGI3* alterations and expression changes have been described in cancers such as glioma, stomach, and lung—[PMID: 29257304](https://pubmed.ncbi.nlm.nih.gov/29257304/), [PMID: 28579810](https://pubmed.ncbi.nlm.nih.gov/28579810/)—but these are unrelated to IDDMTAD.)

**Modifier genes / epigenetics / chromosomal abnormalities.** No disease modifier genes, epigenetic marks, or large-scale chromosomal rearrangements have been reported for IDDMTAD. (Data not available.)

---

## 5. Environmental Information

Not applicable. IDDMTAD is a fully penetrant monogenic recessive disorder with **no known environmental, lifestyle, or infectious contributors**. The only relevant "environmental" factor is the population-genetic context of **consanguinity**, which raises the probability of homozygous LoF genotypes but is not itself a disease mechanism.

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variant in *LGI3*** (nonsense/frameshift/splice, or secretion-defective missense) **leads to** absence of functional, secreted LGI3 protein. *(Demonstrated — human genetics, [PMID: 35948005](https://pubmed.ncbi.nlm.nih.gov/35948005/).)*
2. Loss of secreted LGI3 **results in** failure of the axonal receptor **ADAM23** to engage its LGI3 ligand. *(Demonstrated — "The function of ADAM23 is critically dependent on its interaction with its extracellular ligands LGI2 and LGI3," [PMID: 36828548](https://pubmed.ncbi.nlm.nih.gov/36828548/).)*
3. Failure of LGI3-ADAM23 engagement **leads to** loss of **juxtaparanodal clustering of Kv1 (KCNA, Shaker-type) potassium channels** in myelinated axons. *(Demonstrated — "Lgi3-null mice showed reduced and mis-localized Kv1 channel complexes in myelinated peripheral axons," [PMID: 35948005](https://pubmed.ncbi.nlm.nih.gov/35948005/); [PMID: 38194969](https://pubmed.ncbi.nlm.nih.gov/38194969/).)*
4. Mislocalized/reduced juxtaparanodal Kv1 **results in** impaired control of the axonal **refractory period** and membrane repolarization, lowering the threshold for repetitive/ectopic firing. *(Demonstrated — Kv1 complexes regulate refractory period and high-frequency burst firing, [PMID: 36828548](https://pubmed.ncbi.nlm.nih.gov/36828548/).)*

   **Branch A — Peripheral nervous system:** axonal hyperexcitability **leads to** the clinical PNHS trait — facial myokymia, tongue fasciculations, abnormal EMG with motor nerve instability, and diminished reflexes. *(Demonstrated/clinically observed, [PMID: 35948005](https://pubmed.ncbi.nlm.nih.gov/35948005/).)*

   **Branch B — Central nervous system:** loss of oligodendrocyte-secreted LGI3 **results in** disrupted juxtaparanodal ADAM23/Kv1 organization and **suppressed Kv1-mediated short-term synaptic plasticity**, which **contributes to** developmental delay, intellectual disability, and hypotonia. *(Demonstrated in mice — "A lack of Lgi3 in mice disrupts juxtaparanodal clustering of ADAM23 and Kv1 channels and suppresses Kv1-channel-mediated short-term synaptic plasticity," [PMID: 38194969](https://pubmed.ncbi.nlm.nih.gov/38194969/); clinical link inferred.)*

   **Branch C — Skeletal:** chronic abnormal neuromuscular activity / tone abnormality **is inferred to lead to** distal skeletal deformities (hip dysplasia, pectus carinatum, kyphosis). *(Inferred — not experimentally demonstrated.)*

### Detail by category

- **Molecular pathways.** The central axis is the **LGI3 → ADAM23 → Kv1 (KCNA) channel-clustering pathway** at the juxtaparanode. ADAM23 is the receptor; Kv1 channels are the downstream effector platform. LGI3 additionally engages intracellular machinery in other contexts (syntaxin-1 / SNARE exocytosis, [PMID: 18760330](https://pubmed.ncbi.nlm.nih.gov/18760330/); Akt-FAK neurite outgrowth, [PMID: 20162351](https://pubmed.ncbi.nlm.nih.gov/20162351/)), but the channelopathy axis is the disease-relevant one.
- **Cellular processes.** Juxtaparanodal membrane-domain organization; regulation of axonal excitability; short-term synaptic plasticity; neuronal exocytosis/neurotransmitter release (LGI3 attenuates Ca²⁺-evoked glutamate release via syntaxin-1, [PMID: 18760330](https://pubmed.ncbi.nlm.nih.gov/18760330/)); neurite outgrowth ([PMID: 20162351](https://pubmed.ncbi.nlm.nih.gov/20162351/)).
- **Protein dysfunction.** Loss of a **secreted LRR/EPTP adaptor**; missense disease alleles cause **defective secretion** (functional null) rather than altered binding ([PMID: 38194969](https://pubmed.ncbi.nlm.nih.gov/38194969/)).
- **Biochemical abnormality.** Effective **potassium-channel (Kv1) dysfunction** secondary to mislocalization — a channelopathy by positional failure rather than intrinsic channel mutation.
- **Cell types involved.** Myelinated axons (motor and central neurons), **oligodendrocytes** (CNS source of secreted LGI3), Schwann cells (PNS myelin context). Suggested CL terms: oligodendrocyte (CL:0000128), neuron (CL:0000540), myelinating Schwann cell (CL:0002573).
- **Suggested GO terms.** Potassium ion transmembrane transport (GO:0071805); regulation of membrane potential (GO:0042391); protein localization to juxtaparanode region of axon (GO:0071205); regulation of short-term neuronal synaptic plasticity (GO:0048172); regulation of neurotransmitter secretion (GO:0046928).

---

## 7. Anatomical Structures Affected

- **Organ / system level.** Primary involvement of the **nervous system** — both **peripheral nerves** (UBERON:0000010) and **central nervous system / brain** (UBERON:0000955). Secondary involvement of the **musculoskeletal system** (skeletal deformity, hypotonia affecting muscle) and growth (short stature, failure to thrive). Craniofacial (narrow mouth) and skin (eczematoid dermatitis) features occur.
- **Tissue / cell level.** **Nervous tissue** — myelinated axons and their glial partners (oligodendrocytes in CNS; Schwann cells in PNS). Skeletal and muscle tissue are affected secondarily.
- **Subcellular level.** The disease localizes to the **juxtaparanode of the myelinated axon** — a specialized plasma-membrane microdomain. LGI3 is **secreted** and also found in **synaptic vesicle / synaptosome / synapse** and **axon (cell projection)** compartments (UniProt Q8N145). Suggested GO cellular-component terms: juxtaparanode region of axon (GO:0044224); extracellular space (GO:0005615); axon (GO:0030424); synapse (GO:0045202).
- **Localization / lateralization.** Involvement is **bilateral and symmetric** (consistent with a systemic genetic channelopathy). Facial myokymia and fasciculations reflect cranial/peripheral motor nerve involvement.

---

## 8. Temporal Development

- **Onset.** **Congenital to early childhood.** Developmental delay and hypotonia are evident in infancy; PNHS features (myokymia, fasciculations) are recognizable in early childhood.
- **Onset pattern.** **Chronic / insidious**, constitutional from birth.
- **Progression.** Largely **static-to-slowly-evolving** neurodevelopmental course; **microcephaly is described as progressive**, and skeletal deformities may evolve with growth. No relapsing-remitting or episodic pattern is reported.
- **Disease duration.** **Chronic, lifelong.**
- **Remission / critical periods.** No spontaneous remission. Early developmental intervention (physical, occupational, speech therapy) during infancy and early childhood represents the principal window of therapeutic opportunity. (Natural-history data are limited by cohort size.)

---

## 9. Inheritance and Population

- **Inheritance pattern.** **Autosomal recessive.** Heterozygous carriers are unaffected (gnomAD LoF-tolerant, pLI ≈ 0).
- **Penetrance / expressivity.** Presumed **complete penetrance** in biallelic LoF genotypes; **expressivity is variable** across the cohort.
- **Epidemiology.** **Ultra-rare.** The defining cohort was 16 individuals from 8 families ([PMID: 35948005](https://pubmed.ncbi.nlm.nih.gov/35948005/)); only ~16 individuals are reported worldwide as of 2022. No formal prevalence/incidence estimate exists; the disorder falls far below Orphanet's ultra-rare threshold (<1/1,000,000).
- **Consanguinity / founder effects.** **Consanguinity is a major contributor**, concentrating homozygous LoF alleles; author affiliations span Kuwait, Saudi Arabia, Iraq, Jordan, Japan, France, and Germany, indicating **multi-ethnic occurrence with enrichment in Middle Eastern consanguineous populations**. No specific founder variant has been established.
- **Sex ratio.** No sex bias expected or reported (autosomal gene); **both sexes affected**.
- **Carrier frequency.** Not formally estimated; expected to be very low outside consanguineous pedigrees.

---

## 10. Diagnostics

- **Primary diagnostic modality.** **Molecular genetic testing** — identification of biallelic LoF *LGI3* variants. Given the ultra-rarity and non-specific presentation, **exome (WES) or genome (WGS) sequencing** is the most effective route; *LGI3* is unlikely to appear on older targeted intellectual-disability panels, though it should be captured by comprehensive neurodevelopmental panels. **Single-gene testing** is appropriate once the diagnosis is suspected or to confirm segregation in families.
- **Electrophysiology.** **EMG is clinically informative** — showing myokymic discharges and features of motor nerve instability consistent with peripheral nerve hyperexcitability ([PMID: 35948005](https://pubmed.ncbi.nlm.nih.gov/35948005/)). Nerve conduction studies and EMG help distinguish PNHS from other causes of hypotonia/weakness.
- **Clinical recognition.** The **combination of developmental delay/ID + visible facial myokymia + fasciculations + diminished reflexes + distal skeletal deformity** constitutes a potentially recognizable clinical "gestalt."
- **Imaging.** Skeletal radiographs document distal deformities (hip dysplasia, pectus, kyphosis); brain MRI may show microcephaly-associated changes. (No pathognomonic neuroimaging signature reported.)
- **Biomarkers / lab tests / biopsy.** No specific biochemical biomarker, blood test, or histopathologic finding is established. (Data not available.)
- **Differential diagnosis.** Other autosomal recessive neurodevelopmental disorders with hypotonia and skeletal involvement; hereditary peripheral nerve hyperexcitability syndromes (e.g., *KCNA1*-related neuromyotonia); and syndromic ID with distal skeletal anomalies (e.g., KDM6B-related NDD, [PMID: 37196654](https://pubmed.ncbi.nlm.nih.gov/37196654/); acromesomelic and acrodysostosis-spectrum dysplasias, [PMID: 33288834](https://pubmed.ncbi.nlm.nih.gov/33288834/), [PMID: 32783359](https://pubmed.ncbi.nlm.nih.gov/32783359/)). The presence of **myokymia/fasciculations + biallelic *LGI3* LoF** distinguishes IDDMTAD.
- **Screening.** No population newborn screening exists. **Cascade carrier testing** within affected consanguineous families and **prenatal/preimplantation genetic testing** are feasible once the familial variant is known.

---

## 11. Outcome / Prognosis

Formal survival, mortality, and standardized outcome data are **not available** for this newly described, ultra-rare disorder. Based on the reported cohort:

- **Survival / life expectancy.** No evidence of markedly shortened survival is reported; the disorder appears compatible with survival into at least childhood/adolescence, though long-term data are lacking.
- **Morbidity / disability.** Substantial — intellectual disability, motor and tone abnormalities, feeding difficulties (failure to thrive), and skeletal deformity collectively impose significant lifelong functional impairment.
- **Disease course.** Chronic and non-remitting; progressive microcephaly and evolving skeletal deformity are noted.
- **Prognostic factors / biomarkers.** None validated. (Data not available.)

---

## 12. Treatment

**There is no disease-specific or curative therapy.** Management is **symptomatic and multidisciplinary**:

- **Pharmacotherapy (symptomatic).** For peripheral nerve hyperexcitability (myokymia, fasciculations, cramps), **membrane-stabilizing agents / sodium-channel-blocking anticonvulsants** (e.g., carbamazepine class) are the rational symptomatic choice by analogy to other peripheral-nerve-hyperexcitability syndromes; efficacy in IDDMTAD specifically is **not established in trials**. (NCIT: Anticonvulsant Agent.)
- **Rehabilitation.** Physical therapy, occupational therapy, and speech/language therapy for developmental delay, hypotonia, and motor function (NCIT: Physical Therapy; Occupational Therapy; Speech Therapy).
- **Orthopedic / surgical.** Management of hip dysplasia, pectus carinatum, and kyphosis as clinically indicated.
- **Supportive care.** Nutritional support for failure to thrive; behavioral/psychiatric support for ADHD and anxiety.
- **Advanced / experimental therapeutics.** No gene therapy, RNA-based therapy, or targeted therapy exists or is in trials for IDDMTAD. The recessive LoF mechanism makes **gene replacement** a theoretically rational long-term strategy, but no program has been reported. (Data not available.)
- **Pharmacogenomics.** Not applicable/none reported.

---

## 13. Prevention

- **Primary prevention.** Not applicable (genetic disorder). The principal preventive lever is **genetic counseling and reproductive planning** in at-risk/consanguineous families.
- **Genetic counseling.** Autosomal recessive inheritance confers a **25% recurrence risk** for siblings of an affected child. Carrier testing of parents and at-risk relatives, and **prenatal or preimplantation genetic testing** once the familial *LGI3* variants are known, are the available preventive options.
- **Secondary / tertiary prevention.** Early developmental intervention and surveillance for skeletal, feeding, and behavioral complications to mitigate morbidity.
- **Public-health note.** In populations with high consanguinity, community genetic education and premarital/preconception carrier screening programs are the relevant public-health context.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs.** *LGI3* is **highly conserved in mammals** ([PMID: 29257304](https://pubmed.ncbi.nlm.nih.gov/29257304/)). Mouse ortholog *Lgi3* (NCBI Taxon:10090; NCBI Gene 56839).
- **Natural disease in other species.** **No naturally occurring *LGI3* disease** in companion animals or wildlife has been reported (no OMIA entry for *LGI3*).
- **Comparative biology — LGI family.** The broader **LGI family (LGI1–4) exerts conserved roles in synaptic transmission and neuronal excitability**, and family dysfunction causes hyperexcitability/epilepsy disorders across species: *LGI1* mutation causes autosomal dominant lateral temporal lobe epilepsy in humans (and autoimmune anti-LGI1 limbic encephalitis in humans and cats), and ***LGI2* mutation causes benign familial juvenile epilepsy in Lagotto Romagnolo dogs* ("The LGI2 mutation was identified in benign familial juvenile epilepsy in Lagotto Romagnolo (LR) dogs") ([PMID: 26032921](https://pubmed.ncbi.nlm.nih.gov/26032921/)). These natural animal diseases support the evolutionary conservation of the LGI-ADAM-Kv1 excitability axis, even though *LGI3* itself has no reported spontaneous animal disease.
- **Zoonotic / cross-species transmission.** Not applicable (non-communicable genetic disorder).

---

## 15. Model Organisms

- **Mouse models (primary).** Two engineered mouse models underpin the mechanistic understanding:
  1. ***Lgi3*-null (knockout) mice** — recapitulate the **core molecular pathology**, showing *"reduced and mis-localized Kv1 channel complexes in myelinated peripheral axons"* ([PMID: 35948005](https://pubmed.ncbi.nlm.nih.gov/35948005/)).
  2. **Epitope-tagged *Lgi3* knock-in mice** — demonstrated LGI3 is secreted from oligodendrocytes, uses ADAM23 as its receptor, co-assembles with Kv1 channels, and that *Lgi3* loss disrupts juxtaparanodal ADAM23/Kv1 clustering and suppresses Kv1-mediated short-term synaptic plasticity ([PMID: 38194969](https://pubmed.ncbi.nlm.nih.gov/38194969/)).
- **Phenotype recapitulation.** The mouse models faithfully reproduce the **molecular/electrophysiologic** disease mechanism (Kv1 mislocalization, juxtaparanodal disorganization, synaptic plasticity deficit). The extent to which they reproduce the full behavioral/skeletal clinical phenotype is less fully characterized.
- **Model limitations.** Species differences in skeletal development and cognition limit translation of the distal skeletal and intellectual-disability phenotypes; the skeletal branch of the causal chain remains experimentally unverified.
- **Resources.** MGI (mouse *Lgi3*, NCBI Gene 56839). No zebrafish, Drosophila, or iPSC/organoid IDDMTAD models are reported to date.

---

## Mechanistic Model / Interpretation

```
  Biallelic LGI3 LoF (nonsense/frameshift/splice; or secretion-defective missense)
                              │  (DEMONSTRATED — human genetics, PMID 35948005)
                              ▼
          Absence of functional SECRETED LGI3 ligand
                              │  (DEMONSTRATED — defective secretion of missense, PMID 38194969)
                              ▼
        ADAM23 receptor cannot engage its LGI3 ligand
                              │  (DEMONSTRATED — ADAM23 depends on LGI2/LGI3, PMID 36828548)
                              ▼
   Loss of juxtaparanodal clustering of Kv1 (KCNA, Shaker) K+ channels
                              │  (DEMONSTRATED — Lgi3-null mice, PMID 35948005 / 38194969)
                              ▼
   Impaired refractory-period control → axonal hyperexcitability
         │                                    │                          │
   ┌─────┘                          ┌─────────┘                 ┌────────┘
   ▼  BRANCH A (PNS)                ▼  BRANCH B (CNS)            ▼  BRANCH C (skeletal)
 Facial myokymia,            Suppressed Kv1-mediated         Chronic abnormal
 tongue fasciculations,      short-term synaptic             neuromuscular activity
 abnormal EMG, hyporeflexia  plasticity → DD/ID, hypotonia   → distal skeletal defects
   (DEMONSTRATED/clinical)        (mouse-demonstrated;            (INFERRED — not
                                   clinical link inferred)         demonstrated)
```

IDDMTAD is best understood as a **positional channelopathy**: the Kv1 channels themselves are structurally normal, but loss of the LGI3-ADAM23 scaffold means they are no longer concentrated at the juxtaparanode where they normally dampen repetitive firing and set the refractory period. The resulting axonal hyperexcitability explains the peripheral nerve phenotype directly, while loss of the same LGI3-ADAM23-Kv1 machinery in CNS white matter (oligodendrocyte-secreted LGI3) plausibly accounts for the developmental/cognitive and tone phenotypes through impaired synaptic plasticity. The skeletal branch is the weakest link in the chain, resting on inference from chronic abnormal neuromuscular activity rather than direct demonstration. The defining authors summarize this integrated model: *"bi-allelic LoF variants in LGI3 cause a clinically distinguishable disease trait of PNHS, most likely caused by disturbed Kv1 channel distribution in the absence of LGI3"* ([PMID: 35948005](https://pubmed.ncbi.nlm.nih.gov/35948005/)).

---

## Evidence Base

| PMID | Title (abbrev.) | Role | Evidence type |
|---|---|---|---|
| [35948005](https://pubmed.ncbi.nlm.nih.gov/35948005/) | Marafi et al., biallelic LGI3 LoF cohort (AJHG 2022) | **Defining paper** — gene, inheritance, clinical trait, Lgi3-null mouse Kv1 mislocalization | Human clinical + mouse |
| [38194969](https://pubmed.ncbi.nlm.nih.gov/38194969/) | LGI3 from oligodendrocytes clusters ADAM23/Kv1 | Mechanism — CNS LGI3-ADAM23-Kv1 axis; missense secretion defect; synaptic plasticity | Mouse / in vitro |
| [36828548](https://pubmed.ncbi.nlm.nih.gov/36828548/) | LGI3/2-ADAM23 cluster Kv1, regulate refractory period | Mechanism — ADAM23 depends on LGI2/LGI3; Kv1 sets refractory period / burst firing | Mouse / electrophysiology |
| [26032921](https://pubmed.ncbi.nlm.nih.gov/26032921/) | LGI2 benign familial juvenile epilepsy, Lagotto dogs | Comparative biology — natural LGI-family disease across species | Veterinary/natural |
| [12023020](https://pubmed.ncbi.nlm.nih.gov/12023020/) | LGI1 / new LRR subfamily | Protein family domain architecture context | Molecular |
| [29257304](https://pubmed.ncbi.nlm.nih.gov/29257304/) | LGI3 integrative/prognostic analysis | LGI3 secreted, highly conserved in mammals; variant catalog | Computational |
| [18760330](https://pubmed.ncbi.nlm.nih.gov/18760330/) | LGI3 associates with syntaxin-1 | Secondary function — exocytosis regulation | In vitro |
| [20162351](https://pubmed.ncbi.nlm.nih.gov/20162351/) | LGI3 neurite outgrowth via Akt-FAK | Secondary function — neuritogenesis | In vitro |
| [37196654](https://pubmed.ncbi.nlm.nih.gov/37196654/) | KDM6B-related NDD | Differential diagnosis (ID + distal skeletal) | Human clinical |
| [33288834](https://pubmed.ncbi.nlm.nih.gov/33288834/) | Acromesomelic dysplasia (NPR2) | Differential diagnosis (distal skeletal + ID) | Human clinical |

**How the evidence converges.** The disease-defining human genetics ([PMID: 35948005](https://pubmed.ncbi.nlm.nih.gov/35948005/)) and two independent mechanistic mouse studies ([PMID: 38194969](https://pubmed.ncbi.nlm.nih.gov/38194969/), [PMID: 36828548](https://pubmed.ncbi.nlm.nih.gov/36828548/)) agree on a single coherent model—LGI3-ADAM23-Kv1 juxtaparanodal channel clustering—giving unusually strong mechanistic confidence for an ultra-rare disorder. The comparative-biology literature ([PMID: 26032921](https://pubmed.ncbi.nlm.nih.gov/26032921/)) corroborates the conserved role of the LGI family in excitability. No reviewed paper contradicts the core model; the secondary LGI3 functions (syntaxin-1, Akt-FAK) are context-dependent and not clearly disease-driving.

---

## Limitations and Knowledge Gaps

1. **Tiny cohort.** The entire clinical understanding rests on ~16 individuals from 8 families; per-phenotype frequencies, penetrance, expressivity, and natural history are not statistically robust.
2. **Skeletal mechanism unproven.** The link from LGI3 loss/axonal hyperexcitability to distal skeletal defects is **inferred**, not demonstrated. Whether skeletal features are neurogenic, developmental, or reflect an undescribed direct LGI3 role in bone/cartilage is unknown.
3. **CNS-to-cognition link.** The mouse synaptic-plasticity deficit is a plausible but not proven explanation for human intellectual disability.
4. **No prognosis/treatment data.** Survival, long-term outcomes, and any therapeutic efficacy are undocumented; symptomatic treatment recommendations are extrapolated from analogous peripheral-nerve-hyperexcitability syndromes.
5. **No Orphanet/ICD/MeSH coding** yet, reflecting recency.
6. **No biomarker or imaging signature** beyond EMG and genetics.
7. **Model gaps.** Only mouse models exist; no iPSC/organoid, zebrafish, or Drosophila *Lgi3* disease model; skeletal/behavioral recapitulation incompletely characterized.

---

## Proposed Follow-up Experiments / Actions

1. **Expand the patient cohort** via GeneMatcher/Matchmaker Exchange to refine the phenotype spectrum, establish per-feature frequencies, penetrance, and natural history.
2. **Test the skeletal hypothesis** — examine bone/cartilage phenotypes directly in *Lgi3*-null mice (micro-CT, growth-plate histology) and assess *Lgi3* expression in developing skeleton to determine whether skeletal defects are neurogenic or cell-autonomous.
3. **Behavioral/cognitive phenotyping** of *Lgi3*-null mice (learning, memory, motor tasks) to validate the CNS branch linking Kv1/plasticity deficits to intellectual disability.
4. **Deep electrophysiology** in patients and models — quantify refractory period, myokymic discharges, and nerve excitability to establish objective diagnostic/outcome biomarkers.
5. **Functional classification of VUS** — develop a secretion assay (per [PMID: 38194969](https://pubmed.ncbi.nlm.nih.gov/38194969/)) as a routine functional test to reclassify the many *LGI3* missense VUS in ClinVar under ACMG PS3/BS3.
6. **Therapeutic proof-of-concept** — test membrane-stabilizing / Kv-modulating agents, and explore AAV-mediated *LGI3* gene replacement, in *Lgi3*-null mice.
7. **iPSC-derived neuron/oligodendrocyte models** from patients to study juxtaparanodal assembly in a human context.
8. **Obtain formal ontology/disease coding** (Orphanet, ICD-11) and register the disorder to improve ascertainment.

---

*Report compiled from 9 confirmed findings and 16 reviewed papers over a 5-iteration autonomous investigation. Evidence source types are annotated throughout: human clinical, model organism (mouse), in vitro, and computational.*


## Artifacts

- [OpenScientist final report](Intellectual_Developmental_Disorder_With_Muscle_Tone_Abnormalities_And_Distal_Skeletal_Defects-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Intellectual_Developmental_Disorder_With_Muscle_Tone_Abnormalities_And_Distal_Skeletal_Defects-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 12 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 23 |
| Terms named correctly | 20 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859277` (3 mentions) - the report calls it "MONDO"; MONDO calls it **intellectual developmental disorder with muscle tone abnormalities and distal skeletal defects**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000010` (1 mention) - the report calls it "peripheral nerves"; UBERON calls it **peripheral nervous system**
- `UBERON:0000955` (1 mention) - the report calls it "central nervous system / brain"; UBERON calls it **brain**, and lists "suprasegmental levels of nervous system" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.