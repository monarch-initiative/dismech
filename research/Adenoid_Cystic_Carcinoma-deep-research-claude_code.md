---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T13:46:10.805376'
end_time: '2026-07-31T13:52:18.860124'
duration_seconds: 368.05
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Adenoid Cystic Carcinoma
  mondo_id: ''
  category: Cancer
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
  web_search_requests: 21
  num_turns: 26
  total_cost_usd: 2.1149992999999996
  session_id: 08830454-df71-5945-9a4b-ec1fa63d3551
  stop_reason: end_turn
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Adenoid Cystic Carcinoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Adenoid Cystic Carcinoma** covering all of the
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

# Adenoid Cystic Carcinoma (ACC): Comprehensive Research Report

## 1. Disease Information

**Overview.** Adenoid cystic carcinoma (ACC) is a rare, histologically distinctive malignant epithelial neoplasm that most commonly arises in the major and minor salivary glands of the head and neck but also occurs in the breast, lacrimal gland, trachea/bronchus, skin, and uterine cervix. It is a **biphasic tumor** composed of malignant epithelial (ductal/luminal) and myoepithelial (abluminal/basaloid) cells, and it is genomically defined by recurrent rearrangements activating the *MYB* transcription-factor family. Clinically, ACC is characterized by an unusual combination of **indolent growth with relentless local infiltration**, a striking propensity for **perineural invasion**, frequent late local recurrence, and delayed distant metastasis (commonly to lung, bone, and liver) that can occur many years to decades after initial diagnosis (PMC3597152, PMC11387731).

**Key identifiers:**
- **MONDO:** MONDO:0004971 (adenoid cystic carcinoma, general); site-specific children include MONDO:0003175 (salivary gland ACC) and MONDO:0003181 (lung ACC) (monarchinitiative.org)
- **ICD-O-3 morphology:** 8200/3 (malignant) — combined with topography codes for site (e.g., C07 parotid gland, C08.0 submandibular gland, C05.0 hard palate, C50.9 breast)
- **ICD-10:** varies by site (e.g., C07, C08.0, C50.91)
- **MeSH:** D003528 (Carcinoma, Adenoid Cystic)
- **OMIM:** No dedicated OMIM phenotype entry exists — ACC is predominantly a **sporadic, somatically driven** malignancy rather than a classic monogenic Mendelian disorder, so it is not catalogued in OMIM the way inherited syndromes are.
- **Orphanet:** site-specific Orphanet entries exist (e.g., ORPHA:213823 for cervical ACC); a general salivary-gland ACC entry is also indexed under Orphanet's rare tumor nomenclature.

**Synonyms:** cylindroma (historical term, now largely reserved for the benign cutaneous adnexal tumor to avoid confusion), adenocystic carcinoma, cribriform carcinoma (older term reflecting histology), "adenoid cystic basal cell carcinoma" (obsolete).

**Evidence provenance:** Most quantitative data on ACC (incidence, survival, treatment response) derive from **aggregated disease-level resources** — national cancer registries (SEER, National Cancer Database), multi-institutional retrospective cohorts, and pooled genomic sequencing cohorts — rather than individual electronic health records, reflecting the tumor's rarity and the resulting reliance on multi-center consortia (e.g., the Adenoid Cystic Carcinoma Research Foundation's genomic sequencing program) (PMC11476411, JCI:128227).

---

## 2. Etiology

**Disease causal factors.** ACC is a genetically/mechanistically driven malignancy rather than one with an established infectious or classical toxic etiology. Its defining molecular event is **activation of the MYB transcription-factor family** — predominantly via a t(6;9)(q22-23;p23-24) chromosomal translocation producing an **MYB-NFIB gene fusion**, first reported by Persson et al. (Proc Natl Acad Sci USA, 2009;106:18740–18744; PMCID PMC2773970). This translocation truncates *MYB*, removing its 3′ untranslated region and thereby escaping microRNA-mediated (miR-15a/16, miR-150) negative feedback regulation, leading to *MYB* overexpression (PMC11387731).

**Genetic risk/causal factors:**
- ***MYB-NFIB* fusion** — the genomic hallmark, detected in ~28–86% of primary ACCs and up to 35% of metastatic ACCs depending on cohort and assay (meta-analysis: Mitani et al., systematic review PMID:30269389). Serves as "a specific and sensitive marker to distinguish ACC from other salivary gland tumors."
- ***MYBL1* (A-MYB) rearrangements** (*MYBL1-NFIB*, *MYBL1-YTHDF3*) — found in *MYB*-fusion-negative tumors (~2.4–8% of cases), mutually exclusive with *MYB* alterations, and reported to skew toward submandibular gland primaries (PMID:29149504, "MYBL1 rearrangements and MYB amplification in breast adenoid cystic carcinomas lacking the MYB-NFIB fusion gene").
- **High-level *MYB* amplification** (copy-number gain) as an alternative, fusion-independent route to *MYB* overexpression.
- **Nonclassical fusions** (*MYB-TGFBR3*, *MYB-RAD51B*) in a small subset (~2.2%) (PMC11387731).
- ***NOTCH1* activating mutations** in the negative regulatory region (NRR) and PEST domain hotspots shared with T-cell acute lymphoblastic leukemia — found in ~13.7–20% of primary tumors and markedly enriched (26.3% vs. 8.5%) in recurrent/metastatic disease (Ferrarotto et al., *J Clin Oncol* 2017;35(3):352-360, DOI:10.1200/JCO.2016.67.5264; Ho et al., genetic hallmarks study, *J Clin Invest* 2019, DOI:10.1172/JCI128227).
- ***TERT* promoter mutations** — present in ~13.1% of recurrent/metastatic ACC and **mutually exclusive** with both *NOTCH1* mutations and *MYB/MYBL1* fusions, suggesting a distinct alternative oncogenic route (JCI:128227).
- Chromatin-remodeling gene alterations enriched in recurrent/metastatic disease relative to primary tumors: *KDM6A* (15.2% vs 3.4%), *KMT2C/MLL3* (14.3% vs 4.0%), *ARID1B* (14.1% vs 4.0%), *ARID1A* (13.7% vs 2.3%) (JCI:128227).
- DNA-damage-repair gene alterations (*ATM*, enriched 6.8% vs 1.7% in recurrent/metastatic disease) (JCI:128227).
- Rare germline predisposition: isolated familial reports associated with germline *BRCA2* mutations, but no established hereditary cancer syndrome accounts for a meaningful fraction of cases; genetic predisposition otherwise plays a limited, largely unproven role.

