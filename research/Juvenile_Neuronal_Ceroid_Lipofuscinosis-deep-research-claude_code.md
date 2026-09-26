---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-08T18:10:05.511346'
end_time: '2026-08-08T18:30:22.953577'
duration_seconds: 1217.44
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: "Juvenile Neuronal Ceroid Lipofuscinosis \u2014 the genetically heterogeneous\
    \ juvenile-onset NCL grouping, MONDO:0019262, distinct from CLN3 disease MONDO:0008767"
  mondo_id: MONDO:0019262
  category: Mendelian onset-defined grouping
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    system_prompt: 'Research the exact ontology entity MONDO:0019262: juvenile neuronal
      ceroid lipofuscinosis as a genetically heterogeneous juvenile-onset grouping.
      It is explicitly distinct from CLN3 disease / NCL3 / MONDO:0008767. CLN3 is
      one classic subtype, not the whole target. Establish gene-by-gene which NCL
      genotypes have defensible juvenile-onset presentations, and distinguish late-infantile
      and adult forms. Do not re-anchor the report to MONDO:0008767. Produce a comprehensive,
      citation-rich report directly in Markdown, prioritizing primary literature and
      exact identifiers.'
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5
  web_search_requests: 11
  num_turns: 83
  total_cost_usd: 6.4927565
  session_id: a732201e-7d30-437d-8a12-1fb882b7288c
  stop_reason: end_turn
citation_count: 49
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Juvenile Neuronal Ceroid Lipofuscinosis — the genetically heterogeneous juvenile-onset NCL grouping, MONDO:0019262, distinct from CLN3 disease MONDO:0008767
- **MONDO ID:** MONDO:0019262 (if available)
- **Category:** Mendelian onset-defined grouping

## Research Objectives

Please provide a comprehensive research report on **Juvenile Neuronal Ceroid Lipofuscinosis — the genetically heterogeneous juvenile-onset NCL grouping, MONDO:0019262, distinct from CLN3 disease MONDO:0008767** covering all of the
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

# Juvenile Neuronal Ceroid Lipofuscinosis (MONDO:0019262)

## A genetically heterogeneous, onset-defined NCL grouping — *not* CLN3 disease

**Research report for knowledge-base curation**
Compiled 2026-08-08. All ontology records retrieved live from OLS4/MONDO; literature retrieved via NCBI E-utilities and PMC.

---

## 0. Scope discipline — read this first

This report is about **MONDO:0019262**, an **age-of-onset-defined grouping class** that spans multiple NCL genotypes. It is **not** about MONDO:0008767 (neuronal ceroid lipofuscinosis 3 / CLN3 disease / OMIM:204200), which is **one member** of the grouping.

The distinction is asserted in MONDO itself. The class carries an explicit editor note that it **"groups different neuronal ceroid lipofuscinoses despite historical merging with CLN3 disease"**, and its textual definition is genotype-agnostic:

> "A genetically heterogeneous group of neuronal ceroid lipofuscinoses (NCLs) typically characterized by onset at early school age with vision loss due to retinopathy, seizures and the decline of mental and motor capacities."
> — MONDO:0019262 definition (OLS4, MONDO current release)

The historical conflation is real and is the single largest curation hazard here. The synonym list on MONDO:0019262 still carries **"Batten disease"**, **"Spielmeyer-Vogt disease"**, and **"JNCL"** — all three of which are, in most of the clinical literature, used as names for *CLN3 disease specifically*. Any literature search on "juvenile NCL", "JNCL", or "Batten disease" will return a corpus that is **~80–90% CLN3**, and an uncritical curation pass will silently re-anchor the entry onto MONDO:0008767. **This is the Named Entity Confusion risk for this entity, and it runs through synonym aliasing rather than through a wrong-gene deep-research report.**

The correct model of MONDO:0019262 is: *"a juvenile-onset presentation of an NCL, from any of several causal genes."* CLN3 is the modal member, not the definition.

---

## 1. Disease Information

### 1.1 Overview

The neuronal ceroid lipofuscinoses (NCLs) are a group of inherited, mostly autosomal recessive, lysosomal-storage neurodegenerative disorders unified by the intracellular accumulation of autofluorescent, PAS- and Sudan-black-positive "ceroid-lipofuscin" storage material in neurons and extraneural tissue. They have been subclassified since Santavuori's era along two orthogonal axes:

1. **Age of onset** — congenital, infantile, late-infantile, **juvenile**, adult (Kufs)
2. **Causal gene** — CLN1–CLN8, CLN10–CLN14 (CLN9 is withdrawn; see §4.6)

MONDO:0019262 is a class on the **first** axis. It denotes the cohort of NCL patients whose first symptom appears in the **juvenile window — conventionally ~5–10 years of age** (some authors use 4–10 or extend to early adolescence) — regardless of which gene is mutated.

The clinical gestalt of the juvenile window is distinctive and largely gene-independent:

- **Vision is usually the herald symptom.** A previously normal school-age child presents to an ophthalmologist with rapidly progressive central visual loss and a pigmentary retinopathy/bull's-eye maculopathy. Frequent initial misdiagnoses are Stargardt disease, retinitis pigmentosa, or cone–rod dystrophy.
- **Cognitive and behavioural decline follows** within 1–3 years — school failure, then frank dementia, often with a striking psychiatric prodrome (anxiety, psychosis, hallucinations) in the CLN3 subgroup.
- **Seizures** (generalised tonic-clonic and myoclonic) begin typically age 8–13.
- **Motor decline** — extrapyramidal (parkinsonism, dystonia, rigidity) plus cerebellar ataxia and pyramidal signs — leads to loss of ambulation in the second decade.
- **Death** in the late second to third decade for CLN3; earlier or later for other genotypes.

The critical exceptions to this gestalt are diagnostically load-bearing and are detailed gene-by-gene in §4: **CLN8/EPMR ("Northern epilepsy") presents with seizures and no visual failure**, and **some CLN6 juvenile patients present with ataxia/spasticity and explicitly no visual loss**.

### 1.2 Key identifiers

| Resource | Identifier | Note |
|---|---|---|
| **MONDO** | **MONDO:0019262** | The target entity. Definition and editor note quoted above. |
| Orphanet | **ORPHA:79264** | Primary xref; the Orphanet grouping "Juvenile neuronal ceroid lipofuscinosis". |
| DOID | DOID:0050756 | |
| GARD | GARD:0004938 | |
| MedDRA | MedDRA:10052073 | |
| SNOMED CT | SCTID:61663001 | |
| ICD-11 Foundation | icd11.foundation:1716107919 | |
| NANDO | NANDO:1200154, NANDO:2201243 | Japanese rare-disease nomenclature |
| ICD-10 | E75.4 (group-level, "Neuronal ceroid lipofuscinosis") | ⚠️ *Group-level code shared with all NCLs; not juvenile-specific. Not independently re-verified this session.* |
| OMIM | **none** | ⚠️ **Important:** MONDO:0019262 has **no OMIM xref**, because OMIM is organised gene-first. Every OMIM number in this space (204200, 256730, 204500, 256731, 601780, 610951, 600143, 610127, 614706, 606693, 615362, 611726) belongs to a *gene*-defined entity, not to the onset grouping. Do not attach OMIM:204200 to this entry — that is MONDO:0008767. |

**Contrast — MONDO:0008767 (do not conflate):** label "neuronal ceroid lipofuscinosis 3"; definition *"A condition associated with mutation(s) in the CLN3 gene, encoding battenin…"*; xrefs OMIM:204200, Orphanet:228346, MEDGEN:155549, NCIT:C61258, UMLS:C0751383, DOID:0110731, GARD:0005897, NORD:843; material basis in germline mutation in CLN3 (HGNC:2074).

### 1.3 MONDO hierarchy and children (retrieved live)

**Parents of MONDO:0019262:**
- MONDO:0016295 — neuronal ceroid lipofuscinosis
- MONDO:0020143 — cerebral lipidosis with dementia

**Direct children returned by OLS4** (`/children` and `/descendants` both returned the same four):

| Child CURIE | Label | Gene | Note |
|---|---|---|---|
| MONDO:0979341 | juvenile neuronal ceroid lipofuscinosis 1 | *PPT1/CLN1* | syn. "juvenile CLN1 disease"; xref Orphanet:699739 |
| MONDO:0979345 | juvenile neuronal ceroid lipofuscinosis 2 | *TPP1/CLN2* | syn. "juvenile CLN2 disease"; xref Orphanet:699769 |
| MONDO:0012188 | neuronal ceroid lipofuscinosis 9 | *(none — withdrawn)* | see §4.6 |
| MONDO:0017809 | parkinsonism due to ATP13A2 deficiency | *ATP13A2/CLN12* | Kufor-Rakeb syndrome |

Plus, confirmed by direct class lookup (it is dual-parented and was missed by the descendants call):

| MONDO:0979346 | juvenile neuronal ceroid lipofuscinosis 3 | *CLN3* | syn. "juvenile CLN3 disease"; xrefs Orphanet:699780, MEDGEN:1897244, UMLS:C6012317. **Parents: MONDO:0019262 *and* MONDO:0008767.** |

**Two curation-relevant ontology observations:**

1. **MONDO:0979346 is the correct bridging term** between the onset grouping and CLN3. It sits under *both* MONDO:0019262 and MONDO:0008767. This is exactly the right modelling: "juvenile CLN3 disease" is simultaneously a juvenile NCL and a form of CLN3 disease. If a KB entry needs to reference "the CLN3 member of the juvenile grouping", **MONDO:0979346 — not MONDO:0008767 — is the term.**
2. **The grouping is under-populated relative to the literature.** Orphanet has minted a `juvenile CLNx disease` series (ORPHA:699739 = juvenile CLN1, ORPHA:699769 = juvenile CLN2, ORPHA:699780 = juvenile CLN3), and MONDO has imported three of them. But juvenile-onset presentations are well documented for **CLN5, CLN6, CLN7/MFSD8, CLN8, and CLN10/CTSD** (§4), and **no corresponding MONDO children exist**. MONDO:0019262's asserted extension is therefore substantially narrower than its textual definition. This is a genuine ontology gap worth reporting upstream, and it means a KB entry for this grouping should enumerate members from the literature rather than from the MONDO child list.

### 1.4 Synonyms

**Safe (onset-neutral):** juvenile NCL; JNCL; juvenile neuronal ceroid lipofuscinosis; juvenile-onset neuronal ceroid lipofuscinosis; juvenile Batten disease *(with caution)*.

**Hazardous — carried by MONDO but in practice CLN3-specific in the literature:** "Batten disease"; "Spielmeyer-Vogt disease"; "Spielmeyer-Sjögren disease"; "Vogt-Spielmeyer disease"; "Batten-Spielmeyer-Vogt disease". Note that "Vogt Spielmeyer disease" and "Spielmeyer Sjogren disease" are *also* synonyms on MONDO:0008767 — the synonym sets overlap, which is the mechanical root of the conflation.

### 1.5 Data provenance

Information in this report is **aggregated disease-level** (ontologies, OMIM/Orphanet, GeneReviews, cohort studies, case series), not individual-patient/EHR-derived. There is no EHR-scale phenotyping resource for this grouping; the DEM-CHILD and NCL Resource (UCL) patient/mutation databases are the closest thing to patient-level aggregation, and the Rochester UBDRS natural-history cohort is patient-level but **CLN3-restricted**.

---

## 2. Etiology

### 2.1 Causal factors

Monogenic, overwhelmingly **autosomal recessive**, biallelic loss-of-function or hypomorphic variants in a lysosomal/endolysosomal gene. There is **no infectious, toxic, or environmental etiology**. The one non-recessive member of the wider NCL family, autosomal-dominant *DNAJC5*/CLN4, is adult-onset and is **not** a member of this grouping (§4.7).

The unifying etiological statement for the grouping is a **quantitative** one rather than a gene-level one: *juvenile onset arises when residual function of an NCL gene product is reduced enough to cause progressive storage, but not so severely as to produce infantile or late-infantile presentation.* This "residual-activity gradient" model is the single most important mechanistic concept for MONDO:0019262 and is supported directly for CLN2:

> "loss of function variants abolishing TPP1 enzyme activity lead to CLN2 disease, whereas variants that diminish TPP1 enzyme activity lead to SCAR7."
> — Sun Y et al., *Hum Mutat* 2013;34(5):706-13 (PMID:23418007)

and is the framing of the comprehensive mutation-spectrum review:

> "Different mutations within the NCL spectrum can cause variable disease severity. The NCLs exemplify both phenotypic convergence or mimicry and phenotypic divergence. For example, mutations in CLN5, CLN6, MFSD8, or CLN8 can underlie the clinically similar late infantile variant NCL disease. Phenotypic divergence is exemplified by different CLN8 mutations giving rise to two very different diseases, the mild CLN8 disease, EPMR (progressive epilepsy with mental retardation), and the more severe CLN8 disease, late infantile variant."
> — Kousi M, Lehesjoki A-E, Mole SE. *Hum Mutat* 2012;33(1):42-63 (PMID:21990111)

**Practical corollary for curation:** the causal chain for this grouping should be modelled as *[gene-specific hypomorphic lesion] → [partial residual protein function] → [slower storage accumulation] → [juvenile-window onset]*, with the gene as a substitutable slot — this is structurally analogous to a `lysosomal_substrate_accumulation` module conformer with the *severity/timing* dimension made explicit.

### 2.2 Genetic risk factors

- **Causal variants:** biallelic in *PPT1, TPP1, CLN3, CLN5, CLN6, MFSD8, CLN8, CTSD, ATP13A2* (see §4 for the defensibility grading).
- **Consanguinity** is a major risk factor for all recessive members and is documented in most non-CLN3 juvenile reports (Cypriot CLN6 families, Chinese CLN6 family, Somali CTSD sibship, Turkish/Roma CLN7 cohorts).
- **Founder effects** are strong and population-specific (§9.3): the CLN3 1.02-kb deletion in Northern Europeans; *CLN5* p.Tyr392* in Finns; *CLN8* p.Arg24Gly in Finns (EPMR); *MFSD8* p.Thr294Lys in Roma of the former Czechoslovakia; *PPT1* p.Arg122Trp in Finns.
- **No established common-variant susceptibility loci.** There is no GWAS signal for NCL — this is a Mendelian entity and GWAS Catalog/PheGenI are not informative sources here.

### 2.3 Modifier genes

Formally identified genetic modifiers are **not established** for the juvenile NCLs. There is, however, strong indirect evidence of modification:

