---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-20T13:02:31.708208'
end_time: '2026-07-20T13:07:49.563547'
duration_seconds: 317.86
template_file: templates\disease_pathophysiology_research.md
template_variables:
  disease_name: MERTK-Related Retinopathy
  mondo_id: MONDO:0800394
  category: Mendelian
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: C:/Users/flaharty/AppData/Roaming/npm/node_modules/@anthropic-ai/claude-code/bin/claude.exe
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    working_dir: C:/Users/flaharty/AppData/Local/Temp/claude/C--Users-flaharty-Desktop-VSCode/634cea2b-38e9-4ffb-8048-fd46243e54f3/scratchpad
    timeout: 1800
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 26
  num_turns: 33
  total_cost_usd: 1.4987291
  session_id: 822042ec-53d1-4a9c-931f-084c5ef97877
  stop_reason: end_turn
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MERTK-Related Retinopathy
- **MONDO ID:** MONDO:0800394 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MERTK-Related Retinopathy** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# MERTK-Related Retinopathy: Comprehensive Disease Characteristics Report

## 1. Disease Information

**Overview:** MERTK-related retinopathy is a rare, autosomal recessive inherited retinal degeneration caused by biallelic loss-of-function variants in *MERTK* (MER proto-oncogene, tyrosine kinase). It presents classically as an early/childhood-onset, severe rod–cone dystrophy with disproportionately early macular involvement, distinguishing it from typical adult-onset retinitis pigmentosa (RP). The molecular basis was the first conclusive evidence implicating a defect in retinal pigment epithelium (RPE) phagocytosis — rather than a photoreceptor-intrinsic defect — as a cause of human retinal degeneration (Gal et al., *Nat Genet* 2000, PMID 11062461).

**Key identifiers:**
- **MONDO:** MONDO:0800394 (MERTK-related retinopathy)
- **OMIM Phenotype:** #613862 — Retinitis Pigmentosa 38 (RP38)
- **OMIM Gene:** *604705 — MER Tyrosine Kinase Protooncogene (MERTK)
- **Gene locus:** 2q13 (also reported as 2q14.1 in older literature)
- **HGNC:** HGNC:7027
- **ICD-10-CM:** H35.52 (Pigmentary retinal dystrophy / retinitis pigmentosa) — no MERTK-specific ICD code exists; classified under the general RP code
- **MeSH:** Retinitis Pigmentosa (D012174)
- **Orphanet:** No dedicated ORPHA number specific to "MERTK-related retinopathy" was identified in this search; it is grouped under broader entries such as "Severe early-childhood-onset retinal dystrophy" (ORPHA:364055) and "Retinitis pigmentosa" (autosomal recessive) entries. This should be verified directly against the current Orphanet database.
- **ClinGen Gene-Disease Validity:** **Definitive** classification (approved 2022-07-07) for MERTK–MERTK-related retinopathy, autosomal recessive inheritance, based on 12/12 maximum genetic evidence points (6 probands, 8 unique variants, segregation LOD 4.63 across 3 families) plus experimental/model organism evidence.

**Synonyms/alternative names:** Retinitis pigmentosa 38 (RP38); MERTK-associated retinitis pigmentosa; MERTK-related retinitis pigmentosa; childhood-onset rod-cone dystrophy due to MERTK mutation; autosomal recessive retinitis pigmentosa due to MERTK deficiency.

**Data source type:** This report is derived from aggregated disease-level resources — peer-reviewed case series, natural history cohort studies, gene-disease curation panels (ClinGen), and animal/cellular model literature — not from individual patient EHR data.

---

## 2. Etiology

**Disease causal factor:** Purely genetic/monogenic. Biallelic (homozygous or compound heterozygous) pathogenic variants in *MERTK* are necessary and sufficient to cause disease; no environmental or infectious trigger is implicated in the primary etiology.

**Genetic risk factors:**
- Biallelic loss-of-function or hypomorphic missense variants in *MERTK* (2q13/2q14.1) — causal.
- Consanguinity strongly increases risk given autosomal recessive inheritance; many reported pedigrees are consanguineous Middle Eastern or North African families (Mackay et al., *Mol Vis* 2010, PMID 20300561).
- Population founder alleles (see Section 9) act as regional genetic risk factors (e.g., Faroe Islands 91-kb deletion).
- No established modifier genes with strong evidence, though genotype (missense vs. null) appears to influence severity (see below).

**Environmental/lifestyle risk factors:** None established as causal. As with other RP subtypes, light exposure and oxidative stress are hypothesized generic contributors to photoreceptor stress in degenerating retinas, but no MERTK-specific environmental risk factor has been demonstrated in the literature reviewed.

**Protective factors:** No genetic or environmental protective factors specific to MERTK-related retinopathy were identified. Vitamin A palmitate supplementation, used generically in RP management, has shown inconsistent/mixed benefit in RP broadly and is not specifically validated for MERTK-related disease.

**Gene-environment interactions:** None specifically documented for MERTK-related retinopathy in the literature reviewed; this is a monogenic disease with recessive inheritance where phenotype is driven primarily by allelic severity rather than environmental modification.

---

## 3. Phenotypes

