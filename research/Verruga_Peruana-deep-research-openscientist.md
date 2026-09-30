---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-28T10:38:34.564411'
end_time: '2026-09-28T10:53:19.931742'
duration_seconds: 885.37
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Verruga Peruana
  mondo_id: MONDO:0971058
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
citation_count: 20
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 21
  on_topic: 17
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 22
  verified: 22
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 15
  labels_variant: 6
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Verruga_Peruana-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Verruga_Peruana-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Verruga Peruana
- **MONDO ID:** MONDO:0971058 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Verruga Peruana** covering all of the
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

# Verruga Peruana (Peruvian Wart) — Comprehensive Disease Characterization Report

**Disease:** Verruga Peruana (chronic eruptive phase of Carrión's disease)
**MONDO ID:** MONDO:0971058
**Category:** Infectious Disease (neglected tropical, vector-borne, bacterial)
**Investigation:** 5 iterations · 16 confirmed findings · 71 papers reviewed
**Evidence base:** Aggregated disease-level literature (reviews, clinical series, meta-analysis, in vitro/molecular studies). No individual-patient (EHR) data or primary datasets were provided.

---

## Summary

**Verruga Peruana ("Peruvian wart") is the chronic, eruptive tissue phase of Carrión's disease, a biphasic bacterial infection caused by the sand fly–transmitted α-proteobacterium *Bartonella bacilliformis* (rarely *B. ancashensis* or *B. rochalimae*).** It is endemic to the Andean valleys of Peru, Ecuador, and Colombia (typically 500–3,200 m elevation), where an estimated **1.7 million people are at risk**. The disease is purely infectious and vector-borne: there is **no human genetic etiology, no causal gene, and no inheritance pattern**. The relevant genetics belong entirely to the pathogen.

The core biology is best summarized as **one pathogen with two tropisms**. After inoculation by a *Lutzomyia*/*Pintomyia* sand fly, *B. bacilliformis* pursues two distinct cellular targets. In the **acute phase (Oroya fever)**, it invades and lyses circulating **erythrocytes** — up to 100% parasitized and 80% lysed — producing severe, often-fatal hemolytic anemia. In the **chronic eruptive phase (verruga peruana)**, tropism shifts to **dermal vascular endothelial cells**, where the bacterium drives pathological angiogenesis to produce crops of bleeding, angioproliferative skin nodules. The autotransporter **BafA** promotes endothelial proliferation via **VEGF-receptor signaling**, while an immunosuppressive, TH1-downregulated, pro-angiogenic (IL-10-high) cytokine milieu facilitates persistence.

Clinically, the two phases diverge sharply in prognosis and treatment. Untreated Oroya fever carries high mortality; the eruptive verruga phase is rarely fatal and its nodules regress once the bacterial stimulus is cleared. Treatment is **phase-specific** — ciprofloxacin (or chloramphenicol + penicillin G) for the acute phase, and **rifampin or azithromycin** for the eruptive phase. Prevention relies on **sand fly vector control and early case detection**; there is **no licensed vaccine**, only preclinical *in silico* multi-epitope candidates. Diagnosis rests on peripheral blood smear/culture (acute) and skin biopsy with **Warthin-Starry silver staining** (eruptive), supported by PCR and serology. The disease remains neglected: asymptomatic carriers sustain transmission, diagnostics miss low-bacteremia carriers, and antibiotic-resistant strains are emerging.

---

## Key Findings

### F001 — Verruga Peruana is the chronic eruptive phase of Carrión's disease

Verruga peruana is the **tissue/eruptive phase** of the biphasic **Carrión's disease**, caused by *Bartonella bacilliformis*, a motile, flagellated, Gram-negative intracellular α-proteobacterium. The eruptive phase is characterized by eruptive nodules that commonly bleed, plus arthralgias, with **currently very low mortality** — in stark contrast to the acute Oroya fever phase. A second causal agent, *Bartonella ancashensis*, was isolated from Verruga Peruana patients in the rural Ancash region of Peru.

> *"produces in its tissue phase a characteristic dermal eruption (Verruga peruana) resulting from a pronounced endothelial cell proliferation"* — [PMID: 1693472](https://pubmed.ncbi.nlm.nih.gov/1693472/)

> *"The eruptive phase, also known as Peruvian Wart, is characterized by eruptive nodes (which commonly bleed) and arthralgias. The mortality of the eruptive phase is currently extremely low."* — [PMID: 15798808](https://pubmed.ncbi.nlm.nih.gov/15798808/)

> *"Bartonella ancashensis, which was isolated in blood samples from 2 patients living in Caraz, Peru, during a clinical trial of treatment for bartonellosis"* — [PMID: 28221130](https://pubmed.ncbi.nlm.nih.gov/28221130/)

**Synonyms / alternative names:** Peruvian wart, Verruga peruana, eruptive-phase bartonellosis, chronic-phase Carrión's disease. **Identifiers:** MONDO:0971058; MeSH "Bartonella bacilliformis"/"Bartonella Infections"; ICD-10 A44.1 (cutaneous/mucocutaneous bartonellosis), A44.0 (systemic/Oroya fever); ICD-11 1C11.1. This is an aggregated disease-level characterization (not derived from individual EHR patients).

### F002 — Pathological angiogenesis via VEGF-receptor signaling (BafA)

Verruga formation results from *B. bacilliformis*-driven endothelial cell proliferation and pathological angiogenesis. Bacterial extracts stimulate human endothelial cell proliferation **up to three times control** and induce new blood-vessel formation *in vivo*. The autotransporter **BafA** passenger domain promotes endothelial angiogenesis via **VEGF-receptor signaling**. Histologically, bacteria reside in the interstitium and within endothelial cytoplasm (Rocha-Lima inclusions).

> *"B. bacilliformis possess an activity that stimulates endothelial cell proliferation up to three times that of control"* — [PMID: 1693472](https://pubmed.ncbi.nlm.nih.gov/1693472/)

> *"B. bacilliformis extracts stimulate the formation of new blood vessels in an in vivo model for angiogenesis"* — [PMID: 1693472](https://pubmed.ncbi.nlm.nih.gov/1693472/)

> *"Bartonella bacilliformis is a Gram-negative bacterial pathogen that provokes pathological angiogenesis and causes Carrion's disease, a neglected tropical disease restricted to South America"* — [PMID: 35379004](https://pubmed.ncbi.nlm.nih.gov/35379004/)

**Ontology suggestions:** GO:0001525 (angiogenesis), GO:0001938 (positive regulation of endothelial cell proliferation), GO:0048010 (VEGF receptor signaling pathway); CL:0000115 (endothelial cell); protein: BafA autotransporter.

### F003 — Sand fly transmission; endemic Andean valleys; ~1.7 million at risk

Transmission is by phlebotomine sand flies (*Lutzomyia verrucarum* and related *Pintomyia*/*Lutzomyia* spp.). *B. bacilliformis* DNA has been detected in *Pintomyia robusta* at the Ecuador–Peru border. The disease is endemic to Andean regions of Peru, Ecuador, and Colombia at 500–3,200 m; **~1.7 million South Americans are estimated at risk**. Seroprevalence of **28% among healthy children** in rural Loja Province, Ecuador, indicates widespread unrecognized infection.

