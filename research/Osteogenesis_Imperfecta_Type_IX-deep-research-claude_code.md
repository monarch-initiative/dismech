---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-4-6
cached: false
start_time: '2026-06-30T06:41:07.363997'
end_time: '2026-06-30T06:47:43.962084'
duration_seconds: 396.6
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Osteogenesis Imperfecta Type IX
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
  - claude-sonnet-4-6
  web_search_requests: 20
  num_turns: 27
  total_cost_usd: 1.6840811000000002
  session_id: a0983c7d-7ead-508e-9595-741563096619
  stop_reason: end_turn
citation_count: 12
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Osteogenesis Imperfecta Type IX
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Osteogenesis Imperfecta Type IX** covering all of the
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

I now have sufficient data to compile the comprehensive research report. Let me write it up.

---

# Osteogenesis Imperfecta Type IX — Comprehensive Research Report

---

## 1. Disease Information

### Overview

Osteogenesis Imperfecta Type IX (OI9; OI type 9) is a rare, autosomal recessive form of brittle bone disease caused by loss-of-function variants in the *PPIB* gene (peptidylprolyl isomerase B), which encodes cyclophilin B (CyPB), an endoplasmic reticulum–resident peptidyl-prolyl cis-trans isomerase. OI type IX was formally delineated as a molecular subtype when Van Dijk et al. (2009) demonstrated that homozygous null mutations in *PPIB* cause severe-to-lethal bone fragility (PMID: 19781681). It is distinguished from other recessive OI types affecting the prolyl 3-hydroxylation complex (types VII and VIII, caused by *CRTAP* and *LEPRE1/P3H1* mutations, respectively) primarily by the absence of rhizomelia (proximal limb shortening) and by a relatively broader phenotypic spectrum ranging from perinatal lethality to moderate deforming disease.

### Key Identifiers

| Resource | Identifier |
|----------|------------|
| OMIM | **#259440** |
| Orphanet | ORPHA:216820 |
| MONDO | MONDO:0012978 |
| ICD-10 | Q78.0 (Osteogenesis imperfecta) |
| ICD-11 | LD24.00 |
| MeSH | C537614 |
| NCBITaxon | 9606 (Homo sapiens) |
| Gene HGNC | hgnc:9239 (PPIB) |

### Synonyms and Alternative Names

- Osteogenesis imperfecta, type 9
- OI9
- Osteogenesis imperfecta due to cyclophilin B deficiency
- PPIB-related osteogenesis imperfecta
- Cyclophilin B-deficient osteogenesis imperfecta
- Recessive OI type IX

### Evidence Base

Information is derived from aggregated disease-level resources (OMIM, Orphanet), published molecular genetics studies, individual patient case reports, and animal model data from the *Ppib*-null mouse. Because OI type IX is extremely rare, the clinical literature consists primarily of small case series and individual family reports rather than large epidemiological cohorts.

---

## 2. Etiology

### Disease Causal Factors

OI type IX is a **monogenic disorder**. It is caused exclusively by biallelic (homozygous or compound heterozygous) loss-of-function variants in *PPIB* (chromosome 15q22.31), the gene encoding cyclophilin B (CyPB). There are no established non-genetic causes. The disorder arises from deficiency of CyPB, which impairs post-translational modification of type I procollagen in the endoplasmic reticulum.

### Genetic Risk Factors

- **Causal gene:** *PPIB* (HGNC:9239), chromosome 15q22.31
- **Inheritance:** Autosomal recessive — both copies of *PPIB* must be non-functional for disease to occur
- **Carrier status:** Heterozygous carriers are phenotypically unaffected
- **Founder variants:** A homozygous missense variant c.509G>A / p.Gly170Asp is specific to East Asian (predominantly Chinese) populations, with an allele frequency of ~0.000924 in gnomAD East Asian populations; estimated variant age ~65,160 years (PMID: 34659339)
- **Consanguinity:** Described in multiple consanguineous families given the rarity of null alleles

### Pathogenic Variants Reported

| Variant | Effect | Families | Reference |
|---------|--------|----------|-----------|
| c.556–559delAAGA (exon 5); p.Lys186GlnfsX8 | Frameshift, truncation of 31 C-terminal amino acids | 1 | PMID: 19781681 |
| c.451C>T (exon 4); p.Gln151X | Nonsense, removes 65 C-terminal amino acids | 1 | PMID: 19781681 |
| c.136-2A>G (splice site) | Likely NMD/null | 1 (Native American) | PMID: 27625864 |
| c.509G>A (exon 4); p.Gly170Asp | Missense, pro-isomerase domain | Multiple Chinese families | PMID: 34659339 |
| Multiple additional loss-of-function variants | Various null effects | Multiple | PMID: 21282188 |

