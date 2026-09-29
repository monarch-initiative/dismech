---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T12:00:32.394181'
end_time: '2026-09-25T12:14:15.271832'
duration_seconds: 822.88
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Lemierre Syndrome
  mondo_id: MONDO:0015306
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
citation_count: 22
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 20
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 24
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 12
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: UBERON:0001584
    reported_labels:
    - internal jugular vein
    - Internal jugular vein
    ontology_label: left subclavian artery
  - term_id: CHEBI:6077
    reported_labels:
    - metronidazole
    ontology_label: Ivalin
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Lemierre_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Lemierre_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lemierre Syndrome
- **MONDO ID:** MONDO:0015306 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Lemierre Syndrome** covering all of the
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

# Lemierre Syndrome: A Comprehensive Disease Characteristics Report

**Disease:** Lemierre Syndrome (LS)
**MONDO ID:** MONDO:0015306
**Category:** Infectious Disease
**Report type:** Disease knowledge-base entry (multi-iteration autonomous literature synthesis)
**Evidence base:** 27 PubMed sources; predominantly human clinical case series, systematic reviews, and national registry studies, supplemented by veterinary/in-vitro mechanistic studies. No patient-level data files provided.

---

## Summary

**Lemierre syndrome is a rare, life-threatening, acquired infectious disease defined by septic thrombophlebitis of the internal jugular vein (IJV) that develops as a complication of an oropharyngeal (usually pharyngotonsillar) infection, with subsequent metastatic septic emboli that spread most often to the lungs.** It is caused predominantly by the Gram-negative obligate anaerobe *Fusobacterium necrophorum*, which is identified in roughly 78% of cases in systematic reviews. The classic causal triad is: (1) oropharyngeal infection → (2) IJV septic thrombophlebitis → (3) metastatic septic emboli. The syndrome characteristically strikes previously healthy adolescents and young adults (median age ~15–20 years) with a male predominance.

**Critically, Lemierre syndrome is NOT a genetic disease.** No causal human gene, Mendelian inheritance pattern, penetrance/expressivity behavior, heritable variant, or founder effect exists for this condition. It is an acquired complication of bacterial infection. Consequently, the many sections of the research template dealing with causal genes, pathogenic variants, ACMG variant classification, gnomAD allele frequencies, genetic testing (WGS/WES/panels/karyotyping), carrier screening, genetic counseling, and inheritance are **Not Applicable**, and this report explicitly documents them as such rather than fabricating content. The etiologically relevant "genome" here is that of the pathogen: the *F. necrophorum* leukotoxin operon and associated virulence factors.

**Prognosis is favorable with prompt treatment but the illness remains serious.** Modern mortality is approximately 5% (versus up to 80% in the pre-antibiotic era, when death commonly occurred within 7–15 days), but complication rates are high—sepsis in ~83%, thrombocytopenia in ~75%, ICU admission in ~43%, and septic shock in ~18% of hospitalized patients. Management centers on prolonged anaerobe-active antibiotic therapy (a beta-lactam/beta-lactamase inhibitor or third-generation cephalosporin combined with metronidazole, or a carbapenem) plus source control; adjunctive anticoagulation remains controversial and of unproven benefit. With appropriate therapy the disease is self-limited/curable (no chronic or relapsing course), and thrombus resolves or recanalizes in ~78% of cases on follow-up imaging. A key evidence gap is that the platelet-aggregation/thrombus-initiation step of human pathophysiology is inferred from in-vitro and ruminant data rather than directly demonstrated in humans.

---

## Key Findings

### Finding 1 — Definition and dominant pathogen

