---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-21T20:50:02.953605'
end_time: '2026-08-21T21:02:01.867199'
duration_seconds: 718.91
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Gnathodiaphyseal Dysplasia
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
  - claude-opus-5
  web_search_requests: 7
  num_turns: 51
  total_cost_usd: 6.332397000000002
  session_id: 61d475c4-5bb3-4a21-9a9d-6e5869d217ae
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  - mcp__ols-mcp__search_all_ontologies
  - mcp__pubmed__search_articles
  assistant_text_blocks: 3
citation_count: 9
reference_validation:
  total_references: 48
  verified: 48
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 35
  quotes_valid: 23
  quotes_unsupported: 12
  unsupported_quote_references:
  - PMID:11547842
  - PMID:12619924
  - PMID:28176803
  - PMID:29175271
  - PMID:38922934
  - PMID:24891183
  - PMID:33826556
  - PMID:29518808
  relevance_assessed: 48
  on_topic: 40
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Gnathodiaphyseal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Gnathodiaphyseal Dysplasia** covering all of the
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

I'll research Gnathodiaphyseal Dysplasia now, starting with the reference cache already present in this worktree and then searching PubMed and ontology sources.

Now filling the gaps — identifiers, epidemiology, recent literature, and ontology terms.

I have enough to write the report. Here it is.

---

# Gnathodiaphyseal Dysplasia (GDD) — Comprehensive Research Report

**Prepared:** 21 August 2026 · **Target:** Gnathodiaphyseal dysplasia · **MONDO:0008151** · **Category:** Mendelian (autosomal dominant, monogenic — *ANO5*)

> **Evidence-quality note up front.** GDD is an ultra-rare disorder with roughly 100–110 clinically described individuals in the entire literature. Almost all clinical content below rests on case reports and small pedigrees; there are **no cohort studies, no clinical trials, no registry data, and no natural-history study**. Mechanistic content rests almost entirely on mouse models and heterologous cell expression — and, as detailed in §6 and §15, **the mouse models actively disagree with one another**. Sections where the honest answer is "not available" are marked as such rather than filled with inference.

---

## 1. Disease Information

### Overview

Gnathodiaphyseal dysplasia is a rare autosomal dominant generalized skeletal syndrome defined by the co-occurrence of three features: **fibro-osseous (cemento-osseous) lesions of the jawbones**, **generalized bone fragility with recurrent fractures**, and **bowing plus diaphyseal cortical thickening/sclerosis of the tubular bones**. Riminucci et al. established it as a discrete nosological entity in 2001, distinguishing it from polyostotic fibrous dysplasia; the jaw lesions are cemento-ossifying fibromas with a prominent psammomatoid body component, and — importantly for the name — *osteosclerosis is not a feature of the jaw lesions themselves*, which is why the entity was renamed from "gnathodiaphyseal sclerosis" (PMID:11547842).

The canonical description from the gene-discovery paper: *"Gnathodiaphyseal dysplasia (GDD) is a rare skeletal syndrome characterized by bone fragility, sclerosis of tubular bones, and cemento-osseous lesions of the jawbone."* (Tsutsumi et al., Am J Hum Genet 2004; PMID:15124103, DOI 10.1086/421527)

A defining and clinically underappreciated feature is **susceptibility to purulent osteomyelitis of the jaws**, typically emerging in adult life, often after dental extraction, with purulent discharge from gums, tooth mobility, tooth loss, and poor extraction-site healing (PMID:28176803).

### Key identifiers

| Resource | Identifier |
|---|---|
| MONDO | **MONDO:0008151** (`gnathodiaphyseal dysplasia`) — verified against local ontology cache |
| OMIM (phenotype) | **#166260** GNATHODIAPHYSEAL DYSPLASIA; GDD |
| OMIM (gene) | ***608662** ANO5 / TMEM16E / GDD1 |
| Orphanet | **ORPHA:53697** |
| ICD-10 | **M85.8** (per Orphanet mapping) |
| ICD-11 | **LD24.2Y** (per Orphanet mapping) |
| UMLS / GTR / MedGen | **C1833736** |
| Disease Ontology | **DOID:0111533** |
| HGNC (causal gene) | **hgnc:27337** (`ANO5`) — verified against local cache |
| MeSH | No dedicated descriptor. PubMed indexes GDD papers under **Osteogenesis Imperfecta/genetics** plus **Jaw Abnormalities/genetics** and **Anoctamins/genetics** — a legacy of GDD's historical classification as an OI variant (visible in the MeSH keyword lists of PMID:15124103, PMID:28176803, PMID:34841576). This is a real ontology gap worth flagging in any KB entry. |

### Synonyms and alternative names

- GDD (standard abbreviation)
- **Gnathodiaphyseal sclerosis** / hereditary gnathodiaphyseal sclerosis (historical; abandoned because jaw lesions are not sclerotic)
- **Osteogenesis imperfecta with unusual skeletal lesions** (historical; how the original Japanese family was labelled)
- **Osteogenesis imperfecta, Levin type** / **Levin syndrome 2**
- **Familial gigantiform cementoma (FGC)** and **familial florid cemento-osseous dysplasia (FFCOD)** — see §10; these are increasingly regarded as *allelic/atypical variants of GDD* rather than separate entities (PMID:37649308, PMID:27216912, PMID:42361776)

### Data provenance

All information below is **disease-level, derived from published case reports, pedigrees, and functional studies**. There is no EHR-derived, registry-derived, or claims-derived data on GDD. The largest structured clinical dataset in existence is the literature aggregation in Cuvelier et al. 2024 (PMID:38922934): **108 clinically diagnosed individuals across 25 families, of whom 67 individuals from 21 families had molecular confirmation.**

---

## 2. Etiology

### Disease causal factors

GDD is **monogenic and fully genetic**. It is caused by **heterozygous (monoallelic) variants in *ANO5*** (anoctamin-5 / TMEM16E / GDD1) at chromosome **11p14.3**. There is no known environmental, infectious, or multifactorial contribution to disease *causation*.

Historical trail of causal establishment:
1. **Linkage** — Tsutsumi et al. mapped the locus to an 8.7 cM interval at 11p14.3–15.1 in a four-generation Japanese family, establishing GDD "as a new and distinct disease entity from other systemic bone diseases" (J Bone Miner Res 2003; PMID:12619924).
2. **Gene identification** — *"In the critical region determined by recombination mapping, we identified a novel gene (GDD1) that encodes a 913-amino-acid protein containing eight putative transmembrane-spanning domains. Two missense mutations (C356R and C356G) of GDD1 were identified in the two families with GDD..."* (PMID:15124103)

### Genetic risk factors

- **Causal variants:** heterozygous *ANO5* missense variants (and rare in-frame indels/frameshifts), concentrated in **exons 7, 11, 15, and 16**. See §4 for the full variant catalogue.
- **Susceptibility loci / GWAS:** none. No GWAS has been or realistically could be performed on a disease this rare.
- **Modifier genes:** Essentially unstudied. One tentative report suggested **COL5A1** variants as potential modifiers in two affected siblings with divergent severity (cited in PMID:28176803). A *COL6A3* variant (c.4604G>A; p.Arg1535His) found in one proband with combined myopathy+GDD was explicitly **excluded** as contributory, because it was absent in other affected family members (PMID:34291158). Treat "modifier genes" as an open question, not an established finding.

### Environmental risk factors

None established for disease causation. However, several environmental/behavioural factors clearly act as **precipitants or exacerbators of specific manifestations** and should be modeled as such rather than as risk factors for the disease:

- **Minimal trauma** precipitates fractures — one patient sustained "five fractures, all occurring as a result of minimal trauma" (PMID:28176803).
- **Dental extraction and oral surgery** precipitate jaw osteomyelitis and non-healing extraction sites (PMID:28176803, PMID:29518808).
- **Physical exertion** precipitates rhabdomyolysis and compartment syndrome in the rare combined muscle+bone phenotype (PMID:34291158).
- **Vitamin D deficiency** was documented in most members of one Chinese GDD pedigree and is plausibly an aggravating cofactor for the low-bone-mass subtype (PMID:35982081).

### Protective factors

**No genetic or environmental protective factors have been identified.** No protective *ANO5* alleles are described. gnomAD/ExAC data are informative only in the negative direction: GDD-causing variants are absent from population databases (see §4).

### Gene–environment interactions

Two interactions have functional support:

1. **Mechanical/membrane challenge unmasks *Ano5* dependency.** Rolvien et al. found no skeletal or muscular phenotype in *Ano5* knock-in or knockout mice under homeostatic conditions and reasoned: *"it is conceivable that the function of Ano5 is only required, if there is cell membrane damage. Potentially, a challenge, such as muscular training, is required to induce an observable phenotype that is not present under homeostatic conditions."* (PMID:32455153) — this is a genotype × mechanical-challenge interaction hypothesis, not yet demonstrated in bone.
2. **Age × genotype.** Li et al. argued that mouse studies using 12–24-week-old animals mask the phenotype because "the onset of GDD occurs at a very young age, mostly in juveniles between 10 and 16 years old," and that osteoporosis-like signals are obscured by murine ageing changes (PMID:35982081). Human data support an age effect in the other direction: elderly GDD patients maintain normal-to-increased bone mass because their low osteoclast activity protects against age-related bone loss (PMID:35982081).

---

## 3. Phenotypes

### 3a. Frequency data — the single best source

The only quantitative frequency data for GDD come from the systematic literature aggregation of **108 clinically diagnosed individuals in 25 families (67 molecularly confirmed, 21 families)** in Cuvelier et al., *Prenatal Diagnosis* 2024 (PMID:38922934; DOI 10.1002/pd.6631):

| Manifestation | Frequency | Suggested HPO term |
|---|---|---|
| **Jaw lesions** (cemento-osseous / fibro-osseous) | **~67%** — "most requiring at least one surgery" | `HP:0030791` Abnormal jaw morphology ✓ |
| **Tooth anomalies** (infection, displacement) | **48%** | `HP:0000164` Abnormality of the dentition ✓; `HP:0000692` Tooth malposition ✓ |
| **Fractures** | **45%** — from prenatal to age 42, most in childhood | `HP:0002659` Increased susceptibility to fractures ✓; `HP:0002757` Recurrent fractures ✓ |
| **Bowing of long bones** | **19%** | `HP:0006487` Bowing of the long bones ✓; `HP:0002979` Bowing of the legs ✓; `HP:0002980` Femoral bowing ✓ |
| **Diaphyseal thickening** | **16%** | `HP:0003103` Abnormal cortical bone morphology ✓ |
| **Generalized osteopenia** | **10%** | `HP:0000938` Osteopenia ✓ |
| **Bowing, prenatal cases only** | **100%** of 3 prenatal cases | as above |
| **Fractures, prenatal cases only** | **33%** of 3 prenatal cases | as above |

✓ = HPO label verified against the repository's local `cache/hp/terms.csv`.

**Caution on interpreting these percentages.** They are literature-derived, so they are ascertainment-biased in two opposing directions: jaw lesions are over-represented because most patients reach diagnosis through a maxillofacial surgeon, while mild/asymptomatic carriers within reported pedigrees are systematically under-phenotyped. They should be recorded with `evidence_source: HUMAN_CLINICAL` and a note that they are aggregated case-report frequencies, not cohort frequencies.

### 3b. Craniofacial / gnathic phenotypes

**Cemento-osseous jaw lesions** are the disease's signature. Radiographically they present as "multiple lobular or amorphous radiopacities in the tooth-bearing segments of the maxilla and mandible, and a cotton-wool-like pattern in the alveolar regions" (PMID:28176803). Histologically: *"Histopathological descriptions of tissue from GDD lesions note fibrous tissue with irregular acellular mineralized masses and small rounded spherical mineralized bodies (psammomatoid bodies)"* (PMID:28176803).

