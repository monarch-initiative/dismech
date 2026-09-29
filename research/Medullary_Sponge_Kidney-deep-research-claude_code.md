---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-23T23:58:45.800539'
end_time: '2026-09-24T00:04:22.500965'
duration_seconds: 336.7
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Medullary Sponge Kidney
  mondo_id: MONDO:0015268
  category: Developmental
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 23
  num_turns: 32
  total_cost_usd: 1.8155274000000001
  session_id: 45ce5f1a-6721-5dd9-af0a-cb3620796386
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 43
reference_validation:
  total_references: 29
  verified: 29
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 29
  on_topic: 17
  validator_version: 0.2.1
term_validation:
  total_terms: 34
  verified: 32
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.03
  labels_checked: 11
  labels_matching: 7
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0015268
    reported_labels:
    - MONDO
    ontology_label: medullary sponge kidney
  - term_id: HP:0012622
    reported_labels:
    - Hypocitraturia; use as available in dynamic enum
    ontology_label: Chronic kidney disease
  - term_id: HP:0002900
    reported_labels:
    - Secondary to dRTA
    ontology_label: Hypokalemia
  labels_variant: 1
  unresolved_terms:
  - HP:0004735
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Medullary Sponge Kidney
- **MONDO ID:** MONDO:0015268 (if available)
- **Category:** Developmental

## Research Objectives

Please provide a comprehensive research report on **Medullary Sponge Kidney** covering all of the
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

I now have comprehensive material to compile the full report.

I now have sufficient depth across all sections. Compiling the comprehensive report.

# Medullary Sponge Kidney: Comprehensive Research Report

## 1. Disease Information

### Overview

