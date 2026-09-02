---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-09-01T08:15:16.920883'
end_time: '2026-09-01T08:31:51.063281'
duration_seconds: 994.14
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Secondary Hypertension
  mondo_id: ''
  category: Complex
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
  web_search_requests: 19
  num_turns: 42
  total_cost_usd: 4.822962
  session_id: e0ee6759-99da-423e-afaa-47e5cae93234
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 55
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Secondary Hypertension
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Secondary Hypertension** covering all of the
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

sup — did the digging. Here's the whole report. One framing note before you dive in: **"secondary hypertension" is not one disease, it's a bucket** — the way "anemia" is a bucket. I've written it as the template asks, but I flag the lump/split question explicitly at the end, because in dismech terms this smells more like a `GROUPING` than a `DISEASE`.

---

# Secondary Hypertension — Comprehensive Research Report

**Prepared:** 2026-09-01
**Target concept:** Secondary Hypertension
**MONDO:** `MONDO:0001200` (secondary hypertension) — resolved live against EBI OLS4
**Category:** Complex (multi-etiology; heterogeneous)

### How to read the citations in this report

Citations fall into three tiers, and they are **not** interchangeable for dismech evidence purposes:

| Tier | Meaning | Safe to use as an evidence `snippet:`? |
|---|---|---|
| **✔ VERIFIED** | Record pulled directly from NCBI E-utilities; PMID, title, authors, journal confirmed | Title/authorship yes. **Quoted text still needs `just fetch-reference PMID:x` re-verification** — quotes below came through a summarizing fetch layer and may be lightly paraphrased |
| **○ SOURCED** | Claim traced to a named journal/agency page but PMID not independently confirmed | No — resolve the PMID first |
| **△ UNVERIFIED ID** | Ontology CURIE offered as a *lead*, not confirmed against the ontology | **No.** Run `runoak` / `just validate-terms` first |

Two candidate PMIDs I tested came back as *entirely different papers* (17174708 → a Lancet paper on generalised anxiety disorder; 18445663 → a BMI/aldosterone correlation study). That is the exact "real-but-wrong identifier" failure mode. Everything marked ✔ below was checked one by one.

---

## 1. Disease Information

### 1.1 Overview

Secondary hypertension is arterial hypertension arising from an **identifiable, and frequently correctable, underlying cause** — as opposed to primary (essential) hypertension, where no single cause is demonstrable. The distinction is not academic bookkeeping: correcting the upstream lesion can cure the blood pressure elevation outright, or convert an unmanageable resistant hypertension into a treatable one. Think of it as the difference between a leaking pipe and a house built on a slope. Both give you a wet basement; only one is fixed by fixing the pipe.

The clinically operational definition has three parts:
1. Confirmed hypertension (office BP plus out-of-office confirmation — ABPM or home BP).
2. A demonstrable causal condition (endocrine, renal, vascular, neurogenic, pharmacologic, or monogenic).
3. Plausible temporal/mechanistic linkage, ideally with BP improvement on treating the cause.

### 1.2 Identifiers

| System | Identifier | Notes |
|---|---|---|
| MONDO | `MONDO:0001200` | secondary hypertension ✔ (resolved via OLS4 API) |
| MONDO (children) | `MONDO:0001646` benign secondary hypertension; `MONDO:0001785` malignant secondary hypertension ✔ | Both returned by the same OLS4 query |
| MONDO (related) | `MONDO:0006947` renovascular hypertension ✔ | A major sub-etiology with its own term |
| ICD-10-CM | **I15** — Secondary hypertension; I15.0 renovascular; I15.1 secondary to other renal disorders; I15.2 secondary to endocrine disorders; I15.8 other; I15.9 unspecified | ○ SOURCED — standard ICD-10-CM block; verify subcodes against the current release |
| ICD-11 | **BA01** Secondary hypertension (with BA01.0 renovascular hypertension and endocrine/renal-parenchymal children) | ○ SOURCED — **subcode structure not independently confirmed; verify against the ICD-11 browser before binding** |
| MeSH | No single dedicated descriptor for "secondary hypertension." Nearest: *Hypertension* (D006973), *Hypertension, Renal* (D006977), *Hypertension, Renovascular* (D006978) | △ — descriptor IDs from memory; verify in the MeSH browser |
| OMIM | Not applicable to the umbrella concept. Individual monogenic forms have OMIM entries (see §4) | — |
| Orphanet | No ORPHA code for the umbrella; individual causes coded (e.g. familial hyperaldosteronism, Liddle syndrome, pheochromocytoma) | — |

### 1.3 Synonyms

Secondary arterial hypertension · non-essential hypertension · secondary HTN · secondary high blood pressure · hypertension of known cause · (historically) "curable hypertension"

### 1.4 Nature of the evidence base

**Mixed, and the mix matters.** Prevalence estimates come from two very different kinds of study:

- **Systematic-screening cohorts** in referral hypertension centers (individual-patient level, protocol-driven) — these produce the *high* prevalence figures.
- **Population/registry/claims data** — these produce the *low* figures, because they only capture causes somebody bothered to look for.

The gap between them is the single most important epidemiological fact in this whole area, and I return to it in §9.

---

## 2. Etiology

### 2.1 Causal architecture

Secondary hypertension has no single etiology. It is a **convergence phenotype**: many distinct upstream lesions funnel into a shared final common pathway of raised systemic arterial pressure, in the same way that many separate injuries funnel into "fever." The upstream lesions sort into six families:

**A. Endocrine**
- **Primary aldosteronism (PA)** — by a wide margin the leading cause. Aldosterone-producing adenoma, bilateral idiopathic hyperaldosteronism, unilateral hyperplasia, aldosterone-producing micronodules, rare adrenocortical carcinoma, and familial forms FH-I through FH-IV.
- **Pheochromocytoma / paraganglioma (PPGL)** — catecholamine-secreting chromaffin tumors.
- **Cushing syndrome / disease** — cortisol excess (ACTH-dependent or independent).
- **Congenital adrenal hyperplasia**, specifically 11β-hydroxylase (CYP11B1) and 17α-hydroxylase (CYP17A1) deficiency — the two "hypertensive" CAH variants.
- **Thyroid dysfunction** — hyperthyroidism (systolic hypertension, wide pulse pressure) and hypothyroidism (diastolic hypertension, raised systemic vascular resistance).
- **Primary hyperparathyroidism** — hypertension in ~20% of patients ○ SOURCED.
- **Acromegaly** — growth hormone/IGF-1 excess with sodium retention.

**B. Renal**
- **Renal parenchymal disease** — chronic glomerulonephritis, diabetic nephropathy, polycystic kidney disease, reflux nephropathy, CAKUT, chronic interstitial nephritis. Dominant in children.
- **Renovascular disease** — atherosclerotic renal artery stenosis (older, diffuse atherosclerosis) and fibromuscular dysplasia (younger, female-predominant).
- Renin-secreting juxtaglomerular tumor (very rare), Page kidney (subcapsular hematoma compressing parenchyma).

**C. Vascular / mechanical**
- **Coarctation of the aorta** — including recoarctation after repair. Classically upper-limb hypertension with a radiofemoral delay.
- Large-vessel arteritis (Takayasu, giant cell) involving renal or aortic segments.
- Mid-aortic syndrome.

**D. Neurogenic / sleep**
- **Obstructive sleep apnea** — extremely common and frequently the reason a hypertension is "resistant."
- Raised intracranial pressure, brainstem compression (neurovascular conflict at the RVLM), autonomic dysreflexia after spinal cord injury, baroreflex failure.

**E. Drug- and toxin-induced** (the "iatrogenic and ingested" family — most directly relevant to a toxicology-flavored curation)
- NSAIDs (COX-2 mediated renal sodium retention)
- Combined oral contraceptives / estrogen-containing preparations
- Glucocorticoids and mineralocorticoids
- Calcineurin inhibitors (ciclosporin, tacrolimus)
- **VEGF/VEGFR pathway inhibitors** (bevacizumab, sunitinib, sorafenib, pazopanib) — near-class-effect hypertension
- Erythropoiesis-stimulating agents
- Sympathomimetics: decongestants, amphetamines, cocaine, MDMA
- SNRIs/venlafaxine, MAOI + tyramine
- Alcohol (dose-dependent), **liquorice / glycyrrhizic acid** (11β-HSD2 inhibition → acquired apparent mineralocorticoid excess)
- Herbal ephedra, yohimbine, high-dose caffeine

**F. Monogenic / Mendelian** — see §4.

### 2.2 Relative frequency of causes (the headline recent dataset)

**✔ VERIFIED — de Freminville JB, Gardini M, Cremer A, et al. "Prevalence and Risk Factors for Secondary Hypertension in Young Adults." *Hypertension*. 2024. PMID:39297209. DOI:10.1161/HYPERTENSIONAHA.124.22753**

Cross-sectional study of **2,090 hypertensive patients aged 18–40**:

| Finding | Value |
|---|---|
| Overall secondary hypertension | **29.6%** |
| Primary aldosteronism | 54.8% of secondary cases |
| Renovascular hypertension | 18.4% |
| Primary kidney disease | 12.9% |
| Drug-induced hypertension | 6.0% |
| Pheochromocytoma/paraganglioma | 5.9% |

Reported quotes (re-verify before use as snippets): *"29.6%"* had secondary hypertension; the authors concluded *"all patients with hypertension under 40 years of age should be screened for secondary causes."*

Two things in that dataset deserve emphasis for a knowledge base:
1. **BP severity did not stratify risk.** "Blood pressure levels below 160/100 mm Hg did not correlate with lower secondary hypertension rates." The common clinical heuristic — *screen only the severe ones* — fails here.
2. **Risk factors were counterintuitive**: female sex, low potassium, multiple antihypertensive medications, **absence** of a family history of hypertension, **normal** body weight, and diabetes. Normal weight and no family history raise suspicion because they remove the usual explanations for essential hypertension.

### 2.3 Risk factors

**Genetic risk factors**
- Monogenic causal variants (see §4) — full penetrance for the hypertension phenotype in most.
- Germline PPGL-susceptibility variants (SDHB, SDHD, SDHC, SDHA, SDHAF2, RET, VHL, NF1, MAX, TMEM127, FH) — **25–40% of all PPGL carry a pathogenic germline variant** ○ SOURCED.
- Familial hyperaldosteronism types I–IV.
- Polygenic background modulating expression of any of the above (shared with essential hypertension: NPPA/NPPB, UMOD, CYP17A1, ATP2B1 loci — GWAS Catalog).

**Environmental / acquired risk factors**
- **Age** — bimodal. High secondary fraction in the very young (renal/vascular) and in the elderly (atherosclerotic RAS, drug burden).
- **Obesity** — drives OSA, and independently raises aldosterone. Note the paradox: in the young-adult cohort, *normal* weight predicted secondary hypertension, because obesity offers a competing explanation.
- **Dietary sodium** — the permissive substrate for every mineralocorticoid-excess mechanism.
- **Alcohol** — dose-dependent pressor effect.
- **Smoking / atherosclerotic risk factors** — for atherosclerotic renovascular disease.
- **Female sex** — for fibromuscular dysplasia (30s–40s, normal renal function) ○ SOURCED, and in the young-adult secondary hypertension cohort ✔.
- **Occupational/environmental toxicants** — lead and cadmium exposure (nephrotoxic, chronic), noise and air pollution (sympathetic activation).
- **Pregnancy** — unmasks Geller syndrome (progesterone-activated MR); preeclampsia is a distinct entity but overlaps mechanistically.
- **Solid organ transplantation** — calcineurin inhibitors, hypertension in **32–81% of renal transplant recipients on ciclosporin, approaching ~100% in cardiac transplant recipients** ○ SOURCED.

**Protective factors**
- Genetic: loss-of-function variants in the *opposite* direction of the disease genes — e.g. ENaC loss-of-function (pseudohypoaldosteronism type 1), NCC loss-of-function (Gitelman), NKCC2/ROMK loss-of-function (Bartter). These lower blood pressure and are the natural mirror image of Liddle and Gordon syndromes. Heterozygous carriers of Bartter/Gitelman alleles show lower BP at population level ○ SOURCED (the classic Ji et al. 2008 *Nat Genet* observation — resolve the PMID before citing).
- Environmental: sodium restriction, potassium-rich diet, weight loss, CPAP adherence in OSA, alcohol reduction, avoidance of the pressor drug classes in §2.1E.

