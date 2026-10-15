---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-06T19:11:11.300418'
end_time: '2026-09-06T19:28:02.388705'
duration_seconds: 1011.09
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: NAD(P)HX Dehydratase Deficiency
  mondo_id: MONDO:0034121
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
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 15
  on_topic: 14
  validator_version: 0.2.1
term_validation:
  total_terms: 44
  verified: 42
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 10
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0034121
    reported_labels:
    - MONDO
    ontology_label: NAD(P)HX dehydratase deficiency
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: NAD_P_HX_Dehydratase_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: NAD_P_HX_Dehydratase_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** NAD(P)HX Dehydratase Deficiency
- **MONDO ID:** MONDO:0034121 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **NAD(P)HX Dehydratase Deficiency** covering all of the
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

# NAD(P)HX Dehydratase (NAXD) Deficiency — Comprehensive Disease Characteristics Report

**Disease:** NAD(P)HX Dehydratase Deficiency (PEBEL2)
**MONDO ID:** MONDO:0034121 · **OMIM (phenotype):** #618321 · **Gene:** *NAXD* (HGNC:25576)
**Category:** Mendelian (autosomal recessive inborn error of metabolite repair)

---

## Summary

NAD(P)HX dehydratase (NAXD) deficiency — clinically designated **PEBEL2** (Progressive Encephalopathy with Brain Edema and/or Leukoencephalopathy, type 2; OMIM #618321) — is an ultra-rare, autosomal-recessive **inborn error of metabolite repair**. It is caused by biallelic loss-of-function variants in *NAXD*, the gene encoding the ATP-dependent NAD(P)HX dehydratase (EC 4.2.1.93). Together with its partner enzyme NAD(P)HX epimerase (NAXE; the sister disorder PEBEL1), NAXD constitutes the intracellular **NAD(P)HX repair system**, which converts the toxic, non-functional hydrated forms of the redox cofactors NADH and NADPH (collectively NAD(P)HX) back to usable NAD(P)H. When NAXD is deficient, S-NADHX, R-NADHX and cyclic-NADHX accumulate and functional NAD(P)H is depleted, producing a cellular energy/redox crisis ([PMID: 30576410](https://pubmed.ncbi.nlm.nih.gov/30576410/); [PMID: 34161859](https://pubmed.ncbi.nlm.nih.gov/34161859/)).

The defining clinical feature is a **gene–environment interaction**: the enzymopathy is often silent until a metabolic stressor — most commonly **fever or infection**, but also immunization, or physical trauma — sharply increases the non-enzymatic hydration of NAD(P)H and can denature thermolabile mutant enzyme. This precipitates acute, frequently fatal **neurometabolic decompensation**: rapidly progressive encephalopathy with brain and cerebellar edema and/or leukoencephalopathy, seizures, loss of developmental milestones, elevated CSF/serum lactate, characteristic **flexural necrotic skin lesions**, and — particularly for variants restricted to the mitochondrial isoform — **cardiomyopathy** and myopathy. Reported mortality across the combined NAXD/NAXE literature is approximately **78%**, with survivors experiencing neurological sequelae ([PMID: 39887790](https://pubmed.ncbi.nlm.nih.gov/39887790/)).

Critically, the disorder is at least partly **treatable**: niacin/nicotinamide (vitamin B3), which feeds NAD *de novo* / salvage synthesis and replenishes the depleted cofactor pool, improves skin lesions and survival in reported patients, providing a rational metabolic bypass therapy alongside aggressive control of febrile triggers ([PMID: 39887790](https://pubmed.ncbi.nlm.nih.gov/39887790/); [PMID: 27616477](https://pubmed.ncbi.nlm.nih.gov/27616477/); [PMID: 38974613](https://pubmed.ncbi.nlm.nih.gov/38974613/)). This report synthesizes 9 confirmed findings across 18 papers into a complete disease knowledge-base entry.

> **Evidence-source note.** This is an ultra-rare disease first defined in 2019; knowledge is derived almost entirely from **aggregated case reports/series and functional studies** (human clinical, patient fibroblasts/iPSCs, HAP1 knockouts, zebrafish, recombinant-enzyme biochemistry), not from population EHR or registry data. Fewer than ~20 genetically confirmed NAXD patients have been published. Where a claim rests on the sister disorder NAXE (PEBEL1) or on model systems, this is stated explicitly.

---

## 1. Disease Information

**Overview.** NAXD deficiency is a rare metabolite-repair disorder. NAD(P)HX dehydratase is a highly conserved enzyme essential for intracellular repair of the damaged/hydrated redox cofactor NAD(P)HX. As stated in the founding case series: *"The highly conserved enzyme NAD(P)HX dehydratase (NAXD) is essential for intracellular repair of NAD(P)HX"* ([PMID: 30576410](https://pubmed.ncbi.nlm.nih.gov/30576410/)). Loss of the enzyme produces a fever-triggered neurodegenerative and multisystem disease.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| Disease name | NAD(P)HX Dehydratase Deficiency / PEBEL2 |
| MONDO | MONDO:0034121 |
| OMIM (phenotype) | #618321 (Encephalopathy, progressive, early-onset, with brain edema and/or leukoencephalopathy, 2) |
| OMIM (gene) | 615910 |
| Gene symbol | *NAXD* (HGNC:25576) |
| NCBI Gene | 55739 |
| Ensembl | ENSG00000213995 |
| UniProt | Q8IW45 |
| Enzyme | EC 4.2.1.93 (ATP-dependent, ADP-forming NAD(P)HX dehydratase) |
| Locus | 13q34 (GRCh38 chr13:110,615,505–110,643,086, + strand) |
| Aliases | CARKD, LP3298 |

The disease designation and OMIM ID are confirmed: *"Encephalopathy, progressive, early-onset, with brain edema and/or leukoencephalopathy, 2 (PEBEL2; MIM# 618321), caused by biallelic pathogenic variants in the NAD(P)HX dehydratase (NAXD) is a rare metabolite repair disorder"* ([PMID: 34161859](https://pubmed.ncbi.nlm.nih.gov/34161859/)).

**Synonyms / alternative names:** PEBEL2; NAXD deficiency; NAD(P)HX dehydratase deficiency; carbohydrate kinase domain-containing protein deficiency (CARKD). The closely related sister disorder is **NAXE deficiency / PEBEL1** (OMIM #617186), caused by the partner repair enzyme.

**Information source.** Knowledge derives predominantly from **aggregated disease-level resources** (OMIM, Orphanet, MONDO) and from **individual patient case reports / small case series** in the primary literature, supplemented by in vitro (cell line, recombinant enzyme) and model-organism (zebrafish) data. There is no large EHR-derived cohort; this is an ultra-rare disorder documented through gene-first (WES/WGS) discovery.

---

## 2. Etiology

**Primary cause — genetic.** The disease is caused by **biallelic (homozygous or compound-heterozygous) loss-of-function variants in *NAXD***, inherited in an autosomal-recessive pattern. Biallelic *NAXD* variants were identified by whole-exome/whole-genome sequencing in a case series of infants and children with febrile-illness-induced neurodegeneration or cardiac failure and early death ([PMID: 30576410](https://pubmed.ncbi.nlm.nih.gov/30576410/)). The molecular defect is a failure of an essential housekeeping "metabolite repair" function.

**Genetic risk factors.** The only established causal genetic factor is biallelic pathogenic *NAXD* variation. gnomAD constraint metrics (v2.1.1) are consistent with a recessive loss-of-function mechanism: pLI ≈ 5.5×10⁻⁵ (i.e., ~0, the gene tolerates heterozygous LoF) with observed/expected LoF (oe_lof/LOEUF) = 0.615 (95% CI 0.44–0.88). Carriers (heterozygotes) are asymptomatic.

**Environmental "risk"/trigger factors.** Uniquely, environment acts as the **decompensation trigger** rather than an independent cause. Documented triggers include **febrile illness and infection** (most common), **routine immunization** ([PMID: 38214124](https://pubmed.ncbi.nlm.nih.gov/38214124/)), and **physical/mechanical stress such as mild head trauma** ([PMID: 36834994](https://pubmed.ncbi.nlm.nih.gov/36834994/)). These raise body temperature and metabolic flux, accelerating non-enzymatic cofactor hydration and denaturing thermolabile mutant enzyme.

**Protective factors.** No genetic protective variants or modifier alleles have been defined. The main *modifiable* protective actions are **avoidance/aggressive management of fever and triggers** and **niacin/nicotinamide supplementation** (see Treatment).

**Gene–environment interaction.** This is a paradigmatic G×E disorder. The recombinant NAXD proteins bearing patient missense changes p.(Gly63Ser) and p.(Arg608Cys) were **thermolabile** with decreased Vmax and increased KM ([PMID: 30576410](https://pubmed.ncbi.nlm.nih.gov/30576410/)) — providing a direct molecular explanation for why fever (a rise in body temperature) converts a compensated enzymopathy into an acute crisis. During stress, *"nonenzymatic conversion of NAD(P)H to NAD(P)HX increases, and in the absence of repair, NAD(P)H is depleted, and NAD(P)HX accumulates, leading to decompensation"* ([PMID: 35637064](https://pubmed.ncbi.nlm.nih.gov/35637064/)).

---

## 3. Phenotypes

The phenotype spectrum spans neurological, cutaneous, cardiac, muscular and biochemical domains. Onset is typically in the first 1–3 years of life (median age of onset ~1.16 years across the combined cohort), though adult-onset is reported.

| Phenotype | Type | Onset / severity / course | Frequency | Suggested HPO |
|---|---|---|---|---|
| Progressive encephalopathy / psychomotor regression | Clinical sign | Infancy–early childhood; severe; episodic-on-progressive, often fever-triggered | Very frequent | HP:0002376 (Developmental regression); HP:0006846 (Acute encephalopathy) |
| Brain / cerebellar edema | Physical manifestation (imaging) | Acute during crisis; severe | Frequent | HP:0002181 (Cerebral edema) |
| Leukoencephalopathy / white-matter changes | Imaging abnormality | Subacute–chronic; severe | Frequent | HP:0002352 (Leukoencephalopathy) |
| Seizures (incl. myoclonic) | Clinical sign | Infancy; variable | Frequent (whole-cell deficiency) | HP:0001250 (Seizure); HP:0002123 (Generalized myoclonic seizures) |
| Hypotonia (axial) | Clinical sign | Infancy; moderate–severe | Frequent | HP:0001252 (Hypotonia); HP:0008936 (Axial hypotonia) |
| Ataxia | Clinical sign | Childhood; variable | Frequent | HP:0001251 (Ataxia) |
| Flexural erythematous/erosive/necrotic skin lesions | Physical manifestation | With crisis; severe | ~31% of whole-cell deficiency | HP:0000988 (Skin rash); HP:0200041 (Skin erosion); HP:0100697 (Necrosis of the skin) |
| Cardiomyopathy / cardiac failure | Clinical sign | Infancy or later; severe | Subset (esp. mito-isoform variants) | HP:0001638 (Cardiomyopathy); HP:0001635 (Congestive heart failure) |
| Myopathy / neuropathy | Clinical sign | Variable; moderate | Mito-isoform variants | HP:0003198 (Myopathy); HP:0009830 (Peripheral neuropathy) |
| Elevated CSF/serum lactate | Laboratory abnormality | During/after crisis; mild–marked | Frequent | HP:0002151 (Increased serum lactate); HP:0002490 (Increased CSF lactate) |
| Respiratory insufficiency | Clinical sign | Crisis; severe | Subset | HP:0002093 (Respiratory insufficiency) |
| Ophthalmoparesis | Clinical sign | Variable | Subset | HP:0000602 (Ophthalmoplegia) |
| Premature death | Outcome | Early childhood typical | ~78% mortality | HP:0001522 (Death in infancy) |

**Characteristic cutaneous phenotype:** *"The characteristic skin eruption comprises well-demarcated erythematous and erosive plaques progressing to blistering and necrosis, predominantly affecting flexural surfaces"* ([PMID: 39887790](https://pubmed.ncbi.nlm.nih.gov/39887790/)).

**Phenotypic diversity / atypical presentations.** Not all patients show the full picture. One 7-month-old with a novel homozygous variant had neither preceding fever nor skin lesions, prompting the authors to note that *"cases show phenotypic diversity"* ([PMID: 36158054](https://pubmed.ncbi.nlm.nih.gov/36158054/)). A patient presenting after routine immunizations had prominent skin findings **in the absence of fevers** ([PMID: 38214124](https://pubmed.ncbi.nlm.nih.gov/38214124/)).

**Quality-of-life impact.** Formal QoL instruments (EQ-5D/SF-36) have not been applied to this ultra-rare disease. Qualitatively, the impact is profound: acute crises cause loss of acquired milestones, severe disability in survivors, and high early mortality.

---

## 4. Genetic / Molecular Information

**Causal gene.** *NAXD* (HGNC:25576; NCBI Gene 55739; Ensembl ENSG00000213995; gene-OMIM 615910), located at **13q34**, encoding NAD(P)HX dehydratase (UniProt Q8IW45; EC 4.2.1.93). The sister gene is *NAXE* (HGNC:18453; Gene 128240; ENSG00000163382; 1q22; UniProt Q8NCW5; EC 5.1.99.6; phenotype-OMIM 617186; aliases APOA1BP/AIBP/YJEFN1).

**Pathogenic variant spectrum.** Variants are biallelic and predominantly **missense**, with frameshift/loss-of-function alleles also reported. Representative documented variants:

| Variant (cDNA / protein) | Zygosity | Functional evidence | Reference |
|---|---|---|---|
| p.(Gly63Ser) and p.(Arg608Cys) | Compound het (recombinant) | Thermolabile; ↓Vmax, ↑KM for ATP-dependent NADHX dehydratase activity | [PMID: 30576410](https://pubmed.ncbi.nlm.nih.gov/30576410/) |
| c.301G>A, p.(Ala101Thr) | Homozygous | Novel missense via exome sequencing | [PMID: 34161859](https://pubmed.ncbi.nlm.nih.gov/34161859/) |
| c.247G>A | Homozygous | Novel; myoclonic seizures, no fever/skin lesions | [PMID: 36158054](https://pubmed.ncbi.nlm.nih.gov/36158054/) |
| c.101_102delTA, p.(Thr35Phefs*63) + c.318C>G, p.(Ile160Met) | Compound het | Used to derive patient iPSC line | [PMID: 38387170](https://pubmed.ncbi.nlm.nih.gov/38387170/) |
| c.362C>T, p.(Pro121Leu) | VUS | Probable PEBEL2, post-immunization skin findings | [PMID: 38214124](https://pubmed.ncbi.nlm.nih.gov/38214124/) |
| Compound-heterozygous (cardiomyopathy) | Compound het | Metabolic cardiomyopathy with interstitial fibrosis | [PMID: 39822994](https://pubmed.ncbi.nlm.nih.gov/39822994/) |

The founding study demonstrated loss of function at the protein level: *"Recombinant NAXD protein harbouring two missense variants leading to the amino acid changes p.(Gly63Ser) and p.(Arg608Cys) were thermolabile and showed a decrease in Vmax and increase in KM for the ATP-dependent NADHX dehydratase activity"* ([PMID: 30576410](https://pubmed.ncbi.nlm.nih.gov/30576410/)).

**Variant classification & population frequency.** Reported variants are classified pathogenic/likely-pathogenic per ACMG (with occasional VUS such as p.Pro121Leu). Pathogenic alleles are exceedingly rare in gnomAD, consistent with a severe recessive disorder; heterozygous LoF is tolerated (pLI≈0), while biallelic LoF is disease-causing.

**Functional consequence — loss of function** (reduced/abolished enzymatic repair activity), not gain of function or dominant negative.

**Isoform-determined genotype–phenotype correlation (modifier of expression).** *NAXD* encodes two subcellular isoforms: *"Exon 1 of NAXD contains a mitochondrial propeptide, and a unique cytosolic isoform is initiated from an alternative start codon in exon 2"* ([PMID: 35866541](https://pubmed.ncbi.nlm.nih.gov/35866541/)). The isoform hit by a given variant dictates phenotype: variants affecting **both** isoforms → neurological degeneration, seizures and skin lesions; variants affecting **only the mitochondrial** isoform → *"myopathy, moderate neuropathy and a cardiac presentation, without the characteristic skin lesions, seizures or neurological degeneration"* ([PMID: 35866541](https://pubmed.ncbi.nlm.nih.gov/35866541/)).

**Modifier genes / epigenetics / chromosomal abnormalities.** No trans-acting modifier genes, epigenetic mechanisms, or large-scale chromosomal abnormalities have been implicated; the "modifier" of expression is the intragenic isoform architecture described above.

---

## 5. Environmental Information

- **Environmental triggers (not toxins per se):** febrile illness, infection, immunization, and physical/mechanical stress (e.g., mild head trauma). These accelerate the endogenous chemical damage reaction (NAD(P)H → NAD(P)HX). NAD(P)HX itself is described as *"a toxic metabolite that is produced by stressors such as a fever, infection, or physical stress"* ([PMID: 38214124](https://pubmed.ncbi.nlm.nih.gov/38214124/)).
- **Lifestyle factors:** none established; disease presents in infancy/childhood. Relevant management is trigger avoidance and prompt antipyresis.
- **Infectious agents:** no specific pathogen causes the disease; **any** febrile infection can act as a non-specific trigger of decompensation.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function variants in *NAXD*** → **loss of ATP-dependent NAD(P)HX dehydratase activity** (demonstrated: thermolabile recombinant mutants with reduced Vmax/increased KM; [PMID: 30576410](https://pubmed.ncbi.nlm.nih.gov/30576410/)).
2. Loss of repair capacity **leads to** failure to convert the damaged, hydrated cofactors back to NAD(P)H → **accumulation of S-NADHX, R-NADHX and cyclic-NADHX** and **depletion of functional NAD(P)H** (demonstrated in patient fibroblasts: *"highly elevated concentrations of the damaged cofactors S-NADHX, R-NADHX and cyclic NADHX"*; [PMID: 30576410](https://pubmed.ncbi.nlm.nih.gov/30576410/)).
3. A **metabolic stressor (fever/infection/immunization/trauma) results in** an increased rate of non-enzymatic NAD(P)H hydration **and** denaturation of thermolabile mutant enzyme → an unrepaired surge in NAD(P)HX and acute cofactor depletion (*"During stress, nonenzymatic conversion of NAD(P)H to NAD(P)HX increases…leading to decompensation"*; [PMID: 35637064](https://pubmed.ncbi.nlm.nih.gov/35637064/)).
4. This **branches** into downstream lesions:
   - **4a.** Accumulated NAD(P)HX **inhibits multiple dehydrogenases** and NAD(P)H is depleted → impaired redox/energy metabolism → **mitochondrial dysfunction** (higher sensitivity to metabolic stress in galactose/azide media; [PMID: 30576410](https://pubmed.ncbi.nlm.nih.gov/30576410/)).
   - **4b.** Repair failure **results in strong inhibition of the cytosolic, de novo serine synthesis pathway** — a distinct, recently discovered downstream mechanism beyond mitochondrial impairment (*"metabolomic analyses revealed a strong inhibition of the cytosolic, de novo serine synthesis pathway"*; [PMID: 39789421](https://pubmed.ncbi.nlm.nih.gov/39789421/)).
5. Combined energetic/redox and biosynthetic failure **injures high-demand tissues** → **brain/cerebellum/white matter** (encephalopathy, edema, leukoencephalopathy, seizures), **heart/muscle** (cardiomyopathy, myopathy), and **skin** (flexural erosive/necrotic lesions), with **elevated CSF/serum lactate** as a biochemical readout.
6. Untreated, the crisis **progresses to** coma, brain atrophy and **death** (~78% mortality); metabolic bypass with niacin/nicotinamide **partially reverses** the cofactor deficit and improves skin and survival.

### Detail by category

- **Molecular pathway / biochemical abnormality:** defect in the **NAD(P)HX repair (metabolite-repair) pathway**; NAXD (EC 4.2.1.93) works with NAXE (EC 5.1.99.6). The hydrated cofactors are inhibitors of several dehydrogenases and generate harmful byproducts.
- **Metabolic changes:** depletion of the NAD(P)H redox pool; impaired energy metabolism; **inhibition of de novo serine synthesis** ([PMID: 39789421](https://pubmed.ncbi.nlm.nih.gov/39789421/)); elevated lactate reflecting a shift toward anaerobic metabolism / mitochondrial impairment.
- **Cellular processes:** mitochondrial dysfunction; vulnerability under oxidative/metabolic stress (demonstrated by growth impairment in galactose vs glucose; [PMID: 39789421](https://pubmed.ncbi.nlm.nih.gov/39789421/), [PMID: 30576410](https://pubmed.ncbi.nlm.nih.gov/30576410/)); neurodegeneration.
- **Protein dysfunction:** thermolability of mutant enzyme (mechanistic link to fever); reduced catalytic efficiency (↓Vmax, ↑KM).
- **Immune involvement:** zebrafish *naxd* knockouts reveal **immune-system perturbations in early development** ([PMID: 41621837](https://pubmed.ncbi.nlm.nih.gov/41621837/)); clinically, infection/immunization acts as trigger, and inflammation likely amplifies cofactor-hydration stress.
- **Tissue-damage mechanisms:** metabolic/redox stress leading to cytotoxic edema, necrosis (skin), fibrosis (cardiac interstitial fibrosis; [PMID: 39822994](https://pubmed.ncbi.nlm.nih.gov/39822994/)).

**Suggested GO / CHEBI / CL terms:** GO:0110051 (metabolite repair) / GO:0046496 (nicotinamide nucleotide metabolic process); GO:0052855 (ADP-dependent NAD(P)H-hydrate dehydratase activity, EC 4.2.1.93); GO:0006564 (L-serine biosynthetic process); GO:0005739 (mitochondrion, CC); GO:0005829 (cytosol, CC). CHEBI: NADHX, NADPHX, NAD(H), NADP(H), nicotinamide (CHEBI:17154), niacin (CHEBI:15940). CL: neuron (CL:0000540), cardiomyocyte (CL:0000746), keratinocyte (CL:0000312).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** brain and cerebellum (UBERON:0000955 brain; UBERON:0002037 cerebellum), cerebral white matter (UBERON:0002316), spinal cord (UBERON:0002240; myelopathy reported in the NAXE sister disorder). **Skin** (UBERON:0002097), predominantly flexural surfaces. **Heart** (UBERON:0000948) and skeletal muscle (UBERON:0001134) in cardiac/myopathic presentations.
- **Body systems:** central and peripheral **nervous system**, **integumentary** system, **cardiovascular** system, **musculoskeletal** system; **respiratory** insufficiency during crisis.
- **Tissue/cell level:** neurons and glia (white-matter/leukoencephalopathy → oligodendrocyte-supported myelin); cardiomyocytes (with interstitial fibrosis); keratinocytes/epidermis (necrotic skin lesions).
- **Subcellular level:** **mitochondrion** (GO:0005739) and **cytosol** (GO:0005829) — the two compartments corresponding to the mitochondrial and cytosolic NAXD isoforms; this compartmentalization directly maps to phenotype (Section 4).
- **Lateralization:** central lesions are typically **bilateral/symmetric** (edema, leukoencephalopathy); skin lesions are bilateral and flexural.

---

## 8. Temporal Development

- **Onset:** typically **congenital-to-early-childhood**, most within the first 1–3 years; median age of onset ~1.16 years in the combined NAXD/NAXE cohort ([PMID: 39887790](https://pubmed.ncbi.nlm.nih.gov/39887790/)). **Adult onset is possible**: a 32-year-old presented after mild head trauma ([PMID: 36834994](https://pubmed.ncbi.nlm.nih.gov/36834994/)).
- **Onset pattern:** characteristically **(sub)acute** decompensation superimposed on a previously well or mildly affected child, precipitated by a trigger.
- **Progression:** **episodic-on-progressive** — stepwise deterioration with each febrile/stress event, often **rapidly progressive** to coma and death without intervention. Between crises, patients may be relatively stable.
- **Disease course / duration:** frequently **fatal in early childhood**; survivors have chronic, lifelong neurological sequelae.
- **Remission:** no spontaneous cure; **treatment-induced stabilization/improvement** is reported with niacin/nicotinamide and trigger control.
- **Critical periods / window of opportunity:** the peri-febrile window is both the period of maximal vulnerability and the key intervention window — prompt antipyresis, supportive care and NAD-precursor supplementation.

---

## 9. Inheritance and Population

- **Inheritance:** **autosomal recessive** (biallelic *NAXD* variants). Both parents are asymptomatic carriers.
- **Penetrance/expressivity:** appears **high penetrance in the biallelic state** but **variable expressivity** — modulated by which isoform is affected (Section 4) and by exposure to triggers; some homozygotes present atypically without fever or skin lesions ([PMID: 36158054](https://pubmed.ncbi.nlm.nih.gov/36158054/)).
- **Epidemiology:** **ultra-rare**; only case reports and small series (tens of patients worldwide across NAXD and NAXE). No reliable prevalence/incidence estimate exists; Orphanet lists it among ultra-rare metabolic disorders. A literature review compiled **45 NAXD/NAXE patients with 31 pathogenic/likely-pathogenic mutations** ([PMID: 39887790](https://pubmed.ncbi.nlm.nih.gov/39887790/)).
- **Founder effects / consanguinity:** homozygous variants in reported patients suggest a role for **consanguinity** in some families; no defined founder allele has been reported.
- **Carrier frequency:** not formally established; consistent with rarity, gnomAD shows very low pathogenic-allele frequencies.
- **Population demographics / geography:** cases reported across diverse populations (Europe, Middle East, Asia including China; a Chinese cardiomyopathy case is noted as "one of the few" in China; [PMID: 39822994](https://pubmed.ncbi.nlm.nih.gov/39822994/)). No strong sex bias is established (both sexes affected). Age distribution skews to infancy/early childhood.

---

## 10. Diagnostics

**Laboratory tests / biomarkers.**
- **Elevated CSF and/or serum lactate** is a key, reproducible biochemical clue (mild-to-marked; present in the NAXE sister disorder in all affected individuals: *"Lactate was elevated in cerebrospinal fluid of all affected individuals"*; [PMID: 27616477](https://pubmed.ncbi.nlm.nih.gov/27616477/)). Basal metabolic tests may otherwise be near-normal ([PMID: 36158054](https://pubmed.ncbi.nlm.nih.gov/36158054/)).
- **Definitive biomarker:** markedly elevated damaged cofactors **S-NADHX, R-NADHX and cyclic-NADHX** in patient fibroblasts (research/specialized assay), abrogated by wild-type *NAXD* rescue ([PMID: 30576410](https://pubmed.ncbi.nlm.nih.gov/30576410/)).
- **LOINC:** lactate CSF (LOINC 2519-7), lactate plasma/serum (LOINC 2524-7 / 32693-4).

**Imaging.** Brain **MRI** showing cerebral/cerebellar **edema**, **leukoencephalopathy**, and (in progression) global brain atrophy is central to recognizing the acute encephalopathy.

**Cardiac work-up.** Echocardiography/cardiac MRI and endomyocardial evaluation may reveal metabolic **cardiomyopathy with interstitial fibrosis** in the absence of coronary disease or hypertension ([PMID: 39822994](https://pubmed.ncbi.nlm.nih.gov/39822994/)).

**Genetic testing (diagnostic gold standard).** Diagnosis is molecular. **Whole-exome or whole-genome sequencing** identifies biallelic *NAXD* variants (the discovery and most subsequent diagnoses used WES/WGS; [PMID: 30576410](https://pubmed.ncbi.nlm.nih.gov/30576410/); [PMID: 34161859](https://pubmed.ncbi.nlm.nih.gov/34161859/)). Targeted single-gene/panel testing (mitochondrial/leukodystrophy/metabolic-encephalopathy panels including *NAXD* and *NAXE*) is appropriate when the phenotype is suggestive. Segregation confirms biallelic status. Functional confirmation (fibroblast NAD(P)HX measurement or recombinant enzyme assay) can resolve VUS.

**Clinical criteria / differential diagnosis.** No formal consensus criteria exist; diagnosis rests on the triad of **fever-triggered neuroregression + suggestive MRI (edema/leukoencephalopathy) + elevated lactate**, confirmed genetically. Because it can be mistaken for a **primary mitochondrial disease** (patients have been treated with a "mitochondrial cocktail"; [PMID: 36158054](https://pubmed.ncbi.nlm.nih.gov/36158054/)), key differentials include Leigh syndrome and other mitochondrial encephalopathies, other leukodystrophies, biotin-thiamine-responsive basal ganglia disease, and — with skin involvement — nutritional/genetic niacin-deficiency states (pellagra-like). The sister disorder **NAXE deficiency (PEBEL1)** is the closest differential and is distinguished by gene.

**Screening.** Not part of routine newborn screening. **Cascade carrier testing** of relatives and **prenatal/preimplantation genetic testing** are available once the familial variants are known.

---

## 11. Outcome / Prognosis

- **Mortality:** high — *"The mortality rate was 78%, with survivors experiencing varying degrees of neurological sequelae"* ([PMID: 39887790](https://pubmed.ncbi.nlm.nih.gov/39887790/)). In the NAXE sister disorder, the course was rapidly progressive to coma, global brain atrophy and death.
- **Morbidity/disability:** survivors typically have significant neurological disability (developmental regression, spasticity, epilepsy, motor impairment).
- **Prognostic factors:** **which isoform is affected** (mitochondrial-only vs whole-cell) shapes organ involvement and course; **frequency/severity of triggering events**; and **early institution of niacin/nicotinamide and trigger control**, which improve skin lesions and survival. Niacin response, however, is **not universal**: one PEBEL1 patient deteriorated to a fatal outcome despite the highest reported niacin dose ([PMID: 38974613](https://pubmed.ncbi.nlm.nih.gov/38974613/)).
- **Complications:** status epilepticus, respiratory failure, cardiac failure, secondary infections, and sequelae of brain injury.

---

## 12. Treatment

There is no curative therapy; management is **metabolic bypass + aggressive trigger control + supportive care**.

**Pharmacotherapy / metabolic bypass.**
- **Niacin / nicotinamide (vitamin B3)** — the principal disease-modifying agent. By feeding NAD *de novo*/salvage synthesis it replenishes the depleted NAD(P) pool: *"Niacin/nicotinamide supplementation resulted in improvements in skin lesions and survival rates"* ([PMID: 39887790](https://pubmed.ncbi.nlm.nih.gov/39887790/)). The rationale is explicit in the NAXE literature: *"NAD or nicotinic acid (vitamin B3) supplementation might have therapeutic implications for this fatal disorder"* ([PMID: 27616477](https://pubmed.ncbi.nlm.nih.gov/27616477/)). A systematic review of 7 PEBEL1/PEBEL2 patients found most improved or stabilized on niacin, though one deteriorated fatally ([PMID: 38974613](https://pubmed.ncbi.nlm.nih.gov/38974613/)). NCIT: niacin (NCIT:C574), nicotinamide (NCIT:C577).
- **Adverse-event management:** niacin-related urticaria has been managed off-label with a COX-2 inhibitor ([PMID: 38974613](https://pubmed.ncbi.nlm.nih.gov/38974613/)).

**Acute supportive care.** Prompt **antipyresis** and **treatment of the precipitating infection**, intensive supportive/neurocritical care during crises, seizure management, and cardiac support as needed. Empirical **mitochondrial "cocktail"** has been used but is not specifically corrective ([PMID: 36158054](https://pubmed.ncbi.nlm.nih.gov/36158054/)).

**Advanced / experimental therapeutics.** No approved gene, cell, or RNA therapy exists. Wild-type *NAXD* lentiviral rescue corrects the biochemical defect in patient fibroblasts (proof of concept for gene replacement; [PMID: 30576410](https://pubmed.ncbi.nlm.nih.gov/30576410/)). NAD-precursor strategies (nicotinamide riboside, nicotinic acid) are of mechanistic interest.

**Personalized approach.** Genotype (isoform affected) and trigger history should guide monitoring (e.g., cardiac surveillance for mitochondrial-isoform variants) and preventive planning.

---

## 13. Prevention

- **Primary prevention:** for at-risk families, **genetic counseling**, carrier testing, and reproductive options (prenatal/PGT) prevent recurrence. There is no population-level primary prevention (not vaccine-preventable; disease is genetic).
- **Secondary prevention (trigger mitigation):** in known-affected individuals, **prompt and aggressive control of fever/infection**, vigilance around immunizations and physical stress, and **prophylactic niacin/nicotinamide** aim to prevent decompensation. Caution and close monitoring are warranted around immunization given a reported post-vaccination decompensation ([PMID: 38214124](https://pubmed.ncbi.nlm.nih.gov/38214124/)).
- **Tertiary prevention:** rehabilitation, epilepsy management, cardiac and respiratory support to limit complications in survivors.
- **Counseling:** autosomal-recessive recurrence risk is **25%** per pregnancy for carrier couples; cascade testing of relatives is recommended.
- **Screening:** cascade carrier screening; prenatal diagnosis where familial variants are known. Not currently in newborn-screening panels.

---

## 14. Other Species / Natural Disease

- **Evolutionary conservation:** the NAD(P)HX repair system is **ancient and highly conserved**. NAXD/NAXE orthologs function in plants (*Arabidopsis thaliana*, *Zea mays*), E. coli, and vertebrates: *"Arabidopsis thaliana and Zea mays NAD(P)HX dehydratase (NAXD) and NAD(P)HX epimerase (NAXE), two enzymes that are involved in repair of chemically damaged NAD(P)H cofactors"* ([PMID: 36710015](https://pubmed.ncbi.nlm.nih.gov/36710015/)).
- **Orthologs / taxonomy (NCBI Taxon):** human *NAXD* (Gene 55739); zebrafish *naxd* (used for CRISPR models; *Danio rerio*, taxon 7955); plant orthologs in *A. thaliana* (taxon 3702) and *Z. mays* (taxon 4577); bacterial *yjeF*-family in *E. coli*.
- **Natural disease in other species:** no spontaneously occurring NAXD-deficiency disease has been catalogued in companion animals/wildlife (no OMIA entry noted); relevance to date is via engineered models.
- **Zoonotic potential:** not applicable (genetic, non-transmissible).

---

## 15. Model Organisms

| Model | Type | Key features / recapitulation | Reference |
|---|---|---|---|
| Zebrafish *naxd* (and *naxe*) CRISPR/Cas9 knockouts | Vertebrate, in vivo | Both accumulate NADHX; *naxd* line shows distinctive features and **immune-system perturbations in early development** | [PMID: 41621837](https://pubmed.ncbi.nlm.nih.gov/41621837/) |
| Human HAP1 *NAXD* knockout | Cellular, in vitro | Growth impairment specifically in galactose vs glucose; metabolomics reveals **de novo serine synthesis inhibition**; models the metabolic lesion | [PMID: 39789421](https://pubmed.ncbi.nlm.nih.gov/39789421/) |
| Patient fibroblasts | Primary human cells | Elevated S-/R-/cyclic-NADHX; corrected by WT *NAXD* rescue; mitochondrial-stress sensitivity | [PMID: 30576410](https://pubmed.ncbi.nlm.nih.gov/30576410/) |
| Patient iPSC line BCHNDi001-A | iPSC | Derived from PEBEL2 fibroblasts (c.101_102delTA; c.318C>G); enables differentiation into affected lineages | [PMID: 38387170](https://pubmed.ncbi.nlm.nih.gov/38387170/) |
| Recombinant NAXD/NAXE (E. coli; plant systems) | In vitro enzymology | Purified enzymes for kinetic/thermostability assays (demonstrated thermolability of mutants) | [PMID: 30576410](https://pubmed.ncbi.nlm.nih.gov/30576410/); [PMID: 36710015](https://pubmed.ncbi.nlm.nih.gov/36710015/) |

**Zebrafish CRISPR evidence:** *"we generated zebrafish lines deficient in naxe or naxd using CRISPR/Cas9 technology. While both models accumulated NADHX, only naxd…"* ([PMID: 41621837](https://pubmed.ncbi.nlm.nih.gov/41621837/)). **iPSC evidence:** *"we generated an induced pluripotent stem cell (iPSC) line from the dermal fibroblasts (HDFs) of a PEBEL2 patient who carried biallelic mutations, c.101_102delTA(p.Thr35Phefs*63) and c.318C > G (p.Ile160Met) in NAXD"* ([PMID: 38387170](https://pubmed.ncbi.nlm.nih.gov/38387170/)).

**Model applications & limitations:** these systems recapitulate the core **NADHX accumulation** and metabolic lesion and enable therapeutic testing; limitations include incomplete recapitulation of the full human multisystem/fever-triggered clinical phenotype and species-specific differences. Resources: ZFIN (zebrafish), Cellosaurus (HAP1, iPSC lines).

---

## Mechanistic Model / Interpretation

```
 Biallelic LoF NAXD (recessive; gnomAD pLI≈0)
        │  loss of ATP-dependent NAD(P)HX dehydratase (EC 4.2.1.93)
        ▼
 Failure of NAD(P)HX repair
   ├── ↑ S-NADHX / R-NADHX / cyclic-NADHX  (toxic, inhibit dehydrogenases)
   └── ↓ functional NAD(P)H  (redox/energy pool depleted)
        │
   [ TRIGGER: fever / infection / immunization / trauma ]
        │  ↑ non-enzymatic NAD(P)H→NAD(P)HX  +  denatures thermolabile mutant enzyme
        ▼
 Acute unrepaired NAD(P)HX surge  →  metabolic decompensation
        ├──► Mitochondrial dysfunction  ─┐
        └──► ↓ de novo serine synthesis ─┤ combined energetic/biosynthetic failure
                                          ▼
        Injury to high-demand tissues:
        • Brain/cerebellum/white matter → encephalopathy, edema, leukoencephalopathy, seizures, ↑lactate
        • Heart/muscle → cardiomyopathy (interstitial fibrosis), myopathy   [esp. mito-isoform variants]
        • Skin (flexural) → erosive/necrotic plaques   [whole-cell deficiency]
        ▼
        ~78% mortality  ── niacin/nicotinamide (↑NAD synthesis) + trigger control → improved skin & survival
```

**Upstream vs downstream:** the *NAXD* mutation and cofactor-repair failure are **upstream**; mitochondrial dysfunction and serine-synthesis inhibition are **parallel downstream** effectors; tissue injury and clinical crisis are **terminal**. The **fever/thermolability node** is the key modifiable amplifier converting a compensated enzymopathy into acute disease, and the **niacin bypass** is the key therapeutic lever.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [30576410](https://pubmed.ncbi.nlm.nih.gov/30576410/) | *NAXD deficiency: a novel neurodegenerative disorder exacerbated by febrile illnesses* | Founding disease description; recessive WES/WGS diagnosis; elevated S-/R-/cyclic-NADHX; thermolabile mutant enzyme (↓Vmax, ↑KM); mitochondrial-stress sensitivity; WT rescue |
| [34161859](https://pubmed.ncbi.nlm.nih.gov/34161859/) | *NAXD deficiency due to a novel biallelic missense variant + review* | Disease name/OMIM #618321; recessive basis; novel c.301G>A p.(Ala101Thr) |
| [35866541](https://pubmed.ncbi.nlm.nih.gov/35866541/) | *Clinical/biochemical distinctions for NAXD or NAXE deficiency* | Isoform architecture (mito propeptide exon 1 vs cytosolic exon 2) → genotype–phenotype correlation |
| [39789421](https://pubmed.ncbi.nlm.nih.gov/39789421/) | *Failure to repair NAD(P)H blocks de novo serine synthesis* | HAP1 KO galactose sensitivity; serine-synthesis inhibition mechanism |
| [39887790](https://pubmed.ncbi.nlm.nih.gov/39887790/) | *Cutaneous manifestations of NAXD/NAXE deficiency* | 45-patient review; ~78% mortality; flexural necrotic skin phenotype; niacin improves skin/survival |
| [35637064](https://pubmed.ncbi.nlm.nih.gov/35637064/) | *NAXE deficiency amenable for metabolic correction* | Stress-triggered decompensation mechanism (NAD(P)H depletion) |
| [27616477](https://pubmed.ncbi.nlm.nih.gov/27616477/) | *NAXE mutations cause a lethal neurometabolic disorder* | Sister disorder (PEBEL1): febrile-triggered ataxia/edema/skin; elevated CSF lactate; niacin rationale |
| [41621837](https://pubmed.ncbi.nlm.nih.gov/41621837/) | *Zebrafish models of NADHX repair deficiency* | naxd/naxe CRISPR models; NADHX accumulation; immune perturbation |
| [38387170](https://pubmed.ncbi.nlm.nih.gov/38387170/) | *iPSC line BCHNDi001-A from PEBEL2 patient* | Patient-derived iPSC with defined biallelic variants |
| [39822994](https://pubmed.ncbi.nlm.nih.gov/39822994/) | *Metabolic cardiomyopathy from compound-het NAXD* | Cardiac phenotype with interstitial fibrosis |
| [36834994](https://pubmed.ncbi.nlm.nih.gov/36834994/) | *Severe NAXD syndrome in adulthood after mild head trauma* | Adult onset; non-febrile physical-stress trigger |
| [36158054](https://pubmed.ncbi.nlm.nih.gov/36158054/) | *A case with NAXD deficiency (novel c.247G>A)* | Phenotypic diversity; atypical case without fever/skin lesions; mild lactate elevation |
| [38214124](https://pubmed.ncbi.nlm.nih.gov/38214124/) | *Progressive encephalopathy after 4-month immunizations* | Immunization as trigger; skin findings without fever; VUS c.362C>T |
| [38974613](https://pubmed.ncbi.nlm.nih.gov/38974613/) | *Transient response to high-dose niacin (NAXE)* | Niacin efficacy but not universal (one fatal outcome despite highest dose) |
| [36710015](https://pubmed.ncbi.nlm.nih.gov/36710015/) | *Systems for plant protein expression* | Evolutionary conservation of NAXD/NAXE (Arabidopsis, maize) |

**Evidence source types:** human clinical (case reports/series, literature reviews), in vitro (patient fibroblasts, HAP1 KO, recombinant enzyme, iPSC), model organism (zebrafish), and computational/genomic constraint (gnomAD).

---

## Limitations and Knowledge Gaps

- **Ultra-rare, no cohort epidemiology.** Prevalence/incidence, carrier frequency, sex ratio, and penetrance estimates are unavailable; all clinical data come from small series prone to ascertainment/publication bias toward severe cases (mortality may be overestimated).
- **Treatment evidence is anecdotal.** Niacin/nicotinamide benefit is based on case reports and one small systematic review; there are **no randomized trials**, optimal dosing is undefined, and at least one patient deteriorated despite maximal therapy ([PMID: 38974613](https://pubmed.ncbi.nlm.nih.gov/38974613/)).
- **Mechanistic gaps.** The relative contributions of mitochondrial dysfunction versus serine-synthesis inhibition to specific organ phenotypes are not resolved; why skin and cerebellum are especially vulnerable is unexplained; the immune-perturbation finding is model-derived and needs human validation.
- **Genotype–phenotype nuance.** The isoform rule explains broad patterns but individual variability (atypical fever-negative cases) indicates unidentified modifiers.
- **No natural animal disease / limited long-term outcome data.**

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry** to define natural history, prevalence, penetrance, sex ratio, and standardized outcomes; harmonize trigger and treatment data.
2. **Prospective, dose-finding evaluation of NAD precursors** (niacin, nicotinamide, nicotinamide riboside) with biochemical endpoints (NADHX/NAD(P)H, lactate) — ideally a basket trial spanning PEBEL1/PEBEL2.
3. **iPSC-derived organoid modeling** (neuronal, cardiac, keratinocyte) from BCHNDi001-A and new lines to test whether serine supplementation and NAD precursors rescue tissue-specific phenotypes ([PMID: 38387170](https://pubmed.ncbi.nlm.nih.gov/38387170/); [PMID: 39789421](https://pubmed.ncbi.nlm.nih.gov/39789421/)).
4. **Thermal-stress assays across the variant panel** to build a genotype→thermolability→clinical-severity map, informing prognosis and trigger-avoidance counseling ([PMID: 30576410](https://pubmed.ncbi.nlm.nih.gov/30576410/)).
5. **Gene-replacement proof-of-concept in vivo** (zebrafish *naxd* and/or AAV-*NAXD* in mammalian models), building on fibroblast lentiviral rescue.
6. **Dissect the immune-perturbation phenotype** from zebrafish in human systems to test whether inflammation independently amplifies decompensation ([PMID: 41621837](https://pubmed.ncbi.nlm.nih.gov/41621837/)).
7. **Develop a clinical NAD(P)HX/serine metabolite biomarker assay** for rapid diagnosis and treatment monitoring, and evaluate inclusion of *NAXD*/*NAXE* in mitochondrial/leukodystrophy gene panels and consideration for newborn screening pilots.

---

*Report compiled from 9 confirmed findings across 18 reviewed papers. All quoted material is verbatim from the cited PubMed abstracts.*


## Artifacts

- [OpenScientist final report](NAD_P_HX_Dehydratase_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](NAD_P_HX_Dehydratase_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 15 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 44 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 14 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0034121` (2 mentions) - the report calls it "MONDO"; MONDO calls it **NAD(P)HX dehydratase deficiency**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005739` (2 mentions) - the report calls it "mitochondrion, CC", "mitochondrion", "Subcellular level:** **mitochondrion"; GO calls it **mitochondrion**
- `GO:0005829` (2 mentions) - the report calls it "cytosol, CC", "cytosol"; GO calls it **cytosol**
- `UBERON:0002097` (1 mention) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005739` - called "mitochondrion, CC", "mitochondrion", "Subcellular level:** **mitochondrion"
- `GO:0005829` - called "cytosol, CC", "cytosol"