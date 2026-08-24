---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T00:35:17.781009'
end_time: '2026-08-01T00:53:30.342973'
duration_seconds: 1092.56
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MSMO1 deficiency
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 11
  num_turns: 83
  total_cost_usd: 5.890569999999999
  session_id: ac027c74-88c0-4fdf-a0e5-ae3ee3e69e80
  stop_reason: end_turn
citation_count: 28
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MSMO1 deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MSMO1 deficiency** covering all of the
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

# MSMO1 Deficiency (Microcephaly–Congenital Cataract–Psoriasiform Dermatitis Syndrome, MCCPD)
## Comprehensive Research Report for Knowledge Base Curation

**Compiled:** 1 August 2026
**Disease category:** Mendelian; inborn error of post-squalene cholesterol biosynthesis
**Evidence base:** ~11 reported individuals from ~8 families worldwide (ultra-rare)

> **Curation caveat up front.** This is an ultra-rare disorder whose entire published clinical evidence base consists of single case reports and small sibships. Almost every "frequency" figure below is a denominator of ≤11 patients. Per the dismech frequency-evidence SOP, most phenotype `frequency:` fields should be **omitted** rather than fabricated; I flag below the handful where a defensible qualitative band exists.

---

## 1. Disease Information

### Overview

MSMO1 deficiency is an autosomal recessive inborn error of the **distal (post-squalene) cholesterol biosynthesis pathway**, caused by biallelic loss-of-function (predominantly missense) variants in *MSMO1* (formerly *SC4MOL*), encoding **methylsterol monooxygenase 1** / sterol-C4-methyl oxidase (SMO). The enzymatic block at the first step of sterol C4-demethylation causes accumulation of **4α-monomethylsterols** and **4,4′-dimethylsterols** — a class that includes the biologically active **meiosis-activating sterols (MAS)** — with variably reduced cholesterol synthesis.

The core clinical picture is the triad of **microcephaly, congenital cataract, and psoriasiform dermatitis**, plus growth and developmental delay and immune dysregulation. Importantly, it is one of the few neurodevelopmental disorders that is **partially treatable** by pathway-directed therapy (cholesterol supplementation + statin, oral and topical).

> "Deficiency of SMO represents a biochemical defect in the cholesterol synthesis pathway, the clinical spectrum of which remains to be defined." — He et al. 2011, J Clin Invest (**PMID:21285510**; DOI 10.1172/JCI42650)

> "MSMO1 deficiency (OMIM #616834) is an ultrarare autosomal recessive disorder of distal cholesterol metabolism with only five cases reported to date. The disorder is caused by missense variants in the MSMO1 gene encoding methylsterol monooxygenase 1, leading to the accumulation of methylsterols." — Tkemaladze et al. 2023, Clin Dysmorphol (**PMID:37195326**; DOI 10.1097/MCD.0000000000000461)

### Key identifiers

| Resource | Identifier |
|---|---|
| **MONDO** | **MONDO:0014793** — "microcephaly-congenital cataract-psoriasiform dermatitis syndrome" *(verified via OLS4)* |
| **OMIM (phenotype)** | **616834** — MICROCEPHALY, CONGENITAL CATARACT, AND PSORIASIFORM DERMATITIS; MCCPD |
| **OMIM (gene)** | **607545** — *MSMO1* (SC4MOL) |
| **Orphanet** | **ORPHA:488168** — Microcephaly-congenital cataract-psoriasiform dermatitis syndrome |
| **MedGen** | UID 1798933 / Concept ID **C5567510** |
| **UMLS** | C5567510 |
| **GARD** | 0017886 (rarediseases.info.nih.gov/diseases/17886) |
| **HGNC** | **HGNC:10545** (`hgnc:10545`) |
| **NCBI Gene** | 6307 |
| **Ensembl gene** | ENSG00000052802 |
| **UniProt** | **Q15800** (ERG25_HUMAN / MSMO1) |
| **EC number** | **EC 1.14.18.9** (methylsterol monooxygenase) |
| **ICD-10** | No specific code. Best fit **E78.7** "Disorders of bile acid and cholesterol metabolism" (generic bucket for cholesterol biosynthesis defects). *Not independently confirmed as an official Orphanet mapping — flag as inferred.* |
| **ICD-11** | No specific code identified. *Not available.* |
| **MeSH** | No dedicated descriptor identified. *Not available.* |

### Synonyms and alternative names

- Microcephaly, congenital cataract, and psoriasiform dermatitis (**MCCPD**)
- **SC4MOL deficiency**
- **SMO deficiency** / sterol-C4-methyl oxidase deficiency
- Methylsterol monooxygenase 1 deficiency
- Microcephaly with congenital cataract and psoriasiform dermatitis
- Gene aliases: *SC4MOL*, *ERG25*, *DESP4*, *MCCPD*

### Provenance of the information

**Disease-level aggregated resources** (OMIM, Orphanet, MedGen, GARD, HPO) are derived almost entirely from **individual published case reports**, not EHR cohorts or registries. The HPO annotation set for OMIM:616834 is dominated by a single source (PMID:21285510, the index patient), with frequencies recorded as literal `1/1`. There is **no disease registry, natural history study, or EHR-derived cohort** for MSMO1 deficiency.

---

## 2. Etiology

### Disease causal factors

**Purely genetic (monogenic, autosomal recessive).** Biallelic pathogenic variants in *MSMO1* (4q32.3) abolish or severely reduce sterol-C4-methyl oxidase activity. No infectious, environmental, or acquired etiology exists.

Mechanistically, the causal factor is a **metabolic block at the first of three enzymatic steps of C4-demethylation** in the post-squalene cholesterol pathway, producing a dual insult: (i) **substrate accumulation** of bioactive methylsterols, and (ii) **product deficiency** of cholesterol.

### Risk factors

**Genetic:**
- **Biallelic *MSMO1* pathogenic variants** — necessary and sufficient (see §4). Relationship type: CAUSAL.
- **Consanguinity** — a demonstrated major risk factor. Homozygous variants were reported in a consanguineous **Turkish** family (Kalay Yildizhan et al. 2020, PMID:33161406) and a consanguineous **Georgian** family (Tkemaladze et al. 2023, PMID:37195326).
- **Carrier (heterozygous) status** — carriers are clinically unaffected but are **not biochemically silent**: "Methylsterol levels were also increased (though less so) in the plasma of the patient's parents" (He et al. 2011). Strikingly, the index patient's **father** showed granulocyte activation phenotypes approaching the proband's: "activated CD16+ granulocytes ... were increased 30- and 20-fold in the patient and her father, respectively" (PMID:21285510). This raises a genuinely open question about a **heterozygote phenotype** (possible risk factor for common inflammatory skin disease) — see §4 modifier discussion.

**Environmental / non-genetic modifiers of expression (not of occurrence):**
- **Cold/winter season and psychological stress** worsened dermatitis in the index patient: "Dermatitis worsened in winter or with stress" (PMID:21285510). This is an exacerbating factor, not a disease-risk factor.
- **Dietary cholesterol intake** — theoretically modifies substrate/product balance; there is no published evidence that dietary cholesterol status modifies disease onset.
- No toxin, radiation, occupational, or infectious risk factor has been reported.

### Protective factors

- **Genetic protective factors:** none identified. No modifier alleles or protective variants have been described.
- **Environmental protective factors:** exogenous **cholesterol supplementation** is therapeutic (see §12) rather than preventive; it does not prevent disease onset in a genetically affected individual but reduces methylsterol burden and cutaneous/immune manifestations.
- Note a mechanistically interesting *pharmacologic* observation: metabolic blockade **upstream** of MSMO1 is protective at the cellular level. "Metabolic blocks upstream of SC4MOL with ketoconazole rescued viability and EGFR degradation" (Sukhanova et al. 2013, Cancer Discov, **PMID:23125191**; DOI 10.1158/2159-8290.CD-12-0031). This is the conceptual rationale for statin co-therapy in patients (reduce flux into the blocked step).

### Gene–environment interactions

The clearest GxE interaction in this disorder is **pharmacological**: the genetic block interacts with (a) exogenous cholesterol and (b) HMG-CoA reductase inhibition to determine methylsterol burden. He et al. 2014 documented a dose/regimen interaction:

> Cholesterol supplementation (100 mg/kg/day) alone reduced methylsterol levels by ~20%; addition of "oral statin (10 mg/day) plus bile acids (30 mg/kg/day) along with cholesterol normalized" methylsterol levels. — He et al. 2014, BBA (**PMID:24144731**; DOI 10.1016/j.bbalip.2013.10.009)

A second GxE axis is **azole/vitamin D analog drug metabolism**: MSMO1 participates in hepatic metabolism of the anti-osteoporosis vitamin D analog eldecalcitol (Yasuda et al. 2015, **PMID:26038696**), implying potential altered handling of such compounds in deficient patients — theoretical, no clinical data.

---

## 3. Phenotypes

### 3.1 HPO annotation set for OMIM:616834 (retrieved from the HPO/JAX API, August 2026)

All frequencies are literal counts from the annotation file; **`1/1` reflects the single index patient (PMID:21285510), not a population frequency.**

| HPO ID | Label | Category | HPO frequency | Source |
|---|---|---|---|---|
| HP:0000252 | Microcephaly | Head/neck | 1/1 | PMID:21285510 |
| HP:0000519 | Developmental cataract | Eye | 1/1 | PMID:21285510 |
| HP:0003765 | Psoriasiform dermatitis | Immunology/skin | 1/1 | PMID:21285510 |
| HP:0008064 | Ichthyosis | Skin | 1/1 | PMID:21285510 |
| HP:0000498 | Blepharitis | Head/neck | 1/1 | PMID:21285510 |
| HP:0001263 | Global developmental delay | Nervous system | 1/1 | PMID:21285510 |
| HP:0001256 | Mild intellectual disability | Nervous system | — | OMIM:616834 |
| HP:0001508 | Failure to thrive | Growth | 1/1 | PMID:21285510 |
| HP:0004322 | Short stature | Growth | 1/1 | PMID:21285510 |
| HP:0002750 | Delayed skeletal maturation | Skeletal | 1/1 | PMID:21285510 |
| HP:0000823 | Delayed puberty | Endocrine | — | OMIM:616834 |
| HP:0002829 | Arthralgia | Musculoskeletal | — | OMIM:616834 |
| HP:0003146 | Hypocholesterolemia | Lab | 1/1 | PMID:21285510 |
| HP:0003233 | Decreased circulating HDL-C concentration | Lab | 1/1 | PMID:21285510 |
| HP:0003563 | Decreased circulating LDL-C concentration | Lab | 1/1 | PMID:21285510 |
| **HP:6000753** | **Elevated circulating monomethyl sterol concentration** | Lab | 1/1 | PMID:21285510 |
| **HP:6000754** | **Elevated circulating dimethyl sterol concentration** | Lab | 1/1 | PMID:21285510 |
| **HP:6001113** | **Elevated circulating methysterol concentration** | Lab | — | OMIM:616834 |
| HP:0011463 | Childhood onset | Clinical course | 1/1 | PMID:21285510 |
| HP:0000007 | Autosomal recessive inheritance | Inheritance | — | PMID:21285510 |

> **Curation note:** HP:6000753 / HP:6000754 / HP:6001113 are the disease-defining biochemical HPO terms and are the highest-value annotations for this entry. Note HP:6001113's label is spelled "methysterol" in HPO (sic) — reproduce exactly in `term.label`.

### 3.2 Phenotypes reported in the literature but **not yet in the HPO annotation set**

These come from patients published after the HPO annotation was created. Each needs its own evidence item.

