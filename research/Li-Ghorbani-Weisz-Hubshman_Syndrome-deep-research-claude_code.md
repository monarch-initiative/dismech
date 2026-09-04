---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T14:25:16.073506'
end_time: '2026-08-27T14:28:32.749273'
duration_seconds: 196.68
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Li-Ghorbani-Weisz-Hubshman Syndrome
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
  web_search_requests: 11
  num_turns: 18
  total_cost_usd: 0.9235589999999998
  session_id: 98b3127c-432a-57dc-acc9-774218ba8a79
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 15
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Li-Ghorbani-Weisz-Hubshman Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Li-Ghorbani-Weisz-Hubshman Syndrome** covering all of the
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

Good, I have the core identity established (KAT8, OMIM #618974, MONDO:0033547). Now let me fetch the primary OMIM entry, clinical synopsis, MedGen, MalaCards, and the founding PubMed paper for detailed data.

Excellent, found the primary paper: PMID:31794431 (PMC7269600). Let me fetch the full text for detailed mechanism, phenotype, and genetics data, plus other key sources in parallel.

# Li-Ghorbani-Weisz-Hubshman Syndrome (LIGOWS): Comprehensive Research Report

## 1. Disease Information

### Overview
Li-Ghorbani-Weisz-Hubshman syndrome (LIGOWS) is a rare, autosomal dominant (with one reported autosomal recessive family) neurodevelopmental disorder caused by heterozygous (or, rarely, biallelic) pathogenic variants in **KAT8** (Lysine Acetyltransferase 8, also known as *MOF*/*MYST1*) on chromosome 16p11.2. It was first delineated in 2020 by Li, Ghorbani, Weisz-Hubshman and colleagues, who identified pathogenic *KAT8* variants in 9 unrelated individuals with intellectual disability, seizures, autism, dysmorphic features, and other congenital anomalies, and mechanistically linked the disorder to impaired histone H4 lysine 16 acetylation (H4K16ac) ([Li et al. 2020, *J Clin Invest* 130(3):1431-1445, PMID:31794431](https://pmc.ncbi.nlm.nih.gov/articles/PMC7269600/)).

### Key Identifiers
| Resource | ID |
|---|---|
| OMIM phenotype | **#618974** — LI-GHORBANI-WEISZ-HUBSHMAN SYNDROME; LIGOWS ([omim.org/entry/618974](https://omim.org/entry/618974)) |
| OMIM gene | **\*609912** — KAT8 (Lysine Acetyltransferase 8) |
| MONDO | **MONDO:0033547** ([monarchinitiative.org/MONDO:0033547](https://monarchinitiative.org/MONDO:0033547)) |
| MedGen | **C5436525** / UID 1763263 ([ncbi.nlm.nih.gov/medgen/1763263](https://www.ncbi.nlm.nih.gov/medgen/1763263)) |
| Gene symbol / HGNC | KAT8 / HGNC:17933 |
| Gene location | 16p11.2 |
| Inheritance | Autosomal dominant (predominant); rare autosomal recessive reported |

### Synonyms
"LIGOWS," "Li-Ghorbani-Weisz-Hubshman syndrome," and informally "KAT8-related neurodevelopmental disorder" / "KAT8-associated intellectual disability."

### Data provenance note
Nearly all clinical characterization derives from a single aggregated, multi-center case series (the founding 2020 report), not from population-level EHR data or disease registries — this is a very recently delineated ultra-rare Mendelian disorder with a small published cohort (9 probands in the original description; independent replication cohorts are sparse in subsequent literature searches).

---

## 2. Etiology

### Disease Causal Factors
LIGOWS is caused by **de novo heterozygous missense (and one nonsense) variants in KAT8**, with one family showing biallelic (compound heterozygous) inheritance from unaffected carrier parents, suggesting rare autosomal recessive transmission with possible incomplete penetrance for milder alleles (PMID:31794431).

### Genetic Risk Factors
- **Causal variant class:** De novo heterozygous missense variants clustering in two functional domains of KAT8: the **chromobarrel domain** (nucleosome/histone recognition) and the **catalytic MYST domain** (acetyl-CoA binding/enzymatic activity).
- A **recurrent de novo variant**, c.269A>G (p.Tyr90Cys), was found independently in three unrelated patients (T1–T3), indicating a mutational hotspot in the chromobarrel domain.
- No modifier genes have yet been reported.

### Environmental Risk Factors
None identified; this is a purely monogenic disorder with no established environmental, infectious, or lifestyle contribution to causation.

### Protective Factors
None reported in the literature to date.

### Gene-Environment Interactions
Not applicable/not studied — no data on environmental modulation of penetrance or severity.

---

## 3. Genetic/Molecular Information

### Causal Gene
**KAT8** (Lysine Acetyltransferase 8; aliases *MOF*, *MYST1*, *hMOF*), HGNC:17933, OMIM \*609912, located at 16p11.2. KAT8 encodes a MYST-family histone acetyltransferase with a chromobarrel domain (histone/nucleosome recognition), an acetyl-CoA-binding MYST catalytic domain, and a C2HC-type zinc finger ([GeneCards](https://www.genecards.org/card/KAT8)).

### Pathogenic Variants Identified (Li et al. 2020, PMID:31794431)

| Patient(s) | Nucleotide change | Protein change | Domain | Zygosity |
|---|---|---|---|---|
| T1, T2, T3 | c.269A>G | p.Tyr90Cys | Chromobarrel | De novo heterozygous |
| T4 | c.293G>A | p.Arg98Gln | Chromobarrel | De novo heterozygous |
| T5 | — | p.Arg99Gln | Chromobarrel | De novo heterozygous |
| T6 | — | p.Ala165Val | Catalytic (MYST) | De novo heterozygous |
| T7 | c.523A>G | p.Lys175Glu | Catalytic (MYST) | De novo heterozygous |
| T8 | — | p.Lys181Arg | Catalytic (MYST) | De novo heterozygous |
| T9 | compound: missense + nonsense | p.Arg325Cys + p.Lys175* (c.523A>T, nonsense at codon 176) | Acetyl-CoA binding motif + C-terminal truncation | Biallelic (inherited from unaffected parents) |

- **Variant classification:** All are classified pathogenic/likely pathogenic per ACMG/AMP criteria in ClinVar (e.g., [RCV001253776 for p.Tyr90Cys](https://www.ncbi.nlm.nih.gov/clinvar/RCV001253776/); [RCV001253778 for p.Lys175Glu](https://www.ncbi.nlm.nih.gov/clinvar/RCV001253778/)); GenCC lists KAT8–LIGOWS as an autosomal dominant "Definitive"/"Strong" gene-disease relationship (Ambry Genetics submission, [GenCC entry](https://search.thegencc.org/submissions/GENCC_000101-HGNC_17933-OMIM_618974-HP_0000006-GENCC_100003)).
- **Variant type:** Predominantly missense; one nonsense allele (biallelic case only).
- **Population allele frequency:** Not reported in gnomAD (consistent with de novo, ultra-rare pathogenic status); not found as common polymorphisms.
- **Somatic vs. germline:** All germline (constitutional), no somatic mosaicism reported.
- **Functional consequence:** Loss-of-function at the biochemical level — all seven tested missense variants were "defective in acetylating histone H4 at lysine 5 or 16 when recombinant nucleosomes were used as substrate," despite normal protein expression levels and (for most variants) normal complex assembly with MSL proteins. Chromobarrel-domain variants (Tyr90Cys, Arg98Gln, Arg99Gln) showed the most severe functional impact, consistent with impaired nucleosome engagement.

### Modifier Genes
None established.

### Epigenetic Information
This is fundamentally an **epigenetic-machinery disorder**: KAT8 is the enzyme that writes the H4K16ac mark. Pathogenic variants cause a downstream, genome-wide epigenetic deficiency (loss of H4K16 acetylation) rather than acting through a separate epigenetic mechanism.

### Chromosomal Abnormalities
Not applicable — LIGOWS results from point mutations in KAT8, not large chromosomal rearrangements. (Note: microdeletion of the adjacent/nearby 16p11.2 region causes a distinct, well-known 16p11.2 deletion syndrome, which should be considered as a differential rather than confused with LIGOWS.)

**Suggested ontology terms:** Gene — `hgnc:17933` (KAT8); functional impact — `LOSS_OF_FUNCTION` (catalytic/enzymatic) at `functional_impact_category`.

---

## 4. Phenotypes

### Neurological / Developmental (Human, HP-codable)
| Feature | Frequency in cohort (n=9) | Suggested HP term |
|---|---|---|
| Global developmental delay | 9/9 (universal) | HP:0001263 |
| Intellectual disability (mild–moderate) | 9/9 (universal) | HP:0001249 |
| Delayed speech and language development | 9/9 | HP:0000750 |
| Delayed motor development (gross/fine) | Most patients | HP:0001270 / HP:0011342 |
| Seizures / epilepsy | 7/9 | HP:0001250 |
| Autistic behavior | 2/9 | HP:0000729 |
| ADHD | 1/9 (T2) | HP:0007018 |
| Behavioral abnormalities (incl. difficulty with numbers/money concepts) | Subset | HP:0000708 |

### Brain Imaging (structural)
- Ventriculomegaly / enlarged ventricles — HP:0002119
- Thin/hypoplastic corpus callosum — HP:0002079 / HP:0033725
- Periventricular / gray matter nodular heterotopia — HP:0002185
- Decreased white matter volume — HP:0034185

### Craniofacial Dysmorphism (recurrent pattern)
Upper lateral eyelid fullness, telecanthus (HP:0000506), epicanthus (HP:0000286), upslanted palpebral fissures (HP:0000582), depressed/prominent nasal bridge (HP:0000431/HP:0000426), mild malar hypoplasia (HP:0000272), thick vermilion border (HP:0012471), downturned corners of the mouth (HP:0002714), low-set ears (HP:0000369).

### Cardiac
Cardiac defects (atrial septal defect, ventricular septal defect, patent ductus arteriosus) in 4/9 patients — HP:0001631, HP:0001629, HP:0001643.

### Ophthalmologic
Esotropia (HP:0000565), hypermetropia (HP:0000540), hypotelorism (HP:0000601).

### Other Systemic
Feeding difficulties in infancy (HP:0011968); limb anomalies including clinodactyly (HP:0030084) and overlapping toes (HP:0001845).

### Phenotype Characteristics
- **Onset:** Congenital/infantile (developmental delay and dysmorphism present from early childhood).
- **Severity:** Mild-to-moderate intellectual disability predominates (not severe/profound in the reported cohort).
- **Progression:** Static/developmental (not degenerative) — a neurodevelopmental rather than neurodegenerative course.
- **Frequency data:** As tabulated above from the n=9 founding cohort; broader population-level frequencies are not yet established given the rarity of the condition.

### Quality of Life
Not formally studied with standardized instruments (EQ-5D/SF-36) in the literature to date; qualitatively, affected individuals require developmental/educational support consistent with mild-moderate intellectual disability.

---

## 5. Mechanism / Pathophysiology

### Molecular Function of KAT8
KAT8 is a MYST-family lysine acetyltransferase that operates as the catalytic subunit of two distinct, evolutionarily conserved multiprotein complexes:
- **MSL complex** (Male-Specific Lethal: MSL1, MSL2, MSL3) — within this complex, KAT8 catalyzes the bulk of genome-wide **H4K16 acetylation**, marking open chromatin and decompacting the chromatin fiber.
- **NSL complex** (Non-Specific Lethal, containing KANSL1 and related subunits) — within this complex, KAT8 instead acetylates **H4K5 and H4K8** at gene promoters, driving transcriptional activation of essential/housekeeping genes.

("KAT8 serves as a catalytic subunit of two independent protein complexes conserved from Drosophila to mammals... it catalyzes H4K5ac and H4K8ac as part of the NSL complex, whereas it catalyzes the bulk of H4K16ac as part of the MSL complex" — [Molecular Cell 2021](https://www.cell.com/molecular-cell/fulltext/S1097-2765(21)00098-8).)

### Causal Chain (Mechanism → Phenotype)
1. **Molecular trigger:** De novo missense variant in KAT8 chromobarrel or catalytic domain → impaired nucleosome recognition or catalytic (acetyl-CoA transfer) activity.
2. **Biochemical consequence:** Severely reduced H4K16 (and H4K5) acetylation on nucleosomal substrates in vitro, despite normal protein expression and (mostly) normal MSL-complex assembly.
3. **Cellular consequence (from Kat8 cerebrum-conditional knockout mice):**
   - Loss of H4K16ac in the cerebrocortical neuroepithelium as early as E12.5.
   - Reduced SOX2+ neural stem/progenitor cells (NSPCs) by E13.5.
   - Premature/excessive neurogenesis: increased Tuj1+ neurons with aberrant migration.
   - Reduced proliferation (fewer BrdU+/Ki-67+ cells) and massive apoptosis (TUNEL+, cleaved caspase-3) at E12.5–E13.5.
   - Complete failure of mutant NSPCs to form neurospheres in vitro; pharmacologic KAT8 inhibition (MG149) similarly abolished wild-type neurosphere formation.
4. **Tissue/organ consequence:** Severe cerebral (neocortical and hippocampal) hypoplasia, altered cortical lamination, "flat-head" skull phenotype, and perinatal lethality in the mouse model.
5. **Organism-level phenotype:** In humans — global developmental delay, intellectual disability, seizures, structural brain anomalies (ventriculomegaly, thin corpus callosum, heterotopia), and craniofacial dysmorphism.

**Suggested GO terms:** `GO:0043984` (histone H4-K16 acetylation), `GO:0043974` (histone H4-K5 acetylation), `GO:0043982` (histone H4-K8 acetylation), `GO:0022008` (neurogenesis), `GO:0007399` (nervous system development), `GO:0006325` (chromatin organization). **Suggested CL terms:** `CL:0000047` (neural stem cell) / neural progenitor cell equivalents.

### Additional Molecular Finding
KAT8 also catalyzes **H4K16 propionylation** in vivo (a novel, less-studied acyl mark), with distinct subnuclear distribution from acetylation; this mark was virtually absent in Kat8-mutant neuroepithelium, suggesting a "complementary mechanism" active when propionyl-CoA levels are elevated.

### Counterbalancing Deacetylases
SIRT1 and SIRT2 are candidate H4K16 deacetylases; HDAC1/2/3 are also important for cerebral development (HDAC3 loss causes H4K16 *hyper*acetylation), framing KAT8 loss-of-function within a broader acetylation/deacetylation balance relevant to potential therapeutic modulation.

### Related Disease Mechanisms (for context/differential)
The paper situates LIGOWS within a family of "Mendelian disorders of the epigenetic machinery" acting on H4/H3 acetylation: CREBBP/EP300 (Rubinstein-Taybi syndrome, H3K27ac), KAT6A/KAT6B (H3K23ac), BRPF1, KANSL1 (Koolen-de Vries syndrome, part of the NSL complex), and MSL3 (recently linked to an X-linked developmental disorder, Basilicata-Akhtar syndrome).

---

## 6. Anatomical Structures Affected

- **Organ level (primary):** Central nervous system — cerebral cortex, hippocampus (UBERON:0000956, UBERON:0002421).
- **Secondary/associated:** Heart (septal structures, ductus arteriosus), craniofacial skeleton, eyes.
- **Tissue/cell level:** Neuroepithelium; neural stem/progenitor cells; cortical neurons (Tuj1+); chromatin/nucleosomes at the subcellular level.
- **Subcellular:** Nucleus/chromatin — GO Cellular Component `GO:0000786` (nucleosome), `GO:0005634` (nucleus).
- **Localization:** Bilateral, diffuse cerebral involvement (not lateralized); structural brain findings (ventriculomegaly, thin corpus callosum, heterotopia) are typically bilateral/symmetric.

---

## 7. Temporal Development

- **Onset:** Congenital/prenatal at the molecular-developmental level (mouse data show defects from E12.5–E16.5); clinically apparent as **infantile/early childhood** developmental delay.
- **Progression:** Neurodevelopmental (static/non-degenerative) — features reflect an early developmental insult rather than progressive tissue loss; seizures may emerge in childhood.
- **Disease course:** Chronic, lifelong intellectual disability; no reports of regression.
- **Critical period:** Embryonic corticogenesis (E12.5–E16.5 in mouse models) represents the developmental window of maximal vulnerability to KAT8 loss-of-function.

---

## 8. Inheritance and Population

### Epidemiology
LIGOWS is an ultra-rare, only recently delineated disorder (2020). No formal prevalence or incidence estimates exist in Orphanet, GBD, or other epidemiological databases; the literature to date describes single-digit numbers of published cases (originally 9 in the founding cohort), so it should be treated as **CASES_IN_LITERATURE**-tier for prevalence purposes rather than a population rate.

### Inheritance Pattern
- **Predominant:** Autosomal dominant, de novo (8 of 9 original patients).
- **Rare alternative:** Autosomal recessive/biallelic — one patient (T9) inherited compound heterozygous variants from unaffected parents, suggesting incomplete penetrance of milder alleles in the heterozygous carrier state.
- **Penetrance:** Appears high for de novo heterozygous variants (all reported de novo carriers were affected); incomplete for at least one biallelic-context allele (unaffected heterozygous parents).
- **Expressivity:** Variable — severity and specific features (seizures, cardiac defects, autism) vary among carriers of different (and even the same) variant.
- **Anticipation, mosaicism, founder effects, consanguinity, carrier frequency:** Not reported/not applicable given the ultra-rare de novo nature of the disorder.

### Population Demographics
- **Affected populations:** No specific ethnic or geographic enrichment reported; patients were ascertained through international collaborative exome-sequencing efforts.
- **Sex ratio:** Not reported as skewed (autosomal gene, not X-linked).
- **Age distribution:** Pediatric ascertainment predominant (patients described in the founding cohort ranged from early childhood through adolescence, e.g., ages 2–18 reported across summaries).

---

## 9. Diagnostics

### Genetic Testing (primary diagnostic modality)
- **Exome sequencing (WES)** was the method by which all founding-cohort variants were identified — the most direct approach given the absence of a specific hotspot outside the recurrent p.Tyr90Cys allele.
- **Whole genome sequencing (WGS):** Not specifically reported but would be expected to detect the same coding variants.
- **Gene panels:** Intellectual disability/epilepsy/neurodevelopmental gene panels including KAT8 would be expected to capture pathogenic variants.
- **Single-gene (Sanger) testing:** Appropriate for confirming a specific familial variant or the recurrent p.Tyr90Cys allele.
- **Chromosomal microarray / karyotype / FISH:** Not causal for this disorder (point mutations, not large CNVs), though CMA is often part of a standard ID/developmental-delay diagnostic workup to exclude 16p11.2 deletion/duplication and other CNV syndromes as differentials.

### Functional/Research-Level Diagnostics
Patient-derived cell acetyltransferase assays (H4K16/H4K5 acetylation on nucleosome substrates) were used in the discovery study to establish variant pathogenicity but are not standard clinical diagnostics.

### Clinical Criteria
No formal consensus diagnostic criteria (DSM/ICD-specific) exist; diagnosis rests on the combination of the clinical phenotype (developmental delay, dysmorphism, brain imaging findings) plus confirmatory KAT8 variant identification.

### Differential Diagnosis
Other "Mendelian disorders of the epigenetic machinery" with overlapping intellectual disability/dysmorphism phenotypes: Rubinstein-Taybi syndrome (CREBBP/EP300), KAT6A syndrome (Arboleda-Tham syndrome), KAT6B disorders, Koolen-de Vries syndrome (KANSL1 — same NSL complex), Basilicata-Akhtar syndrome (MSL3 — same MSL complex as KAT8), and 16p11.2 microdeletion/duplication syndrome (distinct etiology, nearby locus).

### Screening
No population or newborn screening programs exist; this is a variant-level, symptomatic diagnostic pathway (typically initiated by developmental delay/ID/seizure workup).

---

## 10. Outcome / Prognosis

- **Survival/mortality:** No mortality data reported in the human cohort (contrast with the fully penetrant perinatal lethality of the cerebrum-specific Kat8 mouse knockout, which is a complete-loss-of-function model rather than the partial-loss-of-function missense alleles seen in patients).
- **Morbidity/function:** Lifelong mild-to-moderate intellectual disability with associated speech/language impairment; a minority have autism or ADHD features; epilepsy present in ~78% (7/9) of the founding cohort.
- **Complications:** Structural cardiac defects requiring cardiology follow-up in ~44% (4/9); seizure disorder requiring anticonvulsant management.
- **Prognostic factors:** Variant domain may correlate with severity — chromobarrel-domain variants showed the most severe biochemical (H4K16ac) impairment in functional assays, though a clear genotype-severity correlation in patients has not yet been formally established in a larger cohort.

---

## 11. Treatment

### Pharmacotherapy — Seizure Management
**Valproate (valproic acid)** was used in 2 of the 7 patients with epilepsy in the founding cohort, and both were responsive. The proposed mechanistic rationale is that valproate, a histone deacetylase (HDAC) inhibitor, may partially compensate for the acetylation deficiency caused by KAT8 loss-of-function ("may ameliorate potential acetylation deficiency resulting from KAT8 impairment" — PMID:31794431).

**Suggested NCIT term:** `NCIT:C15986` (Pharmacotherapy), with `therapeutic_agent` bound to valproic acid (CHEBI, if available) as an anticonvulsant/HDAC inhibitor.

### Experimental/Preclinical
Authors propose that **Kat8-mutant mice may serve as preclinical models for testing deacetylase inhibitor drugs** (e.g., valproic acid) as a therapeutic strategy — this remains a research-stage concept, not an established clinical protocol, and no clinical trials specific to LIGOWS (NCT identifiers) were identified in the literature searched.

### Supportive/Multidisciplinary Care
As for intellectual disability generally, management requires a multidisciplinary team: special education, speech-language therapy, behavioral therapy, occupational therapy, and social/community support services (`NCIT:C15302` Physical Therapy, `NCIT:C15747` Supportive Care, as broadly applicable but not KAT8-specific).

### Cardiac
Standard cardiology management/surgical correction as indicated for septal defects/PDA in affected patients (`NCIT:C15329` Surgical Procedure where structural repair is needed).

### Gene-targeted/Precision Approaches
None reported — no gene therapy, ASO, or targeted molecular therapy has been developed or trialed for KAT8-related disease as of the literature available.

---

## 12. Prevention

No primary, secondary, or tertiary prevention strategies exist for this de novo genetic disorder beyond standard **genetic counseling** for recurrence risk (low for de novo cases; up to 25% per pregnancy in the rare biallelic/autosomal-recessive family pattern) and prenatal/preimplantation genetic testing where a familial variant is known. No immunization, screening program, or behavioral intervention is applicable to primary prevention of this monogenic disorder.

---

## 13. Other Species / Model Organisms

### Mouse Model (primary animal evidence)
**Cerebrum-specific Kat8 conditional knockout mice** (Emx1-Cre driven, complete loss-of-function in cerebral tissue) were generated and characterized in the founding study:
- **Phenotype:** Early lethality before weaning (by ~3 weeks); "flat-head" phenotype from skull flattening; severe cerebral hypoplasia (neocortex + hippocampus), reduced brain weight from birth.
- **Developmental timeline:** Defects traceable to E12.5 (loss of H4K16ac) through E16.5 (progressive hypoplasia); altered cortical lamination by E13.5.
- **Cellular phenotype:** Depleted SOX2+ neural stem/progenitor cells, premature neurogenesis (excess Tuj1+ neurons), reduced proliferation (BrdU+/Ki-67+), massive apoptosis (TUNEL+/cleaved caspase-3+), and complete failure of neurosphere formation in vitro.
- **Fidelity:** This is a complete-null model (not the patient's partial-loss-of-function missense alleles), so it recapitulates the qualitative developmental mechanism (H4K16ac loss → NSPC failure → cerebral hypoplasia) but represents a more severe phenotype (perinatal lethality) than the human disease, which is compatible with survival to adulthood. This fidelity gap (complete knockout vs. partial-function missense variants) is a notable human-model consideration for future curation (HUMAN_MODEL_MISMATCH pattern).

### Drosophila
KAT8 is the direct ortholog of Drosophila MOF, the catalytic subunit of the *Drosophila* male-specific lethal (MSL) core complex that mediates dosage compensation on the male X chromosome via H4K16 acetylation — establishing deep evolutionary conservation of the H4K16ac-writing function, though this Drosophila biology (dosage compensation) is not itself a disease model.

### Zebrafish
No zebrafish KAT8 loss-of-function neurodevelopmental model was identified in the literature searched.

### Cell-based/in vitro models
Patient-variant-expressing HEK293/cell-line systems (FLAG-tagged KAT8 constructs co-expressed with HA-tagged MSL proteins) were used for biochemical acetyltransferase activity and complex-assembly assays; primary mouse embryonic neurosphere cultures were used to model NSPC self-renewal defects.

### Natural Disease in Other Species
No naturally occurring veterinary/companion-animal KAT8-related disease has been reported (OMIA has no listing found in this search); this is an engineered/experimental mouse model only, not a spontaneous natural-disease model.

---

## Summary Table of Suggested Ontology Bindings for KB Curation

| Concept | Suggested term |
|---|---|
| Disease | MONDO:0033547 |
| Gene | hgnc:17933 (KAT8) |
| Key phenotypes | HP:0001263 (Global developmental delay), HP:0001249 (Intellectual disability), HP:0001250 (Seizure), HP:0000750 (Delayed speech and language development), HP:0002119 (Ventriculomegaly), HP:0002079 (Thin corpus callosum), HP:0002185 (Neuronal heterotopia), HP:0000729 (Autistic behavior) |
| Cardiac phenotypes | HP:0001629 (ASD), HP:0001629 (VSD — verify specific term), HP:0001643 (PDA) |
| Biological processes | GO:0043984 (histone H4-K16 acetylation), GO:0043974 (histone H4-K5 acetylation), GO:0022008 (neurogenesis) |
| Cell types | Neural stem/progenitor cell (CL) |
| Anatomy | UBERON:0000956 (cerebral cortex), UBERON:0002421 (hippocampal formation) |
| Treatment | NCIT:C15986 (Pharmacotherapy) + therapeutic_agent valproic acid |

---

## Sources

- [Entry - #618974 - LI-GHORBANI-WEISZ-HUBSHMAN SYNDROME; LIGOWS - OMIM](https://omim.org/entry/618974)
- [Clinical Synopsis - #618974 - OMIM](https://omim.org/clinicalSynopsis/618974)
- [Entry - *609912 - LYSINE ACETYLTRANSFERASE 8; KAT8 - OMIM](https://omim.org/entry/609912)
- [Li-Ghorbani-Weisz-Hubshman syndrome (Concept Id: C5436525) - MedGen - NCBI](https://www.ncbi.nlm.nih.gov/medgen/1763263)
- [Li-Ghorbani-Weisz-Hubshman syndrome | Monarch Initiative (MONDO:0033547)](https://monarchinitiative.org/MONDO:0033547)
- [Li-Ghorbani-Weisz-Hubshman Syndrome - MalaCards](https://www.malacards.org/card/li_ghorbani_weisz_hubshman_syndrome)
- [KAT8 | Li-Ghorbani-Weisz-Hubshman syndrome | GenCC](https://search.thegencc.org/submissions/GENCC_000101-HGNC_17933-OMIM_618974-HP_0000006-GENCC_100003)
- [Li, Ghorbani, Weisz-Hubshman et al., "Lysine acetyltransferase 8 is involved in cerebral development and syndromic intellectual disability," J Clin Invest 2020;130(3):1431-1445, PMID:31794431 - PMC7269600](https://pmc.ncbi.nlm.nih.gov/articles/PMC7269600/)
- [NM_032188.3(KAT8):c.269A>G (p.Tyr90Cys) AND LIGOWS - ClinVar RCV001253776](https://www.ncbi.nlm.nih.gov/clinvar/RCV001253776/)
- [NM_032188.3(KAT8):c.523A>G (p.Lys175Glu) AND LIGOWS - ClinVar RCV001253778](https://www.ncbi.nlm.nih.gov/clinvar/RCV001253778/)
- [KAT8 gene - GeneCards](https://www.genecards.org/card/KAT8)
- [Complex-dependent histone acetyltransferase activity of KAT8 determines its role in transcription and cellular homeostasis - Molecular Cell 2021](https://www.cell.com/molecular-cell/fulltext/S1097-2765(21)00098-8)
- [The non-specific lethal (NSL) complex at the crossroads of transcriptional control and cellular homeostasis - PMC6607013](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6607013/)
- [Li-Ghorbani-Weisz-Hubshman Syndrome (LIGOWS) - RDDC](https://rddc.tsinghua-gd.org/disease/LGH020)
- [Li-Ghorbani-Weisz-Hubshman syndrome profile page - Open Targets Platform](https://platform.opentargets.org/disease/MONDO_0033547)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.