---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T01:14:35.561560'
end_time: '2026-07-31T01:19:37.473907'
duration_seconds: 301.91
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Naxos disease
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
  web_search_requests: 13
  num_turns: 20
  total_cost_usd: 1.7357198
  session_id: d712849a-ae1d-5ccc-9dd4-91ca274b09e7
  stop_reason: end_turn
citation_count: 15
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Naxos disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Naxos disease** covering all of the
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

# Naxos Disease — Comprehensive Research Report

## 1. Disease Information

**Overview:** Naxos disease (Naxos syndrome; also called cardiocutaneous syndrome) is a rare, autosomal recessive disorder defined by a triad: **woolly hair**, **diffuse non-epidermolytic palmoplantar keratoderma (PPK)**, and **arrhythmogenic right ventricular cardiomyopathy (ARVC)**. It is the prototype "cardiocutaneous syndrome" and was the first ARVC subtype for which the causal gene was identified, establishing desmosomal dysfunction as a mechanism of arrhythmogenic cardiomyopathy more broadly (McKoy et al., *Lancet* 2000, PMID: 10902626). It was first clinically described by Protonotarios and colleagues in 1986 in nine patients from four families on the Greek island of Naxos ("Cardiac abnormalities in familial palmoplantar keratosis," *Br Heart J* 1986;56:321-6), from which the eponym derives.

**Key identifiers:**
- **OMIM:** #601214 (Naxos disease, NXD); gene locus *173325 (JUP, junction plakoglobin)
- **Orphanet:** ORPHA:34217
- **MONDO:** MONDO:0009782
- **MeSH/related:** indexed under "Arrhythmogenic Right Ventricular Dysplasia" and "Hair Diseases, Woolly Hair" cross-terms; GARD/GTR record C1832600
- **ICD-10:** typically coded via Q84.8 (other specified congenital malformations of integument) plus I42.8/I42.9 for the cardiomyopathy component, since no dedicated ICD-10 code exists for the syndrome as a unit
- **Related/allelic disorder:** **Carvajal syndrome** (a *DSP*/desmoplakin-mutant variant with predominant left-ventricular/dilated cardiomyopathy) is often described as "the Naxos disease variant" and grouped with it under the broader **keratoderma-with-woolly-hair** cardiocutaneous spectrum.

**Evidence base:** Almost all data derive from **aggregated disease-level resources** — case series and pedigree studies from the founder Greek-island population (Naxos, other Cyclades), plus subsequently identified families in Turkey, Israel, Saudi Arabia, India, Bangladesh, Argentina, Ecuador, and French-Canadian populations — rather than large EHR-based cohorts, reflecting its rarity. Sources: Orphanet Journal of Rare Diseases review, PMID: 16722579; JACC: Advances review 2024 (PMC11773020).

---

## 2. Etiology

**Causal factor:** Naxos disease is a **monogenic, autosomal recessive** disorder. The classic and founder mutation is a **homozygous 2-base-pair deletion (2157del2, historically also annotated as c.2037-2038delTG)** in exon 14 of **JUP** (junction plakoglobin, 17q21.2), causing a frameshift, loss of the last 56 C-terminal residues (including part of the 13th armadillo repeat), and truncation of the plakoglobin protein (McKoy et al. 2000, PMID: 10902626; gene mapped to 17q21 by Coonar et al., *Circulation* 1998, PMID: 9610534 [linkage mapping paper]).

- **Genetic risk factor:** Biallelic (homozygous, or compound heterozygous) loss-of-function *JUP* variants. Heterozygous carriers are asymptomatic (recessive), though isolated dominant *JUP* missense mutations have separately been reported to cause a milder, cardiac-only ARVC phenotype without the cutaneous features (PMID: 17924338) — an important genotype-phenotype distinction.
- **Allelic/genetically related disorder — Carvajal syndrome:** biallelic loss-of-function mutations in **DSP** (desmoplakin, 6p24.3), which binds plakoglobin at the desmosomal plaque, cause an overlapping but left-ventricle-predominant, earlier-onset dilated cardiomyopathy with the same cutaneous triad (Norgett et al. 2000, PMID: 11063735; Rampazzo et al. 2002; Protonotarios & Tsatsopoulou 2004, PMID: 15210133).
- **Founder effect:** The homozygous JUP 2157del2 mutation is a **founder mutation** traced to the Aegean island population, with carrier frequency reported up to **~5% in the Naxos population** and disease prevalence approaching **1:1000** on the island — among the highest reported prevalences for any severe recessive cardiomyopathy (Protonotarios & Tsatsopoulou, *Orphanet J Rare Dis* 2018, PMID not directly retrieved but summarized in PMC review chain; see also PMID: 16722579).
- **Consanguinity:** Historically relevant given the isolated island population structure; non-Greek cases (Turkey, Saudi Arabia, India, Israel) similarly often arise in consanguineous or genetically isolated communities. A separate Arab family was shown to have Naxos-like disease **not** due to the Pk2157del2 mutation, indicating locus heterogeneity even within apparently classic phenotypes (PMID: 15494820).
- **Environmental/modifying factors:** Not causal, but **physical exertion/endurance exercise** is a well-documented **disease-modifying and arrhythmia-triggering** factor — it accelerates myocyte detachment under mechanical stress, worsens right ventricular remodeling, and increases risk of ventricular arrhythmia and sudden death (supported mechanistically in murine *Jup*+/− models, where swim training accelerated RV dilation — PMID: 32670084 review). This mirrors general ARVC genotype-agnostic exercise risk data.
- **Protective factors:** No genetic or environmental protective factors are established. There is no known modifier allele that attenuates penetrance — cardiac penetrance approaches 100% by adulthood in *JUP*-homozygous individuals.
- **Gene-environment interaction:** Mechanical/hemodynamic stress (exercise) interacting with a structurally weakened desmosome-intermediate filament network is the central G×E paradigm: the disrupted cell-adhesion complex cannot withstand repetitive shear stress in the thin-walled right ventricle, precipitating myocyte death, inflammation and fibrofatty replacement preferentially in mechanically stressed regions.