**Phenotype type:** Primarily clinical signs and symptoms (ophthalmologic); no behavioral phenotype; some laboratory/imaging biomarkers.

### Core phenotype: Nyctalopia (night blindness)
- **Type:** Symptom
- **Onset:** Earliest and most common presenting symptom; mean age of onset ~9.4 years (±3.4; range 4–15) in one cohort (Retina 2026 cohort); other series report symptom onset as early as age 3 and as late as 12–16 years.
- **Severity/progression:** Progressive.
- **Frequency:** Most common initial symptom across nearly all reported cohorts.
- **HPO term suggestion:** Nyctalopia (HP:0000662)

### Rod-cone dystrophy (progressive peripheral field loss)
- **Type:** Clinical sign (fundoscopic/functional)
- **Onset:** Childhood.
- **Progression:** Progressive, relentless; full-field ERG becomes "barely recordable" in advanced disease (Ophthalmic Genetics 2021, PMID 34289798).
- **HPO terms:** Rod-cone dystrophy (HP:0000510); Retinal rod-cone dystrophy; Constricted visual fields (HP:0001133); Abnormal electroretinogram (HP:0000512)

### Early/disproportionate macular atrophy
- **Type:** Clinical sign
- **Onset:** Distinctive feature — occurs earlier than typical RP, often within the first two decades. Central macular atrophy related to asymmetric visual acuity was common after age 10 (11/17 patients in one series).
- **Severity/progression:** Progressive; a key distinguishing biomarker of this gene-specific phenotype versus other RP genes.
- **HPO terms:** Macular atrophy (HP:0007401); Bull's eye maculopathy (HP:0007843, seen in some cases)

### Central visual acuity loss
- **Onset:** Significant visual acuity loss "usually occurs by the teenage years" (Retina 2026, PMID/DOI 10.1097/IAE.0000000000004713).
- **Frequency/severity:** Visual acuity 20/70 or worse in at least one eye after age 17 in nearly all patients (16/17 in one cohort); all patients legally blind by age 39 in another series.
- **Progression rate (quantified):** Mean BCVA declined from 0.84 ± 0.86 to 1.14 ± 0.86 logMAR at final follow-up (~0.05 ± 0.03 logMAR/year); ellipsoid zone width declined ~141 µm/year; central macular thickness declined ~11.2 µm/year (PMID 34289798).
- **HPO terms:** Reduced visual acuity (HP:0007663); Progressive visual loss (HP:0000529)

### Structural/imaging findings
- Subretinal debris/hyper-reflective deposits beneath the sensory retina on OCT (a relatively distinctive feature of MERTK retinopathy, thought to reflect unphagocytosed outer segment debris).
- Ultra-widefield fundus autofluorescence: central macular hyperautofluorescence.
- Optic disc drusen and myopia reported as common associated findings in the 2026 Retina cohort.
- HPO terms: Abnormality of the outer nuclear layer; Myopia (HP:0000545); Optic disc drusen (HP:0011766)

**Additional reported signs:** Bone-spicule pigmentation (variable/less prominent than typical RP in some case series), attenuated retinal vessels, waxy disc pallor — classic RP fundus triad, present variably.

**Quality of life impact:** Not separately quantified with validated instruments (EQ-5D/SF-36) in MERTK-specific literature reviewed; broader RP literature documents substantial QOL burden from progressive vision loss affecting independence, employment, and mobility, with impact escalating as patients become legally blind by young/mid-adulthood. No MERTK-specific QOL studies were identified — **data gap**.

**Systemic/extra-ocular phenotype:** MERTK-related retinopathy is considered **nonsyndromic** — disease is confined to the retina/RPE in reported human cohorts, despite MERTK's broader immunologic roles (see Section 6). No consistent systemic autoimmune phenotype has been reported in affected patients, though this remains a theoretical area of interest given MERTK's role in efferocytosis.

---

## 4. Genetic/Molecular Information

**Causal gene:** *MERTK* (HGNC:7027; OMIM *604705), chromosome 2q13. Encodes a receptor tyrosine kinase of the TAM (TYRO3/AXL/MERTK) family.

**Variant classification and types:** Pathogenic variants span essentially all mutation classes:
- **Missense:** e.g., c.1133C>T (p.Thr378Met), c.2163T>A (p.His721Gln), c.1866G>C (p.Lys622Asn), c.2020A>G (p.Met674Val) — PMC9615558; ClinGen curation.
- **Nonsense:** c.1843A>T (p.Lys615*); c.2262C>G (p.Tyr754*) — ClinGen curation.
- **Frameshift:** c.1744_1751delinsT (p.Ile582Ter, functionally a truncation); Ser331Cysfs*5 (used to generate the iPSC disease model, PMID 26263531); c.2214del (p.Cys738Trpfs*32).
- **Splice-site:** c.61+1G>A (intron 1 donor site, Mackay et al. PMID 20300561); additional splice mutations reported in consanguineous families with paternal isodisomy for chromosome 2.
- **Large structural deletions:** ~9 kb deletion removing exon 8 (PMID 20300561); 91-kb deletion spanning exons 1–7, a Faroese founder allele arising from non-homologous recombination between Alu and LINE-1 repeats (Molecular Vision, mol vis v24/667); 5-bp deletion reported in a consanguineous family.

