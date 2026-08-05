---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-06-30T11:05:52.254759'
end_time: '2026-06-30T11:10:59.071494'
duration_seconds: 306.82
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Hyper-IgE Syndrome
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
  - claude-opus-4-8[1m]
  web_search_requests: 5
  num_turns: 10
  total_cost_usd: 2.1589630000000004
  session_id: 52be64db-4552-416d-82a8-448a251b5ac8
  stop_reason: end_turn
citation_count: 11
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Hyper-IgE Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Hyper-IgE Syndrome** covering all of the
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

I now have enough to write a comprehensive, well-cited report. Here it is.

---

# Comprehensive Research Report: Autosomal Dominant Hyper-IgE Syndrome (AD-HIES / STAT3-HIES / Job Syndrome)

> **A note on citations (important for this knowledge base):** PMIDs below are drawn from the literature and the cited reviews/GeneReviews. Per the dismech DR-verification SOP, every PMID and snippet must be re-fetched with `just fetch-reference PMID:XXXX` and substring-verified before it goes into the YAML — treat the citations here as *leads*, not ground truth. I have flagged confidence where relevant.

---

## 1. Disease Information

**Overview.** Autosomal dominant hyper-IgE syndrome (AD-HIES) is a rare multisystem **primary (inborn-error-of-immunity) immunodeficiency** caused by heterozygous **dominant-negative loss-of-function variants in *STAT3***. It is the prototypic "connective-tissue/immune" inborn error: it couples a recognizable immunologic triad — markedly **elevated serum IgE**, **recurrent "cold" staphylococcal skin abscesses**, and **recurrent pneumonia with pneumatocele formation** — with **non-immune** craniofacial, dental, skeletal, and vascular abnormalities. This combination of an immunodeficiency that also disrupts somatic tissue is what makes STAT3-HIES distinctive among the inborn errors of immunity. The eponym **Job syndrome** (1966, Davis et al., describing girls with "cold" abscesses, after the biblical Job "smitten with sore boils") predates the unified description by **Buckley** (1972, adding the facial/skeletal features and high IgE), and the molecular cause (*STAT3*) was discovered in **2007**.

**Key identifiers.**
- **MONDO:** `MONDO:0007818` — *hyper-IgE recurrent infection syndrome 1, autosomal dominant* (the value already in the YAML; correct).
- **OMIM:** **147060** (HYPER-IgE RECURRENT INFECTION SYNDROME 1, AUTOSOMAL DOMINANT; HIES1). Gene: ***STAT3*** OMIM **\*102582**.
- **Orphanet:** **ORPHA:2314** — *Autosomal dominant hyper-IgE syndrome due to STAT3 deficiency* (under the broader Job syndrome grouping ORPHA:2316).
- **ICD-10:** **D82.4** (Hyperimmunoglobulin E [IgE] syndrome). **ICD-11:** **4A00.20** (Hyper-IgE syndromes).
- **MeSH:** **D007589** (Job Syndrome).
- **HGNC (gene):** `hgnc:11364` (*STAT3*).

**Synonyms / alternative names:** AD-HIES; STAT3-HIES; STAT3 dominant-negative HIES; Job syndrome; Buckley syndrome; HIES type 1; classic/sporadic hyper-IgE syndrome.

**Data source character.** Information is overwhelmingly **disease-level aggregated** (curated cohorts from the NIH, French national survey, GeneReviews, and the international HSCT consortium), not EHR/individual-patient registries. The largest well-phenotyped series are single-center/national cohorts of tens to low-hundreds of molecularly confirmed patients.

---

## 2. Etiology

**Primary cause (genetic).** Heterozygous **germline dominant-negative variants in *STAT3*** (signal transducer and activator of transcription 3), chromosome **17q21.2**. STAT3 is the shared signaling node for a large family of cytokines (IL-6, IL-10, IL-11, IL-21, IL-22, IL-23, G-CSF, leptin, etc.). The mutant allele produces a full-length but non-functional protein that **poisons the wild-type STAT3** in the obligate dimer, so a single mutant allele reduces overall STAT3 activity well below the ~50% expected from simple haploinsufficiency.
- *Holland et al., NEJM 2007* (**PMID:17881745**): "heterozygous … mutations in … STAT3 in the majority of patients with the hyper-IgE syndrome."
- *Minegishi et al., Nature 2007* (**PMID:17676033**): "**Dominant-negative mutations in the DNA-binding domain of STAT3 cause hyper-IgE syndrome.**"
- *Asano et al., J Exp Med 2021* (**PMID:34137790**, PMC8217968): of in-frame variants studied, **128/135 (95%)** were experimentally dominant-negative, and **all 15 out-of-frame** variants were dominant-negative via truncated neoproteins/reinitiation isoforms — i.e., **negative dominance, not haploinsufficiency**, is the unifying mechanism.

**Genetic risk factors.** The disorder is **monogenic and fully penetrant** — there is no separate "susceptibility locus." The relevant genetic facts are the mutational hotspots (below): missense/in-frame deletions clustering in the **DNA-binding domain** and the **SH2 domain** of STAT3.