---

## 3. Phenotypes

The triad has a characteristic **temporal sequence** — cutaneous/hair features present from birth/infancy, cardiac disease emerges later — which is itself diagnostically important.

| Phenotype | Type | Onset | Course | Frequency | Suggested HPO term |
|---|---|---|---|---|---|
| Woolly hair | Physical/ectodermal sign | Birth (present at birth, sometimes worsens in the first year) | Stable/lifelong | Essentially 100% (defining feature) | HP:0002415 (Woolly hair) |
| Palmoplantar keratoderma (diffuse, non-epidermolytic) | Physical/dermatologic sign | Infancy — appears within the first year of life, as hands/feet begin bearing mechanical load | Progressive/stable, may worsen with friction | ~100% | HP:0000982 (Palmoplantar keratoderma); consider HP:0007542 (diffuse palmoplantar keratoderma) |
| Arrhythmogenic right ventricular cardiomyopathy | Structural/functional cardiac sign | Adolescence/young adulthood (concealed ECG changes may predate symptoms; overt disease usually by teens–20s) | Progressive through concealed → overt-arrhythmic → heart-failure phases | ~100% penetrance by adulthood | HP:0004269 (Arrhythmogenic right ventricular cardiomyopathy) |
| Palpitations / syncope | Symptom | Adolescence onward | Episodic, may be first presentation | Common (majority of symptomatic patients) | HP:0001279 (Syncope); HP:0001962 (Palpitations) |
| Sustained ventricular tachycardia (typically LBBB morphology) | Clinical sign/arrhythmia | Adolescence/adulthood | Recurrent/episodic; risk increases with disease stage | Frequent | HP:0004756 (Ventricular tachycardia) |
| Sudden cardiac death | Outcome | Any age post-onset, including as first manifestation | N/A | Reported annual SCD mortality ~2.3% (see Prognosis) | HP:0001645 (relates to Sudden cardiac death conceptually via arrhythmia terms) |
| Right ventricular dilation / dysfunction on echo/MRI | Structural imaging finding | Progresses over the second-third decade | Progressive; may extend to biventricular involvement in >50% over 10-year follow-up | Common in overt phase | HP:0011675 (Arrhythmia) / structural terms per imaging criteria |
| Fibrofatty myocardial replacement (histology) | Laboratory/pathology finding | Progressive with disease stage | Progressive | Characteristic finding at biopsy/autopsy | — |
| Right (and later biventricular) heart failure | Symptom/sign | End-stage disease | Progressive | Subset of patients, more common/earlier in Carvajal variant | HP:0001635 (Congestive heart failure) |

**Quality of life impact:** The dermatologic features (woolly hair texture, thickened/fissured palmoplantar skin) can cause cosmetic distress and mechanical discomfort (fissuring, pain on ambulation) from infancy, while the cardiac disease drives the major morbidity/mortality burden — activity restriction, ICD-related psychological impact, risk of sudden death, and progression to heart failure/transplantation in advanced cases. No disease-specific validated QoL instrument was identified in the literature searched; ARVC-general QoL data (activity limitation, ICD shock anxiety) are presumed to apply.

---

## 4. Genetic/Molecular Information

**Causal gene:** ***JUP*** (Junction Plakoglobin, also known as γ-catenin), HGNC:6207, chromosome **17q21.2**, OMIM *173325. Encodes **plakoglobin**, a member of the armadillo-repeat protein family shared between **desmosomes** and **adherens junctions**.

- **Founder pathogenic variant:** homozygous **2-bp deletion, 2157del2 (legacy nomenclature)**, historically also cited as c.2036-2037delTG / c.2037-2038delTG depending on transcript numbering — causes a **frameshift and premature stop codon**, truncating the C-terminal 56 amino acids of the 13th armadillo repeat domain (McKoy 2000, PMID: 10902626). This is a clear **loss-of-function** allele (confirmed functionally in knock-in mouse models via nonsense-mediated decay rescue experiments — PMC7327121 review).
- **Variant classification:** Pathogenic per ClinVar/ACMG (frameshift, null variant in a gene where LOF is an established disease mechanism, segregates with recessive phenotype in multiple families, absent/extremely rare in population databases such as gnomAD given founder-population enrichment only).
- **Locus heterogeneity:** A separate Arab-family case of clinically classic Naxos disease was shown **not** to be caused by the 2157del2 mutation and JUP was formally excluded by linkage, indicating **genetic heterogeneity** — additional causal loci exist for the same phenotype (PMID: 15494820).
- **Allelic dominant variant:** A distinct **dominant** JUP missense mutation causes non-syndromic ARVC (cardiac-only, no cutaneous phenotype) — illustrating that zygosity/variant type, not just gene identity, determines phenotype severity and tissue distribution (PMID: 17924338).
- **Related gene (Carvajal syndrome):** ***DSP*** (Desmoplakin), HGNC:3052, 6p24.3, OMIM *125647. Biallelic DSP truncating variants (e.g., a variant disrupting the intermediate-filament-binding domain, reported in Ecuadorian families) cause the DSP-associated cardiocutaneous variant with predominant/early left-ventricular dilated cardiomyopathy (Norgett 2000 PMID: 11063735; Carvajal-variant genotype-outcome study PMC11924745).
- **Functional consequence:** Loss (or severe truncation) of plakoglobin protein disrupts **desmosomal plaque assembly**, weakening cell-cell adhesion at intercalated discs (heart) and at keratinocyte desmosomes (skin/hair follicle). Because plakoglobin is a dual adherens-junction/desmosome and Wnt-signaling component, its loss also **de-represses nuclear signaling** (see Mechanism, below).
- **Population frequency:** Homozygotes are essentially confined to founder-effect populations (Naxos and other Aegean islands); the pathogenic allele is at very low frequency genome-wide (not a common gnomAD variant) but locally enriched (~5% Naxos carrier frequency).
- **Somatic vs. germline:** Purely germline (constitutional) — no somatic mosaicism or oncologic relevance reported.
- **Epigenetics:** No disease-specific DNA methylation/histone-modification studies were identified specific to Naxos disease; broader ARVC epigenomic studies are limited and non-specific to JUP.
- **Chromosomal abnormalities:** None — Naxos disease is a single-gene, small-indel disorder, not a copy-number/structural chromosomal disease.
- **Modifier genes:** None formally established for Naxos disease specifically; in the broader ARVC/desmosomal-cardiomyopathy literature, digenic/oligogenic modifier effects (e.g., additional desmosomal gene variants) are increasingly recognized as influencing severity, but this is not yet mapped for JUP-Naxos cohorts specifically.