**Gene–environment interactions**
- **Salt × mineralocorticoid genotype** is the archetype: Liddle syndrome, GRA, AME, and Gordon syndrome are all *conditionally* hypertensive — the phenotype requires dietary sodium. Restrict sodium and the pressure falls, because the gain-of-function is in a sodium-reabsorption pathway with nothing to reabsorb.
- **Liquorice × HSD11B2 genotype**: heterozygous HSD11B2 carriers are disproportionately sensitive to glycyrrhizic acid — a pharmacologic phenocopy of a genetic disease. A clean two-hit gene–environment model.
- **VEGF inhibitor × baseline endothelial reserve**: pre-existing hypertension and endothelial dysfunction predict severity of VEGFi-induced hypertension ○ SOURCED.
- **Obesity × aldosterone**: adiposity independently raises aldosterone secretion, so obesity both mimics and aggravates PA ○ SOURCED (Rossi 2008, PMID:18445663 ✔ — BMI independently predicted plasma aldosterone concentration in primary hypertension, β=0.153, P<0.0001, though notably *not* in the PA group, and this did not degrade ARR diagnostic accuracy).

---

## 3. Phenotypes

**Important caveat on the HPO IDs below.** I am giving labels I am confident in and CURIEs at two confidence levels. Anything marked △ is a *lead* — do not bind it without `runoak -i sqlite:obo:hp info` confirmation. Per this project's own rules, a plausible-but-wrong CURIE is worse than no CURIE.

### 3.1 Core phenotype

| Phenotype | HPO | Frequency | Onset | Course |
|---|---|---|---|---|
| Hypertension | `HP:0000822` (confident) | 100% (definitional) | Any; bimodal | Persistent unless cause corrected |
| Resistant hypertension | △ label-only | High — enriched cause for screening | Adult | Persistent |
| Hypertensive emergency/malignant phase | △ (`MONDO:0001785` covers the disease-level concept) | Minority | Any | Acute, life-threatening |

### 3.2 Laboratory abnormalities (the diagnostic tells)

| Phenotype | HPO lead | Which cause it points at | Frequency |
|---|---|---|---|
| Hypokalemia | `HP:0002900` | PA, Cushing, Liddle, AME, CAH, liquorice | **Absent in most PA cases** — the 2025 AHA/ACC guideline explicitly de-links screening from potassium ○ |
| Hyperkalemia | `HP:0002153` | Gordon syndrome (PHA2) — the diagnostic inversion | Characteristic |
| Metabolic alkalosis | △ | PA, Liddle, AME, Cushing | Common with hypokalemia |
| Suppressed plasma renin | △ | All mineralocorticoid-excess states | Defining for PA |
| Elevated plasma aldosterone | △ (see also `HP:0000859` hyperaldosteronism, △) | PA, FH types | Defining for PA |
| Elevated plasma/urine metanephrines | △ | PPGL | High sensitivity |
| Hypercalcemia | △ | Primary hyperparathyroidism | ~definitional for that cause |
| Proteinuria | `HP:0000093` | Renal parenchymal disease; also a consequence | Common |
| Reduced eGFR / CKD | `HP:0012622` (chronic kidney disease, confident) | Renal parenchymal, ischemic nephropathy | Common |
| Hyperglycemia / diabetes | △ | Cushing, acromegaly, PPGL; also a risk marker ✔ (de Freminville) | Variable |

### 3.3 Symptoms and signs by cause

- **PA**: frequently *asymptomatic* apart from the hypertension. Muscle weakness (`HP:0001324`), cramps, polyuria (`HP:0000103`), polydipsia (`HP:0001959`), nocturia — all downstream of hypokalemia and impaired renal concentrating ability.
- **PPGL**: the classic triad — episodic **headache** (`HP:0002315`), **palpitations** (`HP:0001962`), **diaphoresis** (`HP:0000975` hyperhidrosis). Paroxysmal, episodic course; pallor, tremor, anxiety, orthostatic hypotension between spells. *"PPGL could produce catecholamines such as epinephrine, norepinephrine, and dopamine leading to clinical presentation of hypertension, headache, diaphoresis, palpitations"* ○ SOURCED. Roughly half have sustained rather than paroxysmal hypertension.
- **Cushing syndrome**: central obesity, moon facies, violaceous striae, proximal myopathy, easy bruising, glucose intolerance, osteoporosis. △ on all CURIEs.
- **OSA**: witnessed apneas (`HP:0002870` obstructive sleep apnea, confident), snoring, excessive daytime somnolence, **nocturnal hypertension and non-dipping BP** — this last one is the pathognomonic *pattern* rather than a symptom.
- **Coarctation**: upper-limb hypertension with diminished/delayed femoral pulses, interscapular murmur, claudication, rib notching on chest radiograph.
- **Renovascular**: abdominal bruit, flash pulmonary edema (Pickering syndrome, bilateral disease), acute kidney injury on starting an ACE inhibitor or ARB — a genuinely useful provocative sign.
- **Thyroid**: hyperthyroid — weight loss, heat intolerance, tremor, tachycardia, systolic hypertension, exophthalmos; hypothyroid — fatigue, weight gain, cold intolerance, diastolic hypertension ○ SOURCED.

### 3.4 Target-organ damage phenotypes (shared downstream)

Left ventricular hypertrophy (`HP:0001712`), heart failure (`HP:0001635`), atrial fibrillation (△), ischemic and hemorrhagic stroke (`HP:0002140` / △), hypertensive retinopathy (△), CKD progression (`HP:0012622`), aortic dissection/ectasia (△).

**These are disproportionately severe in secondary hypertension**, especially PA, and are *not* fully explained by the BP level itself — see §6.2 and §11.

### 3.5 Quality of life

- PA specifically: adrenalectomy *"greatly improves quality of life by resolving hypertension, hypokalemia, and associated symptoms"* ○ SOURCED. QoL improvement after surgical cure is a consistently reported outcome and one of the better arguments for aggressive case-finding.
- OSA: daytime somnolence, cognitive impairment, and accident risk carry QoL burden independent of the BP.
- Drug-induced: forces the oncology/transplant/rheumatology trade-off — dose-reduce the culprit or accept the BP.
- Instruments in use: SF-36, EQ-5D, RAND-36 in PA cohorts; ESS and FOSQ in OSA.

---

## 4. Genetic / Molecular Information

### 4.1 Monogenic (Mendelian) hypertension — the causal gene table

All gene symbols below are HGNC-approved. **I have deliberately not written HGNC numeric IDs** — those must come from an HGNC lookup, not from recall.

| Syndrome | Gene(s) | Inheritance | Molecular consequence | Biochemical signature |
|---|---|---|---|---|
| **Liddle syndrome** | *SCNN1B*, *SCNN1G* (rarely *SCNN1A*) | AD | Gain of function. Truncation of the C-terminal PY motif (exon 13) of the β/γ ENaC subunits, abolishing NEDD4-2–mediated ubiquitination and degradation → ENaC accumulates at the apical membrane ○ SOURCED | Low renin, **low** aldosterone, hypokalemic alkalosis |
| **Glucocorticoid-remediable aldosteronism / FH-I** | *CYP11B1*–*CYP11B2* chimera, chr8q24.3 | AD | Unequal crossover creates a chimeric gene: *CYP11B1* regulatory elements driving *CYP11B2* coding sequence → aldosterone synthesis under **ACTH** control instead of angiotensin II ○ SOURCED | Aldosterone suppressible by dexamethasone; hybrid steroids in urine |
| **Familial hyperaldosteronism II** | *CLCN2* | AD | Gain-of-function chloride channel variants depolarize zona glomerulosa cells | PA phenotype, not dexamethasone-suppressible |
| **Familial hyperaldosteronism III** | *KCNJ5* (germline) | AD | Loss of K⁺ selectivity in Kir3.4 → Na⁺ influx, depolarization, Ca²⁺ entry, constitutive CYP11B2 transcription | Severe early-onset PA, massive adrenal hyperplasia |
| **PASNA / FH-IV** | *CACNA1D*, *CACNA1H* | AD / de novo | Gain-of-function L- and T-type Ca²⁺ channel variants | PA ± seizures and neurologic abnormality (*CACNA1D*) |
| **Gordon syndrome / PHA2** | *WNK1*, *WNK4*, *KLHL3*, *CUL3* | AD (KLHL3 also AR) | Gain of function in the WNK–SPAK–NCC axis. KLHL3/CUL3 form the ubiquitin-ligase complex that degrades WNKs; losing it stabilizes WNK → NCC hyperactivity ○ SOURCED | **Hyperkalemia** with hypertension, metabolic acidosis, low renin, normal/low aldosterone; short stature, dental abnormalities, muscle weakness ○ |
| **Apparent mineralocorticoid excess (AME)** | *HSD11B2* | AR | Loss of 11β-HSD2 → cortisol not converted to cortisone → cortisol occupies MR ("Cushing's disease of the kidney") ○ SOURCED | Low renin, **low** aldosterone, high cortisol:cortisone ratio |
| **Geller syndrome** | *NR3C2* (MR), p.Ser810Leu | AD | Altered MR ligand specificity — **progesterone becomes an agonist**; spironolactone becomes an agonist too | Hypertension exacerbated in pregnancy; spironolactone paradoxically worsens it |
| **Hypertensive CAH** | *CYP11B1* (11β-OHase), *CYP17A1* (17α-OHase) | AR | Precursor steroids (DOC) accumulate and act as mineralocorticoids | Low renin, low aldosterone, ambiguous genitalia (11β) or absent puberty (17α) |
| **Hypertension with brachydactyly (Bilginturan)** | *PDE3A* | AD | Gain-of-function phosphodiesterase 3A variants | Hypertension + type E brachydactyly; neurovascular conflict at brainstem |
| **PPGL syndromes** | *SDHA/B/C/D/AF2*, *RET*, *VHL*, *NF1*, *MAX*, *TMEM127*, *FH* | AD (mostly) | Pseudohypoxic (cluster 1) or kinase-signaling (cluster 2) tumorigenesis | Catecholamine/metanephrine excess |

**PPGL germline frequency ○ SOURCED:** *"Pheochromocytoma and paragangliomas carry 25–40% pathogenic germline gene variants."* A 2023 cohort reported *RET* 38.3%, *VHL* 21.3%, *SDHB* and *NF1* 17% each; another analysis put total germline-plus-somatic explanation *"up to about 60%."* Germline *SDHB* and *VHL* variants were found **exclusively in patients under 30**, and bilateral disease **exclusively in VHL carriers** ○ — both directly actionable for a testing-strategy annotation.

### 4.2 Somatic variants — aldosterone-producing adenomas

This is one of the tidiest genotype–phenotype stories in endocrine oncology. **>90% of aldosterone-producing adenomas carry a somatic driver** ○ SOURCED, and every driver converges on the same cell-physiology endpoint: **depolarization of the zona glomerulosa cell → Ca²⁺ influx → constitutive CYP11B2 transcription → autonomous aldosterone**.

| Gene | Protein | Reported frequency | Mechanism |
|---|---|---|---|
| *KCNJ5* | Kir3.4 inward-rectifier K⁺ channel | 37.1%–61.5% depending on population ○ | Loss of K⁺ selectivity → Na⁺ leak → depolarization |
| *CACNA1D* | Ca_v1.3 L-type Ca²⁺ channel | ~10.3% ○ | Gain of function; direct Ca²⁺ entry |
| *ATP1A1* | Na⁺/K⁺-ATPase α1 | ~8.2% ○ | Loss of pump function → depolarization |
| *ATP2B3* | PMCA3 Ca²⁺-ATPase | ~3.1% ○ | Impaired Ca²⁺ extrusion |
| *CTNNB1* | β-catenin | ~2.1% ○ | Wnt pathway activation |
| *CLCN2*, *SLC30A1*, *CADM1* | — | Rare | Depolarizing / gap-junction mechanisms |

**Ancestry and sex structure the mutation spectrum:** *"Somatic CACNA1D gene mutations are particularly more prevalent in black males whereas KCNJ5 gene mutations are most frequently present in black females"* ○ SOURCED. *KCNJ5* dominance is much higher in East Asian cohorts (Taiwanese series: 59.5% ○).

**Clinical correlate ○ SOURCED:** *KCNJ5*-mutant APAs are associated with *"a worse baseline status and better recovery of left ventricular remodeling and diastolic function"* after treatment — worse going in, better coming out.

### 4.3 Modifier genes

- Renin–angiotensin polymorphisms (*AGT* M235T, *ACE* I/D) modulate severity of renovascular and salt-sensitive phenotypes.
- *HSD11B2* heterozygosity as a liquorice-sensitivity modifier.
- *CYP3A5* expressor status affects tacrolimus dosing and therefore calcineurin-inhibitor hypertension exposure — a pharmacogenomic modifier.
- Polygenic BP score adds to monogenic burden (relevant for FH-I penetrance variability).

