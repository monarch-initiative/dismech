---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-12T18:03:14.514353'
end_time: '2026-09-12T18:19:36.556961'
duration_seconds: 982.04
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Triple-Negative Breast Cancer
  mondo_id: MONDO:0005494
  category: ''
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
citation_count: 57
reference_validation:
  total_references: 57
  verified: 57
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 16
  quotes_valid: 15
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:42373230
  relevance_assessed: 57
  on_topic: 34
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 28
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 6
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: DOID:0060081
    reported_labels:
    - Disease Ontology
    ontology_label: triple-negative breast cancer
  - term_id: HP:0031416
    reported_labels:
    - Breast mass / palpable lump
    ontology_label: Abnormal nasal mucus secretion
  - term_id: HP:0030075
    reported_labels:
    - neoplasm of lung
    ontology_label: Ductal carcinoma in situ
  - term_id: UBERON:0000310
    reported_labels:
    - Primary organ:** breast
    - UBERON:** breast
    ontology_label: breast
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Triple_Negative_Breast_Cancer-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Triple_Negative_Breast_Cancer-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Triple-Negative Breast Cancer
- **MONDO ID:** MONDO:0005494 (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Triple-Negative Breast Cancer** covering all of the
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

# Triple-Negative Breast Cancer (MONDO:0005494): A Comprehensive Disease Characteristics Report

## Summary

**Triple-negative breast cancer (TNBC)** is an aggressive, molecularly heterogeneous subtype of invasive breast carcinoma that accounts for approximately **10–15% of all new breast cancer diagnoses**. It is operationally defined by the absence of three receptors on tumor immunohistochemistry: estrogen receptor (ER), progesterone receptor (PR), and lack of amplification/overexpression of human epidermal growth factor receptor 2 (HER2). This receptor-negative phenotype removes the two most successful therapeutic targets in breast oncology — endocrine therapy and HER2-directed agents — leaving cytotoxic chemotherapy, and more recently immunotherapy and biology-guided targeted agents, as the therapeutic backbone. TNBC disproportionately affects younger women, women of African ancestry, premenopausal women, and germline *BRCA1* mutation carriers, and it is a major contributor to racial disparities in breast cancer mortality.

Mechanistically, TNBC is best understood as a **TP53-mutant, homologous-recombination–deficient (HRD) disease**. Near-universal *TP53* mutation (with combined loss-of-function and oncogenic gain-of-function) cooperates with loss of homologous-recombination (HR) DNA repair — arising from germline or somatic *BRCA1/2*, *PALB2*, and *RAD51* pathway defects, or from epigenetic *BRCA1* promoter hypermethylation ("BRCAness") — to produce profound genomic instability. This drives a highly proliferative, basal-like tumor cell that undergoes early hematogenous spread with a strong tropism for visceral organs and brain. Superimposed metabolic reprogramming (Warburg glycolysis and glutamine addiction) supports rapid proliferation and stress resistance. TNBC resolves into four tumor-intrinsic transcriptomic subtypes — **basal-like 1 (BL1), basal-like 2 (BL2), mesenchymal (M), and luminal androgen receptor (LAR)** — that differ in biology, prognosis, and therapy response.

Clinically, the HRD/genomic-instability biology has become therapeutically actionable. Standard of care now includes **neoadjuvant pembrolizumab plus chemotherapy (KEYNOTE-522)** for stage II–III disease, **PARP inhibitors (olaparib, talazoparib)** exploiting synthetic lethality in germline-*BRCA*-mutated tumors, the **Trop-2 antibody–drug conjugate sacituzumab govitecan** for metastatic disease, and **androgen-receptor blockade** for the LAR subtype. Tumor-infiltrating lymphocytes (TILs) predict chemoimmunotherapy response. Despite these advances, metastatic TNBC still carries a dismal prognosis (~12-month median overall survival), and prevention in hereditary disease relies on risk-reducing surgery and intensified surveillance in *BRCA1/2* carriers. This report synthesizes 14 confirmed findings across 65 reviewed papers into the full 15-section disease knowledge template. No primary patient-level data files were provided; all statements are aggregated disease-level evidence from primary literature and reviews.

---

## Key Findings

### 1. Disease Information

TNBC is a subtype of invasive breast carcinoma "with a poor prognosis and aggressive behavior that accounts for 10-15% of all new cases of breast cancer... characterized by the absence of progesterone and estrogen receptor expression and lacks gene amplification or overexpression of HER2" ([PMID: 37044296](https://pubmed.ncbi.nlm.nih.gov/37044296/)). It is a molecular/immunohistochemical classification rather than a distinct histologic entity — most TNBCs are invasive ductal carcinomas of no special type, frequently high-grade (grade 3) and basal-like.

**Key identifiers and ontology terms:**

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0005494 (triple-negative breast cancer) |
| MeSH | Triple Negative Breast Neoplasms (D064726) |
| ICD-10 | C50.x (malignant neoplasm of breast; TNBC not separately coded) |
| ICD-O morphology | 8500/3 (invasive ductal carcinoma NST, most common) |
| NCIT | C71732 (Triple-Negative Breast Carcinoma) |
| Disease Ontology | DOID:0060081 |

**Synonyms / alternative names:** triple-negative breast carcinoma; ER-/PR-/HER2- breast cancer; basal-like breast cancer (overlapping but not identical — see below); ductal breast carcinoma triple-negative.

**Source of information:** This report is derived predominantly from *aggregated disease-level resources* — clinical trials, molecular profiling cohorts (TCGA), registry data (SEER), and mechanistic literature — rather than individual EHR records.

### 2. Etiology

**Causal factors and risk factors.** TNBC arises from acquired and inherited defects in genome maintenance. Established epidemiological risk factors are well characterized: "Risk factors for TNBC include young age at breast cancer diagnosis, young age at menarche, high parity, lack of breast feeding, high body mass index and African American ethnicity. The majority of BRCA1 tumours are TNBC" ([PMID: 21080741](https://pubmed.ncbi.nlm.nih.gov/21080741/)).

- **Genetic risk factors:** Germline pathogenic variants confer graded risk. In multigene panel testing, "Germline pathogenic variants in BARD1, BRCA1, BRCA2, PALB2, and RAD51D were associated with high risk (odds ratio > 5.0) of TNBC," while BRIP1, RAD51C, and TP53 conferred moderate risk (OR > 2) ([PMID: 30099541](https://pubmed.ncbi.nlm.nih.gov/30099541/)). *BRCA1* is the dominant hereditary driver, and the majority of *BRCA1*-associated tumors are triple-negative.
- **Environmental/reproductive risk factors:** young age at menarche, high parity, lack of breastfeeding, high BMI/obesity, and African American ethnicity ([PMID: 21080741](https://pubmed.ncbi.nlm.nih.gov/21080741/)).
- **Protective factors:** Breastfeeding is protective (its absence is a risk factor). In *BRCA* carriers post-oophorectomy, estrogen-only hormone replacement therapy was **not** associated with increased breast cancer risk and each year was associated with reduced risk (HR 0.90, 95% CI 0.81–0.99; and HR 0.87 in *BRCA1* carriers) ([PMID: 41949865](https://pubmed.ncbi.nlm.nih.gov/41949865/)).
- **Gene–environment interactions:** Obesity and ancestry interact with tumor immunobiology — in a balanced Black/White TNBC cohort, immune deconvolution showed higher abundance of several immune cell populations in tumors from Black women, though neither Black race nor obesity was intrinsically predictive of poor outcome after balancing for stage and subtype ([PMID: 41224793](https://pubmed.ncbi.nlm.nih.gov/41224793/)).

### 3. Phenotypes

TNBC most commonly presents as a **palpable breast mass** (HP:0031416, breast mass), often growing rapidly. In an imaging cohort, TNBC was associated with presentation on breast exam (56%), palpability (59.1%), more invasive ductal carcinoma (92.4%), higher stage (stage III, 16.5%), and higher grade (grade 3, 82.7%), and notably *lower* mammographic breast density ([PMID: 31927471](https://pubmed.ncbi.nlm.nih.gov/31927471/)).

| Phenotype | HPO suggestion | Characteristics |
|-----------|---------------|-----------------|
| Breast mass / palpable lump | HP:0031416 | Adult-onset; often rapidly enlarging; frequently interval (between screens) |
| High tumor grade (grade 3) | — | 82.7% grade 3; severe/aggressive |
| Visceral metastasis | HP:0030075 (neoplasm of lung), liver/lung involvement | Early; poor prognosis |
| Brain metastasis | HP:0030692 (brain neoplasm) | Overrepresented in rapid-relapse TNBC (10.9%) |
| Lymph node metastasis | HP:0002716 | Common at presentation |

**Age of onset:** adult, skewing younger than other breast cancers (basal subtype significantly more common in patients aged <50 and premenopausal women; [PMID: 37482851](https://pubmed.ncbi.nlm.nih.gov/37482851/)). **Severity/progression:** severe, progressive, with early distant relapse. **Quality of life:** In metastatic disease, PARP inhibition improved health-related QoL versus chemotherapy (global health status difference 7.5 points, 95% CI 2.48–12.44, P=0.0035; [PMID: 31446213](https://pubmed.ncbi.nlm.nih.gov/31446213/)).

### 4. Genetic / Molecular Information

**TP53 and BRCA1/2 are the dominant genomic drivers.** In germline *BRCA*-mutated early TNBC (NEOTALA/talazoparib cohort), "Ninety-eight percent of patients had TP53 mutations," and "Strong concordance (97.8%) was observed between tumor BRCA and germline BRCA mutations, and 90.5% (38/42)... were predicted to exhibit BRCA loss of heterozygosity (LOH)" ([PMID: 38869771](https://pubmed.ncbi.nlm.nih.gov/38869771/)).

- **Causal genes:** *TP53* (OMIM 191170), *BRCA1* (OMIM 113705), *BRCA2* (OMIM 600185), *PALB2*, *RAD51C/D*, *BARD1*, *BRIP1* (HGNC-approved symbols). High-risk (OR>5): *BARD1, BRCA1, BRCA2, PALB2, RAD51D*; moderate-risk (OR>2): *BRIP1, RAD51C, TP53* ([PMID: 30099541](https://pubmed.ncbi.nlm.nih.gov/30099541/)).
- **Somatic vs germline:** *BRCA* alterations occur both germline and somatically, with distinct biological/clinical patterns; somatic alterations "should not be interpreted in isolation and require integration with germline status" ([PMID: 42492369](https://pubmed.ncbi.nlm.nih.gov/42492369/)). Whole-exome sequencing of Indian TNBC found ~106 mutations/sample, recurrent somatic mutations in *CTNNB1* (47%), *TP53* (33%), *PIK3CA*, *BRCA1/2*, and mutational signature 3 (HR-repair failure) associated with high tumor mutational burden ([PMID: 41324770](https://pubmed.ncbi.nlm.nih.gov/41324770/)).
- **Variant classification/type:** Pathogenic germline *BRCA1* founder-type frameshifts (e.g., c.66_67delAG [185delAG], c.3226_3227delAG) reported in TNBC; somatic *TP53* missense predominate ([PMID: 34097676](https://pubmed.ncbi.nlm.nih.gov/34097676/)).
- **Functional consequences:** *BRCA1/2* loss = loss of function → HRD; mutant *TP53* combines loss of function with oncogenic gain of function (see Finding 13 below).
- **Epigenetic information:** "Aberrant methylation patterns are characterized by promoter hypermethylation of tumor suppressor genes (BRCA1, CDH1, PTEN, RARβ)... and global hypomethylation that activates oncogenes and promotes genomic instability" ([PMID: 40925466](https://pubmed.ncbi.nlm.nih.gov/40925466/)). *BRCA1* promoter hypermethylation phenocopies *BRCA1* loss ("BRCAness").
- **Chromosomal abnormalities:** Genomic instability, chromosomal instability, centrosome amplification, and copy-number alterations mirroring TCGA are characteristic ([PMID: 33267874](https://pubmed.ncbi.nlm.nih.gov/33267874/); [PMID: 30859564](https://pubmed.ncbi.nlm.nih.gov/30859564/)).

### 5. Environmental Information

- **Lifestyle factors:** high BMI/obesity, high parity, lack of breastfeeding, and young age at menarche are the established modifiable/reproductive contributors ([PMID: 21080741](https://pubmed.ncbi.nlm.nih.gov/21080741/)).
- **Environmental/social determinants:** Residential racialized economic segregation independently affects outcomes — patients in the most deprived counties had higher breast cancer–specific mortality (HR 1.14) and late-stage diagnosis (OR 1.15), explaining ~28% of the excess Black-vs-White mortality ([PMID: 40105752](https://pubmed.ncbi.nlm.nih.gov/40105752/)).
- **Infectious agents:** Not applicable — TNBC is not caused by an infectious agent. (Iatrogenic infection risk, e.g., parvovirus B19 during immunochemotherapy, is a treatment complication, not a cause; [PMID: 42500288](https://pubmed.ncbi.nlm.nih.gov/42500288/).)

### 6. Mechanism / Pathophysiology

**Causal chain (initiating lesion → clinical manifestation):**

```
1. Germline or somatic loss of BRCA1/BRCA2/PALB2/RAD51 pathway
   —OR— epigenetic BRCA1 promoter hypermethylation ("BRCAness")
        │  leads to
        ▼
2. Homologous-recombination deficiency (HRD) — inability to accurately
   repair DNA double-strand breaks
        │  results in
        ▼
3. Near-universal TP53 mutation (loss-of-function + gain-of-function),
   abrogating G2/M checkpoint and apoptosis
        │  leads to
        ▼
4. Genomic instability: chromosomal instability, centrosome
   amplification, loss of heterozygosity, high mutational burden
        │  drives
        ▼
5. Emergence of a highly proliferative, poorly differentiated
   basal-like tumor cell (EGFR+, CK5/6+, high Ki67)
        │  supported by
        ▼
6. Metabolic reprogramming — Warburg aerobic glycolysis + glutamine
   addiction — fueling biosynthesis, redox/ferroptosis defense
        │  enables
        ▼
7. Invasion, EMT, and early hematogenous dissemination
        │  results in
        ▼
8. Visceral- and brain-tropic metastasis, chemoresistant relapse,
   and death (~12-month median OS in metastatic disease)

   BRANCH (LAR subtype): androgen-receptor–driven signaling defines a
   distinct, chemo-resistant, AR-targetable trajectory.
```

**Molecular detail.**

- **Mutant TP53 gain-of-function.** "the R181C mutation leads to 'loss-of-function' of transcriptional regulating tumor suppressor genes like p21, bax, and PUMA as well as 'gain-of-function' of transcriptional regulating tumor promoting genes of PIK3CA, SHC1, SRC and PAK4. This dysregulation promotes genomic instability" ([PMID: 41484250](https://pubmed.ncbi.nlm.nih.gov/41484250/)). Mutant p53 also drives loss of the wild-type allele: "we observed profound stabilization of mutp53 protein, the loss of p21 expression, the abrogation of G2/M checkpoint, chromosomal instability, centrosome amplification" (via Nek2 upregulation; [PMID: 33267874](https://pubmed.ncbi.nlm.nih.gov/33267874/)). *GO terms:* GO:0006281 (DNA repair), GO:0000724 (double-strand break repair via homologous recombination), GO:0007049 (cell cycle), GO:0006915 (apoptotic process).
- **HRD synthetic lethality.** "Poly(ADP-ribose) polymerase (PARP) inhibitors exploit this deficiency through synthetic lethality... especially in BRCA1 or BRCA2 mutation carriers" ([PMID: 29753961](https://pubmed.ncbi.nlm.nih.gov/29753961/)). Basal-like/TNBC tumors "share several histo-molecular characteristics with BRCA1-deficient tumors, including genomic instability and reduced BRCA1 expression beyond germline-mutated cases" ([PMID: 42394702](https://pubmed.ncbi.nlm.nih.gov/42394702/)).
- **Metabolic reprogramming.** TNBC exhibits the Warburg effect and glutamine addiction: "the addiction of TNBC to Gln could facilitate the proliferation and invasiveness of these cancers. Thus, Gln metabolism inhibitors, such as CB-839, could be applied" ([PMID: 34083056](https://pubmed.ncbi.nlm.nih.gov/34083056/)). Integrated omics in MDA-MB-231 show glutamine drives reductive TCA lipogenesis/sterol synthesis (SREBF1/2) while glucose "licens[es] chromatin engagement, DNA replication, and mitotic progression" ([PMID: 42373230](https://pubmed.ncbi.nlm.nih.gov/42373230/)). *CHEBI:* glutamine (CHEBI:28300), glucose (CHEBI:17234), lactate (CHEBI:24996).
- **Immune microenvironment.** TILs shape prognosis and therapy response; the immunomodulatory signal reflects infiltrating lymphocytes and varies by subtype (highest in BL1; [PMID: 30312311](https://pubmed.ncbi.nlm.nih.gov/30312311/)).
- **Cell types (CL):** basal/luminal-progenitor mammary epithelial cell (CL:0002326, luminal epithelial cell of mammary gland; CL:0000646 basal cell), tumor-infiltrating T lymphocyte (CL:0000084), regulatory T cell (CL:0000815).

### 7. Anatomical Structures Affected

- **Primary organ:** breast (UBERON:0000310), specifically mammary gland epithelium/ductal-lobular units (UBERON:0002114 duct; mammary gland epithelium).
- **Tissue/cell:** epithelial tissue; basal-like tumors express EGFR and cytokeratin 5/6 and arise from a basal/luminal-progenitor lineage.
- **Secondary organ involvement (metastatic tropism):** lung, liver, bone, lymph nodes, and brain. In a real-world sacituzumab govitecan cohort, metastatic sites were lymph nodes (60.9%), bone (43.0%), lung (42.6%), liver (33.2%), brain (26.2%) ([PMID: 42413328](https://pubmed.ncbi.nlm.nih.gov/42413328/)). Rapid-relapse TNBC preferentially presents with visceral (74.9%) and brain (10.9%) metastases ([PMID: 42499497](https://pubmed.ncbi.nlm.nih.gov/42499497/)).
- **Subcellular (GO CC):** nucleus (GO:0005634, site of TP53/BRCA DNA-repair defects), centrosome (GO:0005813, amplified), mitochondrion (GO:0005739, metabolic rewiring).
- **Lateralization:** unilateral at presentation (as in most breast cancers), bilateral risk elevated in *BRCA* carriers.
- **UBERON:** breast (UBERON:0000310), mammary gland (UBERON:0001911), lung (UBERON:0002048), liver (UBERON:0002107), brain (UBERON:0000955), bone (UBERON:0002481), lymph node (UBERON:0000029).

### 8. Temporal Development

- **Onset:** adult-onset, skewing younger/premenopausal; basal subtype significantly more common in patients <50 and premenopausal women ([PMID: 37482851](https://pubmed.ncbi.nlm.nih.gov/37482851/)).
- **Progression:** rapid. TNBC is graded by AJCC stage; stage III independently predicts worse recurrence-free survival (HR 2.18) and distant metastasis-free survival (HR 2.43) ([PMID: 42292008](https://pubmed.ncbi.nlm.nih.gov/42292008/)).
- **Disease course:** aggressive, progressive, with a characteristic early relapse peak. "Rapid relapse" TNBC (distant metastasis/death within 24 months) is associated with platinum resistance and visceral/CNS tropism ([PMID: 42499497](https://pubmed.ncbi.nlm.nih.gov/42499497/)).
- **Critical period / window of opportunity:** the neoadjuvant setting — achieving pathologic complete response (pCR) is the key early prognostic milestone and intervention window (KEYNOTE-522).
- **Remission:** treatment-induced (pCR after neoadjuvant chemoimmunotherapy); spontaneous remission is not a feature.

### 9. Inheritance and Population

- **Epidemiology:** ~10–15% of all breast cancers ([PMID: 37044296](https://pubmed.ncbi.nlm.nih.gov/37044296/)); basal-like ~15–20% of cases ([PMID: 42394702](https://pubmed.ncbi.nlm.nih.gov/42394702/)).
- **Inheritance:** the hereditary fraction follows **autosomal dominant** transmission of *BRCA1/2*, *PALB2*, *RAD51* pathway variants with incomplete, age-dependent penetrance; the disease itself is multifactorial/polygenic. Founder *BRCA1* variants (e.g., 185delAG) occur ([PMID: 34097676](https://pubmed.ncbi.nlm.nih.gov/34097676/)).
- **Sex ratio:** overwhelmingly female (as with breast cancer generally).
- **Population demographics:** Higher incidence and worse outcomes in Black/African American women and younger women. "Black women experience a 36% higher mortality rate" than White women, partly attributable to higher prevalence of aggressive subtypes such as TNBC ([PMID: 42320849](https://pubmed.ncbi.nlm.nih.gov/42320849/)). SEER analyses show young Black women with TNBC and Asian women <50 carry elevated hazard ratios ([PMID: 41896553](https://pubmed.ncbi.nlm.nih.gov/41896553/)). In African American women with invasive breast cancer, 64.1% met NCCN genetic-testing criteria; pathogenic mutations concentrated in *BRCA2* (29.4%) and *BRCA1* (15.7%) ([PMID: 33083949](https://pubmed.ncbi.nlm.nih.gov/33083949/)).

### 10. Diagnostics

**Core diagnosis is immunohistochemistry demonstrating ER-negative, PR-negative, HER2-negative status** (with HER2 confirmed by ISH if IHC equivocal). Within TNBC, basal-like tumors are identified by additional markers: "Basal subtype was significantly more common in patients aged <50 years at diagnosis, premenopausal women, patients with positive nodal status, those with grade III tumours, and patients with Ki67 proliferation marker >20% (p<0.05)" — basal markers being EGFR and CK5/6 ([PMID: 37482851](https://pubmed.ncbi.nlm.nih.gov/37482851/)). An IHC combination of high CK19 + high Ki-67 + E-cadherin loss identified the worst relapse-free and overall survival ([PMID: 39435793](https://pubmed.ncbi.nlm.nih.gov/39435793/)).

- **Imaging:** mammography (TNBC associated with lower mammographic density), MRI, ultrasound; TNBC often presents as an interval/palpable mass ([PMID: 31927471](https://pubmed.ncbi.nlm.nih.gov/31927471/)). Trop-2-directed PET/CT is emerging ([PMID: 42559486](https://pubmed.ncbi.nlm.nih.gov/42559486/)).
- **Biopsy/pathology:** core-needle biopsy with histopathology (usually invasive ductal carcinoma NST, grade 3) plus IHC panel.
- **Genetic testing:** Germline multigene panel testing (BRCA1/2, PALB2, RAD51C/D, BARD1, BRIP1, TP53) is recommended given the high hereditary yield ([PMID: 30099541](https://pubmed.ncbi.nlm.nih.gov/30099541/)); tumor BRCA and germline BRCA show 97.8% concordance ([PMID: 38869771](https://pubmed.ncbi.nlm.nih.gov/38869771/)). NCCN criteria capture the majority but miss ~12.5% of African American mutation carriers ([PMID: 33083949](https://pubmed.ncbi.nlm.nih.gov/33083949/)).
- **Omics/transcriptomic diagnostics:** Lehmann TNBCtype-4 subtyping (BL1, BL2, M, LAR) and PAM50, plus HRD/genomic scar scores and DNA-damage-repair signatures, refine classification and predict therapy ([PMID: 27310713](https://pubmed.ncbi.nlm.nih.gov/27310713/); [PMID: 37334114](https://pubmed.ncbi.nlm.nih.gov/37334114/)).
- **Predictive biomarkers:** PD-L1 (immunotherapy), germline/somatic BRCA and HRD (PARP inhibitors), TILs (pCR), Trop-2 (ADC), AR (LAR subtype).

### 11. Outcome / Prognosis

TNBC has the worst stage-adjusted prognosis of the major breast cancer subtypes. **Metastatic TNBC "bears a dismal prognosis with an average survival of 12 months"** ([PMID: 29753961](https://pubmed.ncbi.nlm.nih.gov/29753961/)). In a large real-world PD-L1-negative metastatic cohort (n=929), "Median rwOS and rwPFS... were 12.2 (10.7, 14.4) months and 4.7 (4.5, 5.2) months" ([PMID: 42554864](https://pubmed.ncbi.nlm.nih.gov/42554864/)).

| Prognostic factor | Direction | Source |
|-------------------|-----------|--------|
| Stage III | Worse RFS (HR 2.18), DMFS (HR 2.43) | [PMID: 42292008](https://pubmed.ncbi.nlm.nih.gov/42292008/) |
| TILs present | Better (higher pCR: 70% vs 48%) | [PMID: 42360368](https://pubmed.ncbi.nlm.nih.gov/42360368/) |
| pCR achieved | Better EFS/OS | [PMID: 42607489](https://pubmed.ncbi.nlm.nih.gov/42607489/) |
| Basal markers (EGFR/CK5/6, CK19+Ki67+/E-cad loss) | Worse RFS/OS | [PMID: 39435793](https://pubmed.ncbi.nlm.nih.gov/39435793/) |
| LAR subtype | Chemo-resistant, lowest pCR | [PMID: 29940524](https://pubmed.ncbi.nlm.nih.gov/29940524/) |
| Low SPDEF expression | Worse RFS/OS | [PMID: 42305508](https://pubmed.ncbi.nlm.nih.gov/42305508/) |
| High miR-1911-3p | Worse recurrence-free survival (HR 3.04) | [PMID: 42517063](https://pubmed.ncbi.nlm.nih.gov/42517063/) |

**Racial disparity:** Black women experience 36% higher breast cancer mortality, and residential segregation explains ~28% of the excess mortality ([PMID: 42320849](https://pubmed.ncbi.nlm.nih.gov/42320849/); [PMID: 40105752](https://pubmed.ncbi.nlm.nih.gov/40105752/)). **Complications** include visceral organ failure from metastasis, CNS metastasis, and treatment toxicities (e.g., immune-related adverse events, cytopenias).

### 12. Treatment

TNBC treatment has shifted from chemotherapy-only to **biology-guided, multimodal therapy**.

**Neoadjuvant chemoimmunotherapy (standard for stage II–III).** "Neoadjuvant chemotherapy (NACT) combined with pembrolizumab is now standard care for early-stage, triple-negative breast cancer (TNBC), based on KEYNOTE-522 demonstrating improved pathological complete response (pCR), event-free survival, and overall survival" ([PMID: 42607489](https://pubmed.ncbi.nlm.nih.gov/42607489/)). Real-world pCR ~57%, and TILs predict response (70% vs 48% pCR, p=0.0027; TIL-positive 2.44× more likely to achieve pCR; [PMID: 42360368](https://pubmed.ncbi.nlm.nih.gov/42360368/)). *NCIT:* pembrolizumab (C106432).

**PARP inhibitors (germline BRCA).** In OlympiAD, olaparib prolonged PFS versus chemotherapy, with strong benefit in the triple-negative subgroup (PFS HR 0.47, 95% CI 0.32–0.69; [PMID: 36971103](https://pubmed.ncbi.nlm.nih.gov/36971103/)), durable long-term survival in first-line metastatic disease ([PMID: 36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/)), and improved QoL ([PMID: 31446213](https://pubmed.ncbi.nlm.nih.gov/31446213/)). Talazoparib is used in the neoadjuvant germline-*BRCA* setting ([PMID: 38869771](https://pubmed.ncbi.nlm.nih.gov/38869771/)). *NCIT:* olaparib (C71721), talazoparib (C97316).

**Trop-2 antibody–drug conjugate (metastatic).** Sacituzumab govitecan (SG) delivers durable benefit in real-world mTNBC: median rwPFS 6.4 months, rwOS 13.6 months, ORR/CR+PR 37.5% ([PMID: 42413328](https://pubmed.ncbi.nlm.nih.gov/42413328/)). Combination with PD-1 inhibitors ± antiangiogenics improves response in later lines ([PMID: 42714605](https://pubmed.ncbi.nlm.nih.gov/42714605/)), and SG synergizes with TRAIL agonists preclinically ([PMID: 42601637](https://pubmed.ncbi.nlm.nih.gov/42601637/)). *NCIT:* sacituzumab govitecan (C124255).

**Androgen-receptor blockade (LAR subtype).** "The partial AR antagonist bicalutamide and the next-generation AR inhibitor enzalutamide are being assessed in standard protocols for the mitigation of TNBC" ([PMID: 36612226](https://pubmed.ncbi.nlm.nih.gov/36612226/)). AR blockade induces G1 arrest in AR-positive MDA-MB-453 cells; nuclear AR is detectable in ~30% of TNBC ([PMID: 42373057](https://pubmed.ncbi.nlm.nih.gov/42373057/)). The LAR subtype is chemo-resistant with the lowest pCR ([PMID: 29940524](https://pubmed.ncbi.nlm.nih.gov/29940524/)). *NCIT:* bicalutamide (C1685), enzalutamide (C95733).

**Other modalities:** cytotoxic chemotherapy backbone (anthracycline/taxane, platinum for HRD), surgery (breast-conserving or mastectomy), and adjuvant radiotherapy. Experimental: metabolic inhibitors (CB-839/telaglenastat targeting glutaminase; [PMID: 34083056](https://pubmed.ncbi.nlm.nih.gov/34083056/)), p53-reactivating small molecules (PRIMA-1/APR-246; [PMID: 35234267](https://pubmed.ncbi.nlm.nih.gov/35234267/)), PLK2 inhibitors to disarm mutant p53 ([PMID: 39480521](https://pubmed.ncbi.nlm.nih.gov/39480521/)), and iPSC-derived mesothelin-targeted CAR-NK cells ([PMID: 37584622](https://pubmed.ncbi.nlm.nih.gov/37584622/)).

**Adverse events:** SG toxicities include alopecia (69.1%), neutropenia (57%), nausea, anemia, diarrhea ([PMID: 42413328](https://pubmed.ncbi.nlm.nih.gov/42413328/)); pembrolizumab carries immune-related adverse events and rare severe cytopenias ([PMID: 42500288](https://pubmed.ncbi.nlm.nih.gov/42500288/); [PMID: 42314326](https://pubmed.ncbi.nlm.nih.gov/42314326/)).

### 13. Prevention

- **Primary prevention (hereditary):** For *BRCA1/2* carriers, guideline strategies include risk-reducing mastectomy, risk-reducing bilateral salpingo-oophorectomy (RRBSO), and intensified MRI surveillance. In a population-based cohort, "Of those without a prior breast cancer (n = 1021), 20.8% underwent bilateral mastectomy... 71.8% underwent RRBSO" ([PMID: 42166900](https://pubmed.ncbi.nlm.nih.gov/42166900/)); breast MRI uptake was ~31–33% ([PMID: 42647762](https://pubmed.ncbi.nlm.nih.gov/42647762/)).
- **Secondary prevention:** breast screening (mammography/MRI in high-risk women); TNBC's lower mammographic density and interval-cancer tendency underscore the value of supplemental MRI in carriers.
- **Genetic counseling and cascade testing:** identify carriers for prevention; decision-coaching reduces decisional conflict and increases decision-making in carriers with open family planning ([PMID: 42607047](https://pubmed.ncbi.nlm.nih.gov/42607047/)). Disparities in counseling access persist for young Black women ([PMID: 25868867](https://pubmed.ncbi.nlm.nih.gov/25868867/)).
- **Behavioral/public-health:** weight management, breastfeeding, and addressing socioeconomic/segregation drivers of late-stage diagnosis ([PMID: 40105752](https://pubmed.ncbi.nlm.nih.gov/40105752/)).

### 14. Other Species / Natural Disease

Spontaneous triple-negative mammary carcinoma occurs naturally in companion animals, providing immunocompetent comparative models. "Feline invasive mammary carcinomas are characterized by their high clinical aggressiveness, rare expression of hormone receptors, and pathological resemblance to human breast cancer, especially triple-negative breast cancer" — including an immune-suppressed, FOXP3+ Treg-infiltrated basal-like subgroup mirroring human TNBC immunobiology ([PMID: 31959092](https://pubmed.ncbi.nlm.nih.gov/31959092/)). In dogs, mammary epitheliosis "was a slow-growing, triple-negative process with a strong predominance of basal-like nonmyoepithelial cells" (CK14+) associated with malignancy ([PMID: 35451346](https://pubmed.ncbi.nlm.nih.gov/35451346/)).

- **Taxonomy:** *Felis catus* (NCBI:txid9685), *Canis lupus familiaris* (NCBI:txid9615), *Mus musculus* (NCBI:txid10090).
- **Orthologous genes:** *Trp53*, *Brca1*, *Brca2* (mouse orthologs of human *TP53*, *BRCA1*, *BRCA2*).
- **Veterinary relevance:** naturally occurring, immunocompetent, spontaneously arising — valuable for microenvironment and immunotherapy studies.

### 15. Model Organisms

TNBC is studied across in vitro, in vivo, and ex vivo systems.

| Model | Examples | Use |
|-------|----------|-----|
| Human cell lines | MDA-MB-231 (basal/mesenchymal), MDA-MB-453 (LAR), MDA-MB-468, HCC1806, HCC1937 | Mechanistic, drug testing |
| Syngeneic mouse | 4T1 | Immunocompetent metastasis/immunotherapy ([PMID: 33727591](https://pubmed.ncbi.nlm.nih.gov/33727591/)) |
| Patient-derived xenografts | 61-PDX panel | Recapitulate molecular heterogeneity ([PMID: 30859564](https://pubmed.ncbi.nlm.nih.gov/30859564/)) |
| Organoids | Patient-derived | Precision phototherapy/drug testing ([PMID: 38532439](https://pubmed.ncbi.nlm.nih.gov/38532439/)) |
| iPSC-derived | CAR-NK (mesothelin-targeted) | Immunotherapy development ([PMID: 37584622](https://pubmed.ncbi.nlm.nih.gov/37584622/)) |

PDX fidelity: "TNBC PDX represent all of the various TNBC subtypes identified by the Lehmann classification except for immunomodulatory subtype, which is underrepresented in PDX. NGS and copy number data showed a similar diversity of significantly mutated gene and somatic copy number alteration in PDX and the Cancer Genome Atlas TNBC patients" ([PMID: 30859564](https://pubmed.ncbi.nlm.nih.gov/30859564/)). **Limitation:** the immunomodulatory/TIL-driven biology is underrepresented in immunodeficient xenografts — a key gap given the therapeutic importance of TILs and immunotherapy.

---

## Mechanistic Model / Interpretation

TNBC is best conceptualized not as a single disease but as a **convergent phenotype of genome-maintenance failure** landing on the mammary epithelium. Two upstream lesions dominate and cooperate:

1. **HR-repair collapse** (BRCA1/2/PALB2/RAD51 mutation or *BRCA1* promoter hypermethylation) removes the cell's ability to faithfully repair double-strand breaks.
2. **TP53 loss/gain-of-function** removes the checkpoint that would otherwise arrest or eliminate genomically damaged cells, and actively upregulates oncogenic programs (PIK3CA, SRC, PAK4).

Together these produce runaway **genomic instability** — the disease's central engine — which manifests as chromosomal instability, LOH, centrosome amplification, and high mutational burden. Downstream, this instability generates a basal-like, highly proliferative tumor (EGFR+, CK5/6+, Ki67-high) that is metabolically rewired (Warburg glycolysis + glutamine addiction) to sustain proliferation and resist oxidative/ferroptotic stress. The tumor disseminates early, with a distinctive visceral and brain tropism, producing the disease's poor prognosis.

Crucially, the same instability that makes TNBC aggressive is its **therapeutic Achilles heel**: HRD confers synthetic-lethal sensitivity to PARP inhibitors and platinum, high mutational/neoantigen burden invites checkpoint immunotherapy (potentiated where TILs are present), and surface Trop-2 offers an ADC target. The four transcriptomic subtypes (BL1/BL2/M/LAR) overlay biological trajectories onto this core, with LAR representing a distinct AR-driven, chemo-resistant but AR-targetable branch. The persistent racial disparity is a product of both biology (higher TNBC prevalence in Black and young women) and structural factors (segregation, delayed diagnosis, unequal access to genetic services).

```
        HR-repair loss ──┐
   (BRCA1/2, PALB2,      │
    RAD51; or BRCA1      ├──► GENOMIC INSTABILITY ──► basal-like tumor ──► early visceral/
    hypermethylation)    │    (the engine)             + metabolic          brain metastasis
                         │                              rewiring            ──► ~12-mo mOS (mets)
        TP53 LOF+GOF ────┘                                                        │
                                                                                  ▼
   Therapeutic corollary: PARPi (HRD) · platinum · pembrolizumab (TMB/TILs) ·
                          sacituzumab govitecan (Trop-2) · AR blockade (LAR)
```

---

## Evidence Base

| PMID | Contribution | Supports / Challenges |
|------|--------------|----------------------|
| [37044296](https://pubmed.ncbi.nlm.nih.gov/37044296/) | Definition, 10–15% prevalence, receptor-negativity | Supports Finding 1 |
| [21080741](https://pubmed.ncbi.nlm.nih.gov/21080741/) | Epidemiological risk factors, BRCA1 association | Supports Findings 1–2 |
| [27310713](https://pubmed.ncbi.nlm.nih.gov/27310713/) | TNBCtype-4 subtypes (BL1/BL2/M/LAR) | Supports Finding 2 |
| [38869771](https://pubmed.ncbi.nlm.nih.gov/38869771/) | 98% TP53, 97.8% BRCA concordance, 90.5% LOH | Supports Finding 3 |
| [30099541](https://pubmed.ncbi.nlm.nih.gov/30099541/) | Panel-based risk genes (OR>5 high-risk) | Supports Finding 3 |
| [42607489](https://pubmed.ncbi.nlm.nih.gov/42607489/) | KEYNOTE-522 standard of care | Supports Finding 4 |
| [42360368](https://pubmed.ncbi.nlm.nih.gov/42360368/) | TILs predict pCR (70% vs 48%) | Supports Finding 4 |
| [36971103](https://pubmed.ncbi.nlm.nih.gov/36971103/) | Olaparib PFS HR 0.47 in TNBC | Supports Finding 5 |
| [29753961](https://pubmed.ncbi.nlm.nih.gov/29753961/) | PARP synthetic lethality; 12-mo mOS | Supports Findings 5–6 |
| [42320849](https://pubmed.ncbi.nlm.nih.gov/42320849/) | 36% higher Black mortality | Supports Finding 6 |
| [42499497](https://pubmed.ncbi.nlm.nih.gov/42499497/) | Visceral/brain tropism of rapid relapse | Supports Finding 6 |
| [37482851](https://pubmed.ncbi.nlm.nih.gov/37482851/) | Basal markers ↔ aggressive features | Supports Finding 7 |
| [39435793](https://pubmed.ncbi.nlm.nih.gov/39435793/) | CK19+Ki67+/E-cad loss = worst survival | Supports Finding 7 |
| [42166900](https://pubmed.ncbi.nlm.nih.gov/42166900/) | Risk-reducing surgery uptake | Supports Finding 8 |
| [31959092](https://pubmed.ncbi.nlm.nih.gov/31959092/) | Feline TNBC model | Supports Finding 9 |
| [35451346](https://pubmed.ncbi.nlm.nih.gov/35451346/) | Canine basal-like mammary dysplasia | Supports Finding 9 |
| [36612226](https://pubmed.ncbi.nlm.nih.gov/36612226/) | Bicalutamide/enzalutamide for LAR | Supports Finding 10 |
| [29940524](https://pubmed.ncbi.nlm.nih.gov/29940524/) | LAR clinical behavior | Supports Finding 10 |
| [30859564](https://pubmed.ncbi.nlm.nih.gov/30859564/) | PDX fidelity/heterogeneity | Supports Finding 11 |
| [40925466](https://pubmed.ncbi.nlm.nih.gov/40925466/) | BRCA1 hypermethylation/BRCAness | Supports Finding 12 |
| [41484250](https://pubmed.ncbi.nlm.nih.gov/41484250/) | Mutant p53 LOF+GOF | Supports Finding 13 |
| [33267874](https://pubmed.ncbi.nlm.nih.gov/33267874/) | p53LOH, CIN, centrosome amplification | Supports Finding 13 |
| [34083056](https://pubmed.ncbi.nlm.nih.gov/34083056/) | Glutamine addiction, CB-839 | Supports Finding 14 |
| [42373230](https://pubmed.ncbi.nlm.nih.gov/42373230/) | Glucose/glutamine metabolic states | Supports Finding 14 |

---

## Limitations and Knowledge Gaps

- **No primary dataset was analyzed:** This report is a literature/knowledge synthesis; no de novo statistical analysis of a patient cohort or omics dataset was performed. Effect sizes and quotes are drawn from published cohorts of varying size, geography, and quality (several are single-center or real-world retrospective studies).
- **Subtype instability:** The Lehmann TNBCtype-4 classification is refined but still evolving; immunomodulatory (IM) and mesenchymal stem-like (MSL) signals were reassigned to microenvironment rather than tumor-intrinsic biology, and boundaries between "basal-like" (PAM50) and "TNBC" (IHC) are imperfect (~partial overlap).
- **Model gaps:** Immunodeficient PDX/xenograft models underrepresent the immunomodulatory/TIL-driven biology that is central to modern immunotherapy — a major translational blind spot.
- **HRD quantification:** The exact prevalence and best clinical assay for HRD beyond germline *BRCA* (e.g., genomic scar scores, *BRCA1* methylation) remain incompletely standardized.
- **Disparities causation:** The relative contributions of ancestry-linked tumor biology versus structural/socioeconomic factors to racial outcome disparities are entangled and not fully resolved.
- **Metastatic prognosis:** Despite new agents, metastatic TNBC survival remains ~12 months; predictive biomarkers for immunotherapy (beyond PD-L1/TILs) and ADC resistance mechanisms are incompletely defined.

---

## Proposed Follow-up Experiments / Actions

1. **Quantitative HRD landscape:** Analyze a genomic dataset (e.g., TCGA-BRCA TNBC subset or a public cohort) to quantify the fraction of TNBC that is HRD-positive by combined germline *BRCA*, somatic *BRCA/PALB2/RAD51*, and *BRCA1* methylation, and correlate with genomic scar scores — filling the standardization gap.
2. **Subtype × therapy-response mapping:** Integrate TNBCtype-4 subtype calls with pCR and survival across neoadjuvant cohorts to formally test whether BL1 (immune-rich) predicts pembrolizumab benefit and LAR predicts AR-blockade benefit.
3. **Immune-competent modeling:** Prioritize syngeneic (4T1), humanized-mouse, or organoid-immune co-culture systems to study checkpoint/ADC combinations, addressing the PDX immunobiology gap.
4. **Metabolic–DNA-repair combination trials:** Preclinically test glutaminase inhibition (CB-839) or p53-reactivation (APR-246/PLK2 inhibition) combined with PARP inhibitors/platinum, exploiting the convergence of metabolic and genomic vulnerabilities.
5. **Equity intervention study:** Design a prospective analysis linking cascade genetic-testing access, MRI surveillance uptake, and stage-at-diagnosis in Black and young women to quantify how much of the mortality gap is modifiable through service delivery.
6. **Liquid-biopsy relapse detection:** Evaluate ctDNA (TP53/BRCA-informed) for early detection of rapid-relapse TNBC within the 24-month high-risk window.

---

*Report compiled from 14 confirmed findings across 65 reviewed papers over 5 iterations. Evidence source types span human clinical trials/cohorts, model organism (mouse, cat, dog), in vitro cell-line, and computational/omics studies, as annotated throughout.*


## Artifacts

- [OpenScientist final report](Triple_Negative_Breast_Cancer-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Triple_Negative_Breast_Cancer-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 57 |
| Resolved | 57 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 16 |
| Quoted claims found in source | 15 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 57 |
| On topic | 34 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:42373230` *(abstract only)*: "licens[es] chromatin engagement, DNA replication, and mitotic progression"
  - closest text in source: "Conversely, glucose alone acts as the executor, licensing chromatin engagement, DNA replication, and mitotic progression"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 11 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0060081` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **triple-negative breast cancer**
- `HP:0031416` (2 mentions) - the report calls it "Breast mass / palpable lump"; HP calls it **Abnormal nasal mucus secretion**
- `HP:0030075` (1 mention) - the report calls it "neoplasm of lung"; HP calls it **Ductal carcinoma in situ**
- `UBERON:0000310` (2 mentions) - the report calls it "Primary organ:** breast", "UBERON:** breast"; UBERON calls it **breast**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002716` (1 mention) - the report calls it "Lymph node metastasis"; HP calls it **Lymphadenopathy**, and lists "Lymph node hyperplasia" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0000310` - called "Primary organ:** breast", "UBERON:** breast"