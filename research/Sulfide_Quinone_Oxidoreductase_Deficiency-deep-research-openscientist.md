---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-08T13:33:01.149376'
end_time: '2026-10-08T14:24:39.507971'
duration_seconds: 3098.36
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Sulfide Quinone Oxidoreductase Deficiency
  mondo_id: MONDO:0030982
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
citation_count: 6
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 4
  validator_version: 0.3.0
term_validation:
  total_terms: 42
  verified: 39
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 7
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0032263
    reported_labels:
    - Multiorgan failure
    ontology_label: Increased blood pressure
  - term_id: HP:0012719
    reported_labels:
    - Neurostorming / dysautonomia
    ontology_label: Functional abnormality of the gastrointestinal tract
  labels_variant: 2
  unresolvable_prefixes:
  - GARD
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Sulfide_Quinone_Oxidoreductase_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Sulfide_Quinone_Oxidoreductase_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sulfide Quinone Oxidoreductase Deficiency
- **MONDO ID:** MONDO:0030982 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Sulfide Quinone Oxidoreductase Deficiency** covering all of the
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

# Sulfide:Quinone Oxidoreductase Deficiency (SQORD) — Comprehensive Disease Characteristics Report

**Disease:** Sulfide Quinone Oxidoreductase Deficiency
**MONDO:** MONDO:0030982 · **OMIM (phenotype):** #619221 · **Gene:** *SQOR* (OMIM *617658)
**Category:** Mendelian — autosomal-recessive mitochondrial (inborn error of hydrogen-sulfide catabolism)
**Report date:** 2026-10-08

---

## Summary