**Environmental risk factors:**
- **Prior therapeutic ionizing radiation to the head/neck** (e.g., childhood radiotherapy for benign conditions or other malignancies) is the most established environmental/iatrogenic risk factor, with elevated risk manifesting 10–20 years after exposure, attributed to radiosensitivity of salivary gland tissue.
- No consistent association has been demonstrated with tobacco smoking or alcohol consumption — in contrast to most other head and neck carcinomas.
- No established viral or infectious etiology (unlike, e.g., HPV-driven oropharyngeal SCC or EBV-driven nasopharyngeal carcinoma).
- Age and sex: peak incidence in the 4th–6th decades (median age ~58 years per SEER; PMID:39410002), with a female predominance (female:male ratio approximately 3:2, and 63.3% female in the SEER cohort).

**Protective factors:** No specific genetic or environmental protective factors have been established in the literature; this is an area of relative research gap for ACC (in contrast to more common cancers where lifestyle/dietary protective factors are better characterized).

**Gene-environment interactions:** No well-documented gene-environment interaction has been established for ACC; the disease is best modeled as a somatic-driver-defined malignancy with radiation as the principal known extrinsic contributor, acting independently of germline genotype in essentially all reported cases.

---

## 3. Phenotypes

ACC's phenotype spectrum is dominated by mass-effect and neurotropic (perineural) manifestations rather than systemic/laboratory abnormalities, consistent with a locally aggressive solid tumor.

| Phenotype | Type | Onset/course | Frequency/severity | Suggested HPO term |
|---|---|---|---|---|
| Painless or painful mass/swelling (salivary gland, oral cavity, breast, etc.) | Clinical sign | Insidious onset, adult (median ~58y); slowly progressive | Most common presenting sign | HP:0100721 (Neoplasm) / site-specific mass terms |
| Facial/cranial nerve palsy (especially facial nerve, CN VII) | Clinical sign | Subacute-chronic, progressive with perineural spread | Occurs in a meaningful minority, especially with parotid/skull-base disease; strongly associated with perineural invasion | HP:0010628 (Facial palsy) |
| Perineural pain, paresthesia, hypoesthesia, burning sensation | Symptom | Chronic, often precedes imaging-detectable spread | Frequent — described as an "outstanding feature" of ACC due to marked neurotropism | HP:0033046 (Paresthesia) / HP:0025406 (sensory neuropathy-type terms) |
| Trigeminal neuralgia-like pain | Symptom | Chronic | Reported specifically with perineural invasion along V2/V3 | HP:0100659 (Trigeminal neuralgia, related) |
| Dysphagia / difficulty swallowing | Symptom | Progressive with local tumor growth | Occurs with oropharyngeal/base-of-tongue or tracheal ACC | HP:0002015 (Dysphagia) |
| Dyspnea/airway obstruction (with tracheobronchial ACC) | Symptom | Progressive | Site-specific | HP:0002094 (Dyspnea) |
| Nasal obstruction/epistaxis (sinonasal ACC) | Symptom/sign | Progressive | Site-specific | HP:0031417 (Nasal obstruction); HP:0000421 (Epistaxis) |
| Facial numbness | Symptom | Chronic, insidious | Common with perineural infiltration | HP:0007478 (Facial numbness-type terms) |
| Masticatory muscle weakness | Sign | Progressive | With trigeminal motor branch involvement | related to HP:0001324 (Muscle weakness) |
| Local recurrence | Disease course feature | Often years after initial treatment | Reported in roughly one-third to one-half of patients over long follow-up | n/a (disease-course descriptor) |
| Distant metastasis (lung most common, then bone, liver) | Disease course feature | Very late — median time to distant recurrence ~50 months, and can occur >10-15 years post-diagnosis | Occurs in up to ~40-50% of patients over long-term follow-up; lung is site in the majority of distant metastases | HP:0002090 (Pulmonary metastasis-type descriptor); relevant UBERON/anatomical terms for metastatic sites |

**Age of onset:** ACC spans the first to ninth decades but is most frequent in middle-aged and older adults (peak 45–60 years); rare pediatric cases occur (PMC11387731).

**Severity/progression:** Best characterized as "indolent but aggressive" — slow radiographic growth juxtaposed with a high propensity for perineural spread, positive margins, and eventual distant relapse. Course is typically **chronic and progressive** with a **prolonged natural history** (median overall survival reported around 16 years in some cohorts) but a persistent risk of recurrence that does not plateau even after 10–15 years, mandating indefinite surveillance (PMC10163974, SEER-based studies).

**Quality of life impact:** Cranial nerve deficits (facial paralysis, numbness, masticatory dysfunction), dysphagia, and disfigurement from radical surgery substantially affect quality of life; long-term surveillance imaging and the psychological burden of a disease with a very long "tail" of recurrence risk are notable but under-quantified in standardized instruments (EQ-5D/SF-36 data specific to ACC are sparse in the literature reviewed).

---

## 4. Genetic/Molecular Information

**Causal/driver genes:**
- ***MYB*** (HGNC:7545; 6q23.3) — via t(6;9)(q22-23;p23-24) fusion to ***NFIB*** (HGNC:7784; 9p23-24), or via 3′UTR truncation/amplification. This is the dominant genomic hallmark (Persson et al. 2009, PMCID PMC2773970).
- ***MYBL1*** (HGNC:7548; 8q13.1) — alternative driver in *MYB*-fusion-negative ACC, fusing to *NFIB* or *YTHDF3*; mutually exclusive with *MYB* alterations (PMID:29149504).
- ***NOTCH1*** (HGNC:7881; 9q34.3) — recurrent activating mutations clustering in the negative regulatory region (heterodimerization domain) and PEST domain, analogous to T-ALL hotspots (Ferrarotto et al., *J Clin Oncol* 2017;35:352-360).
- ***TERT*** promoter — recurrent hotspot promoter mutations in a mutually exclusive subset (JCI:128227).

**Variant classification/type:** *MYB-NFIB* and *MYBL1* alterations are chromosomal **rearrangements/gene fusions** (structural variants), essentially always **somatic**. *NOTCH1* and *TERT* promoter alterations are **somatic point mutations/small indels**; *NOTCH1* mutations are gain-of-function (activating), analogous to leukemia-associated NOTCH1 mutations. There is no established ClinVar/ACMG germline pathogenic-variant framework for ACC, since virtually all reported drivers are somatic tumor events rather than germline predisposition alleles.

**Somatic vs. germline:** ACC driver alterations are overwhelmingly **somatic**. COSMIC and TCGA-style sequencing (whole-exome sequencing of lacrimal gland ACC, PMC5562266; genomic landscape studies) confirm this. Rare germline *BRCA2* variants have been reported anecdotally in familial clusters but are not an established recurrent germline predisposition mechanism.

