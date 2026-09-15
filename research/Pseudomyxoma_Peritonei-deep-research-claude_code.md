---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-26T16:14:55.173135'
end_time: '2026-08-26T16:19:53.115038'
duration_seconds: 297.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pseudomyxoma Peritonei
  mondo_id: ''
  category: Neoplastic
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
  num_turns: 29
  total_cost_usd: 1.6264682000000001
  session_id: 00937d02-a143-56ac-a731-3747f9ee4c64
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 37
reference_validation:
  total_references: 32
  verified: 31
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.031
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:12218214
  relevance_assessed: 31
  on_topic: 19
  unresolved_references:
  - DOI:10.3390/biomedicines11072049](https://doi.org/10.3390/biomedicines11072049
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pseudomyxoma Peritonei
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Pseudomyxoma Peritonei** covering all of the
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

I'll research Pseudomyxoma Peritonei comprehensively, starting by loading the search/fetch tools.

I now have sufficient material to compile the comprehensive report.

# Pseudomyxoma Peritonei: Comprehensive Research Report

## 1. Disease Information

**Overview.** Pseudomyxoma peritonei (PMP) is a rare, clinically distinctive syndrome of progressive intraperitoneal mucin accumulation ("jelly belly") caused, in the overwhelming majority of cases, by a mucinous neoplasm that perforates the appendix and seeds mucin-producing epithelial cells across the peritoneal surfaces. It is best conceptualized not as a single histologic entity but as a *clinical syndrome* with a spectrum of underlying pathology ranging from acellular mucin to low-grade and high-grade mucinous carcinoma peritonei. The 2019 PSOGI review frames it as "a clinical entity characterised by the presence of mucinous ascites, omental cake, peritoneal implants and possibly ovarian involvement" ([Pathophysiology and classification of pseudomyxoma peritonei, PMC6386305](https://pmc.ncbi.nlm.nih.gov/articles/PMC6386305/)).

**Key identifiers:**
- **Orphanet:** ORPHA:26790 ([Orphanet](https://www.orpha.net/en/disease/detail/26790); [OLS](https://www.ebi.ac.uk/ols4/ontologies/ordo/terms?iri=http://www.orpha.net/ORDO/Orphanet_26790))
- **MONDO:** MONDO:0017048
- **ICD-10-CM:** C78.6 (Secondary malignant neoplasm of retroperitoneum and peritoneum — used when coding the peritoneal spread; some coders use the appendiceal primary code) ([icd10data.com](https://www.icd10data.com/ICD10CM/Codes/C00-D49/C76-C80/C78-/C78.6))
- **ICD-9-CM:** 197.6
- **ICD-O morphology code:** 8480 (mucinous adenocarcinoma)
- **GARD/NORD** entry (NIH rare disease portal): [GARD 7488](https://rarediseases.info.nih.gov/diseases/7488/pseudomyxoma-peritonei); [NORD](https://rarediseases.org/rare-diseases/pseudomyxoma-peritonei/)
- **OMIM:** No dedicated OMIM phenotype MIM number exists — PMP is treated as a sporadic neoplastic syndrome rather than a classic Mendelian phenotype, consistent with its overwhelmingly somatic mutational origin.

**Synonyms/alternative names:** "jelly belly"; disseminated peritoneal adenomucinosis (DPAM, when low-grade); peritoneal mucinous carcinomatosis (PMCA, when high-grade); mucinous carcinoma peritonei; PMP syndrome.

**Data derivation:** The evidence base is drawn almost entirely from aggregated disease-level resources — retrospective single- and multi-institutional surgical cohorts (typically from specialist national referral centers, since PMP is centralized to a handful of high-volume units), pooled national/regional epidemiologic registries (e.g., a nationwide Chinese urban cohort), and increasingly targeted/whole-exome sequencing panels across pooled tumor collections — rather than individual EHR-level data, reflecting the rarity and referral-center concentration of the disease.

---

## 2. Etiology

**Primary causal mechanism.** PMP is, in essence, a *mechanistic* rather than classically genetic or infectious disease: an epithelial neoplasm — almost always a low-grade appendiceal mucinous neoplasm (LAMN), less commonly a high-grade appendiceal mucinous adenocarcinoma — obstructs and distends the appendiceal lumen, perforates the appendiceal wall, and disseminates mucin-secreting epithelial cells onto peritoneal surfaces. A population-based study found the primary site identifiable in 68% of cases, dominated by the appendix in 82% of those ([Smeenk et al., PMID: 17524597](https://pubmed.ncbi.nlm.nih.gov/17524597/)). Non-appendiceal primaries (ovary, urachus, colon, pancreas, gallbladder) are rare and the historical belief that ovarian mucinous tumors were a common primary source has been revised — most "ovarian" PMP is now understood to be secondary/metastatic from an appendiceal primary via immunohistochemical concordance (MUC2, CK20, CDX2 positivity favoring appendiceal origin over CK7-positive primary ovarian mucinous tumors).

**Genetic causal factors (somatic driver mutations):**
- **KRAS** — mutated in 58–100% of sequenced cases depending on cohort and methodology, predominantly at codon 12 ([Pathophysiology review, PMC6386305](https://pmc.ncbi.nlm.nih.gov/articles/PMC6386305/); [High prevalence of KRAS/GNAS mutations, PMID: 41868810](https://pubmed.ncbi.nlm.nih.gov/41868810/))
- **GNAS** — activating mutations (predominantly R201H/R201C) reported in 12–100% of cases depending on grade and cohort, thought to drive the mucin-hypersecretory phenotype via cAMP signaling ([Nummela et al. molecular profiles study, PMC5123786](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5123786/))
- **TP53** — more prevalent in high-grade disease (17–31% vs. 4–7% in low-grade, p=0.012–0.005), associated with female sex and worse survival
- **SMAD4, PIK3CA, BRAF, APC, ERBB4, BAP1, TGFBR2, ATM, FAT4** — minority alterations (1–10% each), with BRAF V600E enriched specifically in high-grade signet-ring-cell disease
- A 223-case targeted sequencing study found GNAS and KRAS mutated in **42% each**, with strong co-occurrence (adjusted p=2.72×10⁻²¹, odds ratio 22.3), and that mutation in either gene predicted worse survival (combined HR 1.87, p=0.004) ([Targeted Genetic Sequencing of 223 Cases, PMID: 39435876 / PMC11494485](https://pmc.ncbi.nlm.nih.gov/articles/PMC11494485/))
- This genetic profile is notably distinct from colorectal adenocarcinoma: PMP shows markedly higher KRAS/GNAS rates but lower TP53/PI3K-AKT pathway involvement.

**Risk factors.** No established environmental, occupational, dietary, infectious, or lifestyle risk factors have been identified for PMP itself. NORD explicitly states "there are no genetic, familial, or environmental factors known to cause this disorder" beyond the mechanical event of LAMN perforation ([NORD](https://rarediseases.org/rare-diseases/pseudomyxoma-peritonei/)). This distinguishes PMP sharply from peritoneal mesothelioma (which shares a similar clinical/radiologic appearance but has well-established asbestos/smoking risk associations) — a distinction that matters diagnostically since the two can be difficult to distinguish radiologically and pathologically. The dominant "risk factor" is simply the presence of a perforated (or perforation-prone) LAMN — perforation status is the single strongest determinant of progression to PMP.

**Protective factors.** None specifically established; early diagnosis and resection of an appendiceal mucinous neoplasm before perforation is the only known "protective" intervention, effectively preventing PMP rather than modifying an established risk.

**Familial/hereditary clustering.** True hereditary PMP is exceptionally rare, with only a handful of reported kindreds:
- A father-daughter pair with appendiceal mucinous tumors and PMP underwent germline whole-exome sequencing; 15 novel shared variants across 15 genes were identified, including a nonsense mutation in **REEP5**, correlated against regions of tumor loss of heterozygosity ([Germline WES family study, PMC7195761](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195761/))
- A separate first-degree relative pair shared germline **RAD51C** and **FH** variants alongside somatic KRAS/GNAS/TSC1 mutations ([King et al., Clinical Case Reports](https://onlinelibrary.wiley.com/doi/full/10.1002/ccr3.3338))
- Only two prior familial kindreds have otherwise been documented in the literature (monozygotic twin brothers; a brother-sister pair), underscoring that these findings are exploratory leads, not established Mendelian etiology.

**Gene-environment interactions.** None described in the literature; the mechanistic pathway is essentially cell-autonomous (somatic driver mutation → epithelial proliferation/mucin hypersecretion → mechanical perforation → peritoneal seeding) with no identified environmental modifier.

---

## 3. Phenotypes

PMP phenotypes are predominantly mass-effect/obstructive and laboratory (tumor marker) findings rather than classic syndromic HPO-style malformations, consistent with its acquired/neoplastic nature.

**Symptoms and clinical signs** (suggested HP terms in parentheses):
- **Progressive abdominal distension/"jelly belly"** — the classic presenting sign, from mucinous ascites (HP:0003270 Abdominal distention)
- **Abdominal pain/discomfort** (HP:0002027 Abdominal pain)
- **Bloating, early satiety, loss of appetite** (HP:0004396 Abdominal bloating; HP:0004395 Decreased appetite)
- **New-onset or worsening inguinal hernia** in men, from raised intra-abdominal pressure (HP:0000023 Inguinal hernia)
- **Palpable ovarian/pelvic mass** in women — historically misattributed to primary ovarian neoplasm (HP:0100615 Ovarian neoplasm)
- **Bowel obstruction** in advanced disease (HP:0025144 Bowel obstruction)
- **Dyspnea/shortness of breath** from diaphragmatic compression by ascites (HP:0002094 Dyspnea)
- **Weight loss, constipation, urinary symptoms** — less common
- **Incidental discovery** at appendectomy or unrelated abdominal surgery/imaging — a substantial minority present asymptomatically

**Characteristics:**
- **Onset:** Adult-onset; commonly diagnosed in the 5th–6th decade, though the underlying LAMN may be indolent for years before perforation/diagnosis
- **Progression:** Classically slow/indolent, especially in low-grade (DPAM) disease, which can smolder over years; high-grade disease progresses more rapidly
- **Course:** Often initially asymptomatic or mimicking irritable bowel syndrome, then progressive distension, then mechanical bowel/organ compromise if untreated — "tumors provoke fibrosis of surrounding tissues and impede digestion and organ function... ultimately destroy function of colon, small intestine, stomach, or other intra-abdominal organs" if untreated
- **Frequency:** Population estimates suggest 68% have an identifiable primary (82% appendiceal); ovarian involvement is common in women due to secondary seeding rather than primary origin

**Laboratory abnormalities (biomarkers):**
- **Elevated CEA** — in ~75% of patients preoperatively
- **Elevated CA19-9** — in ~58%
- **Elevated CA-125** — commonly elevated, historically contributing to misdiagnosis as ovarian cancer
- Elevated tumor markers correlate with higher Peritoneal Cancer Index (PCI), higher risk of incomplete cytoreduction, longer hospital stay, and worse prognosis ([Prognostic Value of CEA, CA19-9, CA125, CA724, CA242, PMID: 34733775](https://pubmed.ncbi.nlm.nih.gov/34733775/))

**Quality of life impact:** Progressive abdominal distension, early satiety, and mechanical compression significantly impair daily functioning; disease recurrence after surgery and the morbidity of CRS-HIPEC itself (a major, high-morbidity operation) both substantially affect QOL, though structured EQ-5D/SF-36 PMP-specific QOL data are sparse in the literature relative to more common cancers.

---

## 4. Genetic/Molecular Information

**Causal/driver genes** (see Etiology for frequencies): **KRAS** (HGNC:6407), **GNAS** (HGNC:4392), **TP53** (HGNC:11998), **SMAD4** (HGNC:6770), **PIK3CA** (HGNC:8975), **BRAF** (HGNC:1097), **APC** (HGNC:583), **ERBB4** (HGNC:3432), **BAP1** (HGNC:950), **TGFBR2** (HGNC:11772).

**Variant classification/type:**
- **KRAS:** Missense hotspot mutations, predominantly codon 12 (G12D most common — reported at 63% of KRAS-mutant preclinical models; also G12V, G12C, A146, G13C) — activating, gain-of-function
- **GNAS:** Missense hotspot mutations at codon 201 (R201H ~86%, R201C ~14% in one preclinical series) — activating (constitutive Gsα/cAMP signaling), gain-of-function
- **BRAF:** V600E — enriched in high-grade signet-ring-cell tumors, activating
- **TP53:** Predominantly loss-of-function/dominant-negative missense and truncating variants, more common in high-grade disease

**Somatic vs. germline:** The overwhelming majority of PMP-driving mutations are **somatic**. Germline predisposition variants have only been reported in isolated familial case reports (REEP5, RAD51C, FH — see Etiology) and are not established as recurrent causal loci.

**Population allele frequency databases:** Not directly applicable, since these are somatic cancer driver mutations rather than population polymorphisms; standard population databases (gnomAD, 1000 Genomes) are not the relevant reference for KRAS/GNAS hotspot variants in this context (COSMIC is more relevant for somatic frequency).

**Functional consequences:**
- KRAS mutation → constitutive RAS/MAPK pathway activation; in PMP specifically, KRAS has been proposed to induce **GM-CSF** expression contributing to the immunosuppressive tumor microenvironment
- GNAS mutation → constitutive Gsα activation → elevated cAMP → enhanced **A2AR (adenosine A2A receptor) signaling** and mucin hypersecretion — a mechanism distinct from and potentially synergistic with KRAS-driven effects ([A2AR Expression and Immunosuppressive Environment in PMP, doi:10.3390/biomedicines11072049](https://doi.org/10.3390/biomedicines11072049))
- The GNAS-KRAS co-mutation signature is a defining molecular feature that distinguishes PMP from colorectal adenocarcinoma, where GNAS mutations are rare

**Molecular subtype correlation:** Molecular profiling shows GNAS mutation rates as high as 63–100% in low-grade disease with "no marked difference" reported between grades in some series, while TP53 is clearly grade-associated (enriched in high-grade). KRAS mutation status, unlike in colorectal cancer, does **not** predict survival independently in most series, though the newer 223-case cohort found both KRAS (HR 1.72) and GNAS (HR 1.48) individually prognostic for worse survival, with combined mutation carrying the highest hazard (HR 1.87) ([PMC11494485](https://pmc.ncbi.nlm.nih.gov/articles/PMC11494485/)).

**Epigenetic information:** Limited direct PMP-specific epigenetic data exist; hypoxia-driven transcriptional regulation of mucin genes (see Mechanism section) represents the best-characterized regulatory layer, mediated through **HIF-1α** binding to the MUC2 promoter rather than classical DNA methylation/histone studies.

**Chromosomal abnormalities:** Not a defining feature; PMP is not classically associated with recurrent aneuploidy, translocations, or copy-number syndromes in the way many solid tumors are — the driver landscape is dominated by point mutations (KRAS/GNAS) rather than structural variation.

---

## 5. Environmental Information

As noted above, no established environmental toxin, occupational exposure, radiation, dietary, or lifestyle factor has been linked to PMP causation. No infectious agent has been implicated. This is a notable negative finding worth stating explicitly for KB purposes: **PMP has no known ECTO-bindable exposure etiology** — its causal chain begins with somatic mutation and mechanical perforation, not exogenous exposure.

---

## 6. Mechanism / Pathophysiology

**Causal chain (initiating trigger → clinical manifestation):**

1. **Initiating event:** Somatic KRAS and/or GNAS activating mutation arises in appendiceal mucosal epithelium (molecular scale)
2. **Neoplastic transformation:** Low-grade appendiceal mucinous neoplasm (LAMN) forms — villiform/undulating/flat low-grade mucinous epithelium with a "pushing" (non-destructive) growth pattern, distending the appendiceal lumen with accumulated mucin (cellular/tissue scale)
3. **Mechanical failure:** Progressive luminal distension causes appendiceal wall thinning and **perforation** (tissue scale) — perforation status is the single most important determinant of subsequent peritoneal dissemination
4. **Peritoneal seeding:** Mucin-secreting epithelial cells and acellular mucin extravasate into the peritoneal cavity
5. **Redistribution phenomenon** (Sugarbaker, 1994, PMID: 8129480): tumor cells and mucin follow peritoneal fluid circulation dynamics — driven by gravity, the clockwise flow imposed by GI peristalsis, and diaphragmatic/omental fluid reabsorption suction — to accumulate preferentially at fixed anatomic "collection points": the greater omentum ("omental cake"), right hemidiaphragm, Morrison's pouch, and recto-vesical/pelvic pouch (pouch of Douglas), while relatively sparing the peristaltically active small bowel surface ([PMC6386305](https://pmc.ncbi.nlm.nih.gov/articles/PMC6386305/); [Sugarbaker 1994, PMC1243111](https://pmc.ncbi.nlm.nih.gov/articles/PMC1243111/))
6. **Mucin hypersecretion:** GNAS mutation-driven Gsα/cAMP signaling upregulates gel-forming mucin production (organism/tissue scale)
7. **Hypoxic amplification loop:** As mucin accumulates and tumor nodules enlarge, intratumoral **hypoxia develops**, and hypoxia-inducible factor **HIF-1α** binds directly to the **MUC2** promoter, further upregulating MUC2 transcription/secretion — a self-amplifying mucin-production loop implicated as a druggable node ("Targeting hypoxia-mediated mucin 2 production as a therapeutic strategy," PMID: 26589109)
8. **Mechanical/compressive end-organ damage:** Progressive mucin/tumor accumulation causes fibrosis, adhesions, and compression of abdominal viscera, ultimately impairing bowel, stomach, and other organ function if untreated — the proximate cause of morbidity/mortality
9. **Immunosuppressive microenvironment:** CD163+ M2-polarized tumor-associated macrophages (TAMs) are found in 67% of PMP cases (in the microenvironment) and 27% (within tumor cells); in the hypoxic milieu, M2 TAMs promote angiogenesis and exert immunosuppression via PD-L1 expression and Treg recruitment, contributing to disease persistence despite host immune surveillance ("Progress on immuno-microenvironment... in PMP," PMC11271218)

**Molecular pathways involved:** RAS/MAPK (KRAS), Gsα/cAMP/PKA and downstream A2AR adenosine signaling (GNAS), HIF-1α hypoxia response pathway, TGF-β/SMAD4 (minority of cases), PI3K-AKT (minority).

**Mucin biology:** **MUC2** (gel-forming, intestinal-type secreted mucin) is the dominant molecular marker of PMP and is overexpressed relative to MUC5AC in appendiceal-origin tumors (contrasting with ovarian mucinous tumors, which show a different mucin expression pattern) — MUC2 is described as "a molecular marker for pseudomyxoma peritonei" (PMID: 12218214). MUC5AC and MUC5B are also detected biochemically in patient mucus. CK20, CDX2, and CK7 immunohistochemical staining patterns further support appendiceal (vs. ovarian) origin assignment.

**Cell types involved:** Mucinous (goblet-cell-like) neoplastic epithelial cells of appendiceal origin (candidate CL term: CL:0000160 goblet cell / intestinal epithelial lineage); CD163+ M2 macrophages (CL:0000891 or CL:0000235 macrophage subtype); regulatory T cells (Tregs, CL:0000815) recruited into the immunosuppressive microenvironment.

**Biological processes (candidate GO terms):** mucus secretion (GO:0070254), response to hypoxia (GO:0001666), positive regulation of Ras protein signal transduction, adenylate cyclase-activating GPCR signaling (via GNAS/Gsα), cellular response to hypoxia mediated by HIF-1 transcription factor.

**Advanced molecular profiling:** Whole-exome sequencing has been used to characterize both somatic mutation/LOH landscapes and rare germline variants (see above). Targeted next-generation sequencing panels are used clinically to prognosticate and to identify actionable targets (droplet digital PCR successfully validated druggable mutations in 83% of tumor samples even from low-cellularity intra-abdominal mucin biopsies) ([Precision Oncology in PMP, PMC11393541](https://pmc.ncbi.nlm.nih.gov/articles/PMC11393541/)). Patient-derived organoid (PDO) and patient-derived xenograft (PDX) models have enabled genomic characterization revealing KRAS and BRAF as druggable targets.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary organ:** Appendix (vermiform appendix) — site of the originating neoplasm in ~82% of cases with an identifiable primary
- **Secondary/disseminated involvement:** Peritoneum (parietal and visceral), greater omentum, ovaries (secondary seeding, not primary origin in most cases), diaphragmatic surfaces, liver capsule/subcapsular surface (with characteristic "scalloping" from mucin compression rather than true parenchymal invasion), spleen capsule, small and large bowel serosal surfaces (compressed/scalloped rather than typically invaded, per the redistribution phenomenon sparing peristaltically active surfaces)
- **Body system:** Primarily gastrointestinal/peritoneal; secondarily reproductive (ovary) and, via mass effect, respiratory (diaphragmatic compression → dyspnea) and urinary (compression symptoms)

**Tissue/cell level:**
- Peritoneal mesothelial surface and subperitoneal connective tissue (site of mucin deposition and fibrotic reaction)
- Mucinous epithelial cell strips/glands floating within extracellular mucin pools (the defining histologic picture)
- Omental adipose/connective tissue, remodeled into the characteristic "omental cake"

**Subcellular level:** Not a classically subcellular-organelle disease; relevant compartments include the secretory pathway (ER/Golgi) of mucin-producing goblet-like cells and the nuclear compartment for GNAS/KRAS/TP53 signaling effects.

**Localization/UBERON candidates:** UBERON:0004063 (appendix), UBERON:0002358 (peritoneum), UBERON:0002101 (omentum), UBERON:0000992 (ovary), UBERON:0002107 (liver — capsule), UBERON:0002106 (spleen — capsule).

**Lateralization:** Not applicable in the classic sense; disease distribution is dictated by peritoneal fluid dynamics (redistribution phenomenon) rather than left/right asymmetry, though there is a described right-hemidiaphragm predilection over the left, attributed to differential fluid reabsorption dynamics.

---

## 8. Temporal Development

**Onset:** Adult-onset, most commonly diagnosed in the 5th–6th decade of life; the underlying LAMN may be present and slowly enlarging for years to a decade or more prior to perforation and clinical presentation. Onset pattern is typically **insidious**, with a substantial fraction discovered incidentally at unrelated surgery or imaging.

**Progression/staging:**
- **AJCC 9th edition staging** for appendiceal adenocarcinoma/PMP now formally distinguishes:
  - **M1a** — intraperitoneal acellular mucin only, no identifiable tumor cells in disseminated mucinous deposits
  - **M1b** — intraperitoneal metastasis with tumor cells present in peritoneal mucinous deposits
  - **M1c** — extraperitoneal metastasis
  - **T4** — tumor (including acellular mucin) involving the serosal (visceral peritoneal) surface or directly invading adjacent organs
  - Stage grouping: M1a disease (regardless of grade) is Stage IVA; M1b disease is staged IVA (Grade 1) or IVB (Grade 2/3/X) depending on histologic grade
- **Histopathologic grading** (the dominant prognostic staging framework in practice) — see Section 10/Diagnostics
- **Progression rate:** Highly variable by grade — low-grade (DPAM) disease can be indolent over years to decades; high-grade (PMCA), and especially high-grade with signet-ring cells (PMCA-S), progresses more rapidly and carries substantially worse prognosis
- **Disease course pattern:** Generally progressive if untreated, though the indolent low-grade form can appear relatively "stable" over long intervals; recurrence after CRS-HIPEC affects roughly one-quarter to nearly half of treated patients

**Remission patterns:** Primarily treatment-induced (via complete cytoreductive surgery ± HIPEC); spontaneous remission is not described. Long-term survivors after complete cytoreduction can achieve what is sometimes termed "clinical cure," though recurrence surveillance is typically lifelong given the biology of residual microscopic disease.

**Critical periods/intervention windows:** The window before appendiceal perforation (i.e., diagnosis and resection of an intact LAMN) represents the key preventive opportunity; once peritoneal dissemination has occurred, the critical determinant of outcome becomes achieving **complete cytoreduction** (CC-0/CC-1) at the time of definitive surgery — later-stage disease with higher PCI is progressively less amenable to complete resection.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Incidence:** Classically cited at 1–2 cases per million per year; a more recent statistical estimate calculated an incidence of **3.2 per million per year**, with an estimated prevalence around **22 per million** ([Estimating the Prevalence of PMP in Europe, PMC7752784](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7752784/))
- **China nationwide data:** Urban Chinese cohort study found crude PMP prevalence of **2.47 per million person-years** in 2016, with higher prevalence in females than males ([PMID: 35764460](https://pubmed.ncbi.nlm.nih.gov/35764460/))
- **Orphanet prevalence class:** Consistent with "1-9 per 1,000,000" (ultra-rare) band
- **Appendiceal mucinous neoplasm base rate:** A mucinous epithelial neoplasm is identified in ~0.3% of all appendiceal specimens, and ~20% of these patients go on to develop PMP

**Inheritance pattern:** PMP is overwhelmingly **sporadic**, driven by somatic (not germline) mutation. No established Mendelian inheritance pattern exists. The rare familial clusters reported (father-daughter; first-degree relative pairs; twin brothers; a sibling pair) suggest an as-yet-uncharacterized predisposition in isolated kindreds, but no confirmed inheritance mode (AD/AR/X-linked) has been established — these remain case-report-level observations rather than a validated genetic syndrome.

**Penetrance/expressivity/anticipation/mosaicism/founder effects/consanguinity/carrier frequency:** Not applicable/not established, given the sporadic somatic-driver nature of the disease and the rarity of any hereditary predisposition signal.

**Population demographics:**
- **Sex ratio:** Notable female predominance is repeatedly reported (partly an artifact of secondary ovarian involvement drawing gynecologic-oncology attention, but a true excess in some population cohorts as well, e.g., the Chinese nationwide cohort)
- **Age distribution:** Peak diagnosis in the 50s; can occur across a wide adult age range
- **Geographic distribution:** No striking endemic geographic clustering has been described; incidence estimates have been generated primarily from European and Chinese cohorts, likely reflecting availability of centralized referral/registry data from specialist CRS-HIPEC centers rather than a true geographic risk gradient
- **Ethnic/racial predisposition:** No specific ethnic predisposition established in the literature reviewed

---

## 10. Diagnostics

**Laboratory tests/biomarkers:**
- **CEA, CA19-9, CA-125** — the three standard serum tumor markers monitored; elevated preoperatively in 75%, 58%, and a majority of patients respectively; used for diagnosis, disease-burden estimation, treatment response monitoring, and prognosis ([PMID: 34733775](https://pubmed.ncbi.nlm.nih.gov/34733775/); [PMID: 27038681](https://pubmed.ncbi.nlm.nih.gov/27038681/))
- **CA72-4, CA242** — additional markers studied in serum and ascites for prognostic stratification
- Number of elevated markers correlates with PCI and resectability

**Imaging:**
- **Contrast-enhanced CT of chest/abdomen/pelvis** is the imaging modality of choice; characteristic finding is **"scalloping"** of the liver/spleen surface from loculated mucin deposits, plus omental caking and ascites with a gelatinous (rather than simple fluid) density
- **MRI** — superior soft-tissue contrast; CT alone consistently *underestimates* peritoneal spread; combined CT+MRI improves preoperative PCI estimation accuracy compared to CT alone
- **Peritoneal Cancer Index (PCI)** (Sugarbaker scoring system, 0–39) is the standard quantitative surgical/radiologic staging tool for disease extent; **PCI ≥20 is generally considered a marker of unresectability**
- Diagnostic laparoscopy is sometimes used when CT findings are equivocal

**Histopathology (definitive diagnosis) — PSOGI 2016 consensus classification** (Peritoneal Surface Oncology Group International modified Delphi process, PMID: 26492181):
1. **Acellular mucin (AC)** — mucin without identifiable neoplastic epithelium
2. **Low-grade mucinous carcinoma peritonei (LG-MCP)** = synonym DPAM (disseminated peritoneal adenomucinosis) — abundant extracellular mucin, scant epithelial strips/small islands, minimal cytologic atypia, maintained cell polarity, low mitotic activity
3. **High-grade mucinous carcinoma peritonei (HG-MCP)** = synonym PMCA (peritoneal mucinous carcinomatosis) — enlarged vesicular nuclei, full-thickness stratification, loss of polarity, prominent nucleoli, cribriform/micropapillary architecture, increased mitoses
4. **High-grade mucinous carcinoma peritonei with signet ring cells (HG-MCP-S)** = PMCA-S — >50% signet-ring morphology; worst prognosis of the four tiers

This PSOGI system superseded the original Ronnett et al. 1995 three-tier system (DPAM / PMCA / intermediate PMCA-I/D, PMID: 7503361) and subsequent iterations (Bradley 2006 two-tier; Shetty 2013 three-tier PMP1-3), consolidating terminology while retaining DPAM/PMCA as accepted synonyms.

**Immunohistochemistry:** MUC2 (positive marker), CK20, CDX2 (support appendiceal/intestinal origin) vs. CK7 (favors non-appendiceal/ovarian primary); EpCAM also studied.

**Genetic/molecular testing:** Targeted NGS panels (KRAS, GNAS, TP53, SMAD4, BRAF, PIK3CA) increasingly used for prognostication and precision-therapy matching; droplet digital PCR (ddPCR) has been validated as feasible even on low-cellularity intra-abdominal mucin biopsies (83% mutation detection rate), addressing the classic challenge of low tumor cellularity in PMP specimens for standard sequencing.

**Differential diagnosis:** Peritoneal mesothelioma (can closely mimic PMP radiologically and clinically — asbestos/smoking-associated, unlike PMP), primary ovarian mucinous carcinoma, peritoneal carcinomatosis from other GI/pancreatic primaries, simple/loculated ascites.

**Staging:** AJCC 9th edition TNM system for appendiceal neoplasms (T4/M1a/M1b/M1c as above) plus the surgical/pathologic PCI and completeness-of-cytoreduction (CC) score are the operative staging tools that drive management decisions.

**Screening:** No population screening program exists given the extreme rarity of PMP; incidental appendiceal mucinous neoplasms are occasionally detected on imaging/colonoscopy performed for unrelated indications, and prompt resection before perforation is the closest analog to secondary prevention.

---

## 11. Outcome/Prognosis

**Survival by histologic grade** (the dominant prognostic determinant):
- Ronnett et al. (1995) original series: 5-year survival **84% for DPAM vs. 6.7% for PMCA** (PMID: 7503361)
- Contemporary CRS-HIPEC-treated series: 5-year OS approximately **81% (DPAM) / 78% (hybrid) / 59% (PMCA)** in one series, and **93% (acellular mucin) / 69.8% (DPAM) / 55% (PMCA)** in another
- Single-surgeon uniformly treated cohort: 5-year survival **75% (DPAM), 50% (PMCA-I/D), 14% (PMCA)**
- PMCA-S (signet-ring) subtype consistently shows the **worst prognosis** of the four PSOGI tiers
- With modern CRS-HIPEC, large series report OS up to 196 months, with **5- and 10-year survival rates reaching 74% and 63%**, and some large series report median survival of 16.3 years and 86% 5-year OS in favorable subsets

**Prognostic factors (independent predictors of survival):**
- **Completeness of cytoreduction (CC-0/CC-1 vs. CC-2/CC-3)** — consistently the single strongest prognostic factor across studies, generally outweighing even histologic grade or mutation status
- **Histologic grade/PSOGI subtype** — independent predictor
- **Molecular status** — GNAS and/or KRAS mutation independently associated with worse survival in the 223-case cohort (combined HR 1.87, p=0.004); TP53 mutation associated with worse survival and higher grade
- **PCI at presentation** — higher PCI associated with lower rates of achievable complete cytoreduction and worse outcomes
- **Elevated tumor markers (CEA, CA19-9, CA-125)** — associated with higher disease burden and worse prognosis
- **Postoperative anemia within 24h** — recently reported as an independent prognostic factor in one series

**Morbidity/complications:** Bowel obstruction, malnutrition, adhesion-related complications, and the substantial perioperative morbidity of CRS-HIPEC itself (a long, complex operation) are the principal sources of disease- and treatment-related morbidity. Recurrence occurs in roughly one-quarter to nearly half of CRS-HIPEC-treated patients.

**Quality of life/functional outcomes:** Limited PMP-specific structured QOL data; the disease and its treatment both carry significant impact on daily functioning, though many long-term survivors after complete cytoreduction report favorable long-term function relative to the pre-treatment natural history of progressive obstruction.

---

## 12. Treatment

**Standard of care — Cytoreductive Surgery + Hyperthermic Intraperitoneal Chemotherapy (CRS-HIPEC):**
- CRS involves radical peritonectomy and multivisceral resection to remove all visible tumor and mucin, followed by intraoperative HIPEC to treat microscopic residual disease
- This is now the internationally accepted standard treatment, significantly prolonging survival and, in a subset, achieving durable long-term survival/clinical cure
- **Completeness of cytoreduction (CC score)** is the key modifiable surgical determinant of outcome (NCIT candidate: NCIT:C15329 Surgical Procedure; more specifically a cytoreductive/peritonectomy procedure)
- **HIPEC agents:** Mitomycin C (traditional standard) and oxaliplatin are the most-studied intraperitoneal agents; a 10-year outcome analysis of a randomized trial compared mitomycin C vs. oxaliplatin HIPEC for appendiceal neoplasms with peritoneal dissemination. A newer retrospective propensity-matched study found **cisplatin + docetaxel HIPEC superior to cisplatin + mitomycin C** for PMP survival, suggesting a role for personalized HIPEC regimen selection
- NCIT candidate terms: NCIT:C15632 (Chemotherapy); therapeutic_agent CHEBI terms for mitomycin C, oxaliplatin, cisplatin, docetaxel, fluorouracil

**Systemic chemotherapy** (for unresectable/recurrent disease):
- **FOLFOX (oxaliplatin/5-FU/leucovorin)** used as first-line systemic therapy for unresectable mucinous appendiceal adenocarcinoma with PMP, with promising results in several series
- **Mitomycin C + capecitabine** — Phase II study showed clinical benefit in 38% of 39 assessable patients; 2 patients converted from unresectable to resectable
- **NCT01946854** — randomized crossover trial of systemic chemotherapy for metastatic well-differentiated mucinous appendiceal adenocarcinoma with PMP (MD Anderson)
- **NCT00352755** — Phase II peritonectomy + intraperitoneal 5-FU + systemic oxaliplatin/5-FU/leucovorin (terminated)

**Targeted/precision therapy (emerging):**
- **BRAF V600E-mutant, high-grade PMP:** Encorafenib (BRAF inhibitor) showed significant monotherapy efficacy in BRAF V600E patient-derived organoid/xenograft models
- **KRAS G12D:** The KRAS G12D-selective inhibitor MRTX1133 showed dose-dependent efficacy in preclinical PMP models
- Standard chemotherapy (mitomycin C, oxaliplatin) showed only minimal effect in these same preclinical models, reinforcing rationale for a precision-oncology approach guided by ddPCR/NGS mutation profiling ([Precision Oncology in PMP, PMC11393541](https://pmc.ncbi.nlm.nih.gov/articles/PMC11393541/))
- Anti-EGFR agents (cetuximab) have shown only limited benefit despite high KRAS mutation prevalence
- Immune checkpoint blockade (anti-PD-1/PD-L1) is of theoretical interest given the CD163+ M2-macrophage/PD-L1-rich immunosuppressive microenvironment, but clinical data specific to PMP remain preliminary

**Palliative/emerging local therapy:**
- **PIPAC (Pressurized IntraPeritoneal Aerosol Chemotherapy)** — minimally invasive, low-dose aerosolized intraperitoneal chemotherapy (typically cisplatin 7.5 mg/m² + doxorubicin 1.5 mg/m²) for unresectable/recurrent disease; a case report documented clinical and histological remission in a PMP patient (PMID: 26076000); overall PIPAC across peritoneal malignancies carries a severe complication rate of ~6.2%, with improved survival in patients receiving multiple sessions or bidirectional (systemic + intraperitoneal) treatment

**Supportive care:** Nutritional support, management of bowel obstruction, and symptom-directed palliation (ascites/mucin drainage) for advanced/recurrent disease not amenable to further cytoreduction.

**Treatment algorithm:** Complete surgical cytoreduction (CC-0/CC-1) + HIPEC is preferred whenever feasible based on PCI/resectability assessment; unresectable disease is managed with systemic chemotherapy ± PIPAC, with molecular profiling increasingly used to select targeted agents (BRAF/KRAS inhibitors) in appropriate mutation-positive patients.

---

## 13. Prevention

**Primary prevention:** No general population-level primary prevention exists given the sporadic, non-environmentally-triggered etiology. The only actionable primary-prevention-adjacent measure is timely diagnosis and resection of an appendiceal mucinous neoplasm (LAMN) **before** perforation occurs, since perforation is the proximate mechanical trigger for peritoneal dissemination.

**Secondary prevention:** No population screening program exists (extreme rarity precludes cost-effective screening). Incidental detection of appendiceal mucinous lesions on imaging or at appendectomy for unrelated indications, followed by prompt appropriate surgical management, functions as de facto secondary prevention.

**Tertiary prevention:** Complete cytoreductive surgery with HIPEC is itself the principal tertiary-prevention strategy — preventing progression/recurrence in patients who already have established peritoneal disease. Surveillance imaging and tumor marker monitoring after CRS-HIPEC are used to detect recurrence early, when repeat cytoreduction may still be feasible.

**Genetic counseling:** Not routinely indicated given the sporadic somatic nature of disease; counseling could be considered on a case-by-case, research basis for the rare identified familial kindreds, but no validated predictive genetic test or established hereditary syndrome exists to counsel around.

**Public health/environmental interventions:** Not applicable — no known modifiable environmental risk factor.

---

## 14. Other Species / Natural Disease

**Naturally occurring veterinary disease:** PMP-like syndromes have been documented in **dogs** as a rare complication of caecal/appendiceal (cecal, since dogs lack a true vermiform appendix analog but a functionally similar cecal apex process is described) mucocele/mucinous neoplasm perforation. Malignant mucocele cases in dogs show neoplastic cells penetrating the wall and seeding the peritoneum with adhesive, semi-solid mucin containing neoplastic cells — mirroring the human mechanism closely (McKenna et al., caecal mucocele in a dog, [JSAP](https://onlinelibrary.wiley.com/doi/10.1111/jsap.13175)).

**Canine myxoid mesothelioma** has also been reported with a clinical presentation resembling pseudomyxoma peritonei (gelatinous, translucent peritoneal material), though this represents a mesothelial rather than epithelial-mucinous-neoplasm mechanism and should be distinguished from true PMP.

**Taxonomy:** No formal OMIA entry specific to canine PMP was identified; these remain individual case reports rather than a curated naturally-occurring-disease model in veterinary genetics databases.

**Comparative biology:** The core redistribution-phenomenon mechanism (fluid-dynamics-driven mucin/tumor cell distribution to fixed anatomic collection points) is conserved enough between human and canine disease that the veterinary cases are cited in the human clinical literature as supportive natural-history evidence, though systematic comparative pathology/genomic characterization (KRAS/GNAS mutation status in canine cases) has not been reported in the sources reviewed.

**Zoonotic potential:** None — not a transmissible disease in either species.

---

## 15. Model Organisms

**Patient-derived xenograft (PDX) models:**
- PDX models generated by serial engraftment of patient PMP tumors into immunocompromised mice have been established and reported in both mice and rats
- Notably, **high-grade PMP tumors have been successfully xenografted, but low-grade tumors have not** — a significant modeling limitation given that most clinically relevant PMP is low-grade
- Kuracha et al. (2016) demonstrated that PDX models of PMP **recapitulate the human inflammatory tumor microenvironment** (PMID: 26833741; PMC4831290), supporting their use for microenvironment-directed drug studies
- Orthotopic mouse models specifically reproducing the **PMCA-I (intermediate) histopathologic subtype** have also been described (*American Journal of Pathology*, "Orthotopic Animal Model of Pseudomyxoma Peritonei")
- Genomic characterization of PDX/organoid collections revealed KRAS and BRAF as druggable targets, with BRAF^V600E^ models responding to targeted therapy in vivo (encorafenib) — direct translational validation from model to precision therapy hypothesis

**Patient-derived organoid (PDO) models:**
- A 2024 "combinatorial culture strategy" was developed specifically to overcome the low tumor cellularity/high mucin content that has historically made PMP difficult to culture as organoids (Varinelli et al., *Journal of Surgical Oncology* 2024; PMC11826015)
- PDO models are positioned as a platform for multilevel preclinical drug testing, biomarker discovery, and identification of novel therapeutic targets
- Combined PDO/PDX collections have enabled the KRAS-G12D-inhibitor (MRTX1133) and BRAF-inhibitor (encorafenib) preclinical efficacy studies cited above

**Model limitations:** The inability to reliably xenograft **low-grade** disease (the more common and more indolent clinical phenotype) is the single most significant acknowledged gap in current PMP modeling — most existing PDX/PDO data are biased toward the more aggressive high-grade biology, limiting translational inference for the majority of low-grade PMP patients. No genetically engineered (germline knock-in/knockout) mouse model specifically recapitulating spontaneous appendiceal-origin PMP was identified in the sources reviewed; existing models are xenograft/organoid-based rather than genetically engineered.

**Research applications:** These models have been used to (1) confirm the human inflammatory/immunosuppressive tumor microenvironment is recapitulated in vivo, (2) validate KRAS/GNAS/BRAF as druggable molecular targets, (3) test BRAF and KRAS-G12D inhibitors with in vivo efficacy readouts, and (4) demonstrate that standard cytotoxic chemotherapy (mitomycin C, oxaliplatin) has limited direct antitumor effect in these models — supporting the rationale that HIPEC's clinical benefit may derive substantially from mechanical/cytoreductive and locoregional pharmacokinetic effects rather than purely from cytotoxic potency against the tumor cell population itself.

---

## Summary of Key Ontology Term Suggestions

| Category | Suggested terms |
|---|---|
| Disease | MONDO:0017048; ORPHA:26790 |
| Genes | hgnc:6407 (KRAS), hgnc:4392 (GNAS), hgnc:11998 (TP53), hgnc:6770 (SMAD4), hgnc:1097 (BRAF), hgnc:8975 (PIK3CA) |
| Phenotypes (HP) | HP:0003270 (Abdominal distention), HP:0002027 (Abdominal pain), HP:0025144 (Bowel obstruction), HP:0000023 (Inguinal hernia), HP:0100615 (Ovarian neoplasm), HP:0002094 (Dyspnea) |
| Anatomy (UBERON) | UBERON:0004063 (appendix), UBERON:0002358 (peritoneum), UBERON:0002101 (omentum), UBERON:0000992 (ovary) |
| Biological process (GO) | GO:0070254 (mucus secretion), GO:0001666 (response to hypoxia) |
| Cell types (CL) | goblet/mucinous epithelial cell; CD163+ M2 macrophage; regulatory T cell (CL:0000815) |
| Chemicals (CHEBI) | mitomycin C, oxaliplatin, cisplatin, docetaxel, fluorouracil |
| Treatment (NCIT) | NCIT:C15329 (Surgical Procedure — cytoreductive surgery), NCIT:C15632 (Chemotherapy — HIPEC) |

---

## Sources

- [Pathophysiology and classification of pseudomyxoma peritonei — PMC6386305](https://pmc.ncbi.nlm.nih.gov/articles/PMC6386305/)
- [High prevalence of KRAS and GNAS mutations in pseudomyxoma peritonei — PubMed 41868810](https://pubmed.ncbi.nlm.nih.gov/41868810/)
- [Targeted Genetic Sequencing Analysis of 223 Cases of PMP — PMC11494485 / PubMed 39435876](https://pmc.ncbi.nlm.nih.gov/articles/PMC11494485/)
- [A2AR Expression and Immunosuppressive Environment in PMP — Biomedicines 2023](https://doi.org/10.3390/biomedicines11072049)
- [Orphanet: Pseudomyxoma peritonei (ORPHA:26790)](https://www.orpha.net/en/disease/detail/26790)
- [GARD: Pseudomyxoma peritonei](https://rarediseases.info.nih.gov/diseases/7488/pseudomyxoma-peritonei)
- [NORD: Pseudomyxoma Peritonei](https://rarediseases.org/rare-diseases/pseudomyxoma-peritonei/)
- [ICD-10-CM C78.6](https://www.icd10data.com/ICD10CM/Codes/C00-D49/C76-C80/C78-/C78.6)
- [Appendiceal neoplasms and pseudomyxoma peritonei: a population based study — PubMed 17524597](https://pubmed.ncbi.nlm.nih.gov/17524597/)
- [Prevalence and incidence of PMP in urban China — PubMed 35764460](https://pubmed.ncbi.nlm.nih.gov/35764460/)
- [Estimating the Prevalence of PMP in Europe — PMC7752784](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7752784/)
- [A Consensus for Classification and Pathologic Reporting of PMP (PSOGI) — PubMed 26492181](https://pubmed.ncbi.nlm.nih.gov/26492181/)
- [Ronnett et al. 1995 DPAM/PMCA — PubMed 7503361](https://pubmed.ncbi.nlm.nih.gov/7503361/) (via [Johns Hopkins](https://pure.johnshopkins.edu/en/publications/disseminated-peritoneal-adenomucinosis-and-peritoneal-mucinous-ca-4/))
- [Sugarbaker 1994 redistribution phenomenon — PMC1243111](https://pmc.ncbi.nlm.nih.gov/articles/PMC1243111/)
- [Molecular profiles of high-grade and low-grade PMP — PMC5123786](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5123786/)
- [MUC2 Is a Molecular Marker for PMP — PubMed 12218214](https://pubmed.ncbi.nlm.nih.gov/12218214/)
- [Targeting hypoxia-mediated MUC2 production — PubMed 26589109](https://pubmed.ncbi.nlm.nih.gov/26589109/)
- [Prognostic Value of CEA, CA19-9, CA125, CA724, CA242 — PubMed 34733775](https://pubmed.ncbi.nlm.nih.gov/34733775/)
- [Expression of CEA, CA19-9, CA125, EpCAM in PMP — PubMed 27038681](https://pubmed.ncbi.nlm.nih.gov/27038681/)
- [Precision Oncology and Systemic Targeted Therapy in PMP — PMC11393541 (Clin Cancer Res 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11393541/)
- [Progress on immuno-microenvironment and immune-related therapies in PMP — PMC11271218](https://pmc.ncbi.nlm.nih.gov/articles/PMC11271218/)
- [Germline whole exome sequencing of a family with appendiceal mucinous tumours — PMC7195761](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195761/)
- [Germline and somatic genetic alterations in two first-degree relatives — Wiley](https://onlinelibrary.wiley.com/doi/full/10.1002/ccr3.3338)
- [A combinatorial culture strategy to develop PMP organoid models — PMC11826015](https://pmc.ncbi.nlm.nih.gov/articles/PMC11826015/)
- [Patient-derived xenograft mouse models of PMP recapitulate inflammatory microenvironment — PubMed 26833741 / PMC4831290](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4831290/)
- [Ten-Year Outcome of a Randomized Trial: Mitomycin C vs Oxaliplatin HIPEC](https://link.springer.com/article/10.1245/s10434-024-16441-z)
- [Cisplatin + docetaxel vs cisplatin + mitomycin C HIPEC for PMP](https://www.tandfonline.com/doi/full/10.1080/02656736.2025.2467296)
- [PIPAC with cisplatin and doxorubicin in PMP — PubMed 26076000](https://pubmed.ncbi.nlm.nih.gov/26076000/)
- [The emergence of PIPAC as a palliative treatment option — PMC8100694](https://pmc.ncbi.nlm.nih.gov/articles/PMC8100694/)
- [AJCC Cancer Staging System Version 9: Appendiceal Adenocarcinoma](https://link.springer.com/article/10.1245/s10434-024-14892-y)
- [Diagnosis and treatment of a caecal mucocoele in a dog — JSAP](https://onlinelibrary.wiley.com/doi/10.1111/jsap.13175)
- [Canine myxoid mesothelioma with clinical presentation of Pseudomixoma peritonei](https://bjvp.org.br/bjvp/article/download/532/501)
- [Orthotopic Animal Model of Pseudomyxoma Peritonei — American Journal of Pathology](https://ajp.amjpathol.org/article/S0002-9440(14)00212-0/fulltext)
- [StatPearls: Pseudomyxoma Peritonei — NCBI Bookshelf NBK541116](https://www.ncbi.nlm.nih.gov/books/NBK541116/)
- [Pseudomyxoma peritonei: More Questions Than Answers — J Clin Oncol](https://ascopubs.org/doi/10.1200/JCO.2012.42.3764)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 31 |
| On topic | 19 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.3390/biomedicines11072049](https://doi.org/10.3390/biomedicines11072049` (1 mention) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:12218214` *(abstract only)*: "a molecular marker for pseudomyxoma peritonei"
  - closest text in source: "MUC2 is therefore a reliable molecular marker for pseudomyxoma peritonei."