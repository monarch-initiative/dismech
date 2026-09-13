---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-04T01:53:15.341912'
end_time: '2026-09-04T01:57:36.220515'
duration_seconds: 260.88
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spermatogenic Failure 18
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
  - claude-sonnet-5
  web_search_requests: 18
  num_turns: 21
  total_cost_usd: 1.3240573999999998
  session_id: 1d4c83ee-98b8-54c2-892b-3815ba752722
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 1
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 18
  verified: 15
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 2
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0034424
    reported_labels:
    - 100% (defining feature); "mosaic" pattern rather than a single uniform defect
    ontology_label: Clicking tinnitus
  - term_id: HP:0008734
    reported_labels:
    - Severe to complete; variable between families/genotypes
    ontology_label: Decreased testicular size
  labels_variant: 1
  unresolvable_prefixes:
  - Taxon
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic Failure 18
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 18** covering all of the
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

I have enough material now to compile a comprehensive, well-cited report. Here it is.

# Spermatogenic Failure 18 (SPGF18) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Spermatogenic Failure 18 (SPGF18; OMIM #617576) is a monogenic, autosomal recessive form of male infertility caused by biallelic (homozygous or compound heterozygous) mutation of **DNAH1** (Dynein Axonemal Heavy Chain 1; HGNC:2940; chromosome 3p21.1), which encodes an inner dynein arm heavy chain of the sperm flagellar axoneme. SPGF18 is the prototype genetic cause of **multiple morphological abnormalities of the sperm flagella (MMAF)**, a clinical/histological entity first formally defined in the disease-founding paper:

> Ben Khelifa M, Coutton C, Zouari R, et al. "Mutations in DNAH1, which Encodes an Inner Arm Heavy Chain Dynein, Lead to Male Infertility from Multiple Morphological Abnormalities of the Sperm Flagella." *American Journal of Human Genetics* 2014;94(1):95-104. **PMID: 24360805**.

Affected men are phenotypically normal apart from primary infertility; ejaculated spermatozoa show a heterogeneous ("mosaic") mixture of **absent, short, coiled, bent, and irregular-caliber flagella**, producing severe asthenozoospermia (near-total or total immotility) combined with teratozoospermia (asthenoteratozoospermia).

