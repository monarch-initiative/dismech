---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-03T01:32:04.261638'
end_time: '2026-08-03T01:37:45.502892'
duration_seconds: 341.24
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: KLHL24-Related Hypertrophic Cardiomyopathy
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
  web_search_requests: 12
  num_turns: 27
  total_cost_usd: 1.8037469000000004
  session_id: ccfe4e45-02a4-514e-bba5-3af1e8db647b
  stop_reason: end_turn
citation_count: 12
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** KLHL24-Related Hypertrophic Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **KLHL24-Related Hypertrophic Cardiomyopathy** covering all of the
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

# KLHL24-Related Hypertrophic Cardiomyopathy — Comprehensive Research Report

## 1. Disease Information

**Overview:** KLHL24-related hypertrophic cardiomyopathy (HCM) is a recently described, autosomal recessive cardiomyopathy caused by biallelic loss-of-function variants in *KLHL24* (Kelch-like family member 24). It is characterized by early-onset (typically second–third decade) left ventricular hypertrophy, a distinctive histopathology of intracellular polyglucosan body accumulation and desmin intermediate-filament aggregation, and a markedly elevated risk of malignant ventricular arrhythmia and sudden cardiac death relative to classical sarcomeric HCM. The disease was first reported in 2019 by Zetterberg et al. in two unrelated consanguineous families (Iraqi and Iranian) ([Human Molecular Genetics](https://academic.oup.com/hmg/article/28/11/1919/5305756); PMID:30715372), and additional cases (including a compound-heterozygous kindred) have since been reported ([Frontiers in Cardiovascular Medicine 2026](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2026.1771424/full); [JACC: Case Reports 2026](https://www.jacc.org/doi/10.1016/j.jaccas.2026.107178), [JACC: Case Reports 2026](https://www.jacc.org/doi/10.1016/j.jaccas.2026.107473)).

**Key identifiers:**
- **OMIM phenotype:** #620236 — Cardiomyopathy, familial hypertrophic, 29, with polyglucosan bodies (**CMH29**) ([OMIM:620236](https://omim.org/entry/620236))
- **OMIM gene:** *611295 — KLHL24 ([OMIM:611295](https://www.omim.org/entry/611295))
- **MONDO:** MONDO:0859372 (cardiomyopathy, familial hypertrophic, 29, with polyglucosan bodies)
- **HGNC:** HGNC:25947 (*KLHL24*)
- **Gene location:** chromosome 3q27.1
- **GenCC/ClinGen classification:** *KLHL24*–autosomal recessive HCM is rated **"Moderate"** (not yet "Definitive") by the ClinGen Hereditary Cardiovascular Disease Gene Curation Expert Panel, based on 3 publications and 4 probands as of the 2024/2025 reappraisal ([JACC 2024](https://www.jacc.org/doi/10.1016/j.jacc.2024.12.010))
- **ICD-10/11:** No disease-specific code exists; falls under the general hypertrophic cardiomyopathy codes (ICD-10 I42.1/I42.2; ICD-11 BB80–BB81) with a genetic-cardiomyopathy modifier
- **Note:** This entity must be distinguished from the mechanistically **opposite** *KLHL24*-related disease, generalized intermediate **epidermolysis bullosa simplex 6 with or without cardiomyopathy (EBS6)**, OMIM #617294, MONDO:0015006, Orphanet:508529 — an **autosomal dominant, gain-of-function** disorder (see §2 and §6 for the mechanistic contrast).

**Synonyms:** "KLHL24-associated hypertrophic cardiomyopathy," "familial hypertrophic cardiomyopathy 29," "recessive KLHL24 cardiomyopathy with polyglucosan bodies," "KLHL24-related desminopathy" (cardiac phenotype only — this term is also loosely used for the dominant EBS/DCM entity, so context matters).

**Evidence basis:** All currently available data derive from aggregated case reports/small case series in the medical literature (not large-cohort registries or EHR aggregation) — fewer than ~10 kindreds and ~20–35 affected individuals have been published to date.

---

## 2. Etiology

**Disease causal factor:** Biallelic (homozygous or compound heterozygous) **loss-of-function** variants in *KLHL24*, inherited in an **autosomal recessive** pattern. This is a purely monogenic Mendelian cardiomyopathy — no environmental or infectious trigger has been implicated in symptom onset, though arrhythmic events (syncope, sudden death) are precipitated in the setting of physical exertion in several reported cases.

**Genetic risk factors:**
- Homozygous nonsense variant **c.1048G>T (p.Glu350\*)** — truncates the protein just before/within the Kelch repeat domain (Family A, Iraqi) (PMID:30715372)
- Homozygous missense variant **c.917G>A (p.Arg306His)** — affects a residue highly conserved across species and among KLHL family members (Family B, Iranian) (PMID:30715372)
- Compound heterozygous variants **c.532del (p.His178Ilefs\*66)**, a frameshift in the **BACK domain** (exon 3; ACMG: Likely Pathogenic, PVS1+PM2_Supporting), and **c.1514A>G (p.Tyr505Cys)**, a missense variant in the **Kelch domain** (exon 7; ACMG: Likely Pathogenic, PM3+PM2_Supporting+PP3_Strong) — reported in two non-consanguineous brothers, each parent a heterozygous carrier ([Frontiers in Cardiovascular Medicine 2026](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2026.1771424/full))
- Neither of the original founder variants was found in the Greater Middle Eastern Variome or in 500 ethnically matched control exomes, consistent with rare, population-restricted recessive alleles.
- **Consanguinity** is a major risk factor in the founding families (both original kindreds were consanguineous); the 2026 compound-heterozygous case demonstrates the disease can also arise in non-consanguineous families via two independently-inherited rare alleles.
- Because genetic evidence to date comes almost entirely from consanguineous Middle Eastern kindreds, ClinGen curators explicitly "down-scored" the evidence to avoid over-inflating gene-disease validity, since the two alleles are unlikely to have arisen independently within a single consanguineous pedigree ([JACC 2024](https://www.jacc.org/doi/10.1016/j.jacc.2024.12.010)).

**Protective factors:** None reported. Heterozygous carrier parents/relatives in all reported families are clinically asymptomatic, indicating full recessivity with no reported semi-dominant carrier phenotype (in contrast to some desmin-related myopathies).

**Gene–environment interactions:** Not established; disease expression appears driven primarily by genotype, though exertion appears to be a proximate trigger for documented arrhythmic/sudden-death events in several cases.

---

## 3. Phenotypes

| Phenotype | Type | Onset/Course | Frequency (of reported cases) | Suggested HP term |
|---|---|---|---|---|
| Left ventricular hypertrophy (often asymmetric septal) | Clinical sign | 2nd–3rd decade (range ~16–36 y in original cohort; as young as childhood/teens in compound-het/pediatric cases) | Core/defining feature | HP:0001639 (Hypertrophic cardiomyopathy) |
| Palpitations | Symptom | Presenting symptom in most patients | Frequent | HP:0001962 (Palpitations) |
| Syncope | Symptom | Presenting/recurring | Frequent | HP:0001279 (Syncope) |
| Dyspnea on exertion | Symptom | Presenting, may progress | Frequent | HP:0002094 (Dyspnea) |
| Nonsustained/sustained ventricular tachycardia | Clinical sign (arrhythmia) | Variable, often precedes SCD | Frequent | HP:0004758 (Nonsustained ventricular tachycardia) / HP:0004756 (Sustained ventricular tachycardia) |
| Sudden cardiac death | Outcome | Young adulthood (documented as early as mid-20s) | ~27% of original cohort (3/11) | HP:0001645 (Sudden cardiac death) |
| Left ventricular outflow tract obstruction | Clinical sign | Variable | Present in some (e.g., Family A proband) | HP:0001718 (Left ventricular outflow tract obstruction) |
| Reduced left ventricular ejection fraction / progression to dilated phenotype | Clinical sign | Later disease course | Documented in advanced cases (e.g., pre-transplant EF 25%) | HP:0005110 (Reduced left ventricular ejection fraction) |
| Heart failure requiring transplantation | Outcome | Young adulthood | 1/11 in original cohort; additional transplant cases in literature | HP:0001635 (Congestive heart failure) |
| Skeletal muscle weakness/myopathic features | Clinical sign | Variable | Reported in a subset (subclinical to overt) | HP:0003324 (Generalized muscle weakness) |
| Elevated cardiac biomarkers (troponin T, NT-proBNP/BNP) | Laboratory abnormality | Progressive with disease severity | Reported when measured | HP:0031547 (Elevated circulating troponin T) |
| Conduction abnormalities (prolonged PR, need for pacing) | Clinical sign | Variable | Documented in a subset (e.g., pacemaker for syncope) | HP:0006682 (Prolonged PR interval) |

**Severity/progression:** Highly variable — from asymptomatic screening detection to catastrophic sudden death in the 2nd–3rd decade. Disease course is generally **progressive**, with some patients evolving from a hypertrophic to a mixed/dilated phenotype with declining ejection fraction over years to a decade of follow-up. Extreme hypertrophy (interventricular septum up to 38–42 mm) has been documented in the most severely affected reported patient (age 20).

**Quality of life impact:** Not formally studied with validated instruments (no EQ-5D/SF-36 data identified); qualitatively, activity restriction, ICD/pacemaker implantation, and progressive heart failure symptoms substantially affect daily functioning in symptomatic patients.

---

## 4. Genetic/Molecular Information

**Causal gene:** *KLHL24* (Kelch-like family member 24), HGNC:25947, OMIM *611295, chromosome 3q27.1.

**Protein structure:** KLHL24 belongs to the BTB-Kelch family of Cullin3-RING E3 ubiquitin ligase (CRL3) substrate adaptors, comprising an N-terminal **BTB/POZ domain** (binds Cullin3), a **BACK domain** (structural linker, also implicated in substrate/complex regulation), and a C-terminal **Kelch repeat (propeller) domain** (six blades, mediates substrate recruitment). In the recessive HCM-causing alleles, the E350* nonsense variant truncates the protein before/at the start of the Kelch domain (loss of substrate-binding function); R306H affects a conserved residue; the compound-heterozygous case combines a BACK-domain frameshift (complete loss of function) with a Kelch-domain missense variant (impaired substrate recognition).

**Variant classification (ACMG/AMP):**
- c.1048G>T (p.Glu350\*) — nonsense, loss-of-function
- c.917G>A (p.Arg306His) — missense, functionally validated as loss-of-function via zebrafish rescue failure
- c.532del (p.His178Ilefs\*66) — frameshift, Likely Pathogenic (PVS1+PM2_Supporting)
- c.1514A>G (p.Tyr505Cys) — missense, Likely Pathogenic (PM3+PM2_Supporting+PP3_Strong)

**Population frequency:** None of the reported pathogenic variants appear in gnomAD/1000 Genomes/ExAC at appreciable frequency; the original two founder variants were absent from the Greater Middle Eastern Variome and 500 ethnically matched control exomes, consistent with private/founder recessive alleles.

**Origin:** All reported variants are germline.

**Functional consequence:** **Loss of function** — impaired Cullin3-RING E3 ubiquitin ligase substrate-adaptor activity, resulting in failure to ubiquitinate and target the intermediate filament protein **desmin** (DES; HGNC:2770) for proteasomal degradation, with consequent pathological desmin accumulation in cardiac and skeletal muscle (confirmed by Western blot showing markedly upregulated desmin protein in patient tissue) (PMID:30715372).

**Modifier genes:** None specifically established; genetic background/consanguinity structure is a de facto contributing factor to biallelic variant co-occurrence.

**Epigenetic information:** Not reported for this entity.

**Chromosomal abnormalities:** None reported; disease is caused by small-scale sequence variants (SNVs/indels), not structural rearrangements.

**Suggested gene/ontology annotations:**
- Gene: *KLHL24*, hgnc:25947
- Target/interacting protein: *DES* (desmin), hgnc:2770
- GO Molecular Function: GO:0031625 (ubiquitin protein ligase binding); GO:0004842 (ubiquitin-protein transferase activity, via CRL3 complex)
- GO Biological Process: GO:0043161 (proteasome-mediated ubiquitin-dependent protein catabolic process); GO:0045104 (intermediate filament cytoskeleton organization)

---

## 5. Environmental Information

No environmental, toxic, occupational, or infectious contributing factors have been identified or reported for this monogenic recessive cardiomyopathy. Lifestyle factor of note: strenuous physical exertion appears to be a proximate trigger for arrhythmic events/sudden death in several reported cases, supporting activity-restriction as a management consideration, though this has not been formally studied.

---

## 6. Mechanism / Pathophysiology

**Molecular pathway:** KLHL24 functions as a substrate-specific adaptor within the **Cullin3-RING E3 ubiquitin ligase (CRL3) complex**. The BTB domain binds Cullin3/RBX1; the Kelch domain recruits substrate proteins for ubiquitination and subsequent 26S proteasomal degradation. In cardiac and skeletal muscle, the principal validated substrate is **desmin**, the muscle-specific type III intermediate filament protein that forms the cytoskeletal scaffold linking sarcomeres, the sarcolemma, mitochondria, and the nuclear envelope.

**Causal chain (loss-of-function / HCM arm):**
1. Biallelic loss-of-function *KLHL24* variant → loss of CRL3 substrate-adaptor activity
2. Failure of desmin ubiquitination/proteasomal turnover → pathological **desmin accumulation** (confirmed by Western blot and immunostaining) in cardiomyocytes and skeletal myocytes
3. Desmin/intermediate-filament aggregation and disordered assembly, together with abnormal intramyocellular **polyglucosan (glycogen-derived, alpha-amylase-resistant PAS-positive) body** deposition
4. Cardiomyocyte hypertrophy, interstitial fibrosis, and macrophage infiltration → structural left ventricular hypertrophy and outflow tract obstruction in some patients
5. Disrupted cytoskeletal-mechanical and electrical coupling → **arrhythmogenic substrate** → ventricular tachyarrhythmia and sudden cardiac death
6. In advanced/longstanding disease, progression to reduced systolic function and a mixed/dilated phenotype with heart failure

**Contrast — the gain-of-function *KLHL24* arm (EBS6/dilated cardiomyopathy):** Heterozygous, dominant translation-reinitiation/start-codon variants (e.g., c.1A>G, c.2T>C, c.2T>G) produce an N-terminally truncated KLHL24-ΔN28 protein that **escapes its own normal N-terminal-degron-mediated turnover**, becoming hyperstable. This gain-of-function protein then **excessively** degrades intermediate filament substrates — keratin-14 in basal keratinocytes (causing epidermolysis bullosa simplex with skin fragility) and, in the heart, again **desmin** (causing progressive dilated cardiomyopathy and sudden death, typically in early adulthood) ([Human Molecular Genetics 2022](https://academic.oup.com/hmg/article/31/8/1308/6420897); [PMC9029237](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9029237/); [JCI 2021](https://www.jci.org/articles/view/140615), PMID:34292882; [Cardiovascular Research 2025](https://academic.oup.com/cardiovascres/article/121/17/2714/8369605)). Thus **both the recessive HCM entity and the dominant EBS/DCM entity converge on desmin dysregulation**, but via **opposite** directions of KLHL24 dosage/activity — too little CRL3 adaptor activity (LOF, → desmin excess/HCM) versus pathologically too much (GOF, → desmin depletion/DCM). This is a striking allelic-series example of bidirectional dosage pathology at a single E3-ligase adaptor locus.

**Cellular processes involved:** Ubiquitin-proteasome system dysfunction; intermediate filament cytoskeletal organization failure; glycogen/polyglucosan metabolism disruption; myocyte hypertrophic remodeling; fibrosis; macrophage-mediated inflammatory infiltration.

**Protein dysfunction:** Loss of substrate-adaptor (E3 ligase) function (LOF alleles) vs. hyperstabilized, overactive adaptor (GOF alleles in the allelic EBS/DCM disorder).

**Tissue damage mechanism:** Accumulation of misfolded/aggregated desmin and polyglucosan material is thought to impair myofibrillar force transmission and mechanical/electrical coupling, driving both structural hypertrophy/fibrosis and a primary arrhythmogenic substrate independent of the degree of hypertrophy — explaining the "genotype outpaces phenotype" pattern of sudden death occurring even with modest structural disease, as highlighted in a 2026 case report title ([JACC: Case Reports 2026](https://www.jacc.org/doi/10.1016/j.jaccas.2026.107178)).

**Biochemical abnormality:** Pathological glycogen/polyglucosan accumulation (alpha-amylase/diastase-resistant PAS-positive material) — placing this entity in partial mechanistic overlap with glycogen-storage cardiomyopathies (see §10 differential diagnosis).

**Molecular profiling:**
- Gene expression (GTEx): *KLHL24* shows highest expression in **skeletal muscle**, followed by lung, then left ventricular myocardium — consistent with the muscle-predominant phenotype (PMID:30715372).
- Western blot: desmin markedly upregulated in patient skeletal and cardiac muscle relative to controls.
- HEK293 transfection studies (referenced in review literature) confirm KLHL24-mediated desmin degradation in vitro, with KLHL24 knockdown or desmin overexpression restoring desmin protein levels.

**Model system validation (zebrafish):** *klhl24a* is expressed from early developmental stages and, by 22 hours post-fertilization, localizes to the cardiac cone, particularly ventricular myocytes. Morpholino knockdown of *klhl24a* produced cardiac defects (pericardial edema, altered heart rate, reduced circulation, ventricular failure) in **90% of morphants (n=179)** vs. **4% of controls (n=119)**. Co-injection of wild-type *klhl24a* mRNA partially rescued the phenotype (51.5% normal hearts vs. 16% with morpholino alone), whereas mRNA encoding the human R306H (c.917G>A) or E350\* (c.1048G>T)-equivalent mutations **failed to rescue** (71.5% and 77.5% of embryos still showed heart defects, respectively) — direct functional evidence that both variants are loss-of-function (PMID:30715372).

**Suggested GO/CL terms:**
- GO:0045104 (intermediate filament cytoskeleton organization)
- GO:0043161 (proteasome-mediated ubiquitin-dependent protein catabolic process)
- GO:0005978 (glycogen biosynthetic process) / GO:0005980 (glycogen catabolic process) as relevant to polyglucosan pathology
- CL:0000746 (cardiac muscle cell); CL:0000188 (skeletal muscle cell / myocyte)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Heart (myocardium — predominantly left ventricle; also right ventricular involvement reported on cardiac MRI in some cases)
- **Secondary:** Skeletal muscle (subclinical to overt myopathic changes, "cogwheel fiber" histology); conduction system (AV conduction disease requiring pacing in some patients)
- **Body systems:** Cardiovascular system (primary); musculoskeletal system (secondary)
- Note: skin is **not** involved in the recessive/LOF HCM entity (unlike the dominant EBS6/DCM entity), a key clinical differentiator confirmed in the compound-heterozygous 2026 case report, where siblings had no cutaneous findings.

**Tissue/cell level:**
- Cardiomyocytes (CL:0000746) — hypertrophy, polyglucosan/glycogen accumulation, desmin aggregation
- Skeletal myocytes (CL:0000188) — subsarcolemmal/intermyofibrillar glycogen and desmin accumulation, "cogwheel" fiber morphology
- Cardiac interstitial fibroblasts — fibrosis
- Macrophages — interstitial infiltration in myocardium

**Subcellular level:**
- Intermediate filament cytoskeleton (GO:0045111, intermediate filament cytoskeleton) — desmin aggregates, tubular structures (8–12 nm filaments on EM)
- Cytoplasmic glycogen/polyglucosan deposits
- Ubiquitin-proteasome system machinery (cytoplasmic)

**Localization (UBERON):**
- UBERON:0002080 (heart left ventricle) — primary site of hypertrophy
- UBERON:0001133 (cardiac muscle tissue)
- UBERON:0001134 (skeletal muscle tissue)
- Lateralization: Not applicable (bilateral/systemic muscle involvement; LV-predominant cardiac disease, with some RV involvement on imaging)

---

## 8. Temporal Development

**Onset:** Typically **second to third decade of life** (documented range ~16–36 years in the original cohort); however, more recent reports document presentation in adolescence/childhood (e.g., syncope at age 20 requiring pacemaker; severe biventricular hypertrophy detected on screening at age 18–20 in a sibling pair). Onset pattern is generally **insidious**, with palpitations/dyspnea/syncope as presenting features, though the first clinical event in some patients is **sudden cardiac death**.

**Progression:** **Progressive** in most reported cases — declining ejection fraction and worsening heart failure symptoms over years (e.g., LVEF decline from 77%→70%→55% over a decade in one proband); a subset progresses to a dilated/mixed cardiomyopathy phenotype with need for transplantation. Disease course is variable in rate — from stable/mild over a decade of follow-up (with ICD/pacemaker support) to rapid deterioration and early sudden death (mid-20s).

**Disease stages:** Not formally staged in the literature; can be conceptually divided into (1) early/subclinical (structural hypertrophy on screening, asymptomatic), (2) symptomatic hypertrophic phase (palpitations, dyspnea, arrhythmia), and (3) advanced/mixed phase (systolic dysfunction, heart failure, transplant candidacy).

**Patterns:** No remission pattern described (progressive, non-relapsing disease). No specific critical intervention window has been established, though early genetic diagnosis and cardiac screening are advocated given the disproportionate arrhythmic risk relative to degree of hypertrophy.

---

## 9. Inheritance and Population

**Epidemiology:** No formal prevalence or incidence estimates exist; this is an **ultra-rare** disease with fewer than 10 kindreds (~20–35 affected individuals) reported in the literature as of 2026. All originally reported affected families were of Middle Eastern origin (Iraqi, Iranian) and consanguineous; a 2026 case report describes a non-consanguineous Chinese family, indicating the disease is not geographically restricted.

**Inheritance pattern:** **Autosomal recessive** — confirmed by homozygosity in consanguineous pedigrees and compound heterozygosity (with confirmed biparental inheritance) in a non-consanguineous family.

**Penetrance:** Appears high among biallelic carriers based on reported pedigrees, though the true penetrance is unknown given the small number of families and potential ascertainment bias toward severely affected probands.

**Expressivity:** **Variable** — ranging from mild/stable disease over a decade to catastrophic early sudden death, and from isolated cardiac phenotype to additional skeletal muscle involvement.

**Genetic anticipation:** Not reported/not applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not reported.

**Founder effects:** The original two variants (c.1048G>T, c.917G>A) are private/founder-type alleles specific to their respective consanguineous Middle Eastern pedigrees; absent from Greater Middle Eastern Variome and other population databases.

**Consanguinity role:** Central to disease manifestation in the originally reported families; ClinGen curators specifically note that genetic evidence from these families was discounted to avoid overcounting evidence, since biallelic inheritance of the same rare variant is expected in consanguineous unions.

**Carrier frequency:** Unknown/not established in any population database given the extreme rarity and lack of large-scale carrier screening data.

**Sex ratio:** No clear sex predilection reported across the described cases (both male and female probands affected in each family).

**Age distribution:** Predominantly diagnosed in adolescence through the 4th decade; symptomatic onset clusters in the late teens to 30s.

---

## 10. Diagnostics

**Clinical/imaging tests:**
- **Echocardiography:** Left ventricular hypertrophy (often asymmetric septal), +/- LV outflow tract obstruction, variable systolic function (normal to reduced), occasional mild LV dilation
- **Cardiac MRI:** Extensive subepicardial/transmural late gadolinium enhancement (LGE) in the LV free wall with relative apical sparing; RV inferior wall LGE also described; midapical hypertrabeculation noted in one case
- **ECG:** ST-T changes, prolonged PR interval, widened QRS, low voltages, or evidence of conduction disease; ambulatory (Holter) monitoring reveals frequent polymorphic/dimorphic ventricular ectopy and nonsustained VT
- **Biomarkers:** Elevated high-sensitivity troponin T and NT-proBNP/BNP, correlating with disease severity

**Histopathology (endomyocardial/skeletal muscle biopsy — key diagnostic clue):**
- Cardiomyocyte hypertrophy with PAS-positive, alpha-amylase/diastase-**resistant** material (polyglucosan bodies)
- Desmin-positive immunostaining showing intermediate filament accumulation
- Interstitial fibrosis with small macrophage infiltrates
- Skeletal muscle: focal subsarcolemmal/intermyofibrillar glycogen accumulation producing a characteristic **"cogwheel" fiber** appearance — proposed as a diagnostic marker
- Electron microscopy: accumulation of glycogen, tubular structures, and irregularly arranged intermediate filaments (8–12 nm diameter) in intermyofibrillar regions

**Genetic testing:**
- **Gene panel testing** for HCM (including *KLHL24*) or a broader cardiomyopathy/desminopathy panel is the recommended first-line approach given phenotypic overlap with sarcomeric HCM
- **Whole exome/genome sequencing** appropriate when panel testing is uninformative, particularly in consanguineous families (homozygosity mapping proved diagnostic in the original two kindreds) or when compound heterozygous variants are suspected
- Single-gene *KLHL24* sequencing reasonable when strong family history/phenotype (recessive pattern, biopsy showing polyglucosan bodies/desmin accumulation) points to this specific gene

**Differential diagnosis:**
- Sarcomeric HCM (MYH7, MYBPC3, TNNT2, etc.) — lacks polyglucosan body/desmin-accumulation histology
- Glycogen storage cardiomyopathies: PRKAG2 cardiomyopathy, Danon disease (LAMP2), Pompe disease (GAA) — distinguished by specific glycogen-handling gene defects and differing histology/clinical syndrome (e.g., WPW pre-excitation in PRKAG2, autophagic vacuoles in Danon)
- Desmin-related myopathy/desminopathy (primary *DES* gene mutations) — a key phenocopy given shared desmin-accumulation pathology; distinguished by direct *DES* sequencing
- Other polyglucosan body diseases (adult polyglucosan body disease, GBE1; Lafora disease) — typically have prominent neurological/hepatic involvement not seen in KLHL24-HCM
- The dominant *KLHL24*-EBS/DCM entity (EBS6, OMIM #617294) — distinguished by cutaneous blistering/scarring history, dominant inheritance, and dilated (rather than hypertrophic) phenotype

**Screening:** Given autosomal recessive inheritance, cascade screening of at-risk siblings in affected families is warranted; targeted variant testing of parents/relatives once a proband is identified. No population-based newborn screening exists given rarity.

---

## 11. Outcome/Prognosis

**Mortality:** Poor prognosis reported in the founding cohort — of 11 affected young adults in the two original families, **3 died suddenly** (~27%) and **1 required cardiac transplantation** (~9%) due to heart failure (PMID:30715372). Additional individual case reports describe sudden cardiac death in the mid-20s to 50s and heart transplantation in teenagers with rapidly progressive disease.

**Disease course:** Variable — some patients remain relatively stable for a decade with medical/device therapy (pacemaker/ICD), while others show a malignant course with early sudden death, sometimes with only modest structural hypertrophy at the time of the fatal event (the basis for describing this as a condition where "genotype outpaces phenotype").

**Complications:** Ventricular tachyarrhythmia, sudden cardiac death, progressive heart failure, conduction system disease requiring pacing, and (in a subset) progression to a dilated/mixed cardiomyopathy phenotype.

**Prognostic factors:** Disproportionate arrhythmic risk relative to degree of hypertrophy is repeatedly emphasized as a defining and clinically important feature — implying that conventional HCM risk-stratification tools (which weight hypertrophy severity heavily) may underestimate sudden death risk in *KLHL24*-HCM patients, supporting a lower threshold for ICD consideration.

**Quality of life/functional outcomes:** Formal outcome measures not reported; qualitatively, patients on device therapy and guideline-directed heart failure therapy have maintained NYHA Class I–II status over 1–2 year follow-up in reported pediatric cases.

---

## 12. Treatment

No disease-specific approved therapy exists; management is **supportive/symptomatic**, following general HCM/heart failure and inherited-arrhythmia-syndrome principles:

**Pharmacotherapy:**
- Beta-blockers (e.g., metoprolol succinate) — NCIT:C15986 (Pharmacotherapy); CHEBI-bindable agent (metoprolol)
- ACE inhibitors / mineralocorticoid receptor antagonists (spironolactone) — standard heart failure therapy
- Diuretics (furosemide) and vasopressin antagonists (tolvaptan) in decompensated/severely hypertrophied cases
- Antiarrhythmic considerations as per general HCM arrhythmia management (not disease-specific)

**Device/interventional therapy:**
- **Implantable cardioverter-defibrillator (ICD)** for primary or secondary prevention of sudden cardiac death — used in multiple reported cases given documented nonsustained VT and high SCD risk — NCIT:C50592 (or closest device/procedure term)
- **Permanent pacemaker** implantation for conduction system disease/syncope
- **Cardiac transplantation** for end-stage heart failure — NCIT:C15289 (Organ Transplantation) — performed in at least 2 reported cases (one at age 26, one pediatric case)

**Supportive care:**
- Activity/exercise restriction given exertion-associated arrhythmic risk
- Regular cardiac surveillance (echocardiography, Holter monitoring, cardiac MRI) in affected individuals and at-risk relatives

**Genetic counseling:** Recommended for families given autosomal recessive inheritance, recurrence risk (25% for siblings of an affected proband), and implications for cascade testing — NCIT:C15240 (Genetic Counseling)

**Experimental/targeted therapy:** None specific to *KLHL24*-HCM currently in clinical trials (no NCT identifiers identified). Given the mechanistic understanding of desmin dysregulation, this represents a theoretical target for future precision therapeutics, but no such approach has reached clinical development.

**Treatment outcomes:** Limited data; reported ICD-treated pediatric patients have remained stable without device discharges over 1–2 years; pacemaker therapy abolished recurrent syncope in one adult proband over a decade of follow-up, though cardiac function gradually declined.

---

## 13. Prevention

- **Primary prevention:** Genetic counseling and carrier testing in families with a known proband, particularly relevant in consanguineous unions or populations/communities where founder alleles have been identified (Iraqi, Iranian kindreds to date)
- **Secondary prevention:** Cascade cardiac and genetic screening of at-risk siblings/relatives of an affected proband, given the significant risk of sudden death as a first clinical manifestation
- **Tertiary prevention:** ICD implantation to prevent sudden death in individuals with documented ventricular arrhythmia or high-risk features; guideline-directed heart failure therapy to slow progression to end-stage disease
- **Screening:** No population-based screening program exists; risk stratification is currently informed by general HCM criteria, though the literature suggests these may be insufficiently sensitive for this specific genotype (disproportionate arrhythmic risk relative to hypertrophy severity)
- **Reproductive options:** Preimplantation genetic diagnosis/prenatal testing could be offered to carrier couples once a familial variant is identified, though not specifically documented in the literature for this disease

---

## 14. Other Species / Natural Disease

No naturally occurring animal disease (companion animal, livestock, or wildlife) attributable to *KLHL24* loss-of-function has been reported in the veterinary or OMIA literature identified in this search. No spontaneous non-human model of *KLHL24*-HCM is described.

---

## 15. Model Organisms

**Zebrafish (Danio rerio):** The principal functional/disease model used to validate pathogenicity.
- *klhl24a* (zebrafish ortholog) is expressed from early developmental stages, localizing to the cardiac cone (particularly ventricular myocytes) by 22 hours post-fertilization
- **Morpholino knockdown model:** Produces cardiac defects (pericardial edema, altered heart rate, reduced circulation, and — in the majority — ventricular failure) in 90% of morphants vs. 4% of controls
- **mRNA rescue/complementation assay:** Co-injection of wild-type human/zebrafish *klhl24* mRNA partially rescues the knockdown phenotype (~51.5% normal hearts vs. 16% with morpholino alone); mRNA encoding the human pathogenic variants (equivalent to R306H and E350\*) **fails to rescue**, providing direct functional confirmation of loss-of-function pathogenicity for both disease-causing alleles (PMID:30715372)
- **Applications:** This model has been used specifically to functionally validate variant pathogenicity (rescue assay) and to demonstrate a conserved, essential role for *klhl24* in early cardiac development/function
- **Limitations:** As an early-developmental knockdown/complementation model, it captures acute cardiac dysfunction but does not recapitulate the adult-onset, chronic hypertrophic/fibrotic/arrhythmogenic disease course, the polyglucosan body pathology, or the skeletal muscle phenotype seen in human patients

**Mouse:** No *Klhl24* cardiac-specific knockout/knock-in mouse model was identified in this search. A relevant **comparator model** is the desmin-null (*Des⁻/⁻*) mouse, which develops cardiomyopathy and skeletal myopathy due to loss of the same downstream substrate protein implicated in *KLHL24*-HCM pathogenesis, though this is not a direct *KLHL24* model.

**Cellular/iPSC models:** hiPSC-derived engineered heart tissue models have been used to study the **gain-of-function** *KLHL24* variants (relevant to the allelic EBS/DCM disorder), demonstrating KLHL24-mediated desmin degradation and tissue dilation ([JCI 2021](https://www.jci.org/articles/view/140615), PMID:34292882); no iPSC-cardiomyocyte model specific to the loss-of-function HCM-causing alleles was identified in this search — representing a clear model-system gap for this specific disease entity.

**Resource note:** Given the paucity of species/model-organism data specific to the recessive HCM phenotype, this represents an area of active knowledge gap suitable for flagging as a `KNOWLEDGE_GAP` in a knowledge-base curation context (particularly the absence of a chronic/adult-onset mammalian model recapitulating the polyglucosan-body and arrhythmogenic phenotype).

---

## Summary Table of Key Citations

| PMID/Source | Title | Key Contribution |
|---|---|---|
| PMID:30715372 | Zetterberg et al., Hum Mol Genet 2019, "Cardiomyopathy with lethal arrhythmias associated with inactivation of KLHL24" | Founding paper: 2 consanguineous families, variant identification, histopathology, zebrafish functional validation |
| OMIM #620236 | CMH29 clinical synopsis | Curated phenotype/inheritance summary |
| OMIM *611295 | KLHL24 gene entry | Gene/protein reference |
| [Frontiers Cardiovasc Med 2026](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2026.1771424/full) | Compound heterozygous KLHL24 case report | First compound-het (non-consanguineous) family; detailed clinical/imaging/treatment data |
| [JACC Case Reports 2026 (107178)](https://www.jacc.org/doi/10.1016/j.jaccas.2026.107178) | "KLHL24-Associated HCM: When Genotype Outpaces Phenotype" | Emphasizes arrhythmic risk disproportionate to hypertrophy |
| [JACC Case Reports 2026 (107473)](https://www.jacc.org/doi/10.1016/j.jaccas.2026.107473) | "Biallelic KLHL24 LOF Variants: Early-Onset Arrhythmias and HCM" | Additional case evidence, early-onset emphasis |
| [PMC12926016](https://pmc.ncbi.nlm.nih.gov/articles/PMC12926016/) | Pediatric EBS-KLHL24 arrhythmogenic cardiomyopathy series | Contrast cases (dominant/GOF) + literature compilation table (32 prior cases) |
| [JACC 2024/2025](https://www.jacc.org/doi/10.1016/j.jacc.2024.12.010) | ClinGen HCM Gene Curation Expert Panel reappraisal | Formal "Moderate" gene-disease validity classification and evidentiary caveats |
| PMID:34292882 | JCI 2021, gain-of-function KLHL24/hiPSC engineered heart tissue | Mechanistic contrast — dominant GOF arm |
| [HMG 2022](https://academic.oup.com/hmg/article/31/8/1308/6420897) / PMC9029237 | Proteasome-mediated keratin degradation by mutant KLHL24 | Mechanistic contrast — skin/EBS arm |

**Data gaps flagged for curation:** (1) No large-cohort prevalence/incidence data exist — true population prevalence unknown; (2) no adult/chronic mammalian model exists specific to the LOF cardiac phenotype; (3) no disease-specific therapeutic trials; (4) genotype-phenotype correlation (e.g., nonsense vs. missense vs. compound heterozygous severity) remains preliminary given the very small number of published cases.