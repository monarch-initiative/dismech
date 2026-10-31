---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-16T20:15:11.545947'
end_time: '2026-10-16T20:53:54.343755'
duration_seconds: 2322.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Congenital Myopathy 11
  mondo_id: MONDO:0859264
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
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 14
  on_topic: 11
  validator_version: 0.3.0
term_validation:
  total_terms: 27
  verified: 25
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 3
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0001319
    reported_labels:
    - Clinical sign
    ontology_label: Neonatal hypotonia
  - term_id: HP:0003324
    reported_labels:
    - Clinical sign
    ontology_label: Generalized muscle weakness
  - term_id: HP:0001270
    reported_labels:
    - Clinical sign
    ontology_label: Motor delay
  - term_id: HP:0003749
    reported_labels:
    - Laboratory/path
    ontology_label: Pelvic girdle muscle weakness
  - term_id: HP:0009020
    reported_labels:
    - Imaging
    ontology_label: Exercise-induced muscle fatigue
  - term_id: HP:0003236
    reported_labels:
    - Lab
    ontology_label: Elevated circulating creatine kinase activity
  - term_id: UBERON:0002385
    reported_labels:
    - muscle of pelvic girdle
    ontology_label: muscle tissue
  labels_variant: 3
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
  path: Congenital_Myopathy_11-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Myopathy_11-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Myopathy 11
- **MONDO ID:** MONDO:0859264 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Myopathy 11** covering all of the
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

# Congenital Myopathy 11 (CMYP11 / HACD1-related congenital myopathy) — Disease Characterization Report

**Prepared:** 2026-10-16 | **Target:** Congenital Myopathy 11 | **MONDO:0859264**
**Evidence base:** This is an **ultra-rare Mendelian disease**. Information is derived from **disease-level/aggregated resources** (OMIM, gnomAD, UniProt) and a small number of **individual-patient case reports/series** (fewer than ~15 reported human families worldwide), supplemented by an extensively characterized **naturally occurring canine model** and **mouse/cell models**. There are **no registries, EHR cohorts, GWAS, or population epidemiology datasets** for this disease.

---

## 1. Disease Information

**Overview.** Congenital Myopathy 11 (CMYP11) is an autosomal recessive congenital myopathy caused by biallelic loss-of-function (LoF) variants in **HACD1** (3-hydroxyacyl-CoA dehydratase 1; legacy symbol **PTPLA**). It presents at birth with generalized muscle weakness and hypotonia, motor developmental delay, and frequently respiratory distress, with a characteristic **improvement over time**. Muscle biopsy typically shows **congenital fiber-type disproportion (CFTD)**; the canine orthologous disease is classified as **centronuclear myopathy (CNM)**. First linked to humans in 2013 (PMID 23933735) and confirmed as a "bona fide" congenital myopathy gene in 2021 (PMID 33354762).

**Key identifiers.**
- **OMIM (phenotype):** #619967 (Myopathy, congenital, 11) · **OMIM (gene HACD1):** 610467
- **MONDO:** MONDO:0859264
- **Gene:** HACD1 — **HGNC:9639**, Ensembl **ENSG00000165996**, UniProt **B0YJ81** (HACD1_HUMAN), **EC 4.2.1.134**
- **Orphanet:** HACD1 congenital myopathy falls within "Congenital myopathy with fiber type disproportion" (ORPHA:2020) group
- **ICD-11:** 8C70.0 (Congenital myopathies) · **ICD-10:** G71.2 · **MeSH:** Myopathies, Structural, Congenital (D020914)
- **Chromosome:** 10p13 (chr10:17,589,032–17,617,374, GRCh38)

**Synonyms / alternative names.** HACD1-related congenital myopathy; PTPLA-related myopathy; congenital myopathy with fiber-type disproportion (HACD1 type); (canine) autosomal recessive centronuclear myopathy / "Labrador myopathy" / type II fiber deficiency.

---

## 2. Etiology

**Primary cause — genetic (monogenic, autosomal recessive).** Biallelic LoF variants in HACD1 are the sole established cause. There is **no environmental, infectious, or multifactorial contribution**; the disease is fully genetically determined.

