---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T14:07:47.084526'
end_time: '2026-09-01T14:29:14.114226'
duration_seconds: 1287.03
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: TFRC-Related Combined Immunodeficiency
  mondo_id: ''
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
citation_count: 9
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 9
  on_topic: 8
  validator_version: 0.2.1
term_validation:
  total_terms: 49
  verified: 45
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 1
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0002028
    reported_labels:
    - 100% (part of presenting triad)
    ontology_label: Chronic diarrhea
  - term_id: HP:0004313
    reported_labels:
    - 100% (one with elevated IgM)
    ontology_label: Decreased circulating immunoglobulin concentration
  unresolvable_prefixes:
  - ORPHA
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
  path: TFRC-Related_Combined_Immunodeficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: TFRC-Related_Combined_Immunodeficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TFRC-Related Combined Immunodeficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **TFRC-Related Combined Immunodeficiency** covering all of the
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

# TFRC-Related Combined Immunodeficiency — Comprehensive Disease Report

**Disease:** TFRC-Related Combined Immunodeficiency (TFRC-CID)
**Primary ontology ID:** MONDO:0014760 · OMIM #616740 (Immunodeficiency-46, IMD46) · ORPHA:476113 · DOID:0111948 · UMLS/MedGen C5568133 · SNOMED CT 1179288008
**Causal gene:** *TFRC* (transferrin receptor 1, TfR1/CD71; HGNC:11763; NCBI Gene 7037; Ensembl ENSG00000072274; OMIM gene 190010)
**Category:** Mendelian, autosomal recessive inborn error of immunity

---

## Summary

TFRC-Related Combined Immunodeficiency is an ultra-rare, autosomal-recessive **inborn error of immunity (IEI)** caused by biallelic hypomorphic missense mutations in *TFRC*, the gene encoding transferrin receptor 1 (TfR1, also known as CD71). The disease is a "single-gene experiment of nature" that demonstrates that **TfR1-mediated iron uptake is a non-redundant metabolic and signaling checkpoint** required for antigen-receptor–driven lymphocyte activation, clonal expansion, and immunoglobulin class-switching. Every reported pathogenic allele lies in the receptor's cytoplasmic **YTRF internalization motif**, disrupting clathrin-mediated endocytosis of iron-loaded transferrin. The consequence is intracellular iron starvation that selectively cripples the most iron-avid cells of the body — proliferating lymphocytes — while erythropoiesis is largely spared through an accessory endocytosis route provided by the erythroblast metalloreductase STEAP3.

Clinically, patients present in early life with a triad of **recurrent sinopulmonary infections, chronic diarrhea, and failure to thrive**, accompanied by hypogammaglobulinemia (occasionally with elevated IgM), impaired T-cell function despite frequently normal lymphocyte counts, and intermittent multilineage cytopenias (neutropenia, thrombocytopenia, anemia). The disease behaves as a combined immunodeficiency (CID) rather than SCID; total lymphocyte numbers are often preserved but their function is compromised. Untreated, the disorder carries risk of fatal sepsis and neurological complications, and bone-marrow dysmyelopoiesis with clonal cytogenetic changes has been observed.

**Allogeneic hematopoietic stem cell transplantation (HSCT) is curative**, restoring immune function and abolishing transfusion/IVIG dependence, with excellent reported survival. Supportive management (immunoglobulin replacement, antimicrobial prophylaxis) sustains non-transplanted patients, and in vitro data show that iron supplementation (iron citrate / ferric ammonium citrate) can rescue the lymphocyte proliferation defect, pointing toward possible adjunctive metabolic therapies. This report integrates nine confirmed findings and 25 reviewed papers into a complete disease-knowledge-base entry spanning etiology, phenotype, mechanism, genetics, diagnostics, prognosis, treatment, prevention, and model organisms.

---

## Key Findings

### Finding 1 — Biallelic *TFRC* mutations disrupting the TfR1 internalization motif cause the disease

The founding cohort carried a homozygous **c.58T>C (p.Tyr20His)** substitution in *TFRC*. The Tyr20 residue is part of the **YTRF endocytic internalization motif** in the TfR1 cytoplasmic tail; its substitution to histidine (Y20H) impairs recognition by the clathrin adaptor machinery, causing defective receptor endocytosis, failure of iron internalization, and a paradoxical **increase in surface TfR1 expression** (because the receptor cannot be internalized and recycled normally). Functional rescue experiments confirmed causality: iron citrate restored lymphocyte proliferation in vitro, and expression of wild-type — but not mutant — TfR1 rescued transferrin uptake in patient-derived fibroblasts.

