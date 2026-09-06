---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-19T08:42:59.473431'
end_time: '2026-08-19T08:47:13.784387'
duration_seconds: 254.31
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Intellectual Developmental Disorder, X-Linked, Syndromic 37
  mondo_id: ''
  category: Genetic
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
  web_search_requests: 13
  num_turns: 20
  total_cost_usd: 1.9032706999999998
  session_id: f3f55950-48a9-5033-a85c-1dcc22637229
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 10
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 4
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Developmental Disorder, X-Linked, Syndromic 37
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Intellectual Developmental Disorder, X-Linked, Syndromic 37** covering all of the
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

# Research Report: Intellectual Developmental Disorder, X-Linked, Syndromic 37 (MRXS37)

## 1. Disease Information

**Overview.** X-linked syndromic intellectual developmental disorder-37 (MRXS37) is a recently delineated (2024) neurodevelopmental disorder caused by heterozygous (in females) or hemizygous (in males) pathogenic variants in **ZFX** (zinc finger protein, X-linked), located at Xp22.11. It is characterized by global developmental delay, intellectual disability of variable severity, behavioral abnormalities (autism spectrum disorder, sleep disturbance), a recurrent facial gestalt, and a broad range of variably penetrant congenital anomalies including sensorineural hearing loss, congenital heart defects, genitourinary defects, musculoskeletal anomalies, and endocrine dysfunction (notably hyperparathyroidism/hypogonadism) (OMIM #301118).

**Key identifiers:**
- **OMIM:** #301118 (MRXS37); gene locus *314980 (ZFX)
- **MedGen:** CUI C5935567 (UID 1854940)
- **Monarch/MONDO:** MONDO:0958322
- **Gene:** ZFX (HGNC:12874), Xp22.11
- **No dedicated Orphanet ORPHA code or GeneReviews chapter was identified as of this search** — reflecting the disorder's very recent characterization (first cohort description: Shepherdson et al., 2024, *AJHG*, PMID:38325380).
- ICD-10/11: no disease-specific code identified; would fall under general X-linked intellectual disability codes (ICD-10 F70–F79 with genetic modifier).

**Synonyms:** MRXS37; ZFX-related neurodevelopmental disorder; ZFX syndrome.

**Data provenance:** The evidence base is derived almost entirely from aggregated multi-family case-series/cohort studies (the founding 2024 AJHG paper: 18 individuals/16 families) supplemented by individual case reports (e.g., a 2025/2026 AJMG-A case report, PMID:41074764) — i.e., **aggregated disease-level cohort data plus incremental single-patient case reports**, not large-scale registry or EHR-derived data, consistent with an ultra-rare, newly described gene-disease relationship.

Sources: [OMIM #301118](https://www.omim.org/entry/301118), [MedGen](https://www.ncbi.nlm.nih.gov/medgen/1854940), [AJHG 2024](https://www.cell.com/ajhg/fulltext/S0002-9297(24)00007-7)

---

## 2. Etiology

**Disease causal factors:** Monogenic, caused by de novo (predominantly) or inherited heterozygous/hemizygous variants in **ZFX**. The founding cohort (PMID:38325380) reported **11 distinct ZFX variants in 18 individuals (14 males, 4 females) from 16 unrelated families**; 10 were de novo, while 8 were inherited from a mildly affected or clinically unaffected mother, demonstrating **variable penetrance and expressivity in female carriers**.

**Genetic risk factors:**
- **Variant type is mechanistically bifurcated:**
  - **Truncating variants** (frameshift, nonsense; 7 of 11 variants) — presumed loss-of-function, distributed across the gene.
  - **Missense variants** — cluster specifically in the **12th and 13th (penultimate and ultimate) C2H2 zinc-finger domains** of the DNA-binding domain (DBD), which are critical for sequence-specific DNA contact. These missense alleles are strongly associated with the **hyperparathyroidism** phenotype (see below), suggesting a distinct genotype-phenotype correlation, possibly reflecting a gain-of-function/dominant-negative transcriptional mechanism rather than simple haploinsufficiency.
- **gnomAD constraint:** ZFX is predicted highly loss-of-function intolerant (pLI = 1.0, gnomAD v4.1.0), consistent with its essential transcription-factor role and supporting pathogenicity of truncating alleles even outside the zinc-finger hotspot.
- **X-linked dosage context:** Unlike most X-linked genes, **human ZFX escapes X-inactivation** (PMID:1970799, PMID:2500252), meaning both X chromosomes express ZFX in females. This is mechanistically important — it may partially explain why heterozygous females can be substantially, even similarly, affected to hemizygous males (unlike typical X-linked NDD genes where skewed XCI protects carrier females), while also creating room for variable expressivity depending on relative dosage/expression balance between the two alleles.

**Environmental/other risk factors:** None identified; this is a purely monogenic disorder with no reported environmental, infectious, or lifestyle contributors.

**Protective factors:** No specific protective genetic or environmental modifiers have been reported. Some heterozygous female carriers are asymptomatic, likely reflecting incomplete penetrance rather than an identified protective mechanism (OMIM #301118).

**Gene-environment interactions:** None described in the literature to date.

Sources: [Shepherdson et al. 2024, AJHG, PMID:38325380](https://www.cell.com/ajhg/fulltext/S0002-9297(24)00007-7), [ZFX escapes XCI, PMID:1970799](https://pubmed.ncbi.nlm.nih.gov/1970799/)

---

## 3. Phenotypes

Phenotype data are drawn from OMIM's clinical synopsis (#301118) aggregating the founding cohort and subsequent case reports. Suggested HPO term bindings are noted in brackets.

**Neurodevelopmental (core, high frequency):**
- Global developmental delay [HP:0001263]
- Delayed walking [HP:0031936] / motor delay
- Speech and language delay [HP:0000750]
- Intellectual disability, borderline to moderate (variable) [HP:0002342 / HP:0001256]
- Hypotonia [HP:0001252]

**Behavioral (frequent):**
- Autism spectrum disorder [HP:0000717]
- Sleep disturbance [HP:0002360]
- ADHD, aggressive behavior, anxiety (reported variably across cases)

**Craniofacial gestalt (recurrent, described as a defining feature — PMID:38325380):**
- Thickened, medially broadened eyebrows [HP:0000574-adjacent / custom]
- Long and/or smooth philtrum [HP:0000343 / HP:0000319]
- External eye abnormalities, epicanthus, blepharophimosis [HP:0000286, HP:0000581]
- Ear abnormalities — low-set, posteriorly rotated, macrotia [HP:0000369, HP:0000368, HP:0000400]
- Frontal bossing, broad forehead, midface retrusion [HP:0002007, HP:0000337, HP:0011800]

**Sensory:**
- Sensorineural hearing loss [HP:0000407] (variable frequency)
- Ocular anomalies (variable)

**Skeletal/musculoskeletal:**
- Scoliosis [HP:0002650], joint hypermobility [HP:0001382], clinodactyly [HP:0030084], pectus deformities [HP:0000768/HP:0000765], osteopenia [HP:0000938]

**Cardiac (variable, ~subset of patients):**
- Congenital heart defects generally [HP:0001627]; patent ductus arteriosus, ASD, VSD, coarctation of aorta, bicuspid aortic valve reported in individual cases

**Genitourinary:**
- Cryptorchidism [HP:0000028], hypospadias [HP:0000047] in males; hydronephrosis, horseshoe kidney

**Gastrointestinal:**
- Feeding difficulties [HP:0011968], poor growth, dysphagia, constipation

**Endocrine (notable genotype-correlated finding):**
- Hypogonadism [HP:0000135]
- **Hyperparathyroidism / parathyroid adenoma [HP:0000843 / HP:0008163]** — reported in 3 of 7 probands with data available who carried missense (zinc-finger DBD) variants (PLOS One 2025, PMID pending; JCEM Case Reports PMID search), representing a striking genotype-phenotype correlation not typically seen in NDD genes.
- Hypercalcemia [HP:0003072]

**Neuroimaging:**
- Cerebral atrophy, hypoplasia of the corpus callosum, delayed myelination, arachnoid/choroid plexus cysts — reported variably; in the 2026 case report, novel findings included **inferior cerebellar vermian hypoplasia**, hypoplastic vertebral artery, and aberrant subclavian artery (PMID:41074764).

**Phenotype characteristics:**
- **Onset:** Congenital/early infancy (motor and speech delay presenting in early childhood in reported cases).
- **Severity/frequency:** Highly variable; "male mutation carriers tend to be more severely affected than female mutation carriers, some of whom may even be asymptomatic" (OMIM #301118).
- **Progression:** Generally a static/stable developmental disorder, though the endocrine complication (hyperparathyroidism, potential parathyroid neoplasia) can develop later and progressively.
- **QoL impact:** Not formally studied with standardized instruments (EQ-5D/SF-36); OMIM notes "many patients are able to attend mainstream schools with assistance and work under supervision," implying a moderate but variable functional impact.

Sources: [OMIM Clinical Synopsis #301118](https://www.omim.org/entry/301118), [AJHG 2024, PMID:38325380](https://www.cell.com/ajhg/fulltext/S0002-9297(24)00007-7), [AJMG-A 2026 case report, PMID:41074764](https://onlinelibrary.wiley.com/doi/10.1002/ajmg.a.64280)

---

## 4. Genetic/Molecular Information

**Causal gene:** ZFX (HGNC:12874; OMIM *314980), Xp22.11.

**Gene product:** A Krüppel-type C2H2 zinc-finger transcription factor with three domains:
1. An N-terminal **acidic transcriptional activation domain (AD)**
2. A **nuclear localization sequence (NLS)**
3. A C-terminal **DNA-binding domain (DBD)** consisting of **13 tandem C2H2-type zinc fingers**

**Pathogenic variant spectrum (PMID:38325380):**
- 11 distinct variants across 18 individuals/16 families
- **Truncating variants (frameshift, nonsense)** — 7 of 11 variants; distributed throughout the coding sequence; presumed haploinsufficiency mechanism, consistent with the gene's extreme LOF intolerance (gnomAD pLI = 1.0)
- **Missense variants** — cluster in **zinc fingers 12 and 13** (the "penultimate and ultimate" fingers of the DBD), altering DNA-contact residues
- **Inheritance of variant:** ~56% de novo (10/18); remainder inherited from a mother with mild or no symptoms — indicating **variable penetrance/expressivity**, notably unusual for an X-linked gene because ZFX escapes X-inactivation
- **Variant classification:** Pathogenic/likely pathogenic per ACMG criteria in the reporting studies; specific ClinVar submissions exist for the reported variants (not individually enumerated here — recommend direct ClinVar query for `ZFX[gene]` for current classifications)

**Case-specific example:** A de novo frameshift variant, **p.(Met666Valfs*2)**, was independently identified in a female patient (PMID:41074764) — the same variant previously reported in an affected male, demonstrating recurrence and supporting causality.

**Allele frequency:** Not reported in gnomAD as a common/polymorphic allele; pathogenic ZFX variants are absent or exceedingly rare in population databases, consistent with de novo occurrence and severe fitness consequence.

**Somatic vs. germline — a distinctive dual mechanism:** ZFX is notable among NDD genes for also functioning as a **somatic proto-oncogene**. Recurrent **somatic** missense mutations at a hotspot involving two adjacent arginine residues (**R786/R787**) in the 13th zinc finger domain are found in **sporadic parathyroid adenomas** (PMID:25594030), independent of the germline NDD variants but located in the same functional domain (ZF12/13). This somatic-germline convergence on the same zinc-finger domain provides strong mechanistic support for the germline missense-hyperparathyroidism genotype-phenotype correlation described above.

**Functional consequence (functional studies, PMID:38325380):**
- **Transcriptional activity assays** (luciferase/reporter-based) in cultured cells showed that **DNA-binding-domain missense variants produce differential/altered transcriptional output** compared to wild-type ZFX, consistent with dysregulated (rather than simply abolished) transcription factor activity for the missense class — distinct from a pure loss-of-function truncating mechanism.
- **Zebrafish loss-of-function model:** *zfx* knockout zebrafish displayed altered behavior on standardized assays: modified novel-tank-assay responses, altered light preference (scototaxis), and enhanced startle responses — supporting a causal, evolutionarily conserved neurobehavioral role for ZFX loss.

**Modifier genes / epigenetics:** None specifically reported for MRXS37.

**Chromosomal abnormalities:** Not a copy-number/structural disorder; caused by point mutations (SNVs/indels) within ZFX. No recurrent microdeletion/microduplication syndrome overlapping ZFX has been described in this context.

**Suggested ontology terms:** Gene — HGNC:12874 (ZFX); GO terms — "DNA-binding transcription factor activity" (GO:0003700), "sequence-specific DNA binding" (GO:0043565), "regulation of transcription by RNA polymerase II" (GO:0006357), "stem cell population maintenance" (GO:0019827).

Sources: [OMIM *314980 ZFX](https://www.omim.org/entry/314980), [AJHG 2024, PMID:38325380](https://www.cell.com/ajhg/fulltext/S0002-9297(24)00007-7), [Recurrent ZFX mutations in parathyroid adenomas, PMID:25594030](https://pubmed.ncbi.nlm.nih.gov/25594030/), [PLOS One 2025, germline ZFX and PHPT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0329388)

---

## 5. Environmental Information

No environmental toxins, occupational exposures, lifestyle factors, or infectious agents have been implicated in MRXS37 — it is a purely monogenic disorder. No gene-environment interaction data exist in the literature reviewed.

---

## 6. Mechanism / Pathophysiology

**Causal chain (proposed, integrating functional and human genetic data):**

1. **Trigger:** De novo or inherited pathogenic ZFX variant (truncating → haploinsufficiency; or missense in ZF12/13 → altered/dysregulated DNA-binding and transcriptional output).
2. **Molecular consequence:** ZFX, an X-inactivation-escaping C2H2 zinc-finger transcription factor, normally acts as a key regulator of **stem cell self-renewal** — directly activating target genes shared between embryonic stem cells (ESCs) and hematopoietic stem cells (HSCs), including ESC-specific self-renewal regulators such as **Tbx3** and **Tcl1** (PMID for Cell 2007 Zfx paper — Harel/Lengner et al.). Loss or dysregulation of ZFX transcriptional activity is predicted to impair progenitor/stem-cell maintenance during neurodevelopment.
3. **Cellular process:** In model systems, Zfx-deficient ESCs and HSCs show **increased apoptosis** and stress-response gene upregulation, with impaired self-renewal but preserved differentiation capacity — pointing to a stem/progenitor cell-maintenance defect rather than a differentiation block as the proximate cellular mechanism.
4. **Tissue/organism-level consequence:** Disrupted neural progenitor maintenance and downstream cortical/craniofacial developmental programs plausibly underlie the global developmental delay, intellectual disability, and characteristic facial gestalt; behavioral phenotypes are corroborated by zebrafish knockout behavioral assays (anxiety-like phenotypes on novel tank/scototaxis tests, enhanced startle).
5. **Divergent missense mechanism (endocrine arm):** In parallel, missense variants specifically disrupting ZF12/13 DNA contact residues appear to confer a distinct, possibly gain-of-function or altered-specificity transcriptional activity that predisposes to parathyroid chief cell proliferation (adenoma) and hyperparathyroidism — mirroring the recurrent somatic R786/787 hotspot mutations found in sporadic parathyroid adenomas. This represents a **two-track genotype-phenotype model**: truncating/LOF variants → classical NDD phenotype via haploinsufficiency; DBD missense variants → NDD **plus** endocrine tumor predisposition via altered transcriptional specificity.

**Molecular pathways:** No canonical signaling pathway (Wnt/MAPK/mTOR/PI3K-AKT) has been directly implicated; the mechanism is that of a **stem-cell transcriptional regulator** acting through direct target gene activation (an ESC/HSC self-renewal transcriptional network), rather than a signal-transduction cascade.

**Cell types involved:** Neural progenitor cells (inferred), embryonic/hematopoietic stem cells (direct evidence from model systems), parathyroid chief cells (for the endocrine/oncogenic arm).

**Suggested GO terms:** "stem cell population maintenance" (GO:0019827), "regulation of stem cell proliferation" (GO:1902850), "positive regulation of transcription by RNA polymerase II" (GO:0045944), "apoptotic process" (GO:0006915).

**Suggested CL terms:** "neural progenitor cell" (CL:0011020), "hematopoietic stem cell" (CL:0000037), "parathyroid chief cell" (CL:0000432).

**Molecular profiling:** No published transcriptomic/proteomic/single-cell datasets specific to MRXS37 patient tissue were identified; functional data derive from reporter assays in cultured cells and zebrafish whole-organism transcript/behavior analysis (PMID:38325380).

Sources: [Zfx controls ESC/HSC self-renewal, Cell 2007](https://www.cell.com/cell/comments/S0092-8674(07)00339-X), [ZFX controls human ESC self-renewal, PMID (PMC3411758)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3411758/), [AJHG 2024, PMID:38325380](https://www.cell.com/ajhg/fulltext/S0002-9297(24)00007-7)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Central nervous system (brain — developmental delay, intellectual disability, behavioral phenotype); craniofacial skeleton.
- **Secondary/variable:** Heart (congenital defects), kidney/urinary tract (hydronephrosis, horseshoe kidney), ear (sensorineural hearing loss), eye, musculoskeletal system (scoliosis, joint laxity), endocrine glands (parathyroid, gonads), gastrointestinal tract.
- **Body systems:** Nervous, craniofacial/skeletal, cardiovascular, renal, endocrine, auditory, ocular, gastrointestinal.

**Tissue/cell level:**
- Neural progenitor cells and developing cortical neurons (inferred from stem-cell biology of ZFX).
- Parathyroid chief cells (adenoma formation).
- Hematopoietic stem cell compartment (demonstrated in mouse Zfx studies, not directly assessed in MRXS37 patients but biologically relevant given shared ZFX-dependent self-renewal program).

**Subcellular level:** Nucleus (ZFX is a nuclear transcription factor; NLS-disrupting variants — e.g., in the related but distinct HNRNPH2/Bain-type disorder — impair nuclear localization; for ZFX the DBD zinc fingers act at chromatin). Suggested GO Cellular Component term: "nucleus" (GO:0005634), "nucleoplasm" (GO:0005654).

**Localization:** Bilateral/systemic (developmental disorder affecting multiple organ systems symmetrically; no lateralization reported).

**Suggested UBERON terms:** "brain" (UBERON:0000955), "cerebral cortex" (UBERON:0000956), "parathyroid gland" (UBERON:0001132), "heart" (UBERON:0000948), "kidney" (UBERON:0002113), "inner ear" (UBERON:0001846).

---

## 8. Temporal Development

- **Onset:** Congenital/early infancy. Reported cases show motor and speech delay evident from early childhood (e.g., PMID:41074764 describes onset "in early childhood").
- **Onset pattern:** Insidious/developmental rather than acute.
- **Progression:** The core neurodevelopmental phenotype is generally **static** (a developmental disorder rather than a degenerative one), though endocrine complications (hyperparathyroidism, potential parathyroid adenoma) can manifest or progress later in life, representing an evolving component of the phenotype.
- **Disease stages:** No formal staging system exists; this is not a staged disease in the oncologic sense.
- **Disease course:** Chronic, lifelong; no spontaneous remission reported.
- **Critical periods:** Not formally established, but early developmental intervention (as for other NDDs) would be expected to be beneficial during early childhood.

No natural history studies, longitudinal cohorts, or disease registries specific to MRXS37 were identified — consistent with its very recent (2024) delineation.

---

## 9. Inheritance and Population

**Epidemiology:** No formal prevalence or incidence estimates exist. This is an **ultra-rare, recently described disorder** — the entire published literature comprises approximately 30 individuals (14 males and up to 16 females cumulatively reported across the 2024 AJHG cohort and subsequent case reports as of late 2025/2026).

**Inheritance pattern:** X-linked, with both **de novo occurrence** (predominant, ~56% in the founding cohort) and **maternal inheritance** from mildly/subclinically affected mothers.

**Penetrance:** Variable/incomplete, especially in females — "some [female carriers] may even be asymptomatic" (OMIM #301118). This incomplete penetrance is mechanistically notable because ZFX escapes X-inactivation (unlike most X-linked genes), which would typically be expected to increase (not decrease) female expressivity relative to genes subject to XCI — the variable expressivity observed instead likely reflects variant-specific effects (missense vs. truncating) and possibly stochastic/tissue-specific expression modulation.

**Expressivity:** Highly variable, spanning asymptomatic carriers to severely affected males and, per the 2025/2026 literature, syndromic females with extensive multi-organ involvement.

**Genetic anticipation:** Not reported/not applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically documented in the literature reviewed but is a theoretical possibility relevant to recurrence-risk counseling in any de novo-appearing X-linked condition.

**Founder effects:** None reported; variants have arisen independently (de novo) in unrelated families.

**Consanguinity:** Not implicated as a risk factor (X-linked dominant/de novo pattern rather than autosomal recessive).

**Carrier frequency:** Not established given the small number of reported families and predominance of de novo variants.

**Sex ratio:** Both sexes affected, but with sex-differential severity — "male mutation carriers tend to be more severely affected than female mutation carriers" (OMIM #301118). Total reported cases per most recent literature: 14 males, up to 16 females.

**Geographic/ethnic distribution:** No specific enrichment reported; cohorts described are drawn from international clinical genetics referral populations (exact case series data spans North American and international cohorts per the AJHG multi-center study).

---

## 10. Diagnostics

**Clinical tests:**
- No disease-specific biomarker or biochemical assay exists.
- **Relevant laboratory work-up given the endocrine association:** serum calcium and parathyroid hormone (PTH) levels are recommended in patients with a confirmed ZFX missense (DBD) variant, given the demonstrated hyperparathyroidism association (PMID for JCEM Case Reports, PLOS One 2025).
- **Imaging:** Brain MRI is commonly performed given the neurodevelopmental presentation, showing variable findings (corpus callosum hypoplasia, cerebral atrophy, cerebellar vermian hypoplasia in at least one reported case) — not diagnostic in itself but useful for phenotyping and ruling out alternative etiologies.
- **Echocardiography** and **renal ultrasound** are reasonable given the reported congenital heart and genitourinary anomaly rates.
- **Audiology testing** given reported sensorineural hearing loss.

**Genetic testing (primary diagnostic modality):**
- **Exome sequencing (WES) or genome sequencing (WGS)** is the diagnostic method used in essentially all reported cases (trio-based sequencing identifying de novo variants, or targeted segregation analysis for inherited variants) — this is a gene newly implicated in disease, so **targeted single-gene panels for "X-linked intellectual disability" would need to specifically include ZFX**, and many older ID gene panels may not yet include it given its 2024 discovery.
- **Single-gene ZFX Sanger confirmation/segregation analysis** in relatives following exome/genome finding.
- **Chromosomal microarray (CMA)** is typically part of the standard first-tier NDD work-up to exclude copy-number etiologies before/alongside sequencing, though MRXS37 itself is caused by sequence-level variants, not CNVs.
- No specific role for karyotyping, FISH, mitochondrial DNA testing, or repeat-expansion testing has been described for this disorder.

**Omics-based diagnostics:** Not part of routine diagnosis; functional transcriptional-activity assays (luciferase reporter) have been used in a **research** context to support variant pathogenicity classification for novel missense alleles, not as a clinical diagnostic test.

**Clinical criteria:** No formal consensus diagnostic criteria (e.g., DSM/ICD-style) have been published; diagnosis rests on molecular confirmation of a pathogenic ZFX variant in the context of a compatible phenotype (recurrent facial gestalt + developmental delay/ID + variable multisystem anomalies).

**Differential diagnosis:** Given overlapping features (X-linked ID, facial dysmorphism, congenital anomalies, endocrine involvement), differentials would include other X-linked syndromic ID disorders such as **HNRNPH2-related (Bain-type) MRXSB (OMIM #300986)**, other zinc-finger-associated NDDs (e.g., ZFHX3, ZFHX4, ZNF711), and other causes of syndromic ID with hyperparathyroidism (e.g., MEN1-related syndromes, though these are autosomal and tumor-predominant rather than NDD-predominant).

**Screening:** No population or newborn screening applies (private, ultra-rare monogenic disorder identified only via clinical/diagnostic sequencing).

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No mortality data have been reported; there is no indication in the literature that MRXS37 shortens lifespan, though the cohort is too young/recently described for long-term outcome data.
- **Morbidity/function:** Variable functional outcomes. OMIM notes prognostic optimism relative to many syndromic ID disorders: **"Many patients are able to attend mainstream schools with assistance and work under supervision"** (OMIM #301118), suggesting a generally mild-to-moderate functional trajectory for many affected individuals, particularly females and those with milder variant effects.
- **Complications:** Hyperparathyroidism/parathyroid adenoma is a recognized complication in the missense-variant subgroup, warranting endocrine surveillance; other reported complications include recurrent seizures (including absence seizures), congenital heart defects requiring surgical correction, and renal anomalies.
- **Recovery potential:** Not a degenerative disorder in most cases (though the related but distinct HNRNPH2/Bain-type MRXSB disorder does show developmental regression in some patients — this should **not** be conflated with MRXS37/ZFX, which has not been reported to show regression).
- **Prognostic factors:** Preliminary genotype-phenotype correlation suggests **variant type is prognostically informative** — missense DBD variants correlate with hyperparathyroidism risk; truncating variants presumably behave via straightforward haploinsufficiency. No formal severity-scoring or prognostic biomarker system has been developed given the small case numbers to date.

---

## 12. Treatment

**No disease-specific or targeted pharmacotherapy exists for MRXS37.** Management is entirely **supportive and multidisciplinary**, following standard practice for syndromic intellectual disability:

- **Developmental/rehabilitative therapies:** Early intervention services, physical therapy, occupational therapy, and speech-language therapy for developmental delay (NCIT:C15302 Physical Therapy; NCIT:C159273 Speech Therapy; NCIT:C121351 Occupational Therapy).
- **Behavioral management:** Behavioral therapy/counseling for autism spectrum disorder and behavioral symptoms (NCIT:C181743 Behavioral Counseling); pharmacotherapy for co-occurring ADHD/anxiety/aggression is used symptomatically as in general ASD/ID management, not disease-specific.
- **Seizure management:** Anti-seizure medication as clinically indicated for reported absence/other seizure types (NCIT:C15632-adjacent Pharmacotherapy; specific agent selection per epilepsy type, not disease-specific).
- **Surgical/interventional:** Cardiac surgical correction for congenital heart defects as indicated (NCIT:C15329 Surgical Procedure); orthopedic management (e.g., for scoliosis) (NCIT:C16186 Orthopedic Surgical Procedure); urological surgery for cryptorchidism/hypospadias as indicated.
- **Endocrine management:** Monitoring of serum calcium/PTH; **parathyroidectomy** for symptomatic/significant primary hyperparathyroidism or parathyroid adenoma in the missense-variant subgroup (NCIT:C15329 Surgical Procedure — parathyroidectomy specifically).
- **Audiology/ENT:** Hearing aids or other amplification devices for sensorineural hearing loss.
- **Genetic counseling:** Recommended for families given the de novo/variably inherited pattern and recurrence-risk implications (NCIT:C15240 Genetic Counseling).
- **Supportive care:** General supportive/multidisciplinary care coordination (NCIT:C15747 Supportive Care).

**Experimental/investigational treatments:** No gene therapy, RNA-based therapy, or targeted molecular therapy has been reported or is in clinical trials for ZFX-related disorder specifically (no ClinicalTrials.gov entries identified for MRXS37/ZFX-NDD as of this search).

**Treatment outcomes/algorithms:** No standardized treatment algorithm or published response-rate data exist given the rarity and recency of this diagnosis.

---

## 13. Prevention

- **Primary prevention:** Not applicable — this is a de novo/inherited monogenic disorder with no known modifiable risk factor.
- **Secondary prevention:** Early diagnosis via genetic testing enables early developmental intervention; endocrine screening (calcium/PTH) in variant-positive individuals (particularly missense DBD carriers) could allow early detection of hyperparathyroidism/parathyroid adenoma before complications (nephrocalcinosis, kidney stones — both reported phenotypic features) develop.
- **Genetic counseling and reproductive options:** Recommended for families with an identified pathogenic variant, including discussion of recurrence risk (de novo vs. inherited), possible prenatal diagnosis, or preimplantation genetic testing in future pregnancies, per standard practice for X-linked disorders (NSGC/ACMG frameworks) — no disorder-specific guideline has been published.
- **Public health/immunization/prophylaxis:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring ZFX-related disease has been reported in non-human species (e.g., companion animals, livestock, or wildlife) in OMIA or veterinary literature searched.
- **Orthologous gene:** Mouse *Zfx* (Mouse Genome Informatics; NCBI Gene) is the principal ortholog used experimentally. Notably, **mouse Zfx does NOT escape X-inactivation** the way human ZFX does — it maps near the mouse X-inactivation center (PMID:2052543) — representing an important **species divergence** relevant to interpreting mouse model data (a human-model-mismatch consideration for dosage-sensitivity extrapolation).
- **Comparative biology:** ZFX belongs to a small gene family with paralogs **ZFY** (Y-linked) and **ZNF711** (autosomal), sharing structural and possibly partially redundant functional features; ZFY has also been examined (with largely negative results) for a parallel role in parathyroid adenoma.
- **Zebrafish:** *zfx* zebrafish knockouts show conserved neurobehavioral phenotypes (described in Section 4/6), supporting deep evolutionary conservation of ZFX's neurodevelopmental role, though zebrafish is not a "natural disease" model per se but an induced loss-of-function model.
- **Zoonotic potential:** Not applicable (non-infectious, monogenic disorder).

---

## 15. Model Organisms

**Zebrafish (induced, loss-of-function):**
- ***zfx* knockout zebrafish** (CRISPR-generated, per PMID:38325380) recapitulate a **behavioral/neuropsychiatric-like phenotype**: altered novel-tank-assay exploration, altered light/dark preference (scototaxis), and enhanced startle response — supporting causality of ZFX loss for neurobehavioral dysfunction. This model captures behavioral but not the full syndromic (craniofacial/cardiac/endocrine) human phenotype.
- **Limitation:** Zebrafish models capture conserved neurobehavioral circuitry but cannot recapitulate human-specific craniofacial gestalt, cardiac malformation, or endocrine (parathyroid) phenotypes.

**Mouse (genetic models, gene-function studies rather than disease-specific models):**
- **Zfx knockout mice** are viable but show **impaired self-renewal of embryonic stem cells (ESCs) and adult hematopoietic stem cells (HSCs)**, with increased apoptosis and stress-gene upregulation, while short-term progenitor function and fetal HSC/erythromyeloid progenitors are relatively spared (Cell 2007, Harel/Lengner group). This establishes ZFX's essential role in stem/progenitor cell maintenance but has **not** been characterized as a full syndromic neurodevelopmental disease model (no published assessment of craniofacial, cardiac, or cognitive/behavioral phenotyping analogous to the human disorder).
- **Human model mismatch consideration:** Because mouse *Zfx* is subject to X-inactivation (unlike human ZFX), the dosage biology in mouse models may not fully mirror the human disease mechanism — an important caveat for translational interpretation of any future *Zfx* conditional/disease-specific mouse model.

**Human embryonic stem cells (in vitro):**
- **ZFX controls self-renewal of human ESCs** (PMC3411758), described as a "molecular rheostat" balancing self-renewal versus differentiation — directly relevant, evolutionarily conserved, human cellular evidence for the stem-cell-maintenance mechanism proposed to underlie the neurodevelopmental phenotype.

**Cultured cell reporter assays (in vitro, variant functional characterization):**
- Luciferase/transcriptional-reporter assays in cultured cells were used to demonstrate **differential transcriptional activity of DNA-binding-domain missense variants** versus wild-type ZFX, supporting a functional (not merely bioinformatic) basis for missense variant pathogenicity (PMID:38325380).

**Resources:** MGI (Mouse Genome Informatics) for *Zfx* alleles; ZFIN for zebrafish *zfx* lines; no dedicated MRXS37 model organism database or registry exists given the disorder's recent characterization.

---

## Summary of Key Citations

| PMID/Source | Content |
|---|---|
| OMIM #301118 | Clinical synopsis, disease definition, gene assignment |
| OMIM *314980 | ZFX gene entry, structure/function |
| PMID:38325380 (Shepherdson et al., *AJHG* 2024) | Founding cohort (18 pts/16 families), variant spectrum, facial gestalt, functional/zebrafish studies |
| PMID:41074764 (*AJMG-A*, 2025/2026 case report) | Female frameshift case, phenotype expansion, updated cumulative case counts |
| PMID:25594030 | Recurrent somatic ZFX mutations (R786/787) in sporadic parathyroid adenomas |
| PLOS One 2025 (germline ZFX/PHPT) | Genotype-phenotype link between missense DBD variants and hyperparathyroidism |
| PMID:1970799 / PMID:2500252 | ZFX escapes X-inactivation in humans |
| PMID:2052543 | Mouse *Zfx* subject to X-inactivation (species divergence) |
| Cell 2007 (Harel/Lengner) & PMC3411758 | Zfx/ZFX controls ESC and HSC self-renewal (mouse and human) |

**Notable data gaps for curation:** No GeneReviews chapter, no Orphanet ORPHA code, no formal prevalence/incidence estimate, no published natural history study, no clinical trials, and no disease-specific (as opposed to gene-function) animal model exist as of this search — all consistent with MRXS37 being a disorder characterized only since 2024.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.