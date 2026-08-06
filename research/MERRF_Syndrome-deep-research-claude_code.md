---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-05T12:16:47.125521'
end_time: '2026-08-05T12:35:52.687378'
duration_seconds: 1145.56
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MERRF Syndrome
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
  - claude-opus-5[1m]
  web_search_requests: 18
  num_turns: 9
  total_cost_usd: 6.231523499999999
  session_id: e7b19b16-ae7f-4ea8-ba06-c647c11152dc
  stop_reason: end_turn
citation_count: 20
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MERRF Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MERRF Syndrome** covering all of the
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

# Research Report: MERRF Syndrome (Myoclonic Epilepsy with Ragged Red Fibers)

**Compiled:** 2026-08-05 · **Target MONDO:** MONDO:0010790 · **Category:** Mendelian (mitochondrial, maternally inherited)

### Provenance and verification status (read first)

This report was assembled from GeneReviews, the founding primary literature, and cohort/cell-biology papers pulled from PubMed and PMC. **No deep-research provider was used**, so the named-entity-confusion (NEC) failure mode does not apply here; the identity anchor (MT-TK / m.8344A>G / OMIM 545000) was checked against ClinVar and GeneReviews directly.

Quotes are tagged:
- **[V]** = verbatim, checked against a cached PubMed abstract in `references_cache/` (fetched this session with `just fetch-reference`)
- **[S]** = pulled via a summarizing web fetch — **re-verify with `just fetch-reference` before using as an evidence `snippet:`**

Ontology IDs marked **⚠** were not re-derived from OAK in this session and must be confirmed with `just validate-terms` before curation. IDs marked **✓** are already committed and validated in `kb/disorders/MERRF_Syndrome.yaml`.

A dismech entry for this disease already exists (commit `46f49f9`, 2047 lines, 86 evidence references). The material below is organized to *extend* it — new cohort data, imaging, therapeutics pipeline, model systems, and epidemiology are the main additions.

---

## 1. Disease Information

### Overview

MERRF is a maternally inherited, multisystem mitochondrial encephalomyopathy. Its classical definition is a tetrad: **myoclonus, generalized epilepsy, cerebellar ataxia, and ragged-red fibers (RRF) on muscle biopsy**. The proximal defect is a point variant in a mitochondrial transfer RNA gene — most often *MT-TK*, encoding tRNA-lysine — that cripples the mitochondrion's ability to translate its own 13 respiratory-chain subunits. Because mitochondrial genomes exist in hundreds of copies per cell and the variant is present as a mixture with normal genomes (heteroplasmy), the disease surfaces only where the mutant fraction crosses a steep threshold. That is the single most important structural fact about MERRF: it is a dosage disease with a patchy, tissue-by-tissue distribution, not a uniform loss of function.

> "MERRF (myoclonic epilepsy with ragged red fibers) is a multisystem disorder characterized by myoclonus (often the first symptom) followed by generalized epilepsy, ataxia, weakness, exercise intolerance, and dementia." — GeneReviews, **PMID:20301693** [V, already in KB]

**A critical nosological caveat that should frame the whole entry:** large modern cohorts show the full tetrad is the *minority* outcome of the causal genotype. See §3 and §9.

### Identifiers

| Resource | Identifier |
|---|---|
| MONDO | **MONDO:0010790** (MERRF syndrome) |
| OMIM | **545000** (MERRF); *MT-TK* locus **590060** |
| Orphanet | **ORPHA:551** (Orphanet page was CAPTCHA-blocked this session — ⚠ confirm number before citing) |
| ICD-10-CM | **E88.42** — "MERRF syndrome" (billable, dedicated code) |
| ICD-11 | Mitochondrial-disease chapter; a MERRF-specific stem code was not confirmed this session — ⚠ verify in the ICD-11 browser |
| MeSH | **D017243** — "MERRF Syndrome" |
| ClinVar (variant) | VCV000009579; dbSNP **rs118192098** |
| HGNC (gene) | **hgnc:7489** (*MT-TK*); NCBI Gene **4566** |
| MITOMAP | m.8344A>G, confirmed pathogenic mt-tRNA variant |

### Synonyms

MERRF; myoclonic epilepsy with ragged red fibers; myoclonus epilepsy associated with ragged-red fibers; myoclonic epilepsy associated with ragged-red fibers; **Fukuhara disease** (eponym, from the 1980 Japanese description); "myoclonic ataxia" (proposed renaming — see §3).

### Data provenance type

**Aggregated disease-level**, with two useful registry-derived exceptions that behave more like individual-patient datasets: the German **mitoNET/mitoREGISTER** cohort (PMID:26995359) and the **Nation-wide Italian Collaborative Network of Mitochondrial Diseases** database (PMID:23635963). No EHR-derived MERRF phenotype algorithm is published; the ICD-10-CM code E88.42 is specific enough that an OMOP-style case-finding definition is feasible and would be a reasonable `definitions[]` addition (currently absent from the KB entry).

---

## 2. Etiology

### Primary causal factor

A heteroplasmic point variant in a mitochondrially encoded tRNA gene → failure of intramitochondrial translation. The dominant lesion:

**m.8344A>G in *MT-TK*** (NC_012920.1:m.8344A>G), an A→G transition in the T-ψ-C loop of mt-tRNA^Lys.

> "An A to G transition mutation at nucleotide pair 8344 in human mitochondrial DNA (mtDNA) has been identified as the cause of MERRF." — Shoffner et al., *Cell* 1990, **PMID:2112427** [V]

> "The m.8344A>G pathogenic variant in the mitochondrial gene MT-TK is present in more than 80% of affected individuals with typical findings." — GeneReviews, **PMID:20301693** [V]

Independent estimate: "point mutations in the tRNALys gene of the DNAmt, mainly A8344G, are responsible for almost 90% of MERRF cases" — Lorenzoni et al., **PMID:25337734** [V].

### Genetic risk factors

- **Causal variants (germline, mitochondrial):** m.8344A>G (dominant); other *MT-TK* alleles m.8356T>C, m.8363G>A, m.8361G>A, m.8340G>A (⚠ these specific positions were not individually confirmed against MITOMAP this session — verify before curating); a **novel m.8315A>C** *MT-TK* variant reported as a MERRF cause (PMC9319148 — ⚠ PMID not resolved, CAPTCHA-blocked).
- **Non-*MT-TK* causes:** "Pathogenic variants in MT-TF, MT-TH, MT-TI, MT-TL1, MT-TP, MT-TS1, and MT-TS2 have also been described in a subset of individuals with MERRF." — **PMID:20301693** [V]. A worked *MT-TF* case (typical clinical, histological and biochemical MERRF from a phenylalanine-tRNA variant) is documented in **PMID:16414077** [V]. That several different tRNAs produce the same syndrome argues the operative lesion is *generic translation failure*, not anything lysine-specific.
- **Heteroplasmy level** is the proximate quantitative risk factor — but a badly behaved one (see §9 and the controversy in the KB `discussions` block).
- **Nuclear background as a modifier:** the strongest human evidence is the Zhou/Attardi autopsy study (§6), which concluded that "**nuclear-controlled neuronal differences among various regions of the CNS**" contribute to which neurons die — **PMID:9315896** [V].

### Environmental risk factors

There is **no established environmental cause**. What exists is a set of **decompensation triggers and mitochondrial toxins** that convert a compensated carrier state into clinical disease or accelerate it:

- **Valproic acid** — interferes with mitochondrial respiration and β-oxidation; can precipitate hepatic failure. Specifically contraindicated despite being the conventional first choice for progressive myoclonic epilepsy.
- **Aminoglycoside antibiotics, linezolid** (both inhibit the same mitochondrial ribosome that is already failing).
- **Cigarettes and alcohol** — named explicitly in GeneReviews management.
- Catabolic stress: intercurrent infection, fasting, dehydration, surgery/anesthesia.

> "valproic acid should be avoided in the treatment of seizures" — GeneReviews **PMID:20301693** [V]
> Avoid "Aminoglycoside antibiotics, linezolid, cigarettes, alcohol, valproic acid" — GeneReviews **PMID:20301693** [S]

### Protective factors

- **Retention of wild-type mtDNA is the only well-established protective factor**, and it is remarkably potent: "This suggests that a small percentage of normal mtDNAs has a large protective effect on phenotype." — Shoffner 1990, **PMID:2112427** [V]
- No protective nuclear variant, haplogroup, diet, or exposure has been established. Aerobic exercise is used therapeutically on a mitochondrial-biogenesis rationale but has not been shown to prevent onset.