**Functional consequence:** Predominantly **loss of function** — null alleles (nonsense, frameshift, large deletion, canonical splice-site) abolish MERTK protein/kinase activity; missense variants affect highly conserved residues in functional domains (extracellular Ig-like/fibronectin III domains or the intracellular tyrosine kinase domain) and are predicted pathogenic by low population frequency and computational tools, generally producing hypomorphic or complete loss of kinase signaling. No gain-of-function or dominant-negative mechanism has been described; disease is strictly autosomal recessive, consistent with a loss-of-function/haploinsufficiency-tolerant mechanism (heterozygous carriers are unaffected).

**Allele frequency / population genetics:** No pathogenic MERTK variant is common in general population databases (gnomAD), consistent with rarity of the disease; MERTK accounts for roughly 1% of autosomal recessive RP cases generally, but with striking founder effects in specific populations (see Section 9). Specific gnomAD allele frequencies for individual pathogenic alleles were not retrievable in this search session — **recommend direct gnomAD browser query for exact figures**.

**Somatic vs. germline:** All disease-causing variants are germline. (Note: *MERTK* has separate, unrelated somatic relevance as an oncogenic driver in leukemia, melanoma, gastric cancer, and Ewing sarcoma — this is a distinct area of cancer biology, not part of the retinal phenotype.)

**Modifier genes:** No formally validated modifier genes for MERTK-related retinopathy were identified. Genotype-phenotype correlation (null vs. hypomorphic missense alleles) is suggested as an informal severity modifier across case series, but this has not been systematically established.

**Epigenetic information:** No MERTK-retinopathy-specific epigenetic (DNA methylation/histone) studies were identified in this search — **data gap**.

**Chromosomal abnormalities:** No aneuploidy/translocation etiologies reported; disease arises from intragenic variants and structural deletions at the *MERTK* locus itself, not from large chromosomal rearrangements.

**Gene/protein structure:** MERTK protein has two Ig-like C2-type domains, two fibronectin type-III domains (ligand-binding extracellular region), a transmembrane domain, and an intracellular tyrosine kinase domain — GeneCards/UniProt.

---

## 5. Environmental Information

No established environmental toxin, occupational, or infectious contributors to MERTK-related retinopathy were identified — this is a purely monogenic disease. Lifestyle factors relevant to general RP care (UV/blue-light protection, smoking avoidance for general retinal health) are extrapolated from broader RP guidance rather than MERTK-specific evidence. No infectious agents are implicated.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**
1. Biallelic loss-of-function *MERTK* variants → absent/nonfunctional MERTK receptor tyrosine kinase on the apical RPE surface.
2. Failure of MERTK-dependent signaling in response to its ligands **Gas6** and **Protein S**, which normally bind externalized phosphatidylserine on shed photoreceptor outer segment (POS) tips and bridge them to RPE MERTK.
3. Loss of POS **ensheathment, fragmentation, and internalization** by RPE — MERTK ligands trigger POS ensheathment, and "ensheathment, fragmentation, and internalization [are] abolished in MERTK mutant RPE" (PMC7066375).
4. Progressive accumulation of unphagocytosed/undigested photoreceptor outer segment debris in the subretinal space — visualized clinically as subretinal hyper-reflective debris on OCT and hyperautofluorescence on FAF.
5. Chronic subretinal debris accumulation triggers **RPE inflammation** — a 2022 study (bioRxiv/PMID pending) reported "Inflammation of the retinal pigment epithelium drives early-onset photoreceptor degeneration in Mertk-associated retinitis pigmentosa," implicating a secondary inflammatory mechanism beyond simple debris toxicity.
6. Secondary photoreceptor (rod, then cone) death by apoptosis, driven by loss of trophic RPE support, toxic debris accumulation, and local inflammation.
7. Clinical endpoint: progressive rod-cone dystrophy, early macular atrophy, and legal blindness by the third–fourth decade.

**Molecular pathway:** RPE apical phagocytic receptor signaling — two convergent/complementary pathways: (a) αvβ5 integrin, stimulated by MFG-E8, signaling to the actin regulator Rac1 (controls timing of phagocytosis, circadian burst); (b) MERTK, activated by Gas6/Protein S, signaling via focal adhesion kinase (FAK) to drive actual particle **internalization**. MERTK deficiency selectively abolishes the internalization step while initial binding/recognition may remain partially intact (integrin-mediated).

**Cellular processes involved:** Phagocytosis/efferocytosis (specifically "clearance phagocytosis"), cytoskeletal (actin) remodeling, receptor tyrosine kinase signal transduction, secondary apoptosis of photoreceptors, and RPE-driven inflammatory signaling.

**Protein dysfunction:** Loss of MERTK kinase activity (null alleles) or impaired ligand engagement/kinase signaling (missense alleles) — a loss-of-function mechanism at the RPE cell membrane.