### 4.4 Epigenetics

- Adrenal *CYP11B2* expression is regulated by promoter methylation; hypomethylation is reported in APA relative to adjacent cortex ○ SOURCED (verify specific PMID).
- Renal *HSD11B2* promoter methylation is a candidate mechanism for acquired salt sensitivity ○.
- Chronic intermittent hypoxia (OSA) induces persistent epigenetic changes in carotid body and adrenal medulla — the proposed substrate for "BP memory" after OSA treatment ○.
- This is the least mature area in the whole report. Treat it as a knowledge gap rather than a curatable mechanism.

### 4.5 Chromosomal abnormalities

- **Turner syndrome (45,X)** — coarctation, bicuspid aortic valve, and hypertension. A genuine chromosomal cause of secondary hypertension.
- The GRA chimeric gene is itself a structural rearrangement (unequal crossover at 8q24.3) detectable by long-range PCR / MLPA.
- Otherwise not a major etiologic category.

---

## 5. Environmental Information

### 5.1 Environmental and toxicant factors

| Exposure | Mechanism | Evidence tier |
|---|---|---|
| **Dietary sodium** | Substrate for every mineralocorticoid mechanism; volume expansion | Established |
| **Glycyrrhizic acid (liquorice)** | 11β-HSD2 inhibition → acquired AME. CHEBI: glycyrrhizic acid △ | Established |
| **Lead, cadmium** | Chronic nephrotoxicity → renal parenchymal hypertension; oxidative stress | ○ SOURCED (CTD) |
| **Arsenic** | Endothelial dysfunction, vascular injury | ○ |
| **Air pollution (PM2.5), noise** | Sympathetic activation, systemic inflammation | ○ |
| **Alcohol** | Dose-dependent sympathetic and cortisol effects | Established |

### 5.2 Drug-induced hypertension (mechanistic detail)

This family deserves its own mechanistic treatment because it is the one where dismech can model a *toxicologic* causal chain end-to-end.

- **NSAIDs** — *"The hypertensive effect of NSAIDs is dose dependent and probably involves inhibition of COX-2 in the kidneys, which reduces sodium excretion and increases intravascular volume."* Indomethacin, naproxen and piroxicam produce the largest rises ○ SOURCED.
- **Combined oral contraceptives** — historical literature reports new hypertension in ~5% of users; modern low-dose formulations (20–35 μg ethinyl estradiol) carry a smaller effect ○ SOURCED. Mechanism: hepatic angiotensinogen induction → RAAS activation.
- **VEGF/VEGFR inhibitors** — reduced NO and prostacyclin production, increased endothelin-1, capillary rarefaction, increased peripheral resistance. Often dose-limiting in oncology but *"typically resolves with discontinuation of the provoking agent"* ○ SOURCED. Bevacizumab was the first agent (approved 2004); the small-molecule TKIs sorafenib, sunitinib, pazopanib followed ○.
- **Calcineurin inhibitors** — *"related to interference with the balance of vasoactive substances, including endothelin and nitric oxide"*, plus direct NCC activation via the WNK–SPAK pathway (mechanistically a *pharmacologic Gordon syndrome*, which is a lovely piece of convergence). Incidence 32–81% in renal transplant, ~100% in cardiac transplant recipients ○ SOURCED.
- **Glucocorticoids** — MR occupancy at high dose plus GR-mediated ENaC activation. Notably, a mouse model of Cushing syndrome showed **both** MR *and* GR stimulate ENaC activity ○ SOURCED — so the mechanism is not purely MR spillover.
- **Sympathomimetics** — direct α-adrenergic vasoconstriction (cocaine, amphetamines, decongestants, MAOI–tyramine interaction).
- **Erythropoiesis-stimulating agents** — increased viscosity, endothelin release, reversal of hypoxic vasodilation.

### 5.3 Infectious agents

Not a primary cause, but relevant paths exist:
- Post-streptococcal glomerulonephritis (*Streptococcus pyogenes*, NCBITaxon:1314 △) → acute nephritic hypertension.
- HIV-associated nephropathy (NCBITaxon:11676 △) → renal parenchymal hypertension.
- Hepatitis B–associated polyarteritis nodosa → renovascular hypertension.
- Chronic pyelonephritis with reflux nephropathy → parenchymal scarring → hypertension.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chains — ordered, one step per line

Secondary hypertension is genuinely **branched**, so here are six chains rather than one. Each terminates in the shared node *Elevated Systemic Arterial Pressure*. `→` reads as "leads to". I mark inference where the step is extrapolated rather than directly demonstrated in humans.

---

**CHAIN A — Autonomous mineralocorticoid excess (primary aldosteronism)**

1. Somatic gain-of-function variant in *KCNJ5*, *CACNA1D*, *ATP1A1*, *ATP2B3* (or germline FH variant) arises in an adrenal zona glomerulosa cell → **loss of the resting hyperpolarized membrane potential**.
2. Membrane depolarization → **opening of voltage-gated Ca²⁺ channels** → sustained rise in intracellular Ca²⁺.
3. Sustained intracellular Ca²⁺ → **constitutive transcription of *CYP11B2* (aldosterone synthase)**, uncoupled from angiotensin II and potassium.
4. Constitutive CYP11B2 activity → **renin-independent aldosterone overproduction**. *(This is the defining lesion; Brown 2020 ✔ showed it exists as a continuum rather than a threshold.)*
5. Aldosterone → **binds the mineralocorticoid receptor (NR3C2)** in the distal nephron principal cell.
6. MR activation → **transcriptional induction of SGK1** → SGK1 **phosphorylates NEDD4-2** → NEDD4-2 can no longer ubiquitinate ENaC ○ SOURCED.
7. Reduced ENaC turnover → **increased ENaC surface density and open probability** → increased apical Na⁺ entry.
8. Increased Na⁺ reabsorption → **plasma volume expansion** and, via the lumen-negative potential, **K⁺ and H⁺ secretion** → hypokalemia and metabolic alkalosis.
9. Volume expansion → **elevated systemic arterial pressure**, with reciprocal **renin suppression** (the biochemical fingerprint).
10. *In parallel* (not downstream of volume): MR activation in **endothelium, vascular smooth muscle, cardiomyocytes, fibroblasts and macrophages** → Nox1/p66Shc-mediated oxidative stress, pro-inflammatory and pro-fibrotic signaling ○ SOURCED → **vascular stiffening, cardiac and renal fibrosis**.
11. Step 10 → **target-organ damage disproportionate to the BP level** — the explanation for the excess cardiovascular risk in §11. Endothelial MR activation also raises endothelial sodium channel (EnNaC) activity, *"an important mechanism by which cardiovascular stiffness is promoted by excess aldosterone"* ○.

*Branch point at step 4:* unilateral (adenoma/APN — surgically curable) vs bilateral (idiopathic hyperaldosteronism — medically managed). This branch is the entire reason adrenal vein sampling exists.

---

**CHAIN B — Renovascular hypertension (2-kidney-1-clip physiology)**

1. Atherosclerotic plaque or fibromuscular dysplastic web narrows a renal artery → **reduced perfusion pressure at the afferent arteriole**.
2. Reduced afferent pressure sensed by the **juxtaglomerular apparatus** → **renin release** from JG cells.
3. Renin cleaves angiotensinogen → **angiotensin I** → ACE (pulmonary and endothelial) → **angiotensin II**.
4. Angiotensin II → **AT1 receptor–mediated arteriolar vasoconstriction** → raised systemic vascular resistance.
5. Angiotensin II → **adrenal aldosterone release** → Chain A steps 5–9 (sodium retention).
6. Angiotensin II → **central sympathetic activation and thirst**, plus vasopressin release.
7. Steps 4–6 → **elevated systemic arterial pressure**.
8. *Critical branch:* with **one** stenosed kidney, the contralateral kidney pressure-natriureses, so renin stays high and the hypertension remains **renin-dependent** — this is the state where revascularization works. With **bilateral** stenosis or a solitary kidney, sodium retention takes over, renin normalizes, and the hypertension becomes **volume-dependent** ○ SOURCED (directly demonstrated in the 2K1C vs 1K1C animal models, §15).
9. Chronic ischemia → **tubulointerstitial fibrosis and atrophy → ischemic nephropathy** → irreversibility. This is why late revascularization fails, and a plausible explanation for the negative CORAL/ASTRAL trial results.

---

**CHAIN C — Glucocorticoid-mediated (Cushing syndrome; and its genetic phenocopy, AME)**

1. Cortisol excess (pituitary ACTH adenoma, adrenal adenoma, ectopic ACTH, exogenous steroid) → **plasma cortisol far above normal**.
2. Cortisol binds MR with **affinity equal to aldosterone** ○ SOURCED; normally 11β-HSD2 protects the receptor by converting cortisol → inactive cortisone.
3. Severe cortisol excess → **saturation of renal 11β-HSD2** → *"a functional mineralocorticoid excess, due to the binding and activation of the mineralocorticoid receptor by excessive glucocorticoids"* ○ SOURCED.
4. MR occupancy by cortisol → Chain A steps 6–9 → **sodium retention, hypokalemia, volume expansion, hypertension**.
5. *Parallel GR-mediated arm:* glucocorticoid receptor signaling **also** stimulates ENaC ○ SOURCED, plus increased hepatic angiotensinogen, enhanced vascular α-adrenergic reactivity, and suppressed NO and prostacyclin.
6. **Genetic phenocopy:** *HSD11B2* loss-of-function reaches the identical step-3 state at **normal** cortisol levels — *"'Cushing's disease of the kidney' results in cortisol-mediated mineralocorticoid excess"* ○ SOURCED. **Pharmacologic phenocopy:** glycyrrhizic acid inhibits the same enzyme.

---

**CHAIN D — Catecholamine excess (PPGL)**

1. Germline or somatic driver (*SDHx*, *VHL*, *RET*, *NF1*, *MAX*, *TMEM127*) in a chromaffin progenitor → **pseudohypoxic (cluster 1) or kinase-driven (cluster 2) tumorigenesis**.
2. Clonal expansion of chromaffin cells → **catecholamine-synthesizing tumor mass** in adrenal medulla or extra-adrenal paraganglia.
3. Unregulated **epinephrine, norepinephrine and/or dopamine** synthesis and release ○ SOURCED — critically, release is *not* under normal neural control.
4. Norepinephrine → **α1-adrenergic vasoconstriction** → raised systemic vascular resistance; epinephrine → **β1-mediated increases in heart rate and contractility** → raised cardiac output.
5. Steps 4 → **paroxysmal or sustained elevated arterial pressure** with headache, palpitations, diaphoresis ○.
6. Chronic catecholamine exposure → **downregulation of adrenergic receptors and reduced plasma volume** → the orthostatic hypotension between paroxysms, and the profound hypotension on tumor devascularization if the patient has not been α-blocked and volume-repleted first. *(This step is the mechanistic basis of the preoperative α-blockade requirement.)*
7. Chronic catecholamine exposure → **catecholamine cardiomyopathy, takotsubo-like injury, myocardial fibrosis**.

---

**CHAIN E — Obstructive sleep apnea**

1. Upper airway collapsibility (anatomic and non-anatomic traits) → **repetitive apnea/hypopnea during sleep**.
2. Apnea → **intermittent hypoxia and hypercapnia**, plus repeated **arousals and sleep fragmentation**.
3. Chemoreceptor stimulation by intermittent hypoxia + arousal → **sympathetic overactivity** — *"Sympathetic activity due to intermittent hypoxia and/or fragmented sleep is the most important mechanisms triggering the elevation in blood pressure in OSA"* ✔ VERIFIED (Shiina 2024, PMID:39210083).
4. Sympathetic outflow → **renal vasoconstriction and altered sodium handling** → **RAAS activation** (a sympathetic–RAAS reinforcing loop) ○ SOURCED.
5. RAAS activation → aldosterone → Chain A steps 5–9 → **fluid retention**.
6. Fluid retention → **nocturnal rostral fluid shift** → increased peri-pharyngeal tissue pressure → **worse airway collapsibility** → back to step 1. *A closed positive-feedback loop* — this is why MRAs reduce both BP **and** the apnea–hypopnea index in this population ○ SOURCED.
7. Steps 3–5 → **nocturnal hypertension, non-dipping/reverse-dipping BP pattern, exaggerated BP variability, vascular remodeling, resistant hypertension** ✔.
8. Negative intrathoracic pressure swings against a closed airway → **increased LV transmural pressure and afterload** → an additional, purely mechanical contribution.