**Genetic risk factors.**
- **Causal variants (human, all biallelic LoF):** nonsense c.?? (first family, NMD reducing HACD1 mRNA to 31% — PMID 23933735); splice/deletion **c.373_375+2delGAGGT**; splice **c.785-1G>T**; nonsense **c.458G>A** (PMID 33354762); **biallelic LINE insertion** (PMID 32426512). (Canine) tRNA-derived **SINE insertion in exon 2** of PTPLA (PMID 15829503).
- **Susceptibility loci / modifier genes:** none identified in humans. HACD2 (ubiquitous paralog) is a plausible genetic modifier via functional redundancy (inferred, not demonstrated).
- **Family history / consanguinity:** affected individuals are typically from **consanguineous** families (Middle East/Asia; now Brazil); consanguinity is the major demographic risk factor for homozygosity.

**Environmental risk / protective factors.** None known. No toxins, diet, lifestyle, or exposures are implicated as causes, modifiers, or protectors. No protective genetic alleles described.

**Gene–environment interactions.** None established. (Not applicable for this monogenic disorder.)

---

## 3. Phenotypes

Phenotype frequencies are **qualitative** (small N). Core features, with suggested HPO terms:

| Phenotype | Type | HPO term | Onset | Severity/Course | Frequency |
|---|---|---|---|---|---|
| Neonatal hypotonia | Clinical sign | HP:0001319 | Neonatal/congenital | Severe at birth, improves | Very frequent |
| Generalized muscle weakness | Clinical sign | HP:0003324 | Neonatal | Severe→improving | Very frequent |
| Motor developmental delay | Clinical sign | HP:0001270 | Infancy | Moderate, improves | Frequent |
| Respiratory distress / insufficiency | Clinical sign | HP:0002098 / HP:0002093 | Neonatal | Severe, often transient | Frequent |
| Congenital fiber-type disproportion (biopsy) | Laboratory/path | HP:0003749 | Congenital | Static | Characteristic |
| Reduced fetal movements / feeding difficulty | Symptom | HP:0001558 / HP:0011968 | Perinatal | Variable | Reported |
| Muscle fatty infiltration on MRI (pelvic/posterior leg) | Imaging | HP:0009020 | Childhood | Slowly evolving | 3/3 imaged (PMID 42275936) |
| Normal/mildly elevated serum CK | Lab | HP:0003236 | — | Static | Typical of congenital myopathies |

**Progression:** Non-progressive/improving — the hallmark "temporally progressive improvement" (PMID 33354762). **Severity:** severe neonatal presentation, moderate residual weakness later. **Quality of life:** major early impact (respiratory/feeding/motor), substantially improving with age; most survivors become ambulant. Formal EQ-5D/SF-36/PROMIS data are **not available**.

---

## 4. Genetic / Molecular Information

- **Causal gene:** **HACD1** (HGNC:9639; OMIM 610467). Sole gene.
- **Variant classification:** reported alleles are **pathogenic/likely pathogenic** (ACMG), acting as **loss-of-function**.
- **Variant types/classes:** nonsense, canonical splice-site, small deletion with splice disruption, and **transposable-element insertions (LINE in humans; SINE in dogs)** — a notable recurrent mutational mechanism for this gene.
- **Allele frequency (gnomAD):** HACD1 is **not LoF-constrained**: pLI ≈ 0 (1.8×10⁻¹⁷), observed/expected LoF = **1.28** (41 obs / 32 exp), **LOEUF = 1.66**, LoF Z = −1.35, missense Z = −0.35. Individual pathogenic alleles are rare/private; heterozygous carriers are asymptomatic.
- **Origin:** **germline** (constitutional); not somatic. **COSMIC/TCGA:** not applicable (non-oncologic).
- **Functional consequence:** **loss of function** (abolished dehydratase activity; NMD of transcript).
- **Modifier genes:** none proven (HACD2 redundancy inferred).
- **Epigenetics:** no disease-specific methylation/histone data.
- **Chromosomal abnormalities:** none (not a CNV/aneuploidy disorder).

---

## 5. Environmental Information

