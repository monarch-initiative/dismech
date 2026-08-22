---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-03T01:06:33.418059'
end_time: '2026-08-03T01:12:10.959031'
duration_seconds: 337.54
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: IREB2-Related Neurodegeneration
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
  web_search_requests: 26
  num_turns: 31
  total_cost_usd: 2.037688
  session_id: ccfe4e45-02a4-514e-bba5-3af1e8db647b
  stop_reason: end_turn
citation_count: 17
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IREB2-Related Neurodegeneration
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **IREB2-Related Neurodegeneration** covering all of the
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

# IREB2-Related Neurodegeneration (Neurodegeneration, Early-Onset, with Choreoathetoid Movements and Microcytic Anemia — NDCAMA): Comprehensive Research Report

## 1. Disease Information

**Overview.** IREB2-related neurodegeneration — formally designated **NDCAMA (Neurodegeneration, Early-onset, with Choreoathetoid Movements and Microcytic Anemia)** — is an ultra-rare, autosomal recessive, early-onset neurodevelopmental/neurodegenerative disorder caused by biallelic loss-of-function or hypomorphic variants in **IREB2**, the gene encoding **Iron Regulatory Protein 2 (IRP2)**. IRP2 is a cytosolic RNA-binding protein that post-transcriptionally controls cellular iron homeostasis by binding iron-responsive elements (IREs) in the untranslated regions of mRNAs encoding ferritin (FTH1/FTL), transferrin receptor (TFRC), ferroportin, and other iron-metabolism proteins. Loss of IRP2 produces a state of **functional/cytosolic iron deficiency despite normal or elevated body iron stores**, with downstream mitochondrial dysfunction (particularly loss of iron-sulfur-cluster-containing respiratory chain subunits) that is thought to drive progressive neurodegeneration, severe developmental impairment, extrapyramidal movement disorder, and a distinctive microcytic, iron-refractory anemia.

The disorder was first described in humans in 2019 (Costain et al., *Brain*) and remains exceedingly rare — as of the most recent literature (2024–2025) only **~5 patients from ~4 unrelated families** worldwide have been reported (Filipino, Australian, US, and two Chinese kindreds).

