---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-06-30T20:53:36.607888'
end_time: '2026-06-30T20:57:49.686224'
duration_seconds: 253.08
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Kikuchi-Fujimoto Disease
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-4-8[1m]
  web_search_requests: 9
  num_turns: 14
  total_cost_usd: 2.3192139999999997
  session_id: 607620eb-bd9b-463e-9e93-5ad47ccbb217
  stop_reason: end_turn
citation_count: 15
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Kikuchi-Fujimoto Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Kikuchi-Fujimoto Disease** covering all of the
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

I have enough to write a comprehensive, well-cited report. Here it is.

---

# Research Report: Kikuchi-Fujimoto Disease

**Prepared:** 2026-06-30 · **Category:** Complex (immune-mediated / idiopathic) · **Target KB entry:** `kb/disorders/Kikuchi-Fujimoto_Disease.yaml`

> **Evidence-source note for curators:** Nearly the entire KFD literature is **HUMAN_CLINICAL** — case reports, single-institution retrospective series, and narrative reviews. There are essentially **no validated animal models** and **no interventional RCTs**. Molecular claims rest on immunohistochemistry of human nodal tissue (**IN_VITRO / ex vivo**) and a small number of transcriptomic/exome studies. Treat every "mechanism" as a well-supported hypothesis rather than proven causation — the etiology remains formally unknown.

---

## 1. Disease Information

