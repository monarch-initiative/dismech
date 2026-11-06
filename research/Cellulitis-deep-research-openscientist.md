---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T11:05:06.376682'
end_time: '2026-09-29T11:22:11.709716'
duration_seconds: 1025.33
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cellulitis
  mondo_id: MONDO:0005230
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
citation_count: 39
reference_validation:
  total_references: 39
  verified: 39
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 12
  quotes_valid: 11
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:23635049
  relevance_assessed: 39
  on_topic: 20
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 32
  verified: 31
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 10
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0005230
    reported_labels:
    - MONDO
    ontology_label: cellulitis
  - term_id: NCIT:C349
    reported_labels:
    - First-line, non-purulent
    ontology_label: Carmustine
  - term_id: NCIT:C376
    reported_labels:
    - Streptococcal cellulitis; prophylaxis
    ontology_label: Cisplatin
  - term_id: NCIT:C932
    reported_labels:
    - Severe/IV MRSA coverage
    ontology_label: Vinca Alkaloid Compound
  labels_variant: 7
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
  path: Cellulitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Cellulitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cellulitis
- **MONDO ID:** MONDO:0005230 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Cellulitis** covering all of the
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

# Cellulitis (MONDO:0005230): A Comprehensive Disease Characteristics Report

## Summary

**Cellulitis is a common acute bacterial infection of the deep dermis and subcutaneous tissue that arises from a "two-hit" combination of a skin-barrier breach and impaired lymphatic/venous drainage.** In its most common (non-purulent) form it is predominantly caused by β-hemolytic streptococci, while purulent forms are typically driven by *Staphylococcus aureus* (including MRSA). Bacterial invasion of subcutaneous tissue, amplified by toxin-mediated cytolysis and a brisk innate inflammatory response, produces the cardinal clinical picture of poorly demarcated erythema, warmth, swelling (edema), pain, and tenderness — usually unilateral and most often affecting the lower leg. It is a clinical diagnosis with no gold-standard laboratory test; roughly one-third of patients admitted for "cellulitis" actually have a non-infectious mimic ("pseudocellulitis"), which drives substantial unnecessary antibiotic use and hospitalization.

The disease sits within a spectrum of skin and soft-tissue infections (SSTIs). At the mild end it overlaps with erysipelas (more superficial) and simple abscess; at the dangerous end it must be distinguished from **necrotizing fasciitis (NF)**, a surgical emergency. The two critical clinical decisions in cellulitis care are therefore (1) purulent vs. non-purulent (which determines whether empiric MRSA coverage is needed) and (2) cellulitis vs. necrotizing infection (which determines whether urgent surgery is required). Uncomplicated non-purulent cellulitis is treated with streptococcal-targeted β-lactams (e.g., cephalexin, dicloxacillin/flucloxacillin, penicillin); a landmark randomized trial showed that adding MRSA-active trimethoprim-sulfamethoxazole to cephalexin provides no benefit in uncomplicated disease.

Cellulitis is a large, rising, and costly public-health burden strongly linked to chronic edema and lymphedema. Recurrence is frequent and is driven by a self-reinforcing cycle in which each episode further damages lymphatics, worsening drainage and predisposing to the next episode. Two categories of prevention have robust randomized-trial support: **prophylactic low-dose penicillin V** (PATCH I trial: hazard ratio 0.55 for recurrence, number-needed-to-treat 5) and **compression therapy for chronic leg edema** (Webb NEJM trial: hazard ratio 0.23, stopped early for efficacy). This is not a genetic/Mendelian disease — there are no causal genes; "genetics" enters only through host susceptibility (e.g., diabetes, immune impairment) and pathogen virulence genetics (e.g., group A *Streptococcus* covR/covS regulatory mutations and toxins SpeB and streptolysin S).

---

## Section 1 — Disease Information

**Overview.** Cellulitis is an acute, spreading bacterial infection of the deep dermis and subcutaneous fat. Clinically it presents as an area of expanding erythema with warmth, edema, and tenderness, frequently accompanied by systemic features (fever, malaise) in more severe cases. **Erysipelas** is a closely related, more superficial variant involving the upper dermis and superficial lymphatics, classically with a raised, sharply demarcated border; in much of the clinical literature "cellulitis" and "erysipelas" are grouped together (as in the PATCH prophylaxis trials and the US burden analyses). The disease is best understood as the confluence of two prerequisites: **a portal of entry** (barrier breach) and **impaired local host drainage** (edema/lymphedema/venous insufficiency).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0005230 |
| ICD-10 | L03 (Cellulitis and acute lymphangitis); e.g., L03.11 cellulitis of lower limb; periorbital/orbital variants coded under H00–H05 |
| ICD-11 | 1B70 (Cellulitis) |
| MeSH | D002481 "Cellulitis" |
| SNOMED CT | 128045006 (Cellulitis) |
| OMIM / Orphanet | Not applicable — cellulitis is an acquired infectious disease, not a Mendelian disorder; no OMIM phenotype entry, not a rare disease with an Orphanet number |

**Synonyms / alternative names.** Cellulitis; bacterial cellulitis; skin and soft-tissue infection (as a parent category); erysipelas (superficial variant, often grouped); acute bacterial skin and skin-structure infection (ABSSSI — the regulatory term used in clinical trials); phlegmon (for the more diffuse suppurative form). Site-specific named entities include **periorbital (preseptal) cellulitis**, **orbital (postseptal) cellulitis**, and diabetic-foot cellulitis.

**Data source type.** The evidence base for cellulitis is drawn overwhelmingly from **aggregated disease-level resources** — randomized controlled trials, systematic reviews/meta-analyses, population-based case-control studies, and national administrative datasets (e.g., US National Emergency Department Sample, National Inpatient Sample) — rather than from individual-patient genomic/EHR mining. This reflects its nature as a common acquired infection rather than a rare genetic disorder.

---

## Section 2 — Etiology

**Primary cause: infectious.** Cellulitis is caused by bacteria that gain access to the deep dermis/subcutaneous tissue. The dominant organisms differ by clinical subtype:

