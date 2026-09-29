---
provider: claude_code
model: claude-fable-5-1, claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-09-27T04:02:27.686394'
end_time: '2026-09-27T04:20:06.807351'
duration_seconds: 1059.12
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Invasive Non-Typhoidal Salmonellosis
  mondo_id: MONDO:0017944
  category: Infectious Disease
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
  - claude-fable-5-1
  - claude-haiku-4-5-20251001
  - claude-opus-5
  web_search_requests: 16
  num_turns: 57
  total_cost_usd: 8.905380249999999
  session_id: 9e7ba3dd-2008-409b-8741-22851ab900c2
  stop_reason: end_turn
  assistant_text_blocks: 5
citation_count: 22
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Invasive Non-Typhoidal Salmonellosis
- **MONDO ID:** MONDO:0017944 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Invasive Non-Typhoidal Salmonellosis** covering all of the
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

I'll research invasive non-typhoidal salmonellosis (iNTS) across the requested sections using web search and PubMed lookups, then write the report inline.

Continuing the literature search in smaller batches.

Gathering the remaining sections in parallel.

Verifying the ontology identifiers I plan to cite rather than writing them from memory.

# Invasive Non-Typhoidal Salmonellosis (iNTS Disease) — Comprehensive Research Report

**Target:** Invasive Non-Typhoidal Salmonellosis · **MONDO:0017944** · Category: Infectious Disease
**Report date:** 2026-09-27 · **Intended use:** dismech knowledge-base entry population

> **Provenance note, read this first.** Quotations marked **[verbatim abstract]** were retrieved as abstract text from PubMed Central, Europe PMC, or the publisher. Statements marked **[tool-summarized]** were paraphrased by a retrieval tool from the full text and are *leads, not snippets*. Before any of this becomes a dismech `evidence.snippet`, fetch the reference (`just fetch-reference PMID:…`) and confirm the exact substring; `just count-verified-snippets` and `just validate-kb-references` are the gates. All ontology CURIEs below were resolved live against EBI OLS4, HGNC REST, or NCBI Taxonomy during this session — none were written from memory — but dynamic-enum membership (e.g. whether an NCIT term is reachable from `NCIT:C25218`) was **not** checked and must be confirmed with `just validate-terms`.

---

## 1. Disease Information

### Overview

Invasive non-typhoidal salmonellosis (iNTS disease) is extraintestinal infection — principally bloodstream infection, with meningitis and focal metastatic infection as important variants — caused by non-typhoidal serovars of *Salmonella enterica*. It is epidemiologically and clinically distinct from the self-limiting enterocolitis that the same serovars cause in high-income settings. In sub-Saharan Africa it presents as a non-specific febrile systemic illness resembling enteric fever, is caused predominantly by a small number of genetically distinct, human-adapted pathovars, carries a case-fatality ratio of roughly 15–20%, and occurs against a background of specific host comorbidities (HIV, malaria, malnutrition, anaemia, sickle cell disease).

**[verbatim abstract, PMID:30657108]** "Nontyphoidal salmonellae (NTS) are a major cause of invasive (iNTS) disease in sub-Saharan Africa, manifesting as bacteremia and meningitis. Available epidemiological data indicate that iNTS disease is endemic in much of the region. Antimicrobial resistance is common and case fatality rates are high. There are well-characterized clinical associations with iNTS disease, including young age, HIV infection, malaria, malnutrition, anemia, and sickle cell disease. However, the clinical presentation of iNTS disease is often with fever alone, so clinical diagnosis is impossible without blood culture confirmation."

