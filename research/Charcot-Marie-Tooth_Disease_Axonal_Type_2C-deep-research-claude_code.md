---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T23:16:39.845807'
end_time: '2026-08-27T23:21:20.584794'
duration_seconds: 280.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Charcot-Marie-Tooth Disease Axonal Type 2C
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
  web_search_requests: 16
  num_turns: 19
  total_cost_usd: 1.1450722
  session_id: 2df13fb4-9115-50fa-aa7c-75f1d91c874a
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 32
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  quotes_not_checkable: 1
  relevance_assessed: 13
  on_topic: 6
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth Disease Axonal Type 2C
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease Axonal Type 2C** covering all of the
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

I'll research this now using web search tools to gather current, authoritative information on CMT2C.

# Charcot-Marie-Tooth Disease Axonal Type 2C (CMT2C) — Comprehensive Research Report

## 1. Disease Information

**Overview:** Charcot-Marie-Tooth disease axonal type 2C (CMT2C), also designated Hereditary Motor and Sensory Neuropathy type IIC (HMSN2C), is an autosomal dominant, motor-predominant, non-length-dependent peripheral neuropathy or motor neuronopathy caused by heterozygous gain-of-function mutations in *TRPV4*. It is one of three clinically recognized autosomal dominant "TRPV4 neuromuscular disorders" — alongside scapuloperoneal spinal muscular atrophy (SPSMA) and congenital distal spinal muscular atrophy (CDSMA/CSMA) — which together with a family of TRPV4 skeletal dysplasias constitute the broader "TRPV4-pathy" spectrum ([GeneReviews: Autosomal Dominant TRPV4-Related Disorders](https://www.ncbi.nlm.nih.gov/books/NBK201366/); [Nature Genetics 2010, ng.512](https://www.nature.com/articles/ng.512); [J Hum Genet 2010, jhg201037](https://www.nature.com/articles/jhg201037)).

**Key identifiers:**
- **OMIM:** #606071 — Hereditary Motor and Sensory Neuropathy, Type IIC (HMSN2C) ([OMIM 606071](https://omim.org/entry/606071)); the *TRPV4* gene entry is OMIM *605427 ([OMIM 605427](https://www.omim.org/entry/605427))
- **Orphanet:** ORPHA:99937 — "Autosomal dominant Charcot-Marie-Tooth disease type 2C" ([Orphanet 99937](https://www.orpha.net/en/disease/detail/99937))
- **MONDO/MedGen:** MedGen concept C1853710 ([MedGen 342947](https://www.ncbi.nlm.nih.gov/medgen/342947); [GARD](https://rarediseases.info.nih.gov/diseases/1250/charcot-marie-tooth-disease-axonal-type-2c))
- **Gene:** *TRPV4* (transient receptor potential cation channel subfamily V member 4), chromosome 12q24.11
- **Allelic disorders (same gene, different phenotype "bin"):** Scapuloperoneal spinal muscular atrophy (SPSMA, OMIM 181405), congenital distal spinal muscular atrophy (CDSMA/HMND8, OMIM 600175), and a family of TRPV4 skeletal dysplasias (metatropic dysplasia, spondylometaphyseal dysplasia Kozlowski type, brachyolmia, parastremmatic dysplasia)

**Synonyms:** HMSN2C; CMT2C; hereditary motor and sensory neuropathy type 2C; TRPV4-related axonal neuropathy; CMT2C with vocal cord paresis.

**Evidence basis:** This is an aggregated disease-level entity, not derived from a single EHR cohort. Curation rests on published case series/family pedigrees, a small number of dedicated CMT2 patient cohorts (USA, European, Australian), the OMIM/Orphanet/GeneReviews synthetic entries, and mechanistic cell/animal-model studies — not large-scale registry or claims data.

---

## 2. Etiology

**Primary cause:** CMT2C is caused entirely by heterozygous, dominantly acting, **gain-of-ion-channel-function missense variants in *TRPV4*** ([Deng et al., Nat Genet 2010;42:165–169](https://www.nature.com/articles/ng.509); [Landouré et al., Nat Genet 2010, ng.512](https://www.nature.com/articles/ng.512)). It is a monogenic Mendelian disorder — there is no evidence for polygenic, infectious, or purely environmental causation of the core neuropathy phenotype.

**Genetic risk factors:**
- Causal variants cluster on "the highly positively charged convex surface of the ankyrin repeat domain," targeting strictly conserved arginine residues in three consecutive finger loops of the protein ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/)).
- Well-validated recurrent pathogenic variants: **p.Arg186Gln, p.Arg232Cys, p.Arg269Cys, p.Arg269His, p.Arg315Trp, p.Arg316Cys, p.Arg316His** ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/)). The founding CMT2C family carried **c.806G>A (p.Arg269His)** ([Deng et al. 2010](https://www.nature.com/articles/ng.509)); another kindred with the founding phenotype carried the paralogous **c.805C>T/c.806G>A → R269C/R269H** substitutions at the same residue ([review, PMC10311707](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10311707/)).
- **Modifier/severity determinants:** the same residue can produce markedly different severity; "the degree of baseline calcium elevation correlates with development of mixed [neuropathy + skeletal] phenotypes and sensitivity to pharmacologic channel inhibition" ([Nishida/Zhu et al., PMC8935273](https://pmc.ncbi.nlm.nih.gov/articles/PMC8935273/)). No independent trans-acting modifier gene has been established for the neuromuscular phenotype.
- Reduced penetrance and highly variable expressivity are intrinsic features — the specific subtype (CMT2C vs. SPSMA vs. CDSMA), age of onset, and severity "cannot be accurately predicted" from genotype alone ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/)).

**Environmental/lifestyle risk factors:** None specific to disease *causation* are documented (this is a fully penetrant-genotype, non-environmentally-triggered channelopathy). However, several environmental/physiologic exposures **exacerbate manifestations** in carriers:
- Obesity worsens ambulation ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/))
- Upper respiratory tract infections can precipitate acute worsening of vocal-fold/airway obstruction via laryngeal edema ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/))
- Neurotoxic medications (standard CMT avoid-list) can accelerate neuropathy
- Pregnancy: ~50% of women with CMT report increased weakness during pregnancy, typically resolving postpartum; CMT pregnancies show higher rates of placenta previa, abnormal fetal presentation, and preterm delivery, though overall neonatal outcomes are comparable to background populations ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/))