**Overview.** Kikuchi-Fujimoto disease (KFD), synonymously **histiocytic necrotizing lymphadenitis (HNL)**, is a rare, benign, usually self-limiting cause of subacute regional (typically cervical) lymphadenopathy with fever. It was described independently in Japan in 1972 by Masahiro Kikuchi and by Yoshiro Fujimoto. Diagnosis is **exclusively histopathological** — the clinical and imaging picture is nonspecific and closely mimics both lymphoma and lupus lymphadenitis, so an excisional lymph-node biopsy is essential ([PMC11592699, MDPI *Diseases* 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11592699/); [comprehensive review, PMID 37383134 / PMC10294163](https://pmc.ncbi.nlm.nih.gov/articles/PMC10294163/)).

> *"A rare form of necrotizing lymphadenitis, is an uncommon, benign, self-limiting disorder of obscure etiology."* — comprehensive review (PMID 37383134)

**Key identifiers.**

| System | ID |
|---|---|
| **MONDO** | **MONDO:0018864** |
| Orphanet | **ORPHA:50918** |
| ICD-11 | **4B2Y** (other/unspecified) — often coded under nonspecific lymphadenitis |
| ICD-10 | **I88.1** (chronic lymphadenitis) |
| MeSH | **D020042** ("Histiocytic Necrotizing Lymphadenitis") |
| UMLS | C0398367 |
| GARD | 6834 |
| MedDRA | 10069070 |

*(Identifiers compiled from Orphanet/NORD/EBI-OLS listings — please re-verify MONDO/ICD mappings against the local `sqlite:obo:mondo` adapter before committing, per the NEC preflight in CLAUDE.md.)*

**Synonyms / alternative names:** Kikuchi disease; Kikuchi-Fujimoto syndrome; histiocytic necrotizing lymphadenitis (HNL); necrotizing lymphadenitis; subacute necrotizing lymphadenitis.

**Data provenance:** Disease-level, aggregated from case series and reviews (not EHR/individual-patient registries). No dedicated large prospective registry exists.

---

## 2. Etiology

**The cause is unknown.** Two non-exclusive hypotheses dominate: (a) an **infectious trigger** (most often viral) and (b) an **exaggerated, self-limited autoimmune/T-cell–mediated response** in a genetically susceptible host — essentially a transient "SLE-like" reaction.

**Infectious/viral hypothesis.** Many agents have been *associated* (temporally, serologically, or by case report) but **none proven causal**: EBV, HSV, VZV, HHV-6/7/8, parvovirus B19, paramyxovirus, parainfluenza, rubella, CMV, and — more recently — SARS-CoV-2 infection and post-COVID-vaccination cases ([PMC11592699](https://pmc.ncbi.nlm.nih.gov/articles/PMC11592699/)). Support for a viral component comes from raised **IFN-α** and its downstream marker **2′,5′-oligoadenylate synthetase**, plus **tubuloreticular structures** in the cytoplasm of stimulated lymphocytes/histiocytes/endothelium — an interferon-signature also seen in SLE (PMID 37383134).

> *"Increased levels of IFN-α and its stimulators including 2′,5′-oligoadenylate synthetase, and tubuloreticular structures in the cytoplasm of stimulated lymphocytes."* — PMID 37383134

**Autoimmune hypothesis.** KFD is postulated to be *"a self-limiting SLE-like autoimmune disorder caused by virus-infected transformed lymphocytes"* triggering a cell-mediated response *"to a variety of antigens in genetically susceptible people"* ([PMC11592699](https://pmc.ncbi.nlm.nih.gov/articles/PMC11592699/)).

**Genetic risk factors.** No causal Mendelian gene. The principal susceptibility signal is **HLA class II**, notably **HLA-DPA1 and HLA-DPB1** alleles that are far more common in East Asians than in Europeans. A Japanese case-control study (86 KFD patients vs 525 controls) found **DPA1\*01** and **DPB1\*0202** significantly over-represented in KFD; these alleles are common in Korea (~9.9%) and Japan (~4.5%) but rare in French (~0.4%) and Italian (~0.8%) populations — plausibly explaining the Asian predominance ([summarized in PMC11592699](https://pmc.ncbi.nlm.nih.gov/articles/PMC11592699/)). A 2023 report described **familial KFD in HLA-partially-matched siblings both carrying DPB1\*0202** ([PMC10803893](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10803893/)). RNA- and exome-sequencing efforts have begun to nominate additional candidate genes ([ScienceDirect S0890850821000359](https://www.sciencedirect.com/science/article/abs/pii/S0890850821000359)).

**Environmental / lifestyle risk factors:** young age and Asian ancestry are the strongest demographic risks; female sex from the 30s onward. No confirmed occupational, toxic, dietary, or smoking association.

**Protective factors:** none established (genetic or environmental).

**Gene–environment interaction (working model):** an environmental antigen (virus) in a host carrying permissive HLA-DP alleles drives an over-exuberant CD8⁺ T-cell response that produces the necrotizing lesion, then self-terminates.

---

## 3. Phenotypes

For a KB entry, the core phenotype bundle (with suggested HPO terms and approximate frequencies from case series) is:

| Phenotype | Type | Frequency | Suggested HPO |
|---|---|---|---|
| **Cervical lymphadenopathy** (usually unilateral, posterior, tender) | Sign | ~virtually all cases; cervical ~85% | **HP:0002726** (Abnormal cervical lymph node morphology) / HP:0002716 (Lymphadenopathy) |
| **Fever** (intermittent, low-grade) | Symptom | ~30–55% | **HP:0001945** (Fever) |
| **Leukopenia** | Lab | ~18–50% (commonest lab abnormality) | **HP:0001882** (Leukopenia) |
| **Elevated ESR** | Lab | ~16–70% | **HP:0003565** (Elevated erythrocyte sedimentation rate) |
| **Elevated LDH** | Lab | frequent | **HP:0025435** (Increased circulating lactate dehydrogenase) |
| **Anemia** (chronic disease) | Lab | ~9–23% | **HP:0001903** (Anemia) |
| **Cutaneous lesions** (facial erythema, papules/plaques, morbilliform/acneiform) | Sign | ~30–40% | **HP:0000988** (Skin rash) |
| **Night sweats** | Symptom | common | **HP:0000989**? (use HP:0030166 Night sweats) |
| **Weight loss** | Symptom | occasional | **HP:0001824** (Weight loss) |
| **Splenomegaly** | Sign | occasional (severe cases) | **HP:0001744** (Splenomegaly) |
| **Hepatomegaly / elevated transaminases** | Sign/Lab | occasional | **HP:0002240** / HP:0002910 |
| **Arthralgia/arthritis** | Symptom | occasional | **HP:0002829** (Arthralgia) |
| **Aseptic meningitis / CNS involvement** | Sign | rare (extranodal) | **HP:0033146** (Aseptic meningitis) / HP:0002383 (Encephalitis) |
| **Atypical lymphocytosis** | Lab | ~25–30% | **HP:0031392** (Atypical lymphocytes) |

**Characteristics.** Onset is **subacute** over 1–4 weeks; symptom duration averages ~2–3 weeks but can persist — one Japanese cohort reported a **mean symptomatic duration of 71.5 days** ([PMID 39961627 / PMC12129606](https://pmc.ncbi.nlm.nih.gov/articles/PMC12129606/)). Severity is usually **mild–moderate and self-limited**; a minority have severe systemic/extranodal disease. Course is **self-limited but occasionally recurrent** (see §8, §11).

> *"Fever (55.2%) was the most common clinical manifestation. Leukopenia (49.3%) was the commonest reported laboratory abnormality."* — cervical-KFD retrospective (n=134), [PMC10446312](https://pmc.ncbi.nlm.nih.gov/articles/PMC10446312/)

**Quality-of-life impact:** generally limited given self-resolution, but the diagnostic odyssey (fear of lymphoma), painful nodes, prolonged fever, and recurrence-related anxiety are the main burdens. No KFD-specific QoL instrument exists.

---

## 4. Genetic / Molecular Information

- **Causal genes:** **none.** KFD is not a Mendelian disorder.
- **Susceptibility loci:** **HLA-DPA1** (HGNC:4938) and **HLA-DPB1** (HGNC:4940); risk alleles **DPA1\*01**, **DPB1\*0202** ([PMC11592699](https://pmc.ncbi.nlm.nih.gov/articles/PMC11592699/); familial case [PMC10803893](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10803893/)). These are **germline, common population variants** (association, not pathogenic mutations) — not classifiable by ACMG as pathogenic.
- **Somatic vs germline:** the HLA association is germline; no recurrent somatic driver is described (KFD is non-neoplastic — clonality studies are typically negative, distinguishing it from lymphoma).
- **Modifier genes / epigenetics / chromosomal abnormalities:** none established. Karyotype and clonality are normal — an important negative used to exclude lymphoma.
- **Emerging genomics:** RNA-seq/exome studies are early-stage and nominate immune/interferon-pathway genes rather than a single culprit ([ScienceDirect 2021](https://www.sciencedirect.com/science/article/abs/pii/S0890850821000359)).

**Suggested gene descriptors (HGNC):** hgnc:4938 (HLA-DPA1), hgnc:4940 (HLA-DPB1). Because casing in this repo is lowercase `hgnc:`.

---

## 5. Environmental Information

- **Environmental/toxic/occupational factors:** none confirmed.
- **Lifestyle factors:** none confirmed.
- **Infectious agents (candidate triggers, unproven):** EBV (NCBITaxon:10376), HSV (10298), VZV/HHV-3 (10335), HHV-6 (10368), HHV-8 (37296), parvovirus B19 (10798), CMV/HHV-5 (10359), paramyxoviruses, parainfluenza, rubella virus (11041), **SARS-CoV-2 (2697049)** — associations are temporal/serological; **no organism has been consistently isolated or shown causal** ([PMC11592699](https://pmc.ncbi.nlm.nih.gov/articles/PMC11592699/); [SARS-CoV-2-triggered case, PMC10077921](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10077921/)).

---

## 6. Mechanism / Pathophysiology

**Causal chain (best-supported hypothesis):**

1. **Trigger** — a viral (or other) antigen in an HLA-DP–permissive host.
2. **Interferon-driven activation** — type I IFN (IFN-α) signature: elevated 2′,5′-oligoadenylate synthetase, tubuloreticular inclusions, and recruitment/activation of **plasmacytoid dendritic cells (pDCs)** (upstream) (PMID 37383134).
3. **CD8⁺ cytotoxic T-cell response** — an **exaggerated T-cell–mediated immune response** with marked CD8⁺ T-lymphocyte predominance.
4. **Fas–Fas-ligand apoptosis** — *"apoptotic cell death induced by the Fas–Fas ligand system mediated by cytotoxic CD8+ cells is the principal mechanism of cellular destruction in KFD"* (PMID 37383134). This produces the hallmark **apoptotic karyorrhexis**.
5. **Histiocytic phagocytosis** — CD68⁺/CD163⁺/MPO⁺ histiocytes (many crescentic/"C-shaped" nuclei) clear apoptotic debris, forming necrotic foci **without neutrophils and without well-formed granulomas** (downstream) ([PMC11592699](https://pmc.ncbi.nlm.nih.gov/articles/PMC11592699/)).
6. **Self-limited resolution** — the response terminates, node architecture recovers.

**Cell types involved (suggested CL terms):**
- **CD8⁺ cytotoxic T cell** — **CL:0000794**
- **Plasmacytoid dendritic cell** — **CL:0000784** (CD123⁺/CD303⁺; a defining infiltrate)
- **Myeloid/immature dendritic cell** — **CL:0000840** (immature) / CL:0000451
- **Histiocyte / macrophage** — **CL:0000235** (CD68⁺, CD163⁺, MPO⁺, lysozyme⁺)
- **Immunoblast** (large transformed lymphoid cell) — CL:0000653? (use B/T immunoblast as available)

**Immunophenotype of the diagnostic lesional cells** (Pileri/Facchetti-type analysis, [PMID 19141377](https://pubmed.ncbi.nlm.nih.gov/19141377/)): the "plasmacytoid" mononuclear cells are **two populations of immature dendritic cells** — myeloid DCs (CD68⁺, CD1c/BDCA-1⁺, CD13/CD33⁺) and plasmacytoid DCs (CD303/BDCA-2⁺, CD123⁺), strongly **MxA⁺** (IFN-α–inducible) and **fascin-negative** (immature).

> *"The morphologically distinctive mononuclear cells in lesional areas consisted of 2 populations of immature DCs: myeloid DCs …"* — PMID 19141377

**Suggested GO biological-process terms:**
- **GO:0006915** apoptotic process (INCREASED)
- **GO:0097191** extrinsic apoptotic signaling pathway / **GO:0036337** Fas signaling (INCREASED)
- **GO:0060337** type I interferon signaling pathway (INCREASED)
- **GO:0001913** T cell–mediated cytotoxicity (INCREASED)
- **GO:0006909** phagocytosis (INCREASED)
- **GO:0002456** T cell–mediated immunity (INCREASED)

**Immune involvement:** this is fundamentally an **immune-mediated** disease (cytotoxic T cell + interferon + dendritic-cell axis), sitting on a spectrum toward SLE — hence the overlapping interferon signature and the clinical progression of a subset to lupus. **Molecular profiling** beyond IHC (bulk transcriptomics/single-cell/proteomics) is sparse; no metabolomic or lipidomic signature is defined.

---

## 7. Anatomical Structures Affected

- **Primary:** **lymph nodes**, especially **cervical** (posterior triangle, levels II–V), usually **unilateral** (**UBERON:0000029** lymph node; **UBERON:0002429** cervical lymph node). ~85% cervical.
- **Other nodal sites:** axillary, supraclavicular, mesenteric, mediastinal; **generalized lymphadenopathy** in a minority.
- **Extranodal / secondary (organ systems):** **skin** (UBERON:0002097; 30–40%), **spleen** (UBERON:0002106, splenomegaly), **liver** (UBERON:0002107), **bone marrow** (UBERON:0002371, in HLH), and **CNS** (UBERON:0001017 — aseptic meningitis, meningoencephalitis, cerebellar ataxia, optic neuritis).
- **Tissue/cell level:** paracortical (T-zone) expansion with patchy necrosis; infiltrate of CD8⁺ T cells, immature dendritic cells, and histiocytes; **B cells and plasma cells characteristically scarce** (their presence suggests lupus instead).
- **Subcellular (GO cellular component):** cytoplasmic **tubuloreticular structures** (endoplasmic-reticulum–derived; GO:0005783 endoplasmic reticulum); nuclear fragmentation (karyorrhexis) of apoptotic bodies.
- **Lateralization:** predominantly **unilateral** cervical.

---

## 8. Temporal Development

- **Onset:** young adults (mean ~30 years); **subacute** over days–weeks. Pediatric cases occur.
- **Course:** **self-limited**, typically resolving in **1–4 months**. Symptom duration is variable (mean ~71.5 days in one series; [PMID 39961627](https://pmc.ncbi.nlm.nih.gov/articles/PMC12129606/)).
- **Histologic evolution:** **proliferative (early) → necrotizing (peak) → xanthomatous/foamy (resolving)** phases — a temporal, not just categorical, sequence ([PMC11592699](https://pmc.ncbi.nlm.nih.gov/articles/PMC11592699/)). The necrotizing pattern correlates with larger nodes and longer symptom duration ([PMID 39961627](https://pmc.ncbi.nlm.nih.gov/articles/PMC12129606/)).
- **Remission:** usually **spontaneous**; corticosteroids hasten resolution in severe cases.
- **Recurrence:** reported **~3–23% in adults** (up to **~42%** in some pediatric series); often multiple episodes (44% of recurrers had ≥2). Recurrence flags a higher likelihood of underlying/evolving autoimmunity (see §11).

---

## 9. Inheritance and Population

- **Epidemiology:** **rare**; true incidence/prevalence undefined. Most reported cases are from **East and Southeast Asia**; uncommon in the US/Europe.
- **Age:** predominantly **20–40 years** (mean ~29–30).
- **Sex:** historically described as female-predominant (older reports up to ~1:4 M:F), but recent large series show a **near-equal or only mildly female-skewed ratio** — one 112-patient Japanese cohort was **54.5% female**, with **male predominance up to age 20 and female predominance from the 30s onward** ([PMID 39961627 / PMC12129606](https://pmc.ncbi.nlm.nih.gov/articles/PMC12129606/)).
- **Inheritance pattern:** **not inherited** in a Mendelian sense; **multifactorial** with an **HLA-DP association** and rare familial clustering ([PMC10803893](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10803893/)). No penetrance/expressivity/anticipation/mosaicism/founder/carrier-frequency parameters apply.
- **Geographic distribution:** endemic-appearing clustering in Asia, mirroring HLA-DPB1\*0202/DPA1\*01 allele frequencies.

---

## 10. Diagnostics

**Definitive test: excisional lymph-node biopsy with histopathology** (FNA is often nondiagnostic and risks missing lymphoma).

- **Histopathology (diagnostic hallmarks):** paracortical **necrotizing** foci with abundant **apoptotic karyorrhexis**, crescentic **histiocytes**, immunoblasts, and plasmacytoid dendritic cells; **absence of neutrophils and plasma cells**; **no granulomas**. Three patterns: **proliferative (~77%), necrotizing (~22%), xanthomatous (~1%)** ([PMID 39961627](https://pmc.ncbi.nlm.nih.gov/articles/PMC12129606/)).
- **Immunohistochemistry:** CD8⁺ T cells predominate (CD4:CD8 reversed); histiocytes CD68⁺/CD163⁺/**MPO⁺**/lysozyme⁺; **CD123⁺** plasmacytoid DCs; scant CD20⁺ B cells; **no clonal rearrangement** (excludes lymphoma).
- **Laboratory:** leukopenia (commonest), atypical lymphocytes, elevated ESR/CRP, elevated LDH, mild transaminitis, anemia; **ANA usually negative** at baseline (positivity raises suspicion of SLE).
- **Imaging (supportive, nonspecific):** ultrasound — enlarged nodes with preserved echogenic hilum, no calcification; CT — homogeneous, enhancing unilateral cervical nodes (levels II–V); **¹⁸F-FDG PET/CT — multiple hypermetabolic nodes** that can strongly mimic lymphoma (PMID 37383134).
- **Differential diagnosis (critical):** **non-Hodgkin lymphoma** and **Hodgkin lymphoma** (most important to exclude), **SLE lymphadenitis** (histologically indistinguishable in ~20% — look for hematoxylin bodies, abundant plasma cells, DNA deposits), **tuberculosis** and other granulomatous infections, cat-scratch disease, infectious mononucleosis, HSV lymphadenitis, Sweet syndrome, histoplasmosis, syphilis, leprosy ([PMC11592699](https://pmc.ncbi.nlm.nih.gov/articles/PMC11592699/)).
- **Genetic/omics testing:** **not indicated clinically** — HLA typing is a research tool, not diagnostic. No newborn/carrier/cascade screening applies.

---

## 11. Outcome / Prognosis

- **Overall prognosis: excellent** — most patients recover spontaneously within months.
- **Mortality:** **~2.1%**, essentially confined to severe cases with **hemophagocytic lymphohistiocytosis (HLH)/macrophage-activation syndrome**, connective-tissue disease, or complications such as pulmonary hemorrhage, DIC, or heart failure (PMID 37383134).

> *"With a reported fatality rate of 2.1% and severe and fatal cases having been generally associated with hemophagocytic syndrome or connective tissue disease."* — PMID 37383134

- **Recurrence:** ~3–23% (adults); higher in children.
- **Progression to autoimmunity (key prognostic concern):** a subset develop **SLE** — before, concurrent with, or after KFD (reported split ≈ KFD-before 30% / simultaneous 47% / KFD-after 23%). **Recurrent KFD** is an *"intermediate status between transient KFD and overt autoimmune disease,"* associated with **higher ANA positivity (57% vs 7%) and lower C4** ([PMID 39961627](https://pmc.ncbi.nlm.nih.gov/articles/PMC12129606/)). **Long-term follow-up with ANA monitoring is recommended.**
- **Prognostic factors:** ANA positivity, low complement (C4), extranodal/CNS involvement, HLH, and necrotizing histology (larger nodes, longer course) predict more severe/protracted or recurrent disease.
- **Complications:** HLH/MAS, aseptic meningitis/meningoencephalitis, cerebellar ataxia, optic neuritis, myocarditis, hepatitis, uveitis — all uncommon.

---

## 12. Treatment

**No approved disease-specific therapy; management is empirical and largely supportive** — the disease self-resolves ([PMC11592699](https://pmc.ncbi.nlm.nih.gov/articles/PMC11592699/); PMID 37383134).

| Line | Intervention | Notes | Suggested MAXO/NCIT |
|---|---|---|---|
| Mild disease | **NSAIDs / analgesics / antipyretics** | Symptom control (fever, node pain) | MAXO:0000058 (NSAID therapy) / **NCIT:C15986** Pharmacotherapy + CHEBI agent |
| Moderate–severe / extranodal / relapsing | **Systemic corticosteroids** (e.g., prednisolone) | Rapid symptom resolution; reserved for severe/extranodal disease | **NCIT:C15986** Pharmacotherapy + therapeutic_agent **NCIT:C2322** Corticosteroid (or CHEBI prednisolone) |
| Recurrent / steroid-dependent / autoimmune-leaning | **Hydroxychloroquine** | Immunomodulatory; used in recurrent/lupus-associated cases | **NCIT:C15986** + CHEBI:5801 (hydroxychloroquine) |
| Severe/refractory or HLH | **IVIG**, other immunomodulators; HLH-directed therapy | Case-based | MAXO:0000841 (immunoglobulin therapy) / supportive care MAXO:0000950 |
| Supportive | **Supportive care** | Hydration, monitoring | **MAXO:0000950** supportive care |

- **Pharmacogenomics:** none established for KFD.
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno):** **not applicable** — no targeted or biologic therapy is standard.
- **Surgery:** limited to **diagnostic excisional biopsy**; not therapeutic (MAXO:0000004 surgical procedure).
- **Clinical trials:** essentially none of note; a historical observational study exists ([NCT00172445, "Clinical Studies of Kikuchi's Disease"](https://clinicaltrials.gov/study/NCT00172445)). No modern interventional RCTs.
- **Response:** corticosteroids reliably shorten severe episodes; overall outcomes are excellent regardless.

---

## 13. Prevention

- **Primary prevention:** **none** — cause unknown, so no vaccine or risk-factor modification.
- **Secondary prevention / early detection:** the practical "prevention" target is **early lymph-node biopsy** to avoid misdiagnosis as lymphoma and unnecessary chemotherapy, and **post-diagnosis surveillance for SLE** (periodic ANA/complement).
- **Tertiary prevention:** monitor and promptly treat recurrences, HLH, and evolving autoimmunity.
- **Immunization / public-health / behavioral / prophylaxis / genetic counseling:** **not applicable** (non-heritable, non-communicable).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** KFD is described **only in humans (NCBITaxon:9606)**.
- **Natural animal disease:** **none reported** — no recognized veterinary/wildlife counterpart in OMIA or veterinary literature.
- **Orthologous genes:** the implicated **HLA-DP** loci belong to the MHC class II system, which has orthologues across mammals, but no cross-species KFD phenotype is documented.
- **Zoonotic / cross-species transmission:** **not applicable** (KFD is not an infection).

---

## 15. Model Organisms

- **Animal models:** **none validated.** There is no established mouse, rat, zebrafish, or other in-vivo model that recapitulates KFD. This is a genuine knowledge gap — appropriate for a `KNOWLEDGE_GAP` discussion node in the KB entry.
- **In-vitro / ex-vivo systems:** mechanistic work relies on **human lymph-node tissue** (IHC, in-situ apoptosis assays, interferon-marker studies) rather than engineered models.
- **Implication for curation:** all mechanistic evidence should be tagged **HUMAN_CLINICAL** or **IN_VITRO** (tissue-based); **do not tag any KFD evidence as MODEL_ORGANISM**, since no animal model data exist.

---

## Curation Summary — high-confidence anchors for the KB entry

- **Identity:** MONDO:0018864 / ORPHA:50918 / MeSH D020042; synonym "histiocytic necrotizing lymphadenitis."
- **Core pathophysiology edge chain:** viral/antigen trigger → type I interferon activation + pDC recruitment → exaggerated CD8⁺ cytotoxic T-cell response → **Fas–FasL apoptosis (karyorrhexis)** → histiocytic phagocytosis/necrosis (no neutrophils, no granulomas) → self-limited resolution.
- **Genetics:** HLA-DPA1\*01 / HLA-DPB1\*0202 susceptibility (association only).
- **Phenotype core:** cervical lymphadenopathy (HP:0002716/HP:0002726) + fever (HP:0001945) + leukopenia (HP:0001882) + elevated ESR (HP:0003565) + elevated LDH (HP:0025435).
- **Prognosis:** self-limited, ~2.1% mortality (via HLH/CTD); recurrence 3–23%; **SLE overlap** is the defining long-term concern.
- **Treatment:** NSAIDs → corticosteroids → hydroxychloroquine/IVIG; supportive.

### Priority PMIDs to fetch & snippet-validate before committing
- **PMID 37383134** — Kikuchi-Fujimoto disease: a comprehensive review (interferon mechanism, Fas-FasL, 2.1% mortality, imaging).
- **PMID 39961627** — clinicopathological features & recurrence risk factors (subtype %, recurrence 23%, ANA/C4).
- **PMID 19141377** — immature dendritic-cell phenotype of lesional cells (CD123, CD303, MPO, MxA, fascin-neg).
- **Archives of Pathology & Lab Medicine 2018;142(11):1341** (Perry & Choi) — authoritative pathology review.
- MDPI *Diseases* 2024 case series ([PMC11592699](https://pmc.ncbi.nlm.nih.gov/articles/PMC11592699/)) and the HLA familial case ([PMC10803893](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10803893/)).

> ⚠️ **Follow the dismech SOP:** run `just fetch-reference PMID:37383134` (etc.), then confirm each `snippet:` is an exact substring of the cached abstract before validating — several quotes above are paraphrase-adjacent and must be tightened to verbatim abstract text. Re-verify the MONDO/ICD-11 mappings against the local ontology adapter per the NEC preflight.

---

**Sources:**
- [Kikuchi-Fujimoto disease: A comprehensive review — PMID 37383134 / PMC10294163](https://pmc.ncbi.nlm.nih.gov/articles/PMC10294163/)
- [Kikuchi–Fujimoto Disease: A Case Series and Review — PMC11592699 (MDPI *Diseases* 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11592699/)
- [Clinicopathological features and risk factors for recurrence — PMID 39961627 / PMC12129606 (*Histopathology* 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12129606/)
- [Retrospective study of 134 cervical KFD patients — PMC10446312](https://pmc.ncbi.nlm.nih.gov/articles/PMC10446312/)
- [Lesional cells exhibit an immature dendritic cell phenotype — PMID 19141377](https://pubmed.ncbi.nlm.nih.gov/19141377/)
- [KFD in HLA partially-matched siblings (familial susceptibility) — PMC10803893](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10803893/)
- [Genes associated with KFD via RNA/exome sequencing — ScienceDirect 2021](https://www.sciencedirect.com/science/article/abs/pii/S0890850821000359)
- [SARS-CoV-2 triggering KFD — PMC10077921](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10077921/)
- [KFD + SLE + HLH case report — PMC6551871](https://pmc.ncbi.nlm.nih.gov/articles/PMC6551871/)
- [Kikuchi-Fujimoto Disease: A Review — Arch Pathol Lab Med 2018](https://meridian.allenpress.com/aplm/article/142/11/1341/103043/Kikuchi-Fujimoto-Disease-A-Review)
- [Orphanet ORPHA:50918](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=50918) · [NORD MONDO listing](https://rarediseases.org/mondo-disease/kikuchi-fujimoto-disease/) · [GARD 6834](https://rarediseases.info.nih.gov/diseases/6834/kikuchi-fujimoto-disease)
- [StatPearls: Kikuchi-Fujimoto Disease — NBK430830](https://www.ncbi.nlm.nih.gov/books/NBK430830/)