- Intrafamilial variability with an identical genotype is documented. In a consanguineous Chinese *CLN6* family, "Both patients exhibited seizures and progressive psychomotor decline and mental deterioration without visual impairment. They had different ages of onset, although they carried the same missense mutation. The affected female showed a pronounced abnormal MRI signal in the bilateral hippocampus, while her younger brother only showed a very slight abnormal signal." (*Neurodegener Dis* 2021;21(5-6):126-131; PMID:35609511)
- Cross-CLN protein interdependence is a plausible modifier mechanism: "Loss of CLN3 has been shown to affect PPT1, TPP1, CLN5, and CTSD" (Zhang Y et al., *CNS Neurosci Ther* 2025;31(2):e70261; PMID:39925015). A hypomorphic allele in a second NCL gene could therefore plausibly modify severity — **hypothesis, not established finding**.

### 2.4 Protective factors

**None identified.** There are no reported protective alleles, dietary factors, or lifestyle exposures that modify onset or course. Claims to the contrary should be treated as unsupported. The only "protective" genetic phenomenon is intra-locus: a **hypomorphic allele in trans to a null allele is protective relative to two nulls**, shifting the phenotype from late-infantile toward juvenile/protracted. This is the mirror image of the residual-activity gradient in §2.1 and is best modelled as allelic severity, not as a protective factor.

### 2.5 Gene–environment interactions

**Not applicable / none documented.** No GxE interaction has been demonstrated for any NCL. Intercurrent febrile illness can lower seizure threshold and precipitate clinical deterioration, but this is a nonspecific epilepsy phenomenon and not a disease-modifying interaction.

---

## 3. Phenotypes

⚠️ **Frequency caveat, stated once and applying throughout this section.** Quantitative frequency data for "juvenile NCL" in the literature are **overwhelmingly derived from CLN3 cohorts** (the Rochester UBDRS cohort, the DEM-CHILD/NCL Resource registries, Scandinavian and Danish series). Applying those frequencies to the *grouping* over-weights CLN3 and imports precisely the conflation this entry exists to avoid. Where I give a frequency below, I state which population it came from. **For a dismech entry, the defensible position is to curate the grouping's phenotypes with `frequency:` omitted for most terms**, per the frequency-evidence SOP, and to attach quantitative frequencies only at the member (`juvenile CLN3 disease`, MONDO:0979346) level.

### 3.1 Ophthalmological (the cardinal presenting domain)

| Phenotype | HPO term | Onset | Course | Notes |
|---|---|---|---|---|
| Progressive visual loss | **HP:0000529** Progressive visual loss | 4–7 y (CLN3); 6–11 y (CLN6, CLN7) | Progressive | Herald symptom in most members; **absent in CLN8/EPMR and in some CLN6** |
| Rod-cone dystrophy | **HP:0000510** Rod-cone dystrophy | juvenile | Progressive | |
| Retinal dystrophy | **HP:0000556** Retinal dystrophy | juvenile | Progressive | |
| Bull's eye maculopathy | **HP:0011504** Bull's eye maculopathy | juvenile | Progressive | Classic in CLN3; drives Stargardt misdiagnosis |
| Pigmentary retinopathy | **HP:0000580** Pigmentary retinopathy | juvenile | Progressive | |
| Macular degeneration | **HP:0000608** Macular degeneration | juvenile | Progressive | Isolated in non-syndromic *MFSD8* maculopathy |
| Optic atrophy | **HP:0000648** Optic atrophy | juvenile | Progressive | "disc pallor 56%" in a mixed pediatric NCL cohort (PMID:39281238) |
| Attenuation of retinal blood vessels | **HP:0007843** | juvenile | Progressive | |
| Abnormal electroretinogram | **HP:0000512** Abnormal electroretinogram | early, often pre-symptomatic | → extinguished | ERG becomes **HP:0000550** Undetectable electroretinogram |
| Abnormal fundus autofluorescence imaging | **HP:0030602** | juvenile | | |
| Blindness | **HP:0000618** Blindness | typically within 2–4 y of visual onset | | |

**Quality-of-life impact:** vision loss in this window is uniquely destructive because it lands at the start of formal literacy acquisition. It forces immediate transition to braille/assistive technology — which is then itself lost as dementia advances, producing a documented "double loss" and a well-described family-reported crisis point. Loss of independent mobility and reading are the two dominant QoL domains in the CLN3 literature.

### 3.2 Cognitive / behavioural / psychiatric

| Phenotype | HPO term | Notes |
|---|---|---|
| Cognitive impairment | **HP:0100543** Cognitive impairment | |
| Dementia | **HP:0000726** Dementia | Progressive, onset ~1–3 y after visual failure |
| Developmental regression | **HP:0002376** Developmental regression | |
| Intellectual disability | **HP:0001249** Intellectual disability | Progresses to **HP:0010864** Severe / **HP:0002187** Profound |
| Loss of speech | **HP:0002371** Loss of speech | |
| Psychosis | **HP:0000709** Psychosis | Prominent in adolescent CLN3; can precede or dominate |
| Hallucinations | **HP:0000738** Hallucinations; **HP:0002367** Visual hallucination | |
| Anxiety | **HP:0000739** Anxiety | |
| Aggressive behavior | **HP:0000718** Aggressive behavior | |
| Attention deficit hyperactivity disorder | **HP:0007018** | Early, often pre-diagnostic |
| Sleep disturbance | **HP:0002360** Sleep disturbance | High family-burden item |

The **psychiatric phenotype is a genuine differentiator within the grouping**: florid psychosis with hallucinations in an adolescent with visual failure is characteristically CLN3, whereas the CLN6 and CLN8 juvenile forms are dominated by seizures and motor decline with less prominent psychosis.

### 3.3 Seizures / epilepsy

| Phenotype | HPO term | Notes |
|---|---|---|
| Seizure | **HP:0001250** Seizure | |
| Bilateral tonic-clonic seizure | **HP:0002069** | Most common type |
| Generalized myoclonic seizure | **HP:0002123** | |
| Myoclonus | **HP:0001336** Myoclonus | Often action/stimulus-sensitive |
| Photosensitive myoclonic seizure | **HP:0001327** | |
| Generalized non-motor (absence) seizure | **HP:0002121** | |
| Status epilepticus | **HP:0002133** | Later stages |

**Seizure onset is the *defining* first symptom in the CLN8/EPMR member** — Ranta et al. describe EPMR as "an autosomal recessive disorder characterized by onset of generalized seizures between 5 and 10 years, and subsequent progressive mental retardation" (*Nat Genet* 1999;23(2):233-6; PMID:10508524). That onset window is squarely juvenile, but the phenotype lacks retinopathy — which is why a purely vision-anchored definition of "juvenile NCL" would wrongly exclude it.

In a mixed pediatric NCL cohort (median onset 5.46 ± 1.95 y), "myoclonic seizures in 68%, and motor difficulty in 24%" were the presenting symptoms, with "visual impairment (80%), global developmental delay (56%), and disc pallor (56%)" as primary features (Pak J Med Sci 2024;40(8):1638-1643; PMID:39281238). Note this cohort was CLN6-dominant (42%), not CLN3-dominant, which explains the seizure-first skew relative to classic CLN3 descriptions.

### 3.4 Motor: extrapyramidal, cerebellar, pyramidal

| Phenotype | HPO term | Notes |
|---|---|---|
| Ataxia / Progressive cerebellar ataxia | **HP:0001251** / **HP:0002073** | Cardinal in CLN5, CLN6, CLN10, and TPP1-SCAR7 |
| Gait ataxia | **HP:0002066** Gait ataxia | |
| Dysarthria | **HP:0001260** Dysarthria | |
| Parkinsonism | **HP:0001300** Parkinsonism | Prominent in CLN3 adolescence and definitional in ATP13A2/CLN12 |
| Bradykinesia | **HP:0002067**; Rigidity **HP:0002063** | |
| Dystonia | **HP:0001332** Dystonia | |
| Spasticity | **HP:0001257** Spasticity | Prominent in the Cypriot CLN6 juvenile families |
| Abnormal pyramidal sign | **HP:0007256** | |
| Loss of ambulation | **HP:0002505** Loss of ambulation | Second decade |
| Tremor | **HP:0001337** Tremor | |

### 3.5 Other systemic

| Phenotype | HPO term | Notes |
|---|---|---|
| Dysphagia | **HP:0002015** Dysphagia | Drives gastrostomy decision; aspiration is a major mortality route |
| Scoliosis | **HP:0002650** Scoliosis | Secondary to immobility |
| Peripheral neuropathy | **HP:0009830** Peripheral neuropathy | Documented in CTSD/CLN10 juvenile ("sensory axonal neuropathy", PMID:25298308) |
| Cardiac involvement | **HP:0011675** Arrhythmia *(⚠️ ID not re-verified against the local cache)* | Ventricular hypertrophy, repolarisation abnormalities, and sinus-node dysfunction are described in CLN3 adolescents/adults; **not** established for other members |

### 3.6 Neuroimaging and laboratory

| Finding | HPO term | Notes |
|---|---|---|
| Cerebral atrophy | **HP:0002059** Cerebral atrophy | |
| Cerebellar atrophy | **HP:0001272** Cerebellar atrophy | Prominent in CLN5, CLN6, CLN7 |
| Generalized cerebral atrophy/hypoplasia | **HP:0007058** | |
| Neuronal loss in central nervous system | **HP:0002529** | Neuropathological |
| Gliosis | **HP:0002171** Gliosis | Neuropathological; reactive astro-/microgliosis |
| **Vacuolated lymphocytes** | HP:0001922 *(⚠️ ID not present in the local HP cache and not verified this session — verify before use)* | **CLN3-specific**; a genuinely discriminating bedside test within the grouping |

### 3.7 Phenotype characteristics summary

- **Onset:** juvenile, ~5–10 y (grouping-defining). Range across defensible members: ~4 y (some CLN6/CLN5) to ~15 y (CTSD family A; some CLN7 protracted).
- **Severity:** severe and uniformly fatal in the classic members; **variable** across the grouping — protracted CLN2, CLN5, and CLN7 forms can survive into the fourth decade.
- **Progression:** **progressive**, monotonic, without remission. Not episodic or relapsing.
- **Frequency:** see the caveat opening §3.

---

## 4. Genetic / Molecular Information — the gene-by-gene core of this report

This is the section the entity requires. Below, each NCL gene is graded for whether a **juvenile-onset presentation is defensibly attributable to it**.

### 4.0 Grading key

- **Tier A — Established.** Multiple independent reports, or an authoritative classification source (GeneReviews Table 1 / Kousi 2012 / Mole & Cotman 2015) lists juvenile onset as a recognised phenotype for the gene.
- **Tier B — Reported, limited.** Juvenile onset reported in one or few families; real but thinly evidenced.
- **Tier C — Not defensible as juvenile.** The gene's recognised onset windows are infantile, late-infantile, or adult. Do not list as a member.
- **Tier X — Withdrawn / invalid.**

The two anchor classification sources agree substantially. GeneReviews *Neuronal Ceroid-Lipofuscinoses* (NBK1428) Table 1, retrieved this session:

| CLN | Gene | OMIM | Classic phenotype | Atypical phenotypes |
|---|---|---|---|---|
| CLN1 | *PPT1* | 256730 | Infantile | Late infantile, **Juvenile**, Adult |
| CLN2 | *TPP1* | 204500 | Late infantile | Congenital/infantile, **Juvenile**, **Late juvenile/protracted**, Adult |
| CLN3 | *CLN3* | 204200 | **Juvenile** | Protracted, Isolated retinal degeneration |
| CLN4 | *DNAJC5* | 162350 | Adult | — |
| CLN5 | *CLN5* | 256731 | Late infantile | Congenital, Infantile, **Juvenile**, Protracted, Teenage, Adult |
| CLN6 | *CLN6* | 601780, 204300 | **Late infantile to juvenile** | Protracted, Teenage, Adult Kufs A & B |
| CLN7 | *MFSD8* | 610951 | Late infantile | **Juvenile / late juvenile** |
| CLN8 | *CLN8* | 600143, 610003 | **Late infantile to juvenile** | — |
| CLN10 | *CTSD* | 610127 | Congenital | Late infantile, **Juvenile**, Adult |
| CLN11 | *GRN* | 614706 | Teenage to adult | — |
| CLN13 | *CTSF* | 615362 | Adult Kufs type B | — |
| CLN14 | *KCTD7* | 611726 | Late infantile | — |

Mole & Cotman 2015 (*Biochim Biophys Acta* 1852(10 Pt B):2237-41; PMID:26026925) Table 2 concurs and additionally lists **CLN12/ATP13A2 → juvenile**.

---

### 4.1 Tier A — *CLN3* (HGNC:2074) — the modal, but not the definitional, member

- **MONDO:** disease MONDO:0008767; **juvenile member term MONDO:0979346**. **OMIM:** 204200. **Protein:** CLN3/battenin, a polytopic lysosomal/endosomal membrane protein of incompletely defined function.
- **Onset:** 4–7 y with visual failure. **Course:** vision → cognition/behaviour → seizures (~8–13 y) → extrapyramidal motor decline → death typically in the third decade.
- **Variant spectrum:** dominated by a single founder allele, a **~1.02-kb genomic deletion removing exons 7 and 8** (`c.461-280_677+382del966`, historically "1 kb deletion"), reported in roughly 80–85% of disease alleles in Northern European ancestry, with ~70–75% of patients homozygous. ⚠️ *These specific percentages are from the standard literature (International Batten Disease Consortium, Cell 1995) but were not re-verified against a fetched abstract in this session — verify before curating as evidence.* Remaining alleles are missense, nonsense, frameshift, and splice.
- **Functional consequence:** loss of function. The common deletion produces a frameshifted truncated product.
- **Allelic non-NCL phenotype:** isolated/non-syndromic retinal degeneration from hypomorphic *CLN3* genotypes — clinically important because such patients are juvenile-onset and present to retina clinics.
- **Ultrastructure:** **fingerprint profiles**, with curvilinear and rectilinear components (GeneReviews Table 2).
- **Discriminating lab feature:** **vacuolated peripheral lymphocytes**, essentially unique to CLN3 within the grouping.
- **Carrier frequency:** ~1/500 in the US when adjusted for ethnic diversity (Gene 2016; see §4.14).

### 4.2 Tier A — *PPT1* / CLN1 (HGNC:9325) — juvenile CLN1 disease