**Protective factors:** No genetic or environmental protective factors are described in the literature for TRPV4 neuromuscular disease; this contrasts with skeletal-dysplasia TRPV4 alleles, where no protective variants are documented either.

**Gene-environment interaction:** Not a recognized feature of this disorder; the driving mechanism is cell-autonomous/vascular channel gain-of-function rather than an environmentally modulated genetic susceptibility.

---

## 3. Phenotypes

CMT2C exists on a phenotypic continuum with SPSMA and CDSMA. Core features (with suggested HPO terms):

| Phenotype | Type | Frequency/Notes | Suggested HPO |
|---|---|---|---|
| Distal limb weakness/atrophy, pes cavus, foot drop | Sign | Core feature; onset early childhood–age 25 typically, but ranges birth to 8th decade | HP:0003693 (Distal amyotrophy), HP:0001761 (Pes cavus), HP:0001771 (Foot drop... use HP:0001269 foot drop analog) |
| Non-length-dependent, proximal + asymmetric weakness | Sign | Shoulder abduction weakness, scapular winging, asymmetric knee extension/hip flexion weakness — distinguishes CMT2C from typical length-dependent CMT | HP:0003324 (Generalized muscle weakness), HP:0003691 (Proximal muscle weakness), HP:0003691 |
| Vocal fold (cord) paresis/paralysis | Sign | "Hallmark" feature across all TRPV4 neuromuscular subtypes; bilateral or asymmetric, often worse on left; hoarse voice/inspiratory stridor | HP:0001611 (Hoarse voice), HP:0012046 (Vocal cord paralysis), HP:0010307 (Vocal cord paresis) |
| Diaphragm weakness / respiratory insufficiency | Sign | Orthopnea, decreased inspiratory/expiratory pressures, sleep apnea incl. central | HP:0009088 (Diaphragmatic paralysis/weakness), HP:0002093 (Respiratory insufficiency), HP:0002104 (Apnea) |
| Sensorineural hearing loss | Sign | Bilateral, progressive, mild–moderate, childhood–adult onset (locus overlaps DFNA25) | HP:0000407 (Sensorineural hearing impairment) |
| Sensory loss (vibration > pain) | Symptom | Present in a subset; predominantly motor disease overall | HP:0003390 (Loss of proprioception... use HP:0003701 or vibratory), HP:0007099 |
| Kyphoscoliosis / joint contractures / hip dysplasia | Sign | Ankle, knee, hip contractures common; tethered spinal cord in 7.5% of a 40-patient cohort | HP:0002751 (Kyphoscoliosis), HP:0034332 (Joint contracture), HP:0001385 (Hip dysplasia), HP:0002230 (Tethered cord) |
| Short stature | Sign | Present in a subset, overlaps skeletal-dysplasia end of spectrum | HP:0004322 |
| Bladder dysfunction | Sign | Incontinence, urinary frequency | HP:0000010 (Urinary bladder sphincter dysfunction) |
| Skin changes | Sign | Scaliness, dryness, itching, fissures (reported subset) | HP:0000962 (Dry skin) |

**Onset:** Highly variable — "usually between early childhood and age 25 years," but documented range is birth to after the 8th decade; some carriers have subtle findings that escape clinical recognition entirely (reduced penetrance) ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/)). Course is chronic/progressive in most, but severity and rate vary widely even within one family carrying the identical variant.