**Suggested ontology terms:** Gene — `hgnc:6207` (JUP); protein — UniProt P14923 (plakoglobin/γ-catenin); GO molecular function `GO:0005198` (structural molecule activity) / `GO:0045296` (cadherin binding); GO cellular component `GO:0030057` (desmosome), `GO:0005913` (cell-cell adherens junction), `GO:0014704` (intercalated disc).

---

## 5. Environmental Information

Naxos disease is fundamentally a monogenic disorder, so classic "environmental etiology" does not apply to causation. Environmental factors instead act as **disease modifiers/triggers**:

- **Physical exertion:** The single best-documented environmental modifier. Endurance/competitive exercise increases mechanical stress on a desmosomally weakened right ventricle, accelerating myocyte loss, fibrofatty replacement, and arrhythmic risk — consistent with general ARVC exercise-restriction guidance and with murine swim-training data in *Jup+/−* mice (PMC7327121).
- **Occupational/mechanical friction:** Repetitive mechanical stress on palms/soles (e.g., barefoot walking, manual labor from childhood) is proposed to explain the site-specific severity and appearance timing of the keratoderma (emerging as infants begin weight-bearing/grasping), paralleling the "mechanical stress unmasks weak adhesion" theme seen in the heart.
- **Toxins/pollutants:** No specific toxin, chemical, or occupational exposure has been implicated.
- **Lifestyle factors:** Beyond exercise, no diet, smoking, or alcohol associations are documented specific to Naxos disease; standard cardiovascular risk-factor management is presumably still relevant for concurrent cardiovascular health but is not disease-modifying in a specific mechanistic sense.
- **Infectious agents:** None implicated in Naxos disease etiology. (Myocardial **inflammation/myocarditis-like infiltrates** are part of the downstream pathophysiology — see Mechanism — but this is sterile/mechanically triggered inflammation, not an infectious trigger.)

---

## 6. Mechanism / Pathophysiology

**Causal chain (trigger → clinical manifestation):**

1. **Molecular lesion:** Homozygous *JUP* frameshift/truncation → loss of functional, full-length plakoglobin protein (or severely truncated, non-functional protein) (PMID: 10902626).
2. **Desmosomal/adherens-junction assembly failure:** Plakoglobin is a core structural linker of the desmosomal plaque (binding desmosomal cadherins — desmoglein/desmocollin — to intermediate filaments via desmoplakin) and of adherens junctions (binding classical cadherins to the actin cytoskeleton). Its loss destabilizes **intercalated discs** in cardiomyocytes and **desmosomes** in epidermal keratinocytes/hair follicle keratinocytes.
3. **Mechanical failure under stress:** Because desmosomes and adherens junctions provide the mechanical "glue" resisting shear stress, the weakened junctional complex fails preferentially under repetitive mechanical load — the thin-walled, high-wall-stress right ventricle in the heart, and the friction-exposed palms/soles and hair shaft in the skin. This produces **progressive myocyte detachment, cell death, and myocardial atrophy**, replaced by **fibrofatty tissue** (the histologic hallmark of ARVC).
4. **Electrical remodeling / arrhythmogenesis:** Structural intercalated-disc disruption is accompanied by **mislocalization/downregulation of connexin-43 gap junctions**, slowing and heterogenizing electrical conduction; the fibrofatty replacement itself creates anatomic re-entry substrate. Together these generate **ventricular tachyarrhythmia** (typically LBBB-morphology VT arising from right ventricular substrate) and risk of sudden cardiac death.
5. **Signaling dysregulation (Wnt/GSK3β axis):** Plakoglobin is a paralog of β-catenin and, when displaced from the desmosome, can **translocate to the nucleus**, competing with β-catenin and **suppressing canonical Wnt/β-catenin signaling**. This shift is mechanistically linked to **adipogenic transdifferentiation** of cardiac progenitor/myocardial cells, contributing to the fibrofatty phenotype. **Glycogen synthase kinase-3β (GSK3β)** was identified as a **central convergent node**: in two independent murine desmosomal-mutant models (plakoglobin-Naxos-mutant transgenic mice and Dsg2 knock-in mice), pharmacologic **GSK3β inhibition rescued myocyte injury, fibrosis, inflammation, and arrhythmia**, while constitutive GSK3β activation worsened disease — establishing GSK3β as a druggable convergence point downstream of desmosomal loss (Chelko, Asimaki, Judge et al., *JCI Insight* 2016, PMID: 27170944). This has since progressed to an active clinical trial of GSK3 inhibition for arrhythmogenic cardiomyopathy (ClinicalTrials.gov NCT06174220).
6. **Inflammatory amplification:** Myocyte injury triggers sterile inflammatory infiltration (macrophage/lymphocytic), which further injures myocardium and promotes fibrosis — a "hit-and-run" myocarditis-like component increasingly recognized in desmosomal ARVC pathogenesis (related mechanistic work: CCR2+ macrophage-driven injury in murine ACM models).
7. **Skin/hair phenotype mechanism:** The same desmosomal weakening in the epidermis and hair-follicle keratinocytes underlies the **non-epidermolytic palmoplantar keratoderma** (compensatory hyperkeratosis in response to chronic mechanical/adhesive stress) and **woolly hair** (structurally abnormal hair shaft formation due to follicular desmosome dysfunction).