**Functional consequences:** All reported variants result in absence or severe reduction of CyPB protein. Critically, CyPB loss is independent of its complex partners: in patient fibroblasts, P3H1 levels are substantially reduced (indicating P3H1 stability depends partially on CyPB), but CRTAP remains unaffected (PMID: 19781681).

### Environmental Risk Factors

No environmental risk factors specifically modulate risk of OI type IX. As a Mendelian autosomal recessive disorder, risk is determined entirely by carrier status of parents. Advanced parental age is not a significant risk factor. Consanguinity increases the probability of biallelic inheritance in rare-allele families.

### Protective Factors

No genetic protective factors have been identified that prevent disease expression once biallelic *PPIB* mutations are inherited. Modifier alleles affecting collagen processing could theoretically modulate severity but have not been systematically identified.

---

## 3. Phenotypes

OI type IX spans a **spectrum from perinatal lethality to moderate deforming disease** (PMID: 21282188). The majority of reported patients have severe-to-lethal phenotypes, but at least one molecularly confirmed patient without rhizomelia has had a moderate disease course.

### Core Skeletal Phenotypes

| Phenotype | HPO Term | Frequency | Severity | Notes |
|-----------|----------|-----------|----------|-------|
| Recurrent bone fractures | HP:0002757 | Very frequent (80–100%) | Severe | Often begin prenatally; long bone and rib fractures at birth |
| Multiple prenatal fractures | HP:0002813 | Frequent | Severe | Key distinguishing feature of severe/lethal form |
| Osteoporosis / osteopenia | HP:0000939 | Very frequent | Severe | Dramatically reduced bone mineral density |
| Bone deformity / bowing of long bones | HP:0002645 | Frequent | Moderate–severe | Bowed femora and tibiae |
| Short stature | HP:0004322 | Frequent | Moderate–severe | Progressive growth deficiency |
| Kyphosis | HP:0002808 | Frequent | Progressive | Progressive spinal curvature; prominent in mouse model (PMID: 19997487) |
| Scoliosis | HP:0002650 | Frequent | Progressive | — |
| Platyspondyly | HP:0000926 | Present | Moderate | Flattened vertebral bodies |
| Pectus deformity | HP:0000768 | Present | Variable | Narrow chest contributing to respiratory compromise |
| Wormian bones | HP:0002645 (radiographic) | Present | — | Sutural bones on skull radiograph |
| Joint hypermobility | HP:0001382 | Present | Mild | Ligamentous laxity |
| Decreased calvarial ossification | HP:0002683 | Present in severe cases | — | — |

### Extraskeletal Phenotypes

| Phenotype | HPO Term | Frequency | Notes |
|-----------|----------|-----------|-------|
| Blue sclerae | HP:0000592 | Present (variable) | Caused by abnormal scleral collagen; not consistently reported in all PPIB cases |
| Dentinogenesis imperfecta | HP:0000703 | Present (variable) | Discolored, translucent, fragile teeth |
| Sensorineural hearing loss | HP:0000407 | Present (inconsistent) | Congenital bilateral SNHL documented in one Native American case (PMID: 27625864); may be co-incidental in some patients |
| Loose/lax skin | HP:0000963 | Present in model | Documented prominently in Ppib-KO mouse; human data limited |
| Respiratory compromise | HP:0002093 | Frequent in severe cases | Secondary to narrow chest and rib fractures |
| Triangular face | HP:0000325 | Present | Characteristic facial gestalt |
| Delayed motor development | HP:0001270 | Frequent | Secondary to fractures and deformity |
| Wheelchair dependence | HP:0004736 | Present in severe cases | One surviving patient wheelchair-dependent by age 7 (PMID: 19781681) |

### Clinical Distinctive Features Vs. Other Recessive OI Types

A key distinguishing phenotypic feature is the **absence of rhizomelia** (proximal limb shortening) in OI type IX, contrasting with OI types VII (CRTAP) and VIII (LEPRE1/P3H1), which typically show rhizomelic shortening of upper extremities. As noted for the Native American patient: "There appears to be a trend toward rhizomelic shortening and less severe bowing of the extremities, as compared to patients with comparably severe OI caused by COL1A1 or COL1A2 mutation" (PMID: 27625864)—though one case did show prenatal rhizomelia, indicating phenotypic overlap.

### Hearing Loss

Hearing loss management recommendations: "Patients with OI caused by PPIB mutation should have appropriate early and regular management of their hearing" (PMID: 27625864). Whether congenital sensorineural hearing loss is a true recurrent feature of OI type IX or represents a co-incidental finding remains uncertain given limited case numbers.

### Onset and Severity

- **Onset:** Prenatal in severe/lethal cases (fractures visible on ultrasound in 2nd trimester); perinatal in lethal form; early postnatal in survivors
- **Severity spectrum:** Perinatal lethality (Sillence type II equivalent) to severe deforming (Sillence type III equivalent) to moderate
- **Progression:** Progressive deformity with growth; multiple fractures throughout childhood and potentially adulthood

---

