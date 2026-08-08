---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T00:35:45.448780'
end_time: '2026-08-01T00:53:08.737317'
duration_seconds: 1043.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: OTUD6B-Related Neurodevelopmental Disorder
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
  web_search_requests: 6
  num_turns: 96
  total_cost_usd: 6.312819999999997
  session_id: 4c6c13d8-4ee2-4dbf-a9e8-979c524ffbbd
  stop_reason: end_turn
citation_count: 40
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** OTUD6B-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **OTUD6B-Related Neurodevelopmental Disorder** covering all of the
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

# OTUD6B‑Related Neurodevelopmental Disorder (IDDFSDA) — Comprehensive Research Report

**Prepared:** 2026‑08‑01 · **Target entity:** OTUD6B‑Related Neurodevelopmental Disorder · **MONDO:0044319**

---

## ⚠️ Curation Preflight Notes (read before using this report)

Three disambiguation hazards apply to this entity and should be treated as **Named Entity Confusion (NEC) risk** per the dismech DR SOP:

1. **`OTUD6B-AS1` is a different molecular entity.** Of ~76 PubMed records for "OTUD6B," the large majority (≈40) concern **OTUD6B‑AS1**, a long non‑coding antisense RNA transcribed at the same 8q21.3 locus, studied almost exclusively as a cancer biomarker (breast, colorectal, cervical, thyroid, bladder). None of these bear on the neurodevelopmental disorder. Do not cite OTUD6B‑AS1 papers as OTUD6B evidence.
2. **`OTUD7A` is a different DUB / different NDD gene.** OTUD7A (15q13.3 microdeletion driver, MIM 612024) also causes a DUB‑related NDD with epilepsy and ID (PMID:36604605). It is a sister-gene confusion, not the same disease.
3. **`OTUD6A` is a paralog** at Xq26.1, not currently a Mendelian disease gene.

**MONDO identity anchors verified:** MONDO:0044319 carries xrefs `OMIM:617452`, `Orphanet:505237`, `GARD:0017942`, `MEDGEN:1375601`, `UMLS:C4479520`, and sits under `MONDO:0000508` (syndromic intellectual disability) — matching the ClinGen gene‑disease validity assertion (below). Causal gene = **OTUD6B**. Preflight passes.

**Protein numbering discrepancy to resolve before curating catalytic residues:** UniProt canonical Q8N6M0 is a **293‑aa** protein with the OTU domain at **residues 147–284** and catalytic residues **Cys158 (nucleophile) / His277**. The original AJHG paper's full text (per PMC5384096) describes a **323‑aa** protein with a predicted active site of "Asp185, Cys188, and His307" — an offset consistent with a longer alternative isoform's numbering. **All clinically reported variants use NM_016023.5 / 293‑aa numbering** (e.g., p.Lys291AsnfsTer3 is near the C‑terminus of a 293‑aa protein). Anchor on the 293‑aa numbering; flag the 323‑aa figures as isoform‑dependent.

**Verbatim status of quotations below:** Abstract text marked with `>` block quotes was retrieved verbatim from PubMed record pages and is suitable for evidence `snippet:` use *after* `just fetch-reference` + `just validate-references`. Figures attributed to **PMC5384096 full text** were extracted by an automated reader and are **paraphrase-risk** — verify against the article before using as snippets.

---

## 1. Disease Information

### 1.1 Overview

OTUD6B‑related neurodevelopmental disorder is a **rare autosomal recessive multisystem developmental disorder** caused by biallelic loss‑of‑function variants in *OTUD6B*, which encodes an ovarian‑tumour (OTU)‑domain deubiquitinating enzyme. The core phenotype is global developmental delay and intellectual disability with early‑onset seizures, a recognizable dysmorphic facial gestalt, and distal limb anomalies (notably broad distal phalanges/thumbs with persistent fetal fingertip pads). Prenatal‑onset growth restriction, microcephaly, hypotonia, feeding difficulty, structural brain anomalies, and congenital heart disease are frequent. Severity is strikingly bimodal: predicted‑null biallelic genotypes produce a severe, often non‑ambulatory, non‑verbal, gastrostomy‑dependent phenotype, whereas hypomorphic missense/leaky‑splice genotypes may produce only mild‑to‑moderate ID with preserved speech and ambulation.

The disorder was defined in 2017 by Santiago‑Sim et al. in the *American Journal of Human Genetics* (PMID:28343629), with 12 individuals from 6 families:

> Ubiquitination is a posttranslational modification that regulates many cellular processes including protein degradation, intracellular trafficking, cell signaling, and protein-protein interactions. Deubiquitinating enzymes (DUBs), which reverse the process of ubiquitination, are important regulators of the ubiquitin system. OTUD6B encodes a member of the ovarian tumor domain (OTU)-containing subfamily of deubiquitinating enzymes. Herein, we report biallelic pathogenic variants in OTUD6B in 12 individuals from 6 independent families with an intellectual disability syndrome associated with seizures and dysmorphic features. In subjects with predicted loss-of-function alleles, additional features include global developmental delay, microcephaly, absent speech, hypotonia, growth retardation with prenatal onset, feeding difficulties, structural brain abnormalities, congenital malformations including congenital heart disease, and musculoskeletal features. Homozygous Otud6b knockout mice were subviable, smaller in size, and had congenital heart defects, consistent with the severity of loss-of-function variants in humans. Analysis of peripheral blood mononuclear cells from an affected subject showed reduced incorporation of 19S subunits into 26S proteasomes, decreased chymotrypsin-like activity, and accumulation of ubiquitin-protein conjugates. Our findings suggest a role for OTUD6B in proteasome function, establish that defective OTUD6B function underlies a multisystemic human disorder, and provide additional evidence for the emerging relationship between the ubiquitin system and human disease.
> — *Santiago‑Sim T et al., Am J Hum Genet 2017;100(4):676‑688. doi:10.1016/j.ajhg.2017.03.001 (PMID:28343629)*

### 1.2 Key identifiers

| Resource | Identifier | Label |
|---|---|---|
| **MONDO** | `MONDO:0044319` | intellectual developmental disorder with dysmorphic facies, seizures, and distal limb anomalies |
| **OMIM (phenotype)** | `#617452` | INTELLECTUAL DEVELOPMENTAL DISORDER WITH DYSMORPHIC FACIES, SEIZURES, AND DISTAL LIMB ANOMALIES; IDDFSDA |
| **OMIM (gene)** | `*612021` | OTU DOMAIN‑CONTAINING PROTEIN 6B; OTUD6B |
| **Orphanet** | `ORPHA:505237` | Early‑onset seizures–distal limb anomalies–facial dysmorphism–global developmental delay syndrome |
| **ICD‑10** | `Q87.8` | Other specified congenital malformation syndromes NEC (via Orphanet mapping) |
| **ICD‑11** | *no dedicated code*; nearest is LD2F "syndromes with intellectual disability as a major feature" (⚠️ not independently verified) |
| **MedGen / UMLS** | `C4479520` (MedGen UID 1375601) | — |
| **GARD** | `GARD:0017942` | — |
| **HGNC (gene)** | `HGNC:24281` (dismech form: `hgnc:24281`) | OTU deubiquitinase 6B |
| **Entrez Gene** | `51633` | — |
| **Ensembl** | `ENSG00000155100` | — |
| **UniProt** | `Q8N6M0` | Deubiquitinase OTUD6B |
| **RefSeq transcript** | `NM_016023.5` | reference transcript used by ClinVar |
| **Cytoband** | `8q21.3` | GRCh38 chr8:91,070,196–91,087,095 |

### 1.3 Synonyms and alternative names

- IDDFSDA (OMIM acronym)
- OTUD6B‑related syndrome / OTUD6B‑related disorder / OTUD6B‑associated intellectual disability
- Intellectual disability syndrome with seizures and dysmorphic features
- Early‑onset seizures–distal limb anomalies–facial dysmorphism–global developmental delay syndrome (Orphanet preferred term)

**Gene aliases:** `CGI-77`, `DUBA5`; previous HGNC symbol "OTU domain containing 6B".

### 1.4 Information provenance

This is an **aggregated disease‑level** entity, not an EHR‑derived one. The knowledge base is built entirely from published case reports and small family series (n ≈ 28–30 individuals worldwide as of 2025), plus curated aggregators (OMIM, Orphanet, ClinGen, HPO, ClinVar). There is **no registry, no natural‑history cohort, and no EHR phenotype algorithm** for this disorder. The 2025 BMC Pediatrics report states verbatim:

> There have been < 30 reported cases globally without fundus and retinal lesions.
> — *Novel variant causing OTUD6B-related syndrome with ocular dysplasia and hypothyroidism: the first Chinese case. BMC Pediatr. 2025 Nov 4;25(1):905 (PMID:41188742, PMC12584513)*

---

## 2. Etiology

### 2.1 Disease causal factors

**Single, monogenic cause:** biallelic (homozygous or compound heterozygous) pathogenic variants in *OTUD6B*. No environmental, infectious, or multifactorial etiology has been described or is biologically plausible for this entity. The etiologic mechanism is **loss of function** of the OTUD6B deubiquitinase, with resulting perturbation of ubiquitin‑dependent proteostasis — specifically 26S proteasome assembly/activity — during embryonic and postnatal development.

### 2.2 Risk factors

**Genetic (causal):**
- Two pathogenic *OTUD6B* alleles. Reported allele classes: nonsense, frameshift, canonical splice‑site (with demonstrated aberrant splicing), and rare missense variants localized to the OTU catalytic domain.
- **Consanguinity** is the dominant risk amplifier. Reported families are overwhelmingly consanguineous — Turkish, Egyptian (two unrelated families, PMID:34354232), Saudi/Gulf, Mexican, Spanish, Italian, Chinese. Founder/recurrent alleles: **c.433C>T (p.Arg145\*)** was homozygous in three of the six original families and independently in the Mexican proband, consistent with either a recurrent CpG transition or a shared haplotype.
- **Second‑locus / blended phenotypes** — an under‑appreciated etiologic modifier in this disorder. Three published probands carry a *second* pathogenic locus that contributes phenotype: a homozygous *RP1L1* nonsense variant causing retinal degeneration in Egyptian Family I (PMID:34354232); a heterozygous *PKD1* variant contributing renal cystic disease alongside Tetralogy of Fallot (PMID:35707595); and a *ZMIZ1* splice variant co‑occurring with an *OTUD6B* point mutation + 8q21.3 microdeletion (PMID:34680978).

**Environmental risk factors:** none identified. No toxin, exposure, maternal factor, parity, or ascertainment‑independent sex effect has been reported.

**Age/sex:** onset is congenital‑to‑infantile in all reported cases. No sex bias is expected (autosomal recessive); reported cohorts include both sexes with no reported skew, though n is far too small to test.

### 2.3 Protective factors

- **Genetic:** the only demonstrated modifier of severity is **residual OTUD6B activity**. Hypomorphic missense alleles and leaky splice alleles are associated with markedly milder disease. Two structural‑modelling studies make this explicit — PMID:35430327 concluded that **p.Tyr216Cys** (milder phenotype) causes "localized destabilization" whereas **p.Ile274Arg** (severe phenotype) causes "significant distortion in the overall fold of OTUD6B." Similarly, PMID:30364145's Italian proband with two splice variants retained "less than 1% of wild-type transcripts" yet had only **mild** ID — indicating that the genotype–severity map is not fully resolved and that trace residual protein may be disproportionately protective (or that other modifiers exist).
- **Environmental protective factors:** none identified. Standard heterozygote carriers are unaffected (pLI 0; see §4.2).

### 2.4 Gene–environment interactions

None established. One clinically relevant *gene–physiology* interaction is worth flagging for the pathograph: the Chinese proband's seizures were **febrile** ("two episodes of febrile seizure" at 13 and 17 months, PMID:41188742) — raising a hypothesis, currently unsupported by cohort data, that intercurrent illness/pyrexia lowers seizure threshold in this proteostasis disorder. This should be curated at most as a `KNOWLEDGE_GAP` discussion, not as an asserted mechanism.

