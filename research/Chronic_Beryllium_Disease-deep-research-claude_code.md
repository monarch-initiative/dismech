---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-16T23:27:57.714697'
end_time: '2026-07-16T23:32:56.655380'
duration_seconds: 298.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chronic Beryllium Disease
  mondo_id: ''
  category: Respiratory Disease
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
  - claude-opus-4-8
  web_search_requests: 10
  num_turns: 16
  total_cost_usd: 2.68482825
  session_id: f4d7111d-2b66-4d63-9eee-1f9da06540d1
  stop_reason: end_turn
citation_count: 13
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chronic Beryllium Disease
- **MONDO ID:**  (if available)
- **Category:** Respiratory Disease

## Research Objectives

Please provide a comprehensive research report on **Chronic Beryllium Disease** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

Alright, I've got a solid citation spine. Here's the full report. sup — quick note before we dive in: the science below is cited hard, but per the dismech reference SOP, treat every snippet as a *lead* until you've run `just fetch-reference` and confirmed the quote is an exact substring. I've flagged the PMIDs I'm most confident in and paraphrased where I couldn't hold an exact quote in hand.

---

# Chronic Beryllium Disease — Comprehensive Research Report

## 1. Disease Information

Chronic beryllium disease (CBD, "berylliosis") is a granulomatous interstitial lung disease driven by a beryllium-specific, cell-mediated (delayed-type, Type IV) immune response to inhaled beryllium. Think of it as the immune system deciding a chunk of metal is a permanent enemy it can't digest and building little fortified walls (granulomas) around it forever — a grudge that slowly stiffens the lung. It's the textbook gene-environment disease: you need both the exposure *and* the right immune-presentation genotype.

**Key identifiers:**
- **MONDO:** MONDO:0015274 (chronic beryllium disease) — already in the entry.
- **MeSH:** D001607 ("Berylliosis").
- **ICD-10:** J63.2 (Berylliosis).
- **ICD-11:** under occupational/inorganic-dust pneumoconioses (CA60.1 region) — *verify the exact leaf against the current ICD-11 browser; codings have shifted.*
- **OMIM:** No Mendelian OMIM entry — CBD is a complex susceptibility trait, not a single-gene disease. The relevant genetics live in HLA-DPB1 allele associations, not an OMIM disease number.
- **Orphanet:** A rare-disease entry exists for berylliosis; confirm the ORPHA number in the current Orphadata pull rather than trusting memory.