## 4. Genetic / Molecular Information

### Causal Gene

- **Gene symbol:** *PPIB*
- **Gene full name:** Peptidylprolyl isomerase B (cyclophilin B)
- **HGNC ID:** hgnc:9239
- **OMIM Gene:** #123841
- **Chromosome location:** 15q22.31
- **Protein:** Cyclophilin B (CyPB), 21 kDa
- **Alternative gene names:** CYP-S1, CYPB, HEL-S-39, SCYLP

### Variant Classification

All reported disease-causing variants are classified **pathogenic or likely pathogenic** (ACMG/AMP criteria). The founder variant p.Gly170Asp received PM3, PM1 (change at pro-isomerase domain), and PP3 (REVEL score 0.94) evidence codes (PMID: 34659339).

**Variant types reported:**
- Nonsense (PTC)
- Frameshift (deletion)
- Splice-site
- Missense (affecting pro-isomerase domain)

All result in **loss of function**. Biochemical studies consistently reveal undetectable CyPB protein in patient fibroblasts from families with frameshift/nonsense mutations (PMID: 19781681).

### Allele Frequency

- The c.509G>A / p.Gly170Asp Chinese founder allele frequency in gnomAD: 0.000924 in East Asian populations; absent in non-East Asian populations (PMID: 34659339)
- Other pathogenic alleles are extremely rare, below gnomAD detection thresholds or absent

### Somatic vs. Germline

OI type IX is exclusively a **germline** disorder. Somatic mosaicism is theoretically possible but has not been documented in published literature.

### Modifier Genes

No confirmed modifier genes have been described for OI type IX specifically. In the broader OI context, variants in *BMP1*, *PLOD2*, *IFITM5*, and other collagen-modifying genes have been considered modifiers, but these have not been specifically studied in PPIB-null disease.

### Chromosomal Abnormalities

Not applicable; OI type IX is a point mutation / small insertion-deletion disorder without large-scale chromosomal changes.

---

## 5. Environmental Information

### Environmental Factors

No specific environmental toxins, radiation, or occupational exposures are known to cause or exacerbate the molecular defect in OI type IX. As with all OI, **secondary fracture risk** may be modulated by environmental factors including fall risk, activity level, and calcium/vitamin D nutrition, but these do not alter the underlying genetic defect.

### Lifestyle Factors

- Calcium and vitamin D supplementation are standard supportive measures for all OI patients
- Exercise programs (especially swimming, low-impact activities) are recommended to build muscle strength and improve mobility
- Contact sports are generally contraindicated

### Infectious Agents

Respiratory infections are a significant **complication** (not cause) in patients with severe thoracic involvement. The Native American patient with lethal OI IX died at age 16 months from pneumonia (PMID: 27625864). Recurrent respiratory infections are a major source of morbidity in the severe phenotype.

---

## 6. Mechanism / Pathophysiology

### The Prolyl 3-Hydroxylation Complex

The central pathophysiological mechanism in OI type IX is **deficiency of cyclophilin B (CyPB)**, disrupting multiple post-translational modification steps of type I collagen in the endoplasmic reticulum.

CyPB (PPIB) functions as a component of a heterotrimeric complex with:
1. **P3H1** (prolyl 3-hydroxylase 1, encoded by *LEPRE1/P3H1*) — the enzymatic hydroxylase
2. **CRTAP** (cartilage-associated protein) — structural scaffolding

This complex performs the 3-hydroxylation of **proline at position 986 (P986)** in the α1(I) chain of type I collagen — a modification essential for normal collagen fibril structure and bone mechanical properties.

**Molecular functions of CyPB:**
- **Peptidyl-prolyl cis-trans isomerase (PPIase) activity:** CyPB is proposed to be the major PPIase catalyzing the rate-limiting step in collagen triple-helix formation, catalyzing cis-to-trans isomerization of proline imidic peptide bonds (proline constitutes ~20% of collagen residues)
- **Chaperone function:** CyPB participates in ER chaperone complexes with BiP, GRP94, PDI, and calreticulin
- **Complex stabilization:** CyPB is required for proper P3H1 retention/stability in cells; loss of CyPB leads to substantial reduction of P3H1 levels in patient fibroblasts

### Collagen Modification Defects

**Prolyl-3 hydroxylation:** In PPIB-null patient fibroblasts, P986 3-hydroxylation is severely reduced (to ~33% of controls in OI IX, compared to 93–100% in controls). Paradoxically, this is less severe than in OI VII (CRTAP null, ~16%) and OI VIII (P3H1 null, ~22%), suggesting CyPB influences complex function but P3H1 retains partial activity without CyPB (PMID: 19781681). In the *Ppib*-KO mouse, only 5–11% of α1(I) P986 residues were hydroxylated in osteoblasts and fibroblasts, and 1–2% in tissue (PMID: 24968150).