---

## 3. Phenotypes

### 3.1 Authoritative HPO annotation set (OMIM:617452)

Retrieved from `https://ontology.jax.org/api/network/annotation/OMIM:617452`. Frequencies are the HPOA `n/m` counts, derived from the 12‑individual founding cohort (PMID:28343629) except cardiac terms, which are n/6.

| HPO ID | Term | Frequency | Notes |
|---|---|---|---|
| **HP:0010864** | Severe intellectual disability | **12/12 (100%)** | Core; but see §3.3 — milder alleles give mild/moderate ID |
| **HP:0001250** | Seizure | **12/12 (100%)** | Early‑onset |
| **HP:0001263** | Global developmental delay | (not quantified) | Universal |
| **HP:0000252** | Microcephaly | **9/12 (75%)** | Onset `HP:0003593` (Infantile onset) |
| **HP:0002194** | Delayed gross motor development | **9/12 (75%)** | Onset `HP:0003593` |
| **HP:0000750** | Delayed speech and language development | **9/12 (75%)** | Absent speech in the severe group |
| **HP:0001290** | Generalized hypotonia | **9/12 (75%)** | |
| **HP:0011968** | Feeding difficulties | **9/12 (75%)** | G‑tube dependence in severe cases |
| **HP:0001511** | Intrauterine growth retardation | **7/12 (58%)** | Onset `HP:0030674` (Antenatal onset) |
| **HP:0004322** | Short stature | **7/12 (58%)** | |
| **HP:0000343** | Long philtrum | **7/12 (58%)** | Facial gestalt |
| **HP:0000400** | Macrotia | **7/12 (58%)** | Facial gestalt |
| **HP:0011304** | Broad thumb | **6/12 (50%)** | Distal limb anomaly |
| **HP:0004325** | Decreased body weight | **6/12 (50%)** | |
| **HP:0000219** | Thin upper lip vermilion | **6/12 (50%)** | Facial gestalt |
| **HP:0000637** | Long palpebral fissure | **6/12 (50%)** | Kabuki‑overlap feature |
| **HP:0000426** | Prominent nasal bridge | **5/12 (42%)** | Facial gestalt |
| **HP:0002650** | Scoliosis | **5/12 (42%)** | |
| **HP:0000278** | Retrognathia | **4/12 (33%)** | |
| **HP:0001845** | Overlapping toe | **3/12 (25%)** | |
| **HP:0000729** | Autistic behavior | **3/12 (25%)** | |
| **HP:0002079** | Hypoplasia of the corpus callosum | **3/12 (25%)** | Brain MRI |
| **HP:0000470** | Short neck | **3/12 (25%)** | |
| **HP:0002553** | Highly arched eyebrow | **3/12 (25%)** | Kabuki‑overlap feature |
| **HP:0200021** | Down‑sloping shoulders | **3/12 (25%)** | |
| **HP:0001631** | Atrial septal defect | **3/6 (50%)** | Cardiac |
| **HP:0001629** | Ventricular septal defect | **2/6 (33%)** | Cardiac; matches the mouse |
| **HP:0002510** | Spastic tetraplegia | **2/12 (17%)** | Severe group |
| **HP:0012450** | Chronic constipation | **2/12 (17%)** | |
| **HP:0000960** | Sacral dimple | **2/12 (17%)** | |
| **HP:0000248** | Brachycephaly | **1/12 (8%)** | |
| **HP:0000007** | Autosomal recessive inheritance | — | Inheritance term |

**Annotated without frequency:** `HP:0002119` Ventriculomegaly · `HP:0002540` Inability to walk · `HP:0001508` Failure to thrive · `HP:0001371` Flexion contracture · `HP:0000028` Cryptorchidism · `HP:0000369` Low‑set ears · `HP:0000411` Protruding ear · `HP:0000377` Abnormal pinna morphology · `HP:0000365` Hearing impairment · `HP:0001276` Hypertonia · `HP:0000527` Long eyelashes · `HP:0000218` High palate · `HP:0000276` Long face · `HP:0000494` Downslanted palpebral fissures · `HP:0005469` Flat occiput · `HP:0000431` Wide nasal bridge · `HP:0001762` Talipes equinovarus · `HP:0001182` Tapered finger.

### 3.2 Post‑2017 phenotypic expansions (each from a specific report)

| Feature | Source | Suggested HPO (⚠️ verify with `just validate-terms`) |
|---|---|---|
| **Persistent fetal fingertip pads**; broad distal phalanges of thumbs and halluces with prominent interphalangeal joints — called **pathognomonic** | PMID:34354232 (verbatim: *"Broad distal phalanges (especially the thumbs and halluces) with prominent interphalangeal joints and fetal pads were recognized in all patients and hence considered pathognomonic."*) | `HP:0001212` Prominent fingertip pads; `HP:0011304` Broad thumb; `HP:0010511` Broad hallux |
| **Orodental features:** macrodontia, dental crowding, abnormally shaped teeth, thick alveolar ridges | PMID:34354232 (verbatim: *"various orodental features were present including macrodontia, dental crowding, abnormally shaped teeth, and thick alveolar ridges"*) | `HP:0001572` Macrodontia; `HP:0000678` Dental crowding; `HP:0006482` Abnormal dental morphology |
| **Delayed eruption of primary dentition; soft doughy skin with reduced sweating; mirror movements** | PMID:38389298 (verbatim: *"previously unreported clinical manifestations such as delayed eruption of primary dentition, soft doughy skin with reduced sweating, and mirror movements present in our patients suggest an expansion of the phenotype"*) | `HP:0000680` Delayed eruption of teeth; `HP:0000966` Hypohidrosis; `HP:0004302` Mirror movements |
| **Hypothyroidism** and **hypogammaglobulinemia** — third reported patient with both | PMID:32924626 (verbatim: *"this is the third patient with associated hypothyroidism and hypogammaglobulinemia, underscoring the value of screening for these conditions in other patients"*) | `HP:0000821` Hypothyroidism; `HP:0004313` Decreased circulating antibody level |
| **Ocular developmental anomalies:** nystagmus, optic disc hypoplasia, retinal abnormalities — first report | PMID:41188742 (verbatim: *"Significantly, none of the 27 previously reported IDDFSDA cases exhibited ocular developmental abnormalities."*) | `HP:0000639` Nystagmus; `HP:0000609` Optic nerve hypoplasia |
| **Tetralogy of Fallot** (index case + a prior medically terminated pregnancy in the same family) | PMID:35707595 | `HP:0001636` Tetralogy of Fallot |
| **Renal parenchymal disease with simple cortical cysts** (blended with a heterozygous *PKD1* variant) | PMID:35707595 | `HP:0000107` Renal cyst |
| **Williams‑syndrome‑like facial features:** periorbital edema, hanging cheek, long smooth philtrum; **polydactyly** | PMID:34680978 (verbatim: *"We suggest that Williams syndrome-like phenotypes, namely, periorbital edema, hanging cheek, and long and smooth philtrum represent expanded phenotypes of OTUD6B-related ID."*) | `HP:0100539` Periorbital edema; `HP:0000174` Abnormality of the palate; `HP:0010442` Polydactyly |
| **Vertebral anomaly** | PMID:38389298 | `HP:0003468` Abnormal vertebral morphology (⚠️ verify) |
| Brain MRI: white matter abnormalities, cortical atrophy (in addition to hypoplastic CC and ventriculomegaly) | Orphanet ORPHA:505237 summary | `HP:0002500` Abnormal cerebral white matter morphology; `HP:0002059` Cerebral atrophy |
| **Abnormal cytoplasmic inclusions in lymphocytes** (cellular phenotype) | PMC5384096 full text (⚠️ paraphrase‑risk) | *no direct HPO*; curate as `category: Cellular` |

### 3.3 Phenotype characteristics

**Age of onset.** Congenital‑to‑infantile. Prenatal onset is documented in a substantial minority: IUGR is annotated with HPO onset term `HP:0030674` (Antenatal onset) at 7/12, and one family had a pregnancy medically terminated for antenatally diagnosed Tetralogy of Fallot (PMID:35707595). Microcephaly and motor delay carry HPO onset `HP:0003593` (Infantile onset). Orphanet records age of onset as **infancy**. GARD summarizes symptom emergence at **1–23 months**.

**Severity — a genuinely bimodal distribution.** This is the single most curation‑relevant characteristic of the disorder and should be modelled as `has_subtypes` or at minimum as an explicit severity axis:
- **Severe (predicted‑null biallelic genotypes):** microcephaly, absent speech, inability to walk, feeding‑tube dependence, spastic quadriplegia. MedGen summarizes: *"The most severely affected patients have a neurodevelopmental disorder with microcephaly, absent speech, and inability to walk, and they require feeding tubes."*
- **Mild (hypomorphic missense / leaky splice):** *"less severely affected individuals have mild to moderate intellectual disability with normal speech and motor development."* The Italian proband (PMID:30364145) is the archetype — *"mild intellectual disability, speech and motor delay, and recurrent seizures."*

PMID:35430327 makes the genotype→severity link explicit and computational: *"our findings support that the clinical severity could be related with the predicted functional severity of the variations in OTUD6B."*

Critically, **intra‑familial variability also exists** — PMID:34354232: *"our patients showed inter- and intrafamilial differences with regard to the clinical and brain imaging findings."* This argues against a purely genotype‑determined severity model and supports curating an unresolved modifier gap.

**Progression.** No natural‑history study exists. The disorder is best characterized as a **static (non‑degenerative) encephalopathy** with a congenital structural/developmental basis — brain MRI shows malformation (corpus callosum hypoplasia, ventriculomegaly) rather than progressive atrophy in most reports, though cortical atrophy is listed by Orphanet. Seizures are recurrent/episodic on a chronic lifelong background. Scoliosis and contractures are expected to be **progressive** secondary orthopedic complications of hypotonia/spasticity. **This progression characterization is an inference from the reported feature set, not a cited finding — flag as a knowledge gap.**

**Frequency evidence discipline.** Per `docs/frequency-evidence-guidelines.md`, the HPOA `n/12` counts are *derived counts* from the founding cohort and are acceptable justification for `FrequencyEnum` bands. However, they reflect a **single ascertainment‑biased cohort of predominantly severe cases**; frequencies for the mild end of the spectrum are almost certainly overstated (e.g., "Severe intellectual disability 12/12" is contradicted by later mild cases). Recommend curating the HPOA frequencies with an explicit note, or omitting `frequency:` for terms where the 2018–2025 literature conflicts with the 2017 cohort.

**Quality of life.** No EQ‑5D, PROMIS, SF‑36, or disease‑specific QoL instrument has been applied. The only QoL statement in the literature is a clinical aspiration, from PMID:32924626: *"The current challenge with this patient is to ensure medical management of his seizures and provide him with a better quality of life."* Expected QoL burden is dominated by (a) refractory seizures, (b) non‑verbal status and total care dependence in the severe group, (c) feeding‑tube dependence, and (d) caregiver burden. **Mark as a knowledge gap.**

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

**OTUD6B** (`hgnc:24281`; OMIM \*612021; Entrez 51633; Ensembl ENSG00000155100; UniProt Q8N6M0), 8q21.3, reference transcript **NM_016023.5**. Encodes a **293‑aa** cysteine‑protease deubiquitinase of the OTU family.

UniProt Q8N6M0 FUNCTION comment (verbatim):
> [Isoform 1]: Deubiquitinating enzyme that may play a role in the ubiquitin-dependent regulation of protein synthesis, downstream of mTORC1. May associate with the protein synthesis initiation complex and modify its ubiquitination to repress translation. May also repress DNA synthesis and modify different cellular targets thereby regulating cell growth and proliferation. May also play a role in proteasome assembly and function. [Isoform 2]: Stimulates protein synthesis. Influences the expression of CCND1/cyclin D1 by promoting its translation and regulates MYC/c-Myc protein stability.