| Feature | HPO suggestion *(verified where marked ✓)* | Reported in |
|---|---|---|
| Alopecia / hair changes | **HP:0001596 Alopecia** ✓ (OLS-verified) | Tkemaladze 2023 (PMID:37195326); He 2014 "hair changes" (PMID:24144731) |
| Polydactyly | **HP:0010442 Polydactyly** ✓ (OLS-verified); postaxial subtype **HP:0100259** ✓ | Tkemaladze 2023 (PMID:37195326) |
| Spasticity / spastic quadriplegia | HP:0001257 Spasticity; HP:0002510 Spastic tetraplegia *(unverified — check with OAK)* | Tkemaladze 2023; Hassas 2026 (PMID:41718295) |
| Nystagmus | HP:0000639 Nystagmus *(unverified)* | Kalay Yildizhan 2020 (PMID:33161406); Morales 2022 |
| Optic nerve hypoplasia | HP:0000609 Optic nerve hypoplasia *(unverified)* | Kalay Yildizhan 2020 (PMID:33161406) |
| Myopia | HP:0000545 Myopia *(unverified)* | Kalay Yildizhan 2020 |
| Strabismus | HP:0000486 Strabismus *(unverified)* | Kalay Yildizhan 2020 |
| Severe intellectual disability | HP:0010864 *(unverified)* | Kalay Yildizhan 2020 |
| Autism spectrum disorder | HP:0000717 Autism *(unverified)* | Morales, Curry & Enns 2022 (DOI 10.20517/jtgg.2022.01) |
| Behavioral abnormality | HP:0000708 *(unverified)* | Frisso 2017 (PMID:28673550) |
| Joint contractures | HP:0034392 / HP:0001371 *(unverified)* | He 2014, patient 2 (PMID:24144731) |
| Cerebral white matter volume loss / T2-FLAIR hyperintensity | HP:0012429 Cerebral white matter atrophy; HP:0002500 Abnormal cerebral white matter morphology *(unverified)* | Hassas 2026 (PMID:41718295) |
| Genu valgum | HP:0002857 *(unverified)* | Morales 2022 |
| Segmental hyperpigmentation | HP:0011821 / HP:0001000 *(unverified)* | Hassas 2026 |
| Erythroderma / ichthyosiform erythroderma | HP:0001019 Erythroderma *(unverified)* | He 2011 (PMID:21285510) |
| Immune dysregulation / recurrent infection | HP:0002721 Immunodeficiency; HP:0002960 Autoimmunity *(unverified)* | He 2011, He 2014 |
| Scalp scaling / dandruff | (no precise HPO; consider HP:0011368 Eczematoid dermatitis or HP:0001051 seborrheic-type) | Frisso 2017 — "abundant scalp dandruff, without other skin manifestations" |

### 3.3 Phenotype characteristics by domain

**Dermatologic — psoriasiform dermatitis (the most distinctive feature)**
- **Type:** physical manifestation / clinical sign.
- **Onset:** typically **infancy to early childhood**, but *not* congenital. In the index patient: "She did not show signs of dermatitis at birth; it was first noted around her umbilicus at the age of 2" and "subsequently progressed to her back, trunk, and then the remainder of her body by the age of 6" (PMID:21285510). Patients 3 and 4 had "severe skin manifestations similar to patient one beginning in early infancy" (PMID:24144731).
- **Severity:** highly **variable** — from full-body ichthyosiform erythroderma sparing only the palms (index patient), to isolated scalp dandruff (Frisso 2017), to transient perianal dermatitis (Morales 2022), to **absent** ("her skin is dry but has never demonstrated a marked psoriasiform rash," He 2014 patient 2), to no dermatitis at all (Hassas 2026).
- **Progression:** chronic, **fluctuating/relapsing** with seasonal and stress triggers.
- **Frequency:** roughly 6–8 of ~11 reported individuals. Defensible band: **FREQUENT** (with explicit evidence quote), or omit.
- **QoL impact:** substantial — pruritus, disfigurement, thermoregulatory and barrier compromise, and refractoriness to conventional psoriasis therapy (steroids, calcipotriene, cyclosporine, etanercept, phototherapy, isotretinoin all failed in the index patient). No formal QoL instrument (DLQI, EQ-5D, PROMIS) has ever been applied in this disease — **not available.**

**Ocular — congenital/infantile cataract**
- **Type:** physical manifestation.
- **Onset:** **congenital or within the first year**. Diagnosed at 8 months in Hassas 2026; requiring lensectomy at 7 months in Morales 2022.
- **Laterality:** **bilateral** in all reported cases.
- **Severity:** vision-threatening; requires surgery. Hassas 2026: "diffuse cataracts bilaterally with scattered, white fleck-like opacities in the anterior lens," with "intumescent appearance with significant lenticular liquefaction"; post-operatively only "perception to light."
- **Progression:** progressive opacification; **not reversible** by metabolic therapy — the critical period has passed by diagnosis.
- **Frequency:** present in essentially every reported patient — the most consistent feature. Defensible band: **VERY_FREQUENT**.
- **QoL impact:** severe and permanent; drives lifelong low vision, compounding developmental delay.
- Associated ocular findings: blepharitis, nystagmus, optic nerve hypoplasia, myopia, strabismus.

**Neurologic — microcephaly, developmental delay, intellectual disability**
- **Onset:** congenital (microcephaly) to infantile (developmental delay).
- **Severity:** **variable** — "mild developmental delay" and mild ID in the index patient; "severe intellectual disability" in the Turkish siblings; non-verbal, non-ambulatory with spastic quadriplegia in Hassas 2026; ASD with normal head circumference in the mildest case (Morales 2022).
- **Progression:** **static/non-progressive** developmental impairment in most; spasticity may be progressive. No neurodegeneration has been documented.
- **Microcephaly frequency:** **not universal** — explicitly absent in Frisso 2017 ("but not microcephaly") and Morales 2022 ("Normal head circumference (unlike typical MCCPD triad cases)"). Defensible band: **FREQUENT**, not obligate.
- **QoL:** dominant driver of lifelong dependency in severe cases.

**Growth and endocrine**
- Failure to thrive, short stature, delayed skeletal maturation with **normal bone morphology** (PMID:21285510), delayed puberty. Index patient at age 13: height 140 cm (<3rd centile; 50th centile for a 10.5-year-old); weight 28.6 kg (<3rd centile; 50th centile for a 9-year-old); OFC 53.5 cm (<3rd centile).
- Onset: infancy/childhood; **progressive** relative to peers; partially treatment-responsive.

**Immunologic**
- Type: laboratory abnormality + clinical immune dysregulation.
- Granulocyte and T-cell abnormalities (detailed in §6). Elevated serum GM-CSF, IL-6, IL-8; **normal TNF-α** — which correctly predicted etanercept failure.
- Onset: presumably congenital; detected only on specialized flow cytometry.

**Laboratory / biochemical (the diagnostic core)**
- **Elevated 4α-monomethylsterols (~20-fold) and 4,4′-dimethylsterols (~500-fold)** in plasma; dimethylsterol preferentially accumulates in **skin scales**.
- **Cholesterol is variably low** — index patient total cholesterol 85 mg/dL (nl 140–176), HDL 28 (nl 35–75), LDL 49 (nl 70–160), triglycerides normal at 84. He 2014 patient 2: ~90 mg/dL. **But patients 3, 4 had normal cholesterol**, and Morales 2022 reported "Normal total cholesterol levels throughout." Hassas 2026 reported "Normal serum lipid measurements."
- **Curation implication:** hypocholesterolemia is a *supportive*, not obligate, finding. **Methylsterol elevation is the obligate biochemical signature.** Do not model normal cholesterol as excluding the diagnosis.

---

## 4. Genetic / Molecular Information

### Causal gene

**MSMO1** (methylsterol monooxygenase 1), formerly *SC4MOL*.

| Attribute | Value |
|---|---|
| HGNC | `hgnc:10545` |
| Cytoband | **4q32.3** |
| GRCh38 coordinates | NC_000004.12: 165,327,669–165,343,164 |
| Exons | 6 |
| Canonical RefSeq | **NM_006745.5** → NP_006736.1 (isoform 1, 293 aa) |
| Other transcripts | NM_001440534.1 (isoform 1); NM_001017369.3 → NP_001017369.1 (isoform 2) |
| OMIM gene | 607545 |
| UniProt | Q15800 |
| Protein family | **Sterol desaturase family** (fatty acid hydroxylase superfamily) |
| Topology | ER membrane, **multi-pass**; three helical TM segments at aa 55–75, 100–120, 199–219 |
| Cofactor | **Fe cation (non-heme di-iron)**; electron donor Fe(II)-cytochrome *b5* |
| Expression | Broad; highest in **liver** (RPKM 94.8), then **brain** (RPKM 43.2), plus ~20 other tissues (NCBI Gene); UniProt notes "Enhanced expression in liver" |

### Reported pathogenic variants (all published cases)

All disease-causing variants reported to date are **missense**; no truncating, splice, or structural variant has been reported as causal. This is consistent with the gene being **intolerant of complete loss of function** (see constraint below and the zebrafish/mouse data in §15) — i.e., human MSMO1 deficiency likely represents **hypomorphic residual activity**, not a true null state.

| cDNA (NM_006745.5) | Protein | Zygosity / origin | Family / ethnicity | Reference |
|---|---|---|---|---|
| c.519T>A | **p.His173Gln** | compound het (paternal) | Family 1 (index) | He 2011, PMID:21285510 |
| c.731A>G | **p.Tyr244Cys** | compound het (maternal) | Family 1 | He 2011, PMID:21285510 |
| c.343G>A | **p.Gly115Arg** | homozygous | Family 2 (Hispanic) | He 2014, PMID:24144731 |
| c.605G>A | **p.Gly202Glu** (novel at the time) | compound het (maternal) | Family 5 (Italian) | Frisso 2017, PMID:28673550 |
| c.731A>G | **p.Tyr244Cys** | compound het (paternal) | Family 5 (Italian) | Frisso 2017, PMID:28673550 |
| c.81A>C | **p.Asn27Thr** | homozygous | Family 6 (consanguineous Turkish) | Kalay Yildizhan 2020, PMID:33161406 |
| c.536C>T | **p.Pro179Leu** (VUS) | compound het (maternal) | Family 7 | Morales/Curry/Enns 2022, DOI 10.20517/jtgg.2022.01 |
| c.731A>G | **p.Tyr244Cys** (likely pathogenic) | compound het (paternal) | Family 7 | Morales 2022 |
| c.548A>C | **p.Glu183Ala** (novel) | homozygous | Family 8 (consanguineous Georgian) | Tkemaladze 2023, PMID:37195326 |
| c.343G>A | **p.Gly115Arg** | homozygous | Family 9 | Hassas 2026, PMID:41718295 |

**Recurrent alleles:** **c.731A>G (p.Tyr244Cys)** has now been seen in three unrelated families (US, Italy, US) and **c.343G>A (p.Gly115Arg)** in two — these are the two candidate recurrent/founder-like alleles. No formal founder haplotype study exists.

**Structure–function.** Both original variants hit conserved metal-binding motifs: "Both positions encode amino acids that occur in highly conserved metal-binding domains in SMO," and "H173Q alters a predicted active site encompassing the second iron-binding motif" (PMID:21285510). PolyPhen scored Y244C at 2.5 and H173Q at 3.2 — both "probably damaging."

### Variant classification (ACMG/AMP) — worked example

For **c.343G>A (p.Gly115Arg)**, Hassas et al. 2026 reclassified from VUS to **likely pathogenic**:

> "Based on its computational predictions, rarity in the population, and presence in the homozygous state in multiple individuals with suspected MSMO1 deficiency, re-assessment of the variant's clinical significance by the study team was consistent with a classification as likely pathogenic (ACMG-AMP criteria applied: PP3_Strong, PM3, and PM2_Supporting)." — PMID:41718295

Supporting criteria detail: "The amino acid substitution is strongly predicted by AlphaMissense to be damaging to protein function (score = 0.9933)" (PP3_Strong); "It is in gnomAD v4.1 in just two heterozygous individuals" (PM2_Supporting).

### Allele frequency / population data

- **c.343G>A (p.Gly115Arg):** 2 heterozygotes in **gnomAD v4.1** (PMID:41718295). No homozygotes.
- Population frequencies for the other alleles are not published; all are ultra-rare.
- **No founder mutation, no carrier-frequency estimate, and no population-specific screening data exist.**

### Gene-level constraint (ClinGen/gnomAD v4.0, retrieved August 2026)

| Metric | Value | Interpretation |
|---|---|---|
| **pLI** | **0** | Not LoF-intolerant in the heterozygous state (expected for a recessive gene) |
| **LOEUF** | **0.9** | Moderate LoF constraint |
| DECIPHER %HI | 44.79 | Low haploinsufficiency likelihood |
| ClinGen gene-disease validity | **0 classifications** — "ClinGen has not yet published curations for MSMO1 (HGNC:10545)" | **Curation gap** — no CGGV assertion available to cite |
| ClinGen dosage sensitivity | 0 classifications | — |

> **Curation note:** because ClinGen has no MSMO1 curation, a `CGGV:` structured-source evidence item is **not available** for this entry. Gene-disease validity must be argued from primary literature (multiple unrelated families + biochemical concordance + functional data), which would support a "Definitive"-equivalent argument if curated.

### ClinVar

A gene-level ClinVar query (`MSMO1[gene]`, August 2026) returned on the order of 50 variation records across all classifications; the great majority are VUS or benign/likely benign, with the literature-reported missense alleles above carrying pathogenic/likely-pathogenic assertions. **I was unable to reliably enumerate per-variant ClinVar classifications through the accessible interfaces — verify individual variant IDs directly before asserting classifications in the KB.**

### Somatic vs germline

All disease-causing variants are **germline**. *MSMO1* is, however, of considerable **somatic/oncologic** interest as an expression-level driver rather than a mutational target (see §6 and §12): upregulation in cervical cancer associates with poor survival, and MSMO1 modulates breast-cancer chemosensitivity via T-MAS/PERK signaling (iScience 2026, DOI 10.1016/j.isci.2026.112...; ScienceDirect PII S2589004226001653). No recurrent somatic *MSMO1* mutation is reported in COSMIC/TCGA as an oncogenic driver.