**Collagen folding delay:** "Collagen folds more slowly in the absence of CyPB," with 5–8 minute delays in triple helix formation documented in *Ppib*-KO osteoblasts. This implicates CyPB as the predominant collagen PPIase, though residual CsA-sensitive activity (possibly FKBPs) provides partial redundancy (PMID: 24968150).

**Lysyl hydroxylation defects — a distinctive biochemical signature:** Beyond the prolyl-3 hydroxylation defect, CyPB deficiency creates tissue-specific dysregulation of helical lysyl hydroxylation and glycosylation by **disrupting lysyl hydroxylase (LH) chaperone complexes**:
- In bone: site-specific underhydroxylation at crosslinking residues α1(I) K87 (57% vs. 98% in wild-type) and α2(I) K87 (45% vs. 77%), leading to an altered collagen crosslink profile
- In skin: >80% decrease in total hydroxylysine; positive regulatory LH chaperones (FKBP65/Sc65/P3H3) drop to <11% of wild-type while negative regulator HSP47 increases
- "CyPB deficiency profoundly affects Lys post-translational modifications of collagen likely by modulating LH chaperone complexes" (PMID: 30562343)

**Crosslink abnormalities:** In *Ppib*-KO bone:
- Nearly 3-fold increase in the helical lysine-involved crosslink hydroxylysinonorleucine (HLNL)
- Lysylpyridinoline (LP) increased 4–5-fold
- HP/LP (hydroxylysylpyridinoline/lysylpyridinoline) ratio decreased 4.25- to 5.6-fold
- Deoxy-HHMD and LNL (non-hydroxylysine crosslinks) form exclusively in KO tissue (PMID: 24968150)

These crosslink alterations reduce bone mechanical competence independently of the prolyl-3 hydroxylation defect.

**ER trafficking defect:** In CyPB-deficient fibroblasts, "a significant amount of collagen remained in the ER" rather than trafficking properly to the Golgi after ascorbic acid stimulation (PMID: 19997487), indicating disrupted intracellular collagen transport.

**Reduced collagen deposition:** Collagen deposited into insoluble extracellular matrix by *Ppib*-KO osteoblasts was decreased ~80%, linked to altered fibrillogenesis and abnormal fibril structure (PMID: 24968150).

### Collagen Fibril Morphology

Transmission electron microscopy of *Ppib*-KO mice shows collagen fibrils are **abnormally enlarged** — on average 1.45 times wider than controls (114.6 ± 22.4 nm vs. 78.6 ± 12.4 nm diameter) (PMID: 19997487), indicating disrupted fibril assembly.

### Causal Chain Summary

```
Biallelic PPIB loss-of-function mutation
    ↓
Absence of cyclophilin B (CyPB) in ER
    ↓
[Branch 1] Reduced P3H1 stability → decreased Pro-986 3-hydroxylation
[Branch 2] Disrupted PPIase activity → delayed collagen triple-helix folding
[Branch 3] Disrupted LH chaperone complexes → abnormal helical lysyl hydroxylation
    ↓
Altered collagen crosslink chemistry (LP↑, HP/LP ratio↓)
Abnormal fibril morphology (enlarged fibrils)
Reduced collagen matrix deposition
    ↓
Defective bone matrix organization and mechanical incompetence
    ↓
Severe osteoporosis, bone fragility, susceptibility to fractures
```

### Cell Types and Biological Processes Involved

**Primary cell types:**
- **Osteoblasts** (CL:0000062): Primary producers of type I collagen; most severely affected by CyPB deficiency
- **Chondrocytes** (CL:0000138): Type II collagen also lacks Pro3-hydroxylation in KO mice
- **Fibroblasts** (CL:0000057): Show ER retention of collagen and reduced P3H1 levels
- **Odontoblasts** (CL:0000060): Involved in dentinogenesis imperfecta

**GO Biological Processes:**
- Collagen fibril organization (GO:0030199)
- Peptidyl-proline modification (GO:0018208)
- Post-translational protein modification (GO:0043687)
- Collagen biosynthetic process (GO:0032964)
- Bone mineralization (GO:0030282)
- Protein folding (GO:0006457)
- Endoplasmic reticulum to Golgi vesicle-mediated transport (GO:0006888)

**GO Cellular Components:**
- Endoplasmic reticulum lumen (GO:0005788)
- Collagen-containing extracellular matrix (GO:0062023)
- Extracellular matrix (GO:0031012)

---

## 7. Anatomical Structures Affected

### Skeletal System (Primary)

- **Long bones** (UBERON:0002492): Femur, tibia, humerus, radius, ulna — cortical thinning, bowing, fractures
- **Spine** (UBERON:0001617): Platyspondyly, kyphoscoliosis
- **Skull** (UBERON:0003129): Decreased calvarial ossification, wormian bones (sutural ossification)
- **Ribs** (UBERON:0002228): Fractures, narrow thorax
- **Teeth** (UBERON:0007759): Dentinogenesis imperfecta