**Immune system involvement:** MERTK is a core "eat-me" signal receptor for apoptotic cell clearance (efferocytosis) broadly, not only in RPE but in macrophages/microglia throughout the body. *Mertk*-knockout mice show defective macrophage clearance of apoptotic thymocytes/lymphocytes and develop **autoimmune features** (increased autoantibodies, lupus-like phenotype) due to impaired self-antigen clearance — TAM-receptor-deficient mice are established autoimmunity models. Microglial MERTK deficiency also impairs efferocytosis in the CNS/retina and modulates neuroinflammation. However, systemic autoimmune disease is **not** a prominent reported feature of human MERTK-related retinopathy patients in the ophthalmic literature reviewed — this immune dimension is primarily documented in model systems and represents a biologically plausible but clinically under-characterized aspect of the human disease.

**Tissue damage mechanism:** Combination of (1) toxic/metabolic stress from undigested POS debris, (2) chronic local RPE inflammation, and (3) loss of RPE trophic/metabolic support for photoreceptors, converging on photoreceptor apoptosis.

**Molecular/omics profiling:** No MERTK-retinopathy-specific transcriptomic, proteomic, metabolomic, or lipidomic human datasets were identified in this search. A related mouse model study ("MerTK-cleavage-resistant mouse") reported "retinal atrophy, inflammation, phagocytic and metabolic disruptions" using multimodal approaches, suggesting metabolic dysregulation accompanies phagocytic failure at the mechanistic level in animal models — human confirmatory omics data represent a **data gap**.

**Suggested GO terms:** Phagocytosis (GO:0006909); phagocytosis, engulfment (GO:0006911); regulation of phagocytosis (GO:0050764); receptor tyrosine kinase signaling pathway (GO:0007169); apoptotic cell clearance (GO:0043277); photoreceptor cell maintenance (GO:0045494); visual perception (GO:0007601)

**Suggested CL (Cell Ontology) terms:** Retinal pigment epithelial cell (CL:0002586); rod photoreceptor cell (CL:0000604); cone photoreceptor cell (CL:0000573); microglial cell (CL:0000129); macrophage (CL:0000235)

---

## 7. Anatomical Structures Affected

**Organ level:** Eye — specifically the retina and retinal pigment epithelium. Disease is nonsyndromic/ocular-limited in humans; no established secondary organ involvement.

**Body system:** Visual/sensory system (nervous system component — retina is CNS-derived tissue).

**Tissue/cell level:**
- Primary target: **Retinal pigment epithelium (RPE)** — site of the primary phagocytic defect (CL:0002586).
- Secondarily affected: **Rod photoreceptors** (CL:0000604) — die first/predominantly, consistent with rod-cone dystrophy pattern; **cone photoreceptors** (CL:0000573), particularly in the macula, affected early and disproportionately relative to typical RP.
- Outer nuclear layer (photoreceptor cell bodies) shows thinning on OCT.
- Photoreceptor outer segments — site of debris accumulation (ensheathment failure).

**Subcellular level (GO Cellular Component):** Plasma membrane / apical microvilli of RPE (site of MERTK receptor and phagocytic cup formation, GO:0005886, GO:0031514); phagosome (GO:0045335); relevant to receptor tyrosine kinase trafficking.

**Localization (UBERON terms):** Retina (UBERON:0000966); retinal pigment epithelium (UBERON:0002566); macula lutea (UBERON:0002187); neural retina.

**Lateralization:** Bilateral disease; however, asymmetry between the two eyes in visual acuity and macular atrophy extent is a recognized and somewhat distinctive clinical feature (asymmetric VA loss associated with central macular atrophy after age 10, per the 2026 Retina cohort).

---

## 8. Temporal Development

**Onset:** Childhood/juvenile-onset — mean symptom onset ~9.4 years (range 3–16 years across cohorts); essentially all patients symptomatic before age 16. Onset pattern is **insidious** (gradual nyctalopia progressing over years), not acute.

**Progression:**
- **Stages (informal, based on natural history cohorts):** (1) Early — nyctalopia with preserved central acuity, childhood; (2) Intermediate — progressive peripheral field constriction with emerging macular atrophy, typically starting after age 10; (3) Advanced — significant bilateral, often asymmetric, central vision loss with legal blindness reached by young-to-mid adulthood (by age 39 in one series; VA 20/70 or worse in at least one eye after age 17 in nearly all patients).
- **Rate:** Relatively rapid/aggressive compared to many other RP genotypes — described as "early-onset and severe form of autosomal recessive RP." Quantified structural progression: EZ width loss ~141 µm/year; central macular thickness loss ~11.2 µm/year; BCVA decline ~0.05 logMAR/year (PMID 34289798). The Faroese founder-deletion homozygotes showed "onset in the first decade followed by a rapid deterioration of both rod and cone photoreceptor function."
- **Course pattern:** Chronic, progressive, non-remitting — no episodic or relapsing-remitting pattern described.
- **Duration:** Lifelong, chronic, currently non-reversible (though early-phase gene therapy trials aim to slow/halt progression — see Section 12).

**Patterns:** No spontaneous remission reported. No clearly defined "critical window" for intervention has been established in humans, though gene therapy trials have targeted patients across a wide age range (14–54 years in the AAV2 phase I trial), and preclinical models suggest earlier intervention (before substantial photoreceptor loss) is likely to preserve more function — consistent with general IRD gene therapy principles.