**Severity/progression:** "There is a wide range of phenotypic severity; in the mildest of the autosomal dominant TRPV4-related disorders life span is normal, whereas in the most severe it is shortened" ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/)). Suggestive "red flag" combination for clinicians: vocal cord paralysis + scapular weakness/wasting + skeletal dysplasia + hearing loss in a CMT2 patient ([Neurology 2015, Neurology 2014 WNL.0000000000000450](https://www.neurology.org/doi/10.1212/WNL.0000000000000450); [NeuroMolecular Medicine 2019](https://link.springer.com/article/10.1007/s12017-019-08564-4)).

**Quality of life:** No CMT2C-specific EQ-5D/SF-36 data were identified; general CMT registry literature documents mobility impairment, orthotic/AFO dependence, and — distinctively for this subtype — impact from laryngeal dysfunction (dysphonia, aspiration risk, airway obstruction) and respiratory limitation, which are less prominent in typical demyelinating/axonal CMT.

---

## 4. Genetic/Molecular Information

**Causal gene:** *TRPV4* (HGNC:17728, chr12q24.11); OMIM gene entry *605427.

**Variant classification/type:** Exclusively missense (with rare splice-site variants reported in ClinVar, e.g., c.2209-5C>T); no whole-gene deletions/duplications have been reported for the autosomal dominant neuromuscular phenotype, and sequence analysis alone identifies essentially 100% of currently known pathogenic variants ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/)). ClinVar lists numerous variant-specific submissions explicitly annotated "AND Charcot-Marie-Tooth disease axonal type 2C," e.g. p.Arg774Cys, p.Arg464Cys, p.Arg151Trp, p.Arg315Trp ([ClinVar RCV000645535](https://www.ncbi.nlm.nih.gov/clinvar/RCV000645535/); [RCV000645552](https://www.ncbi.nlm.nih.gov/clinvar/RCV000645552/); [RCV000005291](https://www.ncbi.nlm.nih.gov/clinvar/RCV000005291/)).

**Functional consequence:** Uniformly **gain of channel function** (not loss of function) — increased constitutive and agonist-evoked Ca²⁺ influx through the mutant channel, producing "cytotoxic hypercalcemia" ([Neurology 2011, WNL.0b013e31820f2de3](https://www.neurology.org/doi/10.1212/WNL.0b013e31820f2de3); PMID 21288981). Original functional work: HEK293 cells transfected with mutant TRPV4 (R269H) showed normal plasma-membrane trafficking but markedly increased constitutive and stimulus-evoked channel currents plus cellular toxicity ([Deng et al. 2010](https://www.nature.com/articles/ng.509); [Landouré et al. 2010](https://www.nature.com/articles/ng.512)).

**Allele frequency:** These are rare, largely private, dominant disease-causing missense variants; population allele frequency in gnomAD is expected to be near-absent for pathogenic alleles (no specific carrier-frequency estimate was located in this search — flag as data gap).

**Origin:** Both inherited (familial, autosomal dominant transmission with 50% recurrence risk) and de novo cases occur; severe skeletal-dysplasia-end phenotypes are typically de novo in unaffected parents, while milder/classic neuromuscular phenotypes are more often inherited ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/)). No somatic/mosaic TRPV4 CMT2C cases were identified in this search.

**Modifier genes:** None specific and validated; phenotypic variability appears largely explained by variant position/severity of channel gain-of-function rather than a distinct modifier locus (see §2).

**Structural/mechanistic basis:** Cryo-EM structures of TRPV4 in complex with **RhoA GTPase** show that many disease residues lie at the TRPV4–RhoA interface; disrupting this interface (by mutating either partner) increases TRPV4 channel activity, drives cytoskeletal remodeling, and impairs neurite extension ([Deng lab/PMC10290081](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10290081/); [PMID 33664271](https://pubmed.ncbi.nlm.nih.gov/33664271/)). A second regulatory mechanism involves **ubiquitination** of intrinsically disordered N- and C-terminal cytosolic regions of TRPV4: neuropathy-causing gain-of-function mutations reduce channel ubiquitination in cellular and *Drosophila* models, and experimentally increasing mutant-channel ubiquitination partially suppresses channel overactivity ([Aisenberg et al., J Biol Chem 2022, PMC9010760](https://pmc.ncbi.nlm.nih.gov/articles/PMC9010760/)).

**Epigenetics/chromosomal abnormalities:** Not described as relevant to this single-gene channelopathy; no epigenetic or large chromosomal-rearrangement mechanism has been reported.

---

## 5. Environmental Information

CMT2C is not primarily environmentally caused, but relevant environmental/exposure modulators of morbidity include:
- **Upper respiratory infection** — precipitates vocal-fold edema and can acutely worsen airway obstruction in patients with baseline vocal-fold paresis ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/))
- **Neurotoxic drug exposure** — standard CMT avoidance list (vincristine and other agents) can worsen underlying axonal neuropathy
- **Obesity** — a modifiable factor worsening ambulatory function
- No infectious agent is causally implicated in CMT2C itself (distinct from acquired/inflammatory neuropathies).

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular initiating event:** Heterozygous missense variant in the ankyrin-repeat domain (or C-terminal region) of TRPV4 disrupts autoinhibitory conformational constraints, including loss of normal TRPV4–RhoA interaction and reduced channel ubiquitination/turnover ([PMC10290081](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10290081/); [PMC9010760](https://pmc.ncbi.nlm.nih.gov/articles/PMC9010760/)).
2. **Molecular consequence:** Constitutive and stimulus-evoked **gain of Ca²⁺-channel function** — excess Ca²⁺ influx through the nonselective cation channel ([Nat Genet 2010](https://www.nature.com/articles/ng.509); [Neurology 2011 PMID 21288981](https://pubmed.ncbi.nlm.nih.gov/21288981/)).
3. **Cellular consequence:** "Cytotoxic hypercalcemia" — sustained intracellular Ca²⁺ overload causes cytoskeletal/RhoA-pathway dysregulation, impaired neurite extension, and cell process retraction in neuronal/glial cell models ([PMID 33664271](https://pubmed.ncbi.nlm.nih.gov/33664271/)).
4. **Vascular/barrier consequence (new mechanistic insight, 2024):** Knock-in mouse models (R269C, R232C) show that the dominant pathogenic driver is TRPV4 gain-of-function specifically **in vascular endothelial cells**, causing focal breakdown of the blood–spinal cord barrier (BSCB); genetic deletion of mutant *Trpv4* from endothelial cells (but not neurons, glia, or muscle) rescues the motor phenotype, indicating a **non-cell-autonomous, endothelial-driven mechanism of motor neuron degeneration** ([Chen et al., PMC11316273, PMID 38776392](https://pmc.ncbi.nlm.nih.gov/articles/PMC11316273/)).
5. **Tissue/organism consequence:** Regional anterior horn cell/motor neuron loss, motor axon degeneration → progressive limb, laryngeal, diaphragmatic, and (in overlap cases) skeletal phenotypes.

**Molecular pathways:** TRPV4 calcium signaling; RhoA GTPase/cytoskeletal remodeling pathway; ubiquitin-proteasome-linked channel turnover regulation.

**Cellular processes:** Calcium-dependent cytotoxicity; impaired neurite outgrowth; vascular endothelial barrier dysfunction; (in the skeletal-dysplasia allelic spectrum) altered chondrocyte hypertrophic differentiation — TRPV4 skeletal-dysplasia mutations "suppress the hypertrophic differentiation of human iPSC-derived chondrocytes" (biorxiv preprint referenced in search, distinguishing the skeletal branch mechanistically from the neuromuscular branch).

**Suggested ontology terms:**
- GO biological process: GO:0070588 (calcium ion transmembrane transport), GO:0007584 (response to nutrient — n/a), better: GO:0006816 (calcium ion transport), GO:0007015 (actin filament organization, via RhoA), GO:0007520 (myoblast fusion — n/a)
- GO molecular function: GO:0005227 (calcium-activated cation channel activity), GO:0015276 (ligand-gated ion channel activity)
- Cell types (CL): CL:0000540 (neuron)/CL:0011031 (spinal cord motor neuron), CL:0002139 (vascular associated smooth muscle... or) CL:0002139/CL:0000115 (endothelial cell), CL:0000499 (stromal cell — n/a)

**Biochemical abnormality:** Ion channel gain-of-function (not enzyme deficiency); no metabolic pathway defect is implicated.

**Immune involvement:** None established; this is not an inflammatory/autoimmune neuropathy.

**Omics:** No large-scale human transcriptomic/proteomic/metabolomic dataset specific to CMT2C patient tissue was identified in this search (data gap). Model-system transcriptomic/functional-genomics data exist chiefly in the *Drosophila* and mouse knock-in systems described above and in the endothelial-lineage-tracing study (PMC11316273).

---

## 7. Anatomical Structures Affected

**Organ/system level:**
- Peripheral nervous system: motor and (secondarily) sensory peripheral nerves; anterior horn cells (motor neuronopathy component)
- Larynx: vocal fold/recurrent laryngeal nerve-innervated musculature
- Respiratory system: diaphragm, intercostal muscles
- Auditory system: cochlea (sensorineural hearing loss)
- Musculoskeletal system: distal and (asymmetrically) proximal limb muscles; spine (kyphoscoliosis, tethered cord); joints (contractures, hip dysplasia)
- Vasculature: spinal cord microvascular endothelium (per the 2024 mouse mechanism data) — UBERON: blood-spinal cord barrier
- Urinary system: bladder (dysfunction reported)
- Integument: skin (dryness/fissuring in a subset)

**Suggested UBERON terms:** UBERON:0001017 (central nervous system) — not primary; UBERON:0002240 (spinal cord), UBERON:0002423 (anterior horn), UBERON:0001519 (larynx), UBERON:0002616 (diaphragm), UBERON:0001846 (cochlea), UBERON:0002471 (skeletal muscle organ), UBERON:0007798 (skeletal system), UBERON:0001981 (blood vessel endothelium).

**Tissue/cell level:** Lower motor neurons (anterior horn cells); axons of peripheral motor nerves; laryngeal muscles; vascular endothelial cells of the spinal cord microvasculature (mechanistically central per 2024 mouse data); cochlear hair cells/stria vascularis (candidate site for hearing loss, given TRPV4's proposed role transporting K⁺ into the endolymph at the DFNA25 locus).

**Subcellular:** Plasma membrane (TRPV4 channel localization); cytoskeleton (RhoA-regulated actin remodeling); N-/C-terminal intrinsically disordered cytosolic domains (site of regulatory ubiquitination).

**Suggested GO Cellular Component terms:** GO:0005886 (plasma membrane), GO:0015629 (actin cytoskeleton).

**Laterality:** Weakness/wasting and vocal-fold paresis are frequently **asymmetric** — a distinguishing clinical clue versus typical symmetric length-dependent CMT ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/); left side often more severely affected for vocal fold paresis).

---

## 8. Temporal Development

**Onset:** Extremely variable — "usually between early childhood and age 25 years," documented range birth to 8th decade+ ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/)). Onset pattern is generally insidious/chronic rather than acute, though congenital presentations (overlapping CDSMA) exist at the severe end of the spectrum.

**Progression:** Chronic, generally slowly progressive; disease course pattern is progressive rather than relapsing-remitting. Severity is markedly variable even within a family sharing the identical variant, consistent with variable expressivity. No formalized clinical staging system specific to CMT2C exists (unlike, e.g., cancer staging); severity is generally described qualitatively (mild/moderate/severe) and via CMT-specific functional scales (e.g., CMTNS) in the broader CMT literature.

**Duration/course:** Chronic, lifelong. Most patients have a normal lifespan; the most severely affected (especially those with significant respiratory/diaphragmatic involvement) may have reduced life expectancy from respiratory complications ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/)).

**Remission:** Not a relapsing-remitting disease; no spontaneous remission pattern is described. Pregnancy-associated worsening typically resolves postpartum (see §2).

**Critical periods:** Early recognition of laryngeal/respiratory involvement is clinically critical because airway compromise (from vocal-fold paresis plus superimposed URI-related edema) can be acutely life-threatening, making this a key intervention window distinct from the general limb-weakness natural history.

---

## 9. Inheritance and Population

**Epidemiology:** CMT2C is rare among an already-rare disease group. *TRPV4* pathogenic variants account for **~1–3.5% of CMT2/hereditary motor neuropathy (HMN)** overall ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/)). In specific published cohorts:
- 13/422 individuals (<1%) with a general CMT2 phenotype carried heterozygous *TRPV4* variants; this rose to **9–16%** among CMT2 patients selected for additional atypical features (vocal fold weakness, diaphragmatic paresis, skeletal dysplasia) ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/); [Neurology 2015, WNL.0000000000000450](https://www.neurology.org/doi/10.1212/WNL.0000000000000450))
- A USA cohort of 62 unrelated CMT2 patients (MFN2/GARS/NEFL/GDAP1-negative) found 2 *TRPV4* mutations (R316C, R269C) — **~3.2%** ([NeuroMolecular Medicine 2019](https://link.springer.com/article/10.1007/s12017-019-08564-4))
- Incidence across European/Australian axonal-neuropathy cohorts ranges **0–7%**, and data from outside Europe/Australia/USA remain largely unknown ([Neurology 2015](https://www.neurology.org/doi/10.1212/WNL.0000000000000450))
- Orphanet epidemiologic class: rare disease (prevalence class consistent with "<1/1,000,000" to "not yet documented" tier typical of CMT2 subtypes; exact Orphanet prevalence class was not directly captured in this search — recommend confirming via a direct Orphanet epidemiology table pull before finalizing).

**Inheritance:** Autosomal dominant, by definition ([OMIM 606071](https://omim.org/entry/606071)). Recurrence risk to offspring of an affected individual is 50%.

**Penetrance:** Reduced — not all variant carriers manifest symptoms, and asymptomatic/subclinically affected carriers are documented ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/); [MedGen 342947](https://www.ncbi.nlm.nih.gov/medgen/342947)).

**Expressivity:** Highly variable — same variant can produce anything from a CMT2C-limb phenotype to SPSMA to CDSMA to a mixed neuropathy/skeletal-dysplasia phenotype, even within one family ([review PMC10311707](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10311707/)).

**Genetic anticipation:** Not reported as a feature (this is a channelopathy caused by point missense variants, not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically documented in the literature reviewed here (data gap).

**Founder effects:** Not established for CMT2C specifically; the recurrent Arg-residue "hotspot" variants (e.g., R269C/H, R316C/H) likely reflect mutational hotspots at CpG-type or structurally constrained codons rather than a single founder haplotype, though this was not explicitly confirmed in the sources reviewed.

**Consanguinity:** Autosomal dominant CMT2C does not require consanguinity; however, homozygous *TRPV4* mutations have been reported causing the more severe, biallelic congenital distal SMA/arthrogryposis phenotype in a consanguineous setting ([Neurology Genetics, NXG.0000000000000312](https://www.neurology.org/doi/10.1212/NXG.0000000000000312)) — a distinct, allelic (not identical) disease entity.

**Carrier frequency:** Not established at a population level (extremely rare, largely private variants).

**Population demographics:** No specific ethnic or geographic predilection has been established for CMT2C; cases have been reported across European, North American, and Asian cohorts. Sex ratio: no strong skew reported (autosomal dominant disorder).

---

## 10. Diagnostics

**Molecular genetic testing (primary/definitive):**
- **Sequence analysis of *TRPV4*** is first-line, detecting missense, nonsense, splice-site variants, and small indels; identifies ~100% of currently known pathogenic variants; whole-gene deletion/duplication has not been reported in the autosomal dominant neuromuscular phenotype ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/))
- Testing modalities: single-gene sequencing, multigene CMT/HMN panels (including the differential-diagnosis gene list below), or phenotype-focused exome analysis

**Electrophysiology (EMG/NCV):**
- Reduced compound motor action potential (CMAP) amplitudes with **normal conduction velocities** (>40–60 m/s) — consistent with an axonal/neuronopathic rather than demyelinating process
- Sensory nerve action potentials (SNAPs): normal, decreased, or absent
- EMG: predominantly chronic neurogenic changes
([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/))

**Other clinical tests:**
- Laryngoscopy for vocal fold paresis
- Pulmonary function testing and dynamic breathing chest radiographs for diaphragm assessment
- Sleep study (central/obstructive sleep apnea screening)
- Audiologic evaluation (sensorineural hearing loss)
- Skeletal imaging when skeletal-dysplasia overlap is suspected
- Spinal MRI to evaluate for tethered cord in appropriate clinical settings

**Diagnostic criteria:** Diagnosis is established by combining "characteristic clinical and neurophysiologic findings" with identification of a heterozygous *TRPV4* variant suspected to cause channel gain-of-function ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/)).

**Differential diagnosis (genes to exclude/consider):** *ATP7A, BICD2, BSCL2, DCTN1, DYNC1H1, GARS1, HSPB1, HSPB3, HSPB8, IGHMBP2, JAG1, MYH14, PLEKHG5, SETX, SLC5A7, SMN1* ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/)) — these overlap clinically as other distal hereditary motor neuropathies/CMT2/SMA-spectrum disorders.

**Screening:** No population-based newborn screening; genetic counseling and predictive/cascade testing are offered to at-risk relatives given autosomal dominant inheritance and 50% recurrence risk, with the caveat that penetrance/expressivity cannot be predicted.

---

## 11. Outcome/Prognosis

- **Survival:** Most affected individuals have a **normal lifespan**. A subset with severe respiratory (diaphragmatic) involvement may have **shortened life expectancy secondary to respiratory complications** ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/)).
- **Morbidity:** Chronic motor disability (distal and proximal weakness, foot deformity, need for orthoses/mobility aids), laryngeal dysfunction with aspiration/airway risk, restrictive respiratory impairment, progressive hearing loss, and skeletal complications (scoliosis, contractures, hip dysplasia, tethered cord in ~7.5% of one 40-patient cohort).
- **Complications:** Airway obstruction precipitated by intercurrent URI in the context of pre-existing vocal fold paresis is a specifically flagged acute risk. Aspiration pneumonia risk from laryngeal dysfunction. Sleep-disordered breathing (including central sleep apnea).
- **Recovery potential:** The underlying motor neuron/axonal loss is not reversible with current standard-of-care (supportive) management; functional improvement is achieved via orthotic/surgical/rehabilitative support rather than disease reversal. The investigational TRPV4-inhibitor pipeline (see §12) specifically aims to change this by targeting the causal channel gain-of-function.
- **Prognostic factors:** Variant identity/position (correlating with degree of baseline Ca²⁺ elevation) predicts development of mixed neuropathy-skeletal phenotypes and *in vitro* sensitivity to pharmacologic channel inhibition — a mechanistic biomarker relevant to future trial stratification ([PMC8935273](https://pmc.ncbi.nlm.nih.gov/articles/PMC8935273/)).

---

## 12. Treatment

There is currently **no approved disease-modifying therapy**; management is supportive/multidisciplinary, though a mechanistically targeted therapeutic is in active clinical development.

**Multidisciplinary supportive care** (NCIT terms suggested in parentheses):
- **Orthotic/mobility support:** supportive shoes, orthotics, ankle-foot orthoses/knee-ankle-foot orthoses; orthopedic surgery for severe foot deformity (NCIT:C16186, Orthopedic Surgical Procedure); mobility aids and exercise as tolerated (NCIT:C15302, Physical Therapy)
- **Laryngeal management:** vocal fold lateralization surgery or tracheostomy in severe airway compromise; speech therapy (NCIT:C15329, Surgical Procedure; speech-language therapy term)
- **Respiratory management:** noninvasive ventilatory support, pulmonary function monitoring (NCIT:C15747, Supportive Care)
- **Spinal/orthopedic management:** kyphoscoliosis management; neurosurgical release of tethered spinal cord when symptomatic
- **Audiology:** hearing aids/rehabilitation
- **Genetic counseling** (NCIT:C15240)
- **Preventive care:** avoidance of obesity, avoidance of known neurotoxic medications, prompt treatment of URIs

**Experimental/targeted therapeutics (therapeutic_modality: SMALL_MOLECULE, mechanism: TRPV4 channel antagonism):**
- **ABS-0871** (Actio Biosciences) — a novel oral TRPV4 inhibitor purpose-built for TRPV4-positive CMT2C. First-in-human Phase 1 healthy-volunteer trial dosing began **March 2025**; the drug received **FDA Orphan Drug Designation and Rare Pediatric Disease Designation in August 2024**. In "novel construct-valid preclinical CMT2C rare disease models," ABS-0871 produced "marked improvements in motor function and mobility compared to untreated controls" ([BioSpace press release](https://www.biospace.com/press-releases/actio-biosciences-announces-first-participant-dosed-in-phase-1-clinical-trial-of-abs-0871-a-novel-trpv4-inhibitor-for-the-treatment-of-charcot-marie-tooth-disease-2c); [CMTAUSA](https://cmtausa.org/simply-cmt/actio-phasei/); [Actio Biosciences](https://actiobiosciences.com/actio-biosciences-announces-first-participant-dosed-in-phase-1-clinical-trial-of-abs-0871-a-novel-trpv4-inhibitor-for-the-treatment-of-charcot-marie-tooth-disease-2c/)).
- **Proof-of-concept preclinical rescue:** *Trpv4* knock-in mice with the severe, rapidly fatal neuromuscular phenotype can be **rescued by pharmacologic inhibition of TRPV4 channel activity** ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/)), providing strong mechanistic rationale for the antagonist approach.
- **Other TRPV4 antagonist tool/clinical compounds** (used in broader TRPV4-pathy research, not CMT2C-specific trials): **HC-067047** (a pyrrolocarboxamide research antagonist, IC50 ~48 nM human TRPV4) and **GSK2798745** (a spiro-carbamate that advanced to Phase II for heart failure/pulmonary edema indications, demonstrating human tolerability of TRPV4 antagonism as a drug class) ([MedChemExpress HC-067047](https://www.medchemexpress.com/HC-067047.html); [PMID 34531959](https://pubmed.ncbi.nlm.nih.gov/34531959/)).
- **CMT Research Foundation / HNF** natural history study of TRPV4 neuromuscular disease (CMT2C) is ongoing to characterize disease trajectory and support trial readiness ([CMTAUSA natural history](https://www.cmtausa.org/our-research/for-patients-and-families/patients-as-partners/natural-history-trpv4-cmt2c/); [HNF TRPV4 program](https://www.hnf-cure.org/research/trpv4/)).

**Pharmacogenomics:** Not applicable/established for this monogenic channelopathy (no drug-metabolism pharmacogenomic modifier reported).

**Treatment strategy:** Because the causal lesion is a well-characterized channel gain-of-function, the field's guiding treatment algorithm is genotype-directed small-molecule channel antagonism layered on top of standard multidisciplinary supportive/rehabilitative care — a precision-medicine approach analogous to other channelopathies.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the population sense (autosomal dominant single-gene disorder); the relevant "prevention" lever is reproductive/genetic counseling rather than public-health risk-factor modification.
- **Secondary prevention (early detection):**
  - Genetic counseling and predictive testing for at-risk relatives of a known proband (50% recurrence risk), with explicit counseling that reduced penetrance/variable expressivity precludes reliable phenotype prediction
  - Prenatal/preimplantation genetic testing options can be discussed for known familial variants (general reproductive-genetics principle; not specifically documented as routinely used for CMT2C in the sources reviewed)
  - Vigilant surveillance for laryngeal/respiratory involvement in known carriers, given the acute-risk nature of airway compromise
- **Tertiary prevention (complication avoidance in affected individuals):** Recommended annual surveillance per GeneReviews includes neurologic exam/PT assessment, otolaryngology evaluation of laryngeal function, dynamic breathing chest radiograph + pulmonary function tests, sleep study, hearing assessment, musculoskeletal evaluation (contractures, hip dysplasia, scoliosis, tethered cord signs), and weight/height/obesity assessment ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/)).
- **Agents/circumstances to avoid:** Obesity, known neurotoxic medications (per CMT Association neurotoxic drug list), and untreated upper respiratory infections (risk of acute airway compromise from vocal-fold edema).
- **Immunization:** No CMT2C-specific vaccine strategy; general recommendation would be routine respiratory-pathogen immunization (e.g., influenza) given baseline respiratory vulnerability, though this is inferred rather than explicitly documented in the sources found.
- **Genetic counseling:** Central to prevention/family planning in this dominant disorder; standard NSGC/ACMG genetic-counseling frameworks apply.

---

## 14. Other Species / Natural Disease

- **Taxonomy of study organisms:** *Mus musculus* (NCBITaxon:10090), *Drosophila melanogaster* (NCBITaxon:7227); orthologous *Trpv4* gene exists broadly across vertebrates.
- **Naturally occurring disease in other species:** No naturally occurring companion-animal or wildlife TRPV4 neuropathy analog was identified in this search (this appears to be a human-specific documented clinical entity to date; OMIA search was not directly performed but no hits surfaced organically — flag as a gap to confirm via a direct OMIA query if veterinary relevance is needed).
- **Orthologous gene:** Mouse *Trpv4* (MGI ortholog of human *TRPV4*) is the basis of the knock-in disease models described below; NCBI Gene entries exist for mouse and other model organisms' *Trpv4* orthologs.
- **Comparative pathology/evolutionary conservation:** The ankyrin-repeat arginine residues mutated in human disease are evolutionarily conserved, which is why mouse knock-in of the orthologous R269C/R232C substitutions faithfully reproduces a severe motor phenotype (see below) — supporting deep functional conservation of the TRPV4 channel-gating mechanism across mammals.
- **Zoonotic potential/transmission:** Not applicable — this is a non-infectious monogenic channelopathy.

---

## 15. Model Organisms

**Mouse (mammalian genetic knock-in models):**
- *Trpv4^R269C* and *Trpv4^R232C* knock-in mice (endogenous locus, disease-causing missense knock-ins) exhibit **weakness, early lethality, and regional motor neuron loss**, closely recapitulating the severe end of the human phenotype spectrum ([Chen et al. 2024, PMC11316273](https://pmc.ncbi.nlm.nih.gov/articles/PMC11316273/); PMID 38776392).
- Symptomatic mutant mice show **focal disruption of blood–spinal cord barrier (BSCB) integrity**, linked to endothelial-cell-autonomous TRPV4 gain-of-function.
- **Key causal/rescue experiment:** Conditional genetic deletion of the mutant *Trpv4* allele specifically from **vascular endothelial cells** (but not from neurons, glia, or muscle) rescues the motor and survival phenotypes — establishing endothelial cells, not neurons, as the primary disease-driving cell type in this model ([PMC11316273](https://pmc.ncbi.nlm.nih.gov/articles/PMC11316273/)).
- Separately, GeneReviews notes that *Trpv4* knock-in mice with a "severe, rapidly progressive fatal neuromuscular phenotype" can be **rescued by pharmacologic TRPV4 channel inhibition**, directly supporting the small-molecule antagonist therapeutic strategy now in human trials ([GeneReviews NBK201366](https://www.ncbi.nlm.nih.gov/books/NBK201366/)).
- **Limitations:** As with many gain-of-function knock-in models, the mouse phenotype (early lethality, prominent vascular/BSCB pathology) is more acute/severe than the typical chronic, slowly progressive human CMT2C course — the vascular-barrier mechanism's relative contribution in human disease (versus a purely cell-autonomous neuronal mechanism) remains an area of active investigation, representing a **human-model translational-fidelity open question** worth flagging as a `HUMAN_MODEL_MISMATCH`-type knowledge gap for KB curation (rodent lethality/BSCB phenotype vs. the typically non-lethal, chronic human trajectory).

**Cellular/heterologous models:**
- HEK293 cells transiently transfected with mutant TRPV4 constructs (the original functional-validation system) — demonstrate increased constitutive/evoked Ca²⁺ channel currents and cytotoxicity for CMT2C-associated variants ([Deng et al. 2010](https://www.nature.com/articles/ng.509); [Landouré et al. 2010](https://www.nature.com/articles/ng.512); PMID 21288981).
- Structural biology: Cryo-EM of purified TRPV4–RhoA complexes used to map the disease-residue interface and mechanistically explain gain-of-function ([PMC10290081](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10290081/)).

**Invertebrate models:**
- ***Drosophila melanogaster*** models expressing neuropathy-causing TRPV4 mutants have been used to study the ubiquitination-dependent regulatory mechanism, showing reduced channel ubiquitination and channel overactivity that can be experimentally suppressed by enhancing ubiquitination ([Aisenberg et al., PMC9010760](https://pmc.ncbi.nlm.nih.gov/articles/PMC9010760/); grant description at [Grantome F31-NS105404](https://grantome.com/grant/NIH/F31-NS105404-01A1)).

**Applications:** These models collectively support (1) confirmation of the gain-of-function pathomechanism, (2) identification of endothelial cells as an unexpected primary disease-driving cell type, (3) a druggable regulatory node (ubiquitination of channel IDRs), and (4) preclinical proof-of-concept for pharmacologic TRPV4 antagonism as a rational, mechanism-based therapeutic strategy now advancing into human Phase 1 trials (ABS-0871).

---

## Summary of Key Evidence Gaps for Curation

1. No formal prevalence/incidence rate-per-100,000 figure was located specifically for CMT2C (only relative frequency *within* CMT2 cohorts, 1–3.5% to ~16% in enriched subgroups) — recommend using Orphanet's own epidemiology table (ORPHA:99937) directly if a numeric prevalence class is required.
2. No germline mosaicism or founder-effect data specific to *TRPV4* CMT2C were found.
3. No large-scale human transcriptomic/proteomic dataset from patient-derived tissue was identified (model-organism/cell-line data dominate the molecular-profiling literature).
4. No veterinary/naturally-occurring animal disease analog was found (distinguishing this from many other monogenic channelopathies with OMIA entries).
5. The apparent tension between the acute/lethal, endothelial-driven mouse knock-in phenotype and the typically chronic, non-lethal human course is a candidate `HUMAN_MODEL_MISMATCH` worth explicit curation.

---

### Sources

- [OMIM #606071 — Hereditary Motor and Sensory Neuropathy, Type IIC](https://omim.org/entry/606071)
- [OMIM *605427 — TRPV4](https://www.omim.org/entry/605427)
- [Orphanet 99937 — Autosomal dominant CMT type 2C](https://www.orpha.net/en/disease/detail/99937)
- [MedGen C1853710](https://www.ncbi.nlm.nih.gov/medgen/342947)
- [GARD — CMT2C](https://rarediseases.info.nih.gov/diseases/1250/charcot-marie-tooth-disease-axonal-type-2c)
- [GeneReviews — Autosomal Dominant TRPV4-Related Disorders (NBK201366)](https://www.ncbi.nlm.nih.gov/books/NBK201366/)
- [Deng et al., Nat Genet 2010 — SPSMA and CMT2C are allelic disorders caused by TRPV4](https://www.nature.com/articles/ng.509)
- [Landouré et al., Nat Genet 2010 — Mutations in TRPV4 cause CMT2C](https://www.nature.com/articles/ng.512)
- [Journal of Human Genetics 2010 — TRPV4-pathy, a novel channelopathy](https://www.nature.com/articles/jhg201037)
- [Neurology 2011 — TRPV4 mutations and cytotoxic hypercalcemia (PMID 21288981)](https://pubmed.ncbi.nlm.nih.gov/21288981/)
- [Neurology 2015 — Phenotypic spectrum and incidence of TRPV4 mutations (WNL.0000000000000450)](https://www.neurology.org/doi/10.1212/WNL.0000000000000450)
- [NeuroMolecular Medicine 2019 — Incidence/features of TRPV4-linked axonal neuropathies in a USA CMT2 cohort](https://link.springer.com/article/10.1007/s12017-019-08564-4)
- [BMC Neurology / PMC10311707 — TRPV4 mutation causing CMT2C/SPSMA overlap in one family](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10311707/)
- [PMC8935273 — TRPV4 mutations causing mixed neuropathy/skeletal phenotypes result in severe gain of function](https://pmc.ncbi.nlm.nih.gov/articles/PMC8935273/)
- [PMC10290081 — TRPV4–Rho GTPase complex structures reveal mechanisms of gating and disease](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10290081/)
- [PMID 33664271 — Neuropathy-causing TRPV4 mutations disrupt TRPV4–RhoA interactions and impair neurite extension](https://pubmed.ncbi.nlm.nih.gov/33664271/)
- [PMC9010760 — Multiubiquitination of TRPV4 reduces channel activity independent of surface localization](https://pmc.ncbi.nlm.nih.gov/articles/PMC9010760/)
- [Grantome F31-NS105404 — Aisenberg, ubiquitination and TRPV4 gain-of-channel function](https://grantome.com/grant/NIH/F31-NS105404-01A1)
- [PMC11316273 / PMID 38776392 — Gain-of-function TRPV4 in endothelial cells drives blood-CNS barrier breakdown and motor neuron degeneration in mice](https://pmc.ncbi.nlm.nih.gov/articles/PMC11316273/)
- [Neurology Genetics NXG.0000000000000312 — Homozygous TRPV4 mutation causes congenital distal SMA and arthrogryposis](https://www.neurology.org/doi/10.1212/NXG.0000000000000312)
- [BioSpace — Actio Biosciences ABS-0871 Phase 1 trial announcement](https://www.biospace.com/press-releases/actio-biosciences-announces-first-participant-dosed-in-phase-1-clinical-trial-of-abs-0871-a-novel-trpv4-inhibitor-for-the-treatment-of-charcot-marie-tooth-disease-2c)
- [Actio Biosciences press release](https://actiobiosciences.com/actio-biosciences-announces-first-participant-dosed-in-phase-1-clinical-trial-of-abs-0871-a-novel-trpv4-inhibitor-for-the-treatment-of-charcot-marie-tooth-disease-2c/)
- [CMTAUSA — Actio Phase I announcement](https://cmtausa.org/simply-cmt/actio-phasei/)
- [CMTAUSA — Natural History of TRPV4 Neuromuscular Disease (CMT2C)](https://www.cmtausa.org/our-research/for-patients-and-families/patients-as-partners/natural-history-trpv4-cmt2c/)
- [HNF-Cure — TRPV4 research program](https://www.hnf-cure.org/research/trpv4/)
- [PMID 34531959 — Major circulating human metabolite of TRPV4 antagonist GSK2798745](https://pubmed.ncbi.nlm.nih.gov/34531959/)
- [MedChemExpress — HC-067047](https://www.medchemexpress.com/HC-067047.html)
- [ClinicalGenome / ClinGen CMT Gene Curation Expert Panel](https://clinicalgenome.org/affiliation/40063/)
- [ClinVar RCV000645535 (p.Arg774Cys, CMT2C)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000645535/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 13 |
| On topic | 6 |
| Off topic | 0 |

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1212/WNL.0b013e31820f2de3`: "cytotoxic hypercalcemia"
  - Reference resolved but exposes no abstract or full text to search

All extracted references resolved successfully.