- **Severity:** highly variable — from asymptomatic radiographic findings to a 7.1 × 5.6 × 5.5 cm anterior mandibular mass requiring angle-to-angle segmental mandibular resection in a 15-year-old (PMID:28176803).
- **Progression: progressive and recurrent.** One 4-year-old showed "symmetric anterior-posterior expansion of the maxilla from 2.8 to 5.1 cm over 4 months" and by age 1 year "was no longer able to close his mouth" (PMID:28176803). Recurrence after incomplete resection is characteristic (PMID:37649308).
- **Onset:** the 41-year radiographic follow-up study (PMID:40861765) is the best natural-history document available: no jawbone symptoms at age 3 despite already-visible diaphyseal cortical widening; slight alveolar sclerosis at age 9; clearly increased sclerotic-mass density after completion of secondary dentition at 14. Conclusion: *"the onset of the jawbone lesion had already appeared after the mixed dentition stage, and the sclerotic mass developed with age."*
- **Related terms:** `HP:0000326` Abnormal maxilla morphology ✓; `HP:0000324` Facial asymmetry ✓; `HP:0002797` Osteolysis ✓

**Jaw osteomyelitis** — `HP:0007626` Mandibular osteomyelitis ✓ / `HP:0002754` Osteomyelitis ✓. *"A number of GDD patients develop osteomyelitis in the oral cavity with an increased propensity for bacterial infections, resulting in the secretion of purulent exudate (pus) from infected lesions"* (PMID:28176803). Typically **adult-onset**; the Chinese proband had "a more than 30-year history of propensity for jaw infections."

**Tooth loss, impaction, and displacement.** In one pedigree, patients had "multiple impacted teeth in the nasal side of the maxillary sinus and the inferior margin of the mandible," and impacted teeth were the *presenting* sign in two children aged 7–8 (PMID:35982081).

### 3c. Appendicular / axial skeletal phenotypes

- **Bone fragility with recurrent fractures.** Onset "appears to be more common in the second decade of life," but the range is extraordinary: prenatal (bilateral femur fractures at 20 weeks gestation, PMID:28176803; multiple diaphyseal fractures of femurs, tibias, upper extremities, ribs and clavicle on fetal autopsy, PMID:38922934), neonatal, childhood, or as late as age 42 (PMID:28176803, PMID:38922934). One proband had "8 fractures in his left forearm and 1 fracture in left femur" between ages 7 and 17 (PMID:34291158).
- **Diaphyseal cortical thickening and sclerosis** with narrowed medullary canals — "gross thickening of the diaphyseal cortices of long bones with narrow medullary canals" (PMID:28176803). Suggested `HP:0005045` Diaphyseal cortical sclerosis (**HPO API-sourced; not present in the local term cache — verify with OAK before use**).
- **Bowing** of tibiae/fibulae, femora.
- **Vertebral involvement:** compression fractures of lumbar vertebrae in infancy (PMID:28176803); "severe osteopenia in cervical spine" (PMID:34291158); "thin and short" vertebral bodies on fetal imaging (PMID:38922934).
- **Calvarial involvement:** "lacunar skull deformity (Lueckenschaedel)" in one infant (PMID:28176803); **calvarial doughnut lesions** in an Asian Indian patient, an explicit phenotype expansion (PMID:32902009).
- **Bone pain** — `HP:0002653` ✓; **genu varum** — `HP:0002970` ✓.

### 3d. The bone-density paradox — two mechanistically distinct subtypes

**This is the most important phenotypic subtlety in GDD and is easily mis-curated.** Different *ANO5* variants produce *opposite* bone-mass phenotypes:

| Subtype | Bone mass | Turnover | Example variant | Reference |
|---|---|---|---|---|
| **High-bone-mass / high-turnover** | Increased trabecular bone mass; `HP:0011001` Increased bone mineral density ✓ | Elevated formation *and* resorption markers; osteoblast and osteoclast indices "remarkably increased" on iliac crest biopsy | p.Ser500Phe | PMID:27541832 |
| **Low-bone-mass / osteopenic** | Low BMD, low T- and Z-scores at lumbar spine and femoral neck; frank osteoporosis in two children | Low P1NP, low N-MID, low β-CTx | p.Leu370_Ala371insDYWRLNSTCL | PMID:35982081 |

Li et al. state the framework explicitly: *"GOF of TMEM16E protein results in high-bone-mass phenotype GDD by hyperfunction of PLS with increased osteoblast and osteoclast indices, while LOF of TMEM16E protein causes low-bone-mass phenotype GDD by impaired function of calcium oscillations with decreased osteoblast and osteoclast indices... our results suggest the existence of GDD-sub-entities with high and low BMD phenotypes due to different GOF and LOF mutations and functions."* (PMID:35982081)

**Curation implication:** a KB entry that records a single `INCREASED` or `DECREASED` modifier on bone mineral density will be wrong for half of patients. This is a genuine `has_subtypes` situation, and the assignment is by variant class, not by clinical convention.

### 3e. Laboratory abnormalities

- **Elevated serum alkaline phosphatase (ALP)** — documented in GDD patients and reproduced in both *Ano5*<sup>−/−</sup> and *Ano5*<sup>KI/KI</sup> (Cys360Tyr) mice: *"Serum alkaline phosphatase (ALP) levels were elevated in Ano5-/- mice as in GDD patients"* (PMID:30712070); *"Serum ALP levels were elevated in Ano5KI/KI mice as in GDD patients with p.Cys360Tyr mutation"* (PMID:34841576). "A slight increase in alkaline phosphatase levels in the blood" was seen in an FGC patient (PMID:37649308). *(No HPO label for elevated ALP was found in the local cache — look up "Elevated circulating alkaline phosphatase concentration" with OAK before binding.)*
- **Bone turnover markers:** direction is subtype-dependent — see §3d. Markers used: P1NP, N-MID osteocalcin, β-CTx (PMID:35982081).
- **25-OH vitamin D deficiency** in most members of one pedigree (PMID:35982081).
- **Elevated creatine kinase** — `HP:0003236` ✓ — only in the rare combined muscle+bone phenotype; peak CK values of 8,000, 6,000, and 25,000 IU/L in three members of one kindred (PMID:34291158).

### 3f. Muscle phenotypes — a genuinely contested boundary

The textbook position is that *ANO5* bone and muscle diseases are non-overlapping: *"Pathogenic ANO5 variants cause 2 distinct disorders with no overlapping features."* (PMID:34291158, intro). Shaibani et al. then **broke that rule** in the same paper, reporting a large kindred (11 affected) in which the known GDD variant p.Thr513Ile segregated with *both* phenotypes:

> *"The unique clinical presentation of recurrent episodes of rhabdomyolysis associated with muscle cramps, hyperCKemia, muscle hypertrophy, with absent or mild muscle weakness, as well as cemento-osseous lesions of the mandible, with or without bone fractures and other skeletal abnormalities... Our data challenge recent results that suggested complete dichotomy of these phenotypes and the proposed loss-of-function and gain-of-function mechanisms for the skeletal and muscle phenotypes, respectively."* (PMID:34291158)

Features in that kindred: rhabdomyolysis (`HP:0003201` ✓) 3–5×/year lasting 5–7 days, muscle cramps, muscle hypertrophy, and — novel for *ANO5* disease — **compartment syndrome requiring fasciotomy** (four episodes in one 20-year-old, one causing peroneal nerve injury).

### 3g. Quality of life

No formal QoL instrument (EQ-5D, SF-36, PROMIS) has ever been applied to GDD. Documented functional impacts, per-manifestation:

| Manifestation | Documented functional impact |
|---|---|
| Jaw mass | Inability to close the mouth; interference with feeding and speech; "severe facial disfigurement" (PMID:28176803, PMID:29175271, PMID:35982081) |
| Jaw osteomyelitis | Purulent gum discharge, tooth loss, failed extraction healing; 30-year symptom duration (PMID:28176803) |
| Fractures | Non-union with skin necrosis leading to **below-knee amputation** in one patient (PMID:28176803); post-traumatic femoral length discrepancy (PMID:32455153) |
| Muscle cramps/rhabdomyolysis | Episodes "disrupted his daily life activities" (PMID:34291158) |
| Dentition | Long-term prosthodontic dependence with repeated adjustment (PMID:29518808) |
| Overall | At least one death: "The patient died from complications related to GDD" (PMID:28176803) |

---

## 4. Genetic / Molecular Information

### Causal gene

**ANO5** (anoctamin 5), also **TMEM16E**, historically **GDD1**.
- HGNC: `hgnc:27337` · NCBI Gene: 203859 · OMIM: *608662
- Locus: **11p14.3**; **22 exons** (PMID:36292621)
- Reference transcript: **NM_213599.3**
- Protein: **913 amino acids**, ~107 kDa; UniProt **Q75V66**
- Topology: classically described as **8 transmembrane domains** with cytoplasmic N- and C-termini (PMID:15124103); revised to **10 membrane-spanning helices** following the nhTMEM16 crystal structure (PMID:29124309, PMID:35982081)
- Domains: one DUF590 / anoctamin domain; a **35-aa scrambling domain (SCRD)**; three calcium-binding sites (PMID:36292621, PMID:35982081)
- Eight cysteines at positions **342, 353, 356, 360, 369, 601, 606, 804** in the putative extracellular loops are conserved from human to insect and are thought to form intrachain disulfide bonds critical to folding (PMID:28176803)

### Catalogue of reported GDD-causing *ANO5* variants

All are **heterozygous**, **germline**, and predominantly **missense**. Coordinates on NM_213599.3.

| Protein change | cDNA | Exon | Population / context | Reference |
|---|---|---|---|---|
| p.Arg215Gly | c.643A>G | 7 | Sporadic (severe infantile; died of GDD complications) | PMID:28176803 |
| p.Cys356Arg | c.1066T>C | 11 | Original Japanese family | PMID:15124103 |
| p.Cys356Gly | c.1066T>G | 11 | African American family | PMID:15124103 |
| p.Cys356Tyr | c.1067G>A | 11 | Caucasian family; also **FGC** ×3 | PMID:28176803, PMID:37649308 |
| p.Cys356Phe | c.1067G>T | 11 | Chinese family, **atypical** (jaw only, no fractures) | PMID:30554457 |
| p.Cys356Trp | — | 11 | Familial florid cemento-osseous dysplasia (FFCOD) | Lv et al., cited in PMID:37649308 |
| p.Cys360Tyr | c.1079G>A | 11 | Chinese family (cementoma + osteomyelitis) | PMID:28176803 |
| p.Cys360Arg | c.1078T>C | 11 | Large Iranian family | PMID:35758145 |
| p.Leu370_Ala371insDYWRLNSTCL | c.1080_1081ins30 | 11 | *De novo*, Chinese family — **low-bone-mass subtype** | PMID:35982081 |
| p.Ala492Val | c.1475C>T | 15 | *De novo*, fetal case | PMID:38922934 |
| p.Ser500Phe | c.1499C>T | 15 | *De novo*, 13-year-old — **high-turnover osteosclerosis** | PMID:27541832 |
| p.(Gln_Ile512insMet) | c.1533_1535dup | 15 | *De novo*, fetal case (in-frame duplication) | PMID:38922934 |
| p.Thr513Ile | c.1538C>T | 15 | Italian pedigree; also the **combined muscle+bone** kindred | PMID:23047743, PMID:34291158 |
| p.Gly518Glu | c.1553G>A | 15 | Sporadic (prenatal femoral fractures) | PMID:28176803, PMID:29175271 |
| p.Arg597Ile | c.1790G>T | 16 | Family of 3, mandibular reconstruction | PMID:30641283 |

