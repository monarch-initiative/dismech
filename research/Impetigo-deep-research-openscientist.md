---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T10:30:32.491179'
end_time: '2026-09-29T10:46:34.251650'
duration_seconds: 961.76
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Impetigo
  mondo_id: MONDO:0004592
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
citation_count: 31
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 32
  on_topic: 25
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 31
  verified: 30
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 25
  labels_matching: 17
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0001366
    reported_labels:
    - post-streptococcal glomerulonephritis
    ontology_label: splenic sequestration
  - term_id: MONDO:0005295
    reported_labels:
    - rheumatic fever
    ontology_label: intermittent vascular claudication
  - term_id: CHEBI:4508
    reported_labels:
    - dicloxacillin
    ontology_label: diclofenac potassium
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Impetigo-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Impetigo-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Impetigo
- **MONDO ID:** MONDO:0004592 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Impetigo** covering all of the
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

# Impetigo (MONDO:0004592): A Comprehensive Disease Characteristics Report

**Disease:** Impetigo | **MONDO:** MONDO:0004592 | **Category:** Infectious Disease
**Report date:** 2026-09-29 | Evidence base: PubMed primary literature, Cochrane, GBD, clinical guidelines

## Summary

**Impetigo is a common, highly contagious, superficial bacterial infection of the epidermis caused predominantly by *Staphylococcus aureus* and *Streptococcus pyogenes* (group A streptococcus, GAS).** It presents in two clinical forms: nonbullous impetigo (~70% of cases), caused by both *S. aureus* and *S. pyogenes*, and bullous impetigo (~30%), caused specifically by exfoliative-toxin-producing *S. aureus* strains. The disease is diagnosed clinically by its characteristic evolution of erythematous papules into vesicles or bullae over 4–6 days, forming pathognomonic honey-colored crusts. It is an **acquired, non-genetic infectious disease** — there are no causal human genes — although host factors such as skin-barrier and antimicrobial-peptide deficiency (as in atopic dermatitis and filaggrin insufficiency) create a permissive substrate for *S. aureus* colonization and subsequent infection.

Impetigo is overwhelmingly a disease of childhood and of poverty. More than **162 million children** are affected globally at any one time, with a median childhood prevalence of 12.3%, concentrated in tropical, resource-poor, and marginalized communities. The Global Burden of Disease (GBD) 2019 analysis places pyoderma/impetigo as the dominant bacterial skin disease burden (~0.41 million DALYs), with the heaviest impact in low-middle sociodemographic index (SDI) regions. Although usually mild and self-limited, streptococcal impetigo can trigger serious post-infectious sequelae — acute post-streptococcal glomerulonephritis (APSGN) and acute rheumatic fever (ARF) — which occur at the highest documented rates in the world in remote Aboriginal Australian communities.

The mechanistic centerpiece of bullous impetigo (and its severe systemic counterpart, staphylococcal scalded skin syndrome) is the cleavage of **desmoglein-1 (Dsg1)**, a desmosomal keratinocyte adhesion molecule, by glutamate-specific serine protease exfoliative toxins (ETA, ETB, ETD). Removal of the amino-terminal extracellular domains of Dsg1 is sufficient to initiate intraepidermal blister formation. Treatment is stratified by severity: topical antibiotics (mupirocin, retapamulin, ozenoxacin) for limited disease and oral antibiotics (dicloxacillin, cephalexin) for extensive/bullous/outbreak disease. Rising antimicrobial resistance — exemplified by the epidemic European fusidic-acid-resistant impetigo clone (EEFIC) and its emergent mupirocin-resistant variant — is a growing threat. At the community level, ivermectin-based mass drug administration (MDA) for scabies substantially reduces impetigo prevalence and its bacterial complications.

---

## Key Findings

### Finding 1 — Impetigo is a superficial bacterial infection in two clinical forms

Impetigo is a common superficial bacterial infection of the skin with a global disease burden exceeding 140 million cases. It manifests in two forms with distinct proportions and microbiology. **Nonbullous impetigo (~70%)** is caused by both *S. aureus* and *S. pyogenes* (group A streptococcus) and is the classic "school-sores" presentation. **Bullous impetigo (~30%)** is caused exclusively by exfoliative-toxin-producing *S. aureus* strains. Diagnosis is clinical: erythematous papules progress to vesicles or bullae over 4–6 days, ultimately rupturing and drying into the characteristic honey-colored crusts.

