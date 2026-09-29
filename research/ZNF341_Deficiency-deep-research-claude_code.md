---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-23T19:28:45.817388'
end_time: '2026-09-23T19:33:30.966304'
duration_seconds: 285.15
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: ZNF341 Deficiency
  mondo_id: MONDO:0032654
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
  web_search_requests: 13
  num_turns: 21
  total_cost_usd: 1.4605926000000002
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 2
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: claude_code
  succeeded: true
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ZNF341 Deficiency
- **MONDO ID:** MONDO:0032654 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ZNF341 Deficiency** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

I'll research ZNF341 Deficiency (Hyper-IgE Syndrome 3, HIES3) using primary literature. Let me start by loading web research tools and searching for key sources.

# ZNF341 Deficiency (Autosomal Recessive Hyper-IgE Syndrome 3, HIES3): Comprehensive Research Report

**Source classes used throughout:** primary literature (original patient-cohort papers), a narrative review (Béziat et al. 2023, itself reporting two new patients), structured databases (OMIM, Orphanet, GeneCards/NCBI Gene), and one case report. Numeric phenotype-frequency data below are drawn from the 2023 review's aggregation of the published cohort (n=20 as of that publication) and are flagged as such — they are a secondary tabulation, not independently re-derived from each primary paper in this report.

---

## 1. Disease Information

**Overview.** ZNF341 deficiency is an autosomal recessive primary immunodeficiency that produces a phenocopy of autosomal-dominant STAT3 (Job/hyper-IgE) syndrome. It was first described in 2018 by two independent groups working with overlapping/related consanguineous kindreds, who found that biallelic loss-of-function variants in *ZNF341* — a zinc-finger transcription factor that transactivates the *STAT3* promoter — reduce basal STAT3 expression and abolish STAT3 "autoinduction," producing a milder, incompletely penetrant phenocopy of classic Job syndrome (Frey-Jakobs et al., *Sci Immunol* 2018, PMID 29907690; Béziat et al., *Sci Immunol* 2018, PMID 29907691; commentary by Al-Herz, PMID 29907692).

**Key identifiers:**
- **OMIM disease:** #618282 — Hyper-IgE syndrome 3, autosomal recessive, with recurrent infections (HIES3)
- **OMIM gene:** *618269 — ZINC FINGER PROTEIN 341; ZNF341
- **Orphanet:** ORPHA:641368 — Autosomal recessive hyper-IgE syndrome due to ZNF341 deficiency
- **HGNC:** HGNC:15992
- **NCBI Gene:** 84905
- **Cytogenetic location:** 20q11.22
- **MONDO:** MONDO:0032654 (as supplied in the task; not independently re-verified against the MONDO browser in this session — flag this as unverified/a lead)

**Synonyms:** Hyper-IgE syndrome 3 (HIES3); autosomal recessive Job syndrome; ZNF341-related hyper-IgE syndrome.

**Data provenance:** All clinical/phenotype-frequency data available to date derive from published case series aggregated across a small number of consanguineous kindreds (Moroccan, Afro-Caribbean, Iranian, Turkish, Lebanese, and Israeli Arab backgrounds per the 2023 review) — this is **aggregated case-series data**, not registry- or EHR-derived population data. No large administrative/claims-based cohort exists given the rarity of the condition.

---

## 2. Etiology

**Disease Causal Factor:** Purely genetic — biallelic (homozygous or compound heterozygous) loss-of-function variants in *ZNF341*. No environmental, infectious, or purely mechanistic (non-genetic) causal factor has been reported; this is a monogenic Mendelian disorder.

**Genetic risk factors:**
- Biallelic *ZNF341* LOF variants are causal, not merely a risk factor — this is a fully penetrant Mendelian loss-of-function disease at the molecular level (all reported homozygotes/compound heterozygotes are symptomatic), though clinical severity varies (see §9, expressivity).
- **Mutational hotspot:** p.Arg302* was found in 13 of the 20 reported patients across 6 independent kindreds (Béziat et al. 2023 review, PMC10620851) — consistent with either a true mutational hotspot (CpG-associated nonsense codon) or a shared/founder haplotype in populations with high consanguinity; the review does not resolve which, so this should be treated as an open question rather than settled founder-effect fact.
- Consanguinity is a strong risk-modifying factor given the autosomal recessive inheritance and small global patient count concentrated in consanguineous populations (Moroccan, Iranian, Turkish, Lebanese, Israeli Arab, Afro-Caribbean).

**Environmental risk factors:** None specifically implicated in disease causation. However, ionizing radiation is a documented **aggravating/harm-amplifying** exposure post-diagnosis (see Mechanism/Malignancy sections) — ZNF341-deficient leukocytes show impaired post-irradiation DNA repair (PMC9307231), which is a modifier of secondary risk (malignancy) rather than a cause of the primary immunodeficiency.

**Protective factors:** None reported in the literature located.

**Gene-environment interactions:** The one documented interaction is genotype × ionizing-radiation exposure increasing malignancy/DNA-damage risk (below), not a classical GxE susceptibility interaction for the primary disease.

---

## 3. Phenotypes

