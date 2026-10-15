---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-24T16:12:01.914523'
end_time: '2026-09-24T16:41:05.271191'
duration_seconds: 1743.36
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Neonatal Diabetes Mellitus With Congenital Hypothyroidism
  mondo_id: MONDO:0012436
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
citation_count: 25
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 25
  quotes_valid: 25
  relevance_assessed: 25
  on_topic: 21
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 38
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 14
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0000851
    reported_labels:
    - Highly frequent (one compound-het patient lacked it)
    ontology_label: Congenital hypothyroidism
  - term_id: HP:0008007
    reported_labels:
    - Frequent
    ontology_label: Primary congenital glaucoma
  - term_id: CL:1000454
    reported_labels:
    - kidney collecting-duct epithelial cell
    - "Renal tubular epithelium** \u2014 shortened cilia, cyst formation"
    ontology_label: kidney collecting duct epithelial cell
  - term_id: GO:0005634
    reported_labels:
    - GLIS3 transactivation
    ontology_label: nucleus
  labels_variant: 4
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neonatal_Diabetes_Mellitus_With_Congenital_Hypothyroidism-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neonatal_Diabetes_Mellitus_With_Congenital_Hypothyroidism-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neonatal Diabetes Mellitus With Congenital Hypothyroidism
- **MONDO ID:** MONDO:0012436 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neonatal Diabetes Mellitus With Congenital Hypothyroidism** covering all of the
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

# Neonatal Diabetes Mellitus With Congenital Hypothyroidism (NDH Syndrome): A Comprehensive Disease Characteristics Report

**Disease:** Neonatal Diabetes Mellitus With Congenital Hypothyroidism (NDH syndrome)
**MONDO ID:** MONDO:0012436 · **OMIM:** #610199 · **Causal gene:** *GLIS3* (HGNC:28510; NCBI Gene 169792; UniProt Q8NEA6; 9p24.2)
**Category:** Mendelian (autosomal recessive)

---

## Summary

