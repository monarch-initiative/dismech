---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-09T14:25:36.902445'
end_time: '2026-08-09T14:31:18.154047'
duration_seconds: 341.25
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Alcohol Use Disorder
  mondo_id: ''
  category: Psychiatric
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
  web_search_requests: 18
  num_turns: 16
  total_cost_usd: 1.8833275
  session_id: db8ba393-450c-5f19-a078-2aa9b08ae5a8
  stop_reason: end_turn
citation_count: 34
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Alcohol Use Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Alcohol Use Disorder** covering all of the
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

# Alcohol Use Disorder (AUD): Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview.** Alcohol use disorder (AUD) is a chronic, relapsing brain disorder characterized by an impaired ability to stop or control alcohol use despite adverse social, occupational, or health consequences. It is a "brain disease" model condition in the addiction neuroscience literature — involving compulsive substance seeking and use, loss of control over intake, and a negative emotional state when the substance is unavailable (Koob & Volkow, *Lancet Psychiatry* 2016, PMID: 27475769; Volkow, Koob & McLellan, *NEJM* 2016, PMID: 26816013). The DSM-5 (American Psychiatric Association, 2013) merged the former DSM-IV categories of "alcohol abuse" and "alcohol dependence" into a single diagnosis, **Alcohol Use Disorder**, scored on a continuum of mild (2–3 symptoms), moderate (4–5 symptoms), or severe (≥6 symptoms) from an 11-item symptom list spanning impaired control, social impairment, risky use, and pharmacological criteria (tolerance, withdrawal).

**Key identifiers:**
| Resource | Identifier | Notes |
|---|---|---|
| OMIM | **#103780** "Alcohol Dependence" (phenotype MIM); related gene loci *ADH1B* (*103720), *ALDH2* (*100650) | Number-sign entry reflecting polygenic susceptibility (multiple genes/loci) rather than a single-gene Mendelian disorder |
| ICD-11 | **6C40** "Disorders due to use of alcohol" (parent), with children **6C40.0** (episode of harmful use), **6C40.1** (harmful pattern of use), **6C40.2** (alcohol dependence), plus **6C40.3–6C40.7** (alcohol intoxication, withdrawal, withdrawal delirium, alcohol-induced psychotic/mood/anxiety disorder) (Saunders, *Alcohol Clin Exp Res* 2019, PMID: 31194891; Poznyak et al., PMC9881115) |
| ICD-10-CM | **F10.-** "Alcohol related disorders" (e.g., F10.20 alcohol dependence, uncomplicated; F10.10 alcohol abuse) |
| MeSH | **Alcoholism** (D000437); related headings "Alcohol-Related Disorders" (D000431) and "Binge Drinking" (D058188) |
| MONDO | Mondo harmonizes AUD with OMIM #103780 and ICD-11 6C40; the exact MONDO CURIE was not confirmed against a live ontology browser in this research pass and should be verified via the Monarch Initiative / OLS4 MONDO browser before use in curation, rather than asserted here |
| Orphanet | Not applicable — AUD is a common complex disorder, outside Orphanet's rare-disease scope |
| GARD/NORD | Not applicable (common disorder) |

**Synonyms/alternative names:** Alcoholism; alcohol dependence; alcohol addiction; alcohol abuse (older, narrower DSM-IV term now subsumed); "problematic alcohol use" (the phenotype label commonly used in genetics literature to combine clinical AUD diagnoses with the AUDIT-C/AUDIT screening-based phenotype).

**Evidence basis.** Most of the epidemiological and diagnostic-criteria literature is derived from aggregated population-level survey data (e.g., NESARC-III, NSDUH, UK Biobank) rather than individual EHR chart review, supplemented by large-scale biobank/EHR-linked genomic cohorts (Million Veteran Program, UK Biobank, FinnGen, Psychiatric Genomics Consortium) for genetic association analyses.

---

## 2. Etiology

### Disease Causal Factors
AUD is a **multifactorial, gene-environment disorder**. No single causal lesion exists; risk emerges from the additive and interactive effects of many common genetic variants of small individual effect, combined with environmental exposure (access to alcohol, early-life drinking onset, stress, trauma, peer/family use) and repeated pharmacological exposure to ethanol producing durable neuroadaptation (see Mechanism, §6).

### Genetic Risk Factors