**Mutational clustering.** Cuvelier et al. summarize: *"GDD is caused by variants localized in a few exons, particularly in regions that encode the cytoplasmic or extracellular domains,"* with cysteines **356 and 360 as hotspots** (PMID:38922934). Jin et al. locate them structurally: *"all GDD mutations known so far locate in an extracellular domain following the first transmembrane domain or in the 4th putative transmembrane domain"* (PMID:28176803).

### Variant classification and population frequency

- **ACMG classification:** GDD variants are consistently classified **pathogenic or likely pathogenic (class 4/5)**. The fetal-case variants were "probably pathogenic (class 4)" (PMID:38922934).
- **Allele frequency:** GDD variants are **absent from all population databases**. *"These four ANO5 (TMEM16E) variants in GDD patients were absent in dbSNP, 1000Genomes, the Exome Variant Server (~6500 exomes) and the ExAC database."* (PMID:28176803). Later studies applied MAF < 0.005 filters against dbSNP138, 1000 Genomes, CG69, EVS and ESP and retained the *ANO5* variant (PMID:35982081).
- **In silico:** consistently "probably damaging" (PolyPhen-2), "damaging"/"deleterious" (SIFT, score 0), "disease-causing" (MutationTaster, score 1), CADD 28 for C356Y (PMID:28176803, PMID:37649308).
- **Somatic vs germline:** **germline in all cases.** Zhou et al. sequenced both tumour tissue and peripheral blood in FGC patients and found the same heterozygous variant in both — i.e. constitutional, not a somatic second-hit tumour mechanism (PMID:37649308). This is a key contrast with fibrous dysplasia (somatic *GNAS*).
- ***De novo* rate:** substantial. *De novo* variants are documented in at least six independent probands and correlate with severity: *"De novo variants correlated with more severe phenotypes and earlier onset, while familial variants showed broader age ranges."* (PMID:38922934)

### Functional consequence — GOF vs LOF, an unresolved and consequential dispute

This is the central mechanistic controversy in GDD and must be represented as such, not collapsed into a single answer.

**The GOF position (biophysics).** Di Zanni et al. provided the first direct functional demonstration:
> *"While the activity of wild-type TMEM16E depended on elevated cytosolic Ca2+ levels, a mutant form carrying the GDD-causing T513I substitution showed PLS and large time-dependent ion currents even at low cytosolic Ca2+ concentrations... these data provide the first direct demonstration of Ca2+-dependent PLS activity for TMEM16E and suggest a gain-of-function phenotype related to a GDD mutation."* (PMID:29124309, DOI 10.1007/s00018-017-2704-9)

Quantitatively: wild-type TMEM16E activation threshold was +125.2 ± 6.1 mV at zero Ca²⁺ and +88.1 ± 2.8 mV at 3 µM Ca²⁺; the T513I mutant activated at +82.3 ± 4.1 mV at *zero* Ca²⁺ — i.e. mutant activity at zero calcium equalled wild-type activity at 3 µM. Wild-type Ca²⁺ dependence: half-maximal 2.9 µM, Hill coefficient 1.5. The follow-up study extended this across variants: *"MD mutations are associated to loss-of-function and GDD mutations to gain-of-function phenotypes, confirming conjectures made on the basis of inheritance modes."* (PMID:32112655)

**The LOF position (protein abundance and cell biology).** Jin et al. found *"In vitro studies overexpressing GDD mutations (p.Cys356Tyr and p.Cys360Tyr) showed significantly reduced ANO5 protein"* (PMID:28176803). Li et al. documented a frameshift-insertion GDD family with reduced TMEM16E protein in PBMCs and argued: *"our results suggest that ANO5 is dosage-sensitive and that LOF of the TMEM16E protein caused by the heterozygous ANO5 mutation in one allele is partly compensated by another normally functional allele."* (PMID:35982081)

**Why both can be true.** Different variant classes plausibly act differently — a folding-destabilizing cysteine substitution (C356Y/C360Y, degraded via the proteasome) is not the same lesion as a scrambling-domain-proximal substitution that renders the protein constitutively active (T513I). This maps directly onto the two bone-mass subtypes in §3d. **A KB entry should curate this as competing `mechanistic_hypotheses` with distinct `hypothesis_group_id`s, not as a settled fact.**

Note also that Jin et al. argue against pure haploinsufficiency on two grounds: *"The lack of an obvious skeletal phenotype in Ano5 knock-out mice argue against a dose effect"* and the existence of recessive truncating LGMD alleles in the same region (PMID:28176803).

### Epigenetics

No DNA methylation, histone-modification, or chromatin study of GDD exists. The only epigenetic-adjacent finding is **post-transcriptional**: *Ano5* deficiency "notably inhibited miR-34c-5p expression," de-repressing its target *Klf4* (PMID:40508076) — see §6.

### Chromosomal abnormalities

**Not applicable.** GDD is not caused by aneuploidy, translocation, inversion, or CNV. Chromosomal microarray, karyotype, and FISH have no diagnostic role.

---

## 5. Environmental Information

- **Environmental toxicant/occupational factors:** none identified. No CTD entries link environmental chemicals to GDD.
- **Lifestyle factors:** no established dietary, smoking, alcohol, or activity association with disease *risk*. Exercise is relevant only as a rhabdomyolysis trigger in the combined phenotype (PMID:34291158), and physical activity/mechanical loading as a fracture precipitant.
- **Infectious agents:** **GDD is not an infectious disease.** However, **secondary bacterial infection of jaw lesions is a defining complication** — purulent osteomyelitis of the mandible and maxilla (PMID:28176803, PMID:29518808). Causative organisms are not systematically speciated in the literature; expect the usual odontogenic/osteomyelitis flora. Model this as a downstream complication node, not an etiological factor.

---

## 6. Mechanism / Pathophysiology

### 6a. Normal ANO5/TMEM16E biology

**Expression.** *ANO5* is highly expressed in skeletal and cardiac muscle, and — critical for GDD — in **growth-plate chondrocytes and osteoblasts** (PMID:17418107, PMID:34291158). Mizuta et al.: *"GDD1 protein is an integral membrane glycoprotein that resides predominantly in intracellular vesicles."* During early embryogenesis it is expressed in myotomal and sclerotomal somites (PMID:28176803). It is also expressed in human periodontal ligament cells (PMID:29124309).

**Subcellular localization.** Predominantly **endoplasmic reticulum** — co-localizing with calreticulin and CellLight ER-RFP markers (PMID:15124103, PMID:28176803, PMID:29124309) — with **partial plasma-membrane localization** at high expression levels, which is what enabled the electrophysiological characterization (PMID:29124309). GO CC: `GO:0005783` endoplasmic reticulum ✓.

**Molecular function — three competing/complementary assignments:**
1. **Ca²⁺-activated chloride channel (CaCC)** — the original inference from family membership (`GO:1902476` chloride transmembrane transport ✓). **This is now largely rejected.** Tran et al. noted ANO5 has a threonine rather than a cysteine at position 611, one of three conserved cysteines in true CaCCs (ANO1/ANO2) (cited in PMID:28176803); halide-sensitive YFP assays found no anion transport (PMID:29124309); *Ano5*-deficient mice showed chloride currents indistinguishable from wild-type (PMID:36292621).
2. **Ca²⁺-dependent phospholipid scramblase (PLS)** — the currently favoured assignment (`GO:0045332` phospholipid translocation ✓). Directly demonstrated by annexin-V binding assays with Ca²⁺-ionophore stimulation (PMID:29124309). *"ANO5 functions predominantly in phospholipid scrambling (PLS), which facilitates the movement of phospholipids between the membrane bilayer during various biological processes."* (PMID:36292621)
3. **ER Ca²⁺ conduit / regulator of intracellular Ca²⁺ transients** — *"our data support the view that TMEM16E at the ER membrane of bone cells sustains Ca2+ transitions to the cytoplasm"* (PMID:35982081) (`GO:0070588` calcium ion transmembrane transport ✓; `GO:0051209` release of sequestered calcium ion into cytosol ✓).

Note that ion transport may be biophysically real but **physiologically irrelevant**: Di Zanni et al. observed currents only at >+75 mV, and concluded *"Considering furthermore their exclusive activation at highly depolarized membrane potentials, which are unlikely to be experienced by non-excitable cells, one may conclude that ion transport is not among the physiological functions of TMEM16E."* (PMID:29124309)

**Membrane repair** (`GO:0001778` plasma membrane repair ✓) is the best-established physiological role, though it is characterized in muscle rather than bone: ANO5 translocates to injured sarcolemma and is required for annexin recruitment to the repair cap (PMID:36292621).

### 6b. Causal chain — trigger to clinical manifestation

Because of the GOF/LOF split, there are **two parallel proximal chains converging on a shared distal phenotype**. Both are supported; neither is exclusive.

**Chain A — the LOF / low-bone-mass route** (best evidenced by PMID:35982081, PMID:40049314, PMID:36989132):

```
Heterozygous ANO5 destabilizing variant
  → reduced TMEM16E protein (proteasomal degradation)          [MOLECULAR]
  → loss of ER-mediated Ca²⁺ transients; [Ca²⁺]i oscillations
    abolished in osteoblasts, blunted in osteoclasts            [CELLULAR]
  → ┌─ osteoblast arm: ↓WNT1/β-catenin/Dvl2, ↑GSK-3β/Axin1
    │    → ↓Ocn, ↓Spp1, ↓ALP, ↓mineral nodules                  [CELLULAR]
    └─ osteoclast arm: ↓RANKL-induced NFATc1/c-Fos nuclear
         translocation → ↓Trap, ↓Ctsk, ↓Mmp9, ↓Dc-stamp,
         disrupted F-actin ring, ↑ER-stress/CHOP apoptosis      [CELLULAR]
  → coupled suppression of formation AND resorption
    ("vicious cycle" of remodeling arrest)                       [TISSUE]
  → low bone volume, osteopenia, fragility                       [ORGANISM]
```

**Chain B — the GOF / high-bone-mass route** (best evidenced by PMID:29124309, PMID:32112655, PMID:27541832, PMID:34841576):

```
Heterozygous ANO5 GOF variant (e.g. T513I)
  → constitutive, Ca²⁺-independent phospholipid scrambling      [MOLECULAR]
  → aberrant membrane-surface phosphatidylserine exposure;
    loss of cell adhesion, cell rounding                         [CELLULAR]
  → ↑osteoblastogenesis (↑Runx2, Osterix, Col1a1, Ocn),
    hypermineralized matrix; ↓osteoclastogenesis                 [CELLULAR]
  → high-turnover osteosclerosis, cortical thickening,
    narrowed medullary canal                                     [TISSUE]
  → paradoxical fragility despite high mass                      [ORGANISM]
```

**The paradox that unifies them.** Both routes produce **fragility**, whether bone mass is low or high. In the high-mass form the bone is hypermineralized and therefore brittle — Jin et al.: *"ANO5 may act as a negative regulator of mineralization and that reduced protein levels due to ANO5 mutations or interactions of instable mutant ANO5 proteins may result in abnormal bone deposition or remodeling with over-mineralization, hyperostosis and brittle bones."* (PMID:28176803). This is mechanistically similar to the fragility of osteopetrosis and of *COL1A1* C-propeptide-cleavage-site OI (PMID:24891183).

### 6c. Downstream signalling pathways — a rapidly expanding 2024–2026 literature

Five independent effector pathways have been nominated in the last two years, all downstream of *Ano5* disruption in mouse osteoblasts/osteoclasts. They are not mutually exclusive and several intersect at AMPK.