- **MONDO:** **MONDO:0979341** ("juvenile neuronal ceroid lipofuscinosis 1"; Orphanet:699739); gene-level MONDO:0009744. **OMIM:** 256730. **Protein:** palmitoyl-protein thioesterase 1, a soluble lysosomal enzyme removing thioester-linked palmitate from S-acylated proteins.
- **Defensibility: strong and long-established.** The defining paper is explicitly titled for this phenotype: *"Mutations in the palmitoyl-protein thioesterase gene (PPT; CLN1) causing juvenile neuronal ceroid lipofuscinosis with granular osmiophilic deposits"* (Mitchison HM et al., *Hum Mol Genet* 1998;7(2):291-7; **PMID:9425237**). It reported: **"Five mutations in the PPT gene were identified: three missense mutations, Thr75Pro, Asp79Gly, Leu219Gln, and two nonsense mutations, Leu10STOP and Arg151STOP."**
- **The diagnostic trap this paper solved:** juvenile CLN1 combines a **juvenile clinical course** with **infantile-type ultrastructure (GROD, granular osmiophilic deposits)**. A pathologist who reads GROD and reports "infantile NCL" will contradict the clinician. Mitchison et al. concluded this demonstrates "the correlation which exists between genetic basis and ultrastructural changes in the NCLs" — i.e. **ultrastructure tracks the gene, not the onset age.** This is the single most useful ultrastructural rule for triaging a juvenile NCL: **GROD in a juvenile patient means *PPT1* or *CTSD*, not *CLN3*.**
- **Genotype–phenotype:** juvenile onset associates with missense/hypomorphic alleles retaining partial PPT1 activity; null/null gives classic infantile CLN1 (Santavuori-Haltia).
- **Biochemically confirmable:** PPT1 enzyme assay in leukocytes/fibroblasts/dried blood spot. This makes juvenile CLN1 one of only three members with a cheap, definitive, non-sequencing first-line test.
- **Carrier frequency:** highest of any NCL gene — **1/75 in Finns**; ~1/500 US-adjusted (Gene 2016).

### 4.3 Tier A — *TPP1* / CLN2 (HGNC:2073) — juvenile and late-juvenile/protracted CLN2

- **MONDO:** **MONDO:0979345** ("juvenile neuronal ceroid lipofuscinosis 2"; Orphanet:699769); gene-level MONDO:0009746. **OMIM:** 204500. **Protein:** tripeptidyl peptidase 1, a soluble lysosomal serine protease.
- **Defensibility: strong.** GeneReviews lists both "Juvenile" and "Late juvenile/protracted" as recognised atypical CLN2 phenotypes. The historically important report is Wisniewski KE et al., *"Reevaluation of neuronal ceroid lipofuscinoses: atypical juvenile onset may be the result of CLN2 mutations"* (*Mol Genet Metab* 1999) — ⚠️ *the exact-title PubMed query failed this session and I could not confirm its PMID; verify before citing.*
- **The best-characterised juvenile *TPP1* phenotype is SCAR7.** Sun et al. showed that autosomal recessive spinocerebellar ataxia 7 is allelic to CLN2: SCAR7 patients **"showed ataxia and low activity of tripeptidyl-peptidase 1, but no ophthalmologic abnormalities or epilepsy"**, and proposed that **"loss of function variants abolishing TPP1 enzyme activity lead to CLN2 disease, whereas variants that diminish TPP1 enzyme activity lead to SCAR7."** (*Hum Mutat* 2013;34(5):706-13; **PMID:23418007**). SCAR7 = MONDO:0012452 / OMIM:609270.
- **Why this matters for MONDO:0019262:** the *TPP1* juvenile/protracted phenotype is a **cerebellar-ataxia-first** presentation without the retinopathy that anchors the classic juvenile gestalt. A juvenile NCL grouping defined only by "vision loss + seizures + dementia" will miss it.
- **Biochemically confirmable:** TPP1 enzyme assay (leukocyte / dried blood spot). **This is the highest-yield single test in the entire grouping**, because CLN2 is the only NCL with an approved disease-modifying therapy (§12.1).
- **Ultrastructure:** curvilinear profiles.
- **Carrier frequency:** ~1/500 US-adjusted (Gene 2016).

### 4.4 Tier A — *CLN5* (HGNC:2076) — juvenile is the *predominant* onset outside Finland

- **MONDO:** MONDO:0008768 (gene-level) — **no juvenile-specific MONDO child exists.** **OMIM:** 256731. **Protein:** CLN5, a soluble lysosomal glycoprotein; recently characterised as a lysosomal bis(monoacylglycero)phosphate synthase.
- **Defensibility: strong, and the evidence is directionally surprising.** *CLN5* is classically the "Finnish variant late-infantile" gene (vLINCL<sup>Fin</sup>, onset 4.5–6 y — already at the late-infantile/juvenile boundary). But in non-Finnish populations juvenile onset predominates. Xin W et al. screened 47 clinically diagnosed, molecularly unsolved NCL patients and found 10 with pathogenic *CLN5* variants (11 previously undescribed), concluding: **"The age at disease onset in this cohort is predominantly juvenile rather than late infantile. Importantly, we have identified 2 adult-onset patients who share a common pathogenic allele."** (*Neurology* 2010;74(7):565-71; **PMID:20157158**). The title itself is the claim: *"CLN5 mutations are frequent in juvenile and late-onset non-Finnish patients with NCL."*
- **Clinical texture:** the same paper notes most patients presented with **motor and visual impairment rather than seizures**.
- **Founder allele:** the Finnish major mutation p.Tyr392* (historically "2467A>T").
- **Ultrastructure:** rectilinear, curvilinear, fingerprint.
- **Curation note:** *CLN5* is arguably the strongest single argument that MONDO:0019262 must not be modelled as CLN3 — a non-Finnish patient with a juvenile NCL and no *CLN3* variant has *CLN5* as a leading candidate.

### 4.5 Tier A — *CLN6* (HGNC:2077) — juvenile onset is in the *classic*, not atypical, range

- **MONDO:** MONDO:0011503 (gene-level) — no juvenile-specific child. **OMIM:** 601780 (CLN6), 204300 (Kufs type A). **Protein:** CLN6, a non-glycosylated ER transmembrane protein implicated in lysosomal acidification and in the CLN6–CLN8 (EGRESS) complex trafficking lysosomal enzymes from ER to Golgi.
- **Defensibility: strong.** GeneReviews classifies the *classic* phenotype as **"Late infantile to juvenile"** — CLN6 straddles the boundary by default. Mole & Cotman list "juvenile cerebellar ataxia" and "teenage progressive myoclonic epilepsy" among CLN6 phenotypes.
- **Two recent, well-characterised juvenile-onset families, both with a phenotype that breaks the vision-first rule:**

  Kyriakou K et al. reported two Greek-Cypriot families: *"We report clinical and genetic findings of three patients from two Greek-Cypriot families (families 915 and 926) with JNCL. All patients were males, and the first symptoms appeared at the age of 6 years. The proband of family 926 presented with loss of motor abilities, ataxia, spasticity, seizure, and epilepsy. The proband of family 915 had ataxia, spasticity, dysarthria, dystonia, and intellectual disability. Both probands did not show initial signs of vision and/or hearing loss."* Molecular findings: *"family 926 revealed two CLN6 biallelic variants: the novel, de novo p.Tyr295Cys and the known p.Arg136His variants. In family 915, both patients were homozygous for the p.Arg136His CLN6 variant."* — *Front Genet* 2021;12:746101 (**PMID:34868216**), titled *"A Novel CLN6 Variant Associated With Juvenile Neuronal Ceroid Lipofuscinosis in Patients With Absence of Visual Loss as a Presenting Feature."*

  A consanguineous Chinese family with a novel homozygous *CLN6* c.14G>T (p.Arg5Leu): *"Both patients exhibited seizures and progressive psychomotor decline and mental deterioration without visual impairment."* — *Neurodegener Dis* 2021;21(5-6):126-131 (**PMID:35609511**), titled *"Juvenile-Onset Kufs Disease in a Chinese Consanguineous Family due to CLN6 Mutation."*

- **The absent-visual-loss signature is the key CLN6 discriminator** within the juvenile grouping and should be curated explicitly. Together with CLN8/EPMR, it establishes that **visual failure is *typical* of MONDO:0019262 but not *necessary*.**
- **Also note:** *CLN6* additionally causes **adult Kufs type A** (autosomal recessive progressive myoclonic epilepsy) — so one gene spans late-infantile, juvenile, teenage, and adult windows. CLN6 is the clearest example of why gene ≠ onset class.
- **Epidemiological weight:** CLN6 was the **most common** genotype (42%) in a 153-patient pediatric NCL cohort (PMID:39281238), well ahead of CLN2 (16%) and CLN7 (12%).

### 4.6 Tier A — *MFSD8* / CLN7 (HGNC:28486) — juvenile / late-juvenile protracted

- **MONDO:** MONDO:0012588 (gene-level) — no juvenile-specific child. **OMIM:** 610951. **Protein:** MFSD8/CLN7, a lysosomal major-facilitator-superfamily transmembrane transporter.
- **Defensibility: strong.** GeneReviews lists "Juvenile/late juvenile" as the recognised atypical phenotype. Kousi et al.'s foundational *MFSD8* paper, while framed around variant late-infantile disease — *"With one exception, the CLN7/MFSD8 mutation positive patients present a phenotype indistinguishable from the other vLINCL forms"* (*Brain* 2009;132(Pt 3):810-9; **PMID:19201763**) — describes that exception as a **Dutch patient with a protracted course who presented at age 11 with visual failure**, with motor impairment and seizures in his mid-twenties and mental/speech regression in his thirties. That is a juvenile-onset, decades-long *MFSD8* NCL.
- **Founder allele:** p.Thr294Lys, homozygous in 14 Roma patients from 12 families of the former Czechoslovakia.
- **Allelic non-syndromic juvenile eye disease:** Roosing S et al. identified compound-heterozygous *MFSD8* variants causing **nonsyndromic autosomal recessive macular dystrophy** with central cone involvement, normal/subnormal full-field ERG but reduced multifocal ERG. Both families carried the mild missense p.Glu336Gln in trans to a severe allele (protein-truncating in one family, splicing-defect in the other), supporting an explicit dose model: *"proposing a genotype-phenotype model where variant combinations determine disease severity."* (*Ophthalmology* 2015;122(1):170-9; **PMID:25227500**).
- **Why this matters here:** *MFSD8* produces a graded juvenile-onset visual spectrum from isolated maculopathy (no neurodegeneration) through juvenile NCL — the residual-activity gradient of §2.1 made visible in one gene.
- **Ultrastructure:** rectilinear, fingerprint.

### 4.7 Tier A — *CLN8* (HGNC:2079) — EPMR / Northern epilepsy: juvenile by age, atypical by phenotype

- **MONDO:** MONDO:0009746-adjacent; gene-level MONDO:0008776 (Northern epilepsy) / MONDO:0012531 (CLN8 vLINCL) — *⚠️ these two CURIEs were not individually verified this session.* **OMIM:** 600143 (EPMR/Northern epilepsy), 610003 (CLN8 vLINCL). **Protein:** CLN8, an ER/ERGIC transmembrane protein; partner of CLN6 in the EGRESS complex.
- **Defensibility: strong on age, with an explicit clinical caveat.** GeneReviews classifies the *classic* CLN8 phenotype as **"Late infantile to juvenile."** Ranta et al.'s positional cloning paper defines EPMR as *"an autosomal recessive disorder characterized by onset of generalized seizures between 5 and 10 years, and subsequent progressive mental retardation"*, caused by a homozygous missense mutation **"(70C-->G, R24G) that was not found in homozygosity in 433 controls"** (*Nat Genet* 1999;23(2):233-6; **PMID:10508524**).
- **5–10 years is the textbook juvenile window.** EPMR therefore belongs in MONDO:0019262 on the grouping's own onset criterion — but it presents with **epilepsy, not vision loss**, and is comparatively mild (patients survive into middle age with intellectual disability).
- **CLN8 is also the canonical illustration of intra-genic phenotypic divergence.** Kousi et al.: *"Phenotypic divergence is exemplified by different CLN8 mutations giving rise to two very different diseases, the mild CLN8 disease, EPMR (progressive epilepsy with mental retardation), and the more severe CLN8 disease, late infantile variant."* (PMID:21990111)
- **Founder allele:** p.Arg24Gly, essentially restricted to a region of northern Finland (Kainuu), hence "Northern epilepsy". The Turkish vLINCL *CLN8* alleles are distinct and produce the more severe late-infantile disease.
- **Ultrastructure:** curvilinear-like fingerprint, granular.

### 4.8 Tier B — *CTSD* / CLN10 (HGNC:2529) — juvenile-onset ataxia with retinopathy

- **MONDO:** MONDO:0012350 (gene-level) — *⚠️ CURIE not verified this session.* **OMIM:** 610127. **Protein:** cathepsin D, a soluble lysosomal aspartyl protease.
- **Defensibility: reported and credible, but few families.** GeneReviews lists "Juvenile" among CTSD atypical phenotypes (classic = congenital). The primary evidence:
  - Steinfeld R et al., *"Cathepsin D deficiency is associated with a human neurodegenerative disorder"* (*Am J Hum Genet* 2006; **PMID:16685649**) — established CTSD as an NCL gene, including a juvenile-onset sibship.
  - Two consanguineous pedigrees **"both with a juvenile onset of NCL"** were characterised in *Neurology* 2014;83(20):1873-5 (**PMID:25298308**), titled *"Cathepsin D deficiency causes juvenile-onset ataxia and distinctive muscle pathology."* Family A carried a **"homozygous missense mutation (p.G149V in exon 4 of CTSD)"** with **"juvenile onset of cerebellar ataxia and retinitis pigmentosa at around 15 years, which progressed to significant motor impairment and cognitive decline."** Family B carried a **"homozygous missense mutation… (p.Arg399His in exon 9 of CTSD)"** with an **"earlier age at onset of 8 years"** and additionally **"sensory axonal neuropathy."** Fibroblast assay showed **"a significant reduction in enzyme activity compared to controls."** Muscle biopsy showed **"granulovacuolar material in angular atrophic fibers in addition to the granular osmiophilic deposits that are diagnostic for neuronal ceroid lipofuscinosis."**
- **Notably, in a 153-patient pediatric NCL cohort, CLN10 was the *only* genotype presenting exclusively as juvenile** (PMID:39281238) — a small-n but striking observation.
- **Biochemically confirmable:** cathepsin D enzyme activity assay in fibroblasts. Third of the three assayable members.
- **Ultrastructure:** GROD — the other GROD-in-a-juvenile gene alongside *PPT1*.

### 4.9 Tier B — *ATP13A2* / CLN12 (HGNC:30213) — juvenile NCL / Kufor-Rakeb syndrome

