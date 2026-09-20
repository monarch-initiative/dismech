---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-08T14:21:46.733476'
end_time: '2026-08-08T14:26:49.565591'
duration_seconds: 302.83
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Gonorrhea
  mondo_id: ''
  category: Infectious Disease
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
  web_search_requests: 18
  num_turns: 20
  total_cost_usd: 1.8713029999999997
  session_id: b20bd498-c3d4-5201-8d0b-983a970fa830
  stop_reason: end_turn
citation_count: 54
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Gonorrhea
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Gonorrhea** covering all of the
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

# Gonorrhea (*Neisseria gonorrhoeae* Infection) — Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview.** Gonorrhea is a sexually transmitted bacterial infection caused by *Neisseria gonorrhoeae*, a Gram-negative, oxidase-positive, obligate human diplococcus. It is the second most common notifiable bacterial STI globally after chlamydia. Infection most commonly involves the mucosal epithelium of the urogenital tract (urethra, endocervix), but also infects the rectum, oropharynx, and conjunctiva, and can disseminate hematogenously to cause systemic disease (disseminated gonococcal infection, DGI). Untreated infection in women is a leading preventable cause of pelvic inflammatory disease (PID), tubal infertility, and ectopic pregnancy; in neonates it causes a sight-threatening ophthalmia neonatorum. *N. gonorrhoeae* is an obligate human pathogen with no other natural reservoir (PMID:35489793 — "Neisseria gonorrhoeae physiology and pathogenesis," comprehensive review, *Adv Microb Physiol* 2022).