### Functional consequence

**Loss of function (hypomorphic).** Missense substitutions in iron-coordinating/active-site residues reduce catalytic activity. No gain-of-function or dominant-negative mechanism has been proposed. Heterozygotes show intermediate biochemistry (elevated but sub-diagnostic methylsterols) — consistent with a **gene-dosage-sensitive enzymatic step**, though clinically unaffected.

### Modifier genes

None established. Two mechanistically plausible candidates, **untested**:
- ***NSDHL*** and ***HSD17B7*** — the other two members of the sterol C4-demethylation complex. Combined partial deficiency would be expected to be additive.
- ***CYP51A1*** and ***HMGCR*** — upstream flux controllers; genotype-determined flux may modify substrate accumulation (this is the pharmacological premise of statin therapy).

An intriguing, unresolved candidate-modifier observation is the **heterozygous father's immune phenotype** (PMID:21285510), suggesting that a single hypomorphic *MSMO1* allele may be a susceptibility factor rather than fully recessive.

### Epigenetics

**No data.** No DNA methylation, histone modification, chromatin, or episignature study of MSMO1 deficiency exists. There is no published MSMO1 episignature in the DNA-methylation-signature literature for Mendelian disorders. **Not available.**

### Chromosomal abnormalities

**None reported.** No aneuploidy, translocation, inversion, or CNV involving 4q32.3 has been reported as a cause of MSMO1 deficiency. CMA is not a diagnostic modality for this disorder.

---

## 5. Environmental Information

- **Environmental factors:** none causal. No toxicant, pollutant, radiation, or occupational exposure is implicated. CTD lists *MSMO1* as chemically responsive (notably to azoles and sterol-pathway drugs), but this is expression modulation, not disease etiology.
- **Lifestyle factors:** none causal. Cold weather and stress **exacerbate** the dermatitis (PMID:21285510). Dietary cholesterol is therapeutically relevant, not etiologic.
- **Infectious agents:** **not applicable.** No pathogen causes or triggers MSMO1 deficiency. However, the documented immune dysregulation (granulocyte activation, TLR-2/TLR-4 dysregulation, reduced CD16b) raises a theoretical concern for **altered infection susceptibility** — clinically undocumented.

---

## 6. Mechanism / Pathophysiology

### 6.1 The enzymatic lesion

Cholesterol synthesis from lanosterol requires removal of three methyl groups. **CYP51A1** removes the 14α-methyl. The two C4 methyls are removed by **two successive rounds** of a three-enzyme **sterol C4-demethylation complex** on the ER membrane:

1. **MSMO1 / SC4MOL** — sterol-C4-methyl oxidase; performs **three sequential monooxygenations** of the 4α-methyl group (methyl → hydroxymethyl → aldehyde → carboxylate), using **Fe(II)-cytochrome b5** as electron donor and a non-heme **di-iron** center (EC 1.14.18.9).
2. **NSDHL** — 3β-hydroxysteroid dehydrogenase / C4-decarboxylase.
3. **HSD17B7** — 3-ketosteroid reductase.

MSMO1 catalyzes the **rate-limiting first step**, and in the UniProt pathway annotation performs **step 3 of 6 in zymosterol biosynthesis from lanosterol**.

> "SC4MOL deficiency is the first autosomal recessive disorder identified in the sterol demethylation complex." — He et al. 2014 (PMID:24144731)

*(NSDHL deficiency causes CHILD syndrome and CK syndrome; the C4-demethylation complex is thus responsible for at least two distinct Mendelian disorders — useful for module/grouping design.)*

### 6.2 Accumulating metabolites — the meiosis-activating sterols

The block causes accumulation of the **immediate substrates**:

| Metabolite | Chemistry | CHEBI |
|---|---|---|
| **T-MAS** (testis meiosis-activating sterol) = **14-demethyllanosterol** = 4,4-dimethyl-5α-cholesta-8,24-dien-3β-ol | 4,4-dimethylsterol | **CHEBI:18364** ✓ (OLS-verified: "A 3β-sterol formed formally by loss of a methyl group from the 14-position of lanosterol") |
| **FF-MAS** (follicular fluid MAS) = 4,4-dimethyl-5α-cholesta-8,14,24-trien-3β-ol | 4,4-dimethylsterol | **CHEBI:17813** ✓ (OLS-verified) |
| 4α-monomethylsterols | monomethylsterol | (no single CHEBI class; use the HPO lab term HP:6000753) |
| Cholesterol (deficient product) | — | **CHEBI:16113** ✓ (OLS-verified) |
| Lanosterol (upstream) | — | CHEBI:16521 *(unverified — confirm with OAK)* |

**These are not inert:**
> "C4-Methylsterols are meiosis-activating sterols (MASs). They exist at high concentrations in the testis and ovary and play roles in meiosis activation. ... MASs serve as ligands for liver X receptors α and β (LXRα and LXRβ), which are important in regulating not only lipid transport in the epidermis, but also innate and adaptive immunity." — He et al. 2011 (PMID:21285510)

This dual-signaling identity (MAS = mitogenic/meiotic signal **and** LXR ligand) is the mechanistic key to the disease being far more than a cholesterol-deficiency phenotype.

### 6.3 Causal chain (upstream → downstream)

**Node 1 (MOLECULAR) — MSMO1 loss-of-function missense variant.** Substitution in an iron-binding/active-site residue reduces sterol-C4-methyl oxidase catalytic activity.
↓
**Node 2 (MOLECULAR) — Block of sterol C4-demethylation.** GO:0000254 C-4 methylsterol oxidase activity ✓ (DECREASED); GO:0006695 cholesterol biosynthetic process ✓ (DECREASED).
↓ *(branches into two arms)*

**Arm A — Substrate accumulation (dominant arm)**

**Node 3A (MOLECULAR) — Methylsterol/MAS accumulation.** 4α-monomethylsterols ↑ ~20-fold; 4,4′-dimethylsterols ↑ ~500-fold in plasma; dimethylsterol preferentially deposits in **skin** (PMID:21285510, PMID:24144731). Also demonstrated in patient fibroblasts: "Methylsterols were indeed markedly elevated in the patient's fibroblasts, but not any of the controls."
↓ *(three parallel downstream effectors)*

- **Node 4A-i (CELLULAR) — LXRα/β dysregulation.** MAS are LXR ligands. He 2011 proposes: "the reduction of TLR-4 expression in SMO deficiency may be related to inhibition of LXR by T-MAS, which is structurally similar to FF-MAS," noting "activated LXR binds to TLR-4 promoter through an LXRE site to regulate TLR-4 expression" and "The promoter region of ABCA1 also has an LXRE site, which is strongly inhibited by TLR-4 signaling." Consequence: dysregulated **epidermal lipid transport** and **innate immune tone**. Independent confirmation of the MAS→LXR→ABCA1/ABCG1/LDLR axis comes from Gabitova et al. 2015 (**PMID:26344763**): "Loss of Nsdhl induced the expression of ATP-binding cassette (ABC) transporters ABCA1 and ABCG1, reduced the expression of low-density lipoprotein receptor (LDLR), decreased intracellular cholesterol, and was dependent on the liver X receptor (LXR) α."

- **Node 4A-ii (CELLULAR) — Cell-cycle activation / hyperproliferation.** "The S-G2-M to G0-G1 ratio in patient skin fibroblasts was 3-fold higher than in control cells" in cholesterol-restricted medium; "This ratio peaked after 2–3 days growth in the cholesterol-restricted medium and corresponded with peaks of cellular methylsterols and total protein." Pharmacologic phenocopy: the SMO inhibitor **ATZ** increased the ratio 3-fold in normal lymphoblasts, whereas **simvastatin and fluconazole did not** — establishing that it is *methylsterol accumulation*, not cholesterol deficiency, that drives proliferation (PMID:21285510). GO:0008284 positive regulation of cell population proliferation *(unverified)*.

- **Node 4A-iii (CELLULAR) — Impaired EGFR endosomal trafficking.** "SC4MOL is required for effective endosomal trafficking of EGFR." Silencing MSMO1 prevents EGFR association with **RAB11 recycling endosomes** and shifts it toward **RAB7 late endosomes**; patient fibroblasts show "diminished EGFR signaling" with reduced downstream **ERK phosphorylation** despite elevated EGFR phosphorylation (PMID:24144731). Corroborated in the cancer setting: "Bioinformatics modeling revealed an unexpected role for these genes in controlling EGFR signaling, trafficking, and degradation" and "Analysis of Nsdhl-deficient mice confirmed dramatic loss of internalized growth factor receptors in fibroblasts and reduced activation of EGFR signaling in NSDHL-lacking skin regions" (Sukhanova 2013, PMID:23125191).

**Arm B — Product deficiency**

**Node 3B (ORGANISM) — Reduced cholesterol availability.** Hypocholesterolemia (variable, ~50% of patients): total cholesterol 85–90 mg/dL, low HDL and LDL. Consequences relevant to affected organs: membrane raft composition (lens fiber cells, neurons), myelination, and **Sonic hedgehog** signaling (SHH requires cholesteroylation) — the last is the standard explanation for developmental malformation in cholesterol-synthesis defects, though it has **not been directly demonstrated in MSMO1 deficiency** (an explicit knowledge gap).

**Convergent downstream tissue phenotypes**

- **Skin (Node 5, TISSUE):** MAS-driven keratinocyte/fibroblast hyperproliferation + LXR-mediated barrier-lipid dysregulation + constitutive IL-6 → **psoriasiform epidermal hyperplasia and inflammation**. "Cultures of patient skin fibroblasts showed constitutive production of IL-6 compared with control fibroblasts"; after 24 h of simvastatin, "IL-6 production by patient fibroblasts was significantly decreased" (PMID:21285510) — the direct in-vitro rationale for statin therapy.
- **Immune system (Node 5, CELLULAR/ORGANISM):** see 6.4.
- **Lens (Node 5, TISSUE):** "the mechanism of early lens opacification is thought to result from impaired cholesterol synthesis, altering the lipid composition of the lens membrane" (Hassas 2026, PMID:41718295). The lens is uniquely vulnerable because it is **avascular and cannot import LDL cholesterol**, relying on local de novo synthesis — hence cataract in nearly every distal cholesterol-synthesis defect.
- **Brain (Node 5, ORGAN):** microcephaly, DD, white matter loss. The brain likewise depends on local cholesterol synthesis (blood–brain barrier excludes lipoprotein cholesterol), explaining why systemic cholesterol supplementation **does not rescue** neurologic features.
- **Skeleton (Node 5, TISSUE):** delayed skeletal maturation with normal morphology; zebrafish data implicate **hypertrophic chondrocyte patterning** (see §15).

### 6.4 Immune system involvement (detailed)

From He et al. 2011 (PMID:21285510), all human in vivo flow cytometry:

- **Granulocytes:** "activated CD16+ granulocytes (identified by CD25+CD69+ and CD86+HLA-DR+ subsets) were increased 30- and 20-fold in the patient and her father, respectively"; "30- and 15-fold increases in the numbers of TLR-2+TLR-4– granulocytes in the patient and her father"; "CD16b isoform was also markedly downregulated in both the patient and her father."
- **T cells:** "both patient and father had a significantly higher proportion of CD8dim T cells that were also CD28–CD56+" — a senescent/NK-like effector phenotype.
- **Monocytes:** "No significant differences were observed in the monocyte population."
- **Cytokines:** serum GM-CSF, IL-6, IL-8 increased; **TNF-α normal** — explaining etanercept failure.
- **Pharmacologic phenocopy in normal cells:** SMO inhibition with ATZ produced "a greater than 6-fold increase in the TLR-2+TLR-4– granulocyte population" and a "2-fold decrease in CD8 expression" — establishing causality rather than mere association.

This is a **sterol-driven innate-immune reprogramming** phenotype (TLR-2 high / TLR-4 low), which is notable because the TLR-2^high^ granulocyte pattern is "typical of psoriasis patients" (PMID:24144731) — providing a mechanistic bridge from a rare metabolic disease to common inflammatory skin disease.

### 6.5 Link to common disease — PSORS9

> "SC4MOL is situated within the psoriasis susceptibility locus PSORS9, and may be a genetic risk factor for common skin conditions." — He et al. 2014 (PMID:24144731)

PSORS9 (OMIM 607857) maps to 4q31–4q32, encompassing *MSMO1* at 4q32.3. Note that the historically favored PSORS9 candidate in Han Chinese linkage studies has been *IL15* at 4q31.2; the MSMO1 candidacy remains a **hypothesis** (appropriate for a `mechanistic_hypotheses` entry with `status: EMERGING`, not an asserted mechanism).