### Secondary Organ Involvement

- **Lung / respiratory system** (UBERON:0001004): Restrictive lung disease secondary to narrow chest; recurrent pneumonias in severe cases
- **Ear** (UBERON:0001690): Sensorineural hearing loss (cochlea); possibly also conductive component
- **Eye / sclera** (UBERON:0001827): Blue sclerae from abnormal scleral collagen
- **Skin** (UBERON:0002097): Documented loose/lax skin; abnormal collagen crosslinking

### Tissue and Cell Level

- **Bone tissue** (UBERON:0002481): Primary affected tissue — osteoporotic cortical and trabecular bone
- **Connective tissue** (UBERON:0002384): Broadly affected given ubiquitous type I collagen
- **Cartilage** (UBERON:0002418): Type II collagen also affected in KO model

### Subcellular Level

- **Endoplasmic reticulum** (GO:0005783): Site of CyPB action; collagen retained here in CyPB deficiency
- **Golgi apparatus** (GO:0005794): Impaired collagen trafficking
- **Extracellular matrix** (GO:0031012): Reduced collagen deposition, abnormal fibril assembly

---

## 8. Temporal Development

### Onset

- **Perinatal lethal form:** Fractures present in utero (detectable by ultrasound at 2nd trimester); bowed long bones at birth; respiratory failure common
- **Severe deforming (non-lethal) form:** Fractures at birth or early infancy; wheelchair dependence by age 7 documented (PMID: 19781681)
- **Moderate form:** Onset with fractures in early childhood; slower progression

### Progression

- **Disease course:** Chronic, progressive
- **Fracture accumulation:** Multiple fractures through childhood and adolescence, often with minimal trauma
- **Deformity progression:** Progressive kyphoscoliosis and long-bone deformity from repeated fracture-healing cycles
- **Lifespan:** Variable — perinatal lethality in severe cases; the *Ppib*-KO mouse has a lifespan of 40–50 weeks with progressive kyphosis (PMID: 19997487)

### Critical Periods

- **Prenatal period:** Fracture accumulation in utero in severe cases
- **Early childhood:** Most critical for fracture management and mobility preservation; "The age at onset of long bone fractures is a critical predictor of future ambulatory ability"
- **Puberty:** BMD typically improves relative to childhood during growth but deformity may worsen

---

## 9. Inheritance and Population

### Epidemiology

- **Overall OI prevalence:** ~1 in 15,000–20,000 births across all types
- **OI type IX specifically:** Extremely rare; estimated incidence in Chinese population ~1/1,000,000 (PMID: 34659339); worldwide frequency not established due to rarity
- **Fraction of all OI:** OI types caused by CRTAP, LEPRE1, and PPIB mutations collectively account for a small minority of OI cases (~5% of total OI); PPIB variants are the least common of the three

### Inheritance Pattern

- **Autosomal recessive (AR)**
- **Penetrance:** Complete — biallelic loss-of-function results in disease
- **Expressivity:** Variable (perinatal lethal to moderate)
- **Consanguinity:** Multiple reported families involve parental consanguinity, consistent with AR inheritance of rare alleles

### Founder Effect

- East Asian (Chinese) populations have a specific founder variant c.509G>A/p.Gly170Asp with estimated mutation age 65,160 years (~3,258 generations), implying spread from a single common ancestral haplotype. This provides the basis for targeted carrier screening in Chinese populations (PMID: 34659339).

### Carrier Frequency

- Based on gnomAD data for the Chinese founder allele (AF ~0.000924), carrier frequency is approximately 1/540 in East Asian populations for this single variant
- No reliable carrier frequency data for global PPIB pathogenic variants

### Sex Ratio

No sex predilection — autosomal recessive, affects males and females equally.

### Geographic Distribution

OI type IX cases have been reported in multiple ethnic and geographic contexts:
- North America (consanguineous families; one Native American family)
- China/Taiwan (multiple families with founder variant)
- Middle Eastern consanguineous families (not specifically OI IX, but recessive OI broadly)

---

## 10. Diagnostics

### Clinical Criteria

No OI-type-IX-specific diagnostic criteria exist. Diagnosis follows the **general OI diagnostic approach** combined with molecular confirmation:

1. Clinical recognition of bone fragility with multiple fractures, ± blue sclerae, ± DI, ± hearing loss
2. Exclusion of non-accidental injury
3. Radiographic assessment (wormian bones, osteopenia, long-bone bowing, platyspondyly)
4. DXA bone mineral density (reduced Z-score for age/height)
5. Molecular genetic confirmation (PPIB sequencing)

### Laboratory Tests

- **Routine labs** are typically normal in OI (including calcium, phosphate, alkaline phosphatase); ALP may be mildly elevated
- **Collagen biochemical analysis:** Electrophoretic analysis of type I collagen from fibroblast culture can show slightly delayed migration (from altered PTMs); may reveal reduced P3H1 complex function
- **Pro-986 hydroxylation assay:** Mass spectrometric analysis can demonstrate reduced Pro-986 3-hydroxylation in collagen from patient fibroblasts (33% vs. controls 93–100%) (PMID: 19781681)

