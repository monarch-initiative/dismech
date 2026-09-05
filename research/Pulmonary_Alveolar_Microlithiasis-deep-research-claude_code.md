---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-16T10:01:44.435492'
end_time: '2026-08-16T10:14:38.106358'
duration_seconds: 773.67
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pulmonary Alveolar Microlithiasis
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 5
  num_turns: 34
  total_cost_usd: 4.289822999999999
  session_id: 62a3a0a3-3773-4d2b-8098-0753e315d473
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 17
reference_validation:
  total_references: 36
  verified: 33
  not_found: 3
  unverifiable: 0
  confabulation_rate: 0.083
  quotes_checked: 1
  quotes_valid: 1
  unresolved_references:
  - PMID:41019964
  - PMID:37663718
  - PMID:42194933
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pulmonary Alveolar Microlithiasis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Pulmonary Alveolar Microlithiasis** covering all of the
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

I'll dig into this properly — searching now.

# Pulmonary Alveolar Microlithiasis — Research Report

**Prepared:** 2026-08-16 · **Target:** `kb/disorders/Pulmonary_Alveolar_Microlithiasis.yaml` · **MONDO:0009928**

sup. so PAM is one of those diseases that reads like a geology paper wearing a lung. the alveoli — the little wet grape-cluster air sacs where you actually breathe — slowly fill with tiny stones. Not metaphor-stones. Actual concentrically-layered hydroxyapatite pebbles, the same mineral your bones are made of, laid down ring by ring like a pearl or a cave formation, in a place that is supposed to be nothing but thin fluid and air.

And the cause turns out to be beautifully, almost cartoonishly simple: one broken pump.

---

## 0. Verification status — read this before you curate a single line

Everything below is sourced. But two tiers exist and mixing them will bite you:

| Tier | What it is | Safe to quote as `snippet:`? |
|---|---|---|
| **A — verbatim abstract** | Pulled from Europe PMC `abstractText` field, word for word | Yes, after `just fetch-reference` + `just count-verified-snippets` |
| **B — full-text derived** | Numbers extracted from the PMC full text of the 2020 ERS review (incidence-per-million, the 53-patient Japanese cohort, the 18 transplant cases) | **No** — these won't match a cached *abstract*, and `just validate-disorders` runs `--no-full-text`. Put them in `notes:` or find an abstract that states them |

**Ontology IDs:** the HPO terms marked ✅ came from the live JAX annotation API for OMIM:265100. Everything marked 🔍 is my suggestion and **must** be run through `just validate-terms` / OAK before it goes in the file. I am not guessing IDs into your KB.

**NEC preflight (informal):** SLC34A2 dominates every source; OMIM 265100 matches the MONDO xref; no rival gene appears. The name-collision risk here is *semantic*, not genetic — PAM is chronically confused with **pulmonary alveolar proteinosis** (also "PAP", also alveolar, also crazy-paving on CT, completely different mechanism) and with **testicular microlithiasis** (a real but separate entity that shares the gene sideways). Keep those straight.

---

## 1. Disease Information

### What it is

A rare autosomal-recessive lung disease in which calcium-phosphate concretions ("microliths") accumulate inside the alveolar airspaces, progressing over decades toward fibrosis, pulmonary hypertension, and respiratory failure.

> **Verbatim, Kosciuk et al. 2020 (PMID:33246992):** "Pulmonary alveolar microlithiasis (PAM) is a fascinating rare lung disease that is associated with the accumulation of hydroxyapatite microliths within the lumen of the alveolar spaces. In most patients, PAM is discovered incidentally on radiographs performed for other purposes, and the typical disease course is characterised by slowly progressive respiratory insufficiency over decades."

> **Verbatim, Castellana et al. 2015 (PMID:26621975):** "Pulmonary alveolar microlithiasis (PAM) is a rare disease characterised by the widespread intra-alveolar accumulation of minute calculi called microliths. It is caused by mutation of the SLC34A2 gene encoding the type IIb sodium phosphate cotransporter in alveolar type II cells."

The single most characteristic thing about PAM clinically is the **mismatch**. The chest film looks like someone shook a jar of sand over the patient's lungs, and the patient shrugs and says they feel fine. Enemark et al. 2021 (PMID:34970102) name it outright:

> **Verbatim:** "A hallmark of the disease is the discrepancy between perceived symptoms upon diagnosis compared with the extensive, sandstorm-like appearance of the microliths on chest X-ray or HRCT."

### Identifiers (all verified against MONDO via OLS)

| Resource | ID |
|---|---|
| **MONDO** | `MONDO:0009928` |
| **OMIM** | `265100` (PULAM) |
| **Orphanet** | `ORPHA:60025` |
| **UMLS** | `C0155912` |
| **MeSH** | `C562405` |
| **MedGen** | `56374` |
| **ICD-10-CM** | `J84.02` |
| **ICD-9** | `516.2` |
| **ICD-11** | foundation `1220010076` |
| **DOID** | `DOID:12117` |
| **GARD** | `0011894` |
| **SNOMED CT** | `87153008` |
| **MedDRA** | `10037315` |
| **NANDO** (Japan) | `2200202` |

⚠️ Note the Orphanet number: several secondary sources float `ORPHA:44042` — the MONDO equivalent-xref is **60025**. Use 60025.

### Synonyms

PAM; PULAM (OMIM symbol); pulmonary microlithiasis; alveolar microlithiasis; "microlithiase alvéolaire pulmonaire"; historically "pulmonary alveolar calcinosis" and in older Turkish/Italian literature "sandstorm lung" (descriptive, not formal).

### Data provenance

Everything in the literature is **aggregate-level and case-based**. There is no PAM registry, no EHR cohort, no biobank series. The largest single evidence object in the field is a literature census — Castellana's 1,022 cases assembled from 544 papers. Treat every prevalence figure accordingly.

---

## 2. Etiology

### Causal factor — one gene, and that's basically it

Biallelic loss-of-function variants in **SLC34A2** (HGNC:11020, 4p15.2), encoding **NaPi-IIb / NPT2b**, a sodium-dependent phosphate cotransporter.

Two groups landed it independently in 2006–2007, from opposite directions:

> **Verbatim, Corut et al. 2006 (PMID:16960801):** "We first identified a PAM locus by homozygosity mapping to 4p15, then identified, by a candidate-gene approach, the gene responsible for the disease as SLC34A2 (the type IIb sodium-phosphate cotransporter gene), which is involved in phosphate homeostasis in several organs. We identified six homozygous exonic mutations in the seven unrelated patients with PAM we studied... We show that impaired activity of the phosphate transporter is presumably responsible for the microliths and that PAM is a recessive monogenic disease with full penetrance."

> **Verbatim, Huqun et al. 2007 (PMID:17095743):** "We identified a candidate gene, SLC34A2, that encodes a type IIb sodium phosphate cotransporter and that is mutated in six of six patients investigated. SLC34A2 is specifically expressed in type II alveolar cells, and the mutations abolished the normal gene function." … "Mutations in the SLC34A2 gene that abolish normal gene function cause pulmonary alveolar microlithiasis."

**"Full penetrance" is an explicit, quotable claim** (Corut 2006) — worth curating as such, and worth noting it sits in tension with the wild variability in *severity* (see §9).

### Risk factors

**Genetic:** biallelic SLC34A2 — necessary and sufficient, as far as anyone can tell. No susceptibility loci, no GWAS (population too small), no established modifier genes.

**Consanguinity:** the dominant "risk factor" in practice, because it's how you get two copies of a rare recessive allele. Enemark 2021: *"an autosomal recessive transmitted disorder, and as such has a high correlation to consanguinity."* The ERS review reports consanguinity in **22% of familial cases** (Tier B, full text).

**Environmental:** none established. Historically people blamed dust, milk, water minerals — all of it evaporated once the gene was found. Castellana 2015 is careful here and it matters:

