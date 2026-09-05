---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-09-01T00:02:58.339090'
end_time: '2026-09-01T00:17:27.810154'
duration_seconds: 869.47
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 88
  mondo_id: ''
  category: Mendelian
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
  - claude-opus-5[1m]
  web_search_requests: 6
  num_turns: 65
  total_cost_usd: 5.881967000000001
  session_id: 279c45be-0e70-4621-8617-1b324d1b80f7
  stop_reason: end_turn
  permission_denials: 7
  denied_tools:
  - Bash
  assistant_text_blocks: 1
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 24
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 22
  on_topic: 13
  validator_version: 0.2.1
term_validation:
  total_terms: 107
  verified: 97
  not_found: 0
  obsolete: 0
  unverifiable: 10
  confabulation_rate: 0.0
  labels_checked: 36
  labels_matching: 19
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: UBERON:0002439
    reported_labels:
    - Axillary lymph node
    ontology_label: myenteric nerve plexus
  - term_id: UBERON:0003950
    reported_labels:
    - Abdominal/mesenteric lymph nodes
    ontology_label: inner ear canal
  labels_variant: 15
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  - LOINC
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 88
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 88** covering all of the
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

# Immunodeficiency 88 (IMD88) — Comprehensive Disease Research Report

**Prepared:** 2026-09-01 · **Target:** Immunodeficiency 88 / T-bet (TBX21) deficiency · **MONDO:0030483** · **Category:** Mendelian