The table below reproduces the **frequency data as tabulated in the 2023 review** (Béziat et al., *Curr Opin Immunol*, PMID 37080116; PMC10620851), which aggregated all 20 published patients as of early 2023 and compared them to a STAT3-dominant-negative HIES reference cohort. This is a **secondary source's tabulation of primary case data** — treat percentages as approximate given n≈20.

| Phenotype (ZNF341-deficient) | Frequency | Suggested HPO term (unverified against HPO browser — lead only) |
|---|---|---|
| Atopic dermatitis / eczema | 100% | HP:0001047 Atopic dermatitis |
| Elevated IgE (>1000 IU/mL) | 85% | HP:0003212 Increased IgE level |
| High IgG (>16 g/L) | 83% | HP:0010702 (Abnormal immunoglobulin level, or a more specific IgG-elevation term — needs lookup) |
| Skin abscesses | 75% | HP:0031469 (skin abscess — verify) |
| Low NK cell counts/frequency | 67% | HP:0040088 Abnormal NK cell count |
| Chronic mucocutaneous candidiasis | 60% | HP:0002728 Chronic mucocutaneous candidiasis |
| Recurrent upper respiratory infections | 58% | HP:0002788 Recurrent respiratory infections |
| Eosinophilia | 58% | HP:0001880 Eosinophilia |
| Pneumonia | 56% | HP:0002090 Pneumonia |
| Facial dysmorphia | 53% | HP:0001999 Abnormal facial shape |
| High palate | 45% | HP:0000218 High palate |
| Bronchiectasis | 35% | HP:0002110 Bronchiectasis |
| Mental/developmental delay | 37% | HP:0001256 Intellectual disability, mild (or HP:0001263 Global developmental delay) |
| Deciduous tooth retention | 25% | HP:0006335 (retained primary teeth — verify exact ID) |
| Joint hyperextensibility | 15% | HP:0001382 Joint hypermobility |
| Growth retardation | 15% | HP:0001510 Growth delay |
| Newborn rash | 15% | HP:0001066 (neonatal dermatologic finding — verify) |
| Pneumatocele | 10% | HP:0025134 Pneumatocele |
| Scoliosis | 10% | HP:0002650 Scoliosis |

**Important caveat on HPO IDs:** Per this repository's ontology-term contract, I have **not** independently looked up each of these CURIEs in an HPO adapter this session — they are supplied from memory as candidates and must be verified (`runoak` lookup or `cache/hp/terms.csv`) before use in curation. Treat every ID above as a lead, not a checked binding.

**Onset/severity/progression:** Onset is generally in early childhood, paralleling classic Job syndrome, with atopic dermatitis as the earliest and most penetrant feature (100%). The review explicitly frames severity via the **NIH HIES clinical scoring system**: median score 28.5 in ZNF341-deficient patients vs. 64 in STAT3-deficient patients — a roughly two-fold lower composite severity score, supporting the "phenocopy but milder" characterization (PMC10620851, direct quote: "The clinical phenotype of patients with AR ZNF341 deficiency is essentially a phenocopy of AD STAT3 deficiency. However, it has milder consequences.").

**Distinguishing features vs. AD-STAT3 HIES** (important for differential/lump-split reasoning):
- **NK cell deficiency is a discriminating feature**: low NK cells/frequency in 67% of ZNF341-deficient patients vs. only 8% of STAT3-deficient patients.
- **Vascular complications (aneurysms, tortuosity) are absent** in the reported ZNF341 cohort ("none of the ZNF341-deficient patients were reported to have vascular complications") vs. 84% in STAT3-deficient patients — a notable negative finding, though it may partly reflect the smaller/younger cohort rather than a true mechanistic absence.
- **Higher IgG** despite low memory B cells in ZNF341 deficiency, contrasting with STAT3 deficiency.
- **Two reported cases of tuberculosis**, suggesting a possible (unconfirmed) increased mycobacterial susceptibility signal not typical of classic AD-HIES.

**Quality of life:** No disease-specific QoL instrument data (EQ-5D, SF-36, PROMIS) were located for ZNF341 deficiency specifically; this is a genuine literature gap, not an omission from this report.

---

## 4. Genetic/Molecular Information

**Causal gene:** *ZNF341* (HGNC:15992; NCBI Gene 84905; OMIM *618269), chromosome 20q11.22, 15 exons, encoding a Cys2His2 zinc-finger transcription factor with 12 zinc fingers.

**Reported pathogenic variants** (from Béziat et al. 2023 review, aggregating the full published cohort of 20 patients / 10 kindreds):

| Variant | Patients | Notes |
|---|---|---|
| p.Arg302* | 13 (6 kindreds) | Described as a "mutational hotspot" |
| p.Arg379* | 3 | |
| p.Gln195* | 1 | |
| p.Lys355Serfs*28 | 1 | Frameshift |
| p.Tyr542* | 1 | |
| p.Ser64* | 1 (new case, P20) | |
| c.1943+1G>A / p.Gly611Glyfs*15 | 1 (new case, P19) | Essential splice-site variant |

All reported variants are predicted **loss-of-function** (nonsense/frameshift/splice), consistent with the biallelic LOF mechanism described below. No missense pathogenic variants have been reported to date in the literature I could access.