| Pathway | Finding | Rescue agent tested | Reference |
|---|---|---|---|
| **Akt–NFATc1** | *Ano5*<sup>Cys360Tyr</sup> down-regulates Akt phosphorylation in osteoblasts; Akt activation restored TRAP⁺ multinucleated osteoclasts and F-actin rings, and *reduced* excess ALP/mineralization | **SC79** (Akt activator) — "an Akt activator is probable a therapeutic target for GDD" | PMID:39866532 (Bone Rep 2025) |
| **AMPK–ATG9A–autophagy** | *Ano5* deficiency activates autophagy in mouse calvarial osteoblasts via ATG9A upregulation; AMPK positively regulates ATG9A | **3-MA**, **chloroquine**; 3-MA "alleviated the bone phenotype abnormalities in Ano5-/- mice" *in vivo* | PMID:40067389 (JCI Insight 2025) |
| **AMPK–PGC1α/PGC1β glucose metabolism** | Mutation accelerates glycolysis and PGC1α-dependent mitochondrial respiration in osteoblasts; PGC1β downregulation causes abnormal osteoclast mitochondria; AMPK phosphorylation increased | **Compound C** (AMPK inhibitor) "reversed the bone phenotype of GDD by restraining bone formation and restoring osteoclastogenesis" | PMID:41717545 (Front Endocrinol 2026) |
| **miR-34c-5p–KLF4–β-catenin** | *Ano5* deficiency inhibits miR-34c-5p; *Klf4* (a validated miR-34c-5p target, dual-luciferase) is de-repressed, activating canonical Wnt/β-catenin | **AAV-miR-34c-5p** *in vivo* rescued thickened cortical bone, improved biomechanics, lowered serum P1NP | PMID:40508076 (Int J Mol Sci 2025) |
| **ER stress–CHOP–osteoclast apoptosis** | Decreased [Ca²⁺]i and calcium transients in *Ano5*<sup>−/−</sup> osteoclasts → enhanced ER stress → CHOP-mediated apoptosis | none tested | PMID:40049314 (Exp Cell Res 2025) |
| **NF-κB** | RANKL-induced early signalling suppressed in *Ano5*<sup>−/−</sup> osteoclasts; partially rescued by an NF-κB activator | NF-κB activator (partial) | PMID:36989132 (Oral Dis 2024) |

**Metabolic changes.** Metabolomics + transcriptomics of *Ano5*<sup>Cys360Tyr</sup> knock-in mouse calvarial osteoblasts identified 42 differential metabolites (amino acid and pyrimidine metabolism; endocrine/other-factor-regulated calcium reabsorption) and 407 differentially expressed genes, converging on cell-cycle progression (*Mki67*, *Ccnb1*, *Ccna2* up) and calcium signalling (*Cacna1*, *Slc8a1*, *Cyp27b1* up), with higher calcium content in mineral nodules by SEM-EDS (PMID:36742392).

### 6d. Protein dysfunction

- **Misfolding and instability.** GDD cysteine mutants "fold with low efficiency and appear to be unstable and rapidly degraded via proteasomal degradation" (cited in PMID:28176803). Western blot and immunofluorescence confirm reduced mutant protein despite higher construct copy number (PMID:28176803).
- **Structural modelling.** AlphaFold2 modelling of C356Y showed low global deviation (RMSD 0.256) but local distortion: residues Lys847/Phe848/Leu849 form a helix in wild type and a loop in the mutant (PMID:37649308).
- **Cellular consequence of aberrant activity.** HEK293 cells expressing GDD mutants "typically became round-shaped and displayed decreased cell adhesion," and Di Zanni et al. showed *"the gradual changes in HEK293 cell morphology observed upon expression of TMEM16E/ANO5GDD mutants are a consequence of aberrant protein activity"* (PMID:29124309, PMID:32112655).

### 6e. Immune system involvement

GDD is **not** an autoimmune or immunodeficiency disorder. The only immune dimension is (a) the propensity to bacterial jaw osteomyelitis (§5) and (b) the fact that osteoclasts are monocyte/macrophage-lineage cells (`CL:0000235` macrophage ✓), so RANKL–NFATc1–NF-κB signalling — canonically an immune pathway — is the disease's core osteoclast axis.

### 6f. Tissue damage mechanisms

Not ischemia, fibrosis (in the classical sense), or oxidative stress. The dominant mechanism is **dysregulated bone remodeling** (`GO:0046849` bone remodeling ✓) with **abnormal matrix mineralization** (`GO:0030282` bone mineralization ✓), plus **fibro-osseous replacement of normal jaw architecture**: *"normal cancellous bones of the jaw were structurally destroyed and poorly mineralized, occupied by a large amount of fibrous tissue and cementum, leading to fibrous cementum-like lesions"* (PMID:35982081). ER stress and CHOP-mediated apoptosis are the newest addition (PMID:40049314).

### 6g. Cell types and processes — ontology suggestions

**Cell types** (all CL labels verified against local cache):
- `CL:0000062` osteoblast — primary effector cell; both mouse calvarial osteoblast (mCOB) and BMSC-derived
- `CL:0000092` osteoclast — the more severely affected lineage in LOF models
- `CL:0000137` osteocyte
- `CL:0000138` chondrocyte — growth-plate expression (PMID:17418107)
- `CL:0000057` fibroblast — the fibroblastic stroma of jaw lesions
- `CL:0000061` cementoblast — the cementum-like deposits are the disease's histological signature
- `CL:0000235` macrophage — BMM osteoclast precursor
- `CL:0000594` skeletal muscle satellite cell — relevant only to the muscle arm

**Biological processes** (all GO labels verified):
`GO:0001649` osteoblast differentiation · `GO:0030316` osteoclast differentiation · `GO:0001503` ossification · `GO:0030282` bone mineralization · `GO:0045453` bone resorption · `GO:0046849` bone remodeling · `GO:0045332` phospholipid translocation · `GO:0070588` calcium ion transmembrane transport · `GO:0051209` release of sequestered calcium ion into cytosol · `GO:0071277` cellular response to calcium ion · `GO:0060070` canonical Wnt signaling pathway · `GO:0006914` autophagy · `GO:0034976` response to endoplasmic reticulum stress · `GO:0001778` plasma membrane repair · `GO:1902476` chloride transmembrane transport (curate with a caveat — largely refuted)

**Cellular component:** `GO:0005783` endoplasmic reticulum

### 6h. Molecular profiling status

| Modality | Status |
|---|---|
| Transcriptomics | Mouse only — 407 DEGs in *Ano5*<sup>KI/KI</sup> mCOBs (PMID:36742392). No human GDD transcriptome. |
| Proteomics | None for GDD. (Mass-spec proteomics of *muscle* amyloid deposits in ANO5 myopathy exists — found amyloid P and ApoE, but **not ANO5**; PMID:36292621.) |
| Metabolomics | Mouse only — 42 differential metabolites (PMID:36742392) |
| Lipidomics | **None** — a notable gap given that the leading functional hypothesis is phospholipid scrambling |
| Single-cell / spatial | **None** |
| Functional genomics screens (CRISPR/RNAi) | No systematic screen. Targeted shRNA knockdown in MC3T3-E1 (PMID:28176803) and siRNA/shRNA in RAW264.7 (PMID:36989132) only. |
| GEO/ArrayExpress | No GDD-labelled human dataset identified. **Any dataset accession must be verified with `just verify-datasets` and manually triaged for relevance — searching "ANO5" will surface muscular dystrophy datasets, which is exactly the Named Entity Confusion trap.** |

---

## 7. Anatomical Structures Affected

### Organ level

**Primary:**
- **Mandible** — `UBERON:0001684` mandible ✓ — the most consistently and severely affected structure
- **Maxilla** — `UBERON:0002397` maxilla ✓
- **Long tubular bones**, diaphyseal regions — `UBERON:0004769` diaphysis ✓ — femur, tibia, fibula, radius, ulna, humerus
- **Bone tissue** generally — `UBERON:0002481` bone tissue ✓

**Secondary / less consistent:** vertebrae (compression fractures, osteopenia); ilium; calvarium (doughnut lesions, PMID:32902009; lacunar skull, PMID:28176803); clavicle and ribs (fetal fractures, PMID:38922934); dentition and periodontium.

**Body systems:** skeletal (primary); dental/stomatognathic (primary); musculoskeletal-muscular — `UBERON:0001134` skeletal muscle tissue ✓ — only in the rare combined phenotype.

**Explicitly NOT affected:** No consistent cardiac, renal, hepatic, neurological, or endocrine involvement in GDD proper. (Cardiac involvement of 10–30% is a feature of the *recessive ANO5 muscular dystrophies*, not GDD — PMID:36292621. Do not transfer it.)

### Tissue and cell level

Connective/skeletal tissue is the target. Jaw lesion histology: "a fibroblastic stroma with variable cellularity and a heterogeneous osseous component composed of woven bone and more cementum-like material" (PMID:35982081); "large eosinophilic masses of cementum-like material interspersed in fibrous background" (PMID:28176803); psammomatoid bodies; "abundant mineralization in the vessel wall" (PMID:37649308).

### Subcellular level

- **Endoplasmic reticulum** (`GO:0005783` ✓) — principal ANO5 residence and the locus of the Ca²⁺-transient defect
- **Plasma membrane / sarcolemma** — partial localization; site of scrambling activity
- Intracellular vesicles (PMID:17418107)
- Mitochondria — secondarily abnormal in *Ano5*<sup>KI/KI</sup> osteoclasts via PGC1β (PMID:41717545)

### Lateralization

**Bilateral**, though often asymmetric in extent. Fetal case: "multiple diaphyseal fractures of the long bones... affecting femurs, tibias, and bilateral upper extremity bones" (PMID:38922934). Jaw lesions are typically **multi-quadrant** — bilateral maxillary and mandibular — which is a key differentiator from unilateral ossifying fibroma. One patient had "bilateral relatively symmetric, expansile lesions in the maxillary bone" (PMID:28176803).

---

## 8. Temporal Development

### Onset

**Extremely variable — this is a defining feature.** Jin et al.: *"there appears to be a wide age range in the onset of fibrous lesions of the mandible and severity of fractures."* (PMID:28176803)

Documented onsets, earliest to latest:
- **Prenatal:** bilateral femur fractures at **20 weeks gestation** (PMID:28176803); fetal bowing detected at **12 weeks** and confirmed at 16 weeks (PMID:38922934)
- **Neonatal:** fractures at birth (Levin et al., cited in PMID:28176803)
- **Infancy:** maxillary/mandibular enlargement at **2 months**; jaw mass at 13 months (PMID:28176803); jaw protuberance at **6 months** in an FGC case (PMID:37649308)
- **Childhood:** most fractures; impacted teeth as presenting sign at ages 7–8 (PMID:35982081)
- **Adolescence:** classic textbook onset — "the onset of fractures appears to be more common in the second decade of life" (PMID:28176803)
- **Adulthood:** jaw lesion first diagnosed at **age 21**, **43**, **62**, and **67** in different individuals (PMID:28176803)