- **MONDO:** **MONDO:0017809** ("parkinsonism due to ATP13A2 deficiency") — **this is an asserted direct child of MONDO:0019262.** **OMIM:** 606693. **Protein:** ATP13A2/PARK9, a lysosomal P5B-type polyamine transporting ATPase.
- **Defensibility: reported, single-family origin for the NCL designation, but ontologically endorsed.** Bras J et al. described a family with typical NCL pathology in which exome sequencing found a homozygous *ATP13A2* mutation segregating with disease, noting that **"Mutations in ATP13A2 are a known cause of Kufor-Rakeb syndrome (KRS), a rare parkinsonian phenotype with juvenile onset"**, and concluding that NCL and KRS may share etiological mechanisms and **"implicate the lysosomal pathway in Parkinson's disease."** (*Hum Mol Genet* 2012;21(12):2646-50; **PMID:22388936**). Mole & Cotman Table 2 lists CLN12/ATP13A2 as **juvenile**. Zhang et al. 2025 give onset ~13 y.
- **Phenotype:** juvenile-onset parkinsonism with pyramidal signs, supranuclear gaze palsy, and cognitive decline (Kufor-Rakeb), plus NCL storage. The extrapyramidal dominance distinguishes it, though note that CLN3 adolescents also develop parkinsonism.
- **Caveat for curation:** the NCL designation for *ATP13A2* rests on a small evidence base and the gene is far better known as a parkinsonism gene. Model as a member with explicit acknowledgement of the thin evidence, and preserve the KRS identity rather than flattening it into "juvenile NCL".

### 4.10 Tier B/borderline — *GRN* / CLN11 (HGNC:4601) — adolescent-to-young-adult, mostly *outside* the juvenile window

- **MONDO:** MONDO:0013839 *(⚠️ not verified this session)*. **OMIM:** 614706. **Protein:** progranulin, a secreted glycoprotein processed to granulin peptides; lysosomal chaperone functions including interaction with prosaposin and cathepsin D.
- **Defensibility: weak as a *juvenile* member; strong as an *adult/teenage* member.** GeneReviews classifies CLN11 as **"Teenage to adult."** The defining paper reported two siblings homozygous for **c.813_816del (p.Thr272Serfs\*10)**, and its central point is the dosage dichotomy: *"Heterozygous mutations in GRN are a major cause of frontotemporal lobar degeneration with TDP-43 inclusions (FTLD-TDP)… The age-at-onset and neuropathology of FTLD-TDP and NCL are markedly different. Our findings reveal an unanticipated link between a rare and a common neurological disorder and illustrate pleiotropic effects of a mutation in the heterozygous or homozygous states."* (Smith KR et al., *Am J Hum Genet* 2012;90(6):1102-7; **PMID:22608501**). Reexamination of progranulin-deficient mice **"revealed rectilinear profiles typical of NCL."**
- **Onset in homozygous *GRN* NCL is typically ~20–25 y** (retinal dystrophy first, then ataxia, seizures, cognitive decline). Zhang et al. 2025 quote a wider "5–25 years" band; I could not verify a specific well-documented childhood-onset homozygous *GRN* case in this session.
- **Recommendation: do NOT list *GRN*/CLN11 as a core member of MONDO:0019262.** List it as an adjacent, adult-boundary entity to be **excluded** in differential reasoning, with a note that the youngest reported onsets brush the upper edge of adolescence.

### 4.11 Tier C — *DNAJC5* / CLN4 (HGNC:24586) — **adult only; exclude**

- **OMIM:** 162350. **Protein:** cysteine-string protein alpha (CSPα), a synaptic-vesicle co-chaperone.
- **Autosomal DOMINANT adult-onset Kufs disease**, onset typically mid-20s to 40s, with progressive myoclonic epilepsy and dementia. GeneReviews: classic phenotype **"Adult"**; no atypical phenotypes listed.
- **Explicitly not juvenile.** The current gene list for adult NCL is stated cleanly in Jedličková I et al.: *"Adult-onset neuronal ceroid lipofuscinoses (ANCL, Kufs disease) are rare hereditary neuropsychiatric disorders characterized by intralysosomal accumulation of ceroid in tissues… Although several causative genes have been identified (DNAJC5, CLN6, CTSF, GRN, CLN1, CLN5, ATP13A2), the genetic underpinnings of ANCL in some families remain unknown."* (*Eur J Hum Genet* 2020;28(6):783-789; **PMID:31919451**). That paper also carries a diagnostic caution worth recording: a 30-bp in-frame *DNAJC5* duplication **"was not detected initially by standard Sanger sequencing due to a preferential PCR amplification of the shorter wild-type allele and allelic dropout of the mutated DNAJC5 allele. It was also missed by subsequent whole-exome sequencing (WES)."**
- **Note the overlap this creates:** *CLN6, CTSF, GRN, CLN1, CLN5, ATP13A2* appear in **both** the adult list above and (for CLN1, CLN5, CLN6, ATP13A2) the juvenile list. **The same gene can be a member of the juvenile grouping and of the adult grouping via different alleles.** This is the central structural fact about onset-defined NCL groupings and must not be modelled as an inconsistency.

### 4.12 Tier C — *CTSF* / CLN13 (HGNC:2531) — **adult Kufs type B; exclude**

- **OMIM:** 615362. **Protein:** cathepsin F, a lysosomal cysteine protease. GeneReviews: **"Adult Kufs type B"**, no atypical phenotypes. Onset typically after age 20 (Zhang 2025: "After 20 years"). Ultrastructure: GROD and fingerprint.

### 4.13 Tier C — *KCTD7* / CLN14 (HGNC:21957) — **infantile/late-infantile PME; exclude**

- **OMIM:** 611726 (progressive myoclonic epilepsy 3 with or without intracellular inclusions). **Protein:** potassium channel tetramerisation domain-containing 7, a cytoplasmic/peripherally membrane-associated protein. GeneReviews: classic **"Late infantile"**; Zhang 2025 gives onset ~14 months. No credible juvenile-onset NCL attribution.

### 4.14 Tier X — "CLN9" — **withdrawn; the label survives in ontologies as an artefact**

- **MONDO:0012188** ("neuronal ceroid lipofuscinosis 9") is an asserted **direct child of MONDO:0019262** — but **there is no CLN9 gene.** OMIM 609055 remains as a legacy entry.
- History: Schulz A et al. (2004; **PMID:15349861**, *"Impaired cell adhesion and apoptosis in a novel CLN9 Batten disease variant"*) described a juvenile-onset NCL variant in two Serbian sisters and two German brothers, attributed to a putative new gene "CLN9". Kousi et al. still listed CLN4 and CLN9 as "provisionally named" in 2012 (PMID:21990111). **El Haddad et al. (2012) subsequently identified a homozygous *CLN5* nonsense mutation in affected siblings from one of the Schulz families**, reclassifying that family as CLN5. ⚠️ *The El Haddad PMID and the exact *CLN5* variant nomenclature were reported to me in secondary search summaries and were not verified against a primary abstract this session — verify before citing.*
- **Curation guidance:** CLN9 should be recorded as an **invalid/withdrawn designation**, retained only to explain legacy literature and legacy ontology terms. Do **not** curate it as a distinct genetic member. Its presence as a MONDO child of MONDO:0019262 is a defect worth reporting upstream, alongside the missing CLN5/CLN6/CLN7/CLN8/CLN10 juvenile children (§1.3).

### 4.15 Population allele frequencies and carrier burden

The best single quantitative source is an ExAC-based analysis of ~61,000 exomes across twelve NCL genes:

> "Estimates of NCL incidence range from 0.6 to 14 per 100,000 live births but vary widely between populations and are influenced by whether patients are classified based upon clinical or genetic criteria. We investigated mutations in twelve NCL genes in ~61,000 individuals represented in the Exome Aggregation Consortium (ExAC) whole exome sequencing database… Carrier frequency was dependent on ethnicity, with the highest (1/75) observed for PPT1 in the Finnish. When data are adjusted for ethnic diversity within the USA, PPT1, TPP1 and CLN3 carrier frequencies were found to be the highest of the NCLs, each at ~1/500."
> — *Gene* 2016;593(2):284-91 (**PMID:27553520**)

That paper also carries a warning directly relevant to ClinVar-based curation:

> "the analysis identified numerous variants that are annotated as pathogenic in public repositories but have a predicted frequency that is not consistent with patient studies. These variants appear to be neutral polymorphisms that are reported as pathogenic without validation."

**Variant classification and origin:** all variants are **germline**; ACMG/AMP classification applies; COSMIC/TCGA/ICGC are **not applicable** (no somatic component). ClinVar and the **NCL Mutation and Patient Database (UCL, ucl.ac.uk/ncl-disease)** are the two primary variant resources; the latter is NCL-specific and organises Patient Datasheets and Mutation Datasheets per gene. Kousi et al. catalogued **365 NCL-causing mutations across eight genes** as of 2012 (PMID:21990111); Mole & Cotman put the figure at **"more than a dozen genes containing over 430 mutations"** by 2015 (PMID:26026925).

### 4.16 Epigenetics and chromosomal abnormalities

- **Epigenetics:** no established disease-causing epigenetic mechanism. No imprinting, no methylation-defined subtype. ENCODE/Roadmap/DiseaseMeth are not informative for this entity.
- **Chromosomal abnormalities:** the only recurrent structural variant of note is the **CLN3 ~1.02-kb intragenic deletion** — a small CNV detectable by targeted PCR or by exon-level dosage analysis, **not** by routine karyotype or standard-resolution chromosomal microarray. Larger multi-exon deletions occur in several NCL genes and are a recognised cause of "one variant found, one missing" cases. **Karyotype and FISH have no role.** CMA has a limited role only if it is exon-resolution over the relevant genes.

---

## 5. Environmental Information

- **Environmental factors:** none. No toxin, radiation, pollutant, or occupational exposure contributes to NCL causation. CTD/TOXNET/EPA are not informative sources for this entity.
- **Lifestyle factors:** none causal. Nutritional status and aspiration risk affect *outcome*, not etiology.
- **Infectious agents:** none. NCL is not infectious, not triggered by infection, and has no zoonotic dimension. Intercurrent febrile illness may transiently worsen seizure control — a nonspecific epilepsy effect.

**This section is genuinely empty for MONDO:0019262 and should be curated as such**, rather than padded.

---

## 6. Mechanism / Pathophysiology

### 6.1 The shared final common pathway

All members converge on **lysosomal dysfunction with accumulation of autofluorescent ceroid-lipofuscin**, then on neuronal death with regional selectivity. The proximal defects are heterogeneous — soluble lysosomal enzymes (*PPT1*, *TPP1*, *CTSD*, *CTSF*), a soluble lysosomal protein (*CLN5*), a secreted protein (*GRN*), cytosolic/membrane-peripheral proteins (*DNAJC5*, *KCTD7*), and multiple transmembrane proteins at different subcellular locations (*CLN3*, *CLN6*, *MFSD8*, *CLN8*, *ATP13A2*):

> "These genes encode lysosomal enzymes (CLN1, CLN2, CLN10, CLN13), a soluble lysosomal protein (CLN5), a protein in the secretory pathway (CLN11), two cytoplasmic proteins that also peripherally associate with membranes (CLN4, CLN14), and many transmembrane proteins with different subcellular locations (CLN3, CLN6, CLN7, CLN8, CLN12). For most NCLs, the function of the causative gene has not been fully defined."
> — Mole & Cotman, PMID:26026925

**Proposed causal chain for the grouping** (upstream → downstream):

1. **[MOLECULAR]** Biallelic hypomorphic variant → partial loss of gene-product function (residual activity in the juvenile-permissive range).
2. **[MOLECULAR]** Failure of the specific lysosomal degradative/transport step → substrate accumulation.
3. **[CELLULAR]** Progressive intralysosomal accumulation of autofluorescent ceroid-lipofuscin storage material.
4. **[CELLULAR]** Autophagic-lysosomal pathway failure — accumulation of autophagic vacuoles, impaired autophagosome-lysosome fusion, impaired lysosomal acidification.
5. **[CELLULAR/TISSUE]** Reactive microgliosis and astrogliosis; neuroinflammation, which in NCL models **precedes and predicts** regional neuron loss.
6. **[TISSUE]** Selective neurodegeneration — photoreceptors and retinal ganglion cells early (accounting for the vision-first phenotype), then cortical layers II/III/V, cerebellar Purkinje and granule cells, thalamic relay nuclei.
7. **[ORGANISM]** Visual failure → cognitive/behavioural decline → epilepsy → motor decline → death.

### 6.2 The stored material — a genuine mechanistic discriminator

The storage body composition is **not** uniform, and this maps onto ultrastructure and onto gene:

- In most NCLs the major stored protein is **subunit c of mitochondrial ATP synthase (SCMAS)** — established by Palmer and colleagues: *"Mitochondrial ATP synthase subunit c storage in the ceroid-lipofuscinoses (Batten disease)"*, *Am J Med Genet* 1992 (**PMID:1535179**), and the companion immunocytochemical study, *Am J Med Genet* 1995 (**PMID:7668326**). This corresponds to curvilinear/rectilinear/fingerprint ultrastructure.
- In **CLN1/PPT1** and **CLN10/CTSD**, the predominant stored proteins are instead **saposins A and D**, and the ultrastructure is **GROD**. ⚠️ *The saposin attribution is standard in the field (Tyynelä et al.) but I did not verify a specific PMID for it this session.*

**Curation consequence:** a juvenile NCL entry should model *two* storage-composition branches (SCMAS-type vs saposin/GROD-type), not one.

### 6.3 Gene-specific proximal mechanisms

| Gene | Protein | Proximal molecular defect | Suggested GO terms |
|---|---|---|---|
| *PPT1* | palmitoyl-protein thioesterase 1 | Failure to remove thioester-linked palmitate from S-acylated proteins in the lysosome | GO:0008474 palmitoyl-(protein) hydrolase activity; GO:0006508 proteolysis |
| *TPP1* | tripeptidyl peptidase 1 | Failure of N-terminal tripeptide removal from small polypeptides in the lysosome | GO:0008240 tripeptidyl-peptidase activity; GO:0006508 proteolysis |
| *CTSD* | cathepsin D | Loss of lysosomal aspartyl endopeptidase activity | GO:0004190 aspartic-type endopeptidase activity |
| *CLN3* | battenin | Undefined; implicated in lysosomal pH/osmoregulation, membrane trafficking, glycerophosphodiester efflux | GO:0007040 lysosome organization |
| *CLN5* | CLN5 | Soluble lysosomal protein; BMP (bis(monoacylglycero)phosphate) synthase activity | GO:0007040 lysosome organization |
| *CLN6*, *CLN8* | CLN6, CLN8 | ER/ERGIC EGRESS complex — trafficking of soluble lysosomal enzymes from ER to Golgi; lysosomal acidification | GO:0006888 endoplasmic reticulum to Golgi vesicle-mediated transport |
| *MFSD8* | MFSD8/CLN7 | Lysosomal MFS transporter; substrate not definitively assigned | GO:0055085 transmembrane transport |
| *ATP13A2* | ATP13A2 | Lysosomal polyamine (spermidine/spermine) export; P5B-ATPase | GO:1902047 polyamine transmembrane transport; GO:0140326 ATPase-coupled intramembrane lipid transporter activity |
| *GRN* | progranulin | Loss of secreted lysosomal chaperone; prosaposin/cathepsin D regulation | GO:0007040 lysosome organization |