**Additional genomic alterations** (enriched particularly in recurrent/metastatic disease per Ho et al., *J Clin Invest* 2019, DOI:10.1172/JCI128227):
- Chromatin remodeling: *KDM6A*, *KMT2C/MLL3*, *ARID1A*, *ARID1B*, *SMARCA4*, *SMARCB1*, *PBRM1*
- DNA damage/checkpoint: *ATM*
- FGF/IGF/PI3K signaling pathway alterations
- *TP53* mutations (associated with recurrent/metastatic disease and solid histologic subtype)
- *TP63* activation (paradoxically associated with a **better** prognosis subgroup; induces *AXL*, *EGFR*, *MET* expression)
- *RAS* pathway mutations (associated with worse disease-free and overall survival)
- *FAT1*/*FAT3* (Hippo-YAP pathway) mutations; *YAP1* alterations common in lung-primary ACC
- *EGFR* mutations (~1–2%), with EGFR overexpression linked to poor prognosis and PD-L1 induction via c-Myc
- 1p36 locus deletion — reported as an independent adverse prognostic marker (Virchows Arch, 2018)

**Molecular subtyping:** Ferrarotto and colleagues proposed an "ACC-I" molecular class characterized by NOTCH-MYC pathway activation, solid histology, minor salivary gland origin, and co-mutation of *SPEN*, *CREBBP*, *EP300* — associated with significantly worse prognosis (PMC11387731).

**Epigenetic information:** *MYB* overexpression is reinforced by a **positive-feedback super-enhancer loop** in which MYB binds its own enhancer elements; disruption of the normal miRNA-mediated (miR-15a/16, miR-150) post-transcriptional brake via 3′UTR loss is a key epigenetic-adjacent mechanism of MYB dysregulation. Downregulation of chromatin remodeling complex components (SWI/SNF family: *SMARCA4*, *SMARCB1*, *ARID1A/B*, *PBRM1*) has been reported, implicating global chromatin dysregulation as ACC progresses.

**Chromosomal abnormalities:** The signature **t(6;9)(q22-23;p23-24)** translocation generating *MYB-NFIB*; 1p36 deletions as a secondary recurrent copy-number event associated with prognosis.

**Suggested ontology terms:**
- Genes (HGNC): `hgnc:7545` MYB, `hgnc:7784` NFIB, `hgnc:7548` MYBL1, `hgnc:7881` NOTCH1, `hgnc:11730` TERT, `hgnc:11998` TP53, `hgnc:12558` TP63, `hgnc:3236` EGFR

---

## 5. Environmental Information

- **Environmental/occupational factors:** No consistently reproduced association with specific toxins, industrial exposures, or air pollutants has been established, unlike some other salivary or sinonasal malignancies (e.g., wood-dust exposure and sinonasal adenocarcinoma). The strongest documented environmental contributor remains **prior ionizing radiation exposure** to the head and neck.
- **Lifestyle factors:** Tobacco and alcohol use — unlike most head and neck squamous cell carcinomas — have **not** been shown to increase ACC risk in the literature reviewed.
- **Infectious agents:** No infectious/microbial trigger (viral, bacterial, fungal, parasitic) has been implicated in ACC pathogenesis; this distinguishes it from HPV-associated oropharyngeal cancers and EBV-associated nasopharyngeal carcinoma, both of which can present in overlapping anatomic sites.

---

## 6. Mechanism / Pathophysiology

**Causal chain overview:** Trigger (MYB-family transcription-factor dysregulation, principally via *MYB-NFIB*/*MYBL1* fusion or amplification) → constitutive transcriptional activation of proliferative and anti-apoptotic MYB target genes → cooperating/parallel NOTCH1 pathway hyperactivation (particularly in aggressive/recurrent disease) → downstream MYC upregulation, EMT induction, angiogenesis, and immune evasion → biphasic tumor growth with intrinsic myoepithelial/luminal cellular heterogeneity → perineural invasion and local infiltration → (in a subset) late hematogenous metastasis, chiefly to lung.

