---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T04:24:09.936586'
end_time: '2026-08-27T04:29:56.266001'
duration_seconds: 346.33
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: FAM111A-Related Skeletal Dysplasia
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
  web_search_requests: 23
  num_turns: 33
  total_cost_usd: 1.6023811999999997
  session_id: a1f65bb8-1b49-516c-9197-25fb2b9c84dd
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 31
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 25
  on_topic: 20
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** FAM111A-Related Skeletal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **FAM111A-Related Skeletal Dysplasia** covering all of the
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

I'll research FAM111A-Related Skeletal Dysplasia now, loading web search tools and gathering information from primary literature.

# FAM111A-Related Skeletal Dysplasia: Comprehensive Research Report

## Executive Summary

FAM111A-related skeletal dysplasia is not a single entity but an allelic disease spectrum caused by variants in **FAM111A** (FAM111 trypsin-like peptidase A; HGNC:24151; chromosome 11q12.1), spanning from the relatively milder, non-lethal **Kenny-Caffey syndrome type 2 (KCS2)** (OMIM #127000) at one end to the perinatally lethal **Gracile Bone Dysplasia / Osteocraniostenosis (GCLEB/OCS)** (OMIM #602361) at the other, with a growing recognition of **autosomal recessive forms** at both ends of severity described in 2024–2025. The unifying molecular mechanism is **gain-of-function (hyperactivation) of the FAM111A serine protease**, a PCNA-associated enzyme that normally clears protein obstacles from DNA replication forks; disease-causing variants relieve autoinhibitory constraints on the protease, producing a dose-dependent, cytotoxic excess of proteolytic activity that impairs replication, triggers apoptosis, and secondarily disrupts skeletal mineralization and parathyroid gland development (Unger et al., *Am J Hum Genet* 2013, PMID: [23684011](https://pubmed.ncbi.nlm.nih.gov/23684011/); Alabert lab and collaborators, EMBO Reports 2020, PMC: [PMC7534640](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7534640/)).

---

## 1. Disease Information

**Overview.** FAM111A-related skeletal dysplasia comprises a phenotypic continuum of rare, genetically defined skeletal/endocrine disorders unified by pathogenic variation in *FAM111A*:

| Entity | OMIM | Severity | Typical inheritance |
|---|---|---|---|
| Kenny–Caffey syndrome, type 2 (KCS2) | #127000 | Non-lethal; short stature + hypoparathyroidism | Autosomal dominant (usually de novo); recessive forms now reported |
| Gracile bone dysplasia (GCLEB) / Osteocraniostenosis (OCS) | #602361 | Perinatally lethal | Autosomal dominant (de novo) and recessive (biallelic hypomorphic/hypermorphic) forms |
| Gene | *FAM111A* | OMIM *615292 | 11q12.1 |

Osteocraniostenosis (OCS) and gracile bone dysplasia (GCLEB) are generally treated as the same entity/synonymous terminology in the literature (also called "osteocraniosplenic syndrome" when splenic hypoplasia is emphasized).

**Key identifiers:**
- OMIM: 127000 (KCS2), 602361 (GCLEB/OCS), *615292 (FAM111A gene)
- Orphanet: ORPHA2333 (Kenny-Caffey syndrome)
- MONDO/MedGen: Osteocraniostenosis, MedGen concept C1865639
- MeSH: Kenny-Caffey Syndrome (D064878)
- Gene: HGNC:24151, NCBI Gene 63901, Ensembl ENSG00000166801
- Contrast with the *TBCE*-associated, unrelated **Kenny-Caffey syndrome type 1 (KCS1)**, OMIM #244460, an autosomal recessive disorder allelic to **Sanjad-Sakati syndrome** — an important differential (see §10).

**Synonyms:** Kenny-Caffey syndrome, dominant type; Kenny-Caffey syndrome, autosomal dominant; osteocraniostenosis; osteocraniosplenic syndrome; gracile bone dysplasia with skull dysplasia.

**Evidence basis.** The knowledge base for this condition derives almost entirely from **aggregated case reports and small case series/cohort reviews** (total published cohort now approaching ~50 KCS2 patients and fewer than 30 GCLEB/OCS cases), rather than large EHR-derived or population-registry datasets, reflecting its extreme rarity (Chen & Zou, *Mol Genet Genomic Med* 2024, PMID: [38591167](https://pmc.ncbi.nlm.nih.gov/articles/PMC11002637/); malacards.org).

---

## 2. Etiology

**Disease causal factor.** Monogenic — heterozygous (dominant) or, in newly described families, biallelic (recessive) pathogenic variants in *FAM111A*, essentially always missense variants clustering in and around the C-terminal trypsin-like serine protease domain (SPD). No environmental, infectious, or multifactorial contribution is documented; this is a purely genetic/mechanistic disease.

**Genetic risk factors:**
- **Dominant hotspot:** c.1706G>A (p.Arg569His) accounts for ~70% (32/46) of reported KCS2 cases in one systematic literature review, and up to 87.5% of some regional cohorts (Chen & Zou 2024). It arises recurrently *de novo* (ClinVar RCV000050209).
- Other recurrent dominant KCS2/OCS variants: p.Tyr511His (c.1531T>C), p.Ser541Pro, p.Asp528Gly (D528G), p.Thr338Ala (T338A), and others in the SPD (Isojima et al., *J Bone Miner Res* 2014; Chen & Zou 2024).
- **De novo rate:** ~79.5% (31/39) of dominant cases arise de novo; parent-to-child (both mother-to-daughter and, newly documented, father-to-daughter) transmission has been reported, confirming full penetrance with dominant inheritance (Chen & Zou 2024).
- **Newly described recessive alleles (2024–2025):**
  - *Hypermorphic* recessive: homozygous p.Tyr414Cys / p.Tyr414Asn — a "quantitative hypermorphic" mechanism where the homozygous state produces intermediate protease hyperactivation sufficient to cause KCS2/OCS, while heterozygous carriers are asymptomatic (Li et al., *JCI Insight* 2025, PMID: [39932783](https://pmc.ncbi.nlm.nih.gov/articles/PMC11949059/)).
  - *Hypomorphic* recessive: homozygous synonymous variant c.81G>A (p.Pro27=) causing aberrant splicing, reduced mRNA, and near-absent protein — a partial loss-of-function mechanism in a consanguineous family (2 siblings) (Journal of Human Genetics 2024, DOI: 10.1038/s10038-024-01301-1, PMC: [PMC11762410](https://pmc.ncbi.nlm.nih.gov/articles/PMC11762410/)).
  - Compound heterozygous *FAM111A* variants have also been reported causing autosomal recessive KCS2 (PMID: [34382758](https://pubmed.ncbi.nlm.nih.gov/34382758/)).
- **No modifier genes, susceptibility loci, or GWAS hits** are established — this is a fully penetrant Mendelian disease, not a complex/polygenic trait.

**Environmental risk factors:** None identified; not associated with teratogens, maternal exposures, or lifestyle factors.

**Protective factors:** None described; there is no known protective allele. Notably, mouse *Fam111a* knockout studies (below) show **no overt skeletal or electrolyte phenotype**, implying the human disease mechanism is a toxic gain-of-function rather than simple loss of a protective/essential activity — so there is no analogous "loss-of-function protects" relationship as seen in some other disorders.

**Gene-environment interactions:** None reported; disease expression appears to be driven purely by the quantitative level of FAM111A protease hyperactivation (a dose-dependent, cell-intrinsic mechanism), not by external modifiers.

---

## 3. Phenotypes

Phenotype data below are drawn primarily from the 46-patient KCS2 literature synthesis (Chen & Zou 2024, PMC11002637) and OMIM.

### Cardinal / near-universal features (KCS2)
| Phenotype | Frequency | Suggested HPO term |
|---|---|---|
| Proportionate short stature (severe, congenital-onset, often −3 to −10 SDS) | 95–100% | HP:0003508 (Proportionate short stature) |
| Hypoparathyroidism | 80–86.5% | HP:0000829 (Hypoparathyroidism) |
| Hypocalcemia | 82.9% | HP:0002901 (Hypocalcemia) |
| Medullary stenosis of tubular bones | 73% | HP:0003044 (Long bone bowing) / custom: medullary stenosis |
| Cortical thickening of long bones | 69.4% | HP:0002684 (Thickened cortex of long bones) |
| Delayed closure of anterior fontanelle | 67.6% | HP:0001005 (Large fontanelles) |
| Prominent/bossed forehead | 73.5% | HP:0000239 (Frontal bossing) |
| Ocular abnormalities (hypermetropia most common, 60%) | ~75% overall | HP:0000540 (Hypermetropia); HP:0000568 (Microphthalmia) |
| Dental abnormalities (defective dentition, caries, oligodontia) | ~72% | HP:0000692 (Abnormality of dental enamel) / HP:0000668 (Dental crowding) / HP:0000668 |
| Seizures/hypocalcemic spasms | ~70% | HP:0001250 (Seizure) |
| Micrognathia | 35.3% | HP:0000347 |
| Cerebral calcification (basal ganglia, secondary to chronic hypocalcemia) | 35.3% | HP:0002514 (Basal ganglia calcification) |
| Depressed nasal bridge | 38.2% | HP:0005280 |
| Small eyes | 41.2% | HP:0020045 |
| Micropenis / microorchidism (males) | reported in subset | HP:0000054 / HP:0000035 |
| Growth hormone deficiency | 37.5% of those tested | HP:0000824 |
| Intellectual disability | 11.6% (an emerging, previously atypical finding — historically KCS2 was defined by *normal* intelligence, distinguishing it from KCS1/Sanjad-Sakati) | HP:0001249 |

**Onset/course:** Prenatal ultrasound may show shortened long bones and IUGR in some cases; postnatal presentation is frequently a **neonatal hypocalcemic seizure** picture. Mean age at diagnosis across the literature is 13.2 years (range 20 weeks gestation to 66 years — reflecting both severe neonatal presentations and mild adult-diagnosed cases). Calcium control tends to stabilize with age in survivors, but long-term complications (chronic kidney disease, nephrocalcinosis from treatment-related hypercalciuria) are increasingly recognized (Chen & Zou 2024; case report literature).

### Gracile Bone Dysplasia / Osteocraniostenosis (the lethal end of the spectrum)
- Gracile (thin-diaphysis) long bones, HP:0004970 (Thin long bones)
- Cloverleaf-shaped, hypomineralized skull with premature closure of basal cranial sutures — HP:0002676 (Cloverleaf skull) / HP:0011328 (Craniosynostosis)
- Microphthalmia / aniridia — HP:0000568 / HP:0000526
- Small philtrum, short nose, narrow mouth with tented upper-lip vermilion — HP:0000322 (loss of prominent premaxilla-type features), HP:0000463 (short nose)
- Splenic hypoplasia/aplasia — HP:0001743 (Absent spleen)/HP:0001744 (Splenomegaly is the opposite; use HP:0030068 for asplenia or HP:0001743)
- Overmodeled, short, gracile tubular bones of hands/feet; brachydactyly — HP:0009381
- Irregular, gracile ribs — HP:0000772
- Fetal hydrops / pleural effusions in some severe/lethal cases — HP:0001789 (Hydrops fetalis)
- Outcome: most patients are stillborn or die within hours to months of birth from respiratory insufficiency due to a restrictive, hypomineralized thoracic cage (rarediseases.org via search synthesis; Genes 2022, PMID: [35205306](https://pubmed.ncbi.nlm.nih.gov/35205306/)).

**Quality of life impact:** For KCS2 survivors, QoL is driven chiefly by (1) seizure burden from labile hypocalcemia, (2) short stature and its psychosocial effects, (3) visual impairment from significant hypermetropia, and (4) dental morbidity requiring extensive restorative care. No formal EQ-5D/SF-36/PROMIS studies specific to KCS2 were identified in the literature (consistent with its extreme rarity) — this is a case-report-level knowledge base, not systematically measured QoL data.

---

## 4. Genetic/Molecular Information

**Causal gene:** *FAM111A* (HGNC:24151; NCBI Gene ID 63901; OMIM *615292), encoding a 611-amino-acid, ~70 kDa protein.

**Protein domain architecture** (Unravelling FAM111A/FAM111B review, PMC: [PMC10931937](https://pmc.ncbi.nlm.nih.gov/articles/PMC10931937/)):
- N-terminal **PCNA-interacting protein (PIP) box** — tethers FAM111A to the DNA sliding clamp PCNA at replication forks
- Two **ubiquitin-like domains (UBL-1, UBL-2)**
- C-terminal **trypsin-like serine protease domain (SPD)**, catalytic triad His385–Asp439–Ser541, structurally resembling Trypsin-2/PRSS2 but with chymotrypsin-like substrate specificity
- The protein undergoes **autocleavage** between Phe334 and Gly335

**Variant classification and type:** Essentially all reported pathogenic variants are **missense** substitutions clustering in the serine protease domain (dominant hotspot p.Arg569His; other dominant sites p.Tyr511His, p.Ser541Pro, p.Asp528Gly, p.Thr338Ala; recessive sites p.Tyr414Cys/Asn); one recessive **synonymous/splice-altering** variant (p.Pro27=) has also been reported causing loss of function. No large structural rearrangements, frameshift, or nonsense variants have been reported to cause disease — consistent with a strict gain-of-function/toxic mechanism for the dominant/hypermorphic recessive forms, where haploinsufficiency (nonsense/frameshift null alleles) is apparently tolerated (as also suggested by the viable, largely unaffected *Fam111a*-null mouse — see §15).

**Allele frequency:** All known pathogenic missense variants are absent or present at only extremely low frequency in gnomAD population databases (consistent with a fully penetrant, mostly de novo dominant disease); specific gnomAD allele counts were not enumerated in the sources reviewed but rarity is implicit in ClinVar submissions for this gene.

**Somatic vs. germline:** Disease-causing variants are germline (constitutional); separately, *FAM111A* has been implicated in **somatic** contexts in cancer genomics (see below), which is a distinct, unrelated body of literature from the skeletal dysplasia.

**Functional consequence — the core molecular mechanism:**
FAM111A pathogenic variants are **gain-of-function (hyperactivating)** with respect to its intrinsic serine protease activity. Two converging structural/functional studies establish this:
1. Kim et al./Alabert-lab-adjacent work (EMBO Reports 2020, PMC: [PMC7534640](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7534640/)) showed that "FAM111A proteolytic activity suppresses DNA replication and transcription by displacing key effectors of these processes from chromatin, triggering rapid programmed cell death by Caspase-dependent apoptosis... Patient-associated point mutations in FAM111A exacerbate these phenotypes by hyperactivating its intrinsic protease activity."
2. A 2024 X-ray crystallography study (Nature Communications, PMID: [38453899](https://pmc.ncbi.nlm.nih.gov/articles/PMC10920703/)) solved the SPD structure (using a catalytically dead S541A mutant to avoid autocleavage) and showed that **FAM111A is a dimerization-dependent protease**: dimerization via an N-terminal helix triggers an allosteric activation cascade from a "dimerization sensor loop" to the oxyanion hole through disorder-to-order transitions, and this dimerization is essential for proteolytic activity against DNA-protein crosslink (DPC) substrates in cells (though dispensable for autocleavage).
3. The 2025 JCI Insight recessive-allele paper (PMID: [39932783](https://pmc.ncbi.nlm.nih.gov/articles/PMC11949059/)) refined this to a **quantitative, gene-dose-dependent model**: Tyr414 sits in the dimer-sensing L4 loop, contacting Tyr359 in the central β-sheet; substitutions here partially disrupt the allosteric network, producing a *mild* gain-of-function that is subclinical in heterozygotes but disease-causing when homozygous — directly explaining how the same gene produces both dominant (single strong hypermorphic allele) and recessive (double weak hypermorphic allele, or biallelic hypomorphic-loss-of-function) inheritance patterns. Structural modeling also predicts that more severe positions (e.g., Tyr562Ser) are "far more destabilizing," correlating with the lethal OCS phenotype — an emerging genotype-severity correlation.

**Epigenetic information / chromosomal abnormalities:** No epigenetic (DNA methylation/histone) mechanism or chromosomal-scale abnormality (aneuploidy, translocation) has been implicated in FAM111A-related skeletal dysplasia; disease is driven by point-mutation-level protein hyperactivation, not epigenetic dysregulation of the locus itself.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributing factors are documented for FAM111A-related skeletal dysplasia — it is a purely monogenic disorder with full/near-full penetrance independent of exposure history. (Note: FAM111A itself has a documented role as a host **antiviral restriction factor** — see §6 — but this is a downstream *consequence* of its normal biology, not an environmental trigger of the skeletal dysplasia phenotype.)

---

## 6. Mechanism / Pathophysiology

### Causal chain (upstream → downstream)
1. **Molecular trigger:** Germline missense variant in the FAM111A serine protease domain (or, in recessive hypermorphic disease, a homozygous weakly-activating variant) → disrupted allosteric regulation of the dimerization-sensor-to-catalytic-site network.
2. **Molecular consequence:** Hyperactivated (gain-of-function) intrinsic serine protease activity — "unrestrained" relative to wild-type, which is normally kept tightly autoinhibited and only locally activated at replication forks encountering protein obstacles.
3. **Cellular consequence — replication/chromatin disruption:** Excess FAM111A protease activity **displaces key DNA replication and transcription effectors from chromatin**, impairs **PCNA chromatin loading**, causes accumulation of DNA damage markers (γ-H2AX), and reduces efficient replication origin activation (Rios-Szwed et al., *Life Sci Alliance* 2023, PMID: [37793778](https://pubmed.ncbi.nlm.nih.gov/37793778/); JCI Insight 2025).
4. **Cellular fate:** Triggers **caspase-dependent apoptosis** — cleaved Caspase-3 elevation is a direct functional readout of pathogenic-variant hyperactivation in patient-derived and engineered cell studies.
5. **Tissue-level consequence:** In tissues most dependent on tightly-regulated proliferation during embryonic/fetal development — parathyroid gland progenitors, osteoblast/chondrocyte precursors in growth plates, ocular and dental primordia — excess apoptosis and replication stress impairs organogenesis, producing **parathyroid gland hypoplasia/dysfunction (hypoparathyroidism)** and **impaired skeletal growth-plate and cortical bone development** (medullary stenosis, cortical thickening, short stature).
6. **Organism-level consequence:** Chronic hypoparathyroidism → hypocalcemia → secondary neurologic (seizures) and cerebral (basal ganglia calcification) sequelae; skeletal dysgenesis → short stature, cranial/dental/ocular dysmorphism; in the most severe (lethal) allelic end of the spectrum, a hypomineralized, restrictive thoracic cage → fatal respiratory insufficiency (osteocraniostenosis).

The rhPTH treatment case report (PMC: [PMC13025059](https://pmc.ncbi.nlm.nih.gov/articles/PMC13025059/)) proposes specifically that "FAM111A dysfunction impairs parathyroid progenitor cell development during embryogenesis" — i.e., the parathyroid glands are structurally hypoplastic/dysfunctional from a developmental replication-stress insult, rather than merely under-secreting from an otherwise normal gland, which is the rationale for hormone-replacement (rather than secretagogue) therapy.

### Molecular pathways / biological processes (with suggested GO terms)
- Serine-type endopeptidase activity — **GO:0004252**
- PCNA-dependent DNA replication / replisome function — **GO:0006260** (DNA replication)
- Regulation of DNA replication origin licensing/firing — **GO:0006270** (DNA replication initiation)
- Resolution of DNA-protein crosslinks (DPC repair), including at trapped topoisomerase I (TOP1) and PARP1-DNA complexes — related to **GO:0006281** (DNA repair)
- Positive regulation of apoptotic process / caspase activation — **GO:0043065**, **GO:0006919**
- Antiviral innate immune restriction (vaccinia virus I3 protein autophagic degradation; RFC3-mediated RNA virus restriction via IRF2) — **GO:0051607** (defense response to virus)

### Cell types and tissues involved (with suggested CL/UBERON terms)
- Parathyroid chief cell (CL:0000446) / parathyroid gland (UBERON:0001132) — site of hypoplasia underlying hypoparathyroidism
- Osteoblast (CL:0000062) and chondrocyte (CL:0000138) in growth plate cartilage (UBERON:0002229) — impaired proliferation/replication underlying medullary stenosis and short stature
- Long bone diaphysis (UBERON:0003457) — cortical thickening/medullary stenosis site
- Fibroblasts (patient-derived skin fibroblasts, CL:0000057) — the standard functional-validation cell type used across the cited mechanistic papers (e.g., near-absent FAM111A protein demonstrated in fibroblasts of the recessive hypomorphic-splice family)
- Lens/ocular structures — relevant to hypermetropia/microphthalmia phenotype (UBERON:0000970, eye)
- CD4+/CD8+ T cells, CD19+ B cells, NK cells, monocytes — FAM111A is broadly expressed in these immune populations, motivating (still unresolved) investigation of a possible immune component to the "recurrent infection" phenotype noted in some KCS2 patients, though direct immunodeficiency testing in reported cases has generally shown **normal T-cell numbers and immunoglobulin levels** despite clinical infection susceptibility — an open mechanistic question rather than an established immunodeficiency (search synthesis of case literature).

### Protein dysfunction
Not a loss-of-function/misfolding disease in the classical sense; rather, the disease protein is **structurally intact but biochemically dysregulated** — an unrestrained/hyperactive enzyme. This distinguishes FAM111A-related dysplasia mechanistically from most other skeletal dysplasias (e.g., collagenopathies), which are typically loss-of-function or dominant-negative structural-protein disorders.

### Broader biology of FAM111A/FAM111B (paralog context)
- FAM111A protects replication forks from protein obstacles via its trypsin-like domain, notably resolving trapped TOP1 and PARP1-DNA cleavage complexes (Nature Communications 2020, PMID: [32165630](https://pubmed.ncbi.nlm.nih.gov/32165630/); 2024 dimerization paper).
- FAM111A acts as a broad-spectrum **antiviral restriction factor**: it targets the vaccinia virus DNA-binding protein I3 for autophagic degradation, and via IRF2/RFC3 signaling contributes to RNA-virus restriction (PMC10931937; also see "FAM111A induces nuclear dysfunction in disease and viral restriction," PMID: [33369867](https://pubmed.ncbi.nlm.nih.gov/33369867/)).
- The paralog **FAM111B** causes a distinct disease, **POIKTMP** (hereditary fibrosing poikiloderma with tendon contractures, myopathy, and pulmonary fibrosis), via a related but molecularly distinct gain-of-function/telomere-maintenance (TRF2-dependent) mechanism — useful comparator disease for curators researching the FAM111 gene family, but genetically and clinically separate from FAM111A-related skeletal dysplasia.
- **Somatic FAM111A** variation/expression has separately been implicated (with much lower evidence weight, correlative genomics) in prostate cancer predisposition, glioma prognosis, gastric cancer, and hepatocellular carcinoma (via a FAM111A-DT long non-coding RNA/m6A mechanism) — these are not part of the Mendelian skeletal dysplasia phenotype and should be treated as a separate cancer-genomics literature.

### Omics / advanced technologies
No transcriptomic (GEO/ArrayExpress), proteomic (PRIDE), metabolomic, single-cell, or spatial-transcriptomic dataset specific to patient tissue in FAM111A-related skeletal dysplasia was identified in this search — molecular characterization to date rests on **patient-derived fibroblast functional assays** (chromatin fractionation, NanoBRET dimerization assays, apoptosis marker immunoblotting) and **heterologous overexpression systems**, not large-scale omics profiling. This is a notable knowledge gap given the rarity of patient material.

---

## 7. Anatomical Structures Affected

**Organ level:**
- Skeletal system (primary): long bones (femur, tibia, radius, ulna — cortical thickening, medullary stenosis, gracile diaphyses in the lethal form), skull (delayed fontanelle closure in KCS2; cloverleaf, hypomineralized skull in OCS), ribs (gracile/irregular in OCS), hands/feet (short, overmodeled tubular bones; brachydactyly)
- Endocrine system: parathyroid glands (hypoplasia/dysfunction → hypoparathyroidism); anterior pituitary/GH axis (deficiency in ~37.5% tested)
- Eyes: hypermetropia, microphthalmia, papilledema
- Teeth: enamel defects, oligodontia, caries
- Spleen: hypoplasia/aplasia (OCS)
- CNS: basal ganglia calcification (secondary to chronic hypocalcemia); seizures
- Reproductive: micropenis/microorchidism reported in a subset of males
- Respiratory: restrictive lung insufficiency from thoracic cage dysplasia — the proximate cause of death in lethal OCS

**Body systems:** Skeletal, endocrine (parathyroid/pituitary), ophthalmologic, dental, and (secondarily) neurologic systems are the principal ones involved; splenic and respiratory involvement is specific to the lethal OCS end of the spectrum.

**Tissue/cell level:** Growth-plate cartilage and cortical/trabecular bone-forming cells (chondrocytes, osteoblasts); parathyroid chief cells; corneal/lens tissue.

**Subcellular level:** The core lesion is **nuclear/chromatin-level** — FAM111A acts at replication forks and chromatin (GO Cellular Component: nucleus GO:0005634, replication fork GO:0005657); pathogenic hyperactivation displaces replication/transcription machinery from chromatin.

**Lateralization:** Not applicable — this is a systemic, bilateral/symmetric developmental disorder (e.g., bilateral ocular and dental findings), not a lateralized process.

---

## 8. Temporal Development

**Onset:**
- **KCS2:** Congenital/perinatal onset of skeletal findings (detectable on prenatal ultrasound as shortened long bones in some cases); classic clinical presentation is a **neonatal or early-infancy hypocalcemic seizure**. Diagnosis can, however, be delayed into adulthood in milder presentations (reported diagnostic ages up to 66 years), and late-middle-age case reports exist describing "KCS2-suggestive" features emerging over a long follow-up (PMC: [PMC9846794](https://pmc.ncbi.nlm.nih.gov/articles/PMC9846794/)).
- **GCLEB/OCS:** Prenatal onset, detectable by ultrasound in the second/third trimester; presentation at birth or shortly after.

**Progression:**
- KCS2 is generally **non-progressive to slowly evolving** in its skeletal features once established, but the endocrine (hypocalcemia control) and secondary complications (nephrocalcinosis from treatment, chronic kidney disease) can evolve over years — so "disease course" is better characterized as chronic/lifelong management of a static structural lesion with an evolving complication burden, rather than a classic progressive degenerative disease.
- OCS is **rapidly fatal**, typically within hours to months of birth (respiratory failure).

**Patterns:** No remission pattern is described (this is a structural/developmental, not relapsing-immunologic, disease); calcium homeostasis can "stabilize" with age in survivors per the Chen & Zou 2024 cohort review, but this reflects treatment optimization and possibly some catch-up parathyroid function rather than true disease remission. **Critical period:** the parathyroid/skeletal developmental window in utero and early infancy is the critical period during which FAM111A hyperactivation produces its organ-level damage; there is no evidence of a postnatal "window of opportunity" for prevention once the germline variant is present, though early recognition and calcium/PTH management is critical to prevent secondary seizure-related and nephrocalcinosis-related morbidity.

---

## 9. Inheritance and Population

**Epidemiology:** KCS2 is classified as **ultra-rare, prevalence <1:1,000,000**. Fewer than 50 KCS2 cases and fewer than 30 GCLEB/OCS cases have been published in total to date (search synthesis; malacards.org). No formal incidence/prevalence registry (e.g., GBD, national birth-defect registry) figure specific to this gene was identified — figures are literature-count-based estimates rather than population-ascertained rates, an inherent epistemic limitation for an ultra-rare Mendelian disease.

**Inheritance pattern:**
- **Autosomal dominant** (most common) — typically *de novo* (~79.5% of cases); rare vertical transmission (mother-to-daughter and father-to-daughter both documented) confirms full penetrance and absence of imprinting effects.
- **Autosomal recessive** (newly recognized, 2021–2025) — via (a) biallelic weakly-hypermorphic missense alleles (e.g., homozygous p.Tyr414Cys/Asn) or (b) biallelic hypomorphic/loss-of-function alleles (e.g., homozygous synonymous splice-altering p.Pro27=), the latter identified in a consanguineous family.
- **Penetrance:** Complete/full penetrance for dominant pathogenic missense variants (no documented non-penetrant heterozygous carriers of the classical hotspot variants); by contrast, the recessive Tyr414 variant is **fully non-penetrant in the heterozygous state** — obligate carrier relatives in both reported families are asymptomatic — which is itself an important, quantifiable genotype-phenotype/dosage finding.
- **Expressivity:** Variable — the literature documents a wide severity range even among KCS2 patients with the identical p.Arg569His hotspot variant, and Chen & Zou (2024) found **no statistically significant phenotypic difference between hotspot-variant carriers and carriers of other FAM111A variants**, suggesting expressivity is not strongly variant-position-dependent within the dominant-KCS2 range (though it clearly differs sharply between the dominant-KCS2 range and the more severely destabilizing OCS-associated variants).
- **Genetic anticipation, germline mosaicism, founder effects, consanguinity:** No genetic anticipation is reported (not a repeat-expansion disorder). No specific founder-population variant or consanguinity-linked founder effect is documented for the dominant hotspot (it is recurrent de novo, not inherited from a founder chromosome), though the recessive forms have specifically been described in **consanguineous families**, consistent with a classical recessive-disease ascertainment pattern. No mosaicism data specific to FAM111A were identified in this search.
- **Carrier frequency:** Not established/reported for recessive pathogenic alleles given the disease's ultra-rarity; not present in population databases at frequencies suggesting a common carrier state.

**Population demographics:**
- **Sex ratio:** Approximately 1:1 (no sex predominance) — literature review found 25 females : 20 males among reported KCS2 cases (ratio ~1:1.25), not statistically distinct from unity.
- **Ethnic/geographic distribution:** General search results (via malacards/secondary sources) suggested a higher reported incidence in Middle Eastern and Arabian Gulf populations — however, this may partly reflect ascertainment bias and the historical confusion with the *TBCE*-related KCS1/Sanjad-Sakati syndrome (which does have a well-established Middle Eastern/Bedouin founder-mutation epidemiology). Recent large single-country cohorts have also come from China (Chen & Zou 2024, 8 patients from 6 families), suggesting the true distribution is likely pan-ethnic with variable ascertainment.
- **Age distribution:** Bimodal in effect — neonatal/infantile presentation (hypocalcemic seizures, most common ascertainment route) versus occasional adult incidental/delayed diagnosis.

---

## 10. Diagnostics

**Laboratory tests:**
- Serum calcium (low), phosphate (may be elevated), magnesium (may be low), PTH (low/inappropriately normal for the hypocalcemia — primary hypoparathyroidism pattern; note some "atypical" cases now reported with normal PTH, per Chen & Zou 2024)
- 24-hour urinary calcium/creatinine ratio — critical for monitoring hypercalciuria risk during conventional (calcium/vitamin D) therapy (LOINC-codeable analytes)
- Growth hormone axis testing when short stature is disproportionate to calcium control (GH deficiency found in ~37.5% tested)

**Imaging:**
- Long-bone radiographs: cortical thickening + medullary stenosis (KCS2) vs. gracile/thin diaphyses (OCS) — the defining radiographic dichotomy across the disease spectrum
- Skull imaging: delayed fontanelle closure (KCS2) vs. cloverleaf/hypomineralized skull (OCS)
- Prenatal ultrasound: shortened long bones, IUGR; the first molecularly confirmed **prenatal diagnosis of OCS** was achieved via targeted whole-exome sequencing after ultrasound suggested a "serious but non-lethal" skeletal dysplasia (BMC Med Genet 2019 case report, PMC: [PMC6947839](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6947839/))
- Neuroimaging (CT/MRI): basal ganglia calcification secondary to chronic hypocalcemia (found in ~35% of cases)

**Genetic testing:**
- **Single-gene *FAM111A* sequencing or targeted skeletal-dysplasia/hypoparathyroidism gene panel** is the recommended first-tier approach given the well-defined hotspot (p.Arg569His) and clustering of variants in the SPD.
- **Whole-exome sequencing (WES)** has proven diagnostic utility, including for prenatal diagnosis and for identifying atypical/recessive presentations (e.g., the synonymous splice variant, which would likely be missed or misclassified by a naive coding-only variant filter and required RNA/splicing-level functional follow-up).
- Chromosomal microarray/karyotype/FISH are not primary diagnostic tools here (this is not a copy-number or chromosomal disorder) but may be used to exclude differentials in an undiagnosed short-stature/skeletal-dysplasia workup.

**Clinical/differential diagnosis** (critical distinguishing step):
- **Kenny-Caffey syndrome type 1 (KCS1)** and the allelic **Sanjad-Sakati syndrome**, both caused by biallelic *TBCE* variants (OMIM #244460), are autosomal **recessive** and are distinguished from FAM111A-related KCS2 by the presence of **microcephaly and intellectual disability** in KCS1/Sanjad-Sakati, which are absent (or only rarely present, ~11.6%) in classic FAM111A-KCS2. An overlapping/blended phenotype case has been reported, underscoring that clinical overlap exists and molecular confirmation is essential (PMID: [33010201](https://pubmed.ncbi.nlm.nih.gov/33010201/)).
- Other causes of isolated/syndromic hypoparathyroidism (e.g., 22q11.2 deletion syndrome, autoimmune polyglandular syndrome type 1, HDR/Barakat syndrome via *GATA3*) should be excluded in an undiagnosed hypocalcemic infant without a clear skeletal-dysplasia radiographic picture.
- Other lethal skeletal dysplasias with hypomineralized skull (e.g., osteogenesis imperfecta type II, hypophosphatasia) enter the differential for OCS on imaging alone, but splenic hypoplasia and the specific gracile-bone/cloverleaf-skull combination, plus molecular confirmation, are distinguishing.

**Screening:** No population/newborn screening program exists for this ultra-rare condition; case ascertainment is clinical (neonatal hypocalcemic seizure or dysmorphic skeletal survey) followed by confirmatory single-gene or exome sequencing. Cascade testing of relatives is warranted given documented vertical transmission of dominant alleles and the discovery of asymptomatic heterozygous carriers in recessive families.

---

## 11. Outcome/Prognosis

**Survival/mortality:**
- **KCS2:** Not classically lethal; reported patients survive into adulthood (up to 66 years at diagnosis in the literature), though long-term mortality/survival statistics (e.g., formal life-table or actuarial data) are not available given the small cohort size. Fatalities have, however, been reported among *recessive*-form family members with severe/hydropic presentations (e.g., a sibling in the Y414 kindred died at 14 months with hydrops fetalis and respiratory distress), indicating the dominant/recessive-hypermorphic spectrum blurs into life-threatening severity in some individuals.
- **GCLEB/OCS:** Essentially uniformly **perinatally lethal** — stillbirth or death within hours to months after birth from restrictive respiratory failure; "no treatment currently exists, leading to a poor prognosis."

**Morbidity/function (KCS2 survivors):**
- Chronic seizure risk (especially in early childhood, tied to labile calcium control)
- Visual impairment from marked hypermetropia
- Significant dental morbidity
- Short stature with limited response to growth hormone therapy (see §12)
- Emerging long-term renal morbidity: nephrocalcinosis and chronic kidney disease from hypercalciuric conventional (calcium + vitamin D) therapy — this is now recognized as a major long-term complication driver, motivating interest in rhPTH therapy (see §12)

**Prognostic factors:** Genotype-severity correlation is emerging but incomplete — structural destabilization modeling correlates variant position with severity (mild Y414 hypermorph → recessive KCS2/OCS spectrum; more destabilizing SPD positions like Y562S → lethal OCS), but Chen & Zou (2024) found no significant phenotype difference across dominant KCS2 variants including the p.Arg569His hotspot, so genotype is not yet a reliable individual-level prognostic tool within the dominant-KCS2 range.

**No established prognostic biomarker** beyond genotype/variant position and clinical calcium control status.

---

## 12. Treatment

There is **no curative or disease-modifying (protease-inhibitor) therapy** for FAM111A-related skeletal dysplasia at present; all management is supportive/replacement-based for KCS2, and OCS has no effective treatment (uniformly lethal).

### Pharmacotherapy
- **Conventional hypoparathyroidism therapy:** oral calcium supplements + active vitamin D metabolites (e.g., alfacalcidol, calcitriol); sodium, levothyroxine, and hydrocortisone as needed for associated multi-hormonal deficiency during physiologic stress. NCIT term: `NCIT:C15986` (Pharmacotherapy); therapeutic agents e.g. calcitriol (CHEBI), calcium carbonate (CHEBI).
- **Major limitation:** conventional therapy causes **hypercalciuria with risk of nephrocalcinosis**, and treatment-resistant/labile hypocalcemia is common, sometimes requiring chronic parenteral (IV) calcium and central venous catheterization in severe infantile cases.
- **Recombinant human parathyroid hormone (rhPTH; teriparatide)** — the **first reported use in KCS2** was published in 2025 (a Serbian case report, PMC: [PMC13025059](https://pmc.ncbi.nlm.nih.gov/articles/PMC13025059/), DOI: 10.3390/diseases14030091): a 2-month-old with a p.Ser541Pro variant, refractory to high-dose conventional therapy with recurrent seizures and sepsis risk from prolonged central venous access, was started on subcutaneous rhPTH (initial 0.54 µg/kg/24h, divided BID; maintenance 2.2 µg/24h). Over 14 months this achieved rapid calcium normalization, resolution of hypercalciuria (urinary Ca/Cr ≤0.5 mmol/mmol), discontinuation of phenobarbital and oral calcium, and successful weaning back to conventional therapy alone with no nephrocalcinosis and no further hypocalcemic episodes at 2-year follow-up. NCIT: this is a hormone-replacement pharmacotherapy (`NCIT:C15986`), therapeutic agent teriparatide (recombinant PTH 1-34).
- **Growth hormone therapy** has been tried for short stature but with **disappointing/limited efficacy** — case reports describe minimal improvement in height velocity despite adequate dosing, even in patients with confirmed GH deficiency, suggesting the growth plate defect is structurally/mechanistically resistant to GH stimulation (consistent with the underlying replication-stress/apoptosis mechanism rather than a simple GH-axis deficiency).

### Surgical/interventional
- Orthopedic management as needed for skeletal complications (NCIT: `NCIT:C16186`, Orthopedic Surgical Procedure)
- Dental restorative/extraction procedures for the substantial dental phenotype (NCIT: `NCIT:C15302`-adjacent dental care terms)
- Ophthalmologic correction (refractive correction for hypermetropia)

### Supportive/rehabilitative
- Seizure management (anticonvulsants during periods of hypocalcemia; typically can be weaned once calcium is well-controlled)
- Genetic counseling given documented dominant transmission and newly recognized recessive inheritance (NCIT: `NCIT:C15240`, Genetic Counseling)
- Multidisciplinary care (endocrinology, orthopedics, ophthalmology, dentistry, nephrology surveillance) — "coordinated effort from medical professionals belonging to different fields of expertise is required" (NORD synthesis)

### Experimental / research-stage
No registered clinical trials (ClinicalTrials.gov) specific to FAM111A-related skeletal dysplasia were identified. Given the established gain-of-function protease mechanism, a **small-molecule FAM111A protease inhibitor** is a logical future therapeutic direction, but no such agent has entered even early preclinical development based on available literature — this represents an open translational-research gap.

### Treatment outcomes
- rhPTH: single case report, favorable outcome (see above) — too preliminary for response-rate statistics.
- GH: poor/limited response documented across multiple independent case reports.
- No FDA Adverse Event (FAERS) signal specific to this ultra-rare, off-label-use population was identified.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (no modifiable risk factor); the only "primary prevention" lever is **reproductive/genetic counseling** for known carrier families (recognizing both dominant transmission risk and, in consanguineous families, recessive recurrence risk), and **prenatal diagnosis** via targeted variant testing or WES in a pregnancy with a known familial variant or with ultrasound findings suggestive of a lethal skeletal dysplasia (enabling informed reproductive decision-making, as demonstrated in the first prenatal OCS diagnosis case, PMC6947839).
- **Secondary prevention:** Early recognition of neonatal hypocalcemic seizures as a trigger for genetic workup, enabling prompt calcium/vitamin D (or rhPTH) management to prevent seizure-related morbidity.
- **Tertiary prevention:** Close monitoring of urinary calcium excretion during conventional hypoparathyroidism therapy to catch hypercalciuria before nephrocalcinosis/CKD develops — this is the specific, actionable tertiary-prevention lesson emphasized in the rhPTH case report literature.
- **Screening:** No population or newborn screening program exists (disease too rare, no biomarker suitable for universal screening); **cascade genetic testing of first-degree relatives** of a diagnosed proband is the relevant targeted-screening strategy, especially important now that asymptomatic heterozygous carriers of recessive-form alleles have been documented.
- **Immunization/public health/prophylaxis:** Not applicable — this is not an infectious or environmentally modifiable disease.

---

## 14. Other Species / Natural Disease

No naturally occurring FAM111A-associated disease in non-human animal species (companion animals, livestock, wildlife) was identified in the literature search — no OMIA (Online Mendelian Inheritance in Animals) entry or veterinary case series for a FAM111A-related skeletal dysplasia was found. This gene's disease relevance to date is human-specific in the clinical/veterinary literature reviewed; the "natural disease" comparative angle is essentially unexplored for this gene, unlike many other skeletal dysplasia genes.

*FAM111A* has clear orthologs in standard vertebrate model species (mouse *Fam111a*, used experimentally — see §15), but no report of spontaneous/natural veterinary disease.

---

## 15. Model Organisms

**Mouse (the only in vivo model identified):**
- A **Fam111a knockout (*Fam111a⁻/⁻*) C57BL/6N mouse**, reported as "the first to characterise the function of FAM111A in vivo" (Scientific Reports 2022, PMID: [35715480](https://pubmed.ncbi.nlm.nih.gov/35715480/); PMC: [PMC9205974](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9205974/)).
- **Key, somewhat counterintuitive finding: the knockout is essentially phenotypically silent** — normal body weight, normal serum PTH, unaltered serum/24h-urine magnesium, calcium, and phosphate, normal femur bone morphology/density, and normal kidney and parathyroid histology.
- **Interpretation/limitation:** This result is consistent with the human disease mechanism being a **toxic gain-of-function** (not simple loss-of-function), so a null mouse would not be expected to recapitulate a hyperactivation phenotype — meaning the knockout mouse is **not a disease model for KCS2/OCS** and instead only demonstrates that FAM111A itself is dispensable for baseline electrolyte/skeletal homeostasis in mice. The authors also raise the possibility that redundant/compensating proteases mask a phenotype in mice that would be revealed by protein-level loss in humans.
- **Consequently, there is no validated knock-in point-mutation (patient-variant) mouse model, no zebrafish, Drosophila, C. elegans, or yeast model, and no organoid/iPSC-based whole-tissue model** of FAM111A-related skeletal dysplasia identified in this search — this is a significant translational-model gap. All current mechanistic work is done in:
  - **Patient-derived dermal fibroblasts** (used to demonstrate reduced protein/aberrant splicing in the recessive hypomorphic family, and hyperactivation markers in other functional studies)
  - **Heterologous cell-line overexpression systems** (e.g., U2OS, HEK293-type systems) expressing wild-type vs. patient-mutant FAM111A to assay chromatin displacement, PCNA loading, DNA damage markers, apoptosis, and (via NanoBRET) dimerization behavior.

**Applications/limitations of current "models":**
- The knockout mouse is useful for excluding an essential-housekeeping-loss explanation and for baseline in vivo electrolyte physiology, but **cannot** be used to study the actual gain-of-function disease mechanism, model therapeutic protease-inhibition strategies, or test rhPTH/other interventions in vivo.
- **A patient-variant knock-in mouse (e.g., R569H or Y414C) would be a high-value, currently unmet model-development need** for this disease, given (a) the mechanism is now well-defined at the biochemical/structural level, (b) a monogenic gain-of-function point mutation is technically tractable to knock in, and (c) it would enable in vivo testing of hypothetical protease-inhibitor therapeutics.

**Resources:** MGI (Mouse Genome Informatics) carries the *Fam111a* gene/allele records referenced in the 2022 knockout study; no IMPC/KOMP conditional-allele-specific disease-modeling publication beyond the constitutive knockout was identified.

---

## Summary Table: Suggested Ontology Bindings for KB Curation

| Concept | Suggested term |
|---|---|
| Disease (KCS2) | MONDO (search "Kenny-Caffey syndrome type 2"); OMIM:127000 |
| Disease (GCLEB/OCS) | OMIM:602361; MedGen C1865639 |
| Gene | hgnc:24151 (FAM111A) |
| Short stature | HP:0003508 |
| Hypoparathyroidism | HP:0000829 |
| Hypocalcemia | HP:0002901 |
| Thickened long-bone cortex | HP:0002684 |
| Large/delayed fontanelle | HP:0001005 |
| Hypermetropia | HP:0000540 |
| Seizure | HP:0001250 |
| Basal ganglia calcification | HP:0002514 |
| Cloverleaf skull | HP:0002676 |
| Thin long bones | HP:0004970 |
| Splenic hypoplasia/aplasia | HP:0030068 / HP:0001743 |
| Hydrops fetalis | HP:0001789 |
| Serine-type endopeptidase activity (GO) | GO:0004252 |
| DNA replication (GO) | GO:0006260 |
| Apoptotic process (GO) | GO:0006915 |
| Parathyroid chief cell (CL) | CL:0000446 |
| Osteoblast (CL) | CL:0000062 |
| Chondrocyte (CL) | CL:0000138 |
| Growth plate cartilage (UBERON) | UBERON:0002229 |
| Parathyroid gland (UBERON) | UBERON:0001132 |
| Calcitriol (CHEBI) | CHEBI:17823 |
| Teriparatide/rhPTH pharmacotherapy (NCIT) | NCIT:C15986 (Pharmacotherapy) |
| Genetic counseling (NCIT) | NCIT:C15240 |

---

## Key Evidence Gaps (for curation flagging)

1. **No genotype-validated in vivo (mouse/other) disease model** — the existing knockout mouse does not recapitulate the human gain-of-function phenotype.
2. **No systematic QoL instrument data** (EQ-5D/SF-36/PROMIS) specific to this population.
3. **No population-based prevalence/incidence estimate** — all figures are literature case-counts, not registry-derived.
4. **Immune/infection-susceptibility mechanism remains unresolved** — some patients show clinical recurrent infection despite normal standard immune labs.
5. **No disease-modifying (protease-inhibitor) therapeutic in development** despite a well-characterized, structurally resolved catalytic mechanism — an actionable translational opportunity.
6. **Genotype-phenotype correlation is only partially established** — validated for the dominant-vs-recessive and Y414-vs-more-destabilizing-position axis, but not for fine-grained severity prediction within the dominant KCS2 hotspot group.

---

## Sources

- [FAM111A mutations result in hypoparathyroidism and impaired skeletal development (Unger et al., Am J Hum Genet 2013, PMID:23684011)](https://pubmed.ncbi.nlm.nih.gov/23684011/)
- [A recurrent de novo FAM111A mutation causes Kenny-Caffey syndrome type 2 (PMID:23996431)](https://pubmed.ncbi.nlm.nih.gov/23996431/)
- [127000 - KENNY-CAFFEY SYNDROME, TYPE 2; KCS2 - OMIM](https://omim.org/entry/127000)
- [Entry - #602361 - GRACILE BONE DYSPLASIA; GCLEB - OMIM](https://omim.org/entry/602361)
- [244460 - KENNY-CAFFEY SYNDROME, TYPE 1; KCS1 - OMIM](https://omim.org/entry/244460)
- [Orphanet: Kenny-Caffey syndrome (ORPHA2333)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Expert=2333&lng=EN)
- [Further delineation of phenotype and genotype of Kenny–Caffey syndrome type 2 (Chen & Zou, Mol Genet Genomic Med 2024, PMID:38591167)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11002637/)
- [Quantitative hypermorphic FAM111A alleles cause autosomal recessive Kenny-Caffey syndrome type 2 and osteocraniostenosis (JCI Insight 2025, PMID:39932783)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11949059/)
- [Homozygous synonymous FAM111A variant underlies an autosomal recessive form of Kenny-Caffey syndrome (J Hum Genet 2024)](https://www.nature.com/articles/s10038-024-01301-1)
- [Compound Heterozygous Variants in FAM111A Cause Autosomal Recessive Kenny-Caffey Syndrome Type 2 (PMID:34382758)](https://pubmed.ncbi.nlm.nih.gov/34382758/)
- [FAM111 protease activity undermines cellular fitness and is amplified by gain-of-function mutations in human disease (EMBO Reports 2020)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7534640/)
- [FAM111A protects replication forks from protein obstacles via its trypsin-like domain (Nature Communications 2020, PMID:32165630)](https://www.nature.com/articles/s41467-020-15170-7)
- [Dimerization-dependent serine protease activity of FAM111A prevents replication fork stalling at topoisomerase 1 cleavage complexes (Nature Communications 2024, PMID:38453899)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10920703/)
- [FAM111A regulates replication origin activation and cell fitness (Life Science Alliance 2023, PMID:37793778)](https://www.life-science-alliance.org/content/6/12/e202302111)
- [Unravelling the Intricate Roles of FAM111A and FAM111B (PMC10931937)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10931937/)
- [Functions and evolution of FAM111 serine proteases (Frontiers 2022)](https://www.frontiersin.org/journals/molecular-biosciences/articles/10.3389/fmolb.2022.1081166/full)
- [FAM111A is dispensable for electrolyte homeostasis in mice (Scientific Reports 2022, PMID:35715480)](https://www.nature.com/articles/s41598-022-14054-8)
- [First Reported Use of Recombinant Parathyroid Hormone in Kenny–Caffey Syndrome Type 2 (Diseases 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13025059/)
- [Clinical and Molecular Diagnosis of Osteocraniostenosis in Fetuses and Newborns (Genes 2022, PMID:35205306)](https://pubmed.ncbi.nlm.nih.gov/35205306/)
- [Case report: targeted whole exome sequencing enables the first prenatal diagnosis of osteocraniostenosis (BMC Med Genet 2019)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6947839/)
- [Overlapping phenotype comprising Kenny-Caffey type 2 and Sanjad-Sakati syndromes (PMID:33010201)](https://pubmed.ncbi.nlm.nih.gov/33010201/)
- [Case report: Late middle-aged features of FAM111A variant, Kenny–Caffey syndrome type 2 (PMC9846794)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9846794/)
- [Kenny-Caffey Syndrome, Type 2 - MalaCards](https://www.malacards.org/card/kenny_caffey_syndrome_type_2_2)
- [Kenny-Caffey Syndrome - NORD](https://rarediseases.org/rare-diseases/kenny-caffey-syndrome/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 25 |
| On topic | 20 |
| Off topic | 0 |

All extracted references resolved successfully.