### 6.6 Oncologic mechanism (adjacent, for completeness)

- **MSMO1/NSDHL inactivation sensitizes tumors to EGFR inhibitors:** "We established that inactivation of 2 sterol biosynthesis pathway genes, SC4MOL and NSDHL, sensitized tumor cells to EGFR inhibitors. ... SC4MOL inactivation sensitized A431 xenografts to cetuximab." (PMID:23125191)
- **LXR-dependent anti-tumor effect:** "Inhibition of SC4MOL or NSDHL, or activation of LXRα by sterol metabolites, can be an effective strategy against carcinomas with activated EGFR-KRAS signaling." (PMID:26344763)
- **Chemoresistance (2026):** MSMO1 modulates breast-cancer sensitivity to paclitaxel, carboplatin, and epirubicin by tuning its substrate T-MAS, which regulates ER stress and apoptosis via the **PERK/eIF2α/ATF4/CHOP** axis; plasma exosomal MSMO1 proposed as a predictive biomarker (iScience, Jan 2026, ScienceDirect PII S2589004226001653). **PMID not confirmed — verify before citing.**
- MSMO1 upregulation associates with poor survival in **cervical cancer** (PMC11543037).

### 6.7 Molecular profiling in patients

- **Transcriptomics:** no patient-derived RNA-seq study published. **Not available.**
- **Proteomics:** none. **Not available.**
- **Metabolomics/sterolomics:** this *is* the diagnostic modality — GC/MS sterol profiling of plasma, fibroblasts, and skin scales (see §10). This is the richest omics layer for the disease.
- **Lipidomics:** the skin-scale sterol data constitute a targeted lipidomic finding (preferential dimethylsterol deposition in cutaneous tissue), but no untargeted lipidomics has been reported.
- **Single-cell / spatial transcriptomics:** none. **Not available.**
- **Functional genomics screens:** *MSMO1* appears in CRISPR/RNAi screens as an EGFR-inhibitor sensitizer (Sukhanova 2013, PMID:23125191). DepMap data exist at the cell-line level but have not been analyzed in a disease context.

### 6.8 Ontology term suggestions for pathophysiology nodes

**GO biological processes / molecular functions:**
| GO ID | Label | Verification |
|---|---|---|
| **GO:0000254** | C-4 methylsterol oxidase activity | ✓ OLS-verified |
| **GO:0006695** | cholesterol biosynthetic process | ✓ OLS-verified |
| GO:0016126 | sterol biosynthetic process | unverified |
| GO:0008203 | cholesterol metabolic process | unverified |
| GO:0005506 | iron ion binding | unverified |
| GO:0008284 | positive regulation of cell population proliferation | unverified |
| GO:0032456 | endocytic recycling | unverified |
| GO:0007173 | epidermal growth factor receptor signaling pathway | unverified |
| GO:0006954 | inflammatory response | unverified |
| GO:0002224 | toll-like receptor signaling pathway | unverified |

**GO cellular components:** GO:0005789 endoplasmic reticulum membrane; GO:0055037 recycling endosome; GO:0005770 late endosome *(all unverified — confirm with OAK)*.

**CL cell types:**
| CL ID | Label | Verification |
|---|---|---|
| **CL:0011004** | lens fiber cell | ✓ OLS-verified |
| **CL:0002224** | lens epithelial cell | ✓ OLS-verified |
| CL:0000312 | keratinocyte | unverified |
| CL:0000057 | fibroblast | unverified |
| CL:0000775 | neutrophil | unverified |
| CL:0000625 | CD8-positive, alpha-beta T cell | unverified |
| CL:0000138 | chondrocyte (hypertrophic: CL:0000743) | unverified |

**UBERON anatomical sites:** UBERON:0002097 skin of body; UBERON:0000965 lens of camera-type eye; UBERON:0000955 brain; UBERON:0002107 liver; UBERON:0000473 testis; UBERON:0000992 ovary; UBERON:0002481 bone tissue *(all unverified — confirm with OAK)*.

---

## 7. Anatomical Structures Affected

### Organ level

**Primary organs (directly affected):**
- **Skin** (UBERON:0002097) — psoriasiform dermatitis, ichthyosis, erythroderma, alopecia; the tissue with the highest measured dimethylsterol accumulation.
- **Lens of the eye** (UBERON:0000965) — bilateral congenital/infantile cataract.
- **Brain** (UBERON:0000955) — microcephaly, cerebral white matter volume reduction with T2-FLAIR hyperintensity (Hassas 2026).
- **Eyelid / ocular adnexa** — blepharitis.

**Secondary / systemic involvement:**
- **Immune system** — granulocyte and T-cell dysregulation (bone marrow–derived, systemically distributed).
- **Skeletal system** — delayed skeletal maturation with normal bone morphology; genu valgum; polydactyly (developmental, therefore arguably primary).
- **Joints** — arthralgia; joint contractures (lower extremities, He 2014 patient 2).
- **Endocrine / reproductive** — delayed puberty. Note: MAS are physiologically concentrated in **testis and ovary** (PMID:21285510), so gonadal involvement is mechanistically expected, but **no fertility or gonadal-histology data exist in patients** — a notable knowledge gap.
- **Liver** — the highest-expressing tissue for MSMO1 (RPKM 94.8); no hepatic phenotype has been reported, which is itself mechanistically interesting.

**Body systems:** integumentary, nervous, visual/special sense, immune/hematologic, musculoskeletal, endocrine.

### Tissue and cell level

- **Epidermis / stratum corneum** — hyperproliferative keratinocytes (CL:0000312); scale contains the highest dimethylsterol.
- **Dermal fibroblasts** (CL:0000057) — the primary patient-derived experimental cell type; show elevated methylsterols, 3-fold increased S-G2-M/G0-G1 ratio, constitutive IL-6.
- **Lens fiber cells** (CL:0011004 ✓) and **lens epithelial cells** (CL:0002224 ✓) — opacification.
- **Granulocytes/neutrophils** (CL:0000775) — CD16+, activated (CD25+CD69+, CD86+HLA-DR+), TLR-2^+^TLR-4^−^, CD16b down.
- **CD8 T cells** (CL:0000625) — CD8^dim^CD28^−^CD56^+^ subset expanded.
- **B cells** (CL:0000236) — He 2014 states immunologic analyses covered "granulocytes and B cells" and indicated "dysregulation of immune-related receptors"; specific B-cell findings not detailed in the accessible text.
- **Monocytes** — explicitly **unaffected** ("No significant differences were observed in the monocyte population").
- **Pre-hypertrophic / hypertrophic chondrocytes** — the cell type identified by the zebrafish model (see §15).

### Subcellular level

- **Endoplasmic reticulum membrane** (GO:0005789) — the site of MSMO1 catalysis; "localized to the endoplasmic reticulum membrane" with three TM helices.
- **Recycling endosome (RAB11+)** and **late endosome (RAB7+)** — the trafficking compartments whose EGFR partitioning is disrupted.
- **Plasma membrane / lipid rafts** — the downstream target of altered sterol composition (lens fiber membranes, immune receptor platforms).

### Localization and lateralization

- Cataract: **bilateral** in all reported cases.
- Dermatitis: **generalized/diffuse**, characteristically **sparing the palms** in the index patient ("affecting the entire body except palms"); umbilical onset with centrifugal spread. Perianal-limited in the mild case; scalp-limited (dandruff) in Frisso's patient.
- Note the contrast with **CHILD syndrome** (NSDHL, the adjacent enzyme in the same complex), which is characteristically **strikingly unilateral/lateralized** due to X-inactivation mosaicism. MSMO1 deficiency is autosomal and therefore **symmetric/generalized** — a clinically useful discriminator.

---

## 8. Temporal Development

### Onset

- **Congenital:** cataract (present at birth or detected in the first months), microcephaly, polydactyly.
- **Infantile (1–23 months, per GARD):** growth failure, developmental delay, early-onset dermatitis in the severe cases.
- **Early childhood:** dermatitis in the index patient began at **age 2** at the umbilicus and generalized by **age 6**.
- **Onset pattern:** **insidious/chronic**, not acute. There is **no metabolic decompensation phenotype** — this disorder does **not** conform to the `metabolic_intoxication_decompensation` module. No crises, no catabolic triggers, no acute encephalopathy.
- HPO clinical-course annotation: **HP:0011463 Childhood onset** (from PMID:21285510) — but this reflects the dermatitis onset in the index case and understates the congenital ocular/head-size features.

### Progression

- **Neurologic:** **static** developmental impairment. No documented neurodegeneration. Spasticity may worsen with growth (as in cerebral palsy–like static encephalopathy).
- **Ocular:** cataract is **progressive** until surgically removed; **irreversible**.
- **Dermatologic:** **chronic relapsing–remitting** with seasonal (winter) and stress-related flares; the index patient's skin "once almost completely normalized."
- **Growth:** progressive falling away from centiles through childhood; delayed skeletal maturation and delayed puberty imply a prolonged growth window.
- **Overall course:** **chronic, lifelong**, non-lethal in reported cases. Reported patients have survived into the third decade (index patient was 20 at the 2014 report; the Italian patient was 19).
- **Disease staging:** no formal staging system exists. **Not available.**

### Patterns

- **Remission:** dermatologic remission is **treatment-induced** (cholesterol/statin) and, less durably, spontaneous. Metabolic remission (normalized methylsterols) is achievable with combined oral cholesterol + statin + bile acid (PMID:24144731). **Neurologic and ocular deficits do not remit.**
- **Critical periods — the central prognostic issue:**
  - The **prenatal/perinatal window** determines microcephaly and lens clarity. Both are essentially fixed before diagnosis is currently made. This is why the disorder is "**potentially partially treatable**" (PMID:37195326) rather than treatable.
  - The **postnatal window** governs dermatitis, immune dysregulation, growth, and — suggestively — some developmental gain. Morales 2022 reported "Marked language improvements within 6 months of treatment initiation," and Tkemaladze 2023 reported treatment "resulted in a marked improvement of psoriasiform dermatitis and some hair growth."
  - **Implication for prevention/screening:** any meaningful reduction in the neuro-ophthalmic burden requires pre-symptomatic (newborn or prenatal) identification — currently not performed anywhere.

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence:** **<1 / 1,000,000** — Orphanet-class `BELOW_1_IN_1000000`; realistically "not yet documented." With ~11 individuals ever reported worldwide, the observed prevalence is on the order of 10⁻⁹. Recommended structured curation:
  - `measure_type: POINT_PREVALENCE`, `prevalence_class: BELOW_1_IN_1000000` (or `NOT_YET_DOCUMENTED`), `population: Worldwide`
  - Plus a `measure_type: CASES_IN_LITERATURE` record with `notes` recording the count.
- **Incidence:** **not available.**
- **Case count discrepancy — flag this.** Published tallies conflict: He 2014 reported "four patients from three different families"; Kalay Yildizhan 2020 stated "5 patients from 4 unrelated families ... reported to date"; Tkemaladze 2023 stated "only five cases reported to date" — which appears to **undercount**, since He (4) + Frisso (1) + Kalay Yildizhan (2) + Morales (1) = 8 before their own 2 siblings. My reconstruction from primary sources is **~11 individuals across ~9 families**. Curate the count with an explicit caveat rather than repeating any single paper's figure.

### Inheritance

- **Pattern: Autosomal recessive** (HP:0000007). Annotated to OMIM:616834 from PMID:21285510. Both compound heterozygous and homozygous states are documented, with confirmed parental segregation in multiple families ("The 519T→A mutation was carried by the patient's father, and the 731A→G mutation was present in the mother"; "Segregation analysis in all available family members confirmed recessive inheritance of the mutation," PMID:33161406).
- **Not digenic/oligogenic.** No multi-locus inheritance has been reported.
- **Penetrance:** appears **complete** in biallelic individuals, though with only ~11 cases this is weakly established.
- **Expressivity: markedly variable** — the single most important genetic-counseling point. The same disorder spans severe non-ambulatory spastic quadriplegia with erythroderma to a boy with normal head circumference, ASD, and transient perianal dermatitis described as "the mildest case of SC4MOL deficiency to date" (Morales 2022). Even **within a genotype**: c.343G>A homozygotes include He's patient 2 (no psoriasiform rash) and Hassas's patient (spastic quadriplegia, no dermatitis) — arguing for genotype-independent modifiers.
- **Genetic anticipation:** **not applicable** (no repeat expansion).
- **Germline mosaicism:** **not reported.**
- **Founder effects:** none established. Two recurrent alleles (p.Tyr244Cys ×3 families; p.Gly115Arg ×2 families) warrant haplotype investigation but have **not** been shown to be founder alleles.
- **Consanguinity:** a clear contributor. Homozygosity in consanguineous **Turkish** and **Georgian** families; the Georgian family's variant was found by WES in a consanguineous pedigree.
- **Carrier frequency:** **not available.** Not on any carrier-screening panel; no gnomAD-derived estimate published. Given that all known pathogenic alleles are private/near-private missense variants, a reliable carrier-frequency estimate cannot currently be computed.
- **Heterozygote biochemical phenotype:** carriers have mildly elevated plasma methylsterols and (in one father) markedly abnormal granulocyte activation markers — clinically silent but a research-relevant intermediate phenotype.