**Key identifiers:**
- **OMIM:** #617576 (SPERMATOGENIC FAILURE 18; SPGF18), part of the Spermatogenic Failure phenotypic series PS258150
- **Gene/locus OMIM:** *603332 (DNAH1), 3p21.1
- **Related but distinct OMIM entry:** #617577 — Ciliary Dyskinesia, Primary, 37 (CILD37), also caused by biallelic DNAH1 mutation but presenting as a respiratory ciliopathy rather than isolated infertility (see §5/§9 for the allelic-disorder distinction)
- **MalaCards:** "Spermatogenic Failure 18" (https://www.malacards.org/card/spermatogenic_failure_18)
- **HGNC:** DNAH1, HGNC:2940
- **Suggested MONDO/HPO framing:** HP:0034424 "Multiple morphological abnormalities of the sperm flagella"; HP:0008734 "Asthenozoospermia"; the disease is best represented in MONDO as a DNAH1-specific subtype within the broader MMAF/spermatogenic-failure disease family
- **Synonyms:** "DNAH1-related MMAF," "Spermatogenic failure due to multiple morphological abnormalities of the sperm flagella," "MMAF1" (informal literature usage)

**Evidence basis.** Nearly all published data on SPGF18 derive from **aggregated clinical/genetic cohort studies** of infertile men (exome/panel sequencing, semen analysis, electron microscopy), not individual case-report EHR data — i.e., disease-level knowledge assembled from multiple consanguineous and sporadic families across North African, Middle Eastern, and East Asian cohorts, supplemented by a mouse (*Dnah1*) knockout model.

---

## 2. Etiology

**Primary cause:** Biallelic loss-of-function or missense mutation in **DNAH1** is necessary and sufficient to cause SPGF18; there is no reported environmental or infectious trigger — this is a purely Mendelian, structural/genetic disease of the sperm flagellar axoneme.

**Genetic risk factors:**
- **Consanguinity** is a strong risk factor for expression of this autosomal recessive disease: in the founding cohort, 12 of 20 subjects were born to consanguineous parents (Ben Khelifa et al. 2014, PMID: 24360805).
- **Founder mutations.** A recurrent splice-acceptor mutation (c.11788−1G>A) was found in 4/18 index cases in the original North African (Tunisian/Algerian/Libyan) cohort, with haplotype analysis supporting a **founder effect** (PMID: 24360805). Independently, a distinct frameshift founder allele, **c.11726_11727delCT (p.Pro3909ArgfsTer33)**, linked to the polymorphism rs12163565, was identified as recurrent in **East Asian/Chinese cohorts** and was absent from non-Asian populations (Chinese cohort study; PMID: 33929677, *J Assist Reprod Genet* 2021).
- No susceptibility loci, GWAS signals, or polygenic risk contributions have been reported; this is a single-gene Mendelian disorder, not a complex trait.

**Environmental/lifestyle risk factors:** None specifically implicated for SPGF18/DNAH1-MMAF; general male-infertility risk modifiers (smoking, heat exposure, toxins) are not reported as disease modifiers for this specific genetic entity in the literature retrieved.

**Protective factors:** None identified in the literature; there is no described protective allele or environmental protective factor specific to DNAH1-MMAF.

**Gene-environment interaction:** Not reported for this gene/phenotype; SPGF18 behaves as a fully genetically-determined trait.

---

## 3. Phenotypes

SPGF18 is essentially monosymptomatic at the organismal level (primary infertility) with the defining abnormality confined to **sperm cell morphology and motility (laboratory/semen-analysis findings)**:

| Phenotype | Description | Frequency/Severity | Suggested HP term |
|---|---|---|---|
| Primary male infertility | Inability to conceive despite unprotected intercourse; presenting complaint in all reported cases | 100% (defining feature) | HP:0003251 (Male infertility) |
| Multiple morphological abnormalities of the sperm flagella (MMAF) | Mosaic of absent, short, coiled, bent, and irregular-caliber flagella in the same ejaculate | 100% (defining feature); "mosaic" pattern rather than a single uniform defect | HP:0034424 |
| Severe/total asthenozoospermia | Near-zero to zero progressive sperm motility. In the founding cohort, 11/18 index cases had 0% motility and 8 had <10% motility (PMID: 24360805) | Severe to complete; variable between families/genotypes | HP:0008734 |
| Teratozoospermia | Abnormal sperm head/midpiece/flagellum morphology co-occurring with flagellar defects | Present in essentially all cases (asthenoteratozoospermia) | HP:0012207 (Teratozoospermia, if available) / free text |
| Normal secondary sexual characteristics, normal testicular volume, normal hormone profile | Reported as typically normal in DNAH1-MMAF cases, distinguishing it from hypogonadal causes of infertility | Common but not universally documented | — |
| Absence of respiratory/ciliary symptoms | Ben Khelifa et al. note that DNAH1-MMAF patients reported **no primary ciliary dyskinesia (PCD) symptoms** despite DNAH1 expression in ciliated respiratory tissue, suggesting tissue-specific compensation (PMID: 24360805) | Notable negative finding | Relevant to differential diagnosis (see §6, §9) |

**Onset:** Adult-onset presentation, essentially always identified at reproductive age during infertility workup; there is no pediatric or congenital extra-reproductive phenotype described for the pure SPGF18 form (contrast with the CILD37 allelic disorder, which can present with neonatal respiratory distress; see §9).

**Progression:** Non-progressive — this is a static structural/functional defect of gametogenesis rather than a degenerative process; severity (percent motility, proportion of morphologically normal spermatozoa) is stable for a given individual and largely genotype-dependent.

**Quality of life impact:** The principal burden is reproductive/psychosocial (infertility-related distress) and the need for assisted reproduction; no data indicate impact on other domains of daily functioning, consistent with the tissue-restricted nature of the defect in the isolated SPGF18 form.

---

## 4. Genetic/Molecular Information

**Causal gene:** DNAH1 (Dynein Axonemal Heavy Chain 1)
- **HGNC:** HGNC:2940
- **Gene OMIM:** *603332
- **Cytoband/coordinates:** 3p21.1 (GRCh38 chr3:52,310,920–52,400,492) — per GeneCards
- **Protein:** A large (~4,477 amino acid) axonemal inner dynein arm (IDA) heavy chain, an ATPase-based motor protein containing **six tandem AAA-ATPase domains** in its motor head plus a microtubule-binding domain (Ben Khelifa et al. 2014, PMID: 24360805; GeneCards). IDA heavy chains are believed to strengthen the mechanical linkage between the radial spokes and the outer doublet microtubules, driving flagellar beat generation and regulation.

**Pathogenic variant spectrum (representative, from primary literature):**
- c.11788−1G>A (splice acceptor) — recurrent/founder in North African patients; 4/18 index cases (PMID: 24360805)
- c.5094+1G>A (splice donor)
- c.12796T>C (stop-loss)
- c.3877G>A, p.Asp1293Asn (missense)
- c.11726_11727delCT, p.Pro3909ArgfsTer33 — recurrent founder mutation in East Asian/Chinese cohorts, found in 4/9 patients with severe asthenozoospermia in one series (PMID: 33929677)
- Additional hotspot variants reported in Chinese cohorts: p.R868X, p.Q1518X, p.E3284K, p.R4096L (PMID: 33929677)
- Both truncating (nonsense, frameshift, splice) and missense variants have been associated with the classical MMAF phenotype, indicating that both complete loss-of-function and specific missense substitutions in functional domains (e.g., AAA-ATPase or microtubule-binding regions) are pathogenic.

**Variant classification:** Variants are generally classified pathogenic/likely pathogenic under ACMG/AMP criteria (biallelic occurrence, segregation with disease in consanguineous families, loss-of-function mechanism, absence/rarity in population databases such as gnomAD). Exact gnomAD allele-frequency and constraint (pLI/LOEUF) values for DNAH1 could not be retrieved from the sources searched in this session; DNAH1 is a very large gene, which typically yields a high raw count of rare missense/LoF variants in population databases even though biallelic pathogenic combinations remain rare — recommend querying gnomAD directly (gnomad.broadinstitute.org, gene DNAH1) to source these figures for curation.

**Inheritance and zygosity:** Autosomal recessive; both homozygous (favored in consanguineous pedigrees) and compound heterozygous genotypes are reported. Segregation was confirmed in a three-affected-brother sibship carrying the same homozygous splice mutation (PMID: 24360805).

**Modifier genes:** None specifically reported for DNAH1/SPGF18; however, MMAF as a phenotypic class is genetically heterogeneous, with distinct genes producing a convergent phenotype (locus heterogeneity, not modifier-gene effect — see §6).

**Epigenetic information:** No epigenetic (DNA methylation, histone) mechanism has been reported for DNAH1-associated MMAF; this is a structural axonemal-protein deficiency, not an epigenetic dysregulation disorder.

**Chromosomal abnormalities:** No aneuploidy, translocation, or copy-number mechanism reported; disease arises from small-scale (point/indel/splice) sequence variants within DNAH1.

---

## 5. Environmental Information

No environmental toxins, occupational exposures, radiation, infectious agents, or lifestyle factors have been implicated as causal or contributory to SPGF18 in the literature retrieved. This is consistent with SPGF18 being a fully penetrant, structurally determined Mendelian disorder of axonemal assembly rather than an environmentally modulated trait. (General environmental causes of asthenozoospermia — heat, toxins — are documented for male infertility broadly, but none are specifically linked to the DNAH1-MMAF mechanism.)

---

## 6. Mechanism / Pathophysiology

### Causal chain (numbered, from molecular lesion to clinical manifestation)

1. Biallelic loss-of-function or damaging missense variants in **DNAH1** → **loss/reduction of functional DNAH1 protein** in developing spermatid flagella (demonstrated directly; PMID: 24360805).
2. Loss of DNAH1 **leads to** failure of proper **inner dynein arm (IDA) assembly and localization** within the axoneme of the elongating sperm tail — TEM in an index case showed mislocalization and loss of inner dynein arms (PMID: 24360805).
3. Disrupted IDA scaffolding **results in** secondary **structural disorganization of the "9+2" axonemal core**: approximately one-third of outer microtubule doublets were malformed or absent, and the central-pair microtubules were entirely missing in 47% of examined cross-sections (a "9+0" configuration) in the founding study (PMID: 24360805).
4. Axonemal disorganization **leads to** severe **disorganization of the surrounding fibrous sheath** (abnormal/absent in ~90% of sections examined) — i.e., the defect is not confined to the dynein motor complex but propagates to the accessory cytoskeletal sheath that normally regulates flagellar beat mechanics (PMID: 24360805). This is presented as a downstream structural consequence, inferred from co-occurrence in the same ultrastructural sections rather than shown as an independent direct DNAH1 interaction.
5. Combined loss of IDA motor force generation, doublet/central-pair disorganization, and fibrous sheath collapse **produces** the **mosaic gross flagellar phenotype** observed by light microscopy — absent, short, coiled, bent, and irregular-caliber flagella coexisting within a single ejaculate (PMID: 24360805).
6. Structurally defective, motor-deficient flagella **cause** **severe-to-total asthenozoospermia** (0–<10% motility in most index cases) **and** **teratozoospermia**, jointly producing the clinical endpoint of **primary male infertility** by preventing normal sperm progression to and penetration of the oocyte (PMID: 24360805).
7. **Branch — tissue-restricted expression/compensation:** Despite DNAH1 also being expressed in respiratory motile cilia, DNAH1-MMAF patients characteristically lack primary ciliary dyskinesia (PCD) respiratory symptoms, suggesting a compensatory mechanism (e.g., partial redundancy with paralogous axonemal dyneins) operative in respiratory cilia but not in the sperm-specific flagellar axoneme (PMID: 24360805 — explicitly flagged by the authors as an inferred, not directly demonstrated, mechanism). A separate allelic disorder (CILD37, OMIM #617577) shows that sufficiently severe DNAH1 loss-of-function *can* produce a respiratory ciliopathy phenotype in some patients/pedigrees (PMID for the DNAH1-PCD family: 25927852), indicating this compensation is incomplete/variant-dependent rather than absolute.

### Detail by category

- **Molecular pathway:** Not a signaling cascade but a **cytoskeletal motor-protein assembly pathway** — dynein arm docking onto the axonemal doublet microtubules (relevant Reactome/GO context: "cilium organization," "axoneme assembly," "microtubule-based movement"). Suggested GO terms: **GO:0036126** (sperm flagellum assembly), **GO:0003777** (microtubule motor activity), **GO:0005858** (axonemal dynein complex), **GO:0030317** (flagellated sperm motility).
- **Cellular process:** Spermiogenesis-stage flagellar morphogenesis defect (failure of proper axonemal/accessory-structure assembly during spermatid elongation), not apoptosis or classic degenerative cell death.
- **Protein dysfunction:** Loss-of-function (absent/truncated protein from nonsense, frameshift, and splice variants) or presumed hypomorphic/structural missense dysfunction (e.g., p.Asp1293Asn) impairing motor-domain (AAA-ATPase) or microtubule-binding function, causing failure of stable dynein-arm docking (PMID: 24360805).
- **Species divergence (important translational caveat):** The murine *Dnah1* (Mdhc7) knockout is infertile via **reduced sperm motility only**, with **no observable axonemal ultrastructural defect** by electron microscopy — a materially milder phenotype than the severe human axonemal disorganization/MMAF seen with human DNAH1 loss. This is a documented human–model discordance (species/paralog redundancy differences), relevant to any `HUMAN_MODEL_MISMATCH`-type curation flag: the mouse model recapitulates the motility/infertility endpoint but **fails to recapitulate** the structural axonemal lesion.
- **Immune system involvement:** None reported.
- **Tissue damage mechanism:** Not classic tissue injury (oxidative stress, ischemia, fibrosis) — a developmental/structural assembly failure specific to a specialized cytoskeletal organelle (the flagellar axoneme) in a single, terminally differentiating cell type (the spermatid/spermatozoon).
- **Biochemical abnormality:** Failure of a specific ATPase motor complex (inner dynein arm) to assemble/function normally within the axoneme.
- **Omics/advanced technologies:** No dedicated transcriptomic, proteomic, metabolomic, single-cell, or spatial-transcriptomic dataset specific to DNAH1-MMAF spermatids was retrieved in this search; characterization to date rests principally on **exome/targeted sequencing plus transmission electron microscopy (TEM)** ultrastructural phenotyping, which remains the primary diagnostic and mechanistic tool in this literature.

**Suggested cell type:** CL:0000019 (sperm), or more specifically the elongating spermatid (developing flagellum) as the affected cell population; **UBERON:0000995 / UBERON:0001301** (testis / spermatid) for anatomical/cellular context.

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Testis — specifically the process of spermiogenesis (post-meiotic sperm maturation); **UBERON:0000473** (testis).
- **Organ level (secondary/systemic):** None — SPGF18 is not reported to involve other organ systems in its isolated form (contrast with the CILD37 allelic phenotype, which affects the respiratory tract; see §9).
- **Body system:** Male reproductive system only (isolated form).
- **Tissue/cell level:** Germ-cell lineage, specifically **spermatids/spermatozoa** during flagellar morphogenesis; Cell Ontology term **CL:0000019** (sperm) or **CL:0000018/CL:0000216** (spermatid stages) as appropriate.
- **Subcellular level:** The **sperm flagellum/axoneme** is the principal subcellular structure affected — **GO:0036126** (sperm flagellum assembly, cellular component), **GO:0005858** (axonemal dynein complex), **GO:0031514** (motile cilium), and the accessory **fibrous sheath** of the principal piece of the flagellum.
- **Localization:** Bilateral/systemic within the reproductive tract (affects all developing spermatozoa, not a focal lesion); no lateralization concept applies.

---

## 8. Temporal Development

- **Onset:** Adult, reproductive-age onset of clinical recognition (infertility investigation); the underlying structural defect is present from spermiogenesis onset but is asymptomatic until fertility is attempted.
- **Onset pattern:** Not applicable in the acute/subacute/chronic sense — a stable, lifelong structural gametogenic defect.
- **Disease stages:** Not applicable; MMAF/SPGF18 does not have formal staging.
- **Progression rate/course:** Stable/non-progressive — repeat semen analyses in affected men are expected to show a consistently severe phenotype rather than worsening or fluctuating motility, since the defect is intrinsic to axonemal assembly rather than an ongoing degenerative process.
- **Duration:** Lifelong (the underlying genetic lesion does not resolve), though the reproductive consequence is addressable via assisted reproduction (see §12).
- **Remission:** None spontaneously; assisted reproduction (ICSI) can achieve pregnancy despite the underlying sperm defect (see §12), which functions as a bypass rather than a disease remission.
- **Critical periods:** The relevant "critical period" is embryological/spermatogenic — spermiogenesis (the post-meiotic differentiation phase during which the flagellum is assembled) is the developmental window in which the DNAH1 defect is manifested.

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal recessive (established via consanguineous pedigrees, sibling recurrence, and biallelic variant segregation; PMID: 24360805).
- **Penetrance:** Appears complete for the infertility phenotype in biallelic carriers reported to date (all reported homozygotes/compound heterozygotes are infertile), though ascertainment bias (patients identified through infertility clinics) should be considered.
- **Expressivity:** Variable in **severity of motility/morphology defect** and in **extra-reproductive manifestation** — most patients show isolated infertility, but rare DNAH1-biallelic patients present instead with the primary ciliary dyskinesia phenotype (CILD37, OMIM #617577; PMID: 25927852, describing a homozygous missense p.Lys1154Gln DNAH1 variant in a consanguineous Saudi Arabian PCD family with chronic wet cough, sinusitis, bronchiectasis, and neonatal respiratory distress). This indicates that **DNAH1 is an allelic-disorder gene**: different biallelic genotypes (and possibly genetic background) determine whether the clinical presentation is isolated MMAF/infertility (SPGF18) or a systemic ciliopathy (CILD37) — an important curation distinction to keep the two OMIM phenotypes (#617576 vs #617577) separate rather than conflated.
- **Genetic anticipation:** Not reported/applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically reported.
- **Founder effects:** Documented — the c.11788−1G>A splice mutation is a founder allele in North African populations (Tunisia/Algeria/Libya; PMID: 24360805), and c.11726_11727delCT (p.Pro3909ArgfsTer33) is a distinct founder allele reported specifically in East Asian (Chinese) cohorts and linked to marker rs12163565 (PMID: 33929677) — evidence of independent founder events in geographically distinct populations rather than a single global founder mutation.
- **Consanguinity:** A strong ascertainment/risk factor; 12/20 subjects in the founding cohort were from consanguineous unions (PMID: 24360805).
- **Carrier frequency:** Not established/reported in the retrieved literature; DNAH1's large coding size likely yields population-level rare-variant carriage, but a validated carrier frequency figure was not found in this search and should be sourced from gnomAD directly for curation purposes.

**Epidemiology:**
- DNAH1 is consistently identified as the **most frequently mutated single gene** in MMAF cohorts, accounting for roughly **28–29% of MMAF cases** in the two largest reported series (28% in the founding North African cohort of 18 index cases, PMID: 24360805; 29% [12/41] in a Chinese NGS-panel cohort, PMID: 33929677), making DNAH1/SPGF18 the single largest identifiable genetic subgroup within the broader ~40-gene MMAF genetic landscape, within which "identified variants could account for about 60.0%–75.0% of infertile men diagnosed with MMAF," leaving 25–40% of MMAF cases genetically unsolved (review literature retrieved via search).
- MMAF as a phenotypic class is a rare cause of male infertility overall; asthenozoospermia broadly accounts for a substantial fraction of male-factor infertility (~19–80% of cases depending on definition used across sources retrieved), but MMAF itself is a much narrower, severe subset. A precise population prevalence figure (cases per 100,000) specific to MMAF or SPGF18 was not found in the sources searched and is likely to be reported (if at all) via Orphanet, which should be queried directly for curation (Orphanet entry not successfully retrieved in this session due to a tool access limitation).
- **Population/geographic distribution:** Cohorts studied span **North Africa (Tunisia, Algeria, Libya)**, **China/East Asia**, **Iran** (Amiri-Yekta et al., Royan Institute), and **Pakistan**, with population-specific founder alleles identified in North African and East Asian groups — indicating DNAH1-MMAF is globally distributed but shaped by locally private founder mutations rather than one worldwide recurrent allele.
- **Sex ratio:** Not applicable — by definition this is a male-limited spermatogenic phenotype (though female carriers of heterozygous variants are, as expected for autosomal recessive disease, unaffected and can transmit the allele).
- **Age distribution:** Reproductive-age men presenting for infertility evaluation (typically 20s–40s), consistent with standard fertility-clinic ascertainment.

---

## 10. Diagnostics

- **Clinical/laboratory tests:**
  - **Semen analysis** (WHO criteria) is the first-line test, showing severe asthenozoospermia (frequently 0–<10% motility) with concurrent teratozoospermia.
  - **Light microscopy of sperm morphology** reveals the characteristic mosaic of absent, short, coiled, bent, and irregular-caliber flagella that defines the MMAF phenotype.
  - **Transmission electron microscopy (TEM)** of sperm flagella is a key diagnostic/mechanistic tool, revealing inner dynein arm loss/mislocalization, disorganized/missing microtubule doublets (including 9+0 configurations from central-pair loss), and fibrous sheath disorganization (PMID: 24360805). Suggested SNOMED CT/pathology-relevant term: sperm axonemal ultrastructural abnormality.
- **Genetic testing:**
  - **Whole-exome sequencing (WES)** and **targeted MMAF gene panels** (encompassing DNAH1 plus the ~40 other known MMAF genes: CFAP43, CFAP44, CFAP69, AK7, ARMC2, QRICH2, TTC29, DNAH8, DNAH17, DNAH2, FSIP2, CFAP91/WDR66, SPEF2, CFAP65, CEP135, TTC21A, AKAP4, CFAP47, CFAP57, CFAP70, DNHD1, TTC12, DNAH6, DNAH3, DNAH12, BRWD1, among others) are the standard diagnostic approach, since MMAF is genetically highly heterogeneous and clinically indistinguishable across causal genes by light microscopy alone.
  - **NCBI GTR** lists commercial "Spermatogenic failure: Full gene sequencing panel" tests covering DNAH1 and related genes.
  - Homozygosity mapping (SNP arrays) has historically been used in consanguineous pedigrees to localize the causal gene, as in the original DNAH1 discovery study.
- **Differential diagnosis:** Other MMAF-causing genes (listed above) are the primary differential, since phenotype at the light-microscopy level is convergent/non-specific across genes; genetic testing is required to distinguish DNAH1-MMAF (SPGF18) from other genetic MMAF subtypes and from the related-but-distinct DNAH1-associated **primary ciliary dyskinesia (CILD37)** phenotype, which additionally requires assessment for respiratory ciliary dysfunction (nasal nitric oxide, ciliary beat pattern analysis, respiratory TEM) if extra-reproductive symptoms are present.
- **Screening:** No population/newborn screening applies (adult-onset ascertainment via infertility); genetic counseling and carrier testing are relevant for consanguineous families or when a proband's biallelic genotype is known, to inform recurrence risk and family planning (including preimplantation genetic testing where infertility is overcome via ICSI).

---

## 11. Outcome/Prognosis

- **Survival/mortality:** Not applicable — SPGF18 is not a life-limiting or morbid systemic condition in its isolated form; there is no reported mortality or shortened life expectancy directly attributable to DNAH1-MMAF.
- **Morbidity:** The morbidity is essentially confined to infertility itself and its downstream psychosocial and reproductive-treatment burden.
- **Fertility-specific outcomes (the disease's core outcome measure):**
  - DNAH1-mutated MMAF patients are reported to have a **comparatively favorable prognosis with intracytoplasmic sperm injection (ICSI)** relative to some other MMAF genotypes — this is a recurring theme across the literature retrieved (e.g., "Patients with multiple morphological abnormalities of the sperm flagella due to DNAH1 mutations have a good prognosis following intracytoplasmic sperm injection," *Human Reproduction* 2016;31(6):1164-1172).
  - One cohort reported a **pregnancy rate of 61.90%** among DNAH1-variant patients undergoing ICSI (Zhuang et al., cited in secondary literature retrieved).
  - Outcomes are nonetheless **variable and genotype-dependent**: not all DNAH1-mutation-positive patients succeed, and "failed cases still occur," attributed to variability in residual sperm structural/functional integrity and to specific variant effects on embryonic development potential (2022 literature review, *Frontiers in Genetics*, and related MMAF/ICSI outcome literature).
  - Broader MMAF literature (not DNAH1-specific) reports **decreased embryo developmental potential and lower cumulative pregnancy rate** in MMAF patients generally compared with non-MMAF infertile controls, underscoring that while DNAH1 has a relatively favorable reputation among MMAF genes, ICSI outcomes in MMAF as a class remain inferior to normospermic controls.
- **Complications:** None specific to the disease beyond the infertility itself and standard ICSI-related risks (procedural, not disease-related).
- **Recovery potential:** The underlying gametogenic/structural defect is not reversible, but fertility can be achieved via assisted reproduction bypassing the natural motility requirement (ICSI directly injects an immotile/structurally abnormal but genetically intact spermatozoon into the oocyte).
- **Prognostic factors:** Genotype (specific DNAH1 variant/domain affected) appears to influence the degree of residual sperm structural integrity and thus ICSI/embryonic outcome, though granular genotype-outcome correlation data were not comprehensively retrievable in this search session.

---

## 12. Treatment

There is **no curative or disease-modifying pharmacotherapy** for SPGF18 — the mainstay of management is assisted reproductive technology bypassing the natural motility/morphology defect.

- **Primary therapeutic approach — Intracytoplasmic Sperm Injection (ICSI):**
  - ICSI is the standard and effective treatment strategy, as DNAH1-mutation-positive men have consistently favorable reported ICSI outcomes relative to many other MMAF genotypes (Human Reproduction 2016;31(6):1164-1172, and subsequent cohort/review literature).
  - Clinical guidance explicitly states: "**DNAH1 mutation positive patients can thus be encouraged to initiate an IVF/ICSI procedure**" (2022 literature-review synthesis, *Frontiers in Genetics*, "Clinical detection, diagnosis and treatment of morphological abnormalities of sperm flagella: A review of literature").
  - **NCIT clinical-intervention terms:** Assisted reproductive procedures such as ICSI do not map to a discrete standard NCIT term set in the dismech treatment vocabulary excerpted; the closest general clinical-action term would be a fertility/reproductive procedure category — curators should verify against NCIT for an ICSI-specific term (e.g., search NCIT for "intracytoplasmic sperm injection") rather than assuming coverage under a generic surgical-procedure term.
  - Testicular sperm extraction (in cases of very low ejaculated sperm availability/quality) combined with ICSI has also been reported as a successful route in severe MMAF/total-immotility cases in the broader literature (e.g., successful birth after ICSI with testicular immotile spermatozoa in total-MMAF patients).
- **Sperm selection adjuncts:** Techniques such as intracytoplasmic morphologically selected sperm injection (IMSI) have been studied in general severe male-factor infertility, though evidence specifically isolating DNAH1-MMAF benefit was not found in this search.
- **Genetic counseling:** Recommended for affected men and their partners given the autosomal recessive inheritance and (in consanguineous populations) elevated recurrence risk; relevant for informed reproductive decision-making, including consideration of preimplantation genetic testing for offspring once pregnancy is achieved via ICSI, if the couple wishes to know/avoid transmission (though offspring would typically only be carriers unless the partner is also a carrier, given the rarity of the allele outside of consanguineous or founder populations).
- **No pharmacotherapy, gene therapy, or targeted molecular therapy** has been reported or is in clinical development specifically for DNAH1/SPGF18 in the literature retrieved; this remains a structural/mechanical fertility problem managed via reproductive technology rather than molecular correction.
- **Experimental treatments:** No DNAH1-specific clinical trials were identified in this search (search focused on general ICSI trials, not DNAH1-specific interventional trials); a targeted ClinicalTrials.gov / WHO ICTRP search for "DNAH1" or "MMAF" trials is recommended for curation completeness but did not surface a specific NCT identifier in the sources retrieved here.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (this is a fixed germline genetic disease, not preventable by exposure/behavior modification); the only "prevention" lever is reproductive — genetic counseling and carrier testing in consanguineous families or populations with known founder alleles (North African, East Asian) to inform reproductive planning.
- **Secondary prevention/early detection:** Genetic testing of infertile men with the MMAF semen phenotype allows early, specific molecular diagnosis, which informs prognosis (see §11) and avoids unnecessary repeated empiric fertility interventions.
- **Screening:** No population-level newborn or carrier screening program specific to DNAH1/MMAF was identified; carrier screening would be most relevant in a targeted fashion within consanguineous or founder-mutation-enriched populations, analogous to other autosomal recessive disease carrier-screening paradigms, but no such formal program was found in the literature searched.
- **Genetic counseling:** The principal "preventive" clinical service applicable here — counseling affected men (and, where relevant, their reproductive partners) about autosomal recessive inheritance, recurrence risk for future pregnancies (particularly relevant if using a sperm donor is not desired and the couple pursues ICSI with the affected man's own testicular/ejaculated sperm), and reproductive options.
- **Public health/behavioral/immunization:** Not applicable — no infectious, immunization-preventable, or public-health-environmental dimension to this disease.

---

## 14. Other Species / Natural Disease

- **Mouse (*Mus musculus*, NCBI Taxon:10090):** The orthologous gene is *Dnah1* (also referenced historically as *Mdhc7*; MGI:107721). ***Dnah1*-knockout mice are infertile due to markedly reduced sperm motility** (dramatically reduced straight-line velocity and progressive movement, preventing sperm transit from the uterus into the oviduct), recapitulating the motility/infertility endpoint of the human disease. **However, the mouse model critically fails to recapitulate the human structural phenotype:** knockout sperm show **no observable axonemal ultrastructural defect by electron microscopy**, in clear contrast to the severe axonemal disorganization (doublet loss, missing central pair, fibrous sheath disruption) documented in DNAH1-deficient human spermatozoa (PMID: 24360805 and subsequent literature, e.g., PMC8635859 "Novel Loss-of-Function Mutations in DNAH1 Displayed Different Phenotypic Spectrum in Humans and Mice"). This is a well-documented, citable **human/model fidelity gap** — of direct relevance to curation using the `HUMAN_MODEL_MISMATCH` framework: the mouse model is informative for the infertility/motility endpoint (moderate-to-high fidelity) but has **low fidelity for the axonemal ultrastructural mechanism** specifically, likely reflecting species differences in dynein-arm paralog redundancy or compensatory motor proteins.
- **Natural/veterinary disease:** No naturally occurring companion-animal or livestock DNAH1-associated MMAF disease was retrieved in this session, though the broader MMAF-associated gene family has been studied in **goats** in the context of litter size and reproductive genetics (ScienceDirect: "Multiple morphological abnormalities of the sperm flagella (MMAF)-associated genes: The relationships between genetic variation and litter size in goats") — indicating comparative/agricultural relevance of the MMAF gene family (not confirmed DNAH1-specific) to livestock reproductive traits, worth checking OMIA for a DNAH1-specific animal entry during formal curation.
- **Comparative biology:** DNAH1 is a member of a large, evolutionarily conserved axonemal dynein heavy chain gene family (paralogs include DNAH2, DNAH3, DNAH6, DNAH8, DNAH11, DNAH12, DNAH17, among others), each associated with distinct but phenotypically overlapping MMAF and/or PCD presentations in humans and, in several cases, validated in mouse knockout models (e.g., DNAH2, DNAH3, DNAH8, DNAH12), reflecting deep evolutionary conservation of axonemal dynein-based ciliary/flagellar motility across metazoans.
- **Transmission/zoonotic potential:** Not applicable — this is a non-communicable, structural/genetic reproductive disorder.

---

## 15. Model Organisms

- **Primary genetic model: *Dnah1* knockout mouse** (constitutive knockout; historically referenced as Mdhc7−/−). 
  - **Phenotype recapitulation:** Faithfully reproduces **male infertility via severely impaired sperm motility** (failure of sperm transit from uterus to oviduct due to reduced straight-line velocity/progressive movement).
  - **Model limitation:** Does **not** reproduce the defining human **axonemal ultrastructural disorganization** (no TEM-detectable doublet/central-pair/fibrous-sheath defects), making it a good model for the functional (motility) endpoint but a poor model for the structural (MMAF) mechanism — an important caveat for any computational or translational inference drawn from the mouse data.
  - **Resource:** MGI:107721 (Mouse Genome Informatics, Dnah1 gene page) for allele/phenotype records.
- **No invertebrate (Drosophila, C. elegans), zebrafish, yeast, or iPSC/organoid model** specific to DNAH1/SPGF18 was identified in the literature retrieved during this session; given that flagellar/ciliary axonemal biology is broadly conserved, related invertebrate ciliary-motility models likely exist for the dynein gene family generally, but a DNAH1-specific citation was not found and should be checked directly in FlyBase/WormBase/ZFIN if needed for curation completeness.
- **Applications:** The mouse model is primarily useful for studying **motility mechanics and fertilization competence** downstream of dynein-arm loss, but is not suited to modeling the **axonemal structural assembly defect** that is the histopathological hallmark of the human disease — human sperm TEM (from patient semen samples) therefore remains the indispensable source of mechanistic/structural data for SPGF18, rather than the mouse model.

---

## Summary of Key Citations

| Citation | Contribution |
|---|---|
| Ben Khelifa M, et al. *Am J Hum Genet* 2014;94(1):95-104. **PMID: 24360805** | Disease-founding paper: DNAH1 mutations cause MMAF/SPGF18; defines phenotype, mechanism, mouse-human discordance |
| *Hum Reprod* 2016;31(6):1164-1172 (Amiri-Yekta/Wambergue et al.) | DNAH1-MMAF ICSI prognosis is favorable |
| *Hum Reprod* 2016;31(12):2872-2880 | Whole-exome sequencing of familial MMAF cases, new DNAH1 mutations |
| Chinese cohort study, *J Assist Reprod Genet* 2021. **PMID: 33929677** | Mutational landscape of DNAH1 in Chinese patients; East Asian founder allele |
| OMIM #617576 (SPGF18), *603332 (DNAH1), #617577 (CILD37) | Clinical synopsis, molecular genetics, allelic-disorder cross-reference |
| DNAH1-PCD family report. **PMID: 25927852** | DNAH1 as a cause of the allelic ciliopathy CILD37 |
| GeneCards (DNAH1) | Gene structure, chromosomal location, protein domain architecture |

**Notable gaps for follow-up curation:** exact Orphanet ORPHA code and formal prevalence class for MMAF/SPGF18 (WebFetch access to Orphanet was blocked this session — retry directly); gnomAD allele frequency/constraint (pLI, LOEUF) metrics for DNAH1; a DNAH1-specific ClinicalTrials.gov/WHO ICTRP entry, if any; and confirmation of whether an OMIA veterinary entry exists for DNAH1 specifically (distinct from the general goat MMAF-gene-family study identified).

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 18 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 5 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0034424` (2 mentions) - the report calls it "100% (defining feature); "mosaic" pattern rather than a single uniform defect"; HP calls it **Clicking tinnitus**
- `HP:0008734` (2 mentions) - the report calls it "Severe to complete; variable between families/genotypes"; HP calls it **Decreased testicular size**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0012207` (1 mention) - the report calls it "Teratozoospermia, if available"; HP calls it **Reduced sperm motility**, and lists "Asthenozoospermia" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`, `MGI`.