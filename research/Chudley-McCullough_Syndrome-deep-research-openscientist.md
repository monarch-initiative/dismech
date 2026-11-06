---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-02T23:45:08.848375'
end_time: '2026-11-02T23:57:06.343253'
duration_seconds: 717.49
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Chudley-McCullough Syndrome
  mondo_id: MONDO:0011411
  category: Mendelian
  causal_genes: GPSM2
  omim_id: OMIM:604213
  synonyms: CMCS
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
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 5
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:22578326
  - PMID:29799026
  relevance_assessed: 17
  on_topic: 11
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 41
  verified: 40
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 4
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: UBERON:0001846
    reported_labels:
    - inner ear / auditory-vestibular system
    ontology_label: internal ear
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Chudley-McCullough_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Chudley-McCullough_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chudley-McCullough Syndrome
- **MONDO ID:** MONDO:0011411 (if available)
- **Causal gene(s):** GPSM2
- **OMIM:** OMIM:604213
- **Synonyms:** CMCS
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Chudley-McCullough Syndrome** covering all of the
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

# Chudley-McCullough Syndrome (CMCS): Comprehensive Disease Characteristics Report

**Disease:** Chudley-McCullough Syndrome (CMCS/CMS) · **MONDO:** MONDO:0011411 · **Phenotype OMIM:** #604213
**Causal gene:** **GPSM2** (G protein signaling modulator 2; aka *LGN*, *Pins*), HGNC:29501, gene OMIM *609245, NCBI Gene 29899, Ensembl ENSG00000121957, 1p13.3
**Category:** Mendelian, autosomal recessive

> **Summary answer:** Chudley-McCullough syndrome is a rare autosomal-recessive disorder caused by **biallelic loss-of-function variants in GPSM2 (LGN/Pins)**. It is defined by **profound congenital sensorineural hearing loss** combined with a **distinctive, largely static constellation of brain malformations** (partial agenesis of the corpus callosum, frontal polymicrogyria, gray-matter heterotopia, inferior cerebellar dysplasia, ventriculomegaly, and arachnoid/interhemispheric cysts) — yet, strikingly, affected individuals usually have **normal or near-normal cognition**. The unifying mechanism is loss of GPSM2-dependent **mitotic-spindle orientation / asymmetric cell division** (brain) and **stereocilia elongation / hair-bundle polarity** (inner ear). Management is supportive, centered on **cochlear implantation**.

Evidence base: this report is derived from **aggregated disease-level literature** (primary case series, molecular genetics papers, and animal/in-vitro mechanistic studies), not from individual EHR data.

---

## 1. Disease Information

Chudley-McCullough syndrome is a clinically recognizable autosomal-recessive syndrome pairing early-onset/congenital severe-to-profound sensorineural hearing loss with a characteristic brain malformation pattern, in the context of preserved psychomotor/cognitive development (PMID 22578326; PMID 41323166; PMID 33016209). First described in 1997 by Chudley, McCullough and McCullough in a consanguineous Manitoba Mennonite brother–sister pair; the causal gene (GPSM2) was identified in 2012 by Doherty et al. (PMID 22578326).

**Key identifiers:**
- **MONDO:** MONDO:0011411
- **OMIM (phenotype):** #604213 (CHUDLEY-McCULLOUGH SYNDROME; CMCS)
- **OMIM (gene GPSM2):** *609245
- **Orphanet:** Chudley-McCullough syndrome (ORPHA; rare genetic deafness-malformation entity — *specific ORPHA code not verified in this analysis*)
- **ICD-10:** no dedicated code; component codes apply — H90.3 (bilateral sensorineural hearing loss), Q04.0 (congenital malformations of corpus callosum), Q04.3 (other reduction deformities of brain)
- **ICD-11:** no dedicated stem; map via structural developmental anomalies of the brain + sensorineural hearing loss
- **MeSH:** no unique MeSH descriptor (covered by supplementary concept / indexed under the component terms)
- **HGNC:** HGNC:29501 (GPSM2)