### Population demographics

- **Reported ancestries:** United States (index family, ancestry not specified), Hispanic, Italian, Turkish (consanguineous), Georgian (consanguineous), plus two additional US families. **No ethnic predilection has been established** — the distribution most likely reflects ascertainment (specialist metabolic centers, WES availability, consanguinity).
- **Geographic distribution:** cases reported from North America, Western Europe (Italy), and Western Asia/Caucasus (Turkey, Georgia). No endemic region.
- **Geographic distribution of specific variants:** p.Tyr244Cys reported in US and Italian families; p.Asn27Thr in Turkey; p.Glu183Ala in Georgia. Too few observations to establish geographic clustering.
- **Sex ratio:** both sexes affected, consistent with autosomal recessive inheritance. Reported individuals include at least 4 females and at least 4 males. **No sex bias; ratio effectively 1:1** but the sample is far too small to state formally.
- **Age distribution:** all reported individuals identified in childhood or adolescence, with the oldest reported at ~20 years. **No adult-diagnosed or elderly patients reported** — reflecting the era of WES availability rather than mortality.

---

## 10. Diagnostics

### 10.1 Laboratory / biochemical testing — the diagnostic cornerstone

**Plasma sterol profiling by GC/MS** is the definitive biochemical test and the single most important diagnostic recommendation for this disease.

- **Diagnostic signature:** marked elevation of **4α-monomethylsterols (~20-fold)** and **4,4′-dimethylsterols (~500-fold)**, with **normal proximal cholesterol precursors**. Morales 2022 explicitly noted "Normal proximal cholesterol precursors," which localizes the block distally.
- **Total cholesterol may be low OR normal** — it is *not* a screening test.
- Standard lipid panel in the index patient: TC 85 mg/dL (nl 140–176), HDL 28 (nl 35–75), LDL 49 (nl 70–160), TG 84 (nl 50–200).
- **Alternative sample types:** cultured **skin fibroblasts** (methylsterols "markedly elevated in the patient's fibroblasts, but not any of the controls") and **skin scales** (where dimethylsterol accumulation is greatest). Skin-scale sterol analysis is a nearly disease-specific, non-invasive test that deserves wider use.
- LOINC: no dedicated LOINC codes exist for 4-monomethylsterol or 4,4-dimethylsterol quantification. **Not available** — sterol profiling is reported as a specialty-lab panel.

Frisso et al. 2017 make the explicit clinical recommendation:
> "we suggest that these two analyses should be performed as soon as possible in all undiagnosed patients affected by bilateral cataracts and developmental delay." (PMID:28673550)

### 10.2 Biomarkers

- **Diagnostic biomarkers:** plasma/fibroblast/skin-scale 4α-monomethylsterols and 4,4′-dimethylsterols (T-MAS, FF-MAS).
- **Treatment-response biomarker:** serial plasma methylsterol concentration — used in every treated case to titrate therapy. Morales 2022 tracked methylsterols longitudinally, observing an initial fall on statin and later "upward trend" prompting dose escalation.
- **Inflammatory biomarkers:** serum GM-CSF, IL-6, IL-8 elevated; **TNF-α normal** — the normal TNF-α is a useful negative predictor for anti-TNF therapy.
- **Immunophenotyping biomarkers (research):** CD16+CD25+CD69+ and CD86+HLA-DR+ granulocyte fractions; TLR-2^+^TLR-4^−^ granulocytes; CD16b expression; CD8^dim^CD28^−^CD56^+^ T cells.
- No FDA-qualified biomarker exists for this disease.

### 10.3 Imaging

- **Brain MRI:** recommended. Findings reported: "diffuse white matter volume reduction, T2 FLAIR hyperintensity" (Hassas 2026, PMID:41718295). Not specific; used to characterize the neurologic phenotype and exclude alternatives.
- **Ocular examination / slit lamp / B-scan:** essential for cataract characterization. Described morphology: "diffuse cataracts bilaterally with scattered, white fleck-like opacities in the anterior lens," "intumescent appearance with significant lenticular liquefaction."
- **Skeletal survey / bone age:** documents **delayed skeletal maturation with normal bone morphology** (PMID:21285510) — the normal morphology is diagnostically informative because it distinguishes MSMO1 deficiency from the chondrodysplasia-punctata group (CDPX2, CHILD, HEM/Greenberg), where stippled epiphyses are characteristic.
- No disease-specific imaging biomarker.

### 10.4 Functional tests and electrophysiology

- **Not established.** No pulmonary, cardiac, EEG, EMG, ECG, or NCS abnormality is characteristic. VEP/ERG may be used in the ophthalmologic workup of infantile cataract but is not disease-specific. **Not applicable / not available.**

### 10.5 Biopsy and histopathology

- **Skin biopsy** shows psoriasiform epidermal hyperplasia (consistent with the clinical descriptor "psoriasiform dermatitis"); it is **non-diagnostic** — the histology mimics true psoriasis, which is exactly why the disorder is misdiagnosed. Detailed histopathologic and immunohistochemical characterization has **not** been systematically published. **Largely not available** — a genuine curation gap.
- No other tissue biopsy plays a diagnostic role.

### 10.6 Genetic testing

**Recommended approach:** the diagnosis is now most often made by **exome or genome sequencing**, with confirmatory sterol profiling; the reverse order (biochemical first, gene second) was used in the earlier cases.

| Modality | Utility for MSMO1 deficiency |
|---|---|
| **Whole exome sequencing (WES)** | **High — the current first-line modality.** Diagnostic in Kalay Yildizhan 2020 ("We undertook whole-exome sequencing and identified a new homozygous missense mutation") and Tkemaladze 2023 ("Whole-exome sequencing revealed a novel, homozygous c.548A>C, p.(Glu183Ala) variant"). Because all known variants are missense in coding exons, WES coverage is excellent. |
| **Whole genome sequencing (WGS)** | Useful; adds little over WES for this gene given the coding-missense spectrum, but would capture regulatory variants — note the zebrafish *kolibernu7* allele is a **cis-regulatory** mutation abolishing tissue-specific expression, raising the possibility of undiscovered human regulatory alleles missed by WES. |
| **Gene panels** | *MSMO1* is included on **cholesterol/sterol biosynthesis disorder panels**, **congenital cataract panels**, and **ichthyosis/inherited skin disorder panels**. Panel testing is appropriate when the biochemical phenotype is already known. Available tests are registered in GTR under gene 6307. |
| **Single-gene testing** | Appropriate only after a diagnostic sterol profile, or for **cascade/carrier testing** of relatives once the familial variants are known. |
| **Chromosomal microarray** | **Not indicated** — no CNV etiology reported. |
| **Karyotype / FISH** | **Not indicated.** |
| **Mitochondrial DNA testing** | **Not applicable.** |
| **Repeat expansion testing** | **Not applicable.** |

**Key interpretive challenge:** most *MSMO1* missense variants are initially reported as **VUS**. Reclassification depends on (i) sterol profiling as a functional assay, (ii) in-silico support (AlphaMissense), and (iii) homozygosity in additional affected individuals — exactly the PP3_Strong + PM3 + PM2_Supporting pathway used by Hassas 2026. **Biochemical testing is therefore not merely confirmatory; it is the practical route to variant classification for this gene.**

### 10.7 Omics-based diagnostics

- **Metabolomics/sterolomics:** the primary diagnostic omics layer (see 10.1). GC/MS.
- **RNA sequencing:** not established diagnostically; could in principle detect a regulatory/expression-null allele.
- **Proteomics, epigenomics, liquid biopsy:** **not applicable / not available** for diagnosis.

### 10.8 Clinical criteria and differential diagnosis

There are **no formal consensus diagnostic criteria** (no society guideline, no DSM/ICD-based criteria). Diagnosis rests on: compatible phenotype + diagnostic sterol profile + biallelic *MSMO1* variants.

**Differential diagnosis — post-squalene cholesterol biosynthesis disorders (discriminated by sterol profile):**

| Disorder | Gene | Accumulating sterol | Distinguishing features |
|---|---|---|---|
| **MSMO1 deficiency (MCCPD)** | *MSMO1* | **4α-methyl- and 4,4-dimethylsterols (T-MAS/FF-MAS)** | Microcephaly + congenital cataract + **symmetric** psoriasiform dermatitis; normal bone morphology |
| Smith–Lemli–Opitz syndrome | *DHCR7* | 7-dehydrocholesterol | 2-3 toe syndactyly, genital anomalies, characteristic facies |
| Desmosterolosis | *DHCR24* | desmosterol | Nonspecific; "difficult to suspect clinically" |
| Lathosterolosis | *SC5D* | lathosterol | SLOS-like; liver disease |
| **CHILD syndrome** | *NSDHL* (**same C4-demethylation complex**) | 4-methylsterols | **X-linked dominant, strikingly unilateral/lateralized** ichthyosiform nevus + ipsilateral limb defects |
| CK syndrome | *NSDHL* | — | X-linked recessive; ID, seizures, cortical malformation |
| **CDPX2** (Conradi–Hünermann–Happle) | *EBP* | 8(9)-cholestenol, 8-dehydrocholesterol | X-linked dominant; **chondrodysplasia punctata**, Blaschkoid ichthyosis, cataract |
| HEM / Greenberg dysplasia | *LBR* | cholesta-8,14-dien-3β-ol | Lethal; hydrops, "moth-eaten" skeletal dysplasia |
| Antley–Bixler / POR deficiency | *POR* | lanosterol, dihydrolanosterol | Craniosynostosis, disordered steroidogenesis |

**Non-metabolic differentials to exclude:** true psoriasis/psoriasis vulgaris (the most common misdiagnosis — the index patient failed steroids, calcipotriene, cyclosporine, etanercept, phototherapy, and isotretinoin before diagnosis); congenital ichthyoses; other syndromic congenital cataract (e.g., Lowe, galactosemia, peroxisomal disorders); other syndromic microcephaly with ID.

**A useful clinical rule derived from this literature:** *psoriasiform dermatitis refractory to conventional psoriasis therapy, in a child with congenital cataract and/or microcephaly, should prompt plasma sterol profiling.*

### 10.9 Screening

- **Newborn screening:** MSMO1 deficiency is **not** on any newborn screening panel anywhere (not on the US RUSP). Standard MS/MS acylcarnitine/amino-acid NBS **would not detect it** — detection would require sterol-specific methodology. Given the treatability of the cutaneous/immune/growth arm and the fixed nature of the neuro-ocular arm, this is a legitimate (though currently impractical) NBS candidate discussion point.
- **Carrier screening:** *MSMO1* is **not** on expanded carrier screening panels.
- **Cascade screening:** appropriate for at-risk siblings once familial variants are known — and is arguably time-critical, since presymptomatic treatment is the only route to preventing the cutaneous/growth phenotype.

---

## 11. Outcome / Prognosis

> **Global caveat:** there is **no natural history study, registry, or survival analysis** for MSMO1 deficiency. Everything below is inferred from ≤11 individually reported patients. Any quantitative prognostic statement should be curated as low-confidence.

### Survival and mortality

- **Survival rate (5-/10-year/overall):** **not available.** No deaths have been reported among published patients.
- **Life expectancy:** **not established**, but the disorder is **not known to be life-limiting**. Patients have been reported alive at 19 and 20 years. Contrast with the lethal end of the cholesterol-synthesis spectrum (HEM/Greenberg, severe SLOS).
- **Mortality rate / disease-specific mortality:** **not available.**
- The zebrafish and mouse data (§15) show that **complete** Msmo1 loss is lethal, implying that human survivors necessarily carry hypomorphic alleles with residual activity — a true human null may be embryonic-lethal and therefore unascertained. This is an important, curatable inference.

### Morbidity and function

- **Dominant sources of morbidity:** (1) **visual impairment** from bilateral cataract — permanent, sometimes profound ("perception to light" post-surgery in Hassas 2026); (2) **intellectual disability / developmental delay** — ranging from mild to severe with non-ambulatory spastic quadriplegia; (3) **chronic disfiguring, pruritic dermatitis**; (4) **short stature and delayed puberty**.
- **Disability outcomes:** the severe end entails lifelong total care dependency (non-verbal, non-ambulatory). The mild end is compatible with mainstream functioning with ASD-related support needs.
- **Quality of life measures:** **no EQ-5D, SF-36, PROMIS, DLQI, or disease-specific instrument has ever been applied.** Complete evidence gap.

### Disease course and complications

