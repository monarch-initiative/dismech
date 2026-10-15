---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T19:31:22.270598'
end_time: '2026-09-30T20:02:27.240649'
duration_seconds: 1864.97
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Platelet-type Bleeding Disorder 16
  mondo_id: MONDO:0008552
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
citation_count: 15
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 11
  quotes_valid: 10
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:40123272
  relevance_assessed: 16
  on_topic: 9
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 32
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 3
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0008552
    reported_labels:
    - MONDO
    ontology_label: platelet-type bleeding disorder 16
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Platelet-type_Bleeding_Disorder_16-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Platelet-type_Bleeding_Disorder_16-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Platelet-type Bleeding Disorder 16
- **MONDO ID:** MONDO:0008552 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Platelet-type Bleeding Disorder 16** covering all of the
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

# Platelet-type Bleeding Disorder 16 (BDPLT16): Comprehensive Disease Characteristics Report

**Disease:** Platelet-type Bleeding Disorder 16 (BDPLT16)
**Also known as:** ITGA2B/ITGB3-related macrothrombocytopenia; Glanzmann thrombasthenia-like syndrome (GTLS); autosomal dominant macrothrombocytopenia with αIIbβ3 gain-of-function
**OMIM:** #187800 · **MONDO:** MONDO:0008552 · **ICD-10:** D69.1 · **Category:** Mendelian (autosomal dominant)

---

## Summary

Platelet-type Bleeding Disorder 16 (BDPLT16) is a rare, autosomal dominant inherited platelet disorder defined at the molecular level by heterozygous **gain-of-function** variants in *ITGA2B* (encoding integrin αIIb/GPIIb) or *ITGB3* (encoding integrin β3/GPIIIa). These variants cluster in the **membrane-proximal (transmembrane and cytoplasmic) region** of the αIIbβ3 integrin and disrupt the conserved intracytoplasmic **salt bridge between αIIb-Arg995 and β3-Asp723**. Loss of this clasp releases the integrin from its resting conformation, producing a **constitutively active** αIIbβ3 receptor. This is the mechanistic inverse of classic Glanzmann thrombasthenia (GT), which is caused by recessive loss-of-function of the same genes.

Constitutive αIIbβ3 activation drives permanent "outside-in" signaling in megakaryocytes, which perturbs cytoskeletal (actin/tubulin) dynamics and produces **abnormal proplatelet formation**. The clinical consequence is a **macrothrombocytopenia** — large platelets present in reduced numbers — together with reduced αIIbβ3 surface expression (from receptor internalization), a **partial (not absent) platelet aggregation defect**, and lifelong, usually **mild-to-moderate mucocutaneous bleeding** (easy bruising, epistaxis, gum bleeding, menorrhagia). Enlarged and fused α-granules are seen ultrastructurally. Because the count is low and the platelets are large, patients are **frequently misdiagnosed as immune thrombocytopenia (ITP)** and treated ineffectively with corticosteroids/splenectomy.

BDPLT16 is genetically and mechanistically distinct from recessive GT; diagnosis rests on recognizing dominant inheritance, macrothrombocytopenia with *reduced* (not absent) αIIbβ3, a partial aggregation defect, and an activating membrane-proximal *ITGA2B/ITGB3* variant on next-generation sequencing. No disease-specific or curative therapy exists; management is supportive and extrapolated from inherited platelet function disorders — antifibrinolytics (tranexamic acid), recombinant activated factor VII (rFVIIa), platelet transfusion for major bleeds/surgery, and hormonal control of heavy menstrual bleeding. This report synthesizes the molecular pathogenesis, phenotype, genetics, diagnostics, prognosis, treatment, and model systems across all requested disease-characteristic domains.

---

## 1. Disease Information