---

**CHAIN F — Drug/toxin-induced (the VEGF-inhibitor exemplar)**

1. Administration of a VEGF-A antibody or VEGFR tyrosine-kinase inhibitor → **blockade of VEGFR2 signaling in vascular endothelium**.
2. Loss of VEGFR2 signaling → **reduced eNOS activation → reduced nitric oxide bioavailability**, and reduced prostacyclin.
3. Reduced NO → **loss of tonic vasodilation** → increased arteriolar tone; concurrently **increased endothelin-1** production.
4. Sustained VEGF blockade → **capillary rarefaction** (loss of microvascular density) → structurally increased peripheral resistance *(inferred from preclinical models; human histologic confirmation is limited)*.
5. Steps 3–4 → **increased systemic vascular resistance → elevated arterial pressure**, typically within days to weeks of the first dose.
6. Drug withdrawal → **reversal** in most cases ○ SOURCED — the reversibility is what makes this a clean causal demonstration.

*Parallel toxicologic chains:* NSAID → COX-2 inhibition → reduced renal prostaglandin → reduced natriuresis → volume expansion. Calcineurin inhibitor → endothelin↑ / NO↓ **plus** WNK–SPAK–NCC activation → sodium retention. Both converge on the same terminal node.

### 6.2 Cross-cutting mechanistic themes

- **Convergence on ENaC and NCC.** Liddle (ENaC directly), PA (ENaC via SGK1/NEDD4-2), AME and Cushing (ENaC via unprotected MR), Gordon and calcineurin inhibitors (NCC via WNK–SPAK). Five etiologies, two transporters. This is the strongest argument that a **`mineralocorticoid_excess_sodium_retention`-type mechanism module** would earn its keep in dismech.
- **Aldosterone is not just a volume hormone.** The MR is expressed in endothelium, VSMC, cardiomyocytes, fibroblasts and myeloid cells. *"Deletion of endothelial cell MRs prevents the development of vascular and cardiac fibrosis and stiffness"* ○ SOURCED. Aldosterone induces damage via *"MR-Nox1-p66Shc-mediated processes that modulate pro-fibrotic and pro-inflammatory signaling pathways"* ○. This decoupling of *pressure* from *injury* is the mechanistic core of §11.
- **Immune involvement.** Myeloid-cell corticosteroid receptor signaling contributes to salt-sensitive hypertension; a 2024 preprint argues the effect runs through **glucocorticoid**, not mineralocorticoid, receptors in myeloid cells via cortisol ○ SOURCED (preprint — treat as a hypothesis, not established).
- **Oxidative stress and NO deficiency** are the shared tissue-injury currency: Nox1/Nox4-derived ROS in MR signaling, eNOS uncoupling in VEGFi and calcineurin-inhibitor hypertension, carotid-body ROS in intermittent hypoxia.

### 6.3 Ontology term leads

**GO biological process (all △ — verify with `runoak -i sqlite:obo:go`):**
`GO:0008217` regulation of blood pressure · `GO:0003073` regulation of systemic arterial blood pressure · `GO:0002018` renin-angiotensin regulation of aldosterone production · `GO:0032342` aldosterone biosynthetic process · `GO:0035813` regulation of renal sodium excretion · `GO:0006814` sodium ion transport · `GO:0048010` vascular endothelial growth factor receptor signaling pathway · `GO:0006809` nitric oxide biosynthetic process · `GO:0042311` vasodilation · `GO:0042310` vasoconstriction

**Cell Ontology (all △):**
juxtaglomerular cell · kidney distal convoluted tubule epithelial cell · kidney collecting duct principal cell · adrenal zona glomerulosa cell · chromaffin cell (`CL:0000166` — reasonably confident, still verify) · endothelial cell (`CL:0000115`) · vascular smooth muscle cell · myofibroblast · macrophage

**UBERON (all △):**
kidney (`UBERON:0002113`) · adrenal gland (`UBERON:0002369`) · adrenal cortex · adrenal medulla · renal artery · aorta · heart (`UBERON:0000948`) · retina · upper respiratory tract / pharynx

### 6.4 Molecular profiling

