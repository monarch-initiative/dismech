---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-11-11T22:37:38.379922'
end_time: '2026-11-11T22:57:40.867467'
duration_seconds: 1202.49
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Neurocutaneous Melanocytosis
  mondo_id: MONDO:0009578
  category: Genetic
  causal_genes: NRAS
  omim_id: OMIM:249400
  synonyms: NCM; neurocutaneous melanosis; neurocutaneous melanosis, somatic
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
  web_search_requests: 10
  num_turns: 112
  total_cost_usd: 8.912262250000003
  session_id: 0cc51d18-194b-4f8d-8be8-5132053dc6e9
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 23
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurocutaneous Melanocytosis
- **MONDO ID:** MONDO:0009578 (if available)
- **Causal gene(s):** NRAS
- **OMIM:** OMIM:249400
- **Synonyms:** NCM; neurocutaneous melanosis; neurocutaneous melanosis, somatic
- **Category:** Genetic

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Neurocutaneous Melanocytosis** covering all of the
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

# Neurocutaneous Melanocytosis (MONDO:0009578) — Comprehensive Disease Research Report

**Prepared:** 11 November 2026
**Target concept:** Neurocutaneous melanocytosis / neurocutaneous melanosis (NCM), MONDO:0009578, OMIM:249400
**Causal gene:** **NRAS** (NRAS proto-oncogene, GTPase; `hgnc:7989`, 1p13.2) — present as a **post-zygotic (somatic, mosaic) activating mutation**, almost always in codon 61

> **Evidence-handling caveat for the curator.** Every quotation below was retrieved from PubMed/PMC/OLS during this session, but several passed through a summarising fetch layer. **Before any snippet enters a KB entry it must be re-cached with `just fetch-reference <ID>` and re-verified as an exact substring of the committed `references_cache/` file.** Treat every CURIE below as a *lead*, not a binding: the ones explicitly marked ✅ were resolved against OLS4, HGNC REST, the HPO annotation API, MGI/Alliance or OMIA in this session; the rest are flagged **[verify]**.

---

## 1. Disease Information

### Overview

Neurocutaneous melanocytosis is a **rare, congenital, non-inherited mosaic neurocristopathy** in which a single post-zygotic activating mutation — in the great majority of cases in **codon 61 of *NRAS*** — arises in a progenitor cell of the developing neural crest/neuroectoderm. The mutant clone populates both the **skin** (producing large, giant and/or multiple congenital melanocytic naevi, CMN) and the **central nervous system** (producing melanocytosis of the leptomeninges and/or brain parenchyma, and a range of non-melanocytic CNS malformations).

MONDO's own definition (OLS4, ✅ retrieved):

> "Neurocutaneous melanocytosis (NCM) is a rare congenital neurological disorder characterized by abnormal aggregations of nevomelanocytes within the central nervous system (leptomeningeal melanocytosis) associated with large or giant congenital melanocytic nevi (CMN)."

The most authoritative recent clinical synthesis is Ruggieri et al. (PMID:33048248), whose abstract is quoted at length because it is the single best "what is this disease" statement in the literature:

> "Neurocutaneous melanosis (NCM; MIM # 249400; ORPHA: 2481], first reported by the Bohemian pathologist Rokitansky in 1861, and now more precisely defined as neurocutaneous melanocytosis, is a rare, congenital syndrome characterised by the association of (1) congenital melanocytic nevi (CMN) of the skin with overlying hypertrichosis, presenting as (a) large (LCMN) or giant and/or multiple (MCMN) melanocytic lesions (or both; sometimes associated with smaller 'satellite' nevi) or (b) as proliferative melanocytic nodules; and (2) melanocytosis (with infiltration) of the brain parenchyma and/or leptomeninges."
> — Ruggieri M, Polizzi A, Catanzaro S, et al. *Childs Nerv Syst.* 2020. **PMID:33048248**

**NCM is now best understood as one CNS phenotype within "congenital melanocytic naevus syndrome" (CMNS), a mosaic RASopathy** — not as a free-standing disease of unrelated aetiology. Jaeger et al. explicitly file it among the **mosaic RASopathies**:

> "...and mosaic conditions such as sebaceous nevus syndrome, neurocutaneous melanosis, McCune-Albright syndrome, phakomatosis pigmentokeratotica, epidermal nevus syndrome, and encephalocraniocutaneous lipomatosis."
> — Jaeger ZJ, et al. *RASopathies. Part II: Cutaneous and extracutaneous manifestations.* J Am Acad Dermatol. 2025. **PMID:40532825**

### Key identifiers

| Resource | Identifier | Status |
|---|---|---|
| Mondo | **MONDO:0009578** (*neurocutaneous melanocytosis*) | ✅ OLS4 |
| OMIM | **OMIM:249400** — "MELANOSIS, NEUROCUTANEOUS; NCMS" | ✅ xref in MONDO; OMIM page itself returned HTTP 403 this session |
| Orphanet | **ORPHA:2481** | ✅ xref in MONDO |
| MeSH | **MeSH:C537387** (supplementary concept record) | ✅ xref in MONDO |
| UMLS | **UMLS:C0544862** | ✅ xref in MONDO |
| GARD | **GARD:0007186** | ✅ xref in MONDO |
| ICD-11 | WHO entity **403221860**; the human-readable stem code could **not** be retrieved (`id.who.int` returned HTTP 401) | **[verify]** |
| ICD-10 | **No code verified in this session.** Do not bind one from memory | **not available** |
| Causal gene | **`hgnc:7989`** NRAS, "NRAS proto-oncogene, GTPase", 1p13.2, ENSG00000213281, NCBI Gene 4893, UniProt P01111, OMIM:164790 | ✅ HGNC REST |

### Synonyms and alternative names

From MONDO (✅): exact — **NCM**, **neurocutaneous melanosis**; related — **NCMS**, **neurocutaneous melanosis syndrome**. Also in use: *neurocutaneous melanoblastosis*, *Rokitansky–van Bogaert syndrome* (historical), *melanophakomatosis*, *leptomeningeal melanocytosis with giant congenital naevus*. Ruggieri et al. argue that **"neurocutaneous melanocytosis" is the more precise term** than "melanosis", because the lesion is a proliferation of melanocytes, not merely melanin deposition (PMID:33048248). The contemporary umbrella term for the whole mosaic disorder is **congenital melanocytic naevus syndrome (CMNS)**.

### Provenance of the information in this report

**Aggregated disease-level resources and case-series literature only.** There is no EHR-derived or individual-patient-data source for NCM at scale. The largest datasets are:
- **Great Ormond Street Hospital (GOSH) prospective CMN registry**, 1988–present (PMID:18811688, 18671780, 25966033, 28078671) — the single most informative cohort;
- the **Nevus Outreach Internet-based registry** (PMID:16310055);
- a Japanese single-centre MRI series (PMID:37777590);
- a 74-patient systematic review of neurosurgical management (PMID:35535823);
- `NCT06828822` (**CINCLE** — CongenItal Naevus Cohort for Longitudinal Evaluation), recruiting from 23 July 2025, which collects prospective neurodevelopmental and QoL data (ClinicalTrials.gov, ✅ API v2).

---

## 2. Etiology

### 2.1 Disease causal factors — a single mosaic oncogenic point mutation

The defining paper is Kinsler et al. 2013, which established causation:

> "...oncogenic missense mutations in codon 61 of NRAS were found in affected neurological and cutaneous tissues of 12 out of 15 patients" ... "single postzygotic NRAS mutations are responsible for multiple CMN and associated neurological lesions in the majority of cases."
> — Kinsler VA, Thomas AC, Ishida M, et al. *Multiple congenital melanocytic nevi and neurocutaneous melanosis are caused by postzygotic mutations in codon 61 of NRAS.* J Invest Dermatol. 2013;133(9):2229–36. **PMID:23392294**, DOI:10.1038/jid.2013.70

Three features of that study are mechanistically decisive:

1. **The mutation is in codon 61 and is recurrent.** "c.181C>A, p.Q61K" in 10 of 12 mutation-positive patients, "c.182A>G, p.Q61R" in 2.
2. **It is mosaic.** The mutation was absent from blood and from clinically unaffected tissues — so it is **not inherited and not germline**.
3. **Skin and CNS lesions are clonally identical.** All 11 melanocytic *and non-melanocytic* CNS lesions from 5 patients carried the same codon-61 mutation as that patient's cutaneous naevi. This is the evidence that NCM is one mosaic clone in two organs, not two diseases.

Charbel et al. independently showed the mutation is both near-universal in large/giant CMN and *sufficient*:

> "Large-giant CMNs displayed NRAS mutations in 94.7% of cases (18/19)... We therefore performed exome sequencing on five specimens of large-giant nevi. The results showed that NRAS mutation was the sole recurrent somatic event found in such melanocytic proliferations... These findings strongly suggest that NRAS mutations are sufficient to drive melanocytic benign proliferations in utero."
> — Charbel C, et al. J Invest Dermatol. 2014;134(4):1067–74. **PMID:24129063**

**Timing matters as much as the mutation.** Charbel's small/medium CMN comparison group had a *different* genetic profile (70% NRAS, 30% BRAF), consistent with later, more restricted clonal origin. The large-CMN/NCM phenotype requires the mutation to arise **early enough to be inherited by both cutaneous and CNS melanoblast precursors** — i.e. at or before neural-crest specification/migration.

### 2.2 Risk factors

**Genetic (all somatic / mosaic, none heritable):**

| Factor | Evidence |
|---|---|
| **NRAS codon 61 (Q61K ≫ Q61R)** | 12/15 patients (PMID:23392294); 94.7% of large-giant CMN (PMID:24129063); 77.3% of 66 patients, 75% of the NCM subset (PMID:25490715); 68% of a 2020 GOSH series (PMID:31111470) |
| **BRAF V600E** (minority alternative driver) | Salgado et al. found BRAF V600E in 7.6% of 66 CMN patients and reported, as a novel finding, that BRAF V600E also occurs in large/giant CMN **and in NCM** (PMID:25490715). Polubothu et al.: NRAS 68%, BRAF 7% (mutually exclusive), **double wild-type 25%** (PMID:31111470). A 2026 case showed "sustained neurologic and cutaneous improvement following BRAF inhibition" in BRAF-V600E NCM (PMID:42384401) |
| **BRAF fusion oncogenes** | A distinct CMN subset is initiated by *BRAF fusion*, with a characteristic firm, pruritic, desmoplastic phenotype (Roy SF, et al. Br J Dermatol. 2025. **PMID:40036344**) |
| **Second-hit / progression events** (risk of malignancy, not of NCM itself) | Whole-genome copy-number gains and losses in progressive CNS disease (PMID:27933403); *NRAS G12V* acquired only in the malignant site, plus copy-neutral LOH (PMID:38254245); loss of H3K27me3 in 4/5 childhood nodular melanomas in CMN vs 0/20 proliferative nodules (PMID:27849631); GNAS copy gain + 10q loss in one malignantly transformed NCM (PMID:34994589) |

**Cutaneous phenotype as the dominant clinical risk factor for CNS involvement** — this is the practical risk model:

- **Projected adult size (PAS) of the largest naevus**, especially >40 cm: "MRI and/or clinical neurological abnormalities were found in 22 patients (18%) and were significantly associated with projected adult size of the CMN (particularly > 40 cm), and independently with **male gender**" (Kinsler VA, Chong WK, Aylett SE, Atherton DJ. Br J Dermatol. 2008;159(4):907–14. **PMID:18671780**).
- **Satellite/multiple naevus count.** In the same study, "No complications were seen in the 16 patients with no satellite lesions at birth." More than 20 satellites is the usual threshold: "The presence of more than 20 accompanying nevi indicates an elevated risk of central nervous system (CNS) involvement" (*Diagnostics.* 2024;14(21):2345. **PMID:39518313**).
- Multivariable Japanese data found significant associations of NCM with CMN **distribution** (p=0.002), **size** (p=0.01), **satellite nevi count** (p=0.002), **rugosity** (p=0.009) and **nodules** (p=0.006) (PMID:37777590).
- **Male sex** is an independent risk factor for neurological complications (PMID:18671780); 76% of 74 published NCM patients were male (PMID:35535823).
- **Posterior axial / dorsal distribution** is traditionally cited (80% of Agero's NCM cases had posterior-axis LCMN, PMID:16310055), but **Kinsler's larger prospective series explicitly disputes it**: "Importantly, there was no significant association between CMN distribution (including posterior axial location) and adverse outcomes" (PMID:18671780). This is a live disagreement in the literature and should be curated as such.

**Environmental:** essentially **none established as causal.** The mutation is a spontaneous post-zygotic event. The one epidemiological signal is weak and from a recall-prone design: "Other factors found to be significantly increased in CMN families compared with controls were **maternal smoking and ill health during pregnancy**. Maternal smoking was positively associated with PAS" (Kinsler VA, Birley J, Atherton DJ. Br J Dermatol. 2009;160(1):143–50. **PMID:18811688**). The authors themselves caution the study "may be subject to recall bias." There is **no** evidence for toxin, radiation, infectious or occupational causation. Age, sex and family history are *not* risk factors for acquiring the mutation (though 25% of CMN families reported a CMN in a second-degree relative, with a different gender ratio, "suggesting a different underlying mutation" — PMID:18811688).

### 2.3 Protective factors

**No genetic or environmental protective factor is established.** Two indirect observations:

- **Germline NRAS codon-61 mutation is presumed incompatible with life**, which is why the disorder exists only in mosaic form. Germline *NRAS* variants at other residues cause **Noonan syndrome 6** and **autoimmune lymphoproliferative syndrome type 4** (Alliance of Genome Resources record for the NRAS ortholog, ✅) — i.e. a quite different, non-naevoid phenotype. This is an inference from the absence of germline Q61 cases, not a demonstrated lethality.
- **MC1R genotype** modifies CMN *colour* (and therefore, arguably, photoprotection/surveillance), not CNS risk: "Final CMN colour in childhood is significantly associated with the individual's normal skin colour, and with MC1R genotype, and is therefore genetically determined" (PMID:31120141). Compound heterozygous MC1R risk variants have been reported alongside giant CMN (PMID:41624622).
- **Spontaneous lightening of CMN** is common and is an argument *against* early surgery, not a protective factor against NCM (PMID:19244003).

### 2.4 Gene–environment interactions

**None demonstrated.** The maternal-smoking association with PAS (PMID:18811688) is the only candidate and is unreplicated and confounded. UV exposure is a general melanoma risk factor but has **not** been shown to modify melanoma risk *within* CMN, where melanoma characteristically arises in the **dermis/subcutis or the CNS** rather than at the dermo-epidermal junction — which argues against a UV mechanism for the CMN-associated tumours.

---

## 3. Phenotypes

### 3.1 HPO annotations currently attached to OMIM:249400

Retrieved ✅ from the HPO annotation API (`ontology.jax.org`, disease "Neurocutaneous melanosis, somatic"). **These 15 are authoritative and can be bound directly:**

| HPO term | Label | Recorded frequency |
|---|---|---|
| **HP:0005603** | Numerous congenital melanocytic nevi | — |
| **HP:0002861** | Melanoma | — |
| **HP:0001250** | Seizure | — |
| **HP:0000238** | Hydrocephalus | Occasional |
| **HP:0001305** | Dandy-Walker malformation | Occasional |
| **HP:0100702** | Arachnoid cyst | Occasional |
| **HP:0003396** | Syringomyelia | Occasional |
| **HP:0006824** | Cranial nerve paralysis | — |
| **HP:0001263** | Global developmental delay | Occasional |
| **HP:0001268** | Mental deterioration | — |
| **HP:0002858** | Meningioma | Occasional |
| **HP:0200022** | Choroid plexus papilloma | Occasional |
| **HP:0001522** | Death in infancy | — |
| **HP:0001442** | Typified by somatic mosaicism | *(inheritance)* |
| **HP:0003745** | Sporadic | *(inheritance)* |

Note that **HP:0001442 is already annotated**, so the repository's `somatic-mosaicism` skill applies directly: this entry should carry an `inheritance` block bound to HP:0001442 with its own cited evidence, plus `variant_origin: SOMATIC` on the NRAS record.

### 3.2 Cutaneous phenotypes

| Phenotype | Characteristics | Frequency | Suggested HPO |
|---|---|---|---|
| **Large/giant congenital melanocytic naevus** | Present at birth; PAS >20 cm (large) or >40 cm (giant); "bathing trunk" distribution common; follows the archetypal **6B mosaic patterns** (PMID:33048248); Krengel's consensus categories: small <1.5 cm, medium 1.5–20 cm, large >20–40 cm, giant >40 cm (PMID:22982004) | Definitional | HP:0005603 ✅; *congenital melanocytic nevus* **[verify]** |
| **Multiple / satellite naevi (>3; risk threshold >20)** | Present at birth or appearing through infancy; counted during infancy per Krengel | Definitional for the "multiple CMN" arm | HP:0005603 ✅ |
| **Overlying hypertrichosis** | Congenital, stable | Common ("CMN... with overlying hypertrichosis", PMID:33048248); Krengel grades hair growth none/moderate/marked | *Hypertrichosis* **[verify]** |
| **Rugose/verrucous surface change, dermal–subcutaneous nodules** | Evolving through childhood; nodules associated with BRAF-mutant lesions (PMID:25490715) and are an NCM risk marker (p=0.006, PMID:37777590) | Variable | **[verify]** |
| **Proliferative nodules** | Benign nodular growths that mimic melanoma; H3K27me3 **retained** (0/20 lost) vs lost in 4/5 melanomas (PMID:27849631) | Common in large CMN | **[verify]** |
| **Cutaneous melanoma** | Arises typically in dermis/subcutis of the naevus; median age 7 y (PMID:16792745) | 0.7–2.2% (see §11) | HP:0002861 ✅ |
| **Progressive lightening** | Spontaneous, sometimes dramatic | Common (PMID:19244003) | — |

### 3.3 Neurological phenotypes

Onset pattern is bimodal: a **paediatric form presenting usually before age 2** and a late/adult form. Ji et al. (PMID:41141235): pediatric NCM typically manifests before age 2; adult-type usually presents after age 30.

| Phenotype | Onset | Severity / course | Frequency | Suggested HPO |
|---|---|---|---|---|
| **Intraparenchymal / leptomeningeal melanocytosis on MRI (often asymptomatic)** | Congenital, detectable in infancy; **prenatally at 23 weeks' gestation** in one case (PMID:41474606) | Static in the "group 1" form | **21% of children with multiple CMN had an abnormal MRI** (PMID:25966033); 18% MRI and/or clinical abnormality (PMID:18671780); **31.6% (95% CI 19.0–47.0%)** of 38 Japanese infants, 25.0% (95% CI 13.0–42.0%) treatment-naive (PMID:37777590); only 4.8% asymptomatic abnormality in a self-reported registry (PMID:16310055) | — |
| **Seizures / epilepsy** | Infancy to adolescence; can be the presenting sign at 13 y (PMID:33257354) | Can be drug-resistant; NCM is a recognised cause of **focal cortical dysplasia with drug-resistant epilepsy** (PMID:41467858) | **Seizures 55%, epilepsy 45%** of 74 published cases (PMID:35535823); 7/14 developed epilepsy (PMID:22469364) | HP:0001250 ✅ |
| **Raised intracranial pressure / hydrocephalus** | Infancy most often | Requires shunting; a driver of mortality | **24%** (PMID:35535823); often from diffuse leptomeningeal disease | HP:0000238 ✅ |
| **Developmental delay / cognitive and behavioural abnormality** | Early childhood | Variable, can be independent of MRI findings | **20% of CMN patients had abnormal neurodevelopment**, positively associated with PAS but "seen across all size categories" (PMID:18811688) | HP:0001263 ✅ |
| **Cranial nerve palsies** | Any age | Progressive with leptomeningeal infiltration | Listed by Ruggieri (PMID:33048248) | HP:0006824 ✅ |
| **Motor / sensory deficits, myelopathy** | Any age | Progressive | Listed (PMID:33048248) | **[verify]** |
| **Sleep-cycle anomalies** | Childhood | — | Listed (PMID:33048248) | **[verify]** |
| **CNS melanoma / leptomeningeal melanomatosis** | Peak in infancy–early childhood; mean/median age at death 3.9/2.5 y (PMID:28078671) | Rapidly fatal | 4/6 deaths had leptomeningeal melanoma (PMID:22469364); 62% of Kadonaga & Frieden's 39 historical cases had leptomeningeal melanoma (PMID:1869648) | HP:0002861 ✅ |
| **Optic neuropathy** | Young adult | Progressive | **Newly described**; "optic neuropathy in NCM has not been reported earlier" (PMID:38803399) | **[verify]** |
| **Growth / endocrine abnormality** | Childhood | BMI rose at twice the UK population rate; premature thelarche variant in 3% of girls; persistent undescended testes in 6% of boys; moderate–severe insulin insensitivity in 5/10 on OGTT; **fat and muscle mass reduced under large naevi causing limb asymmetry** | Waelchli R, et al. Br J Dermatol. 2015;173(6):1471–8. **PMID:26286459** | **[verify]** |

### 3.4 Associated CNS and spinal malformations

Ruggieri et al. (PMID:33048248) enumerate them:

> "Associated brain and spinal cord malformations include the Dandy-Walker malformation (DWM) complex, hemimegalencephaly, cortical dysplasia, arachnoid cysts, Chiari I and II malformations, syringomyelia, meningoceles, occult spinal dysraphism, and CNS lipoma/lipomatosis."

- **Dandy-Walker malformation: 24%** of 74 published NCM cases (PMID:35535823). But a 2026 case report states "the combination of NCM and DWM is extremely rare, with fewer than 40 reported cases" (PMID:42626233) — the two figures are not inconsistent (24% of a *published-case* denominator heavily enriched for severe disease).
- **Extensive dorsal arachnoid cysts** in 3/14 (PMID:22469364); the *Diagnostics* review notes an "increased incidence of arachnoid cysts" (PMID:39518313).
- **Primary CNS tumours: 23%** of published cases (PMID:35535823). HPO additionally records meningioma (HP:0002858) and choroid plexus papilloma (HP:0200022) as occasional.
- **Extramedullary intradural spinal tumour** reported in infancy (PMID:42252882).

### 3.5 Quality of life

There is **no NCM-specific EQ-5D/SF-36/PROMIS dataset.** What exists:

- An international **core domain set** for medium/large/giant CMN agreed by 144 stakeholders from 27 countries: "We reached consensus on six domains, four of which were applied to both care and research: 'quality of life', 'neoplasms', 'nervous system' and 'anatomy of skin'" (Oei W, et al. Br J Dermatol. 2021. **PMID:33237568**). This is the right instrument scaffold for a future dismech `clinical_burden` block.
- Vourc'h-Jourdain's systematic review: "Behavioral and emotional difficulties appeared common in affected children independent of lesion characteristics" (PMID:23182059) — i.e. psychosocial burden does **not** track naevus size, which is a clinically important dissociation.
- Choi et al. frame the surgical burden explicitly: "This risk often triggers preemptive extensive surgical excisions in childhood, producing severe lifelong challenges" (PMID:35561684).
- Active QoL studies: `NCT02280889` (quality of life in children with CMN, recruiting), `NCT06934759` (parents of a child with large/giant CMN, enrolling by invitation), `NCT06828822` (CINCLE, includes QoL assessment) — all ✅ ClinicalTrials.gov API.

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

**NRAS** — `hgnc:7989` (✅ HGNC REST): approved name "NRAS proto-oncogene, GTPase"; locus **1p13.2**; ENSG00000213281; NCBI Gene 4893; UniProt **P01111**; **OMIM:164790**; alias *N-ras*.

### 4.2 Pathogenic variants

| Attribute | Detail |
|---|---|
| **Canonical variants** | **NM_002524.5(NRAS):c.181C>A (p.Gln61Lys / Q61K)** — the dominant allele; **c.182A>G (p.Gln61Arg / Q61R)** — minority. Ratio 10:2 in the index series (PMID:23392294). Both are in ClinVar linked to "Neurocutaneous melanocytosis" (ClinVar RCV000144964 for c.181C>A, seen in search results — **[verify in ClinVar before binding]**) |
| **Variant type/class** | **Missense**, single-nucleotide substitution in the switch II/catalytic region |
| **Functional consequence** | **GAIN OF FUNCTION.** Gln61 is the catalytic glutamine required for GTP hydrolysis; Q61K/Q61R abolish intrinsic and GAP-stimulated GTPase activity, locking NRAS in the GTP-bound active state → constitutive RAF–MEK–ERK and PI3K–AKT–mTOR signalling. In dismech terms this is `functional_impact_category: GAIN_OF_FUNCTION` on the `genetic_context`, with `modifier: GAIN_OF_FUNCTION` (not merely `INCREASED`) on the pathway nodes, because the pathway is outside normal regulatory control |
| **Origin** | **SOMATIC / post-zygotic mosaic, obligately.** "none of the blood samples or clinically unaffected tissue samples carried this mutation" (PMID:23392294). Practical corollary, now documented: a prenatal/postnatal **blood-based CNV-seq + WES can be entirely negative** — one 2026 prenatal case concluded NCM may occur "without definite pathogenic mutations" (PMID:41474606), which is better read as *lesional tissue was not sequenced* than as a genuinely mutation-negative disease |
| **Population allele frequency** | **Not applicable / expected absent.** gnomAD, 1000 Genomes and TOPMed are germline resources; a germline NRAS Q61K is not expected to be viable. Do not quote a gnomAD frequency for this variant in a germline context. NRAS Q61K/Q61R are, by contrast, among the commonest somatic drivers in cutaneous melanoma (COSMIC) — **[verify COSMIC figures before quoting a percentage]** |
| **Classification** | ACMG/AMP germline tiers do not apply cleanly to an obligate mosaic oncogenic driver; report as a somatic pathogenic driver (ClinVar does carry an NCM-linked record) |

### 4.3 Alternative and secondary drivers

- **BRAF V600E** — 7.6% of 66 CMN patients, and present in large/giant CMN and in NCM (PMID:25490715); 7% in the GOSH genotyping series, mutually exclusive with NRAS (PMID:31111470). Therapeutically actionable with BRAF inhibition (PMID:42384401).
- **BRAF fusion** — initiates a morphologically distinct CMN subtype (PMID:40036344).
- **Double wild-type ≈25%** of CMN by hotspot testing (PMID:31111470) — i.e. a quarter of patients have no identified driver on targeted assays. One atypical large CMN with no NRAS/BRAF hotspot showed **melanocyte-associated mTORC1 activation** and a maternally inherited **TSC2 VUS** (PMID:42890568).
- **Progression drivers (not initiating):**
  - *NRAS G12V* found **only** in the malignant abdominal deposit, with GNAQ R183Q and S1PR3 G89S shared between tumour and normal tissue, and **copy-neutral LOH** in tumour: "NRAS mutation was found only in the abdominal tumour and was thought to be responsible for malignant progression in the present case" (Takahashi H, et al. Acta Neuropathol Commun. 2024. **PMID:38254245**).
  - **GNAS copy-number gain and 10q loss** in malignant transformation of NCM (PMID:34994589).

### 4.4 Modifier genes

- **CDKN2A/INK4a** — not a human modifier of NCM *per se*, but in the mouse it is the decisive cooperating lesion: ">90% of Tyr::N-RasQ61K INK4a−/− transgenic mice develop melanoma at 6 months" (PMID:15899789). This is the strongest candidate mechanism for the second hit in human CMN-associated melanoma and should be flagged as a knowledge gap rather than asserted.
- **MC1R** — modifies naevus colour (PMID:31120141) and general melanoma susceptibility (PMID:41624622).
- **PAX3** — haplosufficient for melanoma development in the Tyr::NRAS^Q61K;Cdkn2a−/− model, i.e. *not* a modifier: "Tyr::NRAS(Q61K); Cdkn2a(-/-); Pax3(GFP/+) mice developed metastasizing melanoma as their Tyr::NRAS(Q61K); Cdkn2a(-/-) littermates" (PMID:26587692).
- **SALL4** — an embryonic stem-cell factor re-expressed in the Tyr::NrasQ61K;Cdkn2a−/− model whose *loss* prevents primary tumour formation but promotes micrometastasis (PMID:34417458). Relevant to the stem-cell phenotype of CMN cells.

### 4.5 Epigenetic information

- **H3K27me3 loss** distinguishes melanoma from proliferative nodules in CMN: "Significant loss of H3K27me3 expression was seen in 4 of 5 melanomas, but not in any of the 20 PNs" (Busam KJ, et al. Am J Surg Pathol. 2017;41(3):396–404. **PMID:27849631**). The authors conclude "epigenetic events likely play a role in the pathogenesis of melanoma developing in the dermis or subcutis of CMN."
- **DNA-methylation-directed therapy is being attempted:** azacitidine combined with trametinib against leptomeningeal melanosis in CMNS (Raljević L, et al. Mol Cell Pediatr. 2026. **PMID:41973363**) — note this is a single case-level report.
- **No ENCODE / Roadmap / DiseaseMeth NCM-specific dataset was identified.**

### 4.6 Chromosomal abnormalities

NCM itself carries **no constitutional karyotypic abnormality** — CMA and karyotype are normal, because the lesion is a point mutation in a mosaic clone. Chromosomal change is instead the **signature of malignant progression**:

> "Whole genome copy number abnormalities in newly acquired, or clinico-radiologically progressive melanotic disease in the CNS seem to mirror those described in cutaneous melanoma, with a characteristic signature of multiple gains and losses of parts of chromosomes seen in fatal cases even where histology was not clearly malignant. These can, therefore be considered as primary CNS melanoma."
> — Kinsler VA, Polubothu S, Calonje JE, et al. Acta Neuropathol. 2017;133(2):329–31. **PMID:27933403**

In that series, the one patient with **stable** leptomeningeal melanocytosis had "a normal chromosomal copy number pattern and the patient continues to be clinically stable", while all five with copy-number abnormality died. **This is the single most important diagnostic distinction in the disease** (see §10 and the curation note in §16).

---

## 5. Environmental Information

- **Environmental factors:** none established. No CTD/TOXNET/EPA signal was identified for NCM. The mutation arises spontaneously in utero.
- **Lifestyle factors:** none established for disease causation. Maternal smoking in pregnancy was associated with larger PAS in a recall-prone questionnaire study (PMID:18811688) — report as a weak, unreplicated association only. Standard photoprotection is advised for CMN as for any pigmented-lesion-bearing skin, but UV has **not** been shown to drive the characteristic dermal/CNS tumours.
- **Infectious agents:** **not applicable.** NCM is not an infectious or post-infectious disease. No `infectious_agent` or `transmission` block should be created.
- **Iatrogenic / procedural risk worth recording:** abdominal dissemination of leptomeningeal melanomatosis **via a ventriculoperitoneal shunt**, causing death from respiratory failure (PMID:38254245). This is a treatment-related mechanism, not an environmental exposure, and belongs with the treatment record.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain, as an ordered sequence

1. **A single post-zygotic missense mutation in *NRAS* codon 61 (c.181C>A p.Q61K, or c.182A>G p.Q61R) arises in a multipotent progenitor of the neural crest or neuroectoderm during early embryogenesis.** → This creates a mosaic clone carrying the mutation while all other tissues remain wild-type. *Demonstrated* — mutation present in affected skin and CNS, absent from blood and unaffected tissue (PMID:23392294). The progenitor identity is *inferred*: Kinsler et al. state the mutation "probably occurs in a progenitor cell in the developing neural crest or neuroectoderm."

2. **Loss of the catalytic Gln61 abolishes GTP hydrolysis, so mutant NRAS is locked in its GTP-bound active conformation.** → This results in **constitutive, ligand-independent activation of downstream effectors**. *Inferred for this disease from established RAS biochemistry*; directly supported in NCM tissue by pERK immunohistochemistry, which fell after MEK inhibition (PMID:24713450).

3. **Constitutively active NRAS drives the RAF→MEK→ERK (MAPK) cascade and, in parallel, PI3K→AKT→mTOR signalling.** → These branch; both are required. Ruggieri et al.: the mutations "disrupt the RAS/ERK/mTOR/PI3K/akt pathways" (PMID:33048248). *Branch point.* Functional proof of both arms comes from patient-derived cells: "Clonogenicity appeared to depend on bFGF and IGF1 signaling through ERK and Akt" (PMID:29976629), and inhibitors of MEK (MEK162), PI3K (GDC0941) and dual PI3K/mTOR (GSK2126458) each reduced viability, with the dual inhibitor strongest (PMID:26354928).

4. **Sustained MAPK/PI3K signalling in the mutant melanoblast lineage leads to excessive proliferation, expanded survival and failure of the normal limits on melanocytic colonisation.** → This produces an abnormally large and numerous population of naevomelanocytes. *Demonstrated in model systems*: embryonic expression of oncogenic NRAS "induced melanocyte proliferation and congenital melanocytic lesions" (PMID:23303902); Tyr::N-RasQ61K mice "show hyperpigmented skin" (PMID:15899789). The mutation is **sufficient**: "NRAS mutations are sufficient to drive melanocytic benign proliferations in utero" (PMID:24129063).

5. **Because the clone was specified before neural-crest migration diverged, the same mutant population seeds two destinations** — the branch that defines the syndrome:
   - **5a. Skin** → expanded dermal and epidermal naevomelanocytes → **large/giant and multiple congenital melanocytic naevi with overlying hypertrichosis**. Mutant CMN cells have a stem-cell-like immunophenotype and ultrastructure (Kinsler VA, et al. Br J Dermatol. 2013. **PMID:23620525**-adjacent; see PMC3838625), which plausibly explains their clonogenic growth in vitro (PMID:26354928).
   - **5b. Leptomeninges and brain parenchyma** → **leptomeningeal and intraparenchymal melanocytosis**, concentrated where leptomeningeal melanocytes are normally densest. *Demonstrated clonality*: all 11 CNS lesions carried the same codon-61 mutation as the skin (PMID:23392294).

6. **In the CNS, melanin-laden melanocytes accumulate in the pia-arachnoid and in anterior temporal/limbic parenchyma, most often the amygdala, then cerebellum, brainstem/pons and cerebral hemispheres.** → This produces the pathognomonic **T1-shortening on MRI** (melanin is paramagnetic) rather than mass effect, and is often clinically silent. "NCM lesions were most frequently seen in the amygdala, followed by the cerebellum, brainstem, and cerebral hemispheres" (PMID:37777590).

7. **The mutation in non-melanocytic neuroectodermal derivatives of the same clone disturbs CNS and axial morphogenesis** → **Dandy-Walker malformation complex, hemimegalencephaly, cortical dysplasia, arachnoid cysts, Chiari I/II, syringomyelia, meningoceles, occult spinal dysraphism, CNS lipoma** (PMID:33048248). This is the step that explains why NCM has *non*-pigmentary malformations at all, and it rests on the demonstration that **non-melanocytic CNS lesions carry the mutation too** (PMID:23392294). NCM is now also recognised as a cause of **focal cortical dysplasia** with drug-resistant epilepsy (PMID:41467858).

8. **From step 6/7 the clinical phenotype diverges along three largely separable routes:**
   - **8a. Focal parenchymal melanosis (notably amygdala) → cortical/limbic irritability → seizures and epilepsy.** "Focal melanosis correlates with seizures" (PMID:39518313). Epilepsy in 45–55% of published cases (PMID:35535823).
   - **8b. Diffuse leptomeningeal melanocytosis → impaired CSF flow/absorption over the basal cisterns and subarachnoid space → hydrocephalus and raised intracranial pressure → vomiting, papilloedema, cranial-nerve palsy, developmental regression, death.** "Diffuse leptomeningeal melanosis associates with hydrocephalus and CNS melanoma" (PMID:39518313). All six deaths in Ramaswamy's series had diffuse leptomeningeal deposits (PMID:22469364).
   - **8c. Acquisition of additional genomic lesions in the mutant clone (whole-chromosome-arm gains/losses; H3K27me3 loss; a second RAS hit such as NRAS G12V; GNAS gain/10q loss) → malignant transformation to primary CNS melanoma or cutaneous melanoma → leptomeningeal melanomatosis, dissemination, death.** This is the route to mortality and is *demonstrated genomically*: "large gains and/or losses of parts of chromosomes, with a similar pattern to known findings in cutaneous melanoma in CMN patients" in all five fatal cases (PMID:27933403); "NRAS mutation was found only in the abdominal tumour and was thought to be responsible for malignant progression" (PMID:38254245).

9. **Pharmacological interruption of step 3 reverses steps 4–8 in part** — the therapeutic proof of the chain. Post-mortem tissue from a MEK162-treated patient showed "Lower MIB-1 expression and lower pERK expression in the post-treatment samples compared to pre-treatment, suggesting a potential effect of MEK inhibiting therapy" (PMID:24713450); trametinib gave "measurable and objective relief of symptoms and signs in all patients" in four NRAS-mutant CNS melanomas (PMID:28078671); topically delivered MEK, PI3K and c-KIT inhibitors "achieved major regressions" of nevi in mice and human xenografts (PMID:35561684).

### 6.2 Molecular pathways

| Pathway | Role | Suggested GO term |
|---|---|---|
| RAS→RAF→MEK→ERK (MAPK) cascade | Primary oncogenic driver; the validated drug target | **GO:0000165** MAPK cascade ✅; **GO:0070374** positive regulation of ERK1 and ERK2 cascade ✅ |
| Ras signal transduction | The lesion itself | **GO:0007265** Ras protein signal transduction ✅ |
| PI3K→AKT→mTOR | Co-required; supports clonogenic survival; druggable (omipalisib, alpelisib) | **GO:0043491** phosphatidylinositol 3-kinase/protein kinase B signal transduction ✅; *TOR signaling* **[verify]** |
| Growth-factor input (bFGF, IGF1) | Required for clonogenicity of NCM cells (PMID:29976629) | *fibroblast growth factor receptor signaling pathway*, *insulin-like growth factor receptor signaling pathway* **[verify]** |
| KIT signalling | Topical c-KIT inhibition regresses nevi in model systems (PMID:35561684) | **[verify]** |
| Melanocyte development/pigmentation | The affected differentiation programme | **GO:0030318** melanocyte differentiation ✅; *melanin biosynthetic process* **[verify]** |
| Neural crest migration | Explains the dual skin/CNS distribution | *neural crest cell migration* **[verify]** |

**Pathway-database coverage:** KEGG (hsa04010 MAPK, hsa04151 PI3K-Akt, hsa05218 Melanoma) and Reactome (Signalling by RAS mutants / Signalling by NRAS) both cover the generic pathways; **neither has an NCM-specific pathway entry.**

### 6.3 Cellular processes

Proliferation of naevomelanocytes with **stem-cell/clonogenic properties** (nevospheres grow on Geltrex matrix and "maintained their clonogenicity in vitro over passages"; skin-derived cells formed more colonies than CNS-derived — PMID:26354928); **evasion of apoptosis**; **autophagic cell death as the therapeutic exit** ("Omipalisib treatment prevented colony formation and induced autophagic cell death" — PMID:29976629; alpelisib's nevocyte reduction was "probably inducted by autophagy" — PMID:38071601); **innate-immune-mediated ablation** as an alternative exit (SADBE "triggered innate immunity that ablated detectable nevocytes" — PMID:35561684); **nestin-expressing primitive precursors** in the mouse tumours suggesting hierarchical organisation (PMID:15899789).

### 6.4 Protein dysfunction

NRAS (UniProt P01111) is a small GTPase cycling between GDP- and GTP-bound states. Gln61 positions the catalytic water for GTP hydrolysis; Q61K/Q61R **ablate hydrolysis** → persistent GTP loading → **constitutive effector binding (RAF, PI3K)**. This is a **gain-of-function / hypermorphic** change, not misfolding, loss of function or aggregation. No structural NCM-specific PDB entry exists; the generic NRAS and Q61-mutant RAS structures apply.

### 6.5 Metabolic, immune, tissue-damage and biochemical aspects

- **Metabolic:** no primary metabolic defect. Systemically, CMNS children show **BMI rising at twice the population rate with increased adiposity, insulin insensitivity in 5/10 on OGTT, and impaired glucose tolerance in 1/10** (PMID:26286459) — mechanism unresolved between a genetic effect of the mosaic clone and an environmental one, as the authors state. **Locally**, "Naevus-related reduction of fat and muscle mass suggests local hormonal or metabolic effects on development or growth of adjacent tissues, or mosaic involvement of these tissues at the genetic level."
- **Immune:** no autoimmunity or immunodeficiency. The immune system is instead **therapeutically exploitable**: SADBE-driven innate immune activation ablates nevocytes and fully prevented melanoma in the mouse CGN model (PMID:35561684); checkpoint blockade (nivolumab/ipilimumab) has been used in leptomeningeal melanomatosis (PMID:33921303).
- **Tissue damage:** not oxidative, ischaemic or fibrotic. Injury is by (i) **space-occupying/infiltrative leptomeningeal melanocytic proliferation** obstructing CSF dynamics, (ii) **cortical/limbic dysfunction** from parenchymal melanosis and associated cortical dysplasia, and (iii) **frank malignant invasion** once transformation occurs.
- **Biochemical abnormalities:** no enzyme deficiency, receptor or channel defect. The one biochemically distinctive substance is **melanin** (**CHEBI:89634** Melanin ✅ / **CHEBI:25179** melanins ✅), whose paramagnetism produces the T1 shortening used diagnostically and whose presence in CSF cytology supports diagnosis.

### 6.6 Molecular profiling

| Modality | What exists | Gap |
|---|---|---|
| Transcriptomics | Mouse-model transcriptional profiling (PMID:34417458); mTORC1-pathway profiling of lesional vs normal tissue in one atypical CMN (PMID:42890568) | **No published patient NCM CNS transcriptome; no GEO series identified for NCM specifically.** A GEO/dbGaP discovery pass would be needed before any `datasets:` block |
| Proteomics | None NCM-specific. IHC-level only: pERK, MIB-1 (PMID:24713450); HMB-45, Melan-A, S100 (PMID:41141235); H3K27me3 (PMID:27849631); BAP1 (PMID:26769193) | **No PRIDE/ProteomeXchange dataset identified** |
| Metabolomics / lipidomics | **None identified** | Complete gap |
| Genomic structural features | Whole-genome copy-number arrays on CNS lesions (PMID:27933403); multiregional exome sequencing of brain, abdominal tumour, naevus and normal tissue in one autopsy (PMID:38254245) | Small n |
| Single-cell / spatial | **None identified for NCM** | Complete gap — a strong candidate knowledge gap for the entry |
| Functional genomics screens | **No CRISPR/RNAi screen in NCM cells identified.** Pharmacological screens in patient-derived nevospheres (PMID:26354928) and ex vivo explants (PMID:38071601) substitute | Gap |

---

## 7. Anatomical Structures Affected

### Organ level

**Primary:** central nervous system (brain, leptomeninges, spinal cord) and skin. **Body systems:** nervous and integumentary. Ruggieri is explicit that this is essentially a two-organ disease: "There is no systemic involvement, or only rarely" (PMID:33048248) — which is an important negative for curation, since it means no cardiac, renal or hepatic records are warranted.

**Secondary / complication-level involvement:** ventricular system (hydrocephalus); optic nerve and visual pathway (PMID:38803399); peritoneum, via VP-shunt dissemination of malignant cells (PMID:38254245); lymph nodes, lung and liver in the metastatic setting (demonstrated in the mouse model, PMID:15899789); skeletal muscle and subcutaneous fat locally beneath large naevi (PMID:26286459).

### Tissue and cell level

| Structure | Suggested term |
|---|---|
| **Leptomeninges (pia + arachnoid)** — the signature site | **UBERON:0000391** leptomeninx ✅ |
| **Amygdala** — the single most frequent parenchymal site | **UBERON:0001876** amygdala ✅ |
| **Cerebellum** | **UBERON:0002037** cerebellum ✅ |
| **Pons / brainstem** | **UBERON:0000988** pons ✅ |
| Anterior temporal lobe, interpeduncular fossa, medulla, base of brain, cerebral hemispheres, spinal cord, subarachnoid space | **[verify]** |
| **Skin** | **UBERON:0002097** skin of body ✅ (dermis and subcutis are the critical compartments for melanoma arising in CMN) |

| Cell population | Suggested term |
|---|---|
| **Melanocyte** (naevomelanocyte; leptomeningeal melanocyte) | **CL:0000148** melanocyte ✅ |
| **Melanoblast** (the likely cell of the initiating lesion, developmentally) | **CL:0000541** melanoblast ✅ |
| **Neural crest cell** (the mutated progenitor) | **CL:0011012** neural crest cell ✅ |
| Leptomeningeal cell / arachnoid barrier cell; Schwann cell (relevant to the plexiform melanocytic schwannoma reported in PMID:41624622) | **[verify]** |

**Subcellular:** **melanosome** — the defining organelle; "Melanosomes were observed in pigmented cells in the brain by electron microscopic examination" in the macaque case (PMID:19276048). Bind a GO cellular-component term for melanosome **[verify]**. Plasma membrane (NRAS is farnesylated and membrane-anchored) and cytosol are the signalling compartments.

**Localisation and lateralisation:** CNS melanocytosis is characteristically **bilateral but asymmetric**. Reported MRI patterns include "extensive, bilateral, asymmetric leptomeningeal spontaneous T1 hyperintense signal" and "T1 hyperintensity in the bilateral amygdala and anterior temporal lobes" (PMID:33257354). Cutaneous distribution follows the **6B archetypal mosaic patterns** (PMID:33048248), with a posterior-axial/"bathing trunk" predominance in symptomatic series.

---

## 8. Temporal Development

### Onset

- **The cutaneous lesion is congenital by definition**, present and fully distributed at birth: "The CMN are recognised at birth" (PMID:33048248).
- **The CNS lesion is also congenital** and can be detected prenatally — diffuse cerebellar enhancement at 23 weeks' gestation (PMID:41474606) — but is frequently **asymptomatic at birth**.
- **Neurological onset is bimodal.** "Neurological manifestations can appear acutely in infancy, or more frequently later in childhood or adult life" (PMID:33048248). Classically most symptomatic patients present **in the first two years**; Kadonaga & Frieden found most presented within the first two years of life (PMID:1869648). Orphanet records age of onset as **childhood**. An adult-onset form presenting after age 30 is recognised (PMID:41141235), and symptomatic debut as late as age 13 with a single seizure (PMID:33257354) or age 20 with optic neuropathy and spinal melanoma (PMID:38803399) is documented.
- **Onset pattern:** congenital and insidious for the melanocytosis; **acute or stepwise** for complications (hydrocephalus, status epilepticus, malignant transformation).

### Progression and course

There is no formal staging system. The clinically operative stratification is **Waelchli's radiological subclassification**, which is the best prognostic instrument available:

> "Abnormalities were subclassified into group 1 'intraparenchymal melanosis alone' (n = 28) and group 2 'all other pathology' (n = 18). **Group 1 was not associated with malignancy or death during the study period, even when symptomatic with seizures or developmental delay**, whereas group 2 showed a much more complex picture, requiring individual assessment."
> — Waelchli R, Aylett SE, Atherton D, Thompson DJ, Chong WK, Kinsler VA. Br J Dermatol. 2015;173(3):739–50. **PMID:25966033**

So three courses must be curated separately:

1. **Stable, often asymptomatic intraparenchymal melanosis** (group 1) — static; normal copy number; compatible with long survival even with epilepsy or delay (PMID:25966033; PMID:27933403).
2. **Progressive non-malignant disease** — chronic, lifelong; hydrocephalus requiring shunting, drug-resistant epilepsy, cognitive decline.
3. **Malignant transformation to primary CNS melanoma or cutaneous melanoma** — **rapid and usually fatal**. Mean/median age at death from melanoma 3.9 and 2.5 years (PMID:28078671); in primary diffuse leptomeningeal melanomatosis "a median overall survival of 4 months from diagnosis" (PMID:33921303); both patients in a 2025 review died within 13 months of symptom onset (PMID:41141235).

**Duration:** lifelong. **Remission:** no spontaneous remission of the CNS lesion is documented; cutaneous naevi do **lighten** spontaneously, sometimes dramatically (PMID:19244003), and complete nevocyte ablation has been achieved only pharmacologically in models (PMID:35561684).

**Critical periods.** (i) **Embryogenesis** — the only window in which the disease could in principle be prevented; inaccessible. (ii) **The first screening MRI in infancy**, which is the decision point that determines prognosis and surveillance intensity. (iii) **Any stepwise neurological change at any age** — the window for detecting transformation while it is still treatable: "Any child with a stepwise change in neurological/developmental symptoms or signs should have an MRI with contrast of the brain and spine to look for new CNS melanoma" (PMID:25966033). (iv) **Early childhood (0–5 y)** — the peak hazard period for melanoma death.

---

## 9. Inheritance and Population

### Epidemiology

| Measure | Value | Source |
|---|---|---|
| **NCM prevalence** | **1/50,000–1/200,000** (Orphanet ORPHA:2481) — Orphanet's banded point prevalence reads 1–9/100,000. "The incidence of symptomatic NCM appears to be approximately a third to a half of these." | Orphanet, retrieved indirectly (orpha.net blocked direct fetch) — **[verify on the Orphanet page before binding]** |
| **Large CMN incidence** | ~**1 in 20,000** live births | PMID:23182059 ("They affect roughly 1 in 20,000 to 1 in 500,000 newborns") |
| **Giant CMN incidence** | ~**1 in 500,000** newborns | PMID:23182059 |
| **Proportion of large CMN developing NCM** | "**Approximately 12% of individuals with LCMN will develop NCM**: wide extension and/or dorsal axial distribution of LCMN increases the risk of NCM" | PMID:33048248 |
| **Proportion of multiple-CMN children with abnormal MRI** | **21%** | PMID:25966033 |
| **Proportion with MRI and/or clinical neuro abnormality** | **18%** | PMID:18671780 |
| **NCM on screening MRI, Japanese infants <1 y** | **31.6% (95% CI 19.0–47.0%)**; **25.0% (95% CI 13.0–42.0%)** treatment-naive | PMID:37777590 |
| **Asymptomatic NCM, self-reported registry** | **4.8%** (9/186 who had MRI) — the lowest published estimate, and the authors note the limitation of self-report | PMID:16310055 |

**These figures are not interchangeable and must not be averaged.** They differ by denominator (all CMN vs large CMN vs multiple CMN), by case definition (MRI melanin vs symptomatic NCM vs Kadonaga criteria) and by ascertainment (prospective tertiary cohort vs self-reported registry). A dismech `prevalence` block should carry each as a separate record with its own `population`, `measure_type` and `notes`.

### Inheritance

- **Not inherited.** `HP:0003745` Sporadic and `HP:0001442` Typified by somatic mosaicism are both annotated to OMIM:249400 (✅ HPO API). Orphanet records inheritance as **not applicable**.
- **Mechanism:** post-zygotic somatic mosaicism in *NRAS*, demonstrated by mutation presence in lesional and absence in blood/unaffected tissue (PMID:23392294).
- **Penetrance / expressivity:** the concepts apply only *within* the mosaic clone. Expressivity is **highly variable** and the literature attributes this to mosaic architecture — the proportion and distribution of mutant cells: "Interpersonal variation may reflect the mosaic nature of this disease and patients should be considered individually" (PMID:26286459).
- **Genetic anticipation:** not applicable (not a repeat expansion, not transmitted).
- **Germline mosaicism:** no vertical transmission of NRAS Q61 has been reported. However, 25% of CMN families reported a CMN in a second-degree relative, with a different gender ratio, "suggesting a different underlying mutation" (PMID:18811688) — a real but unexplained familial clustering signal that should be recorded as a knowledge gap rather than as inheritance.
- **Founder effects / consanguinity / carrier frequency:** **not applicable.** Do not create carrier-frequency or consanguinity records.

### Population demographics

- **Ethnicity/ancestry:** CMN incidence is reported to be independent of skin colour or ethnicity; no ancestry-specific NCM risk is established. NCM has been reported from Europe, North America, East Asia (PMID:37777590, PMID:41183822), South Asia (PMID:38803399), the Middle East (PMID:42626233) and South America (PMID:41417533). **No HANCESTRO-bindable population-specific effect was identified.**
- **Geographic distribution:** worldwide; no endemic area.
- **Sex ratio:** **male predominance among symptomatic NCM.** 76% male among 74 published cases (PMID:35535823); male sex was an **independent** predictor of neurological abnormality in the GOSH cohort (PMID:18671780). Note the contrast with CMN itself, which is commonly reported with a slight female predominance (≈3:2) — so the male skew appears to be in *CNS involvement*, not in naevus occurrence. Record them separately.
- **Age distribution:** bimodal as above. Rahman's published-case series had a mean age of 16.66 years (PMID:35535823), reflecting inclusion of surgically managed older patients; the mortality burden is concentrated under 5.

---

## 10. Diagnostics

### 10.1 Clinical / diagnostic criteria

**Kadonaga & Frieden (1991) remain the reference criteria** (PMID:1869648; restated verbatim in the 2025 review, PMID:41141235):

> "(1) The presence of a large congenital melanocytic nevus (greater than 20 cm in diameter) and/or multiple CMNs (> 3 in number), in association with meningeal melanosis or melanoma; (2) Histopathological examination revealing benign melanocytic infiltration in the meningeal lesions, without evidence of cutaneous melanoma involvement; (3) Histologically benign cutaneous melanocytic nevi, with no evidence of meningeal melanoma infiltration."

Criteria 2 and 3 are **exclusions designed to separate NCM from metastatic melanoma**; they were written before MRI screening and before molecular diagnosis, and they are now supplemented rather than replaced. Krengel's consensus descriptors (projected adult size bands, satellite count in infancy, site, colour heterogeneity, surface rugosity, hypertrichosis grade, nodules) are the standard way to record the cutaneous phenotype, with "moderate to excellent interobserver agreement for categorization of the clinical descriptors (kappa values 0.54-0.93)" (PMID:22982004).

### 10.2 Imaging — the single most important investigation

- **MRI brain (and spine) with and without contrast is the modality of choice.** "Brain MRI is considered the imaging modality of choice for identifying leptomeningeal and parenchymal melanocytic infiltration, which often appears as abnormal contrast enhancement on T1-weighted sequences" (PMID:41141235).
- **Signature finding: intrinsic T1 shortening (T1 hyperintensity without contrast) from melanin**, bilaterally in the **amygdala/anterior temporal lobes**, with the cerebellum, pons, medulla, interpeduncular fossa and base of brain next most frequent; plus **diffuse leptomeningeal enhancement** of brain and spine in diffuse disease.
- **Site frequency:** "NCM lesions were most frequently seen in the amygdala, followed by the cerebellum, brainstem, and cerebral hemispheres" (PMID:37777590).
- **Protocol:** the 2024 review describes 1.5 T T1-weighted (axial, sagittal, coronal), T2-weighted and T2* acquisitions, noting that contrast-enhanced sequences become more necessary as the brain myelinates (PMID:39518313).
- **Who to image:** "The Nevosurgery Network, therefore, recommends MRI examinations in cases of GCMN (>40 cm projected adult size (PAS)), and/or the presence of >20 concomitant nevi, and/or neurological symptoms" (PMID:39518313). GOSH uses a broader criterion — **a single screening MRI in any child with more than one CMN at birth, independent of size and site**, and concludes: "For screening for congenital neurological lesions a single MRI in multiple CMN is a clinically relevant strategy" (PMID:25966033). **These two recommendations differ and the disagreement should be curated, not reconciled.**
- **Timing:** best before extensive myelination (i.e. in the first months of life), because myelin reduces the conspicuity of intrinsic T1 hyperintensity.
- **Why the MRI matters prognostically:** "Abnormal MRI was the most significant predictor of all outcome measures" (abnormal neurodevelopment, seizures, requirement for neurosurgery) (PMID:25966033). And for malignancy: "the rate of melanoma is higher with positive MRI (detection of melanin in the CNS) than in patients with negative MRI (12% vs. 2%)" (PMID:39518313).
- **Adjuncts:** MR angiography; **FDG-PET/PET-MRI**, which demonstrated FDG avidity in an epidural thoracic melanoma deposit (PMID:38803399); visual evoked potentials (prolonged latencies in the optic-neuropathy case, PMID:38803399). Ruggieri's recommended work-up is "physical examination, ophthalmoscopy, brain/spinal cord magnetic resonance imaging (MRI) and angiography (MRA), positron emission tomography (PET), and video-EEG and IQ testing" (PMID:33048248).

### 10.3 Laboratory, CSF and biopsy

- **CSF examination** — recommended since 1991: Kadonaga & Frieden's "Recommended diagnostics include cerebrospinal fluid analysis and MRI with contrast enhancement" (PMID:1869648). CSF cytology plus immunohistochemistry confirmed leptomeningeal melanosis in a 5-month-old (PMID:29948137). Melanin-laden cells, raised protein and raised opening pressure are the typical findings.
- **CSF liquid biopsy for the NRAS mutation** is the most important recent diagnostic advance: in primary diffuse leptomeningeal melanomatosis, Baumgartner et al. "show, for the first time, that this somatic mutation can be exploited for cerebrospinal fluid liquid biopsy detection, revealing a novel potential biomarker for diagnosis and monitoring of PDLMM" (PMID:33921303). Serial ddPCR of CSF NRAS mutant allele frequency tracks disease burden and falls with treatment. **This is the right basis for a biomarker/readout record, and it is also the non-invasive route to a molecular diagnosis when lesional CNS tissue is unobtainable.**
- **Biopsy / histopathology** — skin: naevomelanocytes in dermis and subcutis, often with deep adnexal and neurovascular extension; CNS: melanin-pigmented spindled/epithelioid melanocytes in the pia-arachnoid and perivascular Virchow–Robin spaces. **IHC: Melan-A, S100 and HMB-45 positive** (PMID:41141235). **H3K27me3 immunohistochemistry is diagnostically useful** for the hardest question — melanoma vs proliferative nodule: loss in 4/5 melanomas, 0/20 nodules (PMID:27849631). Ki-67/MIB-1 for proliferative index (PMID:24713450).
- **No blood or urine biochemical marker exists.** No LOINC-codable NCM-specific analyte was identified; do not invent one.
- **Electrophysiology:** video-EEG for seizure localisation (epileptiform discharges over the right frontal region in PMID:33257354); VEP for optic involvement.

### 10.4 Genetic testing

| Approach | Utility in NCM |
|---|---|
| **Targeted hotspot testing of lesional tissue (NRAS codon 61, BRAF V600)** | **The test of choice.** Must be performed on **affected tissue** — naevus skin, CNS lesion, or CSF cfDNA — never on blood. Sensitive methods matter because mutant allele fraction can be low: Charbel used Sanger, pyrosequencing, HRM and "mutation enrichment by an enhanced version of ice-COLD-PCR" (PMID:24129063); ddPCR is now standard for CSF (PMID:33921303; PMID:38254245) |
| **WES / WGS of lesional tissue** | Informative for progression and for the ~25% hotspot-negative group. Multiregional exome sequencing resolved which mutation drove malignant progression in one autopsy case (PMID:38254245); exome of five large-giant naevi showed NRAS was the **sole** recurrent somatic event (PMID:24129063) |
| **Copy-number analysis (array/WGS) of a new or progressive CNS lesion** | **Decisive for the malignant-vs-benign question** (PMID:27933403). Should be regarded as part of the diagnostic standard for progressive CNS melanotic disease |
| **Germline WES/WGS, CMA, karyotype, FISH** | **Expected normal and not diagnostic.** A 2026 prenatal case had negative CNV-seq and WES (PMID:41474606) — a negative germline test does not exclude NCM |
| **mtDNA testing, repeat-expansion testing** | **Not applicable** |

### 10.5 Differential diagnosis

| Condition | Distinguishing features |
|---|---|
| **Metastatic melanoma to the leptomeninges** | Kadonaga criteria 2–3 exist to exclude it; a primary cutaneous melanoma must be absent |
| **Primary leptomeningeal melanocytic neoplasm *without* CMN (circumscribed melanocytoma / meningeal melanoma)** | **Molecularly distinct.** "GNAQ(Q209) mutations were present in eleven LMNs, while two of 20 cases carried a GNA11(Q209) mutation"; these tumours "harbor oncogenic mutations in GNAQ and GNA11 but lack mutations in BRAF, NRAS and HRAS" (PMID:25315378). Also SF3B1/EIF1AX in 8/24 (33%), which "underscores that these tumors genetically resemble uveal melanoma" (PMID:26769193). **The WHO 2021 CNS classification separates diffuse meningeal melanocytic neoplasms (meningeal melanocytosis / melanomatosis — NRAS-associated) from circumscribed ones (melanocytoma / melanoma — GNAQ, GNA11, PLCB4, CYSLTR2)**, which maps exactly onto this molecular split |
| **Primary CNS melanoma arising in NCM** | Same NRAS driver as the naevi, **plus** whole-arm copy-number gains/losses (PMID:27933403) |
| **Proliferative nodule in a CMN** | H3K27me3 retained; no copy-number signature (PMID:27849631) |
| **Melanotic schwannoma** | Morphology plus GNAQ status; a plexiform melanocytic schwannoma was found in a giant CMN (PMID:41624622) |
| **Other mosaic RASopathies and neurocutaneous syndromes** | Sebaceous naevus syndrome, phakomatosis pigmentovascularis/pigmentokeratotica, encephalocraniocutaneous lipomatosis, McCune-Albright (PMID:40532825); naevus of Ota/dermal melanocytosis; Sturge-Weber. Note one report of NCM **co-existing with neurofibromatosis** (PMID:42240487) |
| **Causes of T1-hyperintense basal-ganglia/temporal signal** | Haemorrhage, calcification, melanin from other sources, high-protein content, manganese deposition |

### 10.6 Screening

- **Newborn / carrier / cascade screening: not applicable** (non-heritable somatic mosaicism).
- **The screening that matters is phenotype-triggered neuroimaging** (§10.2) — one MRI in infancy, then symptom-triggered re-imaging with contrast of brain and spine.
- **Surveillance of the skin** for melanoma and for new nodules, with AI-assisted total-body dermoscopic mapping now being described (PMID:41624622).
- **Prenatal:** fetal MRI/ultrasound can detect NCM (PMID:41474606) but is not a screening strategy; there is no population screening test.
- **Periodic brain and spine imaging** is recommended by some authors for established NCM (PMID:38803399) — frequency is not evidence-based.

---

## 11. Outcome / Prognosis

### Survival and mortality

| Measure | Value | Source |
|---|---|---|
| **Historical prognosis of symptomatic NCM** | "symptomatic neurocutaneous melanosis had an extremely poor prognosis" — even without malignancy; leptomeningeal melanoma in 62% of 39 cases | PMID:1869648 |
| **Mortality in symptomatic NCM** | "approximately 50% of affected children succumbing to the disease by the age of five years" | PMID:41141235 |
| **Mortality in a 14-patient MRI-defined series** | 6/14 died; all six had diffuse leptomeningeal deposits and four had leptomeningeal melanoma | PMID:22469364 |
| **Death in a prospective CMN cohort (not NCM-selected)** | 3/120 (2.5%) — one from neuromelanosis, two from melanoma; death significantly associated with CMN size >40 cm | PMID:18671780 |
| **Age at death from melanoma** | mean 3.9 y, median 2.5 y | PMID:28078671 |
| **Overall survival, primary diffuse leptomeningeal melanomatosis** | "a median overall survival of 4 months from diagnosis"; the index trametinib/everolimus→nivolumab/ipilimumab patient achieved 7 months | PMID:33921303 |
| **Melanoma lethality in large CMN** | "55% were fatal, with age at death ranging from 0.9 to 40 (mean 10) years" | PMID:23182059 |

### Melanoma incidence (the dominant hard outcome)

| Denominator | Incidence | Source |
|---|---|---|
| All CMN, pooled systematic review (6,571 patients) | "46 patients (0.7%) developed 49 melanomas"; mean age at diagnosis 15.5 y, median 7; "patients with CMN carry an approximately 465-fold increased relative risk of developing melanoma during childhood and adolescence" | PMID:16792745 |
| Large CMN, systematic review (2,578 patients) | 52 melanomas (**2%**); estimated incidence "2.3 per 1000 patient-years" | PMID:23182059 |
| GOSH prospective cohort (448 patients), childhood 0–16 y | "In the whole group the incidence of melanoma in childhood (0–16 years) is 2·2%"; "an incidence of melanoma in children with CMN > 60 cm projected adult size of 8%, and an incidence of 1% in those who are in any other cutaneous phenotypic group" | PMID:28078671 |
| GOSH registry, questionnaire cohort | 1.4% overall; **14%** in the >60 cm PAS / multiple-CMN group | PMID:18811688 |
| Stratified by MRI | **12% with positive MRI vs 2% with negative MRI** | PMID:39518313 |

Note that **7 of 10 GOSH melanoma cases occurred in the >60 cm PAS or multiple-CMN-without-a-large-naevus group** (PMID:28078671) — the "multiple small/medium CMN, no giant naevus" phenotype is **not** low risk.

### Morbidity, disability and function

- Abnormal neurodevelopment in **20%** of a CMN cohort, present across all naevus size categories (PMID:18811688).
- Epilepsy in 45–55% of published NCM cases, sometimes drug-resistant and surgically relevant (PMID:35535823; PMID:41467858).
- Shunt-dependent hydrocephalus in ~24% (PMID:35535823).
- **Crucially, symptomatic group-1 disease can still have a benign trajectory:** group 1 "was not associated with malignancy or death during the study period, even when symptomatic with seizures or developmental delay" (PMID:25966033). This is the counterweight to the historical nihilism of the 1991 literature.
- Growth/endocrine morbidity: accelerated BMI gain, insulin insensitivity, limb asymmetry from reduced fat and muscle under large naevi (PMID:26286459).
- Psychosocial morbidity is common and **independent of lesion characteristics** (PMID:23182059); no validated NCM-specific QoL instrument exists (see §3.5).

### Prognostic factors

**Favourable:** normal screening MRI; "intraparenchymal melanosis alone" (Waelchli group 1); **normal whole-genome copy number** in a CNS lesion; no satellite naevi at birth ("No complications were seen in the 16 patients with no satellite lesions at birth", PMID:18671780); PAS <20 cm.

**Adverse:** abnormal MRI, and in particular **diffuse leptomeningeal melanocytosis** (the pattern present in every fatal case in PMID:22469364); Waelchli group 2 pathology; PAS >40 cm and especially >60 cm; >20 satellite naevi; male sex (for neurological involvement); any **stepwise** neurological change; **copy-number gains/losses** on CNS lesion genomics (PMID:27933403); **loss of H3K27me3** in a nodular lesion (PMID:27849631); acquisition of a second RAS or GNAS lesion (PMID:38254245; PMID:34994589); unrecognised raised intracranial pressure, which delayed diagnosis in 67% of PDLMM cases (PMID:33921303).

**Prognostic biomarkers, ranked by strength of evidence:** (1) whole-genome copy number on CNS tissue; (2) CSF NRAS mutant allele frequency by ddPCR, serially; (3) H3K27me3 IHC on a nodule; (4) MRI pattern (focal vs diffuse); (5) Ki-67/MIB-1 and pERK as pharmacodynamic rather than prognostic readouts.

---

## 12. Treatment

**There is no curative therapy.** "Currently, there is no established curative treatment for NCM" and management "largely palliative" (PMID:41141235). Ruggieri summarises current practice as: "Treatment strategies include laser therapy, chemical peeling, dermabrasion, and surgical removal/grafting for CMNs and shunt surgery and surgical removal/chemo/radiotherapy for CNS lesions" (PMID:33048248).

### 12.1 Targeted pharmacotherapy — MEK inhibition (the main therapeutic development)

| Agent | Evidence | Outcome |
|---|---|---|
| **Trametinib** (MEK1/2 inhibitor; **CHEBI:75998** ✅) | GOSH case series of **four patients with NRAS-mutated CNS melanoma, three with CMN**: "This demonstrated measurable and objective relief of symptoms and signs in all patients, although to varying degrees" (PMID:28078671) | Symptomatic benefit; not curative |
| Trametinib | 13-year-old with amygdala melanosis and seizures: "The patient is being managed with levetiracetam and trametinib and shows no further neurological decline at 1-year follow-up, providing prognostic hope in this case of NCM" (PMID:33257354) | Stable at 1 year |
| Trametinib | 5-month-old with GCMN, leptomeningeal melanosis and hydrocephalus; VP shunt then "trametinib, a MAPK/Erk kinase inhibitor for 7 months"; at 30 months developed hemiparesis and status epilepticus and "eventually succumbed to malignant transformation of leptomeningeal disease" (PMID:29948137) | Did not prevent transformation |
| Trametinib, pooled | "trametinib showed 'mild clinical improvement' with symptom-free periods of 'one to nine months'" (PMID:41141235) | Modest, time-limited |
| **MEK162 / binimetinib** (**CHEBI:145371** ✅) | 13-year-old boy, NRAS Q61K, progressive leptomeningeal melanocytosis, compassionate use at **45 mg BID**; died of respiratory failure on day 5, so efficacy was unassessable, but paired tissue showed "Lower MIB-1 expression and lower pERK expression in the post-treatment samples compared to pre-treatment, suggesting a potential effect of MEK inhibiting therapy" (Küsters-Vandevelde HVN, et al. Acta Neuropathol Commun. 2014;2:41. **PMID:24713450**) | Pharmacodynamic effect demonstrated; clinical effect unknown |
| **Mirdametinib** | **`NCT07891286`** (NCI, **Phase 2, not yet recruiting, estimated start 4 January 2027**): oral mirdametinib **2–4 mg/m² twice daily, 3 weeks on / 1 week off**, ages 3–40, LGCMN ≥20 cm, Karnofsky ≥70%, no prior melanoma; primary endpoint "whether treatment with mirdametinib results in objective decreases in the largest diameter of LGCMN" over up to 24 months (✅ ClinicalTrials.gov API v2) | **The first prospective interventional trial of MEK inhibition in this disease** |
| **BRAF inhibition** (for the BRAF-V600E minority) | "sustained neurologic and cutaneous improvement following BRAF inhibition" in BRAF-V600E NCM (Doolan BJ, et al. JAMA Dermatol. 2026. **PMID:42384401**) | Genotype-directed; promising single case |

Suggested treatment annotations: `treatment_term` **NCIT:C15986** Pharmacotherapy with `therapeutic_agent` CHEBI:75998 trametinib / CHEBI:145371 binimetinib, `therapeutic_modality: SMALL_MOLECULE`; or **NCIT:C93352** Targeted Therapy. (NCIT codes here are taken from the repository's own documented list and should still be re-verified with `just validate-terms`.)

### 12.2 PI3K / mTOR inhibition

- **Omipalisib / GSK2126458** (dual PI3K/mTOR) was the **most effective agent** against patient-derived NCM nevospheres: "The highest effect was obtained with GSK2126458, showing a viability reduction below 50%" (PMID:26354928); and separately "Omipalisib treatment prevented colony formation and induced autophagic cell death... omipalisib treatment as a monotherapy or in combination with MEK162 could be an effective therapeutic strategy to inhibit clonogenic growth" (PMID:29976629). **Not clinically approved for any indication.**
- **Alpelisib** (approved for PIK3CA-related overgrowth spectrum) reduced nevocytes in ex vivo explants from 10 patients: decreased cell density (p=0.0273), SOX10+ cell density (p=0.0391) and %S-100+ area (p=0.0078), "probably inducted by autophagy" (Tomás-Velázquez A, et al. JEADV. 2024. **PMID:38071601**). This is the most immediately repurposable PI3K agent because its paediatric safety profile is established in another mosaicism.
- **Everolimus** has been used in combination with trametinib in PDLMM (PMID:33921303).

### 12.3 Topical / local therapy — the most promising preclinical direction

> "Cutaneously delivered MEK, PI3K, and c-KIT inhibitors or proinflammatory squaric acid dibutylester (SADBE) achieved major regressions. SADBE triggered innate immunity that ablated detectable nevocytes, fully prevented melanoma, and regressed human giant nevus xenografts."
> — Choi YS, Erlich TH, von Franque M, et al. *Topical therapy for regression and melanoma prevention of congenital giant nevi.* Cell. 2022;185(12):2071–2085.e12. **PMID:35561684**

A commentary frames the translational significance: "topical application of a proinflammatory hapten for alopecia treatment [squaric acid dibutylester (SADBE)] caused nevus regression and prevented melanoma in an Nras mouse CGN model" (PMID:35718707). **Clinical translation has begun:** `NCT04999631`, "SADBE for Congenital Melanocytic Nevi", Early Phase 1 (✅ ClinicalTrials.gov; listed as not-yet-recruiting with an estimated 2027 start). Note that topical therapy addresses the **cutaneous** burden and melanoma prevention — it does not reach the CNS.

### 12.4 Immunotherapy, chemotherapy and radiotherapy

- **Checkpoint blockade:** intravenous nivolumab + ipilimumab with concomitant intensive intraventricular chemotherapy, after trametinib + everolimus, gave "temporary significant clinical improvement and overall survival of 7 months" in paediatric PDLMM (PMID:33921303).
- **Chemotherapy / radiotherapy for CNS melanoma:** largely ineffective — "Symptomatic NCM is refractory to radiotherapy and chemotherapy and has a poor prognosis" (PMID:29948137). Three Chinese children treated with resection plus chemotherapy/radiotherapy all died of raised intracranial pressure and hydrocephalus (PMID:41183822). Temozolomide and intrathecal chemotherapy are used but unsupported by controlled data.
- **Epigenetic combination:** azacitidine + trametinib against leptomeningeal melanosis in CMNS (PMID:41973363) — single report, 2026.

### 12.5 Surgical and interventional

| Intervention | Evidence | Suggested NCIT |
|---|---|---|
| **CSF diversion (VP/ventriculoatrial shunt, ETV)** — the commonest operation | "The most common surgical technique was CSF shunting (43%, 24/56 operations)" (PMID:35535823). Effective for hydrocephalus (PMID:29948137). **Carries the specific hazard of peritoneal seeding of malignant melanocytes** (PMID:38254245) | NCIT:C15329 Surgical Procedure **[verify]** |
| **Resection / biopsy of a CNS mass** | Diagnostic and decompressive; does not cure diffuse disease (PMID:41183822) | NCIT:C15329 **[verify]** |
| **Epilepsy surgery** | Relevant where NCM has produced focal cortical dysplasia with drug-resistant epilepsy (PMID:41467858) | **[verify]** |
| **Naevus excision ± tissue expansion, grafting; laser, dermabrasion, chemical peel** | Cosmetic and psychosocial, **not protective against melanoma**. Tissue expansion in 68 cases was "a safe and ideal surgical method for the early treatment of congenital giant melanocytic nevus" (PMID:42023207). But GOSH's position is explicit: "routine surgery has not been demonstrated to reduce the risk of malignancy and is, therefore, for cosmetic reasons only"; "early surgery has not been shown to be advantageous and carries increased anaesthetic risk"; "there is some evidence that surgical intervention may adversely affect the behaviour of the CMN cells" (PMID:19244003). **This is a genuine, live controversy and both positions should be curated** | NCIT:C15329 **[verify]** |

### 12.6 Supportive, rehabilitative and strategic

Antiepileptic drugs (levetiracetam was used with trametinib in PMID:33257354); analgesia and management of raised ICP; developmental, physical, occupational and speech therapy; **multidisciplinary care is universally recommended** — "A multidisciplinary approach is necessary in the management of NCM patients" (PMID:29948137); GOSH practice is "patients are treated in a multidisciplinary-team setting which includes the specialties of paediatric dermatology, plastic surgery and neuroradiology with access to neurology, neurosurgery and oncology" (PMID:19244003). Suggested: NCIT:C15747 Supportive Care, NCIT:C15315 Rehabilitation, NCIT:C15302 Physical Therapy **[all verify]**.

**Treatment algorithm, as the literature supports it:**
1. Phenotype the naevi (Krengel descriptors) → 2. Screening MRI brain (±spine) in infancy → 3. If normal: cutaneous surveillance; re-image only on stepwise neurological change → 4. If abnormal: subclassify (group 1 intraparenchymal melanosis alone vs group 2 other pathology) → 5. Group 1: symptomatic management, surveillance → 6. Group 2 / new or progressive melanotic disease: contrast MRI brain **and spine**, biopsy where feasible, **copy-number analysis**, CSF cytology + ddPCR NRAS → 7. Benign and stable: surveillance; malignant or progressive: genotype-directed MEK inhibitor (trametinib) for NRAS-mutant, BRAF inhibitor for BRAF-V600E, ± checkpoint blockade, ± CSF diversion; consider trial enrolment → 8. Cosmetic/psychosocial management of the naevi, deliberately decoupled from melanoma prevention.

### 12.7 Pharmacogenomics and adverse events

- **Pharmacogenomics in the conventional (germline CYP) sense: no NCM-specific data; no PharmGKB/CPIC guideline identified.** The actionable genotype is **somatic**: NRAS codon 61 → MEK inhibitor; BRAF V600E → BRAF inhibitor; PI3K-pathway activation → PI3K inhibitor. This is precision oncology applied to a benign-origin mosaic disorder, and the drug–genotype pairing is the whole therapeutic rationale.
- **Adverse events** are those of the drug classes in children: MEK inhibitors — acneiform rash, paronychia, diarrhoea, peripheral oedema, reduced ejection fraction, retinopathy/central serous retinopathy, raised CK (hence the `NCT07891286` cardiac and blood-pressure eligibility requirements); PI3K inhibitors — hyperglycaemia, rash, stomatitis, diarrhoea; SADBE — deliberate contact dermatitis. **No NCM-specific FAERS analysis was identified.**

---

## 13. Prevention

- **Primary prevention: not possible.** The causal event is a spontaneous somatic mutation in early embryogenesis. There is no vaccine, no modifiable exposure, and no behavioural intervention that prevents NCM. **Do not create primary-prevention records beyond this statement.**
- **Secondary prevention (early detection) is where everything useful sits:**
  - A **single screening MRI** in infancy for every child with more than one CMN at birth (GOSH, PMID:25966033) or for GCMN >40 cm PAS / >20 satellites / neurological symptoms (Nevosurgery Network, PMID:39518313).
  - **Urgent contrast MRI of brain and spine on any stepwise neurological or developmental change** (PMID:25966033).
  - Lifelong cutaneous surveillance, including for new dermal/subcutaneous nodules; AI-assisted total-body dermoscopy is emerging (PMID:41624622).
  - "Patients with large or multiple congenital nevi should therefore be investigated early to facilitate treatment" (PMID:29948137).
  - Serial CSF ddPCR NRAS where CNS disease is known (PMID:33921303).
- **Tertiary prevention:** shunting before irreversible damage from raised ICP; seizure control; genotype-directed MEK/BRAF inhibition to delay progression; **melanoma prevention is the explicit goal of topical SADBE** — it "fully prevented melanoma" in the mouse model and regressed human xenografts (PMID:35561684), and is the first intervention with a prevention claim.
- **Immunization: not applicable.**
- **Genetic screening / prenatal / PGD: not applicable** for recurrence prevention, because the mutation is post-zygotic and not transmitted. Prenatal **detection** of established NCM by fetal MRI is possible (PMID:41474606) but is not prevention.
- **Genetic counselling is indicated and its central message is reassurance about recurrence.** NRAS Q61 CMN/NCM is sporadic and mosaic, so **recurrence risk for siblings and for the patient's own offspring is not increased** on current evidence. Counsel on the 25% familial-CMN-history observation and its uncertain meaning (PMID:18811688), and on the mosaic basis of phenotypic variability. Suggested: NCIT:C15240 Genetic Counseling **[verify]**.
- **Public-health and environmental interventions: not applicable.** **Prophylactic medication: none established** — note explicitly that prophylactic naevus excision is **not** supported as melanoma prophylaxis (PMID:19244003; PMID:16792745).

---

## 14. Other Species / Natural Disease

### Natural disease

**One naturally occurring case of NCM has been reported in a non-human animal**, and it appears to be the only one:

> "Neurocutaneous melanosis represents 'a rare phakomatosis characterized by proliferation of melanin-producing cells in both the skin and the brain.' This case study examined the condition in a young female cynomolgus macaque, documenting skin lesions resembling blue nevi and brain involvement with pigmented cell infiltration. 'Melanosomes were observed in pigmented cells in the brain by electron microscopic examination.' ... the authors noting this may represent **the first documented instance in animals**."
> — Chen Y, Deng W, Zhu H, et al. *The pathologic features of neurocutaneous melanosis in a cynomolgus macaque.* Vet Pathol. 2009. **PMID:19276048**

Species: *Macaca fascicularis* (cynomolgus macaque) — NCBITaxon:9541 **[verify]**. The genotype of that animal was not determined.

**No naturally occurring NCM is recorded in dogs, cats, cattle or horses** in the sources searched. A targeted PubMed query for meningeal/leptomeningeal melanosis in veterinary species returned exactly one record — the macaque case above.

### Comparative biology: congenital melanocytic proliferation in other species

| Species | Entity | Identifier | Relevance |
|---|---|---|---|
| **Pig** (*Sus scrofa*) | **Melanoma, congenital** | **OMIA:000634-9823** ✅ (OMIA URL encodes NCBI taxon 9823) | Congenital melanocytic neoplasia with a heritable component |
| **Pig** (Sinclair miniature swine) | **Melanoma, Sinclair swine cutaneous malignant** | **OMIA:000633-9823** ✅ | Congenital or early-postnatal cutaneous melanoma with **spontaneous regression accompanied by depigmentation** — a long-standing large-animal model of human melanoma; first observed 1967 at 21% incidence. Both cutaneous and visceral congenital melanomas are documented. The **spontaneous immune-mediated regression** is of direct interest given the SADBE innate-immunity mechanism (PMID:35561684) |
| **Dog** | Spontaneous melanoma | — | Used for cytokine and gene-therapy protocols; not a CMN/NCM model |
| **Grey horse** | Dermal melanoma (*STX17* duplication) | — | A melanocytic proliferation model, not congenital, not RAS-driven **[verify genetics before citing]** |

### Orthologous genes

| Species | Gene | Identifier |
|---|---|---|
| Human | **NRAS** | **`hgnc:7989`** ✅ (HGNC REST) |
| Mouse | **Nras**, "Nras proto-oncogene, GTPase" | **MGI:97376** ✅ (Alliance of Genome Resources) |
| Rat, zebrafish, *Xenopus*, *Drosophila*, *C. elegans* | *Nras* / *nras* / *Ras85D* orthologs exist | **[verify each via Alliance before binding; use the MOD prefix per the repository's gene-namespace rule]** |

### Evolutionary conservation and transmission

RAS signalling and its codon-61 catalytic glutamine are **deeply conserved across metazoa**, and melanocytes are a conserved neural-crest derivative — which is why mouse models recapitulate the disease so well (§15). **Zoonotic potential: none. Cross-species transmission: not applicable** (a somatic mutation is not transmissible).

---

## 15. Model Organisms

### 15.1 Mouse — the CNS phenotype model (the most faithful to NCM)

> "NRAS mutations are common in human melanoma. To produce a mouse model of NRAS-driven melanoma, we expressed oncogenic NRAS (NRAS(G12D)) in mouse melanocytes. **When NRAS(G12D) was expressed in the melanocytes of developing embryos, it induced melanocyte proliferation and congenital melanocytic lesions reminiscent of human blue nevi but did not induce cutaneous melanoma. Unexpectedly, however, it did induce early-onset primary melanoma of the central nervous system (CNS).** The tumors were rapidly proliferating and caused neurologic symptoms, rapid health deterioration, and death. NRAS is not a common driver oncogene of primary melanoma of the CNS in adults, but we report two cases of primary melanoma of the CNS in children, both of which carried oncogenic mutations in NRAS. We conclude that acquisition of somatic mutations in NRAS in CNS melanocytes is a predisposing risk factor for primary melanoma of the CNS in children, and we present a mouse model of this disease."
> — Pedersen M, Küsters-Vandevelde HVN, Viros A, et al. Cancer Discov. 2013;3(4):458–69. **PMID:23303902**

- **Model type:** genetically engineered mouse (*Mus musculus*, NCBITaxon:10090 **[verify]**); tyrosinase-promoter-driven, embryonically expressed oncogenic Nras.
- **Phenotype recapitulation:** **high fidelity for the CNS arm** — congenital melanocytic lesions *plus* early-onset primary CNS melanoma with neurological decline and death. This is the only model that reproduces the specific human combination.
- **Limitations:** uses **NRAS G12D**, not the human Q61K/Q61R allele; lesions resemble **blue naevi** rather than giant CMN; germline-driven lineage-wide expression rather than true mosaicism; no cutaneous melanoma. Suggested `divergences`: `PROXY_QUANTITY` (different allele), `POPULATION_MISMATCH` or `BOUNDARY_OMISSION` (lineage-wide vs mosaic), `SPECIES_MISMATCH`.
- **Relationship to the pathograph:** `RECAPITULATES` for a CNS-melanoma node; `PARTIALLY_RECAPITULATES` for congenital melanocytic proliferation; `FAILS_TO_RECAPITULATE` for giant CMN.

### 15.2 Mouse — the Q61K melanoma model

> "In human cutaneous malignant melanoma, a predominance of activated mutations in the N-ras gene has been documented. To obtain a mouse model most closely mimicking the human disease, a transgenic mouse line was generated by targeting expression of dominant-active human N-ras (N-RasQ61K) to the melanocyte lineage by tyrosinase regulatory sequences (Tyr::N-RasQ61K). **Transgenic mice show hyperpigmented skin and develop cutaneous metastasizing melanoma.** Consistent with the tumor suppressor function of the INK4a locus that encodes p16INK4A and p19(ARF), **>90% of Tyr::N-RasQ61K INK4a-/- transgenic mice develop melanoma at 6 months.** ... primary melanomas and metastases contain cells expressing the stem cell marker nestin..."
> — Ackermann J, Frutschi M, Kaloulis K, McKee T, Trumpp A, Beermann F. Cancer Res. 2005;65(10):4005–11. **PMID:15899789**

This is the **human Q61K allele** — the exact NCM mutation — in the melanocyte lineage. It gives hyperpigmentation and, with *Cdkn2a* loss, metastasising melanoma, modelling the **transformation step (chain step 8c)** rather than the congenital naevus itself. Supporting resources: a histopathological atlas and classification of melanocytic lesions in `Tyr::NRASQ61K; Cdkn2a−/−` mice (PMID:23647911) and a reproducible simplified classification (PMID:29224244); a `Pax3GFP` reporter allele for sorting melanoma cells (PMID:26587692); `Sall4` dependence of primary tumour formation (PMID:34417458).

### 15.3 Mouse and human xenograft — the therapeutic platform

Choi et al. built the only platform designed for *therapeutic* testing in giant congenital naevi: "The authors presented preclinical models, including **multiple genetically engineered mice and xenografted human lesions**, which enabled testing locally applied pharmacologic agents to avoid surgery" (PMID:35561684). Readouts: nevocyte ablation, melanoma prevention, xenograft regression. This is the model that produced an actionable clinical candidate (SADBE → `NCT04999631`).

### 15.4 Patient-derived in vitro models (NAMs)

> "We generated nevomelanocytic spheroids in vitro from lesions of the spinal cord, brain, and skin from 4 NCM patients... Cultured cell identity was confirmed by demonstration of the same NRAS mutation found in the original lesions and by immunophenotyping... Cultured cells were growth-factor dependent, grew as spheroids on Geltrex matrix, and maintained their clonogenicity in vitro over passages. Skin-derived cells formed more colonies than CNS-derived cells... NCM lesional spheroids represent a new and reliable experimental model of NCM for use in drug testing and mechanistic studies."
> — Basu D, Salgado CM, Bauer BS, et al. Neuro Oncol. 2016. **PMID:26354928**

- **The only human NCM-derived cellular model, and it is genotype-verified against the patient's own lesion** — which makes it the strongest in vitro system available.
- Used to screen vemurafenib, MEK162, GDC0941 and GSK2126458 (PMID:26354928) and to establish Akt-dependence of clonogenicity and omipalisib-induced autophagic death (PMID:29976629).
- **Limitations:** 4 patients; spheroids, not an organoid with stroma, vasculature or immune compartment; cannot report CSF dynamics, hydrocephalus or seizures. A link to a tissue- or organism-scale node would be a **2-step upward extrapolation** and must carry `limitations` and a `SCALE_EXTRAPOLATION` divergence.
- Ruggieri also notes an experimental NCM cell line, **"YP-MEL"** (PMID:33048248) — **[verify provenance before citing]**.
- **Ex vivo organotypic explants** of patient naevus tissue (10 patients, 5-day culture) supported the alpelisib result (PMID:38071601) — an organotypic model that retains tissue architecture.

### 15.5 Model types with no NCM representation

**No zebrafish, *Drosophila*, *C. elegans*, yeast, iPSC-derived or organ-chip model of NCM was identified**, and no IMPC/KOMP conditional allele study addressing the CNS phenotype. Resources to search if building the entry out: MGI, IMSR, Alliance of Genome Resources, Cellosaurus (for any derived line), ATCC.

---

## 16. Curation notes for the dismech entry

These are judgements about how this disease should be modelled, offered because the report is to be used to populate a KB entry.

1. **Granularity / lump–split.** NCM is **not** an independent disease of unknown aetiology; it is the CNS-involvement phenotype of **congenital melanocytic naevus syndrome**, a mosaic NRAS RASopathy. It nonetheless has its own MONDO term, OMIM entry, ORPHA code, diagnostic criteria and literature, so a `Disease` entry bound to MONDO:0009578 is defensible. **Check for an existing CMN/CMNS entry before creating this one**, and if both exist, record the relationship explicitly in `mappings.mondo_mappings` with a `skos:broadMatch` to the parent concept rather than letting two entries share a `disease_term`.

2. **Somatic mosaicism is structural, not incidental.** `HP:0001442` *Typified by somatic mosaicism* is already an HPO annotation for OMIM:249400. Use the `somatic-mosaicism` skill: an `inheritance` block bound to HP:0001442 with its own cited evidence, plus `variant_origin: SOMATIC` and `functional_impact_category: GAIN_OF_FUNCTION` on the NRAS `genetic_context`. The entry is a candidate member of the `Somatic_Mosaic_Disorders` grouping.

3. **The cell of origin is derivable, not a slot.** Mark the initiating node (the NRAS codon-61 lesion) with `genetic_context: {variant_origin: SOMATIC, functional_impact_category: GAIN_OF_FUNCTION}` and bind `cell_types` there. The honest binding is the **neural crest cell / melanoblast** (CL:0011012 ✅ / CL:0000541 ✅), because Kinsler's own wording is that the mutation "probably occurs in a progenitor cell in the developing neural crest or neuroectoderm" — and the non-melanocytic CNS malformations require a progenitor broader than the melanocyte. `just check-cancer-origin` may report more than one derived origin; that is the correct signal here and should be explained in `notes`, not engineered away.

4. **Do not merge the benign and malignant entities.** The most important finding in the modern literature is that **new or progressive melanotic CNS disease in a CMN patient is primary CNS melanoma, not "NCM"** (PMID:27933403). Model stable intraparenchymal melanosis and primary CNS melanoma as distinct nodes with distinct prognoses, linked by an explicit transformation edge whose evidence is the copy-number and H3K27me3 work.

5. **Candidate mechanism modules to conform to:** the hallmarks-of-cancer family (for the transformation arm), and any RAS/MAPK or MEK-inhibitor module. Run `just list-modules` before choosing — do not assume a module exists under a guessed name.

6. **Knowledge gaps worth recording as `discussions`:**
   - **`HUMAN_MODEL_MISMATCH`:** the best CNS model uses NRAS **G12D**, not the human Q61K/Q61R, and produces blue-naevus-like rather than giant congenital lesions (PMID:23303902); and the Q61K model requires *Cdkn2a* loss for melanoma, a cooperating lesion not established in human CMN (PMID:15899789).
   - **`KNOWLEDGE_GAP`:** no single-cell or spatial transcriptomics of human NCM; no metabolomic or proteomic dataset; no functional-genomics screen; no validated QoL instrument; the ~25% of CMN that are hotspot-negative (PMID:31111470) have no identified driver; the 25% familial-CMN-history signal (PMID:18811688) is unexplained.
   - **Unresolved clinical controversies to curate as such, not to resolve:** posterior-axial distribution as a risk factor (PMID:16310055 vs PMID:18671780); who should be screened by MRI (GOSH vs Nevosurgery Network); whether prophylactic naevus excision reduces melanoma risk (PMID:19244003).

7. **Evidence-source grading.** Grade from the quoted sentence: the GOSH, Orphanet, Japanese MRI and systematic-review material is `HUMAN_CLINICAL`; Ackermann, Pedersen, Choi (mouse arms) and Diener are `MODEL_ORGANISM`; Basu, Tomás-Velázquez and the nevosphere/explant work are `IN_VITRO`. Several reviews (Ruggieri PMID:33048248, Kinsler PMID:28078671) are `REVIEW_SYNTHESIS` for `quote_role` where the quoted sentence restates others' work. **Watch for the background-citation trap:** Pedersen's abstract states the human paediatric CNS-melanoma cases in a mouse paper — grade that `HUMAN_CLINICAL` with `quote_role: BACKGROUND` rather than forcing it to `MODEL_ORGANISM` or `OTHER`.

---

## Verified ontology term summary

**Resolved in this session and safe to use as leads (still re-run `just validate-terms` after binding):**

| CURIE | Label | Source |
|---|---|---|
| MONDO:0009578 | neurocutaneous melanocytosis | OLS4 ✅ |
| `hgnc:7989` | NRAS proto-oncogene, GTPase | HGNC REST ✅ |
| MGI:97376 | Nras (mouse) | Alliance ✅ |
| HP:0005603, HP:0002861, HP:0001250, HP:0000238, HP:0001305, HP:0100702, HP:0003396, HP:0006824, HP:0001263, HP:0001268, HP:0002858, HP:0200022, HP:0001522, HP:0001442, HP:0003745 | see §3.1 table | HPO annotation API ✅ |
| CL:0000148 | melanocyte | OLS4 ✅ |
| CL:0000541 | melanoblast | OLS4 ✅ |
| CL:0011012 | neural crest cell | OLS4 ✅ |
| UBERON:0000391 | leptomeninx | OLS4 ✅ |
| UBERON:0001876 | amygdala | OLS4 ✅ |
| UBERON:0002037 | cerebellum | OLS4 ✅ |
| UBERON:0000988 | pons | OLS4 ✅ |
| UBERON:0002097 | skin of body | OLS4 ✅ |
| GO:0000165 | MAPK cascade | OLS4 ✅ |
| GO:0007265 | Ras protein signal transduction | OLS4 ✅ |
| GO:0070374 | positive regulation of ERK1 and ERK2 cascade | OLS4 ✅ |
| GO:0030318 | melanocyte differentiation | OLS4 ✅ |
| GO:0043491 | phosphatidylinositol 3-kinase/protein kinase B signal transduction | OLS4 ✅ |
| CHEBI:89634 / CHEBI:25179 | Melanin / melanins | OLS4 ✅ |
| CHEBI:75998 | trametinib | OLS4 ✅ |
| CHEBI:145371 | binimetinib | OLS4 ✅ |
| OMIA:000633-9823, OMIA:000634-9823 | Sinclair swine cutaneous malignant melanoma; congenital melanoma (pig) | OMIA ✅ |

**Explicitly NOT verified and must be looked up before use:** every NCIT treatment code cited above (taken from the repository's own documentation, not from an ontology lookup this session); the ICD-10 and ICD-11 stem codes; NCBITaxon IDs for mouse and macaque; GO terms for melanin biosynthesis, TOR signalling, neural crest migration and melanosome; UBERON terms for temporal lobe, spinal cord, subarachnoid space, medulla and interpeduncular fossa; HPO terms for hypertrichosis, congenital melanocytic nevus, optic neuropathy and focal cortical dysplasia; the ClinVar accession for NRAS c.181C>A.

---

## Principal references

**Genetics and mechanism** — Kinsler VA, et al. J Invest Dermatol. 2013;133(9):2229–36. **PMID:23392294** · Charbel C, et al. J Invest Dermatol. 2014;134(4):1067–74. **PMID:24129063** · Salgado CM, et al. Pediatr Dev Pathol. 2015. **PMID:25490715** · Polubothu S, et al. Br J Dermatol. 2020. **PMID:31111470** · Kinsler VA, et al. Acta Neuropathol. 2017;133(2):329–31. **PMID:27933403** · Busam KJ, et al. Am J Surg Pathol. 2017;41(3):396–404. **PMID:27849631** · Takahashi H, et al. Acta Neuropathol Commun. 2024. **PMID:38254245** · Küsters-Vandevelde HV, et al. Pathol Oncol Res. 2015. **PMID:25315378**; Acta Neuropathol Commun. 2016. **PMID:26769193** · Roy SF, et al. Br J Dermatol. 2025. **PMID:40036344** · Jaeger ZJ, et al. J Am Acad Dermatol. 2025. **PMID:40532825**

**Clinical phenotype, CNS spectrum, epidemiology** — Kadonaga JN, Frieden IJ. J Am Acad Dermatol. 1991;24(5 Pt 1):747–55. **PMID:1869648** · Ruggieri M, et al. Childs Nerv Syst. 2020. **PMID:33048248** · Waelchli R, et al. Br J Dermatol. 2015;173(3):739–50. **PMID:25966033**; Br J Dermatol. 2015;173(6):1471–8. **PMID:26286459** · Kinsler VA, et al. Br J Dermatol. 2008;159(4):907–14. **PMID:18671780**; Br J Dermatol. 2009;160(1):143–50. **PMID:18811688**; Br J Dermatol. 2017;176(5):1131–43. **PMID:28078671** · Ramaswamy V, et al. Dev Med Child Neurol. 2012;54(6):563–8. **PMID:22469364** · Rahman RK, et al. Neurosurg Focus. 2022;52(5):E8. **PMID:35535823** · Takiya M, et al. Sci Rep. 2023;13:16442. **PMID:37777590** · Agero AL, et al. J Am Acad Dermatol. 2005. **PMID:16310055** · Krengel S, et al. Br J Dermatol. 2006. **PMID:16792745**; J Am Acad Dermatol. 2013. **PMID:22982004** · Vourc'h-Jourdain M, et al. J Am Acad Dermatol. 2013;68(3):493–8. **PMID:23182059** · Oei W, et al. Br J Dermatol. 2021. **PMID:33237568** · *Diagnostics.* 2024;14(21):2345. **PMID:39518313** · Ji Y, et al. Clin Case Rep. 2025. **PMID:41141235**

**Treatment and models** — Küsters-Vandevelde HVN, et al. Acta Neuropathol Commun. 2014;2:41. **PMID:24713450** · Choi YS, et al. Cell. 2022;185(12):2071–2085.e12. **PMID:35561684** · Grafanaki K, et al. Trends Cancer. 2022;8(8):626–8. **PMID:35718707** · Basu D, et al. Neuro Oncol. 2016. **PMID:26354928**; Cancer Genomics Proteomics. 2018;15(4):239–48. **PMID:29976629** · Tomás-Velázquez A, et al. JEADV. 2024. **PMID:38071601** · Pedersen M, et al. Cancer Discov. 2013;3(4):458–69. **PMID:23303902** · Ackermann J, et al. Cancer Res. 2005;65(10):4005–11. **PMID:15899789** · Baumgartner A, et al. J Pers Med. 2021;11(4):292. **PMID:33921303** · Sharouf F, et al. Childs Nerv Syst. 2018. **PMID:29948137** · Vanood A, et al. BMJ Case Rep. 2020. **PMID:33257354** · Raljević L, et al. Mol Cell Pediatr. 2026. **PMID:41973363** · Doolan BJ, et al. JAMA Dermatol. 2026. **PMID:42384401** · Chen Y, et al. Vet Pathol. 2009. **PMID:19276048** · ClinicalTrials.gov: **NCT07891286**, **NCT04999631**, **NCT06828822**, **NCT02280889**, **NCT06934759**, **NCT02775643**

Sources:
- [Kinsler 2013 — NRAS codon 61 in multiple CMN and NCM (PMID:23392294)](https://pubmed.ncbi.nlm.nih.gov/23392294/)
- [Ruggieri 2020 — Neurocutaneous melanocytosis (melanosis) (PMID:33048248)](https://pubmed.ncbi.nlm.nih.gov/33048248/)
- [Waelchli 2015 — MRI as best predictor of outcome (PMID:25966033)](https://onlinelibrary.wiley.com/doi/10.1111/bjd.13898)
- [Kinsler 2017 — Melanoma in congenital melanocytic naevi (PMC5484991)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5484991/)
- [Kinsler 2017 — Copy number abnormalities confirm primary CNS melanoma (PMC5250663)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5250663/)
- [Küsters-Vandevelde 2014 — MEK162 in NRAS-mutated NCM (PMC4023633)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4023633/)
- [Choi 2022 — Topical therapy for congenital giant nevi, Cell](https://www.cell.com/cell/fulltext/S0092-8674(22)00472-X)
- [Pedersen 2013 — Primary CNS melanoma driven by congenital NRAS (PMID:23303902)](https://pubmed.ncbi.nlm.nih.gov/23303902/)
- [Ackermann 2005 — Tyr::N-RasQ61K INK4a−/− mouse melanoma (PMID:15899789)](https://pubmed.ncbi.nlm.nih.gov/15899789/)
- [Diagnostics 2024 — CNS involvement and neuroradiological imaging in NCM (PMC11545461)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11545461/)
- [Ji 2025 — NCM in children and adults, case report and review (PMC12552845)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12552845/)
- [Takiya 2023 — Incidence of NCM in Japanese paediatric CMN patients (PMC10542349)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10542349/)
- [Rahman 2022 — Neurosurgical management of NCM: systematic review](https://thejns.org/focus/view/journals/neurosurg-focus/52/5/article-pE8.xml)
- [Takahashi 2024 — NRAS missense mutation and malignant progression in NCM](https://link.springer.com/article/10.1186/s40478-024-01723-0)
- [MONDO:0009578 — neurocutaneous melanocytosis (Monarch)](https://monarchinitiative.org/MONDO:0009578)
- [OMIM 249400 — MELANOSIS, NEUROCUTANEOUS; NCMS](https://omim.org/entry/249400)
- [Orphanet — Neurocutaneous melanocytosis (ORPHA:2481)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=2481)
- [ClinVar — NRAS c.181C>A (p.Gln61Lys) and Neurocutaneous melanocytosis](https://www.ncbi.nlm.nih.gov/clinvar/RCV000144964/)
- [ClinicalTrials.gov — NCT07891286, mirdametinib for large/giant CMN](https://clinicaltrials.gov/study/NCT07891286)
- [OMIA:000633-9823 — Melanoma, Sinclair swine cutaneous malignant](https://omia.org/OMIA000633/9823/)
- [OMIA:000634-9823 — Melanoma, congenital in Sus scrofa](https://omia.org/OMIA000634/9823/)
- [2021 WHO Classification of Tumors of the CNS: a summary (PMC8328013)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8328013/)
- [Congenital Melanocytic Nevi — StatPearls](https://www.ncbi.nlm.nih.gov/sites/books/NBK563168/)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 72 |
| Resolved | 72 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 67 |
| Quoted claims found in source | 49 |
| Quoted claims **not** found in source | 18 |
| References weighed for topical relevance | 72 |
| On topic | 42 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:39518313` *(abstract only)*: "The presence of more than 20 accompanying nevi indicates an elevated risk of central nervous system (CNS) involvement"
  - closest text in source: "Their association with the central nervous system (CNS) poses significant risks, including melanoma and neurocutaneous melanocytosis (NCM), where melanocytes infiltrate the CNS, potentially causing seizures, hydrocephalus, and, rarely, CNS melanoma"
- `PMID:39518313` *(abstract only)*: "increased incidence of arachnoid cysts"
  - Text part not found as substring: 'increased incidence of arachnoid cysts' (note: only abstract available for PMID:39518313, full text may contain this excerpt)
- `PMID:23182059` *(abstract only)*: "Behavioral and emotional difficulties appeared common in affected children independent of lesion characteristics"
  - closest text in source: "Behavioral/emotional problems independent of the lesion were common in children"
- `PMID:23392294` *(abstract only)*: "none of the blood samples or clinically unaffected tissue samples carried this mutation"
  - closest text in source: "Oncogenic missense mutations in codon 61 of NRAS were found in affected neurological and cutaneous tissues of 12 out of 15 patients, but were absent from unaffected tissues and blood, consistent with NRAS mutation mosaicism"
- `PMID:41474606` *(abstract only)*: "without definite pathogenic mutations"
  - Text part not found as substring: 'without definite pathogenic mutations' (note: only abstract available for PMID:41474606, full text may contain this excerpt)
- `PMID:38254245` *(abstract only)*: "NRAS mutation was found only in the abdominal tumour and was thought to be responsible for malignant progression in the present case"
  - closest text in source: "NRAS mutation was found only in the abdominal tumor and was thought to be responsible for malignant progression in the present case"
- `PMID:29976629` *(abstract only)*: "Clonogenicity appeared to depend on bFGF and IGF1 signaling through ERK and Akt"
  - closest text in source: "RESULTS: Clonogenicity appeared to depend on bFGF and IGF1signaling through ERK and Akt"
- `PMID:39518313` *(abstract only)*: "Focal melanosis correlates with seizures"
  - closest text in source: "Their association with the central nervous system (CNS) poses significant risks, including melanoma and neurocutaneous melanocytosis (NCM), where melanocytes infiltrate the CNS, potentially causing seizures, hydrocephalus, and, rarely, CNS melanoma"
- `PMID:39518313` *(abstract only)*: "Diffuse leptomeningeal melanosis associates with hydrocephalus and CNS melanoma"
  - closest text in source: "Their association with the central nervous system (CNS) poses significant risks, including melanoma and neurocutaneous melanocytosis (NCM), where melanocytes infiltrate the CNS, potentially causing seizures, hydrocephalus, and, rarely, CNS melanoma"
- `PMID:38254245` *(abstract only)*: "NRAS mutation was found only in the abdominal tumour and was thought to be responsible for malignant progression"
  - closest text in source: "NRAS mutation was found only in the abdominal tumor and was thought to be responsible for malignant progression in the present case"
- `PMID:41141235` *(abstract only)*: "Brain MRI is considered the imaging modality of choice for identifying leptomeningeal and parenchymal melanocytic infiltration, which often appears as abnormal contrast enhancement on T1-weighted sequences"
  - closest text in source: "Neurocutaneous melanosis (NCM) is a rare, non-inherited disease characterized by the presence of giant congenital melanocytic nevi (CMN) or multiple CMN, and it is often associated with meningeal melanosis or meningeal melanoma"
- `PMID:39518313` *(abstract only)*: "The Nevosurgery Network, therefore, recommends MRI examinations in cases of GCMN (>40 cm projected adult size (PAS)), and/or the presence of >20 concomitant nevi, and/or neurological symptoms"
  - closest text in source: "The Nevosurgery Network recommends MRI examinations in cases of GCMN (>40 cm PAS), the presence of over 20 concomitant nevi, and neurological symptoms requiring clarification"
- `PMID:39518313` *(abstract only)*: "the rate of melanoma is higher with positive MRI (detection of melanin in the CNS) than in patients with negative MRI (12% vs. 2%)"
  - closest text in source: "MRI is recommended for GCMN patients, particularly those with numerous satellite nevi or neurological symptoms, to detect CNS involvement"
- `PMID:1869648` *(abstract only)*: "Recommended diagnostics include cerebrospinal fluid analysis and MRI with contrast enhancement"
  - closest text in source: "Useful diagnostic procedures include cerebrospinal fluid cytology and magnetic resonance imaging with gadolinium contrast"
- `PMID:28078671` *(abstract only)*: "This demonstrated measurable and objective relief of symptoms and signs in all patients, although to varying degrees"
  - closest text in source: "Management strategies are proposed for presentation of suspected melanoma of the skin and the central nervous system in patients with CMN, including use of oral mitogen-activated protein kinase kinase inhibitors in NRAS-mutated tumours."
- `PMID:41141235` *(abstract only)*: "trametinib showed 'mild clinical improvement' with symptom-free periods of 'one to nine months'"
  - closest text in source: "The research analysis highlights that individualized monitoring and related intervention strategies may improve the clinical prognosis of patients with this uncommon and potentially fatal disease through the process of early identification of high-risk features associated with malignant transformation."
- `PMID:35718707` *(abstract only)*: "topical application of a proinflammatory hapten for alopecia treatment [squaric acid dibutylester (SADBE)] caused nevus regression and prevented melanoma in an Nras mouse CGN model"
  - closest text in source: "topical application of a proinflammatory hapten for alopecia treatment [squaric acid dibutylester (SADBE)] caused nevus regression and prevented melanoma in an Nras mouse CGN model"
- `PMID:35561684` *(abstract only)*: "The authors presented preclinical models, including **multiple genetically engineered mice and xenografted human lesions**, which enabled testing locally applied pharmacologic agents to avoid surgery"
  - closest text in source: "We have presented preclinical models, including multiple genetically engineered mice and xenografted human lesions, which enabled testing locally applied pharmacologic agents to avoid surgery"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC8328013` (2 mentions) - The 2021 WHO Classification of Tumors of the Central Nervous System: a summary.
  - shared terms: cns

Weighed against this report's own most characteristic terms: `ncm`, `melanoma`, `cmn`, `nras`, `cns`, `disease`, `lesion`, `patient`, `mutation`, `congenital`, `cutaneous`, `cell`, `melanosis`, `melanocytic`, `model`, `leptomeningeal`, `mri`, `mosaic`, `giant`, `naevus`.