---

## 9. Inheritance and Population

**Inheritance pattern:** Autosomal recessive (confirmed by ClinGen Definitive classification, 2022).

**Penetrance:** Appears complete/high in biallelic pathogenic variant carriers based on reported pedigrees, though formal penetrance estimates were not identified — **data gap**.

**Expressivity:** Variable — age of onset (3–16 years) and rate of progression vary across families/genotypes, suggesting variable expressivity, possibly genotype-dependent (null vs. missense alleles).

**Genetic anticipation:** Not described/not applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically reported for MERTK.

**Founder effects:**
- **Faroe Islands:** A 91-kb deletion (exons 1–7) is a common founder mutation responsible for **~30%** of nonsyndromic RP cases in this population; carrier frequency ~3% among Faroese controls (3/94 anonymous controls) (PMID 21677792).
- **North Africa:** MERTK variants account for **~18%** of rod-cone dystrophy in some North African cohorts (vs. ~1% generally in mixed populations) — reflecting regional founder alleles and high consanguinity rates.
- **Middle East:** Multiple consanguineous pedigrees reported (Saudi Arabia — site of the AAV2 gene therapy trial; other Gulf states).

**Consanguinity:** Plays a major role — many published families are consanguineous, consistent with autosomal recessive inheritance and regional prevalence patterns.

**Carrier frequency:** General population carrier frequency is presumed low (consistent with ~1% contribution to AR RP generally), but elevated in founder populations (e.g., ~3% in Faroe Islands for the specific 91-kb deletion). Population-wide gnomAD-derived carrier frequency estimates were not retrieved in this session — **recommend direct gnomAD query**.

### Epidemiology
- General RP prevalence: ~1/3,500 to 1/4,000 (varies by source, 1/2,500–1/4,000 range).
- Inheritance breakdown of RP overall: autosomal recessive 15–25%, autosomal dominant 5–20%, X-linked recessive 5–15%, simplex/unknown 40–50%.
- **MERTK contributes ~1–2–3% of autosomal recessive RP/IRD cases generally**, with substantially higher regional contributions in the Faroe Islands (~30% of RP) and North Africa (~18% of rod-cone dystrophy).
- Estimated global affected population: Opus Genetics cites "an estimated 60,000 patients worldwide" for MERTK-related RP (StockTitan/Foundation Fighting Blindness press coverage, 2026) — this is an industry/advocacy estimate rather than a peer-reviewed epidemiologic figure and should be treated with appropriate caution.

**Population demographics:** No strong sex predilection reported (consistent with autosomal, non-sex-linked inheritance). Geographic clustering in the Faroe Islands, North Africa, and consanguineous Middle Eastern populations, alongside sporadic cases described worldwide (China, Pakistan, UK, US).

---

## 10. Diagnostics

**Clinical tests:**
- **Fundoscopic examination:** RP-pattern findings — bone-spicule pigmentation (variable), attenuated vessels, waxy disc pallor, optic disc drusen (frequently noted in the 2026 Retina cohort), myopia.
- **Electroretinography (ERG):** Full-field and pattern ERG markedly reduced/"barely recordable" in established disease — used to confirm rod-cone dysfunction pattern.
- **Optical coherence tomography (OCT):** Ellipsoid zone (EZ) width and central macular thickness as quantitative structural biomarkers of progression; characteristic subretinal hyper-reflective debris/deposits distinguish MERTK retinopathy from many other IRD genotypes.
- **Fundus autofluorescence (FAF), including ultra-widefield:** Central macular hyperautofluorescence pattern.
- **Visual field testing:** Documents peripheral constriction.
- **Visual acuity (BCVA):** Serial tracking is a core outcome measure in natural history and trial studies.

**Genetic testing:**
- **Recommended approach:** Multi-gene NGS panel testing for inherited retinal disease (IRD) is first-line, given phenotypic overlap with many other rod-cone/cone-rod dystrophy genes; MERTK is included in standard comprehensive IRD panels (e.g., 176-gene and 351-gene panels referenced in PMC8683638 and PMC11276581).
- **Panel-based testing yield:** Achieves molecular diagnosis in ~59% of IRD patients overall (higher, ~92%, in children under 6).
- **WES/WGS:** Useful for cases where panel testing is non-diagnostic, or to detect structural/deep-intronic variants (e.g., large deletions like the Faroese 91-kb deletion, which would require copy-number-sensitive analysis such as CMA, targeted deletion/duplication analysis, or WGS rather than standard exome capture alone).
- **Single-gene testing/segregation analysis:** Useful in known consanguineous families or when a specific founder variant is suspected (e.g., targeted testing for the Faroese deletion in that population).
- **Chromosomal microarray/karyotype/FISH:** Not primary diagnostic modalities for MERTK (disease is not caused by large chromosomal rearrangements/aneuploidy), though CMA or targeted CNV analysis can detect the multi-exon deletions reported in several families.
- **Mitochondrial DNA testing:** Not applicable (nuclear gene, autosomal recessive).

