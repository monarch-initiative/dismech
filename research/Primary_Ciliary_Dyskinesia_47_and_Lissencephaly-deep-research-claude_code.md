---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T22:09:07.999635'
end_time: '2026-07-31T22:14:31.477298'
duration_seconds: 323.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Primary Ciliary Dyskinesia 47 and Lissencephaly
  mondo_id: ''
  category: Genetic
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
  - claude-sonnet-5
  web_search_requests: 16
  num_turns: 21
  total_cost_usd: 1.8838864999999996
  session_id: d9593d63-da8a-51dc-ac14-f15a6943c38f
  stop_reason: end_turn
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Ciliary Dyskinesia 47 and Lissencephaly
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Primary Ciliary Dyskinesia 47 and Lissencephaly** covering all of the
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

# Research Report: Primary Ciliary Dyskinesia-47 and Lissencephaly (TP73-Related Mucociliary Clearance Disorder)

## 1. Disease Information

**Overview:** Primary Ciliary Dyskinesia-47 and Lissencephaly (CILD47) is an ultra-rare autosomal recessive disorder caused by biallelic loss-of-function variants in **TP73** (the p53-family transcription factor gene). It combines a motile-ciliopathy respiratory phenotype (chronic mucociliary clearance failure) with a neurodevelopmental phenotype (anterior-predominant lissencephaly/pachygyria with corpus callosum abnormality). Mechanistically it is not a classic axonemal-structure PCD but belongs to the "**reduced generation of multiple motile cilia**" (RGMC) subgroup — a defect in the transcriptional program that specifies multiciliated cell (MCC) differentiation itself, analogous to MCIDAS-, CCNO-, and FOXJ1-related disease, rather than a defect of the assembled axoneme (Wallmeier et al. 2021, PMID:34077761).

**Key identifiers:**
- **OMIM phenotype:** #619466 — "Ciliary dyskinesia, primary, 47, and lissencephaly (CILD47)"
- **OMIM gene:** *601990 — TP73 (tumor protein p73)
- **Gene location:** 1p36.32 (HGNC:12003; NCBI Gene ID 7161)
- **MONDO/Orphanet:** No independently verified MONDO or dedicated Orphanet ID was found in this search; the condition is recent (2021) and may only be indexed under a general PCD/RGMC or OMIM-derived term. **This should be explicitly checked with OAK/MONDO lookup before curation** rather than assumed.
- **Inheritance:** Autosomal recessive
- Distinguish from "isolated" lissencephaly (LIS1/PAFAH1B1, DCX, TUBA1A etc.) — TP73-lissencephaly is a **syndromic, ciliopathy-associated** lissencephaly, mechanistically and radiologically distinct (see §6, §7).

**Synonyms/alternative names:** "TP73-related mucociliary clearance disorder and lissencephaly"; "CILD47"; occasionally described under the umbrella term "reduced generation of multiple motile cilia (RGMC) with lissencephaly."

**Evidence basis:** All currently published human data derive from a single case series — **7 affected individuals from 5 unrelated, mostly consanguineous families** (Wallmeier et al. 2021, *Am J Hum Genet* 108(7):1318–1329, PMID:34077761) — supplemented by extensive **mouse-model** mechanistic literature on Trp73/TAp73 in ciliated epithelia (see §6, §15). This is aggregated disease-level case-series data, not large-cohort or EHR-derived data — sample size is a fundamental limitation for all epidemiological/prognostic claims below.

---

## 2. Etiology

**Disease causal factor:** Purely genetic — biallelic (homozygous or compound heterozygous) loss-of-function variants in **TP73**, disrupting both major isoform classes (TAp73, the N-terminally intact transactivating isoform, and ΔNp73, the N-terminally truncated isoform), resulting in complete TP73 protein deficiency (PMID:34077761).

**Genetic risk factors:**
- Biallelic TP73 null alleles are causal and (based on the reported families) appear fully penetrant for the respiratory+CNS phenotype.
- **Consanguinity** is a major risk factor observationally — "most families showed consanguinity" in the founding cohort (PMID:34077761), consistent with an autosomal recessive, presumably ultra-rare allele model with regional/familial enrichment rather than a common founder variant.
- No modifier genes have yet been reported; genotype-phenotype correlation across the 5 families is not yet resolved (small n).

**Environmental/lifestyle risk factors:** None identified or plausible — this is a monogenic transcription-factor deficiency, not a multifactorial or exposure-modulated disease. No gene-environment interaction data exist.