Neonatal Diabetes Mellitus with Congenital Hypothyroidism (NDH syndrome) is an ultra-rare autosomal-recessive Mendelian disorder caused by biallelic loss-of-function mutations in **GLIS3** (GLI-Similar 3), a Krüppel-like C2H2 zinc-finger transcription factor gene on chromosome 9p24.2. First defined molecularly by Senée and colleagues in 2006 ([PMID: 16715098](https://pubmed.ncbi.nlm.nih.gov/16715098/)), the syndrome couples **permanent neonatal diabetes** with **congenital hypothyroidism** as its two defining and near-obligate features, superimposed on a variable multi-organ phenotype that can include congenital glaucoma, hepatic (biliary) fibrosis/cirrhosis, polycystic/cystic kidney disease, sensorineural deafness, and exocrine pancreatic insufficiency.

The unifying mechanism is developmental: GLIS3 is a master transcriptional regulator required simultaneously in several organ programs. In the pancreas it transactivates **neurogenin 3 (Neurog3/Ngn3)** and binds directly to the regulatory regions of *Ins2*, *Slc2a2* (GLUT2), and *Mafa*, driving beta-cell specification, insulin production, and beta-cell survival; loss of GLIS3 therefore produces a severe developmental beta-cell deficiency and insulin-dependent diabetes rather than a channelopathy. In the thyroid, GLIS3 is required for follicular-cell maturation and thyroid-gene expression, so its loss produces congenital hypothyroidism (a "gland-in-situ" dyshormonogenesis-type defect rather than athyreosis in most cases). GLIS3 also localizes to the **primary cilium** and cooperates with the Hippo-pathway coactivator **WWTR1/TAZ**, explaining the cystic renal, hepatobiliary, and ocular manifestations.

Clinically, the most important consequence for the knowledge base is that GLIS3-NDH belongs to the **transcription-factor / beta-cell-development class of neonatal diabetes**, which is **insulin-dependent and NOT responsive to sulfonylureas** — a sharp contrast with KATP-channel (KCNJ11/ABCC8) neonatal diabetes. There is no cure. Management is lifelong, organ-directed supportive care: exogenous insulin, levothyroxine replacement, and treatment of hepatic, renal, and ophthalmic complications, with liver transplantation considered for life-limiting biliary cirrhosis. Prevention rests entirely on genetic counseling and cascade/carrier testing in at-risk (frequently consanguineous) families. This report synthesizes 14 confirmed findings from 32 reviewed papers across all 15 requested disease-characteristic domains. Evidence source types are flagged as [human clinical], [model organism], [in vitro], or [computational].

---

## 1. Disease Information

**Overview.** NDH syndrome is a monogenic (Mendelian) neonatal diabetes syndrome in which insulin-dependent diabetes presenting in the first weeks/months of life co-occurs with congenital hypothyroidism. It is a **developmental** endocrinopathy: the same transcription factor that fails to build the insulin-secreting beta cells also fails to build/maintain the thyroid follicular apparatus, and additionally disrupts cilium-dependent development of the kidney, biliary tree, and eye.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | #610199 (Neonatal diabetes mellitus with congenital hypothyroidism) |
| MONDO | MONDO:0012436 |
| Orphanet | ORPHA:79369 |
| Gene (HGNC) | *GLIS3* (HGNC:28510; NCBI Gene 169792; UniProt Q8NEA6), 9p24.2 |
| ICD-10 | P70.2 (neonatal diabetes) + E03.1 (congenital hypothyroidism without goitre) as component codes |
| ICD-11 | 5A11 (monogenic/neonatal diabetes) with 5A00.1 (congenital hypothyroidism) |
| MeSH | Diabetes Mellitus + Congenital Hypothyroidism (no single dedicated descriptor) |

**Synonyms / alternative names.** NDH syndrome; GLIS3-related neonatal diabetes and congenital hypothyroidism; Neonatal diabetes mellitus with congenital hypothyroidism syndrome; "GLIS3 syndrome."

**Source of information.** Findings here are derived from **aggregated, disease-level resources** [human clinical] — primarily published clinical case series (e.g., Dimitri et al., 12 patients, [PMID: 26259131](https://pubmed.ncbi.nlm.nih.gov/26259131/)), original gene-discovery reports ([PMID: 16715098](https://pubmed.ncbi.nlm.nih.gov/16715098/)), mechanistic model-organism/cell studies, and consanguineous-cohort monogenic-diabetes registries — not individual EHR extraction.

---

## 2. Etiology

**Primary cause (genetic).** NDH syndrome is caused by **biallelic (homozygous or compound heterozygous) loss-of-function mutations in GLIS3** [human clinical] ([PMID: 16715098](https://pubmed.ncbi.nlm.nih.gov/16715098/)). The original family carried a frameshift mutation predicting a truncated protein; two additional families carried deletions of the 11–12 most 5′ exons. The disorder is autosomal recessive with a loss-of-function mechanism.

> "this syndrome results from mutations in GLIS3, encoding GLI similar 3, a recently identified transcription factor. In the original family, we identified a frameshift mutation predicted to result in a truncated protein" — [PMID: 16715098](https://pubmed.ncbi.nlm.nih.gov/16715098/)

**Genetic risk factors.**
- **Causal variants:** biallelic GLIS3 frameshift, nonsense, splice, missense, and large multi-exon deletions (see Section 4).
- **Susceptibility/dosage series:** common SNPs at the GLIS3 locus are established GWAS susceptibility loci for **both type 1 and type 2 diabetes** ([PMID: 27813676](https://pubmed.ncbi.nlm.nih.gov/27813676/); [PMID: 23197416](https://pubmed.ncbi.nlm.nih.gov/23197416/)), and **rare monoallelic pathogenic variants increase type 2 diabetes risk** ([PMID: 38051360](https://pubmed.ncbi.nlm.nih.gov/38051360/)). Thus GLIS3 shows an allelic dosage continuum (Finding F011).
- **Consanguinity** is the dominant epidemiological risk amplifier because the disorder is recessive (Section 9).

**Environmental risk factors.** No specific environmental cause of the Mendelian syndrome is known; it is fully genetically determined. Sex, ethnicity, and non-genetic exposures do not cause NDH. However, in the *heterozygous* dosage context, gene–environment interaction is demonstrable: Glis3+/− mice on a **high-fat diet** develop diabetes due to impaired beta-cell-mass expansion, with GLIS3 regulating *Ccnd2* (cyclin D2) [model organism] ([PMID: 23197416](https://pubmed.ncbi.nlm.nih.gov/23197416/)).

**Protective factors.** No established genetic or environmental protective factors reduce risk of the biallelic Mendelian disease. (Not applicable — the disease is fully penetrant for neonatal diabetes given biallelic LOF.)

**Gene–environment interactions.** Relevant only to the susceptibility (heterozygous/common-variant) end of the spectrum: diet-induced metabolic demand unmasks beta-cell proliferation deficits via *Ccnd2* ([PMID: 23197416](https://pubmed.ncbi.nlm.nih.gov/23197416/)). For the syndromic biallelic disease, penetrance is essentially complete regardless of environment.

---

## 3. Phenotypes

NDH is defined by two obligate/near-obligate features plus a variable multi-organ spectrum. Frequencies below are from Dimitri et al. (n=12, [PMID: 26259131](https://pubmed.ncbi.nlm.nih.gov/26259131/)) and Senée et al. ([PMID: 16715098](https://pubmed.ncbi.nlm.nih.gov/16715098/)).

| Phenotype | Type | Onset | Frequency | Suggested HPO |
|---|---|---|---|---|
| Permanent neonatal diabetes mellitus | Lab/clinical (hyperglycemia, insulin deficiency) | Neonatal (first days–weeks) | ~100% (defining) | HP:0006202 / HP:0000857 |
| Intrauterine growth restriction / low birth weight | Physical | Congenital | Common | HP:0001511 (IUGR) |
| Congenital hypothyroidism | Lab/clinical | Congenital | Highly frequent (one compound-het patient lacked it) | HP:0000851 |
| Congenital glaucoma | Clinical sign | Congenital | Frequent | HP:0008007 |
| High hyperopia / short axial length | Lab/imaging | Congenital | Reported (distinctive) | HP:0000540 |
| Hepatic disease (hepatitis → cirrhosis/fibrosis, bile-duct paucity) | Clinical/pathology | Infancy | Common | HP:0001394 / HP:0002908 |
| Cystic renal dysplasia / polycystic kidneys | Imaging/clinical | Congenital–infancy | Common | HP:0000107 / HP:0000113 |
| Sensorineural deafness | Clinical | Congenital/infancy | Reported | HP:0000407 |
| Exocrine pancreatic insufficiency | Lab/clinical | Infancy | Reported | HP:0001738 |
| Craniosynostosis, hiatus hernia, ASD, splenic cyst, choanal atresia | Physical/structural | Congenital | Rare/novel | HP:0001363, HP:0002036, HP:0001631, —, HP:0000453 |

> "All patients presented with neonatal diabetes with a range of insulin sensitivities. Thyroid disease varied among patients. Hepatic and renal disease was common with liver dysfunction ranging from hepatitis to cirrhosis; cystic dysplasia was the most common renal manifestation" — [PMID: 26259131](https://pubmed.ncbi.nlm.nih.gov/26259131/)

> "We describe new presenting features in patients with GLIS3 mutations, including craniosynostosis, hiatus hernia, atrial septal defect, splenic cyst, and choanal atresia and confirm further cases with sensorineural deafness and exocrine pancreatic insufficiency" — [PMID: 26259131](https://pubmed.ncbi.nlm.nih.gov/26259131/)

**Severity/progression/QoL.** Diabetes is severe and lifelong (insulin-dependent from the neonatal period). Hypothyroidism, if untreated, causes irreversible intellectual disability and short stature; treated early it is manageable. Hepatic and renal disease can be **life-limiting and progressive**. Overall, affected children carry a high cumulative disease burden across endocrine, hepatic, renal, ophthalmic, and auditory systems, with major QoL impact from insulin dependence, developmental risk, and organ complications.

---

## 4. Genetic / Molecular Information

**Causal gene.** *GLIS3* (GLI-similar 3), a C2H2 zinc-finger transcription factor at **9p24.2**; disease OMIM #610199. GLIS3 is expressed in the pancreas from early developmental stages, with greater expression in beta cells than other pancreatic tissues ([PMID: 16715098](https://pubmed.ncbi.nlm.nih.gov/16715098/)). Its DNA-binding domain contains a repeated Cys2/His2 zinc-finger motif ([PMID: 28523428](https://pubmed.ncbi.nlm.nih.gov/28523428/)).

> "GLIS3 is expressed in the pancreas from early developmental stages, with greater expression in beta cells than in other pancreatic tissues" — [PMID: 16715098](https://pubmed.ncbi.nlm.nih.gov/16715098/)

**Pathogenic variant classes (all germline, biallelic for the syndrome):**
- **Frameshift** → truncated protein (original Senée family, [PMID: 16715098](https://pubmed.ncbi.nlm.nih.gov/16715098/)).
- **Large multi-exon deletions** (deletion of the 11–12 most 5′ exons; homozygous deletions including non-coding exon 1 + coding exon 2 in Saudi siblings, [PMID: 40583116](https://pubmed.ncbi.nlm.nih.gov/40583116/)).
- **Missense / nonsense / splice-site** variants that reduce GLIS3 transactivation of the *INS* promoter — of 105 rare variants resequenced in 5,471 RaDiO individuals, functional luciferase assays showed **49 variants decreased INS-promoter activation** [in vitro/human] ([PMID: 38051360](https://pubmed.ncbi.nlm.nih.gov/38051360/)). Variants classified per ACMG/AMP (functional assays addressing the PS3 criterion).

**Allele frequency & origin.** Pathogenic biallelic variants are individually ultra-rare; common tag SNPs at the locus are frequent (population susceptibility variants). All disease variants are **germline** (no somatic component; this is not a neoplastic disorder).

**Functional consequence.** **Loss of function** — reduced/absent GLIS3 transcriptional activity, i.e., failure to transactivate downstream targets. A critical structural determinant is the C-terminal **P/LPXY motif** recognized by WWTR1/TAZ; mutating this motif abrogates GLIS3 transcriptional activity ([PMID: 19273592](https://pubmed.ncbi.nlm.nih.gov/19273592/)).

**Dosage/allelic series (Finding F011).**

> "Rare pathogenic, bi-allelic mutations in GLIS3 cause syndromic neonatal diabetes whereas frequent SNPs at this locus associate with common type 2 diabetes risk" — [PMID: 38051360](https://pubmed.ncbi.nlm.nih.gov/38051360/)

| GLIS3 genotype | Phenotype |
|---|---|
| Biallelic LOF | Syndromic permanent neonatal diabetes + congenital hypothyroidism (NDH) |
| Monoallelic pathogenic | Increased type 2 diabetes risk; subgroup sulfonylurea-sensitive ([PMID: 38051360](https://pubmed.ncbi.nlm.nih.gov/38051360/)) |
| Common SNPs | GWAS susceptibility for type 1 and type 2 diabetes ([PMID: 27813676](https://pubmed.ncbi.nlm.nih.gov/27813676/)) |

**Modifier genes / epigenetics / chromosomal abnormalities.** No specific modifier genes are established for NDH. Oligogenic contribution and epigenetic/penetrance factors have been raised generally in congenital-hypothyroidism cohorts that include GLIS3 ([PMID: 36125728](https://pubmed.ncbi.nlm.nih.gov/36125728/)) but are not proven modifiers of GLIS3-NDH. The relevant "chromosomal" lesions are the large 9p24.2 GLIS3 deletions noted above, not aneuploidy or translocations.

---

## 5. Environmental Information

**Environmental factors / toxins / radiation / infectious agents:** **Not applicable** — NDH is a fully genetic, non-infectious Mendelian disorder. No toxin, pollutant, occupational exposure, or pathogen causes or triggers it.

**Lifestyle factors:** Not causal for the biallelic syndrome. High-fat diet is relevant only in the heterozygous/susceptibility context (beta-cell-mass expansion failure in Glis3+/− mice, [PMID: 23197416](https://pubmed.ncbi.nlm.nih.gov/23197416/)), not for the neonatal disease.

**Consanguinity** (a population-structure factor rather than an environmental exposure) markedly elevates recessive-disease risk (Section 9).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

```
1. Biallelic loss-of-function mutation in GLIS3 (9p24.2)
        │  results in
        ▼
2. Loss/reduction of functional GLIS3 zinc-finger transcription factor
   (nuclear transactivation + primary-cilium localization both impaired)
        │  leads to (branches to 4 organ programs)
        ├───────────────► PANCREAS BRANCH
        │  3a. Failure to transactivate Neurog3 (Ngn3) (>90% reduction in
        │       Glis3-/- embryos) AND loss of direct GLIS3 binding to
        │       Ins2, Slc2a2/GLUT2, Mafa regulatory regions
        │            │ results in
        │  4a. Failed endocrine (beta-cell) specification + reduced beta-cell
        │       mass + reduced insulin transcription
        │            │ leads to
        │  5a. Severe insulin deficiency  ──►  PERMANENT NEONATAL DIABETES
        │       (plus GLIS3-loss sensitizes surviving beta cells to apoptosis
        │        via SRp55/Bim-splicing, accelerating beta-cell loss)
        │
        ├───────────────► THYROID BRANCH
        │  3b. Loss of GLIS3-driven thyroid-gene expression from ~E15.5
        │            │ results in
        │  4b. Impaired thyroid follicular-cell maturation/function
        │            │ leads to
        │  5b. CONGENITAL HYPOTHYROIDISM (gland-in-situ / dyshormonogenesis type)
        │
        ├───────────────► CILIARY / WWTR1-TAZ BRANCH (kidney, liver, eye)
        │  3c. Loss of ciliary GLIS3 signaling + loss of GLIS3–WWTR1/TAZ
        │       transactivation (P/LPXY motif); shortened renal cilia
        │            │ results in
        │  4c. Reduced urine flow, abnormal tubulogenesis; abnormal bile-duct
        │       development; anterior-segment eye maldevelopment
        │            │ leads to
        │  5c. POLYCYSTIC/CYSTIC KIDNEY DISEASE, BILIARY CIRRHOSIS/bile-duct
        │       paucity, CONGENITAL GLAUCOMA (with high hyperopia)
        │
        └───────────────► OTHER (sensorineural deafness, exocrine pancreatic
                          insufficiency, rare structural anomalies)
```

### Detail by category

**Molecular pathways.** The dominant node is **GLIS3-dependent transcription**. GLIS3 transactivates *Neurog3* (the master pro-endocrine bHLH factor) and co-occupies islet regulatory regions with other islet transcription factors, directly binding *Ins2*, *Slc2a2* (GLUT2), and *Mafa* (ChIP-seq) [model organism] ([PMID: 31340201](https://pubmed.ncbi.nlm.nih.gov/31340201/)). It intersects the **Hippo pathway** via WWTR1/TAZ coactivation ([PMID: 19273592](https://pubmed.ncbi.nlm.nih.gov/19273592/)) and functions in a **primary-cilium-associated** signaling context.

> "GLIS3 controls islet differentiation by transactivating neurogenin 3 (Ngn3)" — [PMID: 27813676](https://pubmed.ncbi.nlm.nih.gov/27813676/)

> "with global Glis3-knockout mice suffering from severe hyperglycemia and dying by post-natal day 11" — [PMID: 31340201](https://pubmed.ncbi.nlm.nih.gov/31340201/)

**Cellular processes.** (i) Cell-fate specification/differentiation of pancreatic endocrine progenitors; (ii) beta-cell maintenance and identity in adults ([PMID: 23197416](https://pubmed.ncbi.nlm.nih.gov/23197416/)); (iii) **intrinsic (mitochondrial) apoptosis** of beta cells when GLIS3 is lost.

> "TAM-mediated beta cell-specific inactivation of Glis3 in adult mice downregulates insulin expression, leading to hyperglycaemia and subsequently enhanced beta cell apoptosis" — [PMID: 23197416](https://pubmed.ncbi.nlm.nih.gov/23197416/)

**Beta-cell apoptosis mechanism (Finding F009).** GLIS3 knockdown in INS-1E cells, primary rat beta cells, and human islets lowered MafA, Ins2, and Glut2 and impaired glucose oxidation and insulin secretion; it increased apoptosis basally and **sensitized cells to cytokine (IL-1β + IFN-γ) and palmitate-induced death** — the mediators of beta-cell loss in type 1 and type 2 diabetes respectively — via the intrinsic pathway (cytochrome c release, Bax translocation, caspase 9/3). Mechanistically, GLIS3 loss inhibits the splicing factor **SRp55**, shifting alternative splicing of the BH3-only protein **Bim** toward the pro-death **BimS** variant; Bim knockdown rescued the phenotype [in vitro] ([PMID: 23737756](https://pubmed.ncbi.nlm.nih.gov/23737756/); [PMID: 29246973](https://pubmed.ncbi.nlm.nih.gov/29246973/)).

> "GLIS3 KD increased beta cell apoptosis basally and sensitized the cells to death induced by pro-inflammatory cytokines (interleukin 1β + interferon-γ) or palmitate" — [PMID: 23737756](https://pubmed.ncbi.nlm.nih.gov/23737756/)

> "modulation of alternative splicing of the pro-apoptotic BH3-only protein Bim, favouring expression of the pro-death variant BimS via inhibition of the splicing factor SRp55" — [PMID: 23737756](https://pubmed.ncbi.nlm.nih.gov/23737756/)

**Protein dysfunction.** LOF of the GLIS3 zinc-finger transcription factor: truncation, deletion, or missense changes reduce DNA binding/transactivation and disrupt the C-terminal WWTR1/TAZ-binding P/LPXY motif ([PMID: 19273592](https://pubmed.ncbi.nlm.nih.gov/19273592/)).

**Metabolic changes.** Downstream of beta-cell failure: absolute insulin deficiency → neonatal hyperglycemia, ketoacidosis risk, and impaired glucose oxidation in beta cells ([PMID: 23737756](https://pubmed.ncbi.nlm.nih.gov/23737756/)). Thyroid-hormone deficiency perturbs systemic metabolism.

**Immune involvement.** Not autoimmune — this is a developmental (autoantibody-negative) diabetes. However, GLIS3-deficient beta cells are hypersensitized to pro-inflammatory cytokine killing, mechanistically linking GLIS3 to the T1D susceptibility signal ([PMID: 23737756](https://pubmed.ncbi.nlm.nih.gov/23737756/)).

**Tissue damage mechanisms.** Beta-cell apoptosis (islet); biliary cirrhosis from abnormal bile-duct development/paucity (liver, [PMID: 36917836](https://pubmed.ncbi.nlm.nih.gov/36917836/)); cyst formation from shortened cilia and reduced urine flow (kidney) [model organism] ([PMID: 19609364](https://pubmed.ncbi.nlm.nih.gov/19609364/)).

> "The cilia on the surface of the renal tubular epithelium were significantly shorter in the pc mutant than in wild-type, suggesting that shortened cilia resulted in a decrease in driving force and, in turn, a reduction in urine flow rate" — [PMID: 19609364](https://pubmed.ncbi.nlm.nih.gov/19609364/)

**Thyroid mechanism (Finding F006).** GLIS3 protein is first detectable at E15.5 of murine thyroid development, coinciding with expression of GLIS3 target genes; thyroid-specific Glis3-KO mice show dysregulated thyroid gene expression ([PMID: 37461635](https://pubmed.ncbi.nlm.nih.gov/37461635/)).

> "Loss of GLI-Similar 3 (GLIS3) function in mice and humans causes congenital hypothyroidism (CH)" — [PMID: 37461635](https://pubmed.ncbi.nlm.nih.gov/37461635/)

**Suggested GO / CL terms.** Biological process: GO:0030154 (cell differentiation), GO:0003309 (type B pancreatic cell differentiation), GO:0006006 (glucose metabolic process), GO:0006915 (apoptotic process), GO:0060271 (cilium assembly), GO:0035148 (tube formation). Cell types: CL:0000169 (type B pancreatic/beta cell), CL:0002258 (thyroid follicular cell), CL:1000454 (kidney collecting-duct epithelial cell), CL:0000068 (duct epithelial cell / cholangiocyte).

---

## 7. Anatomical Structures Affected

**Organ level (primary).** Pancreatic islets (endocrine pancreas), thyroid gland. **Secondary/associated:** liver and biliary tree, kidneys, eyes (anterior segment), inner ear (cochlea), exocrine pancreas, and rarely skull sutures, diaphragm/esophageal hiatus, heart (atrial septum), spleen, choanae.

**Body systems.** Endocrine (primary), hepatobiliary/digestive, renal/urinary, ophthalmic/nervous (sensory), auditory.

**Tissue & cell level.**
- Pancreatic **beta cells** (CL:0000169) — reduced mass, impaired function/survival.
- **Thyroid follicular cells** (CL:0002258) — impaired maturation.
- **Renal tubular epithelium** — shortened cilia, cyst formation (CL:1000454).
- **Cholangiocytes / bile-duct epithelium** — bile-duct paucity/abnormal development.

**Subcellular level.** **Nucleus** (GO:0005634 — GLIS3 transactivation) and the **primary cilium** (GO:0005929) are the two key compartments; GLIS3 localizes to both ([PMID: 19273592](https://pubmed.ncbi.nlm.nih.gov/19273592/)). Beta-cell death proceeds through **mitochondria** (GO:0005739; intrinsic apoptosis).

> "We demonstrate that Glis3 localizes to the primary cilium, suggesting that Glis3 is part of a cilium-associated signaling pathway" — [PMID: 19273592](https://pubmed.ncbi.nlm.nih.gov/19273592/)

**Localization / lateralization.** Systemic/bilateral where paired (kidneys, eyes, cochleae). Suggested UBERON: UBERON:0000006 (islet of Langerhans), UBERON:0002046 (thyroid gland), UBERON:0002107 (liver), UBERON:0002113 (kidney), UBERON:0000970 (eye), UBERON:0001844 (cochlea).

---

## 8. Temporal Development

**Onset.** **Congenital / neonatal.** Diabetes typically presents within the first days to weeks of life (permanent neonatal diabetes, <6 months by definition), frequently with **intrauterine growth restriction**, hyperglycemia, and sometimes diabetic ketoacidosis. Congenital hypothyroidism is present from birth (detectable on newborn screening). Onset pattern is **congenital/acute** for diabetes and **congenital/insidious** for the hepatic and renal disease, which may declare over infancy.

**Progression.** Diabetes is **permanent and lifelong** (not transient/self-limited). Hepatic disease can be **progressive** (hepatitis → fibrosis → cirrhosis), and renal cystic disease may progress. Overall course is chronic and, for some organs, life-limiting.

**Patterns / critical periods.** No spontaneous remission of the diabetes. The critical intervention windows are (i) immediate neonatal insulin initiation to control hyperglycemia and (ii) **early levothyroxine** to prevent irreversible neurodevelopmental injury from hypothyroidism. The beta-cell-development defect occurs in utero and is not reversible postnatally.

---

## 9. Inheritance and Population

**Epidemiology.** Neonatal diabetes mellitus overall has an incidence of **~1 in 90,000 live births** (range 1:90,000–1:160,000) [human clinical] ([PMID: 38752501](https://pubmed.ncbi.nlm.nih.gov/38752501/)). GLIS3-related NDH is a **very rare recessive subset (<1% of NDM)**; on the order of ~20 families/patients are reported in the literature (Finding F013).

> "These disorders are rare and the incidence is approximately 1 in 90,000 live births" — [PMID: 38752501](https://pubmed.ncbi.nlm.nih.gov/38752501/)

**Inheritance.** **Autosomal recessive**, with **high penetrance for neonatal diabetes** and **variable expressivity** for the other organ features (e.g., one compound-heterozygous patient lacked congenital hypothyroidism, [PMID: 26259131](https://pubmed.ncbi.nlm.nih.gov/26259131/)). No genetic anticipation (not a repeat-expansion disorder). Germline mosaicism not specifically reported.

**Consanguinity & founder effects.** Recessive syndromic neonatal diabetes is strongly over-represented in **consanguineous** Middle Eastern/North African and South Asian populations, where homozygous GLIS3 large deletions and point mutations occur ([PMID: 40583116](https://pubmed.ncbi.nlm.nih.gov/40583116/); [PMID: 37897565](https://pubmed.ncbi.nlm.nih.gov/37897565/); [PMID: 42468610](https://pubmed.ncbi.nlm.nih.gov/42468610/); [PMID: 41275391](https://pubmed.ncbi.nlm.nih.gov/41275391/)).

> "Monogenic diabetes is estimated to account for 1-6% of paediatric diabetes cases in primarily non-consanguineous populations, while the incidence and genetic spectrum in consanguineous regions are insufficiently defined" — [PMID: 37897565](https://pubmed.ncbi.nlm.nih.gov/37897565/)

In a Saudi cohort with 81% consanguinity, autosomal-recessive syndromic and permanent neonatal diabetes predominated ([PMID: 42468610](https://pubmed.ncbi.nlm.nih.gov/42468610/)); Sudanese cohorts likewise showed a predominance of syndromic recessive forms ([PMID: 41275391](https://pubmed.ncbi.nlm.nih.gov/41275391/)).

**Demographics.** No strong sex bias (recessive). Carrier frequency is low in outbred populations, higher within consanguineous kindreds. Age distribution: affected individuals identified in the neonatal period.

---

## 10. Diagnostics

**Clinical/laboratory tests.**
- **Glucose/insulin/C-peptide:** persistent neonatal hyperglycemia with low insulin/C-peptide (insulin-deficient), autoantibody-negative.
- **Thyroid function:** low free T4 with elevated TSH (primary congenital hypothyroidism); thyroid imaging typically shows a **gland in situ** (dyshormonogenesis pattern) rather than athyreosis in most cases.
- **Hepatic panel:** transaminitis/cholestasis; explant/biopsy histology shows **biliary cirrhosis / bile-duct paucity** ([PMID: 36917836](https://pubmed.ncbi.nlm.nih.gov/36917836/)).
- **Renal imaging (ultrasound):** cystic dysplasia / polycystic kidneys ([PMID: 26259131](https://pubmed.ncbi.nlm.nih.gov/26259131/)).
- **Ophthalmology:** congenital glaucoma with **high hyperopia and short axial length** ([PMID: 40583116](https://pubmed.ncbi.nlm.nih.gov/40583116/)).
- **Audiology:** sensorineural hearing testing.
- **Pancreatic exocrine:** fecal elastase for exocrine insufficiency.

> "ophthalmic assessments revealed congenital glaucoma, high hyperopia, and short axial length of the globe" — [PMID: 40583116](https://pubmed.ncbi.nlm.nih.gov/40583116/)

**Genetic testing (definitive).** Molecular confirmation is essential and **directly influences prognosis and treatment**.

> "molecular diagnosis is crucial, as it directly influences prognosis and treatment - particularly the potential responsiveness to sulfonylureas in ATP-sensitive potassium (KATP)-channel-related NDM" — [PMID: 41769619](https://pubmed.ncbi.nlm.nih.gov/41769619/)

Recommended approach:
- **Targeted neonatal-diabetes / monogenic-diabetes NGS gene panel** (must include GLIS3 alongside KCNJ11, ABCC8, INS, EIF2AK3, PDX1, PTF1A, GATA6, RFX6, NEUROG3, FOXP3, etc.).
- **WES/WGS** for atypical/syndromic presentations and novel-variant discovery ([PMID: 38051360](https://pubmed.ncbi.nlm.nih.gov/38051360/); [PMID: 42468610](https://pubmed.ncbi.nlm.nih.gov/42468610/)).
- **Chromosomal microarray / deletion analysis** is important because GLIS3 large multi-exon and whole-gene deletions occur ([PMID: 16715098](https://pubmed.ncbi.nlm.nih.gov/16715098/); [PMID: 40583116](https://pubmed.ncbi.nlm.nih.gov/40583116/)) and may be missed by SNV-only panels.
- Variant interpretation per **ACMG/AMP**; functional INS-promoter luciferase assays can supply PS3-level evidence ([PMID: 38051360](https://pubmed.ncbi.nlm.nih.gov/38051360/)).

**Clinical criteria / differential diagnosis.** Diagnosis rests on the combination of **permanent neonatal diabetes + congenital hypothyroidism** plus GLIS3 confirmation. Key differentials (Finding F014):

| Gene(s) | Mechanistic class | Distinguishing feature vs GLIS3 |
|---|---|---|
| KCNJ11 / ABCC8 | KATP-channel | **Sulfonylurea-responsive**; usually no CH |
| INS | insulin gene / ER stress | Isolated PNDM; no CH |
| EIF2AK3 (Wolcott-Rallison) | ER stress | Epiphyseal dysplasia, liver/renal, but **not CH** |
| GATA6 / GATA4 / PDX1 | pancreatic agenesis/hypoplasia | Exocrine insufficiency + cardiac/gallbladder anomalies; labile diabetes ([PMID: 41006196](https://pubmed.ncbi.nlm.nih.gov/41006196/)) |
| FOXP3 (IPEX) | immune dysregulation | Autoimmune enteropathy; thyroiditis (acquired, not congenital) |
| CISD2 (Wolfram syndrome 2) | Ca²⁺/ER | Later onset, optic atrophy ([PMID: 40189101](https://pubmed.ncbi.nlm.nih.gov/40189101/)) |
| **GLIS3** | **developmental TF** | **Neonatal diabetes + congenital hypothyroidism** (± glaucoma, biliary cirrhosis, polycystic kidneys) |

> "NDM is caused by single-gene mutations that disrupt pancreatic β-cell function or development" — [PMID: 41614934](https://pubmed.ncbi.nlm.nih.gov/41614934/)

**Screening.** Congenital hypothyroidism is captured by routine **newborn screening (TSH/T4)**; neonatal hyperglycemia prompts glucose testing. Cascade genetic testing in families follows molecular diagnosis.

---

## 11. Outcome / Prognosis

**Survival/mortality.** No formal survival statistics exist for this ultra-rare disorder. Prognosis is **guarded** and driven by the sum of complications: brittle insulin-dependent diabetes, and potentially **life-limiting hepatic (biliary cirrhosis) and renal disease** ([PMID: 36917836](https://pubmed.ncbi.nlm.nih.gov/36917836/)). Global Glis3-knockout mice die by postnatal day ~11 from severe hyperglycemia ([PMID: 31340201](https://pubmed.ncbi.nlm.nih.gov/31340201/)), underscoring the severity of complete loss; humans survive with intensive supportive care.

**Morbidity/function.** High: lifelong insulin dependence, neurodevelopmental risk from hypothyroidism (mitigated by early treatment), visual impairment from glaucoma, hearing loss, malnutrition from exocrine insufficiency, and organ-failure risk. QoL impact is substantial and multi-domain.

**Complications & recovery.** Progressive liver disease may require **liver transplantation**; renal disease may progress toward insufficiency; brittle diabetes complicates post-transplant management.

> "GLIS3 mutations need to be added to the list of non-syndromic causes of bile duct paucity in the liver. Liver transplantation should be considered in patients with life-limiting complications related to liver disease" — [PMID: 36917836](https://pubmed.ncbi.nlm.nih.gov/36917836/)

**Prognostic factors.** Severity/completeness of GLIS3 LOF, presence and progression of hepatic/renal disease, and adequacy of early metabolic and thyroid control.

---

## 12. Treatment

There is **no cure**; management is **lifelong, organ-directed supportive care** (Findings F002, F005, F010).

**Pharmacotherapy.**
- **Insulin (exogenous)** — the cornerstone for the diabetes. GLIS3-NDH is a **beta-cell-developmental/deficiency** diabetes and is **insulin-dependent** (NCIT: C2271 Insulin). It is **NOT sulfonylurea-responsive**, in sharp contrast to KATP-channel NDM.

> "patients with ABCC8 or KCNJ11 mutations treated with insulin therapy can switch to hypoglycemic sulfonylureas (SU). These drugs close the KATP channel binding the SUR1 subunit of the potassium channel and restoring insulin secretion after a meal" — [PMID: 37251668](https://pubmed.ncbi.nlm.nih.gov/37251668/)

- **Levothyroxine** — lifelong thyroid-hormone replacement for congenital hypothyroidism (NCIT: C29101 Levothyroxine Sodium), started as early as possible to protect neurodevelopment.
- **Pancreatic enzyme replacement** for exocrine pancreatic insufficiency.
- **Anti-glaucoma therapy / surgery** for congenital glaucoma.

**Pharmacogenomics.** The single most actionable pharmacogenomic point is the **genotype-defined therapeutic split**: molecular diagnosis distinguishes sulfonylurea-responsive (KATP) from insulin-dependent (GLIS3/developmental) NDM ([PMID: 41769619](https://pubmed.ncbi.nlm.nih.gov/41769619/); [PMID: 41614934](https://pubmed.ncbi.nlm.nih.gov/41614934/)). Note that *monoallelic* GLIS3 T2D patients can be sulfonylurea-sensitive ([PMID: 38051360](https://pubmed.ncbi.nlm.nih.gov/38051360/)) — this does **not** extend to biallelic NDH.

**Surgical/interventional.** **Liver transplantation** for life-limiting biliary cirrhosis (NCIT: C15311 Liver Transplantation); combined multi-organ transplantation (liver ± pancreas ± kidney) has been considered but performed as liver-alone in reported cases ([PMID: 36917836](https://pubmed.ncbi.nlm.nih.gov/36917836/)). Glaucoma surgery as needed.

> "Histology demonstrated predominantly biliary cirrhosis consistent with abnormal bile duct development" — [PMID: 36917836](https://pubmed.ncbi.nlm.nih.gov/36917836/)

**Advanced/experimental therapeutics.** No approved gene, cell, or RNA therapy exists for GLIS3-NDH. Because the defect is developmental (failed beta-cell formation in utero), gene replacement faces the challenge that the target cells are largely absent — making **stem-cell-derived beta-cell replacement** a more plausible future avenue than in-situ gene correction. Human iPSC/hPSC CRISPR models confirm the conserved GLIS3 requirement in human pancreatic differentiation ([PMID: 27133796](https://pubmed.ncbi.nlm.nih.gov/27133796/)), providing a platform for such work. No NCT-registered GLIS3-specific trials were identified.

**Treatment strategy.** Genotype-guided precision medicine: confirm GLIS3, commit to insulin (not a therapeutic sulfonylurea trial beyond diagnostic exclusion), replace thyroid hormone early, and institute multidisciplinary surveillance (hepatology, nephrology, ophthalmology, audiology, nutrition).

> "necessitating a shift from symptomatic management to precision medicine" — [PMID: 41614934](https://pubmed.ncbi.nlm.nih.gov/41614934/)

---

## 13. Prevention

- **Primary prevention:** None possible for the biallelic Mendelian disease (fully genetically determined). Prevention operates at the **reproductive/genetic-counseling** level.
- **Secondary prevention (early detection):** Newborn screening detects congenital hypothyroidism (TSH/T4); prompt recognition of neonatal hyperglycemia enables early insulin and molecular diagnosis. Early levothyroxine prevents irreversible neurodevelopmental injury.
- **Tertiary prevention:** Multidisciplinary surveillance and management of hepatic, renal, ophthalmic, and auditory complications to limit disability.
- **Genetic counseling / screening:** The key preventive strategy. Autosomal-recessive counseling for consanguineous families, **carrier/cascade testing**, and options for **prenatal diagnosis / preimplantation genetic testing** once the familial GLIS3 variant(s) are known ([PMID: 42468610](https://pubmed.ncbi.nlm.nih.gov/42468610/); [PMID: 41275391](https://pubmed.ncbi.nlm.nih.gov/41275391/)).
- **Immunization / public-health / environmental interventions:** Not applicable (non-infectious, non-environmental).

---

## 14. Other Species / Natural Disease

- **Taxonomy of models/orthologs:** *Mus musculus* (NCBI:txid10090), *Oryzias latipes* (medaka; NCBI:txid8090). GLIS3 is evolutionarily conserved, and its disease mechanisms are conserved across mouse, fish, and human ([PMID: 19609364](https://pubmed.ncbi.nlm.nih.gov/19609364/); [PMID: 27133796](https://pubmed.ncbi.nlm.nih.gov/27133796/)).
- **Orthologous genes:** mouse *Glis3*, medaka *glis3*.
- **Natural disease:** No well-documented naturally occurring companion-animal (OMIA) equivalent of GLIS3-NDH was identified; the "natural disease" model is the **medaka *pc* mutant**, which arose from a transposon insertion in *glis3* and models polycystic kidney disease ([PMID: 19609364](https://pubmed.ncbi.nlm.nih.gov/19609364/)).

> "the Gli-similar3 (glis3) gene was identified as the causal gene of the medaka pc mutant, a model of PKD" — [PMID: 19609364](https://pubmed.ncbi.nlm.nih.gov/19609364/)

- **Comparative biology:** Glis3(zf/zf) mice recapitulate the human syndrome (diabetes + PKD), demonstrating strong cross-species conservation of both the beta-cell and ciliary-renal mechanisms.

---

## 15. Model Organisms

| Model | Type | Key phenotype / use | PMID |
|---|---|---|---|
| Global Glis3−/− mouse | knockout, mammalian | Severe hyperglycemia; death by P~11; near-absent insulin; >90% Ngn3 reduction in embryos | [31340201](https://pubmed.ncbi.nlm.nih.gov/31340201/), [27813676](https://pubmed.ncbi.nlm.nih.gov/27813676/) |
| Glis3(zf/zf) mouse | hypomorph/mutant | Diabetes **+ polycystic kidney disease** — recapitulates human NDH | [19273592](https://pubmed.ncbi.nlm.nih.gov/19273592/) |
| Beta-cell-specific Glis3 KO (RipCre / RosaCreERT2, TAM-inducible) | conditional | Insulin downregulation → hyperglycemia + beta-cell apoptosis; proves adult maintenance role | [23197416](https://pubmed.ncbi.nlm.nih.gov/23197416/) |
| Glis3+/− mouse on high-fat diet | heterozygous + environment | Diabetes from impaired beta-cell-mass expansion via Ccnd2 | [23197416](https://pubmed.ncbi.nlm.nih.gov/23197416/) |
| Thyroid-specific Glis3 KO mouse | conditional | Dysregulated thyroid gene expression; GLIS3 protein from E15.5 | [37461635](https://pubmed.ncbi.nlm.nih.gov/37461635/) |
| Medaka *pc* mutant (glis3 transposon insertion) | fish | Polycystic kidney disease from shortened renal cilia, reduced urine flow | [19609364](https://pubmed.ncbi.nlm.nih.gov/19609364/) |
| Human iPSC/hPSC CRISPR/TALEN (GLIS3 among 8 TFs) | in vitro/cellular | Confirms conserved GLIS3 requirement in human pancreatic differentiation | [27133796](https://pubmed.ncbi.nlm.nih.gov/27133796/) |
| INS-1E, primary rat/human islets (GLIS3 KD) | cellular | Beta-cell apoptosis via SRp55/Bim splicing | [23737756](https://pubmed.ncbi.nlm.nih.gov/23737756/) |

> "These mice display abnormalities very similar to those of patients with neonatal diabetes and hypothyroidism syndrome, including the development of diabetes and polycystic kidney disease" — [PMID: 19273592](https://pubmed.ncbi.nlm.nih.gov/19273592/)

**Model characteristics / limitations.** Mouse and medaka models faithfully reproduce the diabetes and renal-cystic components; conditional models successfully dissect organ-specific roles. Limitations: the ocular (high hyperopia/glaucoma) and biliary-cirrhosis phenotypes are less fully modeled, and species differences (e.g., a "potentially divergent role of NGN3 in humans and mice," [PMID: 27133796](https://pubmed.ncbi.nlm.nih.gov/27133796/)) mean human iPSC systems are important complements. Resources: MGI, IMPC, ZFIN/medaka stocks; human iPSC lines from CRISPR studies.

---

## Mechanistic Model / Interpretation

The entire NDH phenotype is best understood as the **pleiotropic failure of a single developmental transcription factor** deployed in parallel organ programs. GLIS3 is not a metabolic enzyme or an ion channel — it is an upstream *builder*. Where KATP-channel neonatal diabetes reflects a **functional** secretory defect in otherwise-formed beta cells (and is therefore drug-reversible with sulfonylureas), GLIS3-NDH reflects a **structural/developmental** deficit: the beta cells are never adequately specified (Ngn3 collapse) and the few that form are hypofunctional and apoptosis-prone (SRp55→BimS). This is the mechanistic reason the two disorders diverge so completely in treatment — a distinction that molecular diagnosis makes actionable (F005, F014).

The same logic explains the multi-organ reach. Because GLIS3 operates both as a **nuclear transactivator** and as a **cilium-associated / WWTR1-TAZ-coupled** factor, its loss simultaneously derails endocrine-pancreas development, thyroid follicular maturation, and cilium-dependent morphogenesis of kidney, biliary tree, and eye. The disorder is thus a "developmental transcription-factor syndrome" whose organ list is essentially the intersection of GLIS3's expression domains and its two molecular modes of action.

```
                    GLIS3 (single TF, two modes)
             ┌──────────────┴───────────────┐
       NUCLEAR TRANSACTIVATION          PRIMARY CILIUM + WWTR1/TAZ
       (Ngn3, Ins2, Glut2, MafA)        (P/LPXY motif; ciliary signaling)
             │                                    │
   Beta-cell + thyroid programs         Kidney / bile-duct / eye programs
             │                                    │
   Neonatal diabetes + CH               PKD + biliary cirrhosis + glaucoma
```

---

## Evidence Base

| PMID | Study type | Contribution |
|---|---|---|
| [16715098](https://pubmed.ncbi.nlm.nih.gov/16715098/) | Human gene discovery | Establishes biallelic GLIS3 LOF as cause; defines core syndrome |
| [26259131](https://pubmed.ncbi.nlm.nih.gov/26259131/) | Human case series (n=12) | Phenotypic spectrum, frequencies, variability |
| [27813676](https://pubmed.ncbi.nlm.nih.gov/27813676/) | Mouse/gene-dosage | GLIS3→Ngn3; GWAS T1D/T2D link |
| [31340201](https://pubmed.ncbi.nlm.nih.gov/31340201/) | Mouse/ChIP-seq | Direct binding to Ins2/Glut2/MafA; lethal global KO |
| [23197416](https://pubmed.ncbi.nlm.nih.gov/23197416/) | Mouse conditional | Adult beta-cell maintenance; Ccnd2/diet interaction |
| [23737756](https://pubmed.ncbi.nlm.nih.gov/23737756/) | In vitro/islets | Beta-cell apoptosis via SRp55/BimS |
| [29246973](https://pubmed.ncbi.nlm.nih.gov/29246973/) | In vitro | SRp55 splicing network in beta cells |
| [37461635](https://pubmed.ncbi.nlm.nih.gov/37461635/) | Mouse thyroid KO | GLIS3 in thyroid development/CH |
| [19273592](https://pubmed.ncbi.nlm.nih.gov/19273592/) | Mouse | Cilium localization; WWTR1/TAZ; PKD |
| [19609364](https://pubmed.ncbi.nlm.nih.gov/19609364/) | Medaka | glis3/cilia/urine-flow renal-cyst mechanism |
| [36917836](https://pubmed.ncbi.nlm.nih.gov/36917836/) | Human explant pathology | Biliary cirrhosis/bile-duct paucity; transplant |
| [40583116](https://pubmed.ncbi.nlm.nih.gov/40583116/) | Human siblings | Congenital glaucoma + high hyperopia; large deletion |
| [38051360](https://pubmed.ncbi.nlm.nih.gov/38051360/) | Human resequencing + functional | Allelic dosage; ACMG functional assays; monoallelic T2D |
| [41769619](https://pubmed.ncbi.nlm.nih.gov/41769619/) / [37251668](https://pubmed.ncbi.nlm.nih.gov/37251668/) | Human NDM series/case | Molecular diagnosis dictates SU vs insulin |
| [41614934](https://pubmed.ncbi.nlm.nih.gov/41614934/) | Review | NDM classification; precision medicine |
| [38752501](https://pubmed.ncbi.nlm.nih.gov/38752501/) | Human cohort | NDM incidence ~1:90,000 |
| [37897565](https://pubmed.ncbi.nlm.nih.gov/37897565/) / [42468610](https://pubmed.ncbi.nlm.nih.gov/42468610/) / [41275391](https://pubmed.ncbi.nlm.nih.gov/41275391/) | Consanguineous cohorts | Recessive burden, consanguinity |
| [27133796](https://pubmed.ncbi.nlm.nih.gov/27133796/) | hPSC editing | Conserved human GLIS3 requirement |
| [28523428](https://pubmed.ncbi.nlm.nih.gov/28523428/) | Review | GLIS3 structure/function; disease associations |

Evidence source types span **human clinical** (gene discovery, case series, cohorts, explant pathology), **model organism** (mouse conditional/global KO, medaka), and **in vitro** (INS-1E, primary/human islets, iPSC), giving convergent, cross-validated support for the developmental-transcription-factor model.

---

## Limitations and Knowledge Gaps

1. **Small n / publication bias.** Only ~20 families are reported; frequency estimates for individual organ features (glaucoma, deafness, EPI) are imprecise and likely biased toward severe, published cases.
2. **No formal natural-history or survival data.** Life expectancy, mortality rates, and validated QoL instruments have not been systematically measured for GLIS3-NDH.
3. **Genotype–phenotype correlation is incomplete.** Why some patients lack congenital hypothyroidism or have milder hepatic/renal disease (variable expressivity) is not mechanistically resolved; no proven modifier genes.
4. **Under-modeled phenotypes.** The ocular (high hyperopia) and biliary-cirrhosis components are not fully recapitulated in existing animal models.
5. **No disease-specific therapeutics.** No gene/cell/RNA therapy exists; stem-cell beta-cell replacement remains conceptual.
6. **Ontology mapping** provided here (HPO/GO/CL/UBERON/NCIT) is expert-suggested and should be curator-verified.

---

## Proposed Follow-up Experiments / Actions

1. **Curate an international GLIS3-NDH registry** to define organ-feature frequencies, natural history, survival, and genotype–phenotype correlations with adequate power.
2. **Systematic ACMG re-classification** of all reported GLIS3 variants using the INS-promoter functional assay (PS3) framework ([PMID: 38051360](https://pubmed.ncbi.nlm.nih.gov/38051360/)), including CNV/deletion detection to avoid missed large deletions.
3. **Human iPSC-derived multi-lineage models** (beta cell, thyroid follicular, cholangiocyte, kidney organoid) from patient GLIS3 genotypes to model the ocular/biliary phenotypes currently missing in mice ([PMID: 27133796](https://pubmed.ncbi.nlm.nih.gov/27133796/)).
4. **Test whether SRp55/Bim-axis modulation** protects GLIS3-deficient human beta cells from apoptosis as a proof-of-concept therapeutic target ([PMID: 23737756](https://pubmed.ncbi.nlm.nih.gov/23737756/)).
5. **Explore stem-cell-derived beta-cell replacement** as a rational strategy given the developmental (cell-absent) nature of the defect.
6. **Formalize a diagnostic algorithm** ensuring GLIS3 is on all neonatal-diabetes NGS panels and that neonatal diabetes + congenital hypothyroidism triggers GLIS3 deletion analysis, avoiding futile sulfonylurea trials.

---

*Report compiled from 14 confirmed findings and 32 reviewed publications across a 5-iteration autonomous investigation. Evidence types: human clinical, model organism, in vitro, computational.*


## Artifacts

- [OpenScientist final report](Neonatal_Diabetes_Mellitus_With_Congenital_Hypothyroidism-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neonatal_Diabetes_Mellitus_With_Congenital_Hypothyroidism-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 25 |
| Quoted claims found in source | 25 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 25 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 22 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000851` (1 mention) - the report calls it "Highly frequent (one compound-het patient lacked it)"; HP calls it **Congenital hypothyroidism**
- `HP:0008007` (1 mention) - the report calls it "Frequent"; HP calls it **Primary congenital glaucoma**
- `CL:1000454` (2 mentions) - the report calls it "kidney collecting-duct epithelial cell", "Renal tubular epithelium** — shortened cilia, cyst formation"; CL calls it **kidney collecting duct epithelial cell**
- `GO:0005634` (1 mention) - the report calls it "GLIS3 transactivation"; GO calls it **nucleus**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0012436` (2 mentions) - the report calls it "MONDO"; MONDO calls it **neonatal diabetes mellitus with congenital hypothyroidism**, and lists "NDH" among its other names
- `CL:0000169` (2 mentions) - the report calls it "type B pancreatic/beta cell", "beta cells", "Pancreatic **beta cells"; CL calls it **type B pancreatic cell**
- `CL:0000068` (1 mention) - the report calls it "duct epithelial cell / cholangiocyte"; CL calls it **duct epithelial cell**
- `GO:0005929` (1 mention) - the report calls it "primary cilium"; GO calls it **cilium**, and lists "primary cilium" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000169` - called "type B pancreatic/beta cell", "beta cells", "Pancreatic **beta cells"
- `CL:0002258` - called "thyroid follicular cell", "Thyroid follicular cells"
- `CL:1000454` - called "kidney collecting-duct epithelial cell", "Renal tubular epithelium** — shortened cilia, cyst formation"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.