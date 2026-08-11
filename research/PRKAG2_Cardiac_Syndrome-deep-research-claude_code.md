---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T16:57:40.889922'
end_time: '2026-07-31T17:03:00.802269'
duration_seconds: 319.91
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: PRKAG2 Cardiac Syndrome
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
  - claude-sonnet-5
  web_search_requests: 22
  num_turns: 35
  total_cost_usd: 2.0259423
  session_id: 1ff1ab7e-d42a-5ad6-b222-89444922f8c7
  stop_reason: end_turn
citation_count: 19
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PRKAG2 Cardiac Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PRKAG2 Cardiac Syndrome** covering all of the
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

# PRKAG2 Cardiac Syndrome — Comprehensive Research Report

## 1. Disease Information

### Overview
PRKAG2 cardiac syndrome (also called PRKAG2 syndrome, PRKAG2 cardiomyopathy, or glycogen-storage cardiomyopathy) is a rare, autosomal dominant, non-lysosomal glycogen storage disease of the heart caused by activating mutations in *PRKAG2*, the gene encoding the regulatory γ2 subunit of AMP-activated protein kinase (AMPK). It is a genocopy/phenocopy of sarcomeric hypertrophic cardiomyopathy (HCM): patients present with left ventricular hypertrophy (LVH) that is caused not by sarcomeric protein dysfunction but by massive intramyocyte glycogen accumulation. The disease's defining clinical triad is **cardiac hypertrophy, ventricular pre-excitation (Wolff-Parkinson-White syndrome, WPW), and progressive cardiac conduction system disease** ([Gollob et al., NEJM 2001, PMID:11407343](https://pubmed.ncbi.nlm.nih.gov/11407343/); [Arad et al., Circulation 2003, PMID:12782567](https://pubmed.ncbi.nlm.nih.gov/12782567/)).

### Key Identifiers
- **Gene:** PRKAG2 (HGNC:9385), chromosome 7q36.1 (candidate region originally mapped as 7q34–q36)
- **OMIM gene:** *602743 – Protein Kinase, AMP-Activated, Gamma-2 Non-Catalytic Subunit; PRKAG2*
- **OMIM phenotypes:**
  - **#194200** – Wolff-Parkinson-White syndrome (WPW), familial, PRKAG2-related
  - **#261740** – Glycogen Storage Disease of Heart, Lethal Congenital (severe infantile/neonatal form)
  - (Some literature also cross-references the entry historically as "familial hypertrophic cardiomyopathy 6 / CMH6" phenotype territory, though the modern preferred label is PRKAG2 cardiac syndrome/PRKAG2 syndrome)
- **MONDO:** A specific PRKAG2-cardiac-syndrome MONDO term was not confidently resolved via search in this pass — verify with `runoak -i sqlite:obo:mondo search` before curation (candidate: search terms "PRKAG2 syndrome" / "glycogen storage disease of heart" in MONDO).
- **ICD-10:** Falls generically under I42.- (Cardiomyopathy); no PRKAG2-specific ICD-10 code exists.
- **Orphanet:** Orphanet lists "PRKAG2 cardiac syndrome" as a distinct entity — verify ORPHA number via `just fetch-reference ORPHA:<code>` lookup or Orphadata search before citing.

### Synonyms
- PRKAG2 syndrome (PS)
- PRKAG2 cardiomyopathy
- Cardiac glycogenosis due to PRKAG2 mutation / PRKAG2-related glycogen storage cardiomyopathy
- Familial Wolff-Parkinson-White syndrome with cardiac hypertrophy
- Glycogen storage disease of the heart (lethal congenital form, for the severe neonatal phenotype)
- WPW syndrome, familial, with or without cardiomyopathy

