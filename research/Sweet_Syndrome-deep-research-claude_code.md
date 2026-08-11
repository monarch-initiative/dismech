---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-07-01T08:45:07.033396'
end_time: '2026-07-01T08:50:16.578993'
duration_seconds: 309.55
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Sweet Syndrome
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
  web_search_requests: 10
  num_turns: 14
  total_cost_usd: 2.319576
  session_id: 7a79d0c1-a1bc-43ed-ab20-e45b219149e9
  stop_reason: end_turn
citation_count: 12
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sweet Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Sweet Syndrome** covering all of the
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

I now have well-grounded, citable material. Here is the complete research report.

---

# Comprehensive Research Report: Sweet Syndrome (Acute Febrile Neutrophilic Dermatosis)

> **Curation note on evidence:** All PMIDs/PMCIDs below were surfaced and cross-checked through live literature search during this research. Before any snippet is committed to a dismech evidence item, it must still be run through `just fetch-reference` and `just validate-references` — the exact-quote snippets I flag as **[verify snippet]** are paraphrases from secondary sources (UpToDate/StatPearls/PMC full-text summaries) and are *leads*, not validated abstract quotes. Sweet syndrome is a **complex, non-Mendelian** disease, so most content is aggregated disease-level knowledge (reviews, cohorts, registries), not individual-patient genomic data.

---

## 1. Disease Information

**Overview.** Sweet syndrome (SS), or **acute febrile neutrophilic dermatosis**, is an uncommon reactive inflammatory (autoinflammatory-spectrum) skin disorder defined by the abrupt onset of tender, edematous, erythematous-to-violaceous papules, plaques, and nodules, typically accompanied by fever, peripheral neutrophilia, and a dense dermal neutrophilic infiltrate on biopsy **without leukocytoclastic vasculitis**. It responds dramatically to systemic corticosteroids. It was first described by the British dermatologist Robert Douglas Sweet in 1964 (Sweet RD, *Br J Dermatol* 1964;76:349–356, **PMID:14201182**).