⚠️ *GO IDs above are suggestions from domain knowledge and were **not** validated against OAK/OLS this session. Run `just validate-terms` before committing any of them.*

Additional shared-process GO terms: **GO:0007041** lysosomal transport; **GO:0006914** autophagy; **GO:0061919** process utilizing autophagic mechanism; **GO:0006954** inflammatory response; **GO:0050808** synapse organization; **GO:0070997** neuron death. *(Same validation caveat.)*

### 6.4 Cross-gene interdependence

An important and under-modelled mechanism: NCL proteins regulate one another, so a single-gene lesion produces a multi-protein lysosomal deficit. *"Loss of CLN3 has been shown to affect PPT1, TPP1, CLN5, and CTSD"* (Zhang et al. 2025, PMID:39925015). CLN6 and CLN8 act as an obligate complex. Progranulin regulates prosaposin and cathepsin D. This explains both phenotypic convergence and why enzyme assays can be mildly abnormal in the "wrong" NCL.

### 6.5 Immune system involvement

**Neuroinflammation, not autoimmunity or immunodeficiency.** Microglial and astrocytic activation is early, regionally patterned, and in models precedes neuron loss: *"Neuroimmune responses mediated by astrocytes and microglia are integral to the progression of neurodegenerative diseases"* (PMID:39925015). Autoantibodies to GAD65 have been reported in CLN3 patients and provide the rationale for the immunosuppression trials in §12.4 — but CLN3 disease is **not** an autoimmune disease, and the entry should not be modelled as one.

Relevant CL terms: **CL:0000129** microglial cell; **CL:0000127** astrocyte; **CL:0000540** neuron; **CL:0000573** retinal cone cell; **CL:0000604** retinal rod cell; **CL:0000740** retinal ganglion cell; **CL:0000121** Purkinje cell; **CL:0000117** CNS neuron (sensu Vertebrata). *(Not OAK-validated this session.)*

### 6.6 Tissue damage mechanisms

Progressive neuronal death (apoptotic and non-apoptotic), synaptic loss preceding somatic loss, axonal/neuritic dystrophy, oxidative stress, and secondary mitochondrial dysfunction. Photoreceptor outer-segment degeneration precedes ganglion-cell loss in the retina. Reactive gliosis and progressive brain atrophy on MRI, most marked cerebellar and cortical.

### 6.7 Molecular profiling

- **Transcriptomics/proteomics/lipidomics:** substantial data exist for *CLN3* mouse and ovine *CLN5*/*CLN6* models; human data are sparse. GEO/PRIDE hold NCL model datasets. Lipidomics is mechanistically important given the CLN5-BMP-synthase finding and the lipid nature of the storage material.
- **Single-cell / spatial:** emerging in NCL mouse models (microglial state transitions); **no established human single-cell atlas** for any juvenile NCL member.
- **Functional genomics screens:** DepMap and CRISPR screens have been used for CLN3 interactor discovery; nothing definitive at grouping level.

**Honest statement for the KB:** molecular-profiling evidence for MONDO:0019262 as a grouping is thin and almost entirely model-derived; gene-specific human omics is largely absent.

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary:**
- **Central nervous system** — UBERON:0001017 central nervous system; **UBERON:0000955** brain; **UBERON:0000956** cerebral cortex; **UBERON:0002037** cerebellum; **UBERON:0001897** dorsal thalamus / UBERON:0001879? *(verify)*; **UBERON:0002420** basal ganglia *(verify)*; **UBERON:0002240** spinal cord.
- **Eye / retina** — **UBERON:0000970** eye; **UBERON:0000966** retina; **UBERON:0001782** macula lutea *(verify)*; **UBERON:0000941** optic nerve *(verify)*.

**Secondary / systemic (storage is ubiquitous even where dysfunction is not):**
- Skin/eccrine sweat glands (the classic EM biopsy site), rectal mucosa, conjunctiva, skeletal muscle (granulovacuolar change in CTSD deficiency), peripheral blood lymphocytes (CLN3), myocardium (CLN3).
- Body systems: **nervous** (primary), **visual/sensory** (primary), **musculoskeletal** (secondary — contractures, scoliosis), **cardiovascular** (CLN3-specific, late), **respiratory** (aspiration), **digestive** (dysphagia, malnutrition).

### 7.2 Tissue and cell level

Neural tissue is the target. Affected cell populations: **retinal photoreceptors (rods and cones)**, **retinal ganglion cells**, **cortical pyramidal neurons** (layers II/III and V), **cerebellar Purkinje cells** and granule cells, **thalamic relay neurons**, with prominent involvement of **microglia** and **astrocytes** as active participants rather than bystanders. Storage material is also present in non-neural cells — fibroblasts, lymphocytes, eccrine gland epithelium — which is what makes peripheral biopsy diagnostically possible.

### 7.3 Subcellular level

- **GO:0005764** lysosome — the primary compartment.
- **GO:0005765** lysosomal membrane — locus of the transmembrane members (CLN3, MFSD8, ATP13A2).
- **GO:0005783** endoplasmic reticulum — locus of CLN6/CLN8.
- **GO:0005794** Golgi apparatus — the EGRESS trafficking route.
- **GO:0005776** autophagosome; **GO:0005739** mitochondrion (SCMAS origin; secondary dysfunction); **GO:0008021** synaptic vesicle (CSPα/CLN4, adult).

*(GO CC IDs not OAK-validated this session.)*

### 7.4 Localization and laterality

**Bilateral and symmetric** throughout. Retinopathy is bilateral; cerebral and cerebellar atrophy are symmetric. Asymmetry is not a feature and should prompt reconsideration of the diagnosis. The characteristic MRI pattern is early **cerebellar atrophy** with progressive **generalised cerebral atrophy**, periventricular white-matter T2 hyperintensity, and thalamic T2 hypointensity (best described in CLN2/late-infantile but seen across members).

---

## 8. Temporal Development

### 8.1 Onset

- **Age:** the grouping's defining criterion — **~5–10 years**, extended by some authors to 4–15 y. Practically: first symptom after the child has been developmentally normal through early schooling, and before the adult (>18 y) Kufs window.
- **Pattern:** **insidious and chronic-progressive.** Not acute, not subacute. The apparent "sudden" presentation is usually delayed recognition of insidious visual loss.
- **Onset symptom by member:** visual failure (CLN3, CLN5, CLN7, CLN10, many CLN1-juvenile) | seizures (CLN8/EPMR, many CLN6) | ataxia (TPP1-SCAR7, CLN6, CLN10) | parkinsonism (ATP13A2/CLN12) | behavioural/school problems (CLN3, frequently the true first sign in retrospect).

### 8.2 Progression and staging

A four-stage frame applies across the grouping (mapped most precisely for CLN3):

| Stage | Approx. age (CLN3) | Features |
|---|---|---|
| I — Visual | 4–7 y | Rapid central vision loss, bull's-eye maculopathy, ERG abnormal → extinguished; behavioural/attention changes often already present |
| II — Cognitive/behavioural | 6–12 y | School failure, dementia onset, anxiety/psychosis, sleep disruption; blindness complete |
| III — Epileptic/motor | 8–18 y | Generalised tonic-clonic and myoclonic seizures; parkinsonism, dystonia, ataxia, dysarthria; ambulation lost |
| IV — End-stage | late teens–20s/30s | Bedbound, anarthric, dysphagic, gastrostomy-dependent; death from aspiration pneumonia/respiratory failure or status epilepticus |

**Formal instruments (CLN3-specific, not grouping-general):**
- **Unified Batten Disease Rating Scale (UBDRS)** — four subscales: physical (28 items, 0–112), seizure (12 items, 0–54), behaviour (9 items, 0–55), capability (5 items, 0–14). Validated in an independent CLN3 sample (PMC9879304).
- **CLN3 Disease Staging System** (*PMID:32300063*).
- **CLN2 Clinical Rating Scale** (Hamburg/Weill Cornell motor-language domains) — used as the primary endpoint in the cerliponase alfa trial.

There is **no validated rating instrument for MONDO:0019262 as a whole**; this is a real gap for any grouping-level natural-history or trial work.

### 8.3 Progression rate and course

**Progression rate is genotype- and allele-dependent**, and is the main axis of within-grouping variation:
- **Rapid:** classic CLN3 (death typically third decade); juvenile CLN1 (faster than CLN3).
- **Intermediate:** CLN6 juvenile, CLN5 juvenile, CLN10 juvenile.
- **Slow/protracted:** *TPP1*-SCAR7 (ataxia only for decades); protracted *MFSD8* (visual failure at 11, motor/seizures in mid-20s, mental/speech regression in the 30s); *CLN8*-EPMR (survival into middle age with seizure attenuation after puberty).

**Course pattern:** progressive, chronic, lifelong. **No remission**, spontaneous or treatment-induced, has ever been reported for any member. **Disease duration:** from onset to death, ~10–25 years for the classic members; longer for protracted forms.

### 8.4 Critical periods

- **Diagnostic window:** the 1–3 years between visual failure and cognitive decline is the therapeutic opportunity. Diagnostic delay in this window is the norm and is the dominant modifiable failure in current care.
- **Therapeutic window:** for the only disease-modifying therapy available (cerliponase alfa in CLN2), benefit is preservation of remaining function, not recovery — so the window closes as function is lost. The same logic applies to every gene therapy in trial. Zhang et al. put this bluntly: *"these therapies are unlikely to achieve partial disease reversal, and complete reversal remains improbable."*
- **Presymptomatic identification** (sibling cascade testing) is currently the only route to treatment before loss.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

**Grouping-level, from the Scandinavian survey** (Neuropediatrics 1997;28(1):6-8; **PMID:9151309**) — the best direct data on *juvenile* NCL as such:

> "For juvenile NCL 40 Swedish living patients were identified. The corresponding number for Finland was 61, for Norway 28, for Denmark 16 and for Iceland three. The prevalence of juvenile NCL was thus 4.6, 12.2, 6.5, 3.1 and 11 per million inhabitants in Sweden, Finland, Norway, Denmark, and Iceland, respectively. For calculating incidence the years 1976-85 were used. The incidence was 2.2 per 100,000 live births in Sweden, 4.8 in Finland, 3.7 in Norway, 2.0 in Denmark, and 7.0 in Iceland."

**Structured for curation:**

| Population | Measure | Value | `rate_per_100000` |
|---|---|---|---|
| Sweden | Point prevalence | 4.6 / 1,000,000 | 0.46 |
| Finland | Point prevalence | 12.2 / 1,000,000 | 1.22 |
| Norway | Point prevalence | 6.5 / 1,000,000 | 0.65 |
| Denmark | Point prevalence | 3.1 / 1,000,000 | 0.31 |
| Iceland | Point prevalence | 11 / 1,000,000 | 1.10 |
| Sweden | Birth prevalence / incidence (1976–85) | 2.2 / 100,000 live births | 2.2 |
| Finland | Birth prevalence / incidence | 4.8 / 100,000 live births | 4.8 |
| Norway | Birth prevalence / incidence | 3.7 / 100,000 live births | 3.7 |
| Denmark | Birth prevalence / incidence | 2.0 / 100,000 live births | 2.0 |
| Iceland | Birth prevalence / incidence | 7.0 / 100,000 live births | 7.0 |

**Italy** (Orphanet J Rare Dis 2013;8:19; **PMID:23374165**), a contrasting low-incidence population, and directly informative about the *juvenile fraction*:

> "One hundred eighty-three NCL patients from 156 families were recruited between 1966 and 2010… Late infantile onset NCL (LINCL) accounted for 75.8% of molecularly confirmed cases, the most frequent form being secondary to mutations in CLN2 (23.5%). **Juvenile onset NCL patients accounted for 17.7% of this cohort, a smaller proportion than found in other European countries.** … An incidence rate of 0.98/100,000 live births was found in 69 NCL patients born between 1992 and 2004, predicting 5 new cases a year. Prevalence was 1.2/1,000,000."

**All-NCL range** (Gene 2016, PMID:27553520): *"Estimates of NCL incidence range from 0.6 to 14 per 100,000 live births but vary widely between populations."*

**Synthesis:** juvenile NCL is best characterised as **~2–5 per 100,000 live births in Northern Europe, ~0.2–1 per 100,000 in Southern Europe**, with point prevalence of roughly **0.3–1.2 per 100,000 population**. In Orphanet prevalence-class terms this is `BAND_1_9_PER_1000000` for point prevalence in most European populations. The **juvenile fraction of all NCL** ranges from ~18% (Italy) to a majority in Northern Europe.

### 9.2 Inheritance genetics

- **Pattern:** **autosomal recessive** for every defensible member. HPO **HP:0000007** Autosomal recessive inheritance. (The one AD NCL, *DNAJC5*/CLN4, is adult-onset and excluded.)
- **Penetrance:** complete for biallelic pathogenic genotypes. No reported non-penetrant biallelic carriers.
- **Expressivity:** **variable**, including within families sharing a genotype (documented in the Chinese *CLN6* sibship, PMID:35609511). Age of onset and MRI severity varied between siblings with the identical homozygous missense variant.
- **Anticipation:** **not applicable** — no repeat-expansion mechanism in any NCL gene.
- **Germline mosaicism:** not documented as a recurrence mechanism; recurrence risk for AR members is the standard 25%. Note the *de novo* p.Tyr295Cys *CLN6* allele in Cypriot family 926 (PMID:34868216) — a *de novo* event on one allele in an otherwise recessive disorder, which alters recurrence counselling for that family.
- **Consanguinity:** a major contributor. Homozygosity for private missense alleles in consanguineous pedigrees is the modal route to the non-CLN3 juvenile forms (Cypriot, Chinese, Somali, Turkish, Roma reports).
- **Carrier frequency:** *PPT1* 1/75 in Finns; *PPT1*, *TPP1*, *CLN3* each ~1/500 US-adjusted (PMID:27553520).

### 9.3 Population demographics and geography