> *"Impetigo can be nonbullous (70%) or bullous (30%) and is most commonly caused by group A streptococcus and Staphylococcus aureus."* — [PMID: 41839109](https://pubmed.ncbi.nlm.nih.gov/41839109/)

> *"Impetigo is a common superficial bacterial infection of the skin, with a global disease burden of greater than 140 million."* — [PMID: 33105179](https://pubmed.ncbi.nlm.nih.gov/33105179/)

**Ontology anchors:** MONDO:0004592 (impetigo); ICD-10 L01; ICD-11 1B72; UBERON:0002097 (skin of body), UBERON:0001003 (skin epidermis); NCBITaxon:1280 (*S. aureus*), NCBITaxon:1314 (*S. pyogenes*).

### Finding 2 — Bullous impetigo pathogenesis: exfoliative toxins cleave desmoglein-1

The molecular mechanism of bullous impetigo is now precisely defined. *S. aureus* produces three isoforms of exfoliative toxin — **ETA, ETB, and ETD** — which are **glutamate-specific serine proteases** that cleave a single peptide bond in extracellular domains 3–4 of **desmoglein-1 (Dsg1)**, a desmosomal cell–cell adhesion molecule expressed by keratinocytes in the superficial epidermis. This proteolysis disrupts intercellular adhesion within the granular layer, producing the superficial intraepidermal split characteristic of the disease.

> *"the three isoforms of ETs, i.e., ETA, ETB, and ETD, are glutamate-specific serine proteases that specifically and efficiently cleave a single peptide bond in the extracellular region of human and mouse desmoglein 1 (Dsg1), a desmosomal intercellular adhesion molecule"* — [PMID: 17582744](https://pubmed.ncbi.nlm.nih.gov/17582744/)

Critically, removal of the amino-terminal extracellular domains of Dsg1 is **sufficient** to initiate blister formation, demonstrated as early as 60 minutes after ETA injection in neonatal mice — establishing Dsg1 cleavage as the direct, proximate cause rather than a downstream correlate.

> *"the removal of amino-terminal extracellular domains of Dsg1 by ETs is sufficient to initiate ep[idermal blister formation]"* — [PMID: 20728315](https://pubmed.ncbi.nlm.nih.gov/20728315/)

The toxin genes have distinct genetic bases: **ETA is phage-encoded**, whereas **ETB is plasmid-encoded**, informing strain epidemiology and horizontal transfer of virulence.

> *"ETA is encoded on a phage genome and ETB is enocded on a large plasmid"* — [PMID: 21282415](https://pubmed.ncbi.nlm.nih.gov/21282415/)

The same molecular target (Dsg1) is shared across bullous impetigo, staphylococcal scalded skin syndrome (SSSS, the disseminated toxin-mediated form), and the autoimmune blistering disease pemphigus foliaceus — a striking example of convergent pathology at a single adhesion molecule.

**Ontology anchors:** HGNC gene DSG1 (desmoglein-1); GO:0007156 (homophilic cell adhesion via plasma membrane adhesion molecules), GO:0030057 (desmosome), GO:0008233 (peptidase activity); CL:0000312 (keratinocyte); HP:0008066 (abnormal blistering of the skin).

### Finding 3 — Global burden exceeds 162 million children, concentrated in the tropics and poverty

A systematic review of 89 studies encompassing 145,028 children established a **median childhood prevalence of 12.3% (IQR 4.2–19.4%)**. The burden is highly unequal: low and low-middle income countries showed median prevalences of 8.4–14.5%, but the highest burden was paradoxically in underprivileged children within high-income countries (median 19.4%, IQR 3.9–43.3%). Extrapolating these prevalences yields an estimate of **more than 162 million children affected at any one time**, predominantly in tropical, resource-poor contexts.

> *"we estimate the global population of children suffering from impetigo at any one time to be in excess of 162 million, predominantly in tropical, resource-poor contexts"* — [PMID: 26317533](https://pubmed.ncbi.nlm.nih.gov/26317533/)

> *"Median childhood prevalence was 12·3% (IQR 4·2-19·4%)"* — [PMID: 26317533](https://pubmed.ncbi.nlm.nih.gov/26317533/)

### Finding 4 — Streptococcal impetigo drives post-infectious sequelae (APSGN and ARF)

Group A streptococcal impetigo is not merely a nuisance skin infection; it is an antecedent of serious immune-mediated sequelae. Skin infection with GAS can trigger **acute post-streptococcal glomerulonephritis (APSGN)**, and GAS pharyngitis or impetigo can precede **acute rheumatic fever (ARF)** and its long-term consequence, rheumatic heart disease. In remote Australian Aboriginal communities, the combination of scabies, impetigo, and these post-infectious complications occurs at the highest documented rates in the world.

> *"associated with serious long term sequelae, including invasive infection and post-infectious complications, such as acute post-streptococcal glomerulonephritis and acute rheumatic fever, which occurs at the highest documented rates in the world in remote Aboriginal communities"* — [PMID: 31630410](https://pubmed.ncbi.nlm.nih.gov/31630410/)

> *"Acute rheumatic fever (ARF) is an autoimmune disorder resulting from Group A Streptococcus (GAS) pharyngitis or impetigo in children and adolescents"* — [PMID: 40484016](https://pubmed.ncbi.nlm.nih.gov/40484016/)

**Ontology anchors:** MONDO:0001366 (post-streptococcal glomerulonephritis); MONDO:0005295 (rheumatic fever); HP:0000790 (hematuria), HP:0000093 (proteinuria).

### Finding 5 — Treatment is severity-stratified; topical antibiotics are effective first-line

The evidence base for impetigo treatment is substantial. A Cochrane systematic review incorporated **68 randomized controlled trials with 5,578 participants** reporting on 50 different treatments. Pooled analysis showed topical antibiotics were markedly superior to placebo (**pooled OR 6.49, 95% CI 3.93–10.73**), with topical mupirocin superior to oral erythromycin and no significant difference between mupirocin and fusidic acid.

> *"The total number of included trials was, thus, 68, with 5578 participants, reporting on 50 different treatments"* — [PMID: 22258953](https://pubmed.ncbi.nlm.nih.gov/22258953/)

> *"Topical antibiotics showed better cure rates than placebo (pooled odds ratio (OR) 6.49, 95% confidence interval (CI) 3.93 to 10.73)"* — [PMID: 15106198](https://pubmed.ncbi.nlm.nih.gov/15106198/)

Current guidance recommends **topical mupirocin 2% or retapamulin 1%** for mild nonbullous and bullous disease, reserving oral agents (dicloxacillin, cephalexin) targeting both GAS and *S. aureus* for extensive, bullous, or outbreak disease.

> *"Topical mupirocin 2% ointment or retapamulin 1% ointment are the recommended initial treatments for mild, nonbullous and bullous impetigo."* — [PMID: 41839109](https://pubmed.ncbi.nlm.nih.gov/41839109/)

A newer non-fluorinated quinolone, **ozenoxacin 1% cream**, has demonstrated efficacy in randomized trials with rapid clinical and microbiological response, including activity against both MSSA and MRSA (see Evidence Base).

**Ontology anchors:** NCIT / CHEBI:7025 (mupirocin), retapamulin, ozenoxacin, CHEBI:4508 (dicloxacillin), cephalexin.

### Finding 6 — Ivermectin mass drug administration substantially reduces community impetigo

Because impetigo frequently follows scabies infestation (excoriation breaches the skin barrier), community-level scabies control translates into impetigo reduction. Multiple trials confirm this across settings:

| Setting | Intervention | Key result | PMID |
|---|---|---|---|
| Fiji (cluster RCT, n=2,051) | Ivermectin MDA | Scabies 32.1%→1.9% (RR 94%, 95% CI 83–100); impetigo declined most in ivermectin arm | [26650152](https://pubmed.ncbi.nlm.nih.gov/26650152/) |
| Solomon Islands (AIM trial, Choiseul, ~26,000 people) | Ivermectin + azithromycin MDA | Scabies 18.7%→2.3% (RR 88%), impetigo 24.8%→6.4% (RR 74%) | [30956111](https://pubmed.ncbi.nlm.nih.gov/30956111/) |
| Northern India (single-arm, moderate prevalence) | Ivermectin MDA | Impetigo 1.2%→0.4% (RRR 66.1%, 95% CI 7.0–87); scabies RRR 87.7% | [39431149](https://pubmed.ncbi.nlm.nih.gov/39431149/) |
| Fiji (before-after, n=131,914) | Population MDA | SSTI hospitalisations 17% lower (IRR 0.83, 95% CI 0.74–0.94) | [35345391](https://pubmed.ncbi.nlm.nih.gov/35345391/) |

> *"The prevalence declined from 32.1% to 1.9% in the ivermectin group (relative reduction, 94%; 95% confidence interval [CI], 83 to 100)"* — [PMID: 26650152](https://pubmed.ncbi.nlm.nih.gov/26650152/)

> *"The incidence of hospitalisations with skin and soft tissue infections was 17% lower after the intervention compared to baseline (388 vs 467 per 100,000 person-years; incidence rate ratio 0.83, 95% CI, 0.74 to 0.94"* — [PMID: 35345391](https://pubmed.ncbi.nlm.nih.gov/35345391/)

> *"5 had impetigo (0.4%; relative risk reduction, 66.1%; 95% CI, 7.0%-87[%])"* — [PMID: 39431149](https://pubmed.ncbi.nlm.nih.gov/39431149/)

### Finding 7 — Antimicrobial-resistant *S. aureus* impetigo clones are emerging

Resistance to first-line topical agents is escalating. The **epidemic European fusidic acid-resistant impetigo clone (EEFIC)** persists in Belgium: among community-onset skin/soft-tissue *S. aureus* isolates, 16.2% were fusidic-acid-resistant, of which 48.1% belonged to the EEFIC, disproportionately from young impetigo patients with a late-summer seasonal peak.

> *"Of these, 79 (16.2%) were resistant to fusidic acid, of which 38 (48.1%) belonged to the EEFIC. EEFIC isolates were mostly isolated from young patients with impetigo and showed a seasonal late summer peak."* — [PMID: 37358399](https://pubmed.ncbi.nlm.nih.gov/37358399/)

A **mupirocin-resistant variant** of this clone has since emerged and spread, threatening a second first-line topical agent:

> *"Emergence and spread of a mupirocin-resistant variant of the European epidemic fusidic acid-resistant impetigo clone"* — [PMID: 38726693](https://pubmed.ncbi.nlm.nih.gov/38726693/)

Clones resistant to both mupirocin and fusidic acid and carrying exotoxin genes are increasingly causing skin infections ([PMID: 28592549](https://pubmed.ncbi.nlm.nih.gov/28592549/)), and community MRSA impetigo outbreaks have been reported (e.g., the Netherlands, [PMID: 36695440](https://pubmed.ncbi.nlm.nih.gov/36695440/)).

### Finding 8 — Host skin-barrier and innate-immune dysfunction predispose to impetigo

Impetigo begins with *S. aureus* colonization, which is strongly modulated by host skin integrity. Keratinocytes are the principal epidermal cell orchestrating innate defense against *S. aureus*, which is rarely found on healthy skin but frequently colonizes atopic dermatitis (AD) skin.

> *"Staphylococcus aureus is only rarely found on healthy human skin, but frequently colonizes the skin of atopic dermatitis (AD) patients"* — [PMID: 28655473](https://pubmed.ncbi.nlm.nih.gov/28655473/)

AD promotes colonization through three converging mechanisms — barrier dysfunction, increased extracellular-matrix adhesins, and defective innate immunity from decreased antimicrobial peptides (AMPs):

> *"The mechanisms that allergic skin inflammation of AD promotes the increase of S. aureus colonization include skin barrier dysfunction, increased synthesis of the extracellular matrix adhesins for S. aureus, and defective innate immune responses due to decreased production of endogenous antimicrobial peptides"* — [PMID: 18163223](https://pubmed.ncbi.nlm.nih.gov/18163223/)

The relevant AMPs whose deficiency impairs cutaneous antibacterial defense are named explicitly:

> *"low production of the antimicrobial peptides cathelicidin LL-37 and human β-defensins"* — [PMID: 31836943](https://pubmed.ncbi.nlm.nih.gov/31836943/)

A **filaggrin (FLG) Pro478Ser polymorphism** associates with AD severity and *S. aureus* colonization ([PMID: 27012026](https://pubmed.ncbi.nlm.nih.gov/27012026/)). Clinically, in a series of children with disseminated bullous impetigo, **92% had severe AD** ([PMID: 31755570](https://pubmed.ncbi.nlm.nih.gov/31755570/)) — powerful convergent evidence that barrier compromise is an upstream host-susceptibility axis.

**Ontology anchors:** HGNC gene FLG (filaggrin); CAMP (cathelicidin/LL-37), DEFB (β-defensins); GO:0019730 (antimicrobial humoral response), GO:0061436 (establishment of skin barrier); CL:0000312 (keratinocyte); MONDO:0004980 (atopic dermatitis).

### Finding 9 — GBD 2019: pyoderma/impetigo is the dominant bacterial skin disease burden

The GBD 2019 analysis of bacterial skin diseases (BSD) quantified an age-standardized incidence of **169.72 million [165.28–175.44]** and **0.41 million DALYs [0.33–0.48]**. Of the two main BSD categories, pyoderma causes a significantly heavier burden than cellulitis, with the highest burden in low-middle SDI areas and the lowest in high-middle SDI regions.

> *"Of the two main BSD, pyoderma cause significantly much heavier burden than cellulitis. The highest burden was in the low-middle sociodemographic index (SDI) area"* — [PMID: 35547219](https://pubmed.ncbi.nlm.nih.gov/35547219/)

> *"The age-standardized incidence and age-standardized DALYs rate of BSD are: 169.72 million [165.28-175.44] and 0.41 million [0.33-0.48]"* — [PMID: 35547219](https://pubmed.ncbi.nlm.nih.gov/35547219/)

Trend analysis (1990–2019) shows **rising** age-standardized incidence and mortality rates for pyoderma/impetigo, with burden concentrated in children under 5 and the elderly and inversely related to socioeconomic development ([PMID: 39805883](https://pubmed.ncbi.nlm.nih.gov/39805883/)).

---

## Section-by-Section Report

### 1. Disease Information

Impetigo is a highly contagious, superficial bacterial infection of the epidermis, and one of the most common skin infections of childhood worldwide. **Key identifiers:** MONDO:0004592; ICD-10 **L01** (L01.0 impetigo, L01.1 impetiginization of other dermatoses); ICD-11 **1B72**; MeSH D007169 ("Impetigo"); SNOMED CT 48277006. There is no OMIM entry because impetigo is not a Mendelian genetic disorder, and it is not a rare disease with a dedicated Orphanet entry. **Synonyms/alternative names:** impetigo contagiosa, "school sores," pyoderma (a broader term encompassing impetigo), non-bullous impetigo (impetigo vulgaris/crusted impetigo), bullous impetigo, and ecthyma (the deeper, ulcerative variant). The information in this report is derived from **aggregated disease-level resources** — systematic reviews, GBD modeling, and clinical cohorts — rather than from individual EHR patient records.

### 2. Etiology

**Causal factors:** Impetigo is an **infectious disease** caused by Gram-positive bacteria — predominantly *Staphylococcus aureus* (NCBITaxon:1280) and *Streptococcus pyogenes* (group A streptococcus; NCBITaxon:1314). Bullous impetigo is specifically caused by exfoliative-toxin-producing *S. aureus* (Finding 2).

**Environmental/lifestyle risk factors:** warm humid tropical climate, crowding, poverty, poor hygiene and limited access to water, and — importantly — **antecedent skin trauma or infestation** (scabies, insect bites, minor abrasions, atopic dermatitis) that breaches the epidermal barrier. Young age (2–5 years) is the strongest demographic risk factor. **Genetic risk:** There are no causal or susceptibility loci for impetigo itself; however, host genetic factors influencing barrier and innate immunity — notably **filaggrin (FLG)** loss-of-function and the Pro478Ser polymorphism — modulate *S. aureus* colonization and thereby indirect risk (Finding 8).

**Protective factors:** intact skin barrier, adequate cutaneous antimicrobial peptide production (cathelicidin LL-37, β-defensins), good hygiene, and — at the community scale — scabies control via ivermectin MDA (Finding 6).

**Gene–environment interaction:** The clearest example is filaggrin deficiency (genetic) combined with environmental *S. aureus* exposure and AD inflammation, which together amplify colonization and infection risk (Finding 8, [PMID: 18163223](https://pubmed.ncbi.nlm.nih.gov/18163223/), [PMID: 27012026](https://pubmed.ncbi.nlm.nih.gov/27012026/)).

### 3. Phenotypes

| Phenotype | Type | Characteristics | Suggested HPO |
|---|---|---|---|
| Honey-colored crusted lesions | Clinical sign | Childhood onset; mild-moderate; classic nonbullous form | HP:0011368 (epidermal thickening/crusting); HP:0200042 (skin ulcer) |
| Vesicles/pustules | Physical manifestation | Precede crusting; rupture over 4–6 days | HP:0200037 (vesicle) |
| Flaccid bullae (bullous form) | Physical manifestation | ~30% of cases; Dsg1-mediated; neonates/infants | HP:0008066 (abnormal blistering of the skin) |
| Pruritus | Symptom | Common; promotes autoinoculation/spread | HP:0000989 (pruritus) |
| Regional lymphadenopathy | Clinical sign | More common with streptococcal disease | HP:0002716 (lymphadenopathy) |
| Erythema | Clinical sign | Surrounds lesions | HP:0000988 (skin rash) |

**Onset:** predominantly childhood (peak 2–5 years); neonatal for bullous forms. **Severity:** usually mild and localized; occasionally extensive/disseminated. **Progression:** acute and self-limited over days to a few weeks; episodic recurrences occur with re-exposure. **Quality-of-life impact:** generally modest and transient (discomfort, pruritus, cosmetic and social stigma, school exclusion), but recurrent or disseminated disease and post-infectious sequelae impose substantial morbidity in endemic settings.

### 4. Genetic/Molecular Information

**Impetigo has no causal human genes** — it is an acquired infection, so there are no pathogenic germline variants, modifier genes, or chromosomal abnormalities in the classical Mendelian sense. The relevant molecular players are: (a) the **bacterial virulence genes** — *eta* (phage-encoded), *etb* (plasmid-encoded), and *etd* exfoliative toxin genes of *S. aureus* (Finding 2); and (b) the **host target and susceptibility genes** — **DSG1** (desmoglein-1, the toxin substrate) and barrier/innate-immunity genes **FLG** (filaggrin), **CAMP** (cathelicidin), and *DEFB* (β-defensins) whose deficiency predisposes to colonization (Finding 8). The FLG Pro478Ser polymorphism is a documented modifier of colonization risk ([PMID: 27012026](https://pubmed.ncbi.nlm.nih.gov/27012026/)). Epigenetic and chromosomal-abnormality data are **not applicable** to this infectious disease.

### 5. Environmental Information

**Infectious agents:** *S. aureus* (including MRSA and MSSA) and *S. pyogenes* are the etiologic organisms; the exfoliative-toxin-producing *S. aureus* strains cause bullous disease. **Environmental/lifestyle factors:** heat, humidity, crowding, poor sanitation, and limited water access drive transmission; skin trauma, insect bites, and scabies infestation provide the portal of entry. There is no known role for chemical toxins, radiation, or occupational exposures. Impetigo is transmitted person-to-person by direct contact and via fomites; autoinoculation spreads lesions on the same host.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (bullous impetigo):**

1. Host skin-barrier/innate-immune compromise (e.g., atopic dermatitis, filaggrin deficiency, reduced LL-37/β-defensins) → **permits** *S. aureus* colonization of the skin. *(inferred host-susceptibility step; supported by AD/FLG data)*
2. Breach of the epidermis (trauma, scabies, insect bite) → **allows** bacterial entry and superficial proliferation.
3. Toxigenic *S. aureus* expresses exfoliative toxins ETA/ETB/ETD → **secretes** glutamate-specific serine proteases into the superficial epidermis.
4. Exfoliative toxins cleave a single peptide bond in extracellular domains 3–4 of **desmoglein-1** → **abolish** Dsg1-mediated keratinocyte adhesion in the granular layer.
5. Loss of Dsg1 adhesion → **results in** intraepidermal acantholysis and a superficial blister split (demonstrated: Dsg1 domain removal is sufficient, blistering within 60 min in neonatal mice).
6. Superficial blister roof ruptures → **produces** erosions that dry into honey-colored crusts (clinical manifestation).

**Branch — nonbullous streptococcal impetigo:**

3b. *S. pyogenes* (± *S. aureus*) colonizes traumatized skin → local pyogenic inflammation, pustule and crust formation without Dsg1 cleavage.
4b. In susceptible hosts, nephritogenic GAS strains → **trigger** immune-complex-mediated APSGN; rheumatogenic strains → **can trigger** ARF via molecular mimicry. *(downstream, immune-mediated)*

**Molecular/cellular detail:** The upstream lesion is bacterial colonization gated by host innate immunity (keratinocytes as sensors, [PMID: 28655473](https://pubmed.ncbi.nlm.nih.gov/28655473/)); the proximate mechanism is **proteolytic destruction of a desmosomal adhesion molecule** (protein loss-of-function of Dsg1 via extracellular cleavage). The downstream clinical event is intraepidermal blistering; the downstream systemic events (APSGN, ARF) are host immune responses to streptococcal antigens. **Cell types:** keratinocytes (CL:0000312), neutrophils (CL:0000775). **Biological processes:** GO:0007156 (cell–cell adhesion), GO:0030057 (desmosome), GO:0006508 (proteolysis), GO:0019730 (antimicrobial humoral response), GO:0006954 (inflammatory response). **Subcellular compartments:** desmosome/plasma membrane (GO:0030057), extracellular space (GO:0005615).

### 7. Anatomical Structures Affected

**Primary organ:** skin (UBERON:0002097), specifically the **epidermis** (UBERON:0001003) and its superficial **stratum granulosum**, where Dsg1 is concentrated. **Tissue:** keratinized stratified squamous epithelium. **Cell populations:** keratinocytes (CL:0000312) are the direct target; neutrophils (CL:0000775) infiltrate lesions. **Common sites:** exposed skin — face (especially perioral and perinasal), extremities; bullous disease favors intertriginous areas and, in neonates, the diaper region and trunk. **Lateralization:** typically bilateral/multifocal and asymmetric, spreading by autoinoculation. **Secondary organ involvement:** kidney (glomerulus) in APSGN; heart/joints/CNS in ARF; rarely deeper soft tissue (ecthyma) or systemic (SSSS, sepsis). **Subcellular level:** the desmosome (GO:0030057) at the keratinocyte plasma membrane.

### 8. Temporal Development

**Onset:** acute; predominantly pediatric (peak 2–5 years), neonatal for bullous forms. **Course:** self-limited; individual lesions evolve over 4–6 days and resolve within ~2–3 weeks even without treatment, though treatment shortens the course and reduces spread. **Progression:** usually stable/localized but can be episodic and recurrent with re-exposure; disseminated bullous impetigo occurs in barrier-compromised (AD) children. **Remission:** spontaneous or treatment-induced; complete without scarring in uncomplicated disease. **Critical periods:** early antibiotic treatment prevents dissemination and reduces transmission; treatment does **not** reliably prevent APSGN (a key public-health caveat).

### 9. Inheritance and Population

**Epidemiology:** Median childhood prevalence 12.3% (IQR 4.2–19.4%); >162 million children affected globally at any one time ([PMID: 26317533](https://pubmed.ncbi.nlm.nih.gov/26317533/)); GBD 2019 age-standardized BSD incidence 169.72 million and 0.41 million DALYs, pyoderma-dominant ([PMID: 35547219](https://pubmed.ncbi.nlm.nih.gov/35547219/)). **Inheritance:** not applicable (non-genetic infectious disease); no penetrance/expressivity/anticipation/founder-effect/carrier-frequency parameters apply. **Population demographics:** highest burden in tropical, low-middle-SDI regions and in marginalized populations of high-income countries (e.g., remote Aboriginal Australian communities, [PMID: 31630410](https://pubmed.ncbi.nlm.nih.gov/31630410/)); children under 5 and the elderly are most affected ([PMID: 39805883](https://pubmed.ncbi.nlm.nih.gov/39805883/)). Sex ratio is approximately equal. Geographic and seasonal patterns exist (warm/humid seasons; late-summer peaks for the EEFIC clone).

### 10. Diagnostics

Diagnosis is **primarily clinical**, based on the characteristic honey-colored crusts (nonbullous) or flaccid bullae (bullous) ([PMID: 41839109](https://pubmed.ncbi.nlm.nih.gov/41839109/)). **Laboratory/microbiology:** Gram stain and bacterial culture with antibiotic sensitivity testing are recommended when MRSA is suspected, when disease is recurrent/extensive, or during outbreaks, to guide therapy and detect resistant clones (EEFIC, MRSA). Wound swab of the crust base or bulla fluid is the standard specimen. Anti-DNase B and anti-streptolysin O (ASO) titers can retrospectively confirm streptococcal infection (more reliably anti-DNase B for skin GAS) in suspected APSGN. **Histopathology** (rarely needed): subcorneal/granular-layer split with acantholysis and neutrophils in bullous disease. **Genetic and omics-based diagnostics are not applicable.** **Differential diagnosis:** atopic dermatitis flare (frequently confused — 67% of disseminated bullous impetigo cases were initially misdiagnosed as AD flares, [PMID: 31755570](https://pubmed.ncbi.nlm.nih.gov/31755570/)), herpes simplex/eczema herpeticum, varicella, scabies, contact dermatitis, tinea, and — for bullous forms — SSSS, bullous pemphigoid, and pemphigus foliaceus (which shares the Dsg1 target).

### 11. Outcome / Prognosis

Prognosis is **excellent** for uncomplicated impetigo: self-limited, resolving without scarring, with high cure rates on topical therapy (Finding 5). Direct mortality is very low but non-zero at population scale (GBD records rising age-standardized pyoderma mortality, driven by resource-poor settings and complications, [PMID: 39805883](https://pubmed.ncbi.nlm.nih.gov/39805883/)). **Morbidity** derives chiefly from: (1) transmission and recurrence; (2) local complications — ecthyma, cellulitis, abscess, lymphangitis; and (3) serious post-infectious sequelae — **APSGN and ARF/rheumatic heart disease** — which dominate the long-term burden in endemic communities (Finding 4). **Prognostic factors:** streptococcal (vs staphylococcal-only) etiology raises sequela risk; host barrier compromise (AD) predisposes to dissemination; antimicrobial resistance (EEFIC, MRSA) predicts treatment failure. Quality-of-life impact is generally transient for individuals but substantial cumulatively in high-burden populations.

### 12. Treatment

**Pharmacotherapy — topical (limited disease):** mupirocin 2% (targets *S. aureus* incl. MRSA), retapamulin 1% (pleuromutilin; MSSA and *S. pyogenes*), and ozenoxacin 1% (non-fluorinated quinolone; MSSA, MRSA, *S. pyogenes*) — all superior to vehicle in RCTs (Finding 5; ozenoxacin [PMID: 29898217](https://pubmed.ncbi.nlm.nih.gov/29898217/), [PMID: 25340832](https://pubmed.ncbi.nlm.nih.gov/25340832/), [PMID: 30365584](https://pubmed.ncbi.nlm.nih.gov/30365584/)). Fusidic acid is used outside the US but faces rising resistance. **Oral (extensive/bullous/outbreak disease):** dicloxacillin or cephalexin (cover both GAS and *S. aureus*); cephalosporins are recommended for disseminated bullous impetigo given high clindamycin resistance ([PMID: 31755570](https://pubmed.ncbi.nlm.nih.gov/31755570/)); MRSA-directed agents (e.g., clindamycin, trimethoprim-sulfamethoxazole, doxycycline) per local sensitivities. **Treatment strategy** follows a severity- and resistance-aware algorithm ([PMID: 33538559](https://pubmed.ncbi.nlm.nih.gov/33538559/)): localized disease (<10 lesions, <36 cm²) → topical; widespread/epidemic → oral, guided by local resistance trends. **Advanced/experimental/surgical therapies, pharmacogenomics, and personalized medicine are not applicable** to this common bacterial infection. **Adverse events** are minimal for topical agents (mainly application-site pruritus). **Suggested NCIT anchors:** mupirocin, retapamulin, ozenoxacin, cephalexin, dicloxacillin (antibacterial-agent class terms).

### 13. Prevention

**Primary prevention:** hygiene (handwashing, wound care), reducing crowding, treating predisposing skin conditions (scabies, AD), and — at the community scale — **ivermectin-based MDA for scabies**, which robustly lowers impetigo prevalence and SSTI hospitalisations (Finding 6). **Secondary prevention:** early diagnosis and treatment to limit spread and, in endemic settings, surveillance for APSGN/ARF. **Tertiary prevention:** management of established sequelae (nephritis, rheumatic heart disease). **Public-health interventions:** improved water/sanitation/hygiene (WASH), health education, and integrated NTD control programs. **Immunization:** no impetigo vaccine exists, but a **group A streptococcal vaccine** is in active development and could provide primordial prevention of GAS impetigo and its sequelae ([PMID: 38164699](https://pubmed.ncbi.nlm.nih.gov/38164699/)). Genetic screening/counseling is not applicable.

### 14. Other Species / Natural Disease

Impetigo as clinically defined is a **human disease** (*Homo sapiens*, NCBITaxon:9606). However, the causative organisms and mechanisms have cross-species relevance: exfoliative toxins cleave **both human and mouse Dsg1** ([PMID: 17582744](https://pubmed.ncbi.nlm.nih.gov/17582744/)), and *S. aureus* causes pyoderma and impetigo-like superficial pyoderma in companion animals (dogs, via *Staphylococcus pseudintermedius*), giving veterinary relevance. Orthologous **Dsg1** genes exist across mammals, and the mouse *Dsg1* ortholog underpins neonatal-mouse toxin models (Finding 2). Zoonotic transmission is not a primary feature of human impetigo, though *S. aureus* strains can move between humans and animals.

### 15. Model Organisms

The principal experimental model is the **neonatal mouse** (*Mus musculus*, NCBITaxon:10090), in which subcutaneous or intraperitoneal injection of purified exfoliative toxin (ETA) reproduces the superficial intraepidermal split within ~60 minutes, and Dsg1 domain-removal experiments established sufficiency of Dsg1 cleavage for blistering ([PMID: 20728315](https://pubmed.ncbi.nlm.nih.gov/20728315/), [PMID: 17582744](https://pubmed.ncbi.nlm.nih.gov/17582744/)). This model faithfully recapitulates the **molecular mechanism** of bullous impetigo/SSSS (Dsg1 proteolysis → superficial blister) but does not capture the full contagious, colonization-driven natural history or the streptococcal post-infectious sequelae. Murine AD models (e.g., [PMID: 32438777](https://pubmed.ncbi.nlm.nih.gov/32438777/)) and the EL4 lymphoma model ([PMID: 41795941](https://pubmed.ncbi.nlm.nih.gov/41795941/)) are used to study the barrier-dysfunction/*S. aureus*-colonization axis relevant to impetigo susceptibility. **In vitro** keratinocyte cultures are used to study Dsg1 cleavage and cytokine-driven barrier-protein repression.

---

## Mechanistic Model / Interpretation

```
UPSTREAM (host susceptibility)                     PROXIMATE MECHANISM                    CLINICAL OUTCOME
--------------------------------                   --------------------                    ----------------
Barrier/innate-immune deficit                      Toxigenic S. aureus                     Bullous impetigo
(AD, FLG deficiency, low LL-37/                    secretes ETA/ETB/ETD  ── cleaves ──►    (superficial blisters,
 β-defensins)                                      (glutamate-specific     Dsg1 ECD3-4      honey crusts)
        │                                           serine proteases)          │
        ▼                                                                      ▼
  S. aureus colonization ──► skin breach ──►  ┌── toxigenic S. aureus ──► Dsg1 loss ──► intraepidermal split
  (trauma, scabies,          (portal of       │
   insect bite)               entry)          └── S. pyogenes / non-toxigenic S. aureus
                                                        │
                                                        ▼
                                                  Nonbullous impetigo (pustules, crusts)
                                                        │
                                                        ├──► nephritogenic GAS ──► APSGN
                                                        └──► rheumatogenic GAS ──► ARF / RHD
                                                             (immune-mediated, downstream)
```

The unifying narrative is a two-tier causal architecture. **Tier 1 (host susceptibility, upstream):** the epidermal barrier and cutaneous antimicrobial-peptide system normally exclude *S. aureus*; when these fail — genetically (filaggrin), inflammatorily (atopic dermatitis), or mechanically (scabies, trauma) — colonization and infection follow. **Tier 2 (pathogen effector, proximate):** the pathology diverges by organism. Toxigenic *S. aureus* executes a precise proteolytic attack on a single adhesion molecule (Dsg1) to produce bullae; streptococci and non-toxigenic staphylococci produce nonbullous pyoderma. A distinct **downstream immune tier** converts streptococcal skin infection into systemic sequelae (APSGN, ARF). This model explains why interventions at different tiers all work: barrier/scabies control (upstream, MDA), antibiotics (proximate, killing the organism), and future GAS vaccines (blocking the downstream sequela pathway).

---

## Evidence Base

| PMID | Title (abbrev.) | Role in report |
|---|---|---|
| [41839109](https://pubmed.ncbi.nlm.nih.gov/41839109/) | *Impetigo: Rapid Evidence Review* | Forms/proportions, causative pathogens, first-line topical therapy |
| [33105179](https://pubmed.ncbi.nlm.nih.gov/33105179/) | *Impetigo* | Superficial bacterial etiology, >140M global burden |
| [17582744](https://pubmed.ncbi.nlm.nih.gov/17582744/) | *Staphylococcal exfoliative toxins: "molecular scissors"* | ET isoforms as Dsg1-cleaving serine proteases |
| [20728315](https://pubmed.ncbi.nlm.nih.gov/20728315/) | *Removal of N-terminal Dsg1 domains…* | Dsg1 cleavage is sufficient for blistering |
| [21282415](https://pubmed.ncbi.nlm.nih.gov/21282415/) | *Regulatory mechanism for ET production* | ETA phage-encoded, ETB plasmid-encoded |
| [26317533](https://pubmed.ncbi.nlm.nih.gov/26317533/) | *Global Epidemiology of Impetigo* | 12.3% prevalence, >162M children |
| [31630410](https://pubmed.ncbi.nlm.nih.gov/31630410/) | *Skin infections in Australian Aboriginal children* | APSGN/ARF sequelae, highest documented rates |
| [40484016](https://pubmed.ncbi.nlm.nih.gov/40484016/) | *Acute rheumatic fever* | Impetigo as ARF antecedent |
| [15106198](https://pubmed.ncbi.nlm.nih.gov/15106198/) | *Interventions for impetigo (Cochrane)* | Topical antibiotics OR 6.49 vs placebo |
| [22258953](https://pubmed.ncbi.nlm.nih.gov/22258953/) | *Interventions for impetigo (Cochrane, 68 RCTs)* | Scale of evidence base |
| [26650152](https://pubmed.ncbi.nlm.nih.gov/26650152/) | *MDA for Scabies Control (Fiji)* | Scabies 94% reduction; impetigo declined most |
| [30956111](https://pubmed.ncbi.nlm.nih.gov/30956111/) | *AIM trial (Solomon Islands)* | Large-scale MDA: impetigo 74% reduction |
| [39431149](https://pubmed.ncbi.nlm.nih.gov/39431149/) | *Ivermectin MDA (Northern India)* | Impetigo RRR 66.1% in moderate-prevalence setting |
| [35345391](https://pubmed.ncbi.nlm.nih.gov/35345391/) | *Prevention of bacterial complications (Fiji)* | SSTI hospitalisations 17% lower post-MDA |
| [37358399](https://pubmed.ncbi.nlm.nih.gov/37358399/) | *Persistence of EEFIC (Belgium)* | Fusidic-acid-resistant impetigo clone |
| [38726693](https://pubmed.ncbi.nlm.nih.gov/38726693/) | *Mupirocin-resistant EEFIC variant* | Resistance to second first-line agent |
| [28592549](https://pubmed.ncbi.nlm.nih.gov/28592549/) | *S. aureus clone resistant to mupirocin+fusidic acid* | Dual-resistant exotoxin-carrying clone |
| [28655473](https://pubmed.ncbi.nlm.nih.gov/28655473/) | *Keratinocytes as sensors vs S. aureus* | S. aureus rarely on healthy skin, colonizes AD |
| [18163223](https://pubmed.ncbi.nlm.nih.gov/18163223/) | *Role of bacterial pathogens in AD* | Barrier + adhesin + AMP mechanisms |
| [31836943](https://pubmed.ncbi.nlm.nih.gov/31836943/) | *Eczema Herpeticum* | Names LL-37, β-defensins deficiency |
| [27012026](https://pubmed.ncbi.nlm.nih.gov/27012026/) | *Filaggrin Pro478Ser* | FLG variant ↔ AD severity + S. aureus colonization |
| [31755570](https://pubmed.ncbi.nlm.nih.gov/31755570/) | *Disseminated bullous impetigo + AD* | 92% severe AD; misdiagnosis; cephalosporin recommendation |
| [35547219](https://pubmed.ncbi.nlm.nih.gov/35547219/) | *Global Burden of Bacterial Skin Diseases* | GBD 2019 incidence/DALYs, pyoderma-dominant |
| [39805883](https://pubmed.ncbi.nlm.nih.gov/39805883/) | *Burden of bacterial pyoderma 1990–2019* | Rising ASIR/ASMR, SDI gradient |
| [29898217](https://pubmed.ncbi.nlm.nih.gov/29898217/) | *Ozenoxacin RCT* | Ozenoxacin superior to vehicle |
| [33538559](https://pubmed.ncbi.nlm.nih.gov/33538559/) | *Treatment algorithm* | Resistance-aware localized-vs-widespread algorithm |
| [38164699](https://pubmed.ncbi.nlm.nih.gov/38164699/) | *Streptococcal vaccine development workshop* | GAS vaccine as primordial prevention |

**Evidence source types:** human clinical (systematic reviews, RCTs, cohorts, GBD modeling) dominate; the Dsg1 mechanism is supported by model-organism (neonatal mouse) and in vitro work.

---

## Limitations and Knowledge Gaps

1. **No molecular profiling of impetigo lesions.** Transcriptomic, proteomic, metabolomic, and single-cell data specific to human impetigo lesions were not identified; the mechanistic model relies on toxin biochemistry and AD-colonization literature rather than direct lesional omics.
2. **Prevalence heterogeneity.** The 12.3% median prevalence has a wide IQR (4.2–19.4%) and derives from heterogeneous study designs and diagnostic definitions, limiting precision.
3. **Sequela causation is population-level.** The link from streptococcal impetigo to APSGN/ARF is epidemiologically robust but strain-specific (nephritogenic/rheumatogenic emm types); individual-level predictive markers remain incompletely defined, and antibiotic treatment does not reliably prevent APSGN.
4. **Resistance surveillance is geographically patchy.** EEFIC and MRSA data concentrate in a few high-income countries; the true global resistance landscape (especially in high-burden low-SDI regions) is under-characterized.
5. **Host-susceptibility genetics unproven for impetigo per se.** FLG/AMP associations are established for *S. aureus* colonization and AD, and are inferred (not directly demonstrated) as impetigo risk modifiers.
6. **One treatment claim relies on a related source.** The Cochrane trial-count snippet (PMID 22258953) remained unverified in the knowledge state; the efficacy figure (OR 6.49) rests on the related Cochrane review (PMID 15106198).

---

## Proposed Follow-up Experiments / Actions

1. **Lesional multi-omics:** Perform single-cell RNA-seq and spatial transcriptomics on nonbullous vs bullous impetigo lesions to map keratinocyte, neutrophil, and immune responses and validate the two-tier model directly in human tissue.
2. **Prospective resistance surveillance:** Establish standardized *S. aureus* impetigo isolate surveillance (mupirocin, fusidic acid, retapamulin, ozenoxacin MICs; EEFIC/MRSA genotyping) in high-burden low-SDI settings, not just Europe.
3. **Host-genetics cohort:** Test whether FLG loss-of-function and AMP-gene variants independently predict impetigo incidence (not just colonization) in a prospective pediatric cohort with genotyping.
4. **GAS vaccine impact modeling:** Model the projected reduction in impetigo and downstream APSGN/ARF burden achievable with a group A streptococcal vaccine, integrating GBD and MDA-trial data.
5. **Integrated NTD control trials:** Evaluate combined WASH + ivermectin MDA + targeted topical therapy for durability of impetigo control and sequela reduction in endemic communities, extending the Fiji/Solomon Islands model to larger non-island populations.
6. **Ozenoxacin real-world evidence:** Assess ozenoxacin's role against resistant clones (EEFIC, MRSA) in pragmatic post-marketing studies to define its niche within resistance-aware treatment algorithms.

---

*Report compiled from a 5-iteration autonomous investigation: 9 confirmed findings, 44 papers reviewed. Evidence spans human systematic reviews, RCTs, GBD modeling, and mechanistic model-organism/in vitro studies.*


## Artifacts

- [OpenScientist final report](Impetigo-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Impetigo-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 32 |
| On topic | 25 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 25 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0001366` (1 mention) - the report calls it "post-streptococcal glomerulonephritis"; MONDO calls it **splenic sequestration**
- `MONDO:0005295` (1 mention) - the report calls it "rheumatic fever"; MONDO calls it **intermittent vascular claudication**
- `CHEBI:4508` (1 mention) - the report calls it "dicloxacillin"; CHEBI calls it **diclofenac potassium**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0001003` (2 mentions) - the report calls it "skin epidermis", "epidermis"; UBERON calls it **skin epidermis**, and lists "epidermis" among its other names
- `NCBITaxon:1280` (2 mentions) - the report calls it "S. aureus", "Staphylococcus aureus"; NCBITaxon calls it **Staphylococcus aureus**, and lists "Micrococcus aureus" among its other names
- `NCBITaxon:1314` (2 mentions) - the report calls it "S. pyogenes"; NCBITaxon calls it **Streptococcus pyogenes**
- `GO:0007156` (2 mentions) - the report calls it "homophilic cell adhesion via plasma membrane adhesion molecules", "cell–cell adhesion"; GO calls it **homophilic cell-cell adhesion**
- `HP:0200037` (1 mention) - the report calls it "vesicle"; HP calls it **Skin vesicle**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0001003` - called "skin epidermis", "epidermis"
- `NCBITaxon:1280` - called "S. aureus", "Staphylococcus aureus"
- `GO:0007156` - called "homophilic cell adhesion via plasma membrane adhesion molecules", "cell–cell adhesion"