**Cell types involved:** cardiomyocytes (`CL:0000746`), cardiac fibroblasts (`CL:0000057`) and myofibroblasts, epicardial/subepicardial adipocytes (`CL:0000136`), infiltrating macrophages (`CL:0000235`), epidermal keratinocytes (`CL:0000312`), hair follicle keratinocytes/trichocytes.

**Suggested GO terms:** `GO:0030057` (desmosome), `GO:0005911` (cell-cell junction), `GO:0016055` (Wnt signaling pathway), `GO:0060071` (Wnt-Frizzled-LRP5/6 complex-related regulation), `GO:0007507` (heart development), `GO:0055010` (ventricular cardiac muscle tissue morphogenesis), `GO:0070268` (cornification, for the keratoderma arm), `GO:0042733` (embryonic digit morphogenesis — n/a), `GO:0006915` (apoptotic process, for myocyte death).

**Suggested UBERON/anatomical terms:** `UBERON:0002080` (heart right ventricle), `UBERON:0014704`-type intercalated disc terms if modeled, `UBERON:0001003` (skin epidermis), `UBERON:0002073` (palm skin) / sole skin, `UBERON:0002073`, hair follicle `UBERON:0002073`-adjacent structures.

**Fit to dismech mechanism-module framework:** This disorder is a strong candidate conformer to relevant dismech mechanism modules — notably **`cardiomyopathy_maladaptive_remodeling`** (structural/contractile arm) and **`cardiac_ion_channel_repolarization`**/arrhythmogenic-substrate concepts for the ventricular tachyarrhythmia arm, plus potentially a bespoke desmosomal cell-adhesion node given its status as the founding cause of the broader arrhythmogenic-cardiomyopathy disease class.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Heart — predominantly **right ventricle** (classic Naxos/JUP disease); **skin** (palms and soles); **hair/hair follicles** (scalp).
- **Secondary/complication-driven:** Left ventricle (in advanced/biventricular disease and especially in the DSP-Carvajal variant), systemic venous system/liver (right heart failure congestion in end-stage disease).
- **Body systems:** Cardiovascular system (primary), integumentary system (primary), and secondarily the conduction system (arrhythmia).

**Tissue/cell level:**
- Cardiac muscle tissue — ventricular myocardium, intercalated discs, subepicardial/epicardial adipose and fibrous tissue (fibrofatty replacement).
- Epidermis — stratum corneum thickening (keratoderma); hair shaft/follicle keratinocytes (woolly hair).
- Cell populations: cardiomyocytes, cardiac fibroblasts/myofibroblasts, adipocytes, macrophages/lymphocytes (inflammatory infiltrate), keratinocytes.

**Subcellular level:**
- Desmosomes and adherens junctions at the **intercalated disc** (`GO:0014704`) and at keratinocyte cell-cell borders (`GO:0030057`, `GO:0005913`).
- Gap junctions (connexin-43, `GO:0005921`) — secondarily mislocalized.
- Nucleus — site of aberrant plakoglobin translocation and Wnt-pathway interference.

**Localization/laterality:** Right ventricle is classically and preferentially affected early (bilateral/global cutaneous involvement of palms and soles; scalp hair diffusely woolly, not focal). Cardiac disease frequently progresses to **biventricular** involvement over the disease course (>50% by 10-year follow-up per Protonotarios/Tsatsopoulou natural-history data, PMID: 16722579); the DSP-Carvajal variant is distinguished by predominant/early **left ventricular** involvement.

---

## 8. Temporal Development

- **Onset:** Cutaneous features (woolly hair) are present **at or shortly after birth**; palmoplantar keratoderma emerges in the **first year of life** as the hands/feet begin bearing mechanical/functional load. Cardiac disease is **occult in childhood** (concealed ECG-only abnormalities may be detectable), becoming clinically **overt in adolescence to young adulthood**, with roughly one-third of patients symptomatic before age 30.
- **Onset pattern:** Cutaneous features — congenital/insidious. Cardiac disease — insidious progression through a concealed phase, punctuated by acute arrhythmic events (syncope, VT, or sudden death as first presentation in some patients).
- **Disease stages (classic three-phase ARVC natural history model, directly documented for Naxos disease):**
  1. **Concealed phase:** subtle ECG repolarization/depolarization abnormalities (e.g., T-wave inversion in right precordial leads, epsilon waves), minimal or no structural changes, patient largely asymptomatic; sudden death can rarely occur even in this phase during exertion.
  2. **Overt/arrhythmic phase:** symptomatic ventricular arrhythmias (typically LBBB-morphology sustained VT), syncope, palpitations; progressive right (and often biventricular) structural/functional deterioration.
  3. **Heart failure/end-stage phase:** right (or biventricular) pump failure, congestive symptoms, potential need for transplantation.
- **Progression rate:** Variable but generally **progressive** over years to decades; biventricular extension in >50% of patients over 10 years of follow-up (PMID: 16722579). The Carvajal/DSP variant progresses **faster and earlier**, with heart failure in ~50% of patients and death frequently in childhood/adolescence.
- **Course pattern:** Progressive structural disease with a superimposed **episodic arrhythmic** component (VT episodes are paroxysmal against a background of progressive myocardial replacement).
- **Duration:** Chronic, lifelong — no spontaneous remission of the underlying structural disease; arrhythmic episodes may remit/recur unpredictably. Disease-modifying therapy does not reverse fibrofatty replacement.
- **Critical periods:** Adolescence and young adulthood represent the critical window during which concealed disease becomes overt and sudden death risk sharply rises — this is the rationale for cardiac screening beginning in the pre-teen/teen years in known *JUP*-homozygous family members, and for exercise-restriction counseling initiated as early as possible once genotype/phenotype risk is established.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence:** Estimated **~1:1000** on the island of Naxos and neighboring Aegean islands — an extraordinarily high prevalence for a lethal recessive cardiomyopathy, attributable to founder effect and historical geographic/reproductive isolation.
- **Carrier frequency:** Up to **~5%** heterozygous carriers in the Naxos population.
- **Global rarity:** Outside the founder population, Naxos disease is extremely rare, with case reports/small series from Turkey, Israel, Saudi Arabia, India, Bangladesh, Argentina, Ecuador (Carvajal variant), and French-Canadian kindreds.