### Imaging

- **Radiographs (X-ray):** Primary modality — reveals osteopenia, long-bone bowing, fractures, platyspondyly, wormian bones
- **Prenatal ultrasound:** Short/bowed long bones in severe cases detectable in 2nd trimester
- **DXA:** Quantitative BMD measurement; height-adjusted Z-scores used in children; reveals severely reduced BMD
- **CT:** For assessment of scoliosis, basilar invagination

### Genetic Testing

- **Preferred approach:** Next-generation sequencing (NGS) gene panel for OI-related genes (includes *COL1A1*, *COL1A2*, *PPIB*, *CRTAP*, *LEPRE1/P3H1*, and others)
- **Whole exome sequencing (WES):** Highly effective; identified novel PPIB variants in multiple families (PMID: 34659339: average WES coverage 242×)
- **Sanger sequencing:** Targeted confirmation of variants and parental carrier testing
- **ACMG/AMP classification:** All reported PPIB variants are pathogenic or likely pathogenic
- **Carrier testing:** Targeted Sanger sequencing of familial variant for parental/sibling testing
- **Prenatal diagnosis:** Chorionic villus sampling or amniocentesis with targeted PPIB analysis is feasible once familial variant is known

Available genetic tests: NIH GTR lists **34 clinical tests** for OI type IX conditions, including sequence analysis (31 tests), deletion/duplication analysis (18), and targeted variant analysis (7).

### Differential Diagnosis

| Condition | Key Distinguishing Feature |
|-----------|--------------------------|
| OI Type VII (CRTAP) | Rhizomelia present; similar prolyl 3-hydroxylation defect |
| OI Type VIII (LEPRE1/P3H1) | Rhizomelia; white sclerae; P986 hydroxylation more severely reduced |
| OI Type I-IV (dominant, COL1A1/2) | Autosomal dominant; structurally abnormal collagen; different collagen electrophoresis |
| Child abuse / non-accidental injury | Normal genetics; absence of family history |
| Hypophosphatasia | Low ALP; *ALPL* mutation; responsive to enzyme replacement |

---

## 11. Outcome / Prognosis

### Survival and Mortality

- **Perinatal lethal form (Type II-equivalent):** Death in utero or within days of birth from respiratory failure secondary to rib fractures and pulmonary hypoplasia
- **Severe deforming form (Type III-equivalent):** Variable survival; one reported patient died at 16 months from pneumonia (PMID: 27625864); survival into adulthood possible with intensive support
- **Life expectancy:** Not established for OI IX specifically; severe OI overall has significantly reduced life expectancy, primarily from pulmonary and neurological complications (basilar invagination)

### Morbidity

- **Mobility:** Progressive loss of ambulatory ability in severe cases; wheelchair dependence may occur by mid-childhood
- **Respiratory:** Restrictive lung disease is a major cause of morbidity and death in severe cases
- **Hearing:** Early-onset bilateral sensorineural hearing loss documented; requires audiological follow-up
- **Chronic pain:** From recurrent fractures and skeletal deformity

### Prognostic Factors

- **Severity of skeletal phenotype at birth** — most important prognostic indicator
- **Achievement of motor milestones** — children achieving independent sitting/standing by age 12 have better ambulatory prognosis
- **Spinal deformity** — severe kyphoscoliosis worsens pulmonary and cardiovascular prognosis
- **Response to bisphosphonate treatment** — improves BMD and may reduce fracture rate

---

## 12. Treatment

### Bisphosphonate Therapy (Standard of Care)

Bisphosphonates are the most established pharmacological treatment across all OI types, including recessive forms:

- **Intravenous pamidronate:** Most widely used in children; typical regimen 1–3 mg/kg every 3–4 months; reduces fracture rate and improves lumbar spine BMD (~25% annual increase in young children); PMID: 25054949
- **Intravenous zoledronic acid:** 0.05 mg/kg/dose; comparable efficacy to pamidronate with fewer infusions; both increase lumbar spine BMD (51.8% vs. 67.6% respectively)
- **Oral alendronate:** Alternative for milder cases
- **Duration:** Typically continued through childhood growth; drug holiday considered after reaching final height

No *PPIB*-specific pharmacological trials exist; bisphosphonate data for OI IX is extrapolated from broader OI studies.

**MAXO term:** MAXO:0000647 (chemotherapy) — not applicable; pharmacotherapy with bisphosphonates: NCIT:C15986 (Pharmacotherapy); specific agents: CHEBI:60753 (pamidronate), CHEBI:74699 (zoledronic acid)

### Emerging Pharmacological Treatments