> *"This infection is endemic of Andean regions and it is estimated that approximately 1.7 million of South Americans are at risk."* — [PMID: 26824740](https://pubmed.ncbi.nlm.nih.gov/26824740/)

> *"Seroprevalence of 28% was found among children in the study communities."* — [PMID: 29941982](https://pubmed.ncbi.nlm.nih.gov/29941982/)

**Ontology suggestions:** UBERON:0002097 (skin of body); vector taxa *Lutzomyia verrucarum*, *Pintomyia robusta*.

### F004 — Acute-phase hemolysis via porin A and an α/β-hydrolase

The acute phase (Oroya fever) is characterized by fatal hemolytic anemia. A Tn5 transposon screen identified **porin A and an α/β-hydrolase** as both **necessary and sufficient** for *B. bacilliformis*-induced hemolysis; the α/β-hydrolase catalytic triad (**Ser205, Asp267, His310**) is essential, and compound 48/80 inhibits hemolysis in the micromolar range. The bacterium invades and parasitizes erythrocytes, producing intracellular bacilli visible on blood smear.

> *"we determine that porin A and α/β-hydrolase are both necessary and sufficient for hemolysis induced by B. bacilliformis"* — [PMID: 41315277](https://pubmed.ncbi.nlm.nih.gov/41315277/)

> *"Carrion's disease is endemic to the South American Andes and is characterized by fatal hemolytic anemia."* — [PMID: 41315277](https://pubmed.ncbi.nlm.nih.gov/41315277/)

### F005 — Phase-specific treatment

Nationally standardized treatment for the **acute phase** in Peru is **ciprofloxacin**, with chloramphenicol plus penicillin G as an alternative. For the **eruptive (verruga peruana) phase** the recommended treatment is **rifampin** (azithromycin is also used). Emergence of antibiotic-resistant strains motivates anti-virulence and novel drug-target discovery efforts.

> *"There are nationally standardized treatments for the acute phase, which consist of ciprofloxacin, and alternatively chloramphenicol plus penicillin G."* — [PMID: 15798808](https://pubmed.ncbi.nlm.nih.gov/15798808/)

> *"During the eruptive phase the recommended treatment is rifampin"* — [PMID: 15798808](https://pubmed.ncbi.nlm.nih.gov/15798808/)

> *"the emergence of antibiotic-resistant strains underscores the urgent need for novel therapeutic interventions"* — [PMID: 41792177](https://pubmed.ncbi.nlm.nih.gov/41792177/)

**Ontology suggestions (NCIT):** Rifampin, Azithromycin, Ciprofloxacin, Chloramphenicol, Penicillin G.

### F006 — Clinical phenotype

The eruptive verruga phase presents with **crops of red-purple angiomatous papules/nodules** on skin (face, trunk, extremities) that commonly bleed and can ulcerate, accompanied by arthralgias and malaise. Peruvian wart may be clinically indistinguishable from bacillary angiomatosis. The preceding acute Oroya fever phase presents with fever, anorexia, malaise, nausea/vomiting, pallor, hepatomegaly, lymphadenopathy, cardiac murmur, jaundice, arthralgias, and severe hemolytic anemia. In pediatric outbreaks, children are the most affected group.

> *"Peruvian wart, caused by B. bacilliformis, may be indistinguishable from bacillary angiomatosis caused by the other two species."* — [PMID: 31780437](https://pubmed.ncbi.nlm.nih.gov/31780437/)

> *"In the pediatric population, the acute phase symptoms are fever, anorexia, malaise, nausea and/or vomiting. The main signs are pallor, hepatomegaly, lymphadenopathies, cardiac murmur, and jaundice."* — [PMID: 15798808](https://pubmed.ncbi.nlm.nih.gov/15798808/)

**Suggested HPO terms:** HP:0000988 (skin nodule), HP:0011276 (vascular skin abnormality), HP:0002829 (arthralgia), HP:0001945 (fever), HP:0001878 (hemolytic anemia — acute phase), HP:0002240 (hepatomegaly), HP:0002716 (lymphadenopathy), HP:0000952 (jaundice).

### F007 — Diagnosis and differential

Acute-phase diagnosis relies on **Giemsa-stained peripheral blood smear** (intraerythrocytic bacilli) and blood culture; eruptive-phase diagnosis rests on skin biopsy showing vascular proliferation with prominent endothelium and *Bartonella* aggregates, demonstrable by **Warthin-Starry silver stain**. Serology and PCR (16S-23S ITS, *gltA*, MLST) confirm. The angioproliferative nodules resemble **bacillary angiomatosis, Kaposi sarcoma, pyogenic granuloma, and epithelioid hemangioma** — the differential diagnosis.

> *"vessels with prominent endothelium and stroma rich in leukocytoclastic polymorphonuclears"* — [PMID: 12152480](https://pubmed.ncbi.nlm.nih.gov/12152480/)

> *"Histopathologically, BA may be confused with angiosarcoma, pyogenic granuloma and epithelioid hemangioma."* — [PMID: 10718405](https://pubmed.ncbi.nlm.nih.gov/10718405/)

> *"This bacterium is a fastidious slow growing microorganism, which is difficult and cumbersome to isolate from clinical sources"* — [PMID: 26824740](https://pubmed.ncbi.nlm.nih.gov/26824740/)

### F008 — Purely infectious etiology; no human genetics

Verruga Peruana / Carrión's disease is caused by infection with *B. bacilliformis* (rarely *B. ancashensis* or *B. rochalimae*), transmitted by phlebotomine sand flies. There is **no Mendelian inheritance, no human causal gene, no pathogenic germline/somatic variant, and no chromosomal abnormality**; OMIM has no gene entry. The relevant genetics are the pathogen's virulence genes: *bafA* (autotransporter), porin A, α/β-hydrolase, flagellin *flaA*, and the *ialB* invasion locus. *B. ancashensis* uniquely carries a **type IV secretion system** absent from *B. bacilliformis*.

> *"B. ancashensis contains type IV secretion system proteins, which are not present in B. bacilliformis"* — [PMID: 28221130](https://pubmed.ncbi.nlm.nih.gov/28221130/)

**Implication:** Sections on causal genes, pathogenic variants, modifier genes, epigenetics, chromosomal abnormalities, inheritance patterns, penetrance, carrier frequency, and genetic screening are **not applicable** to this disease as a host trait.

### F009 — Immunosuppressive, TH1-downregulated, pro-angiogenic cytokine profile

In 144 healthy Peruvian subjects from endemic/post-outbreak villages, bacteremia was associated with **low concentrations of TH1/pro-inflammatory mediators**: HGF (p=0.005), IL-15 (p=0.002), IL-6 (p=0.05), IP-10/CXCL10 (p=0.008), MIG/CXCL9 (p=0.03), and MIP-1α/CCL3 (p=0.03). Angiogenic chemokines and **IL-10 were positively associated** with infection. Recent acute infection (IgM+) showed lower eotaxin, IL-6, and VEGF but higher GM-CSF and IL-10.

> *"the same and further TH1-related and pro-inflammatory biomarkers were inversely associated with infection, whereas angiogenic chemokines and IL-10 were positively associated"* — [PMID: 28628613](https://pubmed.ncbi.nlm.nih.gov/28628613/)

> *"The presence of bacteremia was associated with low concentrations of HGF (p = 0.005), IL-15 (p = 0.002), IL-6 (p = 0.05), IP-10 (p = 0.008), MIG (p = 0.03) and MIP-1α (p = 0.03)"* — [PMID: 28628613](https://pubmed.ncbi.nlm.nih.gov/28628613/)

**Interpretation:** Immune evasion (TH1 suppression) and a pro-angiogenic/IL-10-high milieu together support bacterial persistence and feed the angioproliferative phenotype — immune modulation and angiogenesis are mechanistically coupled.

### F010 — Epidemiology and asymptomatic reservoir

A 2025 systematic review/meta-analysis (5 studies, 717 individuals, Peru & Ecuador) found IgG seropositivity of **28.21% (95% CI 6.29–33.39)** in healthy Ecuadorian children and a pooled molecular detection rate of **15.60% (95% CI 4.24–31.98)** in symptomatic Peruvian individuals. A gradual reduction in infection rates among acute febrile patients in Peru was observed. **Asymptomatic carriers act as a human reservoir**, and current PCR tools poorly detect low-bacteremia carriers.

> *"The percentage of seropositive IgG antibodies against B. bacilliformis was 28.21% (95% CI: 6.29-33.39) among healthy Ecuadorian children. In Peru, the pooled bacterial detection rate in symptomatic individuals was 15.60% (95% CI: 4.24-31.98)"* — [PMID: 40037746](https://pubmed.ncbi.nlm.nih.gov/40037746/)

> *"misdiagnosis, wrong treatments and perpetuation of asymptomatic carriers living in endemic areas"* — [PMID: 26959642](https://pubmed.ncbi.nlm.nih.gov/26959642/)

### F011 — Phase-dependent prognosis

Untreated acute-phase Carrión's disease (Oroya fever) has **high mortality**, driven by severe hemolytic anemia and superimposed infections (e.g., *Salmonella*) plus cardiovascular/neurologic complications. In contrast, mortality of the eruptive (verruga peruana) phase is **extremely low**, and the angioproliferative nodules **regress** once the bacterial stimulus is cleared. Antibiotic-resistant strains have been reported, and there is no vaccine.

> *"responsible for the Carrion's disease widely distributed in Ecuador, Peru, and Colombia with a high mortality rate when no specific treatment is received"* — [PMID: 32931955](https://pubmed.ncbi.nlm.nih.gov/32931955/)

> *"The mortality of the eruptive phase is currently extremely low."* — [PMID: 15798808](https://pubmed.ncbi.nlm.nih.gov/15798808/)

### F012 — Prevention: vector control; no vaccine

There is **no available vaccine**. Prevention is based on vector control against phlebotomine sand flies — insecticide spraying, insecticide-treated bed nets, protective clothing/repellents, and avoiding dusk-dawn exposure — plus early case detection and treatment to reduce the human reservoir. **Multi-epitope subunit vaccine candidates** (targeting flagellar biosynthetic protein, Pap31, heme/hemin transporters) have been designed by immunoinformatics but remain preclinical/*in silico*.

> *"Currently there is no available vaccine against B. bacilliformis. While antibiotics are the standard treatment, resistant strains have been reported, and there is a potential spread of the vector that transmits the bacteria."* — [PMID: 39566279](https://pubmed.ncbi.nlm.nih.gov/39566279/)

> *"B bacilliformis is transmitted by Sand fly (Lutzomyia verrucarum) to healthy individuals"* — [PMID: 32931955](https://pubmed.ncbi.nlm.nih.gov/32931955/)

### F013 — Erythrocyte tropism: adhesins bind spectrin, band 3, glycophorin A

During the acute phase, **up to 100% of circulating erythrocytes can be parasitized and 80% lysed**. *B. bacilliformis* binds multiple surface erythrocyte proteins: **spectrin (α/β, 230/210 kDa), band 3 (100 kDa), and glycophorin A (83 kDa)**, dependent on carbohydrate moieties. Invasion is mediated by invasion-associated loci **ialA/ialB**; *ialB* is induced by lower temperature (20°C) and acidic pH — cues signaling sandfly-to-host transmission — and repressed at 37°C. *B. bacilliformis* is the sole ancestral-lineage *Bartonella*, lacks the VirB/VirD4 T4SS, and the modern lineage uses the **Trw T4SS pilus** for erythrocyte invasion.

> *"During the primary disease phase, up to 100% of the circulating erythrocytes can be parasitized and 80% lysed. During the secondary phase of this disease, bacterial invasion shifts to endothelial cells lining the vasculature."* — [PMID: 12668141](https://pubmed.ncbi.nlm.nih.gov/12668141/)

> *"the 230 and 210 kDa proteins are the alpha and beta subunits of spectrin; the 100 and 83 kDa proteins are band 3 protein and glycophorin A"* — [PMID: 10968948](https://pubmed.ncbi.nlm.nih.gov/10968948/)

> *"Trw, is present in a sub-branch of the modern lineage. Trw does not translocate any known effectors, but produces multiple variant pilus subunits critically involved in the invasion of erythrocytes"* — [PMID: 18489724](https://pubmed.ncbi.nlm.nih.gov/18489724/)

**Ontology suggestions:** CL:0000232 (erythrocyte); GO:0007155 (cell adhesion); UBERON:0000178 (blood).

### F014 — Endothelial invasion requires tyrosine phosphorylation and α5β1 integrin

In the secondary (tissue) phase, invasion shifts to endothelial cells. Invasion of human endothelial (HUVEC) and epithelial (HEp-2) cells is reduced by protein kinase inhibitors **genistein** (tyrosine kinase) and **staurosporine** (PKC/tyrosine kinase) dose-dependently. Infection induces host **tyrosine phosphorylation** of multiple proteins (110–243 kDa), and anti-α5 and anti-β1 integrin antibodies moderately decrease uptake, implicating **α5β1 integrin** in bacterial entry into nucleated cells.

> *"exposure of normal human umbilical vein endothelial cells to staurosporine, a potent inhibitor of protein kinase C and some tyrosine protein kinases, resulted in a considerable reduction in the number of organisms internalized"* — [PMID: 10077844](https://pubmed.ncbi.nlm.nih.gov/10077844/)

> *"anti-alpha 5 and anti-beta 1 chain integrin monoclonal antibodies resulted in a moderate decrease in the invasion of these cells, suggesting a possible role of alpha 5 beta 1 integrins in the uptake"* — [PMID: 10077844](https://pubmed.ncbi.nlm.nih.gov/10077844/)

**Ontology suggestions:** GO:0007169 (transmembrane receptor protein tyrosine kinase signaling), GO:0007229 (integrin-mediated signaling pathway); protein: ITGA5/ITGB1 (α5β1 integrin).

### F015 — Anatomical involvement and model systems

Primary anatomical targets: **circulating erythrocytes/blood** (acute) and **dermal vascular endothelium/skin** (eruptive). Secondary organ involvement in severe acute disease includes liver (hepatomegaly), spleen (splenomegaly), lymph nodes (lymphadenopathy), heart (murmur/myocarditis), and CNS (neurobartonellosis). Model systems are **cellular/in vitro** (HUVEC, HEp-2, human erythrocyte-binding assays) and **entomological** (experimental colonization of *Lutzomyia* sand flies). **Humans (*Homo sapiens*, NCBI Taxon 9606) are the sole known reservoir**; there is no established natural non-human animal disease, though historically experimental infection of non-human primates (rhesus macaque) was used.

> *"B. bacilliformis is transferred between human hosts by the sandfly, Lutzomyia verrucarum"* — [PMID: 12668141](https://pubmed.ncbi.nlm.nih.gov/12668141/)

> *"colonize endothelial cells and erythrocytes of their mammalian reservoir hosts, thereby causing long-lasting intraerythrocytic infections"* — [PMID: 18489724](https://pubmed.ncbi.nlm.nih.gov/18489724/)

**Ontology suggestions:** UBERON:0002097 (skin), UBERON:0000178 (blood), UBERON:0001981 (blood vessel), UBERON:0002107 (liver), UBERON:0002106 (spleen); CL:0000115 (endothelial cell), CL:0000232 (erythrocyte).

### F016 — Integrated model: one pathogen, two tropisms

Synthesis of all findings: sand fly inoculation of *B. bacilliformis* → **Branch A** (IalA/IalB + flagella-mediated erythrocyte invasion via spectrin/band 3/glycophorin A; porin A/α-β-hydrolase hemolysis) → severe hemolytic anemia (Oroya fever, high untreated mortality); → **Branch B** (α5β1-integrin/tyrosine-kinase-dependent endothelial invasion + BafA/VEGFR-driven angiogenesis, aided by an IL-10/pro-angiogenic, TH1-suppressed immune milieu) → bleeding dermal angioproliferative nodules (verruga peruana, low mortality, regress with treatment). Endemic to Andean valleys (~1.7M at risk; 28% child seropositivity). Treatment is phase-specific; prevention is vector control.

> *"During the secondary phase of this disease, bacterial invasion shifts to endothelial cells lining the vasculature."* — [PMID: 12668141](https://pubmed.ncbi.nlm.nih.gov/12668141/)

> *"Bartonella bacilliformis is a Gram-negative bacterial pathogen that provokes pathological angiogenesis and causes Carrion's disease"* — [PMID: 35379004](https://pubmed.ncbi.nlm.nih.gov/35379004/)

---

## Mechanistic Model / Interpretation

### Ordered causal chain (from initiating infection to clinical manifestation)

```
1.  Phlebotomine sand fly (Lutzomyia verrucarum/Pintomyia spp.) bites human host
        │  leads to
2.  Inoculation of Bartonella bacilliformis into dermis/bloodstream
        │  results in (temperature/pH cues: 20°C, acidic → ialB induction)
3.  Flagella-driven motility + IalA/IalB adhesins engage host cells
        │
        ├──────────────── BRANCH A: ACUTE PHASE (Oroya fever) ────────────────
        │  4A. Adhesins bind erythrocyte spectrin (α/β), band 3, glycophorin A
        │        │  leads to
        │  5A. Trw T4SS pilus–mediated erythrocyte invasion (up to 100% parasitized)
        │        │  results in
        │  6A. Porin A + α/β-hydrolase (Ser205/Asp267/His310) drive hemolysis (80% lysed)
        │        │  leads to
        │  7A. Severe hemolytic anemia + secondary infections (Salmonella)
        │        │  results in
        │  8A. High untreated mortality (Oroya fever)
        │
        └──────────────── BRANCH B: CHRONIC PHASE (verruga peruana) ──────────
           4B. Tropism shifts to dermal vascular endothelial cells (HUVEC-type)
                 │  requires (inferred from in vitro inhibitor studies)
           5B. Host tyrosine-kinase signaling + α5β1 integrin–mediated internalization
                 │  concurrent with
           6B. TH1 suppression (↓IL-6, IP-10, MIG, MIP-1α) + ↑IL-10/pro-angiogenic milieu
                 │  leads to (immune evasion enables persistence)
           7B. BafA autotransporter passenger domain activates VEGF-receptor signaling
                 │  results in
           8B. Endothelial proliferation (up to 3× control) + neovascularization
                 │  produces
           9B. Crops of bleeding angioproliferative dermal nodules (Peruvian wart)
                 │  regress upon
          10B. Clearance of bacterial stimulus (rifampin/azithromycin) — low mortality
```

**Upstream vs downstream.** The upstream, shared initiating event is sand fly inoculation and adhesin-mediated cell engagement. The two branches diverge at the level of **cellular tropism** (erythrocyte vs endothelium), which is the master switch dividing the acute from the chronic phase. Within Branch B, immune modulation (F009) is **upstream/permissive**, BafA-VEGFR angiogenesis (F002) is the **central effector**, and the visible nodule (F006) is the **downstream manifestation**.

**Inferred vs demonstrated.** Erythrocyte receptors (F013), hemolysis effectors (F004), the BafA-VEGFR axis (F002), and the tropism shift (F013/F014) are experimentally demonstrated. The α5β1-integrin/tyrosine-kinase requirement (F014) is inferred from *in vitro* inhibitor and antibody-blocking studies (moderate effect sizes), not from *in vivo* human tissue. The coupling of the IL-10/TH1-suppressed milieu to nodule formation (F009) is an association from cross-sectional human cohorts, not a proven causal step.

### Two-tropism comparison

| Feature | Acute phase (Oroya fever) | Chronic phase (Verruga Peruana) |
|---|---|---|
| Target cell | Erythrocytes (CL:0000232) | Vascular endothelium (CL:0000115) |
| Key adhesins/receptors | Spectrin, band 3, glycophorin A; Trw pilus | α5β1 integrin; host tyrosine kinases |
| Effector mechanism | Porin A + α/β-hydrolase hemolysis | BafA → VEGFR → angiogenesis |
| Immune milieu | Massive parasitemia | TH1-suppressed, IL-10/pro-angiogenic |
| Clinical result | Severe hemolytic anemia | Bleeding angioproliferative skin nodules |
| Mortality (untreated) | High | Very low |
| First-line treatment | Ciprofloxacin (or chloramphenicol+PenG) | Rifampin (or azithromycin) |
| Course | Acute, life-threatening | Chronic, self-limited/regressing |

---

## Evidence Base

| PMID | Title (abbrev.) | Supports | Evidence type |
|---|---|---|---|
| [1693472](https://pubmed.ncbi.nlm.nih.gov/1693472/) | *B. bacilliformis stimulates endothelial cells / angiogenic in vivo* | F001, F002 (angiogenesis, tissue phase) | In vitro + in vivo model |
| [35379004](https://pubmed.ncbi.nlm.nih.gov/35379004/) | *BafA passenger domain promotes angiogenesis via VEGFR* | F002, F016 (VEGFR axis) | In vitro molecular |
| [28221130](https://pubmed.ncbi.nlm.nih.gov/28221130/) | *Whole-genome analysis of B. ancashensis* | F001, F008 (second species; T4SS) | Genomic |
| [26824740](https://pubmed.ncbi.nlm.nih.gov/26824740/) | *MLST of B. bacilliformis in Oroya fever outbreak* | F003, F007 (at-risk pop; fastidious culture) | Molecular epi |
| [29941982](https://pubmed.ncbi.nlm.nih.gov/29941982/) | *Seroprevalence in Loja, Ecuador* | F003 (28% child seroprevalence) | Serosurvey |
| [42127128](https://pubmed.ncbi.nlm.nih.gov/42127128/) | *B. bacilliformis DNA in Pintomyia robusta* | F003 (vector) | Entomological |
| [41315277](https://pubmed.ncbi.nlm.nih.gov/41315277/) | *Porin A and α/β-hydrolase necessary/sufficient for hemolysis* | F004 (hemolysis effectors) | Bacterial genetics |
| [15798808](https://pubmed.ncbi.nlm.nih.gov/15798808/) | *Bartonelosis in Peruvian pediatric population* | F001, F005, F006, F011 | Clinical review |
| [41792177](https://pubmed.ncbi.nlm.nih.gov/41792177/) | *Drug target mining for Oroya fever* | F005 (resistance) | Computational |
| [31780437](https://pubmed.ncbi.nlm.nih.gov/31780437/) | *Cutaneous manifestations of bartonellosis* | F006 (angiomatous nodule) | Clinical review |
| [12152480](https://pubmed.ncbi.nlm.nih.gov/12152480/) | *Bacillary angiomatosis* | F007 (histopathology) | Histopathology |
| [10718405](https://pubmed.ncbi.nlm.nih.gov/10718405/) | *BA affecting oral cavity* | F007 (differential dx) | Case/review |
| [28628613](https://pubmed.ncbi.nlm.nih.gov/28628613/) | *Immunosuppressive/angiogenic cytokine profile* | F009 (cytokines) | Human cohort (n=144) |
| [40037746](https://pubmed.ncbi.nlm.nih.gov/40037746/) | *Diagnosis of Carrion's disease: systematic review/meta-analysis* | F010 (seroprevalence, detection) | Meta-analysis |
| [26959642](https://pubmed.ncbi.nlm.nih.gov/26959642/) | *Evaluation of PCR approaches* | F010 (asymptomatic reservoir) | Diagnostic |
| [32931955](https://pubmed.ncbi.nlm.nih.gov/32931955/) | *Subtractive proteomics multi-epitope vaccine* | F011, F012 (mortality; vector) | Computational |
| [39566279](https://pubmed.ncbi.nlm.nih.gov/39566279/) | *Multi-epitope vaccine against Carrion disease* | F012 (no vaccine) | Immunoinformatics |
| [12668141](https://pubmed.ncbi.nlm.nih.gov/12668141/) | *Differential expression of ialB* | F013, F014, F015, F016 (tropism, ialB cues) | Bacterial genetics |
| [10968948](https://pubmed.ncbi.nlm.nih.gov/10968948/) | *Interaction with erythrocyte membrane proteins* | F013 (receptors) | In vitro |
| [18489724](https://pubmed.ncbi.nlm.nih.gov/18489724/) | *Infection-associated T4SS of Bartonella* | F013, F015 (Trw pilus; reservoir) | Review |
| [10077844](https://pubmed.ncbi.nlm.nih.gov/10077844/) | *Host tyrosine phosphorylation in HEp-2 invasion* | F014 (integrin/kinase) | In vitro |

**Consistency and independent corroboration.** The two-tropism model rests on multiple independent lines: bacterial genetics (F004, F013, F014), *in vitro* cell biology (F002, F014), human cohort immunology (F009), and molecular epidemiology (F003, F010). The angiogenesis mechanism is corroborated across a 1990 functional study (PMID 1693472) and a 2022 molecular study identifying BafA-VEGFR (PMID 35379004) — a 32-year span of consistent findings. No retrieved evidence contradicts the core model.

---

## Limitations and Knowledge Gaps

1. **No human genetics.** As a purely infectious disease, host-genetic sections of the template (causal genes, variants, inheritance, penetrance, epigenetics, chromosomal abnormalities, carrier/genetic screening, pharmacogenomics) are **not applicable**. This is a definitive negative finding (F008), not a data gap.
2. **Mechanistic steps in Branch B are partly inferred.** The α5β1-integrin/tyrosine-kinase requirement (F014) derives from *in vitro* inhibitor and antibody-blocking assays with moderate effect sizes; it has not been confirmed in human verruga tissue. The causal link between the IL-10/TH1-suppressed milieu (F009) and nodule formation is associative (cross-sectional cohort), not demonstrated by intervention.
3. **No robust animal model.** Humans are the sole reservoir (F015). There is no naturally occurring animal disease and no genetic model organism; work relies on cellular/*in vitro* systems and experimental sand fly colonization. This limits *in vivo* mechanistic and therapeutic testing.
4. **Diagnostic sensitivity gaps.** Current PCR poorly detects low-bacteremia asymptomatic carriers (F010), meaning prevalence is likely underestimated and the reservoir is imperfectly characterized.
5. **Sparse quantitative phenotype data.** Frequencies for individual verruga phenotypes (proportion with arthralgia, ulceration, mucosal involvement) and formal quality-of-life measures (EQ-5D/SF-36) are not available in the retrieved literature.
6. **Emerging species and resistance underexplored.** The clinical spectrum, virulence, and treatment response of *B. ancashensis* and *B. rochalimae*, and the prevalence/mechanisms of antibiotic resistance, remain poorly quantified.
7. **BafA-VEGFR pathway details.** Whether BafA acts directly on VEGFR or via induced host VEGF, and the downstream signaling (PI3K-AKT, MAPK) in verruga endothelium, are not fully resolved.

---

## Proposed Follow-up Experiments / Actions

1. **Validate the endothelial-entry receptor in situ.** Use immunohistochemistry/spatial transcriptomics on human verruga peruana biopsies to confirm α5β1 integrin engagement and map tyrosine-phosphorylation signaling in lesional endothelium (moving F014 from *in vitro* inference to *in vivo* demonstration).
2. **Dissect the BafA-VEGFR axis.** Test BafA passenger-domain mutants for VEGFR2 binding/phosphorylation, and profile downstream PI3K-AKT/MAPK activation in HUVEC; evaluate anti-VEGF/VEGFR agents (e.g., bevacizumab, kinase inhibitors) as adjuncts to shrink refractory nodules.
3. **Develop an improved diagnostic for asymptomatic carriers.** Benchmark ultrasensitive/droplet-digital PCR and serologic multiplex assays against latent-class models to close the low-bacteremia detection gap (F010) and better estimate the reservoir.
4. **Advance vaccine candidates beyond in silico.** Move multi-epitope constructs (Pap31, flagellar biosynthetic protein, heme transporters) into immunogenicity/challenge testing; establish a tractable *in vivo* or organoid endothelial model for protection assays.
5. **Characterize emerging species.** Systematic genomic and clinical comparison of *B. ancashensis* (T4SS+) and *B. rochalimae* isolates versus *B. bacilliformis* to define virulence determinants and phase-specific treatment response.
6. **Map antibiotic resistance.** Surveil rifampin/ciprofloxacin/azithromycin susceptibility across endemic Andean foci; correlate with treatment failure and define resistance mechanisms to guide anti-virulence drug development (e.g., α/β-hydrolase inhibitors building on compound 48/80).
7. **Vector-control trial.** Evaluate insecticide-treated bed nets plus active case detection/treat-to-clear-reservoir in a cluster-randomized design in high-transmission valleys.

---

## Applicability Notes for the Knowledge Base

- **Not applicable (host genetics):** causal genes, pathogenic variants, allele frequencies, modifier genes, epigenetics, chromosomal abnormalities, inheritance pattern, penetrance/expressivity, anticipation, mosaicism, founder effects, consanguinity, carrier frequency, genetic testing/screening, pharmacogenomics. Etiology is infectious (F008).
- **Pathogen taxonomy (NCBI Taxon):** *Bartonella bacilliformis*, *Bartonella ancashensis*, *Bartonella rochalimae*; vectors *Lutzomyia verrucarum*, *Pintomyia robusta*; host *Homo sapiens* (Taxon 9606).
- **Key UBERON:** skin (0002097), blood (0000178), blood vessel (0001981), liver (0002107), spleen (0002106).
- **Key CL:** endothelial cell (0000115), erythrocyte (0000232).
- **Key GO:** angiogenesis (0001525), VEGF receptor signaling (0048010), integrin-mediated signaling (0007229), positive regulation of endothelial cell proliferation (0001938).
- **Key NCIT (treatment):** Rifampin, Azithromycin, Ciprofloxacin, Chloramphenicol.


## Artifacts

- [OpenScientist final report](Verruga_Peruana-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Verruga_Peruana-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 21 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 6 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0048010` (1 mention) - the report calls it "VEGF receptor signaling pathway"; GO calls it **vascular endothelial growth factor receptor signaling pathway**, and lists "VEGF receptor signaling pathway" among its other names
- `CL:0000115` (3 mentions) - the report calls it "endothelial cell", "Vascular endothelium"; CL calls it **endothelial cell**, and lists "endotheliocyte" among its other names
- `UBERON:0002097` (2 mentions) - the report calls it "skin of body", "skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `HP:0000988` (1 mention) - the report calls it "skin nodule"; HP calls it **Skin rash**
- `HP:0001878` (1 mention) - the report calls it "hemolytic anemia — acute phase"; HP calls it **Hemolytic anemia**
- `GO:0007169` (1 mention) - the report calls it "transmembrane receptor protein tyrosine kinase signaling"; GO calls it **cell surface receptor protein tyrosine kinase signaling pathway**, and lists "transmembrane receptor protein tyrosine kinase signalling pathway" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000115` - called "endothelial cell", "Vascular endothelium"
- `UBERON:0002097` - called "skin of body", "skin"
- `CL:0000232` - called "erythrocyte", "Erythrocytes"

Every term resolved, and every label the report gave matched.