---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-09T18:27:00.529099'
end_time: '2026-08-09T18:32:42.005250'
duration_seconds: 341.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Opioid Use Disorder
  mondo_id: ''
  category: Psychiatric
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
  web_search_requests: 12
  num_turns: 14
  total_cost_usd: 1.6887547
  session_id: db8ba393-450c-5f19-a078-2aa9b08ae5a8
  stop_reason: end_turn
citation_count: 42
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Opioid Use Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Opioid Use Disorder** covering all of the
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

# Opioid Use Disorder — Comprehensive Disease Characteristics Research Report

*Prepared for dismech knowledge-base curation. All ontology term suggestions below are proposals only and must be independently verified (OAK lookup / label match) before being written into KB YAML, per the project's anti-hallucination SOP — several IDs below are given with explicit confidence caveats for that reason.*

---

## 1. Disease Information

**Overview.** Opioid use disorder (OUD) is a chronic, relapsing brain disease characterized by compulsive opioid seeking and use despite harmful consequences, driven by neuroadaptations in reward, stress, and executive-control circuitry following repeated exposure to exogenous opioid agonists (prescription analgesics, heroin, or illicit synthetic opioids such as fentanyl). It is defined clinically (DSM-5-TR) as a problematic pattern of opioid use leading to clinically significant impairment or distress, manifested by ≥2 of 11 criteria within a 12-month period, with severity graded mild (2–3 criteria), moderate (4–5), or severe (≥6). OUD sits on a continuum with physiological tolerance and withdrawal (which can occur with appropriate medical use and alone do not establish OUD) and encompasses what was previously split into DSM-IV "opioid abuse" and "opioid dependence."

**Key identifiers:**
- **ICD-10-CM:** F11.- (Opioid related disorders): F11.10 (abuse, uncomplicated), F11.20 (dependence, uncomplicated), F11.23 (dependence with withdrawal), F11.90 (use, unspecified)
- **ICD-11:** 6C43 (Disorders due to use of opioids); 6C43.2 (Opioid dependence)
- **OMIM:** 613459 — "Opioid Dependence, Susceptibility to" (candidate-gene entry, points to OPRM1)
- **MONDO:** MONDO:0001225 (opioid use disorder) — *verify before curating; some MONDO releases model "opioid dependence" as a related/child term*
- **MeSH:** D000068092 (Opioid-Related Disorders); D009293 (Narcotic-Related Disorders, older/broader term)
- **DSM-5-TR code:** 304.00/305.50 (legacy DSM-IV codes still cross-walked)

**Synonyms/alternative names:** opioid addiction, opioid dependence, narcotic addiction, heroin use disorder (heroin-specific), prescription opioid misuse/addiction, opioid abuse (legacy DSM-IV term).

**Evidence character:** Information below is drawn from aggregated epidemiological/registry data (CDC NCHS/NVSS, SAMHSA NSDUH), large genetic consortia (Million Veteran Program, Psychiatric Genomics Consortium, FinnGen, 23andMe), systematic reviews/meta-analyses, and mechanistic studies primarily in rodent models with translational human neuroimaging/genetic corroboration — not a single-patient EHR source.

---

## 2. Etiology

### Disease causal factors
OUD is a multifactorial, biopsychosocial disorder — no single causal genetic lesion (unlike Mendelian dismech entries); risk arises from the interaction of (a) pharmacological exposure to an exogenous mu-opioid-receptor (MOR) agonist, (b) polygenic genetic liability, and (c) environmental/psychosocial exposures. Exposure — most commonly initiated via a legitimate prescription for acute or chronic pain, or via non-medical use of diverted prescription opioids or illicit heroin/fentanyl — is a *necessary* but not sufficient cause; only a minority of opioid-exposed individuals develop OUD.

### Risk factors