> **Verbatim:** "The clinical course is not uniform and the causes of this clinical variability seem to be largely nongenetic."

That sentence is doing something subtle and useful for your entry: **the disease is genetic; the trajectory is not (entirely).** Nobody has identified what the nongenetic modifiers are. That's a legitimate `KNOWLEDGE_GAP` discussion.

### Protective factors

None known in humans. But here's the interesting one — **dietary phosphate restriction is protective in the mouse**, which makes it a candidate protective exposure with a mechanism behind it (see §12 and §15). In the one reported human trial of a low-phosphate diet, disease progressed anyway despite serum phosphate dropping (Tier B, ERS review). Which tells you something important: the relevant phosphate pool is **local, in the alveolar lining fluid**, not the one your blood test measures.

### Gene–environment interaction

Mechanistically plausible and preclinically demonstrated (dietary phosphate load × NaPi-IIb deficiency), clinically unproven. Note the wrinkle: SLC34A2 is *also* the main intestinal phosphate absorber, so a PAM patient has a partly-disabled gut phosphate uptake system too — meaning the dietary-phosphate lever may pull differently than intuition suggests.

---

## 3. Phenotypes

### HPO annotations — verified live from the JAX API (OMIM:265100)

| HP ID | Label | Frequency as annotated |
|---|---|---|
| ✅ `HP:0006514` | Intraalveolar nodular calcifications | — (defining) |
| ✅ `HP:0002091` | Restrictive ventilatory defect | — |
| ✅ `HP:0006520` | Progressive pulmonary function impairment | — |
| ✅ `HP:0003677` | Slowly progressive | — |
| ✅ `HP:0000007` | Autosomal recessive inheritance | — |
| ✅ `HP:0011462` | Young adult onset | 4/8 |
| ✅ `HP:0003621` | Juvenile onset | 3/8 |
| ✅ `HP:0011463` | Childhood onset | 1/8 |

That onset breakdown (8 annotated individuals) is thin evidence for a frequency band. Per your frequency SOP — **I'd omit `frequency:` on onset rather than manufacture a band from n=8.**

### Clinical phenotypes with literature-grounded frequency language

**Asymptomatic at diagnosis — the majority.** Mariotta 2004 (PMID:15554073) is the cleanest quotable source:

> **Verbatim:** "Symptoms were absent in more than half the patients; dyspnoea, cough and chest pain were reported in the other cases."

Maps to roughly `FREQUENT` for the asymptomatic state. Suggested candidate terms (🔍 all need OAK verification):

| Phenotype | Candidate HP | Notes on frequency evidence |
|---|---|---|
| Exertional dyspnea | 🔍 `HP:0002875` | Most common symptom once symptomatic (Mariotta 2004, Bendstrup 2020) |
| Dry / nonproductive cough | 🔍 `HP:0031246` | Co-leading symptom |
| Chest pain | 🔍 `HP:0100749` | Third-ranked (Mariotta 2004) |
| Fatigue | 🔍 `HP:0012378` | Listed by Bendstrup 2020 |
| Digital clubbing | 🔍 `HP:0100759` | ~7% (Tier B, ERS review) |
| Cyanosis | 🔍 `HP:0000961` | "Less frequent" (Tier B) |
| Hemoptysis | 🔍 `HP:0002105` | "Less frequent" (Tier B) |
| Spontaneous pneumothorax | 🔍 `HP:0002107` | 1.6% (Tier B); recent case PMID:41939679 |
| Pulmonary fibrosis | 🔍 `HP:0002206` | Late-stage |
| Pulmonary hypertension | 🔍 `HP:0002092` | Late-stage; PMID:8215680 documents severe PH pre-transplant |
| Cor pulmonale | 🔍 `HP:0001648` | Terminal; Jönsson 2012 (PMID:22941890) names it explicitly |
| Respiratory failure | 🔍 `HP:0002878` | Cause of death |
| Reduced DLCO | 🔍 verify — do not guess | "reduction in diffusion capacity for carbon monoxide is most typical" (Tier B) |

Bendstrup & Jönsson 2020 (PMID:32964001) gives you the symptom quartet verbatim:

> **Verbatim:** "Many patients are asymptomatic and the diagnosis is made at random. When symptomatic, dyspnoea, cough, chest pain and fatigue are common complaints."

And Jönsson 2012 (PMID:22941890) gives you the physiology and the bifurcating course in one sentence:

> **Verbatim:** "Many patients are asymptomatic and the majority of patients either have normal or restrictive pulmonary function. The clinical course of the disease varies. While it remains static in some patients, it progresses into pulmonary fibrosis, respiratory failure and cor pulmonale in others."

### Extrapulmonary phenotypes

Because SLC34A2 is expressed beyond lung, calcification shows up elsewhere — reported in **seminal vesicles, testes, epididymis, and heart valves** (Jönsson 2023 full text). Two anchor citations:

