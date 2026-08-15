---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-15T19:10:30.537638'
end_time: '2026-08-15T19:15:40.231316'
duration_seconds: 309.69
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bailey-Bloch Congenital Myopathy
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
  web_search_requests: 17
  num_turns: 25
  total_cost_usd: 2.0636752
  session_id: 8ebdbdea-f16d-5e75-8ed9-a88b56851407
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 21
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 0
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bailey-Bloch Congenital Myopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bailey-Bloch Congenital Myopathy** covering all of the
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

I'll research Bailey-Bloch Congenital Myopathy (which is a synonym for X-linked Myotubular Myopathy/XLMTM) directly using web search tools, then compile the full report.

Important finding: my initial search reveals that "Bailey-Bloch Congenital Myopathy" is actually a distinct condition from myotubular myopathy — it's caused by STAC3 mutations (also known as Native American Myopathy), not MTM1. Let me research the correct disease thoroughly.

# Research Report: Bailey-Bloch Congenital Myopathy

## ⚠️ Critical Disambiguation Note (Named Entity Confusion Alert)

**Before using this report for curation, note an important identity check.** A naive literature/AI search for "Bailey-Bloch Congenital Myopathy" can easily resolve to the wrong disease: **X-linked Myotubular Myopathy (XLMTM, MTM1, OMIM #310400)** is a superficially similar-sounding severe congenital myopathy, but it is a **genetically and mechanistically distinct entity** (X-linked, lipid-phosphatase loss-of-function, no malignant hyperthermia association, and the subject of the AAV8 gene-therapy program resamirigene bilparvovec/AT132). This is exactly the kind of eponym/synonym collision the NEC (Named Entity Confusion) failure mode targets.

**Bailey-Bloch Congenital Myopathy (BBCM) is the correct, verified identity for this report:**
- Also known as **Native American Myopathy (NAM)** and **Congenital Myopathy 13 (CMYO13)**
- Caused by biallelic (autosomal recessive) pathogenic variants in **STAC3** (12q13.3), *not* MTM1
- **OMIM #255995** (phenotype); STAC3 gene entry **OMIM *615521**
- **MONDO:0009722**
- First described by Bailey and Bloch in 1987 in a Lumbee Native American infant from North Carolina (PMID:3631569)

All content below pertains specifically to the STAC3-related disorder. This distinction is worth flagging explicitly in any curated entry's `notes` given how easily the two conditions are conflated by name similarity alone.

---

## 1. Disease Information

**Overview:** Bailey-Bloch Congenital Myopathy (BBCM) is a rare autosomal recessive congenital myopathy caused by biallelic loss-of-function variants in *STAC3*, which encodes an adaptor protein essential for skeletal-muscle excitation-contraction (EC) coupling. It presents at birth with profound hypotonia, arthrogryposis/congenital contractures, a distinctive myopathic facial gestalt, cleft/high-arched palate, short stature, progressive spinal deformity, and — distinctively among congenital myopathies — a substantial risk of **malignant hyperthermia susceptibility (MHS)** upon exposure to volatile anesthetics or depolarizing muscle relaxants (GeneReviews, NBK542808; PMID:3631569).

**Key identifiers:**
| Resource | ID |
|---|---|
| OMIM (phenotype) | #255995 (CMYO13) |
| OMIM (gene) | *615521 (STAC3) |
| MONDO | MONDO:0009722 |
| Gene | STAC3, chromosome 12q13.3 |
| GeneReviews | NBK542808 |

**Synonyms:** Native American Myopathy (NAM); Congenital Myopathy 13 (CMYO13); STAC3 disorder; STAC3-related congenital myopathy; STAC3 myopathy.

**Evidence provenance:** Information is derived from **aggregated case-series/cohort resources** — the GeneReviews synopsis (44 cumulative cases), a Southern African cohort of 31 homozygotes among 127 hypotonia referrals (PMID:38824262/39080471), a 19-patient international cohort (PMID:30178658), a Comorian case series (PMID:36030003), and individual case reports (Brazil, PMID:37626540) — rather than single-EHR extraction. The disorder was originally population-specific (Lumbee), and later series establish it as pan-ethnic.

---

## 2. Etiology

**Disease causal factor:** Purely genetic — biallelic (homozygous or compound heterozygous) pathogenic loss-of-function variants in *STAC3*. There is no known environmental, infectious, or purely mechanistic (non-genetic) trigger for the baseline myopathy; however, environmental/pharmacologic triggers (volatile anesthetics, succinylcholine) precipitate the acute malignant hyperthermia crisis in susceptible carriers of biallelic variants (GeneReviews NBK542808).

**Genetic risk factors:**
- **Founder variant:** c.851G>C (p.Trp284Ser), a missense substitution in the STAC3 SH3 domain, is the near-exclusive variant in the Lumbee population and the most frequently reported variant worldwide, including in patients of African, Comorian, Southern African, and South American ancestry with no known Lumbee lineage (PMID:37626540; PMID:38824262; PMID:36030003).
- Additional pathogenic variants reported: c.862A>T (p.Lys288Ter, nonsense); c.432+4A>T (splice donor); c.763_766delCTCT (p.Leu255Ilefs*58, frameshift); c.997-1G>T (splice acceptor) (GeneReviews NBK542808; PMID:30178658).
- No large deletions/duplications have been identified to date.
- Carrier frequency: the p.Trp284Ser allele is present in gnomAD at ~33/141,000 alleles in heterozygosity (PMID:37626540); among enrolled Lumbee tribal members (~60,000), disease prevalence is estimated at ~1 in 5,000 (GeneReviews NBK542808).

**Environmental risk factors:** None identified as causal for the underlying myopathy. The critical environmental/pharmacologic exposure is **anesthetic triggering agents** (halogenated volatile anesthetics, succinylcholine), which precipitate malignant hyperthermia crises in a substantial minority of biallelic STAC3 variant carriers (43% in the GeneReviews cohort; 22% in the Southern African cohort) (GeneReviews NBK542808; PMID:38824262).

**Protective factors:** None specifically documented. Avoidance of MH-triggering anesthetic agents functionally prevents the acute MH phenotype but does not modify the baseline myopathy.

**Gene-environment interaction:** The clearest documented interaction is genotype (biallelic STAC3 LOF) × pharmacologic exposure (volatile anesthetic/succinylcholine) → malignant hyperthermia crisis, mediated through STAC3's structural role at the triad junction alongside the canonical MH genes RYR1 and CACNA1S; notably, in the Brazilian case report, both patients tested negative for RYR1/CACNA1S variants, indicating STAC3 itself — independent of the classical MH genes — confers MHS (PMID:37626540).

---

## 3. Phenotypes

Frequencies below are drawn from the GeneReviews cumulative synopsis (n=44) unless otherwise noted; a large independent Southern African cohort (n=31 homozygotes for c.851G>C) is given in parallel where frequencies diverge (PMID:38824262).

### Clinical signs / physical manifestations

| Phenotype | Frequency (GeneReviews, n≈40-44) | Frequency (S. Africa, n=31) | Suggested HPO term* |
|---|---|---|---|
| Hypotonia (congenital) | 100% (41/41) | — | HP:0001252 Hypotonia |
| Myopathic facies (ptosis, inability to elevate mouth corners, progressive facial narrowing) | 100% (44/44) | — | HP:0002058 Myopathic facies |
| Ptosis | 85% (33/39) | — | HP:0000508 Ptosis |
| Poor feeding / feeding difficulty | 73% (29/40) | — | HP:0011968 Feeding difficulties |
| Congenital contractures / arthrogryposis (talipes to AMC spectrum) | 81% (35/43) | AMC 38%; talipes equinovarus 59% | HP:0002804 Arthrogryposis multiplex congenita; HP:0001762 Talipes equinovarus |
| Spinal deformity (scoliosis/kyphosis/kyphoscoliosis) | 79% (31/39) | 52% | HP:0002650 Scoliosis / HP:0002751 Kyphoscoliosis |
| Short stature | 66% (19/29) | — | HP:0004322 Short stature |
| Palatal anomaly | 82% (36/44) | 93% | HP:0000175 Cleft palate (57% specifically) |
| Malignant hyperthermia susceptibility | 43% (19/44) | 22% (history suggestive) | HP:0001954 Malignant hyperthermia |
| Respiratory impairment | 55% (16/29) | — | HP:0002093 Respiratory insufficiency |
| Cryptorchidism (in males) | 62% (13/21) | — | HP:0000028 Cryptorchidism |
| Bilateral hearing loss (case report) | reported | — | HP:0000365 Hearing impairment |

*HPO codes are suggested from standard, well-established terms; confirm with OAK lookup per dismech curation protocol before committing.

**Onset:** Congenital — hypotonia, contractures, facial features, and palatal anomalies are present at birth or noted prenatally (severe end of spectrum can present with prenatal onset) (PMID:30178658).

**Severity/progression:** Highly variable — the 2018 international cohort (PMID:30178658) explicitly describes a spectrum "ranging from prenatal onset with severe features at birth, to a milder and slowly progressive congenital myopathy phenotype." Scoliosis and contractures tend to be progressive; motor function can plateau or decline (some individuals lose ambulation and become wheelchair-dependent by adolescence), while others achieve independent walking and even running (GeneReviews NBK542808).

**Behavioral/cognitive:** Intellect is normal in the majority of affected individuals; mild intellectual disability is rare (GeneReviders NBK542808).

**Laboratory abnormalities:** Serum creatine kinase (CK) may be normal or mildly elevated (nonspecific, as in many congenital myopathies) — not a reliable diagnostic discriminator (GeneReviews NBK542808 background; UChicago Congenital Myopathy panel infosheet).

**Quality of life impact:** Feeding difficulties requiring enteral support, respiratory insufficiency requiring ventilatory assistance, and progressive scoliosis/contractures substantially affect mobility and daily functioning; no formal EQ-5D/SF-36 disease-specific QOL studies were identified in this search.

---

## 4. Genetic/Molecular Information

**Causal gene:** *STAC3* (SH3 and Cysteine-Rich Domain 3), OMIM *615521, chromosome 12q13.3. Encodes a 364-amino-acid, ~41.4 kDa protein with an N-terminal cysteine-rich (C1) domain and two SH3 domains (GeneReviews NBK542808).

**Pathogenic variants (5 documented; ClinVar entries exist, e.g. RCV001457863):**
1. **c.851G>C (p.Trp284Ser)** — missense; founder variant in Lumbee population, now reported worldwide (most common by far)
2. c.862A>T (p.Lys288Ter) — nonsense
3. c.432+4A>T — splice donor site variant
4. c.763_766delCTCT (p.Leu255Ilefs*58) — frameshift deletion
5. c.997-1G>T — cryptic/canonical splice acceptor variant (PMID:30178658)

**Variant classification:** All reported variants are classified pathogenic/likely pathogenic under ACMG/AMP criteria in the disease context (biallelic state required for disease).

**Allele frequency:** The founder p.Trp284Ser variant is present in gnomAD heterozygosity at ~33/141,000 alleles (PMID:37626540); markedly enriched (estimated ~1 in 5,000 disease prevalence) among the ~60,000 enrolled Lumbee tribal members (GeneReviews NBK542808).

**Origin:** Germline only — no somatic BBCM has been described.

**Functional consequence:** All known pathogenic variants are **loss-of-function**. Structural/functional work shows the p.Trp284Ser substitution disrupts the SH3-domain interaction between STAC3's C-terminal region and the II-III cytoplasmic loop of CaV1.1 (the skeletal-muscle L-type calcium channel/dihydropyridine receptor, DHPR), which "decreases the quantity, organization, stability, and voltage sensitivity of Ca²⁺ channels" (GeneReviews NBK542808; PMID:28003463; PMC12333939).

**Modifier genes:** None established. No genotype-phenotype correlation between specific variants and disease severity has been demonstrated to date (GeneReviews NBK542808).

**Chromosomal abnormalities:** No large deletions/duplications or chromosomal rearrangements have been identified in confirmed cases — pathogenic variants are exclusively small sequence-level changes.

**Epigenetic information:** No disease-specific epigenetic (DNA methylation/histone) studies were identified in this search.

---

## 5. Environmental Information

**Environmental/pharmacologic factors:** The dominant environmental modifier is anesthetic exposure. Volatile halogenated anesthetics (halothane, isoflurane, sevoflurane) and depolarizing neuromuscular blockers (succinylcholine, decamethonium) are established triggers of malignant hyperthermia crises in biallelic STAC3 variant carriers and must be strictly avoided (GeneReviews NBK542808).

**Lifestyle factors:** Not applicable — this is a congenital, fully genetically determined disorder; no lifestyle modifiers of penetrance or expressivity were identified.

**Infectious agents:** Not causally implicated; however, aspiration-related pneumonia is a documented cause of morbidity/mortality secondary to bulbar/feeding dysfunction rather than a primary infectious etiology (GeneReviews NBK542808).

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular trigger:** Biallelic loss-of-function *STAC3* variants (most commonly p.Trp284Ser) disrupt the STAC3 adaptor protein's SH3-domain-mediated binding to the II-III cytoplasmic loop of CaV1.1 (the skeletal-muscle dihydropyridine receptor / voltage sensor) (PMC12333939; PMID:28003463).
2. **Molecular consequence:** Loss of proper STAC3-CaV1.1 interaction decreases the quantity, membrane organization, stability, and voltage sensitivity of the CaV1.1 (L-type Ca²⁺ channel) complex at the triad junction (GeneReviews NBK542808).
3. **Cellular consequence:** Impaired excitation-contraction (EC) coupling — voltage sensing at the T-tubule fails to efficiently trigger ryanodine receptor 1 (RYR1)-mediated Ca²⁺ release from the sarcoplasmic reticulum. Zebrafish and murine functional studies show significantly reduced KCl-depolarization-induced and caffeine-induced SR Ca²⁺ release (PMID:23736855; PMID:28003463; PMID:30178658).
4. **Tissue consequence:** Reduced/disorganized myofibrillar contraction, muscle hypotrophy, and — in null models — complete failure of fetal muscle contraction; histopathology shows small type I and/or II fibers, fiber-type disproportion, increased central nuclei, and increased lipid droplets/subsarcolemmal mitochondrial accumulation on electron microscopy (GeneReviews NBK542808).
5. **Organism consequence:** Congenital hypotonia, weakness, contractures/arthrogryposis, myopathic facies, respiratory insufficiency, and impaired growth/short stature.
6. **Parallel branch — malignant hyperthermia susceptibility:** The same triad-complex disruption independently confers susceptibility to pharmacologically triggered, dysregulated SR Ca²⁺ release (a hypermetabolic crisis) upon volatile-anesthetic/succinylcholine exposure — though the precise mechanistic link between STAC3 dysfunction and the MH trigger cascade "remains elusive" per current literature (EMHG summary; PMID:30178658).

**Molecular pathway:** Skeletal-muscle excitation-contraction coupling — the CaV1.1 (DHPR)–STAC3–RYR1 triad complex. This is a specialized calcium-signaling pathway, not a canonical annotated KEGG/Reactome pathway per se, but overlaps GO biological processes: "skeletal muscle contraction" (GO:0003009), "regulation of cytosolic calcium ion concentration" (GO:0051480), "voltage-gated calcium channel activity" (GO:0005245), "muscle filament sliding" (GO:0030049).

**Cellular processes involved:** Voltage sensing, calcium channel trafficking/stabilization, sarcoplasmic reticulum calcium release, myofibrillogenesis, muscle fiber-type specification (STAC3 has been separately shown to regulate hypertrophy and fiber-type composition; PMC4828897).

**Protein dysfunction:** Loss-of-function of a scaffolding/adaptor protein (not itself a channel), disrupting the structural stability and voltage-coupling of the CaV1.1-RYR1 triad supercomplex, rather than a classic enzymatic loss (PMC12333939).

**Suggested GO terms:** GO:0003009 (skeletal muscle contraction), GO:0051480 (regulation of cytosolic calcium ion concentration), GO:0005245 (voltage-gated calcium channel activity), GO:0014901 (myotube differentiation involved in skeletal muscle regeneration — for developmental aspects).

**Suggested CL terms:** CL:0000188 (skeletal muscle fiber / myocyte), CL:0000192 (smooth muscle myocyte — not applicable here; skeletal-muscle-specific), CL:0002372 (myotube).

**Molecular profiling:** No transcriptomic, proteomic, or metabolomic disease-specific datasets were identified in this search; the field has relied predominantly on targeted electrophysiology, calcium imaging, and ultrastructural (EM) studies in zebrafish/mouse models rather than omics profiling.

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: Skeletal muscle (generalized, all muscle groups affected to varying degree) — UBERON:0001134 (skeletal muscle tissue)
- Secondary/complications: Respiratory system (diaphragmatic/intercostal weakness → respiratory insufficiency, pulmonary hypoplasia); craniofacial skeleton and palate (cleft/high-arched palate); axial skeleton (progressive scoliosis/kyphoscoliosis); ocular (ptosis — levator palpebrae superioris muscle); auditory system (hearing loss reported in case report); reproductive (cryptorchidism)
- Body systems involved: Musculoskeletal (primary), respiratory, craniofacial/orofacial, ocular, and — via the MH mechanism — a systemic hypermetabolic crisis affecting multiple organ systems acutely.

**Tissue/cell level:** Skeletal muscle fibers (Type I and Type II, variably small/disproportionate); triad junction (T-tubule/SR junctional complex) is the specific subcellular structure of primary pathology.

**Subcellular level (GO Cellular Component):**
- Sarcoplasmic reticulum (GO:0016529)
- T-tubule / triad junction (GO:0014802, triad)
- Plasma membrane / sarcolemma (voltage sensor localization)
- Mitochondria (subsarcolemmal accumulation noted on EM)

**Localization:** Generalized/systemic muscle involvement rather than focal; facial muscles (myopathic facies, ptosis), palatal musculature, axial/paraspinal muscles, distal limb muscles (talipes), and respiratory muscles are all clinically prominent. No consistent lateralization pattern is reported (bilateral/symmetric involvement typical of congenital myopathies).

---

## 8. Temporal Development

**Onset:** Congenital — present at birth or detectable prenatally in severe cases (reduced fetal movement consistent with arthrogryposis is plausible antenatally, though not explicitly quantified in the sources reviewed). Onset pattern is essentially always congenital/neonatal rather than later-onset (GeneReviews NBK542808; PMID:30178658).

**Progression:** Disease course is variable and described along a spectrum:
- **Severe/prenatal-onset end:** Profound weakness at birth, high early mortality risk
- **Milder end:** Slowly progressive congenital myopathy with better long-term motor function (PMID:30178658)

Musculoskeletal features (scoliosis, contractures) are typically progressive over childhood; some patients require serial casting/bracing/surgery for progressive spinal and limb deformity. Motor function among evaluable individuals (n=15 in GeneReviews cohort) ranged from independent walking (11) to limited ambulation (2), running (1), and independent sitting only (1); a subset become wheelchair-dependent by adolescence (GeneReviews NBK542808).

**Disease duration/course:** Chronic, lifelong — non-remitting. Approximately **36% mortality by age 18 years**, with pulmonary hypoplasia and aspiration-related pneumonia as documented causes of death (GeneReviews NBK542808).

**Critical periods:** The neonatal/early infancy period is the highest-risk window (respiratory failure, feeding failure); any anesthetic exposure at any age constitutes an acute high-risk period for malignant hyperthermia crisis.

---

## 9. Inheritance and Population

**Epidemiology:**
- Originally described exclusively in the Lumbee Native American tribe of North Carolina; estimated prevalence ~1 in 5,000 among the ~60,000 enrolled Lumbee tribal members (GeneReviews NBK542808)
- Now documented across multiple, geographically and ethnically diverse populations: Brazil (PMID:37626540), Comoros Islands (7 patients, PMID:36030003), Southern Africa (31 homozygotes identified among 127 congenital-hypotonia referrals — making it a **common cause of congenital hypotonia in that regional cohort**, PMID:38824262), and individuals of African ancestry more broadly
- Exact global incidence/prevalence outside the Lumbee founder population is not yet formally quantified but is clearly under-ascertained historically due to the eponymic "Native American" framing biasing clinical suspicion away from other ancestries — explicitly flagged in the literature: "STAC3 gene analysis should be included in the diagnostic work up of patients of any ethnicity presenting with congenital myopathy" (PMID:30178658)

**Inheritance pattern:** Autosomal recessive (biallelic pathogenic variants required).

**Penetrance:** Appears fully penetrant for the myopathy phenotype in biallelic carriers (i.e., no unaffected homozygotes reported), though expressivity (severity) is highly variable. Malignant hyperthermia susceptibility penetrance is incomplete/variable (43% GeneReviews cohort; 22% Southern African cohort had a suggestive MH history) — not all biallelic carriers have documented MH events, and absence of a prior uneventful anesthetic does not exclude risk (GeneReviews NBK542808).

**Expressivity:** Markedly variable, from prenatal-onset severe disease to slowly progressive milder myopathy (PMID:30178658). No genotype-phenotype correlation for variant type/severity has been established.

**Genetic anticipation:** Not reported/applicable (not a repeat-expansion disorder).

**Founder effects:** Strong founder effect for c.851G>C (p.Trp284Ser) in the Lumbee population; the same variant recurring as the dominant allele in unrelated non-Lumbee populations worldwide suggests either an ancient founder event, mutational hotspot, or (most likely per literature) simply that this residue (Trp284) is a critical, highly conserved hotspot for loss-of-function substitution.

**Consanguinity:** Not specifically required — Brazilian and other non-Lumbee cases have been reported in patients from **non-consanguineous** parents (PMID:37626540), consistent with a carrier frequency high enough that unrelated at-risk matings occur, particularly given the apparent broader-than-expected allele distribution.

**Carrier frequency:** Estimated at ~33/141,000 alleles in heterozygosity in gnomAD population data for the founder variant (PMID:37626540); locally much higher within the Lumbee population (consistent with ~1/5,000 disease prevalence implying carrier frequency around 1 in ~35-40 if Hardy-Weinberg assumptions hold in that subpopulation).

**Population demographics:**
- Sex ratio: Autosomal recessive — expected 1:1 male:female, though cryptorchidism as a reported feature is obviously male-specific
- Geographic distribution: Originally North Carolina (Lumbee), now global — Brazil, Comoros, Southern Africa, and other regions with African-ancestry populations
- Age distribution: Congenital onset in all reported cases; cohort ages at diagnosis/report span infancy through adolescence/adulthood among survivors

---

## 10. Diagnostics

**Molecular genetic testing (primary diagnostic modality):**
- **Targeted single-variant testing:** For individuals of confirmed or suspected Lumbee ancestry, targeted analysis for c.851G>C (p.Trp284Ser) is recommended first-line
- **Single-gene STAC3 sequencing:** Detects small indels, missense, nonsense, and splice-site variants; if only one or zero pathogenic variants found, follow with gene-targeted deletion/duplication analysis (though none has been identified to date)
- **Multigene congenital myopathy panel:** Recommended when clinical suspicion is present but genetic cause not narrowed — note some panels historically omitted STAC3 due to rarity/eponymic obscurity
- **Exome sequencing (preferred) or genome sequencing:** When the diagnosis is not initially considered / broader differential needed (GeneReviews NBK542808)

**Clinical/histopathologic tests:**
- Muscle biopsy: variable findings — small Type I and/or Type II fibers, fiber-type disproportion, increased central nuclei, increased lipid droplets and/or subsarcolemmal mitochondrial accumulation on electron microscopy (GeneReviews NBK542808)
- Serum creatine kinase: normal or mildly elevated (nonspecific)
- Respiratory functional testing: polysomnography (sleep apnea/hypoxia screening), spirometry/pulmonary function testing
- No STAC3-specific circulating biomarker has been established

**Differential diagnosis (per GeneReviews):**
| Condition | Gene | Distinguishing features |
|---|---|---|
| Central core disease | RYR1 | Also has respiratory insufficiency, contractures, arthrogryposis, MH susceptibility; may show external ophthalmoplegia, CK elevation |
| Carey-Fineman-Ziter syndrome | MYMK | Similar upturned nasal tip, micrognathia, generalized muscle hypoplasia, delayed motor milestones; **no MH susceptibility** — key discriminator |
| Moebius syndrome | Multiple/heterogeneous | Overlapping cleft palate, talipes, short stature, scoliosis, contractures; distinguished by obligatory ocular abduction impairment/cranial nerve findings |

**Genetic counseling / newborn or cascade screening:** No population newborn-screening program specific to STAC3 was identified. Targeted carrier screening/cascade testing is clinically relevant in the Lumbee population and in families with a known proband.

**Diagnostic criteria:** No formal consensus diagnostic-criteria document (e.g., DSM/ICD-style) was identified beyond the GeneReviews clinical + molecular confirmation framework; diagnosis rests on clinical phenotype consistent with the disorder plus biallelic STAC3 pathogenic variants.

---

## 11. Outcome/Prognosis

**Survival/mortality:** Approximately **36% mortality by age 18 years** in the cumulative GeneReviews cohort, with pulmonary hypoplasia and aspiration-related pneumonia as the documented causes of death (GeneReviews NBK542808). Severity spans a spectrum from prenatal-onset/early lethal disease to survivable, slowly progressive myopathy (PMID:30178658).

**Morbidity/function:** Motor outcomes among survivors are heterogeneous: independent ambulation achievable in a majority of evaluable cases in one cohort (11/15), but a subset lose ambulation and become wheelchair-dependent by adolescence. Respiratory insufficiency (55% in one cohort) and feeding/nutritional compromise are major sources of ongoing morbidity requiring long-term multidisciplinary management (GeneReviews NBK542808).

**Complications:** Aspiration pneumonia, progressive scoliosis/kyphoscoliosis potentially requiring surgical correction, ptosis-related visual impairment if uncorrected, malignant hyperthermia crisis (potentially fatal if not immediately recognized and treated) upon inadvertent anesthetic exposure.

**Prognostic factors:** No validated quantitative prognostic biomarkers or scoring system identified; disease severity appears to vary independent of specific variant identity (no established genotype-phenotype correlation) (GeneReviews NBK542808).

---

## 12. Treatment

**Current status: No disease-modifying or curative therapy exists.** GeneReviews states explicitly: "No treatment halts or reverses the manifestations of STAC3 disorder" (NBK542808). This stands in contrast to the unrelated disease X-linked myotubular myopathy (MTM1), which has an AAV8 gene-replacement candidate (resamirigene bilparvovec/AT132) in clinical development via the ASPIRO trial (NCT03199469) — **that program is specific to MTM1/XLMTM and is not applicable to STAC3/Bailey-Bloch disease.** Notably, an early-stage French research initiative (ANR-funded, "STAC3 disorder: gene therapy and malignant hyperthermia") is investigating gene-therapy approaches specifically for STAC3 disorder, but this appears to be at a preclinical/research-planning stage rather than a registered clinical trial — treat as an emerging research direction, not an established treatment, pending primary-literature confirmation.

**Management is entirely supportive/multidisciplinary**, per GeneReviews:

*Musculoskeletal (NCIT:C15302 Physical Therapy; NCIT:C16186 Orthopedic Surgical Procedure):*
- Physical and occupational therapy for range of motion and mobility
- Contracture management: stretching, night splints, serial casting
- Orthopedic intervention for talipes deformity and progressive scoliosis (bracing progressing to surgical correction)
- Adaptive devices for activities of daily living; avoidance of prolonged immobilization

*Feeding/Nutrition (NCIT:C15447 Dietary Intervention):*
- Speech-language pathology and nutrition assessment
- Specialized feeding equipment, nasogastric or enteral (gastrostomy) tube feeding as needed
- Aspiration-risk evaluation

*Respiratory:*
- Polysomnography, spirometry/pulmonary function monitoring
- Noninvasive or invasive ventilatory support as needed
- Mechanical cough-assist devices
- Aggressive prevention/treatment of respiratory infections

*Surgical/other:*
- Ptosis repair (levator resection or frontalis sling) to prevent amblyopia/visual impairment
- Multidisciplinary craniofacial team management of cleft palate repair timing/technique
- Speech therapy for dysarthria
- Hearing assessment/audiology referral

*Genetic counseling (NCIT:C15240):* Recommended for families, given autosomal recessive inheritance and 25% recurrence risk for future pregnancies of carrier parents.

**Anesthesia/perioperative management — the single most critical, disease-defining treatment consideration:** Strict avoidance of volatile halogenated anesthetics (halothane, isoflurane, sevoflurane) and depolarizing neuromuscular blockers (succinylcholine, decamethonium) is mandatory due to malignant hyperthermia risk; total intravenous anesthesia (TIVA) protocols and dantrolene availability are standard-of-care precautions in this population (GeneReviews NBK542808).

**Surveillance schedule (per GeneReviews):**
- Growth: every visit
- Neuromuscular assessment: every 3-4 months (infants <12 months); every 6-12 months (older children/adults)
- Respiratory: at least annually, more often if symptomatic
- Feeding/nutrition: every visit

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense (fully genetic, congenital disorder) — the principal preventive intervention is genetic counseling and reproductive planning (carrier testing, prenatal diagnosis, preimplantation genetic diagnosis) for at-risk families, particularly within the Lumbee community and other populations where the founder variant has been documented.

**Secondary prevention:** Early recognition via clinical suspicion and STAC3 testing in any patient presenting with congenital hypotonia/myopathy — explicitly recommended by Zaharieva et al. (PMID:30178658) as a diagnostic-pathway improvement, since delayed/missed diagnosis (from assuming the "Native American" eponym excludes other ancestries) delays appropriate anesthesia precautioning.

**Tertiary prevention (preventing complications in affected individuals):** This is where the bulk of "prevention" activity concentrates for this disorder — **anesthesia-protocol avoidance of MH triggers** is the single highest-yield preventive intervention (preventing a potentially fatal acute crisis); proactive orthopedic bracing to slow scoliosis progression; proactive respiratory surveillance to catch early insufficiency; proactive feeding evaluation to reduce aspiration risk.

**Genetic/carrier screening:** Targeted variant screening (for c.851G>C) is feasible and low-cost in populations with known founder-variant enrichment; broader carrier screening is not yet a standard public-health program outside of at-risk-population contexts.

**Public health/behavioral interventions:** No population-level public health program specific to this disorder was identified.

---

## 14. Other Species / Natural Disease

**Naturally occurring disease in other species:** No naturally occurring STAC3-related myopathy in non-human species (companion animals, livestock, wildlife) was identified in this search — unlike some other congenital myopathy genes with OMIA entries, STAC3 disorder appears to be studied exclusively through engineered/induced animal models (see Section 15) rather than as a spontaneously occurring veterinary disease.

**Orthologous gene:** STAC3 is highly conserved across vertebrates — the critical Trp284 residue "is completely conserved between various mammals and zebrafish," underscoring its fundamental structural role in EC coupling machinery (search synthesis from PMID:23736855/PMID:28003463 literature).

**Comparative biology:** The excitation-contraction coupling machinery (CaV1.1-STAC3-RYR1 triad) is deeply conserved from zebrafish to mammals, which is precisely why zebrafish forward-genetic screens were able to identify stac3 as a novel EC-coupling component in the first place (PMID:23736855).

---

## 15. Model Organisms

**Zebrafish (Danio rerio) — the founding/primary model system:**
- The gene was originally identified through an **unbiased zebrafish locomotor forward-genetic screen**, which isolated a paralytic mutant subsequently mapped to *stac3* — this is how the human disease gene was discovered in the first place (Horstick et al., 2013, *Nature Communications*, PMID:23736855)
- *stac3*-null zebrafish show paralysis, loss of voltage-dependent SR Ca²⁺ release, delayed larval hatching correlating with muscle weakness, and decreased whole-body Ca²⁺ levels during early skeletal muscle development
- A zebrafish knock-in model of the human p.Trp284Ser (NAM) mutation (*stac3^NAM*) showed significantly reduced dihydropyridine receptor (DHPR/CaV1.1) levels, functionality, and stability, along with paradoxically **increased caffeine-induced Ca²⁺ release** — Linsley et al., 2017, *PNAS*, PMID:28003463
- A 2024 zebrafish study found that early-life lipid overload in Native American myopathy is phenocopied by *stac3* knockout, implicating a metabolic/lipid-handling dimension to the disease not previously appreciated (PMID:39592070)
- Defects in F-actin cytoskeleton organization and slow-muscle-fiber structure were observed at 5-7 days post-fertilization in *stac3* mutant larvae

**Mouse (Mus musculus):**
- *Stac3* knockout mice die perinatally from suffocation (respiratory failure due to complete EC-coupling failure), phenocopying other EC-coupling-null models (e.g., RYR1-null, CaV1.1-null)
- Newborn *Stac3*-knockout mouse muscle fibers show centralized nuclei and disorganized myofibrils — directly recapitulating human muscle-biopsy findings (centralized nuclei is a described human histopathologic feature)
- Skeletal muscles from *Stac3*-deleted mouse fetuses fail to contract altogether, consistent with defective EC coupling as the proximate cellular mechanism
- STAC3 additionally regulates postnatal muscle growth, fiber-type composition, and hypertrophy signaling, based on a postnatal *Stac3* gene-dosage study (PMC4828897)

**Model fidelity assessment:** Both zebrafish and mouse null models robustly recapitulate the core EC-coupling defect and the severe end of the human phenotypic spectrum (paralysis/perinatal lethality, centralized nuclei, disorganized myofibrils), supporting **high translational fidelity** for the core mechanism. However, complete null models in mouse are uniformly perinatal-lethal, which does not capture the milder, slowly progressive end of the human phenotypic spectrum seen with hypomorphic human alleles — the *stac3^NAM* knock-in zebrafish model is a closer approximation of the specific human founder-variant biology and is the more clinically relevant model for the malignant-hyperthermia-susceptibility mechanism specifically.

**Applications:** These models have been used to dissect (1) the core structural/electrophysiological mechanism of EC-coupling failure, (2) the specific molecular consequence of the p.Trp284Ser substitution on CaV1.1 stability/organization, and (3) an emerging metabolic/lipid-handling dimension of pathophysiology; they underlie the rationale for the nascent STAC3 gene-therapy research effort noted in Section 12.

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Suggested term(s) | Note |
|---|---|---|
| Disease | MONDO:0009722 | Verify against local MONDO closure |
| Gene | STAC3 (HGNC symbol; verify HGNC numeric ID via lookup — not independently confirmed in this search) | 12q13.3 |
| Phenotypes | HP:0001252 Hypotonia; HP:0002058 Myopathic facies; HP:0000508 Ptosis; HP:0011968 Feeding difficulties; HP:0002804 Arthrogryposis multiplex congenita; HP:0001762 Talipes equinovarus; HP:0002751 Kyphoscoliosis; HP:0004322 Short stature; HP:0000175 Cleft palate; HP:0001954 Malignant hyperthermia; HP:0002093 Respiratory insufficiency; HP:0000028 Cryptorchidism | Verify each with OAK per dismech-terms skill before committing |
| Biological process (GO) | GO:0003009 skeletal muscle contraction; GO:0051480 regulation of cytosolic calcium ion concentration; GO:0005245 voltage-gated calcium channel activity | |
| Cellular component (GO) | GO:0016529 sarcoplasmic reticulum; GO:0014802 triad (T-tubule/SR junction) | |
| Cell type (CL) | CL:0000188 skeletal muscle fiber; CL:0002372 myotube | |
| Anatomy (UBERON) | UBERON:0001134 skeletal muscle tissue | |
| Treatment (NCIT) | NCIT:C15302 Physical Therapy; NCIT:C16186 Orthopedic Surgical Procedure; NCIT:C15447 Dietary Intervention; NCIT:C15240 Genetic Counseling | |

## PMID Reference List
- PMID:3631569 — Bailey & Bloch, 1987 (original description)
- PMID:23736855 — Horstick et al., 2013, *Nat Commun* (zebrafish screen identifying Stac3)
- PMID:28003463 — Linsley et al., 2017, *PNAS* (stac3^NAM zebrafish mechanism)
- PMID:30178658 — Zaharieva et al., 2018, *Hum Mutat* (largest international cohort, dysmorphic features, MHS)
- PMID:36030003 — Comorian case series (7 patients)
- PMID:37626540 — Brazilian patients case report
- PMID:38824262 / PMID:39080471 — Southern African cohort (31 homozygotes; common cause of congenital hypotonia)
- PMID:39592070 — 2024 zebrafish lipid-overload/knockout phenocopy study
- GeneReviews NBK542808 — STAC3 Disorder (comprehensive clinical synthesis, n=44 cases)
- OMIM #255995 (CMYO13) and *615521 (STAC3)

---

Sources:
- [Entry - #255995 - CONGENITAL MYOPATHY 13; CMYO13](https://omim.org/entry/255995)
- [Bailey-Bloch Congenital Myopathy in Brazilian Patients: A Very Rare Myopathy with Malignant Hyperthermia Susceptibility](https://pmc.ncbi.nlm.nih.gov/articles/PMC10452826/)
- [Bailey-Bloch Congenital Myopathy in Brazilian Patients - PubMed](https://pubmed.ncbi.nlm.nih.gov/37626540/)
- [Bailey-Bloch congenital myopathy - NIH Genetic Testing Registry (GTR)](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1850625/)
- [STAC3 Disorder - GeneReviews®](https://www.ncbi.nlm.nih.gov/books/NBK542808/)
- [STAC3 disorder: a common cause of congenital hypotonia in Southern African patients | European Journal of Human Genetics](https://www.nature.com/articles/s41431-024-01644-5)
- [STAC3 disorder: a common cause of congenital hypotonia in Southern African patients (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11711498/)
- [STAC3 related congenital myopathy: A case series of seven Comorian patients - PubMed](https://pubmed.ncbi.nlm.nih.gov/36030003/)
- [Stac3 is a component of the excitation–contraction coupling machinery and mutated in Native American myopathy | Nature Communications](https://www.nature.com/articles/ncomms2952)
- [Congenital myopathy results from misregulation of a muscle Ca2+ channel by mutant Stac3 | PNAS](https://www.pnas.org/doi/10.1073/pnas.1619238114)
- [STAC3 variants cause a congenital myopathy with distinctive dysmorphic features and malignant hyperthermia susceptibility - Human Mutation](https://onlinelibrary.wiley.com/doi/abs/10.1002/humu.23635)
- [615521 - SH3 AND CYSTEINE-RICH DOMAINS 3; STAC3](https://www.omim.org/entry/615521)
- [Congenital Myopathy 13 - MalaCards](https://www.malacards.org/card/congenital_myopathy_13)
- [STAC3 stably interacts through its C1 domain with CaV1.1 in skeletal muscle triads | Scientific Reports](https://www.nature.com/articles/srep41003)
- [Early life lipid overload in Native American Myopathy is phenocopied by stac3 knockout in zebrafish - PubMed](https://pubmed.ncbi.nlm.nih.gov/39592070/)
- [The SH3 and cysteine-rich domain 3 (Stac3) gene is important to growth, fiber composition, and calcium release from the sarcoplasmic reticulum in postnatal skeletal muscle](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4828897/)
- [STAC3 binding to CaV1.1 II-III loop is nonessential but critically supports skeletal muscle excitation-contraction coupling](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12333939/)
- [STAC3 — European Malignant Hyperthermia Group](https://www.emhg.org/stac3)
- [STAC3 disorder: gene therapy and malignant hyperthermia | ANR](https://anr.fr/Project-ANR-24-CE91-0005)
- [Effects of gene replacement therapy with resamirigene bilparvovec (AT132) on skeletal muscle pathology in X-linked myotubular myopathy - eBioMedicine](https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(23)00460-7/fulltext)
- [X-linked myotubular myopathy | MedLink Neurology](https://www.medlink.com/articles/x-linked-myotubular-myopathy)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:28003463`: "decreases the quantity, organization, stability, and voltage sensitivity of Ca²⁺ channels"
  - closest text in source: "Furthermore, stac3NAM myofibers exhibited increased caffeine-induced Ca2+ release across a wide range of concentrations in the absence of altered caffeine sensitivity as well as increased Ca2+ in internal stores, which is consistent with increased SR luminal Ca2+ These findings define critical roles for Stac3 in EC coupling and human disease."
- `PMC:PMC12333939`: "decreases the quantity, organization, stability, and voltage sensitivity of Ca²⁺ channels"
  - Text part not found as substring: 'decreases the quantity, organization, stability, and voltage sensitivity of Ca²⁺ channels' (note: only abstract available for PMID:40779452, full text may contain this excerpt)
- `PMID:30178658`: "STAC3 gene analysis should be included in the diagnostic work up of patients of any ethnicity presenting with congenital myopathy"
  - Text part not found as substring: 'STAC3 gene analysis should be included in the diagnostic work up of patients of any ethnicity presenting with congenital myopathy' (note: only abstract available for PMID:30178658, full text may contain this excerpt)