**Key identifiers:**
- **MONDO:** MONDO:0004277 (gonorrhea)
- **ICD-10-CM:** A54 (Gonococcal infection), with subcodes A54.0 (lower genitourinary tract, no abscess), A54.1 (with periurethral/accessory gland abscess), A54.2 (pelviperitonitis and other genitourinary), A54.3 (eye), A54.4 (musculoskeletal), A54.5 (pharynx), A54.6 (anus/rectum), A54.8 (other), A54.9 (unspecified)
- **ICD-11 (MMS):** 1A72 Gonococcal infection (with site-specific extension codes)
- **MeSH:** D006069 (Gonorrhea); organism MeSH D009349 (*Neisseria gonorrhoeae*)
- **Orphanet:** not a rare disease — no ORPHA code (common infectious STI, outside Orphanet's rare-disease scope)
- **NCBITaxon:** NCBITaxon:485 (*Neisseria gonorrhoeae*)

**Synonyms:** "the clap," gonococcal infection, GC infection, gonococcal urethritis/cervicitis, gonococcemia (for disseminated disease).

**Data provenance note:** Most quantitative claims below derive from aggregated, disease-level public-health surveillance (CDC NNDSS/STI Surveillance reports, WHO global STI estimates) and case-series/cohort literature rather than individual EHR data, consistent with an infectious disease whose primary curation sources are population surveillance and clinical microbiology literature rather than genetic registries.

---

## 2. Etiology

### Disease Causal Factor
The sole causal agent is infection with *Neisseria gonorrhoeae*. This is a purely **infectious** etiology — there is no genetic Mendelian basis for the disease itself (as distinct from host susceptibility modifiers, below). Transmission is via direct mucosal contact — genital, anorectal, or oropharyngeal sexual contact, or perinatal (mother-to-child) transmission during vaginal delivery.

### Risk Factors

**Environmental / behavioral risk factors** (PMID:35489793; CDC STI Surveillance 2024):
- Multiple or new sexual partners; unprotected (condomless) intercourse
- Age 15–24 years (highest incidence band in most surveillance systems)
- Men who have sex with men (MSM) — disproportionately high rectal/pharyngeal incidence
- Prior gonorrhea or other STI (marker of ongoing exposure risk)
- Sex work; high local community prevalence ("core group" transmission dynamics)
- Illicit drug use, incarceration history, and inconsistent healthcare access (social determinants correlated with surveillance-reported incidence, CDC 2024 STI Surveillance Report, https://www.cdc.gov/sti-statistics/annual/index.html)
- Co-infection with other STIs (chlamydia, syphilis, trichomoniasis) — shared risk-factor and mucosal-vulnerability profile

**Genetic / host susceptibility risk factors:**
- **Terminal complement pathway deficiencies** (C5, C6, C7, C8, C9 and Factor I/Factor H of the alternative pathway) markedly predispose to **disseminated** and **recurrent** neisserial infection (both meningococcal and gonococcal), because the membrane attack complex (MAC) is the principal bactericidal mechanism against *Neisseria* in blood. A 2026 case report describes disseminated gonococcal infection due to a homozygous nonsense mutation in *CFI* (Factor I; p.Arg474*) causing complete Factor I deficiency (PMID:41607490, PMC12829745). A separate case describes DGI in a man with compound-heterozygous *C7* deficiency (PMC8021336). "Deficiencies of components of the alternative and terminal complement pathways have long been implicated in increasing the risk for neisserial infections."
- **Acquired complement deficiency** (e.g., hypocomplementemic urticarial vasculitis, systemic lupus erythematosus with autoantibody-mediated complement consumption) has also been linked to extreme gonococcal susceptibility.
- **CEACAM receptor polymorphism/expression variability** on genital epithelium modulates strain-specific Opa-mediated adhesion/invasion susceptibility, though this is a variable host receptor-expression trait rather than a Mendelian risk allele (see Mechanism, §6).

**Suggested ontology terms:** HP:0005361 (Recurrent bacterial infections context — as HPO does not carry a "gonorrhea susceptibility" term per se, complement deficiency phenotypes are better captured via the causal gene); HGNC gene symbols for host modifier genes: `CFI` (hgnc:5394), `C7` (hgnc:1346), `C6` (hgnc:1339), `C8A`/`C8B`/`C8G`, `C9` (hgnc:1358), `CFH` (hgnc:4883).

### Protective Factors
- Consistent condom use (mechanical barrier to mucosal contact)
- **Meningococcal serogroup B outer-membrane-vesicle (OMV) vaccines** (4CMenB/Bexsero, and the earlier MeNZB) show cross-protective effectiveness against gonorrhea due to genomic/antigenic homology between *N. meningitidis* and *N. gonorrhoeae* — a landmark finding in STI vaccinology (see §13, Prevention).
- No known protective human genetic alleles specific to gonococcal infection have been robustly established (unlike, e.g., sickle trait for malaria); complement *sufficiency* is simply the normal protective state, not a "protective variant."

### Gene–Environment Interactions
The clearest gene–environment interaction is that an otherwise ordinary sexual exposure produces **disseminated** rather than localized infection specifically in hosts with terminal-complement-pathway lesions — i.e., the same environmental exposure (mucosal inoculation) yields a qualitatively different, more severe phenotype conditioned on host complement genotype (PMID:41607490; PMC8021336). This is the dominant, well-documented gene×environment axis for this disease; there is no evidence for polygenic susceptibility loci from GWAS at this time.

---

## 3. Phenotypes

Gonorrhea phenotypes are strongly **site-dependent** and **frequently asymptomatic**, which is itself an important epidemiological/clinical phenotype (~50% of women and up to 10% of men with urogenital infection are asymptomatic; pharyngeal and rectal infections are asymptomatic in the majority of cases; PMID:35489793 and CDC clinical guidance).

### A. Uncomplicated urogenital infection
| Phenotype | HPO suggestion | Notes |
|---|---|---|
| Urethral discharge (purulent, men) | HP:0030128 (Urethral discharge) | Onset 2–7 days post-exposure; classically profuse, yellow-green, purulent |
| Dysuria | HP:0100518 | Common in men; less prominent in women |
| Mucopurulent cervicitis / vaginal/cervical discharge | HP:0000132 (Abnormal vaginal discharge) — best available fit | Frequently subclinical in women |
| Intermenstrual bleeding | HP:0100608 | Cervicitis-associated |
| Testicular pain/epididymitis | HP:0000796 (Testicular pain) / epididymitis phenotype | Complication of male urethral infection |

### B. Extragenital/site-specific infection
| Phenotype | HPO suggestion | Notes |
|---|---|---|
| Pharyngitis / sore throat | HP:0025439 (Pharyngitis) | Usually asymptomatic; oropharyngeal reservoir important for AMR spread via commensal Neisseria recombination |
| Proctitis (anorectal discharge, pain, tenesmus) | HP:0002027 (Abdominal pain) is too broad — use free-text; SNOMED-preferred | Common in receptive anal intercourse; often asymptomatic |
| Purulent conjunctivitis | HP:0000534 (Purulent conjunctivitis) | In neonates = ophthalmia neonatorum; in adults from autoinoculation |

### C. Ascending / complicated disease
| Phenotype | HPO suggestion | Notes |
|---|---|---|
| Pelvic inflammatory disease (salpingitis) | HP:0030014 (Pelvic inflammatory disease) if available, else free text | ~10–15% of untreated women; N. gonorrhoeae accounts for roughly a third of PID cases (Illinois DPH; PMID:23007248) |
| Tubo-ovarian abscess | — | Severe PID sequela |
| Chronic pelvic pain | HP:0030832 or free text | Long-term PID sequela |
| Tubal factor infertility | HP:0000789 (Infertility) | Result of tubal scarring/occlusion following salpingitis |
| Ectopic pregnancy | HP:0010935 (Ectopic pregnancy) | Life-threatening PID sequela |
| Fitz-Hugh-Curtis syndrome (perihepatitis) | — (right-upper-quadrant pain phenotype; "violin-string" adhesions between liver capsule and peritoneum) | Extragenital spread of PID; PMID:6769152, PMC5755950 |
| Epididymitis / prostatitis (men) | — | Ascending male infection |

### D. Disseminated gonococcal infection (DGI) — hematogenous spread (~0.5–3% of untreated infections)
Two classical clinical patterns (PMC11368578, PMC12701954):
1. **Triad form:** fever, dermatitis (pustular/vesiculopustular skin lesions on an erythematous base, typically acral), migratory polyarthralgia, and tenosynovitis (asymmetric, affecting wrists/fingers/knees/ankles)
2. **Purulent monoarticular/oligoarticular septic arthritis** — abrupt-onset asymmetric joint pain/swelling, often afebrile
- Rare but severe: endocarditis, meningitis, osteomyelitis (PMC9602952 — gonococcal meningitis)
- Strains from disseminated sites are disproportionately of the **transparent (Opa-low)** phenotype (90% in classic series), reflecting serum-resistance/immune-evasion phenotype selection for bloodstream survival

Suggested HP terms: HP:0001945 (Fever), HP:0100546 (Arthralgia), HP:0001369 (Arthritis), HP:0001386 (Joint swelling), HP:0100678 (Skin nodule)/pustular rash, HP:0100033 (Osteomyelitis), HP:0001297 (Stroke) N/A, HP:0001298 (Encephalopathy)/meningitis-related terms, HP:0030842 (Infective endocarditis).

### E. Neonatal
| Phenotype | Notes |
|---|---|
| Gonococcal ophthalmia neonatorum | Onset within first 5 days of life; marked bilateral purulent conjunctival discharge; historically a leading cause of infantile blindness before universal prophylaxis (PMID:8771523; NBK537599; NBK551572) |

### Quality of life impact
Asymptomatic and untreated infection drives ongoing transmission; symptomatic disease causes acute discomfort (dysuria, discharge, pelvic pain) and — critically — the downstream PID/infertility/ectopic pregnancy sequelae carry major reproductive-health and psychosocial quality-of-life burden in women of reproductive age. DGI-associated arthritis causes acute functional disability. No disease-specific validated QoL instrument was identified; general STI-related psychosocial burden is documented in the PID and infertility literature (PMID:12346974 — immunopathogenesis of PID and infertility).

---

## 4. Genetic/Molecular Information

Gonorrhea is **not a human Mendelian disease** — there is no human causal gene. The relevant "genetics" for this KB entry falls into two categories:

### A. Host modifier/susceptibility genes (see §2)
- `CFI` (Complement Factor I, hgnc:5394) — homozygous loss-of-function → complete Factor I deficiency → extreme susceptibility to disseminated/recurrent neisserial infection (PMID:41607490)
- `C7` (hgnc:1346), `C6`, `C8A/C8B/C8G`, `C9` — terminal complement component deficiencies → impaired membrane attack complex formation → recurrent/disseminated neisserial disease (PMC8021336)
- `CFH` — alternative pathway regulator; acquired/functional deficiency states similarly predispose

Relationship type for genetic annotation: `MODIFIER`/`SUSCEPTIBILITY` (not `CAUSAL`), since these genes govern severity/dissemination of an exogenous infection rather than causing the disease de novo.

### B. Pathogen (bacterial) genetics — antimicrobial resistance determinants
These are not human genes but are central to modern gonorrhea molecular epidemiology and directly determine treatment mechanism/failure:

| Gene | Resistance phenotype | Mechanism |
|---|---|---|
| **penA** (mosaic alleles, e.g., penA-237.001, penA-60.001) | Reduced susceptibility / resistance to extended-spectrum cephalosporins (cefixime, ceftriaxone) | Altered penicillin-binding protein 2 (PBP2) reduces β-lactam binding affinity (PMC9808317 — novel mosaic penA-237.001 causing ceftriaxone-resistant, multidrug-resistant *N. gonorrhoeae*, France 2022) |
| **mtrR** (promoter/coding mutations, mosaic mtrR-mtrCDE from *N. meningitidis*/*N. lactamica*) | Increased efflux → macrolide (azithromycin) and other multidrug resistance | Derepresses/upregulates the MtrC-MtrD-MtrE multidrug efflux pump (PMC6134098, PMC6083905 — Wadsworth et al., *mBio* 2018, PMID for related work; epistasis between mtrR and mosaic mtrD required for full azithromycin resistance) |
| **ponA** (P.A517G) | Contributes to penicillin/cephalosporin resistance | Altered PBP1 |
| **porB1b** (penB) | Reduced outer-membrane permeability | Porin mutation reduces antibiotic influx |
| **gyrA** (S91F and related QRDR mutations) | Fluoroquinolone (ciprofloxacin) resistance | Altered DNA gyrase target; wild-type gyrA S91 used as a molecular susceptibility screen |
| **parC** | Fluoroquinolone resistance (secondary target) | Altered topoisomerase IV |
| **23S rRNA** (A2059G, C2611T) | High-level azithromycin resistance | Ribosomal target alteration |

(PMC5628311 — comprehensive review "Antimicrobial resistance in Neisseria gonorrhoeae: history, molecular mechanisms and epidemiological aspects of an emerging global threat"; PMC9045316 — reliability of genetic markers for predicting ceftriaxone resistance globally.) The WHO in November 2021 flagged emerging ceftriaxone resistance/treatment-failure strains as a global AMR priority.

### C. Epigenetic / chromosomal
No disease-relevant human epigenetic or chromosomal-abnormality literature applies (not a genetic disease). *N. gonorrhoeae* itself undergoes extensive **phase and antigenic variation** (Opa gene slipped-strand mispairing, pilin antigenic variation via recombination with silent pilS loci) — a bacterial "epigenetic-like" mechanism of immune evasion, distinct from human epigenetics (PMID:35489793).

**Suggested ontology terms:** GO:0046677 (response to antibiotic), GO:0015562 (efflux transmembrane transporter activity) for MtrCDE; CHEBI terms for antibiotics (§12).

---

## 5. Environmental Information

- **Infectious agent (primary etiology):** *Neisseria gonorrhoeae*, NCBITaxon:485; Gram-negative diplococcus, family Neisseriaceae. Obligate human pathogen, no environmental or animal reservoir; transmitted exclusively via direct mucosal contact (sexual or perinatal).
- **Behavioral/lifestyle factors:** unprotected sexual contact, multiple partners, sex work, substance use in sexual contexts (see §2 Risk Factors) — CDC/WHO surveillance sources.
- **No chemical/toxin/occupational environmental etiology** applies; this is purely a sexually/perinatally transmitted bacterial infection.
- **Co-circulating pathogen environment:** commensal *Neisseria* species (*N. lactamica*, *N. cinerea*, *N. meningitidis*, *N. polysaccharea*) in the oropharynx serve as a genetic reservoir for horizontal transfer of resistance determinants (mosaic mtr, penA alleles) into *N. gonorrhoeae* — the oropharynx is thus an important "environmental" site for AMR emergence (PMC6134098).

**Suggested ontology terms:** ECTO term for "exposure to sexually transmitted infectious agent" (no highly specific ECTO term for STI contact currently cataloged — would need OAK lookup); NCBITaxon:485 for the organism.

---

## 6. Mechanism / Pathophysiology

### Causal chain overview
**Mucosal exposure → colonization/adherence → epithelial invasion & transcytosis → local inflammatory response (neutrophil influx) → tissue damage / discharge → (if untreated) ascending/hematogenous spread → PID/DGI sequelae.**

### 6.1 Colonization and adherence (initiating step)
- **Type IV pili (Tfp)** mediate initial long-range attachment to mucosal epithelium and microcolony formation; pilin (PilE) undergoes high-frequency antigenic variation via recombination with silent *pilS* loci, and pilus retraction generates twitching motility (PMID:35489793).
- **Opacity-associated (Opa) proteins** — up to 11 phase-variable paralogs — mediate tighter adhesion and, when engaged with host **CEACAM family receptors (CEACAM1, CEACAM3, CEA/CEACAM5, CEACAM6)**, promote receptor-mediated **invasion/transcytosis** of epithelial cells (PMID:21204865 — Opa proteins and CEACAMs review, *FEMS Microbiol Rev*). Differential CEACAM expression along the female reproductive tract determines the outcome (colonization vs. invasion vs. clearance) of infection at different anatomic sites (journals.asm.org/iai.00092-18). Notably, CEACAM engagement is not strictly required — Opa+ gonococci can adhere to/invade genital epithelial cells via heparan sulfate proteoglycans (HSPG) independent of CEACAM (PMID:11580753).
- **Porin (PorB)** also contributes to adherence and, upon translocation into host mitochondrial and plasma membranes, modulates host-cell apoptosis and calcium flux.

### 6.2 Immune evasion (central pathogenic strategy)
- **Lipooligosaccharide (LOS) sialylation**, using host-derived CMP-NANA, masks LOS and blocks classical/alternative complement pathway activation and opsonophagocytic killing — a major serum-resistance mechanism.
- **Anti-phagocytic mechanisms** allow intracellular survival within neutrophils via direct interference with the oxidative burst (NADPH oxidase assembly) and delayed phagolysosome maturation, permitting the organism to persist within — rather than be cleared by — the very cells recruited to fight it (PMC4154863 — "Global Analysis of Neutrophil Responses to *Neisseria gonorrhoeae* Reveals a Self-Propagating Inflammatory Program").
- **Antigenic and phase variation** (Opa, pilin, LOS) generates within-host antigenic diversity that impedes adaptive immune clearance and explains the striking absence of protective natural immunity/reinfection resistance.
- **Macrophage polarization to an M2 (anti-inflammatory/less microbicidal) phenotype** by gonococcal infection has been demonstrated as an additional subversion strategy (PMC4488386).

### 6.3 Inflammatory tissue damage (downstream of colonization)
- Rather than direct cytotoxicity, gonococcal pathology is substantially **immunopathological**: sustained **neutrophil influx** that fails to clear the organism instead releases antimicrobial products (reactive oxygen species, proteases, defensins) that damage host mucosa — producing the purulent discharge that is the clinical hallmark of infection (PMID:35489793, PMC4154863).
- In the fallopian tube, **IL-17C** has been identified as a driver of damaging inflammation during ex vivo *N. gonorrhoeae* infection of human Fallopian tube explants, contributing to ciliated-cell sloughing, epithelial exfoliation, tubal scarring, and eventual occlusion (Nature Communications 2024, DOI:10.1038/s41467-024-48141-3; PMC11069574).
- Progressive fallopian tube damage → **PID → chronic pelvic pain, tubal-factor infertility, ectopic pregnancy** (immunopathogenesis reviewed PMID:12346974).

### 6.4 Dissemination (hematogenous spread → DGI)
- Strains with the **transparent (Opa-low) phenotype** and LOS sialylation/serum-resistance are preferentially recovered from blood/synovial fluid in DGI, reflecting selection for bloodstream survival over epithelial adherence.
- Host **terminal complement pathway deficiency** removes the primary bactericidal barrier to bacteremia, explaining recurrent/disseminated presentations in affected individuals (§2, §4).
- Disseminated organisms seed skin (pustular dermatitis), joints/tendon sheaths (septic arthritis/tenosynovitis), and rarely heart valves, meninges, or bone.

### Cell types and processes involved
- **Cell types:** genital/cervical/urethral/rectal/pharyngeal/conjunctival columnar and stratified epithelial cells (site-specific tropism), neutrophils (CL:0000775), macrophages (CL:0000235), fallopian tube ciliated epithelial cells (CL:1000272 or similar), synoviocytes (DGI arthritis).
- **Suggested GO biological process terms:** GO:0007155 (cell adhesion), GO:0044409 (entry into host), GO:0052255 (modulation by symbiont of host innate immune response), GO:0006956 (complement activation) — as a target of evasion, GO:0002532 (production of molecular mediator involved in inflammatory response), GO:0043312 (neutrophil degranulation).
- **Suggested UBERON terms:** UBERON:0000056 (ureter — n/a), UBERON:0000057 (urethra), UBERON:0000995 (uterine cervix), UBERON:0003889 (fallopian tube), UBERON:0004908 (oropharynx), UBERON:0001358 (cerebrospinal fluid — meningitis), UBERON:0002370 (thymus — n/a); UBERON:0000966 (retina — n/a) — more precisely UBERON:0001759 (conjunctiva) for ophthalmia neonatorum, UBERON:0001474 (bone element) for osteomyelitis, UBERON:0000982 (synovial fluid)/UBERON:0001466 (synovial joint) for DGI arthritis.
- **Suggested CHEBI terms (host/pathogen molecules):** CHEBI:24433 (lipooligosaccharide — approximate; LOS is not a single well-defined CHEBI entity but relevant chemical class), CHEBI for sialic acid (CHEBI:26667, N-acetylneuraminic acid).

---

## 7. Anatomical Structures Affected

**Organ/system level:**
- Primary: male and female lower genitourinary tract (urethra, endocervix, Skene's/Bartholin's glands), rectum, pharynx, conjunctiva
- Secondary (ascending/complications): fallopian tubes, ovaries, peritoneum (pelviperitonitis), epididymis, prostate, liver capsule (Fitz-Hugh-Curtis)
- Disseminated: skin, synovial joints/tendon sheaths, heart valves (rare endocarditis), meninges (rare meningitis), bone (rare osteomyelitis)
- Body systems: reproductive system, integumentary system, musculoskeletal system, ocular system, and rarely cardiovascular and central nervous systems

**Tissue/cell level:** columnar/transitional epithelium (urethra, endocervix, rectum), stratified squamous epithelium (vagina — relatively resistant to colonization compared to columnar epithelium sites), ciliated fallopian tube epithelium, synovium, conjunctival epithelium.

**Subcellular level:** phagosome/phagolysosome (site of intracellular neutrophil survival), plasma membrane and mitochondrial membrane (PorB translocation), outer membrane (LOS/Opa/pilin expression).

**Suggested UBERON terms:** UBERON:0000057 (urethra), UBERON:0000995 (uterine cervix), UBERON:0003889 (fallopian tube/oviduct), UBERON:0001350 (coelomic cavity/peritoneum — approx UBERON:0002358 for peritoneal cavity), UBERON:0004908 (oropharynx), UBERON:0001759 (conjunctiva), UBERON:0001466 (synovial joint), UBERON:0002107 (liver — Fitz-Hugh-Curtis), UBERON:0001474 (bone element).

---

## 8. Temporal Development

**Onset:**
- Incubation period: typically **2–7 days** post-exposure for symptomatic urethral infection in men (classic range); cervical/rectal/pharyngeal infection incubation is less well defined and often clinically silent.
- Onset pattern: acute for symptomatic urogenital disease; frequently **asymptomatic/subclinical** at cervical, rectal, and pharyngeal sites, which is itself the key epidemiologic driver of ongoing transmission.
- Neonatal ophthalmia neonatorum: onset within the **first 5 days of life**, reflecting intrapartum exposure timing.

**Progression:**
- Untreated urogenital infection may **spontaneously clear** over weeks-to-months in a fraction of cases, but a substantial proportion progresses to ascending infection.
- **PID typically develops days to weeks** after untreated cervical infection; roughly **10–15%** of women with untreated gonorrhea (or chlamydia) develop PID.
- **DGI** develops in an estimated **0.5–3%** of untreated gonococcal infections, usually within days to a few weeks of the primary mucosal infection, and can present acutely (arthritis-dermatitis syndrome, days) or with the purulent-arthritis pattern.
- Disease course is **not chronic/progressive** in the classic autoimmune-disease sense; it is an acute-to-subacute bacterial infection whose "chronicity" manifests as (a) persistent untreated colonization enabling transmission and (b) fibrotic/scarring sequelae (tubal occlusion, adhesions) that are permanent once established, even after microbiological cure.

**Patterns:**
- No spontaneous remission-relapse pattern in the classic sense; recurrence is virtually always **reinfection** from an untreated/new partner rather than true relapse, given lack of durable protective immunity and high antigenic variability.
- **Critical intervention window:** early antibiotic treatment before ascending spread prevents essentially all PID/tubal-damage sequelae — this is the central rationale for STI screening programs.

---

## 9. Inheritance and Population

**Not a genetically inherited disease** — inheritance-pattern fields (AD/AR/X-linked, penetrance, expressivity, anticipation, founder effects, consanguinity, carrier frequency) are **not applicable** to gonorrhea itself. (They would be applicable only to the rare host complement-deficiency modifier genes noted in §2/§4, which follow autosomal recessive inheritance for the classic terminal-complement-component deficiencies.)

**Epidemiology:**
- **Global incidence (WHO, 2020 estimate):** approximately **82.4 million new infections** among adults aged 15–49 worldwide in 2020 (WHO fact sheet, https://www.who.int/news-room/fact-sheets/detail/gonorrhoea-(neisseria-gonorrhoeae-infection); WHO Nov 2021 AMR surveillance report). It is the second most common bacterial STI after chlamydia.
- **United States (CDC 2024 provisional surveillance):** Gonorrhea cases declined for a third consecutive year, down ~10% from 2023; combined chlamydia/gonorrhea/syphilis cases fell 9% from 2023. However, total 2024 U.S. STIs (all types) still exceeded **2.2 million reported cases**, and overall STI burden remains **13% higher** than a decade prior (CDC 2024 STI Surveillance report, https://www.cdc.gov/sti-statistics/annual/index.html; https://www.hiv.gov/blog/cdc-releases-2024-national-sti-data).
- Possible contributor to the recent U.S. decline: expanded **meningococcal B vaccine** use in college-age/high-risk adults, given documented cross-protection against gonorrhea (see §13).
- **Disseminated gonococcal infection (DGI)** surveillance in the U.S., 2020–2022 (PMC9751791, "Mind the Clap").

**Population demographics:**
- **Age distribution:** highest incidence in **15–24-year-olds**, reflecting sexual-activity patterns and behavioral/biological (cervical ectopy) susceptibility in young women.
- **Sex/behavioral group distribution:** disproportionately high burden among **men who have sex with men (MSM)**, particularly for rectal and pharyngeal infection; also elevated among sex workers, transgender women, and adolescents/young adults in high-burden settings (WHO fact sheet).
- **Geographic distribution:** globally endemic, with the highest burden in the WHO African and Western Pacific regions per global estimates; substantial regional variation in antimicrobial-resistance prevalence — e.g., high tetracycline resistance prevalence across 22 European countries in 2024 surveillance (PMC12811707).
- Racial/ethnic and state-level U.S. breakdowns for 2024 were **not yet released** by CDC at time of the 2024 provisional report due to ongoing surveillance-system updates (Healthbeat, https://www.healthbeat.org/2025/10/07/sti-chlamydia-gonorrhea-syphilis-cdc-data/).

**Suggested ontology term:** NCBITaxon:9606 (Homo sapiens, sole natural host).

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Nucleic acid amplification testing (NAAT)** is the current diagnostic standard of care — highly sensitive and specific for genital specimens (urine, urethral/endocervical/vaginal swabs), and validated for extragenital (rectal, oropharyngeal) specimens where it substantially outperforms culture (PMID:20335410; PMID:18520976; PMC1871692 "Nucleic Acid Amplification Testing for Neisseria gonorrhoeae: An Ongoing Challenge"; PMC8769746 multicenter NAAT comparison for rectal/oropharyngeal specimens). Commercial platforms include Gen-Probe APTIMA COMBO 2/APTIMA GC, Roche COBAS Amplicor/4800 CT/NG, BD ProbeTec, Abbott RealTime CT/NG (PMC3187337).
  - **Important caveat:** false-positive NAAT results can occur due to horizontal genetic exchange between *N. gonorrhoeae* and commensal *Neisseria* species sharing amplified target sequences — an important diagnostic-interpretation caveat, especially at pharyngeal sites.
- **Culture** (Thayer-Martin or modified selective media) remains essential for **antimicrobial susceptibility testing** and outbreak/AMR surveillance, despite lower sensitivity than NAAT, particularly for extragenital sites.
- **Gram stain** of urethral discharge in symptomatic men (intracellular Gram-negative diplococci within neutrophils) remains a rapid point-of-care diagnostic with high sensitivity/specificity in that specific clinical context, though far less reliable for cervical, rectal, or pharyngeal specimens.
- **Molecular AMR prediction:** genotypic assays targeting gyrA (ciprofloxacin susceptibility screening via detection of wild-type S91), and increasingly whole-genome-sequencing-based prediction of penA/mtrR/23S rRNA resistance markers, though reliability of genotype-based ceftriaxone-resistance prediction remains imperfect globally (PMC9045316).

**Genetic testing:** Not applicable in the human-genetics sense (no causal human gene); pathogen molecular typing (NG-MAST, NG-STAR, whole-genome sequencing) is used for surveillance and AMR-marker detection rather than "genetic testing" of the patient.

**Omics-based diagnostics:** Whole-genome sequencing of clinical isolates is increasingly used for AMR surveillance and outbreak/transmission-cluster tracking (PMC8442004, "Recent advances in understanding and combatting Neisseria gonorrhoeae: a genomic perspective") — this is pathogen genomics, not host omics.

**Clinical criteria / differential diagnosis:** Urethritis/cervicitis differential includes *Chlamydia trachomatis* (frequent co-infection — CDC recommends empiric doxycycline co-treatment when chlamydia is not excluded), *Mycoplasma genitalium*, *Trichomonas vaginalis*, and non-infectious urethritis/cervicitis. DGI arthritis-dermatitis syndrome differential includes reactive arthritis, viral exanthem-associated arthritis, and other causes of septic arthritis.

**Screening:** CDC/USPSTF recommend annual gonorrhea (and chlamydia) screening for sexually active women <25 years and older women with risk factors, and for MSM at exposed anatomic sites (urogenital, rectal, pharyngeal) at least annually (more frequently for high-risk individuals). **Universal ocular prophylaxis at birth** (erythromycin ointment historically; topical agents per current guidance) remains recommended in the U.S. for prevention of ophthalmia neonatorum (NBK537599 — USPSTF reaffirmation evidence review).

**Suggested LOINC/ontology:** LOINC panels exist for *N. gonorrhoeae* NAAT (e.g., LOINC:43304-5 and site-specific variants); SNOMED CT for clinical/pathology findings.

---

## 11. Outcome/Prognosis

- **Mortality:** Direct mortality from uncomplicated gonorrhea is essentially **negligible** with treatment; mortality is confined to rare severe DGI complications (endocarditis, meningitis) and to indirect mortality via **ectopic pregnancy**, which remains a life-threatening PID sequela.
- **Morbidity:** The dominant morbidity burden is **reproductive**: an estimated **10–15%** of women with untreated gonorrhea/chlamydia develop PID; PID prevalence among reproductive-age U.S. women is estimated at **4.1%**, with *N. gonorrhoeae* implicated in roughly a third of cases (Illinois DPH; PMID:23007248). PID sequelae include chronic pelvic pain, tubal-factor infertility, and ectopic pregnancy.
- **Recovery potential:** With prompt, effective antibiotic treatment, uncomplicated mucosal infection resolves completely with no long-term sequelae. Once tubal scarring/occlusion has occurred, however, infertility and elevated ectopic-pregnancy risk are **not reversible** by subsequent antibiotic treatment — underscoring the importance of early detection given the high asymptomatic-carriage rate.
- **DGI outcomes:** With appropriate IV/IM antibiotic therapy, DGI arthritis-dermatitis syndrome and septic arthritis generally resolve without permanent joint damage if treated promptly; delayed treatment risks joint destruction from septic arthritis and, rarely, endocarditis/meningitis-related mortality/morbidity.
- **Prognostic factors:** delay to treatment (strongest driver of PID/tubal-damage risk), host complement status (drives DGI risk), and infecting strain's antimicrobial susceptibility profile (treatment-failure risk with resistant strains is an emerging and consequential prognostic factor per WHO AMR surveillance, 2021).
- **HIV interaction:** gonococcal (especially rectal) co-infection is independently associated with substantially **increased HIV acquisition and transmission risk** — a 2–5-fold increase in susceptibility attributed to mucosal epithelial damage and increased local HIV target-cell recruitment/viral shedding (PMC5779692 — *N. gonorrhoeae* co-infection exacerbates vaginal HIV shedding in a humanized mouse model; academic.oup.com/ofid — repeated rectal gonorrhea independently associated with incident HIV infection risk in MSM). This materially worsens long-term prognosis in co-infected populations by amplifying HIV epidemic spread.

---

## 12. Treatment

**Current first-line pharmacotherapy (CDC 2021 STI Treatment Guidelines, updated 2020 recommendations; PMID:35416971, academic.oup.com/cid supplement):**
- **Ceftriaxone 500 mg IM single dose** (uncomplicated infection of any anatomic site — genital, rectal, pharyngeal) — increased to **1 g IM** for patients weighing ≥150 kg (300 lb).
- This replaced the prior dual-therapy regimen of ceftriaxone 250 mg IM + azithromycin 1 g PO, reflecting rising **azithromycin resistance** concerns and evidence that single-agent ceftriaxone is highly effective, reducing selective pressure for macrolide resistance.
- **Co-treatment for chlamydia:** if chlamydial co-infection has not been excluded, add **doxycycline 100 mg PO BID × 7 days**.
- **Cephalosporin-allergic patients:** limited alternatives exist; **no recommended alternative regimen for pharyngeal infection** specifically, reflecting the therapeutic difficulty of that site; oral **cefixime 800 mg single dose** may be used for expedited partner therapy (EPT) when injectable ceftriaxone is not feasible, though it is not preferred given lower efficacy at some anatomic sites and resistance concerns.
- **DGI (disseminated disease):** requires initial **parenteral ceftriaxone** (typically 1 g IV/IM daily) for a longer course, often transitioning to oral therapy after clinical improvement, per site-specific severity (arthritis, meningitis, endocarditis regimens differ in duration/dose).
- **Ophthalmia neonatorum:** ceftriaxone (single IM/IV dose, weight-based) plus saline eye irrigation; prevention via universal neonatal ocular prophylaxis remains standard of care.

**Pharmacogenomics:** No clinically significant host pharmacogenomic determinants of gonorrhea drug response have been established (unlike, e.g., HLA-linked hypersensitivity syndromes for other drugs); the dominant "resistance genomics" concern is **pathogen** genotype (§4/§9), not host genotype.

**Advanced/experimental therapeutics:** No gene therapy, cell therapy, RNA-based therapy, or targeted/immunotherapy applies to this bacterial infection; management is exclusively antimicrobial.

**Surgical/interventional:** Reserved for complications — e.g., drainage of tubo-ovarian abscess, arthrocentesis/surgical debridement for severe septic arthritis, laparoscopy for Fitz-Hugh-Curtis adhesion lysis/diagnosis.

**Supportive care:** symptomatic management of pain/discharge; partner notification and treatment (expedited partner therapy, EPT) is a core component of clinical management to prevent reinfection and interrupt transmission chains.

**Treatment outcomes / resistance concerns:** The central emerging treatment-outcome issue is **antimicrobial resistance**, with documented multidrug-resistant and ceftriaxone-resistant strains (mosaic *penA* alleles) reported globally, including in France (2022, PMC9808317) and elsewhere, prompting WHO to designate gonococcal AMR a global health priority (WHO, Nov 2021) and driving intensified interest in non-antibiotic prevention strategies (vaccines, see §13).

**Suggested NCIT terms:**
- `NCIT:C15986` (Pharmacotherapy) — generic action for the antibiotic regimens
- `NCIT:C15632` (Chemotherapy) — not applicable here (antibacterial, not chemo)
- Therapeutic agents (CHEBI): ceftriaxone (CHEBI:3508), azithromycin (CHEBI:2955), doxycycline (CHEBI:50845), cefixime (CHEBI:475130), ciprofloxacin (CHEBI:100241) — verify exact CHEBI IDs via OAK lookup before curation.
- `NCIT:C15329` (Surgical Procedure) for abscess drainage/laparoscopy in complicated PID.

---

## 13. Prevention

**Primary prevention:**
- **Barrier contraception** (consistent, correct condom use) remains the principal behavioral primary-prevention measure.
- **Behavioral risk-reduction counseling** and partner-reduction strategies (CDC/WHO public health guidance).
- **Vaccination (major recent development):** **Meningococcal serogroup B outer-membrane-vesicle (OMV) vaccines** — 4CMenB (Bexsero) and the earlier New Zealand MeNZB — demonstrate significant **cross-protective effectiveness against gonorrhea**, attributed to antigenic homology between *N. meningitidis* and *N. gonorrhoeae* OMV components:
  - 4CMenB induces cross-species protection against *N. gonorrhoeae* in preclinical models (PMC7748408/PMID:32218555, *npj Vaccines*).
  - A matched cohort study in Southern California found real-world protective effectiveness (PMID:35642527).
  - Multiple 2025 systematic reviews/meta-analyses confirm statistically significant reductions in gonorrhea incidence among OMV-MenB vaccine recipients versus unvaccinated or non-OMV-vaccinated comparators, with effectiveness estimates in the range of **23–46%**, and one case-control estimate (using chlamydia as a negative control) of **~31%** (PMID:40334533; academic.oup.com/jid/article/231/1/61; PMID:38986746).
  - **Policy uptake:** in **August 2025, the UK Health Security Agency approved 4CMenB use specifically to prevent gonorrhea** in high-risk populations, including individuals with repeat infections and MSM — the first national policy explicitly using a meningococcal vaccine for gonorrhea prevention.
  - **Purpose-built gonococcal vaccines** are in active development: GSK's investigational *N. gonorrhoeae* GMMA (Generalized Modules for Membrane Antigens) vaccine is in a Phase 1/2 clinical trial (NCT05630859); preclinical native-OMV candidate vaccines engineered from gonococcal strains (with *lpxL1*/*rmp* deletions to reduce reactogenicity) show promise compared to 4CMenB in animal models (npj Vaccines 2026, PMID:42259835). WHO identified gonorrhea vaccine development as a **global priority in 2024**, driven by rising antimicrobial resistance.
  - **Caveat:** breakthrough rectal *N. gonorrhoeae* infections after meningococcal B vaccination have been reported, underscoring that current cross-protection is partial, not sterilizing (academic.oup.com/ofid/article/11/11/ofae562).

**Secondary prevention (screening/early detection):**
- Routine annual NAAT-based screening of sexually active women <25 and higher-risk older women, and of MSM at all exposed anatomic sites (§10).
- **Universal neonatal ocular prophylaxis** at birth remains a longstanding, evidence-supported secondary/primary prevention measure against ophthalmia neonatorum (USPSTF reaffirmation, NBK537599).

**Tertiary prevention:** Prompt treatment of diagnosed infection and of PID specifically to minimize progression to tubal damage/infertility/ectopic pregnancy; partner treatment (EPT) to prevent reinfection cycles.

**Public health interventions:** Partner notification/contact tracing programs, expedited partner therapy (EPT) policies, community-based STI testing outreach in high-prevalence "core group" populations, and enhanced AMR surveillance (WHO Gonococcal Antimicrobial Surveillance Programme, GASP) to guide empiric treatment recommendations as resistance patterns shift regionally.

**Prophylaxis:** No pre-exposure chemoprophylaxis is currently recommended for gonorrhea specifically (in contrast to doxycycline post-exposure prophylaxis, "doxy-PEP," which is increasingly used for chlamydia/syphilis prevention in high-risk MSM populations but has shown limited/inconsistent efficacy specifically against gonorrhea due to existing tetracycline-class resistance).

---

## 14. Other Species / Natural Disease

*N. gonorrhoeae* is a **strict human-obligate pathogen** with **no natural non-human reservoir or naturally occurring disease in animals**. This is a defining biological feature of the organism (unlike, e.g., zoonotic pathogens).
- **Taxonomy:** NCBITaxon:485 (*Neisseria gonorrhoeae*); genus Neisseria (NCBITaxon:482) includes related pathogenic species *N. meningitidis* (NCBITaxon:487) and commensal species (*N. lactamica*, NCBITaxon:489; *N. cinerea*; *N. polysaccharea*) that participate in horizontal AMR gene transfer (§4, §5).
- **No breed-specific (VBO) relevance** — not an animal disease.
- **No natural veterinary disease** is recognized; *N. gonorrhoeae* does not naturally infect animals, so there is no OMIA entry or veterinary comparative-pathology literature analogous to a zoonosis.
- **Zoonotic potential:** none — transmission is exclusively human-to-human (sexual or perinatal).

---

## 15. Model Organisms

Because *N. gonorrhoeae* is a strict human pathogen, animal models require special adaptation and none fully recapitulates human disease; each has defined utility and limitations.

**Female mouse model (the dominant experimental system):**
- Wild-type mice are naturally **resistant** to gonococcal genital colonization (PMID:2506350, "Resistance of mice to genital infection with Neisseria gonorrhoeae").
- **Estradiol-treated female mice** serve as surrogate hosts: exogenous 17β-estradiol treatment (which thins the vaginal epithelium toward a more human-cervix-like columnar-favorable state and suppresses normal murine flora) permits reproducible lower-genital-tract colonization that recapitulates many features of human infection, including innate immune responses and gonococcal genetic requirements for in vivo fitness (PMID:21747807, "Estradiol-Treated Female Mice as Surrogate Hosts for Neisseria gonorrhoeae Genital Tract Infections," *Front Microbiol* 2011; developed principally by the Jerse laboratory, Uniformed Services University).
- This model has been used extensively for antimicrobial efficacy testing (e.g., auranofin efficacy against gonococcal genital infection, PMC9022871) and for vaccine preclinical efficacy testing (e.g., OMV candidate vaccine vs. 4CMenB comparison, npj Vaccines 2026).
- **Limitations:** requires exogenous hormone manipulation (not physiologic estrus), does not reproduce upper-tract ascension/PID or DGI pathology, and murine complement/CEACAM/receptor biology differs from human, limiting some immune-evasion and adhesion-mechanism studies to in vitro human-cell systems.
- Review: PMID:28886683, "Neisseria gonorrhoeae: Drug Resistance, Mouse Models, and Vaccine Development," *Annu Rev Microbiol* 2017.

**Other model systems:**
- **Human ex vivo Fallopian tube organ culture** — used to directly study PID-relevant tubal damage mechanisms (e.g., the IL-17C inflammatory-damage studies, PMC11069574/PMC (bioRxiv) 2022) — arguably the most human-fidelity model for upper-tract pathology, since no rodent naturally recapitulates fallopian tube disease.
- **Human cell-line/primary epithelial cell culture** (cervical, urethral epithelial lines; polarized epithelial monolayers) — used extensively for adhesion/invasion/Opa-CEACAM mechanism studies (§6).
- **Humanized (CD34+ engrafted) mouse models** — used specifically to study *N. gonorrhoeae*–HIV co-infection interactions in a system with human immune cells, demonstrating exacerbated vaginal HIV shedding during gonococcal co-infection (PMC5779692).
- **Zebrafish, Drosophila, C. elegans, yeast:** no established gonorrhea disease models identified in the literature searched — *N. gonorrhoeae* research relies predominantly on the estradiol mouse model and human ex vivo/cell-culture systems given the organism's human-restricted tropism.

**Suggested model-organism ontology terms:** NCBITaxon:10090 (*Mus musculus*), model type "induced infection model" (hormone-primed genital colonization); MGI resources for background mouse strain records; Cellosaurus IDs for relevant human epithelial cell lines used in adhesion/invasion assays (e.g., ME-180, HEC-1-B cervical lines — verify via literature before citing specific Cellosaurus accessions).

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Suggested terms |
|---|---|
| MONDO | MONDO:0004277 (gonorrhea) |
| NCBITaxon (pathogen) | NCBITaxon:485 (*N. gonorrhoeae*) |
| HGNC (host modifier genes) | hgnc:5394 (CFI), hgnc:1346 (C7), hgnc:1358 (C9), hgnc:4883 (CFH) |
| HP (phenotypes) | HP:0030128 (urethral discharge), HP:0100518 (dysuria), HP:0000534 (purulent conjunctivitis), HP:0001945 (fever), HP:0100546 (arthralgia), HP:0001369 (arthritis), HP:0000789 (infertility), HP:0010935 (ectopic pregnancy) |
| GO (biological process) | GO:0007155 (cell adhesion), GO:0044409 (entry into host), GO:0052255 (modulation by symbiont of host innate immune response), GO:0043312 (neutrophil degranulation) |
| CL (cell types) | CL:0000775 (neutrophil), CL:0000235 (macrophage), ciliated fallopian-tube epithelial cell |
| UBERON | UBERON:0000057 (urethra), UBERON:0000995 (cervix), UBERON:0003889 (fallopian tube), UBERON:0004908 (oropharynx), UBERON:0001759 (conjunctiva), UBERON:0001466 (synovial joint) |
| CHEBI (drugs) | ceftriaxone, azithromycin, doxycycline, cefixime, ciprofloxacin (verify exact CURIEs via OAK) |
| NCIT (treatment) | NCIT:C15986 (Pharmacotherapy), NCIT:C15329 (Surgical Procedure) |

---

## Sources

- [Neisseria gonorrhoeae physiology and pathogenesis (PMID:35489793)](https://pubmed.ncbi.nlm.nih.gov/35489793/)
- [Mechanisms of host manipulation by Neisseria gonorrhoeae](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9935845/)
- [Neisseria gonorrhoeae Modulates Immunity by Polarizing Human Macrophages to a M2 Profile](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4488386/)
- [Global Analysis of Neutrophil Responses to Neisseria gonorrhoeae](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4154863/)
- [CDC STI Statistics 2024 (Provisional)](https://www.cdc.gov/sti-statistics/annual/index.html)
- [CDC Releases 2024 National STI Data (HIV.gov)](https://www.hiv.gov/blog/cdc-releases-2024-national-sti-data)
- [Are STDs truly declining? Dissecting the 2024 CDC report (Healthbeat)](https://www.healthbeat.org/2025/10/07/sti-chlamydia-gonorrhea-syphilis-cdc-data/)
- [Mind the Clap: Reported Disseminated Gonococcal Infections, 2020-2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9751791/)
- [Antimicrobial resistance in Neisseria gonorrhoeae: history, molecular mechanisms (PMC5628311)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5628311/)
- [Reliability of Genetic Alterations in Predicting Ceftriaxone Resistance (PMC9045316)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9045316/)
- [Ceftriaxone-resistant, multidrug-resistant N. gonorrhoeae, mosaic penA-237.001, France 2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9808317/)
- [Mosaic mtr efflux gene sequences and azithromycin resistance (PMC6134098)](https://ncbi.nlm.nih.gov/pmc/articles/PMC6134098)
- [Azithromycin Resistance through Interspecific Acquisition (PMC6083905)](https://ncbi.nlm.nih.gov/pmc/articles/PMC6083905)
- [Gonococcal meningitis: unusual presentation of DGI](https://pmc.ncbi.nlm.nih.gov/articles/PMC9602952/)
- [Disseminated gonococcal infection (DGI) and gonococcal arthritis - PMID:6112797](https://pubmed.ncbi.nlm.nih.gov/6112797/)
- [Disseminated gonococcal infection: prospective analysis of 49 patients - PMID:6415361](https://pubmed.ncbi.nlm.nih.gov/6415361/)
- [Disseminated Gonococcal Infection Presenting as Isolated Septic Arthritis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11368578/)
- [Gonococcal Tenosynovitis With Abscess Formation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12701954/)
- [Disseminated gonococcal infection secondary to complement factor I deficiency (PMID:41607490)](https://pubmed.ncbi.nlm.nih.gov/41607490/)
- [DGI in a man with complement 7 deficiency](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8021336/)
- [Extreme gonococcal susceptibility with acquired complement deficiency (HUV/SLE)](https://www.sciencedirect.com/science/article/abs/pii/S1341321X21002932)
- [Ocular Prophylaxis for Gonococcal Ophthalmia Neonatorum - USPSTF Evidence Update](https://www.ncbi.nlm.nih.gov/books/NBK537599/)
- [Ophthalmia Neonatorum - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK551572/)
- [Pelvic Inflammatory Disease (PID) from Chlamydia vs. Gonorrhea (PMID:23007248)](https://pubmed.ncbi.nlm.nih.gov/23007248/)
- [Immunopathogenesis of PID and infertility (PMID:12346974)](https://pubmed.ncbi.nlm.nih.gov/12346974/)
- [IL-17C driver of damaging inflammation in Fallopian tube infection (PMC11069574)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11069574/)
- [Fitz-Hugh-Curtis Syndrome - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK499950/)
- [Gonorrhoic perihepatitis. Fitz-Hugh-Curtis syndrome (PMID:6769152)](https://pubmed.ncbi.nlm.nih.gov/6769152/)
- [Evaluating cross-protection: Meningococcal vaccines and gonorrhoea prevention meta-analysis (PMID:40334533)](https://pubmed.ncbi.nlm.nih.gov/40334533/)
- [4CMenB induces cross-species protection against Neisseria gonorrhoeae (PMC7748408)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7748408/)
- [Prevention of N. gonorrhoeae with Meningococcal B Vaccine: Matched Cohort Study (PMID:35642527)](https://pubmed.ncbi.nlm.nih.gov/35642527/)
- [Effectiveness of MenB-4C Vaccine Against Gonorrhea: Systematic Review and Meta-analysis](https://academic.oup.com/jid/article/231/1/61/7724768)
- [WHO Gonorrhoea fact sheet](https://www.who.int/news-room/fact-sheets/detail/gonorrhoea-(neisseria-gonorrhoeae-infection))
- [WHO: Gonorrhoea AMR results and vaccine development guidance, 2021](https://www.who.int/news/item/22-11-2021-gonorrhoea-antimicrobial-resistance-results-and-guidance-vaccine-development)
- [Recent advances in understanding and combatting N. gonorrhoeae: genomic perspective (PMC8442004)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8442004/)
- [High prevalence of tetracycline resistance in N. gonorrhoeae, 22 European countries, 2024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12811707/)
- [Management of N. gonorrhoeae in the US: 2020/2021 CDC Treatment Guidelines Evidence Summary (PMID:35416971)](https://pubmed.ncbi.nlm.nih.gov/35416971/)
- [Update to CDC's Treatment Guidelines for Gonococcal Infection, 2020](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7745960/)
- [Multicenter Comparison of NAATs for Rectal and Oropharyngeal CT/NG](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8769746/)
- [Evaluation of Six Commercial NAATs for N. gonorrhoeae Detection](https://pmc.ncbi.nlm.nih.gov/articles/PMC3187337/)
- [NAAT for N. gonorrhoeae: An Ongoing Challenge](https://pmc.ncbi.nlm.nih.gov/articles/PMC1871692/)
- [Opa proteins and CEACAMs: pathways of immune engagement for pathogenic Neisseria (PMID:21204865)](https://pubmed.ncbi.nlm.nih.gov/21204865/)
- [CEACAM is not necessary for N. gonorrhoeae adherence/invasion (PMID:11580753)](https://pubmed.ncbi.nlm.nih.gov/11580753/)
- [CEACAM binding determines outcome of N. gonorrhoeae infection along female reproductive tract](https://journals.asm.org/doi/full/10.1128/iai.00092-18)
- [Gonococcal outer membrane vesicle vaccines: bacterial population biology, clinical trials (npj Vaccines)](https://www.nature.com/articles/s41541-026-01410-2)
- [Pre-clinical efficacy of candidate OMV gonococcal vaccine vs. 4CMenB (PMID:42259835)](https://pubmed.ncbi.nlm.nih.gov/42259835/)
- [Breakthrough Rectal N. gonorrhoeae Infections After Meningococcal B Vaccination](https://academic.oup.com/ofid/article/11/11/ofae562/7863731)
- [Resistance of mice to genital infection with N. gonorrhoeae (PMID:2506350)](https://pubmed.ncbi.nlm.nih.gov/2506350/)
- [Estradiol-Treated Female Mice as Surrogate Hosts for N. gonorrhoeae Genital Tract Infections (PMID:21747807)](https://pubmed.ncbi.nlm.nih.gov/21747807/)
- [N. gonorrhoeae: Drug Resistance, Mouse Models, and Vaccine Development (PMID:28886683)](https://pubmed.ncbi.nlm.nih.gov/28886683/)
- [Auranofin antibacterial activity in female mouse genital tract infection model](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9022871/)
- [N. gonorrhoeae co-infection exacerbates vaginal HIV shedding in humanized mice](https://pmc.ncbi.nlm.nih.gov/articles/PMC5779692/)
- [Sexually transmitted infections and increased risk of HIV co-infection (PMID:15653780)](https://pubmed.ncbi.nlm.nih.gov/15653780/)
- [Risk of Subsequent HIV Infection Following STIs Among MSM](https://academic.oup.com/ofid/article/6/10/ofz376/5554073)