**Domain architecture:** N‑terminal coiled‑coil region + **OTU catalytic domain, residues 147–284**. Catalytic triad residues: **Cys155/Cys158 (Cys158 is the nucleophile), His277**. Cys→Ser mutation of the nucleophile abolishes DUB activity (functionally demonstrated in PMID:21267069: *"Mutation of the conserved Cys residue abolished its deubiquitinating activity in vitro."*).

**Two functionally opposed splice isoforms.** Isoform 2 (OTUD6B‑2) differs by replacement of residues 1–105 with "MISK." This is not a curatorial footnote — the isoforms have **antagonistic** effects on translation (PMID:27864334, §6.2), which is relevant to interpreting variant consequence: a variant in exon 1–3 may affect only OTUD6B‑1.

### 4.2 Gene constraint (gnomAD v4.0, via ClinGen)

| Metric | Value | Interpretation |
|---|---|---|
| **pLI** | **0** | Not LoF‑intolerant in the heterozygous state |
| **LOEUF** | **1.48** | Far above the 0.35 haploinsufficiency threshold |
| **DECIPHER %HI** | **30.63** | Moderate, but not a haploinsufficiency signal |

These metrics are **exactly what is expected for a recessive disease gene** and should not be read as evidence against pathogenicity. Heterozygous carriers (including all obligate parents in the reported families) are unaffected. This is an important curation point: an automated pipeline keying on pLI would incorrectly deprioritize OTUD6B.

### 4.3 ClinGen gene–disease validity

**Classification: DEFINITIVE.** ClinGen (`search.clinicalgenome.org/kb/genes/HGNC:24281`) records one gene‑disease validity assertion:

- Gene: **OTUD6B** (HGNC:24281)
- Disease: **syndromic intellectual disability** (`MONDO:0000508`)
- Mode of inheritance: **Autosomal recessive**
- Classification: **Definitive**
- Expert panel: **Intellectual Disability and Autism Gene Curation Expert Panel**
- Date: **2024‑08‑22**

No ClinGen dosage‑sensitivity, actionability, or variant‑pathogenicity curations exist for this gene. No CPIC/PharmGKB records. → A `CGGV:` structured‑source citation should be retrievable for this assertion via `just clingen-refresh` / `just clingen-list`.

### 4.4 Reported pathogenic variants (literature)

All in **NM_016023.5** numbering. Zygosity as reported.

| cDNA | Protein | Class | Zygosity | Family / population | Source |
|---|---|---|---|---|---|
| **c.433C>T** | **p.Arg145\*** | nonsense | homozygous | Families 1, 2, 3 (2017 cohort); independently the **first Mexican** proband | PMID:28343629; PMID:32924626 |
| c.469_473delTTAAC | p.Leu157Argfs\*8 | frameshift | homozygous | Family 4 (2017) | PMID:28343629 |
| c.173−2A>G | — (splice acceptor) | canonical splice | homozygous | Family 5 (2017) | PMID:28343629 |
| **c.647A>G** | **p.Tyr216Cys** | missense (OTU domain) | homozygous | Family 6 (2017); **milder** phenotype | PMID:28343629; modelled PMID:35430327 |
| c.324+1G>C | — | splice donor, exon 2 | compound het (with below) | Italian proband; **mild** ID | PMID:30364145 |
| c.405+1G>A | — | splice donor, exon 3 | compound het (with above) | Italian proband | PMID:30364145 |
| **c.271C>T** | **p.Gln91Ter** | nonsense | homozygous | Egyptian Family I | PMID:34354232 |
| **c.767G>T** | **p.Gly256Val** | missense (OTU domain) | homozygous | Egyptian Family II | PMID:34354232 |
| **c.873delA** | **p.Lys291AsnfsTer3** | frameshift | *hemizygous* (in trans with a paternal 0.118 Mb 8q21.3 deletion, chr8:92,084,087–92,202,189) | 5‑yr‑old girl; also carried *ZMIZ1* c.1491+2T>C | PMID:34680978 |
| **c.815T>G** | **p.Ile272Arg** | missense (OTU domain) | homozygous | Tetralogy of Fallot proband; also het *PKD1* variant | PMID:35707595 |
| p.Ile274Arg *(cDNA not stated in abstract)* | p.Ile274Arg | missense (OTU domain) | compound het with a novel frameshift | severe IDDFSDA index case | PMID:35430327 |
| **c.479A>G** | **p.Tyr160Cys** | missense (likely pathogenic) | compound het (with below) | first Chinese case; ocular anomalies + hypothyroidism | PMID:41188742 |
| **c.83−1delG** | — (splice acceptor) | pathogenic splice | compound het (with above) | first Chinese case | PMID:41188742 |
| *(2 variants, not specified in abstract)* | — | — | biallelic | 3 siblings, Kabuki‑syndrome‑like presentation | PMID:38389298 |
| *(not specified in abstract)* | — | — | biallelic | first Spanish case | PMID:31147255 |

**ClinVar (NM_016023.5) additional P/LP small variants** not tied to a specific publication above, confirmed by esummary:
- `c.287del` (p.Pro96fs) — Pathogenic — IDDFSDA
- `c.776C>G` (p.Ser259Ter) — Pathogenic
- `c.381_388del` (p.Leu127fs) — Pathogenic — IDDFSDA
- `c.401A>G` (p.Glu134Gly) — Likely pathogenic — IDDFSDA
- `c.83-1del` — Pathogenic — IDDFSDA (matches PMID:41188742)

**ClinVar counts (2026‑08‑01, via E‑utilities):** 151 total records for OTUD6B; 54 records classified P/LP. **Important caveat:** the majority of the 54 are large chromosome‑8 copy‑number gains/losses that merely span the locus, not gene‑level small variants. The number of distinct P/LP *small* OTUD6B variants is on the order of 10–15. Do not cite "54 pathogenic OTUD6B variants" without this qualification.

**Variant spectrum summary:**
- **Class distribution:** nonsense ≈ 4; frameshift ≈ 4; canonical splice ≈ 4; missense ≈ 5 (all within or adjacent to the OTU domain: Tyr160, Tyr216, Gly256, Ile272/274 — plus Glu134 just N‑terminal); one whole‑gene microdeletion in trans with a point mutation.
- **Missense clustering in the OTU domain (147–284)** is a notable pattern supporting a domain‑restricted missense hotspot and useful for PM1‑type ACMG evidence.
- **Somatic vs germline:** all disease variants are **germline**. Somatic OTUD6B alteration is not a described mechanism in this disorder; OTUD6B's cancer roles (§6.2) are **expression‑level**, not mutational.
- **Allele frequency:** all reported disease alleles are absent or ultra‑rare in gnomAD. PMID:30364145 states verbatim: *"Both variants are reported in the GnomAD database with a frequency lower than the 10‑5 and affect the donor splicing site, of exons 2 and 3, respectively."*
- **Functional consequence:** **loss of function** throughout. Nonsense/frameshift alleles are predicted to trigger NMD (explicitly modelled in PMID:35430327: *"The truncating frameshift variant in one allele was predicted to undergo degradation via nonsense-mediated decay of the mRNA molecule."*); splice alleles cause exon skipping with near‑total loss of wild‑type transcript; missense alleles cause fold destabilization of varying severity. **No gain‑of‑function or dominant‑negative mechanism has been proposed.**

### 4.5 Functional validation of splice variants

PMID:30364145 provides the strongest direct RNA evidence in the disorder:
> RT-PCR experiments demonstrated that both variants affect _OTUD6B_ splicing and lead to the production of aberrant transcripts, the major ones being, in both cases, the skipping of the upstream exon. Quantitative analysis performed by competitive-fluorescent RT-PCR on the patient RNA showed that the proband presents less than 1% of wild-type transcripts, further strengthening the causative role of these variants.

### 4.6 Modifier genes, epigenetics, chromosomal abnormalities

- **Modifier genes:** none identified. The three "blended phenotype" second loci (*RP1L1*, *PKD1*, *ZMIZ1*) are **independent co‑occurring conditions**, not modifiers of the OTUD6B phenotype — PMID:34354232 is explicit that *"Retinal degeneration, albeit present in both patients from Family I, was shown to be unrelated to OTUD6B."* This is a valuable curation exemplar of DR‑style over‑attribution risk.
- **Epigenetics:** No episignature has been published for OTUD6B‑related disorder. (Given the Kabuki‑syndrome mimicry documented in PMID:38389298 and PMID:30364145, this is a concrete, high‑value research gap — DNA‑methylation episignature classifiers already discriminate Kabuki syndrome, so an OTUD6B episignature would be a plausible diagnostic advance.) **No data available.**
- **Chromosomal abnormalities:** one reported case with a **0.118 Mb paternally inherited deletion of 8q21.3 (chr8:92,084,087–92,202,189)** encompassing OTUD6B, in trans with a maternal point mutation (PMID:34680978). This establishes that CMA can contribute the second hit and must be part of the diagnostic strategy (§10.2). Verbatim: *"The CMA showed a paternally inherited 0.118 Mb deletion of 8q21.3, chr8:92084087-92202189, with OTUD6B involved."*

---

## 5. Environmental Information

**Not applicable.** OTUD6B‑related neurodevelopmental disorder is a fully penetrant monogenic recessive condition. There are no reported environmental factors, lifestyle factors, toxicant exposures, or infectious agents that cause, trigger, or modify this disorder. No CTD/TOXNET association exists.

Two peripheral points worth recording as *non‑etiologic*:
- The **febrile** trigger for the two seizures in the 2025 Chinese case (PMID:41188742) is a symptom‑precipitant observation, not an environmental etiology.
- OTUD6B has documented **antiviral innate‑immunity** roles (§6.6). Whether patients with biallelic LoF have altered antiviral responses **has not been tested in humans** and must not be asserted. The reported **hypogammaglobulinemia** in three patients (PMID:32924626) is the only human immune signal.

---

## 6. Mechanism / Pathophysiology

### 6.1 The primary disease mechanism: impaired 26S proteasome assembly

This is the only mechanism established in **patient material** and should be the backbone of the pathograph.

**Causal chain (patient‑derived, PMID:28343629):**

```
Biallelic LoF OTUD6B variant  [MOLECULAR]
  → Loss of OTUD6B deubiquitinase activity  [MOLECULAR]
    → Reduced incorporation of 19S regulatory-particle subunits into 26S proteasomes;
      accumulation of 19S precursor complexes  [MOLECULAR]
      → Decreased 26S chymotrypsin-like peptidase activity  [MOLECULAR]
        → Accumulation of ubiquitin-protein conjugates; cytoplasmic inclusions in lymphocytes  [CELLULAR]
          → Impaired proteostasis in developing neural, cardiac and skeletal tissue  [TISSUE]
            → Multisystem developmental disorder  [ORGANISM]
```

The abstract‑level evidence sentence (verbatim, PMID:28343629): *"Analysis of peripheral blood mononuclear cells from an affected subject showed reduced incorporation of 19S subunits into 26S proteasomes, decreased chymotrypsin-like activity, and accumulation of ubiquitin-protein conjugates."*

