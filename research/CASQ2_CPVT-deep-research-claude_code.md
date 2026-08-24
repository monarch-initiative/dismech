---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T17:11:16.643796'
end_time: '2026-07-31T17:16:57.113982'
duration_seconds: 340.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CASQ2 CPVT
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 22
  num_turns: 29
  total_cost_usd: 1.9748198000000003
  session_id: 1ff1ab7e-d42a-5ad6-b222-89444922f8c7
  stop_reason: end_turn
citation_count: 39
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CASQ2 CPVT
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **CASQ2 CPVT** covering all of the
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

I now have sufficient comprehensive information to compile the full research report.

---

# CASQ2-Related Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT2): Comprehensive Research Report

## 1. Disease Information

**Overview.** Catecholaminergic polymorphic ventricular tachycardia (CPVT) is an inherited primary electrical (arrhythmogenic) disorder of the structurally normal heart, characterized by adrenergically triggered polymorphic or bidirectional ventricular tachycardia (VT) that arises during exercise or acute emotional stress and can degenerate into ventricular fibrillation and sudden cardiac death (SCD). The **CASQ2-related, autosomal recessive form (CPVT2)** is caused by biallelic (homozygous or compound heterozygous) pathogenic variants in *CASQ2*, encoding cardiac calsequestrin-2, the principal Ca²⁺-buffering protein of the cardiac sarcoplasmic reticulum (SR) ([GeneReviews, NBK1289](https://www.ncbi.nlm.nih.gov/books/NBK1289/); [OMIM #611938](https://omim.org/entry/611938)).

**Key identifiers:**
- **OMIM (phenotype):** #611938 — Ventricular Tachycardia, Catecholaminergic Polymorphic, 2 (CPVT2)
- **OMIM (gene):** *114251 — CALSEQUESTRIN 2; CASQ2
- **HGNC:** 1513 (CASQ2); **NCBI Gene ID:** 845
- **UniProt:** O14958 (human CASQ2)
- **Orphanet:** ORPHA3286 (parent term "Catecholaminergic polymorphic ventricular tachycardia," covering both CPVT1/RYR2 and CPVT2/CASQ2)
- **ICD-10-CM:** I47.2 (Ventricular tachycardia), more granularly I47.29 (Other ventricular tachycardia)
- **MeSH:** C536334
- **Disease Ontology:** DOID:0060676
- **Chromosomal locus:** 1p13.1 (CASQ2 gene) ([Lahat et al. 2001](https://omim.org/entry/114251))

**Synonyms:** CPVT2; Familial polymorphic ventricular tachycardia, catecholamine-induced, autosomal recessive; Calsequestrin-associated CPVT; Stress-induced polymorphic ventricular tachycardia (CASQ2-related); VTSCA (older nomenclature).

**Evidence base:** Information is derived primarily from aggregated disease-level resources — case series, multicenter cohort/registry studies (notably the International CPVT collaboration), founder-population family studies (Bedouin, Saudi, other consanguineous kindreds), and functional/model-organism studies — rather than large-scale individual-level EHR mining, reflecting CPVT2's rarity.

---

## 2. Etiology

**Disease causal factor — genetic, monogenic.** CPVT2 is caused by loss-of-function or hypomorphic biallelic variants in *CASQ2* (1p13), inherited in an autosomal recessive pattern; it is not caused by environmental or infectious factors, though environmental/physiologic triggers (see below) precipitate the arrhythmic events themselves. *CASQ2* mutations account for roughly **2–5%** of genotyped CPVT cases overall (some series cite 1–2%), versus ~50–65% for dominant *RYR2* variants ([search synthesis](https://en.wikipedia.org/wiki/Catecholaminergic_polymorphic_ventricular_tachycardia); [Clinical Gate review](https://clinicalgate.com/genetic-diseases-catecholaminergic-ventricular-tachycardia/)).

**Genetic risk factors:**
- **Causal (biallelic) variants** — homozygous or compound heterozygous missense, nonsense, frameshift, and splice-site *CASQ2* variants. The prototype is the Bedouin founder mutation **D307H** (c.1038G>C, exon 9), identified by Lahat et al. in 2001 in 7 consanguineous Bedouin kindreds in northern Israel with a history of unexplained childhood sudden death (9 deaths, 7 during vigorous exercise, 2 during excitement) (PMID cited via [OMIM 114251](https://omim.org/entry/114251); [GeneTests founder-variant review](https://www.ncbi.nlm.nih.gov/books/NBK583118/)). The mutation converts a conserved, negatively charged Asp to a positively charged His in an acidic Ca²⁺-binding domain and was absent in 350 population controls, confirming founder status.
- **Heterozygous "carrier" variants with reduced/variable penetrance** — a subset of missense variants can act in a dominant-negative fashion. In the International Multicenter CASQ2-CPVT study (Circulation, 2020), of 66 heterozygous family members, **17/51 clinically evaluated (33.3%) met CPVT diagnostic criteria**, with penetrance dependent on variant location within the CASQ2 filament structure ([Roston et al. 2020](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.120.045723)). Homozygotes/compound heterozygotes had a 3.2-fold increased hazard of cardiac events versus heterozygotes, and a 38.8-fold increased hazard versus genotype-negative relatives.
- **Population variant burden vs. disease prevalence discordance** — gnomAD collective frequency of presumed pathogenic *CASQ2* variants (0.0997%) is ~398-fold higher than expected CPVT2 disease prevalence, implying incomplete penetrance and/or recessive-only pathogenicity for many variants ([Roston et al. 2020](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.120.045723)).
- **Modifier/other CPVT genes** (genetic heterogeneity, not CASQ2 modifiers per se): *RYR2* (CPVT1, dominant, most common), *CALM1/CALM2/CALM3* (CPVT4, calmodulinopathy), *TRDN*/triadin (CPVT5, recessive, ± skeletal myopathy), *TECRL* (mixed CPVT/LQT phenotype). A standard clinical CPVT NGS panel covers these ~6–7 genes, which together explain up to ~75% of clinically diagnosed CPVT (remainder genetically elusive) ([Mayo Clinic Labs CPVTG panel](https://www.mayocliniclabs.com/test-catalog/overview/617211)).

**Environmental/physiologic risk factors (triggers, not causes):** vigorous physical exertion, competitive sports, acute emotional stress/excitement, sympathomimetic exposure (e.g., epinephrine, some anesthetics), fever (less prominent than in some other channelopathies). Age and pubertal growth are relevant because β-blocker dosing must scale with rapidly changing body weight.

**Protective factors:** No genetic protective alleles are established. Environmentally, adherence to non-selective β-blockade and avoidance of competitive/high-intensity exercise are the dominant modifiable protective factors; there is no dietary or lifestyle protective factor analogous to other cardiac conditions.

**Gene-environment interaction:** The core mechanism *is* a gene-environment (genotype × catecholamine) interaction — the CASQ2 lesion by itself is often clinically silent at rest; sympathetic activation (via β-adrenergic receptor stimulation → PKA-mediated phosphorylation of Ca²⁺-handling proteins) is required to unmask spontaneous SR Ca²⁺ release and triggered arrhythmia. This is the mechanistic basis for exercise stress testing as the diagnostic gold standard.

---

## 3. Phenotypes

CPVT2 has a narrow, cardiology-dominant phenotype spectrum (a "single-mechanism" arrhythmia syndrome), in contrast to multisystem genetic diseases.

| Phenotype | Type | Onset | Severity/course | Frequency | Suggested HPO term |
|---|---|---|---|---|---|
| Syncope (exercise/emotion-induced) | Symptom | Mean 7–12 y (range into 4th decade) | Episodic, recurrent without treatment | Up to 80% of patients before diagnosis | HP:0001279 Syncope |
| Bidirectional ventricular tachycardia | Clinical sign (ECG) | Provoked by exercise/adrenergic stress | Episodic; hallmark finding | Characteristic but not universal | HP:0004308 Ventricular tachycardia (closest available; no dedicated bidirectional-VT HPO term) |
| Polymorphic ventricular tachycardia | Clinical sign (ECG) | Provoked by exercise/emotion | Episodic, can degenerate to VF | Common | HP:0004308 Ventricular tachycardia |
| Ventricular fibrillation / cardiac arrest | Clinical sign | Any age; may be first presentation | Life-threatening | ~30% experience ≥1 cardiac arrest | HP:0001695 Ventricular fibrillation |
| Sudden cardiac death | Outcome | Childhood–adulthood | Can be the presenting/only event | Up to 30–50% by age 20–35 if untreated | HP:0001645 Sudden death |
| Resting sinus bradycardia | Clinical sign / lab (ECG) | Present at baseline | Stable | Frequently reported in CASQ2-linked patients | HP:0001662 Sinus bradycardia |
| Palpitations | Symptom | Exercise-associated | Episodic | Variable | HP:0001962 Palpitations |
| Seizure-like episodes (misdiagnosed) | Symptom (secondary to cerebral hypoperfusion during arrhythmia) | Any | Episodic | Reported (case reports of CPVT presenting as tonic-clonic seizure) | HP:0001250 Seizure |
| Structurally normal heart | Negative finding (diagnostic criterion) | — | — | By definition | — |
| Normal resting 12-lead ECG (baseline) | Negative finding | — | — | By definition | — |

**Phenotype characteristics:**
- **Age of onset:** mean first syncopal episode age 7–12 years; can present as late as the 4th decade of life ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1289/)).
- **Severity/progression:** episodic and stress-triggered rather than progressive/degenerative; however, cumulative arrhythmic burden and risk of SCD increase with age and missed diagnosis. CASQ2-linked (recessive) disease tends to have **earlier onset, more severe presentation, and higher untreated mortality** than RYR2-CPVT ([Josephs et al. 2017, Mol Genet Genomic Med](https://onlinelibrary.wiley.com/doi/full/10.1002/mgg3.323); International Multicenter study).
- **Course pattern:** episodic/paroxysmal (event-driven by exertion/emotion), not relapsing-remitting or chronic-progressive in the classic sense; between events patients are typically asymptomatic.
- **Long-term structural change:** in murine CASQ2-mutant models, cardiac morphology is normal in young animals, but by ~35 weeks some mice develop cardiac hypertrophy and LV dysfunction (model-organism evidence; translational significance in humans not firmly established) ([Circulation 2014, di Barletta model discussion](https://www.ahajournals.org/doi/10.1161/circulationaha.113.006901)).
- **Quality of life impact:** activity restriction (avoidance of competitive sports), psychological burden of ICD shocks/anxiety around exertion, and pediatric-family burden of frequent surveillance visits (every 6–12 months, more often around puberty due to rapid weight-based dose titration) are the dominant QoL domains reported in the clinical literature; no CPVT-specific validated QoL instrument was identified in this search — generic pediatric cardiology QoL literature (not disease-specific) would need separate sourcing.

---

## 4. Genetic/Molecular Information

**Causal gene:** *CASQ2* (calsequestrin 2), HGNC:1513, NCBI Gene 845, chromosome 1p13.1; OMIM gene *114251.

**Variant classes reported (ClinVar/literature):**
- **Missense** — e.g., D307H (Bedouin founder), R33Q, D310N, I161V, and numerous others; several missense variants (especially those disrupting the CASQ2 filament/dimer interface) can behave as **dominant-negative** in heterozygotes, producing a milder dominant phenotype in carriers ([Roston 2020](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.120.045723); [Bal-Erilmaz functional analysis PMC7666291](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7666291/)).
- **Splice-site** — e.g., functionally characterized splicing mutations altering CASQ2 mRNA processing, with implications for genetic counseling.
- **Frameshift/truncating/null** — e.g., G112+5X-type mutations used widely in iPSC and computational disease models; truncating variants collectively reach ~0.049% frequency in gnomAD.
- **Allele frequency (gnomAD):** individual pathogenic *CASQ2* variants range from novel (absent) up to ~0.06424% (p.D310N); the aggregate frequency of presumptively pathogenic variants (0.0997%) substantially exceeds expected disease prevalence, implying incomplete penetrance for many alleles ([Roston 2020](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.120.045723)).
- **Somatic vs. germline:** exclusively germline; no somatic mosaicism literature identified in this search.
- **Functional consequence:** predominantly **loss-of-function / reduced CASQ2 protein expression** (severe reduction or complete loss), with the pathogenic cascade proceeding through compensatory upregulation of calreticulin and RyR2 (below). Some dominant missense alleles act via **dominant-negative disruption of CASQ2 polymer/filament assembly** rather than simple haploinsufficiency ([di Barletta/Knollmann JCI 2006](https://www.jci.org/articles/view/31080)).

**Modifier genes:** No formally validated CASQ2-CPVT-specific modifier genes were identified; genetic background/other Ca²⁺-handling gene variants (RYR2, TRDN, CALM1-3) are relevant to the broader CPVT gene family rather than as CASQ2 modifiers per se.

**Epigenetic information:** No CPVT2-specific epigenetic (DNA methylation/histone) studies were surfaced in this search; not established as disease-relevant currently.

**Chromosomal abnormalities:** CPVT2 is a point-mutation/small-indel monogenic disease; no recurrent large chromosomal rearrangements are described for *CASQ2*.

**Protein structure/function (UniProt O14958):** CASQ2 is a high-capacity, low-affinity Ca²⁺-binding protein of the junctional SR, binding up to ~60 Ca²⁺ ions via clusters of acidic surface residues, especially at subunit interfaces. It is largely monomeric at low luminal [Ca²⁺] and polymerizes into higher-order oligomers/filaments as Ca²⁺ rises, modulating its interaction with the RyR2 channel complex (via triadin/junctin) ([GeneCards](https://www.genecards.org/card/CASQ2); [Wikipedia Calsequestrin](https://en.wikipedia.org/wiki/Calsequestrin)). Mutations at the interdimer/filament interface (e.g., near Tyr180) disrupt this Ca²⁺-dependent polymerization.

---

## 5. Environmental Information

CPVT2 is a purely genetic, monogenic disorder — there are no known toxic, infectious, or occupational causal exposures. The relevant "environmental" factors are physiologic triggers rather than disease causes:
- **Exercise/exertion** — the principal, near-universal trigger of arrhythmic events and the basis of exercise stress testing for diagnosis.
- **Acute emotional stress/excitement** — second major trigger; historically some Bedouin sudden deaths occurred "during excitement" rather than exertion.
- **Catecholamine/sympathomimetic exposure** — iatrogenic epinephrine, certain anesthetic/perioperative catecholamine surges, and possibly stimulant use are theoretically arrhythmogenic, though not systematically studied for CASQ2-CPVT specifically.
- **No infectious agent involvement.**

---

## 6. Mechanism / Pathophysiology

**Overall causal chain:**
CASQ2 loss-of-function/dominant-negative variant → reduced/dysfunctional SR Ca²⁺ buffering capacity in the junctional SR → **compensatory post-transcriptional upregulation of calreticulin and RyR2** (a paradoxical adaptive response) → increased RyR2 "leakiness" (heightened sensitivity to Ca²⁺-induced Ca²⁺ release even at low diastolic cytosolic Ca²⁺) → spontaneous diastolic SR Ca²⁺ release events ("Ca²⁺ sparks/waves") especially under β-adrenergic stimulation → activation of the electrogenic Na⁺/Ca²⁺ exchanger (NCX1; 3 Na⁺ in for 1 Ca²⁺ out) → **delayed afterdepolarizations (DADs)** → if DAD amplitude reaches threshold, triggered activity → bidirectional/polymorphic ventricular tachycardia → possible degeneration to ventricular fibrillation and sudden death ([JCI 2006, Knollmann/Song](https://www.jci.org/articles/view/31080); [PMC8867003 RyR2 molecular changes](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8867003/); [PMC3433449 cell model DADs](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3433449/)).

Direct quote: *"Adaptive changes to CASQ2 deficiency increased posttranscriptional expression of calreticulin and RyR2, which maintained electrical-mechanical coupling but increased RyR2 leakiness, a paradoxical response further exacerbated by stress."* This unifies the CASQ2 mechanism with the RyR2 (CPVT1) mechanism at the level of RyR2 channel dysfunction — *"The central role of RyR2 dysfunction in CASQ2 deficiency unifies the pathophysiologic mechanism underlying CPVT due to RyR2 or CASQ2 mutations."*

**Molecular pathways:** cardiac excitation-contraction (EC) coupling pathway; β-adrenergic receptor–PKA signaling (phosphorylation of RyR2 at Ser2808 is reported to be increased, with decreased binding of the stabilizing subunit FKBP12.6/calstabin2, further destabilizing the channel's closed state) ([PMC2525570](https://ncbi.nlm.nih.gov/pmc/articles/PMC2525570); mechanism reviews). Relevant GO biological process terms: **GO:0086029** (SR Ca²⁺ release for cardiac muscle contraction), **GO:0086036** (regulation of cardiac muscle cell membrane potential), **GO:0002027** (regulation of heart rate by epinephrine-norepinephrine).

**Cellular processes:** disrupted Ca²⁺-induced Ca²⁺ release (CICR); triggered activity (afterdepolarizations) rather than reentry as the dominant arrhythmia mechanism; no apoptosis/inflammation/fibrosis is centrally implicated (structurally normal myocardium is a diagnostic hallmark), though chronic murine models show late hypertrophic remodeling.

**Protein dysfunction:** loss of Ca²⁺-buffering capacity and disrupted Ca²⁺-dependent polymerization/filament formation of CASQ2 within the SR lumen; secondary structural/functional destabilization of the RyR2 macromolecular complex (RyR2–triadin–junctin–CASQ2 "quaternary complex" at the junctional SR-T-tubule interface).

**Biochemical/ion channel abnormality:** functionally, this is a **calcium-release channelopathy** — the defect is not in a voltage-gated channel itself but in luminal Ca²⁺ sensing/buffering that gates RyR2 opening. Suggested GO Cellular Component terms: **GO:0016529** (sarcoplasmic reticulum), **GO:0014701** (junctional sarcoplasmic reticulum membrane), **GO:0034704** (calcium channel complex).

**Molecular/cellular profiling:** Patient-derived iPSC-cardiomyocyte models (e.g., homozygous CASQ2-D307H, CASQ2-G112+5X) recapitulate decreased Ca²⁺ transient amplitude, elevated diastolic Ca²⁺, faster Ca²⁺ transient rise, delayed afterdepolarizations, oscillatory prepotentials, and after-contractions — directly mirroring RYR2-CPVT iPSC phenotypes and validating the RyR2-convergent mechanism ([PMC4549051](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4549051/); [Cell Death & Disease 2016](https://www.nature.com/articles/cddis2016304)). AAV-mediated wild-type CASQ2 gene delivery to these iPSC-CMs restores calsequestrin expression and rescues the DAD/Ca²⁺-transient phenotype, supporting a gene-replacement therapeutic rationale.

**Advanced technologies:** guinea-pig computational (in silico) ventricular myocyte models have been used to dissect pacing-dependent arrhythmogenic mechanisms of the CASQ2-G112+5X mutation ([PMC9858930](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9858930/)) — a COMPUTATIONAL evidence-source example.

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** heart (cardiac conduction/electrical system); specifically ventricular myocardium. No other organ system is primarily affected — CPVT2 is a "pure" primary electrical disease of the structurally normal heart (UBERON:0000948 heart).
- **Secondary/complication-level involvement:** cerebral hypoperfusion during arrhythmic events can produce syncope or seizure-like activity (secondary, not a direct disease target); chronic murine models show secondary ventricular hypertrophy/dysfunction with age.
- **Body systems:** cardiovascular system (primary); nervous system only secondarily via hypoperfusion-related syncope/seizures.
- **Tissue/cell level:** cardiac muscle tissue (UBERON:0003104 cardiac muscle tissue); specific cell population — **cardiac muscle cell / cardiomyocyte** (Cell Ontology **CL:0000746**, cardiac muscle cell of ventricle: CL:0002131 or CL:0000746 depending on specificity). Both atrial and ventricular myocytes express CASQ2, but the ventricular myocyte is the disease-relevant cell type given the ventricular arrhythmia phenotype.
- **Subcellular level:** the **junctional sarcoplasmic reticulum** (GO:0014701) and the SR-T-tubule dyad/triad junction where the RyR2-CASQ2-triadin-junctin macromolecular Ca²⁺-release complex resides (GO:0016529 sarcoplasmic reticulum; GO:0033017 sarcoplasmic reticulum membrane).
- **Localization:** diffuse throughout ventricular (and to a lesser extent atrial) myocardium — not focal/lateralized; the disease is bilateral/global in the sense that it affects the whole ventricular myocardium's excitability, producing the characteristic bidirectional VT pattern (alternating QRS axis on ECG reflecting alternating right/left ventricular ectopic foci or Purkinje-fiber triggered beats).

---

## 8. Temporal Development

- **Onset:** mean age of first syncope 7–12 years (pediatric-onset predominant); can rarely present as late as the 4th decade. Onset pattern is **acute/episodic** (a discrete syncopal or arrhythmic event), not insidious.
- **Progression:** the underlying molecular lesion is present from birth (congenital, though clinically silent at rest); the *clinical* course is not classically "progressive" in a structural sense but the cumulative risk of a fatal event increases with age/exposure to triggers if undiagnosed/untreated. Some murine and possibly human evidence suggests late secondary structural remodeling (hypertrophy) with age.
- **Disease course pattern:** **episodic/paroxysmal** — patients are asymptomatic between adrenergically triggered events; this is a "channelopathy" pattern (crisis-driven) rather than relapsing-remitting or steadily progressive.
- **Disease duration:** chronic, lifelong (genetic, incurable at present outside of experimental gene therapy); however, well-managed patients on adequate therapy can have long event-free intervals.
- **Remission patterns:** no spontaneous remission; treatment (β-blockade ± flecainide ± LCSD ± ICD) substantially reduces but does not eliminate arrhythmic risk. Some published guidance indicates *"a significant burden of life-threatening arrhythmias persists after left cardiac sympathetic denervation"* even with maximal adjunctive therapy.
- **Critical periods:** puberty is a clinically important critical/vulnerable window because rapid weight gain requires frequent β-blocker dose re-titration (surveillance recommended every 6–12 months, more frequently through puberty) — a window of relative under-dosing risk if not actively managed ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1289/)).

---

## 9. Inheritance and Population

**Epidemiology:**
- Overall CPVT (all genetic causes combined) prevalence estimated at **~1:10,000 or less**, though the true prevalence is not firmly established ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1289/); [Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=EN&Expert=3286)).
- *CASQ2*-related (recessive) cases represent a minority subset — roughly **2–5%** of genotyped CPVT (some sources state 1–2%), making CPVT2 itself an ultra-rare disease.
- CPVT overall is implicated in **~12% of autopsy-negative sudden deaths** and **~1.5% of sudden infant deaths** in some series.

**Inheritance pattern:** primarily **autosomal recessive** (biallelic pathogenic variants required for the classic phenotype); however, a clinically important minority of heterozygous carriers manifest a milder/variable CPVT phenotype (apparent semi-dominant/dominant-negative behavior for specific missense alleles), so genetic counseling and clinical screening of heterozygotes is recommended ([Roston et al. 2020, Circulation](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.120.045723); [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1289/)).

**Penetrance:** biallelic *CASQ2* pathogenic variants have been reported as **100% penetrant** in published cohorts (GeneReviews). Heterozygous penetrance is incomplete and variant-dependent (~33% met diagnostic criteria in the largest multicenter series).

**Expressivity:** variable, especially among heterozygotes and even among biallelic carriers (age of onset, event severity vary between families/individuals).

**Genetic anticipation:** not described for CASQ2-CPVT (this is a point-mutation/protein-dysfunction disease, not a repeat-expansion disorder).

**Germline mosaicism:** not specifically documented in the literature surfaced here.

**Founder effects:** well documented — the **D307H founder mutation in a consanguineous Bedouin population** in northern Israel (Lahat et al. 2001) is the paradigm example; additional founder/recurrent variants have been reported in Saudi Arabian and other consanguineous kindreds, and in Chinese and Japanese pediatric cohorts (case reports of homozygous CASQ2 mutations) ([PMC6825949 Chinese cohort](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6825949/); [PMC6341267 Japanese case](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6341267/); [Saudi family](https://pubmed.ncbi.nlm.nih.gov/22650415/)).

**Consanguinity role:** strongly relevant — because CPVT2 is autosomal recessive, it is markedly enriched in populations/kindreds with high consanguinity rates (Bedouin, some Middle Eastern populations), consistent with the founder-mutation pattern above.

**Carrier frequency:** not precisely established population-wide; gnomAD-derived aggregate carrier frequency for presumed-pathogenic CASQ2 alleles is ~0.0997% (collectively), substantially exceeding the expected disease-allele frequency implied by CPVT2's rarity — again pointing to incomplete penetrance of many heterozygous variants rather than an unexpectedly high true carrier rate for fully penetrant recessive alleles.

**Population demographics:**
- **Affected populations:** enriched in consanguineous/founder populations (Bedouin of northern Israel; some Saudi, Chinese, Japanese kindreds reported), but not restricted to any single ethnicity.
- **Geographic distribution:** worldwide,但 with notable founder clusters in the Middle East (Bedouin D307H).
- **Sex ratio:** CPVT overall appears to affect males and females roughly equally; unlike some earlier suggestions that males with RYR2-CPVT face higher SCD risk, more recent data have not confirmed a strong sex-based risk difference. CASQ2-specific sex-ratio data were not identified as distinct from the general CPVT literature in this search.
- **Age distribution:** predominantly pediatric/young-adult presentation (mean first-symptom age 7–12 years), consistent with an early-onset, often more severe phenotype relative to RYR2-CPVT.

---

## 10. Diagnostics

**Clinical diagnostic criteria (EHRA/HRS/APHRS consensus, as applied to CPVT generally, including CASQ2-CPVT):** clinical diagnosis is established in individuals <40 years old with a structurally normal heart, normal resting ECG, and exercise- or emotion-induced polymorphic ventricular premature beats/polymorphic VT/bidirectional VT reproducing symptoms — OR in any individual (regardless of phenotype) found to carry biallelic pathogenic *CASQ2* variants (or a pathogenic RYR2 variant) ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1289/)).

**Clinical tests:**
- **Exercise stress test (EST)** — the gold-standard provocative test; typically the onset of ventricular arrhythmia occurs at a heart rate of ~90–120 bpm. Note: single-test sensitivity is imperfect (repeatability of arrhythmia score is only moderate), so serial/repeat EST is sometimes used for both diagnosis and treatment titration ([PMC12645809 narrative review 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC12645809/); serial EST study).
- **Resting 12-lead ECG** — typically normal (may show sinus bradycardia); used to exclude other channelopathies (long QT, Brugada, ATS).
- **Ambulatory Holter monitoring** — can capture spontaneous ectopy/bidirectional VT, especially during activity.
- **Echocardiography** — used to confirm structurally normal heart (exclusion of cardiomyopathy).
- **Epinephrine/catecholamine provocation testing** — alternative pharmacologic provocation when exercise testing is not feasible.
- **Electrophysiology study** — not typically diagnostic (CPVT arrhythmias are not reliably induced by programmed stimulation), used more for risk stratification/ablation planning in refractory cases.

**Genetic testing:**
- **First-line:** targeted multigene **CPVT panel** — typically covers *RYR2, CASQ2, CALM1, CALM2, CALM3, TRDN, TECRL* (~6–7 genes explaining up to ~75% of clinically diagnosed CPVT) ([Mayo Clinic Labs CPVTG](https://www.mayocliniclabs.com/test-catalog/overview/617211)).
- **Single-gene testing** of *CASQ2* is appropriate when phenotype (early recessive-pattern disease, consanguinity, or known familial variant) suggests CASQ2-CPVT specifically.
- **WES/WGS** may be used when panel testing is uninformative, particularly research-context.
- Chromosomal microarray, karyotyping, FISH, and mitochondrial DNA testing are **not indicated** — this is a single-gene point-mutation disorder without chromosomal or mitochondrial basis.

**Genetic variant interpretation:** ACMG/AMP classification via ClinVar/ClinGen; the ClinGen Cardiovascular Domain Gene Curation Expert Panel has curated CASQ2-CPVT gene-disease validity (HGNC:1513).

**Differential diagnosis:** Long QT syndrome (especially LQT7/Andersen-Tawil syndrome, a recognized clinical phenocopy of CPVT when extracardiac ATS features are subtle/absent), Brugada syndrome (a heterozygous CASQ2 variant has even been reported in a large Brugada-phenotype kindred, indicating some channelopathy phenotypic overlap), idiopathic ventricular fibrillation, short-coupled variant of torsade de pointes, and other causes of exertional syncope (structural cardiomyopathies, coronary anomalies, primary seizure disorders — since CPVT can be misdiagnosed as epilepsy when hypoperfusion produces convulsive syncope) ([MDPI review](https://www.mdpi.com/1422-0067/19/3/692); [Wikipedia CPVT](https://en.wikipedia.org/wiki/Catecholaminergic_polymorphic_ventricular_tachycardia); [PMC11275647 CASQ2-Brugada kindred](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11275647/)).

**Screening:** cascade family screening is essential given autosomal recessive inheritance with reduced heterozygote penetrance — first-degree relatives should undergo exercise stress testing (most sensitive), resting ECG, Holter, echocardiogram, and targeted genetic testing for the known familial variant(s).

---

## 11. Outcome/Prognosis

**Untreated natural history is life-threatening:**
- Mortality up to **~30–50% by age 20–35** if untreated (multiple concordant estimates: 31% by age 30; up to 50% by age 20; 30–50% by age 35) ([search synthesis, multiple concordant sources](https://www.ahajournals.org/doi/pdf/10.1161/JAHA.124.038308)).
- Estimated 4- and 8-year cardiac event rates of **33% and 58% respectively** in cohorts without β-blocker therapy.
- ~30% of patients experience at least one cardiac arrest; up to 80% have ≥1 syncopal episode before diagnosis; sudden death can be the **first manifestation** in previously asymptomatic individuals.
- **CASQ2 (recessive) genotype is associated with earlier onset, more severe phenotype, and higher untreated mortality than RYR2 (dominant) genotype** ([Josephs et al. 2017](https://onlinelibrary.wiley.com/doi/full/10.1002/mgg3.323)).
- Age of first syncope correlates inversely with prognosis — earlier first-syncope age predicts a worse disease course.

**With treatment:** β-blocker therapy (particularly nadolol) markedly reduces mortality; contemporary combination therapy (β-blocker + flecainide ± LCSD ± ICD) further reduces — but does not eliminate — breakthrough arrhythmic events. Long-term (>10 year) follow-up cohorts describe an ongoing, non-trivial residual event rate even under optimized management ([PMC11573199, 10-year follow-up](https://pmc.ncbi.nlm.nih.gov/articles/PMC11573199/)).

**Morbidity:** primarily arrhythmia-related — syncope-associated injury, psychological burden/anxiety, exercise restriction impacting normal childhood/adolescent activity, and the physical/psychological impact of ICD implantation and shocks (including risk of ICD-shock-triggered further arrhythmia in CPVT, a recognized management pitfall).

**Prognostic factors:** genotype (CASQ2 biallelic > CASQ2 heterozygous > general population risk gradient established in the 2020 international multicenter cohort — hazard ratios of 3.2 and 38.8 respectively), age at first symptom, history of cardiac arrest/aborted SCD as index event, adequacy of β-blocker dosing (especially through pubertal growth), and adherence.

---

## 12. Treatment

**Pharmacotherapy (first-line):**
- **Non-selective β-adrenergic blockers** — **nadolol** (1–2.5 mg/kg/day) is considered the most effective agent; non-selective agents (nadolol, propranolol) outperform cardioselective β-blockers ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1289/)). NCIT term: **NCIT:C15986** (Pharmacotherapy) as treatment_term with therapeutic_agent bound to CHEBI (e.g., nadolol CHEBI:7477) or NCIT class term for beta-adrenergic antagonist.
- **Flecainide** (100–300 mg/day, adjunctive) — added when β-blockade alone fails to control arrhythmia on exercise testing; flecainide is thought to act partly via direct RyR2 channel-stabilizing effects beyond its Na⁺-channel blocking action. Recent cohort data associate flecainide use with a lower incidence of arrhythmic events ([Scientia Salut PDF, flecainide cohort](https://scientiasalut.gencat.cat/bitstream/handle/11351/10889/flecainide_is_associated_a_lower_incidence_arrhythmic_events_a_large_cohort_patients_catecholaminergic_polymorphic_ventricular_tachycardia_2023.pdf?sequence=1&isAllowed=y)).

**Interventional/device therapy:**
- **Left cardiac sympathetic denervation (LCSD)** — adjunct for patients with breakthrough life-threatening arrhythmia despite β-blocker + flecainide, or ICD shocks; reduces but does not eliminate residual arrhythmic burden ([PMC3536998](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3536998/)). NCIT candidate: surgical/procedural term (no highly specific NCIT LCSD term identified; general "Surgical Procedure" NCIT:C15329 with therapeutic_modality: SURGERY as fallback).
- **Implantable cardioverter-defibrillator (ICD)** — reserved for arrhythmias not adequately controlled by drug therapy, given known risk that ICD shocks themselves can trigger further catecholamine surge and arrhythmic storm in CPVT (a distinctive management caveat versus other channelopathies). therapeutic_modality: DEVICE.

**Advanced/experimental therapeutics:**
- **AAV-mediated CASQ2 gene replacement therapy** — demonstrated in CASQ2-knockout/knock-in mouse models (single AAV9-CASQ2 delivery cured the arrhythmic phenotype from birth to advanced age) and in patient-derived iPSC-cardiomyocyte models (restored CASQ2 expression, rescued Ca²⁺-transient and DAD abnormalities) ([Circulation 2013 mouse study](https://www.ahajournals.org/doi/10.1161/circulationaha.113.006901); [Cell Death & Disease 2016 iPSC study](https://www.nature.com/articles/cddis2016304)). This is a strong preclinical (MODEL_ORGANISM/IN_VITRO) rationale for gene therapy, with associated patent filings (e.g., US Patents 8859517, 9700636, 10195292, 11173215, "Method of gene transfer for the treatment of recessive catecholaminergic polymorphic ventricular tachycardia (CPVT)") but **no completed human clinical trial identified** in this search — treat as preclinical/experimental only (therapeutic_modality: GENE_THERAPY, NCIT:C15238).
- **Engineered calmodulin constructs for "ryanopathies"** — patent-level preclinical work targeting the broader RyR2-dysfunction disease class (not CASQ2-CPVT-specific human trial data identified).

**Supportive/lifestyle:**
- **Activity restriction** — avoidance of competitive/high-intensity sports is a mainstay of supportive management (behavioral intervention; NCIT:C181743 behavioral counseling / therapeutic_modality: BEHAVIORAL).
- **Genetic counseling** — NCIT:C15240, recommended for probands and at-risk family members given autosomal recessive inheritance with reduced heterozygote penetrance.

**Treatment outcomes/adverse events:** β-blocker non-adherence and under-dosing (especially through pubertal weight gain) are recognized drivers of breakthrough events; ICD shocks carry a specific CPVT-relevant adverse-event profile (catecholamine-surge-induced arrhythmic storm post-shock).

**Treatment algorithm:** stepwise — (1) non-selective β-blocker (nadolol first-line) → (2) add flecainide if breakthrough arrhythmia on serial exercise testing → (3) consider LCSD for continued breakthrough events → (4) ICD reserved for those not adequately controlled by 1–3, used cautiously given shock-triggered arrhythmia risk.

**Clinical trials:** an identified relevant trial is **NCT02927223** ("Atropine in Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)"), investigating the paradoxical/diagnostic use of vagolytic agents in CPVT (general CPVT, not CASQ2-specific) ([clinicaltrials.gov](https://clinicaltrials.gov/study/NCT02927223)).

---

## 13. Prevention

- **Primary prevention:** not possible in the classic sense for a monogenic recessive disease — prevention centers on **genetic counseling and reproductive risk assessment** in consanguineous families/known-carrier couples (25% recurrence risk for biallelic-affected offspring, 50% heterozygous-carrier risk, 25% unaffected/non-carrier per GeneReviews Mendelian recurrence risk).
- **Secondary prevention (early detection):** cascade genetic and clinical (exercise stress test) screening of first-degree relatives of an index case is the principal secondary-prevention strategy, allowing pre-symptomatic identification and prophylactic β-blockade before a first life-threatening event.
- **Tertiary prevention:** the entire pharmacologic/device treatment algorithm above (β-blocker, flecainide, LCSD, ICD) functions as tertiary prevention — preventing sudden death and recurrent events in already-diagnosed individuals.
- **Genetic/reproductive options:** carrier screening in high-consanguinity or founder-mutation populations (e.g., Bedouin community screening for D307H), and prenatal/preimplantation genetic diagnosis are reproductive-option considerations for known-carrier couples, though this search did not surface CPVT2-specific PGD program data.
- **Prophylaxis:** prophylactic β-blockade in genotype-positive, phenotype-negative (asymptomatic) relatives is a recognized preventive strategy given the potential for sudden death as a first presentation.
- **Public health/behavioral:** activity/sports restriction counseling (avoidance of competitive athletics) functions as an ongoing behavioral primary-prevention measure against triggering the first or subsequent events, alongside emergency-preparedness counseling (family CPR/AED training) for at-risk households.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** disease modeling has been performed in *Mus musculus* (NCBITaxon:10090) extensively; guinea pig (*Cavia porcellus*, NCBITaxon:10141) computational/electrophysiological modeling; and human iPSC-derived cardiomyocyte systems.
- **Zebrafish (*Danio rerio*, NCBITaxon:7955):** casq2 and ryr2b orthologs are expressed in zebrafish heart, but **no zebrafish model has yet reported CASQ2-linked cardiac arrhythmias** specifically (unlike the well-characterized *tremblor* mutant, which is an *ncx1*-related Ca²⁺-handling arrhythmia model, not CASQ2) ([PMC8779270 zebrafish arrhythmia review](https://pmc.ncbi.nlm.nih.gov/articles/PMC8779270/)).
- **Naturally occurring canine/other veterinary CASQ2-CPVT:** this search did **not** identify confirmed naturally occurring CASQ2-CPVT in dogs (e.g., German Shepherd inherited sudden death, a well-known distinct polygenic canine arrhythmia syndrome, does not appear to be CASQ2-linked based on available search results) or other companion/livestock species. No OMIA entry was surfaced confirming a natural CASQ2 veterinary disease — this should be treated as **not established** rather than affirmatively absent, pending a dedicated OMIA search.
- **Gene orthology:** mouse *Casq2* (MGI:1309469) is the standard ortholog used in genetic (knockout/knock-in/point-mutant) modeling.
- **Comparative pathology:** the fundamental Ca²⁺-handling/RyR2-CASQ2-triadin macromolecular complex is highly conserved across vertebrate cardiac muscle, supporting strong translational validity of mouse and iPSC models for the core arrhythmogenic mechanism, though whole-organism phenotype penetrance/timing (e.g., late hypertrophy at 35 weeks in mice) may not map precisely onto human disease timelines.

---

## 15. Model Organisms

- **Mouse models (primary model system):**
  - **Casq2 knockout (null) mice** — under resting conditions, **100% of Casq2-null mice** exhibit bidirectional ventricular tachycardia (versus 0% in WT), closely recapitulating the human resting-bradycardia-plus-stress-induced-bidirectional-VT phenotype ([Circulation 2013 AAV rescue study](https://www.ahajournals.org/doi/10.1161/circulationaha.113.006901)).
  - **Casq2-D307H knock-in mice** — recapitulate impaired SR Ca²⁺ handling and complex ventricular arrhythmias, directly modeling the human Bedouin founder mutation ([PMC2717009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2717009/)).
  - **Conditional ablation/rescue (cell-type- and developmentally-controlled) Casq2 models** — used to dissect the developmental timing and cell-type specificity (cardiomyocyte-restricted) requirement for Casq2 in producing the CPVT2 phenotype ([Human Molecular Genetics 2018](https://academic.oup.com/hmg/article/27/9/1533/4857233)).
  - **CRISPR/Cas9-generated novel CPVT mouse models** — recent efforts to generate additional Casq2 (and related) mutant lines for mechanistic study ([bioRxiv 2021](https://www.biorxiv.org/content/10.1101/2021.10.14.464343.full.pdf)).
  - **Phenotype recapitulation:** excellent for the core electrophysiological phenotype (resting bradycardia, exercise/catecholamine-induced bidirectional VT); models also reveal late (35-week) cardiac hypertrophy/LV dysfunction not yet fully characterized as a human correlate.
  - **Limitations:** murine cardiac electrophysiology (heart rate, ion channel repertoire) differs quantitatively from human; late structural remodeling seen in mice is not yet confirmed as a robust human CASQ2-CPVT feature (a candidate `HUMAN_MODEL_MISMATCH` consideration for dismech curation).
  - **AAV gene-therapy rescue in mice:** single neonatal or even adult AAV9-mediated CASQ2 gene delivery to knock-in mice normalized the arrhythmic phenotype "from birth to advanced age," a key translational proof-of-concept ([Circulation 2013](https://www.ahajournals.org/doi/10.1161/circulationaha.113.006901)).

- **Human iPSC-derived cardiomyocyte (iPSC-CM) models:**
  - Patient-specific iPSC-CMs carrying homozygous CASQ2-D307H or CASQ2-G112+5X mutations recapitulate decreased Ca²⁺ transient amplitude, elevated diastolic Ca²⁺, delayed afterdepolarizations, oscillatory prepotentials, and after-contractions — a strong IN_VITRO human-cell-based model with direct disease-mechanism concordance to the mouse/RyR2 literature ([PMC4549051](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4549051/); [Cell Death & Disease 2016](https://www.nature.com/articles/cddis2016304)).
  - AAV-CASQ2 gene delivery to these iPSC-CMs rescues the functional Ca²⁺-handling and DAD defects, mirroring the mouse gene-therapy rescue data and strengthening translational confidence.

- **Computational/in silico models:**
  - A guinea-pig ventricular myocyte computational model has been used to dissect pacing-rate-dependent arrhythmogenic mechanisms specific to the CASQ2-G112+5X mutation, representing a COMPUTATIONAL evidence-source complement to the wet-lab models ([PMC9858930](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9858930/)).

- **Resources:** MGI (Casq2, MGI:1309469) for mouse allele/phenotype data; no dedicated ZFIN CASQ2 arrhythmia model identified; IMPC/KOMP not specifically searched for a validated Casq2 line in this pass.

---

## Summary of Key Citations (PMIDs and identifiers referenced or implied)

- Lahat H et al. 2001 — Bedouin D307H founder mutation (OMIM 114251/611938 primary reference)
- Postma AV et al. / Viatchenko-Karpinski S et al. — RYR2 and CASQ2 mutation comparative clinical series (Circulation)
- di Barletta MR et al. 2006 — Clinical phenotype and functional characterization of CASQ2 mutations (Circulation 2006;114:1012, PMID 16908766)
- Knollmann BC et al. 2006 — Casq2 point mutation impairs SR Ca²⁺ handling in mice (JCI 2006, PMID for JCI article 31080)
- Song L et al. 2007 — CASQ2 mutations increase calreticulin/RyR2 expression (JCI, PMID 17607358)
- Josephs K et al. 2017 — Compound heterozygous CASQ2 mutations, long-term course (Mol Genet Genomic Med, PMID 29178653)
- Roston TM et al. 2020 — International Multicenter Evaluation of Inheritance Patterns, Arrhythmic Risks, and Underlying Mechanisms of CASQ2-CPVT (Circulation 2020;142:2005)
- GeneReviews — Catecholaminergic Polymorphic Ventricular Tachycardia (NBK1289), Roston/Sanatani et al., updated periodically
- Priori SG, Napolitano C et al. — foundational CPVT clinical/genetic reviews
- Chen et al. — CASQ2 variants in Chinese children with CPVT (PMC6825949)
- Faggioni M, Kryshtal DO, Knollmann BC — mechanistic reviews on calstabin/RyR2 phosphorylation and DAD generation

All specific numeric claims above should be independently re-verified against cached PubMed abstracts (via `just fetch-reference PMID:XXXX`) before being committed as dismech evidence snippets, per this repository's evidence SOP — this report is a research synthesis and lead list, not pre-verified curation-ready evidence.

**Sources:**
- [OMIM #611938 — CPVT2](https://omim.org/entry/611938)
- [OMIM *114251 — CASQ2](https://omim.org/entry/114251)
- [GeneReviews — Catecholaminergic Polymorphic Ventricular Tachycardia (NBK1289)](https://www.ncbi.nlm.nih.gov/books/NBK1289/)
- [Orphanet — CPVT (ORPHA3286)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=EN&Expert=3286)
- [Roston et al. 2020, Circulation — International Multicenter CASQ2-CPVT study](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.120.045723)
- [Josephs et al. 2017, Mol Genet Genomic Med — Compound heterozygous CASQ2](https://onlinelibrary.wiley.com/doi/full/10.1002/mgg3.323)
- [di Barletta et al. 2006, Circulation — Clinical Phenotype and Functional Characterization](https://www.ahajournals.org/doi/10.1161/circulationaha.106.623793)
- [Knollmann/Song, JCI 2006 — Calsequestrin mutations increase calreticulin/RyR2](https://www.jci.org/articles/view/31080)
- [Circulation 2013 — AAV-mediated CASQ2 gene transfer in knock-in mice](https://www.ahajournals.org/doi/10.1161/circulationaha.113.006901)
- [Cell Death & Disease 2016 — AAV-CASQ2 rescue in patient-specific iPSC model](https://www.nature.com/articles/cddis2016304)
- [PMC7666291 — Molecular adaptation to CASQ2 R33Q and D307H mutants](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7666291/)
- [PMC4549051 — Functional abnormalities in iPSC-CMs from CPVT1/CPVT2 patients](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4549051/)
- [PMC2717009 — CASQ2-D307H knock-in mouse model](https://pmc.ncbi.nlm.nih.gov/articles/PMC2717009/)
- [Human Molecular Genetics 2018 — Conditional Casq2 ablation/rescue models](https://academic.oup.com/hmg/article/27/9/1533/4857233)
- [PMC9858930 — Guinea pig computational model of CASQ2-G112+5X](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9858930/)
- [PMC6825949 — CASQ2 variants in Chinese children with CPVT](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6825949/)
- [PMC6341267 — Homozygous CASQ2 mutation, Japanese patient](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6341267/)
- [PubMed 22650415 — CASQ2 mutation in a Saudi family](https://pubmed.ncbi.nlm.nih.gov/22650415/)
- [PMC11275647 — CASQ2 variant causing Brugada syndrome phenotype](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11275647/)
- [PMC3536998 — Left cardiac sympathetic denervation in CPVT/LQTS](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3536998/)
- [Flecainide cohort study 2023 (Scientia Salut repository PDF)](https://scientiasalut.gencat.cat/bitstream/handle/11351/10889/flecainide_is_associated_a_lower_incidence_arrhythmic_events_a_large_cohort_patients_catecholaminergic_polymorphic_ventricular_tachycardia_2023.pdf?sequence=1&isAllowed=y)
- [PMC12645809 — CPVT narrative review 2024/2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12645809/)
- [MDPI 2024 — CPVT clinical characteristics, diagnosis, therapy review](https://www.mdpi.com/2077-0383/13/6/1781)
- [Mayo Clinic Labs — CPVT gene panel (CPVTG)](https://www.mayocliniclabs.com/test-catalog/overview/617211)
- [NCBI Gene — CASQ2 (Gene ID 845)](https://www.ncbi.nlm.nih.gov/gene/845)
- [GeneCards — CASQ2](https://www.genecards.org/card/CASQ2)
- [Wikipedia — Calsequestrin](https://en.wikipedia.org/wiki/Calsequestrin)
- [Wikipedia — Catecholaminergic polymorphic ventricular tachycardia](https://en.wikipedia.org/wiki/Catecholaminergic_polymorphic_ventricular_tachycardia)
- [ClinicalTrials.gov NCT02927223 — Atropine in CPVT](https://clinicaltrials.gov/study/NCT02927223)
- [NBK583118 — Founder variants common in the Bedouin population](https://www.ncbi.nlm.nih.gov/books/NBK583118/)