| Population | Enriched gene / allele | Note |
|---|---|---|
| Finland | *CLN8* p.Arg24Gly (EPMR, Kainuu region); *CLN5* p.Tyr392\*; *PPT1* p.Arg122Trp | Finnish disease heritage; highest juvenile NCL prevalence in the Scandinavian survey |
| Northern/Western European ancestry | *CLN3* 1.02-kb deletion | The dominant juvenile NCL allele worldwide by count |
| Roma (former Czechoslovakia) | *MFSD8* p.Thr294Lys | 14 patients from 12 families, founder effect (PMID:19201763) |
| Turkey | *MFSD8*, *CLN8*, *CLN6* | Overrepresented in vLINCL series; high consanguinity |
| Newfoundland | multiple | Distinct genetic epidemiology (Clin Genet 2008; PMID:18684116) |
| Greek-Cypriot | *CLN6* p.Arg136His | Juvenile onset without visual loss (PMID:34868216) |
| Somali | *CTSD* p.Gly149Val | Juvenile CLN10 sibship |
| South America / Caribbean | mixed | Regional overview: Front Neurol 2022 (PMID:36034292) |
| Russia | *CLN* spectrum incl. novel alleles | Mol Genet Genomic Med 2020 (PMID:32412666) |

- **Sex ratio: 1:1.** Autosomal recessive; no sex bias in incidence. (The Cypriot *CLN6* series happened to be all male — a chance finding in n=3, not a sex effect.)
- **Age distribution of affected individuals:** by definition onset 5–10 y; the prevalent population spans childhood through the third decade (longer for protracted members).

---

## 10. Diagnostics

### 10.1 The diagnostic algorithm for a suspected juvenile NCL

This is the practical heart of the entity, and it is genuinely *different* from the CLN3-only algorithm.

**Step 1 — Recognise the syndrome.** School-age child with progressive visual failure + retinal dystrophy, *or* new-onset epilepsy with cognitive regression, *or* progressive ataxia with cognitive decline.

**Step 2 — Enzyme assays first (fast, cheap, and immediately actionable).** In leukocytes, fibroblasts, or dried blood spot:
- **TPP1** (CLN2) — *do this first*: it is the only NCL with an approved therapy.
- **PPT1** (CLN1) — will catch juvenile CLN1, which EM would mislabel as infantile.
- **Cathepsin D** (CLN10).

A normal result on all three excludes three of the nine defensible members in days.

**Step 3 — Blood film for vacuolated lymphocytes.** Positive → strongly suggests CLN3. Cheap, immediate, and one of the few within-grouping discriminators available at the bedside.

**Step 4 — Molecular testing.** Targeted *CLN3* common-deletion PCR if the phenotype is classic; otherwise, and in all enzyme-negative cases, **a multigene NCL panel** covering at minimum *PPT1, TPP1, CLN3, DNAJC5, CLN5, CLN6, MFSD8, CLN8, CTSD, GRN, ATP13A2, CTSF, KCTD7*. **Exome or genome sequencing** where panel is negative or where the differential is broader (juvenile-onset ataxia, PME, or retinal dystrophy differentials). GTR lists dedicated NCL/Batten panels.
- **Copy-number analysis must be included** — the *CLN3* 1.02-kb deletion and multi-exon deletions in other NCL genes are missed by SNV-only pipelines.
- **A known WES failure mode:** in-frame duplications can be missed by both Sanger and WES through allelic dropout — the *DNAJC5* case in PMID:31919451. Reanalysis of raw WES data with modified protocols recovered it.

**Step 5 — Electron microscopy** (skin/conjunctival/rectal biopsy) is now second-line but retains value in molecularly unsolved cases. **Interpret ultrastructure as a pointer to the gene, not to the onset class** (§4.2).

### 10.2 Ultrastructural patterns (GeneReviews Table 2)

| Pattern | Genes |
|---|---|
| **GROD** (granular osmiophilic deposits) | *PPT1*, *CTSD*, *DNAJC5*, (+*CTSF*) |
| **Curvilinear** | *TPP1*, (+*CLN3*, *CLN5*, *CLN6*, *GRN*, *KCTD7*) |
| **Fingerprint** | *CLN3*, *MFSD8*, *GRN*, *CTSF*, *KCTD7*, (+*CLN5*, *CLN6*) |
| **Rectilinear** | *CLN5*, *CLN6*, *MFSD8*, *CLN3*, *KCTD7* |
| **Curvilinear-like fingerprint, granular** | *CLN8* |
| Mixed (GROD + others) | *CLN6* adult |

### 10.3 Imaging, electrophysiology, and other tests

- **MRI brain:** cerebellar atrophy (early and often disproportionate), progressive generalised cerebral atrophy, periventricular T2 white-matter hyperintensity, thalamic T2 hypointensity. In one *CLN6* sibship MRI severity diverged sharply between siblings with an identical genotype (PMID:35609511) — MRI is not a reliable genotype predictor.
- **ERG:** abnormal early, becomes **extinguished**; often the finding that first raises "retinal dystrophy" before the neurological diagnosis. **HP:0000512** → **HP:0000550**.
- **OCT / fundus autofluorescence:** retinal thinning, outer-retinal loss, abnormal autofluorescence (**HP:0030602**).
- **VEP:** enlarged/giant responses early (as in other PMEs), attenuating later.
- **EEG:** progressive slowing; generalised epileptiform discharges; **photoparoxysmal response at low flash frequencies** is a classic PME/NCL clue.
- **Nerve conduction:** may show sensory axonal neuropathy (*CTSD*; PMID:25298308).
- **Muscle biopsy:** not routine, but in *CTSD* deficiency shows **"granulovacuolar material in angular atrophic fibers in addition to the granular osmiophilic deposits"** (PMID:25298308).
- **CSF neurofilament light chain:** an emerging progression biomarker in NCL — **not validated for diagnosis**; do not curate as a diagnostic test.

LOINC coding exists for the enzyme assays and for ERG; ⚠️ *specific LOINC codes were not retrieved this session.*

### 10.4 Omics-based diagnostics

- **RNA sequencing** has a real role: resolving splice-region VUS in NCL genes (functional splicing evidence for ACMG PS3/BS3). Worth curating as an adjunct, not a first-line test.
- **Proteomics / metabolomics / liquid biopsy:** no validated clinical diagnostic role for any NCL.
- **Epigenomics:** no role.

### 10.5 Clinical criteria and differential diagnosis

There are **no formal consensus diagnostic criteria** for "juvenile NCL" as a grouping. Diagnosis is by demonstration of a biallelic pathogenic genotype in an NCL gene, with a compatible juvenile-onset phenotype (and, historically, characteristic storage on EM).

**Differential diagnosis, organised by presenting syndrome** — this is where the grouping earns its keep:

| Presentation | Consider within the grouping | Consider outside |
|---|---|---|
| Juvenile visual failure + maculopathy | CLN3, CLN5, CLN7/MFSD8, CLN10, juvenile CLN1 | Stargardt disease (*ABCA4*), cone-rod dystrophy, retinitis pigmentosa, Leber hereditary optic neuropathy, non-syndromic *MFSD8* maculopathy |
| Juvenile epilepsy + regression | CLN6, CLN8/EPMR, CLN3, CLN2-juvenile | Lafora disease (*EPM2A/NHLRC1*), Unverricht-Lundborg (*CSTB*), MERRF, sialidosis, Gaucher type 3, juvenile Huntington disease, DRPLA, SSPE |
| Juvenile progressive ataxia | *TPP1*-SCAR7, CLN5, CLN6, CLN10 | Friedreich ataxia, ataxia-telangiectasia, AOA1/2, Niemann-Pick type C, mitochondrial ataxias |
| Juvenile parkinsonism | ATP13A2/CLN12 | *PRKN*/*PINK1*/*DJ-1* juvenile parkinsonism, Wilson disease, PKAN/NBIA, dopa-responsive dystonia |
| Juvenile dementia + psychosis | CLN3 | Niemann-Pick type C (a critical and treatable-adjacent mimic), Wilson disease, juvenile Huntington, subacute sclerosing panencephalitis, mitochondrial disease |

**Niemann-Pick type C and Wilson disease deserve specific mention** as the two mimics where missing the diagnosis has the greatest therapeutic cost.

### 10.6 Screening

- **Newborn screening: not implemented anywhere** for any NCL. TPP1 enzyme activity in dried blood spot is technically NBS-compatible and has been piloted; the argument for it strengthened materially once cerliponase alfa was approved, but it targets CLN2 (predominantly late-infantile), not the juvenile grouping. Adding NCL to RUSP-type panels remains an open policy question.
- **Carrier screening:** available for known familial variants; expanded carrier-screening panels increasingly include *CLN3*, *PPT1*, *TPP1*. Population carrier screening is not recommended outside founder populations.
- **Cascade screening of siblings** is the highest-yield screening activity, because it can identify a presymptomatic sibling within the therapeutic window.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

- **Uniformly fatal** for the classic members. **No cure exists for any form.**
- **CLN3:** life expectancy typically **second to third decade**; deaths reported from late teens into the 30s and occasionally 40s.
- **Juvenile CLN1:** generally **more rapid** than CLN3.
- **Protracted members** (*TPP1*-SCAR7, protracted *MFSD8*, *CLN8*-EPMR): survival into the **fourth to sixth decade**, with EPMR patients reaching middle age.
- **Mortality mechanisms:** aspiration pneumonia (the leading cause), respiratory failure, status epilepticus, and — in CLN3 specifically — cardiac arrhythmia/conduction disease in the second-to-third decade.
- ⚠️ *No formal 5-/10-year survival statistics exist for the grouping. There is no SEER-equivalent registry. Any percentage survival figure encountered in the literature is almost certainly CLN3-specific and cohort-specific — do not generalise it to MONDO:0019262.*

### 11.2 Morbidity and function

Profound and cumulative: blindness → dementia → epilepsy → loss of ambulation → loss of speech → gastrostomy dependence → total care dependence. Effectively 100% disability by the end of the second decade in the classic members. Very high caregiver burden; the psychiatric phase in CLN3 adolescence is repeatedly reported as the hardest for families.

**Quality-of-life instruments:** no NCL-specific validated QoL instrument is in general use. Generic pediatric instruments (PedsQL, EQ-5D-Y) are poorly suited once vision and cognition are lost. The **UBDRS capability subscale** is the closest available functional measure and is CLN3-validated only. **This is a documented measurement gap, and the honest curation statement is that grouping-level QoL data do not exist.**

### 11.3 Complications

Status epilepticus; aspiration pneumonia; malnutrition and failure to thrive; contractures and neuromuscular scoliosis; osteopenia/fractures; pressure injury; sleep disorder; behavioural crisis and psychosis; in CLN3, cardiac conduction disease and arrhythmia; drug-refractory epilepsy.

### 11.4 Recovery potential

**None.** No spontaneous or treatment-induced remission has been described. Even the best-evidenced disease-modifying therapy (cerliponase alfa) **slows** decline rather than reversing it — a point the field states plainly (Zhang et al., PMID:39925015). Rehabilitation preserves function and comfort but does not alter trajectory.

### 11.5 Prognostic factors

- **Genotype is the dominant prognostic factor**, and is the strongest argument for pursuing molecular diagnosis even when it does not change treatment: it changes the prognosis conversation from "second-to-third decade" (CLN3) to "possibly middle age" (EPMR, SCAR7, protracted MFSD8).
- **Allele severity within a gene:** null/null → earlier onset and faster decline; hypomorph in trans → later onset, slower decline (the TPP1 CLN2-vs-SCAR7 dichotomy is the cleanest demonstration).
- **Age at onset:** earlier onset predicts faster progression, consistently across members.
- **Seizure control** and **nutritional/respiratory management** are the main modifiable prognostic factors.
- **Prognostic biomarkers:** none validated. CSF NfL and MRI volumetrics are under investigation.

---

## 12. Treatment

**Overarching statement:** there is **no approved disease-modifying therapy for MONDO:0019262 as a grouping**. There is exactly one approved disease-modifying therapy for one member gene (*TPP1*/CLN2), and a set of gene therapies in trial. Everything else is symptomatic and supportive.

### 12.1 Enzyme replacement therapy — *TPP1*/CLN2 only

**Cerliponase alfa (Brineura)** — recombinant human TPP1 delivered by **intracerebroventricular infusion** via an implanted reservoir, 300 mg every 2 weeks. Approved by FDA (2017) and EMA for CLN2 disease. Pivotal evidence:

> "The mean (±SD) unadjusted rate of decline in the motor-language score per 48-week period was 0.27±0.35 points in treated patients and 2.12±0.98 points in 42 historical controls."
> — Schulz A et al. *"Study of Intraventricular Cerliponase Alfa for CLN2 Disease."* N Engl J Med 2018;378(20):1898-1907 (**PMID:29688815**)

The trial enrolled **24 children aged 3–16**, all receiving 300 mg for at least 96 weeks; median time to a 2-point motor-language decline was not reached in treated patients versus 345 days in controls (P<0.001). Adverse events: convulsions, fever, vomiting, hypersensitivity reactions; **two patients developed device-related infections requiring antibiotic therapy and device replacement**.

**Relevance to this entity:** the age range 3–16 y means the trial population *included* juvenile-onset CLN2 patients. **Any child in the juvenile window with a compatible phenotype should have a TPP1 assay early**, because this is the one branch of the differential with an approved therapy. This single fact is the strongest clinical justification for modelling MONDO:0019262 as gene-heterogeneous rather than as CLN3.

- NCIT: `NCIT:C15986` Pharmacotherapy; `NCIT:C158784`? *(a specific cerliponase alfa NCIT code likely exists but was not verified this session)*. `therapeutic_modality: PROTEIN_REPLACEMENT`.
- ERT is **not extensible** to the transmembrane members (CLN3, CLN6, MFSD8, CLN8, ATP13A2) — there is no soluble enzyme to replace. Zhang et al.: ERT is *"limited to soluble lysosomal enzyme deficiencies due to blood-brain barrier challenges."*

### 12.2 Gene therapy (investigational)

AAV-vectored gene transfer, largely AAV9 by intrathecal or intracerebroventricular route. Trials have been run or are running for **CLN2, CLN3, CLN5, CLN6, and CLN7**:

| Target | Trial | Notes |
|---|---|---|
| **CLN3** | **NCT03770572** | Phase 1/2, open-label, single-dose, dose-escalation; intrathecal AAV9 (AT-GTX-502 / CLN-301); low- and high-dose cohorts, 5-year follow-up |
| **CLN6** | **NCT02725580** | Phase 1/2 intrathecal scAAV9.CB.CLN6 for variant late-infantile CLN6 |
| **CLN6** | **NCT07582484** | Phase 1/2b, scAAV9-delivered *CLN6*; estimated start August 2026 |
| **CLN7/MFSD8** | first-in-human high-dose AAV9 intrathecal, phase 1 open-label single ascending dose (published; PMC12703863) | |
| **CLN5** | natural-history study **NCT03822650** underpinning trial design | |