- **Complications:** post-cataract-surgery complications (aphakia/pseudophakia management, amblyopia, nystagmus); joint contractures; growth failure; refractory dermatitis with barrier compromise; potential infection susceptibility from immune dysregulation (theoretical).
- **Recovery potential — the key prognostic distinction:**
  - **Reversible/improvable with treatment:** psoriasiform dermatitis (marked improvement), plasma methylsterol levels (normalizable), immune dysregulation ("partially corrected with cholesterol and statin supplements," per OMIM/MedGen), growth, hair growth, and — suggestively — **language/developmental gains** ("Marked language improvements within 6 months of treatment initiation," Morales 2022).
  - **Irreversible:** congenital cataract (structural, requires surgery), microcephaly, established structural brain changes, and fixed neurodevelopmental deficit.
  - The framing in the title of Tkemaladze 2023 — "**a potentially partially treatable, ultrarare neurodevelopmental disorder**" — is the most accurate one-line prognostic statement available and is worth quoting directly in the KB.

### Prognostic factors

Inferred, **not statistically established**:
- **Age at diagnosis and treatment initiation** — the strongest presumed determinant, given the critical-period argument.
- **Presence and severity of microcephaly** — the mildest reported patient had a **normal head circumference**; the most severe had microcephaly with spastic quadriplegia. Head circumference appears to track with neurodevelopmental outcome.
- **Residual enzyme activity** (inferred from methylsterol elevation magnitude) — plausible but untested.
- **Treatment responsiveness of plasma methylsterols** — biochemical response has tracked with cutaneous response in every treated case.
- **Genotype:** poor predictor. The same c.343G>A homozygous genotype produced markedly different phenotypes in two patients.

**Prognostic biomarkers:** none validated. Serial plasma methylsterol is the only candidate.

---

## 12. Treatment

### 12.1 Overall strategy — pathogenesis-based dual therapy

The therapeutic logic is the standard "**substrate reduction + product replacement**" model used across distal cholesterol-synthesis defects, delivered both systemically and topically:

1. **Cholesterol supplementation** — replaces the deficient product, and via feedback suppresses SREBP-driven flux into the blocked step.
2. **HMG-CoA reductase inhibition (statin)** — reduces flux into the pathway upstream of the block, lowering methylsterol accumulation. This is the *substrate-reduction* arm and is what distinguishes therapy here from simple cholesterol replacement (statins are conventionally counterintuitive in a hypocholesterolemic patient).
3. **Bile acid supplementation** — a third flux-modulating component used in the reported regimen.
4. **Topical cholesterol/statin ointment** — targets the skin directly, where dimethylsterol accumulation is greatest and where systemic delivery is least effective. Directly borrowed from the well-established CHILD syndrome protocol (topical **2% lovastatin/simvastatin + 2% cholesterol**), which is the mechanistic sibling disorder (*NSDHL*, same C4-demethylation complex).

### 12.2 Published regimens and outcomes

**He et al. 2011 — cholesterol monotherapy (index patient, 3 months):**
> "methylsterol level decreased by about 20%, and the plasma cholesterol level was much improved, reaching a level near the low end of the normal range, but the methylsterol level decreased no further with longer treatment" (PMID:21285510)

→ **Conclusion: cholesterol alone is insufficient.**

**He et al. 2014 — the reference combination algorithm:**
> Cholesterol supplementation **100 mg/kg/day** alone reduced methylsterol levels ~20%; addition of "oral statin (**10 mg/day**) plus bile acids (**30 mg/kg/day**) along with cholesterol **normalized**" methylsterol levels. (PMID:24144731)

→ This is the "previously published treatment algorithm" that later authors follow.

**Kalay Yildizhan et al. 2020 (Turkish siblings):**
> "The siblings were treated with a combination of oral and topical statin and cholesterol which resulted in clinical improvement. This study demonstrates how genomics-based diagnosis and therapy can be helpful in clinical practice." (PMID:33161406) *(Exact doses are behind a paywall and could not be verified — do not assert specific doses from this paper.)*

**Morales, Curry & Enns 2022 (mildest case):**
- **Simvastatin** 0.3 mg/kg/day, escalated to 10 mg/day
- **Pravastatin** 4 mg/day added at age 6.4 years
- **Coenzyme Q10** 50 mg/day (standard statin adjunct)
- Topical **cholesterol/simvastatin** combination for perianal dermatitis
- Outcomes: marked language improvement within 6 months; perianal dermatitis resolved; **mild myalgia the only adverse effect**
- Note: statin therapy was used **despite normal total cholesterol** — because the target is methylsterol reduction, not cholesterol lowering.

**Tkemaladze et al. 2023 (Georgian siblings):**
> "Based on previously published treatment algorithms, we initiated a modified dosage regime with systemic cholesterol supplementation, statins and bile acid along with topical application of a cholesterol/statin formulation. This resulted in a marked improvement of psoriasiform dermatitis and some hair growth." (PMID:37195326)

### 12.3 Treatments that FAILED (important negative evidence)

In the index patient, all of the following were tried without durable benefit (PMID:21285510):
- Topical corticosteroids
- Calcipotriene
- **Cyclosporine A** — "her skin briefly improved with cyclosporine A, she did not exhibit a long-term response"
- **Etanercept** (TNF-α inhibitor) — ineffective, consistent with the patient's **normal serum TNF-α**
- Phototherapy
- Oral isotretinoin

→ **Curatable clinical rule:** conventional psoriasis therapy fails; anti-TNF biologics are mechanistically inappropriate here (normal TNF-α; the driver is IL-6/GM-CSF/IL-8 with MAS-driven hyperproliferation).

### 12.4 Supportive, surgical, and rehabilitative care

- **Cataract surgery:** lensectomy ± anterior vitrectomy with intraocular lens implantation. Performed at 7 months (Morales 2022) and in Hassas 2026 ("The patient underwent lensectomy and anterior vitrectomy with intraocular lens implantation"). Early surgery is the standard of care for bilateral infantile cataract to prevent deprivation amblyopia.
- **Low-vision rehabilitation**, refractive correction/aphakia management, amblyopia therapy.
- **Developmental therapies:** physical, occupational, and speech therapy; special education.
- **Spasticity management:** as for static encephalopathy (PT, orthotics, tone management) — no disease-specific protocol.
- **Nutritional support** for failure to thrive.
- **Dermatologic supportive care:** emollients, barrier repair.
- **Genetic counseling** for the family (25% recurrence risk; prenatal/PGT options).

### 12.5 Advanced therapeutics

- **Gene therapy, gene editing, cell therapy, RNA therapies (ASO/siRNA/mRNA), targeted therapy, immunotherapy:** **none exist, none in development, no preclinical program identified.** Complete gap.
- Note conceptually: MSMO1 deficiency is a **loss-of-function enzymopathy in a small, ubiquitously expressed ER protein** — nominally a good AAV gene-replacement or mRNA-therapy candidate — but the key affected tissues (brain, lens) are affected prenatally, which limits postnatal benefit. No published program.

### 12.6 Clinical trials

**No clinical trial of any kind has ever been registered for MSMO1 deficiency / SC4MOL deficiency / MCCPD** on ClinicalTrials.gov. All treatment evidence is uncontrolled single-patient/sibship experience (n≤2 per report). **No NCT identifier is available to cite.**

### 12.7 Pharmacogenomics

- No disease-specific PGx. However, because statins are the backbone of therapy, standard statin PGx applies: **CPIC guideline for *SLCO1B1* (and *ABCG2*, *CYP2C9*) and statin-associated musculoskeletal symptoms**. *SLCO1B1* decreased-function alleles (c.521T>C, rs4149056) increase simvastatin myopathy risk — directly relevant since myalgia was the only reported adverse effect (Morales 2022). *SLCO1B1* genotyping is a reasonable, evidence-supported adjunct for patients on long-term simvastatin.
- No PharmGKB/CPIC record exists for *MSMO1* itself (ClinGen: "CPIC/PharmGKB Records: 0 / 0").

### 12.8 Adverse events

- **Statins:** myalgia (reported), rhabdomyolysis (theoretical), transaminitis; requires CK/LFT monitoring, especially in a growing child on long-term therapy for a non-cardiovascular indication.
- **Oral cholesterol:** generally well tolerated; GI upset.
- **Bile acids:** diarrhea, hepatotoxicity at high dose.
- **Topical statin/cholesterol:** well tolerated in the CHILD-syndrome literature; minimal systemic absorption.
- No FAERS signal specific to this indication (off-label, ultra-rare).

### 12.9 NCIT term suggestions for treatments

> All NCIT IDs below are **suggestions requiring OAK verification** (`uv run runoak -i sqlite:obo:ncit info <ID>`) before entry, per the dismech anti-hallucination SOP.

| Treatment | `treatment_term` (NCIT action) | `therapeutic_agent` | `therapeutic_modality` |
|---|---|---|---|
| Oral cholesterol supplementation | NCIT:C15433 Nutritional Support *or* NCIT:C15986 Pharmacotherapy | CHEBI:16113 cholesterol ✓ | `SMALL_MOLECULE` (**not** BEHAVIORAL — see the CLAUDE.md guardrail on NCIT:C15433) |
| Oral simvastatin | NCIT:C15986 Pharmacotherapy | CHEBI:9150 simvastatin *(verify)* | `SMALL_MOLECULE` |
| Oral pravastatin | NCIT:C15986 Pharmacotherapy | CHEBI:63618 pravastatin *(verify)* | `SMALL_MOLECULE` |
| Bile acid supplementation | NCIT:C15986 Pharmacotherapy | CHEBI:16359 chenodeoxycholic acid / CHEBI:9907 ursodeoxycholic acid *(the specific bile acid is not stated in PMID:24144731 — do not over-specify)* | `SMALL_MOLECULE` |
| Topical cholesterol/statin ointment | NCIT:C15986 Pharmacotherapy | cholesterol + lovastatin/simvastatin | `SMALL_MOLECULE` |
| Coenzyme Q10 | NCIT:C15433 Nutritional Support | CHEBI:46245 ubiquinone-10 *(verify)* | `SMALL_MOLECULE` |
| Cataract extraction (lensectomy + IOL) | NCIT:C15329 Surgical Procedure *(or a cataract-specific NCIT procedure term if one exists)* | — | `SURGERY` |
| Physical therapy | NCIT:C15302 Physical Therapy | — | `BEHAVIORAL` |
| Speech therapy | NCIT:C159273 Speech Therapy | — | `BEHAVIORAL` |
| Occupational therapy | NCIT:C121351 Occupational Therapy | — | `BEHAVIORAL` |
| Genetic counseling | NCIT:C15240 Genetic Counseling | — | *(omit — not platform-classifiable)* |
| Low-vision rehabilitation | NCIT:C15315 Rehabilitation | — | `BEHAVIORAL` |

**`target_mechanisms` pattern (recommended):**
- Statin → `INHIBITS` the "Methylsterol/MAS Accumulation" node (reduces upstream flux into the block).
- Oral/topical cholesterol → `ACTIVATES`/replaces at the "Reduced Cholesterol Availability" node.

This makes MSMO1 deficiency a clean worked example of the **substrate-reduction + product-replacement** drug pattern in a mechanism-module sense.

---

## 13. Prevention

### Primary prevention

**Not possible** for an affected fetus — the disease is fully determined at conception. Primary prevention operates only at the **reproductive** level:
- **Genetic counseling** with 25% recurrence risk per pregnancy for carrier couples.
- **Preimplantation genetic testing (PGT-M)** once familial variants are known.
- **Prenatal diagnosis** by CVS/amniocentesis molecular testing. *In principle*, amniotic-fluid sterol profiling could also be diagnostic (as it is for SLOS), but **prenatal sterol diagnosis has never been reported for MSMO1 deficiency** — this is an untested but plausible approach worth flagging as a knowledge gap.
- **Consanguinity counseling** in populations where it is common — the two homozygous-variant families were consanguineous.
- No vaccination, no risk-factor modification, no environmental intervention is applicable.

### Secondary prevention (early detection)

This is where the largest **unrealized** opportunity lies:
- **Newborn screening: not currently performed anywhere and not detectable by standard MS/MS panels.** Detection would require sterol-specific methodology.
- **Targeted diagnostic screening** is the practical substitute, and Frisso et al. 2017's recommendation is the actionable one: perform **plasma sterol profiling + *MSMO1* sequencing** in every undiagnosed child with **bilateral congenital/infantile cataract + developmental delay**. Given that congenital cataract has a well-defined incidence (~1–6/10,000 births) and is nearly universally investigated genetically, this is a realistic ascertainment pathway.
- **Cascade testing of siblings** at the time of proband diagnosis is the single highest-yield secondary-prevention action — a presymptomatic biallelic sibling could begin cholesterol/statin therapy before dermatitis and growth failure develop.

### Tertiary prevention (preventing complications in affected individuals)