### Gene–environment interactions

The clinically actionable interaction is **genotype × drug**: a valproate exposure that is benign in idiopathic generalized epilepsy is hepatotoxic/decompensating in an m.8344A>G carrier. Similarly, aminoglycoside ototoxicity is amplified on a background of mitochondrial translation failure. These belong in the entry as mechanism-derived treatment decisions (the KB already curates valproate avoidance as a `treatments` entry — the right call).

---

## 3. Phenotypes

### The central finding of the modern literature: the classical tetrad is the exception

Two large cohorts independently dismantled the textbook picture. **This should be the headline phenotype fact in any KB entry.**

**Italian collaborative cohort (n=42 carriers + systematic review of 321 published patients), Mancuso et al., *Neurology* 2013, PMID:23635963** [V — full abstract cached]:

> "Forty-two patients carrying the mutation were identified. The great majority did not have full-blown MERRF syndrome. Myoclonus was present in 1 of 5 patients, whereas myopathic signs and symptoms, generalized seizures, hearing loss, eyelid ptosis, and multiple lipomatosis represented the most common clinical features."

> "Considering all of the 321 patients so far available… at the mean age of approximately 35 years, the clinical picture was characterized by the following signs/symptoms, in descending order: myoclonus, muscle weakness, ataxia (35%-45% of patients); generalized seizures, hearing loss (25%-34.9%); cognitive impairment, multiple lipomatosis, neuropathy, exercise intolerance (15%-24.9%); and increased creatine kinase levels, ptosis/ophthalmoparesis, optic atrophy, cardiomyopathy, muscle wasting, respiratory impairment, diabetes, muscle pain, tremor, migraine (5%-14.9%)."

> "MERRF could be better defined as a myoclonic ataxia rather than a myoclonic epilepsy."

**German mitoNET registry (n=34), Altmann et al., *J Neurol* 2016, PMID:26995359** [V — full abstract cached]:

> "Mean age at symptom onset was 24.5 years ±10.9 (6-48 years) with adult onset in 75 % of the patients."

> "In our cohort, the canonical features seizures, myoclonus, cerebellar ataxia and ragged-red fibres that are traditionally associated with MERRF, occurred in only 61, 59, 70, and 63 % of the patients, respectively. In contrast, other features such as hearing impairment were even more frequently present (72 %). Other common features in our cohort were migraine (52 %), psychiatric disorders (54 %), respiratory dysfunction (45 %), gastrointestinal symptoms (38 %), dysarthria (36 %), and dysphagia (35 %). Brain MRI revealed cerebral and/or cerebellar atrophy in 43 % of our patients."

**East-Chinese tRNA-Lys cohort, PMID:32577866** [V, already in KB]: myopathy-plus-neuropathy dominates; "the classic syndrome of myoclonic epilepsy with ragged-red fibers (MERRF) was rare (23%)"; symptom frequencies "muscle weakness (76.9%), exercise intolerance (76.9%), elevated creatine kinase levels (61.5%), peripheral neuropathy (69.2%) and cerebellar ataxia (61.5%)".

**Pediatric MT-TK cohort (n=22), PMID:39429077** [V, already in KB]: 15 MERRF, 3 Leigh syndrome, 4 LS-MERRF overlap; median onset **5.00 (2.75, 9.00) years**; myoclonus progressive in all 15 MERRF children, initial symptom in 10; EEG split myoclonus into 6 cortical myoclonic epilepsy vs 4 subcortical.

### Phenotype table with HPO suggestions and frequency evidence

| Phenotype | HPO term | Onset | Course | Frequency (source) |
|---|---|---|---|---|
| Myoclonus (often first symptom; action-sensitive) | Myoclonus **HP:0001336** ✓ | childhood–adult | progressive | 35–45% of 321 pooled (PMID:23635963); 59% (PMID:26995359); ~20% in Italian n=42. **Do not assert a band inside a MERRF-defined cohort — circular** |
| Generalized seizures | Seizure **HP:0001250** ✓ | after myoclonus | recurrent/progressive | 25–34.9% pooled; 61% (mitoNET) |
| Cerebellar ataxia | Progressive cerebellar ataxia **HP:0002073** ✓ | variable | progressive | 35–45% pooled; 70% (mitoNET); 61.5% (PMID:32577866) → **FREQUENT** |
| Muscle weakness | **HP:0001324** ✓ | variable | slowly progressive | 76.9% (PMID:32577866) → **FREQUENT** |
| Exercise intolerance | **HP:0003546** ✓ | early | stable-progressive | 76.9% → **FREQUENT** |
| Peripheral neuropathy | **HP:0009830** ✓ | adult | progressive | 69.2%; 15–24.9% pooled → **FREQUENT** |
| Ragged-red fibers | **HP:0003200** ✓ | — | — | 63% (mitoNET) — note: *not* universal |
| Sensorineural hearing impairment | **HP:0000407** ✓ | variable | progressive | **72% (mitoNET) — the single most frequent feature in that cohort**; 25–34.9% pooled → **FREQUENT** |
| Cognitive impairment / dementia | Dementia **HP:0000726** ✓ | late | progressive | 15–24.9% pooled |
| Ptosis / ophthalmoparesis | Ptosis **HP:0000508** ✓ | variable | progressive | 5–14.9% pooled (ptosis common in Italian n=42) |
| Optic atrophy | **HP:0000648** ✓ | variable | progressive | 5–14.9% pooled |
| Cardiomyopathy | **HP:0001638** ✓ | variable | progressive | 5–14.9% pooled |
| Wolff-Parkinson-White | **HP:0001716** ✓ | variable | — | not quantified; named in GeneReviews |
| Diabetes mellitus | **HP:0000819** ✓ | adult | progressive | 5–14.9% pooled |
| Multiple symmetric lipomatosis | Lipoma **HP:0012032** ✓ | adult | progressive | 15–24.9% pooled — clinically distinctive red flag |
| Short stature | **HP:0004322** ✓ | childhood | — | GeneReviews "common" |
| Elevated creatine kinase | **HP:0003236** ✓ | — | — | 61.5%; 5–14.9% pooled → **FREQUENT** in tRNA-Lys carriers |
| **Migraine** *(KB gap)* | Migraine **HP:0002076** ⚠ | adult | recurrent | **52% (mitoNET)** → FREQUENT |
| **Psychiatric disorder** *(KB gap)* | Behavioral abnormality **HP:0000708** ⚠ (or a depression/anxiety child term) | adult | — | **54% (mitoNET)** → FREQUENT |
| **Respiratory dysfunction** *(KB gap)* | Respiratory insufficiency **HP:0002093** ⚠ | adult | progressive | **45% (mitoNET)**; 5–14.9% pooled |
| **Gastrointestinal symptoms** *(KB gap)* | **HP:0011024** ⚠ | adult | — | 38% (mitoNET) |
| **Dysarthria** *(KB gap)* | **HP:0001260** ⚠ | with ataxia | progressive | 36% (mitoNET) |
| **Dysphagia** *(KB gap)* | **HP:0002015** ⚠ | later | progressive | 35% (mitoNET) |
| **Cerebral/cerebellar atrophy on MRI** *(KB gap)* | Cerebellar atrophy **HP:0001272** ⚠ / Cerebral atrophy **HP:0002059** ⚠ | — | progressive | 43% (mitoNET) |
| Elevated lactate (blood/CSF) | Increased circulating lactate **HP:0002151** ⚠ | — | — | supportive, neither sensitive nor specific |
| Pigmentary retinopathy | **HP:0000580** ⚠ | — | — | GeneReviews "have been observed" |
| Tremor, muscle pain, muscle wasting | HP:0001337 ⚠ / HP:0003326 ⚠ / HP:0003202 ⚠ | — | — | 5–14.9% pooled |

**Six of these (migraine, psychiatric, respiratory, GI, dysarthria, dysphagia) are frequency-quantified in a registry cohort and are currently absent from the dismech entry — the highest-yield phenotype additions available.**

### Quality of life

No MERRF-specific QoL study was found. Generic mitochondrial-disease instruments apply and are the right anchors:
- **NMDAS** (Newcastle Mitochondrial Disease Adult Scale) — three sections: current function, system-specific involvement, current clinical assessment.
- **NMQ** (Newcastle Mitochondrial Quality of life measure) — 63 items across 16 domains.
- Predictors of overall QoL in mitochondrial disease are **fatigue and physical functioning**; one cohort reported 79.8% with severe fatigue [S — verify].
- The KL1333 phase 1a/1b trial validated the **30-second Sit-to-Stand** and **patient-reported fatigue scales** as outcome measures in primary mitochondrial disease (**PMID:39657714** [V]).