**Environmental risk factors.** None are required for disease (it is Mendelian). Environmental *triggers of complications* (not of the disease itself) include **colonizing *Staphylococcus aureus***, **Aspergillus/other molds** (which colonize pneumatoceles), and **Candida**. Smoking and recurrent infection accelerate the structural lung disease. No sex predilection (equal M:F).

**Protective factors.** None established at the genetic level. Clinically, **early, lifelong anti-staphylococcal prophylaxis** and **aggressive skin/airway care** are "protective" against the morbidity, and **HSCT** is curative for the immune phenotype (Section 12).

**Gene–environment interaction.** The core G×E story is **STAT3-dependent Th17/IL-17–IL-22 collapse meeting environmental pathogens**: the host is constitutively unable to mount the IL-17/IL-22 mucocutaneous antimicrobial program, so common environmental organisms (*S. aureus*, *Candida albicans*, *Aspergillus*) that are trivial for normal hosts cause recurrent, deep, poorly inflamed infection.

---

## 3. Phenotypes

STAT3-HIES is multisystem. Frequencies vary by cohort (NIH, French survey, US series); ranges are given where sources differ. Suggested HPO terms in brackets.

**Immunologic / infectious (early-onset, often neonatal–infantile):**
- **Markedly elevated serum IgE**, typically **>2000 IU/mL** (peak often ≫10,000); ~**97–100%** at some point (may normalize in adults). `HP:0003212` (Increased circulating IgE concentration). *Onset:* infancy. *Severity:* defining hallmark.
- **Eosinophilia** (>700/µL), ~**80–90%**. `HP:0001880` (Eosinophilia).
- **Recurrent "cold" cutaneous abscesses** (staphylococcal, lacking classic warmth/erythema), ~**>80%**. `HP:0100838` (Recurrent cutaneous abscess formation) / `HP:0002744` (cold abscess concept).
- **Recurrent pneumonia** (S. aureus, S. pneumoniae, H. influenzae) with **pneumatocele/bronchiectasis** from aberrant healing, ~**>85%** pneumonia; pneumatoceles in a large minority. `HP:0006532` (Recurrent pneumonia), `HP:0025428`/`HP:0025427` (pneumatocele), `HP:0002110` (Bronchiectasis). Pneumatoceles then become niches for **Aspergillus/Pseudomonas/non-tuberculous mycobacteria** → fatal hemoptysis/invasive aspergillosis. `HP:0002099` (Asthma not typical; rather chronic pulmonary disease).
- **Chronic mucocutaneous candidiasis** (nails, oral, vaginal), ~**>80%**. `HP:0002728` (Chronic mucocutaneous candidiasis).
- **Newborn/eczematoid dermatitis**, often **first sign within weeks of life**, ~**all**. `HP:0000964` (Eczema) / `HP:0000962` (Hyperkeratosis), `HP:0011123` (papulopustular eruption).
- **Mucocutaneous viral disease** (recurrent HSV, VZV reactivation, molluscum, warts), variable.

**Non-immune connective tissue / skeletal / dental / craniofacial:**
- **Characteristic facies** (emerging by adolescence): facial asymmetry, **prominent forehead**, deep-set eyes, **broad nasal bridge/fleshy nasal tip**, **coarse/"leonine" skin** with prominent pores, prognathism, high-arched palate. ~**80–100%** of adults. `HP:0000271` (Abnormal facial shape), `HP:0000343` (Long philtrum/coarse), `HP:0000218` (High palate).
- **Retained primary (deciduous) teeth** / failure of normal exfoliation, ~**> 50–65%** (US cohort 41%; molecularly-defined series up to 83% delayed). `HP:0006335` (Persistence of primary teeth).
- **Scoliosis**, ~**>60%** (US cohort ~34%). `HP:0002650` (Scoliosis).
- **Minimal-trauma / pathologic fractures and low bone density**, ~**40–50%**. `HP:0002659` (Increased susceptibility to fractures), `HP:0000938` (Osteopenia), `HP:0000939` (Osteoporosis).
- **Joint hyperextensibility / hyperextensible joints**, common. `HP:0001382` (Joint hypermobility).
- **Craniosynostosis** (subset). `HP:0001363`.
- **Degenerative joint disease / osteoarthritis**, adult.

**Neurologic / structural:**
- **Chiari I malformation** in ~**18–20%**. `HP:0002308` (Arnold-Chiari type I).
- **Focal brain hyperintensities** (white-matter lesions) ~**60–70%**, usually clinically silent. `HP:0002518` (Periventricular white matter hyperintensities).
- **Lacunar infarcts/stroke** related to vasculopathy (below).

