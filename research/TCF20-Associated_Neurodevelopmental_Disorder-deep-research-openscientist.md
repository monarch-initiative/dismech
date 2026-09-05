---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-05T14:13:12.451195'
end_time: '2026-09-05T14:44:47.165197'
duration_seconds: 1894.71
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: TCF20-Associated Neurodevelopmental Disorder
  mondo_id: MONDO:0032745
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
citation_count: 13
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 16
  quotes_valid: 16
  relevance_assessed: 13
  on_topic: 9
  off_topic: 2
  off_topic_references:
  - PMID:10995766
  - PMID:22081970
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 67
  verified: 64
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 10
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0032745
    reported_labels:
    - MONDO
    ontology_label: developmental delay with variable intellectual impairment and
      behavioral abnormalities
  labels_variant: 9
  unresolvable_prefixes:
  - OMIM
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: TCF20-Associated_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: TCF20-Associated_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TCF20-Associated Neurodevelopmental Disorder
- **MONDO ID:** MONDO:0032745 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **TCF20-Associated Neurodevelopmental Disorder** covering all of the
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

# TCF20-Associated Neurodevelopmental Disorder (TAND / DDVIBA): A Comprehensive Disease Characteristics Report

**Disease:** TCF20-Associated Neurodevelopmental Disorder (TAND)
**Also known as:** Developmental Delay with Variable Intellectual Impairment and Behavioral Abnormalities (DDVIBA)
**MONDO:** MONDO:0032745 · **OMIM:** #618430 · **Gene:** *TCF20* (HGNC:11631), 22q13.2
**Category:** Mendelian, autosomal dominant
**Report basis:** Aggregated disease-level literature and ontology/database resources (no patient-level EHR data). Evidence drawn from human clinical cohorts, in vitro/biochemical studies, and mouse/cellular models, as indicated per claim.

---

## Summary