**Clinical/differential diagnosis:** MERTK-related retinopathy must be differentiated from other causes of childhood-onset rod-cone/cone-rod dystrophy and early macular atrophy, including RPE65-associated Leber congenital amaurosis/early-onset RP, CRB1-associated retinal dystrophy, ABCA4-associated Stargardt disease/cone-rod dystrophy, RDH12, and other autosomal recessive RP genes (EYS, USH2A with associated hearing loss in Usher syndrome, etc.) — the presence of striking subretinal debris on OCT and disproportionately early macular atrophy are clues favoring MERTK. Genetic testing is required for definitive differentiation since fundus appearance alone is not gene-specific.

**Screening:** No population-based newborn or carrier screening program specific to MERTK was identified; carrier screening would follow general ACMG guidance for autosomal recessive conditions and would be most relevant in high-prevalence founder populations (e.g., Faroe Islands) or for at-risk consanguineous couples via targeted or expanded carrier screening/GTR-listed panels.

---

## 11. Outcome/Prognosis

**Survival/mortality:** MERTK-related retinopathy is an ocular-limited disease with **no reported impact on life expectancy or systemic mortality** in the human literature reviewed.

**Morbidity/functional outcome:** Progressive to severe visual disability — legal blindness reported by age 39 in one series, and VA 20/70 or worse in at least one eye after age 17 in nearly all patients in the 2026 cohort. This represents substantial lifelong disability affecting independence, education, employment, and mobility, though no MERTK-specific formal disability/QOL instrument data (ICF, EQ-5D, PROMIS) were identified — **data gap**.

**Disease course/complications:** Chronic progressive vision loss; no reported systemic complications. Ocular complications specifically related to investigational gene therapy (not the natural disease) include cataract progression, transient subfoveal fluid, filamentary keratitis, and (in two trial patients) unresolved severe visual acuity loss post-injection (PMID 26825853) — important for informed consent/risk discussions in future trials.