**Vascular (under-recognized, prognostically important):**
- **Coronary artery tortuosity/ectasia** ~**50%**, **coronary aneurysms** in a substantial fraction (≈**70%** have *some* coronary abnormality in prospective imaging). `HP:0001640` (Cardiomegaly not specific) → better: `HP:0004942` (Aortic aneurysm), `HP:0025019`/coronary-artery aneurysm. *Chandesris et al., Circulation 2012* (**PMID:22456478**).
- **Cerebral / middle-sized artery aneurysms and arterial tortuosity**; risk of **myocardial infarction, subarachnoid hemorrhage, ischemic stroke** even in young, non-atherosclerotic patients.

**GI / other:**
- **Esophageal dysmotility / GERD / eosinophilic esophagitis**, **>50%**. `HP:0002020` (Gastroesophageal reflux), `HP:0002015` (Dysphagia).
- **Gastrointestinal candidiasis, colon perforation/diverticulitis** (reported).

**Onset / severity / progression summary:** dermatitis and infections begin in **infancy**; the somatic (facial, dental, skeletal, vascular) features **accrue with age** and become diagnostic by adolescence/adulthood. Course is **chronic-progressive**, dominated long-term by **structural lung disease** and **vascular events**.

**Quality-of-life impact:** chronic skin disease/pruritus, recurrent infections, repeated hospitalization/surgery, chronic lung disease with exercise limitation, fracture/scoliosis-related disability, dental morbidity, and the psychological burden of a visible facial phenotype. No HIES-specific validated QoL instrument; generic tools (SF-36, EQ-5D, PedsQL) apply.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***STAT3*** (`hgnc:11364`; OMIM \*102582; Ensembl ENSG00000168610; 17q21.2). Encodes a 770-aa transcription factor with N-terminal, coiled-coil, **DNA-binding**, linker, **SH2**, and C-terminal **transactivation** domains.

**Pathogenic variants.**
- **Type/class:** predominantly **missense** substitutions and small **in-frame deletions**; out-of-frame/splice variants occur but act through translation-reinitiation neoproteins (Asano 2021).
- **Mutational hotspots:** cluster in the **DNA-binding domain** (e.g., recurrent **p.Val463del**, **p.Arg382Trp/Gln**, **p.Val637Met** in SH2) and the **SH2 domain**. *Woellner et al., JACI 2010* (**PMID:20004785**, "**Mutations in STAT3 and diagnostic guidelines for hyper-IgE syndrome**") catalogued the spectrum and tied genotype to the clinical/IgE phenotype.
- **Functional consequence:** **dominant-negative** — mutant monomer dimerizes with wild-type and abolishes DNA binding/transactivation; **NOT** simple loss-of-function/haploinsufficiency, and **NOT** gain-of-function (germline *STAT3* GOF causes a distinct early-onset autoimmunity/lymphoproliferation syndrome — a key contrast).
- **Allele frequency:** essentially **absent from gnomAD** (private, often de novo, pathogenic alleles); recurrent hotspot alleles arise independently.
- **Origin:** **germline**; the **majority are de novo** (sporadic), with autosomal dominant transmission when inherited. **Somatic *STAT3* variants** are unrelated (they appear in LGL leukemia / cancers).

**Variant classification (ACMG/AMP).** Recurrent hotspot dominant-negative missense/in-frame variants are typically **Pathogenic/Likely Pathogenic** (PS3 functional, PM1 hotspot, PS4/PP1 if segregating, PM2 absence in gnomAD). ClinVar lists the classic alleles as pathogenic.

**Modifier genes / epigenetics / chromosomal abnormalities.** No established Mendelian modifier genes; phenotypic variability (even within families) is attributed to which STAT3 target pathways are most disrupted and to stochastic/environmental factors. No recurrent epigenetic mechanism or chromosomal rearrangement is implicated — this is a point-mutation disease.

---

## 5. Environmental Information

- **Environmental/occupational toxins:** not causal.
- **Lifestyle:** smoking and poorly controlled airway infection worsen structural lung disease; otherwise non-contributory to onset.
- **Infectious agents (drivers of morbidity, not cause):**
 - ***Staphylococcus aureus*** (NCBITaxon:1280) — dominant skin/lung pathogen; "cold" abscesses, pneumonia, pneumatoceles.
 - ***Candida albicans*** (NCBITaxon:5476) — chronic mucocutaneous candidiasis.
 - ***Aspergillus fumigatus*** (NCBITaxon:746128) and other molds — colonize/invade pneumatoceles; major cause of late mortality (hemoptysis, invasive aspergillosis).
 - ***Pseudomonas aeruginosa***, **non-tuberculous mycobacteria**, ***Pneumocystis jirovecii*** (especially post-transplant or with lung damage), and **herpesviruses (HSV, VZV, EBV)**.

---

## 6. Mechanism / Pathophysiology

**Apex lesion → causal chain.**

**(0) STAT3 dominant-negative dysfunction.** A single heterozygous DNA-binding/SH2-domain variant produces a full-length mutant that dimerizes with wild-type STAT3 and abolishes DNA binding/transactivation across the entire STAT3 cytokine network. *GO terms:* `GO:0007260` (tyrosine phosphorylation of STAT protein, **DECREASED** downstream output — note phosphorylation itself is often preserved; it is **DNA binding/transactivation** that fails), `GO:0007259` (cell surface receptor signaling pathway via JAK-STAT), `GO:0006357` (regulation of transcription). The defect is **upstream** of everything below.