TCF20-associated neurodevelopmental disorder (TAND), catalogued in OMIM as "Developmental delay with variable intellectual impairment and behavioral abnormalities" (DDVIBA, #618430), is a rare autosomal-dominant neurodevelopmental disorder caused by loss-of-function/haploinsufficiency of *TCF20*, a dosage-sensitive chromatin-binding transcriptional co-regulator on chromosome 22q13.2. *TCF20* (also called *SPBP*) is structurally and functionally related to *RAI1*, the gene responsible for Smith–Magenis syndrome, and the two disorders share substantial clinical overlap. The core phenotype — fully penetrant developmental delay/intellectual disability plus hypotonia — is accompanied in a majority of patients by autism spectrum features (~69%), attention/hyperactivity problems (~67%), and non-specific craniofacial dysmorphism (~67%), with variable movement disorders, sleep disturbance, seizures (~12%), structural brain anomalies (~24%), and, in a subset, postnatal overgrowth (tall stature, macrocephaly, obesity).

Mechanistically, TCF20 acts within a neuronal **MeCP2–PHF14–TCF20 chromatin complex** that co-regulates key neuronal genes. Reduced TCF20 dosage dysregulates this transcriptional program, and reciprocal dosage changes produce "mirror" phenotypes: deletions/loss-of-function cause TAND, whereas duplications spanning *TCF20* cause a related 22q13.2 microduplication neurodevelopmental disorder. The gene is extremely intolerant to loss of function in gnomAD (pLI = 1.0, LOEUF = 0.052), and its pathogenic variant spectrum is overwhelmingly truncating (frameshift, nonsense, splice) or whole-gene deletion, exactly as predicted for a haploinsufficiency mechanism.

The disorder is diagnosed molecularly (predominantly by trio exome sequencing, with chromosomal microarray detecting deletions/duplications). Most cases are de novo (~67%), a minority are inherited from mildly affected parents (~10%), and a notable ~8% arise via germline mosaicism, which has direct genetic-counseling implications for recurrence risk. There is no disease-specific or targeted therapy; management is entirely supportive (early intervention, physical/occupational/speech therapy, behavioral and pharmacologic management of ASD/ADHD, antiseizure medication, sleep/melatonin support). The course is chronic, lifelong, and non-degenerative, with reported patients ranging from 2 to 68 years of age.

---

## 1. Disease Information

**Overview.** TAND is a Mendelian neurodevelopmental disorder defined by heterozygous inactivation of *TCF20*. First delineated as a discrete syndrome in 2019 through two large concurrent cohort studies ([PMID: 30819258](https://pubmed.ncbi.nlm.nih.gov/30819258/); [PMID: 30739909](https://pubmed.ncbi.nlm.nih.gov/30739909/)), it had earlier been implicated in autism spectrum disorder ([PMID: 25228304](https://pubmed.ncbi.nlm.nih.gov/25228304/)) and in an intellectual-disability–overgrowth phenotype ([PMID: 27436265](https://pubmed.ncbi.nlm.nih.gov/27436265/)). Vetrini et al. established that "TCF20 pathogenic variants are associated with a novel syndrome manifesting clinical characteristics similar to those observed in Smith-Magenis syndrome."

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0032745 |
| OMIM (phenotype) | #618430 (DDVIBA) |
| OMIM (gene) | 603107 (*TCF20*) |
| UMLS | C5193092 |
| MedGen | 1676192 |
| GARD | 0018517 |
| HGNC | 11631 |
| Entrez Gene | 6942 |
| Ensembl | ENSG00000100207 |
| ICD-10 / ICD-11 | No specific code; subsumed under ICD-10 F79/F88 or ICD-11 6A00 (disorders of intellectual development) |
| Orphanet | No dedicated ORPHA number identified |

**Synonyms / alternative names.** DDVIBA; TCF20-related disorder; TCF20-related syndrome; TCF20-associated neurodevelopmental disorder (TAND). The gene *TCF20* carries aliases *SPBP*, *AR1*, *TCF-20*, and *DDVIBA*.

**Information source.** Evidence is derived from aggregated disease-level resources (OMIM, ClinVar, gnomAD, HPO) and from published individual-patient case series/cohorts (Torti 2019, Vetrini 2019, Poquérusse 2025), not from a single EHR system.

---

## 2. Etiology

**Primary cause — genetic.** TAND is a monogenic disorder caused by heterozygous loss-of-function of *TCF20*. Vetrini et al. reported "25 unique inactivating single nucleotide variants/indels (1 missense, 1 canonical splice-site variant, 18 frameshift, and 5 nonsense) and 4 deletions of TCF20" ([PMID: 30819258](https://pubmed.ncbi.nlm.nih.gov/30819258/)). The reciprocal dosage change — duplication spanning *TCF20* — causes a related disorder: "Duplication including TCF20 was suspected to cause a neurodevelopmental disorder (NDD) with mirror traits compared to patients with TCF20 deletions" ([PMID: 34904221](https://pubmed.ncbi.nlm.nih.gov/34904221/)).

**Genetic risk factors.** The causal variant is the disease. No independent susceptibility loci or modifier genes are established. Because *TCF20* lies within 22q13, larger 22q13 deletions (Phelan–McDermid spectrum) can co-delete *TCF20* alongside *SHANK3* and contribute to phenotype severity ([PMID: 30216695](https://pubmed.ncbi.nlm.nih.gov/30216695/); [PMID: 42192297](https://pubmed.ncbi.nlm.nih.gov/42192297/)).

**Environmental risk factors.** None established. As a fully penetrant Mendelian dominant disorder for developmental delay/ID, no environmental exposures, lifestyle factors, or infectious agents are implicated in causation.

**Protective factors.** None identified. No protective alleles or modifier variants are described.

**Gene–environment interactions.** None documented. There is no evidence for GxE modulation of this monogenic phenotype.

---

## 3. Phenotypes

TAND phenotypes span neurological, behavioral, musculoskeletal, growth, craniofacial, ophthalmologic, and gastrointestinal domains. The full HPO catalog for OMIM:618430 comprises ~50 terms. Cohort-level frequencies derive principally from Torti et al. ([PMID: 30739909](https://pubmed.ncbi.nlm.nih.gov/30739909/)): "All had developmental delay/intellectual disability. Autism spectrum disorders/autistic features were reported in 69%, attention disorders or hyperactivity in 67%, craniofacial features (no recognizable facial gestalt) in 67%, structural brain anomalies in 24%, and seizures in 12%."

### Core neurodevelopmental/behavioral phenotypes

| Phenotype | HPO term | Frequency | Type | Onset |
|---|---|---|---|---|
| Global developmental delay | HP:0001263 | 100% | Clinical sign | Infantile |
| Intellectual disability (typically mild) | HP:0001256 | 100% (fully penetrant) | Clinical sign | Childhood |
| Motor delay | HP:0001270 | Common | Clinical sign | Infantile |
| Delayed speech/language | HP:0000750 | Common | Clinical sign | Early childhood |
| Autistic behavior / ASD | HP:0000729 | ~69% | Behavioral | Early childhood |
| Hyperactivity / ADHD | HP:0000752 | ~67% | Behavioral | Childhood |
| Anxiety | HP:0000739 | Variable | Behavioral | Childhood |
| Aggressive behavior | HP:0000718 | Variable | Behavioral | Childhood |
| Compulsive / stereotypic behavior | HP:0000722 / HP:0000733 | Variable | Behavioral | Childhood |
| Seizure | HP:0001250 | ~12% | Clinical sign | Variable |
| Ataxia / incoordination | HP:0001251 / HP:0002311 | Subset | Clinical sign | Variable |
| Sleep disturbance | HP:0002360 | Frequent | Clinical sign | Childhood |

### Musculoskeletal, growth, and other systemic phenotypes

- **Hypotonia** (HP:0001252) — frequent; spasticity (HP:0001257) in a subset.
- **Overgrowth subset:** tall stature (HP:0000098), macrocephaly (HP:0000256), obesity (HP:0001513, rare), accelerated skeletal maturation (HP:0005616). Schäfgen et al. described "mild intellectual disability, postnatal tall stature and macrocephaly, obesity and muscular hypotonia as common clinical signs while ASD was only present in one proband" ([PMID: 27436265](https://pubmed.ncbi.nlm.nih.gov/27436265/)).
- **Craniofacial (no recognizable gestalt):** brachycephaly (HP:0000248), frontal bossing (HP:0002007), high forehead (HP:0000348), long face (HP:0000276), midface retrusion (HP:0011800), depressed nasal bridge (HP:0005280), short nose (HP:0003196), bulbous nose (HP:0000414), thin upper lip (HP:0000219), downturned mouth (HP:0002714), open mouth (HP:0000194), plagiocephaly (HP:0001357).
- **Eyes:** strabismus (HP:0000486), myopia (HP:0000545), deeply set eyes (HP:0000490), epicanthus (HP:0000286).
- **Ears:** low-set (HP:0000369), posteriorly rotated (HP:0000358).
- **Limbs/skeletal:** tapered fingers (HP:0001182), fifth-finger clinodactyly (HP:0004209), sandal gap (HP:0001852), scoliosis (HP:0002650).
- **Digestive:** constipation (HP:0002019), feeding difficulties (HP:0011968).
- **Breast:** gynecomastia (HP:0000771), inverted nipples (HP:0003186).

**Severity/progression.** Intellectual disability is generally mild and, critically, **stable and non-regressive** — distinguishing TAND from Rett syndrome despite the shared MeCP2 axis. Expressivity is variable; DD/ID is fully penetrant while ASD is incompletely penetrant.

**Quality-of-life impact.** No disease-specific EQ-5D/SF-36/PROMIS data exist. QoL impact is inferred from the burden of lifelong ID, ASD, ADHD, sleep disturbance, and movement problems, which collectively affect education, independent living, communication, and family functioning.

---

## 4. Genetic / Molecular Information

**Causal gene.** *TCF20* (HGNC:11631; Entrez 6942; Ensembl ENSG00000100207; OMIM gene 603107), located at chr22q13.2 (GRCh38 chr22:42,160,013–42,343,616, minus strand). Aliases: *SPBP*, *AR1*, *TCF-20*, *DDVIBA*.

**Pathogenic variant landscape.** ClinVar (queried 2026-09) lists ~1,377 submitted variants for *TCF20*: **316 Pathogenic, 44 Likely pathogenic (~360 P/LP), and 1,234 VUS.** The pathogenic set is dominated by truncating (frameshift/nonsense/splice) and deletion alleles, consistent with haploinsufficiency; the large VUS fraction reflects abundant tolerated missense variation. This mirrors the cohort spectrum of "1 missense, 1 canonical splice-site variant, 18 frameshift, and 5 nonsense... and 4 deletions" ([PMID: 30819258](https://pubmed.ncbi.nlm.nih.gov/30819258/)).

**Variant classification.** Per ACMG/AMP, truncating variants in a haploinsufficient gene meet strong LoF criteria (PVS1); recurrent LoF variants in unrelated families and de novo occurrence add supporting evidence. Missense variants are largely VUS given the lack of missense constraint.

**Allele frequency / constraint (gnomAD, GRCh38).**

| Metric | Value | Interpretation |
|---|---|---|
| pLI | 1.0 | Extreme LoF intolerance |
| LOEUF (oe_lof upper) | 0.052 | Highly constrained |
| observed/expected LoF | 0.020 (3 obs vs 148.6 exp) | Near-complete LoF depletion |
| LoF Z | 10.13 | Strongly constrained |
| Missense Z | 0.69 | Not missense-constrained |

**Somatic vs germline.** Germline. Pathogenic variants are constitutional; a notable fraction arise via **germline (gonadal) mosaicism** in a transmitting parent (see Section 9).

**Functional consequence.** Loss of function / haploinsufficiency. Reduced TCF20 dosage is the disease driver; the reciprocal duplication produces a "mirror" gain-of-dosage phenotype ([PMID: 34904221](https://pubmed.ncbi.nlm.nih.gov/34904221/)).

**Modifier genes.** None specifically validated for *TCF20*. In the 22q13 deletion context, co-deleted neighboring genes (e.g., *SHANK3*, *CELSR1*, and others) modify the composite phenotype ([PMID: 42192297](https://pubmed.ncbi.nlm.nih.gov/42192297/)).

**Epigenetic information.** TCF20 itself is a chromatin-associated transcriptional co-regulator (see Section 6); no disease-specific DNA-methylation episignature has been formally validated in the reviewed literature, though its mechanistic partner MeCP2 is a methyl-CpG reader, placing TAND within the broader chromatinopathy/methylation-reader disease space.

**Chromosomal abnormalities.** Whole-gene and contiguous 22q13.2 deletions cause TAND; 22q13.2 microduplications spanning *TCF20* cause the reciprocal disorder. A pericentric chromosome 22 inversion physically disrupting *TCF20* was the original ASD-linked lesion ([PMID: 25228304](https://pubmed.ncbi.nlm.nih.gov/25228304/)).

---

## 5. Environmental Information

Not applicable. TAND is a monogenic disorder with no established environmental, lifestyle, or infectious contributors to causation. Environmental factors are relevant only as general supportive-care considerations (e.g., seizure precautions, developmental stimulation), not as etiologic agents.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (loss-of-function branch)

1. A heterozygous truncating/deletion variant in *TCF20* **leads to** nonsense-mediated decay or a non-functional protein → reduced TCF20 protein dosage (haploinsufficiency). *(Demonstrated: variant spectrum + gnomAD constraint.)*
2. Reduced TCF20 **results in** diminished incorporation of TCF20 into the neuronal **MeCP2–PHF14–TCF20 chromatin complex**. *(Demonstrated by BioID complex mapping, [PMID: 35074918](https://pubmed.ncbi.nlm.nih.gov/35074918/).)*
3. Impaired complex function **leads to** dysregulated transcription of key neuronal target genes co-regulated by MeCP2 and TCF20. *(Demonstrated: coexpression + co-regulation.)*
4. Altered neuronal gene expression **results in** abnormal neuronal maturation and circuit function. *(Inferred from downstream cellular/behavioral phenotype.)*
5. Aberrant neuronal circuitry **leads to** the clinical manifestations: developmental delay/ID, ASD, hyperactivity, hypotonia, movement disorders, sleep disturbance, and seizures. *(Clinically demonstrated; step 4→5 mechanistic linkage inferred.)*

**Branch — gain-of-dosage:** Increased TCF20 dosage (22q13.2 microduplication) **results in** a reciprocal "mirror" neurodevelopmental disorder ([PMID: 34904221](https://pubmed.ncbi.nlm.nih.gov/34904221/)), underscoring bidirectional dosage sensitivity.

### Molecular detail

**TCF20/SPBP protein.** A nuclear multidomain transcriptional co-activator: N-terminal transactivation region, an AT-hook DNA-binding domain, a bipartite nuclear localization signal, and a C-terminal extended PHD (ePHD/ADD) zinc-finger domain of the trithorax family. Rekdal et al. defined it as "a nuclear, multidomain protein containing an N-terminal region with transactivating ability, a novel type of DNA-binding domain containing an AT hook motif, and a bipartite nuclear localization signal as well as a C-terminal zinc finger domain" ([PMID: 10995766](https://pubmed.ncbi.nlm.nih.gov/10995766/)). It enhances transactivation by c-Jun, Ets1, Sp1, Pax6, and the androgen receptor ([PMID: 21935435](https://pubmed.ncbi.nlm.nih.gov/21935435/)).

**Chromatin engagement.** TCF20/SPBP has two independent nucleosome-binding domains and, like its homolog RAI1, is "strongly enriched on chromatin in interphase HeLa cells, and both proteins display low nuclear mobility" ([PMID: 22081970](https://pubmed.ncbi.nlm.nih.gov/22081970/)) — behavior typical of a chromatin scaffolding co-regulator.

**The MeCP2 axis.** Zhou et al. used proximity-dependent biotinylation (BioID) to identify "a transcription factor 20 (TCF20) complex that interacts with MeCP2 at the chromatin interface. Importantly, RTT-causing mutations in MECP2 disrupt this interaction. TCF20 and MeCP2 are highly coexpressed in neurons and coregulate the expression of key neuronal genes" ([PMID: 35074918](https://pubmed.ncbi.nlm.nih.gov/35074918/)). They further showed dosage sensitivity in vivo: "Reducing Tcf20 partially rescued the behavioral deficits caused by MECP2 overexpression, demonstrating a functional relationship between MeCP2 and TCF20 in MECP2 duplication syndrome pathogenesis," and identified "a patient exhibiting RTT-like neurological features with a missense mutation in the PHF14 subunit of the TCF20 complex that abolishes the MeCP2-PHF14-TCF20 interaction." This places TAND firmly within the MeCP2/Rett-spectrum chromatinopathy family.

**Cellular processes / cell types.** Pathology is transcriptional dysregulation in **neurons** (CL:0000540), including forebrain glutamatergic (CL:0000679) and GABAergic (CL:0000617) neurons where TCF20 and MeCP2 are highly coexpressed. Core biological processes: **regulation of transcription, DNA-templated (GO:0006355)** and **chromatin binding (GO:0003682)**.

**Subcellular localization.** Nucleus (GO:0005634), chromatin (GO:0000785), chromosome (GO:0005694).

### Diagram

```
 TCF20 LoF variant (frameshift/nonsense/splice/deletion)
        │  haploinsufficiency (pLI=1.0)
        ▼
 ↓ TCF20 protein dosage
        │
        ▼
 Impaired MeCP2–PHF14–TCF20 chromatin complex ◄── PHF14 missense (RTT-like)
        │  (BioID-validated; MECP2 mutations also disrupt)
        ▼
 Dysregulated transcription of neuronal target genes
        │
        ▼
 Abnormal neuronal maturation / circuit function (inferred)
        │
        ▼
 DD/ID · ASD · ADHD · hypotonia · movement disorder · sleep disturbance · seizures

 [MIRROR BRANCH]  22q13.2 duplication → ↑TCF20 dosage → reciprocal NDD
```

There is no evidence for metabolic, immune, oxidative-stress, ischemic, fibrotic, or enzyme-deficiency mechanisms; TAND is a **transcriptional/chromatin regulatory** disorder.

---

## 7. Anatomical Structures Affected

**Organ / system level.** The **central nervous system** (UBERON:0000955 brain; UBERON:0001017 CNS; UBERON:0001016 nervous system) is the primary affected organ. Regions implicated by clinical features include the **cerebral cortex** (UBERON:0000956) and forebrain (cognition, speech, motor control), the **cerebellum** (UBERON:0002037; inferred from ataxia/incoordination), and **basal ganglia** (inferred from dystonia/movement disorder). Structural brain MRI anomalies are non-specific and present in ~24% of patients, bilateral with no consistent lateralization.

**Secondary systems.** Musculoskeletal (hypotonia; muscle UBERON:0002385; scoliosis), craniofacial skeleton (dysmorphism), **eye** (UBERON:0000970; strabismus/myopia), gastrointestinal (constipation, feeding difficulty), and endocrine/growth axis (overgrowth subset).

**Tissue and cell level.** Nervous tissue; neurons (CL:0000540), with forebrain glutamatergic (CL:0000679) and GABAergic (CL:0000617) subtypes highlighted by TCF20/MeCP2 coexpression.

**Subcellular level.** Nucleus (GO:0005634), chromatin (GO:0000785), chromosome (GO:0005694).

**Lateralization.** Bilateral/symmetric where CNS structural changes occur; no systematic lateralization reported.

---

## 8. Temporal Development

**Onset.** Congenital/infantile (Infantile onset, HP:0003593). Developmental delay is typically recognized in infancy or early childhood; hypotonia may be noted neonatally.

**Progression.** The disorder is **chronic, stable, and non-degenerative.** There is no evidence of regression (contrasting with classic Rett syndrome). Torti et al. ascertained patients "ranged in age from 2 to 68 years" ([PMID: 30739909](https://pubmed.ncbi.nlm.nih.gov/30739909/)), supporting a lifelong but non-progressive course with normal or near-normal survival.

**Disease course pattern.** Static encephalopathy pattern; intellectual disability persists but does not worsen neurodegeneratively. Seizures and behavioral features may fluctuate and require ongoing management.

**Critical periods.** Early childhood is the key window for developmental intervention (early intervention, therapies); no biological disease-modifying window is defined given the absence of targeted therapy.

**Remission.** None; the underlying genetic lesion is constitutional and permanent. Symptomatic domains (e.g., seizures, sleep, behavior) can be managed/controlled but not cured.

---

## 9. Inheritance and Population

**Inheritance pattern.** Autosomal dominant (HP:0000006).

**De novo vs inherited vs mosaic.** Across ~91 reported individuals (Poquérusse 2025 review): "~67% of cases arose de novo, while ~10% were inherited, and, intriguingly, ~8% were either confirmed or suspected to have arisen via germline mosaicism" ([PMID: 40011607](https://pubmed.ncbi.nlm.nih.gov/40011607/)). Vetrini et al. found variants "de novo in 20 instances and inherited from 4 symptomatic parents in 5 [families], including in one set of monozygotic twins" ([PMID: 30819258](https://pubmed.ncbi.nlm.nih.gov/30819258/)).

**Germline mosaicism.** Physically demonstrated: in one family, "droplet digital PCR (ddPCR) of DNA derived from early morning urine detected the variation in 3.2% of the father's urothelial cells, confirming germline mosaicism" ([PMID: 40011607](https://pubmed.ncbi.nlm.nih.gov/40011607/)). This substantially informs recurrence-risk counseling: parents of a "de novo" proband may carry undetectable-in-blood gonadal mosaicism, elevating sibling recurrence risk above the population baseline.

**Penetrance / expressivity.** DD/ID is fully penetrant; ASD and other features show incomplete penetrance and variable expressivity, including mildly affected transmitting parents.

**Constraint / carrier frequency.** *TCF20* is extremely LoF-intolerant (pLI = 1.0), so pathogenic LoF alleles are essentially absent from the general (gnomAD) population; there is no meaningful "carrier" population for a dominant, highly penetrant condition.

**Genetic anticipation / founder effects / consanguinity.** Not applicable (no repeat-expansion mechanism; no reported founder alleles; dominant mechanism unrelated to consanguinity).

**Epidemiology.** Prevalence and incidence are not formally established; TAND is a rare disorder with ~91 reported individuals to date. It is likely underdiagnosed and increasingly recognized as exome sequencing becomes routine in NDD workups.

**Demographics.** No strong ethnic predilection reported; two recurrent LoF variants were observed in unrelated families ([PMID: 30819258](https://pubmed.ncbi.nlm.nih.gov/30819258/)). Sex ratio is not established as strongly skewed for the core NDD phenotype (autosomal gene). Age distribution of ascertained patients spans 2–68 years.

---

## 10. Diagnostics

**Diagnostic approach.** Diagnosis is molecular. The principal modality is **trio exome sequencing (ES)**; Torti et al. identified patients "26 of whom were identified via exome sequencing" ([PMID: 30739909](https://pubmed.ncbi.nlm.nih.gov/30739909/)), and Vetrini et al. noted "Genome-wide analyses by exome sequencing (ES) and chromosomal microarray analysis (CMA) identified individuals with heterozygous, likely damaging, loss-of-function alleles in TCF20" ([PMID: 30819258](https://pubmed.ncbi.nlm.nih.gov/30819258/)).

| Test | Utility in TAND |
|---|---|
| Whole exome sequencing (WES) | Primary diagnostic yield; detects SNVs/indels |
| Whole genome sequencing (WGS) | Useful for non-coding/structural variants missed by ES |
| Chromosomal microarray (CMA) | Detects 22q13.2 deletions and duplications |
| Multigene NDD/epilepsy/ID panels | *TCF20* included in modern ID/ASD panels |
| Single-gene testing | For cascade testing of a known familial variant |
| Karyotype/FISH | Historically detected large rearrangements (e.g., chr22 inversion, [PMID: 25228304](https://pubmed.ncbi.nlm.nih.gov/25228304/)) |
| ddPCR (urine/other tissue) | Confirms parental germline mosaicism ([PMID: 40011607](https://pubmed.ncbi.nlm.nih.gov/40011607/)) |

**Biomarkers / labs.** There is **no specific biochemical biomarker, metabolite, or enzyme assay.** No metabolomic/proteomic diagnostic signature is validated.

**Imaging / electrophysiology.** Brain MRI shows non-specific structural anomalies in ~24% (Torti 2019). EEG is used for seizure evaluation (~12% have seizures).

**Clinical criteria.** No formal DSM/ICD diagnostic criteria specific to TAND; diagnosis rests on identification of a pathogenic *TCF20* variant in a compatible clinical context.

**Differential diagnosis.**

| Condition | Gene/locus | Distinguishing features |
|---|---|---|
| Smith–Magenis syndrome | *RAI1* | Closest mimic; RAI1 is TCF20's paralog; overlapping behavior/sleep phenotype ([PMID: 30819258](https://pubmed.ncbi.nlm.nih.gov/30819258/)) |
| Phelan–McDermid syndrome | 22q13.3 / *SHANK3* | Overlapping 22q13 deletions; *TCF20* co-deletion in larger deletions ([PMID: 30216695](https://pubmed.ncbi.nlm.nih.gov/30216695/), [PMID: 42192297](https://pubmed.ncbi.nlm.nih.gov/42192297/)) |
| Rett / MECP2-related disorders | *MECP2* | Shared MeCP2 axis; but TAND is non-regressive |
| Other overgrowth-ID syndromes | e.g., *NSD1*, *EZH2* | Overlap in overgrowth subset ([PMID: 27436265](https://pubmed.ncbi.nlm.nih.gov/27436265/)) |

Upadia et al. noted that in 22q13.2 microdeletions encompassing *TCF20*, "All eight patients share features common to patients with PMS including developmental delay and language delay" ([PMID: 30216695](https://pubmed.ncbi.nlm.nih.gov/30216695/)), reinforcing the Phelan–McDermid overlap.

**Screening.** No newborn or population carrier screening exists. Cascade testing of at-risk relatives follows identification of a familial variant.

---

## 11. Outcome / Prognosis

**Survival / mortality.** TAND is **not** a life-limiting disorder in the way of neurodegenerative conditions; the reported age range (2–68 years) indicates normal or near-normal survival into adulthood ([PMID: 30739909](https://pubmed.ncbi.nlm.nih.gov/30739909/)). No disease-specific mortality rate is established.

**Morbidity / function.** The principal burden is lifelong intellectual disability (usually mild), plus ASD, ADHD, hypotonia, sleep disturbance, and — in subsets — seizures, movement disorders, and behavioral challenges. These cause meaningful disability in learning, communication, adaptive functioning, and independent living.

**Disease course.** Chronic, stable, non-degenerative. Complications are those of the associated features (e.g., seizure-related, orthopedic from hypotonia/scoliosis, feeding/constipation, behavioral).

**Recovery potential.** No recovery of the underlying deficit; developmental gains occur with intervention but ID persists.

**Prognostic factors.** Severity correlates loosely with variant type/deletion size in contiguous-gene contexts (larger 22q13 deletions co-deleting additional genes tend to be more severe, [PMID: 42192297](https://pubmed.ncbi.nlm.nih.gov/42192297/)). No validated molecular prognostic biomarker exists.

**QoL measures.** No disease-specific validated instruments; generic pediatric/NDD QoL tools apply.

---

## 12. Treatment

**No disease-specific or FDA-approved targeted therapy, gene therapy, RNA therapy, or clinical trial exists for TCF20 to date.** Management is entirely **supportive and symptom-directed** (NCIT: Supportive Care Intervention).

| Domain | Intervention | NCIT-type category |
|---|---|---|
| Developmental delay / ID | Early intervention, special education | Rehabilitation therapy |
| Motor delay / hypotonia | Physical & occupational therapy | Physical therapy |
| Speech/language delay | Speech-language therapy | Speech therapy |
| ASD | Behavioral therapy (ABA), structured supports | Behavioral intervention |
| ADHD/hyperactivity | Stimulants / non-stimulant pharmacotherapy | Pharmacotherapy |
| Seizures | Antiseizure medications | Anticonvulsant therapy |
| Sleep disturbance | Sleep hygiene, melatonin | Supportive care |
| Movement disorder/dystonia | Symptom-directed pharmacologic/PT management | Supportive care |
| Constipation/feeding | Nutritional and GI management | Supportive care |
| Scoliosis | Orthopedic monitoring/management | Surgical/interventional |

**Pharmacogenomics.** No *TCF20*-specific pharmacogenomic guidance; standard PGx applies to any prescribed psychotropics/antiseizure agents.

**Advanced/experimental therapeutics.** None; the MeCP2–TCF20 dosage biology suggests dosage-restoration strategies are theoretically attractive but none are in development.

**Treatment strategy.** Multidisciplinary care coordinated through developmental pediatrics/clinical genetics, with individualized therapy plans and genetic counseling for the family.

---

## 13. Prevention

**Primary prevention.** Not applicable for the disorder itself (a constitutional genetic condition). **Genetic counseling** is the principal preventive tool: for de novo cases, sibling recurrence risk is low but non-negligible because of documented germline mosaicism (~8% of cases; [PMID: 40011607](https://pubmed.ncbi.nlm.nih.gov/40011607/)); for inherited cases, the transmitting parent has a 50% transmission risk.

**Reproductive options.** Prenatal diagnosis and preimplantation genetic testing (PGT) are available when a familial pathogenic variant is known.

**Secondary prevention.** Early molecular diagnosis (via ES/CMA in NDD workup) enables early intervention and anticipatory management of seizures, sleep, and behavior.

**Tertiary prevention.** Prevent complications through seizure control, orthopedic surveillance (scoliosis), management of sleep and behavior, and educational support.

**Immunization / public health / prophylaxis.** Not applicable — no infectious or environmental etiology.

---

## 14. Other Species / Natural Disease

**Orthologs.**

| Species | Gene | Identifier |
|---|---|---|
| Mouse (*Mus musculus*, NCBI Taxon 10090) | *Tcf20* | MGI:108399; Entrez 21411; ENSMUSG00000041852 |
| Rat (*Rattus norvegicus*, Taxon 10116) | *Tcf20* | Entrez 366964 |
| Zebrafish (*Danio rerio*, Taxon 7955) | *tcf20* | Entrez 100006417 |

**Natural disease in other species.** No naturally occurring *TCF20*-associated disease is catalogued in companion animals or wildlife (no OMIA entry identified). The gene is evolutionarily conserved, and its paralog *RAI1* underlies conserved dosage-sensitive behavioral biology, supporting cross-species conservation of the underlying mechanism.

**Zoonotic potential / transmission.** Not applicable (non-infectious genetic disorder).

---

## 15. Model Organisms

**Mouse (mammalian in vivo).** The most informative model. Zhou et al. showed *Tcf20* and *Mecp2* are highly coexpressed in neurons and co-regulate neuronal genes; genetically **reducing *Tcf20* partially rescued behavioral deficits caused by MECP2 overexpression**, establishing a dosage-sensitive *Tcf20*–MeCP2 functional relationship in vivo ([PMID: 35074918](https://pubmed.ncbi.nlm.nih.gov/35074918/)). This model recapitulates the dosage-sensitivity axis central to TAND pathophysiology (and to the mirror duplication phenotype), though a dedicated *Tcf20* haploinsufficiency mouse fully phenocopying the human syndrome is not comprehensively characterized in the reviewed literature — a notable gap.

**Cellular models.** *Tcf20* was identified in a mammalian RNAi screen as a modifier of mutant huntingtin aggregation: "As for Tcf20, which contains polyQ stretches at N-terminus, its binding to mutant huntingtin aggregates is observed in neuro2a cells and in HD model mouse neurons" ([PMID: 24705917](https://pubmed.ncbi.nlm.nih.gov/24705917/)) — indicating a polyQ-containing protein with neuronal aggregation-associated behavior.

**In vitro biochemistry.** SPBP/TCF20 chromatin-binding and coactivator assays in HeLa and reporter systems defined its domain architecture, nucleosome-binding domains, and coactivator partnerships ([PMID: 10995766](https://pubmed.ncbi.nlm.nih.gov/10995766/); [PMID: 22081970](https://pubmed.ncbi.nlm.nih.gov/22081970/); [PMID: 21935435](https://pubmed.ncbi.nlm.nih.gov/21935435/)).

**Model resources.** MGI (mouse), RGD (rat), ZFIN (zebrafish). No iPSC/organoid TAND models were identified in the reviewed literature.

**Recapitulation / limitations.** Existing models validate the **molecular dosage mechanism** (TCF20–MeCP2 co-regulation) rather than the full behavioral/craniofacial/growth syndrome. Limitations include incomplete behavioral phenotyping of *Tcf20*-haploinsufficient animals and absence of patient-derived neuronal models.

---

## Mechanistic Model / Interpretation

TAND is best understood as a **dosage-sensitive chromatinopathy**. TCF20/SPBP is a chromatin-tethered transcriptional co-regulator that, together with MeCP2 (the Rett-syndrome protein) and PHF14, forms a complex that co-regulates neuronal gene programs. The disorder sits at the intersection of two well-known dosage-sensitive paradigms:

1. **RAI1 paralogy → Smith–Magenis / Potocki–Lupski analogy.** Just as *RAI1* deletion causes Smith–Magenis and duplication causes Potocki–Lupski, *TCF20* loss causes TAND and duplication causes a reciprocal "mirror" NDD. The structural/functional relatedness of TCF20 and RAI1 — "TCF20 encodes a transcriptional co-regulator structurally related to RAI1, the dosage-sensitive gene responsible for Smith-Magenis syndrome (deletion/haploinsufficiency) and Potocki-Lupski syndrome (duplication/triplosensitivity)" ([PMID: 30819258](https://pubmed.ncbi.nlm.nih.gov/30819258/)) — explains the striking clinical overlap with Smith–Magenis (behavioral phenotype, sleep disturbance).

2. **MeCP2 partnership → Rett-spectrum linkage.** Because TCF20 physically and functionally cooperates with MeCP2, TCF20 disruption produces overlapping neuronal transcriptional dysregulation — but, importantly, without the regressive course of classic Rett syndrome, likely reflecting the distinct target-gene consequences of losing a partner co-regulator versus losing the methyl-CpG reader itself.

The convergence of extreme gnomAD LoF constraint (pLI = 1.0), a truncating-dominant ClinVar/cohort variant spectrum, a validated dosage-sensitive in vivo genetic interaction, and a reciprocal duplication phenotype forms an unusually coherent, mutually reinforcing evidence base for haploinsufficiency as the mechanism.

---

## Evidence Base

| Paper | PMID | Contribution |
|---|---|---|
| Vetrini et al. 2019 — *De novo and inherited TCF20 pathogenic variants...* | [30819258](https://pubmed.ncbi.nlm.nih.gov/30819258/) | Delineated the syndrome; variant spectrum (LoF-dominant); Smith–Magenis similarity; ES+CMA diagnostics; de novo/inherited breakdown |
| Torti et al. 2019 — *Variants in TCF20 in neurodevelopmental disability* | [30739909](https://pubmed.ncbi.nlm.nih.gov/30739909/) | Largest cohort; phenotype frequencies (DD/ID 100%, ASD 69%, ADHD 67%, craniofacial 67%, brain anomalies 24%, seizures 12%); age range 2–68 |
| Zhou et al. 2022 — *Disruption of MeCP2-TCF20 complex...* | [35074918](https://pubmed.ncbi.nlm.nih.gov/35074918/) | Core mechanism: BioID-defined MeCP2–PHF14–TCF20 complex; dosage rescue in mouse; PHF14 patient |
| Lévy et al. 2022 — *Rare and de novo duplications containing TCF20...* | [34904221](https://pubmed.ncbi.nlm.nih.gov/34904221/) | Reciprocal duplication "mirror" phenotype; expanded neurological feature set |
| Schäfgen et al. 2016 — *De novo nonsense/frameshift... postnatal overgrowth* | [27436265](https://pubmed.ncbi.nlm.nih.gov/27436265/) | Overgrowth subphenotype; incomplete ASD penetrance |
| Babbs et al. 2014 — *TCF20/SPBP in autism spectrum disorder* | [25228304](https://pubmed.ncbi.nlm.nih.gov/25228304/) | First ASD linkage; chr22 inversion; germinal mosaicism; RAI1 relatedness |
| Poquérusse et al. 2025 — *Germline mosaicism in TAND* | [40011607](https://pubmed.ncbi.nlm.nih.gov/40011607/) | Case counts (~91); inheritance breakdown; ddPCR-confirmed germline mosaicism |
| Upadia et al. 2018 — *22q13.2 microdeletion encompassing TCF20/TNFRSF13C* | [30216695](https://pubmed.ncbi.nlm.nih.gov/30216695/) | Contiguous-gene/differential-diagnosis context (Phelan–McDermid overlap) |
| Ricciardello et al. — *22q13 terminal deletion size and clinical features* | [42192297](https://pubmed.ncbi.nlm.nih.gov/42192297/) | Deletion-size/phenotype correlation; neighboring-gene modifiers (incl. TCF20) |
| Rekdal et al. 2000 — *Nuclear factor SPBP domains* | [10995766](https://pubmed.ncbi.nlm.nih.gov/10995766/) | Protein domain architecture / coactivator function |
| Darvekar et al. 2012 — *Two nucleosome-binding domains in SPBP* | [22081970](https://pubmed.ncbi.nlm.nih.gov/22081970/) | Chromatin-binding behavior shared with RAI1 |
| Corsi et al. 2011 — *Pax6 represses AR via SPBP* | [21935435](https://pubmed.ncbi.nlm.nih.gov/21935435/) | Coactivator partnerships (AR, Pax6) |
| Yamanaka et al. 2014 — *RNAi screen, huntingtin aggregation* | [24705917](https://pubmed.ncbi.nlm.nih.gov/24705917/) | Cellular model; Tcf20 polyQ / aggregation biology |

---

## Limitations and Knowledge Gaps

- **Epidemiology undefined.** No formal prevalence/incidence estimates; ~91 reported individuals likely represent substantial underascertainment.
- **No validated biomarker or episignature.** Diagnosis depends entirely on sequencing; no biochemical or methylation-based confirmatory test is established in the reviewed literature.
- **Incomplete animal-model characterization.** The dosage-sensitivity mechanism is validated in mouse, but a *Tcf20*-haploinsufficient model fully phenocopying the human syndrome (behavior, growth, craniofacial) is not comprehensively described; no iPSC/organoid models identified.
- **Genotype–phenotype correlation limited.** Beyond deletion size in contiguous-gene cases, predictors of severity within isolated *TCF20* LoF are not well defined; the overgrowth subset's determinants are unclear.
- **QoL / natural-history data sparse.** No disease-specific longitudinal outcome or QoL instruments.
- **Missense interpretation.** The large VUS burden (1,234 in ClinVar) reflects poor missense constraint and hampers classification of non-truncating variants.
- **Citation caveat:** Several mechanism-related snippets from Zhou et al. 2022 were flagged as not exactly matching the stored abstract text (the abstract was truncated in the source database); the substantive claims are corroborated across multiple findings, but exact-quote verification for those specific lines should be re-checked against the primary source.

---

## Proposed Follow-up Experiments / Actions

1. **Generate and deep-phenotype a *Tcf20* haploinsufficient mouse** (heterozygous null and conditional neuronal knockout) with behavioral, craniofacial, growth, and EEG phenotyping to test full syndrome recapitulation.
2. **Patient-derived iPSC neurons/organoids** to define the dysregulated neuronal target-gene program downstream of reduced TCF20 within the MeCP2–PHF14–TCF20 complex (RNA-seq + CUT&RUN for TCF20/MeCP2 occupancy).
3. **Search for a DNA-methylation episignature** across a TAND patient cohort, given the MeCP2 (methyl-CpG reader) partnership — a positive signature would provide a diagnostic classifier for VUS resolution.
4. **Functional assays for missense VUS** (chromatin binding, complex incorporation, transactivation reporters) to reclassify the large VUS pool.
5. **Prospective natural-history registry** capturing developmental trajectories, seizure/sleep/behavioral outcomes, growth, and validated QoL measures across the lifespan (2–68 years).
6. **Systematic parental germline-mosaicism screening** (ddPCR on sperm/urine) in "de novo" families to refine recurrence-risk counseling.
7. **Explore dosage-restoration therapeutic concepts** (e.g., upregulating the intact allele) informed by the reciprocal duplication phenotype, in cellular models.

---

*Report compiled from OMIM, ClinVar, gnomAD, HGNC/Ensembl, HPO (OMIM:618430), and primary literature. Evidence source types are indicated throughout: human clinical cohorts (Torti, Vetrini, Schäfgen, Poquérusse, Lévy, Upadia), model organism (Zhou mouse; Yamanaka cellular), and in vitro biochemistry (Rekdal, Darvekar, Corsi).*


## Artifacts

- [OpenScientist final report](TCF20-Associated_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](TCF20-Associated_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 16 |
| Quoted claims found in source | 16 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 13 |
| On topic | 9 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:10995766` (6 mentions) - The nuclear factor SPBP contains different functional domains and stimulates the activity of various transcriptional activators.
  - shared terms: gene
- `PMID:22081970` (6 mentions) - Identification of two independent nucleosome-binding domains in the transcriptional co-activator SPBP.
  - shared terms: syndrome

Weighed against this report's own most characteristic terms: `tcf20`, `disorder`, `tand`, `phenotype`, `gene`, `behavioral`, `mecp2`, `variant`, `clinical`, `developmental`, `seizure`, `syndrome`, `sleep`, `deletion`, `duplication`, `delay`, `asd`, `feature`, `patient`, `mechanism`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 67 |
| Resolved | 64 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 20 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032745` (2 mentions) - the report calls it "MONDO"; MONDO calls it **developmental delay with variable intellectual impairment and behavioral abnormalities**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001256` (1 mention) - the report calls it "Intellectual disability (typically mild)"; HP calls it **Mild intellectual disability**, and lists "Intellectual disability, mild" among its other names
- `HP:0000750` (1 mention) - the report calls it "Delayed speech/language"; HP calls it **Delayed speech and language development**, and lists "Delayed speech" among its other names
- `HP:0000729` (1 mention) - the report calls it "Autistic behavior / ASD"; HP calls it **Autistic behavior**, and lists "Autistic behaviors" among its other names
- `HP:0000752` (1 mention) - the report calls it "Hyperactivity / ADHD"; HP calls it **Hyperactivity**
- `HP:0000098` (1 mention) - the report calls it "Overgrowth subset:** tall stature"; HP calls it **Tall stature**
- `HP:0000486` (1 mention) - the report calls it "Eyes:** strabismus"; HP calls it **Strabismus**
- `HP:0001182` (1 mention) - the report calls it "Limbs/skeletal:** tapered fingers"; HP calls it **Tapered finger**, and lists "Distally tapering fingers" among its other names
- `HP:0002019` (1 mention) - the report calls it "Digestive:** constipation"; HP calls it **Constipation**
- `HP:0000771` (1 mention) - the report calls it "Breast:** gynecomastia"; HP calls it **Gynecomastia**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `MGI`.