**Quantitative detail from the full text (PMC5384096) — ⚠️ paraphrase‑risk, verify before citing as snippets:**
- Native PAGE: "substantially reduced incorporation of Rpn5 and Rpt6 subunits into 26S proteasomes," with Rpn5 reduced by ~65% (heterozygote) and ~90% (homozygote) vs. wild‑type.
- 26S chymotrypsin‑like activity reduced ~20% in homozygote vs. heterozygote.
- "19S precursor complexes accumulate in both heterozygous and homozygous subjects but not in wild-type controls."
- Ubiquitin‑protein conjugates "accumulated much stronger in the homozygous sample than in the heterozygous one."
- Proposed mechanism (authors' speculation, flagged as such in the paper): "any impaired de-ubiquitination of proteasome subunits (including Rpn10, Rpn13, or Rpt5) might impact proteasome assembly and/or function," as "formation of 26S complexes is a process regulated by ubiquitin modification."

**Note the gene‑dosage gradient:** heterozygous carriers show *intermediate* biochemical abnormality (19S precursor accumulation, 65% Rpn5 reduction) while remaining clinically unaffected. This is a clean example of a biochemical phenotype that is subclinical in carriers — useful for a `biochemical` marker node with a carrier‑vs‑affected interpretation band.

### 6.2 Translation regulation downstream of mTORC1 (isoform‑opposed)

PMID:27864334 (in vitro, NSCLC cells) established the second major cellular function, verbatim:
> Here, evidence is presented that the deubiquitinase OTUD6B regulates protein synthesis in non-small cell lung cancer (NSCLC) cells, operating downstream from mTORC1. OTUD6B associates with the protein synthesis initiation complex and modifies components of the 48S preinitiation complex. The two main OTUD6B splicing isoforms seem to regulate protein synthesis in opposing fashions: the long OTUD6B-1 isoform is inhibitory, while the short OTUD6B-2 isoform stimulates protein synthesis. […] OTUD6B-2 influences the expression of cyclin D1 by promoting its translation while regulating (directly or indirectly) c-Myc protein stability.

**Relevance to the NDD:** mTORC1‑coupled translational control is a canonical neurodevelopmental/epilepsy axis (cf. tuberous sclerosis, PMSE, focal cortical dysplasia). This provides a mechanistically coherent — but **not experimentally demonstrated in neurons** — bridge from OTUD6B loss to cortical malformation and seizure. Curate as a `mechanistic_hypotheses` entry with `status: EMERGING`, and attach the causal edge to that hypothesis group. Do **not** assert it as established human disease mechanism.

### 6.3 Cell‑cycle control (G1/S)

Two independent lines:
- **PMID:21267069** (mouse Ba/F3 cells + primary B lymphocytes): *"Enforced expression of OTUD-6B in Ba/F3 cells could block cell proliferation by arresting cells in G1 phase. In addition, cyclin D2 level was down-regulated when OTUD-6B WT was overexpressed."* Also documents post‑transcriptional control — *Otud-6b* mRNA is destabilized by tristetraprolin (TTP) via AU‑rich elements.
- **PMID:36059274** (multiple myeloma, EMBO J 2022): *"we screened for DUB vulnerabilities in multiple myeloma […] and identified OTUD6B as an oncogene that drives the G1/S-transition. LIN28B, a suppressor of microRNA biogenesis, is specified as a bona fide cell cycle-specific substrate of OTUD6B. Stabilization of LIN28B drives MYC expression at G1/S, which in turn allows for rapid S-phase entry."*

**Note the direction conflict:** OTUD6B overexpression is *anti*‑proliferative in B lymphocytes (2011) but *pro*‑proliferative via LIN28B‑MYC in myeloma (2022) and isoform‑dependent in NSCLC (2017). OTUD6B's proliferative effect is therefore **context‑ and isoform‑dependent**, and it is not safe to infer a single direction of effect on neural progenitor proliferation. This is a legitimate `KNOWLEDGE_GAP` for the NDD pathograph: *does OTUD6B loss reduce or expand the neural progenitor pool, and is microcephaly proliferative or apoptotic in origin?*

### 6.4 Stress granule dynamics via VCP/p97 — the most neurologically suggestive recent mechanism

PMID:41651815 (Cell Death Dis 2026), verbatim:
> By combining interactomic and proximity proteomic approaches, we reveal that the deubiquitinating enzyme OTUD6B is associated with SG-related functions. Immunofluorescence assays showed that OTUD6B localized to SGs, as well as regulated their early assembly and clearance, partially dependent on its enzymatic activity. Further proximity proteomics and interactomics results uncover the ATPase VCP/p97, a key SG disassembly factor, as an OTUD6B-associated protein. OTUD6B and VCP association is governed through their disordered regions normally participated in biomolecular condensation. VCP knockdown or pharmacological inhibition phenocopied OTUD6B silencing by leading to defects in SG dynamics. […] Therefore, our findings establish OTUD6B as a critical modulator of SG dynamics, linking its function to stress responses and potential disease mechanisms.

The same abstract notes: *"Impaired SG disassembly is closely implicated in neurodegenerative diseases and aging."* Since *VCP* itself is a Mendelian neurodegeneration gene (MSP1/IBMPFD, ALS/FTD), an OTUD6B–VCP condensate axis is a plausible neural mechanism. **Caveat: this work is in non‑neuronal cell lines and makes no claim about IDDFSDA.** Curate as `EMERGING` hypothesis + `IN_VITRO` evidence source.

### 6.5 Enzyme‑independent scaffolding: the pVHL/HIF‑1α axis

PMID:32328410 (Adv Sci 2020) and PMID:32323143 (Protein Cell 2020) independently show OTUD6B stabilizes pVHL **without using its catalytic activity**, verbatim from PMID:32328410:
> OTUD6B directly interacts with pVHL, decreases its ubiquitylation and proteasomal degradation to reduce HIF-1α accumulation in HCC cells under hypoxia. Surprisingly, OTUD6B limits the ubiquitylation of pVHL independent of its deubiquitylase activity. OTUD6B couples pVHL and elongin B/C to form more CBCVHL ligase complex, which protects pVHL from proteasomal degradation. […] Furthermore, _OTUD6B_ gene is a direct transcriptional target of HIF-1α and upregulated upon hypoxia.

**Curation implication:** this is why catalytically‑dead missense variants may not fully phenocopy null alleles — OTUD6B has at least one **non‑catalytic scaffolding function**. This directly bears on interpreting the mild p.Tyr216Cys phenotype. It also predicts that OTUD6B loss should raise HIF‑1α — a testable but untested hypothesis in patient tissue.

### 6.6 Additional characterized functions (not established in the NDD)

| Function | Substrate/partner | Evidence | Species | PMID |
|---|---|---|---|---|
| Type I IFN antiviral response — **positive** regulator | IRF3 (removes K33‑linked polyUb at Lys315) | in vitro + mouse | human | 37650650 |
| Antiviral response — **negative** regulator | irf3/irf7 (suppresses traf6‑mediated K63 polyUb) | zebrafish KO, in vivo | zebrafish | 34183367 |
| Centrosome clustering / mitotic fidelity | KIFC1/HSET (prevents premature mitotic degradation) | siRNA + CRISPR, TNBC | human | 39789388 |
| DUB–DUB heterotypic interaction | **OTUB1** (first direct demonstration) | GFP‑Trap + AlphaScreen | human | 33421002 |
| Pulmonary arterial hypertension | Calpain‑1/HIF‑1α | rodent | rat/mouse | 38878112 |
| Diabetic atherosclerosis / angiogenesis | (loss → increased angiogenesis) | in vivo | mouse | 36200061 |

⚠️ **The human vs. zebrafish IRF3 direction is explicitly contradictory** — PMID:37650650 says so directly: *"unlike the previous report that zebrafish OTUD6B negatively regulates the antiviral response by suppressing K63-linked ubiquitination of IRF3 and IRF7, we demonstrate that human OTUD6B actually enhances type I IFN response."* This is a textbook `HUMAN_MODEL_MISMATCH` discussion candidate.

### 6.7 Suggested ontology terms for the pathograph

**GO biological process / molecular function — all verified against OLS:**

| CURIE | Label | Node |
|---|---|---|
| `GO:0004843` | cysteine-type deubiquitinase activity | Loss of OTUD6B DUB activity (MF; `modifier: DECREASED`) |
| `GO:0016579` | protein deubiquitination | Loss of OTUD6B DUB activity |
| `GO:0043248` | proteasome assembly | Impaired 19S→26S proteasome assembly (`DECREASED`) |
| `GO:0043161` | proteasome-mediated ubiquitin-dependent protein catabolic process | Reduced proteasomal degradation (`DECREASED`) |
| `GO:0034063` | stress granule assembly | Stress granule dynamics (EMERGING hypothesis) |
| `GO:0002183` | cytoplasmic translational initiation | mTORC1-coupled translation dysregulation (EMERGING) |
| `GO:0007507` | heart development | Septation defect node (supported by mouse VSD + human ASD/VSD/ToF) |

⚠️ **Verify with OAK before use** (`uv run runoak -i sqlite:obo:go info <ID> -O obo`): `GO:0031929` TOR signaling; `GO:0007420` brain development; `GO:0021987` cerebral cortex development; `GO:0006915` apoptotic process.

**Cell types (CL) — ⚠️ all require OAK verification:** `CL:2000001` peripheral blood mononuclear cell (the only cell type with direct patient‑derived experimental data) · `CL:0000540` neuron · `CL:0000127` astrocyte (HPA: "Subsets of astrocytes show general, distinct and intense staining throughout the brain") · `CL:0000121` Purkinje cell (HPA: somato‑dendritic staining) · `CL:0000746` cardiac muscle cell · `CL:0000542` lymphocyte (cytoplasmic inclusions).

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary (directly and consistently affected):**
- **Central nervous system** — the dominant organ system. Cortex (ID, seizures, autistic behavior), corpus callosum (hypoplasia 3/12), ventricular system (ventriculomegaly), white matter, with reported cortical atrophy. `UBERON:0000955` brain; `UBERON:0002336` corpus callosum (**verified**); `UBERON:0000956` cerebral cortex (⚠️ verify); lateral ventricle (⚠️ verify ID).
- **Musculoskeletal system** — hands and feet (broad distal phalanges, tapered fingers, clubfoot, overlapping toes, polydactyly), vertebral column (scoliosis, vertebral anomaly), joints (flexion contractures).
- **Craniofacial complex** — the recognizable gestalt; brachycephaly, flat occiput, retrognathia, high palate, ears (macrotia, low‑set, protruding).
- **Heart** — septal defects (ASD 3/6, VSD 2/6) and conotruncal malformation (Tetralogy of Fallot). Interventricular/interatrial septum are the specific sites; the mouse model independently confirms septation as the vulnerable structure.

**Secondary / less consistent:**
- Gastrointestinal tract (feeding difficulties, chronic constipation)
- Genitourinary (cryptorchidism; renal cortical cysts in one blended‑phenotype case)
- Thyroid gland (hypothyroidism, ≥3 patients)
- Immune system (hypogammaglobulinemia, ≥3 patients)
- Eye — optic disc, retina (single case, 2025)
- Ear/auditory (hearing impairment)
- Teeth/oral (macrodontia, dental crowding, delayed eruption, thick alveolar ridges)
- Skin/adnexa (soft doughy skin, hypohidrosis; long eyelashes)

**Body systems involved:** nervous, cardiovascular, musculoskeletal, digestive, endocrine, immune, genitourinary, integumentary, special senses. This breadth is expected for a defect in a ubiquitously expressed proteostasis enzyme and is why the disorder was framed from the outset as "multisystemic."

### 7.2 Tissue and cell level

Human Protein Atlas (ENSG00000155100): OTUD6B has **low tissue specificity** — "Detected in all," tau specificity score **0.24**, clustered as "Non-specific — Basic cellular processes." Protein‑level tissue enhancement is noted in **cerebral cortex and lymphoid tissue**. Within brain, HPA reports immunoreactivity in astrocytes ("Subsets of astrocytes show general, distinct and intense staining throughout the brain"), **cerebellar Purkinje cells** (somato‑dendritic staining), and **choroid plexus** cells, across hippocampal formation, cerebral cortex, and cerebellum.

The mouse *Otud6b*^tm1b^ lacZ reporter independently confirmed near‑ubiquitous expression: per PMC5384096 full text (⚠️ verify), lacZ expression was "nearly ubiquitous" across cardiovascular, nervous, digestive, and musculoskeletal systems.

**Implication for curation:** there is **no evidence for a tissue‑restricted or cell‑type‑restricted primary lesion**. The tissue distribution of disease reflects *differential vulnerability to proteostasis failure* (post‑mitotic neurons, rapidly proliferating embryonic cardiac/limb mesenchyme) rather than restricted gene expression. Model this explicitly rather than implying neural‑specific expression.

### 7.3 Subcellular level

- **Cytosol** (`GO:0005829`, ⚠️ verify) — HPA reports cytoplasmic localization; primary site of proteasome assembly and translation initiation.
- **Proteasome complex** (`GO:0000502`, ⚠️ verify) / **proteasome regulatory particle** — the site of the demonstrated 19S assembly defect.
- **Cytoplasmic stress granule** (`GO:0010494`, ⚠️ verify) — demonstrated OTUD6B localization (PMID:41651815).
- **Centrosome** and **mitotic spindle** (⚠️ verify IDs) — "OTUD6B can localise to centrosomes and the mitotic spindle" (PMID:39789388).
- **Cytoplasmic inclusions** in patient lymphocytes — a pathological subcellular finding, not a normal compartment.

### 7.4 Localization and lateralization

Findings are **bilateral and symmetric** throughout: microcephaly, corpus callosum hypoplasia (a midline structure), bilateral ventriculomegaly ("mild irregular enlargement of the **bilateral** lateral ventricles," PMID:41188742), symmetric distal limb anomalies of both hands and feet, and midline septal cardiac defects. No lateralized or asymmetric presentation is reported. **Note:** the bilateral hand+foot involvement pattern makes this a candidate — though not a demonstrated one — for comparison against the `limb_digit_patterning_serial_homology` module; but OTUD6B is a proteostasis gene, not a limb‑patterning morphogen, so conformance would be phenotypic rather than mechanistic and is **not recommended** without evidence.

---

## 8. Temporal Development

### 8.1 Onset

- **Antenatal:** IUGR (7/12, HPO onset `HP:0030674`); congenital heart defects detectable prenatally (one family terminated a pregnancy for antenatally diagnosed ToF, PMID:35707595); congenital brain malformations.
- **Neonatal/infantile:** hypotonia, feeding difficulties, microcephaly (HPO onset `HP:0003593` Infantile onset), nystagmus (detected at 6 months in the Chinese case).
- **Infancy (1–23 months, per GARD):** seizures, developmental delay becomes apparent.
- **Onset pattern:** **congenital / insidious**, not acute. There is no asymptomatic interval and no acute presenting crisis.
- Orphanet records age of onset as **infancy**.

### 8.2 Progression

**No formal staging system, no natural‑history study, no longitudinal cohort exists.** What can be stated:

- **Course:** chronic, lifelong. The encephalopathy is best characterized as **static/developmental** rather than neurodegenerative — imaging findings are malformative (corpus callosum hypoplasia, ventriculomegaly) rather than showing documented progressive loss. (Orphanet's mention of "cortical atrophy" is the one datum pointing the other way; whether it represents progressive atrophy or congenital hypoplasia is **unresolved**.)
- **Seizures:** recurrent/episodic on a chronic background. Refractoriness is implied by PMID:32924626's framing of seizure control as "the current challenge" but has not been systematically reported.
- **Secondary progression:** scoliosis, joint contractures, and spastic tetraplegia are expected to progress with growth in the severe group — this is an inference from the phenotype set, **not a cited longitudinal finding**.
- **Duration:** lifelong; no self‑limited component.
- **Remission:** none. No spontaneous or treatment‑induced remission of the core phenotype has been reported or would be expected.

### 8.3 Critical periods

- **Embryonic organogenesis (weeks 4–8):** the window during which cardiac septation and limb patterning are established. Both the human cardiac phenotype and the mouse VSD phenotype localize the vulnerability here. **No intervention is possible in this window.**
- **Fetal/perinatal:** the mouse model narrows lethality precisely — homozygotes "survived to E18.5 at expected frequencies," with death occurring between E18.5 and shortly after birth (PMC5384096, ⚠️ verify). This identifies the **perinatal transition** as the critical survival bottleneck in mice, though human patients survive it.
- **Infancy–early childhood:** the only actionable window — for seizure control, feeding support, early intervention/therapy, and detection of the treatable comorbidities (hypothyroidism, hypogammaglobulinemia).

**⚠️ Flag:** everything in §8.2–8.3 beyond the mouse data is inference. This section is the weakest‑evidenced part of the entity and should carry an explicit `KNOWLEDGE_GAP` discussion for natural history.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

| Measure | Value | Source |
|---|---|---|
| **Prevalence** | **<1 / 1,000,000** | Orphanet ORPHA:505237 |
| dismech `prevalence_class` | `BELOW_1_IN_1000000` | derived from Orphanet band |
| dismech `measure_type` | `POINT_PREVALENCE` | Orphanet convention |
| `rate_per_100000` | **<0.1** | 1/1,000,000 → 0.1 per 100,000 |
| **Cases in literature** | **≈28–30 worldwide** (2025) | PMID:41188742 (verbatim: *"There have been < 30 reported cases globally…"*); the 2025 paper's Table 1 tabulates **27 previously reported cases + 1 index = 28** |
| **Incidence** | Not established | — |

An alternative dismech `Prevalence` record with `measure_type: CASES_IN_LITERATURE` and `rate_per_100000` omitted would faithfully capture the ~28‑case count; use the Orphanet band for the population rate.

### 9.2 Genetic epidemiology

- **Inheritance pattern:** **Autosomal recessive** (`HP:0000007`). Confirmed by ClinGen Definitive curation (AR), OMIM, Orphanet, and segregation in every reported family (both parents heterozygous carriers). GARD states the standard recurrence figures: *"there is a 25% chance their child will have the disease and a 50% chance the child will be a carrier."*
- **Penetrance:** appears **complete** for biallelic pathogenic genotypes. No unaffected biallelic individual has been reported. However, with n≈30 and complete ascertainment bias toward affected probands, non‑penetrance for hypomorphic genotypes **cannot be excluded** — a mildly affected biallelic adult would very likely never be sequenced.
- **Expressivity:** **highly variable**, both between and within families (PMID:34354232: *"our patients showed inter- and intrafamilial differences with regard to the clinical and brain imaging findings"*). Genotype accounts for much but not all of the variance (§3.3).
- **Genetic anticipation:** **not applicable** — no repeat expansion mechanism.
- **Germline mosaicism:** not reported; recurrence risk counselling should follow standard AR (25%) figures.
- **Founder effects:** none formally established. **c.433C>T (p.Arg145\*)** recurs in three of the six original families and in the Mexican proband — worth a haplotype study, but published as independent occurrences (a CpG→TpG transition at an arginine codon is a recurrent‑mutation hotspot signature, which is at least as parsimonious as a founder haplotype). **Do not assert a founder effect.**
- **Consanguinity:** **the dominant epidemiological driver**. Homozygous genotypes predominate; families are reported from Turkey, Egypt (two unrelated consanguineous families), the Gulf/Saudi region, Mexico, Spain, Italy, and China. PMID:34354232 draws the methodological conclusion directly: *"demonstrating the need for in-depth analysis of WES data in consanguineous families to uncover simultaneous autosomal recessive disorders."*
- **Carrier frequency:** **not established**. gnomAD LOEUF 1.48 / pLI 0 indicates pLoF alleles are present in the population at low frequency, but no carrier‑frequency estimate has been published. Reported disease alleles are absent or <10⁻⁵ in gnomAD.

### 9.3 Population demographics

- **Affected populations:** no ethnic group has a demonstrated elevated prevalence. The apparent concentration in Middle Eastern, North African, Mediterranean, and Latin American reports reflects **consanguinity rates and access to exome sequencing**, not a population‑specific allele.
- **Geographic distribution:** worldwide; reported from Europe (Italy, Spain), Middle East/North Africa (Turkey, Egypt, Saudi Arabia), the Americas (Mexico, USA), and East Asia (China — first case only in 2025).
- **Variant geography:** no variant is geographically restricted in a way that establishes a founder allele.
- **Sex ratio:** expected **1:1** (autosomal). Reported cases include both sexes with no documented skew; n is too small for a meaningful ratio.
- **Age distribution:** the reported population is overwhelmingly **pediatric** (infants through school age). There are essentially **no published adult patients**, which is itself an information gap — it is unknown whether this reflects reduced survival, diagnostic ascertainment bias toward children in the exome era, or both.

---

## 10. Diagnostics

### 10.1 Clinical tests

**There is no biochemical screening test, no biomarker, and no functional assay in clinical use for this disorder.** Diagnosis is molecular. Supporting/complication‑detection investigations:

| Modality | Finding | Purpose |
|---|---|---|
| **Brain MRI** | Corpus callosum hypoplasia, ventriculomegaly, white‑matter abnormalities, cortical atrophy; "mild irregular enlargement of the bilateral lateral ventricles" (PMID:41188742) | Characterize structural CNS involvement; supports the diagnosis but is non‑specific |
| **EEG** | Required for seizure characterization | No OTUD6B‑specific EEG signature has been described |
| **Echocardiography** | ASD, VSD, Tetralogy of Fallot | **Mandatory at diagnosis** — CHD in ~33–50% |
| **Thyroid function tests (TSH, fT4)** | Hypothyroidism in ≥3 patients | PMID:32924626 explicitly recommends screening: *"underscoring the value of screening for these conditions in other patients"* |
| **Serum immunoglobulins (IgG, IgA, IgM)** | Hypogammaglobulinemia in ≥3 patients | Same recommendation |
| **Ophthalmological exam incl. fundoscopy** | Optic disc hypoplasia, retinal abnormalities, nystagmus (1 case) | Newly recommended by PMID:41188742 |
| **Audiological assessment** | Hearing impairment (HPO‑annotated) | Standard for syndromic ID |
| **Spine radiographs** | Scoliosis, vertebral anomaly | Surveillance |
| **Renal ultrasound** | Cortical cysts (1 case, confounded by *PKD1*) | Consider |
| **Growth monitoring** | IUGR, short stature, failure to thrive | Ongoing |

**Research‑only cellular assays** (not clinically available, but of high mechanistic value — and the basis of any future functional‑evidence framework for VUS interpretation):
- Native PAGE of PBMC lysates for 19S/26S proteasome assembly (Rpn5, Rpt6 incorporation)
- 26S chymotrypsin‑like peptidase activity assay
- Anti‑ubiquitin immunoblot for ubiquitin‑protein conjugate accumulation
- Light microscopy for cytoplasmic lymphocyte inclusions

**Biopsy/histopathology:** no diagnostic biopsy indicated; no characteristic histopathology described beyond the lymphocyte inclusions.

**No LOINC‑coded disease‑specific test exists.**

### 10.2 Genetic testing — the diagnostic route

**Recommended approach: trio exome or genome sequencing, with parallel or reflex chromosomal microarray.**

| Modality | Utility | Notes |
|---|---|---|
| **Trio WES** | **First‑line; highest yield.** Every published diagnosis except one was made by exome sequencing | PMID:41188742 used "TrioWES"; PMID:34680978, 35430327, 35707595, 32924626, 30364145 all WES |
| **WGS** | Useful when WES is negative but suspicion is high | Would capture deep‑intronic and structural events; no published OTUD6B case required WGS |
| **Chromosomal microarray (CMA)** | **Essential adjunct, not optional.** One reported case required CMA to find the second allele — a 0.118 Mb 8q21.3 deletion in trans with a point mutation (PMID:34680978) | A WES‑only workflow would have reported this patient as a heterozygous carrier and missed the diagnosis |
| **Gene panels** | OTUD6B is included on broad ID/epileptic‑encephalopathy/NDD panels | Panel content varies; confirm inclusion |
| **Single‑gene testing** | Justified only for targeted familial testing or where the clinical gestalt is strongly recognizable in a consanguineous family — PMID:34354232's Family II used "targeted sequencing" after clinical suspicion | Not a first‑line strategy |
| **RNA studies (RT‑PCR / competitive‑fluorescent RT‑PCR)** | **High value for splice variants.** The single best functional evidence in the literature (PMID:30364145) came from patient‑RNA quantification | Should be pursued for any canonical or near‑splice VUS |
| **Karyotyping / FISH** | No role — the reported deletion (0.118 Mb) is far below karyotype resolution | |
| **mtDNA testing** | No role | |
| **Repeat expansion testing** | No role | |

**Critical WES‑interpretation caveat, twice demonstrated:** in consanguineous families, a second homozygous recessive disorder may coexist and confound phenotyping. PMID:34354232 found homozygous *RP1L1* nonsense variants explaining retinal degeneration that had initially been attributed to OTUD6B; PMID:35707595 found a heterozygous *PKD1* variant explaining renal cysts. **Do not attribute every feature in a proband to OTUD6B without checking the rest of the exome.**

### 10.3 Omics‑based diagnostics

- **RNA‑seq / transcriptomics:** not in clinical use for this disorder; targeted RT‑PCR for splice variants is the practical alternative (§10.2).
- **Proteomics:** research only. Note that proximity proteomics (BioID‑style) was the discovery method for the OTUD6B–VCP interaction (PMID:41651815).
- **Metabolomics / lipidomics:** no signature described. **No data available.**
- **Epigenomics:** **no episignature published.** Given demonstrated Kabuki‑syndrome mimicry, an OTUD6B episignature would be a high‑value diagnostic development — currently a gap, not a resource.
- **Liquid biopsy:** not applicable.

### 10.4 Clinical criteria and differential diagnosis

**No formal consensus diagnostic criteria exist** (no society guideline, no DSM/ICD operational criteria, no GeneReviews chapter as of this review). Diagnosis = compatible phenotype + biallelic pathogenic *OTUD6B* variants.

**A clinically recognizable gestalt is claimed but contested.** PMID:38389298 puts it precisely: *"Physical differences described for affected individuals suggest that the disorder may be clinically recognizable, but previous publications have reported an initial clinical suspicion for Kabuki syndrome (KS) in some affected individuals."* The most specific reported sign is from PMID:34354232 — broad distal phalanges of thumbs and halluces with prominent interphalangeal joints and persistent fetal pads, described as "pathognomonic." (⚠️ "Pathognomonic" is the authors' assertion from a 5‑patient, 2‑family series; treat as a strong clinical pearl, not an established specificity claim.)

**Differential diagnosis — each entry below is grounded in an actual published misdiagnosis or clinical suspicion, which makes this an unusually well‑evidenced DDx:**

| Condition | Overlapping features | Discriminator |
|---|---|---|
| **Kabuki syndrome** (*KMT2D*, *KDM6A*) | Long palpebral fissures, prominent/cupped ears, persistent fetal fingertip pads, DD, growth deficiency, vertebral anomaly, seizures — *documented initial clinical diagnosis in ≥2 reports* (PMID:38389298, PMID:30364145) | Inheritance (KS is AD/XL vs. AR); *KMT2D/KDM6A* episignature; eversion of the lower lateral eyelid |
| **Rubinstein–Taybi syndrome** (*CREBBP*, *EP300*) | Broad thumbs and halluces, ID, dysmorphism — the Italian proband *"came to our attention after being screened for genes responsible for Rubinstein-Taybi syndrome"* (PMID:30364145) | AD vs. AR; RTS broad thumbs are typically angulated; PMID:30364145 explicitly recommends screening OTUD6B in RTS‑suspected, RTS‑gene‑negative patients |
| **Williams–Beuren syndrome** (7q11.23 del) | Periorbital edema, hanging cheek, long smooth philtrum, cardiac defect, DD — *"facial phenotypes resembling Williams syndrome"* (PMID:34680978) | CMA; supravalvar aortic stenosis; hypercalcemia; social phenotype |
| **ZMIZ1‑related NDD** | ID, facial dysmorphism, distal limb anomalies, seizures — PMID:34680978 notes "shared phenotypes of facial dysmorphism, distal limb anomalies, and seizure disorders" | AD vs. AR |
| **Cornelia de Lange syndrome** | IUGR, microcephaly, limb anomalies, ID, arched eyebrows, long eyelashes | Synophrys; upper‑limb reduction defects; cohesinopathy genes |
| **Other proteostasis/DUB NDDs** — OTUD7A (15q13.3), and proteasome‑associated disorders | ID + epilepsy + DUB/UPS mechanism | Gene identity; OTUD7A is AD/CNV‑driven at 15q13.3 |
| **Other AR syndromic ID with seizures** (broad category) | Overlapping core | Requires ES/GS |

### 10.5 Screening

- **Newborn screening:** **not included** in any NBS panel; no biochemical marker exists to enable it. Notably, the Chinese proband's **hypothyroidism** was detected on routine newborn metabolic screening — an incidental route to earlier attention, not a screen for the disorder itself.
- **Carrier screening:** OTUD6B is included in some expanded carrier‑screening panels (⚠️ panel‑dependent; verify with GTR before asserting). Justified in consanguineous couples and in families with an affected relative.
- **Cascade screening:** standard AR cascade — test at‑risk siblings and offer carrier testing to relatives once the familial variants are known.
- **Prenatal / preimplantation:** available once both familial variants are characterized (see §13).

---

## 11. Outcome / Prognosis

**⚠️ This section is the most evidence‑poor in the report.** There is no survival study, no mortality figure, no life‑expectancy estimate, no disability‑outcome measure, and no validated prognostic model for OTUD6B‑related disorder. What follows distinguishes the few citable facts from clinical inference.

### 11.1 Survival and mortality

- **Human survival data: none published.** No 5‑year or 10‑year survival figure, no mortality rate, no disease‑specific mortality estimate exists. The published cohort is pediatric and cross‑sectional.
- **The published population contains essentially no adults**, which is itself the only survival‑adjacent signal — and it is confounded by the recency of the gene discovery (2017) and by exome‑era ascertainment favoring children.
- **Mouse mortality is severe and well‑characterized**, but does **not** transfer to humans: homozygous *Otud6b* knockouts are subviable with near‑complete perinatal lethality (MGI: "complete perinatal lethality"; PMC5384096: only 2 of 97 births, p<1×10⁻⁵, both died at birth). Human patients with predicted‑null biallelic genotypes **survive infancy**, so the mouse null overstates human lethality. **This is a genuine `HUMAN_MODEL_MISMATCH`** — model it as such, not as a survival prediction.
- Expected principal mortality contributors, by analogy with comparable severe syndromic encephalopathies (**inference, uncited**): aspiration/respiratory infection in feeding‑tube‑dependent non‑ambulatory patients; complications of congenital heart disease; status epilepticus.

### 11.2 Morbidity and function

- **Severe group:** profound functional impairment — non‑verbal, non‑ambulatory ("inability to walk"), spastic tetraplegia, total care dependence, gastrostomy feeding. ICF‑level disability is severe across mobility, communication, and self‑care domains.
- **Mild group:** mild‑to‑moderate ID with preserved speech and ambulation; substantially better functional prognosis.
- **No QoL instrument has been applied** (no EQ‑5D, SF‑36, PROMIS, or disease‑specific PROM). See §3.3.

### 11.3 Complications

Documented: recurrent seizures; feeding failure and aspiration risk; failure to thrive/short stature; congenital heart disease and its sequelae; progressive scoliosis and contractures; hypothyroidism; hypogammaglobulinemia (with attendant infection risk); hearing impairment; visual impairment (single case); constipation.

**Recovery potential:** none for the core neurodevelopmental phenotype. Developmental gains occur but the underlying encephalopathy is not reversible with any current intervention. Treatable comorbidities (hypothyroidism, seizures, CHD, nutrition) are the domains where intervention changes outcome.

### 11.4 Prognostic factors

The only supported prognostic factor is **genotype severity class**:
- Biallelic predicted‑null (nonsense/frameshift/canonical splice, both alleles) → severe phenotype
- Hypomorphic missense or leaky splice on ≥1 allele → milder phenotype

PMID:35430327 formalized this with molecular‑dynamics modelling: p.Tyr216Cys (mild) → "localized destabilization"; p.Ile274Arg (severe) → "significant distortion in the overall fold of OTUD6B." Its own conclusion is appropriately hedged: *"However, additional functional studies are required."*

Additional plausible but unvalidated prognostic markers: presence/severity of microcephaly; age at seizure onset and seizure control; presence of CHD; degree of structural brain malformation on MRI. **None is validated.**

**Prognostic biomarkers:** none. The proteasome‑assembly assay is a candidate quantitative severity readout (given the observed WT < het < hom gradient) but has never been correlated with clinical outcome. **This is a concrete, tractable research proposal worth recording as a `proposed_experiments` item.**

---

## 12. Treatment

**There is no disease‑modifying, targeted, or curative therapy for OTUD6B‑related neurodevelopmental disorder.** Management is entirely **symptomatic, supportive, and anticipatory**. No clinical trial has ever been registered for this disorder (ClinicalTrials.gov search: no OTUD6B‑specific trials). No FDA/EMA‑approved therapy exists. No pharmacogenomic guidance (CPIC/PharmGKB: zero high‑level records for OTUD6B, per ClinGen).

The literature contains no treatment protocol; the closest statement of intent is PMID:32924626: *"The current challenge with this patient is to ensure medical management of his seizures and provide him with a better quality of life. The possibilities of additional therapeutic approaches may increase by understanding the physiopathology of the involved pathways."*

### 12.1 Management components with suggested NCIT terms

⚠️ **All NCIT IDs below require verification** (`uv run runoak -i sqlite:obo:ncit info <ID>` and `just validate-terms`). They are supplied as curation candidates, not verified bindings. Treatments in this section are **standard‑of‑care inferences for syndromic ID with epilepsy**, not OTUD6B‑specific published recommendations — this must be stated explicitly in any KB entry.

| Intervention | `treatment_term` (NCIT, ⚠️ verify) | `therapeutic_modality` | Basis |
|---|---|---|---|
| **Antiseizure medication** | `NCIT:C15986` Pharmacotherapy | `SMALL_MOLECULE` | Universal (seizures 12/12). No agent‑specific data; no evidence any ASM class is preferentially effective. `therapeutic_agent` should be left generic unless a specific drug is documented per patient. |
| **Levothyroxine replacement** | `NCIT:C15986` Pharmacotherapy | `SMALL_MOLECULE` | For the documented hypothyroidism subgroup (PMID:32924626, PMID:41188742). `therapeutic_agent`: levothyroxine (CHEBI, ⚠️ verify) |
| **Immunoglobulin replacement** | `NCIT:C15986` Pharmacotherapy | `OTHER`/`PROTEIN_REPLACEMENT` | Consider for symptomatic hypogammaglobulinemia (PMID:32924626). ⚠️ No published case reports IVIG use — this is inference. |
| **Cardiac surgical repair** (septal defect closure; ToF repair) | `NCIT:C15329` Surgical Procedure | `SURGERY` | CHD in 33–50%; ToF documented (PMID:35707595) |
| **Gastrostomy / enteral feeding** | `NCIT:C15747` Supportive Care or `NCIT:C15433` Nutritional Support | `OTHER` | Feeding tubes explicitly required in the severe group (MedGen/OMIM summary) |
| **Physical therapy** | `NCIT:C15302` Physical Therapy | `BEHAVIORAL` | Hypotonia, contractures, non‑ambulation |
| **Occupational therapy** | `NCIT:C121351` Occupational Therapy | `BEHAVIORAL` | Fine motor, ADLs |
| **Speech and language therapy / AAC** | `NCIT:C159273` Speech Therapy | `BEHAVIORAL` | Absent or delayed speech |
| **Orthopedic management of scoliosis/contractures** (bracing, corrective surgery) | `NCIT:C16186` Orthopedic Surgical Procedure | `SURGERY` | Scoliosis 5/12 |
| **Hearing aids / audiological management** | *(no reliable NCIT action term — see CLAUDE.md note)* | `DEVICE` | Hearing impairment HPO‑annotated |
| **Ophthalmological / low‑vision management** | `NCIT:C49236` Therapeutic Procedure | — | Nystagmus, optic disc hypoplasia (1 case) |
| **Genetic counseling** | `NCIT:C15240` Genetic Counseling | — | AR 25% recurrence; consanguinity counselling |
| **Early intervention / developmental services** | `NCIT:C15315` Rehabilitation | `BEHAVIORAL` | Standard for syndromic ID |

### 12.2 Advanced therapeutics — status

| Modality | Status |
|---|---|
| Gene therapy (AAV gene replacement) | **None. Not in preclinical development.** OTUD6B's small coding sequence (293 aa, ~882 bp) makes it AAV‑tractable in principle, but the disorder's largely prenatal/early‑developmental onset makes postnatal CNS gene replacement of uncertain benefit. |
| Gene editing | None |
| RNA therapeutics (ASO/siRNA) | **None.** Notably, the two splice alleles (c.324+1G>C, c.405+1G>A) are the *type* of lesion sometimes amenable to splice‑switching ASO, but no such program exists and the residual‑transcript data (<1% WT) suggest an already‑near‑null substrate. |
| Cell therapy | None |
| Targeted small molecules | **None.** OTU‑family DUB inhibitors are an active drug‑discovery area (PMID:40527635), but that pipeline aims at **inhibiting** OTU DUBs in cancer — the *opposite* of what a loss‑of‑function disorder requires. **Do not curate OTU‑targeting oncology therapeutics as candidate treatments for this disease.** |
| Proteostasis modulation | Conceptually attractive (a proteasome‑assembly chaperone or activator) but entirely hypothetical; no agent identified. |
| Immunotherapy | Not applicable |

### 12.3 Treatment outcomes, adverse events, algorithms

- **Response rates:** no data. No treatment has been formally evaluated in this disorder.
- **Adverse events:** no disorder‑specific safety signal reported. No published contraindication or pharmacogenomic interaction.
- **Treatment algorithms / clinical pathways:** none published; no NCCN/society guideline. Care should follow generic multidisciplinary syndromic‑ID pathways.
- **Combination therapy / personalized medicine:** not applicable at present. The only genotype‑informed element of care is **prognostic counselling** based on the null‑vs‑hypomorph severity split (§11.4).

### 12.4 Actionable, evidence‑based surveillance recommendation

The single most useful management statement in the literature is the screening recommendation from PMID:32924626, which should be carried into the KB entry:

> In addition to seizures and other more frequently reported manifestations of this condition, this is the third patient with associated hypothyroidism and hypogammaglobulinemia, underscoring the value of screening for these conditions in other patients.

To which PMID:41188742 adds ophthalmological evaluation. **Baseline workup at diagnosis should therefore include: echocardiogram, brain MRI, EEG, thyroid function tests, serum immunoglobulins, ophthalmological examination with fundoscopy, audiology, and spine imaging.**

---

## 13. Prevention

Because this is a fully penetrant monogenic recessive disorder with no environmental component, **prevention means reproductive genetics — not risk‑factor modification.**

### 13.1 Primary prevention

- **Not achievable by any behavioral, dietary, environmental, or public‑health intervention.** There is no modifiable risk factor.
- **Genetic counseling** is the primary preventive intervention. NCIT:C15240 (⚠️ verify). For carrier couples: 25% recurrence per pregnancy, 50% carrier, 25% unaffected non‑carrier (GARD).
- **Preconception carrier screening**, particularly in consanguineous couples and in communities with high consanguinity rates, is the highest‑yield population‑level measure.
- **Preimplantation genetic testing for monogenic disease (PGT‑M)** and **prenatal diagnosis (CVS/amniocentesis)** are available once both familial variants are molecularly characterized. These are the only interventions that prevent occurrence.

### 13.2 Secondary prevention (early detection)

- **Cascade testing** of siblings and at‑risk relatives after a proband diagnosis.
- **Early molecular diagnosis** of a symptomatic infant — the practical benefit is not disease modification but (a) ending the diagnostic odyssey, (b) triggering the surveillance protocol in §12.4, and (c) enabling accurate recurrence counselling before the next pregnancy.
- Note the incidental‑detection route: the Chinese proband's hypothyroidism was picked up on **routine newborn metabolic screening**, which brought her to medical attention at 6 months.
- **No population screening program exists or is proposed**, and none is justified at a prevalence of <1/1,000,000 with no presymptomatic treatment.

### 13.3 Tertiary prevention (preventing complications in diagnosed patients)

This is where prevention is genuinely actionable:
- Systematic screening for **hypothyroidism** and **hypogammaglobulinemia** (explicitly recommended, PMID:32924626) — both are treatable and both, if missed, add avoidable morbidity.
- **Echocardiography** at diagnosis to detect surgically correctable CHD.
- **Ophthalmological** and **audiological** assessment to prevent avoidable sensory‑deprivation contributions to developmental delay.
- **Aspiration prevention** via feeding assessment and, where indicated, gastrostomy.
- **Scoliosis and contracture surveillance** with early orthopedic and physiotherapy intervention.
- **Seizure control** optimization.

### 13.4 Not applicable

- **Immunization:** no disease‑specific vaccine strategy. (Standard childhood immunization applies; if hypogammaglobulinemia is present, live‑vaccine caution and immunological input follow standard immunodeficiency practice — ⚠️ inference, not published for this disorder.)
- **Public‑health / environmental interventions:** not applicable.
- **Chemoprophylaxis:** none, unless antimicrobial prophylaxis is indicated for a documented antibody deficiency (⚠️ inference).

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy and orthologs

| Species | NCBI Taxon | Gene | Identifier | Notes |
|---|---|---|---|---|
| *Homo sapiens* | `NCBITaxon:9606` | *OTUD6B* | Entrez 51633; HGNC:24281 | 8q21.3; 293 aa |
| *Mus musculus* | `NCBITaxon:10090` | *Otud6b* | **MGI:1919451** | Chr4: 14,809,503–14,826,413 (minus strand); ortholog of human chr8:91,070,196–91,087,095 |
| *Danio rerio* | `NCBITaxon:7955` | *otud6b* | ZFIN (⚠️ verify ID) | Functional antiviral studies (PMID:34183367) |
| *Rattus norvegicus* | `NCBITaxon:10116` | *Otud6b* | RGD (⚠️ verify ID) | Used in PAH studies (PMID:38878112) |

⚠️ **Caution:** MGI:1922805 is **not** Otud6b (it is *Nsmce3l*). Use **MGI:1919451**.

### 14.2 Natural disease in other species

**None reported.** There is no naturally occurring OTUD6B‑related disease in any companion animal, livestock species, or wildlife population. A search of the veterinary literature and OMIA yields no OTUD6B entry (⚠️ OMIA was not directly queried in this review — verify at omia.org before asserting absence definitively).

**Veterinary relevance:** none. All animal OTUD6B disease models are **experimentally induced**, not natural.

### 14.3 Comparative biology

- **Evolutionary conservation:** OTUD6B is conserved across vertebrates, with functional orthologs demonstrated in mouse, rat, and zebrafish. The OTU catalytic domain and its cysteine‑protease triad are the deeply conserved elements.
- **Comparative pathology — a key mismatch.** The mouse null is **substantially more severe than the human null**: homozygous *Otud6b*^tm1b/tm1b^ mice are subviable with essentially complete perinatal lethality, whereas human patients with biallelic predicted‑null alleles survive into childhood. Conversely, the **cardiac phenotype is strikingly concordant** — mouse VSD at high penetrance vs. human ASD/VSD/ToF — making the heart the best cross‑species‑validated organ.
- **Direction‑of‑effect divergence in innate immunity:** the human vs. zebrafish IRF3 results are explicitly opposite (§6.6). This is a documented species divergence, not merely an unreplicated result, and should be curated as `HUMAN_MODEL_MISMATCH` rather than as conflicting evidence for a single claim.
- **Transmission / zoonosis / cross‑species susceptibility:** not applicable — this is a germline monogenic disorder.

---

## 15. Model Organisms

### 15.1 Mouse — the principal disease model

**Allele:** `Otud6b^tm1b(EUCOMM)Wtsi` (**MGI:5637064**) — a knockout‑first tm1a converted to tm1b by Cre‑mediated excision of the promoter‑driven neo cassette and critical exon(s), leaving a **lacZ reporter** in place. This design is what enabled the expression mapping.

**Repositories:** MGI records 10 mutations/alleles for *Otud6b* (2 endonuclease‑mediated, 4 gene‑trapped, 4 targeted) and **29 strains/lines available through IMSR**. A line is archived at MRC Harwell (`B6Dnk;B6N-Otud6b^tm1b(EUCOMM)Wtsi/WtsiCnbc`, stock 7042). IMPC phenotyping data at `mousephenotype.org/data/genes/MGI:1919451`.

**Phenotype (MGI summary):** "complete perinatal lethality, decreased fetal size, and ventricular septal defects," with annotations spanning cardiovascular, growth/size, hematopoietic, immune, and mortality/aging systems, from 13 phenotype references.

**Detailed findings (PMC5384096 full text — ⚠️ paraphrase‑risk, verify before use as snippets):**
- **Subviability:** only 2 homozygotes identified from 97 births (p<1×10⁻⁵ deviation from Mendelian expectation); both died at birth.
- **Timing of lethality:** homozygotes survived to **E18.5 at expected frequencies** → death occurs between E18.5 and shortly after birth. This is a precise and useful window.
- **Growth:** E18.5 knockout embryos showed **34% reduced total volume** vs. wild‑type littermates — a direct correlate of the human IUGR/growth restriction phenotype.
- **Cardiac:** **ventricular septal defects in 80% of hearts** (3/3 at E14.5; 1/2 at E18.5) vs. a **0.67%** background rate in C57BL/6N controls.
- **Expression:** lacZ reporter expression "nearly ubiquitous," across cardiovascular, nervous, digestive, and musculoskeletal systems.

**IMPC phenotyping (mousephenotype.org, MGI:1919451):** 2 significant phenotypes; 3 of 21 tested physiological systems significantly impacted — **mortality/aging, immune system, hematopoietic system** (18 systems no significant impact, 3 not tested). Note that the immune and hematopoietic hits are independently interesting given the human hypogammaglobulinemia reports and the B‑lymphocyte cell‑cycle work (PMID:21267069).

### 15.2 Phenotype recapitulation and limitations

| Human feature | Mouse recapitulation | Assessment |
|---|---|---|
| Congenital heart disease (ASD/VSD/ToF) | **VSD in 80% of hearts** vs. 0.67% background | **Excellent** — strongest cross‑species validation |
| Growth restriction / IUGR | 34% reduced embryo volume at E18.5 | **Good** |
| Immune involvement (hypogammaglobulinemia) | IMPC significant immune + hematopoietic impact | **Suggestive** |
| **Intellectual disability** | **Not assessable** — homozygotes die perinatally | **Not recapitulated** |
| **Seizures** | **Not assessable** — perinatal lethality | **Not recapitulated** |
| **Microcephaly / brain malformation** | Not reported | **Not recapitulated / not examined** |
| Survival | **Perinatal lethal** in mouse; **survival to childhood** in humans | **Direct mismatch** |

**Limitations — this is the crux of the model problem and should be curated as an explicit `HUMAN_MODEL_MISMATCH` discussion:**

The constitutive mouse null is **too severe to model the defining features of the human disease**. Because homozygotes die at birth, the model cannot address intellectual disability, seizures, speech, ambulation, microcephaly, or any postnatal neurodevelopmental outcome — i.e., the entire clinical core of IDDFSDA. What the mouse does establish is the *embryonic* arm: cardiac septation and fetal growth. The human null phenotype is milder than the mouse null, meaning there is either species‑specific redundancy (possibly OTUD6A or other OTU‑family paralogs) or a difference in developmental dependence on the enzyme.

**Proposed experiments to resolve the mismatch (`proposed_experiments` candidates):**
1. **Conditional/neural‑specific *Otud6b* knockout** (e.g., Nestin‑Cre, Emx1‑Cre) to bypass perinatal lethality and interrogate cortical development, seizure susceptibility, and behavior.
2. **Hypomorphic knock‑in of the human missense alleles** (p.Tyr216Cys as the "mild" allele; p.Ile272Arg/p.Ile274Arg as the "severe" allele) to test the genotype–severity model computationally proposed by PMID:35430327 in an in‑vivo system.
3. **Patient iPSC‑derived cortical neurons and cerebral organoids** — currently the most important missing model. No iPSC or organoid model of OTUD6B deficiency has been published. This would permit direct testing of the proteasome‑assembly defect in human neurons and of the mTORC1‑translation and stress‑granule hypotheses in the disease‑relevant cell type.
4. **Correlate the PBMC proteasome‑assembly assay with clinical severity** across a genotype‑stratified patient cohort, to test whether it functions as a quantitative severity biomarker.

### 15.3 Other model systems

| System | Use | Relevance to IDDFSDA | PMID |
|---|---|---|---|
| **Zebrafish** *otud6b* mutant/KO | Antiviral innate immunity (irf3/irf7 K63‑Ub) | **Low** — immune, not neurodevelopmental; and direction of effect conflicts with human | 34183367 |
| **Rat** (PAH model) | Calpain‑1/HIF‑1α in pulmonary hypertension | **Low** | 38878112 |
| **Mouse Ba/F3 cells + primary B lymphocytes** | Cell‑cycle G1 arrest; TTP‑mediated mRNA destabilization | Moderate — cell‑cycle mechanism | 21267069 |
| **Human cancer cell lines** (NSCLC, HCC, TNBC, MM, CRC, ESCC, cholangiocarcinoma) | Translation, pVHL/HIF, KIFC1/centrosome, LIN28B/MYC, stress granules | **Mechanistically informative but disease‑context‑mismatched.** All are `IN_VITRO` and none models neurodevelopment. Curate with `evidence_source: IN_VITRO` and explicitly note the context mismatch. | 27864334, 32328410, 39789388, 36059274, 41651815 |
| **Patient PBMCs** | 19S/26S proteasome assembly, chymotrypsin‑like activity, Ub‑conjugate accumulation | **Highest relevance** — the only patient‑derived functional system, and the source of the disease's core mechanism | 28343629 |
| **iPSC / organoid** | — | **None published. Major gap.** | — |
| **Drosophila / C. elegans / yeast** | — | No published OTUD6B‑ortholog disease model | — |

**Model databases:** MGI (`informatics.jax.org/marker/MGI:1919451`), IMPC (`mousephenotype.org/data/genes/MGI:1919451`), IMSR (29 strains), EUCOMM/EMMA, MRC Harwell (stock 7042), ZFIN, RGD, Alliance of Genome Resources.

---

## Consolidated Evidence Register

References with **verbatim abstracts captured** in this report (suitable for `snippet:` after `just fetch-reference` + `just validate-references`):

| PMID | Year | Type | Role | `evidence_source` |
|---|---|---|---|---|
| **28343629** | 2017 | AJHG, original series (n=12/6 families) | **Landmark** — disease definition, variants, mouse, proteasome mechanism | HUMAN_CLINICAL (+ MODEL_ORGANISM, IN_VITRO for sub-claims — split the item) |
| **30364145** | 2018 | Front Genet, case | First independent replication; RT‑PCR splice functional data; Rubinstein‑Taybi DDx | HUMAN_CLINICAL |
| **31147255** | 2020 | An Pediatr, case | First Spanish case *(Spanish‑language; no English abstract — cached record has no abstract text; do not fabricate a snippet)* | HUMAN_CLINICAL |
| **32181568** | 2020 | AJMG A, commentary | Alkuraya comment on the AJHG paper *(no abstract — cache confirms `content_type: abstract_only` with no abstract body; unusable as a snippet source)* | — |
| **32924626** | 2020 | JIMCRI, case | First Mexican case; **hypothyroidism + hypogammaglobulinemia screening recommendation** | HUMAN_CLINICAL |
| **34354232** | 2022 | J Hum Genet, 5 patients/2 families | Egyptian families; orodental features; **"pathognomonic"** fetal pads; *RP1L1* exclusion | HUMAN_CLINICAL |
| **34680978** | 2021 | Genes, case | **Point mutation + 0.118 Mb 8q21.3 microdeletion**; Williams‑like features; *ZMIZ1* co‑occurrence | HUMAN_CLINICAL |
| **35430327** | 2022 | EJMG, case + modelling | Genotype–severity structural/MD modelling (Tyr216Cys vs Ile274Arg) | HUMAN_CLINICAL + COMPUTATIONAL (split) |
| **35707595** | 2022 | Mol Syndromol, case | Tetralogy of Fallot; p.Ile272Arg; *PKD1* blended phenotype | HUMAN_CLINICAL |
| **38389298** | 2024 | AJMG A, 3 siblings | **Kabuki syndrome mimicry**; delayed dentition, hypohidrosis, mirror movements | HUMAN_CLINICAL |
| **41188742** | 2025 | BMC Pediatr, case | First Chinese case; **ocular dysplasia**; 28‑case tabulation; "<30 reported cases globally" | HUMAN_CLINICAL |
| **27864334** | 2017 | Mol Cancer Res | mTORC1‑downstream translation; isoform antagonism; cyclin D1/c‑Myc | IN_VITRO |
| **21267069** | 2011 | PLoS One | First functional characterization; Cys‑dependent DUB activity; G1 arrest; TTP regulation | IN_VITRO + MODEL_ORGANISM |
| **36059274** | 2022 | EMBO J | OTUD6B–LIN28B–MYC axis; G1/S | IN_VITRO |
| **39789388** | 2025 | EMBO Rep | KIFC1/centrosome clustering; catalytic‑activity dependence | IN_VITRO |
| **41651815** | 2026 | Cell Death Dis | **Stress granules + VCP/p97**; most neurologically suggestive recent mechanism | IN_VITRO |
| **32328410** | 2020 | Adv Sci | **Enzyme‑independent** pVHL stabilization; HIF‑1α feedback loop | IN_VITRO |
| **33421002** | 2021 | Methods Mol Biol | First direct OTUD6B–OTUB1 interaction | IN_VITRO |
| **34183367** | 2021 | J Immunol | Zebrafish otud6b, **negative** antiviral regulator | MODEL_ORGANISM |
| **37650650** | 2023 | mBio | Human OTUD6B, **positive** antiviral regulator via IRF3 K33‑Ub — explicit contradiction with zebrafish | IN_VITRO + MODEL_ORGANISM |
| **35662507** | 2022 | Biol Psychiatry, review | "The DUB Club" — DUBs and NDDs framing | OTHER |
| **40527635** | 2026 | Trends Mol Med, review | OTU DUBs in disease and their targeting | OTHER |

**Structured‑database citations available:** `ORPHA:505237` (Orphanet — definition, prevalence <1/1,000,000, ICD‑10 Q87.8, AR inheritance, infancy onset) and a `CGGV:` ClinGen gene‑disease validity record (OTUD6B / syndromic intellectual disability / AR / **Definitive** / ID and Autism GCEP / 2024‑08‑22). Both should be pulled through the repo's structured‑source pipeline (`just structured-rebuild-orphanet --id 505237`, `just clingen-refresh` + `just clingen-list`) rather than hand‑transcribed.

---

## Prioritized Knowledge Gaps

1. **No natural history study.** Survival, life expectancy, adult outcomes, and progression rate are entirely unknown. There are effectively no published adult patients.
2. **No iPSC / cortical organoid model.** The mouse null's perinatal lethality means the human disease's *defining* features (ID, seizures, microcephaly) have never been modelled in any system. This is the single largest mechanistic gap. → `HUMAN_MODEL_MISMATCH`.
3. **The link from proteasome dysfunction to the neural phenotype is unestablished.** The 19S assembly defect is demonstrated in PBMCs; nothing connects it to cortical development, neuronal excitability, or seizure generation. The mTORC1‑translation and stress‑granule/VCP routes are plausible bridges but are `EMERGING` hypotheses from non‑neuronal cells.
4. **Direction of effect on neural progenitor proliferation is unknown** — OTUD6B is anti‑proliferative in one system and pro‑proliferative in another. Is microcephaly proliferative or apoptotic in origin?
5. **No episignature**, despite documented Kabuki‑syndrome mimicry — a tractable diagnostic development.
6. **HPOA frequencies derive from a single, severity‑biased 12‑person cohort** and conflict with later mild cases (e.g., "Severe intellectual disability 12/12").
7. **The proteasome‑assembly assay has never been correlated with clinical severity** despite showing a clean WT<het<hom gradient — an obvious candidate quantitative biomarker.
8. **Genotype–severity model is computational only** (PMID:35430327's own caveat: *"additional functional studies are required"*), and intrafamilial variability argues that genotype is not the whole story.

---

## Sources

**Literature (PubMed):**
[PMID:28343629](https://pubmed.ncbi.nlm.nih.gov/28343629/) · [PMID:30364145](https://pubmed.ncbi.nlm.nih.gov/30364145/) · [PMID:31147255](https://pubmed.ncbi.nlm.nih.gov/31147255/) · [PMID:32181568](https://pubmed.ncbi.nlm.nih.gov/32181568/) · [PMID:32924626](https://pubmed.ncbi.nlm.nih.gov/32924626/) · [PMID:34354232](https://pubmed.ncbi.nlm.nih.gov/34354232/) · [PMID:34680978](https://pubmed.ncbi.nlm.nih.gov/34680978/) · [PMID:35430327](https://pubmed.ncbi.nlm.nih.gov/35430327/) · [PMID:35707595](https://pubmed.ncbi.nlm.nih.gov/35707595/) · [PMID:38389298](https://pubmed.ncbi.nlm.nih.gov/38389298/) · [PMID:41188742](https://pubmed.ncbi.nlm.nih.gov/41188742/) · [PMID:27864334](https://pubmed.ncbi.nlm.nih.gov/27864334/) · [PMID:21267069](https://pubmed.ncbi.nlm.nih.gov/21267069/) · [PMID:36059274](https://pubmed.ncbi.nlm.nih.gov/36059274/) · [PMID:39789388](https://pubmed.ncbi.nlm.nih.gov/39789388/) · [PMID:41651815](https://pubmed.ncbi.nlm.nih.gov/41651815/) · [PMID:32328410](https://pubmed.ncbi.nlm.nih.gov/32328410/) · [PMID:33421002](https://pubmed.ncbi.nlm.nih.gov/33421002/) · [PMID:34183367](https://pubmed.ncbi.nlm.nih.gov/34183367/) · [PMID:37650650](https://pubmed.ncbi.nlm.nih.gov/37650650/) · [PMID:35662507](https://pubmed.ncbi.nlm.nih.gov/35662507/) · [PMID:40527635](https://pubmed.ncbi.nlm.nih.gov/40527635/) · [PMC5384096 (AJHG full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5384096/) · [PMC12584513 (BMC Pediatr full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12584513/)

**Databases and aggregators:**
[OMIM #617452](https://omim.org/entry/617452) · [OMIM \*612021](https://omim.org/entry/612021) · [Orphanet ORPHA:505237](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=505237&lng=en) · [MedGen C4479520](https://www.ncbi.nlm.nih.gov/medgen/1375601) · [GARD 17942](https://rarediseases.info.nih.gov/diseases/17942/intellectual-developmental-disorder-with-dysmorphic-facies-seizures-and-distal-limb-anomalies) · [HPO annotations (ontology.jax.org)](https://ontology.jax.org/api/network/annotation/OMIM:617452) · [ClinGen OTUD6B (HGNC:24281)](https://search.clinicalgenome.org/kb/genes/HGNC:24281) · [HGNC REST (OTUD6B)](https://rest.genenames.org/fetch/symbol/OTUD6B) · [UniProt Q8N6M0](https://rest.uniprot.org/uniprotkb/Q8N6M0.txt) · [Human Protein Atlas ENSG00000155100](https://www.proteinatlas.org/ENSG00000155100-OTUD6B/tissue) · [MGI:1919451 (mouse Otud6b)](https://www.informatics.jax.org/marker/MGI:1919451) · [MGI:5637064 (Otud6b tm1b allele)](https://www.informatics.jax.org/allele/MGI:5637064) · [IMPC MGI:1919451](https://www.mousephenotype.org/data/genes/MGI:1919451) · [MRC Harwell stock 7042](https://archive.har.mrc.ac.uk/stock?id=7042) · ClinVar and PubMed queried via NCBI E‑utilities · [OLS4 (EBI)](https://www.ebi.ac.uk/ols4/) for GO/UBERON/MONDO verification