**Variant classification / population frequency:** I did not obtain gnomAD-specific constraint metrics (pLI, LOEUF, allele frequency) for *ZNF341* in this session — searches for these returned generic gnomAD documentation rather than the gene-specific page. **This is a gap; consult gnomAD directly (gnomad.broadinstitute.org, search ZNF341) before curating population-frequency slots.**

**Functional consequence — mechanism (per Frey-Jakobs 2018 and Béziat 2018, and elaborated in the 2023 review):**
- ZNF341 binds a **bipartite DNA motif**: a ZNF-like site (GGAAC/GA/GGC) and an SP1-like site (GGGAGG), separated by 13–14 nucleotides, located near a STAT3-binding element (SBE) in the *STAT3* promoter.
- ChIP-seq identified **1,457 ZNF341 binding regions** in primary T cells (and many more in transformed cell lines), indicating ZNF341 is a broader transcriptional regulator than a single-target activator of *STAT3* alone.
- Truncating mutations impair transcriptional activation of the *STAT3* promoter, "partly due to nuclear translocation failure" of the truncated protein.
- Functional impact category: **loss of function** (complete, biallelic) — this is a haploinsufficiency-like/dosage mechanism in the affected cell, not a dominant-negative mechanism (contrast with AD-STAT3 HIES, where dominant-negative interference is confirmed in ≥95% of ~150 tested alleles per the review).

**Modifier genes:** None specifically reported.

**Epigenetic information:** ZNF341 itself appears to be **autoregulated** — it contains six canonical ZNF341-binding sites within its own intron 1, and ZNF341-deficient cells show elevated *ZNF341* mRNA, consistent with loss of negative autoregulation (PMC10620851). This is a curator-relevant mechanistic detail (a feedback loop on the causal gene itself, not classical DNA methylation/histone epigenetics — no methylation/ChIP-histone data specific to ZNF341-deficient patients were found).

**Chromosomal abnormalities:** None reported; this is a point-mutation/small-indel disease, not associated with large structural chromosomal rearrangements.

**Additional targets beyond STAT3 (mechanistically relevant, from the 2023 review):**
- **STAT1**: two ZNF341-binding sites ~400 bp upstream of the *STAT1* transcription start site; ZNF341-deficient cells show reduced STAT1, which may explain the (unconfirmed) tuberculosis susceptibility signal.
- **KAT6A**: one of the strongest ChIP-seq binding sites is in the *KAT6A* promoter; *KAT6A* mutations cause Arboleda-Tham syndrome with neurodevelopmental overlap — the functional relationship to ZNF341 deficiency's own neurodevelopmental features (37% mental delay) is stated as unclear in the source and should not be overstated.
- Candidate protein interactions (UBTF, PCM1, PAF1) via affinity purification-mass spectrometry — explicitly described as requiring further validation; do not treat as established.

---

## 5. Environmental Information

No primary causal environmental factor, lifestyle factor, or infectious trigger has been identified for ZNF341 deficiency itself (it is monogenic). The one environmental factor with documented mechanistic relevance is **ionizing radiation exposure post-diagnosis**, which interacts with an underlying DNA-repair defect (see §6/§11) to elevate malignancy risk — this is a disease-consequence/modifier relationship, not a disease-causal environmental exposure, and should be modeled as such if curated (e.g., as an `environmental[]` entry with `environmental_effect: EXACERBATES` targeting a DNA-damage/malignancy-risk pathophysiology node, not `TRIGGERS` the primary immunodeficiency).

No infectious agent causes ZNF341 deficiency; rather, the disease predisposes to infection by *S. aureus* (skin/soft tissue), *Candida* species (mucocutaneous), and, per two case reports, *Mycobacterium tuberculosis* — these are consequences of immunodeficiency, not etiological agents.

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered, with inference flags)

