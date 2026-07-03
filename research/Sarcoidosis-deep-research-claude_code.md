---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-06-24T15:22:16.762809'
end_time: '2026-06-24T15:27:05.909799'
duration_seconds: 289.15
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Sarcoidosis
  mondo_id: ''
  category: Immune
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
  - claude-opus-4-8[1m]
  web_search_requests: 11
  num_turns: 13
  total_cost_usd: 2.012923
  session_id: e367bd02-9270-45ab-bed1-ca7b9bfe04e4
  stop_reason: end_turn
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sarcoidosis
- **MONDO ID:**  (if available)
- **Category:** Immune

## Research Objectives

Please provide a comprehensive research report on **Sarcoidosis** covering all of the
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

I now have a solid, verified evidence base. Here is the comprehensive report.

---

# Comprehensive Research Report: Sarcoidosis

**Prepared for:** dismech knowledge base entry · **Category:** Immune · **Date:** 2026-06-24

> ⚠️ **Curator note on citations:** This report follows the dismech SOP for deep-research outputs — **treat every PMID/snippet below as a *lead*, not ground truth.** Run `just fetch-reference PMID:XXXX` and `just validate-references` before committing any snippet. PMIDs I am highly confident of are marked ✓; those needing confirmation are marked ⚠. There is **no single causal gene / OMIM entry** for sarcoidosis (it is a complex polygenic disease), so the NEC gene-vs-MONDO preflight is less of a trap here than for Mendelian disorders, but synonym collisions (e.g., "Boeck disease") should still be checked.

---

## 1. Disease Information

**Overview.** Sarcoidosis is a multisystem granulomatous inflammatory disease of unknown cause, characterized by the formation of **non-caseating (non-necrotizing) epithelioid-cell granulomas** in affected organs — most commonly the lungs and intrathoracic lymph nodes (>90% of patients), but potentially almost any organ. It results from an exaggerated immune response, in genetically susceptible individuals, to one or more poorly defined antigens. Disease behavior ranges from asymptomatic and spontaneously resolving (e.g., Löfgren syndrome) to chronic, progressive, fibrotic, and occasionally fatal.