This is where the evidence is strongest and should anchor the KB's prevention section:
- **Early cataract surgery** to prevent **deprivation amblyopia** — the most time-critical intervention.
- **Early initiation of cholesterol + statin (± bile acid) therapy** to prevent/limit dermatitis, growth failure, and immune dysregulation.
- **Topical cholesterol/statin** to prevent progression of cutaneous disease and its barrier complications.
- **Avoid ineffective immunosuppression** (cyclosporine, anti-TNF) — prevents iatrogenic harm and diagnostic delay.
- **Statin safety monitoring** (CK, LFTs) and consideration of *SLCO1B1* genotyping.
- **Early developmental intervention** — the language response reported by Morales 2022 argues for aggressive early therapy.
- Routine ophthalmologic, growth, pubertal, and developmental surveillance. **No published surveillance guideline exists** — this would be a valuable contribution.

### Public health and environmental interventions

**Not applicable.** No sanitation, vector-control, health-education, or environmental measure is relevant to a monogenic recessive enzymopathy.

---

## 14. Other Species / Natural Disease

### Taxonomy and orthologs

| Species | NCBI Taxon | Gene | Database ID |
|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | **MSMO1** | NCBI Gene 6307; HGNC:10545 |
| *Mus musculus* | NCBITaxon:10090 | ***Msmo1*** | **MGI:1913484**; Chr 8: 65,171,173–65,186,826 (− strand) |
| *Rattus norvegicus* | NCBITaxon:10116 | *Msmo1* | RGD:620281 |
| *Danio rerio* | NCBITaxon:7955 | *msmo1* | ZFIN (see §15) |
| *Saccharomyces cerevisiae* | NCBITaxon:4932 | ***ERG25*** | SGD — the founding ortholog; the human gene alias *ERG25* derives from it |

The gene is deeply conserved from yeast to human — *ERG25* performs the identical C4-methyl oxidation in ergosterol biosynthesis. This makes the pathway an excellent evolutionary-conservation example and underpins the antifungal relevance of the sterol pathway.

### Natural disease in other species

**None reported.** A search of **OMIA (Online Mendelian Inheritance in Animals)** for *MSMO1* returned **no phenes** — there is no naturally occurring *MSMO1* disorder documented in companion animals, livestock, or wildlife.

- **Veterinary relevance:** none currently. **Not applicable.**
- This contrasts with several other cholesterol-pathway genes that do have OMIA entries, so the absence is likely genuine rather than an ascertainment gap in small animals — though naturally-occurring congenital cataract in dogs remains a plausible place to look.

### Breed

**Not applicable** — no VBO breed association exists.

### Comparative biology

- **Evolutionary conservation:** high. The three-step C4-methyl oxidation and its di-iron/cytochrome-b5 chemistry are conserved from *S. cerevisiae* (Erg25p) through zebrafish to human, as is the three-enzyme C4-demethylation complex architecture.
- **Comparative pathology:** the striking cross-species observation is that **complete loss of function is lethal** in zebrafish (larval death by 9 dpf) while human patients survive with a chronic multisystem phenotype — strong evidence that all reported human alleles are **hypomorphic**. The zebrafish also reveals a tissue-specific requirement (pre-hypertrophic chondrocytes) not obvious from the human phenotype, and predicts the human delayed skeletal maturation.
- **Transmission / zoonotic potential / cross-species susceptibility:** **not applicable** (non-communicable genetic disease).

---

## 15. Model Organisms

### 15.1 Zebrafish (*Danio rerio*) — the best-characterized model

**Anderson RA et al., "Zebrafish models of skeletal dysplasia induced by cholesterol biosynthesis deficiency," *Disease Models & Mechanisms* 2020 (PMID:32430393; PMC7328163; DOI 10.1242/dmm.042549).** Evidence source: **MODEL_ORGANISM.**

> "Human disorders of the post-squalene cholesterol biosynthesis pathway frequently result in skeletal abnormalities, yet our understanding of the mechanisms involved is limited. In a forward-genetic approach, we have found that a late-onset skeletal mutant, named *kolibernu7*, is the result of a *cis*-acting regulatory mutation leading to loss of *methylsterol monooxygenase 1* (*msmo1*) expression within pre-hypertrophic chondrocytes."

**Alleles:**
- ***kolibernu7*** — a **cis-regulatory** mutation causing tissue-restricted loss of *msmo1* expression in **pre-hypertrophic chondrocytes**; produces a viable, **late-onset skeletal** phenotype. (Notable: this allele class — regulatory, tissue-specific — has **no human counterpart yet described**, and is a concrete hypothesis for undiagnosed WES-negative skeletal patients.)
- ***msmo1^nu81^*** — a 37-bp insertion causing frameshift and premature truncation (**functional null**). Homozygotes "**die by 9 dpf**."

**Key findings:**
- Rescued mutants develop "dramatic skeletal abnormalities, with a loss of Msmo1 activity resulting in a more-severe patterning defect of a near-complete loss of hypertrophic chondrocytes marked by *col10a1a* expression."
- **Dual pathogenic mechanism disentangled genetically:** double *lss^nu60^;msmo1^nu81^* mutants (blocking the pathway further upstream at lanosterol synthase) **survive longer** than *msmo1^nu81^* alone, indicating "toxic sterol intermediates may contribute to the death" — i.e., lethality reflects **both** cholesterol deprivation **and** methylsterol toxicity. This is the cleanest in vivo demonstration anywhere of the substrate-toxicity arm and is the direct biological justification for statin (substrate-reduction) therapy in patients.
- **Tissue-specific rescue:** liver-restricted *Tg(fabp10a:msmo1:pA)^nu100^* suppresses early lethality, yielding juvenile mutants phenotypically indistinguishable from *kol^nu7^* — establishing hepatic *msmo1* as sufficient for survival while local chondrocyte expression governs the skeletal phenotype.

**Phenotype recapitulation:** excellent for the **skeletal** dimension (maps onto human delayed skeletal maturation) and for the **dual-mechanism** biochemistry. **Limitations:** does not model psoriasiform dermatitis (no mammalian epidermal barrier equivalent), cataract, or the human immune phenotype; the null is lethal, so it does not model the human hypomorphic steady state without engineered rescue.

**Resources:** ZFIN.

### 15.2 Mouse (*Mus musculus*)

**MGI:1913484** (*Msmo1*, Chr 8). MGI records **14 mutations/alleles**: 8 gene-trapped, 3 targeted, 2 endonuclease-mediated, 1 chemically induced; **20 IMSR strains/lines available**; 15 phenotype references.

**IMPC (mousephenotype.org, MGI:1913484):** the pipeline reports **0 significant phenotypes**, with 20 of 24 physiological systems tested. Viability data were collected but the homozygous viability call was not resolvable from the accessible page.

> **Important caveat for curation:** the "0 significant phenotypes" result must be interpreted with care. Given that zebrafish *msmo1* nulls are larval-lethal, a null-allele mouse would most plausibly be **embryonic/perinatal lethal** — in which case IMPC adult pipelines would return no significant adult phenotypes because homozygotes are absent, not because they are normal. **Do not curate "0 significant phenotypes" as evidence that Msmo1 loss is benign in mouse.** I could not verify the IMPC viability call; this should be checked directly at IMPC before any assertion.

**No published *Msmo1* mouse model of MSMO1 deficiency exists** — i.e., no paper reporting a mouse that recapitulates the human MCCPD phenotype. This is a **major, explicitly curatable knowledge gap** and an obvious target for a `HUMAN_MODEL_MISMATCH` discussion entry: the human disease is a hypomorphic missense disorder, and the available mouse alleles are nulls/gene-traps that likely do not model it.

**The informative mammalian in vivo data come from the *paralogous* gene *Nsdhl*** (same C4-demethylation complex): "Analysis of Nsdhl-deficient mice confirmed dramatic loss of internalized growth factor receptors in fibroblasts and reduced activation of EGFR signaling in NSDHL-lacking skin regions" (PMID:23125191), and "we ablated Nsdhl in adult keratinocytes expressing KRAS(G12D)... Loss of Nsdhl induced the expression of ATP-binding cassette (ABC) transporters ABCA1 and ABCG1, reduced the expression of low-density lipoprotein receptor (LDLR), decreased intracellular cholesterol, and was dependent on the liver X receptor (LXR) α" (PMID:26344763). The classic *Nsdhl* mouse alleles are ***bare patches* (Bpa)** and ***striated* (Str)** — X-linked dominant, male-lethal, modeling CHILD syndrome. These are **paralog** models and must be curated as such, not as MSMO1 models.

**Resources:** MGI, IMPC, IMSR, KOMP/EuMMCR, MMRRC.

### 15.3 Cellular and in vitro models

- **Patient-derived dermal fibroblasts** — the workhorse human model. Demonstrate elevated methylsterols, 3-fold increased S-G2-M/G0-G1 ratio in cholesterol-restricted medium, constitutive IL-6 production suppressible by simvastatin, diminished EGFR/ERK signaling, and disrupted vesicular trafficking (PMID:21285510, PMID:24144731). Evidence source: **IN_VITRO**.
- **Pharmacologic phenocopy model** — SMO inhibition with **ATZ** in normal human lymphoblasts and leukocytes reproduces both the cell-cycle activation (3-fold S-G2-M/G0-G1 increase) and the immune phenotype (>6-fold TLR-2^+^TLR-4^−^ granulocyte increase; 2-fold CD8 decrease). This chemical-genetic approach is elegant because it establishes **causality** in normal human cells and is directly reusable.
- **siRNA/shRNA knockdown in cancer cell lines** — used to define the EGFR-trafficking role (RAB11 vs RAB7) and the EGFR-inhibitor-sensitization phenotype, including **A431 xenografts sensitized to cetuximab** (PMID:23125191).
- **Yeast (*S. cerevisiae* erg25 mutants)** — the original genetic system defining the enzymatic step; available via SGD.
- **iPSC, organoid, and 3D skin-equivalent models:** **none published.** Given that the disease's most treatable manifestation is cutaneous, a patient-iPSC-derived keratinocyte or 3D epidermal-equivalent model is a conspicuous missing tool.

### 15.4 Model summary and gaps

| Model | Recapitulates | Does not recapitulate | Status |
|---|---|---|---|
| Zebrafish *msmo1^nu81^* (null) | Lethality; dual sterol-toxicity/deficiency mechanism | Skin, lens, immune, hypomorphic steady state | Published, robust |
| Zebrafish *kol^nu7^* (cis-regulatory) | Skeletal dysplasia; chondrocyte patterning | Everything non-skeletal | Published, robust |
| Mouse *Msmo1* alleles | — (no disease model published) | Entire human phenotype | **Gap** |
| Mouse *Nsdhl* (Bpa/Str) | EGFR trafficking, LXR/ABCA1, skin sterol biology | Is a **paralog**, X-linked, models CHILD not MCCPD | Published; use with care |
| Patient fibroblasts | Sterol accumulation, hyperproliferation, IL-6, EGFR signaling | Tissue architecture, in vivo immunity | Published, well characterized |
| ATZ chemical phenocopy | Cell cycle, granulocyte TLR phenotype | Chronic/developmental effects | Published |
| iPSC / organoid / 3D skin | — | — | **Gap — none exist** |

---

## Appendix A — Consolidated evidence table (verified PMIDs and DOIs)