**Protective factors:** None described. Heterozygous carriers (unaffected parents in all reported families) show no reported phenotype, consistent with recessive, non-haploinsufficient inheritance for this disease (distinct from *TP73*'s proposed, unrelated, monoallelic-expression/tumor-suppressor role in neuroblastoma, which is a separate biological context — see §4).

---

## 3. Phenotypes

### Respiratory phenotype (present in all 7 reported patients)
| Phenotype | Type | Onset | Frequency (of 7) | Suggested HP term |
|---|---|---|---|---|
| Chronic recurrent respiratory tract infections | Sign/symptom | Neonatal–early childhood | 7/7 | HP:0002205 (Recurrent respiratory infections) |
| Neonatal respiratory distress requiring ventilation | Sign | Neonatal | 4/7 (OP-1693 II1, OP-3039 II1, KI-645 II1, 20DG1336 II1) | HP:0002098 (Respiratory distress) |
| Productive cough | Symptom | Early childhood | Reported in all | HP:0031245 (Productive cough) |
| Chronic rhinitis | Sign | Early childhood | Reported in all | HP:0031417 (Chronic rhinitis) or HP:0012384 |
| Otitis media (recurrent) | Sign | Early childhood | Reported in all | HP:0000388 (Otitis media) |
| Bronchiectasis, mucus plugging, atelectasis | Imaging finding | Progressive | Multiple patients | HP:0002110 (Bronchiectasis), HP:0002099 (Atelectasis) |
| Death from respiratory failure | Outcome | Infancy | 1/7 (20DG1336 II1, died age 2 months) | — |
| **Situs inversus** | — | — | **Absent in all patients** (situs solitus) | — (important negative — distinguishes from classic axonemal PCD) |

### Neurological/CNS phenotype (present in all 7 reported patients)
| Phenotype | Characteristics | Suggested HP term |
|---|---|---|
| Anterior-predominant ("frontoanterior") pachygyria/lissencephaly | Progressive/static malformation, present from birth (developmental) | HP:0007260 (Anterior pachygyria) or HP:0001339 (Lissencephaly) |
| Thin, hypoplastic, or absent corpus callosum | Variable severity across patients | HP:0002079 (Hypoplasia of the corpus callosum) / HP:0001274 (Agenesis of the corpus callosum) |
| Hippocampal dysplasia | Reported in ≥1 patient (OP-3039 II1) | HP:0007364 (Hippocampal malformation) |
| Central (axial) hypotonia | All patients | HP:0008936 (Central hypotonia) |
| Moderate-to-severe cognitive/intellectual impairment | Variable, all patients affected to some degree | HP:0002342 (Intellectual disability) |
| Seizure susceptibility | EEG abnormality noted in ≥1 patient (19DG0120) | HP:0001250 (Seizures) |
| Ventriculomegaly | Prenatal, resolved by age 3 in one patient (OP-1693 II1); overt hydrocephalus notably **absent** in the human cohort (contrasts with mouse model — see §6) | HP:0002119 (Ventriculomegaly) |

**Severity/progression:** The lissencephaly and hypotonia/cognitive impairment are static developmental-malformation phenotypes; the respiratory disease is chronic and can progress to bronchiectasis and, in the most severe neonatal-onset cases, fatal respiratory failure. Frequency is based on n=7, so all frequency bands should be treated with caution (dismech convention: prefer qualitative framing over fabricated FREQUENT/OCCASIONAL percentages absent a larger cohort, per the project's frequency-evidence SOP).

**Quality of life:** No formal QoL instrument (EQ-5D, SF-36) data exist for this specific disease; impact is inferable as substantial (ventilator dependency in infancy, chronic lung disease, moderate–severe developmental impairment) but not separately quantified in the literature.

---

## 4. Genetic/Molecular Information

**Causal gene:** TP73 (HGNC:12003, NCBI Gene 7161, OMIM *601990), chromosome 1p36.32.

**Reported pathogenic variants** (all homozygous, all predicted loss-of-function, disrupting both TAp73 and ΔNp73 isoforms; from Wallmeier et al. 2021, PMID:34077761):
1. Homozygous deletion spanning exons 7–14 (~13.17 kb) — family OP-1693
2. c.1196+1G>A (canonical splice-donor variant, intron retention → premature stop) — families OP-3039 and KI-645
3. c.1459delT, p.Tyr487Thrfs*11 (frameshift) — family 19DG0120
4. c.994C>T, p.Gln332* (nonsense) — families 18DG0963 and 19DG2776 (cousins)
5. c.613G>T, p.Glu205* (nonsense) — family 20DG1336

**Variant classification:** All variants would be classified pathogenic/likely pathogenic under ACMG/AMP criteria (null variant in a gene where LOF is an established disease mechanism, segregation in affected homozygotes, absence/rarity in population databases — gnomAD-level allele frequency data for these specific alleles were not retrieved in this search and should be checked directly against gnomAD before curation).

**Functional consequence:** Complete loss of TP73 protein function (both isoforms) → failure of the TAp73-driven multiciliogenesis transcriptional program (see §6).

**Somatic vs. germline:** Germline only — this is a constitutional Mendelian disorder, unrelated to TP73's somatic tumor-suppressor role in cancers (note: TP73/1p36 is also studied as a candidate tumor-suppressor locus in neuroblastoma and other cancers via a *distinct*, monoallelic-expression mechanism — that biology is not relevant to CILD47 and should not be conflated in curation).

**Modifier genes:** None established.

**Epigenetics:** No disease-specific DNA methylation/chromatin data for TP73-CILD47 were found. Note the general biology: TAp73 itself acts as a master transcriptional activator (not a chromatin modifier per se) of the multiciliogenesis network (FOXJ1, RFX2, RFX3, miR-34bc, and ~50 structural/functional ciliary genes) — see §6.

**Chromosomal abnormalities:** The exon 7–14 deletion in one family is effectively a small structural (contiguous-gene-region) deletion but confined to TP73 itself; no evidence of a broader 1p36 deletion syndrome phenotype overlap was reported.

**HGNC/gene ontology suggestions:** Gene: hgnc:12003 (TP73). Relevant GO molecular function: GO:0003700 (DNA-binding transcription factor activity); GO:0006355 (regulation of DNA-templated transcription).

---

## 5. Environmental Information

No environmental, occupational, toxin, dietary, lifestyle, or infectious-agent contributory factors have been described — this is a monogenic developmental/ciliopathy disorder. Recurrent respiratory infections are a **consequence** of impaired mucociliary clearance (secondary, not causal), typically involving common respiratory pathogens (e.g., *Haemophilus influenzae*, *Pseudomonas aeruginosa*, *Staphylococcus aureus*) as seen generally in PCD/chronic suppurative lung disease, though pathogen-specific data for this particular gene defect were not reported in the primary paper.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular trigger:** Biallelic TP73 LOF → complete loss of TAp73 (and ΔNp73) protein.
2. **Transcriptional failure:** TAp73 normally acts as the central transcriptional regulator of the multiciliogenesis program, acting **downstream of MCIDAS** and **upstream of FOXJ1**, within the Notch1-dependent multiciliated-cell (MCC) differentiation pathway. TAp73 directly activates FOXJ1, RFX2, RFX3, miR-34b/c, and ~50 structural/functional ciliary genes (Nemajerova et al. 2016, *Genes Dev* 30(11):1300, PMID:27257214; a companion paper — Fernández-Alonso, Buscà, et al., PMID:27298333 — independently converged on the same conclusion; Marshall et al. 2016, *Cell Rep* 14(14):2289–300, PMID:26947080).
3. **Cellular consequence — failure of MCC differentiation:** In TP73-deficient human airway epithelial (ALI) cultures: severely reduced FOXJ1-positive and RFX2-positive nuclei; severely reduced numbers of ciliated cells (~20–30% apical MCC coverage vs. ~73% in controls, p<0.0001); markedly shortened residual cilia (~1.5–1.8 µm vs. ~3.8 µm in controls, p<0.0001); occasional basal-body mislocalization within the cytoplasm; and a broader epithelial differentiation defect (epithelial layer height 7–10 µm/2 cell layers vs. 39.9 µm/6 layers in controls) (PMID:34077761).
4. **Functional consequence — impaired mucociliary transport:** Particle-tracking assays showed severely reduced transport velocity and directionality, i.e., a physiologically defective mucociliary escalator — despite grossly **normal axonemal ultrastructure** by electron microscopy (9+2 microtubule arrangement intact; outer dynein arms/DNAH5 and nexin-dynein regulatory complex/GAS8 correctly localized) (PMID:34077761). This distinguishes CILD47 mechanistically from "classical" structural PCD (e.g., DNAH5, CCDC39/40 mutants) — the defect is in **generating enough normal cilia**, not in cilia that are structurally abnormal.
5. **Clinical respiratory consequence:** Chronic impaired mucociliary clearance → recurrent airway infection, bronchiectasis, and (in severe neonatal cases) respiratory failure.
6. **Parallel CNS consequence:** TP73/TAp73 also governs multiciliogenesis and planar cell polarity (PCP) of brain **ependymal cells** and is required for proper corticogenesis. Mouse Trp73-null models show ependymal ciliary and PCP defects, hydrocephalus, hippocampal dysgenesis, and cortical lamination/subventricular-zone (SVZ) architecture abnormalities (Fatt/Gonzalez-Cano et al. lineage of studies: "p73 is required for ependymal cell maturation and neurogenic SVZ cytoarchitecture"; Fuertes-Álvarez et al. 2018, *Cell Death Dis* 9(2):163, "p73 regulates ependymal planar cell polarity by modulating actin and microtubule cytoskeleton," PMID not independently confirmed in this pass — verify before citing; Fujitani et al. 2017, *Sci Rep* 7:12007, "Loss of p73 in ependymal cells during the perinatal period leads to aqueductal stenosis," PMID:28931858). In humans, this maps onto the observed cortical malformation (anterior pachygyria/lissencephaly with corpus callosum hypoplasia/agenesis) — the authors propose that **loss of the same TAp73-driven multiciliogenesis/cytoskeletal program that builds airway MCCs also disrupts a cilia-related process needed for normal neuronal migration/cortical layering**, unifying the dual-organ phenotype under one mechanism rather than two independent gene functions (PMID:34077761).

**Cell types involved:**
- Airway multiciliated epithelial cells (MCCs) — CL:0002145 (ciliated columnar cell of tracheobronchial tree) or CL:1000271 (lung ciliated cell)
- Brain ependymal cells (ciliated, line the ventricles) — CL:0000065 (ependymal cell)
- Cortical neurons / radial glia (migration defect substrate) — CL:0000679 (glutamatergic neuron), CL:0002608 (radial glial cell)

**Suggested GO biological process terms:**
- GO:0035082 (axoneme assembly) — indirectly, via reduced ciliogenesis
- GO:0007368 (determination of left/right symmetry) — notably **not** disrupted (situs solitus preserved), useful negative annotation
- GO:0060271 (cilium assembly)
- GO:0021987 (cerebral cortex development) / GO:0021795 (cerebral cortex cell migration)
- GO:0003356 (regulation of cilium beat frequency involved in ciliary motility) — downstream functional consequence

**Subcellular:** Basal body (GO:0005930 cilium; GO:0032391 photoreceptor connecting cilium is not relevant); centriole/basal body mislocalization is a described cell-biology finding, though core basal-body **number** was preserved (distinguishing from CCNO/MCIDAS-driven centriole-amplification failure — a related but mechanistically distinct RGMC subtype).

**Omics:** No transcriptomic (GEO/ArrayExpress), proteomic, or single-cell datasets specific to human TP73-CILD47 patient tissue were identified in this search; the mechanistic transcription-factor-network data (FOXJ1/RFX2/RFX3/miR-34bc target network) derive primarily from mouse/organoid TAp73 ChIP and knockout transcriptomic studies (PMID:27257214, PMID:26947080).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Respiratory tract (nasal/paranasal sinuses, middle ear, trachea, bronchi, lung parenchyma via airway disease) and central nervous system (cerebral cortex, corpus callosum, hippocampus).
- **Secondary/complication-level:** Lower respiratory tract structural damage (bronchiectasis) as a consequence of chronic infection.
- **Body systems:** Respiratory system and nervous system are the two systems with a documented human phenotype; reproductive system (efferent duct multiciliogenesis, sperm flagella) is affected in other MCIDAS/CCNO/GEMC1 RGMC-family diseases and in Trp73 mouse models (sterility), but human fertility data specific to TP73-CILD47 were not reported (patients are pediatric in the reported cohort).

**Tissue/cell level:**
- Respiratory pseudostratified ciliated epithelium (multiciliated cells) — UBERON:0002185 (bronchial epithelium), UBERON:0001707 (nasal cavity epithelium)
- Ependymal lining of brain ventricles — UBERON:0002316 (ependyma)
- Cerebral cortex (neuronal migration substrate) — UBERON:0000956 (cerebral cortex); UBERON:0002336 (corpus callosum)
- Hippocampus — UBERON:0002421

**Subcellular:** Cilium/axoneme (GO:0005929 cilium), basal body (GO:0005930).

**Localization/laterality:** Situs solitus preserved (no laterality defect) — an important distinguishing negative finding from classical axonemal PCD, where left-right patterning defects (situs inversus/heterotaxy) are common because nodal cilia require normal axonemal dynein function; here nodal cilia function is apparently unaffected, consistent with a selective MCC-differentiation (not axonemal-structural) defect.

---

## 8. Temporal Development

- **Onset:** Congenital for the CNS malformation (developmental, present from birth/prenatally imageable); neonatal-to-early-childhood for respiratory disease onset — several patients presented with respiratory distress in the neonatal period requiring ventilatory support.
- **Onset pattern:** The CNS malformation is a fixed structural defect (not "progressive" in the neurodegenerative sense) but its functional consequences (developmental delay, hypotonia, seizure risk) manifest and are characterized over infancy/childhood. Respiratory disease is chronic and can be insidious/progressive (recurrent infections → bronchiectasis) or acute/severe from birth.
- **Disease course:** Chronic, lifelong for survivors (no described "remission"). One reported death (respiratory failure at 2 months) indicates a severe/fatal end of the phenotypic spectrum.
- **Critical periods:** Neonatal period is the highest-risk window for respiratory decompensation; prenatal/perinatal window is when the cortical malformation is established (developmental, not preventable postnatally).
- No formal staging system exists for this disease given its rarity.

---

## 9. Inheritance and Population

- **Epidemiology:** No dedicated prevalence/incidence estimate exists for CILD47 specifically — only 7 individuals from 5 families have been published (PMID:34077761); it should be treated as ultra-rare/case-series-only. For context, PCD as a whole has classically cited prevalence of ~1 in 10,000–20,000, though a 2022 population-genomic (carrier-frequency-based) analysis of pathogenic variants across 29 PCD genes estimated a much higher global prevalence of ~13.2 per 100,000 (Zariwala/Zhu et al., "The global prevalence and ethnic heterogeneity of primary ciliary dyskinesia gene variants," PMID:35051411) — note TP73 was likely not among the "classical" 29 genes surveyed in earlier PCD gene panels given its 2021 discovery, so this estimate would not capture CILD47-specific carrier frequency.
- **Inheritance pattern:** Autosomal recessive.
- **Penetrance:** Appears complete/full in the reported homozygotes (all 7 affected).
- **Expressivity:** Variable — severity of both the respiratory phenotype (ranging from chronic infections to fatal neonatal respiratory failure) and the CNS phenotype (variable corpus callosum hypoplasia vs. agenesis, variable cognitive impairment severity) across the 7 patients.
- **Consanguinity:** A major contributing factor — most of the 5 founding families were consanguineous, consistent with a rare recessive allele being homozygosed via shared ancestry rather than a common population founder variant (contrast with, e.g., a single recurrent founder mutation).
- **Founder effects:** Not established; the 5 families carry 5 different (largely private) LOF alleles, arguing against a single dominant founder variant, though the c.994C>T (p.Gln332*) variant recurred in two related (cousin) families (18DG0963/19DG2776), consistent with a family-specific founder allele rather than population-wide.
- **Carrier frequency:** Not established for TP73 specifically.
- **Population demographics:** The reported cohort includes patients ascertained via clinical/genetic centers with Middle Eastern (Saudi Arabian — e.g., patient IDs with "19DG"/"20DG" prefixes suggestive of Saudi genomic center nomenclature) and German/European referral patterns, consistent with the multinational, consanguinity-enriched ascertainment typical of ultra-rare AR ciliopathy case series; no formal geographic/ethnic prevalence data exist.
- **Sex ratio / age distribution:** Not reported as skewed; cohort is pediatric (consistent with severe early-onset presentation).

---

## 10. Diagnostics

**General PCD diagnostic framework (per ATS/ERS guidelines), adapted for this syndromic form:**
- **Nasal nitric oxide (nNO):** Standard PCD screening test; low nNO is typical in structural/axonemal PCD. Its behavior in TP73-CILD47 (an MCC-differentiation, not axonemal-structure, defect) was not explicitly reported in the retrieved data and should be checked directly against the primary paper before asserting a specific nNO value/finding.
- **High-speed video microscopy (ciliary beat pattern/frequency):** Would be expected to show reduced/absent ciliary beating due to markedly reduced cilia number and length, though this is inferred from the cell-biology data (particle-tracking dysfunction) rather than a directly quoted clinical HSVA report.
- **Transmission electron microscopy (TEM):** Reported as essentially **normal axonemal ultrastructure** (9+2 arrangement, normal outer dynein arms/DNAH5, normal nexin-dynein regulatory complex/GAS8) — an important diagnostic pitfall, since standard TEM-based PCD diagnosis could be falsely reassuring/normal in this gene defect; diagnosis instead rests on **reduced MCC numbers and ciliary length** (immunofluorescence for FOXJ1/acetylated tubulin) plus **genetic testing**.
- **Genetic testing:** TP73 sequencing (single-gene or as part of an expanded PCD/ciliopathy gene panel) is the definitive diagnostic approach, especially when the combination of PCD-like respiratory disease **plus** lissencephaly is present — this combination should specifically trigger TP73 testing given the described disease. WES/WGS are appropriate given the syndromic (multi-organ) presentation and phenotypic novelty.
- **Brain MRI:** Central to diagnosis of the neurological component — frontoanterior-predominant pachygyria/lissencephaly, thin/absent corpus callosum, ± hippocampal dysplasia.
- **Chest imaging (CT):** Bronchiectasis, mucus plugging, atelectasis.
- **Situs assessment:** Notably normal (situs solitus) — this is diagnostically useful as it can distinguish TP73-CILD47/RGMC-spectrum disease from classical PCD, where situs anomalies occur in ~50% of patients due to nodal cilia dysfunction.

**Differential diagnosis:**
- Other RGMC-spectrum disorders: MCIDAS, CCNO, FOXJ1 (also cause reduced MCC numbers with normal axonemal ultrastructure and normal situs; FOXJ1 pathology can also involve hydrocephalus and, in some reports, laterality defects since FOXJ1 also functions in nodal cilia).
- Classical structural PCD genes (DNAH5, DNAI1, CCDC39, CCDC40, etc.) — distinguished by abnormal TEM/axonemal structure and higher rate of situs anomalies.
- Isolated (non-ciliopathy) lissencephaly syndromes (LIS1/PAFAH1B1, DCX, TUBA1A, ARX) — distinguished by absence of a respiratory/mucociliary phenotype.
- Other syndromic ciliopathies with CNS + respiratory overlap (e.g., some CEP-gene ciliopathies) should be considered in the broader differential.

**Screening:** No population newborn-screening program exists for this ultra-rare condition; prenatal diagnosis/genetic counseling is feasible in known-carrier consanguineous families once a familial variant is identified.

---

## 11. Outcome/Prognosis

- **Mortality:** 1 of 7 reported patients died of respiratory failure at 2 months of age — indicating a potentially high-severity subgroup with neonatal-onset, ventilator-dependent respiratory failure. No formal survival curve/life-expectancy estimate exists given the small cohort.
- **Morbidity:** Chronic lung disease (bronchiectasis) is expected to be lifelong in survivors, analogous to other PCD forms. Neurodevelopmentally, all surviving patients have moderate-to-severe cognitive impairment and central hypotonia; some have seizure risk.
- **Recovery potential:** The cortical malformation is a fixed structural defect with no expected anatomical recovery; developmental outcome depends on the degree of associated intellectual disability and access to supportive/rehabilitative therapy. Respiratory disease, as with other PCD, can be stabilized (not cured) with aggressive airway clearance and infection management, though data specific to long-term respiratory trajectory in TP73-CILD47 beyond the initial case series are not yet available.
- **Prognostic factors:** Severity of the neonatal respiratory presentation (ventilator dependence) appears to correlate with the most severe outcomes (the one death occurred in a neonatal-ventilator-dependent patient); no molecular (variant-type) genotype-severity correlation has yet been established given the small, genetically heterogeneous cohort.

---

## 12. Treatment

No disease-specific (TP73-targeted) therapy exists. Management follows standard **PCD supportive care**, extrapolated from general PCD/RGMC management guidelines, plus standard neurodevelopmental/neurological supportive care for the CNS malformation:

**Respiratory — supportive/standard-of-care:**
- **Airway clearance therapy** (chest physiotherapy, mechanical airway clearance devices) — NCIT:C15315 (Rehabilitation) / a specific airway-clearance NCIT term should be sourced.
- **Mucolytics / hypertonic saline nebulization** — supportive care, NCIT:C15747 (Supportive Care).
- **Prophylactic/therapeutic antibiotics** for recurrent respiratory infections (e.g., macrolides such as azithromycin, used in general PCD/bronchiectasis management for both antimicrobial and anti-inflammatory effect) — NCIT:C15986 (Pharmacotherapy) with therapeutic_agent bound to the specific antibiotic class as appropriate.
- **Ventilatory support** in neonatal/severe presentations (NCIT — mechanical ventilation-type intervention term should be sourced specifically).
- **Otologic management** for recurrent otitis media (e.g., tympanostomy tubes) — surgical/procedural, NCIT:C15329 (Surgical Procedure)-family term.

**Neurological — supportive:**
- **Physical, occupational, and speech therapy** for hypotonia and developmental delay — NCIT:C15302 (Physical Therapy), NCIT:C121351 (Occupational Therapy), NCIT:C159273 (Speech Therapy).
- **Antiepileptic management** if/when seizures manifest — standard pharmacotherapy, agent-specific.
- **Developmental/early intervention services.**

**Advanced/experimental therapeutics:** None reported or in trials specific to TP73-CILD47 (no ClinicalTrials.gov entries identified in this search for this specific gene-disease pair). Gene therapy is not a near-term realistic option given the dual-organ (lung epithelium + CNS developmental) nature of the defect and the fact that the CNS malformation is a fixed prenatal/perinatal structural lesion rather than an ongoing degenerative process amenable to postnatal correction.

**Treatment strategy:** Multidisciplinary (pulmonology, neurology, developmental pediatrics, otolaryngology) supportive management; no published treatment algorithm specific to this gene-disease association exists — management should be extrapolated cautiously from general PCD and general lissencephaly/hypotonia care guidelines, explicitly noted as extrapolated rather than disease-specific evidence.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (monogenic developmental disorder) beyond **genetic counseling** for consanguineous/carrier families with a known familial TP73 variant, and **prenatal diagnosis** (chorionic villus sampling/amniocentesis with targeted variant testing, or prenatal ultrasound/fetal MRI surveillance for cortical malformation) in at-risk pregnancies once the familial variant is known — NCIT:C15240 (Genetic Counseling).
- **Secondary prevention:** Early recognition of the combined respiratory + lissencephaly phenotype should prompt TP73 testing to enable earlier diagnosis, respiratory surveillance, and proactive infection management (reducing risk of the bronchiectasis/respiratory-failure trajectory).
- **Tertiary prevention:** Aggressive airway clearance and infection control aimed at preventing progression to bronchiectasis and respiratory failure in diagnosed patients (extrapolated from general PCD management, not disease-specific evidence).
- **Screening:** No population-level newborn screening exists; carrier screening is only practical within already-identified affected families/consanguineous populations.
- **Immunization:** No disease-specific vaccine strategy, though standard respiratory-pathogen vaccination (influenza, pneumococcal, pertussis-containing) is a reasonable general recommendation by analogy to other chronic suppurative lung diseases, though not specifically documented for this condition.

---

## 14. Other Species / Natural Disease

No naturally occurring TP73-deficient disease has been reported in non-human species (no OMIA entries or veterinary case reports identified in this search). All non-human data derive from **engineered mouse knockout models** (see §15) rather than spontaneously occurring animal disease.

---

## 15. Model Organisms

**Mouse (*Mus musculus*, NCBITaxon:10090) — Trp73 (mouse ortholog) knockout/conditional models** — the primary and extensively characterized model system:

- **Trp73-null mice:** Recapitulate multiple features of the human dual-organ phenotype, unifying several previously separately-described p73-knockout phenotypes under a single ciliogenesis-defect mechanism: chronic respiratory tract infections due to profound ciliogenesis defects and loss of mucociliary clearance, hydrocephalus, hippocampal dysgenesis, sterility, and chronic middle-ear/sinus inflammation (Nemajerova et al. 2016, *Genes Dev*, PMID:27257214; Marshall et al. 2016, *Cell Rep*, PMID:26947080).
- **TAp73 specifically** (the N-terminal transactivating isoform) was shown to be **necessary and sufficient** for basal body docking, axonemal extension, and motility during MCC-progenitor differentiation in mouse organotypic airway (tracheal) cultures, and to directly bind and activate FOXJ1, RFX2, RFX3, and the miR-34bc locus (PMID:27257214).
- **Ependymal-specific conditional models:** Perinatal loss of p73 in ependymal cells leads to **aqueductal stenosis** and disrupted ependymal planar cell polarity (actin/microtubule cytoskeleton), directly implicating the same TAp73-multiciliogenesis axis in the CNS ventricular-lining phenotype relevant to the human lissencephaly/ventricular findings (Fujitani et al. 2017, *Sci Rep* 7:12007, PMID:28931858; related work on p73/ependymal PCP and SVZ neurogenic cytoarchitecture from the same research lineage — cite with direct verification of exact PMIDs before KB entry).
- **Phenotype recapitulation vs. human disease:** The mouse models recapitulate the **airway MCC-differentiation defect and mucociliary clearance failure** well, and support the **mechanistic link** between p73 loss and both ependymal/ciliary and cortical-architecture abnormalities. However, mouse Trp73-null models show more prominent **hydrocephalus** than the reported human cohort (where overt hydrocephalus was largely absent, aside from transient prenatal ventriculomegaly in one patient) — this is a candidate **human-model mismatch** worth flagging explicitly in any dismech curation (per the project's `HUMAN_MODEL_MISMATCH` discussion pattern) rather than assuming full concordance between the mouse hydrocephalus phenotype and the milder human ventricular findings.
- **In vitro human models:** Patient-derived nasal/bronchial air-liquid-interface (ALI) epithelial cultures were the direct human cellular model used in Wallmeier et al. 2021 to demonstrate the MCC-differentiation and ciliary-transport defects described in §6 — this is IN_VITRO (human primary cell) evidence, distinct from the MODEL_ORGANISM (mouse) evidence above, and should be tagged accordingly in any evidence curation.

**Resources:** MGI (Mouse Genome Informatics) holds the Trp73 knockout allele records; no zebrafish, Drosophila, or C. elegans TP73-ortholog disease models specific to this phenotype were identified in this search.

---

## Summary of Key Ontology Term Suggestions (to be independently OAK-verified before KB entry)

| Category | Suggested term(s) |
|---|---|
| Disease | OMIM:619466; gene OMIM:*601990; MONDO ID — **unverified, must be looked up** |
| Gene | hgnc:12003 (TP73) |
| Phenotypes (HP) | Lissencephaly (HP:0001339), Anterior pachygyria, Hypoplasia/agenesis of corpus callosum (HP:0002079 / HP:0001274), Central hypotonia (HP:0008936), Intellectual disability (HP:0002342), Seizures (HP:0001250), Recurrent respiratory infections (HP:0002205), Bronchiectasis (HP:0002110), Otitis media (HP:0000388), Respiratory distress (HP:0002098) |
| Cell types (CL) | Ciliated columnar cell (CL:0002145 / CL:1000271), Ependymal cell (CL:0000065), Radial glial cell (CL:0002608) |
| Biological processes (GO) | Cilium assembly (GO:0060271), Axoneme assembly (GO:0035082), Cerebral cortex development (GO:0021987), Regulation of transcription (GO:0006355) |
| Anatomy (UBERON) | Bronchial epithelium (UBERON:0002185), Ependyma (UBERON:0002316), Cerebral cortex (UBERON:0000956), Corpus callosum (UBERON:0002336) |
| Treatment (NCIT) | Pharmacotherapy (NCIT:C15986), Physical Therapy (NCIT:C15302), Supportive Care (NCIT:C15747), Genetic Counseling (NCIT:C15240) |

---

## Key Primary Citations (PMIDs)

1. **Wallmeier J, Bracht D, Alsaif HS, et al.** Mutations in TP73 cause impaired mucociliary clearance and lissencephaly. *Am J Hum Genet.* 2021;108(7):1318–1329. **PMID:34077761** — the founding/only human clinical-genetic case series (7 patients, 5 families).
2. **Nemajerova A, Kramer D, Siller SS, et al.** TAp73 is a central transcriptional regulator of airway multiciliogenesis. *Genes Dev.* 2016;30(11):1300–1312. **PMID:27257214** — mouse mechanistic model.
3. Companion paper, "Unifying the p73 knockout phenotypes: TAp73 orchestrates multiciliogenesis," *Genes Dev.* 2016. **PMID:27298333** — independent convergent mouse study (verify author list directly before citing).
4. **Marshall CB, Mays DJ, Beeler JS, et al.** p73 Is Required for Multiciliogenesis and Regulates the Foxj1-Associated Gene Network. *Cell Rep.* 2016;14(14):2289–2300. **PMID:26947080**.
5. **Fujitani M, et al.** Loss of p73 in ependymal cells during the perinatal period leads to aqueductal stenosis. *Sci Rep.* 2017;7:12007. **PMID:28931858** — ependymal/CNS mouse mechanistic model.
6. General PCD context: Zariwala MA, Zhu X, et al., global prevalence/gene-variant analysis, **PMID:35051411**; ATS/ERS PCD diagnostic guidelines (multiple; verify exact current PMID before citing, as an updated version was found dated 2026 alongside the earlier 2017/2018 versions).

**Important caveat for dismech curation:** Several of the mechanistic mouse-model PMIDs above (notably the ependymal/PCP lineage of papers) were partially reconstructed from search-result summaries rather than fully verified against the primary abstract text in this pass. Per this project's own DR-verification SOP, **every PMID and snippet listed here must be independently re-verified via `just fetch-reference` and `just validate-references` before being committed to a KB entry** — treat this report as a well-sourced lead set, not pre-verified curation-ready evidence.