- **Transcriptomics:** APA transcriptomes cluster by driver genotype; *KCNJ5*-mutant tumors show a zona-fasciculata-like expression signature, wild-type/*CACNA1D* tumors a glomerulosa-like one. GEO holds multiple adrenal PA series — run `just discover-datasets` rather than trusting a recalled accession.
- **Proteomics/metabolomics:** steroid-profiling by LC-MS/MS is the most clinically mature "omics" here — 18-oxocortisol and 18-hydroxycortisol distinguish *KCNJ5*-mutant APA and GRA from other PA subtypes ○ SOURCED.
- **Spatial / single-cell:** CYP11B2 immunohistochemistry is effectively a low-plex spatial assay and has **rewritten PA pathology** (see §10.3). Single-cell adrenal atlases exist in the Human Cell Atlas.
- **Functional genomics:** no large disease-specific CRISPR screen; adrenal cell line (H295R) work dominates.

---

## 7. Anatomical Structures Affected

**Primary (cause-bearing) sites — vary by etiology:**
- **Adrenal cortex**, zona glomerulosa — PA, CAH △
- **Adrenal medulla** and extra-adrenal **paraganglia** (organ of Zuckerkandl, carotid body, head-and-neck paraganglia) — PPGL △
- **Pituitary gland**, corticotroph — Cushing disease △
- **Kidney**: renal artery (renovascular), glomerulus and tubulointerstitium (parenchymal), distal convoluted tubule and collecting duct (monogenic tubulopathies) △
- **Aorta**, juxtaductal isthmus — coarctation △
- **Upper airway**, pharynx — OSA △
- **Thyroid**, **parathyroid** — endocrine causes △

**Secondary (target-organ) sites — shared:**
- **Heart** — LV hypertrophy, diastolic dysfunction, heart failure, atrial remodeling and fibrillation
- **Brain** — ischemic and hemorrhagic stroke, cerebral small-vessel disease, hypertensive encephalopathy
- **Kidney** — hypertensive nephrosclerosis, albuminuria, CKD progression (kidney is both cause and casualty here, which makes the causal graph genuinely cyclic)
- **Retina** — hypertensive retinopathy, arteriovenous nicking, hemorrhages, papilledema in malignant phase
- **Large arteries** — stiffening, aneurysm, aortic dissection

**Body systems:** cardiovascular, renal/urinary, endocrine, nervous (autonomic and central), respiratory (OSA).

**Tissue and cell level:** vascular endothelium; vascular smooth muscle; renal tubular epithelium (distal convoluted tubule, connecting tubule, cortical collecting duct principal cells); adrenocortical zona glomerulosa cells; adrenal chromaffin cells; cardiac myocytes and fibroblasts; infiltrating macrophages and T cells.

**Subcellular:** apical plasma membrane (ENaC, NCC) △ `GO:0016324` apical plasma membrane; nucleus (MR/GR nuclear receptor translocation) `GO:0005634`; mitochondrial inner membrane (CYP11B2 is a mitochondrial P450) `GO:0005743`; smooth ER (steroidogenesis); secretory/chromaffin granules (catecholamine storage).

**Lateralization** — genuinely important here, unusually so:
- PA: **unilateral vs bilateral** is *the* treatment-determining question (surgery vs lifelong MRA), resolved by adrenal vein sampling.
- Renal artery stenosis: unilateral (renin-dependent, revascularization-responsive) vs bilateral (volume-dependent).
- PPGL: bilateral disease seen *"exclusively in VHL carriers"* in one series ○ — a lateralization finding with direct genetic-testing implications.

---

## 8. Temporal Development

**Onset**
- **Bimodal across the lifespan.** In children <12, secondary causes account for **70–85%** of all hypertension ○ SOURCED, overwhelmingly renal parenchymal. In young adults 18–40, **29.6%** ✔. In middle age the secondary fraction is lowest. In the elderly it rises again with atherosclerotic RAS and polypharmacy.
- Onset pattern by cause: **acute** (acute glomerulonephritis, drug initiation, PPGL crisis), **subacute/insidious** (PA, Cushing, OSA), **congenital** (coarctation, CAKUT, monogenic).
- **Red-flag onset patterns**: hypertension before age 30 without family history or obesity; abrupt onset after age 55; sudden loss of control in previously stable hypertension; hypertensive emergency.

**Progression and staging**
No formal staging system for the umbrella concept. Practically, three stages track reversibility:

1. **Reversible / functional** — the mechanism is active but tissue is intact. Full cure possible on correcting the cause.
2. **Partially reversible** — vascular remodeling, LVH and nephrosclerosis established. BP improves but does not normalize; drug burden falls.
3. **Irreversible / autonomous** — ischemic nephropathy, fixed nephrosclerosis, established target-organ damage. The hypertension has become self-sustaining and behaves like essential hypertension.

**This staircase is the single most consequential temporal fact in the disease.** Duration of hypertension before correction is the strongest predictor of cure after adrenalectomy or revascularization. **Critical intervention window: early.**

**Course patterns**
- **Sustained**: PA, renal parenchymal, coarctation, monogenic.
- **Paroxysmal/episodic**: PPGL (spells lasting minutes to an hour), also episodic on a sustained background in ~50%.
- **Nocturnal-predominant / non-dipping**: OSA, CKD, primary aldosteronism ✔ (Shiina 2024 lists nocturnal hypertension and abnormal BP variability as OSA-hypertension features).
- **Cyclic**: cyclic Cushing syndrome — rare, and a notorious cause of missed diagnosis.
- **Pregnancy-triggered**: Geller syndrome.

**Remission**
- **Treatment-induced** is the norm and is the point of the whole enterprise: adrenalectomy for unilateral PA, tumor resection for PPGL, transsphenoidal surgery for Cushing disease, angioplasty for FMD, coarctation repair, culprit-drug withdrawal.
- **Spontaneous remission is essentially unheard of**, with the narrow exception of self-limited drug or toxin exposures.

---

## 9. Inheritance and Population

### 9.1 Epidemiology — and the estimate you choose determines your answer

Global hypertension baseline: **~1.28 billion adults aged 30–79** have hypertension; **46% are unaware**, 42% are diagnosed and treated, and only **21% are controlled** ○ SOURCED (WHO Global Report on Hypertension, September 2023).

Secondary hypertension as a fraction of that:

| Setting / method | Secondary fraction | Source |
|---|---|---|
| Classical textbook estimate, unselected adults | **5–10%** | ○ SOURCED (long-standing consensus) |
| Young adults 18–40, systematic screening | **29.6%** | ✔ PMID:39297209 |
| Children <12 | **70–85%** | ○ SOURCED |
| Resistant hypertension (PA alone) | up to **20%** | ○ SOURCED (2025 AHA/ACC context) |

**Primary aldosteronism specifically** — where the numbers have moved most:

- **PAPY study ✔** (Rossi GP et al., *J Am Coll Cardiol* 2006, PMID:17161262): 1,125 newly diagnosed hypertensives; *"the prevalence of APA is high (4.8%)"* with idiopathic hyperaldosteronism in a further 6.4% — roughly **11%** total. Also concluded *"the availability of AVS is essential for an accurate identification of the adrenocortical pathologies underlying PA."*
- **Brown JM, Siddiqui M, Calhoun DA, Carey RM, Hopkins PN, Williams GH, Vaidya A. "The Unrecognized Prevalence of Primary Aldosteronism: A Cross-sectional Study." *Ann Intern Med* 2020. PMID:32449886 ✔** — 1,015 participants across four academic centers. Biochemically overt PA prevalence: **11.3% in normotensive individuals**, **15.7% stage 1**, **21.6% stage 2**, **22.0% resistant hypertension**. The authors describe *"a continuum of renin-independent aldosterone production"* and conclude *"The prevalence of primary aldosteronism is high and largely unrecognized."*

That normotensive figure is the striking one. It reframes PA from a discrete rare tumor syndrome into a **graded, continuous trait** that begins before hypertension does — a paradigm shift with obvious implications for how the concept should be modeled.

**The screening gap ○ SOURCED:** PA accounts for ~5–10% of all hypertension and up to 20% of resistant hypertension, *"yet screening rates among eligible patients remain below 2%."* Under 2%. That is not a diagnostic problem, it's a behavioral one.

**Other causes:**
- Symptomatic **renal artery FMD**: prevalence ~**4/1000**, accounting for **<10% of renovascular hypertension** ○ SOURCED; atherosclerosis is the leading RAS cause and FMD is second.
- **OSA**: highly prevalent (roughly 1 billion adults worldwide with some degree, ~425 million moderate-to-severe ○), and hugely enriched in resistant hypertension.
- **PPGL**: ~0.2–0.6% of hypertensive patients ○.
- **Cushing syndrome**: incidence ~0.7–2.4 per million per year ○.

### 9.2 Inheritance

- **The umbrella concept is not heritable** — inheritance is a property of individual causes.
- **Autosomal dominant**: Liddle syndrome, GRA/FH-I, FH-II (*CLCN2*), FH-III (*KCNJ5*), PASNA (*CACNA1D*), Gordon syndrome (mostly), Geller syndrome, hypertension-with-brachydactyly, most PPGL syndromes (with *SDHD* and *SDHAF2* showing **paternal-only transmission** due to imprinting — a real gotcha for counseling).
- **Autosomal recessive**: AME (*HSD11B2*), hypertensive CAH forms, *KLHL3*-recessive Gordon syndrome, ARPKD.
- **X-linked**: not a significant category.
- **Multifactorial/polygenic**: OSA-related and obesity-related hypertension.
- **Penetrance**: high for the hypertension phenotype in Liddle, GRA and AME; **incomplete and age-dependent** in PPGL syndromes (*SDHB* penetrance estimates have fallen substantially with unbiased ascertainment — historically ~70%, more recent estimates far lower, ~20–25% by age 60 ○).
- **Expressivity**: highly variable, notably in Gordon syndrome (*"quite variable"*, with short stature, dental abnormalities and intellectual difficulties in some ○) and in *SDHx* carriers.
- **Anticipation**: not described.
- **Germline mosaicism**: reported in NF1; rare elsewhere.
- **Founder effects**: *SDHD* p.Asp92Tyr (Dutch), *SDHB* founder alleles in several populations, *RET* founder variants ○.
- **Consanguinity**: relevant for AME and recessive CAH — AME clusters in consanguineous populations.
- **Carrier frequency**: *HSD11B2* pathogenic carriers are rare, but heterozygotes may show salt sensitivity — a legitimate "carriers aren't unaffected" observation.

### 9.3 Demographics

- **Sex**: female predominance in the young-adult secondary-hypertension cohort ✔ and strongly in FMD ○. OSA-related hypertension is male-predominant. PA is roughly balanced with sex-linked mutation spectra (see §4.2).
- **Ancestry**: *CACNA1D* somatic mutations more prevalent in Black males, *KCNJ5* in Black females ○; *KCNJ5* dominant in East Asian cohorts ○. Black patients have higher rates of low-renin/salt-sensitive hypertension generally.
- **Geography**: two-thirds of all hypertension burden is in low- and middle-income countries ○ (WHO 2023); secondary-cause *detection* is concentrated in high-income referral centers, so the geographic distribution of *diagnosis* is a health-system artifact, not biology. Worth stating explicitly in any epidemiology annotation.
- **Age**: bimodal — see §8.

---

## 10. Diagnostics

### 10.1 Who to screen — the 2025 guideline shift

**✔ VERIFIED — Adler GK, Stowasser M, Correa RR, Khan N, Kline G, McGowan MJ, Mulatero P, Murad MH, Touyz RM, Vaidya A, Williams TA, Yang J, Young WF, Zennaro MC, Brito JP. "Primary Aldosteronism: An Endocrine Society Clinical Practice Guideline." *J Clin Endocrinol Metab*. 2025. PMID:40658480. DOI:10.1210/clinem/dgaf284**

The headline recommendation: *"all individuals with hypertension be screened for PA by measuring aldosterone and renin."* Also recommends *"mineralocorticoid receptor antagonists (MRAs) over epithelial sodium-channel (ENaC) inhibitors"*, with spironolactone preferred on cost and availability. **Note a published correction exists: PMID:40880123 ✔** (DOI:10.1210/clinem/dgaf472) — check it before quoting specific thresholds.

Its evidence base: **✔ Farah MH, Hegazi M, Firwana M, et al. "A Systematic Review Supporting the Endocrine Society Clinical Practice Guideline on Management of Primary Aldosteronism." *J Clin Endocrinol Metab* 2025. PMID:40658500. DOI:10.1210/clinem/dgaf290** — 95 studies. Screening was *"associated with higher rates of using PA-specific medical therapies and better blood pressure control."* AVS improved surgical cure rates but increased hemorrhage risk. *"Surgical therapy may be associated with better blood pressure control than medical therapy, with a lower number and dosage of antihypertensive medications."* Spironolactone outperformed eplerenone for hypokalemia control.

**2025 AHA/ACC hypertension guideline** ○ SOURCED — expands PA screening to **all patients with stage 2 or resistant hypertension regardless of serum potassium**, plus unexplained hypokalemia, OSA, incidental adrenal mass, family history of early-onset hypertension, or stroke before age 40. Practically important: *"all antihypertensive medications except mineralocorticoid receptor antagonists (MRA) should be continued to avoid unnecessary delays or barriers to screening."* This removes the drug-washout step that historically killed most screening attempts.

**And ✔ the young-adult study's own conclusion:** *"all patients with hypertension under 40 years of age should be screened for secondary causes"* (PMID:39297209).

### 10.2 Test menu by cause

| Cause | First-line test | Confirmatory | Localization |
|---|---|---|---|
| **Primary aldosteronism** | Plasma **aldosterone-to-renin ratio (ARR)** — the preferred initial test across all major guidelines ○ | Saline infusion test, oral sodium loading, fludrocortisone suppression, captopril challenge | Adrenal CT **plus adrenal vein sampling** — AVS is required because CT and AVS disagree often enough to matter ✔ (PAPY) |
| **PPGL** | Plasma free **metanephrines** or 24-h urinary fractionated metanephrines | Clonidine suppression (rarely) | CT/MRI; ¹²³I-MIBG, ⁶⁸Ga-DOTATATE PET (superior for SDHx-related and metastatic disease) |
| **Cushing** | 1-mg overnight dexamethasone suppression, late-night salivary cortisol, 24-h urinary free cortisol (any 2 abnormal) | ACTH level; high-dose DST; CRH stimulation | Pituitary MRI; **inferior petrosal sinus sampling**; chest/abdomen CT for ectopic ACTH |
| **Renovascular** | Renal artery **duplex ultrasound** | CT angiography or MR angiography | Catheter angiography (gold standard; therapeutic in the same sitting) |
| **Renal parenchymal** | Serum creatinine/eGFR, urinalysis, urine albumin-creatinine ratio | Renal ultrasound | Kidney biopsy where indicated |
| **OSA** | STOP-BANG / Epworth, then **polysomnography** or home sleep apnea test | AHI quantification | — |
| **Coarctation** | Four-limb BP, radiofemoral delay, echocardiography | CT/MR angiography | — |
| **Thyroid / parathyroid** | TSH; serum calcium + PTH | Free T4/T3; ionized calcium, 24-h urine calcium | Sestamibi scan for parathyroid |
| **Drug-induced** | **Structured medication and supplement history** — the cheapest, highest-yield test in the entire workup, and the most frequently skipped | Rechallenge/dechallenge observation | — |
| **Monogenic** | Suppressed renin + suppressed aldosterone + early onset + family history | **Targeted gene panel** | — |

**Cross-cutting**: 24-h ambulatory BP monitoring (essential — establishes the diagnosis, detects non-dipping, excludes white-coat effect), ECG and echocardiography for LVH, fundoscopy.

### 10.3 Histopathology — CYP11B2 immunohistochemistry has redefined PA

This is a genuinely recent shift worth curating carefully.

*"The introduction of CYP11B2 immunostaining led to the HISTALDO consensus classification into classical and non-classical histology. The 2022 WHO classification separated solitary aldosterone-producing adenomas/nodules (APA/APN; classical histology) from multiple nodules/micronodules (MAPN/MAPM; non-classical histology)"* ○ SOURCED.

Consequences:
- **Classical** histology (single dominant CYP11B2-positive lesion) → surgery usually curative.
- **Non-classical** (multinodular) → *"~40%–45% persistent biochemical aldosteronism"* after surgery ○.
- A refinement, the **CYP11B2 size ratio (B2R)**: B2R ≥8.1 indicates classical histology with high cure likelihood; **B2R <8.1** indicates non-classical multinodular disease with lower cure rates and higher recurrence risk ○ SOURCED (Stenman et al., *Histopathology*; and PMID:40729417 ○ "Improving diagnosis in primary aldosteronism using HISTALDO and nodule size metrics", *Eur J Endocrinol* 2025).
- **The caveat that keeps it honest**: CYP11B2-positive micronodules are *"common… in adrenals from non-PA patients"* ○, so the assay does not cleanly separate disease from normal ageing adrenal nodularity. Model this as a diagnostic-uncertainty knowledge gap, not a settled criterion.

### 10.4 Genetic testing

- **Gene panel** is the right default for suspected monogenic hypertension. A registered "Monogenic Hypertension Genetic Panel" exists in NCBI GTR (test 592295 ○).
- **PPGL**: germline testing recommended for **all** patients regardless of family history, given the 25–40% germline rate ○. Panel covering *SDHA/B/C/D/AF2*, *VHL*, *RET*, *NF1*, *MAX*, *TMEM127*, *FH*.
- **GRA/FH-I** requires **long-range PCR or MLPA** for the chimeric gene — standard sequencing panels miss it. This is a common false-negative and worth an explicit note.
- **WES/WGS**: reserved for panel-negative, strongly suspicious cases.
- **CMA/karyotype**: for syndromic presentations (Turner syndrome).
- **Cascade testing**: indicated for all confirmed monogenic and PPGL-syndrome families.
- **Somatic testing** of resected APA tissue: research-grade today, but genotype predicts LV remodeling recovery ○ and may become prognostic.

### 10.5 Differential diagnosis

| Confuser | Distinguishing feature |
|---|---|
| Essential hypertension | Normal ARR, normal metanephrines, no cause found on structured workup |
| White-coat hypertension | Normal ABPM/home BP |
| Pseudoresistance (non-adherence) | Drug-level testing or witnessed dosing — a large fraction of "resistant" hypertension |
| Obesity-related hypertension | Overlaps PA mechanistically (obesity raises aldosterone ✔ PMID:18445663), so ARR must be interpreted with care |
| Preeclampsia | Pregnancy-specific, proteinuria, resolves postpartum |
| Anxiety / panic disorder | Mimics PPGL spells; metanephrines normal |
| Bartter/Gitelman | Hypokalemic alkalosis **without** hypertension — the discriminating axis is BP, not potassium |

### 10.6 Screening

- No population-wide screening for secondary hypertension exists. **Case-finding within a hypertensive population** is the operative model, and per §10.1 the eligible population has been broadened dramatically.
- Newborn screening: 21-hydroxylase CAH is screened, but the *hypertensive* CAH forms (11β- and 17α-hydroxylase) are **not** captured by standard 17-OHP newborn screening. Worth noting explicitly.
- Cascade screening for monogenic and PPGL families.
- Pediatric BP measurement from age 3 is the practical screening entry point for the childhood renal causes.

---

## 11. Outcome / Prognosis

### 11.1 The central prognostic fact: secondary hypertension is worse than its blood pressure

**✔ VERIFIED — Monticone S, D'Ascenzo F, Moretti C, Williams TA, Veglio F, Gaita F, Mulatero P. "Cardiovascular events and target organ damage in primary aldosteronism compared with essential hypertension: a systematic review and meta-analysis." *Lancet Diabetes Endocrinol*. 2018. PMID:29129575**

31 studies, **3,838 PA patients vs 9,284 essential-hypertension controls**, median 8.8-year follow-up. Odds ratios vs essential hypertension:

| Outcome | OR |
|---|---|
| Stroke | **2.58** |
| Coronary artery disease | **1.77** |
| Atrial fibrillation | **3.52** |
| Heart failure | **2.05** |

Plus increased diabetes and metabolic syndrome. The authors: *"Diagnosing primary aldosteronism in the early stages of disease, with early initiation of specific treatment, is important because affected patients display an increased cardiovascular risk compared with patients with essential hypertension."*

Broader ranges reported elsewhere: 2.5–4× stroke, 2.6–6.5× non-fatal MI, 3.2–12× atrial fibrillation ○ SOURCED.

### 11.2 The finding that changes how you treat it

**✔ VERIFIED — Hundemer GL, Curhan GC, Yozamp N, Wang M, Vaidya A. "Cardiometabolic outcomes and mortality in medically treated primary aldosteronism: a retrospective cohort study." *Lancet Diabetes Endocrinol*. 2018. PMID:29129576**

602 medically treated PA patients vs 41,853 age-matched essential-hypertension controls. **Despite comparable blood pressure control**, PA patients had cardiovascular events at **56.3 vs 26.6 per 1,000 person-years**, plus higher mortality, diabetes and atrial fibrillation.

The mechanistic punchline: *"excess risk was limited to patients whose renin remained suppressed during treatment; those receiving higher antagonist doses with unsuppressed renin showed no significant excess risk."*

Read that carefully, because it's the whole ballgame. **Normalizing the blood pressure is not the therapeutic target — un-suppressing the renin is.** A suppressed renin on treatment means the MR is still occupied and still driving fibrosis and inflammation, whatever the cuff says. This is the clearest clinical demonstration anywhere that the pressure and the injury are separable, and it converts §6.2's mechanism into a dosing rule.

### 11.3 Recovery with cause-directed treatment

- **Adrenalectomy for unilateral PA**: *"markedly superior outcomes over medical therapy, yielding an absolute risk reduction in all-cause mortality that rivals or exceeds many major cardiovascular surgeries"* ○ SOURCED. Also lowers incident atrial fibrillation long-term ○ (PMID:29483224 ○). Complete clinical success (cure of hypertension off all drugs) in roughly a third; biochemical cure in the large majority. Predictors of cure: shorter hypertension duration, younger age, female sex, fewer antihypertensives, classical HISTALDO histology / B2R ≥8.1 ○.
- **FMD revascularization**: hypertension cure **46% (95% CI 40–52%)** after angioplasty and **58% (95% CI 53–62%)** after surgery ○ SOURCED. Genuinely curative in a way atherosclerotic RAS is not.
- **Atherosclerotic RAS**: CORAL and ASTRAL failed to show benefit of revascularization over medical therapy — and, importantly for interpretation, *"Patients with fibromuscular dysplasia were not part of the CORAL trial"* ○. Do not generalize CORAL to FMD. That is a Named-Entity-Confusion trap sitting right in the literature.
- **CPAP for OSA**: modest BP reduction, *"typically 2–5 mmHg"*, greater in resistant hypertension, obesity, and high adherence ○ SOURCED. CPAP alone rarely suffices — *"often requiring additional antihypertensive medications"* ✔ (Shiina 2024).
- **Drug-induced**: usually fully reversible on withdrawal ○.
- **Coarctation repair**: high rate of persistent or recurrent hypertension even after successful anatomic repair, especially with late repair — an important expectation-setting fact.

### 11.4 Mortality

- Untreated PA: *"10–20% higher mortality rates over 5–10 years compared to essential hypertension"* ○ SOURCED (a modeled/aggregate estimate — flag as such).
- Malignant/accelerated hypertension carries very poor untreated survival (historically ~20% at 1 year) with dramatic improvement on treatment ○.
- PPGL: benign resected disease has near-normal survival; metastatic disease (higher risk with *SDHB*) has 5-year survival ~40–60% ○.
- Untreated Cushing syndrome: ~4–5× standardized mortality ratio, normalizing with remission ○.

### 11.5 Prognostic factors

Duration of hypertension before diagnosis (dominant) · age at diagnosis · degree of target-organ damage at presentation · **on-treatment renin** (PA — ✔ Hundemer) · APA histology class and B2R ○ · APA driver genotype (*KCNJ5* → better LV recovery ○) · lateralization (unilateral vs bilateral) · baseline eGFR · *SDHB* status in PPGL.

---

## 12. Treatment

### 12.1 Governing principle

**Treat the cause, then treat the pressure.** Everything below is downstream of that. Where the cause is correctable, generic antihypertensive therapy is a bridge, not a destination.

### 12.2 Cause-directed treatment

| Cause | Definitive treatment | NCIT lead (all △ — verify) |
|---|---|---|
| Unilateral PA | **Laparoscopic adrenalectomy** | Surgical Procedure `NCIT:C15329` (reasonably confident); a specific adrenalectomy term exists — look it up rather than guessing |
| Bilateral PA | **Lifelong MRA** (spironolactone preferred; eplerenone if intolerant) | Pharmacotherapy `NCIT:C15986` |
| PPGL | **Resection after α-blockade then β-blockade** — order is non-negotiable | Surgical Procedure `NCIT:C15329` |
| Cushing disease | Transsphenoidal pituitary surgery; radiotherapy or medical therapy (osilodrostat, metyrapone, ketoconazole, pasireotide, mifepristone) second-line | Surgical Procedure; Pharmacotherapy |
| Renovascular — FMD | **Percutaneous transluminal angioplasty**, usually without stent | Therapeutic Procedure `NCIT:C49236` |
| Renovascular — atherosclerotic | **Medical therapy first** (CORAL/ASTRAL); revascularization for flash pulmonary edema, refractory BP, or deteriorating renal function | — |
| Coarctation | Surgical repair or stent | Surgical Procedure |
| OSA | **CPAP**; weight loss; consider MRA | Medical Device `NCIT:C16830` as a qualifier; the *action* is the treatment term |
| Renal parenchymal | RAAS blockade, sodium restriction, CKD management; dialysis/transplant at end-stage | Pharmacotherapy; Organ Transplantation `NCIT:C15289` |
| Drug-induced | **Withdraw or substitute the culprit** | — |
| Liddle syndrome | **Amiloride or triamterene** (direct ENaC blockade) — spironolactone does *not* work, because the defect is downstream of the receptor | Pharmacotherapy |
| GRA/FH-I | **Low-dose glucocorticoid** ± MRA | Pharmacotherapy |
| AME | MRA ± dexamethasone; strict sodium restriction | Pharmacotherapy |
| Gordon syndrome | **Thiazide diuretic** (direct NCC blockade) — dramatically effective | Pharmacotherapy |
| Hypertensive CAH | Glucocorticoid replacement suppressing ACTH-driven DOC | Pharmacotherapy |

**Note the pattern in the last five rows.** Each monogenic syndrome has a *mechanistically matched* drug that works far better than generic therapy, and in Liddle's and Geller's cases the "obvious" drug (spironolactone) is useless or actively harmful. This is precision medicine in its oldest and least glamorous form, and it's a strong argument for genotyping.

### 12.3 Pharmacotherapy — agents

**Mineralocorticoid receptor antagonists**: spironolactone (steroidal, non-selective — gynecomastia, menstrual irregularity), eplerenone (selective, weaker, twice-daily), finerenone (non-steroidal, approved for CKD in T2D — cardiorenal rather than antihypertensive indication), esaxerenone. Guideline preference: **MRAs over ENaC inhibitors**, spironolactone first ✔ (PMID:40658480).

**ENaC inhibitors**: amiloride, triamterene. First-line specifically for Liddle syndrome.

**Standard classes as adjuncts**: ACE inhibitors/ARBs (caution and monitoring in bilateral RAS), calcium channel blockers, thiazides, β-blockers (**never before α-blockade in PPGL** — unopposed α-stimulation precipitates crisis), α-blockers (phenoxybenzamine, doxazosin) for PPGL preparation.

**Pharmacogenomics**: *CYP3A5* expressor status affects tacrolimus exposure and therefore CNI-hypertension risk; *CYP2C9*/*VKORC1* relevant to anticoagulation in the AF complications rather than to BP itself; spironolactone has no established PGx gate. PharmGKB is the place to check.