**Inheritance pattern:** **Autosomal recessive.** Both parents of an affected individual are obligate heterozygous carriers (typically asymptomatic).

**Penetrance:** Cardiac phenotype shows **very high (~100%) penetrance** by adulthood in homozygotes, though the *timing* of overt cardiac manifestation is variable (concealed-phase duration differs between individuals). Cutaneous features are essentially fully penetrant from infancy.

**Expressivity:** Variable in cardiac disease severity/progression rate and in age at first arrhythmic event, even among relatives sharing the identical homozygous genotype — implying modifier effects (genetic and/or environmental, especially exercise exposure) not yet fully characterized.

**Genetic anticipation:** Not reported/expected — this is a small-indel loss-of-function disorder, not a repeat-expansion disease.

**Germline mosaicism:** Not specifically documented for JUP-Naxos disease in the literature reviewed.

**Founder effect:** Well-established — the 2157del2 JUP mutation is the paradigmatic founder mutation for the Aegean/Naxos population; a distinct, non-JUP cause was documented in an unrelated Arab family with a phenocopy (PMID: 15494820), underscoring that "Naxos disease" is a clinical/phenotypic diagnosis with genetic heterogeneity, while "JUP-related Naxos disease" is the genetically defined founder-mutation entity.

**Consanguinity:** Plausibly relevant historically in the isolated island population and in reported non-Greek kindreds, though formal consanguinity rates were not quantified in the sources reviewed.

**Population demographics:**
- **Geographic distribution:** Endemic focus on Naxos and other Cyclades/Aegean islands (Greece); sporadic kindreds reported in Turkey, Israel, Saudi Arabia, India, Bangladesh, Argentina, Ecuador, and French-Canadian populations.
- **Sex ratio:** No strong sex predilection is reported for an autosomal recessive disorder; ARVC generally (non-Naxos) shows some male predominance in symptomatic presentation, but Naxos-specific sex-ratio data were not identified in this search.
- **Age distribution:** Skin findings from birth/infancy; cardiac diagnosis clusters in adolescence/young adulthood, consistent with the concealed-to-overt phase transition.

---

## 10. Diagnostics

**Clinical recognition:** The **triad** (woolly hair + PPK + ARVC) in a patient (especially from an endemic population) is highly suggestive and typically prompts genetic confirmation.

**Clinical/cardiac tests:**
- **ECG:** T-wave inversion in right precordial leads (V1–V3), epsilon waves, prolonged QRS/terminal activation duration, and ventricular arrhythmia of **left bundle branch block (LBBB) morphology** (indicating right ventricular origin).
- **Echocardiography:** Right ventricular dilation, regional wall-motion abnormality/akinesia/dyskinesia, reduced RV ejection fraction; may progress to involve the left ventricle.
- **Cardiac MRI:** Assessment of RV (and LV) structure/function, wall-motion abnormalities, and myocardial fibrofatty infiltration (late gadolinium enhancement) — a cornerstone modality per the 2010/2023 Task Force imaging criteria.
- **Signal-averaged ECG (SAECG):** Detects late potentials reflecting delayed, fragmented conduction.
- **Ambulatory/Holter monitoring and exercise testing:** To detect ventricular ectopy/VT burden, often exercise-induced.
- **Electrophysiology study:** For arrhythmia characterization and risk stratification in selected patients.
- **Endomyocardial biopsy / histopathology (when performed, or at autopsy):** Fibrofatty replacement of right ventricular myocardium, myocyte loss — the classic pathologic hallmark; **reduced/altered immunohistochemical signal for plakoglobin** at the intercalated disc has been proposed as a relatively specific diagnostic biomarker for desmosomal ARVC (Asimaki et al. immunohistochemistry work, broader ARVC literature).
- **Diagnostic framework:** The disease is diagnosed under the general **ARVC Task Force Criteria** (originally 1994, revised **2010** International Task Force Criteria, further refined by the **2023 European Task Force Criteria for Arrhythmogenic Cardiomyopathy**), combining major/minor criteria across structural imaging, tissue characterization, repolarization abnormalities, depolarization/conduction abnormalities, arrhythmias, and family history/genetics — with a **positive family history of a confirmed pathogenic desmosomal variant, or presence of the cutaneous phenotype**, constituting a major criterion category. In Naxos disease specifically, the presence of the pathognomonic skin/hair phenotype is itself considered strong diagnostic support even before cardiac criteria are fully met.

**Genetic testing:**
- **Recommended approach:** Targeted **single-gene sequencing of *JUP*** (particularly for the 2157del2 founder variant in patients from/with ancestry linked to endemic regions), or inclusion of *JUP* and *DSP* within an **ARVC/cardiomyopathy gene panel** (alongside PKP2, DSG2, DSC2, TMEM43, RYR2, LMNA, etc., for differential diagnosis of non-syndromic ARVC and other overlapping cardiomyopathies).
- **Whole-exome/whole-genome sequencing:** Useful when panel testing is non-diagnostic, or in atypical/non-founder-population presentations (as demonstrated by the *JUP*-negative Arab-family case, PMID: 15494820), to identify novel/alternative loci.
- **Family cascade testing:** Critical given autosomal recessive inheritance — testing sibs of an affected proband, and carrier testing of relatives in endemic populations, is a key secondary-prevention/counseling tool.
- **Prenatal/preimplantation testing:** Feasible once a family's causal variant is known, though this was not specifically discussed in the sources reviewed.

