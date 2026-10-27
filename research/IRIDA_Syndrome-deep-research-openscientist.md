---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-29T11:31:08.071627'
end_time: '2026-08-29T11:44:55.007964'
duration_seconds: 826.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: IRIDA Syndrome
  mondo_id: MONDO:0008788
  category: Genetic
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
citation_count: 16
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 32
  quotes_valid: 31
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:25156943
  relevance_assessed: 16
  on_topic: 12
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 22
  verified: 20
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 11
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0008788
    reported_labels:
    - MONDO
    ontology_label: IRIDA syndrome
  - term_id: HP:0004840
    reported_labels:
    - Lab / clinical
    ontology_label: Hypochromic microcytic anemia
  - term_id: HP:0001935
    reported_labels:
    - Lab
    ontology_label: Microcytic anemia
  - term_id: HP:0025066
    reported_labels:
    - Lab
    ontology_label: Decreased mean corpuscular volume
  - term_id: HP:0040303
    reported_labels:
    - Lab
    ontology_label: Decreased circulating iron concentration
  - term_id: HP:0012378
    reported_labels:
    - Symptom
    ontology_label: Fatigue
  - term_id: HP:0000980
    reported_labels:
    - Clinical sign
    ontology_label: Pallor
  labels_variant: 1
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
  path: IRIDA_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: IRIDA_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IRIDA Syndrome
- **MONDO ID:** MONDO:0008788 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **IRIDA Syndrome** covering all of the
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

# IRIDA Syndrome (Iron-Refractory Iron Deficiency Anemia): Comprehensive Disease Characteristics Report

**Disease:** IRIDA Syndrome | **MONDO:** MONDO:0008788 | **OMIM:** 206200 | **Orphanet:** ORPHA:209981 | **Category:** Genetic (Autosomal Recessive)

---

## Summary

Iron-Refractory Iron Deficiency Anemia (IRIDA) is a rare Mendelian disorder of systemic iron homeostasis caused by biallelic (homozygous or compound heterozygous) loss-of-function mutations in **TMPRSS6**, the gene encoding the hepatic type II transmembrane serine protease **matriptase-2 (MT2)**. Under normal physiology, matriptase-2 acts as a negative regulator of the iron-regulatory hormone hepcidin: it dampens BMP/SMAD signaling in hepatocytes, in part by cleaving the co-receptor hemojuvelin (HJV). When matriptase-2 function is lost, hepcidin production becomes inappropriately high relative to the body's iron-depleted state. Elevated hepcidin degrades the iron exporter ferroportin (SLC40A1) on duodenal enterocytes and reticuloendothelial macrophages, simultaneously blocking dietary iron absorption and the recycling of iron from senescent red cells. The result is a lifelong, iron-restricted erythropoiesis producing hypochromic microcytic anemia with a distinctive biochemical signature.

The clinical hallmark that unifies diagnosis and mechanism is the paradoxical combination of profound iron deficiency (very low transferrin saturation, typically <5–10%) with **inappropriately normal-to-high serum hepcidin** — the opposite of acquired iron deficiency, in which hepcidin is low or undetectable. This single feature explains the disease name: because hepcidin remains high, oral iron is poorly absorbed and the anemia is "refractory" to oral supplementation, responding only slowly and partially to intravenous iron. The disorder is generally benign with normal life expectancy; anemia is moderate (Hb ~6–9 g/dL) and often attenuates with age, though microcytosis and low transferrin saturation persist throughout life.

This report synthesizes 14 confirmed findings across 21 reviewed primary papers into a complete disease-knowledge entry spanning etiology, phenotype, molecular mechanism, protein architecture, epidemiology, diagnostics, prognosis, treatment, prevention, comparative biology, and model organisms. A recurring theme with translational significance is that TMPRSS6 sits at a therapeutic fulcrum: because loss of matriptase-2 *raises* hepcidin, pharmacologic inhibition of TMPRSS6 (antisense oligonucleotides, siRNA, and anti-matriptase-2 monoclonal antibodies such as RLYB331 and DISC-3405) is being actively developed to *raise* hepcidin in the opposite clinical setting of iron-overload disorders like β-thalassemia and hemochromatosis.

---

## 1. Disease Information

