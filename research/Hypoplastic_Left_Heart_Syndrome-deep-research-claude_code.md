---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-10T03:44:23.674392'
end_time: '2026-08-10T03:49:41.007038'
duration_seconds: 317.33
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypoplastic Left Heart Syndrome
  mondo_id: ''
  category: Congenital
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
  web_search_requests: 11
  num_turns: 13
  total_cost_usd: 1.6596397999999999
  session_id: ccd9973f-d61b-50a6-8cfe-0a77b122d0f2
  stop_reason: end_turn
citation_count: 33
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypoplastic Left Heart Syndrome
- **MONDO ID:**  (if available)
- **Category:** Congenital

## Research Objectives

Please provide a comprehensive research report on **Hypoplastic Left Heart Syndrome** covering all of the
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

# Hypoplastic Left Heart Syndrome (HLHS) — Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview.** Hypoplastic left heart syndrome (HLHS) is a severe congenital heart defect (CHD) characterized by underdevelopment of left-sided cardiac structures — the left ventricle, mitral valve, aortic valve, and ascending aorta/aortic arch — such that the left heart cannot support systemic circulation. It is uniformly fatal without intervention in the neonatal period, historically among the leading causes of death from a single birth defect in the first year of life. HLHS represents the most severe end of a spectrum of left heart underdevelopment/obstruction lesions (sometimes grouped with critical aortic stenosis and other single-ventricle physiologies) ([StatPearls – Hypoplastic Left Heart Syndrome](https://www.ncbi.nlm.nih.gov/books/NBK554576/); [Sergi, Transl Pediatr 2025 scoping review, PMID:40386366](https://pubmed.ncbi.nlm.nih.gov/40386366/)).