> *"had a homozygous p.Tyr20His substitution in transferrin receptor 1 (TfR1), encoded by TFRC. The substitution disrupts the TfR1 internalization motif, resulting in defective receptor endocytosis and markedly increased TfR1 expression on the cell surface. Iron citrate rescued the lymphocyte defects"* — [PMID: 26642240](https://pubmed.ncbi.nlm.nih.gov/26642240/)

A second pathogenic homozygous allele, **c.64C>T (p.Arg22Trp)**, was later reported in the same motif region, confirming allelic heterogeneity and reinforcing that the internalization motif is the mechanistic hotspot:

> *"we herein identified a new disease-causing homozygous germline mutation in the TFRC gene (c.64C > T, p.R22W)"* — [PMID: 38270687](https://pubmed.ncbi.nlm.nih.gov/38270687/)

**Functional consequence:** loss of function for iron internalization (a hypomorphic/partial LOF at the receptor level, with retained or increased surface expression). **Origin:** germline; no somatic contribution.

### Finding 2 — Clinical phenotype: early-onset combined immunodeficiency with cytopenias, infections, and failure to thrive

In the best-characterized cohort of **8 patients from 6 families** (median age 7 years, range 4–32), all presented in early life. Phenotype frequencies:

| Feature | Frequency | HPO term |
|---|---|---|
| Recurrent sinopulmonary infections | 100% | HP:0005425 |
| Chronic diarrhea | 100% (part of presenting triad) | HP:0002028 |
| Failure to thrive | 100% | HP:0001508 |
| Hypogammaglobulinemia | 100% (one with elevated IgM) | HP:0004313 |
| Impaired T-cell function | 100% | HP:0002721 |
| Intermittent neutropenia | 100% | HP:0001875 |
| Recurrent thrombocytopenia | 87% | HP:0004854 |
| Anemia | 62% | HP:0001903 |
| Less common: skin abscesses, conjunctivitis, developmental delay, optic nerve atrophy, vitiligo, multinodular goiter, HLH-like symptoms | variable | HP:0000509 (conjunctivitis), others |

> *"All patients presented with recurrent sinopulmonary infections, chronic diarrhea, and failure to thrive in early life."* — [PMID: 32851577](https://pubmed.ncbi.nlm.nih.gov/32851577/)

> *"All patients had intermittent neutropenia and 87% of the patients had recurrent thrombocytopenia. Anemia was found in 62%. All patients had hypogammaglobinemia"* — [PMID: 32851577](https://pubmed.ncbi.nlm.nih.gov/32851577/)

A key clinical distinction is that **lymphocyte numbers are typically normal but function is impaired** — this is a combined immunodeficiency, not a lymphopenic SCID. One patient died of sepsis with neurological complications; bone-marrow dysmyelopoiesis/dysplasia and one clonal cytogenetic abnormality raised concern for myelodysplasia in the transplant cohort.

### Finding 3 — Mechanism: TfR1-mediated iron uptake is a non-redundant checkpoint; STEAP3 spares erythropoiesis

TfR1 mediates **receptor-mediated endocytosis of diferric transferrin**, the dominant iron-acquisition route for rapidly proliferating cells. When endocytosis fails, activated lymphocytes are starved of iron precisely when they most need it — during antigen-receptor-driven clonal expansion — blocking proliferation and B-cell class-switching. The **erythroid-sparing** phenomenon (why patients have relatively mild anemia despite a global iron-uptake defect) is explained by **STEAP3**, a metalloreductase expressed in erythroblasts that associates with TfR1 and provides an accessory endocytosis signal:

> *"STEAP3, a metalloreductase expressed in erythroblasts, associates with TfR1 and partially rescues transferrin uptake in patient-derived fibroblasts, suggesting that STEAP3 may provide an accessory TfR1 endocytosis signal that spares patients from severe anemia"* — [PMID: 26642240](https://pubmed.ncbi.nlm.nih.gov/26642240/)

Complete loss of TfR1 is incompatible with hematopoiesis, underscoring the receptor's essential, non-redundant role:

> *"Transferrin receptor 1 (Tfr1) mediates the endocytosis of diferric transferrin in order to transport iron, and Tfr1 has been suggested to play an important role in hematopoiesis"* — [PMID: 31601687](https://pubmed.ncbi.nlm.nih.gov/31601687/)

The disease thus provides a "biologically instructive human model" that iron uptake via TfR1 is a metabolic checkpoint for adaptive immunity ([PMID: 41714512](https://pubmed.ncbi.nlm.nih.gov/41714512/)).

### Finding 4 — Allogeneic HSCT is curative

A retrospective study of **5 TFRC-deficient patients** who underwent allogeneic HSCT (Boston Children's, 2011–2018) demonstrated cure of both the hematologic and immunologic defects:

> *"All 5 patients tolerated myeloablative conditioning regimens and had robust donor cell engraftment with resolution of cytopenias and independence from intravenous immunoglobulin substitution."* — [PMID: 33096268](https://pubmed.ncbi.nlm.nih.gov/33096268/)

> *"All 5 patients were alive at a median follow-up of 47.1 months posttransplant"* (range 15.7–85.4 months) — [PMID: 33096268](https://pubmed.ncbi.nlm.nih.gov/33096268/)

In the 8-patient cohort, 2 were transplanted successfully, 5 remained on prophylaxis (immunoglobulin replacement + antimicrobial prophylaxis), and 1 died — consistent with HSCT being the only definitive cure while supportive care manages non-transplanted patients.

### Finding 5 — Gene identifiers, locus, and population genetics

*TFRC* maps to **chromosome 3q29** (GRCh38 chr3:196,012,511–196,082,162, minus strand). The associated Mendelian phenotype is **Immunodeficiency-46 (IMD46), OMIM #616740**. gnomAD constraint metrics indicate only **moderate loss-of-function intolerance** (pLI ≈ 0.31; LOEUF/oe_lof_upper ≈ 0.54; missense Z ≈ 1.31) — consistent with an autosomal-recessive disorder in which heterozygous carriers are unaffected. The founder **c.58T>C (p.Y20H)** allele recurs in consanguineous families of Arabian/Middle Eastern (Kuwaiti/Saudi) origin, while **c.64C>T (p.R22W)** was reported in a Turkish family.

> *"The same homozygous missense mutation c.58T>C:p.Y20H, in the TFRC gene, was detected in all patients."* — [PMID: 32851577](https://pubmed.ncbi.nlm.nih.gov/32851577/)

Reported cases are extremely rare — only a few dozen worldwide.

### Finding 6 — Animal and in vitro models recapitulate the iron-uptake-dependent immune phenotype

A knock-in **Tfrc(Y20H/Y20H) mouse** reproduces the human immunological defects while sparing severe anemia:

> *"Tfrc(Y20H/Y20H) mice recapitulated the immunological defects of patients."* — [PMID: 26642240](https://pubmed.ncbi.nlm.nih.gov/26642240/)

Conditional models reveal TfR1's non-redundant roles across immune compartments. Treg-restricted CD71/*Tfrc* deletion causes a fatal autoimmune syndrome from failed perinatal Treg expansion:

> *"Mice with a Treg-restricted CD71 deficiency spontaneously developed a scurfy-like disease, caused by impaired perinatal Treg expansion."* — [PMID: 38954474](https://pubmed.ncbi.nlm.nih.gov/38954474/)

Antibody blockade of CD71 in fetal thymus organ culture blocks thymocyte proliferation and αβ T-cell maturation ([PMID: 7957580](https://pubmed.ncbi.nlm.nih.gov/7957580/)). The proliferation defect is iron-dependent and iron-reversible in human T cells:

> *"Growth arrest in iron-deficient (Fe-def) T cells was prevented upon addition of exogenous iron in the form of ferric ammonium citrate"* — [PMID: 32284314](https://pubmed.ncbi.nlm.nih.gov/32284314/)

### Finding 7 — Variant-level annotation of the two causal alleles

Both alleles use transcript **NM_001128148.3** and are germline missense variants in the TfR1 cytoplasmic internalization motif; neither has a somatic origin.

| Allele | cDNA / protein | Genomic (GRCh38) | dbSNP | ClinVar | OMIM allelic | Population frequency |
|---|---|---|---|---|---|---|
| Allele 1 | c.58T>C / p.Tyr20His | NC_000003.12:g.196075339A>G | rs863225436 | VCV 218163 (conflicting; functionally pathogenic) | 190010.0001 | gnomAD-exomes 0.00000; TOPMed 0.00001 (ultra-rare) |
| Allele 2 | c.64C>T / p.Arg22Trp | NC_000003.12:g.196075333G>A | rs373123870 | VCV 2999809 (VUS, single submitter; functionally disease-causing) | — | ExAC 0.00001; TOPMed 0.00001; ESP 0.00008 |

The Y20H allele carries an explicit ClinVar trait annotation of "TFRC-related combined immunodeficiency" and UniProt feature VAR_076365 (P02786). Despite ClinVar's "conflicting"/"uncertain" statuses, both variants meet functional evidence for pathogenicity (ACMG **PS3**):

> *"expression of wild-type but not mutant TfR1 rescued impaired transferrin uptake in patient-derived fibroblasts"* — [PMID: 26642240](https://pubmed.ncbi.nlm.nih.gov/26642240/)

### Finding 8 — Ontology mappings and curated HPO term set

The disease resolves to **MONDO:0014760**, mapped to OMIM:616740. The JAX/HPO-curated phenotype annotation set comprises: Immunodeficiency (HP:0002721), Recurrent sinopulmonary infections (HP:0005425), Sepsis (HP:0100806), Meningitis (HP:0001287), Recurrent oral thrush (HP:0009098), Chronic diarrhea (HP:0002028), Failure to thrive (HP:0001508), Conjunctivitis (HP:0000509), Decreased circulating immunoglobulin concentration (HP:0004313), Decreased total neutrophil count (HP:0001875), Intermittent thrombocytopenia (HP:0004854), Anemia (HP:0001903), and Autosomal recessive inheritance (HP:0000007). Mouse ortholog: *Tfrc*, NCBI Gene 22042, **MGI:98822**, mouse chromosome 16 B3.

### Finding 9 — Cross-ontology identifiers and curated GO/Reactome/PDB annotations

UniProt **P02786 (TFR1_HUMAN)** GO annotations directly matching the disease mechanism include: transferrin receptor activity (GO:0004998), receptor-mediated endocytosis (GO:0006898), receptor internalization (GO:0031623), transferrin transport (GO:0033572), iron ion transport (GO:0006826), intracellular iron ion homeostasis (GO:0006879), **positive regulation of T cell proliferation (GO:0042102)**, **positive regulation of B cell proliferation (GO:0030890)**, **positive regulation of isotype switching (GO:0045830)**, positive regulation of canonical NF-κB signaling (GO:0043123), and virus receptor activity (GO:0001618). Cellular-component terms: clathrin-coated pit (GO:0005905), early/recycling endosome (GO:0005769 / GO:0055037), HFE-transferrin receptor complex (GO:1990712). Reactome: Transferrin endocytosis and recycling (R-HSA-917977), Clathrin-mediated endocytosis (R-HSA-8856828), Cargo recognition for clathrin-mediated endocytosis (R-HSA-8856825). Experimental structures: PDB **1CX8** (ectodomain), **1SUV** (TfR1–transferrin), **1DE4** (TfR1–HFE).

---

## Section-by-Section Report

### 1. Disease Information

TFRC-Related Combined Immunodeficiency is a Mendelian, autosomal-recessive inborn error of immunity in which defective cellular iron uptake produces a combined (T- and B-cell) immunodeficiency. It is **information aggregated at the disease level** from a small number of patient cohorts and case reports, supplemented by curated ontology and model-organism resources (not EHR-derived).

**Key identifiers:** OMIM #616740 (phenotype IMD46); OMIM gene 190010 (*TFRC*); Orphanet ORPHA:476113 ("Combined immunodeficiency due to TFRC deficiency"); MONDO:0014760; DOID:0111948; UMLS/MedGen C5568133; SNOMED CT 1179288008. No dedicated ICD code exists; it is coded under combined immunodeficiencies (ICD-10 D81.9; ICD-11 4A01.1Z). MeSH indexing falls under "Severe Combined Immunodeficiency" / "Receptors, Transferrin (CD71)."

**Synonyms:** Immunodeficiency 46; IMD46; Combined immunodeficiency due to TFRC deficiency; Transferrin receptor 1 (TFRC/CD71) deficiency; TfR1 deficiency.

### 2. Etiology

**Causal factor:** purely genetic — biallelic hypomorphic missense mutations in *TFRC* disrupting the YTRF endocytic motif (Finding 1). **Genetic risk factors:** homozygosity/compound heterozygosity for pathogenic *TFRC* alleles; **consanguinity** is the principal risk factor, as founder alleles recur in inbred Middle Eastern and Turkish kindreds (Finding 5). There are no established environmental risk factors, protective factors, or gene–environment interactions for disease causation. Iron availability acts as an in vitro disease-modifying factor at the cellular level (Findings 1, 6) but is not established as a clinical modifier; STEAP3 co-expression is an intrinsic modifier sparing red cells. Heterozygous carriers are unaffected, consistent with recessive inheritance and modest gnomAD LOF-intolerance.

### 3. Phenotypes

Phenotypes are dominated by **laboratory abnormalities** (hypogammaglobulinemia, cytopenias) and **clinical signs/symptoms** (infections, diarrhea, failure to thrive). See Finding 2 table for per-phenotype frequencies and HPO terms. **Age of onset:** early life / infancy (neonatal–childhood). **Severity:** moderate to severe, variable — "clinical presentations have been severe in all reported cases" ([PMID: 33096268](https://pubmed.ncbi.nlm.nih.gov/33096268/)). **Progression:** chronic with episodic infectious/cytopenic exacerbations; cytopenias are typically intermittent/fluctuating. **Quality-of-life impact:** substantial — recurrent infections, chronic diarrhea, growth failure, and transfusion/IVIG dependence impair daily functioning; no disease-specific QoL instrument data are available. Rare/variable features: optic nerve atrophy, developmental delay, vitiligo, multinodular goiter, HLH-like presentation.

### 4. Genetic / Molecular Information

**Causal gene:** *TFRC* (HGNC:11763; NCBI Gene 7037; OMIM 190010) — a type II single-pass transmembrane homodimeric glycoprotein. **Pathogenic variants:** two germline missense alleles in the cytoplasmic internalization motif (Finding 7) — p.Tyr20His (c.58T>C) and p.Arg22Trp (c.64C>T), both ultra-rare in population databases. **Variant type:** missense (internalization-motif); no null alleles seen in patients (presumed lethal). **Functional consequence:** impaired receptor internalization/iron uptake (partial loss of function) with paradoxically increased surface TfR1. **Modifier genes:** **STEAP3** functionally modifies the phenotype (erythroid sparing; Finding 3). **gnomAD constraint:** pLI ≈ 0.31, LOEUF ≈ 0.54, missense Z ≈ 1.31 (moderate, recessive-consistent). **Epigenetic changes / chromosomal abnormalities:** none causal (3q29 CNV entries overlapping *TFRC* relate to the separate 3q29 deletion/duplication syndromes, not TFRC-CID; secondary clonal cytogenetic changes in bone marrow have been noted in individual patients, Finding 2).

### 5. Environmental Information

No environmental, lifestyle, or infectious agents cause this monogenic disease. Cellular **iron availability** is the key modifiable mechanistic variable. Infectious agents are **downstream consequences** — recurrent bacterial sinopulmonary pathogens, opportunistic infections, and oral thrush (*Candida*), consistent with combined immunodeficiency. TfR1 is also exploited as a receptor by several viruses (GO:0001618, virus receptor activity), but this is not part of TFRC-CID etiology.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic *TFRC* missense mutation** (c.58T>C p.Y20H or c.64C>T p.R22W) alters the **YTRF cytoplasmic internalization motif** of TfR1. *(demonstrated)*
2. Motif disruption **leads to** loss of recognition by the clathrin adaptor/AP-2 machinery, **resulting in** defective clathrin-mediated receptor endocytosis and paradoxically increased surface TfR1. *(demonstrated — WT-but-not-mutant rescue in fibroblasts)*
3. Defective endocytosis **results in** failure to internalize diferric transferrin, **leading to** intracellular iron deficiency in cells that depend on TfR1 for iron. *(demonstrated)*
4. Iron starvation **impairs** iron-dependent enzymes required for proliferation (e.g., ribonucleotide reductase for dNTP synthesis) and mitochondrial iron-sulfur functions, **blocking** cell-cycle progression in rapidly dividing cells. *(inferred from iron biology; supported by iron-rescue experiments, PMID 32284314)*
5. **Branch A (adaptive immunity — the disease-defining branch):** iron starvation of antigen-activated lymphocytes **blocks** clonal expansion, T-cell proliferation (GO:0042102), B-cell proliferation (GO:0030890), and immunoglobulin class-switch recombination (GO:0045830), **producing** combined immunodeficiency and hypogammaglobulinemia. *(demonstrated in patients and Y20H mice)*
6. **Branch B (myeloid/megakaryocytic):** impaired iron supply to proliferating progenitors **contributes to** intermittent neutropenia and thrombocytopenia, and bone-marrow dysmyelopoiesis. *(observed; mechanism partly inferred)*
7. **Branch C (erythroid — spared):** in erythroblasts, **STEAP3** associates with TfR1 and provides an **accessory endocytosis signal**, partially rescuing transferrin uptake and **sparing** patients from severe anemia. *(demonstrated in patient fibroblasts)*
8. The immune failure **manifests clinically** as recurrent sinopulmonary infections, chronic diarrhea, failure to thrive, and risk of fatal sepsis; rare HLH-like immune dysregulation may reflect disturbed lymphocyte homeostasis. *(demonstrated / partly inferred)*

**Molecular pathways:** clathrin-mediated endocytosis / transferrin endocytosis and recycling (Reactome R-HSA-917977, R-HSA-8856828, R-HSA-8856825); iron ion transport and homeostasis; downstream NF-κB signaling in lymphocyte activation. **Cellular processes:** receptor-mediated endocytosis (GO:0006898), receptor internalization (GO:0031623), blocked cell proliferation, lymphocyte activation. **Protein dysfunction:** loss of internalization function with retained ligand binding and increased surface density — a trafficking defect, not folding/aggregation; the tyrosine-based internalization signal normally recruits the clathrin adaptor. **Metabolic changes:** cellular iron deficiency impairing iron-dependent metabolism. **Chemical entities (CHEBI):** iron(2+)/iron(3+) (CHEBI:29033/CHEBI:29034), transferrin-bound iron; ferric ammonium citrate as rescuing reagent. **Immune involvement:** combined immunodeficiency (immunodeficiency, not autoimmunity, is the human phenotype; Treg models show autoimmune potential). **Cell types (CL):** T cell (CL:0000084), B cell (CL:0000236), regulatory T cell (CL:0000815), thymocyte, neutrophil (CL:0000775), hematopoietic stem cell (CL:0000037), erythroid precursor (CL:0000038). **Subcellular (GO CC):** plasma membrane (GO:0005886), clathrin-coated pit (GO:0005905), early/recycling endosome (GO:0005769/GO:0055037).

### 7. Anatomical Structures Affected

**Organ/system level:** immune/hematopoietic system (primary) — bone marrow (UBERON:0002371), thymus (UBERON:0002370), spleen, lymph nodes. Secondary: respiratory tract/lungs (UBERON:0002048) and paranasal sinuses (recurrent infections), gastrointestinal tract (UBERON:0001555; chronic diarrhea/malabsorption). Occasional: eye/optic nerve (UBERON:0000941; optic atrophy, conjunctivitis), skin (vitiligo, abscesses), thyroid (UBERON:0002046; goiter), CNS (developmental delay). **Tissue/cell level:** hematolymphoid tissue; T and B lymphocytes, Tregs, neutrophils, megakaryocytes/platelets, with erythroid lineage relatively spared. **Subcellular:** plasma-membrane receptor and endosomal trafficking compartment. **Lateralization:** systemic/bilateral (not a focal lesion).

### 8. Temporal Development

**Onset:** congenital/early infancy; presentation in the first years of life (cohort median age 7 y, range 4–32 y at study, with symptoms beginning early). **Onset pattern:** insidious to subacute, with acute infectious/cytopenic episodes. **Course:** chronic, lifelong without transplant; episodic infections and fluctuating cytopenias. **Progression:** variable; risk of bone-marrow dysplasia and, in severe cases, death from sepsis. **Remission:** treatment-induced (cure) with HSCT; no spontaneous remission. **Critical period for intervention:** early definitive diagnosis and HSCT before irreversible infectious/marrow complications accrue.

### 9. Inheritance and Population

**Inheritance:** autosomal recessive (HP:0000007) — *"Autosomal-recessive mutations in the human TFRC gene cause a combined immunodeficiency"* ([PMID: 33096268](https://pubmed.ncbi.nlm.nih.gov/33096268/)). **Penetrance:** effectively complete in biallelic individuals. **Expressivity:** variable (severity of cytopenias, presence of rare features). **Carrier state:** unaffected. **Founder effects/consanguinity:** major — the p.Y20H founder allele recurs in consanguineous Arabian/Middle Eastern (Kuwaiti/Saudi) families; p.R22W in a Turkish family. **Epidemiology:** ultra-rare; only a few dozen cases worldwide; no reliable prevalence/incidence figures (well below 1/1,000,000). **Sex ratio:** no sex bias expected for an autosomal-recessive trait. **Age distribution:** pediatric-onset. No genetic anticipation, germline mosaicism, or repeat-expansion mechanism applies.

### 10. Diagnostics

**Laboratory:** hypogammaglobulinemia (low IgG ± low/normal/elevated IgM), impaired specific antibody responses, abnormal T-cell proliferation to mitogens/antigens despite frequently **normal lymphocyte counts**, and intermittent multilineage cytopenias (CBC). A characteristic **immunophenotypic clue is markedly increased surface CD71/TfR1** on patient cells (because the receptor cannot be internalized). **Bone marrow:** may show dysmyelopoiesis/dysplasia — monitor for clonal evolution/MDS. **Functional/confirmatory assays:** defective transferrin uptake in patient fibroblasts, rescued by wild-type TfR1; lymphocyte proliferation defect rescued in vitro by iron (ferric) citrate (ACMG PS3). **Genetic testing is definitive:** single-gene *TFRC* sequencing, IEI/CID gene panels, whole-exome (WES) or whole-genome (WGS) sequencing — the disease was discovered by WES, and homozygosity mapping aids consanguineous pedigrees. **Differential diagnosis:** other combined immunodeficiencies/SCID, CVID with T-cell dysfunction, hyper-IgM syndromes (when IgM elevated), congenital neutropenia/thrombocytopenia syndromes, and iron-refractory iron deficiency (IRIDA/TMPRSS6) for the iron axis; the distinguishing feature is elevated surface CD71 with defective transferrin uptake plus biallelic *TFRC* variant. **Screening:** cascade/carrier testing in affected families; not part of standard newborn screening.

### 11. Outcome / Prognosis

**Without transplant:** guarded — chronic morbidity from recurrent infections, cytopenias, diarrhea, and growth failure; at least one death from sepsis/neurological complications ([PMID: 32851577](https://pubmed.ncbi.nlm.nih.gov/32851577/)); risk of progression to bone-marrow dysplasia/myelodysplasia. **With HSCT:** excellent — all 5 transplanted patients achieved donor engraftment, resolution of cytopenias, IVIG independence, and were alive at median 47.1 months, with no reported acute/chronic GVHD (Finding 4). **Prognostic factors:** timely diagnosis, infection burden, absence of pre-transplant marrow dysplasia/clonal evolution, and successful engraftment. No validated disease-specific prognostic biomarkers exist beyond genotype and marrow status.

### 12. Treatment

**Definitive/curative:** allogeneic **hematopoietic stem cell transplantation** with myeloablative conditioning (NCIT: Allogeneic Hematopoietic Stem Cell Transplantation) — the only established cure (Finding 4). **Supportive/prophylactic (non-transplanted patients):** immunoglobulin replacement therapy (IVIG/SCIG; NCIT: Immunoglobulin Therapy), antimicrobial prophylaxis, nutritional support for failure to thrive, and transfusion support for cytopenias. **Investigational/mechanistic:** in vitro **iron supplementation** (iron citrate, ferric ammonium citrate; CHEBI ferric citrate) rescues the lymphocyte proliferation defect (Findings 1, 6) — a rational but clinically unproven adjunct; because the endocytic block limits the transferrin route, non-transferrin iron delivery would likely be required. **Gene/cell therapy:** autologous *TFRC* gene correction of HSCs is a conceptual future direction; none is approved. **Pharmacogenomics:** none specific. Management otherwise follows general CID/IEI guidelines.

### 13. Prevention

**Primary prevention** of occurrence is via **genetic counseling and reproductive options** in at-risk consanguineous families: carrier testing, cascade screening, prenatal diagnosis, and preimplantation genetic testing (PGT) for known familial *TFRC* alleles. **Secondary prevention:** early molecular diagnosis (including high-risk screening in founder populations) enabling timely HSCT and prophylaxis. **Tertiary prevention:** immunoglobulin replacement, antimicrobial prophylaxis, nutritional/hematologic support, and marrow surveillance for MDS. Live vaccines should be used cautiously given the combined immunodeficiency. Consanguinity counseling is the key public-health lever; no vaccine prevents the disease itself.

### 14. Other Species / Natural Disease

**Taxonomy/orthologs:** human *TFRC* (NCBI Taxon 9606); mouse *Tfrc* (NCBI Gene 22042; MGI:98822; NCBI Taxon 10090; mouse chromosome 16 B3). TfR1 is highly evolutionarily conserved, and its role in iron uptake and hematopoiesis is conserved. **Natural disease:** no well-characterized spontaneous companion-animal or wildlife equivalent of TFRC-CID is catalogued in OMIA for this specific entity; knowledge derives from engineered models. Complete *Tfrc* loss is embryonic/hematopoietically lethal in mouse, underscoring conservation of the iron-uptake requirement. No zoonotic relevance.

### 15. Model Organisms

**Mammalian genetic models (mouse):**

| Model | Type | Phenotype recapitulation | PMID |
|---|---|---|---|
| *Tfrc*(Y20H/Y20H) knock-in | humanized point mutation | Recapitulates patients' immune defects (impaired lymphocyte proliferation); spares severe anemia — faithful model | [26642240](https://pubmed.ncbi.nlm.nih.gov/26642240/) |
| HSC-specific *Tfr1* conditional knockout | conditional KO | Severe impairment of hematopoiesis (complete loss non-viable) — shows non-redundancy | [31601687](https://pubmed.ncbi.nlm.nih.gov/31601687/) |
| Treg-restricted CD71/*Tfrc* deletion | conditional KO | Fatal scurfy-like autoimmunity from failed perinatal Treg expansion — reveals tolerance role | [38954474](https://pubmed.ncbi.nlm.nih.gov/38954474/) |

**In vitro / ex vivo models:** patient-derived fibroblasts (transferrin-uptake assay with WT-TfR1 rescue); human T cells under iron deprivation (reversible growth arrest with ferric ammonium citrate, [PMID: 32284314](https://pubmed.ncbi.nlm.nih.gov/32284314/)); fetal thymus organ culture with anti-CD71 antibody blockade ([PMID: 7957580](https://pubmed.ncbi.nlm.nih.gov/7957580/)). **Limitations:** the Y20H knock-in captures the immune phenotype but murine erythropoiesis/iron handling differ; complete knockouts are lethal and cannot model the hypomorphic human condition; patient-specific secondary features (developmental delay, goiter) are not recapitulated. **Resources:** MGI (MGI:98822), IMPC/IMSR for *Tfrc* alleles.

---

## Mechanistic Model / Interpretation

```
   Biallelic TFRC missense (p.Y20H / p.R22W)
                  │  disrupts YTRF internalization motif
                  ▼
   Loss of clathrin/AP-2 recognition of TfR1 tail
                  │  → defective endocytosis; ↑ surface CD71/TfR1
                  ▼
   Failure to internalize diferric transferrin
                  │  → intracellular IRON STARVATION
                  ▼
   Impaired iron-dependent enzymes (e.g., ribonucleotide reductase)
                  │  → blocked cell-cycle progression in dividing cells
      ┌───────────┼───────────────────────────────┐
      ▼           ▼                                ▼
  [Branch A]   [Branch B]                      [Branch C — SPARED]
  Lymphocytes  Myeloid/Mega                    Erythroblasts
  blocked      intermittent                    STEAP3 + TfR1 =
  proliferation neutropenia/                    accessory endocytosis
  & class-      thrombocytopenia;               → partial rescue of
  switch        marrow dysplasia                transferrin uptake
      │                                                │
      ▼                                                ▼
  COMBINED IMMUNODEFICIENCY                     mild/variable anemia
  (recurrent infections, chronic                (severe anemia avoided)
   diarrhea, FTT, hypogamma-
   globulinemia)
                  │
                  ▼
     Cured by allogeneic HSCT (donor cells have WT TfR1)
```

The unifying insight is that **TFRC-CID is a disease of cellular iron-supply logistics, not of iron stores**. Systemic iron is available, but the cells that most need to import it on demand — antigen-activated, rapidly dividing lymphocytes — cannot, because the receptor's "swallow" signal is broken. This explains the otherwise puzzling combination of (a) profound immune failure, (b) preserved lymphocyte *numbers* with impaired *function*, (c) relatively mild anemia (STEAP3 rescue), and (d) complete cure by replacing the hematopoietic system with donor cells carrying a functional receptor.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role |
|---|---|---|---|
| [26642240](https://pubmed.ncbi.nlm.nih.gov/26642240/) | *Missense mutation in TFRC causes combined immunodeficiency* | Human + mouse + in vitro | Landmark discovery: founding Y20H allele, mechanism, STEAP3 rescue, mouse model |
| [32851577](https://pubmed.ncbi.nlm.nih.gov/32851577/) | *Clinical/immunological characterization in 8 patients* | Human clinical cohort | Phenotype frequencies, founder variant, natural history |
| [33096268](https://pubmed.ncbi.nlm.nih.gov/33096268/) | *HSCT is curative for TFRC deficiency* | Human clinical (n=5) | Establishes curative therapy and survival |
| [38270687](https://pubmed.ncbi.nlm.nih.gov/38270687/) | *Novel homozygous TFRC mutation (R22W)* | Human clinical | Second causal allele; allelic heterogeneity |
| [41714512](https://pubmed.ncbi.nlm.nih.gov/41714512/) | *TFRC variants and IEI: iron-immune crosstalk* | Review | Frames disease as non-redundant iron/immune checkpoint |
| [31601687](https://pubmed.ncbi.nlm.nih.gov/31601687/) | *TfR1-mediated iron uptake essential in hematopoiesis* | Mouse | Non-redundancy; complete loss non-viable |
| [38954474](https://pubmed.ncbi.nlm.nih.gov/38954474/) | *Iron capture through CD71 drives Treg expansion* | Mouse | Treg/tolerance role of TfR1 iron uptake |
| [32284314](https://pubmed.ncbi.nlm.nih.gov/32284314/) | *Iron deprivation in human T cells* | In vitro (human) | Iron-dependent, iron-reversible T-cell arrest |
| [7957580](https://pubmed.ncbi.nlm.nih.gov/7957580/) | *Anti-TfR antibody inhibits early T-cell development* | Ex vivo | CD71-dependent thymocyte proliferation/maturation |

Supporting/contextual papers on TfR1 biology (CD71 as viral/particle uptake receptor; iron-chelation immunosuppression; TfR1-targeted therapeutics) corroborate the receptor's centrality to proliferating immune cells but do not directly test TFRC-CID.

---

## Supported vs. Refuted Hypotheses

**Supported:**
1. TFRC-CID is caused by biallelic internalization-motif missense mutations (Y20H, R22W) → defective TfR1 endocytosis and iron uptake ([PMID: 26642240](https://pubmed.ncbi.nlm.nih.gov/26642240/), [38270687](https://pubmed.ncbi.nlm.nih.gov/38270687/)).
2. Iron starvation of proliferating lymphocytes is the proximate mechanism; the defect is iron-rescuable in vitro ([PMID: 26642240](https://pubmed.ncbi.nlm.nih.gov/26642240/), [32284314](https://pubmed.ncbi.nlm.nih.gov/32284314/)).
3. Erythroid sparing is explained by STEAP3 accessory endocytosis ([PMID: 26642240](https://pubmed.ncbi.nlm.nih.gov/26642240/)).
4. HSCT is curative ([PMID: 33096268](https://pubmed.ncbi.nlm.nih.gov/33096268/)).
5. Founder p.Y20H allele in consanguineous Middle-Eastern populations ([PMID: 32851577](https://pubmed.ncbi.nlm.nih.gov/32851577/)).

**Refuted / not supported:**
- That the disease presents primarily as severe anemia (it does not; anemia is mild/variable due to STEAP3).
- That an environmental or infectious agent initiates disease (it is purely Mendelian).

---

## Limitations and Knowledge Gaps

- **Extreme rarity:** with only a few dozen patients (largest cohort n=8, dominated by a single founder variant), phenotype frequencies, prognosis, and epidemiology are subject to ascertainment bias toward severe/consanguineous cases.
- **Variant classification lag:** ClinVar lists both alleles as "conflicting"/"uncertain" despite robust functional (PS3) evidence — a curation gap that could impede diagnosis.
- **Genotype–phenotype correlation** is unresolved: whether R22W differs in severity from Y20H, and what drives variable features (optic atrophy, vitiligo, goiter, HLH-like disease), is unknown.
- **Marrow dysplasia risk:** the mechanistic basis and true frequency of dysmyelopoiesis/clonal evolution are unclear and clinically important.
- **Adjunctive iron therapy** is supported only in vitro; no clinical trial has tested whether systemic or targeted iron delivery improves immune function in patients.
- **No detailed patient omics** (single-cell transcriptomic/proteomic profiling of patient lymphocytes) is available to map the iron-starvation program in vivo.
- **No formal prevalence/incidence, ICD-specific coding, or standardized QoL data** exist.

---

## Proposed Follow-up Experiments / Actions

1. **ClinVar reclassification:** submit the functional-rescue evidence to upgrade p.Y20H and p.R22W toward likely-pathogenic/pathogenic, improving diagnostic yield.
2. **International patient registry:** aggregate cases to define natural history, genotype–phenotype correlations, marrow-dysplasia incidence, and long-term HSCT outcomes.
3. **Single-cell multi-omics of patient lymphocytes** before/after activation and iron rescue to map the intracellular iron-starvation checkpoint (RNR, cell-cycle, class-switch machinery).
4. **Controlled iron-supplementation study** (in vitro dose-response, then compassionate-use assessment) to test targeted/non-transferrin iron delivery as a bridge therapy pre-transplant.
5. **Gene-correction proof-of-concept** in patient HSCs/iPSCs (base or prime editing of c.58/c.64) to evaluate autologous gene therapy feasibility.
6. **Mechanistic dissection of STEAP3 rescue** to determine whether STEAP3-mimetic or alternative-endocytosis strategies could broaden the erythroid-sparing effect to lymphoid cells.
7. **Prospective HSCT-timing analysis** to define the optimal window minimizing pre-transplant infectious and marrow complications.

---

*Report compiled from 9 confirmed findings and 25 reviewed papers across 5 investigation iterations. Evidence types are annotated as human clinical, model organism, in vitro, or computational/ontological throughout. Search date: 2026-09-01.*


## Artifacts

- [OpenScientist final report](TFRC-Related_Combined_Immunodeficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](TFRC-Related_Combined_Immunodeficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 9 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 49 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 3 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002028` (2 mentions) - the report calls it "100% (part of presenting triad)"; HP calls it **Chronic diarrhea**
- `HP:0004313` (2 mentions) - the report calls it "100% (one with elevated IgM)"; HP calls it **Decreased circulating immunoglobulin concentration**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`, `MGI`.