---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-09-01T12:10:42.720631'
end_time: '2026-09-01T12:33:58.907524'
duration_seconds: 1396.19
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Acute Radiation Syndrome
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
  num_turns: 69
  total_cost_usd: 5.788049999999999
  session_id: bf770c9b-6dfd-4fa3-84bb-dd18b49512a4
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 90
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Radiation Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acute Radiation Syndrome** covering all of the
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

I'll dig in. Loading search tools first.

Good haul. Now let me verify ontology IDs against the repo's own term caches rather than guessing.

Alright, I've got what I need. Here's the report.

---

# Acute Radiation Syndrome — Disease Characteristics Research Report

**Prepared:** 2026-09-01 · **Target:** Acute Radiation Syndrome · **MONDO:0033938** · Category: Complex (environmental / toxicologic, non-Mendelian)

---

## ⚠️ Read this before you paste anything into a `snippet:` field

Every quoted fragment below came out of PubMed's efetch records through an automated retrieval layer, which means a summarizing model touched them on the way here. They are *almost certainly* verbatim, but "almost certainly" is exactly the failure mode that eats a whole curation session three PRs later. So:

**Run `just fetch-reference PMID:<id>` and re-verify every snippet against the cache before it goes into YAML.** Treat this whole document the way the repo already tells you to treat a deep-research report — as leads, not as evidence.

Same deal with the ontology terms. I've split them into two buckets:
- **✅ VERIFIED** — I looked the CURIE up either in this repo's own `cache/<prefix>/terms.csv` (which is authority-backed and already passing term validation elsewhere in the KB) or live against EBI OLS4. The id↔label pair is real.
- **🔎 LEAD** — a plausible term I did *not* resolve. Do not bind it until `just validate-terms` says yes.

sup. Let's get into it.

---

## 1. Disease Information

### What it is

Acute radiation syndrome is what happens when a body absorbs a big dose of penetrating ionizing radiation all at once. It isn't one disease so much as a *scheduling problem*: radiation preferentially kills cells that are dividing, and the body's fastest-dividing tissues are the ones constantly rebuilding themselves — bone marrow, gut lining, skin, gonads. The mature cells already made keep working until they hit their normal expiry date. Then nothing replaces them. So the illness arrives on a timetable set by the half-life of each cell type, which is why ARS has that eerie "feels fine for a week, then falls apart" shape. It's less like a poisoning and more like quietly firing the entire maintenance staff of a building and waiting.

Orphanet's definition (ORPHA:454831):

> "Acute radiation syndrome is a rare radiation-induced disorder resulting from whole body exposure to large doses of penetrating radiation (>0.7 Gray) within a very short period of time (usually minutes) and characterized by bone marrow syndrome with pancytopenia, gastrointestinal syndrome, and cardiovascular/central nervous system syndrome."