**Overview.** BDPLT16 is a Mendelian inherited platelet disorder in which a dominant gain-of-function lesion in the fibrinogen receptor αIIbβ3 produces large, poorly functional platelets in reduced numbers, causing a lifelong mild-to-moderate bleeding tendency. It belongs to the broader family of **congenital macrothrombocytopenias** and is a recognized subset now termed **ITGA2B/ITGB3-related macrothrombocytopenia** ([PMID: 41503871](https://pubmed.ncbi.nlm.nih.gov/41503871/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | #187800 (Bleeding disorder, platelet-type, 16; BDPLT16) |
| MONDO | MONDO:0008552 |
| ICD-10 | D69.1 (Qualitative platelet defects) |
| Causal genes | *ITGA2B* (HGNC:6138; OMIM 607759; NCBI Gene 3674; Ensembl ENSG00000005961; UniProt P08514; 17q21.31) · *ITGB3* (HGNC:6156; OMIM 173470; NCBI Gene 3690; UniProt P05106; 17q21.32) |

**Synonyms / alternative names.** ITGA2B/ITGB3-related macrothrombocytopenia; Glanzmann thrombasthenia-like syndrome (GTLS); autosomal dominant macrothrombocytopenia with αIIbβ3 gain-of-function; αIIbβ3-related macrothrombocytopenia.

**Source of information.** Information is derived from **aggregated disease-level resources** (OMIM, MONDO) and from **primary clinical/genetic case series and pedigrees** of individual patients — not from population EHR datasets. The evidence base is a set of small multi-generational families reported worldwide (see Section 9).

---

## 2. Etiology

**Primary cause — genetic (monogenic, dominant, gain-of-function).** BDPLT16 is caused by heterozygous gain-of-function variants in *ITGA2B* or *ITGB3*. These are point mutations (and small in-frame deletions) concentrated in the membrane-proximal region of the integrin that destabilize the αIIb-R995/β3-D723 intracytoplasmic salt bridge, causing constitutive activation ([PMID: 29090484](https://pubmed.ncbi.nlm.nih.gov/29090484/); [PMID: 29380037](https://pubmed.ncbi.nlm.nih.gov/29380037/); [PMID: 33276370](https://pubmed.ncbi.nlm.nih.gov/33276370/)).

**Genetic risk factors.** The causal variants are themselves the disease determinant; there are no known separate susceptibility loci. Documented disease alleles include (non-exhaustive):
- *ITGB3* (β3): **p.Asp723His (D723H)**, **p.Thr720del (T720del)**, D749H, T746P, H748P, R760C, plus membrane-proximal missense/deletion variants (e.g., C560R, βTD_del p.647-686 in Glanzmann-like macrothrombocytopenia).
- *ITGA2B* (αIIb): **p.Arg995Trp (R995W)**, R995Q, **R1026W**, R1026Q, G1007V.

**Environmental / demographic risk factors.** As a monogenic dominant disorder, the disease is **not caused by environmental exposures**. Relevant non-genetic modifiers of *bleeding severity* (not disease causation) are standard hemostatic challenges: surgery, trauma, dental extraction, childbirth/postpartum, menstruation, and antiplatelet/anticoagulant drug use. Female sex confers additional gynecologic/obstetric bleeding burden (menorrhagia, postpartum hemorrhage). A **positive family history** is a hallmark given dominant transmission.

**Protective factors.** No specific genetic or environmental protective factors are established. General avoidance of antiplatelet agents (aspirin, NSAIDs) reduces bleeding risk. There is no evidence of a protective allele.

**Gene–environment interactions.** No formal GxE interaction has been characterized. Practically, the penetrant genetic lesion sets a fixed platelet phenotype whose clinical expression is *unmasked* by hemostatic stressors (surgery, trauma, menstruation, delivery).

---

## 3. Phenotypes

BDPLT16 phenotypes comprise **laboratory abnormalities** and **clinical bleeding signs/symptoms**. Bleeding is typically **mild-to-moderate**, lifelong, and mucocutaneous; severity is **variable** even within families.

| Phenotype | Type | Characteristics | Suggested HPO term |
|---|---|---|---|
| Thrombocytopenia | Lab abnormality | Congenital, lifelong, stable; reduced platelet count | HP:0001873 Thrombocytopenia |
| Large/giant platelets (macrothrombocytopenia) | Lab/morphologic | Enlarged round platelets on smear; increased anisotropy | HP:0040326 Increased mean platelet volume |
| Reduced αIIbβ3 surface expression | Lab abnormality | Low (not absent) GPIIb/IIIa by flow cytometry | HP:0011876 Abnormal platelet function |
| Impaired platelet aggregation | Lab abnormality | Reduced (not absent) response to ADP, collagen, TRAP-6; ristocetin normal | HP:0003540 Impaired platelet aggregation |
| Reduced ATP/dense-granule release | Lab abnormality | Low ATP release to physiologic agonists | HP:0011876 Abnormal platelet function |
| Enlarged/fused α-granules | Ultrastructural | Abnormal large α-granules, some giant/fused | — |
| Easy bruising / mucocutaneous bleeding | Clinical sign | Mild-moderate, episodic (provoked by trauma/surgery) | HP:0000978 Bruising susceptibility |
| Epistaxis | Clinical sign | Recurrent, mild-moderate | HP:0000421 Epistaxis |
| Gingival/gum bleeding | Clinical sign | Mucosal | HP:0000225 Gingival bleeding |
| Menorrhagia / heavy menstrual bleeding | Clinical sign | Prominent in affected women; may be chronic | HP:0000132 Abnormal menstruation (menorrhagia) |
| Prolonged bleeding after surgery/trauma | Clinical sign | Episodic, provoked | HP:0004846 Abnormal bleeding |

**Age of onset.** Congenital laboratory phenotype (thrombocytopenia/large platelets present from birth); bleeding symptoms emerge in **childhood** and persist lifelong. **Severity** is mild-to-moderate and **variable**; **progression** is stable (non-progressive), with bleeding **episodic** and provoked by hemostatic challenge.

**Frequency among affected individuals.** In the largest series (10 Portuguese GTLS families, 33 patients), the core lab tetrad — macrothrombocytopenia, low αIIbβ3 expression, impaired aggregation/ATP release, and low PAC-1 binding — was essentially universal, while clinical bleeding ranged from **absent to moderate** ([PMID: 33276370](https://pubmed.ncbi.nlm.nih.gov/33276370/)).

**Quality of life impact.** Generally modest given mild-moderate severity, but recurrent epistaxis and especially **menorrhagia** can meaningfully impair quality of life and cause iron-deficiency anemia; peri-operative and peri-partum periods carry the highest morbidity risk. No disease-specific EQ-5D/SF-36 data are available.

---

## 4. Genetic / Molecular Information

**Causal genes.** *ITGA2B* (αIIb; HGNC:6138; OMIM 607759; 17q21.31) and *ITGB3* (β3; HGNC:6156; OMIM 173470; 17q21.32). The two chains form the heterodimeric platelet fibrinogen receptor αIIbβ3 (GPIIb/IIIa, integrin αIIbβ3), expressed at ~60,000–80,000 copies per platelet in mouse and abundantly in human platelets ([PMID: 11154120](https://pubmed.ncbi.nlm.nih.gov/11154120/)).

**Pathogenic variants (representative).**

| Gene | Variant | Type | Effect |
|---|---|---|---|
| *ITGB3* | p.Asp723His (D723H) | Missense | Breaks αIIb-R995/β3-D723 salt bridge → constitutive activation |
| *ITGB3* | p.Thr720del (T720del) | In-frame deletion | Spontaneous αIIbβ3 activation |
| *ITGB3* | D749H, T746P, H748P, R760C | Missense | Membrane-proximal, activating |
| *ITGB3* | C560R (EGF-like domain) | Missense | Constitutive activation, differing surface expression |
| *ITGB3* | βTD_del (p.647-686) | In-frame deletion | Constitutive activation (β-tail domain) |
| *ITGA2B* | p.Arg995Trp/Gln (R995W/Q) | Missense | Breaks salt bridge → constitutive activation |
| *ITGA2B* | R1026W, R1026Q, G1007V | Missense | Membrane-proximal, activating |

**Variant classification.** ClinVar corroborates BDPLT16 alleles: *ITGB3* Asp723His and *ITGA2B* Arg995 (R995W/R995Q) records are present, and ~8 *ITGA2B* records are annotated to "macrothrombocytopenia" (Finding F008). The majority of *ITGA2B* (≈345) and *ITGB3* (≈266) pathogenic ClinVar entries reflect the **allelic recessive Glanzmann thrombasthenia**, not the rare dominant BDPLT16.

**Variant type/class.** Predominantly **missense**; also **small in-frame deletions** (T720del, βTD_del). All cluster in the membrane-proximal transmembrane/cytoplasmic interface.

**Allele frequency.** Disease alleles are **private/ultra-rare** and effectively **absent from gnomAD**, consistent with a highly penetrant dominant deleterious effect (Finding F008).

**Somatic vs germline.** **Germline**, heterozygous, dominantly inherited.

**Functional consequence.** **Gain-of-function** (constitutive integrin activation) — mechanistically opposite to the loss-of-function of classic GT. In-silico modeling shows mutated residues "directly modify the salt bridge linking the intra-cytoplasmic part of αIIb to β3" ([PMID: 29090484](https://pubmed.ncbi.nlm.nih.gov/29090484/)).

**Modifier genes / epigenetics / chromosomal abnormalities.** No specific modifier genes, epigenetic marks, or large-scale chromosomal abnormalities are established for BDPLT16. The lesion is a point mutation / small in-frame deletion, not a copy-number or structural variant.

---

## 5. Environmental Information

BDPLT16 is a **monogenic disorder with no environmental, lifestyle, or infectious etiology**. No toxins, radiation, occupational exposures, dietary factors, or pathogens cause or trigger the disease. Environmental factors are relevant only as **bleeding precipitants** (trauma, surgery, dental procedures, childbirth) and as **aggravators** via antiplatelet/anticoagulant drug exposure (aspirin, NSAIDs). Not applicable: infectious agents.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A heterozygous **gain-of-function variant** arises in *ITGA2B* (αIIb) or *ITGB3* (β3) in the membrane-proximal region → **disrupts the conserved αIIb-Arg995 ↔ β3-Asp723 intracytoplasmic salt bridge** (the "clasp" that holds the integrin in its resting/bent state). *(Demonstrated by in-silico + functional studies.)*
2. Loss of the salt-bridge clasp **releases the cytoplasmic/transmembrane restraint** → the integrin adopts an **extended, constitutively active conformation** → **spontaneous (agonist-independent) αIIbβ3 activation** with increased binding of activation-specific ligands (↑PAC-1 binding; adhesion to fibrinogen/VWF under shear). *(Demonstrated in CHO/293T transfectants and patient platelets.)*
3. Constitutive ligand binding triggers **permanent "outside-in" signaling** → **arrest of actin turnover at the polymerization stage** and disordered cytoskeletal (actin/tubulin) reorganization in megakaryocytes. *(Demonstrated.)*
4. Cytoskeletal perturbation **impairs proplatelet formation** → megakaryocytes generate **abnormal cytoplasmic extensions / asymmetric "barbell" proplatelets with fewer, larger tips**. *(Demonstrated in patient CD34+ MK cultures and cell models.)*
5. Abnormal proplatelet fragmentation **leads to incorrect platelet sizing and reduced platelet output** → **macrothrombocytopenia** (large platelets, low count). *(Demonstrated.)*
6. **Branch — receptor internalization:** constitutive activation promotes **αIIbβ3 internalization** → **reduced surface expression** of the receptor on circulating platelets. *(Demonstrated.)*
7. **Branch — granule abnormality:** disordered biogenesis yields **enlarged/fused α-granules** (some giant). *(Observed.)*
8. Reduced receptor density + dysfunctional granule release + abnormal cytoskeleton → **partial platelet aggregation and secretion defect** (reduced but not absent responses to ADP, collagen, TRAP-6) → **mild-to-moderate mucocutaneous bleeding** when hemostasis is challenged. *(Demonstrated clinically.)*

```
GOF variant (ITGA2B/ITGB3, membrane-proximal)
        │
        ▼
Disrupts αIIb-R995 / β3-D723 salt bridge (the "clasp")
        │
        ▼
Constitutive αIIbβ3 activation (↑PAC-1, ligand binding)
        ├───────────────► Receptor internalization ─► ↓ surface αIIbβ3
        │
        ▼
Permanent outside-in signaling ─► actin turnover arrested
        │
        ▼
Abnormal proplatelet formation (asymmetric, few large tips)
        │                         └──► enlarged/fused α-granules
        ▼
Large platelets + low count = MACROTHROMBOCYTOPENIA
        │
        ▼
Partial aggregation/secretion defect ─► mild-moderate mucocutaneous bleeding
```

### Detail by category

- **Molecular pathways / biochemical abnormality.** The defect is **integrin bidirectional (inside-out/outside-in) signaling**. The proximate biochemical lesion is loss of the electrostatic salt bridge that maintains the low-affinity resting state; the downstream signaling engages Rap1/talin-associated outside-in activation cascades and actin dynamics ([PMID: 29380037](https://pubmed.ncbi.nlm.nih.gov/29380037/); [PMID: 26452979](https://pubmed.ncbi.nlm.nih.gov/26452979/)).
- **Protein dysfunction.** **Gain-of-function** conformational change: the mutant integrin is trapped in an active/extended state rather than misfolded or degraded. This distinguishes it from GT loss-of-function (absent/nonfunctional receptor).
- **Cellular processes.** Dysregulated **cytoskeletal reorganization** (actin polymerization/turnover, tubulin-dependent protrusions), **abnormal proplatelet formation**, and **receptor endocytosis/internalization**.
- **Cell types involved.** **Megakaryocytes** (CL:0000556) as the site of defective platelet production; **platelets/thrombocytes** (CL:0000233) as the dysfunctional end product.
- **Suggested GO terms.** GO:0007229 integrin-mediated signaling pathway; GO:0033628 regulation of cell adhesion mediated by integrin; GO:0030168 platelet activation; GO:0030220 platelet formation; GO:0007010 cytoskeleton organization; GO:0006897 endocytosis. Cellular component: GO:0009986 cell surface, GO:0031093 platelet alpha granule, GO:0015629 actin cytoskeleton.
- **Immune / metabolic / infectious involvement.** None intrinsic. (Misdiagnosis as *immune* thrombocytopenia is a clinical, not mechanistic, issue.)

**Instructive natural experiment (sitosterolemia).** In a murine sitosterolemia model, plant-sterol accumulation in the platelet membrane produced **constitutive fibrinogen binding to αIIbβ3, receptor internalization, and macrothrombocytopenia** — phenocopying, via a non-genetic route, the same "constitutively active αIIbβ3 → macrothrombocytopenia" logic and reinforcing causality ([PMID: 23926302](https://pubmed.ncbi.nlm.nih.gov/23926302/)).

---

## 7. Anatomical Structures Affected

- **Organ/system level.** Primary involvement is the **hematopoietic system / blood** (UBERON:0000178 blood) and **bone marrow** (UBERON:0002371) where megakaryopoiesis occurs. The **mucocutaneous vasculature** (skin, nasal mucosa, gingiva, gastrointestinal and genitourinary mucosa) is the site of bleeding manifestations. Secondary involvement: **endometrium/uterus** (menorrhagia) and potential iron-deficiency anemia affecting systemic function.
- **Tissue/cell level.** **Megakaryocytes** (CL:0000556) in bone marrow; **platelets/thrombocytes** (CL:0000233) in circulation. No solid-organ parenchymal tissue is primarily targeted.
- **Subcellular level.** **Plasma membrane / cell surface** (integrin localization; GO:0005886), **platelet α-granules** (GO:0031093; enlarged/fused), and the **actin cytoskeleton** (GO:0015629).
- **Localization / lateralization.** Systemic (blood-borne); bleeding sites are **not lateralized** — diffuse mucocutaneous. No focal or asymmetric anatomic lesion.

---

## 8. Temporal Development

- **Onset.** **Congenital** laboratory phenotype (thrombocytopenia and large platelets from birth); clinical bleeding typically recognized in **childhood**. Onset pattern is **chronic/insidious** rather than acute.
- **Progression.** **Stable / non-progressive**; the platelet count and morphology remain relatively constant over life. Bleeding is **episodic**, provoked by hemostatic challenges (surgery, trauma, menstruation, delivery).
- **Disease course / duration.** **Chronic, lifelong.** There is no staging system and no natural tendency to remission or worsening.
- **Critical periods.** Windows of heightened vulnerability are **surgical/dental procedures, trauma, menarche/menstruation, pregnancy and the peripartum period** — the key opportunities for prophylactic hemostatic intervention.

---

## 9. Inheritance and Population

- **Inheritance pattern.** **Autosomal dominant** (heterozygous gain-of-function). Contrast with recessive classic GT.
- **Epidemiology.** No formal prevalence/incidence figures exist; BDPLT16 is **ultra-rare**, reported as a handful of families worldwide. Known pedigrees include the original *ITGB3* D723H family (5 affected over 3 generations; [PMID: 18065693](https://pubmed.ncbi.nlm.nih.gov/18065693/)), Japanese T720del and related families ([PMID: 29380037](https://pubmed.ncbi.nlm.nih.gov/29380037/)), French salt-bridge families ([PMID: 29090484](https://pubmed.ncbi.nlm.nih.gov/29090484/)), and a Portuguese cohort of 10 families/33 patients ([PMID: 33276370](https://pubmed.ncbi.nlm.nih.gov/33276370/)).
- **Penetrance / expressivity.** Cosegregation is strong (the laboratory phenotype tracks with the variant across generations), implying **high penetrance for the lab phenotype**; **bleeding severity is variably expressed** (absent-to-moderate) even among carriers of the same allele.
- **Anticipation / mosaicism / consanguinity / founder effects.** No genetic anticipation (not a repeat-expansion disorder). No consanguinity required (dominant). The Portuguese cluster of 10 families may reflect ascertainment and/or shared alleles, but no formal founder haplotype has been established. Germline mosaicism not specifically documented.
- **Carrier frequency.** Not applicable in the recessive sense; disease alleles are private/ultra-rare and essentially absent from gnomAD (Finding F008).
- **Population demographics.** No strong ethnic predilection; cases reported across European (French, Portuguese, Italian) and Asian (Japanese) populations. **Sex ratio** for the genetic trait is ~1:1 (autosomal); affected **women carry additional gynecologic/obstetric bleeding burden**. Age distribution spans all ages given lifelong congenital nature.

---

## 10. Diagnostics

**Laboratory tests.**
- **CBC with peripheral blood smear:** thrombocytopenia with **large/giant platelets**; increased mean platelet volume and platelet anisotropy. Automated counters may **undercount** large platelets.
- **Flow cytometry:** **reduced (not absent) αIIbβ3/GPIIb-IIIa surface expression**; **reduced PAC-1 binding** upon stimulation (TRAP-6, ADP) — reflecting low activation-inducible binding sites.
- **Light transmission aggregometry (LTA):** **reduced but not absent** aggregation to ADP and collagen; **normal ristocetin-induced agglutination** (distinguishing from Bernard-Soulier/VWD); reduced ATP/dense-granule release.
- **Electron microscopy (specialized):** enlarged, sometimes fused α-granules; abnormal platelet morphology.

**Biomarkers.** The defining "biomarker" is the **combination** of macrothrombocytopenia + reduced (not absent) αIIbβ3 + partial aggregation defect + activating membrane-proximal *ITGA2B/ITGB3* variant.

**Genetic testing (definitive).**
- **Recommended approach:** **NGS-based inherited platelet disorder gene panels** covering *ITGA2B*, *ITGB3*, and the broader macrothrombocytopenia genes; **WES/WGS** are useful when panels are non-diagnostic. Confirm candidate variants by **Sanger sequencing** and test **family segregation**.
- **Single-gene testing** of *ITGA2B*/*ITGB3* is appropriate when phenotype is strongly suggestive.
- CMA/karyotype/FISH/mtDNA/repeat-expansion testing are **not applicable** (point-mutation disorder).

**Imaging / electrophysiology / biopsy.** Not diagnostic; imaging is used only to evaluate bleeding complications. Bone marrow examination is typically normal (normal megakaryocyte numbers), useful mainly to exclude other causes.

**Clinical criteria & differential diagnosis.** No formal consensus criteria; diagnosis is integrative (phenotype + genetics). **Differential diagnosis** of dominant macrothrombocytopenia with platelet dysfunction includes:

| Condition | Inheritance | Key distinguishing feature |
|---|---|---|
| **BDPLT16 (this disease)** | AD (GOF) | Reduced (not absent) αIIbβ3; partial aggregation defect; activating membrane-proximal *ITGA2B/ITGB3* variant |
| Classic Glanzmann thrombasthenia | AR (LOF) | Absent αIIbβ3/aggregation; **normal** count & size |
| Bernard-Soulier syndrome | AR | GPIb-IX-V defect; abnormal ristocetin agglutination |
| MYH9-related disorders (May-Hegglin) | AD | Leukocyte Döhle-like inclusions; *MYH9* variant |
| von Willebrand disease | AD/AR | VWF defect; abnormal ristocetin; corrects with VWF |
| Immune thrombocytopenia (ITP) | Acquired | No family history; normal platelet size; steroid-responsive |

Congenital macrothrombocytopenias "share common clinical and laboratory features... and patients are often misdiagnosed with and treated for idiopathic thrombocytopenic purpura" ([PMID: 16169642](https://pubmed.ncbi.nlm.nih.gov/16169642/)).

**Screening.** No population/newborn screening. **Cascade genetic testing** of at-risk relatives is appropriate once a familial variant is identified; prenatal/preimplantation testing is technically feasible but rarely indicated given the mild phenotype.

---

## 11. Outcome / Prognosis

- **Survival / life expectancy.** **Normal life expectancy**; BDPLT16 is not associated with increased mortality in the absence of catastrophic bleeding. No disease-specific mortality data.
- **Morbidity.** Driven by bleeding: recurrent epistaxis, easy bruising, **menorrhagia** (with risk of **iron-deficiency anemia**), and peri-operative/peri-partum hemorrhage. Serious spontaneous bleeding (e.g., intracranial) is rare in mild-moderate disease, though documented in the severe allelic condition GT.
- **Disease course.** Chronic and stable; complications are episodic and largely preventable with appropriate hemostatic management around challenges.
- **Prognostic factors.** Bleeding phenotype severity, sex (gynecologic burden), exposure to antiplatelet drugs, and the nature of hemostatic challenges. No validated molecular prognostic biomarker; there is a broad genotype–phenotype trend (all activating salt-bridge variants → macrothrombocytopenia), but bleeding severity is variably expressed.
- **Quality-of-life measures.** No disease-specific EQ-5D/SF-36/PROMIS data; QoL is generally good but reduced in those with significant menorrhagia.

---

## 12. Treatment

**Overarching principle.** There is **no BDPLT16-specific or curative therapy**. Management is **supportive/on-demand**, extrapolated from inherited platelet function disorders and the allelic condition Glanzmann thrombasthenia.

**Pharmacotherapy and hemostatic agents.**

| Intervention | Role | NCIT suggestion |
|---|---|---|
| **Tranexamic acid / antifibrinolytics** | First-line for mucosal bleeding, menorrhagia, dental/minor surgery | NCIT:C739 Tranexamic Acid |
| **Recombinant activated factor VII (rFVIIa)** | Major bleeds/surgery; also reduces risk of platelet alloimmunization | NCIT:C1836 Recombinant Factor VIIa |
| **Platelet transfusion** | Severe/life-threatening bleeding or major surgery; use judiciously (alloimmunization risk) | NCIT:C15328 Platelet Transfusion |
| **Hormonal therapy** (combined OCP, progestins, LNG-IUS) | Control of heavy menstrual bleeding | NCIT:C548 Hormone Therapy |
| **Desmopressin (DDAVP)** | Considered in mild platelet disorders; variable benefit | NCIT:C29179 Desmopressin |
| **Iron supplementation** | Treat/prevent iron-deficiency anemia from chronic blood loss | NCIT:C1381 Iron Supplement |
| **Local measures** | Pressure, nasal packing, topical agents for epistaxis | — |

Evidence: in GT, "bleeding control was achieved through the use of antifibrinolytic agents and recombinant factor VIIa, which also reduces the risk of platelet alloimmunization" ([PMID: 41778036](https://pubmed.ncbi.nlm.nih.gov/41778036/)). In women, "management of chronic HMB required a combination therapy including antifibrinolytics (tranexamic acid [TXA]), hormonal therapies, and recombinant factor VIIa (rFVIIa)" ([PMID: 40123272](https://pubmed.ncbi.nlm.nih.gov/40123272/)). Local measures, desmopressin, and antifibrinolytics are first-line for mild inherited platelet disorders ([PMID: 23269640](https://pubmed.ncbi.nlm.nih.gov/23269640/)).

**Advanced / experimental therapeutics.** No approved gene therapy, cell therapy, RNA-based, targeted, or immunotherapy for BDPLT16. Caution with anticoagulation — provoked thrombosis can occur in αIIbβ3 disorders and carries a narrow therapeutic window ([PMID: 41591555](https://pubmed.ncbi.nlm.nih.gov/41591555/), reported in GT).

**Pharmacogenomics.** Avoid antiplatelet drugs (aspirin, NSAIDs, P2Y12 inhibitors). No BDPLT16-specific pharmacogenomic guidance.

**Treatment strategy.** Individualized, challenge-based prophylaxis: pre-procedural antifibrinolytics ± rFVIIa ± platelets; peri-partum planning in a hemophilia/bleeding-disorder center; proactive management of menorrhagia and iron status.

---

## 13. Prevention

- **Primary prevention.** Not possible (genetic). Preventing *bleeding events*: avoid antiplatelet/anticoagulant drugs, use careful surgical/dental planning with prophylactic hemostatic cover.
- **Secondary prevention.** Early diagnosis (correctly distinguishing from ITP to avoid unnecessary steroids/splenectomy), **cascade genetic testing** of relatives, and iron-deficiency screening in menorrhagic patients.
- **Tertiary prevention.** Prevent complications: peri-operative/peri-partum hemostatic protocols, minimize platelet transfusions to reduce **alloimmunization** (favor rFVIIa where possible), treat anemia.
- **Genetic counseling.** Autosomal dominant → **50% transmission risk** to offspring; counsel on variable bleeding expressivity; offer family-cascade testing; prenatal/PGT feasible but seldom pursued given mild phenotype.
- **Immunization / public health / environmental interventions.** Not applicable beyond general bleeding-risk counseling.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs.** Mouse orthologs *Itga2b* (NCBI Gene 16399) and *Itgb3* (NCBI Gene 16416). Murine αIIbβ3 is functionally homologous to human, expressed at ~60,000–80,000 copies/platelet, with conserved EDTA-dissociation and activation biology ([PMID: 11154120](https://pubmed.ncbi.nlm.nih.gov/11154120/)).
- **Natural disease in other species.** No well-characterized **naturally occurring, dominant gain-of-function** αIIbβ3 macrothrombocytopenia has been catalogued in companion animals for BDPLT16 specifically; naturally occurring *Glanzmann thrombasthenia* (loss-of-function) is documented in dogs and horses (OMIA), which is the allelic recessive disease rather than BDPLT16.
- **Comparative biology.** The αIIb-R995/β3-D723 salt bridge and integrin activation machinery are evolutionarily conserved, so the mechanistic principle (salt-bridge disruption → constitutive activation) is expected to be conserved across mammals.
- **Zoonotic potential.** None (non-transmissible genetic disorder).

---

## 15. Model Organisms

**In vitro / cellular models (primary evidence base for BDPLT16).**
- **Transfected cell lines** (CHO, HEK293/293T) expressing mutant αIIbβ3 (β3-D723H/H723, β3-βTD_del p.647-686, β3-C560R, β3-T720del) reproduce **constitutive activation, increased PAC-1 binding, adhesion to fibrinogen/VWF under shear**, and formation of **abnormal proplatelet-like cytoplasmic extensions** not seen with wild-type ([PMID: 18065693](https://pubmed.ncbi.nlm.nih.gov/18065693/); [PMID: 25806962](https://pubmed.ncbi.nlm.nih.gov/25806962/); [PMID: 29380037](https://pubmed.ncbi.nlm.nih.gov/29380037/); [PMID: 26452979](https://pubmed.ncbi.nlm.nih.gov/26452979/)).
- **Patient-derived CD34+ stem-cell megakaryocyte cultures** confirm **abnormal proplatelet formation** in the propositus, directly linking the variant to the production defect ([PMID: 18065693](https://pubmed.ncbi.nlm.nih.gov/18065693/)).

**Mouse models.**
- The **β3-integrin knockout (*Itgb3⁻/⁻*)** mouse models **loss-of-function Glanzmann thrombasthenia**, NOT gain-of-function BDPLT16: "The mice are viable and fertile, and show all the cardinal features of GT (defects in platelet aggregation and clot retraction, prolonged bleeding times, and cutaneous and gastrointestinal bleeding)," plus placental defects and reduced survival ([PMID: 9916135](https://pubmed.ncbi.nlm.nih.gov/9916135/)).
- **Sitosterolemia mouse (*Abcg5/Abcg8⁻/⁻*)** provides a **phenocopy of the mechanism** — sterol-induced constitutive αIIbβ3 activation, internalization, and macrothrombocytopenia — even though the genetic cause differs ([PMID: 23926302](https://pubmed.ncbi.nlm.nih.gov/23926302/)).

**Phenotype recapitulation & limitations.** No published knock-in mouse carrying a human BDPLT16 activating salt-bridge variant is established; thus the dominant gain-of-function macrothrombocytopenia is **best modeled in vitro and in patient megakaryocytes**, while mouse knockouts capture only the allelic loss-of-function disease. A conditional/knock-in *Itgb3* D723H (or *Itga2b* R995W) mouse is an obvious gap.

---

## Mechanistic Model / Interpretation

BDPLT16 is best understood as a **"stuck-on" integrin disorder**. The αIIbβ3 fibrinogen receptor normally rests in a bent, low-affinity conformation held by an intracellular clasp — the **αIIb-R995 ↔ β3-D723 salt bridge**. BDPLT16 variants **break this clasp**, so the receptor is **constitutively active** even without agonist. Paradoxically, this gain-of-function produces **bleeding**, because (a) chronic activation triggers **receptor internalization**, lowering surface density; and (b) permanent **outside-in signaling** freezes the megakaryocyte cytoskeleton, **garbling proplatelet formation** so platelets emerge **too large and too few** with impaired secretion. The result is a **macrothrombocytopenia with a partial functional defect** — the mirror image of Glanzmann thrombasthenia, where the same receptor is simply **absent/nonfunctional** and platelet number/size are normal.

This unifying logic explains every observed feature: dominant inheritance (a single active allele poisons proplatelet formation), reduced-not-absent αIIbβ3 (internalization vs. deletion), partial-not-absent aggregation, large fused α-granules, and mild-to-moderate bleeding. The sitosterolemia phenocopy independently validates the causal step "constitutive αIIbβ3 activation → internalization → macrothrombocytopenia."

**BDPLT16 vs. classic Glanzmann thrombasthenia (allelic contrast).**

| Feature | BDPLT16 | Classic Glanzmann thrombasthenia |
|---|---|---|
| Molecular effect | Gain-of-function (constitutive activation) | Loss-of-function (absent/defective receptor) |
| Inheritance | Autosomal dominant | Autosomal recessive |
| αIIbβ3 surface level | Reduced (not absent) | Absent/markedly reduced |
| Platelet count | Low (thrombocytopenia) | Normal |
| Platelet size | Large (macrothrombocytes) | Normal |
| Aggregation defect | Partial | Absent/severe |
| Variant location | Membrane-proximal TM/cytoplasmic | Throughout gene |
| Bleeding severity | Mild-moderate | Moderate-severe |

---

## Evidence Base

| PMID | Contribution | Supports |
|---|---|---|
| [29090484](https://pubmed.ncbi.nlm.nih.gov/29090484/) | Salt-bridge disruption (R995W, D723H); enlarged α-granules; mild-moderate phenotype | F001, F003 |
| [29380037](https://pubmed.ncbi.nlm.nih.gov/29380037/) | β3 T720del; membrane-proximal clustering; constitutive activation | F001, F003 |
| [33276370](https://pubmed.ncbi.nlm.nih.gov/33276370/) | 10 families/33 patients; 7 variants; defines core clinical/lab phenotype | F001, F003 |
| [26452979](https://pubmed.ncbi.nlm.nih.gov/26452979/) | Cytoskeletal mechanism: outside-in signaling arrests actin turnover; reduced surface expression | F001, F002 |
| [18065693](https://pubmed.ncbi.nlm.nih.gov/18065693/) | Original D723H pedigree; PAC-1↑; CHO model; patient MK abnormal proplatelets | F002, F004 |
| [25806962](https://pubmed.ncbi.nlm.nih.gov/25806962/) | βTD_del and C560R cause abnormal cytoplasmic extensions (proplatelet defect) | F002, F004 |
| [23926302](https://pubmed.ncbi.nlm.nih.gov/23926302/) | Sitosterolemia: sterol-induced constitutive αIIbβ3 activation → macrothrombocytopenia (mechanism phenocopy) | F002 |
| [9916135](https://pubmed.ncbi.nlm.nih.gov/9916135/) | β3-null mouse = loss-of-function GT model (not BDPLT16) | F004 |
| [11154120](https://pubmed.ncbi.nlm.nih.gov/11154120/) | Murine αIIbβ3 structure/function homology | F004 |
| [16169642](https://pubmed.ncbi.nlm.nih.gov/16169642/) | Congenital macrothrombocytopenias misdiagnosed as ITP | F005 |
| [34400424](https://pubmed.ncbi.nlm.nih.gov/34400424/) | Differential diagnosis framework (BSS, MYH9, GT, VWD) | F005 |
| [41778036](https://pubmed.ncbi.nlm.nih.gov/41778036/) | Antifibrinolytics + rFVIIa hemostatic management | F006 |
| [40123272](https://pubmed.ncbi.nlm.nih.gov/40123272/) | Menorrhagia management (TXA, hormonal, rFVIIa) | F006 |
| [23269640](https://pubmed.ncbi.nlm.nih.gov/23269640/) | First-line local measures/DDAVP/antifibrinolytics in mild platelet disorders | F006 |
| [41503871](https://pubmed.ncbi.nlm.nih.gov/41503871/) | Review defining ITGA2B/ITGB3-related macrothrombocytopenia as GOF subset | F001 |

**Verbatim supporting quotes.**
- "In silico analysis shows how the two mutated amino acids directly modify the salt bridge linking the intra-cytoplasmic part of αIIb to β3 of the integrin αIIbβ3." — [PMID: 29090484](https://pubmed.ncbi.nlm.nih.gov/29090484/)
- "Reported mutations were highly clustered at the membrane proximal region of αIIbβ3, which affected the critical interaction between αIIb R995 and β3 D723, resulting in a constitutionally active form of the αIIbβ3 complex." — [PMID: 29380037](https://pubmed.ncbi.nlm.nih.gov/29380037/)
- "the constitutive activation of the alphaIIbbeta3-H723 receptor causes abnormal proplatelet formation, leading to incorrect sizing of platelets and the thrombocytopenia observed in the pedigree." — [PMID: 18065693](https://pubmed.ncbi.nlm.nih.gov/18065693/)
- "permanent triggering of αIIbβ3-mediated outside-in signaling causes an impairment of cytoskeletal reorganization arresting actin turnover at the stage of polymerization." — [PMID: 26452979](https://pubmed.ncbi.nlm.nih.gov/26452979/)
- "Patients had absent to moderate bleeding, macrothrombocytopenia, low αIIbβ3 expression, impaired platelet aggregation/ATP release to physiological agonists and low expression of activation-induced binding sites on αIIbβ3 (PAC-1)." — [PMID: 33276370](https://pubmed.ncbi.nlm.nih.gov/33276370/)
- "Many of these disorders share common clinical and laboratory features, making accurate diagnosis difficult and patients are often misdiagnosed with and treated for idiopathic thrombocytopenic purpura." — [PMID: 16169642](https://pubmed.ncbi.nlm.nih.gov/16169642/)
- "Bleeding control was achieved through the use of antifibrinolytic agents and recombinant factor VIIa, which also reduces the risk of platelet alloimmunization." — [PMID: 41778036](https://pubmed.ncbi.nlm.nih.gov/41778036/)

---

## Limitations and Knowledge Gaps

1. **No formal epidemiology.** Prevalence/incidence are unknown; evidence is a handful of families. Penetrance and expressivity estimates are qualitative.
2. **No in vivo gain-of-function model.** No knock-in mouse (e.g., *Itgb3* D723H or *Itga2b* R995W) has been established; mechanism relies on in vitro transfectants and patient megakaryocytes. Mouse *Itgb3⁻/⁻* models only the allelic loss-of-function GT.
3. **Mechanistic exceptions.** Recent reports of **non-activating *ITGB3* variants** causing macrothrombocytopenia challenge the uniform gain-of-function model ([PMID: 41503871](https://pubmed.ncbi.nlm.nih.gov/41503871/)), indicating additional/alternative mechanisms remain to be defined.
4. **Treatment evidence is extrapolated**, not BDPLT16-specific — drawn from GT and general inherited platelet disorders; no trials in BDPLT16.
5. **No QoL, natural-history, or prognostic-biomarker data** specific to BDPLT16.
6. **Genotype–phenotype correlation** for bleeding severity is weak; modifier genes are unidentified.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a knock-in mouse** (*Itgb3* p.D723H or *Itga2b* p.R995W) or iPSC-derived megakaryocyte lines to model dominant gain-of-function BDPLT16 in vivo and quantify proplatelet defects.
2. **Systematic genotype–phenotype registry** across reported families to estimate penetrance, expressivity, and bleeding-severity predictors.
3. **Mechanistic dissection of non-activating *ITGB3* macrothrombocytopenia variants** to determine whether a distinct (activation-independent) pathway contributes.
4. **Single-cell transcriptomics/proteomics of patient megakaryocytes** to map the cytoskeletal and granule-biogenesis programs perturbed by constitutive αIIbβ3 signaling (GO:0030220 platelet formation).
5. **Prospective evaluation of hemostatic strategies** (antifibrinolytics ± rFVIIa vs. platelet transfusion) to build BDPLT16-specific, alloimmunization-sparing protocols.
6. **ClinVar/ACMG reclassification effort** to curate BDPLT16 alleles distinctly from recessive GT alleles, improving diagnostic reporting.

---

*Report compiled from 8 confirmed findings and 28 reviewed papers across 5 investigation iterations. Evidence types: human clinical pedigrees/case series, in vitro heterologous-cell and patient-megakaryocyte studies, and mouse models. Ontology suggestions (HPO, GO, CL, UBERON, NCIT) are provided throughout for knowledge-base population.*


## Artifacts

- [OpenScientist final report](Platelet-type_Bleeding_Disorder_16-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Platelet-type_Bleeding_Disorder_16-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 11 |
| Quoted claims found in source | 10 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 16 |
| On topic | 9 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:40123272` *(abstract only)*: "management of chronic HMB required a combination therapy including antifibrinolytics (tranexamic acid [TXA]), hormonal therapies, and recombinant factor VIIa (rFVIIa)"
  - closest text in source: "management of chronic HMB required a combination therapy including antifibrinolytics (tranexamic acid [TXA]), hormonal therapies, and recombinant factor VIIa (rFVIIa)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 5 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008552` (2 mentions) - the report calls it "MONDO"; MONDO calls it **platelet-type bleeding disorder 16**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000233` (2 mentions) - the report calls it "platelets/thrombocytes"; CL calls it **platelet**, and lists "anucleate thrombocyte" among its other names