**Key identifiers.**
- **MONDO:** `MONDO:0011959` (sweet syndrome) — this is the correct MONDO ID for the dismech entry (the template's "MONDO ID: (if available)" field). Related grouping term for neutrophilic dermatoses exists separately.
- **Orphanet:** `ORPHA:3243`
- **MeSH:** `D016463` (Sweet Syndrome)
- **ICD-10:** `L98.2` (Febrile neutrophilic dermatosis [Sweet])
- **ICD-11:** `EB21.1` (Acute febrile neutrophilic dermatosis)
- **OMIM:** `608068` — **Sweet syndrome, familial** (a rare autosomal-dominant familial form; note that most SS is *not* Mendelian and has no OMIM number). **UMLS:** C0085077.
- **SNOMED CT:** 84625002 (Acute febrile neutrophilic dermatosis).

**Synonyms / alternative names:** acute febrile neutrophilic dermatosis; Gomm-Button disease (historical eponym after Sweet's first two patients); neutrophilic dermatosis, acute febrile. Recognized variants: **classical/idiopathic SS**, **malignancy-associated (paraneoplastic) SS**, **drug-induced SS**; histological/clinical variants include **histiocytoid SS**, **subcutaneous SS** (neutrophilic panniculitis), **bullous/necrotizing SS**, and **neutrophilic dermatosis of the dorsal hands**.

**Data provenance:** Aggregated disease-level (Orphanet, OMIM, MeSH, review articles, single-center cohorts). No large EHR/registry-level individual-patient dataset dominates; cohort sizes are typically 50–100 patients.

*Sources:* Cohen PR, *Orphanet J Rare Dis* 2007;2:34 (**PMID:17655751**, PMC1963326); Orphanet ORPHA:3243; MONDO:0011959 (Monarch Initiative).

---

## 2. Etiology

Sweet syndrome is best conceptualized as a **hypersensitivity/reactive process** — an aberrant, cytokine-driven activation and recruitment of neutrophils triggered by an antecedent immunologic stimulus, rather than a primary infection of the skin. The three etiologic settings:

**Disease causal factors / triggers by subtype:**
1. **Classical/idiopathic (~70–80% of cases):** Frequently preceded (1–3 weeks prior) by **upper respiratory tract or gastrointestinal infection**; associated with **inflammatory bowel disease** (Crohn, ulcerative colitis), **autoimmune connective-tissue disease**, **pregnancy**, and **vaccination**.
2. **Malignancy-associated (~15–20%):** Paraneoplastic; **hematologic malignancy predominates, most commonly acute myeloid leukemia (AML)**, then myelodysplastic syndrome (MDS); also CML, lymphoma, multiple myeloma; solid tumors (GU, breast, GI) less often. SS may be the **presenting sign** of an occult hematologic malignancy or herald relapse.
3. **Drug-induced:** Best-established culprit is **granulocyte colony-stimulating factor (G-CSF/filgrastim)**; also all-trans retinoic acid (ATRA), trimethoprim-sulfamethoxazole and other antibiotics, azathioprine, bortezomib, imatinib, lenalidomide, ipilimumab and other immune-checkpoint inhibitors (e.g., pembrolizumab), hydralazine, furosemide, NSAIDs, oral contraceptives, and certain antiepileptics.

**Risk factors.**
- *Environmental/clinical:* female sex, age 30–60, antecedent infection, underlying malignancy (esp. myeloid), autoimmune/inflammatory disease, pregnancy, recent culprit-drug exposure.
- *Genetic/susceptibility:* Not a classic monogenic disease. Reported associations/leads: **MEFV** (Mediterranean fever) variants — a case with **compound heterozygous MEFV mutations** links SS to the familial-Mediterranean-fever autoinflammatory axis (PMC4599868); **HLA associations** have been proposed but are inconsistent; rare **familial SS** (OMIM 608068). A newly recognized major genocopy/mimic is **VEXAS syndrome** (somatic *UBA1* mutation) — see §4.

**Protective factors:** None specifically established (genetic or environmental). By definition, removal/treatment of the trigger (culprit drug withdrawal, treatment of the underlying malignancy or infection) leads to resolution — the closest analog to a "protective" intervention.

**Gene–environment interaction:** The prevailing model is that a susceptible host (autoinflammatory predisposition, e.g., inflammasome/IL-1 pathway priming via MEFV variants, or a clonal myeloid population as in VEXAS/MDS/AML) mounts an exaggerated neutrophilic response to an environmental trigger (infection, drug, tumor antigen). This is analogous to a smoke detector wired too hot: the same puff of environmental smoke that a normal system ignores sets off the whole building's alarm.

*Sources:* PMID:17655751; StatPearls NBK431050; PMC4599868 (MEFV); systematic review PMC11660222.

---

## 3. Phenotypes

Below, phenotypes are grouped with suggested **HPO** terms, typical characteristics, and frequency. Onset is **adult** (typically 30–60 y); the disease course is **acute/episodic** with a tendency to **recur**.

| Phenotype (type) | HPO suggestion | Frequency / characteristics |
|---|---|---|
| Tender erythematous papules/plaques/nodules (cutaneous sign) | HP:0000988 *Abnormal skin morphology* / HP:0011123 *Inflammatory abnormality of the skin*; HP:0200035 *Papule*; HP:0100650? (plaque) | Defining feature; ~100%. Abrupt onset, asymmetric, favoring face, neck, upper limbs; "pseudovesicular"/juicy plaques |
| Fever | **HP:0001945** *Fever* | 30–80% (reported "50–80%" classically); often precedes/accompanies eruption |
| Neutrophilic leukocytosis | **HP:0011897** *Neutrophilia* / HP:0001974 *Leukocytosis* | Common (~60–70%); a diagnostic minor criterion; **may be absent** in malignancy-associated SS with marrow failure |
| Elevated ESR / CRP | HP:0025464 *Elevated circulating C-reactive protein concentration*; HP:0003565 *Elevated erythrocyte sedimentation rate* | Very frequent; diagnostic minor criterion |
| Arthralgia / arthritis | **HP:0002829** *Arthralgia* / HP:0001369 *Arthritis* | ~30–60%; **its absence is associated with malignancy** |
| Ocular involvement (conjunctivitis, episcleritis, scleritis, uveitis) | **HP:0000509** *Conjunctivitis*; HP:0100534 (episcleritis); HP:0000554 *Uveitis* | Conjunctivitis most common; broad spectrum incl. peripheral ulcerative keratitis, iritis |
| Oral/mucosal lesions | HP:0000155 *Oral ulcer* | More common in malignancy-associated SS |
| Pathergy (lesions at trauma sites) | HP:0025614? (pathergy) | Reported; overlaps with pyoderma gangrenosum |
| Malaise / headache / myalgia | HP:0002027, HP:0002315, HP:0003326 | Common constitutional symptoms |
| Extracutaneous neutrophilic infiltration (see §7) | organ-specific HP terms | Up to ~50% of cases |

**Severity/progression:** Individual lesions are **self-limited** but the syndrome is **episodic/recurrent** (recurrence up to ~50%, higher in malignancy/IBD-associated cases). Lesions heal without scarring (except bullous/ulcerative variants). 

**Quality-of-life impact:** Painful eruptions, fever, and arthralgia impair daily functioning acutely; in paraneoplastic cases the driving concern is the underlying malignancy. No SS-specific validated QoL instrument; generic dermatology tools (DLQI) or SF-36 would apply. Formal QoL data are sparse.

*Sources:* von den Driesch P, *J Am Acad Dermatol* 1994 (PMID:8113453); PMID:17655751; PMID:29107342 (83-patient cohort: arthralgia absence, cytopenias associated with malignancy); StatPearls NBK431050.

---

## 4. Genetic / Molecular Information

Sweet syndrome is **predominantly non-Mendelian**; genetics matters chiefly through (a) rare familial forms, (b) autoinflammatory susceptibility genes, and (c) **clonal somatic mutations** in the malignancy/MDS-associated setting.

**Causal / associated genes and variants:**
- **UBA1 (HGNC:12469) — VEXAS syndrome (the transformative recent finding).** Somatic mutations at **methionine-41 (p.Met41)** in *UBA1* (X-linked, encoding the E1 ubiquitin-activating enzyme) cause **VEXAS** (Vacuoles, E1 enzyme, X-linked, Autoinflammatory, Somatic; **OMIM 301054**), an adult-onset autoinflammatory disease in which **Sweet-like neutrophilic dermatosis is the most typical cutaneous histology**. Genotype–phenotype: **p.Met41Leu** carriers frequently show Sweet-like neutrophilic lesions (~82%), whereas **p.Met41Val** more often gives vasculitic lesions (~55%); the dermal infiltrate is derived from the **UBA1-mutated myeloid clone** (PMC11170453). Variant type: somatic missense; origin: **somatic (acquired, myeloid-restricted)**; consequence: hypomorphic loss of canonical cytoplasmic UBA1b isoform → activated innate immunity. VEXAS is a critical mimic to exclude in older men with "refractory Sweet syndrome" + macrocytic anemia/cytopenias.
- **MEFV (HGNC:6998) — pyrin/inflammasome axis.** Compound heterozygous *MEFV* mutations reported in SS, linking it to the familial-Mediterranean-fever/IL-1 autoinflammatory spectrum (PMC4599868). Variant type: missense; origin: germline.
- **Familial Sweet syndrome (OMIM 608068):** rare autosomal-dominant inheritance reported; molecular basis not fully defined.
- **PIK3R1 (HGNC:8979):** a **gain-of-function PIK3R1 variant** in neutrophils from a refractory-SS patient increased IL-1R1 expression and neutrophil migration (reported in the systematic review PMC11660222) — mechanistic, single-case, functional-genomics lead.
- **Clonal myeloid drivers (paraneoplastic SS):** in AML/MDS-associated SS the skin infiltrate can share cytogenetic/molecular abnormalities of the marrow clone (e.g., trisomy 8 associations with MDS/Behçet-overlap neutrophilic disease); these are **somatic** and tumor-derived rather than SS-causal per se.

**Allele frequencies:** *UBA1* p.Met41 variants are somatic (absent/negligible in germline gnomAD). *MEFV* variants (e.g., M694V, V726A) are common founder alleles in Mediterranean populations (gnomAD-documented) but are susceptibility, not causal, for SS.

**Modifier genes:** none robustly established. **Epigenetics:** no well-defined DNA-methylation/histone signature specific to SS (a genuine knowledge gap). **Chromosomal abnormalities:** trisomy 8, del(5q), and other MDS/AML karyotypes appear in the associated hematologic disease.

**Suggested annotations:** genes HGNC UBA1 (hgnc:12469), MEFV (hgnc:6998), PIK3R1 (hgnc:8979), CSF3/CSF3R (G-CSF axis); GENO for somatic vs germline.

*Sources:* Beck DB et al. (VEXAS, *N Engl J Med* 2020, foundational — **verify PMID**); PMC11170453 (VEXAS skin/genotype); OMIM 301054; PMC4599868 (MEFV); PMC11660222 (PIK3R1, molecular review).

---

## 5. Environmental Information

- **Infectious triggers:** antecedent **upper respiratory tract infection** and **gastrointestinal infection** are the classic prodromes of classical SS (e.g., *Streptococcus*, *Yersinia*, *Salmonella* enterocolitis have been implicated); reported associations with HIV, viral hepatitis, and secondary syphilis. These are **triggers**, not direct skin pathogens (the infiltrate is **sterile**). Suggested NCBI Taxonomy anchors only where a specific organism is documented per case.
- **Drug/chemical exposures (see §2):** G-CSF is the flagship; also ATRA, TMP-SMX, azathioprine, bortezomib, checkpoint inhibitors, hydralazine, furosemide, minocycline, NSAIDs, oral contraceptives. (CTD-type chemical→disease links.) CHEBI anchors: G-CSF (protein, not CHEBI), all-trans retinoic acid CHEBI:15367, azathioprine CHEBI:2948, bortezomib CHEBI:52717.
- **Lifestyle factors:** no established smoking/diet/alcohol causal link. Pregnancy is a recognized (physiologic, not lifestyle) trigger.

*Sources:* PMID:17655751; StatPearls NBK431050.

---

## 6. Mechanism / Pathophysiology

**Central causal chain (upstream → downstream):**

1. **Trigger / priming** (infection antigen, drug, tumor-derived cytokines, or a clonal myeloid population) →
2. **Cytokine dysregulation with a G-CSF and IL-1 core.** **G-CSF** is a "major player" driving neutrophil production, survival, and activation across all three subtypes; serum G-CSF rises in active disease (e.g., 390 pg/mL active vs 14 pg/mL inactive) (PMC11660222). The **IL-1β/inflammasome pathway** is a key initiating hub — lesional **IL-1β transcript up to >250-fold** over unaffected skin, though elevation is seen in only a subset of patients (selective inflammasome hyperactivation) (PMC11660222). This is why **IL-1 blockade (anakinra)** works (PMC3953233).
3. **Th1 / IL-17 skewing.** Up-regulation of **IL-12, IL-15, interferon-γ (Th1)** and the **IL-17 axis** (IL-17 + receptor, epidermal IL-17E) contributes an adaptive-immune layer (PMC11660222).
4. **Neutrophil chemotaxis and recruitment.** **IL-6** (up to ~4988 pg/mL in active serum, normalizing after steroids), **IL-8/CXCL8**, and chemokines **CXCL1/2/3 and CXCL16** are overexpressed in lesional tissue, recruiting neutrophils into the dermis (PMC11660222).
5. **Dense sterile dermal neutrophilic infiltration → tissue edema and clinical plaques.** Histology: diffuse mature-neutrophil infiltrate in the reticular dermis, marked papillary-dermal edema, and interstitial **leukocytoclasis (karyorrhectic nuclear debris)**, characteristically **without true vasculitis** (secondary/subtle vascular change may occur). Epidermis usually spared. In the **histiocytoid variant**, the infiltrate is **immature myeloid cells / M2-like CD68+CD163+ macrophages** rather than mature neutrophils — important because it mimics leukemia cutis and flags MDS/AML.
6. **Extracutaneous "sterile neutrophilic infiltration"** of other organs when systemic (§7).

**Cellular processes / GO suggestions:** neutrophil chemotaxis (**GO:0030593**), neutrophil migration (**GO:1990266**), inflammatory response (**GO:0006954**), acute inflammatory response (GO:0002526), interleukin-1-mediated signaling (**GO:0070498**), IL-1β production (GO:0032611), response to granulocyte colony-stimulating factor (GO:0097011), positive regulation of neutrophil activation.

**Cell types / CL suggestions:** **neutrophil** (**CL:0000775**), immature/band neutrophil (**CL:0000776**), myeloid cell / immature myeloid cell (histiocytoid variant), macrophage (**CL:0000235**, M2 CL:0000890), dermal microvascular endothelial cell, keratinocyte (bystander).

**Immune-system framing:** SS sits on the **autoinflammatory (innate-immune) spectrum** — an aberrant, antigen-nonspecific neutrophil-driven response, overlapping with pyoderma gangrenosum, Behçet disease, and the monogenic autoinflammatory syndromes (hence conceptual dismech links to an inflammasome/IL-1 or neutrophilic-dermatosis module, if one exists or is created).

**Protein dysfunction / metabolic changes:** In VEXAS, hypomorphic **UBA1** loss impairs ubiquitylation → innate-immune hyperactivation and cytoplasmic vacuoles in myeloid precursors. No general SS-wide enzyme deficiency or metabolomic/lipidomic signature is established (knowledge gap).

*Sources:* Molecular systematic review PMC11660222; *Front Immunol* 2019;10:414 (Pathogenesis of Sweet's Syndrome — **verify PMID**); PMC3953233 (anakinra/IL-1); StatPearls NBK431050.

---

## 7. Anatomical Structures Affected

**Primary organ:** **skin** (UBERON:0002097 skin of body / UBERON:0002067 dermis; reticular dermis UBERON:0004539; papillary dermis UBERON:0004538). Predilection sites: **face, neck, upper trunk, upper extremities/dorsal hands**; asymmetric; lesions favor sun-exposed/photodistributed and dorsal-hand areas.

**Secondary / extracutaneous involvement (up to ~50% of cases)** — sterile neutrophilic infiltration of:
- **Eyes** (UBERON:0000970): conjunctivitis, episcleritis, scleritis, uveitis, peripheral ulcerative keratitis.
- **Musculoskeletal**: joints (arthralgia/arthritis), sterile **osteomyelitis** (bone, UBERON:0002481), muscle (myositis).
- **Lungs** (UBERON:0002048): neutrophilic alveolitis, pleural effusion, culprit of steroid-responsive infiltrates.
- **Central nervous system** (UBERON:0000955 brain / meninges UBERON:0002360): **aseptic/neutrophilic meningitis**, encephalitis ("neuro-Sweet").
- **Heart** (UBERON:0000948): myocarditis, aortitis.
- **Liver** (UBERON:0002107), **spleen** (UBERON:0002106), **kidney** (UBERON:0002113): sterile neutrophilic infiltration; hepatic/renal involvement reported.
- **Oral/mucosa, intestine, ears**.

**Body systems:** integumentary (primary); hematologic, ophthalmic, musculoskeletal, respiratory, nervous, cardiovascular, hepatobiliary/GI (secondary).

**Subcellular (GO cellular component):** no SS-defining organellar lesion; in VEXAS, **cytoplasmic vacuoles** in myeloid precursors are the hallmark (GO:0005737 cytoplasm).

**Lateralization:** cutaneous lesions are characteristically **asymmetric**.

*Sources:* PMID:17655751; JAAD case/review on extracutaneous SS; StatPearls NBK431050.

---

## 8. Temporal Development

- **Onset:** **adult**, peak **30–60 years** (classical form 30–50 y in women); pediatric and rare congenital/familial cases exist. Pattern is **acute/abrupt** ("sudden onset" is a major diagnostic criterion) — lesions erupt over hours to days.
- **Progression / course:** individual episodes are **self-limited**; untreated lesions may persist weeks to months, but respond within days to corticosteroids. Overall course is **episodic/relapsing–remitting**, especially when tied to an ongoing driver (IBD flare, malignancy relapse, re-exposure to a culprit drug).
- **Remission:** frequently **treatment-induced** (dramatic steroid response); **spontaneous** resolution occurs, particularly in drug-induced SS after withdrawal of the agent.
- **Recurrence:** **up to ~50%**, higher in malignancy-associated and IBD-associated disease; recurrence should prompt re-evaluation for underlying/occult malignancy.
- **Critical windows:** SS as a **presenting or relapse marker of hematologic malignancy** makes the diagnostic moment a key intervention window — new/recurrent SS warrants CBC/marrow evaluation.

*Sources:* StatPearls NBK431050; PMID:17655751; cohort PMC10753595 (long-term follow-up, malignancy association, treatment response).

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence/incidence:** true population incidence undefined; considered **rare**. Institutional data: overall SS incidence ~**0.36%** among screened populations, rising to ~**0.94–1%** among **AML** patients (Karger, *Acta Haematol* 2024, 28-year AML institutional experience).
- **Sex ratio:** female predominance, classically **~4:1 (F:M)** in classical SS; the ratio **approaches 1:1 in malignancy-associated SS**.
- **Age distribution:** peak 30–60 y; mean age ~50 y in the molecular systematic review cohort (mean 50.7 y; 52% female) (PMC11660222).
- **Subtype share:** classical ~70–80%; **malignancy-associated ~15–20%** (AML > MDS > other); drug-induced a smaller fraction.

**Genetic epidemiology (limited, since mostly non-Mendelian):**
- **Inheritance:** predominantly **sporadic/multifactorial**; rare **autosomal-dominant familial SS** (OMIM 608068). **VEXAS** is **somatic, X-linked** (male-predominant, older men) — not heritable.
- **Penetrance/expressivity/anticipation/mosaicism:** not applicable to the sporadic form; VEXAS is defined by **acquired somatic mosaicism** in the myeloid lineage.
- **Founder effects/consanguinity/carrier frequency:** relevant only to the **MEFV** susceptibility axis in Mediterranean populations; no SS-specific carrier screening.
- **Population/geographic distribution:** reported worldwide; no strong ethnic predilection ("no racial predilection" per StatPearls), though some East-Asian/Japanese literature emphasizes SS–MDS and trisomy-8 overlap.

*Sources:* StatPearls NBK431050; PMC11660222; Karger *Acta Haematol* 2024;147(4):457; PMID:29107342.

---

## 10. Diagnostics

**Diagnosis is clinicopathologic**, resting on the **von den Driesch (1994) modification** of the **Su & Liu (1986)** criteria — **both major + ≥2 of 4 minor** for classical SS:

**Major criteria (both required):**
1. Abrupt onset of tender/painful erythematous plaques or nodules. **[verify snippet]**
2. Histopathology: **dense dermal neutrophilic infiltrate without leukocytoclastic vasculitis**. **[verify snippet]**

**Minor criteria (≥2 of 4):**
3. Fever >38 °C.
4. Association with underlying hematologic/visceral malignancy, inflammatory disease, pregnancy, **or** preceding respiratory/GI infection or vaccination.
5. Excellent response to systemic corticosteroids (or potassium iodide).
6. Laboratory abnormalities at presentation (**≥3 of 4**): ESR >20 mm/h; elevated CRP; leukocytosis >8,000; neutrophils >70%.

*(Drug-induced SS uses the separate Walker & Cohen 1996 criteria: temporal relation to drug, and resolution on withdrawal / recurrence on rechallenge.)*

**Laboratory (LOINC-anchorable):** CBC with differential (neutrophilia HP:0011897), **ESR** (LOINC 4537-7), **CRP** (LOINC 1988-5), often anemia/thrombocytopenia if paraneoplastic. **Biopsy is the cornerstone** — punch/incisional skin biopsy for H&E (dense dermal neutrophils, papillary edema, leukocytoclasis, no vasculitis) ± immunohistochemistry (MPO+ neutrophils; CD68/CD163 in histiocytoid variant to distinguish from leukemia cutis).

**Work-up for underlying cause (mandatory):** CBC/peripheral smear, and — given the AML/MDS link — **bone marrow examination and cytogenetics** if cytopenias, atypical/histiocytoid features, absence of arthralgia, or recurrence; malignancy screening; medication review; infection/IBD/autoimmune evaluation. **In refractory or male older-patient cases, sequence *UBA1* to exclude VEXAS.**

**Imaging/other:** guided by extracutaneous symptoms (e.g., CXR/CT for pulmonary infiltrates, MRI/LP for neuro-Sweet, echocardiography for myocarditis).

**Differential diagnosis:** cellulitis/erysipelas (sterile SS mimics infection but doesn't respond to antibiotics), pyoderma gangrenosum, leukocytoclastic vasculitis, erythema nodosum, erythema multiforme, Behçet disease, leukemia cutis, neutrophilic eccrine hidradenitis, VEXAS, bacterial/atypical infection.

**Screening:** no population screening. Key practical rule: **new-onset SS = screen for occult hematologic malignancy**, and monitor known MDS/AML patients.

*Sources:* von den Driesch PMID:8113453; Su & Liu, *Cutis* 1986 (**verify PMID:3527570**); Walker & Cohen 1996 (drug-induced criteria — **verify PMID**); StatPearls NBK431050.

---

## 11. Outcome / Prognosis

- **Classical & drug-induced SS:** generally **excellent prognosis**; rapid, often dramatic response to corticosteroids; drug-induced resolves on withdrawal. Lesions heal without scarring (except bullous/ulcerative variants).
- **Recurrence:** **up to ~50%**, especially IBD- or malignancy-associated.
- **Malignancy-associated SS:** prognosis is governed by the **underlying hematologic disease**; SS itself is steroid-responsive but recurs with tumor relapse and may herald progression. Marked cytopenias, absence of arthralgia, and histiocytoid/subcutaneous histology correlate with malignancy (PMID:29107342).
- **Mortality/morbidity:** SS is rarely directly fatal; serious morbidity/mortality arise from **extracutaneous neutrophilic organ involvement** (myocarditis, alveolitis, aseptic meningitis) and from the **associated malignancy**. Complications: corticosteroid toxicity from prolonged therapy; secondary infection of ulcerated lesions.
- **Prognostic factors:** subtype (drug-induced best; malignancy-associated worst), presence/control of underlying malignancy, degree of cytopenia, extracutaneous involvement.
- **QoL:** acute pain, fever, arthralgia; generally reversible with treatment. No SS-specific validated instrument.

*Sources:* PMC10753595 (93-patient long-term cohort); PMID:29107342; StatPearls NBK431050.

---

## 12. Treatment

Suggested **MAXO** anchor for drug therapy: pharmacotherapy (use NCIT:C15986 Pharmacotherapy per dismech convention, with CHEBI `therapeutic_agent`); MAXO:0000058? (systemic corticosteroid therapy) / MAXO:0000108? — verify exact MAXO IDs with OAK before committing.

**First-line:**
- **Systemic corticosteroids** — gold standard. Prednisone **0.5–1 mg/kg/day (≈40–60 mg/day)** tapered over **2–4 (up to 4–6) weeks**; produces rapid defervescence and lesion regression. CHEBI: prednisone CHEBI:8382, prednisolone CHEBI:8378, methylprednisolone CHEBI:6888. Topical/intralesional corticosteroids for localized disease.
- **Potassium iodide** and **colchicine** (CHEBI:23359) are recognized **alternative first-line** anti-inflammatory options, useful when steroids are contraindicated.
- **Dapsone** (CHEBI:4325) — first-line/steroid-sparing.

**Second-line / steroid-sparing / refractory:** **methotrexate**, **cyclosporine**, indomethacin, clofazimine, and — for autoinflammatory/refractory disease — **biologics targeting the cytokine core**: **IL-1 blockade (anakinra)** with documented efficacy (PMC3953233), TNF inhibitors, and emerging **JAK inhibitors** — e.g., a 2025 report of **Sweet syndrome successfully treated with upadacitinib** (PMC12547819).

**Cause-directed therapy (essential):**
- **Drug-induced:** withdraw the culprit (definitive).
- **Malignancy-associated:** treat the underlying AML/MDS; SS often remits with tumor control and flares with relapse.
- **Infection/IBD-associated:** treat/steroid-manage the underlying condition.

**Pharmacogenomics:** dapsone carries hemolysis risk in **G6PD deficiency** — screen before use (a genotype-guided safety step). No SS-specific PGx-guided efficacy markers.

**Experimental / trials:** IL-1 (anakinra, canakinumab), IL-17, and JAK-pathway agents are the active frontier; check ClinicalTrials.gov for current NCTs (no landmark SS-specific RCT exists — evidence base is case series/cohorts). For **VEXAS-driven** Sweet-like disease, treatment shifts toward the underlying clone (azacitidine, JAK inhibitors, allogeneic HSCT).

*Sources:* UpToDate (management); StatPearls NBK431050; Cohen, *Sweet's Syndrome: Review of Current Treatment Options* (**verify PMID**); PMC3953233 (anakinra); PMC12547819 (upadacitinib, 2025).

---

## 13. Prevention

- **Primary prevention:** limited — the disease is reactive. The principal preventable trigger is **drug-induced SS**: avoid/cautiously monitor known culprits (especially **G-CSF**, and rechallenge avoidance after a documented episode).
- **Secondary prevention / early detection:** recognizing SS as a **paraneoplastic sentinel** → prompt hematologic work-up enables earlier detection of AML/MDS. Surveillance of MDS/AML patients for cutaneous flares.
- **Tertiary prevention:** steroid-sparing maintenance (colchicine, dapsone, methotrexate) to **prevent recurrences** and limit long-term corticosteroid toxicity; management of the underlying IBD/autoimmune/malignant driver.
- **Immunization/public health/environmental:** not applicable (non-infectious, non-communicable).
- **Genetic counseling:** relevant only for the rare familial form and for **VEXAS** (somatic, non-heritable, but with prognostic/therapeutic implications warranting hematology referral).

*Sources:* PMID:17655751; StatPearls NBK431050.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Sweet syndrome is essentially a **human** (NCBITaxon:9606) diagnosis. There is **no well-established naturally occurring homolog** in companion animals or wildlife catalogued in OMIA; "sterile neutrophilic dermatosis" and **sterile neutrophilic dermatosis/"Sweet's-like" syndromes have been described anecdotally in dogs** (canine, NCBITaxon:9615) but are not a defined OMIA Mendelian entry.
- **Orthologous genes:** *UBA1* and *MEFV* have clear mammalian orthologs (mouse *Uba1*, *Mefv*), enabling mechanistic study of ubiquitylation and pyrin-inflammasome biology, but not disease modeling of SS per se.
- **Comparative biology / evolutionary conservation:** the **neutrophil-recruitment and IL-1/inflammasome machinery** driving SS is deeply conserved across vertebrates, which is why cross-species mechanistic work is informative even without a natural animal counterpart.
- **Zoonotic potential:** none (non-infectious).

*Sources:* OMIA (absence of a defined entry); general veterinary dermatology literature (canine sterile neutrophilic dermatosis, MODEL_ORGANISM/case-level).

---

## 15. Model Organisms

Sweet syndrome has **no single canonical animal model** that faithfully reproduces the full syndrome — a genuine limitation to flag in the dismech entry.

- **Relevant genetic models (mechanism, not whole-disease):**
  - ***UBA1* / VEXAS models:** conditional/hematopoietic *Uba1* hypomorph and zebrafish *uba1* models recapitulate innate-immune hyperactivation and vacuolization, informing VEXAS/Sweet-like neutrophilic dermatosis. (IN_VITRO/MODEL_ORGANISM.)
  - ***Mefv* (pyrin) models:** knock-in mice model inflammasome-driven neutrophilic autoinflammation, relevant to the IL-1 axis of SS.
  - **G-CSF / CSF3–CSF3R transgenic or administration models:** exogenous G-CSF drives neutrophilia and can precipitate neutrophilic-dermatosis-like infiltration, mirroring drug-induced SS.
- **Induced / in vitro models:** patient-derived neutrophils and skin explants have been used to demonstrate the **IL-1β/G-CSF/IL-8 cytokine profile** and the **PIK3R1 gain-of-function → enhanced neutrophil migration** phenotype (PMC11660222; IN_VITRO). iPSC-derived myeloid systems are a plausible platform for VEXAS-associated neutrophilic dermatosis.
- **Phenotype recapitulation / limitations:** models capture **components** (neutrophilia, IL-1/inflammasome activation, myeloid clonality) but **not** the integrated clinical syndrome (acute tender plaques + fever + steroid responsiveness). Reactive/paraneoplastic biology is hard to model in a single organism.
- **Resources:** MGI (mouse *Uba1*, *Mefv*, *Csf3/Csf3r*), ZFIN (zebrafish *uba1*), IMPC/IMSR for alleles.

*Sources:* PMC11660222 (functional neutrophil studies, PIK3R1); VEXAS mechanistic literature; MGI/ZFIN gene records.

---

## Consolidated Evidence Table (top curatable citations)

| Claim area | Reference | ID (verify snippet before commit) | Evidence source |
|---|---|---|---|
| Original description; disease definition | Sweet RD, *Br J Dermatol* 1964 | **PMID:14201182** | HUMAN_CLINICAL |
| Comprehensive review; subtypes; criteria | Cohen PR, *Orphanet J Rare Dis* 2007;2:34 | **PMID:17655751** (PMC1963326) | HUMAN_CLINICAL (review) |
| Revised diagnostic criteria | von den Driesch P, *JAAD* 1994 | **PMID:8113453** | HUMAN_CLINICAL |
| Molecular/cytokine mechanisms; PIK3R1; stats | Molecular Characteristics of SS: Systematic Review, 2024 | **PMC11660222** | multiple (review) |
| Malignancy vs non-malignancy features (n=83) | Retrospective cohort 2018 | **PMID:29107342** | HUMAN_CLINICAL |
| 93-patient cohort, autoinflammatory/malignancy, follow-up | Cohort | **PMC10753595** | HUMAN_CLINICAL |
| SS in AML, 28-yr institutional (~0.94–1%) | *Acta Haematol* 2024;147:457 | Karger (verify PMID) | HUMAN_CLINICAL |
| VEXAS skin manifestations & UBA1 genotype | 2024 | **PMC11170453** | HUMAN_CLINICAL |
| MEFV compound-het in SS | Case report | **PMC4599868** | HUMAN_CLINICAL |
| IL-1 blockade (anakinra) | Abstract/report | **PMC3953233** | HUMAN_CLINICAL |
| JAK inhibitor (upadacitinib) success | 2025 | **PMC12547819** | HUMAN_CLINICAL |
| Clinical overview; epidemiology; treatment dosing | StatPearls | **NBK431050** | secondary/reference |

---

## Key gaps flagged for the dismech entry
1. **Epigenetics, metabolomics, lipidomics** of SS are essentially undefined — mark as KNOWLEDGE_GAP.
2. **No faithful whole-disease animal model** — a HUMAN_MODEL_MISMATCH candidate (mechanistic models exist; translational fidelity to the integrated syndrome is unproven).
3. **VEXAS as a molecular genocopy** is the most important recent conceptual shift — consider a conforming link between Sweet syndrome and a VEXAS/*UBA1* autoinflammatory entry, and an IL-1/inflammasome or neutrophilic-dermatosis mechanism module if one exists or is worth creating.
4. **All snippets marked [verify snippet]** are paraphrases and must be replaced with exact abstract quotes via `just fetch-reference` + `just validate-references` before committing evidence items.

**Sources (primary URLs):**
- [Sweet's syndrome comprehensive review (Cohen 2007, PMC1963326)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1963326/)
- [Molecular Characteristics of Sweet Syndrome: Systematic Review (PMC11660222)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11660222/)
- [Sweet Syndrome — StatPearls (NBK431050)](https://www.ncbi.nlm.nih.gov/books/NBK431050/)
- [Sweet syndrome in patients with/without malignancy, n=83 (PMID:29107342)](https://pubmed.ncbi.nlm.nih.gov/29107342/)
- [93-patient cohort with long-term follow-up (PMC10753595)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10753595/)
- [VEXAS skin manifestations & UBA1 genotypes (PMC11170453)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11170453/)
- [MEFV compound heterozygous mutations in Sweet's (PMC4599868)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4599868/)
- [Anakinra for Sweet syndrome (PMC3953233)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3953233/)
- [Upadacitinib for Sweet syndrome, 2025 (PMC12547819)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12547819/)
- [SS in AML, 28-year experience (Acta Haematologica 2024)](https://karger.com/aha/article/147/4/457/870132/)
- [Orphanet ORPHA:3243](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=3243)
- [MONDO:0011959 (Monarch)](https://monarchinitiative.org/MONDO:0011959)

---

**A quick note on how to use this, since it feeds a KB:** think of Sweet syndrome less like a single broken gene and more like a fire alarm that's wired too sensitive — the neutrophils are the sprinklers, and G-CSF plus the IL-1 inflammasome are the trigger circuit. The *cause* (infection, drug, or a smoldering myeloid clone) is the smoke. That framing maps cleanly onto a causal chain for the pathophysiology nodes: **trigger → G-CSF/IL-1 cytokine surge → chemokine-driven neutrophil recruitment → sterile dermal infiltrate → plaques + fever**, with the malignancy-associated arm branching off toward the clonal myeloid/VEXAS biology. Want me to go ahead and draft the actual `Sweet_Syndrome.yaml` pathophysiology/evidence blocks from this (running the fetch-reference + validation loop as I go), or leave it as the research brief?