**Not applicable.** No environmental, lifestyle, or infectious factors cause, trigger, or modify CMYP11. It is a purely genetic, congenital disorder.

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. **Biallelic LoF variant in HACD1** → **leads to** absent/non-functional HACD1 enzyme in striated muscle (NMD; splice/nonsense/insertion) *(demonstrated; PMID 23933735)*.
2. Loss of HACD1 dehydratase activity → **results in** a block at the **third (dehydration) step of the ER very-long-chain fatty-acid (VLCFA) elongation cycle** (ELOVL→KAR→**HACD**→TECR), reducing VLCFA (>C18) synthesis *(demonstrated in vitro/patient muscle; PMID 23933735, 38422897)*.
3. Reduced VLCFA/altered acyl chains → **leads to** remodeled membrane phospholipids: **↑ lysophosphatidylcholine** and **↓ ≥C18/monounsaturated phospholipid fatty acids** → **increased plasma-membrane rigidity** *(demonstrated in dog, Hacd1-KO mouse, deficient myoblasts; PMID 26160855)*.
   - **Branch A (developmental):** membrane rigidity + LPC (a fusion inhibitor) → **impairs myoblast fusion** → **reduced myofiber diameter / fiber-type disproportion** → neonatal weakness/hypotonia *(demonstrated; PMID 26160855)*. PTPLA/HACD1 also supports myoblast proliferation/differentiation via **MyoG** and cell-cycle control *(in vitro; PMID 22106411)*.
   - **Branch B (structural/mature muscle):** membrane-composition defect → **progressive tubuloreticular & sarcolemmal membrane abnormalities, T-tubule dilation/disorganization, mislocalized triads and mitochondria** → **defective excitation–contraction coupling** → weakness; centronuclear histology in dogs *(demonstrated; PMID 27939133)*.
4. Combined developmental hypotrophy + EC-coupling defect → **produces** the clinical phenotype (weakness, respiratory distress). Partial compensation (regeneration, growth, residual HACD2 activity) → **underlies the characteristic postnatal improvement** *(inferred from improving course + redundancy)*.

### Supporting detail
- **Molecular pathways:** fatty-acid elongation (KEGG map00062; Reactome VLCFA synthesis). Myogenic regulatory network (MyoG; SRF upstream of PTPLA, PMID 22106411).
- **Cellular processes:** myoblast fusion (GO:0007520), skeletal muscle fiber development (GO:0048741), excitation–contraction coupling (GO:0006941 muscle contraction), membrane organization.
- **Protein dysfunction:** loss of function of an ER-membrane dehydratase (EC 4.2.1.134); no aggregation/gain-of-function.
- **Metabolic changes:** VLCFA biosynthesis deficiency; lipid/phospholipid remodeling (lipidomics: ↑LPC). **Biochemical defect:** enzyme (dehydratase) deficiency.
- **Immune involvement / inflammation / fibrosis:** not a primary feature.
- **Molecular profiling:** lipidomic shifts documented (PMID 26160855); no human transcriptomic/proteomic/metabolomic disease datasets. CRISPR/RNAi screens: not disease-specific.
- **Cell types (CL):** skeletal muscle myoblast (CL:0000056), skeletal muscle fiber / myotube, type I vs type II fibers. **Subcellular (GO CC):** endoplasmic reticulum membrane (GO:0005789), T-tubule (GO:0030315), sarcoplasmic reticulum, triad.
- **Chemical entities (CHEBI):** very-long-chain fatty acid (CHEBI:27283), 3-hydroxyacyl-CoA, trans-2-enoyl-CoA, lysophosphatidylcholine (CHEBI:17504).

---

## 7. Anatomical Structures Affected

- **Organ/system level:** **Skeletal muscle / musculoskeletal system** (primary). **Respiratory system** (respiratory muscle weakness → neonatal respiratory distress). HACD1 is also highly expressed in **myocardium** (UniProt), but overt cardiomyopathy is **not** a reported human feature (potential monitoring target; the related canine CNM colony is used in CNM cardiac/neuromuscular studies).
- **Tissue/cell level:** striated **muscle tissue** (UBERON:0002036 skeletal muscle tissue); affected cells = **myoblasts/myotubes and mature myofibers**, with relative **type-1 fiber hypotrophy** (human CFTD) or **type II fiber atrophy / centronuclear** change (canine). Cell Ontology: CL:0000056 (myoblast), CL:0000188 (skeletal muscle cell).
- **Subcellular level:** **endoplasmic reticulum membrane** (site of enzyme), **T-tubules/triads**, **sarcolemma**, and **mitochondria** (mislocalized).
- **Localization:** generalized/axial and limb-girdle; MRI shows **symmetrical, bilateral** fatty infiltration predominantly in **pelvic girdle and posterior lower-limb compartments**, sparing anterior thigh/leg (PMID 42275936). **Lateralization:** bilateral/symmetric.
- **UBERON terms:** UBERON:0001134 (skeletal muscle tissue), UBERON:0001388 (gastrocnemius), UBERON:0002385 (muscle of pelvic girdle), UBERON:0000948 (heart, expression).

---

## 8. Temporal Development