1. **Biallelic loss-of-function variant in *ZNF341*** (nonsense/frameshift/splice; e.g., p.Arg302*) → truncated or absent ZNF341 protein. *(Demonstrated — genetic/functional studies in both founding papers.)*
2. Truncated ZNF341 **fails to translocate normally to the nucleus** and/or **fails to bind its bipartite DNA motif** (ZNF-like + SP1-like sites) in target gene promoters, including the *STAT3* promoter. *(Demonstrated in vitro — reporter assays, EMSA/ChIP in Frey-Jakobs 2018 and Béziat 2018.)*
3. This **reduces basal transcriptional activation of *STAT3*** — ZNF341-deficient cells show approximately **50% of normal basal STAT3 mRNA/protein** across lymphocytes, monocytes, and fibroblasts. *(Demonstrated — patient-cell data.)*
4. Critically, **STAT3 "autoinduction" — the positive-feedback loop by which STAT3, once activated by IL-6/TCR costimulation via PKC-θ→NF-κB/AP-1 signaling, binds its own promoter (with ZNF341 support) to further upregulate its own expression — is abolished** in ZNF341-deficient naive T cells (but preserved, i.e., not the defective step, in STAT3-deficient cells stimulated the same way). *(Demonstrated — the review's key mechanistic distinction from AD-STAT3 disease: "STAT3 autoinduction was abolished in ZNF341-deficient naive T cells stimulated under these conditions, but not in STAT3-deficient naive T cells.")*
5. Combined reduced-basal-expression + abolished-autoinduction → **insufficient STAT3 protein/phosphorylation available downstream of IL-6, IL-21, IL-23 and other STAT3-activating cytokine signals**, particularly under the sustained/repeated stimulation needed for full lymphocyte differentiation programs. *(Demonstrated at the cell-biology level; the review states this combination — not either defect alone — "is considered a more likely pathophysiological mechanism" than the basal reduction alone, since "ZNF341 deficiency had only a modest impact on downstream signaling" from the basal reduction by itself — i.e., the review argues the autoinduction defect is the more mechanistically important lesion, though this is the authors' interpretive judgment rather than a directly measured attribution.)*
6. Insufficient STAT3 activity **impairs Th17 differentiation** (STAT3 is required for RORγt induction downstream of IL-6/IL-23/IL-21) → **low/absent Th17 cells** (reported in 82% of patients) and a compensatory/relative **Th2 skew**. *(Demonstrated — flow cytometry in patient cohorts.)* → contributes to **elevated IgE** (85% of patients) via IL-4/IL-13-driven B-cell class switching, and to **atopic dermatitis** (100%) and susceptibility to *Candida* (Th17 is central to mucosal antifungal immunity) and *S. aureus* skin infection.
7. Reduced STAT3 signaling also **impairs B-cell class-switching/memory formation**, producing **low memory B cells** (77%) — yet, distinctively, **preserved/elevated plasma IgG** (83% with IgG >16 g/L) is seen, an apparent dissociation the source literature does not fully mechanistically resolve (flagged as an open question rather than an established downstream step).
8. **STAT3 signaling deficiency in NK-cell lineage development or maintenance** contributes to **low NK cell counts/frequency** (67%, vs. only 8% in AD-STAT3 disease) — the review notes this NK phenotype is disproportionately more common in ZNF341 deficiency than in STAT3 deficiency, implying either (a) a ZNF341-specific, STAT3-independent NK effect, or (b) a quantitative dose-effect difference; the primary literature does not settle which, so this branch point should be marked as **mechanistically underdetermined**.
9. Separately/in parallel: **ZNF341 also transactivates STAT1** (via promoter sites ~400 bp upstream of the *STAT1* TSS); reduced STAT1 in deficient cells is a plausible (not proven) contributor to the reported tuberculosis susceptibility signal in two patients. *(Inferred — the source explicitly frames this as suggestive, not established: "no clear pattern of viral susceptibility emerged.")*
10. Independently of the STAT3/STAT1 axis: ZNF341-deficient leukocytes show **impaired post-irradiation DNA repair** (elevated Comet-assay tail length/%DNA-in-tail/Olive tail moment that fail to normalize during the 2-hour recovery window, versus rapid normalization in healthy controls), an effect of similar magnitude to that seen in STAT3-LOF cells. *(Demonstrated — PMC9307231, n=4 ZNF341-deficient patients, n=12 STAT3-LOF, n=14 controls.)* → this DNA-repair defect is proposed (not proven) to **contribute to the reported malignancy tendency** in this population (see §11), including one ZNF341-deficient patient who developed a nasal neuroendocrine tumor and a secondary papillary thyroid cancer, and a separate reported case of dual malignancy following chemotherapy (Çekiç/Hartberger et al. 2020, PMID 31980991 — I was unable to retrieve full abstract text on the exact malignancy subtype beyond secondary search snippets referencing diffuse large B-cell lymphoma biology in the surrounding literature; **this attribution needs primary-source verification before it is quoted as fact in a KB entry**).

### Branching/downstream summary
- **Th17 deficiency branch** → mucocutaneous candidiasis, skin/soft-tissue *S. aureus* infection, recurrent sinopulmonary infection, bronchiectasis (35%), pneumatocele (10%).
- **Th2 skew / IgE branch** → atopic dermatitis, elevated IgE, eosinophilia.
- **NK-cell branch** → possible contribution to infection susceptibility (not fully characterized).
- **DNA-repair branch** → malignancy predisposition, radiosensitivity (clinically actionable: minimize radiographic/radiotherapeutic exposure).
- **Connective tissue/skeletal branch** (facial dysmorphia 53%, high palate 45%, joint hyperextensibility 15%, scoliosis 10%, retained primary teeth 25%) — mechanistically **not explained** by the STAT3/Th17 axis in the literature reviewed; these features are shared with AD-STAT3 HIES (where they are also incompletely mechanistically explained, historically attributed to broader STAT3 roles in connective tissue/bone remodeling), so should likely be modeled as a parallel/independent downstream branch of "STAT3 pathway insufficiency" rather than forced onto the immune causal chain.

**Molecular pathway (KEGG/Reactome-style):** JAK-STAT signaling pathway (STAT3 node), with ZNF341 acting as an upstream transcriptional gatekeeper rather than a canonical JAK-STAT pathway member — this is explicitly framed in the literature as "a previously unappreciated layer of transcriptional regulation controlling JAK-STAT signaling."

**Suggested GO terms (unverified leads):** GO:0007259 (JAK-STAT cascade — verify), GO:0045944 (positive regulation of transcription by RNA polymerase II), GO:0043433 (negative/positive regulation of DNA-binding transcription factor activity), GO:0030217 (T-helper 17 differentiation — verify exact ID), GO:0006974 (cellular response to DNA damage stimulus).

**Suggested CL terms (unverified leads):** CL:0000899 (Th17 cell), CL:0000623 (natural killer cell), CL:0000787 (memory B cell), CL:0000084 (T cell).

**Suggested CHEBI/molecular entities:** IL-6, IL-21, IL-23 (as cytokine drivers — CHEBI is not the right ontology for cytokines; these would be gene/protein descriptors, HGNC-bound, not CHEBI).

**Multi-omics/single-cell/spatial data:** No transcriptomic (GEO/ArrayExpress), proteomic, or single-cell atlas datasets specific to ZNF341-deficient patient material were located in this session. This is a genuine literature gap for a `datasets:` block — the mechanistic work to date is ChIP-seq (in cell lines/primary T cells for ZNF341 binding-site mapping) and flow cytometry, not bulk/single-cell RNA-seq of patient cells as far as I could determine.

---

## 7. Anatomical Structures Affected

**Organ level (primary):**
- Skin (atopic dermatitis, abscesses) — primary and near-universal.
- Respiratory tract (recurrent URI, pneumonia, bronchiectasis, pneumatocele).
- Oral cavity/dentition (high palate, retained primary teeth).
- Musculoskeletal system (scoliosis, joint hyperextensibility, facial dysmorphia).
- Immune system broadly (thymus/lymphoid tissue — T-cell, B-cell, NK-cell compartments).

**Secondary/complication-level:** Thyroid (secondary papillary thyroid cancer in one reported case), nasal cavity (neuroendocrine tumor in the same case) — these are malignancy complications, not primary disease-organ involvement.

**Body systems:** Immune system (primary); integumentary; respiratory; skeletal/connective tissue; less consistently, endocrine (secondary, via reported malignancy only).

**Tissue/cell level:** Epithelial (skin, respiratory mucosa — site of infection); lymphoid (T cells — especially Th17 and Tfh subsets, memory CD4+/CD8+ T cells; B cells — memory B-cell compartment; NK cells; mucosal-associated invariant T cells; ILC1/ILC2 populations, per PMC10620851).

**Suggested UBERON/CL terms (unverified leads):** UBERON:0002097 (skin), UBERON:0001004 (respiratory system), UBERON:0002370 (thymus), CL:0000899 (Th17 cell), CL:0000623 (NK cell), CL:0000787 (memory B cell), CL:0000940 (mucosal invariant T cell).

**Subcellular:** Nucleus (site of ZNF341's transcriptional action; nuclear translocation failure of truncated protein is a described mechanism) — GO Cellular Component: GO:0005634 (nucleus).

**Laterality:** Not applicable/not reported as a distinguishing feature (skeletal features such as scoliosis are not described as lateralized in a disease-specific way).

---

## 8. Temporal Development

**Onset:** Childhood onset, with atopic dermatitis typically presenting earliest (consistent with the 100% frequency and the "newborn rash" feature reported in 15% of patients, suggesting a subset present in the neonatal period). This mirrors, but is generally reported as somewhat later/milder in onset timing than, classic AD-STAT3 HIES.

**Progression:** Chronic, with cumulative infectious and structural (bronchiectasis, pneumatocele) respiratory damage over time — consistent with other primary immunodeficiencies with recurrent sinopulmonary infection. The disease is **lifelong** (not self-limited); no spontaneous-remission pattern is reported.

**Disease course pattern:** Relapsing/recurrent infections superimposed on a chronic dermatologic/atopic baseline, rather than strictly progressive organ failure — though bronchiectasis, once established, is itself a progressive structural lesion.

**Critical periods:** Early childhood appears to be the critical window for both diagnosis (recurrent infection pattern becoming apparent) and for initiating interventions (e.g., antimicrobial prophylaxis, consideration of dupilumab for dermatitis) to limit cumulative organ damage — this is inferred from the general HIES management paradigm rather than ZNF341-deficiency-specific natural-history data, which does not yet exist at sufficient cohort size.

**Disease stages:** No formal staging system exists for ZNF341 deficiency specifically; the **NIH HIES clinical scoring system** (used for AD-STAT3 HIES) has been applied post hoc to grade ZNF341-deficient patients (median 28.5) for comparative severity purposes, not as a disease-specific staging tool.

---

## 9. Inheritance and Population

**Epidemiology:** Ultra-rare. **Only 20 patients from 10 kindreds** have been reported in the peer-reviewed literature as of the most recent comprehensive review (Béziat et al. 2023). No formal prevalence or incidence estimate (per 100,000) exists — this would fall in the Orphanet "not yet documented" prevalence class if curated, and should **not** be assigned a numeric `rate_per_100000` without a source explicitly providing one (none was found).

**Inheritance pattern:** Autosomal recessive (biallelic — homozygous or compound heterozygous LOF variants required for disease).

**Penetrance:** Appears complete at the molecular/immunologic level (all reported biallelic LOF carriers are symptomatic), though clinical **expressivity is variable** — feature frequencies range from 100% (dermatitis) to 10% (pneumatocele, scoliosis), indicating substantial variable expressivity even among truly biallelic patients. No data on heterozygous carrier phenotype (asymptomatic carriers expected under standard AR inheritance, but not explicitly documented in a carrier-focused study).

**Genetic anticipation:** Not applicable/not reported — this is a nonsense/frameshift/splice-variant disease, not a repeat-expansion disorder.

**Germline mosaicism:** Not reported.

**Founder effects:** The p.Arg302* variant recurring across 6 independent kindreds (13/20 patients) is consistent with either a founder effect or a true mutational hotspot at a CpG-prone nonsense codon; **the source literature does not distinguish between these**, and this distinction matters for population-genetics/counseling purposes — flag as unresolved rather than asserting "founder mutation."

**Consanguinity:** A major contributor to case ascertainment — reported kindreds are predominantly from populations/regions with high rates of consanguineous marriage (Moroccan, Afro-Caribbean, Iranian, Turkish, Lebanese, and Israeli Arab backgrounds).

**Carrier frequency:** Not established in any population database search performed in this session (gnomAD-specific allele-frequency data for *ZNF341* was not successfully retrieved — see §4 gap).

**Population demographics:** Given the ascertainment pattern above, reported cases cluster in populations with elevated consanguinity rates, but this reflects **ascertainment bias in a rare recessive condition**, not necessarily true differential prevalence by ancestry — this distinction should be made explicit in any curated `population` field rather than asserting an "affected population."

**Sex ratio:** Not reported as skewed in any source reviewed (consistent with autosomal, non-sex-linked inheritance; no data located specifically quantifying M:F ratio across the 20 cases).

---

## 10. Diagnostics

**Suggestive clinical picture:** Childhood atopic dermatitis + recurrent bacterial/fungal infections + elevated IgE (>1000 IU/mL, 85% of patients) + eosinophilia (58%) — essentially the same initial clinical suspicion pattern as classic Job syndrome, refined by immunophenotyping.

**Laboratory tests:**
- Serum total IgE (elevated in 85%) and IgG (elevated >16 g/L in 83% — notably *higher* than typical STAT3-deficient patients, a discriminating lab feature).
- Eosinophil count (elevated in 58%).
- Lymphocyte immunophenotyping: low/absent Th17 cells (82%), low memory B cells (77%), low NK cell frequency/count (67% — a key discriminator from AD-STAT3 disease, where this is seen in only 8%).
- STAT3 phosphorylation assay (pSTAT3 by flow cytometry after IL-6/IL-21/IL-23 stimulation) — functionally demonstrates the reduced basal STAT3 and abolished autoinduction described in §6; this is the closest thing to a functional diagnostic assay reported in the primary literature, though it is a research-lab assay rather than a standardized clinical test.

**Genetic testing:** The definitive diagnostic step is **sequencing of *ZNF341*** — either as part of a primary immunodeficiency/HIES-focused gene panel (alongside *STAT3*, *IL6ST*, *DOCK8*, *PGM3*, etc.), whole-exome sequencing, or single-gene Sanger sequencing/confirmation once biallelic candidate variants are found in a consanguineous family. Given the AR inheritance and consanguinity pattern, **homozygosity mapping / autozygosity analysis** was explicitly the ascertainment method in the founding papers (both were consanguineous-family linkage/exome studies).

**Differential diagnosis:** Primarily AD-STAT3 HIES (Job syndrome) — clinically near-identical but distinguished by: (1) inheritance pattern (AR family history/consanguinity vs. AD/de novo), (2) generally milder NIH HIES score, (3) more frequent NK-cell deficiency, (4) absence of reported vascular complications, (5) relatively preserved/elevated IgG despite low memory B cells. Also consider *IL6ST* (gp130) deficiency (another HIES phenocopy gene), DOCK8 deficiency (AR combined immunodeficiency with high IgE but distinct viral-susceptibility profile), and PGM3-CDG.

**Screening:** No specific newborn-screening or population carrier-screening program exists for *ZNF341* given its rarity; not part of standard TREC/KREC-based SCID screening (this is not a T-cell-lymphopenic SCID phenotype).

**Suggested NCIT/LOINC terms:** general immunoglobulin quantification (IgE, IgG — LOINC codes exist generically, not disease-specific) and flow-cytometry lymphocyte subset panels; no ZNF341-specific commercial assay identified.

---

## 11. Outcome/Prognosis

**Survival/mortality:** No formal survival statistics (5-year, 10-year) exist for this ultra-rare condition; the literature is case-series-based, not registry/actuarial.

**Morbidity:** Chronic respiratory morbidity from recurrent infection (bronchiectasis in 35%, pneumatocele in 10%) is the principal long-term structural complication; chronic dermatitis is near-universal morbidity.

**Malignancy risk — a specific, clinically important prognostic finding:**
- A documented case of **dual malignancy** in a ZNF341-deficient patient (Çekiç/Hartberger et al., *J Clin Immunol* 2020, PMID 31980991 — "Cancer Tendency in a Patient with ZNF341 Deficiency"). I was unable to fully verify the exact histologic malignancy type(s) from primary-source text in this session (access blocked); secondary sources associate the case discussion with tumorigenesis mechanisms in diffuse large B-cell lymphoma, but **this specific attribution should be independently verified against the primary abstract/full text before being cited as fact in a KB entry** — flagging this explicitly per the attribution standard (do not substitute a weaker adjacent citation).
- A separate case within the 2022 radiosensitivity study cohort (PMC9307231) describes a ZNF341-deficient patient who developed a **nasal neuroendocrine tumor and a secondary papillary thyroid cancer**.
- Mechanistic support: ZNF341-deficient leukocytes show **impaired DNA repair after ionizing-radiation exposure** (Comet-assay measures — tail length, %DNA in tail, Olive tail moment — remain elevated at 2 hours post-2Gy-irradiation rather than returning toward baseline as in healthy controls; effect sizes >1.30 across measures), of similar magnitude to STAT3-LOF patients (Alsina/Grimbacher-affiliated group, *Clin Exp Immunol* 2022, PMC9307231).
- **Clinical implication explicitly drawn by the source:** clinicians should **minimize ionizing-radiation exposure** (diagnostic imaging, radiotherapy) in these patients where possible and maintain **close malignancy surveillance**.

**Quality of life:** No disease-specific instrument data located (see §3).

**Prognostic factors:** No formal prognostic-biomarker model exists; qualitatively, the NIH HIES severity score and specific complication burden (bronchiectasis, pneumatocele, malignancy history) are the closest available prognostic indicators, by extrapolation from the AD-STAT3 HIES literature rather than ZNF341-deficiency-specific validation.

---

## 12. Treatment

**No disease-specific treatment guideline or FDA-approved therapy exists for ZNF341 deficiency.** Management follows the general primary-immunodeficiency/HIES paradigm, with two published exceptions of ZNF341-deficiency-specific case reports of targeted biologic use:

**Pharmacotherapy (general HIES management, inferred/extrapolated, not ZNF341-specific trial data):**
- Antimicrobial prophylaxis (anti-staphylococcal, antifungal) for recurrent infection — standard HIES practice; not explicitly detailed as ZNF341-specific in the sources reviewed.
- Immunoglobulin replacement therapy (IVIG/SCIG) — referenced only implicitly via general HIES management context in the review; not explicitly documented as used/evaluated in the ZNF341 cohort specifically in the text I could access.

**Targeted biologic therapy (ZNF341-specific case evidence):**
- **Dupilumab** (anti-IL-4Rα monoclonal antibody, blocking IL-4/IL-13 signaling): a patient with severe atopic dermatitis in the setting of ZNF341 deficiency showed "spectacular improvement of symptoms and biological parameters" (Lévy, Béziat, Barbieux et al., *J Clin Immunol* 2020 — "Efficacy of Dupilumab for Controlling Severe Atopic Dermatitis in a Patient with Hyper-IgE Syndrome"). Suggested NCIT term: dupilumab has an NCIT concept code (not independently verified in this session — look up via `runoak` before binding).
- A more recent case series (Dick et al., *Pediatric Dermatology* 2025) reports dupilumab use in children with distinct genetic HIES types including a ZNF341 case, again for atopic dermatitis control and infection reduction — described in secondary search results as "the first to report... a child with AR-HIES... caused by a mutation in ZNF341 to be treated with dupilumab" (this framing should be checked against the primary text, since the 2020 Lévy case may predate it or involve an adult rather than child — potential inconsistency to resolve before citing).

**Surgical/interventional:** Not specifically documented (would follow standard management of bronchiectasis/abscess complications if they arise, per general practice, not ZNF341-specific literature).

**Experimental/advanced therapeutics:** No gene therapy, HSCT, or JAK-inhibitor use was documented in the ZNF341-deficiency literature located in this session. Given that this is a **transcription-factor** (not cytokine-receptor or kinase) defect acting upstream of JAK-STAT signaling via reduced STAT3 dosage/autoinduction rather than an activating/dominant-negative kinase-pathway lesion, the rationale for a JAK inhibitor is less direct than in some other STAT-pathway diseases (e.g., activated PI3K/STAT gain-of-function disorders) — no trial or case evidence either supports or refutes JAK-inhibitor use here; this is a genuine gap, not an oversight.

**Radiation-exposure minimization:** As above (§11), an explicit management recommendation from the DNA-repair/radiosensitivity study — this functions as a preventive/monitoring recommendation more than a "treatment."

---

## 13. Prevention

**Primary prevention:** Not applicable in the population-health sense (monogenic AR disease; no modifiable primary-prevention exposure identified). At the family level, **genetic counseling** for consanguineous couples/carrier parents in populations with known *ZNF341* pathogenic alleles (and prenatal/preimplantation genetic testing where a familial variant is known) is the relevant "primary prevention" analog, by extrapolation from standard AR-disease counseling practice — not explicitly documented as implemented for ZNF341 deficiency specifically in the literature reviewed.

**Secondary prevention:** Early recognition of the clinical pattern (childhood dermatitis + recurrent infection + high IgE) prompting genetic testing, enabling earlier initiation of antimicrobial prophylaxis and directed therapy (e.g., dupilumab for dermatitis).

**Tertiary prevention:** Malignancy surveillance and **minimization of ionizing radiation exposure** given the documented DNA-repair defect — this is the most concrete, literature-supported tertiary-prevention recommendation specific to this disease.

**Screening:** No population or newborn screening program exists (see §10).

**Prophylaxis:** Standard antimicrobial (antibacterial/antifungal) prophylaxis by extrapolation from general HIES/PID management; not documented as a formally studied ZNF341-specific regimen.

---

## 14. Other Species / Natural Disease

**No naturally occurring ZNF341-deficient disease in a non-human species was located in this session.** No veterinary case reports, no OMIA (Online Mendelian Inheritance in Animals) entry, and no companion-animal or wildlife natural-disease reports surfaced in searches. This should be treated as an absence-of-evidence finding rather than a confirmed absence — I did not exhaustively query OMIA directly.

**Orthologous gene:** *Znf341* exists in mouse (murine ortholog), referenced in passing in the mechanistic literature discussing the STAT3-promoter-binding assays, but I did not locate NCBI Gene ID data for the mouse ortholog or confirm cross-species conservation details in this session.

---

## 15. Model Organisms

**No engineered animal model (knockout, knock-in, conditional, or humanized mouse) of ZNF341 deficiency was located in the literature searched in this session.** Searches for a "Znf341 knockout mouse" returned only the human patient-based mechanistic papers, not a dedicated murine model study. This is a **notable gap** relative to many other monogenic PID genes and should be recorded as such (i.e., `animal_models:` may legitimately be left empty for this entry, with a note that a search was performed and returned no in vivo model, rather than fabricating one).

**In vitro/cellular models used in the primary mechanistic literature (not "animal models" but relevant to a `computational_models`/`experimental_models` curation decision):**
- Patient-derived primary T cells, EBV-transformed B-cell lines, and monocytes/fibroblasts (Frey-Jakobs 2018, Béziat 2018) — used for STAT3 mRNA/protein quantification, pSTAT3 flow cytometry, and Th17/Tfh/NK/memory-B immunophenotyping.
- Reporter-gene assays (luciferase, STAT3-promoter constructs) and EMSA/ChIP-seq in transfected/transformed cell lines — used to define the bipartite ZNF341 binding motif and map genome-wide binding sites (1,457 regions in primary T cells).
- Peripheral blood leukocytes ex vivo, alkaline Comet assay — used in the 2022 radiosensitivity study (PMC9307231) to demonstrate impaired post-irradiation DNA repair; this is a functional ex vivo assay on patient material, not an animal or engineered cellular model, and should probably be captured as an `Experiment`/`experimental_models` entry with `modeled_mechanisms` targeting the DNA-repair/malignancy-risk pathophysiology node if this entry is curated into dismech, with `fidelity: HIGH` (it is direct patient-cell measurement) rather than treated as a model-organism proxy.

---

## Summary Table of Key Primary Citations

| Citation | Role |
|---|---|
| Frey-Jakobs S et al., *Sci Immunol* 2018 (PMID 29907690) | Co-founding discovery paper: "ZNF341 controls STAT3 expression and thereby immunocompetence" |
| Béziat V et al., *Sci Immunol* 2018 (PMID 29907691) | Co-founding discovery paper: "A recessive form of hyper-IgE syndrome by disruption of ZNF341-dependent STAT3 transcription and activity" |
| Al-Herz W, *Sci Immunol* 2018 (PMID 29907692) | Commentary: "Who regulates whom: ZNF341 is an additional player in the STAT3/TH17 song" |
| Béziat V et al., *Curr Opin Immunol* 2023 (PMID 37080116; PMC10620851) | Comprehensive review + 2 new cases (total n=20); source of phenotype-frequency table and mechanistic synthesis above |
| Çekiç Ş / Hartberger J et al., *J Clin Immunol* 2020 (PMID 31980991) | Case report: malignancy in a ZNF341-deficient patient — **verify exact malignancy type from primary text before curating** |
| (Alsina/Grimbacher group), *Clin Exp Immunol* 2022 (PMC9307231) | Radiosensitivity/DNA-repair functional study, n=4 ZNF341-deficient patients |
| Lévy R, Béziat V, Barbieux C et al., *J Clin Immunol* 2020 | Case report: dupilumab efficacy for atopic dermatitis in HIES (ZNF341 deficiency context) |
| Dick et al., *Pediatric Dermatology* 2025 | Case series: dupilumab in children with genetically distinct HIES, including ZNF341 |

---

## Explicit Gaps and Items Requiring Verification Before Curation

1. **gnomAD allele-frequency/constraint data for *ZNF341*** were not successfully retrieved — needed for any `case_fractions`/population-frequency work.
2. **Exact malignancy histology** in the Çekiç/Hartberger 2020 case report was not confirmed from primary text (WebFetch was blocked by PubMed/cookie walls); do not cite a specific cancer subtype for that case without independent verification.
3. **MONDO:0032654** as supplied in the task header was not independently cross-checked against a MONDO browser in this session.
4. **All suggested HPO/GO/CL/UBERON CURIEs above are unverified leads**, offered per the report template's request but explicitly not checked against an ontology adapter — per this repository's Ontology Term Contract, they must be looked up (not written from memory) before being bound in any KB entry.
5. **No animal model** of ZNF341 deficiency was located — confirmed as a literature gap, not merely an unsearched area, though the search was not exhaustive of OMIA/IMPC databases directly.
6. **No formal prevalence/incidence estimate** exists; only "20 patients reported" (a `CASES_IN_LITERATURE` measure_type, not a population rate) should be used if curating a `Prevalence` record.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.
