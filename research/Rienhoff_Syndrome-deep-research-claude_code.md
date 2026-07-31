---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-07-30T21:19:51.097776'
end_time: '2026-07-30T21:37:37.406122'
duration_seconds: 1066.31
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Rienhoff Syndrome
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
  - claude-opus-5
  web_search_requests: 16
  num_turns: 70
  total_cost_usd: 5.55554525
  session_id: 049f52f3-7f1f-488e-a849-20e2cb96e8cb
  stop_reason: end_turn
citation_count: 46
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rienhoff Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Rienhoff Syndrome** covering all of the
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

# Comprehensive Research Report: Rienhoff Syndrome (Loeys–Dietz Syndrome 5, TGFB3-Related HTAD)

**Prepared:** 30 July 2026 · **Target entity:** MONDO:0014262 · **Category:** Mendelian (autosomal dominant, TGF-β pathway aortopathy)

**Provenance conventions used below.** `[ABSTRACT-VERBATIM]` = quotation confirmed against the PubMed abstract text; `[FULL-TEXT]` = quotation from the open-access full text (PMC), i.e. **not** validatable against a PubMed abstract; `[DB-RECORD]` = quotation from a structured database record (OMIM/MONDO/Orphanet/MedGen/ClinGen); `[SECONDARY — VERIFY]` = figure obtained via a secondary summary and not yet confirmed against primary text. Curators loading this into a knowledge base should only use `[ABSTRACT-VERBATIM]` or `[DB-RECORD]` strings as evidence `snippet:` values without re-fetching.

---

## 1. Disease Information

### 1.1 Overview

Rienhoff syndrome is a rare autosomal dominant syndromic heritable thoracic aortic disease (HTAD) caused by pathogenic variants in **TGFB3**, the gene encoding the transforming growth factor β3 ligand. It sits at the mildest, latest-onset end of the Loeys–Dietz syndrome (LDS) spectrum and is designated **Loeys–Dietz syndrome 5 (LDS5)** in OMIM. The phenotype combines (a) a variably penetrant thoracic/abdominal aortic and arterial aneurysm–dissection diathesis, (b) craniofacial features shared with LDS/Marfan/Shprintzen–Goldberg syndromes (hypertelorism, cleft palate or bifid uvula, retrognathia), (c) skeletal features (scoliosis, cervical spine instability, clubfoot, arachnodactyly, pectus deformity, joint hypermobility), and (d) in the index family, a striking neuromuscular presentation of low muscle mass, growth retardation and distal arthrogryposis without any vascular disease.

The two poles of the phenotype — the neuromuscular/arthrogrypotic index case and the adult aortopathy cohorts — reflect genuine biological heterogeneity, not curatorial confusion, and both are anchored to the same gene.

**Nomenclature history.** The eponym honours **Hugh Y. Rienhoff Jr.**, a physician-geneticist who pursued the molecular diagnosis of his own daughter's undiagnosed connective-tissue/neuromuscular syndrome and is first author of the founding 2013 report ([PMID:23824657](https://pubmed.ncbi.nlm.nih.gov/23824657/)). "Rienhoff syndrome" and "Loeys–Dietz syndrome 5" are used interchangeably; GeneReviews notes that "*TGFB3*-related LDS may also be referred to as Rienhoff syndrome" `[DB-RECORD]`. The contemporary genetics/cardiology literature increasingly prefers the mechanism-neutral label **"TGFB3-related HTAD"** ([PMID:39653386](https://pubmed.ncbi.nlm.nih.gov/39653386/)).

`[DB-RECORD]` OMIM/MONDO definition (quotable verbatim; source EFO:1000012 / OMIM:615582):

> "Loeys-Dietz syndrome-5 (LDS5), also known as Rienhoff (pronounced REENhoff) syndrome, is characterized by syndromic presentation of aortic aneurysms involving the thoracic and/or abdominal aorta, with risk of dissection and rupture. Other systemic features include cleft palate, bifid uvula, mitral valve disease, skeletal overgrowth, cervical spine instability, and clubfoot deformity; however, not all clinical features occur in all patients. In contrast to other forms of LDS, no striking aortic or arterial tortuosity is present in these patients, and there is no strong evidence for early aortic dissection."