- **Onset:** **congenital/neonatal** (often antenatal — reduced fetal movements). Pattern: **subacute at birth**, clinically evident from the neonatal period.
- **Progression:** **non-progressive to improving**. Severe neonatal nadir (weakness + respiratory compromise) → **remarkable functional improvement** through infancy/childhood (PMID 33354762, 42275936). Disease duration: **chronic/lifelong** (residual weakness) but **not degenerative**.
- **Course pattern:** **stable/improving** (contrasts with progressive dystrophies).
- **Critical period / window of opportunity:** the **perinatal–early-infancy** period (respiratory support during the weakest phase is life-saving; developmental myogenesis window is where fusion defect manifests).
- **Remission:** functional improvement is **spontaneous** (natural history), not treatment-induced.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** (AR).
- **Penetrance:** **complete** in biallelic LoF individuals (reported); **expressivity** relatively **consistent** (comparable presentation across families, PMID 33354762).
- **Epidemiology:** **ultra-rare**; prevalence/incidence **not quantified** (<15 reported human families; Orphanet "unknown/<1:1,000,000" range). No GBD/registry data.
- **Carrier frequency:** not formally estimated in humans; gnomAD indicates pathogenic alleles are individually rare and LoF is tolerated in heterozygotes (asymptomatic carriers).
- **Founder effects:** none established in humans; **striking founder effect in dogs** (single recent PTPLA SINE allele disseminated worldwide via popular sires, PMID 23071563).
- **Consanguinity:** major driver of human cases (homozygosity in consanguineous Middle Eastern/Asian families; the c.373_375+2delGAGGT allele recurs, including in Brazil).
- **Germline mosaicism / anticipation:** not reported / not applicable (no repeat expansion).
- **Population demographics:** reported in Middle East, Asia, and Brazil. **Sex ratio:** ~1:1 (AR, no sex bias). **Age distribution:** presents at birth; patients survive into childhood/adulthood.

---

## 10. Diagnostics

- **Muscle biopsy (key):** **congenital fiber-type disproportion** — smaller type-1 fibers without structural lesions (HP:0003749); canine counterpart shows centronuclear/type II features (PMID 20179953, 27939133, 42275936).
- **Serum CK:** normal or mildly elevated (typical of congenital myopathies).
- **EMG/nerve conduction:** nonspecific myopathic changes; used to exclude neuromuscular-junction and neurogenic disorders.
- **Muscle MRI:** symmetrical pelvic-girdle/posterior lower-limb fatty infiltration sparing anterior compartments — an emerging supportive pattern (PMID 42275936).
- **Genetic testing (definitive):** **congenital-myopathy NGS gene panel → WES/WGS** to identify **biallelic HACD1 variants**; because splice/transposon insertions occur, **RNA sequencing** and **WGS** improve detection of non-canonical/structural alleles. Single-gene HACD1 testing applies for known familial variants / cascade testing. CMA, karyotype, FISH, mtDNA, and repeat-expansion testing are **not diagnostic** (used only to exclude mimics).
- **Clinical criteria:** no disease-specific consensus criteria; diagnosis = neonatal congenital myopathy phenotype + CFTD biopsy + biallelic HACD1 LoF.
- **Differential diagnosis:** other CFTD genes — **ACTA1, TPM3, TPM2, SELENON (SEPN1), RYR1** — and **congenital myotonic dystrophy (DMPK CTG expansion)**, which can mimic CFTD (PMID 20951040, 20179953, 24239060); also other congenital myopathies (nemaline, core, centronuclear/MTM1) and congenital muscular dystrophies.
- **Screening:** not part of newborn screening; **cascade carrier testing** in families and **carrier screening** for consanguineous couples are appropriate.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** main risk is **neonatal respiratory failure**; with supportive care, survival is generally good and many patients improve. No formal survival statistics exist (small N). Life expectancy appears **near-normal** in survivors, but long-term data are limited.
- **Morbidity/function:** early severe disability (respiratory/feeding/motor) that **improves**; residual proximal weakness and possible orthopedic sequelae (contractures, scoliosis) typical of congenital myopathies.
- **Disease course:** **chronic but non-progressive/improving**. Complications: respiratory infections during the weak phase; potential orthopedic and (theoretically, given myocardial expression) cardiac surveillance.
- **Prognostic factors:** severity of neonatal respiratory involvement; **molecular diagnosis carries "impactful prognostic value"** (predicts the favorable improving trajectory) (PMID 33354762). No molecular prognostic biomarkers beyond genotype.
- **QoL tools:** none disease-specific reported.