- **Setrusumab (UX143):** Anti-sclerostin monoclonal antibody promoting bone formation; Phase 2b ASTEROID trial showed BMD improvement in adult OI; Phase 3 ORBIT and COSMIC trials missed primary endpoint (fracture rate reduction) but achieved secondary endpoints (BMD increase); FDA Breakthrough Therapy designation granted. No specific data for OI IX.
- **Anti-TGF-β antibodies (fresolimumab):** Preclinical studies showing promise in OI mouse models
- **4-Phenylbutyrate (4-PBA):** Chemical chaperone shown to rescue ER stress in recessive OI zebrafish models; targets the cellular stress from impaired prolyl hydroxylation complex
- **Denosumab:** Anti-RANKL antibody; small studies in severe pediatric OI; not standard

**MAXO term:** MAXO:0000950 (supportive care) for symptom management

### Surgical Management

- **Intramedullary rodding (telescoping rods — Fassier-Duval, Bailey-Dubow):** Prophylactic stabilization of femora/tibiae prone to bowing and fracture; telescoping rods accommodate growth; telescopic nailing significantly reduces fracture rates (33.3% vs. 75%) and deformity rates (23.3% vs. 50%) vs. traditional nails
- **Osteotomy with internal fixation:** For correction of severe long-bone deformity
- **Spinal surgery:** For severe progressive scoliosis (>40–50°); high complication risk given osteoporotic bone

**MAXO term:** MAXO:0000004 (surgical procedure)

### Supportive Care

- **Physiotherapy:** Aquatic therapy, low-impact exercise; improves muscle strength and mobility; **MAXO:0000011** (physical therapy)
- **Occupational therapy:** Adaptive equipment, fall prevention
- **Calcium and Vitamin D supplementation:** Standard nutritional support
- **Hearing aids / audiological management:** For sensorineural hearing loss; recommended for all PPIB-OI patients (PMID: 27625864)
- **Respiratory support:** Supplemental oxygen, ventilatory assistance in severe cases

### Gene Therapy (Preclinical)

- AAV-based gene editing for collagen mutations is in preclinical development; no specific PPIB-targeted gene therapy trials
- CRISPR/Cas9 and gene addition approaches are in animal model testing
- Stem cell therapy (mesenchymal stem cell transplantation — BOOSTB4 trial) is under investigation for severe OI, potentially applicable to recessive forms

---

## 13. Prevention

### Primary Prevention

- **Genetic counseling** for families with a known PPIB mutation — essential before further pregnancies (MAXO:0000079 genetic counseling)
- **Cascade screening** of siblings and relatives of affected individuals and known carriers
- **Preimplantation genetic diagnosis (PGD):** Available for couples where both are identified carriers

### Secondary Prevention (Early Detection)

- **Prenatal diagnosis:** Molecular analysis of CVS or amniocentesis for known familial PPIB variants; prenatal ultrasound for skeletal dysplasia signs in at-risk pregnancies
- **Newborn screening:** Not currently part of national newborn screening programs; no metabolite-based test exists; diagnosis requires clinical suspicion + genetic testing
- **Founder variant carrier screening:** In East Asian (Chinese) populations, screening for the c.509G>A/p.Gly170Asp founder allele may be considered in preconception or prenatal settings given carrier frequency ~1/540

### Tertiary Prevention (Preventing Complications)

- **Fracture prevention:** Bisphosphonate therapy, intramedullary rodding, avoidance of contact sports
- **Hearing loss monitoring:** Audiological testing at diagnosis and regular follow-up
- **Respiratory monitoring:** Pulmonary function tests; prompt treatment of respiratory infections
- **Scoliosis surveillance:** Regular spinal imaging; early intervention when curvature progresses
- **Nutritional optimization:** Calcium, Vitamin D, protein intake

---

## 14. Other Species / Natural Disease

### Animal Models

OI type IX is not documented as a naturally occurring disease in veterinary species. The PPIB orthologue is highly conserved across mammals.

**NCBI Taxon:** Mus musculus (10090) — primary model

---

## 15. Model Organisms

### Ppib Knockout Mouse Model

The *Ppib*-null (cyclophilin B-deficient) mouse is the principal model organism for OI type IX and was characterized by Choi et al. (PMID: 19997487):

**Phenotype:**
- Severe osteopenia with dramatically reduced trabecular bone volume
- Increased trabecular separation, reduced trabecular number
- Progressive kyphosis, evident by 8 weeks, progressively worsening
- Reduced body size and weight
- Lifespan 40–50 weeks
- Loose, lax skin (Ehlers-Danlos-like properties)
- Normal femur-to-tibia ratios (no rhizomelia)
- Normal fertility and birth appearance