**Differential diagnosis:** Non-syndromic ARVC (PKP2, DSG2, DSC2, TMEM43-related), **Carvajal syndrome** (DSP-related, LV-predominant), other ectodermal dysplasias/keratoderma syndromes with cardiac involvement (e.g., **Bass syndrome**, cardiofaciocutaneous overlap conditions), and other causes of woolly hair (e.g., isolated hereditary woolly hair, Noonan-syndrome-associated woolly hair).

**Screening:** Given the founder-mutation, high-prevalence context, **targeted carrier/genetic screening in the Naxos/endemic population**, and **cardiac screening (ECG/echo) of homozygous or at-risk family members beginning in childhood/pre-adolescence** are recommended surveillance strategies, given the high cardiac penetrance and sudden-death risk once the concealed phase transitions to overt disease.

---

## 11. Outcome/Prognosis

- **Mortality:** From the seminal natural-history literature (Protonotarios/Tsatsopoulou cohort, summarized PMID: 16722579): **annual disease-related mortality ~3%**, with **annual sudden cardiac death mortality ~2.3%** — figures that place Naxos disease among the more malignant arrhythmogenic cardiomyopathies.
- **Sudden death as first presentation:** Documented — sudden cardiac death can be the **initial clinical manifestation** of previously "concealed"-phase disease, particularly in the context of exertion, underscoring the importance of pre-symptomatic screening in known carriers/homozygotes.
- **Risk stratification factors:** History of syncope, symptomatic arrhythmia, severe/extensive right ventricular disease developing before age 35, and **left ventricular involvement** are identified as adverse prognostic markers (PMID: 16722579).
- **Disease course/complications:** Progressive biventricular structural involvement occurs in **>50% of patients over a 10-year follow-up**; end-stage right (or biventricular) heart failure can necessitate heart transplantation.
- **Carvajal (DSP) variant prognosis:** Notably worse and earlier — approximately **50% develop heart failure**, with death commonly occurring in **childhood or adolescence**, reflecting the more aggressive, left-ventricle-predominant dilated-cardiomyopathy phenotype of this allelic variant (genotype-outcome study, PMC11924745).
- **Functional/QoL outcomes:** Beyond mortality, morbidity includes activity restriction, psychological burden of living with ICD/sudden-death risk, and the chronic dermatologic discomfort of PPK (fissuring, pain), though dedicated disease-specific QoL instrument data were not identified.
- **Prognostic biomarkers:** No blood-based prognostic biomarker specific to Naxos disease was identified; risk stratification remains primarily clinical/imaging/electrophysiological, as in ARVC generally.

---

## 12. Treatment

There is **no curative or disease-modifying therapy** that reverses desmosomal dysfunction or established fibrofatty replacement in Naxos disease; management is centered on **arrhythmia/sudden-death prevention** and **heart-failure supportive care**, with emerging **mechanism-targeted** investigational approaches.

**Pharmacotherapy (arrhythmia management):**
- **Antiarrhythmic drugs — sotalol and amiodarone**, alone or combined with **β-blockers**, used for suppression of sustained ventricular tachycardia (PMID: 16722579). Suggested MAXO term: `MAXO:0000647`-adjacent pharmacotherapy action, more precisely treatment_term `NCIT:C15986` (Pharmacotherapy) with therapeutic_agent CHEBI entries for sotalol/amiodarone.
- **β-blockers:** Standard adjunct for arrhythmia suppression and heart-failure management.
- **Heart-failure pharmacotherapy:** **Diuretics** and **ACE inhibitors** for right (or biventricular) heart failure symptoms in advanced disease (PMID: 16722579); by extension, standard contemporary guideline-directed medical therapy (including possibly ARBs/mineralocorticoid antagonists) would be applied, though Naxos-specific trial data are lacking.

**Device therapy (primary/secondary prevention of sudden death):**
- **Implantable cardioverter-defibrillator (ICD):** The cornerstone of sudden-death prevention — recommended for **primary prevention** in symptomatic patients or those with significant structural disease progression, generally before age 35 in the Naxos cohort data reviewed (PMID: 16722579), and for **secondary prevention** after aborted cardiac arrest or sustained VT, consistent with general ARVC ICD guidelines (e.g., PMID: 30678832 on primary-prevention ICD outcomes in ARVC). Suggested MAXO term: relates to `MAXO:0000004`-adjacent device implantation procedures (device/surgical action); therapeutic_modality `DEVICE`.
- **Catheter ablation (endocardial/epicardial, electroanatomic mapping-guided):** Used for control of recurrent VT refractory to antiarrhythmic drugs, reducing arrhythmic burden and ICD shocks, though it does not eliminate sudden-death risk and is typically adjunctive to ICD therapy.

**Surgical/advanced:**
- **Heart transplantation:** Reserved for end-stage refractory heart failure (right- or biventricular) (PMID: 16722579); relevant MAXO term `MAXO:0010039` (organ transplantation).

**Behavioral/lifestyle:**
- **Exercise restriction:** A central, non-pharmacologic recommendation — avoidance of competitive/endurance exercise to reduce mechanical stress on the desmosomally weakened myocardium and lower arrhythmic/progression risk, extrapolated from general ARVC guidance and supported mechanistically by exercise-accelerated disease in *Jup+/−* mouse models. Relevant MAXO term: behavioral counseling `MAXO:0000077`.
- **Dermatologic supportive care:** Emollients, keratolytics, and mechanical offloading for palmoplantar keratoderma; standard dermatologic management, not curative.

**Genetic counseling:** Given autosomal recessive inheritance, family/genetic counseling for at-risk relatives and reproductive planning is an important component of comprehensive care (`MAXO:0000079`).