Lemierre syndrome is septic thrombophlebitis of the internal jugular vein caused predominantly by *Fusobacterium necrophorum* following an oropharyngeal infection. A systematic review of 143 pediatric cases found *F. necrophorum* in 78.3% of patients, with fever as the most common presenting symptom (92%); CT imaging was used in 89.5% of cases and was most useful for detecting IJV thrombosis and septic emboli ([PMID: 42127655](https://pubmed.ncbi.nlm.nih.gov/42127655/)): *"F. necrophorum was the predominantly identified organism in 78.3% of patients."* The defining pathology is captured directly in the literature: *"It is characterized by septic thrombophlebitis of the internal jugular vein and subsequent metastatic abscess formation. The most common causative pathogen of LS is Fusobacterium necrophorum"* ([PMID: 41517763](https://pubmed.ncbi.nlm.nih.gov/41517763/)). The classic clinical sequence—oropharyngeal infection → IJV septic thrombophlebitis → metastatic septic emboli (most often to the lung)—organizes the entire disease concept.

**Ontology anchors:** MONDO:0015306 (Lemierre syndrome); UBERON:0001584 (internal jugular vein); NCBI:txid859 (*Fusobacterium necrophorum*); HP:0001945 (Fever).

### Finding 2 — Epidemiology: rare, rising, young, male-predominant

Lemierre syndrome is rare but with rising incidence, currently estimated at roughly 1–10 cases per million per year (a commonly cited central estimate is ~3.6 per million). A Swedish nationwide study (2010–2017, n = 300 invasive *F. necrophorum* infections) documented that the incidence of invasive *F. necrophorum* infection increased from 2.9 to 5.0 cases/million/year (p = 0.001), that 104/300 (35%) of these patients developed Lemierre syndrome, and that the median age of LS patients was 20 years ([PMID: 31843654](https://pubmed.ncbi.nlm.nih.gov/31843654/)): *"The incidence increased from 2.9 to 5.0 cases/million/year from 2010-13 to 2014-17 (p 0.001)."* A population-level incidence estimate of *"3.6 cases per million population"* is reported in [PMID: 42576194](https://pubmed.ncbi.nlm.nih.gov/42576194/). The disease has been termed "the forgotten disease" because it became rare after the introduction of antibiotics but has been re-emerging since the 2000s. It preferentially affects previously healthy adolescents and young adults with a male predominance.

**Ontology anchors:** age of onset — adolescent/young adult (HP:0011462, Young adult onset).

### Finding 3 — Severe systemic illness; ~5% modern mortality

Lemierre syndrome causes severe systemic illness with high complication rates. In the Swedish cohort of 104 LS patients, 75% (72/96) had thrombocytopenia on admission, 83% (86/104) had sepsis, 18% (19/104) developed septic shock, and 43% (45/104) required intensive care ([PMID: 31843654](https://pubmed.ncbi.nlm.nih.gov/31843654/)): *"72/96 (75%) had thrombocytopenia on admission, 86/104 (83%) had sepsis, 19/104 (18%) developed septic shock and 45/104 (43%) needed intensive [care]."* Modern mortality is approximately 5%, rising with diagnostic delay, whereas in the pre-antibiotic era the disease *"was often characterized by a fatal course within 7-15 days with a mortality rate that could reach up to 80% of cases"* ([PMID: 40265142](https://pubmed.ncbi.nlm.nih.gov/40265142/)). Long-term complications were reported in 4.2% of pediatric cases ([PMID: 42127655](https://pubmed.ncbi.nlm.nih.gov/42127655/)).

| Complication | Frequency (Swedish LS cohort, n=104) |
|---|---|
| Sepsis | 83% (86/104) |
| Thrombocytopenia on admission | 75% (72/96) |
| ICU admission | 43% (45/104) |
| Septic shock | 18% (19/104) |

**Ontology anchors:** HP:0100806 (Sepsis); HP:0001873 (Thrombocytopenia); HP:0031273 (Septic shock).

### Finding 4 — Leukotoxin is the major virulence factor

*F. necrophorum* leukotoxin is the major virulence factor driving Lemierre pathophysiology, with endotoxin (LPS), hemolysin, hemagglutinin, proteases, and adhesins contributing. Reviews conclude that *"leukotoxin and endotoxin are believed to be more important than other toxins in overcoming the host's defence mechanisms to establish the infection"* ([PMID: 8711893](https://pubmed.ncbi.nlm.nih.gov/8711893/)). Mechanistically, purified leukotoxin activates polymorphonuclear leukocytes (PMNs) and induces their apoptosis/necrosis: *"The ability of F. necrophorum leukotoxin to modulate the host immune system by its toxicity, including cellular activation of PMNs and apoptosis-mediated killing of phagocytes and immune effector cells, represents a potentially important mechanism of its pathogenesis"* ([PMID: 12117974](https://pubmed.ncbi.nlm.nih.gov/12117974/)). Subspecies *necrophorum* (biotype A) is more virulent than subspecies *funduliforme* (biotype B) ([PMID: 16701574](https://pubmed.ncbi.nlm.nih.gov/16701574/)).

**Ontology anchors:** GO:0006954 (inflammatory response); GO:0006915 (apoptotic process); GO:0090729 (toxin activity); CL:0000775 (neutrophil); CHEBI:16412 (lipopolysaccharide).

### Finding 5 — Diagnosis: contrast-enhanced CT + anaerobic blood cultures + molecular methods

Diagnosis relies on contrast-enhanced CT of the neck and chest (demonstrating IJV thrombosis and septic emboli) plus anaerobic blood cultures, with molecular methods increasingly used. In the pediatric systematic review, *"Computed tomography (CT) imaging was utilized in 89.5% of cases, and was most useful for detecting thrombosis of the internal jugular vein and septic emboli"* ([PMID: 42127655](https://pubmed.ncbi.nlm.nih.gov/42127655/)). The two-pronged confirmatory standard is stated directly: *"The diagnosis of Lemierre's syndrome is typically confirmed through the identification of thrombophlebitis of the internal jugular vein on radiographic imaging and the isolation of anaerobic bacteria in blood cultures"* ([PMID: 39840169](https://pubmed.ncbi.nlm.nih.gov/39840169/)). Contrast-enhanced cervicothoracic CT is the workhorse ([PMID: 40224244](https://pubmed.ncbi.nlm.nih.gov/40224244/)). Because anaerobic cultures may be slow or negative, molecular diagnostics—16S rDNA sequencing/targeted PCR ([PMID: 31843654](https://pubmed.ncbi.nlm.nih.gov/31843654/)) and targeted next-generation sequencing combined with metagenomic capture—enable rapid *F. necrophorum* detection ([PMID: 41517763](https://pubmed.ncbi.nlm.nih.gov/41517763/)). Common laboratory abnormalities include thrombocytopenia, elevated CRP, and leukocytosis.

**Ontology anchors:** diagnostic imaging — contrast-enhanced CT; LOINC-mappable labs (CRP, platelet count, WBC); anaerobic blood culture.

### Finding 6 — Treatment: prolonged anaerobe-active antibiotics + source control; anticoagulation controversial

Treatment centers on prolonged anaerobe-active antibiotics with source control. First-line therapy is described as: *"Immediate treatment involves broad-spectrum antibiotic therapy, often utilizing a third-generation cephalosporin or a beta-lactam in combination with metronidazole"* ([PMID: 40224244](https://pubmed.ncbi.nlm.nih.gov/40224244/)). Carbapenems are also reported as a good therapeutic choice ([PMID: 20570017](https://pubmed.ncbi.nlm.nih.gov/20570017/)). Anticoagulation remains controversial: a systematic review found parenteral anticoagulation used initially in 12/14 patients and DOAC outcomes similar to warfarin, but concluded that *"the thromboembolic events have rarely led to significant complications; thrombi typically resolve independently, and concerns for bleeding risks are well founded"* ([PMID: 32909436](https://pubmed.ncbi.nlm.nih.gov/32909436/)). Anticoagulation was used in 62.2% of pediatric cases and surgery in 6% ([PMID: 42127655](https://pubmed.ncbi.nlm.nih.gov/42127655/)). Surgical options include abscess drainage, with IJV ligation/excision reserved for non-responders ([PMID: 39257960](https://pubmed.ncbi.nlm.nih.gov/39257960/)).

| Treatment element | Detail | NCIT-type mapping |
|---|---|---|
| Beta-lactam/BLI (e.g., ampicillin-sulbactam, piperacillin-tazobactam) | Empiric anaerobe coverage | Antibacterial agent |
| Third-gen cephalosporin + metronidazole | Common first-line combination | Metronidazole (NCIT antibacterial) |
| Carbapenem (e.g., meropenem) | Alternative broad-spectrum choice | Carbapenem antibiotic |
| Anticoagulation (LMWH/DOAC/warfarin) | Selected high-risk cases; controversial | Anticoagulant therapy |
| Abscess drainage / IJV ligation-excision | Source control; salvage for non-responders | Surgical procedure |

**Ontology anchors:** CHEBI:6077 (metronidazole); NCIT antibacterial/anticoagulant/surgical-procedure branches.

### Finding 7 — Anatomy and phenotypes

The primary source is oropharyngeal (tonsillitis/pharyngitis, peritonsillar abscess), with odontogenic and otogenic (otitis media/mastoiditis) sources also described ([PMID: 42517948](https://pubmed.ncbi.nlm.nih.gov/42517948/), [PMID: 12109395](https://pubmed.ncbi.nlm.nih.gov/12109395/)). Septic thrombophlebitis localizes to the internal jugular vein, and septic emboli disseminate preferentially to the lungs (pulmonary emboli/cavitary consolidations); in one series *"All [patients had] sore throat and pulmonary embolisms"* ([PMID: 20570017](https://pubmed.ncbi.nlm.nih.gov/20570017/)). Metastatic and contiguous spread can reach the intracranial venous sinuses, orbit, joints, and pleura (empyema), and can be complicated by DIC and ARDS. An otogenic pediatric series documented that *"Internal jugular vein thrombosis occurred in 80%, sigmoid sinus thrombosis in 60%, and cavernous sinus thrombosis in 30%"* ([PMID: 42141231](https://pubmed.ncbi.nlm.nih.gov/42141231/)). Common phenotypes include fever (92%), sore throat, neck pain/swelling, chest pain, hemoptysis, and dyspnea.

| Level | Structure | UBERON / ontology term |
|---|---|---|
| Primary source | Oropharynx / palatine tonsil | UBERON:0001729 (oropharynx); UBERON:0002373 (palatine tonsil) |
| Primary vascular lesion | Internal jugular vein | UBERON:0001584 |
| Dominant embolic target | Lung | UBERON:0002048 |
| Intracranial extension | Sigmoid/cavernous venous sinuses | UBERON:0006459 (sigmoid sinus); UBERON:0004024 (cavernous sinus) |
| Body systems | Cardiovascular, respiratory, digestive/upper aerodigestive | — |

**Phenotype ontology anchors:** HP:0001945 (Fever); HP:0002098 (Respiratory distress/dyspnea); HP:0002105 (Hemoptysis); HP:0100749 (Chest pain).

### Finding 8 — Not genetic; expanding etiologic spectrum ("Lemierre-like syndrome")

Lemierre syndrome is not a genetic disease—no causal human gene, inheritance pattern, or heritable variant is described; it is an acquired complication of bacterial infection. Beyond classic *F. necrophorum*, cases arise from viridans group streptococci (often odontogenic; [PMID: 42517948](https://pubmed.ncbi.nlm.nih.gov/42517948/)) and other anaerobes/streptococci. "Lemierre-like syndrome" (LLS) from non-oropharyngeal sources is increasingly recognized: *"In contrast to classic Lemierre syndrome, sources of infection are not related to oropharyngeal infections, as are frequent soft tissue infections. In recent years, Staphylococcus aureus has been identified as an emergent pathogen that causes this syndrome. The mortality rate of LLS caused by this pathogen is approximately 16%"* ([PMID: 38363930](https://pubmed.ncbi.nlm.nih.gov/38363930/)). An "incomplete Lemierre's syndrome" variant is also defined: *"Incomplete Lemierre's syndrome is a bacterial oropharyngeal infection, complicated by septic emboli to end organs, but without thrombophlebitis of the internal jugular vein"* ([PMID: 42286749](https://pubmed.ncbi.nlm.nih.gov/42286749/)). Risk factors are environmental/infectious: preceding pharyngotonsillitis, young age, and restricted/inappropriate antibiotic use for sore throat ([PMID: 12109395](https://pubmed.ncbi.nlm.nih.gov/12109395/)).

### Finding 9 — Natural animal disease and models (necrobacillosis)

*F. necrophorum* causes major naturally occurring disease in animals (necrobacillosis), which informs pathogenesis and prevention. It is a normal alimentary-tract commensal and opportunistic pathogen; *"Of these, bovine liver abscesses and foot rot are of significant concern to the cattle industry"* ([PMID: 16701574](https://pubmed.ncbi.nlm.nih.gov/16701574/)). Liver abscesses arise when ruminal organisms enter the portal circulation secondary to ruminal acidosis. A randomized, blinded feedlot field trial demonstrated that a *F. necrophorum* bacterin reduced liver abscesses (odds ratio 0.27, P = 0.05) and footrot (OR 0.18, P = 0.03) in forage-fed cattle: *"The odds that a vaccinated animal in the ALF group would have an A or A+ liver abscess at slaughter were less than 1/3 the odds that an unvaccinated animal"* ([PMID: 16363327](https://pubmed.ncbi.nlm.nih.gov/16363327/)). Isolates have also been recovered from the respiratory tract of white-tailed deer (*Odocoileus virginianus*) ([PMID: 24590666](https://pubmed.ncbi.nlm.nih.gov/24590666/)). Leukotoxin virulence is studied primarily in bovine leukocyte/PMN in-vitro models ([PMID: 12117974](https://pubmed.ncbi.nlm.nih.gov/12117974/)).

**Taxonomy anchors:** *Bos taurus* (NCBI:txid9913, cattle); *Odocoileus virginianus* (NCBI:txid9874, white-tailed deer); *Fusobacterium necrophorum* (NCBI:txid859).

### Finding 10 — Prevention is secondary; no human vaccine

Prevention of Lemierre syndrome is secondary—early recognition and appropriate anaerobe-active antibiotic treatment of *F. necrophorum* pharyngitis—because no human vaccine or established primary chemoprophylaxis exists. Cost-effectiveness modeling suggests that *"examining throat swabs from 15- to 24-year-olds for F. necrophorum followed by antibiotic treatment will probably be less costly than most other life-saving medical interventions, with a median cost of US$8,795 per QALY saved"* ([PMID: 22886057](https://pubmed.ncbi.nlm.nih.gov/22886057/)); only a 20–25% reduction in LS/PTA incidence would be required for cost-effectiveness. The main preventable drivers are diagnostic delay and inadequate antibiotic coverage; restricted or inappropriate antibiotic use (macrolides, narrow cephalosporins, to which *F. necrophorum* may be resistant) for pharyngitis is linked to rising incidence ([PMID: 12109395](https://pubmed.ncbi.nlm.nih.gov/12109395/), [PMID: 20570017](https://pubmed.ncbi.nlm.nih.gov/20570017/)). Early radiographic recognition of impending LS enables timely intervention ([PMID: 39840169](https://pubmed.ncbi.nlm.nih.gov/39840169/)).

### Finding 11 — Temporal course: acute onset, rapid progression, self-limited with treatment

The temporal course is acute/subacute onset days after pharyngitis, rapid progression to sepsis, but self-limited with treatment (no chronic/relapsing course). The classic sequence is antecedent sore throat/pharyngitis, then within roughly one week the development of IJV thrombophlebitis and septic emboli. Imaging can capture striking speed: *"Within four days, the infection rapidly progressed to complete occlusion of the internal jugular vein with pulmonary septic emboli"* ([PMID: 39840169](https://pubmed.ncbi.nlm.nih.gov/39840169/)). The pre-antibiotic natural history was often fatal within 7–15 days ([PMID: 40265142](https://pubmed.ncbi.nlm.nih.gov/40265142/)). With appropriate therapy the illness is self-limited/curable—there is no lifelong or relapsing course—though recovery requires prolonged (weeks-long) antibiotics; thrombus resolves or recanalizes in ~78% of cases on follow-up imaging: *"Thrombosis resolved or recanalized in 78% of cases on follow-up imaging"* ([PMID: 42141231](https://pubmed.ncbi.nlm.nih.gov/42141231/)). Onset is typically in previously healthy adolescents/young adults (median ~15–20 years); it is not congenital.

### Finding 12 — Evidence gap: human thrombus-initiation step is inferred

The platelet-aggregation/thrombus-initiation step in human Lemierre pathophysiology is inferred, not directly demonstrated. Reviews list hemagglutinin and platelet-aggregating/hemolytic activity among *F. necrophorum* virulence factors implicated in thrombus formation, but candidly note that *"The pathogenic mechanism of F. necrophorum is complex and not well defined"* ([PMID: 16701574](https://pubmed.ncbi.nlm.nih.gov/16701574/), [PMID: 8711893](https://pubmed.ncbi.nlm.nih.gov/8711893/)). Direct experimental demonstration of *F. necrophorum*-driven platelet aggregation causing IJV thrombosis in humans was not identified in this review; the strongest mechanistic data (leukotoxin-mediated leukocyte apoptosis) derive from ruminant/in-vitro systems ([PMID: 12117974](https://pubmed.ncbi.nlm.nih.gov/12117974/)). No human transcriptomic/proteomic/metabolomic disease signatures are available.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Oropharyngeal colonization/infection** by *F. necrophorum* (usually acute tonsillitis/pharyngitis or peritonsillar abscess; alternatively odontogenic or otogenic foci) **leads to** local mucosal invasion. *(Well supported — PMID 42127655, 12109395.)*
2. Local invasion **results in** direct/contiguous spread into the peritonsillar and parapharyngeal soft tissues and the adjacent carotid sheath. *(Well supported anatomically — PMID 42517948.)*
3. Bacterial **leukotoxin and endotoxin (LPS)** activate polymorphonuclear leukocytes and then kill phagocytes by apoptosis/necrosis, **enabling immune evasion** and unchecked local proliferation. *(Mechanism demonstrated in vitro/ruminant models — PMID 12117974, 8711893.)*
4. Endothelial injury plus procoagulant activity (hemagglutinin, platelet-aggregating and hemolytic factors) **is inferred to lead to** septic thrombophlebitis of the internal jugular vein. *(INFERRED in humans — the platelet-aggregation/thrombus-initiation step is not directly demonstrated; PMID 16701574, 8711893, Finding 12.)*
5. IJV septic thrombophlebitis **results in** bacteremia and shedding of infected thrombus fragments → **metastatic septic emboli**, most commonly to the lungs (cavitary consolidations, empyema), and less often to joints, intracranial venous sinuses, and orbit. *(Well supported — PMID 20570017, 42141231.)*
6. Systemic bacteremia and embolization **lead to** sepsis (~83%), thrombocytopenia (~75%), and, in severe cases, septic shock (~18%), DIC, and ARDS. *(Well supported — PMID 31843654, 42517948.)*
7. **Branch:** with prompt anaerobe-active antibiotics ± source control, the process is **self-limited**, thrombus recanalizes (~78%), and mortality is ~5%; **without** timely therapy, the historical course was fatal within 7–15 days (mortality up to 80%). *(Well supported — PMID 40265142, 42141231, 39840169.)*

```
 Oropharyngeal infection (F. necrophorum)
            │  leukotoxin + endotoxin → PMN killing / immune evasion
            ▼
 Contiguous spread to carotid sheath
            │  endothelial injury + (inferred) platelet aggregation
            ▼
 Internal jugular vein SEPTIC THROMBOPHLEBITIS ──► bacteremia
            │                                          │
            ▼                                          ▼
 Septic emboli → LUNGS (dominant)          Sepsis / thrombocytopenia
   also: joints, sinuses, orbit, pleura     → septic shock / DIC / ARDS
            │
            ▼
   ┌───────────────┬───────────────────────────┐
   │ Treated       │ Untreated (historical)     │
   │ ~5% mortality │ ~80% mortality, 7–15 days  │
   │ 78% recanalize│                            │
   └───────────────┴───────────────────────────┘
```

**Upstream vs downstream:** The pathogen's leukotoxin/endotoxin-mediated immune subversion is the upstream driver; IJV thrombosis is the pivotal intermediate lesion; septic emboli and multi-organ failure are downstream consequences. **Cell types / processes:** neutrophils (CL:0000775) and other phagocytes are killed by leukotoxin (GO:0006915 apoptotic process; GO:0006954 inflammatory response); vascular endothelium (CL:0000115) and platelets (CL:0000233) participate in thrombus formation (GO:0007596 blood coagulation). Because the human disease is an acquired infection, there are no host causal genes, pathways (Wnt/MAPK/mTOR/PI3K-AKT), epigenetic changes, or heritable protein dysfunctions to annotate; the relevant molecular apparatus is bacterial.

---

## Not Applicable / Not Available Sections (explicit)

Because Lemierre syndrome is an **acquired infectious disease with no genetic etiology**, the following template items are Not Applicable and should be recorded as such in the knowledge base:

| Template section | Status | Rationale |
|---|---|---|
| Causal genes / OMIM gene entries | **Not Applicable** | No human causal gene; not Mendelian |
| Pathogenic variants / ACMG classification / gnomAD allele frequency | **Not Applicable** | No heritable disease variants |
| Modifier genes, epigenetic changes, chromosomal abnormalities | **Not Applicable** | No genetic disease architecture |
| Inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effects, consanguinity, carrier frequency | **Not Applicable** | Non-genetic |
| Genetic testing (WGS/WES/panels/single-gene/CMA/karyotype/FISH/mtDNA/repeat expansion) | **Not Applicable** | Diagnosis is microbiological + imaging |
| Genetic counseling / carrier & prenatal screening | **Not Applicable** | Non-heritable |
| Pharmacogenomics | **Not Available** | No PGx associations described for LS antibiotics in this context |
| Gene/cell/RNAi/CRISPR functional-genomics screens; human omics signatures | **Not Available** | No human transcriptomic/proteomic/metabolomic disease datasets identified |

The scientifically meaningful "genetics" of this disease reside in the **pathogen genome**—the *F. necrophorum* leukotoxin operon (*lktA*) and the hemagglutinin-related protein gene, both confirmed by PCR and Southern hybridization in virulent isolates ([PMID: 24590666](https://pubmed.ncbi.nlm.nih.gov/24590666/)).

---

## Section-by-Section Digest

- **1. Disease information:** MONDO:0015306; synonyms include necrobacillosis (human), postanginal sepsis, human necrobacillosis, "the forgotten disease." Information is derived from aggregated case series/systematic reviews and individual case reports (there is no large EHR-based cohort; the BATTLE registry, [PMID: 33091703](https://pubmed.ncbi.nlm.nih.gov/33091703/), is assembling disease-specific data).
- **2. Etiology:** Infectious (predominantly *F. necrophorum*; expanding to streptococci and *S. aureus*). Risk factors: antecedent pharyngotonsillitis/peritonsillar abscess, young age, male sex, and inappropriate/restricted antibiotic use for sore throat. Smoking is an established risk factor for peritonsillar abscess (the main precursor). No genetic risk/protective factors; no established gene-environment interaction.
- **3. Phenotypes:** Fever (92%), sore throat, neck pain/swelling, rigors, dyspnea, pleuritic chest pain, hemoptysis; laboratory: thrombocytopenia (~75%), elevated CRP, leukocytosis. Onset is acute in previously healthy young people; severity moderate-to-severe; course rapidly progressive then resolving with treatment.
- **4. Genetic/molecular:** Not Applicable (see table above).
- **5. Environmental/infectious agents:** *Fusobacterium necrophorum* subsp. *necrophorum* (biotype A, more virulent) and subsp. *funduliforme*; viridans streptococci; MRSA (Lemierre-like). No toxin/pollution etiology.
- **6. Mechanism:** See causal chain above.
- **7. Anatomy:** oropharynx/tonsils → internal jugular vein → lungs (dominant), with intracranial-sinus, pleural, joint, and orbital extension.
- **8. Temporal:** acute/subacute onset days after pharyngitis; rapid progression; self-limited with treatment; no chronic/relapsing phase.
- **9. Inheritance/population:** No inheritance. Incidence ~1–10/million/year (rising); median age ~15–20 years; male predominance; global distribution.
- **10. Diagnostics:** contrast-enhanced neck/chest CT (IJV thrombosis + emboli) + anaerobic blood cultures; molecular (16S rDNA, targeted NGS/metagenomics); differential includes other deep-neck-space infections, viral pharyngitis, infectious mononucleosis, and non-septic venous thrombosis.
- **11. Prognosis:** ~5% mortality (up to 80% historically); high acute morbidity; near-complete recovery with treatment; prognostic factors—diagnostic delay, septic shock, and extent of embolization.
- **12. Treatment:** prolonged anaerobe-active antibiotics (beta-lactam/BLI or 3rd-gen cephalosporin + metronidazole, or carbapenem) + source control; anticoagulation controversial; IJV ligation/excision as salvage.
- **13. Prevention:** secondary (early recognition + appropriate antibiotics); cost-effective throat-swab screening modeled but not implemented; no human vaccine.
- **14. Other species:** major veterinary disease (bovine liver abscess, footrot; necrobacillosis in ruminants and wildlife); zoonotic transmission not a feature of human LS.
- **15. Model organisms:** no dedicated rodent LS model; mechanistic work uses bovine PMN/leukocyte in-vitro systems and cattle field trials; a *F. necrophorum* bacterin vaccine is efficacious in cattle.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [42127655](https://pubmed.ncbi.nlm.nih.gov/42127655/) | *Pediatric Lemierre's syndrome: A systematic review* | Dominant pathogen (78.3%), CT utility (89.5%), fever (92%), complications 4.2%, anticoagulation 62.2% |
| [41517763](https://pubmed.ncbi.nlm.nih.gov/41517763/) | *Early diagnosis using targeted NGS + metagenomics* | Definition; molecular diagnostics for culture-negative cases |
| [31843654](https://pubmed.ncbi.nlm.nih.gov/31843654/) | *Invasive F. necrophorum incl. LS: Swedish 8-year study* | Rising incidence (2.9→5.0/M/yr); severity metrics; median age 20 |
| [42576194](https://pubmed.ncbi.nlm.nih.gov/42576194/) | *Atypical LS in a child with nephrotic syndrome* | Incidence estimate 3.6/million |
| [40265142](https://pubmed.ncbi.nlm.nih.gov/40265142/) | *A subtle presentation: Lemierre* | Historical 80% / modern ~5% mortality; 7–15 day course |
| [8711893](https://pubmed.ncbi.nlm.nih.gov/8711893/) | *F. necrophorum virulence factors* | Leukotoxin + endotoxin as principal virulence factors |
| [12117974](https://pubmed.ncbi.nlm.nih.gov/12117974/) | *Leukotoxin induces activation/apoptosis of bovine leukocytes* | Mechanism of immune evasion (in-vitro/ruminant) |
| [16701574](https://pubmed.ncbi.nlm.nih.gov/16701574/) | *F. necrophorum infections in animals* | Subspecies virulence; veterinary disease; "mechanism not well defined" |
| [39840169](https://pubmed.ncbi.nlm.nih.gov/39840169/) | *Early Radiographic Warning Signs* | Confirmatory diagnostic standard; 4-day rapid progression |
| [40224244](https://pubmed.ncbi.nlm.nih.gov/40224244/) | *LS in an immunocompetent patient* | First-line antibiotic regimen; contrast-enhanced CT |
| [32909436](https://pubmed.ncbi.nlm.nih.gov/32909436/) | *Anticoagulation strategies: systematic review* | Anticoagulation controversy |
| [42141231](https://pubmed.ncbi.nlm.nih.gov/42141231/) | *Otogenic pediatric septic thrombophlebitis* | Thrombosis distribution; 78% recanalization |
| [20570017](https://pubmed.ncbi.nlm.nih.gov/20570017/) | *"A forgotten disease"* | Oropharyngeal source + pulmonary emboli; carbapenems |
| [38363930](https://pubmed.ncbi.nlm.nih.gov/38363930/) | *Lemierre-like syndrome after MRSA soft-tissue infection* | Expanding etiologic spectrum; ~16% LLS mortality |
| [42286749](https://pubmed.ncbi.nlm.nih.gov/42286749/) | *Incomplete Lemierre's syndrome* | Clinical variant definition |
| [42517948](https://pubmed.ncbi.nlm.nih.gov/42517948/) | *IJV excision in uncontrolled LS* | Odontogenic/non-Fusobacterium cases; salvage surgery; DIC/ARDS |
| [22886057](https://pubmed.ncbi.nlm.nih.gov/22886057/) | *Cost-effectiveness of throat-swab screening* | Secondary prevention economics ($8,795/QALY) |
| [16363327](https://pubmed.ncbi.nlm.nih.gov/16363327/) | *Vaccination against F. necrophorum in feedlot cattle* | Bacterin efficacy (liver abscess OR 0.27; footrot OR 0.18) |
| [24590666](https://pubmed.ncbi.nlm.nih.gov/24590666/) | *Fusobacterium isolates from white-tailed deer* | Leukotoxin operon confirmation; wildlife reservoir |
| [12109395](https://pubmed.ncbi.nlm.nih.gov/12109395/) | *Postanginal sepsis in South West Peninsula* | Otogenic sources; antibiotic-use link to rising incidence |
| [39257960](https://pubmed.ncbi.nlm.nih.gov/39257960/) | *LS with extensive thrombosis* | Surgical hierarchy; anticoagulation for extensive thrombosis |
| [33091703](https://pubmed.ncbi.nlm.nih.gov/33091703/) | *BATTLE registry rationale* | Registry to address evidence gaps; broadened definition |
| [28260599](https://pubmed.ncbi.nlm.nih.gov/28260599/) | *Peritonsillar abscess microbiology & risk factors* | Smoking as PTA risk factor; FN prevalence in the precursor lesion |
| [42547547](https://pubmed.ncbi.nlm.nih.gov/42547547/) | *Microbiological spectrum of peritonsillar abscesses* | FN more common in adolescents; antibiotic susceptibility |

---

## Limitations and Knowledge Gaps

1. **Mechanistic gap (human thrombogenesis):** The step linking *F. necrophorum* virulence factors to actual IJV thrombus initiation in humans is inferred from in-vitro and ruminant data; direct human evidence of platelet aggregation/endothelial thrombus formation is lacking (Finding 12).
2. **No human omics:** No transcriptomic, proteomic, metabolomic, single-cell, or spatial datasets exist for human LS, limiting molecular annotation and biomarker discovery.
3. **Evidence quality:** The literature is dominated by case reports, retrospective series, and systematic reviews of heterogeneous cases; there are no randomized trials for the central management controversy (anticoagulation).
4. **Definitional drift:** "Lemierre-like" and "incomplete" variants broaden the disease boundary and complicate epidemiologic comparisons; incidence estimates vary (1–10/million/year).
5. **Underdiagnosis/publication bias:** As "the forgotten disease," LS may be under-recognized (biasing incidence downward) while severe/unusual cases are over-represented in the literature (biasing severity upward).
6. **No dedicated small-animal model:** Mechanistic study relies on cattle/bovine leukocyte systems, which may not fully recapitulate human neck-vein thrombophlebitis.

---

## Proposed Follow-up Actions

1. **Contribute to / mine the BATTLE registry** ([PMID: 33091703](https://pubmed.ncbi.nlm.nih.gov/33091703/)) for prospective, standardized data on presentation, management, and anticoagulation outcomes.
2. **Design a pragmatic RCT of adjunctive anticoagulation** in confirmed LS, stratified by extent of thrombosis and intracranial-sinus involvement, to resolve the central management controversy.
3. **Human mechanistic studies:** ex-vivo assays testing *F. necrophorum* leukotoxin, hemagglutinin, and outer-membrane factors against human platelets and jugular-vein endothelial cells to directly test the thrombus-initiation hypothesis (closing the Finding 12 gap).
4. **Molecular diagnostics validation:** prospective evaluation of targeted NGS/16S rDNA turnaround time and sensitivity versus anaerobic culture, to shorten diagnostic delay (the key modifiable prognostic factor).
5. **Prospective evaluation of throat-swab screening** in 15–24-year-olds for *F. necrophorum* pharyngitis to test the modeled cost-effectiveness ([PMID: 22886057](https://pubmed.ncbi.nlm.nih.gov/22886057/)) as a secondary-prevention strategy.
6. **Comparative-biology translation:** leverage the efficacious bovine *F. necrophorum* bacterin ([PMID: 16363327](https://pubmed.ncbi.nlm.nih.gov/16363327/)) and leukotoxin biology to explore antitoxin/antivirulence adjuncts, while recognizing the low human incidence limits vaccine feasibility.

---

## Suggested Ontology Term Set (for knowledge-base ingestion)

- **Disease:** MONDO:0015306 (Lemierre syndrome)
- **Pathogen / animal (NCBI Taxon):** *Fusobacterium necrophorum* txid859; *Bos taurus* txid9913; *Odocoileus virginianus* txid9874
- **Anatomy (UBERON):** internal jugular vein UBERON:0001584; oropharynx UBERON:0001729; palatine tonsil UBERON:0002373; lung UBERON:0002048; sigmoid sinus UBERON:0006459; cavernous sinus UBERON:0004024
- **Phenotypes (HP):** Fever HP:0001945; Sepsis HP:0100806; Thrombocytopenia HP:0001873; Septic shock HP:0031273; Hemoptysis HP:0002105; Chest pain HP:0100749
- **Processes (GO):** inflammatory response GO:0006954; apoptotic process GO:0006915; blood coagulation GO:0007596; toxin activity GO:0090729
- **Cells (CL):** neutrophil CL:0000775; endothelial cell CL:0000115; platelet CL:0000233
- **Chemicals (CHEBI):** lipopolysaccharide CHEBI:16412; metronidazole CHEBI:6077
- **Interventions (NCIT-type):** antibacterial therapy; metronidazole; carbapenem; anticoagulant therapy; abscess drainage; internal jugular vein ligation

*Evidence source types across this report: predominantly **human clinical** (case series, systematic reviews, registries); **in-vitro/model-organism** for virulence mechanism (bovine leukocytes, cattle field trials); **computational/economic** for prevention modeling. No germline-genetic or human-omics evidence exists for this disease.*


## Artifacts

- [OpenScientist final report](Lemierre_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Lemierre_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 20 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 16 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0001584` (3 mentions) - the report calls it "internal jugular vein", "Internal jugular vein"; UBERON calls it **left subclavian artery**
- `CHEBI:6077` (2 mentions) - the report calls it "metronidazole"; CHEBI calls it **Ivalin**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0031273` (2 mentions) - the report calls it "Septic shock"; HP calls it **Shock**
- `HP:0002098` (1 mention) - the report calls it "Respiratory distress/dyspnea"; HP calls it **Respiratory distress**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0001584` - called "internal jugular vein", "Internal jugular vein"