**Key identifiers:**
- **OMIM**: 241550 (Hypoplastic Left Heart Syndrome 1, HLHS1) and 614435 (Hypoplastic Left Heart Syndrome 2, HLHS2 — caused by NKX2-5 mutation) ([OMIM 241550](https://omim.org/entry/241550); [OMIM 614435](https://omim.org/entry/614435))
- **Orphanet**: ORPHA:2248 ([Orphanet: Hypoplastic left heart syndrome](https://www.orpha.net/en/disease/detail/2248))
- **MONDO**: MONDO:0004933
- **ICD-10-CM**: Q23.4
- **ICD-11**: LA61.0 (or equivalent congenital malformation of left ventricle code)
- **MeSH**: D016360 (Hypoplastic Left Heart Syndrome)

**Synonyms / alternative names:** HLHS; hypoplastic left heart complex; aortic atresia/mitral atresia syndrome; hypoplasia of left heart; Noonan-Reid syndrome (historical, not current usage); "underdevelopment of the left heart."

**Evidence base note:** Information on HLHS in the literature is derived from a mix of aggregated disease-level resources (OMIM, Orphanet, national birth-defect registries) and individual patient-level data (single- and multi-center surgical outcome cohorts, exome-sequencing case series, fetal echocardiography case series, and disease registries such as the Pediatric Cardiac Genomics Consortium and the Single Ventricle Reconstruction [SVR] trial cohort). Most genetic and mechanistic claims derive from small clinical cohorts (tens to low hundreds of probands) combined with animal-model and iPSC data, reflecting the rarity of the condition and its genetic heterogeneity.

---

## 2. Etiology

### Disease causal factors
HLHS is now understood as a developmentally and genetically heterogeneous "final common pathway" phenotype rather than a single-gene disorder. Two broad, non-mutually-exclusive models of pathogenesis are debated in current literature ([PMID:42200818, *Pathophysiology* 2026, "Is There a Unified Etiology of HLHS? Evaluating Genetic, Structural, and Hemodynamic Models of Disease Initiation"](https://pubmed.ncbi.nlm.nih.gov/42200818/)):

1. **Primary genetic/developmental model** — an intrinsic defect in cardiomyocyte proliferation, differentiation, or endocardial-to-mesenchymal signaling causes primary hypoplasia of left heart structures.
2. **Flow (hemodynamic) theory** — an initiating lesion (e.g., mitral or aortic valve stenosis/atresia) reduces antegrade flow across the left heart in mid-gestation; per Reynolds/shear-stress-dependent growth ("no-flow, no-grow"), reduced flow secondarily arrests growth of the left ventricle, aortic valve, and ascending aorta. This model is supported by serial fetal echocardiography documenting progression from isolated critical aortic stenosis in mid-gestation to frank HLHS by term, and by the partial rescue of biventricular growth after fetal aortic valvuloplasty relieves the flow obstruction ([PMID:25052401](https://pubmed.ncbi.nlm.nih.gov/25052401/)).

Neither model alone fully explains the pathology; the flow theory does not adequately explain endocardial fibroelastosis (EFE) or the histological/molecular abnormalities seen in even mild-flow-disturbance cases, motivating combined genetic-plus-hemodynamic ("two-hit") models.

### Genetic risk factors
- **Monogenic/familial forms** (minority of cases): pathogenic variants in **NKX2-5** (OMIM 614435, HLHS2; chromosome 5q35.1), **NOTCH1** (9q34.3 — both germline dominant and compound-heterozygous recessive forms reported; [PMID:28608148](https://pubmed.ncbi.nlm.nih.gov/28608148/)), **GJA1** (connexin-43; 6q22 — missense substitutions identified in pediatric HLHS transplant recipients), **HAND1** (5q33, including somatic/postzygotic mutations found in cardiac tissue), **MYH6** (α-myosin heavy chain, 14q11.2 — rare damaging variants enriched in ~10% of HLHS probands, both dominant and recessive patterns, associated with reduced transplant-free survival; [PMID:26085007](https://pubmed.ncbi.nlm.nih.gov/26085007/); PMC5206387), **ZIC3**, **MCTP2**.
- **Oligogenic/polygenic burden**: whole-exome sequencing of HLHS trios (Pediatric Cardiac Genomics Consortium, ~330 coding/splicing candidate variants identified across probands) shows no single shared causal variant across most patients — supporting a model of genetic heterogeneity with variable, possibly additive, contributions from multiple CHD-associated genes including AXIN1, BMP2, COL6A2, GATA4, GATA5, GDF1, MESP1, NFATC1, NKX2-6, PCSK9, TBX1, TBX18, and TBX20 ([PMC9604382, "Considering the Genetic Architecture of Hypoplastic Left Heart Syndrome"](https://pmc.ncbi.nlm.nih.gov/articles/PMC9604382/)).
- **Chromosomal/syndromic causes**: HLHS occurs in association with recognized chromosomal syndromes in an estimated **3–20%** of cases, most commonly **Turner syndrome (45,X)**, **trisomy 13 (Patau syndrome)**, **trisomy 18 (Edwards syndrome)**, **Jacobsen syndrome (terminal 11q deletion)** — notably HLHS occurs in up to **~10% of Jacobsen syndrome patients** vs. ~0.2% in the general population ([PMC9864704, "Jacobsen Syndrome with HLHS: Outcome after Cardiac Transplantation"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9864704/)) — and less commonly Smith–Lemli–Opitz syndrome, Holt–Oram syndrome, and partial trisomy 9.
- **Family recurrence risk**: empiric recurrence risk in siblings of an HLHS proband is elevated (~2–4× population risk, historically cited around 2–4%), and first-degree relatives show increased rates of the broader "left ventricular outflow tract obstruction (LVOTO)" spectrum (bicuspid aortic valve, coarctation), consistent with variable expressivity of shared genetic susceptibility.

### Environmental risk factors
Environmental contributions are less well characterized than in some other CHDs, but epidemiologic studies of the broader CHD/LVOTO spectrum implicate:
- Maternal pregestational diabetes mellitus
- Maternal obesity
- Certain maternal medication exposures (e.g., some anticonvulsants) and possibly maternal febrile illness in the first trimester
- Advanced or very young maternal age (mixed evidence)
- Periconceptional folic acid deficiency (protective factor when adequate; see below)

### Protective factors
- **Genetic**: no well-established protective alleles are specifically described for HLHS; population variant databases (gnomAD) are used to filter candidate pathogenic variants by rarity, but specific protective modifier alleles have not been robustly identified.
- **Environmental**: periconceptional **folic acid/multivitamin supplementation** is associated with reduced risk of CHD broadly (evidence strongest for outflow-tract defects), and is presumed protective for HLHS by extension, though HLHS-specific data are limited.

### Gene-environment interactions
Direct gene-environment interaction data specific to HLHS are sparse. The leading conceptual model is a "two-hit" or multi-hit hypothesis in which an underlying genetic susceptibility (e.g., in a proliferation, ciliary, or Notch-pathway gene) combines with a hemodynamic/flow perturbation (itself potentially influenced by maternal-fetal circulatory factors) to produce the full HLHS phenotype, rather than either factor alone being sufficient. This is analogous to the two-locus requirement demonstrated in the murine Ohia model (see Section 15).

**Suggested ontology terms:** MONDO:0004933 (HLHS); HP:0031335 (Abnormal aortic valve morphology); GO:0003007 (heart morphogenesis); GO:0003231 (cardiac ventricle development).

---

## 3. Phenotypes

HLHS phenotypes span cardiac structural anomalies (present from birth, essentially fully penetrant by definition), physiologic/circulatory consequences of ductal-dependent systemic circulation, and postnatal/post-surgical complications.

### Core structural/anatomic phenotypes (clinical signs — congenital onset, present at birth, generally non-progressive as an anatomic entity though physiologically evolving)
| Phenotype | Frequency | Suggested HPO term |
|---|---|---|
| Mitral valve atresia or severe hypoplasia/stenosis | Frequent, near-universal in classic HLHS | HP:0011623 (Mitral atresia) / HP:0001633 (Mitral stenosis) |
| Aortic valve atresia or severe stenosis | Frequent, near-universal | HP:0011541 (Aortic valve atresia) / HP:0001650 (Aortic valve stenosis) |
| Hypoplastic left ventricle | Obligate | HP:0031624 (Hypoplastic left heart) / HP:0004268 (Hypoplastic left ventricle, if available) |
| Hypoplastic ascending aorta / aortic arch | Frequent | HP:0005107 (Hypoplasia of the aorta) |
| Endocardial fibroelastosis (left ventricular endocardium) | Variable, present in a subset, often correlates with residual antegrade flow | HP:0034194 (Endocardial fibroelastosis) if present in ontology, else free text |
| Atrial septal defect / restrictive foramen ovale | Frequent (often obligate for postnatal mixing) | HP:0001631 (Atrial septal defect) |
| Patent ductus arteriosus (physiologically obligate for survival) | Obligate pre-intervention | HP:0001643 (Patent ductus arteriosus) |
| Retrograde aortic arch flow (fetal/prenatal) | Frequent in classic variant | — |

### Clinical presentation / laboratory-lab-adjacent phenotypes (postnatal, onset within hours to days of birth as the ductus arteriosus closes)
- **Cyanosis** (variable — may be subtle if atrial mixing is adequate; profound if restrictive atrial septum) — HP:0000961
- **Circulatory shock / cardiogenic shock** as PDA closes — HP:0008551 or generic shock term
- **Poor feeding, lethargy, tachypnea, respiratory distress** — HP:0011968 (Feeding difficulties), HP:0002094 (Dyspnea)
- **Weak or absent peripheral pulses**, differential cyanosis
- **Metabolic acidosis** (laboratory abnormality) secondary to systemic hypoperfusion
- **Hypoglycemia**, secondary to poor perfusion/feeding
- **Pulmonary overcirculation** (if ductus remains patent and pulmonary vascular resistance falls) leading to pulmonary edema

### Age of onset / severity / progression
- Onset: **congenital**, almost always diagnosed prenatally (2nd–3rd trimester fetal echocardiogram) in current-era high-income-country practice, or in the immediate neonatal period as the ductus arteriosus closes (typically within the first 24–48 hours of life if undiagnosed prenatally).
- Severity: HLHS is intrinsically severe/lethal without intervention; within the diagnosis there is a spectrum (mitral stenosis/aortic atresia [MS/AA] vs. mitral atresia/aortic atresia [MA/AA] vs. mitral stenosis/aortic stenosis [MS/AS]) that correlates with degree of left ventricular hypoplasia, presence/severity of EFE, and postnatal outcome — the MS/AA and MA/AA subtypes generally carry higher operative risk than milder MS/AS variants.
- Progression: the anatomic lesion itself is largely fixed at birth, but the *physiologic* course is progressive if untreated (ductal closure → cardiovascular collapse → death, typically within days).

### Quality of life impact
Survivors of staged palliation show measurably lower health-related quality of life (HRQOL) than healthy peers and than children with other chronic illnesses across physical, psychosocial, emotional, social, and school-functioning domains, with the proportion of "at-risk"/impaired HRQOL increasing over childhood (e.g., total domain "at risk" 28%→39% over a longitudinal cohort) ([PMID:28847316, Cardiol Young](https://pubmed.ncbi.nlm.nih.gov/28847316/)). Neurodevelopmental dysfunction correlates strongly with worse self-reported HRQOL. Family-level dysfunction is reported in roughly a quarter of families despite overall family function often exceeding published norms.

**Suggested HPO terms (summary):** HP:0011623, HP:0011541, HP:0031624, HP:0005107, HP:0001631, HP:0001643, HP:0000961, HP:0002094, HP:0001943 (hypoglycemia).

---

## 4. Genetic/Molecular Information

### Causal genes (monogenic/major-effect)
| Gene | HGNC/OMIM | Role | Variant classification notes |
|---|---|---|---|
| **NKX2-5** | 5q35.1; OMIM 600584 (gene), 614435 (HLHS2) | Cardiac transcription factor, required for cardiac chamber specification | Missense/LOF variants reported causal in familial HLHS2 |
| **NOTCH1** | 9q34.3; OMIM 190198 | Notch signaling, valvulogenesis, ventricular trabeculation, endocardial cushion/AV canal formation | Germline dominant frameshift/stop-gain (PMID:28608148) and compound-heterozygous recessive variants (Springer 2015, "Compound heterozygous NOTCH1 mutations...") reported; hypomorphic expression alters cardiomyocyte architecture in iPSC models (bioRxiv 2024/2025) |
| **GJA1** (connexin-43) | 6q22.31 | Gap-junction protein, cardiac conduction and morphogenesis | Missense substitutions found in HLHS transplant recipients (Dasgupta et al.) |
| **HAND1** | 5q33.2 | bHLH transcription factor, left ventricular chamber morphogenesis | Includes somatic (postzygotic) mutations detected in cardiac tissue specifically |
| **MYH6** | 14q11.2 | Cardiac α-myosin heavy chain, sarcomere contractile protein | Damaging variants (missense, in-frame deletion, premature stop, de novo, compound heterozygous) enriched in ~10% of HLHS cases (PMID:26085007); associated with reduced transplant-free survival and atrial dysfunction (PMC11593362) |
| **ZIC3** | Xq26.3 | Left-right axis determination | Implicated in laterality-associated HLHS cases |
| **MCTP2** | 15q26.2 | Calcium-binding transmembrane protein, implicated by CNV/exome studies | Candidate gene |
| **SAP130, PCDHA9** | Human orthologs of Ohia mouse genes | Chromatin remodeling (SAP130, part of Sin3A/HDAC complex) and protocadherin cell-adhesion signaling | Identified via mouse forward-genetic screen; human relevance under study |

Additional genes recurrently implicated across cohort exome studies (each accounting for a small fraction of cases): AXIN1, BMP2, COL6A2, GATA4, GATA5, GDF1, MESP1, NFATC1, NKX2-6, PCSK9, TBX1, TBX18, TBX20 ([PMC9604382](https://pmc.ncbi.nlm.nih.gov/articles/PMC9604382/)).

### Variant classification and population frequency
- Per ACMG/AMP framework, most HLHS-associated variants identified to date are classified **pathogenic/likely pathogenic in a minority of cases with clear familial segregation** (e.g., NOTCH1, NKX2-5 dominant families) and **variants of uncertain significance (VUS)** in the majority of sporadic cases, given incomplete penetrance and genetic heterogeneity.
- Rare variant burden analyses show enrichment of predicted-damaging, rare (gnomAD allele frequency typically <0.1–1%) variants in HLHS probands relative to population controls, consistent with a rare-variant, multi-gene architecture rather than common-variant (GWAS-style) risk.
- **Somatic/postzygotic mosaicism**: HAND1 somatic mutations detected specifically in affected cardiac tissue (not blood) implicate postzygotic mosaicism as a contributing mechanism in at least some sporadic cases — an important methodological point, since blood-based exome sequencing alone would miss these variants.

### Functional consequences
- **Loss-of-function / haploinsufficiency**: NOTCH1, NKX2-5 — impairing normal cardiomyocyte proliferation and endocardial cushion/valve formation.
- **Dominant-negative or hypomorphic effects**: hypomorphic NOTCH1 expression (rather than complete null) alters cardiomyocyte cellular architecture in HLHS-derived iPSC models, suggesting partial pathway disruption rather than complete loss is sufficient to produce disease in the sensitized developing heart.
- **Gain/dysregulation of fibrotic signaling**: endothelial-to-mesenchymal transition (EndMT) has been identified as the mechanism underlying endocardial fibroelastosis formation in HLHS hearts, representing a downstream, convergent molecular consequence regardless of the specific upstream causal variant.

### Modifier genes
MYH6 variant status has been shown to modify **outcome** (reduced transplant-free survival) rather than acting as a primary cause in isolation in all carriers, suggesting a modifier role in some genetic backgrounds; the broader multi-gene co-occurrence pattern (e.g., patients carrying variants across AXIN1, BMP2, GATA4/5, TBX1/18/20 simultaneously) is itself consistent with an oligogenic modifier model rather than single fully penetrant drivers.

### Epigenetic information
Limited HLHS-specific epigenomic data exist in the literature relative to the volume of exome/genome work; EndMT (the EFE mechanism) is regulated in other cardiovascular fibrosis contexts by TGF-β/Smad and chromatin-modifying programs, and SAP130 (Ohia model) is itself a component of the Sin3A-HDAC histone-deacetylase corepressor complex, directly linking one of the strongest HLHS mouse candidate genes to chromatin regulation of cardiac developmental gene expression.

### Chromosomal abnormalities
See Section 2 (Turner 45,X; trisomy 13; trisomy 18; Jacobsen 11q terminal deletion) — DECIPHER and ClinVar catalog these recurrent CNV/aneuploidy associations; chromosomal microarray and karyotype are standard first-line genetic tests in a new HLHS diagnosis (see Section 10).

**Suggested ontology terms:** hgnc:7876 (NKX2-5), hgnc:7881 (NOTCH1), hgnc:4274 (GJA1), hgnc:4811 (HAND1), hgnc:7576 (MYH6); GO:0003007 (heart morphogenesis); GO:0007219 (Notch signaling pathway); GO:0001837 (epithelial to mesenchymal transition).

---

## 5. Environmental Information

- **Environmental/toxin factors**: Data specific to HLHS (vs. CHD broadly) are limited. Broader CHD literature (CTD, epidemiologic studies) implicates maternal exposure to certain organic solvents, some pesticides, and air pollution (PM2.5) as modestly associated with CHD risk generally; specificity to HLHS is not well established.
- **Lifestyle factors**: Maternal **pregestational diabetes** and **obesity** are the most consistently reported maternal risk factors across the CHD/LVOTO literature; maternal smoking and alcohol use show inconsistent associations with HLHS specifically.
- **Infectious agents**: No infectious agent is established as a direct cause of HLHS. Maternal febrile illness/rubella exposure in the first trimester is a classical general CHD risk factor (particularly for PDA and pulmonary stenosis in congenital rubella syndrome) but is not specifically linked to HLHS.

Given the paucity of HLHS-specific environmental epidemiology, curators should treat environmental risk-factor claims as extrapolated from the broader CHD/LVOTO literature unless a HLHS-specific citation is found.

---

## 6. Mechanism / Pathophysiology

### Causal chain overview
1. **Initiating lesion** — either (a) an intrinsic genetic defect in cardiomyocyte proliferation/differentiation or valvulogenesis (e.g., NOTCH1, NKX2-5, MYH6, SAP130 dysfunction), or (b) a primary mechanical/flow obstruction at the mitral or aortic valve (e.g., evolving critical aortic stenosis) — occurring in mid-gestation.
2. **Reduced left heart flow** — whichever the primary trigger, flow across the mitral valve and outflow through the aortic valve/ascending aorta becomes markedly reduced.
3. **Impaired shear-stress-dependent growth signaling** — reduced flow removes the mechanotransductive stimulus normally required for proportionate chamber and valve growth ("no-flow, no-grow" hypothesis), while intrinsic transcriptional/proliferative defects independently limit myocardial growth.
4. **Endothelial-to-mesenchymal transition (EndMT) and endocardial fibroelastosis** — abnormal endocardial shear/genetic signaling drives EndMT, producing pathological deposition of fibroelastic tissue lining the hypoplastic LV cavity, further restricting compliance and inflow.
5. **Myocardial disarray and cardiomyocyte-fibroblast imbalance** — histopathology shows disorganized myocyte architecture and a shifted fibroblast:cardiomyocyte ratio, directly contributing to the small, non-compliant, poorly contractile left ventricle.
6. **Progressive left heart hypoplasia** — by term, the mitral valve, LV, aortic valve, and ascending aorta/arch are all markedly undersized/atretic, with the ascending aorta functioning only as a retrograde-perfused conduit to the coronary arteries (via the ductus arteriosus and aortic arch) in classic aortic-atresia HLHS.
7. **Obligate right-heart/ductal-dependent physiology at birth** — after birth, systemic circulation is entirely dependent on right-to-left ductal shunting (PDA) for systemic (and often, in aortic atresia, coronary) perfusion, and on an unrestrictive interatrial communication for pulmonary venous return to reach the systemic circulation; the right ventricle serves as the sole functional systemic ventricle.
8. **Clinical decompensation** — as the ductus arteriosus physiologically closes postnatally (typically 24–72 hours), systemic and/or coronary perfusion collapses, producing shock, acidosis, and death if untreated.

### Upstream vs. downstream
- **Upstream**: genetic lesions in transcription factors/signaling genes (NOTCH1, NKX2-5, GATA4/5, TBX genes) and/or primary valvular obstruction.
- **Midstream**: reduced intracardiac flow, impaired cardiomyocyte proliferation, EndMT.
- **Downstream**: structural hypoplasia of LV/mitral/aortic valve/aorta, EFE, and — postnatally — ductal-dependent circulatory physiology and its complications (shock, end-organ hypoperfusion).

### Molecular pathways
- **NOTCH signaling** (GO:0007219) — valvulogenesis, endocardial cushion formation, ventricular trabeculation; central pathway implicated by NOTCH1 variants and hypomorphic-expression iPSC models.
- **NKX2-5/GATA4/TBX5 cardiac transcriptional network** — chamber specification and septation.
- **TGF-β/Smad signaling** — implicated in EndMT-driven endocardial fibroelastosis.
- **Sin3A-HDAC chromatin corepressor complex** (via SAP130) — implicated by the Ohia mouse model, linking chromatin regulation to left heart growth.
- **Protocadherin (PCDHA9) cell-adhesion signaling** — implicated in aortic/aortic-valve component of the Ohia digenic phenotype.

### Cellular processes
- Decreased cardiomyocyte proliferation and increased apoptosis (demonstrated in Ohia SAP130/PCDHA9 double-mutant mice)
- Altered mitochondrial maturation in cardiomyocytes
- Endothelial-to-mesenchymal transition (EndMT) in endocardium
- Myocardial disarray / disorganized sarcomeric architecture (MYH6-related)

### Protein dysfunction
- MYH6 (α-myosin heavy chain) missense/truncating variants alter sarcomeric contractile function — iPSC-cardiomyocytes carrying an MYH6 head-domain variant show measurably altered contractility (PMC7324479).
- NOTCH1 hypomorphic expression alters cardiomyocyte cellular architecture in iPSC-CM models.

### Tissue damage mechanisms
- Chronic pressure/volume mismatch and reduced coronary perfusion (especially in aortic atresia, where coronary flow is retrograde via the ductus/aortic arch) contribute to subendocardial ischemia and further myocardial injury in the hypoplastic LV.
- EFE itself is a fibrotic tissue-damage response to abnormal flow/shear stress.

### Molecular profiling / advanced technologies
- **Transcriptomics**: iPSC-cardiomyocyte models (NOTCH1-null, MYH6-variant) show altered cardiac proliferative gene programs.
- **Single-cell/functional genomics**: an eLife 2025 study ("Functional analysis across model systems implicates ribosomal proteins in growth and proliferation defects associated with HLHS") extends the candidate gene set to ribosomal protein genes affecting growth/proliferation across zebrafish, mouse, and human iPSC systems.
- **Comparative model systems**: In Vivo and In Vitro modeling reviews (PMC11538128, Curr Cardiol Rep 2024/2025) summarize convergent iPSC-CM, zebrafish, and mouse (Ohia) approaches.

**Suggested GO/CL terms:** GO:0007219 (Notch signaling pathway), GO:0003231 (cardiac ventricle development), GO:0003170 (heart valve development), GO:0001837 (EMT), GO:0006915 (apoptotic process), CL:0000746 (cardiac muscle cell / cardiomyocyte), CL:0000115 (endothelial cell), CL:0000057 (fibroblast).

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary**: heart — specifically left ventricle, mitral valve, aortic valve, ascending aorta, aortic arch.
- **Secondary/complication-related**: right ventricle (chronic systemic-ventricle pressure/volume overload, eventual dysfunction), lungs (pulmonary overcirculation or, post-Fontan, passive pulmonary blood flow and its long-term hepatic/lymphatic consequences), liver (Fontan-associated liver disease from chronically elevated systemic venous pressure), brain (neurodevelopmental sequelae from perioperative hypoxia/hypoperfusion and possible in-utero cerebral blood flow alterations), gastrointestinal tract (protein-losing enteropathy as a late Fontan complication).
- **Body systems**: cardiovascular (primary); neurological (secondary, developmental); hepatic (secondary, chronic); lymphatic (secondary — plastic bronchitis, protein-losing enteropathy).

Suggested UBERON terms: UBERON:0002094 (left ventricle), UBERON:0001917 (mitral valve), UBERON:0002137 (aortic valve), UBERON:0001496 (ascending aorta), UBERON:0001508 (aortic arch), UBERON:0002078 (right ventricle).

### Tissue and cell level
- Endocardium (site of EFE and EndMT) — CL:0002350 (endocardial cell) / CL:0000115 (endothelial cell)
- Cardiac myocytes (myocardial disarray, reduced proliferation) — CL:0000746
- Cardiac fibroblasts (imbalance with cardiomyocytes contributing to hypoplasia) — CL:0000057
- Valve interstitial/endothelial cells in the atretic/stenotic mitral and aortic valves

### Subcellular level
- Sarcomere/myofilament apparatus (MYH6-related dysfunction) — GO:0030017 (sarcomere)
- Mitochondria (altered maturation in HLHS model cardiomyocytes) — GO:0005739
- Cell-cell junctions (GJA1/connexin-43 gap junctions) — GO:0005921 (gap junction)

### Localization
- Left-sided cardiac structures — generally not "unilateral" in the laterality sense but confined to the left heart chambers/valves/great vessel; laterality-gene involvement (ZIC3) links HLHS to the broader left-right patterning disease spectrum in some cases (heterotaxy-associated single ventricle).

---

## 8. Temporal Development

### Onset
- **Congenital** — the structural lesion originates in mid-gestation cardiac development (roughly weeks 5–8 for chamber/valve formation, with progressive hypoplasia through the remainder of gestation in flow-mediated cases).
- **Onset pattern**: the anatomic lesion is present from early-to-mid fetal life; clinically, presentation is **acute** in the newborn period as the ductus arteriosus closes (if not prenatally diagnosed and managed).

### Progression
- **Fetal**: some cases show clear in-utero progression from milder mid-gestation critical aortic stenosis with a borderline (not yet frankly hypoplastic) left ventricle to fully developed HLHS by term — the rationale for fetal aortic valvuloplasty (Section 12).
- **Neonatal/staged-surgical "disease stages"**: (1) Stage I — Norwood (or hybrid) procedure in the first days of life; (2) Stage II — bidirectional Glenn/hemi-Fontan, typically 4–6 months; (3) Stage III — Fontan completion, typically age 2–4 years. Each stage represents a distinct physiologic configuration rather than "natural" disease progression, but each carries its own interstage mortality risk and morbidity profile.
- **Progression rate/pattern of the underlying disease**: after successful staged palliation, the single-right-ventricle Fontan circulation is a chronic, slowly progressive circulatory failure state — patients are at lifelong risk of Fontan-associated complications with a generally progressive (not stable) natural history over decades, though highly variable individually ("high-performing Fontan" phenotype vs. early failure).
- **Duration**: HLHS itself, uncorrected, is rapidly fatal (self-limited only in the sense that death occurs within days); with staged palliation it becomes a chronic, lifelong single-ventricle circulatory condition requiring ongoing surveillance.

### Patterns
- **Remission**: not applicable in the traditional sense — there is no biological remission; "recovery" is surgical/palliative rather than curative, and heart transplantation is the only route to biventricular-equivalent (donor heart) circulation.
- **Critical periods**: (1) the immediate ductal-closure window (first 24–72 hours of life) is the most acute critical period pre-intervention; (2) the interstage period between Stage I (Norwood) and Stage II (Glenn) carries the highest post-surgical mortality risk (interstage I mortality historically ~6.7–16% across series; [PMC11277754](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11277754/)); (3) mid-gestation (roughly 20–30 weeks) is the proposed intervention window for fetal aortic valvuloplasty in evolving HLHS.

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence**: HLHS accounts for approximately **3–4% of all congenital heart defects**. Finnish national registry data report total and live-birth prevalence of **3.66 and 1.78 per 10,000 births**, respectively ([WebSearch summary citing Finnish registry data]). Overall birth prevalence estimates across high-income-country registries typically range from ~1.6–2.6 per 10,000 live births (roughly 1 in 3,800–6,000 live births).
- **Incidence**: essentially equivalent to birth prevalence given the condition's congenital, non-acquired nature.

### Inheritance pattern
- Predominantly **multifactorial/complex** (majority of sporadic cases), with a **minority of familial cases showing autosomal dominant inheritance with reduced/incomplete penetrance** (notably NOTCH1- and NKX2-5-associated families), and rare **autosomal recessive** patterns (compound heterozygous NOTCH1, recessive MYH6 in reduced-ejection-fraction HLHS).
- **Penetrance**: incomplete in familial forms — unaffected obligate carriers of NOTCH1/NKX2-5 variants are reported, and asymptomatic relatives may show milder left-sided lesions (bicuspid aortic valve, mild LVOTO) rather than full HLHS, consistent with variable expressivity. The murine Ohia model directly demonstrates incomplete penetrance (~26% in double-homozygous SAP130;PCDHA9 mutants), providing a mechanistic parallel for human incomplete penetrance.
- **Expressivity**: highly variable — the same causal variant/family can produce phenotypes ranging from isolated bicuspid aortic valve to frank HLHS ("HLHS spectrum" or "LVOTO spectrum" concept).
- **Genetic anticipation**: not established/reported for HLHS.
- **Germline mosaicism**: plausible given somatic HAND1 mutations detected in cardiac tissue but not blood in some cases; formal germline mosaicism recurrence-risk studies are limited.
- **Founder effects**: not specifically described for HLHS.
- **Consanguinity**: recessive forms (compound heterozygous NOTCH1, recessive MYH6) are more likely to be identified in consanguineous families, though HLHS is not classically associated with high consanguinity rates the way some AR metabolic disorders are.
- **Carrier frequency**: not well established at the population level given genetic heterogeneity; not amenable to a single carrier-frequency estimate.

### Population demographics
- **Affected populations**: no strong, well-replicated ethnic-specific prevalence differential has been firmly established; some registry data suggest possible variation by ancestry, but results are inconsistent across studies.
- **Geographic distribution**: reported prevalence varies modestly across national registries (e.g., Finland ~1.78–3.66/10,000), partly reflecting differences in prenatal diagnosis/termination rates, which substantially affect livebirth prevalence figures across health systems.
- **Sex ratio**: HLHS shows a modest **male predominance** in most series (male:female roughly 1.3–1.5:1), though some analyses report near-equal distribution; sex-stratified US mortality trend data (1999–2024) have been specifically analyzed pre- and post-COVID-19 ([Frontiers in Pediatrics 2026, "Sex-stratified trends in hypoplastic left heart syndrome-related mortality among children and young adults in the United States"](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2026.1890070/full)).
- **Age distribution**: essentially all cases present prenatally or in the immediate neonatal period; the *surviving population* age distribution has shifted markedly over recent decades as surgical survival has improved, with growing cohorts now reaching adolescence and young adulthood.

---

## 10. Diagnostics

### Clinical tests
- **Echocardiography (transthoracic, fetal, and postnatal)** — the primary diagnostic modality; demonstrates diminutive/absent mitral and aortic valves, hypoplastic LV, hypoplastic ascending aorta/arch, retrograde arch flow, and ductal-dependent physiology. Fetal echocardiography (typically performed at 18–22 weeks' anatomy scan or dedicated fetal cardiac scan) is now the most common route to diagnosis in settings with routine prenatal screening.
- **Chest X-ray**: may show cardiomegaly and pulmonary vascular congestion, non-specific.
- **ECG**: right ventricular hypertrophy pattern, non-diagnostic alone.
- **Cardiac catheterization**: used selectively pre-Fontan (hemodynamic assessment of pulmonary artery pressures/resistance, collateral vessels) rather than for initial diagnosis.
- **Cardiac MRI**: increasingly used for pre-Stage II/III surgical planning and for longitudinal ventricular function/volume assessment in survivors.
- **Newborn pulse oximetry screening** (critical congenital heart disease [CCHD] screening) — recommended since 2011 by AAP/AHA as a universal newborn screen; meta-analysis of 13 studies (n=229,421) shows pooled sensitivity **76.5%** (95% CI 67.7–83.5) and specificity **99.9%** for critical CHD detection overall, with a false-positive rate of ~0.14%. HLHS is specifically highlighted as a lesion that can present with significant cardiovascular compromise with only subtle cyanosis, making pulse-oximetry screening particularly valuable as a safety-net for cases missed on prenatal ultrasound ([PMC8424789](https://pmc.ncbi.nlm.nih.gov/articles/PMC8424789/); [PMC4946827](https://pmc.ncbi.nlm.nih.gov/articles/PMC4946827/)).

### Genetic testing
- **Chromosomal microarray (CMA)** and/or **karyotype** are recommended in essentially all new HLHS diagnoses to identify Turner syndrome, trisomy 13/18, Jacobsen syndrome (11q deletion), and other CNVs.
- **Gene panel testing** for CHD-associated genes (NOTCH1, NKX2-5, GATA4, GATA5, MYH6, TBX1, TBX5, TBX20, etc.) is reasonable, particularly with a positive family history or syndromic features.
- **Whole-exome/whole-genome sequencing** is increasingly used in research and select clinical contexts (e.g., trio sequencing), given the demonstrated genetic heterogeneity; yield for a single unifying causal variant remains modest in isolated/sporadic HLHS.
- **FISH** for suspected microdeletion syndromes (e.g., 22q11.2, though more classically associated with conotruncal defects than HLHS) may be used when specific syndromic features suggest it.

### Clinical criteria / differential diagnosis
Differential diagnosis includes other ductal-dependent systemic-circulation lesions: critical aortic stenosis (without full LV hypoplasia), interrupted aortic arch, critical coarctation of the aorta, and other single-ventricle variants (e.g., unbalanced atrioventricular septal defect, double-outlet right ventricle with mitral atresia). Distinguishing features rest on echocardiographic assessment of mitral/aortic valve patency and LV size/function.

### Screening
- Routine prenatal anatomy ultrasound (18–22 weeks) with referral to fetal echocardiography for suspected four-chamber-view abnormalities is the primary population screening pathway.
- Universal newborn pulse oximetry CCHD screening serves as a postnatal safety net for prenatally undiagnosed cases.
- No population-level genetic carrier screening program exists for HLHS given its complex/heterogeneous genetic architecture; genetic counseling is offered on a family-specific basis after diagnosis.

**Suggested NCIT/LOINC terms:** NCIT:C17004 (Echocardiography), NCIT:C63668 (or relevant fetal echocardiography code), LOINC codes for neonatal pulse oximetry screening, NCIT:C15709 (Genetic Testing), NCIT term for chromosomal microarray analysis.

---

## 11. Outcome/Prognosis

### Survival and mortality
- **Untreated**: essentially uniformly fatal within days to weeks of birth.
- **Staged surgical palliation era**: high-volume centers now report **>90% hospital survival** for the Norwood (Stage I) procedure ([search summary]). Historical cohort data (post-Norwood introduction) report roughly **65% 5-year survival**.
- **Interstage mortality** (between Stage I and Stage II): reported range **2–16%** across published series, with one major single-center study reporting 6.7% interstage-I mortality and 9% stage-II mortality.
- **Long-term/adult survival**: longitudinal follow-up of the original staged-reconstruction cohorts shows only **~31% of HLHS patients alive without transplant at age 35 years** after Fontan completion ([JACC 2025, "Long-Term Survival and Patient-Reported Outcomes After Staged Reconstructive Surgery for HLHS," PMID:40533128](https://pubmed.ncbi.nlm.nih.gov/40533128/)).
- **Comparative single-ventricle outcomes**: a 2024 multicenter study found HLHS patients had a composite outcome (death, transplant, atrial arrhythmia, or thromboembolism) rate of **7.1 per 100 person-years vs. 2.1 per 100 person-years** for other single-right-ventricle physiologies, indicating HLHS carries a distinctly worse prognosis even within the broader single-ventricle population ([PMID:39604028](https://pubmed.ncbi.nlm.nih.gov/39604028/)).
- **Population mortality trends**: US age-adjusted mortality rate for HLHS declined significantly 1999–2021 in both sexes, reflecting improved surgical/perioperative care, though a more recent 2026 analysis specifically examines pre- vs. post-COVID-19 sex-stratified trends ([Frontiers in Pediatrics 2026](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2026.1890070/full)).
- **Fetal prognosis**: outcome depends heavily on presence/absence of a restrictive atrial septum, ventricular function, and associated anomalies; a restrictive/intact atrial septum in fetal HLHS is a major adverse prognostic factor requiring urgent postnatal intervention ([PMID:39625114, "Fetal hypoplastic left heart syndrome: key factors shaping prognosis"](https://pubmed.ncbi.nlm.nih.gov/39625114/)).
- **Heart transplant waitlist**: infants/children with HLHS awaiting transplant have among the highest waitlist mortality of any solid-organ transplant population (~17% in some cohorts).

### Morbidity and function
- **Neurodevelopmental outcomes**: remain a major concern despite improved survival; in one hybrid-procedure cohort only 10% showed mild developmental delay in at least one domain at 2–3 years (Bayley-III), but broader literature emphasizes persistent, only slightly improved, neurodevelopmental and intellectual impairment across the HLHS survivor population overall ([PMC6514277](https://pmc.ncbi.nlm.nih.gov/articles/PMC6514277/)).
- **Fontan-associated complications** (late morbidity): protein-losing enteropathy, plastic bronchitis, Fontan-associated liver disease/cirrhosis, atrial arrhythmias, thromboembolism, exercise intolerance, and eventual Fontan circulatory failure requiring heart transplantation in a subset.
- **Quality of life**: significantly reduced relative to healthy peers and to children with other chronic illnesses, worsening across school-age years, closely tied to neurodevelopmental status (Section 3).

### Prognostic factors
- Anatomic subtype (mitral/aortic atresia vs. stenosis variants), presence and severity of restrictive/intact atrial septum, right ventricular function, tricuspid valve competence, presence of additional cardiac or extracardiac anomalies, genetic/syndromic status (e.g., MYH6 variant carriers show reduced transplant-free survival), center surgical volume/experience, and choice of Stage I strategy (Norwood with modified Blalock-Taussig-Thomas shunt vs. Sano right-ventricle-to-pulmonary-artery conduit vs. hybrid approach) all influence outcome.
- Fetal prognostic factors specifically include atrial septal restriction, ventricular function/EFE burden, and coronary flow pattern.

---

## 12. Treatment

### Immediate medical stabilization (pre-surgical)
- **Prostaglandin E1 (alprostadil) infusion** to maintain ductal patency — cornerstone of stabilization pending surgery. NCIT term: relevant to Pharmacotherapy (NCIT:C15986); therapeutic agent alprostadil (CHEBI term for alprostadil).
- Balanced circulation management: avoidance of excess supplemental oxygen/hyperventilation (which lowers pulmonary vascular resistance and can "steal" flow from systemic circulation), sometimes with controlled hypoventilation or subambient FiO2/added CO2 to balance pulmonary:systemic flow ratio (Qp:Qs).
- Inotropic/vasoactive support and correction of metabolic acidosis as needed.
- Atrial septostomy (balloon or blade, catheter-based) if the interatrial communication is restrictive.

### Surgical/interventional — staged single-ventricle palliation
1. **Stage I — Norwood procedure** (first days of life): reconstruction of a "neoaorta" from the native pulmonary artery and hypoplastic aorta, atrial septectomy, and a source of pulmonary blood flow (modified Blalock-Taussig-Thomas shunt or Sano right-ventricle-to-pulmonary-artery conduit).
2. **Hybrid Stage I** (alternative to Norwood in select high-risk patients): bilateral pulmonary artery banding plus ductal stenting plus atrial septostomy (avoids cardiopulmonary bypass in the newborn period). Comparative meta-analysis shows hybrid patients have **higher interstage and 1-year mortality** than Norwood patients overall but **lower mortality specifically in high-risk neonates**, with no difference in 3- and 5-year mortality; hybrid patients require more unplanned interventions and longer stage-I hospitalization ([PMC11277754](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11277754/)).
3. **Stage II — bidirectional Glenn (or hemi-Fontan)** (typically 4–6 months of age): superior vena cava anastomosed to the pulmonary artery, reducing right ventricular volume load.
4. **Stage III — Fontan completion** (typically 2–4 years of age): inferior vena cava flow routed directly to the pulmonary arteries (lateral tunnel or extracardiac conduit), completing separation of systemic and pulmonary circulations with the single right ventricle supporting only systemic output.

NCIT terms: NCIT:C15329 (Surgical Procedure), NCIT:C16186 (Orthopedic Surgical Procedure — not applicable here; use general cardiac surgical procedure term), specific Norwood/Fontan/Glenn procedure NCIT codes where available; therapeutic_modality: SURGERY.

### Heart transplantation
Primary or salvage heart transplantation is used for patients with unfavorable single-ventricle anatomy, ventricular dysfunction, or failed staged palliation (including Fontan failure). Infants/children with HLHS awaiting transplant experience among the highest waitlist mortality of any pediatric solid-organ population (~17%); post-transplant outcomes, including in Jacobsen-syndrome-associated HLHS, have been specifically studied ([PMC9864704](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9864704/)). NCIT:C15289 (Organ Transplantation); therapeutic_modality: CELL_THERAPY is not correct here — this is an organ transplant, best captured as SURGERY or a dedicated transplantation category if the schema supports it.

### Fetal intervention
**Fetal aortic valvuloplasty (FAV)** — percutaneous, ultrasound-guided balloon dilation of the stenotic fetal aortic valve performed in mid-gestation (typically ~20–30 weeks) for evolving HLHS with growth-restricted but not yet fully atretic left heart structures, aiming to preserve biventricular circulation potential.
- Technical success in **84% of 143 fetuses**, with **8% fetal demise** as a procedural risk ([PMID:25052401](https://pubmed.ncbi.nlm.nih.gov/25052401/)).
- Biventricular circulation achieved postnatally in **50% of successfully treated live-born infants** vs. only **16%** of those with unsuccessful FAV.
- Among infants achieving biventricular circulation, freedom from cardiac death was **96±4% at 5 years and 84±12% at 10 years**, better than typical HLHS (single-ventricle) outcomes.
- Registered trial: ClinicalTrials.gov NCT01736956 ("Fetal Intervention for Aortic Stenosis and Evolving Hypoplastic Left Heart Syndrome").
- NCIT therapeutic_modality: SURGERY (fetal cardiac catheter intervention); relevant NCIT procedural term for balloon valvuloplasty.

### Pharmacotherapy (chronic/adjunctive)
- Diuretics (furosemide, spironolactone) for volume management
- Afterload reduction / ACE inhibitors in select single-ventricle patients
- Digoxin in some centers for interstage monitoring/heart-failure management
- Anticoagulation/antiplatelet therapy (aspirin post-shunt; warfarin or DOACs post-Fontan for thromboprophylaxis)
- Pulmonary vasodilators (e.g., sildenafil) investigated/used in some Fontan patients to improve exercise tolerance and pulmonary blood flow

### Supportive/rehabilitative care
- Interstage home-monitoring programs (weight, oxygen saturation surveillance) to reduce interstage mortality
- Nutritional support (often including tube feeding) given high metabolic demand and feeding difficulty
- Neurodevelopmental surveillance and early-intervention/rehabilitative therapy (physical, occupational, speech) given the elevated risk of developmental delay
- Psychosocial/family support given documented HRQOL and family-functioning impacts (Section 3)

### Experimental therapies
- Regenerative/cell-based approaches (e.g., autologous cardiac-derived or umbilical-cord-derived stem cell injection at time of staged surgery) have been investigated in early-phase trials for single-ventricle patients, with mixed results to date.
- Ongoing genetic and iPSC-based mechanistic research (Section 6, 15) is oriented toward eventually identifying molecularly targeted or risk-stratifying approaches, but no approved targeted pharmacotherapy currently exists for the underlying developmental defect.

### Treatment outcomes / algorithms
Treatment follows an established staged-palliation algorithm (fetal diagnosis → prenatal counseling ± fetal intervention if eligible → prostaglandin stabilization at birth → Stage I Norwood/hybrid → interstage surveillance → Stage II Glenn → Stage III Fontan → lifelong single-ventricle surveillance → transplant if/when the Fontan circulation fails), individualized by center protocol and patient-specific anatomic/physiologic risk factors.

---

## 13. Prevention

### Primary prevention
No specific primary prevention exists for HLHS given its complex, largely non-modifiable genetic/developmental etiology. General CHD-risk-reduction measures (optimization of maternal pregestational diabetes control, periconceptional folic acid/multivitamin supplementation, avoidance of known teratogens, maternal weight optimization) are reasonable extrapolated public-health measures, though HLHS-specific preventive efficacy data are lacking.

### Secondary prevention (early detection)
- Routine prenatal anatomy ultrasound with fetal echocardiography referral for suspected four-chamber-view abnormalities — the principal secondary-prevention strategy, enabling delivery-planning at a cardiac surgical center and immediate postnatal prostaglandin stabilization (preventing the catastrophic circulatory collapse that occurs with undiagnosed ductal closure).
- Universal newborn pulse-oximetry CCHD screening as a postnatal safety net (Section 10).
- Fetal aortic valvuloplasty as a secondary-prevention-like intervention aimed at halting progression from evolving/borderline left heart hypoplasia to frank HLHS (Section 12).

### Tertiary prevention (preventing complications in affected individuals)
- Interstage home-monitoring programs specifically designed to reduce interstage mortality between Stage I and Stage II palliation.
- Structured post-Fontan surveillance (echocardiography, cardiac MRI, liver imaging/elastography, protein-losing-enteropathy and plastic-bronchitis surveillance) to detect and manage late Fontan-circulation complications early.
- Thromboprophylaxis post-Fontan to reduce thromboembolic complications.
- Neurodevelopmental screening/early intervention programs to mitigate long-term developmental and quality-of-life impact.

### Genetic counseling
Offered to families after an HLHS diagnosis to discuss recurrence risk (elevated above general population risk given the complex-genetic/oligogenic architecture, particularly with identified familial variants such as NOTCH1/NKX2-5), the value of chromosomal microarray/karyotype and gene-panel testing, and reproductive options for future pregnancies (including consideration of fetal echocardiographic surveillance in subsequent pregnancies).

### Public health
Given HLHS's outsized contribution to infant CHD mortality, public-health emphasis centers on: (1) ensuring access to prenatal anatomy ultrasound/fetal echocardiography, (2) universal newborn pulse-oximetry screening implementation, and (3) regionalization of care to high-volume surgical centers, all of which have measurably improved population-level survival trends over the past two decades.

---

## 14. Other Species / Natural Disease

Naturally occurring HLHS as seen in humans is **not well documented as a spontaneous veterinary disease entity** in the same form; most animal knowledge of HLHS-like pathology derives from **engineered/induced genetic models** rather than naturally occurring veterinary cases (unlike, e.g., some inherited cardiomyopathies that occur naturally in cats and dogs). Congenital left-heart obstructive lesions (e.g., subvalvular aortic stenosis) do occur naturally in certain dog breeds (e.g., Newfoundlands, Golden Retrievers) and are cataloged in OMIA (Online Mendelian Inheritance in Animals), but these represent a related-but-distinct phenotype (isolated aortic stenosis without the full LV/mitral/aortic-arch hypoplasia complex defining HLHS) rather than a direct naturally occurring HLHS analog.

**Comparative/orthologous genes**: mouse Nkx2-5, Notch1, Gja1, Hand1, Myh6, Sap130, and Pcdha9 are the principal orthologs used in engineered models (Section 15); NCBI Gene orthology mapping is straightforward for each given high mammalian conservation of these developmental genes.

**Zoonotic potential / transmission**: not applicable — HLHS is a non-communicable congenital developmental disorder.

---

## 15. Model Organisms

### Mouse models
- **Ohia mouse line** — the flagship genetic mouse model, identified through an ENU forward-genetic mutagenesis screen of ~3,000 mice for cardiac laterality/structural defects. Carries **compound heterozygous/digenic mutations in Sap130 and Pcdha9**; double-homozygous mutants show HLHS-like phenotype with **~26% penetrance** — directly demonstrating incomplete penetrance and a **digenic/two-locus requirement** paralleling the oligogenic model proposed for human HLHS ([In Vivo and In Vitro Approaches to Modeling HLHS, PMC11538128](https://pmc.ncbi.nlm.nih.gov/articles/PMC11538128/); related CRISPR/Cas9-edited SAP130/PCDHA9 double-mutant studies).
  - **Gene-specific phenotype dissection**: Sap130 mutation drives the **left ventricular hypoplasia** component; Pcdha9 mutation drives the **aortic/aortic-valve** component — an elegant demonstration that combining two distinct developmental lesions reproduces the full HLHS phenotype.
  - **Cellular phenotype**: increased cardiomyocyte apoptosis, decreased cardiomyocyte proliferation, altered mitochondrial maturation.
  - **Physiological recapitulation**: a related mouse model paper specifically demonstrates **left heart hypoplasia and retrograde aortic arch flow**, directly recapitulating the classic human fetal echocardiographic finding ([PMC8592017, "A mouse model of hypoplastic left heart syndrome demonstrating left heart hypoplasia and retrograde aortic arch flow"](https://pmc.ncbi.nlm.nih.gov/articles/PMC8592017/)).
  - **Placental phenotype**: the Ohia line also shows placental and fetal abnormalities that recapitulate human HLHS outcomes, though this raises a **model-fidelity caveat** — placental abnormalities could themselves contribute to (or confound) the cardiac phenotype and may relate to the embryonic lethality seen in some homozygous double mutants, limiting direct translational inference to human HLHS pathogenesis versus a placental-mediated secondary effect.
- **Endocardial fibroelastosis animal model**: distention of the immature left ventricle has been shown to **trigger EFE development**, providing an induced (non-genetic, mechanical) model supporting the flow/hemodynamic theory and reproducing key morphopathological features of evolving fetal HLHS ([PMC4433646](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4433646/)).

### iPSC / in vitro models
- **NOTCH1-null and hypomorphic human iPSC-cardiomyocyte (hiPSC-CM) models**: NOTCH1 deficiency downregulates cardiac proliferative gene programs, producing stunted hiPSC-CM proliferation in vitro; hypomorphic (rather than complete null) NOTCH1 expression specifically alters cardiomyocyte cellular architecture, a 2024/2025 bioRxiv study directly relevant to the partial-loss-of-function genetic architecture seen in human HLHS families.
- **MYH6-variant patient-derived iPSC-CMs**: iPSC-cardiomyocytes carrying a patient-derived MYH6 head-domain variant show measurably altered contractility, functionally validating the pathogenicity of this variant class ([PMC7324479](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7324479/)).
- **KMT2D-NOTCH interaction model**: implicates KMT2D-NOTCH signaling in coronary artery abnormalities associated with HLHS (bioRxiv 2021).

### Zebrafish and cross-species functional screens
- A 2025 eLife study ("Functional analysis across model systems implicates ribosomal proteins in growth and proliferation defects associated with hypoplastic left heart syndrome") integrates **zebrafish, mouse, and human iPSC systems** to functionally validate ribosomal-protein candidate genes affecting cardiac growth/proliferation, illustrating the current cross-species functional-genomics approach to HLHS candidate gene validation.

### Model characteristics and limitations
- **Phenotype recapitulation**: the Ohia mouse and mechanical LV-distention models each capture specific facets of human HLHS (structural digenic hypoplasia; EFE formation via flow disturbance, respectively), but no single current model fully recapitulates the entire human phenotype (genetic heterogeneity + flow-mediated growth arrest + EFE + postnatal ductal-dependent physiology) simultaneously.
- **Limitations**: placental confounding in the Ohia line; iPSC-CM models capture cell-autonomous proliferation/contractility defects but cannot model in-vivo hemodynamic/flow contributions or the full 3D valve/chamber morphogenetic process; most models address either the genetic or the hemodynamic arm of pathogenesis rather than their interaction.
- **Applications**: candidate gene validation (functional confirmation of exome-sequencing hits), mechanistic dissection of EndMT/EFE formation, drug/therapeutic screening in iPSC-CM platforms, and testing of the combined genetic-plus-hemodynamic ("two-hit") pathogenesis model.

### Resources
Model organism databases relevant to HLHS research: **MGI** (Mouse Genome Informatics, for Ohia/Sap130/Pcdha9/Notch1/Nkx2-5/Gja1/Hand1/Myh6 alleles), **IMPC/KOMP** (systematic mouse knockout phenotyping), **ZFIN** (zebrafish orthologs), and patient-derived **iPSC repositories** (e.g., through the Pediatric Cardiac Genomics Consortium biobank).

**Suggested NCBITaxon/model terms:** NCBITaxon:10090 (Mus musculus), NCBITaxon:7955 (Danio rerio); relevant MGI allele IDs for the Ohia Sap130/Pcdha9 compound mutant.

---

## Summary of Key Ontology Term Suggestions

| Category | Suggested terms |
|---|---|
| Disease | MONDO:0004933, OMIM:241550/614435, ORPHA:2248 |
| Phenotypes (HP) | HP:0011623 (mitral atresia), HP:0011541 (aortic valve atresia), HP:0031624 (hypoplastic left heart), HP:0005107 (aortic hypoplasia), HP:0001631 (ASD), HP:0001643 (PDA), HP:0000961 (cyanosis) |
| Genes (HGNC) | hgnc:7876 (NKX2-5), hgnc:7881 (NOTCH1), hgnc:4274 (GJA1), hgnc:4811 (HAND1), hgnc:7576 (MYH6), hgnc:12873 (ZIC3) |
| Biological processes (GO) | GO:0007219 (Notch signaling), GO:0003231 (cardiac ventricle development), GO:0003170 (heart valve development), GO:0001837 (EMT), GO:0006915 (apoptosis) |
| Cell types (CL) | CL:0000746 (cardiomyocyte), CL:0000115 (endothelial cell), CL:0000057 (fibroblast) |
| Anatomy (UBERON) | UBERON:0002094 (left ventricle), UBERON:0001917 (mitral valve), UBERON:0002137 (aortic valve), UBERON:0001496 (ascending aorta) |
| Treatments (NCIT) | NCIT:C15986 (Pharmacotherapy — alprostadil), NCIT:C15329 (Surgical Procedure — Norwood/Glenn/Fontan), NCIT:C15289 (Organ Transplantation) |

---

## Notes on Evidence Gaps

- HLHS-specific environmental epidemiology (Section 5) is sparse relative to genetic literature; most environmental claims are extrapolated from the broader CHD/LVOTO spectrum and should be flagged as lower-confidence if curated.
- Population-level GWAS/common-variant data specific to HLHS are limited; the genetic architecture literature is dominated by rare-variant/exome-sequencing case-cohort studies rather than large-scale GWAS.
- No naturally occurring veterinary HLHS analog is well established; animal-model evidence is entirely from engineered/induced systems (Section 14–15), which curators should note as a MODEL_SYSTEM evidence-source classification.
- Direct gene-environment interaction studies specific to HLHS were not identified in this search; the "two-hit" genetic-plus-hemodynamic model remains largely conceptual/inferential rather than directly demonstrated in a single unified human dataset, though the Ohia mouse digenic model provides a genetic-locus parallel.

Sources:
- [Hypoplastic Left Heart Syndrome - StatPearls - NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK554576/)
- [Hypoplastic left heart syndrome—a scoping review (PMID:40386366)](https://pubmed.ncbi.nlm.nih.gov/40386366/)
- [OMIM 241550 - HYPOPLASTIC LEFT HEART SYNDROME 1](https://omim.org/entry/241550)
- [OMIM 614435 - HYPOPLASTIC LEFT HEART SYNDROME 2](https://omim.org/entry/614435)
- [Orphanet: Hypoplastic left heart syndrome (ORPHA:2248)](https://www.orpha.net/en/disease/detail/2248)
- [Hypoplastic Left Heart Syndrome Sequencing Reveals a Novel NOTCH1 Mutation (PMID:28608148)](https://pubmed.ncbi.nlm.nih.gov/28608148/)
- [Considering the Genetic Architecture of Hypoplastic Left Heart Syndrome - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9604382/)
- [Compound heterozygous NOTCH1 mutations underlie impaired cardiogenesis](https://link.springer.com/article/10.1007/s00439-015-1582-1)
- [Frontiers: Sex-stratified trends in HLHS-related mortality 1999–2024](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2026.1890070/full)
- [Long-Term Survival and Patient-Reported Outcomes After Staged Reconstructive Surgery for HLHS (JACC, PMID:40533128)](https://pubmed.ncbi.nlm.nih.gov/40533128/)
- [Risk factors for mortality in patients with HLHS after the Norwood procedure - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10448988/)
- [Fetal hypoplastic left heart syndrome: key factors shaping prognosis (PMID:39625114)](https://pubmed.ncbi.nlm.nih.gov/39625114/)
- [Cardiovascular Outcomes Associated With HLHS Versus Other Single Right Ventricle (PMID:39604028)](https://pubmed.ncbi.nlm.nih.gov/39604028/)
- [Is There a Unified Etiology of HLHS? (PMID:42200818)](https://pubmed.ncbi.nlm.nih.gov/42200818/)
- [Distention of the Immature Left Ventricle Triggers EFE - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4433646/)
- [Jacobsen Syndrome with HLHS: Outcome after Cardiac Transplantation - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9864704/)
- [A Rare Combination of Chromosomal Abnormalities in an Infant With Turner Syndrome and HLHS - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8375010/)
- [Fetal aortic valvuloplasty for evolving HLHS: postnatal outcomes of the first 100 patients (PMID:25052401)](https://pubmed.ncbi.nlm.nih.gov/25052401/)
- [Fetal Intervention for Aortic Stenosis and Evolving HLHS - ClinicalTrials.gov NCT01736956](https://clinicaltrials.gov/study/NCT01736956)
- [A mouse model of HLHS demonstrating left heart hypoplasia and retrograde aortic arch flow - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8592017/)
- [In Vivo and In Vitro Approaches to Modeling HLHS - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11538128/)
- [Functional analysis across model systems implicates ribosomal proteins in growth and proliferation defects associated with HLHS - eLife](https://elifesciences.org/articles/106231)
- [The Genetic Landscape of Hypoplastic Left Heart Syndrome (PMID:29569026)](https://pubmed.ncbi.nlm.nih.gov/29569026/)
- [Comparison of Morbidity and Mortality Outcomes between Hybrid Palliation and Norwood Palliation Procedures - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11277754/)
- [Neurodevelopmental outcome in HLHS after hybrid procedure - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6514277/)
- [Impact of MYH6 variants in hypoplastic left heart syndrome - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5206387/)
- [Recessive MYH6 Mutations in Hypoplastic Left Heart With Reduced Ejection Fraction (PMID:26085007)](https://pubmed.ncbi.nlm.nih.gov/26085007/)
- [MYH6 Variants Are Associated with Atrial Dysfunction in Neonates with HLHS - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11593362/)
- [Contractility of iPSC-Cardiomyocytes With an MYH6 Head Domain Variant Associated With HLHS - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7324479/)
- [Newborn pulse oximetry screening for critical congenital heart defects - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8424789/)
- [Pulse oximetry screening: a review of diagnosing critical congenital heart disease in newborns - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4946827/)
- [Children with hypoplastic left heart syndrome have lower quality of life than healthy controls (PMID:28847316)](https://pubmed.ncbi.nlm.nih.gov/28847316/)
- [Hypoplastic Left Heart Syndrome Across the Lifespan - Canadian Journal of Cardiology](https://onlinecjc.ca/article/S0828-282X(22)00290-2/fulltext)