Four conditions have to be met simultaneously for ARS (this is the CDC framing): the dose must be **large**, the radiation must be **penetrating** (gamma, X-ray, neutrons — an external alpha or low-energy beta source can't reach marrow), it must hit **most or all of the body**, and it must be delivered in a **short time at high dose rate**. Drop any one of those four and you get a different disease. Chronic low-dose exposure, internal contamination, and a localized radiotherapy field are all *not* ARS, which matters for scoping the KB entry.

### Identifiers

| Resource | Identifier | Status |
|---|---|---|
| MONDO | **MONDO:0033938** — "acute radiation syndrome" | ✅ VERIFIED (OLS4 + local `cache/mondo/terms.csv`) |
| Orphanet | **ORPHA:454831** — "Acute radiation syndrome" | ✅ VERIFIED (orpha.net) |
| ICD-10-CM | **T66** "Radiation sickness, unspecified" (billable children: `T66.XXXA` initial, `T66.XXXD` subsequent, `T66.XXXS` sequela) | ✅ VERIFIED |
| MeSH | **D054508** "Acute Radiation Syndrome" | ✅ VERIFIED |
| ICD-11 | one source returned `NF00`; the prompt guessed `NF06`. **These disagree.** | 🔎 LEAD — resolve against the ICD-11 browser before binding `icd11f` |
| OMIM | Not applicable — no Mendelian entry, this is not a heritable disease | — |
| DOID | not retrieved | 🔎 LEAD |

MONDO synonym on record: *"Acute radiation sickness"*. Other names in common clinical and lay use: **radiation poisoning**, **radiation toxicity**, **radiation sickness**, and in the older Soviet/Ukrainian literature **acute radiation disease (ARD)**.

### Where the knowledge comes from — and why this matters for evidence grading

This is the unusual bit and it should shape the whole entry. **Human ARS knowledge is aggregated from a small number of catastrophes, not from cohorts or EHR.** The total documented human experience is a few thousand people across ~80 years. Lazarus & Gale put it bluntly (PMID:40074513, *Best Pract Res Clin Haematol* 2024):

> "Radiological accidents/incidents are common with nearly 400 reported since 1944 exposing about 3000 people to substantial doses of ionizing radiations with 127 deaths."

So the sources stack like this:
- **Accident registries and case series** — REAC/TS Radiation Accident Registry (Oak Ridge), IAEA accident reports, the Ukrainian Chernobyl ARS survivor cohort.
- **Atomic bomb survivor data** (RERF, Hiroshima/Nagasaki) — the largest human dose-response dataset, but confounded by blast, burns, and wartime lack of medical care.
- **Iatrogenic near-analogs** — total body irradiation conditioning before transplant is essentially a controlled ARS, and is the reason we know anything at all about supportive care windows.
- **Animal-Rule preclinical studies** — because you cannot ethically run an ARS efficacy trial, the FDA's Animal Rule means *every approved drug for this disease was licensed on non-human primate and rodent data*. Christy & Herzig say it plainly (PMID:39000080): "Since clinical trials for ARS cannot be ethically conducted, animal testing is extremely important."

**Curation consequence:** a large fraction of the mechanistic evidence for this entry will legitimately carry `evidence_source: MODEL_ORGANISM`, and that's not a defect — it's the epistemic structure of the field. But per the repo's own rule, model-organism evidence should not be the *only* support for a human phenotype, and here the human phenotypes genuinely are documented (Chernobyl, Goiânia, Tokai-mura). Keep the two layers distinct.

---

## 2. Etiology

### Primary cause

One cause, no ambiguity: **acute, high-dose-rate, whole-body or significant partial-body exposure to penetrating ionizing radiation.**

**Exposure term:** **ECTO:7000047** — "exposure to ionizing radiation" ✅ VERIFIED (local `cache/ecto/terms.csv`; already bound elsewhere in the KB, so it validates offline).

This is the entry's single initiating node, and it should be wired into the pathograph via `environmental[].influences_mechanisms` with `environmental_effect: TRIGGERS`, not left as a floating list item. There is no other etiology to model.

### Exposure scenarios (the real-world routes)

| Scenario | Worked example | Notes |
|---|---|---|
| Reactor accident | Chernobyl 1986; Fukushima Daiichi 2011 | Chernobyl produced the largest ARS case series ever assembled |
| Criticality accident | Tokaimura, Japan, 30 Sept 1999 | Uranium conversion plant; 2 worker deaths; mixed neutron/gamma field |
| Orphan / lost source | Goiânia, Brazil, 13 Sept 1987 | Cs-137 teletherapy source cracked open and handled by the public; 4 ARS deaths, ~250 contaminated |
| Nuclear detonation | Hiroshima, Nagasaki 1945 | Combined injury — blast + thermal burn + radiation |
| Industrial radiography | numerous | Usually localized/cutaneous rather than whole-body |
| Radiological dispersal device ("dirty bomb") / deliberate act | threat scenario | Drives most current countermeasure funding |
| Medical/radiotherapy accident | numerous | Usually partial-body |
| Iatrogenic TBI conditioning | routine | Intentional, controlled, marrow-rescued ARS |

Feldman & Kazzi (PMID:37280005) note the driver behind the recent surge in preparedness work:

> "The conflict in Ukraine has raised the specter of radiological and nuclear incidents, including fighting at the Zaporizhzhia nuclear plant, the largest nuclear powerplant in Europe; concerns that a radiological dispersion device ('dirty bomb') may be used; and threats to deploy tactical nuclear weapons. Children are more susceptible than adults to immediate and delayed radiation health effects."

### Dose–effect thresholds (the load-bearing numbers)

These are the numbers that structure the whole entry, so get them right and cite them individually rather than as a block.

| Threshold | Value | Source |
|---|---|---|
| ARS possible at all | **>0.7 Gy** whole body (some references say ~1 Gy for clinically overt ARS at high dose rate) | Orphanet ORPHA:454831; CDC |
| H-ARS (hematopoietic) onset | **≥ ~2 Gy** clinically overt; damage begins ~0.7 Gy | Christy & Herzig PMID:39000080 — "Exposure to a whole-body radiation dose above about 0.7 Gy results in H-ARS" |
| GI-ARS onset | **~6 Gy** | Freeman PMID:40368913 — "GI-ARS occurs at radiation doses of 6 Gy, with doses of ≥10 Gy typically resulting in death within 10 days." |
| Uniformly lethal GI dose | **≥10 Gy** → death within ~10 days | same |
| Limit of current therapy | **>12 Gy** | Arnautou & Garnier PMID:39025400 — "Radiation doses below 2 Gray generally result in insignificant clinical consequences, while exposures surpassing 12 Gray exceeds current therapeutic capacities." |
| Neurovascular / CNS syndrome | **>20–50 Gy** (sources vary; commonly cited >50 Gy for the fulminant form) | see §6 Branch D |
| Human LD50/60, no medical care | **~2.7–3.1 Gy** marrow dose (DS02 dosimetry, A-bomb data); **2.3–2.6 Gy** by the earlier DS86 system | Fujita, Kato & Schull PMID:1762100, PMID:2693695 |
| Human LD50/60, with modern supportive care | commonly quoted **~4.5 Gy**, plausibly higher with cytokines | secondary literature — ⚠️ **this number is soft; do not present it as a measured value** |

**A caution worth writing into `notes:`.** The A-bomb LD50 is *lower* than the textbook "3.5–4.5 Gy" figure, and the difference isn't a contradiction — it's confounding. Hiroshima and Nagasaki survivors had concurrent burns, blast trauma, malnutrition, and essentially no medical infrastructure. The higher figure assumes an intact hospital. Any prevalence/prognosis record here should carry the care context in `population` or `notes`, or the two numbers will look like a data error to a later reader.

### Modifying factors — physical

Not all Grays are equal, and the entry should say so:

- **Dose rate.** Same total dose delivered slowly is far less lethal; sublethal damage repair happens between hits.
- **Dose uniformity / partial-body sparing.** This is enormous. Shielding even a small marrow volume changes the outcome completely — the standard preclinical GI-ARS model deliberately spares 5% of marrow precisely so the animal survives long enough to *have* a GI syndrome (Mitra et al., PMID:39930324: "13 Gy partial body X-irradiation with 5% bone marrow shielding").
- **Radiation quality / LET.** Neutrons carry higher relative biological effectiveness than photons at equal absorbed dose. Royba et al. (PMID:35994701) found in the dicentric assay that "the frequency of dicentrics depends on the type of radiation" — which means dose estimation itself is quality-dependent.
- **Geometry** — anteroposterior vs. rotational exposure changes marrow dose for the same free-in-air dose.

### Modifying factors — host

- **Age.** Children are more radiosensitive both acutely and for late effects (PMID:37280005). Elderly patients have less marrow reserve.
- **Pregnancy.** Fetal exposure is a separate injury class (teratogenesis, growth restriction) beyond this entry's scope but relevant to triage.
- **Combined injury — the big one.** Radiation *plus* burn or trauma is dramatically worse than either alone, and this is a real mechanistic interaction rather than additive risk. Kiang & Blakely (PMID:36947602) state: **"At present, no FDA-approved drug to protect, mitigate, or treat CI is available."** Glowacki et al. (PMID:34233299) confirm mouse models "show dose-dependent impairment of wound healing." This deserves its own pathophysiology node with `EXACERBATES` semantics, not a footnote.
- **Nutritional status, baseline marrow reserve, comorbid immunosuppression.**
- **Microbiome composition** — see §6; this turns out to be a genuine host modifier, not a curiosity.

### Genetic risk factors

**There is no causal gene.** ARS is fully environmental. But germline DNA-repair defects are legitimate **susceptibility modifiers**, and the mechanism is clean: if you can't repair a double-strand break, the same physical dose becomes a larger biological dose.

| Gene | HGNC | Syndrome | Radiosensitivity evidence |
|---|---|---|---|
| **ATM** | **hgnc:795** ✅ | Ataxia-telangiectasia (AR) | Homozygotes are clinically radiosensitive; literature reports a severe reaction at a dose as low as **3 Gy** in an A-T patient. Amirifar et al. (PMID:32791865) describe A-T as "a rare autosomal recessive syndrome characterized by progressive cerebellar ataxia, oculocutaneous telangiectasia, variable immunodeficiency, radiosensitivity, and cancer predisposition." |
| **NBN** | **hgnc:7652** ✅ | Nijmegen breakage syndrome | "Lymphocytes and fibroblasts of NBS patients have been found to be hypersensitive to IR" |
| **MRE11** | **hgnc:7230** ✅ | ATLD (A-T–like disorder) | Later onset, milder than A-T, same radiosensitivity + chromosomal instability |
| **PRKDC** (DNA-PKcs) | **hgnc:9413** ✅ | NHEJ deficiency / RS-SCID | Core NHEJ kinase |
| **LIG4** | 🔎 LEAD | LIG4 syndrome | Well-documented clinical radiosensitivity |
| **TP53** | **hgnc:11998** ✅ | Li-Fraumeni | Central to the apoptotic response; relevant to late-effect risk |
| **DCLRE1C** (Artemis), **NHEJ1** (Cernunnos), Fanconi anemia genes | 🔎 LEAD | RS-SCID, FA | FA is "characterized by childhood-onset aplastic anemia, cancer or leukemia susceptibility, and cellular hypersensitivity to DNA-crosslinking agents" — note the crosslinker sensitivity is the *defining* feature; IR sensitivity in FA is more variable and contested |

**The ATM heterozygote question is unsettled and should be curated as such.** Carriers are roughly 1–2.5% of the population, and whether they have clinically meaningful intermediate radiosensitivity remains debated. Model this as a `discussions` entry with `kind: KNOWLEDGE_GAP` rather than asserting an effect.

Beyond single genes, **radiogenomics** — Story & Durante (PMID:30421807) define it as "the study of genomic changes that underlie the radioresponse of normal and tumor tissues" — is the field studying common-variant contributions to normal-tissue radiation toxicity. Almost all of it is radiotherapy-derived (fractionated, localized) and its transfer to single-fraction whole-body ARS is an **inference, not a demonstration**. Flag that explicitly if you use it.

Suggested inheritance modeling: **no `inheritance:` block for the disease itself.** Susceptibility genes go in `genetic:` with `relationship_type: SUSCEPTIBILITY` or `MODIFIER`. Do not use `CAUSATIVE` here — nothing in the genome causes ARS.

### Protective factors

**Physical, not biological, is where the real protection lives:** time, distance, shielding; sheltering and evacuation; partial-body shielding of marrow.

**Genetic protective factors:** none established. 🔎 No published protective allele for ARS that I could find.

**Pharmacological prophylaxis:** none FDA-approved. Singh et al. (PMID:39160790) are explicit: **"Currently, there is no radiation medical countermeasure approved by the U.S. FDA which can be used before radiation exposure to protect exposed individuals."** Candidates in §12.

**A distinction the entry must not blur: potassium iodide is not ARS prophylaxis.** KI (**CHEBI:8346** ✅) saturates the thyroid so inhaled/ingested radioiodine can't be taken up. It does nothing about external whole-body dose and nothing about marrow. Same for Prussian blue (cesium/thallium) and Ca-/Zn-DTPA (transuranics) — those are **decorporation agents for internal contamination**, a different disease process. Putting them in `treatments:` for ARS without a very clear scoping note is a modeling error I'd expect a reviewer to flag.

### Gene–environment interaction

The core interaction is **dose × DNA-repair capacity**: identical physical dose produces a larger biological insult in a repair-deficient host, because unrejoined double-strand breaks are the substrate for cell death. That's the mechanistic through-line linking §2 and §6. Beyond the monogenic syndromes, GxE evidence for ARS specifically is thin — most of it is extrapolated from radiotherapy toxicity cohorts.

---

## 3. Phenotypes

### The four-phase temporal architecture

Every ARS phenotype has to be anchored to a phase, or the entry will read as if these things happen at once. They don't. Arnautou & Garnier (PMID:39025400):

> "This syndrome typically progresses through three stages with a prodromal phase, a latency phase and a critical phase. Each of them varies in intensity and duration depending on the absorbed dose of radiation."

Orphanet counts four: **prodromal → latent → manifest illness → recovery or death.** Use four; the recovery/death fork is a real branch. Higher dose compresses every phase — at very high dose the latent period disappears entirely, which is itself diagnostic.

**Suggested `progression:` records** (the `phase` field is the foreign-key target):

| Phase | Timing | What happens |
|---|---|---|
| Prodromal | minutes–48 h | Nausea, vomiting, anorexia, sometimes diarrhea, fatigue, headache; possibly early transient erythema. Time-to-onset is dose-proportional. |
| Latent | days–~3 weeks (dose-dependent; absent at very high dose) | Patient feels well. Counts are falling. This is the window where dose assessment and countermeasure administration happen. |
| Manifest illness | ~1–6 weeks (much sooner for GI) | Subsyndrome-specific: infection/hemorrhage (H), fluid loss/sepsis (GI), necrosis (cutaneous), coma (CNS). |
| Recovery or death | weeks–months | Marrow reconstitution, or death; survivors enter DEARE. |

### Prodromal phenotypes

| Phenotype | HP term | Status | Notes |
|---|---|---|---|
| Nausea | `HP:0002018` Nausea | ✅ | |
| Vomiting | `HP:0002013` Vomiting | ✅ | **Time to emesis is the single best bedside dose proxy** — see §10 |
| Nausea and vomiting (composite) | `HP:0002017` Nausea and vomiting | ✅ | |
| Diarrhea | `HP:0002014` Diarrhea | ✅ | Early diarrhea = high dose; `temporality: ACUTE` |
| Fatigue | `HP:0012378` Fatigue | ✅ | |
| Headache | `HP:0002315` Headache | ✅ | |
| Fever | `HP:0001945` Fever | ✅ | Early fever is a bad sign |
| Anorexia | 🔎 LEAD (`HP:0002039` Anorexia — verify) | 🔎 | |

**Frequency:** near-universal above ~2 Gy. Prodromal nausea/vomiting is the CDC's and REMM's frontline triage sign precisely because it shows up in essentially everyone with a meaningful dose. Use `frequency` bands cautiously — I did not find a clean cohort denominator to cite, and per the repo's frequency-band guidance, a definitional-sounding statement is not a frequency.

### Hematopoietic subsyndrome (H-ARS) — ≥ ~2 Gy

The dominant subsyndrome and the one every approved drug targets. Yamaga et al. (PMID:38333215) on the kinetics:

> "Depending on the dose of ionizing radiation, death of hematopoietic stem and progenitor cells and apoptosis of lymphocytes occur, and lymphopenia becomes apparent within 6-24 hours after radiation exposure."

| Phenotype | HP term | Status | Timing / notes |
|---|---|---|---|
| Decreased total lymphocyte count | `HP:0001888` (label: *Decreased total lymphocyte count*; syn. Lymphopenia) | ✅ OLS4 | **6–24 h.** Earliest measurable change. Lymphocytes die by interphase apoptosis without needing to divide |
| Decreased total neutrophil count | `HP:0001875` (syn. Neutropenia) | ✅ OLS4 | Nadir ~10–21 d |
| Decreased total leukocyte count | `HP:0001882` (syn. Leukopenia) | ✅ OLS4 | |
| Thrombocytopenia | `HP:0001873` | ✅ | Nadir ~2–4 weeks; drives hemorrhage |
| Anemia | `HP:0001903` | ✅ | Latest to appear — RBC lifespan ~120 d |
| Pancytopenia | `HP:0001876` | ✅ | The composite; Orphanet's headline term |
| Aplastic anemia | `HP:0001915` | ✅ | For the irreversible (METREPOL H4) case |
| Bone marrow hypocellularity | `HP:0005528` | ✅ | The histopathologic finding |
| Petechiae | `HP:0000967` | ✅ | Thrombocytopenic bleeding |
| Sepsis | `HP:0100806` | ✅ | **The proximate cause of most H-ARS deaths** |
| Recurrent infections | `HP:0002719` | ✅ | |
| Immunodeficiency | `HP:0002721` | ✅ | |
| Gastrointestinal hemorrhage | `HP:0002239` | ✅ | Overlaps with GI subsyndrome |
| Epilation / alopecia | `HP:0001596` Alopecia | ✅ | ~2–3 weeks; threshold ~3 Gy |

**Severity:** dose-graded, from mild transient cytopenia to irreversible marrow failure. **Progression:** progressive to nadir, then either recovery or not — model as `PROGRESSIVE` through manifest illness. **QoL:** during aplasia, near-total functional dependence — protective isolation, transfusion dependence, high infection risk. Formal EQ-5D/SF-36 data for ARS specifically: 🔎 **not found.** Don't invent one.

### Gastrointestinal subsyndrome (GI-ARS) — ≥ ~6 Gy

Winters & Marzella (PMID:38616048) on the consequence chain:

> "Damage incurred in the latter can lead to nutrient malabsorption, dehydration, electrolyte imbalance, altered microbiome and metabolites, and impaired barrier function, which can lead to septicemia and death."

| Phenotype | HP term | Status |
|---|---|---|
| Diarrhea (severe, often bloody) | `HP:0002014` | ✅ — use `severity: SEVERE` |
| Malabsorption | `HP:0002024` | ✅ |
| Dehydration | `HP:0001944` | ✅ |
| Hypovolemic shock | `HP:0031274` | ✅ |
| Hypotension | `HP:0002615` | ✅ |
| Gastrointestinal hemorrhage | `HP:0002239` | ✅ |
| Weight loss | `HP:0001824` | ✅ |
| Sepsis / septicemia | `HP:0100806` | ✅ |
| Stomatitis / mucositis | `HP:0010280` Stomatitis | ✅ |
| Oral ulcer | `HP:0000155` | ✅ |
| Electrolyte imbalance | 🔎 LEAD | — |

**Timing:** onset within days; death typically 5–10 days at ≥10 Gy. **Prognosis:** without marrow support, uniformly fatal above ~10 Gy — GI-ARS is a *concurrent* syndrome, not a replacement, so the patient has a wrecked gut *and* no white cells at the same time. That combination is why bacterial translocation across a denuded barrier is so reliably lethal.

### Cutaneous radiation syndrome (CRS)

Iddins et al. (PMID:34488201) frame it: "Cutaneous radiation injuries (CRI) or local radiation injuries (LRI) may lead to cutaneous radiation syndrome."

Manifestations, per the search literature: *"skin damages, erythema, altered sensation, itching, edema, blistering, desquamation, ulcer, necrosis, hair loss, and onycholysis."*

| Phenotype | HP term | Status | Approx. skin-dose threshold |
|---|---|---|---|
| Erythema | `HP:0010783` | ✅ | ~2–3 Gy (often biphasic — an early transient wave, then a later one) |
| Alopecia / epilation | `HP:0001596` | ✅ | ~3 Gy |
| Abnormal blistering of the skin | `HP:0008066` | ✅ | ~15–20 Gy (moist desquamation) |
| Skin erosion | `HP:0200041` | ✅ | |
| Skin ulcer | `HP:0200042` | ✅ | ~20–25 Gy |
| Abnormality of the skin (generic parent) | `HP:0000951` | ✅ | |
| Dry desquamation, onycholysis, skin necrosis | 🔎 LEAD | — | ~10 Gy / ~25 Gy |

⚠️ **The dose thresholds in this table came from general secondary sources, not a single citable primary paper I verified.** They're broadly consensus but you need a real citation per row before they go in as evidence-backed claims.

CRS is famously **waves, not a single event** — erythema recurs at intervals over weeks as successive cell populations fail, which is why it fools clinicians who expect a burn to behave like a burn. It's also the subsyndrome most likely to appear *without* whole-body ARS (industrial source handling), and the one most likely to demand surgery.

### Neurovascular / cardiovascular / CNS subsyndrome — very high dose

> "The neurovascular/cardiovascular/central nervous system syndrome occurs at doses >50 Gray and is characterized by watery diarrhea, convulsions, coma, and death within three days of exposure."

| Phenotype | HP term | Status |
|---|---|---|
| Seizure | `HP:0001250` | ✅ |
| Coma | `HP:0001259` | ✅ |
| Confusion | `HP:0001289` | ✅ |
| Ataxia | `HP:0001251` | ✅ |
| Cerebral edema | `HP:0002181` | ✅ |
| Hypotension (refractory) | `HP:0002615` | ✅ |
| Cognitive impairment | `HP:0100543` | ✅ |

**Prognosis: universally fatal.** There is no treatment; management is palliative. Note the dose threshold varies across sources (>20 Gy in some, >50 Gy in others) — 🔎 pin this to a specific citation rather than averaging.

### Delayed effects (DEARE) — survivors

Wu & Orschell's DEARE work (PMID:37014943) documented in mice, after a *sub-threshold* H-ARS dose: *"residual bone marrow damage (RBMD) and progressive renal and cardiovascular DEARE"*, plus *"physiological and neural function, progressive fur graying, ocular inflammation, and malignancy."*

| Late phenotype | HP term | Status | Evidence |
|---|---|---|---|
| Renal insufficiency | `HP:0000083` | ✅ | Gasperetti et al. PMID:36688956 — rats >8 Gy show *"a dose-dependent impairment of renal function as assessed by blood urea nitrogen (BUN) and urine protein to urine creatinine ratio"* |
| Abnormal renal physiology | `HP:0012211` | ✅ | same |
| Pulmonary fibrosis | `HP:0002206` | ✅ | Rat PBI >12 Gy → pneumonitis days 50–100 |
| Cataract | `HP:0000518` | ✅ | Classic late radiation effect (`UBERON:0000965` lens ✅) |
| Cardiomyopathy | `HP:0001638` | ✅ | Coronary rarefaction + endothelial loss in mouse DEARE |
| Leukemia | `HP:0001909` | ✅ | Thymic lymphoma in mouse models; leukemia in A-bomb survivors |
| Neoplasm | `HP:0002664` | ✅ | Solid tumors, long latency |
| Hypothyroidism | `HP:0000821` | ✅ | |
| Male infertility / Azoospermia / Infertility | `HP:0003251` / `HP:0000027` / `HP:0000789` | ✅ | Spermatogonia are exquisitely radiosensitive |
| Xerostomia | `HP:0000217` | ✅ | Salivary gland involvement |
| Cognitive impairment | `HP:0100543` | ✅ | Behavioral DEARE demonstrated in mice — ⚠️ **mouse data; human translation is a `HUMAN_MODEL_MISMATCH` candidate, not a settled human phenotype** |

**Important curation note:** most of the specific DEARE phenotype list is rodent-derived. The Ukrainian ARS survivor cohort (Belyi et al., PMID:20445398) is the human counterpart and covers "over 20 years of health outcomes among confirmed ARS survivors." Cite the human study for human claims; keep the mouse detail tagged `MODEL_ORGANISM`.

---

## 4. Genetic / Molecular Information

### Causal genes: none

State this explicitly in the entry rather than leaving `genetic:` empty and ambiguous. ARS has no causal gene, no pathogenic variant class, no inheritance pattern, no penetrance, no carrier frequency, no founder effect, and no consanguinity role. Every one of those template fields is **not applicable**, and saying so is more useful than silence.

### Somatic / acquired genomic change — the actual "genetics" of ARS

What radiation *does* to the genome is the disease:

- **DNA double-strand breaks** — the lethal lesion. Huang & Zhou (PMID:32355263): *"DNA double-strand breaks are the most lethal lesions induced by ionizing radiation."*
- **Clustered/complex lesions** — multiple damages within one or two helical turns, much harder to repair than isolated breaks. This is why high-LET radiation is disproportionately lethal.
- **Chromosomal aberrations** — dicentrics, rings, translocations, micronuclei. These aren't just damage; they're the **diagnostic assay** (§10).

### Genes as biodosimetry readout (not as cause)

This is the one place a gene list genuinely belongs in the entry — as **`biochemical:` / `BiomarkerReadout` records**, not as `genetic:` causal entries.

The canonical radiation-responsive transcript panel:

| Gene | HGNC | Role |
|---|---|---|
| **FDXR** | **hgnc:3642** ✅ | The most-cited single transcriptional dosimeter |
| **DDB2** | **hgnc:2718** ✅ | DNA damage-binding, p53 target |
| **MDM2** | **hgnc:6973** ✅ | p53 autoregulatory loop |
| **CDKN1A** (p21) | 🔎 LEAD | Cell-cycle arrest effector |
| **AEN**, **BAX**, **BBC3** (PUMA), **GADD45A**, **CCNG1**, **PCNA**, **ACTA2**, **ASCC3**, **WNT3**, **POU2AF1**, **ACTN1** | 🔎 LEAD | Rest of the reported panel |

From the biodosimetry literature: *"Specific radiation-sensitive genes such as FDXR, DDB2, WNT3, and POU2AF1 have become well established for biodosimetry purposes and acute radiation sickness prediction, with FDXR and DDB2 commonly used as biomarkers for retrospective dosimetry within 72 hours after radiation exposure."*

At the protein level: *"When combining FDXR, ACTN1, and DDB2 proteins to estimate radiation dose by linear regression, the combination showed the lowest mean absolute errors (≤0.13 Gy) and highest coefficients of determination (R² = 0.96)."* ⚠️ Verify this against the primary paper before quoting — it came through a search-result layer, not efetch.

### Mechanism-relevant genes (for pathophysiology node binding)

| Gene | HGNC | Where it sits in the chain |
|---|---|---|
| **ATM** | **hgnc:795** ✅ | Apical DSB kinase. Also, unexpectedly, a ferroptosis regulator — Wu et al. (PMID:36752571) show ATM "phosphorylat[es] NCOA4" to control ferritinophagy, *"largely independently of p53 downstream signaling"* |
| **PRKDC** | **hgnc:9413** ✅ | NHEJ catalytic subunit |
| **NBN**, **MRE11** | **hgnc:7652**, **hgnc:7230** ✅ | MRN complex, break sensing |
| **TP53** | **hgnc:11998** ✅ | The apoptosis/arrest decision node |
| **SMPD1** (acid sphingomyelinase) | **hgnc:11120** ✅ | **The ceramide arm.** ASMase-null mice are protected from GI syndrome |
| **MPL** | **hgnc:7217** ✅ | TPO receptor — romiplostim's target |
| **CSF2** (GM-CSF) | **hgnc:2434** ✅ | Sargramostim's ligand |
| **CSF3** (G-CSF) | 🔎 LEAD | Filgrastim/pegfilgrastim |
| **HMGB1** | **hgnc:4983** ✅ | Prototype DAMP |
| **NLRP3** | **hgnc:16400** ✅ | Inflammasome; upregulated post-TBI in minipig ileum |
| **IL1B**, **TNF** | **hgnc:5992**, **hgnc:11892** ✅ | Cytokine amplification |
| **YAP1** | **hgnc:16262** ✅ | Revival stem cell program |
| **GPX4**, **SLC7A11** | 🔎 LEAD | Ferroptosis axis — both downregulated post-irradiation in minipig ileum (PMID:38674120) |
| **LGR5**, **CLU** | 🔎 LEAD | Crypt base columnar ISC marker; revival SC marker |

### Epigenetics

Radiation-induced methylation and chromatin changes are reported in the multi-omics literature (Shakyawar et al., PMID:36368026, catalogs "radiation-induced changes across genomic, transcriptomic, proteomic, metabolomic, and microbiome profiles"), but I found **no ARS-specific epigenetic mechanism with the evidentiary weight to be a pathophysiology node.** 🔎 Treat as an open area, not a claim.

### Chromosomal abnormalities

Acquired only: **dicentric chromosomes** (the biodosimetry gold standard), rings, reciprocal translocations (persistent — used for retrospective dosimetry years later), and micronuclei. None germline.

---

## 5. Environmental Information

This section *is* the etiology, so it carries most of the entry's causal weight. See §2 for the full scenario list.

**Environmental factor to model:**

```yaml
environmental:
- name: Acute whole-body exposure to penetrating ionizing radiation
  exposure_term:
    preferred_term: acute whole-body exposure to penetrating ionizing radiation
    term:
      id: ECTO:7000047          # ✅ VERIFIED
      label: exposure to ionizing radiation
  influences_mechanisms:
  - target: <the DNA damage / energy deposition node>
    environmental_effect: TRIGGERS
    causal_link_type: DIRECT
```

**Note the `preferred_term` is deliberately more specific than the ECTO label** — that's exactly the pattern the repo's ontology contract endorses, since ECTO has no term for the acute high-dose-rate whole-body case.

**Lifestyle factors:** essentially none. Occupation is the real exposure axis (nuclear workers, industrial radiographers, radiotherapy staff, emergency responders, military). Smoking/diet/alcohol are not established modifiers of acute radiation lethality.

**Infectious agents:** not causal — but bacteria are absolutely part of the mechanism. The killing blow in both H-ARS and GI-ARS is usually **endogenous bacterial translocation across a failed gut barrier into a host with no neutrophils.** Yamaga et al. (PMID:38333215) name it: **"lethal sepsis stands as a major contributor to the mortality in ARS."** So the microbiome belongs in the pathograph, and the relevant taxa are commensals gone rogue rather than an outside pathogen.

**Gut microbiome as a bidirectional modifier** — genuinely one of the most interesting recent developments, covered in §6.

---

## 6. Mechanism / Pathophysiology

### The causal chain, step by step

Here's the spine. Branches are marked. Where a step is inferred rather than demonstrated in humans, I say so.

**Step 0 — Energy deposition.** An ionizing photon or particle traverses tissue and deposits energy, both by directly ionizing macromolecules and — for about two-thirds of low-LET damage — by **radiolysis of water**, generating hydroxyl radicals, superoxide, and hydrogen peroxide. → *leads to*

**Step 1 — Clustered DNA lesions, especially double-strand breaks.** DSBs are the lethal lesion (PMID:32355263). Base damage and single-strand breaks are mostly repaired; complex clustered damage is not. → *leads to*

**Step 2 — DNA damage response activation.** MRN complex senses the break; **ATM** (and ATR, DNA-PKcs) phosphorylate H2AX and downstream substrates; CHK1/CHK2 relay; **TP53** is stabilized. → *branches into three fates*:
- **2a — Repair and survive.** NHEJ or homologous recombination rejoins the break; cell cycle resumes.
- **2b — Arrest / senescence.** p53 → CDKN1A/p21 → durable arrest. `GO:0090398` cellular senescence ✅ — observed as p21/waf1 upregulation in irradiated minipig ileum (PMID:38674120).
- **2c — Death.** p53 → BAX/PUMA → mitochondrial outer membrane permeabilization → intrinsic apoptosis (`GO:0008630` ✅). Or, for cells that attempt to divide with unrepaired breaks, **mitotic catastrophe** — which is why proliferating compartments are hit hardest.

**Step 3 (parallel arm, not downstream of Step 2) — the membrane/ceramide pathway.** This one is important and easy to model wrong. Radiation triggers translocation of secretory acid sphingomyelinase (**SMPD1**) into cholesterol/glycosphingolipid rafts of the outer plasma membrane leaflet, where sphingomyelin is hydrolyzed to **ceramide**, which coordinates transmembrane apoptotic signaling. This happens **within hours and does not require nuclear DNA damage signaling** — it's a parallel initiating lesion, and if you draw it downstream of p53 you've inverted the biology.

From Paris et al. and the anti-ceramide follow-up work: *"Extensive endothelial cell apoptosis occurred in the first 4 hours after administering radiation doses sufficient for inducing the GI syndrome (≥15 Gy), while epithelial cell apoptosis occurred several hours after endothelial cell death."* And the causal test: *"Genetic inactivation of ASMase in mice, or intravenous treatment with the endothelial cell survival factor bFGF prior to whole body irradiation, attenuated radiation-induced endothelial apoptosis of the intestinal microvascular system, preserved crypt stem cell clonogens, and protected mice against lethality from the GI syndrome."*

⚠️ This is `MODEL_ORGANISM` evidence and the endothelial-first model has been contested in the field. Curate it as the leading mechanism with an explicit `discussions` entry noting the debate, not as settled fact.

**Step 4 — Selective destruction of self-renewing compartments.** The tissues that lose are the ones that must constantly rebuild: hematopoietic stem/progenitor cells, intestinal crypt stem cells, basal keratinocytes and follicular stem cells, spermatogonia. Plus lymphocytes, which are the exception that proves the rule — they die by interphase apoptosis *without* dividing, which is why lymphopenia is the earliest signal. → *branches into the four subsyndromes*

---

#### Branch A — Hematopoietic ARS (≥ ~2 Gy)

**4A.1** HSPC apoptosis + mitotic death, plus damage to the **bone marrow niche itself** — endothelial and mesenchymal stromal cells, not just the stem cells. This is a relatively recent refinement and matters therapeutically. Vercellino et al. (PMID:38679747) established that a thrombopoietin mimetic works partly through the niche: *"TPOm interacts with BM vascular and stromal niches to locally support hematopoietic reconstitution and systemically improve survival in mice after TBI."* → *leads to*

**4A.2** Loss of proliferative reserve. Nothing dramatic happens yet — this is the latent phase. → *leads to*

**4A.3** Sequential cytopenias as each mature lineage runs out on its own clock: lymphocytes 6–24 h, neutrophils ~10–21 d, platelets ~2–4 wk, red cells latest. → *leads to*

**4A.4** Two convergent failure modes — **infection** (no neutrophils + breached mucosal barriers) and **hemorrhage** (no platelets). → *leads to*

**4A.5** Sepsis, multi-organ failure, death. Or, with support and cytokines, marrow reconstitution and recovery.

#### Branch B — Gastrointestinal ARS (≥ ~6 Gy)

**4B.1** Endothelial apoptosis in the lamina propria microvasculature (Step 3) **plus** direct crypt stem cell clonogen death. → *leads to*

**4B.2** Crypt depopulation. → *leads to*

**4B.3** Villus denudation — enterocytes continue their normal migration up the villus and slough off, and nothing arrives to replace them. Takes ~3–5 days, which sets the syndrome's timing. → *leads to*

**4B.4** Barrier failure + massive fluid/electrolyte loss + malabsorption. → *leads to*

**4B.5** Dysbiosis and bacterial translocation, DAMP release, cytokine amplification. Freeman (PMID:40368913): the field's priorities are *"Understanding intestinal stem cell contributions to recovery, vascular damage mechanisms, and crypt-villus regeneration following irradiation."* → *converges with 4A.4* →

**4B.6** Septicemia and death, typically 5–10 days.

**The regeneration counter-branch** — genuinely exciting recent biology, and the reason GI-ARS may become treatable:
- **Revival stem cells (revSC)** — Ayyaz et al. (PMID:31019301) identified *"a distinct, damage-induced quiescent cell type that we term the revival stem cell (revSC)"*, marked by high clusterin, "extremely rare under homoeostatic conditions," which "reconstitute the LGR5+ CBC compartment and are required to regenerate a functional intestine" via YAP1.
- **Tuft cells as a human reserve pool** — Huang et al. (PMID:39358509): *"tuft cells survive irradiation damage and retain the ability to generate all other epithelial cell types,"* representing *"a damage-induced reserve intestinal stem cell pool in humans."* **Human tissue evidence, which is rare here — weight it accordingly.**
- **Isthmus progenitors** — Malagola et al. (PMID:38848678) argue stemness "resides in the isthmus region" and that "neither de-differentiation nor reserve ISC are drivers of intestinal regeneration." ⚠️ **This directly contradicts the revSC model.** That's a real live controversy and belongs in `mechanistic_hypotheses` with competing `hypothesis_group_id`s, not resolved by fiat.
- **Niche signals** — macrophages drive repair via NRG1 and osteopontin, and "macrophage ablation led to compromised regeneration" (PMID:40086603); a tissue-intrinsic IL-33/EGF circuit promotes epithelial regeneration (PMID:37669929).

#### Branch C — Cutaneous radiation syndrome

**4C.1** Basal keratinocyte and hair-follicle stem cell death + dermal microvascular endothelial injury. → **4C.2** epilation, erythema in waves, dry then moist desquamation, blistering. → **4C.3** at higher dose, ulceration and necrosis, often requiring surgery. → **4C.4** late dermal fibrosis.

When CRS coexists with whole-body dose, you get **radiation combined injury**, where wound healing is itself radiation-impaired — a vicious circle with no approved therapy (PMID:36947602).

#### Branch D — Neurovascular / CNS syndrome (very high dose)

**4D.1** Overwhelming endothelial death and vascular permeability + direct neuronal/glial damage. → **4D.2** cerebral edema, refractory hypotension. → **4D.3** prostration, ataxia, convulsions, coma. → **4D.4** death within ~3 days. Gorbunov & Kiang (PMID:33979447) note "cranial or total-body irradiation can cause a plethora of biochemical and cellular disorders in brain tissues."

---

**Step 5 — Systemic amplification via DAMPs.** Yamaga et al. (PMID:38333215) describe the loop: radiation causes cellular injury through DNA damage and oxidative stress, prompting DAMP release; these molecules then *"interact with pattern recognition receptors, triggering inflammatory responses"*; and *"lethal sepsis stands as a major contributor to the mortality in ARS."* This makes the syndromes non-independent — GI barrier failure feeds the systemic inflammation that worsens everything else. Radiation-induced **multi-organ dysfunction syndrome** is the terminal common path.

**Step 6 — DEARE in survivors** (months to years): residual bone marrow damage, progressive renal failure, pneumonitis→fibrosis, cardiovascular rarefaction and senescence, cataract, cognitive/behavioral change, secondary malignancy.

### The microbiome layer — a real modifier, not decoration

This deserves its own treatment because the evidence is now strong enough to model.

**Guo et al., *Science* 2020 (PMID:33122357)** — the "elite survivor" study. Mice that survived high-dose radiation to live normal lifespans harbored *"distinct gut microbiota that developed after radiation and protected against radiation-induced damage and death."* Elevated **Lachnospiraceae** and **Enterococcaceae** correlated with restored hematopoiesis and GI repair, and — critically — *"these bacteria were also found to be more abundant in leukemia patients undergoing radiotherapy, who also displayed milder gastrointestinal dysfunction"*, which is the human anchor. On the metabolite side: *"Metabolomics revealed increased fecal concentrations of microbially derived propionate and tryptophan metabolites,"* and administering those metabolites "caused long-term radioprotection."

Supporting metabolite work:
- **Propionate** (`CHEBI:17272` ✅) and **butyrate** (`CHEBI:17968` ✅) — short-chain fatty acids.
- **Valeric acid** — Li et al. (PMID:31931652): *"VA exerted the most significant radioprotection among the SCFAs."*
- **Indole-3-carboxaldehyde (I3A)** — Xie et al. (PMID:38706205): I3A *"activated the AhR/IL-10/Wnt signaling pathway to promote intestinal epithelial proliferation."*
- Contrarily, Jiao et al. (PMID:40192235) found raffinose-metabolizing bacteria *impair* hematopoietic recovery via bile acid/FXR/NF-κB — so it cuts both ways.
- And Cook et al. (PMID:36253079) found that antibiotic microbiome depletion did *not* protect against radiation carcinogenesis and actually "shortened the lifespan when Ab were administered before and after TBI" — a useful **REFUTE**-direction evidence item against naive "just sterilize the gut" reasoning.

### Cell death modes beyond apoptosis

**Ferroptosis** is now implicated. Horseman et al. in the Göttingen minipig (PMID:38674120): *"GPX-4 and SLC7A11 were downregulated post-irradiation, consistent with ferroptosis at 6 and 35 days post-irradiation in all groups."* And the ATM–NCOA4–ferritinophagy link (PMID:36752571) connects the DDR kinase directly to iron-dependent death. Also relevant: necroptosis, autophagy, and pyroptosis via NLRP3 — the minipig study found radiation increased *"IL1B, TNFA, CCL2, IL18, and CXCL8, and the inflammasome component NLRP3."*

### Suggested GO / CL bindings for pathophysiology nodes

**Biological processes — all ✅ VERIFIED against `cache/go/terms.csv`:**

| GO ID | Label | Node it fits |
|---|---|---|
| `GO:0006974` | DNA damage response | Step 2 |
| `GO:0006281` | DNA repair | Step 2a |
| `GO:0006302` | double-strand break repair | Step 2a |
| `GO:0072331` | signal transduction by p53 class mediator | Step 2 |
| `GO:0008630` | intrinsic apoptotic signaling pathway in response to DNA damage | Step 2c |
| `GO:0006915` | apoptotic process | Steps 2c, 4A.1 |
| `GO:0006685` | sphingomyelin catabolic process | Step 3 — `modifier: INCREASED` |
| `GO:0046513` | ceramide biosynthetic process | Step 3 — `modifier: INCREASED` |
| `GO:0072577` | endothelial cell apoptotic process | Step 3 / 4B.1 — `modifier: INCREASED` |
| `GO:0006979` | response to oxidative stress | Step 0/1 |
| `GO:0072593` | reactive oxygen species metabolic process | Step 0 |
| `GO:0090398` | cellular senescence | Step 2b |
| `GO:0097707` | ferroptosis | alternate death mode |
| `GO:0070266` | necroptotic process | alternate death mode |
| `GO:0006914` | autophagy | ferritinophagy arm |
| `GO:0006954` | inflammatory response | Step 5 |
| `GO:0045087` | innate immune response | Step 5 |
| `GO:0019221` | cytokine-mediated signaling pathway | Step 5 |
| `GO:0071425` | hematopoietic stem cell proliferation | 4A.2 — `modifier: DECREASED` |
| `GO:0030099` | myeloid cell differentiation | 4A.3 — `modifier: DECREASED` |
| `GO:0030219` | megakaryocyte differentiation | 4A.3 — `modifier: DECREASED` |
| `GO:0038163` | thrombopoietin-mediated signaling pathway | romiplostim target |
| `GO:0050673` | epithelial cell proliferation | 4B.2 — `modifier: DECREASED` |
| `GO:0016055` | Wnt signaling pathway | crypt regeneration |
| `GO:0001525` | angiogenesis | niche recovery |
| `GO:0051882` | mitochondrial depolarization | Step 2c |

**On `modifier` choice:** most of these are genuinely `INCREASED`/`DECREASED` (quantitative), and per the repo's guidance that's the default. Don't reach for `LOSS_OF_FUNCTION` — nothing here is escaping regulatory control; things are simply running above or below normal.

**Cell types — all ✅ VERIFIED against `cache/cl/terms.csv`:**

`CL:0000037` hematopoietic stem cell · `CL:0000049` common myeloid progenitor · `CL:0000557` granulocyte monocyte progenitor cell · `CL:0000556` megakaryocyte · `CL:0000775` neutrophil · `CL:0000542` lymphocyte · `CL:0000084` T cell · `CL:0000236` B cell · `CL:0000115` endothelial cell · `CL:0002139` endothelial cell of vascular tree · `CL:0002250` intestinal crypt stem cell · `CL:0002563` intestinal epithelial cell · `CL:0000584` enterocyte · `CL:0000510` paneth cell · `CL:0002253` epithelial cell of large intestine · `CL:0000312` keratinocyte · `CL:0002559` hair follicle cell · `CL:0000134` mesenchymal stem cell · `CL:0000235` macrophage · `CL:0000216` Sertoli cell · `CL:0000023` oocyte

🔎 LEAD: tuft cell, revival stem cell (no CL term likely exists — use `preferred_term` and leave `term:` off rather than binding something wrong).

**Chemical entities — ✅ VERIFIED:**
`CHEBI:17761` ceramide · `CHEBI:26523` reactive oxygen species · `CHEBI:16240` hydrogen peroxide · `CHEBI:15379` dioxygen · `CHEBI:17272` propionate · `CHEBI:17968` butyrate
🔎 LEAD: hydroxyl radical, superoxide, indole-3-carbaldehyde, valerate/pentanoate.

### Molecular profiling

- **Transcriptomics** — the biodosimetry panels above; single-cell RNA-seq of the irradiated marrow niche (PMID:38679747) and regenerating intestine (PMID:31019301, PMID:38848678).
- **Proteomics** — FDXR/ACTN1/DDB2 plasma panel; a "plasma proteomic biodosimetry approach based on a panel of radiation-responsive biomarkers" for combined injury (PMID:36947602).
- **Metabolomics** — SCFAs, tryptophan/indole metabolites, bile acids.
- **Microbiome** — 16S and shotgun profiling across mouse, minipig, and human radiotherapy cohorts.
- **Multi-omics integration** — Shakyawar et al. (PMID:36368026): *"multi-omic profiles obtained from high-resolution omics platforms offer a holistic approach"* for identifying organ-specific damage biomarkers.
- **Single-cell** — see above. **Spatial transcriptomics** and **CRISPR screens** for ARS specifically: 🔎 not found in this sweep.

**Datasets:** I did not run `just discover-datasets`. Do that before adding any `datasets:` block, and remember the relevance-triage warning — searching "radiation" or a DDR gene will surface a mountain of radiotherapy and cancer datasets that resolve perfectly and have nothing to do with ARS. That's Named Entity Confusion reached through dataset search, and it's a live risk here more than for most diseases.

---

## 7. Anatomical Structures Affected

### Organ level

**Primary (in rough order of radiosensitivity):**

| Structure | UBERON | Status |
|---|---|---|
| Bone marrow | `UBERON:0002371` | ✅ |
| Small intestine | `UBERON:0002108` | ✅ |
| Ileum | `UBERON:0002116` | ✅ |
| Jejunum | `UBERON:0002115` | ✅ |
| Duodenum | `UBERON:0002114` | ✅ |
| Colon | `UBERON:0001155` | ✅ |
| Skin of body | `UBERON:0002097` | ✅ |
| Hair follicle | `UBERON:0002073` | ✅ |
| Thymus | `UBERON:0002370` | ✅ |
| Spleen | `UBERON:0002106` | ✅ |
| Gonad / testis / ovary | `UBERON:0000991` / `UBERON:0000473` / `UBERON:0000992` | ✅ |
| Blood | `UBERON:0000178` | ✅ |

**Secondary / late (DEARE):** lung `UBERON:0002048` ✅ · kidney `UBERON:0002113` ✅ · brain `UBERON:0000955` ✅ · central nervous system `UBERON:0001017` ✅ · lens of camera-type eye `UBERON:0000965` ✅ · thyroid gland `UBERON:0002046` ✅. 🔎 LEAD: heart, oral mucosa, salivary gland, vasculature/microcirculation.

**Body systems:** hematopoietic/immune, gastrointestinal, integumentary, reproductive, then cardiovascular, respiratory, renal, and nervous late.

### Tissue and cell level

Epithelium (intestinal, epidermal, follicular), hematopoietic tissue, vascular endothelium, and lymphoid tissue. The cell list is in §6. The organizing principle worth stating in the entry's prose: **radiosensitivity tracks proliferative rate** (the old Bergonié–Tribondeau observation), **with lymphocytes as the glaring exception** — they're radiosensitive despite being quiescent, because they're primed for apoptosis.

### Subcellular level

- **Nucleus / chromosome** — the DSB target. 🔎 LEAD: `GO:0005634` nucleus, `GO:0005694` chromosome (verify).
- **Plasma membrane lipid rafts** — the ASMase/ceramide platform, and the reason the membrane is a *second independent* target rather than an afterthought. 🔎 LEAD: `GO:0045121` membrane raft (verify).
- **Mitochondrion** — MOMP, ROS amplification, `GO:0051882` mitochondrial depolarization ✅.
- **Lysosome** — ferritinophagy/autophagy arm.

### Localization / lateralization

**Bilateral and systemic by definition** for whole-body exposure. The clinically important exception is **partial-body exposure**, which is common in real accidents (a worker holding a source) and produces **asymmetric, geometry-dependent** injury: severe local cutaneous/deep-tissue damage over the exposed area with relative marrow sparing elsewhere. This isn't a footnote — partial-body geometry is *the* thing that determines whether biodosimetry estimates are even interpretable, and it's why the field built assays that can distinguish partial- from total-body exposure.

---

## 8. Temporal Development

### Onset

**Age:** any. Not congenital, not age-dependent — it's whenever the exposure happens. Occupational cases skew adult; mass-casualty scenarios include all ages, with children at higher risk per unit dose.

**Pattern:** **acute**, sharply. `temporality: ACUTE` is the right qualifier throughout. Prodromal symptoms begin within minutes to 48 hours; the entire syndrome is defined by a single point-source exposure.

### Progression and the phase structure

Covered in §3, but the two things worth restating for a `progression:` block:

1. **Higher dose compresses everything.** The latent period shortens and eventually disappears; time-to-emesis shortens; time-to-death shortens. The phase structure is dose-parameterized, not fixed.
2. **The subsyndromes are concurrent, not sequential.** At 8 Gy a patient has H-ARS and GI-ARS and CRS simultaneously. Modeling them as stages would be wrong. MacVittie & Farese's framing (PMID:32868706) — "concomitant multiple organ injury" — is the right one.

**Duration:** self-limited in one direction or the other within weeks, then either full recovery, recovery-with-DEARE (lifelong), or death.

### Critical intervention windows — the actionable part

| Window | Why it matters |
|---|---|
| **0–6 h** | Time-to-emesis observation; decontamination; first CBC for the lymphocyte baseline; blood draw for cytogenetics *before* transfusion |
| **First 24 h** | Cytokine administration — this is the window every approved MCM was tested in. Romiplostim, TPOm, and pegfilgrastim efficacy studies all dose at ~24 h post-exposure |
| **First 48 h** | Serial CBC q6h for lymphocyte depletion kinetics; HLA typing while lymphocytes still exist |
| **≤72 h** | Transcriptional biodosimetry validity window (FDXR/DDB2) |
| **~3 weeks** | The HSCT decision point. Arnautou & Garnier: transplant "will be carefully considered on an individual basis, especially for patients who do not respond following 3 weeks of cytokine therapy" |
| **Months–years** | DEARE surveillance; no approved DEARE countermeasure exists |

There's a real asymmetry here that the entry should capture: **the drugs work if given early, and the diagnostics work if sampled early, but the patient feels fine during exactly that window.** The latent phase is a trap, and it's the single most operationally important fact about this disease.

### Remission

Recovery is **treatment-assisted, not spontaneous** above ~2 Gy — marrow reconstitution from surviving stem cells, accelerated by cytokines. Below ~2 Gy, spontaneous recovery is the norm. Above ~12 Gy, neither happens.

---

## 9. Inheritance and Population

### Inheritance

**Not applicable.** No inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency. Say so explicitly.

### Epidemiology

**Orphanet prevalence: 1–9 per 1,000,000.** That maps to `prevalence_class: BAND_1_9_PER_1000000` and a `rate_per_100000` of roughly 0.1–0.9 — though honestly a "prevalence" for an accident-driven condition is a strange quantity, and the `notes:` field should say that plainly. It's a rare-disease registry artifact more than an epidemiological measurement.

**Cumulative human experience** (the more meaningful figure), from Lazarus & Gale (PMID:40074513):

> "Radiological accidents/incidents are common with nearly 400 reported since 1944 exposing about 3000 people to substantial doses of ionizing radiations with 127 deaths."

**Chernobyl — the reference case series.** From Belyi et al. (PMID:20445398): *"134 of those were confirmed, including 28 patients who died due to lethal total-body gamma-irradiation."* The fuller picture from IAEA/WNA sources: 237 initially suspected, **134 confirmed by 1989**, doses **0.8–16 Gy**, **28 deaths within 11 to 96 days**, and a further 19 deaths 1987–2004 from causes not necessarily radiation-attributable.

**Goiânia, 1987** — a Cs-137 teletherapy source opened in a scrapyard: ~250 people contaminated, 4 deaths from ARS. The definitive account is the IAEA's *The Radiological Accident in Goiânia*.

**Tokaimura, 1999** — criticality accident at a uranium conversion plant, 2 worker deaths, 436 people dose-assessed.

**Hiroshima/Nagasaki, 1945** — the largest dataset, but combined injury throughout.

**REAC/TS registry inclusion criteria** (useful for understanding what "a case" means): ≥250 mSv to whole body/marrow/gonads, ≥6,000 mSv to skin of extremities, ≥750 mSv to eye or thyroid, or internal contamination above half the maximum permissible body burden.

### Demographics

- **Sex ratio:** no biological sex difference in radiosensitivity is well established for ARS. Observed case series skew male because of occupational composition, not biology. ⚠️ Don't record a sex ratio as a disease property.
- **Geographic distribution:** wherever sources and reactors are. Historical clusters follow accidents, not populations.
- **Age:** children more sensitive; occupational cases adult.
- **Ethnicity:** no established difference.

---

## 10. Diagnostics

ARS has an unusual diagnostic problem: **there is no confirmatory test that's fast, and the fast tests aren't confirmatory.** So triage runs on clinical kinetics while the real dosimetry catches up.

### Clinical dose assessment — the frontline

**Time to emesis.** From the REMM/AFRRI guidance: *"For time to emesis less than 4 hours, the effective whole-body dose is likely to be at least 3.5 Gy"* and *"If time to emesis is less than 1 hour, the whole-body dose probably exceeds 6.5 Gy, and a very complicated and likely fatal medical course may be expected."*

**Lymphocyte depletion kinetics.** Serial absolute lymphocyte counts, ideally q6h for 48 h. The rule of thumb: *"if within the first two days of exposure, lymphocytes have decreased by 50% and are less than 1000 cells per μL, the patient has received at least a moderate dose."* Two formal models exist — the **Andrews Lymphocyte Nomogram** and the **Goans** exponential-decline model (see PMID:17993851, "Estimating radiation dose from time to emesis and lymphocyte depletion").

**METREPOL response categories** — the structured severity system, and a natural fit for a dismech `definitions:` entry with `definition_type: PHENOTYPE_ALGORITHM` and `derivation_basis: ESTABLISHED_CRITERIA`. It grades four organ systems separately — **H** (hematologic), **N** (neurovascular), **C** (cutaneous), **G** (gastrointestinal) — each on a 1–4 scale, and *"identifies the likelihood of 'irreversible' (H4), and 'reversible' (H3, H2, and H1) damage to the bone marrow"*, linking the four to predict multiorgan failure. Lebaron-Jacobs & Herrera-Reyes (PMID:34801995) revisited it 20 years on, asking "if proposed criteria are still relevant for the medical management of radiation-induced injuries" — so treat it as established-but-under-review, with `validation_status.status: UNVALIDATED` unless you find a validation study.

### Biodosimetry — the confirmatory layer

**Dicentric chromosome assay (DCA) — the gold standard.** Jeong et al. (PMID:36543843): *"The dicentric chromosome assay is the 'gold standard' in biodosimetry for estimating radiation exposure."* Its weakness is throughput: it needs a 48-hour lymphocyte culture and manual scoring, which is fine for one patient and hopeless for ten thousand.

The whole recent field is about fixing that:
- **RENEB inter-laboratory comparison 2021** (Endesfelder et al., PMID:37018160): *"In total 33 laboratories from 22 countries around the world participated"*, with all participants successfully classifying extreme doses into clinically relevant exposure groups. This is the network that would actually run a mass-casualty response.
- **RABiT-II high-throughput DCA** (Royba et al., PMID:35994701) — automated, validated under complex exposures including mixed fields.
- **Deep-learning automated scoring** (PMID:36543843, PMID:38687685) — "particularly advantageous in scenarios such as large-scale radiological incidents."
- **G0-PCC (premature chromosome condensation)** multiwell assay (PMID:38854157): *"Our method can address the need for a same-day cytogenetic biodosimetry test in radiation emergency situations."* Same-day is the goal.

**Other cytogenetics:** cytokinesis-block micronucleus assay (faster, less specific); FISH translocation painting (for retrospective dose years later); ring chromosomes.

**Transcriptional/protein biodosimetry:** the FDXR/DDB2/CDKN1A/AEN qPCR panels (§4), valid within ~72 h. Machine-learning combinations — e.g. ACTN1 + DDB2 + FDXR plus B and T cell counts — can *"quantify and distinguish between partial-body irradiation and total-body irradiation exposures"*, which no single marker does.

**Physical dosimetry:** personal dosimeters where worn; EPR spectroscopy of tooth enamel, fingernails, or toenails; OSL of personal electronics; activation analysis (Na-24 in blood) for neutron exposure.

The NIAID program overview is Satyamitra et al. (PMID:37742625), "The NIAID/RNCP Biodosimetry Program: An Overview."

### Routine clinical workup

CBC with differential q6h × 48 h then daily; comprehensive metabolic panel; serum amylase (rises with salivary gland dose); C-reactive protein; blood/urine/stool cultures; **HLA typing early** (do it while there are still lymphocytes to type); type and screen. Imaging as clinically indicated. Skin photography with serial documentation and mapping for CRS. Biopsy is rarely needed for diagnosis but marrow biopsy documents hypocellularity.

**LOINC-coded lab observations** for a `biochemical:` block: absolute lymphocyte count, absolute neutrophil count, platelet count, hemoglobin. 🔎 I did not resolve specific LOINC codes — look them up rather than guessing, and note the repo's memory that LOINC does *not* carry reference ranges as a field.

### Genetic testing

**Not applicable for diagnosis.** ARS is not a genetic disease. Genetic testing has one narrow role: if a patient shows radiation toxicity grossly disproportionate to estimated dose, consider a DNA-repair-deficiency syndrome (ATM, NBN, LIG4, etc.) — that's a rare-but-real scenario and worth a sentence, not a section. WGS/WES/panels/CMA/karyotype/FISH/mtDNA/repeat expansion: all not applicable. (Note the irony that **karyotyping is central here** — just as a dosimeter, not a genetic test.)

### Differential diagnosis

This is where ARS actually gets missed, because a patient with nausea, vomiting, and falling counts and no exposure history looks like ten other things. Ebeling et al. built a whole simulation curriculum around exactly this (PMID:37538304): "ARS is a high-risk, low-frequency diagnosis that can be fatal and is difficult to diagnose without an obvious history of ionizing radiation exposure."

| Differential | Distinguishing feature |
|---|---|
| Viral gastroenteritis / food poisoning | No progressive lymphopenia; no dicentrics |
| Chemotherapy toxicity / drug-induced marrow suppression | Drug history; different cytopenia kinetics |
| Idiopathic aplastic anemia | Insidious onset; no prodrome; no exposure |
| Sepsis from another source | Cultures; no cytogenetic damage |
| Thrombotic thrombocytopenic purpura | Schistocytes, ADAMTS13 |
| Thermal or chemical burn | CRS is delayed, recurs in waves, and doesn't match a contact pattern |
| Acute leukemia | Blasts on smear/marrow |

The tell that separates ARS from all of them is the **combination of a compressed prodrome, a deceptively well latent period, dose-proportional lymphocyte decline, and dicentric chromosomes.** Nothing else does all four.

### Screening

No population screening — there's no pre-symptomatic state to screen for. "Screening" in the ARS context means **mass-casualty triage biodosimetry**: rapidly sorting thousands of worried-well from the genuinely exposed. That's the entire design driver behind RABiT-II, the G0-PCC assay, and the qPCR panels.

---

## 11. Outcome / Prognosis

### Survival

Prognosis is a nearly pure function of dose, medical care, and combined injury.

| Dose band | Expected course |
|---|---|
| <1 Gy | Minimal to no clinical effect; "Radiation doses below 2 Gray generally result in insignificant clinical consequences" (PMID:39025400) |
| 1–2 Gy | Mild prodrome, mild cytopenia, recovery expected |
| 2–6 Gy | H-ARS; survivable with aggressive supportive care + cytokines; mortality climbs steeply with dose |
| 6–10 Gy | H-ARS + GI-ARS; survival possible at the low end with maximal care, poor at the high end |
| 10–12 Gy | Very poor; GI-ARS typically fatal within ~10 days |
| >12 Gy | *"exceeds current therapeutic capacities"* (PMID:39025400) |
| >20–50 Gy | Neurovascular syndrome; uniformly fatal within days |

**Human LD50/60:** ~2.7–3.1 Gy marrow dose without medical care (A-bomb data, DS02); commonly quoted as ~4.5 Gy with modern care, though as noted in §2 that higher figure is soft.

**NHP LD50/60 with medical management: 7.52 Gy** (Farese et al., PMID:22929469): *"The study defined an LD30/60 of 7.06 Gy, LD50/60 of 7.52 Gy, and an LD70/60 of 7.99 Gy."* ⚠️ Do **not** present this as a human number — the macaque with full supportive care is roughly twice as tolerant as an unsupported human, and conflating the two is an easy and serious error.

**Cause of death:** in H-ARS, infection and hemorrhage during aplasia. In GI-ARS, sepsis from bacterial translocation plus fluid/electrolyte collapse. In CNS syndrome, cerebral edema and cardiovascular collapse.

### Morbidity and function

Survivors face DEARE — progressive renal impairment, pulmonary fibrosis, cardiovascular disease, cataract, endocrine dysfunction, infertility, cognitive/behavioral change, and elevated cancer risk. Gasperetti et al. (PMID:36688956) drive the point home: *"These data show survivors of H-ARS are at risk for the development of delayed renal toxicity and emphasize the need for the development of medical countermeasures for delayed renal injury."* The Ukrainian ARS survivor cohort (PMID:20445398) is the long human record.

There's a structural irony worth writing into the entry: **as H-ARS treatment improves, DEARE becomes a bigger problem, because more people survive to develop it.** Wu et al. (PMID:37014943) note that "while effective medical countermeasures (MCM) for the hematopoietic-acute radiation syndrome (H-ARS) have been identified and approved by the FDA, development of MCM for DEARE has not yet been successful." We got good at the first act and never wrote the second.

**QoL instruments:** 🔎 No ARS-specific validated instrument found. EQ-5D/SF-36/PROMIS data for this population: not located.

### Prognostic factors

Absorbed dose and its uniformity; time to emesis; lymphocyte depletion slope; METREPOL response category (especially H4 = irreversible marrow damage); presence of combined injury (major adverse factor); age; comorbidity; internal contamination; time from exposure to cytokine administration.

**Prognostic biomarkers:** dicentric frequency; ALC nadir and slope; the FDXR/DDB2 transcript panel; 🔎 candidate protein panels not yet clinically qualified.

---

## 12. Treatment

### The frame

There is no antidote. Treatment is: **replace what the marrow can't make, push what's left to regenerate faster, keep infection out, and manage the gut and skin.** Everything approved is in the second category.

### FDA-approved medical countermeasures

All licensed under the **Animal Rule** — no human efficacy trials exist or can exist. Indication wording is consistently *"acute exposure to myelosuppressive doses of radiation."* From REMM's countermeasure page:

| Drug | Brand | Approved | Dose | Mechanism |
|---|---|---|---|---|
| **Filgrastim** | Neupogen | Mar 2015 | 10 mcg/kg/day SC | G-CSF; neutrophil recovery |
| **Pegfilgrastim** | Neulasta | Nov 2015 | two 6 mg SC doses, 1 wk apart (≥45 kg) | Pegylated G-CSF |
| **Sargramostim** | Leukine | Mar 2018 | 7–12 mcg/kg/day SC | GM-CSF |
| **Romiplostim** | Nplate | **28 Jan 2021** | 10 mcg/kg **single** SC dose | TPO receptor agonist; platelet recovery |
| Pegfilgrastim-cbqv | Udenyca | Nov 2022 | as Neulasta | biosimilar |
| Pegfilgrastim-fpgk | Stimufend | Sep 2023 | as Neulasta | biosimilar |
| Pegfilgrastim-bmez | Ziextenzo | Feb 2024 | as Neulasta | biosimilar |
| Filgrastim-txid | Nypozi | Jun 2024 | as Neupogen | biosimilar |
| Filgrastim-sndz | Zarxio | Oct 2024 | as Neupogen | biosimilar |
| Pegfilgrastim-pbbk | Fylnetra | Apr 2025 | as Neulasta | biosimilar |
| Filgrastim-ayow | Releuko | Apr 2025 | as Neupogen | biosimilar |
| Pegfilgrastim-unne | Armlupeg | Nov 2025 | as Neulasta | biosimilar |

⚠️ **Verify the biosimilar approval dates against FDA sources before committing them** — they came from a single page fetch and dates are exactly the kind of thing that gets transcribed wrong.

**Romiplostim is the mechanistically distinct one** and worth its own treatment record. It targets the platelet arm rather than the neutrophil arm — Bussel et al. (PMID:34079225): *"Romiplostim binds to and activates the TPO receptor on megakaryocyte precursors, thus promoting cell proliferation and viability, resulting in increased platelet production."* The pivotal NHP data (Bunin et al., PMID:37224926) showed a **"40% to 55% survival benefit compared with controls, less severe clinical signs, reduced incidence of thrombocytopenia and/or neutropenia."** Single dose, which matters enormously for mass-casualty logistics.

Lazarus & Gale's clinical bottom line (PMID:40074513): *"The favorable benefit-to-risk ratio of these drugs over hematopoietic cell transplants suggests giving them soon after exposure to acute high-dose and-dose-rate whole body ionizing radiations."*

### Suggested treatment YAML shape

```yaml
treatments:
- name: Filgrastim
  therapeutic_modality: OTHER        # 🔎 no ideal value; G-CSF is a recombinant protein
  treatment_term:
    preferred_term: Pharmacotherapy
    term:
      id: NCIT:C15986                # ✅ VERIFIED
      label: Pharmacotherapy
    therapeutic_agent:
    - preferred_term: filgrastim
      term:
        id: NCIT:C1474               # ✅ VERIFIED in cache/ncit/terms.csv
        label: Filgrastim
```

⚠️ **Two traps here.**
1. There's a known pattern in this repo where **NCIT drug terms fail `therapeutic_agent` dynamic-enum validation** even when the CURIE and label are both correct — CHEBI is the safer default. But filgrastim/pegfilgrastim/sargramostim/romiplostim are recombinant proteins and peptibodies with no CHEBI terms, so NCIT is the only option. **Run `just validate-terms` on this block specifically** and be ready for it to fail.
2. `therapeutic_modality` has no value that cleanly fits a recombinant cytokine. `PROTEIN_REPLACEMENT` is wrong (nothing is being replaced), `SMALL_MOLECULE` is wrong. `OTHER` is honest. Don't stretch a value to look complete.

**Verified NCIT terms for the rest:**

| Treatment | NCIT | Status |
|---|---|---|
| Supportive Care | `NCIT:C15747` | ✅ |
| Pharmacotherapy | `NCIT:C15986` | ✅ |
| Hematopoietic Cell Transplantation | `NCIT:C15431` | ✅ |
| Bone Marrow Transplantation | `NCIT:C15194` | ✅ |
| Blood Transfusion | `NCIT:C15192` | ✅ |
| Platelet Transfusion | `NCIT:C15366` | ✅ |
| Antibiotic Therapy | `NCIT:C15620` | ✅ |
| Antifungal Therapy | `NCIT:C15704` | ✅ |
| Antiviral Therapy | `NCIT:C16119` | ✅ |
| Fluid Therapy | `NCIT:C116537` | ✅ |
| Nutritional Support | `NCIT:C15433` | ✅ |
| Wound Care Management | `NCIT:C116681` | ✅ |
| Skin Transplantation | `NCIT:C15325` | ✅ |
| Surgical Procedure | `NCIT:C15329` | ✅ |
| Therapeutic Procedure | `NCIT:C49236` | ✅ |
| Palliative Therapy | `NCIT:C15292` | ✅ |
| Filgrastim / Sargramostim / Romiplostim | `NCIT:C1474` / `NCIT:C1492` / `NCIT:C52183` | ✅ |
| Pegfilgrastim | `NCIT:C1854` | ✅ (OLS4) |

Reminder from the repo's own guidance: `NCIT:C15433` Nutritional Support should **not** be reflexively tagged `BEHAVIORAL` — here it usually means parenteral nutrition, which isn't a diet-pattern change.

### Supportive care backbone

This is where survival actually comes from, and it deserves as much detail as the drugs:
- **Protective/reverse isolation** during neutropenia
- **Broad-spectrum antimicrobial prophylaxis and treatment** — antibacterial, antifungal, antiviral
- **Transfusion support** — and here's the ARS-specific detail that matters: **all cellular blood products must be irradiated** to prevent transfusion-associated GVHD, because a profoundly lymphopenic irradiated patient cannot reject donor lymphocytes. Leukoreduced and CMV-safe as well. This is a genuine ARS-specific practice point, not generic transfusion medicine
- **Antiemetics** — 5-HT3 antagonists; ondansetron `CHEBI:7773` ✅
- **Fluid and electrolyte replacement**, especially in GI-ARS
- **Nutritional support**, often parenteral when the gut is denuded
- **Analgesia** and **wound care** for CRS; surgical debridement, grafting, sometimes amputation
- **Psychosocial support** — the Chernobyl and Goiânia experiences both document severe psychological morbidity, including in the unexposed

### Hematopoietic cell transplantation

Reserved and controversial. Arnautou & Garnier: HSCT *"will be carefully considered on an individual basis, especially for patients who do not respond following 3 weeks of cytokine therapy."* The Chernobyl transplant experience was poor — GVHD in the setting of combined injury, plus autologous recovery in patients who'd been transplanted anyway. The modern consensus leans strongly toward cytokines first.

### Investigational — the pipeline

**Hematopoietic:**
- **TPOm (JNJ-26366821)**, a PEGylated thrombopoietin mimetic — works through the niche (PMID:38679747): *"TPOm interacts with BM vascular and stromal niches to locally support hematopoietic reconstitution."*
- **HemaMax (rHuIL-12)** — Phase 1 completed, **NCT01742221**, "Hematopoietic syndrome due to acute radiation syndrome"
- **PLX-R18** placental cell therapy — Phase 1, **NCT03797040**, for post-exposure prophylaxis or treatment of HS-ARS
- **KMRC011** — Phase 1 completed, **NCT03585803**, listed condition "Acute radiation syndrome"
- **16,16-dimethyl PGE2** — effective as radio*protector* but notably **not** as a mitigator for DEARE (PMID:37014943): given after TBI it "enhances survival from H-ARS but has little impact on RBMD or other DEARE." A nice worked example of `directness` mattering
- **Eltrombopag** post-TBI — **NCT00903929**, Phase 1, completed

**Radioprotectors (pre-exposure):**
- **BIO 300** (synthetic genistein nanosuspension) — NHP pilot (PMID:39160790): all four treated animals survived to day 60 vs 50% of vehicle controls, but notably *"BIO 300 Injectable Suspension did not mediate an improvement in blood cell counts,"* and the authors conclude "protection against irradiation is attainable without much improvement in the complete blood count (CBC) profile." Oral suspension Phase 1 **NCT06741345** completed Dec 2024. ⚠️ n=4 per arm — a pilot, not efficacy
- **5-androstenediol / NEUMUNE** (PMID:38097137) — IND status granted; "modulate[s] cell cycle progression, reduces radiation-induced apoptosis, and regulates DNA repair"
- **Gamma-tocotrienol**, **amifostine** (`CHEBI:2636` ✅, active metabolite WR-1065 `CHEBI:72583` ✅ — but amifostine is approved only for radiotherapy-related xerostomia and cisplatin nephrotoxicity, **not** ARS)

**GI-targeted:**
- **MIIST305**, a mucus-layer glycopolymer (PMID:39930324) — the standout result: *"Approximately 85% of the animals survived the irradiation exposure... In contrast, no control, Vehicle-treated animals survived past day 10 at this radiation dose."*
- **Anti-ceramide scFv** (Nagesh et al., PMID:37815783) — mechanistically the most elegant thing in the pipeline, targeting the Step-3 ceramide arm directly. Mice at 15 Gy + BMT + scFv survived to day 90 with *"normal appearance, behavior, and serum biochemistries, and surprisingly, at full autopsy, near-normal physiology in all 42 tissues examined"*
- **Captopril** (`CHEBI:3380` ✅) — ACE inhibitor, mitigates H-ARS in Göttingen minipigs (PMID:34449797, PMID:38674120); "suppressed radiation-induced IL1B and TNFA"
- **Microbial metabolites** — propionate, tryptophan metabolites, I3A, valeric acid (§6)
- **Liangxue-Guyuan-Yishen decoction** — a TCM formulation with GI-ARS rat data via WNT and MEK/ERK (PMID:37697698)

**Cell and EV therapies:**
- **MSCs and MSC-derived extracellular vesicles** (Miura & Fujii, PMID:39679884) — promising preclinically, but the authors are appropriately cautious: *"the effectiveness of MSC transplantation in addressing acute radiation syndrome affecting organs in irradiated individuals is limited"* and "further investigation is required"
- **Umbilical cord blood** (Hurley et al., PMID:37967239) — improved survival, hematopoietic recovery, reduced GI damage, and mitigation of pneumonitis/fibrosis in preclinical work
- **Romiplostim-induced EVs** (Yamaguchi et al., PMID:37238707) — a genuinely odd and interesting result: serum EVs from romiplostim-rescued mice, transferred to other irradiated mice, *"drastically improved by 50-100%"* their 30-day survival, with miR-144-5p found only in EVs from treated animals

**Combined injury: nothing.** Worth stating as an explicit gap (PMID:36947602).

### Treatment algorithms

Follow the METREPOL response category. Broadly: decontaminate → assess dose (clinical + biodosimetry) → cytokines within 24 h if dose >2 Gy → supportive care scaled to RC → HSCT decision at ~3 weeks for non-responders → DEARE surveillance for survivors.

**Pharmacogenomics:** none established for ARS. `NOT_APPLICABLE`.

**Personalized medicine:** dose-guided rather than genotype-guided. The "biomarker" here is absorbed dose, and the whole biodosimetry enterprise exists to make treatment personalized in that sense.

---

## 13. Prevention

### Primary prevention — where nearly all the real benefit lives

- **Radiation protection fundamentals:** time, distance, shielding. ALARA.
- **Source security and regulatory control** — the Goiânia accident happened because a teletherapy source was abandoned in an unsecured building. *"A caesium-137 teletherapy unit was left unsecured after an institute moved to new premises, becoming totally insecure."* Every orphan-source accident is a regulatory failure before it's a medical one.
- **Reactor safety, criticality controls, transport regulation** (IAEA framework)
- **Emergency planning** — sheltering, evacuation, exclusion zones
- **Occupational dosimetry and dose limits**
- **Nuclear nonproliferation and counterterrorism** — the actual primary prevention for the scenarios driving current funding

**Pharmacological primary prevention: none approved.** Restating Singh et al. (PMID:39160790): *"Currently, there is no radiation medical countermeasure approved by the U.S. FDA which can be used before radiation exposure to protect exposed individuals."*

### The KI distinction, one more time

**Potassium iodide** (`CHEBI:8346` ✅) is thyroid-blocking prophylaxis against radioiodine uptake. It is on every emergency-planning list and is **not** ARS prophylaxis. If the KB entry lists it under `treatments:` without a scoping note, a reader will reasonably conclude it protects against whole-body exposure. It does not. Same logic for **Prussian blue** (Cs/Tl decorporation) and **Ca-DTPA/Zn-DTPA** (transuranic decorporation) — these are for internal contamination, which is a different disease process with a different time course. Consider `ECTO:9000084` "exposure to iodine" ✅ if you model the radioiodine arm at all, and consider whether internal contamination deserves a `differentials:` entry rather than a treatment entry.

### Secondary prevention

Mass-casualty triage biodosimetry (§10) — rapid identification of who actually got a dose so countermeasures go to the right people and the worried-well don't consume the supply.

### Tertiary prevention

Countermeasure administration within the therapeutic window; infection prophylaxis; irradiated blood products; **DEARE surveillance** — renal function, pulmonary function, ophthalmologic exam, cardiovascular risk management, cancer screening. The Ukrainian ARS survivor cohort is the model for this.

### Immunization

Not applicable — no vaccine, no infectious etiology. (Standard vaccination status matters for a neutropenic patient's infection risk, but that's not ARS prevention.)

### Genetic screening and counseling

**Not applicable.** No carrier screening, no PGD, no prenatal testing. `NCIT:C15240` Genetic Counseling ✅ has a vanishingly narrow role — only if a DNA-repair syndrome is uncovered incidentally through disproportionate radiosensitivity.

### Public health

Emergency preparedness training (the simulation curricula like PMID:37538304 exist because clinicians genuinely don't recognize this), stockpiling (Strategic National Stockpile holds the approved cytokines), risk communication, environmental monitoring and remediation, food/water controls after a release.

---

## 14. Other Species / Natural Disease

### Taxonomy

**Every mammal gets ARS**, with the same subsyndrome structure and different dose thresholds. Verified taxon IDs from `cache/ncbitaxon/terms.csv`:

`NCBITaxon:9606` *Homo sapiens* ✅ · `NCBITaxon:10090` *Mus musculus* ✅ · `NCBITaxon:10116` *Rattus norvegicus* ✅ · `NCBITaxon:9544` *Macaca mulatta* ✅ · `NCBITaxon:9615` *Canis lupus familiaris* ✅ · `NCBITaxon:9823` *Sus scrofa* ✅ · `NCBITaxon:9825` *Sus scrofa domesticus* ✅ · `NCBITaxon:7955` *Danio rerio* ✅

🔎 LEAD: *Macaca fascicularis* (cynomolgus).

### Comparative radiosensitivity

Species differ substantially in LD50 — dogs are notably more radiosensitive than mice, primates intermediate. ⚠️ I did not find a single citable modern comparative table, and the numbers floating around secondary sources vary with dose rate, strain, and supportive care. **Don't tabulate species LD50s without a primary citation per row.** One 2025 paper directly compares macaque species ("Comparison of sensitivity of rhesus and cynomolgus macaque for acute radiation effects", *Sci Rep*) — worth chasing for a proper citation.

### Natural disease in other species

**Yes, and it's documented.** Cannon & Kiang (PMID:32663058) reviewed wildlife after Chernobyl and Fukushima: *"Humans were evacuated from the immediate regions but the wildlife stayed and continued to be affected."* Their review covers effects on "vegetation, insects, fish, birds and mammals," and notes that "adaptation to radiation is evident and the ecosystems have dynamically changed."

Domestic animals in the Chernobyl exclusion zone experienced ARS. There is no established naturally occurring animal ARS outside of accidental exposure — no OMIA entry, because it isn't a genetic condition.

**VBO breed identifiers:** not applicable — no breed predisposition.

**Orthologous genes:** the DDR is deeply conserved (ATM, TP53, the MRN complex, NHEJ machinery all have orthologs from yeast through mammals), which is exactly why model organisms work here. 🔎 Specific NCBI Gene IDs not retrieved.

### Zoonosis / transmission

**Not applicable.** ARS is not transmissible. Worth stating explicitly, because there is a persistent public misconception that irradiated people are themselves radioactive. They are not — unless they carry *internal or external contamination*, which is a separate and real concern for responders. That distinction (irradiation ≠ contamination) is worth a `notes:` line; it's the single most consequential public-understanding error about this disease.

---

## 15. Model Organisms

Because of the Animal Rule, model organisms aren't a supporting line of evidence here — **they are the regulatory basis for every approved therapy.** That inverts the usual weighting and should be said in the entry.

### The consortium context

**MCART** (Medical Countermeasures Against Radiological Threats), NIAID-sponsored, is the organizing body: *"charged with developing medical countermeasures (MCM) to treat the key sequelae of acute radiation syndrome (ARS) and the delayed effects of acute radiation exposure (DEARE)."* Its models are built "within the criteria of the FDA's 'animal rule.'" Key reference: MacVittie & Farese, PMID:32868706, "Defining the Concomitant Multiple Organ Injury within the ARS and DEARE in an Animal Model Research Platform."

### Models

**Mouse — `NCBITaxon:10090` ✅**
- **C57BL/6J TBI** — the workhorse H-ARS model, 30-day survival endpoint, LD50/30 typically ~7–8 Gy strain- and facility-dependent
- **Partial-body irradiation with 5% bone marrow shielding at 13 Gy** — the standard GI-ARS model (PMID:39930324). The shielding is the whole trick: without it the animal dies of H-ARS before GI-ARS can be studied
- **15 Gy WBI** — the ~90% GI-ARS lethal dose for C57BL/6J (PMID:37815783)
- **ASMase-knockout (Smpd1−/−)** — the genetic proof of the ceramide arm
- **DEARE longitudinal model** — mice followed to 12+ months (PMID:37014943)
- *Recapitulation:* excellent for H-ARS kinetics and mechanism. *Limitations:* small body mass changes dosimetry; different marrow reserve; supportive care not comparable to human ICU; 30-day endpoint misses DEARE by design

**Rat — `NCBITaxon:10116` ✅**
- **WAG/RijCmcr** — Gasperetti et al. (PMID:36688956) established it "as an effective model for the evaluation of medical countermeasures (MCM) for acute hematologic radiation syndrome (H-ARS)." LD50/30 determined for adult *and* pediatric animals, both sexes. *"87.5% and 100% of adult rats succumb to lethal hematopoietic acute radiation syndrome (H-ARS) at TBI doses of 8 and 8.5 Gy, respectively"*, and pegfilgrastim *"improved 30 d survival from 12.5% to 83% at 8 Gy and from 0% to 63% at 8.5 Gy."*
- **The best DEARE model** — followed to 300 days with renal endpoints. Lung-DEARE at PBI >12 Gy (pneumonitis days 50–100); kidney-DEARE at >8 Gy (BUN >120 mg/dL)

**Non-human primate — `NCBITaxon:9544` ✅ (rhesus); cynomolgus 🔎**
- **The pivotal licensure model.** Farese et al. (PMID:22929469): 48 rhesus macaques, blinded and randomized, LD30/60 7.06 Gy, **LD50/60 7.52 Gy**, LD70/60 7.99 Gy, with supportive care, "with a relatively steep slope of 1.13 probits per linear dose"
- Different radiation sources give different curves — a LINAC 6MV photon study reported LD30/50/70 of 5.71 / 6.78 / 7.84 Gy. **Source and dose rate are not interchangeable**
- *Recapitulation:* the closest to human physiology and supportive care. *Limitations:* cost, ethics, small n (the BIO 300 study had **four animals per arm**), and macaques with full care substantially out-tolerate unsupported humans

**Minipig — `NCBITaxon:9823` / `NCBITaxon:9825` ✅**
- **Göttingen minipig H-ARS** — captopril studies at 1.79–1.80 Gy Co-60 (PMID:34449797, PMID:38674120); skin physiology is the closest available to human, making it the preferred CRS model
- **Sinclair minipig GI-ARS** — dose-finding with microbiome and inflammasome endpoints (PMID:39012765)
- ⚠️ **Provenance caution:** the two Kenchegowda/Seed/Singh minipig methodology papers (PMID:34402700, PMID:32892657) came back with one flagged **RETRACTED**. Check retraction status before citing either

**Canine — `NCBITaxon:9615` ✅** — historical importance (much of the classical dose-response and marrow-transplant work), less used now.

**Zebrafish — `NCBITaxon:7955` ✅** — 🔎 not prominent in the ARS literature I sampled; more common for developmental radiobiology.

**In vitro / NAM systems:**
- **Human intestinal organoids** — used to validate the macrophage/NRG1 regeneration finding (PMID:40086603) and the human tuft-cell reserve pool (PMID:39358509). These belong in `experimental_models:` (not `animal_models:`)
- **Human intestinal resection tissue** — the strongest evidence tier available for GI mechanism
- **Hematopoietically humanized mice** — used for candidate protein biodosimetry markers
- **Primary human lymphocyte culture** — the substrate for the dicentric assay itself

### Modeling these in dismech

Use `ModelMechanismLink` on `animal_models:` entries (this is what `modeled_mechanisms` is for — animal models never belong in `experimental_models:`). Sketch:

```yaml
animal_models:
- name: Rhesus macaque total-body irradiation with medical management
  species: Rhesus macaque
  publication: PMID:22929469
  modeled_mechanisms:
  - target: <the H-ARS marrow failure node>
    relationship: RECAPITULATES
    fidelity: HIGH
    description: >-
      Dose-response for hematopoietic lethality with supportive care;
      the licensure model for every FDA-approved H-ARS countermeasure.
    limitations: >-
      LD50/60 of 7.52 Gy with full supportive care substantially exceeds the
      human LD50/60 of roughly 2.7-3.1 Gy estimated from atomic-bomb survivor
      marrow doses, so the dose axis does not transfer directly to humans.
    readouts:
    - name: 60-day survival
      target: <same node>
      direction: DECREASED
```

And there's at least one good `FAILS_TO_RECAPITULATE` / `HUMAN_MODEL_MISMATCH` candidate here: **the behavioral and cognitive DEARE findings in mice** (PMID:37014943 — anxiety changes in females, blunted shock flinch, altered exploratory behavior in males) have no established human counterpart. That's exactly the "evidence exists in a model, translational validity is the open question" shape the schema's `HUMAN_MODEL_MISMATCH` was built for.

### Model resources

MGI, RGD, ZFIN, Alliance of Genome Resources for the standard organism databases; MCART for consortium models; NIAID/RNCP for the countermeasure program.

---

## Gaps and honest non-findings

Things I looked for and did not find, so nobody re-runs the same search:

- **A validated QoL instrument** for ARS. None found. EQ-5D/SF-36/PROMIS data: absent.
- **An ARS-specific epigenetic mechanism** with enough weight to be a pathophysiology node.
- **Spatial transcriptomics or CRISPR screens** specific to ARS.
- **A clean modern comparative species LD50 table** with a citable primary source.
- **A definitive ICD-11 code.** One source said `NF00`, the template guessed `NF06`. Unresolved.
- **A DOID identifier.**
- **Human efficacy data for any ARS drug.** By construction — the Animal Rule exists because this data cannot exist.
- **Recent ClinicalTrials.gov ARS-condition trials** are sparse: NCT01742221 (HemaMax), NCT03585803 (KMRC011), NCT03797040 (PLX-R18), NCT00903929 (eltrombopag), NCT06741345 (BIO 300 oral, Phase 1). Most `acute radiation syndrome` query hits are TBI-conditioning transplant trials, which are a different thing wearing similar words — classic Named Entity Confusion, and worth a note in the entry so the next curator doesn't fall in.
- **LOINC codes** for the ARS lab panel — not resolved.

---

## Suggested curation approach, briefly

Some structural calls that follow from the above:

1. **`entry_type: DISEASE`.** ARS is a real clinical entity with a defined mechanism, not a grouping — even though it bundles four subsyndromes.
2. **Model the four subsyndromes as `has_subtypes`**, not separate entries. They share one etiology, one dose axis, and one temporal architecture; they differ only in which tissue's threshold you crossed. Names should be short and slug-friendly: `H-ARS`, `GI-ARS`, `CRS`, `CNS-ARS`. Then use the `subtype:` foreign key on phenotypes and progression records.
3. **The initiating node is the exposure**, wired via `environmental[].influences_mechanisms` with `TRIGGERS`. If it isn't wired, the pathograph will have every mechanism node orphaned from its cause — one of the recurring reviewer findings in this repo.
4. **Watch for module conformance opportunities.** `just list-modules` before you build anything — cellular senescence, inflammaging, and any fibrosis or DAMP/inflammation module are plausible conformance targets, and there may be a toxicology-family module that already covers part of this chain under a name you wouldn't guess.
5. **Give the "irradiation ≠ contamination" distinction and the "KI is not ARS prophylaxis" distinction each a `notes:` line.** They're the two errors most likely to be introduced by a future well-meaning editor.
6. **Expect heavy `MODEL_ORGANISM` grading and don't apologize for it** — but keep the human accident evidence (Chernobyl, Goiânia, Tokai-mura, A-bomb) carrying the human phenotype claims.

---

## Sources

**Primary literature (PMIDs cited above):**
[40368913](https://pubmed.ncbi.nlm.nih.gov/40368913/) · [39025400](https://pubmed.ncbi.nlm.nih.gov/39025400/) · [38616048](https://pubmed.ncbi.nlm.nih.gov/38616048/) · [39930324](https://pubmed.ncbi.nlm.nih.gov/39930324/) · [39000080](https://pubmed.ncbi.nlm.nih.gov/39000080/) · [40074513](https://pubmed.ncbi.nlm.nih.gov/40074513/) · [37280005](https://pubmed.ncbi.nlm.nih.gov/37280005/) · [38679747](https://pubmed.ncbi.nlm.nih.gov/38679747/) · [39679884](https://pubmed.ncbi.nlm.nih.gov/39679884/) · [37967239](https://pubmed.ncbi.nlm.nih.gov/37967239/) · [39160790](https://pubmed.ncbi.nlm.nih.gov/39160790/) · [37238707](https://pubmed.ncbi.nlm.nih.gov/37238707/) · [36688956](https://pubmed.ncbi.nlm.nih.gov/36688956/) · [38097137](https://pubmed.ncbi.nlm.nih.gov/38097137/) · [37014943](https://pubmed.ncbi.nlm.nih.gov/37014943/) · [38674120](https://pubmed.ncbi.nlm.nih.gov/38674120/) · [37815783](https://pubmed.ncbi.nlm.nih.gov/37815783/) · [37697698](https://pubmed.ncbi.nlm.nih.gov/37697698/) · [37538304](https://pubmed.ncbi.nlm.nih.gov/37538304/) · [37224926](https://pubmed.ncbi.nlm.nih.gov/37224926/) · [20445398](https://pubmed.ncbi.nlm.nih.gov/20445398/) · [38333215](https://pubmed.ncbi.nlm.nih.gov/38333215/) · [36947602](https://pubmed.ncbi.nlm.nih.gov/36947602/) · [34488201](https://pubmed.ncbi.nlm.nih.gov/34488201/) · [34801995](https://pubmed.ncbi.nlm.nih.gov/34801995/) · [34233299](https://pubmed.ncbi.nlm.nih.gov/34233299/) · [33979447](https://pubmed.ncbi.nlm.nih.gov/33979447/) · [32663058](https://pubmed.ncbi.nlm.nih.gov/32663058/) · [37018160](https://pubmed.ncbi.nlm.nih.gov/37018160/) · [36543843](https://pubmed.ncbi.nlm.nih.gov/36543843/) · [38687685](https://pubmed.ncbi.nlm.nih.gov/38687685/) · [35994701](https://pubmed.ncbi.nlm.nih.gov/35994701/) · [38854157](https://pubmed.ncbi.nlm.nih.gov/38854157/) · [38029728](https://pubmed.ncbi.nlm.nih.gov/38029728/) · [37742625](https://pubmed.ncbi.nlm.nih.gov/37742625/) · [33122357](https://pubmed.ncbi.nlm.nih.gov/33122357/) · [38706205](https://pubmed.ncbi.nlm.nih.gov/38706205/) · [31931652](https://pubmed.ncbi.nlm.nih.gov/31931652/) · [40192235](https://pubmed.ncbi.nlm.nih.gov/40192235/) · [36253079](https://pubmed.ncbi.nlm.nih.gov/36253079/) · [36368026](https://pubmed.ncbi.nlm.nih.gov/36368026/) · [34084131](https://pubmed.ncbi.nlm.nih.gov/34084131/) · [31019301](https://pubmed.ncbi.nlm.nih.gov/31019301/) · [39358509](https://pubmed.ncbi.nlm.nih.gov/39358509/) · [38848678](https://pubmed.ncbi.nlm.nih.gov/38848678/) · [40086603](https://pubmed.ncbi.nlm.nih.gov/40086603/) · [37669929](https://pubmed.ncbi.nlm.nih.gov/37669929/) · [22929469](https://pubmed.ncbi.nlm.nih.gov/22929469/) · [32868706](https://pubmed.ncbi.nlm.nih.gov/32868706/) · [34449797](https://pubmed.ncbi.nlm.nih.gov/34449797/) · [39012765](https://pubmed.ncbi.nlm.nih.gov/39012765/) · [32355263](https://pubmed.ncbi.nlm.nih.gov/32355263/) · [32791865](https://pubmed.ncbi.nlm.nih.gov/32791865/) · [36752571](https://pubmed.ncbi.nlm.nih.gov/36752571/) · [30421807](https://pubmed.ncbi.nlm.nih.gov/30421807/) · [34079225](https://pubmed.ncbi.nlm.nih.gov/34079225/) · [1762100](https://pubmed.ncbi.nlm.nih.gov/1762100/) · [2693695](https://pubmed.ncbi.nlm.nih.gov/2693695/) · [17993851](https://pubmed.ncbi.nlm.nih.gov/17993851/) · [18544701](https://pubmed.ncbi.nlm.nih.gov/18544701/) · [39270512](https://pubmed.ncbi.nlm.nih.gov/39270512/) · [37642199](https://pubmed.ncbi.nlm.nih.gov/37642199/) · [39600027](https://pubmed.ncbi.nlm.nih.gov/39600027/) · [37149389](https://pubmed.ncbi.nlm.nih.gov/37149389/) · [38003561](https://pubmed.ncbi.nlm.nih.gov/38003561/) · [34402700](https://pubmed.ncbi.nlm.nih.gov/34402700/) · [39355046](https://pubmed.ncbi.nlm.nih.gov/39355046/)

**Databases and guidance:**
- [MONDO:0033938 via EBI OLS4](https://www.ebi.ac.uk/ols4/ontologies/mondo)
- [Orphanet — Acute radiation syndrome (ORPHA:454831)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=454831)
- [MeSH D054508](https://meshb.nlm.nih.gov/record/ui?ui=D054508)
- [ICD-10-CM T66](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T66-T78/T66-/T66)
- [REMM — Acute Radiation Syndrome](https://remm.hhs.gov/ars_summary.htm) · [Myeloid Cytokines for H-ARS](https://remm.hhs.gov/cytokines.htm) · [Time Phases of ARS](https://remm.hhs.gov/ars_timephases4.htm) · [Lymphocyte Depletion Kinetics](https://remm.hhs.gov/aboutlymphocytedepletion.htm) · [Time to Onset of Vomiting](https://remm.hhs.gov/aboutvomiting.htm)
- [CDC — Acute Radiation Syndrome: Information for Clinicians](https://www.cdc.gov/radiation-emergencies/hcp/clinical-guidance/ars.html)
- [AFRRI — Medical Management of Radiological Casualties, 4th ed.](https://afrri.usuhs.edu/sites/default/files/2020-07/4edmmrchandbook.pdf)
- [IAEA — The Radiological Accident in Goiânia](https://www-pub.iaea.org/MTCD/Publications/PDF/Pub815_web.pdf) · [IAEA — Tokaimura](https://www.iaea.org/emergency/past-radiological-accidents/tokaimura) · [UNSCEAR — Chernobyl](https://www.unscear.org/unscear/en/chernobyl.html)
- [REAC/TS Radiation Accident Registry overview](https://www.osti.gov/biblio/1060542)
- [NIAID — approval of romiplostim for acute radiation injury](https://www.niaid.nih.gov/news-events/niaid-funded-research-leads-approval-drug-acute-radiation-injury) · [FDA Nplate approval letter, 2021](https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2021/125268Orig1s167ltr.pdf)
- [MCART Consortium Animal Models Series](https://journals.lww.com/health-physics/FullText/2012/10000/The_MCART_Consortium_Animal_Models_Series.2.aspx)
- ClinicalTrials.gov: [NCT01742221](https://clinicaltrials.gov/study/NCT01742221) · [NCT03585803](https://clinicaltrials.gov/study/NCT03585803) · [NCT03797040](https://clinicaltrials.gov/study/NCT03797040) · [NCT00903929](https://clinicaltrials.gov/study/NCT00903929) · [NCT06741345](https://clinicaltrials.gov/study/NCT06741345)

---

**One last time, because it's the thing most likely to bite:** every quote in here needs re-verification against `just fetch-reference` before it becomes a `snippet:`, and every 🔎 CURIE needs `just validate-terms` before it becomes a `term:`. The verified ✅ ones came from this repo's own caches or live OLS, so those should sail through — but the MONDO and ECTO terms in particular are worth a validation run in *both* the worktree and the primary checkout, since the write hook validates from the primary and that's exactly where a cache gap hides.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 68 |
| Resolved | 68 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 68 |
| On topic | 44 |
| Off topic | 0 |

All extracted references resolved successfully.