> **Critical framing caveat for the whole report.** As of this writing, IMD88 rests on **a single reported patient**, from one consanguineous Moroccan kindred, described in one index paper ([PMID:33296702](https://pubmed.ncbi.nlm.nih.gov/33296702/), Yang et al., *Cell*, 23 Dec 2020) and three follow-up studies of the *same* individual ([PMID:35909394](https://pubmed.ncbi.nlm.nih.gov/35909394/), [PMID:35867801](https://pubmed.ncbi.nlm.nih.gov/35867801/), [PMID:36630059](https://pubmed.ncbi.nlm.nih.gov/36630059/)). Every "frequency," "penetrance," "prognosis," and "natural history" statement below is therefore n = 1 unless it is explicitly borrowed from the broader MSMD literature or from mouse models. I flag n = 1 claims throughout. Do not curate them as population frequencies.

---

## 1. Disease Information

### Overview

Immunodeficiency-88 is an **autosomal recessive inborn error of immunity** caused by biallelic loss-of-function variants in *TBX21*, encoding the T-box transcription factor **T-bet**. It is one of the genetic etiologies of **Mendelian susceptibility to mycobacterial disease (MSMD)** — the group of monogenic disorders that selectively predispose otherwise healthy individuals to disease from weakly virulent mycobacteria (BCG vaccine substrains, environmental mycobacteria) and, more variably, to *M. tuberculosis* and non-typhoidal *Salmonella*.

What distinguishes IMD88 mechanistically from the rest of MSMD is **where** in the IFN-γ circuit the lesion sits. Most MSMD genes break IFN-γ *signalling* (IFNGR1/2, STAT1, JAK1) or the IL-12/IL-23→IFN-γ *induction* axis (IL12B, IL12RB1, IL12RB2, IL23R, TYK2). T-bet deficiency instead breaks the **developmental program of the IFN-γ-producing innate and innate-like lymphocyte compartment itself** — NK, iNKT, MAIT, and Vδ2⁺ γδ T cells fail to develop, and the residual cells underproduce IFN-γ. Purely adaptive CD8⁺ αβ T cells and non-classic CD4⁺ TH1\* cells retain normal mycobacterium-specific IFN-γ production and **do not compensate**.

A second, mechanistically separable phenotype accompanies the immunodeficiency: because T-bet normally *represses* the Th2 program, its loss produces **Th2 cytokine excess (IL-4/IL-5/IL-9/IL-13), blood eosinophilia, and chronic upper airway inflammation/asthma** — the human counterpart of the spontaneous asthma-like phenotype of *Tbx21*⁻/⁻ mice.

### Key identifiers

| Resource | Identifier |
|---|---|
| **OMIM** | **619630** (IMMUNODEFICIENCY 88; IMD88) |
| **MONDO** | **MONDO:0030483** — *immunodeficiency 88* |
| **MedGen / UMLS** | MedGen UID 1794236 · UMLS **C5562026** |
| **Orphanet** | No dedicated ORPHA code for TBX21 deficiency. Parent concept: **ORPHA:748** *Mendelian susceptibility to mycobacterial diseases* |
| **Gene (OMIM)** | *TBX21* **\*604895** |
| **HGNC** | **HGNC:11599** (`hgnc:11599`) — *T-box transcription factor 21*; 17q21.32 |
| **NCBI Gene / Ensembl / UniProt** | 30009 / ENSG00000073861 / **Q9UL17** |
| **ICD-10** | No specific code. Closest: **D84.8/D84.9** (other/unspecified immunodeficiency); BCG complication **T88.1 / Y58.0**; disseminated atypical mycobacterial infection **A31.8** |
| **ICD-11** | **4A00.Y / 4A01.Y** (other specified immunodeficiency) — no dedicated stem code |
| **MeSH** | No dedicated descriptor. Related: *Mycobacterium Infections* (D009164), *T-Box Domain Proteins* (D050956), *Immunologic Deficiency Syndromes* (D007153) |
| **IUIS classification** | Table 6, "Defects in intrinsic and innate immunity" → MSMD subgroup ([PMID:35748970](https://pubmed.ncbi.nlm.nih.gov/35748970/), Tangye et al., *J Clin Immunol* 2022) |

### Synonyms

- IMD88
- **T-bet deficiency** / human T-bet deficiency
- **TBX21 deficiency**
- Autosomal recessive complete T-bet deficiency
- Mendelian susceptibility to mycobacterial disease due to TBX21 deficiency
- Immunodeficiency 88, mycobacteriosis, autosomal recessive (MedGen synonym)

### Provenance of the evidence

**Aggregated disease-level resources (OMIM, MONDO, MedGen, HPO) all trace to a single primary case report.** The HPO annotation set for OMIM:619630 is sourced entirely from PMID:33296702 and consists of five terms, all with frequency 1/1. There is **no registry, no EHR-derived cohort, and no natural-history study** for IMD88. Population-level statements must be borrowed from MSMD as a whole.

---

## 2. Etiology

### 2a. Disease causal factors

**Primary cause: monogenic, germline, autosomal recessive.** Homozygous loss-of-function variation in *TBX21*.

The index (and only) patient carries the homozygous indel:

- **cDNA:** `NM_013351.2:c.466_471delGAGATGinsAGTTTA`
- **Protein:** `p.Glu156_Met157delinsSerLeu` (E156→S, M157→L)
- **Consequence:** in-frame two-residue substitution within/adjacent to the T-box DNA-binding domain (UniProt Q9UL17, T-box domain residues 141–326)

> "The rare indel variant c.466_471delGAGATGinsAGTTTA of *TBX21* is MSMD-causing." — derived from [PMID:33296702](https://pubmed.ncbi.nlm.nih.gov/33296702/)

UniProt Q9UL17 annotates the IMD88 variant's functional effect as **"loss of binding to DNA; loss of transcriptional activity."** OMIM 619630 adds that *in vitro* expression in HEK293T cells showed the mutation "impaired protein production and nuclear translocation, as well as interfered with the ability of TBX21 to bind to target DNA." Notably, *TBX21* **mRNA levels are normal** in the patient's cells while endogenous T-bet protein is low — implying a **post-transcriptional/protein-destabilization** component layered on top of the DNA-binding defect. This is a **triple hit** on one allele product: reduced protein, impaired nuclear entry, and abolished DNA binding.

**Required environmental co-factor: mycobacterial exposure.** IMD88 is not a spontaneously symptomatic disorder. The immunodeficiency is only revealed by encounter with a mycobacterium — in this case, **live attenuated BCG vaccine given at 3 months of age** under Morocco's mandatory national immunization schedule. This is the archetypal gene–environment interaction of MSMD: the genotype is necessary but the live vaccine (or environmental mycobacterium) is the precipitant.

### 2b. Risk factors

**Genetic**
- **Biallelic *TBX21* LoF** — causal, not merely a risk factor. n = 1 variant known; no allelic series exists.
- **Consanguinity** — the index patient's parents were **first cousins** (PMID:33296702). In the Moroccan MSMD series, 64% of 22 patients were born to consanguineous parents ([PMID:36630059](https://pubmed.ncbi.nlm.nih.gov/36630059/)); in the broader Moroccan innate/intrinsic immunity cohort, 51.1% ([PMID:41209815](https://pubmed.ncbi.nlm.nih.gov/41209815/), *Pathog Immun*, Nov 2025).
- **Ancestry/founder effects** — none demonstrated. The single variant is private; there is no evidence of a founder haplotype.
- **Modifier loci** — none identified. With n = 1 there is no basis for a modifier claim.

**Environmental / exposure**
- **BCG vaccination** — the dominant precipitant in BCG-vaccinating countries. Errami et al. state plainly: *"BCG vaccination is contraindicated in MSMD patients and should be delayed in newborn siblings until the exclusion of a genetic predisposition to mycobacteria."* ([PMID:36630059](https://pubmed.ncbi.nlm.nih.gov/36630059/))
- **Environmental (non-tuberculous) mycobacteria** — the dominant precipitant in non-BCG-vaccinating countries ([PMID:38535546](https://pubmed.ncbi.nlm.nih.gov/38535546/), *Pathogens* 2024).
- **Tuberculosis endemicity** — Morocco is TB-endemic; Errami et al. name the combination of *"the mandatory use of the BCG vaccine, the endemicity of tuberculosis (TB), and the high rate of consanguinity"* as the triggering context for MSMD in that population.
- **Age** — infantile onset; the vaccine is given in the first months of life, so exposure timing sets onset timing.
- **Sex** — no evidence of sex effect (autosomal recessive; n = 1, male).
- Suggested **ECTO/exposure concepts**: BCG vaccination is a clinical intervention rather than an environmental toxicant; ECTO has no clean term. Consider modelling as `environmental` with `environmental_effect: TRIGGERS` and a free-text `preferred_term` ("BCG vaccination"), leaving `term:` unbound with a `notes:` line recording the ECTO search — per the repo's *no term beats a bad one* rule.

### 2c. Protective factors

- **Heterozygous carriage is asymptomatic.** The patient's mother is heterozygous and healthy; his wild-type brother is healthy (PMID:35867801, Methods). Consistent with fully recessive inheritance.
- **Avoidance of live mycobacterial vaccines** is the single most effective protective intervention (see §13).
- **No protective genetic modifier has been identified.** gnomAD-level protective allele analysis is not informative at n = 1.

### 2d. Gene–environment interaction

The causal architecture is cleanly two-factor:

> **biallelic *TBX21* LoF** (necessary, non-sufficient) **× live/weakly virulent mycobacterial exposure** (necessary, non-sufficient) **→ disseminated mycobacterial disease**

A second, **exposure-independent** branch also exists: the Th2/eosinophilic airway phenotype developed and *persisted* independently of the mycobacterial episode and independently of documented allergen sensitization, mirroring the mouse phenotype in which *"T-bet deficiency, in the absence of allergen exposure, induces a murine phenotype reminiscent of both acute and chronic human asthma"* ([PMID:11786643](https://pubmed.ncbi.nlm.nih.gov/11786643/), Finotto et al., *Science* 2002).

---

## 3. Phenotypes

All frequencies below are **1/1 (single patient)** unless attributed to the wider MSMD literature. HPO annotations for OMIM:619630 (source: PMID:33296702) comprise exactly five terms.

### 3a. Curated HPO annotation set (authoritative, from HPO/ontology.jax.org)

| HP ID | Label | Frequency | Onset |
|---|---|---|---|
| **HP:0020087** | BCGosis | 1/1 | HP:0003593 (Infantile onset) |
| **HP:0002099** | Asthma | 1/1 | — |
| **HP:0001880** | Increased total eosinophil count | 1/1 | — |
| **HP:0003593** | Infantile onset | 1/1 | — |
| **HP:0000007** | Autosomal recessive inheritance | — | — |

### 3b. Clinical signs and infectious manifestations

| Phenotype | Type | Onset | Severity | Course | Freq. | Suggested HP term |
|---|---|---|---|---|---|---|
| **Disseminated BCG disease (BCG-osis)** | Clinical sign / infection | 3–6 months (post-vaccination) | Severe, life-threatening | Acute→subacute; resolved on therapy | 1/1 | **HP:0020087** BCGosis |
| Fever | Symptom | 3 months | Moderate | Persistent until treated | 1/1 | HP:0001945 Fever |
| **Left axillary lymphadenopathy** (ipsilateral to injection) | Clinical sign | 3 months | Moderate | Regressed with therapy | 1/1 | HP:0002733 Generalized lymphadenopathy / HP:0002716 Lymphadenopathy |
| Cutaneous eruption | Clinical sign | 3 months | Mild | Transient | 1/1 | HP:0011123 Inflammatory abnormality of the skin |
| **Hepatosplenomegaly** | Clinical sign | 6 months | Moderate–severe | Regressed | 1/1 | **HP:0001433** Hepatosplenomegaly |
| Abdominal (mesenteric/deep) adenopathy | Imaging sign | 6 months | Moderate | Regressed | 1/1 | HP:0002244 Abdominal lymphadenopathy |
| **Failure to thrive / weight loss** | Clinical sign | 6 months | Moderate | Reversed with treatment | 1/1 | HP:0001824 Weight loss / HP:0001508 Failure to thrive |
| Recurrent mycobacterial infection | Infection susceptibility | — | — | *Absent* in this patient after therapy | 0/1 | HP:0011274 Recurrent mycobacterial infections |
| Other clinical infections | — | — | — | **Notably absent** despite serologically documented exposure to multiple viruses and bacteria | 0/1 | — |

> OMIM 619630: *"The single patient described did not develop other clinical infectious diseases, although serology documented exposure to various viruses and bacteria."*

This selectivity is the diagnostic signature of MSMD and is a **positive discriminating feature** — it separates IMD88 from combined immunodeficiencies.

### 3c. Allergic / type-2 inflammatory manifestations

| Phenotype | Type | Onset | Severity | Course | Freq. | Suggested HP term |
|---|---|---|---|---|---|---|
| **Asthma / reactive airway disease** | Clinical sign | Early childhood | Moderate | **Persistent/chronic** | 1/1 | **HP:0002099** Asthma |
| **Chronic upper airway inflammation** | Clinical sign | Early childhood | Moderate | Persistent | 1/1 | HP:0002257 Chronic rhinitis (`clinical_course: CHRONIC`) |
| **Blood eosinophilia** | Laboratory | Early childhood | Moderate | Persistent | 1/1 | **HP:0001880** Increased total eosinophil count |
| **Elevated plasma IL-5** | Laboratory | Childhood | Marked | Persistent | 1/1 | (no HP term; curate as `biochemical` with a `BiomarkerReadout`) |
| **Elevated plasma IL-13** | Laboratory | Childhood | Marked | Persistent | 1/1 | (no HP term; `biochemical`) |

> Verbatim, from [PMID:35909394](https://pubmed.ncbi.nlm.nih.gov/35909394/) (Benhsaien et al., *Qatar Med J* 2022): *"T-bet deficiency thus underlies the excessive production of Th2 cytokines, particularly IL-5 and IL-13, by CD4+ αβ T cells, causing blood eosinophilia and UAI."*

Critically, the same paper draws the **two-branch dissociation** explicitly: *"The MSMD of this patient results from defective IFN-γ production by innate and innate-like adaptive lymphocytes, whereas the UAI and eosinophilia result from excessive Th2 cytokine production by adaptive CD4+ αβ T lymphocytes."* These are two mechanistically distinct arms of one lesion and should be curated as **two separate causal chains from the same root node**.

### 3d. Laboratory / immunophenotypic abnormalities

| Abnormality | Direction | Freq. | Suggested HP term |
|---|---|---|---|
| **Reduced circulating NK cells** | ↓↓ | 1/1 | **HP:0040218** Reduced total natural killer cell count |
| **Reduced iNKT cells** | ↓↓ | 1/1 | (no precise HP term) |
| **Reduced MAIT cells** | ↓↓ | 1/1 | (no precise HP term) |
| **Reduced Vδ2⁺ γδ T cells** | ↓↓ | 1/1 | (no precise HP term) |
| **Reduced classic TH1 lymphocytes** | ↓↓ | 1/1 | HP:0031132 Decreased proportion of CD4-positive T cells (approximate — flag as imprecise) |
| **Impaired IFN-γ production (most subsets)** | ↓ | 1/1 | HP:0032154 Decreased circulating interferon-gamma level (approximate) |
| Normal IFN-γ from CD8⁺ αβ T and CD4⁺ TH1\* to mycobacterial antigen | = | 1/1 | — |
| **Increased circulating IgE** | ↑ | 1/1 | **HP:0003212** Increased circulating IgE concentration |
| **Increased IgG1** (and modest IgG4) | ↑ | 1/1 | HP:0032297 Increased circulating IgG1 concentration |
| **Decreased IgG2** | ↓ | 1/1 | **HP:0008348** Decreased circulating IgG2 concentration |
| Normal IgA, IgM | = | 1/1 | — |
| Normal vaccine-specific IgG (tetanus, diphtheria, Hib, pneumococcus) | = | 1/1 | — |
| **Absent CD21^lo CD11c^hi T-bet^hi B cells** | absent | 1/1 | (no HP term; curate as a `Cellular` phenotype) |
| Total, transitional, naïve and memory B-cell proportions normal | = | 1/1 | — |
| Somatic hypermutation, affinity maturation intact | = | 1/1 | — |

> From [PMID:35867801](https://pubmed.ncbi.nlm.nih.gov/35867801/) (Yang et al., *Sci Immunol* 2022): *"Thus, human T-bet is largely redundant for long-lived protective humoral immunity but is essential for the development of a distinct subset of human CD11c^hi CD21^lo B cells."*

### 3e. Quality-of-life impact

**No formal QoL instrument (EQ-5D, PROMIS, SF-36, PedsQL) has been applied to any IMD88 patient.** Inference only, and should be curated as such:

- The **acute BCG-osis episode** required hospitalization and 18 months of four-drug therapy — substantial short-term burden, then resolution.
- The **persistent asthma/upper-airway phenotype** is the ongoing QoL determinant, not the immunodeficiency. It is chronic and long-outlasted the infection.
- **BCG contraindication for siblings** and lifelong avoidance of live mycobacterial vaccines carry a family-level counselling burden.
- The patient *"has been in remission and free of mycobacterial infection for several years"* (PMID:35867801) — a favourable trajectory relative to MSMD as a class.

---

## 4. Genetic / Molecular Information

### 4a. Causal gene

**_TBX21_** (T-box transcription factor 21; T-bet; alias TBLYM), `hgnc:11599`, OMIM \*604895, chromosome **17q21.32**, NCBI Gene 30009, Ensembl ENSG00000073861, UniProt **Q9UL17** (535 aa).

**Normal function (UniProt Q9UL17):** a lineage-defining transcription factor that *"initiates Th1 lineage development from naive Th precursor cells both by activating Th1 genetic programs and by repressing the opposing Th2 and Th17 genetic programs."* It transactivates *IFNG* and *CXCR3*. Domain: **T-box DNA-binding domain, residues 141–326**. Subcellular localization: **nucleus** (GO:0005634).

### 4b. Pathogenic variant

| Field | Value |
|---|---|
| **cDNA** | c.466_471delGAGATGinsAGTTTA |
| **Protein** | p.Glu156_Met157delinsSerLeu (E156S, M157L) |
| **Variant class** | **In-frame indel (delins)** — 6 bp deleted, 6 bp inserted; no frameshift |
| **Zygosity** | Homozygous |
| **Origin** | **Germline**, inherited from consanguineous first-cousin parents |
| **Segregation** | Parents heterozygous; wild-type sibling unaffected |
| **Discovery method** | Whole-exome sequencing + linkage analysis, confirmed by Sanger sequencing |
| **Population frequency** | Private/ultra-rare; not observed at appreciable frequency in gnomAD, ESP, or 1000 Genomes. The variant is described as "rare" in the primary report |
| **Functional consequence** | **Complete loss of function** — abolished DNA binding, abolished transactivation, impaired nuclear translocation, plus reduced steady-state protein despite normal mRNA |
| **ACMG/AMP tier (inferred)** | Pathogenic. Supporting criteria: PS3 (well-established functional studies), PM2 (absent from controls), PP1 (co-segregation), PP4 (phenotype highly specific), PM4 (in-frame indel in a critical functional domain). **Note: no ClinVar submission was located for this variant — verify before asserting a ClinVar classification.** |

**Functional-consequence classification for the dismech schema:**
```yaml
genetic:
- name: TBX21
  gene_term: {preferred_term: TBX21, term: {id: hgnc:11599, label: TBX21}}
  genetic_context:
    functional_impact_category: LOSS_OF_FUNCTION   # variant-level claim
    allele_type: INDEL
    variant_origin: GERMLINE
    zygosity: HOMOZYGOUS
```
Do **not** put `LOSS_OF_FUNCTION` on the *pathway* descriptors as well unless you are making a separate activity-state claim — see the repo's GOF/LOF slot decision table. The downstream node "TH1 program transcriptional output" is best described with `modifier: LOSS_OF_FUNCTION` (qualitative: the program is not merely reduced, it is not initiated), while "IFN-γ production" is `modifier: DECREASED` (quantitative, PATO-bound `PATO:0002301`).

### 4c. Gene-level constraint and selection

*TBX21*, like other genes underlying autosomal recessive inborn errors of immunity, is **not under strong negative selection at the gene level**. The related analysis in [PMID:36326697](https://pubmed.ncbi.nlm.nih.gov/36326697/) (Ogishi et al., *J Exp Med* 2023) makes the general point for AR IEI genes: *"Like other genes with mutations underlying AR IEI, ITK is not under negative selection, as shown by CoNeS."* The same logic applies to *TBX21*: recessive, exposure-contingent phenotypes are poorly purged. **Verify the specific CoNeS/pLI values in gnomAD before curating a numeric constraint claim** — I did not retrieve gene-specific gnomAD constraint metrics for *TBX21*.

### 4d. Modifier genes

**None identified.** With one patient, modifier inference is impossible. The obvious candidate class — genes governing residual IFN-γ output (e.g. *EOMES*, which partially overlaps T-bet function in NK/CD8 cells; see [PMID:38740922](https://pubmed.ncbi.nlm.nih.gov/38740922/), *Cell Mol Immunol* 2024) — remains untested in human T-bet deficiency.

### 4e. Epigenetic information — this is unusually well characterized and mechanistically central

T-bet's disease mechanism in IMD88 is **substantially epigenetic**: it acts as a pioneer-like factor establishing chromatin accessibility at lineage-defining loci.

From [PMID:35867801](https://pubmed.ncbi.nlm.nih.gov/35867801/) (Omni-ATAC-seq on patient vs. control naïve B cells):

- Under CpG/αIg/IFN-γ stimulation, chromatin accessibility differed at **2,391 loci** between patient and healthy-donor B cells; under CpG/αIg/IL-27, at 139 loci, 50 overlapping.
- **89%** of the 2,478 loci normally remodelled by CpG/αIg/IFN-γ in healthy donors *"remained unaltered in CpG/αIg/IFN-γ-stimulated T-bet-deficient B cells."* The same 89% figure held for IL-27.
- **902 loci** were shared T-bet-dependent targets of both stimuli. DNA-binding motifs for **IRF1, JUNB, and RUNX1** were the most significantly enriched in these — suggesting *"T-bet provides permissive environment for binding of IRF1 to IFN-γ- and IL-27-dependent targets in human B cells."*
- Specific loci: chromatin **opened** in a T-bet-dependent manner at **FAS, IL21R, SEC61B, DUSP4, DAPP1, SOX5**, plus *IRF4* (3 loci) and *GFI1* (3 loci); **closed** at **CD79B, CXCR4**, plus *SEMA4B*, *CCR6*, *CD37*.
- **CCL3L1** (3 loci) and **CCL4L1** were in a closed configuration in T-bet deficiency even *unstimulated* — interpreted as leaving *"T-bet-deficient B cells... less poised to secrete chemokines required for T-cell recruitment."*
- The index paper (PMID:33296702) likewise reports CpG-island DNA methylation and chromatin analyses in the patient's cells (MeSH indexing includes *DNA Methylation/genetics*, *CpG Islands/genetics*, *Chromatin/metabolism*, *Epigenesis, Genetic*).
- T-bet also **autoregulates**: *"T-bet-deficient B cells had lower levels of T-bet than naïve B cells from most healthy donors... suggesting T-bet promotes its own expression."*

**Suggested GO terms:** GO:0045893 positive regulation of DNA-templated transcription; GO:0006338 chromatin remodeling; GO:0043565 sequence-specific DNA binding; GO:0000978 RNA polymerase II *cis*-regulatory region sequence-specific DNA binding.

### 4f. Chromosomal abnormalities

**None.** IMD88 is a single-nucleotide-scale indel disorder. No aneuploidy, translocation, CNV, or structural variant is implicated. Chromosomal microarray, karyotype, and FISH are **not indicated** for IMD88 diagnosis.

---

## 5. Environmental Information

### 5a. Environmental factors

The disorder has **no toxicological, radiological, or pollution-related component.** CTD/TOXNET/EPA searches are not applicable. The only relevant "environmental" exposures are microbiological and iatrogenic:

| Exposure | Effect | Evidence |
|---|---|---|
| **BCG vaccination (live attenuated *M. bovis* BCG)** | **TRIGGERS** disseminated mycobacterial disease | PMID:33296702 — patient vaccinated at 3 months, symptomatic within weeks |
| **Environmental (non-tuberculous) mycobacteria** | **TRIGGERS** (predicted; not observed in this patient) | PMID:38535546 — NTM predominates in non-BCG-vaccinating countries |
| ***M. tuberculosis*** exposure (TB-endemic Morocco) | **PREDISPOSES** to severe/multifocal TB | PMID:36630059; PMID:36326697 |
| Non-typhoidal *Salmonella* | **PREDISPOSES** (class-level MSMD risk; ~50% of MSMD patients) | PMID:36630059 — *"about half of them develop non-typhoidal salmonellosis of varying severity"* |
| Allergen exposure | **Not required** for the airway phenotype | PMID:11786643 — murine phenotype arises "in the absence of allergen exposure" |

### 5b. Lifestyle factors

**Not applicable.** Smoking, diet, alcohol, and exercise have no established role. The patient is a young child.

### 5c. Infectious agents

| Agent | NCBITaxon | Role |
|---|---|---|
| ***Mycobacterium bovis* BCG** (vaccine substrain) | **NCBITaxon:1765** (*M. bovis*) / NCBITaxon:33892 (BCG str. Pasteur) | **Causative** of the presenting BCG-osis |
| *Mycobacterium tuberculosis* | **NCBITaxon:1773** | Predicted heightened susceptibility (MSMD class) |
| Environmental/non-tuberculous mycobacteria | NCBITaxon:1763 (*Mycobacterium* genus) | Predicted susceptibility |
| Non-typhoidal *Salmonella enterica* | NCBITaxon:28901 | Predicted susceptibility (MSMD class, ~50%) |
| EBV, CMV, common viruses | — | **Serologically documented exposure without clinical disease** — an informative negative |

---

## 6. Mechanism / Pathophysiology

### 6a. Ordered causal chain

**Root lesion**

1. **Homozygous *TBX21* c.466_471delinsAGTTTA (p.E156_M157delinsSL)** → **leads to** a T-bet protein that is expressed at reduced steady-state levels (normal mRNA, low protein — post-transcriptional destabilization), translocates poorly to the nucleus, and cannot bind its T-box DNA motif.
2. Loss of T-box DNA binding → **results in** complete loss of T-bet transactivation function (`GO:0003700` DNA-binding transcription factor activity, `modifier: LOSS_OF_FUNCTION`).
3. Loss of T-bet transactivation → **results in** failure to establish the T-bet-dependent permissive chromatin landscape at lineage-defining loci — ~89% of the normal IFN-γ/IL-27-induced accessibility changes fail to occur, with loss of an IRF1/JUNB/RUNX1-motif-enriched enhancer program (`GO:0006338` chromatin remodeling). *Demonstrated by ATAC-seq in B cells (PMID:35867801); inferred by extension to other T-bet-dependent lineages.*

**Branch A — the immunodeficiency arm (innate/innate-like IFN-γ collapse)**

4. Failure of the T-bet chromatin/transcription program in lymphoid progenitors → **leads to** a block in **terminal maturation of NK cells** (`CL:0000623`), **invariant NKT cells** (`CL:0000921`), **MAIT cells** (`CL:0000940`), and **Vδ2⁺ γδ T cells** (`CL:0000798`). *Directly demonstrated in the human patient (PMID:33296702); mechanistically anchored by the mouse stem-cell-intrinsic maturation defect (PMID:15084276).*
5. In parallel, failure of the T-bet program in naïve CD4⁺ T cells → **results in** failure of **classic TH1 lineage commitment** (`CL:0000545` T-helper 1 cell; `GO:0045063` T-helper 1 cell differentiation, `modifier: LOSS_OF_FUNCTION`), so classic TH1 cells are numerically reduced.
6. Steps 4 and 5 together → **result in** *"extremely low counts of circulating Mycobacterium-reactive natural killer (NK), invariant NKT (iNKT), mucosal-associated invariant T (MAIT), and Vδ2+ γδ T lymphocytes, and of Mycobacterium-non reactive classic TH1 lymphocytes"* (PMID:33296702).
7. Independently, loss of direct T-bet transactivation of *IFNG* → **results in** the residual cells of those populations *"also producing abnormally small amounts of IFN-γ"* (`GO:0032609` interferon-gamma production, `modifier: DECREASED`). **This is a second, additive hit: the cells are both fewer and worse.**
8. Steps 6 + 7 → **result in** a profound deficit in early, antigen-independent IFN-γ available at the site of mycobacterial encounter.

   **Branch point / failed rescue.** 8a. **CD8⁺ αβ T cells and non-classic CD4⁺ αβ TH1\* cells produce IFN-γ normally in response to mycobacterial antigens** — but **do not compensate**. This is not an incidental observation; it is the paper's central claim, and it is *predicted by mouse genetics*: Szabo et al. showed T-bet *"is required for control of IFN-γ production in CD4 and NK cells, but not in CD8 cells"* ([PMID:11786644](https://pubmed.ncbi.nlm.nih.gov/11786644/), *Science* 2002). The human and mouse data converge exactly.

9. Insufficient early IFN-γ → **results in** failure of **macrophage** (`CL:0000235`) classical activation and killing of intracellular mycobacteria (`GO:0006952` defense response; `GO:0071346` cellular response to interferon-gamma, `modifier: DECREASED`).
10. Failure of macrophage mycobactericidal activity → **leads to** uncontrolled intracellular replication of BCG and dissemination beyond the vaccination site.
11. Dissemination → **results in** the clinical phenotype: fever, ipsilateral axillary lymphadenopathy, cutaneous eruption, then hepatosplenomegaly, abdominal adenopathy, and weight loss — i.e. **BCG-osis** (HP:0020087).

**Branch B — the type-2 immunopathology arm (de-repression)**

12. Loss of T-bet's **repressive** function on the Th2 program → **results in** failure to inhibit Th2 cytokine transcription. *Demonstrated by gain-of-function rescue*: unlike WT T-bet, *"the mutant form of T-bet from this patient did not inhibit the production of T helper 2 (Th2) cytokines, including IL-4, IL-5, IL-9, and IL-13, when overexpressed in Th2 cells"* (PMID:35909394).
13. De-repression → **leads to** CD4⁺ αβ T cells (`CL:0000624`) producing excess IL-4 (`CHEBI` n/a; protein), **IL-5**, IL-9, and **IL-13** *"in response to chronic stimulation, regardless of their antigen specificities"* — i.e. an **antigen-nonspecific, cell-intrinsic** skew (`GO:0042092` type 2 immune response, `modifier: INCREASED`).
14. Excess IL-5 → **results in** eosinophil (`CL:0000771`) expansion → **blood eosinophilia** (HP:0001880).
15. Excess IL-13 (plus IL-4/IL-9) → **results in** airway type-2 inflammation → **chronic upper airway inflammation and asthma/reactive airway disease** (HP:0002099).
16. **Rescue confirms causality:** the Th2-skewed phenotype was *"reversed by the expression of WT T-bet."* This is a *bona fide* complementation experiment and should be curated as `SUPPORT` / `directness: DIRECT`.

**Branch C — the B-cell arm (a lineage lost, but clinically quiet)**

17. Loss of T-bet-dependent chromatin opening at *FAS, IL21R, SEC61B, DUSP4, DAPP1, SOX5* and closing at *CD79B, CXCR4* in activated B cells → **results in** complete absence of the **CD21^lo CD11c^hi CD19^hi CD20^hi FCRL5^hi T-bet^hi B-cell subset** (`CL:0000236` B cell), the human counterpart of murine age-associated B cells. Confirmed by 29-colour spectral flow (FlowSOM clusters 9, 10, 13, 14 all depleted) and by CITE-seq (*"the T-bet-deficient patient was completely devoid of cluster 3"*).
18. Loss of T-bet-dependent constraint on class-switch recombination, **plus** the Branch-B Th2 cytokine excess acting on B cells → **results in** skewing to **IgG1, IgG4, and IgE** with **reduced IgG2**. The authors explicitly attribute part of this to Branch B: *"increased serum IgG1, IgG4 and IgE in T-bet deficiency are consistent with skewing of T-bet deficient CD4+ T cells to a TH2-type effector function."* **This is a cross-branch interaction and should be drawn as such in the pathograph.**
19. **Branch C does not reach clinical disease.** Somatic hypermutation, affinity maturation, memory B-cell formation, plasmablast differentiation, and vaccine-specific antibody titres (tetanus, diphtheria, Hib, pneumococcus) were all normal, and *"he has not presented any clinical disease due to infections with, for example, S. pneumoniae."* Curate as a `Cellular`/`Laboratory` phenotype, **not** as an infection-susceptibility phenotype.

### 6b. Molecular pathways

| Pathway | Direction | Notes |
|---|---|---|
| **IL-12/IL-23 → STAT4 → IFN-γ axis** (KEGG hsa04630 JAK-STAT; Reactome R-HSA-877300 Interferon gamma signaling) | ↓ output | T-bet sits at the transcriptional output end; the axis is intact upstream but its effector node is broken |
| **IFN-γ → IFNGR → JAK1/JAK2 → STAT1 → IRF1** | ↓ downstream effect | Reduced ligand, not reduced receptor. Distinguishes IMD88 from IFNGR1/2 and STAT1 deficiencies |
| **TH1 differentiation program** (GO:0045063) | Abolished | *IFNG*, *CXCR3* transactivation lost |
| **TH2 differentiation program** (GO:0045064) | **De-repressed / ↑** | The reciprocal arm |
| **TLR9 (CpG) → MyD88/IRAK4 → T-bet induction in B cells** | Intact upstream, blocked at T-bet | IRAK4 deficiency abolished T-bet induction entirely, establishing TLR signalling as the required upstream input (PMID:35867801, Fig. 6H) |
| **IL-27 → IL27R → STAT1 → T-bet** | Partially redundant with IFN-γ | *"IFN-γ and IL-27 stimulate B cells through a common mechanism, probably involving T-bet, but... IFN-γ is the more potent stimulus"* |

**Suggested GO biological processes:**
`GO:0045063` T-helper 1 cell differentiation · `GO:0032609` interferon-gamma production · `GO:0032729` positive regulation of type II interferon production · `GO:0045064` T-helper 2 cell differentiation · `GO:0042092` type 2 immune response · `GO:0001780` neutrophil homeostasis (n/a) · `GO:0030101` natural killer cell activation · `GO:0001782` B cell homeostasis · `GO:0045190` isotype switching · `GO:0006338` chromatin remodeling · `GO:0071346` cellular response to interferon-gamma · `GO:0050830` defense response to Gram-positive bacterium

**Suggested GO molecular functions:**
`GO:0003700` DNA-binding transcription factor activity · `GO:0000981` DNA-binding transcription factor activity, RNA polymerase II-specific · `GO:0043565` sequence-specific DNA binding

### 6c. Cellular processes

- **Terminal maturation arrest** of NK and iNKT lineages — mouse data establish this is **stem-cell-intrinsic**: *"mice with a targeted deletion of T-bet... have a profound, stem cell-intrinsic defect in their ability to generate mature NK and Valpha14i NKT cells. Both cell types fail to complete normal terminal maturation and are present in decreased numbers in peripheral lymphoid organs"* ([PMID:15084276](https://pubmed.ncbi.nlm.nih.gov/15084276/), Townsend et al., *Immunity* 2004).
- **Lineage-commitment failure** in naïve CD4⁺ T cells (TH1) and in activated B cells (CD21^lo CD11c^hi subset).
- **Impaired macrophage classical activation** — inferred from the IFN-γ deficit, not directly measured in the patient. **Flag as inferred.**
- **Granuloma formation** — not characterized in the human patient. In *Tbx21*⁻/⁻ mice infected with *M. tuberculosis*, there is *"the striking accumulation of eosinophilic macrophages and multinucleated giant cells in the lung"* ([PMID:16177104](https://pubmed.ncbi.nlm.nih.gov/16177104/)) — an abnormal, type-2-flavoured granulomatous response rather than an absent one. **Extrapolation to human; do not curate as a human histopathology finding.**

### 6d. Protein dysfunction

Three concurrent defects in one mutant protein:
1. **Reduced steady-state protein** despite normal mRNA → post-transcriptional degradation.
2. **Impaired nuclear translocation** → less of the residual protein reaches its site of action (GO:0005634 nucleus).
3. **Abolished sequence-specific DNA binding** at the T-box motif → the fraction that does reach the nucleus is non-functional.

The p.E156/M157 residues lie at the N-terminal margin of the T-box domain (141–326). No experimental structure of the mutant is available; **AlphaFold/PDB modelling of this indel has not been reported** — this is an open structural question.

### 6e. Metabolic changes

**None reported.** No evidence of altered energy, lipid, or amino-acid metabolism in IMD88. Immunometabolic profiling of T-bet-deficient human lymphocytes has not been performed. This is a genuine data gap, not an absence.

### 6f. Immune system involvement

This *is* the disease. Two axes, both intrinsic:
- **Immunodeficiency** — selective, narrow, mycobacterial. Not a combined immunodeficiency; not a humoral immunodeficiency.
- **Immune dysregulation (allergic/type-2)** — asthma, upper airway inflammation, eosinophilia, IgE elevation.
- **No autoimmunity.** Despite enrichment of putatively autoreactive IGHV4-34-expressing IgG⁺ memory B cells (20.2% of IgG1 clones vs 8.5% in controls), *"there was no clinical or serological evidence of autoantibodies in the patient."* This is notable given that CD21^lo T-bet⁺ B cells are expanded in SLE and RA — the patient is a natural experiment for whether that expansion is causal, and so far argues against a *requirement*.

### 6g. Tissue damage mechanisms

- **Infectious/granulomatous tissue injury** from disseminated BCG in lymph nodes, liver, spleen, and skin.
- **Type-2 inflammatory airway remodelling.** In mice: *"increased type III collagen deposition below the bronchial epithelium basement membrane"* — i.e. subepithelial fibrosis (PMID:11786643). **Not documented histologically in the human patient**; treat as a model-organism finding with `evidence_source: MODEL_ORGANISM` and consider a `HUMAN_MODEL_MISMATCH` discussion node.
- **No oxidative-stress, ischemic, or necrotic mechanism** is implicated.

### 6h. Biochemical abnormalities

Not an enzymopathy, receptoropathy, or channelopathy. The biochemical lesion is a **transcription-factor DNA-binding defect**. Downstream measurable biochemistry: reduced IFN-γ, elevated IL-5 and IL-13, elevated IgE/IgG1/IgG4, reduced IgG2, elevated eosinophil count.

### 6i. Molecular profiling

| Modality | Finding | Source |
|---|---|---|
| **Bulk transcriptomics** | Transcriptome analysis performed on patient cells (MeSH: *Transcriptome/genetics*) | PMID:33296702 |
| **scRNA-seq / CITE-seq** | 5′ scRNA-seq + surface-protein (TotalSeq) + scVDJ on FACS-sorted live CD20⁺CD21^lo B cells; 937 cells from patient, 328/273 from two age-matched controls, 913 from an IFN-γR1-deficient patient. **Patient completely devoid of cluster 3** (CD19^hi, MS4A1^hi, ITGAX^hi, FCRL2/3/5^hi). Differentially expressed in cluster 3: ↑ *ENC1, ITGB2, TNFRSF1B, FCRL5, CD72, FCRL2, FCRL3, MS4A7, CD22, CD74, CD79A, CD81, CD164, FCGR2B, FCMR, FCRLA, IL21R, ITGB7, NFATC3, NR4A1/2/3*, HLA class II (*HLA-DRB1, -DPB1, -DPA1, -DQA1*); ↓ *CD44, CD53, CD69, CD70, CXCR4, CXCR5, NFKBIA, RELB, FCER2, CD24, CD27, ITGAM, SELL, LTB* | PMID:35867801 |
| **Omni-ATAC-seq (epigenomics)** | See §4e. 2,391 / 139 differentially accessible loci; 902 shared T-bet-dependent targets; IRF1/JUNB/RUNX1 motif enrichment | PMID:35867801 |
| **BCR repertoire (bulk IGH/IGK/IGL)** | Illumina NextSeq 2×300; fewer IgG2 clones, more IgG4; SHM intact; slightly reduced IGHM/IGK/IGL diversity; ↑ *IGHV3-15, IGHV3-43, IGHV7-4-1* in IgM; ↑ *IGHV4-34* in IgG memory | PMID:35867801 |
| **Spectral flow cytometry** | 29- and 30-colour panels, FlowSOM unsupervised clustering (30 clusters); clusters 9, 10, 13, 14 depleted in patient | PMID:35867801 |
| **DNA methylation** | CpG-island methylation analysis performed | PMID:33296702 (MeSH indexing) |
| **Proteomics** | **Not performed.** No PRIDE/ProteomeXchange dataset |
| **Metabolomics / lipidomics** | **Not performed.** No MetaboLights/Metabolomics Workbench dataset |
| **Spatial transcriptomics** | **Not performed** |
| **CRISPR/RNAi functional screens** | **Not performed in this disease context** |

**Dataset curation note.** I did not locate a public GEO/SRA/ArrayExpress accession for the CITE-seq or ATAC-seq data in a form I could verify. **Do not curate a `datasets:` accession for IMD88 without running `just verify-datasets` first** — and be aware that a *TBX21*-gene search will surface asthma and lymphoma datasets that have nothing to do with this disease (the Named Entity Confusion trap the repo's dataset-curation guidance warns about; *TBX21* is far more famous for asthma-association GWAS than for IMD88).

---

## 7. Anatomical Structures Affected

### Organ level

**Primary (site of immune lesion — the "organ" is the immune system itself):**

| Structure | UBERON |
|---|---|
| Hematopoietic/immune system | **UBERON:0002390** hematopoietic system / UBERON:0002405 immune system |
| Bone marrow (stem-cell-intrinsic maturation defect) | **UBERON:0002371** bone marrow |
| Thymus | **UBERON:0002370** thymus |
| Peripheral blood | **UBERON:0000178** blood |
| Lymph node | **UBERON:0000029** lymph node |
| Spleen | **UBERON:0002106** spleen |

**Secondary (sites of disseminated infection, n = 1):**

| Structure | UBERON | Manifestation | Laterality |
|---|---|---|---|
| **Axillary lymph node** | UBERON:0002439 | Lymphadenopathy | **Left — ipsilateral to the deltoid BCG injection site** (unilateral) |
| Skin | UBERON:0002097 | Cutaneous eruption | Variable |
| Liver | UBERON:0002107 | Hepatomegaly | — |
| Spleen | UBERON:0002106 | Splenomegaly | — |
| Abdominal/mesenteric lymph nodes | UBERON:0003950 | Deep adenopathy | Bilateral/central |

**Secondary (type-2 inflammation):**

| Structure | UBERON | Manifestation |
|---|---|---|
| **Upper respiratory tract / nasal mucosa** | UBERON:0001557 / UBERON:0001826 | Chronic upper airway inflammation |
| **Bronchus / lower respiratory tract** | UBERON:0002185 / UBERON:0001558 | Asthma, airway hyperresponsiveness |

**Body systems involved:** hematopoietic/lymphoid, respiratory, integumentary, hepatobiliary (secondary), reticuloendothelial.

**Notably spared:** central and peripheral nervous system, cardiovascular system, musculoskeletal system, kidney, endocrine organs. **No dysmorphology, no developmental anomaly, no neurocognitive involvement.** IMD88 is an *isolated* (non-syndromic) MSMD.

### Tissue and cell level

| Cell population | CL term | Status in IMD88 |
|---|---|---|
| **Natural killer cell** | **CL:0000623** | Severely reduced; residual cells IFN-γ-low |
| **Mature NK cell** | CL:0000824 | Terminal maturation blocked |
| **Invariant NKT (iNKT) cell** | **CL:0000921** (type I NKT) | Severely reduced |
| **MAIT cell** | **CL:0000940** mucosal invariant T cell | Severely reduced |
| **Vδ2⁺ γδ T cell** | **CL:0000798** gamma-delta T cell | Severely reduced |
| **T-helper 1 cell (classic)** | **CL:0000545** | Reduced; IFN-γ-low |
| **CD4⁺ αβ T cell** | **CL:0000624** | Numerically normal; **Th2-skewed** |
| **CD8⁺ αβ T cell** | **CL:0000625** | Normal number; **normal IFN-γ** — spared |
| **B cell** | **CL:0000236** | Normal overall; **CD21^lo CD11c^hi T-bet^hi subset absent** |
| **Memory B cell** | CL:0000787 | Normal number; IgG1⁺ ↑, IgG2⁺ ↓ |
| **Plasmablast** | CL:0000980 | Normal differentiation capacity *in vitro* |
| **Eosinophil** | **CL:0000771** | **Expanded** (blood eosinophilia) |
| **Macrophage** | **CL:0000235** | Impaired IFN-γ-dependent activation (inferred) |
| **Dendritic cell** | CL:0000451 | Studied in the index paper (MeSH: *Dendritic Cells/metabolism*); role in humans not fully resolved. Mouse T-bet regulates DC function |
| **Hematopoietic stem cell** | CL:0000037 | Site of the stem-cell-intrinsic NK/iNKT defect (mouse evidence) |

### Subcellular level

| Compartment | GO CC | Relevance |
|---|---|---|
| **Nucleus** | **GO:0005634** | T-bet's normal site of action; mutant translocates poorly |
| **Chromatin** | **GO:0000785** | Site of the T-bet-dependent accessibility program |
| **Cytoplasm** | GO:0005737 | Mutant protein mislocalized here |

No mitochondrial, lysosomal, peroxisomal, or ER pathology.

---

## 8. Temporal Development

### Onset

- **Age:** **Infantile** (HP:0003593). Symptoms began at **3 months of age**, within weeks of BCG vaccination.
- **Pattern:** **Acute** onset of the infectious episode (fever, regional lymphadenopathy, rash), progressing **subacutely** over ~3 months to disseminated disease by 6 months.
- **Onset is exposure-timed, not age-timed.** In a country that does not give BCG, an IMD88 patient would be expected to present later, on environmental-mycobacterium exposure. The 3-month figure is a property of Morocco's immunization schedule, not of the genotype. **Curate accordingly — do not assert "onset at 3 months" as a disease property.**
- The **asthma/upper-airway phenotype** onset is less precisely dated ("early childhood") and appears independent of the infectious timeline.

```yaml
onset:
  onset_category: INFANTILE_ONSET
  # HP:0003593
```

### Progression

**Stages (n = 1 trajectory):**

| Stage | Age | Features |
|---|---|---|
| **Presymptomatic** | Birth – 3 mo | Genotype present; no disease |
| **Local/regional (BCG-itis-like)** | 3 mo | Fever, left axillary lymphadenopathy, cutaneous eruption |
| **Disseminated (BCG-osis)** | 6 mo | Persistent fever, weight loss, hepatosplenomegaly, abdominal adenopathy → hospitalization |
| **Treated remission** | 6 mo – 2 yr | 18 months of four-drug antimycobacterial therapy, good response |
| **Sustained off-therapy remission** | 2 yr onward | Off antibiotics ≥15 months at the time of the *Cell* study; *"in remission and free of mycobacterial infection for several years"* by 2022 |
| **Chronic type-2 phase** | Concurrent & ongoing | Persistent asthma, upper airway inflammation, eosinophilia — **does not remit** with antimycobacterial cure |

- **Progression rate of the infection:** rapid (weeks–months) if untreated; **arrested by therapy**.
- **Course of the immunodeficiency:** **lifelong and non-progressive** — the underlying genetic defect does not worsen; risk is exposure-contingent.
- **Course of the airway disease:** **chronic, persistent** (`clinical_course: PROGRESSIVE` is *not* supported; use `temporality: CHRONIC`).
- **Disease duration:** **chronic lifelong** susceptibility; individual infectious episodes are self-limited *with treatment*.

### Patterns

- **Remission:** **treatment-induced**, sustained. No spontaneous remission reported. No relapse reported over several years off antibiotics.
- **Critical periods:**
  - **Neonatal/early infancy — the highest-value intervention window.** Withholding or deferring BCG in an at-risk newborn prevents the entire Branch-A clinical phenotype. This is the strongest actionable statement in the whole disease.
  - Errami et al.: BCG *"should be delayed in newborn siblings until the exclusion of a genetic predisposition to mycobacteria."*
  - **Early recognition of BCG-itis** — the regional phase (3 months) precedes dissemination (6 months) by a treatable interval.

---

## 9. Inheritance and Population

### Epidemiology

**IMD88 specifically:**
- **Reported cases: 1 (one).** Prevalence is therefore best recorded as `prevalence_class: CASES_IN_LITERATURE` / `ULTRA_RARE`, `measure_type: CASES_IN_LITERATURE`, count = 1.
- OMIM notes only one patient reported as of 2021, and I found **no subsequent independent case** in literature through September 2026. The 2025 Moroccan cohort ([PMID:41209815](https://pubmed.ncbi.nlm.nih.gov/41209815/)) reports *"TBX21 in 1 patient"* among 23 genetically diagnosed MSMD — **almost certainly the same individual**, since it is the same centre (Casablanca) and same collaborating group. **Do not double-count.**

**MSMD as a class — and note the sources disagree:**

| Estimate | Source |
|---|---|
| **~1/10,000 individuals worldwide** | [PMID:36630059](https://pubmed.ncbi.nlm.nih.gov/36630059/) (Errami et al., *J Clin Immunol* 2023): *"This condition affects about 1/10,000 individuals worldwide."* |
| **~1/50,000 individuals** | [PMID:36326697](https://pubmed.ncbi.nlm.nih.gov/36326697/) (Ogishi et al., *J Exp Med* 2023): MSMD *"selectively predisposes ∼1/50,000 individuals to severe disease caused by weakly virulent mycobacteria."* |

**A five-fold discrepancy between two 2023 papers from overlapping author groups.** Report both; do not average them. If curating a single `Prevalence` record for the MSMD parent concept, curate **two records** with distinct evidence, or pick the more conservative and record the other in `notes`.

- Within MSMD, ***TBX21* accounts for 1 of 23** genetically diagnosed Moroccan MSMD patients (~4%) and **1 of 22** in the earlier kindred series — i.e. **the rarest identified etiology in that cohort**. AR complete IL-12Rβ1 deficiency is *"found in about 60% of diagnosed patients as the most common genetic cause of MSMD."*
- **~50% of all MSMD patients remain genetically unexplained**: *"no genetic disorder has yet been identified for about half of all MSMD patients."* Additional *TBX21* patients plausibly sit in that unexplained fraction.

### Genetic parameters

| Parameter | Value | Basis |
|---|---|---|
| **Inheritance** | **Autosomal recessive** (HP:0000007) | Homozygous variant, consanguineous parents, unaffected heterozygous mother, unaffected WT sibling |
| **Penetrance** | **Undetermined.** n = 1 precludes estimation | — |
| **Penetrance (contextual prior)** | Within MSMD, only AR **complete** IFN-γR1, IFN-γR2, and IFN-γ deficiencies are established as **fully penetrant**; *"defects associated with a residual production or response to IFN-γ show incomplete penetrance"* (PMID:36630059). T-bet deficiency leaves substantial residual IFN-γ from CD8⁺/TH1\* cells — which **predicts incomplete penetrance**, but this is inference, not observation. **Flag explicitly as inferred.** |
| **Expressivity** | Undetermined (n = 1) | — |
| **Genetic anticipation** | **Not applicable** — not a repeat-expansion disorder | — |
| **Germline mosaicism** | Not reported; no reason to suspect | — |
| **Founder effect** | **None demonstrated.** Private variant | — |
| **Consanguinity** | **Central.** First-cousin parents. Regionally: 64% consanguinity among Moroccan MSMD patients (PMID:36630059); 51.1% across Moroccan innate/intrinsic IEI (PMID:41209815); 60.5% across 17,120 MENA IEI patients (cited in PMID:41209815) | — |
| **Carrier frequency** | **Unknown.** No population screening; the variant is private | — |

### Population demographics

- **Affected populations:** one Moroccan (North African/Maghrebi) kindred. **No basis for an ethnic predisposition claim** — ascertainment is entirely explained by BCG mandate + TB endemicity + high consanguinity + an active reference immunology centre in Casablanca collaborating with the Casanova/Bustamante laboratories.
- **Geographic distribution:** Morocco (single kindred). Variant-specific geography: not applicable.
- **Sex ratio:** the index patient is **male**. AR inheritance predicts **1:1**. Do not curate 1:0.
- **Age distribution:** infantile onset; the patient was born in 2015 and was ~3–7 years old across the published studies. No adult IMD88 patient has been described.
- **Diagnostic delay (regional context):** median **35 months** (IQR 6–80) across the Moroccan innate/intrinsic IEI cohort (PMID:41209815); mean age at MSMD diagnosis 87 months vs mean onset 47 months in the same cohort.

---

## 10. Diagnostics

### 10a. Clinical / laboratory tests

**First-line, non-genetic:**

| Test | Expected finding in IMD88 | LOINC (representative) |
|---|---|---|
| CBC with differential | **Eosinophilia** (HP:0001880); anemia/pancytopenia possible during dissemination | LOINC:57021-8 (CBC W Auto Differential) |
| Lymphocyte subset flow cytometry (CD3/CD4/CD8/CD19/CD16+56) | **Reduced NK cells**; CD3/CD4/CD8/CD19 typically within normal range | LOINC:52447-0 |
| **Extended flow: iNKT, MAIT, Vδ2⁺ γδ T** | **Severely reduced — the discriminating test** | — |
| Serum immunoglobulins (IgG, IgA, IgM, IgE) | **↑ IgE**, ↑ total IgG (IgG1-driven) | LOINC:2458-8 (IgE), 2465-3 (IgG) |
| **IgG subclasses** | **↓ IgG2**, ↑ IgG1, modest ↑ IgG4 | LOINC:2465-3 series |
| Plasma IL-5, IL-13 | **Markedly elevated** | — |
| **Whole-blood IL-12/IFN-γ axis functional assay** (BCG ± rhIL-12; BCG ± rhIFN-γ) | **Reduced IFN-γ production**; IL-12 production preserved | — |
| Vaccine-specific IgG (tetanus, diphtheria, Hib, pneumococcus) | **Normal — an informative negative** that excludes humoral immunodeficiency | — |
| NBT / DHR (to exclude CGD) | **Normal** — excludes *CYBB*-related syndromic MSMD | LOINC:32571-0 |
| HIV serology | **Negative** — mandatory exclusion | LOINC:75622-1 |

**Microbiology (essential and often the rate-limiting step):**
- Mycobacterial culture from blood, bone marrow, lymph node aspirate/biopsy
- Ziehl–Neelsen / auramine acid-fast staining
- **BCG substrain-specific PCR** to distinguish vaccine strain from *M. tuberculosis* / *M. bovis* — this distinction changed management in the ITK cohort and is directly relevant here
- Species-level identification (MALDI-TOF, line probe assay, sequencing)

> PMID:38535546 is candid about this: *"Isolating these organisms presents a significant challenge, and treatment is often initiated without confirming the specific species."*

**Imaging:** chest radiograph and CT (pulmonary infiltrates, mediastinal adenopathy, tree-in-bud); abdominal ultrasound/CT (hepatosplenomegaly, mesenteric adenopathy); consider MRI for suspected CNS involvement.

**Functional respiratory:** spirometry with bronchodilator reversibility and/or methacholine challenge for the asthma component; FeNO for type-2 airway inflammation.

**Biopsy/histopathology:** lymph node biopsy showing granulomatous inflammation with acid-fast bacilli. **Human IMD88 granuloma histopathology has not been characterized in the published literature** — an explicit gap. The mouse phenotype (eosinophilic macrophages, multinucleated giant cells) is *not* transferable as a human claim.

**Electrophysiology:** not indicated.

### 10b. Genetic testing

**Recommended approach — WES/WGS first.** The index case was solved by **whole-exome sequencing combined with genome-wide linkage analysis**, confirmed by Sanger. Errami et al. used *"WES for all index cases and Sanger sequencing for relatives or to confirm mutations."*

| Modality | Utility in IMD88 |
|---|---|
| **WES** | **High — the primary modality.** Solved the index case. Standard of care for suspected MSMD |
| **WGS** | High; adds non-coding/structural resolution. No IMD88-specific advantage demonstrated |
| **Targeted MSMD/IEI gene panel** | **High, if *TBX21* is on the panel.** *TBX21* is a recent addition (2020) — **verify panel content**; older MSMD panels omit it. This is a real failure mode |
| **Single-gene *TBX21* sequencing** | Low yield as a first test given genetic heterogeneity. Appropriate for **cascade/family segregation testing** once the familial variant is known |
| **Chromosomal microarray** | **Not indicated** |
| **Karyotype / FISH** | **Not indicated** |
| **mtDNA testing** | **Not indicated** |
| **Repeat-expansion testing** | **Not indicated** |

The Moroccan authors argue for cost-adapted strategies: because six of their patients shared one *IL12RB1* variant, *"cost-effective diagnostic methods, such as PCR, could be used for early detection in this population."* That logic does **not** extend to *TBX21*, whose single known variant is private.

**Functional confirmation is expected for a novel *TBX21* variant** and was performed for the index variant: HEK293T overexpression assays for protein level, nuclear translocation, and DNA binding; EMSA/reporter transactivation; IFN-γ induction in NK/CD4⁺ T cells; and — decisively — **WT T-bet complementation reversing the Th2 phenotype**.

### 10c. Omics-based diagnostics

**None validated for clinical use.** RNA-seq, ATAC-seq, CITE-seq, and BCR repertoire sequencing were **research** tools here, not diagnostics. Liquid biopsy, proteomics, metabolomics: not applicable.

**Deep immunophenotyping is, however, effectively diagnostic** — the combined pattern of reduced NK + iNKT + MAIT + Vδ2⁺ γδ T with preserved CD8⁺ IFN-γ is not produced by any other known MSMD genotype and should be treated as a strong genotype-predictive signature.

### 10d. Clinical criteria

**No IMD88-specific criteria exist.** Diagnosis proceeds via MSMD criteria + molecular confirmation.

MSMD entry criteria as operationalized by Errami et al.: *"complicated local/regional (BCG-itis) or systemic, disseminated reactions (BCG-osis) to BCG vaccination, unusually severe, persistent, and/or recurrent infections with mycobacteria, and/or tuberculosis (TB), and/or salmonella and/or CMC."*

**ESID criteria** are used for disseminated BCG disease. Operational definitions (Errami et al.):
- **Local BCG-itis:** local abscess at the injection site ≥10 mm × 10 mm and/or severe BCG scar ulceration
- **Regional BCG-itis:** involvement of regional lymph nodes or lesions beyond the injection site (axillary, supraclavicular, cervical, ipsilateral)
- **BCG-osis:** confirmed in **more than one remote site** beyond the vaccination site, and/or at least one positive blood or bone marrow culture

The index patient meets **BCG-osis** criteria (hepatosplenomegaly + abdominal adenopathy + axillary node).

### 10e. Differential diagnosis

| Condition | Distinguishing features |
|---|---|
| **AR complete IL-12Rβ1 deficiency** | Most common MSMD cause (~60%); absent IL-12Rβ1 surface expression; abolished IFN-γ response to IL-12; **NK/iNKT/MAIT numbers preserved** |
| **AR/AD IFN-γR1 or IFN-γR2 deficiency** | Defect in *response* to IFN-γ, not production. **Elevated circulating IFN-γ** in complete receptor deficiency (receptor absent → cytokine not cleared — note PMID:41209815 explicitly corrects the misreading of this as compensatory). AR complete forms are fully penetrant and far more severe |
| **AR complete STAT1 deficiency** | Broader: mycobacterial **plus severe viral** susceptibility. CD21^lo CD11c^int B cells present but CD11c^hi T-bet^hi subset reduced — a *partial* phenocopy of the IMD88 B-cell defect (PMID:35867801) |
| **AD STAT1 GOF** | Chronic mucocutaneous candidiasis-dominant, not MSMD |
| **AR TYK2 deficiency / TYK2 P1104A homozygosity** | TB-predominant; incomplete penetrance for MSMD |
| **SPPL2A deficiency** | cDC2 depletion via CD74 fragment toxicity; reduced Th1 memory |
| **IRF8, NEMO, CYBB (X-linked MSMD)** | Syndromic; CGD-overlap for *CYBB* (abnormal DHR) |
| **ITK deficiency** | TB + EBV viremia + warts + lymphoma risk; CD4 lymphopenia with DN αβ/Vδ2⁻ γδ expansion (PMID:36326697) |
| **HIV infection** | Must be excluded — an explicit exclusion criterion in the Moroccan protocol |
| **Severe combined / combined immunodeficiency** | Broad infection spectrum; IMD88's **narrow, mycobacteria-only** clinical susceptibility argues against |
| **Hyper-IgE syndromes (STAT3/DOCK8)** | Share ↑IgE + eosinophilia + asthma-like features. Distinguished by staphylococcal/fungal infections, skeletal/connective-tissue features, NIH score. **This is the most important differential for the type-2 arm** — and a Moroccan HIES cohort of 126 patients exists at the same centre ([PMID:39441153](https://pubmed.ncbi.nlm.nih.gov/39441153/)) |
| **Isolated atopic asthma with eosinophilia** | Would not explain BCG-osis. Conversely: **an infant with BCG complications who also has unexplained persistent asthma and eosinophilia should raise *TBX21* specifically** — this combination is the IMD88 fingerprint |

### 10f. Screening

- **Newborn screening: not available.** TREC-based SCID screening will **not** detect IMD88 (T-cell numbers are normal).
- **Carrier screening: not available**; the variant is private.
- **Cascade screening: the highest-value screening action.** Once a familial *TBX21* variant is known, test siblings by Sanger **before administering BCG**. This is the actionable recommendation and Errami et al. state it directly.
- **Risk stratification:** consanguineous families with a BCG-complication history in TB-endemic, BCG-mandating countries.

---

## 11. Outcome / Prognosis

> **All prognostic statements for IMD88 are n = 1.** Curate them as case-level observations, never as survival statistics.

### Survival and mortality

- **Survival: the single reported patient survived.** Alive and in remission at last report (~2022, age ~7).
- **5-/10-year survival, life expectancy, mortality rate, disease-specific mortality: NOT ESTABLISHED.** No data exist. Do not populate these fields.
- **MSMD-class context:** mortality is highly genotype-dependent. AR complete IFN-γR1/R2 deficiency carries the worst prognosis (often fatal without HSCT); IL-12Rβ1 deficiency is substantially better. **T-bet deficiency's residual CD8⁺/TH1\* IFN-γ capacity predicts a milder position on this spectrum — but this is inference from one favourable case plus mechanistic reasoning, not evidence.**

### Morbidity and function

- **Acute morbidity:** hospitalization, disseminated infection, 18 months of four-drug therapy.
- **Chronic morbidity:** persistent asthma and upper-airway inflammation — **the durable functional burden**, unaffected by antimycobacterial cure.
- **Disability outcomes:** no reported permanent organ damage, no neurological sequelae, no growth failure after recovery.
- **QoL measures:** **none applied.** No EQ-5D, PedsQL, SF-36, PROMIS, or ACT/ACQ asthma-control score has been reported.

### Disease course and complications

- **Complications observed:** dissemination to liver, spleen, abdominal nodes; weight loss; chronic airway disease.
- **Complications predicted but not observed:** recurrent mycobacterial disease, TB, non-typhoidal salmonellosis, NTM infection.
- **Notable non-complications:** no bacterial sepsis, no pneumococcal disease despite documented exposure and reduced IgG2, no EBV disease, no autoimmunity, no malignancy.
- **Recovery potential: excellent with treatment** in this case — complete clinical remission sustained for years off antibiotics.
- **Without treatment:** disseminated BCG disease is expected to be life-threatening (general MSMD principle).

### Prognostic factors

| Factor | Direction | Basis |
|---|---|---|
| **Residual IFN-γ production capacity** | **Favourable.** Preserved CD8⁺ αβ T and CD4⁺ TH1\* IFN-γ responses | PMID:33296702; and PMID:36630059's general rule that residual IFN-γ ⇒ incomplete penetrance |
| Early diagnosis and prompt antimycobacterial therapy | Favourable | PMID:41209815 |
| Diagnostic delay (regional median 35 months) | Unfavourable | PMID:41209815 |
| Avoidance of further live mycobacterial exposure | Favourable | PMID:36630059 |
| Extent of dissemination at presentation | Unfavourable | MSMD class |

**Prognostic biomarkers:** none validated. Plausible candidates requiring study: whole-blood IFN-γ output on BCG stimulation; NK/iNKT/MAIT/Vδ2 absolute counts; plasma IL-5/IL-13 for the type-2 arm.

---

## 12. Treatment

> No IMD88-specific trial or guideline exists. Management follows MSMD principles plus standard asthma care. **All treatment content below is class-level MSMD evidence or single-case experience.**

### 12a. Antimycobacterial pharmacotherapy — the definitive treatment of the acute episode

**What the patient received:** *"Treated with four antimycobacterial drugs for 18 months with good response"* — the standard MSMD regimen. Errami et al. name the agents: **rifampin, isoniazid, pyrazinamide, ethambutol.**

Note: BCG substrains are intrinsically **pyrazinamide-resistant**; regimen composition should follow species/susceptibility once identified.

```yaml
treatments:
- name: Multidrug Antimycobacterial Therapy
  therapeutic_modality: SMALL_MOLECULE
  treatment_term:
    preferred_term: antimycobacterial pharmacotherapy
    term: {id: NCIT:C15986, label: Pharmacotherapy}
    therapeutic_agent:
    - preferred_term: rifampicin
      term: {id: CHEBI:28077, label: rifampicin}
    - preferred_term: isoniazid
      term: {id: CHEBI:6030, label: isoniazid}
    - preferred_term: pyrazinamide
      term: {id: CHEBI:45285, label: pyrazinamide}
    - preferred_term: ethambutol
      term: {id: CHEBI:4877, label: ethambutol}
```
**Verify every CHEBI ID above with `runoak` before curating** — I am supplying these from general knowledge, not from a validated lookup in this session.

### 12b. Recombinant human IFN-γ — the mechanistically indicated adjunct

> *"Patients with defects in IFN-γ production may benefit from treatment with recombinant human IFN-γ, in addition to antibiotics."* — [PMID:36630059](https://pubmed.ncbi.nlm.nih.gov/36630059/)

**IMD88 sits squarely in the "defects in IFN-γ production" category, so IFN-γ replacement is the rational adjunct** — the receptor and its signalling are intact. Efficacy of rhIFN-γ in the same laboratory's ITK-deficiency patients is instructive: subcutaneous rhIFN-γ plus four-drug therapy produced *"complete remission"* in P1 (healthy at 28 years); P2 *"recovered on standard anti-TB therapy plus subcutaneous IFN-γ injections"* and remains on biweekly IFN-γ ([PMID:36326697](https://pubmed.ncbi.nlm.nih.gov/36326697/)).

**However — the published IMD88 case does not report rhIFN-γ use.** He responded to antibiotics alone. **Do not curate rhIFN-γ as an administered treatment for this patient**; curate it as an indicated class-level therapy with `evidence_source: HUMAN_CLINICAL` citing the MSMD literature, and record the distinction in `notes`.

```yaml
- name: Recombinant Interferon Gamma Therapy
  therapeutic_modality: PROTEIN_REPLACEMENT
  treatment_term:
    preferred_term: interferon gamma therapy
    term: {id: NCIT:C15986, label: Pharmacotherapy}
    therapeutic_agent:
    - preferred_term: interferon gamma-1b
      term: {id: NCIT:C1471, label: Interferon Gamma}   # VERIFY with runoak
  notes: >-
    Indicated in MSMD due to impaired IFN-gamma production; not reported as
    administered to the single published IMD88 patient.
```

### 12c. Hematopoietic stem cell transplantation

> *"Hematopoietic stem cell transplantation (HSCT) is the only medical option to date for patients with completely defective responses to IFN-γ."* — PMID:36630059

**HSCT is indicated for defects in IFN-γ *response* — which IMD88 is not.** IMD88 is a production/development defect with intact receptor signalling. HSCT would nonetheless be curative in principle, since the defect is hematopoietic and **stem-cell-intrinsic** for the NK/iNKT compartment (PMID:15084276). **No IMD88 patient has undergone HSCT.** Curate as a theoretical/reserve option, explicitly not as standard of care.

`NCIT:C15431` Hematopoietic Cell Transplantation → `therapeutic_modality: CELL_THERAPY`

### 12d. Management of the type-2 / asthma arm

Standard asthma therapy is indicated; nothing IMD88-specific has been published.

- **Inhaled corticosteroids** — `NCIT:C15986` + CHEBI agent; `therapeutic_modality: SMALL_MOLECULE`
- **Inhaled β2-agonists (bronchodilators)**
- **Leukotriene receptor antagonists** (montelukast)
- **Anti-IL-5 (mepolizumab, benralizumab) or anti-IL-4Rα (dupilumab)** — **mechanistically the most interesting untried option.** The patient has *"markedly high plasma IL-5 and IL-13 concentrations"*; dupilumab blocks IL-4Rα (IL-4 and IL-13 signalling) and anti-IL-5 targets the eosinophil driver directly. `therapeutic_modality: MONOCLONAL_ANTIBODY`, `NCIT:C20401` Monoclonal Antibody. **No IMD88 patient has received biologic therapy; this is a hypothesis, and should be curated as a `discussions` entry with `kind: KNOWLEDGE_GAP` and a `proposed_experiments` block, not as a treatment.**

### 12e. Advanced therapeutics

| Modality | Status for IMD88 |
|---|---|
| **Gene therapy / gene editing** | **Not developed.** No vector, no preclinical program. *TBX21* is a transcription factor requiring stoichiometric and lineage-restricted expression — a hard gene-therapy target |
| **ASO / siRNA / mRNA therapy** | **Not applicable** — LoF disorder; would require gene addition, not knockdown or splice modulation |
| **Cell therapy** | HSCT only (§12c). No adoptive NK/iNKT transfer has been attempted |
| **Targeted small molecules** | None. No T-bet agonist exists |
| **Immunotherapy** | rhIFN-γ (§12b); anti-type-2 biologics (§12d) |

### 12f. Surgical and interventional

- **Lymph node excision/drainage** for suppurative or fistulizing BCG lymphadenitis — supportive, adjunct to chemotherapy. `NCIT:C15329` Surgical Procedure, `therapeutic_modality: SURGERY`
- **Diagnostic biopsy** for microbiological confirmation

### 12g. Supportive and rehabilitative

- Nutritional support during the wasting phase of disseminated disease (`NCIT:C15433` Nutritional Support — **do not auto-tag this as `BEHAVIORAL`**, per the repo's explicit backfill caveat)
- Antipyretics, symptom management
- **Genetic counselling** — `NCIT:C15240` Genetic Counseling, `therapeutic_modality: BEHAVIORAL`
- No rehabilitation need reported

### 12h. Experimental treatments / clinical trials

**No clinical trial has ever enrolled an IMD88 patient.** No NCT identifier is associated with IMD88, TBX21 deficiency, or T-bet deficiency. Broader MSMD trials (rhIFN-γ, HSCT registries) may be relevant but do not name this genotype. **Do not curate a `clinical_trials` block for IMD88 without a verified, disease-specific NCT.**

### 12i. Treatment outcomes

- **Response rate:** 1/1 responded to four-drug therapy with sustained remission.
- **Adverse events:** none reported for this patient. Class AEs of the regimen (hepatotoxicity from isoniazid/rifampin/pyrazinamide; ethambutol optic neuritis; rhIFN-γ flu-like syndrome) apply but are not IMD88-specific.

### 12j. Treatment strategy / algorithm

1. **Recognize** BCG complication or unexplained mycobacterial disease in a child → suspect MSMD
2. **Exclude HIV**; exclude CGD (DHR/NBT)
3. **Culture and speciate** (BCG substrain PCR)
4. **Start empiric multidrug antimycobacterial therapy** — do not wait for species confirmation
5. **Whole-blood IL-12/IFN-γ functional assay** → localize the defect to production vs response
6. **WES** (or a current-generation MSMD panel that includes *TBX21*)
7. **Extended immunophenotyping** (NK, iNKT, MAIT, Vδ2⁺ γδ T) — for IMD88 this is near-pathognomonic
8. **If IFN-γ production defect confirmed → add recombinant human IFN-γ**
9. **Contraindicate all live mycobacterial vaccines**; test and defer BCG in siblings
10. **Genetic counselling** for the consanguineous kindred
11. **Manage the type-2 airway phenotype separately and indefinitely** — it will not remit with antimycobacterial cure
12. **Reserve HSCT** for refractory disease (no IMD88 precedent)

### 12k. Pharmacogenomics

**No IMD88-specific pharmacogenomics.** Generic and important: ***NAT2* acetylator status** governs isoniazid metabolism and hepatotoxicity/neuropathy risk (PharmGKB/CPIC); relevant to any patient on prolonged isoniazid, not to IMD88 specifically.

---

## 13. Prevention

### Primary prevention

**The single highest-impact intervention in this disease is negative: do not give BCG.**

> *"BCG vaccination is contraindicated in MSMD patients and should be delayed in newborn siblings until the exclusion of a genetic predisposition to mycobacteria."* — [PMID:36630059](https://pubmed.ncbi.nlm.nih.gov/36630059/)

- **All live mycobacterial and attenuated-organism vaccines are contraindicated** in confirmed IMD88.
- **Deferral of BCG in newborn siblings** of a known MSMD proband, pending genetic exclusion, prevents the entire Branch-A phenotype.
- Reduce environmental mycobacterial exposure where practicable (aerosolized water sources, soil) — plausible but unevidenced for IMD88 specifically.
- **The disease itself is not primarily preventable** — it is inherited. Prevention targets the *precipitant*, not the genotype.

### Secondary prevention

- **Cascade genetic testing** of siblings and at-risk relatives once the familial variant is known.
- **Early recognition of BCG-itis** — the regional phase precedes dissemination by ~3 months in the index case, a real treatment window.
- **Prompt evaluation of any febrile illness** with mycobacterial cultures.

### Tertiary prevention

- Complete the full antimycobacterial course (18 months in the index case) to prevent relapse.
- Ongoing surveillance for TB, NTM, and salmonellosis.
- **Long-term asthma control** to prevent airway remodelling — supported mechanistically by the mouse subepithelial collagen deposition finding (PMID:11786643), though unproven in humans.

### Immunization

| Vaccine class | Recommendation |
|---|---|
| **BCG and all live mycobacterial vaccines** | **CONTRAINDICATED** |
| Other **live attenuated** vaccines (oral polio, rotavirus, MMR, varicella, yellow fever) | Caution advised on general IEI principles. **Not specifically evaluated in IMD88.** The patient tolerated documented exposure to multiple viruses without disease, which is reassuring but not a licence — flag as an open question |
| **Inactivated / subunit vaccines** (DTaP, IPV, Hib, pneumococcal conjugate, influenza, hepatitis B) | **Recommended and effective.** The patient mounted **normal IgG titres to tetanus, diphtheria, Hib, and pneumococcus** — direct evidence that inactivated vaccination works in IMD88 (PMID:35867801, Table S1) |

This is an unusually clean and clinically useful result: **IMD88 patients respond normally to routine non-live vaccines.**

### Screening, counselling, and public health

- **Newborn screening:** unavailable and not feasible with current TREC-based platforms.
- **Prenatal / PGT:** technically feasible for a known familial variant; not reported. Appropriate to discuss with a consanguineous kindred.
- **Genetic counselling:** 25% recurrence risk per pregnancy; carrier testing for parents and relatives; discussion of consanguinity risk more broadly.
- **Public health:** in high-consanguinity, TB-endemic, BCG-mandating settings, a **family history of BCG complications should trigger deferral of BCG in subsequent newborns pending evaluation**. PMID:41209815 makes the broader system-level point — median 35-month diagnostic delay driven by *"the lack of awareness of emerging diseases unfamiliar to clinicians and the lack of diagnostic facilities due to the high cost of required molecular tests."*
- **Prophylaxis:** no established antimicrobial prophylaxis regimen for IMD88. Prophylactic macrolides/rifamycins are used in some severe MSMD genotypes; no IMD88 precedent.

---

## 14. Other Species / Natural Disease

### Taxonomy and orthologs

| Species | NCBITaxon | Gene | NCBI Gene ID |
|---|---|---|---|
| Human | **NCBITaxon:9606** | *TBX21* | 30009 |
| Mouse | **NCBITaxon:10090** | *Tbx21* | 57765 |
| Rat | NCBITaxon:10116 | *Tbx21* | 301243 |
| Zebrafish | NCBITaxon:7955 | *tbx21* | — |
| Chicken | NCBITaxon:9031 | *TBX21* (T-bet) | — (identified: [PMC12332921](https://pmc.ncbi.nlm.nih.gov/articles/PMC12332921/)) |
| Cattle | NCBITaxon:9913 | *TBX21* | — |

**Verify all non-human Gene IDs before curating** — I supply these from general knowledge, not from a validated NCBI Gene lookup in this session.

### Natural disease in other species

**No naturally occurring *TBX21*-deficiency disease has been described in any animal species.** OMIA contains no entry for T-bet deficiency. There is no veterinary counterpart, no companion-animal or wildlife natural model.

**However, mycobacterial disease susceptibility is a major veterinary problem in its own right**, and T-bet biology is implicated: *"Preferential differential gene expression within the WC1.1+ γδ T cell compartment in cattle naturally infected with Mycobacterium bovis"* ([PMID:37942326](https://pubmed.ncbi.nlm.nih.gov/37942326/), *Front Immunol* 2023) — bovine γδ T cells, the veterinary analog of the Vδ2⁺ compartment lost in IMD88. This is a comparative-immunology parallel, **not a natural disease model of IMD88.**

### Comparative biology

- **Evolutionary conservation is strong.** T-bet's role as the TH1/type-1 master regulator is conserved from birds through mammals.
- **Key conserved function:** T-bet-dependent NK and NKT terminal maturation, demonstrated in mouse (PMID:15084276) and mirrored in human (PMID:33296702).
- **Key conserved dissociation:** T-bet is required for IFN-γ control in CD4 and NK cells **but not CD8 cells** in mouse (PMID:11786644) — and the human patient's CD8⁺ αβ T cells likewise produce IFN-γ normally. **This cross-species concordance is the strongest translational validation in the disease.**
- **Key conserved reciprocal repression:** T-bet loss produces spontaneous asthma-like airway disease in mice (PMID:11786643) and asthma + eosinophilia + Th2 cytokine excess in the human patient (PMID:35909394).
- **Key divergence — curate as a `HUMAN_MODEL_MISMATCH`:** *"T-bet-deficient mice have reduced ABCs and impaired humoral immunity"*, yet the human patient has *"largely normal humoral immunity including intact somatic hypermutation, affinity maturation and memory B cell formation in vivo"* (PMID:35867801). The murine humoral phenotype **does not translate**. This is a textbook case for the `HUMAN_MODEL_MISMATCH` discussion kind rather than a generic knowledge gap: evidence exists in the model, and its translational validity is the open question — and here it has been *answered negatively*.

### Transmission

**No zoonotic potential.** IMD88 is a non-transmissible inherited disorder. The *pathogens* it predisposes to (*M. bovis* BCG, *M. tuberculosis*, *M. bovis*, NTM, *Salmonella*) have their own transmission biology, but the host disorder does not.

---

## 15. Model Organisms

### Available models

| Model | Type | Availability |
|---|---|---|
| ***Tbx21*^tm1Glm* (T-bet knockout mouse)** | Mammalian, germline KO | **The workhorse model.** Generated in the Glimcher laboratory; used in PMID:11786643, PMID:11786644, PMID:15084276, PMID:16177104. Available via **MGI / IMSR / JAX** — verify current stock numbers |
| Conditional / floxed *Tbx21* | Mammalian, conditional | Reported in the literature (lineage-restricted deletion). Verify via MGI/IMPC before citing a specific allele |
| **Knock-in of the human p.E156_M157delinsSL allele** | Mammalian, humanized | **Does not exist.** No disease-specific model of the IMD88 variant has been made |
| **HEK293T overexpression assay** | *In vitro*, heterologous | Used for the index functional work (protein level, nuclear translocation, DNA binding). Cellosaurus CVCL_0063 |
| **Herpesvirus saimiri-immortalized patient T cells** | *In vitro*, patient-derived | **Used and highly informative** — produced *"abnormally large amounts of Th2 cytokines"* (PMID:35909394) |
| **Patient PBMC / primary naïve and memory B cells** | *Ex vivo*, patient-derived | Used for ATAC-seq, CITE-seq, spectral flow, *in vitro* differentiation (PMID:35867801) |
| **Patient-derived iPSC / organoid** | NAM | **Do not exist** |
| Zebrafish, *Drosophila*, *C. elegans*, yeast | — | **Not applicable.** No adaptive immune system / no meaningful ortholog function |

### Phenotype recapitulation — *Tbx21*⁻/⁻ mouse

| Human feature | Mouse | Fidelity | Citation |
|---|---|---|---|
| Failure of TH1 lineage commitment | **Recapitulated** | HIGH | PMID:11786644 |
| Reduced IFN-γ in CD4 and NK cells | **Recapitulated** | HIGH | PMID:11786644 |
| **Preserved CD8⁺ IFN-γ production** | **Recapitulated** — *"required for control of IFN-γ production in CD4 and NK cells, but not in CD8 cells"* | **HIGH — this is the key concordance** | PMID:11786644 |
| Reduced/immature NK and iNKT cells | **Recapitulated** — *"a profound, stem cell-intrinsic defect in their ability to generate mature NK and Valpha14i NKT cells"* | HIGH | PMID:15084276 |
| Susceptibility to mycobacteria | **Recapitulated** — increased systemic bacterial burden with *M. tuberculosis* | HIGH | PMID:16177104 |
| Asthma / airway hyperresponsiveness | **Recapitulated**, spontaneously and allergen-independently | HIGH | PMID:11786643 |
| Eosinophilic airway inflammation | **Recapitulated** — peribronchial eosinophilic and lymphocytic infiltration | HIGH | PMID:11786643 |
| Airway remodelling (subepithelial collagen III) | **Recapitulated in mouse; NOT assessed in human** | UNKNOWN in human | PMID:11786643 |
| MAIT / Vδ2⁺ γδ T deficiency | **Partially — mice lack the human Vδ2 lineage entirely** | LOW/MODERATE | — |
| **Impaired humoral immunity / reduced ABCs** | **FAILS TO RECAPITULATE the human outcome.** Mice have impaired humoral immunity; the human patient does not | **LOW** | PMID:35867801 |
| **IL-10 elevation on *M. tuberculosis* challenge** | Mouse-specific: *"T-bet(-/-) mice did not develop a fully polarized Th2 response toward M. tuberculosis, but exhibited selective elevation of IL-10 production"* — the human patient shows a **full Th2 skew**, not IL-10 elevation | **LOW — an outright divergence** | PMID:16177104 vs PMID:35909394 |

### Model limitations (curate these as `limitations` on `ModelMechanismLink`)

1. **Mice have no Vδ2⁺ γδ T cell lineage**, so the model cannot address one of the four human innate-like compartments lost in IMD88.
2. **The humoral phenotype does not translate.** Reduced ABCs + impaired humoral immunity in mouse vs. absent CD21^lo CD11c^hi B cells + *intact* humoral immunity in human. This is a genuine `FAILS_TO_RECAPITULATE` claim and — per the repo's rules — requires both `limitations` and `evidence`, both of which are available (PMID:35867801).
3. **The mycobacterial immunopathology diverges:** IL-10 elevation without full Th2 polarization in mouse vs. full Th2 skew in human.
4. **The mouse is a complete null; the human variant is an in-frame indel with residual (mislocalized, non-DNA-binding) protein.** Any residual non-DNA-binding function of T-bet — protein–protein interactions, for instance — would be present in the patient and absent in the KO. Untested.
5. **No model carries the human variant.** All mouse data are null-allele data.
6. Mouse infection studies use virulent *M. tuberculosis*; the human presentation was with attenuated BCG.

### Research applications

- Mechanism of NK/iNKT terminal maturation (mouse)
- TH1/TH2 reciprocal regulation (mouse + patient cells)
- T-bet-dependent chromatin programs (patient primary B cells + Omni-ATAC-seq — the human system is superior here)
- Preclinical testing of rhIFN-γ or type-2 biologics — **not yet done in any *Tbx21*⁻/⁻ mycobacterial model**

### Model databases

**MGI** (mouse; *Tbx21* MGI:1888984 — verify), **IMPC**, **IMSR**, **JAX**, **KOMP/EuMMCR/MMRRC**, **Alliance of Genome Resources**, **RGD** (rat), **Cellosaurus** (HEK293T, HVS-immortalized lines).

---

## Summary of Ontology Term Suggestions

**Disease:** `MONDO:0030483` immunodeficiency 88

**Gene:** `hgnc:11599` TBX21 *(lowercase prefix, per repo convention)*

**Phenotypes (HP):** `HP:0020087` BCGosis · `HP:0002099` Asthma · `HP:0001880` Increased total eosinophil count · `HP:0003593` Infantile onset · `HP:0000007` Autosomal recessive inheritance · `HP:0040218` Reduced total natural killer cell count · `HP:0003212` Increased circulating IgE concentration · `HP:0008348` Decreased circulating IgG2 concentration · `HP:0001433` Hepatosplenomegaly · `HP:0002716` Lymphadenopathy · `HP:0001945` Fever · `HP:0001824` Weight loss · `HP:0002257` Chronic rhinitis · `HP:0011274` Recurrent mycobacterial infections *(negative in this patient)*

**Cell types (CL):** `CL:0000623` natural killer cell · `CL:0000921` type I NK T cell · `CL:0000940` mucosal invariant T cell · `CL:0000798` gamma-delta T cell · `CL:0000545` T-helper 1 cell · `CL:0000624` CD4-positive, alpha-beta T cell · `CL:0000625` CD8-positive, alpha-beta T cell · `CL:0000236` B cell · `CL:0000771` eosinophil · `CL:0000235` macrophage · `CL:0000037` hematopoietic stem cell

**Biological processes (GO):** `GO:0045063` T-helper 1 cell differentiation · `GO:0032609` interferon-gamma production · `GO:0032729` positive regulation of type II interferon production · `GO:0045064` T-helper 2 cell differentiation · `GO:0042092` type 2 immune response · `GO:0030101` natural killer cell activation · `GO:0045190` isotype switching · `GO:0006338` chromatin remodeling · `GO:0071346` cellular response to interferon-gamma

**Molecular functions (GO):** `GO:0003700` DNA-binding transcription factor activity · `GO:0043565` sequence-specific DNA binding

**Cellular components (GO):** `GO:0005634` nucleus · `GO:0000785` chromatin

**Anatomy (UBERON):** `UBERON:0002390` hematopoietic system · `UBERON:0002371` bone marrow · `UBERON:0002370` thymus · `UBERON:0000029` lymph node · `UBERON:0002439` axillary lymph node · `UBERON:0002106` spleen · `UBERON:0002107` liver · `UBERON:0002097` skin · `UBERON:0001557` upper respiratory tract · `UBERON:0002185` bronchus

**Organisms (NCBITaxon):** `NCBITaxon:9606` Homo sapiens · `NCBITaxon:1765` Mycobacterium bovis · `NCBITaxon:1773` Mycobacterium tuberculosis · `NCBITaxon:10090` Mus musculus

**Treatments (NCIT):** `NCIT:C15986` Pharmacotherapy · `NCIT:C15431` Hematopoietic Cell Transplantation · `NCIT:C15329` Surgical Procedure · `NCIT:C15240` Genetic Counseling · `NCIT:C15747` Supportive Care · `NCIT:C20401` Monoclonal Antibody

**Every ontology ID above must be validated with `just validate-terms` before curation.** The HP, MONDO, and HGNC identifiers were resolved against authoritative APIs during this research; the CL, GO, UBERON, NCBITaxon, NCIT, and CHEBI suggestions are drawn from general knowledge and are **leads, not verified bindings**.

---

## Reference List (all PMIDs verified against PubMed; cached where noted)

| PMID | Citation | Evidence type | Cached |
|---|---|---|---|
| **33296702** | Yang R, Mele F, Worley L, … Casanova JL. **Human T-bet Governs Innate and Innate-like Adaptive IFN-γ Immunity against Mycobacteria.** *Cell*. 23 Dec 2020. doi:10.1016/j.cell.2020.10.046 — **THE INDEX PAPER** | HUMAN_CLINICAL | ✓ |
| **35909394** | Benhsaien I, Yang R, Ailal F, … Bousfiha A. **Chronic upper airway inflammation related to high Th2 cytokines in Mendelian susceptibility to mycobacterial disease case.** *Qatar Med J*. 2022. doi:10.5339/qmj.2022.fqac.24 | HUMAN_CLINICAL / IN_VITRO | ✓ |
| **35867801** | Yang R, Avery DT, Jackson KJL, … Tangye SG. **Human T-bet governs the generation of a distinct subset of CD11c^high^CD21^low^ B cells.** *Sci Immunol*. Jul 2022. doi:10.1126/sciimmunol.abq3277 | HUMAN_CLINICAL / IN_VITRO | ✓ (full text) |
| **36630059** | Errami A, El Baghdadi J, Ailal F, … Bousfiha AA. **MSMD: Clinical, Immunological, and Genetic Features of 22 Patients from 15 Moroccan Kindreds.** *J Clin Immunol*. 2023. doi:10.1007/s10875-022-01419-x | HUMAN_CLINICAL | ✓ (full text) |
| **41209815** | Refaat M, et al. **Defects in Innate and Intrinsic Immunity in Morocco: A Retrospective Analysis of the Genetic Landscape and Clinical Correlations.** *Pathog Immun*. Nov 2025 | HUMAN_CLINICAL | ✓ (full text) |
| **36326697** | Ogishi M, Yang R, Rodriguez R, … Casanova JL. **Inherited human ITK deficiency impairs IFN-γ immunity and underlies tuberculosis.** *J Exp Med*. 2 Jan 2023 — cited for MSMD gene taxonomy, ~1/50,000 prevalence, rhIFN-γ outcomes | HUMAN_CLINICAL | ✓ (full text) |
| **38535546** | **Diagnosis and Management of Infections in Patients with Mendelian Susceptibility to Mycobacterial Disease.** *Pathogens*. 2024 | Review | ✓ |
| **38025345** | Errami A, et al. **Mendelian susceptibility to mycobacterial diseases: State of the puzzle.** *Qatar Med J*. Nov 2023 | Review | ✓ |
| **35748970** | Tangye SG, et al. **Human Inborn Errors of Immunity: 2022 Update on the Classification from the IUIS Expert Committee.** *J Clin Immunol*. 2022 | Classification | ✓ |
| **11786643** | Finotto S, et al. **Development of spontaneous airway changes consistent with human asthma in mice lacking T-bet.** *Science*. 2002 | MODEL_ORGANISM | ✓ |
| **11786644** | Szabo SJ, et al. **Distinct effects of T-bet in TH1 lineage commitment and IFN-γ production in CD4 and CD8 T cells.** *Science*. 2002 | MODEL_ORGANISM | ✓ |
| **15084276** | Townsend MJ, et al. **T-bet regulates the terminal maturation and homeostasis of NK and Vα14i NKT cells.** *Immunity*. 2004 | MODEL_ORGANISM | ✓ |
| **16177104** | Sullivan BM, Jobe O, Lazarevic V, … Kramnik I. **Increased susceptibility of mice lacking T-bet to infection with *Mycobacterium tuberculosis* correlates with increased IL-10 and decreased IFN-γ production.** *J Immunol*. 2005 | MODEL_ORGANISM | ✓ |
| **39441153** | Fadil I, et al. **Phenotypes of 126 Moroccan HIES patients according to NIH Score.** — cited for the HIES differential in the same population | HUMAN_CLINICAL | ✓ |
| **37727514** | Vaseghi-Shanjani M, et al. **Transcription factor defects in inborn errors of immunity with atopy.** *Front Allergy*. Sep 2023 — contextual review for the type-2 arm | Review | — |
| **37942326** | **Preferential differential gene expression within the WC1.1+ γδ T cell compartment in cattle naturally infected with *Mycobacterium bovis*.** *Front Immunol*. Oct 2023 — comparative γδ biology | MODEL_ORGANISM | — |

**Non-PMID sources:** [OMIM #619630](https://omim.org/entry/619630) · [OMIM \*604895](https://omim.org/entry/604895) · [MedGen 1794236](https://www.ncbi.nlm.nih.gov/medgen/1794236) · [UniProt Q9UL17](https://rest.uniprot.org/uniprotkb/Q9UL17.txt) · [HGNC:11599](https://rest.genenames.org/fetch/symbol/TBX21) · [HPO annotations for OMIM:619630](https://ontology.jax.org/api/network/annotation/OMIM:619630) · [Orphanet ORPHA:748](https://www.orpha.net/en/disease/detail/748) · [GTR: Immunodeficiency 88](https://www.ncbi.nlm.nih.gov/gtr/conditions/C5562026/)

---

## Curation Notes and Open Gaps

**Highest-value things this report establishes for the KB entry:**

1. **Two mechanistically independent causal branches from one root node** — the IFN-γ/innate-lymphocyte collapse and the Th2 de-repression. PMID:35909394 states the dissociation in one sentence. Model them as separate `downstream` chains, not one.
2. **A genuine `FAILS_TO_RECAPITULATE` animal-model link** — the murine humoral phenotype does not translate. This requires `limitations` + `evidence`, both available.
3. **A textbook `HUMAN_MODEL_MISMATCH` discussion** on the mouse-vs-human B-cell/humoral divergence and the IL-10-vs-Th2 divergence in mycobacterial challenge.
4. **A complementation-rescue evidence item** (WT T-bet reverses the Th2 skew) — `directness: DIRECT`.

**Genuine gaps to record as `discussions` with `kind: KNOWLEDGE_GAP`:**
- Human IMD88 granuloma histopathology is uncharacterized.
- No proteomic, metabolomic, or immunometabolic profiling exists.
- rhIFN-γ has never been given to an IMD88 patient despite being the mechanistically indicated adjunct.
- Anti-IL-5/anti-IL-4Rα biologics are untried despite documented IL-5/IL-13 elevation.
- Penetrance is unestimable at n = 1; the "residual IFN-γ ⇒ incomplete penetrance" prediction is untested.
- No knock-in mouse carrying the human p.E156_M157delinsSL allele.

**One housekeeping item:** while chasing the mouse-model references I fetched two PMIDs that turned out to be misidentified (PMID:11934957 is a rheumatology sonography paper; PMID:15308104 is an IL-22 paper) — both irrelevant to this disease. The correct references are PMID:11786644 and PMID:15084276, both now cached and cited above. My attempt to delete the two stray cache files was blocked by the sandbox, so `references_cache/PMID_11934957.md` and `references_cache/PMID_15308104.md` are sitting untracked in the worktree. **Delete them before staging**, or they will end up in the PR.

**Next step:** if you want, I can turn this into the expanded `kb/disorders/Immunodeficiency_88.yaml` — the current stub has one pathophysiology node and one phenotype, and the full causal chain in §6a plus the phenotype table in §3 would populate it properly. Say the word and I'll draft it against the schema and run the validation loop.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 22 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 107 |
| Resolved | 97 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 10 |
| Terms whose name was checked | 36 |
| Terms named correctly | 19 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 15 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0002439` (2 mentions) - the report calls it "Axillary lymph node"; UBERON calls it **myenteric nerve plexus**
- `UBERON:0003950` (1 mention) - the report calls it "Abdominal/mesenteric lymph nodes"; UBERON calls it **inner ear canal**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0020087` (4 mentions) - the report calls it "BCGosis", "BCG-osis"; HP calls it **BCGosis**
- `HP:0003593` (5 mentions) - the report calls it "Infantile onset", "Infantile", "Age:** **Infantile"; HP calls it **Infantile onset**
- `HP:0002099` (4 mentions) - the report calls it "Asthma", "chronic upper airway inflammation and asthma/reactive airway disease"; HP calls it **Asthma**, and lists "Reactive airway disease" among its other names
- `HP:0001880` (5 mentions) - the report calls it "Increased total eosinophil count", "blood eosinophilia", "Eosinophilia"; HP calls it **Increased total eosinophil count**, and lists "Eosinophilia" among its other names
- `HP:0000007` (3 mentions) - the report calls it "Autosomal recessive inheritance", "Autosomal recessive"; HP calls it **Autosomal recessive inheritance**, and lists "Autosomal recessive" among its other names
- `NCBITaxon:1763` (1 mention) - the report calls it "Mycobacterium* genus"; NCBITaxon calls it **Mycobacterium**
- `NCBITaxon:28901` (1 mention) - the report calls it "Non-typhoidal *Salmonella enterica"; NCBITaxon calls it **Salmonella enterica**
- `CL:0000545` (3 mentions) - the report calls it "T-helper 1 cell (classic)"; CL calls it **T-helper 1 cell**
- `GO:0045063` (4 mentions) - the report calls it "TH1 differentiation program"; GO calls it **T-helper 1 cell differentiation**
- `CL:0000624` (3 mentions) - the report calls it "CD4⁺ αβ T cell"; CL calls it **CD4-positive, alpha-beta T cell**
- `GO:0045064` (3 mentions) - the report calls it "TH2 differentiation program"; GO calls it **T-helper 2 cell differentiation**
- `UBERON:0002097` (2 mentions) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `CL:0000824` (1 mention) - the report calls it "Mature NK cell"; CL calls it **mature natural killer cell**, and lists "mature NK cell" among its other names
- `CL:0000625` (2 mentions) - the report calls it "CD8⁺ αβ T cell"; CL calls it **CD8-positive, alpha-beta T cell**
- `NCBITaxon:9913` (1 mention) - the report calls it "Cattle"; NCBITaxon calls it **Bos taurus**, and lists "domestic cattle" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0020087` - called "BCGosis", "BCG-osis"
- `HP:0003593` - called "Infantile onset", "Infantile", "Age:** **Infantile"
- `HP:0002099` - called "Asthma", "chronic upper airway inflammation and asthma/reactive airway disease"
- `HP:0001880` - called "Increased total eosinophil count", "blood eosinophilia", "Eosinophilia"
- `HP:0000007` - called "Autosomal recessive inheritance", "Autosomal recessive"
- `GO:0005634` - called "nucleus", "Nucleus"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`, `LOINC`, `MGI`.