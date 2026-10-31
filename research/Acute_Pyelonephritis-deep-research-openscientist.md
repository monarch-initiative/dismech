---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T02:48:55.490824'
end_time: '2026-09-30T03:08:45.338528'
duration_seconds: 1189.85
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Acute Pyelonephritis
  mondo_id: MONDO:0003529
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
citation_count: 45
reference_validation:
  total_references: 45
  verified: 45
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 5
  quotes_valid: 4
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:38020186
  relevance_assessed: 45
  on_topic: 17
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 32
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 10
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0001945
    reported_labels:
    - Symptom/sign
    ontology_label: Fever
  - term_id: HP:0032453
    reported_labels:
    - pyuria
    ontology_label: Abnormal lip pigmentation
  - term_id: HP:0000790
    reported_labels:
    - Lab/sign
    ontology_label: Hematuria
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Acute_Pyelonephritis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Acute_Pyelonephritis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Pyelonephritis
- **MONDO ID:** MONDO:0003529 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Acute Pyelonephritis** covering all of the
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

# Acute Pyelonephritis (MONDO:0003529): A Comprehensive Disease Characterization

*Infectious Disease — Disease Knowledge Base Research Report*

---

## Summary

**Acute pyelonephritis (APN) is an acute pyogenic bacterial infection of the renal parenchyma and pelvicalyceal system, overwhelmingly caused by ascending uropathogenic *Escherichia coli* (UPEC).** It is not a Mendelian genetic disease; rather, whether a lower urinary tract infection (UTI) ascends and establishes symptomatic parenchymal kidney infection is determined chiefly by the interplay between bacterial virulence factors and the **host innate immune response**. UPEC adhesins — P-fimbriae binding uroepithelial glycosphingolipids and type 1 pilus FimH binding renal desmoglein-2 (DSG2) — anchor bacteria in the kidney and trigger Toll-like receptor 4 (TLR4)→IRF3 signaling and IL-8/CXCR1-mediated neutrophil recruitment. Neutrophils are the decisive clearance effectors: when this axis is intact, infection is contained (asymptomatic bacteriuria); when it is defective (IRF3 promoter variants, IL-8/*CXCL8* rs4073, low CXCR1 expression), bacteria invade the parenchyma, producing symptomatic pyelonephritis and, potentially, permanent renal scarring.

Clinically, APN presents acutely with fever, flank pain, costovertebral angle tenderness, and pyuria, most often in women (anatomic predisposition) and infants, with a distinctly bimodal and female-predominant epidemiology whose incidence roughly doubled between 2000 and 2018 in population data. Most uncomplicated disease is curable with prompt antibiotics — a landmark trial establishes that **7 days of ciprofloxacin is non-inferior to 14 days** in women — but severe complications (urosepsis, emphysematous pyelonephritis, renal/perinephric abscess, scarring and chronic kidney disease) cluster in patients with diabetes, urinary obstruction, pregnancy, and vesicoureteral reflux (VUR). Rising fluoroquinolone resistance and extended-spectrum β-lactamase (ESBL) production in community *E. coli* now constrain empirical therapy, driving interest in carbapenem-sparing agents (ceftazidime-avibactam) and non-antibiotic prevention.

Prevention is anchored in **screen-and-treat of asymptomatic bacteriuria (ASB) in pregnancy**, source control of obstruction, and evidence-based recurrence prophylaxis — antimicrobial prophylaxis in high-grade VUR (RIVUR trial: 50% reduction), and non-antibiotic options with RCT support including the sublingual vaccine MV140, methenamine hippurate, and vaginal estrogen. Biomarkers such as urinary NGAL (LCN2) and procalcitonin aid diagnosis and predict scarring, while DMSA scintigraphy remains the reference standard for detecting parenchymal involvement. This report synthesizes 13 confirmed findings from 69 reviewed papers into a mechanistic and clinical portrait suitable for populating a structured disease knowledge base.

---

## 1. Disease Information

**Definition.** Acute pyelonephritis is an acute suppurative bacterial infection of the renal parenchyma, tubules, and renal pelvis (upper urinary tract), typically arising by ascent of uropathogens from the bladder. It sits at the severe end of the UTI spectrum, above asymptomatic bacteriuria (ASB) and lower-tract cystitis. It is a form of "complicated" or "febrile" UTI when accompanied by systemic signs.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0003529 (acute pyelonephritis) |
| MeSH | Pyelonephritis (D011704); Pyelonephritis, Xanthogranulomatous (D058489) |
| ICD-10 | N10 (Acute tubulo-interstitial nephritis / acute pyelonephritis); O23.x for pregnancy-associated |
| ICD-11 | GB51 (Acute pyelonephritis) |
| SNOMED CT | 45816000 (Pyelonephritis); acute pyelonephritis subtype |
| OMIM / Orphanet | Not a Mendelian disorder; no dedicated OMIM phenotype MIM. Host susceptibility loci exist (see §4). Not an Orphanet rare disease per se. |

**Synonyms / alternative names.** Acute infective tubulo-interstitial nephritis; upper urinary tract infection; acute febrile UTI; ascending pyelonephritis. Variant/related entities: **emphysematous pyelonephritis (EPN)**, **xanthogranulomatous pyelonephritis (XGP)**, **acute lobar nephronia / acute focal bacterial nephritis (ALN/AFBN)**, **pyonephrosis**, and **perinephric abscess**.

**Data provenance.** Evidence in this report is drawn from **aggregated disease-level resources** — population registries (e.g., a 19-year Danish cohort), prospective clinical cohorts, randomized controlled trials, systematic reviews/meta-analyses, and mechanistic model-organism and in-vitro studies — supplemented by EHR-derived cohort studies. It is not derived from a single individual patient.

---

## 2. Etiology

**Primary cause — infectious.** APN is overwhelmingly bacterial and ascending. **Uropathogenic *E. coli* (UPEC)** is the dominant pathogen. In a US prospective study (2013–2014) of adults with culture-confirmed APN, *E. coli* grew in **86.9% (453/521)** of cases ([PMID: 27532362](https://pubmed.ncbi.nlm.nih.gov/27532362/)). Other uropathogens include *Klebsiella pneumoniae*, *Proteus mirabilis* (associated with struvite/staghorn calculi and XGP), *Enterococcus*, *Pseudomonas*, and, in specific contexts, *Staphylococcus saprophyticus* and *Candida*. Hematogenous seeding (e.g., *Staphylococcus aureus*) is a less common alternative route.

**Risk factors.**

*Environmental / clinical (host):*
- **Female sex** — short urethra and perineal proximity favor ascent. Strong female predominance across all age strata ([PMID: 38020186](https://pubmed.ncbi.nlm.nih.gov/38020186/)).
- **Pregnancy** — ureteral dilation, urinary stasis, and ASB markedly raise ascending-infection risk ([PMID: 41274602](https://pubmed.ncbi.nlm.nih.gov/41274602/)).
- **Diabetes mellitus** — the dominant risk factor for necrotizing/emphysematous forms (63–76% of EPN series) ([PMID: 42221797](https://pubmed.ncbi.nlm.nih.gov/42221797/), [PMID: 41836219](https://pubmed.ncbi.nlm.nih.gov/41836219/)).
- **Urinary obstruction / stones** — present in ~46% of severe EPN ([PMID: 42221797](https://pubmed.ncbi.nlm.nih.gov/42221797/)); staghorn calculi underlie XGP.
- **Vesicoureteral reflux (VUR)** and **bladder-bowel dysfunction (BBD)** — key pediatric risk factors and drivers of scarring ([PMID: 35928985](https://pubmed.ncbi.nlm.nih.gov/35928985/)).
- Infancy/early childhood, instrumentation/catheterization, immunosuppression, prior UTI, and sexual activity.

*Genetic (host susceptibility — not causal Mendelian):*
- **IRF3 promoter polymorphisms** associated with symptomatic kidney infection vs asymptomatic carriage ([PMID: 20886096](https://pubmed.ncbi.nlm.nih.gov/20886096/)).
- **IL-8 / *CXCL8* rs4073 (−251A>T)** associated with pediatric parenchymal renal infection ([PMID: 21042230](https://pubmed.ncbi.nlm.nih.gov/21042230/)).
- Low **CXCR1** expression predisposes to pyelonephritis and scarring ([PMID: 11817650](https://pubmed.ncbi.nlm.nih.gov/11817650/)).

**Protective factors.** Intact innate immunity (functional TLR4→IRF3 and IL-8/CXCR1 neutrophil axis); urinary **neutrophil extracellular traps (NETs)** that block ascension ([PMID: 39321268](https://pubmed.ncbi.nlm.nih.gov/39321268/)); adequate hydration/urine flow; absence of obstruction; and, for recurrence, vaginal estrogen in postmenopausal women and prophylactic strategies (§13). No well-established protective germline variant is defined; conceptually, "high" innate-signaling genotypes are protective.

**Gene–environment interactions.** Host genotype modulates the environmental exposure (bacterial colonization): the same UPEC exposure yields ASB in hosts with robust IRF3/IL-8/CXCR1 signaling but ascending symptomatic pyelonephritis in hosts with attenuated signaling. Diabetes (environmental/metabolic) interacts with tissue susceptibility to produce necrotizing EPN. Androgen status interacts with macrophage polarization to modulate post-infection scarring ([PMID: 32849562](https://pubmed.ncbi.nlm.nih.gov/32849562/)).

---

## 3. Phenotypes

| Phenotype | Type | Suggested HPO | Frequency / notes |
|---|---|---|---|
| Fever | Symptom/sign | HP:0001945 | Very frequent; hallmark of "febrile UTI" |
| Flank / loin pain | Symptom | HP:0030157 (flank pain) | Frequent; often unilateral |
| Costovertebral angle tenderness | Clinical sign | — | Characteristic exam finding |
| Dysuria / urinary frequency / urgency | Symptom | HP:0100518 (dysuria) | Common (lower-tract overlap) |
| Nausea and vomiting | Symptom | HP:0002018 / HP:0002013 | Common, especially children |
| Pyuria (leukocyturia) | Lab abnormality | HP:0032453 (pyuria) | Near-universal; basis of leukocyte-esterase/NET dipstick ([PMID: 39321268](https://pubmed.ncbi.nlm.nih.gov/39321268/)) |
| Bacteriuria | Lab abnormality | HP:0012461 (bacteriuria) | Defining; ≥10⁵ CFU/mL |
| Leukocytosis / elevated CRP, PCT | Lab abnormality | HP:0001974 (leukocytosis) | Systemic inflammation; PCT/uNGAL predict severity/scarring |
| Hematuria | Lab/sign | HP:0000790 | Variable |
| Sepsis / septic shock | Clinical complication | HP:0100806 (sepsis) | ~72% septic shock in ICU EPN cohort ([PMID: 42221797](https://pubmed.ncbi.nlm.nih.gov/42221797/)) |
| Renal scarring | Structural sequela | HP:0000800 region / scarring | Long-term; DMSA-defined |

**Onset / severity / progression.** Onset is **acute** (hours to a few days). Age of onset is **bimodal**: high in infancy (especially girls), then predominant in reproductive-age women, with a further rise in the elderly. Severity is **variable** — from outpatient-manageable uncomplicated APN to fulminant urosepsis. Course is typically **self-limited with treatment**, but delayed therapy (>72 h) increases permanent scarring ([PMID: 27748543](https://pubmed.ncbi.nlm.nih.gov/27748543/)).

**Quality-of-life impact.** Acute APN causes marked short-term morbidity (hospitalization, pain, fever, work loss). Recurrent UTI/pyelonephritis substantially impairs quality of life and drives major antibiotic use ([PMID: 42225392](https://pubmed.ncbi.nlm.nih.gov/42225392/)). Post-pyelonephritic scarring can progress to hypertension and CKD, with lasting functional impact.

---

## 4. Genetic / Molecular Information

APN has **no causal Mendelian gene**; it is a multifactorial infectious disease with host **susceptibility loci** that shift the balance between asymptomatic bacteriuria and symptomatic parenchymal infection.

**Susceptibility genes / variants (host innate immunity):**

| Gene (HGNC) | Variant / feature | Effect | Evidence |
|---|---|---|---|
| **IRF3** | Promoter polymorphism; disease genotype lowers promoter activity | Reduced type I IFN/innate signaling → symptomatic kidney infection | [PMID: 20886096](https://pubmed.ncbi.nlm.nih.gov/20886096/) |
| **CXCL8 (IL-8)** | rs4073 (−251A>T) | Altered neutrophil chemokine signaling → parenchymal renal infection in children | [PMID: 21042230](https://pubmed.ncbi.nlm.nih.gov/21042230/) |
| **CXCR1** | Low receptor expression | Impaired neutrophil clearance → pyelonephritis + scarring | [PMID: 11817650](https://pubmed.ncbi.nlm.nih.gov/11817650/) |
| **TLR4** | Signaling capacity | Modulates mucosal response (high response → symptomatic; low → ASB) | [PMID: 21042230](https://pubmed.ncbi.nlm.nih.gov/21042230/) |

Variant class: regulatory/promoter SNPs and expression-modulating polymorphisms (not protein-truncating). Origin: **germline** host variants (susceptibility), distinct from the **bacterial genome** (virulence). Functional consequence: partial **loss of innate signaling function** predisposing to ascension. In [PMID: 21042230](https://pubmed.ncbi.nlm.nih.gov/21042230/), among TLR4/IL-8/CXCR1/CXCR2 SNPs tested in children with APN/ALN (VUR excluded), "*only IL-8 (rs4073, −251A>T) showed significant differences in genotype and allele frequency between the control and APN or ALN cases.*"

**Bacterial "virulence genotype."** Disease is strongly shaped by the pathogen genome: *fim* (type 1 pili/FimH), *pap* (P-fimbriae), *hly* (α-hemolysin), and siderophore systems. ESBL genes (e.g., *bla*CTX-M) and fluoroquinolone-resistance determinants convert treatable disease into refractory disease ([PMID: 27532362](https://pubmed.ncbi.nlm.nih.gov/27532362/)); ST131-H30Rx clones carry virulence factors linked to recurrence ([PMID: 40926251](https://pubmed.ncbi.nlm.nih.gov/40926251/)).

**Modifier genes / epigenetics / chromosomal abnormalities.** Androgen-responsive pathways modify macrophage polarization and scarring ([PMID: 32849562](https://pubmed.ncbi.nlm.nih.gov/32849562/)). No disease-specific DNA-methylation signature or recurrent chromosomal abnormality is established for APN; CAKUT (congenital anomalies of kidney/urinary tract) predispose anatomically but did not explain the observed incidence rise ([PMID: 38020186](https://pubmed.ncbi.nlm.nih.gov/38020186/)).

---

## 5. Environmental Information

- **Infectious agents (NCBI Taxonomy):** *Escherichia coli* (txid562) — dominant; *Klebsiella pneumoniae* (txid573); *Proteus mirabilis* (txid584); *Enterococcus faecalis* (txid1351); *Pseudomonas aeruginosa* (txid287); *Candida* spp. (fungal, in diabetics/instrumented patients).
- **Environmental/metabolic factors:** Diabetes mellitus and hyperglycemia (tissue substrate for gas-forming necrotizing EPN); urinary catheters/instrumentation (nosocomial exposure); obstruction/stones (stasis).
- **Lifestyle factors:** Sexual activity, spermicide/diaphragm use, inadequate fluid intake, and delayed voiding increase lower-UTI and ascension risk. Increased fluid intake benefits those with low baseline intake ([PMID: 42225392](https://pubmed.ncbi.nlm.nih.gov/42225392/)).
- **Occupational/toxin exposures:** No specific occupational toxin is causally linked; APN is infection-driven.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Periurethral/fecal UPEC colonization** of the introitus/urethra **leads to** bladder colonization (ascending route).
2. Bladder UPEC express **type 1 pili (FimH)** and **P-fimbriae (PapG)**; FimH binds **mannosylated desmoglein-2 (DSG2)** on renal epithelium and P-fimbriae bind uroepithelial glycosphingolipids, which **results in** adhesion and ascent up the ureter to the renal pelvis and collecting ducts (demonstrated in C3H/HeN mice; FimH⁻ mutants cannot establish kidney infection) ([PMID: 33513212](https://pubmed.ncbi.nlm.nih.gov/33513212/)).
3. Adhesion and bacterial products (LPS, hemolysin) **activate TLR4 on tubular/uroepithelial cells**, which **leads to** **IRF3-dependent** innate signaling and **IL-8/CXCL8 secretion** (branch point A) ([PMID: 20886096](https://pubmed.ncbi.nlm.nih.gov/20886096/), [PMID: 21042230](https://pubmed.ncbi.nlm.nih.gov/21042230/)).
4. IL-8 engaging **CXCR1** on neutrophils **results in** massive **neutrophil recruitment** across the uroepithelium into the parenchyma and urine — the decisive effector step ([PMID: 11817650](https://pubmed.ncbi.nlm.nih.gov/11817650/)).
5. **Branch A — effective clearance:** Neutrophils phagocytose bacteria, release granules/ROS, and form **NETs** (also present in healthy urine), which **results in** bacterial containment → **asymptomatic bacteriuria or resolution** and a positive leukocyte dipstick ([PMID: 39321268](https://pubmed.ncbi.nlm.nih.gov/39321268/), [PMID: 42524556](https://pubmed.ncbi.nlm.nih.gov/42524556/)).
6. **Branch B — defective clearance** (low CXCR1, IRF3/IL-8 risk genotypes): impaired neutrophil recruitment/function **leads to** parenchymal bacterial proliferation, abscess formation, and **symptomatic acute pyelonephritis** ([PMID: 11817650](https://pubmed.ncbi.nlm.nih.gov/11817650/), [PMID: 20886096](https://pubmed.ncbi.nlm.nih.gov/20886096/)).
7. Persistent/dysregulated neutrophil activation **results in** collateral tissue injury via **ROS, proteases, S100A8/A9, and NET-associated mediators**, which **leads to** tubulointerstitial damage (double-edged effector) ([PMID: 42524556](https://pubmed.ncbi.nlm.nih.gov/42524556/)).
8. Injury plus **androgen-influenced polarization of activin-A–producing macrophages** **leads to** fibrogenic remodeling and **permanent renal scarring** (post-pyelonephritic scarring) — inferred from mouse models ([PMID: 32849562](https://pubmed.ncbi.nlm.nih.gov/32849562/), [PMID: 42524556](https://pubmed.ncbi.nlm.nih.gov/42524556/)).
9. In **diabetic/obstructed** hosts (branch C), high tissue glucose and impaired perfusion **result in** gas-forming necrotizing infection = **emphysematous pyelonephritis**, which **leads to** sepsis/septic shock and, without source control, death ([PMID: 42221797](https://pubmed.ncbi.nlm.nih.gov/42221797/)).
10. Systemically, bacteremia and cytokine release **result in** SIRS/**urosepsis**; scarring over time **leads to** hypertension and **chronic kidney disease** ([PMID: 40022942](https://pubmed.ncbi.nlm.nih.gov/40022942/)).

### Detail by category

- **Molecular pathways:** TLR4 → MyD88/TRIF → **IRF3** (type I IFN) and NF-κB → IL-8/CXCL8; IL-8–CXCR1/CXCR2 chemotaxis. (Reactome: Toll-like receptor cascades; KEGG hsa04620.)
- **Cellular processes:** Innate inflammation, neutrophil chemotaxis/phagocytosis, NETosis, ROS burst, apoptosis/necrosis of tubular cells, macrophage polarization, fibrosis.
- **Protein dysfunction:** Bacterial FimH lectin domain gains pathogenic function by binding host DSG2; a mannose-binding-pocket mutation abolishes binding ([PMID: 33513212](https://pubmed.ncbi.nlm.nih.gov/33513212/)). Host risk = reduced IRF3 promoter activity / low CXCR1.
- **Immune involvement:** Predominantly **innate** (neutrophils, macrophages, epithelial sensing). Not autoimmune.
- **Tissue-damage mechanisms:** Oxidative stress (ROS), protease-mediated injury, NET-associated cytotoxicity, ischemia (obstruction), necrosis, and fibrogenesis.
- **Molecular profiling:** Biomarkers up in disease include **NGAL/LCN2**, procalcitonin, CRP, and S100A8/A9 (calprotectin). NGAL is itself a bacteriostatic (iron-sequestering) innate effector.

**Suggested ontology terms.** GO biological process: neutrophil chemotaxis (GO:0030593), defense response to bacterium (GO:0042742), Toll-like receptor signaling pathway (GO:0002224), neutrophil extracellular trap formation (GO:0140494), response to lipopolysaccharide (GO:0032496). CL cell types: neutrophil (CL:0000775), macrophage (CL:0000235), kidney collecting duct epithelial cell (CL:1000454), renal proximal tubule epithelial cell (CL:1000838). CHEBI: reactive oxygen species (CHEBI:26523), lipopolysaccharide (CHEBI:16412).

---

## 7. Anatomical Structures Affected

- **Primary organ:** Kidney (UBERON:0002113) — specifically **renal parenchyma/cortex** (UBERON:0001225), **renal medulla** (UBERON:0000362), **renal pelvis** (UBERON:0001224), and **collecting duct** (UBERON:0001232), the principal site of FimH–DSG2 adhesion.
- **Secondary/complications:** Perinephric space (perinephric abscess), ureter (UBERON:0000056), bladder (UBERON:0001255, source), bloodstream (bacteremia/urosepsis). Long-term secondary organ: systemic (sepsis), progression to CKD.
- **Body systems:** Renal/urinary system (primary); cardiovascular/immune (sepsis); reproductive/obstetric (pregnancy-associated).
- **Tissues/cells:** Tubular and collecting-duct **epithelial cells** (targets); infiltrating **neutrophils** (CL:0000775) and **macrophages** (CL:0000235). Tissue type: epithelial and tubulointerstitial.
- **Subcellular:** Bacterial engagement at the **apical plasma membrane** (GO:0016324) of tubular epithelium; intracellular bacterial communities; neutrophil **azurophil granules** and NADPH-oxidase-driven ROS; NET chromatin extrusion (extracellular region, GO:0005576).
- **Localization / laterality:** Often **unilateral** (single kidney/segment), can be **bilateral**; EPN commonly affects one kidney with contralateral involvement possible; acute lobar nephronia is focal/segmental.

---

## 8. Temporal Development

- **Onset:** Acute to subacute (hours–days). Age of onset **bimodal** — infancy and reproductive-age adulthood, with elderly resurgence.
- **Progression/stages:** Uncomplicated APN → (if untreated/host-vulnerable) → acute lobar nephronia → renal/perinephric abscess → emphysematous pyelonephritis → urosepsis. Chronic sequela: post-pyelonephritic scarring → CKD.
- **Course/duration:** Typically **self-limited with antibiotics** over 7–14 days; **delay >72 h predicts permanent scarring** ([PMID: 27748543](https://pubmed.ncbi.nlm.nih.gov/27748543/)). Recurrence is common in the presence of unresolved predisposing factors (obstruction, VUR, diabetes).
- **Critical intervention window:** Prompt antibiotics (ideally within hours to <72 h) and, when obstruction is present, **urgent decompression** (nephrostomy/stent). Early nephrectomy (≤24 h) improves survival in fulminant EPN ([PMID: 42221797](https://pubmed.ncbi.nlm.nih.gov/42221797/)).

---

## 9. Inheritance and Population

**Epidemiology.** In a 19-year Danish population-based cohort (66,937 APN episodes in 57,162 patients; ICD-10), the **incidence roughly doubled** over 2000–2018 ([PMID: 38020186](https://pubmed.ncbi.nlm.nih.gov/38020186/)):

| Group | 2000 (per 100,000/yr) | 2018 (per 100,000/yr) |
|---|---|---|
| Women | 6.8 | 15.4 |
| Men | 2.7 | 4.5 |
| Infant girls | 7.4 | 64.8 |
| Infant boys | 17.1 | 52.5 |

Direct quote: "*the incidence increased from 6.8 … to 15.4 … in women and from 2.7 … to 4.5 … in men*" and "*Among infants, the rate rose from 7.4 … to 64.8 … in girls and from 17.1 … to 52.5 … in boys*" ([PMID: 38020186](https://pubmed.ncbi.nlm.nih.gov/38020186/)). The rise was driven largely by young children and not explained by increasing CAKUT prevalence. In US surveillance, pyelonephritis accounted for **19.9%** of invasive *E. coli* infections; APN affects ~**250,000 US patients annually** ([PMID: 41627814](https://pubmed.ncbi.nlm.nih.gov/41627814/), [PMID: 32849562](https://pubmed.ncbi.nlm.nih.gov/32849562/)).

**Inheritance.** Not a monogenic disorder — no Mendelian inheritance pattern, penetrance, anticipation, founder effect, or carrier frequency applies. Susceptibility is **multifactorial/polygenic**, mediated by innate-immunity variants (IRF3, IL-8/rs4073, CXCR1) plus anatomic/metabolic risk.

**Demographics.** Strong **female predominance** across ages; infant male predominance in the neonatal period (before shifting female). Diabetics and pregnant women are over-represented in severe forms. No specific ethnic founder distribution; ESBL/fluoroquinolone-resistant strains show geographic variation (higher ESBL in complicated cases and certain regions).

---

## 10. Diagnostics

**Laboratory tests.** Urinalysis (pyuria, leukocyte esterase, nitrites, hematuria), **urine culture with ≥10⁵ CFU/mL** and susceptibility testing (essential given resistance), blood cultures in severe/hospitalized cases, CBC (leukocytosis), CRP, and creatinine/eGFR. LOINC: urine culture (630-4); leukocyte esterase (5799-2); nitrite (5802-4).

**Biomarkers.**
- **Procalcitonin (PCT):** correlates with acute parenchymal involvement on DMSA (8.81 vs 1.7 ng/mL in lesion vs no-lesion, p=0.01) and predicts scarring (cut-off ~1 ng/mL, AUC 0.74), though it cannot replace DMSA ([PMID: 23481452](https://pubmed.ncbi.nlm.nih.gov/23481452/), [PMID: 19205751](https://pubmed.ncbi.nlm.nih.gov/19205751/), [PMID: 27329559](https://pubmed.ncbi.nlm.nih.gov/27329559/)).
- **Urinary NGAL (LCN2):** meta-analysis (13 studies) — sensitivity 0.88 (95% CI 0.79–0.94), specificity 0.86 (0.78–0.92) for UTI; for APN sensitivity 0.79, specificity 0.78 ([PMID: 39423110](https://pubmed.ncbi.nlm.nih.gov/39423110/)). In 321 febrile children uNGAL outperformed CRP/WBC for UTI and APN (AUC 0.860 and 0.780) ([PMID: 33091975](https://pubmed.ncbi.nlm.nih.gov/33091975/)). uNGAL and PCT are higher in children who later scar ([PMID: 40742430](https://pubmed.ncbi.nlm.nih.gov/40742430/)).

**Imaging.** Reserved for complicated/atypical/non-responding cases: **renal ultrasound** (hydronephrosis, abscess), **contrast-enhanced CT** (reference for EPN — intrarenal gas; abscess; obstruction), and **DMSA (⁹⁹ᵐTc-dimercaptosuccinic acid) scintigraphy** — the **reference standard for parenchymal involvement and scarring** in children ([PMID: 27748543](https://pubmed.ncbi.nlm.nih.gov/27748543/), [PMID: 16894326](https://pubmed.ncbi.nlm.nih.gov/16894326/)). In XGP, CT shows the "bear-paw" sign with staghorn calculus ([PMID: 41323310](https://pubmed.ncbi.nlm.nih.gov/41323310/)).

**Genetic / omics diagnostics.** Not indicated for routine diagnosis (APN is not a monogenic disease). Research-level host-susceptibility genotyping (IRF3, IL-8 rs4073, CXCR1) and pathogen whole-genome sequencing (virulence/resistance profiling, e.g., ST131-H30Rx) are used in studies, not clinical care ([PMID: 40926251](https://pubmed.ncbi.nlm.nih.gov/40926251/)).

**Clinical criteria & differential diagnosis.** Diagnosis is clinical (fever + flank pain + CVA tenderness) plus pyuria/bacteriuria and positive culture; IDSA criteria used for pregnancy studies. Differentials: cystitis (no systemic/CVA signs), nephrolithiasis/renal colic, PID/STIs (co-occur in sexually active women — evaluate for cervical motion tenderness) ([PMID: 40360224](https://pubmed.ncbi.nlm.nih.gov/40360224/)), ovarian vein thrombophlebitis (postpartum fever) ([PMID: 42402563](https://pubmed.ncbi.nlm.nih.gov/42402563/)), appendicitis, and, in mass-forming XGP, renal cell/squamous carcinoma ([PMID: 33282610](https://pubmed.ncbi.nlm.nih.gov/33282610/)).

**Screening.** In pregnancy, **screen for ASB with urine culture** (see §13) ([PMID: 39349024](https://pubmed.ncbi.nlm.nih.gov/39349024/)).

---

## 11. Outcome / Prognosis

**Mortality.** Uncomplicated APN has low mortality with prompt therapy. Severe/complicated forms are dangerous: in critically ill EPN, **ICU mortality ~15%**, with higher SAPS II independently predicting 90-day mortality (HR 1.08/point, 95% CI 1.05–1.12) and **early nephrectomy associated with lower mortality (HR 0.18, 95% CI 0.04–0.90, p=0.037)** ([PMID: 42221797](https://pubmed.ncbi.nlm.nih.gov/42221797/)). In purulent pyelonephritis meta-analysis, overall mortality ~5.8% (342/5912), rising to 20–30% with septic shock ([PMID: 42417339](https://pubmed.ncbi.nlm.nih.gov/42417339/)). In invasive *E. coli* infection surveillance, 7.9% died ([PMID: 41627814](https://pubmed.ncbi.nlm.nih.gov/41627814/)).

**Morbidity / complications.** Urosepsis/septic shock, renal and perinephric abscess, emphysematous pyelonephritis, pyonephrosis, acute kidney injury, and **permanent renal scarring** → hypertension and CKD progression. UTI requiring hospital admission accelerates eGFR decline in CKD patients and is a potentially modifiable CKD-progression factor ([PMID: 40022942](https://pubmed.ncbi.nlm.nih.gov/40022942/)). In pregnancy, APN is linked to preterm birth and low birth weight ([PMID: 41274602](https://pubmed.ncbi.nlm.nih.gov/41274602/), [PMID: 41684314](https://pubmed.ncbi.nlm.nih.gov/41684314/)).

**Prognostic factors.** Delay to treatment >72 h (scarring), VUR presence/grade, diabetes, obstruction, septic shock, pre-existing CKD, thrombocytopenia, and dialysis need. **Prognostic biomarkers:** elevated PCT and uNGAL predict acute parenchymal lesions and later scarring ([PMID: 27748543](https://pubmed.ncbi.nlm.nih.gov/27748543/), [PMID: 40742430](https://pubmed.ncbi.nlm.nih.gov/40742430/)).

---

## 12. Treatment

**Pharmacotherapy (empirical then culture-directed).**

| Setting | Agents | NCIT (suggested) | Evidence |
|---|---|---|---|
| Uncomplicated APN (outpatient) | Fluoroquinolone (ciprofloxacin/levofloxacin); TMP-SMX if susceptible | Ciprofloxacin C376; Levofloxacin C1637 | 7 days non-inferior to 14 days ([PMID: 22726802](https://pubmed.ncbi.nlm.nih.gov/22726802/)) |
| Hospitalized / febrile UTI | 3rd-gen cephalosporin (ceftriaxone) IV ± aminoglycoside; oral step-down | Ceftriaxone C287 | SPILF guidelines ([PMID: 42314979](https://pubmed.ncbi.nlm.nih.gov/42314979/)) |
| Complicated / ESBL / resistant | Carbapenem; **ceftazidime-avibactam** (carbapenem-sparing); piperacillin-tazobactam | Ceftazidime-Avibactam C120207 | Non-inferior to doripenem ([PMID: 27313268](https://pubmed.ncbi.nlm.nih.gov/27313268/)) |
| Uncomplicated (oral, ESBL) | Pivmecillinam, fosfomycin, nitrofurantoin (lower-tract) | Nitrofurantoin C61854 | ([PMID: 42130306](https://pubmed.ncbi.nlm.nih.gov/42130306/)) |
| Pregnancy | Cephalosporins (cefixime), IV for pyelonephritis | — | ([PMID: 39349024](https://pubmed.ncbi.nlm.nih.gov/39349024/), [PMID: 39563593](https://pubmed.ncbi.nlm.nih.gov/39563593/)) |

**Duration.** Landmark RCT: **ciprofloxacin 500 mg BID × 7 days is clinically and bacteriologically non-inferior to 14 days** in women with community-acquired APN (248 randomized) ([PMID: 22726802](https://pubmed.ncbi.nlm.nih.gov/22726802/)). In children, ≤7-day and oral courses may not increase recurrence versus longer/parenteral therapy ([PMID: 42803594](https://pubmed.ncbi.nlm.nih.gov/42803594/)).

**Resistance context.** Empirical therapy is constrained by resistance: fluoroquinolone resistance **6.3% (uncomplicated) vs 19.9% (complicated)** and ESBL production **2.6% vs 12.2%**, with **34.5% of ESBL cases community-acquired** and most ESBL/FQ-resistant cases initially treated with inactive drugs ([PMID: 27532362](https://pubmed.ncbi.nlm.nih.gov/27532362/)). ST131-H30Rx ESBL clones drive recurrence ([PMID: 40926251](https://pubmed.ncbi.nlm.nih.gov/40926251/)).

**Surgical / interventional.** Urgent **decompression** (percutaneous nephrostomy or ureteral stent) for obstruction; **percutaneous drainage** for abscesses >3–5 cm (avoids open surgery in 80–90%); **nephrectomy** for fulminant EPN/XGP; XGP may sometimes be managed with kidney-preserving therapy in non-septic patients ([PMID: 42417339](https://pubmed.ncbi.nlm.nih.gov/42417339/), [PMID: 26889137](https://pubmed.ncbi.nlm.nih.gov/26889137/)).

**Supportive care.** IV fluids, antipyretics/analgesia, vasopressors and ICU care for septic shock; glycemic control in diabetics.

**Experimental / precision approaches.** **FimH mannoside inhibitors** (e.g., FIM1033) attenuate bacterial loads in pyelonephritis models — an anti-adhesion, non-antibiotic strategy ([PMID: 33513212](https://pubmed.ncbi.nlm.nih.gov/33513212/)).

---

## 13. Prevention

**Primary prevention.**
- **Pregnancy screen-and-treat of ASB** — cornerstone: "*During pregnancy, there is increased risk of ascending urinary tract infection (UTI) resulting in pyelonephritis and associated preterm delivery and low birth weight*" ([PMID: 41274602](https://pubmed.ncbi.nlm.nih.gov/41274602/)); "*Screening for ASB with a urine culture is required during pregnancy, and a positive culture is treated for 5 to 7 days with culture-specific antibiotics*" ([PMID: 39349024](https://pubmed.ncbi.nlm.nih.gov/39349024/)). ASB is common (e.g., 29% culture-positive, 72% asymptomatic in a tertiary cohort) ([PMID: 42516470](https://pubmed.ncbi.nlm.nih.gov/42516470/)); risk-factor-based selective screening is emerging to balance stewardship ([PMID: 41274602](https://pubmed.ncbi.nlm.nih.gov/41274602/)).
- Hydration, voiding hygiene, glycemic control, and source control of stones/obstruction.

**Recurrence prevention (non-antibiotic, RCT-supported).**
- **Sublingual vaccine MV140** — "*Immunoprophylaxis with the sublingual vaccine MV140 significantly reduced recurrence compared with placebo, with 56–58% of women remaining UTI free in a large RCT*" ([PMID: 42133003](https://pubmed.ncbi.nlm.nih.gov/42133003/)).
- **Methenamine hippurate** — "*non-inferior to daily antibiotic prophylaxis in preventing rUTIs*" ([PMID: 42133003](https://pubmed.ncbi.nlm.nih.gov/42133003/)); supported alongside cranberry and (postmenopausal) vaginal estrogen in an overview of 27 systematic reviews, while probiotics/D-mannose/vaccines need stronger evidence ([PMID: 42225392](https://pubmed.ncbi.nlm.nih.gov/42225392/)).
- **Vaginal estrogen** in postmenopausal women.

**Antibiotic prophylaxis in VUR (children).** The **RIVUR RCT** (>600 children) showed long-term antimicrobial prophylaxis **reduced UTI recurrence by 50%** (overall NNT ~10) ([PMID: 35928985](https://pubmed.ncbi.nlm.nih.gov/35928985/), [PMID: 38244067](https://pubmed.ncbi.nlm.nih.gov/38244067/)). Re-analysis identified high-benefit subgroups (NNT ≤5): grade IV VUR and children with bladder-bowel dysfunction, especially with febrile index UTI ([PMID: 37693511](https://pubmed.ncbi.nlm.nih.gov/37693511/)).

**Secondary/tertiary prevention.** Prompt treatment (<72 h) to prevent scarring; DMSA/imaging follow-up; management of obstruction/diabetes to prevent EPN and CKD progression.

---

## 14. Other Species / Natural Disease

- **Taxonomy affected:** Humans (NCBI:txid9606) primarily; naturally occurring ascending bacterial pyelonephritis also affects companion animals — **dogs** (*Canis lupus familiaris*, txid9615) and **cats** (*Felis catus*, txid9685) — and livestock (cattle, pigs), typically from ascending *E. coli*/*Proteus*/*Enterococcus* UTIs, obstruction, or stones.
- **Comparative pathology:** Mechanisms are conserved — ascending uropathogen infection, obstruction/stasis predisposition, and neutrophil-mediated parenchymal injury. Veterinary relevance is significant in small-animal medicine (pyelonephritis as a cause of renal failure).
- **Orthologous host genes (NCBI Gene):** mouse *Irf3* (54131), *Tlr4* (21898; human *TLR4* 7099), functional chemokine homologs (mouse *Cxcl1/2* for human *CXCL8* 3576), *Cxcr1*, and *Dsg2* (mouse 13511; human *DSG2* 1829).
- **Transmission / zoonosis:** UPEC strains overlap between humans and animals/food (foodborne extraintestinal *E. coli* reservoirs), but APN itself is not classically person-to-person transmissible.

---

## 15. Model Organisms

- **Mouse (murine) ascending UTI/pyelonephritis models** are the workhorse: transurethral UPEC inoculation in **C3H/HeN** and related strains reproduces ascending kidney infection, abscesses, and scarring.
  - **Genetic models:** *Irf3⁻/⁻* mice show "*a pathogen-specific increase in acute mortality, bacterial burden, abscess formation and renal damage compared to wild type mice*," directly modeling the human IRF3 susceptibility axis ([PMID: 20886096](https://pubmed.ncbi.nlm.nih.gov/20886096/)). CXCR1/IL-8-axis and TLR4 models recapitulate the ASB-vs-pyelonephritis dichotomy ([PMID: 11817650](https://pubmed.ncbi.nlm.nih.gov/11817650/)).
  - **Mechanistic/receptor models:** FimH⁻ UPEC mutants fail to colonize the kidney; DSG2 identified as the renal FimH receptor via CRISPR screen in collecting-duct cells; mannoside FIM1033 attenuates loads — establishing druggable anti-adhesion targets ([PMID: 33513212](https://pubmed.ncbi.nlm.nih.gov/33513212/)).
  - **Scarring/sex-difference models:** androgen-influenced activin-A macrophage polarization drives post-pyelonephritic scarring; sex differences in kidney bacterial community dynamics are modeled in mice ([PMID: 32849562](https://pubmed.ncbi.nlm.nih.gov/32849562/), [PMID: 33468577](https://pubmed.ncbi.nlm.nih.gov/33468577/)).
- **In vitro / cellular:** Renal collecting-duct epithelial cell lines and CRISPR screens (FimH–DSG2 receptor identification); primary neutrophil functional assays (NET formation, ROS).
- **Phenotype recapitulation & limitations:** Mouse models faithfully reproduce ascension, neutrophil-dependent clearance, abscess/scarring, and adhesin dependence. Limitations: interspecies differences in chemokine biology (mice lack a direct IL-8/CXCL8 ortholog; functional homologs used), urinary-tract anatomy, and the human polymorphism spectrum; EPN (diabetes-driven, gas-forming) is less commonly modeled.
- **Resources:** MGI (mouse), plus UPEC strain collections; models used to study innate immunity, virulence, scarring, and anti-adhesion/vaccine therapeutics.

---

## Mechanistic Model / Interpretation

```
 UPEC colonization (introitus -> bladder)
              |  FimH->DSG2 ; P-fimbriae->glycosphingolipid   [PMID 33513212]
              v
 Ascension to renal pelvis / collecting duct
              |  LPS/adhesins -> TLR4
              v
 Epithelial innate sensing -> IRF3 + NF-kB -> IL-8 (CXCL8)    [PMID 20886096, 21042230]
              |  IL-8 -> CXCR1 on neutrophils
              v
 NEUTROPHIL RECRUITMENT (decisive effector)                  [PMID 11817650]
        |------------- Branch A: robust axis --------------|
        |  phagocytosis, ROS, NETs -> clearance            |-> ASB / resolution  [PMID 39321268]
        |                                                  |
        |------------- Branch B: weak axis ----------------|
           (low CXCR1; IRF3/IL-8 rs4073 risk genotype)     |-> ACUTE PYELONEPHRITIS
              |  parenchymal proliferation, abscess        |
              v                                             |
   Dysregulated neutrophil injury (ROS, proteases,          |
   S100A8/A9, NETs) + androgen-macrophage activin-A         |-> RENAL SCARRING -> HTN/CKD
              |                                    [PMID 42524556, 32849562, 40022942]
              v
   Branch C (diabetes/obstruction): gas-forming necrosis    -> EMPHYSEMATOUS PN -> SEPSIS/DEATH
                                                    [PMID 42221797]
```

The unifying theme is that **APN is a disease of the host–pathogen interface**: an identical UPEC exposure yields divergent outcomes (silent carriage vs destructive parenchymal infection vs necrotizing sepsis) depending on host innate-signaling genotype, anatomy (VUR/obstruction), and metabolic state (diabetes/pregnancy). This explains why therapy is not only antimicrobial but also directed at **source control** (decompression, drainage, nephrectomy) and why prevention targets the **modifiable environmental inputs** (ASB in pregnancy, obstruction, recurrence). Neutrophils are the pivotal, double-edged effector — indispensable for clearance yet responsible for the scarring that links acute infection to chronic kidney disease.

---

## Evidence Base

| PMID | Contribution | Type |
|---|---|---|
| [20886096](https://pubmed.ncbi.nlm.nih.gov/20886096/) | IRF3-dependent innate resistance; human promoter polymorphism → symptomatic kidney infection | Mouse + human genetics |
| [11817650](https://pubmed.ncbi.nlm.nih.gov/11817650/) | Neutrophils as critical effectors; CXCR1/IL-8 dysfunction → pyelonephritis + scarring | Review/mechanism |
| [21042230](https://pubmed.ncbi.nlm.nih.gov/21042230/) | IL-8 rs4073 associates with pediatric parenchymal renal infection | Human genetics |
| [33513212](https://pubmed.ncbi.nlm.nih.gov/33513212/) | DSG2 as renal FimH receptor; FimH mannoside FIM1033 therapy | Mouse + in vitro |
| [39321268](https://pubmed.ncbi.nlm.nih.gov/39321268/) | Urinary NETs protect against ascension; basis of leukocyte dipstick | Human + mouse |
| [42524556](https://pubmed.ncbi.nlm.nih.gov/42524556/) | Neutrophil double-edged role; effector molecules of injury/fibrosis | Review |
| [32849562](https://pubmed.ncbi.nlm.nih.gov/32849562/) | Androgen–activin-A macrophage polarization → scarring; ~250k US cases/yr | Mouse |
| [27532362](https://pubmed.ncbi.nlm.nih.gov/27532362/) | US resistance rates (FQ, ESBL) in APN; *E. coli* 86.9% | Prospective cohort |
| [42221797](https://pubmed.ncbi.nlm.nih.gov/42221797/) | EPN ICU cohort; diabetes/shock/obstruction; early nephrectomy benefit | Multicenter cohort |
| [38020186](https://pubmed.ncbi.nlm.nih.gov/38020186/) | Population incidence doubling; sex/infant distribution | Registry cohort |
| [22726802](https://pubmed.ncbi.nlm.nih.gov/22726802/) | 7 vs 14 day ciprofloxacin non-inferiority | RCT |
| [27313268](https://pubmed.ncbi.nlm.nih.gov/27313268/) | Ceftazidime-avibactam vs doripenem for complicated UTI/APN | Phase 3 RCT |
| [42133003](https://pubmed.ncbi.nlm.nih.gov/42133003/) | MV140 vaccine, methenamine non-inferiority | Systematic review |
| [42225392](https://pubmed.ncbi.nlm.nih.gov/42225392/) | Overview of 27 SRs on non-antibiotic prevention | Overview of SRs |
| [35928985](https://pubmed.ncbi.nlm.nih.gov/35928985/) / [37693511](https://pubmed.ncbi.nlm.nih.gov/37693511/) | RIVUR: 50% recurrence reduction; high-benefit subgroups | RCT + re-analysis |
| [27748543](https://pubmed.ncbi.nlm.nih.gov/27748543/) | Delay >72 h → scarring; DMSA outcomes | Pediatric cohort |
| [39423110](https://pubmed.ncbi.nlm.nih.gov/39423110/) / [33091975](https://pubmed.ncbi.nlm.nih.gov/33091975/) / [40742430](https://pubmed.ncbi.nlm.nih.gov/40742430/) | uNGAL diagnostic accuracy; predicts scarring | Meta-analyses/cohort |
| [41274602](https://pubmed.ncbi.nlm.nih.gov/41274602/) / [39349024](https://pubmed.ncbi.nlm.nih.gov/39349024/) | Pregnancy ASB screen-and-treat | Reviews |
| [40022942](https://pubmed.ncbi.nlm.nih.gov/40022942/) | UTI/hospital admission accelerates CKD progression | Multicenter observational |

**Consistency/conflict.** Findings are broadly consistent. One tension: procalcitonin's diagnostic value for parenchymal involvement varies by cut-off and study ([PMID: 16894326](https://pubmed.ncbi.nlm.nih.gov/16894326/) reported limited specificity), and a single-country pregnancy comparison found no difference in pyelonephritis rates between screening vs non-screening centers ([PMID: 37515907](https://pubmed.ncbi.nlm.nih.gov/37515907/)), tempering the universality of screen-and-treat and supporting emerging **selective** screening.

---

## Limitations and Knowledge Gaps

1. **No monogenic basis / modest host-genetics evidence.** Susceptibility variants (IRF3, IL-8 rs4073, CXCR1) derive from candidate-gene and small cohort studies; no large GWAS for APN susceptibility is established, and effect sizes/penetrance are not quantified for clinical use.
2. **Mechanistic reliance on mouse models.** Key adhesin (FimH–DSG2), IRF3, and scarring mechanisms are demonstrated primarily in mice; interspecies chemokine differences (no direct murine IL-8 ortholog) limit translation. Human FimH-mannoside efficacy is not yet clinically proven.
3. **Biomarker thresholds unstandardized.** uNGAL and PCT show promising accuracy but variable cut-offs; neither replaces DMSA. Prospective validation and standardized assays are needed.
4. **Prevention evidence heterogeneity.** ASB screening benefit rests partly on older/low-quality evidence; MV140 and methenamine are promising but need broader confirmation; RIVUR benefit is concentrated in specific subgroups with attendant resistance costs.
5. **Resistance evolution.** Community ESBL/fluoroquinolone-resistant *E. coli* (ST131-H30Rx) is rising, and much of the resistance/epidemiology data is regional (US, Danish, European), limiting global generalizability.
6. **Scarring→CKD causality.** The link between APN and CKD progression is largely observational and confounded by baseline renal function.

---

## Proposed Follow-up Experiments / Actions

1. **Host-genetics validation:** Large multi-ancestry GWAS/targeted sequencing of APN-vs-ASB cohorts to confirm and quantify IRF3, *CXCL8* rs4073, CXCR1, and TLR4 effects; test as a clinical risk-stratification panel.
2. **Anti-adhesion translation:** Advance FimH mannoside inhibitors (FIM1033-class) into human trials for prevention/treatment of recurrent pyelonephritis, and evaluate DSG2-targeting strategies.
3. **Biomarker standardization:** Prospective, multicenter study to establish uNGAL/PCT cut-offs for APN diagnosis and scarring prediction, benchmarked against DMSA, to reduce unnecessary imaging.
4. **Precision prevention trials:** Head-to-head and combination RCTs of MV140, methenamine, and vaginal estrogen vs antibiotic prophylaxis, with resistance and adherence endpoints; define risk-factor-based selective ASB screening in pregnancy.
5. **Stewardship-driven treatment:** Broaden evidence for short-course and carbapenem-sparing regimens (ceftazidime-avibactam and newer β-lactam/β-lactamase inhibitors) in ESBL APN; embed rapid resistance diagnostics to reduce inactive empirical therapy (currently 45–76% in resistant cases).
6. **Scarring/CKD mechanism:** Test whether modulating the neutrophil injury arm (ROS, NETs, S100A8/A9) or androgen–activin-A macrophage axis prevents post-pyelonephritic fibrosis without impairing clearance; longitudinal cohorts to establish APN→CKD causality.

---

*Report compiled from 13 confirmed findings across 69 reviewed papers over 5 iterations. Evidence spans human clinical cohorts/RCTs, population registries, systematic reviews/meta-analyses, mouse models, and in-vitro mechanistic studies, with source types indicated throughout.*


## Artifacts

- [OpenScientist final report](Acute_Pyelonephritis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Acute_Pyelonephritis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 45 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 4 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 45 |
| On topic | 17 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:38020186` *(abstract only)*: "*Among infants, the rate rose from 7.4 … to 64.8 … in girls and from 17.1 … to 52.5 … in boys*"
  - closest text in source: "Among infants, the rate rose from 7.4 (95% CI: 7.4-7.4) to 64.8 (95% CI: 64.7-64.9) in girls and from 17.1 (95% CI: 17.1-17.2) to 52.5 (95% CI: 52.4-52.6) in boys"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 17 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001945` (1 mention) - the report calls it "Symptom/sign"; HP calls it **Fever**
- `HP:0032453` (1 mention) - the report calls it "pyuria"; HP calls it **Abnormal lip pigmentation**
- `HP:0000790` (1 mention) - the report calls it "Lab/sign"; HP calls it **Hematuria**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001974` (1 mention) - the report calls it "leukocytosis"; HP calls it **Increased total leukocyte count**, and lists "Leukocytosis" among its other names
- `UBERON:0002113` (1 mention) - the report calls it "Primary organ:** Kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names
- `UBERON:0001225` (1 mention) - the report calls it "renal parenchyma/cortex"; UBERON calls it **cortex of kidney**, and lists "renal cortex" among its other names
- `GO:0016324` (1 mention) - the report calls it "apical plasma membrane", "Subcellular:** Bacterial engagement at the **apical plasma membrane"; GO calls it **apical plasma membrane**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0016324` - called "apical plasma membrane", "Subcellular:** Bacterial engagement at the **apical plasma membrane"