**(1) Collapse of Th17 differentiation → IL-17/IL-22 deficiency (immune arm, the central mechanism).** STAT3 is required downstream of IL-6 and IL-23 for RORγt-driven **Th17** development. *Milner et al., Nature 2008* (**PMID:18337720**): "**impaired T(H)17 cell differentiation**" in AD-HIES. Loss of **IL-17A/F and IL-22** removes the signals that drive **epithelial β-defensin/antimicrobial-peptide production** and **neutrophil recruitment** to skin and lung → susceptibility to ***S. aureus*** and ***Candida***. *Cell types:* `CL:0000899` (Th17 cell), `CL:0000624` (CD4+ αβ T cell), `CL:0000775` (neutrophil), `CL:0000066` (epithelial cell). *GO:* `GO:0072539` (Th17 cell differentiation), `GO:0097400` (interleukin-17-mediated signaling), `GO:0050830` (defense response to Gram-positive bacterium).

**(2) Blunted IL-6 acute-phase / inflammatory signaling.** Impaired IL-6→STAT3 signaling underlies the paradoxically **"cold," under-inflamed** abscesses (reduced systemic inflammatory response despite deep infection) and contributes to defective antibody/affinity-maturation responses. *Holland 2007 (PMID:17881745):* "impaired … responses to … IL-6." *GO:* `GO:0070102` (interleukin-6-mediated signaling pathway), `GO:0006953` (acute-phase response).

**(3) Dysregulated humoral/atopic balance.** Impaired STAT3 (IL-10, IL-21) signaling skews toward **IgE class-switching/atopy** and impairs **memory B-cell** generation and specific antibody responses → high IgE plus functionally poor antibody. *Cell types:* `CL:0000787` (memory B cell), `CL:0000236` (B cell).

**(4) Non-immune connective-tissue/skeletal/dental program failure (somatic arm).** Because STAT3 transduces **IL-11, leptin, and growth-factor** signals in bone, vasculature, and craniofacial tissue, dominant-negative STAT3 disrupts:
 - **Bone:** STAT3 normally restrains osteoclastogenesis; its loss → **increased osteoclast activity, osteopenia, fractures**. *Zhang et al. 2005* (**PMID:15694417**) — hematopoietic STAT3 deletion → increased osteoclastogenesis/osteopenia in mice (MODEL_ORGANISM). *GO:* `GO:0045671`/`GO:0001503` (osteoclast/ossification), cell type `CL:0000092` (osteoclast).
 - **Craniofacial/dental:** impaired **IL-11→STAT3** signaling links to **craniosynostosis, delayed tooth exfoliation, retained primary teeth** (parallels IL11RA-deficiency craniosynostosis; *Nieminen et al., AJHG 2011*, **PMID:21741611**).
 - **Vasculature:** STAT3 deficiency reduces **VEGF/HIF-1α**-dependent vascular maintenance and dysregulates **matrix metalloproteinases (notably MMP-8)** and TGF-β/TNF-α responses → **arterial tortuosity, ectasia, and aneurysm**; mouse data show STAT3/IL-17A blockade worsens aneurysm severity and rupture. *Chandesris et al., Circulation 2012 (PMID:22456478).* `GO:0001525` (angiogenesis), cell types `CL:0000115` (endothelial cell), `CL:0000192` (vascular smooth muscle cell).
 - **Lung architecture:** impaired epithelial repair + MMP dysregulation → **pneumatocele/bronchiectasis** (aberrant post-pneumonia healing) rather than simple infection.

**Upstream vs downstream summary.** STAT3 DN (upstream) → branches into (a) **Th17/IL-17–IL-22 immune-defense failure** (skin/lung/mucosal infection) and (b) **IL-6 acute-phase blunting** (cold abscesses, antibody defects) on the immune side, and (c) **bone/vascular/dental connective-tissue programs** on the non-immune side. All downstream phenotypes trace to the single transcription-factor lesion.

**Molecular profiling.** Transcriptomic studies of patient T cells show loss of STAT3 target-gene induction (RORC, IL17A, IL17F, IL22, retinoic-acid-receptor–related signatures); proteomic/functional assays show **normal STAT3 protein and tyrosine phosphorylation but absent DNA binding** (the basis of the dominant-negative model). No disease-specific metabolomic/lipidomic signature is established.

---

## 7. Anatomical Structures Affected

**Organ/system level (primary):** **skin** (UBERON:0002097), **lung/respiratory tract** (UBERON:0002048; bronchi UBERON:0002185), **immune/hematopoietic system** (UBERON:0002405), **oral cavity/teeth** (UBERON:0001091 tooth), **skeleton** (UBERON:0002481 bone tissue; vertebral column UBERON:0002240), **craniofacial skeleton/skull** (UBERON:0003129).

