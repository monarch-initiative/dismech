---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-08T08:06:51.059671'
end_time: '2026-09-08T08:11:22.907391'
duration_seconds: 271.85
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hearing Loss Autosomal Recessive 100
  mondo_id: MONDO:0032740
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
  - claude-sonnet-5
  web_search_requests: 11
  num_turns: 21
  total_cost_usd: 1.263286
  session_id: 8e6a3453-99e0-563b-8e2c-3bcb30d1c949
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 10
reference_validation:
  total_references: 2
  verified: 2
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 2
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 16
  verified: 14
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 2
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0000998
    reported_labels:
    - Prelingual sensorineural hearing loss impairment
    ontology_label: Hypertrichosis
  labels_variant: 1
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hearing Loss Autosomal Recessive 100
- **MONDO ID:** MONDO:0032740 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hearing Loss Autosomal Recessive 100** covering all of the
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

I'll research DFNB100 (Autosomal Recessive Hearing Loss 100) using web search and fetch tools to build a comprehensive, well-cited report.

# Autosomal Recessive Deafness‑100 (DFNB100): Comprehensive Research Report

## 1. Disease Information

**Overview.** Autosomal recessive deafness‑100 (DFNB100) is an ultra-rare, monogenic form of prelingual, nonsyndromic sensorineural hearing loss caused by biallelic (homozygous) mutation of **PPIP5K2** (diphosphoinositol‑pentakisphosphate kinase 2) on chromosome 5q21.1. It was first — and to date only — described in two large, apparently unrelated consanguineous Pakistani families (PKDF041 and PKDF751) from Punjab province, comprising 12 affected individuals, in a 2018 *PLOS Genetics* report by Yousaf et al. ([PMID:29590114](https://pubmed.ncbi.nlm.nih.gov/29590114/); [PLOS Genetics 14(3):e1007297](https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1007297)). No independent replication family has been published in the subsequent literature search window (through 2024), consistent with DFNB100 being one of the rarest of the >100 numbered DFNB loci.

**Key identifiers:**
- **OMIM (phenotype):** [#618422](https://omim.org/entry/618422) — DEAFNESS, AUTOSOMAL RECESSIVE 100; DFNB100
- **OMIM (gene):** [*611648](https://omim.org/entry/611648) — DIPHOSPHOINOSITOL PENTAKISPHOSPHATE KINASE 2; PPIP5K2
- **MONDO:** MONDO:0032740
- **MedGen:** [C5193087 / UID 1682525](https://www.ncbi.nlm.nih.gov/medgen/1682525)
- **Gene symbol / HGNC:** PPIP5K2 (HGNC:29035); NCBI Gene ID 23262; also historically known as **VIP2** / **IHPK2**
- **Locus:** 5q21.1 (within the broader linkage interval 5q12.2–q23.3 in family PKDF751)
- **Orphanet umbrella term:** ORPHA:90636 (Autosomal recessive nonsyndromic sensorineural deafness type DFNB — the generic Orphanet grouping under which locus-specific DFNB forms including DFNB100 fall; there is no DFNB100-dedicated ORPHA code identified in this search)
- **Inheritance:** Autosomal recessive (HP mode-of-inheritance term HP:0000007)

**Synonyms:** "Deafness, autosomal recessive 100"; "DFNB100"; "Hearing loss, autosomal recessive 100." The gene itself is also referenced in older literature as IHPK2/VIP2.

**Evidence source note:** All clinical data derive from a single published aggregated case series (two extended pedigrees, not individual EHR records); the genetic/functional data derive from human genetics plus a purpose-built mouse model, i.e., a mixed HUMAN_CLINICAL + MODEL_ORGANISM + IN_VITRO/COMPUTATIONAL evidence base from one primary study.

---

## 2. Etiology

**Disease Causal Factor — genetic, monogenic, single reported variant.** DFNB100 is caused by a homozygous missense variant in *PPIP5K2*:

- **Variant:** c.2510G>A (exon 21), predicting **p.Arg837His (R837H)**, in the phosphatase domain of PPIP5K2.
- The paper states: *"The c.2510G>A transition variant is predicted to substitute a highly invariant arginine residue with histidine (p.Arg837His)"* (PMID:29590114).
- The variant segregated with hearing loss in **both** unrelated Pakistani families under a recessive model, was **absent from 180 ethnically matched Pakistani control chromosomes**, was absent from the 1000 Genomes Project, and was present at low frequency (**0.000146**) in ExAC — consistent with a rare, pathogenic recessive allele rather than a common polymorphism (PMID:29590114).
- ClinVar accessions reported for this variant include **RCV000770902** and **RCV003238202** (per aggregator search; not independently verified against a live ClinVar page in this session — treat as a lead requiring confirmation via `just fetch-reference` against ClinVar directly before KB citation).
- Arg837 is described as evolutionarily invariant across vertebrate orthologs, and in silico prediction tools supported deleteriousness (per the paper's variant-pathogenicity evidence chain, alongside segregation, absence from controls, biochemical functional data, and mouse recapitulation).

**Risk factors:**
- **Genetic:** Homozygosity for the PPIP5K2 R837H allele; parental consanguinity, which is the mechanism by which both reported families became homozygous for an otherwise rare allele (both families are described as consanguineous).
- **Founder/population context:** Both index families are Pakistani (Punjab); whether R837H represents a regional founder allele versus recurrent independent mutation is not established by the available literature — this should be flagged as an open question rather than asserted.
- No other causal or modifier genes for DFNB100 specifically have been reported.
- **Environmental risk factors:** None identified as relevant to DFNB100 causation; nonsyndromic nature and cosegregation strongly indicate the genetic lesion is fully sufficient in the reported pedigrees (i.e., this is not a gene–environment or multifactorial deafness form like some other DFNB loci or aminoglycoside-potentiated forms, e.g., MT-RNR1).

**Protective factors:** None reported specific to DFNB100 in the literature identified.

**Gene–environment interactions:** None described for DFNB100. (This contrasts with mitochondrial DFNB forms driven by aminoglycoside exposure — not applicable here.)

---

## 3. Phenotypes

**Primary phenotype — profound congenital sensorineural hearing loss.**

- **Type:** Clinical sign / audiometric finding (sensorineural hearing loss), nonsyndromic (isolated).
- **Onset:** Prelingual — *"no hearing was reported since birth in all affected individuals"* — i.e., congenital onset (PMID:29590114).
- **Severity:** Severe-to-profound; audiometric testing showed *"profound HL in both ears"* across the tested frequency range.
- **Laterality:** Bilateral, symmetric.
- **Progression:** In the human pedigrees as reported, the phenotype is described at presentation as profound/prelingual without a documented longitudinal progression curve in probands (contrast with the mouse model, which shows late-onset progressive loss — see Mechanism/Model Organisms below). This is an important cross-species discrepancy the authors themselves flag.
- **Frequency among affected individuals:** 12/12 affected individuals across the two families presented with this core phenotype (fully penetrant in the reported pedigrees).

**Otologic / audiologic functional testing:**
- **Otoacoustic emissions:** Three affected individuals failed transient evoked otoacoustic emission (TEOAE) testing, *"indicative of defective outer hair cell function"* — directly implicating cochlear outer hair cells (OHCs) as the primary lesion site, consistent with the mouse histopathology (below).
- **Vestibular testing:** Romberg and tandem gait testing were normal — *"did not reveal any overt vestibular dysfunction"* — despite PPIP5K2 also being expressed in vestibular sensory hair cells, indicating a cochlea-selective functional vulnerability in humans.
- **Ophthalmologic screening:** Normal funduscopy and electroretinography, excluding a Usher-syndrome-like retinal component and supporting the "nonsyndromic" classification.

**Quality of life impact:** Not formally quantified in the primary literature (no EQ-5D/SF-36 or disease-specific QOL instrument reported for this cohort); general inference from profound prelingual deafness (impact on spoken-language acquisition, need for early intervention) is standard for this phenotype class but not DFNB100-specific data.

**Suggested HPO terms:**
| Phenotype | Candidate HPO term |
|---|---|
| Profound bilateral sensorineural hearing loss | HP:0008625 (Sensorineural hearing loss, severe) / consider HP:0001363-adjacent profound-tier term; verify exact profound-tier CURIE via `dismech-terms` before binding |
| Congenital/prelingual onset | HP:0000998 (Prelingual sensorineural hearing loss impairment) — verify exact label match |
| Absent otoacoustic emissions / OHC dysfunction | Consider free-text qualifier if no precise HP term exists; note as a functional-test finding rather than a distinct phenotype node |
| Normal vestibular function (negative finding) | Document as an excluded/negative finding rather than a phenotype node |
| Normal fundus/retina (negative finding) | Document as an excluded/negative finding — supports nonsyndromic classification |

(Per dismech convention, these are leads for the `dismech-terms` skill to verify exact canonical labels/CURIEs before binding — not pre-verified bindings.)

---

## 4. Genetic/Molecular Information

**Causal gene:** PPIP5K2 (HGNC:29035; NCBI Gene 23262; OMIM *611648; UniProt O43314).

**Pathogenic variant details:**
- **Genomic/cDNA change:** c.2510G>A, exon 21
- **Protein change:** p.Arg837His (p.R837H)
- **Variant class:** Missense
- **Zygosity in affected individuals:** Homozygous (biallelic, consistent with consanguinity)
- **Population frequency:** Absent in 180 Pakistani controls and in 1000 Genomes; **0.000146** in ExAC (i.e., ultra-rare, sub-population-level frequency consistent with a rare recessive pathogenic allele)
- **Functional impact category:** The paper's biochemical assays support a mixed/altered-function mechanism rather than simple loss-of-function — see Mechanism section — recorded findings: **~21% decrease in phosphatase activity** and **increased kinase activity**, together yielding **~60% higher IP8 levels** relative to wild-type protein in in vitro assays. This pattern (partial loss of one catalytic activity + gain/elevation of the paired activity, net pathway output shifted) should be curated carefully against the `functional_impact_category` enum — it does not map cleanly to simple LOF or simple GOF and may be best captured descriptively (e.g., partial loss of phosphatase function with consequent kinase/product imbalance) rather than forcing a single enum value; flag for curator judgment.
- **gnomAD constraint metrics (pLI/LOEUF)** for PPIP5K2: not retrievable in this session (gnomAD browser is JavaScript-rendered and did not return data via automated fetch) — this should be looked up directly in the gnomAD browser (gene ENSG00000145725) during curation rather than asserted here.

**Modifier genes:** None identified specific to DFNB100. Notably, in the *mouse* model, a compensatory **~3-fold upregulation of the paralog Ppip5k1** transcript was observed in the inner ear of homozygous mutants at P150 (qPCR finding), suggesting Ppip5k1 may act as a partial genetic modifier/buffer in mice — a candidate hypothesis for why the mouse phenotype is milder and later-onset than the human phenotype, but this has not been tested as a human modifier.

**Epigenetic information:** None reported for DFNB100/PPIP5K2.

**Chromosomal abnormalities:** Not applicable — this is a point-mutation (missense) disorder, not a copy-number/structural disorder. Linkage mapping in family PKDF751 defined a large homozygous interval at chromosome **5q12.2–q23.3**, narrowed by exome sequencing to the single PPIP5K2 variant.

**Protein domain architecture:** PPIP5K2 is a bifunctional enzyme with (1) an N-terminal kinase domain, (2) a phosphatase (histidine acid phosphatase-like) domain, and (3) an intrinsically disordered C-terminal region mediating protein–protein interactions. Arg837 lies within the phosphatase domain.

---

## 5. Environmental Information

No environmental, infectious, or lifestyle contributing factors have been reported for DFNB100. As a fully penetrant monogenic recessive disorder identified in consanguineous pedigrees with segregation-confirmed causation, there is no literature suggesting an environmental co-factor is required for phenotype expression. (This is an appropriate case for an environmental-evidence waiver in `environmental[]` curation, if that section is populated at all, per the `check-environmental-evidence` policy — searched, and nothing quotable was found beyond "no other cause identified.")

---

## 6. Mechanism / Pathophysiology

**Causal chain (numbered, from initiating lesion to clinical manifestation):**

1. Biallelic PPIP5K2 c.2510G>A (p.Arg837His) **leads to** a phosphatase-domain missense substitution at an evolutionarily invariant residue.
2. This substitution **results in** altered catalytic balance of the bifunctional PPIP5K2 enzyme: **reduced phosphatase activity (~21% decrease)** combined with **increased kinase activity**, demonstrated biochemically in vitro (PMID:29590114).
3. The altered kinase/phosphatase balance **leads to** a shift in the interconversion of the paired inositol pyrophosphate signaling messengers **5-IP7 ⇌ IP8**, with the mutant protein producing **~60% higher IP8 levels** than wild-type protein in matched in vitro assays. *(Inferred mechanistic link — demonstrated biochemically for isolated enzyme activity; the causal step from altered IP7/IP8 ratio to downstream cellular consequence is inferred by analogy to known IP7/IP8 signaling roles rather than directly measured in patient/model cochlear tissue.)*
4. Perturbed inositol pyrophosphate signaling **is expected to disrupt** PP-IP-dependent cellular processes that the pathway is broadly known to govern — **endocytosis, vesicle trafficking, apoptosis, and bioenergetic/insulin-secretion homeostasis** — within cells that depend on this signaling for normal function. *(This step is inferred from general PP-IP biology rather than cochlea-specific mechanistic dissection; the paper does not isolate which specific downstream process is causal in hair cells.)*
5. In the cochlea specifically, where PPIP5K2 is expressed in **sensory hair cells, supporting cells, and spiral ganglion neurons** (confirmed by immunostaining, including all three layers of the stria vascularis — marginal, intermediate, and basal cells), this disruption **selectively compromises outer hair cell (OHC) maintenance/survival** rather than inner hair cells, spiral ganglion neurons, or the stria vascularis.
6. OHC compromise **manifests functionally** as **absent/failed transient evoked otoacoustic emissions** in affected humans (direct evidence of OHC dysfunction) and, in the mouse model, as **histologically confirmed degeneration of OHCs in the cochlear basal turn** (statistically significant reduction, p<0.01) with inner hair cells spared and no spiral ganglion or stria vascularis degeneration.
7. OHC loss/dysfunction **leads to** elevated auditory brainstem response (ABR) thresholds, manifesting first and most severely at **high frequencies (24 and 32 kHz in mice, p<0.001)**, consistent with basal-turn (high-frequency-coding) OHC vulnerability, and **culminates in** the clinical phenotype of severe-to-profound bilateral sensorineural hearing loss.

**Branch point / species discrepancy (explicitly flagged by the study authors):** In humans, the phenotype presents as **prelingual/congenital** profound loss; in the *Ppip5k2* gene-trap mouse, the loss is **late-onset and progressive** (thresholds normal through ~P60, becoming significantly elevated by ~P90–P150) and **milder** in degree than the human phenotype. The authors explicitly attribute this to likely **"greater functional redundancy" in mice**, plausibly via the ~3-fold compensatory upregulation of the paralogous gene *Ppip5k1* observed in mutant mouse inner ear — an unresolved cross-species fidelity question (a candidate `HUMAN_MODEL_MISMATCH` consideration for KB curation, since the model does not fully recapitulate onset timing or severity, though it does recapitulate cell-type specificity and general pathway involvement).

**Molecular pathway:** Inositol pyrophosphate (PP-IP) signaling — synthesis/interconversion of 5-IP7 and IP8 by the PPIP5K (VIP1/VIP2 family) enzymes, acting together with IP6 kinases (IP6Ks) upstream in the pathway. This is a comparatively unusual pathway for a hearing-loss gene relative to the canonical DFNB mechanisms (cytoskeletal/stereocilia structural proteins, gap-junction connexins, ion-channel/transporter genes); PPIP5K2 represents an intracellular small-molecule-signaling mechanism rather than a structural or classical channel/transporter mechanism.

**Cellular processes implicated (general PP-IP biology, not cochlea-proven):** endocytosis, vesicle trafficking, apoptosis regulation, exocytosis/secretion (e.g., insulin secretion in other tissues), cytoskeletal dynamics, and bioenergetic homeostasis.

**Cell types involved:**
- Cochlear outer hair cells (primary lesion site) — candidate CL term: CL:0002095 (outer hair cell of Corti) — verify exact CURIE via `dismech-terms`.
- Cochlear supporting cells and spiral ganglion neurons (express PPIP5K2, not shown to degenerate in the mouse model).
- Vestibular sensory hair cells (express PPIP5K2; functionally spared in humans per Romberg/tandem-gait testing).
- Stria vascularis (marginal, intermediate, basal cells; PPIP5K2-immunoreactive but not degenerated).

**Suggested GO terms (leads, to be verified):**
- GO:0043647 (inositol phosphate metabolic process) or a more specific PP-IP interconversion term if one exists
- GO:0007605 (sensory perception of sound) — phenotype-level
- Hair-cell maintenance/homeostasis GO terms if available

**Molecular profiling data:** Real-time qPCR (targeted, not genome-wide RNA-seq) showing ~3-fold *Ppip5k1* upregulation in mutant mouse inner ear at P150; broader transcriptome analysis (cited but not detailed in the extracted text) supporting *Ppip5k2* as the dominant *Ppip5k* paralog expressed in cochlear/vestibular hair cells. No proteomic, metabolomic, lipidomic, single-cell, or spatial transcriptomic datasets specific to DFNB100/PPIP5K2 cochlear pathology were identified in this search.

---

## 7. Anatomical Structures Affected

- **Organ level:** Inner ear (cochlea primarily; vestibular labyrinth anatomically involved by gene expression but not functionally affected). No other organ systems are involved — consistent with the "nonsyndromic" designation (normal retina/fundus, normal gait/balance).
- **Tissue/cell level:** Organ of Corti — specifically outer hair cells (primary degeneration target); supporting cells, spiral ganglion neurons, and stria vascularis (all express the gene but show no demonstrated degeneration).
- **Subcellular level:** PPIP5K2 is a cytosolic/cytoplasmic enzyme, also associated with intracellular membrane-bound organelles consistent with its roles in vesicle trafficking; relevant GO Cellular Component terms would include cytosol/cytoplasm annotations (verify exact CURIEs).
- **Localization:** Bilateral, symmetric cochlear (and by expression pattern, vestibular) involvement; within the cochlea, the mouse histopathology localizes degeneration specifically to the **basal turn** (high-frequency-coding region), correlating with the high-frequency-predominant ABR threshold elevation.

Candidate UBERON terms: cochlea, organ of Corti, outer hair cell region/basal turn, spiral ganglion, stria vascularis, vestibular apparatus — to be resolved to exact CURIEs during curation.

---

## 8. Temporal Development

- **Onset (human):** Congenital/prelingual — "no hearing... since birth" in all affected individuals; this places DFNB100 in the congenital-onset, nonprogressive-by-report category in humans, though formal longitudinal audiometric follow-up data documenting stability versus progression over time were not described in the primary report.
- **Onset (mouse model):** Late-onset relative to the animal's lifespan — thresholds are essentially unremarkable through ~P60, become statistically significantly elevated at 32 kHz by ~P90, and extend to 24 kHz involvement by P120–P150, with progressive worsening across this window.
- **Progression:** In mice, clearly progressive (worsening thresholds and expanding frequency range of involvement with age). In humans, the published cohort was characterized cross-sectionally as profound/prelingual without a documented progression timeline; whether human hearing loss is present at birth in full severity or represents rapid early progression to profound levels is not resolved by the available data.
- **Critical periods:** As with all forms of prelingual profound deafness, early identification (e.g., via newborn hearing screening) and early intervention are clinically critical for language-outcome reasons, though this is a generic inference for the phenotype class rather than DFNB100-specific outcome data.

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal recessive, confirmed by segregation analysis in two independent consanguineous pedigrees under a strict recessive model (heterozygous carriers unaffected).
- **Penetrance:** Complete/full in the 12 reported affected homozygotes (no reported subclinical or unaffected homozygotes).
- **Expressivity:** Reported as consistent (profound, bilateral) across affected individuals in both families, based on the available description; formal variable-expressivity analysis was not performed.
- **Consanguinity:** Central to disease ascertainment — both families are explicitly consanguineous, which is the mechanism enabling homozygosity for this rare allele; this is characteristic of many DFNB loci discovered in South Asian and Middle Eastern consanguineous cohorts.
- **Founder effect:** Not established; both families are Pakistani (Punjab), raising the possibility of a shared regional founder allele, but haplotype-sharing analysis to formally test this was not reported in the material reviewed.
- **Carrier frequency:** Not directly reported; the ExAC frequency of 0.000146 for the pathogenic allele is the only population-frequency data point available, and translating this into a carrier-frequency estimate for any specific population would require formal population-genetics analysis not present in the source.
- **Epidemiology:** DFNB100 is exceptionally rare — to date reported in only 2 families (12 affected individuals) worldwide in the published literature identified by this search, with no independent replication cohorts found in a 2020–2024 literature sweep. No formal prevalence or incidence estimate exists; it should be treated as an ultra-rare/"cases in literature" measure type rather than assigned a population-prevalence band.
- **Geographic distribution:** Punjab province, Pakistan (both reported families); no data on occurrence elsewhere.
- **Sex ratio / age distribution:** Not specifically reported as differing from 1:1 or from other recessive nonsyndromic deafness loci; no sex-specific susceptibility is suggested by an autosomal recessive mechanism.

**Broader context (not DFNB100-specific but relevant framing):** Autosomal recessive nonsyndromic hearing loss (ARNSHL) as a class is a major cause of prelingual deafness worldwide, and GJB2 (DFNB1A) is by far the most common cause; DFNB100 represents one of the more obscure entries among >100 recognized DFNB loci and, per available literature, remains a private/founder-restricted cause rather than a globally recurrent one.

---

## 10. Diagnostics

- **Audiometric/functional testing:** Pure-tone audiometry (documenting bilateral severe-to-profound sensorineural loss), transient evoked otoacoustic emissions (TEOAE — abnormal/absent in DFNB100, reflecting OHC dysfunction), and vestibular functional testing (Romberg, tandem gait — normal in reported cases) were the diagnostic modalities used in the original description. No ABR, DPOAE, or imaging (temporal bone CT/MRI) findings for the human cohort were reported in the material reviewed.
- **Ophthalmologic screening:** Funduscopy and electroretinography were used to exclude a syndromic (Usher-like) retinal component — both normal, supporting nonsyndromic classification. This is a standard part of the differential diagnosis workup for profound congenital SNHL (ruling out Usher syndrome type 1, which also presents with profound congenital deafness plus vestibular areflexia and later retinitis pigmentosa — note DFNB100 is distinguished from Usher type 1 by its *normal* vestibular function).
- **Genetic testing:** The causal variant was identified via genome-wide linkage/homozygosity mapping (STR markers) followed by exome capture and massively parallel sequencing (whole-exome sequencing) in the index families — this remains the appropriate diagnostic strategy for a suspected DFNB-locus disorder in a consanguineous pedigree without a known familial mutation. Given how recently and narrowly PPIP5K2 has been implicated, it is unlikely to be included on all commercial hearing-loss gene panels; comprehensive panel or exome-based testing would be more reliable than a targeted single-gene test for a first diagnostic workup, with PPIP5K2 as one of many genes on a broad ARNSHL panel/exome reanalysis pipeline once a specific hypothesis is raised.
- **Differential diagnosis:** Other nonsyndromic DFNB loci (especially DFNB1A/GJB2, the most common cause), and syndromic profound congenital SNHL — particularly Usher syndrome type 1 (distinguished by vestibular areflexia, present in Usher but absent in DFNB100) and Pendred syndrome (distinguished by goiter/enlarged vestibular aqueduct).
- **Newborn/population screening:** No DFNB100-specific screening protocol exists; standard universal newborn hearing screening (e.g., via OAE/ABR) would detect the phenotype non-specifically as with any congenital profound SNHL, with genetic confirmation required afterward.

---

## 11. Outcome/Prognosis

- **Severity/stability:** The human phenotype is profound and, as reported, present from birth; no data on natural history, hearing aid/cochlear implant outcomes, or long-term morbidity specific to DFNB100 patients were available in this search.
- **Life expectancy/mortality:** Not applicable — nonsyndromic hearing loss of this type does not carry an independent mortality risk; no systemic organ involvement was identified.
- **Functional/QOL outcomes:** Not formally studied for this specific cohort; general expectations for profound prelingual SNHL apply (need for early amplification/cochlear implantation and language intervention to optimize communication outcomes), but this is inferred from the general disease class, not DFNB100-specific data.
- **Prognostic biomarkers:** None identified.

---

## 12. Treatment

No DFNB100-specific treatment trials, gene therapy programs, or pharmacological interventions have been reported. Management would follow standard-of-care for profound congenital sensorineural hearing loss:

- **Amplification/hearing aids** — for residual hearing, though profound loss often limits benefit.
- **Cochlear implantation** — the standard intervention for profound bilateral congenital SNHL when amplification is insufficient (NCIT term candidates: cochlear implantation procedure — bind the surgical action term per the CLAUDE.md guidance on device-vs-action terms, e.g., `NCIT:C15329` Surgical Procedure with a `qualifiers` predicate-value pair for the cochlear implant device, `NCIT:C157820`).
- **Genetic counseling** — appropriate given confirmed autosomal recessive inheritance and consanguinity in the reported families (candidate term `NCIT:C15240`, Genetic Counseling).
- **Speech-language/auditory-verbal therapy** — standard supportive intervention for pediatric profound SNHL (candidate `NCIT:C159273`, Speech Therapy, or `NCIT:C15747`, Supportive Care).

No pharmacotherapy, gene therapy, or RNA-based therapeutic specific to PPIP5K2/DFNB100 was found in the ClinicalTrials.gov or literature search conducted. There is no mechanistic rationale currently published for a targeted PP-IP-pathway-modulating drug in this disorder.

---

## 13. Prevention

- **Primary prevention:** Genetic counseling for consanguineous couples/families with a known PPIP5K2 pathogenic allele; carrier testing where familial mutation status is known.
- **Secondary prevention/early detection:** Universal newborn hearing screening (non-specific to DFNB100, standard practice) enabling early diagnosis and intervention.
- **Prenatal/preimplantation options:** Standard reproductive genetic counseling options (prenatal diagnosis, preimplantation genetic testing) would be applicable once a familial pathogenic variant is confirmed, as for any characterized autosomal recessive disorder, though no DFNB100-specific literature on uptake or outcomes was found.
- **Public health relevance:** Given the extreme rarity (2 families reported to date), DFNB100 is not a target of population-level carrier screening programs; it would only become clinically actionable within an identified family or population subgroup where the allele is known to segregate.

No immunization, prophylaxis, or environmental-intervention strategies apply, as this is a purely genetic, non-infectious, non-environmentally-modulated disorder.

---

## 14. Other Species / Natural Disease

No naturally occurring PPIP5K2-associated deafness has been reported in companion animals, livestock, or wildlife (no OMIA entry identified in this search). All non-human data derive from a **purpose-engineered laboratory mouse model** (see Section 15) rather than natural disease in another species. No zoonotic or cross-species transmission considerations apply, as this is a non-infectious monogenic disorder.

**Orthology:** The mouse ortholog is *Ppip5k2* (NCBI Gene, MGI); the paralog *Ppip5k1* is present in both human and mouse genomes and was noted as compensatorily upregulated in the mouse model's inner ear, a comparative-biology finding of potential relevance to understanding incomplete model penetrance/severity.

---

## 15. Model Organisms

**Primary and (currently) only reported model: mouse (*Mus musculus*), NCBITaxon:10090.**

- **Model type:** Genetically engineered, targeted gene-trap mouse line.
- **Strain/allele:** **B6N(Cg)-Ppip5k2^tm1a(EUCOMM)Wtsi^/J**, generated from a EUCOMM/KOMP gene-trap embryonic stem cell resource. The gene-trap cassette is inserted downstream of exon 13, producing a truncated protein that retains an intact kinase domain but a phosphatase domain truncated to only 84 residues — insufficient for phosphatase catalytic activity. This models a phosphatase-domain-selective loss rather than a precise knock-in of the human R837H missense allele (an important fidelity caveat: the mouse models phosphatase-domain disruption broadly, not the exact human variant/mechanism of altered kinase/phosphatase balance).
- **Phenotype recapitulation:**
  - **Recapitulates:** Cell-type-selective cochlear outer hair cell degeneration (basal turn, statistically significant, p<0.01), elevated ABR thresholds with high-frequency predominance (24–32 kHz, p<0.001), sparing of inner hair cells, spiral ganglion, and stria vascularis — broadly consistent with the human OTOAE-based inference of selective OHC dysfunction.
  - **Does not fully recapitulate:** Onset timing (mouse: late-onset/progressive from ~P90–P150; human: congenital/prelingual) and overall severity (mouse: milder than human). Authors explicitly attribute this divergence to likely greater functional redundancy in mice (candidate ~3-fold compensatory *Ppip5k1* upregulation).
  - This divergence is a strong candidate for `HUMAN_MODEL_MISMATCH` discussion-kind curation in a dismech entry: the model provides good cell-type/mechanistic-target validation (fidelity: MODERATE for OHC degeneration and pathway involvement) but poor validity for modeling onset timing/severity (fidelity: LOW for that specific claim), which should be recorded as separate `modeled_mechanisms` links with distinct `fidelity`/`limitations` per node rather than a single blanket fidelity rating.
- **Applications:** The model was used to (1) confirm PPIP5K2 expression pattern in cochlear/vestibular sensory epithelium and neurons via immunostaining, (2) demonstrate that phosphatase-domain loss is sufficient to cause OHC-selective degeneration and hearing loss in vivo, and (3) generate a hypothesis (Ppip5k1 compensation) for the human–mouse severity/onset discrepancy.
- **Resources:** Strain originates from the EUCOMM/KOMP international knockout mouse consortium resources (accessible via IMSR/MGI for strain sourcing); specific MGI allele accession was not independently confirmed in this session and should be verified directly against MGI before citing a specific MGI ID.

**No other model organism data** (zebrafish, *Drosophila*, *C. elegans*, yeast, cell lines/organoids, iPSC-derived models) were identified for PPIP5K2-related hearing loss in this search; the mouse gene-trap model represents the sole reported in vivo model system for this gene–phenotype relationship.

---

## Summary of Evidence Source Classification for Curation

| Claim | Evidence source | Basis |
|---|---|---|
| Human phenotype (audiometry, TEOAE, vestibular/fundus exam) | HUMAN_CLINICAL | Direct patient observations, PMID:29590114 |
| Variant segregation, population frequency (ExAC, 1000G, Pakistani controls) | HUMAN_CLINICAL | Genetic epidemiology within the same study |
| Biochemical kinase/phosphatase activity assays, IP7/IP8 quantification | IN_VITRO | Purified/recombinant enzyme assays |
| Mouse ABR thresholds, cochlear histology, qPCR expression | MODEL_ORGANISM | *Ppip5k2* gene-trap mouse, same study |
| In silico conservation/pathogenicity prediction of Arg837 | COMPUTATIONAL | Noted but not detailed in extracted text |

**Single-source caveat:** Nearly the entirety of the DFNB100/PPIP5K2 evidence base traces to one primary publication (Yousaf et al. 2018, PMID:29590114). No independent replication family, no independent functional-validation study, and no gnomAD-verified constraint data were retrievable in this session. Any dismech curation should flag this as a thin, single-study evidence base rather than a broadly replicated gene-disease relationship, and should independently verify the ClinVar accessions and gnomAD constraint metrics before quoting them as established facts, since those specific figures were obtained via search-engine synthesis rather than direct primary-source fetch in this session.

---

## Sources

- [OMIM #618422 — DEAFNESS, AUTOSOMAL RECESSIVE 100; DFNB100](https://omim.org/entry/618422)
- [OMIM *611648 — PPIP5K2](https://omim.org/entry/611648)
- [Yousaf R, et al. Mutations in Diphosphoinositol-Pentakisphosphate Kinase PPIP5K2 are associated with hearing loss in human and mouse. PLOS Genetics. 2018;14(3):e1007297.](https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1007297) — [PMID:29590114](https://pubmed.ncbi.nlm.nih.gov/29590114/) — [PMC5891075](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5891075/)
- [MedGen — Hearing loss, autosomal recessive 100 (C5193087 / UID 1682525)](https://www.ncbi.nlm.nih.gov/medgen/1682525)
- [PPIP5K2 Gene — GeneCards](https://www.genecards.org/card/PPIP5K2)
- [PPIP5K2 — NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/23262)
- [Gene: PPIP5K2 (Monogenic hearing loss) — Genomics England PanelApp](https://panelapp.genomicsengland.co.uk/panels/126/gene/PPIP5K2/)
- [OMIM Clinical Synopsis — #618422](https://omim.org/clinicalSynopsis/618422)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 2 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 16 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 4 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000998` (1 mention) - the report calls it "Prelingual sensorineural hearing loss impairment"; HP calls it **Hypertrichosis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0002095` (1 mention) - the report calls it "outer hair cell of Corti"; CL calls it **hilus cell of ovary**, and lists "hilar cell of ovary" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.