**Synonyms / alternative names:** CMCS; CMS; Chudley-McCullough syndrome; (historically allelic designation) **DFNB82** nonsyndromic hearing loss — now understood to lie on the same GPSM2 phenotypic spectrum (PMID 22578326; PMID 20602914).

---

## 2. Etiology

**Primary cause — genetic (Mendelian, monogenic):** Biallelic (homozygous or compound heterozygous) loss-of-function variants in **GPSM2** (PMID 22578326). "*Homozygosity mapping and whole-exome sequencing … revealed four molecular variations (two single-base deletions, a nonsense mutation, and a canonical splice-site mutation) in the G protein-signaling modulator 2 gene, GPSM2, that underlie CMS*" (PMID 22578326).

**Genetic risk factors:**
- **Causal variants:** null alleles in GPSM2 (nonsense, frameshift, canonical splice-site). Examples: p.Ser352* (c.1055C>A; PMID 27180139), p.Arg365* (c.1093C>T; PMID 27064331), c.1473delG founder frameshift (PMID 23494849).
- **Susceptibility/modifier loci:** None established. No disease-modifier gene has been identified.
- **Family history / consanguinity:** Historically strong — many families are consanguineous or from genetically isolated populations (PMID 22578326; PMID 23494849). However, non-consanguineous cases without prior family history occur (PMID 38567212).

**Environmental risk factors:** None known. No toxin, infection, drug, maternal exposure, radiation, age, or sex effect is implicated. It is a purely monogenic developmental disorder.

**Protective factors:** Not applicable in a classical sense. The only "protective" genetic state is the absence of a second pathogenic GPSM2 allele — **heterozygous carriers are unaffected** (consistent with gnomAD pLI ≈ 0; §4, §9).

**Gene–environment interactions:** None documented; environment is not a known contributor.

---

## 3. Phenotypes

All phenotypes are **congenital/prenatal in origin**, **bilateral**, **non-progressive** (except occasional ventriculomegaly), and **lifelong**.

| Phenotype | Type | Onset | Severity | Frequency | HPO |
|---|---|---|---|---|---|
| Sensorineural hearing loss (severe–profound, bilateral) | Clinical sign / sensory | Congenital | Severe–profound | ~100% (defining) | HP:0000407 (sensorineural hearing impairment); HP:0008527 (congenital SNHL) |
| Partial agenesis of corpus callosum (esp. splenium) | Structural (imaging) | Prenatal | — | Hallmark, very high | HP:0001338 (partial ACC); HP:0001274 (abnormal CC) |
| Frontal polymicrogyria | Structural (imaging) | Prenatal | — | "Uniformly present" (PMID 22578326) | HP:0002126 (polymicrogyria) |
| Gray-matter heterotopia (frontal subcortical/periventricular) | Structural (imaging) | Prenatal | — | "Uniformly present" | HP:0002282 (gray matter heterotopia); HP:0030047 |
| Cerebellar dysplasia (inferior) | Structural (imaging) | Prenatal | — | Nearly invariant | HP:0001317 (abnormal cerebellum); HP:0007360 |
| Ventriculomegaly / colpocephaly / slit-like frontal horns | Structural (imaging) | Prenatal | Variable | Nearly invariant (variable degree) | HP:0002119 (ventriculomegaly) |
| Arachnoid / interhemispheric cyst | Structural (imaging) | Prenatal | Variable | Nearly invariant | HP:0100702 (arachnoid cyst) |
| Hydrocephalus (subset) | Clinical/structural | Neonatal | Variable (shunt in some) | Minority | HP:0000238 (hydrocephalus) |
| Balance/vestibular dysfunction (inferred; shown in mouse) | Sign | — | Variable | Uncertain in humans | HP:0002131 / vestibular dysfunction |
| **Preserved cognition / normal development** (a defining *negative* feature) | — | — | — | Typical | (notable *absence* of HP:0001249 intellectual disability) |