**Experimental/targeted therapy:**
- **GSK3β inhibition** — mechanistically supported by murine model data (Chelko/Judge, PMID: 27170944) as a pathway-targeted approach to arrhythmogenic (desmosomal) cardiomyopathy broadly (not JUP-Naxos-specific in isolation but directly relevant given the shared mechanism). This has progressed to an active human trial: **"Targeted Therapy With Glycogen Synthase Kinase-3 Inhibition for Arrhythmogenic Cardiomyopathy"** (ClinicalTrials.gov **NCT06174220**), representing the most disease-mechanism-proximal experimental therapeutic under active clinical investigation for this disease class.
- No gene therapy, gene editing, RNA-based (ASO/siRNA), or cell-therapy approach specific to JUP-Naxos disease was identified as being in active clinical development in the sources reviewed, though desmosomal-gene replacement/correction strategies are an area of broader preclinical ARVC research interest.

**Treatment algorithm summary:** Risk-stratify (syncope/VT history, RV/LV extent of disease, age) → ICD for primary/secondary prevention in higher-risk patients → antiarrhythmics (sotalol/amiodarone ± β-blocker) for arrhythmia suppression and ICD-shock reduction → ablation for refractory VT → heart-failure GDMT as ventricular function declines → transplantation for end-stage disease → lifelong exercise restriction and family cascade screening/counseling throughout.

---

## 13. Prevention

- **Primary prevention:** Not possible in the genetic sense (cannot prevent inheritance of a homozygous recessive genotype), but **exercise restriction** in genotype-positive/at-risk individuals functions as a primary preventive measure against triggering or accelerating cardiac disease expression and arrhythmic events.
- **Secondary prevention (early detection):** **Cardiac screening (ECG, echocardiography, and where available cardiac MRI)** of relatives of an affected proband — particularly siblings and other homozygous or genetically confirmed at-risk family members — beginning in childhood/early adolescence, to detect the transition from concealed to overt disease before a sudden-death event occurs. Population-level carrier/genetic screening is of particular relevance in the endemic Naxos/Aegean population given the high (~5%) carrier frequency.
- **Tertiary prevention:** ICD implantation, antiarrhythmic therapy, and heart-failure management (as above) to prevent sudden death and slow functional decline once disease is established.
- **Genetic counseling:** For carrier couples (both from endemic or consanguineous backgrounds) regarding recurrence risk (25% for offspring of two carriers), and for confirmed homozygous individuals regarding their own risk and that of their children (obligate carriers, or affected if partner is also a carrier).
- **Immunization:** Not applicable (non-infectious disease).
- **Public health:** No organized public-health screening program specific to Naxos disease was identified in this search; management is family/genetic-counseling based rather than population-wide.
- **Prophylaxis:** No pharmacologic prophylaxis is established to prevent onset of the cardiac phenotype in genotype-positive individuals; management is surveillance- and arrhythmia-prevention—based once disease is diagnosed or strongly anticipated.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring veterinary/companion-animal analog of Naxos disease (JUP-associated cardiocutaneous syndrome) was identified in this search — unlike some other Mendelian disorders, this does not appear to have a well-characterized spontaneous animal counterpart in OMIA-type registries based on the sources reviewed.
- **Orthologous gene:** *Jup* is highly conserved; mouse *Jup* (NCBI Gene, chr11 in mouse) and other vertebrate orthologs are used extensively in laboratory models (see Section 15) rather than representing naturally occurring disease.
- **Comparative biology:** The desmosome/plakoglobin structural and Wnt-signaling roles are deeply conserved across vertebrates, which underlies the strong translational relevance of the mouse and zebrafish models described below, despite the absence of documented natural veterinary disease.
- **Zoonotic potential/transmission:** Not applicable — purely genetic, non-transmissible disease.

---

## 15. Model Organisms

**Mouse models** (most extensively characterized; summarized in the 2020 review "Genetic Animal Models for Arrhythmogenic Cardiomyopathy," PMID: 32670084):
- **Global *Jup* knockout:** Complete *Jup* deficiency is **embryonic lethal**, with severe cardiac defects and markedly reduced cardiac desmosomes (classic Kemler/Birchmeier-era developmental studies, 1996), demonstrating an essential developmental role for plakoglobin beyond the postnatal disease phenotype.
- **Heterozygous global *Jup* knockout (*Jup+/−*):** Develop **right ventricular dilation, ventricular arrhythmia, and decreased RV function** without gross structural malformation; disease is **exercise-inducible/accelerated** — 8 weeks of swim training produced increased RV dilation evident by 6 months, directly modeling the human exercise-as-modifier phenomenon (Kirchhof et al., referenced in PMC7327121).
- **Cardiac-specific / inducible cardiac-specific plakoglobin-deficient mice:** Exhibit severe cardiac fibrosis, contractile dysfunction, ventricular arrhythmia, and dilation, supporting a **loss-of-function** disease mechanism localized to the heart.
- **Cardiac-specific transgenic overexpression** of mutant (Naxos-type truncated) or even wild-type plakoglobin (Myh6 promoter): causes **increased mortality**, indicating that excess/dysregulated plakoglobin expression is independently toxic — informative for understanding dosage sensitivity.
- ***Jup*-c.2037-2038del knock-in mice** (Chen lab): precisely models the human founder mutation. Straight knock-in mice die shortly after birth due to **nonsense-mediated mRNA decay (NMD)** of the mutant transcript; when introns 10–14 were deleted to block NMD and rescue truncated-protein expression, mice were protected from the ACM phenotype — strong genetic proof that **loss of truncated protein expression (via NMD), not merely haploinsufficiency**, underlies severity, and that restoring even truncated protein is protective — an important mechanistic and potential therapeutic-strategy insight (e.g., for NMD-modulating or exon-skipping-type approaches).
- **Two-model convergence study (Chelko/Judge, JCI Insight, PMID: 27170944):** Combined a transgenic plakoglobin-Naxos-mutant model and a *Dsg2* knock-in model, showing shared structural, histopathological, and arrhythmic phenotypes, and demonstrating that **GSK3β inhibition (SB216763)** rescues myocyte injury, fibrosis/inflammation, and ventricular ectopy across both models — directly nominating GSK3β as a convergent, druggable node and providing the preclinical basis for the ongoing human GSK3-inhibitor trial (NCT06174220).