Preclinical support is strongest where large-animal models exist: intracerebroventricular scAAV9.CB.CLN6 *"significantly alleviates motor defects, delays learning and memory impairment, and extends lifespan"* (reviewed in PMID:39925015), and the naturally occurring ovine *CLN5*/*CLN6* models have carried much of the translational work (§15).

NCIT: `NCIT:C15238` Gene Therapy; `therapeutic_modality: GENE_THERAPY`.

### 12.3 RNA-based therapy

**Milasen** — the landmark *n*-of-1 patient-customised splice-modulating antisense oligonucleotide, designed against a cryptic splice-acceptor site created by a *MFSD8*/CLN7 retrotransposon insertion, designed, manufactured, and dosed within about a year (Kim J et al., N Engl J Med 2019;381:1644-1652). ⚠️ *The PMID for this paper could not be confirmed by the searches run this session — verify before citing.* Referenced in the 2025 review as *"Milasen, designed to target…cryptic splice-acceptor site"* (PMID:39925015).

**Significance for this entity:** milasen is the proof of concept that a *private* allele in a *rare* member of this grouping can be drugged, and is a strong argument for exact molecular diagnosis rather than a syndromic "juvenile NCL" label.

NCIT: `NCIT:C15986`; `therapeutic_modality: ANTISENSE_OLIGONUCLEOTIDE`; `aso_mechanism: SPLICE_MODULATION_EXON_INCLUSION` *(mechanism assignment should be confirmed against the primary paper)*.

### 12.4 Other investigational and repurposed approaches

- **Miglustat** — substrate-reduction agent; open-label safety/PK/efficacy study in CLN3 (**NCT05174039**).
- **Mycophenolate mofetil** — immunosuppression rationale from the autoimmune/neuroinflammatory arm of CLN3 pathogenesis (NCT01399047).
- **Small molecules:** NtBuHA (a cysteamine-derived thioesterase mimetic, CLN1), **trehalose** (autophagy inducer), **gemfibrozil** (PPARα agonist) — all preclinical/early (PMID:39925015).
- **Hematopoietic stem-cell gene therapy:** *"Overexpressing PPT1 on hematopoietic stem cells… has been shown to extend the lifespan of CLN1-deficient mice"* (PMID:39925015). **Unmodified HSCT has not shown benefit in NCL and should not be offered.**
- **Microglial replacement therapies** — an emerging concept given the centrality of neuroinflammation.
- **Investigations of Juvenile Neuronal Ceroid Lipofuscinosis** — **NCT03307304**; **Natural History Study of Batten Disease** — **NCT04644549**.

### 12.5 Symptomatic and supportive care (the mainstay)

| Domain | Intervention | NCIT |
|---|---|---|
| Epilepsy | **Levetiracetam, valproate, lamotrigine, clobazam, zonisamide**. Myoclonus: levetiracetam, piracetam, clonazepam | `NCIT:C15986` Pharmacotherapy |
| ⚠️ **Drugs to avoid** | **Carbamazepine, oxcarbazepine, phenytoin, and (per PME practice) vigabatrin/tiagabine/gabapentin** may aggravate myoclonus and myoclonic seizures in progressive myoclonic epilepsies including NCL. This is an actionable prescribing caution worth curating explicitly. | — |
| Movement disorder | Trihexyphenidyl, baclofen, botulinum toxin for dystonia; levodopa trial in ATP13A2/CLN12 parkinsonism | `NCIT:C15986` |
| Psychiatric | Risperidone/other atypical antipsychotics for psychosis and agitation; SSRIs for anxiety | `NCIT:C15986` |
| Sleep | Melatonin | `NCIT:C15986` |
| Vision | Low-vision services, braille and orientation/mobility training, assistive technology — **initiate early, before cognitive decline forecloses learning** | `NCIT:C15315` Rehabilitation |
| Nutrition | Dysphagia assessment, thickened feeds, **gastrostomy** | `NCIT:C15433` Nutritional Support; `NCIT:C15329` Surgical Procedure |
| Respiratory | Chest physiotherapy, suctioning, aspiration precautions, vaccination | `NCIT:C15747` Supportive Care |
| Musculoskeletal | Physical and occupational therapy, seating/positioning, scoliosis surveillance and management | `NCIT:C15302` Physical Therapy; `NCIT:C121351` Occupational Therapy |
| Communication | Speech and language therapy; AAC before speech is lost | `NCIT:C159273` Speech Therapy |
| Cardiac (CLN3) | ECG/Holter surveillance from adolescence; pacemaker in selected cases | `NCIT:C15747` |
| Family | **Genetic counselling** | `NCIT:C15240` Genetic Counseling |
| End of life | Palliative care, advance care planning | `NCIT:C15747` Supportive Care |

### 12.6 Pharmacogenomics