**Recovery potential:** Without treatment, disease is non-reversible and progressive. With investigational gene therapy, three of six patients in the phase I AAV2 trial showed measurable VA improvement, but improvement was lost by 2 years in two of the three — indicating that current gene augmentation approaches may provide only transient benefit, underscoring the ongoing need for improved vectors/protocols (addressed by newer trials, e.g., Opus Genetics' OPGx-MERTK).

**Prognostic factors:** Genotype severity (null vs. missense alleles) is an informal prognostic consideration; age/stage at diagnosis affects the amount of remaining photoreceptor structure (EZ width, ONL thickness) available for potential therapeutic rescue — earlier intervention is generally presumed more favorable, consistent with general IRD gene therapy principles, though not proven in a controlled MERTK-specific trial.

**Prognostic biomarkers:** OCT-derived ellipsoid zone width and central macular thickness, and FAF-defined area of "definitely decreased autofluorescence" (DDAF), have been proposed and used as quantitative biomarkers of disease progression and potential trial endpoints (PMID 34289798; 2026 Retina cohort study).

---

## 12. Treatment

**Current standard of care:** **No approved disease-modifying or curative therapy exists.** Management is supportive only:
- **Supportive/rehabilitative care:** Low-vision aids (magnifiers, handheld/bioptic telescopes, CCTV systems, high-contrast lenses, electronic reading/speech-output devices), orientation and mobility training, glare control/illumination optimization, and low-vision counseling.
- **Nutritional supplementation:** Vitamin A palmitate has been used empirically in RP generally, but evidence is mixed/controversial and not proven to alter visual field, acuity, or dark adaptation in controlled trials; no MERTK-specific vitamin A efficacy data exist.
- **MAXO term suggestions:** "vision assistive device provision," "low vision rehabilitation," "genetic counseling," "orientation and mobility training."

**Advanced/experimental therapeutics — Gene therapy (most advanced modality for this specific gene):**
- **Preclinical:** AAV2-VMD2-hMERTK (AAV2 vector, RPE-specific VMD2/bestrophin-1 promoter driving human MERTK cDNA) rescued phagocytic function and photoreceptor structure in the RCS rat model, with demonstrated potency and ocular-confined biodistribution (Conlon et al., PMID 23692380).
- **Completed Phase I trial (NCT01482195):** Subretinal rAAV2-VMD2-hMERTK in 6 patients (ages 14–54) — "acceptable ocular and systemic safety profile" over 2-year follow-up; 3/6 patients showed measurable VA improvement, lost in 2/3 by 2 years; adverse events included filamentary keratitis, progressive cataract, transient subfoveal fluid, monocular oscillopsia; no vector-attributable severe adverse events, though two patients (unrelated report) experienced unresolved severe VA loss post-procedure requiring careful risk disclosure (Ghazi et al., PMID 26825853).
- **New trial (2026, in development):** Opus Genetics' **OPGx-MERTK**, an AAV-based gene therapy, funded via Abu Dhabi's Healthcare Research and Innovation Fund, with Cleveland Clinic Abu Dhabi as the clinical site; clinical development activities expected to commence in 2026, targeting an estimated 60,000 patients worldwide with no approved treatment.
- **MAXO term suggestion:** "gene replacement therapy," "subretinal injection administration."

**Other experimental/preclinical approaches:**
- **Translational readthrough-inducing drugs (TRIDs):** PTC124 partially restored phagocytosis in an iPSC-RPE MERTK-deficient (nonsense/frameshift, likely applicable to premature termination codon alleles) disease model, illustrating a potential small-molecule strategy for nonsense-mutation subgroups (PMID 28303901/Scientific Reports 2017).
- **CRISPR/base editing:** At least one MERTK variant has been noted as a single-nucleotide transition theoretically amenable to CRISPR-Cas9 base editing (PMC8486302 review) — preclinical/conceptual stage only, no human trials identified.
- **Long-term rescue studies in rodent models** (e.g., Nat Sci Rep 2018, "Long-term Rescue of Photoreceptors in a Rodent Model of Retinitis Pigmentosa Associated with MERTK Mutation") support continued gene-therapy vector optimization.

**Pharmacogenomics:** No MERTK-specific pharmacogenomic data identified (not applicable to a gene-replacement paradigm in the same way as small-molecule drug metabolism).

**Treatment algorithm:** Given absence of approved therapy, current clinical pathway is: (1) genetic confirmation of diagnosis, (2) baseline and serial structural/functional biomarker monitoring (OCT EZ width, BCVA, FAF), (3) supportive low-vision care, (4) genetic counseling for family planning, and (5) referral to gene therapy clinical trials where eligible/available (e.g., emerging Opus Genetics OPGx-MERTK trial).

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense (no modifiable risk factor); the only "primary prevention" avenue is genetic — carrier screening and reproductive counseling in at-risk families/populations (e.g., consanguineous couples, Faroese descent) to inform reproductive decision-making, including preimplantation genetic diagnosis (PGD) or prenatal testing where a familial pathogenic variant is known.

**Secondary prevention:** Early genetic diagnosis via NGS panel testing in children presenting with nyctalopia enables earlier initiation of low-vision support services and, potentially, earlier eligibility for gene therapy trials before extensive photoreceptor loss occurs (biologically plausible rationale, not yet proven in controlled human studies).

**Tertiary prevention:** Low-vision rehabilitation, mobility training, and psychosocial support to minimize functional disability and complications of severe vision loss (falls, social/occupational impact) once disease is established.

**Genetic counseling:** Central to management — autosomal recessive inheritance implies 25% recurrence risk for future affected offspring of carrier parents; counseling should address consanguinity risk, founder variant testing in relevant populations, and availability of clinical trials.

**Screening:** No population-based public health screening program exists; targeted carrier screening is most relevant in high-prevalence founder populations (Faroe Islands) or in genetic counseling settings for consanguineous families with a family history of early-onset RP.

**Immunization/infectious prevention:** Not applicable (non-infectious, monogenic disease).

---

## 14. Other Species / Natural Disease

**Taxonomy and naturally occurring disease:**
- **Rat — Royal College of Surgeons (RCS) rat** (*Rattus norvegicus*, NCBI Taxon 10116): The classical, decades-old naturally occurring model. Caused by a large deletion in *Mertk* (~409 bp reported in one study; ~1,850 bp reported in another, resulting in a truncated protein) that abolishes RPE phagocytic function, producing progressive photoreceptor degeneration. This model **preceded and directly led to discovery** of human MERTK-RP (D'Cruz et al., *Hum Mol Genet* 2000; Gal et al., *Nat Genet* 2000). Historically the single most important natural animal model of RPE-phagocytosis-defect retinal degeneration and the basis for the first successful RPE-directed retinal gene therapy proof-of-concept (viral *Mertk* gene transfer corrected the phenotype — PMID 11592982).
- **Dog — Swedish Vallhund** (*Canis lupus familiaris*): A naturally occurring progressive retinal atrophy (PRA) mapped to an intronic LINE-1 retroelement insertion (6–8 kb) in *MERTK* intron 1, recessively inherited, conferring ~20-fold increased risk of retinopathy in homozygotes; phenotype: normal early vision progressing to nyctalopia and eventual day-vision impairment (PMC5558984). A distinct, milder canine retinopathy with *increased* MERTK expression has also been described in another breed context (PMC4269413), indicating that both loss- and altered-expression mechanisms can produce canine retinal disease at this locus.

**Veterinary relevance:** Genetic testing for the Swedish Vallhund LINE-1 insertion is commercially available (e.g., cagt.co.uk) for breeding management, given the ~20-fold risk association and recessive inheritance.

**Comparative biology:** The RPE phagocytosis pathway and MERTK's role are highly conserved across mammals (rat, dog, mouse, human), supporting strong translational validity of these animal models for mechanism and gene-therapy development. Orthologous gene: *Mertk* (mouse, MGI:96965; NCBI Gene 17289), *Mertk* (rat, NCBI Gene 56822).

**Zoonotic/transmission potential:** Not applicable — this is a non-infectious, purely genetic disease; no cross-species transmission relevance.

---

## 15. Model Organisms

**Mammalian genetic models:**
- **RCS rat (spontaneous/naturally occurring):** Gold-standard model; loss-of-function *Mertk* mutation causes RPE phagocytic failure and progressive photoreceptor degeneration; extensively used for gene therapy proof-of-concept (viral *Mertk* delivery corrects phagocytic defect and rescues photoreceptors — PMID 11592982; long-term rescue data in Sci Rep 2018).
- **Mertk knockout mouse (Mertk⁻/⁻, engineered):** Recapitulates an "RCS-like retinal dystrophy phenotype" (IOVS, ARVO). Also used extensively to study MERTK's systemic efferocytosis/immune roles — defective clearance of apoptotic thymocytes/lymphocytes, autoimmune susceptibility (lupus-like phenotype in TAM-deficient mice), and microglial efferocytosis defects. A newer independent knockout allele (PMC11121519, 2024) was generated to re-evaluate and dissect phagocytic versus anti-inflammatory MERTK functions, noting that some other *Mertk* mutant alleles (e.g., *Mertk^nmf12*) do **not** phenocopy the early/rapid RCS-like degeneration — indicating allele-specific phenotypic variability even within mouse models, an important caveat for interpreting model data.
- **MerTK-cleavage-resistant mouse (engineered, 2024, Frontiers in Neuroscience):** A gain-of-function/cleavage-resistant model showing retinal atrophy, inflammation, and phagocytic/metabolic disruption — used to dissect the physiological role of MERTK ectodomain shedding, complementary to loss-of-function models.

**Cellular/in vitro models:**
- **Patient-derived iPSC-RPE model:** Generated from a patient with the Ser331Cysfs*5 frameshift variant; iPSC-RPE cells showed absent MERTK protein and near-absent phagocytic uptake of fluorescently labeled photoreceptor outer segments (minimal internalization vs. clear internalization in controls) — validates human cellular disease modeling and serves as a drug-screening platform (Sci Rep 2015, PMID 26263531; used subsequently for PTC124 TRID rescue studies, Sci Rep 2017).
- **Human pluripotent stem cell-derived RPE (hPSC-RPE), general):** Used to dissect MERTK-dependent POS ensheathment mechanisms mechanistically (PMC7066375), independent of patient-specific mutations.

**Model characteristics — recapitulation and limitations:**
- Rodent and canine models faithfully recapitulate the core RPE phagocytic defect and progressive photoreceptor loss, and have been essential for gene therapy vector development directly translated into human trials.
- **Limitation:** Mouse *Mertk*-null models show variable degeneration kinetics depending on the specific allele, complicating direct extrapolation; the RCS rat, while historically foundational, has a genetic background (large deletion, potentially affecting neighboring genes/regulatory elements) that may not perfectly mirror discrete human point mutations.
- Human iPSC-RPE models capture the RPE-intrinsic phagocytic defect faithfully but, being 2D monolayer cultures, do not recapitulate the full retinal architecture, chronic inflammatory microenvironment, or systemic immune components (efferocytosis in lymphoid tissue, autoimmunity) seen in whole-organism knockout models.

**Applications:** RCS rat and *Mertk*-KO mice — gene therapy vector testing (AAV serotype/promoter optimization), natural history/mechanism studies, and pharmacological modulator testing (e.g., MERTK inhibitor ocular safety studies, PMC8837544, relevant given MERTK's dual role as an oncology drug target). iPSC-RPE — patient-specific mechanism validation and small-molecule (TRID) drug screening for genotype-specific approaches (e.g., nonsense-mutation readthrough).

**Resources:** MGI (Mouse Genome Informatics) for *Mertk* mouse alleles; RGD (Rat Genome Database) for RCS rat strain data; no major zebrafish or invertebrate (Drosophila/C. elegans/yeast) MERTK-retinopathy model was identified in this search, likely reflecting the RPE-specific, mammalian-retina-dependent nature of the phenotype.

---

## Summary of Key Data Gaps
- Precise current gnomAD allele/carrier frequencies for specific MERTK pathogenic alleles (recommend direct database query).
- MERTK-specific validated QOL instrument data (EQ-5D/SF-36/PROMIS).
- Human transcriptomic/proteomic/metabolomic/lipidomic/epigenomic datasets specific to MERTK-retinopathy RPE or retina.
- Formal penetrance/expressivity statistics beyond qualitative case-series impressions.
- A confirmed, disease-specific Orphanet ORPHA number (requires direct Orphanet database verification).
- Systematic human data on whether MERTK's systemic immune/efferocytosis role produces subclinical autoimmune findings in patients.

## Selected Key Citations (PMID)
- Gal A et al., *Nat Genet* 2000 — PMID 11062461 (original human gene discovery)
- Mackay DS et al., *Mol Vis* 2010 — PMID 20300561 (childhood-onset rod-cone dystrophy phenotype)
- Conlon TJ et al., *Hum Gene Ther* 2013 — PMID 23692380 (preclinical AAV2 vector)
- Ghazi NG et al., *Hum Genet* 2016 — PMID 26825853 (Phase I gene therapy trial)
- Lew DS et al./Charbel Issa et al., *Sci Rep* 2015 — PMID 26263531 (iPSC-RPE disease model)
- Ksantini/Faroe Islands founder deletion — PMID 21677792
- MERTK retinopathy biomarkers — PMID 34289798
- ClinGen Gene-Disease Validity Curation (MONDO:0800394), Definitive classification, approved 2022-07-07