**Molecular pathways:**
- **MYB transcriptional program:** MYB (with cooperating partner NFIB) drives a transcriptional program promoting cell cycle progression and inhibiting apoptosis partly through MYC; also upregulates VEGFA and vimentin, contributing to angiogenesis, EMT, and metastatic competence (PMC11387731).
- **NOTCH-MYC/HES-HEY axis:** Activating *NOTCH1* mutations (or wild-type pathway hyperactivation via paracrine ligand signaling) drive NOTCH intracellular domain (NICD)-mediated transcription of *HES1*, *HEY1*, *REST*; the NOTCH1-HEY1 axis is implicated in proliferation, invasion, metastasis, and apoptosis resistance. Notably, MYB and NOTCH pathways appear to have **opposing effects on cellular differentiation**, and single-cell data show that metastatic lesions have elevated MYB/lower NOTCH1 expression while recurrent tumors show the inverse (increased NOTCH signaling, reduced MYB), suggesting dynamic pathway switching across the disease course (Cell Reports single-cell study, PMC9714264/PMID:36465348).
- **EGFR-PI3K-AKT / MEK-ERK signaling:** EGFR overexpression (mutation rate only ~1–2%) is linked to poor prognosis; EGFR activation induces PD-L1 expression via c-Myc, offering one mechanistic link between growth-factor signaling and immune evasion.
- **Hippo-YAP pathway:** *FAT1*/*FAT3* mutations and *YAP1* alterations (particularly common in lung-primary ACC).
- **TGF-β signaling:** implicated in the biphasic epithelial/myoepithelial differentiation program.
- **RAS/MAPK:** RAS pathway mutations associated with poorer disease-free and overall survival.

**Cellular processes and cell-of-origin.** Single-cell RNA-sequencing studies (Lin et al., PMID:36465348; Cell Reports, PMID/PMC9714264) profiled ~49,948 cells from paracarcinoma/carcinoma tissue and identified:
- **Myoepithelial-like cells (CD49f+)** — higher tumorigenic potential than ductal cells, serving as progenitors for ductal differentiation, and expressing NOTCH ligands (DLL1, JAG1, JAG2) that paracrine-signal to adjacent luminal cells.
- **Intercalated duct-like cells (KRT19+/AQP5+/KIT+)** and **duct-like cells (KRT19+/AQP5−/KIT−)**, expressing high levels of NOTCH receptors and NOTCH target genes.
- **Pre-malignant cells** (~47% of paracarcinoma epithelial cells) with copy-number alterations affecting the *MYB* family and *EN1*; pseudotime trajectory analysis suggests these differentiate into malignant cells over time, implying an **intercalated-duct cell of origin**.
- **Tumor microenvironment composition:** epithelial cells ~40.1%, fibroblasts ~27.9% (subdivided into proliferative, myogenic, inflammatory, and fibrotic cancer-associated fibroblast [CAF] subtypes), T/NK cells ~11.3%, endothelial cells ~10.8%.

**Immune system involvement / "cold" tumor phenotype:** ACC exhibits significantly reduced tumor-infiltrating lymphocytes compared with normal tissue, downregulated CD8+ and CD4+ T-cell populations, absent IgA plasma cells, inhibited canonical PD-1/PD-L1 signaling but activated **immunosuppressive PD-L2 and HLA-G**, and elevated M2 macrophages/myeloid-derived suppressor cells (with macrophage communication mediated via the MIF-CD74 axis rather than classical HLA-MHC signaling). This immunologically "cold," low-tumor-mutational-burden phenotype underlies the generally poor response of ACC to immune checkpoint inhibition (PMC11387731).

**Tissue damage / perineural invasion mechanism:** Perineural invasion — one of ACC's most defining pathophysiological features — has been mechanistically linked to **brain-derived neurotrophic factor (BDNF)** signaling promoting neurotropism (Kulasegaran/Vered et al., PMID:12378520, "Perineural invasion in adenoid cystic carcinoma: Its causation/promotion by brain-derived neurotrophic factor"). PNI classically shows a "target-like arrangement" of tumor cells around nerve fibers and independently predicts worse disease-free and overall survival.

**Biochemical/protein-level abnormalities:**
- **c-KIT (CD117)** overexpression in ~90% of ACC — associated with enhanced invasiveness, though targeting KIT with imatinib/dasatinib has shown minimal clinical efficacy, implying KIT expression is a bystander/marker rather than a driver.
- **p53** overexpression in ~50% of cases, associated with solid histologic subtype, higher metastatic potential, and reduced 5-year overall survival.
- **Bcl-2** overexpression associated with perineural invasion and worse prognosis.
- **Beclin-1** (autophagy regulator) — lower expression correlates with higher histologic grade.
- **SOX2/SOX-10** — broadly expressed; SOX2 correlates with clinical progression.

**Molecular/omics profiling:**
- **Transcriptomics:** Single-cell RNA-seq (above) plus bulk expression studies show MYB target gene programs and NOTCH pathway signatures distinguishing primary from recurrent/metastatic disease.
- **Genomics:** Whole-exome sequencing of lacrimal gland ACC (PMC5562266) and personalized oncogenomic whole-genome sequencing of metastatic ACC (Molecular Case Studies, molecularcasestudies.cshlp.org/content/4/2/a002626) have informed individualized treatment decisions.
- **Proteomics:** Comparative proteomic analysis distinguishes breast ACC from basal-like triple-negative breast cancer despite morphologic and IHC overlap (PMC9366086).
- **Spatial transcriptomics:** Recent work has mapped molecular heterogeneity by pathological grade using combined whole-exome sequencing and spatial transcriptomics (ScienceDirect, S0046817725000450).

**Suggested ontology terms:**
- **GO Biological Process:** GO:0007219 (Notch signaling pathway), GO:0038095 (Fc-epsilon receptor... not relevant); more precisely GO:0045747 (positive regulation of Notch signaling), GO:0001525 (angiogenesis), GO:0001837 (epithelial to mesenchymal transition), GO:0006915 (apoptotic process), GO:0007050 (cell cycle arrest — inverse), GO:0035633 (maintenance of blood-brain barrier — not relevant), GO:0021675 (nerve development, for perineural invasion biology)
- **GO Molecular Function:** GO:0003700 (DNA-binding transcription factor activity) for MYB/MYBL1
- **Cell Ontology (CL):** CL:0002326 (luminal epithelial cell of mammary gland — analog for ductal/luminal ACC cells), CL:0000185 (myoepithelial cell), CL:0000066 (epithelial cell)
- **UBERON:** UBERON:0001830 (major salivary gland), UBERON:0001831 (minor salivary gland), UBERON:0001911 (mammary gland)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary sites** (per SEER 2000–2019 cohort of 5,150 cases, PMID:39410002): head and neck 70.1% (parotid and submandibular glands together ~37% of all ACC, oral cavity/minor salivary glands ~22%), breast 14.1%, thoracic (trachea, bronchus, lung) 6.8%, genitourinary (cervix uteri, Bartholin gland, prostate) 2.2%, miscellaneous sites (skin, lacrimal gland, esophagus) 6.8%.
- **Secondary/metastatic involvement:** lung (most common distant metastatic site), bone, liver; regional lymph node metastasis is comparatively uncommon relative to squamous cell carcinoma of the head and neck, reflecting ACC's preference for hematogenous over lymphatic spread.
- **Body systems involved:** exocrine gland tissue (salivary, lacrimal, mammary, tracheobronchial submucosal glands), integumentary system (rare cutaneous ACC), and — via perineural spread — the peripheral and cranial nervous system (facial [VII], trigeminal [V], and other cranial nerves).

**Tissue and cell level:**
- Epithelial (ductal/luminal) and myoepithelial (basaloid/abluminal) cell populations, arranged in cribriform, tubular, or solid architectural patterns.
- Perineural tissue — Schwann cells and nerve fibers infiltrated by tumor cells in a "target-like" pattern.

**Suggested Cell Ontology terms:** CL:0000185 (myoepithelial cell), CL:0000068 (duct epithelial cell), CL:0002327 (mammary luminal progenitor cell — analog).

**Subcellular level:** Nuclear localization of MYB/MYBL1 and NICD (Notch intracellular domain) as transcription factors (GO Cellular Component: GO:0005634 nucleus); mitochondrial/ER stress pathways implicated in ferroptosis-based therapeutic vulnerability research (GPX4 inhibitor studies).

**Localization/lateralization:** Typically unilateral at presentation (e.g., unilateral parotid or submandibular mass); bilateral or midline presentations occur with minor salivary gland (palate) or tracheal primaries. Perineural spread can cross the skull base bilaterally in advanced disease via named neural foramina.

**Suggested UBERON terms:** UBERON:0001831 (minor salivary gland), UBERON:0001830 (major salivary gland; parotid UBERON:0006330, submandibular UBERON:0006331), UBERON:0001911 (mammary gland), UBERON:0003126 (trachea), UBERON:0002048 (lung), UBERON:0000948 (heart — not typically involved), UBERON:0000948... (for cervix: UBERON:0000002 uterine cervix).

---

## 8. Temporal Development

**Onset:** Adult-onset predominant, with a broad age range (first through ninth decades) and median age at diagnosis of ~58 years (IQR 47–70, SEER cohort). Onset is typically **insidious** — patients often present with a slow-growing, painless mass for months to years before diagnosis, though pain and neurologic symptoms may prompt earlier presentation when perineural invasion is present.

**Progression:**
- **Histologic grading correlates with growth pattern and prognosis:** Grade I (predominantly tubular) — most favorable; Grade II (predominantly cribriform, <30% solid) — intermediate; Grade III (>30% solid component) — least favorable, associated with higher proliferation, greater local invasiveness, and reduced survival. Historical cumulative 15-year survival by grade: 39% (Grade I), 26% (Grade II), 5% (Grade III), with Grade III tumors often proving fatal within 4 years in early cohorts. More recent analyses suggest **tumor stage may be a more robust prognostic indicator than histologic grade alone**.
- **High-grade transformation (HGT):** a described phenomenon in which a conventional low/intermediate-grade ACC acquires markedly increased mitotic activity, Ki-67 index, and p53 positivity, associated with a more aggressive clinical course.
- **Progression rate:** locally, growth is slow, but the disease is notable for continuing to progress/recur over a very long time horizon; distant metastasis, when it occurs, has a median time-to-recurrence of approximately 50–51 months post-primary treatment, and events can occur even after 10–15+ years of apparent disease-free survival.
- **Disease course pattern:** best described as chronic-progressive with a long "tail" — unlike many carcinomas that either recur within 2–5 years or are cured, ACC carries persistent recurrence risk indefinitely, necessitating lifelong surveillance.

**Patterns:**
- **Remission:** Achievable with complete surgical resection ± adjuvant radiotherapy in localized disease, but "cure" is difficult to declare definitively given the long natural history; spontaneous remission is not described.
- **Critical periods:** The window for achieving durable local control is at initial surgical resection (negative margins); once perineural spread has occurred along a named nerve to the skull base, the opportunity for complete resection narrows considerably, making early, meticulous margin-negative surgery a key point of intervention leverage.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Incidence:** approximately **3–4.5 cases per million people per year**; ACC represents ~1% of all head and neck malignancies and ~10% of all salivary gland neoplasms (PMC11387731, PMC11476411).
- **SEER-based cohort (2000–2019, N=5,150; PMID:39410002)** provides the most detailed contemporary US population data:
  - Median age 58 years (IQR 47–70)
  - Sex: 63.3% female, 36.7% male (female:male ≈ 1.7:1, broadly consistent with the commonly cited ~3:2 ratio)
  - Race/ethnicity: White 75.9%, Asian 11.2%, Black 10.8%, other/unknown 2.1%
  - Stage at diagnosis: localized 77.5%, regional 14.3%, distant 8.2%
  - Site distribution: head/neck 70.1%, breast 14.1%, thoracic 6.8%, genitourinary 2.2%, miscellaneous 6.8%

**Inheritance pattern:** ACC is essentially always a **sporadic, somatically driven malignancy**; there is no established Mendelian inheritance pattern (autosomal dominant/recessive, X-linked, mitochondrial) for the disease as a whole. Rare familial clustering has been anecdotally linked to germline *BRCA2* mutations, but this does not constitute an established hereditary cancer syndrome specific to ACC, and penetrance/expressivity data for such associations are not robust in the literature. Genetic anticipation, germline mosaicism, founder effects, and consanguinity are **not applicable/not established** for this predominantly somatic-driver disease.

**Population demographics:**
- **Geographic distribution:** No strong endemic geographic clustering is reported; SEER regional analysis found some survival variation by US region (Northeast longest median OS at 171 months vs. Midwest 132 months), likely reflecting access-to-care and treatment-pattern differences rather than incidence differences.
- **Sex ratio:** Female predominance (~3:2 to ~1.7:1 depending on cohort/site — notably even more female-predominant in breast-primary ACC, which is inherently sex-skewed given anatomic site).
- **Age distribution:** Broad (1st–9th decades), peak in middle-to-older adulthood (45–70 years).
- **Ethnicity/hospital-based series** suggest some site-distribution variation (e.g., a higher proportion of Hispanic patients showing modestly better 6-year OS: 73.9% vs. 70.4% non-Hispanic in the SEER cohort), though causal interpretation is limited by retrospective registry design.

---

## 10. Diagnostics

**Clinical/laboratory tests:** No specific serum biomarker or routine laboratory test is diagnostic for ACC; diagnosis rests on tissue biopsy with histopathology and immunohistochemistry, supported by imaging for local/perineural extent and staging.

**Imaging studies:**
- **MRI** is the preferred modality for staging, treatment planning, and surveillance because of superior soft-tissue contrast and multiplanar capability, and is particularly valuable for detecting **perineural spread** — appearing as replacement of normal fat within neural foramina and pathologic nerve enhancement/thickening. MRI sensitivity/specificity for perineural spread has been reported at ~100%/85%, compared with ~88%/89% for CT (JAMA Otolaryngol Head Neck Surg, PMID:17576903).
- **CT** remains useful for assessing bony invasion/erosion (e.g., skull base, mandible, maxillary sinus) and for chest staging (screening for pulmonary metastases, the most common distant metastatic site).
- **PET/CT** may be used for staging and surveillance, though ACC's typically low proliferative index in low-grade tumors can limit FDG-avidity sensitivity.

**Biopsy/pathology findings:** Core needle or incisional biopsy demonstrating the characteristic **biphasic** population of ductal/luminal and myoepithelial/basaloid cells arranged in **cribriform** (most common; "Swiss cheese" pattern with basement-membrane-like/glycosaminoglycan-filled pseudocysts), **tubular**, or **solid** patterns. Perineural invasion is frequently identified histologically as a target-like tumor cuff around nerve fascicles.

**Immunohistochemistry (diagnostic panel):**
- **MYB nuclear expression** (by IHC) — a highly sensitive and specific surrogate for *MYB-NFIB* fusion status, useful for distinguishing ACC from morphologic mimics (e.g., basal cell adenoma/adenocarcinoma, polymorphous adenocarcinoma) and for detecting the solid variant of breast ACC among triple-negative breast cancers.
- **c-KIT (CD117)** — positive in ~90% of ACC.
- **p63/p40** and **calponin/SMA/S100** — myoepithelial cell markers, highlighting the biphasic architecture.
- **Ki-67** proliferation index — higher indices correlate with solid pattern and worse prognosis.
- **p53** — overexpressed in ~50% of cases, associated with solid subtype and worse survival.

**Molecular/genetic testing:**
- **FISH or NanoString-based detection of *MYB-NFIB* / *MYBL1* rearrangements** — used diagnostically in ambiguous cases and increasingly to guide clinical trial eligibility (e.g., MYB-inhibitor trials).
- **Targeted NGS panels covering *NOTCH1*, *NOTCH2*, *NOTCH3*** hotspots — used to identify NOTCH-activating mutations that may render patients eligible for gamma-secretase inhibitor (GSI) trials (e.g., AL101, CB103).
- Whole-exome/whole-genome sequencing has been used investigationally (including for individualized treatment selection in metastatic cases, e.g., the personalized oncogenomic case study at molecularcasestudies.cshlp.org).

**Differential diagnosis:** basal cell adenoma/adenocarcinoma, polymorphous adenocarcinoma (PAC), epithelial-myoepithelial carcinoma, dermal cylindroma (shares the *MYB-NFIB* fusion but is histologically and clinically distinct — an important molecular-vs-morphologic diagnostic nuance), and — for breast primaries — basal-like triple-negative breast cancer (distinguished by MYB IHC/FISH and generally much better prognosis for ACC-of-breast despite triple-negative receptor status).

**Screening:** No population-based or high-risk-group screening program exists for ACC, reflecting its rarity and lack of a clearly definable high-risk population (in contrast to, e.g., BRCA1/2-driven breast/ovarian cancer screening).

---

## 11. Outcome/Prognosis

**Survival:**
- Long-term reported survival is notably better than raw 5-year figures suggest, owing to the tumor's protracted natural history: one classic cohort reported **mean survival of 16 years**, with actuarial survival of **77% at 5 years, 66% at 10 years, and 56% at 15 years**.
- Another cohort reported overall survival of **80.4% at 5 years, 61.3% at 10 years, and 29.4% at 15 years** — illustrating cohort-to-cohort variability tied to stage/site mix.
- **SEER (2000–2019) 6-year overall survival by primary site** (PMID:39410002): breast 86.5% ± 1.4% (best prognosis site), genitourinary 75.3% ± 4.5%, miscellaneous 73.8% ± 2.7%, head/neck 68.2% ± 0.9%, thoracic 60.5% ± 3.0% (worst).
- Median overall survival varies substantially by US region in the SEER cohort: Northeast 171 months, West 144 months, South 136 months, Midwest 132 months — likely reflecting access/treatment-pattern effects.
- **Independent adverse prognostic factors (SEER multivariable analysis):** thoracic primary site, regional disease (HR 1.63), distant metastasis at diagnosis (HR 2.55), chemotherapy use (HR 1.76, likely reflecting more advanced/refractory disease selection), Western US region of treatment (HR 2.93), and unmarried status (HR 1.27, a social-support proxy).
- **Favorable factors:** surgical resection (HR 0.43) and breast primary site.

**Distant metastasis and lung-specific outcomes:**
- Mean survival after the appearance of distant metastases is reported at approximately **11 years** in one cohort.
- For patients undergoing pulmonary metastasectomy, mean survival from the time of distant metastasis appearance was **72 months**, versus **62 months** for those who did not undergo resection — suggesting a potential (though selection-biased) survival benefit from surgical management of oligometastatic pulmonary disease (Eur J Cardiothorac Surg, PMID:18343149).

**Recurrence patterns:** Approximately **one-third of patients experience recurrence**, predominantly at distant sites rather than locoregionally; median time to locoregional recurrence and to distant metastasis are both approximately **50–51 months**, but late events (>10 years) are well documented, reinforcing the need for indefinite long-term surveillance rather than the typical 5-year "cure" window used for many other carcinomas.

**Prognostic factors/biomarkers:**
- **Histologic grade/pattern** (solid > cribriform > tubular for aggressiveness), though tumor stage may be a more robust predictor in contemporary series.
- **Perineural invasion** — independently associated with worse disease-free and overall survival.
- ***NOTCH1*-activating mutations** — independently associated with markedly worse survival (median OS 55.1 vs. 204.5 months in NOTCH1-mutant vs. wild-type recurrent/metastatic ACC per Ho et al., *J Clin Invest* 2019).
- ***KDM6A*** mutation — associated with markedly worse overall survival (HR = 3.428, p = 0.0012) in one cohort.
- **1p36 deletion** — independent adverse prognostic marker.
- **p53 overexpression, RAS mutation, TP53 mutation** — each associated with worse outcomes.
- ***TP63* activation** — paradoxically associated with a more favorable prognostic subgroup.
- **Margin status and surgical resection** — consistently favorable.

**Morbidity:** Cranial neuropathies (facial, trigeminal), disfigurement from radical resection, and functional deficits (dysphagia, speech impairment, airway compromise for tracheal disease) constitute the principal non-fatal morbidity burden; standardized quality-of-life instrument data specific to ACC are limited in the literature surveyed.

---

## 12. Treatment

**Surgery** — the primary and preferred treatment modality regardless of anatomic site. Complete surgical resection with tumor-free margins is considered the "gold standard," though achieving negative margins is frequently challenged by the tumor's propensity for microscopic perineural extension well beyond the grossly visible tumor margin, often necessitating sacrifice of, or careful dissection around, critical nerves (e.g., facial nerve in parotid ACC). MAXO term: MAXO:0000004 (surgical procedure).

**Radiation therapy:**
- **Postoperative radiotherapy (PORT)** is widely used for advanced, high-grade, or margin-positive/close-margin ACC, typically to a conventional photon dose around 60 Gy; recommended for all cases except T1N0 disease with clear margins. Evidence suggests PORT improves local control and may improve quality of life, though its impact on overall survival is debated in some series. MAXO:0000014 (radiation therapy).
- **Particle/advanced radiotherapy modalities** show particular promise for ACC given its relatively radioresistant, low-proliferative biology:
  - **Carbon-ion radiotherapy (CIRT)** — an oxygen enhancement ratio near 1.0 (vs. 2.5–3.0 for photons) and reported 1.5–3× higher biological efficacy; evaluated in the phase II **ACCO trial** (adenoid cystic Carcinoma and Carbon ion Only irradiation), a prospective randomized two-arm study (PMC8281682).
  - **Proton therapy (IMPT)** — superior depth-dose distribution permitting dose escalation (70.0–79.1 CGE) with reported enhanced local control and reduced neurotoxicity.
  - **Fast neutron therapy** — high linear energy transfer, effective against the low-metabolic-rate biology typical of ACC.
  - **Boron neutron capture therapy (BNCT)** — investigational for skull-base ACC.

**Systemic therapy:**
- **Cytotoxic chemotherapy** has limited efficacy in ACC; platinum-based regimens (e.g., cisplatin + paclitaxel) achieve response rates of only ~15–25%, and chemotherapy is generally reserved for symptomatic, rapidly progressive, or otherwise unresectable/unirradiable metastatic disease.
- **Tyrosine kinase inhibitors (targeting angiogenesis/VEGFR predominantly, given limited actionable driver mutations):**
  - **Lenvatinib** (VEGFR/FGFR/PDGFR) — disease control and stability in most recurrent/metastatic cases, with 40.6% (13/32) achieving ≥6-month clinical benefit in one series.
  - **Axitinib** — 18% objective response rate (5/28), median PFS 7.3 months, median OS 16.6 months.
  - **Apatinib** (selective VEGFR2 inhibitor) — one series reported a 92.3% response rate; an international phase II trial (NCT02775370) reported a more modest but still notable 15.3% ORR with 14.9-month median response duration, reported as superior to other TKIs and chemotherapy in that comparison.
  - **Sorafenib** — ~10% ORR, with frequent adverse reactions limiting tolerability.
  - c-KIT-targeted agents (**imatinib**, **dasatinib**) and EGFR-targeted agents (**gefitinib**, **cetuximab**, **lapatinib**) have shown minimal-to-no objective response despite target expression, underscoring that IHC positivity (e.g., CD117) does not equate to oncogenic dependence in ACC.
- **NOTCH pathway inhibitors** (for the *NOTCH1*-mutant subgroup, ~13–20% of patients):
  - **AL101 (osugacestat)**, a pan-NOTCH gamma-secretase inhibitor — the **ACCURACY** phase II trial reported clinical activity at 4 mg once weekly with a disease control rate of 68% (15% partial response); AL101 received FDA Orphan Drug (2019) and Fast Track designations. Preclinical/mechanistic rationale published in *Cell Death & Disease* (PMID from PMC9355983).
  - **CB103** (pan-NOTCH inhibitor blocking the CSL-NICD interaction) — phase I reported 58% disease stabilization, median PFS 2.5 months, OS 18.4 months (NCT03422679).
  - **Brontictuzumab** (anti-NOTCH1 monoclonal antibody) — phase I: 2 partial responses and 3 stable disease among 12 ACC patients.
- **Emerging MYB-directed strategies:**
  - **All-trans retinoic acid (ATRA)** — reduces MYB enhancer binding, attenuating the MYB overexpression feedback loop (trials NCT03999684, NCT04433169).
  - **RGT-61159** — an oral RNA-splicing modulator selectively inhibiting c-MYB, effective in ACC patient-derived xenograft (PDX) models, now in phase I (NCT06462183).
  - Preclinical MYB-targeting approaches: monensin A (ionophore screen hit), Bcr-TMP/oprozomib (proteasome inhibition, p300-dependent), and ferroptosis-inducing GPX4 inhibitors (ML162, ML210, RSL3) correlated with MYBL1 dependency; HDAC inhibitors (vorinostat) implicated in ferroptosis sensitivity regulation.
- **Immunotherapy:** Given ACC's immunologically "cold" phenotype (low mutational burden, minimal lymphocyte infiltration, rare PD-L1 expression, active PD-L2/HLA-G immunosuppression), checkpoint inhibitor monotherapy has shown limited efficacy — **pembrolizumab** achieved only a 12% partial response rate among 26 advanced salivary gland cancer patients (including 2 ACC) in KEYNOTE-028, and pembrolizumab + radiotherapy (NCT03087019) achieved 0% objective response in 20 metastatic ACC patients. Combination strategies (e.g., **axitinib + avelumab**, a checkpoint inhibitor, in an ongoing phase II trial) and a **MYB peptide vaccine + anti-PD-1** trial (NCT03287427) are being explored to convert the cold tumor microenvironment.
- **Other investigational targeted agents:** cabozantinib (multikinase AXL/MET/VEGFR inhibitor, NCT03729297, rationale tied to TP63-activated AXL/EGFR/MET expression conferring EGFR-inhibitor resistance), everolimus (mTOR inhibitor; 0% ORR but 65.5% disease stabilization), bortezomib (proteasome inhibitor; 0% ORR, 68% stable disease), PARP inhibitors (proposed for the ACC-I molecular subtype with high PARP/CHK1/CHK2 expression), CDK9 inhibitor KB-0742 (53.8% disease control in 18 patients), and the STING agonist TAK-676 (NCT04879849).
- **Combination approaches:** triple combination of linsitinib (IGF1R) + gefitinib (EGFR) + crizotinib (ALK/MET) significantly reduced MYB expression preclinically; combination strategies pairing NOTCH inhibitors with MYC-targeting agents (e.g., PRMT5 inhibitor GSK3326595, which produced partial responses in 3/14 patients) and BCL2 inhibitors with gamma-secretase inhibitors are being explored to address tumor heterogeneity.

**Supportive/rehabilitative care:** Facial nerve rehabilitation (physical therapy, nerve grafting/reanimation surgery when the facial nerve is sacrificed), speech and swallowing therapy for oropharyngeal/laryngotracheal disease, and pain management for perineural neuropathic symptoms.

**Suggested MAXO terms:** MAXO:0000004 (surgical procedure), MAXO:0000014 (radiation therapy), MAXO:0000647 (chemotherapy), MAXO:0000011 (physical therapy), MAXO:0000950 (supportive care); with the pharmacotherapy modality (NCIT:C15986) plus `therapeutic_agent` bindings to CHEBI/NCIT terms for lenvatinib, axitinib, apatinib, sorafenib, imatinib, cetuximab, pembrolizumab, and the investigational AL101/CB103 gamma-secretase inhibitors.

---

## 13. Prevention

**Primary prevention:** No established primary prevention strategy exists, since ACC lacks a clearly modifiable lifestyle risk factor (unlike smoking-associated head and neck cancers). The one identified modifiable/avoidable risk factor is **minimizing unnecessary ionizing radiation exposure to the head and neck**, particularly in children, given the well-documented latency-associated risk of radiation-induced salivary gland malignancy.

**Secondary prevention (screening/early detection):** No population-based screening program exists for ACC due to its rarity and lack of a definable high-risk population; early detection instead relies on prompt clinical evaluation (and imaging/biopsy) of persistent head/neck masses, unexplained cranial neuropathy, or slow-growing breast/skin lesions.

**Tertiary prevention:** Given the long natural history and persistent late-recurrence risk, **indefinite long-term clinical and radiographic surveillance** (including periodic chest imaging for pulmonary metastasis surveillance) after primary treatment functions as the principal tertiary-prevention strategy to enable early detection and potential resection of oligometastatic (particularly pulmonary) recurrence.

**Genetic counseling:** Not routinely indicated given the absence of an established hereditary ACC syndrome; counseling would only be considered in the rare context of a family history suggestive of a *BRCA2*-associated cancer predisposition syndrome, and even then would be directed at the broader hereditary breast/ovarian cancer risk rather than ACC specifically.

**Immunization/prophylaxis:** Not applicable — no infectious trigger has been identified.

---

## 14. Other Species / Natural Disease

**Taxonomy and natural disease:** Adenoid cystic-type carcinomas arising from salivary and other exocrine glandular tissue are recognized in **veterinary comparative oncology**, most notably in **dogs** (NCBITaxon:9615) and **cats** (NCBITaxon:9685), where salivary gland adenocarcinomas — including adenoid cystic-type histology — occur as naturally occurring tumors, and mammary gland carcinomas (the most common tumor type in intact female dogs) can show adenoid cystic-like ("mucinous") morphologic patterns. The literature search did not surface a dedicated OMIA (Online Mendelian Inheritance in Animals) entry specifically for canine ACC as a distinct catalogued entity, though comparative-oncology reviews of canine mammary carcinoma emphasize strong molecular parallels with human breast malignancies in cell-cycle regulatory and oncogene/tumor-suppressor gene expression patterns (PMC5644615), supporting the general utility of the dog as a comparative model for glandular carcinomas, even though ACC-specific *MYB-NFIB* comparative genomic data in veterinary species were not identified in this search.

**Comparative biology:** No strong evidence was found in this search for a dedicated invertebrate, zebrafish, or other non-mammalian natural-disease correlate of ACC, consistent with its origin from exocrine/glandular epithelial-myoepithelial architecture that is a mammalian anatomic feature.

**Zoonotic potential/transmission:** Not applicable — ACC is a non-infectious, non-transmissible somatic malignancy.

---

## 15. Model Organisms

**Genetically engineered mouse models (GEMMs):** Because the *MYB-NFIB* fusion is the genomic hallmark of human ACC, at least **three GEMMs** have been engineered to test its in vivo oncogenic role (as reviewed in PMC11387731 and by the Adenoid Cystic Carcinoma Research Foundation, accrf.org/tools-for-researchers/gemms/):
- **Mikse et al. (2016)** — crossed bi-allelic *MYB-NFIB*/MMTV-Cre mice (driving fusion expression in salivary and mammary tissue) with *p53^fl/fl^* mice. Notably, **no mice developed salivary gland cancer**, but **poorly differentiated mammary tumors** developed specifically in *MYB-NFIB*/MMTV-Cre/*p53^+/fl^* mice — indicating that *MYB-NFIB* expression alone is insufficient for tumorigenesis and requires cooperating *p53* pathway loss, at least in this model, and highlighting a **human-model mismatch**: the model did not recapitulate the salivary-gland tropism of human ACC despite transgene expression there.
- **Jiang et al. (2019)** — crossed a *MYB-NFIB* GEMM with *Ink4a^+/−^*/*Arf^+/−^* mice; one resulting mouse developed a mammary tumor with **cribriform ACC-like adenocarcinoma histology**, overexpressing Myb protein and positive for the human *MYB-NFIB* transgene, providing partial phenotypic recapitulation of human cribriform-pattern ACC.
- A third model exists per the ACCRF GEMM resource page, underscoring active community effort to build faithful in vivo models (accrf.org/tools-for-researchers/gemms/).

