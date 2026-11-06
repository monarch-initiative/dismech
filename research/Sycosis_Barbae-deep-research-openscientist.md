---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T14:00:41.369332'
end_time: '2026-09-29T14:23:39.165693'
duration_seconds: 1377.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Sycosis Barbae
  mondo_id: MONDO:1050000
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
citation_count: 19
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 22
  quotes_valid: 22
  relevance_assessed: 19
  on_topic: 5
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 21
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 2
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Sycosis_Barbae-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Sycosis_Barbae-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sycosis Barbae
- **MONDO ID:** MONDO:1050000 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Sycosis Barbae** covering all of the
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

# Sycosis Barbae — Comprehensive Disease Characteristics Report

**Disease:** Sycosis Barbae (staphylococcal beard folliculitis)
**MONDO ID:** MONDO:1050000 (as provided)
**Category:** Infectious Disease
**Evidence base:** 11 confirmed findings, 46 papers reviewed, 5 investigation iterations
**Report type:** Literature-based disease knowledge-base entry. No primary datasets were provided; all content is derived from aggregated, disease-level resources (PubMed primary literature, ontologies, clinical references), not from individual patient/EHR data.

---

## Summary

**Sycosis barbae is a chronic, deep-seated bacterial (staphylococcal) folliculitis and perifolliculitis of the bearded skin of adult men.** It is caused by *Staphylococcus aureus* infecting terminal beard-hair follicles that have been rendered susceptible by shaving-induced follicular microtrauma. The disease lies on a severity continuum: it begins as a superficial folliculitis barbae (Bockhart impetigo), and if untreated deepens into sycosis barbae, then can progress to furuncles (boils) and coalescing carbuncles with occasional systemic upset. A chronic variant, **lupoid sycosis**, produces scarring (cicatricial) alopecia and permanent cosmetic disfigurement of the beard ([PMID: 25226722](https://pubmed.ncbi.nlm.nih.gov/25226722/)).

Mechanistically, the disease follows a well-defined causal chain drawn largely from murine *S. aureus* skin-infection models plus human genetics: shaving microtrauma and follicular *S. aureus* colonization → bacterial breach of the follicular epithelium → secreted toxins (phenol-soluble modulins, α-hemolysin) trigger innate immune sensing → MyD88/EGR1-dependent recruitment of neutrophils, amplified by T-cell-derived IL-17A and IL-22 → neutrophils wall bacteria into a perifollicular abscess (furuncle) → α-hemolysin-mediated dermonecrosis causes tissue damage. Failure of clearance—because of host neutrophil/immune defects or persistent nasal carriage—produces the chronic, relapsing course ([PMID: 34873293](https://pubmed.ncbi.nlm.nih.gov/34873293/); [PMID: 26351278](https://pubmed.ncbi.nlm.nih.gov/26351278/); [PMID: 32946878](https://pubmed.ncbi.nlm.nih.gov/32946878/); [PMID: 25681348](https://pubmed.ncbi.nlm.nih.gov/25681348/)).

Sycosis barbae is an **acquired infection with no Mendelian/genetic basis and no available vaccine**. Diagnosis is primarily clinical, supplemented by Gram stain and bacterial culture, with KOH/fungal culture and dermatophyte PCR used to exclude the principal infectious mimic, **tinea barbae**, and clinical judgment to exclude the non-infectious mimic **pseudofolliculitis barbae** and the viral mimic **herpetic sycosis**. Treatment combines anti-staphylococcal antibiotics (topical for limited disease, systemic for deep/extensive disease), incision and drainage of fluctuant lesions, *S. aureus* decolonization, and shaving modification. Prognosis is benign with respect to mortality but prone to chronicity and relapse while shaving and nasal carriage persist.

---

## Key Findings

### F001 — Sycosis barbae is a deep-seated staphylococcal folliculitis of the beard

Sycosis barbae is defined as a chronic, deep, perifollicular bacterial infection of the bearded region, representing the deep progression of a superficial folliculitis barbae (Bockhart impetigo). The most common etiologic agent is *Staphylococcus aureus*, and the condition is precipitated and aggravated by shaving. Untreated superficial folliculitis can deepen into sycosis barbae, and coalescing perifollicular nodules (furuncles) can progress to carbuncles with systemic upset.

> "It most frequently presents as a superficial folliculitis, with fine pustules appearing at the opening of hair follicles in the beard area, often associated with shaving; known as Bockhart impetigo and usually due to infection caused by Staphylococcus aureus. If untreated, the infection and inflammation can progress, leading to a more deeply seated infection known as sycosis barbae." — [PMID: 25226722](https://pubmed.ncbi.nlm.nih.gov/25226722/)

This establishes the core definition, the causative organism, the severity continuum, and the shaving trigger that organize the rest of this report.

### F002 — Tinea barbae is the principal infectious mimic

Deep beard-area infections that resemble sycosis barbae or a carbuncle can also be caused by dermatophytes (**tinea barbae**), most often zoophilic *Trichophyton* species (e.g., *T. mentagrophytes*, *T. verrucosum*) acquired through animal/livestock contact, and occasionally anthropophilic species (*T. rubrum*, *T. tonsurans*—the latter transmissible via contaminated barbershop tools). Clues favoring tinea barbae over bacterial sycosis include close animal contact, lack of response to antibiotics, deep boggy nodules/pustules with adherent crusts, and regional lymphadenopathy. An intense inflammatory reaction can form a kerion. Diagnosis requires mycological culture, histology, and dermatophyte PCR; treatment is systemic antifungals (terbinafine/itraconazole) ± corticosteroids, and surgical incision is contraindicated.

> "Particularly in the context of a history of close animal contact or a lack of response to antibiotic treatment, a diagnosis of tinea barbae should be considered and investigated." — [PMID: 25226722](https://pubmed.ncbi.nlm.nih.gov/25226722/)

> "Often this leads to the initial suspected diagnosis of a bacterial folliculitis barbae or impetigo contagiosa." — [PMID: 31001659](https://pubmed.ncbi.nlm.nih.gov/31001659/)

### F003 — Pseudofolliculitis barbae is the main non-infectious differential and has a genetic basis

**Pseudofolliculitis barbae (PFB)** is a chronic inflammatory disorder of the beard caused by shaved curly hairs re-penetrating the skin (extrafollicular and transfollicular penetration), producing a foreign-body inflammatory reaction with papules, pustules, post-inflammatory hyperpigmentation, and sometimes keloidal scarring. It is far more common in men of African and Asian ancestry. Unlike infectious sycosis barbae, PFB is mechanical/foreign-body rather than infectious. A single-nucleotide substitution (A12T) in the hair-follicle companion-layer keratin gene **K6hf (KRT75)** confers roughly six-fold increased risk of PFB.

> "Individuals with the single nucleotide substitution in the hair follicle companion layer specific keratin gene (K6hf) have a six fold increased chance of developing PFB." — [PMID: 31354326](https://pubmed.ncbi.nlm.nih.gov/31354326/)

> "Pseudofolliculitis barbae (PFB) is an inflammatory condition of the beard area, with a high prevalence in men of subequatorial African ancestry" — [PMID: 27212468](https://pubmed.ncbi.nlm.nih.gov/27212468/)

### F004 — S. aureus nasal carriage and host immune factors drive recurrent/chronic disease

*S. aureus* is the dominant pathogen of pilosebaceous-unit infections (folliculitis, furunculosis, carbunculosis). Its invasiveness depends on numerous cellular and extracellular virulence factors whose expression varies with growth phase, environment, and infection site; host susceptibility reflects innate and acquired immune responses to colonization. Recurrent/chronic disease is associated with *S. aureus* reservoirs (notably the anterior nares) and with host defects—for example, documented recurrent furunculosis with defective neutrophil phagocytic (ingestion-phase) activity, in whom early antibiotics and intensified hygiene reduced abscess formation.

> "S. aureus produces a great variety of cellular and extracellular factors responsible for its invasiveness and ability to cause pathological lesions. Their expression depends on the growth phase, environmental factors, and location of the infection." — [PMID: 30995649](https://pubmed.ncbi.nlm.nih.gov/30995649/)

> "All laboratory tests were normal except for a decrease of the neutrophil phagocytic ingestion phase." — [PMID: 11269901](https://pubmed.ncbi.nlm.nih.gov/11269901/)

### F005 — Management combines antibiotics with decolonization and shaving hygiene

First-line therapy for bacterial sycosis barbae targets *S. aureus*: topical antibiotics (e.g., mupirocin, fusidic acid) for limited disease and systemic anti-staphylococcal antibiotics for deeper/extensive disease, plus incision and drainage of fluctuant furuncles/carbuncles. Because colonization is an early, critical step and more than half of patients with staphylococcal skin and soft tissue infection (SSTI) experience recurrence (often clustering in households), recurrence prevention emphasizes **decolonization**: intranasal mupirocin plus antiseptic washes (chlorhexidine or dilute bleach baths) for the patient and household members, hygiene optimization, and avoiding shared personal items. Beard-specific measures include temporarily stopping shaving and not sharing razors. Importantly, decolonization reliably reduces colonization but has **variable** effect on recurrence, with sustained/periodic regimens showing the most benefit.

> "A recommended decolonization regimen includes application of intranasal mupirocin and antiseptic body washes with chlorhexidine or dilute bleach water baths." — [PMID: 30859379](https://pubmed.ncbi.nlm.nih.gov/30859379/)

> "More than half of patients experiencing SSTI will have at least one recurrent infection. These infections frequently cluster in households." — [PMID: 30859379](https://pubmed.ncbi.nlm.nih.gov/30859379/)

> "Despite successful decolonization, the rate of SSTI recurrence did not decrease." — [PMID: 27820584](https://pubmed.ncbi.nlm.nih.gov/27820584/)

### F006 — Mechanistic causal chain: toxins → innate sensing → neutrophilic follicular abscess

The pathophysiology follows a defined causal chain (largely from mouse SSTI models plus human genetics), described in full in the Mechanistic Model section below. Key experimentally supported steps: phenol-soluble modulins (PSMs) directly recruit leukocytes via an EGR1-dependent "high-alert" mechanism; MyD88-dependent sensing by dermal macrophages escalates and terminates neutrophil recruitment; T-cell-derived IL-17A and IL-22 drive neutrophil infiltration and antimicrobial peptide production; neutrophils wall bacteria into a discrete abscess; and α-hemolysin causes dermonecrosis, with antibody neutralization plus early neutrophil recruitment limiting necrosis.

> "this early recruitment was dependent on the transcription factor EGR1 and contributed to the prevention of infection" — [PMID: 34873293](https://pubmed.ncbi.nlm.nih.gov/34873293/)

> "Neutralization of either IL-17A or IL-22 reduced T cell and neutrophil infiltration and host defense peptide elaboration in lesions. These events corresponded with increased abscess severity, MRSA viability, and CFU density in skin." — [PMID: 26351278](https://pubmed.ncbi.nlm.nih.gov/26351278/)

> "Protection was characterized by robust neutrophilic inflammation and compartmentalization of bacteria into discrete abscesses" — [PMID: 32946878](https://pubmed.ncbi.nlm.nih.gov/32946878/)

> "MyD88-dependent sensing of S. aureus by dermal macrophages (Mϕ) contributes to both timely escalation and termination of PML-mediated inflammation" — [PMID: 25681348](https://pubmed.ncbi.nlm.nih.gov/25681348/)

### F007 — Comparative disease: staphylococcal superficial bacterial folliculitis in animals

An analogous staphylococcal folliculitis occurs naturally in other species. In dogs, **superficial bacterial folliculitis (SBF)** is the most common bacterial skin disease and is caused principally by *Staphylococcus pseudintermedius* (NCBI Taxonomy txid283734), with histology showing neutrophilic follicular/intracorneal pustules containing intracellular cocci within neutrophils—mirroring the neutrophilic follicular inflammation of human sycosis barbae. Methicillin-resistant *S. pseudintermedius* (MRSP) and MRSA are increasingly prevalent, driving reliance on culture-guided systemic antibiotics plus topical antiseptics (dilute sodium hypochlorite/bleach, chlorhexidine, benzoyl peroxide)—the same topical antiseptic principles used in human decolonization.

> "Superficial bacterial folliculitis (SBF) is more common in the dog than other mammalian species." — [PMID: 24345778](https://pubmed.ncbi.nlm.nih.gov/24345778/)

> "Cytology from the margins of collarettes identified neutrophils, extracellular and intracellular cocci within neutrophils" — [PMID: 27426474](https://pubmed.ncbi.nlm.nih.gov/27426474/)

> "methicillin resistant Staphylococcus pseudintermedius (MRSP) and Staphylococcus aureus (MRSA) are becoming more prevalent in canine SBF cases" — [PMID: 24345778](https://pubmed.ncbi.nlm.nih.gov/24345778/)

### F011 — Herpetic sycosis (HSV) is a viral mimic requiring antivirals

A third important differential of beard folliculitis is **herpetic sycosis**—a follicular infection of the beard caused by herpes simplex virus (HSV-1 or HSV-2), a variant of herpetic folliculitis. It presents with acutely developing grouped papulovesicles/pustules, pain, crusting, and reactive cervical lymphadenopathy, and characteristically **fails to respond to antibacterial and antifungal therapy**. It occurs in immunocompromised and immunocompetent hosts and may be primary or recurrent/relapsing. Routine bacterial, mycological, and Tzanck tests may be negative; diagnosis is confirmed by Tzanck cytology, direct immunofluorescence, viral culture, or (most sensitively) HSV PCR. Treatment is systemic antivirals (aciclovir/valaciclovir), with rapid resolution.

> "We describe an otherwise healthy young adult male with extensive herpetic sycosis of the beard area, which is a variant of herpetic folliculitis." — [PMID: 11896419](https://pubmed.ncbi.nlm.nih.gov/11896419/)

> "The possibility of a herpetic sycosis of the beard must be considered in the case of non-response to antibiotic or antifungal treatment." — [PMID: 15118392](https://pubmed.ncbi.nlm.nih.gov/15118392/)

> "Bacteriological, mycological and Tzanck tests from the lesions were negative... nested PCR technique (nPCR) demonstrated the presence of herpes simplex virus type 2" — [PMID: 15564209](https://pubmed.ncbi.nlm.nih.gov/15564209/)

---

## Report by Template Section

### 1. Disease Information

Sycosis barbae is a chronic, deep-seated staphylococcal folliculitis and perifolliculitis of the bearded skin of the face and neck in adult men. It represents the deep progression of superficial folliculitis barbae (Bockhart impetigo) and can advance to furuncles and carbuncles ([PMID: 25226722](https://pubmed.ncbi.nlm.nih.gov/25226722/)).

**Key identifiers** (aggregated ontology/terminology resources; to be verified against source browsers):
- **MONDO:** MONDO:1050000 (as provided)
- **ICD-10:** L73.8 "Other specified follicular disorders" (sycosis barbae, non-parasitic sycosis)
- **ICD-9:** 704.8
- **SNOMED CT:** concept "Sycosis barbae"
- **MeSH:** no dedicated descriptor; indexed under *Folliculitis* (D005499) / *Staphylococcal Skin Infections* (D013207)
- **OMIM:** none (non-Mendelian, acquired infection)

**Synonyms / alternative names:** sycosis vulgaris, non-parasitic sycosis, staphylogenous sycosis, folliculitis barbae (staphylococcal), and the lay term "barber's itch" (note: "barber's itch" is also historically applied to tinea barbae, causing ambiguity).

**Information source type:** derived from aggregated disease-level clinical and textbook description, case reports, and mechanistic model-organism studies—not from individual-patient EHR datasets or disease registries.

### 2. Etiology

**Causal factors:** Sycosis barbae is a multifactorial acquired infection. The necessary agent is *Staphylococcus aureus* (infectious; NCBI Taxonomy txid1280) acting on beard follicles primed by a mechanical trigger (shaving-induced follicular microtrauma). There is **no Mendelian/causal gene**; it is not heritable.

**Risk factors (environmental/host):** male sex with post-pubertal terminal beard hair; regular shaving (especially close/against-the-grain shaving, shared or contaminated razors); *S. aureus* nasal/skin carriage (anterior nares reservoir); coexisting pseudofolliculitis barbae or atopic dermatitis; immunosuppression/diabetes and neutrophil-function defects predisposing to recurrent staphylococcal disease ([PMID: 11269901](https://pubmed.ncbi.nlm.nih.gov/11269901/)); warm humid climate and poor hygiene; barbershop exposure.

**Genetic risk factors:** none for bacterial sycosis barbae. (The related mechanical mimic PFB carries the KRT75/K6hf A12T variant conferring ~6-fold risk — [PMID: 31354326](https://pubmed.ncbi.nlm.nih.gov/31354326/).)

**Protective factors (environmental/behavioral):** growing a beard / cessation of shaving; single-use clean razors; pre-shave hydration and post-shave moisturization; good hygiene; *S. aureus* decolonization. No genetic protective variants are described.

**Gene-environment interaction:** No specific GxE is established for bacterial sycosis barbae. The closely related mechanical mimic PFB shows a clear GxE—a KRT75 (K6hf) A12T variant (curly-hair/follicle-curvature phenotype) combined with the environmental exposure of shaving produces ~6-fold risk; secondary *S. aureus* infection of PFB lesions links the two conditions ([PMID: 31354326](https://pubmed.ncbi.nlm.nih.gov/31354326/)).

### 3. Phenotypes

Clinical signs and symptoms (from clinical description; [PMID: 25226722](https://pubmed.ncbi.nlm.nih.gov/25226722/)):

| Phenotype | Type | HPO suggestion | Characteristics |
|---|---|---|---|
| Follicular papules/pustules centered on beard hairs | Clinical sign | Folliculitis (HP:0025084); Pustule (HP:0200037); Papule (HP:0200034) | Adult-onset; mild–moderate; the defining lesion |
| Perifollicular erythema, edema, crusting | Clinical sign | — | Episodic/fluctuating with shaving |
| Pruritus and burning/tenderness | Symptom | Pruritus (HP:0000989) | Common; affects daily comfort |
| Deep nodules (furuncles) coalescing into carbuncles | Physical manifestation | — | Moderate–severe; may cause systemic upset |
| Sinus tracts / scarring / cicatricial alopecia (lupoid sycosis) | Physical manifestation | Alopecia (HP:0001596) | Chronic variant; permanent hair loss |

**Age of onset:** post-pubertal adult men (essentially absent prepubertally and in women). **Severity:** variable (mild superficial to severe deep/scarring). **Progression:** episodic/fluctuating while shaving continues; chronic and relapsing in lupoid sycosis. **Quality of life:** cosmetic disfigurement of the beard, psychosocial distress, and functional discomfort (pruritus, tenderness), particularly in the scarring lupoid variant.

### 4. Genetic/Molecular Information

**Not applicable as a genetic disease.** Sycosis barbae has no causal gene, no pathogenic germline/somatic variants, no modifier genes, no disease-defining epigenetic changes, and no chromosomal abnormalities. It is an acquired bacterial infection. The relevant "molecular information" is microbial: *S. aureus* virulence factors (phenol-soluble modulins, α-hemolysin/Hla, and numerous growth-phase- and site-dependent factors) drive pathology ([PMID: 30995649](https://pubmed.ncbi.nlm.nih.gov/30995649/); [PMID: 34873293](https://pubmed.ncbi.nlm.nih.gov/34873293/); [PMID: 32946878](https://pubmed.ncbi.nlm.nih.gov/32946878/)). For completeness, the related mimic PFB has a host keratin variant, KRT75 (K6hf) A12T ([PMID: 31354326](https://pubmed.ncbi.nlm.nih.gov/31354326/)).

### 5. Environmental Information

- **Environmental/mechanical factors:** shaving (follicular microtrauma), shared/contaminated razors and barbershop tools, warm humid climate.
- **Lifestyle factors:** shaving practices and personal hygiene; barbershop attendance.
- **Infectious agents:** *Staphylococcus aureus* (NCBI Taxonomy txid1280) is the primary agent. Mimics that must be distinguished are dermatophytes (tinea barbae: *Trichophyton mentagrophytes*, *T. verrucosum*, *T. rubrum*, *T. tonsurans*) and herpes simplex virus (herpetic sycosis) ([PMID: 25226722](https://pubmed.ncbi.nlm.nih.gov/25226722/); [PMID: 11896419](https://pubmed.ncbi.nlm.nih.gov/11896419/)).

### 6. Mechanism / Pathophysiology

**Ordered causal chain** (steps largely demonstrated in murine SSTI models plus human genetics; inferred steps flagged):

1. Shaving produces follicular microtrauma **and** *S. aureus* colonizes the beard follicle → **leads to** bacterial breach of the follicular epithelium into the dermis (*inferred* for the beard specifically, extrapolated from SSTI biology).
2. Secreted **phenol-soluble modulins (PSMs)** directly recruit circulating leukocytes via an **EGR1-dependent** "high-alert" mechanism → **results in** early neutrophil influx ([PMID: 34873293](https://pubmed.ncbi.nlm.nih.gov/34873293/)).
3. **MyD88-dependent sensing** of *S. aureus* by resident dermal macrophages → **escalates and later terminates** polymorphonuclear leukocyte (neutrophil) recruitment ([PMID: 25681348](https://pubmed.ncbi.nlm.nih.gov/25681348/)).
4. T-cell-derived **IL-17A and IL-22** → **drive** neutrophil infiltration and antimicrobial host-defense-peptide production; their neutralization increases abscess severity and bacterial burden ([PMID: 26351278](https://pubmed.ncbi.nlm.nih.gov/26351278/)).
5. Neutrophils **wall off** bacteria into a discrete perifollicular abscess (furuncle) ([PMID: 32946878](https://pubmed.ncbi.nlm.nih.gov/32946878/)).
6. Pore-forming toxin **α-hemolysin (Hla)** → **causes** dermonecrosis and tissue damage; antibody neutralization of Hla plus early neutrophil recruitment limits necrosis and enhances clearance ([PMID: 32946878](https://pubmed.ncbi.nlm.nih.gov/32946878/)).
7. **Branch:** coalescence of abscesses → **yields** a carbuncle; failure of clearance (host neutrophil/immune defects, persistent nasal carriage) → **produces** chronic/recurrent disease and, in lupoid sycosis, scarring alopecia ([PMID: 11269901](https://pubmed.ncbi.nlm.nih.gov/11269901/); [PMID: 30995649](https://pubmed.ncbi.nlm.nih.gov/30995649/)).

**Pathways/processes and ontology suggestions:** innate immune response (GO:0045087), neutrophil chemotaxis (GO:0030593), inflammatory response (GO:0006954), MyD88-dependent toll-like receptor signaling (GO:0002755), defense response to Gram-positive bacterium (GO:0050830). **Cell types (CL):** neutrophil (CL:0000775), macrophage (CL:0000235), T cell (CL:0000084), keratinocyte (CL:0000312). **Upstream** events are toxin secretion and innate sensing; **downstream** events are neutrophilic abscess formation, dermonecrosis, and (in chronic disease) fibrosis/scarring.

### 7. Anatomical Structures Affected

- **Organ level:** skin (integumentary system only). Primary site is bearded skin of the face and neck; secondary involvement is limited to regional lymphadenopathy or, rarely, systemic upset with carbuncle.
- **Tissue/cell level:** pilosebaceous unit / hair follicle of terminal beard hairs; epithelial (follicular epithelium, epidermis) and dermal connective tissue; neutrophils and macrophages dominate the infiltrate.
- **UBERON terms:** hair follicle (UBERON:0002073), skin of face (UBERON:0008203), skin (UBERON:0002097), dermis (UBERON:0002067), epidermis (UBERON:0001003).
- **CL terms:** neutrophil (CL:0000775), macrophage (CL:0000235), keratinocyte (CL:0000312).
- **Subcellular:** no disease-specific compartment; the microbial pore-forming toxin acts at the host plasma membrane (GO:0005886).
- **Localization/lateralization:** typically **bilateral**, over upper lip, chin, cheeks, and mandibular/submental neck.

### 8. Temporal Development

- **Onset:** post-pubertal adult men; onset is typically subacute to chronic and insidious, superimposed on ongoing shaving.
- **Progression:** superficial folliculitis barbae → deep sycosis barbae → furuncle → carbuncle; the chronic lupoid variant is slowly progressive with scarring. Course is episodic/relapsing while shaving and *S. aureus* carriage persist.
- **Duration:** self-limited superficial episodes can resolve, but the deep/chronic form tends to be chronic and relapsing.
- **Remission:** treatment-induced remission is achievable with antibiotics + decolonization + shaving cessation; relapse is common if shaving resumes and carriage persists ([PMID: 27820584](https://pubmed.ncbi.nlm.nih.gov/27820584/); [PMID: 30859379](https://pubmed.ncbi.nlm.nih.gov/30859379/)).
- **Critical intervention window:** early antibiotic treatment of superficial folliculitis to prevent deepening into sycosis/furuncle/carbuncle ([PMID: 25226722](https://pubmed.ncbi.nlm.nih.gov/25226722/)).

### 9. Inheritance and Population

- **Inheritance:** none — acquired infection, not heritable; no OMIM entry.
- **Epidemiology:** no formal incidence/prevalence figures are available (not a reportable disease; data derive from clinical/textbook description rather than registries).
- **Demographics:** overwhelmingly post-pubertal adult men with terminal beard hair who shave; essentially absent in prepubertal children and in women (who lack a terminal beard). Sex ratio strongly male-predominant.
- **Geographic distribution:** worldwide; no defined endemic areas for the bacterial form (unlike zoophilic tinea barbae, which clusters among people with animal/livestock contact).

### 10. Diagnostics

Diagnosis is primarily **clinical** (beard-area follicular pustules/papules in an adult man who shaves). Confirmatory/differentiating tests:

1. **Bacterial swab with Gram stain and culture + susceptibility** of pustule contents to confirm *S. aureus* and detect MRSA (LOINC: aerobic wound culture, Gram stain).
2. **KOH wet mount, fungal culture, and dermatophyte PCR** of plucked hairs to **exclude tinea barbae** — mandatory when there is animal contact or antibiotic non-response ([PMID: 25226722](https://pubmed.ncbi.nlm.nih.gov/25226722/); [PMID: 31001659](https://pubmed.ncbi.nlm.nih.gov/31001659/)).
3. **Skin biopsy/histopathology** in atypical or chronic scarring cases: perifollicular/follicular neutrophilic (suppurative) inflammation acutely; mixed granulomatous inflammation with fibrosis/scarring in lupoid sycosis.
4. **HSV testing** (Tzanck cytology, direct immunofluorescence, viral culture, or HSV PCR) when lesions are acute/grouped/vesicular and fail antibiotics and antifungals — to identify herpetic sycosis ([PMID: 11896419](https://pubmed.ncbi.nlm.nih.gov/11896419/); [PMID: 15118392](https://pubmed.ncbi.nlm.nih.gov/15118392/); [PMID: 15564209](https://pubmed.ncbi.nlm.nih.gov/15564209/)).
5. **Dermoscopy** and **anterior-nares carriage swabs** in recurrent disease.

**Differential diagnosis:** tinea barbae (fungal), pseudofolliculitis barbae (mechanical), herpetic sycosis (viral), acne vulgaris, folliculitis decalvans, and other pustular dermatoses.

### 11. Outcome / Prognosis

Prognosis is generally **good/benign**: acute bacterial sycosis barbae is curable with appropriate antibiotics and hygiene and carries **no mortality**. However, it is prone to chronicity and relapse while shaving continues and *S. aureus* carriage persists. The chronic deep **lupoid sycosis** variant can cause permanent **cicatricial (scarring) alopecia** and cosmetic disfigurement, with attendant psychosocial/quality-of-life impact. **Complications:** furuncle, carbuncle, abscess, cellulitis, regional lymphadenitis, and rarely systemic/bacteremic spread. **Recurrence** is common: more than half of patients with staphylococcal SSTI have at least one recurrence ([PMID: 30859379](https://pubmed.ncbi.nlm.nih.gov/30859379/)).

### 12. Treatment

| Modality | Agents/approach | NCIT suggestion |
|---|---|---|
| Topical antibiotics (limited disease) | Mupirocin, fusidic acid | Topical Antibiotic Therapy |
| Systemic antibiotics (deep/extensive) | Anti-staphylococcal agents (culture-guided; cover MRSA if indicated) | Systemic Antibiotic Therapy |
| Procedural | Incision and drainage of fluctuant furuncles/carbuncles | Incision and Drainage |
| Decolonization | Intranasal mupirocin + chlorhexidine or dilute-bleach washes for patient and household | Decolonization |
| Behavioral | Stop/modify shaving; single-use clean razors; avoid sharing items | Behavioral Intervention |

Standard decolonization: "application of intranasal mupirocin and antiseptic body washes with chlorhexidine or dilute bleach water baths" ([PMID: 30859379](https://pubmed.ncbi.nlm.nih.gov/30859379/)). Decolonization reliably reduces colonization but its effect on recurrence is variable ([PMID: 27820584](https://pubmed.ncbi.nlm.nih.gov/27820584/)). **Pharmacogenomics:** not established for this condition. **Advanced/experimental therapeutics** (gene, cell, RNA, immunotherapy): not applicable. **Mimic-specific therapy:** systemic antifungals (terbinafine/itraconazole) for tinea barbae; systemic antivirals (aciclovir/valaciclovir) for herpetic sycosis ([PMID: 25226722](https://pubmed.ncbi.nlm.nih.gov/25226722/); [PMID: 11896419](https://pubmed.ncbi.nlm.nih.gov/11896419/)).

### 13. Prevention

- **Primary:** behavioral — shaving modification (or beard growth), single-use clean razors, avoiding shared razors, good hygiene, and reducing *S. aureus* carriage.
- **Secondary:** early antibiotic treatment of superficial folliculitis to prevent progression to deep sycosis/furuncle/carbuncle.
- **Tertiary:** decolonization and shaving cessation to prevent recurrence and scarring.
- **Immunization:** **NOT AVAILABLE** — no licensed *S. aureus* vaccine exists; multiple candidates have failed clinical endpoints, and natural colonization/infection does not elicit protective immunity because of extensive immune-evasion factors: "S. aureus colonization and invasive disease are not associated with the development of protective immune responses, which is attributable to a large spectrum of immune evasion factors." ([PMID: 27526714](https://pubmed.ncbi.nlm.nih.gov/27526714/)).

### 14. Other Species / Natural Disease

Human sycosis barbae affects *Homo sapiens* (NCBI Taxonomy txid9606); its agent is *S. aureus* (txid1280). A close natural analog is **canine superficial bacterial folliculitis (SBF)**, the most common bacterial skin disease of dogs, caused principally by *Staphylococcus pseudintermedius* (txid283734), with neutrophilic follicular pustules containing intracellular cocci—histologically parallel to human staphylococcal folliculitis. Shared antimicrobial-resistance dynamics (MRSP, MRSA) and shared topical antiseptic management (dilute bleach, chlorhexidine, benzoyl peroxide) further underscore the comparative relevance ([PMID: 24345778](https://pubmed.ncbi.nlm.nih.gov/24345778/); [PMID: 27426474](https://pubmed.ncbi.nlm.nih.gov/27426474/)). Zoonotic note: the *tinea barbae* mimic is often zoophilic (livestock-acquired), whereas bacterial sycosis barbae itself is not classically zoonotic.

### 15. Model Organisms

There is no dedicated genetic model of "sycosis barbae." The pathophysiology is studied in **murine *S. aureus* skin and soft-tissue infection models**, including LysM-EGFP reporter mice for noninvasive neutrophil imaging and MyD88-deficient strains for innate-immunity dissection ([PMID: 30882782](https://pubmed.ncbi.nlm.nih.gov/30882782/); [PMID: 25681348](https://pubmed.ncbi.nlm.nih.gov/25681348/); [PMID: 26351278](https://pubmed.ncbi.nlm.nih.gov/26351278/); [PMID: 32946878](https://pubmed.ncbi.nlm.nih.gov/32946878/)). **Recapitulation:** these models faithfully reproduce neutrophilic abscess formation, toxin-mediated dermonecrosis, and cytokine (IL-17/IL-22) control of bacterial burden. **Limitations:** mice are more resistant to several human-adapted *S. aureus* virulence factors, and no model reproduces the beard-follicle-specific, shaving-triggered anatomy of human sycosis barbae. The dog (SBF) serves as a naturally occurring large-animal comparator.

---

## Mechanistic Model / Interpretation

```
 Shaving microtrauma  +  S. aureus follicular colonization
                          |
                          v
        Breach of follicular epithelium into dermis   (inferred for beard)
                          |
          +---------------+----------------+
          |                                |
   PSMs -> EGR1-dependent            MyD88 sensing by dermal
   early leukocyte recruitment       macrophages: escalate + terminate
   [PMID 34873293]                   neutrophil recruitment [PMID 25681348]
          |                                |
          +---------------+----------------+
                          v
        IL-17A / IL-22 (T cells) drive neutrophils + AMPs
                    [PMID 26351278]
                          |
                          v
        Neutrophils wall bacteria into perifollicular abscess (FURUNCLE)
                    [PMID 32946878]
                          |
          +---------------+----------------+
          |                                |
   alpha-hemolysin (Hla)            Coalescence -> CARBUNCLE
   -> dermonecrosis                        |
   [PMID 32946878]                         v
          |                     Failure to clear (neutrophil defect,
          |                     nasal carriage) -> CHRONIC/RECURRENT
          +----------------------------->  -> lupoid sycosis / scarring
                                          [PMID 11269901, 30995649]
```

The unifying interpretation is that sycosis barbae is a **host-defense outcome**: neutrophilic walling-off is simultaneously the protective response and the histologic lesion (the abscess). Disease severity is set by the balance between toxin output (PSMs, Hla) and the speed/adequacy of the IL-17/IL-22 → neutrophil axis. This explains why the three cornerstones of therapy—killing the organism (antibiotics), removing the reservoir (decolonization), and removing the trigger (shaving modification)—map directly onto the causal chain, and why host immune defects and persistent nasal carriage predict the chronic/relapsing phenotype.

A second, clinically essential model is the **differential-diagnosis triad** of beard folliculitis. All three mimics present as beard-area pustules but diverge in cause and treatment:

| Condition | Cause | Key discriminators | Treatment |
|---|---|---|---|
| **Sycosis barbae** | *S. aureus* (bacterial) | Responds to antibiotics; Gram-positive cocci | Anti-staph antibiotics + decolonization + shaving change |
| **Tinea barbae** | Dermatophytes (fungal) | Animal contact; antibiotic non-response; boggy nodules/kerion; lymphadenopathy | Systemic antifungals; **no** incision |
| **Herpetic sycosis** | HSV-1/2 (viral) | Acute grouped vesicles; fails antibiotics **and** antifungals; HSV PCR+ | Systemic antivirals |
| **Pseudofolliculitis barbae** | Ingrown curly hairs (mechanical) | Curly hair, African/Asian ancestry; KRT75 A12T; foreign-body reaction | Shaving modification; not primarily antimicrobial |

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [25226722](https://pubmed.ncbi.nlm.nih.gov/25226722/) | *Infection of the beard area. Kerion: a review of 2 cases* | Core definition of sycosis barbae; tinea barbae as mimic; diagnostic branch point |
| [31001659](https://pubmed.ncbi.nlm.nih.gov/31001659/) | *Tinea barbae profunda due to T. mentagrophytes* | Tinea barbae misdiagnosed as bacterial folliculitis; PCR/culture/histology diagnosis |
| [31354326](https://pubmed.ncbi.nlm.nih.gov/31354326/) | *Pseudofolliculitis barbae; current treatment options* | KRT75/K6hf A12T ~6-fold PFB risk (GxE for the mimic) |
| [27212468](https://pubmed.ncbi.nlm.nih.gov/27212468/) | *Pseudofolliculitis barbae: understanding the condition* | PFB epidemiology / ancestry predisposition |
| [30995649](https://pubmed.ncbi.nlm.nih.gov/30995649/) | *S. aureus and host immunity in recurrent furunculosis* | Virulence-factor basis; host immunity in recurrence |
| [11269901](https://pubmed.ncbi.nlm.nih.gov/11269901/) | *Repeated furunculosis with abnormal neutrophil activity* | Host neutrophil-function defect predisposing to recurrence |
| [30859379](https://pubmed.ncbi.nlm.nih.gov/30859379/) | *Prevention of recurrent CA-S. aureus SSTI* | Decolonization regimen; recurrence rate; household clustering |
| [27820584](https://pubmed.ncbi.nlm.nih.gov/27820584/) | *CA-MRSA decolonization: do they reduce recurrence?* | Variable/limited effect of decolonization on recurrence |
| [34873293](https://pubmed.ncbi.nlm.nih.gov/34873293/) | *Rapid pathogen-specific recruitment by secreted toxins* | PSM/EGR1-dependent early leukocyte recruitment |
| [25681348](https://pubmed.ncbi.nlm.nih.gov/25681348/) | *MyD88 in macrophages critical for abscess resolution* | Dermal-macrophage MyD88 orchestration of neutrophils |
| [26351278](https://pubmed.ncbi.nlm.nih.gov/26351278/) | *IL-17A and IL-22 in cutaneous/hematogenous MRSA defense* | IL-17/IL-22 control abscess severity and bacterial burden |
| [32946878](https://pubmed.ncbi.nlm.nih.gov/32946878/) | *Antibody protection against S. aureus dermonecrosis* | Neutrophil abscess compartmentalization; Hla dermonecrosis |
| [24345778](https://pubmed.ncbi.nlm.nih.gov/24345778/) | *Canine superficial bacterial folliculitis* | Animal comparator (S. pseudintermedius); shared AMR |
| [27426474](https://pubmed.ncbi.nlm.nih.gov/27426474/) | *Epidermal collarettes in dogs* | Neutrophil-and-cocci histology paralleling human disease |
| [27526714](https://pubmed.ncbi.nlm.nih.gov/27526714/) | *S. aureus vaccines: deviating from the carol* | No protective immunity → no vaccine; recurrence rationale |
| [11896419](https://pubmed.ncbi.nlm.nih.gov/11896419/) | *Herpetic folliculitis* | Herpetic sycosis as HSV variant mimicking sycosis barbae |
| [15118392](https://pubmed.ncbi.nlm.nih.gov/15118392/) | *Fulminant herpetic sycosis* | Antibiotic+antifungal non-response → suspect HSV |
| [15564209](https://pubmed.ncbi.nlm.nih.gov/15564209/) | *Relapsing HSV-2 folliculitis in the beard* | HSV PCR diagnosis when routine tests negative |
| [30882782](https://pubmed.ncbi.nlm.nih.gov/30882782/) | *Mouse model of innate response to S. aureus* | Murine models (LysM-EGFP; MyD88) for mechanism |

**Consistency:** The mechanistic papers (mouse models + human genetics) converge on a single neutrophil-centric abscess narrative; the clinical papers converge on the antibiotics + decolonization + shaving-modification management triad. The main internal tension is the **variable efficacy of decolonization** on recurrence ([PMID: 27820584](https://pubmed.ncbi.nlm.nih.gov/27820584/)) versus its consistent reduction of colonization ([PMID: 30859379](https://pubmed.ncbi.nlm.nih.gov/30859379/)), which is faithfully reflected in the report's prognosis section.

---

## Limitations and Knowledge Gaps

1. **No sycosis-barbae-specific epidemiology.** No incidence/prevalence figures exist; the condition is not reportable and lacks registries. Demographic statements are qualitative.
2. **Mechanism is extrapolated.** The causal chain derives from general murine *S. aureus* SSTI models and human SSTI genetics, **not** from beard-follicle-specific experiments. The beard-follicle breach step is inferred.
3. **No molecular profiling of the disease itself.** No transcriptomic, proteomic, metabolomic, or single-cell datasets specific to sycosis barbae were identified; molecular data are from *S. aureus* biology and mouse models.
4. **Identifier verification pending.** ICD/SNOMED/MeSH mappings are compiled from aggregated resources and should be confirmed against primary ontology browsers; the MONDO ID was supplied by the template.
5. **No dedicated animal or genetic model** reproduces the shaving-triggered, terminal-beard-follicle anatomy.
6. **Lupoid sycosis** (the scarring chronic variant) is described mainly in older/textbook literature; modern mechanistic and outcome data are sparse.

---

## Proposed Follow-up Experiments / Actions

1. **Verify identifiers** against OMIM (expected absent), Orphanet, ICD-10/11, SNOMED CT, MeSH, and MONDO browsers; record cross-references explicitly.
2. **Targeted literature/registry search** for any quantitative epidemiology (dermatology outpatient series, military grooming/PFB cohorts) that might yield frequency estimates for beard folliculitis subtypes.
3. **Skin microbiome / host-response profiling** of clinically confirmed sycosis barbae lesions vs. adjacent normal beard skin (16S + host RNA-seq) to test whether the mouse-derived IL-17/IL-22–neutrophil axis operates in the human beard follicle.
4. **Prospective decolonization trial in recurrent beard folliculitis** specifically, stratified by anterior-nares carriage and neutrophil-function status, to resolve the colonization-vs-recurrence discrepancy.
5. **Diagnostic-algorithm validation** for the bacterial/fungal/viral triad: prospective evaluation of when Gram stain + culture alone suffices versus when reflexive KOH/dermatophyte-PCR and HSV-PCR are cost-effective.
6. **Curate the animal comparator** (canine SBF, *S. pseudintermedius*) for the knowledge base as a natural model, including phenotype-recapitulation annotations.

---

*Report compiled from 11 confirmed findings and 46 reviewed papers across 5 investigation iterations. Evidence types: human clinical (case series, reviews, guidelines), model organism (murine S. aureus SSTI), comparative/veterinary (canine SBF), and computational/ontology mapping.*


## Artifacts

- [OpenScientist final report](Sycosis_Barbae-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Sycosis_Barbae-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 22 |
| Quoted claims found in source | 22 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 19 |
| On topic | 5 |
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
| Terms whose name was checked | 4 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000775` (2 mentions) - the report calls it "CL terms:** neutrophil"; CL calls it **neutrophil**
- `UBERON:0002073` (1 mention) - the report calls it "UBERON terms:** hair follicle"; UBERON calls it **hair follicle**

Every term resolved, and every label the report gave matched.