Key quote: "*frontal polymicrogyria and gray matter heterotopia are uniformly present, whereas cerebellar dysplasia, ventriculomegaly, and arachnoid cysts are nearly invariant. Despite these striking brain malformations, individuals with CMS generally do not present with significant neurodevelopmental abnormalities, except for hearing loss*" (PMID 22578326).

**Quality-of-life impact:** Dominated by profound deafness (language/communication, education, social participation) — largely remediable with cochlear implantation (§12). Cognitive/motor QoL is generally preserved. No disease-specific validated QoL instrument exists (generic pediatric hearing-loss/EQ-5D/SF-36 tools would apply). Hydrocephalus, when present, adds neurosurgical morbidity.

---

## 4. Genetic / Molecular Information

**Causal gene:** GPSM2 (HGNC:29501; gene OMIM *609245; Ensembl ENSG00000121957; chr1:108,875,350–108,934,545 GRCh38; cytoband 1p13.3). The protein GPSM2/LGN is a scaffolding cell-polarity protein with **N-terminal TPR (tetratricopeptide) repeats** (bind mInsc and NuMA) and **C-terminal GoLoco/GPR motifs** (bind Gαi-GDP) (PMID 11781568; PMID 22074847; PMID 27180139).

**Pathogenic variants:**
- **Type/class:** Predominantly **truncating loss-of-function** — nonsense, frameshift (single-base deletions), and canonical splice-site. No recurrent pathogenic missense class established. Representative alleles: c.1055C>A/p.Ser352* (PMID 27180139); c.1093C>T/p.Arg365* (PMID 27064331); c.1473delG (Dutch/Mennonite founder frameshift; PMID 23494849). Truncations "*abolish all four GoLoco domains in GPSM2*" (PMID 27180139).
- **Classification (ACMG/AMP):** Reported disease alleles are **Pathogenic**, with null mechanism supporting PVS1-type evidence.
- **Allele frequency (gnomAD):** Individual pathogenic null alleles are rare. Gene-level constraint: **pLI = 6.4×10⁻¹⁵ (≈0)**, **oe_lof = 0.74 (90% CI 0.60–0.92; LOEUF 0.92)**, obs_lof 58 / exp_lof 78.4, lof_z = 1.96 — i.e., GPSM2 is **tolerant of heterozygous LoF**, fully consistent with recessive inheritance (carriers unaffected).
- **Somatic vs germline:** **Germline** only; no somatic/cancer association, no mosaicism required.
- **Functional consequence:** **Loss of function** (not gain-of-function or dominant-negative).

**Modifier genes:** None identified (intrafamilial variability — e.g., discordant twins — suggests stochastic/epigenetic rather than defined modifiers; PMID 27064331).

**Epigenetic information:** No disease-specific DNA-methylation/histone signature reported.

**Chromosomal abnormalities:** None — CMCS is a single-gene point/indel disorder; CMA/karyotype are normal and low-yield.

---

## 5. Environmental Information