**In vitro / cell line models:** Established ACC cell lines (e.g., ACC2, SACC-83) are used widely but have documented **significant genetic drift** with passage, and some historically used lines have been found to be **misidentified/contaminated**, a recognized limitation flagged in recent reviews (PMC11387731) — an important caveat for interpreting older cell-line-based mechanistic and drug-screening literature.

**Patient-derived organoids (PDOs):** Report a relatively low establishment success rate (~19%), but successfully derived organoids **maintain *MYB(L1)/NFIB* rearrangement status**, making them a molecularly faithful (if logistically challenging) platform.

**Patient-derived xenografts (PDX):** Higher establishment success rate (~60%) and maintain genomic alterations, though production remains resource- and time-intensive; PDX models have been used to validate emerging MYB-directed agents such as RGT-61159.

**Model limitations:** No single current model (GEMM, cell line, organoid, or PDX) fully recapitulates the combination of (a) faithful anatomic tropism (salivary gland vs. mammary gland), (b) the full spectrum of cribriform/tubular/solid histologic heterogeneity, (c) the biphasic epithelial-myoepithelial cellular architecture, and (d) the immunologically "cold" tumor microenvironment seen in human disease — motivating ongoing development of orthotopic transplantation models (implantation directly into mouse salivary gland) and next-generation genetically diverse cell lines and 3D organoid systems (PMC11387731).