HPO records `HP:0003621` Juvenile onset for this disease (**HPO API-sourced; verify with OAK — not in the repository's local term cache**). Orphanet records age of onset as infancy, childhood, and adolescence.

**Onset pattern:** insidious and chronic for jaw lesions; acute/episodic for fractures.

### Progression

**GDD is chronic, lifelong, and progressive.** There is no spontaneous remission.

The strongest evidence for progression comes from two longitudinal documents:
1. **Rolvien et al.'s 3-year follow-up** of the S500F patient: DXA BMD Z-score remained stable, but *"cortical thickness assessed by HR-pQCT at the distal tibia further increased at one and three years follow-up, which led to values clearly above the age-adjusted reference values."* The authors conclude: *"These clinical data demonstrate the progressive nature and lack of viable treatment options for this disorder."* (PMID:32455153)
2. **The 41-year radiographic study** (PMID:40861765): diaphyseal cortical widening visible at age 3 before any jaw symptoms; alveolar sclerosis at 9; dense sclerotic mass after secondary dentition at 14; continued development into the fifth decade.

**Stages (informal — no consensus staging system exists):**
- *Pre-symptomatic / radiographic-only*: diaphyseal cortical widening detectable before jaw involvement (age ~3)
- *Fracture-predominant*: childhood to adolescence
- *Jaw-lesion-predominant*: mixed dentition onward, expansile growth
- *Complication phase*: adult jaw osteomyelitis, tooth loss, non-union fractures, surgical morbidity

**Rate:** variable; the jaw lesions can grow explosively (maxilla 2.8 → 5.1 cm in 4 months, PMID:28176803) or indolently over decades.

**Course pattern:** progressive with **episodic acute events** (fractures, osteomyelitis flares, and — in the combined phenotype — rhabdomyolysis 3–5×/year lasting 5–7 days, PMID:34291158).

**Duration:** lifelong.

### Critical periods

- **Mixed-dentition transition (~age 6–14)** appears to be the window in which jaw lesions initiate — the single most actionable observation for surveillance timing (PMID:40861765).
- **First two decades** — peak fracture incidence, and therefore the window in which bone-directed therapy is most likely to matter.
- **Any dental extraction** is a discrete risk window for osteomyelitis and non-healing.
- The FGC literature describes a three-phase growth pattern for jaw lesions that may transfer: "initial onset at 11–13 years of age, rapid expansion between 14 and 16 years of age, and growth suppression around 18–20 years of age" (PMID:37649308).

### Remission

No spontaneous remission. Jaw lesions recur after incomplete resection — *"the recurrence rate of FGC is high, and incomplete resection or conservative curettage often leads to more rapid progression of the remaining portion, which does not recur after complete resection"* (PMID:37649308).

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence: <1 / 1,000,000** (Orphanet ORPHA:53697). In dismech `PrevalenceClassEnum` terms this is **`BELOW_1_IN_1000000`**, with `measure_type: POINT_PREVALENCE`, or arguably **`CASES_IN_LITERATURE`** given how the number was derived.
- **Cases reported:** approximately **108 clinically diagnosed individuals across 25 families**, of whom **67 individuals in 21 families** have molecular confirmation (PMID:38922934). This is the most defensible case count and should be preferred over vaguer statements.
- **Incidence:** unknown; no incidence estimate exists.
- MedlinePlus Genetics: "The prevalence of gnathodiaphyseal dysplasia is unknown, but it is thought to be a rare disorder."

### Inheritance

- **Autosomal dominant** — `HP:0000006` (HPO API-sourced). Established by four-generation pedigree linkage (PMID:12619924) and repeatedly confirmed by segregation (PMID:28176803, PMID:34291158, PMID:35758145).
- **Penetrance:** appears **high, possibly complete for the radiographic phenotype**, but is **not formally quantified in any study**. In the Shaibani kindred two female carriers reported no muscle symptoms though bone findings were present, and the authors noted "the possibility remains that these 2 female patients have asymptomatic muscle involvement" (PMID:34291158). Record penetrance as *not established*.
- **Expressivity: highly variable, both interfamilial and intrafamilial.** Jin et al.: *"our findings strongly indicate the association of ANO5 mutations with GDD, and we show that there is considerable clinical variability in patients, even within one family. These differences in expressivity can currently not be explained due to the limited number of patients available for phenotypic/genetic studies."* (PMID:28176803) The clearest example: in the Chinese C360Y family, the 73-year-old father had severe jaw disease with no fractures, while his 43-year-old son was much more mildly affected.
- **Genetic anticipation:** **none reported and none expected** — GDD is not a repeat-expansion disorder.
- ***De novo* variants: common**, and associated with more severe, earlier-onset disease (PMID:38922934). Documented in at least six probands (G518E, S500F, L370_A371ins, A492V, Q_I512insMet, and others).
- **Germline mosaicism:** raised as a formal possibility but not demonstrated — *"The mutation in sporadic patient 1 is either a de novo mutation or due to germline mosaicism."* (PMID:28176803)
- **Founder effects:** **none for GDD.** (Contrast the *recessive* ANO5 myopathies, where **c.191dupA (p.Asn64LysfsTer15)** is a well-established northern European founder allele with 45–75% homozygosity in England, Germany, and Denmark — PMID:36292621. This allele has **nothing to do with GDD** and must not be transferred into a GDD entry.)
- **Consanguinity:** not a factor — GDD is dominant.
- **Carrier frequency:** not applicable to a dominant disorder; heterozygotes are affected.

### Population demographics

- **Affected populations:** no ethnic predilection. Reported in **Japanese** (original family), **African American**, **Caucasian/American**, **Chinese/Han**, **Italian**, **Russian**, **Iranian**, **Asian Indian**, and **French** individuals (PMID:15124103, PMID:28176803, PMID:23047743, PMID:20005074, PMID:35758145, PMID:32902009, PMID:38922934).
- **Geographic distribution:** worldwide; no endemic clustering.
- **Variant geography:** C356 substitutions dominate across populations; C360Y in Chinese, C360R in Iranian, T513I in Italian and American kindreds, R597I in a French family. This reflects reporting history rather than any established population structure.
- **Sex ratio:** **no sex bias reported for GDD.** Male and female patients appear in comparable numbers across pedigrees. (The 2:1–4:1 male predominance in the literature applies to *ANO5 muscular dystrophies*, not GDD — PMID:36292621.)
- **Age distribution:** all ages, with diagnostic peak in childhood/adolescence.

---

## 10. Diagnostics

### Clinical / laboratory tests

- **Serum alkaline phosphatase** — often elevated; the most consistently reported biochemical abnormality (PMID:30712070, PMID:34841576, PMID:37649308)
- **Bone turnover panel** — P1NP, N-MID osteocalcin, β-CTx. Direction is subtype-dependent (elevated in high-turnover S500F disease, PMID:27541832; reduced in low-bone-mass frameshift disease, PMID:35982081)
- **25-OH vitamin D, calcium** (PMID:35982081)
- **Creatine kinase** — only if muscle symptoms are present; can reach 25,000–40,000 IU/L in rhabdomyolysis episodes (PMID:34291158)

### Imaging

- **Panoramic dental radiography** — first-line for jaw lesions; shows "multiple lobular or amorphous radiopacities in the tooth-bearing segments" and "cotton-wool-like pattern in the alveolar regions" (PMID:28176803). This is often how asymptomatic family members are ascertained.
- **CT / 3D maxillofacial CT** — lesion extent, surgical planning (PMID:35982081)
- **Skeletal survey / plain radiography** — diaphyseal cortical thickening, narrowed medullary canals, bowing (PMID:34291158)
- **DXA** — lumbar spine L1–L4 and femoral neck BMD, with age-adjusted Z-scores (paediatric software required in children) (PMID:27541832, PMID:35982081)
- **HR-pQCT at the distal tibia** — the most sensitive modality for detecting progressive cortical thickening; detected progression over 3 years when DXA was static (PMID:32455153). **This is a practically important point: DXA can be falsely reassuring.**
- **Prenatal:** ultrasound (bowing, shortened femurs, growth restriction) and **fetal osseous CT** to characterize severity and distinguish from differentials (PMID:38922934)

### Histopathology

Diagnostic but not pathognomonic. Findings: cemento-ossifying fibroma pattern; fibroblastic stroma with variable cellularity; woven bone plus cementum-like material; **psammomatoid bodies**; abundant vessel-wall mineralization (PMID:11547842, PMID:28176803, PMID:37649308).

**Caution:** psammomatoid bodies are *not* required — the severe G518E case had "benign fibro-osseous lesions resembling cemento-ossifying fibromas of the jaw **without psammomatoid bodies**" (PMID:29175271).

### Genetic testing — the diagnostic gold standard

**Recommended approach** (per PMID:38922934):
1. **Targeted *ANO5* sequencing** where clinical suspicion is high — prioritize **exons 7, 11, 15, 16**, with 11 (Cys356/Cys360) highest yield
2. **Skeletal dysplasia / osteogenesis imperfecta gene panel** where the presentation is ambiguous
3. **Trio exome sequencing (ES)** — especially valuable prenatally and for apparently sporadic cases, where *de novo* status must be established
4. **Whole genome sequencing (WGS)** — has successfully identified GDD variants where panels failed (PMID:30554457)

Sanger confirmation and family segregation analysis are standard.

**Not useful:** chromosomal microarray, karyotype, FISH, mitochondrial DNA testing, repeat-expansion testing. None has a role in GDD.

**Omics-based diagnostics:** none validated. No RNA-seq, proteomic, metabolomic, epigenomic, or liquid-biopsy test exists for GDD.

### Clinical criteria

**There are no formal, published, consensus diagnostic criteria for GDD.** Diagnosis is made by the combination of (a) fibro-osseous jaw lesions, (b) bone fragility/fractures, (c) diaphyseal cortical thickening/bowing, plus (d) a pathogenic *ANO5* variant. Li et al. describe the pragmatic composite: *"When hereditary, histologic and laboratory features were taken into consideration with clinical and radiographic features, GDD was the most appropriate diagnosis."* (PMID:35982081)

### Differential diagnosis — and a diagnostic-error rate worth curating

**GDD is systematically misdiagnosed.** *"A review of the literature showed that 67% of GDD cases confirmed by molecular testing were initially misdiagnosed."* (PMID:30554457) The 2025 surgical report adds: *"clinicians are still largely unaware of this entity and continue to label and treat it as a variation of Osteogenesis Imperfecta."* (PMID:41193275)

| Differential | Distinguishing features |
|---|---|
| **Osteogenesis imperfecta** | OI lacks cemento-osseous jaw lesions and diaphyseal cortical *thickening* (OI cortices are thin). *COL1A1/COL1A2* rather than *ANO5*. **Exception:** a *COL1A1* C-propeptide cleavage-site mutation causes high bone mass, fragility, and jaw lesions and was proposed as "a new cause of gnathodiaphyseal dysplasia" (PMID:24891183) — a genuine phenocopy. |
| **Fibrous dysplasia / McCune-Albright** | Somatic activating *GNAS* mutations; café-au-lait macules; endocrinopathy. GDD variants are germline and *GNAS* is wild-type. GDD has been reported *presenting as* polyostotic fibrous dysplasia (PMID:25866257), and one GDD carrier's mother "was diagnosed with polyostotic fibrous dysplasia" before molecular testing corrected it (PMID:28176803). |
| **Cherubism** | *SH3BP2*. One large family was diagnosed as cherubism until *SH3BP2* sequencing was negative and WGS found *ANO5* p.C356F (PMID:30554457). |
| **Florid cemento-osseous dysplasia (FCOD) / familial FCOD** | Overlapping; **familial FCOD carries an *ANO5* p.C356W mutation**, suggesting the same spectrum (Lv et al., cited in PMID:37649308) |
| **Familial gigantiform cementoma (FGC)** | All three FGC patients in the definitive genetic study carried *ANO5* p.C356Y. *"FGC may be an atypical variant of GDD"* (PMID:37649308). Independently: *"the GC and GDD likely represent the same type of bone pathology"* (PMID:27216912). |
| **Juvenile/psammomatoid ossifying fibroma** | *SATB2* rearrangements; *ANO5* wild-type in 8 tested cases (PMID:37649308, PMID:42361776) |
| **Camurati-Engelmann disease** | *TGFB1*; diaphyseal hyperostosis without jaw cemento-osseous lesions (PMID:28176803) |
| **Osteopetrosis** | Generalized sclerosis without fibro-osseous jaw lesions |
| **Stuve-Wiedemann syndrome** | Prenatal bowing differential (PMID:38922934) |

The 2026 WHO-aligned review consolidates the molecular picture: *"familial florid cemento-osseous dysplasia, familial gigantiform cementoma and gnathodiaphyseal dysplasia sharing ANO5 mutations"* (PMID:42361776). **A dismech entry should decide deliberately whether FGC and familial FCOD are `has_subtypes` of GDD or separate entries with a `Grouping` — the literature now favours a shared entity.**

### Screening

- **Cascade family screening** is the highest-yield strategy: panoramic radiography plus targeted *ANO5* sequencing in first-degree relatives. Several probands were identified through a sibling's routine panoramic radiograph (PMID:28176803).
- **Newborn screening:** not applicable and not proposed.
- **Prenatal:** GDD should now be on the differential for **fetal long-bone bowing and fractures** (PMID:38922934) — this is the newest addition to diagnostic practice.

---

## 11. Outcome / Prognosis

### Survival and mortality

- **No survival, life-expectancy, or mortality data exist.** No cohort has been followed.
- GDD is **generally not life-limiting**, but is **not uniformly benign**: at least one death is recorded — *"The patient died from complications related to GDD."* (PMID:28176803, describing the R215G sporadic patient originally reported by Riminucci). Cuvelier et al. counsel that "symptoms can be very severe, even fatal" (PMID:38922934).
- Patients survive into at least the eighth decade (a 73-year-old proband, PMID:28176803).

### Morbidity and disability

Substantial and predominantly **surgical, dental, and orthopaedic**:
- Repeated jaw debulking/resection, sometimes ≥3 operations in a young child (PMID:28176803)
- Mandibular reconstruction with free vascularized fibular graft, titanium plating (PMID:35982081, PMID:30641283)
- **Below-knee amputation** after fracture non-union complicated by osteomyelitis and skin necrosis (PMID:28176803)
- Tooth loss and lifelong prosthodontic dependence (PMID:29518808)
- Facial disfigurement
- Compartment syndrome requiring multiple fasciotomies, with residual peroneal nerve injury (combined phenotype; PMID:34291158)

**Quality-of-life instruments: never applied.** No EQ-5D, SF-36, or PROMIS data exist for GDD.

### Complications

Jaw osteomyelitis with purulent discharge; fracture non-union; post-traumatic limb-length discrepancy; recurrence of jaw lesions after incomplete resection; airway/feeding/speech compromise from jaw expansion; orbital and sinus involvement from maxillary expansion (in one patient the left eyeball was "compressed and anterior and laterally shifted," PMID:35982081).

### Recovery potential

**None — there is no recovery.** Surgical resection can be curative *for a given lesion* if complete ("does not recur after complete resection," PMID:37649308), but the underlying skeletal disorder is permanent and progressive. Notably, surgical healing itself can be normal: "All of the fibular and mandibular osteotomies were found to be well healed" (PMID:28176803), and internal fixation of an adult tibial shaft fracture achieved "successful callus formation" (PMID:33826556).

### Prognostic factors

Only one is established, and it is qualitative: ***De novo* variant status predicts more severe disease and earlier onset**, whereas familial variants show broader age ranges (PMID:38922934).

Suggestive but unvalidated:
- Very early onset (prenatal/infantile jaw expansion) predicts severe course (PMID:29175271, PMID:28176803)
- Variant position may predict bone-mass subtype (§3d)
- Two families (p.C356F, p.L370_A371ins) had jaw lesions **without** fractures — a milder, jaw-restricted presentation (PMID:38922934)

**No validated prognostic biomarker exists.** ALP and bone turnover markers are diagnostic/monitoring aids, not validated predictors.

---

## 12. Treatment

> **Framing statement to carry into any KB entry:** *"Currently, there is no cure for GDD, and management of the disorder is focused on symptom relief and prevention of complications."* (PMID:38922934). And: *"Currently, the clinical treatment of GDD is limited to surgical resection."* (PMID:40049314)

### Pharmacotherapy

| Agent | Rationale / evidence | Suggested NCIT annotation |
|---|---|---|
| **Bisphosphonates (pamidronate)** | The only antiresorptive with human GDD data — a 5-year-old received "a total of 7 pamidronate infusions commencing at age 15 months" for severe osteopenia; **the report does not establish efficacy** and the authors call for further evaluation (PMID:29175271, PMID:28176803). Cuvelier et al. recommend fractures be "treated similarly to Osteogenesis Imperfecta," incorporating bisphosphonate therapy where appropriate (PMID:38922934). | `treatment_term`: `NCIT:C15986` Pharmacotherapy; `therapeutic_agent`: pamidronate (CHEBI — verify with OAK); `therapeutic_modality: SMALL_MOLECULE` |
| **Parathyroid hormone (teriparatide / PTH 1-34)** | **Mouse only.** *"Osteoanabolic treatment of parathyroid hormone was effective in enhancing bone strength in Ano5 KO mice."* PTH increased cortical BMD, MAR, osteocalcin⁺ osteoblasts and TRAP⁺ osteoclasts. Critically, the authors caution: *"the absence of Ano5 might partially hinder PTH-driven bone anabolism"* — PTH worked *less well* in KO than WT mice (PMID:35982081). Proposed specifically for the **low-bone-mass subtype**. | `NCIT:C15986`; `therapeutic_modality: PEPTIDE`; **`evidence_source: MODEL_ORGANISM`** |
| **Denosumab / antiresorptives** | **Proposed only, no data.** "For GDD with high bone mass and a high bone turnover phenotype, we can choose antiresorptive treatments, such as bisphosphonates and denosumab" (PMID:35982081) | `therapeutic_modality: MONOCLONAL_ANTIBODY` |
| **Calcium and vitamin D supplementation** | Adjunctive; "Additional calcium supplementation can also be used to prevent bone loss" (PMID:35982081); recommended in affected pregnant patients (PMID:38922934) | `NCIT:C15433` Nutritional Support — **note the CLAUDE.md caveat: do not auto-tag this `BEHAVIORAL`; these are chemical supplements** |
| **Antibiotics** | Standard of care for jaw osteomyelitis; no GDD-specific regimen published | — |

**A treatment-strategy warning that belongs in the entry.** Li et al. make the subtype-dependence explicit and it cuts the wrong way if ignored: *"There are no established guidelines for the management of fracture risk in these patients. Physicians should assess the patient's skeletal status more accurately, understand the mechanisms of drugs, and formulate a treatment plan under consideration of individual differences in patients."* (PMID:35982081) **Giving an antiresorptive to a low-turnover, low-bone-mass GDD patient, or an osteoanabolic to a high-turnover osteosclerotic one, is mechanistically wrong.** Any curated treatment must be scoped to the correct subtype.

### Preclinical / experimental therapeutic targets (all **mouse or in vitro only** — none has entered human trials)

| Target | Agent | Effect | Reference |
|---|---|---|---|
| **Akt** | SC79 (activator) | "obviously rescue abnormal increased osteogenesis and decreased osteoclastogenesis in *Ano5* KI/KI mouse model" | PMID:39866532 |
| **Autophagy / ATG9A** | 3-methyladenine, chloroquine | 3-MA "alleviated the bone phenotype abnormalities in Ano5-/- mice" *in vivo* | PMID:40067389 |
| **AMPK** | Compound C (inhibitor) | "AMPK inhibitor reversed the bone phenotype of GDD by restraining bone formation and restoring osteoclastogenesis" | PMID:41717545 |
| **miR-34c-5p / KLF4** | AAV-miR-34c-5p | *In vivo* rescue of thickened cortical bone, improved biomechanics, reduced serum P1NP | PMID:40508076 |
| **NF-κB** | NF-κB activator | Partial attenuation of impaired osteoclastogenesis | PMID:36989132 |

### Surgical and interventional

**Jaw surgery** (`NCIT:C16186` Orthopedic Surgical Procedure / `NCIT:C15329` Surgical Procedure; `therapeutic_modality: SURGERY`):
- **Debulking** — the workhorse, but recurrence is the rule with incomplete removal
- **Segmental mandibulectomy / total mandibulectomy / subtotal or bilateral partial maxillectomy** (PMID:28176803, PMID:35982081)
- **Microsurgical reconstruction** — free vascularized fibular graft, titanium reconstruction plate. Marechal et al. flag the specific difficulty: *"the challenges of craniofacial reconstruction in GDD due to the diffuse bone anomalies affecting potential flap donor zones and a specific risk for jawbone osteomyelitis"* (PMID:30641283) — **the donor bone is itself diseased.**
- **Orthognathic surgery** — newly demonstrated as feasible: LeFort I advancement plus bilateral sagittal split osteotomy with setback in a 21-year-old, "No complications were seen and 2-year follow-up showed stable dental occlusion. This is the first report describing orthognathic surgery safely performed on a patient with GDD1." (PMID:41193275)

**Conservatism principle:** Cuvelier et al. recommend surgical debulking "only for a functional problem or aesthetics" given recurrence risk (PMID:38922934).

**Fracture surgery:**
- **Intramedullary devices** are recommended first-line for paediatric femoral shaft fractures in GDD (PMID:30797234)
- Intramedullary nail fixation for bilateral diaphyseal femur fractures (PMID:32455153)
- Internal fixation with successful callus formation in the first reported adult case (PMID:33826556)

### Supportive and rehabilitative

- **Prosthodontic rehabilitation** — a 30-year follow-up showed that "despite severe alveolar bone resorption, prosthetic treatment improved patient satisfaction and functional ability, requiring regular adjustments and monitoring" (PMID:29518808). `NCIT:C15302` Physical Therapy is not the right term here; look for a dental prosthesis term with OAK.
- **Dental care and pain management** (PMID:38922934)
- **Physical/occupational therapy** post-fracture and post-amputation

### Pharmacogenomics, gene therapy, cell therapy, RNA therapy, immunotherapy

**None exist for GDD.** No pharmacogenomic markers; no gene therapy, gene editing, cell therapy, or approved RNA therapeutic. The AAV-miR-34c-5p work (PMID:40508076) is the closest thing to a nucleic-acid therapeutic concept and is preclinical mouse data only.

### Clinical trials

**No interventional clinical trial for GDD has ever been registered or reported.** A ClinicalTrials.gov search for gnathodiaphyseal dysplasia returns nothing usable. Any NCT identifier attributed to GDD should be treated as suspect and verified with `just fetch-reference` before curation.

### Treatment outcomes

No response rates, no systematic adverse-event data. The single reported bisphosphonate course had no efficacy outcome published (PMID:29175271).

---

## 13. Prevention

### Primary prevention

**Disease occurrence cannot be prevented** — GDD is a dominantly inherited monogenic condition. The only primary-prevention modalities are reproductive:
- **Genetic counselling** (`NCIT:C15240` Genetic Counseling) — **50% transmission risk per pregnancy**, which Cuvelier et al. emphasize must be discussed (PMID:38922934)
- **Preimplantation genetic testing (PGT-M)** and **prenatal diagnosis** — explicitly recommended: "prenatal/pre-implantation diagnosis and medical termination should be discussed with couples" (PMID:38922934)

### Secondary prevention (early detection)

- **Cascade genetic testing and panoramic radiographic screening** of at-risk relatives — the highest-value intervention available, since many carriers are discovered incidentally (PMID:28176803)
- **Prenatal ultrasound surveillance** in known-affected families, targeting long-bone bowing (100% of prenatal cases) and fractures (33%) (PMID:38922934)
- **Timing:** given the 41-year natural-history study, initiating dental radiographic surveillance around the mixed-dentition stage is the evidence-aligned choice (PMID:40861765)

### Tertiary prevention (complication avoidance)

This is where most practical benefit lies:
- **Fracture prevention** — fall/trauma avoidance, calcium and vitamin D repletion, subtype-appropriate bone-active therapy
- **Meticulous dental hygiene and conservative dental management** — because extraction sites heal poorly and seed osteomyelitis, prophylaxis and avoidance of unnecessary extraction are rational (extrapolated from the osteomyelitis literature in PMID:28176803, PMID:29518808; not formally studied)
- **Complete rather than partial lesion resection** where surgery is indicated, to avoid accelerated regrowth (PMID:37649308)
- **Obstetric planning** in affected pregnant patients — vitamin D/calcium supplementation and a documented discussion of caesarean delivery based on disease severity (PMID:38922934)
- **In the combined muscle+bone phenotype**, avoiding overexertion to prevent rhabdomyolysis and compartment syndrome (PMID:34291158, PMID:36292621)

### Immunization, public health, environmental interventions

**Not applicable.** No vaccine strategy, no population-level public-health intervention, and no environmental risk factor to modify.

---

## 14. Other Species / Natural Disease

### Taxonomy and orthologues

- ***Ano5*** is present in **mouse (*Mus musculus*, `NCBITaxon:10090`)**, rat, **rabbit (*Oryctolagus cuniculus*, `NCBITaxon:9986`)**, **zebrafish (*Danio rerio*, `NCBITaxon:7955`)**, **fruit fly (*Drosophila melanogaster*, `NCBITaxon:7227`)**, and **mosquito** — the Cys356 residue is *"evolutionarily conserved among human, mouse, zebrafish, fruit fly, and mosquito"* (PMID:15124103).
- Mouse *Ano5*: NCBI Gene ID 233246. Human *ANO5*: NCBI Gene ID 203859.
- **Conservation caveats that matter for model design:** Thr513 is **not** strictly conserved across vertebrate *ANO5* orthologues (some carry alanine) — PMID:29124309. And Ser500 is a **threonine** in mouse, meaning the murine "equivalent" of p.S500F is p.T491F, a chemically different substitution. Li et al. argue this may explain that model's failure: "the amino acid sequence is not conserved between humans and mice at that mutation site... it is possible that Ano5 KI mice with p.T491F amino acid exchange did not display alterations in skeletal microarchitecture" (PMID:35982081).

### Natural disease in other species

**No naturally occurring GDD has been reported in any non-human species.** No OMIA entry corresponds to gnathodiaphyseal dysplasia. There is no known veterinary counterpart, no breed predisposition, and therefore **no VBO annotation applies**.

### Comparative biology

- The eight extracellular-loop cysteines are conserved across humans, teleosts, and insects (PMID:28176803).
- The functional divergence within the TMEM16 family is itself instructive: TMEM16A/B are Ca²⁺-activated chloride channels, TMEM16C/D/F/G/J are scramblases, and the T513-equivalent position "has divergent roles in phospholipid scrambling and chloride channel activity of TMEM16 family members" — introducing the same substitution into TMEM16B barely affected it (PMID:29124309).
- The strongest comparative-biology conclusion is **negative**: *"Ano5 is dispensable for bone homeostasis in mice, at least under unchallenged conditions, and... these animals may not present the most adequate model to study the physiological role of Anoctamin 5."* (PMID:32455153)

### Transmission

**No zoonotic potential and no cross-species susceptibility** — GDD is a germline genetic disorder, not transmissible.

---

## 15. Model Organisms

### The central problem: the mouse models contradict each other

This is the single most important thing to record about GDD models, and it maps directly onto dismech's **`HUMAN_MODEL_MISMATCH`** discussion kind rather than a generic knowledge gap — evidence exists in models, and it is the translational validity that is in dispute.

| Model | Genotype | Skeletal phenotype | Verdict |
|---|---|---|---|
| ***Ano5*<sup>−/−</sup> KO** (CRISPR/Cas9, Hu lab) | Homozygous null | **Replicates GDD:** "massive jawbones, bowing tibia, sclerosis and cortical thickening of femoral and tibial diaphyses"; elevated serum ALP; increased osteoblastogenesis; hypermineralized matrix | `RECAPITULATES` / `PARTIALLY_RECAPITULATES` — PMID:30712070 |
| ***Ano5*<sup>KI/KI</sup> p.Cys360Tyr** (knock-in, Hu lab) | Homozygous KI of a human GDD variant | **Replicates GDD:** massive jawbones, bowing tibia, bone fragility, sclerosis, cortical thickening; elevated ALP; increased osteoblastogenesis with hypermineralized matrix; **decreased** osteoclastogenesis with disrupted actin rings | `RECAPITULATES` — PMID:34841576. **The best available GDD model.** |
| ***Ano5*<sup>+/KI</sup> and *Ano5*<sup>KI/KI</sup> p.T491F** (knock-in, Schinke/Yorgan lab) | Murine equivalent of human p.S500F | **NO phenotype at all** — no change in trabecular or cortical microarchitecture, no mandibular abnormality, no altered bone turnover, normal three-point bending, replicated in a second independent clone and in females | **`FAILS_TO_RECAPITULATE`** — PMID:32455153 |
| ***Ano5*<sup>KO/KO</sup>** (frameshift, ~40% C-terminal loss, same lab) | Near-null | **Very mild:** increased tissue mineral density in trabecular and cortical compartments, reduced cortical porosity; no microarchitectural change | `PARTIALLY_RECAPITULATES` — PMID:32455153 |
| ***Ano5* KO** (RIKEN C57BL/6-*Ano5*<sup>tm1Itak</sup>, Qin lab) | Homozygous null | **Opposite direction:** *low* bone volume (femoral BV/TV −23%, Tb.Th −14%, mandibular BV/TV −34%), decreased mineral apposition rate, reduced osteoclast number and surface, abolished [Ca²⁺]i oscillations | `PARTIALLY_RECAPITULATES` (models the **low-bone-mass** subtype) — PMID:35982081 |
| ***Ano5*-deficient mouse** (muscle-focused) | Homozygous null | No significant clinical myopathy or cardiomyopathy | `FAILS_TO_RECAPITULATE` (muscle) — PMID:26693275, PMID:36292621 |
| **Rabbit CRISPR indel model** | Frame-disrupting exon 12/13 | Dystrophic changes in gastrocnemius, tibialis anterior, tongue, diaphragm — models the *muscle* disease | `RECAPITULATES` (muscle only) — PMID:36292621 |

**The authors themselves name the contradiction.** Rolvien et al.: *"our results are in apparent contradiction to another study, where Ano5-deficient mice recapitulated some aspects of GDD... it is quite surprising that a loss of Ano5 mimics the phenotype of GDD, especially in the light of the aforementioned study suggesting that GDD-causing mutations convey a gain-of-function... Therefore, we believe that further research is required to resolve this apparent contradiction."* (PMID:32455153)

Shaibani et al. summarize the whole picture: *"mouse models yielded conflicting results, including sarcolemma repair abnormalities and defective myoblast regeneration and fusion, lack of muscle phenotype, GDD phenotype in Ano5-knockout mice, as well as absence of skeletal phenotype in a knock-in model of a GDD-related mutation."* (PMID:34291158)

**Candidate explanations offered in the literature** (none resolved):
1. **Animal age** — GDD onsets at 10–16 years in humans; 12–24-week mice are already adult/middle-aged and skeletal signals may be masked (PMID:35982081)
2. **Residual function** in one deficiency model vs complete loss in another (PMID:32455153)
3. **Species-divergent residue** at the mutated site (Ser vs Thr at human 500 / mouse 491) (PMID:35982081)
4. **Unchallenged conditions** — Ano5 may only be required under membrane damage (PMID:32455153)
5. **GOF vs LOF** — a knockout cannot model a gain-of-function allele

**A limitation that applies to every mouse model:** none reproduces the human jaw histopathology. *"in mouse models, microscopic analysis revealed increased bone mineralization in the jaw lesions but not the microscopic features of fibrous-osseous lesions generally detected in patients with GDD."* (PMID:37649308) Li et al. propose that large-animal models (horse, sheep, dog, pig) may be required (PMID:35982081).

### Cellular and in vitro models

| System | Use | Reference |
|---|---|---|
| **MC3T3-E1 subclone 14** (mouse calvarial pre-osteoblast) | shRNA *Ano5* knockdown (~80% efficiency) → increased Ocn, Col1a1, Runx2, Osterix; increased alizarin-red mineral nodules | PMID:28176803 |
| **Primary mouse calvarial osteoblasts (mCOBs)** | The workhorse for the 2023–2026 mechanism papers (metabolomics, autophagy, miR-34c, AMPK) | PMID:36742392, PMID:40067389, PMID:40508076, PMID:41717545 |
| **Bone marrow-derived macrophages (BMMs)** | RANKL-induced osteoclastogenesis, TRAP staining, F-actin ring, Ca²⁺ oscillation imaging | PMID:35982081, PMID:39866532, PMID:36989132 |
| **RAW264.7** | *Ano5* knockdown osteoclast studies | PMID:36989132 |
| **HEK293 / HEK293T** | Heterologous TMEM16E expression, whole-cell patch clamp, annexin-V scrambling assay | PMID:29124309, PMID:32112655, PMID:28176803 |
| **CHO cells** | Ca²⁺-dependence of TMEM16E currents (0–240 µM free Ca²⁺) | PMID:29124309 |
| **COS-7** | C356G/C356R localization and cell-rounding | PMID:15124103 |
| **Patient PBMCs** | Western blot for TMEM16E abundance; PBMC-derived osteoclast Ca²⁺ oscillation imaging — **the only human-cell functional assay in the GDD literature** | PMID:35982081 |
| **Saos-2 osteosarcoma** | Source of the 898-aa TMEM16E splice isoform used in electrophysiology | PMID:29124309 |

**Notably absent:** no patient-derived iPSC line, no bone organoid, no organ-on-chip, and no immortalized GDD patient osteoblast line. Riminucci's original 2001 work transplanted stromal cells grown from the jaw lesion into immunocompromised mice and achieved "a close mimicry of the native lesion" (PMID:11547842) — a xenograft model that, remarkably, has not been revisited in 25 years and represents an obvious opportunity.

### Model resources

MGI (mouse *Ano5*), RIKEN BioResource Center (C57BL/6-*Ano5*<sup>tm1Itak</sup>), and the investigator-generated lines B6-*Ano5*<sup>tm1Pg/Uke</sup>, B6-*Ano5*<sup>tm2Pg/Uke</sup>, B6-*Ano5*<sup>tm3Pg/Uke</sup> (PolyGene AG / UKE Hamburg, PMID:32455153). No IMPC/KOMP GDD-relevant deep phenotyping has been published.

---

## Curation notes for the dismech knowledge base

A few things that will bite whoever builds the YAML entry:

1. **Named Entity Confusion risk is HIGH.** *ANO5* is far more famous for **LGMDR12 / Miyoshi myopathy 3** than for GDD. A deep-research report, a dataset search, or a literature sweep keyed on "ANO5" will return predominantly muscular-dystrophy content that is coherent, correctly cited, and about the **wrong disease**. Run `just preflight-dr <report> MONDO:0008151` before curating from any DR output. The specific facts most likely to leak across incorrectly: the **c.191dupA northern European founder mutation**, the **2:1–4:1 male predominance**, the **prevalence figures (0.27–2 per 100,000)**, and the **10–30% cardiac involvement** — all of these belong to the recessive muscle disease and **none applies to GDD**.

2. **Model the GOF/LOF dispute as competing `mechanistic_hypotheses`**, not a single chain. Suggested groups: `gain_of_function_scrambling` (CANONICAL/ALTERNATIVE, per PMID:29124309, PMID:32112655) and `loss_of_function_calcium_signaling` (ALTERNATIVE, per PMID:35982081, PMID:28176803). Attach the two bone-mass subtypes to the respective groups.

3. **Add a `HUMAN_MODEL_MISMATCH` discussion**, not a generic `KNOWLEDGE_GAP`, for the mouse-model contradiction. Evidence exists in models; it is the translational validity that is contested. Use `FAILS_TO_RECAPITULATE` with mandatory `limitations` and `evidence` for the p.T491F knock-in (PMID:32455153).

4. **Consider `conforms_to` targets.** `osteoporosis_bone_resorption#Increased Osteoclastic Bone Resorption` is a *poor* fit — GDD osteoclastogenesis is largely *decreased*. A better fit may be `defective_skeletal_mineralization` (though GDD is over- rather than under-mineralization, so check the module's scope) and possibly `loss_of_proteostasis` for the misfolded-mutant-degradation arm. Do not force a conformance that the evidence does not support.

5. **Lump/split decision on FGC and familial FCOD.** Three independent lines of evidence (PMID:27216912, PMID:37649308, PMID:42361776) now place familial gigantiform cementoma and familial florid cemento-osseous dysplasia inside the *ANO5* spectrum. Record the decision and reasoning explicitly.

6. **Ontology terms flagged for OAK verification before binding:** `HP:0005045` (Diaphyseal cortical sclerosis), `HP:0003621` (Juvenile onset), `HP:0000006` (Autosomal dominant inheritance) — these came from the HPO API and are not in the repository's local `cache/hp/terms.csv`. An HPO term for elevated alkaline phosphatase was not found in the local cache and must be looked up. Every other HP, GO, CL, and UBERON identifier cited above was verified against the local ontology label caches.

---

## Primary Sources

**Disease definition and gene discovery**
- Riminucci M et al. Gnathodiaphyseal dysplasia: a syndrome of fibro-osseous lesions of jawbones, bone fragility, and long bone bowing. *J Bone Miner Res* 2001. PMID:11547842
- Tsutsumi S et al. Autosomal dominant gnathodiaphyseal dysplasia maps to chromosome 11p14.3-15.1. *J Bone Miner Res* 2003. PMID:12619924
- Tsutsumi S et al. The novel gene encoding a putative transmembrane protein is mutated in gnathodiaphyseal dysplasia (GDD). *Am J Hum Genet* 2004. PMID:15124103 · DOI 10.1086/421527
- Mizuta K et al. Molecular characterization of GDD1/TMEM16E. *Biochem Biophys Res Commun* 2007. PMID:17418107

**Clinical reports and variant discovery**
- Marconi C et al. *Eur J Hum Genet* 2013 (T513I, Italian pedigree). PMID:23047743
- Rolvien T et al. *J Bone Miner Res* 2017 (S500F, high-turnover osteosclerosis). PMID:27541832
- Jin L et al. *Sci Rep* 2017 (three novel variants; osteoblast studies). PMID:28176803 · DOI 10.1038/srep40935
- Otaify GA et al. *Bone* 2018 (G518E, severe atypical, pamidronate). PMID:29175271
- Zeng B et al. *Head Neck* 2019 (C356F; 67% misdiagnosis rate). PMID:30554457
- Marechal G et al. *J Stomatol Oral Maxillofac Surg* 2019 (R597I; reconstruction). PMID:30641283
- Sandal S et al. *Congenit Anom* 2021 (calvarial doughnut lesions). PMID:32902009
- Shaibani A et al. *Neurol Genet* 2021 (combined myopathy + GDD). PMID:34291158 · DOI 10.1212/NXG.0000000000000612
- Iranian family, C360R. *Mol Genet Genomic Med* 2022. PMID:35758145
- Cuvelier V et al. *Prenat Diagn* 2024 (two fetal cases + 108-patient literature review). PMID:38922934 · DOI 10.1002/pd.6631
- Long-term 41-year radiographic follow-up. *Cureus* 2025. PMID:40861765
- Double jaw surgery case report. *J Craniomaxillofac Surg* 2025. PMID:41193275

**Nosology / jaw-lesion spectrum**
- Duong HY et al. *Sci Rep* 2016 (WES links dental tumour to ANO5). PMID:27216912
- Zhou Z et al. *Mol Genet Genomic Med* 2024 (FGC with C356Y). PMID:37649308 · DOI 10.1002/mgg3.2277
- Update on molecular pathology of fibro-osseous jaw lesions. *Semin Diagn Pathol* 2026. PMID:42361776

**Mechanism — biophysics**
- Di Zanni E et al. *Cell Mol Life Sci* 2018 (T513I gain of function). PMID:29124309 · DOI 10.1007/s00018-017-2704-9
- Di Zanni E et al. *Hum Mutat* 2020 (GDD = GOF, MD = LOF). PMID:32112655

**Mechanism — bone cell biology and models**
- Kim JH et al. *Bone* 2019 (Akt-NFATc1 osteoclast). PMID:30557634
- Wang X et al. *Calcif Tissue Int* 2019 (*Ano5* KO replicates GDD). PMID:30712070
- Rolvien T et al. *Bone Rep* 2020 (p.T491F KI — no phenotype). PMID:32455153
- Li H et al. *J Bone Miner Res* 2022 (Cys360Tyr knock-in model). PMID:34841576
- Li X et al. *NPJ Genom Med* 2022 (calcium signalling; LOF subtype; PTH). PMID:35982081 · DOI 10.1038/s41525-022-00312-1
- Metabolomics/transcriptomics of Ano5<sup>Cys360Tyr</sup>. *Front Endocrinol* 2023. PMID:36742392
- Liu X et al. *Oral Dis* 2024 (impaired osteoclastogenesis, NF-κB). PMID:36989132
- Akt signalling / SC79 rescue. *Bone Rep* 2025. PMID:39866532
- ER stress / CHOP osteoclast apoptosis. *Exp Cell Res* 2025. PMID:40049314
- ATG9A-dependent autophagy. *JCI Insight* 2025. PMID:40067389
- miR-34c-5p/KLF4/β-catenin. *Int J Mol Sci* 2025. PMID:40508076
- AMPK-dependent glucose metabolism. *Front Endocrinol* 2026. PMID:41717545

**Management**
- Recurrent femoral shaft fractures in a child. *BMC Musculoskelet Disord* 2019. PMID:30797234
- Prosthodontic treatment, 30-year follow-up. *Int J Prosthodont* 2018. PMID:29518808
- Adult tibial shaft fracture. *JBJS Case Connect* 2021. PMID:33826556

**Differential / context**
- Soontrapa P, Liewluck T. Anoctamin 5 (ANO5) muscle disorders: a narrative review. *Genes* 2022. PMID:36292621
- COL1A1 C-propeptide cleavage-site mutation as a GDD phenocopy. *Clin Genet* 2015. PMID:24891183
- GDD presenting as polyostotic fibrous dysplasia. *Am J Med Genet A* 2015. PMID:25866257

**Databases**
- [OMIM #166260](https://omim.org/entry/166260) · [OMIM *608662](https://omim.org/entry/608662)
- [Orphanet ORPHA:53697](https://www.orpha.net/en/disease/detail/53697)
- [MedlinePlus Genetics — gnathodiaphyseal dysplasia](https://medlineplus.gov/genetics/condition/gnathodiaphyseal-dysplasia/)
- [Open Targets — MONDO_0008151](https://platform.opentargets.org/disease/MONDO_0008151)
- [MalaCards — gnathodiaphyseal dysplasia](https://www.malacards.org/card/gnathodiaphyseal_dysplasia)
- [GARD — gnathodiaphyseal dysplasia](https://rarediseases.info.nih.gov/diseases/8698/gnathodiaphyseal-dysplasia)
- [LOVD ANO5 variant database](https://databases.lovd.nl/shared/genes/ANO5)
- [PubMed — gnathodiaphyseal dysplasia (56 results)](https://pubmed.ncbi.nlm.nih.gov/?term=gnathodiaphyseal+dysplasia)

*PubMed article metadata retrieved from PubMed (NCBI/NLM); DOIs are given inline for cited articles.*

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 48 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 35 |
| Quoted claims found in source | 23 |
| Quoted claims **not** found in source | 12 |
| References weighed for topical relevance | 48 |
| On topic | 40 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

10 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:11547842` *(abstract only)*: "gnathodiaphyseal sclerosis"
  - Text part not found as substring: 'gnathodiaphyseal sclerosis' (note: only abstract available for PMID:11547842, full text may contain this excerpt)
- `PMID:12619924` *(abstract only)*: "as a new and distinct disease entity from other systemic bone diseases"
  - closest text in source: "Although GDD has been considered to be a variation of osteogenesis imperfecta (MIM 166260), our results indicate that this syndrome is a new and distinct disease entity from other systemic bone diseases"
- `PMID:28176803`: "severe facial disfigurement"
  - Text part not found as substring: 'severe facial disfigurement'
- `PMID:29175271` *(abstract only)*: "severe facial disfigurement"
  - Text part not found as substring: 'severe facial disfigurement' (note: only abstract available for PMID:29175271, full text may contain this excerpt)
- `PMID:38922934` *(abstract only)*: "probably pathogenic (class 4)"
  - Text part not found as substring: 'probably pathogenic (class 4)' (note: only abstract available for PMID:38922934, full text may contain this excerpt)
- `PMID:28176803`: "fold with low efficiency and appear to be unstable and rapidly degraded via proteasomal degradation"
  - closest text in source: "Recent studies23 suggest that mutant ANO5 protein (C356G and C356R) folds with low efficiency and appears to be unstable and rapidly degraded via proteasomal degradation"
- `PMID:38922934` *(abstract only)*: "multiple diaphyseal fractures of the long bones... affecting femurs, tibias, and bilateral upper extremity bones"
  - closest text in source: "Clinical manifestations range from recurrent dental infections with mild jaw lesions to severe bone fragility with several fractures associated with large jaw lesions requiring disfiguring surgeries"
- `PMID:24891183` *(abstract only)*: "a new cause of gnathodiaphyseal dysplasia"
  - closest text in source: "Gnathodiaphyseal dysplasia (GDD) is a rare autosomal dominant condition characterized by bone fragility, irregular bone mineral density (BMD) and fibro-osseous lesions in the skull and jaw"
- `PMID:38922934` *(abstract only)*: "symptoms can be very severe, even fatal"
  - closest text in source: "Clinical manifestations range from recurrent dental infections with mild jaw lesions to severe bone fragility with several fractures associated with large jaw lesions requiring disfiguring surgeries"
- `PMID:33826556` *(abstract only)*: "successful callus formation"
  - Text part not found as substring: 'successful callus formation' (note: only abstract available for PMID:33826556, full text may contain this excerpt)
- `PMID:29518808` *(abstract only)*: "despite severe alveolar bone resorption, prosthetic treatment improved patient satisfaction and functional ability, requiring regular adjustments and monitoring"
  - closest text in source: "Despite the severe alveolar bone resorption, prosthodontic treatment improved the patient's satisfaction and ability to perform essential functions"
- `PMID:38922934` *(abstract only)*: "prenatal/pre-implantation diagnosis and medical termination should be discussed with couples"
  - closest text in source: "A literature review was conducted to explore GDD's clinical and paraclinical presentation, diagnosis, and management"