---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-24T18:51:36.535251'
end_time: '2026-08-24T18:55:49.507129'
duration_seconds: 252.97
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hereditary Spastic Paraplegia 7
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
  web_search_requests: 13
  num_turns: 16
  total_cost_usd: 1.434067
  session_id: 5f967ed8-4b7d-5ed5-b009-2720effe579b
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 34
reference_validation:
  total_references: 17
  verified: 4
  not_found: 0
  unverifiable: 13
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 2
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Spastic Paraplegia 7
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Spastic Paraplegia 7** covering all of the
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

I now have comprehensive sourced material. Compiling the full research report.

# Hereditary Spastic Paraplegia 7 (SPG7) — Comprehensive Disease Research Report

## 1. Disease Information

**Overview.** Hereditary Spastic Paraplegia 7 (SPG7; also called SPG7-related neurologic disorder) is an autosomal recessive neurodegenerative disorder caused by biallelic pathogenic variants in *SPG7*, which encodes the mitochondrial inner-membrane m-AAA protease subunit **paraplegin**. It is the first-identified autosomal recessive form of hereditary spastic paraplegia (HSP) and one of the most common causes of autosomal recessive HSP and spastic ataxia, accounting for roughly 5–12% of AR-HSP cases. The classic presentation is slowly progressive bilateral lower-limb spasticity and weakness from corticospinal tract axonal degeneration, but SPG7 is now recognized as a broad phenotypic spectrum encompassing uncomplicated spastic paraplegia, complicated spastic ataxia, isolated cerebellar/spinocerebellar ataxia, isolated optic atrophy, chronic progressive external ophthalmoplegia (PEO), and other presentations (GeneReviews, [NCBI Bookshelf NBK1107](https://www.ncbi.nlm.nih.gov/books/NBK1107/)).

**Key identifiers:**
- **OMIM:** #607259 (Spastic Paraplegia 7, Autosomal Recessive); gene locus OMIM #602783 (SPG7 Matrix AAA Peptidase Subunit, Paraplegin) ([OMIM #607259](https://omim.org/entry/607259); [OMIM #602783](https://www.omim.org/entry/602783))
- **Gene location:** Chromosome 16q24.3
- **GeneReviews:** SPG7-Related Neurologic Disorder ([NBK1107](https://www.ncbi.nlm.nih.gov/books/NBK1107/))
- **GARD/NIH Rare Disease listing:** [Hereditary spastic paraplegia 7](https://rarediseases.info.nih.gov/diseases/4927/hereditary-spastic-paraplegia-7)
- **GTR condition record:** [C1846564](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1846564/)
- **Reference transcript:** NM_003119 (used for HGVS variant nomenclature in ClinVar)

**Synonyms/alternative names:** Spastic paraplegia 7, autosomal recessive; SPG7-related disorder; hereditary spastic ataxia-7; paraplegin deficiency; SPG7 spastic ataxia; autosomal recessive spastic ataxia with optic atrophy (in some phenotype descriptions).

**Evidence base.** Information derives primarily from aggregated cohort/disease-level resources (GeneReviews expert-curated summaries drawing on the international cohort of Coarelli et al. 2019 [n=241], OMIM, and case series/registries), not raw individual-level EHR data. Molecular/mechanistic data derive from model-organism (mouse, Drosophila) and patient-derived iPSC/fibroblast studies.

---

## 2. Etiology

### Disease Causal Factors
SPG7 is a monogenic mitochondrial disorder. Biallelic (homozygous or compound heterozygous) loss-of-function or missense pathogenic variants in *SPG7* impair the m-AAA protease, causing progressive degeneration of the longest corticospinal and cerebellar axons — a length-dependent "dying-back" axonopathy driven by mitochondrial dysfunction and impaired axonal transport (see Mechanism, §6).

### Risk Factors
- **Genetic risk factors:**
  - **Causal biallelic variants** in *SPG7* (>100 reported pathogenic variants: missense, nonsense, frameshift, splice-site, and rare deletion/duplication CNVs).
  - **p.Ala510Val (c.1529C>T)** is the single most prevalent pathogenic allele, with a reported **carrier frequency up to ~1% in the general population** — making it a common "hypomorphic" variant that frequently appears in trans with a second, more severe allele, and occasionally appears to act as a low-penetrance dominant risk allele.
  - **p.Leu78Ter (c.233T>A)**, a nonsense variant in exon 2, was the most frequent variant in a Hungarian cohort (Frontiers Genetics, [PMC12215234](https://pmc.ncbi.nlm.nih.gov/articles/PMC12215234/)), with gnomAD minor allele frequency 0.0028 in South Asians (5 homozygotes reported).
  - **Compound heterozygosity/consanguinity** in populations with elevated consanguinity rates increases homozygosity risk.
  - **Heterozygous monoallelic SPG7 variants** have been reported as possible risk/modifier alleles for amyotrophic lateral sclerosis (ALS), and digenic heterozygosity with **AFG3L2** (the paralogous m-AAA subunit) causes a distinct motor-neuron/cerebellar disorder (see below).
- **Environmental/demographic risk factors:** None specifically established; disease is fully genetically determined, though age (onset window 20–40, mean 35.5 ± 14.3 years; range infancy to age 72) modifies symptom expression.
- **Protective factors:** None specifically documented in the literature reviewed; no known protective genetic modifiers or lifestyle protective factors are established.
- **Gene-environment interactions:** Not established for SPG7; disease penetrance and severity appear driven by variant type (loss-of-function vs. missense) rather than documented environmental modifiers.

---

## 3. Phenotypes

Frequencies below are drawn from the international GeneReviews-cited cohort (Coarelli et al. 2019, n=241), reported at first and follow-up ("second") examination, reflecting disease progression over time:

| Phenotype | HPO term (suggested) | Frequency (1st exam → 2nd exam) | Onset/course |
|---|---|---|---|
| Lower-limb spasticity / pyramidal syndrome | HP:0001257 (Spasticity) / HP:0002061 (Spastic paraplegia) | 89% → 97% | Progressive; severe gait abnormality in ~1/3 of individuals 8–10 yrs post-onset |
| Hyperreflexia | HP:0001347 | Common, part of pyramidal syndrome | Progressive |
| Extensor plantar (Babinski) response | HP:0003487 | Common | Progressive |
| Cerebellar ataxia (gait/limb) | HP:0001251 | 66% → 78% | Progressive |
| Cerebellar dysarthria | HP:0001260 | 42% → 57% | Progressive |
| Dysphagia | HP:0002015 | 15% → 28% | Progressive |
| Muscle wasting/amyotrophy | HP:0003202 | 10% → 30% | Progressive; distal predominance |
| Cognitive impairment (executive/visuoconstructive) | HP:0100543 | 8% → 19% | Progressive, mild |
| Decreased visual acuity (optic neuropathy) | HP:0000572 / HP:0000648 (Optic atrophy) | 7% → 14% | Progressive |
| Ptosis | HP:0000508 | 5% → 17% | Progressive |
| Dystonia (mainly lower limb) | HP:0001332 | 2% → 11.5% | Progressive |
| Ophthalmoparesis/progressive external ophthalmoplegia | HP:0000602 | Variable (in one cohort, PEO seen in 1 patient) | Variable |
| Nystagmus | HP:0000639 | Common ocular finding (65% ocular abnormality overall; nystagmus most frequent) | Variable |
| Peripheral sensorimotor neuropathy | HP:0007141 | Present in subset | Progressive |
| Neuropathic pain | HP:0012532 | Present in subset | Variable |
| Pes cavus | HP:0001762 | Reported | Static/progressive |
| Scoliosis | HP:0002650 | Reported | Progressive |
| Hearing loss | HP:0000365 | Reported in subset | Variable |
| Urinary urgency/bladder dysfunction | HP:0000012 | Common, part of complicated HSP | Progressive |
| Loss of vibratory sense | HP:0007190 | Common | Progressive |

**Phenotype spectrum categories** (GeneReviews): uncomplicated spastic ataxia, complicated spastic ataxia, spinocerebellar ataxia, and isolated optic nerve atrophy — the boundaries between these presentations are not fixed, and spasticity and ataxia can occur "in isolation, at the same time, or sequentially," with most patients eventually developing both.

**Age of onset:** Mean 35.5 ± 14.3 years (typically 20–40 years), but ranges from infancy to age 72.

**Progression:** Insidious, slowly progressive. Roughly one-third of individuals show severe gait abnormality within 8–10 years of onset; some become wheelchair-dependent.

**Quality of life impact:** A cerebello-cortical connectivity study found cognitive and social/behavioral deficits (e.g., disturbed attention, executive function, emotional communication impairment) linked to cerebellar-cortical circuit alterations in SPG7 patients (PMC7053515). Progressive mobility loss, dysphagia risk (aspiration), visual impairment, and bladder dysfunction compound cumulative disability and reduced independence over the disease course.

---

## 4. Genetic/Molecular Information

**Causal gene:** *SPG7* (HGNC gene symbol SPG7; protein: paraplegin), chromosome 16q24.3, OMIM gene entry #602783.

**Variant classification and types:**
- >100 reported pathogenic/likely pathogenic variants (ClinVar, HGMD): missense, nonsense, frameshift, splice-site, and rare deletion/duplication CNVs.
- **Detection rates:** sequence analysis (missense/nonsense/small indel/splice) detects >90% of pathogenic alleles; gene-targeted deletion/duplication analysis (qPCR, long-range PCR, MLPA, targeted microarray) detects <10% of the remainder.
- **Deep intronic/non-coding variants** missed by exome sequencing have been identified via genome sequencing, explaining some cases with only one variant found by exome (PMC12883507 — "Identification of an additional deep intronic splice variant prompts critical evaluation of SPG7 inheritance").

**Recurrent/founder variants:**
- **p.Ala510Val (c.1529C>T)** — most common pathogenic allele overall; population carrier frequency up to ~1%; associated with a **cerebellar-ataxia-predominant** phenotype and slightly later onset; frequently found as compound heterozygote or in apparent pseudodominant pedigrees.
- **p.Leu78Ter (c.233T>A)** — nonsense/loss-of-function variant, most common in a Hungarian cohort; associated with more severe, spasticity/pyramidal-and-optic-atrophy–predominant phenotype (loss-of-function genotype-phenotype correlation).

**Genotype-phenotype correlation:** Biallelic loss-of-function variants correlate with more pronounced pyramidal signs and optic atrophy; individuals carrying at least one missense allele (especially p.Ala510Val) tend to show more pronounced ataxia relative to spasticity.

**Population/allele frequency databases:** gnomAD, 1000 Genomes, ExAC/TOPMed for carrier-frequency and homozygote counts (e.g., p.Leu78Ter MAF 0.002778 in South Asian gnomAD subpopulation, 5 homozygotes).

**Functional consequences:** Loss of paraplegin function impairs the mitochondrial m-AAA protease quality-control complex (formed with AFG3L2), causing reduced Complex I respiratory chain activity, defective processing of mitochondrial substrates (e.g., MRPL32, EMRE), and dysregulated mitochondrial calcium handling via altered MCU-EMRE assembly and the mitochondrial permeability transition pore (mPTP) (Cell Research review, [PMC5835776](https://pmc.ncbi.nlm.nih.gov/articles/PMC5835776/)).

**Modifier genes / digenic interaction:** **AFG3L2** — the paralogous m-AAA protease subunit (mutated in autosomal dominant SCA28) — physically and functionally interacts with paraplegin. A 2025 study (medRxiv/BMC Medicine) found **digenic combined heterozygosity in SPG7 + AFG3L2** in patients with motor neuron disease and cerebellar ataxia phenotypes: among 4,817 MND/ataxia patients, 6 carried digenic variants (none among 1,827 controls); segregation in families was perfect; animal models with combined dysfunction of both genes show early-onset axonal degeneration and prominent Purkinje cell loss ([BMC Medicine 2025](https://link.springer.com/article/10.1186/s12916-026-04805-z); [medRxiv preprint](https://www.medrxiv.org/content/10.1101/2025.07.05.24312261.full.pdf)).

**Epigenetic information:** No disease-specific epigenetic (DNA methylation/histone) mechanism has been established for SPG7 in the literature reviewed.

**Chromosomal abnormalities:** SPG7 is caused by point mutations/small indels, not large chromosomal rearrangements; no recurrent CNV/aneuploidy syndrome association identified.

**Mitochondrial genome consequence (secondary):** Pathogenic *SPG7* variants cause **secondary mitochondrial DNA instability** — multiple mtDNA deletions accumulate in postmitotic tissue (skeletal muscle), analogous to POLG-related disorders, due to disordered mtDNA maintenance (Brain 2014, [Hudson lab study](https://academic.oup.com/brain/article/137/5/1323/335381)). Single-fiber molecular studies show multiple mtDNA deletions segregating at 38–97% heteroplasmy in COX-deficient muscle fibers ([PMC3899233](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3899233/)).

---

## 5. Environmental Information

No established environmental, lifestyle, or infectious causal or exacerbating factors are documented for SPG7 in the literature surveyed — it is a fully genetically determined mitochondrial disorder. No infectious agents are implicated. Systemic mitochondrial-toxic environmental exposures have not been specifically studied as modifiers of SPG7 severity, though caution around known mitochondrial-toxic drugs (e.g., certain antiretrovirals, statins in some mitochondrial disease contexts) may be prudent extrapolation from general mitochondrial disease management principles, not SPG7-specific evidence.

---

## 6. Mechanism / Pathophysiology

**Molecular function of paraplegin.** Paraplegin is the catalytic ATP-dependent metalloprotease subunit of the mitochondrial inner-membrane **m-AAA protease** complex, forming a hetero-oligomer with AFG3L2. This complex:
1. Performs mitochondrial **protein quality control** — degrading misfolded polypeptides and unassembled proteins on the matrix side of the inner mitochondrial membrane.
2. Carries out **proteolytic maturation** of specific substrates, including ribosomal protein MRPL32 (required for mitochondrial ribosome assembly/translation) and EMRE (a component of the mitochondrial calcium uniporter, MCU).
3. Regulates **mitochondrial calcium homeostasis**, limiting MCU-EMRE complex assembly and thereby modulating opening of the mitochondrial permeability transition pore (mPTP) — a key determinant of cell death susceptibility ([Cell Research, PMC5835776](https://pmc.ncbi.nlm.nih.gov/articles/PMC5835776/)).

**Causal chain (trigger → consequence):**
1. **Biallelic SPG7 loss-of-function/missense variant** → loss of functional m-AAA protease (paraplegin-AFG3L2 complex).
2. → **Reduced mitochondrial Complex I respiratory chain activity** and impaired mitoribosomal protein maturation (MRPL32 processing failure).
3. → **Mitochondrial calcium dysregulation** (via defective EMRE processing / MCU-EMRE control) and increased mPTP susceptibility.
4. → **Secondary mitochondrial genome instability** — accumulation of multiple mtDNA deletions in postmitotic tissues (muscle, neurons), producing COX-deficient, ragged-red fibers.
5. → **Mitochondrial morphological abnormalities** — swollen, dysmorphic mitochondria appearing first in **distal axons and synaptic terminals**, well before axonal swelling (mouse model: swollen mitochondria at 4.5 months, axonal swelling at 8 months, degeneration at 15 months — [JCI, Ferreirinha et al. 2004](https://www.jci.org/articles/view/20138)).
6. → **Impaired axonal transport** — anterograde transport impairment causes massive accumulation of organelles and neurofilaments within axonal swellings; retrograde transport is also delayed in symptomatic animals.
7. → **Length-dependent ("dying-back") axonal degeneration** — preferentially affecting the longest and largest-caliber axons: the corticospinal tract (causing spasticity), cerebellar afferent/efferent pathways (ataxia), and optic nerve (optic atrophy), because these neurons are most dependent on efficient long-distance axonal mitochondrial transport and energy supply.
8. → **Clinical manifestation**: progressive spastic paraparesis, cerebellar ataxia/dysarthria/dysphagia, optic atrophy, peripheral neuropathy, and (in a subset) PEO from muscle mtDNA deletion accumulation.

**Cell types/tissues involved:** upper motor neurons of corticospinal tract (Betz cells, axons), Purkinje cells and cerebellar circuitry, retinal ganglion cells/optic nerve axons, peripheral sensory/motor neurons, skeletal muscle fibers (secondary mitochondrial myopathy), and in digenic SPG7/AFG3L2 models, astrocytes (astrocyte-specific m-AAA protease deletion reveals a glial contribution to neurodegeneration — [PMC6618114](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6618114/)).

**Suggested ontology terms:**
- GO biological process: GO:0034982 (mitochondrial protein processing), GO:0006515 (protein quality control for misfolded/incompletely synthesized proteins), GO:0051560 (mitochondrial calcium ion homeostasis), GO:0007005 (mitochondrion organization), GO:0008090 (retrograde axonal transport), GO:0008089 (anterograde axonal transport)
- GO molecular function: GO:0004176 (ATP-dependent peptidase activity), GO:0004222 (metalloendopeptidase activity)
- GO cellular component: GO:0005743 (mitochondrial inner membrane), GO:0031966 (mitochondrial membrane)
- CL cell types: CL:0000029 (neuron, Betz cell / upper motor neuron equivalent), CL:0000121 (Purkinje cell), CL:0000740 (retinal ganglion cell), CL:0000187 (myocyte, skeletal muscle)
- CHEBI: CHEBI:29108 (calcium(2+) ion) for the calcium-dysregulation arm

**Molecular profiling / omics findings:** Patient-derived iPSC neurons and fibroblasts show mitochondrial functional deficits specific to SPG7 (contrasted with SPAST-mutant HSP lines, which do not show comparable mitochondrial deficits) ([PMC7469654](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7469654/)). A 2023 high-throughput pharmacological rescue study in SPG7 patient-derived neurons identified compounds that reverse mitochondrial and neuronal phenotypic defects, supporting mitochondrial dysfunction as a druggable node ([Frontiers in Neuroscience, PMC10520970](https://pmc.ncbi.nlm.nih.gov/articles/PMC10520970/)).

---

## 7. Anatomical Structures Affected

**Organ/system level:**
- **Primary:** Central nervous system — corticospinal tracts (spinal cord lateral columns), cerebellum (cortex, dentate nuclei, peduncles), optic nerve.
- **Secondary:** Peripheral nervous system (sensorimotor peripheral nerves), skeletal muscle (secondary mitochondrial myopathy with COX-deficient/ragged-red fibers), extraocular muscles (in PEO variant), bladder (neurogenic dysfunction), skeletal system (secondary orthopedic deformity — pes cavus, scoliosis from chronic spasticity/imbalance), auditory system (sensorineural hearing loss in a subset).
- Body systems: nervous system (primary), musculoskeletal, ophthalmologic, urologic.

**Tissue/cell level:** Corticospinal upper motor neuron axons (longest CNS axons, most vulnerable); cerebellar Purkinje cells and associated circuitry; retinal ganglion cell axons forming the optic nerve; peripheral motor/sensory axons; skeletal and extraocular muscle fibers.

**Subcellular level:** Mitochondria — specifically the **inner mitochondrial membrane** (where the m-AAA protease complex resides), affecting mitochondrial matrix protein quality control and mitochondrial DNA maintenance/nucleoid stability.

**UBERON terms (suggested):** UBERON:0002240 (spinal cord), UBERON:0002037 (cerebellum), UBERON:0001784 (lateral corticospinal tract) / UBERON:0002367 (corticospinal tract), UBERON:0000941 (optic nerve), UBERON:0001017 (central nervous system), UBERON:0000010 (peripheral nervous system), UBERON:0001134 (skeletal muscle tissue).

**GO Cellular Component:** GO:0005743 (mitochondrial inner membrane), GO:0005759 (mitochondrial matrix).

**Localization/laterality:** Bilateral and symmetric involvement of corticospinal tracts and cerebellar structures is characteristic (distinguishing from focal/asymmetric lesions); cerebellar atrophy in SPG7 has been reported to preferentially involve the **cerebellar hemispheres rather than the vermis** in at least one imaging series, and the "hot cross bun" pontine sign classically associated with MSA-C is **not** a typical SPG7 finding ([Human Genome Variation, PMC4785587](https://pmc.ncbi.nlm.nih.gov/articles/PMC4785587/)).

---

## 8. Temporal Development

- **Onset:** Adult-onset in the majority (mean 35.5 ± 14.3 years; typical range 20–40 years), but documented range extends from infancy to age 72 — making SPG7 a disorder with wide age-of-onset variability even within families (intrafamilial range 7–35 years documented).
- **Onset pattern:** Insidious/gradual, not acute or episodic.
- **Progression:** Slowly progressive, typically over years to decades. Pyramidal signs are usually earliest/most prevalent (89% at first exam, rising to 97%), with cerebellar features (66%→78%), dysarthria (42%→57%), dysphagia (15%→28%), amyotrophy (10%→30%), cognitive impairment (8%→19%), visual loss (7%→14%), ptosis (5%→17%), and dystonia (2%→11.5%) all increasing in frequency at longitudinal follow-up — demonstrating a **cumulative, multisystem progressive course** rather than a stable or episodic one.
- **Disease course pattern:** Chronic, progressive, lifelong; not relapsing-remitting.
- **Severity milestone:** Roughly one-third of affected individuals develop severe gait abnormality (wheelchair dependence in some) within 8–10 years of symptom onset.
- **Remission patterns:** None documented — SPG7 does not remit spontaneously; no disease-modifying treatment currently alters the progressive course.
- **Critical periods:** No defined developmental critical window; the length-dependent axonopathy mechanism implies risk accumulates with axon length and metabolic demand over time rather than at a discrete developmental stage, consistent with the typically adult (rather than pediatric) symptom onset despite the causal mutation being congenital.

---

## 9. Inheritance and Population

**Epidemiology:**
- Global prevalence of **all HSP forms**: ~3.6 per 100,000.
- Global prevalence of **SPG7 specifically**: **~0.22 per 100,000** (modeled estimate; [BMC Neurology 2022](https://bmcneurol.biomedcentral.com/articles/10.1186/s12883-022-02595-4); [PMC8944001](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8944001/)).
- SPG7 accounts for **5–12% of autosomal recessive HSP** cases and is recognized as a **common cause of previously undiagnosed adult-onset ataxia** ("SPG7 mutations are a common cause of undiagnosed ataxia," [Neurology 2015](https://www.neurology.org/doi/10.1212/WNL.0000000000001369)).

**Inheritance pattern:** **Autosomal recessive** (biallelic pathogenic variants required in the classic model). However:
- Multiple reports of **apparent autosomal dominant inheritance** with a single heterozygous variant have emerged, and "the possibility of autosomal dominant inheritance remains controversial" per GeneReviews.
- Much of this apparent dominance is now attributed to (1) **pseudodominance** — an autosomal recessive disorder appearing across two generations because the founder allele (e.g., p.Ala510Val, carrier frequency ~1%) is common enough that an affected homozygote's partner is frequently also a carrier, producing affected offspring without consanguinity; and (2) **"missing heritability"** — a second pathogenic allele in a deep intronic or other non-coding region that is missed by exome sequencing but detectable by genome sequencing ([PMC12883507](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12883507/); "Evidence for non-Mendelian inheritance in spastic paraplegia 7," [medRxiv](https://www.medrxiv.org/content/10.1101/2020.09.25.20176032.full.pdf)).
- **Digenic inheritance** with **AFG3L2** is a separate, recently described mechanism producing a related but distinct motor-neuron/cerebellar phenotype through combined heterozygosity across the two m-AAA protease genes.

**Penetrance/expressivity:** Full biallelic genotypes are generally considered highly, though not completely, penetrant; monoallelic (heterozygous) carriers are typically unaffected clinically but may show subtle imaging changes (reduced white matter integrity in the corpus callosum on DTI in heterozygote carriers). Expressivity is markedly variable — intrafamilial variation in age of onset (7–35 years) and in phenotype (pure spastic paraplegia through complicated spastic ataxia) is well documented even among relatives sharing the same genotype.

**Genetic anticipation:** Not established/reported for SPG7 (unlike triplet-repeat spinocerebellar ataxias).

**Germline mosaicism:** Not specifically documented in the literature reviewed for SPG7.

**Founder effects / carrier frequency:** p.Ala510Val is a recurrent, likely founder-associated allele with carrier frequency up to ~1% in general populations; p.Leu78Ter shows elevated frequency in South Asian gnomAD subpopulation (MAF 0.0028) and was most frequent in a Hungarian cohort — suggesting population-specific variant spectra.

**Consanguinity:** As an autosomal recessive disorder, parental consanguinity is a recognized risk factor and diagnostic clue (elicited in the family history per GeneReviews suggestive-findings criteria).

**Population demographics:** No strong ethnic-specific prevalence differences beyond the founder-allele distribution noted above; affects males and females roughly equally (no established sex-ratio skew, consistent with autosomal — not X-linked — inheritance). Age distribution reflects the adult-onset pattern described above.

---

## 10. Diagnostics

**Clinical suggestive findings** (GeneReviews): adult-onset (mean 35.5 years) uncomplicated or complicated spastic paraplegia, cerebellar ataxia, and/or optic nerve atrophy on exam; brain MRI with cerebellar atrophy or corticospinal/frontal white-matter changes on DTI; family history compatible with autosomal recessive inheritance (affected siblings, consanguinity).

**Establishing the diagnosis:** Biallelic pathogenic *SPG7* variants identified by molecular genetic testing in a proband with suggestive findings.

**Molecular genetic testing:**
- **Multigene panel** (SPG7 + other HSP genes) — first-line, focused.
- **Exome sequencing** — detects >90% of pathogenic variants (option when panel is uninformative or phenotype is broad).
- **Genome sequencing** — recommended when only one pathogenic allele is found by exome, to detect deep intronic/non-coding variants.
- **Deletion/duplication analysis** (qPCR, long-range PCR, MLPA, targeted array) — needed for the <10% of alleles that are CNVs.

**Imaging:**
- Brain MRI: cerebellar atrophy (reported as preferentially hemispheric rather than vermian in some series) and/or cortical atrophy; diffusion tensor imaging shows white matter changes in frontal lobes, corticospinal tracts, and brainstem.
- The "hot cross bun" pontine sign (classic for MSA-C) is not a typical SPG7 finding, aiding radiological differentiation.

**Laboratory/histopathology:**
- Skeletal muscle biopsy in severely affected individuals: **ragged-red fibers** and **cytochrome c oxidase (COX)-deficient fibers**, reflecting secondary mitochondrial dysfunction and multiple mtDNA deletions (up to 38–97% heteroplasmy in individual respiratory-deficient fibers).
- Optical coherence tomography (OCT): useful for detecting subclinical optic neuropathy.

**Differential diagnosis:** Other AR/AD-HSP subtypes; spinocerebellar ataxias (SCA1, 2, 3, 6, 7, 17; DRPLA); **AFG3L2-related autosomal recessive SCA** (shares the same pathway); other mitochondrial disorders with overlapping ptosis/ophthalmoplegia/optic atrophy (e.g., POLG-related disease, which also causes multiple mtDNA deletions); treatable mimics such as dopa-responsive dystonia and specific metabolic disorders should be excluded given management implications.

**Screening:** No population newborn-screening program exists (adult-onset disorder); carrier/cascade testing and prenatal/preimplantation genetic testing are available once family-specific variants are identified.

**Suggested NCIT terms:** NCIT:C15709 (Genetic Testing) generally; specific molecular diagnostic procedures map to NCIT terms for exome sequencing, genome sequencing, and muscle biopsy as applicable.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** SPG7 is generally not associated with reduced life expectancy from the core neurodegenerative process itself; disability rather than mortality is the primary burden. No specific survival/mortality statistics were located in the sources reviewed (consistent with a slowly progressive, non-lethal neurodegenerative disorder in most cases, though secondary complications of severe disability — e.g., aspiration from dysphagia — could contribute to morbidity/mortality risk in advanced disease).
- **Morbidity/functional outcomes:** Progressive gait impairment, with severe gait abnormality in ~1/3 of patients by 8–10 years post-onset; a subset become wheelchair-dependent. Multisystem morbidity accumulates over the disease course (see §3/§8 frequency table): dysarthria, dysphagia (aspiration risk), amyotrophy, cognitive impairment, visual loss, ptosis, and dystonia.
- **Complications:** Aspiration pneumonia risk from dysphagia; bladder dysfunction complications (UTIs); orthopedic complications (contractures, scoliosis, pes cavus) from chronic spasticity/gait abnormality; social/cognitive impact from cerebello-cortical circuit dysfunction affecting attention, executive function, and social cognition.
- **Prognostic factors:** Genotype correlates with phenotype trajectory — biallelic loss-of-function variants predict a more pyramidal/optic-atrophy-predominant, potentially more severe course; missense variants (notably p.Ala510Val) correlate with a more cerebellar-ataxia-predominant course with somewhat later onset.
- **Quality of life measurement:** No SPG7-specific validated QoL instrument identified; standardized ataxia severity scales (SARA, ICARS, BARS) are used for longitudinal tracking rather than generic QoL tools in the surveillance framework.

---

## 12. Treatment

**No disease-modifying cure or specific drug therapy exists.** Management is entirely **supportive and multidisciplinary**, involving neurology, ophthalmology, occupational/physical therapy, physiatry, orthopedics, nutrition, speech-language pathology, urology, social work, psychology, and clinical genetics.

**Pharmacotherapy for spasticity** (symptomatic, not disease-modifying):
- Oral antispasticity agents: baclofen, tizanidine, dantrolene, diazepam (NCIT:C529 Baclofen, general pharmacotherapy class NCIT:C15986).
- Botulinum toxin injections for focal spasticity.
- Intrathecal baclofen pump for severe, refractory spasticity.

**Rehabilitative/supportive care:**
- Physical therapy: balance exercises, gait training, muscle strengthening (NCIT:C15302, Physical Therapy).
- Occupational therapy: adaptive devices (weighted utensils, dressing aids) (NCIT:C15302-adjacent).
- Mobility aids: canes, walkers, motorized wheelchairs; home modifications (grab bars, ramps).
- Speech-language therapy for dysarthria; augmentative/alternative communication evaluation.
- Dysphagia management: feeding therapy, video esophagram-guided diet modification, gastrostomy tube for high aspiration risk.
- Vision: corrective lenses, prisms, low-vision services for optic atrophy.
- Bladder management: antimuscarinics, beta-3 agonists, botulinum toxin per urology.
- Orthopedic: orthotic devices for pes cavus/scoliosis.
- Cognitive/psychiatric: standard pharmacotherapy and psychotherapy/neuropsychological rehabilitation as needed.

**Experimental/investigational approaches:**
- **Pharmacological rescue studies** in patient-derived iPSC neurons (high-throughput screening) have identified small molecules that reverse SPG7-associated mitochondrial and neuronal phenotypic defects in vitro — an early-stage discovery platform, not yet a clinical therapy ([Frontiers Neuroscience 2023, PMC10520970](https://pmc.ncbi.nlm.nih.gov/articles/PMC10520970/)).
- **Digital-motor outcome measures** are being developed specifically as candidate endpoints for future SPG7 clinical trials, reflecting active trial-readiness research even though no SPG7-specific disease-modifying trial was identified as completed/ongoing ("Patient-Relevant Digital-Motor Outcomes for Clinical Trials in Hereditary Spastic Paraplegia Type 7," [Neurology 2024](https://www.neurology.org/doi/10.1212/WNL.0000000000209887)).
- Coenzyme Q10/mitochondrial cofactor supplementation strategies have been trialed in **other** mitochondrial diseases (e.g., NCT00432744, Phase III CoQ10 in mitochondrial disease; NCT01126697, CoQ10 + lisinopril in muscular dystrophies) but no SPG7-specific CoQ10/idebenone trial was located in this search — this represents a plausible but currently unvalidated extrapolated intervention for the SPG7 mitochondrial mechanism.
- No approved gene therapy, cell therapy, or targeted molecular therapy currently exists for SPG7 in humans (an experimental **intramuscular viral delivery of paraplegin** rescued peripheral axonopathy in the mouse model — a proof-of-concept gene-replacement study, not yet translated to human trials — [JCI 2005](https://www.jci.org/articles/view/26210)).

**Genotype-informed considerations:** No current pharmacogenomic (CPIC/PharmGKB) guidance specific to SPG7 was identified.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (no modifiable environmental cause); the relevant primary-prevention lever is **genetic**: carrier screening and reproductive genetic counseling in families/populations with known pathogenic alleles (notably relevant given the ~1% carrier frequency of p.Ala510Val).
- **Secondary prevention:** Early molecular diagnosis via genetic testing in individuals with suggestive adult-onset spastic ataxia/optic atrophy enables earlier initiation of supportive/rehabilitative care and surveillance, and informs family counseling before further affected pregnancies occur.
- **Genetic counseling:** Sibling recurrence risk 25% (affected) / 50% (carrier) / 25% (unaffected, non-carrier) when both parents are known heterozygotes; offspring of an affected individual are obligate heterozygous carriers (and could be at risk of being affected if the partner also carries a pathogenic allele, given founder-allele carrier frequency). Prenatal and preimplantation genetic testing are available once family-specific variants are identified.
- **Screening programs:** No population-based newborn screening exists for SPG7 (adult-onset, non-emergent phenotype); carrier screening is family/variant-specific rather than population-panel-based at this time, though its relatively high founder-allele carrier frequency could support future consideration in expanded carrier panels.
- **Behavioral/lifestyle interventions:** No specific risk-reducing lifestyle intervention is established; general good mitochondrial-health practices (avoidance of mitochondrial-toxic drugs where possible, regular exercise/physical therapy to maintain function) are reasonable extrapolated supportive measures rather than evidence-based disease-modifying prevention.
- **Public health/environmental interventions:** Not applicable — SPG7 has no environmental or infectious trigger requiring public health intervention.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *SPG7* orthologs show stringent 1:1 orthology across vertebrates: human (*Homo sapiens*, NCBITaxon:9606), mouse (*Mus musculus*, NCBITaxon:10090), rat (*Rattus norvegicus*, NCBITaxon:10116), and zebrafish (*Danio rerio*, NCBITaxon:7955; UniProt E7F2S4).
- **Gene orthologs:** Mouse *Spg7* (MGI:2385906); Drosophila paraplegin ortholog (studied via null-mutant/deletion models).
- **Natural disease in other species:** No naturally occurring companion-animal or wildlife SPG7-orthologous disease was identified in this search (OMIA not specifically queried/found with a hit); the available animal data are all **engineered/induced models** (knockouts), not natural disease.
- **Comparative biology:** The m-AAA protease mechanism (paraplegin-AFG3L2 complex) and its role in mitochondrial protein quality control, calcium homeostasis, and axonal maintenance is evolutionarily conserved from yeast (yeast m-AAA protease orthologs originally characterized the pathway) through Drosophila, zebrafish, mouse, and human — underscoring deep conservation of the disease mechanism.
- **Zoonotic potential/cross-species transmission:** Not applicable — SPG7 is a non-infectious, genetic, non-transmissible disorder.

---

## 15. Model Organisms

| Model | Type | Key findings | Fidelity/limitations |
|---|---|---|---|
| **Paraplegin-deficient mouse** (Ferreirinha et al. 2004; [JCI](https://www.jci.org/articles/view/20138)) | Genetic knockout (mammalian) | Slow, progressive motor impairment (rotarod deficits); distal axonopathy of spinal and peripheral axons with axonal swelling and degeneration. Temporal sequence: swollen mitochondria in spinal cord axons at 4.5 months → axonal swelling at 8 months → degeneration at 15 months. Swellings show massive accumulation of organelles/neurofilaments (impaired anterograde transport); retrograde transport delayed in symptomatic mice. | RECAPITULATES the length-dependent axonal degeneration and mitochondrial-transport mechanism; a mammalian model with strong construct and face validity for the corticospinal/peripheral axonopathy arm. |
| **Intramuscular AAV-paraplegin gene delivery in paraplegin-null mice** ([JCI 2005](https://www.jci.org/articles/view/26210)) | Induced/rescue model | Viral delivery of paraplegin rescued peripheral axonopathy — proof-of-concept for gene-replacement therapy. | RESCUES peripheral (not central) axonopathy; demonstrates causal sufficiency of paraplegin restoration. |
| **Drosophila SPG7-null mutant** ([Cell Death & Disease 2018](https://www.nature.com/articles/s41419-018-0365-8); [PMC5833341](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5833341/)) | Genetic knockout (invertebrate) | Mitochondrial dysfunction, shortened lifespan, neuronal and muscular degeneration; reduced respiratory chain complex I and II activity; electron-dense material accumulation in flight-muscle mitochondria; severely swollen/dysmorphic mitochondria in photoreceptor synaptic terminals. | RECAPITULATES core mitochondrial bioenergetic and morphological defects; useful for rapid genetic/pharmacological screening; limited translational fidelity for CNS-specific corticospinal phenotype (invertebrate nervous system). |
| **Zebrafish spg7 ortholog** (UniProt E7F2S4) | Genetic (potential knockout/knockdown model) | Confirmed conserved 1:1 ortholog present; disease-specific phenotyping less thoroughly documented in the sources reviewed compared to other HSP genes (e.g., spastizin/SPG15 zebrafish models are more developed). | Model existence confirmed by orthology; disease-modeling literature less extensive than mouse/Drosophila for SPG7 specifically. |
| **Astrocyte-specific m-AAA protease conditional knockout mouse** ([PMC6618114](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6618114/)) | Conditional genetic knockout (glial-specific) | Reveals a **glial (astrocyte) contribution** to neurodegeneration in m-AAA protease deficiency, expanding the mechanism beyond cell-autonomous neuronal axonopathy. | PARTIALLY_RECAPITULATES — isolates the astrocytic arm; complements but does not replace the neuron-autonomous mouse knockout model. |
| **Combined SPG7 + AFG3L2 dysfunction animal models** (cited in digenic-inheritance study, [BMC Medicine 2025](https://link.springer.com/article/10.1186/s12916-026-04805-z)) | Genetic (double dysfunction) | Early-onset axonal degeneration, prominent cerebellar degeneration with Purkinje cell and parallel fiber loss, reactive astrogliosis, defective mitochondria. | RECAPITULATES the more severe digenic human phenotype (motor neuron + cerebellar disease); supports the synergistic pathogenic model for combined SPG7/AFG3L2 heterozygosity. |
| **Patient-derived iPSC/fibroblast lines** ([PMC7469654](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7469654/); [PMC10520970](https://pmc.ncbi.nlm.nih.gov/articles/PMC10520970/)) | Human cellular model (in vitro, IN_VITRO evidence class) | SPG7 patient-derived neurons/fibroblasts show mitochondrial functional deficits **not seen** in SPAST-mutant (SPG4) patient lines, establishing SPG7 as mechanistically distinct within HSP; used as a platform for high-throughput pharmacological rescue screening. | HIGH translational relevance (human genetic background) but lacks the in vivo axonal-length/circuit context of animal models — best used in combination with the mouse model. |

**Research applications:** These models collectively support study of (1) the temporal sequence of mitochondrial dysfunction preceding axonal degeneration, (2) axonal transport impairment as a proximate mechanism, (3) cell-autonomous (neuronal) vs. non-cell-autonomous (astrocytic) contributions, (4) digenic/synergistic genetic interactions (SPG7+AFG3L2), and (5) small-molecule/gene-therapy rescue strategies as a translational pipeline toward future SPG7 clinical trials.

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Domain | Suggested terms |
|---|---|
| Disease | MONDO (SPG7-related neurologic disorder; exact MONDO CURIE not confirmed in this search — verify via OAK/MONDO lookup before curating), OMIM:607259 |
| Gene | HGNC symbol SPG7 (paraplegin), OMIM:602783 |
| Phenotypes (HP) | Spastic paraplegia, cerebellar ataxia, dysarthria, dysphagia, muscle wasting/amyotrophy, optic atrophy, ptosis, dystonia, nystagmus, ophthalmoparesis, peripheral neuropathy, pes cavus, scoliosis, hearing loss, urinary urgency, hyperreflexia, Babinski sign |
| GO Biological Process | mitochondrial protein processing/quality control, mitochondrial calcium ion homeostasis, anterograde/retrograde axonal transport, mitochondrion organization |
| GO Molecular Function | ATP-dependent peptidase activity, metalloendopeptidase activity |
| GO Cellular Component | mitochondrial inner membrane, mitochondrial matrix |
| CL cell types | upper motor neuron/corticospinal neuron, Purkinje cell, retinal ganglion cell, skeletal myocyte, astrocyte |
| UBERON | spinal cord, cerebellum, corticospinal tract, optic nerve, skeletal muscle tissue |
| NCIT treatments | Pharmacotherapy (C15986), Physical Therapy (C15302), Genetic Counseling (C15240), Genetic Testing |
| Model organisms (NCBITaxon) | Mouse (10090), Drosophila (7227, implied), Zebrafish (7955) |

---

### Sources
- [SPG7-Related Neurologic Disorder – GeneReviews (NCBI Bookshelf NBK1107)](https://www.ncbi.nlm.nih.gov/books/NBK1107/)
- [OMIM #607259 – Spastic Paraplegia 7, Autosomal Recessive](https://omim.org/entry/607259)
- [OMIM #602783 – SPG7 Matrix AAA Peptidase Subunit, Paraplegin](https://www.omim.org/entry/602783)
- [GARD – Hereditary spastic paraplegia 7](https://rarediseases.info.nih.gov/diseases/4927/hereditary-spastic-paraplegia-7)
- [NIH GTR – Hereditary spastic paraplegia 7](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1846564/)
- [MalaCards – Spastic Paraplegia 7, Autosomal Recessive](https://www.malacards.org/card/spastic_paraplegia_7_autosomal_recessive)
- [Expanding the Phenotypic Spectrum of SPG7 Rare Damaging Variants: Insights From a Hungarian Cohort (PMC12215234)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12215234/)
- [A Novel SPG7 Gene Pathogenic Variant in a Cypriot Family (PMC8793673)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8793673/)
- [Digenic inheritance of mutations in SPG7 and AFG3L2 causes motor neuron and cerebellar disorders – BMC Medicine 2025](https://link.springer.com/article/10.1186/s12916-026-04805-z)
- [Digenic SPG7/AFG3L2 – medRxiv preprint](https://www.medrxiv.org/content/10.1101/2025.07.05.24312261.full.pdf)
- [An integrated modelling methodology for estimating global incidence and prevalence of HSP subtypes SPG4, SPG7, SPG11, SPG15 – BMC Neurology 2022](https://bmcneurol.biomedcentral.com/articles/10.1186/s12883-022-02595-4) / [PMC8944001](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8944001/)
- [SPG7 mutations are a common cause of undiagnosed ataxia – Neurology 2015](https://www.neurology.org/doi/10.1212/WNL.0000000000001369)
- [Evidence for non-Mendelian inheritance in spastic paraplegia 7 – medRxiv](https://www.medrxiv.org/content/10.1101/2020.09.25.20176032.full.pdf)
- [Identification of an additional deep intronic splice variant prompts critical evaluation of SPG7 inheritance (PMC12883507)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12883507/)
- [Loss of the Drosophila m-AAA mitochondrial protease paraplegin – Cell Death & Disease 2018](https://www.nature.com/articles/s41419-018-0365-8) / [PMC5833341](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5833341/)
- [Axonal degeneration in paraplegin-deficient mice is associated with abnormal mitochondria and impairment of axonal transport – JCI](https://www.jci.org/articles/view/20138)
- [Intramuscular viral delivery of paraplegin rescues peripheral axonopathy – JCI 2005](https://www.jci.org/articles/view/26210)
- [m-AAA proteases, mitochondrial calcium homeostasis and neurodegeneration – Cell Research (PMC5835776)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5835776/)
- [Astrocyte-specific deletion of the mitochondrial m-AAA protease reveals glial contribution to neurodegeneration (PMC6618114)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6618114/)
- [Predominant cerebellar phenotype in spastic paraplegia 7 (SPG7) – Human Genome Variation (PMC4785587)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4785587/)
- [Novel genotype-phenotype and MRI correlations in a large cohort of patients with SPG7 mutations – Neurology Genetics (PMC6244025)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6244025/)
- [Cerebello-Cortical Alterations Linked to Cognitive and Social Problems in SPG7 (PMC7053515)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7053515/)
- [Mutations in the SPG7 gene cause chronic progressive external ophthalmoplegia through disordered mitochondrial DNA maintenance – Brain 2014](https://academic.oup.com/brain/article/137/5/1323/335381)
- [Spastic Paraplegia Type 7 Is Associated with Multiple Mitochondrial DNA Deletions (PMC3899233)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3899233/)
- [Mitochondrial Function in Hereditary Spastic Paraplegia: Deficits in SPG7 but Not SPAST Patient-Derived Stem Cells (PMC7469654)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7469654/)
- [Pharmacological rescue of mitochondrial and neuronal defects in SPG7 patient neurons using high throughput assays – Frontiers Neuroscience 2023 (PMC10520970)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10520970/)
- [Patient-Relevant Digital-Motor Outcomes for Clinical Trials in Hereditary Spastic Paraplegia Type 7 – Neurology 2024](https://www.neurology.org/doi/10.1212/WNL.0000000000209887)
- [Ataxia UK – SPG7 patient information PDF](https://www.ataxia.org.uk/wp-content/uploads/2025/01/SPG7-1.pdf)
- [ClinicalTrials.gov NCT00432744 – Phase III Trial of Coenzyme Q10 in Mitochondrial Disease](https://clinicaltrials.gov/study/NCT00432744)
- [ClinicalTrials.gov NCT01126697 – Coenzyme Q10 and Lisinopril in Muscular Dystrophies](https://clinicaltrials.gov/study/NCT01126697)
- [UniProt E7F2S4 – zebrafish spg7 ortholog](https://www.uniprot.org:443/uniprot/E7F2S4)
- [MGI:2385906 – mouse Spg7 gene detail](https://www.informatics.jax.org/marker/MGI:2385906)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 13 |
| References weighed for topical relevance | 4 |
| On topic | 2 |
| Off topic | 0 |

4 of 17 references resolved; the rest could not be looked up either way.