---

## 12. Treatment

**No curative or disease-specific (pharmacologic/gene/RNA) therapy exists.** Management is **supportive and multidisciplinary** (NCIT: Supportive Care Intervention):

- **Pharmacotherapy:** none targeted. No pharmacogenomic guidance.
- **Supportive/rehabilitative (mainstay):**
  - **Respiratory support** — neonatal ventilation, **non-invasive ventilation (NIV)**, airway clearance (NCIT: Respiratory Therapy).
  - **Nutritional/feeding support** — assisted feeding for neonatal feeding difficulty (NCIT: Nutritional Support).
  - **Physical & occupational therapy**, stretching to prevent **contractures**; orthopedic management of **scoliosis** (NCIT: Physical Therapy, Occupational Therapy).
- **Surgical/interventional:** orthopedic (scoliosis/contracture) procedures as needed.
- **Anesthesia:** caution advised in congenital myopathies; in the canine HACD1/CNM model, sensitivity to the non-depolarizing blocker **vecuronium was not increased** vs controls (PMID 25815571) — informative but not a substitute for standard neuromuscular-disease anesthetic precautions.
- **Advanced/experimental (future directions):** the recessive LoF mechanism and the **validated Labrador large-animal model** make **gene replacement/editing** conceptually attractive (the same canine platform enabled successful MTM1 gene therapy for X-linked CNM; PMID 31450509). **No clinical trials (ClinicalTrials.gov) are currently open for HACD1 myopathy.**
- **Personalized medicine:** genotype-guided counseling/prognosis; no genotype-directed drugs.

---

## 13. Prevention

- **Primary prevention:** **genetic counseling** for at-risk/consanguine families; **carrier screening**; **prenatal diagnosis** or **preimplantation genetic testing (PGT-M)** for couples with a known biallelic genotype (NCIT: Genetic Counseling).
- **Secondary prevention:** early recognition of neonatal hypotonia/respiratory compromise → prompt respiratory support; early molecular diagnosis to guide monitoring.
- **Tertiary prevention:** prevent complications — respiratory surveillance/vaccination against respiratory pathogens, orthopedic surveillance (scoliosis/contractures), aspiration precautions.
- **Immunization/public health/environmental:** no disease-specific vaccine or environmental intervention (not applicable).
- **Risk stratification:** family history/consanguinity + known familial variant enables **cascade testing**.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** **Canis lupus familiaris** (NCBI Taxon **9615**) — dog; **Mus musculus** (NCBI Taxon **10090**) — engineered model.
- **Breed:** **Labrador Retriever** (naturally affected; VBO term for Labrador Retriever). Historically "Labrador myopathy" / type II fiber deficiency.
- **Orthologous gene:** canine/murine **Hacd1/PTPLA** (NCBI Gene orthologs).
- **Natural disease (veterinary):** autosomal recessive **centronuclear myopathy (CNM)** in Labradors — generalized weakness, exercise intolerance, type II fiber atrophy, centronuclear histology; onset in puppyhood. Driven by a **recent founder SINE insertion** in PTPLA exon 2, disseminated worldwide; carrier allele frequency ~1.8% in an Italian sample (~1/20,000 affected) (PMID 15829503, 23071563, 21217042). **Veterinary importance:** significant inherited neuromuscular disease of a popular breed; **DNA carrier testing is used in breeding programs** to avoid carrier×carrier matings.
- **Comparative pathology:** dogs show CNM features (and progressive membrane/triad defects), humans show CFTD; both reflect the same VLCFA/membrane mechanism — strong **evolutionary conservation** of HACD1 function in striated muscle.
- **Transmission:** none — **not zoonotic/infectious**; purely inherited.

---

## 15. Model Organisms