### 12.4 Recent and emerging therapeutics (2023–2026)

**Aldosterone synthase inhibitors** — the most consequential new mechanism in decades. These inhibit CYP11B2 directly, cutting aldosterone at the source rather than blocking its receptor, with the design challenge being selectivity over the 93%-identical CYP11B1 (cortisol synthase) to avoid adrenal insufficiency.

- **✔ VERIFIED — Freeman MW, Halvorsen YD, Marshall W, Pater M, Isaacsohn J, Pearce C, Murphy B, Alp N, Srivastava A, Bhatt DL, Brown MJ; BrigHTN Investigators. "Phase 2 Trial of Baxdrostat for Treatment-Resistant Hypertension." *N Engl J Med*. 2023. PMID:36342143.** 248 patients on ≥3 antihypertensives. *"Dose-dependent changes in systolic blood pressure of -20.3 mm Hg, -17.5 mm Hg, -12.1 mm Hg, and -9.4 mm Hg were observed in the 2-mg, 1-mg, 0.5-mg, and placebo groups, respectively."* The 2-mg dose beat placebo by **-11.0 mm Hg (P<0.001)**, with selective aldosterone reduction and **no adrenocortical insufficiency**. *"No deaths occurred during the trial, no serious adverse events were attributed by the investigators to baxdrostat."*
- **The honest counterweight ✔** — Dey S, Frishman WH, Aronow WS. "Baxdrostat: An Aldosterone Synthase Inhibitor for the Treatment of Systemic Hypertension." *Cardiol Rev*. 2025. PMID:37548462. *"An increased level of aldosterone is associated with inflammation, systemic hypertension, and organ fibrosis, contributing to adverse cardiovascular events."* But: **"the subsequent HALO trial failed to demonstrate blood pressure-lowering benefits compared to placebo."** Do not curate baxdrostat as an unqualified success — BrigHTN was positive, HALO was not, and reconciling them (dosing, adherence, population) is an open question.
- Baxdrostat in PA specifically: a **Phase 2a study, *NEJM* 2025** ○ — 15 PA patients, resolved or reduced hypertension, aldosterone excess, and hypokalemia.
- **✔ VERIFIED — Laffin LJ, Kopjar B, Melgaard C, Wolski K, Ibbitson J, Bhikam S, Weir MR, Ofili EO, Mehra R, Luther JM, Cohen DL, Sarraju A, Wilkinson MJ, Flack JM, Rodman D, Nissen SE; Advance-HTN Investigators. "Lorundrostat Efficacy and Safety in Patients with Uncontrolled Hypertension." *N Engl J Med*. 2025. PMID:40267417. DOI:10.1056/NEJMoa2501440.** 285 participants. At 12 weeks, systolic BP fell **15.4 mm Hg** (stable 50 mg) and **13.9 mm Hg** (dose-adjusted) vs **7.4 mm Hg** placebo. Hyperkalemia in 5–7% of lorundrostat recipients vs none on placebo — the expected class toxicity, and the thing to monitor. Conclusion: *"Lorundrostat was associated with greater reductions in 24-hour average blood pressure than placebo."*
- Related: Launch-HTN and Target-HTN lorundrostat programs ○; a review of the class, PMID:38358268 ✔ (Feldman, Frishman, Aronow, *Cardiol Rev*).

**Renal denervation** — **two systems FDA-approved in November 2023** ○ SOURCED, ten days apart: ReCor Medical's ultrasound **Paradise** system (advisory panel voted unanimously on safety, 8–3 on efficacy) and Medtronic's radiofrequency **Symplicity Spyral**. Both carry broad indications for hypertension when lifestyle change and drugs fail. Relevant trial: **✔ Townsend RR, Ferdinand KC, Kandzari DE, Kario K, Mahfoud F, Weber MA, Schmieder RE, Pocock S, Tsioufis K, David S, Steigerwalt S, Walton A, Hopper I, Bertolet B, Sharif F, Fengler K, Fahy M, Hettrick DA, Brar S, Böhm M. "Impact of Antihypertensive Medication Changes After Renal Denervation Among Different Patient Groups: SPYRAL HTN-ON MED." *Hypertension*. 2024. PMID:38314554.** Note RDN targets the *sympathetic* limb, so it is mechanistically aimed at Chain E and neurogenic hypertension rather than at mineralocorticoid excess — an important scoping point when linking treatments to mechanism nodes.

**Other emerging**: zilebesiran (siRNA against hepatic *AGT*, ~6-monthly dosing — note the several angiotensinogen-iRNA patents that surfaced in searching, which is a signal of how active this space is); endothelin antagonists (aprocitentan, approved for resistant hypertension); SGLT2 inhibitors and GLP-1/GIP receptor agonists as adjuncts, *"may benefit patients with nocturnal and obesity-related hypertension"* ✔ (Shiina 2024).

### 12.5 Adverse events

Spironolactone: hyperkalemia, gynecomastia (dose-dependent, up to ~10%), menstrual irregularity, AKI. ASIs: hyperkalemia (5–7% ✔), hyponatremia, theoretical cortisol suppression (not observed at effective baxdrostat doses ✔). Phenoxybenzamine: profound orthostatic hypotension, reflex tachycardia, nasal congestion. Adrenalectomy: hemorrhage, adrenal insufficiency if bilateral. AVS: **hemorrhage/adrenal vein rupture** ✔ (Farah 2025). Renal angioplasty: dissection, restenosis, atheroembolism. RDN: access-site complications, rare renal artery stenosis (FDA MAUDE analysis exists ○).

