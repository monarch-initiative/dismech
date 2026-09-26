---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T18:50:52.710606'
end_time: '2026-09-25T19:08:07.374810'
duration_seconds: 1034.66
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Infectious Discitis
  mondo_id: MONDO:8000000
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
citation_count: 45
reference_validation:
  total_references: 45
  verified: 45
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 45
  on_topic: 18
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 21
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 12
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0032243
    reported_labels:
    - Bacteremia
    ontology_label: Abnormal tissue metabolite concentration
  - term_id: UBERON:0006678
    reported_labels:
    - Primary structures:** intervertebral disc
    ontology_label: foramen secundum
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Infectious_Discitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Infectious_Discitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Infectious Discitis
- **MONDO ID:** MONDO:8000000 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Infectious Discitis** covering all of the
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

# Infectious Discitis (Spondylodiscitis): A Comprehensive Disease-Characteristics Report

**Disease:** Infectious Discitis / Spondylodiscitis
**Category:** Infectious Disease
**Proposed MONDO:** the template-supplied MONDO:8000000 is a placeholder; the closest resolvable concepts are spondylitis/osteomyelitis of the spine (no distinct Mendelian entry)
**Evidence base:** 14 confirmed findings, 65 papers reviewed across 5 investigation iterations

---

## Summary

Infectious discitis — more precisely termed **spondylodiscitis** or **disco-vertebral infection** — is an acquired microbial infection of the intervertebral disc and the two adjacent vertebral endplates/bodies. It is fundamentally **not a genetic disease**: there are no causal genes, pathogenic germline variants, inheritance patterns, or heritable susceptibility loci. Consequently, all template sections concerning causal genes, ACMG variant classification, chromosomal abnormalities, inheritance, penetrance, carrier frequency, and genetic screening are **not applicable** and are marked as such below. The disease is driven overwhelmingly by **hematogenous seeding of *Staphylococcus aureus***, with a well-defined anatomical causal chain: bacteremia → seeding of the vascularized vertebral endplate → vertebral osteomyelitis → spread across the endplate into the avascular disc (discitis) → paravertebral/psoas and epidural abscess → spinal cord/root compression → neurologic deficit, deformity, sepsis, and death.

Epidemiologically the disease is a **rising-incidence condition of the aging population**. German population data show the age-adjusted incidence roughly doubled (5.4 → 11.0 per 100,000, +104%, p<0.001) between 2005 and 2021, and Korean nationwide data show a 1.5-fold rise (22.90 → 35.79 per 100,000) from 2010–2019, with a simultaneous shift away from tuberculous toward pyogenic disease. The lumbar spine is most commonly affected (~51%), and the elderly (≥60y) constitute ~48% of cases. A distinct, generally milder **pediatric form** peaks at 0.5–4 years of age. Key risk factors are immunocompromise, bacteremic sources (endocarditis, IV drug use, hemodialysis), diabetes, and prior spinal instrumentation; malnutrition and substance-use disorder are emerging drivers.

Management rests on **contrast-enhanced whole-spine MRI plus microbiological confirmation** (blood cultures and image-guided disc/vertebral biopsy) supported by elevated CRP/ESR, and increasingly on **18F-FDG PET/CT** and **metagenomic next-generation sequencing (mNGS)** for inconclusive imaging and culture-negative disease (culture-negative rate ~43%). A landmark randomized trial established that **6 weeks of pathogen-directed antibiotics is non-inferior to 12 weeks**, with surgery reserved for instability, neurologic deficit, abscess, or medical failure. Prognosis is generally favorable (in-hospital mortality ~7%) but morbidity is substantial: 20–30% residual disability, 6–17% recurrence, and markedly worse outcomes with extensive epidural abscess, concurrent infection, thoracic involvement, and concomitant infective endocarditis.

---

## Section 1 — Disease Information