- **Non-purulent cellulitis → β-hemolytic streptococci** (predominantly group A *Streptococcus pyogenes*, but also groups B, C, G). This is **Finding F001**. Two 2026 narrative reviews concur that "*β-hemolytic streptococci are the most common cause of non-purulent cellulitis*" ([PMID: 42711142](https://pubmed.ncbi.nlm.nih.gov/42711142/)) and that "*Non-purulent SSTI is most commonly associated with beta-haemolytic streptococci, while purulent SSTI is typically associated with Staphylococcus aureus*" ([PMID: 42727947](https://pubmed.ncbi.nlm.nih.gov/42727947/)).
- **Purulent cellulitis / abscess → *Staphylococcus aureus*, including MRSA.**
- **Special hosts/exposures** broaden the microbiology: diabetic foot infection can be polymicrobial (gram-negative aerobes and anaerobes) ([PMID: 27377687](https://pubmed.ncbi.nlm.nih.gov/27377687/)); water/marine exposure raises *Vibrio*/*Aeromonas*; endemic-area/diabetic patients can develop *Burkholderia pseudomallei* (melioidosis) mimicking necrotizing infection ([PMID: 41580634](https://pubmed.ncbi.nlm.nih.gov/41580634/)); immunocompromised patients may present with fungal mimics such as primary cutaneous cryptococcosis ([PMID: 42240944](https://pubmed.ncbi.nlm.nih.gov/42240944/)).

**Risk factors (environmental/host).** **Finding F002** synthesizes the strongest quantitative evidence. A systematic review/meta-analysis of 6 case-control studies ([PMID: 27864837](https://pubmed.ncbi.nlm.nih.gov/27864837/)) and a population-based case-control study of 29,062 pairs ([PMID: 29427797](https://pubmed.ncbi.nlm.nih.gov/29427797/)) establish the following:

| Risk factor | Odds ratio (95% CI) | Source |
|---|---|---|
| Previous cellulitis | OR 40.3 (22.6–72.0) | PMID 27864837 |
| Wound | OR 19.1 (9.1–40.0) | PMID 27864837 |
| Current leg ulcer | OR 13.7 (7.9–23.6) | PMID 27864837 |
| Lymphoedema / chronic leg oedema | OR 6.8 (3.5–13.3) | PMID 27864837 |
| Excoriating skin disease | OR 4.4 (2.7–7.1) | PMID 27864837 |
| Tinea pedis | OR 3.2 (1.9–5.3) | PMID 27864837 |
| Varicose veins | AOR 2.95 (2.50–3.48) | PMID 29427797 |
| Tinea pedis | AOR 3.05 (1.45–6.42) | PMID 29427797 |
| Lymphoedema | AOR 2.65 (1.71–4.10) | PMID 29427797 |
| Obesity (BMI >30) | AOR 2.05 | PMID 29427797 |
| Saphenous vein harvest | AOR 1.74 | PMID 29427797 |
| Rheumatologic disease | AOR 2.12 | PMID 29427797 |
| Liver disease | AOR 1.77 | PMID 29427797 |
| Renal disease | AOR 1.28 | PMID 29427797 |

These cluster into two mechanistic themes: **barrier breaches** (wounds, ulcers, tinea pedis, excoriating skin disease) and **impaired drainage** (lymphedema, chronic edema, varicose veins, obesity, vein harvest). Additional host risk factors include diabetes mellitus, older age, immunosuppression, and congestive heart failure (an ICU-symposium population study reported increased cellulitis risk in CHF, [PMID: 27885969](https://pubmed.ncbi.nlm.nih.gov/27885969/)). An SSTI resource-utilization cohort confirmed diabetes (OR 1.65), chronic kidney disease (OR 1.34), and lymphedema (OR 1.85) as predictors of adverse hospital course ([PMID: 42759235](https://pubmed.ncbi.nlm.nih.gov/42759235/)).

**Genetic risk factors.** There are **no established Mendelian causal genes or GWAS-confirmed susceptibility loci** for cellulitis. Host genetic contribution is indirect (e.g., genetic conditions producing lymphedema, immunodeficiency, or diabetes would raise risk). This is a key "not applicable" for this disease.

**Protective factors.** Modifiable/environmental protective factors are the mirror image of the risk factors: treatment of tinea pedis and interdigital maceration, wound care, weight reduction, and control of chronic edema (compression) all reduce risk. Antibiotic prophylaxis (penicillin) reduces recurrence. No genetic protective variants are established.

**Gene–environment interactions.** The most relevant "gene–environment" axis is **pathogen genetics × host environment**: e.g., group A *Streptococcus* strains carrying covR/covS regulatory mutations produce more toxin and cause more aggressive local infection (see Section 6), and diabetic (immunocompromised) hosts allow pathogen regulatory pathways (e.g., staphylococcal ClpX-dependent pathways, [PMID: 42262120](https://pubmed.ncbi.nlm.nih.gov/42262120/)) to exacerbate disease. Human germline gene–environment interaction data are not established for cellulitis.

---

## Section 3 — Phenotypes

Cellulitis phenotypes are **clinical signs/symptoms** rather than laboratory-defined. Core manifestations, with suggested HPO terms:

| Phenotype | Type | HPO suggestion | Frequency/notes |
|---|---|---|---|
| Erythema (poorly demarcated, spreading) | Clinical sign | HP:0010783 (Erythema) | Near-universal (defining feature) |
| Localized skin warmth | Clinical sign | HP:0011121 (Abnormality of skin morphology) | Very common |
| Edema/swelling of affected area | Clinical sign | HP:0000969 (Edema) | Very common |
| Pain / tenderness | Symptom | HP:0025280 (Pain) | Very common |
| Fever | Symptom/sign | HP:0001945 (Fever) | Common in moderate–severe disease |
| Leukocytosis | Laboratory abnormality | HP:0001974 (Leukocytosis) | Component of ALT-70/LRINEC scoring |
| Tachycardia | Clinical sign | HP:0001649 (Tachycardia) | Component of ALT-70 |
| Lymphangitis / regional lymphadenopathy | Clinical sign | HP:0002716 (Lymphadenopathy) | Variable |
| Bullae / skin necrosis | Clinical sign | HP:0008066 (Abnormal blistering of the skin) | Red flag for necrotizing infection |

**Characteristics.** *Age of onset:* any age but incidence rises with age; lower-extremity disease predominates in adults and the elderly. Periorbital cellulitis is disproportionately pediatric. *Severity:* variable, from mild outpatient-managed cellulitis to severe/systemic disease with sepsis. *Progression:* typically acute and progressive over hours to a few days; **episodic/recurrent** over a patient's lifetime is characteristic in those with chronic edema. *Frequency among affected:* recurrence is common — in prophylaxis-trial control arms, 33–40% of high-risk patients had a recurrence within the study window ([PMID: 23635049](https://pubmed.ncbi.nlm.nih.gov/23635049/); [PMID: 32786188](https://pubmed.ncbi.nlm.nih.gov/32786188/)).

**Quality-of-life impact.** Cellulitis, especially recurrent disease, imposes significant QOL burden and healthcare cost; chronic edema and repeated episodes cause pain, immobility, missed work, and hospital admissions ([PMID: 31420389](https://pubmed.ncbi.nlm.nih.gov/31420389/), ICTOC protocol; [PMID: 33238162](https://pubmed.ncbi.nlm.nih.gov/33238162/)).

---

## Section 4 — Genetic / Molecular Information

**This section is largely "not applicable" in the Mendelian sense.** Cellulitis has:

- **No causal human genes**, no OMIM phenotype, no pathogenic germline variants, no ACMG/AMP variant classifications, no modifier genes, no disease-defining chromosomal abnormalities, and no established disease-specific epigenetic signatures.
- **Molecular genetics resides in the pathogen.** The clinically important "genetics" of cellulitis are microbial virulence determinants. In group A *Streptococcus* (GAS), the **covR/covS (CsrRS) two-component regulatory system** controls virulence-gene expression; loss-of-function mutations de-repress toxins and are frequent in severe invasive disease (necrotizing fasciitis, toxic shock). Key toxin genes include *speB* (streptococcal pyrogenic exotoxin B, a cysteine protease) and *sagA*/the *sag* operon encoding **streptolysin S (SLS)** (see Section 6 and **Finding F005**, [PMID: 41175456](https://pubmed.ncbi.nlm.nih.gov/41175456/)). Additional pathogen-genetics literature reviewed here includes acquisition of toxin-encoding lysogenic bacteriophage elements enhancing GAS virulence ([PMID: 41661104](https://pubmed.ncbi.nlm.nih.gov/41661104/)), a socially-regulated teichoic-acid-like wall modification associated with immune suppression ([PMID: 41733371](https://pubmed.ncbi.nlm.nih.gov/41733371/)), and a staphylococcal ClpX-dependent regulatory pathway that exacerbates infection in diabetes ([PMID: 42262120](https://pubmed.ncbi.nlm.nih.gov/42262120/)).

Suggested gene annotations (pathogen, not human): GAS *covR*/*covS*, *speB*, *sagA*/streptolysin S; *S. aureus* toxin/regulatory loci.

---

## Section 5 — Environmental Information

**Environmental/host factors** (non-genetic) are the principal drivers (see Section 2): skin barrier disruption (trauma, wounds, ulcers, tinea pedis, eczema, injection drug use), chronic edema/lymphedema, venous insufficiency/varicose veins, obesity, diabetes, prior surgery (e.g., saphenous vein harvest), and immunosuppression.

**Lifestyle factors.** Obesity is a robust modifiable risk factor (AOR ~2.05). Injection drug use is a recognized portal of entry and outbreak source (e.g., wound botulism among people who inject drugs, [PMID: 27885969](https://pubmed.ncbi.nlm.nih.gov/27885969/)). Poor foot hygiene facilitating tinea pedis increases risk.

**Infectious agents (NCBI Taxonomy).**

| Organism | NCBI Taxon | Role |
|---|---|---|
| *Streptococcus pyogenes* (group A) | txid1314 | Predominant cause of non-purulent cellulitis |
| β-hemolytic streptococci groups B/C/G (incl. *S. dysgalactiae*) | e.g., *S. agalactiae* txid1311 | Common causes, esp. in comorbid hosts |
| *Staphylococcus aureus* (incl. MRSA) | txid1280 | Purulent cellulitis/abscess |
| *Haemophilus influenzae* type b | txid727 | Historically periorbital/orbital cellulitis (now rare post-vaccine) |
| *Streptococcus pneumoniae* | txid1313 | Periorbital/orbital cellulitis |
| *Burkholderia pseudomallei* | txid28450 | Melioidosis mimicking necrotizing SSTI in endemic areas/diabetics |
| *Vibrio*/*Aeromonas* spp. | — | Water-exposure cellulitis |

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **A skin-barrier breach** (tinea pedis interdigital fissure, wound, ulcer, excoriation, surgical incision) **creates a portal of entry** for bacteria into the deep dermis/subcutis. *(Demonstrated epidemiologically via strong ORs for wounds/ulcers/tinea; F002.)*
2. **Impaired lymphatic/venous drainage** (lymphedema, chronic edema, venous insufficiency, obesity) **results in** local stasis, protein-rich interstitial fluid, and reduced immune surveillance, which **lowers the inoculum threshold** needed to establish infection. *(Inferred mechanistically; supported by strong ORs for lymphedema/edema and by the therapeutic success of compression; F002, F009.)*
3. **Bacteria (predominantly β-hemolytic streptococci) invade and proliferate** in subcutaneous tissue. *(Demonstrated microbiologically; F001.)*
4. **Secreted virulence factors mediate tissue damage.** In GAS, covR/covS regulatory mutations de-repress toxins; **SpeB cleaves gasdermin A → keratinocyte pyroptotic death**, and **streptolysin S (SLS) drives keratinocyte and macrophage death with elevated IL-1β**, producing larger lesions. *(Demonstrated in mouse subcutaneous infection model; F005: SLS-deficient ΔcovR mutant showed reduced lesion size and mortality.)*
5. **Toxin-mediated cell death and pathogen-associated molecular patterns trigger a brisk innate immune/inflammatory response** — cytokine release (IL-1β, IL-6, TNF), neutrophil recruitment, vasodilation, and increased vascular permeability. *(Inferred from toxin biology and standard inflammation pathways.)*
6. **Inflammation and edema produce the cardinal clinical signs**: erythema, warmth, swelling, pain/tenderness — the diagnosable phenotype. *(Demonstrated clinically.)*
7. **Branch A — resolution:** appropriate antibiotics + host defenses clear infection; inflammation subsides.
8. **Branch B — recurrence loop:** each episode **further damages lymphatics → worsens drainage → predisposes to the next episode** (previous cellulitis is the single strongest risk factor, OR 40.3). *(Demonstrated epidemiologically; interrupted by prophylaxis/compression; F002, F003, F009.)*
9. **Branch C — escalation to necrotizing infection:** with highly virulent strains (covR/covS mutants) or vulnerable hosts, infection **extends to fascia → necrotizing fasciitis**, a surgical emergency with tissue ischemia/necrosis. *(Demonstrated; distinguished by LRINEC score; F011.)*
10. **Branch D — host-factor amplification (diabetes):** neuropathy + peripheral arterial disease + immune impairment **allow progression** from superficial cellulitis to deep abscess, osteomyelitis, gangrene, and amputation. *(Demonstrated clinically; F010.)*

### Detail by category

- **Molecular pathways / cellular processes:** Innate inflammatory signaling — pattern-recognition (TLR) activation, inflammasome activation (IL-1β maturation), NF-κB–driven cytokine transcription; **pyroptosis** via gasdermin A (SpeB-cleaved). GO suggestions: GO:0006954 (inflammatory response), GO:0070269 (pyroptosis), GO:0050830 (defense response to Gram-positive bacterium), GO:0032611 (interleukin-1 beta production), GO:0071224 (cellular response to peptidoglycan).
- **Protein dysfunction (pathogen effectors):** SpeB is a secreted cysteine protease (gain of destructive proteolytic function on host gasdermin A); SLS is a post-translationally modified cytolytic peptide.
- **Immune system involvement:** Predominantly **acute innate inflammation** rather than autoimmunity/immunodeficiency (though host immunodeficiency raises susceptibility and severity). IL-1β is a notable mediator (F005).
- **Tissue damage mechanisms:** toxin-mediated cytolysis/pyroptosis (keratinocytes, macrophages), inflammatory edema, and — in the necrotizing branch — ischemia and necrosis.
- **Cell types (CL suggestions):** keratinocyte (CL:0000312), macrophage (CL:0000235), neutrophil (CL:0000775), dermal fibroblast (CL:0002620), lymphatic endothelial cell (CL:0002138).
- **Molecular profiling / advanced technologies:** No human transcriptomic/proteomic/metabolomic disease signatures are established for cellulitis; mechanistic omics evidence derives from pathogen models (mouse subcutaneous infection; covR/covS mutant expression profiling of SLS, F005).

---

## Section 7 — Anatomical Structures Affected

- **Organ level (primary):** skin (UBERON:0002097) — specifically the **deep dermis** (UBERON:0002067) and **subcutaneous tissue / hypodermis** (UBERON:0002072). Erysipelas involves the **upper dermis and superficial lymphatics**.
- **Most common site:** lower extremity/leg (UBERON:0000978) — 88% of lymphedema-related cellulitis admissions were lower-extremity ([PMID: 32932222](https://pubmed.ncbi.nlm.nih.gov/32932222/)).
- **Site-specific entities:** periorbital/preseptal tissue and orbit (UBERON:0001697 orbit) — periorbital vs. orbital cellulitis (F008); face; diabetic foot/hand ([PMID: 19882060](https://pubmed.ncbi.nlm.nih.gov/19882060/)).
- **Secondary/complication involvement:** lymphatic vessels (lymphangitis; UBERON:0001473), regional lymph nodes (lymphadenitis), fascia (necrotizing fasciitis; UBERON:0007844), bone (osteomyelitis in diabetic foot), bloodstream (bacteremia/sepsis), and, for orbital cellulitis, the CNS/cavernous sinus (intracranial extension).
- **Tissue types:** connective tissue (subcutis), vascular/lymphatic endothelium, epidermis (keratinocytes at barrier).
- **Subcellular (GO cellular component):** extracellular space (GO:0005615) — site of toxin action; host plasma membrane (GO:0005886) — target of pore-forming SLS/gasdermin pores.
- **Lateralization:** characteristically **unilateral** (asymmetry is a diagnostic clue — the "A" in ALT-70). Bilateral lower-leg erythema more often indicates a mimic (e.g., stasis dermatitis).

---

## Section 8 — Temporal Development

- **Onset:** **acute**, over hours to a few days. Any age; incidence increases with age and comorbidity. Periorbital cellulitis skews pediatric.
- **Progression:** rapidly progressive erythema is typical; **red-flag rapid spread with systemic toxicity, disproportionate pain, or bullae** signals possible necrotizing infection (F011).
- **Course pattern:** Individual episodes are usually **self-limited with appropriate treatment** (days to ~1–2 weeks). Over a lifetime, disease is frequently **episodic/recurrent** in patients with chronic edema.
- **Duration:** uncomplicated cellulitis treated 5–7 days; complicated/bacteremic disease longer.
- **Remission/critical periods:** Prophylaxis and compression alter the natural history of recurrence — notably, penicillin's protective effect **waned after prophylaxis stopped** (F003), indicating an ongoing-intervention-dependent window. Early recognition of the necrotizing branch is the critical time-sensitive intervention opportunity (early debridement).

---

## Section 9 — Inheritance and Population

- **Inheritance:** **None** — acquired infectious disease. No inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effects, consanguinity, or carrier frequency applies.
- **Epidemiology / burden (Finding F006):** Cellulitis/erysipelas is a frequent primary ED diagnosis. In the US National Emergency Department Sample (2006–2016, ~320 million ED visits), the mean ED-visit cost "*more than doubled in adults (from \$720 to \$1680) and tripled in children (from \$939 to \$2,823)*" ([PMID: 33238162](https://pubmed.ncbi.nlm.nih.gov/33238162/)). It is associated with public/no insurance, lower income, and weekend/summer presentation; most visits are for uncomplicated disease.
- **Lymphedema link (F006):** In the National Inpatient Sample (2012–2017), of ~165,055 lymphedema-related admissions, "*the vast majority of hospitalizations were for cellulitis (92%), lower extremity disease (88%)*" ([PMID: 32932222](https://pubmed.ncbi.nlm.nih.gov/32932222/)); inpatient mortality was low (0.03%), with age >80 (OR 3.83) and Charlson comorbidity index ≥3 (OR 4.13) predicting inpatient death.
- **Demographics:** Rises with age; strong comorbidity associations (obesity, diabetes, venous/lymphatic disease). No strong ethnic/founder predisposition (consistent with acquired etiology). Geographic variation is driven by pathogen exposure (e.g., melioidosis in Southeast Asia/northern Australia).

---

## Section 10 — Diagnostics

**Cellulitis is a clinical diagnosis** — there is no confirmatory gold-standard test. Blood and skin cultures are frequently negative (e.g., usually negative in periorbital/orbital series, [PMID: 20544674](https://pubmed.ncbi.nlm.nih.gov/20544674/)).

**Laboratory / biomarkers:** Non-specific inflammatory markers (leukocytosis, elevated CRP) support but do not confirm the diagnosis and feed prediction scores. Blood cultures are low-yield except in systemic illness.

**Clinical prediction tools (Finding F004):** The **ALT-70 model** (Asymmetry, Leukocytosis, Tachycardia, Age ≥70) "*offers an objective tool to help differentiate between cellulitis and other clinically similar conditions at the time of initial emergency department (ED) presentation*" and retains predictive value at 24 and 48 hours ([PMID: 30914341](https://pubmed.ncbi.nlm.nih.gov/30914341/)). **Dermatology consultation** frequently modifies management and reduces unnecessary antibiotics/hospitalization ([PMID: 39614879](https://pubmed.ncbi.nlm.nih.gov/39614879/)).

**Differential diagnosis (critical):** ~One-third of admitted "cellulitis" is **pseudocellulitis** — "*Inflammatory dermatoses of the lower extremity are often misdiagnosed as cellulitis (aka 'pseudocellulitis') and treated with antibiotics and/or hospitalization*" ([PMID: 27806170](https://pubmed.ncbi.nlm.nih.gov/27806170/)). Common mimics: stasis dermatitis, contact dermatitis, lipodermatosclerosis, DVT, gout, and infectious mimics (cryptococcosis [PMID: 42240944](https://pubmed.ncbi.nlm.nih.gov/42240944/), kerion/tinea [PMID: 42670489](https://pubmed.ncbi.nlm.nih.gov/42670489/)).

**The high-stakes branch — necrotizing fasciitis (Finding F011):** NF "*is a rapidly progressing infection of the soft tissues associated with high morbidity and mortality and hence it is a surgical emergency*"; the **LRINEC score ≥6** yielded a C-statistic of 0.839 (95% CI 0.682–0.995, P=0.001) for NF vs. severe cellulitis ([PMID: 36462382](https://pubmed.ncbi.nlm.nih.gov/36462382/)). Atypical pathogens (melioidosis) can mimic NSTI in endemic areas ([PMID: 41580634](https://pubmed.ncbi.nlm.nih.gov/41580634/)).

**Imaging:** Ultrasound helps exclude abscess and DVT; MRI increases sensitivity/specificity for deep involvement (osteomyelitis in diabetic foot, [PMID: 27377687](https://pubmed.ncbi.nlm.nih.gov/27377687/); intramuscular abscess in melioidosis, [PMID: 41580634](https://pubmed.ncbi.nlm.nih.gov/41580634/)); CT for orbital cellulitis and sinusitis.

**Genetic/omics diagnostics:** **Not applicable** — no role for genetic testing, karyotyping, CMA, or human omics diagnostics in cellulitis.

---

## Section 11 — Outcome / Prognosis

- **Overall prognosis is good** for uncomplicated disease. Inpatient mortality for lymphedema-related cellulitis was 0.03% (F006).
- **Recurrence** is the dominant morbidity: 33–40% of high-risk patients recur without prophylaxis (F003, F009).
- **Complications:** bacteremia/sepsis, abscess, lymphangitis, recurrent episodes with progressive lymphatic damage, necrotizing fasciitis (surgical emergency, high mortality), and — in orbital cellulitis — vision loss, intracranial extension, and death (F008, [PMID: 40642363](https://pubmed.ncbi.nlm.nih.gov/40642363/)). In diabetes, progression to osteomyelitis, gangrene, and **amputation** (digit amputation in 14.3% of a diabetic hand-sepsis series, [PMID: 19882060](https://pubmed.ncbi.nlm.nih.gov/19882060/)).
- **Prognostic factors:** advanced age (>80, OR 3.83 for inpatient mortality), comorbidity burden (Charlson ≥3, OR 4.13), diabetes, chronic kidney disease, lymphedema, and systemic inflammatory response (SIRS OR 4.43 for adverse hospital course, [PMID: 42759235](https://pubmed.ncbi.nlm.nih.gov/42759235/)). Return ED visits requiring admission in older adults carry higher in-hospital mortality, with cellulitis among the top diagnoses ([PMID: 42215907](https://pubmed.ncbi.nlm.nih.gov/42215907/)).

---

## Section 12 — Treatment

**First-line pharmacotherapy targets streptococci for non-purulent disease (Finding F007).** A multicenter double-blind RCT (5 US EDs, N=496) tested cephalexin + trimethoprim-sulfamethoxazole vs. cephalexin + placebo for uncomplicated cellulitis (abscess excluded by ultrasound) and found **no benefit from adding MRSA coverage**: "*For cellulitis without purulent drainage, β-hemolytic streptococci are presumed to be the predominant pathogens. It is unknown if antimicrobial regimens possessing in vitro MRSA activity provide improved outcomes compared with treatments lacking MRSA activity*" ([PMID: 28535235](https://pubmed.ncbi.nlm.nih.gov/28535235/)). This anchors streptococcal-targeted therapy for uncomplicated non-purulent cellulitis.

| Drug / class | Role | NCIT suggestion |
|---|---|---|
| Cephalexin (1st-gen cephalosporin) | First-line, non-purulent | NCIT:C349 |
| Dicloxacillin / flucloxacillin (anti-staph penicillin) | First-line | — |
| Penicillin V/G | Streptococcal cellulitis; prophylaxis | NCIT:C376 |
| TMP-SMX, clindamycin, doxycycline | Add for purulent/MRSA-risk | — |
| Vancomycin | Severe/IV MRSA coverage | NCIT:C932 |
| Daptomycin | Complicated SSTI (esp. elderly), incl. MRSA | — |
| Oritavancin, dalbavancin, tedizolid, ceftaroline, delafloxacin, omadacycline | Newer QIDP ABSSSI agents; single-dose options reduce admissions | — |

Supporting drug evidence: newer ABSSSI agents reviewed in [PMID: 31528278](https://pubmed.ncbi.nlm.nih.gov/31528278/); single-dose oritavancin safety in the SOLO phase 3 trials ([PMID: 29358292](https://pubmed.ncbi.nlm.nih.gov/29358292/)); daptomycin first-line in elderly complicated SSTI ([PMID: 23990341](https://pubmed.ncbi.nlm.nih.gov/23990341/)).

**Purulent cellulitis / abscess:** incision and drainage is central (I&D associated with lower odds of adverse hospital course, OR 0.16, [PMID: 42759235](https://pubmed.ncbi.nlm.nih.gov/42759235/)), plus MRSA-active antibiotics.

**Diabetic foot / severe disease (Finding F010):** mild/moderate infection is empirically treated for gram-positive cocci, whereas "*severe or infection caused by drug resistant organisms needs broad spectrum anti-microbial targeting aggressive gram-negative aerobes and obligate anaerobes*," with surgical debridement/amputation as needed ([PMID: 27377687](https://pubmed.ncbi.nlm.nih.gov/27377687/); surgical management [PMID: 18512303](https://pubmed.ncbi.nlm.nih.gov/18512303/)).

**Necrotizing fasciitis:** **early surgical debridement** is the definitive intervention alongside broad-spectrum antibiotics (F011).

**Orbital cellulitis:** IV antibiotics, ENT/ophthalmology involvement, drainage of sinus/orbital abscess when indicated (F008).

**Supportive care:** limb elevation, analgesia, treatment of the portal of entry (e.g., antifungals for tinea pedis), and edema management.

**Pharmacogenomics / advanced (gene/cell/RNA) therapeutics:** **Not applicable** to cellulitis.

---

## Section 13 — Prevention

**Primary prevention:** treat and prevent barrier breaches (tinea pedis, wounds, eczema), control chronic edema, weight management, glycemic control, and good foot/skin hygiene (targets the risk factors in F002).

**Secondary/tertiary prevention — two RCT-backed interventions:**

1. **Prophylactic low-dose penicillin V (Finding F003, PATCH I).** In a double-blind RCT of 274 patients with ≥2 leg-cellulitis episodes, penicillin V 250 mg twice daily reduced recurrence: "*During the prophylaxis phase, 30 of 136 participants in the penicillin group (22%) had a recurrence, as compared with 51 of 138 participants in the placebo group (37%) (hazard ratio, 0.55; 95% confidence interval [CI], 0.35 to 0.86; P=0.01), yielding a number needed to treat to prevent one recurrent cellulitis episode of 5*" ([PMID: 23635049](https://pubmed.ncbi.nlm.nih.gov/23635049/)). PATCH II (underpowered, n=123) was directionally concordant (HR 0.53, P=0.08, [PMID: 21910701](https://pubmed.ncbi.nlm.nih.gov/21910701/)); pooled economic analysis showed "*a 29% reduction in the number of recurrences... (IRR: 0.71 95%CI: 0.53 to 0.90, p = 0.02)*" ([PMID: 24551029](https://pubmed.ncbi.nlm.nih.gov/24551029/)). **Caveat:** protective effect waned after stopping prophylaxis.

2. **Compression therapy for chronic leg edema (Finding F009, Webb NEJM).** Single-center RCT (N=84) of compression + education vs. education alone: "*6 participants (15%) in the compression group and 17 (40%) in the control group had had an episode of cellulitis (hazard ratio, 0.23; 95% confidence interval [CI], 0.09 to 0.59; P = 0.002)*" — trial **stopped early for efficacy** ([PMID: 32786188](https://pubmed.ncbi.nlm.nih.gov/32786188/)). Extended follow-up confirmed sustained benefit and identified that "*Chronic oedema is a key modifiable risk factor for incident and recurrent cellulitis*" ([PMID: 42597865](https://pubmed.ncbi.nlm.nih.gov/42597865/)); compression is cost-saving ([PMID: 35997601](https://pubmed.ncbi.nlm.nih.gov/35997601/)).

**Immunization (Finding F008, site-specific).** The **Haemophilus influenzae type b (Hib) vaccine** dramatically reduced Hib-related periorbital/orbital cellulitis: "*The introduction of the Hib vaccine coincided with a sharp decline not only in the number of periorbital and orbital cellulitis cases related to H. influenzae, but also in the annual case rate*" ([PMID: 10919886](https://pubmed.ncbi.nlm.nih.gov/10919886/)); "*H influenzae type b is no longer a significant pathogen in periorbital or orbital cellulitis*" ([PMID: 9310918](https://pubmed.ncbi.nlm.nih.gov/9310918/)). No vaccine exists for streptococcal/staphylococcal cellulitis generally.

**Genetic screening/counseling:** **Not applicable.**

---

## Section 14 — Other Species / Natural Disease

Cellulitis as a bacterial soft-tissue infection occurs naturally across many mammals. A documented veterinary example: in stocker cattle, **interdigital necrobacillosis (foot rot)** is a polymicrobial interdigital infection where "*breach of skin allows bacteria to cause cellulitis, septic arthritis, and lameness*," implicating *Fusobacterium necrophorum*, with prevention via hygiene and possible *F. necrophorum* vaccination ([PMID: 42309844](https://pubmed.ncbi.nlm.nih.gov/42309844/)). This mirrors the human "barrier-breach → cellulitis" mechanism.

- **Taxonomy of affected species:** broad — cattle (*Bos taurus*, txid9913), and companion animals (dogs *Canis lupus familiaris* txid9615, cats *Felis catus* txid9685) develop bacterial cellulitis/abscesses from bites and wounds.
- **Comparative biology:** the core mechanism (skin breach + bacterial invasion + inflammation) is evolutionarily conserved; pathogen species differ (e.g., *Fusobacterium* in bovine foot rot).
- **Zoonotic/transmission:** cellulitis itself is not person-to-person transmissible; zoonotic relevance is via animal-bite inoculation (e.g., *Pasteurella*) and shared environmental pathogens.

Orthologous "disease genes" are not applicable (no human causal genes). Model-organism pathogen genes (murine GAS infection) are covered in Section 15.

---

## Section 15 — Model Organisms

- **Mouse subcutaneous infection model (primary mechanistic system; Finding F005).** In this model, GAS with covR/covS mutations cause severe local skin lesions; "*SpeB-mediated gasdermin A cleavage triggers keratinocyte death, resulting in sizeable lesion size but preventing invasive skin infection by GAS*," and streptolysin S drives keratinocyte/macrophage death and IL-1β. Causality was demonstrated by loss-of-function: "*In a mouse subcutaneous infection model, the SLS-deficient ∆covR mutant exhibited reduced lesion size and mortality compared to the ∆covR mutant*" ([PMID: 41175456](https://pubmed.ncbi.nlm.nih.gov/41175456/)). Model type: mammalian (*Mus musculus*, txid10090), induced by bacterial inoculation, using bacterial genetic knockouts (Δ*covR*, SLS-deficient).
- **Diabetic infection models** support the host-factor branch, e.g., staphylococcal ClpX-dependent regulatory pathways exacerbating infection in diabetes ([PMID: 42262120](https://pubmed.ncbi.nlm.nih.gov/42262120/)).
- **Phenotype recapitulation:** murine subcutaneous models reproduce local lesion formation, toxin-driven cell death, and virulence-regulator effects well, enabling dissection of pathogen mechanisms.
- **Limitations:** these are **pathogen-mechanism models**, not models of the human host-susceptibility phenotype (chronic edema, lymphedema, recurrence). The two dominant clinical drivers — impaired drainage and recurrence — are not fully captured by acute murine inoculation models. Human disease is not driven by host genetics, so there are no "disease-gene knockout" mouse models of cellulitis per se.

---

## Mechanistic Model / Interpretation

```
   BARRIER BREACH                         IMPAIRED DRAINAGE
 (tinea pedis, wound,                (lymphedema, chronic edema,
  ulcer, excoriation)                 venous insufficiency, obesity)
   OR up to 40.3 (prior              OR ~2.7-6.8 (lymphedema/edema,
   cellulitis), 19.1 (wound)               varicose veins)
         |                                        |
         +------------------+---------------------+
                            v
              BACTERIAL ENTRY & PROLIFERATION
        (beta-hemolytic streptococci [non-purulent];
              S. aureus/MRSA [purulent])
                            v
        VIRULENCE FACTORS (GAS covR/covS mutants):
        SpeB -> gasdermin A cleavage -> keratinocyte pyroptosis
        Streptolysin S -> keratinocyte/macrophage death, IL-1beta
                            v
             INNATE INFLAMMATION + EDEMA
                            v
      ERYTHEMA + WARMTH + SWELLING + PAIN (unilateral)
                            |
     +----------------------+----------------------+-------------------+
     v                      v                      v                   v
  RESOLUTION           RECURRENCE LOOP        NECROTIZING           DIABETIC
 (antibiotics +     (lymphatic damage ->     FASCIITIS            ESCALATION
  host defense)      worse drainage ->      (fascia; LRINEC>=6;   (osteomyelitis,
                     next episode)           surgical emergency)   gangrene,
                     PREVENT: penicillin                           amputation)
                     (HR 0.55) & compression
                     (HR 0.23)
```

The unifying insight is that cellulitis is a **"two-hit" disease**: neither a barrier breach nor impaired drainage alone reliably causes it, but together they establish infection. This explains why the most effective preventive strategies target the *host substrate* (compression for edema) and *bacterial persistence/recolonization* (penicillin prophylaxis) rather than any intrinsic host genetics. It also explains the self-perpetuating recurrence loop (prior cellulitis = strongest risk factor) via cumulative lymphatic injury.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [42711142](https://pubmed.ncbi.nlm.nih.gov/42711142/) | *Non-Purulent Cellulitis—An Updated Review* | F001 microbiology |
| [42727947](https://pubmed.ncbi.nlm.nih.gov/42727947/) | *Advances in diagnosis/management of SSTI* | F001 purulent vs non-purulent |
| [27864837](https://pubmed.ncbi.nlm.nih.gov/27864837/) | *Risk factors for nonpurulent leg cellulitis (meta-analysis)* | F002 risk factors |
| [29427797](https://pubmed.ncbi.nlm.nih.gov/29427797/) | *Severe lower limb cellulitis case-control* | F002 risk factors |
| [23635049](https://pubmed.ncbi.nlm.nih.gov/23635049/) | *Penicillin to prevent recurrent leg cellulitis (PATCH I)* | F003 prophylaxis |
| [24551029](https://pubmed.ncbi.nlm.nih.gov/24551029/) | *PATCH I&II economic analysis* | F003 pooled effect |
| [21910701](https://pubmed.ncbi.nlm.nih.gov/21910701/) | *PATCH II trial* | F003 corroboration |
| [39614879](https://pubmed.ncbi.nlm.nih.gov/39614879/) | *Dermatology consultation/diagnostic stewardship* | F004 diagnosis |
| [30914341](https://pubmed.ncbi.nlm.nih.gov/30914341/) | *ALT-70 model at 24/48h* | F004 prediction tool |
| [27806170](https://pubmed.ncbi.nlm.nih.gov/27806170/) | *Costs of misdiagnosed cellulitis (pseudocellulitis)* | F004 mimics |
| [41175456](https://pubmed.ncbi.nlm.nih.gov/41175456/) | *Streptolysin S / covR-covS keratinocyte death* | F005 mechanism |
| [33238162](https://pubmed.ncbi.nlm.nih.gov/33238162/) | *Burden of cellulitis/erysipelas in US ED* | F006 burden |
| [32932222](https://pubmed.ncbi.nlm.nih.gov/32932222/) | *Epidemiology of lymphedema admissions* | F006 lymphedema link |
| [28535235](https://pubmed.ncbi.nlm.nih.gov/28535235/) | *Cephalexin ± TMP-SMX RCT* | F007 treatment |
| [20544674](https://pubmed.ncbi.nlm.nih.gov/20544674/) | *Periorbital/orbital cellulitis 10-yr review* | F008 site-specific |
| [10919886](https://pubmed.ncbi.nlm.nih.gov/10919886/) | *Pre/post Hib vaccination cellulitis* | F008 vaccine prevention |
| [9310918](https://pubmed.ncbi.nlm.nih.gov/9310918/) | *Periorbital/orbital cellulitis in Hib vaccine era* | F008 corroboration |
| [32786188](https://pubmed.ncbi.nlm.nih.gov/32786188/) | *Compression therapy RCT (NEJM)* | F009 prevention |
| [42597865](https://pubmed.ncbi.nlm.nih.gov/42597865/) | *Sustained benefit of compression (follow-up)* | F009 durability |
| [35997601](https://pubmed.ncbi.nlm.nih.gov/35997601/) | *Compression is cost-saving* | F009 economics |
| [27377687](https://pubmed.ncbi.nlm.nih.gov/27377687/) | *Understanding diabetic foot infection* | F010 diabetic branch |
| [19882060](https://pubmed.ncbi.nlm.nih.gov/19882060/) | *Hand sepsis in diabetes* | F010 amputation risk |
| [36462382](https://pubmed.ncbi.nlm.nih.gov/36462382/) | *LRINEC/SIARI validation for NF* | F011 diagnosis branch |
| [41580634](https://pubmed.ncbi.nlm.nih.gov/41580634/) | *Melioidosis mimicking NSTI* | F011 mimics |
| [31528278](https://pubmed.ncbi.nlm.nih.gov/31528278/) | *New ABSSSI drugs* | Treatment options |
| [29358292](https://pubmed.ncbi.nlm.nih.gov/29358292/) | *Oritavancin SOLO safety* | Single-dose therapy |
| [23990341](https://pubmed.ncbi.nlm.nih.gov/23990341/) | *Daptomycin in elderly cSSTI* | Treatment (elderly) |
| [42759235](https://pubmed.ncbi.nlm.nih.gov/42759235/) | *ED disposition/resource use for SSTI* | Prognostic factors |
| [42309844](https://pubmed.ncbi.nlm.nih.gov/42309844/) | *Non-respiratory diseases of stocker cattle* | Veterinary/comparative |

---

## Limitations and Knowledge Gaps

1. **Microbiology is largely inferential.** Because cultures are frequently negative in non-purulent cellulitis, the streptococcal predominance is "presumed" from serology, syndromic association, and treatment-response data rather than direct isolation in most patients.
2. **Mechanistic depth comes from pathogen models, not human tissue.** The SpeB/gasdermin A and streptolysin S mechanisms (F005) derive from mouse subcutaneous infection with hypervirulent covR/covS mutants — informative for severe/necrotizing GAS disease but not necessarily representative of ordinary streptococcal cellulitis. No human transcriptomic/proteomic/metabolomic disease signature was identified.
3. **Prevention evidence has scale limits.** The compression RCT (F009) is single-center (N=84, stopped early — early-stopped trials can overestimate effect); PATCH II was underpowered. Penicillin's benefit does not persist after stopping.
4. **Recurrence biology is under-characterized.** The lymphatic-damage recurrence loop is well-supported epidemiologically (prior cellulitis OR 40.3) but the molecular mechanism of episode-induced lymphatic injury is inferred, not directly demonstrated in humans.
5. **No genetic/omics dimension.** Sections on causal genes, variants, inheritance, genetic testing, and pharmacogenomics are genuinely not applicable, consistent with an acquired infection.
6. **Heterogeneous case definitions.** "Cellulitis/erysipelas" grouping and variable coding across administrative datasets limit precision of burden and outcome estimates.

---

## Proposed Follow-up Experiments / Actions

1. **Implement and audit ALT-70 (± LRINEC) at ED triage** to reduce pseudocellulitis over-treatment and to systematically flag necrotizing infection; measure impact on antibiotic days and admissions (F004, F011).
2. **Pragmatic multicenter RCT of combined compression + penicillin prophylaxis** vs. each alone in recurrent leg cellulitis with chronic edema, powered for time-to-recurrence and cost — the two proven interventions have never been directly compared or combined at scale (F003, F009).
3. **Trial of continued vs. tapered penicillin prophylaxis** to address the waning-benefit problem (define optimal duration and identify who can safely stop).
4. **Human mechanistic study of lymphatic function across cellulitis episodes** (e.g., lymphoscintigraphy before/after an episode) to test the hypothesized episode-induced lymphatic-damage recurrence loop.
5. **Skin/blood molecular profiling (transcriptomics, host biomarkers)** in culture-negative non-purulent cellulitis vs. pseudocellulitis to develop an objective diagnostic biomarker.
6. **Structured tinea pedis / interdigital-barrier eradication program** in high-risk (edema/diabetic) patients as a primary-prevention intervention, with cellulitis incidence as the endpoint (targets the barrier-breach hit; F002).
7. **Diabetic foot pathway optimization** integrating early MRI and multidisciplinary surgical review to reduce progression from cellulitis to amputation (F010).

---

*Report generated from a 5-iteration autonomous discovery investigation: 11 confirmed findings, 52 papers reviewed. Evidence types span human clinical RCTs and observational studies (F001–F004, F006–F011) and mouse/in-vitro pathogen-mechanism studies (F005).*


## Artifacts

- [OpenScientist final report](Cellulitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Cellulitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 39 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 11 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 39 |
| On topic | 20 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:23635049` *(abstract only)*: "*During the prophylaxis phase, 30 of 136 participants in the penicillin group (22%) had a recurrence, as compared with 51 of 138 participants in the placebo group (37%) (hazard ratio, 0.55; 95% confidence interval [CI], 0.35 to 0.86; P=0.01), yielding a number needed to treat to prevent one recurrent cellulitis episode of 5*"
  - closest text in source: "During the prophylaxis phase, 30 of 136 participants in the penicillin group (22%) had a recurrence, as compared with 51 of 138 participants in the placebo group (37%) (hazard ratio, 0.55; 95% confidence interval [CI], 0.35 to 0.86; P=0.01), yielding a number needed to treat to prevent one recurrent cellulitis episode of 5 (95% CI, 4 to 9)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 21 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005230` (2 mentions) - the report calls it "MONDO"; MONDO calls it **cellulitis**
- `NCIT:C349` (1 mention) - the report calls it "First-line, non-purulent"; NCIT calls it **Carmustine**
- `NCIT:C376` (1 mention) - the report calls it "Streptococcal cellulitis; prophylaxis"; NCIT calls it **Cisplatin**
- `NCIT:C932` (1 mention) - the report calls it "Severe/IV MRSA coverage"; NCIT calls it **Vinca Alkaloid Compound**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011121` (1 mention) - the report calls it "Abnormality of skin morphology"; HP calls it **Abnormal skin morphology**, and lists "Abnormality of skin morphology" among its other names
- `HP:0025280` (1 mention) - the report calls it "Pain"; HP calls it **Pain characteristic**
- `HP:0001974` (1 mention) - the report calls it "Leukocytosis"; HP calls it **Increased total leukocyte count**, and lists "Leukocytosis" among its other names
- `GO:0070269` (1 mention) - the report calls it "pyroptosis"; GO calls it **pyroptotic inflammatory response**, and lists "pyroptosis" among its other names
- `UBERON:0002067` (1 mention) - the report calls it "deep dermis"; UBERON calls it **dermis**
- `UBERON:0002072` (1 mention) - the report calls it "subcutaneous tissue / hypodermis"; UBERON calls it **hypodermis**, and lists "subcutaneous tissue" among its other names
- `UBERON:0000978` (1 mention) - the report calls it "Most common site:** lower extremity/leg"; UBERON calls it **leg**, and lists "lower extremity" among its other names