### 12.6 Treatment algorithm (synthesized)

1. Confirm hypertension with out-of-office BP. Exclude pseudoresistance and non-adherence.
2. Screen by risk profile — and note that the risk profile is now **very** wide: all hypertensives for PA per the Endocrine Society ✔, all under-40s for secondary causes generally ✔, stage 2/resistant per AHA/ACC ○.
3. Structured medication and supplement review. *Do this first — it costs nothing.*
4. Baseline: electrolytes, creatinine/eGFR, urinalysis + ACR, TSH, calcium, ECG, ABPM.
5. ARR (continuing all drugs except MRAs ○). If positive → confirmatory testing → CT → AVS if surgery is contemplated.
6. Targeted testing driven by phenotype: metanephrines, cortisol screen, renal imaging, polysomnography.
7. Genetic panel if young onset, family history, or a suppressed-renin/suppressed-aldosterone biochemical signature.
8. Cause-directed definitive treatment (§12.2).
9. Residual hypertension → guideline combination therapy, with **MRA as the preferred fourth agent** in resistant hypertension.
10. **Titrate to unsuppressed renin in PA, not merely to target BP** ✔ (Hundemer 2018) — the most under-implemented recommendation in this whole field.
11. Consider ASI or renal denervation for genuinely refractory cases.

---

## 13. Prevention

**Primary prevention** — mostly not applicable to the genetic and neoplastic causes. Where it applies:
- Sodium restriction and potassium-rich diet (blunts every mineralocorticoid mechanism).
- Weight management → prevents OSA and obesity-associated aldosterone excess.
- Avoid/limit the pressor drug classes; use the lowest effective NSAID dose and duration.
- Avoid chronic liquorice ingestion (and be aware it hides in confectionery, teas and some tobacco products).
- Atherosclerosis risk-factor control → prevents atherosclerotic RAS.
- Occupational lead and cadmium controls.
- Alcohol moderation.

**Secondary prevention (early detection)** — this is where the leverage is, given screening rates below 2% ○:
- Systematic PA screening per the 2025 guidelines ✔.
- Screen every hypertensive under 40 ✔.
- Pediatric BP measurement from age 3.
- Cascade genetic screening in monogenic and PPGL families; biochemical + imaging surveillance for *SDHx* carriers, beginning in childhood for *SDHB*.
- Prenatal/preimplantation testing available for monogenic forms — a genetic-counseling conversation, not a routine offer.

**Tertiary prevention (preventing complications in established disease)**:
- Achieve **and biochemically confirm** cause-directed control — the on-treatment renin target ✔.
- Statins, glycemic control, smoking cessation.
- Post-adrenalectomy and post-coarctation-repair surveillance for recurrence.
- Lifelong BP monitoring after any "cure" — cure is frequently partial.

**Immunization**: not applicable, except indirectly (streptococcal and hepatitis B vaccination reduce post-infectious glomerulonephritis and HBV-PAN routes).

**Genetic counseling**: essential for all monogenic forms and PPGL syndromes. Flag the imprinting quirk — *SDHD* and *SDHAF2* transmit disease **only from the father**, and a counselor who misses that gives wrong risk figures to half the family.

**Public health**: population sodium reduction (reformulation, labeling), the WHO HEARTS package, air-pollution and noise abatement, lead abatement. WHO estimates **76 million deaths could be averted 2023–2050** with scaled-up hypertension coverage ○.

---

## 14. Other Species / Natural Disease

**This section has a genuinely underappreciated star: the cat.**