**Applications:** Current models are primarily used to (1) validate MYB-directed and NOTCH-directed small-molecule/biologic therapeutics preclinically, (2) study the biology of the *MYB-NFIB*/*MYBL1* fusion's transforming potential and its dependency on cooperating lesions (e.g., *p53*, *Ink4a/Arf*), and (3) explore mechanisms of perineural invasion and the cold immune microenvironment for future immunotherapy-sensitization strategies.

---

## Summary of Key Evidence Sources

| Topic | Key citation |
|---|---|
| MYB-NFIB fusion discovery | Persson M et al., *Proc Natl Acad Sci USA* 2009;106:18740-18744 (PMCID PMC2773970) |
| NOTCH1 mutations define aggressive subgroup | Ferrarotto R et al., *J Clin Oncol* 2017;35(3):352-360 (DOI:10.1200/JCO.2016.67.5264) |
| Genetic hallmarks of recurrent/metastatic ACC (NOTCH1, TERT, chromatin genes) | Ho AS et al., *J Clin Invest* 2019;129(10) (DOI:10.1172/JCI128227) |
| t(6;9) MYB-NFIB meta-analysis | PMID:30269389 |
| MYBL1 rearrangements in MYB-fusion-negative breast ACC | PMID:29149504 |
| BDNF and perineural invasion mechanism | PMID:12378520 |
| Single-cell transcriptomics / cell-of-origin | PMID:36465348 (PMC9714264) |
| SEER population-based epidemiology/outcomes (2000-2019) | PMID:39410002 (PMC11476411) |
| Comprehensive molecular characterization and therapeutic advances review | PMC11387731 |
| Lung metastasectomy outcomes | PMID:18343149 |
| Perineural spread imaging sensitivity/specificity | PMID:17576903 |
| AL101 gamma-secretase inhibitor preclinical/ACCURACY trial | PMC9355983 |

**Data gaps flagged for curation:** standardized QoL instrument data specific to ACC; robust germline predisposition data beyond anecdotal BRCA2 reports; a dedicated OMIA veterinary entry; comprehensive epigenomic (ENCODE/Roadmap-style) profiling specific to ACC; and confirmed PMID numbers for the Persson 2009 and select other papers cited here by PMCID/DOI only — verify final PMIDs directly on PubMed before entering `evidence.reference` fields.