Per-phenotype QoL impact: myoclonus is the dominant disability driver in classical MERRF (the levetiracetam case report documented that "the average myoclonus score improved dramatically, as well as the quality of life" — **PMID:16414077** [V]); ataxia and hearing loss dominate in the broader carrier population.

---

## 4. Genetic / Molecular Information

### Causal gene

**MT-TK** — mitochondrially encoded tRNA-lysine. HGNC:7489 (lowercase `hgnc:7489` in dismech), NCBI Gene 4566, OMIM 590060. A 70-nucleotide RNA at mtDNA map position **8295–8364**. GeneReviews: *MT-TK* accounts for **>90%** of MERRF; m.8344A>G alone for **>80%** of typical presentations.

### Pathogenic variants

| Field | m.8344A>G |
|---|---|
| Nomenclature | NC_012920.1(MT-TK):m.8344A>G |
| dbSNP | rs118192098 |
| ClinVar | VCV000009579; **Pathogenic**, 2-star review status (criteria provided, multiple submitters, no conflicts), 6 submissions, last evaluated 2026-01-07 |
| Variant class | Point substitution (transition) in a non-coding structural RNA — **not** missense/nonsense/frameshift; standard ACMG protein-level codes do not apply, mt-tRNA-specific criteria (Yarham/McFarland scoring) do |
| Origin | **Germline, maternal; mitochondrial; heteroplasmic** (occasionally homoplasmic) |
| Population frequency | Heteroplasmic allele frequency **0.011% in gnomAD v4.1.0** [S — verify in gnomAD directly] |
| Functional consequence | **Loss of function of the tRNA** via loss of the wobble-uridine taurine modification → complete failure to decode both AAA and AAG |

Other *MT-TK* alleles reported in MERRF: m.8356T>C, m.8363G>A, m.8361G>A, m.8340G>A ⚠, plus the newly reported **m.8315A>C** ⚠. Non-*MT-TK* genes: *MT-TF, MT-TH, MT-TI, MT-TL1, MT-TP, MT-TS1, MT-TS2* (**PMID:20301693** [V]).

### Functional consequence — the molecular core

> "revealed the lack of a post-transcriptional taurine-modification at the anticodon wobble uridine in two mt tRNAs bearing typical pathogenic mutations" — Kirino/Suzuki, **PMID:17132941** [V]

> "The MERRF mt tRNA(Lys) lacking the wobble modification cannot translate either of its codons (AAA and AAG), while the translational activity of MELAS mt tRNA(Leu(UUR)) lacking wobble modification is more depressed in decoding of UUG codon than UUA codon." — **PMID:17132941** [V]

That contrast is the cleanest molecular discriminator between MERRF and MELAS: **MERRF's decoding failure is complete; MELAS's is codon-selective.** GO term: `tRNA wobble uridine modification` **GO:0002098** ✓ (DECREASED).

### Modifier genes

No named modifier gene is established. The strongest evidence that nuclear modifiers *exist* is Zhou 1997 (**PMID:9315896** [V]) — see §6. Candidate classes (all unvalidated): mitochondrial biogenesis capacity (PGC-1α axis), mitophagy capacity, antioxidant reserve, mtDNA haplogroup. In the rapamycin study, MERRF fibroblasts carried haplogroups H and U vs control T/U5a/U5b — an incidental observation, **not** a haplogroup association [S].

### Epigenetics

No established role for nuclear DNA methylation or histone modification in MERRF. The relevant "epigenetic-adjacent" layer is **mitochondrial RNA post-transcriptional modification** (the taurinomethyl-uridine tag itself, installed by MTO1/GTPBP3/TRMU) — mechanistically central, and worth flagging as distinct from classical epigenetics.

### Chromosomal abnormalities

**Not applicable.** MERRF is caused by point variants in a 16.6 kb circular genome; karyotype, CMA, and FISH have no role.

---

## 5. Environmental Information

- **Environmental factors:** none causal. Mitochondrial toxins (aminoglycosides, linezolid, valproate, tobacco, alcohol) modify course. No occupational or pollutant exposure is implicated.
- **Lifestyle:** avoidance of alcohol and tobacco is recommended; aerobic exercise is recommended (biogenesis rationale); fasting and catabolic stress should be avoided.
- **Infectious agents:** none causal. Intercurrent infection is a recognized decompensation trigger — relevant to the `metabolic_intoxication_decompensation` module logic, though MERRF is not itself an intoxication-type IEM.

---

## 6. Mechanism / Pathophysiology

### Causal chain (upstream → downstream)

```
m.8344A>G in MT-TK (heteroplasmic)                        [MOLECULAR]
   ├─→ Loss of tRNA-Lys wobble taurine modification        [MOLECULAR]  GO:0002098 ↓
   │      └─→ Defective mitochondrial translation          [MOLECULAR]  GO:0032543 ↓
   └─→ Mitotic segregation → tissue heteroplasmy threshold [CELLULAR]   GO:0042391 abnormal
          └─→ Respiratory chain deficiency + ΔΨm collapse  [CELLULAR]   GO:0042775 ↓, GO:0004129 ↓, GO:0072593 ↑
                 ├─→ Compensatory mitochondrial proliferation in muscle [TISSUE] → RAGGED-RED FIBER
                 │      └─→ Skeletal muscle respiratory failure [TISSUE] → weakness, exercise intolerance, ↑CK
                 └─→ Neuronal energy failure + oxidative stress [CELLULAR] GO:0006915 ↑
                        ├─→ Cortical neuronal hyperexcitability [CELLULAR] → progressive myoclonic epilepsy
                        ├─→ Dentate/cerebellar degeneration     [TISSUE]   → progressive ataxia + subcortical myoclonus
                        └─→ Progressive multisystem involvement [ORGANISM] → deafness, cardiomyopathy, DM, lipomatosis
```