### Evidence Basis
Nearly all data are aggregated disease-level resources: OMIM entries, multicenter/multinational retrospective cohort studies (the largest being a 27-center, 90-subject natural history study — [Thevathasan et al., JACC 2020, PMID:32646569](https://pubmed.ncbi.nlm.nih.gov/32646569/)), single/multi-family pedigree case series, and transgenic/iPSC model-organism mechanistic studies. No large-scale population EHR studies exist owing to disease rarity.

---

## 2. Etiology

### Disease Causal Factors
PRKAG2 cardiac syndrome is a monogenic, Mendelian disorder. It is caused by heterozygous, dominant, **gain-of-function (constitutively activating) missense mutations** in *PRKAG2*, which encodes the γ2 regulatory subunit of AMPK — a heterotrimeric (α/β/γ) serine/threonine kinase that is the master sensor of cellular energy status (AMP:ATP ratio). There is no known environmental, infectious, or purely multifactorial etiology; this is a purely genetic cardiomyopathy.

### Genetic Risk Factors
- **Causal variants** cluster in the **cystathionine-β-synthase (CBS) domains** of the γ2 subunit, which form two tandem Bateman domains that bind AMP/ADP/ATP competitively and allosterically regulate kinase activity:
  - **R302Q** (CBS1 domain) — the single most frequently reported variant, seen across many unrelated families/geographic cohorts (South Asian cohort of 22 patients all carrying R302Q — [PMID:33244021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7691361/))
  - **H383R** — associated with a more severe phenotype, including pediatric/antenatal presentations
  - **T400N** — CBS2 domain; mouse-model workhorse mutation, myocyte vacuolation with minimal fibrosis
  - **N488I** — linker region between CBS domains; the principal transgenic-mouse disease model mutation
  - **R531Q/R531G** — CBS3 domain; the recurrent mutation causing the **lethal congenital/neonatal form** (OMIM #261740) — biochemically shows >100-fold reduced AMP/ATP binding affinity but enhanced basal kinase activity ([related ClinVar/OMIM entries](https://omim.org/entry/261740))
  - **K290I/K291I** (nomenclature varies slightly by transcript numbering across papers) — large Brazilian kindred, 66 members studied over 18 years, 19 carriers ([PMID:39082507](https://pmc.ncbi.nlm.nih.gov/articles/PMC11239200/))
  - Additional reported variants: L341S, H401Q, V336I (Val336Ile), G75A, P198R, H222R, S143= (silent, pathogenic via splicing)
- **De novo mutations** occur and are reported to cause particularly early-onset, severe heart failure ([PLOS ONE, PMC3669303](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3669303/)).
- No established genetic **protective factors** or modifier alleles are described in the literature to date; no GWAS-identified susceptibility loci exist (this is fully penetrant-monogenic, not polygenic/complex).

### Environmental Risk Factors
None established — this is a purely genetic disorder. No toxin, lifestyle, or occupational exposure has been implicated as causal. Age and sex are relevant only insofar as disease expression is age-dependent (see Temporal Development, §8) — the largest natural history cohort found a slight male predominance in several cohorts (e.g., South Asian cohort 68% male).

### Protective Factors
None specific to the disease etiology are documented. At the mechanistic/experimental level, pharmacologic and genetic **normalization of AMPK signaling** is protective in animal models (see Mechanism, §6, and Treatment, §12) — e.g., transgene suppression (tetracycline-repressible system) reverses cardiomyopathy in mice ([Wolf et al., Circulation 2008, PMID:18158359](https://pmc.ncbi.nlm.nih.gov/articles/PMC2957811/)), and co-expression of a dominant-negative α2-AMPK subunit partially/completely normalizes the phenotype in compound-heterozygous mice, implicating the α2 catalytic subunit as the principal disease-mediating partner.

### Gene-Environment Interactions
No documented gene-environment interaction data exist for PRKAG2 syndrome; disease expression appears to be driven by genotype (which specific CBS-domain mutation) and, secondarily, by age/developmental stage rather than by identified external modifiers.

---

## 3. Phenotypes

### Cardiac Phenotypes (symptoms/signs, per Thevathasan et al. 2020, PMID:32646569, n=90, 27 centers, median follow-up 6 years)

| Phenotype | Frequency (baseline → follow-up) | Suggested HP term* |
|---|---|---|
| Left ventricular hypertrophy | 67% → 71% | HP:0001712 (Left ventricular hypertrophy) — verify |
| Ventricular pre-excitation / WPW | ~33% at baseline (30/90 with pre-excitation or prior AP ablation) | HP:0001716 (Wolff-Parkinson-White syndrome) — verify |
| Atrial fibrillation | 18% → 29% | (Atrial fibrillation HP term — verify) |
| Need for de novo pacemaker | 19% baseline pacemakers (median implant age 36y) → 21% additional by follow-up | (Atrioventricular block / Sinus node dysfunction HP terms — verify) |
| Heart failure hospitalization | — → 14% | — |
| Sudden cardiac death / equivalent | — → 8% | — |
| Heart transplantation | — → 4% | — |
| Death (all-cause) | — → 13% | — |

South Asian R302Q cohort (n=22, PMID:33244021): LVH 86%, WPW pattern 77%, pacemaker 36%, AF 14%, SCD 27% — illustrating substantial genotype/cohort-dependent variability.

Symptom presentation frequently includes palpitations (~48% in some case series), syncope/pre-syncope, chest pain/angina, exertional dyspnea, and progressive systolic dysfunction (eccentric LV hypertrophy pattern, contrasting with the concentric/asymmetric septal pattern typical of sarcomeric HCM).

### Extracardiac Phenotypes
- **Neurocognitive/psychiatric:** learning disability, intellectual disability, anxiety, aggression, mood disturbance, speech disorder — reported "only in carriers of mutations" in the Brazilian K290I/K291I kindred ([PMID:39082507](https://pmc.ncbi.nlm.nih.gov/articles/PMC11239200/)).
- **Obstetric:** increased spontaneous abortion, premature/neonatal death, forceps deliveries, and cesarean deliveries reported in affected female carriers in the same kindred (mechanistically unexplained; possibly reflects placental AMPK expression, since AMPK is highly expressed in placenta).
- **Skeletal muscle:** AMPK is expressed in skeletal muscle and glycogen storage/myopathy has been reported in some case reports, but this is not consistently observed across cohorts (absent in the Brazilian cohort).
- **Pseudotumor cerebri** reported in at least one case ([PMID:29298659](https://pubmed.ncbi.nlm.nih.gov/29298659/)) — likely incidental/anecdotal rather than a core feature.
- **Sensorineural hearing loss:** not substantiated in the literature reviewed here (searched specifically; no clear supporting citation found) — do not curate without a direct source.
- **Hepatic involvement:** at least one case report describes PRKAG2 variant presenting with liver cirrhosis in a family ([BMC Med Genomics, PMC7845137](https://pmc.ncbi.nlm.nih.gov/articles/PMC7845137/)) — AMPK is expressed in liver; this appears to be a rare/atypical presentation and should be treated as a single-family observation, not a core phenotype.

### Phenotype Characteristics
- **Age of onset:** Highly variable — from lethal congenital/neonatal-onset (severe R531Q-type mutations) through childhood-onset WPW (often the earliest sign, sometimes without LVH) to adult-onset progressive LVH/conduction disease (median age at cohort entry ~33–39 years across studies).
- **Severity/progression:** Progressive — LVH and conduction disease worsen over time; pre-excitation may be an early, isolated finding that precedes hypertrophy by years. The disease is explicitly noted to progress toward a "burned-out phase" resembling dilated cardiomyopathy/advanced heart failure in some patients ([Circ Heart Failure 2024 case report](https://www.ahajournals.org/doi/10.1161/CIRCHEARTFAILURE.124.012047)).
- **Penetrance:** Age-dependent and incomplete at young ages — one cohort reported penetrance of only 31% by age ≤40 years, rising to 76% of patients showing signs/symptoms by end of follow-up, despite fully penetrant genotype-carrier status ultimately expected with dominant inheritance.

### Quality of Life Impact
Not systematically quantified with standard instruments (EQ-5D/SF-36) in the literature surveyed; impact is inferred from the high burden of pacemaker implantation at young ages (median 36 years), heart failure hospitalization, and premature mortality/SCD risk — all of which substantially affect functional status and psychosocial burden, compounded by the reported neurocognitive/psychiatric extracardiac features in at least one large kindred.

*Note: HP term IDs above should be independently verified with `runoak -i sqlite:obo:hp info <ID> -O obo` per dismech's anti-hallucination policy before being committed to a KB entry — this report flags them as unverified suggestions only.

---

## 4. Genetic/Molecular Information

### Causal Gene
**PRKAG2** — HGNC:9385, chromosome 7q36.1, encodes the γ2 regulatory subunit of AMP-activated protein kinase (AMPK). OMIM gene entry *602743.

### Pathogenic Variant Classes and Structural/Functional Consequences
Missense mutations cluster in the **two tandem Bateman domains (four CBS repeats)** that form the nucleotide-sensing regulatory module of γ2:
- **R302Q (CBS1):** computational modeling suggests decreased ATP-binding affinity ([eBioMedicine, Yang et al. 2020](https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(20)30098-0/fulltext) — direct abstract text not retrievable in this session, cite with caution and re-verify before use)
- **H383R, T400N (CBS2):** alter orientation of adjacent H383/R531 residues, altering nucleotide binding
- **N488I** (linker) **and L341S:** cause structural instability in the Bateman domain, disrupting intramolecular (CBS-domain) autoinhibitory regulation
- **R531Q (CBS3):** >100-fold reduced AMP/ATP binding affinity but *enhanced basal kinase activity* and increased α-subunit phosphorylation — the mechanistic basis for the most severe, lethal congenital phenotype

**Net functional consequence:** all disease-causing variants are **gain-of-function / constitutively activating** with respect to AMPK signaling (chronic/inappropriate AMPK activation), rather than loss-of-function — this is the opposite direction from what might be assumed for a "regulatory subunit mutation," and is a key mechanistic point.

- **Variant classification (ACMG/ClinVar):** Most well-established variants (R302Q, N488I, T400N, H383R, R531Q) are classified Pathogenic/Likely Pathogenic in ClinVar under both the WPW (#194200) and lethal congenital glycogen storage disease (#261740) phenotype associations.
- **Allele frequency:** These variants are essentially absent or present only as extreme rarities in population databases (gnomAD) consistent with a highly penetrant, severe autosomal dominant Mendelian disease under purifying selection — exact gnomAD allele counts were not retrieved in this search pass and should be confirmed directly in gnomAD before citing specific frequencies.
- **Somatic vs. germline:** Germline only; no somatic/mosaic PRKAG2 cardiac disease is described.
- **Modifier genes:** None firmly established in humans; in mice, co-expression of a dominant-negative AMPK **α2** catalytic subunit transgene substantially rescues the γ2-N488I phenotype, implicating α2 as a key downstream modifier/mediator (not yet translated to a human modifier-gene finding).

### Epigenetic Information
No disease-specific DNA methylation, histone modification, or chromatin-level studies specific to PRKAG2 syndrome were identified in this search pass.

### Chromosomal Abnormalities
None — this is a single-gene missense-mutation disorder; no relevant aneuploidy, translocation, or CNV mechanism is described.

---

## 5. Environmental Information
No specific environmental toxin, occupational exposure, dietary factor, or infectious trigger is implicated in PRKAG2 cardiac syndrome onset or severity in the literature reviewed. This section is not substantially applicable for this purely monogenic disorder.

---

## 6. Mechanism / Pathophysiology

### Causal Chain (Molecular → Cellular → Tissue → Organ)

1. **Trigger (molecular):** Germline missense mutation in a CBS domain of AMPK γ2 subunit → loss of normal AMP/ADP/ATP-dependent allosteric inhibition of the α-catalytic subunit → **constitutive/inappropriate activation of AMPK** even under normal cellular energy (ATP-replete) conditions.
2. **Molecular consequence:** Chronically active AMPK phosphorylates and activates downstream effectors of glucose uptake and glycogen synthesis, notably **glycogen synthase** and **AS160/TBC1D4** (regulator of GLUT4 translocation) — "Acute expression of gamma(2)R302Q induces AMPK activation and upregulation of glycogen synthase and AS160, with an associated increase in glycogen content" ([PMID:20031621](https://pubmed.ncbi.nlm.nih.gov/20031621/)). Notably, AMPK activity and glycogen content show a complex, partly inverse relationship over time, suggesting feedback dysregulation rather than simple linear causation.
3. **Cellular consequence:** Cardiomyocytes accumulate massive, membrane-bound, non-lysosomal glycogen deposits ("vacuolated myocytes") — in the N488I transgenic mouse model, cardiac glycogen reached ~30-fold above normal levels ([Arad et al., Circulation 2003, PMID:12782567](https://pubmed.ncbi.nlm.nih.gov/12782567/)). Metabolically, mutant cardiomyocytes (iPSC-CM models) show reduced glycolytic function, increased maximal mitochondrial respiration with elevated mitochondrial content, increased lipid storage, and altered redox regulation ([Cell Reports, PIIS2211-1247(16)31640-0](https://www.cell.com/cell-reports/fulltext/S2211-1247(16)31640-0)).
4. **Tissue consequence — mechanism of ventricular pre-excitation (WPW):** Glycogen-filled myocytes physically **disrupt the annulus fibrosus**, the normal fibrous insulating ring that electrically isolates the atria from the ventricles. This produces **anomalous microscopic atrioventricular myocardial connections** — rather than a single discrete morphologically distinct accessory bypass tract as in idiopathic WPW — providing the anatomic substrate for ventricular pre-excitation ([Arad et al. 2003, PMID:12782567](https://pubmed.ncbi.nlm.nih.gov/12782567/); the same authors note this mechanism likely generalizes to pre-excitation seen in other glycogen-storage cardiomyopathies such as Pompe and Danon disease).
5. **Organ consequence:** Progressive glycogen-driven myocyte hypertrophy and vacuolation → left ventricular hypertrophy (eccentric pattern, distinct from sarcomeric HCM's typical asymmetric septal hypertrophy with myofiber disarray) → progressive degeneration of the cardiac conduction system (sinus node dysfunction, AV block) → arrhythmia (WPW-mediated SVT, atrial fibrillation, ventricular tachyarrhythmia) → heart failure / sudden cardiac death.

### Key Distinguishing Histopathology
"PRKAG2 syndrome is defined by vacuolated myocytes with glycogen deposits, **minimal fibrosis**, and **absence of sarcomeric disarray**" — a critical differentiator from sarcomeric HCM (myofiber disarray + fibrosis) on endomyocardial biopsy.

### Reversibility (mechanistic proof-of-concept)
Using an inducible, tetracycline-repressible transgenic N488I mouse model, suppression of mutant AMPK expression (at various developmental time points, including prenatally) reduced cardiac glycogen content and **reversed** the cardiomyopathy, pre-excitation, and conduction system degeneration phenotypes ([Wolf et al., Circulation 2008, PMID:18158359](https://pmc.ncbi.nlm.nih.gov/articles/PMC2957811/)) — direct causal evidence that ongoing AMPK hyperactivity (not just a fixed developmental lesion) drives the phenotype, and that the disease could in principle be therapeutically targetable.

### Molecular Pathways / GO Suggestions (verify before curation)
- **Molecular function:** AMP-activated protein kinase activity (GO:0004679, protein serine/threonine kinase activity variant — verify exact ID)
- **Biological process:** glycogen biosynthetic process (GO:0005978); positive regulation of glycogen biosynthetic process; cellular response to AMP; regulation of AMP-activated protein kinase activity
- **Cellular component:** AMP-activated protein kinase complex (GO:0031588)

### Cell Types / Anatomical Involvement (CL/UBERON suggestions, verify before curation)
- Cardiac muscle cell / cardiomyocyte (CL:0000746)
- Cardiac conduction system myocyte (sinoatrial node cell, atrioventricular node cell)
- UBERON: myocardium (UBERON:0002349), annulus fibrosus of heart / cardiac skeleton, atrioventricular node, sinoatrial node

### Molecular Profiling / Omics
- iPSC-CM transcriptomic/metabolomic studies show remodeling of gene expression favoring glycogen storage and oxidative metabolism over glycolysis in mutant cells.
- AMPK activator **metformin** treatment of PRKAG2-mutant iPSC-CMs normalized oxygen consumption rate parameters, "eliminating the bioenergetic abnormalities" — an intriguing but counterintuitive finding (since AMPK is already overactive) suggesting complex/paradoxical pharmacology in this model (Frontiers Cardiovasc Med, PRKAG2 iPSC-CM WPW study).
- Integrative iPS/microtissue analysis identifies AMPK as a broader "regulator of metabolism, survival, and fibrosis" with implications extending to other cardiomyopathies (Cell Reports 2016).

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary:** Heart (ventricular myocardium, atrioventricular conduction axis, sinoatrial node, atrioventricular node, annulus fibrosus/cardiac fibrous skeleton, atria — atrial lesions also reported in pedigree studies, [PMC8960295](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8960295/))
- **Secondary:** Skeletal muscle (glycogen storage, variably reported), liver (rare reports of cirrhosis in one kindred), central nervous system (neurocognitive/psychiatric features in at least one large kindred)
- **Body systems:** Cardiovascular system predominant; possible musculoskeletal, hepatic, and neuropsychiatric secondary involvement (heterogeneously reported, not core/universal features)

### Tissue and Cell Level
- Cardiac/striated muscle tissue — vacuolated cardiomyocytes with intracytoplasmic, non-membrane-bound (non-lysosomal) glycogen deposits
- Cardiac conduction tissue — nodal and junctional myocytes disrupted by glycogen infiltration

### Subcellular Level
- Cytoplasm (glycogen granule accumulation — non-lysosomal, distinguishing from Pompe disease's lysosomal glycogen storage)
- Mitochondria (increased mitochondrial content/respiration reported in iPSC-CM models)
- GO Cellular Component candidates: cytoplasm, glycogen granule, mitochondrion — verify specific terms before curation

### Localization
- Bilateral/global cardiac involvement (not lateralized); LVH typically eccentric rather than the asymmetric septal pattern of sarcomeric HCM.

---

## 8. Temporal Development

### Onset
- **Congenital/neonatal (lethal form):** R531Q and similar highly-activating CBS3 mutations cause massive cardiomegaly with cardiac/respiratory distress at birth, death typically between 3 weeks and 5 months of age (OMIM #261740).
- **Childhood:** Isolated ventricular pre-excitation (WPW) without hypertrophy has been reported as an early/pediatric presentation, preceding overt cardiomyopathy by years ([Circulation, "Novel PRKAG2 Mutation... Childhood Onset and Absence of Cardiac Hypertrophy"](https://www.ahajournals.org/doi/10.1161/hc5001.102111)).
- **Adult:** Most large cohorts show median age at diagnosis/enrollment in the 30s–40s, with progressive LVH, conduction disease, and pacemaker requirement (median implant age 36 years).

### Progression
- Generally **progressive**: LVH prevalence increases over follow-up (67%→71% over ~6 years in the largest cohort), AF increases (18%→29%), pacemaker need accrues over time.
- Disease course is described as capable of culminating in a **"burned-out phase"** resembling dilated/advanced heart failure.
- Progression rate is genotype-dependent — some mutations (e.g., R531Q, H383R) cause rapid, severe/lethal early progression; others (e.g., some R302Q-associated presentations) show slower, adult-onset progression.

### Patterns
- No spontaneous remission is described; disease is chronic and lifelong once manifest.
- Reversibility has only been demonstrated experimentally (transgene suppression in mice), not yet in human therapeutics.
- No clearly defined "critical window" for intervention has been established in humans, though the mouse reversibility data (including prenatal suppression) suggest a rationale for early intervention if disease-modifying therapy becomes available.

---

## 9. Inheritance and Population

### Epidemiology
- **True population prevalence is unknown / not well characterized** — this is an ultra-rare disease.
- Among patients evaluated for suspected hypertrophic cardiomyopathy, PRKAG2 variants are estimated at **~0.23–1%** prevalence.
- Prevalence rises to as much as **29%** in the specific subgroup of patients presenting with both LVH *and* pre-excitation — a much higher pretest probability subgroup for genetic testing.
- One older estimate (Murphy et al.) put prevalence at ~1% among patients with combined HCM and premature sinoatrial/AV conduction disease.
- The disease is considered **underdiagnosed** given phenotypic overlap with sarcomeric HCM and other glycogen storage cardiomyopathies.

### Inheritance Pattern
**Autosomal dominant.** De novo mutations are also reported (causing early-onset severe disease in the absence of family history).

### Penetrance
Age-dependent and incomplete at young ages: one cohort reported only 31% penetrance by age 40, rising to 76% of genotype-positive individuals showing signs/symptoms by end of follow-up. This nuances the "full penetrance" label sometimes applied and has direct implications for family screening/surveillance intervals.

### Expressivity
Highly variable — even within the same family/same variant, phenotype severity ranges from isolated pre-excitation without hypertrophy to lethal neonatal cardiomyopathy, and genotype-phenotype correlations (e.g., R531Q → lethal congenital form; H383R → severe pediatric/antenatal form; R302Q → variable adult-onset spectrum) are only partially predictive.

### Genetic Anticipation
Not established/reported as a feature of this disease (unlike repeat-expansion disorders).

### Germline Mosaicism
Not specifically documented in the literature reviewed; de novo cases are described but germline mosaicism specifically is not detailed.

### Founder Effects
Not clearly established as a global founder phenomenon, though recurrent large single-family/single-population cohorts (e.g., the South Asian family cohort all sharing R302Q, the Brazilian kindred sharing K290I/K291I) suggest regional/familial founder-type recurrence rather than true independent recurrent mutation in every case — this needs formal haplotype study to confirm.

### Consanguinity Role
Not implicated — autosomal dominant disease does not require biallelic inheritance; no consanguinity association reported.

### Population Demographics
- Reported cohorts span South Asian, Brazilian, Chinese, and Caucasian/European-ancestry families — the disease is not confined to a single ethnic group.
- Slight male predominance noted in some cohorts (e.g., 68% male in the South Asian cohort; 53% men in the largest natural history cohort), though this may partly reflect referral/ascertainment bias rather than true sex-linked penetrance difference (the gene is autosomal, not X-linked).
- Sudden cardiac death risk in young patients (<40 years) has been cited as high as ~20% in some early WPW-focused cohorts.

---

## 10. Diagnostics

### Clinical Tests
- **ECG:** Short PR interval, delta wave (ventricular pre-excitation/WPW pattern); progressive PR prolongation and AV block over time; sinus node dysfunction/chronotropic incompetence.
- **Echocardiography:** LVH, typically eccentric pattern (vs. asymmetric septal in sarcomeric HCM); reduced EF in advanced/"burned-out" cases.
- **Cardiac MRI:** Used to characterize myocardial tissue in PRKAG2 mutation carriers ([PMC4619453](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4619453/)) — helps differentiate from sarcomeric HCM (e.g., late gadolinium enhancement/fibrosis patterns may differ given the "minimal fibrosis" histopathology).
- **Endomyocardial biopsy:** Vacuolated myocytes with glycogen-filled vacuoles (PAS-positive, diastase-sensitive glycogen), minimal fibrosis, no myofiber disarray — a key differentiator from sarcomeric HCM.
- **Electrophysiology study:** Characterizes accessory pathway location/multiplicity (often diffuse/microscopic rather than a single discrete bypass tract) and conduction system disease extent.

### Genetic Testing
- **Recommended approach:** Targeted *PRKAG2* sequencing or inclusion in HCM/cardiomyopathy gene panels, particularly triggered by the combination of LVH + pre-excitation or LVH + early pacemaker requirement.
- **Panel context:** PRKAG2 is a standard component of clinical hypertrophic cardiomyopathy / arrhythmia gene panels alongside sarcomeric genes (MYH7, MYBPC3, etc.) and other glycogen-storage-cardiomyopathy genes (LAMP2 for Danon disease, GAA for Pompe disease).
- **Single-gene testing** is appropriate when the phenotype (LVH + WPW + early conduction disease, especially with a family history suggestive of autosomal dominant inheritance) is highly specific.

### Clinical Criteria / Differential Diagnosis
The key differential is against other glycogen-storage or lysosomal-storage cardiomyopathies presenting with LVH + pre-excitation:
- **Danon disease (LAMP2, X-linked):** Distinguished by retinal involvement (a key discriminating exam finding not seen in PRKAG2 or Pompe disease), skeletal myopathy, and intellectual disability; X-linked with more severe disease in males.
- **Fabry disease (GLA, X-linked):** Considered in the differential given severity of LVH; distinguished by systemic features (angiokeratoma, renal disease, neuropathic pain, corneal verticillata).
- **Pompe disease (GAA, lysosomal, autosomal recessive):** Also produces glycogen-storage-related pre-excitation via the same annulus-fibrosus-disruption mechanism, but is lysosomal (acid maltase deficiency) and typically has more prominent skeletal myopathy/respiratory involvement.
- **Sarcomeric HCM:** Myofiber disarray + fibrosis on biopsy (absent in PRKAG2 syndrome); different genetic panel (MYH7, MYBPC3, TNNT2, etc.).

### Screening
- Cascade genetic testing/family screening is indicated once a proband's pathogenic *PRKAG2* variant is identified, given autosomal dominant inheritance and age-dependent penetrance (necessitating longitudinal, not one-time, screening of at-risk relatives).
- No population-based newborn screening program exists specifically for PRKAG2 syndrome.

---

## 11. Outcome / Prognosis

### Survival and Mortality
- In the largest natural history cohort (n=90, median follow-up 6 years): **13% all-cause mortality**, **8% sudden cardiac death or equivalent**, **4% required heart transplantation** ([PMID:32646569](https://pubmed.ncbi.nlm.nih.gov/32646569/)).
- The lethal congenital form (severe CBS3-domain mutations, e.g., R531Q) has a **uniformly fatal neonatal/infantile course**, with death typically between 3 weeks and 5 months of age due to heart failure and respiratory compromise (OMIM #261740).
- Historical estimates of premature (<40 years) sudden cardiac death as high as ~20% have been cited in early WPW-focused PRKAG2 cohorts.
- Overall, PRKAG2 syndrome is characterized in the literature as carrying a **"poor prognosis with a high rate of complications"** — juvenile-onset conduction disease, advanced heart failure, and potentially lethal arrhythmias.

### Morbidity and Functional Outcomes
- High burden of pacemaker implantation (19–36% across cohorts, median implant age ~36 years) due to progressive AV block/sinus node dysfunction.
- Heart failure hospitalization in ~14% over 6-year follow-up; progressive LV systolic dysfunction (EF decline to <50%) reported in up to 45% of one cohort over time.
- Neurocognitive/psychiatric morbidity reported in at least one large kindred (learning disability, intellectual disability, anxiety, mood disorders).

### Disease Course / Complications
- Atrial fibrillation is a major and increasing complication over time (18%→29% in the largest cohort).
- Progression to a "burned-out," dilated-cardiomyopathy-like advanced heart failure phase is described in case reports, distinct from typical sarcomeric HCM's more stable/hypertrophic-restrictive course.
- Recovery/regression of cardiomyopathy has only been shown experimentally in animal models via genetic suppression of mutant AMPK expression (not yet clinically achievable).

### Prognostic Factors
- Specific genotype is a major prognostic determinant: R531Q/severe CBS3 mutations → lethal congenital course; other variants → more variable adult-onset course.
- Early pre-excitation without hypertrophy in childhood may herald later progression to overt cardiomyopathy and conduction disease and warrants close longitudinal follow-up.
- Presence of pre-excitation, early pacemaker requirement, and young age at conduction disease onset are red flags distinguishing PRKAG2 syndrome from sarcomeric HCM and are associated with the classic high-risk phenotype.

---

## 12. Treatment

### Pharmacotherapy
- No disease-modifying/curative pharmacotherapy currently exists for humans; management is **symptomatic/supportive**:
  - Antiarrhythmic drugs for arrhythmia control
  - Anticoagulation for atrial fibrillation (stroke prevention)
  - Standard heart-failure pharmacotherapy for those progressing to systolic dysfunction
- **Experimental/preclinical:** The AMPK activator **metformin** normalized bioenergetic abnormalities in PRKAG2-mutant iPSC-derived cardiomyocytes in vitro — an early, paradoxical proof-of-concept finding (activating AMPK further via a different route ameliorated the metabolic phenotype), not yet validated in animal models or humans; should be treated as a research finding, not a clinical recommendation.
- Patents exist for antibody-oligonucleotide conjugates targeting PRKAG2 and other approaches to cytoplasmic glycogen storage disorders, indicating active pharmaceutical-industry interest in RNA-based/targeted knockdown approaches (patent literature only — not yet in clinical trials per the searches performed here).

### Advanced Therapeutics
- Gene therapy / RNA-based therapy (ASO, siRNA) targeting mutant *PRKAG2* transcript is a plausible therapeutic modality given the gain-of-function, single-gene, dominant mechanism (analogous to RNase-H knockdown ASO strategies used in other dominant-gain-of-function cardiac/systemic diseases), but no approved or clinical-trial-stage RNA therapeutic specific to PRKAG2 syndrome was identified in this search.
- No CRISPR/gene-editing, cell therapy, or immunotherapy approaches are reported for this indication.

### Surgical and Interventional
- **Catheter (radiofrequency) ablation** of accessory pathways: used but **arrhythmias frequently recur** because the diffuse, microscopic glycogen-mediated AV connections (rather than a single discrete bypass tract) provide a poor substrate for definitive ablative cure — in one cohort only 2 of 22 patients underwent AP ablation over 7-year follow-up, reflecting both diffuse substrate and disease-course considerations.
- **Permanent pacemaker implantation:** the mainstay intervention for progressive AV block/sinus node dysfunction (36% in one cohort; median implant age 36 years); often required at unusually young ages compared to typical age-related conduction disease, a key diagnostic clue.
- **Septal myectomy** has been used for outflow obstruction in select cases, alongside coronary "unroofing" procedures in reported case reports with concurrent anomalies.
- **Heart transplantation:** indicated for end-stage heart failure; ~4% of the largest cohort required transplantation by 6-year median follow-up; early referral while the patient remains a good surgical candidate is recommended in the literature.

### Supportive/Rehabilitative Care
Standard heart failure and arrhythmia supportive care; no PRKAG2-specific rehabilitation protocols identified.

### Experimental
No PRKAG2-syndrome-specific registered clinical trials were identified in this search pass; searches of ClinicalTrials.gov specifically for PRKAG2 interventional trials should be performed directly before curation (not completed in this session).

### Treatment Strategy
Management is largely **algorithmic/consensus-based rather than evidence-based from randomized trials** (given disease rarity): early genetic diagnosis to distinguish from sarcomeric HCM (important because standard HCM therapies like septal reduction have variable relevance), arrhythmia/conduction surveillance with a low threshold for pacemaker implantation, anticoagulation for AF, and heart failure management with early transplant evaluation for those progressing to end-stage disease.

### Suggested NCIT Terms (verify before curation)
- NCIT:C15329 (Surgical Procedure) — for ablation/myectomy
- NCIT:C15986 (Pharmacotherapy) — for antiarrhythmics/anticoagulants
- NCIT:C15289 (Organ Transplantation) — for heart transplant
- A specific NCIT term for "pacemaker implantation" should be looked up directly (not confidently identified in this pass)

---

## 13. Prevention

### Primary/Secondary/Tertiary Prevention
- No primary prevention exists (monogenic disease; risk factor modification is not applicable).
- **Secondary prevention = family cascade genetic screening**, given autosomal dominant inheritance and age-dependent, incomplete penetrance — relatives of a confirmed proband should undergo genetic testing and, if positive, longitudinal cardiac surveillance (ECG, echocardiography) rather than a single-timepoint screen, since penetrance increases with age.
- **Tertiary prevention** in established disease centers on early pacemaker implantation to prevent sudden death from advanced conduction disease, anticoagulation to prevent stroke in AF, and arrhythmia surveillance/ICD consideration in high-risk individuals (specific ICD/SCD-risk-stratification criteria for PRKAG2 syndrome specifically were not detailed in the sources reviewed and should be checked against current HCM/arrhythmia society guidelines before curation).

### Genetic Counseling
Recommended for affected families given autosomal dominant inheritance, variable expressivity (ranging from isolated pre-excitation to lethal neonatal disease), and reported reproductive/obstetric complications in at least one large kindred — prenatal counseling and, potentially, preimplantation genetic testing may be relevant for families with known severe/lethal variants (e.g., R531Q), though this specific application was not directly documented in the literature reviewed.

### Screening
Genetic cascade screening (as above) is the primary applicable "screening" modality; no population-based newborn or general screening program exists for this ultra-rare disease.

---

## 14. Other Species / Natural Disease

No naturally occurring PRKAG2-orthologous cardiac disease in companion animals or wildlife was identified in this search (unlike, e.g., the well-characterized porcine *PRKAG3* R200Q "RN-" gene affecting pork quality via skeletal muscle glycogen — note this is a *different* AMPK gamma subunit gene, γ3, not γ2, and a different tissue, skeletal muscle not heart; do not conflate the two in curation). No OMIA entry for a natural PRKAG2 cardiac disease analog was found. This section is not substantially populated for this disease in the current literature.

---

## 15. Model Organisms

### Mouse (primary model)
- **Transgenic overexpression models** (α-myosin heavy chain promoter-driven mutant γ2 transgenes) — the flagship model uses the **N488I** mutation:
  - Elevated AMPK activity, ~30-fold increase in cardiac glycogen, dramatic LVH, ventricular pre-excitation, and sinus node dysfunction, closely recapitulating the human phenotype ([Arad et al., Circulation 2003, PMID:12782567](https://pubmed.ncbi.nlm.nih.gov/12782567/)).
  - **T400N** transgenic hearts also show vacuolated myocytes, glycogen excess, hypertrophy, and pre-excitation.
  - **R302Q** transgenic/knock-in mouse models show biphasic AMPK activity changes and do not confer ischemic protection despite chronic AMPK activation ([PMID:17597581](https://pubmed.ncbi.nlm.nih.gov/17597581/)), and develop myocardial insulin resistance ([PMC3707764](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3707764/)).
- **Inducible (tetracycline-repressible) N488I model:** demonstrates that suppressing mutant transgene expression at various life stages (including prenatally) reverses glycogen accumulation, cardiomyopathy, and conduction system degeneration — direct causal/reversibility evidence ([Wolf et al., Circulation 2008, PMID:18158359](https://pmc.ncbi.nlm.nih.gov/articles/PMC2957811/)).
- **Compound-heterozygous rescue model:** co-expression of a dominant-negative α2-AMPK subunit transgene (TGα2DN) with the γ2-N488I transgene partially/completely normalizes ECG, cardiac function, morphology, and exercise capacity — implicates α2 as the key catalytic mediator of the disease phenotype and is a useful genetic-epistasis tool for mechanism dissection.

### Human iPSC-derived cardiomyocyte models
- Patient-derived iPSC-CMs (R302Q) and TALEN-genome-engineered isogenic iPSC-CM lines recapitulate glycogen accumulation, lipid storage, altered redox regulation, reduced glycolysis, and increased mitochondrial respiration — useful for mechanistic and drug-screening studies (e.g., the metformin rescue finding) ([Cell Reports 2016](https://www.cell.com/cell-reports/fulltext/S2211-1247(16)31640-0); Frontiers Cardiovasc Med 2026).
- Microtissue (3D engineered cardiac tissue) models extend these findings to fibrosis and survival phenotypes.

### Invertebrate Models
- **Drosophila melanogaster:** *SNF4Aγ* is the fly ortholog of PRKAG1/2/3, sharing 39–57% identity / 53–71% similarity in the CBS/ligand-binding domains with the human genes; required for regulation of developmental and stress-induced autophagy — used to study conserved AMPK-γ biology (lipid metabolism, autophagy, starvation response) rather than a direct cardiac-phenotype disease model, since Drosophila lacks a chambered heart with a conduction system analogous to the mammalian AV node/annulus fibrosus.
- No *C. elegans* or yeast PRKAG2-specific disease models were identified in this search, though AMPK (SNF1 in yeast) is broadly conserved and yeast SNF1/AMPK biology has informed general enzymology of the CBS-domain nucleotide-sensing mechanism.

### Model Limitations
- Mouse transgenic-overexpression models (rather than physiological knock-in models in all cases) may not perfectly recapitulate human dosage/expression-level effects, though later knock-in-style and inducible models substantially strengthen causal inference.
- iPSC-CM models, while capturing metabolic/glycogen phenotypes, do not recapitulate the whole-organ conduction-system anatomy (annulus fibrosus disruption) that is central to the WPW mechanism in vivo — this aspect of pathophysiology is best studied in the mouse models.

---

## Summary Table of Key PMIDs Cited

| PMID | First author/Journal/Year | Key content |
|---|---|---|
| 11407343 | Gollob, NEJM 2001 | Original gene identification (linkage 7q34-q36 → PRKAG2, R302Q) |
| 12782567 | Arad, Circulation 2003 | Transgenic N488I/T400N mouse model; annulus fibrosus mechanism of WPW |
| 18158359 | Wolf, Circulation 2008 | Reversibility of glycogen-storage cardiomyopathy via transgene suppression |
| 32646569 | Thevathasan, JACC 2020 | Largest natural history cohort (n=90, 27 centers) |
| 33244021 | — , Sci Rep 2020 | South Asian R302Q cohort (n=22) |
| 39082507 | — , Einstein (São Paulo) 2024 | Brazilian K290I/K291I kindred, 18-year follow-up, extracardiac features |
| 29298659 | — , BMC Med Genet 2018 | R302Q case, biopsy vacuolated myocytes, pseudotumor cerebri |
| 17597581 | — , PubMed 2007 | R302Q mouse model, biphasic AMPK activity, no ischemic protection |
| 20031621 | — , PubMed | Early signaling events, glycogen synthase/AS160 upregulation |

**Note on evidence quality:** Several statistics and specific quotes above were retrieved via secondary web-search summarization rather than direct primary-abstract fetch (a number of publisher URLs — jacc.org, ahajournals.org, thelancet.com/ebiom — returned HTTP 403 in this session and could not be directly fetched). Before committing any snippet-level evidence to a dismech KB entry, **each PMID must be independently re-verified** via `just fetch-reference PMID:XXXX` against the cached real abstract, per the project's mandatory anti-hallucination SOP — several numeric details here (e.g., exact percentages, exact variant nomenclature such as K290I vs. K291I) should be cross-checked against the primary source before quoting as an exact snippet. Similarly, all suggested HP/GO/CL/UBERON/NCIT/MONDO term IDs in this report are **unverified suggestions** and must be confirmed with OAK (`runoak -i sqlite:obo:<ontology> info <ID> -O obo`) before use in curation, consistent with dismech's ontology-term verification policy.