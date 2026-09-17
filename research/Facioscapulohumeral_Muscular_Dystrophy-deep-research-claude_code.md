---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T19:31:00.604677'
end_time: '2026-07-31T19:35:46.046411'
duration_seconds: 285.44
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Facioscapulohumeral Muscular Dystrophy
  mondo_id: ''
  category: Genetic
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 17
  num_turns: 19
  total_cost_usd: 1.7294569
  session_id: 48b2469d-2e0b-54ee-9a3e-76c9362b0d69
  stop_reason: end_turn
citation_count: 46
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Facioscapulohumeral Muscular Dystrophy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Facioscapulohumeral Muscular Dystrophy** covering all of the
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

# Facioscapulohumeral Muscular Dystrophy (FSHD) — Comprehensive Research Report

## 1. Disease Information

**Overview:** Facioscapulohumeral muscular dystrophy (FSHD) is an autosomal dominant, progressive skeletal myopathy classically characterized by weakness beginning in the facial muscles, muscles stabilizing the scapula (periscapular/shoulder girdle), and foot dorsiflexors, with later, often asymmetric, involvement of the trunk, hip girdle, and lower limbs. It is the third most common inherited muscular dystrophy after Duchenne/Becker and myotonic dystrophy. Onset is typically in the first three decades of life (95% show clinical signs before age 20), severity is highly variable (even within families), progression is slow but steady, and life expectancy is generally not shortened, although up to ~20–24% of affected individuals eventually require wheelchair use ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/n/gene/fsh/); [5-year natural history study, PMID:39508285](https://pubmed.ncbi.nlm.nih.gov/39508285/)).

**Key identifiers:**
- **OMIM:** #158900 (FSHD1), #158901 (FSHD2, digenic)
- **MONDO:** MONDO:0001347 (disease umbrella); FSHD1/FSHD2 subtypes are separately mapped in MONDO/OMIM
- **ICD-10-CM:** G71.02 (Facioscapulohumeral muscular dystrophy), under G71.0 (Muscular dystrophy)
- **ICD-11:** 8C70.3
- **Disease Ontology:** DOID:11727 (FSHD), DOID:0111192
- **MeSH:** D020391 (Muscular Dystrophy, Facioscapulohumeral)
- **Orphanet:** ORPHA:269 (FSHD), with ORPHA:2044/369 for FSHD1/FSHD2 subtypes

**Synonyms:** Landouzy-Dejerine muscular dystrophy; FSHD; facioscapulohumeral dystrophy (FSHMD).

**Evidence source note:** Most information below derives from aggregated disease-level resources (OMIM, GeneReviews, Orphanet), large clinical cohort/registry studies (French, Italian, Dutch, US national registries), and primary molecular/cell-biology literature — individually cited by PMID where possible; a smaller subset (mouse/zebrafish models) is model-organism evidence, explicitly flagged.

Sources: [GeneReviews — FSHD](https://www.ncbi.nlm.nih.gov/books/n/gene/fsh/) · [OMIM #158900](https://www.omim.org/entry/158900) · [OMIM #158901](https://www.omim.org/entry/158901) · [NORD](https://rarediseases.org/rare-diseases/facioscapulohumeral-muscular-dystrophy/) · [ICD10Data G71.02](https://www.icd10data.com/ICD10CM/Codes/G00-G99/G70-G73/G71-/G71.02)

---

## 2. Etiology

### Disease causal factors — genetic, chromatin-based mechanism
FSHD is fundamentally a **chromatin-derepression disease**, not a classic loss-of-function/structural-protein myopathy. Both molecular subtypes converge on the same final pathogenic event: **inappropriate somatic expression of the DUX4 retrogene** in skeletal muscle.

- **FSHD1 (~95% of cases):** monoallelic **contraction of the D4Z4 macrosatellite repeat array** in the subtelomeric region of chromosome 4q35, from the normal 11–150 repeat units down to **1–10 units**, occurring specifically on a "permissive" **4qA haplotype** that provides a polyadenylation signal (PAS) distal to the last repeat unit, stabilizing the DUX4 transcript.
- **FSHD2 (<5% of cases):** normal-sized (non-contracted) D4Z4 array but **digenic inheritance** of (1) a permissive 4qA haplotype in trans, plus (2) a loss-of-function variant in a chromatin-modifier gene — most commonly **SMCHD1** (chromosome 18), and less commonly **DNMT3B** or **LRIF1** — that causes genome-wide/D4Z4-specific hypomethylation.

> "Digenic inheritance of an SMCHD1 mutation and an FSHD-permissive D4Z4 allele causes facioscapulohumeral muscular dystrophy type 2" ([Lemmers et al. 2012, PMID:23143600](https://pubmed.ncbi.nlm.nih.gov/23143600/))

- **SMCHD1 as a disease-severity modifier in FSHD1:** independent of causing FSHD2, hypomorphic SMCHD1 variants can act as a *second hit* in FSHD1 families, worsening severity when co-inherited with a D4Z4 contraction ([Sacconi et al. 2013, PMID:24075187](https://pubmed.ncbi.nlm.nih.gov/24075187/)).

### Risk factors
- **Genetic:**
  - D4Z4 repeat number is inversely correlated with severity/earlier onset — the shortest arrays (1–3 units) produce infantile/severe disease.
  - Reduced-penetrance ("grey zone") alleles of 8–11 repeat units on a permissive haplotype confer variable, epigenetically-modulated penetrance.
  - SMCHD1 loss-of-function variants (modifier in FSHD1; causal in FSHD2).
  - The non-permissive 4qB haplotype and homologous chromosome 10q35 D4Z4 repeats are **not** pathogenic even when contracted, because they lack the stabilizing PAS.
- **Environmental/demographic:** Sex — males are more frequently and more severely affected than females at any given repeat size (a documented sex-modifier effect, mechanism not fully resolved); no clear toxin/occupational/infectious risk factors identified. Age of onset is a marker of severity (earlier onset → more severe course; PMID:30819914 / Neurology 2019 review referenced above).
- **Ancestry:** Population studies note genetic and haplotype diversity affecting FSHD across ancestries; diagnostic algorithms developed largely in European cohorts under-recognize some non-European allele configurations ([*J Hum Genet* 2025](https://www.nature.com/articles/s10038-025-01401-6)).

### Protective factors
- Longer residual D4Z4 arrays (11+ units) on a permissive haplotype are largely non-penetrant.
- Non-permissive 4qB haplotype is protective regardless of repeat number.
- Intact SMCHD1/DNMT3B/LRIF1 function maintaining D4Z4 heterochromatinization is protective against DUX4 de-repression.
- No established pharmacologic/dietary protective factor is validated in humans to date.

### Gene–environment interactions
The core "interaction" in FSHD is **genetic epistasis rather than classic gene-environment interaction**: D4Z4 copy number, haplotype (cis) and SMCHD1/DNMT3B/LRIF1 genotype (trans, modifying chromatin state) jointly determine whether the chromatin permits DUX4 transcription. Muscle-intrinsic stressors (oxidative stress, myogenic differentiation state) modulate DUX4 expression level within a genetically permissive substrate, but there is no established exogenous environmental trigger. Suggested GENO/relationship modeling: SMCHD1 as `MODIFIER`/`SUSCEPTIBILITY` in FSHD1 entries; DUX4 (D4Z4-encoded) as the primary causal locus.

Sources: [Lemmers 2012, PMID:23143600](https://pubmed.ncbi.nlm.nih.gov/23143600/) · [Sacconi 2013, PMID:24075187](https://pubmed.ncbi.nlm.nih.gov/24075187/) · [OMIM 158901](https://www.omim.org/entry/158901) · [Genetic and Epigenetic Contributors to FSHD, PMC4674299](https://pmc.ncbi.nlm.nih.gov/articles/PMC4674299/)

---

## 3. Phenotypes

| Phenotype | Type | Onset | Frequency | Suggested HPO term |
|---|---|---|---|---|
| Facial weakness (orbicularis oris/oculi) | Physical sign | Childhood–young adult | Very frequent, often earliest sign | HP:0000371 (facial palsy) / HP:0025336 (facial diplegia) |
| Inability to whistle / pucker lips | Symptom | Often first noticed | Common | HP:0031202 or descriptive |
| Scapular winging | Physical sign | Early | Very frequent, hallmark | HP:0003691 |
| Shoulder girdle weakness | Physical sign | Early | Very frequent | HP:0003547 |
| "Popeye arm" (biceps/triceps sparing deltoid relatively) | Physical sign | Progressive | Frequent | HP:0033653 (descriptive) |
| Foot dorsiflexor (tibialis anterior) weakness / foot drop | Physical sign | Variable, often subclinical early | Frequent | HP:0009027 |
| Asymmetric limb weakness | Physical sign | Progressive | Very frequent, distinguishing feature | HP:0100568 |
| Abdominal muscle weakness (Beevor sign) | Physical sign | Later | Frequent | HP:0003707 |
| Lumbar hyperlordosis | Physical sign | Progressive | Frequent | HP:0002938 |
| Pelvic girdle weakness / difficulty climbing stairs | Symptom | Later-stage | Common in progressive disease | HP:0003749 |
| Sensorineural hearing loss (high-frequency) | Lab/clinical sign | Any age, often subclinical | ~64–75% (extramuscular) | HP:0000407 |
| Retinal telangiectasia / vasculopathy (Coats-like) | Clinical/imaging sign | Any age | ~49–75% (mostly asymptomatic) | HP:0025637 / HP:0000651 (Coats disease-like) |
| Coats disease with exudative retinal detachment (rare, severe) | Clinical complication | Usually infantile-onset cases | Rare but sight-threatening | HP:0025637 |
| Respiratory insufficiency (restrictive) | Clinical/functional | Late-stage, more common in wheelchair-dependent patients | Occasional-frequent in advanced disease | HP:0002093 |
| Fatigue / chronic pain | Symptom | Any stage | Very common, patient-reported | HP:0012378 / HP:0012531 |
| Intellectual disability / epilepsy (infantile FSHD only) | Neurodevelopmental | Infantile-onset | Rare, seen with very short (1–3 unit) D4Z4 arrays | HP:0001249 / HP:0001250 |
| Cardiac involvement (arrhythmia — debated) | Clinical sign | Variable | Rare/controversial, less prominent than in other dystrophies | HP:0011675 |

**Progression/severity pattern:** Slowly progressive, often asymmetric, "descending" pattern (face → shoulder girdle → trunk/foot dorsiflexors → hip girdle/proximal legs); quantitative muscle strength declines ~1–4%/year on average, with substantial inter-individual variability ([5-year natural history, PMID:39508285](https://pubmed.ncbi.nlm.nih.gov/39508285/); [Statland 2019 Neurology, early-onset severity marker](https://www.neurology.org/doi/abs/10.1212/WNL.0000000000006819)).

**Quality of life impact:** Chronic pain, fatigue, and mobility limitation (up to 20–24% requiring wheelchair by disease course) are major drivers of reduced quality of life; facial weakness affects speech/expression and social functioning; scapular winging and shoulder weakness substantially limit overhead activity and activities of daily living.

Sources: [Pediatric Review of FSHD, PMC6435288](https://pmc.ncbi.nlm.nih.gov/articles/PMC6435288/) · [Ophthalmologic Manifestations of FSHD — EyeWiki](https://eyewiki.org/Ophthalmologic_Manifestations_of_Facioscapulohumeral_Dystrophy) · [Retinal vascular disease and hearing loss in FSHD, PMID:23573590](https://pubmed.ncbi.nlm.nih.gov/23573590/) · [Longitudinal childhood-onset FSHD, PMC11655134](https://pmc.ncbi.nlm.nih.gov/articles/PMC11655134/)

---

## 4. Genetic/Molecular Information

**Causal loci:**
- **DUX4** (Double homeobox 4; HGNC:50800), encoded within each D4Z4 repeat unit on chromosome 4q35, subtelomeric. OMIM gene: *DUX4, 606009. This is the pathogenic effector gene for both FSHD1 and FSHD2.
- **D4Z4 repeat array** itself (a 3.3-kb macrosatellite, not a conventional gene) — copy number is the causal structural variant in FSHD1.
- **SMCHD1** (Structural Maintenance of Chromosomes flexible Hinge Domain containing 1; HGNC:29092), chromosome 18p11.32. OMIM *614982. Primary FSHD2 gene; modifier in FSHD1.
- **DNMT3B** (DNA methyltransferase 3 beta; HGNC:2979), chromosome 20q11.21. OMIM *602900. Rare FSHD2 gene.
- **LRIF1** (Ligand Dependent Nuclear Receptor Interacting Factor 1; HGNC:21470), chromosome 1p13.2. Very rare FSHD2 gene, converges with SMCHD1 at the D4Z4 locus and its own promoter ([PMC10307901](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10307901/)).

**Pathogenic variant classes:**
- FSHD1: not a point-mutation disease — the pathogenic lesion is a **repeat contraction** (structural variant), classified/sized by pulsed-field gel electrophoresis (EcoRI fragment size), Southern blot, or optical genome mapping. Contracted alleles of 1–10 units are pathogenic; 8–11 units on a permissive haplotype represent reduced-penetrance "grey zone" alleles.
- FSHD2 (SMCHD1/DNMT3B/LRIF1): predominantly **loss-of-function variants** — nonsense, frameshift, splice-site, and some missense variants disrupting ATPase or hinge domains of SMCHD1 — classified pathogenic/likely pathogenic per ACMG/AMP criteria in ClinVar.
- **Allele frequency:** Because pathogenic D4Z4 contractions are structural/repeat-based, they are not well-represented in standard SNV population databases (gnomAD/1000 Genomes); permissive 4qA vs. non-permissive 4qB/10q-derived haplotype frequencies have been characterized by haplotype-specific genotyping across populations.
- **Somatic vs. germline:** FSHD1 contractions and FSHD2 variants are typically germline (heritable), but **somatic mosaicism is common**: found in ~40% of *de novo* FSHD1 families (patient or unaffected parent), often via an intrachromosomal gene-conversion-like mechanism, sometimes involving mitotic interchromosomal exchange between 4q35 and its homologous 10q26 locus ([Lemmers 2004, PMID:15174019](https://pubmed.ncbi.nlm.nih.gov/15174019/); [van der Maarel 2000, PMID:10631134](https://pubmed.ncbi.nlm.nih.gov/10631134/)). Germline mosaicism is also documented and important for recurrence-risk counseling in apparently *de novo* cases.
- **Functional consequence:** Loss of D4Z4-array heterochromatin repression (FSHD1: reduced unit number reduces chromatin-packing capacity; FSHD2: SMCHD1/DNMT3B/LRIF1 LOF removes the trans-acting silencing machinery) → chromatin opening/hypomethylation → **DUX4 gain-of-function** (ectopic transcription factor expression) is the shared functional endpoint. This is best framed as a **gain-of-function toxic-protein mechanism secondary to an epigenetic derepression event**.

**Modifier genes:** SMCHD1 (in FSHD1), and D4Z4 repeat number itself modifies FSHD2 penetrance/severity (larger residual arrays in FSHD2 patients still require SMCHD1 hypomorphism to permit DUX4 expression).

**Epigenetic information:** The central epigenetic lesion is **loss of D4Z4 CpG methylation and repressive heterochromatin marks** (reduced H3K9me3, loss of SMCHD1-dependent chromatin compaction) at the contracted (FSHD1) or SMCHD1-destabilized (FSHD2) D4Z4 array, permitting transcription factor access and stabilized DUX4 mRNA via the distal permissive PAS. DNA-methylation analysis of D4Z4 (bisulfite sequencing) is diagnostically useful, particularly for confirming FSHD2 when repeat size is normal.

**Chromosomal context:** No aneuploidy/large structural chromosomal abnormality is causal; the key structural feature is the tandem-repeat copy-number variant at 4q35, and the near-identical but non-pathogenic homologous repeat array at 10q26 (a recognized source of diagnostic confusion requiring haplotype-specific testing).

Suggested ontology bindings: gene `hgnc:50800` (DUX4), `hgnc:29092` (SMCHD1), `hgnc:2979` (DNMT3B), `hgnc:21470` (LRIF1); GO biological process GO:0006325 (chromatin organization), GO:0006306 (DNA methylation).

Sources: [Genetic and Epigenetic Contributors to FSHD, PMC4674299](https://pmc.ncbi.nlm.nih.gov/articles/PMC4674299/) · [SMCHD1/LRIF1 convergence, PMC10307901](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10307901/) · [Somatic mosaicism, PMID:15174019](https://pubmed.ncbi.nlm.nih.gov/15174019/) · [OMIM 158901](https://www.omim.org/entry/158901)

---

## 5. Environmental Information

FSHD has **no established environmental, toxic, occupational, or infectious causal or triggering factor** — it is a monogenic/digenic disease driven entirely by the D4Z4/DUX4 chromatin mechanism above. No lifestyle factor (smoking, diet, alcohol) has been shown to alter disease risk or onset, though general muscle-health lifestyle measures (avoiding disuse, moderate aerobic/resistance exercise under supervision) are recommended as supportive management, not causal-risk mitigation (see Treatment/Prevention). No infectious agent is implicated. This section is largely **not applicable** for FSHD beyond noting the absence of such factors — a point worth explicitly recording rather than omitting.

---

## 6. Mechanism / Pathophysiology

**Causal chain (trigger → clinical manifestation):**

1. **Trigger:** D4Z4 repeat contraction (FSHD1) or SMCHD1/DNMT3B/LRIF1 loss-of-function on a background of a normal-length D4Z4 array (FSHD2), both occurring in cis/trans with a permissive 4qA haplotype.
2. **Chromatin derepression:** Loss of D4Z4 heterochromatin (reduced CpG methylation, reduced repressive histone marks, SMCHD1-dependent chromatin compaction failure) → open chromatin state at the distal D4Z4 unit.
3. **Stabilized DUX4 transcription:** The permissive 4qA polyadenylation signal stabilizes the DUX4-fl (full-length) transcript, which would otherwise be degraded. Only DUX4-fl (retaining its C-terminal transactivation domain) is transcriptionally active.
4. **DUX4 target-gene activation:** DUX4 is a double-homeodomain transcription factor that binds and activates a "germline/cleavage-stage embryo" gene program normally restricted to early embryogenesis/zygotic genome activation (e.g., *ZSCAN4*, *PRAMEF1*, *RFPL2*, *TRIM43*, *MBD3L2*, *KHDC1*), plus retroelements (endogenous retroviruses/LINE elements) and innate-immune mediators ([Geng 2012, PMID cited in Developmental Cell paper](https://www.cell.com/developmental-cell/fulltext/S1534-5807(11)00523-5)).
5. **Cellular toxicity:** Because the germline is immune-privileged, aberrant somatic expression of germline-restricted proteins triggers **innate immune/dsRNA sensing pathways** and **MYC-mRNA-stabilization-driven apoptosis** ([PMID: PLOS Genetics, PMC5362247](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5362247/)); DUX4 also increases **reactive oxygen species (ROS)** and confers susceptibility to oxidative-stress-induced cell death, rescuable by DUX4 knockdown or antioxidants.
6. **Muscle-specific consequences:** DUX4 globally represses **PAX7 target genes**, impairing satellite-cell/myogenic regenerative programs ([Banerji 2017, PMC5735185](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5735185/)); combined with atrophy/protein-degradation gene induction and impaired regeneration, this drives progressive myofiber loss, replacement by fat/fibrosis, and clinical weakness following the characteristic descending facioscapulohumeral distribution.
7. **Downstream tissue effects:** Chronic muscle degeneration → weakness, scapular winging, contractures; extramuscular DUX4-related or vascular effects → retinal telangiectasia/Coats-like vasculopathy and sensorineural hearing loss (mechanism less well resolved than muscle pathway, possibly reflecting low-level DUX4 expression or vascular developmental sensitivity in cochlea/retina).

**Cell types/processes involved:**
- Skeletal myonuclei (mosaic/sporadic DUX4 expression — only a small fraction of nuclei per myofiber express DUX4 at any time, a hallmark "bursting" expression pattern (CL:0000188 skeletal muscle fiber, CL:0000059/myonuclei more specifically muscle satellite/myogenic lineage: CL:0000515 or CL:0008019 skeletal muscle satellite stem cell for PAX7-related regenerative deficit).
- Innate immune signaling (dsRNA sensors, e.g., PKR/interferon pathway) — GO:0060337 (type I interferon signaling), GO:0006915 (apoptotic process).
- Retinal vascular endothelium (Coats-like vasculopathy) and cochlear hair cells/stria vascularis (sensorineural hearing loss) — mechanistically less characterized but plausibly linked to low DUX4 expression in these tissues during development.

**Protein dysfunction:** DUX4 itself functions as a **gain-of-function transcriptional activator** (not a misfolding/loss-of-function protein); SMCHD1 loss is a **loss-of-function chromatin-structural defect** (SMCHD1 normally compacts D4Z4 chromatin via its ATPase/hinge domains).

**Molecular profiling:** Muscle transcriptomic studies (RNA-seq) in FSHD biopsies and myoblast/myotube models show the DUX4-target signature (germline genes, immune genes) as a validated disease biomarker used in clinical trials (e.g., losmapimod trials measured DUX4-driven gene expression as a pharmacodynamic biomarker, though technical variability limited its use as a primary trial endpoint).

**Advanced technologies:** Single-nucleus/single-cell approaches have shown DUX4 expression occurs in rare, transient "bursts" in a small subset of myonuclei — a key reason bulk transcriptomic DUX4 biomarkers are noisy and difficult to use clinically. CRISPR-based functional screens and engineered SMCHD1/D4Z4 mutant cell/mouse models have been used to dissect the synergy between heterochromatin disruption and DUX4 network feedforward activation ([bioRxiv/PMC10951985](https://pmc.ncbi.nlm.nih.gov/articles/PMC10951985/)).

Sources: [DUX4 activates germline genes, retroelements, immune mediators — Developmental Cell](https://www.cell.com/developmental-cell/fulltext/S1534-5807(11)00523-5) · [DUX4-induced dsRNA/MYC apoptosis, PMC5362247](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5362247/) · [PAX7 target gene repression, PMC5735185](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5735185/) · [Engineered SMCHD1/D4Z4 mutations, PMC10951985](https://pmc.ncbi.nlm.nih.gov/articles/PMC10951985/) · [DUX4 signalling review, MDPI](https://www.mdpi.com/1422-0067/21/3/729)

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: skeletal muscle (face, shoulder girdle/scapular stabilizers, upper arm, foot dorsiflexors, later abdominal/trunk and pelvic-girdle muscles).
- Secondary: eye (retina — vasculopathy/Coats disease), ear (cochlea — sensorineural hearing loss), lung (restrictive respiratory insufficiency in advanced/wheelchair-dependent disease), rarely CNS (intellectual disability/epilepsy in infantile-onset cases only).
- Body systems: musculoskeletal (primary), sensory (auditory, visual), respiratory (secondary/late), rarely neurodevelopmental.

**Tissue/cell level:**
- Skeletal muscle fibers (type-specific vulnerability not sharply established), muscle satellite cells/myogenic progenitors (CL:0008019), retinal vascular endothelium, cochlear sensory/vascular structures.

**Subcellular level:**
- Nucleus (chromatin/heterochromatin at the D4Z4 locus; GO:0000228 nuclear chromosome), site of DUX4 transcriptional activity; mitochondria (oxidative stress/ROS generation — GO:0005739).

**Localization (UBERON suggestions):**
- UBERON:0001630 (muscle organ) — specifically facial muscles (UBERON:0001336 orbicularis oculi / UBERON:0011639 orbicularis oris region), UBERON:0006611 (scapular musculature) or specific muscles (trapezius, serratus anterior, rhomboids), UBERON:0001383 (tibialis anterior/dorsiflexor compartment).
- UBERON:0000966 (retina) for Coats-like vasculopathy.
- UBERON:0001846 (cochlea) for sensorineural hearing loss.

**Lateralization:** A hallmark distinguishing clinical feature is **asymmetric weakness** — unlike most other muscular dystrophies, FSHD often shows notably asymmetric involvement between left and right sides, even within the same muscle group.

Sources: [EyeWiki — Ophthalmologic Manifestations of FSHD](https://eyewiki.org/Ophthalmologic_Manifestations_of_Facioscapulohumeral_Dystrophy) · [Medscape FSHD Clinical Presentation](https://emedicine.medscape.com/article/1176126-clinical)

---

## 8. Temporal Development

**Onset:**
- Typical: first–third decade of life; 95% show clinical signs before age 20 (childhood/adolescent-to-young-adult onset is most common presentation, though subclinical facial weakness may predate recognized symptoms).
- Infantile-onset FSHD: a distinct, more severe subset presenting as early as infancy (case reports of symptom onset by 5 months of age), strongly associated with very short D4Z4 arrays (1–3 units, EcoRI fragment 10–14 kb) ([Timely Review, PMC7589635](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7589635/)).
- Onset pattern: insidious/gradual in classic FSHD; more rapid and multisystemic in infantile-onset disease.

**Progression:**
- Disease course: chronic, slowly progressive; classic "descending" spatial pattern — face → shoulder girdle/scapular stabilizers → upper arm → trunk/foot dorsiflexors → hip girdle/proximal lower limb.
- Progression rate: quantitative muscle strength declines at an average ~1–4%/year, but highly variable between individuals and even between muscle groups in the same patient; 6-year cumulative risk of wheelchair dependence estimated at ~24% in one longitudinal cohort ([5-year natural history study, PMID:39508285](https://pubmed.ncbi.nlm.nih.gov/39508285/)).
- Disease duration: chronic, lifelong; not typically self-limited or remitting.
- Infantile FSHD: rapid decline, marked muscle wasting, more prominent extramuscular (hearing, retinal, occasionally CNS) involvement.

**Patterns:**
- No spontaneous or treatment-induced remission is described — FSHD is a monotonic, progressive (though slow and plateau-punctuated) disease.
- Critical/vulnerable periods: earlier age of onset is itself a validated marker of eventual disease severity, making early recognition clinically important for prognostication and counseling (rather than for a treatable "window").

Sources: [Longitudinal childhood-onset FSHD 5-year study, PMC11655134](https://pmc.ncbi.nlm.nih.gov/articles/PMC11655134/) · [Early onset as marker for severity, Neurology 2019](https://www.neurology.org/doi/abs/10.1212/WNL.0000000000006819) · [Early-Onset Infantile FSHD Review, PMC7589635](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7589635/)

---

## 9. Inheritance and Population

**Epidemiology:**
- Prevalence estimates vary by methodology: ~3.2–4.6 per 100,000 in several population studies; US estimate ~1 in 20,000; broader worldwide estimates of 4–10 per 100,000.
- Incidence: conservative estimate ~1 in 14,286 births; with improved genetic testing and ascertainment, some estimate a true incidence closer to 1 in 7,500 births.
- Recognized as the **third most common muscular dystrophy** overall.

**Inheritance pattern:**
- FSHD1: **autosomal dominant** (single contracted D4Z4 allele on a permissive haplotype is sufficient).
- FSHD2: **digenic** — autosomal dominant SMCHD1 (or DNMT3B/LRIF1) variant *combined with* a permissive 4qA haplotype in trans (inherited independently; both are required for disease expression) — a well-characterized digenic inheritance exemplar (OMIM #158901).
- **Penetrance:** Generally high but genotype-dependent; incomplete/age- and epigenetically-dependent penetrance in the 8–11 unit "grey zone" alleles. Overall clinical penetrance by age 30 is estimated around 95% for classic contracted alleles, but is lower and more variable for borderline-sized alleles.
- **Expressivity:** Markedly **variable expressivity**, even within the same family carrying an identical D4Z4 contraction — a defining feature of FSHD, attributed to superimposed epigenetic/stochastic DUX4-expression variability and modifier loci (e.g., SMCHD1 second hits).
- **Genetic anticipation:** Not a classic anticipation disease (unlike CTG-repeat disorders), though intergenerational contraction-size instability of D4Z4 can occur.
- **Germline and somatic mosaicism:** Both are well documented; somatic mosaicism found in ~40% of *de novo* FSHD1 families; mosaic males are typically clinically affected while mosaic females are more often unaffected carriers/parents of a nonmosaic de novo child (a notable sex-dependent asymmetry) ([van der Maarel 2000, PMID:10631134](https://pubmed.ncbi.nlm.nih.gov/10631134/)).
- **Founder effects:** Not a major feature; permissive-haplotype (4qA) frequency and specific haplotype subtypes vary by ancestry, contributing to some population-level diagnostic complexity ([*J Hum Genet* 2025](https://www.nature.com/articles/s10038-025-01401-6)).
- **Consanguinity:** Not a notable risk factor given the dominant/digenic (not recessive) inheritance.
- **Carrier frequency:** Population frequency of the permissive 4qA haplotype itself is common in the general population (a large fraction of people carry a permissive haplotype without ever having a pathogenic contraction), underscoring that haplotype alone is necessary but not sufficient.

**Population demographics:**
- No strong racial/ethnic predilection reported, though data ascertainment has historically skewed European; diversity studies are ongoing.
- Sex ratio: males more frequently and more severely affected than females at a given genotype (asymptomatic carriage more common in females) — a recognized but mechanistically unresolved sex-modifier effect.
- Age distribution: broad, spanning infantile to adult-onset; most clinically recognized cases present in childhood through young adulthood.

Sources: [Wellstone Program — FSHD Facts and Statistics](https://www.umassmed.edu/wellstone/overview/fshdfacts/) · [Medscape — FSHD Epidemiology](https://emedicine.medscape.com/article/1176126-overview) · [Diversity challenges genetics in FSHD, *J Hum Genet* 2025](https://www.nature.com/articles/s10038-025-01401-6) · [OMIM #158901](https://www.omim.org/entry/158901)

---

## 10. Diagnostics

**Clinical tests / exam:**
- Clinical diagnosis rests on the characteristic pattern of facial, scapular-stabilizer, and foot-dorsiflexor weakness with typical asymmetry.
- Creatine kinase (CK): typically normal to mildly elevated (2–5× ULN), distinguishing FSHD from dystrophinopathies where CK is markedly elevated.
- EMG: myopathic pattern (nonspecific).
- Muscle MRI: identifies pattern and degree of fatty infiltration/edema in affected muscles, increasingly used for phenotyping and clinical-trial outcome assessment (quantitative MRI fat-fraction as a biomarker).
- Muscle biopsy: nonspecific dystrophic changes; historically used before molecular testing became standard, now largely reserved for atypical presentations.

**Genetic testing (primary diagnostic modality):**
- **FSHD1:** Molecular confirmation via **Southern blot with EcoRI/EcoRI-BlnI digestion** (measuring D4Z4 repeat/EcoRI fragment size) or newer techniques — **optical genome mapping** has been validated as an accurate, higher-throughput alternative for sizing D4Z4 alleles and determining 4qA/4qB haplotype ([PMC10664978](https://pmc.ncbi.nlm.nih.gov/articles/PMC10664978/); [PMC10743191](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10743191/)).
- **Haplotype analysis:** visual genotyping / multiplex dipstick assays distinguish the permissive 4qA vs. non-permissive 4qB/10q-derived haplotypes — essential because a short array on a non-permissive haplotype is not pathogenic.
- **FSHD2:** diagnosed when a patient has classic clinical features, a normal-sized D4Z4 array on a permissive 4qA haplotype, and **D4Z4 hypomethylation** on bisulfite/methylation analysis — followed by sequencing of **SMCHD1** (first-line), then **DNMT3B**/**LRIF1** if SMCHD1-negative.
- Long-read genome sequencing and rare-variant linkage analysis have also been used for complex/ambiguous cases ([medRxiv 2023.06.05.23290975](https://www.medrxiv.org/content/10.1101/2023.06.05.23290975.full.pdf)).
- Chromosomal microarray, karyotyping, FISH, and mitochondrial DNA testing are **not** primary diagnostic tools for FSHD (the causal lesion is a repeat-array size/methylation change, not aneuploidy or a point variant detectable by standard panels).

**Clinical diagnostic criteria:** No formal DSM/consensus scoring system analogous to other diseases; diagnosis is established per GeneReviews criteria combining clinical phenotype + molecular confirmation (repeat size + haplotype for FSHD1; methylation + SMCHD1/DNMT3B/LRIF1 sequencing for FSHD2). An AAN practice guideline exists for evaluation, diagnosis, and management ([AAN Guideline](https://www.aan.com/Guidelines/home/GuidelineDetail/701)).

**Differential diagnosis:** Limb-girdle muscular dystrophies, myotonic dystrophy, congenital myopathies, mitochondrial myopathies, polymyositis/inflammatory myopathy (facial-sparing usually distinguishes these), and other scapuloperoneal syndromes.

**Screening:** No population-based newborn screening program exists for FSHD (unlike some other genetic muscular dystrophies); genetic counseling and cascade testing of at-risk relatives is standard once a proband is confirmed, given autosomal dominant/digenic inheritance and variable/incomplete penetrance in grey-zone alleles.

Sources: [Optical genome mapping validation, PMC10664978](https://pmc.ncbi.nlm.nih.gov/articles/PMC10664978/) · [Molecular diagnosis review — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S096089662600057X) · [GeneReviews FSHD](https://www.ncbi.nlm.nih.gov/books/n/gene/fsh/) · [AAN FSHD Guideline](https://www.aan.com/Guidelines/home/GuidelineDetail/701)

---

## 11. Outcome/Prognosis

**Survival/mortality:** Life expectancy is generally **not shortened** in classic FSHD; it is considered a disease of morbidity rather than mortality, distinguishing it from many other muscular dystrophies (e.g., Duchenne). Infantile-onset/very-severe cases with major respiratory or CNS complications may carry somewhat worse prognoses, but disease-specific mortality data are limited.

**Morbidity/function:**
- Up to ~20–24% of patients become wheelchair-dependent over the disease course (6-year cumulative risk ~24% in one cohort).
- Progressive weakness affects mobility, upper-limb function (especially overhead reaching due to scapular winging), facial expression/speech, and — in a minority — respiratory function in advanced disease.
- Chronic pain and fatigue are prominent, underrecognized contributors to reduced quality of life, frequently reported in patient registry studies.

**Disease course/complications:** Retinal Coats-disease-related vision loss (rare but serious, more common in early-onset/severe genotypes), sensorineural hearing loss, contractures, and (in advanced disease) restrictive respiratory insufficiency requiring monitoring/ventilatory support.

**Prognostic factors:** D4Z4 repeat array size is the strongest genotype-phenotype correlate — shorter arrays (fewer repeat units) predict earlier onset and more severe, faster-progressing, more extramuscularly-involved disease; age of onset itself is an independent severity marker (earlier onset correlates with worse ultimate outcome). SMCHD1 modifier status in FSHD1 patients further worsens prognosis.

**Prognostic biomarkers:** DUX4-driven target-gene expression signatures and muscle MRI fat-fraction/STIR-hyperintensity have been explored as biomarkers of disease activity and progression risk, used in recent clinical trials (though with technical reproducibility challenges).

Sources: [5-year natural history cohort, PMID:39508285](https://pubmed.ncbi.nlm.nih.gov/39508285/) · [Italian National Registry 5-year follow-up, PMC7815626](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7815626/) · [Early onset as severity marker, Neurology 2019](https://www.neurology.org/doi/abs/10.1212/WNL.0000000000006819)

---

## 12. Treatment

**Current standard of care is supportive** — there is **no FDA-approved disease-modifying therapy** for FSHD as of mid-2026.

**Pharmacotherapy:**
- No approved DUX4-targeted or disease-modifying drug. Symptomatic management includes analgesics for chronic pain and standard supportive medications; no established pharmacogenomic guidance specific to FSHD.
- **Losmapimod** (p38α/β MAPK inhibitor; indirectly reduces DUX4 program activation without impairing myogenesis) — showed encouraging Phase 2b (ReDUX4) results (slowed structural/functional disease progression at 48 weeks), but the confirmatory **Phase 3 REACH trial (NCT04003974)** reported topline results on **Sept 12, 2024** that **did not meet its primary endpoint** (Reachable Workspace change) or achieve nominally significant secondary endpoints; Fulcrum Therapeutics subsequently suspended the losmapimod FSHD program ([Fulcrum press release, Sept 2024](https://www.globenewswire.com/news-release/2024/09/12/2945039/0/en/Fulcrum-Therapeutics-Announces-Topline-Results-from-Phase-3-REACH-Clinical-Trial-of-Losmapimod-in-Facioscapulohumeral-Muscular-Dystrophy-FSHD.html); [NeurologyLive coverage](https://www.neurologylive.com/view/losmapimod-shows-potential-fshd-despite-not-meeting-primary-end-point)).

**Advanced/RNA-based therapeutics in development (not yet approved):**
- **Direct DUX4 mRNA knockdown — antisense oligonucleotides (ASOs)/gapmers:** preclinical work (2′MOE and LNA-chemistry gapmers) shows effective DUX4 knockdown and improved muscle function (grip strength) in mouse models via subcutaneous dosing ([PMC12795667](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12795667/); [systemic ASO delivery, PMC8526479](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8526479/)). Companies pursuing direct DUX4-targeting approaches include **Dyne Therapeutics, Avidity Biosciences, Arrowhead Pharmaceuticals, and miRecule**.
- **AOC 1020 (Avidity Biosciences)** — an antibody-oligonucleotide conjugate targeting DUX4, evaluated in the Phase 1/2 **FORTITUDE trial (NCT05747924)**, with a Phase 3 trial in the pipeline as of 2025–2026 as a step toward potential FDA approval.
- **Follistatin/myostatin-pathway (muscle-growth-promoting) approach — ACE-083 (Acceleron):** a locally-injected follistatin-based agent that increased target muscle volume in a Phase 2 trial but **did not translate to improved function**, leading to discontinuation of that program for FSHD ([Statland et al. 2022, *Muscle & Nerve*, PMID via search](https://onlinelibrary.wiley.com/doi/10.1002/mus.27558)).
- **Gene therapy/CRISPR-based epigenetic silencing** approaches (targeting DUX4 locus re-repression, e.g., via engineered zinc-finger or CRISPR-dCas9 epigenetic editors) and further AAV-delivered shRNA approaches are in earlier preclinical stages; a 2025 mouse study found **AAV-shDUX4 provided only short-term benefit with waning long-term efficacy** due to muscle regeneration diluting AAV genomes ([Molecular Therapy Methods & Clinical Development 2025](https://www.cell.com/molecular-therapy-family/advances/fulltext/S2329-0501(25)00129-9)).

**Surgical/interventional:**
- **Scapular fixation/fusion surgery** — stabilizes the winging scapula to the rib cage (bone graft fusion or screw/wire fixation), improving functional leverage for arm use in appropriately selected patients, performed by surgeons experienced with FSHD; decreases scapular rotation range but often nets functional benefit for overhead/reaching tasks (NCIT:C15329 Surgical Procedure / more specific orthopedic procedure term).

**Supportive/rehabilitative:**
- Physical and occupational therapy focused on maintaining function and preventing contractures/disuse atrophy (rather than restorative rehab); orthoses (e.g., ankle-foot orthoses for foot drop); moderate, individualized aerobic/strength exercise programs under specialist supervision (research ongoing on optimal, safe exercise protocols); respiratory therapy/monitoring for advanced disease; low-vision/audiology support for extramuscular retinal/hearing complications; ophthalmologic screening and, when needed, laser photocoagulation or anti-VEGF therapy (e.g., ranibizumab) for Coats-disease-related retinal vasculopathy.

**Experimental/clinical trials:** Numerous active trials registered at ClinicalTrials.gov beyond those above, including natural history/outcome-measure studies (e.g., NCT04369209 registered cohort) and shoulder-instability mechanism studies (NCT05239520).

**Treatment strategy:** Multidisciplinary care (neurology, physiatry/PT-OT, orthopedic surgery, ophthalmology, audiology, pulmonology, genetic counseling) is the current mainstay; no genotype-guided personalized pharmacotherapy yet exists, though D4Z4 size/SMCHD1 status informs prognosis and eligibility for genotype-restricted (e.g., FSHD1-only) trials such as REACH.

Suggested NCIT terms: NCIT:C15986 (Pharmacotherapy, for losmapimod/investigational agents) with `therapeutic_modality: SMALL_MOLECULE`; NCIT:C15238 (Gene Therapy) / `ANTISENSE_OLIGONUCLEOTIDE` modality for DUX4-targeted ASOs/AOC 1020; NCIT:C15329 or C16186 (Orthopedic Surgical Procedure) for scapular fixation; NCIT:C15302 (Physical Therapy).

Sources: [Fulcrum REACH topline results](https://www.globenewswire.com/news-release/2024/09/12/2945039/0/en/Fulcrum-Therapeutics-Announces-Topline-Results-from-Phase-3-REACH-Clinical-Trial-of-Losmapimod-in-Facioscapulohumeral-Muscular-Dystrophy-FSHD.html) · [ACE-083 Phase 2, Statland 2022](https://onlinelibrary.wiley.com/doi/10.1002/mus.27558) · [AOC 1020 FORTITUDE trial, NCT05747924](https://clinicaltrials.gov/study/NCT05747924) · [Current landscape management review, PMC12287641](https://pmc.ncbi.nlm.nih.gov/articles/PMC12287641/) · [ASO gapmer DUX4 knockdown, PMC12795667](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12795667/)

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense (no modifiable environmental cause to eliminate); the closest analog is **reproductive/genetic prevention** via genetic counseling and prenatal or preimplantation genetic diagnosis (PGD) for known-carrier families, given autosomal dominant/digenic inheritance.

**Secondary prevention (early detection):** Cascade genetic testing of at-risk relatives once a proband is molecularly confirmed; given variable/incomplete penetrance especially for grey-zone (8–11 unit) alleles, early molecular diagnosis allows anticipatory monitoring (audiology, ophthalmology, pulmonary function) before symptom onset, particularly relevant for early-onset/short-repeat genotypes at higher risk of extramuscular complications.

**Tertiary prevention:** Ophthalmologic screening and monitoring to catch and treat retinal vasculopathy before progression to Coats-disease-related vision loss; audiologic monitoring for hearing loss; proactive physical therapy/orthotic management and periodic pulmonary function assessment to reduce complications of progressive weakness (contractures, falls, respiratory insufficiency) in more advanced disease.

**Immunization:** Not disease-specific (standard care includes ensuring routine immunizations, including respiratory pathogens, are up to date in patients with any respiratory muscle compromise, but this is generic supportive care, not FSHD-specific prophylaxis).

**Genetic counseling:** Central to FSHD family management — addressing the autosomal dominant (FSHD1) or digenic (FSHD2) inheritance pattern, variable expressivity, incomplete penetrance of grey-zone alleles, and both somatic and germline mosaicism (which affects recurrence-risk estimates for apparently *de novo* cases — a parent with somatic/germline mosaicism can have a higher-than-expected recurrence risk for future children despite testing negative on peripheral blood).

**Public health/behavioral:** No population-level public-health intervention exists (rare monogenic disease); individualized behavioral guidance centers on maintaining physical activity/muscle conditioning within safe limits and fall-prevention strategies as weakness progresses.

Sources: [GeneReviews FSHD — Genetic Counseling section](https://www.ncbi.nlm.nih.gov/books/n/gene/fsh/) · [Germinal mosaicism in FSHD, Upadhyaya 1995](https://onlinelibrary.wiley.com/doi/10.1002/mus.880181310)

---

## 14. Other Species / Natural Disease

FSHD is a **human-specific molecular disease** in a strict sense: the pathogenic DUX4 retrogene and its D4Z4 macrosatellite array, along with the specific 4qA permissive haplotype/polyadenylation signal architecture, are primate/human-specific genomic features. There is **no well-characterized naturally occurring FSHD-equivalent disease in veterinary species** (dogs, cats, livestock) analogous to, for example, canine dystrophin-deficient muscular dystrophy models for DMD. DUX-family genes exist across mammals (e.g., mouse *Dux*, expressed during zygotic genome activation), providing evolutionary/developmental-biology context for DUX4's normal role, but these orthologs are not linked to a spontaneous disease phenotype in the source species. This section is therefore largely **not applicable**, beyond noting the evolutionary conservation of the DUX-family developmental gene-activation role (relevant to model organism engineering, below) rather than any natural veterinary disease counterpart.

Suggested taxonomy note: NCBITaxon:9606 (Homo sapiens) is the sole natural host species for the clinical disease.

---

## 15. Model Organisms

Because FSHD's pathogenic mechanism (DUX4 gain-of-function via loss of D4Z4 repeat-mediated silencing) has no natural non-human counterpart, **all animal models are engineered/induced**, generally via transgenic or conditional expression of human DUX4:

- **Mouse models (multiple engineered lines):**
  - **FLExDUX4** — a widely used **Cre-inducible, floxed DUX4-full-length conditional transgenic mouse**, allowing tunable, tissue- and time-restricted DUX4 expression to titrate pathology severity and avoid the developmental lethality of constitutive DUX4 expression ([PMC5802938](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5802938/)).
  - **iDUX4pA** and related "TIC-DUX4" inducible models — considered to come closest to recapitulating both clinical (muscle weakness, histopathology) and molecular (DUX4 target-gene activation) features of human FSHD; used as the basis for testing follistatin gene therapy (AAV-follistatin improved functional outcomes in TIC-DUX4 mice — [JCI Insight](https://insight.jci.org/articles/view/123538)) and AAV-shDUX4 knockdown approaches ([Molecular Therapy Methods & Clinical Development 2025](https://www.cell.com/molecular-therapy-family/advances/fulltext/S2329-0501(25)00129-9)).
  - Newer transgenic mouse models specifically for investigating human DUX4 expression continue to be developed (2025 bioRxiv report).
  - Genetic models available include conditional/inducible transgenics (Cre-lox systems); classic knockout models are not applicable since FSHD is a gain-of-function disease, not a loss-of-function one for DUX4 itself (though SMCHD1 knockout/knock-in mouse models are used to study the FSHD2 chromatin-modifier mechanism).

- **Zebrafish model:** A **transgenic zebrafish DUX4-misexpression model** demonstrated that an induced early-developmental burst of DUX4 produces FSHD-like phenotypes emerging later in adulthood, even after DUX4 is no longer detectable — supporting a **developmental-origin hypothesis** for at least part of FSHD pathogenesis, distinct from purely adult muscle-toxicity mechanisms ([Hum Mol Genet 2018, PMID:30307508](https://pubmed.ncbi.nlm.nih.gov/30307508/)).

- **Cellular/in vitro models:** Patient-derived myoblast/myotube cultures (including immortalized FSHD1/FSHD2 patient lines) are the mainstay for mechanistic and drug-screening studies (e.g., losmapimod's selective inhibition of the DUX4 program without impairing myogenesis was demonstrated in FSHD myotube cultures). iPSC-derived myogenic models are increasingly used for genotype-specific (grey-zone allele, SMCHD1-variant) disease modeling.

**Model characteristics/limitations:** Because DUX4 expression is mosaic, transient/"bursting," and cytotoxic even at low levels, constitutive whole-body DUX4 mouse models are frequently embryonic lethal or severely runted — necessitating the conditional/inducible systems above to titrate expression to sub-lethal, disease-relevant levels. No current animal model fully recapitulates the human D4Z4 repeat-contraction genetics (mice lack a directly homologous D4Z4/DUX4 locus with the human-specific permissive-haplotype architecture), so all models rely on **transgenic human DUX4 insertion** rather than an endogenous orthologous mutation — an important translational caveat (a candidate `HUMAN_MODEL_MISMATCH` consideration for any dismech entry: whether mouse/zebrafish DUX4-overexpression phenotypes faithfully model the graded, chronic, mosaic-expression human disease process).

**Applications:** These models are used to study DUX4-driven transcriptional/apoptotic pathways, test DUX4-suppression therapeutics (ASOs, small molecules, gene therapy), and assess the developmental-origin hypothesis of FSHD pathogenesis.

Sources: [FLExDUX4 mouse model, PMC5802938](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5802938/) · [AAV-follistatin in TIC-DUX4 mice, JCI Insight](https://insight.jci.org/articles/view/123538) · [AAV-shDUX4 mouse model 2025](https://www.cell.com/molecular-therapy-family/advances/fulltext/S2329-0501(25)00129-9) · [Transgenic zebrafish DUX4 model, PMID:30307508](https://pubmed.ncbi.nlm.nih.gov/30307508/) · [Transgenic mouse models 2025, bioRxiv](https://www.biorxiv.org/content/10.1101/2025.08.22.671867v1.full.pdf)

---

## Summary of Key Evidence Gaps / Notes for Curation

- **Not applicable / no data:** environmental/infectious causal factors, veterinary/natural-disease counterparts, cardiac involvement is debated/minor (unlike other dystrophies), no approved disease-modifying pharmacotherapy or gene therapy as of this writing (mid-2026).
- **High-confidence, well-cited mechanistic core:** D4Z4 contraction/SMCHD1-DNMT3B-LRIF1 chromatin derepression → stabilized DUX4-fl transcription → germline/immune gene program activation → apoptosis/oxidative stress + PAX7-regenerative-program repression → progressive myofiber loss — suitable as the spine of a `pathophysiology` causal chain, with `conforms_to` candidacy against no existing dismech module (a novel DUX4-chromatin-derepression mechanism, potentially a future module given its shared logic with other repeat/epigenetic-derepression diseases).
- **Active clinical trial landscape (rapidly moving target):** losmapimod program discontinued (Sept 2024, Phase 3 miss); ASO/AOC-based DUX4-knockdown programs (AOC 1020/Avidity FORTITUDE, plus Dyne/Arrowhead/miRecule preclinical-to-early-clinical programs) are the most active current therapeutic frontier — recommend periodic re-verification of trial status (NCT05747924 and successors) given the pace of change.
- **Digenic inheritance model:** FSHD2 is a strong, well-documented exemplar for the dismech digenic/oligogenic inheritance pattern (HP:0010984), directly relevant to the `Digenic_and_Oligogenic_Disorders` grouping referenced in project conventions.