**Secondary / complication-level:** **cardiovascular system** — **coronary arteries** (UBERON:0001621), **cerebral arteries/aorta** (UBERON:0001637 artery); **central nervous system/brain** (UBERON:0000955) — Chiari I, white-matter lesions; **esophagus/GI tract** (UBERON:0001043) — dysmotility, candidiasis.

**Tissue/cell level:** **epithelium** (skin and airway, `CL:0000066`), **Th17 lymphocytes** (`CL:0000899`), **neutrophils** (`CL:0000775`), **memory B cells** (`CL:0000787`), **osteoclasts** (`CL:0000092`), **vascular endothelial** (`CL:0000115`) and **smooth-muscle** (`CL:0000192`) cells.

**Subcellular level:** STAT3 acts in the **cytoplasm → nucleus** (`GO:0005634` nucleus; `GO:0005829` cytosol); the functional defect is **nuclear DNA binding/transcription** (`GO:0003700` DNA-binding transcription factor activity).

**Localization/lateralization:** infections and abscesses are **multifocal**; vascular and skeletal involvement is typically **bilateral/systemic**; facial features are roughly **symmetric/asymmetric** (facial asymmetry is itself a feature).

---

## 8. Temporal Development

- **Onset:** **congenital/neonatal-infantile** — eczematoid newborn rash and recurrent infections usually within the first weeks–months of life.
- **Pattern:** **chronic**, with **recurrent episodic infections** superimposed.
- **Progression/stages:** *early childhood* — dermatitis, abscesses, pneumonias, candidiasis, high IgE; *adolescence* — emergence of the **characteristic facies, retained teeth, scoliosis, fractures**; *adulthood* — dominated by **chronic structural lung disease** (bronchiectasis/pneumatoceles with mold/Pseudomonas/NTM superinfection) and **vasculopathy** (coronary/cerebral aneurysms), plus **lymphoma** risk.
- **Rate:** slow but cumulative; **lifelong** chronic disease (not self-limited).
- **Critical windows for intervention:** **infancy/childhood** for prophylaxis and dental management; **pre-irreversible-lung-damage** window for considering HSCT; **adult vascular surveillance** (every ~3 years) to pre-empt fatal aneurysmal events.

---

## 9. Inheritance and Population

- **Inheritance:** **autosomal dominant**; **majority de novo** (sporadic). 50% transmission risk per offspring of an affected parent.
- **Penetrance:** **complete/essentially complete**; **expressivity variable** (intra-familial variability in non-immune features).
- **Anticipation / germline mosaicism / founder effects:** no genetic anticipation; **germline/somatic mosaicism** is rare but reported (relevant to recurrence counseling); no classic founder populations — recurrent hotspot alleles arise independently across ethnic groups.
- **Carrier frequency / consanguinity:** not a recessive carrier disease; consanguinity is **not** a risk factor (that points instead to the recessive HIES mimics — DOCK8, etc.).
- **Epidemiology:** **rare; prevalence on the order of ~1 in 1,000,000** (some older estimates ~1:100,000). Hundreds of molecularly confirmed cases worldwide.
- **Demographics:** **no sex predilection** (M:F ≈ 1:1); **reported across all ethnicities/geographies**; no endemic geographic clustering.

---

## 10. Diagnostics

**Clinical scoring.** The **NIH HIES score** (Grimbacher et al., NEJM 1999, **PMID:10053177** — "Hyper-IgE syndrome with recurrent infections—an autosomal dominant multisystem disorder") weights 19 clinical/lab findings; **>40 points** suggests HIES, **<20** makes it unlikely. *Woellner 2010 (PMID:20004785)* refined diagnostic guidelines and showed that **low Th17 counts and the genotype** improve discrimination.

**Laboratory.** **Serum IgE >2000 IU/mL** (often historically much higher); **eosinophilia >700/µL**; **reduced/absent IL-17-producing CD4+ (Th17) cells** by flow cytometry (a strong discriminator); variably impaired specific antibody responses; normal-to-reduced memory B cells.

**Functional/imaging.** **Chest CT** for pneumatoceles/bronchiectasis; **coronary CT/MR angiography and brain MRA** for aneurysm surveillance; **spine imaging** for scoliosis; **DXA** for bone density; **echocardiography**.