- **Environmental factors:** None known (no toxin/radiation/pollution/occupational link).
- **Lifestyle factors:** None relevant.
- **Infectious agents:** None — CMCS is genetic. (Clinically important *differential*: congenital infections such as CMV can mimic SNHL + brain anomalies, so infectious causes must be excluded diagnostically; §10.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic GPSM2 (LGN) loss-of-function variants** → truncated protein lacking GoLoco (Gαi-binding) motifs → **loss of a functional LGN/Pins scaffold** (*demonstrated*; PMID 22578326; PMID 27180139).
2. Loss of LGN **results in** failure to assemble the cortical **Gαi–LGN–NuMA** spindle-tethering complex at the cell cortex (*demonstrated in vitro/cell models*; PMID 11781568).
3. **Branch A — Brain:** Failure of the LGN complex **leads to** mis-oriented mitotic spindles / disrupted **asymmetric cell division (planar polarity)** in neural progenitors during fetal corticogenesis (*inferred for human brain from LGN biology*; PMID 22578326) → disordered neuronal production/migration → **polymicrogyria, subcortical/periventricular gray-matter heterotopia, callosal (splenial) agenesis, cerebellar dysplasia**, and impaired CSF-space/ependymal development → **ventriculomegaly, interhemispheric/arachnoid cysts**.
4. **Branch B — Inner ear:** Loss of apical **Gpsm2–Gαi** at hair-cell stereocilia tips **results in** defective **actin-rich stereocilia elongation** and loss of row-1 tip-complex (Gpsm2-Gαi-Whirlin-Myo15-Eps8) assembly (*demonstrated in mouse & in vitro*; PMID 28387217; PMID 35687681; PMID 20602914) → short/disorganized hair bundles → cochlear (and vestibular) hair-cell dysfunction → **profound sensorineural hearing loss** (± balance defects).
5. Because the lesion acts during a **prenatal critical window** and GPSM2 is dispensable for post-mitotic neuronal *function*, the malformations are **static** and **cognition is typically preserved** (*inferred*; PMID 22578326; PMID 27312216).

### Detail by category
- **Molecular pathways / machinery:** G-protein (Gαi) signaling–modulated **mitotic spindle orientation** and **planar cell polarity**; LGN–NuMA–dynein spindle-pulling. Not a classical Wnt/MAPK/mTOR disease. GO:BP: **GO:0000132** (establishment of mitotic spindle orientation), **GO:0007163** (establishment/maintenance of cell polarity), **GO:0001736** (establishment of planar polarity), **GO:0060113** (inner ear receptor cell differentiation), **GO:0007605** (sensory perception of sound).
- **Cellular processes:** Asymmetric cell division, spindle positioning, actin-bundle (stereocilia) morphogenesis. Not apoptosis/inflammation driven.
- **Protein dysfunction:** Truncation → loss of Gαi-binding GoLoco motifs → loss-of-scaffold function (no aggregation/GoF).
- **Metabolic / immune / epigenetic:** No primary metabolic, immune, or epigenetic contribution described.
- **Subcellular compartments (GO:CC):** **GO:0005938** (cell cortex), **GO:0000922** (spindle pole), **GO:0120044** (stereocilium tip), **GO:0032420** (stereocilium).
- **Cell types (CL):** cochlear/auditory hair cell **CL:0000202** (inner **CL:0000589**, outer **CL:0000601**), vestibular hair cell, inner-ear supporting cell, neural/radial-glial progenitor **CL:0000681**.
- **Molecular profiling:** No human CMCS transcriptomic/proteomic/metabolomic signature published; mechanistic data come from mouse and biochemical/biophysical (phase-separation) studies (PMID 35687681).

---

## 7. Anatomical Structures Affected

- **Organ/system level — primary:** **Central nervous system** (UBERON:0001017) and **inner ear / auditory-vestibular system** (UBERON:0001846).
  - Corpus callosum (**UBERON:0002336**) — partial agenesis, splenium-predominant
  - Frontal cerebral cortex (**UBERON:0016525**) — polymicrogyria
  - Subcortical/periventricular white & gray matter — heterotopia
  - Cerebellum (**UBERON:0002037**) — inferior dysplasia
  - Lateral ventricles (**UBERON:0002285**) — ventriculomegaly/colpocephaly, slit-like frontal horns
  - Arachnoid/subarachnoid & interhemispheric space — cysts
  - Cochlea (**UBERON:0001844**) and vestibular organs — hair-cell/stereocilia pathology
- **Secondary involvement:** Obstructive hydrocephalus (subset) → neurosurgical shunt.
- **Tissue/cell level:** Neuroepithelium/neural tissue (nervous tissue); inner-ear sensory epithelium (specialized epithelial hair cells). CL:0000202 (hair cell), CL:0000681 (radial glial/progenitor).
- **Subcellular:** cell cortex / mitotic spindle pole (brain); stereocilium tip/actin core (ear). GO:CC as in §6.
- **Localization / lateralization:** **Bilateral/symmetric** for deafness; brain malformations **bilateral with midline/frontal emphasis**.

---

## 8. Temporal Development

- **Onset:** **Congenital/prenatal.** Brain malformations form during fetal neurogenesis; detectable prenatally on fetal MRI/US (slit-like frontal horns, ACC, frontal subcortical heterotopia, arachnoid cysts, cerebellar dysplasia; PMID 27312216). Hearing loss present at/from birth.
- **Onset pattern:** Insidious/developmental (structural), not acute.
- **Progression:** **Static/non-progressive** malformations; cognition stable. **Exception:** ventriculomegaly can progress to hydrocephalus in a subset (neonatal), occasionally requiring shunt (PMID 27064331).
- **Course/duration:** Chronic, lifelong, non-degenerative.
- **Remission:** None spontaneously; hearing is **functionally restorable** by cochlear implant (treatment-induced functional "remission" of the deafness).
- **Critical period:** The **prenatal window of progenitor division/hair-cell differentiation** is the vulnerability window; postnatally the key intervention window is **early cochlear implantation** for language development.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** (OMIM #604213).
- **Penetrance:** Effectively **complete** for profound congenital SNHL and core cortical malformations in biallelic-null individuals.
- **Expressivity:** **Variable** for ventriculomegaly/hydrocephalus and cyst burden — even **discordant between twins** with identical genotype (PMID 27064331); some GPSM2 individuals (originally "nonsyndromic"/DFNB82) have cortical malformation but **no ventriculomegaly** (PMID 22578326).
- **Anticipation:** None (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically reported.
- **Founder effects:** **Dutch/Mennonite c.1473delG** founder haplotype traced to Europe and carried to North America (PMID 23494849); **Palestinian** DFNB82 founder (PMID 20602914). Additional families: Yemeni (PMID 27180139), others.
- **Consanguinity:** Major contributor historically (homozygous null in consanguineous/isolated populations), but non-consanguineous compound-heterozygous cases exist (PMID 38567212).
- **Carrier frequency:** Not formally estimated; gnomAD LoF alleles individually rare; elevated locally in founder populations.
- **Epidemiology:** **Ultra-rare** — reported **~30 times** in the literature since 1997 (PMID 38567212). No validated prevalence/incidence figures (too rare for registry estimates).
- **Demographics:** Panethnic reports; clustering in consanguineous/founder populations. **Sex ratio ≈ 1:1** (expected for AR; no sex bias). Age distribution: diagnosed in infancy/childhood (congenital), individuals survive into adulthood.

---

## 10. Diagnostics

- **Imaging (cornerstone):** **Brain MRI** showing the recognizable pattern — partial ACC (splenium), frontal polymicrogyria, frontal subcortical/periventricular heterotopia, inferior cerebellar dysplasia, ventriculomegaly/colpocephaly with slit-like frontal horns, and arachnoid/interhemispheric cysts (PMID 22578326; PMID 27312216; PMID 41323166). **Prenatal** fetal imaging can suggest the diagnosis and is prognostically important (PMID 27312216). RadLex/NCIT: MRI (NCIT:C16809).
- **Audiology:** Newborn hearing screen fail; ABR/OAE/audiometry confirm **severe–profound bilateral SNHL**. LOINC-coded audiometry/ABR.
- **Genetic testing (confirmatory):** Detection of **biallelic GPSM2 pathogenic variants** via **single-gene testing**, **hereditary-hearing-loss gene panels**, or **whole-exome/whole-genome sequencing** (WES/WGS). WES + homozygosity mapping was the original discovery route (PMID 22578326; PMID 20602914; PMID 23494849). An **LOVD GPSM2 database** supports interpretation (PMID 23494849). GTR: GPSM2 single-gene and deafness-panel tests. NCIT: Genetic Testing (NCIT:C15709).
- **Low-yield/not indicated:** Chromosomal microarray, karyotype, FISH, mtDNA, repeat-expansion testing (no structural/mitochondrial/repeat basis).
- **Laboratory/biomarkers:** No specific biochemical blood/urine biomarker; genotype is the molecular marker.
- **Omics diagnostics:** Not used clinically (no RNA/proteomic/metabolomic diagnostic assay).
- **Clinical criteria:** No formal consensus criteria; diagnosis is **pattern recognition (SNHL + characteristic MRI) + GPSM2 confirmation**.
- **Differential diagnosis:** Other malformations of cortical development / ACC syndromes; **congenital CMV**; tubulinopathies; Aicardi syndrome; other syndromic deafness. **Distinguishing feature: preserved cognition despite severe imaging findings** (PMID 27312216) — key for counseling because prognosis is far better than look-alikes.
- **Screening:** Captured indirectly by **newborn hearing screening** (triggers evaluation); **carrier/cascade testing** in families and founder populations.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** **Life expectancy appears normal**; no disease-specific mortality described. CMCS is non-degenerative.
- **Morbidity/disability:** Dominated by **profound deafness** → communication/language disability if untreated. Cognition and motor function generally preserved; thus overall functional prognosis is **favorable**, markedly better than morphologically similar brain-malformation syndromes (PMID 27312216).
- **Complications:** Hydrocephalus requiring shunt in a subset (PMID 27064331); shunt-related complications possible. Deafness-related developmental/educational impact if not remediated.
- **Recovery potential:** Brain malformations are fixed/non-recoverable but non-progressive; **hearing is functionally recoverable with cochlear implantation** (§12).
- **Prognostic factors:** Timeliness of hearing habilitation (early CI → better language outcomes); presence/progression of ventriculomegaly/hydrocephalus. No molecular prognostic biomarker beyond genotype (all null → consistent core phenotype).
- **QoL measures:** Generic pediatric hearing-loss/EQ-5D/SF-36/PROMIS; no CMCS-specific tool.

---

## 12. Treatment

**No disease-modifying, pharmacologic, gene, cell, or RNA therapy exists.** Management is **supportive and multidisciplinary**, targeting the deafness and any hydrocephalus.

- **Hearing habilitation (primary):** **Bilateral cochlear implantation** effectively restores functional hearing — "*two successful cases of bilateral cochlear implantation in two children with CMS*" (PMID 38567212); additional CI reports (PMID 30907716; Forli 2019). Hearing aids/auditory-verbal therapy as adjuncts. NCIT: **Cochlear Implantation (NCIT:C53473)**.
- **Neurosurgical:** **Ventriculoperitoneal shunt** for hydrocephalus when present/progressive (PMID 27064331). NCIT: shunt/ventriculoperitoneal shunt procedure.
- **Supportive/rehabilitative:** Speech-language therapy, early-intervention/educational support, audiologic follow-up; physical/occupational therapy if balance/vestibular issues. NCIT: Supportive Care (NCIT:C15399), Speech Therapy.
- **Pharmacotherapy / pharmacogenomics:** None specific.
- **Experimental / clinical trials:** No CMCS-specific trials identified; GPSM2 is not currently a gene-therapy target.
- **Treatment outcomes:** CI outcomes reported as successful hearing restoration (PMID 38567212); no CMCS-specific adverse-event profile beyond standard CI/shunt risks.
- **Personalized medicine:** Diagnosis-guided counseling; otherwise genotype does not alter management (uniform null mechanism).

---

## 13. Prevention

- **Primary prevention:** Not preventable at the individual level (congenital genetic). Population-level risk reduction via **genetic counseling** and reduced consanguinity in high-risk groups.
- **Genetic counseling (central):** AR recurrence risk **25%** for carrier couples; cascade carrier testing; discussion of options. NSGC/ACMG/GeneReviews frameworks apply.
- **Reproductive options / secondary prevention:** **Preimplantation genetic testing (PGT-M)** and **prenatal diagnosis** (molecular if familial variants known; fetal MRI pattern recognition otherwise) — prenatal diagnosis is feasible and prognostically valuable (PMID 27312216).
- **Carrier/founder screening:** Targeted carrier screening in founder populations (Dutch/Mennonite c.1473delG; Palestinian DFNB82) (PMID 23494849; PMID 20602914).
- **Newborn screening:** Universal **newborn hearing screening** enables early detection and timely CI (secondary prevention of language disability).
- **Tertiary prevention:** Early cochlear implantation; monitoring/treatment of hydrocephalus.
- **Immunization / behavioral / environmental / prophylaxis:** Not applicable (non-infectious, non-environmental).

---

## 14. Other Species / Natural Disease

- **Orthologous gene:** Mouse **Gpsm2** (NCBI Gene 76123); the gene/pathway (LGN/Pins) is **deeply conserved** — *Drosophila* **Pins**, mammalian **LGN/AGS3** paralogs (PMID 11781568; PMID 22074847; PMID 37017303).
- **Species affected (experimental):** *Mus musculus* (**NCBITaxon:10090**). No naturally occurring companion-animal/wildlife CMCS-equivalent disease is cataloged in OMIA (not reported here).
- **Comparative biology:** The spindle-orientation (Pins/LGN–NuMA/Mud–Gαi) module is conserved from *Drosophila* neuroblasts to mammalian progenitors and epithelia (PMID 11781568; PMID 37017303), underpinning cross-species mechanistic study. Paralog **AGS3/Gpsm1** modulates LGN function (PMID 37017303; PMID 28684399).
- **Zoonotic potential / transmission:** Not applicable (genetic, non-transmissible).

---

## 15. Model Organisms

- **Mouse (primary model):** *Gpsm2* mutant mice recapitulate the **auditory phenotype** and reveal **vestibular/balance defects** via impaired **actin-rich stereocilia elongation** — "*mutation of the mouse orthologue of GPSM2 affects actin-rich stereocilia elongation in auditory and vestibular hair cells, causing deafness and balance defects*" (PMID 28387217; correction PMID 29799026). GPSM2 localizes to the apical surface of hair/supporting cells, highest in embryonic development (PMID 20602914).
- **In-vitro/biochemical models:** Reconstitution showing Gpsm2-Gαi **phase separation** drives row-1 tip-complex (5xTCD: Gpsm2-Gαi-Whirlin-Myo15-Eps8) condensate formation and actin bundling; a deafness-associated Gpsm2 mutation impairs this — "*A deafness-associated mutation of Gpsm2 leads to impaired formation of the 5xTCD condensates and consequently reduced actin bundling, providing possible clues for etiology of hearing loss in patients with Chudley-McCullough syndrome*" (PMID 35687681). Crystal structures of LGN–mInsc / LGN–NuMA interfaces inform the spindle mechanism (PMID 22074847; PMID 11781568).
- **Model types available:** Knockout/mutant mice; cellular spindle-orientation assays; invertebrate (Drosophila Pins) genetics for conserved mechanism.
- **Phenotype recapitulation:** **Strong for the hearing-loss/stereocilia component**; the **human brain-malformation component is less fully modeled** in published auditory-focused mouse studies (a current limitation).
- **Applications:** Dissecting stereocilia morphogenesis, hair-bundle polarity, and spindle-orientation/asymmetric-division biology; platform for future hearing-loss therapeutics.
- **Resources:** MGI (Gpsm2), IMPC/IMSR, Alliance of Genome Resources.

---

## Supported vs. Refuted Hypotheses

**Supported:**
- GPSM2 biallelic LoF is the cause of CMCS (PMID 22578326). ✓
- Mechanism = spindle-orientation/asymmetric-division defect (brain) + stereocilia-elongation defect (ear) (PMID 22578326; PMID 28387217; PMID 35687681). ✓
- AR inheritance with LoF-tolerant gene (carriers unaffected; gnomAD pLI≈0). ✓
- Deafness + partial ACC with preserved cognition is a recognizable, prognostically favorable entity (PMID 22578326; PMID 27312216). ✓
- Cochlear implantation restores hearing (PMID 38567212). ✓

**Refuted / Not supported:**
- Gain-of-function or dominant mechanism — refuted (all alleles null; gene LoF-tolerant).
- Environmental/infectious causation — not supported (purely genetic).
- Strict genotype–phenotype correlation for brain severity — refuted (discordant twins; variable ventriculomegaly; PMID 27064331; PMID 22578326).

## Limitations & Future Directions
- No formal prevalence/incidence or large natural-history cohort (ultra-rare).
- Human brain-malformation mechanism is **inferred** from LGN cell biology rather than directly demonstrated in human/CMCS neural tissue; brain-specific animal models are limited.
- Modifiers of expressivity (e.g., why some develop hydrocephalus) are unknown.
- No human omics profiling; no targeted/gene therapy.

## Key References (PMID)
22578326 (Doherty 2012, landmark gene discovery) · 20602914 (Walsh 2010, DFNB82/GPSM2) · 23494849 (Almomani 2013, founder variant) · 27180139 (Hamzeh 2016, p.Ser352*) · 27064331 (Koenigstein 2016, discordant twins) · 27312216 (Chapman 2016, prenatal diagnosis) · 38567212 (Alter 2024, cochlear implants, ~30 cases) · 33016209 (Blauen 2021, clinical review) · 41323166 (Ouqlani 2026, case/MRI) · 28387217 & 29799026 (Mauriac 2017, mouse) · 35687681 (Shi 2022, tip-complex condensates) · 11781568 (Du 2001, LGN–NuMA) · 22074847 (Yuzawa 2011, LGN–mInsc structure) · 37017303 (Descovich 2023, AGS3–LGN).


## Artifacts

- [OpenScientist final report](Chudley-McCullough_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Chudley-McCullough_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 17 |
| On topic | 11 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:22578326` *(abstract only)*: "*Homozygosity mapping and whole-exome sequencing … revealed four molecular variations (two single-base deletions, a nonsense mutation, and a canonical splice-site mutation) in the G protein-signaling modulator 2 gene, GPSM2, that underlie CMS*"
  - closest text in source: "Homozygosity mapping and whole-exome sequencing of DNA from affected individuals in eight families (including the family in the first report of CMS) revealed four molecular variations (two single-base deletions, a nonsense mutation, and a canonical splice-site mutation) in the G protein-signaling modulator 2 gene, GPSM2, that underlie CMS"
- `PMID:29799026` *(abstract only)*: "*mutation of the mouse orthologue of GPSM2 affects actin-rich stereocilia elongation in auditory and vestibular hair cells, causing deafness and balance defects*"
  - Text part not found as substring: '*mutation of the mouse orthologue of GPSM2 affects actin-rich stereocilia elongation in auditory and vestibular hair cells, causing deafness and balance defects*' (note: only abstract available for PMID:29799026, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 8 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0001846` (1 mention) - the report calls it "inner ear / auditory-vestibular system"; UBERON calls it **internal ear**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000202` (2 mentions) - the report calls it "hair cell"; CL calls it **auditory hair cell**
- `CL:0000681` (2 mentions) - the report calls it "radial glial/progenitor"; CL calls it **radial glial cell**
- `UBERON:0001017` (1 mention) - the report calls it "Central nervous system", "Organ/system level — primary:** **Central nervous system"; UBERON calls it **central nervous system**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0001017` - called "Central nervous system", "Organ/system level — primary:** **Central nervous system"