The MONDO definition (retrieved live from OLS4) reads: "Invasive non-typhoidal salmonellosis (iNTS) is a rare bacterial infectious disease caused by extraintestinal infection of non-typhoidal serotypes of *Salmonella enterica* in patients with underlying HIV infection, malaria or malignancy. It has a high mortality rate and patients typically present with fever, pallor and respiratory signs (cough, tachnypnea, pneumonia). Gastrointestinal manifestations (diarrhea, vomit, abdominal pain) are not common. Occasionally, organ absseses, septic shock and meningitis may be observed." (Note: the MONDO text contains the typographical errors "tachnypnea" and "absseses"; if quoted as a dismech snippet, copy it verbatim including the errors, per the repository's snippet rule.)

### Identifiers (verified)

| Resource | Identifier |
|---|---|
| MONDO | `MONDO:0017944` (label: *invasive non-typhoidal salmonellosis*; parent `MONDO:0000827` *salmonellosis*) |
| Orphanet | `Orphanet:324648` (MONDO xref) |
| GARD | `GARD:0021449` (MONDO xref) |
| UMLS | `UMLS:C4706572` (MONDO xref) |
| MedGen | `MEDGEN:1638286` (MONDO xref) |
| SNOMED CT | `SCTID:763772002` (MONDO xref) |
| ICD-10 | A02.1 *Salmonella sepsis*; A02.2 *localized salmonella infections*; A02.0 *Salmonella enteritis*; A02.9 *Salmonella infection, unspecified* (not present as MONDO xrefs; assign by curator judgement) |
| MeSH | *Salmonella Infections* (D012480) — no iNTS-specific MeSH descriptor exists |
| OMIM | **Not applicable** — iNTS is an acquired infection, not a Mendelian disorder. OMIM entries are relevant only to host susceptibility (see §4). |
| NCBITaxon (pathogens) | `NCBITaxon:28901` *Salmonella enterica*; `NCBITaxon:90371` serovar Typhimurium; `NCBITaxon:149539` serovar Enteritidis; `NCBITaxon:98360` serovar Dublin |

### Synonyms

iNTS disease; invasive non-typhoidal *Salmonella* disease (both are MONDO exact synonyms); non-typhoidal *Salmonella* bacteraemia/bacteremia; NTS bloodstream infection; invasive salmonellosis (non-typhoidal). Note that "non-typhoidal salmonellosis" without "invasive" usually denotes the gastroenteritis phenotype and should not be treated as a synonym.

### Data provenance character

Knowledge of this disease is overwhelmingly **aggregate and hospital-based rather than patient-level EHR-derived**. The Marchello meta-analysis found that **[verbatim abstract, PMID:35114140]** "Of these included studies, 77 (91·7%) were hospital-based and 66 (78·6%) were located in Africa or Asia… Of all 84 studies, 66 (78·6%) had an overall high risk of bias, 18 (21·4%) had a moderate risk, and none had a low risk." The most granular individual-level data come from single-site sentinel blood-culture surveillance (notably Malawi-Liverpool-Wellcome, Blantyre) and from genomic cohorts (§4, §6). No population-based registry exists.

---

## 2. Etiology

### Causal factors

The **necessary cause is infection** by a non-typhoidal serovar of *Salmonella enterica* subsp. *enterica*. Serovar distribution is strikingly narrow for invasive disease:

- Marchello et al. **[tool-summarized, PMID:35114140, Table]**: among 12,977 invasive isolates, Typhimurium 45.7%, Enteritidis 31.8%, Dublin 3.1%.
- Blantyre, Malawi, 2011–2019 **[tool-summarized, PMID:37153453]**: *S.* Typhimurium 84.8%, *S.* Enteritidis 10.3%, other 4.9% of invasive isolates.
- The Nature Medicine global genomic census identifies **[verbatim abstract, PMID:40205197]** "*Salmonella* Enteritidis identified as a major cause" outside Africa.

Within Typhimurium, the African invasive phenotype is carried by a specific sequence type: **[verbatim abstract, PMID:37872141]** "At least six invasive *S.* Typhimurium clades have already emerged, with ST313 lineage 2 or ST313-L2 driving the current pandemic. ST313-L2 likely emerged in the Democratic Republic of Congo around 1980 and further spread in the mid 1990s."

**Sufficiency requires a permissive host.** The defining etiologic feature of iNTS disease is that invasion is comorbidity-gated: the same organisms cause enterocolitis in immunologically intact hosts.

### Risk factors — host/comorbid (environmental in the dismech sense)

| Risk factor | Evidence |
|---|---|
| **Advanced HIV infection** (adults) | **[tool-summarized, PMID:22587967]** "The main risk factor in adults is undoubtedly advanced HIV infection. Case series typically show 95% of adult cases to be in people infected with HIV." **[tool-summarized, PMID:30657108]** "iNTS disease in African adults is overwhelmingly HIV-associated, with rates of HIV coinfection in excess of 95%." Salmonella bacteraemia is an AIDS-defining infection **[tool-summarized, PMID:35041743]**. |
| **Malaria** (children) | Concurrent parasitaemia, recent malaria, and especially **severe malarial anaemia** are associated with iNTS disease **[tool-summarized, PMID:30657108, PMID:22587967]**. |
| **Malnutrition / acute severe malnutrition** | Recognized clinical association **[verbatim abstract, PMID:30657108]**. |
| **Anaemia** | Both as a marker and a risk factor; 47.3% of patients had anaemia as a complication **[verbatim abstract, PMID:35114140]**. |
| **Sickle cell disease** | **[tool-summarized, PMID:30657108]** "NTS is a common cause of invasive infection… in the context of sickle cell disease." Hallmark association with *Salmonella* osteomyelitis (`HP:0005661`). Relevant gene: *HBB* (`hgnc:4827`). |
| **Young age** | Incidence peaks in infancy/second year of life. **[verbatim abstract, PMID:40684736]** "iNTS disease is observed from birth, with a peak incidence early in the second year of life, declining before the age of 3 years." |
| **Older age (high-income settings)** | In a Taiwanese cohort of 272 adults with NTS bacteraemia, 162 (59.6%) were ≥55 years, with more extra-intestinal focal infections and higher 30-day mortality **[tool-summarized, PMID:22261309]**. |
| **Malignancy, corticosteroids, transplantation, haematologic malignancy** | Recognized risk groups in high-income settings **[tool-summarized, PMID:35041743]**. |
| **Sex** | **[verbatim abstract, PMID:40205197]** "Age and sex emerged as significant risk factors." Direction/magnitude should be read from that paper's tables, not assumed. |

### Risk factors — genetic (host susceptibility)

See §4 for detail. In brief: Mendelian defects of the IL-12/IFN-γ (type II interferon) axis, and a common-variant risk locus at *STAT4*.

### Protective factors

- **Antiretroviral therapy** reduced recurrence and incidence in HIV-infected adults. Pre-ART, **[tool-summarized, PMID:22587967]** "Before the antiretroviral therapy era 20–40% of survivors had recurrence, even after appropriate antimicrobial drugs."
- **Malaria control.** A temporal association between falling malaria incidence and falling iNTS incidence has been reported from The Gambia, Kenya and Malawi **[tool-summarized, PMID:30657108]**. Modelling of Blantyre data attributes the paediatric decline jointly to malaria, HIV and malnutrition control **[PMID:26230258]**.
- **Antibody-mediated immunity.** **[verbatim abstract, PMID:30657108]** "immunoepidemiological studies from Africa indicate an important role for antibody for protective immunity, supporting the development of antibody-inducing vaccines against iNTS disease." This is the mechanistic rationale for the entire vaccine pipeline (§12, §13).
- **Genetic protective factors:** no validated protective allele is established. The *STAT4* finding is a *risk* allele; the alternative allele is protective by construction, not by independent demonstration. `gnomAD` allele frequencies for rs13390936 should be read directly rather than inferred.

### Gene–environment interaction

The central interaction is **host IFN-γ capacity × pathogen exposure**. The *STAT4* risk genotype is associated with reduced IFN-γ output, and the risk it confers is realized only in an exposed, comorbidity-burdened population **[PMID:29523850]**. A second, well-documented interaction is **HIV × humoral immunity**: HIV infection does not simply reduce antibody, it dysregulates it. MacLennan et al. showed that HIV-infected African adults have high-titre anti-LPS antibody that *inhibits* bactericidal killing **[tool-summarized, PMID:20413503]**. A third is **malaria × phagocyte function**, where haemolysis-derived haem and haem oxygenase-1 induction are proposed to impair neutrophil oxidative burst; treat this as mechanistically plausible and incompletely demonstrated in humans.

Risk factors are explicitly **not independent**: **[tool-summarized, PMID:30657108]** "HIV-infected South African children with NTS bacteremia are more likely to be malnourished than their HIV-uninfected counterparts."

---

## 3. Phenotypes

### The defining phenotypic fact

There is no pathognomonic presentation. **[tool-summarized, PMID:30657108]** "The lack of a pathognomonic clinical presentation makes clinical diagnosis of iNTS disease impossible." **[tool-summarized, PMID:22587967]** "The clinical presentation of invasive non-typhoidal salmonella disease in Africa is typically febrile systemic illness resembling enteric fever; diarrhoea is often absent." For a dismech entry this means most phenotype nodes carry **moderate-to-low specificity** and several will legitimately bind coarse HPO terms — see the repository's `coarse-phenotype-bindings` guidance.

### Presenting features with frequencies (African paediatric/adult series)

Frequencies below are **[tool-summarized, PMID:30657108]** study medians with ranges as reported in that review's tables.

| Phenotype | Frequency | Suggested HP term |
|---|---|---|
| Fever | median 97% (range 74–100%) | `HP:0001945` Fever |
| Tachypnea | median 72% (66–77%) | `HP:0002789` Tachypnea |
| Diarrhoea (children) | median 35% | `HP:0002014` Diarrhea |
| Splenomegaly | median 31% (19–45%) | `HP:0001744` Splenomegaly |
| Hepatosplenomegaly | common in series | `HP:0001433` Hepatosplenomegaly |
| Cough | common | `HP:0012735` Cough |
| Pallor | common (tracks anaemia) | `HP:0000980` Pallor |
| Respiratory distress | common | `HP:0002098` Respiratory distress |

### Complications and their pooled prevalence

From the global meta-analysis **[verbatim abstract, PMID:35114140]**: "Among 55 studies reporting non-typhoidal salmonella disease-associated complications, a total of 45 different complications were reported and 1824 complication events were identified among 6974 study participants. The most prevalent complication was septicaemia, occurring in 171 (57·2%) of 299 participants, followed by anaemia in 580 (47·3%) of 1225 participants."

Additional complication frequencies **[tool-summarized, PMID:35114140, Table 1]** — treat every row as a lead requiring re-extraction from the paper, and note the authors' own finding that 78.6% of studies were at high risk of bias and that denominators differ per complication:

| Complication | Reported proportion | Suggested HP term |
|---|---|---|
| Septicaemia | 171/299 (57.2%) | `HP:0100806` Sepsis |
| Anaemia | 580/1225 (47.3%) | `HP:0001903` Anemia |
| Shock | 107/560 (19.1%) | `HP:0002615` Hypotension |
| Encephalopathy | 8/40 (20.0%) | `HP:0001298` Encephalopathy |
| Pneumonia | 232/1619 (14.3%) | `HP:0002090` Pneumonia |
| Septic shock | 36/331 (10.9%) | `HP:0002615` Hypotension |
| Seizures | 25/256 (9.8%) | `HP:0001250` Seizure |
| Extraintestinal focal infection | 66/721 (9.2%) | — (use specific focus) |
| Mycotic aneurysm | 124/1991 (6.2%) | no HP term; anchor to `UBERON:0000947` aorta in pathophysiology |
| Recurrence | 110/2299 (4.8%) | `HP:0002718` Recurrent bacterial infections |
| Abscess | 47/1609 (2.9%) | `HP:0025059` Splenic abscess (if splenic) |
| Septic arthritis | 16/566 (2.8%) | `HP:0003095` Septic arthritis |
| Osteomyelitis | 38/1498 (2.5%) | `HP:0002754` Osteomyelitis / `HP:0005661` Salmonella osteomyelitis |
| Endocarditis | 6/366 (1.6%) | `HP:0100584` Endocarditis |

The mycotic-aneurysm proportion is high relative to African series because the pooled denominator is dominated by East Asian adult cohorts; do not carry 6.2% into an African-context entry without stratification. This is a real example of aggregation across two different diseases-in-practice.

### Meningitis as a distinct syndrome

Salmonella meningitis is uncommon but disproportionately lethal. **[tool-summarized, PMID:35041743]** case fatality "up to 50–70%" in recent reviews, with "mortality was ~20%" in African infants specifically. In Blantyre 2011–2019, 26 confirmed CSF-culture cases occurred, 88.5% *S.* Typhimurium, mostly in children **[tool-summarized, PMID:37153453]**. Suggested terms: `HP:0001287` Meningitis; anatomy `UBERON:0002360` meninx, `UBERON:0001359` cerebrospinal fluid.

### Laboratory abnormalities

| Abnormality | HP term |
|---|---|
| Anaemia | `HP:0001903` |
| Thrombocytopenia | `HP:0001873` |
| Increased total leukocyte count | `HP:0001974` |
| Decreased total neutrophil count | `HP:0001875` |
| Elevated CRP | `HP:0011227` |
| Increased circulating lactate | `HP:0002151` |
| Hypoglycaemia | `HP:0001943` |
| Jaundice | `HP:0000952` |
| Disseminated intravascular coagulation | `HP:0005521` |
| Haemophagocytosis | `HP:0012156` |

Haemophagocytic lymphohistiocytosis due to fulminant *Salmonella* sepsis has been reported specifically in IL-12Rβ1 deficiency, linking a laboratory phenotype to a host-genetic mechanism (see §4).

### Onset, severity, progression, and quality of life

- **Onset:** acute, over days. Not congenital, not late-onset in the Mendelian sense. Age of *occurrence* peaks in infancy/second year of life in Africa **[PMID:40684736]** and in adults ≥55 years in high-income settings **[PMID:22261309]**.
- **Severity:** severe by definition of the entry (bloodstream/sterile-site infection), with pooled CFR ~15%.
- **Progression:** acute and either resolving or fatal within days to weeks; **recurrent/relapsing** in HIV without ART (20–40% pre-ART recurrence **[PMID:22587967]**).
- **Quality of life:** no iNTS-specific EQ-5D, SF-36, or PROMIS data were located. The GBD framework assigns disability weights via generic severe-infectious-episode and sequelae states; the 2021 analysis reports 4,740,235 DALYs (95% UI 2,762,282–7,597,208) **[tool-summarized, DOI:10.1371/journal.pntd.0012960]**. **State plainly in the KB entry that per-phenotype QoL data are absent** rather than substituting a generic sepsis instrument.

---

## 4. Genetic / Molecular Information

### Causal genes: not applicable

iNTS disease has **no causal human gene**. Do not populate `genetic:` with a causal `relationship_type` for this entry. The genetics that matter are (a) **host susceptibility** and (b) **pathogen genomics**, which in dismech belong in `genetic:` with `relationship_type: SUSCEPTIBILITY` and in `pathophysiology:` respectively.

### Host susceptibility — Mendelian

Defects of the IL-12/IL-23/IFN-γ axis (Mendelian susceptibility to mycobacterial disease, MSMD, and related inborn errors) predispose to non-typhoidal *Salmonella* invasive and recurrent disease. **[tool-summarized, PMID:35041743]** "conditions that compromise Th1 immune responses increase the risk," specifically "Mendelian mutations in the interleukin 12 (IL-12)/interferon γ (IFNγ) axis." The canonical review is Gilchrist, MacLennan & Hill, *Nat Rev Immunol* 2015 (PMID:26109132, DOI:10.1038/nri3858).

Genes to curate as susceptibility loci (HGNC verified live):

| Gene | HGNC | Axis role |
|---|---|---|
| *IL12B* | `hgnc:5970` | IL-12p40 subunit |
| *IL12RB1* | `hgnc:5971` | IL-12/IL-23 receptor β1 |
| *IFNGR1* | `hgnc:5439` | IFN-γ receptor 1 |
| *IFNGR2* | `hgnc:5440` | IFN-γ receptor 2 |
| *STAT1* | `hgnc:11362` | Downstream transcription factor |
| *IKBKG* (NEMO) | `hgnc:5961` | NF-κB signalling |
| *CYBB* | `hgnc:2578` | Phagocyte NADPH oxidase (CGD) |
| *NCF1* | `hgnc:7660` | Phagocyte NADPH oxidase (CGD) |
| *HBB* | `hgnc:4827` | Sickle cell disease (non-immune susceptibility) |

For variant-level classification, ACMG/AMP calls, and allele frequencies, read ClinVar and gnomAD directly at curation time — this report does not assert variant-level pathogenicity, and none should be written into the entry from here.

### Host susceptibility — common variant

**[verbatim abstract, PMID:29523850]** "Nontyphoidal Salmonella (NTS) is a major cause of bacteraemia in Africa. The disease typically affects HIV-infected individuals and young children, causing substantial morbidity and mortality. Here we present a genome-wide association study (180 cases, 2677 controls) and replication analysis of NTS bacteraemia in Kenyan and Malawian children. We identify a locus in STAT4, rs13390936, associated with NTS bacteraemia."

| Field | Value |
|---|---|
| Gene | *STAT4* (`hgnc:11365`) |
| Variant | rs13390936, intronic |
| Model / effect | recessive, OR 7.61 (95% CI 3.98–14.55) **[tool-summarized]** |
| Combined *p* | 8.62 × 10⁻¹⁰ **[tool-summarized]** |
| Cohorts | Kenyan discovery + Kenyan replication + Malawian replication |
| Functional support | context-specific eQTL for *STAT4* in stimulated immune cells; risk genotype associated with reduced IFN-γ production in stimulated NK cells and lower circulating IFN-γ during acute bacteraemia **[tool-summarized]** |

Note the two published effect sizes differ by source (OR 7.2 in one summary, OR 7.61 recessive in another); resolve against the paper before recording a number.

### Pathogen genomics — the substantive "molecular information" for this entry

**ST313 lineage structure and dating** **[verbatim abstract, PMID:37872141]**: "By analysing whole genome sequence data from 1303 *S.* Typhimurium isolates originating from 19 African countries and isolated between 1979 and 2017… At least six invasive *S.* Typhimurium clades have already emerged, with ST313 lineage 2 or ST313-L2 driving the current pandemic. ST313-L2 likely emerged in the Democratic Republic of Congo around 1980 and further spread in the mid 1990s. We observed plasmid-borne as well as chromosomally encoded fluoroquinolone resistance underlying emergences of extensive-drug and pan-drug resistance."

Supporting detail **[tool-summarized, PMID:37872141]**: MRCA of ST313-L2 dated 1980 (95% HPD 1974–1986); five independent introductions from DRC into East Africa 1995–2000; one major West African introduction (Ghana, 1994).

**Sublineage displacement in Malawi** **[verbatim abstract, PMID:38623411]**: "We performed an intensive comparative genomic analysis of 608 *S*. Typhimurium ST313 isolates dating between 1996 and 2018 from Blantyre, Malawi. We discovered that following the arrival of the well-characterized *S*. Typhimurium ST313 lineage 2 in 1999, two multidrug-resistant variants emerged in Malawi in 2006 and 2008, designated sublineages 2.2 and 2.3, respectively. The majority of *S*. Typhimurium isolates from human bloodstream infections in Malawi now belong to sublineages 2.2 or 2.3." Sublineage 2.2 shows constitutive SPI-2 expression under non-inducing conditions, reduced flagellar gene expression, a pCol1B9 plasmid with loss of pBT1, and a competitive fitness advantage **[tool-summarized]**.

**Genome degradation** is the hallmark molecular signature: **[verbatim abstract, PMID:25569606]** "*S.* Typhimurium ST313 strains have acquired pseudogenes and genetic deletions and appear to be evolving to become more like the typhoidal serovars *S*. Typhi and *S*. Paratyphi A."

**Antimicrobial resistance determinants** **[tool-summarized, PMID:37872141]**:
- MDR: *cat* (chloramphenicol), *bla*TEM (ampicillin), *dfrA* + *sul* (co-trimoxazole)
- ESBL: *bla*CTX-M-15, *bla*SHV-12, *bla*OXA-1
- Azithromycin: *mphA*
- Fluoroquinolone: chromosomal *gyrA* S83F/S83Y/D87G/D87N/D87Y, *gyrB* E466Y; plasmid-borne *qnrB*, *qnrS*, *aac(6′)-Ib-cr*
- XDR and pan-drug resistance arose independently multiple times, associated with IncHI2 and IncI1 plasmids

### Epigenetics and chromosomal abnormalities

**Not applicable to the host.** No DNA-methylation or histone-modification signature is established for iNTS susceptibility or pathogenesis, and no chromosomal abnormality causes this disease. If an epigenetic mechanism is curated at all, it belongs to the bacterium (Dam/Dcm methylation of *Salmonella* regulons) and should be marked as such, not as a host epigenetic change. Leave these fields empty with a `notes:` line recording that the literature was searched.

---

## 5. Environmental Information

### Infectious agents

| Agent | NCBITaxon | Role |
|---|---|---|
*Salmonella enterica* | `NCBITaxon:28901` | species |
*S. enterica* serovar Typhimurium (esp. ST313 L2) | `NCBITaxon:90371` | dominant African cause |
*S. enterica* serovar Enteritidis | `NCBITaxon:149539` | second most common; dominant in several non-African settings |
*S. enterica* serovar Dublin | `NCBITaxon:98360` | bovine-adapted, disproportionately invasive |

Co-infecting agents that act as risk modifiers: *Plasmodium falciparum* (malaria), HIV-1.

### Transmission and reservoir — a genuinely open question

This is the most important unresolved epidemiological issue and should be curated as a knowledge gap rather than settled. The classical NTS model is zoonotic foodborne transmission; the African iNTS pathovars appear not to follow it.

**[tool-summarized, PMID:36910696]** The sources of iNTS infections "remain unclear, with two main hypotheses: transmission from a zoonotic reservoir or person-to-person transmission." Two studies found isolates in stool of household members very closely related to the index iNTS isolate, "consistent with the hypothesis of person-to-person transmission, though infection from a common source cannot be excluded," and thorough investigation of the domestic environment and food pathway yielded "only a single iNTS-associated *Salmonella* Enteritidis isolate."

**[verbatim abstract, PMID:40205197]** "Importantly, our genomic and transmission analyses suggest that iNTS infections may involve human-to-human transmission, with diarrheal patients acting as potential intermediaries, deviating from typical zoonotic pathways."

Supporting host-restriction evidence **[tool-summarized, PMID:30657108]**: African invasive isolates "may be restricted, or be in the process of becoming restricted, to humans," with studies showing "isolated *Salmonella* strains in humans and animals were distinct," suggesting anthroponotic transmission.

Suggested dismech treatment: an `environmental[]` entry for the exposure route with `environmental_effect: TRIGGERS` linked to the colonization node, plus a `discussions[]` entry with `kind: KNOWLEDGE_GAP` on reservoir identity. ECTO binding for "exposure to *Salmonella*" should be searched at curation time; if nothing fits, record the queries run verbatim in `notes:` per the repository's negative-existence rule — do not write "no ECTO term exists" without the recorded searches.

### Non-infectious environmental and lifestyle factors

- **Rainfall/seasonality:** iNTS incidence in Malawi is seasonal, and rainfall was included as a covariate in the decline model (PMID:26230258).
- **Water, sanitation and hygiene:** plausibly central given the person-to-person hypothesis, but no trial has demonstrated WASH impact on iNTS specifically. Curate as inferred, not demonstrated.
- **Food exposures** (eggs, meat, dairy, produce) and **overseas travel** are established for NTS gastroenteritis in high-income settings and are the likely route for many high-income invasive cases; they are *not* established as the route for African iNTS.
- No toxicological or occupational exposure is implicated. CTD/TOXNET yield nothing specific to this entry.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

The chain below is written for a dismech pathograph. Steps are numbered; branch points are explicit; where a step is **inferred** rather than demonstrated in humans, it is labelled.

1. **Ingestion of, or mucosal exposure to, an invasive NTS pathovar** (ST313 L2 Typhimurium or invasive Enteritidis) **leads to** arrival of viable bacteria in the small intestine. Enhanced acid resistance of ST313 relative to ST19 promotes survival of gastric transit — D23580 "exhibited enhanced resistance to acid stress relative to SL1344, which may lend towards increased capability to survive passage through the gastrointestinal tract" **[verbatim abstract, PMID:26091096]**. *Route in African settings is inferred (see §5).*
2. **Intestinal epithelial and M-cell translocation** (`CL:0002563`, `CL:0000682`; `UBERON:0002108`, `UBERON:0001211`) **results in** submucosal bacterial arrival. In ST313 this step is **attenuated, not enhanced**: ST313 shows "reduced SPI-1–mediated epithelial invasion" **[tool-summarized, PMID:30657108]**. This is the first mechanistic branch away from the gastroenteritis phenotype — less epithelial invasion means less enterocolitis, which is why diarrhoea is often absent.
3. **Phagocytosis by macrophages and monocytes** (`CL:0000235`, `CL:0000576`; `GO:0006909`) **leads to** an intracellular niche. ST313 is taken up more efficiently than ST19: **[verbatim abstract, PMID:25569606]** "strains of the ST313 genotype are phagocytosed more efficiently and are highly resistant to killing by macrophage cell lines and primary mouse and human macrophages compared to ST19 strains."
4. **Intramacrophage survival and replication** (`GO:0030254` type III secretion; SPI-2) **results in** a replicating, sheltered bacterial population. **[verbatim abstract, PMID:25569606]** "*S*. Typhimurium ST313 strains survived and replicated within different macrophages." Malawian sublineage 2.2 expresses SPI-2 constitutively even under non-inducing conditions **[tool-summarized, PMID:38623411]**, i.e. the intracellular programme is pre-armed.
5. **Blunted innate inflammatory response**, via reduced flagellin (`GO:0044780`) and consequently reduced inflammasome-driven IL-1β and pyroptosis (`GO:0032731`, `GO:0070269`), **leads to** failure of early containment and reduced macrophage death. **[verbatim abstract, PMID:25569606]** "Infection of macrophages with *S*. Typhimurium ST19 strains resulted in increased apoptosis and higher production of proinflammatory cytokines… compared to *S*. Typhimurium ST313 strains. This difference… could be explained, in part, by an increased production of flagellin by ST19 strains." Independent work confirms ST313 with "naturally attenuated flagellin elicits reduced inflammation and replicates within macrophages."
6. **Serum and antimicrobial-peptide resistance** — increased *pgtE* expression **results in** degradation of host antimicrobial proteins and "increased resistance to complement deposition" (`GO:0006956`) **[tool-summarized, PMID:30657108]** — **leads to** survival in blood.
7. **Dissemination via infected mononuclear phagocytes** to reticuloendothelial organs — spleen (`UBERON:0002106`), liver and Kupffer cells (`UBERON:0002107`, `CL:0000091`), bone marrow (`UBERON:0002371`), mesenteric lymph nodes (`UBERON:0002509`), gallbladder (`UBERON:0002110`) — **results in** systemic infection. Demonstrated in vivo: D23580 colonized "the spleen, mesenteric lymph nodes and gall bladder in mice… more rapidly… when compared to… SL1344" **[verbatim abstract, PMID:26091096]** *(model organism)*.
8. **Sustained bacteraemia** (`UBERON:0000178`) **leads to** the clinical syndrome: fever, hepatosplenomegaly, respiratory signs, anaemia (`HP:0001945`, `HP:0001433`, `HP:0002789`, `HP:0001903`).

**Branch A — host control succeeds.** Adequate IL-12→IFN-γ→STAT1 signalling (`GO:0032735`, `GO:0032729`, `GO:0060333`, `GO:0071346`) drives macrophage activation (`GO:0042116`) and Th1 responses (`GO:0042088`, `CL:0000624`, `CL:0000623`) **resulting in** bacterial clearance. **[tool-summarized]** "macrophages recognize the bacteria, activating T cells and NK cells through IL-12 and IL-23, and these activated cells release interferon-γ, which enhances macrophage activity via STAT1, aiding pathogen clearance."

**Branch B — host control fails.** This is the disease. Three non-exclusive routes:
- **B1, cellular:** Mendelian IL-12/IFN-γ axis defect, or the *STAT4* risk genotype with "reduced interferon-γ production in stimulated natural killer cells" and lower circulating IFN-γ during acute bacteraemia **[tool-summarized, PMID:29523850]**, **leads to** failure of step B's macrophage activation.
- **B2, humoral (HIV):** HIV infection **leads to** dysregulated anti-LPS antibody that inhibits serum bactericidal killing rather than mediating it **[tool-summarized, PMID:20413503]** — a *gain* of a harmful antibody specificity, not simply a loss.
- **B3, phagocyte-functional (malaria):** haemolysis and haem oxygenase-1 induction are proposed to impair neutrophil oxidative burst (`CL:0000775`, `GO:0006979`, `GO:0006879`, `CHEBI:18248`), **leading to** permissiveness. *Mechanistically attractive and not established in human iNTS; curate as a hypothesis with `status: EMERGING`.*

**Downstream branches from sustained bacteraemia:**
- **→ Septic shock:** LPS-driven (`CHEBI:16412`, `GO:0032496`) cytokine response **results in** hypotension, lactataemia, DIC (`HP:0002615`, `HP:0002151`, `HP:0005521`).
- **→ Meningeal seeding** (`UBERON:0002360`, `UBERON:0001359`) **results in** meningitis with very high case fatality (`HP:0001287`).
- **→ Endovascular seeding** of atheromatous aorta or endocardium (`UBERON:0000947`, `UBERON:0002165`) **results in** mycotic aneurysm or endocarditis (`HP:0100584`). Predominantly in older adults.
- **→ Osteoarticular seeding** (`UBERON:0001474`, `UBERON:0003657`), strongly potentiated by sickle cell disease, **results in** osteomyelitis and septic arthritis (`HP:0005661`, `HP:0003095`).
- **→ Persistence in gallbladder/reticuloendothelial niche** with inadequate cell-penetrating therapy or uncorrected immunodeficiency **results in** recurrence (`HP:0002718`).

### Category checklist coverage

- **Molecular pathways:** IL-12/IL-23 → IFN-γ → JAK/STAT1 (KEGG hsa04630 JAK-STAT; hsa05132 *Salmonella* infection; Reactome interferon-γ signalling). Bacterial side: SPI-1 and SPI-2 type III secretion (`GO:0030254`), PhoPQ regulon, *pgtE*.
- **Cellular processes:** phagocytosis (`GO:0006909`), intracellular replication, macrophage apoptosis (`GO:0071888`), pyroptosis (`GO:0070269`), neutrophil chemotaxis (`GO:0030593`), macrophage activation (`GO:0042116`).
- **Protein dysfunction:** in the host, loss-of-function of IL-12Rβ1/IFNγR1/STAT1 (`functional_impact_category: LOSS_OF_FUNCTION` on the relevant `genetic_context`); in the pathogen, pseudogenization of flagellar and metabolic genes. Note for dismech: a pathogen-driven activity change with no host variant must use `Descriptor.modifier`, not `functional_impact_category` — the repository's `Adult_T_Cell_Leukemia_Lymphoma` precedent applies directly here.
- **Metabolic changes:** ST313 shows altered melibiose and inositol utilization and differing Voges-Proskauer/catalase results versus SL1344 **[verbatim abstract, PMID:26091096]** — bacterial metabolic remodelling consistent with host restriction. No characterized host metabolomic signature.
- **Immune involvement:** immunodeficiency-driven, not autoimmune. Both cellular (IFN-γ) and humoral (bactericidal antibody) arms are implicated, and their relative contribution is the field's stated open question: **[verbatim abstract, PMID:30657108]** "research efforts should focus on understanding the relative contributions of antibody and cell-mediated immunity to protection against iNTS disease in humans."
- **Tissue damage:** reticuloendothelial hyperplasia, abscess formation, endovascular wall destruction in mycotic aneurysm, meningeal inflammation.
- **Molecular profiling:** the substantial published profiling is **bacterial transcriptomics** (ST313 vs ST19 expression signatures; sublineage 2.2 signature, PMID:38623411) and **bacterial genomics** (PMID:37872141, PMID:40205197), not host omics. Host transcriptomic, proteomic, metabolomic and lipidomic signatures of iNTS disease are **not established** — search GEO/ArrayExpress at curation time rather than asserting any. The *STAT4* eQTL work (PMID:29523850) is the closest thing to a host functional-genomics result.
- **Single-cell / spatial / CRISPR screens:** no iNTS-specific published single-cell or spatial dataset was located. TraDIS (transposon-directed insertion-site sequencing) has been applied to *S.* Typhimurium in cattle, which is a bacterial functional-genomics screen and should be labelled as such.

---

## 7. Anatomical Structures Affected

**Primary (always):** blood `UBERON:0000178`.

**Reticuloendothelial system (near-always, often subclinically):** spleen `UBERON:0002106`; liver `UBERON:0002107`; bone marrow `UBERON:0002371`; mesenteric lymph nodes `UBERON:0002509`.

**Portal of entry:** small intestine `UBERON:0002108`, Peyer's patch `UBERON:0001211`, large intestine `UBERON:0000059`.

**Secondary/metastatic sites:** meninx `UBERON:0002360` and cerebrospinal fluid `UBERON:0001359`; lung `UBERON:0002048`; gallbladder `UBERON:0002110`; aorta `UBERON:0000947`; endocardium `UBERON:0002165`; bone element `UBERON:0001474`; limb joint `UBERON:0003657`.

**Body systems:** cardiovascular (bacteraemia, endovascular), haematopoietic/reticuloendothelial, digestive, respiratory, nervous (meningitis), musculoskeletal.

**Cell populations:**

| Cell type | CL term | Role |
|---|---|---|
| macrophage | `CL:0000235` | primary replicative niche |
| monocyte | `CL:0000576` | dissemination vehicle |
| Kupffer cell | `CL:0000091` | hepatic reservoir |
| neutrophil | `CL:0000775` | effector; impaired in malaria hypothesis |
| natural killer cell | `CL:0000623` | early IFN-γ source; site of *STAT4* effect |
| CD4-positive, alpha-beta T cell | `CL:0000624` | Th1 macrophage activation |
| dendritic cell | `CL:0000451` | antigen presentation / IL-12 |
| intestinal epithelial cell | `CL:0002563` | invasion (attenuated in ST313) |
| M cell of gut | `CL:0000682` | translocation route |
| B cell / memory B cell | `CL:0000236` / `CL:0000787` | bactericidal antibody; vaccine target |
| erythrocyte | `CL:0000232` | anaemia; haemolysis interface with malaria |

**Subcellular:** *Salmonella*-containing vacuole (GO cellular-component binding should be searched at curation time rather than assumed); phagolysosome; cytosol for inflammasome assembly. Do not write a GO CC CURIE for the *Salmonella*-containing vacuole from memory — resolve it.

**Localization/lateralization:** systemic and bilateral by nature. Focal complications are typically unilateral and site-specific (a single aortic segment, one long bone, one joint) — lateralization carries no diagnostic meaning here.

---

## 8. Temporal Development

- **Onset:** acute to subacute febrile illness developing over days. Not congenital. Age of occurrence is bimodal across settings: infants/toddlers in sub-Saharan Africa (peak "early in the second year of life" **[PMID:40684736]**), older adults elsewhere.
- **Stages:** no formal staging system exists. A clinically useful progression is (i) uncomplicated bacteraemic febrile illness → (ii) bacteraemia with organ dysfunction (respiratory, anaemia, encephalopathy) → (iii) septic shock, or focal metastatic infection → (iv) death or recovery, with (v) recurrence as a distinct later state.
- **Progression rate:** rapid. Untreated or inadequately treated disease progresses to death within days; meningitis and shock are the fastest routes.
- **Course pattern:** acute and self-limited *with treatment* in immunocompetent hosts; **relapsing/recurrent** in uncontrolled HIV (20–40% recurrence pre-ART **[PMID:22587967]**); pooled recurrence 4.8% in the global meta-analysis **[tool-summarized, PMID:35114140]**, a figure that reflects contemporary ART coverage.
- **Duration:** days to weeks for an episode; chronic only in the sense of repeated episodes or an untreated endovascular/osteoarticular focus.
- **Remission:** treatment-induced. Spontaneous resolution of true bacteraemia in a susceptible host should not be assumed.
- **Critical intervention windows:** (a) first hours — prompt empiric therapy with an intracellularly active agent; (b) the whole episode — source control for endovascular foci, where **[tool-summarized, PMID:35041743]** "surgical intervention is indispensable in the management of *Salmonella* mycotic aneurysms"; (c) post-episode — ART initiation to prevent recurrence; (d) pre-exposure — infancy, the window a vaccine would target.

---

## 9. Inheritance and Population

### Epidemiology

**GBD 2017** **[PMID:31562022, DOI:10.1016/S1473-3099(19)30418-9]**:

| Metric (2017) | Estimate (95% UI) |
|---|---|
| Cases | 535,000 (409,000–705,000) |
| Deaths | 77,500 (46,400–123,000) |
| HIV-attributable deaths | 18,400 (12,000–27,700) — 24.3% of total |
| DALYs | 4.26 million (2.38–7.38 million) |
| Incidence, sub-Saharan Africa | 34.5 per 100,000 person-years (26.6–45.0) |
| Incidence, all other regions | <3.0 per 100,000 person-years |
| Incidence, <5 years | 34.3 per 100,000 person-years (23.2–54.7) |
| Case fatality, all ages | 14.5% (9.2–21.1) |
| Case fatality, ≥70 years | 51.2% (30.2–72.9) |
| Case fatality, HIV-positive | 41.8% (30.0–54.0) |
| Case fatality, HIV-negative | 12.0% (7.3–18.0) |

**GBD 2021** **[DOI:10.1371/journal.pntd.0012960, PLOS NTD, April 2025]** **[tool-summarized]**: 509,976 incident cases (95% UI 413,361–606,167); 4,740,235 DALYs (2,762,282–7,597,208); age-standardized incidence 7.21 per 100,000 (5.83–8.64); Western sub-Saharan Africa highest burden (305,959 cases; ASR 47.54); low-SDI incidence 20.91 per 100,000; cases rose 1990–2005 then declined 2005–2021, with a net 45% increase in absolute cases driven chiefly by population growth.

**Site-level trend, Blantyre, Malawi 2011–2019** **[PMID:37153453]** **[tool-summarized]**: minimum incidence fell from 21 to 7 per 100,000 per year; MDR in *S.* Typhimurium fell from 78.5% to 27.7% (via re-emergent chloramphenicol susceptibility); fluoroquinolone and third-generation cephalosporin resistance remained uncommon (1.3% and 1.1%); ESBL-producing *Salmonella* appeared in 2019.

**Case fatality, pooled** **[verbatim abstract, PMID:35114140]**: "the overall pooled CFR estimate was 14·7% (95% CI 12·2–17·3). When stratified by UN region, the pooled CFR was 17·1% (13·6–21·0) in Africa, 14·0% (9·4–19·4) in Asia, 9·9% (6·4–14·0) in Europe, and 9·6% (0·0–25·1) in the Americas."

Additional stratification **[tool-summarized, PMID:35114140]**: Southern Africa 33.1%, Western Africa 19.9%, Middle Africa 18.9%, Eastern Africa 15.8%; adults >15 y 21.0% vs children ≤15 y 12.0%; by serovar, Typhimurium 21.6%, Dublin 19.1%, Enteritidis 15.0%. HIV co-infection pooled OR for death 2.4 (95% CI 1.4–4.1).

An earlier Africa-specific systematic review covering 1966–2014 is available for regional incidence, risk factors and CFR **[PMID:28056035, DOI:10.1371/journal.pntd.0005118]**.

### Inheritance

**Not a heritable disease.** Inheritance pattern, penetrance, expressivity, anticipation, germline mosaicism, founder effects, consanguinity and carrier frequency are **not applicable to iNTS disease itself**. They apply only to the host susceptibility disorders in §4, where the MSMD-spectrum defects are variously autosomal recessive (*IL12B*, *IL12RB1*, complete *IFNGR1*/*IFNGR2*), autosomal dominant (partial *IFNGR1*, *STAT1*), or X-linked (*IKBKG*, *CYBB*). Do not populate an `inheritance:` block for this entry; record the susceptibility genes in `genetic:` with `relationship_type: SUSCEPTIBILITY` instead.

### Population demographics

- **Geographic:** overwhelmingly sub-Saharan Africa, with Western sub-Saharan Africa the highest-burden subregion. Secondary foci in South and Southeast Asia and East Asia (Taiwan, mainland China), where the adult/elderly endovascular phenotype predominates. Lowest burden Australasia.
- **Variant geography:** ST313-L2 originated in DRC (~1980), spread to East Africa (~1995–2000) and West Africa (Ghana, 1994); sublineages 2.2 and 2.3 emerged in Malawi in 2006 and 2008 and now dominate there **[PMID:37872141, PMID:38623411]**.
- **Age:** infants and children <5 years in Africa; ≥55 years in high-income and East Asian series.
- **Sex ratio:** reported as a significant risk factor in the global genomic census **[PMID:40205197]** but the direction and magnitude should be read from that paper; do not assert a ratio from this report.
- **Ethnicity:** the burden distribution is driven by comorbidity prevalence and geography, not by ancestry per se. The one ancestry-linked genetic signal, *STAT4* rs13390936, was identified in Kenyan and Malawian children; its frequency in other populations should be read from gnomAD.

---

## 10. Diagnostics

### The one indispensable test

**Blood culture.** **[tool-summarized, PMID:30657108]** "bacterial culture of blood or cerebrospinal fluid is the only available method for diagnosis." This is the central diagnostic and health-systems problem: iNTS disease is undiagnosable clinically, and blood-culture capacity is scarce exactly where the disease is. The Marchello authors explicitly conclude **[verbatim abstract, PMID:35114140]** that "investments in improving clinical microbiology facilities to identify non-typhoidal salmonella… would prevent non-typhoidal salmonella invasive disease-associated illness and death."

Suggested terms: `NCIT:C19347` Culturing, In Vitro Microbial; `NCIT:C122437` Positive Blood Culture; `NCIT:C173272` CSF Analysis. LOINC codes for blood culture and CSF culture should be looked up at curation time.

### Supporting laboratory tests

Full blood count (anaemia, thrombocytopenia, leukocyte abnormalities), CRP/procalcitonin, lactate, glucose, renal and liver panels, blood film or rapid diagnostic test for malaria co-infection, HIV testing (mandatory in any adult with NTS bacteraemia, since it is AIDS-defining), CD4 count, sickle cell screening in children with osteomyelitis. Antimicrobial susceptibility testing is essential given the resistance landscape (§4).

### Biomarkers

No validated iNTS-specific diagnostic or prognostic biomarker exists. No FDA-qualified biomarker is listed for this indication. Serology is not diagnostically useful — the MacLennan finding (high anti-LPS titres in the most susceptible hosts) shows why antibody titre cannot serve as a diagnostic marker here.

### Imaging and functional studies

Imaging is used to find and characterize a focus, not to diagnose the infection: chest radiograph or CT for pneumonia and empyema; CT angiography for suspected mycotic aneurysm (essential in any older adult with NTS bacteraemia and back or abdominal pain); echocardiography for endocarditis; MRI for osteomyelitis and discitis; ultrasound or CT for splenic and hepatic abscess; CT/MRI brain in meningitis. Electrophysiology (EEG, EMG, ECG) has no primary diagnostic role; EEG may be used in encephalopathy or seizures.

### Biopsy and pathology

Histopathology is rarely the diagnostic route. When tissue is obtained (aneurysm wall, bone, abscess), findings are non-specific acute suppurative inflammation with necrosis; culture of the tissue is the informative test. Reticuloendothelial hyperplasia may be seen at autopsy.

### Genetic testing

Genetic testing is **not** part of diagnosing an iNTS episode. It is indicated to investigate the host when the clinical pattern suggests an inborn error: recurrent NTS invasive disease, NTS disease in an immunocompetent-appearing child, disseminated disease with an unusual serovar, or co-occurring mycobacterial or *BCG* disease. In that setting:

- **Targeted gene panel** for MSMD / inborn errors of IL-12/IFN-γ immunity is the appropriate first-line test — consult the Genetic Testing Registry for current panels.
- **WES/WGS** is appropriate when a panel is negative and clinical suspicion of an inborn error persists.
- **Single-gene testing** is reasonable when a specific syndrome is suspected (e.g. *CYBB* for CGD with a suggestive dihydrorhodamine assay, or haemoglobin electrophoresis rather than sequencing for sickle cell disease).
- **Chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion testing: not applicable.** No copy-number, aneuploidy, mitochondrial, or repeat-expansion mechanism is implicated. Say so explicitly in the entry rather than leaving the fields ambiguous.
- Functional immunology often precedes or complements sequencing: dihydrorhodamine/nitroblue-tetrazolium for CGD, IFN-γ/IL-12 pathway functional assays.

### Omics-based diagnostics

**Pathogen-side WGS is the mature omics application** and is genuinely diagnostic-adjacent: it assigns sequence type and lineage, predicts resistance from *gyrA*/*bla*CTX-M/*mphA* genotype, and supports transmission inference **[PMID:37872141, PMID:40205197]**. Host-side RNA-seq, proteomics, metabolomics, epigenomics and liquid biopsy have **no established diagnostic role** for iNTS. Direct-from-blood molecular assays (multiplex PCR, metagenomic sequencing) are an active research direction for febrile-illness diagnosis in low-resource settings but are not standard of care for iNTS.

### Clinical criteria and differential diagnosis

There is **no consensus clinical case definition**; the case definition is microbiological — isolation of a non-typhoidal *Salmonella* serovar from blood, CSF, or another normally sterile site. This is precisely how the meta-analysis defined inclusion **[verbatim abstract, PMID:35114140]**: "confirmed by culture of samples taken from a normally sterile site (eg, blood or bone marrow)."

Differential diagnosis of the African febrile child or adult presenting this way:

| Condition | Distinguishing feature |
|---|---|
| Severe malaria | Parasitaemia on film/RDT — but **co-infection is common**, so a positive malaria test does not exclude iNTS |
| Typhoid fever (*S.* Typhi) | Clinically near-identical; separated only by serovar identification |
| Pneumococcal or other bacterial sepsis | Blood culture |
| Bacterial meningitis (other organisms) | CSF culture/PCR |
| Tuberculosis, disseminated | Chronicity, imaging, mycobacterial testing; note MSMD hosts get both |
| HIV seroconversion / opportunistic infection | HIV testing and CD4 |
| Rickettsial and arboviral febrile illness | Serology, exposure history, blood-culture-negativity |
| Brucellosis, leptospirosis, melioidosis | Geography, exposure, targeted culture/serology |

### Screening

**No screening programme exists or is recommended for iNTS**, and none of newborn screening, carrier screening, or cascade screening applies. The closest analogues are (a) HIV testing as reflex screening in anyone with NTS bacteraemia, and (b) cascade family evaluation when an inborn error of IL-12/IFN-γ immunity is identified in an index case. Record both as such rather than as disease screening.

---

## 11. Outcome / Prognosis

### Mortality

- **Pooled case fatality: 14.7% (95% CI 12.2–17.3)** **[PMID:35114140]**; GBD 2017 estimate 14.5% **[PMID:31562022]**. The WHO consultation characterizes iNTS in sub-Saharan Africa as "associated with up to 20 % case-fatality ratio" **[verbatim abstract, PMID:40132323]**.
- **Age gradient is steep:** children ≤15 y 12.0%, adults >15 y 21.0% **[PMID:35114140]**; GBD puts ≥70 y at 51.2% **[PMID:31562022]**.
- **HIV is the dominant prognostic comorbidity:** CFR 41.8% HIV-positive vs 12.0% HIV-negative **[PMID:31562022]**; pooled OR for death 2.4 (1.4–4.1) **[PMID:35114140]**.
- **Serovar matters:** Typhimurium 21.6% > Dublin 19.1% > Enteritidis 15.0% **[PMID:35114140]**.
- **Syndrome matters most:** meningitis case fatality up to 50–70% in reviews, ~20% in African infants **[PMID:35041743]**; endocarditis "mortality is almost 50%, with or without cardiac surgery" **[tool-summarized, PMID:35041743]**.

Survival is measured in 30-day or in-hospital terms, not 5- or 10-year terms. **Do not populate 5-year or 10-year survival fields** — they are not meaningful for an acute infection, and no such data exist. Life expectancy after recovery is governed by the underlying comorbidity (HIV stage, sickle cell disease), not by the iNTS episode.

### Morbidity and function

Disability arises from (a) the acute episode's DALY burden — 4.26 million DALYs in 2017 **[PMID:31562022]**, 4.74 million in 2021 **[DOI:10.1371/journal.pntd.0012960]** — dominated by years of life lost in young children rather than years lived with disability; (b) neurological sequelae of meningitis (hearing loss, epilepsy, developmental impairment) in survivors; (c) orthopaedic sequelae of osteomyelitis; (d) post-surgical morbidity after aneurysm repair. **No iNTS-specific EQ-5D, SF-36, PROMIS, or ICF-coded outcome data were located.** State this absence rather than borrowing a generic sepsis instrument.

### Complications and recovery

See §3 for the complication table. Recovery is generally complete in immunocompetent survivors of uncomplicated bacteraemia treated promptly. Recovery potential is materially worse with (i) meningitis, (ii) endovascular focus without surgery, (iii) uncontrolled HIV, (iv) shock at presentation.

### Prognostic factors

Established or strongly supported: HIV status and CD4 count; age (both extremes); shock at presentation; meningitis; endovascular focus; serovar; malnutrition; antimicrobial resistance of the isolate and consequent delay to effective therapy; malignancy. In the elderly Taiwanese cohort, independent predictors of 30-day mortality were solid-organ tumour (aOR 4.4), mycotic aneurysm (aOR 3.7), and shock (aOR 12.1) **[tool-summarized, PMID:22261309]**.

Notably, malaria co-infection was **not** associated with increased mortality in the pooled analysis (OR 0.6, 95% CI 0.3–1.4) **[tool-summarized, PMID:35114140]** — malaria is a risk factor for acquiring iNTS disease but not, on this evidence, for dying of it. That distinction matters and is easy to get wrong.

**No validated prognostic biomarker or prediction model** exists for iNTS. Lactate, CRP and procalcitonin carry generic sepsis prognostic information only.

---

## 12. Treatment

### Core principle

Effective agents must reach an intracellular pathogen. **[tool-summarized, PMID:35041743]** the agents with adequate intracellular penetration are "trimethoprim/sulfamethoxazole, fluoroquinolones, third generation cephalosporins, and azithromycin," and critically, **[tool-summarized, PMID:35041743]** "aminoglycosides should not be used even if the organisms are susceptible in vitro." That in-vitro-susceptible-but-clinically-ineffective gap is the single most important prescribing trap in this disease, and it has a mechanistic basis: gentamicin "lacks intracellular penetration" **[tool-summarized, PMID:30657108]**.

### Pharmacotherapy

| Agent | CHEBI | Role | dismech modelling note |
|---|---|---|---|
| Ceftriaxone | `CHEBI:29007` | first-line empiric in Africa | `treatment_term` `NCIT:C15986` Pharmacotherapy + `therapeutic_agent` ceftriaxone; `therapeutic_modality: SMALL_MOLECULE` |
| Cefotaxime | `CHEBI:204928` | alternative third-generation cephalosporin | as above |
| Ciprofloxacin | `CHEBI:100241` | targeted therapy for confirmed iNTS **[tool-summarized, PMID:30657108]** | note reduced-susceptibility caveat below |
| Azithromycin | `CHEBI:2955` | intracellularly active option | *mphA*-mediated resistance emerging |
| Co-trimoxazole | `CHEBI:3770` (components `CHEBI:45924`, `CHEBI:9332`) | historic therapy; now widely resisted; also HIV prophylaxis | |
| Ampicillin | `CHEBI:28971` | historic; MDR *bla*TEM | |
| Chloramphenicol | `CHEBI:17698` | historic; susceptibility re-emerged in Malawi | |
| Meropenem | `CHEBI:43968` | reserve for ESBL/XDR isolates | |
| Dexamethasone | `CHEBI:41879` | adjunct in bacterial meningitis per general guidelines | evidence is not iNTS-specific — mark as such |

**Fluoroquinolone caveat** **[tool-summarized, PMID:35041743]**: the reduced-breakpoint problem established for nalidixic-acid-resistant *S.* Typhi means "it is likely that the same issue pertains to treatment of iNTS infections." Read that as an explicit inference, not a demonstrated iNTS finding.

**Duration** is not standardized and should be taken from current guidelines at curation time, not from this report. The principle is that uncomplicated bacteraemia requires a substantially shorter course than an endovascular or osteoarticular focus, and that a focus requires prolonged therapy plus source control.

### Pharmacogenomics

No CPIC guideline or FDA pharmacogenomic biomarker applies to iNTS therapy specifically. *NAT2* and *G6PD* considerations for co-trimoxazole, and *CYP3A4* interactions with azithromycin and antiretrovirals, are general rather than iNTS-specific. Check PharmGKB rather than asserting anything here.

### Surgical and interventional

Source control is decisive for endovascular disease: **[tool-summarized, PMID:35041743]** "surgical intervention is indispensable in the management of *Salmonella* mycotic aneurysms." Also relevant: abscess drainage, empyema drainage, osteomyelitis debridement, prosthetic joint management (rare — "accounting for only 0.2% of PJI treated at the Mayo Clinic" **[tool-summarized, PMID:35041743]**), valve surgery in endocarditis. Suggested term `NCIT:C15329` Surgical Procedure; `therapeutic_modality: SURGERY`.

### Supportive, rehabilitative, and comorbidity-directed care

Fluid resuscitation (`NCIT:C116537` Fluid Therapy), blood transfusion for severe anaemia (`NCIT:C15192`), oxygen and respiratory support, antimalarial treatment of co-infection, nutritional rehabilitation (`NCIT:C15433` Nutritional Support), and — pivotally for recurrence prevention — **antiretroviral therapy** (`NCIT:C94631` Antiretroviral Therapy). General supportive care `NCIT:C15747`. Rehabilitation is relevant to meningitis and osteomyelitis survivors (physiotherapy, audiology, developmental follow-up).

> **dismech binding caution.** `TreatmentTerm` is rooted at `NCIT:C25218` (Clinical Intervention or Procedure). Several terms above were resolved by label only and their enum reachability was **not** checked — `NCIT:C116537` Fluid Therapy and `NCIT:C122437` Positive Blood Culture in particular need `just validate-terms` before use. `NCIT:C20496` Interferon Gamma and `NCIT:C126712` Fluoroquinolone Antibiotic are substances/classes, not clinical actions, and belong in `therapeutic_agent` or `qualifiers`, never in `treatment_term.term`.

### Advanced therapeutics

- **Gene therapy, cell therapy, RNA-based therapy, CAR-T, checkpoint inhibitors: not applicable** to iNTS disease. Haematopoietic stem cell transplantation is relevant only as curative therapy for an underlying inborn error of IL-12/IFN-γ immunity, and should be curated on that entry rather than here.
- **Recombinant IFN-γ** is used adjunctively in some patients with MSMD-spectrum defects and refractory intracellular infection. Evidence in iNTS specifically is case-level; curate with `evidence_source: HUMAN_CLINICAL` and `directness: INDIRECT` at best.
- **Monoclonal antibodies:** a specific monoclonal antibody has been shown to overcome *S.* Typhimurium's intramacrophage survival mechanisms in vitro — a preclinical lead only.

### Experimental treatments in trials

The active clinical development in this disease is **preventive, not therapeutic** (§13). No interventional therapeutic trial specific to iNTS disease was identified. One observational trial directly relevant to prevention is registered:

| Field | Value |
|---|---|
| Registration | **NCT07416461** (VINS) |
| Title | Effectiveness of Malaria Vaccines in Reducing the Risk of Invasive Non-Typhoidal *Salmonella* Disease |
| Status | Recruiting; actual start 2025-10-27 |
| Design | Observational, case-control (test-negative), prospective |
| Intervention studied | R21/Matrix-M malaria vaccine |
| Primary outcome | Blood-culture-confirmed iNTS disease in fully malaria-vaccinated vs unvaccinated children |
| Enrolment | 10,000 (estimated) |
| Setting / sponsor | Kisantu Health Zone, DRC / International Vaccine Institute |

Curate this as `phase: NOT_APPLICABLE` (observational) and `status: RECRUITING`, and re-check the status before commit — the repository's `just clinicaltrials-status-audit` exists precisely because these drift.

### Treatment strategy

Empiric therapy for severe febrile illness in an iNTS-endemic setting must cover NTS with a cell-penetrating agent, which in practice means a third-generation cephalosporin. On culture confirmation, narrow by susceptibility, extend duration for a focus, image for endovascular disease in older adults, treat malaria co-infection, test for HIV and start ART, and correct malnutrition and anaemia. There is no genotype-guided personalization of iNTS therapy; the one place host genotype changes management is when an inborn error of immunity is identified, which changes long-term prophylaxis and transplant candidacy rather than the acute regimen.

---

## 13. Prevention

### Primary prevention

**Comorbidity control is the intervention with demonstrated population effect.** The Malawian decline — 21 to 7 per 100,000 per year between 2011 and 2019 **[PMID:37153453]** — occurred alongside reductions in malaria, HIV and acute malnutrition, and modelling attributes it to that combination rather than to any one factor **[PMID:26230258]**. Read this as strong quasi-experimental evidence that iNTS is controllable indirectly, and as the rationale for the VINS malaria-vaccine study above. Components: insecticide-treated nets and malaria chemoprevention, ART scale-up and prevention of vertical HIV transmission, nutrition programmes. `NCIT:C15843` Preventive Intervention; `NCIT:C16664` Health Education.

### Immunization — the central prevention question

No licensed iNTS vaccine exists. **[verbatim abstract, PMID:30657108]** "No vaccine is currently available, making this a priority area for global health research." The pipeline has moved substantially since 2023, and this is the part of the entry most likely to be stale within a year.

| Candidate | Platform | Stage / result | Registration | Citation |
|---|---|---|---|---|
| **iNTS-GMMA** (GSK GVGH) | Bivalent generalized modules for membrane antigens (SEn + STm O-antigen) | First-in-human phase 1, 31 healthy adults, 3 doses at 0/2/6 months. **[tool-summarized]** No serious or unexpected severe AEs; "All participants (19/19, 100%) in the iNTS-GMMA groups reported at least one solicited AEs, which were mostly mild to moderate in severity"; anti-O-antigen IgG and serum bactericidal antibody peaked at day 28 and persisted to day 350; supports advancement to phase I/II African trials | EudraCT 2020-000510-14; ISRCTN51750695 | **PMID:40907249**, eBioMedicine 2025, DOI:10.1016/j.ebiom.2025.105903 |
| **SALVO** | iNTS-GMMA in a European cohort | Randomised placebo-controlled trial protocol published | — | **PMID:37963701**, BMJ Open 2023, DOI:10.1136/bmjopen-2023-072938 |
| **TSCV** (trivalent Salmonella conjugate) | Vi–tetanus-toxoid + core-plus-O-polysaccharide of STm and SEn conjugated to homologous FliC flagellin | **[verbatim abstract, PMID:41062830]** "A total of 22 healthy adults aged 18-45 years were randomly allocated to 6.25-µg TSCV (n = 8), 12.5-µg TSCV (n = 10) or placebo (n = 4)… TSCV was safe and well tolerated… For each of the three polysaccharides, immune responses, as demonstrated by ≥4-fold increases over baseline, were observed among all (100%) vaccinees, and no responses were elicited in the placebo group" | NCT03981952 | **PMID:41062830**, Nature Medicine 2025, DOI:10.1038/s41591-025-04003-z |
| **TSCV, phase 1/2a** | as above, dose-ranging in 80 US adults | **[tool-summarized]** Well tolerated, no fevers; 85–100% response rates to all three polysaccharide antigens with no significant difference between doses | NCT05525546 | **PMID:41885624**, J Infect Dis 2026;233(6):1081–1090, DOI:10.1093/infdis/jiag156 |
| **iNTS-TCV** (GVGH, trivalent with typhoid) | GMMA + TCV combination | Trial registered and ongoing | NCT05480800 | ClinicalTrials.gov |

Regulatory and policy framing **[verbatim abstract, PMID:40684736]**: "A clinical development plan and regulatory pathway for licensure of iNTS vaccines has been shaped following the development of Preferred Product Characteristics and R&D Roadmap through a series of expert consultations. Several iNTS alone or combined with Typhoid Conjugate Vaccine platforms are in early clinical development. Encouraging safety and immunogenicity data have prompted developers and manufacturers to plan efficacy trials, aligned with regulatory expectations." The WHO expert consultation report **[PMID:40132323]** is the authoritative statement of the vaccine use case and Full Value of Vaccines Assessment framing.

Suggested term for the intervention class: `NCIT:C15346` Vaccination; `therapeutic_modality: VACCINE`.

### Secondary prevention

No screening programme for asymptomatic iNTS is recommended or plausible — there is no asymptomatic detectable state to screen for. Secondary prevention in practice means **reducing time from fever to effective therapy**, which is a diagnostic-capacity intervention (blood culture availability) rather than a screening one.

### Tertiary prevention

Preventing recurrence and complications: ART initiation and adherence (the single most effective measure, given 20–40% pre-ART recurrence **[PMID:22587967]**); co-trimoxazole prophylaxis in HIV per national guidelines (`NCIT:C51993` Antibiotic Prophylaxis — note this reduces a range of infections and is not iNTS-specific); source control for endovascular and osteoarticular foci; nutritional rehabilitation; pneumococcal and other routine immunization in sickle cell disease.

### Genetic counselling

Applies only to identified inborn errors of IL-12/IFN-γ immunity and to sickle cell disease, where standard counselling, carrier testing and prenatal options apply to *those* conditions. There is **no genetic counselling, carrier screening, PGD, or prenatal testing for iNTS disease**. Do not create a `treatments:` entry for genetic counselling on this disease entry.

### Public health and environmental interventions

Water, sanitation and hygiene; food safety along the poultry, egg, dairy and meat chain; hand hygiene; health education. **The honest caveat is that the evidence base for WASH and food-safety impact on African iNTS specifically is thin**, because the reservoir is unresolved (§5). If transmission is predominantly person-to-person within households, as the recent genomic evidence suggests **[PMID:36910696, PMID:40205197]**, then food-chain interventions designed for zoonotic NTS may have limited effect on iNTS, and household-level hygiene and case-contact measures matter more. This is a live policy-relevant uncertainty and should be curated as such.

---

## 14. Other Species / Natural Disease

### Taxonomy of affected hosts

| Species | NCBITaxon | Relevance |
|---|---|---|
| *Homo sapiens* | `NCBITaxon:9606` | the disease entry's host |
| *Bos taurus* | look up at curation time | *S.* Dublin host-adapted reservoir |
| *Mus musculus* | `NCBITaxon:10090` | primary experimental model |
| *Gallus gallus* | `NCBITaxon:9031` | experimental model; poultry reservoir for NTS generally |
| *Macaca mulatta* | `NCBITaxon:9544` | non-human primate work exists for *Salmonella* generally |

### Natural disease in other species

The clearest natural counterpart is **bovine salmonellosis due to *S.* Dublin**, a host-adapted invasive serovar. **[tool-summarized]** *S.* Dublin "is a bovine-adapted zoonotic pathogen, capable of causing invasive disease in both cattle and human hosts"; it is "the most common serovar isolated from clinical case submissions" in cattle, has "become substantially more prevalent in dairy and calf-rearing facilities in the US and Canada since 2012," and in calves "infections are invasive, leading to high rates of septicemia, respiratory disease, and death." Transmission is "primarily fecal-oral, cattle-to-cattle and cattle-to-human transmission may also occur via contaminated saliva or milk," and the organism is multi-drug resistant.

This matters for the human entry in two ways: *S.* Dublin has the third-highest serovar-specific human iNTS case fatality (19.1% **[PMID:35114140]**), and it is the one invasive serovar with an unambiguous animal reservoir — the counterexample that makes the African ST313 host-restriction argument sharper.

Non-typhoidal salmonellosis also occurs naturally in horses, pigs, poultry, reptiles (a well-known source of human paediatric infection), companion animals, and wildlife. OMIA is the resource for any heritable animal susceptibility trait; none is established as a counterpart to human MSMD for this purpose.

### Comparative biology and evolutionary conservation

The mechanistically interesting comparison is **convergent host restriction**: ST313 is undergoing genome degradation that parallels *S.* Typhi and *S.* Paratyphi A **[verbatim abstract, PMID:25569606]**, and independently parallels the host adaptation of *S.* Dublin (cattle) and *S.* Gallinarum (poultry). Pseudogene accumulation, reduced flagellar expression, and loss of broad-host-range metabolic capacity recur across these lineages. The host-side IL-12/IFN-γ axis is deeply conserved, which is what makes the mouse model informative at all — IFN-γ-axis knockouts in mice reproduce the human susceptibility phenotype in kind.

### Zoonotic potential and cross-species susceptibility

Non-typhoidal *Salmonella* as a genus is strongly zoonotic. The specific African iNTS pathovars appear to be losing that character, which is the crux of §5. Cross-species experimental susceptibility is demonstrated: D23580 (ST313) "is able to establish an invasive infection in chickens" **[verbatim abstract, PMID:26091096]**, so ST313 is not host-restricted in the strict experimental sense even if it is epidemiologically anthroponotic. Both facts should appear in the entry; quoting only one misrepresents the field.

---

## 15. Model Organisms

### Murine models

**Oral-challenge BALB/c model of ST313** **[verbatim abstract, PMID:26091096]**: "we report that D23580 causes lethal and invasive disease in a murine model of infection following peroral challenge. The LD50 of D23580 in female BALB/c mice was 4.7 x 10⁵ CFU. Tissue distribution studies performed 3 and 5 days post-infection confirmed that D23580 was able to more rapidly colonize the spleen, mesenteric lymph nodes and gall bladder in mice when compared to the well-characterized *S*. Typhimurium strain SL1344." The authors state this is "the first full duration infection study using an ST313 strain following the entire natural course of disease progression."

For a dismech `animal_models[]` entry:

```
species: Mouse
genotype: BALB/c (Nramp1/Slc11a1-susceptible), wild-type host
name: BALB/c peroral D23580 (ST313) challenge model
publication: PMID:26091096
modeled_mechanisms:
  - target: <dissemination-to-reticuloendothelial-organs node>
    relationship: PARTIALLY_RECAPITULATES
    fidelity: MODERATE
    model_scale: ORGANISM
    limitations: >-
      BALB/c mice carry a susceptible Slc11a1 allele, so the model's
      permissiveness derives from a murine genetic defect with no counterpart
      in the human risk factors (HIV, malaria, malnutrition) that define iNTS
      disease. The model reproduces invasive dissemination but not the
      comorbidity gating that is the disease's defining epidemiological feature.
```

**Key limitation to state explicitly:** the standard mouse typhoid model achieves invasiveness through *Slc11a1* (Nramp1) susceptibility and an artificially high inoculum, not through the immunodeficiency states that permit human iNTS disease. A `HUMAN_MODEL_MISMATCH` discussion is the right structure for this, not a generic `KNOWLEDGE_GAP` — the model exists and works, and the open question is its translational validity to the comorbidity-gated human disease.

### Cellular and in vitro models

The macrophage-infection system is where the ST313 phenotype was defined **[PMID:25569606]**, using J774 murine macrophages, THP-1 cells, U937 monocytes, HEK293-Luc reporter cells, primary peritoneal macrophages from BALB/c and CD-1 mice, and human PBMCs. Reported quantitative readouts **[tool-summarized]**: ST313 intracellular survival 160% ± 26% in THP-1 at 24 h versus 47% ± 3% for ST19; motility zone 17 ± 3 mm (ST313) versus 24 ± 2 mm (ST19), *P*<0.001; lower IL-1β and TNF-α at 3 and 8 h.

For dismech, these are `experimental_models:` entries (non-animal systems) with `modeled_mechanisms` linking to the intramacrophage-replication and blunted-inflammation nodes, `model_scale: CELLULAR`, and `readouts` carrying the survival percentages and motility measurements above. Note that linking a `CELLULAR`-scale model to a `TISSUE`- or `ORGANISM`-scale node is upward extrapolation and requires `limitations` under `check_upward_extrapolating_links_are_caveated`.

### Avian model

D23580 establishes invasive infection in experimentally infected chickens, demonstrating that ST313 is "not host-restricted" in an experimental sense. Useful specifically for testing the host-restriction hypothesis; `species: Chicken`, `NCBITaxon:9031`, `relationship: PARTIALLY_RECAPITULATES` at best, since the avian immune context differs substantially.

### Genetic models available

Mouse knockouts across the relevant axis are standard and well-characterized: *Ifng*, *Ifngr1*, *Ifngr2*, *Il12b*, *Il12rb1*, *Stat1*, *Stat4*, *Slc11a1* congenics, *Cybb* (CGD model). Conditional and humanized options exist. Consult MGI, IMPC, KOMP and IMSR for current allele availability rather than asserting a specific allele here. A *Stat4* model is the obvious direct test of the human GWAS finding and would close a real evidential gap — the human result is genetic and eQTL-based, and an in vivo challenge experiment in a *Stat4*-hypomorphic host would be the corresponding `Experiment` with `would_support: pathophysiology#<IFN-γ axis failure node>`.

### Bacterial genetic resources

Not "model organisms" in the usual sense but central to this disease's experimental literature: D23580 is the reference ST313 L2 isolate with an annotated, functionally characterized genome; SL1344 and ATCC 14028 are the ST19 comparators; A130 is a second ST313 strain. Transposon-directed insertion-site sequencing has been applied to *S.* Typhimurium in a bovine niche.

### What the models do not capture

1. **Comorbidity gating** — no model reproduces the HIV/malaria/malnutrition context that defines human iNTS.
2. **Dysregulated inhibitory anti-LPS antibody** — the MacLennan mechanism **[PMID:20413503]** is a human HIV-specific phenomenon with no animal counterpart.
3. **Transmission** — if iNTS is person-to-person **[PMID:40205197]**, no animal model can test the transmission route.
4. **Human-specific IFN-γ axis variants** — mouse orthologs are conserved but the specific human hypomorphic alleles and the *STAT4* eQTL effect are not modelled.

---

## Cross-cutting notes for the dismech entry

1. **Genetics slots:** populate `genetic:` with `relationship_type: SUSCEPTIBILITY` only. There is no causal gene, no inheritance block, no chromosomal abnormality, no host epigenetics. Say so explicitly in `notes:` rather than leaving the sections silently empty.
2. **Pathogen activity states use `modifier`, not `functional_impact_category`.** ST313's constitutive SPI-2 expression and blunted flagellin output are bacterial states with no host variant to describe — the same rule the repository applies to HTLV-1 Tax in `Adult_T_Cell_Leukemia_Lymphoma`.
3. **Prevalence records:** GBD figures are `measure_type: ANNUAL_INCIDENCE` with `rate_denominator: PERSON_YEARS` (the GBD figures are per 100,000 person-years, and that denominator has no fallback). The Blantyre figures are minimum incidence estimates and should carry that caveat in `notes:`.
4. **Two case-fatality figures will both look right:** 14.5% (GBD 2017 modelled) and 14.7% (Marchello pooled, hospital-based). They are different measurements, not a discrepancy; record both with their measure and source rather than picking one.
5. **Candidate mechanism modules to check before creating anything new:** run `just list-modules` and look for existing sepsis/bacteraemia, intracellular pathogen persistence, granuloma/abscess, and immunodeficiency modules. `intracellular_pathogen_persistence` is named in CLAUDE.md as a gating module for antimicrobial work and is a strong `conforms_to` candidate for the intramacrophage-replication node.
6. **Coarse phenotype bindings are expected here** and are not a defect. `HP:0001945` Fever on a disease whose presentation is "fever alone" is `SOURCE_UNSPECIFIED` or `VARIABLE_SPECTRUM`, not a curation failure — see the `coarse-phenotype-bindings` skill.
7. **Every number and quotation above needs a cache file before it becomes evidence.** Fetch each PMID with `just fetch-reference`, then `just count-verified-snippets` in the loop and `just validate-disorders` once before the PR.

---

## Reference list

| PMID | DOI | Citation |
|---|---|---|
| 31562022 | 10.1016/S1473-3099(19)30418-9 | GBD 2017 Non-Typhoidal Salmonella Invasive Disease Collaborators. The global burden of non-typhoidal salmonella invasive disease. *Lancet Infect Dis* 2019;19(12):1312–24 |
| 35114140 | 10.1016/S1473-3099(21)00615-0 | Marchello CS, Birkhold M, Crump JA. Complications and mortality of non-typhoidal salmonella invasive disease: a global systematic review and meta-analysis. *Lancet Infect Dis* 2022;22(5):692–705 |
| 30657108 | 10.1128/ecosalplus.esp-0007-2018 | Invasive Nontyphoidal Salmonella Disease in Africa. *EcoSal Plus* 2019 |
| 22587967 | 10.1016/S0140-6736(11)61752-2 | Feasey NA, Dougan G, Kingsley RA, Heyderman RS, Gordon MA. Invasive non-typhoidal salmonella disease: an emerging and neglected tropical disease in Africa. *Lancet* 2012;379(9835):2489–99 |
| 37872141 | 10.1038/s41467-023-41152-6 | A genomic appraisal of invasive Salmonella Typhimurium and associated antibiotic resistance in sub-Saharan Africa. *Nat Commun* 2023 |
| 38623411 | 10.1093/femsml/uqae005 | S. Typhimurium ST313 sublineage 2.2 has emerged in Malawi with a characteristic gene expression signature and a fitness advantage. *microLife* 2024 |
| 25569606 | 10.1371/journal.pntd.0003394 | S. Typhimurium ST313 phagocytosis, macrophage survival and flagellin. *PLoS Negl Trop Dis* 2015 |
| 26091096 | 10.1371/journal.pntd.0003839 | Characterization of D23580 in a murine model of infection. *PLoS Negl Trop Dis* 2015 |
| 29523850 | 10.1038/s41467-017-02398-z | Risk of nontyphoidal Salmonella bacteraemia in African children is modified by STAT4. *Nat Commun* 2018 |
| 26109132 | 10.1038/nri3858 | Gilchrist JJ, MacLennan CA, Hill AVS. Genetic susceptibility to invasive Salmonella disease. *Nat Rev Immunol* 2015 |
| 20413503 | 10.1126/science.1180346 | MacLennan CA et al. Dysregulated humoral immunity to nontyphoidal Salmonella in HIV-infected African adults. *Science* 2010 |
| 35041743 | 10.1093/cid/ciac035 | Invasive Non-typhoidal Salmonella (iNTS) Infections. *Clin Infect Dis* 2022;75(4):732 |
| 37153453 | 10.12688/wellcomeopenres.17754.1 | Incidence of invasive non-typhoidal Salmonella in Blantyre, Malawi, January 2011–December 2019. *Wellcome Open Res* 2022 |
| 26230258 | 10.1371/journal.pntd.0003979 | Modelling the contributions of malaria, HIV, malnutrition and rainfall to the decline in paediatric iNTS disease in Malawi. *PLoS Negl Trop Dis* 2015 |
| 28056035 | 10.1371/journal.pntd.0005118 | Uche IV et al. A systematic review of the incidence, risk factors and case fatality rates of invasive nontyphoidal Salmonella (iNTS) disease in Africa (1966–2014). *PLoS Negl Trop Dis* 2017 |
| 36910696 | 10.1093/ofid/ofad086 | Chirwa EB, Dale H, Gordon MA, Ashton PM. What is the source of infections causing invasive nontyphoidal Salmonella disease? *Open Forum Infect Dis* 2023 |
| 40205197 | 10.1038/s41591-025-03644-4 | Genomic census of invasive nontyphoidal Salmonella infections reveals global and local human-to-human transmission. *Nat Med* 2025 |
| 40907249 | 10.1016/j.ebiom.2025.105903 | Safety and immunogenicity of the iNTS-GMMA vaccine: a first-in-human, randomised, dose escalation trial. *eBioMedicine* 2025 |
| 41062830 | 10.1038/s41591-025-04003-z | A combination typhoid and non-typhoidal Salmonella polysaccharide conjugate vaccine in healthy adults: phase 1. *Nat Med* 2025 |
| 41885624 | 10.1093/infdis/jiag156 | Safety and immunogenicity of a trivalent Salmonella conjugate vaccine. *J Infect Dis* 2026;233(6):1081–90 |
| 40132323 | 10.1016/j.vaccine.2025.127008 | Landscape analysis of iNTS disease and iNTS vaccine use case and demand: report of a WHO expert consultation. *Vaccine* 2025 |
| 40684736 | 10.1016/j.vaccine.2025.127515 | Non-typhoidal Salmonella combination vaccines: clinical development plan and regulatory considerations. *Vaccine* 2025 |
| 37963701 | 10.1136/bmjopen-2023-072938 | SALVO trial protocol. *BMJ Open* 2023 |
| 22261309 | 10.1017/S0950268811002901 | Non-typhoidal Salmonella bacteraemia in elderly patients. *Epidemiol Infect* 2012 |
| — | 10.1371/journal.pntd.0012960 | The global, regional, and national burden of invasive non-typhoidal Salmonella: GBD 1990–2021. *PLoS Negl Trop Dis* 2025 |
| — | NCT07416461 | VINS: Effectiveness of malaria vaccines in reducing the risk of iNTS disease (recruiting, 2025) |

**Sources:** [GBD 2017 iNTS burden](https://pmc.ncbi.nlm.nih.gov/articles/PMC6892270/) · [Marchello complications and mortality meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC9021030/) · [EcoSal Plus iNTS in Africa](https://pmc.ncbi.nlm.nih.gov/articles/PMC11573285/) · [Feasey Lancet 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3402672/) · [Genomic appraisal of invasive S. Typhimurium](https://pmc.ncbi.nlm.nih.gov/articles/PMC10593746/) · [ST313 sublineage 2.2 in Malawi](https://pmc.ncbi.nlm.nih.gov/articles/PMC11018118/) · [ST313 macrophage phenotype](https://pmc.ncbi.nlm.nih.gov/articles/PMC4287482/) · [D23580 murine model](https://pmc.ncbi.nlm.nih.gov/articles/PMC4474555/) · [STAT4 GWAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC5844948/) · [CID iNTS infections review](https://academic.oup.com/cid/article/75/4/732/6511004) · [Blantyre incidence 2011–2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC10160792/) · [Source of iNTS infections](https://pmc.ncbi.nlm.nih.gov/articles/PMC10004642) · [Nature Medicine genomic census](https://www.nature.com/articles/s41591-025-03644-4) · [iNTS-GMMA phase 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC12444187/) · [Trivalent Salmonella conjugate vaccine phase 1/2a](https://pmc.ncbi.nlm.nih.gov/articles/PMC13118129/) · [WHO iNTS vaccine landscape analysis](https://www.sciencedirect.com/science/article/pii/S0264410X25003056) · [GBD 1990–2021 iNTS](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0012960) · [MacLennan Science 2010](https://www.science.org/doi/10.1126/science.1180346) · [Elderly NTS bacteraemia](https://pubmed.ncbi.nlm.nih.gov/22261309/) · [VINS trial NCT07416461](https://clinicaltrials.gov/study/NCT07416461) · [MONDO:0017944 via NORD](https://rarediseases.org/mondo-disease/invasive-non-typhoidal-salmonellosis/) · [Salmonella Dublin in cattle](https://veterinaryresearch.biomedcentral.com/articles/10.1186/s13567-019-0720-5)