- **Canine (natural, large-animal):** PTPLA/HACD1-deficient **Labrador Retriever** colony — the premier model; recapitulates weakness, exercise intolerance, fiber pathology, and progressive membrane/triad/EC-coupling defects (PMID 27939133); supports functional outcome measures (**6-minute walk test**, PMID 27012153) and anesthetic/physiologic studies; a proven platform for CNM therapy translation (PMID 31450509).
- **Mouse:** **Hacd1-knockout** mice — reduced myofiber size, impaired myoblast fusion, altered membrane lipid composition/fluidity (PMID 26160855). Available via standard repositories (MGI/IMSR).
- **Cellular/in vitro:** HACD1-deficient primary myoblasts and PTPLA-knockdown myoblast lines — fusion failure, differentiation/cell-cycle defects (MyoG axis) (PMID 26160855, 22106411). iPSC-derived myotubes are feasible but not yet reported for HACD1.
- **Phenotype recapitulation:** high — animal/cell models reproduce the core developmental (fusion/fiber-size) and structural (membrane/triad) defects and the lipid biochemistry.
- **Limitations:** canine disease is labeled CNM (vs human CFTD); the characteristic human postnatal improvement is less emphasized in models; no reported invertebrate (fly/worm/zebrafish) disease model.
- **Resources:** MGI (mouse Hacd1), IMSR; canine colony literature; Alliance of Genome Resources for orthology.

---

## Summary (Answer to the Research Question)

Congenital Myopathy 11 is an **ultra-rare autosomal recessive congenital myopathy** caused by **biallelic loss-of-function variants in HACD1 (PTPLA)**, the muscle-enriched ER enzyme catalyzing the dehydration step of **very-long-chain fatty-acid elongation**. Enzyme loss remodels muscle-membrane phospholipids (↑lysophosphatidylcholine, ↑rigidity), **impairing myoblast fusion and triad/excitation–contraction architecture**, which produces **neonatal hypotonia, generalized weakness, and respiratory distress with congenital fiber-type disproportion on biopsy** — followed by a **characteristic clinical improvement**. Diagnosis is **molecular (biallelic HACD1 LoF) plus CFTD biopsy**; management is **supportive/multidisciplinary** (no curative therapy); and a **naturally occurring Labrador Retriever model** provides a validated platform for mechanism and future gene therapy.

## Supported vs Refuted Hypotheses
- **Supported:** HACD1 LoF is the cause (H1); mechanism = VLCFA-elongation→membrane-lipid→fusion/triad defect (H2); AR inheritance with tolerant heterozygotes (H3, gnomAD); favorable improving prognosis (H4); robust canine model (H5).
- **Refuted/Excluded:** no environmental/infectious etiology; not a channelopathy, aggregation, or gain-of-function disorder; no somatic/oncologic component; HACD1 is **not** a functional tyrosine phosphatase despite the PTPLA name.

## Limitations & Future Directions
- Very small human N → frequencies qualitative; no epidemiology, QoL, survival statistics, or human omics datasets.
- Possible cardiac involvement (myocardial HACD1 expression) is **untested** in humans and warrants surveillance studies.
- Natural history and genotype–phenotype correlation need prospective cohorts; **gene-replacement/editing** is a logical therapeutic avenue leveraging the canine model.

### Key References (PMID)
23933735 (first human cause); 33354762 (bona fide confirmation, variant spectrum, prognosis); 42275936 (MRI, Brazilian cohort); 26160855 (membrane/fusion mechanism); 27939133 (triad/membrane defects, canine); 22106411 (MyoG/cell-cycle); 38422897 (VLCFA elongation machinery); 15829503, 23071563, 21217042, 27012153, 25815571, 31450509 (canine model); 20951040, 20179953, 24239060 (CFTD differential); 32426512 (LINE insertion).


## Artifacts

- [OpenScientist final report](Congenital_Myopathy_11-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Myopathy_11-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 14 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 13 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001319` (1 mention) - the report calls it "Clinical sign"; HP calls it **Neonatal hypotonia**
- `HP:0003324` (1 mention) - the report calls it "Clinical sign"; HP calls it **Generalized muscle weakness**
- `HP:0001270` (1 mention) - the report calls it "Clinical sign"; HP calls it **Motor delay**
- `HP:0003749` (2 mentions) - the report calls it "Laboratory/path"; HP calls it **Pelvic girdle muscle weakness**
- `HP:0009020` (1 mention) - the report calls it "Imaging"; HP calls it **Exercise-induced muscle fatigue**
- `HP:0003236` (1 mention) - the report calls it "Lab"; HP calls it **Elevated circulating creatine kinase activity**
- `UBERON:0002385` (1 mention) - the report calls it "muscle of pelvic girdle"; UBERON calls it **muscle tissue**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007520` (1 mention) - the report calls it "Cellular processes:** myoblast fusion"; GO calls it **myoblast fusion**
- `CL:0000188` (1 mention) - the report calls it "skeletal muscle cell"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `UBERON:0000948` (1 mention) - the report calls it "heart, expression"; UBERON calls it **heart**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.