*Curation note:* the final clause of that definition is now partly superseded — arterial tortuosity was documented in 25% of the Montalcino cohort ([PMID:39653386](https://pubmed.ncbi.nlm.nih.gov/39653386/)) and tortuosity plus iliac/femoral aneurysms were the *presenting* problem in a 2025 case ([PMID:39450604](https://pubmed.ncbi.nlm.nih.gov/39450604/)). Flag as a stale ontology definition worth reporting upstream to MONDO/OMIM.

### 1.2 Identifiers

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | **MONDO:0014262** | label "Rienhoff syndrome"; `is_a` MONDO:0018954 (Loeys-Dietz syndrome) **and** MONDO:0005172 (skeletal system disorder); `RO:0004003` → HGNC:11769 (TGFB3) |
| OMIM (disease) | **615582** — LOEYS-DIETZ SYNDROME 5; LDS5 (alt: RIENHOFF SYNDROME, RNHF) | |
| OMIM (gene) | **190230** — TRANSFORMING GROWTH FACTOR, BETA-3; TGFB3 | also carries the ARVD1 allelic disorder |
| HGNC | **HGNC:11769** (TGFB3); dismech house style `hgnc:11769` | |
| UniProt | **P10600** (TGFB3_HUMAN) | 412 aa proprotein |
| DOID | DOID:0070236 | |
| EFO | EFO:1000012 | source of the MONDO definition |
| MedGen / UMLS | MedGen **816342** / UMLS **C3810012** | |
| GARD | GARD:12356 | |
| Orphanet | **No dedicated LDS5/Rienhoff code.** Subsumed under **ORPHA:60030** "Loeys-Dietz syndrome", which lists OMIM:615582 as a **Broader** cross-reference and TGFB3 (hgnc:11769) as "Disease-causing germline mutation(s) in" | ORPHA:60030 also maps ICD-10:**Q87.4** (Narrower), ICD-11:**BD50.Z** (Narrower), MeSH:**D055947**, MedDRA:10081284, GARD:10788, UMLS:C2697932 |
| ICD-10 / ICD-11 | No LDS5-specific code. Coded via the LDS umbrella: **ICD-10 Q87.4**; **ICD-11 BD50.Z** (per Orphanet mapping) | ICD-10-CM users also encounter Q87.89 |
| GTR | NIH Genetic Testing Registry condition C3810012 "Rienhoff syndrome" | |
| ClinGen | Gene-disease validity: TGFB3 ↔ familial TAAD (MONDO:0019625) = **Limited** (HTAAD GCEP, 2016-12-22); TGFB3 ↔ ARVC (MONDO:0016587) = **Limited** (ARVC GCEP, 2019-08-16, `CGGV:assertion_36ed9be9-2854-49e5-801c-a8fd65fec98e-2019-08-16T160000.000Z`). Actionability: **Strong** for Loeys-Dietz syndrome (adult + pediatric working groups, 2019-03-01). Dosage sensitivity: **0 classifications** | The "Limited" TAAD validity call is important context for the low-penetrance findings in §9 |

### 1.3 Synonyms

Rienhoff syndrome · Loeys–Dietz syndrome 5 · Loeys–Dietz syndrome type 5 · LDS5 · LDS type V · RNHF · TGFB3-related Loeys–Dietz syndrome · TGFB3-related heritable thoracic aortic disease (TGFB3-related HTAD) · (historical, index family) "syndrome of low muscle mass, growth retardation and distal arthrogryposis with Marfan/Loeys–Dietz overlap".

### 1.4 Nature of the evidence base

Essentially **all** knowledge derives from **aggregated, expert-curated case series and registries**, not from EHR-scale phenotyping. There is no population EHR cohort, no claims-based study, and no registry-derived incidence estimate. The four evidentiary pillars are:

1. **Index family case report + functional work** — n=1 proband ([PMID:23824657](https://pubmed.ncbi.nlm.nih.gov/23824657/), 2013)
2. **Gene-discovery multi-family series** — 43 patients / 11 families ([PMID:25835445](https://pubmed.ncbi.nlm.nih.gov/25835445/), 2015)
3. **Variant/mutation update** — pooled variant table ([Schepers et al. 2018, PMC5947146](https://pmc.ncbi.nlm.nih.gov/articles/PMC5947146/))
4. **Two contemporary penetrance cohorts** — Belgian founder families n=27 ([PMID:37719708](https://pubmed.ncbi.nlm.nih.gov/37719708/), 2023) and the international **Montalcino Aortic Consortium** registry n=34 ([PMID:39653386](https://pubmed.ncbi.nlm.nih.gov/39653386/), 2025)

Total published individuals with TGFB3 variants is on the order of **~110–140**, with substantial overlap between series (the 2023 paper explicitly excluded 12 individuals already counted in its own families from its 82-patient literature comparator).

---

## 2. Etiology

### 2.1 Primary causal factor

Monogenic. **Heterozygous germline TGFB3 variants** (14q24.3) are the cause in essentially all reported patients. A single **biallelic (homozygous)** case is known and is markedly more severe (§4.4).

`[ABSTRACT-VERBATIM]` ([PMID:25835445](https://pubmed.ncbi.nlm.nih.gov/25835445/)):
> "Here, we report on 43 patients from 11 families with syndromic presentations of aortic aneurysms caused by TGFB3 mutations. We demonstrate that TGFB3 mutations are associated with significant cardiovascular involvement, including thoracic/abdominal aortic aneurysm and dissection, and mitral valve disease."

`[ABSTRACT-VERBATIM]` ([PMID:23824657](https://pubmed.ncbi.nlm.nih.gov/23824657/)) — the founding report established this as "the first example of a mutation in the coding portion of TGFB3" causing human disease, implicating the gene in "palatogenesis and normal muscle growth."

### 2.2 Genetic risk factors

- **Causal variants:** see §4 for the full curated variant table.
- **Founder allele:** `NM_003239.5(TGFB3):c.787G>C, p.(Asp263His)` (rs796051886, ClinVar 203492) is a **Belgian founder variant** of the Campine region, Flanders. Haplotype sharing of 1.92–4.14 Mb (markers D14S1047–D14S270 minimal; D14S1028–D14S983 maximal) across five families places the most recent common ancestor **~22 generations (~434 years)** ago `[FULL-TEXT / PMID:37719708]`. Schepers et al. had already flagged this: "Of the 23 currently known *TGFB3* mutations, three substitute histidine for aspartic acid at amino acid position 263 … Since all described patients with this mutation originate from the same county, this might represent a founder mutation" `[FULL-TEXT / PMC5947146]`.
- **Population frequency of the founder allele:** dbSNP/gnomAD v4 exomes report **1 allele in 595,680** (global AF ≈ 2×10⁻⁶), the single carrier of European ancestry; 0 in South Asian, American, East Asian, Ashkenazi Jewish, African and Middle Eastern populations. Consistent with a private/near-private pathogenic allele.
- **Second/modifier loci (hypothesis-generating, not established):** the Belgian study raised four candidate explanations for low penetrance — age-dependent penetrance, a second *TGFB3* allele (cis or somatic), modifier loci elsewhere in the TGF-β network, and variable "paradoxical" pathway compensation. One clinically affected family member carried a **NOTCH1 VUS (c.6910T>G, p.Leu2304Val)** absent in unaffected relatives `[FULL-TEXT / PMID:37719708]`. This is a single observation and should be curated as a *hypothesis*, not a modifier claim.
- **Gene-level constraint:** TGFB3 is reported as loss-of-function constrained — **pLI 1, LOEUF 0.25** in gnomAD v4.0 `[SECONDARY — VERIFY against the gnomAD browser before use]`. If confirmed this supports haploinsufficiency as the operative mechanism.

### 2.3 Environmental risk factors

No environmental factor is established as necessary or sufficient. Recognised **aortic-event modifiers** carried over from general HTAD management, and explicitly discussed in the Belgian cohort as insufficient to explain the observed variability:

- **Hypertension**, **smoking**, **hypercholesterolaemia** `[FULL-TEXT / PMID:37719708]`
- **Pregnancy and the puerperium** — GeneReviews: "Pregnancy and the postpartum period can be dangerous for women with LDS because of increased risk of aortic dissection/rupture and uterine rupture." `[DB-RECORD]`
- **Isometric/competitive exertion and cardiovascular stimulants** — GeneReviews advises avoiding "Contact sports, competitive sports, and isometric exercise" and "Agents that stimulate the cardiovascular system including routine use of decongestants or triptan medications" `[DB-RECORD]`
- **Age** is the single strongest observed modifier: mean age at TAAD onset in the founder cohort was **63 years**; both dissections in the Montalcino cohort occurred at **ages 55–60**.

### 2.4 Protective factors

No genetic protective variant or protective allele is described. There are **no data specific to TGFB3** on dietary or lifestyle protection. Presumed protective by extrapolation from HTAD management (not TGFB3-validated): blood-pressure control, avoidance of tobacco, avoidance of isometric strain, and pre-emptive prophylactic aortic repair at the gene-adjusted threshold.

### 2.5 Gene–environment interaction

The core G×E hypothesis in this disease is that **TGFB3 haploinsufficiency creates a permissive aortic-wall state that requires an additional insult (age-accumulated haemodynamic stress, hypertension, pregnancy, or a somatic/second genetic hit) to manifest as aneurysm**. The authors' formulation `[FULL-TEXT / PMID:37719708]`:

> "haploinsufficiency alone by the TGFB3 variant may not result in aneurysm development but that additional factors are required to provoke the aneurysm phenotype"

A separate, well-documented G×E thread exists for TGFB3 in **non-syndromic orofacial clefting**, where TGFB3 markers show association and **parent-of-origin effects** (lower risk on maternal than paternal transmission of the rs2300607 T allele; [PMID:18480962](https://pubmed.ncbi.nlm.nih.gov/18480962/)), with positive associations in some populations (Japanese candidate-gene analyses, Indian subcontinent, South American, Philippine) and null results in others (Norwegian). This is a *susceptibility* signal at the same locus, mechanistically coherent with the Tgfb3-null cleft palate phenotype, and should be curated as a distinct association — **not** as Rienhoff syndrome.

---

## 3. Phenotypes

### 3.1 Two phenotypic poles

**Pole A — the index/neuromuscular presentation** (index proband, [PMID:23824657](https://pubmed.ncbi.nlm.nih.gov/23824657/)). Onset **congenital/neonatal**, non-progressive-to-slowly-improving, **no vascular disease** on serial imaging:

| Feature | Detail (all `[FULL-TEXT]`) | HPO suggestion (OAK-verified) |
|---|---|---|
| Distal arthrogryposis / contractures | Right hand (3rd–4th fingers worst), bilateral toes; "Marked contractures at the proximal phalangeal joints" | **HP:0005684** Distal arthrogryposis; **HP:0002803** Congenital contracture; **HP:0001371** Flexion contracture |
| Low muscle mass | Strength 1/5, decreased bulk, diminished reflexes; quadriceps biopsy age 7 with "Type 1 fiber predominance but mild and focal Type 1 fiber disproportion consistent with disuse" and "no evidence of chronic dystrophic or inflammatory changes" | **HP:0003199** Decreased muscle mass; **HP:0003701** Proximal muscle weakness; **HP:0003202** Skeletal muscle atrophy |
| Hypotonia | Mild, neonatal | **HP:0001252** Hypotonia; **HP:0001319** Neonatal hypotonia |
| Failure to thrive / growth retardation | 2.9 kg at birth (5th c.), 4.2 kg at 3 mo (<5th c.), 7.5 kg at 17 mo (<1st c.), 15.5 kg / 115 cm at 7 y | **HP:0001508** Failure to thrive; **HP:0001510** Growth delay |
| Reduced subcutaneous fat | "markedly reduced subcutaneous fat" | **HP:0003758** Reduced subcutaneous adipose tissue |
| Delayed motor milestones | Walked independently at 24 months, Gowers sign, "hip waddle" gait | **HP:0002194** Delayed gross motor development |
| Bifid uvula, intact hard palate | Normal voice | **HP:0000193** Bifid uvula |
| Hypertelorism | Outer canthal 7.8 cm, >97th centile | **HP:0000316** Hypertelorism |
| Blue sclerae, prominent eyes | | **HP:0000592** Blue sclerae; **HP:0000520** Proptosis |
| Pes planus, pectus excavatum, retrognathia, coxa valga, large-joint hyperextensibility | Bilateral | **HP:0001763**, **HP:0000767**, **HP:0000278**, **HP:0002673**, **HP:0001382** |
| Midline facial naevus flammeus | | **HP:0001052** Nevus flammeus |
| **Cardiovascular — negative** | "Yearly echocardiograms beginning at 18 months showed no cardiac defect or dysfunction"; aortic annulus and root within normal range at 6.5 y | — |

**Pole B — the adult aortopathy presentation** (Bertoli-Avella 2015; Belgian founder cohort 2023; Montalcino 2025). Onset **adult, frequently ≥50 years**; the cardinal manifestation is aortic dilation, with dissection a late and uncommon event.

`[ABSTRACT-VERBATIM]` ([PMID:25835445](https://pubmed.ncbi.nlm.nih.gov/25835445/)):
> "Other systemic features overlap clinically with Loeys-Dietz, Shprintzen-Goldberg, and Marfan syndromes, including cleft palate, bifid uvula, skeletal overgrowth, cervical spine instability and clubfoot deformity."

### 3.2 Frequencies — the three quantitative datasets, kept separate

These three denominators are **not interchangeable**. Cohort ascertainment drives the numbers: the Belgian series is cascade-tested (includes asymptomatic carriers), Montalcino is an aortopathy registry, and the "literature" column is proband-enriched. A knowledge-base entry should carry all three with distinct `population` values rather than averaging them.

**(a) Montalcino Aortic Consortium, n=34, median age 42 y, 56% male** ([PMID:39653386](https://pubmed.ncbi.nlm.nih.gov/39653386/)):

| Feature | Frequency | HPO suggestion |
|---|---|---|
| Aortic dilation (Z-score >2) | **29% (10/34)** — `[ABSTRACT-VERBATIM]` "Aortic dilation (Z-Score>2) was present in 10 individuals (29%) and aortic dissection occurred in 2 (6%)." | **HP:0002616** Aortic root aneurysm / **HP:0002617** Vascular dilatation |
| Aortic dissection | **6% (2/34)**, ages 55–60 | **HP:0002647** Aortic dissection |
| Arterial tortuosity | **25%** | **HP:0005116** Arterial tortuosity |
| Extra-aortic arterial aneurysm | **6%** | **HP:0004942** Aortic aneurysm (use with anatomical qualifier) |
| Mitral valve prolapse | **21%** | **HP:0001634** Mitral valve prolapse |
| **Free of aortic disease** | **68%** | — |
| Deaths | **0** | — |

**(b) Belgian c.787G>C founder cohort, n=27 (10 F / 17 M), ages 5–84 y, mean 47 y** ([PMID:37719708](https://pubmed.ncbi.nlm.nih.gov/37719708/)):

| Feature | Frequency | Notes |
|---|---|---|
| Aortic aneurysm/dissection (TAAD) | **15% (4/27)**, mean age at onset **63 y** | `[ABSTRACT-VERBATIM]` "only in 4 out of the 27 variant-harboring individuals, significant aortic involvement was observed" |
| Any arterial involvement | **19% (5/27)** | |
| Any connective-tissue finding | **52% (14/27)** | |
| **Completely unaffected carriers** | **41% (11/27)** | The single most important number for genetic counselling |

Non-aortic cardiovascular findings in this cohort `[FULL-TEXT]`: bicuspid aortic valve with 50 mm aneurysm (Z=5.2) (**HP:0001647**), hypertrophic cardiomyopathy (**HP:0001639**), mitral insufficiency ×2 (**HP:0001653**), ventricular septal defect (**HP:0001629**), concentric/septal hypertrophy, conduction abnormalities requiring pacemakers. Connective-tissue findings: easy bruising (**HP:0000978**), inguinal hernia (**HP:0000023**), arachnodactyly with wrist/thumb signs (**HP:0001166**), pes planus ×2 (**HP:0001763**), disc herniation ×2, bifid uvula (**HP:0000193**), mild scoliosis (**HP:0002650**), Dupuytren disease ×2.

The four TAAD events `[FULL-TEXT]`: 31 y M type A dissection (post-Bentall); 65 y M sinus of Valsalva aneurysm 50 mm + BAV insufficiency; 80 y M aortic root 43 mm (Z=2.1); 75 y M ascending aneurysm 44 mm (Z=6.4).

**(c) Pooled prior literature, n=82 published TGFB3 patients** (comparator table in [PMID:37719708](https://pubmed.ncbi.nlm.nih.gov/37719708/)):

| Feature | Literature (82) | Founder cohort (27) | p |
|---|---|---|---|
| TAAD penetrance | **40% (33/82)** | 15% (4/27) | 0.0288 |
| Any arterial involvement | **46% (38/82)** | 19% (5/27) | 0.0194 |
| Connective-tissue findings | **93% (76/82)** | 52% (14/27) | <0.0001 |

A further breakdown of "aortic dilation 42%, aneurysm 16%, dissection 12%" among reported TGFB3 patients appears in the same literature review `[SECONDARY — VERIFY]`.

Sources pooled in that 82-patient literature column: Rienhoff 2013, Matyas 2014, Bertoli-Avella 2015, Kuechler 2015, Ziganshin 2015, Overwater 2018, Schepers 2018, Marsili 2020, Abdelhadi 2021, Hussein 2021.

### 3.3 Additional phenotypes in the OMIM/MedGen clinical synopsis for LDS5

`[DB-RECORD, MedGen 816342]` — organ-system synopsis, useful for HPO seeding but **without frequencies** (do not assign frequency bands from this source):

- **Cardiovascular:** aortic root aneurysm (**HP:0002616**), ascending aortic dissection (**HP:0002647**), atrial septal defect (**HP:0001631**), ventricular septal defect (**HP:0001629**), mitral regurgitation (**HP:0001653**), patent foramen ovale (**HP:0001655**)
- **Skeletal:** pectus excavatum/carinatum (**HP:0000767**/**HP:0000768**), kyphoscoliosis (**HP:0002751**), **cervical spine instability (HP:0010646)**, clubfoot (**HP:0001762**), pes planus (**HP:0001763**), arachnodactyly (**HP:0001166**), joint hypermobility (**HP:0001382**), congenital finger flexion contractures (**HP:0001371**), spondylolisthesis (**HP:0003302**), osteoarthritis (**HP:0002758**), scapular winging, retrognathia (**HP:0000278**), bilateral coxa valga (**HP:0002673**)
- **Craniofacial:** cleft palate (**HP:0000175**), bifid uvula (**HP:0000193**), hypertelorism (**HP:0000316**), midface retrusion / malar flattening (**HP:0000272**), high palate, downslanted palpebral fissures (**HP:0000494**), overhanging nasal tip, prominent nasal bridge, long palpebral fissure, tented upper lip vermilion, smooth philtrum, brachycephaly/dolichocephaly (**HP:0000268**), dental crowding (**HP:0000678**), overfolded helix
- **Ocular:** proptosis (**HP:0000520**), ptosis (**HP:0000508**), blue sclerae (**HP:0000592**); exotropia (**HP:0000577**) noted in the Schepers comparison
- **Growth/muscle:** tall **or** short stature (**HP:0000098** / short stature), increased arm span, decreased muscle mass (**HP:0003199**), reduced subcutaneous adipose tissue (**HP:0003758**), hypotonia (**HP:0001252**), delayed gross motor development (**HP:0002194**), failure to thrive in infancy (**HP:0001508**)
- **Integument:** bruising susceptibility (**HP:0000978**), naevus flammeus (**HP:0001052**)
- **Other:** inguinal and hiatus hernia (**HP:0000023**, **HP:0002036**), eosinophilic esophagitis (**HP:0410151** Eosinophilic infiltration of the esophagus), **uterine rupture in pregnancy (HP:0100718)**

**Distinguishing negatives** (per Schepers et al. Table 5 comparison `[FULL-TEXT]`): craniosynostosis **absent** (contrast Shprintzen–Goldberg), pneumothorax **absent**, arterial tortuosity historically scored **absent** (now known to occur — see §1.4), dural ectasia and young-age dissection **uncertain**.

### 3.4 Reference frequencies for the LDS *umbrella* (ORPHA:60030) — use with caution

The Orphanet phenotype–frequency table for ORPHA:60030 is dominated by TGFBR1/TGFBR2 disease and **systematically overstates severity for TGFB3**. It is quotable as a structured reference (`snippet` rows are stable substrings) but should be labelled as pertaining to the LDS group, not LDS5:

```
| HP:0004942 | Aortic aneurysm | Very frequent (99-80%) |
| HP:0002647 | Aortic dissection | Very frequent (99-80%) |
| HP:0005116 | Arterial tortuosity | Very frequent (99-80%) |
| HP:0100718 | Uterine rupture | Very frequent (99-80%) |
| HP:0000175 | Cleft palate | Frequent (79-30%) |
| HP:0000193 | Bifid uvula | Frequent (79-30%) |
| HP:0001363 | Craniosynostosis | Frequent (79-30%) |
| HP:0002099 | Asthma | Frequent (79-30%) |
| HP:0410151 | Eosinophilic infiltration of the esophagus | Occasional (29-5%) |
```

### 3.5 Onset, severity, progression

- **Onset:** bimodal. Congenital/neonatal for the palatal, contractural and neuromuscular features; **adult (often ≥50 y)** for the aortic and arterial features.
- **Severity:** **variable**, ranging from lifelong asymptomatic carriage (41% of founder-variant carriers) to type A dissection and to a severe multisystem biallelic phenotype.
- **Progression:** the aortopathy is **slowly progressive**; the craniofacial/skeletal features are **static or slowly progressive** (scoliosis, osteoarthritis). Muscle mass in the index case did **not** progressively deteriorate (biopsy showed disuse change, not dystrophy) — relevant for distinguishing this from a myopathy.
- **Quality-of-life impact:** **No disease-specific QoL instrument data exist for LDS5/TGFB3.** No EQ-5D, SF-36 or PROMIS study identified. Per-phenotype QoL burden must be reasoned by analogy to LDS/Marfan (activity restriction, surgical burden, pain from scoliosis/osteoarthritis/disc herniation, reproductive risk counselling, and the psychological load of aortic surveillance). **Mark this as an explicit data gap.**

---

## 4. Genetic / Molecular Information

### 4.1 Gene and protein

- **TGFB3**, 14q24.3, **7 exons** `[FULL-TEXT / PMC5947146: TGFB3 is on "the long arm of chromosome 14" and "include[s] 7 exons"]`. HGNC:11769; OMIM *190230.
- **Protein (UniProt P10600), 412 aa proprotein**, three regions: signal peptide 1–23; **latency-associated peptide (LAP) 24–300**; **mature TGF-β3 cytokine 301–412**. Furin-type **RKKR** cleavage motif at the LAP/mature boundary (~codon 300). Cystine-knot disulfides 307–316, 315–378, 344–409, 348–411; interchain disulfide at 377. N-glycosylation at N74, N135, N142. **Cell-attachment (RGD) motif at residues 261–263** — the residue hit by the Belgian founder variant. PDB structures: 1TGJ, 1KTZ, 1TGK, 2PJY, 3EO1, 8V52, 9B9F (X-ray); 8VS6, 8VSB (full-length cryo-EM 24–412), 9FK5.

### 4.2 Curated variant table

From Schepers et al. 2018 `[FULL-TEXT / PMC5947146]` (15 variants tabulated; the paper states 23 TGFB3 mutations were known at the time). This table is directly reusable for a KB variant list:

| cDNA (NM_003239.5) | Protein | Domain | Type | First report |
|---|---|---|---|---|
| c.106A>T | p.Lys36* | LAP | nonsense | Schepers 2018 |
| c.437delT | p.Leu146Hisfs*68 | LAP | frameshift | Schepers 2018 |
| c.704delA | p.Asn235Metfs*11 | LAP | frameshift | Bertoli-Avella 2015 |
| c.754+2T>C | p.Glu216_Lys251del | LAP | splice | Bertoli-Avella 2015 |
| **c.787G>C** | **p.Asp263His** | LAP (RGD motif) | missense | Bertoli-Avella 2015 — **Belgian founder** |
| c.796C>T | p.Arg266Cys | LAP | missense | Schepers 2018 |
| c.898C>T | p.Arg300Trp | RKKR motif | missense | Bertoli-Avella 2015 |
| c.899G>A | p.Arg300Gln | RKKR motif | missense | Matyas 2014 |
| c.898C>G | p.Arg300Gly | RKKR motif | missense | Kuechler 2015 |
| c.965T>C | p.Ile322Thr | cytokine | missense | Bertoli-Avella 2015 |
| c.979G>T | p.Asp327Tyr | cytokine | missense | Schepers 2018 |
| c.1095C>A | p.Tyr365* | cytokine | nonsense | Bertoli-Avella 2015 |
| c.1157delT | p.Leu386Argfs*21 | cytokine | frameshift | Bertoli-Avella 2015 |
| c.1202T>C | p.Leu401Pro | cytokine | missense | Bertoli-Avella 2015 |
| **c.1226G>A** | **p.Cys409Tyr** | cytokine (cystine knot) | missense | **Rienhoff 2013 — index case, de novo** |

Additional variants outside that table:
- **c.427A>T, p.Arg143*** — LAP nonsense; ClinVar RCV003050507 classified **Pathogenic for Rienhoff syndrome**; reported in a woman with a *forme fruste* LDS5 phenotype ([Ann Intern Med Clin Cases 2023, doi:10.7326/aimcc.2023.0035](https://www.acpjournals.org/doi/10.7326/aimcc.2023.0035))
- **c.926+2T>C** — splice; ClinVar RCV005250424, submitted under "Loeys-Dietz syndrome"
- **Homozygous deletion of exons 2–7** — ([PMID:32022420](https://pubmed.ncbi.nlm.nih.gov/32022420/))
- **Regulatory 5′/3′-UTR variants** — cause the **allelic** disorder ARVD1, not LDS5 (§4.6)

**Variant-type distribution** `[FULL-TEXT / PMC5947146, quotable]`:
> "The majority of the TGFB3 mutations consist of missense mutations (60%), whereas 20% are frameshift mutations, 13% are nonsense mutations, and 7% of mutations affect a splice site."

**Domain clustering is mechanistically informative:** three separate mutations at **codon 300 (the RKKR furin cleavage site)** and the RGD motif at 261–263 indicate that disrupting either *proteolytic maturation* or *integrin-mediated activation* of latent TGF-β3 is sufficient to cause disease — the ligand need not be structurally destroyed.

### 4.3 Classification, origin, allele frequency

- **ACMG classification:** the founder variant p.(Asp263His) is **Likely pathogenic**; p.Arg143* is **Pathogenic** in ClinVar; several missense variants remain **VUS** in isolation. Note the discordance risk: rs796051886 carries two ClinVar entries — **Pathogenic for Rienhoff syndrome** *and* **Uncertain significance for hypertrophic cardiomyopathy**.
- **Germline** in all reported cases. **No somatic TGFB3 driver in aortic disease has been demonstrated**, though somatic second hits in aortic tissue were raised as a low-penetrance hypothesis `[FULL-TEXT / PMID:37719708]`.
- **Allele frequency:** pathogenic alleles are private/ultra-rare (founder allele 1/595,680 in gnomAD v4 exomes). The benign polymorphism **p.Thr60Met (rs4252315)** is annotated in UniProt and should not be confused with a causal allele.
- **De novo rate:** the index p.Cys409Tyr was de novo. GeneReviews reports for LDS as a whole: "Approximately 75% of probands diagnosed with LDS have the disorder as the result of a de novo pathogenic variant; approximately 25% of individuals diagnosed with LDS have an affected parent" `[DB-RECORD]`. **Caution:** that 75% is an LDS-wide figure driven by severe TGFBR1/2 disease; TGFB3 families are predominantly **multigenerational and inherited** (11 families in 2015; 5 founder families in 2023), so the de novo fraction for TGFB3 specifically is almost certainly far lower.

### 4.4 Functional consequences — and an unresolved controversy

Three positions coexist in the literature. A knowledge base should record this as a **live mechanistic disagreement**, not pick a winner.

1. **Loss of function / hypomorph (index case).** `[FULL-TEXT / PMID:23824657]` p.Cys409Tyr is "a hypomorphic allele encoding a TGFB3 ligand that is not functional." "This penultimate cysteine is conserved in all TGFB family member ligands." Mutant protein was secreted but inert: no signal in a HeLa p3TPLux reporter; in *Xenopus*, "A 1:1 ratio of mutant-to-wild-type TGFB3 RNA diminished the pSMAD2 and pERK1/2 signals to approximately 40% and 60%" respectively — i.e. **dominant-negative-like interference**, while BMP signalling was spared ("Ectopic expression of TGFB3-C409Y had no effect on either SMAD1 phosphorylation (pSMAD1) or dorsal ventral patterning").
2. **Haploinsufficiency with paradoxical pathway up-regulation (aortopathy).** `[ABSTRACT-VERBATIM / PMID:25835445]`: "In line with previous observations in aortic wall tissues of patients with mutations in effectors of TGF-β signaling (TGFBR1/2, SMAD3, and TGFB2), we confirm a paradoxical up-regulation of both canonical and noncanonical TGF-β signaling in association with up-regulation of the expression of TGF-β ligands." Schepers et al. concur: TGFB3 variants cause "paradoxical activation of TGF-β signaling" via increased phospho-SMAD2 and downstream target up-regulation `[FULL-TEXT]`.
3. **Gain of function at codon 300.** `[ABSTRACT-VERBATIM / PMID:26184463]`: mutations at "codon Arg300 presumably lead to increased TGF-beta signalling." This is the crux of the published exchange between Matyas et al. ([PMID:24798638](https://pubmed.ncbi.nlm.nih.gov/24798638/)) and Rienhoff ([PMID:24817670](https://pubmed.ncbi.nlm.nih.gov/24817670/)) — whether RKKR-motif variants that block furin cleavage produce *less* free active ligand or an aberrantly *more* active/differently-localised species.

**Reconciling view for a pathophysiology model:** the primary lesion is reduced availability of correctly matured, integrin-activatable TGF-β3, and the aortic wall then exhibits secondary, compensatory (and ultimately maladaptive) up-regulation of TGF-β signalling — the canonical "TGF-β paradox" of the LDS family, explicitly named as a mechanism to be dissected in the 2026 preclinical modelling review ([PMID:42380922](https://pubmed.ncbi.nlm.nih.gov/42380922/), which addresses "the TGF-β paradox, extracellular matrix dysregulation and immune activation").

### 4.5 Dose–response: biallelic loss is far more severe

`[ABSTRACT-VERBATIM / PMID:32022420]` — the homozygous exon 2–7 deletion case is "the first case of a homozygous TGFB3 variant associated with a severe LDS5 and Marfan-like presentation," with cleft palate and bifid uvula, long triangular face, large ears and nose, thin lips, dental crowding, severe scoliosis, joint laxity, long digits, flat feet, dilated ascending aorta and patent foramen ovale. This provides in-human allelic-series evidence for a **dosage mechanism** and strongly supports haploinsufficiency as the heterozygous mechanism.

### 4.6 Allelic disorder: ARVD1

Regulatory (UTR) TGFB3 mutations cause **arrhythmogenic right ventricular cardiomyopathy type 1** — mechanistically distinct from LDS5. `[ABSTRACT-VERBATIM / PMID:15639475]`: "In vitro expression assays with constructs containing the mutations showed that mutated UTRs were twofold more active than wild-types." ClinGen's ARVC GCEP rates this gene-disease relationship **Limited** (2019). Curate as an allelic disorder, not as a Rienhoff phenotype.

### 4.7 Modifier genes, epigenetics, chromosomal abnormalities

- **Modifier genes:** none established. The NOTCH1 VUS observation (§2.2) is the only candidate reported.
- **Epigenetics:** **no TGFB3-specific methylation or chromatin study in LDS5 identified.** Adjacent-but-not-equivalent: parent-of-origin effects at TGFB3 in non-syndromic clefting ([PMID:18480962](https://pubmed.ncbi.nlm.nih.gov/18480962/)) hint at imprinting-like regulation; and a multi-ancestry EWAS identified methylation sites associated with aortic augmentation index in TOPMed MESA ([PMID:37848499](https://pubmed.ncbi.nlm.nih.gov/37848499/)) — general aortic biology, not LDS5. **Data gap.**
- **Chromosomal abnormalities:** the only structural variant reported is the intragenic **homozygous exon 2–7 deletion**. No recurrent 14q24.3 microdeletion syndrome encompassing TGFB3 is described as a cause of LDS5. Chromosomal microarray therefore has limited but non-zero yield (it would detect that class of intragenic multi-exon deletion only if probe density suffices — exon-level CNV analysis from NGS data is preferable).

---

## 5. Environmental Information

- **Environmental toxicants / radiation / occupational exposure:** **no established role.** No CTD-documented chemical–disease association specific to LDS5.
- **Lifestyle:** relevant only as aortic-event modifiers — smoking, hypertension, hypercholesterolaemia (`[FULL-TEXT / PMID:37719708]`, judged insufficient to explain phenotypic heterogeneity); isometric/competitive exercise and cardiovascular stimulants (GeneReviews avoidance list); pregnancy/postpartum haemodynamics.
- **Infectious agents:** **not applicable.** No infectious trigger.

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (upstream → downstream), with ontology anchors

**Node 1 — TGFB3 ligand deficiency / mis-maturation** *(scale: MOLECULAR)*
Heterozygous TGFB3 variant → reduced quantity or functionality of mature, activatable TGF-β3. Mechanistic sub-branches by domain: (i) truncating/frameshift → haploinsufficiency; (ii) **RGD motif (261–263)** → failure of integrin-mediated activation of the latent complex; (iii) **RKKR (codon 300)** → failure of furin cleavage/maturation; (iv) **cystine-knot cysteines (e.g. C409)** → secreted but signalling-incompetent dimer with dominant-negative interference on wild-type ligand.
GO: **GO:0008083** growth factor activity; **GO:0005160** transforming growth factor beta receptor binding; **GO:0031012** extracellular matrix; **GO:0005576** extracellular region.

**Node 2 — Perturbed TGF-β receptor signalling in the aortic wall** *(scale: CELLULAR)*
Impaired ligand → altered TGFBR1/TGFBR2 → SMAD2/3 signalling, with the paradoxical net result of **increased** canonical (phospho-SMAD2) and non-canonical (ERK) pathway output in patient aortic tissue.
GO: **GO:0007179** transforming growth factor beta receptor signaling pathway (`modifier: DYSREGULATED`); **GO:0071560** cellular response to transforming growth factor beta stimulus.
CL: **CL:0000359** vascular associated smooth muscle cell; **CL:0002139** endothelial cell of vascular tree; **CL:0000057** fibroblast; **CL:0000186** myofibroblast cell.

**Node 3 — Medial degeneration and ECM dysregulation** *(scale: TISSUE)*
Elastic-fibre fragmentation, ECM disorganisation, VSMC phenotypic switching and loss of contractile identity → reduced tensile strength of the aortic media. This is the shared hub of heritable aortopathy and the natural `conforms_to` target for the dismech `aortopathy_tgfbeta_dysregulation#TGF-beta Signaling Dysregulation` and `#Medial Degeneration` nodes.
GO: **GO:0030198** extracellular matrix organization; **GO:0048251** elastic fiber assembly; **GO:0035909** aorta morphogenesis.
UBERON: **UBERON:0000947** aorta; **UBERON:0001496** ascending aorta; **UBERON:0004178** aorta smooth muscle tissue; **UBERON:0001637** artery.
Supporting general mechanism (not TGFB3-specific): SLC44A2-mediated VSMC phenotypic switching in aortic aneurysm ([PMID:39145443](https://pubmed.ncbi.nlm.nih.gov/39145443/), *J Clin Invest* 2024).

**Node 4 — Progressive aortic dilation → dissection/rupture** *(scale: ORGANISM)*
Late-onset, incompletely penetrant. HP:**HP:0002617** → **HP:0002616** → **HP:0002647**.

**Parallel developmental arm (explains the congenital features):**

**Node 2′ — Impaired epithelial-to-mesenchymal transition in palatal shelf fusion and myogenesis** *(scale: CELLULAR)*
`[FULL-TEXT / PMID:23824657]` the authors propose impaired TGFB3 signalling disrupts EMT during myogenesis and palatogenesis: "Partial or incomplete EMT may diminish the number of embryonic muscle precursor cells, ultimately reducing post-natal myofibril mass but not affecting muscle architecture." Alternatives they discuss: **unopposed myostatin (GDF8) signalling**, and premature myocyte differentiation from reduced SMAD1/5 phosphorylation.
GO: **GO:0001837** epithelial to mesenchymal transition; **GO:0060021** roof of mouth development; **GO:0060022** hard palate development; **GO:0007519** skeletal muscle tissue development; **GO:0030509** BMP signaling pathway (antagonised arm).
CL: **CL:0008019** mesenchymal cell; **CL:0000188** cell of skeletal muscle; **CL:0000138** chondrocyte.
UBERON: **UBERON:0003216** hard palate; **UBERON:0001733** soft palate; **UBERON:0001734** palatine uvula; **UBERON:0001134** skeletal muscle tissue.

**Node 3′ — Cleft palate / bifid uvula and reduced postnatal muscle mass** *(scale: TISSUE/ORGANISM)*
HP:**HP:0000175**, **HP:0000193**, **HP:0003199**, **HP:0005684**.

### 6.2 Protein dysfunction

Position-specific and well characterised for the index allele. The mutated **C409** is the penultimate cysteine of the cystine knot; substitution to tyrosine permits secretion but abolishes signalling competence, and the mutant interferes with wild-type ligand in a co-expression setting (Xenopus 1:1 → pSMAD2 ~40%, pERK1/2 ~60% of control). RKKR-motif and RGD-motif variants act on maturation and activation rather than on fold integrity.

### 6.3 Metabolic and biochemical abnormalities

**None described.** There is no enzyme deficiency, no biomarker metabolite, no ion-channel defect, and no reported metabolomic or lipidomic signature for LDS5. Serum TGF-β1/β2/β3 levels have been explored as biomarkers in Marfan/LDS generally but are **not validated for TGFB3-related disease**. Explicit gap.

### 6.4 Immune system involvement

No TGFB3-specific immunopathology is reported. Two adjacent findings should be curated with clear attribution:
- **TGFBR1/TGFBR2-restricted (not TGFB3):** Frischmeyer-Guerrerio et al. showed LDS patients with receptor mutations are "strongly predisposed to develop allergic disease, including asthma, food allergy, eczema, allergic rhinitis, and eosinophilic gastrointestinal disease," with elevated IgE, eosinophils and TH2 cytokines ([PMID:23884466](https://pubmed.ncbi.nlm.nih.gov/23884466/), *Sci Transl Med* 2013). The eosinophilic-esophagitis and asthma entries appearing in the LDS umbrella HPO annotations trace to this receptor-side biology; **do not transfer them to TGFB3 without primary evidence.**
- **Immune activation is named as one of three mechanistic axes** for LDS modelling generally in the 2026 review ([PMID:42380922](https://pubmed.ncbi.nlm.nih.gov/42380922/)).
- An open trial studies LDS immunopathology broadly: [NCT05472519](https://clinicaltrials.gov/study/NCT05472519) "Immunopathology of Loeys-Dietz Syndrome."

### 6.5 Tissue damage mechanisms

Medial degeneration with elastic-fibre fragmentation and VSMC loss; haemodynamic wall stress as the chronic driver; no ischaemic, oxidative-stress-specific or necroinflammatory mechanism uniquely attributed to TGFB3. Fibrotic remodelling is implicated by the TGF-β paradox but has not been quantified in TGFB3 patient aortas beyond the pSMAD2/ligand up-regulation reported in 2015.

### 6.6 Molecular profiling

- **Transcriptomics — the key recent dataset:** [PMID:40923070](https://pubmed.ncbi.nlm.nih.gov/40923070/) (*JTCVS Open* 2025) performed **single-cell RNA sequencing on aortic tissue** from 62 LDS patients undergoing aortic root replacement and found "distinct smooth muscle cell dysregulation patterns between genetic subtypes," with markedly different clinical trajectories by subtype (5-/10-year survival 97%/86% for TGFBR1/2 with aortic events in 17–28%; 94% at both time points for SMAD3 with 0% aortic events). **Caveat: the TGFB3 representation in this surgical cohort is not stated in the abstract and is likely very small or zero** — verify before attributing subtype-specific transcriptomics to LDS5.
- **Proteomics / metabolomics / lipidomics:** none for LDS5.
- **Functional genomics screens (CRISPR/RNAi):** no TGFB3-focused aortopathy screen identified. DepMap contains TGFB3 dependency data but in cancer-cell-line context, not disease-relevant.
- **Developmental transcriptomics of relevance:** [PMID:39096177](https://pubmed.ncbi.nlm.nih.gov/39096177/) "Modulation of mechanosensitive genes during embryonic aortic arch development" (*Dev Dyn* 2025); and Tgfb3-mutant palatal transcriptome studies (e.g. *Sci Rep* 2020, "Transcriptional analysis of cleft palate in TGFβ3 mutant mice").

---

## 7. Anatomical Structures Affected

**Primary organs / systems**
- **Aorta and arterial tree** (cardiovascular): **UBERON:0000947** aorta; **UBERON:0001496** ascending aorta; aortic root/sinus of Valsalva; abdominal aorta; **UBERON:0001637** artery — arch vessels, cerebral circulation, iliac and femoral arteries. Distribution is **diffuse and multi-segment**; the 2025 LDS-wide aneurysm study found "75% of AAs were in the arch vessels or cerebral circulation" ([PMID:40533122](https://pubmed.ncbi.nlm.nih.gov/40533122/)) and a TGFB3 case presented with giant iliac + true deep femoral artery aneurysms ([PMID:39450604](https://pubmed.ncbi.nlm.nih.gov/39450604/)).
- **Cardiac valves:** **UBERON:0002135** mitral valve (prolapse 21%, regurgitation); **UBERON:0002137** aortic valve (bicuspid variant reported).
- **Palate and craniofacial skeleton:** **UBERON:0003216** hard palate, **UBERON:0001733** soft palate, **UBERON:0001734** palatine uvula; midface, mandible, zygoma.
- **Axial and appendicular skeleton:** **UBERON:0002413** cervical vertebra (instability — a distinctive and anaesthetically important feature), thoracolumbar spine (scoliosis, spondylolisthesis, disc herniation), chest wall, feet/hands.
- **Skeletal muscle:** **UBERON:0001134** skeletal muscle tissue; **UBERON:0001630** muscle organ (reduced mass, not dystrophy).

**Secondary involvement**
- Uterus (rupture risk in pregnancy), inguinal canal and diaphragmatic hiatus (hernias), eye (proptosis, ptosis, blue sclerae, myopia, exotropia), skin/subcutis (bruising, reduced subcutaneous fat, naevus flammeus), joints (osteoarthritis, hypermobility, Dupuytren disease), oesophagus (eosinophilic infiltration — LDS-umbrella attribution).

**Tissue and cell level**
Connective tissue is the unifying substrate: **CL:0000359** vascular associated smooth muscle cell (the principal effector cell of medial degeneration), **CL:0002139** endothelial cell of vascular tree, **CL:0000057** fibroblast, **CL:0000186** myofibroblast cell, **CL:0008019** mesenchymal cell, **CL:0000138** chondrocyte, **CL:0000188** cell of skeletal muscle.

**Subcellular level**
- **GO:0005576** extracellular region and **GO:0031012** extracellular matrix — the site of latent TGF-β3 storage and integrin-dependent activation (the LAP–mature complex is stored in the ECM).
- Golgi apparatus — the site of furin cleavage disrupted by RKKR-motif variants.
- Cell surface — integrin/TGFBR receptor complexes.

**Lateralisation**
Aortic and craniofacial involvement are **midline/axial**; limb and arterial aneurysmal disease may be **unilateral or asymmetric** (e.g. right-hand-predominant contractures in the index case; unilateral iliac/femoral aneurysms).

---

## 8. Temporal Development

**Onset**
- **Congenital/neonatal** for palatal clefting/bifid uvula, distal arthrogryposis, hypotonia, hypertelorism, blue sclerae, clubfoot.
- **Adult, characteristically late** for the aortopathy. Median cohort age 42 y (Montalcino); mean age at first TAAD event **63 y** in the founder cohort; both Montalcino dissections at **55–60 y**.
- Onset pattern: **insidious/chronic** for the aortopathy; **acute catastrophic** at the point of dissection.

**Progression**
- Course: **chronic, lifelong, slowly progressive** for the vascular arm; **static** for craniofacial/palatal features once repaired.
- Rate: **slow**, and slower than any other LDS subtype. `[ABSTRACT-VERBATIM / PMID:39653386]`: TGFB3-related HTAD "is characterised by late-onset and less penetrant thoracic aortic and arterial disease compared with other transforming growth factor β HTAD."
- Staging: no disease-specific staging system exists. In practice aortic diameter/Z-score plus growth rate is the operative stage; per the 2022 ACC/AHA guideline, **rapid growth is defined as ≥0.3 cm in 1 year** for HTAD.
- **68% of the Montalcino cohort and 41% of founder-variant carriers never develop the defining lesion at all** — this disease is better modelled as an *age-dependent, incompletely penetrant risk state* than as an inexorable progression.

**Patterns**
- **Remission:** none spontaneously. Aortic risk is *removed segmentally*, not remitted, by prophylactic repair — and residual native aorta/arterial tree remains at risk (17% of LDS extra-aortic aneurysms enlarged over time; 38% of those that enlarged led to clinical events — [PMID:40533122](https://pubmed.ncbi.nlm.nih.gov/40533122/)).
- **Critical windows:** (i) fetal palatogenesis — irreversible once passed; (ii) infancy/childhood for cleft repair, feeding and motor rehabilitation; (iii) **pre-conception** — the decision window for prophylactic aortic repair (2022 ACC/AHA: repair before pregnancy is reasonable at ≥4.5 cm for TGFB2/TGFB3); (iv) mid-to-late adulthood — the surveillance window when dilation actually appears.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- **Prevalence: unknown.** No estimate exists for LDS5 specifically. Orphanet records for the LDS umbrella (ORPHA:60030): `| Unknown | Worldwide | Point prevalence |` — i.e. explicitly undocumented. Secondary sources give LDS overall as **1/25,000–1/100,000**.
- **Proportion of LDS attributable to TGFB3: ~1%–5%** `[DB-RECORD / GeneReviews]`. Applied to the LDS range this implies an order-of-magnitude estimate of roughly **0.04–2 per 1,000,000** — a derived figure, not a published one; label any KB `prevalence_class` as `NOT_YET_DOCUMENTED` or `ULTRA_RARE` with `measure_type: UNKNOWN` rather than asserting a rate.
- **Incidence:** not established.
- **Ascertainment context:** TGFB3 variants were found in 11 families among **470 index cases with thoracic aortic aneurysms** screened by linkage + exome + Sanger (`[ABSTRACT-VERBATIM / PMID:25835445]`) — a useful denominator for the gene's share of syndromic TAAD.

### 9.2 Inheritance genetics

- **Pattern: autosomal dominant** (HP:**HP:0000006**). One **autosomal recessive/biallelic** case (homozygous exon 2–7 deletion, [PMID:32022420](https://pubmed.ncbi.nlm.nih.gov/32022420/)) demonstrates a more severe recessive extreme — worth curating as a dosage observation rather than as a second inheritance mode for the disease.
- **Penetrance — a genuine and important discrepancy in the literature.** GeneReviews states, for the LDS genes collectively, "The penetrance of *SMAD2*, *SMAD3*, *TGFB2*, *TGFB3*, *TGFBR1*, and *TGFBR2* pathogenic variants is reported to be near 100%" `[DB-RECORD]`. The TGFB3-specific cohort data flatly contradict this for TGFB3: **41% of founder-variant carriers had no phenotypic abnormality at all**, TAAD penetrance was **15%**, and **68% of the Montalcino registry cohort is free of aortic disease**. `[FULL-TEXT / PMID:37719708]`:
  > "From all LDS genes, TGFB3 seems to have the lowest penetrance, both for vascular and connective tissue features."

  **Recommended curation:** record penetrance as **incomplete and age-dependent**, cite the cohort figures, and note the conflicting near-100% GeneReviews statement as an umbrella-level claim that does not hold for TGFB3. This is also consistent with ClinGen's **Limited** gene-disease validity call for TGFB3–familial TAAD.
- **Expressivity: highly variable, both within and between families** — the defining feature of this entity. The same founder allele produced a 31-year-old type A dissection and lifelong asymptomatic 80-year-olds.
- **Genetic anticipation:** not applicable (no repeat expansion); none reported.
- **Germline mosaicism:** not reported.
- **Founder effect:** yes — Campine region, Flanders, Belgium (§2.2).
- **Consanguinity:** relevant only to the biallelic case.
- **Carrier frequency:** not applicable (dominant); pathogenic-allele frequency is ~10⁻⁶ (§4.3).

### 9.3 Population demographics

- **Affected populations:** reported families are predominantly **European** (Belgian/Dutch/Flemish, German, Italian) and **Japanese** (the 2015 discovery cohort included Japanese co-investigators and families); the biallelic case arose in a Middle Eastern/consanguineous context. No population shows established excess risk apart from the Belgian founder cluster.
- **Geographic distribution of variants:** p.(Asp263His) → Campine region, Flanders. Others are private.
- **Sex ratio:** the two cohorts are **male-skewed** — Montalcino 56% male; Belgian founder cohort 17 M / 10 F, and **all four TAAD events occurred in males**. This is a small-numbers observation but aligns with the sex effect documented across LDS ([PMID:40482834](https://pubmed.ncbi.nlm.nih.gov/40482834/), "Sex-based differences in patients with Loeys-Dietz syndrome"). Treat as a signal warranting confirmation, not an established sex ratio.
- **Age distribution:** wide — carriers ascertained from age **5 to 84 y** (mean 47) in the founder cohort; Montalcino median 42 y.

---

## 10. Diagnostics

### 10.1 Genetic testing — the definitive modality

`[DB-RECORD / GeneReviews]`: the molecular diagnosis of LDS is established in a proband with "a heterozygous pathogenic (or likely pathogenic) variant in *SMAD2*, *SMAD3*, *TGFB2*, *TGFB3*, *TGFBR1*, or *TGFBR2*" plus clinical features (aortic root enlargement, type A dissection, characteristic features, or an established family history).

Recommended approach, in descending practical priority:
1. **Multigene HTAD/aortopathy panel** — TGFB3 is a standard panel member alongside FBN1, TGFBR1/2, TGFB2, SMAD2/3, ACTA2, MYH11, MYLK, PRKG1, COL3A1, SKI. This is the first-line test for syndromic TAAD and remains preferred over single-gene testing given phenotypic overlap.
2. **Exome sequencing (WES)** — historically the discovery route for this disease (index case 2013; Kuechler family 2015) and appropriate when the phenotype is atypical (e.g. arthrogryposis + connective-tissue features without aortopathy).
3. **Genome sequencing (WGS)** — adds value for regulatory/UTR variants (relevant given the ARVD1 UTR mechanism) and for structural variants.
4. **Exon-level CNV / deletion-duplication analysis** — required to detect the multi-exon deletion class ([PMID:32022420](https://pubmed.ncbi.nlm.nih.gov/32022420/)). Standard CMA may miss an intragenic exon 2–7 deletion depending on probe density.
5. **Targeted single-variant testing** — the correct and cheapest test for **cascade screening** in a family with a known variant, and specifically for the Belgian founder allele in Campine-region families.
6. **Not indicated:** karyotype, FISH, mtDNA testing, repeat-expansion testing.

**Interpretive cautions:** many TGFB3 missense variants are VUS; the same variant may carry conflicting ClinVar assertions across submitted conditions (rs796051886: Pathogenic for Rienhoff syndrome / VUS for hypertrophic cardiomyopathy); and ClinGen's **Limited** validity classification means a TGFB3 variant alone is weaker evidence for an HTAD diagnosis than a TGFBR1/2 variant would be.

### 10.2 Imaging (the surveillance backbone)

`[DB-RECORD / GeneReviews]`:
> "Echocardiography to monitor the status of the aortic root and ascending aorta (at least annually)"
> "magnetic resonance angiography or computerized tomography angiography to assess the entire arterial tree (at least every other year); more frequent imaging may be indicated based on genotype, family history, absolute vessel size or growth rate, or vascular pathology."

Reinforced by the 2025 LDS aneurysm characterisation study: comprehensive **head-to-pelvis** imaging is recommended, since 77 aneurysms were found in 43/103 LDS patients, 75% in arch vessels or cerebral circulation ([PMID:40533122](https://pubmed.ncbi.nlm.nih.gov/40533122/)). Note the nuance from a 2026 report that increased cervical vessel tortuosity in LDS is **not** associated with intracranial aneurysms ([PMID:42184884](https://pubmed.ncbi.nlm.nih.gov/42184884/)) — tortuosity is not a surrogate for aneurysm risk.

MAXO/ontology anchors: **MAXO:0010203** echocardiography; **MAXO:0035088** magnetic resonance angiography procedure. CTA — use the closest available NCIT procedure term.

Additional imaging: **cervical spine radiography/flexion-extension imaging** before any intubation or surgery, given cervical spine instability (HP:0010646); spine radiography for scoliosis; DXA is not indicated.

### 10.3 Laboratory tests and biomarkers

- **There is no diagnostic laboratory test, enzyme assay, or validated circulating biomarker for LDS5.** Diagnosis is genetic plus clinical/imaging. Explicit gap — do not populate a biochemical marker block without primary evidence.
- **Electrophysiology:** ECG is standard cardiac assessment; conduction abnormalities requiring pacemakers were observed in the founder cohort. Note the ARVD1 allelic disorder gives a rationale for ECG attention, though ARVD1 arises from UTR rather than coding variants.
- **Functional/other:** EMG and muscle biopsy have a role only in the arthrogryposis/low-muscle-mass presentation, and their value is largely **exclusionary** — the index biopsy showed normal architecture with disuse-type type 1 fibre predominance and "no evidence of chronic dystrophic or inflammatory changes," excluding a primary dystrophy.

### 10.4 Histopathology

Aortic wall in TGF-β pathway HTAD shows **medial degeneration** with elastic-fibre fragmentation and VSMC loss; immunohistochemistry in TGFB3 patients demonstrated **increased phospho-SMAD2 and up-regulated TGF-β ligand expression** — the "paradoxical up-regulation of both canonical and noncanonical TGF-β signaling" of the 2015 abstract. Single-cell RNA-seq of LDS aortic tissue is now available for the subtype comparison ([PMID:40923070](https://pubmed.ncbi.nlm.nih.gov/40923070/)).

### 10.5 Omics-based diagnostics

**None in clinical use for this disease.** RNA-seq has a plausible role in resolving the splice-variant class (c.754+2T>C, c.926+2T>C) but no published diagnostic RNA study for TGFB3 exists. No proteomic, metabolomic, epigenomic or liquid-biopsy diagnostic.

### 10.6 Clinical criteria and differential diagnosis

There are **no LDS5-specific diagnostic criteria.** Diagnosis follows the LDS framework (molecular + clinical). Key differentials and discriminators:

| Condition | Discriminating features |
|---|---|
| **Marfan syndrome** (FBN1) | Marfan has **ectopia lentis** (absent in LDS5) and more pronounced skeletal overgrowth; LDS has bifid uvula/cleft palate and arterial tortuosity. GeneReviews notes LDS dissection occurs at smaller diameters |
| **LDS 1–4** (TGFBR1, TGFBR2, SMAD3, TGFB2) | Earlier onset, higher penetrance, more aggressive arterial disease, more prominent tortuosity/craniosynostosis; **TGFB3 is the mildest** |
| **Shprintzen–Goldberg syndrome** (SKI) | SGS has "near-uniform incidence of developmental delay" and craniosynostosis; LDS has more aggressive arterial disease and **craniosynostosis is absent** in TGFB3 patients |
| **Vascular EDS** (COL3A1) | Arterial/bowel/uterine rupture, thin translucent skin, no bifid uvula/skeletal overgrowth |
| **Arterial tortuosity syndrome** (SLC2A10) | Extreme generalised tortuosity, AR inheritance |
| **Distal arthrogryposis syndromes** (TNNI2, TNNT3, MYH3, TPM2, etc.) | Relevant differential for the *index-case* presentation; no aortopathy or bifid uvula |
| **Nonsyndromic familial TAAD** (ACTA2, MYH11, MYLK, PRKG1) | Absence of syndromic craniofacial/palatal features |
| **ARVD1** | Allelic at TGFB3 but a distinct cardiomyopathy phenotype from UTR variants |

### 10.7 Screening

- **Cascade (targeted-variant) family screening** is the highest-yield screening intervention — imperative given the 41% asymptomatic carrier fraction. ClinGen rates LDS actionability **Strong** for both adult and paediatric populations.
- **Newborn screening: not applicable** (no biochemical marker, no urgent neonatal intervention).
- **Population carrier screening: not indicated** (ultra-rare, dominant, private alleles).
- **Prenatal and preimplantation testing:** `[DB-RECORD / GeneReviews]` "If the LDS-related pathogenic variant(s) have been identified in an affected family member, prenatal and preimplantation genetic testing are possible."

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

**The most striking prognostic finding is the absence of deaths in the largest dedicated cohort.** `[ABSTRACT-VERBATIM / PMID:39653386]` documents that "68% of the entire cohort remains free of aortic disease" with no deaths in 34 individuals. Combined with the founder cohort's carriers surviving to ages 80 and 84 with only mild aortic dilation, this positions LDS5 as substantially more benign than TGFBR1/2-related LDS.

- **No 5-/10-year survival estimate specific to TGFB3 exists.** For contrast within LDS (from surgically treated patients, [PMID:40923070](https://pubmed.ncbi.nlm.nih.gov/40923070/)): "Estimated 5- and 10-year survivals for TGFBR1/2 patients were 97% (99%-82%) and 86% (96%-61%)" with aortic events in 17–28%; for SMAD3, "estimated survival was 94% (99%-63%) at both 5 and 10 years, and estimated incidence of aortic events at both 5- and 10-year follow-ups was 0%."
- **Life expectancy:** likely near-normal with surveillance and timely repair; not formally quantified. Untreated risk is dominated by the low-probability, high-lethality dissection event.
- **Disease-specific mortality:** not quantified; aortic dissection/rupture is the mechanism of concern, plus uterine rupture in pregnancy.

### 11.2 Morbidity and function

- Surgical morbidity (Bentall/aortic root replacement, staged endovascular and open peripheral aneurysm repair — [PMID:39450604](https://pubmed.ncbi.nlm.nih.gov/39450604/)); lifelong anticoagulation where a mechanical valve is used.
- Skeletal morbidity: scoliosis, disc herniation, osteoarthritis, cervical instability, Dupuytren disease.
- Speech/feeding morbidity from cleft palate; motor disability in the arthrogrypotic presentation (independent ambulation at 24 months in the index case, with persistent weakness).
- Reproductive morbidity: aortic dissection and **uterine rupture** risk in pregnancy.
- **No formal disability outcome data and no QoL instrument data for LDS5.** Gap.

### 11.3 Prognostic factors

Data-supported: **age** (risk rises with decades), **male sex** (all four founder-cohort TAAD events), **aortic diameter and Z-score**, **growth rate ≥0.3 cm/year** (2022 ACC/AHA HTAD definition of rapid growth), **presence of bicuspid aortic valve**, **hypertension/smoking**, **family history of dissection**, and **genotype** (TGFB3 confers lower risk than TGFBR1/2). For extra-aortic aneurysms: "17% of AAs enlarged over time, and 38% of AAs that enlarged led to clinical events" ([PMID:40533122](https://pubmed.ncbi.nlm.nih.gov/40533122/)).

**No molecular prognostic biomarker is validated.**

---

## 12. Treatment

No disease-specific or disease-modifying therapy exists. Management is the LDS/HTAD paradigm, **gene-adjusted to reflect TGFB3's milder course.**

### 12.1 Pharmacotherapy

`[DB-RECORD / GeneReviews]`: "Angiotensin receptor blockers, beta-adrenergic receptor blockers, or other medications are used to reduce hemodynamic stress," with the important caveat that "No clinical trials evaluating efficacy of beta-blockers vs ARBs have been completed in persons with LDS."

| Agent class | Example agents (CHEBI, OAK-verified) | Rationale / status |
|---|---|---|
| Angiotensin receptor blocker | **losartan CHEBI:6541**; irbesartan **CHEBI:5959** | Reduces haemodynamic stress; mechanistic rationale of attenuating TGF-β signalling; extrapolated from Marfan trials |
| Beta-adrenergic blocker | **atenolol CHEBI:2904**; **propranolol CHEBI:8499**; celiprolol (CHEBI has only the hydrochloride, **CHEBI:31385**) | Reduces dP/dt and wall stress |
| Antihypertensives generally | — | BP control as a modifier-directed intervention |

Suggested treatment annotation shape: `treatment_term` = **NCIT:C15986** Pharmacotherapy, with `therapeutic_agent` bound to the CHEBI terms above and `therapeutic_modality: SMALL_MOLECULE`.

**A specific negative result worth curating.** `[FULL-TEXT / PMID:23824657]`, on the index patient's neuromuscular phenotype:
> "A 3-year trial of losartan at a dose of up to 2.0 mg/kg/day produced no change in muscle strength or mass."

This is genuine `supports: REFUTE`-grade evidence that ARB therapy does not address the myopathic/low-muscle-mass arm — it is an aortic-protection strategy only.

**Pharmacogenomics:** no CPIC/PharmGKB guideline relevant to TGFB3. None applicable.

### 12.2 Surgical and interventional

**Gene-specific thresholds — the single most actionable TGFB3-specific management fact.**

`[DB-RECORD / GeneReviews]`:
> "For *TGFB3*-related LDS, consider surgical repair of ascending aorta once maximal dimension approaches 5 cm."

This is deliberately **higher** than for other LDS genes (≈4.0 cm for TGFBR1/TGFBR2 in adolescents/adults; ≈4.5 cm for SMAD2/SMAD3/TGFB2). The Montalcino authors reach the same conclusion independently: they "recommend a larger aortic size threshold for prophylactic surgery in TGFB3-related cases versus TGFBR1 or TGFBR2 variants."

**Pre-pregnancy repair** — 2022 ACC/AHA Aortic Disease Guideline ([PMID:36334952](https://pubmed.ncbi.nlm.nih.gov/36334952/)): surgery prior to pregnancy is reasonable in patients with LDS attributable to pathogenic variants in **TGFB2 or TGFB3 and aortic diameter ≥4.5 cm**.

Procedures: aortic root replacement (valve-sparing or Bentall), ascending aortic replacement, arch/descending repair, and peripheral aneurysm repair — the 2025 case report documents staged internal-iliac coiling + EVAR for a giant common iliac aneurysm plus open repair of a true deep femoral artery aneurysm in an LDS type V patient ([PMID:39450604](https://pubmed.ncbi.nlm.nih.gov/39450604/)). Also cleft palate repair, scoliosis correction, cervical spine stabilisation, hernia repair.

Ontology: **MAXO:0000004** surgical procedure (or NCIT:C15329 Surgical Procedure / NCIT:C16186 Orthopedic Surgical Procedure); `therapeutic_modality: SURGERY`.

### 12.3 Advanced therapeutics

**None.** No gene therapy, gene editing, cell therapy, RNA-based therapy (ASO/siRNA), targeted small molecule, or immunotherapy exists or is in trial for TGFB3-related disease. TGF-β pathway modulation is conceptually attractive but hazardous given the paradoxical-signalling biology (direction of desired intervention is not established). Emerging strategies are surveyed in the 2026 preclinical modelling review ([PMID:42380922](https://pubmed.ncbi.nlm.nih.gov/42380922/)).

### 12.4 Supportive, rehabilitative, and lifestyle

- Physical/occupational therapy for contractures and weakness (**MAXO:0000011** physical therapy; MAXO:0001351 occupational therapy); speech therapy post-cleft-repair (MAXO:0000930).
- Nutritional support for failure to thrive (**MAXO:0000009** nutrition intervention).
- **Activity restriction** `[DB-RECORD / GeneReviews]`: avoid "Contact sports, competitive sports, and isometric exercise" and cardiovascular stimulants including routine decongestants and triptans; **moderate aerobic activity is permitted.**
- **Anaesthetic precautions:** cervical spine instability mandates pre-operative cervical imaging and careful airway management — a frequently overlooked, high-consequence point.
- **Genetic counselling** (**MAXO:0000079**) — see §13.
- Supportive care generally: **MAXO:0000950**.

### 12.5 Experimental / trials

No interventional trial recruits TGFB3/LDS5 specifically. Relevant observational study: **[NCT05472519](https://clinicaltrials.gov/study/NCT05472519)** "Immunopathology of Loeys-Dietz Syndrome." Marfan/LDS ARB-vs-beta-blocker literature is the closest evidence base and does not include TGFB3-stratified results.

### 12.6 Treatment outcomes and adverse events

No TGFB3-specific response-rate or adverse-event data. Standard class effects apply (ARB: hypotension, hyperkalaemia, renal function change, fetal toxicity — the last being important in a population where pregnancy planning is central; beta-blocker: bradycardia, fatigue, bronchospasm). Surgical outcomes are extrapolated from LDS cohorts.

### 12.7 Treatment algorithm

1. Confirm molecularly (HTAD panel / WES) → classify the variant.
2. Baseline echo + head-to-pelvis CTA/MRA; cervical spine imaging.
3. Start beta-blocker and/or ARB.
4. Annual echo; whole-arterial-tree cross-sectional imaging at least every other year (more often per growth rate/family history).
5. Cascade-test at-risk relatives with the family variant; enrol carriers in surveillance regardless of symptoms.
6. Refer for prophylactic ascending aortic repair as the maximal dimension **approaches 5 cm** (or ≥4.5 cm before a planned pregnancy).
7. Pre-conception counselling; intensified imaging during pregnancy and in the weeks postpartum.
8. Lifelong activity and stimulant counselling; multidisciplinary aortic team.

---

## 13. Prevention

**Primary prevention** — the disease itself cannot be prevented (germline). Preventable is the *event*: BP control, tobacco avoidance, lipid management, avoidance of isometric strain and cardiovascular stimulants, and pre-pregnancy risk mitigation. Reproductive primary prevention is available via **preimplantation genetic testing** and **prenatal diagnosis** when the family variant is known `[DB-RECORD / GeneReviews]`.

**Secondary prevention** — the core of care: **cascade genetic testing** of first-degree relatives (ClinGen actionability **Strong**), followed by lifelong imaging surveillance to detect dilation before dissection. Given that 41% of founder-variant carriers were phenotypically normal, **phenotype-based ascertainment is inadequate — genotype-first cascade testing is the only reliable route.**

**Tertiary prevention** — prophylactic aortic repair at the gene-adjusted threshold; surveillance of the residual arterial tree after repair (17% of extra-aortic aneurysms enlarge; 38% of those cause events); scoliosis and cervical spine management; peri-operative airway precautions.

**Immunisation** — not applicable to disease prevention; routine immunisation per age. (Endocarditis prophylaxis considerations follow standard valve/prosthesis guidance, not LDS-specific rules.)

**Screening programmes** — no population or newborn screening is indicated or justified.

**Risk stratification** — by genotype (TGFB3 < TGFBR1/2), age, sex, aortic diameter/Z-score, growth rate, BAV status, family history of dissection, and cardiovascular risk factors.

**Genetic counselling** — must convey: autosomal dominant transmission with 50% recurrence per child; **incomplete, age-dependent penetrance with a large asymptomatic-carrier fraction**; marked intrafamilial variability; the aortic and uterine risks of pregnancy; and the availability of prenatal/PGT options. The conflict between the GeneReviews "near 100% penetrance" statement and the TGFB3 cohort data should be disclosed explicitly rather than smoothed over.

**Public health / environmental interventions** — not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens* **NCBITaxon:9606** for the disease. Experimental orthologue work is in *Mus musculus* **NCBITaxon:10090** and *Xenopus laevis* **NCBITaxon:8355** (the assay system in the founding paper).
- **Orthologous genes:** mouse *Tgfb3* (MGI); rat *Tgfb3*; zebrafish *tgfb3*; chicken *TGFB3*. TGF-β3 is deeply conserved across vertebrates, and the cystine-knot cysteine mutated in the index case is conserved across the entire TGFB ligand family `[FULL-TEXT / PMID:23824657]`.
- **Naturally occurring disease in other species:** **none identified.** A targeted search did not surface an OMIA entry for a naturally occurring TGFB3 variant causing a connective-tissue or aortopathy phenotype in dogs, cattle, horses or other species. Record as **not documented in this search** rather than as absent — an OMIA browse (omia.org) keyed on the TGFB3 orthologue would be the definitive check and remains an open task.
- **Breed:** no VBO-identified breed predisposition known.
- **Veterinary relevance:** none established.
- **Comparative pathology:** the mouse null recapitulates the **cleft palate** and **lung** phenotypes but **not** the aortopathy (§15), so cross-species conservation is *partial* — the palatogenesis function is conserved and modellable; the vascular function in the heterozygous state is not captured by existing models.
- **Zoonotic potential / cross-species transmission:** not applicable (Mendelian disorder).

---

## 15. Model Organisms

### 15.1 Mouse — the foundational genetic models (1995)

Two independent *Tgfb3*-null lines were reported back-to-back in *Nature Genetics*, December 1995:

- **Kaartinen et al.** ([PMID:7493022](https://pubmed.ncbi.nlm.nih.gov/7493022/), *Nat Genet* 11(4):415–21) — homozygous *Tgfb3*−/− mice `[ABSTRACT-VERBATIM]` "die with unique and consistent phenotypic features including delayed pulmonary development and defective palatogenesis," notably **without** other craniofacial abnormalities, implicating defective **epithelial–mesenchymal interaction**.
- **Proetzel et al.** ([PMID:7493021](https://pubmed.ncbi.nlm.nih.gov/7493021/), *Nat Genet* 11(4):409–14) — "Transforming growth factor-beta 3 is required for secondary palate fusion." Exon 6 replaced by neo. **Heterozygotes had no apparent phenotype**; homozygotes had **incompletely penetrant** failure of palatal shelf fusion, from "impaired adhesion of the apposing medial edge epithelia of the palatal shelves" and failure to eliminate the midline epithelial seam.

**Model type:** constitutive germline knockout (mammalian, in vivo). Available via MGI/IMSR; downstream *Tgfb3* mutant alleles and conditional lines have since been generated, and palatal transcriptomes of *Tgfb3* mutants have been profiled (e.g. *Sci Rep* 2020, "Transcriptional analysis of cleft palate in TGFβ3 mutant mice").

### 15.2 Phenotype recapitulation — and the central limitation

| Human feature | Mouse *Tgfb3*−/− | Verdict |
|---|---|---|
| Cleft palate / bifid uvula | **Yes** (incompletely penetrant, strain-dependent) | **Recapitulated** |
| Pulmonary development | Delayed (mouse-specific finding; not a prominent human LDS5 feature) | Divergent |
| Aortic aneurysm / dissection | **Not reported** | **Not recapitulated** |
| Low muscle mass / arthrogryposis | Not reported | Not recapitulated |
| **Heterozygous (human-equivalent) genotype** | **"heterozygotes had no apparent phenotypic change"** | **Critical mismatch** |

This is a textbook `HUMAN_MODEL_MISMATCH` rather than a plain knowledge gap: evidence exists in the model, but its translational validity to human heterozygous disease is the open question. The human disease is a **heterozygous, adult-onset aortopathy**; the mouse heterozygote is normal and the homozygote dies perinatally of a palatal/pulmonary phenotype. Consequently **no mouse model of TGFB3-related aortopathy currently exists**, and the mouse cannot presently be used to test aortic-protective interventions for LDS5. Mouse genetic background, sex, and variant-specific (as opposed to null) effects are flagged as key variables in the 2026 review ([PMID:42380922](https://pubmed.ncbi.nlm.nih.gov/42380922/)) — a knock-in of a human missense allele (e.g. p.Asp263His at the RGD motif or p.Cys409Tyr) rather than a null is the obvious missing model.

### 15.3 Xenopus — the functional assay system

The index-case functional work used *Xenopus laevis* embryo RNA co-injection to establish dominant-negative-like interference: a 1:1 mutant:wild-type ratio reduced pSMAD2 to ~40% and pERK1/2 to ~60% of control, with no effect on pSMAD1 or dorsoventral patterning (i.e. BMP signalling spared) `[FULL-TEXT / PMID:23824657]`. This is an *in vivo* signalling-readout assay, not a disease model.

### 15.4 In vitro / cellular systems

- **293T cells** — expression/secretion analysis by immunoprecipitation and western blot: mutant TGFB3-C409Y is secreted but non-functional.
- **HeLa p3TPLux reporter assay** — the mutant construct "produced no transcriptional signal versus robust wild-type response" `[FULL-TEXT]`.
- **Patient aortic tissue** — the source of the paradoxical pSMAD2/ligand up-regulation finding (2015) and of the LDS single-cell transcriptomic atlas (2025, [PMID:40923070](https://pubmed.ncbi.nlm.nih.gov/40923070/)).
- **Patient quadriceps biopsy** — histology excluding dystrophy.
- **No published iPSC or organoid model of TGFB3-related disease.** Given the established VSMC-differentiation iPSC platforms used for other LDS genes, this is a tractable gap.

### 15.5 Zebrafish

A zebrafish LDS model exists but targets a **different** gene — *tgfbr2b* knockdown ([*J Hum Genet* 2026](https://www.nature.com/articles/s10038-026-01457-y)). **No zebrafish *tgfb3* aortopathy model** is reported.

### 15.6 Research applications and resources

Usable today: palatogenesis and EMT biology; TGF-β3 ligand maturation/activation biochemistry (furin cleavage, integrin/RGD activation); structural biology of the cystine knot (PDB 1TGJ, 8VS6/8VSB full-length cryo-EM, 9FK5); the TGF-β paradox in aortic tissue. Not yet possible: preclinical testing of aortic-protective therapy in a TGFB3 genotype.

Databases: **MGI** and **IMSR** (mouse *Tgfb3* alleles), **Alliance of Genome Resources**, **ZFIN**, **Xenbase**, **IMPC**, **MMRRC/KOMP/EMMA** for line availability; **Cellosaurus** for the cell lines used.

---

## Curation Guidance and Explicit Gaps

**Highest-value, defensible claims for a KB entry**
1. TGFB3 is the causal gene; heterozygous, autosomal dominant; MONDO:0014262 / OMIM 615582 (`[ABSTRACT-VERBATIM]` snippets available from PMID:25835445, 23824657, 39653386, 37719708, 32022420, 26184463).
2. LDS5 is the **mildest, latest-onset, least penetrant** LDS subtype — with three independent quantitative supports (Montalcino 68% aortic-disease-free; founder cohort 15% TAAD and 41% unaffected; GeneReviews "Mildest form of LDS").
3. The gene-adjusted **~5 cm** surgical threshold, and **≥4.5 cm pre-pregnancy** (2022 ACC/AHA) — the most clinically consequential TGFB3-specific facts.
4. Mechanism: ligand loss/mis-maturation → paradoxical up-regulation of canonical and non-canonical TGF-β signalling in the aortic wall (`conforms_to: aortopathy_tgfbeta_dysregulation#TGF-beta Signaling Dysregulation`); plus a parallel EMT-dependent developmental arm for palate and muscle.
5. Belgian founder allele p.(Asp263His) with a ~22-generation MRCA — a clean `Prevalence`/population-genetics record.

**Do not assert without further verification**
- gnomAD pLI 1 / LOEUF 0.25 (secondary source only).
- "Aortic dilation 42% / aneurysm 16% / dissection 12%" (secondary summary of the literature review).
- Eosinophilic esophagitis and asthma as **TGFB3** phenotypes — these trace to TGFBR1/TGFBR2 biology ([PMID:23884466](https://pubmed.ncbi.nlm.nih.gov/23884466/)) and to the LDS-umbrella HPO annotation set.
- Bertoli-Avella's per-feature percentages (the abstract gives counts of patients/families, not a feature-frequency table; the full text was not retrievable in this session — the JACC, Radboud and Leiden repository copies all returned HTTP 403 or exceeded size limits).
- Any de novo rate for TGFB3 specifically (the 75% figure is LDS-wide and almost certainly wrong for TGFB3).

**Documented data gaps**
Prevalence/incidence · quality-of-life and disability outcomes · validated biomarkers · metabolomics/proteomics/lipidomics · epigenetics · a heterozygous mouse (or any) aortopathy model · iPSC/organoid models · TGFB3-stratified drug-efficacy data · OMIA/natural animal disease confirmation · resolution of the loss-of-function vs codon-300 gain-of-function dispute · the stale MONDO/OMIM definition clause asserting absence of arterial tortuosity.

---

## Sources

- [OMIM #615582 — Loeys-Dietz syndrome 5 (LDS5)](https://omim.org/entry/615582)
- [OMIM *190230 — TGFB3](https://omim.org/entry/190230)
- [Rienhoff et al. 2013, Am J Med Genet A — PMID:23824657](https://pubmed.ncbi.nlm.nih.gov/23824657/) · [full text PMC3885154](https://pmc.ncbi.nlm.nih.gov/articles/PMC3885154/)
- [Bertoli-Avella et al. 2015, JACC — PMID:25835445](https://pubmed.ncbi.nlm.nih.gov/25835445/) · [JACC](https://www.jacc.org/doi/10.1016/j.jacc.2015.01.040)
- [Matyas et al. 2014, Am J Med Genet A — PMID:24798638](https://pubmed.ncbi.nlm.nih.gov/24798638/) · [Rienhoff response — PMID:24817670](https://pubmed.ncbi.nlm.nih.gov/24817670/)
- [Kuechler et al. 2015 — PMID:26184463](https://pubmed.ncbi.nlm.nih.gov/26184463/)
- [Schepers et al. 2018, Hum Mutat — PMC5947146](https://pmc.ncbi.nlm.nih.gov/articles/PMC5947146/) · [Wiley](https://onlinelibrary.wiley.com/doi/10.1002/humu.23407)
- [Mégarbané et al. 2020, Am J Med Genet A — PMID:32022420](https://pubmed.ncbi.nlm.nih.gov/32022420/)
- [Vanhoutte et al. 2023, Front Genet (Belgian TGFB3 founder variant) — PMID:37719708](https://pubmed.ncbi.nlm.nih.gov/37719708/) · [full text PMC10500191](https://pmc.ncbi.nlm.nih.gov/articles/PMC10500191/) · [Frontiers](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2023.1251675/full)
- [Lim et al. 2025, J Med Genet — Montalcino Aortic Consortium TGFB3 cohort — PMID:39653386](https://pubmed.ncbi.nlm.nih.gov/39653386/)
- [Koefoed et al. 2025, JACC — Characterization of Arterial Aneurysms in LDS — PMID:40533122](https://pubmed.ncbi.nlm.nih.gov/40533122/)
- [Pedroza et al. 2025, JTCVS Open — LDS subtypes / aortic scRNA-seq — PMID:40923070](https://pubmed.ncbi.nlm.nih.gov/40923070/)
- [Preclinical modeling of Loeys-Dietz syndrome, Orphanet J Rare Dis 2026 — PMID:42380922](https://pubmed.ncbi.nlm.nih.gov/42380922/)
- [Cervical vessel tortuosity in LDS and intracranial aneurysms, 2026 — PMID:42184884](https://pubmed.ncbi.nlm.nih.gov/42184884/)
- [Sex-based differences in LDS, Int J Cardiol 2025 — PMID:40482834](https://pubmed.ncbi.nlm.nih.gov/40482834/)
- [LDS type V giant iliac + deep femoral artery aneurysm repair, Acta Chir Belg 2025 — PMID:39450604](https://pubmed.ncbi.nlm.nih.gov/39450604/)
- [Heterozygous TGFB3 variant, atypical LDS (c.427A>T, p.Arg143*), Ann Intern Med Clin Cases 2023](https://www.acpjournals.org/doi/10.7326/aimcc.2023.0035)
- [Beffagna et al. 2005, Cardiovasc Res — TGFB3 regulatory mutations in ARVD1 — PMID:15639475](https://pubmed.ncbi.nlm.nih.gov/15639475/)
- [Kaartinen et al. 1995, Nat Genet — PMID:7493022](https://pubmed.ncbi.nlm.nih.gov/7493022/) · [Nature Genetics](https://www.nature.com/articles/ng1295-415)
- [Proetzel et al. 1995, Nat Genet — PMID:7493021](https://pubmed.ncbi.nlm.nih.gov/7493021/)
- [Frischmeyer-Guerrerio et al. 2013, Sci Transl Med — PMID:23884466](https://pubmed.ncbi.nlm.nih.gov/23884466/)
- [TGFB3 parent-of-origin effects in nonsyndromic cleft lip/palate — PMID:18480962](https://pubmed.ncbi.nlm.nih.gov/18480962/)
- [2022 ACC/AHA Guideline for the Diagnosis and Management of Aortic Disease — PMID:36334952](https://pubmed.ncbi.nlm.nih.gov/36334952/) · [Circulation](https://www.ahajournals.org/doi/10.1161/CIR.0000000000001106)
- [GeneReviews: Loeys-Dietz Syndrome (NBK1133)](https://www.ncbi.nlm.nih.gov/books/NBK1133/)
- [MedGen 816342 — Rienhoff syndrome](https://www.ncbi.nlm.nih.gov/medgen/816342) · [GTR condition C3810012](https://www.ncbi.nlm.nih.gov/gtr/conditions/C3810012/)
- [ClinGen TGFB3 curation results (HGNC:11769)](https://search.clinicalgenome.org/kb/genes/HGNC:11769)
- [ClinVar RCV003050507 — TGFB3 c.427A>T (p.Arg143Ter) / Rienhoff syndrome](https://www.ncbi.nlm.nih.gov/clinvar/RCV003050507/) · [dbSNP rs796051886](https://www.ncbi.nlm.nih.gov/snp/rs796051886)
- [UniProt P10600 — TGFB3_HUMAN](https://rest.uniprot.org/uniprotkb/P10600.txt)
- [Orphanet: TGFB3 gene page](https://www.orpha.net/en/disease/gene/TGFB3) · [ORPHA:60030 Loeys-Dietz syndrome](http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=60030) (also available locally as `references_cache/ORPHA_60030.md`, Orphadata snapshot 2025-12-09, CC-BY 4.0)
- [VASCERN TGFB3 gene compendium (Loeys & Verstraeten, 2023)](https://vascern.eu/app/uploads/2023/11/TGFB3-Gene-Compendium.pdf) — *listed for completeness; both mirrors returned HTTP 403 in this session and its contents are not incorporated above*
- [NCT05472519 — Immunopathology of Loeys-Dietz Syndrome](https://clinicaltrials.gov/study/NCT05472519)
- [SLC44A2-mediated VSMC phenotypic switch in aortic aneurysm, J Clin Invest 2024 — PMID:39145443](https://pubmed.ncbi.nlm.nih.gov/39145443/)
- [Zebrafish LDS model via tgfbr2b knockdown, J Hum Genet 2026](https://www.nature.com/articles/s10038-026-01457-y)

---

**One process note.** All HPO, GO, CL, UBERON, CHEBI and MAXO identifiers above were verified against the local OAK adapters in this repository, so labels match canonical ontology labels. Three cautions surfaced during verification: `GO:0060389` (pathway-restricted SMAD protein phosphorylation) and `GO:0005615` (extracellular space) are **obsolete** in the current GO release and should not be used; and `HP:0002617` is labelled **"Vascular dilatation"**, not "Dilatation" as the Orphanet table renders it.