Medullary sponge kidney (MSK), also known as Cacchi–Ricci disease or Lenarduzzi–Cacchi–Ricci disease, is a congenital/developmental renal malformation characterized by cystic dilatation of the medullary and papillary portions of the collecting ducts, producing a "sponge-like" appearance of the renal pyramids on gross pathology and imaging ([Wikipedia](https://en.wikipedia.org/wiki/Medullary_sponge_kidney); [GARD](https://rarediseases.info.nih.gov/diseases/232/medullary-sponge-kidney)). The cysts, typically 1–8 mm in diameter and filled with clear, jelly-like material, communicate proximally with collecting ducts of otherwise normal caliber ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK470220/); [Dovepress review](https://www.dovepress.com/medullary-sponge-kidney-current-perspectives-peer-reviewed-fulltext-article-IJNRD)). It is functionally defined by the resulting complications: nephrocalcinosis, recurrent calcium-based nephrolithiasis, incomplete distal renal tubular acidosis (dRTA), and recurrent urinary tract infection (UTI), while the renal cortex is typically spared and overall renal function is usually preserved.

### Key Identifiers

| Resource | Identifier |
|---|---|
| OMIM | 174000 |
| Orphanet | ORPHA:1309 |
| ICD-10-CM | Q61.5 (Medullary cystic kidney — the code covers both MSK and medullary cystic disease) |
| MeSH | D007691 |
| MONDO | MONDO:0015268 |

([GARD](https://rarediseases.info.nih.gov/diseases/232/medullary-sponge-kidney); [icd10data.com](https://www.icd10data.com/ICD10CM/Codes/Q00-QA0/Q60-Q64/Q61-/Q61.5))

### Synonyms

Cacchi–Ricci disease; Lenarduzzi–Cacchi–Ricci disease; renal tubular ectasia; precalyceal canalicular ectasia; sponge kidney disease ([Wikipedia "Cacchi-Ricci disease"](https://en.wikipedia.org/wiki/Cacchi-Ricci_disease)).

### Data Source Basis

Most published data derive from **aggregated clinical/radiologic case series and single-center cohorts** (Italian, French, US, and Chinese nephrology/urology referral populations), rather than large population-level EHR studies. Recent work has begun to layer in prospective phenotyping (functional MRI, metabolomics) and genomic cohorts recruited partly through patient-advocacy channels (e.g., a Facebook patient community used to recruit for a 2024 exome-sequencing study), reflecting the rarity and historical under-ascertainment of the disease ([JASN 2024 abstract](https://journals.lww.com/jasn/fulltext/2024/10001/genotyping_patients_with_medullary_sponge_kidney.1752.aspx)).

---

## 2. Etiology

### Disease Causal Factors

MSK is best understood as a **developmental anomaly of the distal nephron/collecting-duct system**, arising from disrupted interaction at the ureteric bud–metanephric mesenchyme interface during nephrogenesis ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK470220/); [Dovepress](https://www.dovepress.com/medullary-sponge-kidney-current-perspectives-peer-reviewed-fulltext-article-IJNRD)). Two broad causal frameworks have been proposed and are not mutually exclusive:

1. **Genetic/developmental hypothesis (GDNF–RET axis).** GDNF (glial cell line–derived neurotrophic factor), secreted by the metanephric blastema, signals through the RET receptor tyrosine kinase on the ureteric bud to drive branching morphogenesis. Disruption of this axis impairs growth and differentiation of the lower (distal) nephron segments, producing collecting-duct dilation and cyst formation ([CJASN, GDNF variant study](https://cjasn.asnjournals.org/content/5/7/1205.full); [Dovepress](https://www.dovepress.com/medullary-sponge-kidney-current-perspectives-peer-reviewed-fulltext-article-IJNRD)).
2. **Secondary/acquired obstructive hypothesis.** An alternative or contributing mechanism holds that collecting-duct dilation results from *in utero* tubular obstruction — proposed causes include occlusion by uric acid during fetal life, or obstruction by calcium oxalate microliths secondary to infantile hypercalciuria — rather than a primary branching defect ([WebSearch synthesis of StatPearls/Dovepress](https://www.ncbi.nlm.nih.gov/books/NBK470220/)).

A 2025–2026 wave of exome-sequencing studies reframes MSK as **genetically heterogeneous and likely polygenic** rather than a single-gene disorder in most patients (see Section 4).

### Risk Factors

**Genetic:**
- Family history / familial clustering — an apparent autosomal dominant pattern with **reduced penetrance and variable expressivity** has been repeatedly described; in one classic series, 5 of 8 MSK cases were familial, with allele variants cosegregating in a dominant pattern ([ScienceDirect, "Evidence for inheritance"](https://www.sciencedirect.com/science/article/pii/S0085253815557426)).
- Rare heterozygous **GDNF** variants — found in ~12% of a 57-patient Italian MSK cohort, clustering in a putative PAX2 transcription-factor binding domain ([CJASN](https://cjasn.asnjournals.org/content/5/7/1205.full)).
- **RET** variants/polymorphisms (e.g., G691S/S904S), also implicated in a subset, with mechanistic overlap with MEN2A-associated RET mutations ([PMC6036688](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6036688/)).
- **HNF1B** pathogenic variants — 6 novel HNF1B variants (3 frameshift, 2 missense, 1 nonsense) identified in a 2024 genotyping cohort, implicating this classic renal-developmental gene in a subset of MSK ([JASN abstract 2024](https://journals.lww.com/jasn/fulltext/2024/10001/genotyping_patients_with_medullary_sponge_kidney.1752.aspx)).
- Broader panel of candidate genes proposed from expression/genotyping studies: *HNF1B, CLCN5, GDNF, ATP6V0A4, ATP6V1B1, LAMA2, RET, ACAN, ABCC8* ([Li et al. 2022, BioMed Research International](https://pmc.ncbi.nlm.nih.gov/articles/PMC9674422/)).
- Association with **PKHD1** (ARPKD gene) — MSK-like imaging has been reported both in adult-onset ARPKD and in obligate heterozygous PKHD1 carriers, and a 2025 phenotyping study flagged possible PKHD1/ciliopathy overlap (though genetic data were incomplete) ([Kidney International Reports](https://www.kireports.org/article/S2468-0249(21)01560-6/fulltext); [J Nephrol 2025, PMID:40973923](https://pmc.ncbi.nlm.nih.gov/articles/PMC12630228/)).
- 2025 whole-exome sequencing of 42 clinically diagnosed MSK patients found a **diverse set of genes related to kidney-stone disease and/or cystic kidney disease**, concluding MSK "may represent a macroscopic phenotype with polygenic origins rather than a distinct [monogenic] entity" ([PubMed 41790480](https://pubmed.ncbi.nlm.nih.gov/41790480/); [NDT abstract #170](https://academic.oup.com/ndt/article/40/Supplement_3/gfaf116.0155/8294692)).

**Environmental / demographic:**
- Female sex (women more frequently affected; incidence of calcium stones reaching 20–30% in women with MSK vs. 15–20% overall) ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK470220/)).
- Age 20–40 (typical age at diagnosis; mean ~27 years) ([Dovepress](https://www.dovepress.com/medullary-sponge-kidney-current-perspectives-peer-reviewed-fulltext-article-IJNRD)).
- High-sodium diet noted as a stone-risk-amplifying factor in MSK patients ([Dovepress](https://www.dovepress.com/medullary-sponge-kidney-current-perspectives-peer-reviewed-fulltext-article-IJNRD)).
- Family history of nephrolithiasis.

### Protective Factors

No genetic protective variants have been specifically described. Environmentally, **high fluid intake, low-sodium diet, and avoidance of excess dietary protein** are associated with reduced stone risk in MSK patients, and **potassium citrate supplementation** substantially reduces stone recurrence (see Section 12) ([StatPearls; Dovepress](https://www.dovepress.com/medullary-sponge-kidney-current-perspectives-peer-reviewed-fulltext-article-IJNRD)).

### Gene–Environment Interactions

The dominant model is that a developmental/genetic predisposition (GDNF–RET–HNF1B axis dysfunction) creates the anatomic substrate (dilated collecting ducts) for **urinary stasis**, and that this anatomic substrate then interacts with acquired metabolic derangements — dRTA-driven hypercalciuria/hypocitraturia — to precipitate stone and Randall's-plaque formation. Biopsy studies show ductal stones form largely via simple crystallization/stasis in dilated inner medullary collecting ducts (IMCD) rather than via an osteogenic (bone-forming) interstitial process, despite positive Runx2/Osterix staining in interstitial cells ([Evan et al. 2015, Anat Rec, PMID:25615853](https://pmc.ncbi.nlm.nih.gov/articles/PMC4405475/)).

---

## 3. Phenotypes

Most MSK patients (roughly half to two-thirds in various series) are **asymptomatic**, with the diagnosis made incidentally on imaging performed for unrelated reasons or during stone workup ([GARD](https://rarediseases.info.nih.gov/diseases/232/medullary-sponge-kidney)).

### Symptomatic Phenotypes

| Phenotype | Frequency / Notes | Suggested HPO term |
|---|---|---|
| Nephrolithiasis (recurrent calcium oxalate/phosphate stones) | Found in ~70% of MSK patients overall; ductal stones roughly equal parts CaOx monohydrate and hydroxyapatite | HP:0000787 (Nephrolithiasis) |
| Nephrocalcinosis | Common; medullary distribution | HP:0000121 (Nephrocalcinosis) |
| Gross/microscopic hematuria | Common presenting sign, from stone passage or duct plug erosion | HP:0000790 (Hematuria) |
| Recurrent urinary tract infection | Secondary to stasis/stones | HP:0000010 (Recurrent urinary tract infections) |
| Distal (type 1) renal tubular acidosis, often incomplete | Present in 30–40% (incomplete form) of patients | HP:0008341 (Impaired renal tubular resorption of bicarbonate) / HP:0012625 (Renal tubular acidosis) |
| Hypercalciuria | Predominantly "renal leak" type; most frequent metabolic abnormality (8/12 in one biopsy series) | HP:0002150 (Hypercalciuria) |
| Hypocitraturia | Frequent (60% in one prospective cohort) | HP:0012622 (Hypocitraturia; use as available in dynamic enum) |
| Chronic flank/loin pain | Ranges from mild to a severe, disabling chronic-pain phenotype in a subgroup | HP:0012531 (Pain) |
| Failure to thrive / short stature (pediatric dRTA presentation) | Neonatal/pediatric MSK with dRTA | HP:0001508 / HP:0004322 |
| Polyuria, polydipsia | From concentrating defect | HP:0000103 / HP:0001959 |
| Urinary concentrating defect | Underlies polyuria | HP:0004735 (Nephrogenic diabetes insipidus-like) |
| Secondary hyperparathyroidism / osteopenia | From chronic hypercalciuria-driven negative calcium balance | HP:0000870 / HP:0000939 |
| Hypokalemia, hypokalemic periodic paralysis (rare) | Secondary to dRTA | HP:0002900 |
| Chronic kidney disease (late) | ~10% lifetime risk | HP:0012622/HP:0012623 (CKD stages) |

### Phenotype Characteristics

- **Age of onset:** Congenital anatomic lesion, but clinical presentation is typically delayed to the **second–third decade** (mean age at diagnosis ~27 years); neonatal/pediatric presentation with dRTA and failure to thrive is described but rarer and more severe ([PMC2726488](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2726488/); [Dovepress](https://www.dovepress.com/medullary-sponge-kidney-current-perspectives-peer-reviewed-fulltext-article-IJNRD)).
- **Severity:** Highly variable — from radiographically incidental/asymptomatic to a severe chronic-pain phenotype independent of active stone passage in a distinct subgroup ("MSK-chronic pain," MSK-CP).
- **Progression:** Generally stable/non-progressive at the renal-function level, punctuated by episodic stone events and UTIs; a minority progress to CKD.
- **Frequency among affected individuals:** Nephrolithiasis ~70%; incomplete dRTA ~30–40%; bilateral kidney involvement ~70% of cases (i.e., 30% unilateral) ([GARD](https://rarediseases.info.nih.gov/diseases/232/medullary-sponge-kidney); [Dovepress](https://www.dovepress.com/medullary-sponge-kidney-current-perspectives-peer-reviewed-fulltext-article-IJNRD)).

### Quality of Life Impact

A dedicated chronic-pain MSK cohort study found:
- **71% of participants reported daily pain** that strongly interfered with everyday life and quality of life (mean Wisconsin Quality of Life Questionnaire score 29.4).
- **69% used daily pain medication (70% opioids).**
- Pain was attributed to stone passage in most cases, but **15% reported pain with no apparent cause**.
- Chronic-pain patients produce substantially more renal calculi than typical MSK patients (**3.1 stones/patient/year**) and require frequent hospitalization ([J Nephrol 2018, PMID:29468561](https://link.springer.com/article/10.1007/s40620-018-0480-8); follow-up work on renal denervation and spinal cord stimulation as salvage therapies, [PMID:37929332](https://pubmed.ncbi.nlm.nih.gov/37929332/), [PMID:41460036](https://pubmed.ncbi.nlm.nih.gov/41460036/)).

---

## 4. Genetic/Molecular Information

### Causal / Candidate Genes

MSK has moved from a "sporadic, cause-unknown" disorder to one with an emerging **oligogenic/polygenic genetic architecture** in a meaningful subset of patients:

| Gene (HGNC symbol) | Role | Evidence |
|---|---|---|
| **GDNF** | Ligand for RET; drives ureteric-bud outgrowth and branching | Rare heterozygous variants found in ~12% of an Italian 57-patient MSK cohort, clustering in a PAX2-binding regulatory domain ([CJASN, PMID from CJASN full text](https://cjasn.asnjournals.org/content/5/7/1205.full)) |
| **RET** | Receptor tyrosine kinase for GDNF; ureteric bud branching | G691S/S904S polymorphism reported with MSK + hyperparathyroidism ([PMC6036688](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6036688/)); RET mutations found in ~20% of renal agenesis cases generally, supporting pathway relevance |
| **HNF1B** | Transcription factor, renal cysts and diabetes syndrome (RCAD) | 6 novel pathogenic variants (3 frameshift, 2 missense, 1 nonsense) identified in a 42-patient exome cohort ([JASN 2024 abstract](https://journals.lww.com/jasn/fulltext/2024/10001/genotyping_patients_with_medullary_sponge_kidney.1752.aspx)) |
| **PKHD1** | ARPKD gene (fibrocystin) | MSK-like phenotype reported in adult-onset ARPKD and in heterozygous PKHD1 carriers; flagged as a candidate overlap gene in a 2025 phenotyping cohort ([Kidney International Reports](https://www.kireports.org/article/S2468-0249(21)01560-6/fulltext); [J Nephrol 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12630228/)) |
| **SLC4A1** | Distal RTA (AE1 anion exchanger) | Heterozygous missense variant identified in an MSK/dRTA genetics-first case series ([Nephron 2024, 148(8):569](https://karger.com/nef/article/148/8/569/896648/Medullary-Sponge-Kidney-and-Its-Relationship-with)) |
| CLCN5, ATP6V0A4, ATP6V1B1, LAMA2, ACAN, ABCC8 | Assorted developmental/tubular genes | Proposed as candidate independent diagnostic indicators from a targeted-gene expression/retrospective correlation study of 17 MSK patients ([Li et al. 2022, PMC9674422](https://pmc.ncbi.nlm.nih.gov/articles/PMC9674422/)) — lower-confidence, hypothesis-generating |

**2025/2026 whole-exome sequencing (42 patients, Jan 2023–Jun 2024):** identified pathogenic/candidate variants across a **diverse set of genes associated with kidney-stone disease and/or cystic kidney disease**, concluding that "MSK may represent a macroscopic phenotype with polygenic origins rather than a distinct entity" — i.e., genetic heterogeneity converging on a common radiographic/pathologic endpoint ([PubMed 41790480](https://pubmed.ncbi.nlm.nih.gov/41790480/)).

### Variant Classification / Pathogenic Variants

- No single "founder" pathogenic variant is established; reported variants span **missense, frameshift, and nonsense** classes (HNF1B cohort: 3 frameshift, 2 missense, 1 nonsense).
- GDNF variants described are novel, heterozygous, non-synonymous changes in a regulatory (PAX2-binding) region rather than the canonical coding/catalytic domain.
- Formal ACMG/AMP pathogenicity classification (ClinVar-level detail) is not well established for MSK-specific variants in the literature surveyed; most reports are case-series/cohort level rather than curated clinical-variant databases.

### Allele Frequency / Population Data

Population-database allele-frequency data (gnomAD, 1000 Genomes) specific to MSK-associated GDNF/RET/HNF1B variants were not identified in the searched literature; this is an area of research immaturity consistent with the disease's rarity and recent genetic characterization.

### Somatic vs. Germline

All described variants are **germline**; there is no described somatic/mosaic contribution to MSK pathogenesis in the literature reviewed.

### Functional Consequences

- **GDNF/RET axis:** Loss-of-function-type disruption is implicated by analogy to mouse knockout data — GDNF-null mice show absent renal development/complete renal agenesis; GDNF heterozygous mice show small kidneys, cortical cysts, and unilateral dysgenesis (nephron under-endowment) ([Kidney International, GDNF+/- mice](https://www.kidney-international.org/article/S0085-2538(15)47816-0/fulltext); [Dovepress](https://www.dovepress.com/medullary-sponge-kidney-current-perspectives-peer-reviewed-fulltext-article-IJNRD)).
- **HNF1B:** Established developmental transcription factor for renal tubulogenesis; loss-of-function variants plausibly impair distal nephron segment patterning, consistent with a renal cystic dysplasia spectrum.

### Modifier Genes

No formal modifier-gene studies were identified; phenotypic variability (asymptomatic vs. severe stone-forming vs. chronic-pain phenotype) likely reflects a combination of the underlying developmental variant(s), acquired metabolic factors (citrate/calcium handling), and environmental exposures (diet, hydration) rather than a discrete modifier locus.

### Epigenetic Information

No MSK-specific epigenetic (DNA methylation, histone modification) studies were identified in the literature searched — an open gap.

### Chromosomal Abnormalities

No recurrent aneuploidy, translocation, or copy-number variant has been specifically linked to isolated MSK; MSK's association with **Beckwith–Wiedemann syndrome** (commonly caused by 11p15.5 imprinting/methylation defects, paternal UPD, or CDKN1C mutations — not itself detailed in the search results but well established in BWS literature) is a recognized syndromic overlap (see Section 5/9).

---

## 5. Environmental Information

### Environmental / Occupational Factors

No specific toxin, radiation, or occupational exposure has been established as causal for MSK; the disease is primarily viewed as developmental/genetic in origin. High-sodium diet is described as amplifying stone risk once the anatomic substrate (dilated ducts) is present, rather than as a primary cause ([Dovepress](https://www.dovepress.com/medullary-sponge-kidney-current-perspectives-peer-reviewed-fulltext-article-IJNRD)).

### Lifestyle Factors

- **Low fluid intake** predisposes to urinary stasis and stone formation in the anatomically predisposed collecting-duct system.
- **High-protein diet** is specifically flagged as a factor to avoid in MSK patients with hypercalciuria, given its acid-load and calciuric effects ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK470220/)).
- **High-sodium diet** increases urinary calcium excretion and stone risk.

### Infectious Agents

MSK is not caused by an infectious agent, but the anatomic lesion (stasis in dilated ducts) predisposes to **recurrent bacterial urinary tract infection and pyelonephritis** as a secondary/consequential process rather than an etiologic one ([StatPearls; Dovepress](https://www.dovepress.com/medullary-sponge-kidney-current-perspectives-peer-reviewed-fulltext-article-IJNRD)).

---

## 6. Mechanism / Pathophysiology

### Ordered Causal Chain

1. **Developmental trigger (inferred, genetically heterogeneous):** A germline variant disrupting GDNF–RET signaling (or, in a separate subset, HNF1B, PKHD1, or another renal-developmental/ciliopathy gene) impairs normal ureteric bud branching and/or terminal differentiation of the distal nephron during nephrogenesis → **leads to** failure of proper growth/maturation of the pre-calyceal (medullary and papillary) collecting ducts. *(Inferred from mouse knockout phenotypes and human variant association studies; not directly demonstrated in human embryonic tissue.)*
2. Abnormal ureteric-bud/metanephric-mesenchyme interaction → **results in** cystic dilatation of the inner medullary collecting ducts (IMCD), with multilayered hyperplastic epithelium in non-dilated segments and single-layered epithelium plus **primitive, embryonic-fibroblast-like interstitial cells** in dilated segments ([Evan et al. 2015, PMID:25615853](https://pmc.ncbi.nlm.nih.gov/articles/PMC4405475/)).
3. Dilated, ectatic ducts → **cause** chronic urinary stasis within the medullary/papillary collecting system.
4. Stasis, combined with a distal tubular acidification/concentrating defect (incomplete dRTA in a substantial minority) → **leads to** persistently alkaline urine, defective ammonium and titratable-acid excretion, and impaired urinary concentrating ability.
5. dRTA and the tubular milieu → **result in** hypercalciuria (predominantly renal-leak type), hypocitraturia, and elevated urinary pH — the classic MSK "lithogenic triad."
6. Hypercalciuria + hypocitraturia + alkaline urine, within the stasis-prone IMCD lumen → **precipitate** intraductal crystallization of calcium oxalate monohydrate and calcium phosphate (hydroxyapatite), forming free-floating **ductal stones** ("rolling out like marbles" on surgical exposure) rather than stones fixed to Randall's plaque in most cases ([Evan et al. 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4405475/)).
7. Ductal stones pass into the renal pelvis, where they may **serve as nidi** for further papillary/pelvic stone growth → **causes** recurrent symptomatic nephrolithiasis, hematuria, and obstructive episodes.
8. Recurrent stone passage and urinary stasis → **predispose to** recurrent urinary tract infection and, less commonly, pyelonephritis.
9. Chronic hypercalciuria → negative calcium balance → **triggers** compensatory (secondary) hyperparathyroidism and contributes to osteopenia/osteoporosis; a distinct **primary**-hyperparathyroidism association via RET-pathway crosstalk has also been proposed but the mechanism is unresolved ([PMC6036688](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6036688/)).
10. In a minority of patients, cumulative stone events, obstruction, and recurrent infection → **lead to** chronic kidney disease/renal insufficiency (~10% lifetime risk); most patients do not progress to ESRD.
11. **Separately and not fully explained:** a subset of patients develop a **chronic visceral pain syndrome (MSK-CP)** that correlates with stone burden but sometimes occurs without an identifiable stone or obstructive event (~15% of chronic-pain patients), suggesting a component of **renal sensory/neurogenic dysregulation** that is not accounted for by the stone-stasis chain alone — an active area of investigation (renal denervation, spinal cord stimulation trials) ([PMID:37929332](https://pubmed.ncbi.nlm.nih.gov/37929332/); [PMID:41460036](https://pubmed.ncbi.nlm.nih.gov/41460036/)).
12. A 2025 functional-imaging study additionally found **impaired renal medullary oxygenation** (higher cortex:medulla BOLD-MRI R2* ratio, 0.60 vs. 0.55 in controls, p=0.04) in MSK patients, correlating with potassium citrate dose — suggesting a chronic hypoxic/microvascular component to the medullary lesion that may contribute to, or result from, the structural/functional abnormality, and which is measurably reduced kidney function (mGFR 78 vs. 90 mL/min/1.73m², p=0.008) beyond what eGFR alone captures ([J Nephrol 2025, PMID:40973923](https://pmc.ncbi.nlm.nih.gov/articles/PMC12630228/)).

### Molecular Pathways

- **GDNF–RET receptor tyrosine kinase signaling** (ureteric bud branching morphogenesis) — the best-characterized pathway; modeled computationally as a **Turing-type reaction-diffusion mechanism**, with WNT11 providing pattern-modulating feedback ([PMID:30651543](https://pubmed.ncbi.nlm.nih.gov/30651543/)).
- **HNF1B transcriptional network** governing distal nephron segment identity.
- Sphingomyelin metabolism pathway — implicated by a 2021 omics study identifying **ENPP6** (ectonucleotide pyrophosphatase/phosphodiesterase 6) and **SPP1/osteopontin** as the most significantly dysregulated urinary (and, for ENPP6, plasma) proteins in MSK vs. idiopathic calcium stone formers, pointing to a "pivotal biological role of sphingomyelin" in MSK pathophysiology ([PMID:34124100 / PMC8187918](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8187918/)).

Suggested GO Biological Process terms: **GO:0001658** (branching involved in ureteric bud morphogenesis), **GO:0072205** (metanephric collecting duct development), **GO:0055074** (calcium ion homeostasis), **GO:0035725** (sodium ion transmembrane transport, for dRTA-related handling).

### Cellular Processes

- Cyst-lining epithelial hyperplasia in non-dilated ducts vs. epithelial simplification (single layer) in massively dilated segments.
- Expansion/proliferation of **primitive interstitial cells** resembling embryonic fibroblasts, at abnormally high density around dilated IMCD.
- Intraductal biomineralization (crystallization), not classic epithelial-driven osteogenesis — a key distinguishing finding from Randall's-plaque biology in idiopathic calcium stone formers ([Evan et al. 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4405475/)).

### Protein Dysfunction

- GDNF/RET: putative loss- or altered-function variants impairing ligand–receptor signaling for branching morphogenesis.
- Runx2 and Osterix (bone-lineage transcription factors) are **expressed** (positive immunostaining) in MSK interstitial cells at a subset of biopsy sites, but this expression did **not** correlate significantly with actual mineral deposition (mineral present at only 1 of 34 bone-gene-expression-positive sites, χ²=31, p<0.001) — arguing against a primary osteogenic-differentiation mechanism for stone formation in MSK, in contrast to some hypotheses for idiopathic calcium stone disease ([Evan et al. 2015, PMID:25615853](https://pmc.ncbi.nlm.nih.gov/articles/PMC4405475/)).

### Metabolic Changes

- Hypercalciuria (renal-leak type predominating).
- Hypocitraturia — the most frequent metabolic abnormality in a 2025 prospective cohort (60% of patients; urine citrate 1.96 vs. 3.68 mmol/24h in controls, p=0.01) ([PMC12630228](https://pmc.ncbi.nlm.nih.gov/articles/PMC12630228/)).
- Hyperoxaluria in a subset (3/12 in the Evan biopsy series).
- Sphingomyelin-pathway metabolomic signature distinguishing MSK from idiopathic calcium stone formers ([PMC8187918](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8187918/)).

### Immune System Involvement

No primary autoimmune or immunodeficiency mechanism is described; recurrent UTI is a secondary consequence of urinary stasis rather than a primary immune defect.

### Tissue Damage Mechanisms

Chronic medullary hypoxia (elevated cortex:medulla R2* ratio on BOLD-MRI) and recurrent obstructive/infectious insult from stone events are the principal tissue-injury mechanisms; overt fibrosis was **not** detected by T1 mapping or diffusion-weighted MRI in a 2025 pilot cohort, suggesting the functional GFR deficit precedes or occurs independent of gross fibrotic remodeling ([PMC12630228](https://pmc.ncbi.nlm.nih.gov/articles/PMC12630228/)).

### Biochemical Abnormalities

- Defective distal tubular acid secretion (incomplete dRTA): elevated urine pH, elevated urinary ammonia/titratable acidity handling defects, normal-to-elevated urinary potassium/bicarbonate handling abnormalities.
- Impaired urinary concentrating ability (medullary architecture disruption).

### Epigenetic Changes

Not characterized in MSK-specific studies to date (gap).

### Molecular Profiling

- **Proteomics:** Urinary extracellular vesicle proteomics identified a **specific kinase protein profile** proposed as a novel biomarker signature for MSK ([PMID:35685307](https://pubmed.ncbi.nlm.nih.gov/35685307/)); broader review of the Italian collaborative network's proteomics findings in ([Kidney Blood Press Res, PMID:36265463](https://karger.com/kbr/article/47/12/683/824519/Proteomics-Insights-into-Medullary-Sponge-Kidney)).
- **Metabolomics:** Plasma LC-ESI-MS/MS metabolomic profiling (15 MSK vs. 15 idiopathic calcium-stone controls) identified a distinct sphingomyelin-centered signature ([PMC8187918](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8187918/)).
- **Single-cell/targeted gene expression:** A 17-patient retrospective correlation of CT features with expression of *HNF1B, CLCN5, GDNF, ATP6V0A4, ATP6V1B1, LAMA2, RET, ACAN, ABCC8* proposed these as candidate diagnostic/preventive indicators (hypothesis-generating; single small cohort) ([PMC9674422](https://pmc.ncbi.nlm.nih.gov/articles/PMC9674422/)).

### Advanced Technologies

- **Functional MRI (BOLD, T1 mapping, DWI):** 2025 prospective pilot study (20 MSK vs. 13 controls) is the first to apply multiparametric functional renal MRI to MSK, demonstrating impaired medullary oxygenation and measured-GFR deficits not captured by eGFR ([PMC12630228](https://pmc.ncbi.nlm.nih.gov/articles/PMC12630228/); companion [ClinicalTrials.gov NCT05682053](https://clinicaltrials.gov/study/NCT05682053)).
- **Whole-exome sequencing:** Two independent 2024–2026 cohorts (42 patients each, overlapping or parallel efforts) establishing genetic heterogeneity ([JASN 2024](https://journals.lww.com/jasn/fulltext/2024/10001/genotyping_patients_with_medullary_sponge_kidney.1752.aspx); [PubMed 41790480](https://pubmed.ncbi.nlm.nih.gov/41790480/)).
- No CRISPR/RNAi functional-genomics screens specific to MSK were identified.

---

## 7. Anatomical Structures Affected

### Organ Level

- **Primary organ:** Kidney, specifically the **renal medulla and papillae** (inner medullary collecting ducts); renal cortex is typically spared/normal.
- **Secondary involvement:** Urinary bladder and lower urinary tract are secondarily affected via stone passage and recurrent infection; skeletal system secondarily affected via osteopenia/osteoporosis from chronic hypercalciuria and secondary hyperparathyroidism.
- **Body systems involved:** Genitourinary (primary); endocrine (secondary hyperparathyroidism); skeletal (bone demineralization); rarely reproductive (testicular dysgenesis syndrome reported in one case series, [PMC3971849](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3971849/)).

Suggested UBERON terms: **UBERON:0000362** (renal medulla), **UBERON:0001225** (renal papilla), **UBERON:0004134** (renal collecting duct).

### Tissue and Cell Level

- **Epithelium:** Collecting-duct principal-cell epithelium — multilayered/hyperplastic in non-dilated ducts, single-layered/attenuated in dilated (cystic) ducts.
- **Interstitium:** Expanded population of primitive, embryonic-fibroblast-like interstitial cells.
- Suggested Cell Ontology terms: **CL:1001432** (kidney collecting duct principal cell), **CL:0002520** (kidney interstitial fibroblast, as nearest available term).

### Subcellular Level

Not extensively characterized at the organelle level in the literature surveyed; biomineralization occurs at the luminal/extracellular level within the collecting-duct lumen rather than being primarily described as an intracellular organelle process. Relevant GO Cellular Component term: **GO:0005576** (extracellular region, for the biomineralized matrix).

### Localization

- **Bilateral in ~70% of cases**, unilateral in ~30% ([GARD](https://rarediseases.info.nih.gov/diseases/232/medullary-sponge-kidney)).
- Distribution within the kidney is typically diffuse across the medullary pyramids, though severity can be patchy/segmental (mild "papillary blush" vs. severe "bouquet of flowers" pattern on imaging, see Section 10).

---

## 8. Temporal Development

### Onset

- **Underlying anatomic lesion is congenital/developmental** (present from nephrogenesis), but **clinical onset is typically delayed** until the second–third decade of life when metabolic/stone complications manifest (mean age at diagnosis ~27 years).
- **Neonatal/pediatric onset** occurs when dRTA is clinically significant early, presenting with failure to thrive, feeding problems, vomiting, polyuria/polydipsia, and dehydration episodes ([PMC2726488](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2726488/)).
- Onset pattern is generally **insidious** rather than acute, except for acute presentations related to obstructing stones or UTI.

### Progression

- Disease course is **generally stable** at the structural/renal-function level over years, punctuated by **episodic** stone and infection events.
- A minority (up to ~10%) show **slow progression** to CKD/renal insufficiency.
- The chronic-pain subgroup (MSK-CP) shows a distinct, often **relapsing-remitting or persistent** pain trajectory that is only partially linked to discrete stone events.
- No formal staging system (analogous to CKD or cancer staging) exists specifically for MSK; severity is generally graded radiographically (mild "papillary blush" → "linear striations/paint brush" → severe "papillary bouquets") and clinically by stone-event frequency.

### Patterns

- **Remission:** Stone episodes can remit spontaneously between events; potassium citrate/thiazide therapy substantially reduces recurrence (stone rate from 0.58 to 0.10 stones/year/patient with potassium citrate) ([PMID:20576821](https://pubmed.ncbi.nlm.nih.gov/20576821/)).
- **Critical periods:** Early identification and initiation of alkali/citrate therapy in childhood-onset dRTA is important to prevent growth failure, nephrocalcinosis progression, and bone demineralization.

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence estimates vary widely** depending on ascertainment method: commonly cited as **~1/5,000** in the general population, with a broader literature range of **5/10,000 to 5/100,000** ([GARD](https://rarediseases.info.nih.gov/diseases/232/medullary-sponge-kidney); [Dovepress](https://www.dovepress.com/medullary-sponge-kidney-current-perspectives-peer-reviewed-fulltext-article-IJNRD)).
- Among patients presenting with **nephrolithiasis**, prevalence is much higher: up to **20%** of stone formers show at least mild radiographic MSK features, with one study reporting **12% frequency in nephrolithiasis patients vs. 1% in non-stone-formers**.
- This ascertainment bias (diagnosed mainly through stone/imaging workups) means true population prevalence is likely underestimated, and the disease is widely considered **under-recognized**, especially as IVU (the most sensitive imaging modality) has been supplanted by CT in routine practice, reducing detection rates ([Dovepress](https://www.dovepress.com/medullary-sponge-kidney-current-perspectives-peer-reviewed-fulltext-article-IJNRD)).

### Inheritance Pattern

- MSK is **predominantly sporadic**.
- A **minority of cases are familial**, with an **autosomal dominant** pattern showing **reduced penetrance and variable expressivity** ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0085253815557426); GARD).
- With the 2024–2026 exome-sequencing work, the genetic architecture is now understood as **heterogeneous/polygenic** in a meaningful fraction of patients rather than following a single clean Mendelian pattern — different patients carry variants in different genes (GDNF, RET, HNF1B, and cystic-kidney/stone-disease genes), converging on a shared radiographic/clinical phenotype.
- Suggested HPO mode-of-inheritance term: **HP:0000006** (Autosomal dominant inheritance) with a note on incomplete penetrance (**HP:0003829**); genetic counseling literature discusses a **~50% recurrence risk to offspring** when a pathogenic familial variant is identified ([WebSearch synthesis](https://karger.com/nef/article/148/8/569/896648/Medullary-Sponge-Kidney-and-Its-Relationship-with)).

### Penetrance / Expressivity

- **Reduced penetrance** is explicitly described in familial MSK.
- **Variable expressivity** is well documented — ranging from asymptomatic radiographic findings in relatives to overt stone disease.

### Genetic Anticipation, Germline Mosaicism, Founder Effects, Consanguinity, Carrier Frequency

No specific data on genetic anticipation, germline mosaicism, founder-population effects, consanguinity-driven recessive contribution, or carrier frequency for MSK were identified in the literature searched (a gap — consistent with the disease's recent and still-incomplete genetic characterization).

### Population Demographics

- **Sex ratio:** Women more frequently affected than men; calcium-stone incidence 20–30% in affected women vs. 15–20% overall.
- **Age distribution:** Most commonly diagnosed ages 20–40 (mean ~27); pediatric cases are less common but recognized, particularly with dRTA.
- No specific ethnic/geographic prevalence disparities were identified in the search results, though most large cohort studies derive from **Italian** research networks (reflecting a strong historical/ongoing Italian MSK research tradition going back to the original Cacchi–Ricci description), with additional recent cohorts from **France** (Lyon) and **China**.

---

## 10. Diagnostics

### Clinical/Laboratory Tests

- Urinalysis: hematuria, alkaline pH.
- 24-hour urine chemistry: calcium, citrate, oxalate, uric acid, sodium, creatinine (to characterize the lithogenic risk profile — hypercalciuria, hypocitraturia, hyperoxaluria).
- Serum electrolytes/acid-base panel: to identify incomplete or overt dRTA (hyperchloremic metabolic acidosis pattern), hypokalemia.
- Serum PTH, calcium, vitamin D: to evaluate for 2° or coincident 1° hyperparathyroidism.

### Biomarkers

- Emerging: urinary extracellular vesicle kinase protein profile ([PMID:35685307](https://pubmed.ncbi.nlm.nih.gov/35685307/)); plasma/urinary sphingomyelin-pathway metabolomic and proteomic signature (ENPP6, SPP1/osteopontin) ([PMC8187918](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8187918/)) — proposed as potential future non-invasive diagnostic alternatives to radiologic testing, though not yet clinically validated/adopted.

### Imaging Studies

- **Intravenous urography (IVU)** remains historically the **gold-standard/most sensitive** imaging modality: shows contrast pooling in dilated papillary ducts producing the classic **"paint brush" / "bouquet of flowers" / papillary blush** appearance ([Radiopaedia](https://radiopaedia.org/articles/bouquet-of-flowers-appearance-medullary-sponge-kidney?lang=us); [PMC4588331](https://pmc.ncbi.nlm.nih.gov/articles/PMC4588331/); [Abdominal Radiology, PMID from Springer](https://link.springer.com/article/10.1007/s00261-017-1420-0)).
- **CT urography (CTU) with delayed/excretory phase and MIP reconstructions** can reproduce IVU-like coronal images and is diagnostic in most previously IVU-positive cases (9/10 in one comparative study), though with **slightly lower sensitivity than IVU** and no false positives reported ([American Journal of Nephrology, PMID from Karger](https://karger.com/ajn/article/39/2/165/326012/CT-Urography-for-the-Diagnosis-of-Medullary-Sponge); [PMID:29692693](https://pubmed.ncbi.nlm.nih.gov/29692693/)); routine (non-delayed) CT has **limited diagnostic accuracy** and has contributed to under-diagnosis as IVU use has declined.
- **Ultrasonography:** Shows echogenic/hyperechoic medullary pyramids, hypoechoic medullary areas with hyperechoic spots, microcystic dilatation of the papillary zone, and multiple calcifications — useful adjunct, particularly given accessibility, but less specific than IVU/CTU ([PMC7552549](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7552549/)).
- **Multiparametric functional MRI (BOLD, T1 mapping, DWI):** emerging research tool (2025 pilot study; active [ClinicalTrials.gov NCT05682053](https://clinicaltrials.gov/study/NCT05682053)) demonstrating impaired medullary oxygenation and structural cysts, not yet a standard diagnostic test.
- **Endoscopy (ureteroscopy):** Can directly visualize diffuse papillary abnormality — contour rounding, "billowy" appearance, blunting of distal papillae — and can establish the diagnosis when imaging is equivocal.

### Genetic Testing

- Not yet standard of care, but **whole-exome sequencing** is increasingly used in a research/genetics-first context, particularly for familial cases, early-onset/pediatric cases with dRTA, or cases with atypical/syndromic features, given the identification of GDNF, RET, HNF1B, PKHD1, and SLC4A1 variants in recent cohorts.
- No commercial MSK-specific gene panel was identified in the search results; testing in practice likely proceeds via broader cystic-kidney-disease or nephrolithiasis gene panels, or exome sequencing.

### Clinical Criteria / Differential Diagnosis

MSK must be distinguished from other causes of **medullary nephrocalcinosis**, principally:
- Primary hyperparathyroidism
- Distal (type 1) renal tubular acidosis (primary, without MSK)
- Hypervitaminosis D
- Milk-alkali syndrome
- Sarcoidosis
- Autosomal recessive polycystic kidney disease (ARPKD)/PKHD1-related disease, particularly atypical adult-onset presentations, which can radiographically mimic MSK ([PMC9039475](https://pmc.ncbi.nlm.nih.gov/articles/PMC9039475/); [Kidney International Reports](https://www.kireports.org/article/S2468-0249(21)01560-6/fulltext))
- Autosomal dominant polycystic kidney disease (macrocysts, cortical involvement, family history pattern differ)

Distinguishing imaging feature: MSK shows **patent, rounded, enlarged, "puffy" papillae** with ductal ectasia, rather than the diffuse cortical/corticomedullary macrocysts of ADPKD or the more uniformly enlarged, hyperechoic kidneys with hepatic fibrosis of ARPKD.

### Screening

- **Wilms tumor / abdominal tumor surveillance** is recommended in children diagnosed with MSK, particularly those with congenital hemihypertrophy or Beckwith–Wiedemann features, given the increased embryonal-tumor risk in this overlapping group ([WebSearch synthesis; PMC5308029](https://pmc.ncbi.nlm.nih.gov/articles/PMC5308029/); [AJR survey](https://doi.org/10.2214/ajr.116.4.773)); children with MSK and gross hematuria specifically warrant Wilms tumor evaluation.
- No formal population-based newborn or carrier screening program exists for MSK.

---

## 11. Outcome/Prognosis

### Survival and Mortality

MSK carries **no specific mortality data** distinct from its complications; disease-specific mortality is not separately tracked, and overall MSK is regarded as a benign condition with respect to survival.

### Morbidity and Function

- Overall, **long-term prognosis is excellent** with appropriate management of metabolic/stone complications, and progression to significant renal impairment is **unusual** — but **up to ~10% of patients develop renal insufficiency/failure** over their lifetime, generally attributable to recurrent UTI, obstruction, and stone burden rather than an intrinsic progressive nephropathy ([Dovepress](https://www.dovepress.com/medullary-sponge-kidney-current-perspectives-peer-reviewed-fulltext-article-IJNRD); consistent NKF patient-facing statement).
- A 2025 functional-MRI study found a **measurable mGFR deficit** (78 vs. 90 mL/min/1.73m², p=0.008) and **20% prevalence of CKD stage 3a** even in a relatively contained cohort, with eGFR **overestimating** true kidney function by ~11 mL/min/1.73m² — suggesting renal functional impairment in MSK may be more prevalent than previously appreciated when measured directly rather than estimated ([PMC12630228](https://pmc.ncbi.nlm.nih.gov/articles/PMC12630228/)).
- **Quality of life** is substantially impacted in the chronic-pain subgroup (71% report daily QoL-impairing pain; see Section 3).

### Disease Course / Complications

- Nephrolithiasis (70%), nephrocalcinosis, recurrent UTI/pyelonephritis, dRTA-related metabolic derangement, osteopenia/osteoporosis from chronic hypercalciuria, and — in a subset — chronic pain syndrome.
- **Unilateral nephrectomy** (for severe unilateral disease) reduces stone-related events on the treated side but does **not** significantly reduce overall ESRD incidence, attributable to the typically **bilateral** nature of the underlying malformation ([Dovepress](https://www.dovepress.com/medullary-sponge-kidney-current-perspectives-peer-reviewed-fulltext-article-IJNRD)).

### Prognostic Factors

- Presence of stone risk factors (hypercalciuria, hypocitraturia, hyperuricosuria, hyperoxaluria) is the **key modifiable prognostic determinant** — patients with these factors warrant prophylactic potassium citrate; those without tend to have a more benign stone-free course.
- Chronic-pain phenotype correlates with **higher stone event rate** (3.1 stones/patient/year) and predicts a more morbid course requiring multidisciplinary pain management.

---

## 12. Treatment

Treatment is **targeted at complications** (stone prevention, dRTA correction, infection management, pain control) rather than at a disease-modifying cure, since MSK is a structural malformation.

### Pharmacotherapy

| Treatment | Mechanism / Use | Suggested NCIT term |
|---|---|---|
| **Potassium citrate** (starting ~20 mEq/day, titrated to a urinary citrate target ~450 mg/day and urine pH 7.0–7.2, avoiding overalkalinization which risks calcium-phosphate stones) | Corrects hypocitraturia, alkalinizes urine to counter dRTA, reduces stone recurrence (from 0.58 to 0.10 stones/yr/patient in a long-term study, [PMID:20576821](https://pubmed.ncbi.nlm.nih.gov/20576821/)); also mitigates bone loss | NCIT:C15986 (Pharmacotherapy) |
| **Thiazide diuretics** (e.g., hydrochlorothiazide 25 mg PO daily) | Reduces urinary calcium excretion (enhanced distal tubular calcium reabsorption), preventing calcium stone recurrence | NCIT:C15986 (Pharmacotherapy) |
| High fluid intake (target urine output >2 L/day) | Reduces urinary stasis and supersaturation | NCIT:C15447 (Dietary Intervention) |
| Dietary sodium restriction, avoidance of high-protein diet | Reduces calciuria | NCIT:C15447 (Dietary Intervention) |

### Advanced Therapeutics

No gene therapy, cell therapy, RNA-based therapy, targeted molecular therapy, or immunotherapy is described or in development for MSK — consistent with its nature as a structural/anatomic malformation rather than a targetable single-pathway molecular disease at the population level (though pathway-specific genetic subsets, e.g., HNF1B-related, may eventually inform more precise counseling).

### Surgical and Interventional

- **Endourologic stone management** (ureteroscopy, shock-wave lithotripsy/ESWL) for symptomatic calculi — "the impact of modern endourological techniques" is specifically reviewed in the literature ([PMC4034299](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4034299/)).
- **Urothelial/papillary vaporization** in selected cases with cystic dilation contributing to recurrent stone nucleation.
- **Nephrectomy** (unilateral) as a last resort for severe, refractory unilateral disease — reduces local stone events but does not reduce ESRD risk given typical bilaterality.

### Supportive and Rehabilitative

- Management of recurrent UTIs with antibiotics as needed (no specific prophylactic regimen uniquely validated for MSK identified in the search results).
- Multidisciplinary chronic pain management for the MSK-CP subgroup, including emerging **spinal cord stimulation** ([PMID:37929332](https://pubmed.ncbi.nlm.nih.gov/37929332/)) and **renal denervation** ([PMID:41460036](https://pubmed.ncbi.nlm.nih.gov/41460036/)) as salvage options when conventional stone-prevention and analgesic strategies fail — both approaches are still early/limited-evidence (case reports/small series) as of this report.

### Experimental / Clinical Trials

- **NCT05682053** — Multiparametric MRI in Medullary Sponge Kidney (functional imaging characterization) ([ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT05682053)).
- **NCT06418230** — Exome Sequencing in Medullary Sponge Kidney (genetic characterization) ([ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT06418230)).

### Treatment Outcomes

- Potassium citrate: robust, well-documented reduction in stone event rate with long-term use; also implicated in reducing bone-density loss.
- No systematic adverse-event/FAERS-level data specific to MSK pharmacotherapy were identified beyond the known class effects of thiazides (hypokalemia, hyperuricemia) and citrate (risk of calcium-phosphate stone formation if overalkalinized).

### Treatment Strategy

- **Risk-stratified approach:** Patients with ≥1 lithogenic risk factor (hypercalciuria, hypocitraturia, hyperuricosuria, hyperoxaluria) are treated prophylactically with citrate ± thiazide; those without risk factors are managed more conservatively (hydration, monitoring).
- No formal combination-therapy trials or genotype-guided personalized-medicine protocols specific to MSK were identified.

---

## 13. Prevention

### Prevention Levels

- **Primary prevention:** Not applicable in the traditional sense, as MSK is a congenital/developmental malformation; no described modifiable primary-prevention strategy prevents the anatomic lesion itself.
- **Secondary prevention:** Early diagnosis (imaging, metabolic stone-risk workup) and initiation of citrate/thiazide therapy to prevent progression from asymptomatic anatomic lesion to symptomatic stone disease/CKD.
- **Tertiary prevention:** Aggressive management of recurrent stones/UTIs to prevent obstruction, chronic infection, and progression to renal insufficiency; osteoporosis screening/bone-protective measures given chronic hypercalciuria risk.

### Screening and Early Detection

- **Genetic screening/counseling** is recommended for individuals with a positive family history, including preconception counseling; when a familial pathogenic variant is identified, a **50% recurrence risk to offspring** is quoted in patient-counseling contexts (consistent with autosomal dominant transmission in the familial subset) ([Nephron 2024](https://karger.com/nef/article/148/8/569/896648/Medullary-Sponge-Kidney-and-Its-Relationship-with)).
- No population-based or newborn screening program exists.
- **Wilms tumor/abdominal-mass surveillance** in children with MSK, particularly those with hemihypertrophy or Beckwith–Wiedemann features, functions as targeted secondary screening for a specific high-risk subgroup.

### Behavioral Interventions

High fluid intake, low sodium, moderate protein intake, and avoidance of dehydration are the primary behavioral/lifestyle prevention measures for stone recurrence.

### Counseling

Genetic counseling is advised when there is a positive family history or an identified pathogenic variant, covering recurrence risk, reproductive options, and cascade screening/testing of at-risk relatives.

### Prophylaxis

Potassium citrate and thiazide diuretics function as ongoing pharmacologic prophylaxis against stone recurrence in at-risk patients (see Section 12).

---

## 14. Other Species / Natural Disease

The literature searched did **not identify a well-characterized, naturally occurring MSK phenotype in non-human species** (companion animals or wildlife) analogous to, for example, documented veterinary polycystic kidney disease in cats. This is likely due to (a) MSK's relatively subtle papillary/medullary phenotype being harder to ascertain incidentally in veterinary imaging compared to cortical macrocystic disease, and (b) the limited comparative-pathology literature specifically targeting MSK. This represents a **gap** rather than an established negative finding — no OMIA (Online Mendelian Inheritance in Animals) entry or veterinary case series was surfaced in the searches performed. GDNF/RET pathway orthologs are broadly conserved across mammals (as evidenced by the mouse knockout literature used to model human MSK biology — see Section 15), but this reflects **model-organism** use rather than documented **natural** disease in another species.

---

## 15. Model Organisms

### Genetic Mouse Models (GDNF–RET Pathway)

The principal model-organism evidence for MSK pathogenesis comes from mouse genetics of the GDNF–RET axis, used to infer mechanism rather than to directly recapitulate the clinical MSK phenotype:

- **GDNF-null (Gdnf−/−) mice:** Complete absence of renal development / renal agenesis, demonstrating GDNF's essential role in ureteric bud induction ([Dovepress synthesis](https://www.dovepress.com/medullary-sponge-kidney-current-perspectives-peer-reviewed-fulltext-article-IJNRD)).
- **GDNF heterozygous (Gdnf+/−) mice:** Reduced nephron endowment; small kidneys, cortical cysts, and unilateral dysgenesis reported ([Kidney International, PMID via kidney-international.org](https://www.kidney-international.org/article/S0085-2538(15)47816-0/fulltext)) — the closest available murine analog to a "partial" GDNF-deficiency phenotype, though it emphasizes cortical rather than purely medullary/papillary pathology.
- **Gdnf−/−;Spry1−/− and Ret−/−;Spry1−/− double mutants:** Develop **large kidneys** with normal ureters, highly branched collecting ducts, extensive nephrogenesis, and normal histoarchitecture — demonstrating that removing the negative regulator Spry1 rescues/overcorrects branching in the absence of GDNF/RET signaling, and that **FGF10 signaling can substitute for GDNF/RET** in driving kidney development in this genetic background ([PMC2797609](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2797609/)).
- **RET mutant mice/computational branching models:** RET mutations are associated with failure of ureteric bud outgrowth and renal agenesis/aplasia in mouse models, and RET variants are found in ~20% of human renal agenesis cases, supporting cross-species relevance of the pathway ([Dovepress](https://www.dovepress.com/medullary-sponge-kidney-current-perspectives-peer-reviewed-fulltext-article-IJNRD)).
- **Computational/image-based modeling of branching morphogenesis:** A GDNF-RET-based **Turing-type reaction-diffusion mechanism**, with WNT11 pattern-modulating feedback, quantitatively recapitulates ureteric-bud branching patterns in wild-type and mutant cultured explants — a computational model system complementing the genetic mouse data ([PMID:30651543](https://pubmed.ncbi.nlm.nih.gov/30651543/)).

### Model Characteristics and Limitations

- **Phenotype recapitulation:** These mouse models recapitulate the **developmental pathway defect** (branching morphogenesis failure/dysregulation) implicated in MSK pathogenesis, but **none directly reproduces the specific adult clinical MSK phenotype** (discrete medullary/papillary cystic dilatation with preserved cortex, dRTA, and recurrent calcium stone disease). Most GDNF/RET pathway mouse mutants instead show more severe, global phenotypes (renal agenesis, dysgenesis, or — in double-mutant rescue models — diffusely hyperbranched kidneys), reflecting the pathway's broader role in nephrogenesis beyond the distal/medullary segment specifically implicated in human MSK.
- **Model limitations:** No described murine, zebrafish, or in vitro (organoid) model isolates the milder, adult-onset, medulla-restricted phenotype seen in most human MSK patients; the field currently relies on **human patient cohorts** (exome sequencing, functional MRI, biopsy) rather than validated animal models for MSK-specific mechanistic study — a clear gap consistent with the disease's newly emerging genetic characterization.

### Research Applications

Mouse GDNF/RET models remain the primary tool for studying the **developmental** side of MSK pathogenesis (ureteric bud branching regulation); human biopsy tissue (Evan et al. 2015) and prospective clinical cohorts (functional MRI, exome sequencing, proteomics/metabolomics) are the primary tools for studying the **metabolic/lithogenic** and **structural/functional** sides of the disease in its clinically relevant, adult-onset form.

### Resources

Standard model-organism databases (MGI for the Gdnf/Ret/Spry1 alleles referenced above) would be the entry point for further model-organism detail; no MSK-specific entries were identified in IMPC, ZFIN, or other model-organism-specific databases in this search.

---

## Summary of Key Gaps for Knowledge-Base Curation

1. **Genetic architecture is actively being revised** (2024–2026 exome cohorts) — treat MSK as **genetically heterogeneous/polygenic**, not attributable to a single gene; curate GDNF, RET, HNF1B, PKHD1, and SLC4A1 as **candidate/subset-associated** genes rather than a unifying monogenic cause, each with modest supporting cohort sizes.
2. **No validated animal model** reproduces the adult, medulla-restricted MSK phenotype — GDNF/RET mouse models illustrate pathway biology but not the specific clinical entity.
3. **Prevalence estimates vary ~20-fold** across sources (1/5,000 to 1/100,000+) due to ascertainment bias toward stone-forming populations and the declining use of the most sensitive diagnostic modality (IVU).
4. **Chronic-pain phenotype (MSK-CP)** is a clinically important, only partially stone/obstruction-linked subgroup with a distinct and still poorly understood mechanism — worth modeling as a discrete phenotype/mechanistic node if curated.
5. **Renal functional impairment may be underestimated by eGFR** in MSK based on a 2025 measured-GFR/functional-MRI study — relevant to how "renal insufficiency" outcome data are interpreted from older literature using eGFR alone.

### Sources

- [GARD — Medullary sponge kidney](https://rarediseases.info.nih.gov/diseases/232/medullary-sponge-kidney)
- [StatPearls — Medullary Sponge Kidney (NBK470220)](https://www.ncbi.nlm.nih.gov/books/NBK470220/)
- [Medscape — Medullary Sponge Kidney](https://emedicine.medscape.com/article/242886-overview)
- [Dovepress — Medullary Sponge Kidney: Current Perspectives (IJNRD 2019)](https://www.dovepress.com/medullary-sponge-kidney-current-perspectives-peer-reviewed-fulltext-article-IJNRD)
- [PMC8187918 — Sphingomyelin and Medullary Sponge Kidney Disease (Omics)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8187918/)
- [CJASN — Identification of GDNF Gene Sequence Variations in MSK](https://cjasn.asnjournals.org/content/5/7/1205.full)
- [PMC6036688 — MSK and hyperparathyroidism with RET G691S/S904S polymorphism](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6036688/)
- [ScienceDirect — Evidence for inheritance of medullary sponge kidney](https://www.sciencedirect.com/science/article/pii/S0085253815557426)
- [Karger Nephron — MSK and primary distal RTA, genetics-first approach (2024)](https://karger.com/nef/article/148/8/569/896648/Medullary-Sponge-Kidney-and-Its-Relationship-with)
- [JASN 2024 — Genotyping Patients with Medullary Sponge Kidney](https://journals.lww.com/jasn/fulltext/2024/10001/genotyping_patients_with_medullary_sponge_kidney.1752.aspx)
- [PubMed 41790480 — Exome sequencing in patients with medullary sponge kidney](https://pubmed.ncbi.nlm.nih.gov/41790480/)
- [PMC12630228 / J Nephrol 2025 — MSK in-depth phenotyping (PMID:40973923)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12630228/)
- [PMC4405475 — Biopsy Proven Medullary Sponge Kidney (Evan et al., Anat Rec 2015, PMID:25615853)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4405475/)
- [PMC9674422 — Single-Cell Gene Expression Analysis in Patients with MSK (Li et al. 2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9674422/)
- [Kidney International Reports — Atypical ARPKD mimicking MSK](https://www.kireports.org/article/S2468-0249(21)01560-6/fulltext)
- [PMC2797609 — Kidney Development in the Absence of Gdnf and Spry1 Requires Fgf10](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2797609/)
- [Kidney International — GDNF heterozygous mouse nephron endowment](https://www.kidney-international.org/article/S0085-2538(15)47816-0/fulltext)
- [PubMed 30651543 — Image-based modeling of GDNF-RET Turing mechanism](https://pubmed.ncbi.nlm.nih.gov/30651543/)
- [Radiopaedia — Bouquet of flowers appearance](https://radiopaedia.org/articles/bouquet-of-flowers-appearance-medullary-sponge-kidney?lang=us)
- [PMC4588331 — Bouquet of flowers: Clue to medullary sponge kidneys](https://pmc.ncbi.nlm.nih.gov/articles/PMC4588331/)
- [American Journal of Nephrology — CT Urography for Diagnosis of MSK](https://karger.com/ajn/article/39/2/165/326012/CT-Urography-for-the-Diagnosis-of-Medullary-Sponge)
- [PubMed 20576821 — Long-term potassium citrate treatment and renal stones in MSK](https://pubmed.ncbi.nlm.nih.gov/20576821/)
- [PubMed 31266277 — Potassium citrate therapy and natural course of MSK nephrolithiasis](https://pubmed.ncbi.nlm.nih.gov/31266277/)
- [PMC4034299 — Modern endourological techniques in MSK-associated nephrolithiasis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4034299/)
- [Journal of Nephrology — Chronic pain in medullary sponge kidney (PMID:29468561)](https://link.springer.com/article/10.1007/s40620-018-0480-8)
- [PubMed 37929332 — Spinal cord stimulation for visceral pain in MSK](https://pubmed.ncbi.nlm.nih.gov/37929332/)
- [PubMed 41460036 — MSK and chronic pain: role of renal denervation](https://pubmed.ncbi.nlm.nih.gov/41460036/)
- [PMC5308029 — Beckwith–Wiedemann syndrome and recurrent bilateral renal calculi](https://pmc.ncbi.nlm.nih.gov/articles/PMC5308029/)
- [AJR — MSK associated with congenital hemihypertrophy](https://doi.org/10.2214/ajr.116.4.773)
- [ICD10Data.com — Q61.5 Medullary cystic kidney](https://www.icd10data.com/ICD10CM/Codes/Q00-QA0/Q60-Q64/Q61-/Q61.5)
- [Wikipedia — Medullary sponge kidney / Cacchi-Ricci disease](https://en.wikipedia.org/wiki/Medullary_sponge_kidney)
- [ClinicalTrials.gov NCT05682053 — Multiparametric MRI in MSK](https://clinicaltrials.gov/study/NCT05682053)
- [ClinicalTrials.gov NCT06418230 — Exome Sequencing in MSK](https://clinicaltrials.gov/study/NCT06418230)
- [PMC9039475 — Atypical ARPKD mimicking MSK](https://pmc.ncbi.nlm.nih.gov/articles/PMC9039475/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 29 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 11 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0015268` (1 mention) - the report calls it "MONDO"; MONDO calls it **medullary sponge kidney**
- `HP:0012622` (2 mentions) - the report calls it "Hypocitraturia; use as available in dynamic enum"; HP calls it **Chronic kidney disease**
- `HP:0002900` (1 mention) - the report calls it "Secondary to dRTA"; HP calls it **Hypokalemia**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0004735` (1 mention), reported as "Nephrogenic diabetes insipidus-like" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000787` (1 mention) - the report calls it "Nephrolithiasis"; HP calls it **Kidney stone**, and lists "Nephrolithiasis" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.