**Zebrafish models:**
- **Morpholino *jup* knockdown:** Produces cardiac edema, decreased heart size, and blood reflux between chambers, with altered desmosomal ultrastructure — useful for rapid, scalable developmental/structural phenotyping, though the two-chambered, regenerative zebrafish heart limits modeling of RV-specific adult disease.

**Model recapitulation and limitations:**
- **Recapitulated:** ventricular arrhythmia, RV (and with cardiac-specific loss, more global) dilation and dysfunction, fibrosis, intercalated-disc/connexin-43 mislocalization, exercise-induced disease acceleration.
- **Not recapitulated:** **Fibro-fatty (adipocytic) replacement** — the histologic hallmark of human ARVC/Naxos disease — is **not reproduced** in mouse or zebrafish models, a major translational gap. Mice frequently require **homozygous/biallelic** manipulation to approximate phenotypes that in some human desmosomal genes (e.g., dominant PKP2 ARVC) arise from heterozygous mutations, reflecting species differences in dosage sensitivity. The cutaneous (woolly hair/PPK) component of the human syndrome is generally not the focus of these cardiac-oriented models.
- **Applications:** These models have been central to establishing loss-of-function as the operative mechanism, identifying GSK3β/Wnt signaling as a therapeutic target, characterizing exercise as a disease accelerant, and are now supporting translational pharmacologic (GSK3 inhibitor) development.

**Resources:** MGI (Mouse Genome Informatics) for *Jup* knockout/knock-in alleles; ZFIN for zebrafish *jup* morpholino/mutant lines; IMPC/KOMP repositories for additional conditional allele resources.

---

## Summary of Key PMIDs Cited

| PMID | Citation focus |
|---|---|
| 10902626 | McKoy et al., *Lancet* 2000 — identification of JUP 2157del2 deletion as cause of Naxos disease |
| 16722579 | Protonotarios & Tsatsopoulou, *Orphanet J Rare Dis* review — epidemiology, natural history, staging, mortality, treatment |
| 15494820 | Naxos-disease phenotype in an Arab family excluded from JUP locus — genetic heterogeneity |
| 15210133 | Naxos disease and Carvajal syndrome — comparative pathogenesis review |
| 11063735 | Norgett et al. — desmoplakin (DSP) mutation causing Carvajal-variant cardiocutaneous syndrome |
| 17924338 | Dominant JUP missense mutation causing non-syndromic ARVC |
| 27170944 | Chelko, Asimaki, Judge et al., *JCI Insight* 2016 — central role of GSK3β in arrhythmogenic cardiomyopathy pathogenesis; murine desmosomal-mutant models |
| 32670084 | Review of genetic animal models for arrhythmogenic cardiomyopathy (mouse/zebrafish *Jup* models) |
| 9610534 | Original 17q21 linkage mapping of the Naxos disease locus |

**Note on evidence quality/gaps for KB curation:** Most quantitative figures (prevalence ~1:1000, carrier rate ~5%, annual mortality ~3%/SCD ~2.3%) trace back to the same core Protonotarios/Tsatsopoulou clinical cohort literature and its review syntheses; independent replication in non-Greek cohorts is limited given global rarity. The GSK3β/Wnt mechanism, while compelling and directly relevant, is derived from **desmosomal ARVC models broadly** (plakoglobin-Naxos-mutant and Dsg2 models) rather than exclusively JUP-Naxos-specific systems, and should be flagged with `evidence_source: MODEL_ORGANISM` when curated. Direct exact-quote abstract snippets should be re-verified against PubMed/PMC full text at curation time per dismech's anti-hallucination SOP before being entered as evidence items.

Sources:
- [Identification of a deletion in plakoglobin in arrhythmogenic right ventricular cardiomyopathy with palmoplantar keratoderma and woolly hair (Naxos disease) - PubMed](https://pubmed.ncbi.nlm.nih.gov/10902626/)
- [Naxos disease: Cardiocutaneous syndrome due to cell adhesion defect - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC1435994/)
- [Naxos disease in an Arab family is not caused by the Pk2157del2 mutation - PubMed](https://pubmed.ncbi.nlm.nih.gov/15494820/)
- [Naxos disease and Carvajal syndrome: cardiocutaneous disorders... - PubMed](https://pubmed.ncbi.nlm.nih.gov/15210133/)
- [Genotype and cardiac outcome in patients with cardiocutaneous syndrome (Naxos disease variant: Carvajal syndrome) - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11924745/)
- [A novel dominant mutation in plakoglobin causes arrhythmogenic right ventricular cardiomyopathy - PubMed](https://pubmed.ncbi.nlm.nih.gov/17924338/)
- [Central role for GSK3β in the pathogenesis of arrhythmogenic cardiomyopathy - PubMed](https://pubmed.ncbi.nlm.nih.gov/27170944/)
- [Genetic Animal Models for Arrhythmogenic Cardiomyopathy - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7327121/)
- [Naxos Disease and Related Cardio-Cutaneous Syndromes - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11773020/)
- [Entry - #601214 - NAXOS DISEASE; NXD - OMIM](https://omim.org/entry/601214)
- [Entry - *173325 - JUNCTION PLAKOGLOBIN; JUP - OMIM](https://omim.org/entry/173325)
- [Orphanet: Naxos disease](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=34217)
- [Naxos disease - National Organization for Rare Disorders / MONDO](https://rarediseases.org/mondo-disease/naxos-disease/)
- [Naxos Disease | GARD - NIH](https://rarediseases.info.nih.gov/diseases/9795/naxos-disease/)
- [Targeted Therapy With GSK-3 Inhibition for Arrhythmogenic Cardiomyopathy - ClinicalTrials.gov NCT06174220](https://clinicaltrials.gov/study/NCT06174220)