> "Sarcoidosis is an inflammatory disease of unknown cause involving the formation of granulomas in almost any organ, although typically in the lungs." — Grunewald et al., *Nat Rev Dis Primers* 2019 ([article](https://www.nature.com/articles/s41572-019-0096-x))

**Key identifiers:**
| Resource | ID |
|---|---|
| **MONDO** | **MONDO:0019338** (sarcoidosis) — *verify with `runoak -i sqlite:obo:mondo info MONDO:0019338`* |
| OMIM | **181000** (SARCOIDOSIS, SS1 / susceptibility) |
| Orphanet | **ORPHA:797** (Sarcoidosis) |
| ICD-10 | **D86** (D86.0 pulmonary; D86.2 lung w/ lymph nodes; D86.3 skin; D86.8x specified sites; D86.9 unspecified) |
| ICD-11 | **4B20** (Sarcoidosis) |
| MeSH | **D012507** (Sarcoidosis) |
| DOID | DOID:11335 |
| UMLS | C0036202 |

**Synonyms / alternative names:** Besnier-Boeck-Schaumann disease; Boeck sarcoid; Boeck disease; Schaumann disease; benign lymphogranulomatosis; sarcoid; (historical) "lupus pernio" refers specifically to the chronic cutaneous facial form.

**Data derivation:** Information here is aggregated disease-level knowledge (society guidelines, registries, GWAS meta-analyses, cohort studies) rather than individual EHR records. Major cohorts referenced: **ACCESS** (A Case Control Etiologic Study of Sarcoidosis, US, n=736), **GRADS**, **WASOG** registry, Swedish national registers, and the **DZL/GenPhenReSa** European cohort.

---

## 2. Etiology

**Disease causal factors.** Sarcoidosis is a **complex (multifactorial) disease**: a combination of genetic susceptibility + environmental/microbial antigen exposure → dysregulated immune granulomatous response. No single cause is established. The leading paradigm is an antigen-driven, Th1/Th17-polarized immune reaction.

**Candidate antigenic triggers (all unproven as causal):**
- **Microbial:** *Mycobacterium tuberculosis*-derived proteins (notably **mKatG**, catalase-peroxidase) and **ESAT-6**; *Cutibacterium (Propionibacterium) acnes* — the only microorganism repeatedly isolated from sarcoid granulomas, especially in Japanese cohorts. (NCBITaxon:1747 *Cutibacterium acnes*; NCBITaxon:1773 *M. tuberculosis*.) These are thought to act as persistent poorly degradable antigens rather than active infection.
- **Environmental/occupational:** insecticides, mold/musty odors, agricultural employment, and **inorganic particulates**. The strongest occupational signal is the **WTC (World Trade Center) dust** "sarcoidosis-like granulomatous disease" among first responders.
- **Autoimmune component:** increasing evidence of autoantigen recognition (e.g., vimentin presented by HLA-DRB1*03).

**Risk factors — genetic** (see §4): **HLA class II (HLA-DRB1, HLA-DQB1)** is the dominant locus; non-HLA loci include **BTNL2, ANXA11, NOTCH4, IL23R, RAB23, OS9, IL12B, FAM177B, C-C chemokine genes**.

**Risk factors — environmental/demographic:**
- Race/ancestry: African ancestry → higher incidence and severity (see §9).
- Family history: first-degree relatives have a **~3.7–5× increased risk** (ACCESS study; sibling relative risk highest).
- Sex: roughly equal; female peak slightly later.
- Occupational/inhalational exposures (above); firefighting/WTC.

**Protective factors:**
- **Smoking** is paradoxically *inversely* associated with sarcoidosis risk (one of the few granulomatous/ILD conditions where smoking appears protective) — though it may worsen some outcomes. ⚠ verify.
- Genetic: **HLA-DRB1*01 and HLA-DRB1*04** are associated with reduced risk; **DRB1*03:01 (DR3)** is strongly associated with the *self-limiting, good-prognosis* Löfgren phenotype (acts as a prognostic protective allele, not a susceptibility-reducing one).

**Gene–environment interactions:** HLA-DRB1*03-restricted T-cell responses to specific antigens (e.g., vimentin) define the Löfgren-syndrome resolving phenotype — a paradigmatic GxE/GxImmunogenetic interaction. *C. acnes*-reactive responses are modulated by HLA background (CTD/PheGenI candidate area).

---

## 3. Phenotypes

Sarcoidosis is defined by organ-specific granulomatous involvement plus constitutional features. Approximate frequencies (ACCESS, WASOG, GenPhenReSa cohorts):

| Phenotype | HPO term (suggested) | Approx. frequency | Notes |
|---|---|---|---|
| Intrathoracic/pulmonary involvement | **HP:0002088** (Abnormal lung morphology) / HP:0006515 (Interstitial pulmonary abnormality) | **>90%** | Defining feature |
| Bilateral hilar lymphadenopathy | **HP:0012246** (hilar lymphadenopathy) / HP:0002721 (Immunodeficiency? no) — use HP:0030075 (Abnormal mediastinal morphology) | ~majority on imaging | Scadding stage I |
| Dyspnea | **HP:0002094** (Dyspnea) | ~30–50% | |
| Cough (chronic, dry) | **HP:0031246** (Chronic cough) / HP:0012735 (Cough) | common | |
| Fatigue | **HP:0012378** (Fatigue) | up to ~50–70% | major QoL driver |
| Erythema nodosum | **HP:0012219** (Erythema nodosum) | ~10–25% (higher in N. Europeans) | part of Löfgren syndrome |
| Lupus pernio / other skin lesions | **HP:0000962** (Hyperkeratosis)? better: HP:0011123 (Inflammatory abnormality of the skin) | skin ~25–30% overall | lupus pernio = chronic marker |
| Uveitis / ocular | **HP:0000554** (Uveitis) | ocular ~10–25% | anterior > posterior |
| Peripheral lymphadenopathy | **HP:0002716** (Lymphadenopathy) | ~10–15% | |
| Hepatic granulomas | **HP:0001392** (Abnormal liver morphology) / HP:0002240 (Hepatomegaly) | ~10–20% (often subclinical) | |
| Splenomegaly | **HP:0001744** (Splenomegaly) | ~5–10% | |
| Arthralgia/arthritis | **HP:0002829** (Arthralgia) / HP:0001369 (Arthritis) | acute (Löfgren) common | |
| Cardiac sarcoidosis | **HP:0001638** (Cardiomyopathy) / HP:0011675 (Arrhythmia) / HP:0001712 (Left ventricular hypertrophy)? | clinically ~5%; subclinical up to ~25% | leading cause of death (esp. Japan) |
| Neurosarcoidosis | **HP:0002383** (Encephalitis)? better HP:0000759 (Abnormal peripheral nervous system) / HP:0100256 (Cranial nerve VII palsy → HP:0010628 Facial palsy) | ~5–10% | facial nerve palsy classic |
| Hypercalcemia | **HP:0003072** (Hypercalcemia) | ~5–10% | from 1,25-(OH)₂-vit D₃ overproduction |
| Hypercalciuria / nephrolithiasis | **HP:0002150** (Hypercalciuria) / HP:0000787 (Nephrolithiasis) | hypercalciuria ~up to 40% | |
| Renal (granulomatous interstitial nephritis) | **HP:0000124** (Renal tubular dysfunction)/HP:0000790 | uncommon | |
| Small-fiber neuropathy | **HP:0000763** (Sensory neuropathy) | underrecognized, common | autonomic + sensory sx |
| Parotid/salivary (with uveitis+fever = Heerfordt syndrome) | HP:0010286 (Parotitis)? | rare | uveoparotid fever |

**Onset & severity:** Adult-onset (peak 25–45y; second female peak >50y). Severity variable; ~50–70% remit (often spontaneously), ~10–30% develop chronic/progressive disease, and ~5–10% develop pulmonary fibrosis. **Quality-of-life impact** is substantial and often disproportionate to organ burden — driven by **fatigue, dyspnea, depression, and small-fiber neuropathy**; measured by the disease-specific **King's Sarcoidosis Questionnaire (KSQ)** and **SF-36/FAS (Fatigue Assessment Scale)**.

---

## 4. Genetic / Molecular Information

Sarcoidosis is **polygenic with no monogenic causal gene**; OMIM lists multiple susceptibility loci (SS1–SS6).

**Major susceptibility loci (germline; all common variants, not "pathogenic" in ACMG Mendelian sense):**

| Gene | HGNC | Locus | Key variant / finding | Evidence |
|---|---|---|---|---|
| **HLA-DRB1** | hgnc:4948 | 6p21 (MHC II) | *DRB1\*11:01 ↑risk (both Black & White); \*03:01 → Löfgren/resolving; \*14,\*15 → chronic; \*01,\*04 protective | GWAS, replicated |
| **BTNL2** | hgnc:1142 | 6p21 | rs2076530 G→A truncating splice variant ↑risk (OR ~1.6–1.8) | ⚠ PMID for Valentonyte 2005 *Nat Genet* |
| **ANXA11** | hgnc:535 | 10q22 | rs1049550 (R230C) — annexin A11, apoptosis regulation | confirmed German/Czech/Portuguese/US ([Nature Genes Immun](https://www.nature.com/articles/gene201248)) |
| **NOTCH4** | hgnc:7884 | 6p21 | eQTL/GWAS, innate immunity | [PMID 38390497 ⚠](https://pubmed.ncbi.nlm.nih.gov/38390497/) |
| **IL23R** | hgnc:19100 | 1p31 | Th17 axis | |
| **RAB23, OS9, IL12B, FAM177B, SH2B3/ATXN2** | — | various | GWAS hits | |

**eQTL study (2024):** "Examination of eQTL Polymorphisms Associated with Increased Risk of Progressive Complicated Sarcoidosis in European and African Descent Subjects" — implicates innate immunity, MHC class II, and allograft-rejection pathways ([PMID 38390497 ⚠](https://pubmed.ncbi.nlm.nih.gov/38390497/)).

**Clinical-course associations:** ANXA11 rs1049550 C/T, BTNL2 rs2076530 G/A, and HLA class I/II alleles modulate disease course ([PMID 27662826 ✓](https://pubmed.ncbi.nlm.nih.gov/27662826/), Morais 2018 *Clin Respir J*).

**Variant classification note:** These are **susceptibility/risk alleles**, not Mendelian pathogenic variants — for the dismech entry, model them as **GENO susceptibility associations**, not causal `pathogenic` variants. Allele frequencies are common (MAF often 0.1–0.4 in gnomAD); origin is **germline**; functional consequence is largely **altered antigen presentation (HLA), altered immune signaling (BTNL2 = loss of negative T-cell costimulation; ANXA11 = apoptosis modulation)**.

**Somatic/acquired:** A key recent insight is **acquired mTORC1 pathway activation in granuloma macrophages** (see §6) — i.e., a somatic/functional signaling lesion, not inherited.

**Modifier genes:** TNF-α promoter polymorphisms (−308A) and HLA alleles modify severity/Löfgren prognosis. **Epigenetics:** altered DNA methylation and miRNA profiles reported in BAL cells and granulomas (DiseaseMeth/GEO candidate area); not yet definitively mechanistic. **No characteristic chromosomal abnormality.**

---

## 5. Environmental Information

- **Environmental/occupational factors** (CTD/ACCESS): agricultural/musty/mold environments, insecticides, metal/silica dust, **WTC dust** (granulomatous "sarcoid-like" disease in responders); firefighting; possibly photocopier toner. Beryllium exposure causes **chronic beryllium disease (berylliosis)** — a clinically/histologically near-identical mimic that must be excluded (BeLPT test).
- **Lifestyle:** **Smoking is inversely associated** with risk (protective signal). Diet/obesity links weak.
- **Infectious agents (trigger candidates, not established pathogens):** *Cutibacterium acnes* (NCBITaxon:1747), *Mycobacterium tuberculosis* antigens mKatG/ESAT-6 (NCBITaxon:1773). The "latent microbial reactivation + immune dysregulation" model is reviewed in 2025 work ([PMC12362391](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12362391/)). Sarcoidosis is **not contagious**.

---

## 6. Mechanism / Pathophysiology

**Core causal chain (upstream → downstream):**

1. **Antigen exposure** (microbial/environmental/auto-) in a genetically susceptible host →
2. **Antigen presentation by APCs (dendritic cells, macrophages) via HLA class II** to **CD4⁺ T cells** →
3. **Th1 / Th17.1 polarization** with **IFN-γ, IL-2, TNF-α, IL-12, IL-18, IL-23** production; **oligoclonal T-cell expansion** (BAL CD4:CD8 ratio often >3.5) →
4. **Macrophage activation and epithelioid/multinucleated giant cell differentiation** → **non-caseating granuloma** formation; macrophages secrete **ACE** and **1α-hydroxylase** (→ hypercalcemia) →
5. **Granuloma maintenance** by persistent antigen + cytokines →
6. Either **resolution** (Treg-mediated) **or** **M2-macrophage / TGF-β-driven fibrosis** → irreversible organ damage.

**Key molecular pathways (suggested GO/KEGG):**
- **mTORC1 / PI3K-AKT-mTOR** — landmark mechanism. Macrophage-specific **Tsc2 deletion → constitutive mTORC1 activation → CDK4-driven proliferation → spontaneous granulomas in mice**, and mTORC1 activity marks progressive human disease ([Linke et al., *Nat Immunol* 2017; PMID 28092373 ✓ / DOI 10.1038/ni.3655](https://www.nature.com/articles/ni.3655)). GO:0031929 (TOR signaling). A 2023 mTORC1-dependent **cardiac sarcoidosis mouse model** extends this ([PMID 37750561 ✓](https://pubmed.ncbi.nlm.nih.gov/37750561/)).
- **JAK–STAT (IFN-γ / STAT1)** — drives the granuloma transcriptome; targetable (tofacitinib normalizes it — see §12). GO:0007259.
- **TNF-α / NF-κB** — central to granuloma integrity; basis for anti-TNF therapy. GO:0033209.
- **NLRP3 inflammasome / IL-1β** — innate amplification. Simultaneous mTORC1/JAK-STAT/NLRP3 activation documented in patients ([PMC10454122](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10454122/)).
- **CCL24–CCR3 axis** (mTORC1-dependent) controls granuloma formation/maintenance ([PMC12338499 ⚠ 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12338499/)).

> "Activation of the metabolic checkpoint kinase mTORC1 in macrophages by deletion of the gene encoding tuberous sclerosis 2 (Tsc2) was sufficient to induce … excessive granuloma formation in vivo." — Linke et al. 2017

**Cellular processes & cell types (suggested CL):** CD4⁺ T helper cell **CL:0000492**, Th17 cell **CL:0000899**, regulatory T cell **CL:0000815**, macrophage **CL:0000235**, epithelioid cell / multinucleated giant cell, dendritic cell **CL:0000451**. **Treg dysfunction** is restored experimentally by IL-33 via PI3K/Akt/mTOR and TGF-β/Smad inhibition.

**Immune involvement:** Paradoxical state — heightened *local* (granuloma) Th1/Th17 activity but *peripheral* anergy/lymphopenia and **T-cell exhaustion** (PD-1↑); increasingly framed as having an **autoimmune component**. "Sarcoidosis pathogenesis reflects dysregulated crosstalk between innate and adaptive immunity … sustained by persistent antigen presentation to T cells" ([Immunopathogenesis review, *J Autoimmun* 2024](https://www.sciencedirect.com/science/article/pii/S0896841124000817)).

**Tissue damage:** chronic inflammation → **fibrosis** (TGF-β, M2 macrophages) — links to the dismech **`fibrotic_response`** module for pulmonary fibrosis; **granuloma-driven destruction** of cardiac conduction tissue, optic/cranial nerves.

**Biochemical hallmarks:** macrophage **ACE** overproduction; **1α-hydroxylase (CYP27B1)**-mediated extrarenal calcitriol synthesis → hypercalcemia/hypercalciuria; elevated **soluble IL-2 receptor (sIL-2R)**, **chitotriosidase**, **neopterin**.

**Comprehensive mechanism reviews:** *Sarcoidosis: molecular mechanisms and therapeutic strategies* ([PMC11794924 ✓ 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11794924/)); *Advance in pathogenesis of sarcoidosis* ([PMC10938127 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC10938127/)).

---

## 7. Anatomical Structures Affected

- **Primary organs:** lung **UBERON:0002048**, intrathoracic/hilar & mediastinal lymph nodes **UBERON:0000029**. Body system: **respiratory system UBERON:0001004**.
- **Secondary / multi-organ:** skin **UBERON:0002097**; eye **UBERON:0000970**; heart **UBERON:0000948** (myocardium UBERON:0002349, conduction system); CNS/peripheral nerves (brain UBERON:0000955; cranial nerve VII / facial nerve UBERON:0001647); liver **UBERON:0002107**; spleen **UBERON:0002106**; kidney **UBERON:0002113**; bone/bone marrow; parotid gland UBERON:0001831; joints.
- **Tissue/cell level:** alveolar macrophages, epithelioid histiocytes, multinucleated giant cells (Langhans type), CD4⁺ lymphocytes; granulomas are typically **perilymphatic** in lung (bronchovascular bundles, septa, pleura — basis for transbronchial/EBUS yield).
- **Subcellular (GO Cellular Component):** within macrophages — **asteroid bodies** and **Schaumann bodies** (calcified inclusions) are characteristic histologic inclusions; lysosomal/phagosomal compartments (GO:0005764).
- **Localization/laterality:** pulmonary involvement is **bilateral** (bilateral hilar lymphadenopathy is the imaging signature); skin/eye often bilateral/symmetric.

---

## 8. Temporal Development

- **Onset:** typically **adult (20–45y)**, with a **second peak in women >50y**; pediatric sarcoidosis rare (early-onset **Blau syndrome / NOD2** is a distinct Mendelian granulomatous mimic — *do not conflate*). Onset acute (Löfgren) or insidious.
- **Scadding chest-radiograph stages (prognostic):** Stage 0 (normal) → I (bilateral hilar adenopathy) → II (adenopathy + parenchymal infiltrates) → III (parenchymal infiltrates alone) → IV (fibrosis/honeycombing). Higher stage → lower spontaneous remission.
- **Course patterns:** **self-limiting/remitting (~50–70%, often within 2–3 yrs)**, **chronic-persistent**, **relapsing-remitting**, or **progressive-fibrotic**. **Löfgren syndrome** (acute triad: bilateral hilar adenopathy + erythema nodosum + arthralgia/fever) has **>85–90% spontaneous resolution**, especially with HLA-DRB1*03.
- **Critical windows:** treatment decisions typically deferred in asymptomatic Stage I; intervention prioritized for threatened vital-organ function (cardiac, neuro, ocular, progressive pulmonary).

---

## 9. Inheritance and Population

**Epidemiology:**
- **Incidence:** ~1–15 per 100,000/yr, region-dependent — lowest in East Asia (~0.5–1), intermediate in N. America/Australia (~5–10), highest in **Scandinavia (~11–15)** ([Rossides et al., *J Intern Med* 2023, DOI 10.1111/joim.13629](https://onlinelibrary.wiley.com/doi/10.1111/joim.13629)).
- **Prevalence:** roughly 1–40 per 100,000 (population-dependent); US lifetime risk ~2.4% (Black) vs ~0.85% (White).
- **Race:** In the US, **Black > White ~3–4:1**; highest age-specific incidence in **Black women aged 30–39 (~107/100,000)** ([Sarcoidosis Epidemiology: Race Matters, PMC7522309](https://pmc.ncbi.nlm.nih.gov/articles/PMC7522309/)). Black patients have **more multiorgan disease, more severe pulmonary disease, higher hospitalization and mortality**.
- **Sex:** approximately equal (slight female predominance); female onset peaks later.
- **Age:** classic peak 25–45y; **rising incidence in older adults (>65y)**; mean diagnosis age now >50 in some datasets.

**Inheritance:** **Not Mendelian — complex/polygenic with environmental contribution.** Familial clustering exists: ACCESS found first-degree relatives at ~5× risk (sibling relative risk highest); concordance higher in monozygotic twins. **No classic penetrance/expressivity/anticipation/founder figures apply** in the Mendelian sense. (For dismech: model inheritance as **multifactorial/polygenic**, GENO susceptibility, *not* AD/AR.)

England population-based study (2024) provides recent incidence/prevalence/mortality figures ([PMC12002749](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12002749/)); Japan nationwide claims study ([PMC12127000](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12127000/)).

---

## 10. Diagnostics

Diagnosis is one of **exclusion + compatible clinico-radiologic picture + histologic non-caseating granulomas with no alternative cause** (per **ATS 2020 guideline**, [Crouser et al., *Am J Respir Crit Care Med* 2020;201(8):e26–e51; **PMID 32293205 ✓**](https://academic.oup.com/ajrccm/article/201/8/e26/8496541)).

**Histopathology (gold standard, SNOMED/path):** non-necrotizing (non-caseating) epithelioid-cell granulomas; Langhans giant cells; asteroid & Schaumann bodies; **must exclude infection (special stains for AFB/fungi) and beryllium.**

**Tissue acquisition:** **EBUS-TBNA** (endobronchial ultrasound–guided transbronchial needle aspiration) of mediastinal nodes is now first-line (higher yield, ATS-recommended); transbronchial lung biopsy; skin/peripheral node biopsy when accessible.

**Biomarkers (supportive, not diagnostic alone):**
- **Serum ACE** — sensitivity ~62%, specificity ~76%.
- **Soluble IL-2 receptor (sIL-2R)** — **superior to ACE (sens ~88%, spec ~85%)** ([PMC6797090](https://pmc.ncbi.nlm.nih.gov/articles/PMC6797090/)); also activity marker.
- **Hypercalcemia/hypercalciuria; chitotriosidase; lysozyme; neopterin.** **BAL CD4:CD8 ratio >3.5** supports diagnosis (high specificity).
- LOINC: ACE LOINC:2004-6 ⚠; serum calcium LOINC:17861-6.

**Imaging:**
- **Chest radiograph** (Scadding staging) and **HRCT** (perilymphatic micronodules, beaded fissures, hilar/mediastinal adenopathy).
- **¹⁸F-FDG-PET/CT** — disease activity, occult sites, viable inflammation vs fibrosis.
- **Cardiac MRI (late gadolinium enhancement)** + FDG-PET — cornerstone of **cardiac sarcoidosis** detection; ECG/Holter for conduction disease/arrhythmia.
- **MRI brain/spine** + CSF (↑protein, lymphocytic pleocytosis, ↑CSF ACE) for neurosarcoidosis.
- Ophthalmologic slit-lamp exam (uveitis screening — recommended in all patients).

**Differential diagnosis:** tuberculosis & other mycobacterial/fungal infection, **chronic beryllium disease** (clinically identical — BeLPT distinguishes), lymphoma, hypersensitivity pneumonitis, granulomatosis with polyangiitis, IgG4-related disease, common variable immunodeficiency–associated granulomatous disease, **Blau syndrome/NOD2** (pediatric), sarcoid-like reactions to malignancy or checkpoint-inhibitor immunotherapy.

**Genetic testing:** *not* used for diagnosis (polygenic); research/HLA-typing only (DRB1*03 for prognosis). **No screening program**; cascade/newborn screening N/A.

---

## 11. Outcome / Prognosis

- **Overall mortality:** low overall — death in roughly **5–10%** of patients; mortality is rising in some registries. Leading causes: **progressive pulmonary fibrosis with respiratory failure / pulmonary hypertension** (esp. US/Europe) and **cardiac sarcoidosis (sudden death, arrhythmia, heart failure)** (esp. Japan).
- **Prognosis by phenotype:** **Löfgren syndrome → excellent (>85–90% remission)**; lupus pernio, cardiac, neuro, Stage IV fibrotic, and **multiorgan disease in Black patients → worse.**
- **Morbidity/QoL:** fatigue, dyspnea, depression, and small-fiber neuropathy dominate disability; **steroid toxicity** is a major iatrogenic morbidity (drives the steroid-sparing agenda below).
- **Complications:** pulmonary fibrosis, **pulmonary hypertension (SAPH)**, aspergilloma/mycetoma in fibrocavitary disease, complete heart block / ventricular arrhythmia / sudden cardiac death, blindness (untreated uveitis), nephrocalcinosis/renal failure (hypercalcemia), neuroendocrine dysfunction.
- **Prognostic factors:** Scadding stage, lupus pernio, cardiac/neuro involvement, race, age >40 at onset, splenomegaly, need for treatment >6 months, and biomarkers (persistently ↑sIL-2R, FDG-PET activity). HLA-DRB1*03:01 = favorable.

---

## 12. Treatment

**Guidelines:** **ERS 2021 treatment guideline** ([Baughman, Wells et al., *Eur Respir J* 2021;58(6):2004079; **PMID 34140301 ✓**](https://publications.ersnet.org/content/erj/58/6/2004079)) and **BTS 2021**. Many patients (esp. asymptomatic Stage I/Löfgren) need **no treatment**; treat to preserve organ function/QoL.

**Stepwise pharmacotherapy** (suggest **MAXO** terms; treatment_term `NCIT:C15986` Pharmacotherapy + CHEBI `therapeutic_agent`):
1. **First-line: oral glucocorticoids** (prednisone) — for symptomatic/threatened-organ disease; ERS advises limiting to a **3–6 month** trial, maintenance **<10 mg/day**. MAXO: `MAXO:0000950` supportive? better generic Pharmacotherapy; CHEBI:8378 prednisone / CHEBI:8382 prednisolone.
2. **Second-line steroid-sparing:** **methotrexate** (CHEBI:44185; most-used), azathioprine (CHEBI:2948), leflunomide, mycophenolate, **hydroxychloroquine** (CHEBI:5801; cutaneous/hypercalcemia/neuro).
3. **Third-line biologics: anti-TNF-α — infliximab** (NCIT:C1296; therapeutic_modality MONOCLONAL_ANTIBODY) for refractory pulmonary, neuro, lupus pernio; **adalimumab** alternative. ERS: conditional recommendation, low-quality evidence. Real-world data: [Respir Res 2022](https://respiratory-research.biomedcentral.com/articles/10.1186/s12931-022-01971-5).

**Emerging / mechanism-targeted:**
- **JAK inhibitors — tofacitinib** (CHEBI:71200): striking responses in cutaneous and multiorgan sarcoidosis; reverses the IFN-γ/JAK-STAT granuloma transcriptome ([Damsky et al., *NEJM* 2018;379:2540–2546; **PMID 30586519 ✓** / DOI 10.1056/NEJMoa1805958](https://www.nejm.org/doi/full/10.1056/NEJMoa1805958)); also ruxolitinib, laryngeal case [PMID 39295484 ⚠](https://pubmed.ncbi.nlm.nih.gov/39295484/).
- **Efzofitimod (ATYR1923)** — first-in-class **neuropilin-2 (NRP2)** immunomodulator. **Phase 3 EFZO-FIT (Sept 2025): MISSED primary endpoint** (steroid-dose reduction 2.79 vs 3.52 mg, p=0.33) but **52.6% vs 40.2% achieved complete steroid withdrawal** with QoL/FVC benefit and good safety ([aTyr topline release](https://investors.atyrpharma.com/news-releases/news-release-details/atyr-pharma-announces-topline-results-phase-3-efzo-fittm-study); NCT03824392 / EFZO-FIT NCT05415137 ⚠).
- mTOR-pathway and CCL24/CCR3 inhibition are preclinical targets (see §6).

**Organ-specific/interventional:**
- **Cardiac:** immunosuppression + **ICD** (device; arrhythmia/sudden-death prevention), pacemaker for heart block, antiarrhythmics.
- **Hypercalcemia:** corticosteroids, hydroxychloroquine, low calcium/vit-D intake, sun avoidance.
- **End-stage:** **lung transplantation** (MAXO:0010039 organ transplantation) / heart transplant; pulmonary rehabilitation; treat SAPH.
- **Supportive:** fatigue/neuropathy management, antidepressants, pulmonary rehab (MAXO:0000950 supportive care; MAXO:0000011 physical therapy).

**Pharmacogenomics:** **TPMT/NUDT15** genotyping before azathioprine (myelotoxicity risk; CPIC guideline). Steroid response heterogeneous.

---

## 13. Prevention

- **No primary prevention** exists (cause unknown, not vaccine-preventable). Risk reduction limited to **avoiding implicated occupational/inhalational exposures** (e.g., WTC-type dust, beryllium control) — more occupational hygiene than personal prevention.
- **Secondary prevention:** early ophthalmologic screening (prevent uveitis blindness), **baseline + periodic ECG/cardiac screening** (detect occult cardiac sarcoidosis → prevent sudden death), monitoring calcium/renal function.
- **Tertiary prevention:** steroid-sparing strategies to prevent iatrogenic harm; FDG-PET/CMR-guided escalation to prevent fibrosis; ICD in high-risk cardiac disease.
- **Counseling:** family risk is modestly elevated but **routine genetic counseling/testing is not indicated** (polygenic). Smoking cessation advised for general health despite the inverse risk association.
- No immunization, no prophylactic medication, no public-health/vector measures (non-infectious).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** primarily a **human (NCBITaxon:9606)** disease — no validated naturally occurring animal homolog.
- **Veterinary:** A clinically and histologically analogous idiopathic systemic granulomatous disease occurs in **horses (NCBITaxon:9796)** — *equine sarcoidosis / equine systemic granulomatous disease* (generalized granulomatous dermatitis ± internal organs). Granulomatous diseases occur in dogs/cats but are not true sarcoidosis homologs.
- **Comparative biology:** the closest experimental analog is **chronic beryllium disease** (HLA-DPB1*Glu69-restricted) — a defined-antigen model of an otherwise sarcoidosis-like granulomatosis.
- **Zoonosis:** none — sarcoidosis is non-infectious and non-transmissible.

---

## 15. Model Organisms

No model fully recapitulates human sarcoidosis; granuloma-focused models dominate ([review, *Front Immunol* 2020](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2020.01719/full)).

- **Mouse (NCBITaxon:10090):**
  - **mTORC1/Tsc2-knockout macrophage model (Linke 2017, PMID 28092373 ✓):** myeloid **Tsc2** deletion → constitutive mTORC1 → spontaneous progressive granulomas; **best genetic model**, recapitulates macrophage proliferation/granuloma growth and progression marker biology. Conditional/Cre-lox (LysM-Cre).
  - **mTORC1-dependent cardiac sarcoidosis mouse (2023, PMID 37750561 ✓):** models cardiac granulomas/conduction disease.
  - **Antigen-induced granuloma models:** *C. acnes*, mycobacterial mKatG/ESAT-6, and **bead/multiwall carbon nanotube + sarcoid-antigen** induction models reproduce granuloma histology.
  - **Adoptive-transfer / Th17 / IL-33 Treg-dysfunction models** for immune mechanism.
- **In vitro / human:** **granuloma-in-a-dish** — PBMC-derived granuloma models (with *C. acnes* or beads); **iPSC-derived macrophages**; BAL-cell transcriptomics (GEO datasets).
- **Limitations:** no single model captures the multiorgan, chronic-relapsing, antigen-ambiguous human disease; most are acute/induced or single-pathway (mTORC1) and lack the human HLA-restricted adaptive arm.
- **Resources:** MGI (Tsc2 conditional alleles), IMPC/KOMP, GEO/ArrayExpress for transcriptomic datasets.

---

## Suggested dismech modeling anchors

- **Module reuse:** link fibrotic pulmonary endpoint to **`fibrotic_response`** (tissue injury → inflammation → mesenchymal activation → ECM → organ dysfunction); cardiac arrhythmic complications could cross-reference electrical-remodeling concepts. Consider whether a new **granuloma-formation mechanism module** (Th1/Th17 → macrophage epithelioid differentiation → mTORC1-driven granuloma) is warranted given recurrence across granulomatous diseases (TB, Crohn, berylliosis, Blau).
- **Inheritance:** model as **multifactorial/polygenic**, GENO susceptibility associations (HLA-DRB1, BTNL2, ANXA11) — **not** Mendelian causal variants.
- **Evidence sourcing:** core mechanism = MODEL_ORGANISM (Linke mouse) + IN_VITRO; epidemiology/prognosis/treatment = HUMAN_CLINICAL; mTORC1 marker work mixes IN_VITRO + HUMAN_CLINICAL — split evidence items accordingly.

---

## Key References (verify all before committing)

| # | Citation | ID |
|---|---|---|
| 1 | Grunewald J, et al. Sarcoidosis. *Nat Rev Dis Primers* 2019;5:45. | DOI 10.1038/s41572-019-0096-x; PMID **31273209** ⚠ |
| 2 | Crouser ED, et al. Diagnosis and Detection of Sarcoidosis: ATS Clinical Practice Guideline. *Am J Respir Crit Care Med* 2020;201(8):e26–e51. | PMID **32293205** ✓ |
| 3 | Baughman RP, Wells AU, et al. ERS guidelines on treatment of sarcoidosis. *Eur Respir J* 2021;58(6):2004079. | PMID **34140301** ⚠ |
| 4 | Linke M, et al. Chronic mTORC1 signaling induces macrophage granuloma formation and marks sarcoidosis progression. *Nat Immunol* 2017;18:293–302. | PMID **28092373** ✓; DOI 10.1038/ni.3655 |
| 5 | Damsky W, et al. Tofacitinib Treatment and Molecular Analysis of Cutaneous Sarcoidosis. *NEJM* 2018;379:2540–2546. | PMID **30586519** ✓ |
| 6 | Rossides M, et al. Sarcoidosis: Epidemiology and clinical insights. *J Intern Med* 2023. | DOI 10.1111/joim.13629 ⚠ |
| 7 | Morais A, et al. ANXA11/BTNL2/HLA and sarcoidosis course. *Clin Respir J* 2018. | PMID **27662826** ✓ |
| 8 | eQTL polymorphisms & progressive complicated sarcoidosis. 2024. | PMID **38390497** ✓ |
| 9 | mTORC1-dependent mouse model for cardiac sarcoidosis. *JAHA* 2023. | PMID **37750561** ✓ |
| 10 | Sarcoidosis: molecular mechanisms and therapeutic strategies. 2025. | PMC11794924 |
| 11 | aTyr Pharma, EFZO-FIT Phase 3 topline (efzofitimod), Sept 2025. | [press release](https://investors.atyrpharma.com/news-releases/news-release-details/atyr-pharma-announces-topline-results-phase-3-efzo-fittm-study) |

**Sources (web):**
- [Grunewald 2019 Nat Rev Dis Primers](https://www.nature.com/articles/s41572-019-0096-x)
- [ATS 2020 diagnosis guideline (Crouser)](https://academic.oup.com/ajrccm/article/201/8/e26/8496541)
- [ERS 2021 treatment guideline](https://publications.ersnet.org/content/erj/58/6/2004079)
- [Linke 2017 mTORC1, Nat Immunol](https://www.nature.com/articles/ni.3655)
- [Damsky 2018 tofacitinib, NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa1805958)
- [Rossides 2023 epidemiology, J Intern Med](https://onlinelibrary.wiley.com/doi/10.1111/joim.13629)
- [Sarcoidosis Epidemiology: Race Matters](https://pmc.ncbi.nlm.nih.gov/articles/PMC7522309/)
- [Morais 2018 ANXA11/BTNL2/HLA, PMID 27662826](https://pubmed.ncbi.nlm.nih.gov/27662826/)
- [eQTL progressive sarcoidosis, PMID 38390497](https://pubmed.ncbi.nlm.nih.gov/38390497/)
- [Cardiac sarcoidosis mTORC1 mouse, PMID 37750561](https://pubmed.ncbi.nlm.nih.gov/37750561/)
- [Molecular mechanisms & therapeutics 2025, PMC11794924](https://pmc.ncbi.nlm.nih.gov/articles/PMC11794924/)
- [Immunopathogenesis review, J Autoimmun 2024](https://www.sciencedirect.com/science/article/pii/S0896841124000817)
- [mTORC1/JAK-STAT/NLRP3 in patients, PMC10454122](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10454122/)
- [sIL-2R diagnostic accuracy, PMC6797090](https://pmc.ncbi.nlm.nih.gov/articles/PMC6797090/)
- [aTyr EFZO-FIT Phase 3 topline](https://investors.atyrpharma.com/news-releases/news-release-details/atyr-pharma-announces-topline-results-phase-3-efzo-fittm-study)
- [ANXA11 association, Genes & Immunity](https://www.nature.com/articles/gene201248)
- [Sarcoidosis models review, Front Immunol 2020](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2020.01719/full)
- [Latent microbial reactivation review 2025, PMC12362391](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12362391/)
- [England population-based study 2024, PMC12002749](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12002749/)

---

**Bottom line:** sarcoidosis is best modeled in dismech as a complex (polygenic + environmental) **immune granulomatous disease** whose pathophysiology runs *HLA-restricted antigen presentation → Th1/Th17.1 activation → IFN-γ/TNF-driven macrophage epithelioid differentiation → mTORC1-sustained non-caseating granuloma → resolution (Treg) or TGF-β/M2 fibrosis*. The two highest-value, well-verified mechanistic citations are **Linke 2017 (mTORC1, PMID 28092373)** and **Crouser 2020 (ATS diagnosis, PMID 32293205)**; the freshest clinical development is the **2025 efzofitimod Phase 3 miss-but-signal**. Re-verify every PMID with `just fetch-reference` before it lands in a YAML evidence block.