- **Twin/family heritability:** Genetic factors account for an estimated **40–60% of variance in liability** to alcohol dependence (OMIM #103780, summarizing family/twin/adoption literature). A twin-and-adoption meta-analysis (Verhulst, Neale & Kendler, *Psychol Med* 2015, PMID: 25066582) is the standard heritability reference. Recent longitudinal twin work models AUD symptom liability as more heritable (~36%) than symptom count (~22%) or categorical diagnosis (~14%), with genetic influence on most DSM-5 criteria (except craving) substantially overlapping across symptoms (per search of PMC13092882 / ScienceDirect twin-genetics literature).
- **Alcohol-metabolizing enzyme variants (largest documented single-locus effects, protective/predisposing):**
  - **ADH1B** (alcohol dehydrogenase 1B; HGNC:249; OMIM *103720) — the fast-metabolizing variant **rs1229984** (His48Arg, also called ADH1B*2) accelerates ethanol→acetaldehyde conversion, causing an aversive acetaldehyde buildup and flushing reaction that is strongly **protective** against AUD (odds ratios for protection commonly reported 1.2–1.8 per allele; the variant is one of the most replicated genome-wide-significant hits across alcohol-phenotype GWAS).
  - **ALDH2** (aldehyde dehydrogenase 2, mitochondrial; HGNC:404) — the East Asian–specific loss-of-function variant **rs671** (Glu504Lys, ALDH2*2) impairs acetaldehyde clearance, producing the "Asian flushing" reaction; it is the single largest-effect protective variant known for alcohol consumption/AUD in East Asian populations (Science Advances 2023/2024 genotype-stratified Japanese GWAS; PMID for Edenberg's foundational review: 17718403).
  - **ADH1C, ADH4** — additional class I/II ADH cluster genes on chr4q23 in linkage disequilibrium with ADH1B, contributing modestly.
- **Reward/neurotransmission genes:**
  - **GABRA2** (GABA-A receptor alpha-2 subunit; HGNC:4083) — one of the earliest and most replicated non-metabolic AUD/alcohol-dependence association genes (Edenberg et al., *Am J Hum Genet* 2004, PMID: 15024690), implicating GABAergic inhibitory tone in dependence risk.
  - **KLB** (beta-klotho, co-receptor for FGF21; chr4q14) — index SNP **rs11940694** associated with AUDIT total score/alcohol consumption across multiple large GWAS; mechanistically links to a liver–brain FGF21 endocrine axis regulating alcohol preference.
  - **GCKR** (glucokinase regulator) — replicated locus linking alcohol consumption to glucose/lipid metabolism pathways.
  - **OPRM1** (mu-opioid receptor; HGNC:8156) — the **rs1799971 (A118G)** variant has been extensively studied as a moderator of naltrexone treatment response (pharmacogenomic significance; see §12) though large prospective genotype-stratified trials have failed to confirm a clinically actionable effect.
- **Large-scale multi-ancestry GWAS:** Zhou et al. (*Nature Medicine*, 2023; cross-ancestry meta-analysis of **1,079,947 individuals** — European N=903,147, African N=122,571, Latin American N=38,962, East Asian N=13,551, South Asian N=1,716) identified **110 independent risk variants** for "problematic alcohol use," with fine-mapping and gene-expression/chromatin-interaction prioritization implicating additional brain-expressed genes beyond the classical metabolic loci; a related multi-ancestry cross-disorder pleiotropy analysis (*Nature Mental Health*, 2024) further links AUD risk loci to psychiatric cross-disorder liability.
- **Polygenic architecture:** As with most psychiatric traits, common-variant SNP heritability is substantial but individual locus effects (outside ADH1B/ALDH2) are small (odds ratios typically 1.03–1.10), consistent with a highly polygenic trait amenable to polygenic risk scoring but not single-gene diagnostic testing.
- **Modifier/pleiotropic genes:** Genome-wide genetic correlations link AUD risk to major depressive disorder, ADHD, schizophrenia, and other substance use disorders (shared liability/"externalizing" and "internalizing" genetic factors), consistent with the high phenotypic psychiatric comorbidity described in §5/§11.

### Environmental Risk Factors
- Early age of drinking onset; heavy episodic ("binge") drinking patterns; chronic stress and adverse childhood experiences/trauma (including PTSD); family/peer alcohol use and permissive social norms; low socioeconomic status and unemployment; occupational alcohol access; psychiatric comorbidity (self-medication hypothesis); male sex (higher prevalence, though the gap is narrowing); comorbid nicotine/other substance use; alcohol outlet density and marketing exposure; and — per Global Burden of Disease trend analyses — rising per-capita alcohol availability in medium-to-high sociodemographic-index regions, particularly pronounced in Eastern Europe (Frontiers in Public Health 2025 GBD working-age trend analysis, PMC12336152).

### Protective Factors
- **Genetic:** ADH1B*2 (rs1229984) and ALDH2*2 (rs671), as above — the clearest examples of genetically protective alleles for any common psychiatric/behavioral disorder.
- **Environmental:** Religious/cultural abstinence norms, strong family cohesion and monitoring, delayed drinking-onset policies (minimum legal drinking age), alcohol taxation/pricing policy, restricted outlet density, and access to early intervention/brief counseling.

### Gene-Environment Interactions
The genotype-stratified 2023/2024 Japanese GWAS (175,672 individuals; Science Advances) is a landmark **G×E-adjacent design**: because ALDH2 rs671 genotype strongly gates the physiological consequence of drinking, stratifying by rs671 genotype revealed genome-wide-significant interaction signals at several loci (in addition to the three loci significant in wild-type homozygotes: GCKR, KLB, ADH1B), demonstrating that genetic background modulates how strongly environmental alcohol exposure translates into consumption/AUD risk. More broadly, stressful environments and early-life adversity are hypothesized to interact with GABAergic/HPA-axis genetic variation to potentiate AUD risk (a widely cited but still maturing area of human GxE research, largely built on candidate-gene rather than genome-wide interaction studies to date).

---

## 3. Phenotypes

AUD phenotypes span behavioral/psychiatric symptoms (the DSM-5 diagnostic criteria), physiological withdrawal/tolerance signs, and downstream organ-system complications from chronic use.

### Core DSM-5 diagnostic symptom domains (11 criteria, ≥2 required within 12 months for diagnosis)
1. Drinking more/longer than intended (impaired control)
2. Persistent desire or unsuccessful efforts to cut down
3. Great deal of time spent obtaining/using/recovering from alcohol
4. **Craving** — strong desire/urge to drink
5. Failure to fulfill major role obligations (social impairment)
6. Continued use despite social/interpersonal problems caused by alcohol
7. Important activities given up/reduced because of drinking
8. Recurrent use in physically hazardous situations (risky use)
9. Continued use despite knowledge of physical/psychological problems caused by alcohol
10. **Tolerance** — need for markedly increased amounts for the same effect
11. **Withdrawal** — characteristic withdrawal syndrome, or use to relieve/avoid withdrawal

### Acute intoxication phenotypes
Slurred speech, incoordination, unsteady gait, nystagmus, impaired attention/memory, stupor/coma at high blood alcohol concentration; behavioral disinhibition, mood lability.
- Suggested HPO: **HP:0001350** (Slurred speech), **HP:0001288** (Gait disturbance), **HP:0000639** (Nystagmus), **HP:0001269** (Abnormality of the nervous system — parent term where specific descendants are lacking)

### Alcohol withdrawal syndrome (onset hours after cessation in a physiologically dependent individual)
- **Minor withdrawal (6–24h):** tremor, anxiety, headache, GI upset, insomnia, autonomic hyperactivity (tachycardia, diaphoresis, hypertension). Suggested HPO: **HP:0002378** (Tremor)/**HP:0030955**, **HP:0000738** (Anxiety), **HP:0002099** (Tachypnea, if relevant), **HP:0100543** (Cognitive impairment).
- **Withdrawal seizures:** typically generalized tonic-clonic, occurring within the first 12–48h. Suggested HPO: **HP:0002069** (Generalized tonic-clonic seizure).
- **Alcohol withdrawal delirium (Delirium Tremens):** the most severe manifestation, occurring 24–72h (occasionally later) after last drink in a minority of patients with withdrawal seizures; fluctuating consciousness disturbance, profound disorientation/confusion, visual/tactile hallucinations, fever, marked tachycardia, diaphoresis, hypertension (StatPearls NBK441882; PMC11069634 DT clinical review). Untreated mortality historically up to 15–20%, now much lower with benzodiazepine-based management. Suggested HPO: **HP:0000726** (Dementia — imprecise), **HP:0031466** or general **HP:0000708** (Behavioral abnormality); note HPO lacks a precise "delirium" term in common use — **best modeled via MONDO's own ICD-11 6C40.4 child term rather than forced HPO mapping.**

### Cognitive/psychiatric phenotypes
Impaired executive function, working memory, and decision-making (frontostriatal dysfunction); depressed mood; anxiety; irritability; sleep disturbance; anhedonia during protracted abstinence (part of the "negative affect" stage of the addiction cycle — see Mechanism). Suggested HPO: **HP:0000726**, **HP:0000716** (Depressivity), **HP:0000739** (Anxiety) mapped as available, **HP:0002360** (Sleep disturbance).

### End-organ complication phenotypes (chronic, downstream)
- **Hepatic:** steatosis → alcoholic hepatitis → fibrosis → cirrhosis. HP:0001397 (Hepatic steatosis), HP:0001394 (Hepatic fibrosis/Cirrhosis).
- **Neurological:** peripheral neuropathy (HP:0009830), cerebellar ataxia/degeneration (HP:0001251), Wernicke encephalopathy (thiamine-deficiency triad: confusion, ataxia, ophthalmoplegia) and Korsakoff amnestic syndrome, cognitive decline.
- **Cardiovascular:** cardiomyopathy (HP:0001638), hypertension, arrhythmia (atrial fibrillation — "holiday heart").
- **GI/pancreatic:** pancreatitis (HP:0001733), gastritis, esophageal varices.
- **Psychiatric comorbid conditions:** as detailed in §5/§11.

### Phenotype characteristics
- **Onset:** Typically emerges in **late adolescence to young adulthood** (peak initiation age 18–25), though diagnostic threshold crossing (moderate/severe AUD) often occurs later after years of escalating use; late-onset AUD (>40–50 years) is a recognized, often better-prognosis subtype.
- **Severity:** DSM-5 stratifies mild/moderate/severe by symptom count; severity correlates with likelihood of withdrawal complications and treatment resistance.
- **Progression:** Variable — can be chronic-progressive, episodic/relapsing-remitting (the modal pattern, with periods of abstinence/moderation punctuated by relapse), or, in a substantial minority, spontaneously remitting without formal treatment ("natural recovery," more common in milder cases).
- **Frequency (US NESARC-III):** 12-month prevalence of DSM-5 AUD ≈ **13.9%**; lifetime prevalence ≈ **29.1%** (Grant et al., *JAMA Psychiatry* 2015, PMID: 26039070).

### Quality of Life Impact
AUD is a leading contributor to global disability-adjusted life years (DALYs) among behavioral/substance disorders (Global Burden of Disease). Impacts span occupational/functional impairment, relationship breakdown, legal/financial consequences, and markedly reduced health-related quality of life scores (EQ-5D/SF-36 domains), compounded further once end-organ complications (cirrhosis, neuropathy, cognitive decline) develop.

---

## 4. Genetic/Molecular Information

### Causal/Major-Effect Genes (complex trait — no monogenic Mendelian cause; these are the largest-effect common-variant loci)
| Gene | HGNC | Locus | Variant | Effect |
|---|---|---|---|---|
| ADH1B | HGNC:249 | 4q23 | rs1229984 (His48Arg) | Protective — fast ethanol oxidation → acetaldehyde buildup |
| ALDH2 | HGNC:404 | 12q24.12 | rs671 (Glu504Lys) | Strongly protective (East Asian populations) — impaired acetaldehyde clearance |
| ADH1C | HGNC:251 | 4q23 | in LD with ADH1B | Modest, population-dependent |
| GABRA2 | HGNC:4083 | 4p12 | multiple intronic/regulatory SNPs | Risk — GABAergic inhibitory signaling |
| KLB | HGNC:24578 | 4q14.1 | rs11940694 | Risk — FGF21 co-receptor, consumption phenotype |
| GCKR | HGNC:4196 | 2p23.3 | rs1260326 (and others) | Risk — metabolic pathway pleiotropy |
| OPRM1 | HGNC:8156 | 6q25.2 | rs1799971 (A118G) | Modifier of opioidergic reward signaling; naltrexone response modifier (contested) |

### Pathogenic Variants / Classification
AUD is **not classified under ACMG/AMP pathogenicity tiers** (pathogenic/likely pathogenic/VUS) because it is a polygenic complex trait, not a monogenic Mendelian condition; ClinVar does not carry AUD-specific variant classifications. Variant-level evidence instead comes from **GWAS association statistics** (odds ratios, p-values, fine-mapping posterior probabilities) rather than clinical variant curation.
- **Allele frequency:** ADH1B*2 (rs1229984) is common in East Asian (~70%) populations and less common in European (~5–10%) and rare in African populations; ALDH2*2 (rs671) allele frequency is ~30–50% in East Asian populations and essentially absent elsewhere (gnomAD, 1000 Genomes population panels).
- **Origin:** Germline, common polymorphisms (not somatic).
- **Functional consequence:** ADH1B*2 = gain-of-function (faster catalytic turnover) in ethanol oxidation; ALDH2*2 = dominant-negative loss-of-function in the tetrameric mitochondrial ALDH2 enzyme (heterozygotes show substantial enzyme inactivation due to the dominant-negative effect of the mutant subunit within the homotetramer).

### Modifier Genes
Genes in the "externalizing" and psychiatric cross-disorder polygenic factors (e.g., loci shared with ADHD, MDD, schizophrenia via genetic correlation) act as risk modifiers rather than primary causal loci; *DRD2*, *CHRM2*, *SLC6A4* (serotonin transporter) have candidate-gene literature of variable replication.

### Epigenetic Information
Chronic alcohol exposure is associated with genome-wide DNA methylation changes in blood and brain tissue, particularly at genes involved in immune signaling, neurodevelopment, and *ALDH2*/*ADH* loci themselves; histone modification changes (e.g., altered H3K4/H3K9 methylation, histone acetylation via HDAC inhibition by acetaldehyde metabolites) in reward-circuit brain regions have been implicated in the maintenance of compulsive drinking behavior in preclinical models. Human epigenome-wide association studies (EWAS) of AUD have identified differentially methylated regions overlapping known GWAS loci (JCI review of AUD human genetics/epigenetics, 2023–2024, JCI 172885).

### Chromosomal Abnormalities
Not a feature of AUD — no recurrent aneuploidy, translocation, or CNV syndrome is causally implicated; AUD is excluded from chromosomal-abnormality databases (DECIPHER, ECARUCA) as it is not a genomic disorder in that sense.

---

## 5. Environmental Information

- **Environmental/toxicological factor:** Ethanol (CHEBI:16236) itself is the causal exposure — a CNS depressant and hepatotoxin metabolized primarily via ADH→acetaldehyde (CHEBI:15343, a Group 1 IARC carcinogen)→ALDH→acetate.
- **Lifestyle factors:** Binge drinking pattern (≥4/5 drinks for women/men in ~2 hours), drinking frequency and quantity, co-use with nicotine/other substances, diet (poor nutrition, thiamine deficiency risk), sedentary behavior, sleep disruption.
- **Infectious agents:** Not a primary etiological factor for AUD itself, though chronic AUD is a major risk factor for infection susceptibility (immune suppression) and complicates management of infections such as hepatitis B/C (shared risk behaviors) and tuberculosis reactivation.
- **Socioenvironmental/structural factors:** Alcohol marketing and outlet density, price/taxation policy, occupational exposure (hospitality/service industries), cultural/religious drinking norms, and adverse childhood experiences (ACEs)/trauma exposure, which is one of the most robust non-genetic risk amplifiers documented in the epidemiological literature.

---

## 6. Mechanism / Pathophysiology

AUD pathophysiology is best conceptualized (Koob & Volkow's addiction-cycle model, *Lancet Psychiatry* 2016, PMID: 27475769) as progression through three recurring, neuroadapting stages: **binge/intoxication → withdrawal/negative affect → preoccupation/anticipation (craving)**, each mapped to a distinct but interconnected brain circuit.

### Molecular pathways and neurotransmitter systems
- **GABAergic potentiation (acute):** Ethanol acutely **potentiates GABA-A receptor**–mediated inhibitory neurotransmission (positive allosteric modulation), producing sedative/anxiolytic acute effects. Ventral tegmental area (VTA) GABA interneurons are implicated in alcohol reward: ethanol increases VTA dopamine neuron firing partly via **inhibition of GABA release onto dopaminergic neurons** (disinhibition mechanism) (PMC5605989; troscriptions/GABA review synthesis; Knowledge atlas bibliometric review PMC9411946).
- **Glutamatergic suppression (acute) → glutamatergic hyperexcitability (chronic):** Acute ethanol **inhibits NMDA receptor**–mediated glutamatergic transmission; chronic exposure produces a compensatory **upregulation/sensitization of NMDA and other glutamate receptor signaling**, so that upon alcohol cessation the CNS is left in a hyperglutamatergic, hyperexcitable state — the principal mechanism underlying withdrawal hyperexcitability, tremor, and seizures (PMC4407613, "Targeting glutamate uptake to treat AUD"; PMC9411946).
- **Mesolimbic dopamine system:** Acute alcohol increases dopamine release in the **nucleus accumbens** via VTA disinhibition, mediating acute reward. With repeated/chronic exposure, there is a **reduction in baseline mesolimbic dopaminergic tone** during withdrawal/abstinence — the "reward deficit" that drives negative affect and relapse vulnerability (Koob, *Curr Top Behav Neurosci* 2013, PMID: 24273570; MDPI AUD Neurobiology and Therapeutics review, 2022).
- **Opioidergic system:** Ethanol triggers endogenous opioid (beta-endorphin) release, which stimulates VTA dopamine neurons via mu-opioid receptor (OPRM1)–mediated disinhibition of GABAergic interneurons — the mechanistic basis for opioid-antagonist pharmacotherapy (naltrexone; see §12).
- **HPA axis and extended amygdala stress systems:** Chronic alcohol exposure dysregulates corticotropin-releasing factor (CRF) signaling in the **central nucleus of the amygdala** and **bed nucleus of the stria terminalis**, producing a sensitized stress response that drives negative-affect-motivated drinking during withdrawal — a key target of experimental CRF1-antagonist and related pharmacotherapies.

### Cellular processes
Neuroinflammation (microglial activation via TLR4 signaling in response to ethanol/acetaldehyde), oxidative stress, mitochondrial dysfunction (notably in hepatocytes, driving alcoholic liver disease — feeds into the dismech `hepatic_steatosis_lipotoxicity` and `drug_induced_liver_injury`-adjacent mechanism space), synaptic pruning/remodeling in prefrontal cortex reducing top-down inhibitory control over subcortical reward circuitry, and apoptosis of thiamine-dependent neurons in Wernicke-Korsakoff pathology.

### Protein dysfunction / biochemical abnormalities
- Enzymatic: ADH/ALDH functional variation (see §4) directly alters the toxic acetaldehyde intermediate's accumulation — the central biochemical determinant of both flushing reactions and long-term carcinogenic/hepatotoxic risk.
- Receptor-level: NMDA receptor subunit composition shifts (increased GluN2B expression) with chronic exposure; GABA-A receptor subunit composition changes (e.g., altered alpha4/delta subunit expression) underlying tolerance.

### Metabolic changes
Ethanol oxidation consumes NAD+ (shifting hepatocyte NADH:NAD+ ratio), promoting lipogenesis and inhibiting fatty acid oxidation and gluconeogenesis — the direct biochemical driver of hepatic steatosis; chronic heavy drinking also produces caloric substitution/malnutrition and thiamine (vitamin B1) deficiency, precipitating Wernicke encephalopathy.

### Immune system involvement
Chronic alcohol exposure activates innate immune signaling (TLR4/NF-kB pathway) in both liver (Kupffer cells) and brain (microglia), producing a pro-inflammatory state that contributes both to alcoholic liver disease progression and to neuroinflammation-driven negative affect/craving.

### Tissue damage mechanisms
Oxidative stress (reactive oxygen species from CYP2E1-mediated ethanol metabolism, induced with chronic heavy use), acetaldehyde protein/DNA adduct formation (carcinogenic mechanism), and progressive fibrosis (activated hepatic stellate cells — connects directly to the dismech `fibrotic_response` module architecture) in the liver; excitotoxic and oxidative neuronal injury in the CNS.

### Molecular profiling
- **Transcriptomics:** Postmortem and preclinical brain expression studies (GEO, GTEx-adjacent AUD brain expression datasets) show altered expression of genes in myelination, synaptic transmission, and immune pathways in prefrontal cortex of individuals with AUD.
- **Proteomics/metabolomics:** Serum biomarkers of chronic heavy use include elevated carbohydrate-deficient transferrin (CDT), phosphatidylethanol (PEth — a direct ethanol metabolite biomarker with high specificity), and gamma-glutamyl transferase (GGT).
- **Single-cell/spatial:** Emerging single-nucleus RNA-seq studies of postmortem AUD prefrontal cortex and amygdala tissue (Human Cell Atlas-adjacent efforts) are beginning to resolve cell-type-specific transcriptional signatures (microglial activation states, oligodendrocyte/myelination changes) associated with chronic alcohol exposure (PMC11566292, "Modeling Brain Gene Expression in AUD with Genetic Animal Models," 2024).

### Suggested ontology terms
- **GO (biological process):** GO:0035249 (synaptic transmission, glutamatergic); GO:0051932 (synaptic transmission, GABAergic); GO:0007268 (chemical synaptic transmission); GO:0006066 (alcohol metabolic process); GO:0006979 (response to oxidative stress); GO:0032496 (response to lipopolysaccharide, for neuroinflammatory signaling).
- **CL (cell types):** dopaminergic neuron (VTA), GABAergic interneuron, hepatic stellate cell, Kupffer cell, microglial cell — exact CL CURIEs should be confirmed via OAK/OLS before KB entry.
- **CHEBI:** ethanol (CHEBI:16236), acetaldehyde (CHEBI:15343), acetate (CHEBI:30089).

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary:** Brain (mesocorticolimbic reward circuitry) and liver (primary site of metabolism and chronic toxic injury).
- **Secondary/complication organs:** Pancreas (pancreatitis), heart (cardiomyopathy, arrhythmia), peripheral nervous system (neuropathy), GI tract (gastritis, esophageal varices from portal hypertension), immune system (impaired host defense).
- **Body systems:** Nervous system (central and peripheral), hepatobiliary system, cardiovascular system, digestive system, endocrine system (HPA axis dysregulation).

### Tissue/cell level
- Neurons (dopaminergic VTA neurons, GABAergic interneurons, glutamatergic pyramidal neurons of prefrontal cortex), microglia, astrocytes; hepatocytes and hepatic stellate cells; pancreatic acinar cells; cardiomyocytes.

### Subcellular level
- Mitochondria (site of ALDH2 activity and oxidative-stress generation), synaptic membrane receptor complexes (GABA-A, NMDA receptor), endoplasmic reticulum (unfolded protein response in hepatocytes under ethanol-metabolic stress).

### Localization (brain circuitry — key nodes)
- Ventral tegmental area (VTA) — dopaminergic cell bodies
- Nucleus accumbens (ventral striatum) — reward/binge-intoxication node
- Central nucleus of the amygdala / extended amygdala — withdrawal/negative-affect node
- Prefrontal cortex (particularly orbitofrontal and dorsolateral) — preoccupation/craving, impaired executive control
- Bed nucleus of the stria terminalis — stress-integration node
- Hippocampus — memory/conditioned-cue association with drinking contexts

Suggested UBERON terms (verify exact CURIEs before curation use): ventral tegmental area, nucleus accumbens, amygdala, prefrontal cortex, liver (UBERON:0002107), pancreas, heart.

---

## 8. Temporal Development

- **Onset:** Modal initiation of alcohol use in adolescence; problematic use/AUD symptom crossing typically emerges in the late teens to twenties, though clinically significant AUD can be diagnosed at any adult age. Earlier age of drinking onset is itself a well-established risk factor for later AUD severity.
- **Onset pattern:** Typically insidious/gradual escalation over months to years, though acute severe intoxication episodes and withdrawal syndromes are themselves acute events superimposed on the chronic underlying disorder.
- **Disease stages:** Mild/moderate/severe by DSM-5 symptom count; clinically often staged as at-risk/hazardous use → harmful use → dependence, paralleling ICD-11's harmful-pattern-of-use vs. dependence distinction.
- **Progression rate/course:** Highly variable — chronic-relapsing course is most typical, with the majority of individuals cycling through periods of abstinence, moderation, and relapse (NESARC longitudinal follow-up data); a substantial minority (especially milder cases) achieve natural remission without formal treatment.
- **Duration:** Can be lifelong/chronic if untreated, though average time from AUD onset to first treatment contact is often many years (a documented treatment gap).
- **Remission patterns:** Both spontaneous ("maturing out," more common with milder AUD and with life transitions such as marriage/parenthood/employment) and treatment-induced remission occur; formal remission criteria (DSM-5: early remission ≥3 but <12 months, sustained remission ≥12 months without criteria met, except craving) are defined.
- **Critical periods:** Adolescence/young adulthood represents a neurodevelopmental window of heightened vulnerability, as the prefrontal cortex (executive control) matures later than subcortical reward circuitry, and early heavy exposure during this window produces more durable neuroadaptation.

---

## 9. Inheritance and Population

### Epidemiology
- **Global prevalence (GBD 2023/2021 estimates):** ~111.12 million people worldwide with AUD in 2021 (per Global Burden of Disease modeling reported via Our World in Data/IHME), representing a **14.66% increase in prevalence between 2000 and 2021**. Age-standardized incidence, mortality, and DALY rates have generally *declined* from 1990–2021 even as absolute case counts (and burden in medium-to-high sociodemographic-index regions, especially Eastern Europe) have risen (Frontiers in Public Health 2025, PMC12336152).
- **US-specific (NESARC-III, DSM-5 criteria):** 12-month prevalence **13.9%**; lifetime prevalence **29.1%** (Grant et al. 2015, PMID: 26039070).

### Inheritance pattern
**Complex/multifactorial (polygenic) inheritance** — not Mendelian. No single gene is necessary or sufficient; risk is conferred by the additive/interactive effect of many common variants (see §4) combined with environmental exposure.
- **Penetrance:** Not applicable in the Mendelian sense; better described via polygenic liability-threshold models, where genetic loading + environmental exposure must exceed a threshold for the clinical phenotype to manifest.
- **Expressivity:** Highly variable — symptom profile, severity, and course differ substantially between individuals with similar genetic loading, reflecting the dominant role of environmental/behavioral exposure.
- **Genetic anticipation, germline mosaicism, chromosomal founder effects:** Not applicable (not a repeat-expansion or single-gene Mendelian disorder).
- **Founder-effect-like population variation:** ALDH2*2 (rs671) and ADH1B*2 (rs1229984) show marked population-specific allele frequency differences (East Asian populations carry much higher frequencies of both protective alleles than European or African populations), producing genuine population-level differences in AUD prevalence and alcohol-flush phenotype that are population-genetic in origin (not classical single-family founder effects).
- **Consanguinity:** Not a relevant risk modifier for a polygenic behavioral trait of this kind.
- **Carrier frequency:** Not applicable (no single causal allele to carry).

### Population demographics
- **Sex ratio:** Historically strongly male-predominant (~2:1 to 3:1 male:female in most population surveys), though the gap has been narrowing in recent US/European cohorts, particularly among younger birth cohorts.
- **Geographic distribution:** Highest age-standardized burden concentrated in Eastern Europe and parts of the former Soviet Union; substantial variation globally tied to per-capita alcohol consumption, religious/cultural abstinence norms (lower burden in many Muslim-majority countries), and alcohol policy environments.
- **Ethnic/ancestry variation:** Markedly lower alcohol consumption and AUD prevalence in East Asian populations carrying high frequencies of ALDH2*2/ADH1B*2 protective alleles; Indigenous populations in some regions show elevated AUD burden associated with a complex mix of socioeconomic marginalization, historical trauma, and, in some studies, differing ADH/ALDH allele frequencies.
- **Age distribution:** Prevalence peaks in young adulthood (18–29) and generally declines with age, though a meaningful late-onset subgroup exists.

---

## 10. Diagnostics

### Clinical tests / laboratory
- **Direct alcohol biomarkers:** Blood alcohol concentration (acute intoxication); **phosphatidylethanol (PEth)** — a direct, highly specific biomarker of recent heavy alcohol use with a longer detection window (~2–4 weeks) than ethanol itself; ethyl glucuronide (EtG) and ethyl sulfate (EtS) in urine/hair for abstinence monitoring.
- **Indirect biomarkers:** Elevated gamma-glutamyl transferase (GGT), carbohydrate-deficient transferrin (CDT), mean corpuscular volume (MCV, macrocytosis), AST:ALT ratio typically >2 in alcoholic hepatitis (vs. viral hepatitis where ALT>AST).
- **Imaging:** Liver ultrasound/elastography (steatosis, fibrosis staging), brain MRI (cerebellar/cortical atrophy in chronic heavy use, mammillary body changes in Wernicke encephalopathy).
- **Biopsy/histopathology:** Liver biopsy showing steatosis, Mallory-Denk bodies, and neutrophilic infiltration in alcoholic hepatitis; progression to bridging fibrosis/cirrhosis on later biopsy.

### Genetic testing
Not part of routine clinical diagnosis — AUD diagnosis is entirely clinical/behavioral (DSM-5/ICD-11 criteria), not confirmed via genetic testing. Research-context genotyping of ADH1B/ALDH2 is occasionally used in pharmacogenomic or population-genetics research contexts (and is directly clinically relevant when disulfiram or disulfiram-like reactions are anticipated), but there is no clinical genetic panel, WGS/WES indication, or GTR-listed diagnostic test for AUD itself.

### Clinical diagnostic criteria
- **DSM-5** (11-criterion symptom count, mild/moderate/severe severity tiers) — the primary US clinical/research diagnostic standard.
- **ICD-11** (6C40 series) — distinguishes harmful pattern of use from dependence using a somewhat different (narrower, more clinically focused) criteria set than DSM-5, a distinction actively discussed in the nosology literature (Saunders 2019, PMID: 31194891; PMC6899584 critique).
- **Screening instruments:** **AUDIT** (Alcohol Use Disorders Identification Test, WHO-developed, 10-item) and its short form **AUDIT-C** (3-item) are the dominant quantitative screening/phenotyping tools used both clinically and as the continuous phenotype in most large-scale genetic association studies; **CAGE** questionnaire is a simpler 4-item clinical screen.
- **Differential diagnosis:** Other substance use disorders, primary mood/anxiety disorders (which can both cause and result from heavy drinking), and other causes of the downstream organ phenotypes (e.g., non-alcoholic fatty liver disease, viral hepatitis for liver findings; other causes of peripheral neuropathy/ataxia).

### Screening
Universal primary-care screening with AUDIT-C is recommended by USPSTF for adults, followed by brief intervention/referral to treatment ("SBIRT" model) for those screening positive.

---

## 11. Outcome/Prognosis

### Survival and mortality
AUD substantially elevates all-cause mortality, chiefly through liver disease (cirrhosis, hepatocellular carcinoma), cardiovascular disease, alcohol-related cancers (esophageal, liver, breast, colorectal — ethanol/acetaldehyde is an IARC Group 1 carcinogen), unintentional injury, and suicide. Age-standardized AUD-attributable mortality has declined globally from 1990–2021 even as absolute burden has risen with population growth (GBD trend analyses, PMC12336152).

### Morbidity and functional outcomes
Substantial disability contribution captured in global DALY estimates; functional impairment spans occupational, relationship, cognitive (frontostriatal executive dysfunction persisting into abstinence in a subset of patients), and legal/financial domains. Quality-of-life measures (EQ-5D, SF-36) are consistently reduced in active AUD relative to the general population and improve, though often not fully normalize, with sustained remission.

### Disease course / complications
Progressive liver disease (steatosis → hepatitis → fibrosis → cirrhosis → hepatocellular carcinoma), Wernicke-Korsakoff syndrome, cardiomyopathy, pancreatitis, peripheral neuropathy, immune suppression/infection susceptibility, and high rates of co-occurring psychiatric illness (below).

### Psychiatric comorbidity (major prognostic driver)
- Comorbid **major depressive disorder**, **anxiety disorders** (including generalized anxiety, panic, and especially **social anxiety disorder** — lifetime comorbidity with AUD ≈2.4% in the general population, with social anxiety disorder associated with OR≈2.8 for alcohol dependence and OR≈1.2 for alcohol abuse; PMC2917264), **PTSD**, and **bipolar disorder** are all substantially elevated among individuals with AUD (PMC7006178 review of psychiatric comorbidities in AUD).
- Among individuals with alcohol-associated liver disease specifically, nationwide data (2015–2023) show significantly increased prevalence of MDD, anxiety, and PTSD in both cirrhotic and non-cirrhotic groups relative to the general population (Digestive Diseases and Sciences 2025 nationwide trend study).
- Top physical comorbidities in treatment-seeking AUD populations include hypertension, asthma, dyslipidemia, and liver enzyme abnormalities (PMC8783789 pilot comorbidity study).

### Prognostic factors
Earlier treatment engagement, milder baseline severity, absence of psychiatric comorbidity, strong social support, and abstinence-oriented treatment adherence predict better outcomes; conversely, comorbid psychiatric illness, severe dependence (high symptom count), early-onset drinking, and ongoing high-risk environmental exposure predict poorer prognosis and higher relapse risk.

---

## 12. Treatment

### Pharmacotherapy (FDA-approved)
Three medications are FDA-approved specifically for AUD:
1. **Naltrexone** (oral, approved 1994; long-acting injectable/Vivitrol, approved 2006) — mu-opioid receptor antagonist; reduces heavy drinking and helps prevent return to heavy drinking after a lapse by blunting the reinforcing/rewarding effects of alcohol. NCIT: Pharmacotherapy (NCIT:C15986); therapeutic_agent naltrexone.
2. **Acamprosate** (Campral, approved 2004) — modulates glutamatergic/GABAergic balance (putative NMDA receptor modulation), normalizing the post-withdrawal hyperglutamatergic state; supports abstinence maintenance with modest effect size; dosed three times daily (2 tablets/dose).
3. **Disulfiram** (Antabuse) — irreversibly inhibits **aldehyde dehydrogenase**, so that alcohol consumption causes acetaldehyde accumulation and an aversive "disulfiram-ethanol reaction" (flushing, nausea, vomiting, headache, hypotension) — a deterrent/aversion-based mechanism rather than an anti-craving mechanism.

### Off-label / commonly used pharmacotherapy
Topiramate (glutamate/GABA modulation), gabapentin (particularly for withdrawal-adjacent anxiety/insomnia and protracted abstinence symptoms), baclofen (GABA-B agonist, used especially in some European countries and in hepatically impaired patients).

### Emerging / investigational pharmacotherapy
**GLP-1 receptor agonists** are an actively emerging investigational class: a phase 2 randomized clinical trial of once-weekly **semaglutide** in AUD (enrollment Sept 2022–Feb 2024) found that low-dose semaglutide reduced alcohol consumption in a laboratory self-administration paradigm and significantly reduced weekly alcohol craving relative to placebo over 9 weeks, though effects on other consumption measures were mixed (published *JAMA Psychiatry*-family journal, PMID: 39937469; PMC11822619). A more recent randomized, double-blind, placebo-controlled trial in patients with AUD **and comorbid obesity** (published in *The Lancet*, 2026) reported alcohol consumption reductions of over 70% after 26 weeks of semaglutide treatment. NIH-funded work has also shown that adding weekly GLP-1 therapy to cognitive behavioral therapy further reduces heavy drinking days. Mechanistically, GLP-1 receptor signaling in reward-circuit regions (VTA, nucleus accumbens) is hypothesized to blunt alcohol's dopaminergic reinforcing effects, paralleling the class's established appetite/reward-modulating action in obesity and other addictive behaviors. Other agents under investigation in the search results include lacosamide (sodium channel modulator), pitolisant (histamine H3 antagonist/inverse agonist), and N-acetylcysteine (antioxidant/glutamatergic modulation), the latter studied specifically in veterans with comorbid TBI.

### Pharmacogenomics
CPIC has issued naltrexone pharmacogenomic guidance considering both pharmacodynamic (**OPRM1** rs1799971/A118G) and pharmacokinetic (**ADH**, **ALDH**) genes. The OPRM1 G-allele has been associated with improved naltrexone response and lower relapse rates in some cohort/meta-analytic studies, but **prospective genotype-stratified randomized trials and rigorous meta-analyses have failed to confirm a clinically actionable effect**, and current evidence does not support routine clinical genotyping to guide naltrexone prescribing (PMC4165632; systematic review/meta-analysis literature on rs1799971).

### Psychosocial/behavioral treatment
Cognitive behavioral therapy (CBT), motivational enhancement therapy, 12-step facilitation/mutual-help group participation (Alcoholics Anonymous), contingency management, and couples/family-based interventions are core evidence-based non-pharmacological treatments, often combined with pharmacotherapy for best outcomes (as illustrated by the CBT+GLP-1 combination trial above). NCIT: Behavioral Counseling / Therapeutic Procedure terms as available.

### Withdrawal management (acute)
Benzodiazepines (the mainstay for withdrawal seizure/delirium tremens prevention) administered on a symptom-triggered or fixed-schedule protocol (e.g., CIWA-Ar scale-guided), supportive care, and thiamine repletion (to prevent/treat Wernicke encephalopathy) prior to glucose administration.

### Treatment gaps and outcomes
Despite three FDA-approved medications, pharmacotherapy remains substantially underutilized in US treatment settings, and treatment response is heterogeneous — motivating the active pharmacogenomic and novel-mechanism (GLP-1, glutamatergic) research programs above.

---

## 13. Prevention

### Primary prevention
Minimum legal drinking age laws, alcohol taxation/pricing policy, restriction of alcohol marketing/advertising (particularly targeting youth), outlet density regulation, school- and community-based prevention programs targeting delayed drinking onset, and parental monitoring interventions.

### Secondary prevention (screening/early intervention)
Universal AUDIT-C screening in primary care with brief intervention and referral to treatment (SBIRT), USPSTF-recommended for all adults; early identification of hazardous/harmful use before progression to dependence.

### Tertiary prevention
Relapse-prevention pharmacotherapy and behavioral maintenance treatment; management of comorbid psychiatric illness to reduce self-medication-driven relapse; thiamine supplementation in at-risk chronic drinkers to prevent Wernicke-Korsakoff progression; vaccination and infection-prevention counseling given AUD-associated immune suppression.

### Genetic/risk counseling
While not a Mendelian disorder amenable to individual genetic counseling in the classical sense, family history discussion (given the well-established ~40–60% heritability) is a recognized part of risk communication in primary care and psychiatric practice, and population-level ALDH2/ADH1B genotype distribution informs public-health messaging in East Asian populations regarding flush-reaction and elevated esophageal cancer risk with continued heavy drinking despite the aversive reaction.

### Public health
Policy-level interventions (minimum unit pricing, taxation, marketing restriction, drunk-driving law enforcement) have the strongest population-level evidence base among all prevention strategies for reducing AUD-attributable morbidity/mortality (WHO Global Status Report on Alcohol and Health framework).

---

## 14. Other Species / Natural Disease

AUD as clinically defined is a human diagnostic construct; however, alcohol-preference and alcohol-dependence-like phenotypes are extensively modeled and, to a lesser degree, observed naturalistically across species:
- **NCBI Taxon:9606** (*Homo sapiens*) — the disease itself.
- No well-characterized **naturally occurring** veterinary/companion-animal AUD analog exists in the way that, e.g., diabetes or cancer have veterinary natural-disease counterparts (OMIA does not carry an AUD entry); alcohol-related pathology in other species is essentially always experimentally induced rather than naturally occurring.
- **Orthologous genes:** ADH1B and ALDH2 orthologs are present and functionally conserved across mammals (mouse *Adh1*, *Aldh2*), underpinning the validity of rodent metabolic/behavioral models.
- **Comparative biology:** The core mesocorticolimbic dopamine reward circuitry and its ethanol-responsive GABA/glutamate physiology are highly evolutionarily conserved from rodents to primates to humans, which is the biological basis for the strong translational utility of animal models (§15) despite AUD itself being a uniquely human diagnostic/behavioral construct.
- **Zoonotic potential:** Not applicable.

---

## 15. Model Organisms

A broad and mechanistically informative set of model systems is used to dissect AUD biology (Cservenka & Ray review and others; PMC6683838 "Animal Models for the Genetic Study of Human Alcohol Phenotypes"; PMC11566292, 2024 review of genetic animal models for brain gene expression in AUD; translational review PMC/Nature Translational Psychiatry 2021):

### Mammalian genetic/selectively-bred models
- **Selectively bred rat/mouse lines:** High Alcohol Preference (HAP) and Low Alcohol Preference (LAP) mouse lines (bred from HS/Ibg founders; cHAP = crossed HAP replicate lines) and the classic alcohol-preferring (P) vs. non-preferring (NP) rat lines model genetic variation in voluntary alcohol consumption.
- **High Drinking in the Dark (HDID)-1 and HDID-2 mice:** selectively bred over 20+ generations for reaching high blood alcohol concentrations in a binge-like "drinking in the dark" assay — models the binge-drinking phenotype specifically.
- **Knockout/transgenic/conditional models:** Gene-targeted mice (e.g., *Gabra2*, *Oprm1*, *Aldh2* knockouts/humanized alleles) used to causally test candidate genes identified in human GWAS; IMPC/KOMP/MGI-cataloged alcohol-related phenotyping data available for many such lines.
- **Non-human primates:** Used for studies requiring closer translational fidelity to human social drinking patterns, voluntary chronic self-administration, and neuroimaging-comparable circuit studies.

### Non-mammalian models
- **Zebrafish (*Danio rerio*):** Increasingly used given transparent embryos enabling live anatomical/circuit characterization and high-throughput genetic screening of alcohol-response behavior.
- **Drosophila melanogaster:** Shows conditioned place-preference-like responses to ethanol-paired cues and robust ethanol-induced behavioral sensitization/tolerance paradigms, exploiting powerful *Drosophila* genetic tools.
- **C. elegans:** A genetically fully tractable invertebrate model with conserved ethanol-response pathways, used both for mechanistic dissection and for small-molecule/therapeutic screening (PMC/ScienceDirect C. elegans AUD therapeutics screening literature).

### Model characteristics — phenotype recapitulation and limitations
Rodent models robustly recapitulate voluntary consumption, escape/withdrawal-associated hyperexcitability (tremor, seizure susceptibility), and core neurocircuit adaptations (mesolimbic dopamine blunting, glutamatergic sensitization) seen in human AUD. Limitations include the difficulty of modeling the complex, criterion-based DSM-5 psychiatric diagnosis (craving, social/role impairment) in non-verbal organisms, and cross-species differences in alcohol pharmacokinetics/metabolism rate that require careful dose calibration for translational validity — an important **human-model-fidelity caveat** analogous to the dismech schema's `HUMAN_MODEL_MISMATCH` discussion category, particularly relevant for translating rodent withdrawal-severity or craving-proxy behavioral assays to the human clinical phenotype.

### Applications
These models collectively support dissection of genetic risk-locus function (knockout/humanized-allele validation of GWAS hits), neurocircuit-level mechanism (optogenetic/chemogenetic manipulation of VTA-NAc-amygdala-PFC circuitry), withdrawal pharmacology (benzodiazepine/anticonvulsant testing), and preclinical efficacy screening for novel pharmacotherapies (e.g., the preclinical GLP-1RA evidence base that motivated the semaglutide human trials in §12).

### Resources
MGI, IMPC/KOMP (mouse gene-targeted lines and phenotyping), RGD (rat genomic resources for P/NP lines), ZFIN (zebrafish), FlyBase (*Drosophila*), WormBase (*C. elegans*), IMSR (strain repository).

---

## Summary Table: Suggested Ontology Term Anchors for KB Curation

| Domain | Suggested term (verify CURIE via OAK/OLS before committing) |
|---|---|
| Disease | OMIM:103780; ICD-11 6C40 series; MONDO CURIE — **unconfirmed, verify live** |
| Causal/risk genes | HGNC:249 (ADH1B), HGNC:404 (ALDH2), HGNC:4083 (GABRA2), HGNC:24578 (KLB), HGNC:4196 (GCKR), HGNC:8156 (OPRM1) |
| Chemicals | CHEBI:16236 (ethanol), CHEBI:15343 (acetaldehyde) |
| Biological processes | GO:0006066 (alcohol metabolic process), GO:0035249 (glutamatergic synaptic transmission), GO:0051932 (GABAergic synaptic transmission) |
| Anatomy | UBERON terms for ventral tegmental area, nucleus accumbens, amygdala, prefrontal cortex, liver — verify exact CURIEs |
| Phenotypes | HP:0002378/HP:0030955 (tremor), HP:0002069 (generalized tonic-clonic seizure), HP:0001394 (cirrhosis), HP:0009830 (peripheral neuropathy), HP:0001397 (hepatic steatosis) |
| Treatment | NCIT:C15986 (Pharmacotherapy) + therapeutic_agent naltrexone/acamprosate/disulfiram/semaglutide; NCIT term for Behavioral Counseling |

---

## Key Gaps / Items Needing Further Verification Before KB Entry
1. **Exact MONDO CURIE** for alcohol use disorder/alcohol dependence — not confirmed via live ontology lookup in this pass; must be resolved via OLS/Monarch before curation to avoid a mismatched identifier.
2. **Exact PMIDs** for the Zhou et al. 2023 *Nature Medicine* multi-ancestry GWAS and the 2024 *Nature Mental Health* cross-disorder pleiotropy paper were not independently confirmed to the numeric PMID in this pass — the papers and journals are correctly identified, but curators should run `just fetch-reference` against the specific PMID before citing.
3. **HPO coverage of AUD-specific behavioral/psychiatric criteria** (craving, impaired control, social impairment) is sparse — HPO is built for somatic/syndromic phenotypes, so most DSM-5 AUD criteria will need to be captured as free-text/`description` content rather than forced HP term bindings; only the physiological/withdrawal and end-organ-complication phenotypes map cleanly to existing HP terms.
4. **CL and UBERON exact CURIEs** for brain reward-circuit cell types and regions listed above are given at the recall/best-estimate level and should be independently verified with `runoak` before use in a schema-bound annotation.

Sources:
- [Alcohol Use Disorders in ICD-11: Past, Present, and Future - PubMed](https://pubmed.ncbi.nlm.nih.gov/31194891/)
- [Alcohol and Substance Use Disorders Diagnostic Criteria Changes and Innovations in ICD-11: An Overview - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9881115/)
- [ICD‐11 for Alcohol Use Disorders: Not a Convincing Answer to the Challenges - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6899584/)
- [Entry - #103780 - ALCOHOL DEPENDENCE - OMIM](https://omim.org/entry/103780)
- [Entry - *103720 - ALCOHOL DEHYDROGENASE 1B - OMIM](https://omim.org/entry/103720)
- [Human genetics and epigenetics of alcohol use disorder - JCI](https://www.jci.org/articles/view/172885)
- [Genetic architecture of alcohol consumption identified by a genotype-stratified GWAS...esophageal cancer risk in Japanese people - Science Advances](https://www.science.org/doi/10.1126/sciadv.ade2780)
- [Multi-ancestry study of the genetics of problematic alcohol use in over 1 million individuals - Nature Medicine](https://www.nature.com/articles/s41591-023-02653-5)
- [Identification of risk variants and cross-disorder pleiotropy through multi-ancestry genome-wide analysis of alcohol use disorder - Nature Mental Health](https://www.nature.com/articles/s44220-024-00353-8)
- [Global trends in the burden of alcohol use disorders in the working-age population from 1990 to 2021 and projections for the next 20 years - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12336152/)
- [Share of population with an alcohol use disorder, 2023 - Our World in Data](https://ourworldindata.org/grapher/share-with-alcohol-use-disorders)
- [Alcohol Use Disorder: Neurobiology and Therapeutics - MDPI](https://www.mdpi.com/2227-9059/10/5/1192)
- [Knowledge atlas of the involvement of glutamate and GABA in alcohol use disorder - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9411946/)
- [Role of GABAA receptors in alcohol use disorders suggested by chronic intermittent ethanol (CIE) rodent model - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5605989/)
- [Targeting glutamate uptake to treat alcohol use disorders - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4407613/)
- [Medications for the Treatment of Alcohol Use Disorder - NY OASAS](https://oasas.ny.gov/providers/medications-treatment-alcohol-use-disorder)
- [Trends in the Use of Naltrexone for Addiction Treatment among Alcohol Use Disorder Admissions - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8394149/)
- [Once-Weekly Semaglutide in Adults With Alcohol Use Disorder: A Randomized Clinical Trial - PubMed](https://pubmed.ncbi.nlm.nih.gov/39937469/)
- [Once-Weekly Semaglutide in Adults With Alcohol Use Disorder: A Randomized Clinical Trial - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11822619/)
- [Once-weekly semaglutide versus placebo in patients with alcohol use disorder and comorbid obesity - The Lancet](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(26)00305-3/fulltext)
- [Adding weekly GLP-1 to cognitive behavioral therapy further reduces heavy drinking - NIH](https://www.nih.gov/news-events/news-releases/adding-weekly-glp-1-cognitive-behavioral-therapy-further-reduces-heavy-drinking)
- [Animal Models for the Genetic Study of Human Alcohol Phenotypes - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6683838/)
- [Modeling Brain Gene Expression in Alcohol Use Disorder with Genetic Animal Models - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11566292/)
- [Translational opportunities in animal and human models to study alcohol use disorder - Translational Psychiatry](https://www.nature.com/articles/s41398-021-01615-0)
- [Ethanol-Related Behaviors in Mouse Lines Selectively Bred for Drinking to Intoxication - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7915226/)
- [Social Anxiety Disorder and Alcohol Use Disorder Comorbidity in NESARC - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2917264/)
- [Psychiatric comorbidities in alcohol use disorder - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7006178/)
- [Trends in Concurrent Psychiatric Comorbidities in Alcohol-Associated Liver Disease - Digestive Diseases and Sciences](https://link.springer.com/article/10.1007/s10620-025-09494-x)
- [Epidemiology of DSM-5 Alcohol Use Disorder: Results From NESARC-III - PubMed](https://pubmed.ncbi.nlm.nih.gov/26039070/)
- [Prevalence and Correlates of Physical Comorbidities in Alcohol Use Disorder (AUD) - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8783789/)
- [Alcohol Withdrawal Syndrome - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK441882/)
- [Delirium Tremens: A Review of Clinical Studies - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11069634/)
- [Pharmacogenetic approaches in the treatment of alcohol use disorders - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4165632/)
- [Association of µ-opioid receptor (OPRM1) gene polymorphism with response to naltrexone in alcohol dependence - PubMed](https://pubmed.ncbi.nlm.nih.gov/22515274/)