**Key identifiers:**
- **OMIM phenotype:** #618451 — "NEURODEGENERATION, EARLY-ONSET, WITH CHOREOATHETOID MOVEMENTS AND MICROCYTIC ANEMIA; NDCAMA" ([OMIM 618451](https://omim.org/entry/618451))
- **OMIM gene:** *147582 — IRON-RESPONSIVE ELEMENT-BINDING PROTEIN 2; IREB2 ([OMIM 147582](https://www.omim.org/entry/147582))
- **MONDO:** MONDO:0032871 (NDCAMA) — recommend independent verification against the live MONDO API before curation
- **MedGen Concept ID:** C5193104 ([MedGen](https://www.ncbi.nlm.nih.gov/medgen/1676579))
- **Gene:** IREB2, HGNC:6115, NCBI Gene ID: 3658, chromosome **15q25.1** (GRCh38: chr15:78,437,431–78,501,453)
- **Inheritance:** Autosomal recessive
- **Orphanet:** No dedicated ORPHA number was confidently identified in this search sweep given the disease's very recent (2019+) description; this should be checked directly against the live Orphanet API before curation, as Orphanet coverage of ultra-recently-described Mendelian disorders often lags OMIM by 1–3 years.
- **Synonyms:** NDCAMA; IRP2 deficiency; IREB2-associated neurodegeneration; IRP2-related neurodevelopmental disorder

**Distinction from a common naming trap:** IREB2 is separately and much more prominently known in the literature as a **COPD/lung-cancer GWAS susceptibility locus** at chromosome 15q25 (in linkage disequilibrium with the CHRNA3/CHRNA5/CHRNB4 nicotinic receptor cluster) — see Section 5. This GWAS association is a *distinct* line of evidence (common noncoding variants, complex/polygenic trait) from the Mendelian neurodegenerative syndrome described here (rare biallelic coding variants causing complete or partial IRP2 loss of function). Curators should keep these evidence streams clearly separated in any pathophysiology model — they converge on the same gene but are mechanistically and clinically distinct entities.

**Evidence basis:** All disease-level clinical information is derived from **individual patient case reports/series** (5 published patients across 4 families) plus supporting **mouse and cellular model organism data** — this is not yet an aggregated disease-level resource (no large natural-history cohort exists given the rarity).

---

## 2. Etiology

**Disease Causal Factors:** Purely genetic/monogenic. Biallelic (homozygous or compound heterozygous) pathogenic variants in *IREB2* causing loss or severe reduction of IRP2 protein/function are necessary and sufficient to cause the disease. There is no known environmental, infectious, or purely mechanistic (non-genetic) causal contributor to the Mendelian syndrome itself.

**Genetic risk factors:**
- Biallelic *IREB2* variants (nonsense, missense, in-frame deletion) — see Section 4 for the full variant catalog.
- All reported cases are compound heterozygous except where consanguinity/founder effects might predispose to homozygosity (not explicitly reported in the literature reviewed).
- No modifier genes have yet been identified, though **IRP1 (ACO1)** functions as a partial, incomplete compensatory paralog — patients and *Ireb2*−/− mice show ~2-fold upregulation of IRP1 IRE-binding activity that is insufficient to normalize iron metabolism (Costain et al. 2019, PMID:30915432; Maio et al. 2022, PMID:35602653).

**Environmental risk factors:** None established for the Mendelian disorder. (By contrast, for the *unrelated* IREB2 COPD-susceptibility locus, cigarette smoking is a major environmental modifier/gene-environment interaction — see Section 5.)

**Protective factors:** None specific to the Mendelian syndrome are established in humans. In the *Ireb2*−/− mouse model, dietary **TEMPOL** (a stable nitroxide) activates latent IRE-binding activity of the paralog IRP1, converting it from its aconitase form to an IRE-binding form, and this "rescues" the neurodegenerative/neuromuscular phenotype (though not the anemia) — this is a pharmacological/experimental protective intervention, not a naturally occurring protective genetic or environmental factor (Ghosh et al. 2008, PNAS, PMID:18685102).

**Gene-environment interactions:** Not established for the Mendelian NDCAMA phenotype. For the distinct IREB2 COPD locus, gene-environment interaction with smoking is well documented (see Section 5), and this is a useful point of *contrast* for dismech curation — the same gene/locus name, entirely different disease and etiologic model.

---

## 3. Phenotypes

Phenotype data below is synthesized across the 5 published human cases (Costain 2019, PMID:30915432; Cooper 2019, *Brain* 142:e40, DOI 10.1093/brain/awz183 — PMID not independently confirmed in this search sweep, please verify; Maio 2022, PMID:35602653; and the 2024 Chinese-pedigree report, DOI 10.1186/s13023-024-03465-7, PMID not independently confirmed — verify directly).

### Core/most-consistent phenotypes (reported in ≥4/5 patients)
| Phenotype | HPO suggestion | Notes |
|---|---|---|
| Global developmental delay / regression | HP:0001263 (Global developmental delay) | Onset in infancy in all reported cases |
| Choreoathetoid movement disorder | HP:0001266 (Choreoathetosis) | Defining/eponymous feature of NDCAMA |
| Dystonia | HP:0001332 (Dystonia) | Present in all reported cases; often progressive |
| Microcytic anemia, iron-refractory | HP:0001935 (Microcytic anemia); consider HP:0004840 (Refractory anemia) qualifier | Unresponsive to iron supplementation — a key diagnostic clue distinguishing this from true iron-deficiency anemia |
| Cerebral/cortical atrophy | HP:0002500 (Cerebral atrophy) or HP:0002120 (Cerebral cortical atrophy) | Progressive on serial MRI in Costain and Cooper cases |
| Spasticity | HP:0001257 (Spasticity) | |
| Seizures | HP:0001250 (Seizure) | Includes infantile spasms/hypsarrhythmia in the Maio 2022 patient (HP:0011097, Epileptic spasm) |
| Absent or minimal speech | HP:0001344 (Absent speech) or HP:0001348 (Poor speech) | |
| Non-ambulatory / impaired ambulation | HP:0002540 (Inability to walk) | |

### Additional reported features
- Microcephaly (HP:0000252) — OFC −2.6 SD in the Maio 2022 patient
- Peripheral neuropathy (HP:0009830)
- Pes cavus, bilateral (HP:0001761)
- Stereotypies (HP:0000733)
- Dysautonomia (HP:0002960)
- Optic nerve hypoplasia (HP:0000609) and cortical visual impairment (HP:0100704)
- Sensorineural and conductive hearing loss (HP:0000407, HP:0000405) — Cooper 2019 patient
- Recurrent infections / neutropenia episodes, oral ulcers, cyclic vomiting, feeding intolerance — Cooper 2019 patient (may represent a broader phenotypic spectrum or additional comorbidity — treat cautiously as n=1 findings)
- Thick corpus callosum with progressive cerebral atrophy (imaging finding) — Cooper 2019
- Non-specific facial dysmorphism — Cooper 2019
- Elevated zinc protoporphyrin IX — a laboratory marker of functional iron deficiency in erythroid precursors, reported in the Costain and Maio patients
- Elevated serum ferritin (paradoxically, despite functional iron deficiency) in the Cooper 2019 and 2024 Chinese-pedigree patients, versus low-normal ferritin in the Maio 2022 patient — **ferritin direction appears variant/patient-dependent** and should not be treated as a uniform diagnostic marker across all IREB2 genotypes.

**Onset:** All reported cases are **infantile-onset** (symptom onset from ~5 months to ~16 months of age), consistent with a severe, early pediatric neurodegenerative/neurodevelopmental disorder rather than an adult-onset process.

**Progression:** Progressive in all reported cases — cerebral atrophy worsens on serial imaging; one patient (Cooper 2019) died at age 10 of progressive neurological disease. The disorder should be modeled as **progressive** (`clinical_course: PROGRESSIVE`) rather than static, distinguishing it from cerebral palsy phenocopies despite the "dystonic cerebral palsy" label sometimes applied clinically before genetic diagnosis.

**Severity/frequency:** Given n=5 patients total, only qualitative frequency descriptors are appropriate (e.g., "reported in all/most published cases") rather than population percentages — standard FrequencyEnum quantitative bands are not well supported by the evidence base and should be used cautiously or omitted per dismech's frequency-evidence guidelines.

**Quality of life impact:** Severe — profound impairment of ambulation, communication, and functional independence reported in all surviving patients; no formal EQ-5D/SF-36 data exists given the pediatric, severely affected population and disease rarity.

---

## 4. Genetic/Molecular Information

**Causal gene:** IREB2 (HGNC:6115; NCBI Gene 3658; *147582; chr15q25.1). Encodes IRP2 (Iron Regulatory Protein 2), a 963-amino-acid, ~105 kDa cytosolic aconitase-family RNA-binding protein.

**Reported pathogenic variants (all biallelic, autosomal recessive):**

| Patient / Source | Allele 1 | Allele 2 | Zygosity | Consequence |
|---|---|---|---|---|
| Costain 2019 (Filipino, 16y) | c.1255C>T, p.Arg419Ter (R419X) | c.1069G>T, p.Gly357Ter (G357X) | Compound het | Complete IRP2 loss (protein undetectable by Western blot) |
| Cooper 2019 (Australian, died age 10) | p.Gly785Arg (maternal) | p.Ser444del (in-frame 3-nt deletion, paternal) | Compound het | Missense/in-frame deletion; Gly785Arg predicted to disrupt a major IRE–IRP contact point |
| Maio 2022 (7yo, US) | c.2240G>A, p.Gly747Glu (paternal) | c.656A>C, p.Glu219Ala (maternal) | Compound het | Missense; predicted mis-splicing/increased protein turnover; IRP2 mRNA and protein effectively undetectable |
| Chinese pedigree 2024 (8mo, China) | c.1111A>G, p.Ile371Val | c.2477A>T, p.Asp826Val | Compound het | Missense; p.Asp826Val causes marked proteasomal degradation of IRP2 |

**Classification (ACMG/AMP):** All reported variants have been treated as pathogenic/likely pathogenic based on segregation, absence/near-absence in population databases (gnomAD), functional evidence of loss of protein/function, and phenotype match — but formal ClinVar submission status should be checked directly (not confirmed in this search sweep).

**Variant type spectrum:** Nonsense (complete loss of function), in-frame deletion, and missense (destabilizing/mis-splicing) — i.e., the disease spectrum spans complete null alleles through severe hypomorphs, consistent with a loss-of-function mechanism of varying severity, which may partly explain phenotypic variability (e.g., complete-null Costain patient vs. hypomorphic missense patients).

**Population frequency:** Given only 4 known families, these variants are expected to be **absent or singleton in gnomAD**; no established carrier frequency or founder-population enrichment has been reported. gnomAD constraint metrics (pLI/LOEUF) for IREB2 itself were not independently confirmed in this search sweep — recommend a direct gnomAD browser query before citing a specific value.

**Functional consequences (mechanistically established across studies):**
- Loss/near-loss of IRP2 protein and complete loss of IRE-binding activity in patient-derived lymphoblasts
- Compensatory ~2-fold increase in IRP1 protein/IRE-binding activity — insufficient to normalize iron handling
- **Downregulation of TFRC** (reduced iron import) and **upregulation of ferritin (FTH1/FTL)** (increased iron sequestration) — the opposite of the expected response to cellular iron deficiency, i.e., a "misread" iron status
- Reduced labile (usable) cytosolic iron pool — a state of functional iron deficiency at the cellular level despite whole-body iron sufficiency/excess
- Reduced ferrochelatase levels
- **Mitochondrial dysfunction:** decreased Complex I (~28% of normal) and Complex II (~52% of normal) respiratory chain activity in patient fibroblasts, with reduced levels of Fe-S-cluster-containing subunits (NDUFS1, NDUFS8 in Complex I; SDHB in Complex II; UQCRFS1 in Complex III) and reduced assembly of Complexes I–V (Maio et al. 2022, PMID:35602653)
- **Functional rescue:** lentiviral re-expression of wild-type IREB2 in patient lymphoblasts normalizes TFRC/ferritin levels, IRE-binding activity, labile iron pool, and Complex I/II activity — strong causal confirmation (Costain 2019; Maio 2022)

**Modifier genes:** IRP1/ACO1 is the closest functional paralog and partial compensator, though not curated as a formal disease modifier gene in any published report. **OTUD3** (a deubiquitylase that stabilizes IRP2 in an iron-independent manner) is mechanistically relevant — *Otud3*-knockout mice show nigral iron accumulation and nigrostriatal dopaminergic degeneration resembling Parkinson's disease (Jia et al. 2022, *Cell Death Dis* 13:418, DOI 10.1038/s41419-022-04704-0; PMID not independently confirmed in this sweep) — relevant as a candidate genetic modulator of IRP2 abundance/stability but not itself an established modifier in human NDCAMA patients.

**Epigenetic information:** None specifically reported for this disorder.

**Chromosomal abnormalities:** Not applicable — this is a single-gene coding-variant disorder, not a copy-number/structural disorder.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious causal factors are established for the Mendelian NDCAMA phenotype itself.

**Important gene-level context (distinct entity):** IREB2 is one of the most replicated genes at the **chromosome 15q25 locus** in COPD and lung cancer genome-wide association studies, in strong linkage disequilibrium with the **CHRNA3/CHRNA5/CHRNB4** nicotinic acetylcholine receptor gene cluster (DeMeo et al. 2009, *Am J Hum Genet* 85:493–502, PMID:19800047; Pillai et al. 2009, *PLoS Genet*, GWAS identifying two major COPD susceptibility loci). Key mechanistic point for curators: *"the effect of variants in CHRNA3/5 appeared to largely be mediated by smoking, while a variant at IREB2 was associated with COPD independent of smoking"* — i.e., the IREB2 COPD association operates through a smoking-independent mechanism (plausibly related to iron-driven oxidative injury in airway epithelium — see Nature Medicine 2016, "Mitochondrial iron chelation ameliorates cigarette smoke–induced bronchitis and emphysema in mice"), distinguishing it from the nicotine-dependence-mediated CHRNA3/5 signal. **This is a separate disease entity (COPD, a common complex trait driven by common noncoding variants) from the Mendelian NDCAMA syndrome (driven by rare biallelic coding variants) and should not be conflated in the KB pathophysiology model**, though both converge on IRP2/iron-metabolism dysregulation as a shared mechanistic thread worth noting as a cross-reference.

**Infectious agents:** None implicated.

---

## 6. Mechanism / Pathophysiology

**Causal chain (established, human + mouse + cellular evidence):**

1. **Trigger:** Biallelic loss-of-function or hypomorphic *IREB2* variant → absent/reduced IRP2 protein and loss of IRE-binding activity
2. **Post-transcriptional iron-gene misregulation:** Failure to stabilize TFRC mRNA and failure to repress ferritin (FTH1/FTL) mRNA translation → **paradoxical downregulation of iron import (TFRC↓) and upregulation of iron sequestration (ferritin↑)**, despite the cell being in a state of cytosolic iron deficiency
3. **Functional/cytosolic iron deficiency:** Reduced labile iron pool available for iron-dependent enzymatic processes, even as total-body/serum iron indices may appear normal or elevated (a key diagnostic paradox — explains why the anemia is unresponsive to oral/parenteral iron supplementation)
4. **Mitochondrial Fe-S cluster biogenesis failure:** Reduced iron availability compromises assembly of iron-sulfur cluster-containing respiratory chain subunits (Complex I: NDUFS1, NDUFS8; Complex II: SDHB; Complex III: UQCRFS1) → **decreased oxidative phosphorylation capacity** (Complex I ~28% of normal, Complex II ~52% of normal activity in patient fibroblasts)
5. **Neuronal energy failure and iron mishandling in CNS:** Neurons and oligodendrocytes are particularly vulnerable to combined iron-handling and mitochondrial-bioenergetic failure; mouse data show white-matter iron deposition, axonal degeneration, and Purkinje cell loss preceding overt movement-disorder symptoms by months (LaVaute et al. 2001, PMID:11175792)
6. **Clinical manifestation:** Progressive neurodegeneration → dystonia/choreoathetosis (basal ganglia/extrapyramidal circuit dysfunction), developmental regression, cerebral atrophy, seizures
7. **Erythroid arm (parallel/downstream branch):** Erythroid precursors similarly cannot mobilize iron for heme synthesis despite adequate substrate → microcytic, hypochromic, iron-refractory anemia with elevated zinc protoporphyrin (a marker of impaired heme synthesis)

**Upstream vs. downstream:** The IRP2 loss-of-function lesion is the sole upstream initiating event; iron-gene misregulation and mitochondrial Fe-S cluster deficiency are intermediate/convergent nodes; neurodegeneration and anemia are parallel downstream phenotypic branches from the shared iron-misregulation node (this maps naturally onto a dismech pathophysiology node structure with a branch point).

**Molecular pathways:** Iron-responsive element (IRE)/iron regulatory protein (IRP) post-transcriptional regulatory system; hypoxia-inducible factor pathway (IRP1/IRP2 also regulate HIF2α mRNA translation via a 5'UTR IRE — relevant to erythropoiesis regulation and potentially to the atypical ferritin/hypoxia signaling crosstalk, PMID:24389303-adjacent literature); mitochondrial Fe-S cluster biogenesis and oxidative phosphorylation (Reactome/KEGG: "Iron uptake and transport," "Respiratory electron transport").

**Cellular processes:** Impaired iron trafficking/import, aberrant translational repression/derepression of iron-metabolism mRNAs, mitochondrial respiratory chain dysfunction, likely secondary oxidative stress, axonal degeneration, neuronal/oligodendrocyte iron deposition.

**Protein dysfunction:** Loss of function (most variants) via nonsense-mediated decay, missense-induced misfolding/proteasomal degradation, or in-frame deletion disrupting IRE-binding surface residues (e.g., Gly785Arg disrupting "a major IRE–IRP contact point").

**Suggested GO terms:**
- GO:0006879 — cellular iron ion homeostasis
- GO:0030350 — iron-responsive element binding
- GO:0003729 — mRNA binding
- GO:0006826 — iron ion transport
- GO:0006783 — heme biosynthetic process (for the erythroid/anemia arm)
- GO:0022900 — electron transport chain
- GO:0016226 — iron-sulfur cluster assembly

**Suggested CL terms (cell types involved):**
- CL:0000031 — neuron (specifically dopaminergic/basal ganglia neurons and Purkinje cells per mouse data)
- CL:0000128 — oligodendrocyte (site of iron deposition in mouse white matter)
- CL:0000038 — erythroid progenitor cell / CL:0000765 — erythroblast (for the anemia arm)

**Molecular profiling:** No transcriptomic/proteomic/metabolomic dataset specific to human NDCAMA patients was identified in this search sweep (consistent with disease rarity — n=5 patients, mostly single-family case reports with targeted functional validation rather than -omics profiling). Mouse model transcriptomic changes ("altered expression profile associated with neurological function") are noted in the 2025 D826V knock-in mouse paper but granular datasets were not retrieved here.

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: Central nervous system (brain — cerebral cortex, basal ganglia, cerebellum, white matter tracts) and hematopoietic system (bone marrow/erythropoiesis)
- Secondary: Peripheral nervous system (peripheral neuropathy reported); possibly immune system (recurrent infections/neutropenia in one patient — needs further validation as a core feature vs. incidental)
- Body systems: Nervous system (primary), hematologic system (primary), musculoskeletal (secondary — pes cavus, spasticity-related contractures)

**Tissue/cell level:**
- White matter tracts (oligodendrocyte iron deposition, demonstrated in mouse model; corresponds to white matter volume loss on human MRI)
- Cerebral cortex (atrophy)
- Cerebellum — Purkinje cell loss (mouse model; not yet directly demonstrated histopathologically in human patients, who are diagnosed via imaging/genetics rather than biopsy)
- Basal ganglia / extrapyramidal motor circuitry (clinical correlate of choreoathetosis/dystonia)
- Bone marrow erythroid precursors

**Subcellular level (GO Cellular Component):**
- GO:0005829 — cytosol (site of IRP2 IRE-binding activity)
- GO:0005739 — mitochondrion (site of Fe-S cluster-dependent respiratory chain dysfunction)
- GO:0005777 — peroxisome (not specifically implicated but part of broader iron-handling machinery in some models — verify before use)

**Localization (UBERON):**
- UBERON:0000955 — brain
- UBERON:0002316 — white matter of cerebrum / relevant white-matter tract terms
- UBERON:0002037 — cerebellum
- UBERON:0002420 — basal ganglion
- UBERON:0002371 — bone marrow

**Lateralization:** Bilateral/symmetric involvement reported (consistent with a systemic metabolic/genetic disorder rather than a focal lesion).

---

## 8. Temporal Development

- **Onset:** Infantile (reported onset ages: ~5 months [Maio 2022 patient — hypotonia/decreased movement], ~11 months [same patient — infantile spasms], and broadly "early-onset" in the other cases per the disease name itself). No adult-onset cases have been reported.
- **Onset pattern:** Insidious/subacute — hypotonia and developmental stagnation precede overt movement disorder and seizures.
- **Progression:** Progressive, non-remitting. Serial neuroimaging in the Costain and Cooper patients showed worsening cerebral atrophy over time.
- **Disease stages:** No formal staging system exists (too rare); can be qualitatively described as (1) early developmental delay/hypotonia phase, (2) movement disorder emergence (dystonia/choreoathetosis) with anemia, (3) progressive neurodegeneration with seizures and cerebral atrophy, (4) severe disability/mortality (one reported death at age 10).
- **Progression rate:** Variable but overall relatively rapid for a pediatric neurodegenerative disorder — death within the first decade reported in one case; others alive into later childhood with severe impairment.
- **Remission:** None reported — no spontaneous or treatment-induced remission documented in any case.
- **Critical periods:** Infancy/early childhood is the critical window of clinical presentation; no data on prenatal detectability or intervention windows.

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal recessive (biallelic variants in all reported cases; parents in reported families are unaffected carriers).
- **Penetrance:** Presumed complete for biallelic null/severe hypomorphic genotypes, based on all reported homozygous/compound-heterozygous individuals being symptomatic — though this is based on only ~5 patients, so formal penetrance estimates are not statistically robust.
- **Expressivity:** Variable — phenotypic severity appears to correlate loosely with variant severity (complete-null Costain patient had a particularly severe/progressive phenotype; missense/hypomorphic patients show a broadly overlapping but not identical feature set — e.g., variable presence of seizures, hearing loss, immune features).
- **Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Founder effects:** None established; reported families are from diverse populations (Filipino, Australian, US, Chinese ×2), arguing against a single founder variant and consistent with private/family-specific variants at each report.
- **Consanguinity:** Not explicitly reported as a feature of the published families (most cases are compound heterozygous rather than homozygous, arguing against obligate consanguinity, though this should be verified per source).
- **Carrier frequency:** Unknown/not established — variants are presumed ultra-rare or absent from population databases (gnomAD) given only 4 known families.
- **Epidemiology:** No formal prevalence or incidence estimate exists; this is one of the rarest reported monogenic neurodegenerative disorders (n≈5 patients in the world literature as of 2024–2025).
- **Population demographics:** No specific ethnic/geographic enrichment identified — cases span East Asian (Chinese, 2 families), Southeast Asian (Filipino), and Oceanian/European-descent (Australian) backgrounds, plus at least one US-diagnosed case, suggesting the disorder occurs across diverse populations as private variants rather than being population-restricted.
- **Sex ratio:** All reported patients described in this search sweep are male (16-year-old boy, 10-year-old boy who died, 7-year-old boy, 8-month-old boy) — this is a striking pattern worth flagging, though with n≈4-5 it cannot be concluded that this reflects a true sex-linked susceptibility (IREB2 is autosomal, not X-linked) rather than ascertainment bias in a tiny case series. Curators should note this as an open observation, not a mechanistic claim.
- **Age distribution:** All reported cases are pediatric (infancy through early adolescence at presentation; one death at age 10).

---

## 10. Diagnostics

**Laboratory tests:**
- Complete blood count: microcytic, hypochromic anemia (variably mild-to-moderate)
- Iron studies: serum ferritin variably normal/low-normal or elevated (not a consistent single-direction marker across reported patients — see Section 3); serum iron/transferrin reported as normal in at least one patient (Cooper 2019)
- Zinc protoporphyrin IX: elevated (marker of impaired heme synthesis / functional iron deficiency at the erythroid level) — reported in Costain and Maio patients
- Key diagnostic clue: **anemia unresponsive to iron supplementation** — should prompt consideration of a functional (rather than true) iron-deficiency mechanism

**Biomarkers:** No validated circulating biomarker beyond the above CBC/iron-study pattern; IRP2 protein/IRE-binding activity assays in patient-derived lymphoblasts (research-use, not clinical-grade) have been used to functionally confirm pathogenicity.

**Imaging:** Brain MRI showing progressive cerebral atrophy, white matter volume loss, and (in one patient) a thickened corpus callosum. No single pathognomonic imaging pattern (e.g., no classic NBIA-type basal ganglia iron signal reported on standard MRI sequences in the human cases reviewed, though iron-sensitive sequences such as SWI were not specifically discussed in the search results retrieved — recommend follow-up).

**Genetic testing:**
- **Whole exome sequencing (trio)** is the diagnostic modality used in all reported cases — appropriate given the extreme rarity and absence of any commercial single-gene or panel test specifically targeting IREB2 at the time of these reports.
- Given the disorder's novelty (first described 2019), IREB2 may not yet be included on standard "NBIA" or "pediatric neurodegeneration/movement disorder" gene panels — worth flagging as a genetic-testing-access gap.
- No newborn screening, carrier screening, or prenatal testing program exists given disease rarity and recency of description.

**Clinical criteria:** No formal consensus diagnostic criteria have been published (disease too recently described / too rare); diagnosis is currently genetic-confirmation-based (biallelic IREB2 variants) plus compatible phenotype (developmental delay, choreoathetosis/dystonia, iron-refractory microcytic anemia, progressive cerebral atrophy).

**Differential diagnosis:** Other genetic causes of infantile neurodegeneration with movement disorder, including:
- Classic **NBIA (Neurodegeneration with Brain Iron Accumulation)** disorders (PANK2, PLA2G6, WDR45, etc.) — mechanistically and clinically overlapping (iron-related neurodegeneration with dystonia) but genetically and (per current data) neuroimaging-pattern distinct (classic NBIA shows T2* basal ganglia iron signal; IREB2-NDCAMA's iron-handling defect is a *functional deficiency* rather than *regional accumulation*, an important mechanistic contrast worth explicit note in any dismech `mechanistic_hypotheses`/discussion)
- Dystonic cerebral palsy (a clinical label sometimes applied before genetic diagnosis, per the Porras 2024 mouse paper's description of the index patient)
- Other causes of iron-refractory iron-deficiency-like anemia (e.g., IRIDA/TMPRSS6-related iron-refractory iron deficiency anemia — mechanistically distinct, worth differentiating)
- Mitochondrial disorders with combined respiratory chain defects

**Screening:** None established.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** At least one reported death (age 10, progressive neurological disease) among 5 reported patients; no formal survival statistics exist given case-series-only data.
- **Morbidity/function:** Severe and progressive functional impairment reported in all surviving patients — non-ambulatory, minimal-to-absent speech, need for full supportive care.
- **Complications:** Seizures (including infantile spasms/hypsarrhythmia), recurrent infections/neutropenia (one patient), feeding intolerance.
- **Recovery potential:** No evidence of spontaneous recovery or disease reversal in any reported patient; cellular/functional rescue has only been demonstrated in vitro (lentiviral gene restoration in patient lymphoblasts), not in vivo.
- **Prognostic factors:** Variant severity (complete null vs. hypomorphic missense) may correlate with phenotype severity, but sample size is too small for statistical confirmation.

---

## 12. Treatment

**No disease-modifying or FDA-approved therapy currently exists.** Management to date has been supportive/symptomatic (standard pediatric neurodegeneration supportive care — physical/occupational/speech therapy, seizure management, nutritional support). Suggested NCIT terms for these general supportive categories: NCIT:C15747 (Supportive Care), NCIT:C15302 (Physical Therapy), NCIT:C121351 (Occupational Therapy), NCIT:C159273 (Speech Therapy).

**Important negative/mechanistic treatment finding:** The authors of the key mechanistic papers explicitly caution that **iron chelation therapy would likely not be therapeutic** (and could be harmful), because the underlying defect is a *functional cytosolic iron deficiency*, not iron overload — despite normal/elevated serum ferritin in some patients. This is an important mechanism-informed treatment caveat for curators to capture (e.g., as a `discussions` entry with `kind: KNOWLEDGE_GAP` or a treatment-avoidance note), since a naive reading of elevated ferritin could otherwise misleadingly suggest chelation.

**Experimental/preclinical therapeutic leads (model-organism evidence only, not yet tested in human patients):**
- **TEMPOL** (a stable nitroxide antioxidant) — dietary TEMPOL in *Ireb2*−/− mice activates latent IRE-binding activity of the paralog IRP1, correcting TfR1 stabilization and ferritin repression in brain tissue, and **"markedly attenuated"** progression of the neuromuscular/neurodegenerative phenotype, though it did **not** correct the microcytic anemia (Ghosh et al. 2008, PNAS, PMID:18685102). This represents a proof-of-concept pharmacological strategy (paralog-activation rather than gene replacement) that has not been translated to human patients.
- **Proteasome inhibition** — in the 2024 Chinese-pedigree functional study, proteasome inhibitors partially restored IRP2 expression in cells carrying the p.Asp826Val degradation-prone variant, "highlighting a promising therapeutic target for patients with IRP2 deficiency" — an in vitro finding only.
- **Gene replacement (research tool, not therapy):** Lentiviral-mediated restoration of wild-type IREB2 expression fully reverses the cellular/molecular phenotype in patient-derived lymphoblasts (Costain 2019; Maio 2022) — proof of principle for a gene-therapy approach (suggested `therapeutic_modality: GENE_THERAPY` if/when this reaches clinical translation), but no in vivo human gene therapy trial exists.
- **HIF2 inhibition:** A related but mechanistically distinct line of mouse work ("Protective Effects of Hif2 Inhibitor PT-2385 on a Neurological Disorder Induced by Deficiency of Irp2," PMID:34675764) suggests that pharmacological HIF2α inhibition may ameliorate the *Ireb2*-deficient mouse neurological phenotype, consistent with the IRP-HIF2α mechanistic link described in Section 6 — another preclinical-only lead.

**Clinical trials:** No IREB2/NDCAMA-specific trials identified in ClinicalTrials.gov in this search sweep (consistent with disease rarity/recency).

**Treatment strategy:** No treatment algorithm exists; management is individualized supportive care by pediatric neurology/genetics teams.

---

## 13. Prevention

- **Primary prevention:** None available (no way to prevent occurrence in an at-risk family beyond genetic counseling).
- **Secondary prevention/screening:** No population or genetic screening program exists (disease too rare/recently described); once a proband is identified, cascade carrier testing of at-risk relatives and prenatal/preimplantation genetic testing could in principle be offered for future pregnancies in a known-carrier family, per standard practice for autosomal recessive Mendelian disorders — not specifically documented as having been performed in the literature reviewed.
- **Genetic counseling:** Standard autosomal recessive recurrence-risk counseling (25% recurrence risk per pregnancy for carrier-carrier couples) applies once a family's causal variants are known. Suggested NCIT term: NCIT:C15240 (Genetic Counseling).
- **Public health/behavioral/prophylaxis:** Not applicable to this Mendelian disorder.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally-occurring veterinary/companion-animal cases of IREB2-deficiency neurodegeneration have been identified in this search sweep (OMIA search not independently performed here — recommend a direct OMIA check before asserting absence).
- **Orthologous gene:** Mouse *Ireb2* (MGI:1928268), NCBI Gene (mouse) — extensively studied via targeted knockout (see Section 15).
- **Comparative biology:** The mouse *Ireb2*−/− phenotype (adult-onset ataxia, bradykinesia, tremor, white-matter iron deposition, Purkinje cell loss — LaVaute et al. 2001, PMID:11175792) served as the original discovery/hypothesis-generating model that motivated the eventual search for and identification of human patients — a textbook example of mouse-to-human translational disease-gene discovery, worth explicitly capturing in the dismech entry's provenance/discussion.

---

## 15. Model Organisms

**Mouse — the dominant model system for this gene:**

1. **Global *Ireb2*−/− knockout (LaVaute et al. 2001, *Nat Genet* 27:209–214, PMID:11175792):** First description; adult-onset movement disorder (ataxia, bradykinesia, tremor) with white-matter and neuronal iron deposition preceding symptom onset by months; misregulation of intestinal iron metabolism; established IRP2 as essential for CNS iron homeostasis and motor function.

2. **A contrasting/discordant *Irp2*-deficient mouse line (Nature Genetics 2006, DOI referenced as "ng0906-967," "Iron homeostasis in the brain: complete iron regulatory protein 2 deficiency without symptomatic neurodegeneration in the mouse"):** Showed **no overt neurodegeneration or brain iron accumulation**, only mild motor coordination/balance deficits — an important discordance across independently generated knockout lines that later behavioral studies (Porras et al. 2024) sought to resolve with more sensitive testing.

3. **Behavioral deep-phenotyping (Porras et al. 2024, *Curr Res Neurobiol*, PMID:39239479):** Using rotarod, hanging-wire, hot/cold-plate, Barnes maze, and touchscreen reversal-learning assays, demonstrated significant **motor, somatosensory, and executive/cognitive dysfunction** in *Irp2*-null mice, explicitly motivated by ("The research was motivated by") the discovery of the first human IREB2-deficient patient — a direct example of reverse-translational model refinement following a human genetic discovery.

4. **Pharmacological rescue model (Ghosh et al. 2008, PNAS, PMID:18685102):** TEMPOL dietary supplementation corrects the neurodegenerative phenotype (not the anemia) via IRP1 paralog activation — see Section 12.

5. **Motor neuron/mitochondrial model (PLOS ONE 2011, "Iron Insufficiency Compromises Motor Neurons and Their Mitochondrial Function in Irp2-Null Mice"):** Direct evidence of mitochondrial dysfunction in motor neurons, mechanistically bridging to the human patient-fibroblast Complex I/II findings.

6. **Patient-variant knock-in mouse model (2025, *Acta Biochim Biophys Sin*, DOI 10.3724/abbs.2025176):** A CRISPR-Cas9-engineered *Ireb2* D826V/D826V mouse (recapitulating the exact c.2477A>T/p.Asp826Val variant from the 2024 Chinese NDCAMA pedigree) — the first patient-variant-specific (rather than null-allele) mouse model, showing impaired spatial learning/memory (Morris water maze), reduced motor activity (open field test), Y-maze deficits, reduced Ireb2 protein levels, and dysregulated iron metabolism — the most disease-relevant genetic model currently available, and a strong candidate for future preclinical therapeutic testing.

7. **Parkinson's-disease-adjacent model (Jia et al. 2022, *Cell Death Dis*, DOI 10.1038/s41419-022-04704-0):** *Otud3*-knockout mice (loss of an IRP2-stabilizing deubiquitylase) show nigral iron accumulation and nigrostriatal dopaminergic degeneration resembling Parkinson's disease — relevant as a mechanistically adjacent model connecting IRP2 stability/regulation to a distinct (sporadic, adult-onset) neurodegenerative phenotype; useful context but should not be conflated with the pediatric NDCAMA Mendelian syndrome itself.

**Model characteristics/limitations:** The existence of two independently generated *Ireb2*−/− mouse lines with discordant neurodegeneration phenotypes (LaVaute line: overt neurodegeneration; the other line: minimal pathology) is a notable **human-model-mismatch-relevant** consideration — worth flagging explicitly in any dismech `HUMAN_MODEL_MISMATCH` discussion, since it shows that genetic background/allele design details significantly affect phenotype penetrance even within the mouse, which should inform caution in extrapolating any single mouse dataset directly to human severity/course.

**Other model systems:** No zebrafish, *Drosophila*, *C. elegans*, or iPSC-derived organoid models specific to IREB2/NDCAMA were identified in this search sweep; patient-derived lymphoblast cell lines (Epstein-Barr-virus-transformed) are the primary human cellular model used across all clinical reports for functional variant validation.

---

## Summary Table of Key Citations

| Citation | PMID | Key Contribution |
|---|---|---|
| LaVaute et al. 2001, *Nat Genet* 27:209–214 | 11175792 | First mouse *Ireb2*−/− neurodegeneration model |
| Ghosh et al. 2008, *PNAS* 105:12028–33 | 18685102 | TEMPOL rescue via IRP1 activation |
| Costain et al. 2019, *Brain* 142:1195–1202 | 30915432 | First human patient (R419X/G357X), NDCAMA established |
| Cooper et al. 2019, *Brain* 142:e40 (letter) | not independently confirmed — verify | Second human patient (Gly785Arg/Ser444del) |
| Reply, Costain/Rouault, *Brain* 142:e41 | 31243430 | Response to Cooper letter |
| DeMeo et al. 2009, *Am J Hum Genet* 85:493–502 | 19800047 | IREB2 as COPD susceptibility gene (distinct entity) |
| Maio et al. 2022, *Brain Commun* 4:fcac102 | 35602653 | Third patient (missense), mitochondrial Complex I/II defect |
| Jia et al. 2022, *Cell Death Dis* 13:418 | not independently confirmed — verify | OTUD3-IRP2-Parkinson's link |
| Porras et al. 2024, *Curr Res Neurobiol* | 39239479 | Deep behavioral phenotyping of *Irp2*-null mice |
| Chinese pedigree 2024, *Orphanet J Rare Dis* | not independently confirmed — verify | Fourth/fifth patient (Ile371Val/Asp826Val) |
| D826V knock-in mouse 2025, *Acta Biochim Biophys Sin* | not independently confirmed — verify | Patient-variant-specific mouse model |

**Curator note on citation verification:** Several PMIDs above are flagged "not independently confirmed" — per dismech's evidence-verification SOP, each of these must be independently confirmed via `just fetch-reference PMID:XXXX` (or direct PubMed lookup to first obtain the correct PMID) before any snippet is committed to a KB entry. Do not treat any PMID/quote in this report as pre-verified for dismech curation purposes — this report is a research lead document, not a validated evidence source.

Sources:
- [Absence of iron-responsive element-binding protein 2 causes a novel neurodegenerative syndrome (Costain et al. 2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6487337)
- [IREB2-associated neurodegeneration (Cooper et al. 2019)](https://academic.oup.com/brain/article/142/8/e40/5523716)
- [Reply: IREB2-associated neurodegeneration](https://pubmed.ncbi.nlm.nih.gov/31243430/)
- [Disruption of cellular iron homeostasis by IREB2 missense variants (Maio et al. 2022)](https://academic.oup.com/braincomms/article/4/3/fcac102/6570544)
- [Novel biallelic variants in IREB2 cause an early-onset neurodegenerative disorder in a Chinese pedigree (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11587613/)
- [OMIM #618451 — NDCAMA](https://omim.org/entry/618451)
- [OMIM *147582 — IREB2](https://www.omim.org/entry/147582)
- [MedGen C5193104](https://www.ncbi.nlm.nih.gov/medgen/1676579)
- [Targeted deletion of Ireb2 causes neurodegenerative disease in mice (LaVaute et al. 2001)](https://pubmed.ncbi.nlm.nih.gov/11175792/)
- [Tempol-mediated activation of latent iron regulatory protein activity (Ghosh et al. 2008)](https://www.pnas.org/doi/full/10.1073/pnas.0805361105)
- [Ablation of Iron Regulatory Protein 2 produces a neurological disorder in mice (Porras et al. 2024)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11372806/)
- [Iron homeostasis in the brain: complete IRP2 deficiency without symptomatic neurodegeneration in mouse](https://www.nature.com/articles/ng0906-967)
- [Deubiquitylase OTUD3 prevents Parkinson's disease through stabilizing IRP2](https://www.nature.com/articles/s41419-022-04704-0)
- [The D826V point mutation in IREB2 causes early-onset neurodegeneration in mice (2025)](https://www.sciengine.com/ABBS/doi/10.3724/abbs.2025176)
- [Integration of Genomic and Genetic Approaches Implicates IREB2 as a COPD Susceptibility Gene (DeMeo et al. 2009)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2756547/)
- [IREB2 Gene - GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=IREB2)
- [Iron Insufficiency Compromises Motor Neurons in Irp2-Null Mice](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3189198/)