**Genetic testing.** The diagnosis is **confirmed by identifying a heterozygous dominant-negative *STAT3* variant**. Approaches: **single-gene *STAT3* sequencing**, **HIES/PID gene panels** (to include *DOCK8*, *PGM3*, *ZNF341*, *IL6ST*/*IL6R*, *SPINK5*, *CARD11*, *ERBIN*, *TGFBR*), or **exome/genome sequencing**. Functional confirmation (absent STAT3 DNA binding / dominant-negative assay) supports VUS reclassification.

**Differential diagnosis** (distinguishing features):
- **DOCK8 deficiency (AR-HIES):** severe cutaneous viral infections (HSV, HPV, molluscum), allergies, **early malignancy**, *no* connective-tissue/skeletal/retained-teeth features. → genetics.
- **STAT3 gain-of-function:** early autoimmunity, lymphoproliferation, enteropathy — opposite mechanism.
- **PGM3 deficiency, ZNF341 (AR STAT3-pathway), IL6ST/IL6R defects, Comèl-Netherton (SPINK5), Wiskott-Aldrich, Omenn, atopic dermatitis with high IgE.**

**Screening.** Not part of routine newborn screening (TREC-based NBS misses HIES). **Cascade testing** of relatives for a known familial variant; prenatal/PGT possible when the familial variant is known.

---

## 11. Outcome / Prognosis

- **Life expectancy:** historically reduced; with modern prophylaxis many reach adulthood, but **median survival is shortened**, driven by **pulmonary complications** and **vascular events**.
- **Leading causes of death:** **invasive pulmonary fungal infection / hemoptysis** from pneumatocele/bronchiectasis (Aspergillus, Pseudomonas, NTM), and **vascular catastrophe** (MI, aneurysm rupture, ischemic/hemorrhagic stroke).
- **Malignancy:** increased risk, chiefly **non-Hodgkin lymphoma** (and EBV-associated lymphoma); surveillance for lymphadenopathy advised.
- **Morbidity:** chronic lung disease, recurrent fractures/scoliosis, dental disease, repeated surgery.
- **Prognostic factors:** extent of **established structural lung damage**, fungal colonization, and presence/severity of **vasculopathy**.
- **Surveillance (per GeneReviews):** **coronary + cerebral vascular imaging every ~3 years in adults**; dental review every 6–12 months in childhood; scoliosis monitoring through adolescence; periodic lung imaging and malignancy vigilance.

---

## 12. Treatment

**Conventional / supportive (lifelong).**
- **Antistaphylococcal prophylaxis:** **trimethoprim-sulfamethoxazole** (cotrimoxazole) is standard; treat exacerbations with anti-staph agents. *MAXO:* `MAXO:0000058`/`MAXO:0000059` (antibiotic/antimicrobial therapy). *CHEBI:* trimethoprim `CHEBI:45924`, sulfamethoxazole `CHEBI:9332`.
- **Antifungal prophylaxis/therapy:** **itraconazole/voriconazole/posaconazole** for Aspergillus and CMC; **fluconazole** for Candida. *MAXO:* antifungal agent therapy; *CHEBI:* itraconazole `CHEBI:6076`, fluconazole `CHEBI:46081`.
- **Skin care:** **bleach (sodium hypochlorite) baths, chlorhexidine, topical antiseptics/emollients**, antihistamines for pruritus. *MAXO:* `MAXO:0000511`/topical therapy concepts.
- **Immunoglobulin replacement (IVIG/SCIG):** for selected patients with poor specific antibody/hypogammaglobulinemia (benefit limited/uncertain). *MAXO:* `MAXO:0000841` (immunoglobulin therapy concept).
- **Pulmonary:** airway clearance, aggressive treatment of bronchiectasis; surgical resection of complicated pneumatoceles is **high-risk** and selective. *MAXO:* `MAXO:0000004` (surgical procedure).
- **Skeletal/dental:** bisphosphonates for low bone density (case-based), orthopedic management of scoliosis/fractures, **timely extraction of retained primary teeth**.
- **Vascular:** risk-factor control and surveillance; aneurysm management per cardiology/neurosurgery.

**Curative — allogeneic HSCT.** Increasingly used and the only therapy that **corrects the immune phenotype** (abolishes infections/abscesses, stabilizes lung disease); it does **not reverse established non-immune features** (skeletal/dental/connective tissue), and its effect on **vasculopathy is uncertain** (vascular events still reported post-HSCT).
- *Worldwide HSCT study (Blood Advances, 2025):* **41 patients**, median age at HSCT **14 y**, **5-year overall survival 93%**, **event-free survival 90%**, with **~87% free of bacterial/fungal respiratory infection** afterward.
- *Harrison/Gennery et al. (J Clin Immunol 2021, PMC8249289):* "**Hematopoietic stem cell transplantation resolves the immune deficit associated with STAT3-dominant-negative hyper-IgE syndrome.**"
- *MAXO:* `MAXO:0010039` (organ/HSCT transplantation), `MAXO:0000827`-type bone-marrow-transplant concepts.

**Experimental / future.** Gene-correction (CRISPR/base-editing of the dominant-negative allele, or allele-specific knockdown to relieve negative dominance) is conceptually attractive but **preclinical only**; no approved targeted/RNA therapy exists. **Pharmacogenomics:** azole–drug interactions (CYP3A4) and TMP-SMX hypersensitivity are the practical PGx concerns.

**Treatment strategy.** Lifelong prophylaxis + skin/airway care from diagnosis; multidisciplinary surveillance (pulmonary, vascular, dental, skeletal, oncologic); **consider HSCT before irreversible lung damage**, weighing transplant risk against progressive infection.

---

## 13. Prevention

- **Primary prevention:** none possible (Mendelian); **genetic counseling** and reproductive options (PGT/prenatal testing) when a familial variant is known. *MAXO:* `MAXO:0000079` (genetic counseling).
- **Secondary prevention:** **early diagnosis** (Th17 flow + STAT3 sequencing in a child with neonatal eczema, abscesses, high IgE) enables prophylaxis before lung damage; **cascade testing** of at-risk relatives.
- **Tertiary prevention (preventing complications):** **antibacterial/antifungal prophylaxis**, **skin antisepsis**, **vaccination** (per IEI guidance; avoid live vaccines if significantly immunocompromised/transplanted), **vascular and malignancy surveillance**, dental and scoliosis management — the core of day-to-day care.
- **Immunization:** standard inactivated vaccines recommended; live-vaccine caution.
- **Behavioral/public-health/environmental:** smoking avoidance, mold-exposure reduction, prompt infection treatment.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** STAT3-HIES as a clinical entity is **human (NCBITaxon:9606)**; no naturally occurring animal counterpart is catalogued in OMIA as a recognized "Job syndrome."
- **Orthologous gene:** ***Stat3*** is **highly conserved** — mouse *Stat3* (NCBI Gene 20848), rat, zebrafish *stat3* orthologs exist. STAT3 is essential and conserved from invertebrates onward.
- **Veterinary/natural disease:** no established spontaneous animal model of this specific dominant-negative HIES; relevance is via engineered models (Section 15).
- **Evolutionary conservation:** the **IL-6/IL-23→STAT3→Th17/IL-17** axis and STAT3's connective-tissue roles are deeply conserved, which is why mouse models recapitulate core features.

---

## 15. Model Organisms

- **Mouse (Mus musculus, MGI):** the primary system. **Constitutive *Stat3* knockout is embryonic lethal**, so disease modeling uses **conditional/tissue-specific deletions** and **knock-in of human dominant-negative alleles**:
 - **Hematopoietic/T-cell-specific *Stat3* deletion** → impaired Th17, defective IL-17/IL-22, mucocutaneous infection susceptibility (models the immune arm).
 - **Dominant-negative STAT3 knock-in** mice reproduce **reduced Th17 and infection phenotypes**.
 - **Osteoclast/bone:** hematopoietic *Stat3* deletion → **increased osteoclastogenesis and osteopenia** (*Zhang 2005, PMID:15694417*) — models the fracture/bone phenotype.
 - **Vascular:** STAT3/IL-17A blockade **worsens aneurysm severity and causes fatal rupture** in mouse aneurysm models — supports the vasculopathy mechanism.
- **In vitro / cellular:** patient **PBMC/CD4+ T-cell cultures** (absent Th17 differentiation, preserved STAT3 phosphorylation but absent DNA binding); **patient-derived iPSCs** and reporter assays used to demonstrate dominant-negative inhibition of wild-type STAT3 (the functional assay underpinning *Asano 2021*, PMID:34137790).
- **Phenotype recapitulation:** mouse models reproduce **Th17/IL-17 immune deficits and the bone/vascular arms well**; they **incompletely reproduce the full human craniofacial/dental "facies"** and the precise human pneumatocele biology.
- **Resources:** MGI (Stat3 alleles), IMPC/KOMP conditional alleles, patient cell repositories; Cellosaurus for patient lines.

---

## Consolidated Ontology Term Suggestions (for KB population)

- **Disease:** `MONDO:0007818`. **Gene:** `hgnc:11364` (STAT3).
- **HPO (key):** `HP:0003212` (↑IgE), `HP:0001880` (eosinophilia), `HP:0100838` (recurrent cutaneous abscess), `HP:0006532` (recurrent pneumonia), `HP:0002110` (bronchiectasis), `HP:0002728` (chronic mucocutaneous candidiasis), `HP:0000964` (eczema), `HP:0006335` (persistence of primary teeth), `HP:0002650` (scoliosis), `HP:0002659` (↑fracture susceptibility), `HP:0000938` (osteopenia), `HP:0001382` (joint hypermobility), `HP:0002308` (Chiari I), `HP:0000271` (abnormal facial shape), `HP:0000218` (high palate), `HP:0002020` (GERD), aortic/coronary aneurysm terms (`HP:0004942` and coronary-artery-aneurysm terms).
- **GO (processes):** `GO:0072539` (Th17 differentiation), `GO:0097400` (IL-17 signaling), `GO:0070102` (IL-6 signaling), `GO:0007259` (JAK-STAT signaling), `GO:0003700` (DNA-binding TF activity), `GO:0050830` (defense response to Gram-positive bacterium), `GO:0001525` (angiogenesis).
- **CL (cells):** `CL:0000899` (Th17), `CL:0000775` (neutrophil), `CL:0000787` (memory B cell), `CL:0000066` (epithelial cell), `CL:0000092` (osteoclast), `CL:0000115` (endothelial cell).
- **UBERON:** `UBERON:0002097` (skin), `UBERON:0002048` (lung), `UBERON:0001621` (coronary artery), `UBERON:0000955` (brain), `UBERON:0002481` (bone tissue), `UBERON:0001091` (tooth).
- **CHEBI (drugs):** trimethoprim `CHEBI:45924`, sulfamethoxazole `CHEBI:9332`, itraconazole `CHEBI:6076`, fluconazole `CHEBI:46081`.
- **MAXO (treatments):** `MAXO:0000058`/antimicrobial therapy, antifungal therapy, `MAXO:0010039` (transplantation/HSCT), `MAXO:0000079` (genetic counseling), `MAXO:0000004` (surgery).

---

## Key Citations (verify before YAML use)

| Claim | Citation | PMID (verify) | Evidence type |
|---|---|---|---|
| STAT3 mutations cause AD-HIES; impaired IL-6 | Holland et al., NEJM 2007 | **17881745** | HUMAN_CLINICAL |
| Dominant-negative STAT3 DNA-binding-domain mutations | Minegishi et al., Nature 2007 | **17676033** | HUMAN_CLINICAL / IN_VITRO |
| Impaired Th17 differentiation | Milner et al., Nature 2008 | **18337720** | HUMAN_CLINICAL / IN_VITRO |
| Mutation spectrum + diagnostic guidelines | Woellner et al., JACI 2010 | **20004785** | HUMAN_CLINICAL |
| Negative dominance is unifying mechanism (in/out-of-frame) | Asano et al., J Exp Med 2021 | **34137790** | IN_VITRO |
| NIH HIES clinical score / multisystem AD disorder | Grimbacher et al., NEJM 1999 | **10053177** | HUMAN_CLINICAL |
| French national survey, molecular/clinical features | Chandesris et al., Medicine 2012 | **22751495** | HUMAN_CLINICAL |
| Widespread vascular abnormalities (coronary/cerebral aneurysms) | Chandesris et al., Circulation 2012 | **22456478** | HUMAN_CLINICAL |
| STAT3 deletion → osteoclastogenesis/osteopenia | Zhang et al., 2005 | **15694417** | MODEL_ORGANISM |
| IL-11/STAT3 craniosynostosis/tooth eruption link | Nieminen et al., AJHG 2011 | **21741611** | HUMAN_CLINICAL |
| HSCT resolves immune deficit | Harrison/Gennery et al., J Clin Immunol 2021 | (PMC8249289) | HUMAN_CLINICAL |
| Worldwide HSCT outcomes (5-yr OS 93%) | Blood Advances 2025 | (in press) | HUMAN_CLINICAL |
| GeneReviews STAT3 HIES (criteria, surveillance, prevalence) | Hsu/Davis/Puck/Holland/Freeman | Bookshelf NBK25507 | OTHER (review) |

**Sources consulted:**
- [Human STAT3 variants underlie AD-HIES by negative dominance (J Exp Med 2021, PMC8217968)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8217968/)
- [STAT3 Hyper IgE Syndrome — GeneReviews (NBK25507)](https://www.ncbi.nlm.nih.gov/books/NBK25507/)
- [STAT3 and the Hyper-IgE syndrome — review (PMC3710320)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3710320/)
- [STAT3 Hyper-IgE Syndrome—an Update and Unanswered Questions (J Clin Immunol 2021)](https://link.springer.com/article/10.1007/s10875-021-01051-1)
- [HSCT for STAT3 HIES: a worldwide study (Blood Advances 2025, PMC12359223)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12359223/)
- [HSCT resolves the immune deficit in STAT3-DN HIES (PMC8249289)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8249289/)
- [HSCT and vasculopathy in STAT3-DN HIES (Front Pediatr 2020, PMC7511721)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7511721/)
- [French national survey (PubMed 22751495)](https://pubmed.ncbi.nlm.nih.gov/22751495/)
- [Mutations in STAT3 and diagnostic guidelines (JACI / Woellner)](https://www.jacionline.org/article/S0091-6749(09)01637-6/fulltext)
- [The genetics of hyper-IgE syndromes (Front Immunol 2025)](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1516068/full)
- [Orphanet: AD hyper-IgE syndrome due to STAT3 deficiency (ORPHA:2314)](https://www.orpha.net/en/disease/detail/2314)

---

**Bottom line for the KB entry:** the existing YAML's framing (dominant-negative STAT3 → Th17/IL-17–IL-22 collapse + blunted IL-6 + connective-tissue/skeletal/vascular disruption) is mechanistically correct and well-supported. The richest additions to make are: the **vasculopathy arm** (coronary/cerebral aneurysms, MMP-8/VEGF-HIF mechanism, ~3-yearly surveillance), the **bone/dental/craniofacial** non-immune phenotypes with frequencies, the **NIH diagnostic score + low Th17** diagnostic pillar, the **lymphoma** risk, and **HSCT** as the curative-for-immune-phenotype treatment. Remember to re-fetch and substring-verify every PMID with `just fetch-reference` before committing snippets.