No NCL-specific pharmacogenomic guidance exists. Standard CPIC guidance applies to the drugs used (e.g. *HLA-B\*15:02* and carbamazepine — moot here, since carbamazepine is relatively contraindicated; *CYP2C9*/*CYP2C19* for valproate/clobazam metabolism). PharmGKB has no NCL-specific entries.

### 12.7 Treatment strategy

The algorithm is short and genotype-gated:

1. **Establish the gene.** Enzyme assays → panel/WES → CNV analysis.
2. **If *TPP1*/CLN2 → refer for cerliponase alfa immediately.** This is the only branch with an approved therapy, and benefit depends on remaining function.
3. **If another member → assess trial eligibility** (CLN3 NCT03770572, CLN6 NCT02725580/NCT07582484, CLN7 AAV9, CLN5 natural history) and enrol in natural-history registries.
4. **In all cases → multidisciplinary symptomatic care** (neurology, ophthalmology/low vision, epileptology, gastroenterology/nutrition, rehabilitation, palliative care, genetics).
5. **In all cases → sibling cascade testing**, to catch a presymptomatic sibling while the therapeutic window is open.

---

## 13. Prevention

- **Primary prevention: not possible.** These are germline monogenic disorders. No vaccination, no risk-factor modification, no behavioural intervention affects occurrence. **Curate this section as explicitly not-applicable rather than inventing content.**
- **Reproductive prevention** is the only route that reduces incidence:
  - **Genetic counselling** (`NCIT:C15240`) — 25% recurrence risk for AR members; discussion of consanguinity where relevant.
  - **Carrier testing** of at-risk relatives once the familial variants are known.
  - **Prenatal diagnosis** (CVS/amniocentesis) and **preimplantation genetic testing for monogenic disease (PGT-M)** — both routine once the biallelic genotype is defined.
  - **Population carrier screening** in founder populations (Finland; Roma communities for *MFSD8* p.Thr294Lys) is technically justifiable; consanguineous-community screening programmes are the highest-yield setting.
- **Secondary prevention (early detection):**
  - **Cascade testing of siblings** — the single highest-value preventive act, and the only one that can place a child in the therapeutic window.
  - **Newborn screening** — not implemented; TPP1 dried-blood-spot assay is the leading candidate now that CLN2 is treatable. This is a live policy question, not current practice.
  - **Awareness-driven earlier diagnosis:** an ophthalmologist encountering a school-age child with rapidly progressive maculopathy and an abnormal ERG should consider NCL, not stop at "Stargardt". Diagnostic-delay reduction is the most tractable secondary-prevention target for this entity.
- **Tertiary prevention (complication avoidance):** seizure-medication optimisation with avoidance of myoclonus-aggravating agents; dysphagia surveillance and timely gastrostomy to prevent aspiration; scoliosis and contracture surveillance; cardiac surveillance in CLN3; vaccination and respiratory care.
- **Public health / environmental interventions: not applicable.**

---

## 14. Other Species / Natural Disease

NCL is one of the best examples in medicine of a human rare disease with **naturally occurring, breed-defined large-animal counterparts** — which is why NCL gene therapy has an unusually strong translational pipeline.

### 14.1 Taxonomy and natural disease

| Species | NCBITaxon | Gene(s) | Notes |
|---|---|---|---|
| Dog (*Canis lupus familiaris*) | NCBITaxon:9615 | *TPP1*, *CLN5*, *CLN6*, *CLN8*, *ATP13A2*, *PPT1*, *ARSG*, *CNP*, *MFSD8* | **OMIA:000181-9615** "Neuronal Ceroid Lipofuscinosis, generic in *Canis lupus familiaris*"; numerous breed-specific gene entries |
| Sheep (*Ovis aries*) | NCBITaxon:9940 | *CLN5* (Borderdale), *CLN6* (South Hampshire, Merino) | The premier large-animal models; used for MRI-based longitudinal studies and gene-therapy proof of concept |
| Cattle (*Bos taurus*) | NCBITaxon:9913 | *CLN5* | Devon cattle |
| Cat, goat, horse | — | various | Sporadic reports |
| Mouse (*Mus musculus*) | NCBITaxon:10090 | *Cln8* (**mnd**, naturally occurring), plus engineered alleles | The *mnd* mouse was identified as a natural *Cln8* mutant in the same paper that cloned human *CLN8* |

**Breeds (VBO):** Tibetan Terrier (*ATP13A2*/CLN12; onset 4–6 y, i.e. adult-equivalent in dog terms), American Staffordshire Terrier (*ARSG*, an NCL-like disorder with **no confirmed human juvenile NCL counterpart** — *ARSG* in humans causes Usher syndrome type IV), Border Collie and Golden Retriever (*CLN5*), Australian Shepherd and Schapendoes (*CLN6*), English Setter (*CLN8*), Dachshund (*TPP1*, *PPT1*), Miniature Schnauzer, Chihuahua. ⚠️ *Specific VBO identifiers were not retrieved this session.*

**Veterinary importance:** canine NCL is a genuine clinical veterinary disease with commercial DNA tests offered by breed clubs for carrier avoidance — a real-world instance of the carrier-screening logic in §13. Border Collie NCL in Japan has been the subject of a dedicated molecular-epidemiological study (PMID:22919312).

### 14.2 Orthologous genes

All human NCL genes have well-conserved orthologues across mammals; *PPT1*, *TPP1*, *CTSD*, *CLN3*, *CLN5*, *CLN6*, *CLN8*, *MFSD8*, and *ATP13A2* orthologues exist in mouse, rat, dog, sheep, and (for most) zebrafish and *Drosophila*. Alliance of Genome Resources and HomoloGene are the reference sources; ⚠️ *specific NCBI Gene IDs were not retrieved this session.*

### 14.3 Comparative biology

- **Conservation of mechanism is high**: lysosomal storage, SCMAS accumulation, autofluorescence, neuroinflammation, and retinal plus CNS neurodegeneration recur across species. Ranta et al. put the *CLN8*/*mnd* correspondence as *"the first description of the molecular basis of a naturally occurring animal model for NCL"* (PMID:10508524).
- **Key comparative divergence:** disease *tempo* and *retinal involvement* differ. Ovine *CLN5*/*CLN6* recapitulate retinal degeneration well (PMC8901734 — natural history of retinal degeneration in ovine CLN5/CLN6) and brain atrophy is trackable by MRI (PMC9830986); rodent models often under-recapitulate the retinal phenotype that dominates the human juvenile presentation.
- **Zoonotic potential / cross-species transmission: none.** Genetic disease; not transmissible.

---

## 15. Model Organisms

### 15.1 Mouse (*Mus musculus*, NCBITaxon:10090) — MGI, IMPC, IMSR, JAX

| Model | Type | Recapitulation | Limitations |
|---|---|---|---|
| ***Cln3*<sup>Δex7/8</sup>** knock-in | Knock-in of the human common 1.02-kb deletion | **The most translationally faithful CLN3 model**: storage, autofluorescence, gliosis, motor decline | Mild and late relative to human; **poor retinal phenotype**; near-normal lifespan — so it does not model the defining human feature (juvenile blindness) or lethality |
| *Cln3*<sup>−/−</sup> | Knockout | Storage, neuroinflammation | Same mildness problem |
| *Ppt1*<sup>−/−</sup> | Knockout | GROD storage, seizures, retinal degeneration, shortened lifespan | Models infantile CLN1, **not** juvenile CLN1 |
| *Tpp1*/*Cln2* mouse | Knockout | Good phenotypic fidelity; used for cerliponase alfa development | Models late-infantile CLN2 |
| *Cln5*<sup>−/−</sup> | Knockout | Storage, gliosis, visual dysfunction | Mild motor phenotype |
| ***Cln6*<sup>nclf</sup>** | Spontaneous frameshift | Storage, retinal degeneration, motor decline, shortened lifespan — a good model | Late-infantile-equivalent tempo |
| ***Cln8*<sup>mnd</sup>** (motor neuron degeneration) | **Naturally occurring** 1-bp insertion (267-268insC, codon 90) | Retinal degeneration, motor neuron degeneration, storage | Was the model that enabled human *CLN8* cloning (PMID:10508524) |
| *Mfsd8*/*Cln7*<sup>−/−</sup> | Knockout | Storage, retinal and CNS degeneration | Used for AAV9/MFSD8 preclinical work |
| *Ctsd*<sup>−/−</sup> | Knockout | Severe, early-lethal (~postnatal day 26) with GROD | Models **congenital** CLN10, not juvenile |
| *Grn*<sup>−/−</sup> | Knockout | *"Reexamination of progranulin-deficient mice revealed rectilinear profiles typical of NCL"* (PMID:22608501) | Lipofuscinosis without frank early neurodegeneration; models the homozygous-*GRN* NCL better than it models FTLD |
| *Atp13a2*<sup>−/−</sup> | Knockout | Lipofuscinosis, gliosis, mild motor | **No robust nigral dopaminergic loss** — a major limitation for the KRS/parkinsonism phenotype |
| *Kctd7*<sup>−/−</sup>, *Ctsf*<sup>−/−</sup>, *Dnajc5* models | Various | Partial | |

**Conditional and cell-type-specific alleles** exist for several (notably *Cln3* and *Ppt1*), enabling dissection of the neuron-vs-glia contribution to neuroinflammation.

**Cross-cutting mouse limitation, stated honestly:** *the mouse models under-recapitulate the two features that define the human juvenile phenotype — early profound visual failure and death in the second-to-third decade.* A dismech entry should record this as a `HUMAN_MODEL_MISMATCH` discussion rather than a generic knowledge gap: the evidence exists in the model, but its translational validity for the juvenile-onset human phenotype is the open question.

### 15.2 Large animals — the translational workhorses

- **Sheep:** the **Borderdale *CLN5*** and **South Hampshire / Merino *CLN6*** flocks (New Zealand) are naturally occurring, well-characterised, and gyrencephalic with a brain size and lifespan permitting realistic dosing, surgical delivery, and longitudinal imaging. Published resources include progressive MRI brain-volume studies (PMC9830986) and natural-history studies of retinal degeneration (PMC8901734). **These models carry much of the credibility of the CLN5/CLN6 gene-therapy programmes.**
- **Dog:** *TPP1* Dachshund, *CLN5* Border Collie/Golden Retriever, *CLN6* Australian Shepherd/Schapendoes/mixed-breed, *CLN8* English Setter, *ATP13A2* Tibetan Terrier. The Dachshund *TPP1* model contributed to ERT development.
- **Cattle:** Devon *CLN5*.

### 15.3 Non-mammalian and in vitro

- **Zebrafish (*Danio rerio*, NCBITaxon:7955)** — ZFIN; *cln3*, *mfsd8*, *ppt1*, *tpp1* morphants/mutants. Value: rapid, optically transparent, well-suited to **retinal phenotyping and small-molecule screening** — arguably the best system for the visual arm of this grouping.
- ***Drosophila melanogaster*** (NCBITaxon:7227) — FlyBase; *Cln3*, *Ppt1*, *Cln7* models for genetic-modifier screens.
- ***C. elegans***, **yeast** — used for CLN3 and MFSD8 orthologue function.
- **Patient-derived fibroblasts** — the practical workhorse for enzyme assays and storage-material characterisation; the substrate for the CTSD activity measurements in PMID:25298308.
- **iPSC-derived neurons, cerebral organoids, and retinal organoids** — the most promising human-relevant systems, and the only ones that can model the human-specific retinal vulnerability. Retinal organoids are particularly apt here given the vision-first phenotype.

### 15.4 Applications

Mechanism dissection (lysosomal storage, autophagy, neuroinflammation), biomarker discovery, preclinical efficacy and safety for AAV gene therapy and ERT, dose-finding and route-of-administration studies (large animals), and high-throughput drug screening (zebrafish, iPSC).

### 15.5 Resources

MGI, IMPC/KOMP, IMSR, JAX, EMMA, MMRRC (mouse); RGD (rat); ZFIN (zebrafish); FlyBase; WormBase; **OMIA (OMIA:000181 and gene-specific entries)** for natural animal disease; Alliance of Genome Resources for orthology; Cellosaurus/ATCC and Coriell (NIGMS repository holds NCL patient fibroblast lines) for cell models; the **UCL NCL Resource** (ucl.ac.uk/ncl-disease) for the mutation and patient database.

---

## 16. Curation guidance and verification status

### 16.1 The three claims this entry must make that a CLN3-anchored entry would not

1. **At least nine genes** — *CLN3, PPT1, TPP1, CLN5, CLN6, MFSD8, CLN8, CTSD, ATP13A2* — have defensible juvenile-onset presentations. CLN3 is the most prevalent, not the definition.
2. **Vision loss is typical but not necessary.** CLN8/EPMR and several CLN6 juvenile families present without visual failure. A definition requiring retinopathy would wrongly exclude real members.
3. **Onset class and gene are orthogonal axes.** The same gene can appear in the juvenile, late-infantile, *and* adult groupings via different alleles — *CLN6* spans all three. This is not an inconsistency to be resolved; it is the structure of the domain.

### 16.2 Members to exclude, and why

| Gene | Reason for exclusion |
|---|---|
| *DNAJC5*/CLN4 | Autosomal dominant, adult-onset Kufs. No juvenile phenotype. |
| *CTSF*/CLN13 | Adult Kufs type B. Onset >20 y. |
| *KCTD7*/CLN14 | Infantile/late-infantile PME. |
| *GRN*/CLN11 | "Teenage to adult" per GeneReviews; typical onset ~20–25 y. Adjacent, not a member. |
| "CLN9" | **Withdrawn.** No gene. The index family was reassigned to *CLN5*. Present in MONDO only as a legacy artefact. |

### 16.3 Ontology defects observed (worth reporting upstream)

1. MONDO:0019262 asserts only **five** children (MONDO:0979341 CLN1, MONDO:0979345 CLN2, MONDO:0979346 CLN3, MONDO:0012188 "NCL 9", MONDO:0017809 ATP13A2), while the literature supports at least nine members. **CLN5, CLN6, CLN7/MFSD8, CLN8, and CLN10 juvenile forms have no corresponding MONDO term.**
2. **MONDO:0012188 ("neuronal ceroid lipofuscinosis 9") is asserted as a child of the juvenile grouping despite CLN9 being a withdrawn designation** whose index family was reassigned to *CLN5*.
3. The **synonym overlap with MONDO:0008767** (`Vogt Spielmeyer disease`, `Spielmeyer Sjogren disease`, `Batten disease`) is the mechanical driver of the historical conflation and is worth flagging even though it accurately reflects historical usage.
4. MONDO:0979346 is correctly dual-parented (MONDO:0019262 + MONDO:0008767) but was **not returned by the OLS4 `/descendants` endpoint** — a retrieval inconsistency that could cause an automated member-enumeration script to silently miss the CLN3 member.

### 16.4 Verification status of citations in this report

**Fully transcribed abstracts (single-PMID E-utilities fetch; quotes in this report are verbatim from those transcriptions):**
PMID:21990111 · PMID:10508524 · PMID:31919451 · PMID:34868216 · PMID:35609511 · PMID:27553520 · PMID:23374165 · PMID:9151309 · PMID:22608501 · PMID:25227500 · PMID:22388936 · PMID:29688815

**Partial quotes only** (fragments returned inside multi-record fetches or PMC full-text extraction; the quoted strings are reliable but the surrounding abstract was summarised): PMID:22778232 · PMID:9425237 · PMID:23418007 · PMID:20157158 · PMID:19201763 · PMID:39281238 · PMID:25298308 · PMID:26026925 · PMID:39925015

**Cited but PMID or content NOT verified this session — verify before curating as evidence:**
- Wisniewski KE et al., "Reevaluation of neuronal ceroid lipofuscinoses: atypical juvenile onset may be the result of CLN2 mutations", *Mol Genet Metab* 1999 (exact-title query returned no results)
- International Batten Disease Consortium, "Isolation of a novel gene underlying Batten disease, CLN3", *Cell* 1995 (author/title queries returned no results)
- Kim J et al., "Patient-Customized Oligonucleotide Therapy for a Rare Genetic Disease" (milasen), *NEJM* 2019
- El Haddad et al. 2012, reassignment of the CLN9 family to *CLN5*
- Tyynelä et al., saposins A and D as the stored proteins in CLN1/CLN10
- The CLN3 1.02-kb deletion allele frequencies (~80–85% of alleles; ~70–75% homozygous)
- ICD-10 E75.4 assignment
- All GO, CL, UBERON, CHEBI, and NCIT identifiers suggested in this report, and HP:0001922 (vacuolated lymphocytes) and HP:0011675 (arrhythmia), which were **not** found in the local HP cache

**Verified against the local `cache/hp/terms.csv`:** every HP identifier in §3 other than HP:0001922 and HP:0011675.

**For dismech curation specifically:** every PMID cited here must go through `just fetch-reference PMID:XXXXXXXX`, and every snippet through `just count-verified-snippets`, before it enters a `kb/disorders/` entry. Several of the quotes above are drawn from PMC **full text** rather than the abstract (notably PMID:25298308) and will therefore **fail** the `--no-full-text` check that `just validate-disorders` and CI run — replace those with abstract-resident quotes or move the claims to `notes`. Ontology terms need `just validate-terms`.

---

## Sources

**Ontology / database records (retrieved live 2026-08-08)**
- [MONDO:0019262 — OLS4](https://www.ebi.ac.uk/ols4/api/v2/ontologies/mondo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0019262) · [MONDO:0008767 — OLS4](https://www.ebi.ac.uk/ols4/api/v2/ontologies/mondo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0008767) · [MONDO:0979346 — OLS4](https://www.ebi.ac.uk/ols4/api/v2/ontologies/mondo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0979346)
- [GeneReviews: Neuronal Ceroid-Lipofuscinoses (NBK1428)](https://www.ncbi.nlm.nih.gov/books/NBK1428/)
- [UCL NCL Resource — Mutation and Patient Database](https://www.ucl.ac.uk/ncl-disease/mutation-and-patient-database)
- [OMIA:000181-9615 — NCL, generic, in dog](https://omia.org/OMIA000181/9615/)
- [GARD: Juvenile neuronal ceroid lipofuscinosis](https://rarediseases.info.nih.gov/diseases/4938/juvenile-neuronal-ceroid-lipofuscinosis)

**Primary literature**
- [PMID:21990111 — Kousi, Lehesjoki, Mole. Hum Mutat 2012;33(1):42-63](https://pubmed.ncbi.nlm.nih.gov/21990111/)
- [PMID:26026925 — Mole & Cotman. Biochim Biophys Acta 2015;1852:2237-41](https://pubmed.ncbi.nlm.nih.gov/26026925/) · [PMC4567481](https://pmc.ncbi.nlm.nih.gov/articles/PMC4567481/)
- [PMID:22778232 — Williams & Mole. Neurology 2012;79(2):183-91](https://pubmed.ncbi.nlm.nih.gov/22778232/)
- [PMID:9425237 — Mitchison et al. Hum Mol Genet 1998;7(2):291-7 (juvenile CLN1/GROD)](https://pubmed.ncbi.nlm.nih.gov/9425237/)
- [PMID:23418007 — Sun et al. Hum Mutat 2013;34(5):706-13 (TPP1/SCAR7)](https://pubmed.ncbi.nlm.nih.gov/23418007/)
- [PMID:20157158 — Xin et al. Neurology 2010;74(7):565-71 (CLN5 juvenile)](https://pubmed.ncbi.nlm.nih.gov/20157158/)
- [PMID:34868216 — Front Genet 2021;12:746101 (CLN6 juvenile, no visual loss)](https://pubmed.ncbi.nlm.nih.gov/34868216/) · [PMC8640139](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8640139/)
- [PMID:35609511 — Neurodegener Dis 2021;21:126-131 (juvenile-onset Kufs, CLN6)](https://pubmed.ncbi.nlm.nih.gov/35609511/)
- [PMID:19201763 — Kousi et al. Brain 2009;132:810-9 (CLN7/MFSD8)](https://pubmed.ncbi.nlm.nih.gov/19201763/)
- [PMID:25227500 — Roosing et al. Ophthalmology 2015;122(1):170-9 (MFSD8 macular dystrophy)](https://pubmed.ncbi.nlm.nih.gov/25227500/)
- [PMID:10508524 — Ranta et al. Nat Genet 1999;23(2):233-6 (CLN8/EPMR, mnd mouse)](https://pubmed.ncbi.nlm.nih.gov/10508524/)
- [PMID:25298308 — Neurology 2014;83(20):1873-5 (CTSD juvenile ataxia)](https://pubmed.ncbi.nlm.nih.gov/25298308/) · [PMC4240432](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4240432/)
- [PMID:16685649 — Steinfeld et al. Am J Hum Genet 2006 (cathepsin D deficiency)](https://pubmed.ncbi.nlm.nih.gov/16685649/)
- [PMID:22388936 — Bras et al. Hum Mol Genet 2012;21(12):2646-50 (ATP13A2/CLN12)](https://pubmed.ncbi.nlm.nih.gov/22388936/)
- [PMID:22608501 — Smith et al. Am J Hum Genet 2012;90(6):1102-7 (GRN dosage)](https://pubmed.ncbi.nlm.nih.gov/22608501/)
- [PMID:31919451 — Jedličková et al. Eur J Hum Genet 2020;28(6):783-9 (DNAJC5, adult NCL gene list)](https://pubmed.ncbi.nlm.nih.gov/31919451/)
- [PMID:15349861 — Schulz et al. 2004 (the "CLN9" variant)](https://pubmed.ncbi.nlm.nih.gov/15349861/)
- [PMID:1535179 — Palmer et al. Am J Med Genet 1992 (SCMAS storage)](https://pubmed.ncbi.nlm.nih.gov/1535179/) · [PMID:7668326](https://pubmed.ncbi.nlm.nih.gov/7668326/)
- [PMID:27553520 — Gene 2016;593(2):284-91 (ExAC carrier frequencies)](https://pubmed.ncbi.nlm.nih.gov/27553520/)
- [PMID:23374165 — Orphanet J Rare Dis 2013;8:19 (Italian molecular epidemiology)](https://pubmed.ncbi.nlm.nih.gov/23374165/)
- [PMID:9151309 — Neuropediatrics 1997;28(1):6-8 (Scandinavian epidemiology)](https://pubmed.ncbi.nlm.nih.gov/9151309/)
- [PMID:39281238 — Pak J Med Sci 2024;40(8):1638-43 (pediatric NCL cohort)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11395386/)
- [PMID:29688815 — Schulz et al. N Engl J Med 2018;378(20):1898-1907 (cerliponase alfa)](https://pubmed.ncbi.nlm.nih.gov/29688815/)
- [PMID:39925015 — Zhang et al. CNS Neurosci Ther 2025;31(2):e70261](https://pmc.ncbi.nlm.nih.gov/articles/PMC11808193/)
- [PMID:32300063 — CLN3 Disease Staging System](https://pubmed.ncbi.nlm.nih.gov/32300063/) · [UBDRS validation, PMC9879304](https://pmc.ncbi.nlm.nih.gov/articles/PMC9879304/)
- [Nat Rev Neurol 2025 — NCL mechanisms and therapeutic targets](https://www.nature.com/articles/s41582-025-01132-4)

**Trials**
- [NCT03770572 — Gene Therapy for Children With CLN3 Batten Disease](https://clinicaltrials.gov/study/NCT03770572) · [NCT02725580 — CLN6 gene therapy](https://cdn.clinicaltrials.gov/large-docs/80/NCT02725580/Prot_000.pdf) · [NCT07582484 — CLN6 scAAV9](https://clinicaltrials.gov/study/NCT07582484) · [NCT05174039 — Miglustat in CLN3](https://cdn.clinicaltrials.gov/large-docs/39/NCT05174039/Prot_000.pdf) · [NCT03822650 — CLN5 natural history](https://clinicaltrials.gov/study/NCT03822650) · [NCT04644549 — Natural History Study of Batten Disease](https://clinicaltrials.gov/study/NCT04644549) · [NCT03307304 — Investigations of JNCL](https://clinicaltrials.gov/study/NCT03307304) · [CLN7 AAV9 phase 1, PMC12703863](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12703863/)

**Animal models**
- [Ovine CLN5/CLN6 MRI brain volume, PMC9830986](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9830986/) · [Ovine CLN5/CLN6 retinal natural history, PMC8901734](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8901734/) · [CLN6 mixed-breed dog, PMC11203140](https://pmc.ncbi.nlm.nih.gov/articles/PMC11203140/)