**Sulfide:quinone oxidoreductase deficiency (SQORD; MONDO:0030982, OMIM #619221)** is an ultra-rare, autosomal-recessive inborn error of mitochondrial hydrogen-sulfide (H₂S) catabolism caused by biallelic loss-of-function variants in **SQOR** (15q21.1; HGNC:20390; UniProt Q9Y6N5). SQOR encodes the committed first enzyme of mitochondrial sulfide oxidation — an inner-membrane FAD flavoprotein (EC 1.8.5.4) that oxidizes H₂S and funnels the electrons into ubiquinone/Coenzyme Q, coupling sulfide detoxification to the respiratory chain.

When SQOR is lost, endogenous and gut-microbiome-derived H₂S can no longer be cleared and accumulates to concentrations that inhibit **complex IV (cytochrome c oxidase)**. The result is an *isolated, functional* complex IV deficiency — activity falls while complex IV protein level and assembly remain normal — producing bioenergetic failure in the most oxygen- and energy-dependent tissues, above all the brain. Clinically this manifests as a childhood-onset, infection-triggered **Leigh-like metabolic encephalopathy** with coma, hypotonia, seizures, lactic acidosis, elevated brain lactate on MR spectroscopy, bilateral basal-ganglia lesions, dysautonomia ("neurostorming"), and, in severe cases, multiorgan failure and death.

Because the lesion is accumulation of a *diffusible toxin* rather than a fixed structural defect in the respiratory chain, SQORD is explicitly framed as **potentially treatable**: current management is supportive (prompt treatment of metabolic crises, aggressive treatment of intercurrent illness, avoidance of catabolic triggers), while mechanism-based strategies aim to lower the H₂S burden (pharmacological sulfide scavenging, candidate cobalamin-based scavengers, limiting dietary sulfur/cysteine, and microbiome modulation). The disease was first delineated in 2020 in two families, including a Lehrerleut Hutterite founder mutation (p.Glu213Lys) with a carrier frequency of 1 in 13. Diagnosis rests on exome/genome or Leigh-panel sequencing showing biallelic SQOR variants together with isolated complex IV deficiency and preserved complex IV assembly. Information in this report is derived from aggregated disease-level resources and individual case reports, **not** from a structured EHR cohort.

---

## Key Findings

### Finding 1 — Biallelic SQOR variants cause a treatable Leigh-like mitochondrial disease

The disease entity was established by **Friederich et al. (2020)** in a study of two families [PMID: 32160317](https://pubmed.ncbi.nlm.nih.gov/32160317/). In **Family A**, two Hutterite sisters were homozygous for SQOR **c.637G>A (p.Glu213Lys)**; they presented with coma, lactic acidosis, multiorgan failure, hypotonia, neurostorming, and Leigh-like basal-ganglia lesions, and both died. In **Family B**, a boy homozygous for the frameshift variant **c.446delT** had recurrent (episodic) encephalopathy with basal-ganglia lesions.

The biochemistry pinpointed the mechanism: *"Muscle and liver tissue had isolated decreased complex IV activity, but normal complex IV protein levels and complex formation."* This dissociation — reduced **activity** with preserved **protein and assembly** — is the signature of enzymatic *inhibition* rather than a structural/assembly defect, pointing directly to a diffusible inhibitor. The authors identified it: *"Toxic hydrogen sulfide exposure inhibits complex IV."* Enzyme assays confirmed severely reduced SQOR activity and protein. The founder allele was characterized as: *"Both patients were homozygous for c.637G > A, which we identified as a founder mutation in the Lehrerleut Hutterite with a carrier frequency of 1 in 13."* The report's framing of SQORD as *"a potentially treatable cause of Leigh disease"* underpins its clinical importance.

### Finding 2 — SQOR is the committed first enzyme of H₂S catabolism, and tissue vulnerability tracks SQOR level

SQOR (EC 1.8.5.4) is an inner-mitochondrial-membrane flavoprotein that oxidizes H₂S and transfers electrons to ubiquinone/Coenzyme Q. Transient-kinetic work by **Mishanina et al. (2015)** [PMID: 26318450](https://pubmed.ncbi.nlm.nih.gov/26318450/) showed that *"the flavin cofactor is intermittently reduced by sulfide and oxidized by ubiquinone, linking H2S oxidation to the electron transfer chain and to energy metabolism"* (bound-flavin redox potential ≈ −123 mV). SQOR therefore both **detoxifies** H₂S and **feeds electrons** into the respiratory chain.

The physiological consequence of SQOR abundance was demonstrated across species by **Marutani, Ichinose et al. (2021)** [PMID: 34035265](https://pubmed.ncbi.nlm.nih.gov/34035265/). Comparing mice, rats, and the hypoxia-tolerant 13-lined ground squirrel, they found *"the sensitivity of the brain to hypoxia is inversely related to the levels of sulfide:quinone oxidoreductase (SQOR) and the capacity to catabolize sulfide."* Silencing SQOR increased hypoxia sensitivity; neuron-specific SQOR expression prevented hypoxia-induced sulfide accumulation, bioenergetic failure, and ischemic injury. Crucially for therapy: *"Pharmacological scavenging of sulfide maintained mitochondrial respiration in hypoxic neurons and made mice resistant to hypoxia."* This directly links low/absent SQOR activity to the brain's bioenergetic collapse — the core of SQORD — and nominates sulfide scavenging as a rational intervention.

### Finding 3 — Consolidated disease and gene identifiers

| Entity | Identifiers |
|---|---|
| **Disease** | MONDO:0030982 "sulfide quinone oxidoreductase deficiency" (syn. SQORD); OMIM #619221; GARD:0025671; MedGen/UMLS C5543168. No dedicated Orphanet/ICD-specific code identified. |
| **Gene** | **SQOR** (aliases SQRDL, SQR, CGI-44, PRO1975); NCBI Gene 58472; Ensembl ENSG00000137767; HGNC:20390; OMIM gene *617658; UniProt Q9Y6N5 |
| **Locus** | 15q21.1 (GRCh38 chr15:45,631,148–45,691,299, + strand) |

Verified via OLS4/MONDO and mygene.info.

### Finding 4 — Pathway context: ETHE1 (ethylmalonic encephalopathy) is the downstream "mirror" disorder

SQORD sits at the head of the mitochondrial sulfide-oxidation pathway:

```
H2S → [SQOR] → persulfide (GSSH) → [ETHE1 sulfur dioxygenase] → sulfite
          |                                                         |
     electrons → CoQ / ETC            [sulfite oxidase SUOX / rhodanese TST] → thiosulfate / sulfate
```

Loss of the **downstream** enzyme **ETHE1** causes **ethylmalonic encephalopathy** (OMIM #602473), which — like SQORD — produces H₂S accumulation and *"decreased activity of the mitochondrial complex IV, which limits energy production in tissues that require a large supply of energy"* [PMID: 40563372](https://pubmed.ncbi.nlm.nih.gov/40563372/). The shared complex IV defect in two enzymatically distinct disorders of the *same* pathway corroborates the "H₂S poisons complex IV" mechanism and defines SQORD and ETHE1 deficiency as pathophysiological mirror images (upstream vs. downstream lesions of sulfide catabolism).

### Finding 5 — Phenotype spectrum with HPO terms

Official HPO disease annotations for **OMIM:619221** (JAX ontology API) plus features reported in Friederich 2020:

| Phenotype | HPO term | Source |
|---|---|---|
| Acute encephalopathy | HP:0006846 | OMIM annotation |
| Coma | HP:0001259 | OMIM annotation |
| Tonic seizure | HP:0032792 | OMIM annotation |
| Migraine | HP:0002076 | OMIM annotation |
| Elevated brain lactate (MRS) | HP:0012707 | OMIM annotation |
| Lactic acidosis | HP:0003128 | OMIM annotation |
| Elevated circulating creatine kinase | HP:0003236 | OMIM annotation |
| Autosomal recessive inheritance | HP:0000007 | OMIM annotation |
| Basal ganglia / Leigh-like lesions | HP:0002518 / HP:0030900 | Friederich 2020 |
| Hypotonia | HP:0001252 | Friederich 2020 |
| Multiorgan failure | HP:0032263 | Friederich 2020 |
| Neurostorming / dysautonomia | HP:0012719 | Friederich 2020 |

The clinical core is captured by the report that the patient *"remained comatose, hypotonic, had neurostorming episodes, elevated lactate, and Leigh-like lesions on brain imaging"* [PMID: 32160317](https://pubmed.ncbi.nlm.nih.gov/32160317/). Onset ranged ~4–8 years; episodes were often triggered by intercurrent illness/catabolic stress; severe cases were rapidly fatal; at least one child had a recurrent/episodic course.

### Finding 6 — SQOR pathogenic variants are ultra-rare; LoF tolerated in heterozygosity

A gnomAD v4 query of **SQOR** (chr15, GRCh38) returned ~2,458 variants. All predicted loss-of-function alleles occur at very low frequencies (~7×10⁻⁷ to ~2.5×10⁻⁵):

| Variant | Consequence | Approx. allele freq (gnomAD v4) |
|---|---|---|
| c.799C>T (p.Arg267Ter) | nonsense | ~2.5×10⁻⁵ |
| c.415C>T (p.Arg139Ter) | nonsense | ~1.6×10⁻⁵ |
| c.446del (p.Leu149ArgfsTer18) — *Family B* | frameshift | ~2.05×10⁻⁶ |
| c.637G>A (p.Glu213Lys) — *Hutterite founder* | missense | ~absent outbred; carrier 1/13 Lehrerleut Hutterite |

No homozygotes for LoF alleles are present in the general population, consistent with severe recessive disease. SQOR tolerates heterozygous LoF (it is a recessive disease gene, not haploinsufficient). The founder missense — *"a founder mutation in the Lehrerleut Hutterite with a carrier frequency of 1 in 13"* [PMID: 32160317](https://pubmed.ncbi.nlm.nih.gov/32160317/) — is essentially absent from outbred populations.

### Finding 7 — Treatment rationale and model organisms

No approved disease-specific therapy exists. Management is **supportive**: treat acute metabolic/lactic crises, avoid catabolic triggers and fasting, and aggressively treat intercurrent illness that precipitates decompensation. **Mechanism-based** strategies target lowering H₂S: pharmacological sulfide scavenging *"maintained mitochondrial respiration in hypoxic neurons and made mice resistant to hypoxia"* [PMID: 34035265](https://pubmed.ncbi.nlm.nih.gov/34035265/). Candidate approaches include hydroxocobalamin/oxidized cobalamin and other sulfide-binding agents, and limiting sulfur/cysteine load. Gut-microbiome-derived H₂S contributes to total sulfide burden and modulates brain bioenergetics, suggesting dietary/microbiome modulation as an adjunct [PMID: 40526718](https://pubmed.ncbi.nlm.nih.gov/40526718/).

**Model organisms:** mouse (*Mus musculus*, Sqor NCBI Gene 59010) with SQOR silencing and neuron-specific re-expression recapitulates sulfide accumulation, bioenergetic failure, and brain hypoxia sensitivity [PMID: 34035265](https://pubmed.ncbi.nlm.nih.gov/34035265/); the hypoxia-tolerant 13-lined ground squirrel is a comparative high-SQOR model; invertebrate/parasite SQOR (*C. elegans*; *Schistosoma mansoni* [PMID: 41638445](https://pubmed.ncbi.nlm.nih.gov/41638445/)) illustrate conserved enzymology; patient fibroblasts, muscle, and liver were the primary human cellular models.

### Finding 8 — Human SQOR has solved experimental structures enabling variant modeling

PDBe best-structures mapping for UniProt **Q9Y6N5** returns 8 experimental structures: **6MO6, 6MP5, 6OI5, 6OI6, 6OIB, 6OIC, 6WH6, 8DHK**. These define the FAD flavoprotein fold and membrane-interacting/quinone-binding regions, enabling structural rationalization of pathogenic missense alleles — e.g., **p.Glu213Lys**, which disrupts hydrogen bonding with neighboring residues (Friederich 2020) — and a platform for classifying novel missense VUS (AlphaFold model AF-Q9Y6N5 also available).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variants in *SQOR*** (e.g., p.Glu213Lys missense; c.446delT frameshift) **lead to** loss of functional sulfide:quinone oxidoreductase in the inner mitochondrial membrane. *(Demonstrated: reduced SQOR activity + protein in patient tissue.)*
2. Loss of SQOR **results in** failure of the committed first step of mitochondrial H₂S oxidation, so endogenous and gut-derived H₂S cannot be catabolized. *(Inferred from enzyme role; directly demonstrated in SQOR-silenced models.)*
3. Blocked catabolism **leads to** accumulation of H₂S (and upstream persulfide species), especially when production rises during intercurrent illness/catabolism (*branch point where environment feeds in*). *(Demonstrated in mouse models; inferred in patients.)*
4. Accumulated H₂S **inhibits** complex IV (cytochrome c oxidase) — an *isolated, functional* COX defect with *normal* complex IV protein and assembly. *(Demonstrated in patient muscle and liver.)*
5. Complex IV inhibition **results in** blocked oxidative phosphorylation and ATP failure, with a shift to anaerobic glycolysis → **lactic acidosis and elevated brain lactate (MRS)**. *(Demonstrated clinically/biochemically.)*
6. Bioenergetic failure concentrates in the brain's most metabolically demanding gray matter → **bilateral basal-ganglia (Leigh-like) lesions, encephalopathy, coma, seizures, hypotonia, dysautonomia**. *(Demonstrated by imaging and clinical course.)*
7. Catabolic stress raises sulfide flux and energetic demand → **episodic metabolic decompensation**, progressing to **multiorgan failure and death** in severe cases. *(Demonstrated: infection-triggered, fatal outcomes in Family A.)*

**Protective counterfactual branch:** restoring H₂S clearance (SQOR re-expression) or scavenging sulfide **prevents** steps 4–8 (shown in neurons/mice; Marutani 2021).

### Upstream vs. downstream

- **Upstream (primary lesion):** SQOR genotype → enzyme loss → H₂S accumulation.
- **Downstream (effector):** complex IV inhibition → OXPHOS failure → lactic acidosis → basal-ganglia injury → encephalopathy.
- **Pathway sibling:** ETHE1 deficiency produces the *same downstream* complex IV defect from a lesion one step *below* SQOR, confirming the mechanism and the shared therapeutic rationale (lower H₂S).

### Ontology annotations

- **Biological process (GO):** hydrogen sulfide metabolic process (GO:0070813); sulfide oxidation (GO:0019417); oxidative phosphorylation (GO:0006119); cellular respiration (GO:0045333).
- **Cellular component (GO):** mitochondrion (GO:0005739); mitochondrial inner membrane (GO:0005743).
- **Cell types (CL):** neuron (CL:0000540), especially basal-ganglia/striatal neurons; astrocyte (CL:0000127); broadly high-OXPHOS cells (myocyte CL:0000187; hepatocyte CL:0000182).
- **Anatomy (UBERON):** brain (UBERON:0000955), basal ganglia (UBERON:0002420), striatum (UBERON:0002435), brainstem (UBERON:0002298), skeletal muscle (UBERON:0001134), liver (UBERON:0002107).
- **Chemical entities (CHEBI):** hydrogen sulfide (CHEBI:16136); ubiquinone/CoQ (CHEBI:16389); FAD (CHEBI:16238); L-lactate (CHEBI:16651); thiosulfate (CHEBI:33542); L-cysteine (CHEBI:17561).
- **Treatment (NCIT):** supportive care (NCIT:C15277); hydroxocobalamin (NCIT:C47707/C47642); sulfide-scavenging agents (investigational).

---

## Section-by-Section Dossier

### 1. Disease Information
Autosomal-recessive mitochondrial inborn error of H₂S catabolism presenting as a Leigh-like metabolic encephalopathy. **Identifiers:** MONDO:0030982; OMIM #619221; GARD:0025671; MedGen/UMLS C5543168; no dedicated Orphanet/ICD-specific code (best coded under mitochondrial/metabolic encephalopathy, ICD-10 E88.8; ICD-11 Leigh-syndrome category by phenotype). **Synonyms:** SQORD; sulfide:quinone oxidoreductase deficiency; SQR deficiency (gene aliases SQRDL, SQR, CGI-44, PRO1975). The knowledge base is disease-level/case-report derived, not EHR-based.

### 2. Etiology
**Primary cause:** biallelic pathogenic SQOR variants → loss of function. **Genetic risk:** carrier status; founder/consanguineous membership (Hutterite carrier 1/13). **Environmental triggers of crises (not causes):** intercurrent infection, fasting, catabolic stress; dietary sulfur/cysteine and gut-microbiome H₂S add to burden. **Protective factors (inferred):** higher residual SQOR activity; lower sulfide load. **Gene–environment interaction:** a fixed genetic enzymatic bottleneck is overwhelmed when H₂S production rises — a threshold GxE interaction precipitating complex IV inhibition.

### 3. Phenotypes
See Finding 5 table. **Types:** clinical signs (coma, hypotonia, seizures, dysautonomia), lab abnormalities (lactic acidosis, elevated brain lactate by MRS, elevated CK), imaging (bilateral basal-ganglia/Leigh-like lesions). **Onset:** childhood (~4–8 y). **Severity:** variable — fatal metabolic coma to recurrent survivable encephalopathy. **Progression:** episodic/fluctuating with stepwise injury accrual. **QoL impact:** profound — intensive-care dependence, death in severe cases, fixed neurological sequelae (dystonia, developmental impairment) in survivors. No formal EQ-5D/SF-36/PROMIS data exist.

### 4. Genetic / Molecular Information
**Causal gene:** SQOR (15q21.1), ~450-aa FAD flavoprotein on the inner mitochondrial membrane. **Reported variants:** c.637G>A p.Glu213Lys (destabilizing missense, founder, LoF-equivalent) and c.446delT p.Leu149ArgfsTer18 (frameshift/null). Population nulls (p.Arg267Ter, p.Arg139Ter) ultra-rare, no homozygotes. **Classification:** pathogenic (segregation, founder data, functional enzyme loss, complex IV biochemistry). **Consequence:** loss of function; **germline** origin. **Modifiers:** none established (plausibly ETHE1, TST, SUOX, CBS, CTH, MPST). SQOR is an **NRF2 target** (PMID 36758466), relevant to expression regulation but not a described modifier. **Epigenetics / chromosomal abnormalities:** none reported.

### 5. Environmental Information
Non-genetic **modulators** rather than causes: intercurrent illness and catabolic stress trigger crises; dietary sulfur/cysteine and gut-microbiome H₂S (e.g., *Desulfovibrio* spp.) add to sulfide burden [PMID: 40526718](https://pubmed.ncbi.nlm.nih.gov/40526718/). Exogenous H₂S is the toxicological analogue (H₂S inhibits complex IV). No infectious etiology.

### 6. Mechanism / Pathophysiology
See the ordered causal chain above. Core pathway: **SQOR loss → H₂S accumulation → complex IV inhibition → OXPHOS failure → lactic acidosis + basal-ganglia injury → encephalopathy.** Supported by isolated functional complex IV deficiency with normal assembly ([PMID: 32160317](https://pubmed.ncbi.nlm.nih.gov/32160317/)), SQOR enzymology ([PMID: 26318450](https://pubmed.ncbi.nlm.nih.gov/26318450/)), the SQOR-level/hypoxia-sensitivity relationship ([PMID: 34035265](https://pubmed.ncbi.nlm.nih.gov/34035265/)), and the ETHE1 pathway mirror ([PMID: 40563372](https://pubmed.ncbi.nlm.nih.gov/40563372/)). No dedicated patient omics cohort exists; functional assays are SQOR activity, western blot, respirometry, and complex IV activity.

### 7. Anatomical Structures Affected
**Primary organ:** brain (basal ganglia, brainstem; Leigh-like). **Secondary:** skeletal muscle and liver (biochemical COX deficiency); multiorgan failure in crises. **Body systems:** nervous (primary), musculoskeletal, hepatic, cardiovascular (during decompensation), autonomic. **Subcellular:** mitochondrion / inner mitochondrial membrane. **Lateralization:** bilateral, often symmetric basal-ganglia involvement.

### 8. Temporal Development
**Onset:** childhood (~4–8 y), acute/subacute, infection-triggered; a milder later spectrum possible (migraine annotation). **Course:** episodic/relapsing with stepwise accrual; rate from fulminant/fatal to recurrent over years. **Duration:** lifelong susceptibility. **Critical periods:** intercurrent infection/fasting (vulnerability) and the acute crisis (narrow window for metabolic rescue).

### 9. Inheritance and Population
**Inheritance:** autosomal recessive (HP:0000007). **Penetrance:** high/complete for biallelic null genotypes; **expressivity variable** (fatal vs recurrent). **Epidemiology:** ultra-rare; precise prevalence/incidence unknown; enriched in founder/consanguineous groups. **Founder/carrier frequency:** Lehrerleut Hutterite 1/13 for c.637G>A; no LoF homozygotes in gnomAD. **Consanguinity:** increases risk. **Anticipation/germline mosaicism:** not applicable/not reported. **Demographics:** pediatric; both sexes (no sex bias expected).

### 10. Diagnostics
**Genetic testing (first-line, confirmatory):** WES/WGS or mitochondrial/Leigh nuclear-gene panel including SQOR; targeted founder-variant/cascade testing in Hutterite families; mtDNA testing to exclude mtDNA Leigh syndrome. CMA/karyotype/FISH/repeat testing not indicated. **Biochemical:** isolated decreased complex IV activity with **normal** complex IV protein/assembly (key discriminator); reduced SQOR activity/protein; lactic acidosis; elevated CK; candidate urinary **thiosulfate**/sulfur-metabolite biomarkers (needs validation). **Imaging:** MRI bilateral basal-ganglia (± brainstem/cortical) Leigh-like lesions; MRS lactate peak. **Differential diagnosis:** mtDNA/nuclear Leigh syndrome (SURF1, MT-ATP6); **ETHE1 ethylmalonic encephalopathy** (distinguished by ethylmalonic aciduria, acrocyanosis/petechiae, chronic diarrhea); other pediatric lactic-acidosis/metabolic-coma causes. **Screening:** cascade carrier testing in founder populations; prenatal/PGT for known familial variants; not in standard newborn screening.

### 11. Outcome / Prognosis
Guarded: both Family A sisters died; the Family B boy had recurrent encephalopathy. Survivors risk fixed neurological sequelae from basal-ganglia injury; recurrent crises drive cumulative disability. **Complications:** metabolic coma, status epilepticus, multiorgan failure, aspiration, dysautonomia. **Recovery:** crisis recovery possible with prompt metabolic management; genetic defect persists (lifelong risk). **Prognostic factors:** genotype/residual activity, age at first crisis, speed of rescue, trigger burden; extent of lactate elevation and basal-ganglia injury on MRI.

### 12. Treatment
No approved disease-specific therapy; care is supportive + mechanism-based/investigational. **Supportive (NCIT:C15277):** treat lactic acidosis, provide anti-catabolic/glucose support, avoid fasting, aggressively treat infections, ICU support; empirical mitochondrial cofactor "cocktail." **Mechanism-based (investigational):** sulfide scavenging (preclinical support, [PMID: 34035265](https://pubmed.ncbi.nlm.nih.gov/34035265/)); hydroxocobalamin/cobalamin sulfide-binding species; dietary sulfur/cysteine restriction; gut-microbiome modulation [PMID: 40526718](https://pubmed.ncbi.nlm.nih.gov/40526718/). **Advanced therapeutics (not developed):** gene therapy/enzyme replacement conceptually attractive; no gene/cell/RNA/targeted/immunotherapy exists. **Surgical/pharmacogenomics:** none. **Trials:** no SQORD-specific registered trials identified.

### 13. Prevention
**Primary:** genetic counseling and carrier/cascade screening in founder/consanguineous populations (Hutterite 1/13); preconception/prenatal/PGT for known variants. **Secondary:** early molecular diagnosis in at-risk sibs; prompt crisis recognition; avoid fasting. **Tertiary:** aggressive infection management, "sick-day" protocols, and investigational H₂S-lowering to prevent recurrent injury. **Counseling:** 25% recurrence risk per pregnancy for carrier couples. **Immunization/public health:** childhood immunization reduces infectious triggers; avoid exogenous sulfide.

### 14. Other Species / Natural Disease
SQOR is deeply conserved (bacteria→mammals). Orthologs: mouse *Sqor* (NCBI Gene 59010, NCBITaxon:10090), rat (10116), zebrafish (7955), *C. elegans* (6239), *Schistosoma mansoni* (6183). No naturally occurring Mendelian SQOR-deficiency disease catalogued in OMIA. Comparative biology: sulfide-tolerant organisms (*S. mansoni* in sulfide-rich mesenteric veins, [PMID: 41638445](https://pubmed.ncbi.nlm.nih.gov/41638445/); *C. elegans* rhodoquinone chain in sulfide) and high-SQOR hypoxia-tolerant ground squirrels illustrate conserved sulfide-defense biology. Not zoonotic/transmissible.

### 15. Model Organisms
**Mouse** (silencing + neuron-specific re-expression) recapitulates sulfide accumulation, bioenergetic failure, and brain hypoxia sensitivity ([PMID: 34035265](https://pubmed.ncbi.nlm.nih.gov/34035265/)); links gut sulfide to brain bioenergetics ([PMID: 40526718](https://pubmed.ncbi.nlm.nih.gov/40526718/)). **Comparative:** 13-lined ground squirrel (high-SQOR, protected). **Invertebrate/microbial:** *C. elegans*, *S. mansoni*, bacterial SQR for conserved enzymology. **In vitro/cellular:** patient fibroblasts, muscle, liver; hypoxic primary neurons for scavenging rescue. **Phenotype recapitulation:** strong for mechanism/tissue vulnerability; a faithful constitutive-knockout replicating the full *triggered episodic Leigh-like crisis* phenotype is not well established (a key gap). **Resources:** MGI (*Sqor*), Alliance of Genome Resources, IMPC/KOMP.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [32160317](https://pubmed.ncbi.nlm.nih.gov/32160317/) | *Pathogenic variants in SQOR … a potentially treatable cause of Leigh disease* | **Primary clinical delineation** — two families, variants, founder effect, isolated functional complex IV deficiency with normal assembly, H₂S mechanism |
| [34035265](https://pubmed.ncbi.nlm.nih.gov/34035265/) | *Sulfide catabolism ameliorates hypoxic brain injury* | SQOR level ∝ brain hypoxia resistance; sulfide scavenging rescues respiration — mechanistic + therapeutic basis; mouse model |
| [26318450](https://pubmed.ncbi.nlm.nih.gov/26318450/) | *Transient Kinetic Analysis … human SQOR* | Defines SQOR biochemistry coupling H₂S oxidation to the ETC via flavin/ubiquinone |
| [40563372](https://pubmed.ncbi.nlm.nih.gov/40563372/) | *mtUPR activation … Ethylmalonic Encephalopathy* | ETHE1 (downstream) deficiency causes the same complex IV defect — pathway corroboration |
| [40526718](https://pubmed.ncbi.nlm.nih.gov/40526718/) | *Gut sulfide metabolism modulates behavior and brain bioenergetics* | Gut-microbiome H₂S contributes to sulfide burden — supports dietary/microbiome adjuncts |
| [41638445](https://pubmed.ncbi.nlm.nih.gov/41638445/) | *S. mansoni SQOR charge-transfer complex* | Evolutionary conservation of SQOR enzymology; comparative model |
| [36758466](https://pubmed.ncbi.nlm.nih.gov/36758466/) | *NRF2 contribution to sulfur metabolism and mitochondrial activity* | SQOR as NRF2 target; expression regulation context |
| 38521487 | *Sulfide catabolism in hibernation and neuroprotection* | Review linking sulfide catabolism, hypoxia, and Leigh syndrome |

**Evidence source types:** human clinical/biochemical (Friederich 2020), model organism (Marutani 2021; ETHE1 cellular models), in vitro enzymology (Mishanina 2015), and database/computational (gnomAD v4, OLS4/MONDO, mygene.info, JAX HPO API, PDBe).

**Supported hypotheses:** (1) biallelic SQOR LoF causes an AR Leigh-like disease; (2) mechanism = H₂S accumulation → complex IV inhibition → energy failure (isolated functional COX defect with normal assembly); (3) ultra-rare, founder-enriched (Hutterite 1/13); (4) childhood-onset, episodic, infection-triggered; (5) "potentially treatable" via H₂S lowering (preclinical support).

**Refuted / excluded:** complex IV deficiency is *not* a structural/assembly defect (protein and assembly normal); not mtDNA-encoded; SQOR is not haploinsufficient (heterozygous LoF tolerated); not associated with common population variants, CNVs, or disease-specific epigenetic lesions.

---

## Limitations and Knowledge Gaps

- **Very small evidence base.** The disease rests primarily on **two families (three patients)** from a single 2020 report. Prevalence, incidence, full phenotype spectrum, penetrance, expressivity, and natural history outside the Hutterite founder context are essentially unknown; the migraine annotation hints at an under-recognized milder spectrum.
- **No approved therapy and no clinical-trial data.** Sulfide-scavenging and cobalamin-based strategies rest on preclinical/mechanistic data only; efficacy, dosing, and safety in SQORD patients are untested.
- **Indirect in-patient H₂S measurement.** Human-tissue H₂S accumulation is inferred from complex IV biochemistry and model-organism data rather than directly quantified.
- **No validated routine biomarker.** Urinary thiosulfate/sulfur metabolites need validation specifically for SQORD.
- **No crisis-faithful knockout disease model.** Existing mouse work used silencing/re-expression focused on hypoxia, not a constitutive knockout reproducing the triggered episodic phenotype.
- **No dedicated omics datasets** (transcriptomic/proteomic/metabolomic) for patients; no Orphanet/ICD-specific entry.
- **Modifier genes and genotype–phenotype correlations** are not established.

## Proposed Follow-up Experiments / Actions

1. **Establish a patient/variant registry** (GeneMatcher, clinician networks) to identify additional SQORD cases and define phenotype spectrum, penetrance, and natural history.
2. **Build a faithful Sqor-knockout (and p.Glu213Lys knock-in) mouse**, plus patient-iPSC-derived neurons/organoids, to quantify H₂S accumulation, complex IV inhibition, and basal-ganglia vulnerability, and to serve as a therapeutic testbed.
3. **Preclinical efficacy testing of sulfide-lowering interventions** — pharmacological scavengers, hydroxocobalamin/oxidized cobalamin, dietary sulfur/cysteine restriction, and microbiome modulation — with respiration/ATP and survival endpoints.
4. **Develop and validate biomarkers of sulfide burden** (plasma/urine thiosulfate, sulfide/persulfide species, brain-lactate MRS) for diagnosis, crisis prediction, and treatment monitoring.
5. **Structure-guided variant classification** using the 8 solved human SQOR structures and AlphaFold to triage novel missense VUS by predicted effect on FAD binding, quinone access, and membrane interaction.
6. **Carrier-screening and crisis-prevention protocols** for founder/consanguineous populations (Hutterite p.Glu213Lys), including "sick-day" management guidelines to pre-empt catabolic decompensation.

---

*Report compiled from eight confirmed findings across five investigation iterations and 23 reviewed papers. Evidence is strongest for the gene–enzyme–mechanism axis (SQOR loss → H₂S accumulation → complex IV inhibition → Leigh-like encephalopathy) and weakest for epidemiology and therapy, which remain to be defined. Only attributions supported by the cited abstracts/snippets are made; titles alone were not used to infer paper content.*


## Artifacts

- [OpenScientist final report](Sulfide_Quinone_Oxidoreductase_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Sulfide_Quinone_Oxidoreductase_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 11 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0032263` (1 mention) - the report calls it "Multiorgan failure"; HP calls it **Increased blood pressure**
- `HP:0012719` (1 mention) - the report calls it "Neurostorming / dysautonomia"; HP calls it **Functional abnormality of the gastrointestinal tract**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0012707` (1 mention) - the report calls it "Elevated brain lactate (MRS)"; HP calls it **Elevated brain lactate level by MRS**
- `HP:0003236` (1 mention) - the report calls it "Elevated circulating creatine kinase"; HP calls it **Elevated circulating creatine kinase activity**, and lists "Elevated circulating creatine phosphokinase" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `GARD`, `OMIM`.