**Overview.** Infectious discitis is an infection localized to the intervertebral disc that, in adults, almost always co-involves the adjacent vertebral endplates and bodies — hence the umbrella terms *spondylodiscitis*, *disco-vertebral infection*, *native vertebral osteomyelitis (NVO)*, and *pyogenic vertebral osteomyelitis (PVO)*. It is a devastating invasive infection that can lead to debilitating pain, motor weakness, or paralysis even with appropriate treatment ([PMID: 40429472](https://pubmed.ncbi.nlm.nih.gov/40429472/)).

**Key identifiers.**
- **ICD-10:** M46.4 (Discitis, unspecified); M46.3– (Infection of intervertebral disc, pyogenic); tuberculous spondylitis A18.01 / M49.0.
- **ICD-11:** FA83 (Infective spondylopathies).
- **MeSH:** *Discitis* (D053161); *Spondylitis*; *Osteomyelitis*.
- **MONDO:** the supplied MONDO:8000000 is a placeholder; closest resolvable concepts are spondylitis/osteomyelitis of spine (not a distinct Mendelian entry).
- **OMIM / Orphanet:** Not applicable — this is an acquired infection, not a Mendelian or rare genetic disorder, with no dedicated OMIM entry.

**Synonyms:** spondylodiscitis, disco-vertebral infection, discitis, infective/infectious discitis, pyogenic vertebral osteomyelitis, native vertebral osteomyelitis, septic discitis.

**Information source:** Aggregated disease-level resources — nationwide registries (German EANS Spine, Korean NHIS), systematic reviews/meta-analyses, and society guidelines (IDSA 2015, SPILF 2022) — supplemented by EHR-derived single-center cohorts.

---

## Section 2 — Etiology

**Primary cause: infectious.** ***Staphylococcus aureus* is the predominant organism** in pyogenic disease. In a comparative series of 114 cases, pyogenic disease accounted for 78% (TB 16%, brucellar 6%), with *S. aureus* the causative agent in most pyogenic cases ([PMID: 41882873](https://pubmed.ncbi.nlm.nih.gov/41882873/)). The pathogen spectrum **shifts with age and site**: in German nationwide 2024 data (10,801 cases), *Staphylococcus* spp. prevalence declined with increasing age (35.7% → 21.3%, p<0.001) while *Enterococcus* (3.9% → 11.8%) and Enterobacterales (17.3% → 21.4%) rose, and lumbar sites carried more Enterobacterales/Enterococcus ([PMID: 42778058](https://pubmed.ncbi.nlm.nih.gov/42778058/)). *S. aureus* bacteremia metastasizes to the spine as spondylodiscitis in ~20% of cases ([PMID: 41905317](https://pubmed.ncbi.nlm.nih.gov/41905317/)).

**Risk factors (environmental/acquired).** Established factors include intravenous drug use, hemodialysis, prior spinal surgery, diabetes, chronic kidney/liver disease, prior invasive procedures, and bacteremia ([PMID: 40429472](https://pubmed.ncbi.nlm.nih.gov/40429472/); [PMID: 42262500](https://pubmed.ncbi.nlm.nih.gov/42262500/)). Community-acquired and persistent *S. aureus* bacteremia increased metastatic infection risk **7.6-fold and 4.8-fold** respectively ([PMID: 41905317](https://pubmed.ncbi.nlm.nih.gov/41905317/)). Substance-use disorder rose >3-fold within spinal-infection cohorts, paralleling a ~40% rise in spinal infections in Washington State ([PMID: 30059485](https://pubmed.ncbi.nlm.nih.gov/30059485/)). **Malnutrition/hypoalbuminemia** independently predicted in-hospital mortality and 90-day readmission ([PMID: 39773279](https://pubmed.ncbi.nlm.nih.gov/39773279/)).

**Genetic risk / protective factors:** Not applicable — no established causal variants, susceptibility loci, or protective alleles. **Protective factors** are environmental: control of bacteremic sources, glycemic control, nutritional optimization, and aseptic surgical technique.

**Gene–environment interactions:** Not applicable in a Mendelian sense; host immune competence (diabetes, immunosuppression, ESRD) modulates susceptibility to a purely exogenous infectious exposure.

---

## Section 3 — Phenotypes

| Phenotype | Type | Frequency | Suggested HPO |
|---|---|---|---|
| Back/spinal pain | Symptom | 78–85% | HP:0003418 (Back pain) |
| Fever | Sign | 29–76% | HP:0001945 (Fever) |
| Elevated CRP | Lab abnormality | ~95% | HP:0011227 (Elevated CRP) |
| Bacteremia | Lab/sign | ~76% | HP:0032243 (Bacteremia) |
| Elevated ESR | Lab abnormality | high (78% sens. in children) | HP:0003565 (Elevated ESR) |
| Motor weakness / paralysis | Sign | variable | HP:0001324 (Muscle weakness) |
| Refusal to walk/stand/sit (pediatric) | Behavioral/sign | 49.8% (children) | gait abnormality |
| Altered mobility | Sign | ~33% | HP:0002540 |

Typical adult presentation: back pain (78%), fever (76%), elevated CRP (95%), bacteremia (76%) ([PMID: 30002914](https://pubmed.ncbi.nlm.nih.gov/30002914/)); in a Scottish cohort back pain 84.7%, altered mobility 33.3%, fever 29.2%, lumbar involvement 51.4% ([PMID: 35904356](https://pubmed.ncbi.nlm.nih.gov/35904356/)). **Onset** is typically subacute/insidious; **severity** is variable; **progression** is progressive if untreated. **Quality of life** is impaired by chronic pain and, in a minority, permanent neurologic disability. Pediatric presentation is dominated by back pain (37.97%) and refusal to walk/stand/sit (49.79%) ([PMID: 33396379](https://pubmed.ncbi.nlm.nih.gov/33396379/)).

---

## Section 4 — Genetic/Molecular Information

**Not applicable — acquired infectious disease.** There are **no causal genes, pathogenic germline/somatic variants, modifier genes, disease-specific epigenetic signatures, or chromosomal abnormalities**. The relevant "molecular" biology is that of the **pathogen**, principally *S. aureus* virulence and biofilm regulation (see Section 6). In a USA300 MRSA implant-osteomyelitis model, the **msaABCR operon** regulated biofilm formation, capsule, protease, persister cells, and cell-wall integrity; wild-type caused severe bone necrosis with sequestra and multinucleated osteoclasts, whereas the msaABCR mutant was attenuated ([PMID: 33109085](https://pubmed.ncbi.nlm.nih.gov/33109085/)). Host genetic susceptibility loci are not established for this condition.

---

## Section 5 — Environmental Information

**Environmental/iatrogenic factors:** spinal surgery and invasive procedures (direct inoculation), indwelling vascular catheters, hemodialysis access. **Lifestyle factors:** intravenous drug use and substance-use disorder ([PMID: 30059485](https://pubmed.ncbi.nlm.nih.gov/30059485/)); poor nutritional status ([PMID: 39773279](https://pubmed.ncbi.nlm.nih.gov/39773279/)).

**Infectious agents (NCBI Taxonomy):**
- ***Staphylococcus aureus*** (txid1280) — predominant pyogenic agent.
- **Enterobacterales** (e.g., *Escherichia coli* txid562) and ***Enterococcus*** spp. (txid1350) — increasing in the elderly and at lumbar sites ([PMID: 42778058](https://pubmed.ncbi.nlm.nih.gov/42778058/)).
- ***Mycobacterium tuberculosis*** (txid1773) — tuberculous spondylitis (Pott disease), declining in incidence but endemic regionally.
- ***Brucella*** spp. (txid234) — brucellar spondylodiscitis in pastoral/endemic areas.
- **Fungi** (*Aspergillus*, *Blastomyces*, *Candida*) — rare, in immunocompromised hosts.
- **Anaerobes** (e.g., *Cutibacterium acnes*, vaginal anaerobes) — implicated in low-grade and culture-negative disease, often requiring molecular detection ([PMID: 42611158](https://pubmed.ncbi.nlm.nih.gov/42611158/)).

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Bacteremia** (from skin, IV drug use, endocarditis, urinary, dental, or procedural source) **leads to** circulating pathogen reaching spinal vasculature.
2. Bloodborne organisms **seed the vascular vertebral endplate** (richly perfused via Batson's venous plexus / segmental arteries) — *hematogenous route is dominant* ([PMID: 26700630](https://pubmed.ncbi.nlm.nih.gov/26700630/)).
3. Seeding **results in vertebral body osteomyelitis** with local proliferation.
4. Infection **spreads across the endplate into the avascular disc**, producing **discitis** (the disc has poor immune surveillance, favoring persistence).
5. Bacterial virulence and **biofilm formation lead to** bone destruction via **two branching mechanisms**: (a) host **osteoclast-mediated resorption** driven by inflammatory cytokines, and (b) **direct biofilm acidification/dissolution** of bone independent of host immunity ([PMID: 33109085](https://pubmed.ncbi.nlm.nih.gov/33109085/); [PMID: 28076372](https://pubmed.ncbi.nlm.nih.gov/28076372/)).
6. Local **inflammatory cytokines (IL-1β, TNF-α, IL-6)** and **microthrombosis** amplify tissue injury and impair vertebral/disc blood supply ([PMID: 18246002](https://pubmed.ncbi.nlm.nih.gov/18246002/); [PMID: 32775107](https://pubmed.ncbi.nlm.nih.gov/32775107/)).
7. Progression **results in paravertebral/psoas and epidural abscess** formation.
8. Abscess and bony destruction **lead to spinal cord/nerve-root compression, vertebral collapse and deformity**.
9. Endpoint: **neurologic deficit, sepsis, and death** — "any delay in diagnosis and treatment can lead to significant spinal cord injury, permanent neurological damage, septicemia, and death" ([PMID: 35706345](https://pubmed.ncbi.nlm.nih.gov/35706345/)). Epidural abscess extending ≥3 segments raised lethality (HR 4.72, 95%CI 1.57–14.20, p=0.006) ([PMID: 35657387](https://pubmed.ncbi.nlm.nih.gov/35657387/)).

```
 Bacteremia ──► endplate seeding ──► vertebral osteomyelitis ──► disc invasion (discitis)
                                             │
                    ┌────────────────────────┴───────────────────────┐
             osteoclast resorption                          biofilm acidification
             (cytokine-driven)                              (host-independent)
                    └────────────────────────┬───────────────────────┘
                                    bone/disc destruction
                                             │
                          paravertebral/psoas + epidural abscess
                                             │
                       cord/root compression, collapse, deformity
                                             │
                          neurologic deficit · sepsis · death
```

**Molecular/cellular processes:** NF-κB–driven inflammation, cytokine cascades (IL-1β, TNF-α, IL-6), osteoclastogenesis (RANKL axis inferred), neutrophil recruitment, microthrombosis. **Upstream** events are bacteremia and endplate seeding; **downstream** are abscess, compression, and systemic sepsis.

**Suggested ontology terms:** GO:0006954 (inflammatory response), GO:0045124 (regulation of bone resorption), GO:0042116 (macrophage activation), GO:0006935 (chemotaxis); CL:0000092 (osteoclast), CL:0000062 (osteoblast), CL:0000775 (neutrophil); CHEBI:16412 (lipopolysaccharide).

---

## Section 7 — Anatomical Structures Affected

- **Primary structures:** intervertebral disc (UBERON:0006678) and adjacent **vertebral endplates/bodies** (UBERON:0002412 vertebral column). **Lumbar spine most commonly affected (~51%)** ([PMID: 35904356](https://pubmed.ncbi.nlm.nih.gov/35904356/)); L7–S1 in canine analogues.
- **Secondary involvement:** epidural space (epidural abscess), psoas/paravertebral muscles (psoas abscess), spinal cord (UBERON:0002240) and nerve roots (compression), bloodstream (sepsis), and heart valves (concurrent infective endocarditis).
- **Body systems:** musculoskeletal (primary), nervous (secondary compression), cardiovascular (bacteremia/endocarditis source).
- **Tissue/cell level:** cartilaginous/fibrocartilaginous disc (nucleus pulposus, annulus fibrosus), trabecular bone, endothelium. Cell types: osteoclasts (CL:0000092), osteoblasts (CL:0000062), neutrophils (CL:0000775), nucleus pulposus cells.
- **Subcellular:** bacterial intracellular persistence and biofilm on bone/implant surfaces; cytoplasmic inflammasome activation (GO:0005737 cytoplasm).
- **Localization/lateralization:** typically midline/bilateral involving two contiguous vertebrae and the interposed disc; abscesses may be asymmetric (unilateral psoas).

---

## Section 8 — Temporal Development

- **Onset:** subacute to insidious in adults; median symptom duration before diagnosis is often weeks. A distinct **pediatric form peaks at 0.5–4 years** ([PMID: 33396379](https://pubmed.ncbi.nlm.nih.gov/33396379/)).
- **Progression:** progressive if untreated — from discitis to abscess and neurologic compromise. Bimodal age distribution (pediatric vs adult/elderly).
- **Course/duration:** the **pediatric form is frequently benign/self-limiting** but risks deformity/neurologic complications if diagnosis is delayed ([PMID: 36000507](https://pubmed.ncbi.nlm.nih.gov/36000507/)); the **adult/elderly form predominates and carries higher mortality** ([PMID: 37384614](https://pubmed.ncbi.nlm.nih.gov/37384614/)).
- **Critical intervention window:** early antibiotics and, when indicated, **timely surgery (≤14 days)** significantly improve survival (see Section 11).

---

## Section 9 — Inheritance and Population (Epidemiology)

**Epidemiology (rising incidence).** German population-based data (2005–2021): age-adjusted incidence rose **104%, from 5.4 to 11.0 per 100,000 (p<0.001)**, with inpatient mortality up 347% ([PMID: 37980371](https://pubmed.ncbi.nlm.nih.gov/37980371/)). Korean nationwide data (2010–2019): infectious spondylodiscitis rose **1.5-fold from 22.90 to 35.79 per 100,000**; pyogenic rose 15.35 → 33.75 while tuberculous fell 7.55 → 2.04 per 100,000; elderly ≥60y = **47.6%** of cases; mean age 58y ([PMID: 37384614](https://pubmed.ncbi.nlm.nih.gov/37384614/)).

| Metric | Value | Source |
|---|---|---|
| German incidence 2005 → 2021 | 5.4 → 11.0 / 100,000 (+104%) | [PMID: 37980371](https://pubmed.ncbi.nlm.nih.gov/37980371/) |
| Korean incidence 2010 → 2019 | 22.90 → 35.79 / 100,000 (1.5×) | [PMID: 37384614](https://pubmed.ncbi.nlm.nih.gov/37384614/) |
| Elderly (≥60y) share | 47.6% | [PMID: 37384614](https://pubmed.ncbi.nlm.nih.gov/37384614/) |
| Lumbar involvement | ~51% | [PMID: 35904356](https://pubmed.ncbi.nlm.nih.gov/35904356/) |
| Pediatric peak age | 0.5–4 years | [PMID: 33396379](https://pubmed.ncbi.nlm.nih.gov/33396379/) |

**Sex ratio:** male predominance in adults (and in canine analogues); pediatric series show near-equal (F:M 1.3:1) ([PMID: 31848723](https://pubmed.ncbi.nlm.nih.gov/31848723/)). **Geographic variation:** tuberculous and brucellar forms concentrate in endemic/pastoral regions; pyogenic disease predominates in high-income aging populations.

**Inheritance, penetrance, expressivity, anticipation, mosaicism, founder effects, consanguinity, carrier frequency:** **All Not Applicable** — acquired infectious disease with no genetic transmission.

---

## Section 10 — Diagnostics

**Imaging.** **Contrast-enhanced MRI is the modality of choice** (87–100% of specialists) and should cover the **entire spine in ≥2 orthogonal planes** ([PMID: 36894008](https://pubmed.ncbi.nlm.nih.gov/36894008/); [PMID: 36690329](https://pubmed.ncbi.nlm.nih.gov/36690329/)). **18F-FDG PET/CT** is a highly sensitive adjunct — meta-analytic sensitivity ~95%, specificity 88–91% — conditionally recommended when MRI is inconclusive, contraindicated, or artifact-limited, and to define healed status ([PMID: 42551483](https://pubmed.ncbi.nlm.nih.gov/42551483/); [PMID: 42533326](https://pubmed.ncbi.nlm.nih.gov/42533326/)). PET/CT also helps differentiate tuberculous from pyogenic disease ([PMID: 42650944](https://pubmed.ncbi.nlm.nih.gov/42650944/)).

**Laboratory/biomarkers.** Elevated **CRP (~95%)** and **ESR**; in children ESR is more sensitive than CRP (78% vs 38%) ([PMID: 31848723](https://pubmed.ncbi.nlm.nih.gov/31848723/)). Leukocytosis is more prominent in pyogenic than brucellar disease. Suggested LOINC: CRP (1988-5), ESR (4537-7).

**Microbiology.** **Blood cultures before therapy** (positive ~70–76%); if negative, obtain **multiple image-guided disc/vertebral biopsy samples** ([PMID: 36690329](https://pubmed.ncbi.nlm.nih.gov/36690329/)). **Culture-negative disease is common — pooled prevalence 43.2% (95%CI 33.8–52.6)** ([PMID: 42262500](https://pubmed.ncbi.nlm.nih.gov/42262500/)). **Metagenomic NGS markedly improves pathogen detection** — pooled sensitivity **89.7% (95%CI 85.6–93.1%)** versus culture ([PMID: 41584315](https://pubmed.ncbi.nlm.nih.gov/41584315/)); disc culture out-yields vertebral bone (50.0% vs 27.8%, p=0.046) and mNGS augments detection further ([PMID: 41407999](https://pubmed.ncbi.nlm.nih.gov/41407999/)). mNGS/16S resolve fastidious anaerobes and uncultivable organisms ([PMID: 42611158](https://pubmed.ncbi.nlm.nih.gov/42611158/); [PMID: 41841243](https://pubmed.ncbi.nlm.nih.gov/41841243/)).

**Clinical criteria & differential diagnosis.** **IDSA 2015** ([PMID: 26229122](https://pubmed.ncbi.nlm.nih.gov/26229122/)) and **SPILF 2022** ([PMID: 36690329](https://pubmed.ncbi.nlm.nih.gov/36690329/)) provide evidence-based diagnostic/treatment frameworks. **Differential diagnosis:** tuberculous spondylitis (longer symptom duration, night sweats, thoracic involvement, abscess, vertebral collapse), brucellar spondylitis (lumbar, less destructive), and degenerative **Modic type-1 changes** ([PMID: 33198439](https://pubmed.ncbi.nlm.nih.gov/33198439/); [PMID: 17624684](https://pubmed.ncbi.nlm.nih.gov/17624684/)). Fever (72.7% vs 45.2%, p=0.004) and sweating (72.7% vs 47.9%, p=0.009) favor brucellar over pyogenic in one comparison ([PMID: 33198439](https://pubmed.ncbi.nlm.nih.gov/33198439/)).

**Genetic testing / newborn screening / karyotyping / repeat expansion / CMA:** **Not applicable.**

---

## Section 11 — Outcome / Prognosis

**Mortality.** In-hospital mortality **7.1%** across 10,801 cases ([PMID: 42778058](https://pubmed.ncbi.nlm.nih.gov/42778058/)); 11–15% in higher-acuity cohorts ([PMID: 35657387](https://pubmed.ncbi.nlm.nih.gov/35657387/); [PMID: 30002914](https://pubmed.ncbi.nlm.nih.gov/30002914/)). **Concurrent infection raised mortality ~4-fold (3.3% vs 0.8%)** ([PMID: 37148755](https://pubmed.ncbi.nlm.nih.gov/37148755/)).

**Morbidity.** Residual disability in **20–30%**, recurrence **6–17%** ([PMID: 42262500](https://pubmed.ncbi.nlm.nih.gov/42262500/)). Neurologic recovery occurred in only **27% of spinal-cord-injured patients** ([PMID: 35657387](https://pubmed.ncbi.nlm.nih.gov/35657387/)).

**Prognostic factors.**
- **Epidural abscess extension ≥3 segments:** HR 4.72 (95%CI 1.57–14.20, p=0.006) for lethality ([PMID: 35657387](https://pubmed.ncbi.nlm.nih.gov/35657387/)).
- **Surgical timing:** timely surgery ≤14 days improved 1-year OS (HR 0.22, p=.019) and recurrence-free survival (HR 0.35, p=.024); prolonged time-to-culture-positivity ≥60h (lower bacterial load) improved OS (HR 0.18, p=.003) ([PMID: 42314843](https://pubmed.ncbi.nlm.nih.gov/42314843/)).
- **Concurrent infective endocarditis (IE):** co-occurs in ~8% of IE patients ([PMID: 33858337](https://pubmed.ncbi.nlm.nih.gov/33858337/)); in combined IE+SD requiring surgery, operating on SD **first** independently predicted 30-day mortality (25.7% vs 11.4%, p=.037) ([PMID: 38964339](https://pubmed.ncbi.nlm.nih.gov/38964339/)).
- Age, thoracic involvement, limb weakness, urinary symptoms/cauda equina, and malnutrition worsen outcomes ([PMID: 35904356](https://pubmed.ncbi.nlm.nih.gov/35904356/); [PMID: 39773279](https://pubmed.ncbi.nlm.nih.gov/39773279/)).

---

## Section 12 — Treatment

**Pharmacotherapy (mainstay).** Prolonged **pathogen-directed antibiotics**. The landmark **Bernard et al. open-label non-inferiority RCT** (NCT00764114; 359 adults, 71 French centers) established that **6 weeks is non-inferior to 12 weeks** for pyogenic vertebral osteomyelitis (non-inferiority margin 10%) ([PMID: 25468170](https://pubmed.ncbi.nlm.nih.gov/25468170/)). **SPILF 2022** recommends short, adapted courses with **early IV-to-oral switch**, reserving >6 weeks for complicated disease ([PMID: 36690329](https://pubmed.ncbi.nlm.nih.gov/36690329/)). Real-world durations run longer (median ~92 days; German survey median total 8 weeks, IV 2 weeks) ([PMID: 30002914](https://pubmed.ncbi.nlm.nih.gov/30002914/); [PMID: 36894008](https://pubmed.ncbi.nlm.nih.gov/36894008/)). Empiric regimens target *S. aureus* (including MRSA where prevalent) pending cultures. **NCIT:** antibiotic therapy (NCIT:C15219 Antibiotic Therapy).

**Surgical/interventional.** Most cases (82–86%) are managed conservatively; surgery in **14–40%** for instability, abscess, neurologic deficit, or medical failure ([PMID: 37384614](https://pubmed.ncbi.nlm.nih.gov/37384614/); [PMID: 42262500](https://pubmed.ncbi.nlm.nih.gov/42262500/); [PMID: 26700630](https://pubmed.ncbi.nlm.nih.gov/26700630/)). Surgical toolkit:
- **Anterior debridement + stabilization + fusion with titanium mesh cage** — systematic review of 192 patients; at admission 48% had abscess and 51% neurologic impairment; gram-positive 71%, gram-negative 24% ([PMID: 27324195](https://pubmed.ncbi.nlm.nih.gov/27324195/)).
- **Transforaminal lumbar interbody debridement and fusion (TLIDF)** for postdiscectomy discitis — 100% infection clearance, superior alignment/function vs conservative care ([PMID: 30308339](https://pubmed.ncbi.nlm.nih.gov/30308339/)).
- **Minimally invasive percutaneous disc irrigation/debridement** (dual Jamshidi needles) — feasible/safe for refractory disease in comorbid elderly (mean 67y) ([PMID: 30123957](https://pubmed.ncbi.nlm.nih.gov/30123957/)).
- **Local antibiotic carriers** (calcium sulfate/hydroxyapatite pellets) may shorten systemic therapy ([PMID: 32719918](https://pubmed.ncbi.nlm.nih.gov/32719918/)).

**Supportive/rehabilitative:** pain control, immobilization/bracing, nutritional support, physiotherapy. **Sequence matters** in combined IE+SD — treat IE surgically first to reduce 30-day mortality ([PMID: 38964339](https://pubmed.ncbi.nlm.nih.gov/38964339/)).

**Gene/cell/RNA/targeted/immunotherapy, pharmacogenomics:** **Not applicable.**

---

## Section 13 — Prevention

- **Primary prevention:** control of bacteremic sources — aseptic vascular access and hemodialysis technique, harm-reduction for IV drug use, prompt treatment of *S. aureus* bacteremia, and infection-control during spinal surgery.
- **Secondary prevention:** early recognition (high index of suspicion for back pain + fever + elevated CRP), and **cardiac screening (echocardiography) given ~8% IE co-occurrence** ([PMID: 33858337](https://pubmed.ncbi.nlm.nih.gov/33858337/)).
- **Tertiary prevention:** guideline-concordant antibiotic duration, timely surgery for abscess/deficit, and management of malnutrition to reduce mortality/readmission ([PMID: 39773279](https://pubmed.ncbi.nlm.nih.gov/39773279/)).
- **Immunization / genetic screening / carrier screening:** Not applicable (no vaccine for pyogenic disease; BCG relevant only to TB).

---

## Section 14 — Other Species / Natural Disease

**Naturally occurring discospondylitis in dogs closely mirrors human hematogenous spondylodiscitis**, providing a spontaneous large-animal comparative model. In a multi-institutional study of 386 dogs, **males were overrepresented (236/386), L7–S1 was the most common site, and *Staphylococcus* species were prevalent (23/38 positive blood cultures)**; trauma increased relapse risk (OR 9.0, 95%CI 2.2–37.0), as did prior steroid therapy ([PMID: 37288966](https://pubmed.ncbi.nlm.nih.gov/37288966/)). **Mycotic (fungal) discospondylitis** in dogs is predominantly *Aspergillus* (7/11), German Shepherd-predisposed, with poor prognosis (median survival 30 days) ([PMID: 40270003](https://pubmed.ncbi.nlm.nih.gov/40270003/)). Disseminated fungal infections (e.g., *Rasamsonia*) cause multifocal discospondylitis in German Shepherds via urinary/hematogenous routes ([PMID: 34387899](https://pubmed.ncbi.nlm.nih.gov/34387899/)).

- **Taxonomy:** *Canis lupus familiaris* (NCBI txid9615); *S. aureus* (txid1280).
- **Breed (VBO):** German Shepherd predisposition, especially for mycotic forms.
- **Zoonotic potential:** the disease itself is not zoonotic, but shared *S. aureus* biology underlies cross-species pathogenesis. Male predominance, lumbosacral predilection, and staphylococcal dominance are conserved across humans and dogs, supporting **evolutionary conservation of the hematogenous-seeding mechanism**.

---

## Section 15 — Model Organisms

- **Spontaneous large-animal model:** canine discospondylitis (above) — high face validity for hematogenous, *Staphylococcus*-driven, lumbosacral disease ([PMID: 37288966](https://pubmed.ncbi.nlm.nih.gov/37288966/)).
- **Induced rodent models:** rat **disc-stab injury models** demonstrate cytokine (IL-1β, TNF-α, IL-6/IL-8) production and MAPK (p38/ERK/JNK) signaling underlying disc inflammation and degeneration ([PMID: 18246002](https://pubmed.ncbi.nlm.nih.gov/18246002/)); useful for the inflammatory/tissue-damage arm rather than infection per se.
- **Murine implant-associated osteomyelitis:** USA300 MRSA K-wire model dissects *S. aureus* biofilm/virulence (msaABCR operon) and osteoclast-mediated bone destruction ([PMID: 33109085](https://pubmed.ncbi.nlm.nih.gov/33109085/)).
- **In vitro/ex vivo biofilm-on-bone systems:** demonstrate direct, host-independent bone dissolution by *S. aureus*, *P. aeruginosa*, *C. albicans*, *S. mutans* biofilms via acidification ([PMID: 28076372](https://pubmed.ncbi.nlm.nih.gov/28076372/)).
- **Limitations:** rodent disc-injury models capture inflammation but not spontaneous hematogenous seeding; implant models emphasize device-associated rather than native disc infection.
- **Resources:** MGI (mouse), RGD (rat), plus veterinary case registries (VetCompass) for canine natural disease.

---

## Mechanistic Model / Interpretation

The unifying model is **hematogenous metastasis of a bacteremic focus to the richly vascularized vertebral endplate, followed by centrifugal spread into the immunologically privileged, avascular disc**. Two destructive engines then operate in parallel — **host osteoclast resorption** (cytokine/RANKL-driven) and **pathogen biofilm acidification** (host-independent). Biofilm additionally explains chronicity, culture-negativity (~43%), and implant-associated recurrence, and rationalizes the need for both prolonged antibiotics and, when biofilm-laden necrotic tissue/hardware is present, surgical debridement. The clinical severity gradient — from self-limiting pediatric discitis to lethal elderly spondylodiscitis with epidural abscess — is governed by host factors (age, immunocompetence, nutrition), bacterial burden (time-to-culture-positivity as a surrogate), and abscess extent. Prognostic levers that are actionable — **early antibiotics, timely surgery ≤14 days, correct IE-first sequencing, and nutritional optimization** — all map cleanly onto this causal chain.

---

## Evidence Base (selected)

| PMID | Contribution | Role |
|---|---|---|
| [37980371](https://pubmed.ncbi.nlm.nih.gov/37980371/) | +104% incidence rise (Germany) | Supports rising epidemiology |
| [37384614](https://pubmed.ncbi.nlm.nih.gov/37384614/) | 1.5× rise, TB decline, elderly 47.6% (Korea) | Supports epidemiology/age |
| [42778058](https://pubmed.ncbi.nlm.nih.gov/42778058/) | Age/site pathogen shift; 7.1% mortality (n=10,801) | Supports etiology & prognosis |
| [41905317](https://pubmed.ncbi.nlm.nih.gov/41905317/) | *S. aureus* bacteremia → spine 20%; 7.6×/4.8× risk | Supports pathogenesis/risk |
| [42262500](https://pubmed.ncbi.nlm.nih.gov/42262500/) | Culture-negative 43.2%; recurrence/disability | Supports diagnostics/prognosis |
| [26700630](https://pubmed.ncbi.nlm.nih.gov/26700630/) / [35706345](https://pubmed.ncbi.nlm.nih.gov/35706345/) | Three routes; downstream complications | Supports causal chain |
| [35657387](https://pubmed.ncbi.nlm.nih.gov/35657387/) | Abscess ≥3 segments HR 4.72; 27% neuro recovery | Supports prognosis |
| [36690329](https://pubmed.ncbi.nlm.nih.gov/36690329/) / [26229122](https://pubmed.ncbi.nlm.nih.gov/26229122/) | SPILF 2022 / IDSA 2015 guidelines | Supports diagnosis/treatment |
| [25468170](https://pubmed.ncbi.nlm.nih.gov/25468170/) | 6 vs 12 wk RCT non-inferiority | Landmark treatment evidence |
| [42551483](https://pubmed.ncbi.nlm.nih.gov/42551483/) / [42533326](https://pubmed.ncbi.nlm.nih.gov/42533326/) | FDG-PET/CT ~95% sens; adjunct recommendation | Supports diagnostics |
| [41584315](https://pubmed.ncbi.nlm.nih.gov/41584315/) / [41407999](https://pubmed.ncbi.nlm.nih.gov/41407999/) | mNGS 89.7% sens; disc>bone yield | Supports molecular diagnostics |
| [33109085](https://pubmed.ncbi.nlm.nih.gov/33109085/) / [28076372](https://pubmed.ncbi.nlm.nih.gov/28076372/) | Biofilm/osteoclast bone destruction | Supports mechanism |
| [37288966](https://pubmed.ncbi.nlm.nih.gov/37288966/) / [40270003](https://pubmed.ncbi.nlm.nih.gov/40270003/) | Canine discospondylitis model | Supports comparative biology |
| [42314843](https://pubmed.ncbi.nlm.nih.gov/42314843/) / [38964339](https://pubmed.ncbi.nlm.nih.gov/38964339/) / [33858337](https://pubmed.ncbi.nlm.nih.gov/33858337/) | Surgical timing; IE co-occurrence/sequencing | Supports prognosis |

---

## Limitations and Knowledge Gaps

1. **Observational evidence dominates.** Apart from the Bernard 6-vs-12-week RCT, most treatment and prognostic data are retrospective; surgical indications and technique choice remain heterogeneous ([PMID: 36894008](https://pubmed.ncbi.nlm.nih.gov/36894008/)).
2. **Culture-negativity (~43%)** limits pathogen-directed therapy; mNGS performance, while strong (89.7% sensitivity), still needs standardization, cost-effectiveness data, and contamination controls.
3. **No host-genetic susceptibility data** — whether polymorphisms in innate immunity modulate risk is unstudied; the disease is treated here as purely acquired.
4. **Prognostic surrogates** such as time-to-culture-positivity are promising but derive from small cohorts (n=48) ([PMID: 42314843](https://pubmed.ncbi.nlm.nih.gov/42314843/)).
5. **Pediatric vs adult forms** may represent partly distinct entities; the self-limiting pediatric form is under-characterized microbiologically.
6. **Low-grade disc infection** (e.g., *Cutibacterium acnes*) and its relationship to Modic changes/low back pain remains controversial and outside classic spondylodiscitis.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective mNGS validation trial** in culture-negative spondylodiscitis, comparing time-to-effective-therapy and outcomes vs culture-guided care.
2. **Randomized evaluation of early surgery (≤14 days)** vs antibiotics-first in patients with epidural abscess but no deficit, to test the observed survival benefit prospectively.
3. **Biomarker study** validating time-to-culture-positivity and CRP/ESR trajectories as prognostic tools in a multicenter cohort.
4. **Anti-biofilm adjunct trials** (e.g., rifampin combinations, local antibiotic carriers) building on [PMID: 32719918](https://pubmed.ncbi.nlm.nih.gov/32719918/).
5. **Standardized IE screening protocol** (routine echocardiography) evaluation given ~8% co-occurrence and the mortality impact of surgical sequencing.
6. **Comparative canine–human genomic/microbiome studies** leveraging the spontaneous dog model to dissect host-independent biofilm bone destruction.
7. **Nutritional intervention trial** targeting hypoalbuminemia to test whether correcting malnutrition improves mortality/readmission.

---

*Report compiled from 14 confirmed findings and 65 reviewed papers over 5 investigation iterations. Sections on causal genes, inheritance, variant classification, chromosomal abnormalities, pharmacogenomics, gene/cell/RNA therapy, and genetic screening are marked Not Applicable because infectious discitis is an acquired microbial infection, not a heritable disorder.*


## Artifacts

- [OpenScientist final report](Infectious_Discitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Infectious_Discitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 45 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 45 |
| On topic | 18 |
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
| Terms whose name was checked | 15 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0032243` (1 mention) - the report calls it "Bacteremia"; HP calls it **Abnormal tissue metabolite concentration**
- `UBERON:0006678` (1 mention) - the report calls it "Primary structures:** intervertebral disc"; UBERON calls it **foramen secundum**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011227` (1 mention) - the report calls it "Elevated CRP"; HP calls it **Elevated circulating C-reactive protein concentration**, and lists "Elevated CRP" among its other names