**Collagen findings:**
- Abnormally enlarged collagen fibrils (114.6 ± 22.4 nm vs. 78.6 ± 12.4 nm in controls) — "on average 1.45 times wider than similar samples from littermate control mice" (PMID: 19997487)
- Near-total loss of Pro-986 3-hydroxylation (1–5% vs. near-100% in controls)
- Severely disrupted helical lysyl hydroxylation and crosslink pattern (PMID: 24968150)
- 80% reduction in collagen matrix deposition by osteoblasts
- Reduced total skin collagen content; reduced skin tensile strength

**Molecular findings:**
- P3H1 levels substantially reduced; CRTAP levels unaffected — demonstrating CyPB-dependent P3H1 stabilization
- Collagen retained in ER rather than trafficking to Golgi
- Residual collagen PPIase activity attributable to cyclosporine A-sensitive enzymes (suggesting FKBP redundancy)

**Model limitations (Human-Model Mismatch considerations):**
- Mice do not show rhizomelia observed in some human cases
- Mouse lifespan (40–50 weeks) and the degree of phenotypic severity may not fully recapitulate the human perinatal lethal form
- Mice show pronounced skin laxity; this is less well-documented in human patients
- Mouse bone biology differs from human (faster remodeling, different cortical organization)

**Genetic model type:** Constitutive knockout (whole-body *Ppib* deletion)

**Available resources:**
- MGI: Available through IMPC and KOMP2 programs
- JAX: Ppib-null alleles available for research

---

## Summary of Key Evidence Citations

| PMID | Description |
|------|-------------|
| **19781681** | Van Dijk et al. — First description of PPIB mutations causing OI (2 families; molecular basis established) |
| **19997487** | Choi et al. — Severe OI in *Ppib*-KO mice; phenotypic and molecular characterization |
| **20089953** | Barnes et al. (NEJM) — Lack of cyclophilin B in OI with normal collagen folding (homozygous start-codon mutation; moderate OI, no rhizomelia) |
| **21282188** | Van Dijk et al. — PPIB mutations delay procollagen chain association; perinatal lethal to moderate phenotype spectrum |
| **24968150** | Pokidysheva et al. — Abnormal type I collagen PTM and crosslinking in *Ppib*-KO mouse; lysyl hydroxylation and crosslink chemistry |
| **27625864** | Balasubramanian et al. — PPIB mutation with severe phenotype and congenital hearing loss (Native American case) |
| **34659339** | Zhu et al. — Founder PPIB variant p.Gly170Asp in Chinese population; prevalence estimate 1/1,000,000 |
| **30562343** | Ishikawa et al. — Cyclophilin B control of skin type I collagen lysine PTMs via LH chaperone complexes |

---

**Suggested MONDO ID:** MONDO:0012978 (Osteogenesis imperfecta type IX)

**Key HPO terms:**
- HP:0002757 (Recurrent fractures)
- HP:0000939 (Osteoporosis)
- HP:0002645 (Wormian bones)
- HP:0002808 (Kyphosis)
- HP:0002650 (Scoliosis)
- HP:0000592 (Blue sclerae)
- HP:0000703 (Dentinogenesis imperfecta)
- HP:0000407 (Sensorineural hearing impairment)
- HP:0004322 (Short stature)
- HP:0001382 (Joint hypermobility)
- HP:0000926 (Platyspondyly)

**Key GO terms (Biological Process):**
- GO:0030199 (Collagen fibril organization)
- GO:0018208 (Peptidyl-proline modification)
- GO:0032964 (Collagen biosynthetic process)
- GO:0006457 (Protein folding)

**Key CL terms:**
- CL:0000062 (Osteoblast)
- CL:0000057 (Fibroblast)
- CL:0000138 (Chondrocyte)

---

Sources:
- [PPIB Mutations Cause Severe Osteogenesis Imperfecta (PMC2756556)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2756556/)
- [Severe Osteogenesis Imperfecta in Cyclophilin B–Deficient Mice (PMC2777385)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2777385/)
- [Abnormal Type I Collagen PTM and Crosslinking in Cyclophilin B KO Mouse (PMC4072593)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4072593/)
- [Osteogenesis imperfecta caused by PPIB mutation with congenital hearing loss (PMC5020983)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5020983/)
- [A Founder Pathogenic Variant of PPIB Unique to Chinese Population (PMC8511635)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8511635/)
- [Cyclophilin B control of lysine PTMs of skin type I collagen (PMC6602281)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6602281/)
- [Osteogenesis Imperfecta - StatPearls (NBK536957)](https://www.ncbi.nlm.nih.gov/books/NBK536957/)
- [OMIM #259440 — Osteogenesis Imperfecta, Type IX](https://omim.org/entry/259440)
- [NIH GTR — Osteogenesis imperfecta type 9](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1850169/)
- [Setrusumab for OI — Phase 2b ASTEROID Study (PMC11371902)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11371902/)
- [Mutations in PPIB delay procollagen chain association (HMG, PMID:21282188)](https://academic.oup.com/hmg/article/20/8/1595/810188)
- [Bisphosphonate therapy for osteogenesis imperfecta (PMC6611487)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6611487/)