This is the graph already committed in `kb/disorders/MERRF_Syndrome.yaml`, with conformance to `epilepsy_excitation_inhibition_imbalance` (at the hyperexcitability node, deliberately not at the module trigger — MERRF's entry point is bioenergetic, not channelopathic) and `cerebellar_purkinje_degeneration`.

### Key mechanistic evidence

**Threshold behavior (in vitro, cybrids/fibroblasts) — PMID:10477264** [V]:
> "Within the range of 87-73% mutated mtDNA, COX activity was decreased to 5-35% and DeltaPsi was decreased to 6-78%."
> "indicate that the biochemical manifestation of the MERRF mutation exerts a very steep threshold of DeltaPsi inhibition"
> "The activity of cytochrome c oxidase (COX) in patient fibroblasts with 89% mutated mtDNA was decreased to 20% of the control levels."

**Causal sufficiency of the tRNA lesion (rescue experiment) — PMID:15317755** [V]:
> "import of tRNALys is accompanied by a partial rescue of mitochondrial functions affected by the mutation such as mitochondrial translation, activity of respiratory complexes, electrochemical potential across the mitochondrial membrane and respiration rate"
> "Import of a tRNALys with a mutation in the anticodon preventing recognition of the lysine codons does not lead to any rescue, whereas downregulation of the transgenic tRNAs by small interfering RNA (siRNA) transiently abolishes the functional rescue, showing that this rescue is due to the import."

**Neuronal-level mechanism, human iPSC model (NEW — not in KB) — Wu et al., *J Biomed Sci* 2023, PMID:37605213** [V]:
> "MERRF neural cells harboring the m.8344A > G mutation exhibited impaired mitochondrial bioenergetic function, elevated ROS levels and imbalanced expression of antioxidant enzymes."
> "Our findings indicate that neural immaturity and synaptic protein loss led to the impairment of neuronal activity and plasticity in MERRF neurons harboring the m.8344A > G mutation."
> "neurons harboring a high level of the m.8344A > G mutation exhibited impairment of the spontaneous and evoked potential-stimulated neuronal activities."

Quantitative [S — from full text, verify]: ATP-coupled respiration 50.1% of control in high-mutation iNSCs; H₂O₂ elevated 307–446%; synaptophysin, vGLUT2 and AMPAR reduced. **This paper supplies a mechanistic bridge dismech currently lacks: bioenergetic deficit → synaptic protein loss → impaired plasticity → network-level dysfunction.** It is the strongest available in-human-cell support for the "Cortical Neuronal Hyperexcitability" node.

**Regional selectivity — the unresolved core problem (NEW evidence for the KB's existing KNOWLEDGE_GAP) — Zhou, Chomyn, Attardi & Miller, *J Neurosci* 1997, PMID:9315896** [V]:
> "Neurons and the surrounding neuropil and glia from all CNS regions that were analyzed exhibited high proportions of mutant mtDNA, ranging from 97.6 +/- 0.7% in Purkinje cells to 80.6 +/- 2.8% in the anterior horn cells."
> "Surprisingly, as compared with controls, neuronal loss ranged from 7% of the Purkinje cells to 46% of the neurons of the dentate nucleus in MERRF cerebellum."
> "Thus, factors other than the high proportion of mutant mtDNA, in particular nuclear-controlled neuronal differences among various regions of the CNS, seem to contribute to the mitochondrial dysfunction and ultimate cell death."

This is a near-perfect adjudication of the `merrf_regional_selectivity_gap` discussion: **Purkinje cells had the *highest* mutant load (97.6%) and the *least* loss (7%); dentate neurons had lower load and the *most* loss (46%).** Single-cell heteroplasmy was already measured, and it does not explain selectivity. The proposed experiment in the KB should be updated to reflect that this measurement exists and was negative — the open question is now *which* nuclear/cell-intrinsic factor, not *whether* load explains it.

**Neuropathology — PMID:3128314** [V]: "degeneration of dentate nucleus, red nucleus, globus pallidus, subthalamic nucleus and pontine tegmentum"; "degeneration of substantia nigra, locus ceruleus, cerebellar cortex and inferior olivary nucleus"; distribution "different from those of dentato-rubropallidoluysian atrophy, Joseph's disease or Friedreich's ataxia."

**Mitochondrial vasculopathy:** intramuscular vessels show the same SDH-strong/COX-deficient pattern (**PMID:8186718**, "Evidence of a mitochondrial vasculopathy in muscle biopsies" [S — verify]; the vascular finding is quoted in KB from PMID:25337734).

### Molecular pathway / process annotations

| Layer | GO / other |
|---|---|
| tRNA modification | **GO:0002098** tRNA wobble uridine modification ✓ (DECREASED) |
| Translation | **GO:0032543** mitochondrial translation ✓ (DECREASED) |
| OXPHOS | **GO:0042775** mitochondrial ATP synthesis coupled electron transport ✓ (DECREASED); **GO:0006119** oxidative phosphorylation ⚠ |
| Terminal oxidase | **GO:0004129** cytochrome-c oxidase activity ✓ (DECREASED) |
| ROS | **GO:0072593** reactive oxygen species metabolic process ✓ (INCREASED); **GO:0006979** response to oxidative stress ⚠ |
| Membrane potential | **GO:0042391** regulation of membrane potential ✓ (ABNORMAL) |
| Cell death | **GO:0006915** apoptotic process ✓ (INCREASED) |
| Mitophagy (therapeutic axis) | **GO:0000422** autophagy of mitochondrion ⚠ |
| Biogenesis (failed therapeutic axis) | **GO:0007005** mitochondrion organization ⚠ |
| Synaptic (NEW, from iPSC paper) | **GO:0048167** regulation of synaptic plasticity ⚠ |
| Pathways | KEGG hsa00190 (Oxidative phosphorylation); Reactome R-HSA-5368287 (Mitochondrial translation) ⚠ |

**Metabolic changes:** blocked electron flow → NADH accumulation → pyruvate diverted to lactate → elevated blood/CSF lactate (CHEBI:24996 ✓) and elevated lactate:pyruvate ratio; secondary carnitine depletion; MR spectroscopy shows elevated lactate and reduced N-acetylaspartate [S].

**Immune involvement:** none primary. No autoimmunity, no immunodeficiency. Secondary neuroinflammation is plausible but not documented in MERRF specifically.

**Molecular profiling available:** transcriptomic/proteomic/metabolomic MERRF-specific datasets are sparse. The iPSC study (PMID:37605213) provides targeted protein-level data (synaptophysin, vGLUT2, AMPAR, antioxidant enzymes). No published single-cell or spatial transcriptomic MERRF atlas was found — a genuine gap. No CRISPR/RNAi functional-genomics screen specific to MERRF; DepMap has no MERRF context.

---

## 7. Anatomical Structures Affected

**Organ level (primary):** central nervous system (cerebellum and its output nuclei, cerebrum), skeletal muscle. **Secondary/multisystem:** heart (cardiomyopathy, conduction — WPW), inner ear (cochlea), eye (optic nerve, retina, levator palpebrae/extraocular), peripheral nerve, endocrine pancreas, adipose tissue (symmetric lipomatosis), GI tract, respiratory system.

**Body systems:** nervous (central + peripheral), musculoskeletal, cardiovascular, special sense, endocrine, gastrointestinal, respiratory.

### Anatomical term suggestions (UBERON)

| Structure | UBERON |
|---|---|
| cerebellum | **UBERON:0002037** ✓ |
| dentate nucleus | UBERON:0002688 ⚠ |
| inferior olivary nucleus | UBERON:0002298 ⚠ |
| red nucleus | UBERON:0002038 ⚠ |
| globus pallidus | UBERON:0001875 ⚠ |
| subthalamic nucleus | UBERON:0001882 ⚠ |
| superior cerebellar peduncle (imaging target) | UBERON:0002807 ⚠ |
| pontine tegmentum / brainstem | UBERON:0002550 ⚠ / UBERON:0002298 ⚠ |
| skeletal muscle tissue | UBERON:0001134 ⚠ |
| optic nerve | UBERON:0000941 ⚠ |
| cochlea | UBERON:0001844 ⚠ |
| heart | UBERON:0000948 ⚠ |

### Cell types (CL)

| Cell type | CL | Note |
|---|---|---|
| neuron | **CL:0000540** ✓ | generic energy-failure node |
| Purkinje cell | **CL:0000121** ✓ | highest mutant load, *least* loss (PMID:9315896) |
| pyramidal neuron | **CL:0000598** ✓ | cortical hyperexcitability node |
| skeletal muscle fiber | **CL:0008002** ✓ | RRF substrate |
| glutamatergic neuron | CL:0000679 ⚠ | the iPSC model's cell type |
| cardiac muscle cell | CL:0000746 ⚠ | cardiomyopathy |
| type B pancreatic cell | CL:0000169 ⚠ | diabetes |
| retinal ganglion cell | CL:0000740 ⚠ | optic atrophy |
| endothelial cell | CL:0000115 ⚠ | intramuscular vasculopathy |

### Subcellular (GO CC)

**GO:0005739** mitochondrion ⚠; **GO:0005743** mitochondrial inner membrane ⚠ (site of the respiratory chain and ΔΨm); **GO:0005759** mitochondrial matrix ⚠ (site of mitochondrial translation); subsarcolemmal mitochondrial accumulation is the histological localization of the RRF.

**Lateralization:** bilateral and broadly symmetric. Neuropathological and imaging findings are symmetric; MERRF has no lateralized presentation (unlike MELAS stroke-like episodes, which are focal and asymmetric — a useful differential handle).

---

## 8. Temporal Development

### Onset

- Normal early development, then onset: "Onset can occur from childhood to adulthood, occurring after normal early development." — **PMID:20301693** [V]
- **Adult cohort:** mean symptom onset **24.5 ± 10.9 years (range 6–48)**; **adult onset in 75%** (**PMID:26995359** [V]).
- **Pediatric cohort:** median onset **5.00 (IQR 2.75–9.00) years** (**PMID:39429077** [V]).
- Pooled published cases: clinical picture characterized "at the mean age of approximately 35 years" (**PMID:23635963** [V]).
- Onset pattern: **insidious/chronic**, occasionally punctuated by subacute decompensation during catabolic stress.
- **Onset order:** myoclonus first in classical MERRF; but *cerebellar ataxia was the first symptom in all three* patients in the imaging series (**PMID:17989367** [V]) — consistent with the "myoclonic ataxia" reframing.

### Progression

- Course: **chronic, lifelong, progressive**; not relapsing-remitting, not self-limited. This is what places MERRF in the progressive myoclonic epilepsy group rather than among the stable genetic generalized epilepsies.
- "Myoclonus presented and worsened progressively in all 15 MERRF children, with 10 as the initial symptom" — **PMID:39429077** [V]
- Rate: highly variable, even within families. mitoNET explicitly documents "large clinical variability between carriers of the same mutation, even within families" [V].
- Staging: no formal MERRF staging system exists. NMDAS is the practical progression instrument.
- Remission: **none spontaneous**; treatment-induced improvement is symptomatic (myoclonus control) only.
- **Critical intervention window (hypothesis, not established):** the rapamycin cell data show complete bioenergetic rescue at *intermediate* mutant load but only marginal effect at *high* load — implying a window that closes (**PMID:35922766** [V]). This is the mechanistic argument for early intervention and is already curated as a KNOWLEDGE_GAP in the entry.

---

## 9. Inheritance and Population

### Epidemiology

| Measure | Value | Source |
|---|---|---|
| mtDNA disease (all causes), adults, NE England | **~20 per 100,000** (1 in 5,000) | Gorman et al., **PMID:25652200** [V] — "The minimum prevalence rate for mtDNA mutations was 1 in 5,000 (20 per 100,000)". **This is an upper bound on MERRF, not a MERRF rate.** |
| m.8344A>G, NE England adults | **0.28 per 100,000** (95% CI 0.02–0.54) | GeneReviews-cited [S] ⚠ verify primary source |
| m.8344A>G, northern Finland (n=353,895) | **0 per 100,000** (95% CI 0–1.5) | Remes et al. 2003, **PMID:12876264** (PubMed record has no abstract text — figures are from secondary citation [S]) |
| m.8344A>G, pediatric western Sweden | **0–0.25 per 100,000** | GeneReviews-cited [S] |
| MERRF syndrome (clinical) | probably **< 1 per 100,000** | StatPearls [S] |

**Suggested dismech `prevalence` records:** keep the existing Gorman upper-bound record, and add a m.8344A>G-specific record with `measure_type: POINT_PREVALENCE`, `prevalence_class: BELOW_1_IN_1000000`… actually 0.28/100,000 = 2.8 per million → **`BAND_1_9_PER_1000000`**, `rate_per_100000: 0.28`, population "Adults in North East England", with the caveat that this is *variant* prevalence, not *syndrome* prevalence.

### Inheritance

- **Maternal (mitochondrial) inheritance with heteroplasmy.** HPO: **HP:0001427** Mitochondrial inheritance ✓.
- "MERRF is caused by pathogenic variants in mtDNA and is transmitted by maternal inheritance." — **PMID:20301693** [V]
- "A female with a mtDNA pathogenic variant (whether symptomatic or asymptomatic) transmits the pathogenic variant to all of her offspring." — **PMID:20301693** [V]
- Affected males transmit nothing.
- **Penetrance:** incomplete and unpredictable; asymptomatic carriers with high mutant load are documented ("high proportions of mutant genomes (up to 63%) were found in asymptomatic relatives" — **PMID:9272179** [V]).
- **Expressivity:** extremely variable, within and between families.
- **Anticipation:** not a repeat-expansion disease; apparent anticipation can occur through bottleneck-driven load increase across generations, but is not a formal genetic anticipation mechanism.
- **Germline mosaicism / bottleneck:** the mtDNA genetic bottleneck in oogenesis is the operative mechanism — the child's mutant load is drawn stochastically and is *not* predictable from the mother's.
- **Founder effects:** none established; m.8344A>G arises recurrently on multiple haplogroup backgrounds.
- **Consanguinity:** irrelevant (not autosomal recessive).
- **Carrier frequency:** not a meaningful concept in the Mendelian sense; population heteroplasmic allele frequency ~0.011% in gnomAD v4.1.0 [S].

### The heteroplasmy–phenotype disconnect (curate as CONTROVERSY — already in the entry)

Three independent lines converge:
- "Although there seems to be a gene dosage effect in MERRF, we found no absolute relationship between the relative proportion of mutant genomes in blood and clinical severity." — **PMID:9272179** [V]
- "heteroplasmy in blood was high both in symptomatic (mean 64.5%, range 41-82%) and asymptomatic individuals (mean 53.1%, range 21-78%)" — **PMID:32577866** [V]
- "**There was no correlation between the heteroplasmy level in blood and age at onset or clinical phenotype.**" — mitoNET, **PMID:26995359** [V] ← *new, independent, registry-scale confirmation; add to the controversy evidence block*
- Counter-directional single case: "the m.8344A>G variant may manifest milder and with a later onset in the homoplasmic as compared to the heteroplasmic form" — **PMID:36176839** [V]
- And at the tissue level, Zhou 1997 shows load doesn't even explain *regional* neuronal loss (**PMID:9315896** [V]).

### Population demographics

- **Ethnic distribution:** worldwide; described in European, Japanese, Chinese, and other populations. No population enrichment established.
- **Geographic:** the Finnish zero-prevalence result vs the English 0.28/100,000 suggests real regional variation in the variant's frequency, though small-number uncertainty dominates.
- **Sex ratio:** ~1:1. Mitochondrial inheritance means both sexes are affected equally; only transmission is sex-asymmetric. (No formal sex-ratio study found.)
- **Age distribution:** bimodal-ish in practice — a pediatric group (median onset 5 y, enriched for Leigh/LS-MERRF overlap) and a much larger adult group (mean onset 24.5 y, 75% adult onset).

---

## 10. Diagnostics

### Laboratory

- **Blood/CSF lactate** (CHEBI:24996 ✓; LOINC 2524-7 ⚠, 32693-4 ⚠): supportive when elevated; **neither sensitive nor specific**, normal value does not exclude. Lactate:pyruvate ratio adds specificity.
- **Creatine kinase** (LOINC 2157-6 ⚠): elevated in 61.5% of tRNA-Lys carriers (**PMID:32577866** [V]).
- Others per Mitochondrial Medicine Society consensus (**PMID:25503498**): plasma amino acids, acylcarnitine profile, urine organic acids, FGF-21/GDF-15 as mitochondrial-myopathy biomarkers (⚠ FGF-21/GDF-15 performance in MERRF specifically not established).

### Imaging (currently a KB gap — nothing in `diagnosis` covers MRI)

**Ito et al., *AJNR* 2008, PMID:17989367** [V]:
> "Conventional brain MR imaging showed atrophy of the superior cerebellar peduncles and the cerebellum in all patients and brain stem atrophy in 2 patients."
> "There was a discrepancy between clinical disabilities (severe) and radiologic abnormalities (mild). This discrepancy and atrophy of the superior cerebellar peduncles and the cerebellum may be important findings suggesting a diagnosis of MERRF."

Registry-scale: "Brain MRI revealed cerebral and/or cerebellar atrophy in 43 % of our patients" (**PMID:26995359** [V]).

Additional reported features [S — verify before curation]: basal ganglia/dentate calcification (better on CT), white-matter change late, signal abnormality in medial thalami/mesencephalon/posterior pons/medulla, MRS showing elevated lactate and reduced NAA. **The clinico-radiological discrepancy is itself a diagnostic clue and deserves a `diagnosis[]` entry.** NCIT: Magnetic Resonance Imaging **NCIT:C16809** ⚠.

### Electrophysiology

- **EEG** (**NCIT:C38054** ✓) with myoclonus correlation — separates cortical myoclonic epilepsy from subcortical myoclonus: "Electroencephalogram monitoring in the 15 MERRF children revealed myoclonic seizures in 10 children, with 6 classified as myoclonic epilepsy, and 4 as subcortical myoclonus." (**PMID:39429077** [V]). Giant SSEPs and C-reflex support cortical origin (⚠ not sourced this session).
- **EMG/NCS**: myopathic units plus axonal sensorimotor neuropathy (69.2% neuropathy — **PMID:32577866** [V]).
- **ECG + echocardiography**: for WPW and cardiomyopathy; recommended annually (GeneReviews).
- **Audiometry**: hearing loss in 72% (mitoNET) — recommended every 2–3 years.

### Biopsy / pathology

Muscle biopsy (**NCIT:C51895** ✓): RRF on modified Gomori trichrome, COX-negative fibers, strong SDH — **including intramuscular vessels**.
> "Morphological changes seen upon muscle biopsy in MERRF include a substantive proportion of RRF, muscle fibers showing a deficient activity of cytochrome c oxidase (COX)" — **PMID:25337734** [V]
> "the presence of vessels with a strong reaction for succinate dehydrogenase and COX deficiency" — **PMID:25337734** [V]

The SDH-spared/COX-deficient dissociation is the histological signature of a *mitochondrially encoded* translation defect: SDH (complex II) is entirely nuclear-encoded and therefore unaffected. Caveat: RRF present in only **63%** of mitoNET patients — a negative biopsy does not exclude.

### Genetic testing

- **Approach:** targeted m.8344A>G testing first; if negative with high suspicion, full **mtDNA sequencing** with heteroplasmy quantification; then nuclear gene panel/exome for phenocopies.
- **Tissue matters:** blood can be falsely reassuring because heteroplasmy varies by tissue and declines in blood with age. **Urinary sediment or muscle** is preferred when blood is negative.
- Historical convenience: "The mutation alters the T psi C loop of the tRNA(Lys) gene and creates a CviJI restriction site, providing a simple molecular diagnostic test for the disease." — **PMID:2112427** [V]
- **Not useful:** karyotype, chromosomal microarray, FISH, repeat-expansion testing (all target nuclear architecture MERRF does not involve). CMA/karyotype should be explicitly marked "not applicable" in the entry.
- **WES caveat worth flagging:** standard exome pipelines historically under-called mtDNA; mtDNA is well covered by genome sequencing and by dedicated mtDNA assays. Resources: **MITOMAP**, **MSeqDR**, ClinVar, GTR.

### Omics-based diagnostics

RNA-seq, proteomics, metabolomics, and liquid biopsy have **no established clinical diagnostic role in MERRF**. Research-grade only.

### Clinical criteria

Four canonical features (**PMID:25337734** [V]):
> "Diagnostic criteria for MERRF include typical manifestations of the disease: myoclonus, generalized epilepsy, cerebellar ataxia and ragged red fibers (RRF) on muscle biopsy."

⚠ **But the criteria are now known to be poorly calibrated against the genotype** — applying them strictly misses most m.8344A>G carriers (PMID:23635963, PMID:26995359, PMID:32577866). A "MERRF Classification: Implications for Diagnosis and Clinical Trials" paper exists (*Pediatr Neurol* — ⚠ PMID unresolved) addressing exactly this.

### Differential diagnosis

| Condition | MONDO | Distinguishing |
|---|---|---|
| **MELAS** | MONDO:0010789 ✓ | m.3243A>G in *MT-TL1*; stroke-like episodes in non-vascular territories; codon-selective (not complete) decoding failure |
| **Leigh syndrome** | MONDO:0009723 ✓ | *Same m.8344A>G can cause it* — symmetric necrotizing basal ganglia/brainstem lesions; earlier onset with regression. Overlap syndrome (LS-MERRF) is real: "Fifteen children had myoclonic epilepsy with ragged-red fibers (MERRF), 3 had Leigh syndrome (LS), and 4 had LS-MERRF overlap syndrome (LS-MERRF)." (**PMID:39429077** [V]) |
| **Lafora disease** | MONDO:0009697 ✓ | AR *EPM2A*/*NHLRC1*; PAS+ Lafora bodies; occipital seizures; rapid cognitive collapse |
| **Unverricht-Lundborg** | MONDO:0009698 ✓ | AR *CSTB* dodecamer expansion; preserved cognition; no myopathy |
| Sialidosis type I | ⚠ | cherry-red spot, *NEU1*, urinary oligosaccharides |
| Neuronal ceroid lipofuscinoses | ⚠ | visual failure first, storage material on EM |
| DRPLA | ⚠ | AD CAG expansion in *ATN1*; overlapping dentatorubral anatomy but different distribution (explicitly distinguished in **PMID:3128314** [V]) |
| KSS / CPEO | ⚠ | large-scale mtDNA deletion; ophthalmoplegia dominant; a MERRF/KSS overlap due to m.3291T>C is reported |

### Screening

- **No newborn screening.** Not on the RUSP; no biochemical marker with adequate sensitivity.
- **Cascade testing** of maternal relatives is the correct family strategy. GeneReviews: at-risk relatives get molecular testing if the family variant is known; otherwise complete neurologic, ophthalmologic and audiology evaluation plus EKG, echocardiogram and blood lactate [S].
- **Carrier screening:** not applicable in the Mendelian sense.

---

## 11. Outcome / Prognosis

**Honest summary: MERRF-specific survival statistics are weak.** No dedicated natural-history/survival study of MERRF was found.

- The most-cited adult mitochondrial-myopathy outcome cohort (Mayo Clinic, n=94, *Brain Commun* 2024, DOI 10.1093/braincomms/fcae041) reports "Thirty patients died, with median survival of 33.4 years from symptom onset and 10.9 years from diagnosis. Median age at death was 55 years" [V] — **but this is the whole mitochondrial-myopathy cohort, dominated by *MT-TL1* and *POLG*; MERRF-specific survival was not separately reported.** Do **not** curate "median age at death 55" as a MERRF figure. Also from that cohort: "Cardiac involvement was associated with increased mortality [hazard ratio 2.36 (1.05, 5.29)]" and "There was no difference in survival based on genotype or phenotype."
- **Prognostic factors (qualitative, well-supported):** cardiac involvement (cardiomyopathy, conduction disease); respiratory dysfunction (45% in mitoNET); dysphagia (35%) with aspiration risk; earlier onset generally worse; higher mutant load associated with more severe manifestations at the family level (but see the disconnect above).
- **Morbidity/disability:** progressive; disability is driven by action myoclonus, ataxia, weakness, deafness and cognitive decline. Median time to gait assistance in the broader mitochondrial-myopathy cohort was 5.5 years from diagnosis / 17 years from onset [V] — again, cohort-wide, not MERRF-specific.
- **Complications:** status myoclonicus/status epilepticus, aspiration pneumonia, respiratory failure, cardiac arrhythmia and sudden death (WPW), diabetes complications, falls/fracture from ataxia, hepatic failure if valproate is given.
- **Recovery potential:** none — no disease-modifying therapy exists; the neuronal loss is not reversible. Symptomatic myoclonus control can meaningfully improve function.
- **Prognostic biomarkers:** none validated. Blood heteroplasmy explicitly fails as a prognostic marker (**PMID:26995359** [V]). GDF-15/FGF-21 are candidate severity markers in mitochondrial disease generally ⚠.

---

## 12. Treatment

**There is no disease-modifying therapy. All current care is symptomatic and supportive.**
> "Therapy is currently limited to symptomatic management of myoclonic epilepsy, and supportive measures to counteract muscle weakness with co-factors/supplements." — **PMID:35922766** [V]

### Pharmacotherapy

| Treatment | Agent (CHEBI) | NCIT action | Modality | Evidence |
|---|---|---|---|---|
| **Levetiracetam** — first choice for myoclonus | levetiracetam **CHEBI:6437** ✓ | Pharmacotherapy **NCIT:C15986** ✓ | SMALL_MOLECULE | "LEV may benefit myoclonus in PME of mitochondrial origin without altering mitochondrial function, and it could be considered the drug of first choice for the treatment of myoclonus in MERRF." — **PMID:16414077** [V] |
| **Clonazepam** | clonazepam **CHEBI:3756** ✓ | NCIT:C15986 ✓ | SMALL_MOLECULE | "levetiracetam or clonazepam for myoclonus" — **PMID:20301693** [V] |
| Other AEDs for generalized seizures (lamotrigine, topiramate, zonisamide, perampanel) ⚠ | ⚠ | NCIT:C15986 | SMALL_MOLECULE | not MERRF-specific; ⚠ unsourced this session |
| **Avoid valproate** (+ aminoglycosides, linezolid, tobacco, alcohol) | valproic acid CHEBI:39867 ⚠ | Supportive Care **NCIT:C15747** ✓ | BEHAVIORAL | "VPA should be used with caution in PME due to mitochondrial dysfunction, i.e. in MERRF… because of its interaction with mitochondrial respiration and metabolism." — **PMID:16414077** [V] |
| **Cofactor/supplement "mito cocktail"** | coenzyme Q10 **CHEBI:46245** ✓, L-carnitine **CHEBI:16347** ✓, α-lipoic acid ⚠, vitamin E ⚠, B vitamins ⚠, creatine ⚠, riboflavin ⚠ | Nutritional Support **NCIT:C15433** ✓ | SMALL_MOLECULE (**not** BEHAVIORAL — see the CLAUDE.md warning about NCIT:C15433) | "Coenzyme Q10 (50-200 mg 2-3x/day), L-carnitine (1000 mg 2-3x/day), alpha lipoic acid, vitamin E, vitamin B supplements, and creatine… have been of modest benefit in some individuals." — **PMID:20301693** [V]. GeneReviews also lists **ubiquinol** [S]. No controlled trial establishes disease modification. |

**Pharmacogenomics:** the relevant interaction is genotype-driven drug *avoidance* (valproate, aminoglycosides, linezolid) rather than metabolizer-status dosing. No PharmGKB/CPIC guideline exists for MERRF. ⚠ Worth noting: *POLG*-related disease has the hardest valproate contraindication; the MERRF contraindication is mechanistically analogous but based on weaker evidence.

### Advanced / experimental therapeutics (none in patients)

**1. Mitochondrial tRNA import — proof of concept, in vitro (PMID:15317755 [V])**
Nuclear-encoded tRNA-Lys targeted into mitochondria partially rescued translation, complex activity, ΔΨm and respiration; rescue was abolished by siRNA knockdown of the transgene, proving specificity.

**2. Mitophagy stimulation (rapamycin) — in vitro (PMID:35922766 [V])**
> "The second approach, when administered chronically (4 weeks), induced a slight increase of mitochondrial respiration in fibroblasts with high-mutation load, and a significant improvement in fibroblasts with intermediate-mutation load, rescuing completely the bioenergetics defect."
> "This suggests that induction of mitochondrial biogenesis may not be sufficient to rescue mitochondrial dysfunction in MERRF cells with high-mutation load."
(The failed arm — PGC-1α overexpression / nicotinic acid — is as informative as the successful one.) CHEBI: sirolimus ⚠.

**3. Heteroplasmy-shifting nucleases — in vitro, MERRF-specific (NEW, a genuine KB gap)**
**Pereira, Bacman, … Moraes, *EMBO Mol Med* 2018, PMID:30012581** [V]:
> "We tested whether molecular hybrids (mitoTev-TALEs) could specifically bind and cleave mtDNA of patient-derived cybrids harboring different levels of the m.8344A>G mtDNA point mutation, associated with myoclonic epilepsy with ragged-red fibers (MERRF). We tested two mitoTev-TALE designs, one of which robustly shifted the mtDNA ratio toward the wild type. When this mitoTev-TALE was tested in a clone with high levels of the MERRF mutation (91% mutant), the shift in heteroplasmy resulted in an improvement of oxidative phosphorylation function."
> "mitoTALENs are dimeric and relatively large, making it difficult to package their coding genes into viral vectors, limiting their clinical application."

Related platform work: mitoTALENs generally (Bacman et al., *Nat Med* 2013, **PMID:23913125** — note this paper targeted a large deletion and m.14459G>A, **not** m.8344A>G; do not miscite it); in vivo mitoTALEN in the m.5024C>T mouse (*Nat Med* 2018); mtZFN tandem architecture (*EMBO Mol Med* 2025) ⚠. **Key mechanistic limitation for MERRF: DdCBE-type base editors perform C•G→T•A conversions, so reverting an A→G transition requires an adenine-capable mitochondrial editor (TALED-class), which remains preclinical.**

**4. Systemic drug candidates in trial (not MERRF-specific)**
- **KL1333** (NAD⁺ modulator, oral) — *Brain* 2025, **PMID:39657714** [V]: "KL1333 aims to normalize the NAD+:NADH ratio that is critical for ATP production… Results indicate KL1333 is safe and well tolerated, with dose-dependent gastrointestinal side effects, and validate potential novel outcome measures in primary mitochondrial disease including the 30-s Sit to Stand, and the patient-reported fatigue scales." Phase 2 pivotal study ongoing; open-label extension **NCT07514338** ⚠. Development explicitly names MERRF among target indications [S].
- **Sonlicromanol** (KH176) — phase 2 reported in *Brain*; primarily studied in m.3243A>G ⚠.
- **Elamipretide** — FDA-approved for Barth syndrome (2025) [S]; not approved for MERRF but establishes regulatory precedent.
- **Vatiquinone (PTC743)** — inherited mitochondrial disease trials, incl. **NCT05218655** ⚠.

⚠ **No interventional trial recruiting MERRF specifically was confirmed this session.** Any `clinical_trials` block should be built by querying ClinicalTrials.gov for "MERRF" directly and validating with `just fetch-reference NCT…`.

### Surgical / device / rehabilitative / supportive

- Cochlear implantation for severe sensorineural hearing loss (mitochondrial deafness responds well) ⚠; hearing aids.
- Cardiac: pacemaker/ICD for conduction disease; ablation for symptomatic WPW ⚠.
- Ptosis surgery / ptosis crutches ⚠.
- Gastrostomy for dysphagia; non-invasive ventilation for respiratory dysfunction (45% affected).
- Debulking of symptomatic lipomas ⚠.
- **Physical therapy and aerobic exercise** (**NCIT:C15302** ✓): "physical therapy to improve any impaired motor function; aerobic exercise" — **PMID:20301693** [V]. Occupational (**NCIT:C121351**) and speech therapy (**NCIT:C159273**) for dysarthria/dysphagia.
- **Genetic counseling** (**NCIT:C15240** ✓) — see §13.

### Surveillance (GeneReviews [S], worth curating as a management block)

Annual neurologic, ophthalmologic, cardiologic (ECG + echocardiogram) and endocrinologic evaluation; audiology every 2–3 years.

---

## 13. Prevention

- **Primary prevention of the disease:** not possible — the variant is present from conception. The only true primary prevention is **reproductive**.
- **Reproductive options and their limits:**
  > "because the mutational load in tissues sampled prenatally may shift in utero or after birth as a result of random mitotic segregation, prediction of the phenotype from prenatal studies is not possible." — **PMID:20301693** [V]

  Prenatal diagnosis and PGT are technically feasible and are offered, but cannot forecast phenotype. **Mitochondrial replacement therapy / mitochondrial donation** (licensed in the UK, and with first outcome reports published) is the only intervention that prevents transmission outright ⚠ — not confirmed against a primary source this session, but should be curated once verified, as it is the single most consequential preventive option for this disease class.
- **Secondary prevention:** cascade testing of maternal relatives; baseline and periodic cardiac (ECG/echo — asymptomatic WPW is silent until it isn't), audiologic, ophthalmologic and diabetes screening in identified carriers.
- **Tertiary prevention (preventing complications) — the practically important arm:**
  - Avoid valproate, aminoglycosides, linezolid, tobacco, alcohol.
  - Avoid prolonged fasting; aggressive management of intercurrent illness and dehydration; careful perioperative/anesthetic planning.
  - Treat WPW and cardiomyopathy before they cause events.
  - Aspiration precautions once dysphagia appears.
- **Immunization:** no MERRF-specific vaccine issue; routine immunization is *encouraged* because infection is a decompensation trigger.
- **Newborn/population screening:** none, and none justified at this prevalence with no disease-modifying therapy.
- **Public health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens* **NCBITaxon:9606**. **No naturally occurring animal disease equivalent to MERRF is documented.** OMIA has no MERRF entry (⚠ not directly queried this session — verify). This is expected: pathogenic heteroplasmic mt-tRNA point variants are purged efficiently by the germline bottleneck in most species and are essentially absent as spontaneous veterinary disease.
- **Orthologous gene:** mouse **mt-Tk** (mitochondrially encoded tRNA lysine) ⚠ — NCBI Gene ID not confirmed this session; do not curate an ID without checking.
- **Evolutionary conservation:** high. The mitochondrial genome's 22-tRNA translation system and the wobble taurine modification are deeply conserved across metazoa, which is why the mechanism generalizes — and why the *absence* of a natural animal model is a limitation rather than a biological difference.
- **Zoonotic potential / cross-species transmission:** **not applicable** (genetic disease).
- **Comparative pathology:** the closest comparative material is engineered — the heteroplasmic mouse mt-tRNA-Ala model (below), which reproduces the *class* of lesion (mt-tRNA point mutation, heteroplasmy, translation failure) in a different tRNA and a different target organ.

---

## 15. Model Organisms

### The honest headline: **there is no mouse model of MERRF.**

No transmitochondrial mouse carrying m.8344A>G (or a mt-tRNA-Lys equivalent) exists. Introducing defined point variants into mtDNA in vivo remains extremely difficult, and this is the field's central experimental bottleneck. Every mechanistic claim about MERRF in a whole organism therefore rests on human tissue.

### What actually exists

| Model | Type | What it captures | What it misses |
|---|---|---|---|
| **Cytoplasmic hybrids (cybrids)** — patient mtDNA into ρ⁰ recipient cells | IN_VITRO, human | The cleanest demonstration that the tRNA lesion alone is sufficient, independent of nuclear background; supports precise heteroplasmy titration (**PMID:10477264** [V]) | Dividing cells; no tissue architecture; no neurons |
| **Patient fibroblasts** | IN_VITRO, human | Threshold behavior, COX kinetics, ΔΨm, drug response (rapamycin — **PMID:35922766** [V]) | Not a post-mitotic, energy-limited cell |
| **iPSC-derived NPCs and cortical glutamatergic neurons** | IN_VITRO, human | **The best current model.** Retains patient heteroplasmy; reproduces bioenergetic deficit, ROS, antioxidant imbalance, neural immaturity, synaptic protein loss, and impaired spontaneous/evoked activity (**PMID:37605213** [V]) | Immature/fetal-like; no cerebellar dentate neurons; no aging; heteroplasmy can drift in culture |
| **mitoTev-TALE / mitoTALEN-engineered MERRF cybrid clones** | IN_VITRO, human | Heteroplasmy manipulation as an experimental variable and a therapeutic readout (**PMID:30012581** [V]) | Delivery, in vivo behavior untested for this variant |
| **m.5024C>T mt-tRNA-Ala mouse** (Kauppila 2016 ⚠) | MODEL_ORGANISM | The *class* model: heteroplasmic mt-tRNA point mutation → reduced steady-state mt-tRNA → impaired mitochondrial translation → hypertrophic cardiomyopathy; the standard platform for testing mitoTALEN/mtZFN/DdCBE in vivo | **Wrong tRNA, wrong target organ (heart, not cerebellum/cortex), no myoclonus, no epilepsy.** Any MERRF claim drawn from it is an extrapolation and should be marked `HUMAN_MODEL_MISMATCH`, not `MODEL_ORGANISM` support for a human phenotype |

### Genetic model types available

Knockout/knock-in/conditional/transgenic approaches used routinely for nuclear genes **do not transfer to mtDNA**: mtDNA is not amenable to homologous recombination, and there is no germline mtDNA transgenesis. Available genetic manipulations are limited to (a) cybrid transfer, (b) nuclease-based heteroplasmy shifting, (c) allotopic/nuclear-encoded rescue constructs, and (d) mtDNA-targeted base editors (C→T only, so **not** capable of reverting m.8344A>G as of this writing).

### Research applications and databases

Applications: threshold biology, drug screening (the iPSC platform is explicitly proposed for this — PMID:37605213 [V]), heteroplasmy-shifting therapeutics, synaptic/network consequences of bioenergetic failure.
Resources: MGI (for *mt-Tk* ⚠), IMSR, Cellosaurus (for MERRF cybrid lines ⚠), MITOMAP/MSeqDR for variant-level curation.

---

## Curation notes for the dismech entry

**Highest-value additions to `kb/disorders/MERRF_Syndrome.yaml`, ranked:**

1. **PMID:26995359 (mitoNET, n=34)** — supplies six frequency-quantified phenotypes the entry lacks (migraine 52%, psychiatric 54%, respiratory dysfunction 45%, GI 38%, dysarthria 36%, dysphagia 35%), a registry-scale onset figure (24.5 ± 10.9 y, 75% adult onset), a brain-atrophy frequency (43%), and — importantly — a third independent statement of the heteroplasmy–phenotype disconnect for the existing CONTROVERSY block.
2. **PMID:23635963 (Italian, n=42 + 321 pooled)** — the full frequency ladder at mean age ~35, and the "myoclonic ataxia rather than myoclonic epilepsy" reframing, which directly supports the nosological arm of the existing controversy.
3. **PMID:9315896 (Zhou/Attardi autopsy)** — nearly resolves the `merrf_regional_selectivity_gap`: single-cell regional heteroplasmy has *already* been measured and is inversely related to loss (Purkinje 97.6% load / 7% loss vs dentate / 46% loss). The proposed experiment in that discussion should be revised accordingly.
4. **PMID:37605213 (iPSC cortical neurons)** — human-cell mechanistic bridge from bioenergetics to synaptic dysfunction; strengthens the Cortical Neuronal Hyperexcitability node, which currently rests on EEG phenomenology.
5. **PMID:17989367 (AJNR MRI)** — the entry has no imaging `diagnosis` entry at all; superior-cerebellar-peduncle atrophy plus the clinico-radiological discrepancy is a distinctive diagnostic clue.
6. **PMID:30012581 (mitoTev-TALE)** — a MERRF-specific heteroplasmy-shifting result that belongs in the `merrf_disease_modifying_therapy_gap` discussion alongside the tRNA-import and rapamycin evidence (and makes the "two independent routes" framing into three).
7. **PMID:39657714 (KL1333 phase 1a/1b)** — the only trial-grade therapeutic evidence touching this disease class; also validates outcome measures.
8. A m.8344A>G-specific `prevalence` record (0.28/100,000 NE England; 0/100,000 northern Finland) distinct from the existing mtDNA-class upper bound.

**Before committing any of the above:** run `just fetch-reference` for every PMID marked **[S]** or ⚠, verify each snippet is an exact substring of the cached abstract, seed and validate all new HP/GO/CL/UBERON/CHEBI/NCIT terms with `just validate-terms`, and run the full `just qc`. Two citation hazards found in this session are worth remembering: **PMID:23913125 (Bacman 2013 mitoTALEN) did *not* target m.8344A>G** despite being widely cited as MERRF gene-therapy work, and the ***Brain Commun* 2024 "median age at death 55 years" figure is cohort-wide, not MERRF-specific** — both are exactly the kind of plausible-but-wrong claim that survives snippet validation.

---

## Sources

- [MERRF — GeneReviews (PMID:20301693)](https://www.ncbi.nlm.nih.gov/books/NBK1520/)
- [Phenotypic heterogeneity of the 8344A>G mtDNA "MERRF" mutation — Neurology 2013 (PMID:23635963)](https://pubmed.ncbi.nlm.nih.gov/23635963/)
- [Expanded phenotypic spectrum of the m.8344A>G "MERRF" mutation: German mitoNET registry — J Neurol 2016 (PMID:26995359)](https://pubmed.ncbi.nlm.nih.gov/26995359/)
- [MERRF: selective vulnerability of CNS neurons does not correlate with tRNAlys mutation level — J Neurosci 1997 (PMID:9315896)](https://www.jneurosci.org/content/17/20/7746)
- [Mitochondrial impairment and synaptic dysfunction in iPSC-derived cortical neurons of MERRF patients — J Biomed Sci 2023 (PMID:37605213)](https://pubmed.ncbi.nlm.nih.gov/37605213/)
- [Rapamycin rescues mitochondrial dysfunction in cells carrying m.8344A>G — Mol Med 2022 (PMID:35922766)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9347137/)
- [mitoTev-TALE: a monomeric DNA editing enzyme to reduce mutant mtDNA levels — EMBO Mol Med 2018 (PMID:30012581)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6127889/)
- [Specific elimination of mutant mitochondrial genomes by mitoTALENs — Nat Med 2013 (PMID:23913125)](https://pubmed.ncbi.nlm.nih.gov/23913125/)
- [Clinical and brain MR imaging features in MERRF due to A8344G — AJNR 2008 (PMID:17989367)](https://pubmed.ncbi.nlm.nih.gov/17989367/)
- [Epidemiology of the mtDNA 8344A>G mutation for MERRF — JNNP 2003 (PMID:12876264)](https://pubmed.ncbi.nlm.nih.gov/12876264/)
- [Optimizing rare disorder trials: phase 1a/1b of KL1333 — Brain 2025 (PMID:39657714)](https://academic.oup.com/brain/article/148/1/39/7911991)
- [Mitochondrial myopathies diagnosed in adulthood — Brain Commun 2024](https://academic.oup.com/braincomms/article/6/2/fcae041/7607785)
- [ClinVar: NC_012920.1(MT-TK):m.8344A>G / MERRF syndrome](https://www.ncbi.nlm.nih.gov/clinvar/RCV000010192/)
- [ICD-10-CM E88.42 MERRF syndrome](https://www.icd10data.com/ICD10CM/Codes/E00-E89/E70-E88/E88-/E88.42)
- [Myoclonic Epilepsy and Ragged Red Fibers — StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK555923/)
- [Diagnosis and management of mitochondrial disease: Mitochondrial Medicine Society consensus (PMID:25503498)](https://pubmed.ncbi.nlm.nih.gov/25503498/)
- [Milder phenotype of homoplasmic vs heteroplasmic m.8344A>G in the same family (PMID:36176839)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9513505/)
- [A novel MTTK gene variant m.8315A>C as a cause of MERRF syndrome](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9319148/)
- [MT-TK gene overview](https://www.genecards.org/cgi-bin/carddisp.pl?gene=MT-TK)
- [Newcastle mitochondrial disease quality-of-life measure development](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3841574/)