**Genetic risk factors:**
- **OPRM1** (mu-opioid receptor, hgnc:8156) — the most-studied candidate gene. The functional coding variant **rs1799971 (A118G, Asn40Asp)** shows a significant association with opioid dependence susceptibility in a 2023 meta-analysis of 13 studies (n=9,385; 4,601 cases/4,784 controls), strongest in Asian populations under a dominant model (PMID:23651028 for the earlier meta-analytic literature; 2023 update per Journal of Pain and Symptom Management search). A genome-wide-significant OPRM1 functional coding-variant association with OUD was also independently confirmed by GWAS (PMID:32492095).
- **FURIN** — identified as a genome-wide-significant lead locus in the largest multi-ancestry OUD GWAS to date (European + African ancestry, N=639,063 across Million Veteran Program, Psychiatric Genomics Consortium, iPSYCH, FinnGen, Partners Biobank, BioVU, Yale-Penn 3), alongside two independent OPRM1 variants; a multi-trait analysis (MTAG) combining OUD with related traits yielded **18–19 independent genome-wide-significant loci** (Nature/Molecular Psychiatry, 2022; PMC9718667).
- **KDM4A** (rs3791033, intronic) and a locus near **LRRIQ3** (rs640561, intergenic) — identified in a 23andMe GWAS of problematic opioid prescription use in 132,113 research participants of European ancestry (PMID:34728798).
- **CPT2, CD47, SLC5A11** — three novel OUD loci from a March 2024 genome-wide analysis of shared genetic architecture between OUD and general cognitive ability, which also replicated 4 loci from prior GWAS and found 7 loci not previously reported (PMC11831617).
- **CNIH3** — implicated in an earlier opioid dependence GWAS (Nelson et al., 2016; PMID:26857631, from established literature).
- Other candidate/modifier genes with supporting literature: **OPRD1** (delta-opioid receptor), **OPRK1**/**PDYN** (kappa-opioid receptor/dynorphin, stress/anti-reward axis), **DRD2** and **BDNF** (associated with continued opioid use during methadone treatment; PMC4672523), **COMT** (dopamine catabolism, pain sensitivity modulation).
- **Heritability:** Twin/family studies estimate heritability at roughly **23–54%**, with more recent estimates clustering around **40–60%**; Kendler et al. (~1,200 male-male twin pairs) estimated ~48% genetic liability, Tsuang et al. (Vietnam Era twins) ~54%. Approximately 38% of variance is opioid-specific (not shared with general substance-use liability), indicating both shared addiction-general and opioid-specific genetic architecture.
- **Pharmacogenomic modifiers of exposure/risk:** **CYP2D6** poor/ultrarapid-metabolizer status alters conversion of prodrug opioids (codeine, tramadol) to active metabolites, affecting individual exposure/efficacy and potentially misuse liability; **CYP3A4/CYP2B6** affect methadone/buprenorphine clearance; **ABCB1** (P-glycoprotein) variants affect CNS opioid penetration.

**Environmental risk factors:**
- Long-term prescription opioid therapy for chronic pain (dose- and duration-dependent risk)
- Prior or current substance use disorder (alcohol, cannabis, cocaine, benzodiazepines — strong polysubstance overlap)
- Family history of substance use disorder
- Adverse childhood experiences (ACEs) / childhood trauma, physical/sexual abuse
- Co-occurring untreated psychiatric illness (depression, anxiety, PTSD — see Section 3)
- Socioeconomic deprivation, unemployment, rural/economically distressed communities (historically linked to the U.S. prescription-opioid "first wave" of the epidemic, 1990s–2000s, driven partly by aggressive marketing/overprescribing of extended-release oxycodone)
- Incarceration history (elevated post-release overdose risk due to loss of tolerance)
- Age of first opioid exposure (adolescent/young-adult initiation confers higher risk owing to ongoing prefrontal cortical maturation)
- Male sex (historically higher prevalence; the sex gap has narrowed substantially in recent U.S. cohorts)
- Illicit drug-supply contamination with fentanyl and fentanyl analogs — a supply-side environmental risk factor that has dramatically increased overdose lethality independent of use-disorder severity (the "third/fourth wave" of the U.S. epidemic, now compounded by opioid-stimulant co-use).

**Protective factors:**
- **Genetic:** evidence here is far less consistent than for risk variants; some studies suggest certain OPRM1 haplotypes or reduced-function variants at addiction-relevant loci may modestly lower liability, but no robustly replicated protective allele is established (unlike, e.g., ALDH2*2 in alcohol use disorder). Flag as an evidence gap rather than assert a specific protective variant.
- **Environmental/clinical:** access to non-opioid pain management, prescription drug monitoring programs (reduce diversion/doctor-shopping), strong social support and family cohesion, higher educational attainment, timely access to medications for OUD (MOUD), community naloxone distribution and harm-reduction services (syringe service programs, fentanyl test strips), effective treatment of comorbid psychiatric illness.

**Gene-environment interactions.** The clearest documented G×E interaction is genotype-dependent *response to exposure/treatment* rather than genotype-dependent initiation risk: OPRM1 A118G carriers show altered β-endorphin binding, altered HPA-axis (cortisol) response to naloxone challenge, and differential dose requirements for opioid analgesics and methadone, and modestly altered naltrexone treatment response (Oslin et al., PGx literature). More broadly, genetic liability for general addiction/externalizing traits appears to interact with the local prescribing/illicit-supply environment (e.g., fentanyl contamination) to determine whether genetic risk translates into fatal overdose versus non-fatal OUD — an environment that has changed dramatically over the past decade and is not fully captured by pre-2015 genetic studies.

---

## 3. Phenotypes

OUD phenotypes span acute intoxication, chronic-use, tolerance/withdrawal, and complication domains. Frequencies below are approximate/derived from clinical literature; treat as `OCCASIONAL`/`FREQUENT`-type qualitative bands pending exact quantitative sourcing per curation SOP.

| Phenotype | Type | Onset/course | Suggested HPO (verify before use) |
|---|---|---|---|
| Craving (persistent urge to use) | Behavioral/cognitive core symptom | Chronic, fluctuating, can persist into prolonged abstinence | — (behavioral abnormality branch; no precise HPO substance-craving term confirmed) |
| Tolerance (need for increasing doses) | Physiological/laboratory-adjacent | Develops over days–weeks of regular use | — |
| Opioid withdrawal syndrome (rhinorrhea, lacrimation, mydriasis, piloerection, myalgia/arthralgia, nausea, vomiting, diarrhea, abdominal cramping, insomnia, yawning, dysphoria, autonomic hyperactivity) | Clinical signs/symptoms | Acute onset 6–24h after last dose (short-acting) or 24–48h (methadone); resolves over 5–10 days for acute phase; protracted withdrawal can persist weeks–months | HP:0002014 (Diarrhea), HP:0000969 (Edema — n/a), HP:0002617 (Piloerection?), HP:0000745 (Irritability), HP:0002367 (Paroxysmal (n/a)) — *most withdrawal signs map to generic HPO clinical-sign terms rather than an opioid-specific term; verify each individually* |
| Miosis (pinpoint pupils) | Clinical sign, acute intoxication | Acute, dose-dependent | HP:0000454 (Miosis, or specific pupillary term — verify) |
| Respiratory depression (acute overdose) | Clinical sign/emergency | Acute, dose-dependent, potentiated by concurrent sedatives/fentanyl potency | HP:0002093-adjacent respiratory terms — verify |
| Opioid-induced constipation / bowel dysfunction | Laboratory/clinical (chronic) | Chronic, dose-related, does not resolve with tolerance to other effects | relevant GI HPO term — verify |
| Opioid-induced hyperalgesia | Clinical/laboratory-adjacent | Emerges with prolonged high-dose exposure | — |
| Sedation/cognitive slowing | Symptom | Acute–subacute | HP:0032988 or similar cognitive-impairment term — verify |
| Hypogonadism (opioid-induced androgen deficiency) | Laboratory/endocrine | Chronic, dose/duration-dependent | HP:0000135 (Hypogonadism) plausible |
| Central sleep apnea / sleep-disordered breathing | Clinical/laboratory (polysomnography) | Chronic, high-dose opioid therapy | HP:0002104 (Apnea) or CSA-specific term — verify |
| Immunosuppression | Laboratory | Chronic use | — |
| Neonatal opioid withdrawal syndrome / neonatal abstinence syndrome (NAS) | In utero-exposed offspring phenotype (relevant to comorbidity/trajectory rather than the proband) | Onset 24h–several days postnatally | HP:0025468 or NAS-specific term if present — verify; MedGen has a distinct NAS concept |
| Depressed mood / anhedonia during withdrawal and protracted abstinence | Behavioral | Subacute–chronic | overlaps HP depression terms |
| Unsuccessful efforts to cut down/control use | Behavioral (DSM criterion) | Chronic | — |
| Continued use despite social/interpersonal problems | Behavioral (DSM criterion) | Chronic | — |
| Hazardous use (e.g., while driving) | Behavioral (DSM criterion) | Episodic | — |

**Severity/progression:** DSM-5-TR severity (mild/moderate/severe) is criterion-count based, not biomarker based; course is frequently chronic-relapsing, with a substantial minority achieving sustained remission, especially with MOUD engagement. **Quality of life:** OUD is associated with markedly reduced quality of life across physical, psychological, and social domains (SF-36/EQ-5D literature); untreated OUD carries a substantially elevated all-cause and overdose-specific mortality risk relative to the general population, with mortality risk sharply reduced during active MOUD treatment and elevated during treatment gaps/post-incarceration/post-detox (loss-of-tolerance overdose risk).

---

## 4. Genetic/Molecular Information

**Causal/major-effect genes:** No single Mendelian causal gene exists (OUD is polygenic/complex, unlike most dismech Mendelian entries); OMIM's "Opioid Dependence, Susceptibility to" (613459) is a susceptibility-locus entry pointing to **OPRM1** (hgnc:8156; chr6q25.2), not a causal-variant Mendelian disease gene.

**Key pathogenic/risk-associated variants:**
- **OPRM1 rs1799971 (A118G / Asn40Asp)** — missense, exon 1; alters MOR N-glycosylation and receptor trafficking/signaling efficacy; associated with altered opioid analgesic requirements, methadone dosing, naltrexone treatment response, and dependence susceptibility (mixed/heterogeneous meta-analytic results across populations; strongest signal in Asian cohorts per the 2023 meta-analysis). Allele frequency varies substantially by ancestry (minor G-allele more common in East Asian populations) — check gnomAD for population-specific frequencies before citing a number.
- **FURIN locus variants** and **two independent OPRM1 variants** — genome-wide significant in the 2022 multi-ancestry MTAG GWAS (PMC9718667).
- **KDM4A (rs3791033)**, **LRRIQ3-adjacent (rs640561)** — from 23andMe GWAS of problematic opioid prescription use (PMID:34728798).
- **CPT2, CD47, SLC5A11** loci — from the 2024 OUD/cognitive-ability shared-architecture GWAS (PMC11831617).
- These are **risk/susceptibility variants**, not ACMG pathogenic-classified Mendelian variants; ClinVar/ClinGen do not carry a curated gene-disease validity assertion for OUD in the sense used for Mendelian dismech entries — this is a key modeling difference from most KB entries and should be flagged in any `genetic:` block (e.g., via `relationship_type: SUSCEPTIBILITY`).

**Functional consequences:** OPRM1 A118G is generally treated in the literature as altering receptor expression/signaling efficiency rather than a classic gain/loss-of-function dichotomy; characterize cautiously as a modifier of receptor trafficking and downstream signaling rather than assigning `functional_impact_category: LOSS_OF_FUNCTION`/`GAIN_OF_FUNCTION` without a specific supporting functional study.

**Somatic vs. germline:** All established OUD risk variants are germline/constitutional; no somatic-mutation component is implicated in this disease process (unlike cancer entries).

**Epigenetics:** Chronic opioid exposure is associated with epigenetic remodeling in reward circuitry — DNA methylation changes at stress- and reward-related genes, and histone modifications (e.g., altered histone acetylation at FosB/ΔFosB and CREB target genes in the nucleus accumbens) have been reported in preclinical models and some human postmortem/peripheral-tissue studies; this literature is less mature/replicated than for the genetic-association findings above and should be sourced to specific primary papers before curating individual claims.

**Chromosomal abnormalities:** No recurrent chromosomal aberration (aneuploidy, translocation) is associated with OUD; this is a polygenic complex trait, not a cytogenetic disorder.

---

## 5. Environmental Information

**Environmental/exposure factors:**
- Prescription opioid exposure for acute or chronic pain — the dominant iatrogenic route of initiation historically in the U.S.
- Illicit opioid supply — heroin, and increasingly **illicitly manufactured fentanyl and fentanyl analogs** (e.g., carfentanil), which now dominate U.S. overdose mortality; synthetic opioids (chiefly fentanyl) accounted for an estimated **48,422 of the 54,743 opioid-involved overdose deaths in 2024** (provisional CDC/NCHS data), underscoring illicit-fentanyl contamination as the primary proximate environmental driver of current mortality (CDC NCHS Data Brief 549; CDC NCHS/NVSS provisional data release, 2025).
- Co-use/adulteration with stimulants (methamphetamine, cocaine) and with benzodiazepines/xylazine — increasingly common and mechanistically important because these combinations increase overdose lethality and complicate naloxone-only reversal (xylazine, an alpha-2 agonist veterinary sedative, does not respond to naloxone).
- Healthcare-system/prescribing environment: opioid marketing practices, prescribing guidelines and their evolution (e.g., 2016/2022 CDC opioid prescribing guidelines), prescription drug monitoring program coverage.

**Lifestyle factors:** Polysubstance use (alcohol, benzodiazepines, stimulants — each independently raising overdose risk via additive/synergistic respiratory depression or complicating clinical management), smoking, housing instability, involvement in the criminal-legal system.

**Infectious agents (indirectly disease-associated, not causal of OUD itself):** Injection drug use associated with OUD is a major transmission route for **HIV**, **hepatitis C virus (HCV)**, and **hepatitis B virus (HBV)**, as well as bacterial infections (infective endocarditis, skin/soft-tissue abscesses, epidural abscess) from non-sterile injection practices — these are downstream comorbidities/complications rather than causal agents of OUD, and would more naturally be modeled as `comorbidities/` or downstream pathophysiology nodes than as OUD's own etiology.

---

## 6. Mechanism / Pathophysiology

### Acute reward mechanism
Opioids (endogenous or exogenous) act primarily via the **mu-opioid receptor (MOR, OPRM1)**, a Gi/Go-coupled GPCR. MOR agonism in the **ventral tegmental area (VTA)** hyperpolarizes local GABAergic interneurons (via Gi-mediated inhibition of adenylyl cyclase and opening of GIRK potassium channels), **disinhibiting VTA dopaminergic neurons** and increasing dopamine release into the **nucleus accumbens (NAc)** — the canonical positive-reinforcement/reward pathway underlying acute drug liking and euphoria. Recent circuit-level work indicates this is not a uniform effect across the entire VTA dopamine population but instead recruits specific dopaminergic and non-dopaminergic (GABAergic, opioid-peptidergic) subcircuits within the mesocorticolimbic system (Nature Reviews Neuroscience, Oct 2025 review; Neuron 2025 mesolimbic-circuitry paper).

### Chronic neuroadaptation ("opponent-process"/allostasis model)
With repeated exposure, the brain's reward system down-regulates (reduced dopaminergic tone, reduced hedonic capacity — "reward deficit") while **anti-reward/stress systems up-regulate**: corticotropin-releasing factor (CRF) is released from hypothalamic/extended-amygdala neurons, activating the HPA axis (ACTH → cortisol) and central stress circuitry (extended amygdala CRF/dynorphin-kappa-opioid-receptor signaling), producing the negative-affective state that drives use to escape withdrawal-associated dysphoria rather than purely to seek euphoria (Koob-model allostasis). This underlies the shift from positive to negative reinforcement across the addiction cycle (binge/intoxication → withdrawal/negative affect → craving/preoccupation).

### Withdrawal mechanism — locus coeruleus (LC) hyperactivity
Chronically, MOR agonism in the **locus coeruleus** (major noradrenergic nucleus) is opposed by compensatory **upregulation of the cAMP–PKA signaling cascade** (adenylyl cyclase superactivation, enhanced G-protein/PKA transduction — classic Nestler-lab cAMP-upregulation model of opiate dependence), so that abrupt opioid removal (or naloxone precipitation) unmasks this compensatory hyperactivity as a surge of LC noradrenergic firing, producing the autonomic/somatic withdrawal syndrome (restlessness, anxiety, sweating, tachycardia, and the classic flu-like symptom cluster in Section 3). Nitric oxide signaling and galanin/GalR1 autoreceptor feedback have been implicated as intermediate messengers modulating LC hyperactivity during withdrawal in rodent models (search-sourced primary literature on LC withdrawal pharmacology).

### Tolerance and opioid-induced hyperalgesia
Chronic MOR activation drives receptor desensitization/internalization, and — mechanistically distinct — a pronociceptive sensitization process: morphine-induced tolerance/hyperalgesia has been linked to increased adenosine kinase expression with reduced A3 adenosine receptor signaling and associated neuroinflammatory glial activation; A3AR agonism attenuates these effects in preclinical models (search-sourced primary literature).

### Neuroimmune involvement
Glial (microglial/astrocytic) activation and neuroinflammatory signaling (e.g., TLR4 pathway activation by opioids, independent of classical MOR signaling in some models) contribute to tolerance, hyperalgesia, and withdrawal severity — an active area of mechanistic and drug-discovery research.

### Cell types and anatomical circuitry involved
- VTA dopaminergic neurons (reward)
- NAc medium spiny neurons (reward output, plasticity — ΔFosB accumulation with chronic exposure)
- Locus coeruleus noradrenergic neurons (withdrawal/arousal)
- Extended amygdala / central nucleus of the amygdala CRF neurons (stress/anti-reward)
- Periaqueductal gray (analgesia, also implicated in withdrawal-associated aversive state)
- Prefrontal cortex circuitry (impaired top-down inhibitory control, craving/relapse vulnerability)
- Microglia/astrocytes (neuroinflammatory contribution to tolerance/hyperalgesia)

### Suggested GO / molecular-function terms (verify before curating)
- G protein-coupled opioid receptor signaling pathway (candidate: GO:0038003)
- Adenylate cyclase-inhibiting G protein-coupled receptor signaling pathway (GO:0007193)
- Response to morphine (candidate GO term exists in this space — confirm exact ID/label via OAK)
- Regulation of dopamine secretion (GO:0014059)
- Positive regulation of synaptic transmission, dopaminergic (verify exact term)

### Suggested CL (cell type) terms (verify before curating)
- Dopaminergic neuron (CL:0000700)
- Medium spiny neuron (CL:0000750)
- Noradrenergic neuron (verify exact CL ID)
- Microglial cell (CL:0000129)
- Astrocyte (CL:0000127)

### Omics/advanced technologies
Human neuroimaging (fMRI, PET receptor-occupancy studies) demonstrates blunted striatal dopaminergic response to non-drug reward and altered prefrontal-limbic connectivity in individuals with OUD; single-cell/spatial-transcriptomic work in rodent models with humanized OPRM1 A118G knock-in shows cell-type-specific transcriptional and connectivity changes following opioid dependence (PMC12393594, PMC10866092 — spatial transcriptomics and neural-connectivity studies in the A118G mouse model). Whole-exome sequencing of opioid dependence cohorts has begun to characterize rare-variant contributions beyond the common-variant GWAS signal (Translational Psychiatry, 2025, whole-exome study).

---

## 7. Anatomical Structures Affected

**Organ/system level:**
- **Primary:** Central nervous system — mesocorticolimbic reward circuit, brainstem (locus coeruleus, periaqueductal gray, respiratory centers in the medulla — the substrate of fatal overdose via central respiratory depression)
- **Secondary/complication-related:** Cardiovascular system (methadone-associated QT prolongation/torsades risk), gastrointestinal system (opioid-induced bowel dysfunction/constipation), endocrine system (hypothalamic-pituitary-gonadal axis suppression → hypogonadism), respiratory system (central and obstructive sleep apnea with chronic high-dose use; acute respiratory failure in overdose), immune system (opioid-associated immunosuppression), and — via the injection-drug-use route specifically — cardiac valves (infective endocarditis), liver (viral hepatitis, hepatotoxicity), skin/soft tissue (abscesses, cellulitis).

**Tissue/cell level:** CNS neurons (dopaminergic VTA, noradrenergic LC, GABAergic interneurons, medium spiny neurons of the NAc), glia (microglia, astrocytes) implicated in neuroinflammatory contributions to tolerance/withdrawal.

**Subcellular level:** MOR receptor trafficking/internalization (plasma membrane → endosomal compartments) is central to tolerance mechanisms; downstream signaling involves adenylyl cyclase/cAMP at the plasma membrane and nuclear transcriptional changes (ΔFosB accumulation in the nucleus of NAc neurons with chronic exposure) as a molecular substrate of long-term neuroplasticity.

**Localization:** Bilateral, diffuse CNS circuit-level disorder rather than a focal anatomical lesion — not a lateralized condition.

**Suggested UBERON terms (verify before curating):** ventral tegmental area (UBERON:0002550), nucleus accumbens (UBERON:0001882), locus coeruleus (UBERON:0002037), amygdala (UBERON:0001876), periaqueductal gray (UBERON:0002440).

---

## 8. Temporal Development

**Onset:** Most commonly young-adult onset, though initiation frequently begins with adolescent or young-adult exposure to prescription opioids (post-surgical, post-injury) or non-medical initiation; onset of the disorder (as opposed to exposure) is typically subacute-to-insidious, evolving over weeks to months of regular use as tolerance and dependence establish, though rapid escalation is well documented with high-potency illicit fentanyl.

**Progression:** Course is classically **chronic and relapsing-remitting** rather than a fixed staged progression (unlike, e.g., cancer TNM staging); the Koob "addiction cycle" framework (binge/intoxication → withdrawal/negative affect → preoccupation/anticipation, recurring) is the standard conceptual staging used in the addiction-neuroscience literature rather than a formal clinical stage system. DSM-5-TR severity (mild/moderate/severe) reflects cumulative criterion count rather than a temporal stage.

**Patterns:**
- Spontaneous remission occurs but is less common than in some other substance use disorders; treatment-facilitated remission with MOUD substantially improves retention and reduces mortality.
- Relapse is common, particularly during high-risk transition periods: post-detoxification, post-incarceration, and after voluntary/involuntary treatment discontinuation — these periods carry sharply elevated overdose mortality risk due to loss of physiological tolerance.
- "Critical periods"/windows of intervention opportunity: the immediate post-overdose period (linkage-to-care), post-incarceration release, and pregnancy (engagement with prenatal care) are recognized high-yield windows for MOUD initiation.
- Protracted withdrawal/post-acute withdrawal syndrome (sleep disturbance, anhedonia, dysphoria, and craving persisting weeks to months beyond acute physical withdrawal) is a recognized clinical pattern contributing to relapse risk.

---

## 9. Inheritance and Population

**Epidemiology:**
- **U.S. overdose mortality (2024, provisional CDC/NCHS data):** an estimated **80,391 total drug overdose deaths**, down 26.9% from 110,037 in 2023; opioid-involved deaths fell from **83,140 (2023) to 54,743 (2024)**; synthetic-opioid (chiefly fentanyl)-involved deaths fell from 76,282 to 48,422 over the same period — the largest year-over-year decline in recent U.S. history, though still representing tens of thousands of deaths annually, and almost all states saw declines (some >35%: Louisiana, Michigan, New Hampshire, Ohio, Virginia, West Virginia, Wisconsin, D.C.), while South Dakota and Nevada saw slight increases (CDC NCHS Data Brief 549, 2025; CDC NCHS/NVSS provisional overdose data release).
- **U.S. prevalence (misuse, NSDUH):** an estimated **8.9 million people aged 12+ misused opioids** in the past year per 2023 NSDUH; 2024 NSDUH reported **7.6 million people misusing prescription opioids** in the past year (methodology shifted between survey years — 2024 collected past-year rather than past-month detail, so year-over-year comparison should be made cautiously) (SAMHSA 2024 NSDUH Annual National Report).
- **Global burden:** Globally, opioid dependence prevalence increased by an estimated **47% from 1990 to 2016**, the largest relative increase among substance use disorders in that period, with the highest opioid-dependence prevalence historically concentrated in North America (search-sourced review literature, PMC4628571/related).
- Only a fraction of people with OUD receive medications for OUD (MOUD); SAMHSA's pooled 2022–2024 NSDUH data are specifically tracking this treatment gap (SAMHSA NSDUH MOUD Data Spotlight).

**Inheritance pattern:** Complex/multifactorial (polygenic), **not** a single-gene Mendelian disorder — model any `inheritance:` block accordingly (e.g., omit a classical AD/AR/X-linked designation, or use a multifactorial/complex-trait annotation if the schema supports one; do not force-fit HP:0010982 polygenic inheritance without checking whether that's the intended semantic for a behavioral/complex trait disease rather than a monogenic disease with polygenic modifiers).

**Heritability:** ~23–60% across twin/family studies (see Section 4), with substantial shared environmental and unique environmental contribution to the remainder — this is a genetically influenced complex trait, not a highly penetrant Mendelian condition, and penetrance/expressivity concepts as used for monogenic dismech entries do not straightforwardly apply.

**Population demographics:**
- Historically higher prevalence in males, though the sex gap in both use and overdose mortality has narrowed substantially in recent U.S. cohorts.
- Marked geographic variation within the U.S. (Appalachia, New England, and parts of the Midwest/Rust Belt historically disproportionately affected during the prescription-opioid and heroin waves; illicit fentanyl has since spread geographically, notably into the Western U.S. in more recent years).
- Racial/ethnic disparities in overdose mortality have shifted over the epidemic's course, with recent years showing disproportionate mortality increases among Black and Native American/Alaska Native populations relative to earlier phases dominated by white, rural populations — consult current CDC/KFF demographic breakdowns for precise, year-specific figures before citing exact rates.
- Age distribution of overdose deaths is concentrated in adults 25–54, though this varies by opioid class and by year.

---

## 10. Diagnostics

**Clinical criteria:** DSM-5-TR opioid use disorder criteria (11 total; ≥2 within 12 months for diagnosis; severity by count as above) remain the primary diagnostic standard; ICD-11 6C43.2 (opioid dependence) uses the ICD dependence-syndrome framework (impaired control, increasing priority over other activities, physiological features).

**Laboratory tests:**
- Urine drug screening (immunoassay) for opioids/opiates — note that standard opiate immunoassays often do **not** reliably detect synthetic opioids (fentanyl, methadone, buprenorphine) without a specific fentanyl or extended-panel assay, a clinically important limitation in the fentanyl era.
- Confirmatory testing via GC-MS or LC-MS/MS for specific opioid/metabolite identification.
- Serum/plasma opioid levels are not routinely used diagnostically for OUD (unlike therapeutic drug monitoring in other contexts) but may be used forensically/in overdose management.
- No specific validated blood biomarker exists for OUD diagnosis at this time (unlike, e.g., HbA1c for diabetes) — this is a clinical/behavioral diagnosis.

**Genetic testing:** Not part of standard clinical diagnostic workup for OUD (unlike Mendelian disease); pharmacogenomic testing (e.g., CYP2D6 genotyping) has clinical utility for individualizing opioid analgesic prescribing/metabolism prediction and, in research contexts, OPRM1 genotyping has been explored to guide naltrexone treatment selection, but this is not standard of care.

**Screening tools:** Structured screening instruments are used far more than lab/genetic tests: Opioid Risk Tool (ORT), Screener and Opioid Assessment for Patients with Pain (SOAPP), COWS (Clinical Opiate Withdrawal Scale) and SOWS (Subjective Opiate Withdrawal Scale) for withdrawal severity grading, DSM-5-TR criteria checklist, and universal prescription drug monitoring program (PDMP) queries prior to opioid prescribing.

**Differential diagnosis:** Other substance use disorders (with polysubstance co-use being common rather than exclusionary), primary anxiety/depressive/PTSD disorders (which are frequently comorbid rather than purely differential — see Section 3), chronic pain syndromes without a use disorder (physiological tolerance/dependence from appropriate medical use alone does not meet OUD criteria), and — in the overdose/acute setting — other causes of altered mental status/respiratory depression (sedative-hypnotic overdose, stroke, hypoglycemia).

**Imaging/functional testing:** Not diagnostic for clinical OUD but used in research: fMRI/PET studies characterizing blunted striatal dopaminergic reward response and altered prefrontal-limbic connectivity.

---

## 11. Outcome/Prognosis

**Mortality:** OUD carries substantially elevated all-cause mortality versus the general population, driven predominantly by fatal overdose (increasingly fentanyl-driven — see Section 9 statistics), but also by infectious complications (endocarditis, sepsis from injection drug use), trauma, and suicide (elevated in the context of comorbid depression/PTSD — see Section 3). Mortality risk is markedly reduced during active engagement in MOUD (methadone/buprenorphine) and is sharply elevated during treatment gaps, immediately post-detoxification, and immediately post-incarceration release, due to loss of physiological tolerance combined with return to a high-potency illicit-fentanyl supply.

**Course/recovery potential:** Chronic-relapsing course is typical, but long-term recovery is achievable and common with sustained MOUD engagement plus psychosocial support; abstinence-only (non-medication) approaches are associated with substantially higher relapse and overdose-death rates than MOUD-based treatment in comparative studies (see Section 12).

**Morbidity/complications:** Injection-related infectious complications (HIV, HCV, HBV, infective endocarditis, skin/soft-tissue infections, epidural abscess), opioid-induced constipation/bowel dysfunction, hypogonadism, sleep-disordered breathing, neurocognitive effects, and — in pregnancy — neonatal opioid withdrawal syndrome/NAS in exposed infants (reported in an estimated 42–94% of infants born to opioid-dependent mothers per older literature, though modern MOUD-in-pregnancy management substantially alters this trajectory; NCBI Bookshelf NBK551498 and PMC5827164).

**Quality of life:** Substantially reduced across physical, psychological, and social functioning domains while actively using; meaningfully improved with sustained MOUD treatment and recovery.

**Prognostic factors:** Treatment engagement/retention (strongest modifiable predictor), presence and treatment of comorbid psychiatric illness, social support/housing stability, access to naloxone and harm-reduction services, and the local illicit-supply fentanyl contamination level (a population-level rather than individual-level prognostic factor that has become increasingly dominant).

---

## 12. Treatment

### Pharmacotherapy (medications for opioid use disorder, MOUD) — the evidence-based first-line standard of care

- **Methadone** — full mu-opioid receptor agonist, long half-life, dispensed through federally regulated Opioid Treatment Programs (OTPs) in the U.S. In network meta-analyses/systematic reviews of retention, methadone shows superior treatment retention compared with buprenorphine, which in turn outperforms naltrexone (PLOS One network meta-analysis; Lancet Psychiatry 2023 systematic review/meta-analysis of buprenorphine vs. methadone).
- **Buprenorphine** (partial MOR agonist, kappa-antagonist; ceiling effect on respiratory depression improves its overdose-safety margin relative to full agonists) — commonly co-formulated with naloxone (buprenorphine-naloxone, e.g., Suboxone) to deter intravenous misuse; office-based prescribing was historically restricted by a DEA "X-waiver," which was **removed under the 2023 MAT Act**, substantially expanding prescriber access. Extended-release formulations: **Sublocade** (monthly SC injection, approved 2017) and **Brixadi** (weekly/monthly injection, approved 2023).
- **Naltrexone** — full MOR antagonist; oral formulation has poor adherence-driven effectiveness (did not show higher retention than placebo in some meta-analyses), while **extended-release injectable naltrexone (Vivitrol)** shows comparable abstinence outcomes to buprenorphine-naloxone in some trials with an advantage in reducing days of opioid use in at least one comparative meta-analysis (PMC12421290); requires full detoxification (opioid-free interval) before initiation, a practical barrier relative to buprenorphine/methadone.
- **Lofexidine (Lucemyra)** — alpha-2 adrenergic agonist (mechanistically targeting the LC noradrenergic-hyperactivity substrate of withdrawal described in Section 6), FDA-approved 2018 specifically for mitigation of opioid withdrawal symptoms (not a maintenance/anti-craving agent).

### Overdose reversal
- **Naloxone** — competitive MOR antagonist, rapidly reverses opioid-induced respiratory depression; nasal spray formulations increasingly available **over-the-counter** (Narcan OTC approved March 2023; RiVive OTC approved July 2023), and higher-dose formulations (Kloxxado) developed to counter high-potency fentanyl overdoses.
- **Nalmefene** (Opvee nasal spray, approved May 2023) — longer-acting opioid antagonist, an alternative/adjunct to naloxone particularly relevant to prolonged fentanyl-driven respiratory depression, though its longer action also raises precipitated-withdrawal-duration considerations.

### Psychosocial/behavioral treatment
Cognitive behavioral therapy, contingency management (among the most robustly evidence-supported behavioral interventions for stimulant/opioid co-use), motivational interviewing, and mutual-support/peer-recovery programs (e.g., Narcotics Anonymous) — generally recommended as an adjunct to, not a substitute for, MOUD.

### Harm reduction
Syringe service programs, fentanyl/xylazine test strips, supervised consumption/overdose-prevention sites (where legally available), and community naloxone distribution — increasingly recognized as an integral component of the treatment/prevention continuum rather than a separate category.

### Treatment in special populations
MOUD (buprenorphine or methadone) during pregnancy is standard of care to reduce maternal relapse/overdose risk and stabilize the fetal environment, though optimal medication choice (methadone vs. buprenorphine) and comparative neonatal-outcome safety data remain an active area of study (PMC11583522; PMC4628571).

### Treatment strategy/algorithms
Clinical guidelines (ASAM National Practice Guideline, SAMHSA TIP series) generally recommend MOUD as first-line for OUD of at least moderate severity, individualized by patient preference, prior treatment response, pregnancy status, and access/logistics (OTP-based methadone vs. office-based buprenorphine vs. extended-release naltrexone).

### Suggested NCIT terms (verify before curating)
- Pharmacotherapy — NCIT:C15986 (generic action term; use with `therapeutic_agent`)
- Specific agents via CHEBI/NCIT `therapeutic_agent`: buprenorphine, methadone, naltrexone, naloxone, nalmefene, lofexidine — look up exact CHEBI/NCIT IDs via OAK before curating (not independently verified in this research pass)
- `therapeutic_modality: SMALL_MOLECULE` for all agents above (none are biologics/ASOs/gene therapies)

---

## 13. Prevention

**Primary prevention:** Cautious/guideline-concordant opioid prescribing (CDC opioid prescribing guidelines), prescription drug monitoring program (PDMP) utilization to reduce diversion/doctor-shopping, patient education on opioid risk at time of prescribing, non-opioid pain-management alternatives where clinically appropriate, and supply-side interventions targeting illicit fentanyl trafficking.

**Secondary prevention (early detection/intervention):** Screening for opioid misuse in primary care and pain-management settings (Opioid Risk Tool, SOAPP), early identification and treatment linkage after a non-fatal overdose event (a recognized high-yield "reachable moment" for MOUD initiation), routine offering of naloxone co-prescription alongside opioid analgesic prescriptions in higher-risk patients.

**Tertiary prevention:** Sustained MOUD engagement to prevent relapse/overdose in individuals with established OUD; treatment of comorbid psychiatric illness to reduce relapse risk; harm-reduction service engagement to reduce infectious and overdose complications in those who continue to use.

**Public health/behavioral/prophylaxis:**
- Community naloxone distribution programs and layperson naloxone-administration training
- Fentanyl/xylazine test-strip distribution
- Syringe service programs (reduce HIV/HCV transmission)
- Public health messaging and prescriber education
- Genetic/prenatal screening is **not** a relevant prevention modality for OUD (unlike Mendelian dismech entries) — this section should not carry a `genetic screening`/carrier-screening annotation.
- Counseling: substance-use-focused counseling and harm-reduction counseling (rather than classical genetic counseling) is the relevant analog here.

**Immunization:** Not directly applicable to OUD itself, though there is active preclinical/early-clinical research into anti-fentanyl and anti-heroin conjugate vaccines intended to blunt drug reward by sequestering the opioid in peripheral circulation before CNS penetration — an experimental, not yet approved, prevention strategy worth flagging as an emerging area if the KB entry includes an "experimental/emerging" treatments or prevention subsection.

---

## 14. Other Species / Natural Disease

OUD as clinically defined (a DSM/ICD-coded behavioral disorder) is fundamentally a **human diagnostic construct** — there is no well-characterized naturally occurring, spontaneous veterinary analog analogous to how, e.g., feline hypertrophic cardiomyopathy naturally recapitulates a human cardiomyopathy. Companion animals (dogs, cats) receiving therapeutic opioids for pain management can develop pharmacological tolerance and physical dependence with abrupt discontinuation producing a withdrawal syndrome, but this reflects the conserved pharmacology of the mu-opioid receptor system rather than a documented spontaneous behavioral-addiction disease entity in veterinary medicine, and is not indexed in OMIA (Online Mendelian Inheritance in Animals) as a natural disease. This section is therefore best modeled in the KB primarily via the **Model Organisms** section (induced/self-administration models) rather than a "natural disease in other species" entry — flag this explicitly as an evidence gap/not-applicable rather than fabricating a veterinary natural-disease citation.

**Orthologous genes:** OPRM1 orthologs are broadly conserved across mammals (mouse *Oprm1*, rat *Oprm1*, rhesus macaque *OPRM1*) and are the basis for cross-species pharmacological/behavioral translational work (Section 15).

**Comparative pathology/evolutionary conservation:** The mu-opioid receptor system and its coupling to mesolimbic dopaminergic reward circuitry is deeply conserved across mammals, which is what makes rodent and non-human-primate models mechanistically informative despite the absence of a natural spontaneous disease analog.

---

## 15. Model Organisms

OUD research relies almost entirely on **induced** models (pharmacological/behavioral induction of dependence-like states) rather than spontaneous genetic models, reflecting the disorder's nature as arising from an environmental exposure (opioid administration) acting on a polygenic-susceptibility background.

**Rodent models:**
- **Operant intravenous opioid self-administration** (rat, mouse) — the gold-standard behavioral model for studying reinforcement, escalation of intake, and relapse/reinstatement after extinction; used extensively to screen candidate MOUD pharmacotherapies.
- **Conditioned place preference (CPP)** — a Pavlovian-conditioning paradigm measuring opioid reward value without requiring self-administration training.
- **Naloxone-precipitated withdrawal** — chronic morphine/fentanyl exposure followed by naloxone challenge to quantify withdrawal severity via somatic signs (jumping, wet-dog shakes, diarrhea, ptosis, teeth chattering in mice/rats) — the standard model for withdrawal pharmacology and the mechanistic LC-hyperactivity studies described in Section 6.
- **Oprm1 knockout mice** — abolish morphine reward, analgesia, and physical dependence/withdrawal, foundational genetic evidence establishing MOR as necessary for opioid reinforcement (classic Kieffer-lab work).
- **Humanized OPRM1 A118G knock-in mice** — carry the human risk-associated coding variant to study its functional/behavioral/circuit consequences directly in vivo; used in the spatial-transcriptomics and neural-connectivity studies cited in Section 6 (Mague et al. and follow-on work; PMC12393594, PMC10866092).
- Chronic morphine tolerance/dependence models in rat locus coeruleus preparations — used to dissect the cAMP/PKA-upregulation mechanism of dependence described above.

**Non-human primate models:** Rhesus macaque intravenous opioid self-administration/reinstatement studies provide higher translational fidelity for reward/relapse pharmacology and are used particularly in medications-development research (e.g., evaluating candidate anti-relapse pharmacotherapies) given closer neuroanatomical and pharmacokinetic similarity to humans.

**Other model systems:** Zebrafish and invertebrate (Drosophila, C. elegans) models are used more for conserved-pathway/high-throughput genetic screening of opioid-response genes than as disease models per se; human iPSC-derived neuronal models (including OPRM1-variant iPSC lines) have been used to study synaptic-function consequences of the A118G variant in a human cellular context, complementing the mouse in vivo work.

**Model limitations:** No rodent or primate model fully recapitulates the human DSM behavioral-criteria construct (craving, social/occupational impairment) — these models capture physiological dependence, reinforcement, and withdrawal robustly, but the "compulsive use despite negative consequences" and subjective-craving dimensions of the human disorder are only partially modeled (e.g., via extended-access self-administration paradigms and punishment-resistant responding paradigms designed to approximate compulsivity). This human-model-fidelity gap is worth flagging explicitly as a `HUMAN_MODEL_MISMATCH`-type discussion if this entry is later built out with `mechanistic_hypotheses`, per the project's convention for model-system evidence whose translational validity to human behavior is uncertain.

---

## Summary of Key Ontology-Term Candidates (all require OAK verification before KB use)

| Domain | Candidate term | Notes |
|---|---|---|
| MONDO | MONDO:0001225 | opioid use disorder — verify exact label/scope match |
| OMIM | 613459 | Opioid Dependence, Susceptibility to (candidate-gene entry) |
| Gene | hgnc:8156 (OPRM1) | primary candidate gene |
| Gene | FURIN, KDM4A, CPT2, CD47, SLC5A11 | GWAS risk loci — resolve HGNC IDs before use |
| GO | response to morphine; G protein-coupled opioid receptor signaling; adenylate cyclase-inhibiting GPCR signaling pathway (GO:0007193) | verify exact IDs/labels |
| CL | dopaminergic neuron (CL:0000700); medium spiny neuron (CL:0000750); microglial cell (CL:0000129); astrocyte (CL:0000127) | core reward/glial cell types |
| UBERON | ventral tegmental area (UBERON:0002550); nucleus accumbens (UBERON:0001882); locus coeruleus (UBERON:0002037); amygdala (UBERON:0001876) | core circuitry |
| CHEBI | morphine, fentanyl, heroin (diacetylmorphine), methadone, buprenorphine, naloxone, naltrexone | resolve exact CHEBI IDs before curating `therapeutic_agent` |
| NCIT | Pharmacotherapy (NCIT:C15986) | generic treatment_term; pair with resolved `therapeutic_agent` |

---

## Sources

- [U.S. Overdose Deaths Drop 26.9% in 2024 — PTTC Network](https://pttcnetwork.org/news/u-s-overdose-deaths-drop-26-9-in-2024/)
- [Opioid Overdose Deaths: National Trends and Variation by Demographics and States — KFF](https://www.kff.org/mental-health/opioid-overdose-deaths-national-trends-and-variation-by-demographics-and-states/)
- [Drug Overdose Deaths in the United States, 2023–2024 — CDC NCHS Data Brief 549](https://www.cdc.gov/nchs/products/databriefs/db549.htm)
- [Products - Vital Statistics Rapid Release - Provisional Drug Overdose Data — CDC](https://www.cdc.gov/nchs/nvss/vsrr/drug-overdose-data.htm)
- [Statement from CDC's National Center for Injury Prevention and Control on Provisional 2024 Overdose Death Data](https://www.cdc.gov/media/releases/2025/2025-statement-from-cdcs-national-center-for-injury-prevention-and-control-on-provisional-2024.html)
- [OPRM1 rs1799971 polymorphism and opioid dependence: evidence from a meta-analysis — PubMed](https://pubmed.ncbi.nlm.nih.gov/23651028/?dopt=Abstract)
- [Association of OPRM1 Functional Coding Variant With Opioid Use Disorder: A Genome-Wide Association Study — PubMed](https://pubmed.ncbi.nlm.nih.gov/32492095/)
- [Spatial transcriptomics reveals distinct cell type dynamics following opioid dependence in mice with Oprm1 A118G — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12393594/)
- [Neural Network Connectivity Following Opioid Dependence Altered by OPRM1 A118G — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10866092/)
- [Genome-wide analyses reveal shared genetic architecture between OUD and general cognitive ability — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11831617/)
- [GWAS in European and African ancestry and multi-trait analysis of OUD identifies 19 independent risk loci — Molecular Psychiatry](https://www.nature.com/articles/s41380-022-01709-1)
- [GWAS of problematic opioid prescription use in 132,113 23andMe participants — Molecular Psychiatry](https://www.nature.com/articles/s41380-021-01335-3)
- [GWAS of problematic opioid prescription use — PubMed](https://pubmed.ncbi.nlm.nih.gov/34728798/)
- [opioid use disorder — Wikidata (MONDO_0001225)](https://www.wikidata.org/wiki/Q1639178)
- [Mondo Disease Ontology — Monarch Initiative](https://mondo.monarchinitiative.org/)
- [Is Buprenorphine More Effective and Safer Than Other Medical Treatments for Managing Opioid Withdrawal? A Cochrane Review Summary — NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK589922/)
- [Relative effectiveness of medications for opioid-related disorders: systematic review and network meta-analysis — PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0266142)
- [Evaluating Treatment Options for Opiate Use Disorder: Meta-Analysis of Buprenorphine-Naloxone and Extended-Release Naltrexone — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12421290/)
- [Buprenorphine versus methadone for opioid dependence: systematic review and meta-analysis — Lancet Psychiatry](https://www.thelancet.com/journals/lanpsy/article/PIIS2215-0366(23)00095-0/abstract)
- [Buprenorphine-Naloxone for OUD: Reduction in Mortality and Increased Remission — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11610725/)
- [The role of mesolimbic circuitry in aversive signaling and opioid dependence — Neuron](https://www.cell.com/neuron/abstract/S0896-6273(25)00625-7)
- [Craving in Opioid Use Disorder: From Neurobiology to Clinical Practice — PubMed](https://pubmed.ncbi.nlm.nih.gov/31543832/)
- [Mu-opioid and nociceptin receptors show divergent, cell-type-specific actions in the mesocorticolimbic reward system — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13106015/)
- [The neural circuits and signalling pathways of opioid use disorder — Nature Reviews Neuroscience](https://www.nature.com/articles/s41583-025-00982-7)
- [SAMHSA releases new 2024 data on rates of mental illness and substance use disorder — NACo](https://www.naco.org/news/samhsa-releases-new-2024-data-rates-mental-illness-and-substance-use-disorder-us)
- [Key Substance Use and Mental Health Indicators: 2024 NSDUH — SAMHSA](https://www.samhsa.gov/data/sites/default/files/reports/rpt56287/2024-nsduh-annual-national/2024-nsduh-annual-national-html-071425-edited/2024-nsduh-annual-national.htm)
- [NSDUH Data Spotlight: Medications for Opioid Use Disorder Among Adults with OUD — SAMHSA CBHSQ](https://www.samhsa.gov/data/report/nsduh-2022-2024-moud)
- [Mechanisms, diagnosis, prevention and management of perioperative opioid-induced hyperalgesia — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8023328/)
- [Opioid withdrawal: role in addiction and neural mechanisms — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11166123/)
- [Molecular and cellular basis of mu-opioid receptor signaling: mechanisms underlying tolerance and dependence development — Frontiers](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1597922/full)
- [Neonatal Abstinence Syndrome — StatPearls / NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK551498/)
- [Neonatal Abstinence Syndrome and Maternal Opioid-Related Diagnoses in the US, 2010–2017 — PubMed](https://pubmed.ncbi.nlm.nih.gov/33433576/)
- [The Epidemic of Neonatal Abstinence Syndrome — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5827164/)
- [Opioids in Pregnancy and Neonatal Abstinence Syndrome — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4628571/)
- [Reviewing the Impact of Maternal Opioid Use Disorder on Fetal Development and Long-Term Pediatric Health Outcomes — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11583522/)
- [Genetic and Epigenetic Approaches to Opioid Use Disorder — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12571026/)
- [Genetics of substance use disorders: a review — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8477224/)
- [A brief review of the genetics and pharmacogenetics of opioid use disorders — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5741106/)
- [Whole-exome sequencing study of opioid dependence — Translational Psychiatry](https://www.nature.com/articles/s41398-025-03578-y)
- [Contribution of BDNF and DRD2 genetic polymorphisms to continued opioid use in methadone treatment — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4672523/)
- [Prevalence of mental disorders among people with opioid use disorder: systematic review and meta-analysis — PubMed](https://pubmed.ncbi.nlm.nih.gov/35797876/)
- [Comorbid Post-Traumatic Stress Disorder and Opioid Dependence — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5669522/)