**Synonyms:** berylliosis, chronic berylliosis, chronic beryllium lung disease, beryllium granulomatosis. (The entry's synonym list is good.)

**Data derivation:** Disease-level, aggregated. The knowledge here comes from occupational cohort studies (nuclear-weapons, aerospace, machining, ceramics workers), medical-surveillance registries (BeLPT screening programs at DOE facilities), immunology/structural-biology studies, and the 2014 ATS official statement — not from a single-patient EHR source.

---

## 2. Etiology

**Primary cause (environmental):** Inhalation of airborne beryllium — dust, fume, or fine particulate — is the *sole* necessary exposure. No beryllium, no CBD. It's an occupational/environmental toxicant acting as an immunogen (CHEBI: beryllium / beryllium(2+) cation; ECTO: exposure to beryllium). The entry correctly lists the at-risk industries: beryllium ore extraction and metal machining, aerospace/defense, nuclear-weapons and reactor work, electronics and semiconductors, dental-alloy and ceramics fabrication, and metal recycling.

Crucially, and unlike the classic fibrogenic pneumoconioses (silicosis, asbestosis), **risk is not simply cumulative-dose-dependent**. Even brief or low-level exposures can sensitize a genetically susceptible person; particle size, solubility, and surface area strongly modulate immunogenicity. Take-home ("paraoccupational") exposure on work clothes and near-facility community exposure are documented.

**Genetic risk factors:**
- **HLA-DPB1 Glu69** is the dominant heritable risk factor. Alleles encoding glutamic acid at position 69 of the DPβ chain (HLA-DPB1*02:01, *17:01, *06:01, etc.) markedly raise risk of both sensitization and disease. Richeldi et al. (Science 1993, **PMID:8105536**) — the founding observation: "*97% [of CBD cases] expressed the HLA-DPB1\*0201-associated glutamic acid (unaffected population, 30%; P < 0.001) at residue 69.*"
- Higher-affinity Glu69 alleles (notably **\*17:01**) and **gene copy number / expression level** further stratify risk (see McCanlies, Silveira, and the E69 genotype-exposure work, e.g. **PMC8760148**).
- A minority susceptibility route via **HLA-DR** (glutamate at DRβ position 71, and an HLA-DRPheβ47 marker in Glu69-negative individuals; **PMC1198259**) exists for the ~15–20% of patients lacking DP-Glu69.

**Environmental/host modifiers:** Higher airborne concentration, respirable particle fraction, and soluble beryllium salts increase risk; smoking is *not* a clear risk factor for CBD itself but suppresses BeLPT responses (see §10). Age, sex, and family history are not established independent risk factors beyond the HLA genetics.

**Protective factors:** Genetically, **absence of a Glu69 allele** is the main "protective" state — DP molecules lacking Glu69 cannot coordinate Be²⁺ and don't present it (mechanistic basis in §6). Environmentally, protection is entirely about exposure reduction: enclosed processes, wet machining, respiratory protection, and the lowered **OSHA permissible exposure limit of 0.2 µg/m³ (8-hr TWA)** under the 2017 final rule (**PMID:28071878**). No dietary/nutritional protective factor is established.

**Gene–environment interaction:** CBD is arguably the cleanest human example of a defined HLA-restricted gene × environment interaction — a specific MHC-II pocket residue (Glu69) is *required* to convert an inhaled metal into a T-cell antigen. Neither factor alone produces disease.

---

## 3. Phenotypes

CBD is insidious and adult-onset (occupational latency of years to decades). Severity and progression are variable. Suggested HP terms (the entry already carries most of these):

| Phenotype | HP term | Type | Notes on frequency/course |
|---|---|---|---|
| Exertional dyspnea | HP:0002094 (Dyspnea) | Symptom | Most common presenting symptom; progressive |
| Chronic nonproductive cough | HP:0031246 | Symptom | Characteristic early symptom; chronic |
| Fatigue / reduced exercise tolerance | HP:0012378 | Symptom | Common constitutional |
| Unintentional weight loss | HP:0001824 | Symptom | Systemic granulomatous feature |
| Chest pain/discomfort | HP:0100749 | Symptom | Variable |
| Non-caseating pulmonary granulomas | HP:0012220 | Histopathology | Pathological hallmark; indistinguishable from sarcoid |
| Pulmonary granulomatosis | HP:0030250 | Histopathology | Interstitial distribution |
| Interstitial pneumonitis | HP:0006515 | Histopathology | Mononuclear infiltrate |
| Pulmonary fibrosis | HP:0002206 | Radiographic/histo | Advanced disease; progressive |
| Restrictive ventilatory defect (↓DLCO) | HP:0002091 | Lab/PFT | Restrictive pattern with reduced diffusing capacity; obstructive/mixed also seen |
| Mediastinal/hilar lymphadenopathy | HP:0100721 | Radiographic | Common; often less bulky than sarcoid |
| Digital clubbing | HP:0100759 | Physical sign | Advanced fibrotic disease |

Additional phenotypes worth considering for completeness: **exercise-induced hypoxemia / reduced gas exchange** (often the earliest physiologic abnormality, sometimes preceding resting PFT changes — cardiopulmonary exercise testing catches it first), **skin granulomas / beryllium ulcers** at sites of dermal beryllium implantation (a documented extrapulmonary manifestation), and in end-stage disease **cor pulmonale / right heart failure** (HP:0001648-ish pulmonary hypertension secondary to fibrosis). Beryllium can also produce contact dermatitis. Hepatic and other systemic granulomas are rare.

**Onset/severity/progression:** adult-onset; severity mild→severe and variable; course insidious then chronic-progressive in the subset that advances; frequency among affected individuals for the core respiratory phenotypes is high but the entry appropriately omits precise `frequency:` bands where quantitative support is thin.

**Quality-of-life impact:** progressive exertional limitation, oxygen dependence in advanced disease, and lifelong therapy burden. No CBD-specific validated QOL instrument is standard; generic respiratory/ILD tools (SF-36, St. George's Respiratory Questionnaire) are used in studies — flag as not-CBD-specific.

---

## 4. Genetic / Molecular Information

- **Susceptibility gene:** **HLA-DPB1** (HGNC — the entry uses `hgnc:4940`; verify this HGNC number resolves to HLA-DPB1, as HLA HGNC IDs are easy to transpose). Also **HLA-DPA1** (the paired α chain), and **HLA-DRB1** for the minority DR-restricted route.
- **Risk "variants":** these are **classical HLA alleles / polymorphic residues**, not ClinVar-style pathogenic point mutations. The functional unit is the **codon-69 residue of DPB1** (Glu69 = risk; non-Glu69 = low risk). This is a germline susceptibility polymorphism, not somatic, and not "pathogenic" in the ACMG/AMP sense — it's an immune-response allele. So most of the ClinVar/gnomAD/COSMIC machinery in the template is **N/A**; the right resources are the **IMGT/HLA database** and HLA allele-frequency references.
- **Functional consequence:** *gain of an antigen-presentation function* — Glu69 creates an acidic pocket that binds Be²⁺. Mechanistically it's a "toxic gain of presentation," not loss-of-function.
- **Dose/copy effect:** susceptibility scales with Glu69 **allele copy number and DP surface expression** (homozygotes and high-expressing haplotypes at higher risk).
- **Modifier genes:** candidate immunogenetic modifiers include **TNF-α promoter polymorphisms (−308)**, **TGF-β1**, and other cytokine variants associated with disease severity/progression in some cohorts, though replication is uneven — cite cautiously.
- **Epigenetics / chromosomal abnormalities:** No established disease-defining DNA-methylation signature, and no aneuploidy/translocation involvement. Treat as **not applicable / not established**.

---

## 5. Environmental Information

- **Environmental factor:** beryllium and beryllium-containing compounds (metal, oxide, alloys such as copper-beryllium, ceramics) as respirable dust/fume. CTD is a good structured source for beryllium–gene interactions.
- **Lifestyle:** No causal lifestyle factor. **Smoking** is a notable confounder — cigarette smoke *suppresses* lymphocyte proliferation and can cause **false-negative BeLPT**, so it affects detection more than causation.
- **Infectious agents:** None. CBD is non-infectious. (This is a key contrast with tuberculosis, whose caseating granulomas it superficially resembles.)

---

## 6. Mechanism / Pathophysiology

This is the heart of the entry and it's already modeled cleanly against the `granuloma_formation` module. The causal chain:

**Step 1 — Deposition & uptake (trigger).** Inhaled beryllium particles deposit in distal airways/alveoli and are engulfed by **alveolar macrophages (CL:0000583)** and **dendritic cells (CL:0000451)**. Beryllium is poorly soluble and biopersistent — the macrophage cannot degrade or clear it, so it becomes the "persistent indigestible stimulus" that converts a normal, self-limited macrophage response into a chronic one. (Conforms to `granuloma_formation#Persistent Indigestible Stimulus`.) GO: chronic inflammatory response (GO:0002544).

**Step 2 — Neoantigen formation (mechanism).** Ionic **Be²⁺** is incorporated into the peptide-binding groove of HLA-DP, coordinated by acidic residues of the DPβ chain *and* a bound self-peptide. This is the structural punchline from Clayton et al. (**Cell 2014, PMID:24995984**): "*the T cell ligand is created when a Be2+ cation becomes buried in an HLA-DP2/peptide complex, where it is coordinated by both MHC and peptide acidic amino acids… the TCR does not interact with the Be2+ itself, but rather with surface changes induced by the firmly bound Be2+.*" So beryllium is **not a classical covalent hapten** — it's buried at the MHC–peptide interface, remodeling the surface into a neoantigen. This is what the paper means by "bridging allergic hypersensitivity and autoimmunity." GO: antigen processing and presentation via MHC class II (GO:0002495).

**Step 3 — Glu69-restricted presentation (mechanism).** Presentation is restricted to DP molecules bearing **Glu69** (the acidic residue that coordinates the cation). Amicosante/Fontenot (**PNAS 2000, PMID:11050177**): beryllium presentation to CD4⁺ T cells "*underlies disease-susceptibility HLA-DP alleles.*" Bill et al. (**J Immunol 2005, PMID:16272364**) pinned it to a single β-chain residue — "*beryllium presentation… is dependent on a single amino acid residue of the MHC class II beta-chain*" (Glu69 on DP, the homologous Glu71 on DR). The crystal structure of HLA-DP2 (**PNAS 2010, PMID:20356827**) showed the unique solvent-exposed acidic pocket.

**Step 4 — CD4⁺ T-cell sensitization (mechanism).** TCR recognition drives clonal expansion of **beryllium-specific CD4⁺ memory/effector T cells** (CL:0000545 T-helper 1 cell as the closest CL anchor). This expanded population *is* beryllium sensitization (BeS) — the state that precedes organ disease and is measured by the BeLPT. GO: T cell proliferation (GO:0042098). **Sensitization is necessary but not sufficient** for CBD.

**Step 5 — Compartmentalized Th1 cytokine response (amplifier).** On re-encounter in the lung, these cells polarize to Th1 and secrete **IFN-γ, TNF, and IL-2**; they accumulate as effector-memory Th1 cells in the bronchoalveolar space (Fontenot, JCI 2002 — target-organ localization of memory CD4⁺ T cells; Fontenot & Maier review, **PMID:18317020**). GO: type II interferon production (GO:0032609), tumor necrosis factor production (GO:0032640).

**Step 6 — Macrophage recruitment & activation (amplifier).** IFN-γ + TNF classically activate lung macrophages and recruit monocytes; **TNF is the non-redundant organizer** of the granulomatous response. (Conforms to `granuloma_formation#Th1 and TNF-Driven Macrophage Recruitment and Activation`.) GO: macrophage activation (GO:0042116).

**Step 7 — Epithelioid/giant-cell transformation (central effector).** Macrophages become **epithelioid cells (CL:0002150)** and fuse into **multinucleated giant cells (CL:0000647)** — the asteroid- and Schaumann-body-containing giant cells shared with sarcoid. GO: syncytium formation by cell-cell fusion (GO:0000768).

**Step 8 — Non-caseating granuloma assembly (effector).** Compact non-caseating granulomas — epithelioid/giant-cell core cuffed by CD4⁺ T cells — form along bronchovascular bundles, interlobular septa, and hilar nodes. *No central caseous necrosis*, which is what makes CBD histologically indistinguishable from sarcoidosis. (Conforms to `granuloma_formation#Organized Granuloma Assembly`.)

**Step 9 — Progressive fibrosis (consequence).** Because the stimulus can't be cleared, the response persists and, in a subset, drives interstitial fibrosis — **fibroblast (CL:0000057)** recruitment and collagen deposition (GO:0030199) → restrictive defect, impaired gas exchange, respiratory failure, cor pulmonale. (Conforms to `granuloma_formation#Tissue Containment versus Destruction and Fibrosis`.)

**Regulatory arm worth noting:** Regulatory T cells modulate granuloma intensity in the HLA-DP2 mouse model (**PMID:24912188**) — a mechanistic knob that partly explains why only some sensitized people progress.

**Molecular profiling:** BAL from CBD patients shows a **compartmentalized Th1 signature** (high IFN-γ, TNF, IL-2; oligoclonal TCR expansion, e.g. Vβ-restricted repertoires). No routine metabolomic/lipidomic/proteomic diagnostic signature is established; single-cell/BAL immunophenotyping is a research tool, not clinical.

---

## 7. Anatomical Structures Affected

- **Primary organ:** lung (UBERON:0002048), specifically the pulmonary interstitium, alveoli/alveolar wall (UBERON:0002299 alveolus), distal airways, and bronchovascular bundles.
- **Regional lymphatics:** hilar and mediastinal lymph nodes (UBERON:0002509 mesenteric-node is wrong — use thoracic/hilar lymph node terms; UBERON:0002509 not applicable; consider UBERON:0000029 lymph node with a mediastinal/hilar qualifier).
- **Body system:** respiratory (with secondary cardiovascular involvement — pulmonary hypertension/cor pulmonale in advanced fibrosis).
- **Secondary/extrapulmonary:** skin (granulomas, ulcers, contact dermatitis; UBERON:0002097), and rarely liver, spleen, myocardium, salivary glands, and other sites — systemic granulomatosis is uncommon but reported.
- **Tissue/cell level:** epithelioid and multinucleated giant-cell macrophages, CD4⁺ Th1 lymphocytes, fibroblasts/myofibroblasts, alveolar macrophages, dendritic cells (CL terms as above).
- **Subcellular:** antigen presentation is at the plasma-membrane MHC-II complex (GO:0042613 MHC class II protein complex); phagolysosomal handling of biopersistent particle in macrophages (GO:0005764 lysosome). No mitochondrial/ER-specific compartment is disease-defining.
- **Laterality:** bilateral, diffuse, typically **upper-and-mid-zone-predominant** on imaging (like sarcoid), often with an upper-lobe fibrotic bias in advanced disease.

---

## 8. Temporal Development

- **Onset:** adult; occupational. **Latency is long and variable** — months to >20–40 years after first exposure, with cases documented decades after exposure ceased.
- **Onset pattern:** insidious/chronic. Acute beryllium disease (a distinct, high-dose chemical pneumonitis) is now essentially historical and mechanistically different — worth explicitly distinguishing from CBD in the entry if not already.
- **Stages:** subclinical sensitization (BeS) → early granulomatous CBD (often asymptomatic, abnormal biopsy/BAL) → symptomatic granulomatous disease → fibrotic end-stage.
- **Progression rate:** variable; **BeS → CBD conversion runs roughly 6–8%/year** in the Newman longitudinal cohort (**PMID:15374840**: 55 sensitized workers, mean follow-up 4.8 yr; ~31% developed CBD; the remaining ~69% stayed sensitized without disease), and a **systematic review put progression at ~3.2–9.2%/year** (**PMID:22705916**). Roughly half of sensitized individuals already have CBD at their first thorough evaluation.
- **Course:** chronic, lifelong. Once fibrosis is established it is **irreversible** — corticosteroids don't reverse scar.
- **Remission:** no spontaneous cure; treatment can stabilize/partially improve inflammation but disease "recrudesces with reduction of the corticosteroid dose," so relapse on tapering is characteristic.
- **Critical window:** exposure cessation *before* fibrosis is the key intervention window; early identification via surveillance BeLPT is the point of maximum leverage.

---

## 9. Inheritance and Population

- **Epidemiology:** CBD is uncommon and occupational. Cross-sectional prevalences among exposed worker cohorts: **beryllium sensitization ~0.8–12%** and **CBD ~0.1–8%**, depending on job/exposure intensity (machinists and ceramics workers highest; lower-exposure nuclear R&D sites ~2–3% sensitization). Population-level prevalence in the general (non-exposed) public is effectively negligible.
- **Inheritance pattern:** **Not Mendelian.** It's a **multifactorial/HLA-restricted susceptibility** requiring environmental exposure. The heritable component is the HLA-DPB1 Glu69 (and minor DR) association — best modeled with `relationship_type: SUSCEPTIBILITY`, exactly as the entry does. Penetrance, expressivity, anticipation, mosaicism, founder effects, consanguinity, and carrier frequency in the classical genetics sense are **N/A**; the analogous concept is **Glu69 allele frequency** (~30–40% of the general population carries a Glu69 allele, vs ~80–97% of CBD patients — i.e., the allele is common but disease requires exposure + likely higher-affinity alleles/copy number).
- **Demographics:** determined by **occupation, not ethnicity** — exposed workforces skew historically male, but that reflects the industries, not a biological sex effect. Geographic distribution tracks beryllium industry (US DOE nuclear-weapons complex, aerospace hubs, and beryllium-processing regions). No endemic geography in the infectious sense.

---

## 10. Diagnostics

**The diagnostic dyad:** documented beryllium exposure **+** demonstrated beryllium-specific immune sensitization **+** granulomatous pathology. Per the **2014 ATS official statement (PMID:25398119)**:

- **Beryllium Lymphocyte Proliferation Test (BeLPT)** — the pivotal test. Patient blood (or BAL) lymphocytes are cultured with beryllium salts; proliferation indicates sensitization. Blood BeLPT single-test **sensitivity ~61.5%, specificity ~90.8%**; split-sample (duplicate) testing raises sensitivity to ~76% at some cost to specificity. BAL BeLPT is more sensitive for organ disease but can be falsely negative in smokers or the immunosuppressed. This is the test that distinguishes CBD from sarcoidosis (which is BeLPT-negative).
- **Bronchoscopy with transbronchial (or surgical) biopsy** — to demonstrate **non-caseating granulomas / mononuclear interstitial infiltrate**; BAL typically shows a **lymphocytosis with elevated CD4:CD8 ratio** and a positive BAL BeLPT.
- **Imaging:** chest CT/HRCT — upper/mid-zone nodular and reticular opacities, ground-glass, septal thickening, hilar/mediastinal adenopathy; can be normal early. RadLex terms apply.
- **Pulmonary function testing:** restrictive (or obstructive/mixed) pattern with **reduced DLCO**; **cardiopulmonary exercise testing** detects gas-exchange abnormality earliest.
- **Genetic testing:** **HLA-DPB1 Glu69 typing** is used in research and risk stratification but is **not a stand-alone diagnostic** — the allele is too common in the general population. It supports susceptibility, not diagnosis.
- **Differential diagnosis:** **sarcoidosis** (the big one — clinically/histologically identical; the exposure history + BeLPT is what separates them), tuberculosis and other infectious granulomas (caseating), hypersensitivity pneumonitis, other pneumoconioses, granulomatosis with polyangiitis.
- **Screening:** workplace medical-surveillance BeLPT programs (DOE, aerospace) for asymptomatic exposed workers — the standard secondary-prevention tool. LOINC codes exist for BeLPT-type lymphocyte proliferation results.

Omics/liquid-biopsy diagnostics: **not clinically applicable**; research only.

---

## 11. Outcome / Prognosis

- **Natural history:** variable — some patients remain stable for years with no treatment; a subset progresses to fibrotic, disabling disease and respiratory failure.
- **Mortality:** CBD can be fatal in advanced fibrotic disease (respiratory failure, cor pulmonale); it is a compensable occupational disease with documented excess mortality in exposed cohorts, but it is not uniformly lethal. No clean 5-/10-year survival figure applies across the disease spectrum — flag as "variable, stage-dependent."
- **Morbidity/disability:** progressive exertional limitation, oxygen dependence, and lifelong immunosuppressive therapy burden drive substantial disability in progressors.
- **Complications:** pulmonary fibrosis, pulmonary hypertension, cor pulmonale, respiratory failure, corticosteroid/immunosuppression side effects, and (rarely) systemic granulomatous involvement.
- **Recovery:** inflammation is partially reversible with therapy; **fibrosis is not**. Exposure cessation improves the trajectory but doesn't erase established sensitization.
- **Prognostic factors:** degree of fibrosis at diagnosis, DLCO/exercise gas exchange, extent of granulomatous burden, and continued vs ceased exposure. TNF-α and severity-associated cytokine polymorphisms are candidate molecular prognostics (unvalidated for clinical use).

---

## 12. Treatment (MAXO/NCIT terms noted)

The entry's treatment block is solid. Detail:

1. **Beryllium exposure cessation** — the essential first step for anyone sensitized or diseased; removes the antigen driving the T-cell response. (Not a drug — best captured as removal-from-exposure; NCIT:C49236 Therapeutic Procedure is a reasonable anchor; there isn't a crisp MAXO "exposure avoidance" term.)
2. **Systemic corticosteroids (prednisone)** — mainstay pharmacotherapy for symptomatic/progressive disease. Typically 3–6 months then reassess PFTs/gas exchange and taper to lowest effective dose. Suppresses granulomatous inflammation; **cannot reverse fibrosis**; disease recrudesces on taper, so therapy is often lifelong. (CHEBI:8382 prednisone; NCIT:C15986 Pharmacotherapy; MAXO could anchor to corticosteroid/anti-inflammatory therapy.)
3. **Steroid-sparing immunosuppressants** — **methotrexate** (e.g., 7.5 mg weekly with folic acid) and **azathioprine**, adapted from sarcoidosis management, to reduce steroid burden (Current Treatment of CBD review, PMC2774897). (CHEBI:44185 methotrexate.)
4. **TNF-α inhibitors (infliximab)** — used in refractory granulomatous disease; targets the non-redundant TNF amplifier. Maier et al. (**PMID:22974830**) showed infliximab "*modulates an antigen-specific immune response in chronic beryllium disease.*" Benefit is less established than in sarcoidosis and **infection risk (reactivation TB, etc.) is a real concern**. The entry correctly links this to the `Th1 and TNF-Driven Macrophage Recruitment and Activation` node with `INHIBITS`. (NCIT:C20401 Monoclonal Antibody / better: infliximab-specific term if available.)
5. **Supportive care** — supplemental **oxygen** (MAXO:0000950 supportive care), pulmonary rehabilitation, vaccination, comorbidity management.
6. **Lung transplantation** — for end-stage fibrotic CBD refractory to medical therapy (MAXO:0010039 organ transplantation).

**Pharmacogenomics:** none clinically actionable specific to CBD. **Experimental/tolerizing approaches** — antigen-specific tolerance strategies (e.g., recombinant HLA-DP2 tolerizing beryllium-specific pathogenic T cells, PMID region ~16951350 / Falta group) are preclinical and mechanistically interesting but not clinical. No approved gene/cell/RNA therapy.

---

## 13. Prevention

- **Primary prevention:** exposure control is everything — engineering controls (enclosure, local exhaust, wet processing), the **OSHA 0.2 µg/m³ PEL** (2017 final rule, **PMID:28071878**), respiratory protection, dermal protection, and hygiene to prevent take-home exposure. This is the only truly effective lever.
- **Secondary prevention:** **medical-surveillance BeLPT screening** of exposed workers to catch sensitization early and remove sensitized individuals from further exposure before organ disease develops.
- **Tertiary prevention:** in diagnosed CBD, exposure removal + monitoring to slow progression and prevent fibrotic complications.
- **Genetic screening:** **HLA-DPB1 Glu69 pre-employment screening is ethically contentious and not standard** — it risks genetic discrimination, the allele is common, and it has poor positive predictive value. Worth flagging as a live policy debate rather than a recommendation.
- **Immunization / public-health / vector control:** N/A (non-infectious).

---

## 14. Other Species / Natural Disease

- **Natural disease:** No meaningful naturally-occurring CBD in companion animals or wildlife — beryllium exposure is essentially an anthropogenic occupational phenomenon. OMIA has no CBD entry.
- **Comparative biology:** the disease is defined by *human* HLA-DP presentation, which doesn't have a direct wild-animal counterpart. Beryllium *toxicity* can be induced experimentally in animals, but the HLA-restricted immune disease is human-specific.
- **Zoonosis / cross-species transmission:** N/A.

---

## 15. Model Organisms

- **Flagship model — HLA-DP2 transgenic mouse** (Mucosal Immunology 2015, **PMID:26129650**): intratracheal beryllium oxide induces lung mononuclear infiltrates and a **CD4-dependent, beryllium-specific adaptive immune response** in lung and spleen, recapitulating the major features of human CBD; beryllium-responsive CD4⁺ T cells were largely **TCR Vβ6⁺**, and the group defined HLA-DP2-binding **mimotopes** recognized by beryllium-specific T cells even without beryllium present. This is the model that ties the human Glu69 genetics to an in-vivo granulomatous phenotype — evidence_source **MODEL_ORGANISM**.
- **Regulatory-T-cell modulation** in the same HLA-DP2 model (**PMID:24912188**) — Tregs tune granuloma intensity, a mechanistic model for variable progression.
- **In vitro / cellular models:** patient **BAL and blood lymphocyte cultures** (the BeLPT itself is a functional cellular assay), beryllium-specific CD4⁺ T-cell clones, and **recombinant soluble HLA-DP2** for structural/binding work (PNAS 2010, Cell 2014) — evidence_source **IN_VITRO**.
- **Model limitations:** mouse models require the human HLA-DP2 transgene to work at all (mouse MHC-II doesn't present beryllium the human way), and murine granulomas don't fully reproduce human fibrotic end-stage disease — a legitimate **HUMAN_MODEL_MISMATCH** candidate for a discussion block if you want to flag translational caveats. Resources: MGI for the transgenic lines.

---

## Key citations (verify snippets before committing, per the DR/anti-hallucination SOP)

| PMID | What it anchors | Evidence source |
|---|---|---|
| **8105536** | Richeldi, Science 1993 — HLA-DPB1 Glu69 as genetic marker (97% vs 30%) | HUMAN_CLINICAL |
| **11050177** | Amicosante/Fontenot, PNAS 2000 — Be presentation to CD4⁺ underlies DP susceptibility | IN_VITRO |
| **16272364** | Bill, J Immunol 2005 — single β-chain residue (Glu69/Glu71) dependence | IN_VITRO |
| **20356827** | HLA-DP2 crystal structure, PNAS 2010 — the acidic solvent-exposed pocket | IN_VITRO |
| **24995984** | Clayton, Cell 2014 — buried Be²⁺ neoantigen; allergy↔autoimmunity bridge | IN_VITRO |
| **18317020** | Fontenot & Maier — Immunology of CBD review | (review) |
| **25398119** | ATS 2014 official statement — diagnosis/management, BeLPT performance | HUMAN_CLINICAL |
| **15374840** | Newman, AJRCCM 2005 — BeS→CBD progression ~6–8%/yr | HUMAN_CLINICAL |
| **22705916** | Systematic review — progression 3.2–9.2%/yr | HUMAN_CLINICAL |
| **17474035** | Exposure-response, beryllium machining plant | HUMAN_CLINICAL |
| **28071878** | OSHA 2017 final rule — 0.2 µg/m³ PEL | (regulatory) |
| **22974830** | Maier — infliximab modulates antigen-specific response in CBD | HUMAN_CLINICAL |
| **26129650** | HLA-DP2 transgenic mouse model, Mucosal Immunol 2015 | MODEL_ORGANISM |
| **24912188** | Tregs modulate granulomatous inflammation, HLA-DP2 model | MODEL_ORGANISM |

Sources consulted: [Richeldi Science 1993](https://www.science.org/doi/10.1126/science.8105536), [Amicosante PNAS 2000](https://pubmed.ncbi.nlm.nih.gov/11050177/), [Bill J Immunol 2005](https://pubmed.ncbi.nlm.nih.gov/16272364/), [Clayton Cell 2014](https://pubmed.ncbi.nlm.nih.gov/24995984/), [ATS 2014 statement](https://pubmed.ncbi.nlm.nih.gov/25398119/), [Newman AJRCCM 2005](https://www.atsjournals.org/doi/10.1164/rccm.200402-190OC), [systematic review PMID 22705916](https://pubmed.ncbi.nlm.nih.gov/22705916/), [HLA-DP2 mouse model](https://pubmed.ncbi.nlm.nih.gov/26129650/), [Treg mouse model](https://pubmed.ncbi.nlm.nih.gov/24912188/), [infliximab in CBD](https://pubmed.ncbi.nlm.nih.gov/22974830/), [OSHA final rule](https://pubmed.ncbi.nlm.nih.gov/28071878/), [Current Treatment of CBD](https://pmc.ncbi.nlm.nih.gov/articles/PMC2774897/), [E69 genotype-exposure](https://pmc.ncbi.nlm.nih.gov/articles/PMC8760148/).

---

**Bottom line for the curation entry:** the existing `Chronic_Beryllium_Disease.yaml` is already in genuinely good shape — the 9-node pathophysiology chain conforms correctly to `granuloma_formation`, the HLA-DPB1 susceptibility modeling is right, and the treatment/target_mechanisms links are sound. The main *gaps* I'd consider adding, if you want to push completeness: (1) a **BeLPT diagnostic** representation and the **CD4:CD8 BAL lymphocytosis**, (2) explicit **skin granuloma / beryllium ulcer** and **pulmonary hypertension/cor pulmonale** phenotypes, (3) a **prevalence** block (BeS 0.8–12%, CBD 0.1–8% in exposed cohorts; MEASURE_TYPE POINT_PREVALENCE, condition on exposed population in `notes`), (4) an **HLA-DP2 transgenic mouse** model/animal block with `evidence_source: MODEL_ORGANISM`, and (5) maybe a **HUMAN_MODEL_MISMATCH** discussion noting the transgene requirement and incomplete fibrosis in mice. Two small things to double-check mechanically: the **HGNC id for HLA-DPB1** (`hgnc:4940`) and the **hilar/mediastinal lymph node UBERON** term if you add anatomy — those are the kind of easy-to-transpose identifiers the term validator will catch.

Want me to fold any of those additions into the YAML and run the validation stack, or keep this as a research reference for now?