| Species | NCBITaxon | Natural disease | Notes |
|---|---|---|---|
| **Domestic cat** | `NCBITaxon:9685` △ | **Feline primary hyperaldosteronism ("Conn's syndrome of cats")** | Increasingly recognized, likely *under*-diagnosed; presents with hypokalemic polymyopathy (cervical ventroflexion, weakness) and hypertensive retinopathy with acute blindness from retinal detachment. Unilateral adrenal adenoma/carcinoma or bilateral hyperplasia — the same architecture as human PA. Treated with adrenalectomy or spironolactone + potassium. A **naturally occurring, spontaneous, non-engineered model of human PA** ○ |
| **Domestic cat** | as above | **CKD-associated hypertension** | The most common feline secondary hypertension; also hyperthyroidism-associated |
| **Domestic dog** | `NCBITaxon:9615` △ | **Pheochromocytoma**; **hyperadrenocorticism (canine Cushing's)** — very common; CKD-associated hypertension | Canine Cushing's is one of the most common canine endocrinopathies; hypertension in a large proportion |
| **Ferret** | `NCBITaxon:9669` △ | Adrenocortical disease (sex-steroid-secreting) | Different steroid output; limited hypertension relevance |
| **Horse** | `NCBITaxon:9796` △ | PPID (equine Cushing's, pars intermedia dysfunction) | Metabolic rather than markedly hypertensive |
| **Rat / mouse** | `NCBITaxon:10116` / `NCBITaxon:10090` △ | Genetic hypertension strains | Mostly *primary*-hypertension models — see §15 |

**Orthologous genes**: *Kcnj5*, *Cacna1d*, *Scnn1b*, *Scnn1g*, *Hsd11b2*, *Nr3c2*, *Cyp11b2*, *Wnk1*, *Wnk4*, *Klhl3*, *Cul3*, *Ren*, *Agt*, *Ace* — all conserved across mammals. Resolve NCBI Gene IDs via the Alliance of Genome Resources rather than by recall.

**Comparative pathology**: the RAAS is deeply conserved across vertebrates; renin-angiotensin regulation of blood pressure and sodium is present from fish onward. This makes the mechanisms of Chains A, B and C highly translatable. The mechanisms of Chain E (OSA) translate poorly — humans' unique upper-airway anatomy and bipedal fluid dynamics have no clean animal counterpart, which is precisely why OSA models rely on artificial intermittent-hypoxia chambers rather than spontaneous airway collapse.

**Zoonotic potential**: none. Not transmissible.

**Look up OMIA** for the feline hyperaldosteronism and canine pheochromocytoma entries before curating — I did not resolve OMIA IDs here.

---

## 15. Model Organisms

### 15.1 Surgical / induced models

**Two-kidney-one-clip (2K1C) Goldblatt — the canonical renovascular model**
- Method: silver clip on one renal artery, contralateral kidney intact. *"Induces renal ischemia and decreases renal blood flow, and the activation of the renin-angiotensin system in the clipped kidney is the most important mechanism contributing to its development"* ○ SOURCED. *"The development of 2K1C Goldblatt hypertension is associated with marked increases in renin expression and angiotensin II generation in the clipped kidney and their release into circulation"* ○.
- Species: originally dogs (Goldblatt, early 1930s), then rats, now well established in mice ○.
- **Fidelity: HIGH** for human unilateral renal artery stenosis. It reproduces the renin-dependence, the two-phase course, and the therapeutic response to RAAS blockade.
- Key validation: *"Angiotensin II is a necessary component for the development of hypertension in the two kidney, one clip rat"* ○ (PMID:6280481 ○). Also: *"Genetic Deletion of AT1a Receptor or Na+/H+ Exchanger 3 Selectively in the Proximal Tubules of the Kidney Attenuates Two-Kidney, One-Clip Goldblatt Hypertension in Mice"* ○ — a clean tubule-specific mechanistic dissection.
- **Limitations**: an abrupt mechanical clip is not slowly progressive atherosclerotic stenosis; no atherosclerotic milieu; young healthy animals; rodent renal physiology differs in renin handling.

**One-kidney-one-clip (1K1C) — the volume-dependent counterpart**
- *"The one-kidney, one-clip model of Goldblatt renovascular hypertension is non-renin-dependent, while the two-kidney, one-clip Goldblatt hypertensive rat is renin-dependent, in which vascular hypertrophy is less severe"* ○ SOURCED.
- **This pair is scientifically gorgeous**: the *same* lesion produces renin-dependent or volume-dependent hypertension purely as a function of whether a pressure-natriuresing kidney remains. It is the direct experimental basis for the Chain B step-8 branch, and it explains at the bench why bilateral RAS behaves differently from unilateral. **Fidelity: HIGH** for bilateral disease / solitary kidney.

**DOCA-salt**
- Method: uninephrectomy + deoxycorticosterone acetate + high-salt drinking water.
- Models **mineralocorticoid-excess hypertension** — the closest induced analogue of PA and AME. Low-renin, volume-dependent, with prominent vascular and cardiac fibrosis and inflammation.
- **Fidelity: MODERATE-HIGH** for the mineralocorticoid mechanism; the uninephrectomy and supraphysiological steroid dose are the main departures from human disease.

**Chronic angiotensin II infusion (osmotic minipump)**
- Models Ang-II-driven hypertension with vascular inflammation, immune-cell infiltration and cardiac remodeling. The workhorse for the immune-mechanism literature.
- **Fidelity: MODERATE** — supraphysiological, non-physiologically-regulated Ang II delivery.

**Chronic intermittent hypoxia (CIH)** — for OSA (Chain E). Cyclic hypoxia chambers reproduce sympathetic activation, carotid-body sensitization and BP elevation. **Fidelity: MODERATE, with a large caveat**: reproduces the *hypoxia* limb but not airway collapse, negative intrathoracic pressure swings, arousals, or the rostral-fluid-shift loop. This is a textbook `PARTIALLY_RECAPITULATES` with a `HUMAN_MODEL_MISMATCH` attached.

### 15.2 Genetic models

| Model | Human counterpart | Notes |
|---|---|---|
| **Scnn1b R566X knock-in mouse** (Liddle mouse) | Liddle syndrome | Salt-dependent hypertension, hypokalemia, low aldosterone. **Fidelity: HIGH** — arguably the best genetic hypertension model available |
| ***Hsd11b2*-null mouse** | AME | Hypertension, hypokalemia, cortisol-mediated MR activation. **Fidelity: HIGH**, though rodents use corticosterone not cortisol — a real species caveat |
| ***Nr3c2* (MR) tissue-specific knockouts** | MR biology | Endothelial-specific MR deletion *"prevents the development of vascular and cardiac fibrosis and stiffness"* ○ — the key evidence separating MR's vascular from its renal actions |
| ***Kcnk3/Kcnk9* (TASK-1/TASK-3) knockout mice** | Primary aldosteronism | Loss of the two-pore K⁺ channels depolarizes zona glomerulosa cells → autonomous aldosterone. A genuine genetic PA model recapitulating the depolarization mechanism ○ |
| ***Kcnj5* knock-in models** | FH-III / APA | Recapitulate the human driver mutation |
| ***Wnk4*, *Klhl3*, *Cul3* mutant mice** | Gordon syndrome | Reproduce hyperkalemic hypertension and thiazide sensitivity |
| ***Cyp11b1*/*Cyp11b2* manipulations** | GRA, CAH | Model the steroidogenic block |
| **TGR(mRen2)27 transgenic rat** | Renin-driven hypertension | Fulminant hypertension from a mouse Ren2 transgene |
| **Dahl salt-sensitive rat** | Salt-sensitive hypertension | Polygenic; closer to essential than secondary hypertension |
| **SHR / SHRSP** | Essential hypertension | *"Vascular dysfunction and fibrosis in stroke-prone spontaneously hypertensive rats: the aldosterone-mineralocorticoid receptor-Nox1 axis"* ○ — useful for MR-mediated vascular injury even though the strain models primary hypertension |

### 15.3 In vitro and NAM systems

- **H295R** human adrenocortical carcinoma line — the standard system for aldosterone synthesis, CYP11B2 regulation, and driver-mutation functional testing (Cellosaurus lookup needed for the accession).
- Primary human adrenal cell culture; adrenal organoids (emerging).
- Xenopus oocyte and HEK293 electrophysiology for ENaC, NCC, KCNJ5, CACNA1D variant function — the workhorse for variant classification.
- Human iPSC-derived vascular endothelial cells and endothelial-cell-on-chip for VEGFi and calcineurin-inhibitor vascular toxicity — the most directly relevant NAM for the drug-induced chains, and worth prioritizing given the toxicology framing.
- Precision-cut kidney slices for tubular transport.

### 15.4 Databases

MGI · RGD (especially strong for hypertension — RGD hosts a dedicated hypertension disease portal) · Alliance of Genome Resources · IMPC · IMSR · MMRRC · Cellosaurus · OMIA (for the veterinary natural disease in §14).

---

## Appendix A — Curation notes for dismech

Some things I noticed while assembling this that bear on how the entry should be built. Take or leave.

**1. This concept is probably a `GROUPING`, not a `DISEASE`.**
Per the project's own lump/split rules, `GROUPING` means "a union of distinct diseases." Secondary hypertension is exactly that — primary aldosteronism, pheochromocytoma, renal artery stenosis and VEGF-inhibitor toxicity share no mechanism, only an endpoint. The existing `kb/disorders/Secondary_Hypertension.yaml` (171 lines) is already curated narrowly around the drug-induced/VEGF branch, which suggests the same tension. Options: keep the disease entry scoped to drug/toxin-induced secondary hypertension and add `kb/groupings/Secondary_Hypertension.yaml` as the union, or promote the whole thing to a grouping. Either way, worth a deliberate decision rather than drift.

**2. There is real module material here.** The strongest candidate is a **mineralocorticoid-excess / distal-nephron sodium-retention module**: MR activation → SGK1 → NEDD4-2 phosphorylation → ENaC stabilization → sodium retention → volume expansion, with a parallel MR–Nox1–fibrosis arm. It would take conformers from PA, AME, Cushing, Liddle, liquorice toxicity, and hypertensive CAH — six diseases, one chain. A second candidate: **VEGF-pathway-inhibitor vascular toxicity** (NO deficit + endothelin + capillary rarefaction), which would sit naturally in the treatment-toxicity family alongside the existing entries.

**3. Existing neighbours in the KB** that this entry should connect to: `Essential_Hypertension`, `Familial_Hyperaldosteronism`, `Familial_Hyperaldosteronism_Type_I`, `Pheochromocytoma_Paraganglioma`, `Hereditary_Pheochromocytoma-Paraganglioma_Syndrome`, `Cushings_Syndrome`, `Cushing_Disease`, `Obstructive_Sleep_Apnea`, `Hypertensive_Heart_Disease`, `Hypertensive_Retinopathy`. There is also an open stub at `stubs/Primary_Aldosteronism.yaml` — given that PA is 54.8% of secondary hypertension ✔ and has moved more in the last three years than anything else here, that stub looks like the highest-value thing in the queue adjacent to this work.

**4. Before any of this becomes YAML:** every CURIE marked △ needs `runoak`/`just validate-terms` confirmation, and every quoted string needs `just fetch-reference PMID:x` plus `just count-verified-snippets`. The quotes in this report passed through a summarizing layer. Two PMIDs I probed came back as completely unrelated papers, which is the whole argument for not trusting a plausible-looking identifier.

**5. Genuine knowledge gaps worth recording as `discussions`:**
- The BrigHTN/HALO discordance for baxdrostat ✔ — positive phase 2, negative follow-on, unreconciled.
- CYP11B2-positive micronodules in non-PA adrenals ○ — the histologic criterion does not cleanly separate disease from ageing.
- Epigenetic mechanisms across the board — thin, mostly candidate-level.
- Whether the "renin-independent aldosteronism continuum" ✔ (Brown 2020) means PA should be modeled as a graded trait rather than a categorical disease. That's a nosology question dismech is unusually well-placed to represent, and it isn't settled anywhere else either.
- CIH models capture the hypoxia limb of OSA but not the mechanical or fluid-shift limbs — a clean `HUMAN_MODEL_MISMATCH`.

---

## Sources

**PubMed records verified directly via NCBI E-utilities (✔):**
- [PMID:39297209 — Prevalence and Risk Factors for Secondary Hypertension in Young Adults, *Hypertension* 2024](https://pubmed.ncbi.nlm.nih.gov/39297209/)
- [PMID:32449886 — The Unrecognized Prevalence of Primary Aldosteronism, *Ann Intern Med* 2020](https://pubmed.ncbi.nlm.nih.gov/32449886/)
- [PMID:29129575 — Cardiovascular events and target organ damage in primary aldosteronism, *Lancet Diabetes Endocrinol* 2018](https://pubmed.ncbi.nlm.nih.gov/29129575/)
- [PMID:29129576 — Cardiometabolic outcomes and mortality in medically treated primary aldosteronism, *Lancet Diabetes Endocrinol* 2018](https://pubmed.ncbi.nlm.nih.gov/29129576/)
- [PMID:17161262 — A prospective study of the prevalence of primary aldosteronism in 1,125 hypertensive patients (PAPY), *JACC* 2006](https://pubmed.ncbi.nlm.nih.gov/17161262/)
- [PMID:18445663 — Body mass index predicts plasma aldosterone concentrations, *JCEM* 2008](https://pubmed.ncbi.nlm.nih.gov/18445663/)
- [PMID:40658480 — Primary Aldosteronism: An Endocrine Society Clinical Practice Guideline, *JCEM* 2025](https://pubmed.ncbi.nlm.nih.gov/40658480/)
- [PMID:40658500 — Systematic Review Supporting the Endocrine Society PA Guideline, *JCEM* 2025](https://pubmed.ncbi.nlm.nih.gov/40658500/)
- [PMID:40880123 — Correction to the Endocrine Society PA Guideline, *JCEM* 2025](https://pubmed.ncbi.nlm.nih.gov/40880123/)
- [PMID:36342143 — Phase 2 Trial of Baxdrostat for Treatment-Resistant Hypertension (BrigHTN), *NEJM* 2023](https://pubmed.ncbi.nlm.nih.gov/36342143/)
- [PMID:37548462 — Baxdrostat: An Aldosterone Synthase Inhibitor, *Cardiol Rev* 2025](https://pubmed.ncbi.nlm.nih.gov/37548462/)
- [PMID:40267417 — Lorundrostat Efficacy and Safety in Patients with Uncontrolled Hypertension (Advance-HTN), *NEJM* 2025](https://pubmed.ncbi.nlm.nih.gov/40267417/)
- [PMID:38358268 — Emerging Therapies for Treatment-Resistant Hypertension: Lorundrostat and Related ASIs, *Cardiol Rev*](https://pubmed.ncbi.nlm.nih.gov/38358268/)
- [PMID:38314554 — SPYRAL HTN-ON MED antihypertensive medication changes after renal denervation, *Hypertension* 2024](https://pubmed.ncbi.nlm.nih.gov/38314554/)
- [PMID:39210083 — Obstructive sleep apnea-related hypertension, *Hypertens Res* 2024](https://pubmed.ncbi.nlm.nih.gov/39210083/)

**Other sources consulted (○):**
- [Prevalence and Risk Factors for Secondary Hypertension in Young Adults — full text PDF, AHA Journals](https://www.ahajournals.org/doi/pdf/10.1161/HYPERTENSIONAHA.124.22753)
- [Genetics of Primary Aldosteronism — *Hypertension*](https://www.ahajournals.org/doi/10.1161/HYPERTENSIONAHA.121.16498)
- [KCNJ5 Somatic Mutations in Aldosterone-Producing Adenoma — *Hypertension*](https://www.ahajournals.org/doi/10.1161/HYPERTENSIONAHA.120.15679)
- [Prevalence and clinical correlates of somatic mutation in aldosterone producing adenoma — Taiwanese population, *Sci Rep*](https://www.nature.com/articles/srep11396)
- [Shifting paradigms in primary aldosteronism — *Front Endocrinol* 2024](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2024.1372683/pdf)
- [Broadening Primary Aldosteronism Screening: Alignment Across Contemporary Guidelines — *Hypertension*](https://www.ahajournals.org/doi/10.1161/HYPERTENSIONAHA.125.26228)
- [Updates in the 2025 AHA/ACC Hypertension Guideline — *Curr Hypertens Rep*](https://link.springer.com/article/10.1007/s11906-026-01372-9)
- [New ACC/AHA Guideline Addresses Prevention, Detection, Evaluation and Management of High Blood Pressure — ACC](https://www.acc.org/Latest-in-Cardiology/Journal-Scans/2025/08/14/15/36/New-ACC-AHA-Guideline-Addresses-Prevention-Detection-Evaluation-and-Management-of-HBP)
- [Overview of Monogenic or Mendelian Forms of Hypertension — *Front Pediatr*](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2019.00263/full)
- [The Molecular Genetics of Gordon Syndrome — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6947027/)
- [Monogenic Hypertension Genetic Panel — NCBI GTR](https://www.ncbi.nlm.nih.gov/gtr/tests/592295/)
- [Pheochromocytoma and paraganglioma: implications of germline mutation investigation — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10528659/)
- [Germline genetic variants in pheochromocytoma/paraganglioma — *Endocrine Oncology* 2023](https://eo.bioscientifica.com/view/journals/eo/3/1/EO-22-0091.xml)
- [The hypertension of Cushing's syndrome — *J Hypertens*](https://journals.lww.com/jhypertension/fulltext/2015/01000/the_hypertension_of_cushing_s_syndrome_.6.aspx)
- [Mineralocorticoid and Glucocorticoid Receptors Stimulate ENaC in a Mouse Model of Cushing Syndrome — *Hypertension*](https://www.ahajournals.org/doi/10.1161/hypertensionaha.109.134973)
- [Endocrine hypertension – Cushing's syndrome — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3230089/)
- [Mineralocorticoid antagonists and ENaC inhibitors in hyperaldosteronism — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8030310/)
- [ENaC in Salt-Sensitive Hypertension: Kidney and Beyond — *Curr Hypertens Rep*](https://link.springer.com/article/10.1007/s11906-020-01067-9)
- [Vascular dysfunction and fibrosis in SHRSP: the aldosterone-MR-Nox1 axis — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5446265/)
- [Efficacy of Revascularization For Renal Artery Stenosis Caused by Fibromuscular Dysplasia — *Hypertension*](https://www.ahajournals.org/doi/10.1161/hypertensionaha.110.152918)
- [Atherosclerotic renal artery stenosis in the post-CORAL Trial Era — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0146280625002245)
- [Long Term Outcomes After Renal Revascularization for Atherosclerotic Renovascular Disease (ASTRAL) — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11404757/)
- [Drug induced hypertension – An unappreciated cause of secondary hypertension — ESH](https://www.eshonline.org/esh-content/uploads/2019/07/1.-Drug-induced-hypertension-An-unappreciated-cause-of-secondary-hypertension-main1.pdf)
- [Drug-Induced Hypertension: Focus on Mechanisms and Management — *Curr Hypertens Rep*](https://link.springer.com/article/10.1007/s11906-017-0736-z)
- [Comprehensive analysis of VEGF/VEGFR inhibitor-induced immune-mediated hypertension — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11534862/)
- [Major Adverse Cardiovascular Events in Primary Aldosteronism After Adrenalectomy or MRA Treatment — *JAHA*](https://www.ahajournals.org/doi/10.1161/JAHA.124.038714)
- [Primary aldosteronism: adrenalectomy could save more lives — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12719244/)
- [Improving diagnosis in primary aldosteronism using HISTALDO and nodule size metrics — *Eur J Endocrinol* 2025](https://academic.oup.com/ejendo/article/193/2/278/8217428)
- [Histopathological stratification of primary aldosteronism using the CYP11B2 size ratio — *Histopathology*](https://onlinelibrary.wiley.com/doi/full/10.1111/his.70254)
- [Clinical significance of CYP11B2 immunostaining in unilateral primary aldosteronism — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10831582/)
- [Two-Kidney, One Clip and One-Kidney, One Clip Hypertension in Mice — *Hypertension*](https://www.ahajournals.org/doi/10.1161/01.HYP.29.4.1025)
- [Genetic Deletion of AT1a Receptor or NHE3 in Proximal Tubules Attenuates 2K1C Hypertension — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9779213/)
- [Childhood Hypertension: A Retrospective Analysis of Causes, Treatments, and Complications — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11505861/)
- [Overview of Endocrine Hypertension — Endotext, NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK278980/)
- [Secondary Hypertension — StatPearls Point of Care](https://www.statpearls.com/point-of-care/28819)
- [WHO — First WHO report details devastating impact of hypertension and ways to stop it (2023)](https://www.who.int/news/item/19-09-2023-first-who-report-details-devastating-impact-of-hypertension-and-ways-to-stop-it)
- [WHO Hypertension fact sheet](https://www.who.int/news-room/fact-sheets/detail/hypertension)
- [FDA Approves Paradise Renal Denervation System — TCTMD](https://www.tctmd.com/news/fda-approves-paradise-renal-denervation-system-what-comes-next)
- [Symplicity Spyral Approved: FDA Clears Second Renal Denervation System — TCTMD](https://www.tctmd.com/news/symplicity-spyral-approved-fda-clears-second-renal-denervation-system)
- [EBI OLS4 — MONDO term resolution](https://www.ebi.ac.uk/ols4/api/search?q=secondary+hypertension&ontology=mondo)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 47 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 47 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.