**Overview.** IRIDA is a hereditary, autosomal-recessive form of iron deficiency anemia that is intrinsically resistant to oral iron therapy. It is a disease of dysregulated iron *distribution* rather than absolute dietary iron insufficiency: iron is present but cannot be mobilized because hepcidin is inappropriately elevated. As summarized by De Falco et al., "Iron refractory iron deficiency anemia is a hereditary recessive anemia due to a defect in the TMPRSS6 gene encoding Matriptase-2" ([PMID: 23729726](https://pubmed.ncbi.nlm.nih.gov/23729726/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0008788 |
| OMIM | 206200 (IRIDA) |
| Orphanet | ORPHA:209981 |
| Gene (HGNC) | TMPRSS6, HGNC:16517 |
| UniProt | Q8IU80 (matriptase-2) |
| Chromosomal locus | 22q12.3 |

**Synonyms / alternative names.** Iron-refractory iron deficiency anemia; IRIDA; iron-refractory IDA; TMPRSS6-related iron deficiency anemia; matriptase-2 deficiency; familial iron deficiency anemia refractory to oral iron.

**Nature of information.** The knowledge base is derived predominantly from **aggregated disease-level resources** (OMIM, Orphanet) and **individual patient/family case reports and small cohort studies** in the primary literature, supplemented by functional in-vitro studies and mouse models. There is no large EHR-derived dataset; the disease's rarity means most evidence comes from published kindreds.

---

## 2. Etiology

**Primary cause (genetic).** IRIDA is a monogenic disorder caused by **germline biallelic loss-of-function mutations in TMPRSS6**. Finberg et al. first established this in 2008, demonstrating that "iron deficiency anemia refractory to oral iron therapy can be caused by germline mutations in TMPRSS6, which encodes a type II transmembrane serine protease produced by the liver that regulates the expression of the systemic iron regulatory hormone hepcidin" ([PMID: 18408718](https://pubmed.ncbi.nlm.nih.gov/18408718/)). There is no environmental or infectious cause; the disorder is entirely determined by genotype.

**Genetic risk factors.**
- **Causal variants:** biallelic pathogenic TMPRSS6 variants (>40 distinct mutations reported, spanning all functional domains of the ectodomain — missense, nonsense, frameshift, and splice-site) ([PMID: 23729726](https://pubmed.ncbi.nlm.nih.gov/23729726/)).
- **Modifier / susceptibility loci:** common TMPRSS6 polymorphisms — most notably **rs855791 (p.V736A / A736V)** — modulate iron status and erythrocyte indices in the general population and can act as modifiers of anemia severity in IRIDA families (see Section 4).
- **Consanguinity** substantially increases the risk of homozygous disease; recurrent alleles (e.g., p.V736A in Saudi families, p.W590R in Southern Italy) reflect founder/population effects ([PMID: 36261087](https://pubmed.ncbi.nlm.nih.gov/36261087/); [PMID: 25156943](https://pubmed.ncbi.nlm.nih.gov/25156943/)).

**Environmental risk factors.** None are causal. However, physiologic states of high iron demand (infancy/rapid growth, menstruation, pregnancy) unmask or worsen the phenotype, making females and young children more symptomatic.

**Protective factors.** No genetic or environmental protective factors are established for IRIDA itself. In the general (non-IRIDA) population, TMPRSS6 iron-lowering alleles are associated with lower iron status; conversely, higher-hepcidin genotypes track with lower iron availability. No dietary or lifestyle factor prevents the monogenic disease.

**Gene–environment interactions.** The principal interaction is between the fixed genetic lesion and physiological iron demand: the same genotype produces more overt anemia during growth spurts, menstruation, and pregnancy. Common modifier alleles (rs855791) interact with the rare causal alleles to shift severity.

---

## 3. Phenotypes

The core phenotype is a **congenital/early-childhood hypochromic microcytic anemia** with a characteristic iron-study profile. Onset is typically in the post-natal period, "although in some cases it is only diagnosed in adulthood" ([PMID: 23729726](https://pubmed.ncbi.nlm.nih.gov/23729726/)).

| Phenotype | Type | HPO term | Characteristics | Frequency |
|---|---|---|---|---|
| Hypochromic microcytic anemia | Lab / clinical | HP:0004840 | Congenital/early childhood onset; moderate (Hb ~6–9 g/dL); lifelong, often attenuates with age | Near-universal (defining) |
| Microcytic anemia | Lab | HP:0001935 | Low MCV | Near-universal |
| Decreased MCV | Lab | HP:0025066 | Reduced red cell size; persists lifelong | Near-universal |
| Decreased serum iron | Lab | HP:0040303 | Hypoferremia | Very frequent |
| Very low transferrin saturation | Lab | (iron studies) | TSAT often <5–10% | Very frequent (hallmark) |
| Inappropriately normal/high hepcidin | Lab | — | Discriminating biochemical feature | Characteristic |
| Normal or elevated ferritin | Lab | — | Iron trapped in macrophages; occasionally frank hyperferritinemia | Frequent |
| Fatigue / reduced exercise tolerance | Symptom | HP:0012378 | Chronic iron-deficiency symptom | Common |
| Pallor | Clinical sign | HP:0000980 | Reflects anemia | Common |
| Growth/developmental impact | Clinical | — | During critical growth windows in childhood | Variable |

**Severity and progression.** Anemia is generally moderate, chronic, and stable-to-improving. Genotype modulates severity: "patients carrying two nonsense mutations present a more severe anemia and microcytosis and higher hepcidin levels than the other patients" ([PMID: 25156943](https://pubmed.ncbi.nlm.nih.gov/25156943/)).

**Atypical presentations.** The phenotypic spectrum is broader than classic microcytosis. Siblings have presented with "severe microcytic anemia, hypoferremia, and hyperferritinemia" ([PMID: 23319530](https://pubmed.ncbi.nlm.nih.gov/23319530/)), and normocytic presentations have been described: "normocytic anemia accompanied by low Hb, normal MCV, low serum iron, low serum ferritin, and normal TIBC" ([PMID: 36261087](https://pubmed.ncbi.nlm.nih.gov/36261087/)).

**Quality-of-life impact.** Chronic fatigue and reduced exercise tolerance are the main daily-functioning burdens. In infancy and childhood, iron deficiency during critical developmental windows is the principal concern; one report emphasized that "the proband was symptomatic for IRIDA during a critical phase of growth and development" ([PMID: 28447549](https://pubmed.ncbi.nlm.nih.gov/28447549/)).

---

## 4. Genetic / Molecular Information

**Causal gene.** **TMPRSS6** (transmembrane protease, serine 6), chromosome **22q12.3**, HGNC:16517, encoding **matriptase-2 (MT2)**, UniProt **Q8IU80**. OMIM disease entry 206200.

**Protein architecture.** Matriptase-2 is an **811-amino-acid type II transmembrane serine protease** with a modular ectodomain:
- N-terminal cytoplasmic tail
- single transmembrane domain
- SEA domain
- two CUB domains
- three LDL-receptor class A (LDLRA) repeats
- C-terminal trypsin-like serine protease (catalytic) domain with the His-Asp-Ser catalytic triad

It is synthesized as a zymogen requiring **autocatalytic activation** and undergoes autocleavage/shedding. "TMPRSS6...encodes a type II transmembrane serine protease produced by the liver" ([PMID: 18408718](https://pubmed.ncbi.nlm.nih.gov/18408718/)).

**Pathogenic variants.** More than 40 distinct mutations span all functional domains. Representative variants:

| Variant | Type | Notes |
|---|---|---|
| p.W590R | Missense | Most frequent mutation in Southern Italy ([PMID: 25156943](https://pubmed.ncbi.nlm.nih.gov/25156943/)) |
| p.V736A (rs855791) | Missense | Recurrent in Saudi families; also a common population modifier ([PMID: 36261087](https://pubmed.ncbi.nlm.nih.gov/36261087/)) |
| p.G442R, p.E522K/E523K | Missense | Compound-heterozygous atypical hyperferritinemia case |
| p.T287N | Missense | Functional exception — retains activity in assays |
| p.I286F (murine analog) | Missense | Activated but functionally compromised in mouse studies |
| Nonsense / frameshift / splice-site | LoF | Associated with more severe phenotype when biallelic |

**Variant classification (ACMG/AMP).** Established recurrent LoF variants are classified pathogenic/likely pathogenic; monoallelic and novel missense variants may be VUS pending functional data.

**Allele frequency.** Rare causal alleles are private or population-recurrent. In contrast, the common modifier **rs855791** is frequent worldwide and was linked by GWAS to "serum iron (rs855791, combined P = 1.5 x 10(-20)), transferrin saturation (combined P = 2.2 x 10(-23)) and erythrocyte mean cell volume (MCV, combined P = 1.1 x 10(-10))" ([PMID: 19820699](https://pubmed.ncbi.nlm.nih.gov/19820699/)).

**Somatic vs germline.** All disease-causing variants are **germline**.

**Functional consequences.** Mutations are overwhelmingly **loss-of-function**. Functional assays show that "all but the p.T287N variant impair matriptase-2 autoproteolytic activation, decrease the ability to cleave membrane HJV and inhibit the HJV-dependent hepcidin activation" ([PMID: 25156943](https://pubmed.ncbi.nlm.nih.gov/25156943/)). Domain-mapping in mice shows "the stem region of MT2 determines the specificity and efficacy for substrate cleavage" ([PMID: 30559294](https://pubmed.ncbi.nlm.nih.gov/30559294/)), and that "the catalytic domain, but not its proteolytic activity, was required for Mt2 to suppress hepcidin expression" ([PMID: 32384154](https://pubmed.ncbi.nlm.nih.gov/32384154/)).

**Modifier genes.** Common TMPRSS6 variants (rs855791 and others) and possibly TF (transferrin) variants modulate iron indices. In IRIDA families, common modifier alleles fine-tune severity alongside the rare causal alleles.

**Epigenetic / chromosomal abnormalities.** No epigenetic mechanism or large-scale chromosomal abnormality is implicated; IRIDA is a point-mutation/small-variant disorder.

---

## 5. Environmental Information

- **Environmental factors:** None causal. No toxin, radiation, or occupational exposure is implicated.
- **Lifestyle factors:** Dietary iron intake does not cause the disease and cannot cure it (oral iron is poorly absorbed). High-iron-demand states (growth, menstruation, pregnancy) modulate symptom expression.
- **Infectious agents:** Not applicable. IRIDA is non-infectious. (Note: inflammation/infection independently raises hepcidin and can confound differential diagnosis — see Section 10.)

---

## 6. Mechanism / Pathophysiology

### Causal chain

```
Biallelic LoF mutation in TMPRSS6
        │
        ▼
Loss / dysfunction of matriptase-2 (MT2) in hepatocytes
        │  (fails to autoactivate; cannot cleave membrane hemojuvelin;
        │   cannot suppress HJV/NEO1-dependent BMP/SMAD signaling)
        ▼
Un-dampened BMP/SMAD signaling  →  INAPPROPRIATELY HIGH HEPCIDIN
        │
        ▼
Hepcidin binds & degrades ferroportin (SLC40A1)
        │
        ├─► Duodenal enterocytes: blocked dietary iron ABSORPTION
        └─► Splenic/hepatic macrophages: blocked iron RECYCLING
        │
        ▼
Low serum iron, very low transferrin saturation
        │
        ▼
Iron-restricted erythropoiesis in bone marrow
        │
        ▼
Hypochromic microcytic anemia (refractory to oral iron)
```

**Molecular pathway (upstream).** Matriptase-2 is a negative regulator of the **BMP/SMAD** hepcidin-induction pathway. "Transmembrane serine protease 6 (TMPRSS6) suppresses hepcidin via the bone morphogenetic protein/small mothers against decapentaplegic (BMP/SMAD) pathway by cleaving the co-receptor hemojuvelin" ([PMID: 42053460](https://pubmed.ncbi.nlm.nih.gov/42053460/)). "In vitro experiments on transfected cells suggest that Matriptase-2 cleaves Hemojuvelin, a major regulator of hepcidin expression and that this function is altered in this genetic form of anemia" ([PMID: 23729726](https://pubmed.ncbi.nlm.nih.gov/23729726/)). MT2 also interacts with additional pathway components including Alk3, ActRIIA, HFE, and **neogenin (NEO1)**; in-vivo mouse work indicates "Mt2 suppression of hepcidin relies on the presence of Neo1" and that MT2 acts "by inhibiting the Neo1/Hjv-induced Bmp-signaling pathway" ([PMID: 41534828](https://pubmed.ncbi.nlm.nih.gov/41534828/)).

**Effector axis (downstream).** Hepcidin is "a circulating hormone produced by the liver that inhibits dietary iron absorption and macrophage iron release" ([PMID: 21355094](https://pubmed.ncbi.nlm.nih.gov/21355094/)). Its excess degrades ferroportin, the sole cellular iron exporter, at the two key gateways: the enterocyte (absorption) and the macrophage (recycling).

**Cellular processes / cell types.** Iron-restricted erythropoiesis (bone marrow erythroblasts), impaired transepithelial iron transport (duodenal enterocytes), impaired iron recycling (reticuloendothelial macrophages).

**Suggested GO / CL terms.** GO:0006879 (intracellular iron ion homeostasis), GO:0060586 (multicellular organismal iron ion homeostasis), GO:0030509 (BMP signaling pathway), GO:0006508 (proteolysis). Cell types: CL:0000182 (hepatocyte), CL:0000584 (enterocyte), CL:0000235 (macrophage), CL:0000765 (erythroblast).

**Metabolic / biochemical abnormality.** The core defect is a **protease loss-of-function** producing hormonal (hepcidin) dysregulation of systemic iron trafficking — not an enzyme-deficiency metabolic block in a biosynthetic pathway.

**Immune involvement.** None primary. IRIDA is not autoimmune or immunodeficient; however, hepcidin is the shared node with anemia of inflammation, which is IL-6/inflammation-driven.

**Molecular profiling.** In-vitro functional studies (transfected cell cleavage assays) and mouse transcriptional readouts of hepatic hepcidin (Hamp) are the principal profiling data. No large human transcriptomic/proteomic/metabolomic dataset is established for IRIDA specifically.

---

## 7. Anatomical Structures Affected

**Site of the primary defect.** The **liver (hepatocytes)** — matriptase-2 is "produced by the liver" ([PMID: 18408718](https://pubmed.ncbi.nlm.nih.gov/18408718/)). UBERON:0002107 (liver); CL:0000182 (hepatocyte).

**Effector sites (secondary).**
- **Duodenum / small intestine** — enterocyte iron absorption blocked. UBERON:0002114 (duodenum); CL:0000584 (enterocyte).
- **Spleen / reticuloendothelial system** — macrophage iron recycling blocked. UBERON:0002106 (spleen); CL:0000235 (macrophage).
- **Bone marrow** — iron-restricted erythropoiesis. UBERON:0002371 (bone marrow); CL:0000765 (erythroblast).

**Body systems.** Hematopoietic/hematologic (primary clinical manifestation) and hepatobiliary/digestive (site of defect and iron absorption).

**Subcellular level.** Matriptase-2 is a plasma-membrane-anchored protein (GO:0005886, plasma membrane); its cytoplasmic tail faces the cytosol and the catalytic ectodomain the extracellular space. Ferroportin resides at the basolateral/plasma membrane of effector cells.

**Localization / lateralization.** The disease is systemic and bilateral/non-lateralized; there is no anatomical asymmetry.

---

## 8. Temporal Development

- **Onset:** Congenital/early post-natal, though sometimes first recognized in adulthood — "The anemia appears in the post-natal period, although in some cases it is only diagnosed in adulthood" ([PMID: 23729726](https://pubmed.ncbi.nlm.nih.gov/23729726/)). Onset pattern is chronic/insidious.
- **Progression:** Slow, chronic, and generally **stable-to-improving**. Hemoglobin frequently improves with age even as microcytosis and low transferrin saturation persist. Not staged like a neoplastic disease.
- **Disease course:** Lifelong (chronic) but non-progressive in a degenerative sense; severity is set largely by genotype (biallelic nonsense = more severe).
- **Critical periods:** Infancy/childhood growth phases and other high-iron-demand windows (menstruation, pregnancy) are periods of greatest vulnerability and the key windows for intervention ([PMID: 28447549](https://pubmed.ncbi.nlm.nih.gov/28447549/)).
- **Remission:** No true remission; partial correction is achievable with parenteral iron, and spontaneous improvement of hemoglobin with age is common.

---

## 9. Inheritance and Population

**Inheritance.** Autosomal recessive; affected individuals are homozygous or compound heterozygous for TMPRSS6 pathogenic variants ([PMID: 23729726](https://pubmed.ncbi.nlm.nih.gov/23729726/)). Sibling recurrence risk is 25%.

**Epidemiology.** Rare; fewer than a few hundred families reported worldwide. Exact prevalence is undetermined and likely underestimated due to under-recognition among common microcytic anemias. Orphanet ORPHA:209981.

**Penetrance / expressivity.** Biallelic pathogenic genotypes are essentially fully penetrant for the biochemical phenotype (microcytosis, low TSAT), with **variable expressivity** of anemia severity governed by genotype and modifier alleles. Monoallelic (single heterozygous) variants may contribute to milder/atypical iron deficiency with incomplete penetrance still under study.

**Founder effects / population recurrence.** Population-recurrent alleles include **p.W590R** ("the most frequent mutation in Southern Italy," [PMID: 25156943](https://pubmed.ncbi.nlm.nih.gov/25156943/)) and **p.V736A**, which "was found in all examined Saudi families with IRIDA" ([PMID: 36261087](https://pubmed.ncbi.nlm.nih.gov/36261087/)). Consanguinity raises homozygous-case frequency.

**Demographics.** Reported across European, Middle Eastern, Asian, and North African populations. Both sexes affected; no strong sex predilection, though females tend to be more symptomatic due to higher iron demands. No genetic anticipation (not a repeat-expansion disorder).

---

## 10. Diagnostics

**Laboratory workup.**
1. **CBC with indices:** low Hb, low MCV, low MCH (hypochromic microcytic pattern).
2. **Iron studies:** low serum iron, **very low transferrin saturation (often <5–10%)**, normal-to-high ferritin.
3. **Serum hepcidin:** inappropriately normal/high — the discriminating biomarker.
4. **Molecular confirmation:** TMPRSS6 sequencing.

**Key discriminating biomarker.** "In contrast to the low/undetectable hepcidin levels observed in acquired iron deficiency, in patients with Matriptase-2 deficiency, serum hepcidin is inappropriately high for the low iron status and accounts for the absent/delayed response to oral iron treatment" ([PMID: 23729726](https://pubmed.ncbi.nlm.nih.gov/23729726/)). The **transferrin saturation/hepcidin ratio** operationalizes this discrimination: van der Staaij et al. showed the "Transferrin Saturation/Hepcidin Ratio Discriminates" pathogenic TMPRSS6-related iron deficiency from other causes ([PMID: 35163840](https://pubmed.ncbi.nlm.nih.gov/35163840/)).

**Genetic testing.** Single-gene TMPRSS6 sequencing, targeted iron/anemia gene panels, or **whole-exome sequencing** for atypical cases. WES has resolved unusual presentations: "whole exome sequencing can be used as a diagnostic tool and greatly facilitate the elucidation of the genetic basis of unusual clinical presentations" ([PMID: 23319530](https://pubmed.ncbi.nlm.nih.gov/23319530/)).

**Differential diagnosis.**

| Condition | Distinguishing feature |
|---|---|
| Nutritional/blood-loss iron deficiency | Hepcidin **low**; responds to oral iron |
| β-/α-thalassemia trait | Normal/high iron; elevated HbA2 (β) or globin imbalance; high-normal RBC count |
| Anemia of chronic disease/inflammation | Hepcidin high but IL-6/CRP elevated; inflammatory context |
| DMT1 (SLC11A2) defect, atransferrinemia, aceruloplasminemia, sideroblastic anemias | Distinct iron-study patterns / systemic features |

"A challenge for the clinicians and pediatricians is the recognition of the disorder among iron deficiency and other microcytic anemias commonly found in pediatric patients" ([PMID: 23729726](https://pubmed.ncbi.nlm.nih.gov/23729726/)).

**Screening.** No population/newborn screening exists. Cascade genetic testing of relatives is appropriate once a proband's variants are known.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** Benign; normal life expectancy. No disease-specific mortality is reported.
- **Disease course:** Lifelong, moderate, chronic anemia that "shows a slow response to intravenous iron injections and partial correction of the anemia" ([PMID: 23729726](https://pubmed.ncbi.nlm.nih.gov/23729726/)); hemoglobin often improves with age.
- **Morbidity:** Chronic fatigue, reduced exercise tolerance, and — in infancy/childhood — potential growth and neurodevelopmental impact during critical windows ([PMID: 28447549](https://pubmed.ncbi.nlm.nih.gov/28447549/)).
- **Prognostic factors:** Genotype is prognostic — biallelic nonsense mutations predict more severe, less-responsive anemia with higher hepcidin ([PMID: 25156943](https://pubmed.ncbi.nlm.nih.gov/25156943/)). Treatment response is itself a prognostic indicator.

---

## 12. Treatment

**First principle:** By definition IRIDA is refractory to oral iron because absorption is hepcidin-blocked.

| Modality | Evidence | NCIT concept |
|---|---|---|
| **Intravenous (parenteral) iron** | Standard of care; slow, partial correction ([PMID: 23729726](https://pubmed.ncbi.nlm.nih.gov/23729726/)) | Iron supplement therapy (parenteral) |
| **Oral iron + vitamin C** | In a pediatric IRIDA-phenotype cohort, "complete response in majority (6/7 = 86%) with >2 g/dL rise in Hb along with significant improvement of other iron related indices" ([PMID: 30594846](https://pubmed.ncbi.nlm.nih.gov/30594846/)) | Ferrous salt + ascorbic acid |
| **Supportive care** | Monitor growth/development in children; manage fatigue | Supportive care |

**Pharmacogenomics.** Response is genotype-dependent (nonsense/nonsense = poorest response). No conventional drug-metabolism pharmacogenomic markers apply.

**Emerging / experimental.** There is no approved IRIDA-specific targeted therapy. Conceptually, a hepcidin-lowering agent (e.g., anti-hepcidin or BMP-pathway antagonist) would be mechanistically rational, but the active TMPRSS6 drug pipeline is aimed at the *opposite* problem (raising hepcidin in iron overload — see Section 13).

---

## 13. Prevention

- **Primary prevention:** Not applicable — the disorder is monogenic with no environmental/infectious trigger.
- **Secondary/tertiary prevention:** Early molecular diagnosis and timely iron repletion (parenteral, or oral iron + vitamin C) to prevent developmental sequelae, especially during childhood growth windows.
- **Genetic counseling (central):** Autosomal-recessive 25% sibling recurrence risk; carrier/cascade testing of relatives; reproductive options (prenatal and preimplantation genetic testing) where the family's TMPRSS6 variants are defined.
- **Screening:** No population or newborn screening. Cascade testing within affected families is the practical preventive tool.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** TMPRSS6 is evolutionarily conserved. Mouse ortholog **Tmprss6** (NCBI Gene 71753; *Mus musculus*, NCBI:txid10090).
- **Natural disease:** No well-documented naturally occurring companion-animal or wildlife IRIDA in OMIA; IRIDA is essentially a human-defined disorder recapitulated in engineered rodents.
- **Comparative biology:** The hepcidin–ferroportin axis and matriptase-2's suppressive role are conserved between human and mouse; Tmprss6 disruption in mice reproduces the human iron-deficiency phenotype (see Section 15).
- **Zoonotic potential:** None (non-infectious genetic disease).

---

## 15. Model Organisms

**Mouse is the principal model.** Two complementary genetic models recapitulate IRIDA:
- **Tmprss6 knockout** and the ENU-derived **"mask" mouse** (Mt2^mask, lacking the catalytic domain), which develop elevated hepcidin, systemic iron deficiency, and microcytic anemia.
- **Modifier/therapeutic-target validation:** Finberg et al. showed "heterozygous loss of Tmprss6 in Hfe(-/-) mice reduced systemic iron overload, whereas homozygous loss caused systemic iron deficiency and elevated hepatic expression of hepcidin" ([PMID: 21355094](https://pubmed.ncbi.nlm.nih.gov/21355094/)) — establishing Tmprss6 as a genetic modifier and therapeutic target.

**Domain-function dissection in mice.**
- "The catalytic domain, but not its proteolytic activity, was required for Mt2 to suppress hepcidin expression" ([PMID: 32384154](https://pubmed.ncbi.nlm.nih.gov/32384154/)).
- "The stem region of MT2 determines the specificity and efficacy for substrate cleavage" ([PMID: 30559294](https://pubmed.ncbi.nlm.nih.gov/30559294/)).
- Hepatocyte neogenin is required: "Mt2 suppression of hepcidin relies on the presence of Neo1" ([PMID: 41534828](https://pubmed.ncbi.nlm.nih.gov/41534828/)).

**Phenotype recapitulation:** Excellent for the core biochemical and hematologic phenotype (high hepcidin, low iron, microcytic anemia). **Limitations:** models are engineered rather than spontaneous; species differences in iron demand and lifespan; human genotype–phenotype heterogeneity (e.g., specific missense alleles) not fully captured by null models.

**Translational fulcrum — the "mirror-image" drug pipeline.** Because loss of matriptase-2 *raises* hepcidin, TMPRSS6 inhibition is being developed to *raise* hepcidin in iron-overload disease:
- Antisense oligonucleotides: "antisense oligonucleotide-mediated inhibition of TMPRSS6, an upstream regulator of hepcidin" ([PMID: 24589273](https://pubmed.ncbi.nlm.nih.gov/24589273/)).
- Anti-matriptase-2 antibody RLYB331: "we tested a fully human anti-matriptase-2 antibody, RLYB331, which blocks the protease activity of matriptase-2" ([PMID: 38241484](https://pubmed.ncbi.nlm.nih.gov/38241484/)).
- Clinical-stage antibody DISC-3405: "a novel humanized monoclonal antibody that enhances hepcidin expression by inhibiting TMPRSS6"; in Phase 1 it "increased hepcidin-25 and reduced serum iron and transferrin saturation across dose levels" ([PMID: 42053460](https://pubmed.ncbi.nlm.nih.gov/42053460/)).

These programs validate TMPRSS6/matriptase-2 biology pharmacologically and, by inference, confirm the IRIDA mechanism in reverse.

---

## Mechanistic Model / Interpretation

IRIDA is best understood as a **hormonal iron-trafficking disease driven by a single upstream protease loss**. The elegance of the model is that one molecular event (loss of matriptase-2) propagates deterministically to the clinical picture:

```
GENE            PROTEIN            SIGNALING           HORMONE        EFFECTOR            PHENOTYPE
TMPRSS6  ──►  matriptase-2  ──►  BMP/SMAD (via     ──► hepcidin  ──► ferroportin    ──►  hypochromic
(LoF, AR)     (loss of           HJV/NEO1              (HIGH,         degradation on       microcytic
              function)          cleavage/            inappropriate)  enterocytes +        anemia,
                                 inhibition lost)                     macrophages          low TSAT,
                                                                                           oral-iron
                                                                                           refractory
```

Everything downstream of hepcidin is shared with normal iron physiology; the disease-specific lesion is the failure to *restrain* hepcidin when iron is low. This explains three otherwise puzzling clinical features simultaneously: (1) why oral iron fails (absorption is blocked at the enterocyte), (2) why ferritin can be normal/high despite anemia (iron is trapped in macrophages), and (3) why the disease is diagnostically distinguishable from every other microcytic anemia by hepcidin measurement.

The **upstream vs downstream** hierarchy also clarifies therapeutic logic: the ideal IRIDA therapy would act upstream (restore matriptase-2 function or lower hepcidin), whereas current management acts far downstream by force-feeding iron parenterally past the enterocyte block. Conversely, the same axis run in reverse (inhibit TMPRSS6 → raise hepcidin) is a validated strategy for iron-overload diseases — a striking example of one gene being both the cause of one disease and the drug target for its mirror image.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [18408718](https://pubmed.ncbi.nlm.nih.gov/18408718/) | *Mutations in TMPRSS6 cause IRIDA* | Foundational — establishes causal gene and matriptase-2's hepcidin-regulating role |
| [23729726](https://pubmed.ncbi.nlm.nih.gov/23729726/) | *Iron refractory iron deficiency anemia* (review) | Core clinical/mechanistic reference: inheritance, hallmarks, hepcidin discriminator, treatment, DDx |
| [25156943](https://pubmed.ncbi.nlm.nih.gov/25156943/) | *Functional and clinical impact of novel TMPRSS6 variants* | Functional LoF evidence; genotype–phenotype (nonsense = severe); p.W590R |
| [42053460](https://pubmed.ncbi.nlm.nih.gov/42053460/) | *Phase 1 DISC-3405 anti-TMPRSS6* | BMP/SMAD-HJV mechanism statement; target validation |
| [19820699](https://pubmed.ncbi.nlm.nih.gov/19820699/) | *Common TMPRSS6 variants & iron status* (GWAS) | Modifier variant rs855791 effects on iron/MCV |
| [36261087](https://pubmed.ncbi.nlm.nih.gov/36261087/) | *TMPRSS6 mutations in Saudi families* | Founder allele p.V736A; atypical normocytic presentation |
| [21355094](https://pubmed.ncbi.nlm.nih.gov/21355094/) | *Tmprss6 modifier of Hfe in mice* | Mouse model; effector definition (enterocyte + macrophage) |
| [23319530](https://pubmed.ncbi.nlm.nih.gov/23319530/) | *IRIDA with hyperferritinemia; WES* | Atypical hyperferritinemia; WES diagnostic utility |
| [30594846](https://pubmed.ncbi.nlm.nih.gov/30594846/) | *Oral iron + vitamin C in IRIDA phenotype* | 86% response — emerging oral therapy |
| [35163840](https://pubmed.ncbi.nlm.nih.gov/35163840/) | *TSAT/Hepcidin ratio discriminates* | Diagnostic biomarker ratio |
| [32384154](https://pubmed.ncbi.nlm.nih.gov/32384154/) | *Ectodomain nonproteolytic role* | Catalytic-domain requirement (mouse) |
| [30559294](https://pubmed.ncbi.nlm.nih.gov/30559294/) | *Catalytic/stem/TM portions required* | Domain structure-function |
| [41534828](https://pubmed.ncbi.nlm.nih.gov/41534828/) | *MT2 requires hepatocyte neogenin* | NEO1 dependency in vivo |
| [24589273](https://pubmed.ncbi.nlm.nih.gov/24589273/) | *Modulation of hepcidin — ASO* | Mirror-image therapy (ASO) |
| [38241484](https://pubmed.ncbi.nlm.nih.gov/38241484/) | *Anti-matriptase-2 antibody RLYB331* | Mirror-image therapy (antibody) in β-thalassemic mice |
| [28447549](https://pubmed.ncbi.nlm.nih.gov/28447549/) | *Child with complex TMPRSS6 genotype* | Critical growth-period vulnerability |

**Concordance:** All reviewed papers point to a consistent single-gene, single-mechanism model. No paper challenges the central TMPRSS6→hepcidin causal chain; heterogeneity is confined to phenotypic spectrum (occasional hyperferritinemia or normocytosis) and treatment response (genotype-dependent).

---

## Limitations and Knowledge Gaps

1. **Prevalence is undetermined.** No population-level incidence/prevalence figures exist; the disease is likely under-diagnosed among common microcytic anemias.
2. **No human -omics datasets.** There are no established large-scale transcriptomic/proteomic/metabolomic profiles specific to IRIDA patients; mechanism rests on in-vitro assays and mouse models.
3. **Monoallelic variant significance is unresolved.** The pathogenic contribution and penetrance of single heterozygous TMPRSS6 variants to milder/atypical iron deficiency remain under study.
4. **No IRIDA-specific approved therapy.** Current care is symptomatic (parenteral iron); the mechanistically ideal hepcidin-lowering therapeutic has not been developed for IRIDA (all TMPRSS6 drugs target the opposite direction).
5. **Genotype–phenotype rules are incomplete.** Beyond the nonsense/nonsense = severe correlation, predictive rules for individual missense alleles and modifier interactions are not fully defined.
6. **Long-term neurodevelopmental outcomes** of childhood iron deficiency in IRIDA are not rigorously quantified.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a natural-history registry** to quantify prevalence, sex ratio, age-dependent hemoglobin trajectory, and neurodevelopmental outcomes.
2. **Prospective trial of oral iron + vitamin C vs IV iron** in molecularly confirmed IRIDA, powered on hemoglobin response and quality of life, to validate the 86% pediatric response signal ([PMID: 30594846](https://pubmed.ncbi.nlm.nih.gov/30594846/)).
3. **Standardize the TSAT/hepcidin ratio** as a first-line discriminating test with defined cutoffs across laboratories ([PMID: 35163840](https://pubmed.ncbi.nlm.nih.gov/35163840/)).
4. **Functional classification pipeline** (cell-based autoactivation + HJV-cleavage + hepcidin-suppression assays, per [PMID: 25156943](https://pubmed.ncbi.nlm.nih.gov/25156943/)) to resolve VUS and monoallelic variants toward ACMG reclassification.
5. **Explore hepcidin-lowering therapeutics for IRIDA** (anti-hepcidin antibodies, BMP-pathway antagonists, or ferroportin stabilizers) — the mechanistically rational but unexploited direction.
6. **Cascade genetic counseling and carrier screening** in consanguineous populations harboring founder alleles (p.V736A, p.W590R).


## Artifacts

- [OpenScientist final report](IRIDA_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](IRIDA_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 32 |
| Quoted claims found in source | 31 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 16 |
| On topic | 12 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:25156943` *(abstract only)*: "all but the p.T287N variant impair matriptase-2 autoproteolytic activation, decrease the ability to cleave membrane HJV and inhibit the HJV-dependent hepcidin activation"
  - closest text in source: "All but the p.T287N variant impair matriptase-2 autoproteotylic activation, decrease the ability to cleave membrane HJV and inhibit the HJV-dependent hepcidin activation"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 19 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008788` (2 mentions) - the report calls it "MONDO"; MONDO calls it **IRIDA syndrome**
- `HP:0004840` (1 mention) - the report calls it "Lab / clinical"; HP calls it **Hypochromic microcytic anemia**
- `HP:0001935` (1 mention) - the report calls it "Lab"; HP calls it **Microcytic anemia**
- `HP:0025066` (1 mention) - the report calls it "Lab"; HP calls it **Decreased mean corpuscular volume**
- `HP:0040303` (1 mention) - the report calls it "Lab"; HP calls it **Decreased circulating iron concentration**
- `HP:0012378` (1 mention) - the report calls it "Symptom"; HP calls it **Fatigue**
- `HP:0000980` (1 mention) - the report calls it "Clinical sign"; HP calls it **Pallor**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0060586` (1 mention) - the report calls it "multicellular organismal iron ion homeostasis"; GO calls it **multicellular organismal-level iron ion homeostasis**, and lists "multicellular organismal iron ion homeostasis" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.