| PMID | Citation | Year | Evidence source | Role in this entry |
|---|---|---|---|---|
| **21285510** | He M, Kratz LE, Michel JJ, Vallejo AN, Ferris L, Kelley RI, et al. Mutations in the human SC4MOL gene encoding a methyl sterol oxidase cause psoriasiform dermatitis, microcephaly, and developmental delay. *J Clin Invest.* DOI 10.1172/JCI42650. PMC3049385 | 2011 | HUMAN_CLINICAL (+ IN_VITRO) | **Landmark / disease-defining.** Index patient, first mutations, sterol values, immunophenotype, LXR/MAS hypothesis, failed therapies |
| **24144731** | He M, Smith LD, Chang R, Li X, Vockley J. The role of sterol-C4-methyl oxidase in epidermal biology. *Biochim Biophys Acta* 1841(3):331-5. DOI 10.1016/j.bbalip.2013.10.009. PMC3943829 | 2014 | HUMAN_CLINICAL (review) | Patients 2–4; **treatment algorithm with doses**; EGFR trafficking; PSORS9 |
| **23125191** | Sukhanova A, Gorin A, Serebriiskii IG, et al. Targeting C4-demethylating genes in the cholesterol pathway sensitizes cancer cells to EGF receptor inhibitors via increased EGF receptor degradation. *Cancer Discov.* DOI 10.1158/2159-8290.CD-12-0031 | 2013 | IN_VITRO + MODEL_ORGANISM | EGFR trafficking/degradation mechanism; ketoconazole upstream-block rescue |
| **26344763** | Gabitova L, Restifo D, Gorin A, et al. Endogenous Sterol Metabolites Regulate Growth of EGFR/KRAS-Dependent Tumors via LXR. *Cell Rep.* DOI 10.1016/j.celrep.2015.08.023 | 2015 | MODEL_ORGANISM + IN_VITRO | MAS→LXRα→ABCA1/ABCG1/LDLR axis (via *Nsdhl* paralog) |
| **26038696** | Yasuda K, et al. Human hepatic metabolism of the anti-osteoporosis drug eldecalcitol involves sterol C4-methyl oxidase. *Pharmacol Res Perspect.* | 2015 | IN_VITRO | Non-sterol substrate; drug-metabolism relevance |
| **28673550** | Frisso G, Gelzo M, Procopio E, Sica C, Lenza MP, Dello Russo A, Donati MA, Salvatore F, Corso G. A rare case of sterol-C4-methyl oxidase deficiency in a young Italian male: Biochemical and molecular characterization. *Mol Genet Metab.* DOI 10.1016/j.ymgme.2017.06.013 | 2017 | HUMAN_CLINICAL | Patient 5; **microcephaly-negative** phenotype; p.Gly202Glu; diagnostic recommendation |
| **32430393** | Anderson RA, et al. Zebrafish models of skeletal dysplasia induced by cholesterol biosynthesis deficiency. *Dis Model Mech.* DOI 10.1242/dmm.042549. PMC7328163 | 2020 | MODEL_ORGANISM | *msmo1* null lethality; chondrocyte patterning; dual-mechanism genetics |
| **33161406** | Kalay Yildizhan I, Gökpınar İli E, Onoufriadis A, Kocyigit P, Kesidou E, Simpson MA, McGrath JA, Yürür Kutlay N, Kundakci N. New Homozygous Missense MSMO1 Mutation in Two Siblings with SC4MOL Deficiency Presenting with Psoriasiform Dermatitis. *Cytogenet Genome Res* 160(9):523-530. DOI 10.1159/000511126 | 2020 | HUMAN_CLINICAL | Turkish siblings; p.Asn27Thr; ocular spectrum; oral+topical therapy |
| **37195326** | Tkemaladze T, Bratland E, Bregvadze K, Shatirishvili T, Tatishvili N, Abzianidze E, Houge G, Douzgou S. MSMO1 deficiency: a potentially partially treatable, ultrarare neurodevelopmental disorder with psoriasiform dermatitis, alopecia and polydactyly. *Clin Dysmorphol.* DOI 10.1097/MCD.0000000000000461 | 2023 | HUMAN_CLINICAL | Georgian siblings; **polydactyly, alopecia, spasticity**; p.Glu183Ala; treatment response |
| **41718295** | Hassas N, Drackley A, Ivanisevic J, Ralay Ranaivo H, Kurup SP. Infantile Cataracts Associated with a Homozygous Missense MSMO1 Variant—Case Report and Literature Review. *Reports* 9(1):45. DOI 10.3390/reports9010045. PMC12922104 | 2026 | HUMAN_CLINICAL | Most recent case; **ACMG reclassification of p.Gly115Arg**; gnomAD v4.1 data; lens mechanism; MRI findings |
| *(no PMID)* | Morales JA, Curry CJ, Enns GM. Clinical characterization of a new individual with mild SC4MOL deficiency: diagnostic and therapeutic implications. *J Transl Genet Genom.* DOI 10.20517/jtgg.2022.01 | 2022 | HUMAN_CLINICAL | **Mildest reported case**; normal OFC and cholesterol; detailed statin dosing; language response |
| *(PMID unconfirmed)* | MSMO1 promotes chemotherapy resistance through modulation of T-MAS metabolism via PERK/eIF2α/ATF4/CHOP pathway. *iScience*. PII S2589004226001653 | 2026 | IN_VITRO | T-MAS/ER-stress mechanism; **verify PMID before citing** |

**Structured-source references available for this entry:**
- `ORPHA:488168` — Orphanet record (I was blocked by Orphanet's bot protection during this session; **fetch the cache with `just structured-rebuild-orphanet --id 488168` and quote actual rows rather than relying on my summary**).
- `CGGV:` / `CGDS:` — **not available**; ClinGen has published no MSMO1 curation.
- `NCIT:` P302 treatment indications — none expected for this indication (all therapy is off-label).
- `ICEES:` — not applicable (ultra-rare; will not appear in EHR comorbidity data).

---

## Appendix B — Curation notes and flagged uncertainties

**Verified during this research (safe to use):**
- MONDO:0014793, OMIM:616834, OMIM gene 607545, ORPHA:488168, MedGen C5567510/UID 1798933, GARD 0017886, UMLS C5567510, HGNC:10545, NCBI Gene 6307, UniProt Q15800, EC 1.14.18.9, ENSG00000052802, NM_006745.5
- All 20 HPO terms in §3.1 (retrieved live from the HPO/JAX annotation API)
- HP:0001596 Alopecia, HP:0010442 Polydactyly, HP:0100259 Postaxial polydactyly (OLS4)
- GO:0000254, GO:0006695 (OLS4)
- CL:0011004, CL:0002224 (OLS4)
- CHEBI:16113 cholesterol, CHEBI:17813 FF-MAS, CHEBI:18364 14-demethyllanosterol (T-MAS) (OLS4)
- gnomAD v4.0 constraint via ClinGen: pLI 0, LOEUF 0.9, %HI 44.79
- All verbatim quotes in this report were taken from PubMed abstract pages or PMC full text and should validate as exact substrings — **but still run `just fetch-reference` + `just validate-references` on each before committing.**

**Explicitly NOT verified — verify with OAK before entry:**
- All ontology IDs marked *(unverified)* in §3.2, §6.8, §7, and §12.9 — in particular every NCIT and CHEBI drug ID in the treatment table.
- ICD-10 E78.7 mapping (inferred, not confirmed as the official Orphanet mapping).
- The iScience 2026 PMID.
- Per-variant ClinVar classifications.
- IMPC *Msmo1* homozygous viability call.

**NEC (Named Entity Confusion) preflight — passed.** The gene named throughout every retrieved source is *MSMO1*/*SC4MOL* at 4q32.3; the OMIM number 616834 is consistent across OMIM, MedGen, Orphanet, GARD, and MONDO; and the MONDO cross-references resolve to the same UMLS concept. There is no eponym, numbered-series, or synonym collision risk here. The one adjacent-entity risk to watch is ***NSDHL***/CHILD syndrome — the same enzyme complex, frequently co-cited, and the source of much of the mammalian in vivo data. **Do not attribute *Nsdhl* mouse findings (Bpa/Str, keratinocyte KRAS ablation) to *MSMO1*.**

**Highest-value knowledge gaps to curate as `discussions`:**
1. `KNOWLEDGE_GAP` — No natural history study, registry, survival data, or QoL measurement exists for any patient.
2. `HUMAN_MODEL_MISMATCH` — No mouse model of MSMO1 deficiency exists; available *Msmo1* alleles are nulls/gene-traps while every human allele is hypomorphic missense, and zebrafish nulls are lethal. IMPC's "0 significant phenotypes" is likely an artifact of homozygote absence, not evidence of a benign knockout.
3. `KNOWLEDGE_GAP` — Whether treatment initiated presymptomatically (via cascade testing) alters neurodevelopmental outcome; the critical-period hypothesis is untested.
4. `KNOWLEDGE_GAP` — MAS are physiologically concentrated in testis and ovary, yet no fertility, gonadal, or meiotic data have ever been reported in patients.
5. `KNOWLEDGE_GAP` (emerging hypothesis) — Whether heterozygous *MSMO1* carriers (who show elevated methylsterols and abnormal granulocyte activation) are at increased risk of common inflammatory skin disease; PSORS9 candidacy remains untested. Curate as `mechanistic_hypotheses` with `status: EMERGING`, not as an asserted mechanism.
6. `KNOWLEDGE_GAP` — No human cis-regulatory *MSMO1* allele has been described, despite the zebrafish *kol^nu7^* precedent; WES-negative patients with compatible phenotypes should have WGS.

**Suggested `conforms_to` / module relationships (for dismech structural curation):**
- MSMO1 deficiency is a strong candidate conformer for a *new* **`sterol_biosynthesis_block`** module (deficient distal enzyme → precursor accumulation + cholesterol deficiency → multisystem developmental and dermatologic disease), which would also cover SLOS, lathosterolosis, desmosterolosis, CHILD, CDPX2, and HEM. No such module currently exists in `kb/modules/`.
- It should **not** conform to `metabolic_intoxication_decompensation` — there is no acute decompensation phenotype.
- It should **not** conform to `lysosomal_substrate_accumulation` — the accumulation is cytosolic/ER-membrane sterol, not lysosomal.
- `cataract_lens_opacification` is a plausible conformance target for the ocular node, though the proximate mechanism (membrane lipid composition) differs from the module's crystallin-aggregation chain — check the module's node definitions before asserting.
- The MSMO1/NSDHL/HSD17B7 **sterol C4-demethylation complex** is a natural grouping axis: a `Grouping` over MSMO1 deficiency + CHILD syndrome + CK syndrome with `grouping_basis: [SHARED_PATHWAY, SHARED_MECHANISM]` would be well-supported by the shared EGFR-trafficking and LXR findings.

---

## Sources

- [He et al. 2011, J Clin Invest — PMID:21285510](https://pubmed.ncbi.nlm.nih.gov/21285510/) · [PMC3049385](https://pmc.ncbi.nlm.nih.gov/articles/PMC3049385/)
- [He et al. 2014, Biochim Biophys Acta — PMID:24144731](https://pubmed.ncbi.nlm.nih.gov/24144731/) · [PMC3943829](https://pmc.ncbi.nlm.nih.gov/articles/PMC3943829/)
- [Sukhanova et al. 2013, Cancer Discov — PMID:23125191](https://pubmed.ncbi.nlm.nih.gov/23125191/)
- [Gabitova et al. 2015, Cell Rep — PMID:26344763](https://pubmed.ncbi.nlm.nih.gov/26344763/)
- [Frisso et al. 2017, Mol Genet Metab — PMID:28673550](https://pubmed.ncbi.nlm.nih.gov/28673550/)
- [Anderson et al. 2020, Dis Model Mech — PMID:32430393](https://pmc.ncbi.nlm.nih.gov/articles/PMC7328163/)
- [Kalay Yildizhan et al. 2020, Cytogenet Genome Res — PMID:33161406](https://pubmed.ncbi.nlm.nih.gov/33161406/) · [Karger](https://karger.com/cgr/article/160/9/523/62866/New-Homozygous-Missense-MSMO1-Mutation-in-Two)
- [Morales, Curry & Enns 2022, J Transl Genet Genom](https://www.oaepublish.com/articles/jtgg.2022.01)
- [Tkemaladze et al. 2023, Clin Dysmorphol — PMID:37195326](https://pubmed.ncbi.nlm.nih.gov/37195326/)
- [Hassas et al. 2026, Reports — PMC12922104](https://pmc.ncbi.nlm.nih.gov/articles/PMC12922104/) · [DOI 10.3390/reports9010045](https://doi.org/10.3390/reports9010045)
- [OMIM 616834](https://omim.org/entry/616834) (403 to automated fetch; content accessed via MedGen/GARD/MalaCards mirrors)
- [NCBI MedGen C5567510](https://www.ncbi.nlm.nih.gov/medgen/?term=MSMO1+deficiency)
- [NCBI Gene 6307 — MSMO1](https://www.ncbi.nlm.nih.gov/gene/6307)
- [NIH GTR — MSMO1](https://www.ncbi.nlm.nih.gov/gtr/genes/6307/)
- [UniProt Q15800](https://rest.uniprot.org/uniprotkb/Q15800.txt)
- [HPO/JAX annotation API — OMIM:616834](https://ontology.jax.org/api/network/annotation/OMIM:616834)
- [EBI OLS4](https://www.ebi.ac.uk/ols4/) (MONDO, GO, CL, CHEBI, HP term verification)
- [ClinGen — MSMO1 (HGNC:10545)](https://search.clinicalgenome.org/kb/genes/HGNC:10545)
- [MGI:1913484 — mouse Msmo1](https://www.informatics.jax.org/marker/MGI:1913484)
- [IMPC — Msmo1](https://www.mousephenotype.org/data/genes/MGI:1913484)
- [GARD 17886](https://rarediseases.info.nih.gov/diseases/17886/microcephaly-congenital-cataract-psoriasiform-dermatitis-syndrome)
- [Orphanet ORPHA:488168](https://www.orpha.net/en/disease/detail/488168) (bot-protected; not directly retrievable this session)
- [OMIA search — no MSMO1 phenes](https://omia.org/)
- [MSMO1/T-MAS/PERK chemoresistance, iScience 2026](https://www.sciencedirect.com/science/article/pii/S2589004226001653)