- **Aortic valve sclerosis** — Jönsson et al. 2012 letter, *AJRCCM* (PMID:22336687), "SLC34A2 gene mutation may explain comorbidity of pulmonary alveolar microlithiasis and aortic valve sclerosis." (Letter — **no abstract**, so per your §6 rule, don't try to snippet it; cite in `notes:` or find the full-text-supported claim elsewhere.)
- **Tricuspid valve calcification** in familial PAM — PMID:32528675.
- **Gastric mucosal calcification** — PMID:38784230.
- **Testicular microlithiasis** — the weakest link and worth curating *as* weak. Corut 2006, verbatim: *"In 2 of the 15 subjects with TM we studied, we identified two rare variants, one synonymous and the other noncoding, that are possibly associated with the condition."* That is a `PARTIAL` at best. A synonymous and a noncoding variant in 2/15 subjects is a hypothesis, not an association. Do not let the paper's *title* ("...and are possibly associated with testicular microlithiasis") do work its results don't support — that's exactly the title-is-not-a-finding trap.

Newer supporting biology for the reproductive-tract angle: Cui et al. 2025 (PMID:41183425) show *"abundant SLC34A2 expression in seminal vesicle."*

### Quality of life

No PAM-specific QoL instrument, no EQ-5D/SF-36/PROMIS data. The honest statement is: unmeasured. Jönsson 2023 gestures at it verbatim — *"some patients remain asymptomatic while others develop severe respiratory failure with a significant symptom burden and compromised survival"* — but that's clinical, not instrumented.

---

## 4. Genetic / Molecular Information

### The gene (HGNC REST, verified)

| Field | Value |
|---|---|
| HGNC ID | `HGNC:11020` (lowercase `hgnc:11020` in dismech) |
| Symbol / name | SLC34A2 / solute carrier family 34 member 2 |
| Locus | **4p15.2** |
| NCBI Gene | 10568 |
| Ensembl | ENSG00000157765 |
| UniProt | **O95436** |
| RefSeq | NM_006424 |
| Gene OMIM | 604217 |
| Aliases | NaPi-2b, NaPi-IIb, NPTIIb, NAPI-3B, NAPI-IIb |

### Variant spectrum — the 2023 systematic review is your anchor

> **Verbatim, Jönsson et al. 2023 (PMID:37259144):** "Rare variants in SLC34A2 are found in almost all genetically tested patients. So far, 34 allelic variants have been identified in at least 68 patients. A majority of these are present in the homozygous state; however, a few are found in the compound heterozygous form. Most of the allelic variants involve only a single nucleotide. Half of the variants are either nonsense or frameshifts, resulting in premature termination of the protein or decay of the mRNA."

Full-text breakdown of the 34 variants (49 families): missense 29% (10), nonsense 24% (8), frameshift 21% (7), large deletion 15% (5), splice-site 9% (3), in-frame deletion 3% (1).

**Functional consequence:** uniformly **loss of function** — `functional_impact_category: LOSS_OF_FUNCTION` on `GeneticContext`. No gain-of-function, no dominant-negative reported. Carriers (heterozygotes) are unaffected.

### Population/ethnic clustering of specific alleles

Not classical founder mutations, but recurrent alleles cluster by ancestry (Jönsson 2023 full text):

| Variant | Population |
|---|---|
| `c.226C>T` | Middle Eastern |
| `c.910A>T` (p.Lys304Ter) | Chinese |
| `c.1048+1G>A` | Japanese |
| `c.1402_1404delACC` (p.Thr468del) | European |

`c.910A>T` also shows up in a 2026 Chinese pediatric compound-het case with a novel splice partner: *"novel compound heterozygous variants in SLC34A2: c.524-1G>C (IVS5) inherited maternally and c.910A>T (EX8) of paternal origin"* (Zhou et al. 2026, PMID:41878462).

### Functional characterization — the one variant that breaks the pattern

This is the most mechanistically informative paper in the whole disease, and it deserves its own pathophysiology node.

> **Verbatim, Jönsson et al. 2022, *Human Genomics* (PMID:35443721):**
> **Methods:** "Two nonsense variants (c.910A > T and c.1456C > T), one frameshift (c.1328delT), and one in-frame deletion (c.1402_1404delACC) previously reported in patients with PAM were selected for investigation. Wild-type and mutant c-Myc-tagged human NaPi-IIb constructs were expressed in Xenopus laevis oocytes."
> **Results:** "Although the protein from the Thr468del construct was synthesised and expressed in the oocyte membrane, phosphate transport was similar to non-injected control oocytes. All other mutants were non-functional and not expressed in the membrane, consistent with the expected impact of the truncations caused by premature stop codons."
> **Conclusions:** "Of four analysed SLC34A2 variants, only the Thr468del showed similar protein expression as the wild-type cotransporter in the oocyte membrane. All mutant transporters were non-functional, supporting that dysfunction of NaPi-IIb underlies the pathology of PAM."

Two mechanistically distinct routes to the same dead end, which is exactly the kind of thing your schema is built to hold:
1. **Truncating variants** → no protein at the membrane (absent transporter)
2. **Thr468del** → protein *is* at the membrane, correctly trafficked, and simply doesn't move phosphate (dead transporter in place)

Both `LOSS_OF_FUNCTION`, different subcellular story. `evidence_source: IN_VITRO` for all of it (Xenopus oocyte expression — and note that's a heterologous *expression* system, not an animal model of the disease; classify carefully).

### Genotype–phenotype correlation — real but soft

> **Verbatim, Jönsson et al. 2020, *ERJ* (PMID:31831582):** "We identified eight novel allelic variants of SLC34A2 in 14 patients with PAM. Four of these were nonsense variants, three were missense and one was a splice site variant. One patient was heterozygous for two different variants and all other patients were homozygous. Four patients were asymptomatic and 10 patients were symptomatic. The severity of the disease was associated with the variant severity." … "An association between disease severity and the severity of the variants was found; however, this needs to be investigated in larger patient populations."

Curate the caveat with the claim. n=14, severity score home-built by the authors. The 2023 review is blunter about it: *"Functional studies exploring the effect of human SLC34A2 variants are sparse, and there is no standardized criterion for clinical classification."*

### Modifier genes, epigenetics, chromosomal abnormalities

- **Modifiers:** none identified. Given that identical variants in the *same family* produce different severity (and different etidronate responses — Tier B, ERS review), modifiers or stochastic/environmental factors clearly exist. Nobody has found them. → `KNOWLEDGE_GAP`.
- **Epigenetics:** no data. Not "no effect" — genuinely unstudied.
- **Chromosomal abnormalities:** PAM is not a CNV syndrome, but note **large deletions are 15% of the variant spectrum**, including Corut's deletion spanning *"the minimal promoter and the first exon."* This matters for diagnostics: a sequencing-only panel misses those. You need del/dup analysis.

---

## 5. Environmental Information

Short section, and the shortness is the finding.

- **Environmental factors:** none established as causal. Historical hypotheses (inhaled dust, mineral-rich water, milk) are dead.
- **Lifestyle:** dietary phosphate load is the only mechanistically motivated candidate; unproven in humans, protective-when-restricted in mice.
- **Infectious agents:** not causal. Relevant only as *complications* — recurrent respiratory infection in advanced disease; a 2026 pediatric case was complicated by *Haemophilus influenzae* pneumonia (PMID:41878462).
- **Occupational:** none. But watch the **misdiagnosis** direction — PAM gets called silicosis, miliary TB, or sarcoidosis. Mariotta 2004, verbatim: *"Pulmonary tuberculosis or sarcoidosis were misdiagnosed in 88 cases out of the 576."* That's 15% of a large series treated for the wrong disease. A 2026 Indian case (PMID:41694967) was *"started on anti-tubercular treatment on clinical grounds"* before anyone said PAM.

---

## 6. Mechanism / Pathophysiology

Here's the causal chain, and it's unusually clean — which makes PAM a genuinely nice dismech entry.

### The normal physiology being broken

Your alveoli are lined with surfactant — a phospholipid film that keeps the air sacs from collapsing on themselves, like the detergent that stops a soap bubble popping. Surfactant is constantly being made, used, chewed up, and recycled. When the phospholipids get broken down, they liberate free phosphate into the thin fluid layer coating the alveolus.

Something has to bail that phosphate out, or it accumulates. That bailer is **NaPi-IIb**, sitting on the apical (air-facing) membrane of the type II pneumocyte, using the sodium gradient as its power source to haul phosphate back into the cell.

> **Verbatim, Jönsson et al. 2023 full text (PMID:37259144):** "Normally, phosphate will be cleared from the alveolar space by transport via NaPi-2b located in the apical membrane of the alveolar type II cell. When the transporter does not work properly, this leads to an excess of phosphate in the alveolar lumen with subsequent precipitation of extracellular calcium."

### The causal chain, node by node

| # | Node | `biological_scale` | Key evidence |
|---|---|---|---|
| 1 | Biallelic loss-of-function SLC34A2 variant | MOLECULAR | PMID:16960801, PMID:17095743 |
| 2 | Absent or non-functional NaPi-IIb at the AT2 apical membrane | MOLECULAR | PMID:35443721 (both failure modes) |
| 3 | Failure of sodium-dependent phosphate reuptake from alveolar lining fluid | MOLECULAR | PMID:35443721, PMID:42520113 |
| 4 | Accumulation of phosphate liberated from surfactant phospholipid catabolism | CELLULAR | PMID:37259144 |
| 5 | Supersaturation of alveolar lining fluid → calcium phosphate nucleation | TISSUE | PMID:37259144 |
| 6 | **Microlith formation** — concentrically laminated hydroxyapatite concretions | TISSUE | PMID:33246992 |
| 7 | Macrophage-rich inflammation triggered by the stones themselves | TISSUE | PMID:26560359 |
| 8 | Alveolar phospholipidosis (surfactant accumulation) | CELLULAR/TISSUE | PMID:26560359 |
| 9 | Interstitial fibrosis + progressive restriction | TISSUE | PMID:26560359, PMID:22941890 |
| 10 | Pulmonary hypertension → cor pulmonale → respiratory failure | ORGANISM | PMID:22941890, PMID:8215680 |

**Node 7 is the one people miss, and it's causally important.** The mouse work proved the stones aren't inert gravel — they actively drive inflammation, and the inflammation *resolves when the stones are cleared*. That's a reversibility experiment, which is rare and valuable:

> **Verbatim, Saito et al. 2015 (PMID:26560359):** "Microliths introduced by adoptive transfer into the lungs of wild-type mice produce marked macrophage-rich inflammation and elevation of serum MCP-1 that peaks at 1 week and resolves at 1 month, concomitant with clearance of stones."

**Node 8 was a genuine surprise** and shouldn't be dropped — it closes a loop back to the surfactant biology:

> **Verbatim, Saito et al. 2015:** "We show that epithelial deletion of Npt2b in mice results in a progressive pulmonary process characterized by diffuse alveolar microlith accumulation, radiographic opacification, restrictive physiology, inflammation, fibrosis, and an unexpected alveolar phospholipidosis."

### Protein-level mechanism — new as of 2026

The transporter's structure was solved this year, which upgrades your "protein dysfunction" section from hand-waving to structural biology:

> **Verbatim, Zhu, Almakki & Diver 2026, *PNAS* (PMID:42520113):** "We present cryoelectron microscopy structures of SLC34A2 when the transporter is empty, bound to Na+ ions only, fully loaded with Na+ ions and Pi, and bound to an inhibitor phosphonoformic acid, revealing its distinct architecture, substrate and ion binding sites, the role of Na+, and multiple transporter states. Pi binds at a highly symmetric, membrane-embedded pocket positioned approximately mid-membrane and is coordinated by its signature four residue QSSS repeat motifs. Na+ shapes the Pi-binding pocket and drives the transition from the outward-open to occluded state. Integrated with functional analyses, these structures reveal that SLC34 transporters operate through an atypical alternating access cycle defined by coordinated elevator movements of an auxiliary gate domain."

The "elevator" mechanism is a nice image for the entry: the phosphate binding site physically rides up and down through the membrane, and sodium binding is what closes the doors. A variant like Thr468del presumably jams the elevator without removing it from the building — which is exactly what the oocyte data showed, five years before the structure explained it.

The same paper hands you the therapeutic angle and the cancer angle in one breath: *"SLC34A2 is also overexpressed in most ovarian and uterine tumors, making it an attractive target for antibody-drug conjugates."*

### Molecular-profiling data

- **Transcriptomics/proteomics/metabolomics of PAM lung:** essentially absent. No GEO series, no PRIDE dataset, no single-cell atlas of a PAM lung that I could find. This is a real and citable gap.
- **Biomarkers (mouse→human translated):** the one exception, and it's good work — see §10.
- **Functional genomics screens:** none.

### Suggested ontology terms — ALL require OAK verification 🔍

**GO (biological process / molecular function):**
- 🔍 sodium:phosphate symporter activity
- 🔍 phosphate ion transmembrane transport
- 🔍 surfactant homeostasis
- 🔍 biomineral tissue development / biomineralization
- 🔍 macrophage chemotaxis
- 🔍 extracellular matrix organization (for the fibrotic arm)

With `modifier:` — phosphate transport is `DECREASED` or, arguably, `LOSS_OF_FUNCTION`. Per your CLAUDE.md discriminator: this is a **variant-driven qualitative abolition** of a transport function, not a process merely running low. `LOSS_OF_FUNCTION` on the `MolecularFunctionDescriptor` is defensible here — Huqun's *"the mutations abolished the normal gene function"* is the qualitative claim you need. Put `functional_impact_category: LOSS_OF_FUNCTION` on the `GeneticContext` separately.

**CL (cell types):**
- 🔍 type II pneumocyte — the primary lesion cell
- 🔍 alveolar macrophage — the inflammatory responder
- 🔍 type I pneumocyte — collateral
- 🔍 fibroblast / myofibroblast — fibrotic arm

**CHEBI:**
- 🔍 hydroxyapatite, phosphate, calcium(2+), sodium(1+), etidronic acid, phosphonoformic acid (foscarnet — the structural inhibitor)

### Module conformance opportunities (dismech-specific)

1. **This is a textbook Xogenesis candidate.** Microlith formation is a pathological-structure-formation process with a discrete product. If you build a `microlith_formation` or broader `ectopic_calcification` module, PAM is the flagship conformer. Anchor with OGMS process + UBERON site per the current convention — and per your own standing decision, **skip MPATH** (the `create-module` skill is stale on this).
2. **`fibrotic_response`** — node 9 conforms; the AT2 injury → inflammation → mesenchymal activation → ECM chain is present.
3. **`pulmonary_vascular_remodeling`** — node 10; PAM is a bona fide secondary cause of PH (PMID:8215680 documents severe PH with RVEF 0.27 pre-transplant).
4. Possible cross-link to a phosphate-handling module if you ever build one — SLC34A2's siblings SLC34A1/A3 cause renal phosphate-wasting disease from the same transporter family (PMID:42520113 frames the whole family).

---

## 7. Anatomical Structures Affected

**Primary organ:** lung 🔍 `UBERON:0002048` — bilateral, diffuse, with **basilar and posterior predominance** on imaging.

**Primary site:** the alveolus 🔍 (verify the exact UBERON ID for pulmonary alveolus / alveolar sac / alveolar lumen — the microliths are specifically *intraluminal*, which is the whole distinction from metastatic pulmonary calcification, where calcium lands in the alveolar basement membranes instead. See PMID:41019964 for the contrasting entity.)

Kosciuk 2020 full text is precise about where they end up as disease advances: *"Variably sized concentrically laminated concretions are present both in alveolar spaces and in the interstitium with diameters ranging from 0.01 to 2.8 mm."* So: starts luminal, ends up in both compartments.

**Also involved:** pleura 🔍 (the "black pleural line" is a subpleural fat layer, plus subpleural cystic change / paraseptal emphysema); pulmonary vasculature (secondary PH); right heart (cor pulmonale).

**Extrapulmonary sites of calcification:** seminal vesicle, testis, epididymis, cardiac valves (aortic, tricuspid), gastric mucosa. All 🔍.

**Cell level:** alveolar type II epithelial cell (primary), alveolar macrophage, type I pneumocyte, interstitial fibroblast.

**Subcellular:** 🔍 apical **plasma membrane** of the AT2 cell is the critical GO cellular-component annotation — the whole disease is about a protein's address. Also lamellar body / surfactant-secretory machinery, given the phospholipidosis finding.

**Lateralization:** bilateral, diffuse, symmetric. Worth curating explicitly — asymmetry should make you doubt the diagnosis (though note PMID:41878462 reports a pediatric case with calcification concentrated in the left lower lobe, so "diffuse" isn't absolute at presentation).

---

## 8. Temporal Development

### Onset

Insidious, and the "onset" you're measuring depends entirely on what you're measuring — mineral deposition begins long before symptoms. Diagnosis clusters at **30–40 years** (Bendstrup 2020, verbatim: *"the majority of cases are diagnosed at the age of 30-40 years"*), but Jönsson 2012 gives the wider true range verbatim: *"The disease is usually discovered from birth up to 40 yrs of age and is often diagnosed incidentally during radiography of the chest for other reasons."*

Pediatric presentations do happen and can be severe — a 2026 *Pediatric Pulmonology* case report is titled "Early-Onset Pulmonary Alveolar Microlithiasis" (PMID:42261209), and a 3-year-old is reported in PMID:41878462. The ERS review notes children under 5 show *"more pronounced dry cough and respiratory failure"* (Tier B).

For dismech: `OnsetDescriptor` with a wide range, plus a note that radiographic onset precedes clinical onset by years-to-decades. Use the HPO onset annotations (✅ young adult 4/8, juvenile 3/8, childhood 1/8) but **without a fabricated frequency band**.

### Progression — four radiographic stages (Tier B, ERS review)

1. **Pre-calcific** — poorly calcified microliths, ground-glass only
2. **"Sandy"** — 2–4 mm calcified micronodules, cardiac borders still visible
3. **Progressive opacification** — heart and diaphragm borders obscured ("vanishing heart")
4. **Intense calcification** — near "white out"

That's a genuinely useful staging scaffold for a `progression:` block, and it's radiographic rather than histologic, which is how it's actually used.

### Rate and course

**Slow — decades.** ✅ `HP:0003677` Slowly progressive is an actual HPO annotation for this disease. But "slow" hides real variance, and the ERS review flags a spectacular outlier: *"Although PAM is typically progressive, there are many exceptions, including reported cases in which a patient diagnosed prior to the age of 10 years lived for >45 years."* (Tier B.)

- **Course pattern:** chronic, progressive, lifelong. Never episodic, never relapsing-remitting.
- **Remission:** does not occur spontaneously. No treatment reliably induces it.
- **Critical window:** unknown, and this is the therapeutically important gap. The mouse data show a low-phosphate diet **prevents** stones in young animals *and* reduces established burden — so there may be a treatable window in humans, but nobody knows where it opens or closes. Prime `proposed_experiments` material.

---

## 9. Inheritance and Population

### Epidemiology — handle with care

There is **no true prevalence or incidence study.** Everything is a literature census, which systematically undercounts an often-asymptomatic disease. Jönsson 2023 says so verbatim: *"It is likely that PAM is under-reported due to lack of recognition, misdiagnosis, and mild clinical presentation."*

| Source | Count | Period |
|---|---|---|
| Castellana & Lamorgese 2003 (PMID:14665786) | 424 cases | to end-2001 |
| Mariotta 2004 (PMID:15554073) | 576 cases | to 2004 |
| Castellana 2015 (PMID:26621975) | **1,022 cases**, from 544 papers | to Dec 2014 |
| Bendstrup 2020 (PMID:32964001) | "fewer than 1100 cases" | 2020 |
| Orphanet | "less than 1200 patients described in the literature" | current |

Reported incidence per million (Tier B, ERS review — **do not snippet this**): Turkey 1.85, Italy 1.08, Japan 0.92, USA 0.15.

**For your structured `prevalence:` block:** Orphanet's own class is the safest citable object. `prevalence_class: BELOW_1_IN_1000000` with `measure_type: CASES_IN_LITERATURE` is the honest encoding of "~1,000–1,200 cases ever reported worldwide." Please do **not** convert the per-million incidence figures into `rate_per_100000` and present them as prevalence — they're incidence estimates derived from case counts over undefined denominators, and they'd give the entry false precision.

### Geographic distribution

> **Verbatim, Castellana 2015:** "PAM is present in all continents and in many nations, in particular in Turkey, China, Japan, India, Italy and the USA. Familiality is frequent."

Continental split (Tier B, ERS review): **56.3% Asia, 27.8% Europe.** Mariotta 2004 (earlier, so Europe-weighted): *"most of them came from Europe (42.7%) and Asia (40.6%)"* across 51 countries.

New geography keeps appearing — a 2026 report describes *"the first case of PAM from Rajasthan, a desert state of India"* (PMID:41694967), and a 2023 case from Syria (PMID:37663718). That trickle is ascertainment, not incidence.

### Inheritance

**Autosomal recessive** ✅ `HP:0000007`, monogenic, with **full penetrance** asserted by Corut 2006 (verbatim above). Carrier frequency: not established; gnomAD-based estimates would be back-of-envelope only. Familiality in ~⅓ of patients (Mariotta 2004, verbatim: *"Family history for the disease was found in one-third of the patients"*).

**Expressivity: highly variable** — and note the tension worth curating explicitly. Penetrance is called complete; expressivity is wildly variable; the drivers of that variability are called "largely nongenetic" (Castellana 2015). Three curated claims that don't contradict each other but definitely need to sit in the same room. Good `discussions` material.

No anticipation (not a repeat disorder). No germline mosaicism reported. No classical founder mutations, but ancestry-clustered recurrent alleles (§4).

### Sex ratio — the sources disagree, so say so

- Bendstrup 2020, verbatim: *"There is no sex difference"*
- ERS review 2020 (Tier B): ~50% male, 41% female (rest unreported)
- Castellana & Lamorgese 2003, **verbatim**: *"a total of 424 cases have been reported worldwide, 269 of which were sporadic and showed a prevalence of the male sex and 155 of which were familial cases and prevalently affected the female sex."*

That last one is fascinating and almost certainly an **ascertainment artifact** — familial cases are found by family screening, sporadic cases are found when someone gets a chest film for another reason, and those two funnels have different sex biases. Curate the observation, flag the artifact hypothesis, don't assert a biological sex effect.

---

## 10. Diagnostics

### The diagnostic pathway, modern version

Bendstrup & Jönsson 2020 state the current standard verbatim, and it represents a real shift away from biopsy:

> **Verbatim (PMID:32964001):** "The diagnosis of PAM can confidently be based on typical radiographic findings and genetic testing proving rare biallelic SCL34A2 gene variants. Bronchoalveolar lavage and histopathology may show microliths."

Jönsson 2023 pushes further, verbatim: *"Genetic testing may in the future be the preferred tool for diagnostics instead of invasive methods."*

The older standard (still cited, and still what happens in resource-limited settings) is Castellana 2015, verbatim: *"The optimal diagnostic procedure is the association of chest high-resolution computed tomography (HRCT) with bronchoalveolar lavage, but a chest radiograph may suffice in families in which a case has already been diagnosed."*

### Imaging

**Chest radiograph:** the "sandstorm" — fine sand-like micronodules, basilar predominant, progressing to the "vanishing heart." Nearly pathognomonic in the right clinical context.

**HRCT** — three findings worth separate curation (Tier B, ERS review):
- Diffuse hyperdense micronodular airspace opacities
- **"Crazy-paving"** with *calcified* interlobular septa — the calcification is what separates it from alveolar proteinosis, which crazy-paves without minerals
- **"Black pleural line"** — a 1–2 mm subpleural fat-density band, visible precisely *because* everything around it is so dense
- Subpleural cysts / paraseptal emphysema

🔍 RadLex terms exist for several of these if you want imaging grounding.

### Histopathology

> **Verbatim, Kosciuk 2020 full text (Tier B):** "Variably sized concentrically laminated concretions are present both in alveolar spaces and in the interstitium with diameters ranging from 0.01 to 2.8 mm."

Composition: **hydroxyapatite**, calcium:phosphate ratio ~2–3:1. Von Kossa positive. SEM shows spherical bodies with porous surfaces. The classic term in pathology reports is **"calcospherites"** — used in current case reports: *"Histopathological analysis confirmed the diagnosis by demonstrating intra-alveolar calcospherites"* (PMID:41939679).

**Tissue acquisition:** transbronchial forceps biopsy, **transbronchial cryobiopsy** (first PAM diagnosis by cryobiopsy: PMID:32108613), or surgical lung biopsy. BAL can recover microliths without any biopsy at all — including in a 3-year-old, where BAL showed *"small clustered onion-like calcifications"* (PMID:41878462).

### Pulmonary function

Restrictive defect with reduced DLCO ✅ `HP:0002091`; normal early. Exercise desaturation precedes resting hypoxemia. Spirometry tracks radiographic stage. See also PMID:39735153, "Lung Function Decline in Pulmonary Alveolar Microlithiasis."

### Biomarkers — the mouse-to-human translation

This is the only real biomarker work in the disease, and it's genuinely nice — biomarkers discovered in the model, then **confirmed in patient serum**:

> **Verbatim, Saito et al. 2015 (PMID:26560359):** "Cytokine and surfactant protein elevations in the alveolar lavage and serum of PAM mice and confirmed in serum from PAM patients identify serum MCP-1 (monocyte chemotactic protein 1) and SP-D (surfactant protein D) as potential biomarkers."

For a `biochemical:` block: **serum SP-D** and **serum MCP-1**, both `INCREASED`. No LOINC-coded reference ranges exist for either in this context — do not invent interpretation bands.

Routine chemistry (serum calcium, phosphate, PTH, ALP, vitamin D) is characteristically **normal**. That's diagnostically load-bearing — it's how you exclude metastatic pulmonary calcification. A normal-labs statement is a real finding, not an absence.

### Genetic testing

- **Targeted SLC34A2 sequencing** — first line
- **Must include del/dup analysis** (15% of variants are large deletions, one of which removes the promoter and exon 1)
- **Gene panels:** SLC34A2 is on childhood-ILD and diffuse-lung-disease panels; the chILD-EU consortium reports 50.8% overall genetic yield in pediatric ILD (PMID:42194933)
- **WES/WGS** — appropriate when the phenotype is atypical; PAM turns up incidentally in broad pediatric rare-disease exome cohorts (PMID:41986647)
- Karyotype, CMA, FISH, mtDNA, repeat-expansion testing: **not applicable**

### Differential diagnosis (with the discriminator, which is what actually matters)

| Condition | What separates it |
|---|---|
| Pulmonary alveolar proteinosis | Crazy-paving **without** calcification; PAS-positive proteinaceous BAL, not stones |
| Miliary tuberculosis | Non-calcified nodules acutely; systemic illness. **88/576 misdiagnosed as TB or sarcoid** (PMID:15554073) |
| Sarcoidosis | Perilymphatic non-calcified nodules, lymphadenopathy, granulomas |
| Silicosis / pneumoconiosis | Occupational history; upper-lobe predominance; different nodule morphology |
| Metastatic pulmonary calcification | **Abnormal** calcium/phosphate metabolism (renal failure, hyperparathyroidism); calcium in alveolar *basement membranes*, not lumen (PMID:41019964) |
| Pulmonary amyloidosis | Congo red birefringence |
| Idiopathic pulmonary hemosiderosis | Iron, not calcium |

### Screening

- **Cascade family screening** — highest-yield intervention in the whole disease. A plain chest radiograph suffices in a family with a known case (Castellana 2015, verbatim above); genetic testing is cleaner now. PMID:32039063 argues for it: *"The family members of patients with PAM may also be kept on follow up with regular imaging."*
- **Newborn/population screening:** not performed, not recommended.
- **Prenatal / preimplantation:** available where the familial variant is known — Enemark 2021, verbatim: *"In families with a history of PAM, genetic counseling should be offered, as well as preimplantation/prenatal testing if necessary."*

---

## 11. Outcome / Prognosis

### Survival

The best available data is a Japanese long-term follow-up of **53 patients** (Tier B, via ERS review — track down the primary citation before curating):
- Respiratory insufficiency caused death in **34.1%** within 10–20 years of diagnosis
- A further **42.9%** of survivors died within 20–49 years
- **Mean age at death ~46.2 years**

Mariotta 2004, verbatim: *"The course of the disease was slow and patients usually died as a result of cardio-respiratory failure."*

Note the shape of that: this is a disease that mostly doesn't kill you for twenty years and then mostly does. And also sometimes doesn't — the >45-years-after-childhood-diagnosis survivor is in the same literature.

### Cause of death

Chronic respiratory failure and cor pulmonale. Jönsson 2012, verbatim: *"it progresses into pulmonary fibrosis, respiratory failure and cor pulmonale."*

### Complications

Progressive restriction · hypoxemic respiratory failure · pulmonary hypertension → cor pulmonale · pulmonary fibrosis · spontaneous pneumothorax (~1.6%, sometimes the *presenting* event — PMID:41939679) · recurrent respiratory infection · post-transplant complications including rejection (PMID:33884208).

**Pregnancy** is under-characterized and now has a dedicated review — PMID:41911679, "Pulmonary Alveolar Microlithiasis in Pregnancy." Restrictive lung disease plus the physiologic demands of pregnancy is a predictable collision; worth an entry note.

### Prognostic factors

- **Variant severity** — the only molecular predictor, and it's soft (PMID:31831582, n=14)
- **Age at diagnosis / symptom onset** — earlier symptomatic onset appears worse
- **Baseline PFT and rate of decline** (PMID:39735153)
- **Serum SP-D** — tracks lung injury in the mouse and is elevated in patients; **not validated as a prognostic marker in humans.** Say that plainly rather than implying it's clinical-grade.
- **Onset of PH** — inflection point toward transplant evaluation

### Recovery potential

Zero, without transplant. Microliths do not dissolve in vivo. The mouse data are the only demonstration anywhere that established burden can be reduced (EDTA lavage, low-phosphate diet) — and that has never translated.

---

## 12. Treatment

The blunt version, straight from the 2020 review, verbatim: **"there are no proven treatments for PAM."** (PMID:33246992)

### Lung transplantation — the only thing that works

> **Verbatim, Castellana 2015:** "At present lung transplantation is the only effective therapy."
> **Verbatim, Jönsson 2023:** "There is currently no cure for PAM, and the only effective treatment is lung transplantation."

Both single and bilateral procedures are performed. Tier B (ERS review): 18 reported cases, mean age at transplant ~46 years, outcomes from death to 74+ months survival, and — importantly — **no documented recurrence of microliths in grafts.** That absence is mechanistically meaningful: it says the defect is intrinsic to the lung epithelium, not a systemic mineral-handling problem raining calcium onto whatever lung you install. Curate that as a mechanistic inference, not just an outcome.

Earliest case, verbatim (PMID:8215680): *"We report about a 32-year-old man with pulmonary alveolar microlithiasis who underwent sequential bilateral lung transplantation. Preoperative hemodynamic studies revealed severe pulmonary hypertension; the right ventricular ejection fraction was 0.27. Eighteen months postoperatively, he continues to do well with normalized pulmonary and cardiac function and without clinical or histopathologic signs of graft rejection."*

Complications are real — familial PAM complicated by transplant rejection, PMID:33884208.

🔍 NCIT: lung transplantation (verify the specific term; `NCIT:C15289` Organ Transplantation is the safe generic). `therapeutic_modality: SURGERY`.

### Supportive care — what patients actually get

> **Verbatim, Enemark et al. 2021 (PMID:34970102):** "Patients with PAM should be offered preventative and symptomatic treatments such as vaccinations and oxygen therapy when needed. In some cases, lung transplantation may be required."

> **Verbatim, Mari et al. 2024 (PMID:39735153):** "PAM management is basically supportive using vaccines, antibiotics in recurrent infections, or long-term oxygen when respiratory failure is determined. A bilateral lung transplant may be a resolutive treatment for end-stage disease."

Components: long-term oxygen 🔍 (`therapeutic_modality: DEVICE`), influenza/pneumococcal/COVID vaccination 🔍 (`VACCINE`), antibiotics for infections 🔍 (`SMALL_MOLECULE`), pulmonary rehabilitation, genetic counseling 🔍 `NCIT:C15240` (`BEHAVIORAL`).

### Everything that's been tried and failed (all Tier B — ERS review full text)

| Intervention | Result |
|---|---|
| **Etidronate** (bisphosphonate) | Radiographic improvement in *some* pediatric cases over 12+ months; **variable response even among family members with identical mutations**; limited benefit in adults. Adverse effects: transient hypocalcemia, rickets, osteomalacia |
| **Systemic corticosteroids** | "Uniformly disappointing" |
| **Sodium thiosulfate** (IV, 9 months) | No improvement; possible *acceleration* |
| **Low-phosphate diet** (human) | Serum phosphate fell; disease progressed anyway |
| **Whole-lung lavage** | Recovered abundant microliths, no meaningful radiographic improvement — stones larger than the airway lumen simply won't come out |

The etidronate finding is the most interesting negative in the disease: **same variant, same family, different response.** That's a screaming signal for an unidentified modifier, and it's exactly the kind of thing a `KNOWLEDGE_GAP` discussion with `proposed_experiments` should capture.

🔍 CHEBI: etidronic acid; NCIT `C15986` Pharmacotherapy + `therapeutic_agent`. `therapeutic_modality: SMALL_MOLECULE`.

### What might work, from the mouse

> **Verbatim, Saito et al. 2015 (PMID:26560359):** "Microliths isolated by bronchoalveolar lavage readily dissolve in EDTA, and therapeutic whole-lung EDTA lavage reduces the burden of stones in the lungs. A low-phosphate diet prevents microlith formation in young animals and reduces lung injury on the basis of reduction in serum SP-D. The burden of pulmonary calcium deposits in established PAM is also diminished within 4 weeks by a low-phosphate diet challenge."

Three preclinical leads: **chelation lavage** (EDTA rather than saline — the difference between rinsing gravel and dissolving it), **phosphate restriction**, and by extension **phosphate binders**. None has a human trial.

### Clinical trials

I queried ClinicalTrials.gov v2 API directly: **zero interventional or observational studies with PAM as a listed condition.** The nearest relevant registration is **NCT02516800** (University of Aarhus, "Prevalence and Significance of Mutations in Genes Encoding NaPi-co-transporters in Development of CAVD," observational, n≈600, status *Unknown*) — same group as the Jönsson aortic-valve-sclerosis observation, testing the NaPi/valve-calcification link in a much larger population. Worth a `clinical_trials:` entry with `phase: NOT_APPLICABLE`, `status: UNKNOWN`, framed honestly as related-mechanism rather than PAM-specific.

### Pharmacogenomics, gene therapy, cell therapy, RNA therapeutics

None. **But** — worth flagging as a `KNOWLEDGE_GAP`, since PAM is an almost embarrassingly good theoretical target: monogenic, loss-of-function, single accessible cell type (AT2), inhalable organ, and a phenotype that the mouse says is *reversible* if you can clear the stones. The pieces are on the table and nobody has assembled them.

---

## 13. Prevention

**Primary prevention:** not possible for a germline recessive disease. The levers are reproductive — genetic counseling, carrier testing in consanguineous families with a known variant, and preimplantation/prenatal testing (Enemark 2021, verbatim above). Population-level consanguinity counseling in high-prevalence regions (Turkey, parts of the Middle East and South Asia) is the public-health-scale version.

**Secondary prevention:** cascade family screening — chest radiograph or, better, targeted variant testing in first-degree relatives of a proband. Cheap, high yield, actually recommended.

**Tertiary prevention:** vaccination, prompt treatment of respiratory infection, smoking avoidance (general, not PAM-specific), oxygen when indicated, early referral for transplant evaluation before PH is fixed. Serial PFT + imaging surveillance to catch the inflection.

**Immunization:** no PAM-specific vaccine; routine respiratory vaccination is explicitly recommended for these patients.

**Newborn/population screening:** not performed, not recommended, not on any ACMG or RUSP list.

**Prophylaxis:** none established. Phosphate restriction from an early age in a known-genotype child is a theoretically attractive, entirely untested intervention — and the human trial that exists was in *established* disease, which is a different question than prevention. That distinction is worth curating.

---

## 14. Other Species / Natural Disease

Thin section, honestly reported.

- **Naturally occurring PAM in animals:** no established OMIA entry for a spontaneous SLC34A2-associated microlithiasis phenocopy that I could confirm. Pulmonary calcification is described sporadically in veterinary pathology (usually secondary to renal disease or hypervitaminosis D — the metastatic-calcification mechanism, not this one). **Treat as "not established" rather than "absent."**
- **Orthologs:** mouse *Slc34a2* (NCBI Gene — 🔍 verify ID); rat and zebrafish orthologs exist. The SLC34 family is deeply conserved — Zhu 2026 frames it as a family-wide architecture, which implies the transport mechanism itself long predates mammals.
- **Comparative biology:** the mouse epithelial knockout recapitulates human disease remarkably well (§15), which is itself the strongest available statement about mechanism conservation.
- **Zoonotic potential / cross-species transmission:** not applicable — genetic disease.
- **NCBI Taxon:** `NCBITaxon:9606` (human), `NCBITaxon:10090` (mouse) 🔍 verify.

---

## 15. Model Organisms

### The flagship: conditional epithelial Npt2b-deleted mouse

Saito et al. 2015, *Science Translational Medicine* 7(313):313ra181, **PMID:26560359**, DOI 10.1126/scitranslmed.aac8577.

Full verbatim abstract (this one is worth quoting extensively because almost every mechanistic claim in the disease traces back to it):

> "Pulmonary alveolar microlithiasis (PAM) is a rare, autosomal recessive lung disorder associated with progressive accumulation of calcium phosphate microliths. Inactivating mutations in SLC34A2, which encodes the NPT2b sodium-dependent phosphate cotransporter, has been proposed as a cause of PAM. We show that epithelial deletion of Npt2b in mice results in a progressive pulmonary process characterized by diffuse alveolar microlith accumulation, radiographic opacification, restrictive physiology, inflammation, fibrosis, and an unexpected alveolar phospholipidosis. Cytokine and surfactant protein elevations in the alveolar lavage and serum of PAM mice and confirmed in serum from PAM patients identify serum MCP-1 (monocyte chemotactic protein 1) and SP-D (surfactant protein D) as potential biomarkers. Microliths introduced by adoptive transfer into the lungs of wild-type mice produce marked macrophage-rich inflammation and elevation of serum MCP-1 that peaks at 1 week and resolves at 1 month, concomitant with clearance of stones. Microliths isolated by bronchoalveolar lavage readily dissolve in EDTA, and therapeutic whole-lung EDTA lavage reduces the burden of stones in the lungs. A low-phosphate diet prevents microlith formation in young animals and reduces lung injury on the basis of reduction in serum SP-D. The burden of pulmonary calcium deposits in established PAM is also diminished within 4 weeks by a low-phosphate diet challenge. These data support a causative role for Npt2b in the pathogenesis of PAM and the use of the PAM mouse model as a preclinical platform for the development of biomarkers and therapeutic strategies."

### For your `animal_models:` block

```
Model type: conditional (epithelial-restricted) Npt2b/Slc34a2 deletion, Mus musculus
Publication: PMID:26560359
```

**`modeled_mechanisms` links to write** (all `evidence_source: MODEL_ORGANISM`):

| Target node | `relationship` | `fidelity` | Readouts |
|---|---|---|---|
| Microlith formation | RECAPITULATES | HIGH | microlith burden ↑ (`INCREASED`); radiographic opacification ↑ |
| Restrictive physiology | RECAPITULATES | HIGH | lung compliance / restriction |
| Macrophage inflammation | RECAPITULATES | HIGH | serum MCP-1 `INCREASED`, then `RESTORED` at 1 month post-clearance |
| Pulmonary fibrosis | RECAPITULATES | MODERATE | histology |
| Alveolar phospholipidosis | *(model-first finding)* | — | Curate carefully — this was found in the mouse and is **not** confirmed as a feature of human PAM lung. That's a `HUMAN_MODEL_MISMATCH` candidate, not a `RECAPITULATES` |
| Low-phosphate rescue | RESCUES | MODERATE | calcium deposit burden `DECREASED`; serum SP-D `DECREASED` |
| EDTA lavage rescue | RESCUES | MODERATE | stone burden `DECREASED` |

**Limitations to state explicitly:** conditional epithelial deletion is not the human germline-biallelic state (the human also loses intestinal NaPi-IIb); mouse lifespan compresses a decades-long human course into months; the phospholipidosis has no confirmed human counterpart; the two rescue interventions have **never** worked in a human (the low-phosphate diet trial failed).

### Other systems

**Xenopus laevis oocyte heterologous expression** — Jönsson 2022 (PMID:35443721). This is `experimental_models:` territory (a non-animal-disease expression system used as an assay), *not* `animal_models:`. It's the only variant-level functional platform in the field, and it's how you'd triage a novel VUS. Readouts: ³²Pi uptake, immunoblot (glycosylation state), immunohistochemical membrane localization.

**Global Npt2b knockout** — reported as embryonic lethal in the broader phosphate-transport literature, which is why the conditional was necessary. 🔍 **Verify the primary citation before curating this** — I'm reporting it as literature context, not as a checked claim.

**iPSC-derived AT2 cells, lung organoids, air-liquid interface models:** none published for PAM. Given how tractable AT2 organoids now are and how single-gene this disease is, that's a conspicuous hole — good `proposed_experiments` content.

**Databases:** MGI (*Slc34a2*), IMPC, Alliance of Genome Resources, IMSR for strain availability. 🔍 verify specific allele IDs.

---

## Curation notes for the dismech entry

A few things I'd flag before you write YAML:

1. **PAM is an unusually *clean* mechanistic entry** — a single gene, a single transporter, a single cell type, and a causal chain where every link has a citation. It'll score well on compliance and it's a genuinely good showcase entry. Take the time to get the pathophysiology graph right.

2. **Build the Xogenesis module.** Microlith formation is a textbook pathological-structure-formation process — discrete product, defined site, conserved logic that recurs in nephrolithiasis, cholelithiasis, gout tophi, and vascular calcification. You already have `nephrolithiasis_crystal_nucleation` and `cholelithiasis_biliary_supersaturation` doing the same shape in other organs. PAM is the pulmonary sibling, and the supersaturation→nucleation→growth→retention→injury chain is nearly identical. Skip MPATH per your standing decision.

3. **The Tier B numbers are a trap.** Incidence-per-million, the 53-patient Japanese cohort, the 18-transplant table, the 1.6% pneumothorax rate — all of it lives in the ERS review's *full text*. `just validate-disorders` runs `--no-full-text`. Either commit the full-text cache for PMID:33246992 or put those numbers in `notes:`.

4. **Watch the title-snippet trap on PMID:16960801.** "Mutations in SLC34A2 cause pulmonary alveolar microlithiasis and are possibly associated with testicular microlithiasis" is a title that *looks* like it states a result. It does — for the first clause. The second clause is 2/15 subjects with a synonymous and a noncoding variant. Quote the abstract sentence, tag `PARTIAL`, and let the explanation say what the data actually are.

5. **Curate the disagreements as disagreements.** Sex ratio (no difference vs. sporadic-male/familial-female), penetrance-complete-but-expressivity-wild, and the same-variant-different-etidronate-response finding are all genuine open questions with citable both-sides evidence. `discussions` with `kind: KNOWLEDGE_GAP` is the right home, not a smoothed-over prose sentence that picks a winner.

6. **`evidence_source` discipline:** Saito 2015 is `MODEL_ORGANISM` (with the human serum-biomarker confirmation arguably splitting into a second `HUMAN_CLINICAL` item — split them, one source per item). Jönsson 2022 is `IN_VITRO`. Zhu 2026 is `IN_VITRO` (structural/biochemical). Corut, Huqun, Castellana, Mariotta, all the case reports: `HUMAN_CLINICAL`.

---

## Reference index

| PMID | First author, year | Journal | Abstract verbatim available |
|---|---|---|---|
| 33246992 | Kosciuk 2020 | Eur Respir Rev | ✓ |
| 26621975 | Castellana 2015 | Eur Respir Rev | ✓ |
| 37259144 | Jönsson 2023 | Orphanet J Rare Dis | ✓ |
| 26560359 | Saito 2015 | Sci Transl Med | ✓ |
| 42520113 | Zhu 2026 | PNAS | ✓ |
| 35443721 | Jönsson 2022 | Human Genomics | ✓ (structured) |
| 31831582 | Jönsson 2020 | Eur Respir J | ✓ (structured) |
| 32964001 | Bendstrup 2020 | ERJ Open Res | ✓ |
| 34970102 | Enemark 2021 | Yale J Biol Med | ✓ |
| 22941890 | Jönsson 2012 | Eur Respir Rev | ✓ |
| 16960801 | Corut 2006 | Am J Hum Genet | ✓ |
| 17095743 | Huqun 2007 | Am J Respir Crit Care Med | ✓ (structured) |
| 15554073 | Mariotta 2004 | Sarcoidosis Vasc Diffuse Lung Dis | ✓ |
| 14665786 | Castellana 2003 | Respiration | ✓ |
| 8215680 | Stamatis 1993 | Ann Thorac Surg | ✓ |
| 9377936 | Edelman 1997 | Chest | partial |
| 22336687 | Jönsson 2012 | Am J Respir Crit Care Med | letter — no abstract |
| 39735153 | Mari 2024 | Cureus | partial |
| 41878462 | Zhou 2026 | Front Pediatr | partial |
| 41939679 | Oujaber 2026 | Cureus | partial |
| 41694967 | Dixit 2026 | Cureus | partial |
| 41911679 | Kale 2026 | Z Geburtshilfe Neonatol | pregnancy review |
| 42261209 | Branco 2026 | Pediatr Pulmonol | early-onset pediatric |
| 33884208 | Helmink 2021 | Case Rep Pathol | transplant rejection |
| 32528675 | Samrah 2020 | Ann Med Surg | tricuspid calcification |
| 38784230 | — 2024 | — | gastric mucosal calcification |
| 32108613 | Goel 2020 | Lung India | first cryobiopsy diagnosis |
| 41183425 | Cui 2025 | EBioMedicine | SLC34A2 in seminal vesicle |
| 42194933 | Rapp 2026 | J Clin Med | chILD-EU diagnostic yield |

---

**Sources:**
- [Kosciuk et al. 2020, Eur Respir Rev — PMC9488654](https://pmc.ncbi.nlm.nih.gov/articles/PMC9488654/)
- [Jönsson et al. 2023, Orphanet J Rare Dis — PMC10230741](https://pmc.ncbi.nlm.nih.gov/articles/PMC10230741/)
- [Jönsson et al. 2023 — Springer Nature](https://link.springer.com/article/10.1186/s13023-023-02712-7)
- [Saito et al. 2015, Sci Transl Med](https://www.science.org/doi/10.1126/scitranslmed.aac8577)
- [Corut et al. 2006, Am J Hum Genet — PubMed 16960801](https://pubmed.ncbi.nlm.nih.gov/16960801/)
- [Huqun et al. 2007, Am J Respir Crit Care Med — PubMed 17095743](https://pubmed.ncbi.nlm.nih.gov/17095743/)
- [Castellana et al. 2015, Eur Respir Rev — PubMed 26621975](https://pubmed.ncbi.nlm.nih.gov/26621975/)
- [OMIM #265100 — PULMONARY ALVEOLAR MICROLITHIASIS](https://www.omim.org/entry/265100)
- [Orphanet: Pulmonary alveolar microlithiasis (ORPHA:60025)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=60025)
- [GARD: Pulmonary alveolar microlithiasis](https://rarediseases.info.nih.gov/diseases/11894/pulmonary-alveolar-microlithiasis)
- [Zhu, Almakki & Diver 2026, PNAS — SLC34A2 cryo-EM structures](https://www.ncbi.nlm.nih.gov/pubmed/42520113)
- [Zhou et al. 2026, Front Pediatr — novel compound heterozygous SLC34A2](https://www.ncbi.nlm.nih.gov/pubmed/41878462)
- [QJM 2024 — novel compound heterozygous SLC34A2 mutation](https://academic.oup.com/qjmed/article/117/4/293/7468130)
- [MONDO:0009928 via EBI OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0009928)
- [HGNC: SLC34A2 (HGNC:11020)](https://rest.genenames.org/fetch/symbol/SLC34A2)
- [HPO annotations for OMIM:265100 (JAX ontology API)](https://ontology.jax.org/api/network/annotation/OMIM:265100)
- [ClinicalTrials.gov API v2 — microlithiasis query](https://clinicaltrials.gov/api/v2/studies?query.term=microlithiasis)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 3 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:41019964` (2 mentions) - Identifier did not resolve to a record
- `PMID:37663718` (1 mention) - Identifier did not resolve to a record
- `PMID:42194933` (1 mention) - Identifier did not resolve to a record